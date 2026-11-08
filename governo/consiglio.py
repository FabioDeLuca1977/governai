"""Consiglio dei ministri di GovernAI: un governo ombra con regole di decisione verificabili.

Il Consiglio riunisce nove ministri, un'opposizione leale e un capo di governo, ciascuno svolto da un agente
distinto (vedi regolamento.md e ruoli/). Questo script fa la parte deterministica, che nessun agente può aggirare:

  1. --prepara   ordine del giorno e contesto dai dati del giorno (allerte, programma del momento, fondi,
                 mandati aperti, credibilità) e un incarico scritto per ogni ruolo, esperti compresi.
                 Con --richiesta FILE la seduta risponde a una domanda (convocazione a richiesta);
  2. --componi   legge posizioni, obiezioni e decisioni; scarta ciò che viola il regolamento (linee rosse,
                 previsioni non verificabili, deroghe non dichiarate); verifica con l'ottimizzatore che le
                 decisioni siano finanziabili senza deficit; scrive il verbale e registra previsioni e mandati;
  3. --valuta    confronta le previsioni scadute con i dati ufficiali e aggiorna la credibilità di ogni ruolo.

Ordine dei lavori: esperti (pareri tecnici) -> ministri -> opposizione -> capo di governo -> --componi.

Uso (dalla radice del repository o da qualsiasi cartella):
  python governo/consiglio.py --prepara [--motivo "testo"]   -> governo/sedute/AAAA-MM-GG/
  python governo/consiglio.py --prepara --richiesta governo/richieste/NOME.md [--ministri 01,06] [--esperti id1,id2]
  python governo/consiglio.py --componi governo/sedute/AAAA-MM-GG
  python governo/consiglio.py --valuta
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

import pandas as pd
import yaml

QUI = Path(__file__).resolve().parent
RADICE = QUI.parent
sys.path.insert(0, str(RADICE / "sistema"))
sys.path.insert(0, str(RADICE / "programma"))

SEDUTE = QUI / "sedute"
VERBALI = QUI / "verbali"
PREVISIONI = QUI / "previsioni.csv"
MANDATI = QUI / "mandati.csv"
CREDIBILITA = QUI / "credibilita.csv"
ESPERTI = QUI / "esperti.yaml"
RICHIESTE = QUI / "richieste"
MAX_ESPERTI = 6
CAMPI_PREV = ["id", "seduta", "autore", "indicatore", "condizione", "soglia", "periodo", "probabilita",
              "condizionata_a", "esito", "valore", "brier"]
CAMPI_MAND = ["id", "seduta", "area", "compito", "scadenza", "stato", "chiuso_il"]

MINISTERI = {
    "01": ("Ministro dell'economia e delle imprese", "ministeri/01_economia_imprese.md"),
    "02": ("Ministro del lavoro, del welfare e della famiglia", "ministeri/02_lavoro_welfare_famiglia.md"),
    "03": ("Ministro dell'ambiente, dell'energia e dell'agricoltura", "ministeri/03_ambiente_energia_agricoltura.md"),
    "04": ("Ministro delle infrastrutture e dei territori", "ministeri/04_infrastrutture_territori.md"),
    "05": ("Ministro dell'istruzione, della ricerca e della cultura", "ministeri/05_istruzione_ricerca_cultura.md"),
    "06": ("Ministro della salute", "ministeri/06_salute.md"),
    "07": ("Ministro della giustizia, dell'interno e della difesa", "ministeri/07_giustizia_interno_difesa.md"),
    "08": ("Ministro degli esteri, dell'Europa e delle istituzioni", "ministeri/08_esteri_europa_istituzioni.md"),
    "09": ("Ministro della PA e del digitale", "ministeri/09_pa_digitale.md"),
}
AZIONI = {"adottare", "rinviare", "sospendere", "modificare"}
DECISIONI = {"adottata", "respinta", "rinviata"}
REGOLE_ARBITRATO = {"linee rosse", "nucleo", "momento", "valori", "deroga"}
GIUDIZI = {"favorevole", "contrario", "condizionato"}
CERTEZZE = {"alta", "media", "bassa"}


# --- Lettura dello stato del sistema ----------------------------------------------------------------

def id_proposta(testo) -> str:
    """L'id di una proposta anche quando gli agenti lo scrivono con il titolo («01-P2 Spese fiscali…»)."""
    m = re.match(r"\s*(\d{2}-[PC]\d+)\b", str(testo or ""))
    return m.group(1) if m else str(testo or "")


def leggi_json(p: Path, predefinito=None):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return predefinito


def config() -> dict:
    return yaml.safe_load((RADICE / "sistema" / "config.yaml").read_text(encoding="utf-8"))


def sezione(md: str, titolo: str) -> str:
    """Il testo di una sezione '## titolo' di un file markdown."""
    m = re.search(rf"^## {re.escape(titolo)}\s*$(.*?)(?=^## |\Z)", md, flags=re.M | re.S)
    return m.group(1).strip() if m else ""


def allerte_attive(conf: dict) -> list[dict]:
    attive = set(leggi_json(RADICE / "sistema" / "stato" / "allerte.json", []))
    return [r for r in conf.get("regole", []) if r.get("id") in attive]


def linee_rosse() -> dict[str, str]:
    """Varianti e coperture escluse dalle linee rosse automatiche (le stesse dell'ottimizzatore)."""
    import ottimizza as ot
    var, menu = ot.carica_varianti(), ot.carica_menu(None)
    chiavi, *_ = ot.costruisci(var, menu, ot.capienze_base(menu))
    return {chiave: motivo for motivo, chiave, _ in ot.linee_rosse(chiavi, menu)}


def serie(ind_id: str, conf: dict) -> pd.DataFrame | None:
    import pipeline as pl
    ind = next((i for i in conf.get("indicatori", []) if i["id"] == ind_id), None)
    return pl.serie_indicatore(ind) if ind else None


def leggi_csv(p: Path, campi: list[str]) -> list[dict]:
    if not p.exists():
        return []
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def scrivi_csv(p: Path, righe: list[dict], campi: list[str]) -> None:
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campi, lineterminator="\n")
        w.writeheader()
        for r in righe:
            w.writerow({c: r.get(c, "") for c in campi})


def forma_periodo(p: str) -> str:
    p = str(p)
    if re.fullmatch(r"\d{4}-Q[1-4]", p):
        return "trimestre"
    if re.fullmatch(r"\d{4}-\d{2}", p):
        return "mese"
    if re.fullmatch(r"\d{4}", p):
        return "anno"
    return "?"


# --- 1. Preparazione della seduta ---------------------------------------------------------------------

def decisioni_vigenti(prima_di: str | None = None) -> tuple[str, dict[str, str]]:
    """Programma deciso dal Consiglio nell'ultima seduta precedente: {proposta: variante}.
    Le decisioni restano in vigore finché una seduta successiva non le cambia."""
    verbali = sorted(f for f in VERBALI.glob("*.json") if prima_di is None or f.stem < prima_di)
    if not verbali:
        return "", {}
    v = leggi_json(verbali[-1], {}) or {}
    adottate = (v.get("ragioneria") or {}).get("varianti_adottate", []) + v.get("vigenti_confermate", [])
    return verbali[-1].stem, dict(k.split(":", 1) for k in adottate if ":" in k)

def scegli_esperti(testo: str, scelti: list[str] | None = None) -> list[dict]:
    """Esperti della seduta: quelli fissi più i più pertinenti alla domanda e alle allerte (parole chiave)."""
    tutti = yaml.safe_load(ESPERTI.read_text(encoding="utf-8"))["esperti"]
    if scelti:
        ignoti = set(scelti) - {e["id"] for e in tutti}
        if ignoti:
            sys.exit(f"--esperti: esperti inesistenti {sorted(ignoti)}")
        return [e for e in tutti if e["id"] in scelti]
    t = testo.lower()
    conta = lambda e: sum(len(re.findall(rf"\b{re.escape(p.lower())}\b", t)) for p in e.get("parole", []))
    fissi = [e for e in tutti if e.get("sempre")]
    altri = sorted((e for e in tutti if not e.get("sempre") and conta(e) > 0), key=lambda e: -conta(e))
    scelta = fissi + altri[:MAX_ESPERTI - len(fissi)]
    if len(scelta) < MAX_ESPERTI and all(e["id"] != "valutazione" for e in scelta):
        scelta += [e for e in tutti if e["id"] == "valutazione"]  # chi misura l'efficacia serve sempre
    return scelta


def prepara(motivo: str, richiesta: Path | None = None, ministri: list[str] | None = None,
            esperti: list[str] | None = None) -> Path:
    oggi = date.today().isoformat()
    domanda = ""
    if richiesta:
        domanda = richiesta.read_text(encoding="utf-8").strip()
        motivo = "Richiesta: " + domanda.splitlines()[0].lstrip("# ").strip()
    base = oggi
    if richiesta:  # le domande datate (AAAA-MM-GG-...) non ripetono la data
        base = richiesta.stem if re.match(r"\d{4}-\d{2}-\d{2}", richiesta.stem) else f"{oggi}-{richiesta.stem}"
    cartella, n = SEDUTE / base, 2
    while (cartella / "verbale_composto").exists():
        cartella = SEDUTE / f"{base}-{n}"
        n += 1
    if domanda and not ministri:
        # riga "Ministri: 01, 06" del modello o campo "Ministri interessati" del modulo pubblico
        m = re.search(r"^(?:Ministri:|#+\s*Ministri[^\n]*\n+)([^\n#]*)$", domanda, flags=re.M)
        ministri = sorted(set(re.findall(r"\b0[1-9]\b", m.group(1)))) if m else None
    ministri = ministri or list(MINISTERI)
    if set(ministri) - set(MINISTERI):
        sys.exit(f"--ministri: aree inesistenti {sorted(set(ministri) - set(MINISTERI))}")
    for sotto in ("posizioni", "pareri"):
        (cartella / sotto).mkdir(parents=True, exist_ok=True)
    conf = config()

    indicatori = leggi_json(RADICE / "sistema" / "stato" / "indicatori.json", [])
    allerte = allerte_attive(conf)
    esito = pd.read_csv(RADICE / "motore" / "esito_proposte.csv")
    sel = pd.read_csv(RADICE / "programma" / "selezione_momento.csv")
    sel_md = (RADICE / "programma" / "selezione_momento.md").read_text(encoding="utf-8")
    scelte = sel[(sel.tipo == "variante") & (sel.scelta == 1)]
    nel_programma = dict(zip(scelte.proposta_id, scelte.variante))
    lr = linee_rosse()
    temi = [domanda, motivo] + [f"{a.get('messaggio', '')} {a.get('azione', '')}" for a in allerte]
    collegio = scegli_esperti(" ".join(temi), esperti)
    da_seduta, vigenti = decisioni_vigenti(cartella.name)
    mandati = [m for m in leggi_csv(MANDATI, CAMPI_MAND) if m["stato"] == "aperto"]
    cred = leggi_csv(CREDIBILITA, [])
    richieste = [p.name for p in (RADICE / "analisi" / "richieste").glob("*.md")
                 if p.name not in ("README.md", "_modello.md")]

    proposte = {}
    for r in esito.itertuples():
        area = r.proposta_id[:2]
        varianti = sel[(sel.tipo == "variante") & (sel.proposta_id == r.proposta_id)]
        proposte.setdefault(area, []).append({
            "id": r.proposta_id, "titolo": r.titolo, "classe": r.classe, "costo_medio_mld": round(r.costo_medio, 3),
            "valori_trainanti": r.valori_trainanti, "nel_programma_del_momento": nel_programma.get(r.proposta_id, "no"),
            "deciso_dal_consiglio": vigenti.get(r.proposta_id, "no") if vigenti else "nessuna seduta precedente",
            "varianti": {v.variante: round(float(v.costo_regime), 3) for v in varianti.itertuples()},
            "varianti_escluse_linee_rosse": {k.split(":")[1]: m for k, m in lr.items()
                                             if k.startswith(r.proposta_id + ":")}})
    contesto = {
        "seduta": cartella.name, "motivo": motivo, "domanda": domanda, "ministri": ministri,
        "esperti": [e["id"] for e in collegio], "indicatori": indicatori,
        "allerte": [{k: a.get(k) for k in ("id", "messaggio", "azione", "priorita", "sospendi")} for a in allerte],
        "proposte_per_area": proposte, "coperture_escluse_linee_rosse": {k: m for k, m in lr.items() if ":" not in k},
        "decisioni_vigenti": {"seduta": da_seduta, "varianti": vigenti},
        "mandati_aperti": mandati, "credibilita": cred, "suggerimenti_in_attesa": richieste,
        "indicatori_per_previsioni": {i["id"]: {"ultimo_periodo": i.get("periodo"), "forma": forma_periodo(i.get("periodo")),
                                              "ultimo_valore": i.get("valore"), "unita": i.get("unita")}
                                     for i in indicatori if i.get("periodo")},
    }
    (cartella / "contesto.json").write_text(json.dumps(contesto, ensure_ascii=False, indent=1), encoding="utf-8")

    rossi = [i for i in indicatori if i.get("delta") is not None and
             ((i["meglio"] == "giu" and i["delta"] > 0) or (i["meglio"] == "su" and i["delta"] < 0))]
    nucleo_fuori = [p for p in esito.proposta_id[esito.classe == "robusta"] if p not in nel_programma]
    prio = sorted({p for a in allerte for p in (a.get("priorita") or [])})
    prio_fuori = [p for p in prio if p not in nel_programma]
    dipendenti = esito[esito.classe == "dipendente dai valori"].proposta_id.tolist()
    righe = [f"# Ordine del giorno — seduta del {cartella.name}", "",
             f"**Motivo della convocazione:** {motivo}", ""]
    if domanda:
        righe += ["## 0. Domanda posta al Consiglio", "", "Ogni ruolo risponde prima a questa domanda, poi agli altri punti.", "",
                  *[f"> {x}" for x in domanda.splitlines()], ""]
    righe += [f"**Ministri convocati:** {', '.join(ministri)}. **Esperti:** {', '.join(e['nome'] for e in collegio)}.", "",
              "## 1. Situazione del Paese", ""]
    righe += [f"- {i['nome']}: {i['valore']:g} {i['unita']} ({i['periodo']}), variazione {i['delta']:+.2f}" for i in rossi] or ["- Nessun indicatore in peggioramento."]
    righe += ["", "Allerte attive:"] + [f"- **{a['id']}**: {a.get('messaggio', '')} Azione prevista: {a.get('azione', '')}"
                                        for a in allerte] + (["- nessuna"] if not allerte else [])
    if vigenti:
        righe += ["", "## Decisioni in vigore", "",
                  f"Restano in vigore le {len(vigenti)} misure adottate nella seduta {da_seduta} "
                  f"(`governo/verbali/{da_seduta}.md`), salvo modifiche decise in questa seduta. "
                  "In `contesto.json`, il campo `deciso_dal_consiglio` di ogni proposta indica la variante in vigore; "
                  "`nel_programma_del_momento` è invece la scelta del motore, che serve a dichiarare le deroghe."]
    righe += ["", "## 2. Programma del momento (calcolato dal motore)", "", sezione(sel_md, "Saldo"), "",
              f"- Proposte del nucleo robusto fuori dal programma: {', '.join(nucleo_fuori) or 'nessuna'}",
              f"- Priorità delle allerte non finanziate: {', '.join(prio_fuori) or 'nessuna'}",
              f"- Proposte la cui scelta dipende dai pesi dei valori (scelte politiche): {', '.join(dipendenti)}", "",
              "## 3. Fondi contesi", "", sezione(sel_md, "Uso dei fondi"), "",
              "## 4. Mandati aperti", ""]
    righe += [f"- {m['id']} ({m['area']}, scadenza {m['scadenza']}): {m['compito']}" for m in mandati] or ["- Nessuno."]
    righe += ["", "## 5. Suggerimenti dei cittadini in attesa", ""]
    righe += [f"- `analisi/richieste/{r}`" for r in richieste] or ["- Nessuno."]
    righe += ["", "## 6. Credibilità", ""]
    righe += [f"- {c['autore']}: Brier {c['brier_medio']} su {c['verificate']} previsioni verificate" for c in cred] or [
        "- Nessuna previsione ancora verificata."]
    (cartella / "ordine_del_giorno.md").write_text("\n".join(righe) + "\n", encoding="utf-8")

    rel = cartella.relative_to(RADICE).as_posix()
    base_lettura = (f"Leggi `governo/regolamento.md`, `{rel}/ordine_del_giorno.md`, `{rel}/contesto.json`, "
                    "`01_carta_valori.md`, `giuridico/quadro.md`, `apprendimento/lezioni.md`.")
    for e in collegio:
        testo = (QUI / "ruoli" / "esperto.md").read_text(encoding="utf-8")
        for k, v in {"{NOME}": e["nome"], "{ID}": e["id"], "{COMPETENZE}": e["competenze"],
                     "{FONTI}": ", ".join(e.get("fonti", [])), "{COMUNI}": base_lettura,
                     "{USCITA}": f"{rel}/pareri/{e['id']}.json"}.items():
            testo = testo.replace(k, v)
        (cartella / f"incarico_esperto_{e['id']}.md").write_text(testo, encoding="utf-8")
    comuni = base_lettura + (f" Leggi prima i pareri degli esperti in `{rel}/pareri/`: se ti discosti da un parere, "
                             "dillo e motiva.")
    if domanda:
        comuni += " Rispondi anche alla domanda posta al Consiglio, nel campo `risposta_alla_domanda` del tuo JSON."
    for area in ministri:
        titolo, dossier = MINISTERI[area]
        testo = (QUI / "ruoli" / "ministro.md").read_text(encoding="utf-8")
        testo = testo.replace("{TITOLO}", titolo).replace("{AREA}", area).replace("{DOSSIER}", dossier)
        testo = testo.replace("{COMUNI}", comuni).replace("{USCITA}", f"{rel}/posizioni/{area}.json")
        (cartella / f"incarico_ministro_{area}.md").write_text(testo, encoding="utf-8")
    for ruolo, uscita in (("opposizione", "opposizione.json"), ("capo", "capo.json")):
        testo = (QUI / "ruoli" / f"{ruolo}.md").read_text(encoding="utf-8")
        testo = testo.replace("{COMUNI}", comuni).replace("{POSIZIONI}", f"{rel}/posizioni/")
        testo = testo.replace("{OPPOSIZIONE}", f"{rel}/opposizione.json").replace("{USCITA}", f"{rel}/{uscita}")
        (cartella / f"incarico_{ruolo}.md").write_text(testo, encoding="utf-8")
    return cartella


# --- 2. Composizione: regole del regolamento e verbale ---------------------------------------------------

def valida_previsione(p: dict, ctx: dict, rilievi: list[str], dove: str) -> bool:
    ind = ctx["indicatori_per_previsioni"].get(str(p.get("indicatore")))
    try:
        prob, soglia = float(p.get("probabilita")), float(p.get("soglia"))
    except (TypeError, ValueError):
        rilievi.append(f"{dove}: previsione senza probabilità o soglia numerica, scartata")
        return False
    if ind is None:
        rilievi.append(f"{dove}: indicatore «{p.get('indicatore')}» non presente nel cruscotto, previsione scartata")
        return False
    per = str(p.get("periodo", ""))
    if p.get("condizione") not in ("<", ">") or not 0 <= prob <= 1:
        rilievi.append(f"{dove}: condizione o probabilità non valida, previsione scartata")
        return False
    if forma_periodo(per) != ind["forma"] or per <= str(ind["ultimo_periodo"]):
        rilievi.append(f"{dove}: periodo «{per}» non verificabile per {p['indicatore']} "
                       f"(serve un {ind['forma']} successivo a {ind['ultimo_periodo']}), previsione scartata")
        return False
    p["probabilita"], p["soglia"] = prob, soglia
    return True


def ottimizza(forza: list[str], escludi: list[str], priorita: list[str], riserva: float = 0.0) -> tuple[bool, str]:
    cmd = [sys.executable, "ottimizza.py", "--n", "60", "--etichetta", "consiglio", "--riserva", str(riserva)]
    cmd += (["--forza", *forza] if forza else []) + (["--escludi", *escludi] if escludi else [])
    cmd += ["--priorita", *priorita] if priorita else []
    r = subprocess.run(cmd, cwd=RADICE / "programma", capture_output=True, text=True, encoding="utf-8", errors="replace")
    righe = [x for x in (r.stdout if r.returncode == 0 else r.stderr).strip().splitlines() if not x.startswith("Highs")]
    return r.returncode == 0, (righe[-1] if righe else "")


def componi(cartella: Path) -> Path:
    ctx = leggi_json(cartella / "contesto.json")
    if ctx is None:
        sys.exit(f"{cartella}: manca contesto.json (prima --prepara)")
    capo = leggi_json(cartella / "capo.json")
    if not isinstance(capo, dict) or not isinstance(capo.get("decisioni"), list):
        sys.exit(f"{cartella}: capo.json mancante o senza 'decisioni'")
    oppo = leggi_json(cartella / "opposizione.json", {}) or {}
    posizioni = {f.stem: leggi_json(f, {}) for f in sorted((cartella / "posizioni").glob("*.json"))}
    pareri = {f.stem: leggi_json(f, {}) for f in sorted((cartella / "pareri").glob("*.json"))}
    rilievi: list[str] = []
    assenti = sorted(set(ctx.get("esperti", [])) - set(pareri))
    if assenti:
        rilievi.append(f"Esperti senza parere: {', '.join(assenti)}")
    mancanti = sorted(set(ctx.get("ministri", MINISTERI)) - set(posizioni))
    if mancanti:
        rilievi.append(f"Ministri assenti (nessuna posizione): {', '.join(mancanti)}")

    proposte = {p["id"]: p for ps in ctx["proposte_per_area"].values() for p in ps}
    lr = linee_rosse()
    previsioni: list[dict] = []

    def raccogli(autore: str, prev: dict, dove: str, condizionata: str = "") -> None:
        if isinstance(prev, dict) and valida_previsione(prev, ctx, rilievi, dove):
            previsioni.append({"autore": autore, "condizionata_a": condizionata, **{k: prev[k] for k in
                               ("indicatore", "condizione", "soglia", "periodo", "probabilita")}})

    # Ministri: richieste valide, pre-mortem, effetti sugli altri, previsioni
    for area, pos in posizioni.items():
        autore = f"ministro_{area}"
        validi = []
        for i, r in enumerate(pos.get("richieste", []) or []):
            dove = f"{autore}, richiesta {i + 1}"
            r["proposta"] = id_proposta(r.get("proposta"))
            if r["proposta"] not in proposte or r.get("azione") not in AZIONI:
                rilievi.append(f"{dove}: proposta o azione non valida, scartata")
                continue
            if not str(r.get("pre_mortem", "")).strip():
                rilievi.append(f"{dove} ({r['proposta']}): manca il pre-mortem (regola 4), scartata")
                continue
            validi.append(r)
            raccogli(autore, r.get("scommessa"), dove, r["proposta"] if r["azione"] == "adottare" else "")
        pos["richieste"] = validi
        if not pos.get("previsioni_contesto"):
            rilievi.append(f"{autore}: nessuna previsione sul contesto (regola 2)")
        for j, p in enumerate(pos.get("previsioni_contesto", []) or []):
            raccogli(autore, p, f"{autore}, previsione {j + 1}")
    # Esperti: pareri con fonti e grado di certezza, giudizi sulle proposte
    contrari: dict[str, list[str]] = {}
    for eid, par in pareri.items():
        autore = f"esperto_{eid}"
        validi = []
        for i, q in enumerate(par.get("pareri", []) or []):
            if not q.get("evidenze") or q.get("certezza") not in CERTEZZE or not str(q.get("cosa_non_sappiamo", "")).strip():
                rilievi.append(f"{autore}, parere {i + 1}: senza evidenze, grado di certezza o limiti dichiarati, scartato")
                continue
            validi.append(q)
        par["pareri"] = validi
        giudizi = []
        for g in par.get("proposte", []) or []:
            g["proposta"] = id_proposta(g.get("proposta"))
            if g["proposta"] in proposte and g.get("giudizio") in GIUDIZI:
                giudizi.append(g)
                if g["giudizio"] == "contrario":
                    contrari.setdefault(g["proposta"], []).append(eid)
            else:
                rilievi.append(f"{autore}: giudizio su proposta inesistente o non valido, scartato ({g.get('proposta')})")
        par["proposte"] = giudizi
        for j, p in enumerate(par.get("previsioni_contesto", []) or []):
            raccogli(autore, p, f"{autore}, previsione {j + 1}")
    for j, p in enumerate(oppo.get("previsioni_contesto", []) or []):
        raccogli("opposizione", p, f"opposizione, previsione {j + 1}")
    for j, p in enumerate(capo.get("previsioni_contesto", []) or []):
        raccogli("capo", p, f"capo, previsione {j + 1}")

    # Capo: decisioni nel rispetto del regolamento
    obiettate = {id_proposta(o.get("proposta")) for o in oppo.get("obiezioni", []) or []}
    decisioni = []
    for i, d in enumerate(capo["decisioni"]):
        dove = f"capo, decisione {i + 1}"
        pid, var = id_proposta(d.get("proposta")), str(d.get("variante") or "").upper()
        d["proposta"] = pid
        if pid not in proposte or d.get("decisione") not in DECISIONI:
            rilievi.append(f"{dove}: proposta o decisione non valida, scartata")
            continue
        d["variante"], d["esito_controlli"] = var, []
        if d["decisione"] == "adottata":
            if var not in proposte[pid]["varianti"]:
                rilievi.append(f"{dove} ({pid}): variante «{var}» inesistente, scartata")
                continue
            if f"{pid}:{var}" in lr:
                d["decisione"] = "respinta d'ufficio"
                d["esito_controlli"].append(f"linea rossa: {lr[f'{pid}:{var}']} (regola 8)")
            if pid in obiettate and not str(d.get("risposta_opposizione", "")).strip():
                rilievi.append(f"{dove} ({pid}): nessuna risposta all'obiezione dell'opposizione (regola 7)")
            if pid in contrari and not str(d.get("risposta_esperti", "")).strip():
                rilievi.append(f"{dove} ({pid}): adottata contro il parere di {', '.join(contrari[pid])} "
                               "senza risposta scritta (regola 11)")
        motore = proposte[pid]["nel_programma_del_momento"]
        # ZERO = status quo: per il motore la proposta è già fuori dal programma
        diverge = (d["decisione"] == "adottata" and motore != var) or (d["decisione"] == "respinta" and motore not in ("no", "ZERO"))
        if diverge and not d.get("deroga"):
            d["deroga"] = True
            d["esito_controlli"].append(f"deroga non dichiarata: il motore indicava {motore} (regola 6)")
            rilievi.append(f"{dove} ({pid}): deroga non dichiarata dal capo, registrata d'ufficio (regola 6)")
        if d.get("deroga") and not str(d.get("motivo_deroga", "")).strip():
            rilievi.append(f"{dove} ({pid}): deroga senza motivazione (regola 6)")
        raccogli("capo", d.get("scommessa"), dove, pid if d["decisione"] == "adottata" else "")
        decisioni.append(d)

    # Ragioneria: le decisioni devono stare insieme senza deficit (in ordine di priorità del capo)
    prio = sorted({p for a in ctx["allerte"] for p in (a.get("priorita") or [])})
    escludi = sorted({d["proposta"] for d in decisioni if d["decisione"] == "respinta"}
                     | {p for a in ctx["allerte"] for p in (a.get("sospendi") or [])})
    adottate = [d for d in decisioni if d["decisione"] == "adottata"]
    # quota delle coperture che il capo destina alla riduzione del deficit (mld/anno): viene prima delle misure
    try:
        riserva = max(float(capo.get("riserva_deficit_mld") or 0), 0.0)
    except (TypeError, ValueError):
        riserva = 0.0
        rilievi.append("capo: riserva_deficit_mld non numerica, considerata 0")
    if riserva and not ottimizza([], escludi, prio, riserva)[0]:
        rilievi.append(f"capo: riserva di {riserva} mld non raggiungibile nemmeno senza misure obbligatorie; ridotta a 0")
        riserva = 0.0
    forza: list[str] = []
    for d in adottate:
        ok, msg = ottimizza(forza + [f"{d['proposta']}:{d['variante']}"], escludi, prio, riserva)
        if ok:
            forza.append(f"{d['proposta']}:{d['variante']}")
        else:
            d["decisione"] = "sospesa: non finanziabile"
            d["esito_controlli"].append("con le decisioni precedenti non c'è copertura senza deficit (regola 8)")
    # Le decisioni delle sedute precedenti restano in vigore se questa seduta non le ha toccate.
    # Vengono dopo le decisioni di oggi: se la copertura non basta, la Ragioneria le sospende e lo scrive.
    da_seduta, vigenti = decisioni_vigenti(cartella.name)
    toccate = {d["proposta"] for d in decisioni}
    confermate, sospese_vigenti = [], []
    for pid, var in vigenti.items():
        if pid in toccate or pid in escludi:
            continue
        k = f"{pid}:{var}"
        if ottimizza(forza + confermate + [k], escludi, prio, riserva)[0]:
            confermate.append(k)
        else:
            sospese_vigenti.append(k)
    if sospese_vigenti:
        rilievi.append(f"Decisioni della seduta {da_seduta} sospese per mancanza di copertura: {', '.join(sospese_vigenti)}")
    ok, ragioneria = ottimizza(forza + confermate, escludi, prio, riserva)

    # Registri: previsioni e mandati
    seduta = cartella.name
    # ricomporre la stessa seduta sostituisce le sue registrazioni, non le duplica
    reg = [r for r in leggi_csv(PREVISIONI, CAMPI_PREV) if r["seduta"] != seduta]
    base = max((int(r["id"][1:]) for r in reg), default=0)
    for k, p in enumerate(previsioni, 1):
        reg.append({"id": f"P{base + k:04d}", "seduta": seduta, **p})
    scrivi_csv(PREVISIONI, reg, CAMPI_PREV)
    mand = [m for m in leggi_csv(MANDATI, CAMPI_MAND) if m["seduta"] != seduta]
    base_m = max((int(m["id"][1:]) for m in mand), default=0)
    chiusi = set(capo.get("mandati_chiusi", []) or [])
    for m in mand:
        if m["id"] in chiusi and m["stato"] == "aperto":
            m["stato"], m["chiuso_il"] = "chiuso", seduta
    nuovi = []
    for m in capo.get("mandati", []) or []:
        if str(m.get("area")) in MINISTERI and str(m.get("compito", "")).strip() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(m.get("scadenza", ""))):
            nuovi.append({"id": f"M{base_m + len(nuovi) + 1:03d}", "seduta": seduta, "area": m["area"],
                          "compito": m["compito"], "scadenza": m["scadenza"], "stato": "aperto"})
        else:
            rilievi.append(f"capo: mandato senza area, compito o scadenza valida, scartato ({m})")
    scrivi_csv(MANDATI, mand + nuovi, CAMPI_MAND)

    # Verbale
    VERBALI.mkdir(exist_ok=True)
    if ctx.get("domanda") and not str(capo.get("risposta_alla_domanda", "")).strip():
        rilievi.append("capo: nessuna risposta alla domanda posta al Consiglio")
    verbale = {"seduta": seduta, "motivo": ctx["motivo"], "domanda": ctx.get("domanda", ""),
               "risposta": capo.get("risposta_alla_domanda", ""), "indirizzo": capo.get("indirizzo", ""),
               "decisioni": decisioni, "posizioni": posizioni, "pareri": pareri, "opposizione": oppo, "mandati": nuovi,
               "mandati_chiusi": sorted(chiusi), "previsioni": len(previsioni), "rilievi": rilievi,
               "vigenti_da": da_seduta, "vigenti_confermate": confermate, "vigenti_sospese": sospese_vigenti,
               "ragioneria": {"finanziabile": ok, "esito": ragioneria, "varianti_adottate": forza, "riserva_deficit_mld": riserva}}
    (VERBALI / f"{seduta}.json").write_text(json.dumps(verbale, ensure_ascii=False, indent=1), encoding="utf-8")
    (VERBALI / f"{seduta}.md").write_text(verbale_md(verbale, proposte), encoding="utf-8")
    (cartella / "verbale_composto").write_text(seduta, encoding="utf-8")
    return VERBALI / f"{seduta}.md"


def nomi_esperti() -> dict[str, str]:
    try:
        return {e["id"]: e["nome"] for e in yaml.safe_load(ESPERTI.read_text(encoding="utf-8"))["esperti"]}
    except (OSError, KeyError, TypeError):
        return {}


NOMI_ESPERTI = nomi_esperti()


def verbale_md(v: dict, proposte: dict) -> str:
    tit = lambda p: proposte.get(p, {}).get("titolo", p)
    r = [f"# Verbale del Consiglio dei ministri — {v['seduta']}", "",
         "*Governo ombra di GovernAI: le decisioni non sono in vigore. Regole in `governo/regolamento.md`; "
         "atti della seduta in `governo/sedute/" + v["seduta"] + "/`.*", "",
         f"**Motivo della convocazione.** {v['motivo']}", ""]
    if v.get("domanda"):
        r += ["## Domanda posta al Consiglio", "", *[f"> {x}" for x in v["domanda"].splitlines()], "",
              "## Risposta del Consiglio", "", v.get("risposta") or "—", ""]
    r += ["## Indirizzo del capo di governo", "", v["indirizzo"] or "—", "",
         "## Decisioni", "", "| Proposta | Variante | Decisione | Regola | Motivazione |", "|---|---|---|---|---|"]
    for d in v["decisioni"]:
        regola = d.get("regola", "") + (" · **deroga**" if d.get("deroga") else "")
        mot = str(d.get("motivazione", "")).replace("|", "/").replace("\n", " ")
        if d.get("esito_controlli"):
            mot += " — *Controlli: " + "; ".join(d["esito_controlli"]) + "*"
        r.append(f"| {d['proposta']} {tit(d['proposta'])} | {d['variante'] or '—'} | {d['decisione']} | {regola} | {mot} |")
    rag = v["ragioneria"]
    r += ["", f"**Ragioneria.** {'Finanziabile senza deficit' if rag['finanziabile'] else 'NON finanziabile'}: {rag['esito']}"]
    if rag.get("riserva_deficit_mld"):
        r.append(f"Riservati alla riduzione del deficit: **{rag['riserva_deficit_mld']:g} mld l'anno** a regime, prima di ogni nuova spesa.")
    r.append("")
    if v.get("vigenti_da"):
        r += [f"**Decisioni precedenti.** Restano in vigore {len(v.get('vigenti_confermate', []))} misure della seduta "
              f"{v['vigenti_da']} non modificate oggi."
              + (f" Sospese per mancanza di copertura: {', '.join(v['vigenti_sospese'])}." if v.get("vigenti_sospese") else ""), ""]
    deroghe = [d for d in v["decisioni"] if d.get("deroga")]
    if deroghe:
        r += ["## Deroghe dall'esito del motore", ""] + [f"- **{d['proposta']}**: {d.get('motivo_deroga') or 'motivazione mancante'}" for d in deroghe] + [""]
    if v.get("pareri"):
        r += ["## Pareri degli esperti", ""]
        risposte_e = {d["proposta"]: d.get("risposta_esperti", "") for d in v["decisioni"]}
        for eid, par in v["pareri"].items():
            r += [f"### {NOMI_ESPERTI.get(eid, eid)}", "", str(par.get("sintesi", "")), ""]
            for q in par.get("pareri", []):
                fonti = "; ".join(f"{e.get('fonte', '')}: {e.get('dato', '')}" for e in q.get("evidenze", []))
                r += [f"- **{q.get('tema', '')}** (certezza {q.get('certezza')}): {q.get('parere', '')}",
                      f"  - Evidenze: {fonti}", f"  - Cosa non sappiamo: {q.get('cosa_non_sappiamo', '')}"]
            for g in par.get("proposte", []):
                cond = f" Condizione: {g['condizione']}" if g.get("condizione") else ""
                risp = f" — *Risposta del capo: {risposte_e[g['proposta']]}*" if g["giudizio"] == "contrario" and risposte_e.get(g["proposta"]) else ""
                r.append(f"- {g['proposta']}: **{g['giudizio']}**. {g.get('motivo', '')}{cond}{risp}")
            r.append("")
    r += ["## Obiezioni dell'opposizione e risposte", ""]
    risposte = {d["proposta"]: d.get("risposta_opposizione", "") for d in v["decisioni"]}
    for o in v["opposizione"].get("obiezioni", []) or []:
        r += [f"- **{o.get('proposta')}** — {o.get('punto_debole', '')}",
              f"  - Prova: {o.get('prova', '')}",
              f"  - Cosa le farebbe cambiare idea: {o.get('cosa_cambierebbe_idea', '')}",
              f"  - Risposta del capo: {risposte.get(o.get('proposta')) or '—'}"]
    if v["opposizione"].get("alternative"):
        r += ["", f"**Alternative dell'opposizione.** {v['opposizione']['alternative']}"]
    r += ["", "## Posizioni dei ministri", ""]
    for area, pos in v["posizioni"].items():
        r += [f"### {MINISTERI.get(area, (area,))[0]}", "", str(pos.get("situazione", "")), ""]
        if pos.get("risposta_alla_domanda"):
            r += [f"*Risposta alla domanda:* {pos['risposta_alla_domanda']}", ""]
        for q in pos.get("richieste", []):
            eff = "; ".join(f"{e.get('area')} {e.get('segno')} {e.get('effetto')}" for e in q.get("effetti_altri", []) or []) or "nessuno dichiarato"
            r += [f"- **{q['azione']} {q['proposta']}** {q.get('variante', '')}: {q.get('motivazione', '')}",
                  f"  - Pre-mortem: {q.get('pre_mortem', '')}", f"  - Effetti su altri ministeri: {eff}"]
        if pos.get("rinunce"):
            r.append(f"- Disposto a rinunciare a: {'; '.join(map(str, pos['rinunce']))}")
        r.append("")
    r += ["## Mandati", ""] + [f"- {m['id']} — {MINISTERI[m['area']][0]}, entro il {m['scadenza']}: {m['compito']}" for m in v["mandati"]]
    if v["mandati_chiusi"]:
        r.append(f"- Chiusi: {', '.join(v['mandati_chiusi'])}")
    r += ["", f"**Previsioni registrate:** {v['previsioni']} (verificate alla scadenza con i dati ufficiali; vedi `governo/credibilita.csv`).", ""]
    if v["rilievi"]:
        r += ["## Rilievi formali", ""] + [f"- {x}" for x in v["rilievi"]] + [""]
    return "\n".join(r)


# --- 3. Valutazione delle previsioni e credibilità ---------------------------------------------------------

def valuta() -> str:
    conf = config()
    reg = leggi_csv(PREVISIONI, CAMPI_PREV)
    reali = set()
    dec = RADICE / "apprendimento" / "decisioni.csv"
    if dec.exists():
        d = pd.read_csv(dec)
        reali = set(d.proposta[d.decisione.str.lower() == "adottata"])
    cache, nuove = {}, 0
    for p in reg:
        if p.get("esito") not in ("", None):
            continue
        # le previsioni condizionate a una misura contano solo se la misura è davvero in vigore
        if p.get("condizionata_a") and p["condizionata_a"] not in reali:
            continue
        if p["indicatore"] not in cache:
            cache[p["indicatore"]] = serie(p["indicatore"], conf)
        s = cache[p["indicatore"]]
        if s is None:
            continue
        riga = s[s.time.astype(str) == p["periodo"]]
        if riga.empty:
            continue
        val = float(riga.valore.iloc[-1])
        o = int(val < float(p["soglia"]) if p["condizione"] == "<" else val > float(p["soglia"]))
        p["esito"], p["valore"], p["brier"] = o, round(val, 4), round((float(p["probabilita"]) - o) ** 2, 4)
        nuove += 1
    if reg:
        scrivi_csv(PREVISIONI, reg, CAMPI_PREV)
    tab = {}
    for p in reg:
        t = tab.setdefault(p["autore"], {"autore": p["autore"], "verificate": 0, "in_attesa": 0, "somma": 0.0})
        if p.get("brier") not in ("", None):
            t["verificate"] += 1
            t["somma"] += float(p["brier"])
        else:
            t["in_attesa"] += 1
    righe = [{"autore": t["autore"], "verificate": t["verificate"], "in_attesa": t["in_attesa"],
              "brier_medio": round(t["somma"] / t["verificate"], 3) if t["verificate"] else ""}
             for t in sorted(tab.values(), key=lambda x: x["autore"])]
    scrivi_csv(CREDIBILITA, righe, ["autore", "verificate", "in_attesa", "brier_medio"])
    return f"consiglio: {len(reg)} previsioni, {nuove} verificate oggi, {sum(r['verificate'] for r in righe)} verificate in totale"


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--prepara", action="store_true", help="convoca una seduta: ordine del giorno e incarichi")
    g.add_argument("--componi", metavar="CARTELLA", help="applica il regolamento e scrive il verbale")
    g.add_argument("--valuta", action="store_true", help="verifica le previsioni scadute e aggiorna la credibilità")
    ap.add_argument("--motivo", default="Seduta ordinaria", help="motivo della convocazione")
    ap.add_argument("--richiesta", help="con --prepara: file con la domanda posta al Consiglio (prima riga = titolo)")
    ap.add_argument("--ministri", help="con --prepara: aree convocate, es. 01,06 (predefinito: tutte)")
    ap.add_argument("--esperti", help="con --prepara: esperti scelti a mano, es. fiscalista,giurista (vedi esperti.yaml)")
    a = ap.parse_args()
    if a.prepara:
        lista = lambda x: [v.strip() for v in x.split(",") if v.strip()] if x else None
        c = prepara(a.motivo, Path(a.richiesta).resolve() if a.richiesta else None, lista(a.ministri), lista(a.esperti))
        ctx = leggi_json(c / "contesto.json")
        print(f"seduta preparata: {c.relative_to(RADICE).as_posix()} (esperti: {', '.join(ctx['esperti'])}; "
              f"ministri: {', '.join(ctx['ministri'])}; opposizione; capo)")
    elif a.componi:
        print(f"verbale: {componi(Path(a.componi).resolve()).relative_to(RADICE).as_posix()}")
    else:
        print(valuta())
    return 0


if __name__ == "__main__":
    sys.exit(main())
