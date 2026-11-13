# Giro di revisione: cittadinanza e decisori, 13 novembre 2026

*Revisione scritta da un agente AI che ragiona come una cittadina/un cittadino e come una persona con responsabilità politiche, 13 novembre 2026; non è la revisione di una persona.*

*Base: il repository al 13 novembre 2026, con le modifiche non ancora salvate in git, e il sito pubblico visto lo stesso giorno. Il sito è indietro di un giorno: mostra 9,2 mld e 66 misure, il repository 9,38 mld e 67 misure. Fa fede il repository. Legenda: **[Fatto]** verificato su file o sul sito; **[Giudizio]** valutazione di questo agente.*

---

## In breve

| Voto (1-10) | Cittadina/o, prima | Cittadina/o, ora | Politica/o, prima | Politica/o, ora |
|---|---|---|---|---|
| Credibilità | 6 | **6** | 6 | **6** |
| Utilità | 5 | **5** | 7 | **7** |
| Fattibilità | 3 | **3** | 3 | **4** |
| Chiarezza | n.d. | **4** | n.d. | **6** |

*La chiarezza non era valutata nel giro precedente.*

**In una frase.** In due giorni il progetto è diventato più onesto: le eccezioni sono dichiarate, i fondi europei sono classificati, le pensioni alte pagano qualcosa di concreto e ci sono regole su chi risponde. Ma i voti salgono poco, per tre motivi:

1. **"Senza deficit" vale solo a regime.** L'ottimizzatore non guarda gli anni 2027-2034. Un valutatore lo ha scritto (Y): negli anni di passaggio possono mancare tra 0,4 e 0,9 mld l'anno. Il programma lo cita in una riga, ma non corregge il calcolo.
2. **Ancora nessuna persona reale.** Le regole sulla persona responsabile e sul comitato ci sono. I nomi no. Tutti i giudizi restano di agenti AI.
3. **I numeri scivolano tra le pagine.** Il controllo di coerenza dice "nessun problema", ma ho trovato almeno otto disallineamenti (sezione "Numeri controllati").

La fattibilità per chi governa sale da 3 a 4. Il motivo è 09-C10: tre regole a costo zero sugli incentivi, scritte come modifica di una legge vigente (d.lgs. 184/2025). Si possono presentare come emendamento domani.

---

## A che punto siamo

### Che cosa è migliorato dal giro precedente

- **Le eccezioni hanno un nome e una condizione di uscita.** 09-C10 e 02-C5 restano pilota, anche se sono nel nucleo robusto. Il testo dice perché, quanto costerebbe la versione essenziale (0,02 e 0,8 mld) e che cosa deve succedere per passarci. Esempio: per 09-C10, tempi di istruttoria giù di almeno un terzo, con valutazione affidata ad altri. **[Giudizio]** È il modo giusto di fare un'eccezione.
- **Il conflitto di interesse su 09-C10 è dichiarato tre volte**: nella scheda, nel programma e nella pagina sulle garanzie. Raro in un programma politico.
- **I fondi europei dopo il 2029 sono classificati** misura per misura (`programma/coesione_dopo_2029.csv`): 21 misure "finiscono", 5 hanno un "successore", e le sperimentazioni sono trattate come "valutazione" nel sito. Il totale da sostituire è 0,50 mld l'anno. Il conto torna (0,25 + 0,15 + 0,08 + 0,02).
- **C'è una regola per il 2029, decisa ora.** Ordine: riserva di 0,05; gettito oltre il minimo, solo se certificato; poi tre misure scendono di versione, in un ordine scritto. Un politico lo apprezza: sa già che cosa succede se mancano i soldi.
- **PE04 ora paga qualcosa.** Prima il risparmio sulle pensioni sopra circa 3.700 euro lordi al mese finiva in un fondo che non spendeva nulla. Ora va alle risorse generali e finanzia il pilota sul personale infermieristico (06-C2).
- **Le tre regole su Invitalia e gli altri gestori** (09-C10, art. 5) sono la parte più matura di tutto il programma: compenso legato ai tempi, cruscotto trimestrale, niente nuove risorse per atto amministrativo senza valutazione sopra i 100 milioni. Il benchmark che le sostiene è solido e prudente: dice chiaro che il risparmio sui costi di gestione è piccolo e che il guadagno vero è il tempo.
- **Le tre proposte eque (X, Y, Z) sono indipendenti e motivate.** Tutte e tre arrivano al pilota 06-C2. La sintesi adottata è dichiarata.

### Che cosa resta aperto

- **Gli anni di passaggio.** Lo dice Y, con stime: gettito minimo circa 5,6 mld nel 2029 contro circa 6,5 di spesa. L'ottimizzatore non legge le colonne `anno_regime` e `gradualita` del menu delle coperture **[Fatto: in `programma/ottimizza.py` non compaiono]**. Il caso più chiaro: 06-C2 pilota costa 0,10 nel 2027, 0,25 nel 2028, 0,35 nel 2029 (`programma/varianti/06_salute.csv`). PE04, che dovrebbe pagarlo, parte nel 2030 con circa 0,1 e arriva a 0,3 nel 2035. Il pilota dura tre anni: finisce prima che la sua copertura renda.
- **Il "precipizio" del 2030 è più grande di 0,50.** Agli 0,50 da sostituire si aggiungono, se i piloti vanno bene, 0,8 mld per 02-C5 essenziale (promessa per la legge di bilancio 2030) e 0,02 per 09-C10. Nessuna copertura è indicata. La riserva è di 0,05.
- **Le persone.** La pagina `24_garanzie_e_responsabilita.md` è buona sulle regole del comitato. Non dice però **chi sceglie la persona responsabile**, né chi può revocarla, né chi paga i gettoni ("nessun costo per lo Stato" non dice da dove arrivano i soldi). Le proposte X, Y e Z lo dicevano; la sintesi lo ha perso.
- **La comunità è su invito e piccola.** La soglia del 10% delle persone iscritte per chiamare un'assemblea sorteggiata ha senso solo con molte persone iscritte.

---

## Pro della struttura

1. **Separare ciò che è robusto da ciò che è scelta politica.** Il motore SMAA prova 20.000 combinazioni di pesi. Dice: "questo conviene quasi con ogni sensibilità" (nucleo) oppure "questo dipende dai valori". **[Giudizio]** È l'idea più forte del progetto. Un politico ci trova un argomento: "anche con i vostri valori, questa misura sta in alto".
2. **Ogni scelta politica ha un prezzo scritto.** Quando chi guida il progetto forza una misura, il testo dice chi scende e chi esce (punti 4-10 del programma). Pochi programmi lo fanno.
3. **Vincoli prima dei pesi.** Linee rosse automatiche, controlli giuridici, gettito al minimo, nessuna evasione recuperata usata come copertura. Escludono in modo visibile SF15 (IVA, direttiva UE) e SAD11 (art. 56 TFUE). È disciplina vera.
4. **Le eccezioni dichiarate.** Sono un buon compromesso tra regola rigida e arbitrio: la regola resta, l'eccezione ha condizioni e una data.
5. **Il controllo giuridico preventivo cambia i testi.** L'art. 5 di 09-C10 è stato riscritto dopo l'esito "condizionato". Questo è utile, non decorativo.
6. **La catena di integrità** (42 versioni) e i file pubblici rendono visibile chi ha cambiato che cosa. Per la fiducia conta più della precisione dei numeri.
7. **Le revisioni AI con prospettive dichiarate** (red team di quattro aree, tre valutatori sulle scelte eque) fanno emergere errori veri: PE04 senza destinazione, il calendario della coesione, gli anni di passaggio.
8. **Il controllo di coerenza esiste.** Va esteso (vedi sotto), ma l'idea è giusta.

**Dove la complessità aiuta.** Nei conti e nelle regole: registro unico dei fondi, gettito minimo, linee rosse, classificazione dopo il 2029. Lì il dettaglio protegge da promesse facili.

## Contro della struttura

1. **Falsa precisione.** Le tabelle danno due decimali (0,09 di margine, 0,01 per 09-C10) su costi che sono "stime GovernAI" con forchette larghe (06-C2 piena: 1,5-2,5 mld). La colonna "Robustezza 100%" in `selezione_intermedio.md` vale 100% anche per le misure **forzate per scelta politica**: lì non misura niente. Una cittadina legge "100%" e pensa a una certezza.
2. **Instabilità delle soluzioni.** Una sola modifica del 13 novembre (PE04 nelle risorse generali) ha cambiato decine di righe nei programmi base e completo. Esempi: 02-C3 nel base passa da essenziale 0,35 a zero; 07-C6 da esclusa a pilota; 05-C10 nel completo da pilota a esclusa. Il base cambia anche se nessuno lo ha toccato. **[Giudizio]** Questo è il segno che l'ottimo è "piatto": molte combinazioni valgono quasi lo stesso. Va detto, altrimenti ogni ricalcolo sembra un ripensamento.
3. **Dipendenza da agenti AI, in tutti i ruoli.** Scrivono le proposte, le valutano, le controllano dal punto di vista giuridico, fanno il red team, simulano il governo e l'opposizione. Il programma lo dichiara con onestà. Ma l'accordo alto del panel (alfa 0,85) dipende anche dai molti zeri, e i valutatori non sono indipendenti da chi ha progettato il sistema. Senza un confronto con persone reali, il voto di credibilità non può salire.
4. **Il centro decisionale è una persona sola.** "Chi guida il progetto" ha fatto sei scelte politiche in cinque giorni (9, 10, 12 e 13 novembre). Il comitato di garanzia è sulla carta. Fino a quando non c'è, la regola "le persone decidono" significa "una persona decide".
5. **Il controllo di coerenza vede poco.** Confronta spesa e numero di misure, e alcune frasi vietate. Non ha visto i disallineamenti elencati sotto. Dà quindi una sicurezza maggiore di quella reale.
6. **Il governo ombra è fermo all'8 novembre.** La home lo mette in primo piano (11,63 mld, 55 misure), ma non ha discusso nessuna delle scelte del 12-13 novembre. Per chi legge, due "programmi" diversi convivono.
7. **Troppi strati per chi arriva dal sito.** Sei versioni del programma, quattro classi, quattro varianti, eccezioni, linee rosse, esiti giuridici ("Richiede notifica", "Condizionato"), allerte, scadenze UE, governo ombra. Ognuno ha senso. Insieme allontanano.
8. **"Senza tasse in più" è una formula delicata.** Il programma intermedio attiva SAD13 (uscita dal gasolio agevolato per autotrasporto e agricoltura entro il 2035, 0,80 mld) e le accise su tabacco, alcol e bevande. Il testo dice "oltre quelle già previste". È corretto, ma chi fa autotrasporto lo leggerà come una tassa nuova.

**Dove la complessità allontana.** Sul sito e nei documenti di sintesi. La cittadina non ha bisogno di sapere che cosa è lo SMAA. Ha bisogno di sapere che cosa cambia per lei, quando, e chi paga.

**Rischi da tenere d'occhio.**
- **Conflitto di interesse**: dichiarato su 09-C10, ma la stessa persona sceglie le eccezioni, le forzature e chi le firma. Serve che la valutazione di 09-C10 sia davvero esterna.
- **Accise "che tornano a chi le paga"**: vincolare alla sanità un importo pari al gettito del tabacco è una buona comunicazione. Ma quei soldi già pagavano la sanità nel modello. **[Giudizio]** Cambia l'etichetta, non i conti. Va detto così.
- **Dati di contesto allarmanti in home** (inflazione 5,6%, debito 139,9%): se sono veri, il programma deve dire che cosa cambia con questi dati. Oggi le allerte vivono separate dal programma di riferimento.

---

## Numeri controllati

Ho ricontrollato dieci numeri tra documenti, CSV, dati locali del sito (`docs/data.js`) e sito pubblicato.

| # | Numero | Dove | Esito |
|---|---|---|---|
| 1 | Spesa del programma intermedio: 9,38 mld | 20, 21, 22, `selezione_intermedio.md`, `docs/data.js` | **Coerente** nel repository. Il sito pubblicato mostra ancora 9,2 (versione del 12 novembre). |
| 2 | Misure: 67 su 78 | 20, 21, 22, CSV | **Coerente** nel repository; sito 66. Però README e 21 dicono "76 proposte" e la home "78 proposte": il lettore non sa da dove vengono le 2 in più (09-C9, 09-C10). |
| 3 | Fonti del programma sul sito: "7,4 da coperture + 1,9 coesione + 0,3 tariffe" | sito, pagina Programma | **Non torna**: la somma fa 9,6, non 9,2. Il 7,4 è il gettito delle coperture, non la spesa su risorse generali (7,22 ora, 7,01 prima). Una cittadina che fa la somma perde fiducia. |
| 4 | Margine di 0,09 | 20 §10: "0,04 per smettere di fumare, 0,05 di riserva" | **Contraddizione**: `selezione_intermedio.md` lo chiama "di cui riservato alla riduzione del deficit". |
| 5 | Fondo pensioni nel base e nel completo: 0,11 | 20 §4, riga "Rivalutazione ridotta delle pensioni più alte e risparmi dall'uscita dalle quote" | **Etichetta sbagliata**: dopo il 13 novembre PE04 è in un altro fondo. Gli 0,11 sono PE01 + PE02, cioè il **contributo di equità** sulle pensioni oltre 80.000 euro lordi l'anno, attivo nel base (robustezza 97%). E nel base quel fondo spende 0,00: un prelievo senza scopo, lo stesso problema appena corretto per PE04. |
| 6 | Pagamenti dei fondi strutturali | 20 §6 punto 7: "8,03% al 31 agosto 2025" | **Superato**: la scheda 09-C10 e il benchmark riportano 14,78% al 31 agosto 2026. Il benchmark stesso scrive che l'8,03% "va sostituito". |
| 7 | Coesione nell'intermedio: 1,90 su 2,00 | 20, 23, `selezione_intermedio.md` | **Coerente.** |
| 8 | Da sostituire dopo il 2029: 0,50 | X, Y, 23, `coesione_dopo_2029.csv` | **Coerente** (0,25 + 0,15 + 0,08 + 0,02). Ma non include 02-C5 essenziale dal 2030 (0,8). |
| 9 | Misure del nucleo robusto: 23 | 20 §1, sito | **Incoerente**: 21 dice "22 proposte formano il nucleo"; 20 §6 punto 6 dice "tutte e 22 restano". |
| 10 | Varianti e coperture | README: 152 varianti, 59 coperture; 20 §2: 184 varianti, 63 coperture; §4: 63 | **Incoerente con i file**: `coperture_menu.csv` ha 72 righe; le varianti distinte sono 233. |

**Altri disallineamenti di testo.**
- 20 §6 salta dal punto 8 al punto 10: manca il 9.
- 21, punto "Ricerca": "restano pieni il credito unico per la ricerca e le consegne pulite". Dal 13 novembre il credito (01-P13) è essenziale. L'intestazione di 21 dice ancora "aggiornato il 12 novembre".
- 21, punto 4: "il personale infermieristico nuovo (06-C2) resta fuori o solo sperimentale" va bene, ma non dice che ora è finanziato.
- La scheda `programma/schede/06_salute.md` non è stata aggiornata il 13 novembre: non c'è il pilota 06-C2 nell'intermedio, né PE04, né il vincolo del gettito del tabacco.
- 20 §7: "Il panel dovrebbe valutare direttamente le varianti": invariato da settimane, ed è la radice della falsa precisione.

**[Fatto]** `python sistema/coerenza.py` risponde "nessun problema tra documenti, scenari e sito". Nessuno dei punti 3-6 e 9-10 è coperto dal controllo.

---

## Che cosa userebbe un politico domani

**Userebbe subito (con poco lavoro).**
1. **09-C10, art. 5: le tre regole sugli incentivi alle imprese.** Sono scritte come modifiche del d.lgs. 184/2025 e della legge 196/2009. Costo zero. Toccano un problema documentato dalla Corte dei conti (Contratti di sviluppo FSC: 2,0 mld assegnati, circa 70 milioni pagati a luglio 2025). È un emendamento pronto per la prossima legge di bilancio o per un decreto.
2. **Il pilota di 09-C10 in una Regione**, senza legge nazionale, con la sola assistenza tecnica: la scheda lo dice esplicitamente. Un assessore può partire.
3. **Le misure "di metodo" a costo quasi zero**: 01-P2 (spese fiscali a scadenza), 01-P1 (bilancio generazionale), 04-P4 (nessuna grande opera senza prova dei numeri), 08-P7 (appalti a vetro). Sono anche quelle che uniscono le quattro aree del red team.
4. **La tabella "dopo il 2029"** come lista di controllo per chi scrive la legge di bilancio 2028-2029: dice quale spesa finisce e quale no.
5. **Il metodo "prezzo dichiarato"** per le scelte politiche: si può copiare in qualunque relazione illustrativa.

**Scarterebbe o metterebbe da parte.**
- I totali a due decimali come cifra da comunicare: nessuno staff di ministero firma una cifra non bollinata dalla Ragioneria.
- La simulazione del governo ombra: interessante, ma superata dalle scelte successive e fatta solo da agenti.
- La parte allerte e scadenze UE: utile, ma esistono già strumenti istituzionali per questo. Qui distrae.

**Che cosa manca per farne uno strumento di governo.**
- **Un profilo anno per anno, 2027-2035**, almeno per spesa e coperture principali. Senza, la frase "senza deficit" non regge davanti alla Ragioneria o all'UPB.
- **Una copertura per il 2030**: 0,50 da sostituire più 0,8 per 02-C5 se il pilota va bene.
- **Una verifica esterna dei costi** su 5-10 misure grandi (02-C2, 06-C3, 03-P4, 05-C2, 06-C2) da parte di persone con esperienza di relazioni tecniche.
- **Effetti distributivi per decili.** Il capitolo equità lo ammette: senza microsimulazione non si sa se il programma riduce le disuguaglianze.
- **Un'interlocuzione con le Regioni.** Molte misure (piloti in 3-4 Regioni, coesione regionale per circa il 70% delle risorse non impegnate) dipendono da loro.

---

## Che cosa capisce un cittadino

**Capisce.**
- Lo slogan: "L'AI propone e verifica. Le persone decidono".
- Che il programma non vuole fare deficit e dice chi paga.
- Alcune misure concrete: nido gratis fino a ISEE 25.000 dove mancano posti, congedo papà di 2 mesi, Case della Comunità, 500 squadre infermieristiche di quartiere, borse di studio garantite. La pagina "Una pagina" aiuta, con gli obiettivi "Ce l'avremo fatta se…".
- Che la sanità è ammessa come punto debole. Questa onestà crea fiducia.

**Lo confonde.**
- Sei versioni del programma, più il governo ombra. Quale è "il" programma?
- Codici (06-C2, PE04, SAD13) dentro frasi lunghe. Il primo paragrafo del programma intermedio è una frase di oltre 150 parole.
- Etichette tecniche sul sito: "Nucleo robusto", "In coda", "Richiede notifica", "Condizionato", "100%".
- Somme che non tornano (7,4 + 1,9 + 0,3).
- "Pilota", "essenziale", "eccezione dichiarata": per la cittadina vogliono dire "forse".

**Lo allontana.**
- Non trova una risposta alla domanda "che cosa cambia per me". Nessuna pagina dice, per esempio: "se hai una pensione di 5.000 euro lordi, dal 2030 perdi circa 6 euro al mese il primo anno". Il calcolo c'è, nella proposta X; non arriva al sito.
- Non trova una persona con nome e cognome. "Chi guida il progetto" è anonimo, e il comitato non esiste ancora.
- La comunità è su invito: chi arriva non può partecipare subito.
- Le allerte in home (inflazione 5,6%, debito 139,9%) fanno paura, ma non dicono che cosa fa il programma in risposta.

**Si fida?** In parte. Si fida del tono: ammette i limiti, dichiara i conflitti, mostra le fonti. Non si fida del fatto che dietro ci siano solo agenti AI e una persona senza nome.

---

## Le 5 cose da fare per prime

In ordine di priorità.

1. **Conti anno per anno, 2027-2035.** Far leggere all'ottimizzatore `anno_regime` e `gradualita`, e aggiungere un vincolo di saldo per ogni anno, o almeno una tabella di controllo. Mostrare il buco degli anni di passaggio e la copertura del 2030 (0,50 più 0,8 per 02-C5). Spostare o accorciare 06-C2 pilota se PE04 non lo paga in tempo. **Sforzo: 2-4 giorni di lavoro, più l'aggiornamento dei documenti.**
2. **Allineare i numeri e allargare il controllo di coerenza.** Correggere i dieci punti della sezione "Numeri controllati" (8,03%, nucleo 22/23, §9 mancante, etichetta del fondo pensioni, "riduzione del deficit", conteggi di varianti e coperture, somma del sito, testo di 21, scheda 06). Decidere che cosa fare di PE01-PE02 nel base: o una destinazione, o fuori. Aggiungere a `coerenza.py` questi controlli. Pubblicare il sito. **Sforzo: 1-2 giorni.**
3. **Mettere persone vere.** Nominare la persona responsabile e la vice, con nome. Completare la pagina 24: chi la sceglie, chi la revoca, chi paga i gettoni. Pubblicare l'avviso per il comitato. Chiedere a 3-5 persone esterne, di aree diverse, una revisione scritta, e a un piccolo panel di persone di dare un punteggio a 10-15 misure, per confrontarlo con quello degli agenti. **Sforzo: 4-8 settimane di calendario, poche ore di lavoro a settimana; costo basso.**
4. **Un "pacchetto per domani" per chi governa.** Tre o quattro testi pronti, con relazione illustrativa e relazione tecnica in formato parlamentare: 09-C10 art. 5, 01-P2, 04-P4, 08-P7. Farli leggere a una persona con esperienza di uffici legislativi. Indicare per ciascuno il veicolo (legge di bilancio, decreto, legge regionale). **Sforzo: 1-2 settimane.**
5. **"Che cosa cambia per me", sul sito.** Una pagina con 6-8 profili tipo: famiglia con un bambino piccolo al Sud, pensionato con 5.000 euro lordi, autotrasportatore, chi fuma con ISEE basso, infermiera in un'area interna, persona con disabilità, piccola impresa che chiede un incentivo. Per ciascuno: che cosa cambia, da quando, quanto, con quale certezza. Sostituire le etichette tecniche con parole semplici e arrotondare le cifre a un decimale. **Sforzo: 3-5 giorni.**

**[Giudizio] Strumento serio o esercizio?** Oggi è un esercizio serio. Il metodo è serio: vincoli prima dei valori, prezzi dichiarati, eccezioni con condizioni, tracciabilità. Diventa uno strumento quando succedono tre cose: i conti tengono anno per anno, una persona con nome firma le scelte, e almeno un gruppo di persone reali ha messo alla prova il lavoro degli agenti.
