# GovernAI — Schede pronte, Area 11: Contrasto all'evasione fiscale e contributiva

*Agente "contrasto all'evasione", 8 novembre 2026. Varianti in `programma/varianti/11_evasione.csv`; gettito atteso in `benchmark/nuove_proposte_evasione.csv`. Fonte principale: MEF, Relazione sull'economia non osservata e sull'evasione fiscale e contributiva 2026 (testo in `dati/raw/01_mef_relazione_evasione_2026.txt`, di seguito "Relazione 2026"). "Stima GovernAI" indica una stima propria senza quantificazione ufficiale; "da verificare" un dato non controllato su fonte primaria. Importi in mld €/anno. Documento di consulenza: le decisioni spettano a Governo e Parlamento.*

## Regole comuni a tutte le schede

- **Il recupero di evasione non copre spesa.** Nessuna variante usa IVA_EVASIONE, RISPARMI_ATTESI o DEFICIT. Il costo nel CSV è solo quello di attuazione (personale, IT, audit, eventuali spese fiscali). Il gettito atteso è scritto nelle note e nel file benchmark: va al deficit e può finanziare spesa permanente solo dopo certificazione a consuntivo nella Relazione annuale. In più, il maggior gettito da adempimento non crea spazio sul tetto alla spesa netta UE (`giuridico/quadro.md`, par. 1).
- **Nessuna duplicazione di 01-P3 (IVA in tempo reale).** Le tre schede coprono ciò che 01-P3 lascia fuori: imposte dirette di autonomi e imprese, contributi, catasto, dati esteri (01-P10); il rapporto con il consumatore finale (01-P11); semplificazione, riscossione e sanzioni (01-P12). Le integrazioni proposte a 01-P3 sono nel riquadro finale.
- **Statuto delle garanzie (valore SIC).** Ogni uso di dati personali segue le regole di 01-P10, art. 3: legge che elenca banche dati e finalità; dati pseudonimizzati fino alla selezione motivata; DPIA pubblica e parere del Garante; nessuna decisione automatica; divieto di variabili sensibili; registro pubblico dei modelli; audit indipendente; nessuna nuova raccolta massiva. **Linee rosse:** niente accesso al contenuto delle comunicazioni (art. 15 Cost.), niente punteggi di "affidabilità" delle persone usati fuori dal fisco, niente liste pubbliche di nomi, niente estensione dei dati fiscali a finalità extra-fiscali senza una legge specifica.

## Diagnosi in cinque dati (Relazione 2026, tabelle I.1, I.2, I.6 e cap. IV)

| Dato | Valore 2023 | Lettura |
|---|---|---|
| Tax gap totale (tributi + contributi) | 107,9-112,8 mld | propensione all'evasione tributaria 17,1-17,3%, -2,4 punti sul 2019 |
| IRPEF lavoro autonomo e impresa | 38,4 mld, **propensione 59,7%** | la voce più grande e quella che scende meno (circa -5% in vent'anni) |
| IVA | 34,4 mld, propensione 20,3%; VAT gap ~15% contro ~9,5% medio UE | oggetto di 01-P3 |
| Contributi (quota a carico di chi lavora + quota datoriale) | 9,2-12,7 mld | +0,8/1,2 mld sul 2022 (circa +10%) |
| Mancati versamenti (dichiarato ma non pagato) | circa 17% del gap (~17 mld); oltre il 30% nel caso di IVA e IRAP | problema di riscossione e liquidità, non di occultamento |

Cosa funziona già: la fatturazione elettronica B2B ha recuperato 1,7-2,1 mld di IVA l'anno (Relazione 2020, citata dalla Relazione 2026); l'Archivio dei rapporti finanziari, usato con DPIA approvata dal Garante (provv. n. 276 del 30/7/2022), ha prodotto 27.197 avvisi e 0,99 mld di maggiore imposta accertata nel 2023-25 (0,51 mld nel 2025); nel 2025 l'Agenzia ha inviato oltre 3,19 milioni di lettere di compliance; il regime di adempimento collaborativo conta 221 società e circa 49 mld di imponibile presidiato.

**Quadro delle varianti (costo di attuazione a regime, intensità)**

| Proposta | PIENA | ESSENZIALE | PILOTA / ZERO | Gettito atteso PIENA (non è copertura) | Variante raccomandata |
|---|---|---|---|---|---|
| 01-P10 Controlli mirati con garanzie | 0,10 · 1 | 0,06 · 0,6 | PILOTA 0,02 · 0,2 | 1,5-3,5 | PIENA |
| 01-P11 Lo scontrino che conviene | 0,50 · 1 | 0,20 · 0,5 | ZERO 0 · 0,15 | 0,2-0,9 lordo (saldo netto incerto) | ZERO, poi ESSENZIALE se la valutazione è positiva |
| 01-P12 Pagare è semplice, condonare no | 0,06 · 1 | 0,04 · 0,6 | ZERO 0 · 0,3 | 0,8-2,0 | PIENA |

Pacchetto raccomandato (P10 piena, P11 zero, P12 piena): **circa 0,16 mld/anno a regime**, tutti in RIALLOCAZIONE (bilancio MEF e agenzie fiscali). Gettito atteso a regime (2031) 2,3-5,5 mld, stima GovernAI, da non contare come copertura.

---

## 01-P10 — Controlli mirati con garanzie: usare meglio i dati che il fisco ha già, senza sorvegliare tutti

**Problema in un dato.** Sui redditi di lavoro autonomo e d'impresa l'imposta evasa è **38,4 mld nel 2023**, pari al **59,7%** di quella dovuta (Relazione 2026, tab. I.1 e I.2). Il gap contributivo è di 9,2-12,7 mld e cresce. Eppure dove il fisco usa bene i dati che ha già, con garanzie, il risultato c'è: l'Archivio dei rapporti finanziari ha prodotto 0,51 mld di maggiore imposta accertata nel 2025, partendo da 154 avvisi nel 2023 e arrivando a 15.873.

**Soluzione.** Si fa **meno controllo a pioggia e più controllo mirato**. L'Agenzia delle entrate, l'INPS e l'INL incrociano soltanto banche dati **che già possiedono per legge**: fatture elettroniche, corrispettivi, saldi e movimentazioni aggregate dell'Archivio dei rapporti finanziari, catasto, contributi e comunicazioni obbligatorie di lavoro, dati esteri CRS e DAC. Lo scopo è individuare le incongruenze più gravi tra reddito dichiarato e flussi economici. Il primo passo è sempre una **lettera di compliance**, che permette di correggere con sanzioni ridotte. L'accertamento arriva solo dopo, con contraddittorio. In cambio la legge fissa uno **Statuto delle garanzie**: è la condizione per fare tutto questo senza scivolare nella profilazione di massa.

Esperienze estere. In Danimarca il reddito comunicato da terzi è evaso quasi per niente (circa 0,3%), quello autodichiarato molto di più (Kleven et al., *Econometrica* 2011): l'incrocio con dati di terzi funziona. Nel Regno Unito il sistema HMRC "Connect" seleziona i controlli incrociando fonti diverse, e le lettere con "norma sociale" aumentano i pagamenti spontanei (Hallsworth et al., *Journal of Public Economics* 2017). La Polonia (STIR, dal 2018) usa i conti bancari solo per le frodi IVA, con blocchi temporanei motivati. Ci sono però anche **lezioni negative, che fondano le garanzie**: nei Paesi Bassi il tribunale dell'Aia ha annullato il sistema di profilazione SyRI per violazione dell'art. 8 CEDU (5/2/2020). Lo scandalo dei sussidi per l'infanzia (*toeslagenaffaire*) ha portato alle dimissioni del governo nel 2021 e a una sanzione dell'Autorità privacy olandese all'amministrazione fiscale, perché il modello di rischio usava la nazionalità. In Australia il sistema automatico "Robodebt" è stato giudicato illegittimo da una Royal Commission (2023). La Corte di giustizia UE (C-175/20, 24/2/2022) ha chiarito che le richieste massive di dati da parte del fisco devono rispettare minimizzazione e proporzionalità.

**Varianti**

| Variante | Contenuto | Costo a regime (2027 / 2028 / 2029) | Intensità |
|---|---|---|---|
| PIENA | analisi del rischio integrata su imposte dirette, contributi e IMU; catasto e "immobili fantasma"; dati CRS, DAC7 e DAC8; lettere di compliance; Statuto delle garanzie; circa 800 unità di personale per analisi e controlli | 0,10 (0,08 / 0,12 / 0,12), RIALLOCAZIONE | 1 |
| ESSENZIALE | solo IRPEF lavoro autonomo e impresa e contributi, con dati fiscali, INPS e Archivio; Statuto delle garanzie; senza catasto ed estero | 0,06 (0,05 / 0,07 / 0,07) | 0,6 |
| PILOTA | tre settori con alta evasione e lavoro irregolare (edilizia, ristorazione e alloggio, logistica in appalto) per 2 anni, con gruppo di controllo e valutazione indipendente | 0,02 | 0,2 |

Motivazione delle intensità: le voci escluse dalla variante essenziale (IMU 4,9 mld, redditi esteri, IRES 12,0 mld) valgono circa un terzo della base aggredibile. Il pilota copre una minoranza del gap, ma permette di misurare il rendimento netto e i falsi positivi prima di estendere la misura.

**Articolato normativo essenziale** (disegno di legge; attuazione con provvedimenti della direzione delle agenzie, sentito il Garante)

> **Art. 1 (Finalità).** 1. La presente legge rafforza la selezione dei controlli fiscali e contributivi mediante l'uso delle informazioni già legittimamente detenute dalle amministrazioni, nel rispetto degli articoli 2, 3, 13, 15, 23 e 53 della Costituzione, dell'articolo 8 della Convenzione europea dei diritti dell'uomo e del regolamento (UE) 2016/679.
>
> **Art. 2 (Banche dati e finalità).** 1. Ai soli fini dell'analisi del rischio di evasione fiscale e contributiva, l'Agenzia delle entrate, l'Istituto nazionale della previdenza sociale e l'Ispettorato nazionale del lavoro possono interconnettere esclusivamente le banche dati elencate nell'allegato A alla presente legge. 2. È vietata l'acquisizione di nuove categorie di dati personali in forma generalizzata. È altresì vietato l'accesso al contenuto di comunicazioni e corrispondenza. 3. L'allegato A è modificabile solo con legge.
>
> **Art. 3 (Statuto delle garanzie).** 1. I dati sono trattati in forma pseudonimizzata. La reidentificazione è consentita solo per le posizioni selezionate, con provvedimento motivato di un funzionario e accesso tracciato. 2. Nessun atto impositivo, sanzione, sospensione o blocco è adottato sulla sola base di un trattamento automatizzato. Si applicano l'articolo 22 del regolamento (UE) 2016/679 e il contraddittorio preventivo di cui all'articolo 6-bis della legge 27 luglio 2000, n. 212. 3. I modelli di rischio non utilizzano dati di cui agli articoli 9 e 10 del regolamento (UE) 2016/679, né la nazionalità o il luogo di nascita, né variabili che li approssimano. Sono sottoposti ogni anno a un test di distorsione per genere, età e territorio. 4. Ciascun modello è iscritto, prima dell'uso, in un registro pubblico che ne indica finalità, categorie di dati, metriche di errore ed esiti degli audit, senza rivelare le soglie operative. 5. Ogni nuovo modello è preceduto da una valutazione d'impatto ai sensi dell'articolo 35 del regolamento (UE) 2016/679, pubblicata per estratto, e dal parere del Garante per la protezione dei dati personali, da rendere entro sessanta giorni. 6. Il contribuente selezionato è informato che il controllo deriva da un'analisi del rischio e dei criteri generali che l'hanno determinata. 7. I dati sono conservati non oltre la scadenza dei termini di accertamento. 8. Gli accessi non giustificati costituiscono illecito disciplinare grave.
>
> **Art. 4 (Prima la correzione).** 1. Salvo il caso di frode o di reato, la prima azione conseguente alla selezione è una comunicazione che consente la regolarizzazione con le riduzioni del ravvedimento operoso.
>
> **Art. 5 (Audit e relazione).** 1. Un comitato di tre esperti indipendenti, nominati dal Garante, dalla Corte dei conti e dall'ISTAT, verifica ogni anno i modelli, i falsi positivi e gli esiti dei controlli. Il Ministro dell'economia e delle finanze trasmette la relazione alle Camere, allegata alla Relazione sull'economia non osservata.
>
> **Art. 6 (Copertura e uso delle maggiori entrate).** 1. Agli oneri, pari a 80 milioni di euro per il 2027, a 120 milioni per ciascuno degli anni 2028 e 2029 e a 100 milioni a decorrere dal 2030, si provvede mediante corrispondente riduzione delle spese di funzionamento del Ministero dell'economia e delle finanze e delle agenzie fiscali, con esclusione delle spese per il personale. 2. Le maggiori entrate non sono utilizzate a copertura di nuove o maggiori spese. Accertate a consuntivo, concorrono alla riduzione dell'indebitamento netto.
>
> **Art. 7 (Revisione).** 1. Decorsi quattro anni, la Corte dei conti riferisce alle Camere su efficacia e proporzionalità del sistema. In assenza di una legge di conferma, l'interconnessione di cui all'articolo 2 limitata alle banche dati INPS e INL cessa al termine del quinto anno.

**Cronoprogramma**
- *Primi 100 giorni:* ddl e allegato A; tavolo AdE, INPS, INL e Garante sulla DPIA unitaria, con base nella DPIA del 2022 sull'Archivio; avvio del PILOTA nei tre settori con atto amministrativo, sulle basi giuridiche vigenti (L. 160/2019, art. 1, c. 682-686; d.lgs. 13/2024, art. 2).
- *Entro 12 mesi:* legge approvata; registro pubblico dei modelli online; nomina del comitato di audit; primo ciclo di lettere integrate tra fisco e contributi.
- *Entro fine legislatura:* sistema a regime; due relazioni di audit; prima misura del calo della propensione IRPEF lavoro autonomo nella Relazione evasione (con 2-3 anni di ritardo statistico); revisione della Corte dei conti.

**Indicatori**

| KPI | Base (dato, anno, fonte) | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Propensione al gap IRPEF lavoro autonomo e impresa | 59,7%, 2023 (Relazione 2026, tab. I.2) | ≤ 57% | ≤ 55% (-5/-8% del gap = 1,9-3,1 mld) |
| Gap contributivo | 9,2-12,7 mld, 2023 (tab. I.1) | -5% | -10% |
| Maggiore imposta accertata da analisi su dati finanziari | 0,51 mld, 2025 (Relazione 2026, tab. IV.1.1.5) | ≥ 0,8 mld | ≥ 1,0 mld, con quota riscossa pubblicata |
| Modelli di rischio iscritti nel registro pubblico con DPIA e audit | 0%, 2026 (registro inesistente) | 100% | 100% |
| Controlli selezionati chiusi senza rilievi o annullati in autotutela o in giudizio (falsi positivi) | da rilevare, 2027 | pubblicato ogni anno | in calo e ≤ soglia fissata dal comitato |

**Rischi e garanzie**
- *Deriva verso la sorveglianza di massa (SIC).* Banche dati elencate solo per legge, nessuna nuova raccolta generalizzata, pseudonimizzazione, clausola di revisione a 5 anni. Si tratta di dati che il fisco ha già: la proposta ne regola l'uso, non ne aggiunge.
- *Discriminazione algoritmica* (lezione SyRI e *toeslagenaffaire*). Divieto di variabili sensibili e di loro approssimazioni, test di distorsione annuale, comitato indipendente. Il considerando 59 dell'AI Act esclude di regola i sistemi delle autorità fiscali dalla classe "alto rischio": GovernAI impone comunque per legge garanzie equivalenti (supervisione umana, registro, audit), in linea con la L. 132/2025.
- *Falsi positivi e costi per chi paga regolarmente.* Lettera prima dell'accertamento, contraddittorio, falsi positivi pubblicati e usati come indicatore di qualità, non solo di quantità.
- *Accertato non è riscosso.* L'indicatore di gettito usa gli incassi, non la maggiore imposta accertata. Il gettito atteso (1,5-3,5 mld a regime, stima GovernAI) è già ridotto per questo motivo.
- *Precedente del redditometro.* Il nuovo decreto del 7/5/2024 è stato sospeso dopo le polemiche (da verificare lo stato attuale). Qui la spesa delle famiglie non è usata per ricostruire il reddito: si confrontano flussi economici d'impresa e professionali con quanto dichiarato.

---

## 01-P11 — Lo scontrino che conviene: un incentivo mirato al posto di lotterie e cashback

**Problema in un dato.** Nel rapporto tra impresa e consumatore finale l'evasione si fa con lo scontrino non emesso o con il "nero" concordato. È qui che si concentra l'IRPEF evasa nel lavoro autonomo (59,7% di propensione) e la parte B2C del gap IVA (20,3%). Gli incentivi usati finora hanno dato risultati scarsi o non misurati:
- **Cashback di Stato** (dicembre 2020-giugno 2021): costo dell'ordine di 1,5-2 mld nel periodo (da verificare, consuntivo MEF/Consap). È stato sospeso dal DL 99/2021, anche perché i rimborsi andavano soprattutto a chi già pagava con carta, cioè famiglie più abbienti e territori con più pagamenti elettronici (da verificare sulle analisi UPB e Banca d'Italia).
- **Lotteria degli scontrini** (dal 2021): a oltre cinque anni dall'avvio manca una valutazione d'impatto pubblica sul gettito, e la partecipazione è rimasta limitata (dato ADM da verificare).

**Soluzione.** Si sostituisce un premio a caso con un **vantaggio certo e mirato**, sul modello portoghese *e-fatura*: dal 2013 chi chiede la fattura con il proprio codice fiscale in alcuni settori ad alta evasione recupera una parte dell'IVA pagata (15%, con tetto per famiglia). Chi compra diventa così parte interessata al controllo. È lo stesso meccanismo che in Brasile (Nota Fiscal Paulista) ha aumentato del 21% in quattro anni i ricavi dichiarati dal commercio al dettaglio (Naritomi, *American Economic Review* 2019).

In Italia la misura riguarda solo i servizi alle famiglie dove la detrazione oggi non esiste: riparazioni di casa e auto, servizi alla persona (parrucchieri, estetica), ristorazione, veterinari. Ha una **scadenza a 5 anni**, come chiede 01-P2 per tutte le spese fiscali, e viene valutata dopo 3. Il collegamento tra POS e registratori di cassa, già obbligatorio, rende verificabile l'incrocio.

**Garanzie privacy specifiche.** Comunicare il codice fiscale è una **scelta di chi compra**, mai un obbligo. Il fisco riceve solo l'importo aggregato per settore e per esercente, non il dettaglio dei beni (in coerenza con i limiti posti dal Garante alla memorizzazione dei dati di dettaglio delle fatture elettroniche, 2018-2019, da verificare gli estremi dei provvedimenti). I dati servono solo alla detrazione e al riscontro con i corrispettivi dell'esercente: non sono usati per ricostruire il reddito di chi compra.

**Varianti**

| Variante | Contenuto | Costo a regime (2027 / 2028 / 2029) | Intensità |
|---|---|---|---|
| PIENA | detrazione del 15% dell'IVA pagata con documento nominativo e pagamento tracciabile in 5 settori, tetto 150 € per contribuente; scadenza a 5 anni; chiusura della lotteria degli scontrini; protocollo per commissioni POS nulle sotto i 10 € per i micro-esercenti | 0,50 (0,01 / 0,02 / 0,50), SPESE_FISCALI 0,47 + RIALLOCAZIONE 0,03 | 1 |
| ESSENZIALE | 3 settori (riparazioni di casa e auto, servizi alla persona), 10% dell'IVA, tetto 100 €; scadenza a 5 anni; chiusura della lotteria | 0,20 (0,01 / 0,01 / 0,20), SPESE_FISCALI 0,18 + RIALLOCAZIONE 0,02 | 0,5 |
| ZERO | valutazione indipendente, entro 12 mesi, di lotteria e cashback con dati ADM e AdE; chiusura della lotteria se l'effetto netto è nullo; protocollo POS; nessuna nuova spesa | 0 | 0,15 |

La detrazione maturata nel 2028 si usa nella dichiarazione del 2029: per questo il costo pieno compare dal 2029. La copertura SPESE_FISCALI va inserita dall'agente coperture come nuova misura del menu, per esempio rimodulando detrazioni che non richiedono tracciabilità. La riga RIALLOCAZIONE corrisponde ai premi e alla gestione della lotteria (importo da verificare con ADM).

**Articolato normativo essenziale** (legge di bilancio)

> **Art. 1 (Detrazione per il documento commerciale nominativo).** 1. Dal periodo d'imposta 2028 e fino al periodo d'imposta 2032, alle persone fisiche spetta una detrazione dall'imposta lorda pari al 15 per cento dell'imposta sul valore aggiunto assolta sugli acquisti di servizi dei settori indicati nell'allegato B. La detrazione spetta se l'acquisto è documentato da fattura elettronica o documento commerciale recante il codice fiscale dell'acquirente ed è pagato con strumenti tracciabili, entro il limite di 150 euro annui. 2. La comunicazione del codice fiscale è facoltativa. L'Agenzia delle entrate riceve, per ciascuna persona acquirente, solo l'importo complessivo per settore e lo utilizza esclusivamente ai fini della detrazione e del riscontro con i corrispettivi dell'esercente, previa valutazione d'impatto ai sensi dell'articolo 35 del regolamento (UE) 2016/679, sentito il Garante.
>
> **Art. 2 (Lotteria degli scontrini).** 1. La lotteria di cui all'articolo 1, commi 540 e seguenti, della legge 11 dicembre 2016, n. 232, cessa dal 1° gennaio 2028. Le relative risorse concorrono alla copertura dell'articolo 1.
>
> **Art. 3 (Commissioni sui micropagamenti).** 1. Il Ministro delle imprese e del made in Italy promuove con i prestatori di servizi di pagamento un protocollo per l'azzeramento delle commissioni sui pagamenti di importo inferiore a 10 euro presso gli esercenti con ricavi fino a 400.000 euro. La Banca d'Italia ne monitora l'attuazione.
>
> **Art. 4 (Valutazione e scadenza).** 1. Entro il 30 giugno 2031 il Dipartimento delle finanze pubblica una valutazione controfattuale dell'effetto della detrazione sui ricavi dichiarati nei settori interessati. La detrazione non è prorogata in assenza di una valutazione positiva.

**Cronoprogramma**
- *Primi 100 giorni:* avvio della valutazione indipendente di lotteria e cashback (variante ZERO, sempre attivata); DPIA con il Garante; tavolo POS.
- *Entro 12 mesi:* norma in legge di bilancio 2028 se la valutazione lo giustifica; adeguamento dei registratori di cassa (software, nessun nuovo apparecchio); campagna informativa.
- *Entro fine legislatura:* primo anno di detrazioni in dichiarazione; valutazione controfattuale sui ricavi dichiarati dei settori rispetto a settori simili non incentivati.

**Indicatori**

| KPI | Base (dato, anno, fonte) | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Ricavi dichiarati nei settori incentivati rispetto a settori di controllo | da rilevare, 2027 (AdE, corrispettivi telematici) | +5% | +10% (Brasile: +21% in 4 anni) |
| Quota di documenti commerciali con codice fiscale nei settori | da rilevare, 2027 (AdE) | ≥ 15% | ≥ 30% |
| Propensione al gap IVA | 20,3%, 2023 (Relazione 2026, tab. I.2) | in calo, misurata insieme a 01-P3 | ≤ 17% (obiettivo condiviso con 01-P3) |
| Costo per euro di gettito emerso | non applicabile | pubblicato | < 1 (altrimenti la detrazione decade) |

**Rischi e garanzie**
- *Costo superiore al gettito.* È il rischio principale: il gettito lordo atteso è di 0,2-0,9 mld (stima GovernAI) a fronte di 0,5 mld di costo della variante PIENA, quindi il saldo netto è tra -0,3 e +0,4 mld. Per questo la raccomandazione è ZERO, poi ESSENZIALE solo se la valutazione è positiva, con scadenza automatica.
- *Regressività.* Il tetto basso e i settori scelti (servizi d'uso comune, non beni di lusso) limitano il vantaggio dei redditi alti. Va verificato per decile in sede di valutazione, come previsto da 01-P2.
- *Raccolta dati sui consumi (SIC).* Adesione facoltativa, solo importi aggregati, finalità esclusiva, nessun uso per accertamenti su chi compra.
- *Frodi sulla detrazione* (scontrini gonfiati). Riscontro automatico con i corrispettivi dell'esercente e pagamento tracciabile obbligatorio.
- *Accordo collusivo* (si dichiara meno con lo sconto in nero). L'incentivo di 15% dell'IVA, circa 3% del prezzo, è modesto: per questo la misura è un complemento di 01-P10 e 01-P3, non un sostituto.

---

## 01-P12 — Pagare è semplice, condonare no: semplificazione, riscossione efficace, sanzioni proporzionate

**Problema in un dato.** Circa **17 mld di gap (17% del totale, 2023)** non sono evasione nascosta ma **imposte dichiarate e non versate**. Questa componente è salita dal 15% del 2019 e supera il 30% del gap per IVA e IRAP (Relazione 2026, cap. I). Il magazzino dei crediti affidati all'agente della riscossione è in gran parte di difficile esazione (prima Relazione della Commissione tecnica per il riordino della riscossione). Le definizioni agevolate ricorrenti insegnano ad aspettare il prossimo condono.

**Soluzione.** Si previene l'evasione rendendo l'adempimento più facile e la riscossione più rapida, con sanzioni graduate. Cinque leve:
1. **IVA e redditi precompilati per le piccole partite IVA.** Per forfettari e semplificati, registri, liquidazioni e dichiarazione sono generati da fatture e corrispettivi: il contribuente conferma o corregge. È il modello estone e portoghese, e il percorso di *Making Tax Digital* nel Regno Unito.
2. **Adempimento collaborativo più largo.** Si rispetta il calendario delle soglie del d.lgs. 221/2023 (da verificare: 500 mln dal 2026, 100 mln dal 2028) e si introduce una **versione semplificata per le medie imprese**, con sistema di controllo fiscale certificato da un soggetto professionale abilitato. In cambio: risposte rapide e sanzioni ridotte.
3. **Riscossione efficace.** Il tempo tra accertamento e riscossione si accorcia. La rateazione è automatica online, con addebito diretto. I crediti inesigibili sono discaricati, come propone la Commissione tecnica. L'azione si concentra sui crediti recuperabili. Si usa la piattaforma CESOP sui pagamenti transfrontalieri (direttiva 2020/284) per chi ha debiti e attività all'estero.
4. **Sanzioni proporzionate.** Le riduzioni del d.lgs. 87/2024 restano per chi sbaglia e corregge. Le sanzioni sono piene, con sanzioni accessorie (sospensione dell'attività), per frode, recidiva nello scontrino non emesso e crediti inesistenti. Non ci sono liste pubbliche di nomi: la pubblicità vale solo per condanne definitive di frode, come già prevede il codice penale.
5. **Niente condoni e valutazione del Concordato preventivo biennale.** Prima di ogni rinnovo il Concordato (520.228 aderenti nel 2025) va valutato con un controfattuale indipendente, come chiede la stessa Relazione 2026 (nota 51). L'impegno "nessun condono" di 01-P3, art. 5, è condiviso. In edilizia esiste già la verifica della **congruità della manodopera**: si estende agli appalti di servizi e logistica, contro l'evasione contributiva.

**Varianti**

| Variante | Contenuto | Costo a regime (2027 / 2028 / 2029) | Intensità |
|---|---|---|---|
| PIENA | le cinque leve | 0,06 (0,05 / 0,08 / 0,08), RIALLOCAZIONE | 1 |
| ESSENZIALE | precompilata per le piccole partite IVA, rateazione automatica, riordino della riscossione; senza adempimento collaborativo semplificato né congruità estesa | 0,04 (0,03 / 0,05 / 0,05) | 0,6 |
| ZERO | solo norme a costo zero: rateazione automatica, sanzioni accessorie per recidivi, valutazione del Concordato, nessun condono | 0 | 0,3 |

**Articolato normativo essenziale** (disegno di legge, collegato alla manovra)

> **Art. 1 (Adempimento precompilato).** 1. L'Agenzia delle entrate mette a disposizione dei contribuenti in regime forfetario e in contabilità semplificata i registri, le liquidazioni periodiche e la dichiarazione IVA e dei redditi elaborati sulla base delle fatture elettroniche e dei corrispettivi telematici. 2. Se il contribuente accetta i dati senza modifiche, non si applicano sanzioni per errori imputabili ai dati messi a disposizione e il controllo formale è escluso.
>
> **Art. 2 (Adempimento collaborativo semplificato).** 1. Le imprese con ricavi superiori a 20 milioni di euro e inferiori alla soglia di accesso al regime di cui al decreto legislativo 5 agosto 2015, n. 128, possono aderire a un regime semplificato previa certificazione del sistema di controllo del rischio fiscale da parte di un soggetto professionale abilitato. Il regime prevede risposte entro novanta giorni e la riduzione delle sanzioni.
>
> **Art. 3 (Riscossione).** 1. Le somme dovute a seguito di controllo automatizzato o di accertamento definitivo possono essere rateizzate, su richiesta telematica e senza istruttoria, fino all'importo stabilito con decreto del Ministro dell'economia e delle finanze, con addebito diretto. 2. Si provvede al discarico dei crediti di difficile esazione secondo i criteri della Commissione tecnica per il riordino della riscossione. L'agente della riscossione pubblica ogni anno gli indicatori di riscossione per anzianità del credito.
>
> **Art. 4 (Sanzioni).** 1. All'articolo 12 del decreto legislativo 18 dicembre 1997, n. 471, la sospensione dell'attività per mancata emissione del documento commerciale si applica alla seconda violazione accertata nel quinquennio. 2. Restano ferme le riduzioni previste dal decreto legislativo 14 giugno 2024, n. 87, per le violazioni regolarizzate spontaneamente.
>
> **Art. 5 (Congruità della manodopera).** 1. La verifica di congruità dell'incidenza della manodopera prevista per il settore edile è estesa, con decreto del Ministro del lavoro e delle politiche sociali sentite le parti sociali, agli appalti di servizi di logistica, pulizia e vigilanza di importo superiore a 150.000 euro.
>
> **Art. 6 (Valutazioni e trasparenza).** 1. Il rinnovo del concordato preventivo biennale è subordinato a una valutazione controfattuale del suo effetto sul gettito, pubblicata dal Dipartimento delle finanze. 2. Fino al termine della legislatura non sono introdotte definizioni agevolate dei carichi affidati all'agente della riscossione.
>
> **Art. 7 (Copertura).** 1. Agli oneri, pari a 50 milioni di euro per il 2027, a 80 milioni per ciascuno degli anni 2028 e 2029 e a 60 milioni a decorrere dal 2030, si provvede mediante riduzione delle spese di funzionamento delle agenzie fiscali, con esclusione delle spese per il personale. Le maggiori entrate non sono utilizzate a copertura di nuove spese.

**Cronoprogramma**
- *Primi 100 giorni:* ddl collegato; piano Sogei-AdE per la precompilata delle piccole partite IVA, a partire dalle bozze già disponibili; atto di indirizzo ad AdER sulla priorità ai crediti recuperabili.
- *Entro 12 mesi:* rateazione automatica online; avvio del discarico; decreto sulla congruità nei servizi; avvio della valutazione del Concordato.
- *Entro fine legislatura:* precompilata per tutti i regimi forfettari e semplificati; adempimento collaborativo semplificato operativo; misura della quota di mancati versamenti nella Relazione evasione.

**Indicatori**

| KPI | Base (dato, anno, fonte) | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Quota dei mancati versamenti sul tax gap | circa 17%, 2023 (Relazione 2026) | ≤ 16% | ≤ 15% (livello del 2019) |
| Imprese in adempimento collaborativo (ordinario + semplificato) | 221, 2025 (Relazione 2026) | ≥ 600 | ≥ 1.500 |
| Piccole partite IVA che usano la precompilata | da rilevare, 2026 (AdE) | ≥ 30% | ≥ 60% |
| Riscossione entro 2 anni dall'accertamento definitivo | da rilevare, 2026 (AdER) | pubblicato | +20% sulla base |
| Nuovi condoni o definizioni agevolate | — | 0 | 0 |

**Rischi e garanzie**
- *La precompilata sposta errori e responsabilità sul fisco.* È voluto: è la contropartita della tracciabilità. La clausola che esclude le sanzioni vale solo se i dati sono accettati senza modifiche.
- *Il discarico percepito come condono.* Riguarda solo crediti già inesigibili (soggetti falliti, deceduti o nullatenenti) secondo criteri tecnici pubblici: non cancella debiti di chi può pagare.
- *Adempimento collaborativo che diventa trattamento di favore.* L'accesso è condizionato a un controllo certificato e revocabile, e le adesioni sono pubbliche nel numero e nei risultati aggregati.
- *Pressione sulle micro-imprese in crisi di liquidità.* La rateazione automatica distingue chi non può pagare da chi non vuole. Le sanzioni piene si applicano solo a frode e recidiva (proporzionalità, valore EQU).
- *Gettito.* 0,8-2,0 mld a regime (stima GovernAI: riduzione del 5-10% dei circa 17 mld di mancati versamenti più effetti di semplificazione). Una parte è temporanea (recupero di stock) e non si somma al gettito di 01-P3 per la quota IVA.

---

## Integrazioni proposte a 01-P3 (da recepire dall'agente area 01, senza duplicare la misura)

1. **Frodi carosello intra-UE.** Partecipazione piena all'analisi di rete Eurofisc (*Transaction Network Analysis*) e uso dei dati CESOP sui pagamenti transfrontalieri. Protocollo GdF-AdE-Procura europea (EPPO) per le frodi IVA transfrontaliere sopra 10 mln, di sua competenza. Preparazione della rendicontazione digitale intra-UE di ViDA dal 1/7/2030.
2. **Lo Statuto delle garanzie di 01-P10, art. 3**, si applica anche al sistema di analisi del rischio IVA di 01-P3: registro dei modelli, test di distorsione, comitato di audit unico.
3. **Indicatore unico.** Il gap IVA di 01-P3 e la propensione IVA di 01-P11 vanno monitorati insieme, per evitare di contare due volte lo stesso recupero.

## Nota per il coordinatore

- Il gettito di queste schede (2,3-5,5 mld a regime per il pacchetto raccomandato, più 5,2-6,9 mld di 01-P3) **non è una copertura**. Va al deficit. Il fondo IVA_EVASIONE e un eventuale analogo per le imposte dirette si alimentano solo dopo la certificazione nella Relazione annuale, che arriva con 2-3 anni di ritardo statistico. Le maggiori entrate da contrasto all'evasione sono già in parte usate dal DDL 2027 e per legge affluiscono al fondo per la riduzione della pressione fiscale (`registro/fondi.csv`): serve una regola esplicita su quale quota sia davvero nuova.
- **Conflitti.** Con *Giustizia e Garante* (SIC): lo Statuto va concordato prima del ddl. Con *Lavoro* (01-P12, congruità): servono le parti sociali. Con *Economia* (01-P2): la detrazione di 01-P11 è una nuova spesa fiscale, quindi è soggetta a scadenza e valutazione. Con il *DDL bilancio 2027*: un'eventuale nuova definizione agevolata confligge con 01-P3, art. 5, e con 01-P12, art. 6.
- **Dati da verificare prima dell'uso pubblico:** costo consuntivo del cashback; partecipazione e costi della lotteria degli scontrini (ADM); soglie vigenti dell'adempimento collaborativo; estremi dei provvedimenti del Garante sulla fatturazione elettronica (2018-2019); stato del redditometro (DM 7/5/2024).

---

*Schede aggiunte il 16 novembre 2026: ricerca su fonti ufficiali, tre valutatori indipendenti, verifica giuridica e scelte di chi guida il progetto. Fonti e modifiche: `benchmark/bozza_proposte_equita_fiscale.md`.*

---

## 01-P19 — Holding personali: sugli utili parcheggiati la stessa imposta che possedendo direttamente

**Problema in un dato.** Un dividendo incassato da una persona paga il **26%**. Incassato dalla sua holding paga l'**1,2%** (95% escluso, 5% all'IRES del 24%; artt. 87 e 89 TUIR). Sull'utile di un'impresa il prelievo complessivo è **43,8%** se il socio è una persona e **24,9%** se è una holding, finché la holding non distribuisce (calcolo nella diagnosi, par. 4.3). Si può non distribuire mai: alla morte del socio, in caso di liquidazione o recesso, il costo delle quote rivalutato in successione (art. 68 c. 6 TUIR) cancella l'imposta rinviata. Nessuna fonte ufficiale dice quanto valga questo canale. La clausola anti-abuso (art. 10-bis L. 212/2000) colpisce il rinvio solo se "sine die" e va provato caso per caso (atto di indirizzo MEF 27/2/2025): poca certezza per chi è in buona fede, poco effetto su chi pianifica.

**Evidenze.**
- Gli studi sui conti distributivi trovano un sistema regressivo sopra il 93°-95° percentile; il top 0,1% paga in media il 32,6-36% (Dalle Luche et al. 2026; Guzzardi et al. 2024; dati 2015). La causa principale è il reddito da capitale tassato poco o in ritardo.
- EU Tax Observatory (*Global Tax Evasion Report 2024*): le holding personali sono il canale principale con cui i miliardari pagano lo 0-0,5% del patrimonio.
- La Francia ha visto la sua imposta minima del 20% rendere 0,4 mld invece di 1,9 anche perché i dividendi sono rimasti nelle società; nel 2026 ha aggiunto una tassa sulle holding patrimoniali (art. 235 ter C CGI).
- Gli Stati Uniti tassano al **20%** gli utili passivi non distribuiti delle *personal holding companies* (IRC §541), definite in modo oggettivo: 5 persone o meno con più della metà, almeno il 60% di redditi passivi. Il Regno Unito tassa i prestiti delle società chiuse ai soci (s. 455 CTA 2010, 33,75%, restituito alla chiusura del prestito).

**Soluzione (PIENA).**
1. **Chi è dentro.** È "holding personale passiva" una società o un ente commerciale che, nello stesso anno:
   - è controllata (più del 50% dei voti o degli utili, anche indirettamente) da **non più di 5 persone fisiche**, con i familiari fino al terzo grado contati come una persona;
   - ha almeno il **60%** dei proventi da fonti passive: dividendi di portafoglio, interessi, plusvalenze su partecipazioni e titoli, canoni di immobili non strumentali, royalty non legate a un'attività. **Non contano come passivi i dividendi delle partecipazioni di almeno il 10% in società che esercitano un'attività d'impresa effettiva** (italiane o estere): una holding che guida un gruppo operativo non è passiva;
   - ha un attivo passivo netto oltre **2 mln €**.
2. **Cosa paga, e da quando.** Sulla quota esclusa (95%) dei dividendi e delle plusvalenze PEX **incassati dal periodo d'imposta successivo all'entrata in vigore**, che non è distribuita ai soci entro 12 mesi dalla chiusura dell'esercizio né reinvestita, la holding versa un'imposta sostitutiva del **26%**: lo stesso prelievo che il socio avrebbe pagato possedendo direttamente. **Le riserve già formate prima della legge non si tassano mai**, nemmeno se restano nella holding.
3. **Cosa resta fuori dalla base.**
   - i dividendi delle partecipazioni di almeno il 10% in società operative (gli utili che restano nell'impresa sono già protetti; tassarli nella holding li penalizzerebbe solo perché passano di livello);
   - i dividendi coperti dalla **direttiva madre-figlia** (2011/96/UE), anche negli anni dopo l'incasso, salvo costruzioni non genuine (art. 1 parr. 2-3 della direttiva);
   - per parità, i dividendi da partecipazioni di almeno il 10% in società italiane che sono a loro volta holding soggette a questa imposta (niente doppia imposta nelle catene).
4. **Niente doppia imposta.** Le riserve già tassate con questa imposta sono distribuite in esenzione. **Il beneficio segue le quote**: in caso di vendita, donazione o successione lo ha chi possiede le quote al momento della distribuzione o della liquidazione.
5. **Reinvestimenti esclusi (protezione delle PMI).** Non entrano nella base gli importi che la holding, entro 3 anni, reinveste in: capitale o finanziamenti di società operative controllate o collegate (≥20%); sottoscrizione di nuove azioni di PMI non quotate o quote di fondi EuVECA, **nei limiti dell'art. 21 del regolamento generale di esenzione per categoria** (aiuti al finanziamento del rischio, o il regolamento che lo sostituisce); beni strumentali. Se il reinvestimento non avviene, l'imposta si paga con interessi legali.
6. **Riserva per acquisizioni e crisi.** La holding può vincolare, dichiarandolo, fino al **30% dell'attivo passivo** (massimo 20 mln €) in una riserva per: acquistare il controllo o almeno il 20% di società operative; ricapitalizzare o finanziare società controllate in perdita o in crisi (Codice della crisi d'impresa). La riserva non paga finché è usata entro **5 anni**; altrimenti l'imposta si paga con interessi legali.
7. **Franchigia.** I primi **100.000 €** l'anno di proventi esclusi trattenuti non pagano.
8. **Prestiti e beni ai soci.** Prestiti, garanzie e beni messi a disposizione dei soci o dei loro familiari si **presumono** distribuzione e pagano il 26%, salvo restituzione entro 12 mesi, interessi e corrispettivi di mercato o **altra prova contraria**. Se lo stesso beneficio è già tassato al socio come reddito diverso (art. 67 c. 1 lett. h-ter TUIR), non si paga due volte.
9. **Liquidazione e recesso.** Le riserve formate **dopo l'entrata in vigore** con proventi esclusi e non tassati restano tassabili come dividendo anche se le quote sono state rivalutate in successione; vale solo per le **successioni aperte dopo** l'entrata in vigore.
10. **Holding estere.** Per le holding passive non residenti controllate da residenti si applica la stessa regola, imputando al socio sul modello dell'art. 167 TUIR, con **la stessa base, la stessa franchigia, gli stessi reinvestimenti esclusi e la stessa riserva** della regola interna, e con l'**esimente dell'attività economica effettiva sempre disponibile** (art. 167 c. 5 TUIR; obbligatoria per UE e SEE: art. 7 par. 2 lett. a ATAD, *Cadbury Schweppes* C-196/04).
11. **Exit tax minima, solo sulle holding passive.** Chi trasferisce la residenza all'estero e possiede, anche indirettamente, quote di una holding personale passiva per un valore oltre **1 mln €** paga il 26% sulla parte di plusvalenza latente che corrisponde alle **riserve formate dopo l'entrata in vigore con proventi esclusi non ancora tassati** (franchigia, reinvestimenti, riserva). Nessuna exit tax sulle riserve pregresse né sulle altre partecipazioni. Verso UE, SEE e Svizzera la riscossione è **sospesa senza interessi e senza garanzie** fino alla vendita o alla distribuzione, e le minusvalenze successive non riconosciute dallo Stato di arrivo riducono l'imposta (CGUE C-9/02, C-470/04, C-581/17 *Wächtler*); verso gli altri Paesi si paga in 5 rate annuali. Vale solo per i trasferimenti successivi all'entrata in vigore.
12. **Antiabuso con interpello.** Clausola antiabuso specifica (soglie calcolate per gruppo familiare; holding "operative di facciata") con interpello preventivo per chi è in dubbio.

**Varianti**

| Variante | Contenuto | Costo di attuazione 2027 / 2028 / 2029 / regime | Intensità | Copertura |
|---|---|---|---|---|
| PIENA | Punti 1-12; soglia 2 mln, franchigia 100.000 €, imposta 26% sulla quota esclusa trattenuta | 0,005 / 0,011 / 0,011 / **0,011** (2028) | 1 | FN05 + FN06 |
| ESSENZIALE | Solo holding residenti; soglia 5 mln, franchigia 250.000 €; imposta del **13%** come acconto, scomputato alla distribuzione; il credito d'acconto **segue le quote** (vendita, donazione, successione), non è rimborsabile se la riserva non è mai distribuita ma si usa in liquidazione; punti 1-3, 5, 6, 8, 9, 11, 12 | 0,004 / 0,007 / 0,007 / **0,007** | 0,6 | FN05 |
| ZERO | Solo trasparenza: prospetto in dichiarazione per le holding personali passive sopra le soglie (attivo passivo, proventi esclusi, utili trattenuti, prestiti ai soci); relazione annuale del Dipartimento delle Finanze con dati solo aggregati; nessun prelievo | 0 | 0,15 | nessuna |

Motivazione delle intensità: la ESSENZIALE dimezza il vantaggio del rinvio e chiude prestiti ai soci, rivalutazione in successione e fuga di residenza, ma lascia fuori le holding tra 2 e 5 mln e quelle estere. Non c'è una variante PILOTA: un'imposta non si sperimenta su un campione senza violare l'art. 3 Cost. Il costo cresce di 0,001 rispetto alla prima bozza per l'exit tax e il controllo della riserva.

**Articolato normativo essenziale** (legge di bilancio o disegno di legge collegato; nuovo articolo nel testo unico delle imposte sui redditi, d.lgs. 117/2026, numerazione da verificare)

> **Art. 1 (Holding personali passive).** 1. Ai fini del presente articolo è holding personale passiva la società o l'ente commerciale residente che nel periodo d'imposta: a) è controllato, ai sensi dell'articolo 2359, primo comma, numero 1), del codice civile, anche indirettamente, da non più di cinque persone fisiche, considerando come una sola persona il coniuge, i parenti entro il terzo grado e gli affini entro il secondo; b) ha conseguito proventi passivi, come definiti dal comma 2, pari almeno al 60 per cento dei proventi complessivi; c) ha un attivo passivo netto superiore a 2 milioni di euro.
> 2. Sono proventi passivi gli utili e le plusvalenze su partecipazioni e titoli, gli interessi, i canoni di immobili non strumentali e i canoni per l'uso di beni immateriali non connessi a un'attività d'impresa effettiva. Non sono proventi passivi gli utili derivanti da partecipazioni non inferiori al 10 per cento in società, residenti o non residenti, che esercitano un'attività d'impresa effettiva.
>
> **Art. 2 (Imposta sugli utili esclusi trattenuti).** 1. Sulla quota degli utili e delle plusvalenze esclusa dal reddito ai sensi degli articoli 87 e 89 del TUIR, conseguiti a decorrere dal periodo d'imposta successivo a quello in corso alla data di entrata in vigore della presente legge, al netto della franchigia di 100.000 euro, che non sia distribuita ai soci entro dodici mesi dalla chiusura del periodo d'imposta né reinvestita o accantonata ai sensi dell'articolo 3, la holding personale passiva versa un'imposta sostitutiva del 26 per cento. Le riserve formate con utili conseguiti in periodi precedenti non sono in alcun caso soggette all'imposta.
> 2. Le riserve formate con utili assoggettati all'imposta di cui al comma 1 non concorrono a formare il reddito di chi possiede le partecipazioni al momento della distribuzione o della liquidazione.
> 3. Sono esclusi dalla base del comma 1, anche nei periodi d'imposta successivi a quello di percezione: a) gli utili derivanti da partecipazioni non inferiori al 10 per cento in società che esercitano un'attività d'impresa effettiva; b) gli utili percepiti da società di altri Stati membri dell'Unione europea che rientrano nell'ambito della direttiva 2011/96/UE, salvo che ricorrano le condizioni dell'articolo 1, paragrafi 2 e 3, della stessa direttiva; c) gli utili derivanti da partecipazioni non inferiori al 10 per cento in holding personali passive soggette all'imposta di cui al comma 1.
>
> **Art. 3 (Reinvestimento produttivo e riserva per acquisizioni e crisi).** 1. Non concorrono alla base di cui all'articolo 2 gli importi investiti, entro i tre periodi d'imposta successivi, in conferimenti o finanziamenti a società che esercitano un'attività d'impresa effettiva e sono controllate o collegate ai sensi dell'articolo 2359 del codice civile, in beni strumentali e, nei limiti dell'articolo 21 del regolamento (UE) n. 651/2014 o della disciplina che lo sostituisce, nella sottoscrizione di azioni o quote di nuova emissione di piccole e medie imprese non quotate o di fondi europei per il venture capital. 2. Non concorrono altresì alla base, fino al 30 per cento dell'attivo passivo netto e comunque fino a 20 milioni di euro, gli importi iscritti in una riserva vincolata all'acquisto del controllo o di partecipazioni non inferiori al 20 per cento in società che esercitano un'attività d'impresa effettiva, o al finanziamento e alla ricapitalizzazione di società controllate in perdita o in stato di crisi, utilizzata entro i cinque periodi d'imposta successivi. 3. In mancanza del reinvestimento o dell'utilizzo della riserva nei termini, l'imposta è dovuta con gli interessi legali.
>
> **Art. 4 (Prestiti e beni ai soci).** 1. I finanziamenti, le garanzie e i beni concessi in uso dalla holding personale passiva ai soci o ai loro familiari si presumono utili distribuiti, salvo restituzione entro dodici mesi, corrispettivo di mercato o altra prova contraria. 2. La presunzione non si applica per la parte di beneficio già tassata ai sensi dell'articolo 67, comma 1, lettera h-ter), del TUIR.
>
> **Art. 5 (Liquidazione e recesso).** 1. Nei casi di cui all'articolo 47, comma 7, del TUIR, la parte delle somme corrispondente a riserve formate, a decorrere dal periodo d'imposta di cui all'articolo 2, comma 1, con utili e plusvalenze esclusi e non assoggettati all'imposta di cui all'articolo 2, costituisce utile, senza tenere conto della determinazione del costo ai sensi dell'articolo 68, comma 6, del TUIR. 2. Il comma 1 si applica alle partecipazioni acquisite per successioni aperte dopo la data di entrata in vigore della presente legge.
>
> **Art. 6 (Soggetti non residenti).** 1. Ai soggetti non residenti che possiedono i requisiti dell'articolo 1 e sono controllati da persone fisiche residenti si applica l'articolo 167 del TUIR, anche in deroga alle condizioni di tassazione effettiva del comma 4, lettera a), con la stessa decorrenza, base, franchigia, esclusioni, reinvestimenti e riserva previsti dagli articoli 2 e 3. 2. Resta sempre ferma l'esimente del comma 5 dell'articolo 167 del TUIR.
>
> **Art. 7 (Trasferimento della residenza).** 1. Le persone fisiche che trasferiscono la residenza fiscale all'estero dopo la data di entrata in vigore della presente legge e possiedono, anche indirettamente, partecipazioni in holding personali passive di valore superiore a 1 milione di euro realizzano, alla data del trasferimento, la plusvalenza corrispondente alle riserve formate ai sensi dell'articolo 2, comma 1, con utili e plusvalenze esclusi non assoggettati all'imposta. 2. In caso di trasferimento in uno Stato dell'Unione europea, dello Spazio economico europeo con adeguato scambio di informazioni o nella Confederazione svizzera, la riscossione è sospesa, senza interessi e senza garanzie, fino al realizzo o alla distribuzione; le minusvalenze successive non riconosciute dallo Stato di destinazione riducono l'imposta. Negli altri casi l'imposta è versata in cinque rate annuali.
>
> **Art. 8 (Antiabuso, decorrenza e valutazione).** 1. Le soglie dell'articolo 1 sono calcolate per gruppo familiare. Il contribuente può presentare interpello ai sensi dell'articolo 11 della legge 27 luglio 2000, n. 212. 2. Le disposizioni si applicano dal periodo d'imposta successivo a quello in corso alla data di entrata in vigore. 3. Entro tre anni il Dipartimento delle finanze pubblica una valutazione degli effetti su gettito, distribuzioni e investimenti, al netto delle minori entrate future dovute alla distribuzione in esenzione delle riserve tassate.

**Chi paga.** Le famiglie con patrimoni finanziari di diversi milioni tenuti in holding che, **dopo la legge**, incassano proventi passivi e non li reinvestono nell'economia produttiva. **Non paga** chi ha un'impresa operativa, chi riceve dividendi dalle proprie società operative, chi reinveste o accantona per acquisizioni e crisi, chi ha una piccola società di famiglia sotto le soglie, chi ha riserve formate prima della legge. Con la ESSENZIALE paga circa metà del vantaggio oggi goduto, come acconto restituito alla distribuzione.

**Costituzionalità.**
- **Art. 53.** L'imposta colpisce un reddito che la holding ha effettivamente incassato: la capacità contributiva c'è. L'imputazione al socio per le holding estere segue lo schema già in vigore dell'art. 167 TUIR.
- **Art. 3.** Elimina una disparità: due persone con lo stesso dividendo pagano oggi 26% o 1,2% a seconda del contenitore. Le soglie e la franchigia sono criteri oggettivi.
- **Art. 23.** Definizioni, aliquota, soglie, esclusioni e riserva sono fissate per legge.
- **Irretroattività e affidamento** (artt. 3 e 10 L. 212/2000): si applica solo ai proventi incassati dal periodo d'imposta successivo; mai alle riserve già formate; la regola su liquidazione e recesso vale solo per le successioni future; l'exit tax solo per i trasferimenti futuri e solo sulle riserve nuove.
- **Art. 41.** Le imprese operative, i loro dividendi, i reinvestimenti e la riserva per acquisizioni e crisi sono esclusi.

**Diritto UE.**
- **Direttiva madre-figlia (2011/96/UE).** La Corte di giustizia (C-68/15, *X*, 17/5/2017, sulla "fairness tax" belga) ha giudicato contraria alla direttiva un'imposta che colpiva oltre il 5% utili ricevuti da figlie UE e redistribuiti negli anni successivi. Per questo l'art. 2 c. 3 lett. b) esclude quei dividendi **anche negli anni dopo l'incasso**, salvo costruzioni non genuine.
- **Discriminazione alla rovescia** (art. 53 L. 234/2012). L'esclusione dei dividendi di tutte le partecipate operative di almeno il 10%, italiane ed estere (art. 2 c. 3 lett. a), e delle holding italiane già soggette all'imposta (lett. c), mette i dividendi italiani sullo stesso piano di quelli UE. **Resta da verificare con il Dipartimento per le politiche europee** il caso residuo delle partecipate italiane non operative e non soggette all'imposta.
- **Libertà di stabilimento e dei capitali (artt. 49 e 63 TFUE).** La regola estera non è più dura di quella interna: stessa base, franchigia, reinvestimenti e riserva; esimente dell'attività economica effettiva sempre disponibile.
- **Exit tax.** Sospensione senza interessi e garanzie verso UE, SEE e Svizzera e riconoscimento delle minusvalenze successive (C-9/02, C-470/04, C-581/17). L'art. 5 ATAD vale solo per le società: per le persone valgono i Trattati.
- **Aiuti di Stato.** L'esclusione per chi reinveste in PMI non quotate e fondi EuVECA è inquadrata nell'art. 21 del regolamento generale di esenzione (o nel successore dal 2027), con i suoi limiti; i reinvestimenti nelle controllate operative sono una misura generale.
- **ATAD** (2016/1164): fissa un minimo; una regola più severa è ammessa (art. 3).

**Rischi e mitigazioni.**
- **Fuga di residenza dei soci.** Ora coperta dall'exit tax minima del punto 11, interna a questa proposta. È volutamente stretta (solo holding passive, solo riserve nuove non tassate, sospensione in UE): **chi si trasferisce porta con sé senza imposta le riserve formate prima della legge e le altre partecipazioni**. È un rischio che resta e va misurato (KPI sotto).
- **Gettito che cresce piano.** Senza le riserve pregresse la base si forma solo con i proventi nuovi: primo versamento nel 2030 sui proventi del 2028, pieno dal 2031 (vedi FN05 e FN06).
- **Riorganizzazioni artificiali** (holding "operative di facciata", proventi spostati sotto soglia, partecipazioni portate al 10% per far rientrare i dividendi nell'esclusione). Soglie consolidate per gruppo familiare; l'esclusione richiede un'attività d'impresa effettiva della partecipata (stesso test dell'art. 167 c. 5); clausola antiabuso con interpello; prospetto in dichiarazione.
- **Holding che accantonano per acquisizioni o rilanci** (rilievo dei valutatori A e B). Riserva vincolata per 5 anni fino al 30% dell'attivo passivo; reinvestimenti anche in fondi EuVECA.
- **Costi di adempimento.** Un prospetto in più per qualche migliaio di società (numero **da verificare** con il DF); nessun adempimento per le altre.
- **Liquidità della holding per pagare l'imposta.** L'imposta colpisce utili incassati e non distribuiti: la liquidità c'è. In caso di reinvestimento mancato, rateazione automatica (01-P12).
- **Gettito in parte anticipato.** Le riserve tassate saranno distribuite in esenzione: le coperture contano solo la parte strutturale (FN05, FN06).

**Indicatori**

| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Holding personali passive censite e utili esclusi trattenuti | non pubblicato, 2026 (DF) | pubblicato ogni anno | pubblicato, con serie |
| Utili distribuiti dalle holding passive ai soci persone fisiche | da rilevare, 2027 | +20% sulla base | +30% |
| Reinvestimenti produttivi e riserve per acquisizioni e crisi dichiarati e usati | 0, 2027 | pubblicato | in crescita |
| Trasferimenti di residenza di soci di holding passive, con e senza exit tax | non rilevato | pubblicato | pubblicato, con valore delle riserve pregresse uscite |
| Aliquota effettiva del top 0,1% (statistica di 01-P23) | 32,6-36%, 2015 (stime accademiche) | prima misura ufficiale | +2/+4 punti |

---

## 01-P21 — Fine dei contenitori: polizze vita senza rischio e trust esteri opachi

**Problema in un dato.** Una polizza vita in cui l'assicuratore non corre quasi nessun rischio è, nei fatti, un portafoglio di investimenti. Eppure i rendimenti si tassano solo al riscatto e il capitale pagato in caso di morte è **escluso dall'imposta di successione** (art. 12 d.lgs. 346/1990). Il beneficiario lo acquista per diritto proprio (art. 1920 c.c.), quindi senza una norma espressa non è attivo ereditario. Le polizze "dedicate", in cui chi le stipula sceglie gli investimenti, spesso emesse all'estero, servono soprattutto a rinviare e a trasmettere. La Cassazione ha più volte riqualificato queste polizze come prodotti finanziari (estremi **da verificare**), ma caso per caso. Le distribuzioni dei **trust esteri opachi** ai beneficiari residenti sono tassate solo se il trust sta in un Paese a fiscalità privilegiata (DL 124/2019, art. 13; circ. AdE 34/E/2022). Il registro dei titolari effettivi è **sospeso** (diagnosi, par. 5).

**Evidenze.** La **Germania** concede il trattamento delle polizze vita solo se la copertura per il caso di morte supera di almeno il 10% il valore della polizza (§20 c. 1 n. 6 EStG, **da verificare** il testo vigente). L'**art. 167 TUIR** già confronta la tassazione estera con quella italiana per le società controllate: la stessa logica si può usare per i trust.

**Soluzione (PIENA).**
1. **Polizze senza rischio.** Una polizza conta come assicurazione solo se il capitale in caso di morte supera di almeno il **10%** il valore della polizza per tutta la durata. La soglia si cambia solo per legge. Altrimenti, **per i premi versati dal 1° gennaio 2028** (nei contratti nuovi e in quelli in corso, solo per la parte di valore che deriva dai premi nuovi):
   - una **norma espressa** stabilisce che il capitale, anche se acquistato dal beneficiario per diritto proprio, **fa parte dell'attivo ereditario** ai fini dell'imposta di successione, con le franchigie ordinarie (1 mln per figli e coniuge, o 500.000 € con SF14);
   - per le **polizze dedicate** (attivi scelti da chi stipula o gestione personalizzata) si tassano **ogni anno solo i redditi realizzati** dagli attivi sottostanti (interessi, dividendi, plusvalenze realizzate), come se fossero posseduti direttamente; al riscatto si scomputa quanto già pagato.
2. **Stesse regole per le compagnie estere** in libera prestazione di servizi, con oneri di adempimento non superiori a quelli delle compagnie italiane (l'intermediario o il contribuente applica l'imposta).
3. **Trust esteri opachi.** Le distribuzioni a beneficiari residenti sono tassate come redditi di capitale (26%) **solo per la parte che corrisponde a redditi** del trust, non per il patrimonio conferito, e **con credito per le imposte pagate all'estero dal trust**. Restano esenti se il reddito è stato tassato all'estero con un'aliquota effettiva almeno pari alla metà di quella italiana (stessa soglia dell'art. 167 TUIR).
4. **Registro dei titolari effettivi.** Il Governo adotta entro 90 giorni i decreti per la riapertura, almeno per trust e istituti affini, in modo conforme alla direttiva (UE) 2024/1640 e alla sentenza della Corte di giustizia del 21/5/2026 (C-684/24 e C-685/24, testo da leggere sulla fonte ufficiale prima di scrivere i decreti). L'accesso dell'amministrazione fiscale non dipende dal contenzioso sull'accesso dei terzi.

**Varianti**

| Variante | Contenuto | Costo di attuazione 2027 / 2028 / 2029 / regime | Intensità | Copertura |
|---|---|---|---|---|
| PIENA | Punti 1-4 | 0,002 / 0,004 / 0,004 / **0,004** (2028) | 1 | FN09 |
| ESSENZIALE | Punto 1 solo per la successione (senza tassazione annua delle polizze dedicate) e solo per premi complessivi oltre 1 mln € per persona, **calcolati su tutti i contratti del contraente, anche con compagnie diverse ed estere**; punti 2-4 | 0,001 / 0,002 / 0,002 / **0,002** | 0,5 | FN09 (circa metà) |
| ZERO | Punto 4 e segnalazione annuale, solo aggregata, di IVASS e AdE delle polizze senza rischio e delle polizze dedicate (numero, valore, compagnie estere); accesso dei terzi al registro solo con legittimo interesse | 0 | 0,15 | nessuna |

**Articolato normativo essenziale** (legge di bilancio; modifica del d.lgs. 346/1990, del TUIR e del d.P.R. 600/1973)

> **Art. 1 (Polizze senza rischio).** 1. Ai fini delle imposte sui redditi e dell'imposta sulle successioni non si considerano contratti di assicurazione sulla vita quelli nei quali il capitale dovuto in caso di morte non supera, in ogni momento della durata, del 10 per cento il valore di riscatto. La percentuale può essere modificata solo con legge. 2. Le disposizioni del comma 1 si applicano ai premi versati dal 1° gennaio 2028, anche nei contratti in corso a tale data, limitatamente alla parte del valore che deriva da tali premi. 3. Le somme dovute ai beneficiari in forza dei contratti di cui al comma 1, ancorché acquistate per diritto proprio ai sensi dell'articolo 1920 del codice civile, si considerano comprese nell'attivo ereditario ai fini dell'imposta sulle successioni. All'articolo 12 del d.lgs. 31 ottobre 1990, n. 346, la lettera c) non si applica a tali somme.
>
> **Art. 2 (Polizze dedicate).** 1. Per i contratti di cui all'articolo 1 nei quali il contraente sceglie gli attivi o ne determina la gestione, i redditi realizzati dagli attivi sottostanti sono tassati annualmente secondo le regole applicabili a tali attivi. Le imposte così versate sono scomputate da quelle dovute al riscatto o alla scadenza. 2. Le imprese di assicurazione non residenti applicano le stesse regole con obblighi non superiori a quelli delle imprese residenti.
>
> **Art. 3 (Distribuzioni di trust esteri).** 1. All'articolo 44, comma 1, lettera g-sexies), del TUIR, le parole relative agli Stati a fiscalità privilegiata sono sostituite dal riferimento ai redditi che hanno scontato all'estero una tassazione effettiva inferiore alla metà di quella applicabile in Italia. 2. Le distribuzioni sono tassate per la sola parte riferibile a redditi del trust, con esclusione del patrimonio conferito; dall'imposta si detraggono le imposte pagate all'estero dal trust sugli stessi redditi.

**Chi paga.** Chi usa polizze senza rischio per patrimoni oltre le franchigie di successione (solo per i premi versati dal 2028), chi ha polizze dedicate, i beneficiari di trust esteri poco tassati. Le polizze **di vera protezione** (caso morte, non autosufficienza, previdenza) **non cambiano**; i premi già versati non cambiano.

**Costituzionalità e diritto UE.**
- **Art. 3 e 53.** Si tassa la sostanza (un investimento) e non la forma; i premi già versati restano con le regole di oggi (affidamento). Tassare solo i redditi realizzati evita di colpire guadagni solo potenziali.
- **Art. 23.** La soglia del 10% è nella legge e si cambia solo per legge.
- **Libera prestazione dei servizi (art. 56 TFUE).** Regole e oneri identici per compagnie italiane ed estere.
- **Trust.** La soglia della metà dell'aliquota italiana segue la logica, già accettata, dell'art. 167 TUIR e della direttiva ATAD; il credito per l'imposta estera evita la doppia imposta.

**Rischi e mitigazioni.**
- **Contratti con il 10% di copertura costruiti al limite.** Il costo della copertura è reale e riduce il vantaggio.
- **Effetto sul settore assicurativo.** Riguarda una nicchia (polizze di investimento per grandi patrimoni). La previdenza e la protezione restano invariate.
- **Gettito lento e in parte anticipato.** Solo premi nuovi; la tassazione annua anticipa imposte oggi pagate al riscatto: FN09 conta solo la parte netta.

**Indicatori**

| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Valore delle polizze senza rischio e dedicate, per emittente italiano o estero | non pubblicato, 2026 | pubblicato da IVASS e AdE | serie |
| Trust registrati nel registro dei titolari effettivi | registro sospeso, 2026 | registro operativo | completezza verificata |
| Gettito dalle polizze in successione | 0 | ≥ minimo FN09 | stabile |

---

## 01-P22 — Eredità: l'impresa che lavora resta esente, il patrimonio passivo no

**Problema in un dato.** L'imposta di successione ha reso **1,08 mld** nel 2025. Il passaggio a figli e coniuge delle partecipazioni di controllo è **esente** se il controllo resta 5 anni (art. 3 c. 4-ter TUS), anche quando la società è una holding con un patrimonio solo finanziario o immobiliare (risposta AdE n. 152/2026). E gli eredi ricevono le partecipazioni al valore di successione (art. 68 c. 6 TUIR): le plusvalenze maturate in vita **non si pagano mai**. Chi lascia un'impresa e chi lascia una cassaforte di titoli è trattato allo stesso modo; chi lascia titoli senza holding paga.

**Evidenze.** La **Germania** esclude dalle agevolazioni per le imprese gli attivi passivi (*Verwaltungsvermögen*: liquidità oltre una quota, titoli, immobili dati in affitto) (§13b ErbStG); la quota di liquidità tollerata è intorno al 15% del valore dell'impresa (**da verificare** il testo vigente). La Corte costituzionale tedesca (BVerfG, 1 BvL 21/12, 17/12/2014) ha giudicato **contrarie all'uguaglianza** agevolazioni troppo larghe per i grandi patrimoni. In Germania gli eredi mantengono il costo fiscale del defunto per le partecipazioni.

**Soluzione (PIENA).**
1. **L'esenzione del passaggio d'impresa resta** (anche con SF14), ma solo per la parte del valore riferibile ad **attività operative**. La parte riferibile ad **attivi passivi**, calcolata in modo consolidato sul gruppo, entra nella base imponibile con le franchigie ordinarie. **I criteri sono scritti nella legge** (il decreto fissa solo i metodi tecnici di calcolo). Sono attivi passivi:
   - la **liquidità netta** (cassa, depositi e titoli a breve meno i debiti finanziari a breve) **solo per la parte che supera il maggiore tra il 20% dell'attivo e un anno di costi operativi** (personale, acquisti, affitti);
   - titoli e strumenti finanziari non usati nell'attività (esclusi crediti commerciali e coperture dei rischi);
   - partecipazioni sotto il 10% e partecipazioni in società a loro volta prevalentemente passive;
   - immobili dati in locazione a terzi, salvo che la locazione sia l'attività principale svolta con una propria organizzazione (dipendenti e mezzi);
   - beni di lusso non usati nell'attività (opere d'arte, gioielli, imbarcazioni, aerei, auto da collezione).
2. **Perché il 20% e non il 10%.** I tre valutatori hanno osservato che una soglia del 10% colpisce le PMI che tengono liquidità per prudenza: stagionalità, crediti lenti della PA, crisi come quella del 2020. Una PMI prudente può avere il 15-20% dell'attivo in liquidità senza essere una cassaforte; una holding di patrimonio ne ha in genere ben oltre la metà. Il criterio alternativo di "un anno di costi" protegge le imprese con molto personale e poco attivo. Il confronto con la liquidità **netta** dai debiti evita di colpire chi ha liquidità perché ha appena preso un prestito. La soglia tedesca è più bassa (circa 15%, da verificare): la scelta italiana è volutamente più prudente.
3. **Pagamento in 10 rate annuali** senza interessi per la parte passiva, per non costringere a vendere. Le rate decadono **solo se l'impresa è ceduta** prima della fine.
4. **Società UE e SEE.** L'esenzione per gli attivi operativi vale anche per le partecipazioni di controllo in società UE e SEE, con gli stessi criteri e lo stesso calcolo consolidato per controllate italiane ed estere (art. 63 TFUE; oggi l'esenzione sembra limitata alle società residenti, **da verificare**).
5. **Costo fiscale degli eredi.** Per partecipazioni e titoli, gli eredi mantengono il costo del defunto per la parte di plusvalenze latenti oltre **1 mln €** per erede. Nessuna imposta alla morte: si paga solo quando l'erede vende. Per non tassare due volte la stessa ricchezza, dall'imposta sulla plusvalenza si detrae, come **credito**, l'imposta di successione pagata sulla stessa partecipazione per la parte di valore che corrisponde alla plusvalenza.
6. **Meno effetto blocco sulle vendite** (rilievo dei valutatori A, B e C). Il blocco nasce dal timore di pagare vendendo. Per attenuarlo: a) l'imposta sulla plusvalenza ereditata si paga in **5 rate annuali** senza interessi quando l'erede vende il controllo di un'impresa operativa a terzi; b) l'erede può in ogni momento **rideterminare** il costo con il regime ordinario di rivalutazione, pagando in 3 rate; c) il credito per l'imposta di successione riduce il costo della vendita. C'è anche un effetto opposto: oggi chi è anziano ha un forte motivo per **non** vendere mai, perché alla morte la plusvalenza sparisce; con il costo mantenuto quel motivo si riduce.
7. **Solo per il futuro.** Le regole valgono per le successioni aperte e le donazioni fatte dopo l'entrata in vigore.

**Varianti**

| Variante | Contenuto | Costo di attuazione 2027 / 2028 / 2029 / regime | Intensità | Copertura |
|---|---|---|---|---|
| PIENA | Punti 1-7 | 0,001 / 0,003 / 0,003 / **0,003** (2028) | 1 | FN10 (punto 1); il gettito del punto 5 arriva dopo il 2030 e non è contato |
| ESSENZIALE | Punti 1-4 e 7, solo per le società con attivi passivi (calcolati come al punto 1) oltre il **50%** dell'attivo (holding prevalentemente passive); nessun cambio sul costo fiscale degli eredi | 0,001 / 0,002 / 0,002 / **0,002** | 0,5 | FN10 (circa metà) |
| ZERO | Statistica DF sulle esenzioni art. 3 c. 4-ter (numero, valore, quota passiva) e sulle plusvalenze latenti rivalutate in successione, pubblicata solo in forma aggregata con soglie di riservatezza statistica | 0 | 0,1 | nessuna |

**Articolato normativo essenziale** (legge di bilancio; modifica del d.lgs. 346/1990 e dell'art. 68 TUIR)

> **Art. 1 (Esenzione dei trasferimenti d'impresa).** 1. All'articolo 3, comma 4-ter, del d.lgs. 31 ottobre 1990, n. 346, sono aggiunti, in fine, i seguenti periodi: «L'esenzione si applica anche alle partecipazioni di controllo in società residenti in altri Stati dell'Unione europea o dello Spazio economico europeo. L'esenzione non si applica alla parte del valore delle quote e delle azioni riferibile ad attivi passivi, determinata su base consolidata con gli stessi criteri per le società controllate residenti e non residenti. Sono attivi passivi: a) le disponibilità liquide e gli strumenti finanziari a breve termine, al netto dei debiti finanziari a breve termine, per la parte che eccede il maggiore tra il 20 per cento dell'attivo e l'ammontare dei costi operativi dell'ultimo esercizio; b) i titoli e gli strumenti finanziari non utilizzati nell'attività d'impresa, esclusi i crediti commerciali e gli strumenti di copertura; c) le partecipazioni inferiori al 10 per cento e quelle in società i cui attivi sono costituiti per più della metà da attivi passivi; d) gli immobili locati a terzi, salvo che la locazione costituisca l'attività principale esercitata con un'organizzazione propria; e) le opere d'arte, i gioielli, le imbarcazioni, gli aeromobili e i veicoli da collezione non utilizzati nell'attività. Con decreto del Ministro dell'economia e delle finanze sono stabiliti i soli metodi tecnici di valutazione.» 2. L'imposta relativa può essere versata in dieci rate annuali senza interessi; il beneficio decade solo in caso di cessione dell'impresa prima del pagamento dell'ultima rata. 3. Le disposizioni si applicano alle successioni aperte e alle donazioni fatte dopo la data di entrata in vigore della presente legge.
>
> **Art. 2 (Costo fiscale degli eredi).** 1. All'articolo 68, comma 6, del TUIR, per le partecipazioni e i titoli acquisiti per successioni aperte dopo la data di entrata in vigore della presente legge, il costo è pari al costo riconosciuto al defunto aumentato di 1.000.000 di euro per ciascun erede, entro il limite del valore definito ai fini dell'imposta di successione. 2. Dall'imposta dovuta sulla plusvalenza si detrae l'imposta di successione riferibile alla parte di valore della stessa partecipazione che corrisponde alla plusvalenza. 3. In caso di cessione a terzi del controllo di una società che esercita un'attività d'impresa effettiva, l'imposta sulla plusvalenza può essere versata in cinque rate annuali senza interessi. Resta ferma la facoltà di rideterminare il costo secondo il regime ordinario, con pagamento in tre rate.

**Chi paga.** Gli eredi di patrimoni passivi grandi tenuti in holding, dopo la legge; gli eredi di grandi plusvalenze latenti, solo quando vendono e al netto dell'imposta di successione già pagata. **Non paga** chi eredita un'impresa operativa e la continua, anche se tiene una liquidità prudente; non paga chi eredita patrimoni sotto le franchigie.

**Rapporto con SF14.** SF14 riduce le franchigie e alza le aliquote, ma "conferma l'esenzione per aziende familiari che proseguono l'attività". 01-P22 restringe quella esenzione agli attivi operativi. Se SF14 è attiva, il gettito di FN10 è più alto (aliquote 4-7% e franchigia 500.000 €): la stima di FN10 usa le **regole vigenti**, quindi non c'è doppio conteggio.

**Costituzionalità e diritto UE.**
- **Art. 3 e 53.** Il trattamento diverso tra impresa e patrimonio passivo ha una ragione (continuità produttiva), come riconosciuto dalla Corte tedesca; oggi il beneficio va anche dove la ragione manca.
- **Art. 23.** I criteri degli attivi passivi sono nella legge; il decreto fissa solo i metodi tecnici.
- **Doppia imposizione.** Imposta di successione e imposta sulla plusvalenza sono imposte diverse, ma il credito evita di colpire due volte la stessa ricchezza.
- **Art. 42 c. 4** (successione): la legge stabilisce i limiti; nessun problema.
- **Libera circolazione dei capitali (art. 63 TFUE).** Esenzione estesa alle società UE e SEE; calcolo consolidato identico per controllate italiane ed estere.

**Rischi e mitigazioni.**
- **Classificazione degli attivi.** Criteri nella legge; liquidità contata al netto dei debiti e solo oltre una soglia alta.
- **Liquidità degli eredi.** Rate decennali che decadono solo se l'impresa è ceduta; nessuna imposta sulle plusvalenze alla morte.
- **Effetto blocco sulle vendite.** Rate in 5 anni per chi vende il controllo, rideterminazione sempre possibile, credito per l'imposta di successione.
- **Donazioni anticipate per evitare la regola.** La stessa disciplina si applica alle donazioni (art. 3 c. 4-ter vale per entrambe).
- **Gettito lento.** Solo successioni future e rate decennali: il gettito pieno arriva dopo il 2035; FN10 conta solo il livello raggiunto nel 2032.

**Indicatori**

| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Valore delle esenzioni art. 3 c. 4-ter, quota passiva | non pubblicato, 2026 | pubblicato | serie |
| Gettito successioni e donazioni | 1,08 mld, 2025 (Bollettino n. 286) | +2-5% (senza SF14) | +4-10% |
| Imprese familiari passate di generazione e ancora attive dopo 5 anni | da rilevare (DF, Registro imprese) | invariato o in crescita | invariato o in crescita |
| Cessioni di imprese operative da parte di eredi | da rilevare | invariato o in crescita | invariato o in crescita |

---

## 01-P23 — Sapere chi paga quanto: statistica ufficiale delle aliquote effettive e unità per i grandi patrimoni

**Problema in un dato.** Le statistiche IRPEF dicono che lo 0,2% dei contribuenti con più di 300.000 € dichiara il 6,6% dell'imposta netta. Ma **non vedono** dividendi, plusvalenze, interessi e utili trattenuti nelle società: proprio i redditi che contano in cima. L'unica misura delle aliquote effettive del top 0,1% (32,6-36%) è accademica e su dati del 2015. Nessuno, nemmeno il MEF, pubblica quanto paga davvero chi sta in cima.

**Evidenze.** L'Australia segue i 500 maggiori gruppi privati e i successivi 5.000 con un programma dedicato (ATO *Top 500* e *Next 5,000*, risultati **da verificare** sui rapporti ATO). Il Regno Unito ha un'unità HMRC per i patrimoni più alti. La Francia pubblica i dati sui foyers più ricchi (DGFiP e IPP). L'Italia ha già i dati: dichiarazioni, Archivio dei rapporti finanziari, catasto, Registro imprese, CRS.

**Soluzione (PIENA).**
1. **Statistica ufficiale annuale delle aliquote effettive** per classi di reddito e di patrimonio (fino al top 0,01%), prodotta da DF, ISTAT e Banca d'Italia su dati collegati, che somma IRPEF, addizionali, sostitutive, imposte patrimoniali e la quota di imposte e utili trattenuti delle società controllate. Pubblicata con la Relazione sull'evasione. Metodo rivisto da UPB. **Garanzie dell'art. 89 GDPR scritte nella legge**: dati pseudonimizzati, trattati solo in un ambiente sicuro presso ISTAT o DF; **soglie minime di frequenza** nelle classi più alte, per non rendere riconoscibili le persone; **divieto di usare i dati collegati per l'accertamento**; parere del Garante sullo schema di norma.
2. **Consultazione della BCE** sullo schema di legge (Decisione 98/415/CE), perché la legge dà un compito nuovo alla Banca d'Italia; il compito non interferisce con quelli del Sistema europeo di banche centrali.
3. **Unità AdE "grandi patrimoni e gruppi familiari"** (circa 100 persone): vede insieme persona, società controllate, trust e polizze. Per le persone con redditi oltre 1 mln o patrimonio oltre 50 mln offre un **adempimento collaborativo per persone fisiche** sul modello del d.lgs. 128/2015: **sanzioni ridotte solo per i rischi comunicati in anticipo**; accesso solo con trasparenza piena su società, trust e polizze; **esclusione e revoca** per chi non comunica; risposte preventive negli stessi tempi dell'interpello ordinario, che resta aperto a tutti (art. 11 L. 212/2000); numeri aggregati pubblici. Svolge i controlli sugli altri.
4. **Trasparenza sui regimi speciali:** numero di optanti e gettito del regime dei neo-residenti (art. 24-bis TUIR), degli impatriati e del forfettario per classi, ogni anno.
5. **Statuto delle garanzie di 01-P10** per ogni uso dei dati: niente nuove raccolte massive, pseudonimizzazione, nessuna lista di nomi.

**Varianti**

| Variante | Contenuto | Costo di attuazione 2027 / 2028 / 2029 / regime | Intensità |
|---|---|---|---|
| PIENA | Punti 1-5 | 0,008 / 0,015 / 0,015 / **0,015** (2028) | 1 |
| ESSENZIALE | Punti 1, 2, 4, 5; unità AdE ridotta (circa 40 persone), senza adempimento collaborativo per persone fisiche | 0,004 / 0,006 / 0,006 / **0,006** | 0,5 |
| PILOTA | Solo la statistica con le sue garanzie e la consultazione BCE (punti 1-2) e la trasparenza (punto 4) | 0,002 / 0,002 / 0,002 / **0,002** | 0,2 |

Costi: stima GovernAI (circa 100 unità di personale qualificato e sistemi, sul modello dei costi di 01-P10, compreso l'ambiente sicuro per i dati), su RIALLOCAZIONE.

**Gettito atteso.** Il maggiore adempimento dei grandi patrimoni non è stimato e **non è copertura**: va al deficit, come per 01-P10.

**Articolato normativo essenziale** (disegno di legge; modifica della L. 196/2009 e del d.lgs. 300/1999; schema trasmesso alla BCE e al Garante prima dell'approvazione)

> **Art. 1 (Statistica delle aliquote effettive).** 1. Il Dipartimento delle finanze, con l'ISTAT e la Banca d'Italia, pubblica ogni anno, in allegato alla Relazione sull'economia non osservata e sull'evasione fiscale e contributiva, la distribuzione delle imposte effettivamente pagate per classi di reddito e di patrimonio, comprese le imposte sostitutive e la quota di imposte e utili non distribuiti delle società controllate. 2. Il collegamento dei dati avviene, ai sensi dell'articolo 89 del regolamento (UE) 2016/679, su dati pseudonimizzati e in un ambiente sicuro presso l'ISTAT o il Dipartimento delle finanze; i dati collegati non possono essere usati per attività di accertamento o controllo; le classi sono pubblicate solo se rispettano soglie minime di frequenza fissate dall'ISTAT. 3. Il metodo è sottoposto all'Ufficio parlamentare di bilancio.
>
> **Art. 2 (Grandi patrimoni).** 1. Nell'Agenzia delle entrate è istituita un'unità per i grandi patrimoni e i gruppi familiari, che opera nel rispetto dell'articolo 3 della legge di cui alla proposta 01-P10. 2. Le persone fisiche con reddito complessivo superiore a 1 milione di euro o patrimonio superiore a 50 milioni di euro possono aderire a un regime di adempimento collaborativo con obbligo di comunicare società controllate, trust e contratti assicurativi. 3. La riduzione delle sanzioni si applica solo ai rischi comunicati prima della presentazione della dichiarazione. L'omessa comunicazione comporta l'esclusione o la revoca dal regime. Le risposte preventive sono rese nei termini dell'articolo 11 della legge 27 luglio 2000, n. 212. Il numero degli aderenti e i risultati sono pubblicati ogni anno in forma aggregata.
>
> **Art. 3 (Trasparenza sui regimi speciali).** 1. Il Rapporto annuale sulle spese fiscali indica, per ciascun regime sostitutivo agevolato riservato alle persone fisiche, il numero dei beneficiari, il gettito e la distribuzione per classi di reddito.

**Rischi e mitigazioni.**
- **Privacy (SIC).** Dati pseudonimizzati, ambiente sicuro, soglie di frequenza, divieto di uso per l'accertamento; per l'unità, Statuto delle garanzie di 01-P10, registro dei modelli, audit.
- **Adempimento collaborativo come favore.** Sconto sulle sanzioni solo in cambio di trasparenza anticipata; revoca per chi omette; numeri pubblici; l'interpello resta aperto a tutti negli stessi tempi.
- **Statistica come strumento di parte.** Metodo pubblico, revisione UPB, dati per tutte le classi.

**Indicatori**

| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Statistica ufficiale delle aliquote effettive fino al top 0,01% | inesistente, 2026 | prima edizione | serie annuale |
| Persone in adempimento collaborativo per persone fisiche | 0, 2026 | ≥ 300 | ≥ 1.000 |
| Optanti e gettito dei regimi speciali pubblicati | parziale, 2026 | completo | completo |
