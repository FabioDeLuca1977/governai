# Bollettino GovernAI — 2026-11-23

*Generato automaticamente da `sistema/pipeline.py` alle 10:40. Fonti: Eurostat, ISTAT, MEF/RGS, Banca d'Italia e documenti ufficiali osservati.*

## 1. Cosa è cambiato nelle fonti

- Modalità di aggiornamento: **mirato**
- Dataset Eurostat aggiornati: nessuno
- File ufficiali aggiornati: 1
- Serie cambiate e archiviate in `dati/storico/`: 09_personale_funzioni_centrali
- Documenti nuovi sulle pagine osservate: 6
  - ISTAT - Home e comunicati: https://www.istat.it/comunicato-stampa/flussi-turistici-iii-trimestre-2026/
  - Corte dei conti: https://www.corteconti.it/HOME/StampaMedia/ComunicatiStampa/DettaglioComunicati?Id=091b2790-acf0-43e0-a4fd-cc03c52bf4aa
  - Gazzetta Ufficiale: http://www.gazzettaufficiale.it/eli/gu/2026/11/20/90/s4/html
  - Gazzetta Ufficiale: http://www.gazzettaufficiale.it/eli/id/2026/11/20/26E06298/s4
  - Gazzetta Ufficiale: http://www.gazzettaufficiale.it/eli/id/2026/11/20/26G00232/sg
  - Gazzetta Ufficiale: http://www.gazzettaufficiale.it/eli/id/2026/11/21/26G00231/sg

## 2. Cruscotto

| | Indicatore | Periodo | Valore | Var. | Var. 12 periodi |
|---|---|---|---|---|---|
| 🔴 | Inflazione (HICP, % annua) | 2026-10 | 5,60 % | +1,40 | +4,30 |
| 🔴 | Disoccupazione (%) | 2026-09 | 6,30 % | +0,10 | +0,40 |
| 🟢 | Disoccupazione under 25 (%) | 2026-09 | 19,90 % | -0,40 | -0,60 |
| 🔴 | Rendimento titoli decennali IT (%) | 2026-10 | 4,68 % | +0,32 | +1,24 |
| 🔴 | Spread IT-DE (punti base) | 2026-10 | 126,40 pb | +37,50 | +43,90 |
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
- **spread_in_salita**: Spread in aumento di oltre 30 punti base in un mese. (valore 126,40 pb, 2026-10)
  - Azione: Monitoraggio rafforzato; nessuna nuova spesa permanente finché non rientra.
  - Priorità: —; sospese: —
- **debito_in_salita**: Debito/PIL in aumento di oltre 1 punto in un trimestre. (valore 139,90 % PIL, 2026-Q2)
  - Azione: Applicare la regola FUT: nessuna variante finanziata a debito; rivedere la traiettoria della Difesa.
  - Priorità: —; sospese: 07-C5
- **fiducia_in_calo**: Fiducia dei consumatori in netto calo sull'anno. (valore -23,30 saldo, 2026-10)
  - Azione: Segnale di rischio per i consumi; valutare la tempistica delle coperture che pesano sui consumatori (IVA, accise).
  - Priorità: —; sospese: —

## 4. Programma del momento

Il programma di riferimento (tutte le coperture, nucleo robusto prima) costa **14,06 mld/anno**; il programma adattato al momento costa **14,07 mld/anno**. Entrambi sono finanziati senza deficit.

**Differenze rispetto al riferimento** (effetto delle allerte):

- 01-P6: PIENA → ESSENZIALE
- 02-C1: ZERO → PIENA
- 05-C8: PIENA → ESSENZIALE
- 06-C9: ESSENZIALE → PIENA
- 07-C6: PIENA → ESSENZIALE

**Cambiamenti rispetto al bollettino precedente:**

- 01-P14: esclusa → ESSENZIALE
- 01-P26: esclusa → PIENA
- 01-P6: PIENA → ESSENZIALE
- 05-C8: PIENA → ESSENZIALE
- 06-C9: ESSENZIALE → PIENA
- 08-P6: PILOTA → esclusa
- 09-C11: esclusa → PIENA
- 09-C12: esclusa → PIENA

Dettaglio: `programma/selezione_momento.md`.

## 5. Revisione AI richiesta

**6 compiti** per il livello AI (`sistema/stato/revisione_ai.json`):
- [documento_nuovo] ISTAT - Home e comunicati: https://www.istat.it/comunicato-stampa/flussi-turistici-iii-trimestre-2026/ → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] Corte dei conti: https://www.corteconti.it/HOME/StampaMedia/ComunicatiStampa/DettaglioComunicati?Id=091b2790-acf0-43e0-a4fd-cc03c52bf4aa → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] Gazzetta Ufficiale: http://www.gazzettaufficiale.it/eli/gu/2026/11/20/90/s4/html → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] Gazzetta Ufficiale: http://www.gazzettaufficiale.it/eli/id/2026/11/20/26E06298/s4 → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] Gazzetta Ufficiale: http://www.gazzettaufficiale.it/eli/id/2026/11/20/26G00232/sg → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] Gazzetta Ufficiale: http://www.gazzettaufficiale.it/eli/id/2026/11/21/26G00231/sg → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.

## Registro tecnico

- sentinella: sentinella: mirato; Eurostat aggiornati 0, file 1, documenti nuovi 6, serie cambiate 1, errori 0
- apprendimento: 193 KPI, stati {'manuale': 147, 'in osservazione': 46}, aree calibrate 0
- legislazione: archivio GU: 832 atti, 832 con testo; nuovi 0; testi scaricati 0; richieste 2; errori 0
- europa: europa: 984 atti GU L in archivio, 333 negli ultimi 30 giorni; 145 direttive con termine (23 critiche, 10 alte); 85 infrazioni aperte; semestre: procedura per disavanzo eccessivo sospesa (raccomandazione del Consiglio del 10/07/2026); richieste 24
- giurisprudenza: pronunce citate: 81; verificate: 81; da controllare: []
- costituzione: 0 atti con forza di legge esaminati; con segnali alti 0
- consiglio: 95 previsioni, 0 verificate oggi, 8 verificate in totale
- verifica sedute: 2 attive, 0 confermate, 2 da riesaminare
- controlla.py: avvisi: 0  ->  bilancio.md
- decidi.py: -> esito.md, esito_proposte.csv
- ottimizza.py (riferimento): spesa 14.06  coperture 11.98  proposte 87/97  -> selezione_riferimento.md
- ottimizza.py (momento): spesa 14.07  coperture 11.98  proposte 87/97  -> selezione_momento.md