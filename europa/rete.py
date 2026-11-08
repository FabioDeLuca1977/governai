"""Libreria comune del modulo europa/: percorsi, rete cortese, SPARQL di CELLAR, cache dell'ultima copia.

Le risposte delle fonti sono DATI: nessun testo scaricato viene mai eseguito o interpretato come istruzione.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import time
from datetime import date
from pathlib import Path

import requests

QUI = Path(__file__).resolve().parent
RADICE = QUI.parent
ARCHIVIO = QUI / "archivio"
CACHE = ARCHIVIO / "cache"
TESTI = ARCHIVIO / "testi"
STATO_ARCHIVIO = ARCHIVIO / "stato.json"

SPARQL = "https://publications.europa.eu/webapi/rdf/sparql"
CELEX_URI = "http://publications.europa.eu/resource/celex/"
EURLEX = "https://eur-lex.europa.eu/legal-content/IT"
EURINFRA = "https://eurinfra.politichecomunitarie.it/ElencoAreaLibera.aspx"
DPE_INFRAZIONI = "https://www.affarieuropei.gov.it/it/attivita/procedure-dinfrazione/stato-delle-infrazioni/"
ECFIN_EDP_ITALIA = ("https://economy-finance.ec.europa.eu/economic-governance-framework/stability-and-growth-pact/"
                    "corrective-arm-excessive-deficit-procedure/excessive-deficit-procedures-overview/italy_en")

TIMEOUT = 120
PAUSA = 1.0
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; GovernAI-europa/0.1; ricerca non commerciale)"}


class Rete:
    """Sessione HTTP con pausa minima tra le richieste e tre tentativi con attesa crescente (come legislazione/norme.py)."""

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

    def fai(self, metodo: str, url: str, tentativi: int = 3, **kw) -> requests.Response:
        timeout = kw.pop("timeout", TIMEOUT)
        for i in range(tentativi):
            self._attendi()
            self.richieste += 1
            try:
                r = self.s.request(metodo, url, timeout=timeout, **kw)
                if r.status_code in (429, 500, 502, 503, 504):
                    raise requests.HTTPError(f"HTTP {r.status_code}")
                r.raise_for_status()
                return r
            except requests.RequestException:
                if i == tentativi - 1:
                    raise
                time.sleep(5 * (i + 1))
        raise RuntimeError("irraggiungibile")

    def get(self, url: str, **kw) -> requests.Response:
        return self.fai("GET", url, **kw)

    def sparql(self, query: str) -> list[dict[str, str]]:
        """Esegue una query SPARQL su CELLAR e restituisce le righe come dizionari di stringhe."""
        r = self.fai("POST", SPARQL, data={"query": query}, timeout=240,
                     headers={"Accept": "application/sparql-results+json"})
        js = r.json()
        righe = js["results"]["bindings"]
        if len(righe) in (10000, 50000, 100000):  # limiti tipici di Virtuoso: il risultato sarebbe troncato in silenzio
            raise ValueError(f"risultato SPARQL troncato a {len(righe)} righe: ridurre la finestra")
        return [{k: pulisci_spazi(v.get("value", "")) for k, v in b.items()} for b in righe]


def pulisci_spazi(s: str) -> str:
    return re.sub(r"[ \t\r\n  ]+", " ", s or "").strip()


def html_a_testo(t: str) -> str:
    t = re.sub(r"<(script|style)\b.*?</\1>", " ", t, flags=re.S | re.I)
    t = re.sub(r"<(br|p|div|tr|li|h\d|table|dt|dd)\b[^>]*>", "\n", t, flags=re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace(" ", " ")
    t = re.sub(r"[ \t]+", " ", t)
    return re.sub(r"\n\s*\n+", "\n", t).strip()


def scarica_con_cache(rete: Rete, url: str, nome: str, **kw) -> tuple[str, str]:
    """Scarica una pagina e ne conserva l'ultima copia in archivio/cache/<nome>.
    Se la fonte non risponde e c'è una copia, usa quella. Restituisce (testo, esito) con esito
    'ok', 'cache (AAAA-MM-GG)' oppure solleva l'eccezione se non c'è nulla."""
    CACHE.mkdir(parents=True, exist_ok=True)
    dest = CACHE / nome
    try:
        r = rete.get(url, **kw)
        try:
            testo = r.content.decode("utf-8")
        except UnicodeDecodeError:
            testo = r.content.decode("cp1252", errors="replace")
        dest.write_text(testo, encoding="utf-8")
        return testo, "ok"
    except requests.RequestException as e:
        if not dest.exists():
            raise
        quando = date.fromtimestamp(dest.stat().st_mtime).isoformat()
        print(f"attenzione: {url} non raggiungibile ({e.__class__.__name__}); uso la copia del {quando}")
        return dest.read_text(encoding="utf-8"), f"cache ({quando})"


def impronta(testo: str) -> str:
    return hashlib.sha256(testo.encode("utf-8")).hexdigest()[:16]


def leggi_json(p: Path, predefinito=None):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return predefinito


def scrivi_json(p: Path, dati) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(dati, ensure_ascii=False, indent=1), encoding="utf-8")


MESI = {m: i for i, m in enumerate(["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto",
                                    "settembre", "ottobre", "novembre", "dicembre"], 1)}


def data_italiana(s: str) -> str:
    """'31 dicembre 2027' o '1 o gennaio 2028' (1º reso come '1 o') -> '2027-12-31'; '' se non riconosciuta."""
    m = re.search(r"(\d{1,2})\s*(?:o|º|°)?\s+(" + "|".join(MESI) + r")\s+(\d{4})", s, flags=re.I)
    if not m:
        return ""
    try:
        return date(int(m.group(3)), MESI[m.group(2).lower()], int(m.group(1))).isoformat()
    except ValueError:
        return ""
