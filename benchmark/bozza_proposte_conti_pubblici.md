*Bozza scritta da un agente AI il 15 novembre 2026; da valutare con il panel e da approvare; non rivista da una persona.*

# Bozza di schede: conti pubblici, pensioni, lavoro (dalle idee A, B, C, E, F, G)

Fonte delle idee: `benchmark/conti_pubblici_nord_europa_spagna.md`, sezione 4. L'idea D (revisioni "a opzioni" con variante -20%) non è stata scelta e non è trattata qui.

Varianti in `benchmark/bozza_varianti_conti_pubblici.csv`. Copertura nuova in `benchmark/bozza_coperture_conti_pubblici.csv`. Importi in mld €/anno, salvo diversa indicazione. "Stima GovernAI" vuol dire stima propria, senza quantificazione ufficiale. "Da verificare" vuol dire cifra o norma non riscontrata sul testo originale.

**Questa bozza non dà punteggi sui valori.** Li daranno tre valutatori indipendenti con `motore/rubrica.md`. Per lo stesso motivo le colonne dei valori (RIS ... CIT) nel CSV delle coperture sono vuote.

## 0. Come sono state classificate le idee

| Idea | Tipo | Id proposto | Rapporto con il programma in uso | Costo a regime (PIENA / ESSENZIALE / PILOTA o ZERO) |
|---|---|---|---|---|
| A. Tetti di spesa per ministero, riserva, entrate inattese | **nuova** (regola di procedura) | **01-P16** | Rafforza l'art. 22-bis L. 196/2009, già usato da RA13. Non è una copertura: non produce gettito proprio | 0,003 / 0,002 / ZERO 0 |
| B + C. UPB più forte e analisi dei programmi elettorali | **nuova**, con C come componente separabile | **01-P17** | Si integra con 01-P1, 02-C3 art. 5, 04-P4, 08-P1 (altre funzioni UPB): un solo disegno di legge "UPB" | 0,006 / 0,0025 / PILOTA 0,0005; ZERO 0 |
| E. Protezione dell'aggancio e correttore sulle pensioni | **nuova** per il correttore; **integrazione di 02-C3** per la protezione dell'aggancio | **02-C8** | La parte 1 entra nel testo di 02-C3 (nuovo art. 2-bis). Il correttore usa il disegno di PE04 e non si somma a PE04 | 0 / 0 / ZERO 0. Risparmio solo eventuale, **non copertura** |
| F. Politiche attive dopo il PNRR | **nuova** | **02-C9** | Nessuna misura simile nel programma. Coerente con 02-C4 art. 5 (case manager) | 0,45 / 0,20 / PILOTA 0,03 |
| F (copertura). Riduzione degli incentivi all'assunzione senza effetto dimostrato | **copertura**, livello 2 | **RA15** | Perimetro distinto da RA04 e RA14 (incentivi alle imprese). Al netto della quota già usata da 02-C1 | gettito 0,15-0,35 dal 2030 |
| G. Registro mensile dei redditi Entrate-INPS | **rafforzamento di 01-P7** (con 09-C2 e 02-C4 art. 3) | **01-P18** | Funziona solo se c'è 01-P7 o 02-C4. Scheda e costo separati, perché va valutato a parte | picco 0,04 (regime 0,015) / picco 0,025 (regime 0,01) / PILOTA 0,005 |

**Verifica degli id (15/11/2026).** Ricerca su tutti i file `.md`, `.csv`, `.yaml`, `.py`, `.js`, `.json` del repository: sono usati 01-P1...01-P15, 02-C1...02-C7, RA01...RA14, RP01...RP08, PE01...PE04. Gli id 01-P16, 01-P17, 01-P18, 02-C8, 02-C9 e RA15 sono liberi.

**Regole applicate (come nelle schede di `programma/schede/`).**
- Nessuna variante usa DEFICIT, RISPARMI_ATTESI, IVA_EVASIONE, ETS o ALTRO.
- I risparmi non certificati non coprono nulla: né quelli delle revisioni della spesa (01-P17), né quelli del correttore (02-C8), né le prestazioni non pagate per errore (01-P18), né i minori sussidi grazie alle politiche attive (02-C9).
- Il fondo RIALLOCAZIONE è già oltre la capienza (4,41 contro 2,49 mld secondo i verbali del 8/11/2026, `governo/verbali/2026-11-08.md`). Le schede 01-P16, 01-P17 e 01-P18 costano pochi milioni, ma pesano comunque su quel fondo. 02-C9 lo usa solo tramite la copertura nuova RA15.

**Righe proposte per `motore/proposte.csv`** (formato `proposta_id,titolo,costo_min,costo_max,costo_opportunita`; da aggiungere solo dopo l'approvazione):

```
01-P16,"Tetti di spesa triennali per ministero, con riserva e regola sulle entrate inattese",0.0,0.003,0.0
01-P17,"UPB più forte: revisioni della spesa indipendenti, rispetta o spiega, analisi volontaria dei programmi elettorali",0.0,0.006,0.0
01-P18,"Registro mensile dei redditi Entrate-INPS per conto fiscale e prestazioni",0.005,0.04,0.0
02-C8,"Aggancio protetto e correttore automatico e temporaneo sulla spesa pensionistica",0.0,0.0,0.0
02-C9,"Politiche attive dopo il PNRR: nucleo minimo di GOL",0.03,0.45,0.0
```

---

## 01-P16 — Tetti di spesa triennali per ministero, con riserva e regola sulle entrate inattese

**Tipo.** Proposta nuova. Non duplica nulla: RA13 è una copertura (un obiettivo di risparmio), l'art. 22-bis della L. 196/2009 fissa obiettivi di spesa per ministero ma non un tetto alla spesa totale di ciascuno (portata dell'art. 22-bis vigente **da verificare** sul testo). 01-P16 trasforma quegli obiettivi in tetti e dà a RA13 e RP01 una cornice stabile.

**Problema in un dato.** Nel 2025 la spesa netta è cresciuta dell'**1,5%** contro un tetto dell'**1,3%** (Commissione UE, citata nella raccomandazione del Consiglio del 10/7/2026, `europa/semestre.md`). La deviazione cumulata è dello **0,1% del PIL, circa 2,4 mld** (UPB, `dati/verifiche/00_vincolo_bilancio.md`). Il tetto UE vale per il totale. Nessuna regola nazionale dice a ogni ministero quanto può spendere nei tre anni.

**Soluzione.**
- La legge di bilancio fissa per tre anni un tetto di spesa netta per ogni ministero. La somma dei tetti è coerente con il percorso UE di spesa netta.
- Una parte del percorso non è assegnata: è una **riserva** per gli imprevisti (0,1-0,15% del PIL, costruita in modo graduale). Se non si usa, migliora il saldo.
- Le **entrate superiori alle previsioni** che non vengono da nuove leggi non finanziano spese nuove né tagli di tasse. Vanno a ridurre deficit e debito.
- Chi vuole superare un tetto lo dice in Parlamento, con un voto motivato e una nota dell'UPB.

**Perché funziona altrove.** Svezia (tetto dal 1997, con margine di bilancio) e Paesi Bassi (dal 1994, entrate in più non spese) hanno ridotto il debito per decenni. La Finlandia mostra il limite: il tetto non basta se l'economia non cresce (rapporto di benchmark, sezione 2; Governo svedese, *The Swedish fiscal policy framework*).

**Varianti**

| Variante | Contenuto | Costo 2027 / 2028 / 2029 / regime | Intensità | Copertura |
|---|---|---|---|---|
| PIENA | Tetti per ministero nella L. 243/2012 (legge rinforzata); riserva 0,05% del PIL nel 2028, 0,1% nel 2029, 0,15% dal 2030; regola sulle entrate inattese; superamento solo con legge motivata e nota UPB | 0,001 / 0,003 / 0,003 / **0,003** (2028) | 1 | RIALLOCAZIONE 0,003 |
| ESSENZIALE | Stesse regole nella L. 196/2009 (legge ordinaria, rafforzando l'art. 22-bis); riserva 0,1% del PIL dal 2029; superamento con relazione motivata del Governo | 0,001 / 0,002 / 0,002 / **0,002** | 0,6 | RIALLOCAZIONE 0,002 |
| ZERO | Tetti indicativi per ministero pubblicati nel Documento di finanza pubblica; monitoraggio trimestrale RGS degli scostamenti; regola sulle entrate inattese come indirizzo | 0 | 0,3 | invarianza |

**Costo: da dove viene (stima GovernAI).** Un'unità RGS di 10-15 persone per i tetti e il monitoraggio trimestrale (circa 0,1 mln per persona con oneri, più 1 mln di sistemi): 2-3 mln l'anno. La riserva **non è un costo**: è una parte del percorso UE che non si assegna in anticipo.

**Coperture.** Il costo diretto si copre con la riduzione delle spese di funzionamento del MEF effettivamente sostenute (consulenze, locazioni passive), non con residui. **La proposta non genera risparmi da contare.** Rende più probabili quelli di RA13 e RP01, ma non li aumenta.

**Chi guadagna e chi paga.**
- *Guadagnano* le generazioni giovani e chi pagherà gli interessi futuri (3,8% del PIL nel 2025, 4,3% previsto nel 2027: MEF, DPB 2027). Guadagnano anche i ministeri che programmano, perché sanno prima quanto avranno.
- *Pagano* in flessibilità: il Parlamento in sessione di bilancio, i ministeri che oggi ottengono fondi in corso d'anno, chi chiede tagli di tasse finanziati da entrate inattese.

**Articolato normativo essenziale** (variante PIENA; disegno di legge a maggioranza assoluta, modifica della L. 243/2012 e della L. 196/2009)

> **Art. 1 (Tetti triennali di spesa).** 1. Nella legge 24 dicembre 2012, n. 243, dopo l'articolo 5 è inserito il seguente: «Art. 5-bis. – 1. La legge di bilancio stabilisce, per ciascuno dei tre anni del periodo di riferimento, il limite massimo della spesa netta di ciascun Ministero, in coerenza con il percorso della spesa netta definito ai sensi del regolamento (UE) 2024/1263. 2. Una quota del percorso, pari ad almeno lo 0,1 per cento del prodotto interno lordo, non è assegnata ed è iscritta in un fondo di riserva per spese impreviste. 3. Il limite di un Ministero può essere superato solo con legge, motivata e corredata di una nota dell'Ufficio parlamentare di bilancio, che indica la compensazione con altri limiti o con la riserva.»
>
> **Art. 2 (Entrate inattese).** 1. Le maggiori entrate rispetto alle previsioni del Documento di finanza pubblica che non derivano da provvedimenti legislativi sono destinate al miglioramento dell'indebitamento netto e alla riduzione del debito. Non possono coprire nuove o maggiori spese né riduzioni di entrate. 2. È coordinata con il comma 1 la disciplina del Fondo per la riduzione della pressione fiscale (art. 1, comma 431, L. 147/2013; disciplina vigente **da verificare**).
>
> **Art. 3 (Monitoraggio).** 1. La Ragioneria generale dello Stato pubblica ogni trimestre, per ciascun Ministero, la spesa rispetto al limite. 2. Il Ministero che supera il limite presenta entro trenta giorni un piano di rientro.
>
> **Art. 4 (Copertura).** 1. Agli oneri, pari a 1 milione per il 2027 e a 3 milioni annui dal 2028, si provvede con la riduzione delle spese di funzionamento del Ministero dell'economia e delle finanze, con esclusione delle spese obbligatorie.

**Rischi giuridici**
- **Art. 81 Cost.** Nessun conflitto: la regola rafforza l'equilibrio (c. 1) e la copertura (c. 3). Il tetto non sostituisce la copertura dei singoli atti.
- **L. 243/2012, legge rinforzata (art. 81, c. 6).** Si modifica solo in modo espresso e a maggioranza assoluta (sent. 88/2014, nel registro verificato `costituzione/giurisprudenza_verificata.json`). È il motivo della variante PIENA: una regola nella sola L. 196/2009 (ESSENZIALE) può essere derogata da qualunque legge ordinaria successiva, compresa la legge di bilancio. Che i tetti per ministero rientrino nelle «norme fondamentali» che la L. cost. 1/2012 (art. 5) riserva alla L. 243/2012 è plausibile ma **da verificare** con il costituzionalista del progetto.
- **Regolamenti parlamentari (art. 64 Cost.).** La legge non può vincolare da sola le procedure delle Camere sugli emendamenti. Il voto motivato per superare un tetto richiede una modifica coordinata dei regolamenti di Camera e Senato.
- **Regole UE.** Il regolamento (UE) 2024/1263 fissa già il percorso di spesa netta su 4-7 anni. Le entrate inattese oggi non creano spazio sul tetto UE, perché la spesa netta è calcolata al netto delle sole misure discrezionali di entrata. La regola nazionale serve quindi soprattutto se le regole UE cambiano o se si attiva una clausola di deroga. La direttiva 2011/85/UE, modificata dalla direttiva (UE) 2024/1265, chiede quadri di bilancio a medio termine nazionali (recepimento italiano **da verificare**).

**Altri rischi e mitigazioni**
- *Deroghe ogni anno:* superamento solo con legge motivata e nota UPB; elenco pubblico delle deroghe.
- *Tetti che spingono a spostare spesa fuori bilancio (società, fondi, crediti d'imposta):* il tetto è sulla spesa netta in contabilità nazionale, non sugli stanziamenti.
- *Emergenze:* riserva, più la clausola generale UE di deroga.

**Cronoprogramma**
- *Primi 100 giorni:* ddl con 01-P17 (stesso testo "conti pubblici"); RGS prepara la ripartizione per ministero sul percorso 2028-2030.
- *Entro 12 mesi:* approvazione a maggioranza assoluta; prima legge di bilancio con tetti (2028-2030); modifica dei regolamenti parlamentari.
- *Entro fine legislatura:* due cicli completi; relazione della Corte dei conti sul rispetto dei tetti.

**Indicatori**

| KPI | Base (dato, anno, fonte) | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Crescita della spesa netta rispetto al tetto UE | 1,5% contro 1,3%, 2025 (Commissione UE) | entro il tetto ogni anno | entro il tetto ogni anno, deviazione cumulata riassorbita |
| Ministeri entro il proprio tetto | non misurato, 2026 (nessun tetto) | ≥ 80% | 100% o deroga votata |
| Entrate inattese destinate al deficit | nessuna regola, 2026 | 100% | 100% |

---

## 01-P17 — UPB più forte: revisioni indipendenti, accesso ai dati, "rispetta o spiega", analisi volontaria dei programmi elettorali

**Tipo.** Proposta nuova, che unisce le idee B e C. La parte C (programmi elettorali) è separabile: è la variante PILOTA. Si integra con le altre funzioni UPB già nel programma (01-P1, 02-C3 art. 5 c. 2, 04-P4, 08-P1). Va in **un solo disegno di legge "UPB"**, come chiede l'esame costituzionale (`costituzione/esami/governai_conti_2027_2029.md`, sezione 4).

**Problema in un dato.** L'UPB può avere **al massimo 40 persone** (art. 17, c. 4, L. 243/2012) e ha una dotazione di **6 mln l'anno** (3 mln per ciascuna Camera, art. 19; UPB, rendiconto 2020). La spagnola AIReF ha esaminato **108 mld di spesa** nel primo ciclo di revisioni 2018-2021 (Hacienda, note al Consiglio dei ministri). In Italia il principio "rispetta o spiega" vale solo sulle previsioni macroeconomiche (art. 18, c. 3, L. 243/2012). Non vale sulle raccomandazioni di spesa.

**Soluzione.**
- **Revisioni indipendenti.** L'UPB rivede ogni anno 2-3 aree di spesa (15-25 mld in tutto) e presenta opzioni, non scelte.
- **Accesso ai dati.** Le amministrazioni rispondono alle richieste dell'UPB entro 30 giorni. Il rifiuto va motivato.
- **Rispetta o spiega.** Il Governo risponde entro 3 mesi a ogni raccomandazione: la accetta o spiega perché no.
- **Programmi elettorali.** Ogni forza politica, se vuole, chiede all'UPB una stima pubblica di costi e coperture del proprio programma, con un metodo unico pubblicato prima. Nessuna classifica, solo numeri. GovernAI si impegna a chiederla per primo.

**Perché funziona altrove.** Spagna: AIReF (LO 6/2013), revisioni della spesa su incarico del Governo; secondo la stessa AIReF le proposte sono state recepite solo in parte (fonte secondaria). Paesi Bassi: il CPB stima i programmi elettorali (*Keuzes in Kaart*). L'edizione 2023 è l'undicesima e ha coperto 8 partiti; l'edizione 2027-2030, pubblicata il 10/10/2025, ne ha coperti 10 (CPB, ricerca del 15/11/2026; anno di avvio **da verificare**).

**Varianti**

| Variante | Contenuto | Costo 2027 / 2028 / 2029 / regime | Intensità | Copertura |
|---|---|---|---|---|
| PIENA | 2-3 revisioni l'anno (15-25 mld); accesso ai dati con obbligo di risposta; rispetta o spiega in 3 mesi; analisi dei programmi elettorali; circa 30 persone in più all'UPB e un nucleo di monitoraggio RGS | 0,002 / 0,005 / 0,006 / **0,006** (2029) | 1 | RIALLOCAZIONE 0,006 |
| ESSENZIALE | 1 revisione l'anno (8-10 mld); rispetta o spiega; analisi dei programmi elettorali; circa 12-15 persone in più | 0,001 / 0,0025 / 0,0025 / **0,0025** | 0,55 | RIALLOCAZIONE 0,0025 |
| PILOTA | Solo analisi volontaria dei programmi elettorali e rispetta o spiega sulle valutazioni UPB già esistenti | 0 / 0,0005 / 0,0005 / **0,0005** | 0,25 | RIALLOCAZIONE 0,0005 |
| ZERO | Solo rispetta o spiega sulle valutazioni UPB già esistenti (estensione dell'art. 18, c. 3) | 0 | 0,15 | invarianza |

**Costo: da dove viene (stima GovernAI).**
- Personale: 25-35 persone × 150.000 € medi con oneri (ipotesi del rapporto di benchmark) = 4-5 mln; nucleo RGS di 5 persone, 0,5 mln.
- Programmi elettorali: 1-2 mln per ciclo, cioè circa 0,3-0,4 mln l'anno.
- **Attenzione alla dimensione dell'UPB.** 01-P1 (circa 10 persone), 08-P1 (sezione fino a 30 persone) e 04-P4 aggiungono già funzioni. Con la PIENA l'UPB passerebbe da 40 a circa 100 persone. Il tetto di 40 dell'art. 17 va alzato nella stessa legge. Serve un piano di assunzioni graduale, altrimenti la qualità cala.

**Coperture.** Riduzione delle spese di funzionamento del MEF; l'aumento della dotazione UPB passa per la legge di bilancio (art. 19 L. 243/2012). **I risparmi delle revisioni non sono una copertura.** Ordine di grandezza, solo indicativo (rapporto di benchmark): rivedere 20 mld, trovare il 10% di margine e realizzarne un terzo vale 0,2-0,7 mld dopo 3-4 anni. Possono entrare in RA13 solo dopo che la legge di bilancio ha davvero tagliato gli stanziamenti.

**Chi guadagna e chi paga.**
- *Guadagnano* contribuenti e utenti dei servizi (spesa più efficace); chi vota (programmi confrontabili); il Parlamento (più informazioni indipendenti).
- *Pagano* i beneficiari di spese senza risultati dimostrati; il Governo, che perde il controllo esclusivo sui numeri; le forze politiche che promettono senza coperture.

**Articolato normativo essenziale** (variante PIENA; disegno di legge a maggioranza assoluta, modifica della L. 243/2012)

> **Art. 1 (Revisioni indipendenti della spesa).** 1. All'articolo 18 della legge 24 dicembre 2012, n. 243, è aggiunto il seguente comma: «L'Ufficio effettua ogni anno la revisione di almeno due aree di spesa, individuate dal Consiglio dell'Ufficio sentite le Commissioni bilancio. Per ciascuna area presenta più opzioni, con i loro effetti finanziari e distributivi, senza indicare una scelta.»
>
> **Art. 2 (Accesso ai dati).** 1. Le amministrazioni pubbliche forniscono all'Ufficio, entro trenta giorni dalla richiesta, i dati e le informazioni necessari, anche in forma individuale e pseudonimizzata, nel rispetto del regolamento (UE) 2016/679. Il rifiuto è motivato e comunicato alle Commissioni bilancio.
>
> **Art. 3 (Rispetta o spiega).** 1. Il Governo, entro tre mesi dalla pubblicazione di una raccomandazione dell'Ufficio, comunica alle Camere se intende conformarsi o le ragioni per cui non lo fa.
>
> **Art. 4 (Programmi elettorali).** 1. Ogni partito o gruppo politico organizzato che presenta candidature alle elezioni della Camera dei deputati può chiedere all'Ufficio, entro il termine fissato dal Consiglio, la stima dei costi e delle coperture del proprio programma. 2. Il metodo è pubblicato almeno dodici mesi prima della scadenza naturale della legislatura. 3. Le stime sono pubblicate insieme, almeno quindici giorni prima del voto, senza classifiche.
>
> **Art. 5 (Personale e dotazione).** 1. All'articolo 17, comma 4, le parole «quaranta unità» sono sostituite dalle seguenti: «settanta unità» (cifra da coordinare con 01-P1, 04-P4 e 08-P1). 2. La dotazione dell'articolo 19 è incrementata di 5 milioni di euro annui dal 2029, con riduzione delle spese di funzionamento del Ministero dell'economia e delle finanze.

**Rischi giuridici**
- **L. 243/2012 e art. 81, c. 6 Cost.** Ogni nuova funzione si scrive in modo espresso nella L. 243/2012, a maggioranza assoluta (sent. 88/2014). Va fuori dalla legge di bilancio, che non può contenere norme ordinamentali (art. 21, c. 1-quinquies, L. 196/2009, richiamato nell'esame costituzionale del progetto).
- **Autonomia delle Camere (art. 64 Cost.).** L'UPB è un organo presso le Camere: compiti e personale vanno concordati con gli Uffici di presidenza (per 08-P1 l'esame cita le sent. 129/1981 e 120/2014, non nel registro verificato: **da verificare**).
- **Programmi elettorali e parità di trattamento (artt. 3, 49 Cost.).** L'adesione è volontaria e il metodo è uguale per tutti. Il rischio è la politicizzazione dell'UPB: per questo nessuna classifica e metodo pubblicato un anno prima. **Per le elezioni del 2027 la legge non arriverebbe in tempo.** GovernAI può chiedere una verifica volontaria a un soggetto indipendente, ma non è questa misura.
- **Regole UE.** La direttiva (UE) 2024/1265 rafforza le istituzioni di bilancio indipendenti e introduce il principio "rispetta o spiega" sulle loro valutazioni (articolo e stato di recepimento **da verificare**). Il regolamento (UE) 473/2013 chiede organismi indipendenti di controllo. La proposta va nella stessa direzione e la estende alla spesa.
- **Protezione dei dati.** L'accesso a dati individuali richiede finalità limitate, pseudonimizzazione e valutazione d'impatto (art. 35 GDPR).

**Altri rischi e mitigazioni**
- *Conflitto di ruolo (chi controlla non decide):* le revisioni si fermano alle opzioni.
- *Raccomandazioni ignorate (caso spagnolo):* rispetta o spiega con termine e pubblicazione delle risposte.
- *Sovraccarico prima del voto:* calendario fisso e personale dedicato.

**Cronoprogramma**
- *Primi 100 giorni:* ddl unico "UPB e conti pubblici" (con 01-P16, 01-P1, 04-P4, 08-P1); intesa con le presidenze delle Camere.
- *Entro 12 mesi:* approvazione; primo bando di assunzione; scelta delle prime due aree.
- *Entro fine legislatura:* almeno 4 revisioni pubblicate con risposte del Governo; metodo per i programmi elettorali pubblicato 12 mesi prima del voto.

**Indicatori**

| KPI | Base (dato, anno, fonte) | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Spesa esaminata da revisioni indipendenti, cumulata | 0, 2026 | ≥ 30 mld | ≥ 60 mld |
| Raccomandazioni con risposta motivata del Governo entro 3 mesi | 0%, 2026 (nessun obbligo) | 100% | 100% |
| Forze politiche che chiedono la stima del programma | 0, 2026 | primo ciclo preparato | ≥ 3 alle prime elezioni utili |
| Risparmi delle revisioni tagliati per legge e certificati a consuntivo | 0, 2026 | da misurare | ≥ 0,2 mld/anno (indicativo, non copertura) |

---

## 01-P18 — Registro mensile dei redditi Entrate-INPS (rafforzamento di 01-P7)

**Tipo.** Rafforzamento di **01-P7** (conto fiscale annuale), di **09-C2** (once-only) e di **02-C4 art. 3** (aggiornamento automatico dell'Assegno di inclusione). Ha un id proprio perché ha un costo proprio e va valutato a parte. **Non ha senso senza 01-P7 o 02-C4.**

**Problema in un dato.** L'ISEE si calcola sui redditi del **secondo anno precedente** (DPCM 159/2013 e successive modifiche; testo vigente **da verificare**). Chi perde il lavoro o ha redditi che cambiano riceve Assegno unico e Assegno di inclusione calcolati su una situazione vecchia di due anni, salvo ISEE corrente su domanda. L'ADI raggiunge **690 mila nuclei** (INPS, giugno 2026, da `programma/schede/02_lavoro.md`). In Finlandia il registro dei redditi è in tempo reale dal 2019: il datore di lavoro comunica ogni pagamento entro pochi giorni (termine di 5 giorni **da verificare**).

**Soluzione.**
- I sostituti d'imposta trasmettono **ogni mese** redditi e ritenute per persona, in un solo flusso. Si parte da UniEmens, che è già mensile per i contributi, e si unisce con i dati della Certificazione Unica.
- Il registro è condiviso tra Agenzia delle entrate e INPS. Alimenta il conto fiscale di 01-P7.
- Ogni mese aggiorna Assegno unico, Assegno di inclusione e ISEE corrente, senza nuova domanda.
- Accessi tracciati. Ogni persona vede chi ha usato i suoi dati (come in 09-C2).

**Varianti**

| Variante | Contenuto | Costo 2027 / 2028 / 2029 / picco | Intensità | Copertura |
|---|---|---|---|---|
| PIENA | Flusso mensile unico per tutti i sostituti (lavoro dipendente, pensioni, assimilati); CU abolita per chi è nel registro; aggiornamento mensile di AUU, ADI e ISEE corrente; alimenta 01-P7 | 0,02 / 0,04 / 0,035 / **0,04** (2028); 0,015 dal 2030 | 1 | COESIONE_2127 0,025 (una tantum) + RIALLOCAZIONE 0,015 |
| ESSENZIALE | Arricchisce UniEmens con le ritenute fiscali per persona; CU resta; aggiornamento mensile solo di ADI e ISEE corrente | 0,01 / 0,025 / 0,02 / **0,025** (2028); 0,01 dal 2030 | 0,55 | COESIONE_2127 0,015 + RIALLOCAZIONE 0,01 |
| PILOTA | Uso dei dati UniEmens già esistenti per aggiornare ogni mese l'ADI (decalage di 02-C4) | 0,005 / 0,005 / 0,005 / **0,005** | 0,15 | RIALLOCAZIONE 0,005 |

**Costo: da dove viene (stima GovernAI, dal rapporto di benchmark).** 0,05-0,10 mld una tantum e 0,01-0,02 mld l'anno di gestione. Ipotesi: dimensione italiana circa 10 volte quella finlandese, con riuso di UniEmens, PDND e fatturazione elettronica. Il costo finlandese di partenza è **da verificare**. Restano fuori, e vanno misurati, i costi di adeguamento dei software paghe per le imprese.

**Coperture.** Investimento iniziale con fondi di coesione 2021-27, obiettivo strategico 1, digitalizzazione della PA (come per 09-C2); gestione con riduzione della spesa ICT corrente di Agenzia delle entrate e INPS. **Non si contano** i minori pagamenti indebiti di prestazioni e i minori recuperi: sono certificabili solo dopo.

**Chi guadagna e chi paga.**
- *Guadagnano* le famiglie con redditi variabili o che perdono il lavoro, che oggi ricevono prestazioni in ritardo o sbagliate e poi devono restituirle. Guadagnano CAF e cittadini, con meno documenti da portare.
- *Pagano* i datori di lavoro e i consulenti del lavoro, per l'adeguamento dei software. Le piccole imprese più delle grandi. Paga, in termini di riservatezza, chiunque abbia i dati in un registro più ricco: per questo servono garanzie forti.

**Articolato normativo essenziale** (disegno di legge; modifica del d.P.R. 600/1973 e del d.lgs. 175/2014)

> **Art. 1 (Registro mensile dei redditi).** 1. A decorrere dal 1° gennaio 2029 i sostituti d'imposta trasmettono mensilmente, con un unico flusso telematico all'INPS e all'Agenzia delle entrate, i compensi corrisposti, le ritenute operate e i contributi dovuti per ciascun percipiente. 2. Per i percipienti inclusi nel flusso, la certificazione unica di cui all'articolo 4, comma 6-ter, del d.P.R. 22 luglio 1998, n. 322, non è più dovuta. *(Comma 2 solo variante PIENA.)*
>
> **Art. 2 (Uso dei dati).** 1. I dati del registro sono usati esclusivamente per: a) il conto fiscale annuale (01-P7); b) il calcolo e l'aggiornamento mensile dell'Assegno unico e universale, dell'Assegno di inclusione e dell'ISEE corrente; c) le statistiche ufficiali, in forma anonima. 2. Ogni altro uso richiede una legge.
>
> **Art. 3 (Garanzie).** 1. Gli accessi sono tracciati; ogni persona può consultare l'elenco delle amministrazioni che hanno usato i suoi dati. 2. Nessuna riduzione di prestazione è disposta senza comunicazione e senza possibilità di correggere i dati entro trenta giorni. 3. Il trattamento è preceduto da valutazione d'impatto ai sensi dell'articolo 35 del regolamento (UE) 2016/679, sentito il Garante.
>
> **Art. 4 (Copertura).** 1. Agli oneri, pari a 20 milioni per il 2027, 40 milioni per il 2028, 35 milioni per il 2029 e 15 milioni annui dal 2030, si provvede per la parte di investimento con le risorse della politica di coesione 2021-2027, obiettivo strategico 1, previa riprogrammazione, e per la parte di gestione con la riduzione della spesa ICT corrente dell'INPS e dell'Agenzia delle entrate.

**Rischi giuridici**
- **Art. 81 Cost.** Copertura certa per la gestione; quella con i fondi di coesione dipende dalla riprogrammazione con la Commissione UE. Se non arriva, si ripiega sulla PILOTA.
- **Protezione dei dati (artt. 2, 3 Cost.; art. 8 CEDU; GDPR artt. 5, 6, 25, 35).** Un registro mensile per persona è un trattamento massivo: regge con base di legge, finalità chiuse, minimizzazione e controllo umano. L'esame costituzionale del progetto richiama la sent. 20/2019 sul bilanciamento tra trasparenza e riservatezza (non nel registro verificato: **da verificare**). Coerenza con le garanzie di 01-P10.
- **Statuto del contribuente (L. 212/2000).** Nuovi adempimenti solo con congruo preavviso (art. 3; verifica del termine **da verificare**) e senza chiedere dati già posseduti (art. 6, c. 4).
- **Regole UE.** Nessun vincolo diretto; coerente con il regolamento (UE) 2024/903 sull'interoperabilità e con il principio once-only.

**Altri rischi e mitigazioni**
- *Errori che riducono le prestazioni:* contraddittorio di 30 giorni; nessuna riduzione automatica senza comunicazione.
- *Costi per le piccole imprese:* riuso di UniEmens, nessun dato nuovo oltre le ritenute per persona; avvio graduale.
- *Progetto IT grande:* PILOTA prima, PIENA solo dopo la prova.

**Cronoprogramma**
- *Primi 100 giorni:* tavolo Entrate-INPS-Sogei; valutazione d'impatto con il Garante; PILOTA sull'ADI con i dati UniEmens.
- *Entro 12 mesi:* legge; specifiche del flusso unico; consultazione dei consulenti del lavoro.
- *Entro fine legislatura:* flusso mensile obbligatorio dal 2029; aggiornamento mensile di AUU e ADI; primo conto fiscale 01-P7 alimentato dal registro.

**Indicatori**

| KPI | Base (dato, anno, fonte) | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Ritardo tra cambio di reddito e aggiornamento della prestazione (AUU, ADI) | fino a 24 mesi, 2026 (ISEE sul secondo anno precedente) | ≤ 2 mesi per l'ADI | ≤ 2 mesi per AUU e ADI |
| Importi di AUU e ADI pagati in eccesso e poi recuperati | base INPS da acquisire | -30% | -50% |
| Sostituti d'imposta nel flusso mensile unico | 0%, 2026 | 50% | 100% |

---

## 02-C8 — Aggancio protetto e correttore automatico e temporaneo sulla spesa pensionistica

**Tipo.** Due parti.
- **Parte 1, protezione dell'aggancio:** integrazione di **02-C3**. Nuovo art. 2-bis nel testo di 02-C3, che oggi conferma l'aggancio (art. 2, c. 2) ma non lo protegge.
- **Parte 2, correttore:** proposta nuova. Usa lo stesso disegno di **PE04** (rivalutazione ridotta sulla sola quota di pensione oltre 6 volte il minimo), ma lo fa scattare solo se serve. **Non si somma a PE04.** Negli anni in cui PE04 è in vigore (2030-2034, se scelta) il correttore non tocca la stessa quota.

**Problema in un dato.** La spesa pensionistica è al **15,2% del PIL** nel 2025 e sale al picco del **17,1%** nel 2041-44. Senza l'aggancio all'aspettativa di vita il picco sarebbe del **18,0%** (RGS, *Tendenze di medio-lungo periodo*, aggiornamento 2026, da `programma/schede/02_lavoro.md`). L'aggancio è già stato attenuato: per la L. 199/2025 l'aumento è di 1 mese nel 2027 e di 3 mesi in tutto nel 2028 (fonte secondaria in `benchmark/programmi/lavoro_welfare.csv`; costo nella relazione tecnica **da verificare**). Oggi nessuna regola obbliga a coprire queste scelte per tutta la durata dei loro effetti.

**Soluzione.**
- **Aggancio protetto.** Una legge che sospende o riduce l'aggancio, o apre nuove uscite anticipate, deve indicare la copertura **dentro il sistema pensionistico** e **per tutti gli anni** in cui produce effetti, non solo per tre. L'UPB ne stima il costo per generazione.
- **Correttore automatico e temporaneo.** Ogni anno la RGS confronta la spesa pensionistica prevista per i tre anni successivi con uno scenario di riferimento fissato per legge. Se lo scarto supera **0,2 punti di PIL** per due previsioni di fila, e non dipende dal ciclo economico, scatta il correttore:
  - la rivalutazione della sola quota di pensione **oltre 6 volte il minimo** (circa 3.700 € lordi al mese) passa dal 75% al **50%**;
  - mai sotto il 50% e mai un blocco totale; al 75% negli anni con inflazione oltre il 4%;
  - dura al massimo **3 anni** per volta, poi decade da solo;
  - non si somma ad altri raffreddamenti sulla stessa quota: si applica il più favorevole.

**Un limite da dire con chiarezza.** Il correttore **non chiude lo scarto**: è un primo argine e un segnale. Calcolo (stima GovernAI): quota di pensioni oltre 6 volte il minimo 20-24 mld l'anno (nota di PE04, `programma/coperture_menu.csv`); inflazione 1,8-2%; riduzione di 25 punti della rivalutazione. Risparmio: **0,09-0,12 mld il primo anno, 0,27-0,36 mld al terzo anno**. Lo scarto che fa scattare il correttore vale invece 0,2 punti di PIL, circa **4,7 mld** (PIL 2026 di 2.326 mld). Il correttore ne copre il **2-8%**. Il resto deve arrivare da una scelta del Parlamento: per questo la variante ESSENZIALE punta sull'obbligo di proporre una correzione, e il correttore scatta solo se il Parlamento non decide.

**Perché funziona altrove.** Svezia: "freno" automatico se gli impegni del sistema superano le attività, scattato più volte dopo il 2008 (anni **da verificare**). Danimarca: età rivista ogni 5 anni; con la legge del 22/5/2025 arriva a 70 anni dal 2040 (fonte secondaria). La Spagna ha fatto il contrario nel 2021-2023 e l'AIReF ne valuta ora la regola di spesa.

**Varianti**

| Variante | Contenuto | Costo 2027 / 2028 / 2029 / regime | Intensità | Copertura |
|---|---|---|---|---|
| PIENA | Aggancio protetto in L. 243/2012 (legge rinforzata) + correttore automatico come sopra, con validazione UPB dello scarto | 0 / 0 / 0 / **0** | 1 | invarianza (risparmio eventuale 0,1-0,36, **non copertura**) |
| ESSENZIALE | Aggancio protetto in L. 196/2009 + correttore "semi-automatico": se c'è lo scarto, il Governo presenta entro il Documento di finanza pubblica una correzione interna al sistema pensionistico; se il Parlamento non la approva entro la legge di bilancio, si applica il correttore | 0 / 0 / 0 / **0** | 0,6 | invarianza |
| ZERO | Solo aggancio protetto in L. 196/2009 (testo per 02-C3) e confronto annuale pubblico RGS-UPB con lo scenario di riferimento | 0 | 0,3 | invarianza |

I costi amministrativi (calcoli RGS e INPS) rientrano nelle attività ordinarie: stima GovernAI trascurabile.

**Coperture.** Nessuna richiesta. Il risparmio del correttore è **solo eventuale**: scatta solo se c'è lo scarto, quindi **non va nel menu delle coperture** e non finanzia nulla. Se scatta, va al deficit.

**Chi guadagna e chi paga.**
- *Guadagnano* le generazioni giovani e chi entra oggi nel lavoro, che pagherebbero lo scarto con più contributi o più debito. Guadagna chi va in pensione con assegni bassi: il correttore non lo tocca.
- *Pagano*, **solo se il correttore scatta**, le persone con pensioni oltre 6 volte il minimo: circa 1 milione (stima GovernAI in PE04; 477.654 sopra 5.000 € al mese, INPS 2025, fonte secondaria). Perdono al massimo un quarto della rivalutazione sulla sola parte oltre la soglia. Esempio (stima GovernAI): pensione di 5.000 € lordi al mese, quota oltre soglia circa 1.300 €, inflazione 2%: circa 6,5 € lordi al mese in meno il primo anno, che restano negli anni successivi.
- *Pagano* in flessibilità i governi futuri: un allentamento dell'aggancio deve trovare la copertura dentro le pensioni.

**Articolato normativo essenziale** (variante PIENA)

> **Art. 1 (Aggancio protetto; nuovo art. 2-bis di 02-C3).** 1. Le disposizioni che sospendono o riducono l'adeguamento dei requisiti all'aspettativa di vita, di cui all'articolo 12 del decreto-legge 31 maggio 2010, n. 78, o che introducono nuove forme di accesso anticipato al pensionamento, indicano la copertura degli oneri per tutti gli anni in cui producono effetti, mediante minori spese o maggiori entrate del sistema previdenziale obbligatorio. 2. Le disposizioni sono corredate di una valutazione dell'Ufficio parlamentare di bilancio sul costo per coorte di nascita. *(Nella PIENA il comma 1 è inserito nella L. 243/2012.)*
>
> **Art. 2 (Scenario di riferimento).** 1. Lo scenario di riferimento della spesa pensionistica in rapporto al prodotto interno lordo potenziale è quello del rapporto della Ragioneria generale dello Stato sulle tendenze di medio-lungo periodo del 2026, aggiornato solo per gli effetti di leggi coperte ai sensi dell'articolo 1.
>
> **Art. 3 (Correttore temporaneo).** 1. Se per due previsioni annuali consecutive la spesa pensionistica prevista per uno dei tre anni successivi supera lo scenario di riferimento di oltre 0,2 punti di prodotto interno lordo potenziale, e l'Ufficio parlamentare di bilancio conferma che lo scarto non dipende da fattori ciclici, dal 1° gennaio dell'anno successivo la rivalutazione della quota di trattamento eccedente sei volte il trattamento minimo è pari al 50 per cento della variazione dei prezzi. 2. La misura si applica per non più di tre anni e cessa prima se lo scarto si chiude. 3. Negli anni in cui l'inflazione supera il 4 per cento la rivalutazione della stessa quota è pari al 75 per cento. 4. La misura non si cumula con altre riduzioni della rivalutazione sulla stessa quota: si applica la più favorevole. 5. Prima dell'applicazione l'INPS trasmette alle Camere una relazione sulla perdita cumulata di potere d'acquisto per fascia di importo, comprese le riduzioni degli anni precedenti. 6. Le minori spese concorrono al miglioramento dell'indebitamento netto.

**Rischi giuridici**

*Giurisprudenza costituzionale sulla perequazione.* Numeri e contenuti delle sentenze 70/2015, 250/2017, 234/2020, 19/2025 e 52/2026 sono riscontrati nel registro verificato del progetto (`costituzione/giurisprudenza_verificata.json`, con data di deposito e dispositivo). Le altre sono citate in `giuridico/conformita.csv` ma non sono nel registro: vanno ricontrollate.

| Sentenza | Che cosa ha deciso | Che cosa vuol dire per il correttore |
|---|---|---|
| 70/2015 (dep. 30/4/2015) | Illegittimo il blocco biennale 2012-13 della perequazione per le pensioni oltre 3 volte il minimo, senza gradualità né motivazione | Mai blocco totale; soglia alta; motivazione nella legge e nella relazione INPS |
| 250/2017 (dep. 1/12/2017) | Legittimo il DL 65/2015, che restituiva una parte della perequazione bloccata, con un bilanciamento motivato | Il bilanciamento con i conti pubblici è ammesso se esplicito |
| 234/2020 (dep. 9/11/2020) | Legittimo il raffreddamento 2019-21; legittimo il contributo di solidarietà, ma ridotto a 3 anni; avverte che la reiterazione rende il vaglio più stretto | Durata massima 3 anni per volta; conteggio di tutti i raffreddamenti precedenti |
| 19/2025 (dep. 14/2/2025) | Questioni sulla perequazione 2023-24 (L. 197/2022, c. 309) non fondate o inammissibili; secondo l'esame del progetto ammette usi dei risparmi anche fuori dal sistema pensionistico e chiede una disciplina più stabile | Una regola fissata prima e uguale nel tempo è coerente con la richiesta di stabilità |
| 52/2026 (dep. 16/4/2026) | Questioni sulla stessa norma (c. 309) non fondate | Conferma il margine del legislatore sui raffreddamenti graduati |
| 316/2010, 173/2016, 167/2025 | Citate in `giuridico/conformita.csv` (167/2025: il raffreddamento non è un tributo) | **Da verificare**: non sono nel registro verificato |

*Punti delicati.*
- **Reiterazione.** Raffreddamenti nel 2023-24, nel 2027 (art. 55 del ddl di bilancio 2027: 100% fino a 4 volte il minimo, poi a scalare; `costituzione/esami/AC3174_manovra_2027.md`) e, se scelta, PE04 nel 2030-34. Un correttore in più può far apparire la perequazione come "sempre ridotta". Per questo: tetto di 3 anni, nessun cumulo, relazione INPS sulla perdita cumulata. **Scelta politica da fare:** usare 02-C8 *al posto* di PE04 (riduzione solo se serve) oppure *dopo* PE04 (dal 2035).
- **Automatismo.** La Corte chiede che ogni intervento sia motivato e proporzionato. Qui la motivazione sta nella legge (soglia, misura, durata, scopo) e lo scatto dipende da un fatto certificato da RGS e UPB. Il rischio residuo è che la Corte chieda una valutazione caso per caso: la ESSENZIALE lo riduce, perché il Parlamento decide prima.
- **Art. 38, c. 2 Cost.** Adeguatezza non toccata a questi importi (250/2017, 234/2020).
- **Art. 3 Cost.** Colpisce solo la parte alta, con tecnica a scaglioni: più favorevole della tecnica "a blocchi" già ammessa (52/2026).
- **Art. 81 e L. 243/2012.** La protezione dell'aggancio rafforza la copertura (c. 3), ma una legge ordinaria può derogarla. Messa nella L. 243/2012 (PIENA) regge di più. Che rientri nelle materie riservate a quella legge (L. cost. 1/2012, art. 5: sostenibilità del debito) è **da verificare** con il costituzionalista.
- **Regole UE.** Il regolamento (UE) 2024/1263 lega l'estensione del percorso a 7 anni a riforme credibili. Un meccanismo che protegge l'aggancio migliora l'analisi di sostenibilità del debito. I risparmi riducono la spesa netta.

**Altri rischi e mitigazioni**
- *Correttore che scatta in recessione:* scarto misurato sul PIL potenziale e validato dall'UPB.
- *Scenario di riferimento manipolabile:* fissato per legge; si aggiorna solo per leggi coperte.
- *Lavori gravosi:* restano protetti da 02-C3 art. 2 c. 3.
- *Consenso:* il correttore è piccolo per chi lo paga e visibile per tutti; pubblicare ogni anno il confronto con lo scenario.

**Cronoprogramma**
- *Primi 100 giorni:* testo dell'art. 2-bis dentro il ddl di 02-C3; RGS e UPB concordano la misura dello scarto.
- *Entro 12 mesi:* approvazione; primo confronto pubblico con lo scenario.
- *Entro fine legislatura:* due confronti annuali; prima relazione INPS sulla perdita cumulata per fascia.

**Indicatori**

| KPI | Base (dato, anno, fonte) | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Spesa pensionistica / PIL rispetto allo scenario RGS | 15,2%, 2025 (RGS agg. 2026) | scarto ≤ 0,2 punti | scarto ≤ 0,2 punti; picco 2041-44 ≤ 17,1% |
| Leggi che allentano l'aggancio con copertura interna per tutta la durata | nessun obbligo, 2026 | 100% | 100% |
| Confronto annuale pubblico RGS-UPB con lo scenario | non previsto, 2026 | pubblicato ogni anno | pubblicato ogni anno |

---

## 02-C9 — Politiche attive dopo il PNRR: un nucleo minimo di GOL

**Tipo.** Proposta nuova. Nessuna misura del programma tratta la fine del programma GOL. È coerente con 02-C4 art. 5 (case manager per chi riceve l'ADI). Si finanzia con la copertura nuova **RA15**.

**Problema in un dato.** Il programma GOL aveva **4,4 mld** del PNRR, aumentati di 1 mld con la revisione del 2023. Al 31/12/2025 il Ministero del lavoro ha rendicontato **3.076.507 beneficiari**, contro un obiettivo di 3 milioni. L'azione PNRR si è chiusa il 30/6/2026 (Ministero del lavoro e INAPP, note di monitoraggio, ricerca del 15/11/2026; cifre da riscontrare sul documento originale). Senza una fonte nuova la presa in carico si ferma. Il tasso di occupazione italiano è il **67,6%** contro il **76,1%** della media UE (`benchmark/confronto.md`).

**Soluzione.**
- **Profilazione entro 30 giorni** per chi riceve la NASpI e per le persone "attivabili" dei nuclei con Assegno di inclusione. Il d.lgs. 150/2015 prevede già profilazione e patto di servizio: il problema è l'attuazione (tempi reali **da verificare** sui dati di monitoraggio).
- **Percorso intensivo solo per chi è più lontano dal lavoro:** orientamento, formazione breve, tirocinio.
- **Valutazione controfattuale INAPP** pubblicata. Se dopo 3 anni non c'è effetto sull'occupazione, il percorso intensivo si rivede.

**Perché funziona altrove.** Danimarca e Paesi Bassi: presa in carico rapida con obblighi chiari. La Spagna ha ridotto il lavoro a termine con le regole sui contratti, non con la spesa (rapporto di benchmark).

**Varianti**

| Variante | Contenuto | Costo 2027 / 2028 / 2029 / regime | Intensità | Copertura |
|---|---|---|---|---|
| PIENA | Profilazione in 30 giorni per NASpI e ADI; percorso intensivo per circa 400.000 persone l'anno; valutazione INAPP; livello essenziale delle prestazioni per i servizi per l'impiego | 0,10 / 0,30 / 0,45 / **0,45** (2030) | 1 | RIALLOCAZIONE 0,30 (RA15) + SPESE_FISCALI 0,15; 2027-29 con FSE+ 2021-27 |
| ESSENZIALE | Profilazione in 30 giorni; percorso intensivo per circa 200.000 persone l'anno, priorità a disoccupati di lunga durata e ADI; valutazione INAPP | 0,05 / 0,15 / 0,20 / **0,20** (2030) | 0,5 | RIALLOCAZIONE 0,20 (RA15); 2027-29 con FSE+ 2021-27 |
| PILOTA | Sperimentazione randomizzata in 10 province per 3 anni, valutazione INAPP-Banca d'Italia | 0,01 / 0,03 / 0,03 / **0,03** (2028) | 0,1 | COESIONE_2127 0,03 (una tantum) |

**Costo: da dove viene (stima GovernAI).**
- Ipotesi del rapporto di benchmark: 1.000 € medi per persona nel percorso intensivo, tra orientamento (300-500 €) e formazione breve (1.500-3.000 €). Va verificato sui costi standard GOL (decreto interministeriale di adozione di GOL, novembre 2021, **da verificare**).
- PIENA: 400.000 × 1.000 € = 0,40, più 0,05 per profilazione rafforzata, sistemi e valutazione.
- ESSENZIALE: 200.000 × 1.000 € = 0,20.
- Il personale dei centri per l'impiego assunto con il Piano di potenziamento è già finanziato: non è contato qui (finanziamento strutturale **da verificare**).
- Se il ddl di bilancio 2027 o il PN Giovani, donne e lavoro finanziano già una prosecuzione di GOL, il costo netto scende: **da verificare**.

**Coperture.**
- 2027-2029: FSE+ 2021-27 (PN Giovani, donne e lavoro e programmi regionali), ammissibile fino al 31/12/2029. È spesa UE, esclusa dalla spesa netta, una tantum.
- Dal 2030: **RA15**, riduzione degli incentivi all'assunzione senza effetto aggiuntivo dimostrato (`benchmark/bozza_coperture_conti_pubblici.csv`, gettito 0,15-0,35). Per la PIENA serve in più 0,15 di SPESE_FISCALI (per esempio la maggiorazione della deduzione del costo del lavoro per le nuove assunzioni, se è strutturale nella legislazione vigente: **da verificare**).
- **Condizione:** RA15 è di livello 2 e il suo perimetro va verificato. Se non regge, 02-C9 resta PILOTA.
- **Non si contano** i minori pagamenti di NASpI e ADI per chi trova lavoro prima.

**Chi guadagna e chi paga.**
- *Guadagnano* chi cerca lavoro, soprattutto chi è più lontano dal lavoro e chi riceve l'ADI; le imprese che cercano personale; i conti pubblici, con meno sussidi lunghi (non contato).
- *Pagano* le imprese che oggi usano incentivi all'assunzione senza effetto aggiuntivo, cioè che avrebbero assunto comunque. Al Sud il peso può essere maggiore: va verificato con i dati per territorio.

**Articolato normativo essenziale** (variante ESSENZIALE; disegno di legge, modifica del d.lgs. 150/2015)

> **Art. 1 (Nucleo minimo delle politiche attive).** 1. I servizi per l'impiego convocano entro trenta giorni dalla domanda le persone che ricevono la NASpI e le persone attivabili dei nuclei beneficiari dell'Assegno di inclusione, per la profilazione e il patto di servizio. 2. Le persone con profilo di maggiore distanza dal lavoro hanno diritto a un percorso intensivo di orientamento, formazione breve o tirocinio. 3. La profilazione e la presa in carico costituiscono livello essenziale delle prestazioni, definito con decreto del Ministro del lavoro previa intesa in Conferenza Stato-Regioni.
>
> **Art. 2 (Valutazione).** 1. L'INAPP valuta con metodo controfattuale gli effetti del percorso intensivo e pubblica i risultati ogni anno. 2. Dopo tre anni, se non si riscontra un effetto significativo sull'occupazione a dodici mesi, il decreto di cui all'articolo 1 rivede il percorso.
>
> **Art. 3 (Copertura).** 1. Agli oneri, pari a 50 milioni per il 2027, 150 milioni per il 2028 e 200 milioni per il 2029, si provvede con le risorse del Fondo sociale europeo Plus 2021-2027, previa riprogrammazione. 2. Agli oneri, pari a 200 milioni annui dal 2030, si provvede con la riduzione delle autorizzazioni di spesa per gli incentivi all'assunzione individuati come privi di effetto aggiuntivo dalla valutazione di cui alla misura RA15, per le sole assunzioni successive all'entrata in vigore.

**Rischi giuridici**
- **Art. 117 Cost.** Le politiche attive sono materia concorrente e i servizi per l'impiego sono regionali. Il livello essenziale è competenza statale (art. 117, c. 2, lett. m), ma standard e riparto richiedono l'intesa: l'esame costituzionale del progetto cita in materia la sent. 182/2026 (non nel registro verificato: **da verificare**).
- **Art. 81 Cost.** Le coperture una tantum (FSE+) non coprono il regime: dal 2030 serve RA15. La riduzione degli incentivi vale solo per le nuove assunzioni, per rispettare l'affidamento di chi li ha già ottenuti: per questo il gettito sale piano.
- **Art. 38 Cost. e condizionalità.** La profilazione è un diritto e una condizione per la prestazione. Le sanzioni restano quelle vigenti; nessun automatismo nuovo.
- **Regole UE.** FSE+ (regolamento (UE) 2021/1057): spesa ammissibile entro il 2029; serve la riprogrammazione con la Commissione. Ridurre incentivi all'assunzione non pone problemi di aiuti di Stato.

**Altri rischi e mitigazioni**
- *Effetti poco misurati in Italia:* valutazione controfattuale e revisione dopo 3 anni.
- *Differenze tra Regioni:* livello essenziale e cruscotto pubblico per Regione.
- *Resistenza di chi usa gli incentivi:* taglio solo sulle linee senza effetto dimostrato, con preavviso.

**Cronoprogramma**
- *Primi 100 giorni:* riprogrammazione FSE+ con le Regioni; bozza del livello essenziale; avvio della valutazione degli incentivi (RA15).
- *Entro 12 mesi:* legge; intesa in Conferenza; avvio della profilazione in 30 giorni.
- *Entro fine legislatura:* prima valutazione INAPP; dal 2030 copertura RA15.

**Indicatori**

| KPI | Base (dato, anno, fonte) | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Persone con NASpI profilate entro 30 giorni | base da acquisire (monitoraggio GOL e INAPP) | 70% | 90% |
| Occupazione a 12 mesi di chi fa il percorso intensivo, rispetto al gruppo di confronto | non misurato, 2026 | misurato | +5 punti (se l'effetto non c'è, il percorso si rivede) |
| Tasso di occupazione 20-64 o 15-64 anni (stessa definizione di `confronto.md`) | 67,6%, UE 76,1% | +1 punto | +2 punti (contributo non isolabile) |

---

## Che cosa resta da verificare prima del panel

1. Testo vigente dell'art. 22-bis L. 196/2009 e del Fondo per la riduzione della pressione fiscale (L. 147/2013, c. 431).
2. Recepimento italiano della direttiva (UE) 2024/1265 e articolo sul "rispetta o spiega".
3. Costo della graduazione dell'aggancio nella L. 199/2025 (relazione tecnica).
4. Sentenze 316/2010, 173/2016, 167/2025, 20/2019, 182/2026, 129/1981, 120/2014: da aggiungere al registro verificato.
5. Perimetro di RA15: quali incentivi all'assunzione sono strutturali nella legislazione vigente, quanto costano (dossier del Servizio Bilancio sul DL 60/2024, artt. 22-24; L. 207/2024; ddl 2027) e quanta parte usa già 02-C1.
6. Dati GOL dal documento originale del Ministero del lavoro; costi standard dei percorsi.
7. Registro finlandese: termine di comunicazione e costo di realizzazione.

## Fonti nuove usate in questa bozza
- UPB, *Rendiconto della gestione finanziaria 2020* (dotazione e limite di 40 unità): https://www.upbilancio.it/wp-content/uploads/2021/07/Rendiconto-della-gestione-finanziaria-2020.pdf
- UPB, *Regolamento del personale* (pianta organica): https://www.upbilancio.it/wp-content/uploads/2019/05/Regolamento_del_personale.pdf
- Ministero del lavoro, monitoraggio GOL: https://lavoro.gov.it/node/42147 ; INAPP, note di monitoraggio GOL: https://oa.inapp.gov.it/server/api/core/bitstreams/8cfb7a99-2124-4d41-a3c4-cf8b2b533ff0/content (attribuzione delle singole cifre da riscontrare)
- CPB, *Keuzes in Kaart* 2023 e 2027-2030: https://cpb.nl/en/node/161183 ; https://www.cpb.nl/sites/default/files/omnidownload/CPB-Notitie-Evaluatie-Keuzes-in-Kaart-2022-2025.pdf
- Servizio Bilancio, dossier DL 60/2024, profili finanziari (per RA15): https://finanze.regione.emilia-romagna.it/documenti-di-finanza/dossier-284-2-dl-60-coesione-parte-ii-profili-finanziari-27-06-2024.pdf
- Tutte le altre fonti sono nei file del repository citati nel testo.
