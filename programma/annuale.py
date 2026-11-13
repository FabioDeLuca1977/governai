"""Conti anno per anno (2027-2035) di uno scenario del programma.

L'ottimizzatore controlla il vincolo di bilancio a regime: spesa a regime <= gettito minimo a regime.
Negli anni di passaggio può non bastare: alcune spese partono prima che le coperture rendano a pieno.
Questo controllo rifà il conto per ogni anno, con regole semplici e dichiarate:

Spesa di una variante nell'anno y
- 2027, 2028, 2029: le colonne costo_2027, costo_2028, costo_2029 delle varianti;
- dal 2030: costo_regime se anno_regime <= 2029; altrimenti crescita lineare da costo_2029 a costo_regime
  nell'anno anno_regime.
- La spesa di ogni anno si divide tra i fondi in proporzione a prelievo_regime. Se nel 2027-29 la spesa
  supera quella a regime, l'eccedenza è considerata una tantum sui fondi europei di coesione 2021-2027
  (è il caso di investimenti e formazione iniziale scritti nelle note delle varianti).
- Dal 2030 la spesa sulla coesione 2021-2027 finisce. Le voci classificate "successore" in
  programma/coesione_dopo_2029.csv restano necessarie e sono contate a parte, come spesa da rifinanziare.

Gettito di una copertura nell'anno y
- gettito_min cresce in modo lineare in `gradualita` anni e arriva al pieno in anno_regime:
  quota = (y - (anno_regime - gradualita)) / gradualita, tra 0 e 1 (ipotesi prudente).
- Ipotesi favorevole: le stesse rampe partono un anno prima (coperture approvate con la prima legge di bilancio
  e attive dal primo anno). Il rapporto mostra entrambe.

Saldo
- risorse generali (SAD, SPESE_FISCALI, ACCISE_SALUTE, RIORDINO_BONUS, RIALLOCAZIONE): gettito - spesa;
- gli altri fondi vincolati: gettito più capienza del registro, meno spesa, fondo per fondo;
- le tariffe sono fuori bilancio.

È una stima: le rampe vere dipendono dalle norme attuative e vanno verificate con la Ragioneria.

Uso:  python annuale.py [etichetta ...]     (default: intermedio; scrive programma/annuale_<etichetta>.md)
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

QUI = Path(__file__).resolve().parent
RADICE = QUI.parent
ANNI = list(range(2027, 2036))
GENERALI = {"SAD", "SPESE_FISCALI", "ACCISE_SALUTE", "RIORDINO_BONUS", "RIALLOCAZIONE"}
FUORI_BILANCIO = {"TARIFFE"}
COESIONE = "COESIONE_2127"


def _varianti() -> pd.DataFrame:
    v = pd.concat([pd.read_csv(f) for f in sorted((QUI / "varianti").glob("*.csv"))], ignore_index=True)
    v["variante"] = v.variante.str.upper().str.strip()
    v["fondo_id"] = v.fondo_id.str.upper().str.strip()
    v["chiave"] = v.proposta_id + ":" + v.variante
    for c in ["costo_2027", "costo_2028", "costo_2029", "costo_regime", "prelievo_regime", "anno_regime"]:
        v[c] = pd.to_numeric(v[c], errors="coerce").fillna(0.0)
    return v


def costo_anno(r, y: int) -> float:
    if y <= 2029:
        return float(getattr(r, f"costo_{y}"))
    if r.anno_regime <= 2029 or y >= r.anno_regime:
        return float(r.costo_regime)
    passi = r.anno_regime - 2029
    return float(r.costo_2029 + (r.costo_regime - r.costo_2029) * (y - 2029) / passi)


def gettito_anno(r, y: int, anticipo: int = 0) -> float:
    g = max(int(r.gradualita) if pd.notna(r.gradualita) else 1, 1)
    inizio = int(r.anno_regime) - g - anticipo
    return float(r.gettito_min) * min(1.0, max(0.0, (y - inizio) / g))


def conti(etichetta: str = "intermedio", anticipo: int = 0) -> pd.DataFrame | None:
    f = QUI / f"selezione_{etichetta}.csv"
    if not f.exists():
        return None
    s = pd.read_csv(f)
    scelte = set(s[(s.tipo == "variante") & (s.scelta == 1)].chiave)
    cop = s[(s.tipo == "copertura") & (s.scelta == 1)].copy()
    cop["fondo_id"] = cop.fondo_id.str.upper().str.strip()
    v = _varianti()
    v = v[v.chiave.isin(scelte)]
    regole = pd.read_csv(QUI / "coesione_dopo_2029.csv").set_index("proposta_id") \
        if (QUI / "coesione_dopo_2029.csv").exists() else pd.DataFrame()
    reg = pd.read_csv(RADICE / "registro" / "fondi.csv")
    cap = {r.fondo_id.upper(): float(pd.to_numeric(r.capienza_min, errors="coerce") or 0.0) for r in reg.itertuples()}
    fondi_menu = set(cop.fondo_id) | set(pd.read_csv(QUI / "coperture_menu.csv").fondo_id.str.upper().str.strip())

    righe = []
    for y in ANNI:
        spesa = {}
        da_rifinanziare = 0.0
        for chiave, g in v.groupby("chiave"):
            r0 = g.iloc[0]
            tot = costo_anno(r0, y)
            base = g.prelievo_regime.sum()
            extra = 0.0
            if y <= 2029 and tot > r0.costo_regime + 1e-9:
                extra, tot_rip = tot - r0.costo_regime, r0.costo_regime
            else:
                tot_rip = tot
            for i, r in enumerate(g.itertuples()):
                quota = tot_rip * (r.prelievo_regime / base) if base > 0 else (tot_rip if i == 0 else 0.0)
                fid = r.fondo_id
                if fid == COESIONE and y >= 2030:
                    pid, var = chiave.split(":")
                    esito = "valutazione" if var == "PILOTA" else (regole.loc[pid, "esito"] if pid in regole.index else "da_decidere")
                    if esito in ("successore", "da_decidere"):
                        da_rifinanziare += quota
                    continue
                spesa[fid] = spesa.get(fid, 0.0) + quota
            if extra and y <= 2029:
                spesa[COESIONE] = spesa.get(COESIONE, 0.0) + extra
        gett = {}
        for r in cop.itertuples():
            gett[r.fondo_id] = gett.get(r.fondo_id, 0.0) + gettito_anno(r, y, anticipo)
        sp_gen = sum(x for k, x in spesa.items() if k in GENERALI)
        ge_gen = sum(x for k, x in gett.items() if k in GENERALI)
        vincolati = 0.0
        for fid in set(spesa) | set(gett):
            if fid in GENERALI or fid in FUORI_BILANCIO:
                continue
            c = 0.0 if fid in fondi_menu else cap.get(fid, 0.0)
            if fid == COESIONE:
                c = cap.get(fid, 0.0) if y <= 2029 else 0.0
            vincolati += min(0.0, gett.get(fid, 0.0) + c - spesa.get(fid, 0.0))
        righe.append({"anno": y, "spesa": round(sum(spesa.values()), 2), "spesa_generali": round(sp_gen, 2),
                      "gettito_generali": round(ge_gen, 2), "saldo_generali": round(ge_gen - sp_gen, 2),
                      "coesione": round(spesa.get(COESIONE, 0.0), 2), "da_rifinanziare": round(da_rifinanziare, 2),
                      "scoperto_vincolati": round(vincolati, 2)})
    return pd.DataFrame(righe)


def num(x: float, d: int = 2) -> str:
    return f"{x:.{d}f}".replace(".", ",").replace("-", "−")


def rapporto(etichetta: str, t: pd.DataFrame, tf: pd.DataFrame) -> str:
    neg = t[t.saldo_generali < -0.005]
    negf = tf[tf.saldo_generali < -0.005]
    out = [f"# Conti anno per anno: scenario {etichetta}", "",
           "*Generato da `programma/annuale.py`. Stima: le regole di calcolo sono scritte all'inizio dello script.*", "",
           "| Anno | Spesa | di cui risorse generali | Gettito risorse generali | Saldo risorse generali (prudente) | Saldo (favorevole) | Coesione 2021-27 | Da rifinanziare dopo il 2029 |",
           "|---|---|---|---|---|---|---|---|"]
    for r, f in zip(t.itertuples(), tf.itertuples()):
        out.append(f"| {r.anno} | {num(r.spesa)} | {num(r.spesa_generali)} | {num(r.gettito_generali)} | "
                   f"**{num(r.saldo_generali)}** | {num(f.saldo_generali)} | {num(r.coesione)} | {num(r.da_rifinanziare)} |")
    out += ["", "## In breve", ""]
    if neg.empty:
        out.append("- Le risorse generali coprono la spesa in ogni anno.")
    else:
        anni = ", ".join(str(a) for a in neg.anno)
        out.append(f"- **Anni scoperti sulle risorse generali: {anni}.** Lo scoperto massimo è di "
                   f"{num(-neg.saldo_generali.min())} mld ({int(neg.loc[neg.saldo_generali.idxmin(), 'anno'])}); "
                   f"in tutto {num(-neg.saldo_generali.sum())} mld negli anni scoperti (ipotesi prudente).")
    if not negf.empty:
        out.append(f"- Anche con l'ipotesi favorevole restano scoperti {', '.join(str(a) for a in negf.anno)}: "
                   f"massimo {num(-negf.saldo_generali.min())} mld, in tutto {num(-negf.saldo_generali.sum())} mld.")
    out.append(f"- Dal 2030 vanno rifinanziati {num(t[t.anno == 2030].da_rifinanziare.iloc[0])} mld l'anno di spesa oggi pagata con la coesione 2021-2027.")
    if (t.scoperto_vincolati < -0.005).any():
        out.append("- Alcuni fondi vincolati non bastano in qualche anno: colonna `scoperto_vincolati` nel calcolo.")
    return "\n".join(out) + "\n"


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    for e in (sys.argv[1:] or ["intermedio"]):
        t = conti(e)
        if t is None:
            print(f"{e}: selezione non trovata"); continue
        (QUI / f"annuale_{e}.md").write_text(rapporto(e, t, conti(e, anticipo=1)), encoding="utf-8")
        neg = t[t.saldo_generali < -0.005]
        print(f"{e}: " + (f"scoperto sulle risorse generali in {', '.join(map(str, neg.anno))} "
                          f"(massimo {-neg.saldo_generali.min():.2f} mld)" if len(neg) else "nessun anno scoperto"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
