# Bollettino GovernAI — 2026-11-17

*Generato automaticamente da `sistema/pipeline.py` alle 13:54. Fonti: Eurostat, ISTAT, MEF/RGS, Banca d'Italia e documenti ufficiali osservati.*

## 1. Cosa è cambiato nelle fonti

- Modalità di aggiornamento: **mirato**
- Dataset Eurostat aggiornati: namq_10_gdp, nasa_10_nf_tr
- File ufficiali aggiornati: 1
- Serie cambiate e archiviate in `dati/storico/`: nessuna
- Documenti nuovi sulle pagine osservate: 10
  - ISTAT - Home e comunicati: https://www.istat.it/comunicato-stampa/prezzi-al-consumo-ottobre-2026/
  - ISTAT - Home e comunicati: https://www.istat.it/documenti/concorso-o-selezione/
  - ISTAT - Home e comunicati: https://www.istat.it/evento/ciclo-di-seminari-sul-presente-e-sul-futuro-della-statistica-ufficiale/
  - ISTAT - Home e comunicati: https://www.istat.it/evento/progetto-insegnanti-istat-statistica-ufficiale-strumenti-per-docenti/
  - Corte dei conti: https://www.corteconti.it/HOME/Documenti/DettaglioDocumenti?Id=4de5a37a-ec30-45bf-95ba-37966439c8a0
  - Corte dei conti: https://www.corteconti.it/HOME/Documenti/DettaglioDocumenti?Id=695a7707-8f69-4c39-9428-d249ab26ab7e
  - Gazzetta Ufficiale: http://www.gazzettaufficiale.it/eli/id/2026/11/16/26G00226/sg
  - Gazzetta Ufficiale: https://www.gazzettaufficiale.it/gazzetta/contratti/caricaDettaglio/home?dataPubblicazioneGazzetta=2026-11-16&numeroGazzetta=131
  - Gazzetta Ufficiale: https://www.gazzettaufficiale.it/gazzetta/serie_generale/caricaDettaglio/home?dataPubblicazioneGazzetta=2026-11-16&numeroGazzetta=267
  - Gazzetta Ufficiale: https://www.gazzettaufficiale.it/gazzetta/unione_europea/caricaDettaglio/home?dataPubblicazioneGazzetta=2026-11-16&numeroGazzetta=90

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

Non ricalcolato: nessun dato nuovo e nessuna nuova allerta.

## 5. Revisione AI richiesta

**10 compiti** per il livello AI (`sistema/stato/revisione_ai.json`):
- [documento_nuovo] ISTAT - Home e comunicati: https://www.istat.it/comunicato-stampa/prezzi-al-consumo-ottobre-2026/ → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] ISTAT - Home e comunicati: https://www.istat.it/documenti/concorso-o-selezione/ → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] ISTAT - Home e comunicati: https://www.istat.it/evento/ciclo-di-seminari-sul-presente-e-sul-futuro-della-statistica-ufficiale/ → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] ISTAT - Home e comunicati: https://www.istat.it/evento/progetto-insegnanti-istat-statistica-ufficiale-strumenti-per-docenti/ → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] Corte dei conti: https://www.corteconti.it/HOME/Documenti/DettaglioDocumenti?Id=4de5a37a-ec30-45bf-95ba-37966439c8a0 → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] Corte dei conti: https://www.corteconti.it/HOME/Documenti/DettaglioDocumenti?Id=695a7707-8f69-4c39-9428-d249ab26ab7e → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] Gazzetta Ufficiale: http://www.gazzettaufficiale.it/eli/id/2026/11/16/26G00226/sg → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] Gazzetta Ufficiale: https://www.gazzettaufficiale.it/gazzetta/contratti/caricaDettaglio/home?dataPubblicazioneGazzetta=2026-11-16&numeroGazzetta=131 → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] Gazzetta Ufficiale: https://www.gazzettaufficiale.it/gazzetta/serie_generale/caricaDettaglio/home?dataPubblicazioneGazzetta=2026-11-16&numeroGazzetta=267 → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] Gazzetta Ufficiale: https://www.gazzettaufficiale.it/gazzetta/unione_europea/caricaDettaglio/home?dataPubblicazioneGazzetta=2026-11-16&numeroGazzetta=90 → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.

## Registro tecnico

- sentinella: sentinella: mirato; Eurostat aggiornati 2, file 1, documenti nuovi 10, serie cambiate 0, errori 0
- apprendimento: 193 KPI, stati {'manuale': 147, 'in osservazione': 46}, aree calibrate 0
- legislazione: archivio GU: 726 atti, 726 con testo; nuovi 27; testi scaricati 27; richieste 142; errori 0
- europa: europa: 878 atti GU L in archivio, 303 negli ultimi 30 giorni; 144 direttive con termine (23 critiche, 11 alte); 84 infrazioni aperte; semestre: procedura per disavanzo eccessivo sospesa (raccomandazione del Consiglio del 10/07/2026); richieste 15; ERRORI: cellar_gu_l, cellar_direttive, cellar_propo
- costituzione: 1 atti con forza di legge esaminati; con segnali alti 0
- consiglio: 95 previsioni, 0 verificate oggi, 8 verificate in totale
- verifica sedute: 2 attive, 0 confermate, 2 da riesaminare
- modelli non ricalcolati: nessun dato nuovo e nessuna nuova allerta