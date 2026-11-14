# GovernAI — Programma selezionato — scenario intermedio

*Generato da `programma/ottimizza.py`. Tutto finanziato nello scenario prudente: niente deficit, niente risparmi non certificati, gettito minimo delle coperture.*

Vincoli di scenario: forzate ['02-C2:ESSENZIALE', '05-C1:PIENA', '03-P4:ESSENZIALE', '07-C1:ESSENZIALE', '04-P6:ESSENZIALE', '07-C2:ESSENZIALE', '07-C3:ESSENZIALE', '09-C3:ESSENZIALE', '05-C2:ESSENZIALE', '05-C7:ESSENZIALE', '01-P7:ESSENZIALE', '02-C7:ESSENZIALE', '07-C4:ESSENZIALE', '09-C5:ESSENZIALE', '09-C8:ESSENZIALE', '03-P3:ESSENZIALE', '01-P3:ESSENZIALE', '01-P12:ESSENZIALE', '06-C3:ESSENZIALE', '05-C4:ESSENZIALE', '05-C5:ESSENZIALE', '02-C5:PILOTA', '09-C10:PILOTA', '06-C8:ESSENZIALE', '04-P8:ESSENZIALE'], escluse —, prioritarie per il momento ['05-C1', '05-C2', '05-C3', '05-C4', '05-C5', '05-C6', '05-C7', '05-C8', '05-C9', '02-C2', '02-C4', '02-C5', '02-C7', '06-C4', '06-C2', '06-C3', '06-C8', '06-C9'], coperture fino al livello tutti, coperture escluse RA11 SF01 SF11 SF12 SF13 SF14 FN01 FN03 SAD12 SAD14 PE01 PE02 SAD06 SAD07.

Priorità al nucleo robusto (Carta, regola 7): **attiva**.

**Escluse dalle linee rosse automatiche** (regole deterministiche, superabili solo con una scelta esplicita):

- 07-C5:PIENA: linea rossa segnalata dalla maggioranza del panel
- 07-C5:ESSENZIALE: linea rossa segnalata dalla maggioranza del panel
- SAD11: incompatibile (UE): art. 56 TFUE; Reg. (CE) 1008/2008 art. 15; CGUE C-70/99 Commissione/Portogallo (
- SF15: incompatibile (FIS): Dir. 2006/112/CE art. 98 par. 1-2 e art. 105 bis (Dir. 2022/542); DPR 633/1972 t
- 04-P3:PIENA: incompatibile (COS): artt. 117 c.4, 118, 119 Cost.; Corte cost. 222/2005
- 08-P3:PIENA: incompatibile (COS): artt. 64 c.3, 70, 138 Cost.
- AS05: copertura regressiva senza compensazione (Equità ≤ −2)
- RB05: copertura regressiva senza compensazione (Equità ≤ −2)

## Saldo

| Voce | mld €/anno a regime |
|---|---|
| Spesa delle misure scelte | 8,64 |
| di cui su risorse generali | 6,50 |
| Gettito minimo delle coperture attivate (risorse generali) | 6,56 |
| di cui tenuto da parte e non speso (riserva: per lo scenario intermedio, 0,04 per smettere di fumare e 0,02 per il dopo 2029) | 0,06 |
| Gettito minimo delle coperture attivate (totale) | 6,67 |
| Proposte nel programma | 63 su 78 |

La colonna **Robustezza** indica in quale quota delle combinazioni di pesi tra i valori la stessa scelta rientra nel programma ottimo. Sopra l'80% la scelta non dipende dalla sensibilità politica.

## Misure del programma

| Proposta | Titolo | Variante | Intensità | Costo | Robustezza |
|---|---|---|---|---|---|
| 02-C2 | Nido esigibile + congedo paterno | ESSENZIALE | 0,6 | 2,00 | 100% |
| 03-P4 | Prevenire costa meno: fondo prevenzione e assicurazione catastrofale | ESSENZIALE | 0,6 | 0,80 | 100% |
| 06-C3 | Case della Comunita' vive | ESSENZIALE | 0,6 | 0,80 | 100% |
| 03-P3 | Ogni goccia conta: reti idriche e riuso | ESSENZIALE | 0,6 | 0,60 | 100% |
| 05-C2 | Conto personale di competenze | ESSENZIALE | 0,5 | 0,45 | 100% |
| 05-C4 | Piu' persone con laurea o diploma terziario: ITS, lauree professionalizzanti, residenze | ESSENZIALE | 0,6 | 0,45 | 100% |
| 04-P6 | Restare e' possibile: servizi essenziali aree interne | ESSENZIALE | 0,6 | 0,42 | 100% |
| 07-C1 | Giustizia a regime: Ufficio per il processo e triage digitale | ESSENZIALE | 0,7 | 0,32 | 100% |
| 05-C1 | Nessuna esclusione: squadre di prossimita' contro la dispersione | PIENA | 1,0 | 0,25 | 100% |
| 07-C2 | Pena utile: misure di comunita' contro il sovraffollamento | ESSENZIALE | 0,6 | 0,25 | 100% |
| 07-C3 | Governance dei flussi migratori fondata sui dati | ESSENZIALE | 0,6 | 0,25 | 100% |
| 09-C3 | Squadre tecniche della Repubblica: pool di competenze per i piccoli enti | ESSENZIALE | 0,5 | 0,22 | 100% |
| 05-C5 | Scuole aperte come presidi di comunita' | ESSENZIALE | 0,5 | 0,20 | 100% |
| 05-C7 | Quota svantaggio nel finanziamento delle scuole | ESSENZIALE | 0,6 | 0,19 | 100% |
| 02-C5 | Progetto di vita esigibile e lavoro per le persone con disabilita' | PILOTA | 0,3 | 0,15 | 100% |
| 01-P7 | Dichiarazione zero: lo Stato fa il conto, chi dichiara controlla | ESSENZIALE | 0,6 | 0,15 | 100% |
| 06-C4 | Budget di cura per la non autosufficienza | PILOTA | 0,1 | 0,10 | 100% |
| 06-C8 | Squadre infermieristiche autonome di quartiere per l'ADI | ESSENZIALE | 0,4 | 0,10 | 100% |
| 02-C7 | Housing First dopo il PNRR | ESSENZIALE | 0,6 | 0,09 | 100% |
| 01-P3 | IVA in tempo reale | ESSENZIALE | 0,6 | 0,08 | 100% |
| 04-P8 | Camion a zero emissioni: patto per la transizione dell'autotrasporto | ESSENZIALE | 0,6 | 0,08 | 100% |
| 09-C5 | AI nella PA con le mani sul volante | ESSENZIALE | 0,6 | 0,08 | 100% |
| 09-C8 | Staffetta delle competenze: il ricambio generazionale come occasione di riqualificazione | ESSENZIALE | 0,4 | 0,08 | 100% |
| 07-C4 | Dal bene confiscato al bene comune | ESSENZIALE | 0,6 | 0,07 | 100% |
| 05-C10 | Rete nazionale per la ricerca applicata sul modello Fraunhofer | PILOTA | 0,1 | 0,05 | 100% |
| 01-P12 | Pagare è semplice, condonare no: semplificazione, riscossione efficace, sanzioni proporzionate | ESSENZIALE | 0,6 | 0,04 | 100% |
| 01-P14 | Sfide Italia: la pubblica amministrazione compra innovazione in tre fasi | PILOTA | 0,1 | 0,03 | 100% |
| 05-C8 | Biblioteche di comunita' | PILOTA | 0,1 | 0,03 | 100% |
| 06-C9 | Equipe di benessere scolastico in rete con la Casa della Comunita' | PILOTA | 0,1 | 0,03 | 100% |
| 05-C9 | Zaino culturale a scuola e tariffa sociale della cultura | PILOTA | 0,1 | 0,02 | 100% |
| 06-C10 | Meno burocrazia, più cura: automazione degli uffici sanitari e riqualificazione del personale amministrativo | PILOTA | 0,1 | 0,01 | 100% |
| 09-C9 | Squadra per la produttività pubblica con l'AI: meno lavoro ripetitivo, più servizi alle persone | PILOTA | 0,1 | 0,01 | 100% |
| 09-C10 | Bandi pubblici con istruttoria assistita: domande compilate una volta, controlli in giorni invece che in mesi | PILOTA | 0,1 | 0,01 | 100% |
| 01-P6 | Turismo che ripaga i territori: tassa di soggiorno intelligente | ZERO | 0,4 | 0,00 | 100% |
| 02-C1 | Salario minimo contrattuale garantito | ZERO | 0,3 | 0,00 | 100% |
| 02-C3 | Patto previdenziale tra generazioni | ZERO | 0,5 | 0,00 | 100% |
| 02-C6 | Bilancio generazionale e strategia demografica | ZERO | 0,3 | 0,00 | 100% |
| 03-P1 | Dividendo climatico: riforma SAD restituita alla cittadinanza | ZERO | 0,2 | 0,00 | 100% |
| 04-P5 | LEP prima: autonomia differenziata reversibile | ZERO | 0,5 | 0,00 | 100% |
| 05-C6 | AI a scuola | ZERO | 0,2 | 0,00 | 100% |
| 06-C1 | Tempo garantito o rimborso | ZERO | 0,2 | 0,00 | 100% |
| 08-P5 | Cooperazione che si misura: traiettoria APS | ZERO | 0,1 | 0,00 | 100% |
| 09-C2 | Chiedilo una volta sola: once-only con rimborso automatico | ZERO | 0,3 | 0,00 | 100% |
| 09-C4 | Cloud pubblico sostenibile e Patto per la manutenzione digitale | ZERO | 0,1 | 0,00 | 100% |
| 01-P9 | Una sola detrazione per il lavoro, senza scalini | ZERO | 0,2 | 0,00 | 100% |
| 01-P11 | Lo scontrino che conviene: un incentivo mirato al posto di lotterie e cashback | ZERO | 0,1 | 0,00 | 100% |
| 01-P5 | Energia a prezzo stabile per le PMI (PPA rinnovabili) | ESSENZIALE | 0,6 | 0,15 | 100% |
| 09-C7 | Automazione dei processi ripetitivi con riallocazione garantita | PILOTA | 0,1 | 0,02 | 100% |
| 08-P7 | Appalti a vetro: cruscotto pubblico dei rischi e dati aperti completi | PIENA | 1,0 | 0,01 | 100% |
| 03-P2 | Elettricita' rinnovabile a prezzo rinnovabile (CfD) | ZERO | 0,5 | 0,00 | 100% |
| 06-C6 | Dividendo della prevenzione e budget unico del farmaco | ZERO | 0,7 | 0,00 | 100% |
| 08-P4 | Beni pubblici europei: capacita' fiscale UE | PIENA | 1,0 | 0,00 | 100% |
| 01-P15 | Dalla scoperta all'impresa: prove di fattibilita', regole per gli spin-off, fondo di fondi deep tech | ZERO | 0,2 | 0,00 | 100% |
| 05-C3 | Carriere della ricerca | ZERO | 0,1 | 0,00 | 100% |
| 01-P2 | Spese fiscali a scadenza (sunset 5 anni) | PIENA | 1,0 | 0,01 | 99% |
| 04-P9 | Consegne pulite in citta': zone a emissioni zero per le merci | ZERO | 0,5 | 0,00 | 99% |
| 01-P8 | Meno scontrini: riordino delle detrazioni del 19% | ZERO | 0,4 | 0,00 | 99% |
| 08-P3 | Regole del gioco stabili (legge elettorale, voto fuorisede) | ZERO | 0,3 | 0,00 | 98% |
| 09-C6 | Lavoro pubblico misurato e giusto: organizzazione, valutazione vera e responsabilità | ZERO | 0,3 | 0,00 | 94% |
| 08-P2 | Patto per la buona legge | PIENA | 1,0 | 0,01 | 84% |
| 08-P1 | Legge sulla consulenza algoritmica pubblica | ESSENZIALE | 0,6 | 0,01 | 79% |
| 04-P4 | Nessuna grande opera senza prova dei numeri | ZERO | 0,3 | 0,00 | 78% |
| 01-P1 | Bilancio generazionale: ogni legge dichiara chi paga e quando | ESSENZIALE | 0,7 | 0,01 | 58% |

## Coperture attivate

| Misura | Descrizione | Fondo | Gettito min | Chi paga | Robustezza |
|---|---|---|---|---|---|
| SAD13 | Uscita completa entro il 2035 dal rimborso gasolio per autotrasporto e dall'agevolazione per il gasolio agricolo, oltre SAD01 e SAD02; sostegno a rinnovo delle flotte e redditi agricoli | SAD | 0,80 | Imprese di autotrasporto, aziende agricole; clientela finale tramite i prezzi | 100% |
| AS01 | Sigarette: ulteriore componente specifica di accisa di 25 € per 1.000 sigarette (circa 0,50 € a pacchetto) in due tappe 2028-2029, oltre a quanto già previsto da L. 199/2025 e DDL 2027 | ACCISE_SALUTE | 0,60 | Chi fuma (prelievo regressivo); filiera del tabacco | 100% |
| RA13 | Revisione strutturale della spesa dei ministeri: ulteriori 0,05% del PIL oltre quanto già nel DPB, con analisi a base zero dei programmi e tagli selettivi | RIALLOCAZIONE | 0,40 | Chi beneficia dei programmi tagliati (da individuare) | 100% |
| SF06 | Detrazione 19% delle spese sanitarie decrescente tra 50.000 e 120.000 € di reddito, salve disabilità, patologie croniche gravi e non autosufficienza (SF-SAN1, area 06) | SPESE_FISCALI | 0,35 | Contribuenti con reddito tra 50.000 e 120.000 € (azzerata oltre) | 100% |
| PE04 | Perequazione differenziata per 5 anni (2030-2034), prorogabile con legge motivata: rivalutazione al 50% (invece del 75%) sulla sola quota di pensione oltre 6 volte il minimo; al 75% negli anni con inflazione oltre il 4%; mai cumulata con altri raffreddamenti (proposta area 02) | RIALLOCAZIONE | 0,30 | Persone in pensione con trattamento oltre circa 3.700 €/mese lordi | 100% |
| SAD01 | Rimborso accise gasolio autotrasporto (EN.SI.19): esclusione Euro 5 dal 2028 e riduzione graduale di un terzo del rimborso per gli Euro 6; 25% del gettito a rinnovo flotte e intermodalità (Ferrobonus/Marebonus) | SAD | 0,30 | Imprese di autotrasporto merci (veicoli da 7,5 t) e passeggeri; in parte la clientela finale tramite i prezzi del trasporto | 100% |
| FN02 | Abolizione dal 2028 delle detrazioni 19% per premi assicurativi vita e infortuni (salvi i premi per non autosufficienza e per la tutela di persone con disabilità grave) e per spese veterinarie | SPESE_FISCALI | 0,25 | Persone capienti titolari di polizze vita/infortuni o proprietarie di animali, distribuite su tutti i decili dal quarto in su | 100% |
| RA06 | SSN: tetto di legge alla spesa per beni e servizi non sanitari degli enti, con gare centralizzate, e riduzione corrispondente del FSN (R-SAN2, area 06) | RIALLOCAZIONE | 0,20 | Fornitori non sanitari del SSN | 100% |
| RA14 | Codice degli incentivi: riordino completo, con abrogazione delle linee di incentivo alle imprese senza addizionalità dimostrata, oltre RA04 | RIALLOCAZIONE | 0,20 | Imprese beneficiarie di incentivi | 100% |
| SF10 | Iperammortamento (L. 199/2025 c. 427-436): riduzione della maggiorazione base per investimenti non qualificati, mantenuta per 4.0, immateriali e transizione (proposta area 01) | SPESE_FISCALI | 0,20 | Imprese che investono in beni strumentali ordinari | 100% |
| SF02 | Regime forfetario: aliquota sostitutiva 20% (invece di 15%) sul reddito corrispondente ai ricavi tra 50.000 e 85.000 €; nessun cambio sotto 50.000 € né alla soglia IVA | SPESE_FISCALI | 0,20 | Lavoratrici e lavoratori autonomi e piccole imprese forfetarie con ricavi tra 50.000 e 85.000 € | 100% |
| SF16 | Nuovo patent box (art. 6 DL 146/2021): nessun nuovo ingresso dal 2027 e uscita graduale per chi è già nel regime; risorse vincolate al credito unico per la ricerca (01-P13) | SPESE_FISCALI | 0,20 | Imprese con redditi da beni immateriali, in prevalenza con almeno 500 addetti (ISTAT) | 100% |
| RA05 | Abrogazione della riduzione del payback farmaceutico per le aziende che investono (DDL 2027 art. 71; R-SAN1, area 06) | RIALLOCAZIONE | 0,16 | Industria farmaceutica | 100% |
| RA12 | Fondo Nuove Competenze e quota del contributo 0,30% non destinata ai fondi interprofessionali confluiscono nel Conto competenze (proposta area 05) | RIALLOCAZIONE | 0,15 | Imprese e personale che oggi usano il Fondo Nuove Competenze | 100% |
| AS03 | Sugar tax: raddoppio delle aliquote dal 2029, dopo il primo anno di applicazione | ACCISE_SALUTE | 0,15 | Chi consuma bevande zuccherate; produttori (spinta a riformulare) | 100% |
| AS02 | Tabacco riscaldato e sigarette elettroniche: accisa avvicinata a quella delle sigarette tradizionali equivalenti (dal livello attuale a circa il 60-70%) | ACCISE_SALUTE | 0,15 | Chi consuma prodotti da inalazione senza combustione | 100% |
| SAD05 | Auto aziendali (TR.SI.04a): fine del regime transitorio per i contratti ante 2025 dal 2028 e percentuale imponibile dal 50% al 60% per i veicoli a combustione | SAD | 0,15 | Personale dipendente con auto aziendale a uso promiscuo; imprese (costo del welfare aziendale) | 100% |
| SAD02 | Gasolio agricolo (EN.SI.21): accisa dal 22% al 40% dell'aliquota normale in 5 anni, con credito per piccole aziende e montagna (mezzi a basse emissioni, biometano) | SAD | 0,15 | Aziende agricole, florovivaistiche, silvicole e della pesca in acque interne che usano gasolio agevolato | 100% |
| RA07 | Riserva di una quota delle facoltà assunzionali da turnover ai profili tecnici (ICT, appalti, progettazione) al posto dei profili amministrativi generici (R09-1, area 09) | RIALLOCAZIONE | 0,15 | Chi si candida a profili generici; uffici che non sostituiscono il personale | 100% |
| SAD03 | Accisa sul cherosene dei voli nazionali (EN.SI.04b) al 50% dell'aliquota normale in 3 anni; esenti le rotte in continuità territoriale (OSP) con Sardegna, Sicilia e isole minori | SAD | 0,12 | Compagnie aeree e chi viaggia sui voli nazionali non OSP | 100% |
| TS01 | Imposta di soggiorno: tetto massimo +2 €/notte nei comuni ad alta intensità turistica, con vincolo di destinazione a casa per residenti, trasporti e patrimonio | TASSA_SOGGIORNO | 0,10 | Chi pernotta nei comuni ad alta pressione turistica | 100% |
| SAD08 | Abolizione di quattro SAD energetici minori: deduzione forfetaria gestori carburanti (EN.SI.18), accisa ridotta gas grandi consumatori (EN.SI.20), GPL industriale (EN.SI.15), esenzione oli lubrificanti (EN.SI.03) | SAD | 0,10 | Gestori di impianti di distribuzione, grandi consumatori industriali di gas, imprese gomma/plastica | 100% |
| RB03 | Bonus lavoratrici madri (DDL 2027 art. 57): soglia di reddito da 40.000 a 32.000 € con uscita graduale fino a 40.000 € | RIORDINO_BONUS | 0,10 | Lavoratrici madri con 2 o più figli e reddito tra 32.000 e 40.000 € | 100% |
| RB04 | Carta del docente: quota di circa 150 € vincolata alla formazione su AI e didattica, al posto di acquisti liberi (proposta area 05) | RIORDINO_BONUS | 0,08 | Docenti di ruolo e supplenti annuali (minor libertà d'uso) | 100% |
| RB02 | Bonus nuovi nati 1.000 € (360 mln/anno, ISEE ≤40.000 €) assorbito in una maggiorazione dell'Assegno unico nel primo anno di vita per ISEE ≤25.000 € | RIORDINO_BONUS | 0,08 | Famiglie con una nuova nascita e ISEE tra 25.000 e 40.000 € | 100% |
| SF05 | Abrogazione delle spese fiscali minori e senza valutazione (fascia 10-20 mln e parte delle misure sotto 10 mln), con clausola di scadenza per le nuove | SPESE_FISCALI | 0,08 | Chi beneficia di agevolazioni minori e frammentate | 100% |
| SF07 | Fondi sanitari integrativi: deducibilità dei contributi (3.615,20 €) decrescente oltre 75.000 € di reddito, e stesso limite per i piani sanitari aziendali esenti (SF-SAN2, area 06) | SPESE_FISCALI | 0,08 | Persone iscritte ai fondi sanitari con reddito oltre 75.000 € | 100% |
| RA02 | Locazioni passive: piano di rientro negli immobili pubblici accelerato, obiettivo -20% dei canoni entro il 2030 | RIALLOCAZIONE | 0,08 | Soggetti privati che affittano immobili alla PA | 100% |
| AS04 | Superalcolici: accisa sull'alcol etilico +20% (birra e vino esclusi); integra AS-SAN2 dell'area 06 | ACCISE_SALUTE | 0,07 | Chi consuma superalcolici; produttori | 100% |
| RA01 | Acquisti centralizzati: obbligo Consip/soggetti aggregatori esteso a nuove categorie merceologiche per le amministrazioni centrali, con prezzi di riferimento vincolanti e taglio corrispondente degli stanziamenti | RIALLOCAZIONE | 0,07 | Fornitori della PA (prezzi più bassi), in parte PMI locali | 100% |
| RP08 | Ricambio selettivo nei profili amministrativi generici degli enti del Servizio sanitario nazionale: per 4 anni (2028-2031) si sostituisce il 75-85% delle cessazioni invece del 100%, con riduzione per legge del finanziamento del SSN d'intesa con le Regioni e destinazione in legge di bilancio a personale infermieristico e Case della Comunità (06-C2, 06-C3). Esclusi profili tecnici, informatici e sportelli di prenotazione; clausola di salvaguardia sui tempi dei servizi. Completa RP01, che esclude la sanità (proposta 06-C10) | RIALLOCAZIONE | 0,05 | Giovani che si candidano ai concorsi amministrativi delle aziende sanitarie; uffici amministrativi che lavorano con meno persone | 100% |
| SF09 | Detrazioni edilizie: aliquota ridotta per le unità diverse dall'abitazione principale non locate a canone concordato (proposta area 04) | SPESE_FISCALI | 0,05 | Chi ristruttura una seconda casa di proprietà | 100% |
| RA10 | Contributo unificato maggiorato per i litiganti seriali (oltre 500 cause l'anno) (proposta area 07) | RIALLOCAZIONE | 0,05 | Grandi litiganti: banche, assicurazioni, società di recupero crediti, utilities | 100% |
| SF04 | Cooperative: esclusione degli utili a riserva indivisibile ridotta dal 90% al 70% per le cooperative con ricavi oltre 50 mln €; invariata per le altre | SPESE_FISCALI | 0,05 | Grandi cooperative (consumo, servizi, agroalimentare) | 100% |
| RB01 | Carta Valore per i neodiplomati (180 mln/anno, universale): limite ISEE 35.000 € come per la vecchia Carta cultura | RIORDINO_BONUS | 0,05 | Persone neodiplomate di famiglie con ISEE oltre 35.000 € | 100% |
| SF03 | Tonnage tax e credito d'imposta armatoriale: rimodulazione con coefficienti legati a emissioni e bandiera UE, tetto al beneficio | SPESE_FISCALI | 0,05 | Imprese armatoriali | 100% |
| SF08 | Detrazione 19% per lo sport di ragazze e ragazzi 5-18 anni sostituita da offerta sportiva gratuita a scuola (proposta area 05) | SPESE_FISCALI | 0,04 | Famiglie che detraggono iscrizioni a palestre e associazioni sportive | 100% |
| RP01 | Turnover selettivo nei profili amministrativi generici di ministeri ed enti pubblici non economici nazionali: per 4 anni (2028-2031) si sostituisce il 75-85% delle cessazioni di quei profili invece del 100%, con taglio corrispondente delle facoltà assunzionali e degli stanziamenti. Esclusi: scuola, università, ricerca e cultura (MIM, MUR, MiC), giustizia, Interno, agenzie fiscali, sanità, sicurezza e soccorso, servizi sociali e inclusione (compresi gli sportelli e le prestazioni di inclusione INPS e la DG inclusione del Ministero del lavoro). Esclusa la quota riservata ai profili tecnici da RA07 | RIALLOCAZIONE | 0,04 | Giovani che si candidano ai concorsi per profili amministrativi generici (meno posti, soprattutto al Sud); uffici di supporto che lavorano con meno persone | 100% |
| RA09 | Spesa ICT corrente delle amministrazioni centrali -4/6%: dismissione dei CED residui, licenze duplicate, accordi quadro Consip (R09-3, area 09) | RIALLOCAZIONE | 0,04 | Fornitori di hosting e licenze legacy | 100% |
| SAD04 | Accisa sui carburanti della navigazione marittima nazionale (EN.SI.05b), esclusi collegamenti in continuità territoriale e pesca | SAD | 0,03 | Armatori di linee nazionali non OSP, crociere e trasporto turistico nazionale | 100% |
| RA04 | Trasferimenti correnti alle imprese: taglio del 3-5% delle linee di incentivo senza valutazione d'impatto positiva (esclusi i contratti di servizio di TPL, ferrovie e servizio postale), in attuazione del Codice degli incentivi | RIALLOCAZIONE | 0,03 | Imprese beneficiarie di incentivi correnti | 100% |
| RP06 | Enti previdenziali e assicurativi nazionali (INPS, INAIL) e altri EPNE: riduzione del 4% della spesa per beni e servizi rispetto al 2025, con versamento al bilancio dello Stato in aggiunta ai versamenti già previsti dalla L. 160/2019. Esclusi gli sportelli, i servizi per l'inclusione e le spese per prestazioni | RIALLOCAZIONE | 0,03 | Fornitori degli enti (ICT, servizi, logistica) | 100% |
| RP07 | Società e organismi partecipati: attuazione obbligatoria del Testo unico (d.lgs. 175/2016), con commissario ad acta, per le società senza dipendenti o con più amministratori che dipendenti, con fatturato sotto 1 mln o in perdita 4 anni su 5; amministratore unico e tetti ai compensi. Una quota dei risparmi certificati degli enti territoriali va alla finanza pubblica con intesa in Conferenza unificata. Esclusi i servizi pubblici locali essenziali e gli organismi dei servizi sociali | RIALLOCAZIONE | 0,02 | Componenti dei consigli di amministrazione e degli organi delle società chiuse o fuse; enti territoriali che cedono una quota dei risparmi | 100% |
| RA03 | Consulenze, studi, auto di servizio e rappresentanza: tetto del 20% sotto la spesa 2025 dei capitoli dedicati | RIALLOCAZIONE | 0,02 | Consulenze esterne, società di noleggio | 100% |
| SAD09 | Contributi agli impianti di risalita (AL.SD.17): metà riconvertita in un fondo per l'adattamento del turismo montano, metà risparmiata | SAD | 0,02 | Gestori di impianti di risalita e comprensori sciistici | 100% |
| SAD10 | Gasolio e GPL da riscaldamento nelle zone svantaggiate (EN.SI.22a/b): agevolazione sostituita in 4 anni da un contributo per pompe di calore e biomassa efficiente, con salvaguardia per ISEE ≤15.000 € | SAD | 0,02 | Famiglie in zone montane, Sardegna e isole minori che si scaldano con gasolio o GPL | 94% |
| RP04 | Accorpamento degli enti pubblici nazionali minori con funzioni sovrapposte e servizi comuni obbligatori (stipendi su NoiPA, contabilità, acquisti, gestione del personale) per gli enti sotto i 200 dipendenti; organi collegiali sostituiti da amministratore unico e revisore unico. Esclusi enti di ricerca, culturali, sanitari, socio-assistenziali e di soccorso | RIALLOCAZIONE | 0,01 | Componenti di consigli di amministrazione e collegi; personale di back-office che cambia sede o mansione (senza licenziamenti) | 100% |
| RP02 | Dirigenza: riduzione dell'8-12% dei posti di funzione dirigenziale di seconda fascia nei ministeri e negli enti pubblici non economici nazionali, accorpando gli uffici piccoli; i posti si sopprimono solo quando si liberano. Limite più basso agli incarichi dirigenziali a esterni (art. 19 c. 6 d.lgs. 165/2001). Esclusi MiC, MIM, MUR e le strutture sanitarie, sociali e di soccorso | RIALLOCAZIONE | 0,01 | Personale funzionario che aspira a incarichi dirigenziali; incarichi dirigenziali esterni non rinnovati | 100% |
| RA08 | Assistenza tecnica e studi d'impatto esterni sostituiti dai pool tecnici e dall'infrastruttura pubblica, oltre RA03 (R09-2, area 09) | RIALLOCAZIONE | 0,01 | Società di consulenza e assistenza tecnica | 100% |
| TS02 | Contributo di accesso per visitatori giornalieri nelle città d'arte sature (modello Venezia), facoltativo per i comuni | TASSA_SOGGIORNO | 0,01 | Chi visita in giornata le città aderenti | 66% |
| RP03 | Uffici di diretta collaborazione dei ministri, strutture di missione e strutture commissariali: tetto di spesa del 20% sotto il 2025 per indennità di diretta collaborazione, consulenze e collaborazioni esterne, personale comandato e funzionamento; organici massimi fissati e pubblicati. Non tocca le consulenze già in RA03 | RIALLOCAZIONE | 0,01 | Consulenze e collaborazioni esterne dei vertici politici; personale che perde l'indennità di diretta collaborazione | 100% |
| RP05 | Sedi degli uffici civili dello Stato: standard di spazio per addetto con lavoro agile e postazioni condivise, sedi uniche territoriali (più uffici statali nello stesso immobile) e rilascio degli immobili in eccesso; taglio dei capitoli di utenze, pulizia, vigilanza e manutenzione ordinaria. Non tocca i canoni (già in RA02) né le sedi di scuole, università, musei, biblioteche, archivi, servizi sociali e sanitari | RIALLOCAZIONE | 0,01 | Fornitori di pulizia, vigilanza e manutenzione; personale che perde la postazione fissa | 100% |
| PE03 | Chiusura definitiva delle 'quote' e di Opzione donna: nessun rinnovo, uscita anticipata solo con calcolo contributivo | PENSIONI | 0,00 | Persone vicine alla pensione che avrebbero usato le quote | 80% |
| FN04 | Imposta sostitutiva sui premi di produttività: limite di reddito per beneficiarne ridotto da 80.000 a 50.000 euro dal 2028 | SPESE_FISCALI | 0,00 | Personale dipendente privato con reddito tra 50.000 e 80.000 euro che ricevono premi di risultato | 100% |

## Proposte non incluse

Restano fuori perché, con le risorse disponibili, altre misure danno più valore per euro, oppure perché il loro effetto netto sui valori è negativo. *Rientrano se si trovano coperture aggiuntive.*

- 01-P10 Controlli mirati con garanzie: usare meglio i dati che il fisco ha già, senza sorvegliare tutti (scelta in 0% delle combinazioni di pesi)
- 01-P13 Un solo credito per la ricerca: stabile, piu' forte per le piccole imprese, certificato prima di spendere (scelta in 1% delle combinazioni di pesi)
- 01-P4 Crescere conviene: eliminare i gradini dimensionali (scelta in 11% delle combinazioni di pesi)
- 02-C4 Reddito di inclusione universale (scelta in 0% delle combinazioni di pesi)
- 03-P5 Contratto agro-climatico (scelta in 0% delle combinazioni di pesi)
- 04-P1 Patto di continuita' post-PNRR (scelta in 0% delle combinazioni di pesi)
- 04-P2 Casa a canone giusto (scelta in 0% delle combinazioni di pesi)
- 04-P3 Prima il treno di chi viaggia ogni giorno: fondo TPL e abbonamento unico (scelta in 0% delle combinazioni di pesi)
- 04-P7 Dal porto al treno: piu' merci sul ferro (scelta in 0% delle combinazioni di pesi)
- 06-C2 Patto per il personale infermieristico e la medicina generale (scelta in 0% delle combinazioni di pesi)
- 06-C5 Salute mentale al 5% (scelta in 0% delle combinazioni di pesi)
- 07-C5 Difesa: percorso NATO 3,5% vincolato a efficienza europea (scelta in 28% delle combinazioni di pesi)
- 07-C6 Scudo cyber territoriale (scelta in 0% delle combinazioni di pesi)
- 08-P6 Export resiliente (scelta in 0% delle combinazioni di pesi)
- 09-C1 Stato a vetro: infrastruttura aperta per l'analisi delle politiche (scelta in 1% delle combinazioni di pesi)

## Uso dei fondi

| Fondo | Spesa | Gettito/capienza disponibile |
|---|---|---|
| ACCISE_SALUTE | 0,33 | 0,97 |
| COESIONE_2127 | 1,86 | 2,00 |
| PENSIONI | 0,00 | 0,00 |
| RIALLOCAZIONE | 2,34 | 2,04 |
| RIORDINO_BONUS | 1,09 | 0,31 |
| SAD | 0,67 | 1,69 |
| SPESE_FISCALI | 2,07 | 1,55 |
| TARIFFE | 0,27 | — |
| TASSA_SOGGIORNO | 0,00 | 0,11 |

Risorse generali (fungibili): spesa 6,50 ≤ gettito 6,56.
