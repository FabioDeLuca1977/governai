"""Validazione completa di un programma proposto con la pagina "Proponi un programma" del sito.

Stesse regole del programma di GovernAI, nessuna eccezione:
1. conti a regime: un vincolo per le risorse generali, uno per ogni fondo vincolato, coperture legate (ottimizza.py);
2. linee rosse automatiche: panel, verifica giuridica, coperture regressive senza compensazione;
3. conti anno per anno dal 2027 al 2035 con lo stesso calendario di avvio (annuale.py);
4. robustezza sui valori: su migliaia di pesi diversi tra i valori (SMAA, motore/decidi.py), quante volte il programma
   proposto fa meglio del programma intermedio.

Uso:
    python programma/valida_proposta.py "https://.../#/programma/proponi?n=Nome&m=01-P1.E,02-C2.P&c=AS01,SF06"
    python programma/valida_proposta.py "<link>" --pubblica 12   (12 = numero della issue; scrive in proposte/)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path
from urllib.parse import parse_qs, unquote

import numpy as np
import pandas as pd

QUI = Path(__file__).resolve().parent
RADICE = QUI.parent
sys.path.insert(0, str(QUI))
import annuale  # noqa: E402
import ottimizza  # noqa: E402
from ottimizza import decidi  # noqa: E402

LETTERE = {"P": "PIENA", "E": "ESSENZIALE", "T": "PILOTA", "Z": "ZERO"}
ETICHETTA = "_verifica"


def decodifica(link: str) -> tuple[str, list[str], list[str]]:
    q = link.split("?", 1)[-1]
    p = {k: v[0] for k, v in parse_qs(q, keep_blank_values=True).items()}
    nome = unquote(p.get("n", "")).strip() or "Senza nome"
    misure = []
    for t in filter(None, p.get("m", "").split(",")):
        pid, _, l = t.partition(".")
        if l not in LETTERE:
            sys.exit(f"variante non riconosciuta: {t}")
        misure.append(f"{pid}:{LETTERE[l]}")
    return nome, misure, [c for c in p.get("c", "").split(",") if c]


def slug(t: str) -> str:
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:50] or "programma"


def num(x: float, d: int = 2) -> str:
    return f"{x:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("link")
    ap.add_argument("--pubblica", metavar="ISSUE", default="", help="scrive l'esito in proposte/ (numero della issue)")
    ap.add_argument("--n", type=int, default=2000, help="combinazioni di pesi per la robustezza")
    a = ap.parse_args()
    nome, misure, cop = decodifica(a.link)

    var, menu = ottimizza.carica_varianti(), ottimizza.carica_menu()
    cap = ottimizza.capienze_base(menu)
    chiavi, A, lb, ub, nomi = ottimizza.costruisci(var, menu, cap)
    J, M = len(chiavi), len(menu)
    ignote = [k for k in misure if k not in set(chiavi.chiave)] + [c for c in cop if c not in set(menu.misura_id)]
    if ignote:
        sys.exit(f"codici sconosciuti: {ignote}")
    x = np.zeros(J + M)
    x[chiavi.index[chiavi.chiave.isin(misure)]] = 1
    x[J + menu.index[menu.misura_id.isin(cop)]] = 1

    problemi = []
    ax = A @ x
    for n, v, lo, hi in zip(nomi, ax, lb, ub):
        if v > hi + 1e-6 or v < lo - 1e-6:
            if n == "risorse generali":
                problemi.append(f"mancano {num(v - hi)} mld di coperture sulle risorse generali")
            elif n.startswith("fondo "):
                problemi.append(f"il {n} supera la disponibilità di {num(v - hi)} mld")
            elif n.startswith("legame "):
                problemi.append(f"la copertura {n[7:]} è usata senza la misura a cui è legata ({', '.join(ottimizza.LEGAMI[n[7:]])})")
            elif n.startswith("una variante"):
                problemi.append(f"più versioni della stessa proposta ({n[13:]})")
    for motivo, chiave, i in ottimizza.linee_rosse(chiavi, menu):
        if x[i]:
            problemi.append(f"linea rossa: {chiave}, {motivo}")

    # conti anno per anno con lo stesso calendario del programma
    sel = chiavi.assign(scelta=x[:J].astype(int), robustezza=np.nan)
    msel = menu.assign(scelta=x[J:].astype(int), robustezza=np.nan)
    f = QUI / f"selezione_{ETICHETTA}.csv"
    pd.concat([sel.assign(tipo="variante"), msel.rename(columns={"misura_id": "chiave"}).assign(tipo="copertura")],
              ignore_index=True).to_csv(f, index=False)
    try:
        pi = annuale.piano(ETICHETTA)
    finally:
        f.unlink(missing_ok=True)

    # robustezza sui valori rispetto al programma intermedio
    rng = np.random.default_rng(7)
    S, _, _, ids = decidi.carica_panel()
    sim = decidi.simula(S, a.n, rng, fattori=decidi.calibrazione(ids))
    U, W = sim["U"], sim["W"]
    pos = {p: i for i, p in enumerate(ids)}
    col = np.array([pos.get(p, -1) for p in chiavi.proposta_id])
    inten = chiavi.intensita.to_numpy()
    Mv = menu[ottimizza.VALORI].to_numpy()
    rif = pd.read_csv(QUI / "selezione_intermedio.csv")
    xr = np.zeros(J + M)
    xr[chiavi.index[chiavi.chiave.isin(rif[(rif.tipo == "variante") & (rif.scelta == 1)].chiave)]] = 1
    xr[J + menu.index[menu.misura_id.isin(rif[(rif.tipo == "copertura") & (rif.scelta == 1)].chiave)]] = 1

    def utilita(xx: np.ndarray, k: int) -> float:
        u = np.where(col >= 0, U[k][np.maximum(col, 0)], 0.0) * inten
        return float(u @ xx[:J] + (Mv @ W[k]) @ xx[J:])
    meglio = np.mean([utilita(x, k) >= utilita(xr, k) for k in range(len(U))])

    spesa = float(chiavi.costo_regime.to_numpy() @ x[:J])
    gettito = float(menu.gettito_min.to_numpy() @ x[J:])
    regr = float(menu.gettito_min.to_numpy() @ (x[J:] * (menu.EQU.to_numpy() < 0)))
    esito = "valido" if not problemi else "non valido"
    righe = [f"# Programma proposto: {nome}", "",
             f"*Validazione automatica del {date.today().strftime('%d/%m/%Y')} con `programma/valida_proposta.py`. "
             "Le regole sono le stesse del programma di GovernAI. Nessuna persona ha cambiato i numeri.*", "",
             f"**Esito: {esito}.**", "",
             f"- Misure: {len(misure)}; spesa a regime {num(spesa)} mld l'anno.",
             f"- Coperture: {len(cop)}; gettito minimo {num(gettito)} mld l'anno, di cui {num(regr)} da coperture che pesano di più su chi ha meno.",
             f"- Robustezza sui valori: con {len(U)} combinazioni diverse di pesi tra i valori, fa almeno quanto il programma intermedio in {round(meglio * 100)} casi su 100."]
    if problemi:
        righe += ["", "## Da sistemare", ""] + [f"- {p}" for p in problemi]
    if pi:
        righe += ["", "## Conti anno per anno (ipotesi prudente)", "",
                  "| Anno | Spesa prevista sulle risorse generali | Avviata | Rinviata |", "|---|---|---|---|"]
        righe += [f"| {r['anno']} | {num(r['prevista'])} | {num(r['avviata'])} | {num(r['rinviata'])} |" for r in pi["anni"]]
        righe += ["", f"In tutto slittano {num(pi['rinviata_totale'])} mld negli anni di passaggio, di cui {num(pi['rinviata_nucleo'])} del nucleo robusto."]
    righe += ["", f"Link per aprirlo sul sito: {a.link}", ""]
    testo = "\n".join(righe)
    print(testo)
    if a.pubblica:
        d = RADICE / "proposte"
        d.mkdir(exist_ok=True)
        nomefile = f"{date.today().isoformat()}_{slug(nome)}.md"
        (d / nomefile).write_text(testo, encoding="utf-8")
        ind_f = d / "validati.json"
        ind = json.loads(ind_f.read_text(encoding="utf-8")) if ind_f.exists() else []
        ind = [e for e in ind if e.get("file") != nomefile] + [{
            "file": nomefile, "nome": nome, "data": date.today().isoformat(), "issue": a.pubblica, "esito": esito,
            "misure": len(misure), "spesa": round(spesa, 2), "coperture": len(cop), "gettito": round(gettito, 2),
            "robustezza": round(float(meglio), 3), "rinviata": pi["rinviata_totale"] if pi else None,
            "codice": a.link.split("?", 1)[-1]}]
        ind_f.write_text(json.dumps(ind, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"scritto proposte/{nomefile}")
    return 0 if not problemi else 1


if __name__ == "__main__":
    raise SystemExit(main())
