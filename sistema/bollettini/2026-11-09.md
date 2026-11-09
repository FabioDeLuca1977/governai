# Bollettino GovernAI — 2026-11-09

*Generato automaticamente da `sistema/pipeline.py` alle 15:49. Fonti: Eurostat, ISTAT, MEF/RGS, Banca d'Italia e documenti ufficiali osservati.*

## 1. Cosa è cambiato nelle fonti

- Modalità di aggiornamento: **nessun aggiornamento**
- Dataset Eurostat aggiornati: nessuno
- File ufficiali aggiornati: 0
- Serie cambiate e archiviate in `dati/storico/`: nessuna
- Documenti nuovi sulle pagine osservate: 4
  - ISTAT - Home e comunicati: https://www.istat.it/documenti/sistema-informativo-6/
  - Corte dei conti: https://www.corteconti.it/HOME/Documenti/DettaglioDocumenti?Id=2b1c4d96-eecd-4863-946a-e2a4f71726e4
  - Corte dei conti: https://www.corteconti.it/HOME/Documenti/DettaglioDocumenti?Id=df6bf072-c88a-4eda-aa56-f5f5947aa1a7
  - Corte dei conti: https://www.corteconti.it/HOME/Documenti/DettaglioDocumenti?Id=ffdaa75d-bd65-4a98-b5e5-068ff3adb288

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

Non ricalcolato: nessun dato nuovo e nessuna nuova allerta.

## 5. Revisione AI richiesta

**4 compiti** per il livello AI (`sistema/stato/revisione_ai.json`):
- [documento_nuovo] ISTAT - Home e comunicati: https://www.istat.it/documenti/sistema-informativo-6/ → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] Corte dei conti: https://www.corteconti.it/HOME/Documenti/DettaglioDocumenti?Id=2b1c4d96-eecd-4863-946a-e2a4f71726e4 → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] Corte dei conti: https://www.corteconti.it/HOME/Documenti/DettaglioDocumenti?Id=df6bf072-c88a-4eda-aa56-f5f5947aa1a7 → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] Corte dei conti: https://www.corteconti.it/HOME/Documenti/DettaglioDocumenti?Id=ffdaa75d-bd65-4a98-b5e5-068ff3adb288 → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.

## Registro tecnico

- sentinella: sentinella: nessun aggiornamento; Eurostat aggiornati 0, file 0, documenti nuovi 4, serie cambiate 0, errori 0
- apprendimento: 189 KPI, stati {'manuale': 143, 'in osservazione': 46}, aree calibrate 0
- legislazione: archivio GU: 576 atti, 576 con testo; nuovi 0; testi scaricati 0; richieste 2; errori 0
- ERRORE europa: FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/governai/governai/europa/archivio/testi/2026/32026H03925.txt'
- giurisprudenza: pronunce citate: 81; verificate: 81; da controllare: []
- costituzione: 0 atti con forza di legge esaminati; con segnali alti 0
- consiglio: 95 previsioni, 0 verificate oggi, 0 verificate in totale
- verifica sedute: 2 attive, 2 confermate, 0 da riesaminare
- modelli non ricalcolati: nessun dato nuovo e nessuna nuova allerta

## 6. Nota del livello AI

Livello AI non eseguito: credenziali dell'API di Claude assenti (impostare la variabile d'ambiente ANTHROPIC_API_KEY).