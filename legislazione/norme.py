"""Libreria comune di `legislazione/`: rete, percorsi e riconoscimento dei riferimenti normativi.

Usata da `scarica_gu.py`, `cerca.py` e `verifica_testo.py`.

- `trova_riferimenti(testo)` riconosce le citazioni di atti statali ("legge 31 dicembre 2009, n. 196",
  "d.lgs. n. 23 del 2011", "decreto-legge 6 novembre 2026, n. 200", "L. 196/2009") e le normalizza
  in un `Riferimento` (tipo, data, anno, numero).
- `urn_normattiva(rif)` costruisce l'URN NIR, risolvibile su https://www.normattiva.it/uri-res/N2Ls?<urn>.
- `verifica_normattiva(rif)` interroga il risolutore URN di Normattiva (con cache locale) e dice se l'atto esiste
  e qual è la sua intestazione ufficiale.
"""
from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import requests

QUI = Path(__file__).resolve().parent
ARCHIVIO = QUI / "archivio"
INDICE = ARCHIVIO / "indice.csv"
TESTI = ARCHIVIO / "testi"
STATO = ARCHIVIO / "stato.json"
CACHE_NORMATTIVA = ARCHIVIO / "cache_normattiva.json"

TIMEOUT = 60
# User-Agent dichiarato: chi gestisce i siti sa chi siamo e perché scarichiamo
HEADERS = {"User-Agent": "GovernAI-legislazione/0.1 (prototipo open source di ricerca; archivio Gazzetta Ufficiale; "
                         "max 1 richiesta al secondo)"}
PAUSA = 1.0  # secondi tra due richieste allo stesso sito

GU = "https://www.gazzettaufficiale.it"
NORMATTIVA = "https://www.normattiva.it"
NORMATTIVA_API = "https://api.normattiva.it/t/normattiva.api/bff-opendata/v1/api/v1"

MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre",
        "ottobre", "novembre", "dicembre"]


# --- Rete ----------------------------------------------------------------------

class Cortese:
    """Sessione HTTP che rispetta una pausa minima tra le richieste e riprova con attesa crescente."""

    def __init__(self, pausa: float = PAUSA):
        self.s = requests.Session()
        self.s.headers.update(HEADERS)
        self.pausa = pausa
        self._ultima = 0.0
        self.richieste = 0

    def _attendi(self):
        d = time.monotonic() - self._ultima
        if d < self.pausa:
            time.sleep(self.pausa - d)
        self._ultima = time.monotonic()

    def get(self, url: str, **kw) -> requests.Response:
        return self._fai("get", url, **kw)

    def post(self, url: str, **kw) -> requests.Response:
        return self._fai("post", url, **kw)

    def _fai(self, metodo: str, url: str, tentativi: int = 3, **kw) -> requests.Response:
        for i in range(tentativi):
            self._attendi()
            self.richieste += 1
            try:
                r = getattr(self.s, metodo)(url, timeout=kw.pop("timeout", TIMEOUT), **kw)
                if r.status_code in (429, 500, 502, 503, 504):
                    raise requests.HTTPError(f"HTTP {r.status_code}")
                r.raise_for_status()
                return r
            except requests.RequestException:
                if i == tentativi - 1:
                    raise
                time.sleep(5 * (i + 1))
        raise RuntimeError("irraggiungibile")


# --- Riferimenti normativi ------------------------------------------------------

# tipo canonico -> (pattern delle forme estese e abbreviate, segmento URN NIR)
TIPI = {
    "legge costituzionale": (r"legge\s+costituzionale|l\.\s*cost\.", "legge.costituzionale"),
    "decreto-legge": (r"decreto[\s-]+legge|d\.\s*l\.|dl", "decreto.legge"),
    "decreto legislativo": (r"decreto\s+legislativo|d\.\s*lgs\.?|dlgs|d\.\s*leg\.?", "decreto.legislativo"),
    "decreto del Presidente della Repubblica": (r"decreto\s+del\s+presidente\s+della\s+repubblica|d\.\s*p\.\s*r\.|dpr",
                                                "decreto.del.presidente.della.repubblica"),
    "decreto del Presidente del Consiglio dei ministri": (
        r"decreto\s+del\s+presidente\s+del\s+consiglio\s+dei\s+ministri|d\.\s*p\.\s*c\.\s*m\.|dpcm", None),
    "regio decreto": (r"regio\s+decreto|r\.\s*d\.", "regio.decreto"),
    "legge": (r"legge|l\.", "legge"),
}
_TIPO_RE = "|".join(f"(?P<t{i}>{p})" for i, (p, _) in enumerate(TIPI.values()))
_DATA_RE = r"(?P<g>\d{1,2})(?:°|º)?\s+(?P<m>" + "|".join(MESI) + r")\s+(?P<a>\d{4})"

# Forma completa: "legge 31 dicembre 2009, n. 196"
RE_COMPLETO = re.compile(rf"\b(?:{_TIPO_RE})\s+{_DATA_RE}\s*,?\s*n\.\s*(?P<n>\d+(?:-\w+)?)", re.I)
# Forma breve: "legge n. 196 del 2009", "d.lgs. n. 23/2011", "L. 196/2009", "DL 200/2026"
RE_BREVE = re.compile(rf"(?<![\w.])(?:{_TIPO_RE})\s*(?:n\.\s*)?(?P<n>\d+)\s*(?:/|\s+del(?:l')?\s*)(?P<a>(?:19|20)\d{{2}})\b", re.I)
# Forma incompleta: tipo + numero senza anno né data ("legge n. 196")
RE_SOLO_NUMERO = re.compile(rf"(?<![\w.])(?:{_TIPO_RE})\s+n\.\s*(?P<n>\d+)\b(?!\s*(?:/|del))", re.I)
# Atti dell'Unione
RE_UE = re.compile(r"\b(?P<tipo>regolamento|direttiva|decisione)\s*(?:delegat[oa]\s*|di esecuzione\s*)?"
                   r"\((?P<org>UE|CE|CEE|Euratom)\)\s*(?:n\.\s*)?(?P<id>\d{2,4}/\d{1,4}(?:/\w+)?)", re.I)


@dataclass
class Riferimento:
    tipo: str
    numero: str
    anno: int | None
    data: date | None = None
    testo: str = ""
    forma: str = "completa"  # completa | breve | incompleta
    pos: int = 0
    extra: dict = field(default_factory=dict)

    @property
    def chiave(self) -> str:
        return f"{self.tipo}|{self.anno}|{self.numero}"

    def descrizione(self) -> str:
        if self.data:
            return f"{self.tipo} {self.data.day} {MESI[self.data.month - 1]} {self.data.year}, n. {self.numero}"
        return f"{self.tipo} n. {self.numero}" + (f" del {self.anno}" if self.anno else "")


def _tipo_da_match(m: re.Match) -> str:
    nomi = list(TIPI)
    for i in range(len(nomi)):
        if m.group(f"t{i}"):
            return nomi[i]
    return "atto"


def trova_riferimenti(testo: str) -> list[Riferimento]:
    """Tutti i riferimenti ad atti statali nel testo, in ordine di posizione, senza sovrapposizioni."""
    trovati: list[Riferimento] = []
    occupato: list[tuple[int, int]] = []

    def libero(a, b):
        return all(b <= x or a >= y for x, y in occupato)

    for m in RE_COMPLETO.finditer(testo):
        try:
            d = date(int(m["a"]), MESI.index(m["m"].lower()) + 1, int(m["g"]))
        except ValueError:
            d = None
        trovati.append(Riferimento(_tipo_da_match(m), m["n"], int(m["a"]), d, m.group(0), "completa", m.start()))
        occupato.append(m.span())
    for m in RE_BREVE.finditer(testo):
        if libero(*m.span()):
            trovati.append(Riferimento(_tipo_da_match(m), m["n"], int(m["a"]), None, m.group(0), "breve", m.start()))
            occupato.append(m.span())
    for m in RE_SOLO_NUMERO.finditer(testo):
        if libero(*m.span()):
            trovati.append(Riferimento(_tipo_da_match(m), m["n"], None, None, m.group(0), "incompleta", m.start()))
            occupato.append(m.span())
    return sorted(trovati, key=lambda r: r.pos)


def trova_atti_ue(testo: str) -> list[dict]:
    return [{"tipo": m["tipo"].lower(), "org": m["org"].upper(), "id": m["id"], "testo": m.group(0), "pos": m.start()}
            for m in RE_UE.finditer(testo)]


def urn_normattiva(rif: Riferimento) -> str | None:
    seg = TIPI.get(rif.tipo, (None, None))[1]
    if not seg or not rif.anno:
        return None
    quando = rif.data.isoformat() if rif.data else str(rif.anno)
    return f"urn:nir:stato:{seg}:{quando};{rif.numero}"


def url_normattiva(rif: Riferimento) -> str | None:
    u = urn_normattiva(rif)
    return f"{NORMATTIVA}/uri-res/N2Ls?{u}" if u else None


def _carica_cache() -> dict:
    try:
        return json.loads(CACHE_NORMATTIVA.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


_cache: dict | None = None
_sessione: Cortese | None = None


def verifica_normattiva(rif: Riferimento, rete: bool = True) -> dict:
    """Risolve l'URN su Normattiva. Esito: {'esito': 'trovato'|'non_trovato'|'non_verificabile'|'errore',
    'intestazione': 'LEGGE 31 dicembre 2009, n. 196', 'url': ...}. I risultati sono messi in cache."""
    global _cache, _sessione
    urn = urn_normattiva(rif)
    if not urn:
        return {"esito": "non_verificabile", "url": None, "intestazione": ""}
    if _cache is None:
        _cache = _carica_cache()
    if urn in _cache:
        return _cache[urn]
    if not rete:
        return {"esito": "non_verificabile", "url": url_normattiva(rif), "intestazione": ""}
    _sessione = _sessione or Cortese()
    try:
        t = _sessione.get(url_normattiva(rif)).text
    except Exception as e:  # rete assente o sito bloccato: non è un errore del testo
        return {"esito": "errore", "url": url_normattiva(rif), "intestazione": str(e)[:100]}
    m = re.search(r"<title>(.*?)</title>", t, re.S)
    titolo = re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
    if "Errore" in titolo or not titolo:
        out = {"esito": "non_trovato", "url": url_normattiva(rif), "intestazione": ""}
    else:
        out = {"esito": "trovato", "url": url_normattiva(rif), "intestazione": titolo.replace(" - Normattiva", "")}
    _cache[urn] = out
    ARCHIVIO.mkdir(parents=True, exist_ok=True)
    CACHE_NORMATTIVA.write_text(json.dumps(_cache, ensure_ascii=False, indent=0), encoding="utf-8")
    return out


def data_da_intestazione(s: str) -> date | None:
    m = re.search(_DATA_RE, s, re.I)
    if not m:
        return None
    try:
        return date(int(m["a"]), MESI.index(m["m"].lower()) + 1, int(m["g"]))
    except ValueError:
        return None
