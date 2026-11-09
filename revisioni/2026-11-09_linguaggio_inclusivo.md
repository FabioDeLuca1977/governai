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
- **Assemblea civica** (`varianti/08_esteri.csv`, `schede/08_esteri.md`): l'istituto proposto si chiamava "Assemblea dei cittadini sui valori". Il 9 novembre 2026, su richiesta di chi guida il progetto, è stato rinominato "Assemblea civica sui valori" in tutti i file sorgente; nel testo discorsivo è "assemblea civica di persone sorteggiate".

## Seconda revisione: maschile generico e stereotipi

*Data: 9 novembre 2026. Richiesta di chi guida il progetto: "Cambia tutto ciò che potrebbe sembrare maschilista o potrebbe sembrare poco equo". La prima revisione lasciava molti maschili generici. Questa li corregge anche nei testi tecnici, nelle tabelle e negli articolati di legge proposti. Perimetro: interfaccia, documenti principali, schede, CSV e YAML del programma, controlli giuridici, dati, benchmark, design e stringhe pubbliche nel codice Python. Sono rimasti fuori, perché ci lavorava un'altra persona: Carta, rubrica, punteggi, `governo/`, `revisioni/` e `ministeri/`.*

### Metodo e regole aggiunte

- Ogni modifica è una sostituzione puntuale: il testo di contesto doveva comparire esattamente il numero di volte previsto. Non ci sono state sostituzioni globali. Nei CSV sono state toccate solo le colonne di testo ammesse, sul testo grezzo e senza riscrivere i file con pandas. Righe, colonne e celle delle altre colonne sono rimaste identiche.
- **Gerarchia delle forme**: prima le forme collettive e le perifrasi ("chi lavora", "chi possiede case", "il personale docente", "la popolazione studentesca", "la cittadinanza", "le persone idonee"); poi le forme doppie, ma solo dove servono e al massimo una per frase ("alunne e alunni", "cittadine e cittadini sorteggiati"). Niente schwa né asterischi.
- **Articolati di legge proposti**: anche qui si usano le forme neutre del linguaggio amministrativo, come raccomandano le linee guida per gli atti. Esempi: "ogni persona con rapporto di lavoro subordinato", "chi è titolare dell'indennità", "le elettrici e gli elettori", "il personale docente con funzione di tutor", "le persone detenute".
- **Stereotipi**: i nomi riferiti a un solo genere restano solo se la misura riguarda davvero quel genere ("congedo dei padri", "bonus lavoratrici madri", tasso di occupazione delle donne o degli uomini). "Bonus mamme" è stato ricondotto al nome ufficiale "bonus lavoratrici madri".
- **Titoli delle proposte**: cinque titoli sono stati cambiati in `motore/proposte.csv` (in ASCII), nelle intestazioni delle schede e nei rimandi dei documenti. I blocchi generati sono stati rigenerati con `programma/documento.py`.

### Correzioni per file (898 in tutto)

| Gruppo | File | Correzioni |
|---|---|---:|
| Interfaccia | `docs/app.js` | 3 |
| | `docs/index.html` | 0 |
| Documenti principali | `21_idee_in_sintesi.md` | 14 |
| | `23_equita_e_linguaggio.md` | 12 |
| | `10_sintesi_coordinatore.md` | 7 |
| | `20_programma_governai.md` (fuori dai blocchi generati) | 4 |
| | `00_metodo.md` | 2 |
| | `README.md` | 1 |
| | `CONTRIBUTING.md` | 0 |
| Titoli e obiettivi | `motore/proposte.csv` (titoli) | 5 |
| | `programma/schema.yaml` | 4 |
| | `apprendimento/obiettivi.yaml` (campo `nome`) | 10 |
| Schede | `01_economia` 17 · `02_lavoro` 28 · `03_ambiente` 9 · `04_infrastrutture` 14 · `05_istruzione` 92 · `06_salute` 45 · `07_giustizia` 22 · `08_esteri` 14 · `09_pa_digitale` 25 · `10_fisco_semplice` 22 · `11_evasione` 18 · `12_pa_produttiva` 30 · `13_integrita` 4 | 340 |
| Coperture e varianti | `coperture_menu.csv` 80 · `coperture_menu.md` 7 · varianti: `01` 9, `02` 17, `03` 4, `04` 3, `05` 47, `06` 25, `07` 6, `08` 5, `09` 5, `10` 6, `11` 6, `12` 1, `13` 0 | 221 |
| Altri file del programma | `coperture_personale.md` 15 · `motore/README.md` 1 · `registro/fondi.csv` 1 · `programma/README.md`, `apprendimento/lezioni.md`, `registro/README.md` 0 | 17 |
| Controlli giuridici | `giuridico/conformita.csv` 43, più le stesse 43 nei file parziali da cui è unito (COS 9, UE 12, FIS 6, COS_nuove 6, NE 5, UE_nuove 3, RI_LG 1, FIS_nuove 1) · `giuridico/*.md` 8 | 94 |
| Costituzione, trasparenza, legislazione | `costituzione/esami/AC3174_manovra_2027.md` 4 · `trasparenza/` 7 · `legislazione/README.md` 1 | 12 |
| Dati, benchmark, design, analisi | `dati/verifiche/` 50 · `benchmark/` 73 · `design/` 22 · `analisi/richieste/README.md` 1 | 146 |
| Codice Python (solo testo) | `motore/decidi.py` 2 · `apprendimento/aggiorna_obi.py` 2 · `programma/ottimizza.py` 1 (commento) · `sistema/analizza_richiesta.py` 1 (docstring) | 6 |

### Titoli cambiati

| Codice | Prima | Dopo |
|---|---|---|
| 01-P7 | Dichiarazione zero: lo Stato fa il conto, il cittadino controlla | Dichiarazione zero: lo Stato fa il conto, chi dichiara controlla |
| 04-P3 | Prima il treno dei pendolari: fondo TPL e abbonamento unico | Prima il treno di chi viaggia ogni giorno: fondo TPL e abbonamento unico |
| 05-C1 | Nessuno escluso: squadre di prossimità contro la dispersione | Nessuna esclusione: squadre di prossimità contro la dispersione |
| 05-C4 | Più laureati e diplomati terziari: ITS, lauree professionalizzanti, residenze | Più persone con laurea o diploma terziario: ITS, lauree professionalizzanti, residenze |
| 09-C3 | Tecnici della Repubblica: pool di competenze per i piccoli enti | Squadre tecniche della Repubblica: pool di competenze per i piccoli enti (cambia anche il nome del ruolo unico nell'articolato e nella variante) |

### Esempi prima e dopo

| # | File | Prima | Dopo |
|---|---|---|---|
| 1 | `docs/app.js` | un membro del progetto legge ogni richiesta | una persona del progetto legge ogni richiesta |
| 2 | `21_idee_in_sintesi.md` | proprietari di case di valore alto; locatori a canone libero; […] consumatori di gas | chi possiede case di valore alto; chi affitta case a canone libero; […] chi consuma gas |
| 3 | `21_idee_in_sintesi.md` | Quattro esperti di aree diverse […] hanno letto il programma | Quattro revisioni da aree diverse […] hanno esaminato il programma |
| 4 | `10_sintesi_coordinatore.md` | Decisioni che spettano agli umani | Decisioni che spettano alle persone |
| 5 | `schede/02_lavoro.md`, Art. 4 | tre rappresentanti dei lavoratori, tre dei datori di lavoro e tre esperti indipendenti | tre rappresentanti delle lavoratrici e dei lavoratori, tre delle parti datoriali e tre componenti indipendenti di comprovata competenza |
| 6 | `schede/05_istruzione.md`, Art. 1 | a tutti gli studenti idonei | a tutta la popolazione studentesca idonea |
| 7 | `schede/06_salute.md` | pazienti cronici in carico | persone con malattie croniche in carico |
| 8 | `schede/07_giustizia.md` | Un detenuto costa circa 178 € al giorno | Ogni persona detenuta costa circa 178 € al giorno |
| 9 | `schede/12_pa_produttiva.md`, Art. 2 | definito dal dirigente con il dipendente, che può farsi assistere da un rappresentante sindacale | definito dalla dirigenza con la persona interessata, che può farsi assistere da una rappresentanza sindacale |
| 10 | `coperture_menu.md` (SF06) | salvi cronici e disabili | salve le persone con malattie croniche o con disabilità |
| 11 | `coperture_menu.csv` | Consumatori di bevande zuccherate; circa 10 mln di fumatori | Chi consuma bevande zuccherate; circa 10 mln di persone che fumano |
| 12 | `varianti/08_esteri.csv` (08-P3) | Voto fuorisede strutturale per studenti, lavoratori e persone in cura | Voto fuorisede strutturale per chi studia, lavora o si cura lontano da casa |
| 13 | `giuridico/conformita*.csv` (06-C4) | la differenza tra vecchi e nuovi beneficiari | la differenza tra chi già riceve la prestazione e chi vi accede dopo |
| 14 | `trasparenza/README.md` | Nessun punteggio è attribuito a dipendenti, dirigenti, imprenditori o professionisti. | Nessun punteggio è attribuito a singole persone: personale dipendente, dirigenza, chi fa impresa o esercita una professione. |
| 15 | `obiettivi.yaml` e `schede/06_salute.md` | Infermieri praticanti per 1.000 abitanti; Rapporto infermieri/medici | Personale infermieristico in attività per 1.000 abitanti; Rapporto tra personale infermieristico e medico |
| 16 | `design/01_brief.md` | Cittadino curioso / Esperto o giornalista | Persona curiosa / Pubblico esperto (anche giornalistico) |

### Lasciato consapevolmente

- **Nomi ufficiali, citazioni e indicatori citati come tali**: "Osservatorio sui lavoratori pubblici" (INPS), "Convenzione europea dei diritti dell'uomo", "lavoratori svantaggiati" (categoria del GBER), "infermiere di famiglia e comunità" (DM 77), "Statuto del contribuente", "bonus lavoratrici madri", "Bonus nuovi nati", il congedo di paternità, i titoli ufficiali di atti UE e della Gazzetta, i passaggi "Testo:" degli esami costituzionali e le raccomandazioni del Consiglio UE in `europa/semestre.md`. Il "Garante nazionale dei detenuti" è stato reso con il nome ufficiale: "Garante nazionale dei diritti delle persone private della libertà personale".
- **Termini giuridici neutri o riferiti a imprese ed enti**: "minori", "contribuenti" negli articolati fiscali, "operatori economici", "clienti finali" (ARERA), "fornitori", "Comuni beneficiari". Restano anche i nomi epiceni senza articolo maschile, come "residenti", "docenti", "giovani" ed "eredi".
- **Ruoli degli agenti AI**: "esperti", "ministri", "valutatori", "coordinatore", "consigliere". Sono titoli di ruolo di agenti, non persone, e i nomi delle sezioni dei verbali vengono da `governo/`. Dove la frase si poteva riformulare senza toccare la logica, è stato fatto.
- **File generati da codice**: `costituzione/esami/governai/*.md`, `costituzione/esami/gu/*.md` e `AC3174_screening.md` li produce `costituzione/controllo.py` a partire da sintesi di sentenze e testi di legge. La riga di intestazione di `giuridico/quadro.md` ("redatta dagli esperti…") viene da `giuridico/unisci.py`.
- **Campo `unita` di `obiettivi.yaml`** ("% alunni", "laureati/anno", "elettori", "detenuti"): fuori dal perimetro, che comprendeva solo il campo `nome`. Si propone di allinearlo ("% alunne e alunni", "persone laureate/anno", "persone detenute").
- **Disegni ASCII in `design/03_schermate.md`**: contengono ancora "il cittadino controlla" e "Nessuno escluso". Cambiarli romperebbe l'allineamento dei riquadri: vanno ridisegnati.
- **File derivati non nel perimetro**: `programma/selezione_*.md/csv`, `motore/esito*.{md,csv}`, `registro/prelievi.csv` e `registro/bilancio.md` portano ancora i vecchi titoli e il vecchio nome "Tecnici della Repubblica". Per questo il sito li mostra ancora in alcuni punti, perché `esporta_web.py` legge anche questi file. Si allineano alla prossima esecuzione di motore, ottimizzatore e registro.
- **Scelta fatta da chi guida il progetto**: l'istituto di 08-P1 si chiama ora "Assemblea civica sui valori" (prima "Assemblea dei cittadini sui valori"), in tutti i file sorgente.

### Verifiche

- I CSV si rileggono con pandas con le stesse dimensioni: `proposte.csv` 75×5, `coperture_menu.csv` 71×23, `fondi.csv` 18×10, varianti con 13 colonne, `conformita*.csv` con 8 colonne. I YAML si rileggono.
- `node --check docs/app.js`: ok. `python -m py_compile` sui quattro file Python modificati: ok.
- `python -I registro/controlla.py`: 0 avvisi.
- `python programma/documento.py`, poi `--controlla`: uscita 0. Sono stati rigenerati `20_programma_governai.md` e `22_programma_in_una_pagina.md`.
- `python sistema/esporta_web.py`: 75 proposte e 6 scenari, senza errori.

## Seconda revisione: Carta, panel, governo ombra, rapporti e dossier

*Data: 9 novembre 2026. Su autorizzazione esplicita di chi guida il progetto ("Cambia tutto ciò che potrebbe sembrare maschilista o potrebbe sembrare poco equo"), la revisione si estende ai file che la prima revisione aveva soltanto segnalato: `01_carta_valori.md`, `motore/rubrica.md`, `motore/punteggi_*.csv` (solo la colonna `motivazione`), `governo/`, `revisioni/` e `ministeri/`. Non sono cambiati codici, numeri, punteggi, confidenze, linee rosse, regole né il significato dei testi.*

### Metodo

- **Carta e rubrica**: 18 correzioni scritte a mano, una per una. Le definizioni restano le stesse nella sostanza, i titoli `### N. Nome (XXX)` sono intatti e il sito li legge come prima.
- **Gli altri file**: una riscrittura controllata con regole di contesto. Ogni sostituzione è stata registrata, rivista e, dove serviva, corretta a mano: accordo degli aggettivi, articoli, usi aggettivali.
- **Tre famiglie di regole**:
  - forme doppie per i nomi di persona marcati al maschile ("le lavoratrici e i lavoratori", "studentesse e studenti", "ricercatrici e ricercatori", "infermiere e infermieri", "mediche e medici", "alunne e alunni", "bambine e bambini", "ragazze e ragazzi", "inquiline e inquilini", "proprietarie e proprietari", "consumatrici e consumatori", "funzionarie e funzionari"; "esperte ed esperti" solo fuori da `governo/`);
  - "la cittadinanza" al posto di "i cittadini" quando la frase lo consente;
  - "persone + condizione" ("persone anziane", "persone detenute", "persone laureate", "persone occupate", "persone disoccupate", "persone in pensione", "persone con disabilità", "persone con malattie croniche") e la sostituzione dei termini stigmatizzanti ("i più deboli", "disabili", "badanti", "ex detenuti", "scarcerati", "malati cronici", "grandi anziani", "meno istruiti").
- **Usi aggettivali**: per esempio "posti nido occupati", "modelli proprietari", "ordini medici" e "lavoratori anziani". Sono stati lasciati o sistemati a mano: "lavoratori anziani", per esempio, è diventato "lavoratrici e lavoratori anziani".
- **Struttura dei verbali** (`governo/verbali/*.md`): titoli `##`/`###`, tabelle delle decisioni, prefissi delle righe ("- Prova:", "- Risposta del capo:", "- M001 — …, entro il …:", "**Previsioni registrate:**", "**Motivo della convocazione.**") e titoli in grassetto delle obiezioni sono identici a prima (verificato con un confronto automatico). È cambiato solo il testo libero.
- **Sorgenti JSON dei verbali**: le stesse correzioni sono state applicate ai sorgenti JSON (`governo/verbali/*.json`, `capo.json` e `contesto.json` delle sedute), così una nuova composizione del verbale non le annulla. Le chiavi e i valori usati come identificativi (autore, id, seduta, area, proposta, variante, indicatore) non sono stati toccati.
- **Nota in calce**: aggiunta in fondo ai due verbali e ai sei rapporti firmati del 2026-11-08.
- **Protetti**: nomi ufficiali, titoli di fonti e indicatori ("Consiglio dei ministri", "Garante nazionale dei detenuti", "Osservatorio sui lavoratori pubblici", "Statuto dei lavoratori", "fiducia dei consumatori" dell'ISTAT, "infermieri di famiglia", "infermieri praticanti", "Occupati e disoccupati"); i titoli delle proposte registrati nei verbali; codice tra backtick; URL; citazioni tra «».

### Correzioni per file (circa 1.090)

| File | Correzioni |
|---|---:|
| `01_carta_valori.md` | 17 |
| `motore/rubrica.md` | 1 |
| `motore/punteggi_A.csv` · `_B` · `_C` (colonna `motivazione`) | 61 · 70 · 79 |
| `governo/verbali/2026-11-08.md` · `.json` | 44 · 48 |
| `governo/verbali/2026-11-08-1-conti-in-ordine.md` · `.json` | 44 · 49 |
| `governo/sedute/*/ordine_del_giorno.md` · `capo.json` · `contesto.json` | 4 · 6 · 6 |
| `governo/mandati.csv` (colonna `compito`) · `governo/richieste/README.md` | 2 · 1 |
| `revisioni/2026-11-08_*` (sei rapporti) | 37 |
| `ministeri/` | 01: 7 · 02: 20 · 03: 6 · 04: 18 · 05: 58 · 06: 31 · 07: 19 · 08: 12 · 09: 23 |

### Esempi prima e dopo

| File | Prima | Dopo |
|---|---|---|
| `01_carta_valori.md` (EQU, linea rossa) | sposti i costi sui più deboli | sposti i costi sulle persone con redditi bassi o in condizioni di fragilità |
| `01_carta_valori.md` (CIT) | Cittadini protagonisti e non solo utenti o assistiti | Cittadine e cittadini protagonisti, non solo destinatari di servizi o di assistenza |
| `01_carta_valori.md` (RIS) | o solo per il cittadino "medio"? […] senza umiliarlo? | o solo per una persona "media"? […] senza umiliarne la dignità? |
| `01_carta_valori.md` (regola 4) | Valutatori indipendenti: […] almeno tre valutatori | Valutazione indipendente: […] almeno tre membri |
| `punteggi_B.csv` (07-C2) | Detenuti in larga parte poveri e stranieri | Persone detenute in larga parte povere e straniere |
| `punteggi_A.csv` (06-C4) | Spesa più mirata per i grandi anziani | Spesa più mirata per le persone molto anziane |
| `punteggi_C.csv` (06-C3) | Assistenza a anziani e cronici | Assistenza a persone anziane o con malattie croniche |
| `governo/verbali/2026-11-08-1-conti-in-ordine.md` | diritto allo studio dei disabili | diritto allo studio delle persone con disabilità |
| `governo/verbali/2026-11-08.md` | Più lavoro per detenuti ed ex detenuti | Più lavoro per persone detenute o che hanno scontato la pena |
| `revisioni/2026-11-08_red_team_centrosinistra.md` | accettabile ai nostri elettori | accettabile al nostro elettorato |
| `revisioni/2026-11-08_red_team_civico.md` | un sistema **per** i cittadini, non **dei** cittadini | un sistema **per** la cittadinanza, non **della** cittadinanza |
| `ministeri/06_salute.md` | servizi di qualità (badanti regolari, …) | servizi di qualità (assistenti familiari regolari, …) |
| `ministeri/07_giustizia_interno_difesa.md` | studio Leonardi 2007 su scarcerati 1998 | studio Leonardi 2007 su persone scarcerate nel 1998 |
| `ministeri/02_lavoro_welfare_famiglia.md` | anche se non ha figli o disabili in casa | anche se non ha figli o persone con disabilità in casa |

### Lasciato consapevolmente

- **Ruoli degli agenti AI** in `governo/`: "ministro", "esperto", "capo di governo", "opposizione". Sono nomi di ruolo usati dal codice (`ministro_01`, `esperto_*`, "Ministro · area" nell'interfaccia) e dai file `governo/ruoli/*.md`. Anche "Ministro della …" nei mandati resta, perché il sito lo legge come campo "chi".
- **Nomi epiceni** con articolo maschile ("i contribuenti", "i docenti", "gli utenti", "i residenti", "i giovani", "i pazienti", "i dipendenti"): per la Crusca (2023) sono accettabili, e la doppia forma solo dell'articolo appesantirebbe il testo. Lo stesso vale per "evasori", "operatori" e "beneficiari", che spesso indicano imprese o enti.
- **Righe di tabella dei verbali**: per esempio "dai pensionati con sola CU" e "esenta lavoratori UE". Restano come registrate, perché la consegna vietava di toccare le tabelle delle decisioni. Lo stesso vale per i vecchi titoli delle proposte registrati nei verbali.
- **JSON di posizioni, pareri e opposizione delle sedute** (`governo/sedute/*/posizioni/*.json`, `pareri/*.json`, `opposizione.json`, `sedute/2026-11-08/capo.json`): hanno una formattazione che non si può riscrivere identica, quindi sono stati lasciati com'erano per non alterarli. Sono atti di lavoro intermedi, non pubblicati. Le stesse frasi sono corrette nei verbali che il sito mostra.
- **Usi aggettivali e nomi di riforme**: "posti nido occupati", "modelli proprietari", "ordini medici", "riforma anziani" (nome giornalistico della L. 33/2023), "minori detenuti", "rapporto anziani/età lavorativa" (indicatore ISTAT di dipendenza).

### Verifiche della seconda revisione

- I CSV si rileggono con pandas con le stesse righe e colonne di prima: `punteggi_A/B/C.csv` 750×8, con le colonne diverse da `motivazione` identiche; `governo/mandati.csv` 19×7, con le colonne diverse da `compito` identiche; `credibilita.csv` e `previsioni.csv` invariati. Tutti i JSON di `governo/` e `esperti.yaml` si rileggono.
- `python motore/decidi.py`: alfa di Krippendorff 0,85. Le classi delle 75 proposte in `motore/esito_proposte.csv` sono identiche a git HEAD (0 differenze).
- `python sistema/esporta_web.py`: 75 proposte e 6 scenari, senza errori. `node --check docs/app.js`: ok.
