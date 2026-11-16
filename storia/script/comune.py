"""Funzioni comuni per gli script delle serie storiche lunghe (storia/).

Ogni serie viene salvata in storia/serie/<nome>.csv in formato lungo:
    anno,paese,valore,unita,fonte
e registrata in storia/serie/_registro.csv.

Codici paese usati: IT, FR, DE, ES, EA (area euro, composizione attuale), UE27.
"""
from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path

import pandas as pd
import requests

BASE = Path(__file__).resolve().parent.parent          # storia/
SERIE = BASE / "serie"
CACHE = Path(__file__).resolve().parent / "_cache"
SERIE.mkdir(parents=True, exist_ok=True)
CACHE.mkdir(parents=True, exist_ok=True)

ANNO_INIZIO = 1970      # teniamo qualche anno prima del 1977 per i confronti
ANNO_FINE = 2026        # oltre il 2026 sono solo previsioni
PAESI = ["IT", "FR", "DE", "ES", "EA", "UE27"]

HEADERS: dict = {}  # user agent predefinito di requests (alcuni server rifiutano UA personalizzati)


def scarica(url: str, nome_cache: str, binario: bool = False, rinnova: bool = False,
            headers: dict | None = None, tentativi: int = 3):
    """Scarica un URL con cache locale in storia/script/_cache/."""
    f = CACHE / nome_cache
    if f.exists() and not rinnova:
        return f.read_bytes() if binario else f.read_text(encoding="utf-8")
    h = dict(HEADERS)
    if headers:
        h.update(headers)
    ultimo = None
    for i in range(tentativi):
        try:
            r = requests.get(url, headers=h, timeout=180)
            r.raise_for_status()
            f.write_bytes(r.content)
            return r.content if binario else r.content.decode("utf-8")
        except Exception as e:  # noqa: BLE001
            ultimo = e
            time.sleep(3 * (i + 1))
    raise RuntimeError(f"Download fallito: {url}: {ultimo}")


def eurostat(dataset: str, filtri: dict, nome_cache: str | None = None) -> pd.DataFrame:
    """Legge un dataset Eurostat (API JSON-stat 2.0) e restituisce un DataFrame lungo
    con una colonna per dimensione + 'valore'."""
    q = "&".join(f"{k}={v}" for k, vals in filtri.items()
                 for v in (vals if isinstance(vals, (list, tuple)) else [vals]))
    url = (f"https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/"
           f"{dataset}?format=JSON&lang=en&{q}")
    nome_cache = nome_cache or f"eurostat_{dataset}_{hashlib.md5(q.encode()).hexdigest()[:10]}.json"
    js = json.loads(scarica(url, nome_cache))
    ids = js["id"]
    size = js["size"]
    cats = []
    for d in ids:
        idx = js["dimension"][d]["category"]["index"]
        inv = sorted(idx.items(), key=lambda kv: kv[1])
        cats.append([k for k, _ in inv])
    righe = []
    for k, v in js["value"].items():
        k = int(k)
        pos = []
        for s in reversed(size):
            pos.append(k % s)
            k //= s
        pos = list(reversed(pos))
        rec = {d: cats[i][pos[i]] for i, d in enumerate(ids)}
        rec["valore"] = v
        righe.append(rec)
    return pd.DataFrame(righe)


GEO_EUROSTAT = {"IT": "IT", "FR": "FR", "DE": "DE", "ES": "ES", "EA20": "EA", "EA19": "EA",
                "EU27_2020": "UE27"}


def salva(nome: str, df: pd.DataFrame, descrizione: str, unita: str, fonte: str, url: str):
    """Salva la serie (colonne anno,paese,valore[,fonte]) e aggiorna il registro."""
    df = df.copy()
    df["anno"] = df["anno"].astype(int)
    df = df[(df["anno"] >= ANNO_INIZIO) & (df["anno"] <= ANNO_FINE)]
    df = df.dropna(subset=["valore"])
    dup = df.duplicated(["anno", "paese"])
    if dup.any():
        raise ValueError(f"{nome}: righe duplicate per anno/paese (manca un filtro?): {df[dup].head()}")
    df["valore"] = df["valore"].astype(float).round(3)
    df["unita"] = unita
    if "fonte" not in df.columns:
        df["fonte"] = fonte
    df = df[["anno", "paese", "valore", "unita", "fonte"]]
    ordine = {p: i for i, p in enumerate(PAESI + ["Nord", "Centro", "Centro-Nord", "Mezzogiorno"])}
    df = df.sort_values(["paese", "anno"], key=lambda s: s.map(ordine) if s.name == "paese" else s)
    df.to_csv(SERIE / f"{nome}.csv", index=False, encoding="utf-8")

    # anni disponibili per paese, es. "IT 1970-2026; FR 1978-2026"
    parti = []
    for p, g in df.groupby("paese", sort=False):
        parti.append(f"{p} {g.anno.min()}-{g.anno.max()}")
    reg_f = SERIE / "_registro.csv"
    reg = pd.read_csv(reg_f) if reg_f.exists() else pd.DataFrame(
        columns=["nome", "descrizione", "unita", "fonte", "url", "anni_disponibili"])
    reg = reg[reg.nome != nome]
    reg = pd.concat([reg, pd.DataFrame([{
        "nome": nome, "descrizione": descrizione, "unita": unita, "fonte": fonte,
        "url": url, "anni_disponibili": "; ".join(parti)}])], ignore_index=True)
    reg.sort_values("nome").to_csv(reg_f, index=False, encoding="utf-8")
    print(f"  salvata {nome}: {len(df)} righe ({'; '.join(parti)})")
