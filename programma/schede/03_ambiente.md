# GovernAI — Schede pronte, area 03: Ambiente, Energia, Agricoltura, Protezione civile

*Agente ministeriale 03, 7 novembre 2026. Varianti e coperture in `programma/varianti/03_ambiente.csv`. Dati da `dati/serie/03_*.csv` e `dati/verifiche/03_ambiente.md`. Importi in mld €/anno a regime. Le stime senza fonte ufficiale sono indicate come "stima GovernAI".*

**Regole di copertura applicate.** Nessuna proposta usa più i proventi ETS1: sono già destinati per legge (d.lgs. 47/2020, art. 23) e il fondo è esaurito. Non si usano DEFICIT, RISPARMI_ATTESI, IVA_EVASIONE o ALTRO. Le fonti sono quattro:
- **SAD**: gettito della riforma dei sussidi dannosi, attivata dal menu coperture;
- **RIALLOCAZIONE**: tagli di spesa nei bilanci MASE, MASAF e Protezione civile;
- **COESIONE_2127**: solo per opere una tantum 2027-29;
- **TARIFFE**: fuori bilancio, con l'effetto distributivo dichiarato.

## Il nodo politico dell'area: a che cosa serve il gettito dei SAD

La riforma dei sussidi ambientalmente dannosi è nel menu coperture. Il suo gettito ha tre usi possibili, e **tutti e tre sono legittimi**:

| Variante 03-P1 | Restituzione | Costo (fondo SAD) | Intensità | Cosa resta del gettito SAD (se il menu attiva circa 5-6 mld) | Chi ne beneficia |
|---|---|---|---|---|---|
| **PIENA** | Tutto il gettito: bollette più leggere (2,5), bonus clima (1,5), conversione flotte (1,0) | 5,0 (2031) | 1,0 | quasi nulla: 03-P4 e 03-P5 vanno coperti con altre fonti, e le altre aree non usano il SAD | Tutti i consumatori elettrici; massima visibilità e consenso |
| **ESSENZIALE** | Solo compensazione: bonus clima per ISEE ≤ 15.000 € e aree interne (0,8), compensazione settoriale decrescente (0,4) | 1,2 (2030) | 0,5 | circa 3,5-4 mld per prevenzione (03-P4), agricoltura (03-P5) e servizi di altre aree | Primi due decili e settori esposti; il resto va a servizi pubblici |
| **ZERO** | Nessuna restituzione; resta la governance (calendario, clausola di sospensione, valutazione UPB) | 0 | 0,2 | tutto | Chi riceve i servizi finanziati; rischio di regressività e di rivolta di categoria |

**Raccomandazione dell'agente (non vincolante): ESSENZIALE.** È la sola variante che rispetta insieme due condizioni della Carta:
- **RIS e BEN**: nessun peggioramento per i redditi bassi;
- **FUT**: il gettito serve anche all'adattamento.

La PIENA ha più consenso e spinge l'elettrificazione, ma assorbe tutto il gettito per restituirlo a tutti, anche a chi non ne ha bisogno. La ZERO massimizza le risorse per i servizi, ma ripete l'errore della Francia nel 2018: un aumento dei prezzi senza una restituzione visibile.

---

## 03-P1 — Dividendo climatico

**Problema in un dato.** Nel 2025 lo Stato ha speso **22,38 mld €** in sussidi ambientalmente dannosi, di cui **20,63 mld** alle fonti fossili. Fonte: MASE, Catalogo SAD/SAF VIII ed., 2026, serie `03_sad_catalogo_mase`. Intanto le emissioni dei trasporti, **113,3 Mt CO₂eq nel 2024**, sono sopra il livello del 1990 (102,2 Mt): Eurostat env_air_gge, serie `03_ghg_settori`.

**Soluzione.** Una legge delega fissa un calendario quinquennale e pubblico di riforma dei SAD riformabili a livello nazionale: in tutto 17,1 mld, di cui una parte da scegliere nel menu coperture. Una parte del maggior gettito *accertato* torna ai cittadini attraverso un Fondo per il dividendo climatico. L'importo e i canali della restituzione dipendono dalla variante. I pagamenti partono solo dopo l'incasso, quindi la misura non crea deficit.

**Varianti.** PIENA 5,0 mld (int. 1,0) · ESSENZIALE 1,2 mld (int. 0,5) · ZERO 0 (int. 0,2). Vedi la tabella sopra. Le coperture sono tutte sul fondo SAD.

### Articolato normativo essenziale (DDL "Transizione fiscale verde e dividendo climatico")

**Art. 1 (Finalità).** 1. La presente legge riduce progressivamente i sussidi ambientalmente dannosi censiti nel Catalogo di cui all'articolo 68 della legge 28 dicembre 2015, n. 221. Lo fa in coerenza con gli obiettivi del Regolamento (UE) 2018/842 e con il Piano sociale per il clima, garantendo che la transizione non peggiori la condizione delle famiglie a basso reddito.

**Art. 2 (Delega al Governo).** 1. Il Governo è delegato ad adottare, entro dodici mesi dall'entrata in vigore della presente legge, uno o più decreti legislativi per la riforma dei sussidi ambientalmente dannosi riformabili a livello nazionale, secondo i seguenti principi e criteri direttivi:
- a) calendario quinquennale pubblicato con almeno dodici mesi di anticipo su ogni scaglione;
- b) priorità alle misure con minore impatto sociale e maggiore effetto ambientale;
- c) compensazioni settoriali solo temporanee, decrescenti e legate a investimenti di conversione;
- d) esclusione delle misure già riformate dalla legge 30 dicembre 2025, n. 199.

**Art. 3 (Fondo per il dividendo climatico).** 1. Nello stato di previsione del Ministero dell'economia e delle finanze è istituito il Fondo per il dividendo climatico. Il Fondo è alimentato, nei limiti del maggior gettito accertato derivante dai decreti di cui all'articolo 2, in misura pari a:
- [PIENA] il 100 per cento di tale gettito;
- [ESSENZIALE] 1,2 miliardi di euro annui a regime.

2. Il Fondo finanzia:
- a) [PIENA] la riduzione degli oneri generali di sistema gravanti sulle bollette elettriche, che sono posti a carico della fiscalità generale;
- b) un bonus clima annuale per i nuclei con ISEE non superiore a 15.000 euro e per i residenti nei comuni delle aree interne privi di servizio di trasporto pubblico di linea;
- c) contributi temporanei e decrescenti alla conversione delle flotte dell'autotrasporto, della pesca e dell'agricoltura.

3. [ZERO] Il maggior gettito affluisce all'entrata del bilancio dello Stato. La relazione di cui all'articolo 5 ne indica la destinazione.

**Art. 4 (Clausola di salvaguardia).** 1. Se il prezzo medio mensile al consumo del gasolio supera per due mesi consecutivi la soglia fissata con decreto del Ministro dell'economia e delle finanze, sentita l'ARERA, l'applicazione dello scaglione successivo è sospesa fino al rientro sotto la soglia.

**Art. 5 (Valutazione e revisione).** 1. Entro il 30 giugno del terzo anno l'Ufficio parlamentare di bilancio trasmette alle Camere una valutazione degli effetti per decile di reddito equivalente e per territorio. 2. Gli scaglioni successivi si applicano solo se la valutazione non rileva un peggioramento del reddito disponibile reale dei primi due decili attribuibile alla riforma.

**Art. 6 (Copertura finanziaria).** 1. Agli oneri derivanti dall'articolo 3 si provvede esclusivamente nei limiti del maggior gettito accertato derivante dai decreti di cui all'articolo 2, ai sensi dell'articolo 17 della legge 31 dicembre 2009, n. 196. 2. I trasferimenti del Fondo sono erogati nell'anno successivo all'accertamento. Dall'attuazione della presente legge non derivano nuovi o maggiori oneri per la finanza pubblica.

### Cronoprogramma

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | DDL delega in Consiglio dei ministri; mandato a UPB e ISTAT per il modello di micro-simulazione per decile; scelta della variante dopo l'ottimizzazione | MEF, MASE, Agenzia Dogane, UPB |
| 12 mesi | Delega approvata; primo decreto legislativo con il calendario quinquennale; piattaforma del bonus clima su ISEE (INPS) | Governo, Parlamento, INPS |
| Fine legislatura | Tre scaglioni applicati (dal 2028, insieme a ETS2); valutazione UPB al 3° anno; dividendo a regime nel 2030-31 | MEF, MASE, ARERA, UPB |

### Indicatori

| KPI | Base | Obiettivo a 3 anni (2029) | Obiettivo a 5 anni (2031) |
|---|---|---|---|
| SAD alle fonti fossili | 20,63 mld € (2025, MASE Catalogo) | ≤ 18 mld | ≤ 15,5 mld |
| Emissioni dei trasporti | 113,3 Mt CO₂eq (2024, Eurostat env_air_gge) | ≤ 109 Mt | ≤ 103 Mt (sotto il 1990) |
| Reddito disponibile reale dei primi due decili, effetto della riforma | da costruire con la micro-simulazione UPB entro 100 giorni | variazione ≥ 0 | variazione ≥ 0 |

### Rischi e mitigazione

| Rischio | Mitigazione |
|---|---|
| Protesta di categoria (autotrasporto, pesca, agricoltura) | Calendario noto con 12 mesi di anticipo; compensazioni decrescenti legate a investimenti |
| Dividendo percepito come invisibile | Voce "dividendo climatico" in bolletta o pagamento annuale esplicito |
| Gettito inferiore al previsto (i valori del Catalogo sono teorici) | Il dividendo si eroga solo sul gettito accertato (art. 6) |
| Shock esogeno sui prezzi | Clausola di sospensione (art. 4) |
| Doppio conteggio con ETS2 e Fondo sociale per il clima | Il FSC resta separato e il bonus clima si coordina con il Piano sociale per il clima |

---

## 03-P2 — Elettricità rinnovabile a prezzo rinnovabile

**Problema in un dato.** Il prezzo unico nazionale dell'elettricità è stato di **115,32 €/MWh nel 2025**, +6,3% sul 2024, perché lo fissa il gas (GME, serie `03_pun_gme`). Le rinnovabili coprono il **41,1% della domanda** e nel 2025 si sono installati **7,19 GW** nuovi, contro circa 9 GW/anno necessari (Terna, serie `03_terna_2025`).

**Soluzione.**
- Tutta la nuova capacità rinnovabile incentivata va in aste GSE con contratti per differenza (CfD) a due vie: gli extra-ricavi tornano in bolletta.
- Un pool rinnovabile rivende a prezzo di costo una quota di questa energia a famiglie vulnerabili, PMI e comunità energetiche.
- Le autorizzazioni si accelerano con aree idonee definitive, silenzio-assenso effettivo e una squadra tecnica statale.

Il costo per il bilancio riguarda solo la squadra tecnica. I CfD sono finanziati in bolletta.

**Varianti.**

| Variante | Costo | Intensità | Fondi |
|---|---|---|---|
| PIENA (squadra di circa 150 tecnici, pool anche per le PMI) | 0,15 | 1,0 | RIALLOCAZIONE 0,10 + TARIFFE 0,05 (corrispettivi GSE) |
| ESSENZIALE (squadra di circa 60 tecnici, pool solo per famiglie vulnerabili) | 0,07 | 0,7 | RIALLOCAZIONE 0,05 + TARIFFE 0,02 |
| ZERO (solo CfD e aree idonee) | 0 | 0,45 | — |

### Articolato normativo essenziale (decreto legislativo in attuazione del Reg. (UE) 2024/1747)

**Art. 1 (Finalità).** 1. Il presente decreto allinea il prezzo dell'energia elettrica da fonti rinnovabili ai suoi costi di produzione, ne stabilizza il prezzo per i clienti finali e accelera l'installazione della capacità necessaria agli obiettivi del PNIEC.

**Art. 2 (Contratti per differenza a due vie).** 1. A decorrere dal 1° gennaio 2028 il sostegno pubblico alla nuova capacità di produzione da fonti rinnovabili è riconosciuto esclusivamente mediante contratti per differenza a due vie, assegnati dal GSE con procedure competitive tecnologicamente neutrali. 2. Le somme dovute dai produttori quando il prezzo di mercato supera il prezzo di esercizio sono destinate dall'ARERA alla riduzione degli oneri generali di sistema.

**Art. 3 (Pool rinnovabile).** 1. Il GSE cede a prezzo pari al costo medio ponderato dei contratti di cui all'articolo 2 una quota dell'energia contrattualizzata, fissata annualmente dall'ARERA, ai clienti titolari del bonus sociale elettrico, alle comunità energetiche rinnovabili e [PIENA] alle piccole e medie imprese.

**Art. 4 (Aree idonee e procedure).** 1. Entro sei mesi le Regioni completano l'individuazione delle aree idonee d'intesa in Conferenza unificata; in mancanza provvede lo Stato in via sostitutiva. 2. Nelle aree idonee il silenzio dell'amministrazione competente, decorsi i termini, equivale ad assenso, anche per gli atti di assenso paesaggistico.

**Art. 5 (Squadra tecnica nazionale).** 1. Presso il MASE, avvalendosi del GSE, è costituita una squadra tecnica di [PIENA: 150; ESSENZIALE: 60] unità a supporto delle Soprintendenze e dei Comuni con meno di 15.000 abitanti per l'istruttoria dei procedimenti autorizzativi.

**Art. 6 (Copertura finanziaria).** 1. Agli oneri dell'articolo 5, pari a [PIENA: 0,15; ESSENZIALE: 0,07] miliardi di euro annui dal 2028, si provvede:
- a) per [0,10; 0,05] miliardi mediante corrispondente riduzione degli stanziamenti del MASE per assistenza tecnica esterna;
- b) per la quota restante a valere sui corrispettivi riconosciuti al GSE ai sensi dell'articolo 25 del decreto-legge 24 giugno 2014, n. 91.

2. Gli articoli 2, 3 e 4 non comportano nuovi o maggiori oneri per la finanza pubblica.

### Cronoprogramma

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | Schema di decreto legislativo; consultazione ARERA sul pool; ricognizione delle istanze pendenti per regione | MASE, ARERA, GSE |
| 12 mesi | Decreto in vigore; aree idonee definitive (o potere sostitutivo); squadra tecnica operativa; regole delle aste CfD | MASE, Regioni, Conferenza unificata, GSE |
| Fine legislatura | Prime aste CfD entro 18 mesi; ≥ 9 GW/anno installati; aste MACSE a regime | GSE, Terna, ARERA |

### Indicatori

| KPI | Base | 3 anni (2029) | 5 anni (2031) |
|---|---|---|---|
| Quota rinnovabili sulla domanda elettrica | 41,1% (2025, Terna) | ≥ 52% | ≥ 62% (traiettoria PNIEC al 2030, da verificare sul testo) |
| Nuova capacità rinnovabile installata | 7,19 GW (2025, Terna) | ≥ 9 GW/anno | ≥ 10 GW/anno |
| Tempo medio di autorizzazione degli impianti in area idonea | da rilevare entro 100 giorni (GSE/MASE) | −40% | −60% |

### Rischi e mitigazione

| Rischio | Mitigazione |
|---|---|
| Conflitti paesaggistici locali | Priorità alle superfici già compromesse; dibattito pubblico per i grandi impianti; compensazioni trasparenti ai comuni ospitanti |
| Saturazione della rete al Sud | Aste coordinate con il piano di sviluppo Terna |
| Prezzi di esercizio troppo alti | Aste competitive e neutrali rispetto alla tecnologia |
| Spesa GSE riclassificata nel conto della PA | Quota TARIFFE piccola (0,05); in alternativa tutto su riallocazione |

---

## 03-P3 — Ogni goccia conta: reti idriche e riuso *(dipende dai valori; nel nucleo robusto con la Carta 1)*

**Problema in un dato.** Nel 2022 si è perso il **42,4% dell'acqua immessa nelle reti comunali**, cioè **3,39 mld m³** (era il 42,2% nel 2020). Basilicata è al 65,5%, Abruzzo al 62,5%, Molise al 53,9%, Sardegna al 52,8%, Sicilia al 51,6% e Campania al 49,9%. Fonte: ISTAT, Censimento delle acque per uso civile, serie `03_acqua_perdite`.

**Soluzione.**
- Obiettivi di riduzione delle perdite vincolanti per ogni ambito, con premi e penalità tariffarie dell'ARERA.
- Aggregazione obbligatoria delle gestioni comunali in economia entro 24 mesi, con gestione pubblica o mista.
- Contributi FESR e fondo di garanzia CDP-BEI per le reti del Mezzogiorno.
- Riuso irriguo obbligatorio nei distretti a stress idrico.
- Bonus idrico sociale potenziato.

Gli investimenti, circa 3-5 mld/anno, poggiano in larga parte su tariffa e prestiti. Il contributo pubblico è una tantum.

**Varianti.**

| Variante | Costo | Intensità | Fondi |
|---|---|---|---|
| PIENA | 1,15 | 1,0 | COESIONE_2127 0,80 (una tantum) + RIALLOCAZIONE 0,05 + TARIFFE 0,30 (bonus idrico e premi) |
| ESSENZIALE (regole intere, investimenti solo per le regioni oltre il 50% di perdite) | 0,60 | 0,6 | COESIONE_2127 0,40 + RIALLOCAZIONE 0,03 + TARIFFE 0,17 |
| PILOTA (3 ambiti: Basilicata, Abruzzo, Sicilia) | 0,12 | 0,15 | COESIONE_2127 0,10 + RIALLOCAZIONE 0,02 |

Nello scenario prudente la parte a carico del bilancio permanente è minima (0,03-0,05 mld). Il resto è coesione una tantum, esclusa dalla spesa netta, oppure tariffa.

### Articolato normativo essenziale (decreto legislativo "Servizio idrico efficiente e riuso")

**Art. 1 (Finalità).** 1. Il presente decreto dimezza in dieci anni le perdite delle reti di distribuzione idrica, completa l'organizzazione industriale del servizio idrico integrato e promuove il riuso delle acque reflue depurate, nel rispetto dell'esito referendario del 2011 sulla remunerazione del capitale.

**Art. 2 (Obiettivi vincolanti di riduzione delle perdite).** 1. L'ARERA fissa per ciascun ambito territoriale ottimale obiettivi annuali di riduzione delle perdite idriche lineari e percentuali, con l'obiettivo nazionale di riportarle sotto il 25 per cento entro il 2036. 2. Il mancato raggiungimento comporta penalità tariffarie a carico del gestore, non trasferibili agli utenti. Il superamento comporta premialità.

**Art. 3 (Aggregazione delle gestioni).** 1. Entro ventiquattro mesi le gestioni in economia non conformi all'articolo 149-bis del decreto legislativo 3 aprile 2006, n. 152, confluiscono nel gestore unico d'ambito. 2. In caso di inerzia il Presidente della Regione, e in via sostitutiva il Governo, nomina un commissario. 3. Resta salva la facoltà dell'ente d'ambito di affidare il servizio a società interamente pubblica.

**Art. 4 (Fondo di garanzia e contributi).** 1. È istituito presso Cassa depositi e prestiti un fondo rotativo di garanzia sui finanziamenti a lungo termine ai gestori, con la partecipazione della BEI. 2. Le amministrazioni titolari dei programmi regionali FESR 2021-2027 riprogrammano, d'intesa con il Dipartimento per le politiche di coesione, risorse non ancora selezionate per [PIENA: 0,8; ESSENZIALE: 0,4] miliardi di euro annui nel triennio 2027-2029. Le risorse sono destinate alla dotazione del fondo e a contributi per distrettualizzazione, sostituzione delle reti e misuratori nelle regioni con perdite superiori al [PIENA: 45; ESSENZIALE: 50] per cento.

**Art. 5 (Riuso e tutela sociale).** 1. Nei distretti idrografici con severità idrica media o alta, i gestori degli impianti di depurazione sopra [PIENA: 10.000; ESSENZIALE: 100.000] abitanti equivalenti predispongono il riuso irriguo ai sensi del Regolamento (UE) 2020/741. 2. L'ARERA adegua il bonus sociale idrico in modo che l'aumento tariffario derivante dal presente decreto non gravi sui nuclei beneficiari.

**Art. 6 (Copertura finanziaria).** 1. Agli oneri dell'articolo 4, comma 2, si provvede a valere sulle risorse dei programmi della politica di coesione 2021-2027 e sul relativo cofinanziamento nazionale. 2. Agli oneri di supporto tecnico, pari a [0,05; 0,03] miliardi annui, si provvede mediante riduzione degli stanziamenti del MASE. 3. Gli oneri dell'articolo 5, comma 2, e le premialità dell'articolo 2 sono coperti dalle componenti tariffarie perequative stabilite dall'ARERA.

### Cronoprogramma

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | Ricognizione delle gestioni in economia per ambito; accordo con le Regioni del Sud sulla riprogrammazione FESR; consultazione ARERA sugli obiettivi | MASE, ARERA, Dip. Coesione, Regioni |
| 12 mesi | Decreto in vigore; obiettivi per ambito nel metodo tariffario; fondo CDP-BEI operativo; primi bandi per la distrettualizzazione | ARERA, CDP, BEI, enti d'ambito |
| Fine legislatura | Aggregazioni completate (commissari dove serve); spesa FESR entro il 2029-30; riuso operativo nei distretti siccitosi | Gestori, Regioni, Autorità di bacino, Consorzi di bonifica |

### Indicatori

| KPI | Base | 3 anni | 5 anni |
|---|---|---|---|
| Perdite idriche totali in distribuzione | 42,4% (2022, ISTAT; misura annuale ARERA-RQTI M1) | ≤ 38% | ≤ 33% |
| Regioni con perdite oltre il 50% | 5: Basilicata, Abruzzo, Molise, Sardegna, Sicilia (2022, ISTAT) | ≤ 3 | 0 |
| Acqua reflua riutilizzata in agricoltura | da rilevare entro 100 giorni (ISPRA/ISTAT) | base × 2 | base × 4 |

### Rischi e mitigazione

| Rischio | Mitigazione |
|---|---|
| Accusa di "privatizzazione" | Facoltà di gestione interamente pubblica (art. 3, c. 3); dati pubblici per gestore |
| Conflitto con i Comuni | Commissari solo dopo 24 mesi; supporto tecnico gratuito |
| Aumento delle tariffe | Bonus idrico adeguato per legge (art. 5, c. 2); penalità non trasferibili agli utenti |
| Lentezza dei cantieri e scadenza FESR (n+3) | Progetti già in parco progetti PNRR non finanziati; centrale di committenza; rotazione verso il fondo di garanzia |
| Diffidenza sul riuso | Controlli ARPA e garanzie sanitarie del Reg. UE 2020/741 |

---

## 03-P4 — Prevenire costa meno *(nucleo robusto, prima proposta per utilità attesa)*

**Problema in un dato.** Il **94,5% dei comuni** (7.463) è in aree a rischio frane, alluvioni, erosione o valanghe. **1,28 milioni di persone** vivono nelle aree a pericolosità da frana elevata e molto elevata (ISPRA, Rapporto dissesto ed. 2024). A fine aprile 2026 solo il **16%** delle imprese aveva la polizza catastrofale obbligatoria (IVASS). Nel 2025 il consumo di suolo è stato di **+102 km²**, record del decennio (ISPRA-SNPA, 2026).

**Soluzione.**
- Un Fondo nazionale per la prevenzione con dotazione pluriennale certa, assegnato su graduatoria di rischio e non sulle emergenze, con progettazione centralizzata per i piccoli Comuni.
- Uno schema assicurativo misto per le abitazioni, con riassicurazione pubblica oltre soglia e premi calmierati per i redditi bassi.
- Norme a costo zero: divieto di edificare nelle aree P3/P4, nessun indennizzo agli edifici abusivi o condonati, consumo di suolo netto zero al 2040.

**Varianti.**

| Variante | Costo | Intensità | Fondi |
|---|---|---|---|
| PIENA (fondo 1,2 + progettazione + contributo ai premi) | 1,50 | 1,0 | SAD 0,50 + RIALLOCAZIONE 0,40 + COESIONE_2127 0,40 + TARIFFE 0,20 |
| ESSENZIALE (fondo 0,6 sui rischi più alti, schema assicurativo con opt-out) | 0,80 | 0,6 | SAD 0,25 + RIALLOCAZIONE 0,20 + COESIONE_2127 0,25 + TARIFFE 0,10 |
| PILOTA (norme intere + 2 bacini pilota) | 0,20 | 0,25 | COESIONE_2127 0,15 + RIALLOCAZIONE 0,05 |

Dal 2030 la quota di coesione va sostituita con il ciclo 2028-34 o con altro gettito SAD. Altrimenti il fondo della PIENA scende a 0,9 mld.

### Articolato normativo essenziale (legge quadro "Prevenzione dei rischi naturali e territorio sicuro")

**Art. 1 (Finalità).** 1. La presente legge sposta le risorse pubbliche dalla riparazione dei danni alla prevenzione dei rischi idrogeologici, idraulici e costieri. Riduce l'esposizione di persone e beni, arresta il consumo di suolo netto e ripartisce in modo equo il rischio catastrofale tra Stato, assicurazioni e cittadini.

**Art. 2 (Fondo nazionale per la prevenzione).** 1. Presso la Presidenza del Consiglio dei ministri, Dipartimento della protezione civile, è istituito il Fondo nazionale per la prevenzione dei rischi naturali, con una dotazione di [PIENA: 1.200; ESSENZIALE: 600] milioni di euro annui dal 2029. 2. Il Fondo è ripartito annualmente su graduatoria nazionale di rischio elaborata dall'ISPRA sulla base della piattaforma IdroGEO e dei piani di gestione del rischio di alluvione. Le richieste conseguenti a eventi emergenziali non costituiscono criterio di priorità. 3. Per i Comuni con meno di 15.000 abitanti la progettazione è svolta da una struttura tecnica nazionale o dalla Regione in qualità di stazione appaltante.

**Art. 3 (Schema assicurativo per le abitazioni).** 1. Le polizze contro l'incendio dei fabbricati a uso abitativo includono, salvo rinuncia espressa [ESSENZIALE] o obbligatoriamente [PIENA], la copertura dei danni da alluvione, frana, inondazione e sisma, con premio determinato secondo criteri fissati con regolamento IVASS. 2. Sui premi di tali polizze si applica una maggiorazione mutualistica uniforme che finanzia la riduzione dei premi per i nuclei con ISEE non superiore a 15.000 euro. 3. La CONSAP riassicura i rischi eccedenti una soglia annua di sinistri, con garanzia dello Stato. La garanzia è iscritta nell'allegato al bilancio relativo alle garanzie prestate.

**Art. 4 (Territorio sicuro).** 1. Nelle aree classificate a pericolosità elevata e molto elevata dai piani di assetto idrogeologico e dai piani di gestione del rischio di alluvione è vietata la realizzazione di nuove costruzioni. 2. Gli immobili realizzati abusivamente, o oggetto di condono, in tali aree non accedono a contributi o indennizzi pubblici per danni da calamità naturali. 3. Lo Stato promuove programmi volontari di delocalizzazione con indennizzo. 4. Il consumo di suolo netto è azzerato entro il 2040, con obbligo di compensazione mediante de-impermeabilizzazione.

**Art. 5 (Valutazione).** 1. Ogni cinque anni la Corte dei conti riferisce alle Camere sul rapporto tra spesa per la prevenzione e spesa per le emergenze, sui tempi di spesa del Fondo e sulle passività potenziali dello schema di riassicurazione.

**Art. 6 (Copertura finanziaria).** 1. Agli oneri dell'articolo 2, pari a [PIENA: 1.300; ESSENZIALE: 700] milioni di euro annui comprensivi della struttura di progettazione, si provvede:
- a) per [500; 250] milioni mediante quota del maggior gettito derivante dalla riforma dei sussidi ambientalmente dannosi;
- b) per [400; 200] milioni mediante corrispondente riduzione delle autorizzazioni di spesa per interventi emergenziali e ristori, sulla base della media certificata dalla Ragioneria generale dello Stato nell'ultimo quinquennio;
- c) per [400; 250] milioni, nel triennio 2027-2029, a valere sui programmi FESR 2021-2027, obiettivo di policy 2.

2. Gli oneri dell'articolo 3, comma 2, sono a carico della maggiorazione mutualistica e non gravano sulla finanza pubblica.

### Cronoprogramma

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | DDL legge quadro; graduatoria di rischio ISPRA aggiornata; censimento della spesa emergenziale dell'ultimo quinquennio (RGS); tavolo IVASS-ANIA-CONSAP sullo schema | Protezione civile, MASE, MEF, ISPRA, IVASS |
| 12 mesi | Legge approvata; primo riparto del Fondo (quota coesione dal 2027); struttura nazionale di progettazione operativa; regolamento IVASS | Governo, Parlamento, Regioni, IVASS |
| Fine legislatura | Fondo a regime dal 2029; schema assicurativo per le abitazioni attivo; prime delocalizzazioni; prima relazione della Corte dei conti | Protezione civile, CONSAP, Autorità di bacino, Comuni |

### Indicatori

| KPI | Base | 3 anni | 5 anni |
|---|---|---|---|
| Imprese con polizza catastrofale | 16% (aprile 2026, IVASS) | ≥ 50% | ≥ 80% |
| Consumo di suolo netto annuo | +102 km² (2025, ISPRA-SNPA) | ≤ 60 km² | ≤ 35 km² |
| Rapporto tra spesa per la prevenzione e spesa per le emergenze | dato pubblico consolidato assente: da costruire con RGS entro 100 giorni | ≥ 1:1 | ≥ 2:1 |

### Rischi e mitigazione

| Rischio | Mitigazione |
|---|---|
| "Tassa sulla casa" percepita | Copertura dentro la polizza incendio; riduzione dei premi per ISEE bassi; opt-out nell'ESSENZIALE |
| Azzardo morale | Franchigie; sconti per chi fa prevenzione; nessun indennizzo agli abusivi |
| Scarsa capacità di spesa dei Comuni | Progettazione nazionale o regionale; graduatoria con progetti esecutivi |
| Riordino della spesa emergenziale non reale | Conta solo il taglio certificato RGS; altrimenti si riduce la dotazione |
| Passività potenziale della riassicurazione | Garanzia esposta in bilancio; relazione della Corte dei conti |
| Uscita dalla coesione dopo il 2029 | Clausola di sostituzione con il ciclo 2028-34 o con gettito SAD |

---

## 03-P5 — Contratto agro-climatico

**Problema in un dato.** Nel 2024 l'agricoltura ha emesso **28,0 Mt CO₂eq**, il **7,7%** del totale nazionale. Il **69%** di queste emissioni viene da fermentazione enterica e deiezioni: 13,5 + 6,0 Mt. Fonte: Eurostat env_air_gge, serie `03_ghg_settori`. Il calo dal 2005 è modesto: da 33,0 a 28,0 Mt.

**Soluzione.**
- Nella PAC si sposta progressivamente il sostegno dai pagamenti per ettaro ai pagamenti per risultati misurati: carbonio nel suolo, acqua, azoto, biodiversità.
- Un fondo mutualistico contro siccità e grandine rafforza AgriCat, con contributo pubblico condizionato all'adattamento.
- Biometano dai reflui zootecnici e consulenza gratuita per le piccole aziende.

Il cofinanziamento nazionale viene dalla riforma dei SAD agricoli.

**Varianti.**

| Variante | Costo | Intensità | Fondi |
|---|---|---|---|
| PIENA | 0,50 | 1,0 | SAD 0,40 (SAD agricoli, menu) + RIALLOCAZIONE 0,10 |
| ESSENZIALE (risultati solo dentro la PAC; consulenza per le aziende sotto i 20 ha) | 0,25 | 0,55 | SAD 0,20 + RIALLOCAZIONE 0,05 |
| PILOTA (3 territori, circa 3.000 aziende) | 0,05 | 0,15 | RIALLOCAZIONE 0,05 |

### Articolato normativo essenziale (decreto legislativo "Contratto agro-climatico")

**Art. 1 (Finalità).** 1. Il presente decreto remunera gli agricoltori per risultati ambientali misurati e rafforza la loro protezione dai rischi climatici, per ridurre le emissioni agricole, preservare la fertilità dei suoli e la risorsa idrica e sostenere il reddito delle piccole e medie aziende.

**Art. 2 (Pagamenti per risultati).** 1. Nella modifica del Piano strategico nazionale della PAC e nella programmazione successiva al 2027, il MASAF destina una quota crescente degli interventi per il clima e l'ambiente a pagamenti commisurati a risultati misurati: carbonio organico del suolo, efficienza irrigua, bilancio dell'azoto, elementi del paesaggio. 2. Il CREA definisce entro dodici mesi protocolli semplificati di misurazione basati su dati satellitari e campionamenti.

**Art. 3 (Fondo mutualistico nazionale).** 1. Il contributo pubblico al fondo mutualistico nazionale per i danni da siccità, gelo e grandine è integrato con risorse nazionali, in misura decrescente nel quinquennio. È riconosciuto alle aziende che adottano le pratiche di adattamento definite con decreto del MASAF.

**Art. 4 (Reflui e consulenza).** 1. Gli allevamenti nelle zone vulnerabili ai nitrati della Pianura Padana hanno priorità nell'accesso agli incentivi esistenti per il biometano da reflui zootecnici. 2. Alle aziende con superficie agricola utilizzata inferiore a [PIENA: 50; ESSENZIALE: 20] ettari è assicurata consulenza tecnica gratuita tramite i servizi regionali e il CREA.

**Art. 5 (Copertura finanziaria).** 1. Agli oneri degli articoli 3 e 4, pari a [PIENA: 500; ESSENZIALE: 250] milioni di euro annui a regime, si provvede:
- a) per [400; 200] milioni mediante quota del maggior gettito derivante dalla revisione dei sussidi ambientalmente dannosi nel settore agricolo;
- b) per [100; 50] milioni mediante corrispondente riduzione degli stanziamenti del MASAF.

2. L'articolo 2 si attua con le risorse della PAC.

### Cronoprogramma

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | Tavolo con le organizzazioni agricole; proposta italiana per il negoziato PAC post-2027; mandato al CREA sui protocolli | MASAF, CREA, Regioni |
| 12 mesi | Protocolli di misurazione; modifica del Piano strategico (ecoschemi a risultato con adesione volontaria); integrazione nazionale di AgriCat | MASAF, AGEA, ISMEA |
| Fine legislatura | Pagamenti per risultati su almeno il 10% della SAU; revisione al 4° anno; regole nella PAC 2028-34 | MASAF, Commissione UE, Regioni |

### Indicatori

| KPI | Base | 3 anni | 5 anni |
|---|---|---|---|
| Emissioni agricole | 28,0 Mt CO₂eq (2024, Eurostat env_air_gge) | ≤ 27,0 Mt | ≤ 26,0 Mt |
| SAU sotto contratti a risultato | 0% (2026) | ≥ 5% | ≥ 15% |
| Aziende sotto i 20 ha aderenti, sul totale degli aderenti | da rilevare (AGEA) | ≥ 40% | ≥ 50% |

### Rischi e mitigazione

| Rischio | Mitigazione |
|---|---|
| Proteste agricole (come nel 2024) | Adesione volontaria iniziale; costruzione con le organizzazioni; riforma del gasolio agricolo graduale e compensata dal fondo mutualistico |
| Costi e incertezza della misurazione | Protocolli semplificati e dati satellitari pubblici; verifica a campione |
| Vincoli UE sulla PAC | Pilota come prova d'efficacia per il negoziato post-2027 |
| Gettito SAD conteso con 03-P1 | Con il dividendo PIENO, P5 scende a PILOTA o va coperta con altra riallocazione |

---

## Quadro di sintesi delle varianti (mld €/anno a regime)

| Proposta | PIENA | ESSENZIALE | PILOTA / ZERO | Fondi in bilancio permanenti | Una tantum / fuori bilancio |
|---|---|---|---|---|---|
| 03-P1 Dividendo climatico | 5,0 (1,0) | 1,2 (0,5) | ZERO 0 (0,2) | SAD | — |
| 03-P2 Rinnovabili a prezzo rinnovabile | 0,15 (1,0) | 0,07 (0,7) | ZERO 0 (0,45) | RIALLOCAZIONE | TARIFFE |
| 03-P3 Reti idriche e riuso | 1,15 (1,0) | 0,60 (0,6) | PILOTA 0,12 (0,15) | RIALLOCAZIONE (0,02-0,05) | COESIONE_2127, TARIFFE |
| 03-P4 Prevenzione e assicurazione | 1,50 (1,0) | 0,80 (0,6) | PILOTA 0,20 (0,25) | SAD, RIALLOCAZIONE | COESIONE_2127, TARIFFE |
| 03-P5 Contratto agro-climatico | 0,50 (1,0) | 0,25 (0,55) | PILOTA 0,05 (0,15) | SAD, RIALLOCAZIONE | — |

*Tra parentesi l'intensità.*

**Combinazione suggerita all'ottimizzatore:** P1 ESSENZIALE + P2 PIENA + P3 PIENA + P4 PIENA + P5 ESSENZIALE.
- Il prelievo SAD dell'area è di 1,2 + 0,5 + 0,2 = **1,9 mld**, sotto la capienza minima del registro (2,0).
- La quota coesione è di 1,2 mld una tantum.
- La riallocazione è di 0,6 mld.

Con P1 PIENA il prelievo SAD dell'area sale a 5,7 mld. Lo sostiene solo un menu SAD vicino al massimo, a spese di P4 e P5 o di altre aree.
