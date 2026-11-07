"""Apprendimento di GovernAI: misura gli obiettivi, riconosce successi e insuccessi, ricalibra le previsioni.

Il ciclo:
  1. obiettivi.yaml   — per ogni misura, i KPI con valore di base e obiettivi a 3 e 5 anni, collegati alle serie
                        ufficiali che il sistema aggiorna ogni giorno;
  2. decisioni.csv    — il registro delle decisioni prese (misura adottata, respinta, rinviata; chi e perché);
  3. valuta.py        — calcola per ogni KPI il progresso verso l'obiettivo e, per le misure adottate, se è
                        in linea con i tempi previsti (raggiunto / in linea / in ritardo / peggiorato);
  4. calibrazione.csv — confronta il risultato osservato con l'effetto previsto dal panel: se le misure di
                        un'area rendono meno del previsto, il motore ne riduce il peso nelle scelte successive
                        (fattore tra 0,5 e 1,5, prudente finché i casi sono pochi);
  5. lezioni.md       — successi e insuccessi in chiaro: li leggono il livello AI e l'analisi su richiesta.

Finché nessuna misura è adottata, i KPI restano "in osservazione": il sistema segue l'andamento del Paese
sugli stessi indicatori, così al momento dell'adozione la base è già solida.

Uso:  python valuta.py
"""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

QUI = Path(__file__).resolve().parent
RADICE = QUI.parent
SERIE = RADICE / "dati" / "serie"
ANNI_OBIETTIVO = 5
CASI_MINIMI = 3        # sotto questo numero di esiti la calibrazione resta prudente
TOLLERANZA = 0.10      # margine sul progresso atteso prima di dichiarare un ritardo
SOGLIA_ARRETRAMENTO = 0.05  # arretramenti più piccoli sono arrotondamenti o rumore statistico


def serie_kpi(o: dict) -> pd.DataFrame | None:
    s = o.get("serie") or {}
    f = SERIE / f"{s.get('file', '')}.csv"
    if not s or not f.exists():
        return None
    d = pd.read_csv(f)
    for col, val in (s.get("filtro") or {}).items():
        if col in d.columns:
            d = d[d[col].astype(str) == str(val)]
    # colonne del tempo e del valore: quelle dichiarate nell'obiettivo, altrimenti i nomi abituali
    tcol = next((c for c in (s.get("tempo"), "time", "anno", "TIME_PERIOD", "periodo") if c and c in d.columns), None)
    vcol = next((c for c in (s.get("colonna"), "valore", "OBS_VALUE") if c and c in d.columns), None)
    if tcol is None or vcol is None:
        return None
    d = d[[tcol, vcol]].rename(columns={tcol: "time", vcol: "valore"}).dropna()
    d["valore"] = pd.to_numeric(d.valore, errors="coerce") * float(s.get("scala", 1))
    return d.dropna().drop_duplicates("time", keep="last").sort_values("time")


def anni_da(periodo: str, inizio: str) -> float:
    def anno(p: str) -> float:
        p = str(p)
        base = float(p[:4])
        if "-Q" in p:
            return base + (int(p[-1]) - 1) / 4
        if len(p) >= 7 and p[4] == "-":
            return base + (int(p[5:7]) - 1) / 12
        return base
    return max(anno(periodo) - anno(inizio), 0.0)


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ob = (yaml.safe_load((QUI / "obiettivi.yaml").read_text(encoding="utf-8")) or {}).get("obiettivi", [])
    dec_f = QUI / "decisioni.csv"
    dec = pd.read_csv(dec_f, dtype=str) if dec_f.exists() else pd.DataFrame(columns=["data", "proposta", "decisione"])
    adottate = {r.proposta: r.data for r in dec[dec.decisione.str.lower() == "adottata"].itertuples()}

    righe = []
    for o in ob:
        d = serie_kpi(o)
        base = (o.get("base") or {}).get("valore")
        obiettivo = o.get("obiettivo_5a") if o.get("obiettivo_5a") is not None else o.get("obiettivo_3a")
        r = {"id": o["id"], "proposta": o.get("proposta"), "nome": o.get("nome"), "unita": o.get("unita", ""),
             "direzione": o.get("direzione"), "base": base, "periodo_base": (o.get("base") or {}).get("periodo"),
             "obiettivo": obiettivo, "valori": ",".join(o.get("valori", [])), "ultimo": None, "periodo": None,
             "progresso": None, "atteso": None, "stato": "manuale" if d is None else "in osservazione"}
        if d is not None and not d.empty:
            r["ultimo"], r["periodo"] = float(d.valore.iloc[-1]), str(d.time.iloc[-1])
            if base is not None and obiettivo is not None and obiettivo != base:
                r["progresso"] = round((r["ultimo"] - base) / (obiettivo - base), 3)
        avvio = adottate.get(o.get("proposta"))
        if avvio and r["progresso"] is not None:
            atteso = min(anni_da(r["periodo"], avvio[:7]) / ANNI_OBIETTIVO, 1.0)
            r["atteso"] = round(atteso, 3)
            p = r["progresso"]
            r["stato"] = ("raggiunto" if p >= 1 else "peggiorato" if p < 0 else
                          "in linea" if p >= atteso - TOLLERANZA else "in ritardo")
        righe.append(r)
    esiti = pd.DataFrame(righe)
    esiti.to_csv(QUI / "esiti.csv", index=False)

    # Calibrazione per area: rendimento osservato / atteso delle misure adottate
    valutati = esiti[esiti.stato.isin(["raggiunto", "in linea", "in ritardo", "peggiorato"]) & (esiti.atteso > 0)].copy()
    cal = []
    if len(valutati):
        valutati["area"] = valutati.proposta.str[:2]
        valutati["rendimento"] = (valutati.progresso / valutati.atteso).clip(-1, 2)
        for area, g in valutati.groupby("area"):
            n = len(g)
            grezzo = float(g.rendimento.mean())
            # più casi, più fiducia nell'osservato; con pochi casi il fattore resta vicino a 1
            peso = n / (n + CASI_MINIMI)
            fattore = float(np.clip(1 + peso * (grezzo - 1), 0.5, 1.5))
            cal.append({"area": area, "casi": n, "rendimento_medio": round(grezzo, 3), "fattore": round(fattore, 3)})
    pd.DataFrame(cal, columns=["area", "casi", "rendimento_medio", "fattore"]).to_csv(QUI / "calibrazione.csv", index=False)

    # Lezioni apprese (parte automatica; il livello AI aggiunge l'interpretazione)
    conta = esiti.stato.value_counts().to_dict()
    lez = [f"# Lezioni apprese — aggiornate al {date.today():%d/%m/%Y}", "",
           "*Parte generata da `apprendimento/valuta.py`. Il livello AI aggiunge sotto le sue interpretazioni.*", "",
           f"- KPI seguiti: {len(esiti)} ({conta.get('in osservazione', 0)} in osservazione, "
           f"{conta.get('manuale', 0)} da misurare a mano)",
           f"- Misure adottate valutate: {len(valutati)} KPI — raggiunti {conta.get('raggiunto', 0)}, in linea "
           f"{conta.get('in linea', 0)}, in ritardo {conta.get('in ritardo', 0)}, peggiorati {conta.get('peggiorato', 0)}"]
    for c in cal:
        verso = "meglio" if c["fattore"] > 1 else "peggio" if c["fattore"] < 1 else "come"
        lez.append(f"- Area {c['area']}: le misure rendono {verso} del previsto (rendimento {c['rendimento_medio']:.2f}, "
                   f"{c['casi']} casi) → fattore di calibrazione {c['fattore']:.2f}")
    for r in esiti[esiti.stato.isin(["peggiorato", "in ritardo"])].itertuples():
        lez.append(f"- Insuccesso da capire: {r.proposta} «{r.nome}» è {r.stato} (progresso {r.progresso:.0%} contro "
                   f"{r.atteso:.0%} atteso)")
    for r in esiti[esiti.stato == "raggiunto"].itertuples():
        lez.append(f"- Successo: {r.proposta} «{r.nome}» ha raggiunto l'obiettivo")
    # Andamento del Paese sui KPI in osservazione: segnali utili anche prima dell'adozione
    oss = esiti[(esiti.stato == "in osservazione") & esiti.progresso.notna()]
    peggio = oss[oss.progresso < -SOGLIA_ARRETRAMENTO].sort_values("progresso").head(5)
    if len(peggio):
        lez += ["", "**Indicatori che si allontanano dall'obiettivo anche senza intervento** (priorità da rivalutare):"]
        lez += [f"- {r.proposta} «{r.nome}»: {r.ultimo:.4g} {r.unita} ({r.periodo}) contro base {r.base:.4g}" for r in peggio.itertuples()]
    vecchio = (QUI / "lezioni.md").read_text(encoding="utf-8") if (QUI / "lezioni.md").exists() else ""
    ai = vecchio.split("## Interpretazioni del livello AI", 1)[1] if "## Interpretazioni del livello AI" in vecchio else "\n"
    (QUI / "lezioni.md").write_text("\n".join(lez) + "\n\n## Interpretazioni del livello AI" + ai, encoding="utf-8")
    print(f"apprendimento: {len(esiti)} KPI, stati {conta}, aree calibrate {len(cal)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
