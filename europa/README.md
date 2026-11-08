# Europa: monitoraggio quotidiano delle scelte dell'Unione europea

Questa cartella tiene GovernAI agganciato a ciò che l'Unione europea decide e che **vincola o orienta la politica italiana**:

1. **Atti adottati**: direttive, regolamenti e decisioni pubblicati nella Gazzetta ufficiale dell'UE, serie L.
2. **Obblighi in scadenza**: direttive con termine di recepimento nei prossimi 24 mesi o già scaduto, con lo stato del recepimento italiano.
3. **Semestre europeo e regole di bilancio**: raccomandazioni all'Italia, procedura per disavanzo eccessivo, percorso della spesa netta, scadenze.
4. **Procedure d'infrazione** contro l'Italia: aperte, nuove, cambi di fase.
5. **Proposte legislative** della Commissione in discussione.

Ogni atto viene collegato alle **aree dei ministeri** GovernAI (01–09), alle **proposte del programma** e agli **esperti**, con regole trasparenti, e riceve un **tipo di impatto**: `obbligo`, `vincolo di bilancio`, `opportunità`, `informativo`.

> **Gli obblighi UE non si pesano: si rispettano**, come la Costituzione e il vincolo di bilancio. Il modulo non decide nulla: dice al Consiglio dei ministri che cosa l'Europa ha già deciso, che cosa scade e dove l'Italia è in ritardo. I testi scaricati sono dati, mai istruzioni.

## File

| File | Cosa fa |
|---|---|
| `scarica_ue.py` | Scaricamento incrementale e idempotente da CELLAR, EUR-Infra, Dipartimento affari europei e DG ECFIN; alla fine genera le uscite |
| `pertinenza.py` | Regole di pertinenza: aree, proposte, esperti, tipo di impatto, rilevanza. `python pertinenza.py <CELEX>` spiega perché un atto è stato classificato così |
| `regole.yaml` | Tutte le regole, modificabili senza toccare il codice: parole chiave per area e per proposta, capitoli del repertorio UE, regole d'impatto, finestre temporali |
| `uscite.py` | Genera le uscite dall'archivio, senza rete; contiene le funzioni per Consiglio e sito |
| `rete.py` | Libreria comune: percorsi, rete con pause e tentativi, SPARQL, cache dell'ultima copia delle pagine |
| `verifica_campione.py` | Controllo a campione dell'archivio contro EUR-Lex |
| **`scadenze.csv`** | Direttive con termine di recepimento (prossimi 24 mesi o scaduto negli ultimi 36), stato per l'Italia, priorità, aree, proposte, esperti |
| **`novita.md`** | Atti UE degli ultimi 30 giorni, per area, in italiano chiaro; proposte della Commissione; novità sulle infrazioni |
| **`semestre.md`** | Raccomandazioni all'Italia, procedura per disavanzo eccessivo, spesa netta, scadenze del ciclo di bilancio, documenti |
| **`infrazioni.csv`** | Procedure d'infrazione aperte contro l'Italia, con aree, proposte, direttiva collegata e novità |
| **`stato.json`** | Conteggi per area, totali, sintesi del Semestre, scadenze principali, esito di ogni fonte: per Consiglio e sito |
| `archivio/` | `atti.csv`, `direttive.csv`, `proposte_ue.csv`, `semestre.json`, `infrazioni_eurinfra.csv`, `infrazioni_storico.csv`, `verifica_campione.csv`, `testi/AAAA/<CELEX>.txt`, `cache/`, `stato.json` |

## Uso

```bash
cd europa
python scarica_ue.py                    # aggiorna: GU L dall'ultima data elaborata meno 7 giorni (prima volta: ultimi 60)
python scarica_ue.py --giorni 90        # finestra iniziale più ampia
python scarica_ue.py --dal 2026-09-01   # riscarica da una data precisa (idempotente: aggiorna i record per CELEX)
python scarica_ue.py --senza-testi      # non scarica i testi delle direttive
python scarica_ue.py --solo-uscite      # rigenera le uscite dall'archivio, senza rete (equivale a python uscite.py)
python pertinenza.py 32026L2383         # perché questo atto è assegnato a queste aree, proposte e impatto
python verifica_campione.py             # confronto con EUR-Lex su 10 atti
```

I percorsi sono assoluti: lo script funziona da qualsiasi cartella e con `python -I`. L'ultima riga stampata riassume l'esecuzione e finisce nel registro del bollettino.

## Fonti

Provate l'8 novembre 2026 da questa macchina, senza chiavi né registrazioni.

### Usate

| Fonte | Che cosa dà | Esito della prova |
|---|---|---|
| **CELLAR, endpoint SPARQL** (`publications.europa.eu/webapi/rdf/sparql`, ontologia CDM) | Atti della GU L per data di pubblicazione (`official-journal-act_date_publication`, raccolta `OJ-L`): CELEX, ELI, tipo, date, entrata in vigore, autori, destinatari, titolo italiano, descrittori EuroVoc in italiano, voci del repertorio della legislazione UE. **Termini di recepimento** (`directive_date_transposition`) con le annotazioni che distinguono adozione e applicazione. **Misure nazionali di esecuzione notificate dall'Italia** (`measure_national_implementing`, paese `ITA`). Proposte della Commissione (`PROP_REG`, `PROP_DIR`, `PROP_DEC`). Documenti del Semestre sull'Italia | Funziona. Circa 40-60 richieste per un riscaricamento di 60 giorni, 19 per l'aggiornamento quotidiano, circa un minuto |
| **CELLAR, contenuto** (`publications.europa.eu/resource/celex/<CELEX>`, `Accept-Language: ita`) | Testo italiano (XHTML) delle direttive nuove e dell'ultima raccomandazione specifica per paese | Funziona |
| **EUR-Infra, area libera** (`eurinfra.politichecomunitarie.it/ElencoAreaLibera.aspx`, Dipartimento per gli affari europei) | Elenco completo delle procedure d'infrazione aperte: numero, oggetto, DG, materia, norme, tipo di inadempienza, fase | Funziona: 84 procedure, lo stesso numero dichiarato dalla pagina e dall'ultimo aggiornamento del Dipartimento (1° ottobre 2026) |
| **affarieuropei.gov.it**, «Stato delle infrazioni» | Sintesi degli aggiornamenti periodici (nuove procedure, aggravamenti, archiviazioni) | Funziona, ma a volte va in timeout: lo script riprova tre volte e poi usa l'ultima copia in `archivio/cache/` |
| **DG ECFIN**, pagina della procedura per disavanzo eccessivo dell'Italia | Cronologia dei passaggi della procedura in corso, con link ai documenti | Funziona |

### Scartate o non integrate

| Fonte | Perché |
|---|---|
| **Feed RSS di EUR-Lex** | Il feed provato (`display-feed.html?rssId=162`) risponde 404. I feed riportano solo le ultime voci (se un'esecuzione salta si perdono atti, come per l'RSS della GU italiana) e non danno termini di recepimento né EuroVoc. SPARQL li copre tutti |
| **Banca dati delle decisioni d'infrazione della Commissione** (`ec.europa.eu/implementing-eu-law/search-infringement-decisions/`) | Il vecchio indirizzo `infringement_decisions/index.cfm` ora reindirizza a un'applicazione Angular. La sua API interna non è documentata e ha risposto HTTP 500 (`/api/referencedata/loadAll`). Nessuna esportazione scaricabile senza interfaccia. Si usa EUR-Infra, la fonte ufficiale italiana, che riporta le stesse procedure |
| **Pagine del Semestre su commission.europa.eu / economy-finance** (indirizzi per paese) | Gli indirizzi provati rispondono 404 o reindirizzano. I documenti del Semestre si prendono da CELLAR, che è la fonte degli atti stessi |
| **Parlamento europeo, Open Data API** (`data.europarl.europa.eu/api/v2/procedures`) | Funziona (HTTP 200, JSON-LD), ma restituisce l'elenco delle procedure senza filtri utili per materia. Non integrata: le proposte arrivano da CELLAR e lo stato della procedura è linkato alla pagina «Procedura» di EUR-Lex. Integrazione possibile in futuro |
| **Osservatorio legislativo (OEIL)** e **programma di lavoro della Commissione** | Non provati in questa versione |
| **EUR-Lex, pagine web** | Usate solo per il controllo a campione (`verifica_campione.py`), non per lo scaricamento quotidiano: CELLAR è la stessa base dati in forma strutturata |

### Un'avvertenza tecnica su CELLAR

Le funzioni di aggregazione SPARQL (`MIN`, `MAX`, `SAMPLE`, `GROUP_CONCAT` con `GROUP BY`) sull'endpoint di CELLAR hanno dato **risultati diversi da un'esecuzione all'altra**, con date di altri atti: per esempio la data di notifica di una misura italiana del 10/07/2024 risultava 2026-06-15 in un'esecuzione e 2026-07-24 nella successiva. Per questo **tutte le query scaricano righe grezze e l'aggregazione si fa in Python**. Con questa scelta due riscaricamenti completi consecutivi producono archivi identici campo per campo (773 atti e 145 direttive, nessuna differenza). Le risposte con 10.000, 50.000 o 100.000 righe vengono rifiutate come probabilmente troncate; la GU L si interroga a finestre di 7 giorni.

## Che cosa viene scaricato

- **Atti della GU L** (`archivio/atti.csv`, chiave CELEX): tutti, comprese le rettifiche, con: `eli`, `tipo_codice` e `tipo`, `data_gu`, `data_atto`, `rif_gu`, `titolo` (italiano; se manca, inglese segnalato), `eurovoc`, `repertorio`, `entrata_in_vigore`, `termine_recepimento` e `termini` (tutti, con l'annotazione adozione/applicazione e l'articolo), `termine_testo` (data letta nel testo italiano della direttiva), `in_vigore`, `autori`, `destinatari`, `url_eurlex`, `testo` e le colonne di pertinenza (`aree`, `proposte`, `esperti`, `impatto`, `rilevanza`, `riguarda_italia`, `motivo`).
- **Direttive con termine** (`archivio/direttive.csv`): tutte quelle con almeno un termine di recepimento tra 36 mesi fa e 24 mesi da oggi, rifatte per intero ogni giorno, con `misure_it` (numero di misure italiane notificate), `ultima_notifica_it` ed `esempio_misura_it`.
- **Proposte della Commissione** degli ultimi 60 giorni (`archivio/proposte_ue.csv`).
- **Semestre** (`archivio/semestre.json`): documenti sull'Italia dal 2024, cronologia DG ECFIN, raccomandazioni estratte dal testo.
- **Infrazioni**: elenco EUR-Infra del giorno (`archivio/infrazioni_eurinfra.csv`) e storico (`archivio/infrazioni_storico.csv`) con prima e ultima rilevazione, cambi di fase, chiusure.
- **Testi**: solo direttive nuove e raccomandazioni specifiche per paese, per contenere il peso.

Comportamento verso i siti:
- User-Agent dichiarato;
- almeno 1 secondo tra due richieste;
- tre tentativi con attesa crescente sugli errori 429/5xx e sui timeout;
- nessun download parallelo;
- se una pagina HTML non risponde si usa l'ultima copia in `archivio/cache/` e lo si scrive nello stato;
- se CELLAR non risponde, l'errore finisce in `archivio/stato.json` e in `stato.json`, le uscite si rigenerano dall'archivio e la pipeline continua.

### Stato dell'archivio

Prima esecuzione dell'8/11/2026, finestra GU L dal 9 settembre all'8 novembre 2026 (60 giorni):

| Voce | Numero |
|---|---|
| Atti della GU L | **773**: 236 decisioni, 192 rettifiche, 158 regolamenti di esecuzione, 79 decisioni di esecuzione, 34 decisioni su atti internazionali, 23 regolamenti delegati, 18 regolamenti, 4 direttive (2 ordinarie, 1 delegata, 1 di esecuzione) e altri |
| Ultimi 30 giorni | 298 atti: 89 obblighi, 8 opportunità, 201 informativi; nessun vincolo di bilancio nella GU L (i documenti del Semestre sono in `semestre.md`) |
| Direttive monitorate per il recepimento | 145, di cui 143 in vigore con termine nella finestra |
| Proposte della Commissione (60 giorni) | 64 |
| Procedure d'infrazione aperte | 84, di cui 21 per mancato recepimento |
| Documenti del Semestre sull'Italia | 16 (dal 2024) |
| Testi | 5 (4 direttive e la raccomandazione specifica per paese 2026) |
| Peso | `archivio/` 1,5 MB; cartella intera 2 MB |

Scadenze per priorità: 23 critiche, 10 alte, 94 medie, 16 basse.

## Regole di pertinenza

Il testo su cui si cercano le parole è il titolo italiano senza l'intestazione, più i descrittori EuroVoc e le voci del repertorio. Tutte le regole sono in `regole.yaml`.

**Aree (01–09).** Si usano due criteri:
1. il capitolo o la sezione del **repertorio della legislazione UE** (per esempio 03 agricoltura → 03; 1530 protezione della salute → 06; 1320 tecnologie dell'informazione → 09; 19 spazio di libertà, sicurezza e giustizia → 07);
2. le **parole chiave** per area.

Un atto collegato a una proposta riceve anche l'area di quella proposta.

**Proposte.** Si usano:
- parole chiave per ciascuna delle 62 proposte;
- gli **atti UE citati nelle schede** del programma: se la scheda 03-P2 cita il Reg. (UE) 2024/1747, ogni atto che lo modifica o lo cita nel titolo è collegato a 03-P2. Sono 14 atti UE citati in tutto.

**Esperti.** Le `parole` di `governo/esperti.yaml`, con lo stesso criterio a parole intere di `governo/consiglio.py`. In più:
- `giurista` per gli obblighi;
- `finanza_pubblica` per i vincoli di bilancio;
- `europa_esteri` per le opportunità e per le infrazioni.

**Tipo di impatto**, valutato in quest'ordine:

| Ordine | Condizione | Impatto |
|---|---|---|
| 1 | Rettifica | informativo |
| 2 | Il titolo nomina solo altri Stati membri | informativo |
| 3 | Parole su disavanzo, spesa netta, Semestre, sorveglianza di bilancio | **vincolo di bilancio** |
| 4 | Parole su fondi, programmi, sovvenzioni (salvo «devono versare» e simili) | **opportunità** |
| 5 | Direttiva | **obbligo** (da recepire) |
| 6 | Atto di gestione corrente: autorizzazioni singole, denominazioni, dazi antidumping, misure restrittive, posizioni in organismi internazionali | informativo |
| 7 | Regolamento o decisione | **obbligo** (applicazione diretta) |
| 8 | Tutto il resto | informativo |

Le proposte della Commissione si valutano come l'atto che diventerebbero.

**Rilevanza.**
- **Alta**: direttive, atti legislativi del Parlamento e del Consiglio, atti che nominano l'Italia, vincoli di bilancio.
- **Media**: altri obblighi e opportunità con un'area assegnata.
- **Bassa**: tutto il resto.

`novita.md` elenca alta e media e conta le basse.

**Stato e priorità delle scadenze** (`scadenze.csv`):

| Stato | Significato | Priorità |
|---|---|---|
| procedura d'infrazione aperta | EUR-Infra ha una procedura che cita la direttiva | critica |
| termine scaduto, nessuna misura italiana notificata | — | critica |
| in termine, nessuna misura notificata | termine entro 6 mesi | alta |
| termine scaduto, misure notificate | la completezza **non** è verificata | media (o bassa) |
| in termine, misure già notificate | — | media o bassa |

Per lo stato «in termine, nessuna misura notificata» la priorità è media entro 12 mesi e bassa oltre.

**Termine di recepimento.** È il primo termine annotato come «adozione» che cade nella finestra; senza annotazione, il primo termine nella finestra. Le direttive con termini scaglionati li hanno tutti in `altri_termini`.

## Prova dell'8 novembre 2026

### Controllo a campione contro EUR-Lex (10 atti)

`verifica_campione.py` confronta l'archivio con la pagina «Tutte le informazioni» di EUR-Lex. Per ogni atto controlla titolo italiano, tipo, data del documento, data di pubblicazione nella GU L e termine di recepimento.

| CELEX | Tipo | Data atto | GU L | Termine (archivio) | Termine (EUR-Lex) | Esito |
|---|---|---|---|---|---|---|
| 32026L2383 | Direttiva | 2026-10-21 | 2026-11-03 | 2027-11-24 | 2027-11-24 | coincide |
| 32026L2450 | Direttiva | 2026-10-21 | 2026-10-30 | 2028-11-20 | 2028-11-20 | coincide |
| 32026L2325 | Direttiva delegata | 2026-07-10 | 2026-10-19 | 2027-01-31 | 2027-01-31 | coincide |
| 32026L2250 | Direttiva di esecuzione | 2026-10-12 | 2026-10-13 | 2027-12-31 | 2027-12-31 | coincide |
| 32024L1275 | Direttiva | 2024-04-24 | 2024-05-08 | 2025-01-01 | 2025-01-01 | coincide |
| 32024L1260 | Direttiva | 2024-04-24 | 2024-05-02 | 2026-11-23 | 2026-11-23 | coincide |
| 32025L0516 | Direttiva | 2025-03-11 | 2025-03-25 | 2026-12-31 | 2026-12-31 | coincide |
| 32026R2473 | Regolamento | 2026-10-21 | 2026-11-04 | — | — | coincide |
| 32026R2490 | Regolamento di esecuzione | 2026-11-03 | 2026-11-04 | — | — | coincide |
| 32026D2494 | Decisione | 2026-10-21 | 2026-11-05 | — | — | coincide |

**10 atti su 10 coincidono in tutti i campi.** Dettagli in `archivio/verifica_campione.csv`.

Altri controlli:
- **Termine letto nel testo.** Per le 4 direttive nuove la data della clausola «Gli Stati membri mettono in vigore / adottano e pubblicano … entro il …» coincide con il metadato di CELLAR (colonna `termine_dal_testo` di `scadenze.csv`).
- **Misure italiane notificate.** Per 3 direttive il numero coincide con la pagina «Misure nazionali di recepimento» di EUR-Lex:
  - 2024/1260: 0;
  - 2021/1883: 1;
  - 2024/1785: 1.
- **Stabilità.** Il controllo è stato ripetuto dopo il passaggio alle query senza aggregazioni (vedi l'avvertenza tecnica sopra): stesso esito.

### Che cosa è emerso

- **Semestre.** La raccomandazione del Consiglio del 10 luglio 2026 (CELEX 32026H03925) dice che, dopo la valutazione della Commissione del 3 giugno 2026, «la procedura per i disavanzi eccessivi per l'Italia è sospesa». La pagina DG ECFIN, rivista il 20 agosto 2026, la elenca ancora tra le procedure in corso. In CELLAR non c'è una decisione di abrogazione. Le raccomandazioni 2026 sono 6; la prima chiede di allineare la spesa netta al percorso correttivo del 21 gennaio 2025. L'8 ottobre 2026 la Commissione ha proposto una raccomandazione che **consente all'Italia di deviare dai tassi massimi di crescita della spesa netta** (attivazione della clausola di salvaguardia nazionale, COM(2026) 553): è in attesa del Consiglio.
- **Opportunità.** La decisione (UE) 2026/2494 mobilita il **Fondo di solidarietà dell'UE** anche per l'Italia, per la tempesta Harry del gennaio 2026.

## Limiti

- **Recepimento «notificato», non «completo».** CELLAR dice quali misure l'Italia ha notificato, non se coprono tutta la direttiva. La valutazione di completezza spetta alla Commissione e oggi è visibile solo attraverso le procedure d'infrazione per mancato o non corretto recepimento. Lo stato «scaduto, misure notificate» va quindi letto come «da verificare».
- **Termini scaglionati.** Molte direttive hanno più termini, per articolo o per fase. L'archivio sceglie il primo termine di adozione nella finestra (per la direttiva sugli edifici 2024/1275 è il 1/1/2025; quello generale, il 29/5/2026, è in `altri_termini`). Le annotazioni di CELLAR a volte mancano («non annotata»).
- **Direttive non pertinenti per l'Italia.** Alcune direttive riguardano solo alcuni Stati, oppure la Commissione invece degli Stati. Le regole non le escludono tutte.
- **Collegamento infrazioni-direttive.** Si basa sul numero della direttiva citato nell'oggetto EUR-Infra. Una procedura per «non corretto recepimento» o per un obbligo specifico rende la direttiva «critica» anche se le misure sono state notificate.
- **Le regole di pertinenza sono parole chiave.**
  - Danno falsi positivi: per esempio «adattamento ai cambiamenti climatici» tra i descrittori EuroVoc collega la direttiva sull'efficienza energetica a 03-P4.
  - Danno anche falsi negativi.
  - Ogni scelta è spiegata nella colonna `motivo` e si corregge in `regole.yaml`.
  - L'area 08 è molto frequente, perché comprende relazioni esterne, PESC e bilancio UE.
- **Rettifiche.** Per 160 delle 192 rettifiche CELLAR non dà un titolo né italiano né inglese: l'archivio scrive «Rettifica dell'atto CELEX …».
- **Proposte.** Alcune proposte recenti (7 su 64) hanno solo il titolo inglese, segnalato come tale. Lo stato della procedura legislativa (Parlamento e Consiglio) non è scaricato: c'è il link alla pagina «Procedura» di EUR-Lex.
- **Infrazioni.**
  - EUR-Infra non riporta la data delle decisioni: le «novità» sono calcolate confrontando le rilevazioni giornaliere. La prima rilevazione, l'8/11/2026, fa da base.
  - Se EUR-Infra non risponde, `infrazioni.csv` resta quello del giorno prima.
- **Scadenze del ciclo di bilancio** in `semestre.md`. Sono le scadenze ricorrenti fissate dai regolamenti (Reg. (UE) 2024/1263, art. 21; Reg. (UE) n. 473/2013, artt. 4, 6, 7), citate con l'articolo: vanno ricontrollate sul testo vigente.
- **Ritardo di CELLAR.** I metadati di un atto (EuroVoc, termini, titolo) possono completarsi nei giorni dopo la pubblicazione: per questo ogni aggiornamento riprende gli ultimi 7 giorni.
- **Il modulo non è un parere giuridico.** Serve a non perdere scadenze e a mettere gli obblighi all'ordine del giorno. Il giudizio spetta al giurista del collegio e, alla fine, agli uffici legislativi e al Dipartimento per gli affari europei.

## Integrazione (a cura del manutentore)

Nessun file fuori da `europa/` è stato modificato. Queste sono le righe da aggiungere.

### 1. `sistema/pipeline.py`: passo quotidiano

Nella funzione `main()`, subito dopo il blocco «# 3d. legislazione …» e prima di «# 3e. governo ombra …»:

```python
    # 3d-bis. europa: atti UE (GU L), scadenze di recepimento, Semestre europeo, infrazioni
    if not a.senza_download and (RADICE / "europa" / "scarica_ue.py").exists():
        ok, msg = esegui(["scarica_ue.py"], RADICE / "europa", timeout=1800)
        log.append(f"europa: {msg}" if ok else f"ERRORE europa: {msg}")
    elif (RADICE / "europa" / "uscite.py").exists():
        esegui(["uscite.py"], RADICE / "europa")  # senza rete: rigenera le uscite dall'archivio
```

Facoltativo, nel bollettino, dopo la sezione delle allerte:

```python
    ue = json.loads((RADICE / "europa" / "stato.json").read_text(encoding="utf-8")) if (RADICE / "europa" / "stato.json").exists() else {}
    if ue:
        t = ue["totali"]
        b += ["", "## Unione europea", "",
              f"{t['novita_30g']} atti UE negli ultimi 30 giorni; scadenze di recepimento: {t['scadenze_per_priorita']['critica']} critiche, "
              f"{t['scadenze_per_priorita']['alta']} alte; {t['infrazioni_aperte']} infrazioni aperte ({t['infrazioni_novita']} novità); "
              f"{ue['semestre']['procedura_disavanzo']}. Dettagli in `europa/novita.md` e `europa/semestre.md`."]
```

### 2. `governo/consiglio.py`: contesto, ordine del giorno, esperto

Nella funzione `prepara()`, subito dopo `collegio = scegli_esperti(" ".join(temi), esperti)`:

```python
    # vincoli UE per le aree convocate (modulo facoltativo europa/)
    try:
        sys.path.insert(0, str(RADICE / "europa"))
        from uscite import contesto_consiglio, odg_consiglio
        ue = contesto_consiglio(ministri)
        ue_odg = odg_consiglio(ministri)
    except Exception as e:  # noqa: BLE001 - senza europa/ la seduta si prepara lo stesso
        ue, ue_odg = {"errore": f"{e.__class__.__name__}: {e}"}, []
    # l'esperto europa_esteri entra se le aree convocate hanno infrazioni aperte o obblighi critici (scaduti o in infrazione),
    # salvo scelta manuale degli esperti; se il collegio è pieno prende il posto dell'ultimo esperto scelto per parole chiave
    if not esperti and ue.get("esperto_europa_consigliato") and all(e["id"] != "europa_esteri" for e in collegio):
        tutti = yaml.safe_load(ESPERTI.read_text(encoding="utf-8"))["esperti"]
        collegio = collegio[:MAX_ESPERTI - 1] + [e for e in tutti if e["id"] == "europa_esteri"]
```

Nel dizionario `contesto = {...}` aggiungere la chiave:

```python
        "europa": ue,
```

Nell'ordine del giorno, subito prima della riga `righe += ["", "## 2. Programma del momento (calcolato dal motore)", ...`:

```python
    if ue_odg:
        righe += [""] + ue_odg
```

`contesto["europa"]` contiene, per le aree convocate:
- `obblighi_in_scadenza`: priorità critica, alta e media, al massimo 8;
- `infrazioni`;
- `novita_30_giorni`: rilevanza alta;
- la sintesi del Semestre;
- `esperto_europa_consigliato`.

Le regole del Consiglio da aggiungere al regolamento (`governo/regolamento.md`) sono una scelta del manutentore. Il criterio suggerito:
- un obbligo UE in scadenza o in infrazione nelle aree convocate va affrontato nella seduta, con una misura di recepimento o un mandato;
- un'opportunità (fondi) va almeno citata;
- le raccomandazioni del Semestre valgono come vincolo per le misure di bilancio.

### 3. `sistema/esporta_web.py`: dati per il sito

Aggiungere la funzione, per esempio dopo `def governo()`:

```python
def europa() -> dict:
    """Scadenze UE, infrazioni, novità e Semestre (europa/); vuoto se il modulo non c'è."""
    try:
        sys.path.insert(0, str(RADICE / "europa"))
        from uscite import dati_web
        return dati_web()
    except Exception:  # noqa: BLE001
        return {}
```

Nel dizionario `dati` aggiungere, accanto a `"governo": governo(),`:

```python
        "europa": europa(),
```

`dati_web()` restituisce:
- `stato`: i conteggi per area;
- `scadenze`: priorità critica, alta e media;
- `infrazioni`;
- `novita_md` e `semestre_md`.

Pesa circa 200 KB, per metà il testo di `novita.md`. Se serve un `data.js` più leggero, si può togliere `novita_md` e linkare il file.

### 4. `integrita/catena.py`: input nella catena

In `REGOLE` aggiungere le regole e il codice che decidono la pertinenza:

```python
          "europa/regole.yaml", "europa/pertinenza.py", "europa/uscite.py", "europa/scarica_ue.py",
```

In `INPUT` aggiungere ciò che il Consiglio e il programma leggono:

```python
         "europa/scadenze.csv", "europa/infrazioni.csv", "europa/stato.json",
         "europa/archivio/atti.csv", "europa/archivio/direttive.csv", "europa/archivio/semestre.json",
```

Non includere `europa/archivio/cache/` né `europa/archivio/testi/`: sono copie di lavoro, rigenerabili.

### 5. Repository

`archivio/cache/` contiene le ultime pagine HTML scaricate, circa 0,3 MB; si può escludere con `.gitignore` (`europa/archivio/cache/`), perché serve solo come ripiego locale. Il resto dell'archivio pesa circa 1 MB e conviene versionarlo: senza lo storico delle infrazioni non si riconoscono le novità.
