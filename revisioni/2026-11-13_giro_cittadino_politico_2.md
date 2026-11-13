# Giro di revisione: cittadinanza e decisori, 13 novembre 2026 (secondo giro)

*Revisione scritta da un agente AI che ragiona come una cittadina/un cittadino e come una persona con responsabilità politiche, 13 novembre 2026 (secondo giro); non è la revisione di una persona.*

*Base: il repository al commit 1af6a68 (13 novembre 2026, sera) e il sito pubblico visto lo stesso giorno. Il sito è allineato al repository: 9,4 mld, 67 misure su 78. Fa fede il repository. Legenda: **[Fatto]** verificato su file, con uno script o sul sito; **[Giudizio]** valutazione di questo agente.*

---

## In breve

| Voto (1-10) | Cittadina/o, 1° giro | Cittadina/o, ora | Politica/o, 1° giro | Politica/o, ora |
|---|---|---|---|---|
| Credibilità | 6 | **6** | 6 | **6** |
| Utilità | 5 | **6** | 7 | **7** |
| Fattibilità | 3 | **4** | 4 | **5** |
| Chiarezza | 4 | **5** | 6 | **6** |

**In una frase.** Il lavoro del pomeriggio ha risposto alla domanda più importante del primo giro: ora c'è un conto per ogni anno, e il programma ammette che "senza deficit" valeva solo a regime. È un passo vero. Ma il calendario che chiude i conti crea problemi nuovi, e alcuni sono seri:

1. **Il nucleo robusto non è completo in tutta la legislatura.** Parte al 43% nel 2027 e arriva al 100% solo nel 2033 (92% nel 2030, 99% nel 2032). Il documento 20 cita solo il 43% e il 74%. Circa tre quarti della spesa rinviata (5,9 mld) è spesa del nucleo e dei piloti, non delle "altre misure". **[Fatto: `annuale.py`, funzione `piano`]**
2. **Il ponte con i fondi europei è fragile.** 1,01 mld nel 2027 pagano spesa corrente del nucleo (personale dei nidi, Case della Comunità, Ufficio per il processo). Ma il registro dei fondi dice che la coesione 2021-2027 vale "solo spesa una tantum, non personale stabile" (`registro/fondi.csv`). Il calendario contraddice una regola del progetto.
3. **Le misure "di metodo" slittano al 2033.** La Legge sulla consulenza algoritmica pubblica (08-P1) è il primo punto dei "Primi 100 giorni" (20 §5), ma nel calendario comincia nel 2033. Lo stesso vale, in pratica, per riforme a costo zero.

Per la cittadina la pagina "Che cosa cambia per me" è il miglioramento più visibile: utilità e chiarezza salgono di un punto. Per chi governa la fattibilità sale di un punto: ora c'è un profilo annuale da portare alla Ragioneria. La credibilità non sale per nessuno dei due profili. I motivi sono tre: i nuovi problemi del calendario, i disallineamenti rimasti e il fatto che nessuna persona con nome firma ancora le scelte.

**Le priorità del primo giro.**

| Priorità | Esito | Commento breve |
|---|---|---|
| 1. Conti anno per anno | **Risolta in gran parte** | Tabella 2027-2035, ipotesi prudente e favorevole, calendario di avvio. Restano: 0,50 mld dopo il 2029 senza copertura, 06-C2 pagato prima di PE04, vincolo annuale fuori dall'ottimizzatore. |
| 2. Allineare i numeri | **A metà** | Corretti 5 punti su 10 (8,03%, punto 9 mancante, somma del sito, etichetta del margine, "100%" sulle misure forzate). Restano 21, 23, 20 §4 e README. |
| 5. "Che cosa cambia per me" | **Risolta in buona parte** | 8 profili chiari, con codici, versioni e incertezze. Mancano gli euro per persona e il profilo di chi paga le accise. |

---

## Che cosa è migliorato

- **C'è un conto per ogni anno, e dice la verità.** `programma/annuale_intermedio.md` mostra che con l'ipotesi prudente le risorse generali sono scoperte dal 2027 al 2034: 2,59 mld nel 2027, 7,11 mld in tutto. Il sito lo scrive in chiaro: "senza calendario mancherebbero fino a 2,6 mld". **[Giudizio]** Pochi programmi pubblicano il proprio buco.
- **Due ipotesi, entrambe visibili.** La prudente (le coperture rendono un anno dopo) e la favorevole (rendono dal primo anno). Anche con la favorevole restano scoperti 1,31 mld tra il 2029 e il 2033. Il calendario usa la prudente: è la scelta giusta per la credibilità.
- **Il calendario ha una regola sola e semplice.** Ogni anno la spesa sulle risorse generali non supera il gettito dell'anno. Il codice è breve e leggibile (`piano()` in `annuale.py`). Chiunque può rifare il conto.
- **Il prezzo del calendario è scritto.** Il documento 20 (§7) elenca le misure che partono nel 2033 e dice "anche il nucleo parte più piano". Il sito mostra la tabella completa e l'elenco "A pieno dal 2035".
- **La pagina "Che cosa cambia per me" esiste ed è buona.** Otto profili, frasi brevi, sigle spiegate (ISEE, INPS, CPIA). Per ogni voce: versione scelta, costo, "solo in prova", "solo regole". La sezione "Da sapere" dice anche le cose sgradite: Opzione donna chiusa, progetto di vita senza personale in tre ambiti su quattro, costi che passano alla clientela. Il controllo di coerenza verifica che ogni misura citata sia davvero nel programma (controllo 11).
- **La somma del sito ora torna.** "7,4 + 1,9 + 0,3 = 9,6 mld di risorse: 0,2 non spesi, di cui 0,09 tenuti da parte e 0,12 di fondi vincolati". Era il problema più visibile per una cittadina.
- **Le misure forzate non mostrano più "100%".** Nella tabella del sito la colonna dice "scelta politica". Era una delle falsità di precisione segnalate.
- **Il controllo di coerenza è cresciuto.** Da 5 a 11 controlli: conteggi di varianti e coperture, punti numerati, dato dei fondi europei, nucleo citato, profili.
- **La pagina sulle garanzie è onesta.** "Oggi c'è una sola persona" è scritto in alto. Il percorso per tappe è realistico: si comincia chiedendo a una persona di leggere una sola misura.

---

## Problemi rimasti

1. **Ancora nessun nome.** La pagina 24 dice che la persona responsabile "è indicata con nome e cognome sul sito", poi che "non nomina nessuno". Oggi la persona responsabile esiste: è chi ha avviato il progetto. Mettere il nome costa un'ora. Finché manca, la regola principale della pagina non è rispettata.
2. **Disallineamenti di testo non corretti.** **[Fatto]**
   - `21_idee_in_sintesi.md`: "aggiornato il 12 novembre", "76 proposte", "22 proposte formano il nucleo robusto". Non cita il calendario.
   - `23_equita_e_linguaggio.md` e la pagina Equità del sito: "Scenario di riferimento: intermedio, 9,2 mld l'anno". Il dato giusto è 9,38.
   - `20_programma_governai.md` §4: "63 misure con gettito" (sono 72, come dice lo stesso documento al §2). L'etichetta "Contributo di equità sulle pensioni più alte e risparmi dall'uscita dalle quote, 0,11" è la stessa segnalata nel primo giro.
   - `20` §2 e `README.md`: "76 proposte"; la home del sito dice 78.
   - `20` §6 punto 6: "tutte e 22 restano"; il nucleo è di 23.
3. **Il controllo di coerenza dà ancora una sicurezza in più del dovuto.** Risponde "nessun problema", ma non vede nessuno dei punti sopra. Cerca frasi esatte con espressioni regolari: "22 proposte formano il nucleo" e "63 misure con gettito" non hanno la forma attesa.
4. **06-C2 e PE04: il problema di tempo resta.** Il profilo pensioni dice: "Il risparmio paga la prova sul personale infermieristico (06-C2)". Ma il pilota è "triennale", parte nel 2027, e PE04 rende dal 2030. In più, nei conti il pilota resta a 0,35 mld l'anno per sempre (`anno_regime` 2029, nessuna fine). Delle due l'una: o finisce nel 2029, e PE04 non lo paga mai; o continua, e non è più un pilota.
5. **Il buco del 2030 non è chiuso.** I 0,50 mld che servono dopo il 2029 (03-P4, 05-C2, 05-C1, 09-C8, tutte del nucleo) sono contati a parte come "da rifinanziare" e tolti dalla spesa. Il calendario non li copre. La regola del 2029 usa per prima la riserva di 0,05, ma con il calendario quella riserva esiste solo dal 2035 (vedi "Problemi nuovi"). A questo si aggiungono, se i piloti vanno bene, 0,8 mld per 02-C5 essenziale.
6. **Il vincolo annuale è un controllo a valle, non un vincolo.** L'ottimizzatore sceglie ancora le misure guardando solo l'anno a regime. Poi il calendario scala tutto in proporzione. Una misura più lenta da finanziare non perde punti nella scelta.
7. **Tutto il resto del primo giro è ancora aperto**: verifica esterna dei costi, effetti per decili, interlocuzione con le Regioni, governo ombra fermo all'8 novembre, allerte in home (inflazione 5,6%) che non dicono che cosa fa il programma.

---

## Problemi nuovi

1. **Il nucleo resta incompleto per tutta la legislatura.** **[Fatto]** Quote del primo gruppo: 43% (2027), 74%, 88%, 92%, 96%, 99% (2032), 100% dal 2033. Se si vota nel 2027, la legislatura finisce nel 2032: nessuna misura del nucleo arriva a pieno prima della fine. Le "altre misure" partono nel 2033, cioè nella legislatura successiva. **[Giudizio]** Per un politico questo è il punto più difficile: è un programma che promette risultati a chi governerà dopo. Va detto in una riga, nel documento 20 e sul sito.
2. **Il peso del rinvio cade sul nucleo, ma il testo dice il contrario.** **[Fatto: calcolo da `piano()`]** Le "altre misure" sulle risorse generali valgono circa 0,26 mld l'anno (01-P13 0,16; 04-P9 0,03; 09-C9 0,03; 06-C10 0,02; 08-P1 0,015; piccole voci). Sui 5,9 mld rinviati, le "altre misure" pesano circa 1,4 mld (stima di questo agente dalle quote anno per anno). Il resto, circa tre quarti, è spesa del nucleo e dei piloti: nidi, Case della Comunità, Ufficio per il processo, prevenzione dei rischi. Il testo ("partono prima le misure del nucleo... le altre più tardi") fa pensare il contrario.
3. **Il ponte con la coesione contraddice la regola del registro.** **[Fatto]** `registro/fondi.csv`, voce COESIONE_2127: "Solo spesa una tantum, non personale stabile", e la capienza annua di 2,0 mld è una "stima GovernAI della quota riprogrammabile". Il calendario usa la capienza libera (1,01 mld nel 2027, 0,18 nel 2028) per pagare la spesa corrente del primo gruppo. Il 70% di quei fondi è nei programmi delle Regioni (20 §9). In più nel 2029 la coesione è già sopra la capienza: 2,06 contro 2,0 (`scoperto_vincolati` −0,06), e nessun documento lo dice.
4. **Il 2027 è un anno quasi fittizio.** Con l'ipotesi prudente le coperture rendono 0,14 mld nel 2027. Quasi tutta la spesa del 2027 (1,01 su 1,15) è pagata dal ponte europeo. **[Giudizio]** Un governo che entra in carica nel 2027 fa la sua prima legge di bilancio per il 2028. Partire dal 2028, con il 2027 dedicato a norme e bandi, sarebbe più realistico e più onesto.
5. **Le riforme a costo zero "partono" nel 2033.** Il calendario scala tutte le misure fuori dal primo gruppo, anche quelle che costano zero o quasi: 01-P1, 01-P2, 04-P4, 08-P7, 02-C1, 02-C3. **[Fatto]** In particolare 08-P1, la Legge GovernAI, è il primo dei "Primi 100 giorni" (20 §5) e compare sul sito tra le misure "A pieno dal 2035". Le regole senza costo dovrebbero partire subito, e il calendario dovrebbe dirlo.
6. **La riserva e i servizi per smettere di fumare arrivano nel 2035.** **[Fatto]** Il margine di 0,09 mld (0,04 per smettere di fumare, 0,05 di riserva) esiste solo a regime. Con il calendario tutto il gettito degli anni 2027-2034 va alla spesa rinviata: il margine è zero fino al 2035. Così l'accisa sul tabacco (AS01, 2028-2029) colpisce chi fuma con ISEE basso sei anni prima del suo servizio di compensazione. E la riserva per il dopo 2029 non c'è nel 2030, quando serve.
7. **Gli obiettivi "in 5 anni" non tengono conto del calendario.** **[Fatto: 22 e sito, "Ce l'avremo fatta se…"]**
   - Spesa delle imprese in ricerca da 0,8% a 0,9% del PIL "in 5 anni", legata a 01-P13. Ma 01-P13 comincia nel 2033.
   - Produttività da 100,4 a 104 "in 5 anni", legata a 01-P4. Ma 01-P4 è "fuori da questa versione" (22, riga 112; sito: "Non inclusa").
   - Posti al nido da 31,6 a 40 "in 5 anni", con il nido al 74-99% della spesa nella legislatura.
8. **Il congedo del papà ha date fisse, la spesa no.** Il profilo famiglia dice "un mese dal 2028, due mesi dal 2030". Il calendario dà a 02-C2 il 74% della spesa nel 2028 e il 92% nel 2030. Un congedo è un diritto: non si può dare al 74%. Bisogna dire se slitta il congedo o se si tagliano di più i posti al nido.
9. **04-P9: prima l'obbligo, poi l'aiuto.** Le zone a emissioni zero per le merci valgono "dal 2030", ma i contributi per cargo bike e ricarica alle microimprese "cominciano nel 2033". Chi consegna in città ha l'obbligo tre anni prima dell'aiuto.
10. **"Che cosa cambia per me" non dice quanto, per me.** "Che cosa ti può costare" mostra il gettito nazionale ("PE04 300 mln l'anno in tutto"), non quello per persona. La pagina dice che serve una microsimulazione. Per molti casi però basta un'aritmetica semplice:
    - pensione di 5.000 euro lordi al mese, inflazione 2%: circa 6-7 euro lordi al mese in meno il primo anno, che si sommano negli anni;
    - un pacchetto di sigarette al giorno: circa 15 euro al mese in più;
    - forfettario con 70.000 euro di ricavi: l'aumento si calcola dalla quota di reddito tra 50.000 e 70.000.
11. **Manca chi paga di più in numero di persone.** Le accise su tabacco, alcol e bevande zuccherate (AS01-AS04, 0,97 mld, circa 10 milioni di persone che fumano) non compaiono in nessun profilo. La pagina Equità le indica come regressive, con "Nessuna dedicata" come compensazione nella tabella; poche righe sotto lo stesso capitolo cita i 0,04 mld per smettere di fumare. Anche questo è un piccolo disallineamento interno.
12. **Il calendario non è uguale in tutti i profili.** Famiglia, scuola, anziani, imprese e Sud hanno la nota "43% nel 2027". Il profilo pensioni, che elenca le stesse Case della Comunità e squadre di quartiere, no. Nel profilo famiglia la stessa misura (02-C2) è ripetuta quattro volte con lo stesso titolo.
13. **PE04: "circa 0,1 il primo anno" vale solo con l'ipotesi favorevole.** Con la rampa prudente di `annuale.py` (6 anni, pieno nel 2035) PE04 rende circa 0,05 nel 2030. Inoltre la misura "dura 5 anni (2030-2034)" ma rende a pieno nel 2035, dopo la scadenza: il motivo (la base ridotta resta) è nella nota del CSV, non nei testi per il pubblico.
14. **Patent box descritto in due modi.** La variante essenziale di 01-P13 dice "patent box ridotto dal 110% al 50%" e si paga così. La copertura SF16 dice "nessun nuovo ingresso dal 2027 e uscita graduale". La pagina 22 dice "chiudendo il patent box". Va scritta una sola versione e va escluso un doppio conteggio.
15. **Piccoli refusi sul sito**: "piu'" e "citta'" con l'apostrofo nell'elenco "A pieno dal 2035".

---

## Numeri controllati

Ho ricontrollato 14 numeri tra documenti, CSV, script e sito pubblicato.

| # | Numero | Dove | Esito |
|---|---|---|---|
| 1 | Spesa dell'intermedio: 9,38 mld | 20, 21, 22, `selezione_intermedio.md`, sito (9,4) | **Coerente.** Ma **23** e pagina Equità: **9,2**. |
| 2 | Misure: 67 su 78 | 20, 21, 22, CSV (67 varianti scelte), sito | **Coerente.** Però README, 20 §2 e 21 dicono "76 proposte". |
| 3 | Nucleo robusto: 23 | 20 §1, sito | **Incoerente**: 21 "22 proposte formano il nucleo"; 20 §6 punto 6 "tutte e 22". |
| 4 | Coperture al minimo: 7,42 mld | `selezione_intermedio.md`, 22, sito (7,4), 23 (7,42 e "2,3 su 7,4") | **Coerente.** |
| 5 | Somma delle risorse sul sito: 7,4 + 1,9 + 0,3 = 9,6 | sito, Programma e In una pagina | **Ora coerente**: spiega gli 0,2 non spesi. |
| 6 | Scoperto prudente: 2,59 mld nel 2027, 7,11 in tutto | `annuale_intermedio.md`, sito ("fino a 2,6") | **Coerente.** Rifatto con lo script. |
| 7 | Scoperto favorevole: 1,31 mld, anni 2029-2033, massimo 0,54 | annuale, 20 §7 ("fino a 0,5, circa 1,3"), sito | **Coerente.** |
| 8 | Ponte UE 1,19 mld; spesa rinviata 5,92 mld | annuale, 20 §7 (1,2 e 5,9), sito | **Coerente**, e 5,92 + 1,19 = 7,11. Ma il ponte contraddice la regola del registro (problema nuovo 3). |
| 9 | Nucleo al 43% nel 2027 e 74% nel 2028 | annuale, 20, `profili.yaml`, sito | **Coerente**, ma il 20 non dice che il 100% arriva solo nel 2033. |
| 10 | Coesione 2029: 2,06 mld | `annuale.py`, registro (capienza 2,0) | **Oltre la capienza** di 0,06. Non citato nei documenti. |
| 11 | PE04: 0,30 a regime, "circa 0,1" nel 2030 | 20 §10, `coperture_menu.csv`, `annuale.py` | **Parziale**: 0,1 solo con l'ipotesi favorevole; prudente circa 0,05. |
| 12 | 06-C2 pilota: 0,35 mld | 20, CSV delle varianti, sito (350 mln) | **Coerente** sul costo. Ma "triennale" nel testo e permanente nei conti. |
| 13 | Coperture nel menu: 72 | README, 20 §2, `coperture_menu.csv` | **Coerente**, ma 20 §4 dice ancora **63**. |
| 14 | Dato dei fondi strutturali: 14,78% al 31 agosto 2026 | 20 §6 punto 7, scheda 09-C10 | **Corretto** (prima era 8,03%). |

**[Fatto]** `python sistema/coerenza.py` risponde "nessun problema tra documenti, scenari e sito". Non rileva i punti 1, 2, 3, 10, 11, 12 e 13.

---

## Le prossime 5 cose da fare

In ordine di priorità.

1. **Correggere il calendario di avvio.** Sforzo: **2-3 giorni**.
   - Le misure a costo zero o quasi (08-P1, 01-P1, 01-P2, 04-P4, 08-P7, 02-C1, 02-C3) partono subito, fuori dalla scala proporzionale. Allineare 08-P1 ai "Primi 100 giorni".
   - Usare il ponte europeo solo per spese una tantum ammissibili, come dice il registro; oppure dichiarare l'eccezione e dire che serve un accordo con le Regioni. Mostrare il calendario anche senza ponte.
   - Valutare l'avvio dal 2028, con la prima legge di bilancio.
   - Tenere da parte la riserva (0,05) e i servizi per smettere di fumare (0,04) dal primo anno dell'accisa, non dal 2035. Indicare una copertura per i 0,50 mld del 2030.
   - Decidere che cosa succede a 06-C2 dopo il 2029 e alle date del congedo del papà.
   - Scrivere nel 20 e sul sito: "il nucleo arriva a pieno nel 2033, dopo la fine della legislatura", con quale quota di nucleo si arriva al 2032.
2. **Chiudere i disallineamenti e rendere il controllo meno cieco.** Sforzo: **1 giorno**.
   - Correggere 21 (data, 76, 22, calendario), 23 (9,2), 20 §2, §4 (63, etichetta 0,11) e §6 punto 6, README (76).
   - Togliere o ricollegare gli obiettivi "in 5 anni" legati a 01-P4 (fuori) e a 01-P13 (dal 2033). Scrivere una sola versione del patent box.
   - Aggiungere a `coerenza.py` controlli più larghi: ogni numero seguito da "proposte" o "nucleo"; il totale nell'intestazione di 23; obiettivi legati a misure escluse o che partono dopo 5 anni; coesione sopra la capienza in qualche anno.
3. **Mettere un nome, oggi.** Sforzo: **1 ora per il nome; poi 4-8 settimane di calendario per le tappe 1 e 2**. La persona responsabile esiste già: va scritta con nome e cognome sul sito e nella pagina 24. Poi invitare le prime 1-5 persone a leggere una sola misura ciascuna, cominciando dal calendario di avvio e dalla pagina "per me".
4. **"Che cosa cambia per me", seconda versione.** Sforzo: **2-3 giorni**.
   - Un esempio in euro per ogni voce che si può calcolare senza microsimulazione: pensione di 5.000 euro, un pacchetto al giorno, forfettario a 70.000 euro, camion Euro 5, detrazioni sanitarie a 60.000 euro di reddito.
   - Un profilo per chi consuma e paga le accise (tabacco, alcol, bevande zuccherate) e uno per chi lavora come dipendente con reddito medio.
   - Per ogni voce: da quale anno, con la quota del calendario. La stessa nota in tutti i profili.
   - Unire le voci ripetute della stessa misura.
5. **Il "pacchetto per domani" per chi governa.** Sforzo: **1-2 settimane**. Era la priorità 4 del primo giro e non risulta avviata. Tre o quattro testi pronti, con relazione illustrativa e tecnica: 09-C10 art. 5, 01-P2, 04-P4, 08-P7. Sono a costo quasi zero: non dipendono dal calendario e possono partire subito. Per un politico è il modo più rapido di usare GovernAI.

**[Giudizio] Strumento serio o esercizio?** Ancora un esercizio serio, ma più vicino a uno strumento. Il conto annuale è la cosa che mancava di più, ed è arrivato. Ora il rischio è un altro: chiudere i conti in modo meccanico, rinviando in proporzione e con fondi europei a uso dubbio, invece di scegliere che cosa parte prima e perché. Le tre condizioni del primo giro restano valide: conti che tengono ogni anno (quasi), una persona con nome che firma (non ancora), persone reali che mettono alla prova il lavoro degli agenti (non ancora).
