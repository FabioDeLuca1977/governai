"""Allinea la copia locale a GitHub prima della pipeline locale, così i due aggiornamenti convivono.

GitHub (Action quotidiana) è la copia di riferimento. La pipeline locale rigenera ogni giorno gli
stessi file di output: prima di scaricare le novità da GitHub, questo script mette da parte (git stash)
gli output locali del giorno prima, così non vanno in conflitto e restano comunque recuperabili.
Si conservano gli ultimi 7 accantonamenti. Le modifiche ai file sorgente non vengono toccate:
`git pull --autostash` le rimette al loro posto dopo l'aggiornamento.

Uso:  python sincronizza.py   (lo chiama avvia_pipeline.cmd)
"""
from __future__ import annotations

import subprocess
import sys
from datetime import date
from pathlib import Path

RADICE = Path(__file__).resolve().parents[1]
# File generati dalla pipeline: sono gli stessi che l'Action salva su GitHub
GENERATI = ["dati/serie", "dati/storico", "sistema/stato", "sistema/bollettini", "docs/data.js",
            "registro/bilancio.md", "motore/esito.md", "motore/esito_proposte.csv", "programma"]
ETICHETTA = "governai-locale"
CONSERVA = 7


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=RADICE, capture_output=True, text=True, encoding="utf-8", errors="replace")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    if git("rev-parse", "--is-inside-work-tree").returncode != 0 or not git("remote").stdout.strip():
        print("sincronizza: nessun repository git con remote, salto")
        return 0
    esistenti = [p for p in GENERATI if (RADICE / p).exists()]
    if git("status", "--porcelain", "--", *esistenti).stdout.strip():
        r = git("stash", "push", "--include-untracked", "-m", f"{ETICHETTA} {date.today()}", "--", *esistenti)
        print(f"sincronizza: output locali accantonati ({r.stdout.strip() or r.stderr.strip()})")
    r = git("pull", "--rebase", "--autostash", "origin", "main")
    if r.returncode != 0:
        print(f"sincronizza: aggiornamento da GitHub non riuscito, la pipeline usa la copia locale ({r.stderr.strip()[:200]})")
        git("rebase", "--abort")
        return 0
    print("sincronizza: copia locale allineata a GitHub")
    # tiene solo gli ultimi accantonamenti della pipeline (gli output si rigenerano comunque)
    nostri = [riga.split(":", 1)[0] for riga in git("stash", "list").stdout.splitlines() if ETICHETTA in riga]
    for ref in reversed(nostri[CONSERVA:]):
        git("stash", "drop", ref)
    return 0


if __name__ == "__main__":
    sys.exit(main())
