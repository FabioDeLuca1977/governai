# Quattro scelte aperte: una proposta equa (valutatore Z)

*Proposta scritta da un agente AI (valutatore Z), 13 novembre 2026; non è una decisione.*

Ho lavorato da solo, senza vedere le proposte degli altri valutatori. Oltre all'equità, ho dato peso a tre cose: che un'amministrazione possa davvero applicare la proposta, che le cittadine e i cittadini possano fidarsi, e che persone di orientamenti diversi possano accettarla.

Uso due etichette. **[Fatto]**: dato del repository o di una fonte esterna, sempre citato. **[Giudizio]**: valutazione mia. Gli importi sono in mld €/anno a regime, al gettito minimo, come nel resto del programma.

## Il punto di partenza: una copertura che oggi non paga niente

**[Fatto]** Nello scenario intermedio la copertura PE04 (rivalutazione al 50% sulla sola quota di pensione oltre 6 volte il minimo, dal 2030) è attiva e rende 0,30. È però iscritta nel fondo vincolato PENSIONI, e quel fondo non paga nessuna misura: spesa 0,00 su 0,30 (`programma/selezione_intermedio.md`, tabella "Uso dei fondi"). PE04 era stata pensata per la pensione di garanzia (02-C3 ESSENZIALE), che costa 0,35 solo dal 2036 e oggi è fuori dal programma (`programma/varianti/`, righe 02-C3; `costituzione/esami/governai_conti_2027_2029.md`).

**[Giudizio]** Spostare questi 0,30 sulle risorse generali non è una tassa in più. Non tocca chi va in pensione più di quanto già previsto e non crea deficit. È il modo più equo per trovare lo spazio che oggi manca. Ha comunque un prezzo, che dichiaro alle scelte 2 e 3.

**Verifica con l'ottimizzatore.** Ho usato una copia locale, fuori dal repository, in cui PE04 è iscritta nelle risorse generali. Ho dato etichette di prova (`prova_z_*`) e poi ho cancellato i file.

| Prova | Esito |
|---|---|
| Riferimento (comando del brief) | spesa 9,17; coperture 7,42; 66 proposte su 78; risorse generali 7,01 ≤ 7,01 |
| 06-C2 PILOTA + 01-P13 ESSENZIALE, PE04 nel fondo vincolato | **non finanziabile** |
| 06-C2 PILOTA senza obblighi sulle misure di innovazione | finanziabile, ma l'ottimizzatore toglie 01-P13 e 04-P7 e azzera 04-P8 e 04-P9 |
| **Proposta: 06-C2 PILOTA + 01-P13 ESSENZIALE + PE04 nelle risorse generali, con 0,09 tenuti da parte** | **finanziabile**: spesa 9,38; 67 proposte su 78; risorse generali 7,22 ≤ 7,31 |

---

## Scelta 1. Responsabilità e garanzia

### Proposta

**A. Una persona responsabile, con nome e cognome**, eletta dalle persone associate (serve uno statuto: `revisioni/2026-11-08_analista_politico.md`, racc. 1 e 8).
- **Compito.** Firma ogni scelta politica del programma, come quelle del 9-13 novembre, con decisione, motivo e prezzo. Risponde in pubblico. Ogni anno presenta un rendiconto con una sessione di domande aperte.
- **Durata.** Due anni, rinnovabile una sola volta. Ha una persona vice, che la sostituisce se la responsabile si candida.
- **Limiti.** Non fa parte del comitato e non ne sceglie i membri. Non cambia da sola la Carta, la rubrica, i punteggi del panel né il codice del motore.
- **Revoca.** Con i due terzi delle persone associate.

**B. Un comitato di garanzia di 9 persone.** Controlla le regole, non decide il programma.

| Componente | Quante persone | Come si scelgono |
|---|---|---|
| Esperte ed esperti indipendenti: diritto costituzionale e UE; finanza pubblica e statistica; etica e governo dei dati e dell'AI | 3 | Avviso pubblico con requisiti scritti, poi sorteggio pubblico tra le candidature idonee |
| Persone di sensibilità culturali diverse | 3 | Chi si candida dichiara la propria area (per esempio conservatrice, liberale, popolare o cattolico-sociale, socialista o laburista, ambientalista). Si sorteggiano 3 aree e poi una persona per ciascuna area. Mai due persone della stessa area |
| Cittadine e cittadini | 3 | Sorteggio tra le persone iscritte, con quote per genere, età e macro-area. Durata 1 anno |

- **Durata.** 3 anni, non rinnovabili. Ogni anno si rinnova un terzo dei membri. Almeno 4 donne e 4 uomini.
- **Compenso.** Solo rimborso spese, pubblicato.
- **Primo comitato.** Si usa lo stesso avviso e lo stesso sorteggio. La persona fondatrice non sceglie nessun membro.

**Incompatibilità.**
- Non può far parte del comitato chi ha avuto negli ultimi 3 anni, o ha oggi:
  - una carica elettiva o di partito;
  - un incarico pagato da GovernAI;
  - un ruolo di fornitore di modelli o servizi AI usati dal progetto;
  - un'attività di lobby iscritta nei registri dei portatori di interessi.
- Chi esce dal comitato non si candida con GovernAI per 2 anni.

**Conflitti di interesse.**
- Ogni membro pubblica una dichiarazione degli interessi (incarichi, finanziamenti, partecipazioni) e la aggiorna ogni anno.
- Su un punto in cui ha un interesse, il membro si astiene. L'astensione è scritta nel registro pubblico.
- Le delibere sono pubbliche, con i voti nominativi. Il registro è legato alla catena di integrità già esistente (`integrita/`).

**Poteri del comitato.** Sono tutti poteri di garanzia.
1. **Parere vincolante sulle regole.** Serve per ogni modifica di Carta, metodo, rubrica, regolamento e motore. La Carta cambia solo con i due terzi del comitato e dopo una consultazione pubblica di 30 giorni.
2. **Sospensione per 30 giorni.** Vale per un documento o un dato pubblicato che viola le regole: numeri senza fonte, una scelta politica non dichiarata, una linea rossa superata. La sospensione finisce con la correzione.
3. **Verifiche esterne.** Può chiedere che un'università o un centro studi replichi stime e codice.
4. **Ricorsi.** È l'ultima istanza sui ricorsi contro la moderazione e sul rispetto del metodo, sopra il riesame dei moderatori (`comunita/regole.md`).
5. **Assemblea sorteggiata.** Vigila sulla sua formazione (08-P1) e sull'indipendenza del panel.
6. **Relazione annuale** pubblica.

**Rapporto con la vision "sul sito nessuno decide".**
- La comunità resta uno spazio per discutere e prendere appunti con l'AI.
- Il comitato non decide i contenuti. Garantisce che chi decide lo faccia secondo le regole e con il proprio nome.
- La responsabile decide le scelte politiche, ma non le regole.
- In futuro i pesi dei valori li fissa l'assemblea sorteggiata (Carta, regola 8).

### Motivazione con i valori
- **Fiducia e trasparenza (FID).** Risponde alla domanda "chi risponde se sbaglia?" (`revisioni/2026-11-08_analista_politico.md`, credibilità 5/10).
- **Cittadinanza responsabile (CIT).** Un terzo dei membri è sorteggiato.
- **Rispetto e diversità (RIS).** Il comitato è plurale, ma senza quote di partito.
- **[Giudizio]** Il sorteggio tra persone idonee toglie potere alla persona fondatrice, e senza questo il comitato non sarebbe credibile.

### Conto
0 mld di bilancio pubblico. Per l'associazione, solo rimborsi spese, da pubblicare.

### Chi guadagna e chi perde
- **Guadagnano** le persone iscritte e chi legge il programma: le regole sono più stabili e le firme verificabili.
- **Perdono** chi guida oggi il progetto, che perde il potere di cambiare da solo le regole, e la velocità: ogni modifica della Carta richiede almeno 30 giorni.

### Rischi
- **Paralisi.** Mitigazione: i poteri sono solo di garanzia e la sospensione dura al massimo 30 giorni.
- **Comunità piccola**, quindi sorteggio poco rappresentativo. Mitigazione: quote, e allargamento quando crescono le persone iscritte.
- **Un'area culturale che "occupa" il comitato.** Mitigazione: mai due persone della stessa area e rinnovo scaglionato.

### Alternative scartate
- **Comitato di sole personalità**, una per area politica. Riproduce la logica dei partiti e il diritto di veto.
- **Solo sorteggio.** Mancano le competenze per controllare conti e codice.
- **Solo controlli automatici dell'AI.** Non risponde a nessuno.

---

## Scelta 2. Coperture regressive

**[Fatto]** Circa 2,3 mld di coperture pesano di più su chi ha meno (`23_equita_e_linguaggio.md`, sez. 4).
- Senza compensazione dedicata: AS01 sigarette (0,60), AS02 tabacco riscaldato (0,15), AS03 bevande zuccherate (0,15).
- Già compensate: SAD01, SAD13, SAD02, SAD10, RP01 e RP08.
- AS04, superalcolici (0,07), ha punteggio di equità 0 (`programma/coperture_menu.csv`).

**[Fatto]** Secondo la sorveglianza PASSI dell'ISS, fuma il 37% delle persone con molte difficoltà economiche e il 21% di chi non ne ha ([scheda PASSI fumo 2024](https://www.epicentro.iss.it/PASSI/pdf2024/SCHEDA%20PASSI%20FUMO%202024.pdf); cifre lette nella ricerca, da verificare sul PDF).

### Proposta, misura per misura

| Copertura | Gettito | Proposta | Costo nuovo |
|---|---|---|---|
| **AS01 + AS02**, tabacco | 0,75 | (1) **Destinazione per legge**: una somma pari al gettito va alla sanità vicino a casa già nel programma (06-C3 con la quota di perequazione, 06-C8, 06-C2), con priorità ai distretti con più deprivazione. Se il gettito cala perché si fuma meno, le misure non si riducono. (2) **"Smettere gratis"**: ambulatori per smettere di fumare nelle Case della Comunità dei distretti più poveri, con consulenza e farmaci. Il costo è stimato in circa 150.000-200.000 percorsi l'anno (stima GovernAI, da verificare; la rimborsabilità attuale dei farmaci è un dato da acquisire) | **0,04**, presi dal margine creato da PE04 |
| **AS03**, bevande zuccherate | 0,15 | Nessuna compensazione in denaro. Il peso medio è di circa 2,5 € per persona l'anno (0,15 mld su circa 59 milioni di residenti, ISTAT). Il gettito rientra nella stessa destinazione alla sanità e alla scuola (06-C9, 05-C5). Si controlla l'effetto per reddito | 0 |
| **SAD01 + SAD13**, gasolio dell'autotrasporto | 1,10 | Il fondo per il rinnovo delle flotte (0,40-0,55, già al netto del gettito) va **almeno per metà** alle imprese con 1-5 veicoli e a quelle del Mezzogiorno e delle isole. Si controllano i prezzi del trasporto merci nelle isole (ISTAT). Il calendario di uscita resta invariato | 0 |
| **SAD02**, gasolio agricolo | 0,15 | Resta il credito già previsto per piccole aziende e montagna. Si aggiunge una priorità per chi è giovane e coltiva la terra | 0 |
| **SAD10**, riscaldamento in montagna | 0,02 | Già compensata (salvaguardia fino a ISEE 15.000 €) | 0 |
| **RP01 + RP08**, meno posti nei concorsi generici | 0,09 | Compensazione in opportunità, non in denaro: posti riservati ai profili tecnici (RA07) e squadre tecniche (09-C3). Ogni anno si pubblicano le assunzioni nette per regione. Se i tempi dei servizi peggiorano, si torna al 100% delle sostituzioni, come già previsto | 0 |

Il bonus per le lavoratrici madri (RB03) e la fine di Opzione donna (PE03) non sono nel conto delle coperture regressive. Li segnalo perché pesano sulle donne: propongo di controllarne l'effetto di genere, senza spesa.

### Motivazione con i valori
- **Equità (EQU).** La linea rossa vieta di spostare costi su chi ha meno senza compensazione. Qui la compensazione è soprattutto in servizi, e va proprio a chi paga di più: le persone che fumano sono più spesso persone con difficoltà economiche.
- **Benessere (BEN).** Aiutare a smettere è la compensazione che fa bene alla salute.
- **Sicurezza senza controllo (SIC).** Compensare in denaro proprio chi fuma vorrebbe dire individuare le persone che fumano, cioè profilarle. La Carta lo vieta.
- **[Giudizio]** "Le tasse sul fumo pagano le cure vicino a casa" è una regola facile da spiegare e da controllare. Può raccogliere consenso sia tra chi difende le accise sulla salute sia tra chi chiede compensazioni.

### Conto
- **Spesa nuova: 0,04.** Viene dai 0,09 liberati alla scelta 3.
- La destinazione del gettito costa 0, perché le risorse generali si possono già usare per qualunque misura.
- La quota del fondo flotte per le piccole imprese costa 0.
- Le coperture restano 7,42, senza tasse nuove.

### Chi guadagna e chi perde
- **Guadagnano:**
  - chi fuma e ha un reddito basso, perché ottiene un aiuto gratuito per smettere;
  - i distretti più deprivati;
  - le imprese di autotrasporto più piccole e quelle del Sud.
- **Perdono:**
  - le flotte più grandi, che ricevono una quota minore dei contributi per il rinnovo;
  - le piccole misure che l'ottimizzatore avrebbe finanziato con lo stesso margine, soprattutto le versioni più ampie di 01-P1, 04-P4, 09-C6 e 01-P2. Le loro versioni a costo zero restano.

### Rischi
- La compensazione in servizi non restituisce reddito: chi fuma molto e non smette resta in perdita. Va dichiarato.
- Manca una microsimulazione per decili di reddito (`23_equita_e_linguaggio.md`, sez. 4).
- **Clausola di revisione.** Se entro 3 anni la quota di persone che fumano tra chi ha molte difficoltà economiche non cala, una parte maggiore della destinazione passa agli ambulatori per smettere.

### Alternative scartate
- **Aumento dell'Assegno unico o dell'Assegno di inclusione per i redditi bassi.** Indicativamente 0,15-0,20. Compensa troppo chi non fuma e troppo poco chi fuma molto, e oggi non ci sono risorse.
- **Togliere AS01.** Toglierebbe 0,60 al programma e anche il beneficio per la salute.

---

## Scelta 3. Personale infermieristico (06-C2)

### Proposta
**06-C2 entra in versione PILOTA (0,35).**
- **Contenuto** (`programma/schede/06_salute.md`): sperimentazione in 4 Regioni, di cui almeno 2 del Mezzogiorno, e nelle aree interne; indennità di area disagiata, 5.000 borse di studio con l'impegno a lavorare nel SSN, infermiere di pratica avanzata in 50 Case della Comunità; valutazione Agenas.
- **Copertura.**
  - **PE04 spostata nelle risorse generali** (+0,30);
  - **01-P13 da piena a essenziale** (−0,14): credito per la ricerca al 12% per le imprese sotto i 50 addetti, certificazione preventiva, senza rimborso in denaro.

**Profilo negli anni.** PE04 parte solo nel 2030 e cresce di circa 0,1 l'anno (`programma/coperture_menu.csv`, nota PE04). Il pilota quindi parte a tappe:

| Anni | Che cosa si finanzia |
|---|---|
| 2027-2029 | Borse dall'anno accademico 2027/28 e infermiere di pratica avanzata, circa 0,03-0,10 l'anno, coperti dal minor costo di 01-P13 (0,01 / 0,06 / 0,11) |
| 2030 | Indennità in 2 Regioni |
| 2031 | Indennità in 4 Regioni |
| Dal 2032 | Regime: 0,35 |

**[Giudizio]** Questo profilo è una stima mia, da verificare con la Ragioneria. Il resto del programma è contato a regime, come qui.

- **Valutazione.** Agenas valuta 30 mesi dopo l'avvio dell'indennità. Si passa alla versione essenziale (1,4) solo se aumentano le iscrizioni e la permanenza del personale, e solo con una copertura nuova.
- **Destinazione di RP08.** Va scritta in legge a 06-C2 e 06-C3, come già indicato in `programma/coperture_personale.md`.

### Motivazione con i valori
- **Benessere (BEN) ed Equità (EQU).** L'Italia ha 6,9 infermiere e infermieri ogni 1.000 abitanti, contro 9,2 della media OCSE (scheda 06-C2). Senza questo personale le Case della Comunità, che costano 0,80, rendono meno (scheda 06-C3, rischi).
- **Fiducia (FID).** Si prova prima di spendere 1,4 mld.
- **[Giudizio, da dichiarare]** Il motore, con utilità che si sommano, preferirebbe tenere 01-P13 pieno. Il valore per mld è 1,44 per 01-P13 e 0,37 per 06-C2 (`motore/esito_proposte.csv`). La mia scelta si regge su due ragioni che il motore non vede:
  - la complementarità con 06-C3, cioè 0,80 già spesi;
  - il valore dell'informazione del pilota.
- 06-C2 è "dipendente dai valori"; 01-P13 è "in coda". Nessuna misura del nucleo robusto scende.
- Resta rispettata la scelta del 9 novembre di tenere le misure di innovazione almeno in versione essenziale.

### Conto (a regime)

| Voce | mld |
|---|---|
| Spesa sulle risorse generali, oggi | 7,01 |
| + 06-C2 PILOTA | +0,35 |
| − 01-P13 da piena a essenziale | −0,14 |
| **Spesa sulle risorse generali, con la proposta** | **7,22** |
| Gettito delle risorse generali: 7,01 + PE04 | 7,31 |
| Margine | 0,09 |
| di cui ambulatori per smettere di fumare (scelta 2) | 0,04 |
| di cui riserva per il dopo 2029 (scelta 4) | 0,05 |
| **Margine finale** | **0** |

- Coperture invariate: 7,42.
- Spesa totale: 9,17 + 0,35 − 0,14 + 0,04 = 9,42.
- Ottimizzatore, senza la voce sul fumo: 9,38 di spesa e 67 proposte su 78.
- Il vincolo di SF16 (risorse del patent box al credito per la ricerca) resta rispettato, perché 0,16 è meno di 0,20.

### Chi guadagna e chi perde
- **Guadagnano:**
  - chi vive nelle 4 Regioni pilota e nelle aree interne;
  - 5.000 studentesse e studenti di infermieristica;
  - il personale infermieristico nelle zone disagiate (fino a 3.000 € lordi l'anno);
  - le persone anziane seguite dalle Case della Comunità.
- **Perdono:**
  - le imprese con almeno 50 addetti, che perdono il credito per la ricerca del 10%;
  - le startup, che perdono il rimborso in denaro;
  - le imprese sotto i 50 addetti, che passano dal 13% al 12%;
  - la riduzione del deficit implicita, cioè i 0,30 di PE04 che oggi migliorano il saldo;
  - la futura pensione di garanzia (02-C3), che perde la copertura pensata per lei.
- **Regola per 02-C3.** La pensione di garanzia costa solo dal 2036. Per lei propongo di usare il gettito di PE04 oltre il minimo (fino a 0,50 nel 2035) e di decidere nella legge di bilancio del 2034.

### Rischi
- **Ricorso alla Corte costituzionale su PE04.** Il dubbio è "serio, attenuato" (`costituzione/esami/governai_conti_2027_2029.md`). Mitigazione: fasce graduate (75% tra 6 e 8 volte il minimo, 50% oltre) e relazione INPS. Il legame con le cure alle persone anziane rafforza la motivazione di solidarietà. Va comunque verificato da chi fa diritto.
- **Imprese che investono in ricerca.** Rischio di contrarietà e di perdere il segnale di stabilità del credito.
- **Personale che si sposta senza aumentare.** Mitigazione: indennità legata alla permanenza e borse con impegno nel SSN.

### Alternativa scartata
Lasciare fare all'ottimizzatore senza obblighi sulle misure di innovazione. In quel caso escono 01-P13 e 04-P7 e si azzerano 04-P8 e 04-P9. Le misure di innovazione avrebbero pagato per la seconda volta in una settimana (12 novembre) e si sarebbe annullata una scelta già dichiarata.

---

## Scelta 4. Fondi europei dopo il 2029

**[Fatto]** Gli 0,50 sono:
- 03-P4 prevenzione dei rischi: 0,25 sul FESR;
- 05-C2 conto competenze: 0,15 sul FSE+;
- 05-C1 dispersione scolastica: 0,08 sul FSE+;
- 09-C8 staffetta delle competenze: 0,02.

Le fonti sono `programma/varianti/` e `programma/coesione_dopo_2029.csv`.

**[Fatto]** Il ciclo europeo 2028-2034 prevede un fondo unico di 865 mld, con almeno il 14% per gli obiettivi sociali. Ci sono regolamenti in parte concordati, ma ancora nessun importo per l'Italia. Il nuovo ciclo comincia a spendere tardi (`benchmark/fondi_coesione_bandi.md`, sezione "Dopo il 2029").

**[Fatto]** Il margine di coesione 2027-2029 è in pratica già usato da prelievi non contati: 07-C4 (0,05), 06-C10 (0,03) e 02-C2 (stessa fonte).

### Proposta: non bloccare oggi 0,50, ma decidere oggi la regola e la riserva

1. **Negoziato, da subito.**
   - Le quattro misure entrano nella proposta italiana di piano di partenariato 2028-2034: adattamento al clima per 03-P4; formazione degli adulti e lotta alla dispersione per 05-C2 e 05-C1.
   - Si chiedono costi semplificati.
   - Si chiede di anticipare la spesa per evitare il vuoto di cassa del 2030-2031.
2. **09-C8 a carico nazionale dal 2030 in ogni caso** (0,02), con i risparmi certificati del ricambio selettivo RP01 oltre il minimo (gettito da 0,04 a 0,10). Sono assunzioni di personale stabile: è coerente con la regola "niente personale stabile su fondi europei".
3. **Clausola di salvaguardia, scritta nella prima legge di bilancio.**
   - Entro il 30 settembre 2029 la Ragioneria certifica, misura per misura, la quota europea programmata per il 2030-2032.
   - Se manca, la legge di bilancio 2030 usa, in quest'ordine:
     - a. **la riserva di 0,05** creata alla scelta 3, destinata per prima a 05-C1;
     - b. **il gettito delle coperture già attive oltre il minimo**, certificato dalla Ragioneria sul consuntivo 2028. Il margine tra gettito minimo e massimo delle coperture generali attive è 6,46 mld (7,01 contro 13,47: mio calcolo su `programma/selezione_intermedio.csv`). I primi 0,50 certificati vanno alla salvaguardia; il resto va alla riduzione del debito;
     - c. **se ancora non basta, si scende di variante in un ordine dichiarato**, per proteggere chi parte svantaggiato:
       - prima 03-P4: la parte opere slitta e restano il fondo nazionale (0,55 senza coesione) e l'assicurazione;
       - poi 05-C2: la dote si riduce in proporzione, come già accettato nel verbale dell'8 novembre;
       - per ultima 05-C1.

### Motivazione con i valori
- **Responsabilità verso il futuro (FUT) e Fiducia (FID).** La regola è scritta prima, non improvvisata nel 2029.
- **Equità (EQU).** Si proteggono per ultime le ragazze e i ragazzi a rischio di abbandono (05-C1, EQU +2).
- **[Giudizio]** Bloccare oggi 0,50 vorrebbe dire tagliare subito misure in corso per un rischio del 2030. È probabile che il fondo europeo copra l'adattamento al clima e la formazione degli adulti, perché sono suoi obiettivi tipici. Il rischio vero sono i tempi e gli importi, e la clausola serve proprio a questo.

### Conto

| Voce | mld |
|---|---|
| Riserva, a regime dal 2032 | 0,05 |
| 09-C8 nazionale dal 2030 | 0,02 (da RP01 oltre il minimo) |
| Parte coperta solo dalla regola (gettito oltre il minimo certificato, poi riduzione di variante) | 0,43 |
| Tasse nuove e deficit nuovo | 0 |

### Chi guadagna e chi perde
- **Guadagnano:** le persone che studiano nelle scuole fragili, perché la loro misura è protetta per prima, e chi segue i conti, perché sa in anticipo che cosa succede.
- **Perdono, se l'Europa non paga:**
  - i Comuni a rischio idrogeologico, perché le opere slittano;
  - le persone adulte senza diploma, perché la dote è più bassa;
  - la riduzione del debito, che riceve una parte minore del gettito oltre il minimo.

### Rischi
- Il gettito oltre il minimo potrebbe non esserci, per esempio per contrabbando o per consumi in calo più del previsto.
- Usarlo sulla regola europea della spesa netta va verificato con la Ragioneria.
- Il vuoto di cassa del 2030-2031 resta probabile anche se i fondi arrivano.
- Fuori dagli 0,50 c'è anche il subentro nazionale di 02-C5 dal 2030: circa 0,033 per il personale (`benchmark/fondi_coesione_bandi.md`).

### Alternative scartate
- **Copertura nazionale piena decisa oggi.** Senza tasse vorrebbe dire abbassare oggi misure del nucleo per 0,50.
- **Usare RA11, cioè l'organico della scuola che segue il calo delle nascite.** È esclusa dallo scenario per scelta politica, e ridurla toglierebbe posti a chi aspira a insegnare.
- **Aspettare senza regola.** Il programma resterebbe, a parole, finanziato da fondi che finiscono nel 2029.

---

## Sintesi delle quattro proposte

| Scelta | Proposta | mld |
|---|---|---|
| 1 | Responsabile eletta per 2 anni, che firma ogni scelta politica. Comitato di garanzia di 9 persone (3 esperti, 3 di sensibilità culturali diverse, 3 cittadini), tutte sorteggiate tra persone idonee. Solo poteri di garanzia | 0 |
| 2 | Gettito del tabacco destinato per legge alla sanità vicino a casa. Ambulatori gratuiti per smettere di fumare. Metà del fondo flotte alle imprese di autotrasporto piccole e del Sud | +0,04 |
| 3 | 06-C2 PILOTA, finanziato da PE04 spostata nelle risorse generali (+0,30) e da 01-P13 in versione essenziale (−0,14) | +0,35 / −0,14 |
| 4 | Negoziato europeo subito, 09-C8 a carico nazionale, riserva di 0,05, clausola con data e ordine di riduzione che protegge 05-C1 | 0,05 di riserva |

Risorse generali: 7,22 di spesa + 0,04 + 0,05 = 7,31, pari al gettito di 7,31. Nessuna tassa nuova e nessun deficit nuovo.
