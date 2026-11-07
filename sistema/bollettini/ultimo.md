# Bollettino GovernAI — 2026-11-07

*Generato automaticamente da `sistema/pipeline.py` alle 18:07. Fonti: Eurostat, ISTAT, MEF/RGS, Banca d'Italia e documenti ufficiali osservati.*

## 1. Cosa è cambiato nelle fonti

- Download non eseguito in questa esecuzione.

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
| 🔴 | Produzione industriale (2021=100) | 2026-08 | 92,80 indice | -1,20 | +0,20 |
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

Il programma di riferimento (tutte le coperture, nucleo robusto prima) costa **13,74 mld/anno**; il programma adattato al momento costa **13,73 mld/anno**. Entrambi sono finanziati senza deficit.

**Differenze rispetto al riferimento** (effetto delle allerte):

- 01-P5: ESSENZIALE → PIENA
- 04-P1: ESSENZIALE → PILOTA
- 04-P2: esclusa → ESSENZIALE
- 05-C4: PIENA → ESSENZIALE
- 06-C6: ZERO → PIENA
- 08-P6: PIENA → esclusa

**Cambiamenti rispetto al bollettino precedente:**

- 02-C5: ZERO → ESSENZIALE
- 03-P3: ESSENZIALE → esclusa
- 03-P5: ESSENZIALE → PIENA
- 04-P1: esclusa → PILOTA
- 04-P3: ESSENZIALE → esclusa
- 04-P6: ESSENZIALE → PIENA
- 05-C2: esclusa → ESSENZIALE
- 05-C3: ESSENZIALE → ZERO
- 05-C6: ESSENZIALE → PIENA
- 06-C2: ESSENZIALE → esclusa
- 06-C6: ZERO → PIENA
- 07-C1: ESSENZIALE → PIENA
- 07-C3: ESSENZIALE → PIENA
- 08-P6: PILOTA → esclusa
- 09-C2: ESSENZIALE → PIENA
- 09-C5: ZERO → PIENA

Dettaglio: `programma/selezione_momento.md`.

## 5. Revisione AI richiesta

Nessuna revisione necessaria.

## Registro tecnico

- apprendimento: 158 KPI, stati {'manuale': 114, 'in osservazione': 44}, aree calibrate 0
- controlla.py: avvisi: 0  ->  bilancio.md
- decidi.py: -> esito.md, esito_proposte.csv
- ottimizza.py (riferimento): spesa 13.74  coperture 11.77  proposte 44/52  -> selezione_riferimento.md
- ottimizza.py (momento): spesa 13.73  coperture 11.77  proposte 44/52  -> selezione_momento.md