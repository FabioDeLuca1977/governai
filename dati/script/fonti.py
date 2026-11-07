"""Libreria comune di GovernAI per scaricare dati da fonti pubbliche.

Ogni funzione restituisce un DataFrame pandas. `salva()` scrive la serie in
dati/serie/<nome>.csv e registra fonte, URL e data di download in
dati/serie/_registro_<area>.csv, così ogni cifra dei dossier è tracciabile.

Uso tipico:
    from fonti import eurostat, salva
    df = eurostat("gov_10dd_edpt1", geo="IT", unit="PC_GDP", na_item="GD", sector="S13")
    salva(df, "debito_pil_it", fonte="Eurostat gov_10dd_edpt1", url=df.attrs["url"])
"""
from __future__ import annotations

import csv
import io
import itertools
from datetime import date
from pathlib import Path
from urllib.parse import urlencode

import pandas as pd
import requests

BASE = Path(__file__).resolve().parents[1]  # cartella dati/
SERIE = BASE / "serie"
RAW = BASE / "raw"
TIMEOUT = 60
# Alcuni siti istituzionali (camera.it, gse.it) rifiutano User-Agent non standard
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; GovernAI-ricerca/0.1)"}


def _get(url: str, **kw) -> requests.Response:
    r = requests.get(url, timeout=kw.pop("timeout", TIMEOUT), headers={**HEADERS, **kw.pop("headers", {})}, **kw)
    r.raise_for_status()
    return r


# --- Eurostat (API JSON-stat 2.0) -------------------------------------------

def eurostat(dataset: str, since: str | None = None, **filtri) -> pd.DataFrame:
    """Scarica un dataset Eurostat. I filtri sono dimensioni (geo="IT", unit=...).
    Un filtro può essere una lista per più valori (geo=["IT", "EU27_2020"]).
    La colonna `flag` riporta lo stato Eurostat del dato (p = provvisorio, b = rottura di serie, e = stima, ...)."""
    params = []
    for k, v in filtri.items():
        for x in (v if isinstance(v, (list, tuple)) else [v]):
            params.append((k, x))
    if since:
        params.append(("sinceTimePeriod", since))
    url = f"https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/{dataset}?{urlencode(params)}"
    js = _get(url).json()
    dims = js["id"]
    cats = [sorted(js["dimension"][d]["category"]["index"].items(), key=lambda kv: kv[1]) for d in dims]
    stati = js.get("status", {})
    righe = []
    for i, combo in enumerate(itertools.product(*cats)):
        v = js["value"].get(str(i))
        if v is not None:
            righe.append({**{d: c[0] for d, c in zip(dims, combo)}, "valore": v, "flag": stati.get(str(i), "")})
    df = pd.DataFrame(righe)
    df.attrs.update(url=url, aggiornato=js.get("updated"), etichetta=js.get("label"))
    return df


# --- ISTAT (SDMX REST, esploradati.istat.it) --------------------------------

ISTAT_WS = "https://esploradati.istat.it/SDMXWS/rest"


def istat(flusso: str, chiave: str = "", since: str | None = None, timeout: int = 180) -> pd.DataFrame:
    """Scarica dati ISTAT in formato SDMX-CSV. `flusso` es. "22_289",
    `chiave` es. "A.IT.JAN.9.TOTAL.99" (vuota = tutto, attenzione alle dimensioni).
    Il servizio ISTAT è lento: alzare `timeout` per flussi grandi."""
    url = f"{ISTAT_WS}/data/IT1,{flusso},1.0/{chiave or 'ALL'}"
    if since:
        url += f"?startPeriod={since}"
    r = _get(url, timeout=timeout, headers={"Accept": "application/vnd.sdmx.data+csv;version=1.0.0"})
    df = pd.read_csv(io.StringIO(r.text))
    df.attrs.update(url=url)
    return df


def istat_cerca(testo: str) -> pd.DataFrame:
    """Cerca tra i flussi ISTAT per parola chiave nel nome (l'elenco completo è lento: ~1-3 minuti)."""
    r = _get(f"{ISTAT_WS}/dataflow/IT1", timeout=300, headers={"Accept": "application/vnd.sdmx.structure+json;version=1.0"})
    flows = r.json()["data"]["dataflows"]
    righe = [{"id": f["id"], "nome": f.get("names", {}).get("it") or f.get("name")} for f in flows]
    df = pd.DataFrame(righe)
    return df[df["nome"].str.contains(testo, case=False, na=False)]


# --- dati.gov.it (CKAN) -----------------------------------------------------

def datigov_cerca(q: str, righe: int = 10) -> pd.DataFrame:
    """Cerca dataset nel catalogo nazionale; restituisce titolo, ente e URL delle risorse."""
    js = _get("https://www.dati.gov.it/opendata/api/3/action/package_search", params={"q": q, "rows": righe}).json()
    out = []
    for p in js["result"]["results"]:
        for res in p.get("resources", []):
            out.append({"dataset": p.get("title"), "ente": (p.get("organization") or {}).get("title"),
                        "formato": res.get("format"), "url": res.get("url")})
    return pd.DataFrame(out)


# --- File generici (CSV, XLSX, PDF) -----------------------------------------

def scarica(url: str, nome: str) -> Path:
    """Salva un file grezzo in dati/raw/ e restituisce il percorso."""
    RAW.mkdir(parents=True, exist_ok=True)
    dest = RAW / nome
    dest.write_bytes(_get(url).content)
    return dest


# --- Registro ---------------------------------------------------------------

def salva(df: pd.DataFrame, nome: str, fonte: str, url: str, nota: str = "", area: str = "00") -> Path:
    """Salva la serie e la registra con fonte e data. Sovrascrive la versione precedente.
    Ogni area ha il proprio registro (_registro_<area>.csv) per evitare scritture concorrenti."""
    SERIE.mkdir(parents=True, exist_ok=True)
    dest = SERIE / f"{nome}.csv"
    df.to_csv(dest, index=False)
    reg = SERIE / f"_registro_{area}.csv"
    righe = []
    if reg.exists():
        with reg.open(encoding="utf-8", newline="") as f:
            righe = [r for r in csv.DictReader(f) if r["nome"] != nome]
    righe.append({"nome": nome, "fonte": fonte, "url": url, "scaricato": date.today().isoformat(),
                  "aggiornato_fonte": df.attrs.get("aggiornato", ""), "nota": nota})
    with reg.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["nome", "fonte", "url", "scaricato", "aggiornato_fonte", "nota"])
        w.writeheader()
        w.writerows(righe)
    return dest
