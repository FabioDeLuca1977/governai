# Bollettino GovernAI — 2026-11-11

*Generato automaticamente da `sistema/pipeline.py` alle 13:56. Fonti: Eurostat, ISTAT, MEF/RGS, Banca d'Italia e documenti ufficiali osservati.*

## 1. Cosa è cambiato nelle fonti

- Modalità di aggiornamento: **mirato**
- Dataset Eurostat aggiornati: sts_inpr_m
- File ufficiali aggiornati: 0
- Serie cambiate e archiviate in `dati/storico/`: 00c_produzione_industriale
- Documenti nuovi sulle pagine osservate: 8
  - MEF - Documenti di finanza pubblica: https://www.rgs.mef.gov.it/_Documenti/VERSIONE-I/Attivit--i/Contabilit_e_finanza_pubblica/DPB/2027/DPB-2027.pdf
  - ISTAT - Home e comunicati: https://www.istat.it/comunicato-stampa/nota-sullandamento-e-prospettive-delleconomia-italiana-anni-2026-2027-aggiornamento-novembre/
  - ISTAT - Home e comunicati: https://www.istat.it/comunicato-stampa/produzione-industriale-settembre-2026/
  - ISTAT - Home e comunicati: https://www.istat.it/documenti/tavole-di-dati/
  - Corte dei conti: https://www.corteconti.it/HOME/Documenti/DettaglioDocumenti?Id=315f7dd2-2978-48a5-98d1-92e787d0d903
  - Corte dei conti: https://www.corteconti.it/HOME/StampaMedia/ComunicatiStampa/DettaglioComunicati?Id=86fafcd2-c3ef-4cf3-9df8-e64b8a6e846b
  - Gazzetta Ufficiale: http://www.gazzettaufficiale.it/eli/id/2026/11/10/26E06207/s4
  - Gazzetta Ufficiale: http://www.gazzettaufficiale.it/eli/id/2026/11/10/26G00219/sg

## 2. Cruscotto

| | Indicatore | Periodo | Valore | Var. | Var. 12 periodi |
|---|---|---|---|---|---|
| 🔴 | Inflazione (HICP, % annua) | 2026-10 *(provv.)* | 5,60 % | +1,40 | +4,30 |
| 🔴 | Disoccupazione (%) | 2026-09 | 6,30 % | +0,10 | +0,40 |
| 🟢 | Disoccupazione under 25 (%) | 2026-09 | 19,90 % | -0,40 | -0,60 |
| 🔴 | Rendimento titoli decennali IT (%) | 2026-09 | 4,36 % | +0,38 | +0,80 |
| 🔴 | Spread IT-DE (punti base) | 2026-09 | 88,90 pb | +8,80 | +1,90 |
| 🔴 | PIL reale (% sul trimestre prec.) | 2026-Q3 | 0,00 % | -0,20 | -0,20 |
| 🔴 | Debito pubblico (% PIL, trimestrale) | 2026-Q2 *(provv.)* | 139,90 % PIL | +1,30 | +2,30 |
| 🟢 | Produzione industriale (2021=100) | 2026-09 | 94,10 indice | +1,10 | -0,10 |
| 🔴 | Fiducia dei consumatori (saldo) | 2026-10 | -23,30 saldo | -0,10 | -7,80 |
| 🔴 | Debito pubblico (% PIL, annuo) | 2025 | 136,70 % PIL | +2,40 | — |
| 🟢 | Saldo di bilancio (% PIL) | 2025 | -3,10 % PIL | +0,30 | — |
| 🟢 | Spesa per interessi (% PIL) | 2025 | 3,80 % PIL | -0,10 | — |
| 🟢 | NEET 15-29 (%) | 2025 | 13,30 % | -1,90 | — |
| 🔴 | Fecondità (figli per donna) | 2024 | 1,18  | -0,03 | — |

🟢 = variazione favorevole, 🔴 = sfavorevole rispetto all'osservazione precedente.

## 3. Allerte attive

- **inflazione_alta**: Inflazione sopra il 3%: i redditi reali scendono e i costi delle misure in euro nominali salgono. (valore 5,60 %, 2026-10)
  - Azione: Rivalutare le varianti a sostegno dei redditi (salario minimo, inclusione, casa, trasporti) e indicizzare i costi del programma.
  - Priorità: 02-C1, 02-C4, 04-P2, 04-P3; sospese: —
- **inflazione_in_salita**: Inflazione in forte aumento sull'anno precedente. (valore 5,60 %, 2026-10)
  - Azione: Verificare l'origine (energia, alimentari) e le misure su prezzo dell'energia.
  - Priorità: 02-C1, 03-P2, 01-P5; sospese: —
- **debito_in_salita**: Debito/PIL in aumento di oltre 1 punto in un trimestre. (valore 139,90 % PIL, 2026-Q2)
  - Azione: Applicare la regola FUT: nessuna variante finanziata a debito; rivedere la traiettoria della Difesa.
  - Priorità: —; sospese: 07-C5
- **fiducia_in_calo**: Fiducia dei consumatori in netto calo sull'anno. (valore -23,30 saldo, 2026-10)
  - Azione: Segnale di rischio per i consumi; valutare la tempistica delle coperture che pesano sui consumatori (IVA, accise).
  - Priorità: —; sospese: —

## 4. Programma del momento

Il programma di riferimento (tutte le coperture, nucleo robusto prima) costa **13,52 mld/anno**; il programma adattato al momento costa **13,49 mld/anno**. Entrambi sono finanziati senza deficit.

**Differenze rispetto al riferimento** (effetto delle allerte):

- 01-P14: PILOTA → ESSENZIALE
- 01-P5: ESSENZIALE → PIENA
- 02-C1: ZERO → PIENA
- 03-P5: ESSENZIALE → PILOTA
- 04-P8: PIENA → ZERO
- 05-C10: PILOTA → esclusa
- 07-C2: PIENA → ESSENZIALE
- 08-P6: PILOTA → esclusa

**Cambiamenti rispetto al bollettino precedente:**

- 01-P13: esclusa → ZERO
- 01-P14: esclusa → ESSENZIALE
- 01-P15: esclusa → PIENA
- 02-C6: PIENA → ZERO
- 02-C7: esclusa → PIENA
- 03-P3: esclusa → ESSENZIALE
- 03-P5: PIENA → PILOTA
- 04-P2: ESSENZIALE → esclusa
- 04-P7: esclusa → PILOTA
- 04-P8: esclusa → ZERO
- 04-P9: esclusa → PIENA
- 05-C7: esclusa → ESSENZIALE
- 05-C8: esclusa → PIENA
- 05-C9: esclusa → PIENA
- 06-C3: esclusa → ESSENZIALE
- 06-C8: esclusa → PIENA
- 06-C9: esclusa → PIENA
- 07-C1: PIENA → ESSENZIALE
- 07-C2: PIENA → ESSENZIALE
- 07-C3: PIENA → ESSENZIALE
- 08-P6: PILOTA → esclusa
- 09-C2: PIENA → ESSENZIALE
- 09-C3: PIENA → ESSENZIALE
- 09-C9: esclusa → PIENA

Dettaglio: `programma/selezione_momento.md`.

## 5. Revisione AI richiesta

**8 compiti** per il livello AI (`sistema/stato/revisione_ai.json`):
- [documento_nuovo] MEF - Documenti di finanza pubblica: https://www.rgs.mef.gov.it/_Documenti/VERSIONE-I/Attivit--i/Contabilit_e_finanza_pubblica/DPB/2027/DPB-2027.pdf → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] ISTAT - Home e comunicati: https://www.istat.it/comunicato-stampa/nota-sullandamento-e-prospettive-delleconomia-italiana-anni-2026-2027-aggiornamento-novembre/ → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] ISTAT - Home e comunicati: https://www.istat.it/comunicato-stampa/produzione-industriale-settembre-2026/ → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] ISTAT - Home e comunicati: https://www.istat.it/documenti/tavole-di-dati/ → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] Corte dei conti: https://www.corteconti.it/HOME/Documenti/DettaglioDocumenti?Id=315f7dd2-2978-48a5-98d1-92e787d0d903 → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] Corte dei conti: https://www.corteconti.it/HOME/StampaMedia/ComunicatiStampa/DettaglioComunicati?Id=86fafcd2-c3ef-4cf3-9df8-e64b8a6e846b → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] Gazzetta Ufficiale: http://www.gazzettaufficiale.it/eli/id/2026/11/10/26E06207/s4 → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] Gazzetta Ufficiale: http://www.gazzettaufficiale.it/eli/id/2026/11/10/26G00219/sg → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.

## Registro tecnico

- sentinella: sentinella: mirato; Eurostat aggiornati 1, file 0, documenti nuovi 8, serie cambiate 1, errori 0
- apprendimento: 193 KPI, stati {'manuale': 147, 'in osservazione': 46}, aree calibrate 0
- legislazione: archivio GU: 621 atti, 621 con testo; nuovi 0; testi scaricati 0; richieste 2; errori 0
- ERRORE europa: FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/governai/governai/europa/archivio/testi/2026/32026H03925.txt'
- costituzione: 0 atti con forza di legge esaminati; con segnali alti 0
- consiglio: 95 previsioni, 0 verificate oggi, 0 verificate in totale
- verifica sedute: 2 attive, 2 confermate, 0 da riesaminare
- controlla.py: avvisi: 0  ->  bilancio.md
- decidi.py: -> esito.md, esito_proposte.csv
- ottimizza.py (riferimento): spesa 13.52  coperture 11.37  proposte 68/76  -> selezione_riferimento.md
- ottimizza.py (momento): spesa 13.49  coperture 11.37  proposte 66/76  -> selezione_momento.md

## 6. Nota del livello AI

Livello AI non eseguito: credenziali dell'API di Claude assenti (impostare la variabile d'ambiente ANTHROPIC_API_KEY).