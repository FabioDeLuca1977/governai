"""Sentinella di GovernAI: rileva gli aggiornamenti delle fonti ufficiali e scarica solo ciò che è cambiato.

Come rileva le novità:
  - Eurostat: indice ufficiale dei dataset ("last update of data"), una sola richiesta per tutti;
  - file ufficiali (PDF, XLSX): intestazioni HTTP ETag / Last-Modified / Content-Length;
  - pagine istituzionali osservate (sistema/config.yaml): nuovi link a documenti;
  - tutte le altre fonti (ISTAT SDMX, API varie): rilancio completo periodico degli script.
Poi rilancia gli script delle aree interessate, confronta l'impronta (hash) di ogni serie e
archivia le versioni cambiate in dati/storico/<serie>/<data>.csv.

Uso:  python sentinella.py [--completo] [--solo-controllo]
Scrive sistema/stato/fonti.json (memoria tra un'esecuzione e l'altra) e sistema/stato/ultima_sentinella.json.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import shutil
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path
from urllib.parse import urljoin

import requests
import yaml

RADICE = Path(__file__).resolve().parents[1]
DATI = RADICE / "dati"
SCRIPT = DATI / "script"
SERIE = DATI / "serie"
STORICO = DATI / "storico"
STATO = Path(__file__).resolve().parent / "stato"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; GovernAI-ricerca/0.1)"}
TOC_EUROSTAT = "https://ec.europa.eu/eurostat/api/dissemination/catalogue/toc/txt?lang=en"
RE_EUROSTAT = re.compile(r"/statistics/1\.0/data/([A-Za-z0-9_]+)")
RE_HREF = re.compile(r'href=["\']([^"\'#]+)["\']', re.I)
RE_DOC = re.compile(r"\.(?:pdf|xlsx?|zip|csv)(?:\?|$)", re.I)
# Nelle pagine che linkano pubblicazioni HTML (non PDF) si seguono i link con queste parole
PAROLE_PUBBLICAZIONE = r"pubblicazion|rapport|audizion|comunicat|relazion|nota-|document|bollettin|catalogo|statistic"


def leggi_json(p: Path, default):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def impronta(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def fonti_registrate() -> list[dict]:
    """Tutte le serie registrate dagli script, con area di appartenenza."""
    out = []
    for reg in SERIE.glob("_registro_*.csv"):
        area = reg.stem.removeprefix("_registro_")
        with reg.open(encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                out.append({**r, "area": area})
    return out


def script_area(area: str) -> Path | None:
    cand = sorted(SCRIPT.glob(f"{area}_*.py"))
    return cand[0] if cand else None


# --- Rilevamento ------------------------------------------------------------

def controlla_eurostat(codici: set[str], stato: dict) -> tuple[set[str], dict]:
    r = requests.get(TOC_EUROSTAT, headers=HEADERS, timeout=180)
    r.raise_for_status()
    ultimi = {}
    for riga in csv.reader(io.StringIO(r.text), delimiter="\t"):
        if len(riga) > 3 and riga[1].strip() in codici:
            ultimi[riga[1].strip()] = riga[3].strip()
    precedenti = stato.get("eurostat", {})
    cambiati = {c for c, v in ultimi.items() if c in precedenti and precedenti[c] != v}
    nuovi = {c for c in ultimi if c not in precedenti}
    return cambiati | nuovi, ultimi


def controlla_file(urls: set[str], stato: dict) -> tuple[set[str], dict]:
    prec = stato.get("file", {})
    firme, cambiati = {}, set()
    for u in sorted(urls):
        try:
            h = requests.head(u, headers=HEADERS, timeout=30, allow_redirects=True)
            firma = "|".join(h.headers.get(k, "") for k in ("ETag", "Last-Modified", "Content-Length"))
        except requests.RequestException:
            firma = ""
        if not firma.strip("|"):
            firme[u] = prec.get(u, "")  # il server non dà indicazioni: si affida al rilancio periodico
            continue
        firme[u] = firma
        if prec.get(u) and prec[u] != firma:
            cambiati.add(u)
    return cambiati, firme


def controlla_pagine(pagine: list[dict], stato: dict) -> tuple[list[dict], dict, list[str]]:
    prec = stato.get("pagine", {})
    link_ora, nuovi, errori = {}, [], []
    for p in pagine:
        try:
            r = requests.get(p["url"], headers=HEADERS, timeout=60)
            r.raise_for_status()
        except requests.RequestException as e:
            errori.append(f"{p['nome']}: {e.__class__.__name__}")
            link_ora[p["url"]] = prec.get(p["url"], [])
            continue
        filtro = re.compile(p.get("pattern", PAROLE_PUBBLICAZIONE), re.I)
        link = sorted({urljoin(p["url"], h) for h in RE_HREF.findall(r.text)
                       if RE_DOC.search(h) or filtro.search(h)})
        link_ora[p["url"]] = link
        if p["url"] in prec:
            for l in sorted(set(link) - set(prec[p["url"]])):
                nuovi.append({"pagina": p["nome"], "aree": p.get("aree", []), "documento": l})
    return nuovi, link_ora, errori


# --- Aggiornamento ----------------------------------------------------------

def rilancia(script: Path) -> tuple[bool, str]:
    try:
        r = subprocess.run([sys.executable, script.name], cwd=SCRIPT, capture_output=True,
                           text=True, encoding="utf-8", errors="replace", timeout=900)
        ok = r.returncode == 0
        coda = (r.stdout if ok else r.stderr).strip().splitlines()[-1:] or [""]
        return ok, coda[0][:200]
    except subprocess.TimeoutExpired:
        return False, "timeout"


def archivia_cambiate(stato: dict, oggi: str) -> list[str]:
    prec = stato.get("serie", {})
    nuove, cambiate = {}, []
    for f in sorted(SERIE.glob("*.csv")):
        if f.name.startswith("_"):
            continue
        h = impronta(f)
        nuove[f.stem] = h
        if prec.get(f.stem) != h:
            cambiate.append(f.stem)
            dest = STORICO / f.stem
            dest.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dest / f"{oggi}.csv")
    stato["serie"] = nuove
    return cambiate if prec else []  # alla prima esecuzione si crea solo la base


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--completo", action="store_true", help="rilancia tutti gli script")
    ap.add_argument("--solo-controllo", action="store_true", help="rileva senza scaricare")
    a = ap.parse_args()
    STATO.mkdir(parents=True, exist_ok=True)
    conf = yaml.safe_load((Path(__file__).parent / "config.yaml").read_text(encoding="utf-8"))
    stato = leggi_json(STATO / "fonti.json", {})
    oggi = date.today().isoformat()
    prima_volta = not stato

    fonti = fonti_registrate()
    per_codice: dict[str, set[str]] = {}
    file_url: dict[str, set[str]] = {}
    for f in fonti:
        for url in re.split(r"\s*;\s*|\s+", f.get("url", "") or ""):  # alcuni registri elencano più URL
            m = RE_EUROSTAT.search(url)
            if m:
                per_codice.setdefault(m.group(1), set()).add(f["area"])
            elif re.search(r"\.(pdf|xlsx?|zip|csv)(\?|$)", url, re.I):
                file_url.setdefault(url, set()).add(f["area"])

    esito = {"data": datetime.now().isoformat(timespec="seconds"), "prima_esecuzione": prima_volta,
             "eurostat_aggiornati": [], "file_aggiornati": [], "documenti_nuovi": [], "errori": [],
             "script": {}, "serie_cambiate": []}
    aree = set()

    try:
        cambiati, ultimi = controlla_eurostat(set(per_codice), stato)
        stato["eurostat"] = ultimi
        esito["eurostat_aggiornati"] = sorted(c for c in cambiati if not prima_volta)
        for c in esito["eurostat_aggiornati"]:
            aree |= per_codice[c]
    except requests.RequestException as e:
        esito["errori"].append(f"indice Eurostat: {e.__class__.__name__}")

    cambiati, firme = controlla_file(set(file_url), stato)
    stato["file"] = firme
    esito["file_aggiornati"] = sorted(cambiati)
    for u in cambiati:
        aree |= file_url[u]

    nuovi, link, errori = controlla_pagine(conf.get("pagine", []), stato)
    stato["pagine"] = link
    esito["documenti_nuovi"] = nuovi
    esito["errori"] += errori

    ultimo_completo = stato.get("ultimo_completo")
    giorni = conf.get("parametri", {}).get("rieseguire_tutto_ogni_giorni", 7)
    scaduto = not ultimo_completo or (date.today() - date.fromisoformat(ultimo_completo)).days >= giorni
    completo = a.completo or scaduto
    if completo:
        da_lanciare = sorted(p for p in SCRIPT.glob("*.py") if p.name != "fonti.py")
    else:
        da_lanciare = sorted({s for s in (script_area(x) for x in aree) if s})
    esito["modalita"] = "completo" if completo else ("mirato" if da_lanciare else "nessun aggiornamento")

    if not a.solo_controllo:
        for s in da_lanciare:
            ok, msg = rilancia(s)
            esito["script"][s.name] = "ok" if ok else f"ERRORE: {msg}"
        if completo:
            stato["ultimo_completo"] = date.today().isoformat()
        esito["serie_cambiate"] = archivia_cambiate(stato, oggi)

    (STATO / "fonti.json").write_text(json.dumps(stato, ensure_ascii=False, indent=1), encoding="utf-8")
    (STATO / "ultima_sentinella.json").write_text(json.dumps(esito, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"sentinella: {esito['modalita']}; Eurostat aggiornati {len(esito['eurostat_aggiornati'])}, "
          f"file {len(esito['file_aggiornati'])}, documenti nuovi {len(nuovi)}, serie cambiate {len(esito['serie_cambiate'])}, "
          f"errori {len(esito['errori'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
