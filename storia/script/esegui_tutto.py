"""Ricostruisce tutte le serie di storia/serie/ e le analisi, nell'ordine giusto.

Uso:  python storia/script/esegui_tutto.py          (usa i file gia' scaricati in _cache/)
      python storia/script/esegui_tutto.py --nuovo  (svuota la cache e riscarica tutto)

Richiede: Python 3.10+, requests, pandas, numpy. Connessione a internet al primo avvio.
Nota: l'API OCSE limita le richieste (circa 20 l'ora): se compare un errore 403,
riprovare dopo un'ora; i file gia' scaricati restano in cache.
"""
import shutil
import sys

import analisi
import scarica_ameco_fmi_ocse
import scarica_eurostat
import scarica_istat_gini
import scarica_ocse_bm
from comune import CACHE

if "--nuovo" in sys.argv:
    for f in CACHE.iterdir():
        if f.name != ".gitignore":
            f.unlink() if f.is_file() else shutil.rmtree(f)

for nome, mod in [("AMECO, FMI, OCSE (finanza pubblica e macro)", scarica_ameco_fmi_ocse),
                  ("Eurostat", scarica_eurostat),
                  ("OCSE lavoro e Banca Mondiale", scarica_ocse_bm),
                  ("ISTAT e Gini OCSE", scarica_istat_gini),
                  ("Analisi", analisi)]:
    print(f"== {nome}")
    mod.main()
