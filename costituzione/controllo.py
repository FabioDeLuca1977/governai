"""Screening costituzionale deterministico di un testo normativo (legge, emendamento, decreto, manovra di bilancio).

E' uno SCREENING: cerca segnali testuali di rischio per i parametri di parametri.yaml e li ordina per livello
(alto / medio / basso). Non decide la legittimita': l'esame approfondito segue istruzioni_costituzionalista.md.

Uso:
    python controllo.py testo.md                                  # rapporto in esami/<nome>.md (+ .json)
    python controllo.py ddl.pdf --nome AC3174 --data 2027-01-01   # PDF (pypdf); data di riferimento per la retroattivita'
    python controllo.py testi/AC3174_articolato.txt --articoli 1-137 --nome AC3174_screening
    python controllo.py --gu                                      # atti con forza di legge nuovi in legislazione/archivio
    python controllo.py --gu --dal 2026-11-01 --max 20

Riusa legislazione/verifica_testo.py (divisione in commi, controlli di copertura e di attuazione) e legislazione/norme.py.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import yaml

QUI = Path(__file__).resolve().parent
RADICE = QUI.parent
sys.path.insert(0, str(RADICE / "legislazione"))
from norme import MESI, trova_atti_ue  # noqa: E402
from verifica_testo import Verifica, dividi_commi, pulisci_md  # noqa: E402

ESAMI = QUI / "esami"
ESAMI_GU = ESAMI / "gu"
STATO_GU = ESAMI_GU / "stato.json"
PESO = {"alto": 3, "medio": 2, "basso": 1}
NOME_LIV = {3: "alto", 2: "medio", 1: "basso"}
ICONA = {"alto": "ALTO", "medio": "MEDIO", "basso": "basso"}

# segnali che servono solo alle regole combinate: da soli non producono un rilievo
SOLO_CONTESTO = {"materia_regionale", "atto_statale_attuativo", "intesa", "onere_quantificato", "lep", "autonomie_speciali",
                 "delega_criteri", "notifica_commissione", "aiuto_stato", "salvezza_effetti", "anni_passati_obblighi",
                 "legge_bilancio_tributaria", "invarianza", "atto_ue", "assunzioni", "limiti_spesa_sanita", "acconti_ricalcolo",
                 "dl_preambolo", "aliquota_aumentata", "settore_specifico", "ateco_settore", "decadenza_preclusione"}

# pronunce da citare per prime, per segnale (le altre restano in parametri.yaml)
PREFERITE = {
    "divieto_traslazione": ["10/2015", "111/2024"], "ateco_settore": ["10/2015", "111/2024"],
    "prelievo_settoriale": ["10/2015", "111/2024", "180/2025"], "regime_settoriale": ["10/2015", "262/2020"], "contributo_solidarieta": ["111/2024", "234/2020", "116/2013"],
    "payback": ["140/2024"], "parere_conferenza": ["182/2026", "251/2016", "223/2023"],
    "statale_senza_intesa": ["222/2005", "370/2003", "195/2024"], "riparto_senza_intesa": ["222/2005", "370/2003", "182/2026"],
    "risorse_bilanci_enti": ["182/2026", "137/2018", "192/2024"], "fondo_regionale_ridotto": ["137/2018", "222/2005", "370/2003"],
    "fondo_soppresso_ridotto": ["137/2018", "195/2024"], "contributo_finanza_pubblica": ["195/2024", "152/2025"],
    "rivalutazione_ridotta": ["70/2015", "234/2020", "19/2025"], "organico_ridotto": ["80/2010", "275/2016", "223/2023"],
    "interpretazione_autentica": ["525/2000", "311/2009", "78/2012"], "si_applica_anche_passato": ["236/2009", "108/2016", "170/2013"],
    "decorrenza_passata": ["236/2009", "16/2017", "264/2005"], "periodo_imposta_in_corso": ["10/2015", "16/2017"],
    "obblighi_anni_passati": ["140/2024", "108/2016", "16/2017"],
    "indebitamento_clausola_ue": ["88/2014", "184/2016", "18/2019"], "modifica_243": ["88/2014"],
    "delega": ["192/2024", "340/2007", "251/2016"], "delega_senza_criteri": ["192/2024", "340/2007"],
    "delega_in_bilancio": ["17/2019"], "norma_ordinamentale_bilancio": ["17/2019"],
    "vantaggio_selettivo": ["269/2017", "170/1984"], "giudizi_in_corso": ["170/2013", "78/2012", "311/2009"],
    "deroga_concorso": ["293/2009", "37/2015"], "cessazione_incarichi": ["103/2007", "104/2007"],
    "poteri_sostitutivi": ["192/2024"], "indebitamento_enti": ["425/2004"], "risorse_disponibili": ["275/2016", "80/2010"],
    "requisiti_residenza": ["31/2025"], "dl_eterogeneo": ["22/2012", "32/2014", "247/2019"],
}


@dataclass
class Segnale:
    parametro: str
    id: str
    livello: str
    comma: str
    estratto: str
    nota: str


@dataclass
class Art:
    numero: str
    rubrica: str
    testo: str
    commi: list = field(default_factory=list)
    segnali: list = field(default_factory=list)

    @property
    def livello(self) -> int:
        return max((PESO[s.livello] for s in self.segnali), default=0)


# --- lettura -------------------------------------------------------------------------------------------------------

def leggi(percorso: Path) -> str:
    if percorso.suffix.lower() == ".pdf":
        from pypdf import PdfReader
        return "\n".join((p.extract_text() or "") for p in PdfReader(str(percorso)).pages)
    return percorso.read_text(encoding="utf-8", errors="replace")


RE_INTEST = re.compile(r"(?m)^\s*(?:Art\.|Articolo)\s+(?P<n>\d+(?:-?(?:bis|ter|quater|quinquies|sexies|septies|octies))?)\s*\.?\s*"
                       r"(?:[-–—]\s*)?(?:\n\s*)?(?:\((?P<rub>[^()]*(?:\([^()]*\)[^()]*)*)\))?")


def articoli(testo: str) -> list[Art]:
    """Divide in articoli: intestazioni a inizio riga ('Art. 21.' con rubrica tra parentesi, anche su piu' righe).
    Le intestazioni dentro le novelle (precedute da «) non sono a inizio riga e quindi non spezzano l'articolo."""
    t = re.sub(r"(?m)^[ 	 ]+", "", pulisci_md(testo))  # rientri iniziali: altrimenti i commi non si riconoscono
    ms = [m for m in RE_INTEST.finditer(t)]
    out = []
    for i, m in enumerate(ms):
        fine = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        corpo = t[m.end(): fine].strip()
        rub = re.sub(r"\s+", " ", m["rub"] or "").strip()
        out.append(Art(m["n"], rub, corpo, dividi_commi(corpo)))
    if not out:
        out = [Art("unico", "", t, dividi_commi(t))]
    # numeri ripetuti (es. un secondo testo allegato): si tiene la prima occorrenza con numerazione crescente
    visti, puliti = set(), []
    for a in out:
        if a.numero in visti:
            continue
        visti.add(a.numero)
        puliti.append(a)
    return puliti


# --- regole --------------------------------------------------------------------------------------------------------

def _estratto(testo: str, m: re.Match, prima: int = 70, dopo: int = 150) -> str:
    s = testo[max(0, m.start() - prima): m.end() + dopo]
    s = re.sub(r"\s+", " ", s).strip()
    return ("…" if m.start() > prima else "") + s + ("…" if m.end() + dopo < len(testo) else "")


RE_DATA = re.compile(r"(?i)(?:a decorrere dal|con decorrenza dal|con effetto dal|a partire dal|dal)\s+(\d{1,2})(?:°|º)?\s+(" + "|".join(MESI) + r")\s+(\d{4})")
RE_OBBLIGO = re.compile(r"(?i)\b(?:erogano|versano|sono tenut|è tenut|ripian|restituisc|recuper|dovut[aoie]|tetti di spesa regionali|si applica|quota di propria competenza)")
RE_OBBLIGO_FORTE = re.compile(r"(?i)(?:erogano|versano|ripian|restituisc|recuper[ao]|sono tenut)")
RE_ANNI = re.compile(r"(?i)(?:per gli anni dal|per ciascuno degli anni dal|relativ[ao] agli anni dal|anni dal)\s+((?:19|20)\d\d)\s+al\s+((?:19|20)\d\d)|(?:all'anno|per l'anno|relativ[ao] all'anno)\s+((?:19|20)\d\d)")
RE_IN_CORSO = re.compile(r"(?i)(?<!successivo a quello )(?<!successivi a quello )in corso al 31 dicembre (\d{4})")
RE_TRIBUT = re.compile(r"(?i)\b(?:impost|aliquot|addizional|tribut|contribut|IRAP|IRES|IRPEF|IVA|accis|deduzion|detrazion)")
RE_RIPARTO = re.compile(r"(?i)\b(?:ripart|riparto|ripartizione|assegna(?:te|zione) (?:alle|delle) (?:regioni|risorse))")


def segnali_yaml(par: dict, a: Art) -> list[Segnale]:
    out = []
    for comma_n, comma_t in a.commi or [("", a.testo)]:
        for pid, p in par.items():
            for s in p.get("segnali", []):
                m = re.search(s["regex"], comma_t)
                if m:
                    out.append(Segnale(pid, s["id"], s["livello"], comma_n, _estratto(comma_t, m), s.get("nota", "")))
    return out


def regole_combinate(a: Art, base: list[Segnale], rif: date, bilancio: bool) -> list[Segnale]:
    out: list[Segnale] = []
    per_comma: dict[str, set] = {}
    for s in base:
        per_comma.setdefault(s.comma, set()).add(s.id)
    ids_art = {s.id for s in base}
    testi = dict(a.commi) if a.commi else {"": a.testo}

    for c, t in testi.items():
        ids = per_comma.get(c, set())
        # tributi: prelievo settoriale
        if ({"ateco_settore", "settore_specifico"} & ids_art) and ({"aliquota_aumentata", "contributo_solidarieta"} & ids):
            m = re.search(r"(?i)aumentat|incrementat|maggiorazion|addizional|contributo", t)
            out.append(Segnale("tributi", "prelievo_settoriale", "alto", c, _estratto(t, m) if m else "",
                               "aumento del prelievo su un solo settore: serve un nesso coerente tra base imponibile, durata e finalita' (Robin tax)"))
        if ({"ateco_settore", "settore_specifico"} & ids_art) and ({"indeducibilita"} & ids or re.search(r"(?i)deduzion|deducibil", t)):
            m = re.search(r"(?i)deduzion|deducibil", t)
            out.append(Segnale("tributi", "regime_settoriale", "medio", c, _estratto(t, m) if m else "",
                               "regime di deducibilita' o di base imponibile differenziato per settore: giustificazione e coerenza (art. 3, 53)"))
        # regioni: atto statale in materia regionale
        if "materia_regionale" in ids and "atto_statale_attuativo" in ids and "intesa" not in ids:
            riparto = RE_RIPARTO.search(t)
            liv = "alto" if riparto else "medio"
            sid = "riparto_senza_intesa" if riparto else "statale_senza_intesa"
            m = re.search(r"(?i)decret[oi] del (?:Ministro|Presidente)|decreto interministeriale", t)
            out.append(Segnale("regioni", sid, liv, c, _estratto(t, m) if m else "",
                               "atto statale in materia regionale senza intesa" + (" per il riparto di risorse" if riparto else "")))
        if "fondo_soppresso_ridotto" in ids and "materia_regionale" in ids:
            m = re.search(r"(?i)soppress|ridott|riduzione", t)
            out.append(Segnale("regioni", "fondo_regionale_ridotto", "alto", c, _estratto(t, m) if m else "",
                               "fondo o risorse in materia regionale soppressi o ridotti: corrispondenza funzioni-risorse"))
        # deleghe
        if "delega" in ids:
            if "delega_criteri" not in ids_art:
                out.append(Segnale("procedimento_deleghe", "delega_senza_criteri", "alto", c, "",
                                   "delega senza principi e criteri direttivi espressi nell'articolo"))
            if bilancio:
                out.append(Segnale("procedimento_deleghe", "delega_in_bilancio", "alto", c, "",
                                   "delega in legge di bilancio: contenuto estraneo (art. 21, comma 1-quinquies, L. 196/2009)"))
        # UE: vantaggio selettivo senza base o clausola di autorizzazione
        if "vantaggio_selettivo" in ids and not ({"aiuto_stato", "notifica_commissione"} & ids_art):
            for s in base:
                if s.id == "vantaggio_selettivo" and s.comma == c:
                    s.nota += "; nessun richiamo a GBER, de minimis o autorizzazione della Commissione nell'articolo"
        # retroattivita': decorrenze passate
        for m in RE_DATA.finditer(t):
            try:
                d = date(int(m[3]), MESI.index(m[2].lower()) + 1, int(m[1]))
            except ValueError:
                continue
            if d < rif:
                liv = "alto" if RE_TRIBUT.search(t) else "medio"
                out.append(Segnale("affidamento_retroattivita", "decorrenza_passata", liv, c, _estratto(t, m),
                                   f"decorrenza {d.isoformat()} anteriore alla data di riferimento {rif.isoformat()}"))
        # periodo d'imposta in corso (Statuto del contribuente, art. 3)
        for m in RE_IN_CORSO.finditer(t):
            anno = int(m[1])
            if anno >= rif.year - 1 and re.search(r"(?i)periodo d'imposta", t[max(0, m.start() - 80): m.start()]):
                liv = "alto" if anno < rif.year else "medio"
                out.append(Segnale("affidamento_retroattivita", "periodo_imposta_in_corso", liv, c, _estratto(t, m),
                                   "la modifica tributaria incide sul periodo d'imposta in corso o gia' chiuso (art. 3 L. 212/2000)"))
        # obblighi riferiti ad annualita' passate
        for m in RE_ANNI.finditer(t):
            anni = [int(x) for x in m.groups() if x]
            vicino = t[max(0, m.start() - 300): m.end() + 300] if m[1] else t[max(0, m.start() - 150): m.end() + 150]
            obbligo = RE_OBBLIGO.search(vicino) if m[1] else RE_OBBLIGO_FORTE.search(vicino)
            if anni and min(anni) < rif.year - 1 and obbligo:
                out.append(Segnale("affidamento_retroattivita", "obblighi_anni_passati", "alto", c, _estratto(t, m),
                                   f"obblighi o tetti riferiti ad annualita' passate ({min(anni)}-{max(anni)})"))
                break
    # legge di bilancio: norme ordinamentali senza effetti finanziari
    if bilancio and "norma_ordinamentale_bilancio" in ids_art and not re.search(r"(?i)euro|oneri|spesa", a.testo):
        out.append(Segnale("procedimento_deleghe", "norma_ordinamentale_bilancio", "medio", "", "",
                           "norma organizzatoria senza effetti finanziari in legge di bilancio: possibile stralcio"))
    return out


def tara(base: list[Segnale], combinati: list[Segnale]) -> list[Segnale]:
    """Toglie i segnali di solo contesto e i duplicati (stesso parametro, segnale e comma)."""
    tutti = [s for s in base if s.id not in SOLO_CONTESTO] + combinati
    visti, out = set(), []
    for s in sorted(tutti, key=lambda s: -PESO[s.livello]):
        k = (s.parametro, s.id, s.comma)
        if k in visti:
            continue
        visti.add(k)
        out.append(s)
    return out


# --- controlli sull'intero testo -------------------------------------------------------------------------------------

def controlli_globali(testo: str, arts: list[Art], bilancio: bool, dl: bool) -> list[str]:
    note = []
    if bilancio:
        note.append("**Legge di bilancio.** Le norme tributarie e di bilancio sono escluse dal referendum abrogativo (art. 75, "
                    "secondo comma). La prima sezione non deve contenere deleghe, norme ordinamentali od organizzatorie ne' "
                    "interventi localistici o microsettoriali (art. 21, comma 1-quinquies, L. 196/2009): verificare gli articoli "
                    "segnalati come `norma_ordinamentale_bilancio` e `delega_in_bilancio`. La copertura complessiva si valuta "
                    "sui saldi (allegato 1, prospetto di copertura) e non articolo per articolo.")
    if dl:
        rub = [a.rubrica for a in arts if a.rubrica]
        note.append(f"**Decreto-legge** con {len(arts)} articoli. Verificare la ratio unitaria (oggetto o finalita') e la "
                    "motivazione della necessita' e urgenza: con molte rubriche eterogenee il rischio di disomogeneita' cresce "
                    "(sent. 22/2012, 32/2014, 247/2019). Rubriche: " + "; ".join(rub[:25]) + ("…" if len(rub) > 25 else ""))
    ue = trova_atti_ue(testo)
    if ue:
        ids = sorted({f"{x['tipo']} ({x['org']}) {x['id']}" for x in ue})
        note.append(f"**Atti UE richiamati** ({len(ids)}): " + "; ".join(ids[:20]) + ". Verificare la conformita' "
                    "(art. 117, primo comma) e, per i vantaggi a imprese, la base nel diritto degli aiuti di Stato.")
    if not bilancio:
        try:
            v = Verifica(testo, rete=False)
            v.finanza()
            v.termini_e_attuazione()
            fin = [r for r in v.r if r.categoria in ("finanza", "termini") or "deleg" in r.problema.lower()]
            for r in fin[:12]:
                note.append(f"**Copertura e attuazione** ({r.livello}, {r.dove}): {r.problema} "
                            f"_(da legislazione/verifica_testo.py)_")
        except Exception as e:  # il controllo redazionale e' accessorio
            note.append(f"Controllo di copertura non eseguito: {e}")
    return note


# --- rapporto ------------------------------------------------------------------------------------------------------

def _giur(par: dict, pid: str, sid: str, verificate: dict, n: int = 3) -> str:
    voci = {g["sentenza"]: g for g in par[pid].get("giurisprudenza", [])}
    scelte = [x for x in PREFERITE.get(sid, []) if x in voci] or list(voci)[:n]
    tutte = {g["sentenza"]: g for p in par.values() for g in p.get("giurisprudenza", [])}
    scelte = [x for x in PREFERITE.get(sid, []) if x in tutte] or scelte
    out = []
    for k in scelte[:n]:
        g = tutte[k]
        tipo = "ord." if g.get("tipo") == "ordinanza" else "sent."
        stato = "" if verificate.get(k, {}).get("esito") == "verificata" else " (da verificare)"
        out.append(f"{tipo} {k}{stato}: {g['sintesi']}")
    return out


def rapporto(titolo: str, origine: str, arts: list[Art], par: dict, rif: date, note: list[str], verificate: dict) -> str:
    seg = [a for a in arts if a.segnali]
    conta = {liv: sum(1 for a in seg if a.livello == PESO[liv]) for liv in PESO}
    L = [f"# Screening costituzionale: {titolo}", "",
         "> **Screening automatico, non e' un parere.** Questo rapporto e' prodotto da `costituzione/controllo.py` con regole "
         "testuali fisse: segnala dove guardare, non decide la legittimita'. Puo' dare falsi positivi (parole presenti in un "
         "contesto innocuo) e falsi negativi (vizi che non lasciano tracce testuali). Ogni rilievo `alto` o `medio` va "
         "esaminato secondo `costituzione/istruzioni_costituzionalista.md`.", "",
         f"- Origine: `{origine}`",
         f"- Data di riferimento per la retroattivita': {rif.isoformat()}",
         f"- Parametri: `costituzione/parametri.yaml` ({len(par)} parametri); giurisprudenza verificata sui dati aperti della Corte",
         f"- Articoli esaminati: {len(arts)}; con segnali: {len(seg)} (alto {conta['alto']}, medio {conta['medio']}, basso {conta['basso']})",
         "", "## Sintesi", "", "| Art. | Rubrica | Livello | Parametri | Segnali |", "|---|---|---|---|---|"]
    for a in sorted(seg, key=lambda a: (-a.livello, _num(a.numero))):
        if a.livello < 2:
            continue
        pars = sorted({s.parametro for s in a.segnali if PESO[s.livello] >= 2})
        ids = sorted({s.id for s in a.segnali if PESO[s.livello] >= 2})
        L.append(f"| {a.numero} | {_cella(a.rubrica)[:90]} | {ICONA[NOME_LIV[a.livello]]} | {', '.join(pars)} | {', '.join(ids)} |")
    L += ["", "## Rilievi per articolo (livello alto e medio)", ""]
    for a in sorted(seg, key=lambda a: _num(a.numero)):
        if a.livello < 2:
            continue
        L.append(f"### Art. {a.numero}" + (f" ({a.rubrica})" if a.rubrica else "") + f": {ICONA[NOME_LIV[a.livello]]}")
        L.append("")
        per_par: dict[str, list[Segnale]] = {}
        for s in a.segnali:
            if PESO[s.livello] >= 2:
                per_par.setdefault(s.parametro, []).append(s)
        for pid, ss in sorted(per_par.items(), key=lambda kv: -max(PESO[s.livello] for s in kv[1])):
            p = par[pid]
            liv = NOME_LIV[max(PESO[s.livello] for s in ss)]
            L.append(f"**[{liv}] {p['titolo']}** ({'; '.join(p['articoli'][:3])})")
            for s in ss:
                dove = f"comma {s.comma}" if s.comma else "articolo"
                L.append(f"- `{s.id}` ({s.livello}, {dove}): {s.nota}" + (f". Testo: {s.estratto}" if s.estratto else ""))
            sid = max(ss, key=lambda s: PESO[s.livello]).id
            L.append("- Giurisprudenza:")
            L += [f"  - {g}" for g in _giur(par, pid, sid, verificate)]
            L.append("- Domande per l'esame approfondito:")
            L += [f"  - {d}" for d in p.get("domande", [])[:3]]
            L.append("")
    bassi, visti = [], set()
    for a in arts:
        for s in a.segnali:
            if s.livello == "basso" and a.livello == 1 and (a.numero, s.parametro, s.id) not in visti:
                visti.add((a.numero, s.parametro, s.id))
                bassi.append((a, s))
    if bassi:
        L += ["## Segnali di livello basso", "", "| Art. | Parametro | Segnale | Nota |", "|---|---|---|---|"]
        for a, s in bassi[:200]:
            L.append(f"| {a.numero} | {s.parametro} | {s.id} | {_cella(s.nota)} |")
        L.append("")
    L += ["## Controlli sull'intero testo", ""] + [f"- {n}" for n in note] if note else []
    L += ["", "## Prossimo passo", "",
          "Esame approfondito secondo `costituzione/istruzioni_costituzionalista.md`: leggere gli articoli segnalati nel testo "
          "integrale, verificare la giurisprudenza (`python costituzione/giurisprudenza.py --verifica N/AAAA` e `--cerca`), "
          "classificare ogni rilievo come *illegittimita' probabile*, *dubbio serio* o *rischio basso* e proporre una "
          "riformulazione conforme."]
    return "\n".join(L) + "\n"


def _num(n: str) -> tuple:
    m = re.match(r"(\d+)", n)
    return (int(m.group(1)) if m else 10 ** 6, n)


def _cella(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ")


# --- esecuzione ----------------------------------------------------------------------------------------------------

def carica_parametri() -> tuple[dict, dict]:
    par = yaml.safe_load((QUI / "parametri.yaml").read_text(encoding="utf-8"))["parametri"]
    try:
        ver = json.loads((QUI / "giurisprudenza_verificata.json").read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        ver = {}
    return par, ver


def esamina(testo: str, rif: date, intervallo: tuple[int, int] | None = None) -> tuple[list[Art], bool, bool]:
    par, _ = carica_parametri()
    bilancio = bool(re.search(r"(?i)Bilancio di previsione dello Stato per l'anno finanziario|livelli massimi del saldo netto da finanziare", testo[:20000]))
    dl = bool(re.search(r"(?i)Ritenuta la straordinaria necessità e urgenza", testo))
    arts = articoli(testo)
    if intervallo:
        arts = [a for a in arts if intervallo[0] <= _num(a.numero)[0] <= intervallo[1]]
    for a in arts:
        base = segnali_yaml(par, a)
        if not dl:  # i segnali propri dei decreti-legge valgono solo per i decreti-legge
            base = [s for s in base if s.parametro != "decreti_legge" or s.id == "dl_conversione"]
        a.segnali = tara(base, regole_combinate(a, base, rif, bilancio))
    return arts, bilancio, dl


def esegui_file(src: Path, nome: str, rif: date, intervallo=None, titolo: str | None = None, cartella: Path = ESAMI,
                scheda: str | None = None) -> tuple[Path, dict]:
    par, ver = carica_parametri()
    testo = leggi(src)
    if scheda:  # solo l'"Articolato normativo essenziale" di una scheda del programma
        from verifica_testo import estrai_scheda
        testo = estrai_scheda(testo, scheda)[1]
    arts, bilancio, dl = esamina(testo, rif, intervallo)
    note = controlli_globali(testo, arts, bilancio, dl)
    try:
        origine = src.resolve().relative_to(RADICE).as_posix()
    except ValueError:
        origine = src.name
    rep = rapporto(titolo or src.name, origine, arts, par, rif, note, ver)
    cartella.mkdir(parents=True, exist_ok=True)
    out = cartella / f"{nome}.md"
    out.write_text(rep, encoding="utf-8")
    sintesi = {
        "origine": origine, "data_riferimento": rif.isoformat(), "articoli": len(arts),
        "alto": [a.numero for a in arts if a.livello == 3], "medio": [a.numero for a in arts if a.livello == 2],
        "rilievi": [{"art": a.numero, "rubrica": a.rubrica, "parametro": s.parametro, "segnale": s.id, "livello": s.livello,
                     "comma": s.comma, "nota": s.nota} for a in arts for s in a.segnali],
    }
    (cartella / f"{nome}.json").write_text(json.dumps(sintesi, ensure_ascii=False, indent=1), encoding="utf-8")
    return out, sintesi


def esegui_gu(dal: str | None, massimo: int) -> str:
    """Screening degli atti con forza di legge nuovi dell'archivio della Gazzetta (legislazione/archivio)."""
    indice = RADICE / "legislazione" / "archivio" / "indice.csv"
    if not indice.exists():
        return "costituzione: archivio GU assente, nessuno screening"
    stato = json.loads(STATO_GU.read_text(encoding="utf-8")) if STATO_GU.exists() else {"esaminati": {}}
    fatti, alti = 0, []
    for r in csv.DictReader(indice.open(encoding="utf-8")):
        if r["tipo"] not in ("legge", "decreto-legge", "decreto legislativo"):
            continue
        if r["testo_stato"] not in ("ok", "parziale") or not r["testo"] or r["codice"] in stato["esaminati"]:
            continue
        if dal and r["data_gu"] < dal:
            continue
        src = RADICE / "legislazione" / "archivio" / r["testo"]
        if not src.exists():
            continue
        try:
            rif = date.fromisoformat(r.get("entrata_in_vigore") or r["data_gu"])
        except ValueError:
            rif = date.fromisoformat(r["data_gu"])
        titolo = f"{r['tipo']} {r['data_atto']} n. {r['numero_atto']}: {r['titolo'][:140]}"
        _, s = esegui_file(src, r["codice"], rif, titolo=titolo, cartella=ESAMI_GU)
        stato["esaminati"][r["codice"]] = {"data_gu": r["data_gu"], "titolo": titolo, "alto": s["alto"], "medio": s["medio"]}
        if s["alto"]:
            alti.append(f"{r['tipo']} n. {r['numero_atto']}/{r['data_atto'][:4]} (artt. {', '.join(s['alto'][:6])})")
        fatti += 1
        if fatti >= massimo:
            break
    ESAMI_GU.mkdir(parents=True, exist_ok=True)
    STATO_GU.write_text(json.dumps(stato, ensure_ascii=False, indent=1), encoding="utf-8")
    return (f"costituzione: {fatti} atti con forza di legge esaminati; con segnali alti {len(alti)}"
            + (": " + "; ".join(alti[:5]) if alti else ""))


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Screening costituzionale deterministico di un testo normativo")
    ap.add_argument("file", nargs="?", help="file .txt, .md o .pdf")
    ap.add_argument("--nome", help="nome del rapporto in esami/ (default: nome del file)")
    ap.add_argument("--titolo", help="titolo del rapporto")
    ap.add_argument("--data", help="data di riferimento AAAA-MM-GG per la retroattivita' (default: oggi)")
    ap.add_argument("--articoli", help="intervallo di articoli, es. 1-137")
    ap.add_argument("--scheda", help="id di una scheda del programma (es. 01-P2): esamina solo il suo articolato")
    ap.add_argument("--gu", action="store_true", help="esamina gli atti con forza di legge nuovi dell'archivio GU")
    ap.add_argument("--dal", help="con --gu: solo atti pubblicati da questa data")
    ap.add_argument("--max", type=int, default=50, help="con --gu: numero massimo di atti per esecuzione")
    a = ap.parse_args()
    if a.gu:
        print(esegui_gu(a.dal, a.max))
        return 0
    if not a.file:
        ap.error("indicare un file oppure --gu")
    src = Path(a.file)
    rif = date.fromisoformat(a.data) if a.data else date.today()
    intervallo = tuple(int(x) for x in a.articoli.split("-")) if a.articoli else None
    out, s = esegui_file(src, a.nome or (a.scheda or src.stem), rif, intervallo, a.titolo, scheda=a.scheda)
    print(f"rapporto: {out} — articoli {s['articoli']}, alto {len(s['alto'])}, medio {len(s['medio'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
