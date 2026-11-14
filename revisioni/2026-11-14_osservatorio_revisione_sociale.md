# Revisione B dei 21 commenti dell'Osservatorio (sensibilità sociale e progressista)

*Revisione scritta da un agente AI a cui è stata data questa sensibilità politica, non da una persona. Le correzioni sono state applicate ai commenti di `osservatorio/atti/` da un altro agente AI, che ha scartato quelle non confermate dalle fonti.*

*14 novembre 2026. Revisore: agente AI. Nessun file del repository è stato modificato.*

## Giudizio d'insieme

1. **Equilibrio complessivo**: buono. Quasi ogni commento dice chi ci guadagna e chi paga, segnala i costi ambientali (bollo, autotrasporto, DL energia) e gli effetti regressivi (giochi, bollette, sanzioni fisse ai genitori). Il confronto con GovernAI è onesto e spesso autocritico.
2. **Punti forti**: numeri quasi sempre ripresi correttamente dalle relazioni tecniche e dai testi (verifica a campione su 25 dati: 23 esatti). Attenzione costante a persone con disabilità, Sud, servizi pubblici e generazioni future.
3. **Rischi di equilibrio**: alcuni passaggi riprendono la cornice del Governo senza vagliarla. Esempi: i Comuni in dissesto descritti come chi "ha accumulato debiti"; le "domande infondate" di gratuito patrocinio; la difesa definita "trasparente". In più, tre richieste attribuite ai sindacati non hanno fonte. Mancano quasi sempre i dati per genere e per territorio sulle misure fiscali maggiori.
4. **Rischi di fatto**: un correttivo chiede ciò che la legge già fa (pensioni, solo 2027). Una quota "libera" è contata tra quelle vincolate (sanità). Alcune descrizioni sono più dure del testo (trattenimento nel DL 190). C'è un numero di proroghe sbagliato (bingo), e la maggioranza della legge elettorale è chiamata "semplice". Dieci sentenze citate non sono nel file verificato.
5. **Linguaggio**: il giudizio entra già in `in_breve` in quattro commenti, contro la regola 1 del metodo. "Ennesima" o "ennesimo" compare sei volte. Restano maschili generici ("lavoratori", "giocatori", "ragazzi", "anziani") e alcune parole inglesi evitabili ("plastic e sugar tax", "over 75").

## Correzioni trasversali (valgono per più file)

- LINGUAGGIO | `in_breve` di dl-2026-185, dl-2026-190, dl-2026-205, legge-2026-180 | Contengono giudizi ("È un aiuto giusto", "Va nella giusta direzione", "Rafforza strumenti utili", "novità buone"). La regola 1 del metodo vuole prima i fatti e poi i valori | Spostare il giudizio in `bilancio`; in `in_breve` lasciare solo che cosa fa l'atto e i numeri.
- LINGUAGGIO | "ennesima/ennesimo/per l'ennesima volta" (dl-2026-185 `in_breve` e FID; manovra-giochi FID e `bilancio`; manovra-evasione `chi_guadagna` e FID) | Il tono è polemico (regola 6) | Usare il numero: "la sesta proroga", "il terzo rinvio", "un altro decreto sull'ex ILVA".
- FATTO | Sentenze non presenti in `costituzione/giurisprudenza_verificata.json`: 130/2023 (pensioni), 85/2013 e 58/2018 (ex ILVA), 168/1994, 263/2019 e 24/2019 (DL 190), 186/2013 (Campi Flegrei), 1/2014 e 35/2017 (legge elettorale) | Sono da verificare prima di pubblicare | Verificarle e aggiungerle al file, oppure scrivere "(sentenza da verificare)" accanto a ciascuna.
- EQUILIBRIO | Richieste attribuite a categorie senza fonte: "una misura cercata dai sindacati del pubblico impiego" (lavoro-giovani), "richiesta storica dei sindacati della dirigenza medica e del comparto" (sanità), "i loro ordini e associazioni chiedevano da tempo la soglia più alta" (IRPEF, forfettario) | La regola 7 chiede una fonte per ogni affermazione. Senza fonte, la frase attribuisce un interesse a un gruppo organizzato | Citare un documento (audizione, piattaforma contrattuale, comunicato) oppure togliere la frase. Trattare allo stesso modo sindacati e ordini professionali.
- EQUILIBRIO | Misure fiscali maggiori (IRPEF, bollo, imposta sulle azioni) | Non si dice a quali generi e territori vanno i benefici. Il metodo e il capitolo 23 chiedono di guardare a donne, Sud e giovani | Aggiungere una `domanda_aperta`: "Come si distribuisce il beneficio per genere e per area geografica? (statistiche MEF sulle dichiarazioni, da verificare)".

## Correzioni per file

### manovra-2027-pensioni-e-anziani.yaml
- FATTO | `cosa_cambieremmo` (2° punto) e `rischi_giuridici` ("va limitato per legge al solo 2027") | L'art. 55 dice già "Nell'anno 2027". L'effetto permanente viene dalla base più bassa negli anni successivi, non dalla durata della norma | Sostituire con: "Restituire in tutto o in parte, dal 2028, l'adeguamento perso nel 2027, così che il taglio non resti nella base per sempre." In `rischi_giuridici` togliere "va limitato per legge al solo 2027" e scrivere: "la norma vale per il 2027, ma l'effetto sulla base è permanente".
- FATTO | `chi_paga` (2° punto), `valori` EQU "-" e `cosa_cambieremmo` (1° punto) | L'art. 55 ha una clausola di salvaguardia: chi supera di poco una soglia riceve comunque l'aumento fino al limite maggiorato. Il "salto" quindi è attenuato e "perde molto più" esagera | Scrivere: "Chi ha un assegno sopra 5 volte il minimo ha il 53% di adeguamento su tutto l'importo; una clausola evita che superi di poco la soglia e resti sotto chi sta appena al di qua."
- FATTO | `chi_paga` (1° punto): "È il terzo intervento di questo tipo in cinque anni" | Non ha fonte | Citare le leggi (per esempio L. 197/2022, art. 1, c. 309, e le successive) oppure togliere la frase.
- FATTO | `chi_guadagna` (2° punto): sent. 130/2023 | Non è nel file verificato | Vedi correzioni trasversali.
- LINGUAGGIO | `titolo` e `numeri` ("over 75", "Carta over 75") | Parola inglese evitabile | "persone con 75 anni e più"; "Carta per chi ha 75 anni e più".
- LINGUAGGIO | `chi_guadagna` (4° punto) e `cosa_cambieremmo` (ultimo punto): "Anziani non autosufficienti", "quanti anziani" | Va messa prima la persona (capitolo 23, punto 5) | "Persone anziane non autosufficienti"; "quante persone anziane".

### manovra-2027-sanita-fondo-e-personale.yaml
- FATTO | `numeri`, "Quote già vincolate nel 2027" | Il totale (1.580) comprende i 138 milioni del comma 7, che la legge dichiara di "libera disponibilità" delle Regioni. Inoltre le ore aggiuntive del comma 4 sono "a valere sul livello di finanziamento indistinto" | Togliere i 138 milioni dalle quote vincolate (circa 1.440 milioni su 2.365, il 61%) e tenerli in una riga separata, "quota libera".
- EQUILIBRIO | `titolo` ("quasi tutti già destinati") e `bilancio` ("quasi tutto l'aumento sia già speso prima di arrivare ai servizi") | Indennità del pronto soccorso, ore contro le attese e tariffe ospedaliere sono spesa per i servizi e per chi ci lavora. La frase le presenta come uno spreco | Titolo: "...circa sei decimi già destinati a tariffe, pronto soccorso e liste d'attesa". Bilancio: "Non bene che gran parte dell'aumento copra costi già decisi, lasciando poco alle Regioni per nuovi servizi..."
- EQUILIBRIO | `chi_guadagna` (2° punto): "È una richiesta storica dei sindacati..." | Senza fonte | Vedi correzioni trasversali.
- EQUILIBRIO | `chi_guadagna` (4° punto) e `valori` | L'art. 74 alza di 3 punti il tetto per i privati accreditati, in modo permanente. Il commento non pesa lo spostamento di spesa verso il privato accreditato | Aggiungere in `valori` EQU o FID: "Il tetto più alto per i privati accreditati è permanente e non chiede in cambio le agende nel CUP: rischia di spostare offerta dal pubblico al privato."
- LINGUAGGIO | `valori` FUT: "mentre crescono gli anziani" | | "mentre cresce il numero di persone anziane".

### manovra-2027-scuola-universita.yaml
- FATTO | `valori` EQU "-" ("Il taglio è uguale ovunque") e `bilancio` ("che il taglio sia uguale per tutte le scuole") | La stessa scheda dice in `domande_aperte` che il decreto di riparto non c'è ancora: non si sa se il taglio sarà uguale | "Il taglio non tiene conto, per legge, di dove la dispersione e i divari sono più alti; il riparto è rinviato a un decreto."
- EQUILIBRIO | `valori` RIS "+" (buono paritarie "alle famiglie con meno reddito") | Con ISEE fino a 30.000 euro il buono raggiunge redditi medi, e solo famiglie che possono già pagare una retta. Le famiglie in povertà non lo usano | Segno "=" e motivo: "Allarga la scelta per famiglie con ISEE medio, ma non per chi non può pagare la parte di retta che resta."
- EQUILIBRIO | `chi_paga` | Mancano gli effetti territoriali. Il calo degli alunni è più forte nel Mezzogiorno e nelle aree interne, quindi il taglio può concentrarsi lì | Aggiungere: "Scuole del Mezzogiorno e delle aree interne, dove il calo degli alunni è maggiore: rischiano più accorpamenti (da verificare sul decreto di riparto)."
- LINGUAGGIO | `chi_guadagna`: "Un gruppo piccolo di giovani ricercatori molto bravi" | Registro colloquiale, maschile generico | "Un piccolo numero di giovani ricercatrici e ricercatori selezionati".

### manovra-2027-revisione-spesa-rinvii.yaml
- EQUILIBRIO | `valori` EQU "=" | Il taglio di 100 milioni l'anno all'Assegno di inclusione e il filtro sul gratuito patrocinio riducono spesa rivolta a chi ha meno. Il segno neutro è indulgente | Segno "-" e motivo: "Si toglie a un fondo per le famiglie in povertà perché non speso, senza chiedersi perché non lo è; il filtro sul gratuito patrocinio può escludere chi non ha mezzi."
- EQUILIBRIO | `chi_guadagna` (4° punto): "un primo filtro contro le domande infondate di gratuito patrocinio" | Riprende la cornice del Governo; non ci sono dati sulle domande infondate | "Il bilancio della giustizia, se il filtro colpisce solo domande davvero infondate (la relazione non dà dati)."
- LINGUAGGIO | `chi_paga` (4° punto): "Le persone povere" | Capitolo 23, punto 4 | "Le persone in povertà".

### manovra-2027-comuni-debiti-avanzo.yaml
- EQUILIBRIO | `chi_paga` (1° e 2° punto): "anche dove la crisi nasce da gestioni locali sbagliate"; "vedono premiato chi ha accumulato debiti" | Tono morale, e la cornice è parziale. Molti dissesti hanno cause anche strutturali (bassa capacità di riscossione, minori entrate proprie, regole contabili cambiate). Chi vive in quei Comuni paga già aliquote massime con servizi più poveri | 1° punto: "Chi paga le tasse in tutta Italia: 400 mln per i disavanzi di pochi enti, senza una diagnosi pubblica delle cause, che possono essere gestionali o strutturali." 2° punto: "I Comuni che non hanno chiesto anticipazioni: non ricevono nulla." Aggiungere: "Chi vive nei Comuni in dissesto: paga addizionali e tariffe al massimo e riceve servizi ridotti; la norma non migliora subito i servizi."
- LINGUAGGIO | `valori` CIT: "spiegare ai cittadini" | | "spiegare a chi vive nel Comune".

### manovra-2027-difesa-clausola-ue.yaml
- EQUILIBRIO | `bilancio`: "Va bene che la spesa per la sicurezza cresca in modo trasparente" | Contraddice FID "-" e `domande_aperte`: non si sa quali programmi finanzi il fondo da 2,6 mld né quali importi abbiano autorizzato le Camere | "Va bene il monitoraggio delle nuove caserme e l'attenzione agli impegni europei e NATO. Non va bene..." (togliere "in modo trasparente").
- EQUILIBRIO | `chi_paga` | Manca il costo opportunità. Nello stesso disegno di legge la spesa sanitaria sul PIL scende (scheda sanità) e i costi fissi dal 2029 tolgono spazio ad altre politiche, senza dire quali | Aggiungere: "Le altre politiche pubbliche: dal 2029 circa 0,6 mld l'anno andranno trovati in altri capitoli, mentre la spesa sanitaria sul PIL scende."
- LINGUAGGIO | `chi_guadagna` (ultimo punto): "Il Governo in carica: spende oggi senza dover trovare subito la copertura" | Suona come un'accusa politica (regola 6) | "Il bilancio del 2027-2028: la spesa non richiede tagli o tasse immediati." Oppure togliere il punto, perché la sostanza è già in `chi_paga`.

### manovra-2027-energia-ferrovie-in-deficit.yaml
- EQUILIBRIO | `valori` EQU e `chi_guadagna` | Manca la distribuzione territoriale delle opere. Nel 2027-2028 vanno 1,6 mld al Terzo valico e 0,5 mld al Brennero; la Messina-Catania compare solo nel 2029-2030, oltre la clausola | Aggiungere in EQU: "La parte ferroviaria finanziata subito va soprattutto a opere del Nord; per la Sicilia le risorse arrivano dopo il 2028."
- LINGUAGGIO | `chi_paga` (1° punto): "secondo l'UPB" | Altre schede attribuiscono il 138,5% al DPB del MEF | Uniformare: "(MEF, DPB 2027; stesso valore nell'audizione UPB)".

### manovra-2027-banche-assicurazioni-energia.yaml
- EQUILIBRIO / FATTO | `rischi_giuridici` e `bilancio` ("rischia ... di non reggere davanti alla Corte") | Si cita solo la sent. 10/2015, che ha censurato la vecchia imposta. La sent. 111/2024, nel file verificato, riguarda proprio il contributo straordinario sulle imprese dell'energia (art. 37 DL 21/2022) e lo ha ritenuto in larga parte legittimo. Qui è citata solo per gli artt. 18-19 | Aggiungere per l'art. 21: "La sent. 111/2024 ha ammesso un prelievo straordinario sul settore energetico; il rischio dipende dal fatto che manchino controlli sulla traslazione." In `bilancio` attenuare: "...e, senza controlli sui prezzi, può essere pagato dai clienti ed esposto a ricorsi."
- EQUILIBRIO | `valori` CIT "-" e `bilancio` ("l'imposta sulle azioni colpisce i risparmiatori più che le banche") | Non si dice che il possesso diretto di azioni è concentrato nelle famiglie più ricche, quindi l'imposta è in buona parte progressiva | Aggiungere: "Il possesso di azioni è concentrato nelle famiglie con più patrimonio (Banca d'Italia, Indagine sui bilanci delle famiglie, da verificare); il peso sui fondi pensione si può evitare con un'esenzione."
- LINGUAGGIO | `chi_paga` (4° punto): "Possibilmente i clienti" | Calco dall'inglese | "Forse anche i clienti".

### manovra-2027-irpef-lavoro-forfettario.yaml
- EQUILIBRIO | `chi_guadagna` (4° punto): "i loro ordini e associazioni chiedevano da tempo la soglia più alta" | Senza fonte | Vedi correzioni trasversali.
- EQUILIBRIO | `chi_paga` | Manca il profilo di chi riceve lo scaglione | Aggiungere la `domanda_aperta` trasversale su genere e territorio.
- LINGUAGGIO | `chi_paga` (2° punto): "incapienti" | Termine tecnico non spiegato | "persone con redditi così bassi da non pagare IRPEF (incapienti)".
- LINGUAGGIO | `chi_guadagna` (4° punto): "lavoratori autonomi e professionisti" | Maschile generico | "persone che lavorano in proprio o come professioniste".

### manovra-2027-lavoro-giovani-e-madri.yaml
- EQUILIBRIO | `chi_guadagna` (5° punto): "una misura cercata dai sindacati del pubblico impiego" | Senza fonte | Vedi correzioni trasversali.
- EQUILIBRIO | `cosa_fa` (1° punto) e `chi_paga` | Non si dice che, con due figli, il bonus dura solo fino ai 10 anni del secondo figlio (relazione tecnica, art. 57). È un limite che pesa sulle madri | Aggiungere: "Con due figli il bonus si ferma quando il secondo compie 10 anni; con tre o più, ai 18 anni del più piccolo."
- LINGUAGGIO | `cosa_fa` (5° punto) "lavoratori nella ZES"; `chi_paga` (3° punto) "I lavoratori nati prima del 1998" | Maschile generico | "lavoratrici e lavoratori nella ZES"; "Chi lavora ed è nato prima del 1998".

### manovra-2027-payback-farmaci-dispositivi.yaml
- FATTO | `chi_paga` (3° punto): "Fornitori di dispositivi più piccoli: pagano circa 2,6 miliardi" | I 2,6 miliardi sono a carico di tutte le imprese. Le piccole pesano di più in proporzione, non pagano tutto | "Imprese fornitrici di dispositivi: pagano circa 2,6 miliardi su fatture fino a otto anni fa; per le più piccole il peso in rapporto al fatturato è maggiore."
- FATTO | `chi_paga` (2° punto): "circa 440 milioni l'anno" | Somma di 292 (solo dal 2028) e 146 (dal 2027): nel 2027 sono circa 146 | "circa 146 milioni nel 2027 e 440 l'anno dal 2028".

### manovra-2027-giochi.yaml
- FATTO | `chi_guadagna` (1° punto): "alla quarta proroga per il bingo" | La relazione tecnica (art. 27) elenca proroghe nel 2017, 2019, 2020, 2022 e 2024: questa è almeno la sesta | "dopo almeno cinque proroghe dal 2017 (relazione tecnica, art. 27)".
- EQUILIBRIO | `rischi_giuridici` | Non si cita la sentenza della Corte di giustizia UE del 20 marzo 2025 (cause C-728/22 e altre), richiamata nella relazione tecnica, che ammette le proroghe tecniche del bingo con canone | Aggiungere: "La Corte di giustizia (20/3/2025) ha ammesso proroghe tecniche con canone proporzionato; il rischio cresce con la ripetizione."
- LINGUAGGIO | `chi_paga` (4° punto): "I contribuenti onesti"; `bilancio` "giocatori più fragili"; FID "Ennesima" | Tono morale, maschile generico | "Chi ha pagato per intero"; "chi gioca ed è più fragile"; "Sesta proroga".

### manovra-2027-evasione-crediti.yaml
- LINGUAGGIO | `in_breve`, `cosa_fa`, `numeri`, `valori`, `bilancio`, `cosa_cambieremmo`: "plastic e sugar tax" | Parole inglesi evitabili | "imposte sulla plastica monouso e sulle bevande zuccherate".
- LINGUAGGIO | `chi_guadagna` (4° punto) e FID: "per l'ennesima volta" | Polemico | Indicare il numero dei rinvii con la fonte, o togliere.
- LINGUAGGIO | `cosa_fa` (1° punto): "chi paga una fattura elettronica a un'impresa" | Può far pensare che valga anche per i consumatori; l'art. 35 riguarda i pagamenti tra imprese | "l'impresa o il professionista che paga una fattura elettronica a un'altra impresa o a un professionista".

### manovra-2027-bollo-auto.yaml
- FATTO | `chi_paga` (2° punto): "Chi non ha l'auto, spesso persone anziane o con redditi bassi" | "Spesso" non ha fonte | Citare ISTAT (famiglie senza auto per reddito ed età) oppure scrivere "anche persone anziane o con redditi bassi (da verificare)".
- Nessun altro rilievo: è il commento più equilibrato sul piano ambientale e distributivo.

### manovra-2027-lep-tpl-regioni.yaml
- LINGUAGGIO | `chi_guadagna` (4° punto), `chi_paga` (4° punto): "Alunni con disabilità", "alunni" | Maschile generico | "Alunne e alunni con disabilità".
- Nessun rilievo di fatto: sentenze 182/2026, 192/2024 e 220/2021 verificate.

### dl-2026-185-ex-ilva.yaml
- EQUILIBRIO | `valori` | Manca un valore sulla salute di chi vive a Taranto. Il rischio è in `chi_paga`, ma con una frase che lo attenua ("tenere caldi gli impianti non è produrre"). Anche gli altoforni tenuti caldi emettono | Aggiungere BEN "-": "Tenere caldi gli altoforni mentre la Cassazione decide prolunga l'esposizione dei residenti alle emissioni, dopo la condanna della Corte EDU (Cordella, 2019)." In `chi_paga` togliere "anche se tenere caldi gli impianti non è produrre".
- EQUILIBRIO | `valori` CIT "+" | L'offerta "congrua" entro 50 km o 80 minuti pesa di più su chi ha compiti di cura, in prevalenza donne | Aggiungere al motivo: "ma la distanza di 80 minuti pesa di più su chi ha figli o familiari da assistere."
- FATTO | `rischi_giuridici`: sent. 85/2013 e 58/2018 | Non sono nel file verificato | Vedi correzioni trasversali.
- LINGUAGGIO | `in_breve` ("È un aiuto giusto... l'ennesima misura"), FID ("Ennesimo decreto"), `chi_guadagna` e `chi_paga` ("Lavoratori dell'indotto", "Lavoratori in crisi") | Giudizio nei fatti, tono polemico, maschile generico | Spostare il giudizio in `bilancio`; "Un altro decreto sull'ex ILVA"; "Lavoratrici e lavoratori".
- LINGUAGGIO | `numeri`: "(somma dell'agente)" | Diverso dagli altri commenti | "(somma dell'Osservatorio)".

### dl-2026-190-sicurezza-minori.yaml
- FATTO | `chi_paga` (3° punto) "possono essere trattenute in base a sospetti, senza un fatto preciso"; `valori` RIS "trattenimento su semplici segnalazioni" | Il nuovo comma 3-ter chiede "specifiche e concrete circostanze di tempo e di luogo e di elementi di fatto" e un "fondato motivo" di pericolo concreto. Le segnalazioni sono uno degli elementi, non l'unico. Il dubbio di vaghezza resta, ma la descrizione va resa fedele | "Persone con precedenti o segnalazioni di polizia: possono essere trattenute in base a circostanze di fatto e a un 'fondato motivo', con criteri ampi e senza durata massima scritta."
- FATTO | `valori` EQU: "dove la stessa relazione dice che nascono le bande" | La relazione illustrativa A.C. 3159 non è nel repository e il testo del decreto non usa queste parole | Citare il passo della relazione con pagina, oppure: "sulle famiglie povere e sulle periferie".
- FATTO | `rischi_giuridici`: sent. 168/1994, 263/2019 e 24/2019 | Non sono nel file verificato | Vedi correzioni trasversali.
- LINGUAGGIO | `cosa_fa` (1° punto) "Il ragazzo tra 14 e 18 anni"; `chi_paga` "Ragazzi tra 14 e 18 anni"; `cosa_fa` (7° punto) "zone della movida" | Maschile generico; parola straniera evitabile | "Chi ha tra 14 e 18 anni"; "Ragazze e ragazzi tra 14 e 18 anni"; "zone della vita notturna".

### dl-2026-193-autotrasporto.yaml
- FATTO | `cosa_fa` (ultimo punto): "come consente la direttiva (UE) 2026/470" | Il testo del decreto (art. 10) non cita alcuna direttiva | Indicare la fonte (relazione A.S. 2074, con pagina) oppure scrivere "(base europea da verificare)".
- EQUILIBRIO | `chi_paga` | L'esonero dalla rendicontazione di sostenibilità (art. 10) non ha un "chi paga" | Aggiungere: "Chi lavora nelle imprese esonerate, chi vi investe e le comunità vicine: per due anni avranno meno informazioni su impatti ambientali e sociali."
- LINGUAGGIO | `chi_paga` (2° punto): "Gli stessi agricoltori" | Maschile generico | "Le stesse imprese agricole".

### dl-2026-205-campi-flegrei.yaml
- FATTO | `valori` FID: "Il denaro è tolto ad altre zone colpite... senza dirlo con chiarezza" | L'art. 8, c. 2, indica in modo esplicito i fondi tagliati. Quello che manca è dire quali interventi altrove saltano | "Il denaro è tolto al Fondo per la ricostruzione di altre zone colpite e alla prevenzione nazionale, senza dire quali interventi slittano."
- FATTO | `rischi_giuridici`: sent. 186/2013 | Non è nel file verificato | Vedi correzioni trasversali.
- LINGUAGGIO | `in_breve` ("Va nella giusta direzione della prevenzione") | Giudizio nei fatti | Spostare in `bilancio`.

### dl-2026-207-energia.yaml
- FATTO | `chi_guadagna` (4° punto): "lo sconto sugli oneri di sistema del 2027" | L'art. 1, lett. c), fissa al 30 novembre 2026 i provvedimenti dell'ARERA ma non dice l'anno dello sconto | "una riduzione degli oneri del gas, nei limiti delle risorse già versate, con regole ARERA entro il 30 novembre 2026".
- Nessun altro rilievo: le stime di stampa sono già indicate come tali.

### legge-2026-180-elettorale.yaml
- FATTO | `valori` FID: "Regole cambiate a maggioranza semplice" | 227 voti su 400 superano la maggioranza assoluta (201). Il punto è che mancano i tre quinti | "Regole cambiate senza la maggioranza dei tre quinti (227 sì su 400), a circa un anno dal voto..."
- FATTO | `numeri`, "Premio e tetto" (55% e 56,5%) | Il tetto di 220 e 113 seggi esclude i seggi dell'Estero. Sui soli seggi in Italia la quota è più alta (circa 56% alla Camera e 58% al Senato, da verificare sul numero dei seggi Estero) | Aggiungere: "esclusi i seggi dell'Estero; sui seggi assegnati in Italia la quota è più alta".
- FATTO | `rischi_giuridici`: sent. 1/2014 e 35/2017 | Non sono nel file verificato | Vedi correzioni trasversali.
- EQUILIBRIO | `domande_aperte` | L'alternanza di genere vale per liste e preferenze, ma i capilista sono eletti senza preferenze e scelti dai partiti. L'effetto sulla presenza delle donne dipende da chi è capolista | Aggiungere: "Quante donne saranno capolista? Da lì dipende gran parte dell'equilibrio di genere tra gli eletti."
- LINGUAGGIO | `chi_paga` "Italiani all'estero"; `chi_guadagna` "I candidati con più risorse" | Maschile generico | "Italiane e italiani all'estero"; "Chi si candida con più risorse".

## Verifiche a campione eseguite (esito positivo)

Ho controllato questi dati sui testi e sulle relazioni, e sono corretti:
- scaglione 28.000-55.000 al 33% e forfettario 100.000/115.000 (art. 9);
- percentuali di adeguamento 100/85/53/47/37/32 (art. 55) e lordo di 1.476 milioni;
- carta da 1.645 milioni, età 75 anni, soglia 28.000 euro (art. 53);
- fondo da 850 milioni (art. 52);
- 2.365/2.352/2.399 milioni, 500, 300 (213+87) e 380 milioni (art. 69) e i 3 punti dell'art. 74;
- 4.925 e 2.049 posti dopo i 5.660 (art. 66, c. 5), risparmi 83,9 e 251,7 milioni;
- 1.434 milioni e 3,2 milioni di contribuenti (relazione tecnica, art. 9);
- bollo a 2.293,5 milioni;
- 2,84 mld di capitale e 0,53 di interessi (art. 124), con effetto neutro;
- ritenuta all'1% e al 2% (art. 35);
- carabinieri ausiliari: 600 posti, paga al 65%, riserva del 30% (art. 93);
- missioni internazionali: 520 e 804 milioni (art. 95);
- art. 44 (nati dopo il 1997, 28.000 e 2.500 euro) e art. 65 (800 euro, 15%, soglia di 50.000 euro);
- fecondità a 1,14 (ISTAT) e debito al 138,5% (UPB e DPB);
- date di conversione dei DL 185, 190, 193, 205 e 207, tutte corrette (60 giorni dalla pubblicazione);
- DL 185: altoforni non oltre il 15 dicembre 2026;
- DL 190: multa da 10.000 a 20.000 euro;
- DL 205: coperture dell'art. 8 e contributo al 100% sotto 28.000 euro;
- DL 207: legge di conversione n. 49 del 10 aprile 2026, quindi "sette mesi prima" è corretto;
- legge elettorale: soglia del 42%, premio di 70 seggi, tetti di 220 e 113 seggi;
- sentenze nel file verificato: 182/2026, 52/2026, 19/2025, 234/2020, 140/2024, 111/2024, 10/2015, 16/2017, 192/2024, 220/2021, 223/2023, 80/2010, 22/2012 e 32/2014.
