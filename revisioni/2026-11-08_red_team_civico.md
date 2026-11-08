# Red team civico: GovernAI letto da chi sta fuori dai partiti

*8 novembre 2026. Prospettiva: partecipazione civica, liste civiche, associazionismo, civic tech, astensionisti. Parere indipendente: non ho letto le altre revisioni. Legenda: [Fatto] = verificato nei documenti, con file; [Valutazione] = mia lettura; [Ipotesi] = da verificare.*

## Giudizio in 5 righe

GovernAI è serio, onesto sui conti e sui propri limiti: più di quanto un elettore deluso si aspetti dalla politica.
Ma oggi è un sistema **per** i cittadini, non **dei** cittadini: le persone osservano, gli agenti decidono, pochi membri anonimi filtrano.
La promessa post-ideologica regge sul metodo, non sul contenuto: le scelte rivelano un orientamento riformista, europeista e di rigore, da dichiarare.
Il rischio più grande non è l'AI, è il "leaderismo nascosto": chi scrive la Carta e approva le richieste non ha volto né regole.
Prima di altro codice serve una comunità: un'assemblea vera, presìdi fisici e una governance scritta del progetto.

| Voto | /10 |
|---|---|
| Utilità | 7 |
| Credibilità | 6 |
| Neutralità percepita | 5 |
| Idee (qualità delle proposte) | 7 |

---

## 1. Prima impressione: suo, distante o sospetto?

**L'attivista civico lo sentirebbe affine nei principi.** [Fatto] Il sito si presenta con il motto "L'AI propone e verifica. Le persone decidono" e con limiti dichiarati: stime non certificate dalla Ragioneria, governo ombra simulato (`docs/app.js`, funzione `metodo`). Il programma dichiara che il panel è fatto di agenti "indipendenti da chi ha scritto le proposte ma non da chi ha progettato il sistema" (`20_programma_governai.md`, §2). [Valutazione] Questa franchezza è rara e piace a chi è stanco di slogan.

**L'elettore comune lo sentirebbe distante.** [Fatto] Il verbale della seduta "Conti in ordine" pesa circa 348 KB. Le decisioni sono scritte in sigle: SAD, RIALLOCAZIONE, M002, RGS, ESSENZIALE, "regola 8" (`governo/verbali/2026-11-08-1-conti-in-ordine.md`). [Valutazione] Un astensionista non arriva alla seconda riga. La progettazione dei percorsi utente è buona (`design/02_architettura.md`, §7.1, "In breve" sopra la piega), ma il materiale di partenza resta da tecnici per tecnici.

**L'astensionista lo guarderebbe con sospetto, per tre motivi.**
1. *Un "governo" senza persone.* [Fatto] Capo di governo, ministri, opposizione ed esperti sono agenti AI (`governo/regolamento.md`). Il capo scrive in prima persona ("non lo nascondo", "mi discosto") e registra circa 30 deroghe all'esito del motore in una sola seduta (verbale, sezione "Deroghe"). [Valutazione] A chi diffida dei palazzi sembra un palazzo nuovo, solo più ordinato.
2. *Chi c'è dietro?* [Fatto] Le domande dei cittadini passano solo dopo l'approvazione di "un membro del progetto" (`governo/richieste/README.md`; `CONTRIBUTING.md`). Non ho trovato nei documenti chi siano i membri, come si diventa membri, né chi può modificare la Carta. [Valutazione] Per questo elettorato è il primo campanello d'allarme: è la domanda che ha affossato molte esperienze "dal basso".
3. *GitHub come porta d'ingresso.* [Fatto] Per partecipare "serve un account GitHub gratuito" (`docs/app.js`, funzione `partecipa`). [Valutazione] È una porta per sviluppatori, non per la pensionata di un'area interna o per il volontario della Caritas.

## 2. La promessa post-ideologica regge?

**Sul metodo, sì, ed è il punto più forte.** [Fatto] La Carta non sceglie un unico insieme di pesi e separa le proposte "robuste" da quelle "dipendenti dai valori", che vanno "ai cittadini e al Parlamento" (`01_carta_valori.md`). Il benchmark mostra convergenze sia con il governo sia con le opposizioni (`benchmark/confronto_programmi.md`). [Valutazione] Rendere visibili i valori invece di nasconderli è la risposta giusta all'accusa di falsa neutralità.

**Sul contenuto, un orientamento c'è.** [Valutazione] Non è destra né sinistra, ma è riconoscibile: riformismo tecnocratico, europeista, di rigore fiscale e di valutazione d'impatto. Esempi:
- [Fatto] "Nessuna spesa in deficit" è una linea rossa (art. 81 nella Carta, valore FUT). La Difesa al 3,5% è classificata "Sfav. · linea rossa" (`20_programma_governai.md`, 07-C5). [Valutazione] Chi mette la sicurezza esterna al primo posto leggerà un giudizio politico travestito da vincolo contabile, anche se il documento lo ammette (§6).
- [Fatto] Le coperture del programma completo colpiscono case di valore alto (SF13), cedolare secca libera (SF11), successioni oltre 500.000 euro (SF14), IVA sul gas domestico (SAD12) (`programma/coperture_menu.csv`). [Valutazione] Sono scelte redistributive e ambientaliste: legittime, ma con un colore.
- [Fatto] 08-P4 chiede una capacità fiscale UE permanente; 02-C4 si prova con un pilota randomizzato. [Valutazione] È la cultura dell'evidenza, legittima ma riconoscibile.
- [Fatto] Lacune dichiarate: premierato, migrazioni e cittadinanza, nucleare, abuso d'ufficio (`benchmark/confronto_programmi.md`). [Valutazione] Proprio i temi identitari mancano: la neutralità qui coincide con l'assenza.
- [Fatto] Il panel è AI e "l'accordo alto tra loro dipende anche dai molti punteggi a zero" (`20_programma_governai.md`, §2). [Ipotesi] Più agenti dello stesso tipo di modello possono condividere lo stesso bias culturale; l'alfa di Krippendorff 0,85 non lo esclude.

**Come gestirlo senza fingere.**
1. Una pagina "Il nostro orientamento" che dica in chiaro: rigore di bilancio, europeismo, valutazione delle politiche. Chiamarlo "orientamento di metodo" è più credibile che "né destra né sinistra".
2. Presentare la scelta di Difesa, coperture strutturali e dividendo climatico come **schede di opzioni** alla pari, senza etichetta "sfavorevole" nel titolo.
3. Far valutare le stesse proposte da un panel umano plurale (almeno tre sensibilità) e pubblicare la differenza con il panel AI.
4. Riempire le lacune identitarie con schede di opzioni, come suggeriscono gli stessi ricercatori del benchmark.

## 3. Partecipazione: le persone decidono davvero qualcosa?

**Oggi, no.** Vediamo i canali uno per uno.

| Canale | Che cosa fa oggi | Lettura civica |
|---|---|---|
| Partecipa via GitHub | [Fatto] Issue con modulo; un membro approva; l'AI risponde con diagnosi e tre opzioni (`CONTRIBUTING.md`). Analisi pubblicate: zero (`docs/data.js`, `"analisi":[]`) | [Valutazione] È una cassetta dei suggerimenti con filtro. Chi propone non decide nulla, e il filtro non ha criteri pubblici |
| Domanda al Consiglio | [Fatto] Approvazione di un membro, poi seduta degli agenti. La seduta "Conti in ordine" nasce da un file in `governo/richieste/`, cioè dal canale dei membri | [Valutazione] La prima domanda "vera" l'ha scritta l'interno. Il cittadino chiede, gli agenti decidono |
| Simulatore "I tuoi valori" | [Fatto] Riordina le proposte con i pesi del singolo (`design/02_architettura.md`) | [Valutazione] Utile per capire, ma è un gioco individuale: nessuno ne aggrega i risultati |
| Assemblea dei sorteggiati | [Fatto] Prevista da 08-P1: 150 persone, sorteggio certificato ISTAT, indennità, rinnovo per metà ogni anno. Decide solo la "matrice dei valori" e "non vincola le Camere né il Governo" (`programma/schede/08_esteri.md`, art. 6) | [Valutazione] Ottimo disegno, ma esiste solo dopo una legge dello Stato. E ai cittadini lascia i pesi, non le scelte |
| Pesi democratici | [Fatto] Il motore userà i pesi dell'assemblea "quando avrà espresso i suoi pesi" (`01_carta_valori.md`, regola 8) | [Valutazione] Oggi i pesi sono di nessuno: tutte le combinazioni, cioè di fatto quelle scelte dall'architettura |

**Che cosa manca per una partecipazione reale e inclusiva.**
1. **Un'assemblea civica del progetto, subito**, non dopo una legge: 40-60 persone sorteggiate (anche con liste civiche, associazioni, CAF, parrocchie, biblioteche come bacini), che fissino i pesi e votino sulle 3 decisioni politiche aperte del §6.
2. **Canali non digitali**: modulo cartaceo, numero di telefono, incontri in biblioteca o nelle sedi del terzo settore, con un "facilitatore" che trascrive. La scheda 09-C5 prevede "Punti digitali facilitati per gli over 65": il progetto dovrebbe applicarlo a sé.
3. **Un modulo web senza GitHub**, con risposta garantita entro una data.
4. **Criteri pubblici di ammissione** delle richieste e registro dei rifiuti motivati.
5. **Restituzione**: a ogni partecipante una risposta in linguaggio semplice su che cosa è cambiato grazie al suo contributo. È il punto su cui falliscono quasi tutte le consultazioni.
6. **Un potere vero**, anche piccolo: la comunità decide l'ordine del giorno di una seduta al mese.

## 4. Le idee: che cosa parla a questo elettorato

**Le 5 che parlano di più.**
1. **08-P7 Appalti a vetro.** [Fatto] Cruscotto pubblico dei rischi; il 54,8% degli appalti competitivi ha un'offerta unica (verbale, decisione 08-P7). [Valutazione] Trasparenza concreta, costo minimo (0,01 mld), misurabile: è il linguaggio dei comitati civici.
2. **09-C2 Chiedilo una volta sola.** [Fatto] Indennizzo di 30 euro al cittadino se l'ente chiede un dato che lo Stato ha già; cruscotto per vedere chi ha consultato i propri dati (`programma/schede/09_pa_digitale.md`). [Valutazione] Il cittadino diventa titolare di un diritto, non utente paziente.
3. **07-C4 Dal bene confiscato al bene comune.** [Fatto] Rafforzamento ANBSC, fondo rotativo, open data georeferenziato su ogni bene (verbale). [Valutazione] Parla direttamente all'associazionismo antimafia e al terzo settore.
4. **04-P4 Nessuna grande opera senza prova dei numeri.** [Fatto] Valutazione indipendente, "Ponte compreso"; sforamento medio dei costi del 28% (verbale; benchmark). [Valutazione] Risponde al rifiuto dei giochi di potere sulle opere bandiera.
5. **08-P3 Votare dove si vive e regole stabili.** [Fatto] Voto fuorisede strutturale e divieto di cambiare la legge elettorale nei 12 mesi prima del voto (`08_esteri.md`). [Valutazione] Tocca il cuore dell'astensione involontaria e delle regole cambiate dai vincitori.

Menzione: 05-C5 Scuole aperte come presidi di comunità e 04-P6 aree interne, molto vicine alle liste civiche dei piccoli comuni.

**Le 5 che lascerebbero freddi o allontanerebbero.**
1. **08-P1 Legge GovernAI, così com'è.** [Fatto] Un ufficio di 70 unità presso le Camere, tre membri nominati dai Presidenti delle Camere; ai cittadini solo i pesi (`08_esteri.md`, artt. 3 e 6). [Valutazione] È la proposta-simbolo, ma l'astensionista legge "nuovo ufficio, nomine dall'alto, AI". E un movimento che fa della propria tecnologia la prima legge dei 100 giorni sembra parlare di sé.
2. **01-P3 IVA in tempo reale.** [Fatto] Blocco preventivo motivato fino a 30 giorni (verbale). [Valutazione] Giusta contro le frodi, ma il piccolo artigiano civico la sente come un'arma contro di lui. Va raccontata con le garanzie in testa.
3. **02-C4 Reddito di inclusione, pilota randomizzato.** [Fatto] Randomizzazione a livello di nucleo con gruppo di controllo (verbale). [Valutazione] Per chi lavora nel sociale, "estrarre a sorte chi aiutare" è difficile da accettare, anche se il gruppo di controllo conserva le misure esistenti.
4. **Le coperture del programma completo (SF13, SF11, SF14, SAD12).** [Fatto] IMU su prime case di valore alto, fine della cedolare libera, IVA sul gas domestico al 22% con bonus per ISEE fino a 15.000 euro (`coperture_menu.csv`). [Valutazione] Il ceto medio proprietario, molto presente tra i delusi, sente "nuove tasse sulla casa e sulle bollette".
5. **08-P4 Capacità fiscale UE.** [Valutazione] Non respinge, ma lascia freddi: lontana dalla vita quotidiana.

**Che cosa manca, da questo punto di vista.** [Fatto] Nelle schede non compaiono una legge sulle lobby, il conflitto di interessi, il bilancio partecipativo, né misure per il terzo settore (ricerca testuale in `programma/schede/`: nessuna occorrenza su lobby e bilancio partecipativo). [Valutazione] Sono le prime tre richieste di un elettorato civico. La loro assenza pesa più di ogni proposta discutibile.

## 5. Il metodo AI: antidoto o nuovo potere opaco?

**Elementi di antidoto.** [Fatto] Ruoli separati, verbali pubblici, catena di integrità, previsioni con punteggio di Brier, opposizione leale che deve dire "che cosa le farebbe cambiare idea", risposta scritta del capo a ogni obiezione (`governo/regolamento.md`). [Valutazione] Il verbale mostra un'opposizione che morde e un capo che accoglie le obiezioni, per esempio sulla copertura RB05 tolta alle madri. È più rendicontazione di quanta ne veda in molte giunte.

**Elementi di potere opaco.**
- [Fatto] Il regolamento vieta all'opposizione di "proporre misure proprie fuori dal programma" e agli esperti di esprimere preferenze politiche. [Valutazione] Il perimetro del dibattito è fissato a monte: si discute solo dentro le 62 proposte.
- [Fatto] Gli agenti seguono istruzioni (`governo/ruoli/`) che qualcuno ha scritto. [Valutazione] Il vero potere è di chi scrive prompt, rubrica e Carta. Oggi non c'è una regola pubblica su chi li cambia e con quale procedura.
- [Fatto] La Carta è già alla versione 2.0 dopo pochi giorni (7 novembre 2026). [Valutazione] Bene che evolva; male che non si sappia chi ha deciso di aggiungere tre valori.
- [Valutazione] La catena di integrità prova che un testo non è stato manomesso, non che sia giusto.

**Che cosa servirebbe per fidarsi.**
1. **Una governance scritta del progetto**: chi sono i membri, come si entra, chi approva, conflitti di interesse, finanziamenti.
2. **Un comitato di garanzia plurale e umano**, con almeno un membro sorteggiato, che approva ogni modifica a Carta, rubrica, ruoli e regolamento. Le modifiche entrano solo dopo un periodo di commento pubblico.
3. **Diritto di veto della comunità** su una modifica alla Carta, con soglia chiara.
4. **Audit esterni periodici** sui prompt e test di bias su temi divisivi, come previsto per l'Ufficio in 08-P1 (art. 8): applicarli prima a sé stessi.
5. **Un'opposizione libera di proporre**: almeno un "controprogramma" per seduta, scritto da persone.

## 6. Lezioni dalle esperienze civiche e digitali

**Errori che rischia di ripetere.**
- *Piattaforma di proprietà di pochi.* [Fatto esterno] La piattaforma Rousseau del M5S era gestita da un'associazione privata ed è stata oggetto di rilievi del Garante privacy sulla sicurezza (provvedimento del 2019) e di contestazioni sulla trasparenza del voto. [Valutazione] Il rischio per GovernAI è identico: chi possiede il repository possiede il movimento.
- *Partecipazione digitale che si svuota.* [Fatto esterno] I sistemi di "democrazia liquida" dei Pirati tedeschi (LiquidFeedback) hanno avuto partecipazione calante e concentrata in pochi attivisti. [Ipotesi] Sui numeri esatti non ho una fonte verificata.
- *Promesse non mantenute.* [Fatto esterno] In Francia la Convention citoyenne pour le climat (150 sorteggiati, 2019-2020) aveva ricevuto la promessa di una ripresa "senza filtro" delle proposte; molte sono state poi modificate o scartate. [Valutazione] Se l'assemblea fissa i pesi e poi il "capo" AI deroga 30 volte, l'effetto è lo stesso.

**Esperienze da cui imparare.**
- [Fatto esterno] Irlanda: le assemblee di cittadini (2016-2018) hanno preparato referendum poi vinti, perché il Parlamento si era impegnato a rispondere.
- [Fatto esterno] Ostbelgien: dal 2019 un Consiglio dei cittadini permanente sceglie i temi delle assemblee sorteggiate. È il modello più vicino a ciò che serve a GovernAI.
- [Fatto esterno] Taiwan (vTaiwan, Pol.is): strumenti che cercano il consenso tra gruppi diversi, non la maggioranza. Coerente con l'idea di "nucleo robusto".
- [Fatto esterno] Italia: la Toscana ha una legge regionale sulla partecipazione con un'Autorità dedicata (l.r. 46/2013); la piattaforma pubblica per le firme di referendum e leggi di iniziativa popolare è attiva dal 2024. Sono alleati istituzionali naturali.

**Che cosa fare nei prossimi 6-12 mesi.**
1. **Mesi 1-2.** Pubblicare governance, nomi dei membri, fonti di finanziamento, procedura di modifica della Carta. Aprire un modulo senza GitHub e un recapito non digitale.
2. **Mesi 2-4.** Un'assemblea civica pilota di 40-60 sorteggiati, con facilitazione professionale e indennità, su un solo tema (per esempio le 3 decisioni politiche aperte). Impegno scritto: il programma recepisce o motiva ogni scostamento.
3. **Mesi 3-6.** Dieci incontri in presenza con liste civiche, associazioni e piccoli comuni (aree interne, periferie), con una versione stampabile di due pagine per area.
4. **Mesi 4-8.** Panel umano plurale che rivaluta il nucleo robusto; pubblicare il confronto con il panel AI.
5. **Mesi 6-12.** Aggiungere al programma lobby, conflitto di interessi, bilancio partecipativo e terzo settore. Una prima seduta del governo ombra con ordine del giorno scelto dalla comunità e un "ministro" umano affiancato a ciascun agente.
6. **Sempre.** Misurare la comunità, non il sito: persone attive, contributi accolti, quota di partecipanti non digitali, risposte restituite.

## 7. Voti

| Criterio | Voto | Motivazione |
|---|---|---|
| Utilità | **7** | Strumento prezioso per capire costi, coperture e compromessi; poco usabile da chi non è già esperto. |
| Credibilità | **6** | Conti prudenti e limiti dichiarati; pesano agenti senza volto e assenza di governance del progetto. |
| Neutralità percepita | **5** | Metodo plurale, ma contenuti riconoscibili (rigore, europeismo, coperture sulla casa) e lacune sui temi identitari. |
| Idee (qualità delle proposte) | **7** | Proposte concrete, finanziate e verificabili; mancano lobby, conflitto di interessi e partecipazione locale. |
