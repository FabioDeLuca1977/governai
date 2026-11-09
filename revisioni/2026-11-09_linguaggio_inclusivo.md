# Revisione del linguaggio inclusivo e chiaro del sito

*Data: 9 novembre 2026. Ambito: tutto il testo pubblicato in `docs/` (interfaccia e contenuti generati da `sistema/esporta_web.py`). Le correzioni sono state fatte nei file sorgente; `docs/data.js` è stato solo rigenerato.*

## Metodo

1. Dall'esportatore (`sistema/esporta_web.py`) si è ricavato l'elenco dei file che finiscono sul sito.
2. Ricerche mirate su due famiglie di termini:
   - **espressioni stigmatizzanti**: disabili, handicap, portatori di handicap, affetti da, clandestini, extracomunitari, nomadi, barboni, clochard, tossicodipendenti, malati mentali, badanti, "i più deboli", "i nostri anziani";
   - **maschile non marcato** per gruppi misti: cittadini, lavoratori, studenti, alunni, bambini, anziani, detenuti, pensionati, docenti, medici, infermieri, ricercatori, dipendenti, laureati, iscritti, idonei.
3. Ordine di priorità: interfaccia; programma in una pagina (`programma/schema.yaml`); documenti principali; titoli delle proposte; nomi degli obiettivi; schede, varianti e coperture; benchmark.
4. Il maschile non marcato è stato corretto dove la correzione è facile e non appesantisce: titoli, gruppi di destinatari, frasi rivolte al pubblico, nomi degli indicatori scritti da GovernAI. Non è stato corretto nei passaggi tecnici molto densi, negli articolati di legge proposti e nei nomi ufficiali.
5. Verifiche finali: `python -I registro/controlla.py` (0 avvisi), `python programma/documento.py` e poi `--controlla` (uscita 0; i blocchi generati di `20_programma_governai.md` e `22_programma_in_una_pagina.md` sono stati rigenerati per i due titoli cambiati), `python sistema/esporta_web.py` (75 proposte, 6 scenari, senza errori), `node --check docs/app.js` (ok). I CSV modificati si rileggono con pandas e i YAML con PyYAML senza errori.

## Regole applicate

Fonti: Linee guida per l'uso del genere nel linguaggio amministrativo (Robustelli, 2012); parere dell'Accademia della Crusca sulla scrittura rispettosa della parità di genere (2023); Convenzione ONU sui diritti delle persone con disabilità (L. 18/2009); Carta di Roma.

- **Genere**: prima le forme neutre e collettive (la cittadinanza, le persone, chi lavora, il personale, il personale docente o infermieristico, chi ha una pensione); poi le forme doppie (bambine e bambini, alunne e alunni, studentesse e studenti, ricercatrici e ricercatori). Niente schwa, asterischi o chiocciole.
- **Disabilità**: "persone con disabilità", mai "disabili" come sostantivo.
- **Origine**: "persone straniere", "di cittadinanza straniera", "di origine straniera".
- **Marginalità**: "persone detenute"; "assistenti familiari" invece di "badanti", salvo norme e voci citate alla lettera.
- **Età**: "persone anziane", "persone anziane non autosufficienti".
- **"I più deboli"**: sostituito dicendo chi sono, per esempio "persone con redditi bassi o in condizioni di fragilità" o "chi ha meno mezzi".
- **Chiarezza**: sigle sciolte alla prima occorrenza nella pagina del programma (ISEE, PNRR, RSA, PA); ISTAT e MEF aggiunti al glossario dell'interfaccia.
- **Non toccati**: nomi di norme e istituti (legge 104, invalidità civile, "Osservatorio sui lavoratori pubblici" dell'INPS, "Garante nazionale dei detenuti", infermieri di famiglia e comunità), indicatori Eurostat e ISTAT citati come tali, il pronome indefinito "nessuno", i blocchi `<!-- auto:... -->`, numeri e codici.

## Correzioni per file (120 in tutto)

| File | Correzioni | Note |
|---|---:|---|
| `docs/app.js` | 3 | 1 linguistica ("più deboli"); 2 voci nuove nel glossario (ISTAT, MEF). Toccate solo le stringhe, non la logica. |
| `docs/index.html` | 0 | Testo già conforme. |
| `programma/schema.yaml` | 37 | Pagina "Il programma in una pagina": gruppi di destinatari, perché e come, 4 sigle sciolte. |
| `21_idee_in_sintesi.md` | 5 | |
| `20_programma_governai.md` | 2 | Più le tabelle generate, aggiornate per i due titoli. |
| `motore/proposte.csv` | 2 | Titoli 03-P1 e 06-C2, in ASCII come da convenzione. |
| `programma/schede/06_salute.md` | 5 | Intestazione 06-C2, allineata al titolo; "badanti"; "anziani". |
| `programma/schede/12_pa_produttiva.md` | 4 | |
| `programma/schede/07_giustizia.md` | 3 | |
| `programma/schede/05_istruzione.md` | 2 | Incluso il titolo della scheda 05-C6. |
| `programma/schede/10_fisco_semplice.md` | 2 | |
| `programma/schede/02_lavoro.md` | 1 | |
| `programma/coperture_menu.csv` | 5 | Colonne descrizione, chi_paga e fonte_dato. |
| `programma/varianti/*.csv` | 26 | 04: 9; 06: 10; 10: 3; 03, 05, 07, 09: 1 ciascuno. |
| `apprendimento/obiettivi.yaml` | 17 | Solo il campo `nome`. |
| `benchmark/confronto.md` | 6 | Incluse due intestazioni di sezione. |

`00_metodo.md`, `README.md`, `CONTRIBUTING.md`, `sistema/README.md`, `giuridico/quadro.md`, `trasparenza/rapporto.md`, `europa/semestre.md`, `legislazione/README.md` e `apprendimento/lezioni.md` non contengono espressioni stigmatizzanti. In questi file il maschile non marcato residuo è raro e tecnico, quindi non è stato modificato.

## Esempi prima e dopo

| # | File | Prima | Dopo |
|---|---|---|---|
| 1 | `docs/app.js` | Le proposte che […] scaricano costi sui più deboli sono escluse | Le proposte che […] scaricano costi sulle persone con redditi bassi o in condizioni di fragilità sono escluse |
| 2 | `schema.yaml` (M2) | Nessuno deve rinunciare a curarsi o restare solo quando è fragile: malati, anziani non autosufficienti, persone con disabilità, chi vive in strada. | Nessuna persona deve rinunciare a curarsi o restare sola quando è fragile: chi ha una malattia, le persone anziane non autosufficienti, le persone con disabilità, chi vive in strada. |
| 3 | `schema.yaml` (M1) | Ogni bambino deve poter partire alla pari | Ogni bambina e ogni bambino deve poter partire alla pari |
| 4 | `schema.yaml` | Famiglie con bambini piccoli, studenti delle scuole più fragili, […] contribuenti | Famiglie con bambine e bambini piccoli, studentesse e studenti delle scuole più fragili, […] chi paga le tasse |
| 5 | `schema.yaml` | Lavoratori con salari bassi / il 10,2% degli occupati | Chi lavora con salari bassi / il 10,2% delle persone occupate |
| 6 | `schema.yaml` | 66.063 detenuti per 51.295 posti | 66.063 persone detenute per 51.295 posti |
| 7 | `schema.yaml` | indennità per circa 35.000 medici, infermieri e insegnanti | indennità per circa 35.000 persone tra personale medico, infermieristico e docente |
| 8 | `schema.yaml` | gratis fino a ISEE 25.000 € | gratis fino a un ISEE (indicatore della situazione economica equivalente) di 25.000 € |
| 9 | `motore/proposte.csv` | Dividendo climatico: riforma SAD restituita ai cittadini | Dividendo climatico: riforma SAD restituita alla cittadinanza |
| 10 | `motore/proposte.csv` e scheda | Patto per infermieri e medicina generale | Patto per il personale infermieristico e la medicina generale |
| 11 | `schede/02_lavoro.md` | anche senza figli, disabili o anziani in casa | anche senza figli, persone con disabilità o persone anziane in casa |
| 12 | `schede/06_salute.md` | agevolazioni per badanti e assistenza personale | agevolazioni per assistenti familiari e assistenza personale |
| 13 | `varianti/04_infrastrutture.csv` | trasporto scolastico disabili | trasporto scolastico di alunne e alunni con disabilità |
| 14 | `benchmark/confronto.md` | dovuto a lavoratori laureati immigrati | dovuto a lavoratrici e lavoratori laureati di origine straniera |
| 15 | `obiettivi.yaml` | Idonei non beneficiari / Laureati e diplomati terziari 25-34 | Persone idonee alla borsa ma senza borsa / Persone di 25-34 anni con titolo terziario |

## Espressioni segnalate ma non corrette (file esclusi)

Questi file sono atti registrati o strati che l'AI non modifica. Le espressioni sono segnalate perché le valuti chi guida il progetto. I numeri di riga si riferiscono alla data di questa revisione.

### Carta, rubrica e punteggi del panel

| File:riga | Espressione | Proposta |
|---|---|---|
| `01_carta_valori.md:68` | "sposti i costi sui più deboli" (linea rossa EQU) | "sulle persone con redditi bassi o in condizioni di fragilità" o "su chi ha meno mezzi". È la fonte da cui la stessa formula passa nei verbali, in `legislazione/istruzioni_revisione.md:72` e in `programma/ottimizza.py:155` (commento). |
| `01_carta_valori.md:61` | "indice di dipendenza degli anziani" | Nome di un indicatore ISTAT: può restare. |
| `motore/rubrica.md` | nessuna espressione rilevata | — |
| `motore/punteggi_B.csv:459` | "il costo ricada sui più deboli" | come sopra |
| `motore/punteggi_B.csv:429` | "Detenuti in larga parte poveri e stranieri" | "Persone detenute in larga parte povere e straniere" |
| `motore/punteggi_A.csv:426, 429`; `punteggi_B.csv:425, 426`; `punteggi_C.csv:425, 426, 428` | "detenuti", "ex detenuti" | "persone detenute", "persone che hanno finito di scontare la pena" |
| `motore/punteggi_A.csv:145`; `punteggi_B.csv:308` | "lavoratori anziani" | "lavoratrici e lavoratori più anziani" |
| `motore/punteggi_A.csv:235, 252, 289, 372, 388, 585, 589, 669`; `punteggi_B.csv:92, 235, 252, 285, 382, 388, 585`; `punteggi_C.csv:235, 252, 289, 375, 379, 582, 585, 586, 589, 612` | "anziani", "grandi anziani", "anziani e cronici", "meno istruiti" | "persone anziane", "persone molto anziane", "persone anziane e con malattie croniche", "persone con meno istruzione" (priorità bassa: motivazioni brevi) |

### Verbali del governo ombra (`governo/verbali/`)

| File:riga | Espressione |
|---|---|
| `2026-11-08-1-conti-in-ordine.md:196` | "diritto allo studio dei disabili" (da preferire: "delle persone con disabilità") |
| `2026-11-08-1-conti-in-ordine.md:423`; `2026-11-08.md:9, 135, 162` | "costi sui più deboli" (riprende la Carta) |
| `2026-11-08-1-conti-in-ordine.md:501, 503, 510`; `2026-11-08.md:232, 239` | "detenuti", "ex detenuti" |
| `2026-11-08-1-conti-in-ordine.md:551` | "lavoratori anziani" |
| `2026-11-08.md:273` | "divario concentrato su anziani" |
| `2026-11-08.md:42, 54`; `2026-11-08-1-conti-in-ordine.md:61, 87` | Vecchi titoli di 03-P1 e 06-C2: restano come registrati. |

### Rapporti firmati (`revisioni/`)

| File:riga | Espressione |
|---|---|
| `2026-11-08_red_team_centrodestra.md:44` | "costi sui più deboli" (cita la Carta) |
| `2026-11-08_red_team_centrodestra.md:74` | "espulsione dei detenuti stranieri", "stranieri detenuti" (posizione simulata di parte; da preferire "persone detenute straniere") |

### Dossier storici (`ministeri/`)

| File:riga | Espressione |
|---|---|
| `02_lavoro_welfare_famiglia.md:39` | "(minori, disabili, over 60)", "i poveri" |
| `02_lavoro_welfare_famiglia.md:134` | "protegge i più deboli del contributivo" |
| `02_lavoro_welfare_famiglia.md:162` | "figli o disabili in casa" |
| `02_lavoro_welfare_famiglia.md:24, 271`; `04_infrastrutture_territori.md:75, 151, 264, 273`; `05_istruzione_ricerca_cultura.md:126`; `06_salute.md:81, 144, 160, 202, 204, 212`; `09_pa_digitale.md:47, 217` | "anziani", "grandi anziani", "lavoratori anziani", "malati cronici" (06_salute:160) |
| `03_ambiente_energia_agricoltura.md:78` | "reddito presente dei più deboli" |
| `06_salute.md:186` | "badanti regolari" (da preferire: "assistenti familiari con contratto regolare") |
| `07_giustizia_interno_difesa.md:24, 25, 91, 93, 102, 104, 249` | "detenuti", "ex detenuti", "minori detenuti" |
| `07_giustizia_interno_difesa.md:26` | "scarcerati" (da preferire: "persone uscite dal carcere") |

### Altri casi lasciati consapevolmente

- **Nomi ufficiali e citazioni**: "Prestazione universale" (D.Lgs. 29/2024), "Garante nazionale dei detenuti", "Osservatorio sui lavoratori pubblici" (INPS), "ricercatori PNRR", "infermieri di famiglia e comunità" (DM 77), il dato ISTAT "persone senza tetto o senza fissa dimora". Restano anche le voci di bilancio "assegno per i figli" e simili.
- **Articolati di legge proposti nelle schede** (righe che iniziano con `> **Art.`): per esempio "detenuti" in `schede/07_giustizia.md`, righe 87 e 89, e "studenti con disturbi specifici" in `schede/10_fisco_semplice.md:206`. Sono testi normativi che seguono lo stile legislativo vigente.
- **Ruoli del governo ombra** ("ministri", "esperti", "valutatori"): indicano agenti AI, non persone. Restano anche il nome istituzionale "Consiglio dei ministri" e il marchio della proposta 09-C3 "Tecnici della Repubblica". Chi guida il progetto può valutare "Tecniche e tecnici della Repubblica".
- **Slogan "Nessuno escluso" (05-C1)**: "nessuno" è un pronome indefinito di uso comune. Una formula alternativa è "Nessuna esclusione".
- **File derivati non pubblicati** che riportano ancora i vecchi titoli di 03-P1 e 06-C2: `motore/esito.md`, `motore/esito_proposte.csv`, `programma/selezione_*.md`, `registro/prelievi.csv`, `registro/bilancio.md`, `benchmark/programmi/servizi_pubblici.csv`. Si allineano alla prossima esecuzione del motore e del registro.
- **Assemblea dei cittadini** (`varianti/08_esteri.csv`, `schede/08_esteri.md`): è il nome dell'istituto proposto. Nel testo discorsivo dei documenti principali è stato reso con "assemblea di cittadine e cittadini sorteggiati". Si suggerisce di decidere un nome ufficiale unico, per esempio "Assemblea civica sui valori".
