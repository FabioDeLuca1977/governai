"""Registro di integrità di GovernAI: una catena di impronte crittografiche, come in una blockchain.

Ogni esecuzione (aggiornamento quotidiano, analisi su richiesta, decisione registrata) aggiunge un anello a
integrita/catena.jsonl con:
  - l'impronta SHA-256 di ogni file che ha determinato il risultato: Carta dei valori, regole, punteggi del panel,
    fondi, varianti, coperture, dati;
  - l'impronta dei risultati: programma scelto, bollettino, analisi;
  - l'impronta dell'anello precedente.
Cambiare di nascosto un dato, una regola o un risultato passato rompe la catena: `python catena.py --verifica`
lo rileva e dice dove. La catena vive nel repository git, che è a sua volta una catena di hash: ogni modifica
resta nella storia con autore e data.

Questo NON rende l'AI incorruttibile: rende ogni manipolazione visibile e attribuibile.

Uso:
  python catena.py --aggiungi aggiornamento [--nota "..."]
  python catena.py --verifica
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

QUI = Path(__file__).resolve().parent
RADICE = QUI.parent
CATENA = QUI / "catena.jsonl"
GENESI = "0" * 64

# Cosa determina le scelte (regole e input) e cosa ne risulta (output)
REGOLE = ["01_carta_valori.md", "00_metodo.md", "motore/rubrica.md", "sistema/config.yaml",
          "motore/decidi.py", "programma/ottimizza.py", "registro/controlla.py", "sistema/revisione_ai.py",
          "sistema/analizza_richiesta.py", "apprendimento/valuta.py"]
INPUT = ["motore/punteggi_*.csv", "motore/proposte.csv", "registro/fondi.csv", "programma/varianti/*.csv",
         "programma/coperture_menu.csv", "giuridico/conformita.csv", "apprendimento/obiettivi.yaml", "apprendimento/decisioni.csv",
         "dati/serie/*.csv"]
OUTPUT = ["programma/selezione_*.csv", "motore/esito_proposte.csv", "sistema/bollettini/ultimo.md",
          "apprendimento/esiti.csv", "apprendimento/calibrazione.csv", "analisi/*.json"]


def impronta_file(p: Path) -> str:
    # fine riga normalizzati: Windows e GitHub Actions devono produrre la stessa impronta
    return hashlib.sha256(p.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def impronte(schemi: list[str]) -> dict[str, str]:
    out = {}
    for s in schemi:
        for p in sorted(RADICE.glob(s)):
            if p.is_file():
                out[p.relative_to(RADICE).as_posix()] = impronta_file(p)
    return out


def radice(d: dict[str, str]) -> str:
    """Un'unica impronta per un insieme di file (ordinati per nome)."""
    return hashlib.sha256("\n".join(f"{k}:{v}" for k, v in sorted(d.items())).encode()).hexdigest()


def hash_anello(a: dict) -> str:
    corpo = {k: v for k, v in a.items() if k != "hash"}
    return hashlib.sha256(json.dumps(corpo, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def leggi_catena() -> list[dict]:
    if not CATENA.exists():
        return []
    return [json.loads(r) for r in CATENA.read_text(encoding="utf-8").splitlines() if r.strip()]


def aggiungi(evento: str, nota: str = "") -> dict:
    catena = leggi_catena()
    regole, ingressi, uscite = impronte(REGOLE), impronte(INPUT), impronte(OUTPUT)
    prec = catena[-1] if catena else None
    a = {
        "n": len(catena),
        "data": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "evento": evento,
        "nota": nota,
        "precedente": prec["hash"] if prec else GENESI,
        "radice_regole": radice(regole),
        "radice_input": radice(ingressi),
        "radice_output": radice(uscite),
        # dettaglio per file solo di regole e output (i dati sono molti: basta la radice, ricalcolabile da git)
        "regole": regole,
        "output": uscite,
        "regole_cambiate": sorted(k for k in regole if not prec or prec.get("regole", {}).get(k) != regole[k]),
    }
    a["hash"] = hash_anello(a)
    with CATENA.open("a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(a, ensure_ascii=False, sort_keys=True) + "\n")
    return a


def verifica() -> list[str]:
    errori, prec = [], GENESI
    for i, a in enumerate(leggi_catena()):
        if a.get("n") != i:
            errori.append(f"anello {i}: numerazione alterata")
        if a.get("precedente") != prec:
            errori.append(f"anello {i}: non punta all'anello precedente (catena spezzata)")
        if hash_anello(a) != a.get("hash"):
            errori.append(f"anello {i}: contenuto modificato dopo la registrazione")
        prec = a.get("hash")
    return errori


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--aggiungi", metavar="EVENTO")
    ap.add_argument("--nota", default="")
    ap.add_argument("--verifica", action="store_true")
    a = ap.parse_args()
    if a.verifica or not a.aggiungi:
        err = verifica()
        n = len(leggi_catena())
        print(f"catena di integrità: {n} anelli, " + ("integra" if not err else f"{len(err)} PROBLEMI"))
        for e in err:
            print(" -", e)
        if a.verifica:
            return 1 if err else 0
    if a.aggiungi:
        err = verifica()
        if err:
            print("catena non integra: nessun anello aggiunto finché non si chiarisce la manomissione")
            return 1
        x = aggiungi(a.aggiungi, a.nota)
        cambi = f"; regole cambiate: {', '.join(x['regole_cambiate'])}" if x["n"] and x["regole_cambiate"] else ""
        print(f"anello {x['n']} aggiunto ({x['evento']}) {x['hash'][:12]}{cambi}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
