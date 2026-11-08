"""Giurisprudenza della Corte costituzionale: verifica e ricerca sui dati aperti ufficiali della Corte.

Fonte: dati.cortecostituzionale.it, «Archivio delle pronunce» (JSON, licenza CC BY-SA 3.0, aggiornato ogni settimana).
Il sito www.cortecostituzionale.it blocca le richieste automatiche con un CAPTCHA (provato l'8/11/2026); i dati aperti
sono pubblicati dalla Corte stessa e contengono numero, anno, ECLI, date, epigrafe, testo e dispositivo di ogni pronuncia.

Uso:
    python giurisprudenza.py --scarica                   # scarica o aggiorna gli archivi in cache/ (circa 105 MB)
    python giurisprudenza.py --verifica 10/2015 275/2016  # estremi, ECLI, oggetto e dispositivo in breve
    python giurisprudenza.py --verifica-parametri        # verifica ogni sentenza citata in parametri.yaml
    python giurisprudenza.py --cerca "contributo straordinario" "extraprofitti" --dal 2023 --tipo S

Da Python:
    from giurisprudenza import pronuncia, cerca
    pronuncia(10, 2015)  -> dict | None
"""
from __future__ import annotations

import argparse
import html
import io
import json
import re
import sys
import zipfile
from functools import lru_cache
from pathlib import Path

QUI = Path(__file__).resolve().parent
CACHE = QUI / "cache"
VERIFICHE = QUI / "giurisprudenza_verificata.json"
BASE = "https://dati.cortecostituzionale.it/opendata/distribuzione/pronunce/"
ARCHIVI = {"P_json1956_1980.zip": (1956, 1980), "P_json1981_2000.zip": (1981, 2000), "P_json2001_oggi.zip": (2001, 2100)}
HEADERS = {"User-Agent": "GovernAI-costituzione/0.1 (prototipo open source di ricerca; verifica delle citazioni)"}
TIPI = {"S": "sentenza", "O": "ordinanza"}


def scarica(forza: bool = False) -> list[str]:
    import requests
    CACHE.mkdir(exist_ok=True)
    out = []
    for nome in ARCHIVI:
        dest = CACHE / nome
        if dest.exists() and not forza:
            out.append(f"{nome}: presente")
            continue
        r = requests.get(BASE + nome, headers=HEADERS, timeout=600)
        r.raise_for_status()
        dest.write_bytes(r.content)
        out.append(f"{nome}: {len(r.content) // 1_000_000} MB")
    _anno.cache_clear()
    return out


def _pulisci(s: str) -> str:
    s = html.unescape((s or "").replace("&#13;", " "))
    return re.sub(r"\s+", " ", s).strip()


@lru_cache(maxsize=None)
def _anno(anno: int) -> tuple[dict, ...]:
    for nome, (a, b) in ARCHIVI.items():
        if a <= anno <= b:
            p = CACHE / nome
            if not p.exists():
                raise SystemExit(f"Manca {p}: eseguire prima `python giurisprudenza.py --scarica`.")
            esterno = zipfile.ZipFile(p)
            interno_nome = next((n for n in esterno.namelist() if f"_{anno}_" in n), None)
            if not interno_nome:
                return ()
            interno = zipfile.ZipFile(io.BytesIO(esterno.read(interno_nome)))
            raw = interno.read(interno.namelist()[0])
            try:
                testo = raw.decode("utf-8")
            except UnicodeDecodeError:
                testo = raw.decode("cp1252", errors="replace")
            return tuple(json.loads(testo)["elenco_pronunce"])
    return ()


def _scheda(p: dict) -> dict:
    tipo = TIPI.get(p.get("tipologia_pronuncia", ""), p.get("tipologia_pronuncia", ""))
    epi = _pulisci(p.get("epigrafe", ""))
    epi = re.sub(r"^ha pronunciato la seguente\s*", "", epi)
    disp = _pulisci(p.get("dispositivo", ""))
    disp = re.sub(r"^(?:per questi motivi|PER QUESTI MOTIVI)\s*LA CORTE COSTITUZIONALE\s*", "", disp, flags=re.I)
    return {
        "tipo": tipo, "numero": int(p["numero_pronuncia"]), "anno": int(p["anno_pronuncia"]),
        "ecli": p.get("ecli", ""), "data_decisione": p.get("data_decisione", ""), "data_deposito": p.get("data_deposito", ""),
        "relatore": p.get("relatore_pronuncia", ""),
        "oggetto": epi[:600], "dispositivo": disp[:900],
        "url": f"https://www.cortecostituzionale.it/actionSchedaPronuncia.do?anno={p['anno_pronuncia']}&numero={p['numero_pronuncia']}",
    }


def pronuncia(numero: int, anno: int, completa: bool = False) -> dict | None:
    for p in _anno(int(anno)):
        if str(p.get("numero_pronuncia")) == str(int(numero)):
            s = _scheda(p)
            if completa:
                s["testo"] = _pulisci(p.get("testo", ""))
            return s
    return None


def cerca(*parole: str, dal: int = 2001, al: int = 2026, tipo: str | None = None, campo: str = "tutto", max_risultati: int = 40):
    """Pronunce che contengono TUTTE le parole (senza distinzione di maiuscole). campo: tutto | oggetto | dispositivo."""
    pats = [re.compile(re.escape(w), re.I) for w in parole]
    out = []
    for anno in range(dal, al + 1):
        for p in _anno(anno):
            if tipo and p.get("tipologia_pronuncia") != tipo:
                continue
            if campo == "oggetto":
                t = p.get("epigrafe", "")
            elif campo == "dispositivo":
                t = p.get("dispositivo", "")
            else:
                t = " ".join([p.get("epigrafe", ""), p.get("testo", ""), p.get("dispositivo", "")])
            if all(x.search(t) for x in pats):
                out.append(_scheda(p))
                if len(out) >= max_risultati:
                    return out
    return out


RE_SENT = re.compile(r"\b(\d{1,4})/((?:19|20)\d{2})\b")


def verifica_parametri() -> dict:
    """Verifica ogni pronuncia citata in parametri.yaml (campo giurisprudenza: 'numero/anno' + parole attese)."""
    import yaml
    par = yaml.safe_load((QUI / "parametri.yaml").read_text(encoding="utf-8"))
    esiti = {}
    for pid, p in par["parametri"].items():
        for g in p.get("giurisprudenza", []):
            rif = str(g.get("sentenza", ""))
            m = RE_SENT.search(rif)
            if not m:
                continue
            n, a = int(m[1]), int(m[2])
            chiave = f"{n}/{a}"
            s = pronuncia(n, a, completa=True)
            if not s:
                esiti[chiave] = {"esito": "non_trovata", "parametro": pid}
                continue
            attese = g.get("verifica_parole", [])
            corpo = " ".join([s["oggetto"], s["dispositivo"], s.get("testo", "")])
            mancanti = [w for w in attese if not re.search(re.escape(w), corpo, re.I)]
            tipo_atteso = g.get("tipo", "sentenza")
            esito = "verificata" if not mancanti and s["tipo"] == tipo_atteso else "da_controllare"
            prec = esiti.get(chiave, {})
            esiti[chiave] = {
                "esito": esito if prec.get("esito", "verificata") == "verificata" else prec["esito"],
                "parametri": sorted(set(prec.get("parametri", [])) | {pid}),
                "tipo": s["tipo"], "ecli": s["ecli"], "data_decisione": s["data_decisione"], "data_deposito": s["data_deposito"],
                "parole_attese": sorted(set(prec.get("parole_attese", [])) | set(attese)),
                "parole_mancanti": sorted(set(prec.get("parole_mancanti", [])) | set(mancanti)),
                "oggetto": s["oggetto"][:300], "dispositivo": s["dispositivo"][:300], "url": s["url"],
            }
    return esiti


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Verifica e ricerca nella giurisprudenza della Corte costituzionale (dati aperti)")
    ap.add_argument("--scarica", action="store_true")
    ap.add_argument("--forza", action="store_true", help="con --scarica: riscarica anche se presente")
    ap.add_argument("--verifica", nargs="*", metavar="N/AAAA")
    ap.add_argument("--verifica-parametri", action="store_true")
    ap.add_argument("--cerca", nargs="*")
    ap.add_argument("--dal", type=int, default=2001)
    ap.add_argument("--al", type=int, default=2026)
    ap.add_argument("--tipo", choices=["S", "O"])
    ap.add_argument("--campo", default="tutto", choices=["tutto", "oggetto", "dispositivo"])
    ap.add_argument("--max", type=int, default=40)
    a = ap.parse_args()
    if a.scarica:
        print("\n".join(scarica(a.forza)))
    if a.verifica:
        for rif in a.verifica:
            m = RE_SENT.search(rif)
            s = pronuncia(int(m[1]), int(m[2])) if m else None
            print(json.dumps(s, ensure_ascii=False, indent=1) if s else f"{rif}: NON TROVATA")
    if a.verifica_parametri:
        es = verifica_parametri()
        VERIFICHE.write_text(json.dumps(es, ensure_ascii=False, indent=1), encoding="utf-8")
        ok = sum(1 for e in es.values() if e["esito"] == "verificata")
        print(f"pronunce citate: {len(es)}; verificate: {ok}; da controllare: "
              f"{[k for k, e in es.items() if e['esito'] != 'verificata']}")
    if a.cerca:
        for s in cerca(*a.cerca, dal=a.dal, al=a.al, tipo=a.tipo, campo=a.campo, max_risultati=a.max):
            print(f"{s['tipo']} {s['numero']}/{s['anno']} (dep. {s['data_deposito']}): {s['oggetto'][:220]}")
            print(f"   -> {s['dispositivo'][:220]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
