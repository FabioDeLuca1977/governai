# GovernAI — Base dati

Base di conoscenza dei dati pubblici usati dagli agenti ministeriali. Ogni cifra dei dossier deve poter essere ricondotta a una serie di questa cartella oppure a un documento ufficiale citato in `verifiche/`.

## Struttura

| Cartella | Contenuto |
|---|---|
| `script/fonti.py` | Libreria comune: Eurostat, ISTAT (SDMX), dati.gov.it, download di file, registro |
| `script/00_macro.py` | Serie macro di base: debito, deficit, PIL, interessi, popolazione |
| `script/NN_area.py` | Script di download di ciascuna area ministeriale |
| `serie/` | Serie scaricate in CSV. I file `_registro_NN.csv` riportano fonte, URL e data di download |
| `raw/` | File grezzi (PDF, XLSX) da fonti ufficiali |
| `verifiche/` | Per ogni area, la tabella che confronta il valore nel dossier con quello verificato |

## Aggiornare i dati

Dalla cartella `dati/script`:

```bash
python 00_macro.py
```

Poi rilanciare gli script di area (`python 01_economia.py`, ecc.). Gli script sovrascrivono le serie e aggiornano la data nel registro.

## Fonti accessibili senza registrazione

| Fonte | Accesso | Note |
|---|---|---|
| Eurostat | API JSON-stat | Veloce; ripubblica molti dati ISTAT. Prima scelta |
| ISTAT | SDMX REST (esploradati.istat.it) | Lento: l'elenco dei flussi è in cache in `serie/_istat_flussi.csv` |
| Banca d'Italia | Base dati statistica (infostat) | |
| MEF-RGS | OpenBDAP | Bilancio dello Stato |
| dati.gov.it | API CKAN | Catalogo nazionale dei dati aperti |
| UPB, Corte dei conti, DPFP, Rapporto spese fiscali | PDF | Le tabelle vanno estratte dal documento |

## Limiti

- **Microdati** (EU-SILC/IT-SILC, INPS individuali, Agenzia delle Entrate): richiedono un accesso istituzionale. Senza di questi non si possono fare microsimulazioni distributive, cioè calcolare con precisione chi guadagna e chi perde.
- **Ritardo dei dati**: molti dati arrivano con 1–2 anni di ritardo. Va sempre indicato l'anno di riferimento.
- **Stime di costo**: le stime delle proposte sono etichettate "stima GovernAI". Non sono quantificazioni ufficiali della Ragioneria.
