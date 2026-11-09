# GovernAI · Architettura dell'informazione

*Versione 1.0, 8 novembre 2026. Presuppone `01_brief.md`.*

## 1. La nuova navigazione in una riga

```
[GovernAI]   Oggi · Programma · Governo · Dati · Controlli        [Cerca]  Metodo  [Partecipa]
```

- **5 voci principali**, identiche su desktop (barra in alto) e telefono (barra in basso, con icona e parola).
- **3 elementi di servizio** sempre visibili: *Cerca*, *Metodo* (come funziona), *Partecipa* (pulsante primario).
- Ogni voce principale risponde a **una domanda** che si fa chi visita il sito:

| Voce | Domanda a cui risponde | Icona (Lucide) |
|---|---|---|
| **Oggi** | Che cosa succede, che cosa è cambiato? | `sunrise` |
| **Programma** | Che cosa propone GovernAI, quanto costa, chi paga? | `list-checks` |
| **Governo** | Che cosa ha deciso il governo ombra e perché? | `users-round` (non `landmark`: niente edifici del potere) |
| **Dati** | Come sta l'Italia secondo i dati ufficiali? | `chart-line` |
| **Controlli** | Rispetta Costituzione e regole europee? Chi controlla l'AI? | `shield-check` |

## 2. Dalle 11 voci attuali alle 5 nuove

Il menu attuale ha 11 voci allo stesso livello (Il progetto, Cruscotto, Programma, Governo, Valori, Obiettivi, Analisi, Coperture, Bollettini, Integrità, Metodo). Su telefono vanno a capo in tre righe e non dicono che cosa è importante. Regola seguita: **raggruppare per domanda di chi visita, non per cartella del repository.**

| Voce attuale | Dove va | Perché |
|---|---|---|
| Il progetto | **Oggi** (in alto: che cos'è, in 3 righe) + **Metodo → Come funziona** | La home deve servire chi arriva per la prima volta *e* chi torna ogni giorno: presentazione breve sopra, novità del giorno sotto |
| Cruscotto | **Dati → Indicatori** (e sintesi in **Oggi**) | "Cruscotto" è gergo; "Dati" è la parola che le persone usano |
| Programma | **Programma → Proposte** | Resta, diventa la sezione centrale |
| Coperture | **Programma → Come si paga** | Chi paga è una domanda sul programma, non un tema a parte. In ogni scheda c'è anche il blocco *Costi e coperture* |
| Valori (simulatore) | **Programma → I tuoi valori** | Il simulatore riordina le proposte: vive accanto all'elenco che modifica. La *Carta* (testo) va in **Metodo** |
| Governo | **Governo** | Resta, riorganizzato per sedute, decisioni, mandati, credibilità |
| Obiettivi | **Dati → Obiettivi e risultati** (e in ogni scheda) | Sono indicatori misurati: stanno con i dati. Nella scheda si vedono gli obiettivi di quella proposta |
| Bollettini | **Dati → Diario quotidiano** | È lo storico giornaliero dei dati; la nota del giorno compare in **Oggi** |
| Analisi | **Partecipa → Richieste e analisi** | Nascono da una richiesta della cittadinanza: si trovano dove si fa la richiesta |
| Integrità | **Controlli → Integrità** | È un controllo, come Costituzione ed Europa: "anche l'AI è controllata" |
| Metodo | **Metodo** (servizio, in testata e piè di pagina) | Serve a chi vuole capire o verificare, non a ogni visita: non occupa una voce principale |
| *(nuova)* Europa | **Controlli → Europa** | Obblighi UE, infrazioni e semestre europeo sono vincoli da rispettare, come la Costituzione |
| *(nuova)* Costituzione | **Controlli → Costituzione** | Controllo di costituzionalità di proposte, leggi e manovre |

**Perché 5 e non 6 voci.** Con Europa e Costituzione come voci autonome si arriverebbe a 7, oltre il limite di una barra di navigazione mobile leggibile (5 voci da 64 px a 375 px di larghezza). Riunirle in **Controlli** ha anche un senso di contenuto: il README dice "Prima i vincoli, poi i valori. Costituzione e vincolo di bilancio non si pesano: si rispettano". *Controlli* è la casa dei vincoli che non si pesano.

**Perché "Controlli" e non "Garanzie" o "Regole".** *Garanzie* in Italia richiama il dibattito garantisti/giustizialisti, che ha una connotazione di schieramento. *Regole* si confonde con il *Regolamento* del Consiglio. *Controlli* è un verbo d'azione neutro e corrisponde a ciò che il sistema fa davvero (controllo giuridico, controllo di integrità).

**Perché "Oggi" e non "Home".** Dice che il contenuto cambia ogni giorno: è il motivo per tornare.

## 3. Mappa dell'app

```
GovernAI
├── Oggi  (/)
│   ├── Che cos'è, in 3 righe + "L'AI propone e verifica. Le persone decidono."
│   ├── Il giorno in 4 numeri (programma, allerte, ultima seduta, scadenze UE)
│   ├── Allerte attive
│   ├── Ultima seduta del Consiglio (sintesi)
│   ├── Prossime scadenze (UE, mandati, semestre)
│   ├── Proposte per tema (9 aree)
│   └── Fiducia verificabile (catena integra, cifre verificate)
│
├── Programma  (/programma)
│   ├── Proposte            /programma                elenco filtrabile (tema, classe, inclusa, controlli)
│   │   └── Scheda          /programma/01-P3          ← OGGETTO CENTRALE
│   ├── Come si paga        /programma/coperture      scenari + 63 coperture
│   ├── I tuoi valori       /programma/valori         simulatore dei pesi
│   └── Confronti           /programma/confronti      altri Paesi; governo e partiti (318 misure)
│
├── Governo  (/governo)          banner fisso "Governo ombra · simulazione"
│   ├── Sedute              /governo                  timeline delle sedute
│   │   └── Verbale         /governo/sedute/2026-11-08-1-conti-in-ordine
│   ├── Decisioni in vigore /governo/decisioni        stato e verifica quotidiana
│   ├── Mandati             /governo/mandati          19 aperti, con scadenza
│   ├── Credibilità         /governo/credibilita      previsioni e punteggio di Brier
│   └── Chi siede e regole  /governo/regolamento      ruoli, 11 regole, 19 esperti
│
├── Dati  (/dati)
│   ├── Indicatori          /dati                     14 indicatori con trend
│   │   └── Indicatore      /dati/inflazione          serie, fonte, proposte collegate
│   ├── Allerte             /dati/allerte
│   ├── Obiettivi e risultati /dati/obiettivi         158 obiettivi misurabili
│   └── Diario quotidiano   /dati/diario              bollettini per data
│
├── Controlli  (/controlli)      hub con tre schede
│   ├── Costituzione        /controlli/costituzione
│   │   ├── Leggi e manovre /controlli/costituzione/AC3174
│   │   └── Proposte        /controlli/costituzione/proposte
│   ├── Europa              /controlli/europa
│   │   ├── Scadenze        /controlli/europa/scadenze      143 direttive
│   │   ├── Infrazioni      /controlli/europa/infrazioni    84 procedure
│   │   ├── Semestre europeo /controlli/europa/semestre
│   │   └── Novità          /controlli/europa/novita        atti degli ultimi 30 giorni
│   └── Integrità           /controlli/integrita            catena di impronte
│
├── Metodo  (/metodo)            servizio
│   ├── Come funziona (7 passi)
│   ├── Carta dei valori    /metodo/carta#FUT
│   ├── Documenti           programma, metodo, quadro giuridico, sistema, legislazione, appalti
│   ├── Limiti dichiarati
│   └── Glossario e sigle   /metodo/glossario
│
├── Partecipa  (/partecipa)      servizio, pulsante primario
│   ├── Proponi un'idea               (issue GitHub, modello "analisi")
│   ├── Fai una domanda al Consiglio  (issue GitHub, modello "consiglio")
│   ├── Segnala un errore             (su qualunque pagina, link contestuale)
│   ├── Richieste e analisi           /partecipa/analisi
│   └── Per i membri del progetto     convoca il Consiglio, riesame, richiesta diretta
│
└── Cerca  (overlay, scorciatoia "/")
```

## 4. Navigazione secondaria

- **Sotto-navigazione a schede** in testa a ogni sezione (es. *Proposte · Come si paga · I tuoi valori · Confronti*). Su telefono è una fila orizzontale scorrevole con l'ultima scheda visibile a metà, così si capisce che si scorre.
- **Briciole di pane** solo dal secondo livello in giù: `Programma › Economia, Imprese, Turismo › IVA in tempo reale`. Su telefono si riducono a "‹ Programma".
- **Indice della pagina** (sommario a lato su desktop, menu "In questa pagina" su telefono) nelle pagine lunghe: scheda della proposta, verbale, Carta.
- **Collegamenti trasversali** in un blocco fisso a fine pagina, *Collegato a*, con al massimo 6 elementi tipizzati (icona + tipo + titolo).
- **Piè di pagina**: Metodo, Integrità, Glossario, Documenti, Repository, Licenze (codice e contenuti), Segnala un errore, avviso di prototipo, data e ora dell'ultimo aggiornamento.

## 5. Ricerca

- **Una sola casella** in testata (icona lente su telefono), scorciatoia da tastiera `/`.
- **Indice lato client** costruito da `data.js`: proposte (id, titolo, area, testo della scheda), coperture, indicatori, sedute e decisioni, mandati, atti UE (CELEX, titolo), infrazioni (numero, oggetto), norme citate (es. "art. 81"), voci del glossario.
- **Riconosce i codici**: `01-P3`, `M011`, `2026_4015`, `32024L1260`, `A.C. 3174`, `art. 53` portano direttamente all'oggetto.
- **Sinonimi del linguaggio comune** → termini del programma: tasse → fisco, IRPEF, IVA; asili → nido; pensioni → previdenza; bollette → energia; medico → medicina generale; carceri → pena; immigrazione → flussi migratori.
- **Risultati raggruppati per tipo** (Proposte, Decisioni, Dati, Europa, Costituzione, Metodo), 3 per gruppo con "vedi tutti", ognuno con chip di stato.
- **Stato vuoto utile**: "Nessun risultato per 'reddito di base'. Forse cercavi *Reddito di inclusione universale (02-C4)*? Oppure proponi l'idea →".

## 6. Il modello degli oggetti e i collegamenti

La **Proposta** è il centro (principio 4 del brief). Ogni altro oggetto si collega a una o più proposte, e ogni proposta mostra tutti i suoi collegamenti.

```
                              ┌──────────────────┐
                              │   VALORE (10)    │  Metodo › Carta
                              │ es. FUT Futuro   │
                              └────────┬─────────┘
                       punteggi panel  │  linee rosse
                                       ▼
┌────────────────┐  finanziata da ┌──────────────────────┐ decisa in  ┌───────────────────┐
│ COPERTURA (63) │◄──────────────►│  PROPOSTA (62)       │◄──────────►│ SEDUTA / DECISIONE│
│ Programma ›    │                │  es. 01-P3 IVA in    │  mandati   │ Governo › verbale │
│ Come si paga   │                │  tempo reale         │◄──────────►│ MANDATO (M001…)   │
└────────────────┘                └──┬───────┬───────┬───┘            └─────────┬─────────┘
                                     │       │       │                          │ previsioni
                 controllo COS       │       │ UE    │ obiettivi                ▼
            ┌────────────────────────┘       │       └──────────┐     ┌───────────────────┐
            ▼                                ▼                  ▼     │ CREDIBILITÀ       │
┌──────────────────────┐  ┌──────────────────────────┐ ┌──────────────┴─────┐ (Brier)    │
│ COSTITUZIONE         │  │ EUROPA                   │ │ DATI               │            │
│ esame di proposte,   │  │ scadenza (es. Dir. 2025/ │ │ indicatore,        │◄───────────┘
│ leggi, manovre       │  │ 516 ViDA, 31/12/2026),   │ │ obiettivo, allerta │ verificate sui dati
│ (es. A.C. 3174)      │  │ infrazione, semestre     │ └─────────┬──────────┘
└──────────────────────┘  └──────────────────────────┘           │ allerta → convoca
            ▲                         ▲                          ▼
            └──────── tutto registrato nella ── INTEGRITÀ (catena di impronte, 9 anelli)
                                                       ▲
                                    METODO spiega e documenta ogni passaggio
```

### Regole di collegamento (valgono per tutte le schermate)

| Da | A | Come appare |
|---|---|---|
| Proposta | Decisioni del Consiglio | Blocco *Che cosa ha deciso il governo ombra*: ultima decisione, variante, regola, link al verbale |
| Proposta | Costituzione / Europa | Blocco *Controlli*: un chip di gravità per ambito (Fiscale, Costituzionale, Europeo) + scadenze UE collegate |
| Proposta | Dati | Blocco *Obiettivi*: obiettivi con base, ultimo dato, traguardo; indicatori di contesto |
| Proposta | Coperture | Blocco *Costi e coperture*: costo per variante, fondi, chi paga |
| Seduta | Proposte | Ogni riga delle Decisioni porta alla scheda |
| Allerta (Dati) | Proposte | Chip "Priorità: 02-C1, 02-C4, 04-P2, 04-P3" e "Sospesa: 07-C5" |
| Scadenza UE | Proposte, esperti | "Collegata a 01-P3, 01-P10" |
| Infrazione | Aree, proposte | Area di governo + proposte collegate |
| Esame di costituzionalità | Articoli, sentenze | Articoli della Costituzione e pronunce della Corte (verificate sui dati aperti della Corte) |
| Ogni pagina | Integrità | Riga in fondo: "Dati del 8/11/2026 · anello n. 8 · impronta f9ecf15b…" |
| Ogni sigla | Glossario | Prima occorrenza sottolineata a puntini, definizione al tocco |

## 7. Percorsi di visita

### 7.1 Persona curiosa — "Che cosa propone sugli asili?" (telefono, 2 minuti)

```
Link condiviso / ricerca web
  → Oggi: legge "Che cos'è" (3 righe) e vede "Proposte per tema"
  → tocca "Lavoro, Welfare, Famiglia"
  → Programma filtrato: 6 proposte, card con chip
  → tocca "Nido esigibile + congedo paterno" (02-C2, Nucleo robusto)
  → Scheda, livello "In breve": problema in un dato, soluzione in 2 frasi,
    costo e chi paga, decisione del governo ombra (adottata, variante Essenziale)
  → (facoltativo) "Prova i tuoi valori" o "Condividi"
```
**Punti critici progettati**: tema in linguaggio comune; titolo prima del codice; *In breve* sopra la piega; condivisione con anteprima neutra (titolo + "GovernAI · simulazione").

### 7.2 Persona attiva — "Che cosa è cambiato e cosa devo fare?" (desktop, 15 minuti)

```
Oggi: blocco "Da ieri" (nuova seduta, 4 allerte attive, mandati in scadenza)
  → Governo › Mandati: filtra "in scadenza entro 60 giorni" → M003 (31/12/2026)
  → apre la seduta d'origine → sezione Mandati
  → Decisioni in vigore: esito della verifica quotidiana ("confermata")
  → "Chiedi un riesame" (membri) oppure Partecipa › Domanda al Consiglio
  → Partecipa › Richieste: segue lo stato (in revisione → in coda → analizzata)
```
**Punti critici**: un elenco "Da ieri" calcolato confrontando le date; stati di una richiesta chiari; azioni per i membri visibili ma distinte da quelle pubbliche (pulsante secondario con etichetta "membri del progetto").

### 7.3 Pubblico esperto o giornalistico — "Da dove viene quel numero? Regge giuridicamente?" (desktop, 30 minuti)

```
Cerca "IVA" → 01-P3 IVA in tempo reale
  → Scheda › "Problema in un dato": 34,4 mld di gap IVA nel 2023 [Verificato su fonte]
      → tocca il badge → fonte: MEF, Relazione evasione 2026, tab. III.1 + link
  → Scheda › Controlli: Costituzionale "Condizionato", Europeo "Condizionato",
      variante Piena "Richiede notifica" → apre norme, motivazione, condizioni, fonti
  → Collegato a: scadenza UE Dir. (UE) 2025/516 (ViDA), termine 31/12/2026
      → Controlli › Europa › scadenza
  → Collegato a: seduta "Conti in ordine…" → deroga su 01-P3 ("non si scrive a
      bilancio una spesa per una misura che può non partire")
  → Metodo › Integrità: anello n. 8, impronta, comando per riverificare
  → "Copia link permanente" / "Scarica dati (CSV)"
```
**Punti critici**: badge di verifica cliccabili; link permanenti per citazione; esportazione CSV per tabelle; versioni e data visibili.

### 7.4 Percorso trasversale — dal dato alla decisione

```
Dati › Inflazione 5,6% (ottobre 2026, provvisorio) ▲ +1,4
  → Allerta "Inflazione sopra il 3%" → Priorità: 02-C1, 02-C4, 04-P2, 04-P3
  → Governo: seduta convocata per l'allerta → Decisioni su quelle proposte
  → Governo › Credibilità: previsioni registrate (57 nella seduta), verificate alla scadenza
```

## 8. Come si collegano le sei aree (sintesi)

| | Programma | Governo | Dati | Europa | Costituzione | Metodo |
|---|---|---|---|---|---|---|
| **Programma** | — | le proposte sono l'ordine del giorno | obiettivi misurabili per proposta | scadenze e infrazioni collegate | esito COS per proposta e variante | Carta, panel, robustezza |
| **Governo** | decide varianti, deroghe | — | le allerte convocano il Consiglio; previsioni verificate sui dati | l'esperto UE e il giurista siedono sempre | l'Ufficio legislativo blocca ciò che non è conforme | Regolamento, 11 regole |
| **Dati** | allerte cambiano il "programma del momento" | verifica quotidiana delle decisioni | — | semestre europeo: spesa netta, disavanzo | — | fonti, serie, 334 cifre verificate |
| **Europa** | vincoli e opportunità per le proposte | mandati verso la Commissione (es. M001) | regole di bilancio | — | primato e compatibilità | quadro giuridico |
| **Costituzione** | linee rosse e condizioni | rilievi formali nel verbale | — | — | — | quadro giuridico |
| **Metodo** | spiega classi e varianti | spiega ruoli | spiega fonti | spiega regole di pertinenza | spiega livelli di rischio | — |

## 9. Regole di URL e stato

- Ogni oggetto ha un **link permanente leggibile** (`/programma/01-P3`, `/governo/sedute/2026-11-08-1-conti-in-ordine#decisioni`).
- Filtri e scenario si riflettono nell'URL (`/programma?tema=02&classe=robusta&scenario=momento`), così una vista si può condividere.
- Con l'hosting statico attuale si usano gli hash (`#/programma/01-P3`); la struttura dei percorsi resta identica.
- La scheda della proposta è una **pagina**, non un cassetto laterale come oggi: si può condividere, stampare e indicizzare. Su desktop l'elenco può aprirla in un pannello affiancato, ma con URL proprio.
