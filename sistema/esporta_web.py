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
    ("intermedio", "Programma intermedio", "Nessun aumento di aliquote su casa, eredità, affitti e IVA (sulle eredità si chiude solo l'esenzione per i patrimoni finanziari parcheggiati nelle holding); più istruzione e servizi sociali; squadre infermieristiche di quartiere e compensazione dell'autotrasporto inserite per scelta politica; dopo la verifica delle coperture del 13 novembre escono il pilota del personale infermieristico, il credito per la ricerca, il pilota del reddito di inclusione e le merci sul treno; dopo quella del 14 novembre Ufficio per il processo e governo dei flussi migratori passano a pilota; restano accise su tabacco e alcol e il riordino di agevolazioni e sussidi dannosi; dal 12 novembre 2026 entrano, senza tasse in più oltre quelle già previste, Case della Comunità, squadre infermieristiche di quartiere e riqualificazione degli amministrativi della sanità; dal 13 novembre il progetto di vita per le persone con disabilità parte come pilota; 0,06 mld restano da parte per smettere di fumare e per il dopo 2029", "selezione_intermedio.csv"),
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


def osservatorio() -> dict:
    """Osservatorio sul governo di oggi (osservatorio/): metodo e commenti agli atti, uno per file YAML."""
    cart = RADICE / "osservatorio"
    if not cart.exists():
        return {}
    atti = []
    for f in sorted((cart / "atti").glob("*.yaml")):
        try:
            x = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        except Exception:
            continue
        if x.get("id"):
            x["data"] = str(x.get("data", ""))
            for r in x.get("revisioni") or []:
                r["data"] = str(r.get("data", ""))
            x["file"] = f"osservatorio/atti/{f.name}"
            atti.append(x)
    ordine = {"legge di bilancio": 0, "decreto-legge": 1, "legge": 2, "decreto legislativo": 3}
    atti.sort(key=lambda x: (ordine.get(x.get("tipo"), 9), x.get("tema", ""), x["id"]))
    return {"metodo": leggi(cart / "metodo.md"), "atti": atti}


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


def motore_web() -> dict:
    """Dati per "Proponi un programma": il sito rifà nel browser lo stesso controllo di bilancio dell'ottimizzatore
    (un vincolo per le risorse generali, uno per ogni fondo vincolato, coperture legate) e applica le stesse linee rosse."""
    sys.path.insert(0, str(RADICE / "programma"))
    import ottimizza  # noqa: E402
    var, menu = ottimizza.carica_varianti(), ottimizza.carica_menu()
    cap = ottimizza.capienze_base(menu)
    chiavi, *_ = ottimizza.costruisci(var, menu, cap)
    prel: dict[str, dict[str, float]] = {}
    for r in var.itertuples():
        if r.prelievo_regime:
            d = prel.setdefault(r.chiave, {})
            d[r.fondo_id] = round(d.get(r.fondo_id, 0.0) + float(r.prelievo_regime), 4)
    rosse = {}
    for motivo, chiave, _ in ottimizza.linee_rosse(chiavi, menu):
        rosse.setdefault(chiave, motivo)
    return {"prelievi": prel, "capienze": {k: round(float(v), 4) for k, v in cap.items()},
            "generali": sorted(ottimizza.GENERALI), "fuori_bilancio": sorted(ottimizza.FUORI_BILANCIO),
            "legami": ottimizza.LEGAMI, "linee_rosse": rosse, "nomi_fondi": NOMI_FONDI}


SERIE_STORIA = ["pil_pro_capite_pps_ue27", "produttivita_oraria_crescita", "debito_pil",
                "saldo_primario_pil", "pressione_fiscale_ocse", "spesa_pubblica_pil", "occupazione_15_64",
                "occupazione_femminile_15_64", "disoccupazione_giovanile", "spread_bund", "inflazione", "fecondita",
                "emigrazione_cittadini", "laureati_25_34", "poverta_assoluta", "divario_nord_sud"]


def storia() -> dict:
    """50 anni di scelte: periodi ragionati, catalogo delle decisioni 1977-2026 e serie lunghe (cartella storia/)."""
    d = RADICE / "storia"
    if not d.exists():
        return {}
    dec = pd.read_csv(d / "decisioni_1977_2026.csv", dtype=str).fillna("")
    reg = pd.read_csv(d / "serie" / "_registro.csv", dtype=str).fillna("").set_index("nome")
    serie = {}
    for nome in SERIE_STORIA:
        f = d / "serie" / f"{nome}.csv"
        if not f.exists():
            continue
        t = pd.read_csv(f)
        t = t[(t.anno >= 1970) & (t.anno <= 2025)]
        r = reg.loc[nome] if nome in reg.index else {}
        serie[nome] = {"descrizione": r.get("descrizione", ""), "unita": r.get("unita", ""), "fonte": r.get("fonte", ""),
                       "url": r.get("url", ""),
                       "dati": {paese: [[int(x.anno), round(float(x.valore), 3)] for x in g.sort_values("anno").itertuples()]
                                for paese, g in t.groupby("paese")}}
    # Indice della ricchezza per abitante (1977 = 100) ricostruito dalla crescita annua: così c'è anche la Germania
    # prima del 1991 (Germania Ovest), che nella serie in livelli manca
    f = d / "serie" / "pil_pro_capite_crescita.csv"
    if f.exists():
        t = pd.read_csv(f)
        ind = {}
        for paese, g in t[t.paese.isin(["IT", "FR", "DE", "ES"])].groupby("paese"):
            g = g.set_index("anno").valore
            if 1977 not in g.index:
                continue
            v, righe = 100.0, [[1977, 100.0]]
            for anno in range(1978, 2026):
                if anno not in g.index:
                    break
                v *= 1 + float(g[anno]) / 100
                righe.append([anno, round(v, 2)])
            ind[paese] = righe
        serie = {"pil_pro_capite_indice": {"descrizione": "Indice del PIL pro capite reale, 1977 = 100, ricostruito da GovernAI concatenando la crescita annua AMECO (Germania: Germania Ovest fino al 1991).",
                                           "unita": "indice 1977 = 100", "fonte": "AMECO (Commissione europea), elaborazione GovernAI",
                                           "url": reg.loc["pil_pro_capite_crescita", "url"] if "pil_pro_capite_crescita" in reg.index else "", "dati": ind}, **serie}
    periodi = (yaml.safe_load(leggi(d / "periodi.yaml")) or {}).get("periodi", []) if (d / "periodi.yaml").exists() else []
    campi = ["id", "anno", "atto", "governo_anno", "presidente_consiglio", "ambito", "decisione", "cosa_cambia",
             "effetto_conti", "effetti_misurati", "giudizio", "solidita_evidenza", "fonti"]
    return {"periodi": periodi, "decisioni": dec[campi].to_dict("records"), "serie": serie}


def chi_paga() -> dict:
    """Chi paga davvero: aliquote effettive per gruppo (analisi/chi_paga/calcola.py) e numeri per gruppo (MEF)."""
    d = RADICE / "analisi" / "chi_paga"
    if not (d / "pagina.yaml").exists():
        return {}
    pag = yaml.safe_load(leggi(d / "pagina.yaml")) or {}
    r = pd.read_csv(d / "risultati.csv")
    righe = []
    for g in pag.get("gruppi", []):
        t = r[(r.gruppo == g["gruppo"]) & (r.variante == g["variante"])]
        righe.append({**g, "valori": {str(int(x.reddito_lordo)): [pulisci(x.aliquota_effettiva_imposte), pulisci(x.aliquota_effettiva_totale)]
                                      for x in t.itertuples()}})
    pop = pd.read_csv(d / "popolazione.csv", dtype=str).fillna("")
    neutr = d / "neutralita.csv"
    return {**{k: v for k, v in pag.items() if k != "gruppi"}, "gruppi": righe, "popolazione": pop.to_dict("records"),
            "neutralita": pd.read_csv(neutr).to_dict("records") if neutr.exists() else []}


def governi() -> dict:
    """Governi a confronto (storia/script/governi.py): indicatori per mandato, Italia rispetto a Francia, Germania e
    Spagna. Nella pagina i governi sono indicati per date: i nomi restano solo in storia/governi.csv come dato storico."""
    d = RADICE / "storia"
    if not (d / "governi_confronto.csv").exists():
        return {}
    def righe(f: Path) -> list:
        if not f.exists():
            return []
        c = pd.read_csv(f)
        c = c[c.confrontabile.astype(str).str.lower().isin(["si", "sì", "true", "1"])]
        return [{"u": r.unita_id, "g": r.governo_periodo, "v": r.versione, "anni": str(r.anni) if pd.notna(r.anni) else "",
                 "amb": r.ambito, "ind": r.indicatore, "um": r.unita_misura, "verso": r.verso,
                 "it": pulisci(r.valore_italia), "vic": pulisci(r.valore_vicini), "diff": pulisci(r.differenza),
                 "rango": pulisci(r.rango), "n": pulisci(r.n_confrontati), "base": r.base_del_rango if pd.notna(r.base_del_rango) else ""}
                for r in c.itertuples()]
    pag = yaml.safe_load(leggi(d / "governi_pagina.yaml")) if (d / "governi_pagina.yaml").exists() else {}
    pag = pag or {}
    # vista per legislatura (storia/script/legislature.py): stesse righe, testi propri
    if isinstance(pag.get("legislature"), dict):
        pag["legislature"] = {**pag["legislature"], "righe": righe(d / "legislature_confronto.csv")}
    return {**pag, "righe": righe(d / "governi_confronto.csv")}


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
        "osservatorio": osservatorio(),
        "mappa": mappa(),
        "comunita": {"regole": leggi(RADICE / "comunita" / "regole.md"), "privacy": leggi(RADICE / "comunita" / "privacy.md")},
        "lezioni": leggi(RADICE / "apprendimento" / "lezioni.md"),
        "integrita": integrita(),
        "governo": governo(),
        "europa": europa(),
        "costituzione": costituzione(),
        "motore": motore_web(),
        "proposte_validate": json.loads(leggi(RADICE / "proposte" / "validati.json") or "[]"),
        "storia": storia(),
        "chi_paga": chi_paga(),
        "governi": governi(),
        "quattro_domande": {k: v for f in sorted((RADICE / "programma").glob("quattro_domande_*.yaml"))
                            for k, v in ((yaml.safe_load(leggi(f)) or {}).get("proposte") or {}).items()},
        "oceano_blu": yaml.safe_load(leggi(RADICE / "programma" / "oceano_blu.yaml")) if (RADICE / "programma" / "oceano_blu.yaml").exists() else {},
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
