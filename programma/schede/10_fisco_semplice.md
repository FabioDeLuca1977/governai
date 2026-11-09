# GovernAI — Schede pronte, Area 10: Fisco semplice

*Agente "confronto internazionale e fisco", 8 novembre 2026. Le proposte appartengono all'area 01 (Economia) e ne continuano la numerazione: 01-P7, 01-P8, 01-P9.*

**File collegati.**
- Varianti: `programma/varianti/10_fisco_semplice.csv`.
- Nuove coperture proposte: `programma/coperture_nuove_fisco.csv`.
- Confronto internazionale: `benchmark/confronto.md`.

"Stima GovernAI" indica una stima propria, senza quantificazione ufficiale. Importi in mld €/anno salvo diversa indicazione. Documento di consulenza: le decisioni spettano a Governo e Parlamento.

**Regole rispettate**
- **Nessun fondo vietato.** Nessuna variante usa DEFICIT, RISPARMI_ATTESI, IVA_EVASIONE, ETS o ALTRO.
- **Fondi usati:**
  - SPESE_FISCALI, la cui capienza nasce solo dalle misure del menu attivate;
  - RIALLOCAZIONE, per i costi informatici dell'Agenzia delle Entrate.
- **Niente doppi conteggi.**
  - Le coperture nuove (FN01-FN04) **non** coincidono con le misure SF01-SF15 del menu né con le aree già coperte: sanità (SF06, SF07), sport (SF08), edilizia (SF09), forfetario (SF02) e cedolare (SF01, SF11).
  - Non sono contati i **7,37 mld** di riordino già nel Piano strutturale di bilancio.
  - Resta però la stessa cautela del menu: la lista delle misure PSB non è pubblica (MEF, Rapporto spese fiscali 2025), quindi la sovrapposizione va verificata con la Relazione di monitoraggio.
- **Il gettito delle abolizioni sta solo nel file delle coperture**, non nelle varianti, per non contarlo due volte.

---

## 1. Il problema: un fisco complicato che pesa su chi ha meno strumenti

### I numeri italiani

| Dato | Valore | Fonte |
|---|---|---|
| Contribuenti IRPEF (anno d'imposta 2024) | 42,8 milioni: 25,2 mln con il 730, 8,4 mln con Redditi PF, 9,2 mln con la sola Certificazione Unica | MEF-DF, *Sintesi dati dichiarazioni 2024* ([finanze.gov.it](https://www1.finanze.gov.it/finanze/analisi_stat/public/v_4_0_0/contenuti/sintesi_analisi_dati_2024_irpef_iva.pdf)) |
| Contribuenti che di fatto non versano IRPEF | 11,3 milioni: imposta netta zero o compensata dal trattamento integrativo | idem |
| 730 precompilati inviati direttamente dai cittadini (campagna 2026) | circa 5,5 milioni; il **31% accettati senza modifiche** | Agenzia Entrate, via [ItaliaOggi](https://www.italiaoggi.it/diritto-e-fisco/fisco/entrate-5-5-mln-di-730-precompilati-il-31-accettati-integralmente-h8gh8p5e) e Fiscal Focus 25/9/2026 (dato parziale a fine settembre) |
| Quota di contribuenti che chiude la dichiarazione "con un clic" | circa **4%** (1,7 mln su 42,8) | calcolo GovernAI dalle due righe precedenti |
| Spese fiscali erariali | 573 misure, di cui **196 sull'IRPEF** per 83,9 mld nel 2026; 58 detrazioni per 74,4 mld | MEF, *Rapporto spese fiscali 2025*, Tav. 13 e Tav. 10 (`dati/raw/01_mef_rapporto_spese_fiscali_2025.txt`) |
| Detrazione 19% per spese sanitarie | 4,87 mld, 22,8 milioni di beneficiari, 213 € in media | idem |
| Aliquote marginali effettive sul lavoro dipendente | **6 di fatto** contro 3 legali; **56,2%** tra 32.000 e 40.000 € nel 2025 | Osservatorio CPI, [*La giungla dell'Irpef per i lavoratori dipendenti*](https://osservatoriocpi.unicatt.it/ocpi-La%20giungla%20dell%20Irpef%20per%20i%20lavoratori%20dipendenti.pdf), 2025 |
| La stessa aliquota marginale effettiva dal 2026 | circa **54%** | stima GovernAI: 33% + 8,7% (riduzione della detrazione da lavoro) + 12,5% (riduzione dell'ulteriore detrazione L. 207/2024), addizionali escluse |
| Ore annue per adempiere agli obblighi fiscali (impresa tipo) | Italia **238**; Estonia 50, Norvegia 79, Finlandia 90, Svezia 122, Danimarca 132, Germania 218 | Banca Mondiale, *Doing Business – Paying Taxes 2020* (dati 2019, ultima edizione: serie sospesa), via [IndexMundi](https://www.indexmundi.com/facts/indicators/IC.TAX.DURS/rankings/europe) |
| Regimi sostitutivi | 48 misure per 12,3 mld; circa 2 milioni di forfetari fuori dall'IRPEF progressiva | MEF RSF 2025; MEF-DF 2024 |

**Cosa manca.**
- Una stima ufficiale recente del costo di adempimento per le **persone fisiche** in Italia, né OCSE né Commissione: non trovata. La serie della Banca Mondiale riguarda le imprese e si ferma al 2019.
- La spesa pubblica per i compensi ai CAF e la spesa privata delle famiglie per l'assistenza fiscale: non verificate. Sono **da quantificare** con i dati MEF-AdE prima della legge di bilancio.

### Cosa fanno gli altri

| Paese | Modello | Dato |
|---|---|---|
| **Danimarca** | *Årsopgørelse*: l'amministrazione calcola l'imposta e invia il conto annuale. Se il cittadino non fa nulla, il conto vale come dichiarazione (silenzio-assenso). | 80% dei cittadini senza alcuna modifica (Skattestyrelsen, [dati 2018](https://sktst.dk/media/Skattestyrelsen/2019/Publikationer_og_tal_&_tendenser/bag-om-danmarks-stoerste-digitale-begivenhed-noegletal-om-aarsopgoerelsen-2018.pdf)) |
| **Svezia** | Dichiarazione precompilata dal 1995; si approva online senza modifiche; rimborso in aprile per chi approva entro marzo | nel 2026, 6,2 milioni su 8,4 (quasi 3 su 4) potevano approvare senza modifiche ([Skatteverket](https://www.skatteverket.se/omoss/pressochmedia/pressmeddelanden/2026/2026/farredeklareradeforstadygnet.5.70685bee19c85dd5dd02aff.html)) |
| **Estonia** | Imposta piatta (22% nel 2026) con poche deduzioni; dichiarazione precompilata in pochi minuti; rimborsi da inizio marzo | 96,4% delle dichiarazioni elettroniche già nel 2020 ([ERR](https://news.err.ee/1115419/more-than-700-000-income-tax-returns-were-filed-in-2020)); impresa tipo: 50 ore l'anno (Banca Mondiale) |
| **Norvegia** | Dichiarazione precompilata (*skattemelding*) che, se corretta, non richiede invio | quota senza azione: non verificata |
| **Finlandia** | "Proposta di imposta" precompilata dal registro dei redditi in tempo reale; se corretta, nessuna azione | — |
| **Spagna, Regno Unito** | Detrazione degli interessi sul mutuo abolita per i nuovi acquisti (Spagna dal 2013, Regno Unito con l'abolizione della MIRAS nel 2000), con salvaguardia dei contratti in corso | riferimento per FN03 |

**La lezione.** Nei Paesi con dichiarazione automatica non conta la tecnologia, che l'Italia ha già: 1,31 miliardi di dati precaricati nel 2026. Contano due cose:
1. **pochi oneri detraibili**, quasi tutti noti all'amministrazione;
2. **il silenzio vale assenso**.

In Italia il 730 precompilato richiede comunque un invio attivo. Ogni detrazione con scontrino, documento o soglia è un motivo per rivolgersi a un intermediario.

### Il problema distributivo nascosto
- Le detrazioni sono **non rimborsabili**: gli 11,3 milioni di contribuenti che non versano IRPEF non ne beneficiano.
- I 9,2 milioni che non presentano la dichiarazione perdono spesso detrazioni a cui avrebbero diritto. Sono soprattutto pensionati e lavoratori con una sola CU, e molti hanno spese mediche registrate nel Sistema Tessera Sanitaria.
- La complessità costa di più a chi ha meno strumenti per gestirla. È un costo regressivo, in contrasto con l'art. 53 Cost. e con il valore EQU della Carta.

---

## Quadro delle varianti (costo lordo a regime, intensità)

| Proposta | PIENA | ESSENZIALE | PILOTA / ZERO | Variante raccomandata |
|---|---|---|---|---|
| 01-P7 Dichiarazione zero | 0,30 · 1 | 0,15 · 0,6 | PILOTA 0,04 · 0,15 | PIENA |
| 01-P8 Meno scontrini: riordino delle detrazioni 19% | 0,35 · 1 | 0,20 · 0,7 | ZERO 0 · 0,4 | ESSENZIALE o PIENA |
| 01-P9 Una sola detrazione per il lavoro, senza scalini | 1,00 · 1 | 0,50 · 0,5 | ZERO 0 · 0,2 | ESSENZIALE |

**Pacchetto raccomandato** (P7 piena, P8 essenziale, P9 essenziale): **circa 1,0 mld/anno a regime**, quasi tutto su SPESE_FISCALI, finanziato dalle nuove coperture FN01-FN04 (1,10-1,54 mld a regime, con FN03 che cresce nel tempo).

**Il saldo è quasi neutro: è una riforma di semplificazione, non un taglio in deficit.**

---

## 01-P7 — Dichiarazione zero: lo Stato fa il conto, il cittadino controlla

**Problema in un dato.** Su 42,8 milioni di contribuenti solo il **4%** circa accetta il 730 precompilato senza modifiche, inviandolo da sé; i 9,2 milioni che non dichiarano perdono spesso detrazioni già note al Fisco. In Danimarca l'80% dei cittadini non tocca il conto annuale.

**Soluzione.** Dal periodo d'imposta 2028 l'Agenzia delle Entrate invia a ogni contribuente con soli redditi certificati un **conto fiscale annuale di una pagina**. Riguarda il lavoro dipendente, le pensioni, i redditi assimilati, le locazioni in cedolare e i forfetari. Il conto indica:
- redditi;
- detrazioni già note: spese sanitarie dal Sistema Tessera Sanitaria, mutui, contributi, familiari a carico;
- imposta dovuta;
- rimborso o debito.

Le regole:
- **Silenzio-assenso.** Senza risposta entro il 30 giugno il conto è definitivo.
- **Rimborso automatico** entro luglio sull'IBAN già comunicato o tramite il sostituto d'imposta; il debito si paga con addebito o trattenuta in busta paga o sulla pensione.
- **Chi deve correggere** lo fa online, con il CAF o allo sportello, entro il 30 settembre, sul **modulo a pagina unica**.
- **Il 730 e il modello Redditi** restano solo per redditi d'impresa, partecipazioni, redditi esteri e altri casi complessi.
- **Esonerati senza obbligo**, cioè la sola CU: ricevono lo stesso conto, solo **a credito**. Se lo Stato deve loro un rimborso lo paga, se non deve nulla il conto è solo informativo. Nessun nuovo debito per chi oggi non dichiara.

**Garanzie.**
- Nessuna sanzione su errori dei dati precaricati.
- Controlli formali esclusi sui dati forniti da terzi, come già per il precompilato accettato.
- Decisione sempre umana sui contestati (GDPR art. 22; L. 132/2025).
- Nessun nuovo flusso di dati personali oltre l'IBAN.

**Varianti**

| Variante | Contenuto | Costo a regime | Intensità |
|---|---|---|---|
| PIENA | conto automatico per tutti i redditi certificati, compresi i 9,2 mln con sola CU (solo a credito); silenzio-assenso; rimborsi automatici | 0,30 (0,27 SPESE_FISCALI + 0,03 RIALLOCAZIONE) | 1 |
| ESSENZIALE | silenzio-assenso per chi ha presentato il 730 l'anno precedente e per i pensionati con sola CU; altri non dichiaranti esclusi | 0,15 (0,13 + 0,02) | 0,6 |
| PILOTA | modello pieno in 3 regioni (una per ripartizione) per 2 anni, con valutazione | 0,04 (0,03 + 0,01) | 0,15 |

**Costo: da dove viene (stima GovernAI).**
- **Costo informatico:** 20-40 mln/anno per l'Agenzia delle Entrate, oltre alla gestione del precompilato già esistente.
- **Costo vero: le detrazioni oggi non chieste.** I 9,2 mln con sola CU che hanno imposta da ridurre, spese sanitarie oltre la franchigia di 129 € o altri oneri noti sono **2-3 milioni** di persone, con un rimborso medio di **80-120 €**: **0,15-0,35 mld**.
- **Non è uno spreco:** è un diritto oggi non esercitato. È un costo da coprire perché riduce il gettito rispetto alla legislazione vigente.
- **Non contati come copertura:** i minori compensi ai CAF (art. 38 d.lgs. 241/1997) e il minore contenzioso. Sono risparmi certificabili solo ex post.

**Articolato normativo essenziale** (disegno di legge, collegato alla legge di bilancio; modifica del d.lgs. 175/2014 e del d.P.R. 600/1973)

> **Art. 1 (Conto fiscale annuale).** 1. A decorrere dal periodo d'imposta 2028, l'Agenzia delle entrate mette a disposizione di ciascun contribuente titolare esclusivamente di redditi oggetto di certificazione o comunicazione da parte di terzi un conto fiscale annuale, redatto su un unico foglio, contenente i redditi, gli oneri detraibili e deducibili noti, l'imposta dovuta e il saldo, entro il 30 aprile dell'anno successivo.
> 2. Il conto fiscale si intende accettato e tiene luogo della dichiarazione dei redditi se il contribuente non presenta, entro il 30 giugno, una dichiarazione rettificativa nella forma semplificata di cui all'articolo 2.
> 3. Per i contribuenti esonerati dall'obbligo di dichiarazione il conto fiscale è emesso solo se determina un credito d'imposta; in nessun caso determina un debito d'imposta non già assolto tramite sostituto.
>
> **Art. 2 (Dichiarazione a pagina unica).** 1. Con provvedimento del Direttore dell'Agenzia delle entrate è approvato un modello di dichiarazione semplificata, di una sola pagina, per i contribuenti con redditi di lavoro, di pensione, fondiari e assoggettati a regimi sostitutivi, che riporta i soli dati da integrare o rettificare rispetto al conto fiscale.
>
> **Art. 3 (Rimborsi automatici).** 1. I rimborsi derivanti dal conto fiscale accettato sono erogati entro il 31 luglio, tramite sostituto d'imposta o accredito sul conto corrente comunicato all'Agenzia; in mancanza dell'IBAN, l'Agenzia invita il contribuente a comunicarlo tramite i canali digitali e assistiti.
>
> **Art. 4 (Garanzie).** 1. Sui dati forniti da terzi e riportati nel conto fiscale accettato non si applicano sanzioni né controlli formali a carico del contribuente. Il contribuente può chiedere la rettifica entro il termine di decadenza dell'accertamento. Ogni decisione sfavorevole è adottata da un funzionario.
>
> **Art. 5 (Copertura).** 1. Agli oneri, pari a 30 milioni per il 2027, 150 milioni per il 2028 e 300 milioni annui dal 2029, si provvede: quanto a 30 milioni annui mediante riduzione delle spese di funzionamento dell'Agenzia delle entrate; quanto alla restante parte con le maggiori entrate derivanti dalle disposizioni di riordino delle detrazioni di cui alla proposta 01-P8 e alle misure FN01-FN04.

**Cronoprogramma**
- **Primi 100 giorni:**
  - ddl presentato;
  - gruppo di lavoro AdE-Sogei-SOSE;
  - consultazione di CAF, professionisti e associazioni di consumatori e pensionati;
  - DPIA con il Garante.
- **Entro 12 mesi:**
  - legge approvata;
  - modulo a pagina unica approvato;
  - campagna IBAN su App IO e cedolino della pensione;
  - test sui dati 2027 in parallelo, non vincolante.
- **Entro fine legislatura:**
  - due campagne con il conto automatico (redditi 2028 e 2029);
  - valutazione pubblica dell'UPB;
  - estensione ai forfetari con dati della fatturazione elettronica.

**Indicatori**

| KPI | Base (dato, anno, fonte) | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Contribuenti che chiudono senza modifiche (accettazione o silenzio) | circa 4%, 2026 (stima GovernAI su dati AdE) | 40% | 60% (Danimarca: 80%) |
| Rimborsi entro il 31 luglio, quota sul totale | non rilevato, 2026 | 70% | 90% |
| Contribuenti con sola CU che ricevono un credito prima perso | 0, 2026 | 2 milioni | 3 milioni |
| Fiducia nell'Agenzia delle Entrate e adempimento spontaneo (tax compliance, valore CIT) | da rilevare con indagine AdE nel 2027 | +5 punti | +10 punti |

**Rischi e mitigazioni**
- **Esclusione digitale delle persone anziane.** Il conto arriva anche per posta o tramite il cedolino della pensione; CAF e patronati restano un canale assistito gratuito, finanziato a prestazione.
- **Errori nei dati di terzi.** Sono i terzi a rispondere delle comunicazioni; non ci sono sanzioni per il contribuente e c'è un anno per rettificare.
- **Opposizione degli intermediari.** Nuova funzione dei CAF come consulenti per i casi complessi e per l'accesso ai benefici (ISEE, Assegno unico) e transizione in 3 anni dei compensi.
- **Costo superiore alla stima per i crediti non chiesti.** Variante ESSENZIALE prima; clausola di monitoraggio art. 17 L. 196/2009.
- **Privacy.** Nessun incrocio nuovo: solo dati che l'Anagrafe tributaria già riceve per legge.

---

## 01-P8 — Meno scontrini: riordino delle detrazioni del 19%

**Problema in un dato.**
- L'IRPEF ha 196 spese fiscali. Per molte detrazioni del 19% il beneficio medio è di poche decine di euro:
  - veterinarie: 44,5 € per 1,7 mln di beneficiari;
  - assicurazioni vita e infortuni: 53,4 € per 5,3 mln;
  - istruzione: 166 € per 4,4 mln (MEF RSF 2025).
- Ognuna richiede documenti, soglie e verifiche, e impedisce la dichiarazione automatica.
- Le detrazioni non arrivano agli 11,3 mln di incapienti.

**Soluzione.** Dal periodo d'imposta 2028:
1. **Abolizione** delle detrazioni 19% per:
   - **premi assicurativi vita e infortuni**, mantenendo quelli per **non autosufficienza** e per la tutela di persone con **disabilità grave**;
   - **spese veterinarie**;
   - **spese di istruzione** (scuola e università). Restano le detrazioni per canoni dei **fuori sede** e per gli studenti con DSA (misure FN01, FN02).
2. **Detrazione degli interessi sul mutuo prima casa** solo per i contratti stipulati fino al 31/12/2027; nessuna detrazione per i nuovi mutui (FN03, modello Spagna 2013 e Regno Unito 2000).
3. **"Quota studio" dell'Assegno unico** per i figli da 6 a 21 anni che frequentano scuola o università, decrescente con l'ISEE: è la compensazione per le famiglie a reddito medio-basso che perdono la detrazione per istruzione. È rimborsabile, quindi raggiunge anche gli incapienti.
4. Le detrazioni che restano sono quasi tutte **già note all'Agenzia**: sanità, mutui in corso, affitti, contributi, erogazioni liberali tracciate. È ciò che rende possibile il conto automatico (01-P7).

**Varianti**

| Variante | Contenuto | Costo lordo a regime | Intensità |
|---|---|---|---|
| PIENA | abolizioni (1) e (2) e quota studio AUU per ISEE ≤30.000 € (circa 60-80 €/anno per figlio, decrescente) | 0,35 (SPESE_FISCALI) | 1 |
| ESSENZIALE | stesse abolizioni; quota studio solo per ISEE ≤20.000 € | 0,20 (SPESE_FISCALI) | 0,7 |
| ZERO | solo abolizioni, senza compensazione | 0 | 0,4 |

**Il gettito delle abolizioni non è in queste righe.** È nelle coperture FN01, FN02 e FN03 (`coperture_nuove_fisco.csv`), insieme a 0,85-1,40 mld a regime. **01-P8 va attivata insieme a FN01 e FN02**: l'ottimizzatore dovrebbe legarle. La variante ZERO senza le coperture non ha senso.

**Coerenza con la Carta e con l'art. 53.**
- Il prelievo aggiuntivo grava su chi oggi usa le detrazioni, cioè contribuenti capienti, in prevalenza dei decili medio-alti.
- La compensazione va ai decili bassi tramite l'AUU, che è rimborsabile.
- La progressività del sistema aumenta: il beneficio di una detrazione al 19% non rimborsabile è nullo sotto la soglia di capienza e costante sopra.
- Le spese legate alla salute, alla disabilità e alla non autosufficienza non sono toccate (RIS).

**Articolato normativo essenziale** (legge di bilancio; modifica degli artt. 15 e 16-ter TUIR e del d.lgs. 230/2021)

> **Art. 1 (Riordino degli oneri detraibili).** 1. All'articolo 15 del TUIR, a decorrere dal periodo d'imposta 2028: a) al comma 1, le lettere e) ed e-bis) sono abrogate; restano ferme le lettere i-sexies) e le detrazioni per studenti con disturbi specifici dell'apprendimento; b) al comma 1, la lettera f) è sostituita dalla seguente: «f) i premi per assicurazioni aventi per oggetto il rischio di non autosufficienza nel compimento degli atti della vita quotidiana e il rischio di morte finalizzate alla tutela delle persone con disabilità grave, nei limiti vigenti»; c) al comma 1, la lettera c-bis) è abrogata.
> 2. La detrazione di cui all'articolo 15, comma 1, lettera b), del TUIR spetta per gli interessi relativi ai contratti di mutuo stipulati entro il 31 dicembre 2027.
>
> **Art. 2 (Quota studio dell'assegno unico).** 1. All'articolo 4 del d.lgs. 29 dicembre 2021, n. 230, è aggiunta una maggiorazione annua per ciascun figlio di età compresa tra 6 e 21 anni iscritto a un percorso di istruzione o formazione, di importo decrescente in funzione dell'ISEE fino ad azzerarsi a 30.000 euro, nel limite di spesa di 350 milioni annui dal 2028.
>
> **Art. 3 (Clausola di valutazione).** 1. Entro il 2031 la Commissione per le spese fiscali pubblica la distribuzione per decili degli effetti degli articoli 1 e 2, calcolata con i dati delle dichiarazioni.

**Cronoprogramma**
- **Primi 100 giorni:** microsimulazione MEF-DF e UPB per decile; decisione sulla variante.
- **Entro 12 mesi:** legge di bilancio 2028; decreto attuativo INPS per la quota studio; comunicazione chiara alle famiglie con un anno di anticipo.
- **Entro fine legislatura:** prima campagna dichiarativa senza le detrazioni abolite (2029); valutazione distributiva pubblica.

**Indicatori**

| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Numero di spese fiscali IRPEF | 196, 2025 (MEF RSF) | 185 | ≤170, con 01-P2 |
| Oneri del 19% non noti all'Agenzia (da documentare) | da rilevare con AdE, 2027 | -50% | -70% |
| Famiglie con ISEE ≤30.000 € e figli 6-21 anni che ricevono la quota studio | 0, 2027 | 80% degli aventi diritto | 90% |

**Rischi e mitigazioni**
- **Scuole paritarie e università non statali.** La detrazione oggi vale in media 166 €: un effetto modesto sulla scelta della scuola. Per gli studenti universitari a basso reddito c'è già l'esonero dalle tasse in base all'ISEE.
- **Mutui: accesso alla casa dei giovani.** I contratti in corso restano salvi. Per i nuovi acquisti restano la garanzia Consap per gli under 36 e le politiche dell'area 04. L'eliminazione riduce la capitalizzazione del beneficio nei prezzi (evidenza spagnola e britannica).
- **Consenso.** Le detrazioni piccole sono molto diffuse: 5,3 milioni di persone per le assicurazioni. La riforma va presentata insieme, nella stessa legge, a 01-P7 (niente più dichiarazione) e a 01-P9 (meno tasse sul lavoro).

---

## 01-P9 — Una sola detrazione per il lavoro, senza scalini

**Problema in un dato.** Tra 32.000 e 40.000 € di reddito un lavoratore dipendente paga circa **54 centesimi di imposta su ogni euro in più** nel 2026 (56,2% nel 2025, Osservatorio CPI), più di chi guadagna 100.000 € (43% più addizionali).

La causa sono tre strumenti sovrapposti, introdotti in anni diversi:
- la detrazione da lavoro (art. 13 TUIR);
- la somma esente;
- l'ulteriore detrazione di 1.000 € che si azzera tra 32.000 e 40.000 € (L. 207/2024).

È un'anomalia contraria alla progressività ordinata richiesta dall'art. 53 Cost.

**Soluzione.**
- Un'**unica "detrazione per il lavoro"**, con una sola formula che sostituisce i tre strumenti a parità di importo per tutti i redditi fino a 32.000 €.
- L'**uscita graduale** si allunga da 32.000 a 50.000 € (PIENA) o a 44.000 € (ESSENZIALE).
- L'aliquota marginale effettiva massima per il lavoro dipendente scende da circa 54% a circa **47%** (PIENA) o **50%** (ESSENZIALE). Calcolo GovernAI: 33% + 8,7% + 1.000/18.000 = 5,6% (PIENA) o 1.000/12.000 = 8,3% (ESSENZIALE).
- Per il datore di lavoro la busta paga usa **una sola formula**.

**Varianti**

| Variante | Contenuto | Costo lordo a regime | Intensità |
|---|---|---|---|
| PIENA | detrazione unica; uscita graduale 32-50.000 € | 1,00 (SPESE_FISCALI) | 1 |
| ESSENZIALE | detrazione unica; uscita graduale 32-44.000 € | 0,50 (SPESE_FISCALI) | 0,5 |
| ZERO | solo unificazione dei tre strumenti in una formula, a parità di importi e di scalini | 0 | 0,2 |

**Costo (stima GovernAI, da verificare con microsimulazione MEF-DF).**
- I lavoratori dipendenti con reddito tra 32.000 e 50.000 € sono circa **4 milioni**: 2,3 tra 32 e 40.000 €, 1,7 tra 40 e 50.000 €. È una stima dalle distribuzioni MEF-DF, perché il 76,6% dei contribuenti dichiara meno di 35.000 €.
- **PIENA:** guadagno da 0 a 556 €, in media circa 250-280 €, quindi **0,9-1,1 mld**.
- **ESSENZIALE:** circa 3 milioni di lavoratori, guadagno medio circa 170 €, quindi **0,45-0,55 mld**.

**Articolato normativo essenziale** (legge di bilancio; modifica dell'art. 13 TUIR e dell'art. 1, commi 4-9, L. 207/2024)

> **Art. 1 (Detrazione unica per il lavoro).** 1. A decorrere dal periodo d'imposta 2028, la detrazione di cui all'articolo 13, comma 1, del TUIR, la somma di cui all'articolo 1, comma 4, e l'ulteriore detrazione di cui all'articolo 1, comma 6, della legge 30 dicembre 2024, n. 207, sono sostituite da un'unica detrazione per redditi di lavoro dipendente, determinata secondo la tabella allegata. Fino a 32.000 euro di reddito complessivo la nuova detrazione non è inferiore alla somma dei benefici sostituiti.
> 2. Per i redditi compresi tra 32.000 e 50.000 euro, la componente aggiuntiva di 1.000 euro si riduce in misura lineare fino ad azzerarsi a 50.000 euro.
> 3. Il sostituto d'imposta applica la detrazione in un'unica formula mensile; la somma esente è convertita in detrazione equivalente, con salvaguardia del trattamento integrativo.
>
> **Art. 2 (Copertura).** 1. Agli oneri, pari a 1.000 milioni annui dal 2028, si provvede con le maggiori entrate delle misure di riordino delle spese fiscali FN01-FN04 e, per la parte residua, con le misure del menu coperture del fondo SPESE_FISCALI attivate con la stessa legge.

**Cronoprogramma**
- **Primi 100 giorni:** microsimulazione per decile e per aliquota marginale effettiva (MEF-DF, UPB); tabella di conversione.
- **Entro 12 mesi:** legge di bilancio 2028; istruzioni ai sostituti d'imposta entro novembre 2027.
- **Entro fine legislatura:** verifica delle aliquote marginali effettive; estensione della logica a pensioni e lavoro autonomo, cioè una sola curva per tipo di reddito.

**Indicatori**

| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Aliquota marginale effettiva massima sul lavoro dipendente sotto i 50.000 € | circa 54%, 2026 (stima GovernAI; 56,2% nel 2025, OCPI) | ≤47% (PIENA) / ≤50% (ESS.) | ≤47% |
| Numero di aliquote marginali effettive distinte sul lavoro dipendente | 6, 2025 (OCPI) | 4 | 3-4 |
| Strumenti di detrazione per il lavoro dipendente | 3 (art. 13, somma esente, ulteriore detrazione) | 1 | 1 |

**Rischi e mitigazioni**
- **"Taglio per il ceto medio" e non per i poveri.** È vero: 01-P9 va ai decili 8-9. Va letta insieme a 01-P7 e 01-P8, che danno ai decili bassi (vedi la tabella dei decili). La variante ESSENZIALE dimezza il costo.
- **Interazione con l'ISEE e le prestazioni.** Le aliquote implicite oltre il 100% citate dall'OCPI nascono dall'ISEE, non dall'IRPEF: da coordinare con l'area 02.
- **Politica invariata del 2027.** Il secondo scaglione esteso a 55.000 € (1,4 mld, solo 2027) è un'alternativa più costosa che non tocca lo scalino. 01-P9 è proposta **al posto** del suo rinnovo, non in aggiunta.

---

## 2. Chi guadagna e chi perde, per decile

**Stima GovernAI ordinale. Non ci sono microdati.**

**Metodo.**
- I decili sono dei contribuenti IRPEF per reddito complessivo. Le soglie sono stimate dalle statistiche MEF-DF 2024: il 47% dei contribuenti è sotto 20.000 € (OCPI), il 76,6% sotto 35.000 € (MEF-DF).
- Le soglie approssimate sono:
  - D1-D3: sotto 12.000 €;
  - D4-D5: 12-20.000 €;
  - D6-D7: 20-30.000 €;
  - D8: 30-38.000 €;
  - D9: 38-55.000 €;
  - D10: oltre 55.000 €.
- Gli effetti per misura sono distribuiti con:
  - la platea e il beneficio medio del Rapporto spese fiscali 2025;
  - l'ipotesi che le detrazioni del 19% siano usate in proporzione all'imposta lorda capiente (assunzione, non dato).
- Variante considerata: PIENA per P7 e P8 ed ESSENZIALE per P9, con FN01-FN04 attive.

| Decile | 01-P7 conto automatico | 01-P8 + FN01-FN03 riordino | 01-P9 (ESS.) | FN04 premi | **Effetto netto medio** |
|---|---|---|---|---|---|
| D1-D3 | **+** crediti oggi persi (pensionati, CU) | ≈0: incapienti, non usano detrazioni; **+** quota studio AUU | 0 | 0 | **guadagno piccolo** (+10/+40 € medi; di più per chi ha spese mediche) |
| D4-D5 | **+** | **–** istruzione e assicurazioni (circa 30-60 € medi); **+** quota studio per le famiglie con ISEE basso | 0 | 0 | **circa neutro**; guadagno per le famiglie con figli |
| D6-D7 | + piccolo | **–** circa 50-90 € medi; quota studio parziale | 0 | 0 | **perdita piccola** (–30/–70 €) |
| D8 | ≈0 | **–** circa 80-110 € | **+** fino a 333 € (media circa 150) | 0 | **guadagno** (+40/+80 €) |
| D9 | ≈0 | **–** circa 100-130 € | **+** media circa 100 € (32-44.000 €) | – piccola | **circa neutro** |
| D10 | 0 | **–** circa 100-150 €: istruzione, assicurazioni, mutui nuovi (già ridotti sopra 75.000 € dal tetto L. 207/2024) | 0 | **–** (premi fino a 80.000 €) | **perdita** (–100/–200 €) |

**Lettura.**
- Il pacchetto è **leggermente progressivo**:
  - guadagnano i decili bassi (crediti oggi persi, quota studio) e il ceto medio nello scalino 32-44.000 €;
  - perdono in modo moderato il decile più alto e una parte dei decili centrali che usano molte detrazioni.
- **Dentro ogni decile** chi perde è chi oggi usa più detrazioni (scuole e università a pagamento, polizze vita, nuovi mutui). Chi guadagna è chi non le usa o non le può usare.
- Non ci sono variazioni per gli incapienti in senso negativo: **nessun aumento di imposta per i decili 1-3** (linea rossa EQU e art. 3, comma 2, Cost.).

**Limiti.**
- Senza microsimulazione non si conoscono la sovrapposizione tra misure nella stessa famiglia né la distribuzione per famiglia (equivalente ISEE) invece che per contribuente.
- Gli importi sono **ordini di grandezza**.
- La prima azione dei 100 giorni è chiedere a MEF-DF e UPB la microsimulazione sui dati delle dichiarazioni.

---

## 3. Coerenza con la Carta (orizzonte medio, valutazione dell'autore da sottoporre al panel)

| Valore | 01-P7 | 01-P8 | 01-P9 | Motivo |
|---|---|---|---|---|
| RIS | +2 | 0 | +1 | la persona non è una pratica; sanità e disabilità salve |
| FID | +3 | +2 | +2 | regole comprensibili, meno arbitrio, rimborsi certi |
| INN | +2 | +1 | 0 | servizio proattivo con dati esistenti |
| BEN | +1 | 0 | +1 | tempo e costi risparmiati; più reddito netto nello scalino |
| APC | 0 | –1/0 | 0 | detrazione istruzione tolta, compensata per i redditi bassi |
| BPA | 0 | 0 | 0 | — |
| FUT | 0 | +1 | 0 | meno spese fiscali, nessun deficit |
| EQU | +2 | +1 | 0/+1 | crediti agli esclusi; beneficio non rimborsabile sostituito da uno rimborsabile; scalino rimosso |
| SIC | 0 | 0 | 0 | nessuna nuova raccolta di dati |
| CIT | +2 | +1 | +1 | lealtà fiscale: lo Stato fa la sua parte, il cittadino controlla |

## 4. Fonti principali
- MEF-DF, *Sintesi dati dichiarazioni IRPEF e IVA, anno d'imposta 2024* ([finanze.gov.it](https://www1.finanze.gov.it/finanze/analisi_stat/public/v_4_0_0/contenuti/sintesi_analisi_dati_2024_irpef_iva.pdf)).
- MEF, *Rapporto annuale spese fiscali 2025* ([mef.gov.it](https://www.mef.gov.it/export/sites/MEF/documenti-allegati/2025/RSF-2025-bis.pdf)), Tav. 7-13 e schede delle misure 171, 192, 232, 279, 313, 319 e seguenti.
- Agenzia delle Entrate, campagna precompilata 2026, via [ItaliaOggi](https://www.italiaoggi.it/diritto-e-fisco/fisco/entrate-5-5-mln-di-730-precompilati-il-31-accettati-integralmente-h8gh8p5e) (dato parziale): **da sostituire con il comunicato finale dell'Agenzia**.
- Osservatorio CPI, [*La giungla dell'Irpef per i lavoratori dipendenti*](https://osservatoriocpi.unicatt.it/ocpi-La%20giungla%20dell%20Irpef%20per%20i%20lavoratori%20dipendenti.pdf), 2025.
- Banca Mondiale, *Doing Business 2020 – Paying Taxes* ([archivio](https://archive.doingbusiness.org/en/reports/thematic-reports/paying-taxes-2020)).
- Skatteverket ([2026](https://www.skatteverket.se/omoss/pressochmedia/pressmeddelanden/2026/2026/farredeklareradeforstadygnet.5.70685bee19c85dd5dd02aff.html)); Skattestyrelsen ([2018](https://sktst.dk/media/Skattestyrelsen/2019/Publikationer_og_tal_&_tendenser/bag-om-danmarks-stoerste-digitale-begivenhed-noegletal-om-aarsopgoerelsen-2018.pdf)); EMTA ([redditi 2025](https://emta.ee/en/private-client/taxes-and-payment/declaration-income/income-tax-returns-2025)).
- OCSE, *Tax Administration 2025* (doi 10.1787/cc015ce8-en): non consultato nel dettaglio. La quota di Paesi OCSE con precompilazione (circa tre quarti nel 2020) viene da [Tax Policy Center](https://taxpolicycenter.org/briefing-book/what-are-prepopulated-tax-returns).
