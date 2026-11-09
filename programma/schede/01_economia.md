# GovernAI — Schede pronte, Area 01: Economia, Imprese, Turismo

*Agente ministeriale area 01, 7 novembre 2026. Varianti in `programma/varianti/01_economia.csv`. Dati da `dati/serie/01_*`, `dati/serie/00b_*` e `dati/verifiche/01_economia.md`; "stima GovernAI" indica una stima propria, senza quantificazione ufficiale. Importi in mld €/anno salvo diversa indicazione. Documento di consulenza: le decisioni spettano a Governo e Parlamento.*

**Regole comuni a tutte le schede**
- Nessuna variante usa DEFICIT, RISPARMI_ATTESI, IVA_EVASIONE, ETS o ALTRO. Il margine sulla spesa netta è zero (circa -2,4 mld di deviazione cumulata, UPB ottobre 2026): ogni euro va coperto con DRM o tagli di spesa effettiva.
- RIALLOCAZIONE significa taglio di spese che si sarebbero davvero fatte, non uso di residui (che aumenterebbe la spesa netta).
- Le proposte 01-P2 e 01-P3 *producono* risorse, ma non le contabilizzano in questo file: 01-P2 è lo strumento per conseguire i 7,37 mld già nel Piano strutturale; il recupero IVA di 01-P3 va al deficit e solo dopo certificazione.

**Quadro delle varianti (costo a regime, intensità)**

| Proposta | PIENA | ESSENZIALE | PILOTA / ZERO | Variante raccomandata |
|---|---|---|---|---|
| 01-P1 Bilancio generazionale | 0,02 · 1 | 0,01 · 0,7 | ZERO 0 · 0,35 | PIENA (costo trascurabile) |
| 01-P2 Spese fiscali a scadenza | 0,01 · 1 | 0,01 · 0,6 | ZERO 0 · 0,3 | PIENA |
| 01-P3 IVA in tempo reale | 0,15 · 1 | 0,08 · 0,6 | PILOTA 0,04 · 0,25 | PIENA o ESSENZIALE |
| 01-P4 Crescere conviene | 2,5 · 1 | 0,6 · 0,5 | ZERO 0,01 · 0,25 | ESSENZIALE |
| 01-P5 PPA per le PMI | 0,35 · 1 | 0,15 · 0,55 | PILOTA 0,05 · 0,15 | ESSENZIALE |
| 01-P6 Turismo che ripaga | 0,15 · 1 | 0,05 · 0,65 | ZERO 0 · 0,4 | ESSENZIALE |

Pacchetto raccomandato (P1 piena, P2 piena, P3 piena, P4 essenziale, P5 essenziale, P6 essenziale): **circa 0,98 mld/anno a regime**, di cui 0,43 RIALLOCAZIONE, 0,4 SPESE_FISCALI (nuova misura di copertura), 0,15 COESIONE_2127 (una tantum 2027-29).

---

## 01-P1 — Bilancio generazionale: ogni legge dichiara chi paga e quando

**Problema in un dato.** La spesa per interessi sale dal 3,8% del PIL nel 2025 (87,2 mld, Eurostat gov_10a_main, `01_interessi_mio_eur`) al 4,3% nel 2027, oltre 100 mld (MEF, DPB 2027, tab. III.1-5). La relazione tecnica guarda però a 3 anni: i costi differiti (pensioni, bonus edilizi, condoni) restano fuori dalla decisione.

**Soluzione.** Ogni atto con effetti superiori allo 0,05% del PIL, o strutturali oltre 10 anni, porta una valutazione a 30 anni su debito, clima e coorti d'età. L'UPB pubblica entro 15 giorni un giudizio a semaforo. Con il rosso il Governo risponde per iscritto in Commissione Bilancio prima del voto: nessun veto, piena responsabilità politica.

**Varianti**

| Variante | Contenuto | Costo a regime | Intensità |
|---|---|---|---|
| PIENA | 3 conti (debito, clima, coorti), soglia 0,05% PIL, semaforo UPB | 0,02 (RIALLOCAZIONE) | 1 |
| ESSENZIALE | debito e coorti, soglia 0,1% PIL, semaforo UPB | 0,01 | 0,7 |
| ZERO | relazione RGS a 10 anni e tabella per coorte, senza UPB | 0 | 0,35 |

**Articolato normativo essenziale** (disegno di legge, modifica della L. 196/2009 e della L. 243/2012)

> **Art. 1 (Finalità).** 1. La presente legge assicura che le decisioni di finanza pubblica rendano esplicito il loro impatto sulle generazioni presenti e future, in attuazione degli articoli 9, terzo comma, 81 e 97, primo comma, della Costituzione.
>
> **Art. 2 (Valutazione generazionale).** 1. Dopo l'articolo 17 della legge 31 dicembre 2009, n. 196, è inserito il seguente: «Art. 17-bis. – 1. I disegni di legge, gli schemi di decreto legislativo e gli emendamenti del Governo i cui effetti finanziari superano, in almeno un anno, lo 0,05 per cento del prodotto interno lordo, o producono effetti strutturali oltre il decimo anno, sono corredati di una valutazione generazionale con orizzonte di trenta anni. 2. La valutazione indica, per intervalli e in almeno due scenari di tasso di interesse: a) l'effetto sul rapporto tra debito e prodotto interno lordo; b) l'effetto sulle emissioni di gas a effetto serra, in coerenza con l'ecobilancio di cui all'articolo 36, comma 6; c) la distribuzione di benefici e oneri per coorte di nascita. 3. La metodologia è adottata con decreto del Ministro dell'economia e delle finanze, sentito l'Ufficio parlamentare di bilancio, ed è pubblicata con i codici di calcolo.»
>
> **Art. 3 (Giudizio dell'Ufficio parlamentare di bilancio).** 1. Entro quindici giorni dalla trasmissione, l'Ufficio parlamentare di bilancio esprime sulla valutazione un giudizio sintetico articolato in tre classi (sostenibile, da motivare, non sostenibile) e lo pubblica. 2. In caso di giudizio "non sostenibile", il Governo deposita presso le Commissioni bilancio, prima del voto finale, una risposta scritta motivata. 3. All'articolo 18 della legge 24 dicembre 2012, n. 243, è aggiunta la relativa funzione.
>
> **Art. 4 (Revisione).** 1. Dopo l'approvazione della terza legge di bilancio successiva all'entrata in vigore, la Corte dei conti riferisce alle Camere sugli effetti della valutazione sulle decisioni, proponendone il rafforzamento o la soppressione.
>
> **Art. 5 (Copertura finanziaria).** 1. Agli oneri, pari a 10 milioni di euro per l'anno 2027 e a 20 milioni a decorrere dal 2028, si provvede mediante corrispondente riduzione delle spese di funzionamento del Ministero dell'economia e delle finanze, missione "Servizi istituzionali e generali", con esclusione delle spese obbligatorie.

**Cronoprogramma**
- *Primi 100 giorni:* MEF-RGS e UPB redigono il ddl e la bozza di metodologia; presentazione alle Camere; protocollo con ISTAT per i conti per coorte.
- *Entro 12 mesi:* approvazione; decreto sulla metodologia; assunzione di circa 10 unità all'UPB e 10 alla RGS; prova sulla legge di bilancio 2028 (in parallelo, non vincolante).
- *Entro fine legislatura:* applicazione piena a due leggi di bilancio; prima revisione esterna; relazione della Corte dei conti.

**Indicatori**

| KPI | Base (dato, anno, fonte) | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Quota di atti sopra soglia con valutazione generazionale | 0%, 2026 (nessun obbligo) | 100% | 100%, con revisione esterna |
| Giudizi "non sostenibile" con risposta scritta del Governo | non applicabile, 2026 | 100% | 100% |
| Scostamento tra costo stimato e costo effettivo delle misure valutate (misure > 0,1% PIL) | non rilevato, 2026 | rilevato per tutte | entro ±20% per l'80% delle misure |

Indicatore di contesto: debito/PIL 138,5% nel 2027 e 136,6% nel 2029 programmato (DPB 2027): la misura non lo "garantisce", ma rende visibile ogni scostamento dal percorso.

**Rischi e mitigazioni**
- *Adempimento formale:* metodologia e codici pubblici, revisione esterna triennale, obbligo di risposta.
- *Incertezza dei modelli a 30 anni:* solo intervalli e scenari, mai un numero unico.
- *Sovrapposizione con 02-C6:* un solo strumento; 02-C6 fornisce le proiezioni demografiche.
- *Tempi parlamentari stretti in sessione di bilancio:* valutazione preliminare RGS già allegata al ddl; per gli emendamenti, solo quelli governativi sopra soglia.

---

## 01-P2 — Spese fiscali "a scadenza": ogni agevolazione decade dopo 5 anni se non dimostra di funzionare

**Problema in un dato.** Le spese fiscali erariali sono **573**, per **129,7 mld nel 2026** (MEF, Rapporto spese fiscali 2025). L'UPB ne contava 466 nel 2018 e 625 nel 2024 (Focus 4/2024): il numero cresce e nessuna misura deve dimostrare di funzionare. Il Piano strutturale di bilancio conta già **7,37 mld** di riordino, senza indicare il metodo.

**Soluzione.** Ogni spesa fiscale riceve una data di scadenza, scaglionata in 5 anni. Una Commissione indipendente pubblica per ciascuna una scheda (costo, chi ne beneficia per decile, efficacia) e il Parlamento la rinnova solo con un voto esplicito e una copertura. È il metodo per conseguire i 7,37 mld già nel Piano, non una risorsa aggiuntiva: il gettito oltre quella soglia va al menu coperture.

**Varianti**

| Variante | Contenuto | Costo a regime | Intensità |
|---|---|---|---|
| PIENA | scadenza per tutte le 573 misure; esenti dalla scadenza (non dalla valutazione) salute, disabilità, famiglia, obblighi UE | 0,01 (RIALLOCAZIONE) | 1 |
| ESSENZIALE | scadenza per le misure nuove o prorogate e per la metà meno valutata dello stock | 0,01 | 0,6 |
| ZERO | solo scheda di valutazione obbligatoria, senza scadenza | 0 | 0,3 |

**Articolato normativo essenziale** (legge delega; decreto legislativo entro 12 mesi)

> **Art. 1 (Finalità).** 1. Al fine di assicurare l'efficacia, l'equità e la trasparenza delle spese fiscali e di conseguire gli obiettivi di riordino previsti dal Piano strutturale di bilancio di medio termine, il Governo è delegato ad adottare, entro dodici mesi, uno o più decreti legislativi secondo i principi e criteri direttivi di cui agli articoli 2 e 3.
>
> **Art. 2 (Clausola di scadenza).** 1. Ciascuna spesa fiscale censita nel rapporto di cui all'articolo 21, comma 11-bis, della legge 31 dicembre 2009, n. 196, cessa di avere efficacia al termine del quinto periodo d'imposta successivo all'entrata in vigore del decreto legislativo, secondo un calendario che distribuisce le scadenze in cinque annualità e pone per prime le misure con minor numero di soggetti beneficiari o prive di valutazione. 2. Le spese fiscali introdotte o prorogate dopo l'entrata in vigore della presente legge hanno durata non superiore a cinque anni. 3. Sono escluse dalla cessazione automatica, ma non dalla valutazione, le agevolazioni relative a spese sanitarie, disabilità, carichi familiari e quelle che attuano obblighi dell'Unione europea.
>
> **Art. 3 (Valutazione e rinnovo).** 1. La Commissione per la redazione del rapporto annuale sulle spese fiscali è integrata da persone esperte indipendenti e dotata di una segreteria tecnica; accede ai dati dell'Agenzia delle entrate in forma anonimizzata, nel rispetto del regolamento (UE) 2016/679. 2. Per ogni misura in scadenza pubblica, almeno dodici mesi prima, una scheda su costo, soggetti beneficiari per decile di reddito e territorio, efficacia rispetto all'obiettivo e alternative. 3. Il rinnovo è disposto con norma specifica, votata separatamente e munita di copertura ai sensi dell'articolo 17 della legge n. 196 del 2009.
>
> **Art. 4 (Destinazione dei risparmi).** 1. I risparmi concorrono prioritariamente al conseguimento dell'obiettivo di riordino previsto dal Piano strutturale di bilancio. 2. Le maggiori entrate eccedenti tale obiettivo, accertate a consuntivo, sono destinate con legge di bilancio alla riduzione del cuneo fiscale sui redditi da lavoro medio-bassi e alla riduzione dell'indebitamento netto.
>
> **Art. 5 (Copertura finanziaria).** 1. Agli oneri per la segreteria tecnica e il laboratorio dati, pari a 5 milioni di euro per il 2027 e a 10 milioni a decorrere dal 2028, si provvede mediante riduzione delle spese di funzionamento del Ministero dell'economia e delle finanze. 2. Dall'attuazione della presente legge non derivano nuovi o maggiori oneri per la finanza pubblica.

**Cronoprogramma**
- *Primi 100 giorni:* MEF (Dipartimento Finanze) presenta la delega, anche come collegato alla manovra; avvio della segreteria tecnica e della convenzione con l'Agenzia delle entrate per i dati.
- *Entro 12 mesi:* decreto legislativo; calendario delle scadenze pubblicato; prime 20 schede sulle misure del primo scaglione.
- *Entro fine legislatura:* due scaglioni scaduti e votati; relazione UPB sul gettito; aggancio esplicito all'obiettivo dei 7,37 mld nel monitoraggio del Piano.

**Indicatori**

| KPI | Base (dato, anno, fonte) | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Numero di spese fiscali erariali | 573, 2026 (MEF, RSF 2025) | ≤ 490 (-15%) | ≤ 400 (-30%) |
| Riordino conseguito rispetto all'obiettivo del Piano | 0 su 7,37 mld (MEF, RSF 2025) | ≥ 50% | 100% |
| Quota di misure con scheda di valutazione pubblica | ~0%, 2026 | 60% | 100% |

**Rischi e mitigazioni**
- *Rinnovi in blocco:* voto separato per misura e obbligo di copertura.
- *Settori fragili (autotrasporto, agricoltura):* transizione triennale e compensazioni non fiscali; coordinamento con la riforma dei SAD (area 03).
- *Doppio conteggio con i 7,37 mld:* nessun gettito della proposta è registrato in questo file; il gettito ulteriore passa solo dal menu coperture.
- *Incertezza per le imprese:* calendario pubblicato dal primo giorno e almeno 12 mesi di preavviso.

---

## 01-P3 — IVA in tempo reale: chiudere il buco più grande dell'evasione

**Problema in un dato.** Il gap IVA è di **34,4 mld nel 2023**, in risalita di 3,6 mld sul 2022 (30,7 mld) (MEF, Relazione evasione 2026, tab. III.1; `01_estratti_documenti.csv`). Il tax gap complessivo è di 107,9-112,8 mld.

**Soluzione.** L'Agenzia delle entrate incrocia fatture elettroniche, corrispettivi e pagamenti elettronici e blocca crediti e compensazioni anomali prima che il denaro sparisca. Chi è affidabile ottiene rimborsi entro 60 giorni e meno controlli. Impegno di legislatura: nessun condono. Il recupero non copre spesa ex ante: va al deficit e, certificato, al fondo IVA_EVASIONE.

**Varianti**

| Variante | Contenuto | Costo a regime (2027-29) | Intensità |
|---|---|---|---|
| PIENA | analisi del rischio, blocco preventivo, reverse charge e split payment estesi (deroga UE), rimborsi rapidi, no condoni | 0,15 (0,4 / 0,4 / 0,3), RIALLOCAZIONE | 1 |
| ESSENZIALE | come sopra senza estensione di reverse charge e split payment | 0,08 (0,2 / 0,2 / 0,15) | 0,6 |
| PILOTA | tre settori ad alto rischio, due anni, valutazione | 0,04 | 0,25 |

**Articolato normativo essenziale** (disegno di legge; parte attuativa con provvedimenti del Direttore dell'Agenzia delle entrate)

> **Art. 1 (Finalità).** 1. Al fine di ridurre il divario tra imposta sul valore aggiunto dovuta e versata e di semplificare gli adempimenti dei contribuenti leali, la presente legge istituisce un sistema di analisi del rischio IVA in tempo quasi reale e una corsia preferenziale per i contribuenti affidabili.
>
> **Art. 2 (Analisi del rischio e misure preventive).** 1. L'Agenzia delle entrate integra i dati delle fatture elettroniche, dei corrispettivi telematici e dei pagamenti elettronici in un sistema di analisi del rischio. 2. In presenza di indici di rischio qualificati, l'Agenzia può sospendere per non più di trenta giorni l'utilizzo in compensazione di crediti IVA e l'efficacia di partite IVA di nuova attivazione, previa verifica di un funzionario e con comunicazione motivata al contribuente, che può presentare osservazioni entro dieci giorni. 3. I modelli di rischio sono sottoposti a valutazione d'impatto ai sensi dell'articolo 35 del regolamento (UE) 2016/679, sentito il Garante per la protezione dei dati personali, e ad audit annuale; nessuna misura è adottata senza decisione umana, in conformità al regolamento (UE) 2024/1689.
>
> **Art. 3 (Contribuenti affidabili).** 1. Ai contribuenti con elevato indice sintetico di affidabilità fiscale o aderenti al regime di adempimento collaborativo i rimborsi IVA sono erogati entro sessanta giorni dalla richiesta, senza garanzia.
>
> **Art. 4 (Settori ad alto rischio).** 1. Il Governo richiede al Consiglio dell'Unione europea, ai sensi dell'articolo 395 della direttiva 2006/112/CE, l'autorizzazione ad applicare l'inversione contabile o la scissione dei pagamenti alle cessioni e prestazioni dei settori individuati con decreto del Ministro dell'economia e delle finanze sulla base dei dati di cui all'articolo 2. *(Solo variante PIENA.)*
>
> **Art. 5 (Divieto di definizioni agevolate e trasparenza).** 1. Fino al termine della legislatura non possono essere introdotte definizioni agevolate dei carichi affidati all'agente della riscossione né condoni dei tributi erariali. 2. Il Ministero pubblica ogni anno i risultati del sistema: frodi intercettate, sospensioni annullate, tempi dei rimborsi.
>
> **Art. 6 (Copertura finanziaria e uso delle maggiori entrate).** 1. Agli oneri, pari a 400 milioni di euro per ciascuno degli anni 2027 e 2028, 300 milioni per il 2029 e 150 milioni a decorrere dal 2030, si provvede mediante riduzione degli stanziamenti di funzionamento del Ministero dell'economia e delle finanze e delle agenzie fiscali, con esclusione delle spese per il personale. 2. Le maggiori entrate derivanti dalla presente legge non sono utilizzate a copertura di nuove o maggiori spese; accertate a consuntivo, concorrono alla riduzione dell'indebitamento netto.

**Cronoprogramma**
- *Primi 100 giorni:* MEF e Agenzia delle entrate definiscono il modello di rischio e il piano IT (Sogei); avvio della valutazione d'impatto con il Garante; presentazione del ddl; avvio del pilota sui tre settori ad alto rischio (atto amministrativo).
- *Entro 12 mesi:* legge approvata; corsia rimborsi rapidi operativa; prima relazione sui crediti bloccati; richiesta di deroga UE (variante piena); coordinamento con il pacchetto ViDA.
- *Entro fine legislatura:* sistema a regime su tutti i settori; prima misura certificata del calo del gap (Relazione evasione); audit indipendente se il gap non scende di almeno il 7% in 3 anni.

**Indicatori**

| KPI | Base (dato, anno, fonte) | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Gap IVA | 34,4 mld, 2023 (MEF, Relazione evasione 2026) | ≤ 32 mld (-7%) | ≤ 28,5 mld (-15/-20% = 5,2-6,9 mld recuperati) |
| Tempo medio dei rimborsi IVA ai contribuenti affidabili | da rilevare (Agenzia delle entrate, 2026) | ≤ 90 giorni | ≤ 60 giorni |
| Nuovi condoni o definizioni agevolate | — | 0 | 0 |

**Rischi e mitigazioni**
- *Falsi positivi e privacy:* decisione umana obbligatoria, contraddittorio in 10 giorni, audit annuale, pubblicazione delle sospensioni annullate.
- *Costi di adeguamento per le micro-imprese:* nessun nuovo adempimento; precompilata IVA come contropartita.
- *Tempi UE per le deroghe:* la variante ESSENZIALE funziona senza deroghe.
- *Tentazione di spendere il recupero in anticipo:* vietato dall'art. 6; il gettito va al deficit e solo dopo certificazione al fondo IVA_EVASIONE.

---

## 01-P4 — "Crescere conviene" (versione mirata): togliere i gradini che tengono piccole le imprese

**Problema in un dato.** Il **60,0%** delle persone occupate lavora in imprese con meno di 50 addetti, contro il 41,6% in Francia e il 39,4% in Germania (Eurostat sbs_sc_ovw, 2024; `01_quota_occupati_micro_piccole`). La produttività del lavoro è cresciuta dello 0,3% l'anno nel 1995-2024, contro l'1,5% dell'UE27 (ISTAT, dicembre 2025); l'indice del PIL per ora lavorata è a 100,4 nel 2025 (2015=100; Eurostat nama_10_lp_ulc).

**Soluzione.** Chi supera 15 o 50 addetti ha tre anni per adeguarsi agli obblighi amministrativi; salute, sicurezza e diritti sindacali restano pieni da subito. Un premio di crescita, con tetto annuo, va solo alle imprese tra 10 e 49 addetti che crescono, si fondono o fanno rete. Il costo scende da 2,5 a 0,6 mld, finanziato rimodulando la parte generica dell'iperammortamento.

**Varianti**

| Variante | Contenuto | Costo a regime (fondi) | Intensità |
|---|---|---|---|
| PIENA | come nel dossier, incentivi per tutte le imprese | 2,5 (SPESE_FISCALI) | 1 |
| **ESSENZIALE (raccomandata)** | soglie graduali a 15 e 50 + premio solo 10-49 addetti con tetto + sportello unico | 0,6 (SPESE_FISCALI 0,4; RIALLOCAZIONE 0,2) | 0,5 |
| ZERO | solo soglie graduali e sportello unico | 0,01 (RIALLOCAZIONE) | 0,25 |

La variante ESSENZIALE prende la parte a costo zero, cioè la graduazione delle soglie, e concentra l'incentivo dove l'effetto soglia è più forte. Realizza metà dell'effetto con un quarto del costo.

**Articolato normativo essenziale** (disegno di legge; premio in legge di bilancio)

> **Art. 1 (Finalità).** 1. Al fine di favorire la crescita dimensionale, l'aggregazione e la produttività delle micro e piccole imprese, senza ridurre i diritti di chi lavora, la presente legge gradua gli obblighi amministrativi connessi alle soglie occupazionali e istituisce un premio di crescita.
>
> **Art. 2 (Mappatura delle soglie).** 1. Entro sei mesi il Ministro delle imprese e del made in Italy, di concerto con i Ministri del lavoro e delle politiche sociali e dell'economia e delle finanze, sentite le parti sociali, pubblica l'elenco degli obblighi amministrativi, contabili e informativi che sorgono al superamento delle soglie di 10, 15, 50 e 250 addetti.
>
> **Art. 3 (Regime transitorio di crescita).** 1. L'impresa che supera per la prima volta la soglia di 15 o di 50 addetti applica gli obblighi amministrativi, contabili e informativi individuati ai sensi dell'articolo 2 a decorrere dal terzo esercizio successivo. 2. Restano immediatamente applicabili gli obblighi in materia di salute e sicurezza sul lavoro, i diritti sindacali e le tutele contro i licenziamenti illegittimi. 3. Il beneficio non spetta e ne è disposto il recupero in caso di frazionamento artificioso dell'impresa, accertato sulla base dei bilanci consolidati e dei rapporti di controllo.
>
> **Art. 4 (Premio di crescita).** 1. Alle imprese con un numero di addetti compreso tra 10 e 49 che, nel triennio successivo all'investimento, superano una soglia di cui all'articolo 3, partecipano a una fusione o stipulano un contratto di rete con programma industriale, ovvero aumentano il valore aggiunto per addetto di almeno il 10 per cento, spetta una maggiorazione aggiuntiva dell'iperammortamento sugli investimenti in beni strumentali, software, formazione e ricerca. Nelle zone economiche speciali la maggiorazione è aumentata di un quinto. 2. Il beneficio è riconosciuto nel limite di spesa di 600 milioni di euro annui a regime; l'Agenzia delle entrate monitora mensilmente gli utilizzi e, al raggiungimento del limite, sospende le nuove prenotazioni.
>
> **Art. 5 (Sportello unico e stabilità delle regole).** 1. È istituito presso il Ministero delle imprese e del made in Italy, avvalendosi di Invitalia e delle piattaforme esistenti, lo sportello digitale "Impresa che cresce", con un'unica istanza per i benefici della presente legge. 2. I requisiti di cui all'articolo 4 non possono essere modificati in senso restrittivo per cinque anni, salvo che per la copertura del limite di spesa.
>
> **Art. 6 (Valutazione e copertura finanziaria).** 1. Dopo quattro anni ISTAT e Agenzia delle entrate valutano gli effetti con metodo controfattuale; se non si riscontra un effetto significativo su dimensione o produttività, il premio cessa. 2. Agli oneri di cui all'articolo 4, pari a 100 milioni per il 2027, 400 milioni per il 2028 e 600 milioni a decorrere dal 2029, si provvede: a) per 400 milioni mediante riduzione della maggiorazione base dell'iperammortamento per gli investimenti non qualificati; b) per 200 milioni mediante riduzione delle autorizzazioni di spesa per incentivi alle imprese gestiti dal Ministero delle imprese e del made in Italy, individuati come a bassa addizionalità dalla valutazione di cui alla legge sulle spese fiscali a scadenza. 3. Agli oneri dell'articolo 5, pari a 10 milioni annui, si provvede a valere sulle risorse di funzionamento del medesimo Ministero.

**Cronoprogramma**
- *Primi 100 giorni:* tavolo MIMIT-Lavoro-MEF con le parti sociali, con la linea rossa "nessun diritto sostanziale toccato"; avvio della mappatura; presentazione del ddl.
- *Entro 12 mesi:* mappatura pubblicata; regime transitorio in vigore; premio in legge di bilancio 2028 con limite di spesa; sportello operativo (Invitalia).
- *Entro fine legislatura:* primi dati sulle imprese che superano le soglie; valutazione controfattuale ISTAT-Agenzia delle entrate al quarto anno; decisione su proroga o chiusura.

**Indicatori**

| KPI | Base (dato, anno, fonte) | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Quota di persone occupate in imprese con meno di 50 addetti | 60,0%, 2024 (Eurostat sbs_sc_ovw) | ≤ 59,3% | ≤ 58,5% |
| Valore aggiunto per addetto delle imprese beneficiarie rispetto al gruppo di controllo | 0, 2026 (avvio) | +3% | +5%, significativo |
| PIL per ora lavorata (indice 2015=100), indicatore di contesto | 100,4, 2025 (Eurostat nama_10_lp_ulc) | ≥ 102 | ≥ 104 |

**Rischi e mitigazioni**
- *Opposizione sindacale:* nessuna modifica a diritti sostanziali, sicurezza e tutele sui licenziamenti; il regime riguarda solo obblighi amministrativi e informativi.
- *Elusione (frazionamenti, fusioni di comodo):* verifica sui bilanci consolidati, recupero del beneficio, requisito del piano industriale per le reti.
- *Sforamento della spesa:* limite annuo con prenotazione e monitoraggio mensile.
- *Squilibrio Nord-Sud:* maggiorazione di un quinto nelle ZES.

---

## 01-P5 — Energia a prezzo stabile per le PMI: contratti di lungo periodo sulle rinnovabili

**Problema in un dato.** Il prezzo medio all'ingrosso dell'elettricità (PUN) è di **115,32 €/MWh nel 2025**, in aumento da 108,52 nel 2024 (GME; `03_pun_gme`). Il sostegno temporaneo all'energia delle imprese costa **1,7 mld** ogni anno in cui si rinnova (politiche invariate, `dati/verifiche/00_vincolo_bilancio.md`) e non cambia il meccanismo di formazione del prezzo.

**Soluzione.** Il GSE mette all'asta contratti di acquisto (PPA) di 10-15 anni tra gruppi di PMI e nuovi impianti rinnovabili. Una garanzia pubblica di prima perdita copre il rischio di insolvenza che oggi esclude le piccole imprese. È l'alternativa strutturale ai bonus in bolletta. In versione mirata è finanziata con strumenti finanziari FESR, a spesa una tantum.

**Varianti**

| Variante | Contenuto | Costo (2027 / 2028 / 2029) | Intensità |
|---|---|---|---|
| PIENA | aste annuali aperte a tutte le PMI, fondo garanzia 1 mld | 0,35 / 0,35 / 0,3 (COESIONE_2127 0,25 + SAD 0,1) | 1 |
| **ESSENZIALE (raccomandata)** | prima perdita 15% solo per consorzi e distretti energivori, fondo 0,4 mld | 0,15 / 0,15 / 0,1 (COESIONE_2127) | 0,55 |
| PILOTA | un'asta in 2-3 distretti | 0,05 / 0,05 / 0,03 (COESIONE_2127) | 0,15 |

Dopo il 2029 il fabbisogno scende a circa 0,02-0,05 mld/anno per le perdite attese (stima GovernAI). Il fondo è rotativo.

**Articolato normativo essenziale** (decreto ministeriale MASE-MIMIT su base di norma primaria breve, da inserire in un decreto legge o in legge annuale sulle PMI)

> **Art. 1 (Finalità).** 1. Al fine di stabilizzare il costo dell'energia elettrica per le piccole e medie imprese e di accelerare la realizzazione di nuova capacità rinnovabile, in coerenza con il regolamento (UE) 2024/1747 sull'assetto del mercato dell'energia elettrica, è istituito il programma "PPA PMI".
>
> **Art. 2 (Aste per contratti aggregati).** 1. Il Gestore dei servizi energetici organizza, con cadenza almeno biennale, procedure competitive per l'abbinamento di contratti di acquisto di energia rinnovabile di durata da dieci a quindici anni tra aggregazioni di PMI (consorzi, contratti di rete, distretti e comunità energetiche industriali) e impianti di nuova costruzione. 2. La quota dei consumi coperta per ciascuna impresa non supera il 70 per cento. 3. Le imprese aderenti effettuano una diagnosi energetica e adottano un piano di efficienza.
>
> **Art. 3 (Garanzia di prima perdita).** 1. È istituita presso il Fondo di garanzia per le PMI una sezione speciale che garantisce, nella misura della prima perdita fino al 15 per cento del portafoglio, gli obblighi di pagamento delle imprese aderenti. 2. La sezione è alimentata con 400 milioni di euro nel triennio 2027-2029 a valere sui programmi cofinanziati dal Fondo europeo di sviluppo regionale 2021-2027, previa riprogrammazione con la Commissione europea, ed è rotativa.
>
> **Art. 4 (Priorità e coordinamento).** 1. Nella prima procedura sono ammesse in via prioritaria le aggregazioni dei settori ad alta intensità energetica. 2. Il programma è coordinato con le misure di cui al decreto FER-X e con l'Energy Release; gli impianti abbinati accedono alle procedure semplificate nelle aree idonee.
>
> **Art. 5 (Valutazione).** 1. Dopo tre anni il Ministero dell'ambiente e della sicurezza energetica riferisce su capacità contrattualizzata, insolvenze garantite e costo per MWh stabilizzato; la notifica alla Commissione europea in materia di aiuti di Stato precede l'avvio.
>
> **Art. 6 (Copertura finanziaria).** 1. Agli oneri di cui all'articolo 3, pari a 150 milioni per ciascuno degli anni 2027 e 2028 e a 100 milioni per il 2029, si provvede a valere sulle risorse dei programmi FESR 2021-2027 riprogrammate ai sensi del medesimo articolo, senza nuovi o maggiori oneri per il bilancio dello Stato.

**Cronoprogramma**
- *Primi 100 giorni:* MASE, MIMIT e GSE redigono lo schema d'asta e il contratto standard; il Dipartimento coesione apre la riprogrammazione FESR con le Regioni interessate; pre-notifica alla DG COMP.
- *Entro 12 mesi:* sezione speciale del Fondo PMI operativa; via libera aiuti di Stato; prima asta pilota in 2-3 distretti.
- *Entro fine legislatura:* due aste nazionali; prima valutazione a 3 anni; decisione su estensione al terziario, con eventuale quota SAD per il Centro-Nord.

**Indicatori** (obiettivi per la variante ESSENZIALE)

| KPI | Base (dato, anno, fonte) | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Nuova capacità rinnovabile contrattualizzata con PPA aggregati di PMI | 0 GW, 2026 (nessun programma) | 0,5 GW | 1,5 GW |
| PMI aderenti | 0, 2026 | 1.000 | 4.000 |
| Prezzo medio pagato dalle aderenti rispetto al PUN | PUN 115,32 €/MWh, 2025 (GME) | ≤ PUN -10% | ≤ PUN -15%, volatilità dimezzata |

**Rischi e mitigazioni**
- *Ritardi autorizzativi degli impianti:* abbinamento solo a impianti in aree idonee o già autorizzati; coordinamento con l'area 03 (CfD, 03-P2) e con le Regioni.
- *Prezzi di mercato sotto il prezzo fisso (rimpianto):* copertura massima del 70% dei consumi e clausole di revisione.
- *Insolvenze sopra le attese:* garanzia limitata alla prima perdita al 15%, con reintegro solo con nuova norma.
- *Vincoli dei fondi FESR (regioni, scadenze n+3):* uso nelle regioni con dotazione disponibile; per il Centro-Nord, quota SAD solo nella variante piena.

---

## 01-P6 — Turismo che ripaga i territori: imposta di soggiorno intelligente e patto per la destagionalizzazione

**Problema in un dato.** Luglio e agosto concentrano il **34,5%** delle presenze annue, giugno-settembre il **56,9%** (466,2 milioni di presenze nel 2024; Eurostat tour_occ_nim, elaborazione GovernAI). Nel 2025 le presenze salgono a 535,5 milioni, ma il dato non è pienamente confrontabile per l'ampliamento del campo di osservazione (`01_presenze_turistiche`).

**Soluzione.** I Comuni ad alta intensità turistica possono modulare l'imposta di soggiorno per stagione e zona, entro un tetto nazionale e con riduzioni obbligatorie in bassa stagione. Almeno metà del gettito va per legge a casa, trasporti e servizi per chi ci abita, e i dati CIN sugli affitti brevi diventano pubblici. Un patto Stato-Regioni premia chi sposta presenze fuori stagione e nelle aree interne.

**Varianti**

| Variante | Contenuto | Costo per lo Stato a regime | Intensità |
|---|---|---|---|
| PIENA | modulazione, vincolo 50%, dati CIN, patto, credito di riqualificazione condizionato | 0,15 (RIALLOCAZIONE, Fondo turismo) | 1 |
| **ESSENZIALE (raccomandata)** | modulazione, vincolo 50%, dati CIN, patto da 50 mln legato a obiettivi | 0,05 | 0,65 |
| ZERO | solo norma su modulazione, vincolo e dati CIN | 0 | 0,4 |

Gettito comunale aggiuntivo stimato in 0,3-0,8 mld/anno (fondo TASSA_SOGGIORNO, entrata dei Comuni vincolata: non finanzia spesa statale).

**Articolato normativo essenziale** (disegno di legge, modifica dell'art. 4 del d.lgs. 23/2011; intesa in Conferenza unificata)

> **Art. 1 (Finalità).** 1. Al fine di distribuire nel tempo e nello spazio i flussi turistici e di destinare alla popolazione residente una quota dei benefici del turismo, la presente legge modifica la disciplina dell'imposta di soggiorno e istituisce il Patto nazionale per la destagionalizzazione.
>
> **Art. 2 (Imposta di soggiorno modulata).** 1. All'articolo 4 del decreto legislativo 14 marzo 2011, n. 23, dopo il comma 1 è inserito il seguente: «1-bis. I comuni individuati come ad alta intensità turistica sulla base di un indice ISTAT di presenze per residente possono articolare l'imposta per periodi dell'anno e zone del territorio, entro il limite massimo fissato con decreto del Ministro dell'economia e delle finanze, d'intesa con la Conferenza Stato-città ed autonomie locali, in misura non superiore alla media dei principali Paesi dell'Unione europea. Nei mesi di bassa stagione individuati dal comune la misura è ridotta di almeno un terzo rispetto alla misura ordinaria.»
>
> **Art. 3 (Destinazione del gettito e trasparenza).** 1. Almeno il 50 per cento del gettito dell'imposta di soggiorno è destinato a trasporto pubblico locale, edilizia residenziale a canone calmierato, gestione dei rifiuti e manutenzione urbana. 2. I comuni pubblicano annualmente il rendiconto del gettito e del suo impiego sul portale della finanza locale.
>
> **Art. 4 (Dati sugli affitti brevi).** 1. Il Ministero del turismo pubblica, in forma aggregata e anonimizzata per sezione di censimento, i dati della banca dati del codice identificativo nazionale, in coerenza con il regolamento (UE) 2024/1028. 2. Sulla base di tali dati e di indicatori di pressione abitativa, i comuni possono stabilire limiti motivati e proporzionati per zona alle locazioni brevi.
>
> **Art. 5 (Patto per la destagionalizzazione).** 1. Con intesa in Conferenza unificata è adottato il Patto nazionale per la destagionalizzazione. Una quota del Fondo per il turismo, pari a 50 milioni di euro annui, è ripartita tra le Regioni in base al raggiungimento di obiettivi misurati di presenze fuori dai mesi di picco e nelle aree interne, con priorità per collegamenti ferroviari e cammini.
>
> **Art. 6 (Copertura finanziaria).** 1. Agli oneri di cui all'articolo 5, pari a 20 milioni per il 2027 e a 50 milioni a decorrere dal 2028, si provvede mediante corrispondente riduzione degli stanziamenti del Ministero del turismo destinati alla promozione generica. 2. Dalle restanti disposizioni non derivano nuovi o maggiori oneri per la finanza pubblica.

**Cronoprogramma**
- *Primi 100 giorni:* Ministero del turismo e ISTAT definiscono l'indice di intensità turistica e l'indicatore di concentrazione su dati comunali, che sostituisce la stima TEHA non verificata; ddl presentato; avvio dell'intesa con ANCI e Regioni.
- *Entro 12 mesi:* legge approvata; decreto MEF sul tetto; pubblicazione dei dati CIN; Patto firmato in Conferenza unificata; primi Comuni con tariffe modulate dalla stagione 2028.
- *Entro fine legislatura:* tre stagioni osservate; valutazione ISTAT-Ministero; revisione del tetto e degli obiettivi del Patto.

**Indicatori**

| KPI | Base (dato, anno, fonte) | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Quota di presenze in luglio e agosto | 34,5%, 2024 (Eurostat tour_occ_nim) | ≤ 33,5% | ≤ 32,0% |
| Quota del gettito dell'imposta destinata ai servizi per la popolazione residente | non rilevata; gettito circa 1,0 mld, 2024 (stime JFC-IRPET, non ufficiali) | ≥ 50% nei Comuni aderenti, rendicontata | ≥ 50% in tutti i Comuni |
| Comuni ad alta intensità con tariffa modulata | 0, 2026 | 50 | 150 |

**Rischi e mitigazioni**
- *Perdita di competitività rispetto all'estero:* tetto nazionale ai livelli medi UE e progressività solo nei picchi.
- *Conflitto Stato-Regioni-Comuni:* intesa in Conferenza unificata; la modulazione è una facoltà, non un obbligo.
- *Gettito usato per la sola promozione:* vincolo del 50% e rendicontazione pubblica; sanzione sulla quota del Patto per chi non rendiconta.
- *Rottura della serie 2025:* KPI calcolati sulla serie ricostruita ISTAT o con base 2025 sul nuovo campo di osservazione.

---

*Le proposte che seguono nascono dal confronto sulla ricerca e l'innovazione nelle imprese (`benchmark/ricerca_innovazione.md`), 9 novembre 2026.*

## 01-P13 — Un solo credito per la ricerca: stabile, più forte per le piccole imprese, certificato prima di spendere

**Problema in un dato.** Le imprese italiane spendono in R&S lo **0,80% del PIL** contro l'1,50% UE (Eurostat, 2024). Il sostegno fiscale passa da due strumenti che si sovrappongono: il credito R&S (10%, **1.823 mln** l'anno) e il Nuovo patent box (deduzione maggiorata del 110%, **283 mln** l'anno tra IRES e IRAP) (MEF, Rapporto spese fiscali 2025). Il patent box va soprattutto alle imprese con almeno 500 addetti e ai settori a bassa intensità tecnologica (ISTAT, *Gli incentivi alle imprese per la R&S*, 2023). Le regole sono cambiate quasi ogni anno dal 2015 e i contenziosi sui crediti 2015-2019 sono stati così diffusi che lo Stato ha aperto una procedura di restituzione senza sanzioni (DL 146/2021, art. 5), riaperta fino al 3 giugno 2025 (numero di adesioni da verificare).

**Soluzione.** Un solo credito per la ricerca, con regole fisse per almeno cinque anni.
- **Aliquota.** Resta al 10% per tutte le imprese. Sale al **13%** per le imprese con meno di 50 addetti, dove l'effetto per euro speso è maggiore (OCSE, microBeRD; Dechezleprêtre et al. sul Regno Unito).
- **Giovani imprese.** Le imprese con meno di cinque anni e senza imposte da compensare ricevono il credito **in denaro** entro 90 giorni, fino a 200.000 € l'anno.
- **Certificazione prima di spendere.** L'impresa può chiedere a un certificatore iscritto all'Albo MIMIT, già esistente (art. 23 DL 73/2022, DPCM 15/9/2023), di certificare il **progetto prima di avviarlo**. La certificazione vincola l'Agenzia delle entrate sulla natura di R&S, salvo dati falsi. Sopra i 500.000 € di credito annuo la certificazione è obbligatoria. Si chiude così la stagione dei recuperi a distanza di anni.
- **Fine del patent box.** Il patent box si chiude in due anni: la maggiorazione scende al 50% per le spese 2027 e si azzera dal 2028. I risparmi pagano il credito più forte per le piccole imprese. È un riordino a parità di costo: le risorse restano alla ricerca, ma passano dalla deduzione sui beni immateriali, che premia soprattutto le grandi imprese, al credito sulla spesa.
- **Un portale, un testo unico.** Un solo portale MIMIT per comunicazioni e certificazioni. Un testo unico degli incentivi fiscali alla R&S. Le modifiche restrittive valgono solo per i periodi d'imposta che iniziano almeno 12 mesi dopo la legge.

L'iperammortamento (L. 199/2025) scade il 30 settembre 2028 e resta fuori da questa proposta. La sua maggiorazione base è già usata da 01-P4. Una eventuale proroga dovrebbe seguire le condizioni di 01-P4 e passare dalla valutazione di 01-P2.

| Variante | Contenuto | Costo 2027/28/29 → regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | Credito unico; 13% per le imprese sotto 50 addetti; rimborso in denaro alle giovani imprese; certificazione preventiva; patent box chiuso dal 2028 | 0,02 / 0,12 / 0,22 → **0,30** (2030) | 1 | SPESE_FISCALI 0,28 (chiusura del patent box); RIALLOCAZIONE 0,02 |
| ESSENZIALE | 12% per le imprese sotto 50 addetti; certificazione preventiva; patent box ridotto al 50% | 0,01 / 0,06 / 0,11 → **0,16** (2030) | 0,5 | SPESE_FISCALI 0,15 (patent box al 50%); RIALLOCAZIONE 0,01 |
| ZERO | Solo certificazione preventiva vincolante, portale unico, testo unico e regola dei cinque anni | 0,01 → **0,01** (2027) | 0,2 | RIALLOCAZIONE 0,01 |

*Come è costruito il costo (stima GovernAI).* Il credito R&S costa 1,823 mld (RSF 2025). Nel 2020 le imprese sotto i 50 addetti ne ricevevano il 42% (ISTAT 2023: il 58% andava alle imprese con almeno 50 addetti), cioè circa 0,77 mld su una spesa agevolata di circa 7,7 mld. Tre punti in più su questa spesa valgono 0,23 mld a comportamento invariato. Il rimborso alle giovani imprese vale circa 0,05 (stima, da verificare con i dati dell'Agenzia delle entrate). Portale, certificazione pubblica e controlli valgono 0,02. Totale 0,30. ESSENZIALE: due punti in più per 0,15, più 0,01 di gestione. Il credito si usa in tre quote annuali dall'anno dopo la spesa, quindi il costo arriva a regime nel 2030. *Ritmo delle coperture*: il patent box ridotto al 50% sulle spese 2027 fa risparmiare circa 0,15 nel 2028 (dichiarazioni 2027); dal 2029 il risparmio è pieno, circa 0,28 (RSF 2025: 244,5 mln IRES + 38,9 mln IRAP). Nel 2028-29 la copertura supera il costo. La quota delle imprese beneficiarie sotto i 50 addetti è un dato del 2020 e va aggiornata.

**Articolato normativo essenziale**

> **Art. 1 (Finalità).** Al fine di aumentare la spesa delle imprese in ricerca e sviluppo e di dare certezza alle regole, in attuazione degli articoli 9 e 41 della Costituzione, la presente legge riordina gli incentivi fiscali alla ricerca e sviluppo in un unico credito d'imposta stabile.
>
> **Art. 2 (Credito unico).** 1. All'articolo 1, comma 203, della legge 27 dicembre 2019, n. 160, dopo il primo periodo è inserito il seguente: «Per le imprese con meno di cinquanta addetti il credito è riconosciuto in misura pari al 13 per cento [ESSENZIALE: 12 per cento].» 2. Le imprese costituite da meno di cinque anni che non hanno imposte o contributi da compensare possono chiedere l'erogazione del credito in denaro, entro il limite di 200.000 euro annui. L'Agenzia delle entrate eroga il rimborso entro novanta giorni. *(Solo variante PIENA.)*
>
> **Art. 3 (Certificazione preventiva).** 1. La certificazione di cui all'articolo 23 del decreto-legge 21 giugno 2022, n. 73, può essere richiesta sul progetto prima dell'avvio delle attività. Salvo il caso di dati falsi o di progetto realizzato in modo difforme, la certificazione vincola l'Amministrazione finanziaria sulla qualificazione delle attività come ricerca e sviluppo. 2. La certificazione è obbligatoria per i crediti superiori a 500.000 euro annui. 3. Il Ministero delle imprese e del made in Italy pubblica ogni anno, in forma aggregata, i progetti certificati, i crediti, i controlli e gli esiti dei contenziosi.
>
> **Art. 4 (Chiusura del patent box).** 1. La maggiorazione di cui all'articolo 6, comma 3, del decreto-legge 21 ottobre 2021, n. 146, è ridotta al 50 per cento per le spese sostenute nel periodo d'imposta 2027 ed è soppressa per le spese sostenute dal periodo d'imposta 2028 [ESSENZIALE: è ridotta al 50 per cento dal periodo d'imposta 2027]. 2. Dal 1° gennaio 2027 non possono essere esercitate nuove opzioni.
>
> **Art. 5 (Stabilità delle regole).** 1. Entro dodici mesi il Governo adotta un testo unico degli incentivi fiscali alla ricerca e sviluppo. 2. Le modifiche che riducono il beneficio si applicano solo ai periodi d'imposta che iniziano almeno dodici mesi dopo l'entrata in vigore della norma che le dispone. 3. Comunicazioni, prenotazioni e certificazioni passano per un unico portale del Ministero delle imprese e del made in Italy.
>
> **Art. 6 (Valutazione).** Ogni tre anni l'ISTAT e la Banca d'Italia valutano l'effetto del credito sulla spesa in R&S, sui brevetti e sulla produttività, con metodo controfattuale e dati dell'Agenzia delle entrate. La valutazione è pubblica e alimenta la scheda prevista dalla legge sulle spese fiscali a scadenza.
>
> **Art. 7 (Copertura finanziaria).** Agli oneri di cui all'articolo 2, pari a 120 milioni di euro per il 2028, 220 milioni per il 2029 e 300 milioni annui dal 2030, si provvede con le maggiori entrate derivanti dall'articolo 4. Agli oneri di cui agli articoli 3 e 5, pari a 20 milioni annui, si provvede mediante riduzione delle spese di funzionamento del Ministero delle imprese e del made in Italy.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | Norme in legge di bilancio 2027 (aliquota, patent box, certificazione); bozza del testo unico; dati dell'Agenzia delle entrate sulle imprese beneficiarie per classe di addetti | MEF, MIMIT, Agenzia delle entrate |
| 12 mesi | Portale unico e certificazione preventiva operativi; testo unico adottato; primi rimborsi alle giovani imprese | MIMIT, Agenzia delle entrate, certificatori |
| Fine legislatura | Regime pieno dal 2030; prima valutazione ISTAT-Banca d'Italia (2030) | ISTAT, Banca d'Italia, Parlamento |

**Indicatori**

| KPI | Base | 3 anni (2029) | 5 anni (2031) |
|---|---|---|---|
| Spesa in R&S delle imprese, % PIL | 0,80% (2024, Eurostat rd_e_gerdtot, BES) | 0,85% | 0,90% |
| Credito R&S coperto da certificazione preventiva | n.d. (certificazione oggi facoltativa e successiva) | 50% | 75% |
| Imprese sotto i 50 addetti che usano il credito R&S | n.d. (dato Agenzia delle entrate da pubblicare) | +20% | +35% |

**Rischi e mitigazione.** *Imprese che perdono il patent box* (grandi imprese, software, marchi già esclusi) → il credito unico resta pieno per loro al 10%; due anni di transizione; il risparmio resta nella ricerca. *Rischio di frodi con il rimborso in denaro* → tetto di 200.000 €, certificazione obbligatoria per il rimborso, controlli a campione. *Certificatori compiacenti* → responsabilità del certificatore, controlli MIMIT sui certificati e pubblicazione degli esiti. *Stima del costo incerta* (quote ISTAT del 2020) → limite di spesa annuo con monitoraggio dell'Agenzia delle entrate; se il costo supera la copertura, l'aliquota maggiorata si riduce per l'anno successivo. *Concorrenza fiscale con altri Paesi* che hanno patent box → secondo la letteratura il patent box sposta brevetti più che creare invenzioni (Gaessler, Hall e Harhoff 2021), quindi la perdita di attività reale attesa è limitata.

**Fonti.** MEF, Rapporto spese fiscali 2025 (misure 169 e 170, tabella di sintesi), https://www.mef.gov.it/export/sites/MEF/documenti-allegati/2025/RSF-2025-bis.pdf; OpenBDAP-RGS, Rendiconto 2025, cap. 7828 MEF (1.823 mln pagati); ISTAT, *Gli incentivi alle imprese per la ricerca e sviluppo*, 20/9/2023, https://www.istat.it/it/files//2023/09/Focus_incentivi_RS_DEFINITIVO.pdf; Banca d'Italia, QEF n. 898, dicembre 2024 (allineare l'aliquota alla media OCSE aumenterebbe la R&S privata di circa il 15%), https://www.bancaditalia.it/pubblicazioni/qef/2024-0898/; MEF-Banca d'Italia-MIMIT, *Piano Transizione 4.0: una valutazione*, sintesi maggio 2026, https://www.mimit.gov.it/images/stories/documenti/allegati/Sintesi_Valutazione_transizione_40_ITA_5_maggio_2026.pdf; UPB, Focus 1/2026 (iperammortamento: 8,4 mld di minor gettito di cassa 2027-2034), https://www.upbilancio.it/wp-content/uploads/2026/02/Focus-1_2026-LB.pdf; Albo dei certificatori MIMIT, https://www.mimit.gov.it/it/notizie-stampa/mimit-da-oggi-online-lalbo-dei-certificatori-del-credito-dimposta-in-attivita-di-ricerca-e-sviluppo-innovazione-tecnologica-design-e-ideazione-estetica. Da verificare: se i crediti per innovazione tecnologica e design (5%, in vigore fino al 2025) sono stati prorogati e quanto pesano nei 1.823 mln.

---

## 01-P14 — "Sfide Italia": la pubblica amministrazione compra innovazione in tre fasi

**Problema in un dato.** Dal 2019 il programma nazionale di appalti innovativi (Smarter Italy) ha avuto circa **93 milioni €** in tutto: 50 dal MISE e 43,4 dal MUR (AgID). Nel 2026 il Consiglio UE raccomanda all'Italia di **"rafforzare gli appalti per l'innovazione"** (Raccomandazione del 10 luglio 2026, punto 3). Manca anche una misura nazionale coerente della spesa pubblica in innovazione (CNR, PPI4MED, 2024).

**Soluzione.** Le amministrazioni centrali pubblicano ogni anno delle **sfide**: problemi concreti per cui non esiste ancora una soluzione sul mercato (ad esempio diagnosi precoce nelle Case della Comunità, monitoraggio di ponti e frane, riduzione dei consumi negli edifici pubblici). Le imprese competono in tre fasi, sul modello SBIR statunitense e SBRI britannico.
- **Fase 1, fattibilità:** fino a 80.000 € per 6 mesi, a più imprese per ogni sfida.
- **Fase 2, prototipo:** fino a 1,5 milioni € per 18-24 mesi, alle migliori della fase 1.
- **Fase 3, acquisto:** l'amministrazione compra la soluzione che funziona con gli ordinari fondi di acquisto, anche tramite Consip.

Le imprese mantengono i diritti di proprietà intellettuale; lo Stato ha una licenza d'uso gratuita. Le regole sono quelle degli appalti pre-commerciali UE e del partenariato per l'innovazione (art. 75 d.lgs. 36/2023). AgID resta la centrale di committenza; un comitato tecnico con MIMIT e MUR sceglie le sfide. Ogni ministero con grandi acquisti di beni e servizi propone almeno una sfida l'anno. Il 60% dei contratti di fase 1 va a PMI.

| Variante | Contenuto | Costo 2027/28/29 → regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | Circa 40 sfide l'anno: 500 contratti di fase 1 e 100 di fase 2 | 0,03 / 0,08 / 0,15 → **0,20** (2030) | 1 | RIALLOCAZIONE 0,12 (acquisti delle amministrazioni proponenti); COESIONE_2834 0,08 (FESR, ricerca e innovazione) |
| ESSENZIALE | Circa 15 sfide l'anno, solo salute, territorio ed energia | 0,01 / 0,04 / 0,06 → **0,08** (2030) | 0,45 | RIALLOCAZIONE 0,05; COESIONE_2834 0,03 |
| PILOTA | 3 sfide con valutazione, 2027-2029 | 0,01 / 0,03 / 0,03 → 0,03 (2028) | 0,15 | COESIONE_2127 0,03 (FESR, temporaneo) |

*Nota del coordinamento (9 novembre 2026): le quote indicate su COESIONE_2834 sono contate come RIALLOCAZIONE, perché nel registro dei fondi COESIONE_2834 ha capienza minima zero e non è una copertura certa. Se i fondi di coesione 2028-34 saranno assegnati, potranno sostituire la riallocazione.*

*Come è costruito il costo (stima GovernAI)*: fase 1, 500 contratti × 80.000 € = 0,04; fase 2, 100 contratti × 1,5 milioni € = 0,15; gestione AgID e valutazione 0,01. Totale 0,20 l'anno. La fase 3 non è un costo aggiuntivo: sostituisce acquisti che l'amministrazione farebbe comunque. ESSENZIALE: 200 × 80.000 € = 0,016; 40 × 1,5 milioni € = 0,06; gestione 0,005. Totale 0,08. *Ritmo delle coperture nella PIENA*: COESIONE_2127 (FESR 2021-27, obiettivo "Europa più intelligente") 0,03 / 0,05 / 0,07 nel 2027-29; RIALLOCAZIONE 0 / 0,03 / 0,08; dal 2030 RIALLOCAZIONE 0,12 e COESIONE_2834 0,08. Nessun personale stabile è pagato con fondi di coesione.

**Articolato normativo essenziale**

> **Art. 1 (Finalità).** Al fine di usare la domanda pubblica per stimolare l'innovazione delle imprese e migliorare i servizi pubblici, in attuazione degli articoli 9 e 97 della Costituzione, è istituito il programma "Sfide Italia" per gli appalti pre-commerciali e per l'innovazione.
>
> **Art. 2 (Sfide).** 1. Ogni anno le amministrazioni centrali dello Stato con una spesa per acquisto di beni e servizi superiore a 100 milioni di euro propongono almeno una sfida. 2. Un comitato tecnico composto da AgID, Ministero delle imprese e del made in Italy e Ministero dell'università e della ricerca seleziona le sfide in base all'utilità pubblica, all'assenza di soluzioni sul mercato e all'impegno dell'amministrazione ad acquistare la soluzione.
>
> **Art. 3 (Fasi).** 1. Ogni sfida si svolge in tre fasi: fattibilità, fino a 80.000 euro per contratto; prototipo e prova sul campo, fino a 1,5 milioni di euro per contratto; acquisto della soluzione. 2. Le fasi di fattibilità e prototipo sono affidate come servizi di ricerca e sviluppo secondo la disciplina europea degli appalti pre-commerciali, o con il partenariato per l'innovazione di cui all'articolo 75 del decreto legislativo 31 marzo 2023, n. 36. 3. I diritti di proprietà intellettuale restano all'impresa. L'amministrazione ha una licenza d'uso gratuita e non esclusiva. 4. Almeno il 60 per cento dei contratti di fattibilità è riservato alle micro, piccole e medie imprese.
>
> **Art. 4 (Acquisto).** L'amministrazione proponente indica, al momento della sfida, le risorse per l'acquisto della soluzione nella fase 3. Se non acquista una soluzione che ha superato la prova sul campo, ne dà motivazione pubblica.
>
> **Art. 5 (Trasparenza e valutazione).** AgID pubblica in formato aperto sfide, partecipanti, contratti, esiti e acquisti. Dopo cinque anni la Corte dei conti e un valutatore indipendente misurano la crescita delle imprese partecipanti rispetto alle imprese non selezionate con punteggi vicini.
>
> **Art. 6 (Copertura finanziaria).** Agli oneri, pari a 30 milioni di euro per il 2027, 80 milioni per il 2028, 150 milioni per il 2029 e 200 milioni annui dal 2030 [ESSENZIALE: 10, 40, 60 e 80 milioni], si provvede: a) per il triennio 2027-2029, a valere sui programmi FESR 2021-2027, obiettivo strategico 1, previa riprogrammazione, e mediante riduzione delle autorizzazioni di spesa per acquisto di beni e servizi delle amministrazioni proponenti, indicate in allegato; b) dal 2030, per 120 milioni [ESSENZIALE: 50] mediante le medesime riduzioni e per la parte restante a valere sulla programmazione 2028-2034.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | Norma in legge di bilancio; riprogrammazione FESR; prime 10 sfide raccolte dai ministeri (salute, protezione civile, energia, trasporti) | MIMIT, MUR, AgID, Dipartimento coesione |
| 12 mesi | Primi bandi di fase 1; piattaforma aperta dei risultati; linee guida sulla proprietà intellettuale | AgID, amministrazioni proponenti |
| Fine legislatura | Primi prototipi in prova; prime acquisizioni di fase 3; valutazione intermedia (2030) | AgID, Corte dei conti, valutatore indipendente |

**Indicatori**

| KPI | Base | 3 anni (2029) | 5 anni (2031) |
|---|---|---|---|
| Valore dei contratti pre-commerciali e per l'innovazione aggiudicati nell'anno | circa 93 mln in tutto nel 2019-2025 (Smarter Italy, AgID; dato annuo n.d.) | 150 mln | 200 mln |
| Soluzioni di fase 2 acquistate da una PA entro 2 anni | n.d. | 25% | 40% |
| Quota di PMI tra le imprese vincitrici di fase 1 | n.d. | ≥60% | ≥60% |

**Rischi e mitigazione.** *Sfide inventate per spendere* → impegno ad acquistare e motivazione pubblica in caso di mancato acquisto. *Amministrazioni senza competenze di gara* → AgID come centrale di committenza unica, collegamento con il personale tecnico di 09-C3. *Aiuti di Stato* → prezzi di mercato e procedure competitive, come prevede la disciplina UE sugli appalti pre-commerciali. *Effetto sugli acquisti ordinari* (la riduzione degli stanziamenti) → riguarda le stesse amministrazioni che ricevono le soluzioni; da tenere distinta dai risparmi sugli acquisti centralizzati (RA01) per non contarli due volte. *Coesione dopo il 2029* → RIALLOCAZIONE prevalente a regime; se il ciclo 2028-34 non conferma le risorse si scende alla ESSENZIALE.

**Fonti.** Consiglio UE, Raccomandazione all'Italia del 10/7/2026 (CELEX 32026H03925), in `europa/semestre.md`; AgID, Smarter Italy (50 mln MISE 2019, 43,4 mln MUR), https://www.agid.gov.it/it/agenzia/stampa-e-comunicazione/notizie/2020/05/04/covid-19-appalti-innovativi-il-rilancio-del-paese.html; Howell, S., *Financing Innovation: Evidence from R&D Grants*, American Economic Review 107(4), 2017 (un contributo di fase 1 SBIR raddoppia circa la probabilità di ricevere venture capital), https://econpapers.repec.org/RePEc:aea:aecrev:v:107:y:2017:i:4:p:1136-64; Commissione UE, benchmarking degli appalti per l'innovazione 2024, https://research-and-innovation.ec.europa.eu/strategy/support-policy-making/shaping-eu-research-and-innovation-policy/new-european-innovation-agenda/innovation-procurement/benchmarking-innovation-procurement-investments-and-policy-frameworks-across-europe_en; CNR, PPI4MED White Paper, https://www.enicbcmed.eu/sites/default/files/2024-01/PPI4MED_WhitePaper_CNR.pdf; d.lgs. 36/2023, art. 75. Da verificare: il valore italiano degli appalti per l'innovazione nel benchmarking UE 2024; la norma nazionale di recepimento dell'esclusione dei servizi di R&S (art. 14 direttiva 2014/24/UE).

---

## 01-P15 — Dalla scoperta all'impresa: prove di fattibilità, regole chiare per gli spin-off, fondo di fondi deep tech

**Problema in un dato.** Nel 2023 università ed enti pubblici di ricerca hanno creato **86 spin-off**, contro le 108 del 2022, e incassato **5,87 milioni €** da licenze attive, con 470 addetti equivalenti a tempo pieno negli uffici di trasferimento tecnologico (Netval, 20° Rapporto, 2025). Il venture capital investe circa **1,5 mld €** nel 2025, lo **0,07% del PIL**, contro lo 0,22% della Francia e lo 0,15% della Germania (EY, VC Barometer 2025; Bain 2026: fonti private, non ufficiali). Il Consiglio UE chiede all'Italia di sostenere "il ruolo degli investitori aziendali e istituzionali nel venture capital" (Raccomandazione 2026, punto 3).

**Soluzione.** Tre strumenti lungo la stessa filiera.
- **Prove di fattibilità (proof of concept).** Un bando annuale e stabile finanzia 250-300 progetti l'anno, da 50.000 a 150.000 €, per portare un brevetto pubblico a un prototipo. Riunisce i bandi PoC e UTT oggi a singhiozzo dell'Ufficio brevetti (cap. 7476 MIMIT).
- **Regole chiare per gli spin-off.** Un regolamento tipo nazionale: quota dell'ateneo nel capitale tra il 5% e il 10%, licenza standard con royalty bassa o in cambio di quote, decisione entro 60 giorni, congedo fino a tre anni per chi fa ricerca e fonda l'impresa, con diritto di rientro.
- **Fondo di fondi deep tech.** CDP Venture Capital, con il Fondo europeo per gli investimenti (FEI), gestisce un fondo di fondi da **1,5 mld €** in cinque anni. Investe in fondi di venture capital su tecnologie avanzate (materiali, scienze della vita, energia, quantistica, AI applicata), solo se **almeno il 60%** dei capitali viene da privati: casse previdenziali, fondi pensione, assicurazioni, fondazioni. Lo Stato mette una **quota di prima perdita** di 300 milioni in cinque anni: assorbe le prime perdite e lascia ai privati una parte maggiore dei guadagni. È il modello israeliano Yozma e del programma francese Tibi, adattato. I fondi selezionati devono investire in Italia almeno il doppio di quanto ricevono dal fondo pubblico.

| Variante | Contenuto | Costo 2027/28/29 → regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | Fondo di fondi da 1,5 mld (prima perdita pubblica 300 mln in 5 anni) + 250-300 prove di fattibilità l'anno + regole spin-off | 0,05 / 0,10 / 0,10 → **0,10** (2028) | 1 | RIALLOCAZIONE 0,06 (bandi PoC/UTT e Fondo crescita sostenibile); COESIONE_2834 0,04 (strumenti finanziari FESR) |
| ESSENZIALE | Fondo di fondi da 750 mln (prima perdita 150 mln) + 130 prove di fattibilità l'anno + regole spin-off | 0,03 / 0,05 / 0,05 → **0,05** (2028) | 0,5 | RIALLOCAZIONE 0,03; COESIONE_2834 0,02 |
| ZERO | Solo regolamento tipo per gli spin-off e congedo per chi fa ricerca e fonda un'impresa | 0 → **0** (2027) | 0,2 | — |

*Nota del coordinamento (9 novembre 2026): le quote indicate su COESIONE_2834 sono contate come RIALLOCAZIONE, perché nel registro dei fondi COESIONE_2834 ha capienza minima zero e non è una copertura certa. Se i fondi di coesione 2028-34 saranno assegnati, potranno sostituire la riallocazione.*

*Come è costruito il costo (stima GovernAI)*: quota di prima perdita 300 mln in cinque rate annue = 0,06; prove di fattibilità, circa 270 × 150.000 € in media = 0,04 (in parte già finanziate dai bandi PoC e UTT MIMIT-UIBM sul cap. 7476, 43,8 mln iniziali nel 2025, OpenBDAP). Totale 0,10. La quota di CDP Venture Capital (circa 0,30 mld su 1,5) è un investimento di una società fuori dal perimetro della PA e non pesa sul bilancio; la quota del FEI è europea. Per prudenza tutta la prima perdita è trattata come spesa, anche se una parte potrebbe essere classificata come operazione finanziaria (da verificare con ISTAT ed Eurostat). ESSENZIALE: 0,03 + 0,02 = 0,05. *Ritmo delle coperture nella PIENA*: COESIONE_2127 0,04 l'anno nel 2027-29 (strumenti finanziari FESR per prove di fattibilità e investimenti seed nelle regioni meno sviluppate); RIALLOCAZIONE 0,01 / 0,06 / 0,06; dal 2030 RIALLOCAZIONE 0,06 e COESIONE_2834 0,04. Il programma dura cinque anni (2027-2031); poi si decide se rifinanziarlo in base ai rendimenti, che rientrano al fondo.

**Articolato normativo essenziale**

> **Art. 1 (Finalità).** Al fine di trasformare i risultati della ricerca pubblica in nuove imprese e di attrarre capitale privato verso le tecnologie avanzate, in attuazione degli articoli 9, 41 e 47 della Costituzione, la presente legge istituisce il programma nazionale per le prove di fattibilità, il regolamento tipo per gli spin-off e il fondo di fondi deep tech.
>
> **Art. 2 (Prove di fattibilità).** 1. Il Ministero delle imprese e del made in Italy, d'intesa con il Ministero dell'università e della ricerca, pubblica ogni anno, a data fissa, un bando per progetti di prova di fattibilità di università, enti pubblici di ricerca e IRCCS, di importo compreso tra 50.000 e 150.000 euro. 2. Nel bando confluiscono le risorse delle misure per la valorizzazione dei brevetti e per gli uffici di trasferimento tecnologico.
>
> **Art. 3 (Spin-off).** 1. Entro sei mesi il Ministro dell'università e della ricerca adotta un regolamento tipo per le imprese spin-off. Il regolamento prevede: una partecipazione dell'ente non superiore al 10 per cento, salvo diverso accordo motivato; un contratto di licenza standard; una decisione entro sessanta giorni dalla domanda. 2. Il personale di ricerca che fonda o lavora in uno spin-off può chiedere un congedo fino a tre anni, con diritto alla conservazione del posto. 3. Gli enti che non adottano un proprio regolamento applicano il regolamento tipo.
>
> **Art. 4 (Fondo di fondi deep tech).** 1. CDP Venture Capital SGR istituisce, anche con il Fondo europeo per gli investimenti, un fondo di fondi dedicato alle tecnologie avanzate, con una dotazione obiettivo di 1,5 miliardi di euro in cinque anni [ESSENZIALE: 750 milioni]. 2. Il fondo investe in fondi di venture capital solo se almeno il 60 per cento dei loro capitali proviene da investitori privati, e a condizione che investano in imprese con sede o attività di ricerca in Italia almeno il doppio dell'importo ricevuto. 3. Lo Stato sottoscrive una quota di prima perdita fino a 300 milioni di euro [ESSENZIALE: 150 milioni] in cinque anni, che assorbe le prime perdite e riconosce agli investitori privati una quota maggiore dei rendimenti. I rendimenti spettanti allo Stato tornano al fondo.
>
> **Art. 5 (Trasparenza e valutazione).** CDP Venture Capital pubblica ogni anno i fondi sottoscritti, i capitali privati raccolti, le imprese finanziate e gli esiti. Dopo cinque anni la Banca d'Italia valuta il programma confrontando le imprese finanziate con imprese simili non finanziate.
>
> **Art. 6 (Copertura finanziaria).** Agli oneri, pari a 50 milioni di euro per il 2027 e a 100 milioni annui dal 2028 al 2031 [ESSENZIALE: 30 e 50 milioni], si provvede: a) per 40 milioni annui nel triennio 2027-2029, a valere sui programmi FESR 2021-2027, mediante strumenti finanziari; b) per la parte restante mediante corrispondente riduzione delle autorizzazioni di spesa di cui al capitolo 7476 e del Fondo per la crescita sostenibile; c) dal 2030 per 40 milioni a valere sulla programmazione 2028-2034.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | Norma in legge di bilancio; regolamento tipo in consultazione con CRUI e Netval; negoziato CDP VC-FEI sul fondo di fondi; primo bando PoC a data fissa | MIMIT, MUR, CDP VC, FEI |
| 12 mesi | Regolamento tipo adottato; prima chiusura del fondo di fondi con le casse previdenziali; primi 250 progetti PoC | MUR, CDP VC, enti di ricerca |
| Fine legislatura | Cinque annate di investimenti; prima valutazione Banca d'Italia (2031) | CDP VC, Banca d'Italia |

**Indicatori**

| KPI | Base | 3 anni (2029) | 5 anni (2031) |
|---|---|---|---|
| Investimenti di venture capital in Italia, % PIL | 0,07% (2025, EY, fonte non ufficiale) | 0,10% | 0,13% |
| Spin-off costituite da università ed enti pubblici di ricerca nell'anno | 86 (2023, Netval 2025) | 110 | 130 |
| Capitale privato raccolto dai fondi sottoscritti per ogni euro pubblico (Stato + CDP) | n.d. (misura nuova) | ≥1,5 | ≥1,5 |

**Rischi e mitigazione.** *Il fondo pubblico sostituisce i privati invece di attirarli* → almeno il 60% privato per ogni fondo; la letteratura trova effetti positivi soprattutto quando il capitale pubblico accompagna quello privato (Brander, Du e Hellmann 2015). *Prima perdita come regalo ai privati* → tetto di 300 mln, gestori selezionati con gara, rendimenti pubblici che tornano al fondo. *Spin-off "di facciata"* → indicatore sulle spin-off ancora attive dopo cinque anni e con ricavi. *Doppio conteggio con 01-P4 e RA04* (incentivi MIMIT a bassa addizionalità) → la riduzione del Fondo per la crescita sostenibile è aggiuntiva a quelle di 01-P4 e RA04 e va verificata dall'agente coperture. *Classificazione statistica* → prudenzialmente tutto a deficit, quindi tutto coperto.

**Fonti.** Netval, 20° Rapporto, 2025, https://www.iris.santannapisa.it/retrieve/bfef2339-d16a-48ff-8362-d845383e7898/rapportonetval2025-e64d.pdf; EY, Venture Capital Barometer 2025 (via StartupItalia), https://startupitalia.eu/startup/ey-venture-capital-barometer-2025-italia/; Bain & Company, comunicato 2026, https://www.bain.com/it/about-bain/media-center/press-releases/italy/2023222/Venture-capital-in-italia-il-2025-e-un-anno-record-sostenuto-dai-mega-deal/; CDP Venture Capital, Piano strategico 2024-2028 (8 mld in gestione, fondo deep tech 500 mln), https://www.cdpventurecapital.it/resources/cms/documents/PianoStrategico_2428.pdf; FEI, European Tech Champions Initiative, https://www.eif.org/etci/index.htm; Brander, Du, Hellmann, *The Effects of Government-Sponsored Venture Capital: International Evidence*, Review of Finance 2015; OpenBDAP-RGS, Rendiconto 2025, capp. 7476 e 7483 MIMIT, 7344 (Fondo venture capital, 5 mln). Da verificare: classificazione Eurostat della quota di prima perdita; stato dell'adesione italiana a ETCI 2.0 e allo Scaleup Europe Fund.
