# Giro di revisione: cittadinanza e decisori, 13 novembre 2026 (terzo giro)

*Revisione scritta da un agente AI che ragiona come una cittadina/un cittadino e come una persona con responsabilità politiche, 13 novembre 2026 (terzo giro); non è la revisione di una persona.*

*Base: il repository al commit e0c25d5 (13 novembre 2026, sera) e il sito pubblico visto lo stesso giorno. Il sito è allineato al repository: 9,4 mld, 67 misure su 78, nucleo a pieno dal 2034, 7,6 mld rinviati. Fa fede il repository. Legenda: **[Fatto]** verificato su file, con uno script o sul sito; **[Giudizio]** valutazione di questo agente.*

---

## In breve

| Voto (1-10) | Cittadina/o: 1° → 2° → **3° giro** | Politica/o: 1° → 2° → **3° giro** |
|---|---|---|
| Credibilità | 6 → 6 → **6** | 6 → 6 → **7** |
| Utilità | 5 → 6 → **6** | 7 → 7 → **8** |
| Fattibilità | 3 → 4 → **4** | 4 → 5 → **6** |
| Chiarezza | 4 → 5 → **5** | 6 → 6 → **6** |

**In una frase.** Il calendario ora rispetta le regole del progetto e dice la verità sui tempi. Il pacchetto "pronto domani" è il passo più utile per chi governa da quando esiste GovernAI. Per la cittadina cambia poco: la pagina "per me" non dice ancora quanto, in euro, e i benefici arrivano più tardi.

Perché i voti si muovono così:

- **Per chi governa, utilità e fattibilità salgono.** Sei testi in formato parlamentare, con relazione tecnica e prospetto dei saldi. Due li ho controllati a fondo (01-P2 e 09-C10) e un terzo in parte (08-P1). Un ufficio legislativo li può usare come **buona prima bozza**, non come testo da depositare domani (vedi sotto).
- **La credibilità sale di un punto solo per chi governa.** Il calendario non usa più fondi europei per la spesa corrente e dichiara il prezzo: 7,6 mld rinviati, 5,7 del nucleo. Ma il programma promette ancora cose che non contiene: il primo punto dei "Primi 100 giorni" cita una misura esclusa (09-C1).
- **Per la cittadina nulla sale.** I posti al nido, le Case della Comunità e il resto del nucleo arrivano a pieno nel 2034. La pagina "per me" lo dice. Ma non dice ancora quanto cambia per una persona in euro, e manca ancora un nome che firmi.

**Le priorità del secondo giro.**

| Priorità del 2° giro | Esito | Commento breve |
|---|---|---|
| 1. Correggere il calendario | **Risolta in gran parte** | Riforme a costo quasi zero subito (28), niente ponte UE per spesa corrente, fumo dal 2028 e riserva dal 2030, 2027 anno di preparazione, nucleo a pieno dal 2034 dichiarato. Restano aperti: congedo del papà, 04-P9, 06-C2 dopo il 2029, i 0,50 mld dopo il 2029, sperimentazioni che non finiscono in tempo. |
| 2. Allineare i numeri e rendere il controllo meno cieco | **A metà** | Corretti 78 proposte, nucleo 23 in 21, 9,4 in 23, README. Restano 20 §4 (63), 20 §6 (22), 21 (data), 22 (2033), gli obiettivi "in 5 anni" e il patent box. Il controllo di coerenza dice ancora "nessun problema". |
| 5. Pacchetto per domani | **Fatta, con riserve** | Sei testi completi e onesti sui propri limiti. Mancano revisione di una persona esperta, un allegato di copertura (08-P1) e alcuni dati di dimostrazione. |

Non fatte, come dichiarato: il nome della persona responsabile (priorità 3) e la seconda versione della pagina "per me" (priorità 4).

---

## Che cosa è migliorato

- **Il calendario non contraddice più il registro dei fondi.** **[Fatto: `annuale.py`, `piano()`]** La colonna "ponte UE" è zero in tutti gli anni. La coesione paga solo le spese già contate lì. Quando nel 2029 supera la capienza (2,06 contro 2,0), lo scarto di 0,06 slitta ed è scritto in `annuale_intermedio.md`.
- **Le riforme senza costo partono subito.** 28 misure con al massimo 20 milioni l'anno sulle risorse generali, tra cui 08-P1, 01-P2, 04-P4, 08-P7, 09-C2, 02-C1, 02-C3. Costano 0,03 mld nel 2027 e 0,04 dal 2029. **[Giudizio]** È la correzione giusta: una legge di trasparenza non deve aspettare il gettito delle accise.
- **Fumo e riserva hanno soldi dal primo anno utile.** 0,04 mld per smettere di fumare dal 2028, insieme all'accisa sul tabacco. 0,05 di riserva dal 2030.
- **Il prezzo è scritto in chiaro.** 20 §7 e sito: "slittano circa 7,6 mld di spesa, di cui 5,7 del nucleo"; "il programma arriva a regime più tardi di quanto promettono le singole schede". Prima il testo faceva pensare che il rinvio toccasse le "altre misure". Ora no.
- **Il 2027 è dichiarato come anno di preparazione.** È più realistico: la prima legge di bilancio di un nuovo governo vale per l'anno dopo.
- **Il calendario è uguale nel 20, in `profili.yaml` e sul sito.** 4% nel 2027, 69% nel 2028, 87% nel 2029, pieno dal 2034. Tutti e cinque i profili con la nota hanno lo stesso testo.
- **Il pacchetto "pronto domani" esiste ed è serio.** Sei misure, ognuna con: scheda breve, relazione illustrativa, articolato, relazione tecnica con prospetto dei saldi (SNF, fabbisogno, indebitamento), analisi tecnico-normativa, analisi d'impatto, note per chi presenta. Ogni file dice quale variante del programma usa e che cosa non c'è. Ogni file elenca i riferimenti "da verificare sul testo vigente". Il sito avvisa: "Testo preparato da agenti AI. Va verificato da una persona esperta".
- **Il controllo di coerenza ha un controllo in più** (numero di proposte, nucleo, intestazione di 23).

---

## Il pacchetto pronto domani alla prova

Ho letto per intero 01-P2 e 09-C10 (art. 5) e la parte normativa e di copertura di 08-P1. Per 08-P7 e 09-C2 ho controllato solo copertura e prospetto.

### Giudizio generale

**[Giudizio]** Un ufficio legislativo può usarli come **base di lavoro di buona qualità**: la tecnica della novella è corretta, le norme modificate sono indicate con articolo e comma, i commi nuovi sono numerati in modo coerente con il testo vigente dichiarato, le relazioni tecniche hanno il prospetto sui tre saldi. Non sono ancora "da depositare domani" per quattro motivi: nessuna persona esperta li ha letti; due testi citano in modo diverso la stessa norma; in 08-P1 l'allegato della copertura è vuoto; le relazioni tecniche a invarianza affermano più di quanto dimostrano.

### 01-P2 — Scheda di valutazione per ogni spesa fiscale

| Controllo | Esito |
|---|---|
| Articolato | **Buono.** Quattro articoli. Novella all'art. 21 L. 196/2009 con commi 11-bis.1, 11-bis.2, 11-bis.3. Contenuto minimo in legge, calendario per terzi, ordine di priorità, base giuridica per i dati (GDPR art. 6.1.e, art. 2-ter Codice privacy), clausola di invarianza. |
| Relazione tecnica e prospetto | **Formalmente completa** (tutti zeri sui tre saldi). **Debole sulla dimostrazione**: per una clausola di invarianza l'art. 17, c. 6-bis, L. 196/2009 chiede gli elementi che provano la neutralità. Il testo dice "nessun onere" per circa 190 schede l'anno con distribuzione per decili, ma non dice quante persone lavorano oggi al rapporto né quanto tempo serve per una scheda. La Ragioneria lo chiederà. Il testo stesso ammette il limite nelle note. |
| Coerenza con la scheda e il programma | **Coerente** con la variante ZERO scelta (costo 0, nessuna scadenza). **[Fatto]** Ma il nome del file (`01-P2_spese_fiscali_a_scadenza.md`) e il titolo sul sito ("Spese fiscali a scadenza (sunset 5 anni)") descrivono la variante PIENA, che **non** è nel testo. Anche 20 (riga 20) parla di "spese fiscali a scadenza". E 22 indica come obiettivo "da 573 a 400 agevolazioni in 5 anni", che la variante ZERO non può garantire (lo dice anche il pacchetto). Infine l'obiettivo a 3 anni dell'indicatore diretto (60%) è sotto quanto chiede la legge stessa (almeno due terzi entro il rapporto 2029). |
| Riferimenti normativi | **Verificabili**, con link Normattiva in formato URN. Ma vedi il problema sul comma della legge di bilancio (sotto). |

### 09-C10, art. 5 — Tempi e valutazione degli incentivi alle imprese

| Controllo | Esito |
|---|---|
| Articolato | **Il più maturo del pacchetto.** Novelle agli artt. 7, 21 e 22 del Codice degli incentivi (d.lgs. 184/2025) e all'art. 17, c. 3, L. 196/2009. Esclusione dei ritardi non imputabili, regime transitorio per in house e gare (art. 120 d.lgs. 36/2023), salvaguardia dei fondi UE, deroga espressa all'art. 25, c. 2. La regola sul rifinanziamento vincola solo gli atti amministrativi: è corretto, una legge ordinaria non può legare il legislatore futuro. |
| Relazione tecnica e prospetto | **Buona.** Per ogni articolo spiega perché non ci sono effetti e cita gli elementi di dimostrazione (art. 17, cc. 6-bis e 7). Dice in chiaro che le somme trattenute al gestore **non** sono una copertura. Due dati restano "da acquisire": costo medio di una valutazione e numero di incentivi sopra 100 milioni. |
| Coerenza con la scheda e il programma | **Coerente sui costi**: il pilota della libreria (5, 10, 10 mln su coesione) è tenuto fuori. **[Fatto]** Due attriti: (1) la variante PILOTA scelta nel programma ("10 bandi in 3 Regioni") non descrive le tre regole dell'art. 5, che stanno solo nel testo della scheda; (2) sul sito la card ha il titolo dell'intera proposta ("Bandi pubblici con istruttoria assistita…") e l'etichetta "pilota, 10 mln l'anno", mentre il testo è a costo zero. Inoltre il README dice "nel calendario partono tutte subito", ma 09-C10 non è tra le 28 riforme del primo gruppo: parte subito perché è pagata dalla coesione. |
| Riferimenti normativi | **Verificabili**, con link. Note di drafting oneste (data di entrata in vigore da inserire, rinvio da correggere nella scheda). Il conflitto di interesse è dichiarato. |

### Un errore che un ufficio legislativo vedrebbe subito

**[Fatto]** Per dire che la norma non può stare nella legge di bilancio, 01-P2 cita l'**art. 21, comma 1-ter**, L. 196/2009; 09-C10 cita l'**art. 21, comma 1-quinquies**. È la stessa regola (niente norme ordinamentali nella legge di bilancio): almeno uno dei due riferimenti è sbagliato. **[Giudizio]** A memoria di questo agente il divieto è al comma 1-quinquies, ma va verificato sul testo vigente. Un errore così, in un pacchetto, toglie fiducia a tutto il resto.

### 08-P1 — Consulenza algoritmica presso l'UPB (lettura parziale)

- **Buono:** la scelta di modificare la L. 243/2012 a maggioranza assoluta è corretta. Le garanzie (non vincolante, sorveglianza umana, divieto di profilazione, firma di un funzionario, audit annuale, silenzio pre-elettorale) sono complete. Il prospetto dei saldi ha i segni giusti.
- **Non pronto:** l'**Allegato A** con le riduzioni per Ministero è "da compilare". Senza allegato la copertura non è utilizzabile. In più la riduzione delle consulenze (6, 12, 15 mln) va scritta come quota **della** copertura RA03 già contata nel programma, non in aggiunta: altrimenti gli stessi capitoli si tagliano due volte. La norma scade dopo cinque anni, ma l'onere è "a decorrere dal 2029": va allineato.
- Cita il d.lgs. 7 ottobre 2026, n. 179: da verificare.

### 08-P7 e 09-C2 (solo copertura)

- 08-P7: copertura sul fondo speciale di parte corrente (Tabella A), prospetto corretto (+2/−2, +3/−3). Manca l'indicazione dell'accantonamento di quale Ministero. **[Fatto]** Sul sito l'etichetta dice "5 mln l'anno": il costo vero è 3. La funzione `euro()` di `docs/app.js` arrotonda tutto sotto i 5 milioni a "5 mln".
- 09-C2: l'indennizzo è un onere eventuale degli enti, dal 37° mese, con tetto dello 0,5% della spesa corrente. È trattato con prudenza. **[Giudizio]** La Ragioneria potrebbe chiedere una clausola di salvaguardia (art. 17, c. 12): il tetto, in teoria, è alto.

---

## Problemi rimasti o nuovi

1. **Il primo dei "Primi 100 giorni" cita una misura che non c'è.** **[Fatto]** 20 §5, punto 1: "Legge GovernAI (08-P1) e Stato a vetro (09-C1) in Consiglio dei ministri. Nascono l'Ufficio per la consulenza algoritmica presso le Camere…". Ma 09-C1 è "fuori da questa versione" (22, riga 230; nessuna variante scelta in `selezione_intermedio.csv`). E la variante scelta di 08-P1 è una sezione **dentro l'UPB**, non un ufficio presso le Camere (anche 21, riga 76, dice "presso le Camere"). Lo stesso vale per 20 riga 20 ("Stato a vetro", "spese fiscali a scadenza"). Per una persona politica è il problema più visibile: la prima promessa non corrisponde al programma.
2. **Le sperimentazioni pagate dalle risorse generali non finiscono in tempo per il 2029.** **[Fatto]** Sono tre: 06-C2 (personale infermieristico, "triennale"), 02-C4 e 04-P7. Nel calendario stanno nel secondo gruppo: 4% nel 2027, 69% nel 2028. Quindi 06-C2 parte di fatto nel 2028 e non può dare una valutazione triennale per le decisioni del 2029. Il documento 20 dice il contrario ("devono produrre le valutazioni in tempo"). Le altre sperimentazioni sono sulla coesione e partono per intero.
3. **Il congedo del papà ha ancora date fisse.** **[Fatto]** Profilo famiglia: "un mese dal 2028, due mesi dal 2030". Il calendario dà a 02-C2 il 69% nel 2028 e il 90% nel 2030. Non è detto se slitta il congedo o se si tagliano di più i posti al nido.
4. **04-P9: l'obbligo arriva quattro anni prima dell'aiuto.** **[Fatto]** Zone a emissioni zero per le merci "dal 2030"; contributi per cargo bike e ricarica dal 2034 (32%), pieni nel 2035. Il divario è cresciuto (prima era il 2033).
5. **I 0,50 mld dopo il 2029 restano senza copertura.** La riserva di 0,05 copre un decimo. 06-C2 resta nei conti a 0,35 l'anno per sempre, anche se è "triennale". PE04, che dovrebbe pagarlo, rende dal 2030.
6. **Disallineamenti di testo ancora aperti.** **[Fatto]**
   - 20 §4: "63 misure con gettito" (il menu ne ha 72); etichetta "Contributo di equità sulle pensioni più alte e risparmi dall'uscita dalle quote, 0,11".
   - 20 §6, punto 6: "tutte e 22 restano"; il nucleo è di 23.
   - 21: "aggiornato il 12 novembre 2026"; nessun cenno al calendario.
   - 22, riga 125, e sito: 01-P13 "parte solo nel 2033"; il calendario dice 2034.
   - 22, obiettivi "in 5 anni" legati a misure escluse o che partono tardi: produttività (01-P4, esclusa), ricerca (01-P13, dal 2034), ore liberate dall'AI (09-C9, dal 2034), grandi opere "con valutazione indipendente" (04-P4 è in variante ZERO, "senza terzietà del valutatore"), agevolazioni da 573 a 400 (01-P2 in variante ZERO).
   - `annuale_intermedio.md`: "-0%" nella colonna "Altre misure" del 2028 (zero con il segno).
7. **Il controllo di coerenza è ancora troppo stretto.** Risponde "nessun problema", ma non vede nessuno dei punti 1 e 6. Cerca frasi esatte. Non controlla che le misure nominate nei "Primi 100 giorni" e negli obiettivi siano nel programma, né che l'anno di avvio permetta l'obiettivo "in 5 anni".
8. **Ancora nessun nome, ancora nessuna persona esterna.** La pagina 24 dice che la persona responsabile "è indicata con nome e cognome sul sito". Non lo è. Il pacchetto, che si rivolge proprio a uffici legislativi, è il primo lavoro dove una sola lettura esperta cambierebbe molto il valore.
9. **Per la cittadina il calendario è una cattiva notizia detta bene.** **[Giudizio]** Nel 2027 parte il 4% della spesa del nucleo. Nessuna misura del nucleo è a pieno entro la fine di una legislatura che parta nel 2027. Il sito lo dice, ma non dice che cosa si vedrà davvero nel 2028: quanti posti al nido, quante Case della Comunità.

---

## Numeri controllati

Ho ricontrollato 14 numeri tra documenti, CSV, script e sito pubblicato.

| # | Numero | Dove | Esito |
|---|---|---|---|
| 1 | Spesa dell'intermedio: 9,38 mld | `selezione_intermedio.csv` (somma 9,38), 20, 22, 23 (ora 9,4), sito | **Coerente.** Corretto il 23. |
| 2 | Proposte 78, misure 67 | `motore/proposte.csv` (78), CSV (67 varianti scelte), README, 20 §2, 21, sito | **Coerente.** |
| 3 | Nucleo robusto: 23 | `esito_proposte.csv` (23), 20 §1, 21, sito | **Coerente**, salvo 20 §6 punto 6 ("tutte e 22"). |
| 4 | Coperture: 72 nel menu, 54 scelte per 7,42 mld | `coperture_menu.csv` (72), selezione (54; 7,42) | **Coerente**, salvo 20 §4 ("63"). |
| 5 | Riforme a costo quasi zero: 28 | `piano()`, 20 §7, sito | **Coerente.** Costano 0,029 mld nel 2027 e 0,04 dal 2029. |
| 6 | Quote del nucleo: 4%, 69%, 87%, pieno dal 2034 | `annuale_intermedio.md`, 20 §7, `profili.yaml` (5 profili), sito (`nucleo_pieno: 2034`) | **Coerente.** Rifatto con lo script. |
| 7 | Spesa rinviata 7,64 mld, di cui 5,68 del nucleo | annuale, 20 §7 (7,6 e 5,7), sito | **Coerente.** |
| 8 | Spesa avviata 2027 = gettito 0,14 | annuale (0,14 e 0,14) | **Coerente**: con 0,03 alle riforme restano 0,11 per 2,70 di nucleo, cioè il 4%. |
| 9 | Coesione 2029: 2,06 contro capienza 2,0 | `annuale.py`, annuale (slittano 0,06) | **Ora dichiarato** nel file annuale; non nel 20. |
| 10 | Altre misure: inizio 2034, pieno 2035 | annuale, 20 §7, `profili.yaml`, sito | **Coerente**, salvo **22 riga 125** e sito ("2033"). |
| 11 | 08-P1: 6, 12, 15 mln | variante ESSENZIALE (0,006 / 0,012 / 0,015), pacchetto, sito (15 mln) | **Coerente.** |
| 12 | 09-C10 pilota: 5, 10, 10 mln su coesione | variante PILOTA, pacchetto | **Coerente.** Sul sito la card del testo a costo zero mostra "10 mln l'anno". |
| 13 | 08-P7: 2, 3, 3 mln | variante ESSENZIALE (0,002 / 0,003), pacchetto | **Coerente nei file**; il sito mostra **"5 mln"** (arrotondamento minimo di `euro()`). |
| 14 | Congedo del papà: un mese dal 2028 | `profili.yaml`, sito | **Incoerente** con la quota di 02-C2 (69% nel 2028). |

**[Fatto]** `python sistema/coerenza.py` risponde "nessun problema tra documenti, scenari e sito". Non rileva i punti 3, 4, 10, 12, 13, 14, né il problema 1 della sezione precedente.

---

## Miglioramenti consigliati

In ordine di valore rispetto allo sforzo.

1. **Riscrivere i "Primi 100 giorni" e le frasi di apertura del 20 sul programma vero.** Sforzo: **1-2 ore. Chi: AI.** Togliere 09-C1 (o dire "fuori da questa versione"). Scrivere 08-P1 come sezione dell'UPB. Scrivere 01-P2 come "scheda di valutazione per ogni agevolazione", non "a scadenza". Aggiungere: "il pacchetto pronto domani contiene i primi sei testi". Correggere anche 21 riga 76 e la data di 21.
2. **Chiudere i disallineamenti con un solo passaggio e insegnarli al controllo.** Sforzo: **mezza giornata. Chi: AI.** Correggere 20 §4 (63, etichetta 0,11), 20 §6 (22), 22 (2033) e gli obiettivi "in 5 anni" di 01-P4, 01-P13, 09-C9, 04-P4 e 01-P2 (togliere, o spostare "a 10 anni", o legarli alla variante scelta). Aggiungere a `coerenza.py` tre controlli: ogni codice citato in 20 §5 e negli obiettivi di 22 deve essere nel programma; l'anno di inizio nel calendario deve lasciare almeno 3 anni all'obiettivo; nessun anno diverso da quello di `piano()` vicino a "parte" o "a pieno".
3. **Rendere il pacchetto pronto per un ufficio legislativo.** Sforzo: **1 giorno. Chi: AI, poi verifica di una persona.**
   - Una sola citazione per il divieto di norme ordinamentali nella legge di bilancio (1-ter o 1-quinquies), verificata sul testo vigente.
   - 01-P2: aggiungere gli "elementi a dimostrazione" della neutralità (persone oggi al rapporto, ore per scheda); rinominare il file.
   - 08-P1: compilare l'Allegato A con i capitoli OpenBDAP; scrivere che la riduzione è "a valere su RA03"; allineare onere e scadenza.
   - 08-P7: indicare l'accantonamento del fondo speciale.
   - Sito: titolo e costo della card presi dal testo del pacchetto, non dalla proposta piena; `euro()` deve mostrare "3 mln", non "5 mln".
4. **Mettere il nome e chiedere una sola lettura esperta.** Sforzo: **1 ora per il nome; 2-4 settimane di calendario per la lettura. Chi: persona.** Il testo da far leggere per primo è 09-C10, art. 5: è il più maturo e il più vicino a un veicolo reale. Basta una persona che abbia lavorato in un ufficio legislativo o in una Ragioneria. Pubblicare le sue note accanto al testo.
5. **Sistemare i tre punti del calendario che toccano le persone.** Sforzo: **mezza giornata di AI più una scelta politica. Chi: AI propone, persona decide.**
   - Sperimentazioni sulle risorse generali (06-C2, 02-C4, 04-P7, 0,19 mld nel 2027): o le si mette davanti al nucleo nel 2028, o si sposta la decisione al 2030. Va scritto.
   - Congedo del papà: date spostate (per esempio un mese dal 2029) oppure nido più lento. Una frase nel profilo.
   - 04-P9: obbligo nelle città dal 2034, oppure i contributi (0,03 mld) nel primo gruppo.
6. **"Che cosa cambia per me", seconda versione con gli euro.** Sforzo: **2-3 giorni. Chi: AI.** Esempi semplici, senza microsimulazione: pensione di 5.000 euro lordi, un pacchetto di sigarette al giorno, forfettario a 70.000 euro, detrazioni sanitarie. Aggiungere un profilo per chi paga le accise. Aggiungere, per il nido e le Case della Comunità, che cosa si vede davvero nel 2028.
7. **Una copertura per i 0,50 mld dopo il 2029 e una fine per 06-C2.** Sforzo: **1 giorno di AI più una scelta politica. Chi: persona decide.** Indicare quali coperture del menu non ancora usate pagano le quattro misure del nucleo dal 2030. Scrivere se 06-C2 finisce nel 2029 o diventa una misura stabile, e con quale fonte.

**[Giudizio] Strumento serio o esercizio?** Per chi governa, ora è più vicino a uno strumento: il pacchetto si può portare a un ufficio legislativo come bozza. Per la cittadina resta un esercizio onesto ma lontano: i benefici arrivano dopo il 2030 e nessuna persona con nome li firma. Le tre condizioni del primo giro sono a questo punto: conti che tengono ogni anno (sì, con il calendario); una persona con nome che firma (non ancora); persone reali che mettono alla prova il lavoro degli agenti (non ancora, e il pacchetto è il posto giusto per cominciare).
