# Bollettino GovernAI — 2026-11-28

*Generato automaticamente da `sistema/pipeline.py` alle 09:11. Fonti: Eurostat, ISTAT, MEF/RGS, Banca d'Italia e documenti ufficiali osservati.*

## 1. Cosa è cambiato nelle fonti

- Modalità di aggiornamento: **completo**
- Dataset Eurostat aggiornati: demo_find, demo_gind, demo_pjan, demo_pjangroup, edat_lfse_03, edat_lfse_14, edat_lfse_16, edat_lfse_20, edat_lfse_22, ei_bsco_m, env_ac_cur, env_air_gge, gba_nabsfin07, gov_10a_exp, gov_10a_main, gov_10a_taxag, gov_10dd_edpt1, gov_10q_ggdebt, hlth_rs_prs2, hlth_sha11_hc, hlth_sha11_hf, hlth_silc_08, ilc_iw01, ilc_lvho07c, irt_lt_mcby_m, isoc_ciegi_ac, isoc_eb_ai, isoc_sk_dskl_i21, isoc_sks_itspt, lfsa_egan, lfsi_emp_a, migr_asyappctza, migr_eiord, migr_eirtn, migr_pop1ctz, nama_10_gdp, nama_10_lp_ulc, namq_10_gdp, nasa_10_nf_tr, nrg_ind_ren, prc_hicp_aind, prc_hicp_minr, prc_hpi_a, proj_25ndbi, rd_e_gerdfund, rd_e_gerdtot, road_eqs_carhab, road_eqs_carpda, sbs_sc_ovw, sts_inpr_m, tepsr_sp200, tour_occ_nim, tour_occ_nin2, tour_occ_ninat, trng_lfs_14, trng_lfse_01, une_rt_m
- File ufficiali aggiornati: 1
- Serie cambiate e archiviate in `dati/storico/`: 00c_fiducia_consumatori, bm_01_produttivita_ora
- Documenti nuovi sulle pagine osservate: 3
  - Gazzetta Ufficiale: https://www.gazzettaufficiale.it/gazzetta/concorsi/caricaDettaglio/home?dataPubblicazioneGazzetta=2026-11-27&numeroGazzetta=92
  - Gazzetta Ufficiale: https://www.gazzettaufficiale.it/gazzetta/contratti/caricaDettaglio/home?dataPubblicazioneGazzetta=2026-11-27&numeroGazzetta=136
  - Gazzetta Ufficiale: https://www.gazzettaufficiale.it/gazzetta/serie_generale/caricaDettaglio/home?dataPubblicazioneGazzetta=2026-11-27&numeroGazzetta=277
- Problemi: 09b_personale_rgs.py ERRORE: requests.exceptions.ReadTimeout: HTTPSConnectionPool(host='bdap-opendata.rgs.mef.gov.it', port=443): Read timed out. (read timeout=60)

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
| 🔴 | Fiducia dei consumatori (saldo) | 2026-11 | -24,90 saldo | -1,70 | -8,30 |
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
- **fiducia_in_calo**: Fiducia dei consumatori in netto calo sull'anno. (valore -24,90 saldo, 2026-11)
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

- nessuno

Dettaglio: `programma/selezione_momento.md`.

## 5. Revisione AI richiesta

**4 compiti** per il livello AI (`sistema/stato/revisione_ai.json`):
- [documento_nuovo] Gazzetta Ufficiale: https://www.gazzettaufficiale.it/gazzetta/concorsi/caricaDettaglio/home?dataPubblicazioneGazzetta=2026-11-27&numeroGazzetta=92 → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] Gazzetta Ufficiale: https://www.gazzettaufficiale.it/gazzetta/contratti/caricaDettaglio/home?dataPubblicazioneGazzetta=2026-11-27&numeroGazzetta=136 → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [documento_nuovo] Gazzetta Ufficiale: https://www.gazzettaufficiale.it/gazzetta/serie_generale/caricaDettaglio/home?dataPubblicazioneGazzetta=2026-11-27&numeroGazzetta=277 → Leggere il documento; se cambia dati, stime o coperture usate dai dossier, aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu.
- [variazione_rilevante] Fiducia dei consumatori (saldo): -23.3 (2026-10) → -24.9 (2026-11) → Valutare se cambiano diagnosi, costi o priorità delle proposte collegate.

## Registro tecnico

- sentinella: sentinella: completo; Eurostat aggiornati 57, file 1, documenti nuovi 3, serie cambiate 2, errori 0
- apprendimento: 193 KPI, stati {'manuale': 147, 'in osservazione': 46}, aree calibrate 0
- legislazione: archivio GU: 951 atti, 951 con testo; nuovi 21; testi scaricati 21; richieste 135; errori 0
- europa: europa: 1033 atti GU L in archivio, 343 negli ultimi 30 giorni; 147 direttive con termine (24 critiche, 9 alte); 85 infrazioni aperte; semestre: procedura per disavanzo eccessivo sospesa (raccomandazione del Consiglio del 10/07/2026); richieste 24
- costituzione: 2 atti con forza di legge esaminati; con segnali alti 0
- consiglio: 95 previsioni, 2 verificate oggi, 10 verificate in totale
- verifica sedute: 2 attive, 0 confermate, 2 da riesaminare
- controlla.py: avvisi: 0  ->  bilancio.md
- decidi.py: -> esito.md, esito_proposte.csv
- ottimizza.py (riferimento): spesa 14.06  coperture 11.98  proposte 87/97  -> selezione_riferimento.md
- ottimizza.py (momento): spesa 14.07  coperture 11.98  proposte 87/97  -> selezione_momento.md