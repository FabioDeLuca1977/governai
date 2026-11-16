# Bollettino GovernAI — 2026-11-16

*Generato automaticamente da `sistema/pipeline.py` alle 09:03. Fonti: Eurostat, ISTAT, MEF/RGS, Banca d'Italia e documenti ufficiali osservati.*

## 1. Cosa è cambiato nelle fonti

- Modalità di aggiornamento: **mirato**
- Dataset Eurostat aggiornati: demo_pjan, demo_pjangroup, migr_pop1ctz
- File ufficiali aggiornati: 0
- Serie cambiate e archiviate in `dati/storico/`: popolazione
- Documenti nuovi sulle pagine osservate: 0

## 2. Cruscotto

| | Indicatore | Periodo | Valore | Var. | Var. 12 periodi |
|---|---|---|---|---|---|
| 🔴 | Inflazione (HICP, % annua) | 2026-10 *(provv.)* | 5,60 % | +1,40 | +4,30 |
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

Il programma di riferimento (tutte le coperture, nucleo robusto prima) costa **13,54 mld/anno**; il programma adattato al momento costa **13,54 mld/anno**. Entrambi sono finanziati senza deficit.

**Differenze rispetto al riferimento** (effetto delle allerte):

- 01-P5: ESSENZIALE → PIENA
- 02-C1: ZERO → PIENA
- 04-P1: PILOTA → esclusa
- 04-P7: ESSENZIALE → PILOTA
- 05-C7: PIENA → ESSENZIALE
- 06-C9: PIENA → ESSENZIALE

**Cambiamenti rispetto al bollettino precedente:**

- 01-P16: esclusa → PIENA
- 01-P17: esclusa → PIENA
- 01-P18: esclusa → PIENA
- 01-P6: ESSENZIALE → PIENA
- 01-P8: ZERO → ESSENZIALE
- 02-C8: esclusa → PIENA
- 02-C9: esclusa → PILOTA
- 03-P5: esclusa → PILOTA
- 04-P1: PILOTA → esclusa
- 04-P8: ZERO → PIENA
- 05-C10: PILOTA → esclusa
- 05-C5: ESSENZIALE → PIENA
- 05-C8: ESSENZIALE → PIENA
- 07-C2: ESSENZIALE → PIENA
- 07-C6: PILOTA → PIENA

Dettaglio: `programma/selezione_momento.md`.

## 5. Revisione AI richiesta

Nessuna revisione necessaria.

## Registro tecnico

- sentinella: sentinella: mirato; Eurostat aggiornati 3, file 0, documenti nuovi 0, serie cambiate 1, errori 0
- apprendimento: 193 KPI, stati {'manuale': 147, 'in osservazione': 46}, aree calibrate 0
- legislazione: archivio GU: 699 atti, 699 con testo; nuovi 0; testi scaricati 0; richieste 2; errori 0
- europa: europa: 857 atti GU L in archivio, 282 negli ultimi 30 giorni; 144 direttive con termine (23 critiche, 11 alte); 84 infrazioni aperte; semestre: procedura per disavanzo eccessivo sospesa (raccomandazione del Consiglio del 10/07/2026); richieste 24
- giurisprudenza: pronunce citate: 81; verificate: 81; da controllare: []
- costituzione: 0 atti con forza di legge esaminati; con segnali alti 0
- consiglio: 95 previsioni, 0 verificate oggi, 8 verificate in totale
- verifica sedute: 2 attive, 0 confermate, 2 da riesaminare
- controlla.py: avvisi: 0  ->  bilancio.md
- decidi.py: -> esito.md, esito_proposte.csv
- ottimizza.py (riferimento): spesa 13.54  coperture 11.45  proposte 74/83  -> selezione_riferimento.md
- ottimizza.py (momento): spesa 13.54  coperture 11.45  proposte 73/83  -> selezione_momento.md