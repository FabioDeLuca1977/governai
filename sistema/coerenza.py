"""Controllo automatico di coerenza tra documenti, scenari e sito.

Per un progetto che chiede di essere verificato, ogni incoerenza tra due pagine costa credibilità.
Questo controllo confronta i numeri e le frasi che più spesso si disallineano:

1. il programma intermedio (versione di riferimento): spesa e numero di misure nei documenti 20, 21 e 22
   e nei dati del sito devono coincidere con `programma/selezione_intermedio.csv`;
2. frasi vietate perché smentite dai dati, per esempio "nessun contributo sulle pensioni" se una copertura
   sulle pensioni è attiva, o "senza nuove tasse" (la formula corretta è "senza tasse in più oltre quelle già previste");
3. le revisioni scritte da agenti AI non vanno presentate come revisioni di persone;
4. refusi ricorrenti nei testi generati.

Uso:  python coerenza.py        (codice di uscita 1 se trova problemi)
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pandas as pd

QUI = Path(__file__).resolve().parent
RADICE = QUI.parent
DOCUMENTI = ["20_programma_governai.md", "21_idee_in_sintesi.md", "22_programma_in_una_pagina.md"]
TESTI = DOCUMENTI + ["programma/schema.yaml", "sistema/esporta_web.py", "docs/app.js"]


def leggi(rel: str) -> str:
    p = RADICE / rel
    return p.read_text(encoding="utf-8") if p.exists() else ""


def intermedio() -> tuple[float, int, set[str]]:
    s = pd.read_csv(RADICE / "programma" / "selezione_intermedio.csv")
    v = s[(s.tipo == "variante") & (s.scelta == 1)]
    c = s[(s.tipo == "copertura") & (s.scelta == 1)]
    return round(float(v.costo_regime.sum()), 2), int(v.proposta_id.nunique()), set(c.chiave)


def numero(t: str) -> float:
    return float(t.replace(".", "").replace(",", "."))


def controlla() -> list[str]:
    errori = []
    spesa, misure, coperture = intermedio()

    # 1. totali del programma di riferimento
    for doc in DOCUMENTI:
        for m in re.finditer(r"Programma intermedio: ([\d.,]+) mld l'anno\*\*, (\d+) misure", leggi(doc)):
            if abs(numero(m.group(1)) - spesa) > 0.005 or int(m.group(2)) != misure:
                errori.append(f"{doc}: programma intermedio {m.group(1)} mld e {m.group(2)} misure, "
                              f"ma la selezione dice {spesa} mld e {misure} misure")
    dati = leggi("docs/data.js")
    m = re.search(r"window\.GOVERNAI = (\{.*\});?\s*$", dati, re.S)
    if m:
        sc = {x["id"]: x for x in json.loads(m.group(1).rstrip(";")).get("scenari", [])}
        x = sc.get("intermedio")
        if x and (abs(x["spesa"] - spesa) > 0.005 or len(x["misure"]) != misure):
            errori.append(f"docs/data.js: intermedio {x['spesa']} mld e {len(x['misure'])} misure, "
                          f"selezione {spesa} e {misure}: rigenerare il sito (esporta_web.py)")
        if x and x.get("deficit", 0) > 0:
            errori.append(f"docs/data.js: l'intermedio ha {x['deficit']} mld di deficit")
    else:
        errori.append("docs/data.js: dati del sito non leggibili")

    # 2-4. frasi smentite dai dati, revisioni AI presentate come umane, refusi
    regole = [(r"senza nuove tasse", "usare «senza tasse in più oltre quelle già previste»: il programma contiene già accise, forfettario e pensioni")]
    if any(k.startswith("PE") for k in coperture):
        regole.append((r"nessun contributo sulle pensioni",
                       "una copertura sulle pensioni (PE) è attiva: scrivere «nessun contributo straordinario sulle pensioni»"))
    regole += [(r"revision[ei][^.\n]{0,160}in modo indipendente(?![^.\n]{0,160}\bAI\b)",
                "le revisioni sono di agenti AI: dirlo"),
               (r"\bda da\b", "refuso «da da»"),
               (r"Staffetta delle competenze\": ", "virgolette sbilanciate nel titolo di 09-C8")]
    for rel in TESTI:
        t = leggi(rel)
        for pat, msg in regole:
            for m in re.finditer(pat, t, re.I):
                riga = t.count("\n", 0, m.start()) + 1
                if rel == "sistema/esporta_web.py" and "help=" in t.splitlines()[riga - 1]:
                    continue
                errori.append(f"{rel}:{riga}: {msg}")
    return errori


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    errori = controlla()
    if not errori:
        print("coerenza: nessun problema tra documenti, scenari e sito")
        return 0
    print(f"coerenza: {len(errori)} problemi")
    for e in errori:
        print(" -", e)
    return 1


if __name__ == "__main__":
    sys.exit(main())
