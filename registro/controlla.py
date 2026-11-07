"""Controllo automatico del registro delle coperture di GovernAI.

Somma i prelievi di tutte le proposte su ogni fondo, li confronta con la
capienza verificata e calcola la parte del programma che resta scoperta.
Due scenari:
  - ottimistico: costi minimi, capienze massime, risparmi attesi accettati;
  - prudente:   costi massimi, capienze minime, nessuna risorsa che richiede
                certificazione ex post, nessun risparmio atteso non certificato.
Scrive bilancio.md accanto a questo file.

Uso:  python controlla.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

QUI = Path(__file__).resolve().parent
TOLL = 0.011  # tolleranza di arrotondamento (mld)

FONDI_AMMESSI = {
    "SAD", "SPESE_FISCALI", "ETS", "ETS2_FSC", "IVA_EVASIONE", "FSN", "COESIONE_2127",
    "COESIONE_2834", "PENSIONI", "TASSA_SOGGIORNO", "ACCISE_SALUTE", "RIORDINO_BONUS",
    "FONDI_UE", "RIALLOCAZIONE", "RISPARMI_ATTESI", "TARIFFE", "DEFICIT", "ALTRO",
}


def carica() -> tuple[pd.DataFrame, pd.DataFrame]:
    fondi = pd.read_csv(QUI / "fondi.csv")
    prel = pd.read_csv(QUI / "prelievi.csv")
    for c in ["capienza_min", "capienza_max", "gia_impegnato"]:
        fondi[c] = pd.to_numeric(fondi[c], errors="coerce")
    for c in ["costo_min", "costo_max", "prelievo_min", "prelievo_max"]:
        prel[c] = pd.to_numeric(prel[c], errors="coerce").fillna(0.0)
    fondi["certificazione"] = fondi["certificazione"].astype(str).str.lower().str.strip()
    fondi["in_bilancio"] = fondi["in_bilancio"].astype(str).str.lower().str.strip()
    return fondi, prel


def valida(fondi: pd.DataFrame, prel: pd.DataFrame) -> list[str]:
    avvisi = []
    sconosciuti = set(prel.fondo_id) - FONDI_AMMESSI
    if sconosciuti:
        avvisi.append(f"fondo_id non ammessi in prelievi.csv: {sorted(sconosciuti)}")
    mancanti = set(prel.fondo_id) - set(fondi.fondo_id)
    if mancanti:
        avvisi.append(f"fondi usati ma senza capienza in fondi.csv (trattati come capienza zero): {sorted(mancanti)}")
    per_prop = prel.groupby("proposta_id").agg(
        costo_min=("costo_min", "first"), costo_max=("costo_max", "first"),
        p_min=("prelievo_min", "sum"), p_max=("prelievo_max", "sum"))
    for pid, r in per_prop.iterrows():
        if abs(r.costo_min - r.p_min) > TOLL or abs(r.costo_max - r.p_max) > TOLL:
            avvisi.append(f"{pid}: prelievi ({r.p_min:.2f}–{r.p_max:.2f}) diversi dal costo ({r.costo_min:.2f}–{r.costo_max:.2f})")
    return avvisi


def capienza(f: pd.Series | None, scenario: str, richiesto: float) -> float:
    """Capienza effettivamente utilizzabile di un fondo nello scenario dato."""
    if f is None:
        return 0.0
    fid = f.fondo_id
    illimitato = pd.isna(f.capienza_max) or f.capienza_max == float("inf")
    if fid == "TARIFFE" or (f.in_bilancio == "no" and illimitato):
        return richiesto  # fuori bilancio senza tetto: non pesa sui conti pubblici
    # i fondi fuori bilancio con capienza (es. prestiti UE) restano limitati dalla capienza
    if fid == "RISPARMI_ATTESI":
        return richiesto if scenario == "ottimistico" else 0.0
    if scenario == "prudente" and f.certificazione == "si":
        return 0.0
    cap = f.capienza_max if scenario == "ottimistico" else f.capienza_min
    if pd.isna(cap):
        return richiesto if scenario == "ottimistico" else 0.0
    return max(float(cap), 0.0)


def analizza(fondi: pd.DataFrame, prel: pd.DataFrame) -> dict:
    idx = {r.fondo_id: r for r in fondi.itertuples(index=False)}
    out = {}
    for scenario, col in [("ottimistico", "prelievo_min"), ("prudente", "prelievo_max")]:
        richieste = prel.groupby("fondo_id")[col].sum()
        righe = []
        for fid, rich in richieste.sort_values(ascending=False).items():
            f = idx.get(fid)
            cap = capienza(pd.Series(f._asdict()) if f is not None else None, scenario, rich)
            eccesso = max(rich - cap, 0.0)
            fuori = fid == "TARIFFE" or (f is not None and f.in_bilancio == "no")
            righe.append({"fondo_id": fid, "richiesto": float(rich), "capienza": float(cap), "eccesso": eccesso,
                          "fuori_bilancio": fuori,
                          "uso_pct": (rich / cap * 100) if cap > 0 else float("inf") if rich > 0 else 0.0})
        tab = pd.DataFrame(righe)
        # Le proposte che pescano da un fondo in eccesso restano scoperte pro quota
        quota_scoperta = {r.fondo_id: (r.eccesso / r.richiesto if r.richiesto > 0 else 0) for r in tab.itertuples()}
        p = prel.assign(scoperto=prel[col] * prel.fondo_id.map(quota_scoperta).fillna(0))
        per_prop = p.groupby(["proposta_id", "titolo"], as_index=False, sort=False).agg(
            costo=(col, "sum"), scoperto=("scoperto", "sum"))
        per_prop = per_prop[per_prop.scoperto > TOLL].sort_values("scoperto", ascending=False)
        out[scenario] = {"fondi": tab, "proposte": per_prop,
                         "costo_totale": prel[col].sum(), "scoperto": tab.eccesso.sum()}
    return out


def md_tabella(df: pd.DataFrame, colonne: dict[str, str]) -> str:
    def fmt(v):
        if isinstance(v, float):
            return "∞" if v == float("inf") else f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        return str(v)
    head = "| " + " | ".join(colonne.values()) + " |"
    sep = "|" + "|".join("---" for _ in colonne) + "|"
    body = ["| " + " | ".join(fmt(r[c]) for c in colonne) + " |" for _, r in df.iterrows()]
    return "\n".join([head, sep, *body])


def num(v: float, dec: int = 1) -> str:
    return f"{v:,.{dec}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def stato(r) -> str:
    if r.eccesso > TOLL:
        return "🔴 esaurito"
    if r.fuori_bilancio:
        return "⚪ fuori bilancio"
    if r.uso_pct > 80:
        return "🟡 quasi pieno"
    return "🟢 ok"


def scrivi(ris: dict, avvisi: list[str], prel: pd.DataFrame, difesa: str | None) -> str:
    righe = ["# GovernAI — Esito del registro delle coperture", "",
             "*File generato da `controlla.py`. Non modificare a mano: modificare `fondi.csv` o `prelievi.csv` e rieseguire.*", "",
             f"Proposte nel registro: **{prel.proposta_id.nunique()}**, righe di prelievo: **{len(prel)}**. Importi in mld €/anno a regime.", ""]
    righe += ["## Riepilogo", "",
              "| Scenario | Costo totale | Coperto | **Scoperto** |", "|---|---|---|---|"]
    for sc in ["ottimistico", "prudente"]:
        r = ris[sc]
        righe.append(f"| {sc.capitalize()} | {num(r['costo_totale'])} | {num(r['costo_totale'] - r['scoperto'])} | **{num(r['scoperto'])}** |")
    righe += ["", "- **Ottimistico**: costi minimi, capienze massime, risparmi attesi accettati.",
              "- **Prudente**: costi massimi, capienze minime, nessuna risorsa da certificare ex post (es. evasione), nessun risparmio non certificato.", ""]
    if difesa:
        righe += [difesa, ""]
    for sc in ["prudente", "ottimistico"]:
        r = ris[sc]
        t = r["fondi"].copy()
        t["stato"] = t.apply(stato, axis=1)
        righe += [f"## Fondi — scenario {sc}", "",
                  md_tabella(t, {"fondo_id": "Fondo", "richiesto": "Richiesto", "capienza": "Capienza", "eccesso": "Eccesso", "stato": "Stato"}), ""]
        if len(r["proposte"]):
            righe += [f"### Proposte scoperte — scenario {sc}", "",
                      md_tabella(r["proposte"], {"proposta_id": "Proposta", "titolo": "Titolo", "costo": "Costo", "scoperto": "Scoperto"}), ""]
    if avvisi:
        righe += ["## Avvisi di coerenza", "", *[f"- {a}" for a in avvisi], ""]
    return "\n".join(righe)


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")  # la console di Windows non è UTF-8 di default
    fondi, prel = carica()
    avvisi = valida(fondi, prel)
    # La Difesa ha una scala diversa da tutto il resto: si mostra anche il saldo senza di essa
    is_dif = prel.proposta_id.str.upper().str.startswith("07-C5")
    ris = analizza(fondi, prel)
    nota_dif = None
    if is_dif.any():
        senza = analizza(fondi, prel[~is_dif])
        nota_dif = ("**Senza la proposta Difesa (07-C5)** lo scoperto è "
                    f"{num(senza['ottimistico']['scoperto'])} (ottimistico) – {num(senza['prudente']['scoperto'])} (prudente) mld/anno.")
    testo = scrivi(ris, avvisi, prel, nota_dif)
    (QUI / "bilancio.md").write_text(testo, encoding="utf-8")
    for sc in ["ottimistico", "prudente"]:
        print(f"{sc:12s} costo {ris[sc]['costo_totale']:6.1f}  scoperto {ris[sc]['scoperto']:6.1f}")
    if nota_dif:
        print(nota_dif.replace("**", ""))
    print(f"avvisi: {len(avvisi)}  ->  bilancio.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
