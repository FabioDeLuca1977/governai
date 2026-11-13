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
    ("intermedio", "Programma intermedio", "Nessun aumento di tasse su casa, eredità, affitti e IVA; più istruzione e servizi sociali; ricerca, innovazione, logistica verde e squadra per la produttività pubblica con l'AI inserite per scelta politica; restano accise su tabacco e alcol e il riordino di agevolazioni e sussidi dannosi; dal 12 novembre 2026 entrano, senza tasse in più oltre quelle già previste, Case della Comunità, squadre infermieristiche di quartiere e riqualificazione degli amministrativi della sanità; dal 13 novembre il progetto di vita per le persone con disabilità e il personale infermieristico partono come pilota; 0,09 mld restano da parte per smettere di fumare e per il dopo 2029", "selezione_intermedio.csv"),
    ("momento", "Completo adattato ai dati di oggi", "Il programma completo ricalcolato con le priorità delle allerte attive: cambia quando cambiano i dati e serve a vedere che cosa suggerirebbero, non è un impegno", "selezione_momento.csv"),
    ("dividendo", "Completo + dividendo climatico", "Restituzione compensativa di 1,2 mld del gettito dal taglio dei sussidi ambientalmente dannosi (SAD)", "selezione_dividendo.csv"),
    ("difesa", "Completo + Difesa al 2,5%", "Traiettoria graduale della spesa militare (+9,1 mld)", "selezione_difesa.csv"),
]
RE_SCHEDA = re.compile(r"^## (0[1-9]-[PC]\d{1,2})\b.*$", re.M)


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


# Fondi con un proprio vincolo (programma/ottimizza.py): la spesa che vi attinge oltre il gettito delle
# coperture dello stesso fondo usa risorse già stanziate (capienza del registro), non nuove tasse né deficit.
GENERALI = {"SAD", "SPESE_FISCALI", "ACCISE_SALUTE", "RIORDINO_BONUS", "RIALLOCAZIONE"}
FUORI_BILANCIO = {"TARIFFE"}
NOMI_FONDI = {"COESIONE_2127": "fondi europei di coesione 2021-2027", "COESIONE_2834": "fondi europei di coesione 2028-2034",
              "FSN": "fondo sanitario nazionale", "PENSIONI": "risorse del sistema pensionistico", "FONDI_UE": "fondi europei",
              "TASSA_SOGGIORNO": "tassa di soggiorno", "ETS2_FSC": "Fondo sociale per il clima (ETS2)"}


def prelievi_varianti() -> pd.DataFrame:
    """Una riga per variante e fondo: la somma dei prelievi di una variante è il suo costo."""
    file = sorted((RADICE / "programma" / "varianti").glob("*.csv"))
    v = pd.concat([pd.read_csv(f) for f in file], ignore_index=True)
    v["chiave"] = v.proposta_id + ":" + v.variante.str.upper().str.strip()
    v["fondo_id"] = v.fondo_id.str.upper().str.strip()
    v["prelievo_regime"] = pd.to_numeric(v.prelievo_regime, errors="coerce").fillna(0.0)
    return v[["chiave", "fondo_id", "prelievo_regime"]]


def dopo_2029(v: pd.DataFrame, prelievi: pd.DataFrame) -> dict:
    """Che cosa succede dopo il 2029 alla spesa pagata con la coesione 2021-2027 (programma/coesione_dopo_2029.csv).
    Le varianti PILOTA finiscono con una valutazione; per le altre il file dice se la spesa finisce o ha un successore."""
    f = RADICE / "programma" / "coesione_dopo_2029.csv"
    regole = pd.read_csv(f).set_index("proposta_id") if f.exists() else pd.DataFrame()
    pr = prelievi[(prelievi.fondo_id == "COESIONE_2127") & prelievi.chiave.isin(v.chiave)].groupby("chiave").prelievo_regime.sum()
    voci, tot = [], {"fine": 0.0, "valutazione": 0.0, "successore": 0.0, "da_decidere": 0.0}
    for chiave, mld in pr.items():
        if mld <= 0:
            continue
        pid, var = chiave.split(":")
        if var == "PILOTA":
            esito, succ, motivo = "valutazione", "", "sperimentazione: finisce nel 2029 e prosegue solo con una valutazione positiva e risorse nuove"
        elif pid in regole.index:
            r = regole.loc[pid]
            esito, succ, motivo = r.esito, ("" if pd.isna(r.successore) else r.successore), r.motivo
        else:
            esito, succ, motivo = "da_decidere", "", "non ancora classificata"
        tot[esito] += float(mld)
        voci.append({"id": pid, "variante": var, "mld": round(float(mld), 3), "esito": esito, "successore": succ, "motivo": motivo})
    return {**{k: round(x, 2) for k, x in tot.items()}, "voci": sorted(voci, key=lambda x: (x["esito"], -x["mld"]))}


def annuale(file_sel: str) -> list[dict]:
    """Conti anno per anno 2027-2035 (programma/annuale.py): saldo delle risorse generali con ipotesi prudente
    e favorevole sulle rampe delle coperture."""
    try:
        sys.path.insert(0, str(RADICE / "programma"))
        import annuale as an
    except Exception:
        return []
    etichetta = file_sel.removeprefix("selezione_").removesuffix(".csv")
    t, tf = an.conti(etichetta), an.conti(etichetta, anticipo=1)
    if t is None or tf is None:
        return []
    return [{"anno": int(r.anno), "spesa": r.spesa, "spesa_generali": r.spesa_generali, "gettito_generali": r.gettito_generali,
             "saldo": r.saldo_generali, "saldo_favorevole": f.saldo_generali, "da_rifinanziare": r.da_rifinanziare}
            for r, f in zip(t.itertuples(), tf.itertuples())]


def calendario(file_sel: str) -> dict:
    """Calendario di avvio (programma/annuale.py, scelta del 13 novembre 2026)."""
    try:
        sys.path.insert(0, str(RADICE / "programma"))
        import annuale as an
        p = an.piano(file_sel.removeprefix("selezione_").removesuffix(".csv"))
    except Exception:
        return {}
    if not p:
        return {}
    tardi = {k: v for k, v in p["misure"].items() if v.get("gruppo") == "g3" and v.get("spesa_max", 0) > 0.005}
    inizio = {k: next((a for a, q in sorted(v["anni"].items()) if q > 0.005), None) for k, v in tardi.items()}
    pieno = {k: next((a for a, q in sorted(v["anni"].items()) if q >= 0.999), None) for k, v in tardi.items()}
    nucleo_pieno = next((a["anno"] for a in p["anni"] if a["quota_nucleo"] >= 0.995), None)
    return {"anni": p["anni"], "rinviata_totale": p["rinviata_totale"], "rinviata_nucleo": p["rinviata_nucleo"],
            "coesione_rinviata": p["coesione_rinviata"], "riforme_subito": p["riforme_subito"], "nucleo_pieno": nucleo_pieno,
            "pieno_dal": {k: a for k, a in pieno.items() if a}, "inizio": {k: a for k, a in inizio.items() if a}}


def scenario(file: Path, prelievi: pd.DataFrame) -> dict | None:
    if not file.exists():
        return None
    s = pd.read_csv(file)
    v = s[(s.tipo == "variante") & (s.scelta == 1)]
    c = s[(s.tipo == "copertura") & (s.scelta == 1)]
    # Come si paga la spesa: coperture nuove, risorse già stanziate nei fondi vincolati, tariffe fuori bilancio
    usa = prelievi[prelievi.chiave.isin(v.chiave)].groupby("fondo_id").prelievo_regime.sum()
    get = c.assign(fondo_id=c.fondo_id.str.upper().str.strip()).groupby("fondo_id").gettito_min.sum()
    gia = {f: round(float(x - get.get(f, 0.0)), 2) for f, x in usa.items()
           if f not in GENERALI | FUORI_BILANCIO and x - get.get(f, 0.0) > 0.005}
    tariffe = round(float(usa[usa.index.isin(FUORI_BILANCIO)].sum()), 2)
    spesa, gettito = round(float(v.costo_regime.sum()), 2), round(float(c.gettito_min.sum()), 2)
    risorse = round(gettito + sum(gia.values()) + tariffe, 2)
    # Margine vero: solo le risorse generali sono spostabili da una spesa all'altra; il resto è vincolato
    margine_gen = round(float(get[get.index.isin(GENERALI)].sum() - usa[usa.index.isin(GENERALI)].sum()), 2)
    # Spesa pagata con la coesione 2021-2027: le spese sono ammissibili solo fino al 2029, poi va sostituita
    temporanei = round(float(usa.get("COESIONE_2127", 0.0)), 2)
    # Varianti imposte per scelta politica (riga "Vincoli di scenario" del file .md dell'ottimizzatore)
    vincoli = re.search(r"forzate \[([^\]]*)\]", leggi(file.with_suffix(".md")))
    forzate = sorted(re.findall(r"'([^']+)'", vincoli.group(1))) if vincoli else []
    return {"misure": {r.proposta_id: {"variante": r.variante, "costo": round(float(r.costo_regime), 3),
                                       "robustezza": round(float(r.robustezza), 3),
                                       **({"imposta": True} if r.chiave in forzate else {})} for r in v.itertuples()},
            "coperture": sorted(c.chiave.tolist()),
            "spesa": spesa, "gettito": gettito,
            "gia_stanziati": [{"fondo": f, "nome": NOMI_FONDI.get(f, f.lower()), "mld": x} for f, x in sorted(gia.items())],
            "tariffe": tariffe, "risorse": risorse,
            "deficit": round(max(0.0, spesa - risorse), 2), "margine": round(max(0.0, risorse - spesa), 2),
            "margine_generali": max(margine_gen, 0.0), "vincolati_non_usati": round(max(0.0, risorse - spesa - max(margine_gen, 0.0)), 2),
            "temporanei_2029": temporanei, "dopo_2029": dopo_2029(v, prelievi)}


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


def mappa() -> dict:
    """Mappa dei ministeri per la home: temi e relazioni tra aree (programma/mappa_ministeri.yaml, dalle sezioni B e D dei dossier)."""
    f = RADICE / "programma" / "mappa_ministeri.yaml"
    if not f.exists():
        return {}
    m = yaml.safe_load(leggi(f)) or {}
    dossier = {x.name[:2]: "ministeri/" + x.name for x in sorted((RADICE / "ministeri").glob("0*.md"))}
    for k, a in (m.get("aree") or {}).items():
        a["dossier"] = dossier.get(k, "")
    return m


def schema() -> dict:
    """Il programma in una pagina: missioni con perché, come, cosa misuriamo e chi ne beneficia (programma/schema.yaml).
    Gli indicatori sono presi da apprendimento/obiettivi.yaml, così base e traguardi restano quelli delle schede."""
    f = RADICE / "programma" / "schema.yaml"
    if not f.exists():
        return {}
    s = yaml.safe_load(leggi(f))
    obi = {o["id"]: o for o in (yaml.safe_load(leggi(RADICE / "apprendimento" / "obiettivi.yaml")) or {}).get("obiettivi", [])}
    usati = set(s.get("programma", {}).get("indicatori_chiave", []))
    for m in s.get("missioni", []):
        usati |= set(m.get("indicatori", []))
    s["indicatori"] = {}
    for i in sorted(usati):
        o = obi.get(i)
        if not o:
            continue
        base = o.get("base") or {}
        sch = o.get("scheda") or {}
        s["indicatori"][i] = {"nome": o.get("nome"), "proposta": o.get("proposta"), "unita": o.get("unita"),
                              "direzione": o.get("direzione"), "valori": o.get("valori") or [],
                              "base": base.get("valore"), "periodo": base.get("periodo"), "fonte": base.get("fonte"),
                              "obiettivo_3a": o.get("obiettivo_3a"), "obiettivo_5a": o.get("obiettivo_5a"),
                              "testo_base": sch.get("base"), "testo_5a": sch.get("obiettivo_5a")}
        semplice = (s.get("indicatori_semplici") or {}).get(i) or {}
        if "obiettivo_5a" in semplice:
            s["indicatori"][i]["testo_5a"] = None
        s["indicatori"][i].update(semplice)
    s.pop("indicatori_semplici", None)
    return s


def integrita() -> dict:
    anelli = catena.leggi_catena()
    campi = ("n", "data", "evento", "nota", "hash", "precedente", "radice_regole", "radice_input", "radice_output",
             "regole_cambiate")
    return {"anelli": len(anelli), "errori": catena.verifica(),
            "ultimi": [{k: a.get(k) for k in campi} for a in anelli[-30:]][::-1]}


def governo() -> dict:
    g = RADICE / "governo"
    leggi_csv = lambda f: records(pd.read_csv(f, dtype=str).fillna("")) if f.exists() else []
    return {"verbali": [{"seduta": f.stem, "testo": leggi(f)} for f in sorted((g / "verbali").glob("*.md"), key=lambda f: f.stem, reverse=True)[:60]],
            "credibilita": leggi_csv(g / "credibilita.csv"), "mandati": leggi_csv(g / "mandati.csv"),
            "verifiche": sorted((json.loads(leggi(f)) for f in (g / "verifiche").glob("*.json")),
                                key=lambda x: x["seduta"], reverse=True),
            "regolamento": leggi(g / "regolamento.md") if (g / "regolamento.md").exists() else "",
            "esperti": {e["id"]: e["nome"] for e in yaml.safe_load(leggi(g / "esperti.yaml"))["esperti"]}
            if (g / "esperti.yaml").exists() else {}}


def europa() -> dict:
    """Scadenze UE, infrazioni e Semestre (europa/); vuoto se il modulo non c'è."""
    try:
        sys.path.insert(0, str(RADICE / "europa"))
        from uscite import dati_web
        d = dati_web()
        d.pop("novita_md", None)  # il testo completo resta in europa/novita.md: il sito resta leggero
        return d
    except Exception:  # noqa: BLE001
        return {}


def costituzione() -> dict:
    c = RADICE / "costituzione"
    if not c.exists():
        return {}
    esami = [{"id": f.stem, "testo": leggi(f)} for f in sorted((c / "esami").glob("*.md"))
             if not f.stem.endswith("_screening")]
    gu = json.loads(leggi(c / "esami" / "gu" / "stato.json")) if (c / "esami" / "gu" / "stato.json").exists() else {}
    screening = []
    for f in sorted((c / "esami").glob("*_screening.json")):
        j = json.loads(leggi(f))
        screening.append({"id": f.stem.replace("_screening", ""), "origine": j.get("origine", ""),
                          "data": j.get("data_riferimento", ""), "articoli": j.get("articoli", 0),
                          "alto": len(j["alto"]) if isinstance(j.get("alto"), list) else j.get("alto", 0),
                          "medio": len(j["medio"]) if isinstance(j.get("medio"), list) else j.get("medio", 0)})
    return {"esami": esami, "screening": screening,
            "gu_alti": [{"codice": k, **v} for k, v in gu.get("esaminati", {}).items() if v.get("alto")][-30:],
            "pronunce_verificate": len(json.loads(leggi(c / "giurisprudenza_verificata.json")))
            if (c / "giurisprudenza_verificata.json").exists() else 0}


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
    giur = pd.read_csv(conf_f, dtype=str).fillna("") if conf_f.exists() else pd.DataFrame(columns=["tipo", "id"])
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
            "giuridico": giur[((giur.tipo == "proposta") & (giur.id == r.proposta_id))
                              | ((giur.tipo == "variante") & giur.id.str.startswith(r.proposta_id + ":"))]
                         .reindex(columns=campi_g).to_dict("records"),
        })

    # Scenari del programma
    scen = []
    prel = prelievi_varianti()
    for sid, nome, desc, f in SCENARI:
        s = scenario(RADICE / "programma" / f, prel)
        if s:
            difesa = (s["misure"].get("07-C5") or {}).get("costo", 0)
            if sid == "difesa" and difesa:  # senza questa riga il totale sembra contraddire i +9,1 mld
                it = lambda x: f"{x:.1f}".replace(".", ",")
                desc = (f"Spesa militare in crescita graduale, +{it(difesa)} mld l'anno a regime (2034). Per restare senza "
                        f"deficit le altre misure scendono a {it(s['spesa'] - difesa)} mld l'anno")
            scen.append({"id": sid, "nome": nome, "descrizione": desc, **s, "annuale": annuale(f), "calendario": calendario(f)})

    # Coperture
    menu = pd.read_csv(RADICE / "programma" / "coperture_menu.csv")
    col = [c for c in ["misura_id", "descrizione", "fondo_id", "gettito_min", "gettito_max", "anno_regime", "chi_paga",
                       "soggetti_coinvolti", "RIS", "FID", "INN", "BEN", "APC", "BPA", "FUT", "EQU", "SIC", "CIT", "strumento", "fonte_dato",
                       "livello"] if c in menu.columns]

    # Cruscotto con serie per i grafici
    ind = json.loads(leggi(QUI / "stato" / "indicatori.json") or "[]")
    registro = {}
    for f in sorted((RADICE / "dati" / "serie").glob("_registro_*.csv")):
        for x in pd.read_csv(f, dtype=str).fillna("").itertuples():
            registro[x.nome] = {"fonte": x.fonte, "url": x.url}
    for i, cfg in zip(ind, conf.get("indicatori", [])):
        i["fonte"] = registro.get(cfg.get("serie") or "00c_rendimenti_decennali", {})
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
        "coperture": [{**c, "giuridico": giur[(giur.tipo == "copertura") & (giur.id == c["misura_id"])]
                       .reindex(columns=campi_g).to_dict("records")} for c in records(menu[col])],
        "indicatori": ind,
        "regole": regole,
        "allerte_attive": sorted(attive),
        "bollettini": [{"data": f.stem, "testo": leggi(f)} for f in boll],
        "repo": repo_url(),
        "analisi": analisi(),
        "obiettivi": obiettivi(),
        "schema": schema(),
        "pacchetto": [{"id": f.stem.split("_")[0], "file": f"pacchetto/{f.name}", "testo": leggi(f)}
                      for f in sorted((RADICE / "pacchetto").glob("*.md")) if f.name != "README.md"]
                     if (RADICE / "pacchetto").exists() else [],
        "profili": (yaml.safe_load(leggi(RADICE / "programma" / "profili.yaml")) or {}).get("profili", [])
                   if (RADICE / "programma" / "profili.yaml").exists() else [],
        "mappa": mappa(),
        "comunita": {"regole": leggi(RADICE / "comunita" / "regole.md"), "privacy": leggi(RADICE / "comunita" / "privacy.md")},
        "lezioni": leggi(RADICE / "apprendimento" / "lezioni.md"),
        "integrita": integrita(),
        "governo": governo(),
        "europa": europa(),
        "costituzione": costituzione(),
        "numeri": {"cifre_verificate": 334, "proposte": len(proposte),
                   "varianti": int(var.drop_duplicates(["proposta_id", "variante"]).shape[0]),
                   "coperture": len(menu), "valori": len(valori_carta()),
                   "serie": len([f for f in (RADICE / "dati" / "serie").glob("*.csv") if not f.name.startswith("_")])},
        "documenti": {"carta": leggi(RADICE / "01_carta_valori.md"),
                      "programma": leggi(RADICE / "20_programma_governai.md"),
                      "sintesi": leggi(RADICE / "21_idee_in_sintesi.md"),
                      "equita": leggi(RADICE / "23_equita_e_linguaggio.md") if (RADICE / "23_equita_e_linguaggio.md").exists() else "",
                      "metodo": leggi(RADICE / "00_metodo.md"),
                      "garanzie": leggi(RADICE / "24_garanzie_e_responsabilita.md") if (RADICE / "24_garanzie_e_responsabilita.md").exists() else "",
                      "sistema": leggi(QUI / "README.md"),
                      "giuridico": leggi(RADICE / "giuridico" / "quadro.md"),
                      "confronto": leggi(RADICE / "benchmark" / "confronto.md"),
                      "partiti": leggi(RADICE / "benchmark" / "confronto_programmi.md"),
                      "ue": leggi(RADICE / "europa" / "semestre.md") if (RADICE / "europa" / "semestre.md").exists() else "",
                      "costituzione": "\n\n---\n\n".join(leggi(f) for f in [RADICE / "costituzione" / "esami" / "AC3174_manovra_2027.md",
                                                                       RADICE / "costituzione" / "esami" / "governai_conti_2027_2029.md"] if f.exists()),
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
