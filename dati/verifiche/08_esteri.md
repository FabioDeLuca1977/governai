# Verifica dati — Area 08 (Esteri, Europa, Riforme istituzionali, Rapporti con il Parlamento)

*Agente verificatore dati GovernAI, 7 novembre 2026. Dossier: `ministeri/08_esteri_europa_istituzioni.md`. Script: `dati/script/08_esteri.py` (serie in `dati/serie/08_*.csv`, registro `dati/serie/_registro_08.csv`, grezzi in `dati/raw/08_*`).*

## Tabella di verifica

| # | Dato | Valore nel dossier | Valore verificato | Fonte primaria (ente, documento/serie, anno, URL) | Esito |
|---|---|---|---|---|---|
| 1 | Spese finali MAECI 2026 | 3,83 mld; 0,4% spesa Stato; ~99% corrente | 3.833,9 mln; 0,4%; 99% (3.796,4 mln correnti) | Camera dei deputati, *Il bilancio del MAECI*, 23/01/2026, https://temi.camera.it/leg19/temi/il-bilancio-del-maeci.html | ✅ |
| 2 | Risorse ministri senza portafoglio | "decine di milioni", stima | non verificato (bilancio PCM non consultato) | — | ❓ |
| 3 | Export beni verso USA 2025 | 69,6 mld (+7,2%), 10,8% | 69,6 mld; +7,2%; 10,8% | Eurostat Comext DS-045409, 2025 (serie `08_commercio_it_partner`) | ✅ |
| 4 | Quota export verso Germania 2025 | 11,4% | **11,2%** (72,2 su 643,2 mld) | Eurostat Comext DS-045409, 2025 | ✏️ |
| 5 | Avanzo commerciale 2025 | 50,7 mld | 50,7 mld (643,2 − 592,5) | Eurostat Comext DS-045409, 2025 | ✅ |
| 6 | Import dagli USA 2025 | +35,9% | +35,9% (26,1 → 35,4 mld) | Eurostat Comext DS-045409 | ✅ |
| 7 | APS/RNL Italia 2025 | 0,30% (ISTAT) | 0,30% (equiv. dono, prelim.); 0,29% nel 2024 | OCSE DAC1, misura 11002, apr. 2026, https://sdmx.oecd.org/public/rest/data/OECD.DCD.FSD,DSD_DAC1@DF_DAC1,/ITA+DAC.......... (serie `08_aps_ocse_dac`) | ✅ |
| 8 | Media OCSE APS/RNL | "intorno allo 0,4%" | **0,26%** totale DAC 2025 (0,34% nel 2024): l'Italia è sopra la media ponderata | OCSE DAC1, misura 11002, DONOR=DAC, 2025 | ✏️ |
| 9 | Quota APS per rifugiati in Italia 2025 | stima, da verificare | **1.331 mln €, 18,5% dell'APS netto** (20,6% dell'equivalente dono); 26,5% nel 2024 | OCSE DAC1, misura 1820 "Refugees in donor countries" | ✏️ |
| 10 | Valutazioni d'impatto APS "poche e non sistematiche" | stima | valutazione qualitativa, non quantificabile | — | ❓ |
| 11 | QFP 2028–34, proposta Commissione | 1.763 mld (circa 2.000 "con rimborso NGEU") | 1.763,1 mld a prezzi 2025 = **1.984,9 mld a prezzi correnti**: la differenza è di prezzi, non di perimetro | Consiglio UE, ST 10058/26, tabella allegata, 11/06/2026, https://data.consilium.europa.eu/doc/document/ST-10058-2026-INIT/en/pdf | ✏️ |
| 12 | Proposta Presidenza cipriota | 1.730,2 mld, −2% (stampa) | 1.730,2 mld prezzi 2025 (1.947,7 correnti); −1,9% | Consiglio UE, ST 10058/26 (Negotiating Box), 11/06/2026 | ✅ |
| 13 | PNRR: dotazione, incassi, ultima rata | 194,4; ~166 (85%); 28,4 entro 31/12/2026 | 194,4; 166 mld dopo la nona rata (04/06/2026); decima rata richiesta 28,4 mld, non ancora pagata (nessuna notizia di pagamento al 7/11) | Camera, *Il PNRR*, https://temi.camera.it/leg19/pnrr.html; conferma stampa (Milano Finanza 04/06/2026, Agenzia Nova) | ✅ |
| 14 | Debito pubblico/PIL | "intorno al 135%" | **136,7% nel 2025** (134,3% nel 2024) | Eurostat gov_10dd_edpt1 (serie `debito_pil`, area 00) | ✏️ |
| 15 | SAFE: dotazione totale e tetto IT | 150 mld; 14,9 mld | confermati (Reg. UE 2025/1106; tetto italiano approvato da Commissione e Consiglio) | Commissione UE, Q&A Rearm Europe (qanda_25_790) | ✅ |
| 16 | SAFE: quota effettivamente richiesta | 8,9 mld o "larga maggioranza" di 14,9, da verificare | **"poco più di 8 mld"**: piano aggiornato approvato dalla Commissione il 13/10/2026; manca il Consiglio, contratto non firmato | Portavoce Commissione, briefing 13/10/2026 (audiovisivo I-296112), via Eunews https://www.eunews.it/2026/10/13/difesa-la-commissione-europea-approva-la-richiesta-dellitalia-per-lo-strumento-safe/ | ✏️ |
| 17 | Numero decreti-legge e fiducie XIX leg. | da verificare | ~98 DL e 91 fiducie secondo stampa su dati Openpolis, data incerta; non verificato su Camera/Openpolis | (secondaria) La Notizia su Openpolis | ❓ |
| 18 | Affluenza politiche 2022 | 63,9% | 63,9% (Camera, Italia) | Ministero dell'Interno, Eligendo, 25/09/2022, https://elezionistorico.interno.gov.it | ✅ |
| 19 | Legge elettorale: stato dell'iter | approvata alla Camera a luglio (217–152), soglia 40% o 42%, all'esame del Senato | **Legge 9 ottobre 2026, n. 180**, GU n. 235 del 9/10/2026, in vigore dal 24/10/2026. Soglia **42%** dei voti validi in ciascuna Camera; premio 70 seggi alla Camera, tetto 220. Iter: Camera 16/07 (217–152), Senato 15/09 con modifiche, Camera definitiva 08/10 (227–164). Ricorsi annunciati | Normattiva, https://www.normattiva.it/eli/stato/LEGGE/2026/10/09/180/ORIGINAL; voti via AGI 08/10/2026 | ✏️ |
| 20 | "Quarta riforma in ~20 anni" (2005, 2015, 2017, 2026) | — | l. 270/2005, l. 52/2015, l. 165/2017, l. 180/2026 | Normattiva | ✅ |
| 21 | Digital Omnibus: adozione formale | accordo provvisorio 07/05/2026; adozione da verificare | **Reg. (UE) 2026/1744 dell'8/07/2026**, GU L 24/07/2026, in vigore 27/07/2026 | EUR-Lex, https://eur-lex.europa.eu/eli/reg/2026/1744/oj | ✏️ |
| 22 | Nuove scadenze alto rischio | 2/12/2027 (All. III), 2/8/2028 (All. I) | confermate (considerando 40 del Reg. 2026/1744) | EUR-Lex, Reg. (UE) 2026/1744 | ✅ |
| 23 | L. 132/2025 in vigore | 10/10/2025 | 10/10/2025 | Normattiva, l. 23/09/2025 n. 132 | ✅ |
| 24 | Decreti attuativi l. 132/2025 | approvati in via preliminare 10/06/2026; pubblicazione da verificare | **D.Lgs. 7/10/2026, n. 179** (poteri autorità, AI nella formazione), GU n. 234 dell'8/10/2026, vigente dal 23/10/2026. Secondo decreto: approvazione definitiva CdM 04/08/2026 secondo stampa, estremi GU non verificati | Gazzetta Ufficiale (testo del d.lgs. 179/2026) | ✏️ (parz. ❓) |
| 25 | P1: costo Ufficio + Assemblea | 30–60 mln/anno, stima | nessuna stima ufficiale: resta stima GovernAI | — | ❓ |
| 26 | P2: costo | <10 mln/anno | nessuna stima ufficiale: stima GovernAI | — | ❓ |
| 27 | P3: costo voto fuorisede | 10–30 mln per consultazione | nessuna stima ufficiale trovata: stima GovernAI | — | ❓ |
| 28 | P4: quota italiana del RNL UE | 12–13%, stima | **12,0%** (2.265,9 su 18.813 mld, 2025); 12,07% nel file della Commissione | Eurostat nasa_10_nf_tr (serie `08_rnl_it_ue`); Commissione, *EU spending and revenue* | ✏️ |
| 29 | P5: costo del salto allo 0,7% | ~9 mld su RNL ~2.200 mld | **9,1 mld** su RNL 2025 di **2.265,9 mld** | Eurostat nasa_10_nf_tr; OCSE DAC1 | ✏️ (RNL), ✅ (costo) |
| 30 | P5: +0,02 pt/anno; +4,5 mld nel 2035 | 0,4–0,5 mld/anno; 4,5 mld | 0,45 mld/anno; 4,5 mld (0,30→0,50% a RNL costante) | calcolo GovernAI su Eurostat | ✅ |
| 31 | P6: costo pacchetto export | 0,2–0,4 mld/anno | nessuna stima ufficiale: stima GovernAI | — | ❓ |
| 32 | Contributo netto italiano al bilancio UE (dato aggiunto) | assente | Saldo semplificato (spesa UE in IT − contributi nazionali esclusi dazi): **−2,5 mld nel 2024, −4,1 mld nel 2025** sul solo QFP; **+6,9 / +6,0 mld** con le sovvenzioni NGEU. Stampa (Eunews, nov. 2025) riporta −1,6 mld per il 2024 con il metodo ufficiale dell'*operating budgetary balance*, che esclude le spese amministrative | Commissione UE, *EU spending and revenue 2000–2025*, xlsx 29/09/2026 (serie `08_saldo_it_bilancio_ue`) | ✏️ (nuovo dato) |

**Riepilogo**: 32 cifre esaminate: 13 ✅, 12 ✏️ (le righe 24 e 29 sono corrette solo in parte), 7 ❓ (5 sono stime di costo GovernAI senza equivalente ufficiale).

## Note di metodo
- I dati di commercio sono Eurostat Comext (concetto comunitario). Coincidono al decimale con i dati ISTAT/ICE citati nel dossier per USA e totali; la quota tedesca risulta 11,2%, non 11,4%.
- L'APS è in "equivalente dono" (standard OCSE dal 2018). La quota per i rifugiati è calcolata sui flussi netti (misura 1010), perché la voce 1820 è registrata su base cassa. I dati 2025 sono preliminari: quelli definitivi escono a dicembre 2026.
- Il saldo con il bilancio UE è un calcolo GovernAI, non l'*operating budgetary balance* ufficiale della Commissione. Il file 2000–2025 non lo riporta: per il valore ufficiale serve la *EU Budget Financial Report*.
- fonti.py: `eurostat()` supporta solo l'endpoint "statistics" e non i dataset Comext (DS-xxxx, endpoint `/api/comext/`). Il problema è aggirato nello script con un parser JSON-stat locale; fonti.py non è stato modificato. Segnalazione minore: `salva()` registra `aggiornato_fonte` solo se `df.attrs["aggiornato"]` è impostato, quindi non per le serie da `scarica()` o da CSV OCSE (impostato a mano nello script).
- Fonti primarie non raggiunte: il profilo OCSE Italia (HTTP 403, rango 17° ripreso dalla sintesi di ricerca) e l'elenco ufficiale di decreti e fiducie (Camera/Openpolis).

## Impatto sulle proposte

- **Proposta 3 (Regole del gioco stabili)**: è la correzione più rilevante. La legge elettorale non è più "riforma in corso" ma **legge 180/2026, in vigore dal 24 ottobre 2026**, e si applicherà alle prossime politiche (entro il 2027), cioè proprio nella finestra di 12 mesi che la Commissione di Venezia sconsiglia. La sostanza della proposta non cambia: la clausola di stabilità resta valida, ma per il futuro. Cambia invece la fattibilità nel breve: la clausola non può più evitare che la nuova legge si applichi al prossimo voto, e una nuova modifica ravvicinata violerebbe lo stesso principio. **Il punteggio Breve resta +1, la confidenza scende da Media a Bassa**; Medio e Lungo invariati. Opzione 1 e rischi sono stati aggiornati al testo vigente (soglia 42%, 70 seggi di premio alla Camera).
- **Proposta 5 (Cooperazione che si misura)**: costi confermati (0,7% = 9,1 mld; +0,45 mld/anno; +4,5 mld al 2035 a RNL costante). Due correzioni nella diagnosi: (a) la media DAC è 0,26%, non ~0,4%, quindi l'Italia nel 2025 è sopra la media ponderata, ma solo per i tagli degli altri donatori; (b) la quota per i rifugiati è scesa al 18,5% (dal 26,5%). La motivazione dell'opzione 1 è stata riformulata, senza cambiare la scelta. **Punteggi invariati.** La "credibilità internazionale" del medio periodo (+1) pesa un po' meno, ma non abbastanza da cambiare il punteggio. Coperture invariate.
- **Proposta 4 (Beni pubblici europei)**: quota italiana del RNL UE corretta al 12,0% (dal 12–13%): effetto trascurabile sull'ordine di grandezza del contributo. Il nuovo dato sul saldo netto (contributore netto sul QFP per 2,5–4,1 mld/anno, beneficiario netto con NGEU) rafforza la diagnosi B.3: dal 2028 finisce NGEU e comincia il rimborso. La richiesta SAFE ridotta a ~8 mld (dal tetto di 14,9) conferma che SAFE è usato come prestito nazionale e non come bene pubblico comune (B.4). **Punteggi invariati.**
- **Proposta 1 (Consulenza algoritmica pubblica)**: confermati l'adozione del Reg. (UE) 2026/1744 e le date di rinvio, ed è in vigore il D.Lgs. 179/2026 sui poteri delle autorità nazionali. Nessun impatto su punteggi o costi. Il costo (30–60 mln) resta stima GovernAI, ora etichettata come tale.
- **Proposte 2 e 6**: nessuna cifra corretta; costi rietichettati "stima GovernAI". Punteggi invariati.
- **Diagnosi B.3**: il debito è al 136,7% (non ~135%). Il dato rafforza l'argomento del dossier, senza effetti sui punteggi.
