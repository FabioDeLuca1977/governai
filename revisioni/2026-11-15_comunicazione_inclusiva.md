*Scritto da un agente AI con il ruolo di esperto di comunicazione inclusiva; non rivisto da una persona.*

# Revisione della comunicazione inclusiva e accessibile

*15 novembre 2026. Ambito: Osservatorio (`osservatorio/`), home e pagine principali (`docs/app.js`), `21_idee_in_sintesi.md`, `22_programma_in_una_pagina.md`, `programma/profili.yaml`, comunità (`comunita/regole.md`, `docs/comunita.js`). Nessun file modificato. Non ripete la revisione del 9 novembre (`revisioni/2026-11-09_linguaggio_inclusivo.md`).*

## 1. Giudizio sintetico

- Le correzioni del 9 novembre reggono: in `app.js`, `21` e `22` non tornano "disabili", "badanti", "i più deboli", e le sigle principali sono sciolte.
- Le parti nuove sono scritte in un registro più tecnico. L'Osservatorio e la comunità usano spesso il maschile generico ("lavoratori", "iscritti", "moderatori") e molte sigle senza spiegazione.
- Il tono è super partes: nessun aggettivo polemico, e lo schema "bene / non bene" è equilibrato. Due regole però escludono qualcuno ("chi vota", "ogni cittadino").
- L'accessibilità grafica è buona (forme oltre ai colori, testi per lettori di schermo). Ci sono due difetti: le caselle delle coperture si leggono solo dal colore, e la striscia dei valori nasconde i giudizi misti.
- Il problema principale per chi ha poca scolarità è la quantità di gergo interno ("nucleo robusto", "coperture", "versione essenziale", codici come SAD13) già in home e in "Che cosa cambia per me".

## 2. I problemi più importanti

**1. La striscia dei valori nasconde i giudizi misti** (`docs/app.js`, `strisciaValori()` riga 857 e matrice in `quadroValori()`; contatore a riga 923)
- Oggi: `Object.fromEntries(...)` tiene solo l'ultimo segno. In 11 atti su 21 un valore ha sia "+" sia "−" (per esempio FUT ed EQU nelle pensioni), ma la casella ne mostra uno solo. Il testo "non toccati" calcola `D.valori.length - val.length`: per le pensioni scrive 3, ma i valori non toccati sono 5.
- Proposta: un segno "misto" (casella metà e metà, etichetta "in parte a favore, in parte contro"); contare i valori distinti.
- Motivo: chi legge solo la grafica riceve un giudizio più netto di quello scritto, a volte più negativo e a volte più positivo. È un rischio per l'imparzialità.

**2. Il criterio "chi vota" esclude delle persone** (`osservatorio/metodo.md:12`)
- Oggi: "Il criterio è il benessere di chi vota."
- Proposta: "Il criterio è il benessere delle persone che vivono in Italia, anche di chi non vota, e di chi verrà dopo."
- Motivo: chi è minorenne o è residente straniero non vota. Lo stesso vale per le generazioni future, che il valore FUT vuole proteggere.

**3. "Ogni cittadino curioso"** (`comunita/regole.md:9`, `docs/comunita.js:114`)
- Oggi: "La comunità è aperta a ogni cittadino curioso."
- Proposta: "Può chiedere di entrare chiunque voglia capire e migliorare il programma, con o senza cittadinanza italiana."
- Motivo: il maschile esclude le donne e "cittadino" esclude chi vive in Italia senza cittadinanza. In più la frase dice "aperta" proprio prima di "su invito", e le due cose si contraddicono.

**4. Maschile generico nella comunità** (`comunita/regole.md:10-12, 29-37`; `docs/comunita.js:149, 151, 188, 197, 216, 230, 289, 339`; `docs/app.js:93, 954`)
- Oggi: "iscritto", "un moderatore", "Non sei iscritto?", "Tu sei entrato", "già collegato", "Se non sei sicuro".
- Proposta: "persona iscritta" o "chi è iscritto alla comunità"; "chi modera", "il gruppo di moderazione"; "Non hai ancora un account?"; "Ti ha invitato…"; "tornerai qui con l'accesso già fatto"; "Se hai dubbi, dillo". Titolo della sezione: "Discussione della comunità su questo atto".
- Motivo: sono messaggi rivolti a una sola persona ("tu"). Il maschile qui si nota più che in un testo tecnico, e la forma neutra non appesantisce.

**5. Maschile generico e "i non autosufficienti" nell'Osservatorio** (`osservatorio/atti/*.yaml`)
- Oggi: "i lavoratori dell'indotto" (`dl-2026-185-ex-ilva.yaml:14, 68, 81, 91`); "Medici e infermieri del pronto soccorso" (`manovra-2027-sanita-fondo-e-personale.yaml:51`); "giovani ricercatori" (`manovra-2027-scuola-universita.yaml:29, 83`); "Dipendenti pubblici", "contribuenti", "beneficiari" in molti file; "la prestazione per i non autosufficienti" (`manovra-2027-pensioni-e-anziani.yaml:87, 100`).
- Proposta: "chi lavora nell'indotto"; "il personale medico e infermieristico del pronto soccorso"; "ricercatrici e ricercatori all'inizio della carriera"; "il personale pubblico"; "chi paga le tasse"; "persone che ricevono l'aiuto"; "le persone non autosufficienti".
- Motivo: sono le regole già adottate in `23_equita_e_linguaggio.md`, e lo stesso file le applica solo in parte (riga 56 sì, riga 68 no).

**6. Le persone come costo** (`manovra-2027-lavoro-giovani-e-madri.yaml:30`)
- Oggi: "deducono l'80% in più del costo delle madri neoassunte".
- Proposta: "deducono l'80% in più del costo del lavoro quando assumono una madre".
- Motivo: la frase fa delle persone un costo. Il dato resta identico.

**7. Sigle e termini tecnici non spiegati nell'Osservatorio** (`osservatorio/atti/*.yaml`; glossario in `docs/app.js:1295`)
- Oggi: nei 21 atti compaiono DL e DDL, DPB, DPFP, IRAP, IRES, ARERA, TPL, APE, TFUE, ATA, AWP, VLT, TTF, GSE, ZES, oltre a "payback", "relazione tecnica", "clausola nazionale", "ripiano", "monte pensioni" e "calcolo attuariale". Il glossario ha 24 voci: mancano ISEE, IRPEF, IVA, LEP, PNRR, "copertura", "decreto-legge", "accisa", "detrazione".
- Proposta: sciogliere ogni sigla la prima volta che compare in un atto, per esempio "APE sociale, l'anticipo della pensione per chi è in difficoltà". Aggiungere queste voci al glossario. Poi collegare in automatico la prima occorrenza di ogni termine alla sua voce.
- Motivo: chi legge in italiano come seconda lingua non può cercare il significato di una sigla.

**8. Frasi e blocchi troppo lunghi** (`osservatorio/atti/*.yaml`, campi `in_breve` e `rischi_giuridici`)
- Oggi: nei riquadri "In 30 secondi" 14 frasi su 58 superano le 25 parole. I testi sui rischi giuridici arrivano a circa 1.900 caratteri in un solo paragrafo (`dl-2026-190-sicurezza-minori.yaml:63`; `dl-2026-185-ex-ilva.yaml:68`; `legge-2026-180-elettorale.yaml:70`).
- Proposta: "In 30 secondi" con al massimo 3 frasi di 20 parole. "Rischi giuridici" con una prima riga "In breve: rischio basso / medio / alto, perché…", seguita dal dettaglio in un elenco.
- Motivo: è la regola 6 di `23_equita_e_linguaggio.md`, e oggi la rispettano il programma ma non l'Osservatorio.

**9. "Che cosa ti può costare" ha per titolo un codice** (`docs/app.js:811`, funzione `perMe()`)
- Oggi: `<strong>${esc(x.copertura)}</strong>`, cioè il titolo della voce è "SAD13", "RB02" o "PE04".
- Proposta: usare la descrizione breve della copertura come titolo, per esempio "Meno sconto sul gasolio agricolo", e spostare il codice nella nota.
- Motivo: la pagina più vicina a chi legge usa la lingua interna del modello. Anche "Versione essenziale", "Pilota" e "Solo in prova" andrebbero spiegati in una legenda in alto nella pagina.

**10. Mancano dei profili** (`programma/profili.yaml`)
- Oggi: ci sono 8 profili, compreso uno per chi ha una "pensione alta". Non c'è un profilo per chi lavora da dipendente con un salario basso, per chi vive in affitto, per chi è in povertà e per chi ha una cittadinanza straniera.
- Proposta: aggiungere "Chi lavora con un salario basso", "Chi vive in affitto", "Famiglia con redditi bassi" e "Persona straniera che vive in Italia", anche quando la risposta onesta è "oggi il programma fa poco".
- Motivo: equilibrio di attenzione. Così non sembra che il programma parli soprattutto a chi ha qualcosa da perdere.

**11. Le caselle delle coperture si leggono solo dal colore** (`docs/app.js:642`, `docs/style.css:449-451`)
- Oggi: le caselle "Effetto sui valori" sono quadrati di 8 pixel, verdi o rossi, senza una forma che li distingua. Anche la colonna "Fondo" mostra codici come `SPESE_FISCALI` e `SAD`.
- Proposta: usare i triangoli già usati nell'Osservatorio (`.sv`) e scrivere il nome del fondo per esteso, per esempio "Sussidi dannosi per l'ambiente (SAD)".
- Motivo: chi non distingue il rosso dal verde non legge il dato. Il testo per i lettori di schermo c'è già.

**12. Home: il gergo arriva prima delle risposte** (`docs/app.js`, `home()` righe 390, 395, 404, 440, 448)
- Oggi: "nucleo robusto", "prima metà nel 87% dei casi", "Registro integro · N versioni", "impronta crittografica", "deroghe dichiarate", "obiezioni dell'opposizione leale". Tra i pulsanti in alto manca "Che cosa cambia per me".
- Proposta: mettere come primo pulsante "Che cosa cambia per me". Scrivere "Le proposte più solide: restano tra le prime qualunque peso si dia ai valori" e "Dati controllati: nessuna modifica nascosta".
- Motivo: chi arriva per la prima volta deve trovare subito la propria domanda. Il gergo del metodo può stare nelle pagine "Metodo" e "Governo".

**13. La pagina "in 10 minuti" è piena di gergo** (`21_idee_in_sintesi.md`, righe 18, 23, 44, 53-57, 95)
- Oggi: "Housing First", "modello americano SBIR", "Fraunhofer", "patent box", "fondo di fondi deep tech", "spin-off", "coperture regressive". La riga 18 è una frase di oltre 100 parole e racconta la cronologia delle verifiche ("la sera del 13 novembre").
- Proposta: spiegare ogni termine in parole comuni, per esempio "prima una casa stabile, poi il resto (Housing First)" e "uno sconto fiscale sui brevetti (patent box)". Spostare la cronologia in una nota "Che cosa è cambiato".
- Motivo: la pagina promette una lettura di dieci minuti a chiunque.

**14. Link e navigazione** (`docs/comunita.js:177, 119, 206`; `docs/index.html:33, 66`)
- Oggi: "clicca il link nell'email… Valgono un'ora". Nei moduli i link con `target="_blank"` non avvisano che si apre una nuova scheda. La stessa sezione si chiama "Osservatorio" nel menu in alto e "Atti" nel menu su telefono.
- Proposta: "apri il link nell'email. Il codice e il link valgono un'ora". Usare la funzione `ext()`, che aggiunge l'avviso, oppure aprire l'informativa nella stessa pagina. Usare un solo nome per la sezione, per esempio "Atti del governo".
- Motivo: "clicca" esclude chi usa la tastiera o il tocco. La parola "valgono" senza soggetto è ambigua. Due nomi diversi per la stessa sezione confondono, soprattutto chi ha difficoltà cognitive.

**15. Parole che giudicano i territori e le scelte di famiglia** (`manovra-2027-comuni-debiti-avanzo.yaml:64`; `profili.yaml:13`; `22_programma_in_una_pagina.md:28, 53`)
- Oggi: "Comuni in crisi, che sono spesso al Sud e hanno servizi deboli… chi è stato virtuoso". Per il congedo si usano tre nomi diversi: "congedo del papà", "congedo papà" e "congedo paterno".
- Proposta: "Comuni con forti debiti, molti nel Mezzogiorno, dove i servizi sono più scarsi… i Comuni con i conti in ordine". Usare sempre "congedo di paternità", il nome della legge. Se estenderlo al secondo genitore è una scelta politica: la segnalo, ma non la prendo.
- Motivo: "virtuoso" dà un giudizio morale. Il Sud va descritto con dati, non come un'etichetta.

## 3. Regole di stile da aggiungere a `23_equita_e_linguaggio.md`

1. **I codici non fanno da titolo.** Codici come 02-C2, SAD13 o FUT stanno nella nota, mai nel titolo o all'inizio della riga. Il titolo dice che cosa cambia.
2. **Una sigla si spiega in ogni pagina.** Si scioglie la prima volta che compare in ogni pagina o atto, non solo nel documento principale. Una sigla nuova entra anche nel glossario.
3. **"In 30 secondi" ha un tetto.** Al massimo 3 frasi di 20 parole, senza sigle e con un solo numero per frase.
4. **I gruppi si nominano con le persone.** Si scrive "chi lavora nell'indotto", "il personale medico e infermieristico", "le persone non autosufficienti". Questo vale anche per i campi `chi_guadagna` e `chi_paga`.
5. **Le persone non sono un costo.** Si scrive "il costo del lavoro", "la spesa per l'assistenza", mai "il costo delle madri" o "il peso dei pensionati".
6. **La platea è chi vive in Italia.** Si scrive "le persone che vivono in Italia", non "i cittadini" o "chi vota", salvo quando il diritto riguarda davvero solo chi ha la cittadinanza, come il voto.
7. **Il significato non sta solo nel colore.** Ogni segno colorato ha anche una forma o un testo, e un giudizio misto si mostra come misto.
8. **I link dicono dove portano.** Niente "clicca" e niente "qui". Si scrive "apri", "vai a" o "leggi" seguito dal nome della pagina, e si avvisa quando il link apre una nuova scheda.

## 4. Che cosa funziona già bene

- **Osservatorio:** fatti e giudizio sono separati, "chi ci guadagna / chi paga" vale per tutte le categorie, i difetti di GovernAI sono dichiarati e il tono è privo di polemica.
- **Persona prima della condizione:** "persone anziane non autosufficienti", "alunne e alunni con disabilità". Il profilo sulla disabilità dice i limiti in modo onesto e senza pietismo.
- **Profili:** ISEE, INPS, RSA, CPIA, ITS e PNRR sono spiegate nel testo.
- **Accessibilità tecnica:** link "Salta al contenuto", `lang="it"`, grafici con testo per i lettori di schermo, forme oltre ai colori nella striscia dei valori, avviso nei link esterni, tema scuro.
- **Sincerità:** ogni testo dice se è stato scritto da un agente AI e non rivisto. La pagina "per me" dichiara che manca la microsimulazione.
- **Comunità:** si modera il comportamento e non le opinioni, ogni decisione ha un motivo scritto e si può riesaminare, ed è ammesso lo pseudonimo.
