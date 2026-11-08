"""Assistente redazionale deterministico per testi di legge ed emendamenti.

Legge un file .md o .txt con un articolato (o una sezione "Articolato normativo essenziale" di una scheda)
e produce un rapporto markdown con errori, avvisi e suggerimenti, secondo le regole di
`regole_redazione.md` (Circolare PCM 2 maggio 2001; Regole e raccomandazioni 20 aprile 2001;
art. 81 Cost. e art. 17 L. 196/2009; L. 400/1988; L. 212/2000).

Controlli:
  struttura      articoli numerati e in sequenza, rubriche uniformi, commi numerati e in sequenza,
                 niente elenchi puntati, lettere ammesse, segnaposto e varianti lasciati nel testo
  linguaggio     "e/o", "deve/devono", "qualora", rinvii relativi, "e successive modificazioni e integrazioni",
                 sigle non definite, abbreviazioni di importi (mln, mld)
  riferimenti    forma completa (tipo, data, numero) alla prima citazione; esistenza e data verificate
                 nell'archivio GU e sul risolutore URN di Normattiva; rinvii interni ad articoli o commi inesistenti;
                 atti UE citati in forma informale
  novelle        formule «le parole … sono sostituite dalle seguenti: …», collocazione (articolo, comma, atto),
                 virgolette basse, modifiche non testuali
  abrogazioni    abrogazioni innominate ("le disposizioni incompatibili sono abrogate"); novelle annunciate ma assenti
  finanza        clausola di copertura o di invarianza (art. 81 Cost.), quantificazione per anno, mezzi di copertura
                 dell'art. 17, comma 1, L. 196/2009, coperture fragili (risparmi, entrate future, bilanci delle Camere)
  termini        entrata in vigore, termini senza decorrenza, deleghe senza termine o criteri, decreti attuativi senza termine

Uso:
  python verifica_testo.py bozza.md                                   # rapporto a video
  python verifica_testo.py ../programma/schede/01_economia.md --scheda 01-P2 -o prove/01-P2.md
  python verifica_testo.py bozza.md --senza-rete                      # niente verifiche su Normattiva
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))  # anche con python -I
from norme import MESI, Riferimento, data_da_intestazione, trova_atti_ue, trova_riferimenti, verifica_normattiva

QUI = Path(__file__).resolve().parent
LIVELLI = {"errore": "🔴 Errore", "avviso": "🟠 Avviso", "suggerimento": "🔵 Suggerimento"}
SIGLE_NOTE = {"UE", "CE", "CEE", "IVA", "IRPEF", "IRES", "IRAP", "INPS", "INAIL", "ISTAT", "PIL", "TFUE", "CEDU", "II",
              "III", "IV", "VI", "VII", "VIII", "IX", "XI", "XII", "NB", "AI", "IA"}


@dataclass
class Rilievo:
    livello: str
    categoria: str
    dove: str
    problema: str
    proposta: str = ""
    fonte: str = ""


@dataclass
class Articolo:
    numero: str
    rubrica: str
    testo: str
    commi: list[tuple[str, str]]  # (numero, testo); numero "" = comma non numerato


# --- Estrazione del testo --------------------------------------------------------------------

def estrai_scheda(md: str, scheda: str) -> tuple[str, str]:
    """Sezione 'Articolato normativo essenziale' della scheda indicata (es. '01-P2'). Restituisce (intestazione, testo)."""
    m = re.search(rf"^#+\s*{re.escape(scheda)}\b.*$", md, re.M)
    if not m:
        raise SystemExit(f"Scheda {scheda} non trovata.")
    fine = re.search(r"^##\s+\S", md[m.end():], re.M)
    blocco = md[m.end(): m.end() + fine.start()] if fine else md[m.end():]
    a = re.search(r"^.*Articolato normativo essenziale.*$", blocco, re.M | re.I)
    if not a:
        raise SystemExit(f"La scheda {scheda} non ha una sezione 'Articolato normativo essenziale'.")
    resto = blocco[a.end():]
    stop = re.search(r"^(?:#+\s*|\*\*)(?:Cronoprogramma|Indicatori|Rischi)", resto, re.M | re.I)
    return a.group(0), resto[: stop.start()] if stop else resto


def pulisci_md(t: str) -> str:
    t = re.sub(r"^\s*>\s?", "", t, flags=re.M)          # citazioni markdown
    t = t.replace("**", "").replace("__", "")
    t = re.sub(r"(?<![\w*])\*(?!\s)([^*\n]+?)\*(?!\w)", r"\1", t)   # corsivo
    t = re.sub(r"^#+\s*", "", t, flags=re.M)
    t = re.sub(r"^\s*---+\s*$", "", t, flags=re.M)
    return t.strip()


RE_ART = re.compile(r"(?:^|(?<=\n)|(?<=\.\s))(?:Art\.|Articolo)\s+(?P<n>\d+(?:-?(?:bis|ter|quater|quinquies|sexies))?)"
                    r"\s*(?:\((?P<rub>[^)]*(?:\([^)]*\)[^)]*)*)\))?\s*\.?", re.I)


def dividi_articoli(t: str) -> list[Articolo]:
    # intestazioni valide: a inizio riga, oppure dopo la fine di un periodo ma solo se hanno la rubrica
    buoni = []
    for m in RE_ART.finditer(t):
        a_capo = m.start() == 0 or t[m.start() - 1] == "\n"
        if a_capo or (m.group("rub") and t[:m.start()].rstrip().endswith((".", ":", "»"))):
            buoni.append(m)
    arts = []
    for i, m in enumerate(buoni):
        fine = buoni[i + 1].start() if i + 1 < len(buoni) else len(t)
        corpo = t[m.end(): fine].strip()
        arts.append(Articolo(m["n"], (m["rub"] or "").strip(), corpo, dividi_commi(corpo)))
    return arts


RE_COMMA = re.compile(r"(?:^|(?<=\n)|(?<=[.;:»)]\s))(?<!n\.\s)(?P<n>\d+(?:-(?:bis|ter|quater))?)\.\s+(?=[A-ZÀÈÉÌÒÙ«(\[])")


def dividi_commi(corpo: str) -> list[tuple[str, str]]:
    """Commi numerati riconosciuti solo se in sequenza (1, 2, 3 …): evita di scambiare importi o anni per commi."""
    candidati = list(RE_COMMA.finditer(corpo))
    scelti, atteso = [], 1
    for m in candidati:
        n = m["n"]
        base = int(re.match(r"\d+", n).group(0))
        if base == atteso or ("-" in n and base == atteso - 1):
            scelti.append(m)
            atteso = base + 1 if "-" not in n else atteso
    if not scelti:
        return [("", corpo.strip())] if corpo.strip() else []
    out = []
    if corpo[: scelti[0].start()].strip():
        out.append(("", corpo[: scelti[0].start()].strip()))
    for i, m in enumerate(scelti):
        fine = scelti[i + 1].start() if i + 1 < len(scelti) else len(corpo)
        out.append((m["n"], corpo[m.end(): fine].strip()))
    return out


def periodi(t: str) -> list[str]:
    return [p for p in re.split(r"(?<=[.;])\s+(?=[A-ZÀÈ«])", re.sub(r"\s+", " ", t)) if p.strip()]


# --- Controlli ---------------------------------------------------------------------------------

class Verifica:
    def __init__(self, testo: str, intestazione: str = "", rete: bool = True):
        self.originale = testo
        self.testo = pulisci_md(testo)
        self.intestazione = intestazione
        self.rete = rete
        self.r: list[Rilievo] = []
        self.arts = dividi_articoli(self.testo)
        self.riferimenti: list[dict] = []

    def add(self, *a, **k):
        self.r.append(Rilievo(*a, **k))

    def dove(self, art: Articolo, comma: str = "") -> str:
        return f"art. {art.numero}" + (f", comma {comma}" if comma else "")

    def esegui(self) -> "Verifica":
        for f in (self.struttura, self.linguaggio, self.riferimenti_esterni, self.rinvii_interni, self.novelle,
                  self.abrogazioni, self.finanza, self.termini_e_attuazione):
            f()
        return self

    # 1. struttura
    def struttura(self):
        if not self.arts:
            self.add("errore", "struttura", "testo", "Nessun articolo riconosciuto (atteso «Art. 1 (Rubrica).»).",
                     "Dividere il testo in articoli numerati con rubrica.", "RR 2001, n. 5")
            return
        nums = [a.numero for a in self.arts]
        attesi = 1
        for a in self.arts:
            b = int(re.match(r"\d+", a.numero).group(0))
            if "bis" in a.numero or "ter" in a.numero:
                continue
            if b != attesi:
                self.add("errore", "struttura", f"art. {a.numero}", f"Numerazione degli articoli non progressiva ({', '.join(nums)}).",
                         "Numerare gli articoli 1, 2, 3 … senza salti né ripetizioni.", "RR 2001, n. 5")
            attesi = b + 1
        con_rub = [a for a in self.arts if a.rubrica]
        if 0 < len(con_rub) < len(self.arts):
            senza = ", ".join(a.numero for a in self.arts if not a.rubrica)
            self.add("avviso", "struttura", f"art. {senza}", "Rubriche non uniformi: alcuni articoli ne sono privi.",
                     "Dare una rubrica a tutti gli articoli (obbligatoria negli atti di delega).", "RR 2001, n. 5")
        senza_num = [a.numero for a in self.arts if not [c for c in a.commi if c[0]]]
        if senza_num:
            self.add("avviso", "struttura", "art. " + ", ".join(senza_num),
                     f"Commi non numerati in {len(senza_num)} articoli su {len(self.arts)}.",
                     "Numerare ogni comma, anche il comma unico: «1. …»; un comma per ogni precetto.", "RR 2001, n. 7, lett. b)-c)")
        for a in self.arts:
            numerati = [c for c in a.commi if c[0]]
            liberi = [c for c in a.commi if not c[0]]
            if numerati and liberi:
                self.add("avviso", "struttura", self.dove(a), "Testo fuori dai commi numerati: «" + liberi[0][1][:80] + "…».",
                         "Ogni periodo deve stare in un comma numerato.", "RR 2001, n. 7")
            if re.search(r"^\s*[-–•*]\s+\S", a.testo, re.M):
                self.add("errore", "struttura", self.dove(a), "Elenco puntato o con trattini dentro l'articolo.",
                         "Usare lettere «a)», «b)» … e, al loro interno, numeri «1)», «2)».", "RR 2001, n. 7, lett. i)")
            if re.search(r"(?<![\w(])[jkwxy]\)\s", a.testo):
                self.add("avviso", "struttura", self.dove(a), "Lettera non ammessa (j, k, w, x, y).", "", "RR 2001, n. 7, lett. g)")
            seg = re.findall(r"\[[^]]{1,160}\]|\bXX+\b|\.\.\.|…|(?<!Capo )(?<!Titolo )(?<!Sezione )(?<!Parte )"
                             r"(?<![\w'])[XYZ](?![\w'])", a.testo)
            if seg:
                self.add("errore", "struttura", self.dove(a),
                         f"Segnaposto o varianti nel testo normativo: {', '.join(sorted(set(seg))[:5])}.",
                         "Un articolato deve avere una sola versione: scrivere un testo per variante o spostare le varianti in nota.",
                         "Guida 2001, § 1 (chiarezza)")
            if len(a.testo) > 2500 and len([c for c in a.commi if c[0]]) <= 2:
                self.add("suggerimento", "struttura", self.dove(a), "Articolo lungo con pochi commi.",
                         "Un comma = un precetto: dividere in più commi o articoli.", "RR 2001, n. 7")

    # 2. linguaggio
    def linguaggio(self):
        controlli = [
            (r"\be/o\b", "errore", "«e/o» non è ammesso.", "Scegliere «e» oppure «o»; se serve, «anche congiuntamente».", "RR 2001, n. 4, lett. f)"),
            (r"\b(?:deve|devono|dovrà|dovranno)\b", "suggerimento", "Verbo servile «deve/devono».",
             "Preferire l'indicativo presente, che in un testo normativo ha già valore precettivo.", "RR 2001, n. 4, lett. b)"),
            (r"\bqualora\b", "suggerimento", "«qualora» (congiuntivo).", "Preferire «se» o «nel caso in cui» con l'indicativo.", "Guida 2001, § 1.8"),
            (r"\b(?:articolo|comma)\s+(?:precedente|successivo|seguente)\b|\be seguenti\b|\bultimo comma\b|\bpenultimo comma\b",
             "avviso", "Rinvio relativo («precedente», «successivo», «e seguenti»).", "Citare il numero preciso dell'articolo o del comma.", "RR 2001, nn. 11-12"),
            (r"successive modificazioni (?:ed|e) integrazioni|modifiche e integrazioni", "avviso",
             "«e successive modificazioni e integrazioni».", "Scrivere solo «e successive modificazioni» (o nulla: il rinvio è di regola mobile).", "RR 2001, n. 12, lett. b)"),
            (r"\b\d+(?:[.,]\d+)?\s*(?:mln|mld|mrd|M€|mil\.)(?!\w)", "errore", "Importo abbreviato (mln, mld).",
             "Scrivere gli importi per esteso: «400 milioni di euro».", "Guida 2001 (linguaggio); RR 2001, n. 4"),
            (r"\b\d+(?:,\d+)?\s+(?:miliard[io]|milion[ei])(?!\s+(?:di\s+)?euro)(?=[\s,.;])", "avviso",
             "Importo senza unità di misura («di euro»).",
             "Scrivere ogni importo per intero: «0,96 miliardi di euro per l'anno 2027».", "Guida 2001 (chiarezza); L. 196/2009, art. 17"),
            (r"\b(?:in quanto compatibil[ei])\b", "suggerimento", "Rinvio «in quanto compatibili».",
             "Indicare le disposizioni applicabili: il rinvio generico crea incertezza.", "RR 2001, n. 12, lett. d)"),
            (r"(?i)\b(?:ecc\.|etc\.|ad esempio|per esempio)\b", "avviso", "Elencazione aperta o esemplificativa.",
             "Un elenco normativo deve essere chiuso o rinviare a un atto che lo completa.", "Guida 2001 (chiarezza)"),
        ]
        for a in self.arts:
            for pat, liv, prob, prop, fonte in controlli:
                m = re.search(pat, a.testo, re.I if liv != "errore" else 0)
                if m:
                    self.add(liv, "linguaggio", self.dove(a), f"{prob} («{m.group(0)}»)", prop, fonte)
        # sigle
        definite = set(re.findall(r"[(«\"“]\s*([A-Z][A-Za-z\-]{1,9})\s*[)»\"”]", self.testo))
        usate = {}
        senza_varianti = re.sub(r"\[[^\]]*\]", " ", self.testo)
        for m in re.finditer(r"(?<![\w(«\"])([A-Z]{2,6}(?:-[A-Z]+)?)(?![\w)»\"])", senza_varianti):
            s = m.group(1)
            if s not in SIGLE_NOTE and s not in definite:
                usate.setdefault(s, m.start())
        if usate:
            elenco = ", ".join(sorted(usate)[:12])
            self.add("avviso", "linguaggio", "testo", f"Sigle usate senza essere definite: {elenco}.",
                     "Alla prima occorrenza scrivere la denominazione completa seguita dalla sigla tra parentesi, "
                     "es. «Servizio sanitario nazionale (SSN)», oppure definirla nell'articolo sulle definizioni.", "RR 2001, n. 4; Guida 2001, § 1.4")

    # 3. riferimenti ad atti esterni
    def riferimenti_esterni(self):
        rifs = trova_riferimenti(self.testo)
        visti_completi: dict[str, Riferimento] = {}
        gia: dict[str, tuple[dict, str]] = {}
        for rf in rifs:
            dove = self._dove_pos(rf.pos)
            ver = {"esito": "non_verificabile", "intestazione": "", "url": None}
            fonte_ver = ""
            if rf.anno:
                arch = self._in_archivio(rf)
                if arch:
                    ver = {"esito": "trovato", "intestazione": arch["intestazione"], "url": arch["url_gu"]}
                    fonte_ver = "archivio GU"
                elif rf.chiave in gia:
                    ver, fonte_ver = gia[rf.chiave]
                else:
                    ver = verifica_normattiva(rf, rete=self.rete)
                    fonte_ver = "Normattiva" if ver["esito"] in ("trovato", "non_trovato") else ""
                gia.setdefault(rf.chiave, (ver, fonte_ver))
            uff = ver.get("intestazione", "")
            completa = self._citazione_completa(rf, uff)
            self.riferimenti.append({"citazione": rf.testo, "forma": rf.forma, "dove": dove, "esito": ver["esito"],
                                     "fonte": fonte_ver, "ufficiale": uff, "url": ver.get("url"), "completa": completa})
            if rf.forma == "incompleta":
                self.add("errore", "riferimenti", dove, f"Riferimento senza anno né data: «{rf.testo}».",
                         "Citare tipo, data e numero: «legge 23 agosto 1988, n. 400».", "RR 2001, n. 12, lett. a)")
                continue
            if ver["esito"] == "non_trovato":
                self.add("errore", "riferimenti", dove, f"Atto non trovato su Normattiva: «{rf.testo}» (tipo, numero o anno errati?).",
                         "Controllare gli estremi sull'atto ufficiale.", "Verifica URN Normattiva")
            if rf.data and uff:
                d_uff = data_da_intestazione(uff)
                if d_uff and d_uff != rf.data:
                    self.add("errore", "riferimenti", dove, f"Data errata in «{rf.testo}»: l'atto ufficiale è «{uff}».",
                             f"Correggere in «{completa}».", "Normattiva")
            if rf.forma == "breve":
                if rf.chiave not in visti_completi:
                    self.add("avviso", "riferimenti", dove, f"Prima citazione in forma abbreviata: «{rf.testo}».",
                             f"Alla prima citazione usare la forma completa: «{completa}»." if completa else
                             "Alla prima citazione indicare tipo, data e numero.", "RR 2001, n. 12, lett. a)")
                    visti_completi[rf.chiave] = rf
                if re.match(r"(?i)(?:d\.\s*lgs|dlgs|l\.|d\.\s*l\.|dl\b|dpr|d\.\s*p\.\s*r)", rf.testo):
                    self.add("suggerimento", "riferimenti", dove, f"Denominazione abbreviata dell'atto: «{rf.testo}».",
                             "Nel testo normativo scrivere «decreto legislativo», «legge», «decreto-legge» per esteso.", "RR 2001, n. 12")
            else:
                visti_completi.setdefault(rf.chiave, rf)
        for ue in trova_atti_ue(self.testo):
            pass  # forma corretta riconosciuta
        for m in re.finditer(r"\b(?:Reg\.|Dir\.)\s*(?:\(?UE\)?|CE)\s*(?:n\.\s*)?\d{2,4}/\d+", self.testo):
            self.add("avviso", "riferimenti", self._dove_pos(m.start()), f"Atto UE citato in forma informale: «{m.group(0)}».",
                     "Scrivere «regolamento (UE) AAAA/N del Parlamento europeo e del Consiglio, del …».", "RR 2001, n. 12, lett. r)")
        for m in re.finditer(r"\b(?:art\.|artt\.)\s*\d+", self.testo):
            self.add("suggerimento", "riferimenti", self._dove_pos(m.start()), f"Abbreviazione «{m.group(0)}».",
                     "Nel dispositivo scrivere «articolo» per esteso.", "RR 2001, n. 12")
            break

    def _in_archivio(self, rf: Riferimento) -> dict | None:
        try:
            from cerca import trova_atto
            d = trova_atto(rf)
            return d.iloc[0].to_dict() if len(d) else None
        except (SystemExit, Exception):
            return None

    @staticmethod
    def _citazione_completa(rf: Riferimento, ufficiale: str) -> str:
        d = data_da_intestazione(ufficiale) if ufficiale else rf.data
        if not d:
            return ""
        return f"{rf.tipo} {d.day}{'°' if d.day == 1 else ''} {MESI[d.month - 1]} {d.year}, n. {rf.numero}"

    def _dove_pos(self, pos: int) -> str:
        # posizione nel testo pulito -> articolo
        best = "testo"
        for a in self.arts:
            i = self.testo.find(a.testo[:60]) if a.testo else -1
            if 0 <= i <= pos:
                best = f"art. {a.numero}"
        return best

    # 4. rinvii interni
    def rinvii_interni(self):
        numeri = {a.numero for a in self.arts}
        ordinali = r"(?:primo|secondo|terzo|quarto|quinto|sesto|settimo|ottavo|nono|decimo|ultimo)"
        partizione = (rf"(?:e\s+\d+(?:-\w+)?|\d+(?:-\w+)?|{ordinali}\s+(?:comma|periodo)|comm[ai]\s+\d+(?:-\w+)?(?:\s*(?:,|e)\s*\d+(?:-\w+)?)*|"
                      r"letter[ae]\s+\w+\)(?:\s*(?:,|e)\s*\w+\))*|numer[oi]\s+\d+\)|allegato\s+\w+)")
        esterno = re.compile(rf"^(?:\s*,?\s*{partizione})*\s*,?\s*(?:della|del|dello|dei|degli|delle|al|alla|allo|n\.|"
                             r"TUIR|TFUE|Cost\.)", re.I)
        for a in self.arts:
            for m in re.finditer(r"\b(?:all'|dell'|nell'|dall'|sull'|l')?articol[oi]\s+(\d+(?:-\w+)?)", a.testo):
                dopo = a.testo[m.end(): m.end() + 160]
                if esterno.match(dopo) and not re.match(rf"^(?:\s*,?\s*{partizione})*\s*,?\s*dell[ao] present[ei]", dopo, re.I):
                    continue
                if m.group(1) not in numeri:
                    self.add("errore", "rinvii interni", self.dove(a),
                             f"Rinvio all'articolo {m.group(1)}, che non esiste in questo testo (né è seguito dall'atto esterno).",
                             "Correggere il numero o completare il rinvio con l'atto: «articolo N della legge …».", "RR 2001, n. 11")
            commi = {c[0] for c in a.commi if c[0]}
            for m in re.finditer(r"\b(?:al|del|dal|nel)\s+comma\s+(\d+(?:-\w+)?)\b(?!\s*,?\s*(?:dell'|della|del)\s)", a.testo):
                if commi and m.group(1) not in commi:
                    self.add("errore", "rinvii interni", self.dove(a), f"Rinvio al comma {m.group(1)}, che non esiste nell'articolo.",
                             "Correggere il numero del comma.", "RR 2001, n. 11")

    # 5. novelle
    def novelle(self):
        t = self.testo
        formule = list(re.finditer(r"(?i)\b(?:sono sostituit[ei]|è sostituit[oa]|è inserit[oa]|sono inserit[ei]|è aggiunt[oa]|"
                                   r"sono aggiunt[ei]|è soppress[oa]|sono soppress[ei]|sono apportate le seguenti modificazioni)\b", t))
        for m in formule:
            s = t[max(0, t.rfind("\n", 0, m.start())): m.end() + 300]
            dove = self._dove_pos(m.start())
            if "«" not in s:
                self.add("errore", "novelle", dove, f"Novella senza testo tra virgolette basse: «…{s.strip()[:90]}…».",
                         "Riportare le parole o il testo nuovo tra « »: «le parole: «x» sono sostituite dalle seguenti: «y»».", "RR 2001, n. 9, lett. c)")
            prima = t[max(0, m.start() - 300): m.start()]
            if not re.search(r"(?i)articol[oi]\s+\d+", prima) or not trova_riferimenti(prima + " "):
                self.add("avviso", "novelle", dove, "La novella non indica con precisione dove interviene (articolo, comma e atto).",
                         "Aprire con «All'articolo X, comma Y, della legge [data], n. [numero], …».", "RR 2001, n. 9, lett. b)")
        for m in re.finditer(r"(?i)sono sostituite dalle seguenti(?!:)", t):
            self.add("suggerimento", "novelle", self._dove_pos(m.start()), "Manca «:» dopo «sono sostituite dalle seguenti».",
                     "«… sono sostituite dalle seguenti: «…»».", "RR 2001, n. 9")
        nontestuali = [
            r"(?i)\bè (?:integrat[oa]|modificat[oa]) nel senso che\b", r"(?i)\bsi intende(?:no)? (?:modificat|sostituit|riferit)",
            r"(?i)\bè (?:integrat[oa]|ampliat[oa]|estes[oa]) (?:da|con)\b", r"(?i)\bè trasformat[oa] in\b",
            r"(?i)\bin deroga (?:a|al|alla|all'|agli|alle)\b",
        ]
        for pat in nontestuali:
            for m in re.finditer(pat, t):
                self.add("avviso", "novelle", self._dove_pos(m.start()), f"Modifica non testuale o deroga implicita: «{m.group(0)}».",
                         "Preferire la novella (testo modificato riscritto) o indicare con precisione la norma derogata.",
                         "RR 2001, n. 9, lett. a); Guida 2001 (novellazione)")
                break
        # l'intestazione annuncia modifiche a leggi esistenti?
        annunciate = trova_riferimenti(self.intestazione) if re.search(r"(?i)modific", self.intestazione) else []
        if annunciate and not formule:
            self.add("errore", "novelle", "intestazione",
                     f"L'articolato dichiara di modificare {', '.join(r.testo for r in annunciate)}, ma non contiene alcuna novella.",
                     "Scrivere le modifiche come novelle: «All'articolo … della legge … sono apportate le seguenti modificazioni: a) …».",
                     "RR 2001, n. 9")

    # 6. abrogazioni
    def abrogazioni(self):
        t = self.testo
        for m in re.finditer(r"(?i)(?:tutte\s+)?le\s+(?:altre\s+)?(?:disposizioni|norme)\s+(?:incompatibili|contrarie|in contrasto)[^.]{0,80}(?:sono\s+)?abrogat[ei]"
                             r"|(?:sono\s+)?abrogat[ei][^.]{0,20}(?:tutte\s+)?le\s+(?:disposizioni|norme)\s+(?:incompatibili|contrarie)", t):
            self.add("errore", "abrogazioni", self._dove_pos(m.start()), f"Abrogazione innominata: «{m.group(0)[:90]}».",
                     "Elencare le disposizioni abrogate: «Sono abrogate, in particolare, le seguenti disposizioni: a) …».", "RR 2001, n. 3, lett. g)-h)")
        sostituisce = re.search(r"(?i)(?<!non )(?<!non la )(?<!non lo )(?<!non li )(?<!non le )\b(?:sostituisce|supera|riordina|sopprime|trasformat[oa] in)\b", t)
        if sostituisce and not re.search(r"(?i)\babrogat", t):
            self.add("avviso", "abrogazioni", self._dove_pos(sostituisce.start()),
                     f"Il testo sostituisce o sopprime una disciplina esistente («{sostituisce.group(0)}») senza abrogazioni espresse.",
                     "Indicare le norme abrogate o modificate; senza, restano dubbi su quale disciplina si applica.", "RR 2001, n. 3, lett. g)")

    # 7. copertura finanziaria
    def finanza(self):
        t = self.testo
        importi = re.findall(r"(?i)\d[\d.,]*\s*(?:milion[ei]|miliard[oi]|mln|mld)(?:\s+di)?\s+(?:di\s+)?euro|\d[\d.]*\s*euro", t)
        onerose = re.search(r"(?i)\b(?:è autorizzata la spesa|è istituito[^.]{0,80}fondo|indennità|borse? di studio|assunzion|"
                            r"contribut[oi]|credito d'imposta|rimborso|incentiv|premio|dotazione)\b", t)
        copertura = re.search(r"(?i)\b(?:agli|ai relativi|al relativo)\s+oner[ei]\b[^\n]{0,400}?\bsi provvede\b|\bsi provvede (?:mediante|a valere)\b", t)
        invarianza = re.search(r"(?i)(?:non (?:devono )?deriva(?:no|re)|senza)\s+nuovi\s+o\s+maggiori\s+oneri", t)
        rubrica_cop = [a for a in self.arts if re.search(r"(?i)copertura|disposizioni finanziarie", a.rubrica)]
        if (importi or onerose) and not copertura:
            self.add("errore", "finanza", "testo", "Il testo prevede spese o benefici ma non ha una clausola di copertura finanziaria.",
                     "Aggiungere l'articolo «Disposizioni finanziarie»: «Agli oneri derivanti dagli articoli …, pari a … euro per l'anno …, "
                     "si provvede mediante …» con un mezzo dell'art. 17, comma 1, della legge 31 dicembre 2009, n. 196.",
                     "Art. 81, terzo comma, Cost.; L. 196/2009, art. 17, c. 1")
        if not importi and not onerose and not copertura and not invarianza:
            self.add("errore", "finanza", "testo", "Manca sia la clausola di copertura sia la clausola di invarianza finanziaria.",
                     "Se il testo non comporta oneri: «Dall'attuazione della presente legge non derivano nuovi o maggiori oneri a carico "
                     "della finanza pubblica. Le amministrazioni interessate provvedono ai relativi adempimenti con le risorse umane, "
                     "strumentali e finanziarie disponibili a legislazione vigente.»", "Art. 81 Cost.; L. 196/2009, art. 17, c. 6-bis")
        if copertura and invarianza:
            m = invarianza
            ctx = t[max(0, m.start() - 80): m.start()]
            if not re.search(r"(?i)fatto salvo|salvo quanto|ad eccezione|fermo restando", ctx):
                self.add("avviso", "finanza", self._dove_pos(m.start()),
                         "Clausola di invarianza accanto a oneri quantificati, senza raccordo: le due affermazioni si contraddicono.",
                         "Scrivere «Fatto salvo quanto previsto dal comma 1, dall'attuazione della presente legge non derivano nuovi "
                         "o maggiori oneri …».", "L. 196/2009, art. 17")
        if invarianza and not re.search(r"(?i)risorse umane, strumentali e finanziarie disponibili a legislazione vigente", t):
            self.add("suggerimento", "finanza", self._dove_pos(invarianza.start()),
                     "Clausola di invarianza senza la seconda parte sulle risorse disponibili.",
                     "Aggiungere: «Le amministrazioni interessate provvedono … con le risorse umane, strumentali e finanziarie "
                     "disponibili a legislazione vigente.» La relazione tecnica deve dimostrare l'invarianza.", "L. 196/2009, art. 17, c. 6-bis")
        if copertura:
            art_cop = next((a for a in self.arts if copertura.group(0)[:40] in a.testo), None)
            blocco = art_cop.testo if art_cop else t[copertura.start(): copertura.start() + 1500]
            dove = self._dove_pos(copertura.start())
            anni = re.findall(r"(?i)(?:per l'anno|per il|nel|dal|a decorrere dal(?:l'anno)?|annui dal)\s+(20\d\d)", blocco)
            if not anni:
                self.add("errore", "finanza", dove, "Oneri non quantificati per ciascun anno.",
                         "Indicare l'importo per ogni anno: «pari a 5 milioni di euro per l'anno 2027 e a 10 milioni di euro annui "
                         "a decorrere dall'anno 2028».", "L. 196/2009, art. 17, c. 1")
            if not re.search(r"(?i)limite massimo di spesa|limiti di spesa|previsioni? di spesa|valutat[io] in", t):
                self.add("avviso", "finanza", dove, "L'onere non è qualificato come limite massimo di spesa o come previsione di spesa.",
                         "Specificare «nel limite massimo di spesa di …» oppure «oneri valutati in …» (con clausola di salvaguardia).",
                         "L. 196/2009, art. 17, c. 1 e 12")
            fragili = [
                (r"(?i)risparmi", "Copertura con «risparmi»: i risparmi si possono contare solo se certi e quantificati (quadro.md: «Risparmi contati solo ex post»)."),
                (r"(?i)maggiori entrate derivanti dalla rimodulazione|maggiori entrate derivanti da(?:lla|ll')?\s+(?!presente|articolo)",
                 "Copertura con maggiori entrate derivanti da misure non scritte in questo testo: la misura che genera l'entrata va disposta nello stesso atto, con la sua quantificazione."),
                (r"(?i)bilanci interni delle Camere|bilanci? (?:della Camera|del Senato)",
                 "Copertura a carico dei bilanci interni delle Camere: le Camere hanno autonomia contabile (art. 64 Cost.); la legge non può disporne."),
                (r"(?i)recupero (?:dell')?evasione|contrasto all'evasione",
                 "Copertura con gettito da recupero dell'evasione: non è un mezzo ammesso se non accertato (art. 17 L. 196/2009; regole UE)."),
                (r"(?i)riduzione (?:delle|dei) (?:spese|stanziamenti) (?:di funzionamento|per)(?![^.]{0,120}autorizzazione di spesa)",
                 "Riduzione di spesa generica: indicare il capitolo o l'autorizzazione di spesa ridotta («corrispondente riduzione dell'autorizzazione di spesa di cui all'articolo …»)."),
                (r"(?i)fondo sanitario nazionale|FSN", "Copertura su risorse del fondo sanitario: chiarire se si riduce il finanziamento a legislazione vigente (non è una nuova risorsa)."),
            ]
            for pat, prob in fragili:
                m = re.search(pat, blocco)
                if m:
                    self.add("avviso", "finanza", dove, prob, "Usare un mezzo dell'elenco tassativo dell'art. 17, comma 1, L. 196/2009.",
                             "L. 196/2009, art. 17, c. 1; giuridico/quadro.md § 3")
        if re.search(r"(?i)il governo è delegato", t) and not re.search(r"(?i)decreti legislativi[^.]{0,200}oneri|oneri[^.]{0,200}decreti legislativi", t):
            self.add("suggerimento", "finanza", "delega",
                     "Delega senza disciplina degli oneri dei decreti legislativi.",
                     "Prevedere che i decreti che comportano oneri siano adottati solo dopo l'entrata in vigore dei provvedimenti che "
                     "stanziano le risorse, o che dai decreti non derivano nuovi o maggiori oneri.", "L. 196/2009, art. 17, c. 2")

    # 8. termini, deleghe, attuazione
    def termini_e_attuazione(self):
        t = self.testo
        if not re.search(r"(?i)entra in vigore|hanno effetto (?:a decorrere )?da|si applica(?:no)? (?:a decorrere )?da", t):
            self.add("suggerimento", "termini", "testo",
                     "Nessuna clausola di entrata in vigore o di decorrenza: vale la vacatio di quindici giorni (art. 73 Cost.).",
                     "Se servono tempi diversi, indicarli con date certe: «Le disposizioni dell'articolo 2 si applicano a decorrere dal 1° gennaio 2028».",
                     "Art. 73, terzo comma, Cost.; RR 2001, n. 15")
        for p in periodi(t):
            for m in re.finditer(r"(?i)\bentro\s+(?:il termine di\s+)?(\w+)\s+(giorni|mesi|anni)\b", p):
                dopo = p[m.end(): m.end() + 120]
                if not re.search(r"(?i)^\s*(?:dalla|dall'|dal|da|a decorrere|successiv|prima)", dopo):
                    self.add("avviso", "termini", self._dove_pos(t.find(p[:50])), f"Termine senza decorrenza: «{m.group(0)}».",
                             "Indicare da quando decorre: «entro sei mesi dalla data di entrata in vigore della presente legge».",
                             "Guida 2001, § 4.7")
        # deleghe
        for m in re.finditer(r"(?i)il governo è delegato ad adottare([^.]*)", t):
            seg = t[m.start(): m.start() + 900]
            dove = self._dove_pos(m.start())
            if not re.search(r"(?i)entro\s+\w+\s+(?:mesi|giorni|anni)|entro il \d", m.group(0)):
                self.add("errore", "deleghe", dove, "Delega senza termine.", "Fissare il termine: «entro dodici mesi dalla data di entrata in vigore della presente legge».",
                         "Art. 76 Cost.; L. 400/1988, art. 14")
            if not re.search(r"(?i)principi e criteri direttivi", seg):
                self.add("errore", "deleghe", dove, "Delega senza «principi e criteri direttivi» espressi.",
                         "Elencare principi e criteri direttivi in lettere a), b), c) …", "Art. 76 Cost.")
            if not re.search(r"(?i)parer[ei]", t):
                self.add("avviso", "deleghe", dove, "Delega senza procedura di adozione (proposta, concerto, pareri parlamentari, intese).",
                         "Prevedere: schemi trasmessi alle Camere per il parere delle Commissioni competenti entro … giorni; "
                         "intesa in Conferenza unificata se tocca materie regionali.", "L. 400/1988, art. 14; Corte cost. 251/2016")
        # rinvii ad atti attuativi
        pat = re.compile(r"(?i)\b(?:con|mediante|secondo il|di cui al)?\s*(?:decreto del Ministro|decreto del Presidente del Consiglio|"
                         r"decreto ministeriale|decreto interministeriale|regolamento (?:adottato|da adottare)|provvediment[oi] del Direttore|"
                         r"decreto del Ministero|decreto direttoriale|linee guida)\b")
        for p in periodi(t):
            m = pat.search(p)
            if not m:
                continue
            dove = self._dove_pos(t.find(p[:50]))
            if not re.search(r"(?i)\bentro\b", p):
                self.add("avviso", "attuazione", dove, f"Rinvio a un atto attuativo senza termine: «{m.group(0).strip()}».",
                         "Indicare chi lo adotta, con quale procedura (concerto, intesa, parere) ed entro quale termine.",
                         "Guida 2001, §§ 4.7, 4.13")
            if re.search(r"(?i)regione|regional|conferenza", p) is None and re.search(r"(?i)sanit|assistenz|istruzion|trasport|turism|territor", p):
                self.add("suggerimento", "attuazione", dove, "Atto attuativo in materia che tocca competenze regionali, senza intesa o parere della Conferenza.",
                         "Valutare l'intesa in Conferenza Stato-Regioni o unificata.", "Art. 117 Cost.; giuridico/quadro.md § 2")
        dispositivo = " ".join(a.testo for a in self.arts if not re.search(r"(?i)copertura|finanziari", a.rubrica))
        if re.search(r"(?i)\bimpost|tribut|aliquot|accis|agevolazion[ei] fiscal|spes[ae] fiscal|detrazion", dispositivo):
            if not re.search(r"(?i)periodo d'imposta successivo|a decorrere dal periodo d'imposta", t):
                self.add("suggerimento", "termini", "testo", "Norma tributaria senza decorrenza dal periodo d'imposta successivo.",
                         "Per i tributi periodici le modifiche si applicano dal periodo d'imposta successivo a quello in corso alla "
                         "data di entrata in vigore (Statuto del contribuente).", "L. 212/2000, art. 3")

    # --- Rapporto ---------------------------------------------------------------------------------
    def rapporto(self, titolo: str, origine: str) -> str:
        cont = {k: sum(1 for x in self.r if x.livello == k) for k in LIVELLI}
        out = [f"# Verifica redazionale — {titolo}", "",
               f"*Generato da `legislazione/verifica_testo.py` il {date.today():%d/%m/%Y}. Testo: `{origine}`. "
               "Controlli deterministici: segnalano possibili problemi, non sostituiscono la revisione giuridica "
               "(vedi `legislazione/istruzioni_revisione.md`).*", "",
               f"**Esito:** {cont['errore']} errori, {cont['avviso']} avvisi, {cont['suggerimento']} suggerimenti. "
               f"Articoli riconosciuti: {len(self.arts)} ({', '.join(a.numero for a in self.arts)}); "
               f"commi numerati: {sum(len([c for c in a.commi if c[0]]) for a in self.arts)}; "
               f"riferimenti normativi: {len(self.riferimenti)}.", ""]
        if self.intestazione:
            out += [f"**Intestazione dichiarata:** {pulisci_md(self.intestazione)}", ""]
        ordine = ["struttura", "linguaggio", "riferimenti", "rinvii interni", "novelle", "abrogazioni", "finanza", "deleghe",
                  "attuazione", "termini"]
        out += ["## Rilievi", ""]
        if not self.r:
            out.append("Nessun rilievo.")
        for cat in ordine:
            righe = [x for x in self.r if x.categoria == cat]
            if not righe:
                continue
            out += [f"### {cat.capitalize()}", "", "| Livello | Dove | Problema | Proposta | Regola |", "|---|---|---|---|---|"]
            for x in sorted(righe, key=lambda x: list(LIVELLI).index(x.livello)):
                out.append(f"| {LIVELLI[x.livello]} | {x.dove} | {_cella(x.problema)} | {_cella(x.proposta)} | {_cella(x.fonte)} |")
            out.append("")
        out += ["## Riferimenti normativi trovati", "",
                "| Citazione | Forma | Dove | Verifica | Atto ufficiale | Forma completa |", "|---|---|---|---|---|---|"]
        for r in self.riferimenti:
            esito = {"trovato": "✅ esiste", "non_trovato": "❌ non trovato", "non_verificabile": "— non verificabile",
                     "errore": "⚠️ rete non disponibile"}[r["esito"]]
            link = f"[{esito}]({r['url']})" if r.get("url") else esito
            fonte = f" ({r['fonte']})" if r.get("fonte") else ""
            out.append(f"| {_cella(r['citazione'])} | {r['forma']} | {r['dove']} | {link}{fonte} | {_cella(r['ufficiale'])} | {_cella(r['completa'])} |")
        ue = trova_atti_ue(self.testo)
        if ue:
            out += ["", "Atti dell'Unione citati (non verificati automaticamente; controllare su EUR-Lex): " +
                    ", ".join(sorted({x['testo'] for x in ue})) + "."]
        out += ["", "## Da completare con la revisione di Claude", "",
                "Seguire `legislazione/istruzioni_revisione.md`: coerenza con la Carta dei 10 valori e con le linee rosse, "
                "conformità con `giuridico/quadro.md`, chiarezza per i cittadini, e verifica dei rilievi qui sopra "
                "(i controlli automatici possono dare falsi positivi)."]
        return "\n".join(out) + "\n"


def _cella(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Verifica redazionale di un testo di legge o emendamento")
    ap.add_argument("file", help="file .md o .txt")
    ap.add_argument("--scheda", help="id della scheda (es. 01-P2): verifica solo il suo 'Articolato normativo essenziale'")
    ap.add_argument("-o", "--output", help="file del rapporto (default: a video)")
    ap.add_argument("--senza-rete", action="store_true", help="non interroga Normattiva (usa solo archivio e cache)")
    a = ap.parse_args()
    src = Path(a.file)
    md = src.read_text(encoding="utf-8")
    intest = ""
    if a.scheda:
        intest, md = estrai_scheda(md, a.scheda)
    v = Verifica(md, intest, rete=not a.senza_rete).esegui()
    titolo = f"scheda {a.scheda}" if a.scheda else src.name
    try:
        origine = src.resolve().relative_to(QUI.parent).as_posix()
    except ValueError:
        origine = src.name
    rep = v.rapporto(titolo, origine + (f" ({a.scheda})" if a.scheda else ""))
    if a.output:
        Path(a.output).parent.mkdir(parents=True, exist_ok=True)
        Path(a.output).write_text(rep, encoding="utf-8")
        e = sum(1 for x in v.r if x.livello == "errore")
        print(f"rapporto: {a.output} — {e} errori, {len(v.r) - e} avvisi e suggerimenti")
    else:
        print(rep)
    return 0


if __name__ == "__main__":
    sys.exit(main())
