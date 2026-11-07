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

**Soluzione.** Ogni spesa fiscale riceve una data di scadenza, scaglionata in 5 anni. Una Commissione indipendente pubblica per ciascuna una scheda (costo, beneficiari per decile, efficacia) e il Parlamento la rinnova solo con un voto esplicito e una copertura. È il metodo per conseguire i 7,37 mld già nel Piano, non una risorsa aggiuntiva: il gettito oltre quella soglia va al menu coperture.

**Varianti**

| Variante | Contenuto | Costo a regime | Intensità |
|---|---|---|---|
| PIENA | scadenza per tutte le 573 misure; esenti dalla scadenza (non dalla valutazione) salute, disabilità, famiglia, obblighi UE | 0,01 (RIALLOCAZIONE) | 1 |
| ESSENZIALE | scadenza per le misure nuove o prorogate e per la metà meno valutata dello stock | 0,01 | 0,6 |
| ZERO | solo scheda di valutazione obbligatoria, senza scadenza | 0 | 0,3 |

**Articolato normativo essenziale** (legge delega; decreto legislativo entro 12 mesi)

> **Art. 1 (Finalità).** 1. Al fine di assicurare l'efficacia, l'equità e la trasparenza delle spese fiscali e di conseguire gli obiettivi di riordino previsti dal Piano strutturale di bilancio di medio termine, il Governo è delegato ad adottare, entro dodici mesi, uno o più decreti legislativi secondo i principi e criteri direttivi di cui agli articoli 2 e 3.
>
> **Art. 2 (Clausola di scadenza).** 1. Ciascuna spesa fiscale censita nel rapporto di cui all'articolo 21, comma 11-bis, della legge 31 dicembre 2009, n. 196, cessa di avere efficacia al termine del quinto periodo d'imposta successivo all'entrata in vigore del decreto legislativo, secondo un calendario che distribuisce le scadenze in cinque annualità e pone per prime le misure con minor numero di beneficiari o prive di valutazione. 2. Le spese fiscali introdotte o prorogate dopo l'entrata in vigore della presente legge hanno durata non superiore a cinque anni. 3. Sono escluse dalla cessazione automatica, ma non dalla valutazione, le agevolazioni relative a spese sanitarie, disabilità, carichi familiari e quelle che attuano obblighi dell'Unione europea.
>
> **Art. 3 (Valutazione e rinnovo).** 1. La Commissione per la redazione del rapporto annuale sulle spese fiscali è integrata da esperti indipendenti e dotata di una segreteria tecnica; accede ai dati dell'Agenzia delle entrate in forma anonimizzata, nel rispetto del regolamento (UE) 2016/679. 2. Per ogni misura in scadenza pubblica, almeno dodici mesi prima, una scheda su costo, beneficiari per decile di reddito e territorio, efficacia rispetto all'obiettivo e alternative. 3. Il rinnovo è disposto con norma specifica, votata separatamente e munita di copertura ai sensi dell'articolo 17 della legge n. 196 del 2009.
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

**Problema in un dato.** Il **60,0%** degli occupati lavora in imprese con meno di 50 addetti, contro il 41,6% in Francia e il 39,4% in Germania (Eurostat sbs_sc_ovw, 2024; `01_quota_occupati_micro_piccole`). La produttività del lavoro è cresciuta dello 0,3% l'anno nel 1995-2024, contro l'1,5% dell'UE27 (ISTAT, dicembre 2025); l'indice del PIL per ora lavorata è a 100,4 nel 2025 (2015=100; Eurostat nama_10_lp_ulc).

**Soluzione.** Chi supera 15 o 50 addetti ha tre anni per adeguarsi agli obblighi amministrativi; salute, sicurezza e diritti sindacali restano pieni da subito. Un premio di crescita, con tetto annuo, va solo alle imprese tra 10 e 49 addetti che crescono, si fondono o fanno rete. Il costo scende da 2,5 a 0,6 mld, finanziato rimodulando la parte generica dell'iperammortamento.

**Varianti**

| Variante | Contenuto | Costo a regime (fondi) | Intensità |
|---|---|---|---|
| PIENA | come nel dossier, incentivi per tutte le imprese | 2,5 (SPESE_FISCALI) | 1 |
| **ESSENZIALE (raccomandata)** | soglie graduali a 15 e 50 + premio solo 10-49 addetti con tetto + sportello unico | 0,6 (SPESE_FISCALI 0,4; RIALLOCAZIONE 0,2) | 0,5 |
| ZERO | solo soglie graduali e sportello unico | 0,01 (RIALLOCAZIONE) | 0,25 |

La variante ESSENZIALE prende la parte a costo zero, cioè la graduazione delle soglie, e concentra l'incentivo dove l'effetto soglia è più forte. Realizza metà dell'effetto con un quarto del costo.

**Articolato normativo essenziale** (disegno di legge; premio in legge di bilancio)

> **Art. 1 (Finalità).** 1. Al fine di favorire la crescita dimensionale, l'aggregazione e la produttività delle micro e piccole imprese, senza ridurre i diritti dei lavoratori, la presente legge gradua gli obblighi amministrativi connessi alle soglie occupazionali e istituisce un premio di crescita.
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
| Quota di occupati in imprese con meno di 50 addetti | 60,0%, 2024 (Eurostat sbs_sc_ovw) | ≤ 59,3% | ≤ 58,5% |
| Valore aggiunto per addetto dei beneficiari rispetto al gruppo di controllo | 0, 2026 (avvio) | +3% | +5%, significativo |
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

**Soluzione.** I Comuni ad alta intensità turistica possono modulare l'imposta di soggiorno per stagione e zona, entro un tetto nazionale e con riduzioni obbligatorie in bassa stagione. Almeno metà del gettito va per legge a casa, trasporti e servizi per i residenti, e i dati CIN sugli affitti brevi diventano pubblici. Un patto Stato-Regioni premia chi sposta presenze fuori stagione e nelle aree interne.

**Varianti**

| Variante | Contenuto | Costo per lo Stato a regime | Intensità |
|---|---|---|---|
| PIENA | modulazione, vincolo 50%, dati CIN, patto, credito di riqualificazione condizionato | 0,15 (RIALLOCAZIONE, Fondo turismo) | 1 |
| **ESSENZIALE (raccomandata)** | modulazione, vincolo 50%, dati CIN, patto da 50 mln legato a obiettivi | 0,05 | 0,65 |
| ZERO | solo norma su modulazione, vincolo e dati CIN | 0 | 0,4 |

Gettito comunale aggiuntivo stimato in 0,3-0,8 mld/anno (fondo TASSA_SOGGIORNO, entrata dei Comuni vincolata: non finanzia spesa statale).

**Articolato normativo essenziale** (disegno di legge, modifica dell'art. 4 del d.lgs. 23/2011; intesa in Conferenza unificata)

> **Art. 1 (Finalità).** 1. Al fine di distribuire nel tempo e nello spazio i flussi turistici e di destinare ai residenti una quota dei benefici del turismo, la presente legge modifica la disciplina dell'imposta di soggiorno e istituisce il Patto nazionale per la destagionalizzazione.
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
| Quota del gettito dell'imposta destinata ai servizi per i residenti | non rilevata; gettito circa 1,0 mld, 2024 (stime JFC-IRPET, non ufficiali) | ≥ 50% nei Comuni aderenti, rendicontata | ≥ 50% in tutti i Comuni |
| Comuni ad alta intensità con tariffa modulata | 0, 2026 | 50 | 150 |

**Rischi e mitigazioni**
- *Perdita di competitività rispetto all'estero:* tetto nazionale ai livelli medi UE e progressività solo nei picchi.
- *Conflitto Stato-Regioni-Comuni:* intesa in Conferenza unificata; la modulazione è una facoltà, non un obbligo.
- *Gettito usato per la sola promozione:* vincolo del 50% e rendicontazione pubblica; sanzione sulla quota del Patto per chi non rendiconta.
- *Rottura della serie 2025:* KPI calcolati sulla serie ricostruita ISTAT o con base 2025 sul nuovo campo di osservazione.
