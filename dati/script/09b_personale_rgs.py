"""Area 09 (PA): personale delle amministrazioni centrali, Conto annuale RGS 2010 e 2024.

Usato nella scheda 09-C12 (riesame delle funzioni con l'AI), paragrafo «Da dove si parte».
Esecuzione: python 09b_personale_rgs.py   (dalla cartella dati/script)

Fonte: Ragioneria generale dello Stato, Conto annuale, OpenBDAP, dataset
«Dipendenti Pubblici - Occupazione Complessiva - Dati analitici per Ente»
(spd_pca_occ_dip_ente_01_<anno>), licenza CC BY 3.0.

Conteggio: persone al 31 dicembre a tempo pieno e in part time (come il Conto annuale);
esclusi tempo determinato, formazione lavoro, interinali e LSU.
Perimetro: comparto «Funzioni centrali» di Ministeri, Agenzie, enti previdenziali e aziende
autonome, cioè il personale amministrativo contrattualizzato dello Stato. Restano fuori la scuola
(comparto Istruzione e ricerca) e il personale in regime di diritto pubblico (forze armate e di
polizia, magistrati, prefetti, diplomatici), a cui l'articolo 3 della 09-C12 non si applica.
Scrive dati/serie/09_personale_funzioni_centrali.csv.
"""
from __future__ import annotations

import csv
import io
import sys
from collections import defaultdict
from pathlib import Path

import requests

API = "https://bdap-opendata.rgs.mef.gov.it/SpodCkanApi/api/3/action/package_search?q=PCA_OCC_DIP_ENTE_001&rows=100"
ANNI = (2010, 2024)
TIPI = {"MINISTERI": "Ministeri", "AGENZIE": "Agenzie", "ENTI PREVIDENZIALI E ASSISTENZIALI": "Enti previdenziali",
        "AZIENDE AUTONOME": "Aziende autonome"}
CAMPI = ["Numero Dipendenti Donne Tempo Pieno", "Numero Dipendenti Uomini Tempo Pieno",
         "Numero Dipendenti Donne Part time Inf. 50%", "Numero Dipendenti Uomini Part time Inf. 50%",
         "Numero Dipendenti Donne Part time Sup. 50%", "Numero Dipendenti Uomini Part time Sup. 50%"]
USCITA = Path(__file__).resolve().parents[1] / "serie" / "09_personale_funzioni_centrali.csv"


def num(v: str) -> float:
    try:
        return float((v or "0").replace(",", "."))
    except ValueError:
        return 0.0


def scarica(anno: int) -> str:
    pacchetti = requests.get(API, timeout=60).json()["result"]["results"]
    meta = next(p for p in pacchetti if p["name"] == f"spd_pca_occ_dip_ente_01_{anno}")
    url = next(r["url"] for r in meta["resources"] if r.get("format", "").lower() == "csv" and "datastore/dump" in r["url"])
    url = url.replace("http://", "https://")
    r = requests.get(url, timeout=600)
    r.raise_for_status()
    return r.content.decode("utf-8-sig", errors="replace")


def main() -> int:
    righe = []
    for anno in ANNI:
        testo = scarica(anno)
        per_tipo, per_ente, totale = defaultdict(float), defaultdict(float), 0.0
        for x in csv.DictReader(io.StringIO(testo), delimiter=";"):
            n = sum(num(x.get(c)) for c in CAMPI)
            totale += n
            tipo = TIPI.get(x["Descrizione Tipo Istituzione"])
            if tipo and x["Descrizione Comparto"] == "FUNZIONI CENTRALI":
                per_tipo[tipo] += n
                per_ente[(tipo, x["Descrizione Ente"].strip())] += n
        righe.append(dict(anno=anno, livello="totale PA", gruppo="", ente="", personale=round(totale)))
        righe.append(dict(anno=anno, livello="funzioni centrali", gruppo="", ente="", personale=round(sum(per_tipo.values()))))
        for t, v in sorted(per_tipo.items()):
            righe.append(dict(anno=anno, livello="tipo", gruppo=t, ente="", personale=round(v)))
        for (t, e), v in sorted(per_ente.items(), key=lambda z: -z[1]):
            righe.append(dict(anno=anno, livello="ente", gruppo=t, ente=e, personale=round(v)))
        print(anno, "totale PA", round(totale), "funzioni centrali", round(sum(per_tipo.values())))
    USCITA.parent.mkdir(parents=True, exist_ok=True)
    with open(USCITA, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["anno", "livello", "gruppo", "ente", "personale"])
        w.writeheader()
        w.writerows(righe)
    print("scritto", USCITA)
    return 0


if __name__ == "__main__":
    sys.exit(main())
