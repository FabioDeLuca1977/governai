# Schede pronte — Area 07: Giustizia, Interno, Difesa

*Agente ministeriale GovernAI, 7 novembre 2026. Varianti in `programma/varianti/07_giustizia.csv`. Dati da `dati/serie/07_*.csv` e `dati/verifiche/07_giustizia.md`. Importi in mld €/anno; i costi sono stime GovernAI, non quantificazioni RGS.*

**Regole rispettate.** Nessuna variante usa DEFICIT, RISPARMI_ATTESI, IVA_EVASIONE, ETS o ALTRO. I risparmi attesi (minori presenze in carcere, minori indennizzi Pinto, minori costi di accoglienza) sono indicati ma **non contati**: si certificano ex post e riducono il prelievo. Coesione e AMIF finanziano solo costi una tantum 2027-29, mai personale stabile.

**Nuova copertura segnalata all'agente coperture.** Contributo unificato maggiorato per i litiganti seriali (oltre 500 cause l'anno): 0,10-0,15 mld/anno, DRM. Nel CSV è imputata a RIALLOCAZIONE (bilancio Giustizia) in attesa di un fondo dedicato.

| Proposta | PIENA | ESSENZIALE | PILOTA / ZERO |
|---|---|---|---|
| 07-C1 Giustizia a regime | 0,55 (int. 1) | 0,32 (0,7) | PILOTA 0,10 (0,15) |
| 07-C2 Pena utile | 0,45 (1) | 0,25 (0,6) | PILOTA 0,06 (0,15) |
| 07-C3 Flussi migratori | 0,55 (1) | 0,25 (0,55) | PILOTA 0,04 (0,15) |
| 07-C4 Beni confiscati | 0,15 (1) | 0,07 (0,6) | PILOTA 0,02 (0,2) |
| 07-C5 Difesa | +32,0 al 2035 (1) | +9,1 al 2034 (0,35) | ZERO 0 (0,1) |
| 07-C6 Scudo cyber | 0,35 (1) | 0,18 (0,6) | PILOTA 0,03 (0,2) |
| **Totale senza Difesa** | **2,05** | **1,07** | **0,25** |

---

## 07-C1 — Giustizia a regime: Ufficio per il processo e triage digitale

**Problema in un dato.** Disposition time civile (tre gradi): **2.512 giorni nel 2019, 1.789 nel 2025 (−28,8%), 1.251 nel I semestre 2026 (−50,2%)**. Il target PNRR è raggiunto, ma con circa 10.000 addetti finanziati dal PNRR fino al 30/6/2026 (Ministero della Giustizia, *Continuous Monitoring PNRR 2025* e *Relazione PNRR* agosto 2026; `07_disposition_time_pnrr.csv`). Senza quel personale i tempi rischiano di risalire dal 2027.

**Soluzione.** Rendere permanente una quota dell'Ufficio per il processo con un concorso riservato e assegnarla ai tribunali più lenti. Introdurre nel Processo civile telematico un triage che classifica le cause e propone il calendario; la decisione resta sempre al giudice. Pubblicare ogni trimestre un cruscotto per tribunale.

| Variante | Contenuto | Costo a regime | Intensità | Copertura |
|---|---|---|---|---|
| PIENA | 7.000 UPP + 500 tecnici + triage + cruscotto | 0,55 (dal 2028) | 1 | RIALLOCAZIONE 0,25 (FUG, contributo unificato litiganti seriali); SPESE_FISCALI 0,30 |
| ESSENZIALE | 4.500 UPP nei tribunali sopra la mediana + triage | 0,32 | 0,7 | RIALLOCAZIONE 0,15; SPESE_FISCALI 0,17 |
| PILOTA | 1.500 UPP in 20 tribunali, valutazione controfattuale | 0,10 | 0,15 | RIALLOCAZIONE 0,10 |

**Articolato normativo essenziale** (legge di bilancio 2027, sezione I)

> **Art. 1 (Finalità).** Al fine di consolidare la riduzione della durata dei procedimenti civili e penali conseguita con il PNRR e di assicurare il rispetto dell'articolo 111 della Costituzione, il presente articolo dispone la stabilizzazione dell'Ufficio per il processo e l'introduzione di strumenti digitali di organizzazione del lavoro giudiziario.
>
> **Art. 2 (Stabilizzazione).** 1. Il Ministero della giustizia è autorizzato a bandire, entro il 30 giugno 2027, procedure concorsuali riservate per l'assunzione a tempo indeterminato di [7.000 / 4.500 / 1.500] unità di addetti all'Ufficio per il processo e di [500 / 0 / 0] unità di personale tecnico, tra il personale assunto a tempo determinato con risorse PNRR, ai sensi dell'articolo 22 del decreto-legge 2 marzo 2024, n. 19. 2. Il personale è assegnato con decreto del Ministro, sentito il CSM, in proporzione ai carichi e al disposition time di ciascun ufficio.
>
> **Art. 3 (Triage digitale).** 1. La DGSIA sviluppa nel Processo civile telematico un modulo di classificazione delle cause per materia e complessità, di proposta di calendario e di individuazione del contenzioso seriale. 2. Il modulo svolge funzioni esclusivamente organizzative; ogni atto incidente sul procedimento è adottato dal giudice, che può disattendere la proposta. Le parti possono contestare la classificazione. 3. Il sistema è iscritto in un registro pubblico degli algoritmi ed è soggetto a valutazione d'impatto ai sensi del regolamento (UE) 2024/1689 e a un audit indipendente biennale.
>
> **Art. 4 (Trasparenza e revisione).** 1. Il Ministero pubblica ogni trimestre, per ciascun ufficio, disposition time, pendenze ultratriennali e indennizzi ex legge 89/2001. 2. Dopo ventiquattro mesi, negli uffici in cui il disposition time non si è ridotto almeno del 10%, il personale è riassegnato.
>
> **Art. 5 (Contributo unificato per il contenzioso seriale).** All'articolo 13 del DPR 115/2002 è aggiunto un comma: per le parti che hanno iscritto più di 500 cause nell'anno precedente, il contributo dovuto è maggiorato del 50%. Sono escluse le controversie di lavoro, previdenza, famiglia e consumo promosse da persone fisiche.
>
> **Art. 6 (Copertura finanziaria).** Agli oneri, pari a [450 / 270 / 80] milioni di euro per il 2027 e a [550 / 320 / 100] milioni annui dal 2028, si provvede: a) quanto a [120 / 90 / 0] milioni, con le maggiori entrate di cui all'articolo 5; b) quanto a [130 / 60 / 100] milioni, con la quota del Fondo unico giustizia spettante al Ministero della giustizia e la riduzione di autorizzazioni di spesa del Ministero; c) per la parte restante, con le maggiori entrate derivanti dal riordino delle spese fiscali disposto dalla presente legge.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | Norma in legge di bilancio; proroga ponte dei contratti in scadenza; bando di concorso; specifiche del triage | Ministero della Giustizia (DOG, DGSIA), MEF, CSM (parere) |
| 12 mesi | Assunzioni concluse; triage attivo in 20 tribunali; primo cruscotto trimestrale; valutazione d'impatto AI Act | DGSIA, capi degli uffici, Garante privacy |
| Fine legislatura | Triage in tutti i tribunali; revisione a 24 mesi con riassegnazione del personale; audit indipendente | Ministero, CSM, Corte dei conti |

**Indicatori**

| KPI | Base | Obiettivo 3 anni (2029) | Obiettivo 5 anni (2031) |
|---|---|---|---|
| Disposition time civile, tre gradi (annuale) | 1.789 giorni, 2025 (Min. Giustizia) | ≤ 1.550 | ≤ 1.400 |
| Disposition time civile in tribunale | 435 giorni, 2025 (Min. Giustizia) | ≤ 390 | ≤ 360 |
| Disposition time penale, tre gradi | 958 giorni, 2025 (Min. Giustizia) | ≤ 880 | ≤ 830 |

**Rischi e mitigazione.** Erosione dei guadagni nel 2027 per ritardi nei concorsi: proroga ponte dei contratti finanziata nella stessa norma. Bias di automazione del triage: funzioni solo organizzative, audit, diritto di contestazione. Calo di produttività dopo il "rush" PNRR: cruscotto pubblico e riassegnazione a 24 mesi. Opposizione delle grandi imprese al contributo maggiorato: soglia alta ed esenzioni per le persone fisiche.

---

## 07-C2 — Pena utile: misure di comunità contro il sovraffollamento

**Problema in un dato.** Al 30/9/2026 erano presenti **66.063 persone detenute** per **51.295 posti regolamentari** in 189 istituti: affollamento del **128,8%**; 20.856 persone detenute hanno cittadinanza straniera (DAP; `07_detenuti_dap.csv`). Sui posti effettivamente disponibili Antigone stima il 139,7% (fonte non governativa). Un detenuto costa circa 178 € al giorno (COFOG carceri 2024 / presenze medie DAP, elaborazione GovernAI).

**Soluzione.** Per chi ha un residuo di pena fino a 2 anni ed è a basso rischio, valutare d'ufficio l'accesso a misure alternative con controllo sul territorio e lavoro. Rafforzare gli UEPE prima di allargare l'accesso. Avviare case di reinserimento per il fine pena e recuperare i posti inagibili. Introdurre una statistica ufficiale sulla recidiva.

| Variante | Contenuto | Costo a regime | Intensità | Copertura |
|---|---|---|---|---|
| PIENA | Misure alternative ≤2 anni + 1.500 UEPE + 2.000 posti in case di reinserimento + Smuraglia + braccialetti + posti inagibili + recidiva | 0,45 (dal 2029) | 1 | RIALLOCAZIONE 0,15; SAD 0,30; coesione 0,05/anno una tantum 2027-29 |
| ESSENZIALE | Misure alternative + 1.000 UEPE + braccialetti + recidiva | 0,25 | 0,6 | RIALLOCAZIONE 0,10; SAD 0,15 |
| PILOTA | 3 distretti, valutazione a 36 mesi | 0,06 | 0,15 | RIALLOCAZIONE 0,06 |

I risparmi da minori presenze (3.000 persone detenute in meno valgono circa 0,2 mld/anno) **non sono contati**: dopo la certificazione riducono il prelievo dai fondi.

**Articolato normativo essenziale** (legge delega e decreto legislativo)

> **Art. 1 (Finalità).** In attuazione degli articoli 13 e 27 della Costituzione e dell'articolo 3 della CEDU, la presente legge riduce il sovraffollamento penitenziario e la recidiva favorendo l'esecuzione della pena nella comunità per i condannati a basso rischio.
>
> **Art. 2 (Valutazione d'ufficio per le misure alternative).** 1. Il Governo è delegato ad adottare, entro dodici mesi, un decreto legislativo che preveda la valutazione d'ufficio, da parte del magistrato di sorveglianza, dell'ammissione a misure alternative dei condannati con pena residua non superiore a due anni, esclusi i delitti di cui all'articolo 4-bis della legge 354/1975. 2. La valutazione si fonda su un programma di trattamento predisposto dall'UEPE e su strumenti strutturati di valutazione del rischio; il braccialetto elettronico è disponibile entro 48 ore dal provvedimento.
>
> **Art. 3 (Esecuzione penale esterna e case di reinserimento).** 1. Il Ministero della giustizia è autorizzato ad assumere [1.500 / 1.000 / 250] funzionari di servizio sociale, psicologi e mediatori per gli UEPE. 2. Sono istituite case di reinserimento a bassa sicurezza per i detenuti con fine pena entro diciotto mesi, in immobili pubblici dismessi o beni confiscati assegnati ai sensi del d.lgs. 159/2011.
>
> **Art. 4 (Lavoro).** Il credito d'imposta di cui alla legge 193/2000 è elevato e esteso ai diciotto mesi successivi alla scarcerazione; le commesse pubbliche possono riservare quote a cooperative che impiegano detenuti.
>
> **Art. 5 (Recidiva e trasparenza).** L'ISTAT e il DAP pubblicano ogni anno, dal 2028, la recidiva a tre e a cinque anni per tipo di esecuzione della pena. Il Ministro riferisce ogni anno alle Camere.
>
> **Art. 6 (Copertura finanziaria).** Agli oneri, pari a [300 / 150 / 40] milioni per il 2027, [450 / 250 / 60] milioni per il 2028 e [450 / 250 / 60] milioni annui dal 2029, si provvede: a) quanto a [150 / 100 / 60] milioni con la riduzione delle autorizzazioni di spesa del DAP per servizi di custodia; b) per la parte restante con le maggiori entrate derivanti dalla riforma dei sussidi ambientalmente dannosi disposta dalla legge di bilancio. Gli interventi edilizi del 2027-29 sono finanziati, nelle regioni ammissibili, con i programmi della politica di coesione 2021-27. I risparmi accertati da minori presenze sono certificati dal MEF-RGS e riducono gli oneri di cui alla lettera b).

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | Ddl delega; bando UEPE; gara per i braccialetti elettronici; censimento dei posti inagibili e degli immobili disponibili | Giustizia (DAP, DGEPE), ANBSC, Agenzia del Demanio |
| 12 mesi | Decreto legislativo approvato; UEPE rafforzati; prime case di reinserimento; avvio della rilevazione sulla recidiva | Governo, Parlamento (pareri), magistratura di sorveglianza, ISTAT |
| Fine legislatura | Regime pieno; posti inagibili recuperati; prima statistica sulla recidiva; revisione a 36 mesi | DAP, ISTAT, Garante nazionale dei detenuti |

**Indicatori**

| KPI | Base | Obiettivo 3 anni (2029) | Obiettivo 5 anni (2031) |
|---|---|---|---|
| Affollamento sui posti regolamentari | 128,8%, 30/9/2026 (DAP) | ≤ 115% | ≤ 105% |
| Detenuti presenti | 66.063, 30/9/2026 (DAP) | ≤ 60.000 | ≤ 56.000 |
| Recidiva a 3 anni, misure alternative vs carcere | assente; prima rilevazione ISTAT-DAP 2028 | base pubblicata | −10% rispetto alla base |

**Rischi e mitigazione.** Reato grave commesso da un beneficiario, con forte eco mediatica: esclusione dei reati 4-bis, valutazione del rischio strutturata, relazione annuale trasparente. Carenza di UEPE: le assunzioni precedono l'allargamento dell'accesso. Opposizione locale alle case di reinserimento: piccole strutture, accordi con i Comuni. Risparmi inferiori al previsto: non sono usati come copertura.

---

## 07-C3 — Governance dei flussi migratori fondata sui dati

**Problema in un dato.** Nel 2025 l'Italia ha eseguito **4.780 rimpatri** a fronte di **21.295 ordini di allontanamento**: circa il **22%**, contro il 32% della media UE (Eurostat migr_eirtn, migr_eiord; `07_rimpatri_eurostat.csv`, `07_ordini_allontanamento_eurostat.csv`). Prime domande d'asilo: 128.655 nel 2025. Sbarchi: 22.786 a settembre 2026, −55% sul 2025 (Viminale).

**Soluzione.** È una cornice comune, compatibile sia con una linea di contenimento sia con una linea di canali regolari e integrazione. L'intensità delle quote resta una scelta politica. La cornice prevede quote motivate da un Osservatorio indipendente sul fabbisogno, decisione sull'asilo entro 6 mesi con le garanzie del Patto UE, priorità ai rimpatri volontari assistiti e un'integrazione misurabile (lingua, SAI, tutori dei minori).

| Variante | Contenuto | Costo a regime | Intensità | Copertura |
|---|---|---|---|---|
| PIENA | Osservatorio + asilo in 6 mesi + italiano entro 3 mesi + SAI + rimpatri volontari + tutori MSNA | 0,55 (dal 2029) | 1 | RIALLOCAZIONE 0,20 (da CAS a SAI); SAD 0,35; AMIF 0,05-0,10/anno solo 2027-29 |
| ESSENZIALE | Osservatorio + asilo in 6 mesi + rimpatri volontari + tutori; italiano solo per protetti e lavoratori | 0,25 | 0,55 | RIALLOCAZIONE 0,10; SAD 0,15 |
| PILOTA | Osservatorio e dati + asilo in 6 mesi in 3 Commissioni | 0,04 | 0,15 | RIALLOCAZIONE 0,04 |

**Articolato normativo essenziale** (disegno di legge)

> **Art. 1 (Finalità).** Nel rispetto degli articoli 10 e 117 della Costituzione, della Convenzione di Ginevra e del diritto dell'Unione, la presente legge fonda la programmazione dei flussi d'ingresso, le procedure di protezione internazionale e i rimpatri su dati pubblici e verificabili.
>
> **Art. 2 (Osservatorio sul fabbisogno).** 1. È istituito presso il CNEL l'Osservatorio indipendente sui flussi e sul fabbisogno di lavoro, composto da ISTAT, INPS, Banca d'Italia, Ministero del lavoro e Conferenza delle Regioni. 2. Entro il 30 giugno di ogni anno l'Osservatorio pubblica il fabbisogno per settore e territorio e il tasso di conversione dei nulla osta in contratti. 3. Il decreto di programmazione dei flussi motiva gli scostamenti dalle stime dell'Osservatorio.
>
> **Art. 3 (Durata delle procedure).** 1. La decisione sulla domanda di protezione internazionale è adottata entro sei mesi dalla presentazione, salvi i termini più brevi delle procedure di frontiera previsti dal regolamento (UE) 2024/1348. 2. Le Commissioni territoriali e le sezioni specializzate sono integrate di [800 / 800 / 60] unità.
>
> **Art. 4 (Integrazione e rimpatri).** 1. Il corso di lingua italiana e di orientamento civico è garantito entro tre mesi dall'ingresso [a tutti / ai titolari di protezione e ai lavoratori con nulla osta]. 2. L'accoglienza dei richiedenti è prioritariamente diffusa nel sistema SAI, con trasferimenti ai Comuni aderenti. 3. Il Ministero dell'interno promuove i rimpatri volontari assistiti e stipula accordi di riammissione collegati a canali di ingresso regolari. 4. Il Garante nazionale monitora i centri e riferisce ogni anno alle Camere. 5. Ai minori stranieri non accompagnati è assegnato un tutore entro trenta giorni.
>
> **Art. 5 (Copertura finanziaria).** Agli oneri, pari a [400 / 200 / 30] milioni per il 2027, [600 / 300 / 40] milioni per il 2028 e il 2029 e [550 / 250 / 40] milioni annui dal 2030, si provvede: a) quanto a [100 milioni per il 2027 e il 2028 e 50 milioni per il 2029 / 50 milioni annui per il 2027-2029 / 0], con le risorse del Fondo Asilo, migrazione e integrazione 2021-27; b) quanto a [200 / 100 / 40] milioni con la riduzione degli stanziamenti per le convenzioni dei centri di accoglienza straordinaria; c) per la parte restante con le maggiori entrate derivanti dalla riforma dei sussidi ambientalmente dannosi.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | Ddl; costituzione dell'Osservatorio; pubblicazione dei dati sui nulla osta 2023-26; piano di assunzioni per le Commissioni | Interno (Dip. Libertà civili), Lavoro, CNEL, ISTAT |
| 12 mesi | Primo rapporto sul fabbisogno; durata media dell'asilo pubblicata ogni trimestre; bando per i corsi di lingua; accordi con 2-3 paesi d'origine | Interno, Esteri, Regioni, ANCI |
| Fine legislatura | Asilo in 6 mesi a regime; SAI prevalente sui CAS; valutazione indipendente | Interno, Garante, Corte dei conti |

**Indicatori**

| KPI | Base | Obiettivo 3 anni (2029) | Obiettivo 5 anni (2031) |
|---|---|---|---|
| Rimpatri eseguiti / ordini di allontanamento | 22% (4.780/21.295), 2025, Eurostat | ≥ 30% | ≥ 35% |
| Durata media della procedura d'asilo in prima istanza | non pubblicata; da rilevare nel 2027 | ≤ 9 mesi | ≤ 6 mesi |
| Conversione dei nulla osta in contratti | non pubblicata; da rilevare nel 2027 | ≥ 60% | ≥ 75% |

**Rischi e mitigazione.** Polarizzazione politica: dati pubblici e Osservatorio indipendente, scelte d'intensità lasciate al decisore. Shock esterni (Nord Africa, Sahel): riserva di capacità e solidarietà UE prevista dal Patto. Dipendenza dagli accordi con paesi terzi: rimpatri volontari, meno conflittuali. Abuso dei canali di lavoro: verifica ispettiva dell'assunzione effettiva.

---

## 07-C4 — Dal bene confiscato al bene comune

**Problema in un dato.** Al 31/12/2025 **19.414 immobili** confiscati (41% del totale) erano ancora in gestione ANBSC, e gli enti hanno preso in carico solo il **44,8%** dei beni loro proposti, contro il 67,2% del 2023 (ANBSC, *Relazione performance 2025*; `07_anbsc_beni_confiscati.csv`). Le cause principali sono gli abusi edilizi e la mancanza di fondi per ristrutturare.

**Soluzione.** Rafforzare l'ANBSC sul territorio. Creare un fondo rotativo per ristrutturare gli immobili e garantire la continuità delle aziende confiscate. Introdurre i tutor d'impresa e pubblicare in open data lo stato di ogni bene. La vendita resta l'ultima istanza, con controlli antiriciclaggio.

| Variante | Contenuto | Costo a regime | Intensità | Copertura |
|---|---|---|---|---|
| PIENA | ANBSC +200 unità + fondo rotativo con quota a fondo perduto + tutor + open data | 0,15 (dal 2030) | 1 | RIALLOCAZIONE 0,05 (FUG); SAD 0,10; coesione 0,07-0,10/anno 2027-29 |
| ESSENZIALE | ANBSC + open data + fondo rotativo solo prestiti | 0,07 | 0,6 | RIALLOCAZIONE 0,04; SAD 0,03; coesione 0,05/anno |
| PILOTA | Fondo e tutor in Sicilia e Campania, solo con fondi di coesione | 0,02 | 0,2 | RIALLOCAZIONE 0,02; coesione 0,03/anno |

**Articolato normativo essenziale** (disegno di legge di modifica del d.lgs. 159/2011)

> **Art. 1 (Finalità).** La presente legge accelera la destinazione e il riuso sociale e produttivo dei beni confiscati alla criminalità organizzata, in coerenza con la direttiva (UE) 2024/1260.
>
> **Art. 2 (Rafforzamento dell'ANBSC).** La dotazione organica dell'Agenzia è incrementata di [200 / 200 / 0] unità; sono istituite sedi territoriali presso le Prefetture dei capoluoghi di distretto.
>
> **Art. 3 (Fondo rotativo).** 1. È istituito presso l'ANBSC un fondo rotativo per prestiti a tasso agevolato e garanzie a favore di enti territoriali, enti del terzo settore e aziende confiscate, alimentato da una quota delle disponibilità del Fondo unico giustizia. 2. Per gli immobili assegnati a Comuni con meno di 15.000 abitanti, il fondo può concedere contributi a fondo perduto fino al 50% del costo di ristrutturazione e di sanatoria. 3. I rimborsi ricostituiscono il fondo.
>
> **Art. 4 (Aziende e trasparenza).** 1. È istituito l'albo dei tutor d'impresa per le aziende sequestrate e confiscate. 2. L'ANBSC pubblica in formato aperto e georeferenziato lo stato di ogni bene, con i tempi di ciascuna fase. 3. Il bene non destinato entro tre anni dalla confisca definitiva è proposto in via prioritaria per le finalità di cui all'articolo 3 della legge di attuazione della proposta 07-C2 (case di reinserimento) e per l'edilizia sociale.
>
> **Art. 5 (Copertura finanziaria).** Agli oneri, pari a [150 / 70 / 20] milioni annui dal 2030, si provvede: a) quanto a [50 / 40 / 20] milioni con la quota del Fondo unico giustizia attribuita al Ministero dell'interno; b) per la parte restante con le maggiori entrate derivanti dalla riforma dei sussidi ambientalmente dannosi. Gli interventi di ristrutturazione del 2027-29 sono finanziati, nelle regioni ammissibili, dal PN Sicurezza per la legalità e dai programmi regionali FESR 2021-27.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | Ddl; accordo con le Autorità di gestione della coesione; bando di assunzione ANBSC; specifiche della piattaforma open data | Interno, ANBSC, Dip. Coesione, Giustizia (FUG) |
| 12 mesi | Fondo operativo; primi 500 immobili finanziati; piattaforma online; albo dei tutor | ANBSC, Prefetture, ANCI, Libera e terzo settore |
| Fine legislatura | Stock in gestione ridotto; valutazione a 3 anni della sopravvivenza delle aziende | ANBSC, Corte dei conti |

**Indicatori**

| KPI | Base | Obiettivo 3 anni (2029) | Obiettivo 5 anni (2031) |
|---|---|---|---|
| Immobili ancora in gestione ANBSC | 19.414, 31/12/2025 (ANBSC) | ≤ 15.000 | ≤ 11.000 |
| Beni opzionati / beni proposti agli enti | 44,8%, 2025 (ANBSC) | ≥ 60% | ≥ 70% |
| Immobili destinati nell'anno | 3.639, 2025 (ANBSC) | ≥ 4.500 | ≥ 5.000 |

**Rischi e mitigazione.** Intimidazioni contro gli assegnatari: protezione e rete con le Prefetture. Piccoli Comuni senza capacità tecnica: assegnazione a reti intercomunali, accompagnamento tecnico (sinergia con 09-C3). Riacquisto tramite prestanome in caso di vendita: vendita solo come ultima istanza, con verifiche antimafia rafforzate. Mancati rimborsi del fondo: rating dei progetti e garanzie parziali.

---

## 07-C5 — Difesa: spendere meglio prima di spendere di più ⚠️

**Problema in un dato.** La spesa per la difesa "core" in senso NATO era l'**1,52% del PIL nel 2024**, il **2,09% (47,2 mld) nel 2025** e il **2,10% (48,3 mld) nel 2026**. L'impegno dell'Aia prevede il **3,5% entro il 2035**, più l'1,5% per sicurezza e resilienza (NATO, *Defence Investment of NATO Countries 2014-2026*, luglio 2026; `07_nato_spesa_difesa_italia.csv`). Il debito è al 136,7% del PIL (2025) e il margine di bilancio del programma è nullo (`dati/verifiche/00_vincolo_bilancio.md`).

**Soluzione.** Una legge di programmazione decennale approvata dal Parlamento fissa la traiettoria, e ogni aumento deve avere una copertura vera. La spesa nuova va prioritariamente in acquisti comuni europei, difesa aerea, munizioni e cyber. Una relazione annuale pubblica, verificata dalla Corte dei conti, rende conto di costi e capacità. **In tutte e tre le varianti non c'è deficit**: si risponde così alla linea rossa sull'articolo 81 segnalata dal panel.

**La scelta è politica, non tecnica: più sicurezza oggi oppure più spazio per le altre politiche e meno debito domani.** L'agente presenta le tre opzioni senza raccomandarne una.

| Variante | Traiettoria | Costo aggiuntivo vs 2,1% | Intensità | Copertura (senza deficit) | Cosa comporta |
|---|---|---|---|---|---|
| **PIENA** | Lineare fino al 3,5% nel 2035 (+0,16 pp/anno) | 3,5 (2027), 7,0 (2028), 10,6 (2029), **32,0 nel 2035**; circa 160 cumulati | 1 | SAD 8,0 · SPESE_FISCALI 11,0 · RIALLOCAZIONE 9,0 · RIORDINO_BONUS 1,5 · ACCISE_SALUTE 1,5 · PENSIONI 1,0 | **Le coperture non bastano**: 32 mld superano la capienza massima permanente di tutti i fondi (circa 18) e assorbirebbero l'intero programma. Richiede tagli rilevanti ad altre spese o nuove imposte, oppure il deficit, che il programma esclude |
| **ESSENZIALE** | Legata al debito: +0,1 pp ogni 2 anni dal 2028 (2,5% nel 2034), solo se il debito/PIL scende secondo il percorso UE e la quota di acquisti comuni UE sale (≥25% nel 2028, ≥40% dal 2032) | 0 (2027), 2,3 (2028-29), 4,6 (2030-31), **9,1 nel 2034** | 0,35 | SAD 3,5 · SPESE_FISCALI 2,5 · RIALLOCAZIONE 1,5 (razionalizzazione interna Difesa) · RIORDINO_BONUS 0,8 · ACCISE_SALUTE 0,8 | Sostenibile fino al 2029; a regime supera la capienza prudente (3,7 mld) e compete con le altre proposte. Non raggiunge l'obiettivo dell'Aia |
| **ZERO** | Stabilizzazione al ~2,1% con efficienza: acquisti comuni, revisione dei programmi duplicati, nuove capacità solo da risparmi interni | **0** | 0,1 | nessuna | Rispetto al programmatico del Governo (NEC per la difesa nel 2027-28, in deficit) riduce il deficit ma non libera spazio sul tetto. Dal 2029 evita circa 7,6 mld/anno da assorbire. Non rispetta l'impegno NATO: costo di credibilità verso gli alleati |

Note: importi a PIL 2025 costante (2.265 mld); in termini nominali sono più alti. I prestiti SAFE (circa 8 mld) sono debito: non sono contati come copertura, ma possono finanziare gli acquisti comuni a tassi più bassi dei BTP se la spesa è già coperta. La clausola nazionale (NEC) resta giuridicamente disponibile al decisore: il programma GovernAI non la usa.

**Articolato normativo essenziale** (legge di programmazione pluriennale della difesa)

> **Art. 1 (Finalità).** In attuazione degli articoli 11, 52 e 81 della Costituzione, la presente legge definisce la traiettoria decennale della spesa per la difesa, ne subordina la crescita alla sostenibilità del debito e alla qualità della spesa e ne assicura il controllo parlamentare.
>
> **Art. 2 (Traiettoria).** 1. La spesa per la difesa, nella definizione NATO, è fissata per il periodo 2027-2036 secondo la traiettoria [lineare fino al 3,5% del PIL nel 2035 / incremento di 0,1 punti di PIL ogni due anni a decorrere dal 2028 / pari al 2,1% del PIL]. 2. [Solo ESSENZIALE] Ogni incremento è sospeso se nel biennio precedente il rapporto debito/PIL si è discostato dal percorso concordato in sede europea o se la quota di investimenti in acquisti congiunti europei è inferiore al 25% nel 2028 e al 40% dal 2032.
>
> **Art. 3 (Qualità della spesa).** 1. Gli investimenti sono destinati in via prioritaria a programmi congiunti con altri Stati membri dell'Unione (SAFE, EDIP), difesa aerea, munizioni, mobilità militare, spazio e cyber. 2. I nuovi programmi nazionali che duplicano capacità disponibili in programmi europei richiedono un parere motivato delle Commissioni parlamentari competenti.
>
> **Art. 4 (Efficienza).** Il Ministero della difesa adotta un piano triennale di razionalizzazione delle infrastrutture e dei programmi, con obiettivi di risparmio vincolati al finanziamento di nuove capacità. I risparmi sono certificati dal MEF-RGS.
>
> **Art. 5 (Trasparenza).** Il Governo presenta ogni anno alle Camere una relazione su costo per capacità, ritardi, quota europea e ricadute industriali, verificata dalla Corte dei conti. Ogni due anni le Camere possono rallentare la traiettoria con una risoluzione.
>
> **Art. 6 (Copertura finanziaria).** Gli incrementi di cui all'articolo 2 sono coperti ai sensi dell'articolo 17 della legge 196/2009, esclusivamente con riduzioni di spesa o maggiori entrate disposte in legge di bilancio. È esclusa la copertura mediante maggior indebitamento, compreso il ricorso alla clausola nazionale di salvaguardia. Se la copertura non è disposta, l'incremento dell'anno è sospeso.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | Decisione politica sulla variante (dibattito e voto in Parlamento); ddl di programmazione; mappatura dei programmi duplicati e delle infrastrutture dismissibili | Consiglio dei ministri, Difesa, MEF, Commissioni Difesa e Bilancio |
| 12 mesi | Legge approvata; piano di razionalizzazione; prima relazione annuale; adesione ai programmi SAFE/EDIP | Difesa (Segretariato generale, DNA), MEF, Corte dei conti |
| Fine legislatura | Prima revisione biennale; verifica della quota europea e del debito; eventuale rallentamento o accelerazione | Parlamento, Governo, Corte dei conti, UPB |

**Indicatori**

| KPI | Base | Obiettivo 3 anni (2029) | Obiettivo 5 anni (2031) |
|---|---|---|---|
| Spesa difesa core, % del PIL | 2,10%, 2026 (NATO) | PIENA 2,57% · ESSENZIALE 2,2% · ZERO 2,1% | PIENA 2,88% · ESSENZIALE 2,3% · ZERO 2,1% |
| Quota degli investimenti in acquisti congiunti UE | non pubblicata; prima relazione 2027 | ≥ 25% | ≥ 40% |
| Debito/PIL rispetto al percorso UE | 136,7%, 2025 (Eurostat); 136,6% programmatico 2029 (DPB 2027) | ≤ percorso programmatico | in calo |

**Rischi e mitigazione.** PIENA: spiazzamento di sanità, scuola e clima e rischio art. 81, cioè il ⚠️ breve +1 / lungo −1 del panel; mitigazione: freno automatico, sospensione senza copertura. ESSENZIALE: credibilità parziale verso gli alleati; mitigazione: quota europea alta e contributo cyber e resilienza (07-C6) nell'1,5%. ZERO: costo diplomatico e di deterrenza, possibili pressioni NATO e USA; mitigazione: efficienza documentata e leadership nei programmi comuni. Per tutte: spesa "di bandiera" inefficiente (verifica della Corte dei conti) e dipendenza da fornitori extra-UE (preferenza europea).

---

## 07-C6 — Scudo cyber territoriale

**Problema in un dato.** Nel 2025 CSIRT Italia ha gestito **2.729 eventi cyber** (1.979 nel 2024) e **615 incidenti con impatto** (573), di cui 103 ransomware, il tipo più dannoso (ACN, *Relazione annuale al Parlamento 2025*; verifica n. 36). Comuni piccoli e aziende sanitarie hanno risorse e competenze limitate (valutazione qualitativa, dato non verificato).

**Soluzione.** Creare centri di sicurezza condivisi (SOC) regionali con ACN, che offrono monitoraggio, backup sicuri e risposta agli incidenti ai Comuni sotto i 50.000 abitanti e alle aziende sanitarie. Istituire una riserva cyber civile-militare. Garantire formazione di base a tutti i dipendenti pubblici e requisiti minimi nei capitolati. La spesa è contabilizzabile nell'1,5% NATO di resilienza.

| Variante | Contenuto | Costo a regime | Intensità | Copertura |
|---|---|---|---|---|
| PIENA | SOC per Comuni sotto 50k e tutta la sanità + riserva cyber + formazione + esercitazioni | 0,35 (dal 2030) | 1 | RIALLOCAZIONE 0,10; SPESE_FISCALI 0,25; coesione 0,15/anno 2027-29 per l'infrastruttura |
| ESSENZIALE | SOC in 10 macro-aree per sanità e Comuni tra 5k e 50k; formazione | 0,18 | 0,6 | RIALLOCAZIONE 0,06; SPESE_FISCALI 0,12; coesione 0,08/anno |
| PILOTA | SOC in 3 Regioni, valutazione a 36 mesi | 0,03 | 0,2 | RIALLOCAZIONE 0,03; coesione 0,04/anno |

**Articolato normativo essenziale** (legge di bilancio + accordo Stato-Regioni)

> **Art. 1 (Finalità).** Al fine di garantire la continuità dei servizi pubblici essenziali e in attuazione del d.lgs. 138/2024 (NIS2), è istituita la rete nazionale dei centri territoriali di sicurezza informatica.
>
> **Art. 2 (SOC territoriali).** 1. L'ACN, d'intesa con la Conferenza Stato-Regioni, istituisce [un SOC per Regione / dieci SOC di macro-area / tre SOC sperimentali] che forniscono monitoraggio, backup protetti e risposta agli incidenti ai Comuni con popolazione inferiore a 50.000 abitanti e agli enti del Servizio sanitario nazionale. 2. L'adesione è gratuita; gli enti aderenti adottano le misure minime definite dall'ACN.
>
> **Art. 3 (Riserva cyber).** È istituita presso l'ACN, in raccordo con il Ministero della difesa, una riserva di professionisti e studenti formati, attivabile in caso di crisi con decreto del Presidente del Consiglio dei ministri.
>
> **Art. 4 (Formazione e capitolati).** 1. Tutti i dipendenti pubblici svolgono entro ventiquattro mesi un modulo di formazione di base sulla sicurezza informatica. 2. I capitolati per software e servizi digitali pubblici includono i requisiti minimi di sicurezza definiti dall'ACN. 3. Ogni anno si tiene un'esercitazione congiunta Difesa, Interno e ACN.
>
> **Art. 5 (Copertura finanziaria).** Agli oneri di gestione, pari a [100 / 40 / 10] milioni per il 2027, [250 / 120 / 30] milioni per il 2028 e [350 / 180 / 30] milioni annui dal 2029, si provvede: a) quanto a [100 / 60 / 30] milioni con la riduzione delle autorizzazioni di spesa per la sicurezza informatica dei Ministeri dell'interno e della difesa e dell'ACN; b) per la parte restante con le maggiori entrate derivanti dal riordino delle spese fiscali. Gli investimenti infrastrutturali del 2027-29 sono finanziati con i programmi regionali FESR 2021-27 (obiettivo di policy 1).

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | Norma; accordo Stato-Regioni; riprogrammazione FESR; censimento degli enti e del loro livello di maturità | ACN, Conferenza Stato-Regioni, Dip. Coesione, ANCI |
| 12 mesi | Primi SOC operativi (sanità prima); avvio della formazione; costituzione della riserva | ACN, Regioni, aziende sanitarie, Difesa |
| Fine legislatura | Copertura di tutti gli enti target; prima esercitazione nazionale; valutazione a 3 anni | ACN, Corte dei conti |

**Indicatori**

| KPI | Base | Obiettivo 3 anni (2029) | Obiettivo 5 anni (2031) |
|---|---|---|---|
| Comuni sotto 50k e aziende sanitarie coperti da un SOC | 0%, 2026 (nessuna rete) | ≥ 60% | 100% |
| Incidenti con impatto in enti locali e sanità | sottoinsieme dei 615 del 2025 (ACN), da rilevare | −20% | −35% |
| Tempo medio di ripristino dopo un ransomware | da rilevare (ACN, 2027) | −30% | −50% |

**Rischi e mitigazione.** Carenza di specialisti: borse con vincolo di servizio e retribuzioni competitive. Sovrapposizioni Stato-Regioni: coordinamento ACN e standard unici. Dipendenza dai fondi di coesione per l'avvio: la gestione stabile è coperta da fondi nazionali dal 2027. Adesione solo formale degli enti: servizio gratuito e misure minime obbligatorie.
