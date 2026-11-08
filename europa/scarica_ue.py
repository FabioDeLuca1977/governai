"""Monitoraggio quotidiano delle scelte dell'Unione europea che vincolano o orientano la politica italiana.

Fonti (provate l'8/11/2026; dettagli, scarti e limiti in README.md):
  1. CELLAR, endpoint SPARQL pubblico dell'Ufficio delle pubblicazioni (ontologia CDM), senza chiavi:
     - atti pubblicati nella Gazzetta ufficiale UE, serie L (direttive, regolamenti, decisioni, ...), con titolo
       italiano, descrittori EuroVoc, voci del repertorio, entrata in vigore e termini di recepimento annotati;
     - direttive con termine di recepimento nella finestra delle scadenze e misure nazionali di esecuzione
       NOTIFICATE DALL'ITALIA alla Commissione (classe cdm:measure_national_implementing);
     - proposte legislative della Commissione (COM ... PC);
     - documenti del Semestre europeo sull'Italia (raccomandazioni, relazioni per paese, procedura per disavanzo).
  2. CELLAR, contenuto: testo italiano (XHTML) delle direttive nuove e dell'ultima raccomandazione specifica per paese.
  3. EUR-Infra, area libera (Dipartimento per gli affari europei): elenco di tutte le procedure d'infrazione aperte.
  4. affarieuropei.gov.it: aggiornamenti periodici sullo stato delle infrazioni (sintesi).
  5. Commissione, DG ECFIN: cronologia della procedura per disavanzo eccessivo dell'Italia.

Archivio in europa/archivio/:
  atti.csv            atti della GU L (chiave: CELEX), con pertinenza (aree, proposte, esperti, impatto)
  direttive.csv       direttive con termine di recepimento nella finestra + misure italiane notificate
  proposte_ue.csv     proposte legislative della Commissione
  semestre.json       documenti del Semestre sull'Italia, cronologia della procedura per disavanzo, raccomandazioni
  infrazioni_storico.csv  procedure viste in EUR-Infra: prima e ultima rilevazione, cambi di fase
  testi/AAAA/<CELEX>.txt  testo italiano di direttive e raccomandazioni
  cache/              ultima copia delle pagine HTML (usata se la fonte non risponde)
  stato.json          ultima data GU elaborata, esito di ogni fonte, numero di richieste

Uso:
  python scarica_ue.py                  # aggiorna (prima volta: ultimi 60 giorni di GU L)
  python scarica_ue.py --giorni 90      # finestra iniziale più ampia
  python scarica_ue.py --dal 2026-09-01 # da una data precisa (ignora lo stato)
  python scarica_ue.py --senza-testi    # non scarica i testi
  python scarica_ue.py --solo-uscite    # rigenera solo le uscite dall'archivio, senza rete
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # anche con python -I
import requests

from rete import (ARCHIVIO, CELEX_URI, DPE_INFRAZIONI, ECFIN_EDP_ITALIA, EURINFRA, EURLEX, STATO_ARCHIVIO, TESTI, Rete,
                  data_italiana, html_a_testo, leggi_json, pulisci_spazi, scarica_con_cache, scrivi_json)

ATTI = ARCHIVIO / "atti.csv"
DIRETTIVE = ARCHIVIO / "direttive.csv"
PROPOSTE_UE = ARCHIVIO / "proposte_ue.csv"
SEMESTRE = ARCHIVIO / "semestre.json"
INF_STORICO = ARCHIVIO / "infrazioni_storico.csv"

CAMPI_ATTI = ["celex", "eli", "tipo_codice", "tipo", "data_gu", "data_atto", "rif_gu", "titolo", "eurovoc", "repertorio",
              "entrata_in_vigore", "termine_recepimento", "termini", "termine_testo", "in_vigore", "autori", "destinatari",
              "url_eurlex", "testo", "aggiornato"]
CAMPI_DIR = ["celex", "eli", "tipo_codice", "tipo", "data_atto", "data_gu", "titolo", "eurovoc", "repertorio",
             "termine_recepimento", "termini", "in_vigore", "misure_it", "ultima_notifica_it", "esempio_misura_it",
             "url_eurlex", "url_misure_nazionali"]
CAMPI_PROP = ["celex", "tipo_codice", "tipo", "data_atto", "numero_com", "titolo", "eurovoc", "repertorio", "url_eurlex",
              "url_procedura"]
CAMPI_INF_ST = ["numero", "prima_rilevazione", "ultima_rilevazione", "fase", "cambio_fase", "fasi_precedenti", "aperta", "chiusa_il"]

RT = "http://publications.europa.eu/resource/authority/resource-type/"
TIPI = {
    "DIR": "Direttiva", "DIR_DEL": "Direttiva delegata", "DIR_IMPL": "Direttiva di esecuzione",
    "REG": "Regolamento", "REG_DEL": "Regolamento delegato", "REG_IMPL": "Regolamento di esecuzione",
    "REG_FINANC": "Regolamento finanziario",
    "DEC": "Decisione", "DEC_DEL": "Decisione delegata", "DEC_IMPL": "Decisione di esecuzione",
    "DEC_ADOPT_INTERNATION": "Decisione su un atto internazionale", "REG_ADOPT_INTERNATION": "Regolamento su un atto internazionale",
    "RECO": "Raccomandazione", "GUIDELINE": "Indirizzo", "RES": "Risoluzione", "AGREE_INTERNATION": "Accordo internazionale",
    "AGREE_PROT": "Protocollo", "PROC_RULES": "Regolamento interno", "BUDGET_SUPPL_AMEND": "Bilancio rettificativo",
    "CORRIGENDUM": "Rettifica",
    "PROP_REG": "Proposta di regolamento", "PROP_DIR": "Proposta di direttiva", "PROP_DEC": "Proposta di decisione",
}
# priorità per scegliere il tipo "principale" quando un'opera ne ha più d'uno (es. rettifica di una direttiva)
ORDINE_TIPI = ["CORRIGENDUM", "DIR", "DIR_DEL", "DIR_IMPL", "REG", "REG_DEL", "REG_IMPL", "DEC", "DEC_DEL", "DEC_IMPL"]
CORPI = {"EP": "Parlamento europeo", "CONSIL": "Consiglio", "COM": "Commissione", "ECB": "BCE", "EUMS": "Stati membri",
         "ITA": "Italia"}

PREFISSI = """PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX annot: <http://publications.europa.eu/ontology/annotation#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
"""
ITA = "<http://publications.europa.eu/resource/authority/language/ITA>"
ENG = "<http://publications.europa.eu/resource/authority/language/ENG>"


# --- Selettori: legano ?w alle opere da elaborare --------------------------------------------------------

def sel_gu(dal: str, al: str) -> str:
    return (f'?w cdm:official-journal-act_date_publication ?dsel ; '
            f'cdm:official-journal-act_part_of_collection_document <http://publications.europa.eu/resource/authority/document-collection/OJ-L> . '
            f'FILTER(?dsel >= "{dal}"^^xsd:date && ?dsel <= "{al}"^^xsd:date)')


def sel_direttive(dal: str, al: str) -> str:
    return (f'?w cdm:directive_date_transposition ?dsel . FILTER(?dsel >= "{dal}"^^xsd:date && ?dsel <= "{al}"^^xsd:date) '
            f'?w cdm:resource_legal_id_celex ?csel . FILTER(!CONTAINS(STR(?csel), "R("))')


def sel_proposte(dal: str, al: str) -> str:
    return (f'?w cdm:work_date_document ?dsel ; cdm:work_has_resource-type ?tsel ; cdm:resource_legal_id_celex ?csel . '
            f'VALUES ?tsel {{ <{RT}PROP_REG> <{RT}PROP_DIR> <{RT}PROP_DEC> }} '
            f'FILTER(STRSTARTS(STR(?csel), "5")) FILTER(?dsel >= "{dal}"^^xsd:date && ?dsel <= "{al}"^^xsd:date)')


# Nessuna aggregazione (MIN, SAMPLE, GROUP_CONCAT) nelle query: provate l'8/11/2026, sull'endpoint di CELLAR davano
# valori diversi da un'esecuzione all'altra (date di altri atti). Si scaricano righe grezze e si aggrega in Python.
PROPRIETA_BASE = ["resource_legal_id_celex", "official-journal-act_date_publication", "work_date_document",
                  "resource_legal_eli", "resource_legal_reference_oj-act", "resource_legal_date_entry-into-force",
                  "resource_legal_in-force", "work_has_resource-type", "work_created_by_agent",
                  "resource_legal_addresses_institution", "work_id_document"]


def q_base(sel: str) -> str:
    valori = " ".join(f"cdm:{x}" for x in PROPRIETA_BASE)
    return PREFISSI + f"""SELECT DISTINCT ?w ?p ?o WHERE {{ {{ SELECT DISTINCT ?w WHERE {{ {sel} }} }}
 VALUES ?p {{ {valori} }} ?w ?p ?o . }}"""


def q_titoli(sel: str) -> str:
    # titolo italiano; se manca (succede per le rettifiche che non toccano la versione italiana) il titolo inglese
    return PREFISSI + f"""SELECT DISTINCT ?w ?lingua ?t WHERE {{ {{ SELECT DISTINCT ?w WHERE {{ {sel} }} }}
 VALUES ?lingua {{ {ITA} {ENG} }}
 ?e cdm:expression_belongs_to_work ?w ; cdm:expression_uses_language ?lingua ; cdm:expression_title ?t . }}"""


def q_eurovoc(sel: str) -> str:
    return PREFISSI + f"""SELECT DISTINCT ?w ?l WHERE {{ {{ SELECT DISTINCT ?w WHERE {{ {sel} }} }}
 ?w cdm:work_is_about_concept_eurovoc ?c . ?c skos:prefLabel ?l . FILTER(lang(?l) = "it") }}"""


def q_repertorio(sel: str) -> str:
    return PREFISSI + f"""SELECT DISTINCT ?w ?c ?l WHERE {{ {{ SELECT DISTINCT ?w WHERE {{ {sel} }} }}
 ?w cdm:resource_legal_is_about_concept_directory-code ?c .
 OPTIONAL {{ ?c skos:prefLabel ?l . FILTER(lang(?l) = "it") }} }}"""


def q_termini(sel: str) -> str:
    return PREFISSI + f"""SELECT DISTINCT ?w ?data ?nota WHERE {{ {{ SELECT DISTINCT ?w WHERE {{ {sel} }} }}
 ?w cdm:directive_date_transposition ?data .
 OPTIONAL {{ ?ax owl:annotatedSource ?w ; owl:annotatedProperty cdm:directive_date_transposition ; owl:annotatedTarget ?data ;
             annot:comment_on_date ?nota }} }}"""


def q_misure_it(sel: str) -> str:
    # righe grezze, aggregate in Python: l'aggregazione MAX/COUNT dentro l'endpoint ha dato date non coerenti tra esecuzioni
    return PREFISSI + f"""SELECT DISTINCT ?w ?m ?dn ?tm
WHERE {{ {{ SELECT DISTINCT ?w WHERE {{ {sel} }} }}
 ?m cdm:measure_national_implementing_implements_resource_legal ?w ;
    cdm:measure_national_implementing_implemented_by_country <http://publications.europa.eu/resource/authority/country/ITA> .
 OPTIONAL {{ ?m cdm:measure_national_implementing_date_notification ?dn }}
 OPTIONAL {{ ?m cdm:work_title ?tm }} }}"""


Q_SEMESTRE = PREFISSI + """SELECT DISTINCT ?celex ?data ?tipo ?titolo WHERE {
 ?w cdm:work_date_document ?data ; cdm:resource_legal_id_celex ?celex .
 FILTER(?data >= "%s"^^xsd:date)
 ?e cdm:expression_belongs_to_work ?w ; cdm:expression_uses_language <http://publications.europa.eu/resource/authority/language/ITA> ;
    cdm:expression_title ?titolo .
 FILTER(CONTAINS(?titolo, "Italia"))
 FILTER(CONTAINS(LCASE(?titolo), "disavanzo") || CONTAINS(LCASE(?titolo), "politiche economiche") ||
        CONTAINS(LCASE(?titolo), "piano nazionale strutturale") || CONTAINS(LCASE(?titolo), "piano strutturale") ||
        CONTAINS(LCASE(?titolo), "documento programmatico di bilancio") || CONTAINS(LCASE(?titolo), "relazione per paese") ||
        CONTAINS(LCASE(?titolo), "squilibri macroeconomici") || CONTAINS(LCASE(?titolo), "ripresa e resilienza") ||
        CONTAINS(LCASE(?titolo), "clausola di salvaguardia"))
 OPTIONAL { ?w cdm:work_has_resource-type ?tipo }
} ORDER BY DESC(?data)"""


# --- Atti -------------------------------------------------------------------------------------------------

def codice_tipo(tipi: str, celex: str) -> str:
    codici = [t.rsplit("/", 1)[-1] for t in tipi.split() if t]
    if "R(" in celex:
        return "CORRIGENDUM"
    for c in ORDINE_TIPI:
        if c in codici:
            return c
    return codici[0] if codici else ""


def corpi(uris: str) -> str:
    return ", ".join(sorted({CORPI.get(u.rsplit("/", 1)[-1], u.rsplit("/", 1)[-1]) for u in uris.split() if u}))


def termini_da_righe(righe: list[dict], da: str = "", a: str = "9999") -> dict[str, tuple[str, str]]:
    """{w: (termine_recepimento, 'AAAA-MM-GG adozione; AAAA-MM-GG applicazione; ...')}.
    Termine di recepimento = la prima data annotata come ADOPTION (adozione delle misure nazionali) che cade nella
    finestra [da, a]; se nessuna è annotata, la prima data della finestra. Le direttive modificate più volte hanno
    più termini: quelli fuori finestra restano nell'elenco completo."""
    per_w: dict[str, list[tuple[str, str]]] = {}
    for r in righe:
        nota = r.get("nota", "")
        etichetta = ("adozione" if "ADOPTION" in nota else "applicazione" if "APPLICATION" in nota
                     else "comunicazione" if "NOTIFICATION" in nota else "non annotata")
        art = re.search(r"\{ART\|[^}]*\}\s*([\w.()]+)", nota)
        per_w.setdefault(r["w"], []).append((r["data"][:10], etichetta + (f" art. {art.group(1)}" if art else "")))
    out = {}
    for w, lista in per_w.items():
        lista = sorted(set(x for x in lista if not x[0].startswith("1001")))
        nella = [(d, e) for d, e in lista if da <= d <= a] or lista
        adoz = [d for d, e in nella if e.startswith("adozione")]
        termine = min(adoz) if adoz else (nella[0][0] if nella else "")
        out[w] = (termine, "; ".join(f"{d} {e}" for d, e in lista))
    return out


def interroga(rete: Rete, sel: str, termini: bool = False, misure: bool = False,
              finestra: tuple[str, str] = ("", "9999")) -> dict[str, dict]:
    """Interroga CELLAR con il selettore e restituisce {w: record} con tutti i metadati."""
    val: dict[str, dict[str, set]] = {}
    for b in rete.sparql(q_base(sel)):
        val.setdefault(b["w"], {}).setdefault(b["p"].rsplit("#", 1)[-1], set()).add(b["o"])
    primo = lambda v, k: min(v.get(k, {""}))
    rec = {}
    for w, v in val.items():
        celex = sorted(v.get("resource_legal_id_celex", {""}), key=lambda c: ("R(" in c, len(c), c))[0]
        tipi = " ".join(sorted(v.get("work_has_resource-type", set())))
        cod = codice_tipo(tipi, celex)
        com = sorted(x for x in v.get("work_id_document", set()) if x.startswith("comnat:"))
        rec[w] = {
            "celex": celex, "eli": primo(v, "resource_legal_eli"), "tipo_codice": cod, "tipo": TIPI.get(cod, cod),
            "data_gu": primo(v, "official-journal-act_date_publication")[:10], "data_atto": primo(v, "work_date_document")[:10],
            "rif_gu": primo(v, "resource_legal_reference_oj-act"), "titolo": "", "eurovoc": "", "repertorio": "",
            "entrata_in_vigore": primo(v, "resource_legal_date_entry-into-force")[:10],
            "termine_recepimento": "", "termini": "", "termine_testo": "", "in_vigore": max(v.get("resource_legal_in-force", {""})),
            "autori": corpi(" ".join(v.get("work_created_by_agent", set()))),
            "destinatari": corpi(" ".join(v.get("resource_legal_addresses_institution", set()))),
            "numero_com": com[0].replace("comnat:", "") if com else "", "url_eurlex": f"{EURLEX}/TXT/?uri=CELEX:{celex}", "testo": "",
        }
    titoli: dict[str, dict[str, str]] = {}
    for b in rete.sparql(q_titoli(sel)):
        lingua = b["lingua"].rsplit("/", 1)[-1]
        if b["w"] in rec and (lingua not in titoli.setdefault(b["w"], {}) or b["t"] < titoli[b["w"]][lingua]):
            titoli[b["w"]][lingua] = b["t"]
    for w, r in rec.items():
        t = titoli.get(w, {})
        r["titolo"] = t.get("ITA") or (f"[solo in inglese] {t['ENG']}" if t.get("ENG") else "")
        if not r["titolo"] and "R(" in r["celex"]:
            r["titolo"] = f"Rettifica dell'atto CELEX {r['celex'].split('R(')[0]} (titolo della rettifica non disponibile in CELLAR)"
    ev: dict[str, set] = {}
    for b in rete.sparql(q_eurovoc(sel)):
        ev.setdefault(b["w"], set()).add(b["l"])
    rep: dict[str, set] = {}
    for b in rete.sparql(q_repertorio(sel)):
        rep.setdefault(b["w"], set()).add(b["c"].rsplit("/", 1)[-1] + "=" + b.get("l", ""))
    for w, r in rec.items():
        r["eurovoc"] = "|".join(sorted(ev.get(w, set())))
        r["repertorio"] = "|".join(sorted(rep.get(w, set())))
    if termini:
        for w, (t, tutti) in termini_da_righe(rete.sparql(q_termini(sel)), *finestra).items():
            if w in rec:
                rec[w]["termine_recepimento"], rec[w]["termini"] = t, tutti
    if misure:
        for r in rec.values():
            r.update(misure_it=0, ultima_notifica_it="", esempio_misura_it="")
        per_w: dict[str, dict[str, tuple[str, str]]] = {}
        for b in rete.sparql(q_misure_it(sel)):
            m = per_w.setdefault(b["w"], {})
            d, t = b.get("dn", "")[:10], b.get("tm", "")
            if b["m"] not in m or (d, t) > m[b["m"]]:
                m[b["m"]] = (d, t)
        for w, misure in per_w.items():
            if w in rec:
                date_ok = sorted(d for d, _ in misure.values() if d and not d.startswith("1001"))
                ultima = max(misure.values())  # la misura notificata più di recente
                rec[w].update(misure_it=len(misure), ultima_notifica_it=date_ok[-1] if date_ok else "",
                              esempio_misura_it=ultima[1])
    return rec


def leggi_csv(p: Path) -> list[dict]:
    if not p.exists():
        return []
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def scrivi_csv(p: Path, righe: list[dict], campi: list[str]) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campi, extrasaction="ignore")
        w.writeheader()
        w.writerows(righe)


def finestre(dal: date, al: date, giorni: int = 7):
    d = dal
    while d <= al:
        fine = min(al, d + timedelta(days=giorni - 1))
        yield d.isoformat(), fine.isoformat()
        d = fine + timedelta(days=1)


# --- Testi ------------------------------------------------------------------------------------------------

RE_RECEPIMENTO = re.compile(
    r"Gli Stati membri (?:mettono in vigore|adottano e pubblicano)[^.]{0,400}?entro (?:e non oltre )?(?:il\s+)?"
    r"(\d{1,2}\s*(?:o|º|°)?\s+\w+\s+\d{4})", re.S)


def scarica_testo(rete: Rete, celex: str, anno: str) -> tuple[str, str]:
    """Testo italiano dell'atto da CELLAR (XHTML o HTML). Restituisce (percorso relativo, termine dal testo)."""
    r = rete.get(CELEX_URI + celex, headers={"Accept": "application/xhtml+xml, text/html;q=0.9", "Accept-Language": "ita"},
                 timeout=180)
    testo = html_a_testo(r.content.decode("utf-8", errors="replace"))
    dest = TESTI / anno / f"{re.sub(r'[^0-9A-Za-z()_-]', '_', celex)}.txt"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(testo, encoding="utf-8")
    return dest.relative_to(ARCHIVIO).as_posix(), termine_da_testo(testo)


def termine_da_testo(testo: str) -> str:
    """Prima data della clausola di recepimento ("Gli Stati membri mettono in vigore ... entro il ..."): controllo dei metadati."""
    m = RE_RECEPIMENTO.search(testo)
    return data_italiana(m.group(1)) if m else ""


# --- Semestre europeo ---------------------------------------------------------------------------------------

def semestre(rete: Rete, esiti: dict, scarica_testi: bool) -> dict:
    vecchio = leggi_json(SEMESTRE, {}) or {}
    out = {"aggiornato": date.today().isoformat(), "documenti": [], "edp_cronologia": [], "csr": vecchio.get("csr", {})}
    try:
        righe = rete.sparql(Q_SEMESTRE % "2024-01-01")
        visti = {}
        for r in righe:
            c = r["celex"]
            tipo = r.get("tipo", "").rsplit("/", 1)[-1]
            if c not in visti or (tipo and not visti[c]["tipo"]):
                visti[c] = {"celex": c, "data": r["data"][:10], "tipo": tipo, "titolo": r["titolo"],
                            "url": f"{EURLEX}/TXT/?uri=CELEX:{c}"}
        out["documenti"] = sorted(visti.values(), key=lambda x: (x["data"], x["celex"]), reverse=True)
        esiti["cellar_semestre"] = f"ok: {len(visti)} documenti"
    except requests.RequestException as e:
        out["documenti"] = vecchio.get("documenti", [])
        esiti["cellar_semestre"] = f"errore: {e.__class__.__name__}; uso l'archivio"

    # ultima raccomandazione del Consiglio sulle politiche economiche dell'Italia (atto definitivo, settore 3)
    csr = [d for d in out["documenti"] if d["celex"].startswith("3") and "politiche economiche" in d["titolo"].lower()
           and d["titolo"].lower().startswith("raccomandazione del consiglio")]
    if csr and scarica_testi and csr[0]["celex"] != out["csr"].get("celex"):
        try:
            rel, _ = scarica_testo(rete, csr[0]["celex"], csr[0]["data"][:4])
            out["csr"] = {"celex": csr[0]["celex"], "data": csr[0]["data"], "titolo": csr[0]["titolo"], "testo": rel,
                          "url": csr[0]["url"]}
            esiti["cellar_testo_csr"] = "ok"
        except requests.RequestException as e:
            esiti["cellar_testo_csr"] = f"errore: {e.__class__.__name__}"
    if out["csr"].get("testo"):
        testo = (ARCHIVIO / out["csr"]["testo"]).read_text(encoding="utf-8")
        out["csr"].update(estrai_csr(testo))

    # cronologia della procedura per disavanzo eccessivo (DG ECFIN)
    try:
        t, esito = scarica_con_cache(rete, ECFIN_EDP_ITALIA, "ecfin_edp_italia.html")
        out["edp_cronologia"] = cronologia_edp(t)
        out["edp_pagina"] = {"url": ECFIN_EDP_ITALIA, "procedura_in_corso": bool(re.search(r"Ongoing procedure", t)),
                             "revisione": (re.search(r"last reviewed on ([^<]+)", t) or [None, ""])[1].strip()}
        esiti["ecfin_edp"] = f"{esito}: {len(out['edp_cronologia'])} passaggi"
    except requests.RequestException as e:
        out["edp_cronologia"] = vecchio.get("edp_cronologia", [])
        out["edp_pagina"] = vecchio.get("edp_pagina", {})
        esiti["ecfin_edp"] = f"errore: {e.__class__.__name__}"
    scrivi_json(SEMESTRE, out)
    return out


def estrai_csr(testo: str) -> dict:
    """Dal testo della raccomandazione: le raccomandazioni numerate e le frasi su disavanzo e spesa netta (citazioni testuali)."""
    t = re.sub(r"\s+", " ", testo)
    racc = []
    m = re.search(r"RACCOMANDA all'Italia (.*?)(?:Fatto a |Per il Consiglio)", t)
    intro = ""
    if m:
        corpo = m.group(1)
        intro = "RACCOMANDA all'Italia " + re.split(r"\s1\.\s", corpo, maxsplit=1)[0].strip()
        racc = [x.strip() for x in re.split(r"\s(?=\d\.\s{1,3}[A-ZÈ])", " " + corpo)[1:]]
        racc = [re.sub(r"^\d\.\s*", "", x).strip() for x in racc]
    frasi = re.split(r"(?<=[.;])\s+(?=[A-Z(])", t)
    edp = [f for f in frasi if re.search(r"procedura per i disavanzi eccessivi|disavanzo eccessivo", f) and len(f) < 900]
    spesa = [f for f in frasi if "tassi massimi di crescita della spesa netta" in f or "spesa netta in Italia" in f]
    spesa = [f for f in spesa if len(f) < 900]
    return {"raccomandazioni_intro": intro, "raccomandazioni": racc, "frasi_edp": edp[:6], "frasi_spesa_netta": spesa[:6]}


def cronologia_edp(t: str) -> list[dict]:
    m = re.search(r"Ongoing procedure</h2>(.*?)</table>", t, flags=re.S)
    if not m:
        return []
    out = []
    for riga in re.findall(r"<tr[^>]*>(.*?)</tr>", m.group(1), flags=re.S):
        celle = re.findall(r"<td[^>]*>(.*?)</td>", riga, flags=re.S)
        if len(celle) != 3:
            continue
        link = re.search(r'href="([^"]+)"', celle[1])
        url = link.group(1) if link else ""
        if url.startswith("/"):
            url = "https://economy-finance.ec.europa.eu" + url
        out.append({"articolo": pulisci_spazi(html_a_testo(celle[0])), "passaggio": pulisci_spazi(html_a_testo(celle[1])),
                    "data": pulisci_spazi(html_a_testo(celle[2])), "url": url})
    return out


# --- Infrazioni ---------------------------------------------------------------------------------------------

def infrazioni(rete: Rete, esiti: dict) -> list[dict]:
    """Elenco delle procedure aperte da EUR-Infra (area libera) e storico delle rilevazioni."""
    try:
        t, esito = scarica_con_cache(rete, EURINFRA, "eurinfra.html")
    except requests.RequestException as e:
        esiti["eurinfra"] = f"errore: {e.__class__.__name__}"
        return []
    tot = re.search(r"Elenco Procedure:\s*(\d+)", t)
    righe = []
    for blocco in re.findall(r"<tr class=\"(?:Even|Odd)\">(.*?)</tr>", t, flags=re.S):
        celle = dict(re.findall(r'<td headers="(\w+)">(.*?)</td>', blocco, flags=re.S))
        if not celle.get("NumProc"):
            continue
        righe.append({k: pulisci_spazi(html_a_testo(v)) for k, v in celle.items()})
    esiti["eurinfra"] = f"{esito}: {len(righe)} procedure" + (f" (il sito dichiara {tot.group(1)})" if tot else "")

    oggi = date.today().isoformat()
    storico = {r["numero"]: r for r in leggi_csv(INF_STORICO)}
    aperte = set()
    for r in righe:
        n = r["NumProc"]
        aperte.add(n)
        s = storico.get(n)
        if not s:
            storico[n] = {"numero": n, "prima_rilevazione": oggi, "ultima_rilevazione": oggi, "fase": r.get("Fase", ""),
                          "fasi_precedenti": "", "aperta": "sì"}
        else:
            if s["fase"] != r.get("Fase", ""):
                s["fasi_precedenti"] = "; ".join(x for x in [s["fasi_precedenti"], f"{s['fase']} (fino al {s['ultima_rilevazione']})"] if x)
                s["fase"], s["cambio_fase"] = r.get("Fase", ""), oggi
            s.update(ultima_rilevazione=oggi, aperta="sì", chiusa_il="")
    if righe:  # se la pagina non ha righe non si chiude nulla
        for n, s in storico.items():
            if n not in aperte and s.get("aperta") != "no":
                s["aperta"], s["chiusa_il"] = "no", oggi  # archiviata o non più elencata
    scrivi_csv(INF_STORICO, sorted(storico.values(), key=lambda x: x["numero"], reverse=True), CAMPI_INF_ST)
    return righe


def aggiornamenti_dpe(rete: Rete, esiti: dict) -> list[dict]:
    """Sintesi degli ultimi aggiornamenti pubblicati dal Dipartimento per gli affari europei."""
    try:
        t, esito = scarica_con_cache(rete, DPE_INFRAZIONI, "dpe_infrazioni.html", timeout=90)
    except requests.RequestException as e:
        esiti["dpe_aggiornamenti"] = f"errore: {e.__class__.__name__}"
        return []
    out = []
    voci = list(re.finditer(r'href="(/it/attivita/procedure-dinfrazione/stato-delle-infrazioni/[^"]+/)"[^>]*>\s*'
                            r'(Infrazioni, aggiornamento[^<]+)<', t))
    for k, m in enumerate(voci):
        fine = voci[k + 1].start() if k + 1 < len(voci) else len(t)
        corpo = pulisci_spazi(html_a_testo(t[m.end():fine]))
        sintesi = re.search(r"(La Commissione europea.*?(?:direttive|dell'Unione)\.)", corpo)
        titolo = pulisci_spazi(html_a_testo(m.group(2)))
        out.append({"titolo": titolo, "sintesi": sintesi.group(1) if sintesi else "", "data": data_italiana(titolo),
                    "url": "https://www.affarieuropei.gov.it" + m.group(1)})
    esiti["dpe_aggiornamenti"] = f"{esito}: {len(out)} aggiornamenti"
    return out[:6]


# --- Principale --------------------------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--giorni", type=int, default=60, help="finestra iniziale in giorni (default 60)")
    ap.add_argument("--dal", help="data iniziale AAAA-MM-GG della GU L (ignora lo stato)")
    ap.add_argument("--senza-testi", action="store_true", help="non scarica i testi")
    ap.add_argument("--solo-uscite", action="store_true", help="rigenera le uscite dall'archivio, senza rete")
    ap.add_argument("--pausa", type=float, default=1.0, help="secondi tra due richieste (min 0,5)")
    a = ap.parse_args()

    import pertinenza
    import uscite

    if a.solo_uscite:
        print(uscite.genera())
        return 0

    ARCHIVIO.mkdir(parents=True, exist_ok=True)
    rete = Rete(max(0.5, a.pausa))
    stato = leggi_json(STATO_ARCHIVIO, {}) or {}
    oggi = date.today()
    esiti: dict[str, str] = {}
    regole = pertinenza.Regole()

    # 1. atti della GU L: incrementale con sovrapposizione di 7 giorni (CELLAR completa i metadati nei giorni successivi)
    if a.dal:
        dal = date.fromisoformat(a.dal)
    elif stato.get("ultima_data_gu"):
        dal = date.fromisoformat(stato["ultima_data_gu"]) - timedelta(days=7)
    else:
        dal = oggi - timedelta(days=a.giorni)
    atti = {r["celex"]: r for r in leggi_csv(ATTI)}
    nuovi = 0
    try:
        for d1, d2 in finestre(dal, oggi):
            rec = interroga(rete, sel_gu(d1, d2), termini=True)
            for r in rec.values():
                if not r["celex"]:
                    continue
                vecchio = atti.get(r["celex"])
                if vecchio:  # conserva testo e termine dal testo già ottenuti
                    r["testo"], r["termine_testo"] = vecchio.get("testo", ""), vecchio.get("termine_testo", "")
                else:
                    nuovi += 1
                r["aggiornato"] = oggi.isoformat()
                atti[r["celex"]] = r
            print(f"GU L {d1} - {d2}: {len(rec)} atti")
        stato["ultima_data_gu"] = oggi.isoformat()
        stato.setdefault("inizio", dal.isoformat())
        if dal.isoformat() < stato["inizio"]:
            stato["inizio"] = dal.isoformat()
        esiti["cellar_gu_l"] = f"ok: {nuovi} atti nuovi dal {dal.isoformat()}"
    except (requests.RequestException, KeyError, ValueError) as e:
        esiti["cellar_gu_l"] = f"errore: {e.__class__.__name__}: {str(e)[:150]}"

    # 2. testi italiani delle direttive (non delle rettifiche): servono per il controllo del termine di recepimento
    for r in atti.values():  # testi già in archivio: rilegge la clausola (nessuna richiesta di rete)
        if r.get("testo") and not r.get("termine_testo") and (ARCHIVIO / r["testo"]).exists():
            r["termine_testo"] = termine_da_testo((ARCHIVIO / r["testo"]).read_text(encoding="utf-8"))
    if not a.senza_testi:
        da_fare = [r for r in atti.values() if r["tipo_codice"].startswith("DIR") and not r.get("testo")]
        ok = 0
        for r in da_fare:
            try:
                r["testo"], r["termine_testo"] = scarica_testo(rete, r["celex"], (r["data_gu"] or r["data_atto"])[:4])
                ok += 1
            except requests.RequestException as e:
                print(f"testo {r['celex']}: {e.__class__.__name__}")
        esiti["cellar_testi"] = f"{ok}/{len(da_fare)} testi di direttive"
    scrivi_csv(ATTI, sorted(atti.values(), key=lambda x: (x["data_gu"], x["celex"]), reverse=True), CAMPI_ATTI)

    # 3. direttive con termine di recepimento nella finestra + misure italiane notificate (rifatto per intero ogni giorno)
    f = regole.finestre
    d_da = (oggi - timedelta(days=round(30.44 * f["scadenze_passato_mesi"]))).isoformat()
    d_a = (oggi + timedelta(days=round(30.44 * f["scadenze_futuro_mesi"]))).isoformat()
    try:
        rec = interroga(rete, sel_direttive(d_da, d_a), termini=True, misure=True, finestra=(d_da, d_a))
        righe = []
        for r in rec.values():
            r["url_misure_nazionali"] = f"{EURLEX}/NIM/?uri=CELEX:{r['celex']}"
            righe.append(r)
        scrivi_csv(DIRETTIVE, sorted(righe, key=lambda x: (x["termine_recepimento"], x["celex"])), CAMPI_DIR)
        esiti["cellar_direttive"] = f"ok: {len(righe)} direttive con termine tra {d_da} e {d_a}"
    except (requests.RequestException, KeyError, ValueError) as e:
        esiti["cellar_direttive"] = f"errore: {e.__class__.__name__}: {str(e)[:150]}; uso l'archivio"

    # 4. proposte legislative della Commissione
    try:
        p_da = (oggi - timedelta(days=f["proposte_giorni"])).isoformat()
        rec = interroga(rete, sel_proposte(p_da, oggi.isoformat()))
        prop = {r["celex"]: r for r in leggi_csv(PROPOSTE_UE)}
        for r in rec.values():
            r["url_procedura"] = f"{EURLEX}/HIS/?uri=CELEX:{r['celex']}"
            prop[r["celex"]] = r
        scrivi_csv(PROPOSTE_UE, sorted(prop.values(), key=lambda x: (x["data_atto"], x["celex"]), reverse=True), CAMPI_PROP)
        esiti["cellar_proposte"] = f"ok: {len(rec)} proposte dal {p_da}"
    except (requests.RequestException, KeyError, ValueError) as e:
        esiti["cellar_proposte"] = f"errore: {e.__class__.__name__}"

    # 5. Semestre europeo e regole di bilancio
    semestre(rete, esiti, not a.senza_testi)

    # 6. infrazioni
    inf = infrazioni(rete, esiti)
    agg = aggiornamenti_dpe(rete, esiti)
    stato["infrazioni_prima_esecuzione"] = stato.get("infrazioni_prima_esecuzione") or (oggi.isoformat() if inf else "")
    stato["dpe_aggiornamenti"] = agg or stato.get("dpe_aggiornamenti", [])
    if inf:
        scrivi_csv(ARCHIVIO / "infrazioni_eurinfra.csv", inf, list(inf[0].keys()))

    stato.update(ultima_esecuzione=datetime.now().isoformat(timespec="seconds"), fonti=esiti, richieste=rete.richieste)
    scrivi_json(STATO_ARCHIVIO, stato)
    for k, v in esiti.items():
        print(f"  {k}: {v}")

    # 7. uscite per il resto del sistema
    riepilogo = uscite.genera()
    errori = [k for k, v in esiti.items() if v.startswith("errore")]
    print(f"{riepilogo}; richieste {rete.richieste}" + (f"; ERRORI: {', '.join(errori)}" if errori else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
