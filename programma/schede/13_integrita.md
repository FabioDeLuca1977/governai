# Schede pronte: Integrità degli appalti

*Agente "integrità degli appalti" di GovernAI, 8 novembre 2026. Consigliere, non decisore. La proposta è numerata **08-P7** perché riguarda l'area istituzionale (riforme, controlli). Varianti in `programma/varianti/13_integrita.csv`. Dati e metodo in `trasparenza/` (`README.md`, `rapporto.md`, `indicatori.py`). Importi in mld €/anno; "stima GovernAI" quando non esiste una stima ufficiale.*

| Proposta | Variante | Intensità | Costo a regime | Anno regime | Fondo |
|---|---|---|---|---|---|
| 08-P7 Appalti a vetro | PIENA | 1 | 0,008 | 2028 | RIALLOCAZIONE |
| | ESSENZIALE | 0,55 | 0,003 | 2028 | RIALLOCAZIONE |
| | PILOTA | 0,15 | 0,001 | 2028 | RIALLOCAZIONE |

**Regole di copertura rispettate.** Nessun prelievo da DEFICIT, RISPARMI_ATTESI, IVA_EVASIONE, ETS o ALTRO. La copertura viene da una riallocazione nel bilancio ANAC e dal taglio delle consulenze esterne della PA, misura già proposta da 08-P1 e 09-C1. **L'agente coperture deve verificarne la capienza complessiva**, per evitare il doppio conteggio. I risparmi attesi da una maggiore concorrenza negli appalti non sono usati come copertura.

---

## 08-P7 — Appalti a vetro: cruscotto pubblico dei rischi e dati aperti completi

### Problema in un dato
Nel 2024, tra le procedure con confronto competitivo per cui il dato è disponibile, **il 54,8% è stato aggiudicato con una sola offerta**: 56.365 procedure valutabili su 904.301 CIG analizzati (ANAC, BDNCP open data; elaborazione GovernAI, `trasparenza/rapporto.md`). Il valore coincide con il 55% trovato dall'UIF sul 2018-2023 (Quaderno 23/2024). Per la Commissione europea, nel Single Market Scoreboard, oltre il 20% di offerte uniche è un risultato "scarso". Inoltre il numero di offerte è noto solo per circa 56.000 procedure non dirette su 191.000. I dati mancano soprattutto in alcuni tipi di enti e territori, secondo l'UIF: **chi comunica meno sembra meno a rischio**.

### Soluzione in 3 righe
1. ANAC pubblica un **cruscotto aperto dei rischi** per stazione appaltante e per settore. Indicatori e pesi sono dichiarati, con intervalli di confidenza e confronto con l'atteso nazionale per lo stesso mix di contratti. Il punto di partenza è il prototipo GovernAI (`trasparenza/`) insieme ai 17 indicatori del progetto ANAC "Misurare la corruzione".
2. La **completezza dei dati** diventa un obbligo misurato. Ogni ente ha un indicatore pubblico di reticenza, e determine e bandi si pubblicano in formato aperto e testuale collegati al CIG, così anche la cittadinanza, la stampa e i RPCT possono leggerli, con l'assistenza di strumenti di AI (`trasparenza/istruzioni_lettura_atti.md`).
3. **Garanzie**: il cruscotto valuta enti e procedure, mai persone. Nessun uso automatico per sanzioni, esclusioni o rating di imprese. Ogni anno una validazione indipendente misura falsi positivi e utilità.

### Varianti
- **PIENA** (intensità 1; 0,008 mld dal 2028): cruscotto trimestrale, obbligo di completezza, repository testuale degli atti collegati al CIG, validazione indipendente, formazione degli RPCT.
- **ESSENZIALE** (0,55; 0,003 mld): cruscotto e indicatore di completezza con delibera ANAC, senza repository testuale. Si possono verificare i segnali statistici, non i requisiti su misura né le motivazioni.
- **PILOTA** (0,15; 0,001 mld): 18 mesi in 3 regioni, con valutazione dei falsi positivi prima dell'estensione.

### Articolato normativo essenziale
**Disegno di legge "Disposizioni per la trasparenza dei rischi negli appalti pubblici"**

**Art. 1 (Finalità).** La presente legge rende pubblici, comprensibili e verificabili i dati sui contratti pubblici e i relativi indicatori di rischio, per orientare i controlli e la partecipazione civica, in attuazione degli articoli 97 della Costituzione, 23 e 28 del decreto legislativo 31 marzo 2023, n. 36, e della legge 6 novembre 2012, n. 190.

**Art. 2 (Cruscotto pubblico dei rischi).**
1. L'Autorità nazionale anticorruzione pubblica, con cadenza almeno trimestrale e in formato aperto, indicatori di rischio sui contratti pubblici calcolati dalla Banca dati nazionale dei contratti pubblici, per stazione appaltante, settore merceologico e territorio.
2. Per ciascun indicatore sono pubblicati la definizione, il peso nell'eventuale indice composito, il numero di casi su cui è calcolato, l'intervallo di confidenza e il valore atteso per contratti dello stesso tipo e importo.
3. Il codice di calcolo è rilasciato con licenza aperta ai sensi dell'articolo 69 del decreto legislativo 7 marzo 2005, n. 82.
4. Gli indicatori non riguardano persone fisiche e non contengono dati personali.

**Art. 3 (Natura degli indicatori e garanzie).**
1. Gli indicatori di cui all'articolo 2 hanno esclusivamente funzione di orientamento dei controlli e di trasparenza. Non costituiscono prova né presupposto sufficiente per l'adozione di provvedimenti sanzionatori, di esclusione o di valutazione di persone o di operatori economici.
2. Ogni pubblicazione reca l'avvertenza che gli scostamenti possono avere giustificazioni legittime. Ciascuna stazione appaltante può pubblicare, accanto ai propri indicatori, le proprie osservazioni.

**Art. 4 (Completezza dei dati).**
1. All'articolo 28 del decreto legislativo 31 marzo 2023, n. 36, dopo il comma 3 è inserito il seguente: «3-bis. Le determinazioni a contrarre, i bandi, gli avvisi e i provvedimenti di aggiudicazione e di modifica del contratto sono trasmessi alla Banca dati nazionale dei contratti pubblici in formato aperto e testuale, collegati al codice identificativo di gara, entro i termini previsti per la pubblicazione.»
2. L'Autorità pubblica per ciascuna stazione appaltante un indicatore di completezza delle comunicazioni dovute. L'indicatore è considerato nella valutazione della performance dei dirigenti responsabili, ai sensi del decreto legislativo 27 ottobre 2009, n. 150.

**Art. 5 (Validazione e strumenti per i controlli).**
1. Ogni anno un comitato indipendente, composto da persone esperte designate dalla Corte dei conti, dall'ISTAT e da università, valuta la capacità predittiva degli indicatori e la quota di falsi positivi e ne riferisce alle Camere.
2. L'Autorità mette a disposizione dei responsabili della prevenzione della corruzione e della trasparenza strumenti di lettura assistita degli atti di gara. Gli strumenti sono conformi al regolamento (UE) 2024/1689 e prevedono sempre la verifica umana.

**Art. 6 (Copertura finanziaria).** Agli oneri, pari a 4 milioni di euro per il 2027 e a 8 milioni di euro annui dal 2028, si provvede mediante riallocazione delle risorse del bilancio dell'Autorità e corrispondente riduzione delle spese per incarichi di consulenza delle amministrazioni centrali.

### Cronoprogramma
| Fase | Chi | Cosa |
|---|---|---|
| Primi 100 giorni | ANAC | Delibera sul cruscotto (variante ESSENZIALE), pubblicazione dei primi indicatori 2024-2025 con avvertenze; avvio del PILOTA in 3 regioni |
| 12 mesi | Governo, Parlamento, ANAC, AgID | Approvazione del DDL; standard per la trasmissione testuale degli atti tramite le piattaforme certificate |
| 24 mesi | ANAC, comitato di validazione | Prima relazione di validazione; revisione di pesi e soglie; estensione nazionale |

### Indicatori
| KPI | Base | Obiettivo a 3 anni | Obiettivo a 5 anni |
|---|---|---|---|
| Procedure non dirette con numero di offerte comunicato | circa 56.000 su 191.000 (29%, 2024, elaborazione GovernAI su ANAC) | 80% | 95% |
| Quota di aggiudicazioni con offerta unica (procedure con confronto competitivo) | 54,8% (2024) | 45% | 35% |
| Enti pubblici con indice di rischio sopra l'atteso anche al limite inferiore IC 90% | 161 su 2.291 (2024) | da ridurre del 30%, con relazione sulle cause | da ridurre del 50% |
| Atti di gara disponibili in formato testuale collegati al CIG | n.d. | 60% | 95% |

### Effetti sui valori della Carta
- **FID** (+): rende pubblici dati, criteri e risultati. È il cuore della definizione di trasparenza.
- **EQU** e **FUT** (+): più concorrenza significa prezzi più bassi e risorse liberate. L'effetto non è usato come copertura.
- **SIC** (neutro o +): controlli mirati e verificabili, senza profilazione di persone, con verifica umana e validazione indipendente.
- **CIT** (+): la cittadinanza, la stampa e chi siede nei consigli locali possono fare domande documentate.
- **Rischio sui valori**: stigmatizzare enti piccoli o in emergenza (RIS). La mitigazione è nelle avvertenze, nel diritto di replica dell'ente e nella graduatoria per limite inferiore.

### Rischi e mitigazione
- **Gogna e falsi positivi.** Le garanzie dell'art. 3 e il diritto di replica limitano il rischio. La graduatoria usa il limite inferiore dell'intervallo, e la validazione annuale misura i falsi positivi.
- **Adattamento degli enti** (gaming): ad esempio inviti di comodo per evitare l'offerta unica. Si attenua ruotando e aggiornando gli indicatori e affiancando al cruscotto la lettura degli atti.
- **Più reticenza invece di più trasparenza.** L'indicatore di completezza è pubblico e pesa nella performance della dirigenza.
- **Carico per i piccoli comuni.** La trasmissione testuale avviene in automatico dalle piattaforme certificate; c'è un raccordo con i pool tecnici di 09-C3.

---

*Schede aggiunte il 16 novembre 2026: ricerca su fonti ufficiali, tre valutatori indipendenti, verifica giuridica e scelte di chi guida il progetto. Fonti e modifiche: `benchmark/bozza_proposte_anticorruzione.md`.*

---

## 08-P8 — Influenza alla luce del sole: registro delle lobby, agenda pubblica, impronta legislativa

### Problema in un dato
L'Italia non ha una legge nazionale sulle lobby. La Commissione europea lo raccomanda dal 2023 e nel 2026 registra solo "progressi limitati": il DDL A.S. 1780, approvato dalla Camera il 29 gennaio 2026, è fermo al Senato. Secondo la Commissione esclude sindacati e associazioni datoriali, non prevede l'impronta legislativa e non obbliga le società di lobbying a dire per conto di chi lavorano (Rapporto Stato di diritto 2026, p. 11). La Corte costituzionale, nella sentenza 185/2025, ha invitato il Parlamento a distinguere per legge la rappresentanza legittima di interessi dal traffico di influenze. Sul finanziamento della politica tramite fondazioni la Commissione non vede progressi dal 2024.

### Evidenze
- **UE**: da quando l'iscrizione al registro per la trasparenza è condizione per incontrare Commissione e Parlamento, le nuove iscrizioni sono salite a 4.112 nel 2025; gli iscritti sono 17.269 ad aprile 2026 (TI EU, fonte secondaria).
- **Francia**: repertorio HATVP con 3.526 iscritti e oltre 107.000 schede di attività a fine 2025; 19 casi trasmessi alla procura per mancata dichiarazione.
- **Irlanda**: Regulation of Lobbying Act 2015, registro online con dichiarazioni periodiche.
- Non ci sono valutazioni causali sull'effetto delle leggi sulle lobby sulla corruzione. L'effetto atteso è sulla **trasparenza e sulla parità di accesso**: chi decide sa di essere visto, e chi non ha lobbisti vede chi ne ha.

### Soluzione in 3 righe
1. **Registro unico e obbligatorio** tenuto dall'ANAC per **tutti** quelli che incontrano Governo, ministeri, autorità indipendenti, Regioni e grandi Comuni per influenzare un atto: società, studi, associazioni, ONG, **sindacati e associazioni datoriali**. Nessuna esenzione per categoria. Si dichiarano i clienti e le risorse spese. **Senza iscrizione, niente incontri.** Restano **liberi** i contatti dei cittadini e delle associazioni che difendono un interesse proprio.
2. **Agenda pubblica** degli incontri di ministri, viceministri, sottosegretari, capi di gabinetto e dirigenti di prima fascia, e **impronta legislativa**: ogni disegno di legge del Governo e ogni decreto elenca gli interessi ascoltati e i documenti ricevuti.
3. **Registro elettronico unico dei finanziamenti alla politica** (partiti, fondazioni e associazioni collegate, candidature), in formato aperto ma con i **soli dati minimi** sui finanziatori.

### Varianti
| Variante | Contenuto | Intensità | Costo a regime | Strumento |
|---|---|---|---|---|
| **PIENA** | Registro ANAC per tutti quelli che incontrano i decisori per influenzare atti, **sindacati e associazioni datoriali compresi**, senza esenzioni per categoria; contatti liberi per cittadini e associazioni che difendono interessi propri; iscrizione gratuita e regime semplificato sotto una soglia di spesa; clienti e spese dichiarati; agenda pubblica; impronta legislativa; registro unico dei finanziamenti alla politica con dati minimi (nome, importo, destinatario sopra 500 €, per 5 anni); periodo di raffreddamento di 2 anni per ex membri del Governo; per Regioni e grandi Comuni principi e livelli essenziali con intesa; per le Camere proposta di modifica dei regolamenti | 1 | 0,004 dal 2028 | disegno di legge (o emendamenti all'A.S. 1780) |
| **ESSENZIALE** | Registro e agenda solo per il Governo e i ministeri, **per tutti i rappresentanti di interessi, parti sociali comprese**; impronta legislativa solo per i disegni di legge del Governo; nessun registro dei finanziamenti alla politica | 0,5 | 0,002 dal 2028 | emendamenti all'A.S. 1780 + DPCM |
| **ZERO** | Approvazione dell'A.S. 1780 con **un solo emendamento** che toglie le esenzioni per categoria (parti sociali comprese); agenda pubblica dei membri del Governo con DPCM, a risorse invariate | 0,2 | 0,0005 | legge già in Parlamento + DPCM |

**Scelta di chi guida il progetto (16/11/2026).** Si iscrivono **tutti** quelli che incontrano i decisori per influenzare atti, sindacati e associazioni datoriali compresi: nessuna esenzione per le parti sociali. È la lacuna che la Commissione europea segnala nell'A.S. 1780. Il ruolo costituzionale delle parti sociali (artt. 39 e 99) non è toccato: l'iscrizione è gratuita, automatica e non è un'autorizzazione; chiede solo di dire chi si incontra e su cosa. Anche gli incontri di concertazione e le consultazioni previste dalla legge restano possibili e finiscono nell'agenda pubblica come gli altri.

### Articolato essenziale
**Disegno di legge "Disposizioni per la trasparenza della rappresentanza di interessi e del finanziamento della politica"**

**Art. 1 (Finalità).** La presente legge rende pubblica e verificabile l'attività di rappresentanza di interessi presso i decisori pubblici e il finanziamento dell'attività politica, in attuazione degli articoli 1, 49 e 97 della Costituzione, e distingue la rappresentanza legittima di interessi dalle condotte di cui all'articolo 346-bis del codice penale.

**Art. 2 (Registro).** 1. È istituito presso l'Autorità nazionale anticorruzione il registro pubblico dei rappresentanti di interessi. 2. È rappresentanza di interessi ogni contatto con i decisori di cui all'articolo 3 diretto a influenzare l'adozione, la modifica o il contenuto di un atto normativo, amministrativo generale o di programmazione, svolto per conto proprio o di terzi da imprese, società di consulenza, studi professionali, associazioni, fondazioni, organizzazioni non governative, organizzazioni sindacali e associazioni dei datori di lavoro. Non sono previste esenzioni per categoria di soggetti. 3. L'iscrizione è gratuita, avviene con una dichiarazione ed è condizione per svolgere attività di rappresentanza di interessi. Gli iscritti dichiarano ogni sei mesi i soggetti per conto dei quali operano, le materie trattate e le risorse impiegate, per fasce; sotto una soglia annua di spesa fissata dall'Autorità la dichiarazione è semplificata. 4. Non costituiscono rappresentanza di interessi: a) i contatti dei cittadini in nome proprio; b) i contatti di associazioni e comitati per la difesa di un interesse proprio, relativo a procedimenti, beni o finanziamenti che li riguardano direttamente, e non degli interessi di una categoria o di un settore; c) le richieste di informazioni su procedimenti propri; d) l'attività giornalistica. 5. Le sedute di concertazione e le consultazioni previste dalla legge sono pubblicate nell'agenda di cui all'articolo 3.

**Art. 3 (Agenda pubblica).** 1. I membri del Governo, i capi di gabinetto e degli uffici legislativi, i dirigenti di prima fascia e i vertici delle autorità indipendenti pubblicano, entro quindici giorni, data, partecipanti e oggetto di ogni incontro con rappresentanti di interessi. 2. Per le Regioni e i Comuni con più di 100.000 abitanti la presente legge stabilisce i principi e i livelli essenziali di trasparenza; le modalità sono definite con intesa in Conferenza unificata. Per le Regioni a statuto speciale e le Province autonome si provvede con norme di attuazione degli statuti.

**Art. 4 (Impronta legislativa).** La relazione illustrativa di ogni disegno di legge del Governo, decreto-legge e decreto legislativo reca l'elenco dei rappresentanti di interessi incontrati e dei contributi ricevuti durante la preparazione dell'atto, con link ai documenti.

**Art. 5 (Periodo di raffreddamento).** Per due anni dalla cessazione dell'incarico, i membri del Governo non possono svolgere attività di rappresentanza di interessi nei confronti dell'amministrazione che hanno diretto.

**Art. 6 (Finanziamento della politica).** 1. È istituito presso la Commissione di garanzia per la trasparenza e il controllo dei rendiconti dei partiti politici un registro elettronico unico, in formato aperto, dei contributi superiori a 500 euro annui ricevuti da partiti, movimenti, fondazioni e associazioni di cui all'articolo 5, comma 4, del decreto-legge 28 dicembre 2013, n. 149, e da candidati alle elezioni. 2. Sono pubblicati entro trenta giorni dalla ricezione solo il nome del contribuente, l'importo e il destinatario; non sono pubblicati indirizzi né altri dati di contatto. I dati restano pubblicati per cinque anni. 3. Il regime si coordina con la legge 9 gennaio 2019, n. 3, in materia di consenso alla pubblicazione. 4. Lo schema dei decreti attuativi è sottoposto al parere del Garante per la protezione dei dati personali.

**Art. 7 (Sanzioni).** La violazione degli obblighi è punita con sanzione amministrativa da 2.000 a 50.000 euro e, nei casi gravi o ripetuti, con la sospensione dal registro fino a un anno. La sanzione si applica anche al decisore che incontra soggetti non iscritti. Si applica la legge 24 novembre 1981, n. 689.

**Art. 8 (Camere).** Le Camere sono invitate ad adottare, con modifiche dei propri regolamenti, regole equivalenti per i propri organi e componenti.

**Art. 9 (Copertura).** Agli oneri, pari a 2 milioni di euro per il 2027 e 4 milioni annui dal 2028, si provvede mediante riallocazione nel bilancio dell'Autorità e corrispondente riduzione delle spese di funzionamento della Presidenza del Consiglio dei ministri.

### Chi ne è toccato
Rappresentanti di interessi, **parti sociali comprese** (obblighi di dichiarazione); decisori pubblici (agenda); partiti e fondazioni (registro dei contributi). Chi dona sopra 500 € l'anno vede pubblicati solo nome, importo e destinatario, per 5 anni. Nessun obbligo per i cittadini e per le associazioni che difendono un interesse proprio. Vantaggio per chi oggi non ha accesso ai decisori: vede chi lo ha.

### Rischi e mitigazione
- **Burocrazia per i piccoli soggetti** (associazioni, comitati): contatti liberi se difendono un interesse proprio; dichiarazione semplificata sotto una soglia di spesa; nessun costo di iscrizione.
- **Libertà sindacale** (art. 39): l'iscrizione è una dichiarazione gratuita, non un'autorizzazione, e non limita la contrattazione; la concertazione resta e diventa pubblica nell'agenda.
- **Effetto di spostamento**: gli incontri passano a canali informali. Mitigazione: la definizione copre anche telefonate e messaggi rilevanti; le sanzioni valgono anche per il decisore che incontra soggetti non iscritti.
- **Autonomia delle Camere** (art. 64 Cost.) **e delle Regioni** (artt. 117 e 123): per le Camere solo modifiche dei regolamenti; per le Regioni principi e livelli essenziali con intesa, norme di attuazione per le speciali.
- **Privacy di chi dona** (il sostegno a un partito è un dato particolare, art. 9 GDPR): soglia di 500 €, solo nome, importo e destinatario, nessun dato di contatto, 5 anni, parere del Garante. Da verificare se la L. 3/2019 chiede oggi il consenso del donatore.

### Indicatori
| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Valutazione della Commissione UE sulla raccomandazione "lobby" | "progressi limitati" (2026) | "progressi significativi" | raccomandazione chiusa |
| Iscritti al registro nazionale | 0 (nessun registro nazionale) | n.d., da fissare dopo il primo anno | crescita annua documentata |
| Disegni di legge del Governo con impronta legislativa | 0% | 90% | 100% |
| Contributi alla politica sopra soglia pubblicati in formato aperto | nessun registro unico | 100% di partiti e fondazioni collegate | 100%, con controlli a campione |
| OCSE PII, lobby, pratica | 44% (2026) | 60% | 70% |

---

## 08-P9 — Integrità di chi decide: dichiarazioni verificate, conflitti di interessi, porte girevoli

### Problema in un dato
Per i conflitti di interessi l'Italia soddisfa il **100% dei criteri OCSE sulle regole, ma solo il 22% sulla pratica** (media OCSE 45%). Il GRECO, a giugno 2026, ha trovato attuata 1 sola raccomandazione su 19; restano aperte la **verifica di merito delle dichiarazioni patrimoniali**, un sistema efficace di sanzioni e i controlli di integrità prima delle nomine. Il DDL sui conflitti di interessi, approvato dalla Camera il 28 maggio 2024, è fermo al Senato. Ad agosto 2025 la L. 122/2025 ha **abrogato** il periodo di raffreddamento per chi passa da cariche locali e regionali alla guida di società pubbliche (art. 7 d.lgs. 39/2013).

### Evidenze
- **Francia, HATVP**: nel 2025 ha ricevuto 10.362 dichiarazioni patrimoniali e di interessi e ne ha **controllate 5.795**; dà pareri preventivi sul passaggio al privato di chi ha avuto incarichi pubblici.
- La **direttiva (UE) 2026/1021** prevede organismi specializzati con risorse e poteri adeguati, che possono verificare le dichiarazioni patrimoniali.
- Il PNA 2026 dell'ANAC prevede già moduli standard e più verifiche a campione sugli incarichi (Rapporto Stato di diritto 2026, nota 84): la proposta dà a questo obiettivo una base di legge e risorse.

### Soluzione in 3 righe
1. Una **Sezione per l'integrità pubblica dentro l'ANAC** (niente nuova autorità) riceve in formato digitale unico le **dichiarazioni patrimoniali e di interessi** di membri del Governo, presidenti e assessori regionali, sindaci e assessori dei Comuni sopra 15.000 abitanti, vertici di autorità, enti e società pubbliche e dirigenti apicali dello Stato.
2. Le dichiarazioni sono **verificate**: sempre per i vertici (ministri, presidenti di Regione, sindaci dei capoluoghi), **a campione sorteggiato** per gli altri, e quando c'è una segnalazione documentata. Per la verifica la Sezione può consultare, caso per caso e con registro degli accessi, l'Anagrafe tributaria e i registri immobiliari e societari: **l'accesso ai dati fiscali è previsto da una norma di legge**, mai da un atto amministrativo.
3. **Coniuge**: la sua dichiarazione si chiede **solo con il suo consenso** (come nella L. 441/1982), serve solo alla verifica e **non è mai pubblicata**; nelle sintesi pubbliche non compaiono nomi di familiari.
4. **Proporzionalità per i piccoli Comuni**: nei Comuni tra 15.000 e 50.000 abitanti modulo breve precompilato con i dati già in possesso della PA, campione di verifica più basso (10%) e nessun nuovo ufficio locale; sotto i 15.000 abitanti nessun obbligo nuovo.
5. **Porte girevoli**: chi lascia un incarico di vertice chiede un **parere preventivo** prima di lavorare per un privato del settore che ha regolato o finanziato; si ripristina il raffreddamento abrogato nel 2025; la legge sui conflitti di interessi del Governo sostituisce la L. 215/2004.

### Varianti
| Variante | Contenuto | Intensità | Costo a regime | Strumento |
|---|---|---|---|---|
| **PIENA** | Sezione ANAC con circa 70 unità; dichiarazioni digitali per circa 10.000-12.000 persone (stima GovernAI); verifica totale dei vertici, a campione del 20% degli altri e del 10% nei Comuni tra 15.000 e 50.000 abitanti (modulo breve precompilato); coniuge solo con consenso e mai pubblicato; parere preventivo vincolante sulle porte girevoli (1-3 anni), con termine perentorio di 60 giorni; ripristino dell'art. 7 d.lgs. 39/2013; nuova legge sui conflitti di interessi del Governo con obbligo di astensione e, sopra una soglia di patrimonio, gestione fiduciaria (blind trust); per le Regioni principi e livelli essenziali con intesa; invito alle Camere ad affidare alla Sezione la verifica delle dichiarazioni dei parlamentari | 1 | 0,010 dal 2028 | disegno di legge |
| **ESSENZIALE** | Stessa Sezione con circa 35 unità; dichiarazioni e verifiche solo per Governo, vertici regionali (con intesa), sindaci dei capoluoghi e vertici di enti e società statali; stesse garanzie su coniuge, pubblicazione e Garante; parere preventivo solo per membri del Governo e capi dipartimento; ripristino dell'art. 7 d.lgs. 39/2013 | 0,55 | 0,005 dal 2028 | disegno di legge |
| **PILOTA** | 18 mesi: dichiarazioni digitali e verifiche per il Governo e per 2-3 Regioni volontarie con i loro Comuni capoluogo; valutazione dei tempi, delle irregolarità trovate e dei costi prima dell'estensione. **Norma di legge breve** per l'accesso ai dati fiscali e per gli obblighi (un DPCM non basta); senza legge, solo su adesione volontaria dei dichiaranti | 0,15 | 0,002 (anni di sperimentazione) | norma di legge breve + protocollo ANAC-Regioni |
| **ZERO** | Solo modulo digitale unico e ripristino dell'art. 7 d.lgs. 39/2013; verifiche a campione con il personale ANAC esistente | 0,2 | 0,0005 | legge ordinaria (norma breve) |

### Articolato essenziale
**Disegno di legge "Disposizioni per l'integrità dei titolari di incarichi pubblici"**

**Art. 1 (Sezione per l'integrità pubblica).** È istituita presso l'Autorità nazionale anticorruzione la Sezione per l'integrità pubblica, con autonomia organizzativa e un contingente di [70 / 35] unità, per la ricezione e la verifica delle dichiarazioni di cui all'articolo 2 e per i pareri di cui all'articolo 4.

**Art. 2 (Dichiarazioni).** 1. I soggetti indicati nell'allegato A presentano alla Sezione, in formato digitale unico, entro trenta giorni dall'assunzione dell'incarico, ogni anno e alla cessazione, una dichiarazione della propria situazione patrimoniale e dei propri interessi. 2. La dichiarazione del coniuge non separato è presentata solo con il suo consenso, è usata solo per la verifica e non è pubblicata. 3. È pubblicata, per la durata dell'incarico e per i tre anni successivi, una sintesi della dichiarazione dei titolari di cariche elettive e di governo, senza nomi di familiari e senza dati da cui si possano ricavare dati particolari; le altre dichiarazioni non sono pubblicate. 4. Per i soggetti dei Comuni con popolazione tra 15.000 e 50.000 abitanti la dichiarazione è resa con un modulo semplificato, precompilato dalla Sezione con i dati già in possesso delle amministrazioni. 5. Restano ferme, ove più ampie, le disposizioni della legge 5 luglio 1982, n. 441, e del decreto legislativo 14 marzo 2013, n. 33. 6. Per le Regioni la presente legge stabilisce i principi e i livelli essenziali; le modalità sono definite con intesa in Conferenza Stato-Regioni; per le Regioni a statuto speciale si provvede con norme di attuazione.

**Art. 3 (Verifiche).** 1. La Sezione verifica ogni anno tutte le dichiarazioni dei soggetti di cui all'allegato A, lettera a), e un campione estratto a sorte, con procedura pubblica, pari ad almeno il [20 / 0] per cento delle altre e al 10 per cento di quelle di cui all'articolo 2, comma 4. 2. Ai soli fini della verifica, la Sezione accede, per il singolo dichiarante e con tracciamento degli accessi, all'Anagrafe tributaria, ai registri immobiliari e al registro delle imprese. 3. È esclusa ogni elaborazione automatizzata diretta a profilare i dichiaranti. 4. In caso di omissione o falsità la Sezione contesta l'irregolarità e chiede chiarimenti; se l'irregolarità persiste, applica una sanzione amministrativa da 5.000 a 50.000 euro, ne dà notizia pubblica solo dopo che la sanzione è definitiva e trasmette gli atti all'autorità giudiziaria quando emergono ipotesi di reato. 5. Lo schema del regolamento di attuazione è sottoposto al parere del Garante per la protezione dei dati personali, previa valutazione d'impatto.

**Art. 4 (Porte girevoli).** 1. Per tre anni dalla cessazione, i soggetti di cui all'allegato A, lettera a), chiedono alla Sezione un parere prima di assumere incarichi presso soggetti privati destinatari di atti o finanziamenti adottati sotto la loro responsabilità. 2. Il parere è reso entro il termine perentorio di sessanta giorni, decorso il quale si intende favorevole; può fissare condizioni ed è pubblicato. 3. È nullo l'incarico assunto in violazione di un parere negativo; si applica l'articolo 53, comma 16-ter, del decreto legislativo 30 marzo 2001, n. 165.

**Art. 5 (Ripristino).** È ripristinato l'articolo 7 del decreto legislativo 8 aprile 2013, n. 39, nel testo vigente prima della legge 8 agosto 2025, n. 122.

**Art. 6 (Conflitti di interessi dei membri del Governo).** Il Governo è delegato ad adottare, entro dodici mesi, un decreto legislativo che sostituisce la legge 20 luglio 2004, n. 215, secondo i seguenti principi: obbligo di astensione documentato; gestione fiduciaria indipendente delle partecipazioni rilevanti sopra una soglia di valore; vigilanza della Sezione; sanzioni proporzionate.

**Art. 7 (Copertura).** Agli oneri, pari a 4 milioni di euro per il 2027 e a [10 / 5] milioni annui dal 2028, si provvede mediante riallocazione nel bilancio dell'Autorità e corrispondente riduzione delle spese di funzionamento dei ministeri.

### Chi ne è toccato
Circa 10.000-12.000 titolari di incarichi pubblici di vertice (stima GovernAI, da verificare con i dati ANAC e Interno). Nessun obbligo nuovo per i dipendenti pubblici che non hanno incarichi di vertice né per gli amministratori dei Comuni sotto i 15.000 abitanti; modulo breve precompilato per i Comuni tra 15.000 e 50.000. Il coniuge dichiara solo se acconsente. Le imprese che assumono ex decisori devono attendere il parere, al massimo 60 giorni.

### Rischi e mitigazione
- **Privacy e Costituzione** (Corte cost. 20/2019; CGUE C-184/20): pubblicazione solo di una sintesi per le cariche elettive e di governo, senza nomi di familiari e per un tempo limitato; dati del coniuge solo con consenso e mai pubblicati; le altre dichiarazioni restano riservate; accessi ai dati fiscali previsti dalla legge, caso per caso e tracciati; niente profilazione; valutazione d'impatto e parere del Garante.
- **Piccoli Comuni** (rilievo dei valutatori): modulo precompilato, campione più basso, nessun nuovo ufficio; sotto i 15.000 abitanti nessun obbligo.
- **Fuga dagli incarichi** e "paura della firma": la verifica riguarda il patrimonio e gli interessi, non la legittimità degli atti; contraddittorio prima della sanzione e pubblicazione solo dopo la sanzione definitiva.
- **Autonomia delle Camere e delle Regioni**: la legge vale per il Governo e per lo Stato; per le Regioni principi, livelli essenziali e intesa (artt. 117 c. 4 e 122 Cost.); per il Parlamento regolamenti. Per le Regioni a statuto speciale serve una norma di attuazione.
- **Sovraccarico di ANAC**, già con vigilanza in calo nel 2025: personale dedicato e non sottratto alla vigilanza sugli appalti.

### Indicatori
| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| OCSE PII, conflitti di interessi, pratica | 22% (2026; media OCSE 45%) | 40% | 50% |
| Raccomandazioni GRECO 5° ciclo attuate | 1 su 19 (giugno 2026; da verificare) | 8 | 15 |
| Dichiarazioni verificate nel merito ogni anno | n.d. (nessuna verifica sistematica) | 2.000 | 3.000 |
| Pareri preventivi sulle porte girevoli resi e pubblicati | 0 | tutti quelli richiesti, entro 60 giorni | idem, con relazione annuale |

---

## 08-P10 — Chi c'è dietro: titolare effettivo verificato per gare e fondi pubblici

### Problema in un dato
Nel 2025 i contratti pubblici sopra 40.000 € hanno raggiunto 287.421 procedure e **309,7 miliardi di €**, di cui circa 20,8 legati al PNRR (Relazione ANAC 2025, sintesi da verificare). Eppure chi partecipa a una gara non deve dichiarare in modo sistematico **chi lo controlla davvero**, e nessuno lo verifica in automatico. Il registro dei titolari effettivi, riformato dal d.lgs. 210/2025, è **sospeso** (Rapporto Stato di diritto 2026, p. 9). Il fascicolo virtuale dell'operatore economico (FVOE) non copre le imprese con sede in altri Stati UE. Senza questo dato, i conflitti di interessi nelle gare (art. 16 d.lgs. 36/2023) e le società schermo si scoprono solo a indagine aperta.

### Evidenze
- L'art. 22 del reg. (UE) 2021/241 obbliga già a raccogliere i titolari effettivi dei destinatari di fondi PNRR: la proposta estende lo standard a tutta la spesa pubblica sopra soglia.
- La direttiva antiriciclaggio (UE) 2024/1640 (art. 12) dà accesso ai registri dei titolari effettivi a giornalisti e società civile con "legittimo interesse"; la Corte di giustizia (C-37/20, 2022) ha annullato l'accesso pubblico generalizzato. La proposta segue questa linea.
- Il PNA 2026-2028 chiede già alle stazioni appaltanti procedure per verificare il titolare effettivo dei fornitori esteri, ma senza un obbligo di legge.

### Soluzione in 3 righe
1. Chi partecipa a una gara sopra 40.000 € o chiede un contributo pubblico sopra 100.000 € **dichiara il titolare effettivo** nel FVOE, una sola volta e con aggiornamento a ogni cambio (once-only, 09-C2).
2. La dichiarazione è **verificata in automatico** con il registro dei titolari effettivi (quando operativo), il registro delle imprese e, per le imprese UE, i registri collegati dalla rete BORIS; per le imprese extra UE serve documentazione equivalente. **Solo una dichiarazione falsa porta all'esclusione** e a una sanzione; un'omissione si sana con il soccorso istruttorio.
3. Il dato serve per **controllare i conflitti di interessi** della singola procedura (commissari, RUP, decisori) e diventa accessibile a chi ha un legittimo interesse. Per gli aggiudicatari sopra 1 milione di € sono pubblicati solo nome, quota e contratto, **per la durata del contratto più 5 anni**, con la motivazione scritta nella legge e il parere del Garante.

### Varianti
| Variante | Contenuto | Intensità | Costo a regime | Strumento |
|---|---|---|---|---|
| **PIENA** | Dichiarazione e verifica per gare ≥ 40.000 € e contributi ≥ 100.000 €; interconnessione FVOE-registro titolari effettivi-registro imprese-BORIS; controllo dei conflitti di interessi nella singola procedura; esclusione solo per dichiarazione falsa, omissione sanabile; pubblicazione di nome, quota e contratto del titolare effettivo degli aggiudicatari sopra 1 milione di €, motivata nella legge e limitata alla durata del contratto più 5 anni, con parere del Garante; accesso per legittimo interesse per gli altri; entrata in vigore per fasi | 1 | 0,004 dal 2029 | decreto legislativo correttivo del d.lgs. 36/2023 |
| **ESSENZIALE** | Solo gare sopra le soglie UE e beneficiari PNRR e coesione; verifica con registro imprese e registro titolari effettivi; esclusione solo per falso, omissione sanabile; nessuna pubblicazione, accesso per legittimo interesse; entrata in vigore per fasi | 0,5 | 0,002 dal 2028 | decreto legislativo correttivo |
| **ZERO** | Campo informativo sul titolare effettivo nel bando-tipo ANAC e nel DGUE, senza verifica automatica e **senza esclusione per omissione** (una delibera non può creare cause di esclusione: art. 10 d.lgs. 36/2023); la falsa dichiarazione resta punita con le cause già previste dal codice | 0,15 | 0,0005 | delibera ANAC |

### Articolato essenziale
**Modifiche al decreto legislativo 31 marzo 2023, n. 36**

**Art. 1.** Dopo l'articolo 24 è inserito il seguente: «Art. 24-bis (Titolare effettivo). 1. Gli operatori economici che partecipano a procedure di affidamento di importo pari o superiore a 40.000 euro dichiarano nel fascicolo virtuale dell'operatore economico i propri titolari effettivi, individuati ai sensi dell'articolo 20 del decreto legislativo 21 novembre 2007, n. 231, e ne comunicano ogni variazione entro trenta giorni. 2. La dichiarazione è verificata in modo automatico mediante interconnessione con la sezione del registro delle imprese dedicata ai titolari effettivi e con i registri degli altri Stati membri collegati ai sensi della normativa dell'Unione. 3. La dichiarazione falsa comporta l'esclusione dalla procedura e la segnalazione all'Autorità per l'iscrizione nel casellario informatico. La dichiarazione omessa o incompleta è regolarizzata con il soccorso istruttorio di cui all'articolo 101; l'esclusione si applica solo se la regolarizzazione non avviene nel termine assegnato. Per gli operatori di Stati non appartenenti all'Unione europea è richiesta documentazione equivalente. 4. I dati sono utilizzati esclusivamente per la verifica dei requisiti, per la prevenzione dei conflitti di interessi di cui all'articolo 16 nella singola procedura e per i controlli antiriciclaggio. È esclusa ogni elaborazione volta a profilare persone fisiche. 5. Poiché l'accesso per legittimo interesse non consente il controllo pubblico sull'uso di somme rilevanti di denaro pubblico, per gli aggiudicatari di contratti di importo superiore a 1 milione di euro sono pubblicati nella Banca dati nazionale dei contratti pubblici solo il nome dei titolari effettivi, la natura e l'entità della partecipazione e il contratto, per la durata del contratto e per i cinque anni successivi. Lo schema delle regole tecniche di pubblicazione è sottoposto al parere del Garante per la protezione dei dati personali. 6. Le disposizioni del presente articolo si applicano per fasi, secondo l'operatività del registro dei titolari effettivi, con decreto del Ministro delle infrastrutture e dei trasporti sentita l'Autorità.»

**Art. 2.** Le disposizioni dell'articolo 24-bis si applicano, in quanto compatibili, ai beneficiari di sovvenzioni, contributi e agevolazioni pubbliche di importo pari o superiore a 100.000 euro, mediante la Piattaforma di cui alla proposta 09-C10.

**Art. 3 (Copertura).** Agli oneri, pari a 2 milioni di euro per il 2027, 5 milioni per il 2028 e 4 milioni annui dal 2029, si provvede mediante riallocazione nel bilancio dell'Autorità nazionale anticorruzione.

### Chi ne è toccato
Le imprese che vendono alla PA o ricevono contributi: un adempimento una tantum, già noto perché previsto dalla normativa antiriciclaggio. Le stazioni appaltanti: meno verifiche manuali. Le persone fisiche titolari effettive: il loro nome è pubblicato solo sopra 1 milione di € di contratto.

### Rischi e mitigazione
- **Privacy e Corte di giustizia (C-37/20 e C-92/09 *Schecke*)**: niente accesso pubblico generalizzato; pubblicazione solo per chi riceve somme rilevanti di denaro pubblico, solo dei dati minimi, per un tempo limitato e con la motivazione di necessità scritta nella legge; parere del Garante sullo schema.
- **Esclusioni sproporzionate**: esclusione solo per falso; omissioni sanate con il soccorso istruttorio.
- **Registro sospeso**: finché il registro dei titolari effettivi non è operativo, la verifica usa il registro delle imprese e i dati PNRR; la norma entra in vigore per fasi.
- **Imprese estere e trust**: la rete BORIS non copre tutto; per i paesi extra UE si chiede documentazione equivalente.
- **Sovrapposizione con l'evasione**: da coordinare con l'agente evasione, che potrebbe proporre usi fiscali dello stesso dato. Qui l'uso è limitato a gare, contributi, conflitti di interessi e antiriciclaggio.

### Indicatori
| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Procedure ≥ 40.000 € con titolare effettivo dell'aggiudicatario dichiarato e verificato | n.d. (nessun obbligo) | 80% | 98% |
| Esclusioni per dichiarazione falsa del titolare effettivo | 0 | dato pubblico annuale | dato pubblico annuale |
| Conflitti di interessi rilevati prima dell'aggiudicazione | n.d. | dato pubblico annuale | in crescita, poi in calo |

---

## 08-P11 — Verifiche a sorte: audit casuali sorteggiati sugli enti che spendono fondi pubblici

### Problema in un dato
La Relazione ANAC 2025 segnala un aumento del 35% delle distrazioni di fondi PNRR (sintesi da verificare), mentre la vigilanza ANAC è scesa da 450 a 208 procedimenti in un anno (Rapporto Stato di diritto 2026). La riforma della Corte dei conti (L. 1/2026) ha ristretto la colpa grave e messo un tetto ai risarcimenti: secondo la Corte stessa cala l'effetto deterrente. Oggi i controlli sul posto si fanno soprattutto **dopo una segnalazione o un'indagine**: chi non è segnalato ha una probabilità di controllo molto bassa e nota.

### Evidenze
- **Brasile**: dal 2003 la CGU sorteggia in pubblico i comuni da controllare sull'uso dei fondi federali. Un audit riduce la corruzione futura dell'**8%** e aumenta del 20% le azioni legali (Avis, Ferraz, Finan, JPE 2018); la pubblicazione dei risultati ha ridotto la rielezione dei sindaci più corrotti (Ferraz, Finan, QJE 2008).
- **Indonesia**: portare la probabilità di audit dal 4% al 100% ha ridotto le spese "mancanti" di circa 8 punti percentuali (Olken, JPE 2007).
- Sono **le prove causali più solide** di tutto il campo anticorruzione. Il sorteggio è anche una garanzia di imparzialità: nessuno è controllato per ragioni politiche.

### Soluzione in 3 righe
1. Ogni anno un **sorteggio pubblico, trasmesso in diretta**, estrae circa 300 enti (Comuni, ASL, enti regionali, società in house) tra quelli che spendono fondi PNRR, di coesione o per investimenti, stratificati per dimensione e territorio.
2. Squadre miste dell'Ispettorato della Ragioneria generale (servizi ispettivi di finanza pubblica) e dell'ANAC controllano **sul posto** un campione di spese e di gare. Il rapporto è **pubblicato entro 90 giorni**, con le osservazioni dell'ente.
3. Gli errori in buona fede portano a un **piano di correzione** e al supporto delle squadre tecniche (09-C3), non a sanzioni; i fatti gravi vanno a Corte dei conti e procura, come oggi. Un gruppo di controllo non sorteggiato permette di **misurare l'effetto**.

### Varianti
| Variante | Contenuto | Intensità | Costo a regime | Strumento |
|---|---|---|---|---|
| **PIENA** | 300 enti l'anno; circa 80 ispettori più analisi, valutazione e sistemi; rapporti pubblici; valutazione controfattuale a 3 anni; nel 2027-29 una parte del costo sugli audit di progetti cofinanziati è a carico dell'assistenza tecnica della coesione | 1 | 0,010 dal 2028 | disegno di legge |
| **ESSENZIALE** | 150 enti l'anno, stessa procedura | 0,5 | 0,005 dal 2028 | disegno di legge |
| **PILOTA** | Due tornate da 40 enti in 4 Regioni (almeno due del Mezzogiorno), con valutazione rigorosa prima di estendere | 0,15 | 0,0015 | decreto MEF + protocollo ANAC |

### Articolato essenziale
**Disegno di legge "Verifiche a sorte sulla spesa pubblica"**

**Art. 1 (Sorteggio).** 1. Ogni anno il Ministero dell'economia e delle finanze, d'intesa con l'Autorità nazionale anticorruzione, estrae a sorte, con procedura pubblica e verificabile, [300 / 150] enti tra le amministrazioni e le società da esse controllate che hanno speso nei due anni precedenti risorse del Piano nazionale di ripresa e resilienza, dei fondi di coesione o per investimenti statali. 2. L'estrazione è stratificata per dimensione e territorio secondo un algoritmo pubblicato. Ogni ente può essere estratto di nuovo. 3. Per le Regioni e i loro enti la verifica riguarda solo la spesa di risorse statali e dell'Unione europea, salvo intesa in Conferenza Stato-Regioni per estenderla; per le Regioni a statuto speciale si provvede con accordi o norme di attuazione.

**Art. 2 (Verifica).** 1. Le verifiche sono svolte entro sei mesi dall'estrazione dai servizi ispettivi di finanza pubblica della Ragioneria generale dello Stato, con personale dell'Autorità per i contratti pubblici. 2. Le verifiche riguardano la regolarità della spesa e delle procedure di affidamento su un campione di atti. 3. Le verifiche non riguardano persone fisiche in quanto tali né l'opportunità delle scelte discrezionali. 4. Le verifiche sono coordinate con le autorità di audit dei programmi cofinanziati, che ne ricevono gli esiti; non si ripetono controlli già svolti sullo stesso campione di atti nello stesso anno.

**Art. 3 (Rapporto ed esiti).** 1. Il rapporto è pubblicato entro novanta giorni dalla conclusione della verifica, con le osservazioni dell'ente e senza dati personali. 2. Per le irregolarità non dolose l'ente adotta un piano di correzione, con il supporto previsto dalla legge di attuazione della proposta 09-C3. 3. Restano fermi gli obblighi di denuncia alla Corte dei conti e all'autorità giudiziaria.

**Art. 4 (Valutazione).** Ogni tre anni l'Istituto nazionale di statistica e università scelte con procedura pubblica valutano l'effetto delle verifiche confrontando gli enti estratti con quelli non estratti, e ne riferiscono alle Camere.

**Art. 5 (Copertura).** Agli oneri, pari a 4 milioni di euro per il 2027 e a [10 / 5] milioni annui dal 2028, si provvede: per gli anni 2027-2029, nel limite di 4 milioni annui, a valere sulle risorse di assistenza tecnica dei programmi della politica di coesione 2021-2027, per le verifiche su progetti cofinanziati; per la parte restante, mediante riduzione delle spese di funzionamento del Ministero dell'economia e delle finanze.

### Chi ne è toccato
Circa 300 enti l'anno (su oltre 8.000 Comuni e migliaia di altri enti); i loro uffici per qualche settimana. I cittadini e i consigli locali, che ricevono un rapporto pubblico sull'uso dei fondi.

### Rischi e mitigazione
- **"Paura della firma" e burocrazia difensiva**: l'audit guarda a processi e spese, non alle persone; gli errori in buona fede portano a correzione e supporto, non a sanzioni; il rapporto distingue errori formali e fatti gravi.
- **Gogna sui piccoli Comuni**: avvertenze nel rapporto, diritto di replica, confronto con enti simili.
- **Qualità degli ispettori**: formazione comune RGS-ANAC; metodo pubblicato.
- **Coerenza con la L. 1/2026 sulla Corte dei conti**: la proposta non tocca la responsabilità erariale; aggiunge solo informazione.
- **Autonomia regionale e doppi controlli**: per le Regioni solo risorse statali e UE, salvo intesa; coordinamento con le autorità di audit della coesione; l'uso dell'assistenza tecnica per pagare gli audit va verificato programma per programma con le autorità di gestione.

### Indicatori
| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Enti verificati a sorte ogni anno | 0 | 300 | 300 |
| Rapporti pubblicati entro 90 giorni | n.d. | 90% | 95% |
| Irregolarità di spesa negli enti estratti una seconda volta, rispetto alla prima | n.d. | misurata | in calo, con stima controfattuale |
| Piani di correzione completati entro 12 mesi | n.d. | 70% | 85% |

---

## 07-C7 — Direttiva anticorruzione recepita bene, reato stretto e tutele contro la "paura della firma", sostegno a chi segnala

### Problema in un dato
La direttiva (UE) 2026/1021 (29/4/2026, pubblicata l'11/5/2026, verificata su EUR-Lex) va recepita entro l'**1/6/2028** (l'1/6/2029 per l'art. 20 par. 5 e l'art. 21). All'**art. 7** chiede di punire l'**esercizio illecito di funzioni pubbliche** ("almeno determinate violazioni gravi della legge", se intenzionali); all'art. 6 un **traffico di influenze** più ampio di quello lasciato dalla L. 114/2024; chiede inoltre sanzioni alle imprese fino al 5% del fatturato e termini minimi di prescrizione. La Corte costituzionale ha dichiarato legittima l'abrogazione dell'abuso d'ufficio, ma ha parlato di "indubbi vuoti di tutela" (sent. 95/2025) e ha ricordato che reintrodurre o no una fattispecie è una scelta del legislatore. Sulle segnalazioni: nel 2025 sono arrivate all'ANAC 1.931 segnalazioni (+40% circa), ma il **55% è stato giudicato inammissibile o archiviato** (Rapporto Stato di diritto 2026, p. 12).

### Evidenze
- Sulla portata dell'obbligo i giuristi sono divisi: per alcuni la direttiva impone una nuova fattispecie vicina all'abuso d'ufficio, per altri no (sintesi in `anticorruzione_diagnosi.md`, sezione 2). La direttiva non fissa "categorie minime" di funzionari: permette di limitare il reato alle categorie scelte dal legislatore nazionale.
- Il timore che il penale paralizzi l'amministrazione ("paura della firma") è reale: l'abrogazione dell'abuso d'ufficio è stata motivata con il forte scarto tra procedimenti aperti e condanne (diagnosi, sezione 5; serie storica del Ministero della giustizia da recuperare). Il rimedio è scrivere un reato che colpisca solo l'abuso **voluto** di regole **precise**.
- Nelle frodi societarie USA gli incentivi economici aumentano le segnalazioni utili (Dyck, Morse, Zingales, 2010), ma i programmi a premio funzionano solo con filtri severi sulla qualità delle segnalazioni.
- Recepire per tempo evita una procedura di infrazione.

### Soluzione in 3 righe
1. Recepire la direttiva **entro il 2027**, con una legge di delegazione europea che scrive il nuovo reato in modo **tassativo**: solo **dolo intenzionale**, solo violazioni di regole precise previste dalla legge, mai la discrezionalità né la mera illegittimità; una serie di **tutele contro la "paura della firma"**; nessuna applicazione al passato.
2. Accanto al penale, una **via amministrativa** per le violazioni meno gravi delle regole di imparzialità (sanzioni ANAC e disciplinari), **coordinata con il penale** per non punire due volte lo stesso fatto.
3. Rafforzare chi segnala: **sportello di supporto** e fondo per l'assistenza legale a chi subisce ritorsioni; **premio** per i segnalanti privati, pagato solo sulle somme recuperate e con **filtri contro le segnalazioni opportunistiche**.

### Varianti
| Variante | Contenuto | Intensità | Costo a regime | Strumento |
|---|---|---|---|---|
| **PIENA** (scelta di chi guida il progetto) | Recepimento entro il 2027; reato tassativo di esercizio illecito di funzioni pubbliche (art. 7 della direttiva) per i funzionari con poteri su appalti, concorsi, autorizzazioni ed erogazioni: solo dolo intenzionale, solo violazione di regole di condotta specifiche previste dalla legge o da atti con forza di legge, senza margini di discrezionalità, con vantaggio patrimoniale ingiusto o danno ingiusto voluti; clausola che esclude la rilevanza penale della mera illegittimità e delle scelte discrezionali, anche tecniche; esclusione del dolo per chi segue un parere scritto preventivo; nessuna sospensione automatica dall'incarico per la sola indagine; nessuna retroattività; ne bis in idem tra penale, sanzioni ANAC e disciplinari; traffico di influenze allineato all'art. 6; sanzioni d.lgs. 231/2001 fino ai massimi della direttiva; verifica della prescrizione; via amministrativa ANAC per le violazioni minori; sportello e fondo per i segnalanti; premio dal 5 al 15% delle somme recuperate in via definitiva, con tetto e filtri; monitoraggio annuale e revisione a 3 anni | 1 | 0,006 dal 2028 | legge di delegazione europea + decreto legislativo |
| **ESSENZIALE** | Recepimento entro la scadenza (1/6/2028) del contenuto obbligatorio, con il reato di esercizio illecito di funzioni limitato a categorie di funzionari indicate dalla legge (la direttiva lo permette); stesse garanzie di formulazione tassativa della PIENA; traffico di influenze e 231 allineati; sportello per i segnalanti; niente premio | 0,55 | 0,002 dal 2028 | legge di delegazione europea approvata nel 2027 + decreto legislativo entro l'1/6/2028 |
| **ZERO** | Recepimento senza nuova fattispecie penale, sostenendo che le norme vigenti (peculato per distrazione, corruzione, falso) bastano; solo misure amministrative e disciplinari e allineamento delle sanzioni alle imprese. **Rischio concreto di procedura di infrazione** sull'art. 7 | 0,2 | 0,0005 | decreto legislativo |

**Scelta di chi guida il progetto (16/11/2026): variante PIENA**, "reato stretto più tutele". Le varianti ESSENZIALE e ZERO restano nel file solo come confronto; nell'ottimizzatore va forzata la PIENA (`--forza 07-C7:PIENA`).

**Tutele aggiunte confermate (16/11/2026).** Chi guida il progetto ha confermato il 16/11/2026 le due tutele aggiunte alla PIENA: **non risponde del reato chi segue un parere scritto chiesto prima dell'atto** (tutela 4, criterio c) e **nessuna sospensione automatica dall'incarico per la sola indagine** (tutela 6, criterio d).

### Tutele contro la "paura della firma" (PIENA)
Sono il cuore della scelta. Ognuna risponde a un timore preciso di chi firma.
1. **Che cosa è reato.** Solo la violazione di una regola di condotta **specifica**, scritta in una legge o in un atto con forza di legge (non in circolari, linee guida o regolamenti), da cui **non resta alcun margine di discrezionalità**.
2. **Con quale intenzione.** Solo **dolo intenzionale**: il vantaggio o il danno ingiusto devono essere lo **scopo** dell'atto, non una conseguenza prevista o accettata. Niente dolo eventuale, niente colpa.
3. **Che cosa non è reato.** Una clausola espressa esclude la rilevanza penale della **mera illegittimità** dell'atto, delle **scelte discrezionali** (anche tecniche) e dell'**interpretazione** di norme incerte.
4. **Chi segue un parere è protetto.** Non c'è dolo intenzionale se il funzionario ha agito in conformità a un **parere scritto preventivo** dell'ANAC (anche in precontenzioso), dell'Avvocatura dello Stato o dell'ufficio legale dell'ente, chiesto prima dell'atto e senza aver nascosto fatti rilevanti.
5. **Chi è coperto.** Solo i pubblici ufficiali con poteri su contratti, concorsi, autorizzazioni ed erogazioni; non tutta la PA.
6. **Niente effetti automatici dell'indagine.** La nuova fattispecie non entra tra quelli che comportano sospensione o decadenza automatica dall'incarico prima di una condanna (coordinamento con il d.lgs. 235/2012).
7. **Nessuna retroattività.** Il reato si applica solo ai fatti commessi dopo l'entrata in vigore (art. 25 Cost., art. 2 c.p.).
8. **Ne bis in idem.** Le sanzioni amministrative ANAC si applicano solo ai fatti che **non** costituiscono reato; se per lo stesso fatto c'è un procedimento penale, il procedimento ANAC è sospeso e la sanzione disciplinare tiene conto di quella penale (art. 4 Prot. 7 CEDU; art. 50 Carta UE).
9. **Il penale resta per i casi gravi.** Le violazioni minori dell'imparzialità vanno per la via amministrativa e disciplinare.
10. **Si misura e si corregge.** Ogni anno il Ministero della giustizia pubblica iscrizioni, archiviazioni, rinvii a giudizio e condanne per la nuova fattispecie; dopo 3 anni una valutazione indipendente propone correzioni se le indagini senza esito sono troppe.
11. **Aiuto a decidere bene.** PNA, formazione e squadre tecniche (09-C3) per gli enti piccoli.

### Premio ai segnalanti: filtri contro le segnalazioni opportunistiche (PIENA)
Rilievo dei valutatori: il premio può gonfiare segnalazioni inutili e il carico dell'ANAC. Per questo il premio spetta solo se:
1. la segnalazione porta **informazioni originali**, non già note all'amministrazione, all'autorità giudiziaria o pubbliche (stampa, atti), ed è **documentata** fin dall'inizio;
2. il segnalante **non è tenuto all'obbligo di denuncia** e non ha funzioni di controllo sull'atto segnalato;
3. il segnalante **non ha promosso o organizzato** l'illecito (chi vi ha solo partecipato può avere un premio ridotto);
4. le somme sono **recuperate in via definitiva** (sentenza o atto non più impugnabile), e il premio si paga solo con quelle;
5. il premio è tra il 5% e il 15%, con un **tetto** (ad esempio 1 mln € per caso, da fissare nel decreto), deciso da una commissione ANAC con motivazione, e si riduce se il segnalante ha ritardato la segnalazione;
6. le segnalazioni **anonime** non danno premio finché il segnalante non si identifica all'ANAC (che lo tutela come oggi);
7. chi fa una segnalazione **falsa** o in mala fede perde ogni premio, paga le sanzioni del d.lgs. 24/2023 e rimborsa i costi;
8. ogni anno l'ANAC pubblica quante segnalazioni con richiesta di premio arrivano, quante sono ammesse e quanto si recupera; se le inammissibili superano la soglia fissata, i criteri si rivedono.

### Articolato essenziale
**Legge di delegazione europea, articolo "Recepimento della direttiva (UE) 2026/1021"**

**Art. 1 (Principi e criteri direttivi).** Nell'esercizio della delega il Governo osserva, oltre ai principi generali, i seguenti criteri:
a) introdurre, in attuazione dell'articolo 7 della direttiva, il reato di esercizio illecito di funzioni pubbliche, punibile solo a titolo di dolo intenzionale, commesso dal pubblico ufficiale che, nell'esercizio di poteri in materia di contratti pubblici, concorsi, autorizzazioni ed erogazioni, in violazione di specifiche regole di condotta espressamente previste dalla legge o da atti aventi forza di legge e dalle quali non residuino margini di discrezionalità, intenzionalmente procura a sé o ad altri un vantaggio patrimoniale ingiusto o arreca ad altri un danno ingiusto [ESSENZIALE: per le categorie di funzionari indicate dalla legge; ZERO: criterio non previsto];
b) escludere espressamente la rilevanza penale della mera illegittimità dell'atto, delle scelte discrezionali, anche tecniche, e dell'interpretazione di disposizioni incerte;
c) escludere il dolo intenzionale quando il pubblico ufficiale ha agito in conformità a un parere scritto dell'Autorità nazionale anticorruzione, dell'Avvocatura dello Stato o dell'ufficio legale dell'amministrazione, richiesto prima dell'atto sulla base di una rappresentazione completa dei fatti;
d) escludere il nuovo reato dai casi di sospensione e decadenza di diritto dalle cariche anteriori alla condanna, coordinando il decreto legislativo 31 dicembre 2012, n. 235;
e) prevedere che le nuove disposizioni penali si applichino solo ai fatti commessi dopo la loro entrata in vigore;
f) adeguare l'articolo 346-bis del codice penale alla definizione di traffico di influenze dell'articolo 6 della direttiva;
g) adeguare le sanzioni del decreto legislativo 8 giugno 2001, n. 231, ai massimi previsti dalla direttiva, compresa l'esclusione dai finanziamenti pubblici;
h) verificare e adeguare i termini di prescrizione dei reati previsti dalla direttiva;
i) prevedere sanzioni amministrative, irrogate dall'Autorità nazionale anticorruzione, per la violazione degli obblighi di astensione e imparzialità che non costituisce reato, con sospensione del procedimento amministrativo in pendenza di procedimento penale per lo stesso fatto e coordinamento con le sanzioni disciplinari, nel rispetto del divieto di doppio giudizio;
l) istituire presso l'Autorità uno sportello di supporto alle persone segnalanti e un fondo per l'assistenza legale a chi subisce ritorsioni accertate ai sensi del decreto legislativo 10 marzo 2023, n. 24 [PIENA e ESSENZIALE];
m) [solo PIENA] riconoscere alla persona segnalante identificata, non tenuta all'obbligo di denuncia, priva di funzioni di controllo sull'atto e che non abbia promosso o organizzato l'illecito, una quota compresa tra il 5 e il 15 per cento delle somme recuperate in via definitiva grazie a informazioni originali e documentate, entro un tetto per caso, con decisione motivata dell'Autorità, a valere esclusivamente sulle somme recuperate; prevedere la perdita del premio, le sanzioni e il rimborso dei costi in caso di segnalazione falsa o in mala fede;
n) prevedere la pubblicazione annuale dei dati sui procedimenti per il reato di cui alla lettera a) e sulle segnalazioni con richiesta di premio, e una valutazione indipendente dopo tre anni;
o) predisporre una tabella di concordanza articolo per articolo con la direttiva, comprese prescrizione e sanzioni alle persone giuridiche.

**Art. 2 (Termini).** Il decreto legislativo è adottato entro il 31 dicembre 2027 e comunque non oltre il 1° giugno 2028.

**Art. 3 (Copertura).** Agli oneri, pari a 1 milione di euro per il 2027 e a [6 / 2 / 0,5] milioni annui dal 2028, si provvede mediante riallocazione nel bilancio dell'Autorità nazionale anticorruzione e nello stato di previsione del Ministero della giustizia. Le quote di cui alla lettera m) sono pagate solo sulle somme effettivamente recuperate e non costituiscono onere aggiuntivo.

### Chi ne è toccato
Pubblici ufficiali con poteri su appalti, concorsi, autorizzazioni ed erogazioni (nuova fattispecie, solo per violazioni volute di regole precise, con più tutele di oggi per chi decide in buona fede); imprese (sanzioni più alte, programmi di compliance riconosciuti); persone che segnalano (più tutela, premio solo per informazioni utili).

### Rischi e mitigazione
- **"Paura della firma" e burocrazia difensiva** (rilievo dei tre valutatori): le undici tutele sopra; in particolare dolo intenzionale, regole di legge senza discrezionalità, protezione di chi segue un parere, nessun effetto automatico dell'indagine, monitoraggio e revisione a 3 anni.
- **Determinatezza e Costituzione** (art. 25 Cost.): formula tassativa, con regole "previste dalla legge o da atti aventi forza di legge". Precisazione: la sent. 8/2022 non ha giudicato la determinatezza del testo del 2020 dell'art. 323 c.p.; ha respinto la questione sul decreto-legge e dichiarato inammissibili le altre. La sent. 95/2025 lascia la scelta al legislatore.
- **Retroattività**: esclusa (criterio e).
- **Doppia punizione**: ne bis in idem tra penale, ANAC e disciplinare (criterio i).
- **Premi e segnalazioni opportunistiche**: otto filtri (informazioni originali e documentate, niente premio a chi ha obbligo di denuncia o funzioni di controllo o ha organizzato l'illecito, solo recuperi definitivi, tetto, niente anonimato per il premio, sanzioni per il falso, revisione dei criteri).
- **Carico dell'ANAC**: commissione dedicata al premio e personale aggiuntivo (costo da 0,005 a 0,006).
- **Procedura di infrazione** con la variante ZERO.

### Indicatori
| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Recepimento della direttiva 2026/1021 | non recepita | recepita entro l'1/6/2028 | nessuna procedura di infrazione |
| Segnalazioni ANAC inammissibili o archiviate | 55% (2025) | 40% | 30% |
| Segnalanti con ritorsione accertata che ricevono assistenza legale | 0 | 100% delle richieste ammissibili | 100% |
| Procedimenti per la nuova fattispecie conclusi con condanna o archiviazione motivata, rispetto ai procedimenti aperti | n.d. | dato pubblico annuale | dato pubblico annuale (misura della "paura della firma") |
| Pareri preventivi chiesti all'ANAC e agli uffici legali prima di atti a rischio | n.d. | dato pubblico | in crescita |
