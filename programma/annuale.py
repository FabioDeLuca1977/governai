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

    righe, gen_mis = [], {}
    for y in ANNI:
        spesa = {}
        gen_mis[y] = {}
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
                if fid in GENERALI:
                    pid = chiave.split(":")[0]
                    gen_mis[y][pid] = gen_mis[y].get(pid, 0.0) + quota
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
    t = pd.DataFrame(righe)
    t.attrs["gen_mis"] = gen_mis
    return t


def piano(etichetta: str = "intermedio") -> dict | None:
    """Calendario di avvio (scelte del 13 novembre 2026, corrette dopo il secondo giro di revisione).

    Ogni anno la spesa sulle risorse generali non supera il gettito dell'anno (ipotesi prudente), al netto di:
    - 0,04 mld per i servizi gratuiti per smettere di fumare, dal primo anno dell'accisa sul tabacco (2028);
    - 0,02 mld di riserva per le misure pagate con i fondi europei dopo il 2029, accantonati dal 2030 (0,05 fino alla
      correzione della copertura RA03 del 13 novembre 2026).
    Ordine di avvio, in tre gruppi:
    1. riforme a costo quasi zero (al massimo 20 milioni l'anno sulle risorse generali): partono subito per intero;
    2. nucleo robusto (Carta, regola 7), sperimentazioni (devono produrre la valutazione entro il 2029), compensazione
       dell'autotrasporto per il taglio del gasolio agevolato (04-P8) e squadre infermieristiche di quartiere (06-C8);
    3. le altre misure, tutte nella stessa proporzione.
    I fondi europei 2021-2027 non fanno da ponte per la spesa corrente: possono pagare solo spese una tantum, già
    contate sulla coesione. Se in un anno la spesa sulla coesione supera la capienza del registro, l'eccedenza slitta."""
    t = conti(etichetta)
    if t is None:
        return None
    esito = pd.read_csv(RADICE / "motore" / "esito_proposte.csv")
    sel = pd.read_csv(QUI / f"selezione_{etichetta}.csv")
    piloti = set(sel[(sel.tipo == "variante") & (sel.scelta == 1) & (sel.variante.str.upper() == "PILOTA")].proposta_id)
    nucleo_carta = set(esito.proposta_id[esito.classe == "robusta"])
    PRIMA = {"04-P8", "06-C8"}
    gruppo2 = nucleo_carta | piloti | PRIMA
    massimo = {}
    for y in ANNI:
        for p, x in t.attrs["gen_mis"][y].items():
            massimo[p] = max(massimo.get(p, 0.0), x)
    gruppo1 = {p for p, x in massimo.items() if x <= 0.02 + 1e-9}
    gruppo2 -= gruppo1
    reg = pd.read_csv(RADICE / "registro" / "fondi.csv").set_index("fondo_id")
    cap_coe = float(reg.loc[COESIONE, "capienza_min"]) if COESIONE in reg.index else 0.0
    anni, quote = [], {}
    for r in t.itertuples():
        mis = t.attrs["gen_mis"][r.anno]
        fumo = 0.04 if r.anno >= 2028 else 0.0
        riserva = 0.02 if r.anno >= 2030 else 0.0
        disp = max(0.0, r.gettito_generali - fumo - riserva)
        fatt = {}
        for k, g in (("g1", gruppo1), ("g2", gruppo2), ("g3", None)):
            dom = sum(x for p, x in mis.items() if (p in g if g is not None else p not in gruppo1 | gruppo2))
            f = min(1.0, disp / dom) if dom > 0 else 1.0
            fatt[k] = f
            disp -= dom * f
        gr = lambda p: "g1" if p in gruppo1 else ("g2" if p in gruppo2 else "g3")
        avviata = sum(x * fatt[gr(p)] for p, x in mis.items())
        prevista = sum(mis.values())
        coe_extra = max(0.0, r.coesione - cap_coe) if r.anno <= 2029 else 0.0
        rinv_nucleo = sum(x * (1 - fatt[gr(p)]) for p, x in mis.items() if p in nucleo_carta)
        anni.append({"anno": r.anno, "prevista": round(prevista, 2), "avviata": round(avviata, 2),
                     "gettito": r.gettito_generali, "fumo": fumo, "riserva": riserva, "ponte_ue": 0.0,
                     "quota_riforme": round(fatt["g1"], 2) + 0.0, "quota_nucleo": round(fatt["g2"], 2) + 0.0, "quota_altre": round(fatt["g3"], 2) + 0.0,
                     "rinviata": round(prevista - avviata, 2), "rinviata_nucleo": round(rinv_nucleo, 2),
                     "coesione_rinviata": round(coe_extra, 2)})
        for p, x in mis.items():
            q = quote.setdefault(p, {"nucleo": p in gruppo1 | gruppo2, "gruppo": gr(p), "anni": {}})
            q["anni"][r.anno] = round(fatt[gr(p)], 2)
            q["spesa_max"] = round(max(q.get("spesa_max", 0.0), x), 3)
    tot = lambda k: round(sum(a[k] for a in anni), 2)
    return {"anni": anni, "misure": quote, "ponte_totale": 0.0, "rinviata_totale": tot("rinviata"),
            "rinviata_nucleo": tot("rinviata_nucleo"), "coesione_rinviata": tot("coesione_rinviata"),
            "riforme_subito": sorted(gruppo1)}


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


def calendario_md(pi: dict | None) -> str:
    if not pi:
        return ""
    righe = ["", "## Calendario di avvio (scelte del 13 novembre 2026)", "",
             "Ogni anno la spesa sulle risorse generali non supera il gettito dell'anno (ipotesi prudente), al netto dei servizi "
             "per smettere di fumare (0,04 mld dal 2028) e della riserva per il dopo 2029 (0,02 mld dal 2030). Partono subito le "
             "riforme a costo quasi zero; poi il nucleo robusto, le sperimentazioni, 04-P8 e 06-C8; poi le altre misure. I fondi "
             "europei 2021-2027 pagano solo spese una tantum, non spesa corrente.", "",
             "| Anno | Spesa prevista sulle risorse generali | Spesa avviata | Rinviata | di cui nucleo | Riforme a costo quasi zero | Nucleo e primo gruppo | Altre misure |",
             "|---|---|---|---|---|---|---|---|"]
    for a in pi["anni"]:
        righe.append(f"| {a['anno']} | {num(a['prevista'])} | {num(a['avviata'])} | {num(a['rinviata'])} | {num(a['rinviata_nucleo'])} | "
                     f"{a['quota_riforme']:.0%} | {a['quota_nucleo']:.0%} | {a['quota_altre']:.0%} |")
    righe += ["", f"In tutto slittano {num(pi['rinviata_totale'])} mld di spesa negli anni di passaggio, di cui {num(pi['rinviata_nucleo'])} "
                  f"del nucleo robusto; sulla coesione slittano {num(pi['coesione_rinviata'])} mld di spese una tantum oltre la capienza.", ""]
    return "\n".join(righe)


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    for e in (sys.argv[1:] or ["intermedio"]):
        t = conti(e)
        if t is None:
            print(f"{e}: selezione non trovata"); continue
        testo = rapporto(e, t, conti(e, anticipo=1))
        pi = piano(e)
        testo += calendario_md(piano(e))
        (QUI / f"annuale_{e}.md").write_text(testo, encoding="utf-8")
        neg = t[t.saldo_generali < -0.005]
        print(f"{e}: " + (f"scoperto sulle risorse generali in {', '.join(map(str, neg.anno))} "
                          f"(massimo {-neg.saldo_generali.min():.2f} mld)" if len(neg) else "nessun anno scoperto"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
