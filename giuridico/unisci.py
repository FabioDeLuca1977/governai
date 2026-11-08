"""Unisce le verifiche dei tre esperti (fiscale, costituzionale, UE) in conformita.csv e quadro.md.

Esito complessivo di un elemento = il più restrittivo tra gli ambiti:
incompatibile > richiede_notifica > condizionato > compatibile.

Uso:  python unisci.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

QUI = Path(__file__).resolve().parent
ORDINE = {"compatibile": 0, "condizionato": 1, "richiede_notifica": 2, "incompatibile": 3}
AMBITI = {"FIS": "Diritto tributario", "COS": "Diritto costituzionale e amministrativo", "UE": "Diritto e governance UE"}


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    file = sorted(QUI.glob("conformita_*.csv"))
    if not file:
        print("nessuna verifica degli esperti trovata")
        return 0
    d = pd.concat([pd.read_csv(f, dtype=str).fillna("") for f in file], ignore_index=True)
    d["esito"] = d.esito.str.strip().str.lower()
    # identificativi delle varianti uniformi: "02-C1:PIENA" (alcuni esperti scrivono "02-C1_PIENA")
    var = d.tipo == "variante"
    d.loc[var, "id"] = d.loc[var, "id"].str.replace(r"^(\d\d-[PC]\d)[_ ]", r"\1:", regex=True).str.upper()
    ignoti = sorted(set(d.esito) - set(ORDINE))
    if ignoti:
        print(f"attenzione: esiti non riconosciuti trattati come 'condizionato': {ignoti}")
        d.loc[~d.esito.isin(ORDINE), "esito"] = "condizionato"
    d = d.sort_values(["tipo", "id", "ambito"])
    d.to_csv(QUI / "conformita.csv", index=False)

    quadro = ["# Quadro giuridico ed europeo di riferimento", "",
              "*Sintesi dei vincoli che ogni proposta e ogni analisi di GovernAI deve rispettare, redatta dagli esperti "
              "tributario, costituzionale e di diritto UE. È un supporto alla decisione, non un parere legale.*", ""]
    for sigla, nome in AMBITI.items():
        f = QUI / f"quadro_{sigla}.md"
        if f.exists():
            testo = f.read_text(encoding="utf-8").strip()
            righe = testo.splitlines()
            if righe and righe[0].startswith("# "):
                righe = righe[1:]
            quadro += [f"## {nome}", "", "\n".join(righe).strip(), ""]
    (QUI / "quadro.md").write_text("\n".join(quadro), encoding="utf-8")

    sintesi = d.groupby(["ambito", "esito"]).size().unstack(fill_value=0)
    print(sintesi.to_string())
    return 0


if __name__ == "__main__":
    sys.exit(main())
