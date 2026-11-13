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
TESTI = DOCUMENTI + ["23_equita_e_linguaggio.md", "programma/schema.yaml", "sistema/esporta_web.py", "docs/app.js"]


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
               (r"(analisi politica|revisione) indipendente(?![^.\n]{0,120}\bAI\b)",
                "le revisioni sono di agenti AI: dirlo"),
               (r"\bda da\b", "refuso «da da»")]

    # 5. titoli delle proposte con virgolette sbilanciate (si propagano a scenari, documenti e sito)
    for r in pd.read_csv(RADICE / "motore" / "proposte.csv").itertuples():
        if str(r.titolo).count('"') % 2:
            errori.append(f"motore/proposte.csv: virgolette sbilanciate nel titolo di {r.proposta_id}")

    # 6. numero delle misure del nucleo robusto citato nei documenti
    esito = pd.read_csv(RADICE / "motore" / "esito_proposte.csv")
    n_nucleo = int((esito.classe == "robusta").sum())
    for doc in DOCUMENTI:
        t = leggi(doc)
        for m in re.finditer(r"nucleo robusto (\d+) su (\d+)|Sono le misure \(oggi (\d+)\)|Sono le (\d+) misure prioritarie", t):
            n = int(m.group(2) or m.group(3) or m.group(4))
            if n != n_nucleo:
                errori.append(f"{doc}:{t.count(chr(10), 0, m.start()) + 1}: nucleo robusto citato con {n} misure, il motore ne conta {n_nucleo}")
    # 7. ogni spesa dell'intermedio pagata con la coesione 2021-2027 deve dire che cosa succede dopo il 2029
    if m_dati := re.search(r"window\.GOVERNAI = (\{.*\});?\s*$", dati, re.S):
        x = {s["id"]: s for s in json.loads(m_dati.group(1).rstrip(";")).get("scenari", [])}.get("intermedio") or {}
        for voce in (x.get("dopo_2029") or {}).get("voci", []):
            if voce["esito"] == "da_decidere":
                errori.append(f"programma/coesione_dopo_2029.csv: manca {voce['id']} ({voce['mld']} mld di coesione nell'intermedio)")
    # 8. conteggi di varianti e coperture citati in README e nel documento di programma
    import glob
    n_var = int(pd.concat([pd.read_csv(f) for f in glob.glob(str(RADICE / "programma" / "varianti" / "*.csv"))])
                .drop_duplicates(["proposta_id", "variante"]).shape[0])
    n_cop = len(pd.read_csv(RADICE / "programma" / "coperture_menu.csv"))
    for doc in ["README.md", "20_programma_governai.md"]:
        t = leggi(doc)
        for m in re.finditer(r"(\d+) varianti\b[^|\n]{0,60}?(\d+) misure di copertura", t):
            if int(m.group(1)) != n_var or int(m.group(2)) != n_cop:
                errori.append(f"{doc}: {m.group(1)} varianti e {m.group(2)} coperture citate, nei file sono {n_var} e {n_cop}")
    # 9. punti numerati della sezione sulle scelte politiche del documento 20: nessun numero saltato
    nums = [int(x) for x in re.findall(r"^\*\*(\d+)\. ", leggi("20_programma_governai.md"), re.M)]
    if nums and nums != list(range(1, len(nums) + 1)):
        errori.append(f"20_programma_governai.md: punti numerati non consecutivi {nums}")
    # 10. dato di spesa dei fondi europei: un solo valore aggiornato nei documenti e nella scheda 09-C10
    for rel in DOCUMENTI + ["programma/schede/12_pa_produttiva.md"]:
        if "8,03%" in leggi(rel):
            errori.append(f"{rel}: dato superato sui pagamenti dei fondi europei (8,03% al 2025)")
    # 11. profili "Che cosa cambia per me": misure e coperture citate devono essere nel programma intermedio
    fp = RADICE / "programma" / "profili.yaml"
    if fp.exists():
        import yaml
        sel = pd.read_csv(RADICE / "programma" / "selezione_intermedio.csv")
        mis = set(sel[(sel.tipo == "variante") & (sel.scelta == 1)].proposta_id)
        for prof in (yaml.safe_load(fp.read_text(encoding="utf-8")) or {}).get("profili", []):
            for g in prof.get("guadagna", []):
                if g.get("proposta") not in mis:
                    errori.append(f"programma/profili.yaml: {prof['id']} cita {g.get('proposta')}, che non è nel programma intermedio")
            for c in prof.get("paga", []):
                if c.get("copertura") not in coperture:
                    errori.append(f"programma/profili.yaml: {prof['id']} cita {c.get('copertura')}, copertura non attiva nell'intermedio")
    rel_files = TESTI + ["revisioni/2026-11-08_analista_politico.md"]
    for rel in rel_files:
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
