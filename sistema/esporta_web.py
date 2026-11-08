"""Esporta i dati di GovernAI per l'interfaccia web (cartella docs/, pubblicabile con GitHub Pages).

Scrive docs/data.js con window.GOVERNAI = {...}: un unico file JavaScript, così l'interfaccia
funziona anche aprendo docs/index.html con un doppio clic, senza server.

Uso:  python esporta_web.py
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

QUI = Path(__file__).resolve().parent
RADICE = QUI.parent
sys.path.insert(0, str(RADICE / "motore"))
sys.path.insert(0, str(QUI))
sys.path.insert(0, str(RADICE / "integrita"))
import catena  # noqa: E402
import decidi  # noqa: E402
import pipeline  # noqa: E402

AREE = {"01": "Economia, Imprese, Turismo", "02": "Lavoro, Welfare, Famiglia", "03": "Ambiente, Energia, Agricoltura",
        "04": "Infrastrutture e Territori", "05": "Istruzione, Ricerca, Cultura", "06": "Salute",
        "07": "Giustizia, Interno, Difesa", "08": "Esteri, Europa, Istituzioni", "09": "PA e Digitale"}
SCENARI = [
    ("base", "Programma base", "Solo coperture a basso costo sociale", "selezione_livello1.csv"),
    ("completo", "Programma completo", "Con le coperture strutturali", "selezione_livello2.csv"),
    ("momento", "Programma del momento", "Completo, adattato alle allerte attive", "selezione_momento.csv"),
    ("dividendo", "Completo + dividendo climatico", "Restituzione compensativa di 1,2 mld del gettito SAD", "selezione_dividendo.csv"),
    ("difesa", "Completo + Difesa al 2,5%", "Traiettoria graduale della spesa militare (+9,1 mld)", "selezione_difesa.csv"),
]
RE_SCHEDA = re.compile(r"^## (0[1-9]-[PC]\d)\b.*$", re.M)


def leggi(p: Path) -> str:
    return p.read_text(encoding="utf-8") if p.exists() else ""


def pulisci(v):
    if isinstance(v, (float, np.floating)):
        return None if np.isnan(v) else round(float(v), 4)
    if isinstance(v, (np.integer,)):
        return int(v)
    if isinstance(v, (np.bool_,)):
        return bool(v)
    return v


def records(df: pd.DataFrame) -> list[dict]:
    return [{k: pulisci(v) for k, v in r.items()} for r in df.to_dict("records")]


def schede() -> dict[str, str]:
    out = {}
    for f in sorted((RADICE / "programma" / "schede").glob("*.md")):
        t = leggi(f)
        pos = [(m.group(1), m.start()) for m in RE_SCHEDA.finditer(t)]
        for i, (pid, ini) in enumerate(pos):
            fine = pos[i + 1][1] if i + 1 < len(pos) else len(t)
            blocco = t[ini:fine]
            coda = re.search(r"^## (?!0[1-9]-)", blocco[3:], re.M)  # sezioni finali non legate a una proposta
            out[pid] = blocco[: coda.start() + 3] if coda else blocco
    return out


def valori_carta() -> list[dict]:
    t = leggi(RADICE / "01_carta_valori.md")
    out = []
    for m in re.finditer(r"### \d+\. (.+?) \((\w{3})\)\n\*\*Definizione\.\*\* (.+?)\n", t):
        out.append({"id": m.group(2), "nome": m.group(1), "definizione": m.group(3).strip()})
    return out


def scenario(file: Path) -> dict | None:
    if not file.exists():
        return None
    s = pd.read_csv(file)
    v = s[(s.tipo == "variante") & (s.scelta == 1)]
    c = s[(s.tipo == "copertura") & (s.scelta == 1)]
    return {"misure": {r.proposta_id: {"variante": r.variante, "costo": round(float(r.costo_regime), 3),
                                       "robustezza": round(float(r.robustezza), 3)} for r in v.itertuples()},
            "coperture": sorted(c.chiave.tolist()),
            "spesa": round(float(v.costo_regime.sum()), 2),
            "gettito": round(float(c.gettito_min.sum()), 2)}


def repo_url() -> str:
    try:
        u = subprocess.run(["git", "remote", "get-url", "origin"], cwd=RADICE, capture_output=True, text=True).stdout.strip()
    except OSError:
        return ""
    return u[:-4] if u.endswith(".git") else u


def analisi() -> list[dict]:
    out = []
    for f in sorted((RADICE / "analisi").glob("*.json"), reverse=True)[:100]:
        d = json.loads(leggi(f))
        out.append({"id": f.stem, "titolo": d["dossier"]["titolo"], "richiesta": d["richiesta"]["titolo"],
                    "issue": d["richiesta"].get("numero"), "testo": leggi(f.with_suffix(".md"))})
    return out


def obiettivi() -> list[dict]:
    f = RADICE / "apprendimento" / "esiti.csv"
    return records(pd.read_csv(f)) if f.exists() else []


def integrita() -> dict:
    anelli = catena.leggi_catena()
    campi = ("n", "data", "evento", "nota", "hash", "precedente", "radice_regole", "radice_input", "radice_output",
             "regole_cambiate")
    return {"anelli": len(anelli), "errori": catena.verifica(),
            "ultimi": [{k: a.get(k) for k in campi} for a in anelli[-30:]][::-1]}


def governo() -> dict:
    g = RADICE / "governo"
    leggi_csv = lambda f: records(pd.read_csv(f, dtype=str).fillna("")) if f.exists() else []
    return {"verbali": [{"seduta": f.stem, "testo": leggi(f)} for f in sorted((g / "verbali").glob("*.md"), reverse=True)[:60]],
            "credibilita": leggi_csv(g / "credibilita.csv"), "mandati": leggi_csv(g / "mandati.csv"),
            "regolamento": leggi(g / "regolamento.md") if (g / "regolamento.md").exists() else ""}


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    conf = yaml.safe_load(leggi(QUI / "config.yaml"))

    # Proposte: esito del motore, varianti, schede, punteggi mediani del panel
    prop = pd.read_csv(RADICE / "motore" / "proposte.csv")
    esito = pd.read_csv(RADICE / "motore" / "esito_proposte.csv").set_index("proposta_id")
    S, _, valutatori, ids = decidi.carica_panel()
    mediana = np.median(S, axis=0)  # p, v, h
    pos = {p: i for i, p in enumerate(ids)}
    var = pd.concat([pd.read_csv(f) for f in sorted((RADICE / "programma" / "varianti").glob("*.csv"))])
    var["variante"] = var.variante.str.upper().str.strip()
    sk = schede()
    conf_f = RADICE / "giuridico" / "conformita.csv"
    conf = pd.read_csv(conf_f, dtype=str).fillna("") if conf_f.exists() else pd.DataFrame(columns=["tipo", "id"])
    campi_g = ["tipo", "id", "ambito", "esito", "norme", "fonti", "motivazione", "condizioni"]
    proposte = []
    for r in prop.itertuples():
        e = esito.loc[r.proposta_id]
        vv = var[var.proposta_id == r.proposta_id].drop_duplicates("variante")
        proposte.append({
            "id": r.proposta_id, "titolo": r.titolo, "area": r.proposta_id[:2], "classe": e.classe,
            "utilita": pulisci(e.utilita_attesa), "p_prima_meta": pulisci(e.p_prima_meta),
            "rango": [int(e.rango_p5), int(e.rango_p95)], "costo_pieno": pulisci(e.costo_medio),
            "linea_rossa": bool(e.linea_rossa), "trainanti": e.valori_trainanti if isinstance(e.valori_trainanti, str) else "",
            "punteggi": mediana[pos[r.proposta_id]].round(2).tolist() if r.proposta_id in pos else None,
            "varianti": [{"variante": x.variante, "intensita": pulisci(x.intensita), "costo": pulisci(x.costo_regime),
                          "descrizione": x.descrizione, "strumento": getattr(x, "strumento", "")} for x in vv.itertuples()],
            "scheda": sk.get(r.proposta_id, ""),
            "giuridico": conf[((conf.tipo == "proposta") & (conf.id == r.proposta_id))
                              | ((conf.tipo == "variante") & conf.id.str.startswith(r.proposta_id + ":"))]
                         .reindex(columns=campi_g).to_dict("records"),
        })

    # Scenari del programma
    scen = []
    for sid, nome, desc, f in SCENARI:
        s = scenario(RADICE / "programma" / f)
        if s:
            scen.append({"id": sid, "nome": nome, "descrizione": desc, **s})

    # Coperture
    menu = pd.read_csv(RADICE / "programma" / "coperture_menu.csv")
    col = [c for c in ["misura_id", "descrizione", "fondo_id", "gettito_min", "gettito_max", "anno_regime", "chi_paga",
                       "soggetti_coinvolti", "RIS", "FID", "INN", "BEN", "APC", "BPA", "FUT", "strumento", "fonte_dato",
                       "livello"] if c in menu.columns]

    # Cruscotto con serie per i grafici
    ind = json.loads(leggi(QUI / "stato" / "indicatori.json") or "[]")
    for i, cfg in zip(ind, conf.get("indicatori", [])):
        d = pipeline.serie_indicatore(cfg)
        if d is not None and not d.empty:
            d = d.tail(36)
            i["serie"] = {"t": [str(x) for x in d.time], "v": [pulisci(x) for x in d.valore]}
    attive = set(json.loads(leggi(QUI / "stato" / "allerte.json") or "[]"))
    regole = [{k: r.get(k) for k in ("id", "indicatore", "condizione", "messaggio", "azione", "priorita", "sospendi")}
              for r in conf.get("regole", [])]

    # Bollettini (gli ultimi 60)
    boll = sorted((QUI / "bollettini").glob("20*.md"), reverse=True)[:60]

    dati = {
        "generato": datetime.now().isoformat(timespec="minutes"),
        "aree": AREE,
        "valori": valori_carta(),
        "valutatori": valutatori,
        "proposte": proposte,
        "scenari": scen,
        "coperture": [{**c, "giuridico": conf[(conf.tipo == "copertura") & (conf.id == c["misura_id"])]
                       .reindex(columns=campi_g).to_dict("records")} for c in records(menu[col])],
        "indicatori": ind,
        "regole": regole,
        "allerte_attive": sorted(attive),
        "bollettini": [{"data": f.stem, "testo": leggi(f)} for f in boll],
        "repo": repo_url(),
        "analisi": analisi(),
        "obiettivi": obiettivi(),
        "lezioni": leggi(RADICE / "apprendimento" / "lezioni.md"),
        "integrita": integrita(),
        "governo": governo(),
        "numeri": {"cifre_verificate": 334, "proposte": len(proposte),
                   "varianti": int(var.drop_duplicates(["proposta_id", "variante"]).shape[0]),
                   "coperture": len(menu), "valori": len(valori_carta()),
                   "serie": len([f for f in (RADICE / "dati" / "serie").glob("*.csv") if not f.name.startswith("_")])},
        "documenti": {"carta": leggi(RADICE / "01_carta_valori.md"),
                      "programma": leggi(RADICE / "20_programma_governai.md"),
                      "metodo": leggi(RADICE / "00_metodo.md"),
                      "sistema": leggi(QUI / "README.md"),
                      "giuridico": leggi(RADICE / "giuridico" / "quadro.md"),
                      "confronto": leggi(RADICE / "benchmark" / "confronto.md"),
                      "trasparenza": leggi(RADICE / "trasparenza" / "rapporto.md"),
                      "legislazione": leggi(RADICE / "legislazione" / "README.md")},
    }
    dest = RADICE / "docs" / "data.js"
    dest.parent.mkdir(exist_ok=True)
    dest.write_text("window.GOVERNAI = " + json.dumps(dati, ensure_ascii=False, separators=(",", ":")) + ";\n",
                    encoding="utf-8")
    print(f"docs/data.js: {dest.stat().st_size / 1024:.0f} KB, {len(proposte)} proposte, {len(scen)} scenari, "
          f"{len(ind)} indicatori, {len(boll)} bollettini")
    return 0


if __name__ == "__main__":
    sys.exit(main())
