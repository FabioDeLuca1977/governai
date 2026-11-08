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
2. La **completezza dei dati** diventa un obbligo misurato. Ogni ente ha un indicatore pubblico di reticenza, e determine e bandi si pubblicano in formato aperto e testuale collegati al CIG, così anche cittadini, giornalisti e RPCT possono leggerli, con l'assistenza di strumenti di AI (`trasparenza/istruzioni_lettura_atti.md`).
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
1. Ogni anno un comitato indipendente, composto da esperti designati dalla Corte dei conti, dall'ISTAT e da università, valuta la capacità predittiva degli indicatori e la quota di falsi positivi e ne riferisce alle Camere.
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
- **CIT** (+): cittadini, giornalisti e consiglieri locali possono fare domande documentate.
- **Rischio sui valori**: stigmatizzare enti piccoli o in emergenza (RIS). La mitigazione è nelle avvertenze, nel diritto di replica dell'ente e nella graduatoria per limite inferiore.

### Rischi e mitigazione
- **Gogna e falsi positivi.** Le garanzie dell'art. 3 e il diritto di replica limitano il rischio. La graduatoria usa il limite inferiore dell'intervallo, e la validazione annuale misura i falsi positivi.
- **Adattamento degli enti** (gaming): ad esempio inviti di comodo per evitare l'offerta unica. Si attenua ruotando e aggiornando gli indicatori e affiancando al cruscotto la lettura degli atti.
- **Più reticenza invece di più trasparenza.** L'indicatore di completezza è pubblico e pesa nella performance dei dirigenti.
- **Carico per i piccoli comuni.** La trasmissione testuale avviene in automatico dalle piattaforme certificate; c'è un raccordo con i pool tecnici di 09-C3.
