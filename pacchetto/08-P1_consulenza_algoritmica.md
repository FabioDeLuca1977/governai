# 08-P1 — Valutazione d'impatto pubblica con l'intelligenza artificiale presso l'Ufficio parlamentare di bilancio

*Testo preparato da un agente AI per GovernAI il 13 novembre 2026, a partire dalle schede e dai controlli giuridici del programma. Non è stato rivisto da una persona esperta: va verificato prima di essere presentato.*

Variante del programma intermedio: **ESSENZIALE** (intensità 0,6). È una sezione di valutazione algoritmica **dentro l'Ufficio parlamentare di bilancio (UPB)**, di circa 30 unità. La valutazione d'impatto pubblica (VIP-AI) riguarda solo la legge di bilancio, i decreti-legge e i disegni di legge con oneri sopra lo 0,1% del PIL. C'è un'Assemblea civica di 100 persone sorteggiate, con una sessione l'anno. Il *comply or explain* vale solo per la legge di bilancio. Costo: 6 milioni nel 2027, 12 nel 2028, 15 dal 2029. Nel calendario di avvio è tra le riforme a costo quasi zero che partono subito. Fonti interne: `programma/schede/08_esteri.md` (08-P1), `programma/varianti/08_esteri.csv`, `giuridico/conformita*.csv` (righe 08-P1, ambiti COS e UE), `giuridico/note_COS.md`, `programma/coperture_menu.csv` (RA03), `dati/verifiche/08_esteri.md`.

Nota di trasparenza: GovernAI è un programma costruito con agenti di intelligenza artificiale. La misura riguarda l'uso dell'AI nelle istituzioni. Chi la presenta deve poter dire che non favorisce alcun fornitore né alcun progetto: per questo il testo impone codice aperto, infrastruttura sotto giurisdizione UE e la possibilità di cambiare modello.

---

## 1. Scheda in breve

- **Che cosa fa.** Dentro l'UPB nasce una sezione che usa sistemi di intelligenza artificiale, sotto la responsabilità di persone, per pubblicare una valutazione d'impatto (VIP-AI) dei provvedimenti più pesanti: legge di bilancio, decreti-legge, disegni di legge con oneri sopra lo 0,1% del PIL. La VIP-AI dice chi guadagna e chi perde (per reddito, territorio, età, genere), che effetti ci sono nel breve, medio e lungo periodo e con quale incertezza. Non dà raccomandazioni e non vincola nessuno. Un'Assemblea civica di 100 persone sorteggiate fissa ogni anno i pesi tra i valori usati di base. Sulla legge di bilancio il Governo spiega per iscritto perché ignora gli effetti negativi di lungo periodo segnalati.
- **Perché.** Nessuna norma disciplina l'uso dell'AI per valutare le leggi: chi la configura, con quali pesi, con quale trasparenza, chi ne risponde. Le regole europee e nazionali ora ci sono (AI Act, L. 132/2025, d.lgs. 179/2026), ma riguardano i sistemi in generale, non l'analisi delle politiche pubbliche.
- **Costo.** 6 milioni nel 2027, 12 nel 2028, 15 dal 2029. Coperti riducendo le spese per studi e consulenze esterne dei ministeri.
- **Veicolo consigliato.** Proposta di legge autonoma che modifica la L. 243/2012. **Va approvata a maggioranza assoluta** dei componenti di ciascuna Camera (art. 81, sesto comma, Cost.; art. 1, comma 2, L. 243/2012). Non può andare nella legge di bilancio (norma ordinamentale; serve la maggioranza assoluta).
- **Chi la può presentare.** Ogni parlamentare o gruppo; meglio una proposta firmata da più gruppi, anche di opposizione, dopo un'intesa con i Presidenti delle Camere. Anche il Governo, come disegno di legge.
- **Tempi.** Presentazione subito; approvazione nel 2027; prima VIP-AI sul disegno di legge di bilancio per il 2028 (ottobre 2027), in forma sperimentale; requisiti AI Act a regime prima del 2 dicembre 2027.

---

## 2. Relazione illustrativa

### Il problema (fatti)

- **Le regole sull'AI ora hanno date certe.**
  - Il [regolamento (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) (AI Act) si applica in generale dal 2 agosto 2026.
  - Il regolamento (UE) 2026/1744 (*Digital Omnibus* sull'AI), pubblicato nella GUUE il 24 luglio 2026 e in vigore dal 27 luglio 2026, rinvia gli obblighi per i sistemi ad alto rischio dell'Allegato III al 2 dicembre 2027 e quelli dell'Allegato I al 2 agosto 2028. Fonte: `dati/verifiche/08_esteri.md` e stampa specializzata; da verificare sul testo in GUUE ([EUR-Lex](https://eur-lex.europa.eu/eli/reg/2026/1744/oj)).
  - In Italia sono in vigore la [L. 23 settembre 2025, n. 132](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-09-23;132), dal 10 ottobre 2025, e il d.lgs. 7 ottobre 2026, n. 179, sui poteri delle autorità nazionali, dal 23 ottobre 2026.
- **Che cosa dicono già.** L'[art. 14 L. 132/2025](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-09-23;132~art14) stabilisce che nella PA l'AI è strumento di supporto, con conoscibilità del funzionamento e tracciabilità dell'uso; la decisione e la responsabilità restano alla persona. L'[art. 20](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-09-23;132~art20) designa AgID e ACN come autorità nazionali per l'AI. Nessuna di queste norme riguarda la valutazione degli atti normativi, né gli organi delle Camere.
- **L'UPB esiste e ha già un meccanismo simile.** L'UPB ([L. 243/2012, Capo VII](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2012-12-24;243~art18)) valuta già l'impatto macroeconomico dei provvedimenti di maggior rilievo (art. 18, comma 1, lett. b). Quando le sue valutazioni divergono in modo significativo da quelle del Governo, su richiesta di un terzo dei componenti di una Commissione il Governo deve dire se le conferma o le adegua (art. 18, comma 3). Ha un tetto di 40 unità di personale (art. 17, comma 4) e una dotazione di 3 milioni l'anno per ciascuna Camera (art. 19, comma 1).
- **Contesto.** Alle politiche del 2022 l'affluenza è stata del 63,9%, minimo storico (Ministero dell'interno, Eligendo). È un dato di contesto: non si attribuisce alla sola misura.

### Giudizio (separato dai fatti)

Gli strumenti di AI sono già usati negli uffici pubblici per scrivere e analizzare testi. Il rischio non è che si usino, ma che si usino senza regole: pesi nascosti, fornitori non controllabili, nessuno che firma. Collocare la funzione dentro l'UPB riusa garanzie di indipendenza già collaudate (nomina d'intesa dei Presidenti delle Camere, autonomia) e riduce il rischio di cattura politica rispetto a un ufficio nuovo o a una struttura del Governo.

### La soluzione

1. Una **sezione per la valutazione d'impatto pubblica** dentro l'UPB, con fino a 30 unità aggiuntive.
2. **VIP-AI obbligatoria** su legge di bilancio, decreti-legge e disegni di legge governativi o schemi di decreto legislativo con oneri sopra lo 0,1% del PIL in almeno un anno.
3. **Garanzie sul sistema.** Conformità volontaria ai requisiti dell'AI Act per l'alto rischio; valutazione d'impatto sui diritti fondamentali; codice, istruzioni e pesi pubblici; infrastruttura sotto giurisdizione UE; firma di un funzionario; audit annuale.
4. **Assemblea civica** di 100 persone sorteggiate, una sessione l'anno. Fissa i pesi di base tra i valori e il tasso di sconto tra generazioni. Non vincola Camere e Governo.
5. **Comply or explain sulla legge di bilancio.** Sul modello dell'art. 18, comma 3, già vigente.
6. **Durata quinquennale** con valutazione indipendente.

### Articolo per articolo

- **Art. 1:** finalità e principi; natura non vincolante; divieti di profilazione e di propaganda.
- **Art. 2:** modifiche alla L. 243/2012: personale (art. 17), nuova funzione (art. 18), nuovo art. 18-bis (sezione, VIP-AI, requisiti del sistema), nuovo art. 18-ter (Assemblea civica), nuovo art. 18-quater (motivazione sulla legge di bilancio), dotazione (art. 19).
- **Art. 3:** raccordo con AI Act, L. 132/2025, d.lgs. 179/2026, protezione dei dati e autonomia delle Camere.
- **Art. 4:** valutazione e durata.
- **Art. 5:** copertura finanziaria.

---

## 3. Articolato

**Proposta di legge — "Modifiche alla legge 24 dicembre 2012, n. 243, per la valutazione d'impatto pubblica dei provvedimenti normativi con il supporto di sistemi di intelligenza artificiale"**

*(Da approvare a maggioranza assoluta dei componenti di ciascuna Camera, ai sensi dell'articolo 81, sesto comma, della Costituzione e dell'articolo 1, comma 2, della legge 24 dicembre 2012, n. 243.)*

**Art. 1** *(Finalità e principi)*

1. La presente legge disciplina l'uso di sistemi di intelligenza artificiale a supporto della valutazione d'impatto dei provvedimenti normativi da parte dell'Ufficio parlamentare di bilancio. Ne assicura la trasparenza, la verificabilità, l'imparzialità e il controllo democratico, in attuazione degli articoli 1, 3, secondo comma, 81 e 97 della Costituzione.

2. Le valutazioni rese ai sensi della presente legge non sono vincolanti. Non incidono sulla validità né sull'efficacia degli atti e non limitano le prerogative delle Camere, dei loro componenti e del Governo. La decisione resta agli organi costituzionali, nel rispetto del principio di sorveglianza umana di cui all'articolo 14 del regolamento (UE) 2024/1689 e dei principi di cui all'articolo 14 della legge 23 settembre 2025, n. 132.

3. È vietato l'uso dei sistemi di cui alla presente legge per profilare persone fisiche, per valutare singoli parlamentari o elettori o per finalità di propaganda.

**Art. 2** *(Modifiche alla legge 24 dicembre 2012, n. 243)*

1. Alla legge 24 dicembre 2012, n. 243, sono apportate le seguenti modificazioni:

a) all'articolo 17, comma 4, è aggiunto, in fine, il seguente periodo: «A decorrere dal 2027 il limite di cui al periodo precedente è elevato a settanta unità, delle quali fino a trenta assegnate alla sezione di cui all'articolo 18-bis.»;

b) all'articolo 18, comma 1, dopo la lettera b) è inserita la seguente: «b-bis) valutazione d'impatto pubblica dei provvedimenti di cui all'articolo 18-bis;»;

c) dopo l'articolo 18 sono inseriti i seguenti:

«Art. 18-bis *(Valutazione d'impatto pubblica)*. — 1. Presso l'Ufficio è costituita una sezione per la valutazione d'impatto pubblica, che può avvalersi di sistemi di intelligenza artificiale ai sensi dell'articolo 3 del regolamento (UE) 2024/1689, nel rispetto del presente articolo.

2. La sezione predispone e pubblica una valutazione d'impatto pubblica (VIP-AI) relativa:
a) al disegno di legge di bilancio;
b) ai disegni di legge di conversione dei decreti-legge;
c) ai disegni di legge di iniziativa governativa e agli schemi di decreto legislativo i cui effetti finanziari, come indicati nella relazione tecnica, superano in almeno un anno lo 0,1 per cento del prodotto interno lordo.

3. La VIP-AI indica:
a) gli effetti attesi del provvedimento su ciascuna delle dimensioni di valutazione individuate ai sensi dell'articolo 18-ter, nel breve, medio e lungo periodo, con il grado di incertezza;
b) la distribuzione degli effetti per livello di reddito, territorio, classe di età e genere, ove i dati lo consentano;
c) l'analisi della sensibilità dei risultati ai pesi tra le dimensioni di valutazione;
d) le fonti, i modelli, le ipotesi e i limiti dell'analisi.
La VIP-AI non contiene raccomandazioni sulle scelte da adottare.

4. La VIP-AI è pubblicata entro quindici giorni dalla trasmissione del provvedimento alle Camere; per i decreti-legge è pubblicata una versione sintetica entro cinque giorni. Il termine non sospende e non condiziona l'esame parlamentare. La VIP-AI integra l'analisi di impatto della regolamentazione di cui all'articolo 14 della legge 28 novembre 2005, n. 246, e non la sostituisce.

5. I sistemi di intelligenza artificiale usati dalla sezione sono sviluppati e gestiti nel rispetto, su base volontaria, dei requisiti che il regolamento (UE) 2024/1689 prevede per i sistemi ad alto rischio, in materia di gestione dei rischi, qualità e governance dei dati, documentazione tecnica, registrazione degli eventi, trasparenza, sorveglianza umana, accuratezza, robustezza e cibersicurezza, e sono messi a regime entro il 2 dicembre 2027. Prima dell'entrata in esercizio e a ogni modifica sostanziale la sezione effettua una valutazione d'impatto sui diritti fondamentali sul modello dell'articolo 27 del medesimo regolamento.

6. Sono pubblicati in formato aperto, ai sensi degli articoli 68 e 69 del decreto legislativo 7 marzo 2005, n. 82, il codice, le istruzioni di sistema, la matrice dei pesi, le fonti dei dati, i modelli di intelligenza artificiale utilizzati e il registro delle loro versioni. Sono esclusi i soli elementi la cui diffusione pregiudica la sicurezza dei sistemi, sentita l'Agenzia per la cybersicurezza nazionale.

7. I dati e le elaborazioni sono trattati su infrastrutture soggette alla giurisdizione dell'Unione europea. I microdati personali sono trattati in ambienti sicuri e in forma pseudonimizzata, ai sensi dell'articolo 89 del regolamento (UE) 2016/679 e dell'articolo 18, comma 7, della presente legge.

8. Ogni VIP-AI dichiara l'uso di sistemi di intelligenza artificiale ed è sottoscritta da un funzionario responsabile, che ne verifica le fonti e la coerenza. La sezione sottopone i sistemi ogni anno a un audit indipendente e a prove di robustezza e di imparzialità, e pubblica gli esiti e il registro degli errori corretti.

9. Nei quarantacinque giorni che precedono le elezioni politiche e le elezioni dei membri del Parlamento europeo spettanti all'Italia, la sezione pubblica solo le VIP-AI obbligatorie ai sensi del comma 2 e non valuta programmi elettorali. Resta ferma la legge 22 febbraio 2000, n. 28.

Art. 18-ter *(Assemblea civica sui valori)*. — 1. È istituita presso l'Ufficio l'Assemblea civica sui valori, composta da cento persone sorteggiate ogni anno tra gli iscritti nelle liste elettorali, con campionamento stratificato per età, genere, territorio, titolo di studio e condizione occupazionale. Il sorteggio è certificato dall'Istituto nazionale di statistica. Il Ministero dell'interno mette a disposizione i dati necessari, che sono trattati al solo fine del sorteggio e cancellati al suo termine.

2. L'Assemblea si riunisce in una sessione annuale, articolata in non più di otto giornate. Dopo audizioni pubbliche di esperti e di portatori di interessi, su materiali validati dal comitato scientifico di cui all'articolo 18, comma 5, composto in modo pluralista, delibera le dimensioni di valutazione, i pesi relativi e il tasso di sconto tra generazioni. La deliberazione vincola la sola configurazione predefinita dei sistemi della sezione. Non vincola le Camere né il Governo. I principi e i diritti costituzionali non sono oggetto di ponderazione.

3. Ai componenti dell'Assemblea spettano un'indennità giornaliera e il rimborso delle spese, nella misura stabilita dal Consiglio dell'Ufficio. I componenti che sono lavoratori dipendenti hanno diritto a permessi retribuiti per i giorni di sessione. Al datore di lavoro è rimborsata dall'Ufficio la retribuzione corrisposta. Gli oneri sono a carico della dotazione di cui all'articolo 19, comma 1-bis.

4. Le modalità del sorteggio, del funzionamento dell'Assemblea e del trattamento dei dati sono stabilite con regolamento dell'Ufficio, d'intesa con i Presidenti delle Camere, sentiti l'Istituto nazionale di statistica e il Garante per la protezione dei dati personali, previa valutazione d'impatto ai sensi dell'articolo 35 del regolamento (UE) 2016/679.

Art. 18-quater *(Motivazione sulla legge di bilancio)*. — 1. Se la VIP-AI sul disegno di legge di bilancio, aggiornata al testo approvato, indica effetti negativi di lungo periodo su una o più dimensioni di valutazione, il Governo, entro trenta giorni dall'approvazione definitiva, trasmette alle Commissioni competenti una relazione motivata. Le Camere ne disciplinano l'esame secondo i rispettivi regolamenti.

2. L'omissione della relazione è registrata e pubblicata dall'Ufficio. Non incide sulla validità né sull'efficacia della legge.»;

d) all'articolo 19, dopo il comma 1 è inserito il seguente: «1-bis. Per le funzioni di cui agli articoli 18-bis, 18-ter e 18-quater è autorizzata l'ulteriore spesa, in favore di ciascuna Camera, di 3 milioni di euro per l'anno 2027, di 6 milioni di euro per l'anno 2028 e di 7,5 milioni di euro annui a decorrere dall'anno 2029. Le somme sono trasferite ai bilanci delle Camere e sono destinate all'Ufficio.».

**Art. 3** *(Raccordo con la disciplina dell'intelligenza artificiale e autonomia delle Camere)*

1. Restano ferme le competenze dell'Agenzia per l'Italia digitale e dell'Agenzia per la cybersicurezza nazionale, quali autorità nazionali per l'intelligenza artificiale ai sensi dell'articolo 20 della legge 23 settembre 2025, n. 132, e del decreto legislativo 7 ottobre 2026, n. 179, nonché quelle del Garante per la protezione dei dati personali, nel rispetto dell'autonomia costituzionale delle Camere.

2. Le Camere, nell'esercizio della propria autonomia regolamentare, disciplinano le modalità con cui le VIP-AI sono rese disponibili nel corso dell'esame dei provvedimenti e l'esame della relazione di cui all'articolo 18-quater della legge n. 243 del 2012.

**Art. 4** *(Valutazione e durata)*

1. Al termine del secondo anno di applicazione, la Corte dei conti e un comitato accademico indipendente, nominato d'intesa dai Presidenti delle Camere, trasmettono alle Camere una valutazione della qualità, dell'utilità e dei costi delle VIP-AI.

2. Gli articoli 18-bis, 18-ter e 18-quater della legge n. 243 del 2012 cessano di avere efficacia il 31 dicembre del quinto anno successivo a quello di entrata in vigore della presente legge, salvo conferma con legge approvata ai sensi dell'articolo 81, sesto comma, della Costituzione.

**Art. 5** *(Copertura finanziaria)*

1. Agli oneri derivanti dall'articolo 2, comma 1, lettera d), pari a 6 milioni di euro per l'anno 2027, a 12 milioni di euro per l'anno 2028 e a 15 milioni di euro annui a decorrere dall'anno 2029, si provvede mediante corrispondente riduzione degli stanziamenti di competenza e di cassa relativi a studi, consulenze e incarichi esterni iscritti negli stati di previsione dei Ministeri, nella misura indicata, per ciascun Ministero, nell'allegato A alla presente legge.

2. Il Ministro dell'economia e delle finanze è autorizzato ad apportare, con propri decreti, le occorrenti variazioni di bilancio.

*Allegato A — Riduzioni per Ministero (milioni di euro, 2027 / 2028 / dal 2029): da compilare con la Ragioneria generale dello Stato sui capitoli di studi e consulenze (dato da acquisire per capitolo).*

> **Verifiche sul testo vigente (Normattiva, 13 novembre 2026):** L. 243/2012, art. 1, comma 2 (modifica solo espressa), art. 17, comma 4 (30 unità nei primi tre anni, poi 40), art. 18 (commi 1-7, lett. a-f al comma 1; comma 3 sul confronto con il Governo; comma 5 sul comitato scientifico; comma 7 sull'accesso alle banche dati, con equiparazione agli enti SISTAN), art. 19, comma 1 (3 milioni per ciascuna Camera dal 2014). L. 132/2025, artt. 14 e 20. Restano [da verificare sul testo vigente]: il testo ufficiale del Reg. (UE) 2026/1744 in GUUE e del d.lgs. 179/2026 in GU; che non esistano già gli artt. 18-bis, 18-ter, 18-quater e il comma 19, 1-bis nella L. 243/2012; l'attuale art. 14 L. 246/2005 sull'AIR.

---

## 4. Relazione tecnica (art. 17, comma 3, L. 196/2009)

**Art. 1.** Norma di principio. Nessun effetto finanziario.

**Art. 2.**
- *Lett. a), b), c).* Definiscono funzioni e limiti di personale. La spesa che ne deriva è contenuta nella dotazione della lett. d). Senza la dotazione aggiuntiva le assunzioni non possono essere effettuate.
- *Lett. d) (dotazione).* Autorizzazione di spesa di 6 milioni nel 2027, 12 nel 2028 e 15 dal 2029, ripartita a metà tra le Camere. La somma è trasferita ai bilanci delle Camere, non imposta su di essi (condizione COS). Composizione a regime, stima GovernAI bottom-up della variante ESSENZIALE: il dettaglio non è nella scheda e va ricostruito con l'UPB (dato da acquisire). Le voci della variante PIENA (`programma/varianti/08_esteri.csv`) danno un riferimento: personale a 0,1 milioni per unità; calcolo su infrastruttura UE; Assemblea (indennità, viaggi, facilitazione, sorteggio certificato); audit e prove di robustezza; convenzioni; riserva. Con circa 30 unità, il personale a regime vale circa 3 milioni. La gradualità 2027-2028 tiene conto dei tempi di reclutamento e della prima sessione dell'Assemblea. È un limite di spesa: la dotazione non può essere superata.

**Art. 3.** Raccordo. Nessun effetto.

**Art. 4.** La valutazione della Corte dei conti rientra nei compiti istituzionali. Il comitato accademico opera senza compensi (da precisare nell'atto di nomina). Nessun onere.

**Art. 5 (copertura).** Riduzione degli stanziamenti per studi, consulenze e incarichi esterni dei ministeri, pari a 6, 12 e 15 milioni. Base di riferimento: circa 189 milioni impegnati nel 2025 sui capitoli di consulenza dello Stato (OpenBDAP-RGS, Rendiconto 2025, ricerca per parole chiave con perimetro probabilmente sottostimato; `programma/coperture_menu.csv`, RA03). A regime la riduzione vale circa l'8% di quella base. **Avvertenza sul doppio conteggio:** nel programma la copertura RA03 (tetto del 20% alle consulenze) assorbe questa riduzione. Se RA03 è approvata nella legge di bilancio, i 15 milioni vanno contati dentro RA03 e non in aggiunta. Copertura di riserva se la Ragioneria non certifica la riduzione per capitolo: riduzione del Fondo per esigenze indifferibili (art. 1, comma 200, L. 190/2014) [da verificare la capienza].

**Prospetto riepilogativo (milioni di euro; segno + = peggioramento del saldo, − = miglioramento)**

| Voce | Saldo netto da finanziare 2027 | 2028 | 2029 | Fabbisogno 2027 | 2028 | 2029 | Indebitamento netto 2027 | 2028 | 2029 |
|---|---|---|---|---|---|---|---|---|---|
| Art. 2, lett. d) — maggiori spese (dotazione UPB) | +6 | +12 | +15 | +6 | +12 | +15 | +6 | +12 | +15 |
| Art. 5 — minori spese (consulenze ministeri) | −6 | −12 | −15 | −6 | −12 | −15 | −6 | −12 | −15 |
| **Saldo** | **0** | **0** | **0** | **0** | **0** | **0** | **0** | **0** | **0** |

Ipotesi: la spesa delle Camere rientra nel conto consolidato delle amministrazioni pubbliche, quindi l'effetto è uguale sui tre saldi. Anche la riduzione delle consulenze è considerata spesa che si sarebbe realizzata nell'anno. La Ragioneria potrebbe applicare coefficienti di realizzo diversi (da verificare).

Coerenza con il programma: variante ESSENZIALE di 08-P1, costi 0,006 / 0,012 / 0,015 miliardi (2027 / 2028 / 2029), fondo RIALLOCAZIONE (`programma/varianti/08_esteri.csv`). Nel calendario di avvio (`programma/annuale_intermedio.md`) le riforme a costo quasi zero partono al 100% dal 2027.

---

## 5. Analisi tecnico-normativa (sintesi)

- **Norme modificate.** [L. 243/2012](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2012-12-24;243): art. 17, comma 4 (limite di personale); art. 18, comma 1 (nuova lett. b-bis); nuovi artt. 18-bis, 18-ter e 18-quater; art. 19, nuovo comma 1-bis. Nessuna abrogazione.
- **Legge rinforzata.** La L. 243/2012 si modifica solo in modo espresso e con legge approvata a maggioranza assoluta (art. 81, sesto comma, Cost.; art. 1, comma 2, L. 243/2012). Condizione COS recepita.
- **Autonomia delle Camere (art. 64 Cost.; Corte cost. [129/1981](https://www.cortecostituzionale.it/stampa-pdf-pronuncia/1981/129) e [120/2014](https://www.cortecostituzionale.it/stampa-pdf-pronuncia/2014/120)).** La legge non impone diritti di richiesta nelle Commissioni né procedure interne: rinvia ai regolamenti (art. 3, comma 2; art. 18-quater). La dotazione è trasferita alle Camere, non prelevata dai loro bilanci. Condizioni COS recepite. Resta necessaria un'intesa preventiva con i Presidenti delle Camere (vedi Note).
- **Ambito dell'UPB.** La lettera b-bis allarga la funzione dell'UPB oltre la finanza pubblica in senso stretto (dimensioni distributive e di lungo periodo). Il controllo COS lo segnala: va motivato come estensione dell'analisi di impatto già prevista dall'art. 18, comma 1, lett. b). La scelta è legittima perché fatta con legge rinforzata.
- **Libero mandato e forma di governo (artt. 67 e 95 Cost.).** Valutazioni non vincolanti; l'Assemblea civica non vincola le Camere né il Governo; la relazione motivata non condiziona la validità della legge.
- **Periodo elettorale (art. 49 Cost.; [L. 28/2000](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2000-02-22;28)).** La variante ESSENZIALE non valuta i programmi elettorali e limita le pubblicazioni ai casi obbligatori. Così supera il rilievo COS sull'art. 9 della scheda completa.
- **Dati personali.** Il sorteggio dalle liste elettorali ha base legale espressa, finalità limitata, cancellazione dei dati e valutazione d'impatto (art. 18-ter, commi 1 e 4). I microdati sono pseudonimizzati, in ambienti sicuri, con l'art. 89 [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj). Condizioni COS e UE recepite.
- **AI Act ([Reg. (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj), come modificato dal Reg. (UE) 2026/1744).**
  - *Classificazione.* Un sistema che aiuta un ufficio parlamentare a valutare leggi non rientra, di per sé, tra i sistemi ad alto rischio dell'Allegato III. Il punto 8, lett. b), riguarda i sistemi destinati a influenzare l'esito di elezioni o il comportamento di voto: l'art. 18-bis, comma 9, e il divieto di propaganda dell'art. 1 tengono il sistema fuori da quell'uso. La conformità volontaria ai requisiti per l'alto rischio (capo III, sezione 2) e la valutazione sul modello dell'art. 27 sono ammesse e anticipano un'eventuale classificazione futura (controllo UE: «condizionato», condizioni recepite).
  - *Obblighi che valgono comunque.* L'alfabetizzazione in materia di AI del personale (art. 4) e la trasparenza (art. 50). L'art. 50, par. 4, esonera i testi generati con AI se sono sottoposti a revisione umana con responsabilità editoriale. La firma del funzionario soddisfa questa condizione, ma la legge sceglie di dichiarare comunque l'uso di AI (art. 18-bis, comma 8).
  - *Modelli per finalità generali.* Gli obblighi del capo V restano in capo ai fornitori dei modelli. L'Ufficio, come deployer, pubblica quali modelli usa (comma 6).
  - *Date.* Requisiti a regime entro il 2 dicembre 2027, la data che il Reg. 2026/1744 fissa per l'Allegato III (da verificare in GUUE).
- **L. 132/2025.** Il testo estende agli organi delle Camere i principi dell'art. 14: supporto e non sostituzione della decisione, conoscibilità, tracciabilità. Il controllo COS lo giudica compatibile. Le competenze di AgID e ACN (art. 20) e i poteri del d.lgs. 179/2026 restano fermi. Va verificato come si coordinano i poteri di vigilanza e ispezione delle autorità con l'autonomia costituzionale delle Camere [da verificare].
- **Riparto Stato-Regioni.** Materia statale (organi costituzionali, art. 117, secondo comma, lett. f). Nessuna intesa.
- **Notifiche alla Commissione europea.** Nessuna. Non è una regola tecnica ([direttiva (UE) 2015/1535](https://eur-lex.europa.eu/eli/dir/2015/1535/oj)) e non è un aiuto di Stato. L'AI Act è un regolamento: le norme nazionali non lo ripetono e non lo derogano, rinviano soltanto.

---

## 6. Analisi d'impatto (sintesi)

**Obiettivi.** Rendere pubbliche, verificabili e confrontabili le conseguenze dei provvedimenti più pesanti, per chi e su quale orizzonte di tempo. Dare regole all'uso dell'AI nel processo legislativo prima che si diffonda senza regole.

**Indicatori** (da `apprendimento/obiettivi.yaml`, righe 08-P1, adattati al perimetro della variante ESSENZIALE)

| Indicatore | Base | Obiettivo a 3 anni | Obiettivo a 5 anni |
|---|---|---|---|
| Quota di atti obbligati (bilancio, decreti-legge, DDL sopra lo 0,1% del PIL) con VIP-AI pubblicata nei termini | 0% (2026, nessuna norma) | ≥ 80% | ≥ 95% |
| Quota di leggi di bilancio con effetti negativi di lungo periodo segnalati e relazione motivata del Governo | 0% (2026) | ≥ 70% | ≥ 95% |
| Inviti al sorteggio accettati | n.d. (riferimenti esteri non verificati) | ≥ 10% | ≥ 15% |
| Affluenza alle politiche (solo contesto, non attribuibile alla misura) | 63,9% (2022, Eligendo) | — | inversione del calo |

**Chi ne beneficia.** Parlamentari di maggioranza e di opposizione (informazione indipendente e tempestiva); cittadine e cittadini (sanno chi guadagna e chi perde); generazioni future (orizzonte lungo esplicito).

**Chi ne sopporta i costi.** Il bilancio dello Stato, per 15 milioni a regime, compensati da minori consulenze esterne dei ministeri: ne sopportano il costo le società di consulenza. Il Governo ha un onere di motivazione in più sulla legge di bilancio.

---

## 7. Note per chi presenta

- **Passaggio preliminare indispensabile.** Un'intesa informale con i Presidenti delle Camere e con il Consiglio dell'UPB, prima del deposito. Senza di essa la proposta urta l'autonomia delle Camere e l'indipendenza dell'Ufficio.
- **Maggioranza assoluta.** Serve un consenso largo: conviene una proposta firmata da più gruppi. È anche il modo migliore per evitare che la misura sembri di parte.
- **Obiezione "lo decide l'algoritmo".** *Risposta:* nessuna valutazione è vincolante; non ci sono raccomandazioni; ogni VIP-AI è firmata da una persona; la sensibilità ai pesi è pubblica; i pesi li fissa un'Assemblea di persone sorteggiate, non i tecnici.
- **Obiezione "l'UPB diventa politico".** *Risposta:* l'UPB valuta già l'impatto dei provvedimenti e ha già un meccanismo di confronto con il Governo (art. 18, comma 3). La VIP-AI descrive effetti e non giudica le scelte. Il Consiglio dell'UPB resta nominato come oggi.
- **Obiezione "costa e non serve".** *Risposta:* 15 milioni a regime, coperti tagliando consulenze esterne; durata di cinque anni con valutazione della Corte dei conti dopo due.
- **Rischi di attuazione.**
  - Reclutamento di 30 persone qualificate: il 2027 è un anno di avvio.
  - Prima VIP-AI sul bilancio 2028 in forma sperimentale.
  - Dipendenza da fornitori extra UE: codice aperto, infrastruttura UE, possibilità di cambiare modello.
  - Errori del modello: audit annuale, registro pubblico degli errori.
- **Alleanze possibili.** Comunità della valutazione delle politiche pubbliche, università, ISTAT, associazioni per la trasparenza e la partecipazione, organizzazioni giovanili (orizzonte intergenerazionale).
- **Passaggi successivi.**
  - Regolamento dell'UPB sull'Assemblea (con ISTAT e Garante).
  - Modifiche ai regolamenti parlamentari o pareri delle Giunte per il regolamento.
  - Valutazione d'impatto sui diritti fondamentali prima dell'esercizio.
  - Allegato A sulle consulenze, con la Ragioneria.
  - Dopo la valutazione biennale, scegliere se passare alla variante PIENA: ufficio autonomo, VIP-AI su richiesta delle minoranze, comply or explain su tutti gli atti valutati.
