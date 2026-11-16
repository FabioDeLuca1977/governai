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

**Scelta di chi guida il progetto (16/11/2026): "holding subito".** Dentro 01-P19 entra anche la regola sui **dividendi della propria società operativa parcheggiati nella holding di famiglia** e non reinvestiti (regola (b) della bozza `benchmark/bozza_proposta_neutralita.md`), con tutte le condizioni del giurista (`giuridico/note_neutralita.md`, `giuridico/conformita_neutralita.csv`). La proposta ha quindi due parti: **parte A**, proventi passivi delle holding passive (punti 1-12, invariati salvo la lett. c dell'art. 2 c. 3); **parte B**, dividendi operativi fermi in qualunque holding personale (punti 13-24). La parte B è il secondo lato di 01-P25 (24% sugli utili lasciati nelle imprese di persone): toglie il vantaggio opposto a chi ha una SRL e una holding.

**Problema in un dato.** Un dividendo incassato da una persona paga il **26%**. Incassato dalla sua holding paga l'**1,2%** (95% escluso, 5% all'IRES del 24%; artt. 87 e 89 TUIR). Sull'utile di un'impresa il prelievo complessivo è **43,8%** se il socio è una persona e **24,9%** se è una holding, finché la holding non distribuisce (calcolo nella diagnosi, par. 4.3). Si può non distribuire mai: alla morte del socio, in caso di liquidazione o recesso, il costo delle quote rivalutato in successione (art. 68 c. 6 TUIR) cancella l'imposta rinviata. Nessuna fonte ufficiale dice quanto valga questo canale. La clausola anti-abuso (art. 10-bis L. 212/2000) colpisce il rinvio solo se "sine die" e va provato caso per caso (atto di indirizzo MEF 27/2/2025): poca certezza per chi è in buona fede, poco effetto su chi pianifica.

**Il secondo dato (parte B).** Sullo stesso utile di 1.000.000 € lasciato nell'impresa una SRL paga il **27,9%**; se il socio porta i dividendi nella sua holding e li tiene fermi paga il **28,8%** e può non pagare mai il resto. Il socio di una SNC paga subito il **47,3%** (`analisi/chi_paga/neutralita.csv`, regole 2026). Una holding che tiene fermi i dividendi della propria società operativa fa, nei fatti, un prelievo che non si chiama prelievo. Nessuna fonte ufficiale dice quanti dividendi operativi arrivano alle holding personali e quanti restano fermi: il DF ha il dato nel modello Redditi SC (quadro RF, utili esclusi art. 89 TUIR) ma non lo pubblica.

**Evidenze.**
- Gli studi sui conti distributivi trovano un sistema regressivo sopra il 93°-95° percentile; il top 0,1% paga in media il 32,6-36% (Dalle Luche et al. 2026; Guzzardi et al. 2024; dati 2015). La causa principale è il reddito da capitale tassato poco o in ritardo.
- EU Tax Observatory (*Global Tax Evasion Report 2024*): le holding personali sono il canale principale con cui i miliardari pagano lo 0-0,5% del patrimonio.
- La Francia ha visto la sua imposta minima del 20% rendere 0,4 mld invece di 1,9 anche perché i dividendi sono rimasti nelle società; nel 2026 ha aggiunto una tassa sulle holding patrimoniali (art. 235 ter C CGI). Nell'apporto di quote a una holding (art. 150-0 B ter CGI) chi vende entro 3 anni deve reinvestire una quota in attività economiche, altrimenti paga l'imposta rinviata.
- Gli Stati Uniti tassano al **20%** gli utili passivi non distribuiti delle *personal holding companies* (IRC §541), definite in modo oggettivo: 5 persone o meno con più della metà, almeno il 60% di redditi passivi; l'*accumulated earnings tax* (IRC §531) colpisce gli utili trattenuti oltre i bisogni ragionevoli dell'impresa. Il Regno Unito tassa i prestiti delle società chiuse ai soci (s. 455 CTA 2010, 33,75%, restituito alla chiusura del prestito).

**Soluzione (PIENA).**

*Parte A: proventi passivi delle holding passive.*
1. **Chi è dentro.** È "holding personale passiva" una società o un ente commerciale che, nello stesso anno:
   - è controllata (più del 50% dei voti o degli utili, anche indirettamente) da **non più di 5 persone fisiche**, con i familiari fino al terzo grado contati come una persona;
   - ha almeno il **60%** dei proventi da fonti passive: dividendi di portafoglio, interessi, plusvalenze su partecipazioni e titoli, canoni di immobili non strumentali, royalty non legate a un'attività. **Non contano come passivi i dividendi delle partecipazioni di almeno il 10% in società che esercitano un'attività d'impresa effettiva** (italiane o estere): una holding che guida un gruppo operativo non è passiva;
   - ha un attivo passivo netto oltre **2 mln €**.
2. **Cosa paga, e da quando.** Sulla quota esclusa (95%) dei dividendi e delle plusvalenze PEX **incassati dal periodo d'imposta successivo all'entrata in vigore**, che non è distribuita ai soci entro 12 mesi dalla chiusura dell'esercizio né reinvestita, la holding versa un'imposta sostitutiva del **26%**: lo stesso prelievo che il socio avrebbe pagato possedendo direttamente. **Le riserve già formate prima della legge non si tassano mai**, nemmeno se restano nella holding.
3. **Cosa resta fuori dalla base.**
   - i dividendi delle partecipazioni di almeno il 10% in società operative: li regola la parte B, solo se restano fermi;
   - i dividendi coperti dalla **direttiva madre-figlia** (2011/96/UE), anche negli anni dopo l'incasso, salvo costruzioni non genuine (art. 1 parr. 2-3 della direttiva);
   - **niente doppia imposta nelle catene (lett. c corretta):** i dividendi da partecipazioni di almeno il 10% in holding italiane o estere già soggette alla parte A, e quelli che una holding riceve da un'altra holding per la parte che **deriva da dividendi di società operative** (che nella catena conservano la loro natura e restano nella parte B). La versione precedente escludeva solo gli utili di holding soggette alla parte A: in una catena operativa → H1 → H2 passiva lo stesso utile poteva essere colpito due volte (rilievo del giurista).
4. **Niente doppia imposta.** Le riserve già tassate con questa imposta sono distribuite in esenzione. **Il beneficio segue le quote**: in caso di vendita, donazione o successione lo ha chi possiede le quote al momento della distribuzione o della liquidazione.
5. **Reinvestimenti esclusi (protezione delle PMI).** Non entrano nella base gli importi che la holding, entro 3 anni, reinveste in: capitale o finanziamenti di società operative controllate o collegate (≥20%); sottoscrizione di nuove azioni di PMI non quotate o quote di fondi EuVECA, **nei limiti dell'art. 21 del regolamento generale di esenzione per categoria** (aiuti al finanziamento del rischio, o il regolamento che lo sostituisce); beni strumentali. Se il reinvestimento non avviene, l'imposta si paga con interessi legali.
6. **Riserva per acquisizioni e crisi.** La holding può vincolare, dichiarandolo, fino al **30% dell'attivo passivo** (massimo 20 mln €) in una riserva per: acquistare il controllo o almeno il 20% di società operative; ricapitalizzare o finanziare società controllate in perdita o in crisi (Codice della crisi d'impresa). La riserva non paga finché è usata entro **5 anni**; altrimenti l'imposta si paga con interessi legali.
7. **Franchigia.** I primi **100.000 €** l'anno di proventi esclusi trattenuti non pagano.
8. **Prestiti e beni ai soci.** Prestiti, garanzie e beni messi a disposizione dei soci o dei loro familiari si **presumono** distribuzione e pagano il 26%, salvo restituzione entro 12 mesi, interessi e corrispettivi di mercato o **altra prova contraria**. Se lo stesso beneficio è già tassato al socio come reddito diverso (art. 67 c. 1 lett. h-ter TUIR), non si paga due volte. La regola vale per tutte le holding personali, anche per quelle soggette solo alla parte B.
9. **Liquidazione e recesso.** Le riserve formate **dopo l'entrata in vigore** con proventi esclusi e non tassati restano tassabili come dividendo anche se le quote sono state rivalutate in successione; vale solo per le **successioni aperte dopo** l'entrata in vigore.
10. **Holding estere.** Per le holding passive non residenti controllate da residenti si applica la stessa regola, imputando al socio sul modello dell'art. 167 TUIR, con **la stessa base, la stessa franchigia, gli stessi reinvestimenti esclusi e la stessa riserva** della regola interna, e con l'**esimente dell'attività economica effettiva sempre disponibile** (art. 167 c. 5 TUIR; obbligatoria per UE e SEE: art. 7 par. 2 lett. a ATAD, *Cadbury Schweppes* C-196/04).
11. **Exit tax minima, solo sulle holding passive.** Chi trasferisce la residenza all'estero e possiede, anche indirettamente, quote di una holding personale passiva per un valore oltre **1 mln €** paga il 26% sulla parte di plusvalenza latente che corrisponde alle **riserve formate dopo l'entrata in vigore con proventi esclusi non ancora tassati** (franchigia, reinvestimenti, riserva). Nessuna exit tax sulle riserve pregresse né sulle altre partecipazioni. Verso UE, SEE e Svizzera la riscossione è **sospesa senza interessi e senza garanzie** fino alla vendita o alla distribuzione, e le minusvalenze successive non riconosciute dallo Stato di arrivo riducono l'imposta (CGUE C-9/02, C-470/04, C-581/17 *Wächtler*); verso gli altri Paesi si paga in 5 rate annuali. Vale solo per i trasferimenti successivi all'entrata in vigore. Non colpisce i conti della parte B (punto 22).
12. **Antiabuso con interpello.** Clausola antiabuso specifica (soglie calcolate per gruppo familiare; holding "operative di facciata") con interpello preventivo per chi è in dubbio.

*Parte B: dividendi della propria società operativa fermi nella holding (scelta del 16/11/2026).*

13. **Quali holding.** Ogni **holding personale**: società o ente commerciale controllato, anche indirettamente, da non più di 5 persone fisiche, con coniuge, parenti entro il terzo grado e affini entro il secondo contati come una persona (stessa definizione del punto 1, senza i requisiti del 60% di proventi passivi e dei 2 mln di attivo passivo). **Non serve che la holding sia passiva.** **Restano fuori** le società semplici, già tassate per trasparenza sui dividendi ricevuti (art. 32-quater DL 124/2019), e le holding che hanno optato per la trasparenza (artt. 115-116 TUIR), il cui reddito è già imputato ai soci.
14. **Chi paga: il socio, non la holding.** Il **contribuente è il socio persona fisica che, con il suo gruppo familiare, controlla la holding o ne determina le distribuzioni**, per la sua quota. I soci di minoranza che non fanno parte del gruppo di controllo non pagano: una famiglia con il 20% in una holding di cinque famiglie non controlla nulla. Se nessun gruppo familiare ha il controllo, la parte B non si applica.
15. **La holding fa solo da sostituto.** La holding versa l'imposta per conto del socio come **responsabile d'imposta con rivalsa obbligatoria**: la somma versata è un **anticipo sui futuri utili di quel socio** e non una distribuzione ulteriore. Senza la rivalsa l'imposta peserebbe sulle riserve della holding e diventerebbe, nella sostanza, un'imposta sulla holding (CGUE C-68/15). È la scelta tecnica più importante della parte B.
16. **Su cosa.** I **dividendi delle partecipazioni di almeno il 10% in società operative**, italiane o estere, **incassati dal periodo d'imposta 2029**. Se la legge entra in vigore entro il **31/12/2027** (per esempio in un collegato fiscale), si parte dai dividendi 2028; le stime contano il 2029. Così l'aggravio vale dal periodo successivo a quello in corso, come chiede l'art. 3 c. 1 dello Statuto del contribuente, senza derogarvi. Ogni anno di dividendi apre un **conto di reinvestimento**. Le riserve già formate prima della legge **non si toccano mai**.
17. **Antiabuso sulla base.** Entrano nel conto anche le somme che la holding riceve dalla società operativa senza chiamarle dividendi:
    - **rimborso di riserve di capitale** e somme da recesso, riduzione del capitale o liquidazione della partecipata, per la parte che eccede il costo fiscale;
    - **plusvalenze esenti (PEX, art. 87 TUIR) su cessioni a parti correlate**, cioè a società o persone dello stesso gruppo familiare;
    - **prestiti dalla società operativa alla holding o ai soci**, compreso il cash pooling, se non vanno a un reinvestimento ammesso. La presunzione è relativa: un cash pooling a condizioni di mercato e con scopo d'impresa si può provare.
18. **Cosa conta come reinvestimento in attività vere, entro 3 anni** (elenco fissato in legge, art. 23 Cost.):
    - capitale o finanziamenti a società operative, italiane o estere, controllate o collegate (almeno 20%), anche la stessa che ha pagato il dividendo;
    - acquisto del controllo o di almeno il 20% di società operative, italiane o estere;
    - beni strumentali usati da società operative del gruppo, compresi gli immobili strumentali;
    - nuove azioni di PMI non quotate e quote di fondi EuVECA, **nei limiti dell'art. 21 del regolamento generale di esenzione** (o del successore dal 2027);
    - rimborso del debito contratto per acquistare partecipazioni operative.

    **Non contano** liquidità, titoli, fondi, immobili dati in affitto a terzi, prestiti ai soci e i beni non strumentali elencati nella legge (imbarcazioni e aeromobili da diporto, autovetture non strumentali, oggetti d'arte e da collezione, metalli preziosi). "Società operativa" è definita in legge con lo stesso test dell'attività d'impresa effettiva usato per l'art. 167 c. 5 TUIR. I reinvestimenti si misurano **al netto** dei rimborsi ricevuti nello stesso periodo, così i giri circolari non contano. **Un euro reinvestito conta una sola volta**: la holding dichiara a quale conto lo imputa (parte A o parte B).

    **Riserva per acquisizioni e crisi:** la holding può vincolare fino al 30% del conto per **5 anni**, per gli stessi scopi del punto 6; il tetto di 20 mln € vale per gruppo familiare insieme alla riserva del punto 6.
19. **Cosa paga.** Alla fine dei 3 anni (o dei 5 per la riserva), la parte del conto **né distribuita né reinvestita** si considera **distribuita ai soci di controllo** e paga il **26%**, la stessa imposta che il socio avrebbe pagato incassando direttamente. Quando la holding distribuisce davvero quelle somme non si paga di nuovo: c'è un **credito che segue le quote** in caso di vendita, donazione o successione.
20. **Franchigia per famiglia.** I primi **100.000 €** l'anno di dividendi operativi fermi, **per gruppo familiare** (non per holding), non pagano. È distinta dalla franchigia della parte A (punto 7): una riguarda i proventi passivi, l'altra i dividendi operativi; nessuna delle due si moltiplica aprendo più holding.
21. **Holding estere trattate come le italiane.** Per i soci residenti di holding estere vale la **stessa regola**: stessa base, stessa franchigia, stessi reinvestimenti in società operative italiane ed estere, stessa riserva, stessi tempi. Il socio ha un **credito per le imposte estere** pagate sugli stessi utili. Con la parità piena non serve l'esimente dell'attività economica (*Cadbury Schweppes*, C-196/04); se in attuazione resta una differenza, l'esimente va data alle holding UE e SEE e, per parità, anche alle italiane. Manca un sostituto italiano: il socio versa direttamente, con il prospetto in dichiarazione e i dati dello scambio di informazioni.
22. **Trasferimento di residenza.** Nessun anticipo dell'imposta all'uscita: il conto **prosegue** anche dopo il trasferimento e alla scadenza si tassa la parte non reinvestita; se la holding è italiana la versa lei, come sostituto. L'exit tax del punto 11 non colpisce gli stessi importi.
23. **Successioni.** I conti di reinvestimento passano agli eredi con il termine che continua a decorrere, e il credito segue le quote. La rivalutazione del costo in successione (art. 68 c. 6 TUIR) non cancella l'imposta già pagata e non la fa pagare due volte. Vale per le successioni aperte dopo la legge.
24. **Prospetto, interpello e direttiva madre-figlia.** Prospetto annuale in dichiarazione con dividendi operativi incassati, conti, reinvestimenti, prestiti ai soci; interpello preventivo (art. 11 L. 212/2000), fermo l'art. 10-bis. La parte B non esclude i dividendi coperti dalla direttiva 2011/96/UE perché tassa il socio, non la holding: la direttiva riguarda la società madre. **Ripiego pronto** se il Dipartimento per le politiche europee giudica alto il rischio: escludere dalla base i dividendi coperti dalla direttiva (salvo art. 1 parr. 2-3) e, per parità (art. 53 L. 234/2012), anche quelli delle figlie italiane operative. Il ripiego svuota gran parte della parte B e di FN13: la relazione tecnica indica a parte la quota di base che viene da figlie UE.

**Varianti**

| Variante | Contenuto | Costo di attuazione 2027 / 2028 / 2029 / regime | Intensità | Copertura |
|---|---|---|---|---|
| PIENA | Punti 1-24; parte A: soglia 2 mln, franchigia 100.000 €, imposta 26% sulla quota esclusa trattenuta; parte B: dividendi operativi fermi dal 2029, franchigia **100.000 €** l'anno per famiglia, **anche holding estere** | 0,005 / 0,016 / 0,016 / **0,016** (2028) | 1 | FN05 + FN06 + FN13 + FN14 |
| ESSENZIALE | Parte A: solo holding residenti; soglia 5 mln, franchigia 250.000 €; imposta del **13%** come acconto, scomputato alla distribuzione; il credito d'acconto **segue le quote** (vendita, donazione, successione), non è rimborsabile se la riserva non è mai distribuita ma si usa in liquidazione; punti 1-3, 5, 6, 8, 9, 11, 12. Parte B: punti 13-20 e 22-24 **solo per holding residenti**, franchigia **500.000 €** l'anno per famiglia, **con data di revisione** (sotto) | 0,004 / 0,011 / 0,011 / **0,011** | 0,6 | FN05 + FN13 |
| ZERO | Solo trasparenza: prospetto in dichiarazione per le holding personali passive sopra le soglie (attivo passivo, proventi esclusi, utili trattenuti, prestiti ai soci) e per le holding personali con dividendi operativi (incassati, fermi, reinvestiti); relazione annuale del Dipartimento delle Finanze con dati solo aggregati; nessun prelievo | 0 | 0,15 | nessuna |

**Parte B nella ESSENZIALE: solo holding residenti, con data di revisione.** Il diritto UE non lo vieta, perché a essere favorito è l'estero, ma due residenti con la stessa ricchezza sono trattati in modo diverso secondo il Paese della holding: si giustifica solo come fase transitoria (giurista). Per questo la legge prevede:
- una **clausola di revisione con data**: entro il 31/12/2031, con i dati del prospetto, il Parlamento estende la parte B alle holding estere controllate da residenti o ne conferma l'esclusione con motivazione;
- una **norma per le holding estere costituite, o che ricevono partecipazioni operative, dopo l'entrata in vigore**: si trattano come residenti salvo prova della sostanza (oltre alla presunzione dell'art. 73 c. 5-bis TUIR, testo vigente da verificare dopo il d.lgs. 209/2023).

Motivazione delle intensità: la ESSENZIALE dimezza il vantaggio del rinvio sui proventi passivi e chiude prestiti ai soci, rivalutazione in successione e fuga di residenza; sui dividendi operativi tocca solo chi tiene fermi più di 500.000 € l'anno in una holding italiana. Lascia fuori le holding passive tra 2 e 5 mln e quelle estere. Non c'è una variante PILOTA: un'imposta non si sperimenta su un campione senza violare l'art. 3 Cost. Il costo cresce di 0,001 rispetto alla prima bozza per l'exit tax e il controllo della riserva; cresce di altri **0,005 (PIENA) e 0,004 (ESSENZIALE)** dal 2028 per la parte B (conti di reinvestimento, sostituto con rivalsa, controlli su prestiti e cash pooling, sistemi Sogei; stima GovernAI: metà della quota di attuazione di 0,01 della bozza di 01-P25, che teneva insieme le due regole; 01-P25 conserva per prudenza la sua quota intera).

**Gettito.** Parte A in FN05 (ESSENZIALE o PIENA) e FN06 (solo PIENA). Parte B in **FN13** (ESSENZIALE o PIENA, 0,03-0,23 a regime) e **FN14** (solo PIENA, in più, 0,02-0,10), con primo gettito nel **2033** (dividendi 2029 non reinvestiti entro il 2032) e pieno dal 2034: vedi `benchmark/finale_coperture_holding.csv`. **Nessun doppio conteggio**: la base della parte A esclude per legge i dividendi operativi (art. 2 c. 3 lett. a), che sono esattamente la base della parte B. FN13 e FN14 non finanziano spese che partono prima del 2033.

**Articolato normativo essenziale** (legge di bilancio o disegno di legge collegato; nuovi articoli nel testo unico delle imposte sui redditi, d.lgs. 117/2026, numerazione da verificare)

> **Art. 1 (Holding personali passive).** 1. Ai fini del presente articolo è holding personale passiva la società o l'ente commerciale residente che nel periodo d'imposta: a) è controllato, ai sensi dell'articolo 2359, primo comma, numero 1), del codice civile, anche indirettamente, da non più di cinque persone fisiche, considerando come una sola persona il coniuge, i parenti entro il terzo grado e gli affini entro il secondo; b) ha conseguito proventi passivi, come definiti dal comma 2, pari almeno al 60 per cento dei proventi complessivi; c) ha un attivo passivo netto superiore a 2 milioni di euro.
> 2. Sono proventi passivi gli utili e le plusvalenze su partecipazioni e titoli, gli interessi, i canoni di immobili non strumentali e i canoni per l'uso di beni immateriali non connessi a un'attività d'impresa effettiva. Non sono proventi passivi gli utili derivanti da partecipazioni non inferiori al 10 per cento in società, residenti o non residenti, che esercitano un'attività d'impresa effettiva.
>
> **Art. 2 (Imposta sugli utili esclusi trattenuti).** 1. Sulla quota degli utili e delle plusvalenze esclusa dal reddito ai sensi degli articoli 87 e 89 del TUIR, conseguiti a decorrere dal periodo d'imposta successivo a quello in corso alla data di entrata in vigore della presente legge, al netto della franchigia di 100.000 euro, che non sia distribuita ai soci entro dodici mesi dalla chiusura del periodo d'imposta né reinvestita o accantonata ai sensi dell'articolo 3, la holding personale passiva versa un'imposta sostitutiva del 26 per cento. Le riserve formate con utili conseguiti in periodi precedenti non sono in alcun caso soggette all'imposta.
> 2. Le riserve formate con utili assoggettati all'imposta di cui al comma 1 non concorrono a formare il reddito di chi possiede le partecipazioni al momento della distribuzione o della liquidazione.
> 3. Sono esclusi dalla base del comma 1, anche nei periodi d'imposta successivi a quello di percezione: a) gli utili derivanti da partecipazioni non inferiori al 10 per cento in società che esercitano un'attività d'impresa effettiva; b) gli utili percepiti da società di altri Stati membri dell'Unione europea che rientrano nell'ambito della direttiva 2011/96/UE, salvo che ricorrano le condizioni dell'articolo 1, paragrafi 2 e 3, della stessa direttiva; c) gli utili derivanti da partecipazioni non inferiori al 10 per cento in società, residenti o non residenti, soggette all'imposta di cui al comma 1 o all'articolo 2-bis, nonché, in ogni caso, gli utili che una società riceve da un'altra società per la parte che deriva da utili esclusi ai sensi della lettera a); a tal fine gli utili conservano la loro natura in ciascun passaggio della catena di partecipazioni.
>
> **Art. 2-bis (Utili di società operative trattenuti dalle holding personali).** 1. Ai fini del presente articolo è holding personale la società o l'ente commerciale, residente o non residente, controllato ai sensi dell'articolo 1, comma 1, lettera a). Non sono holding personali le società semplici di cui all'articolo 32-quater del decreto-legge 26 ottobre 2019, n. 124, né le società che hanno optato per il regime degli articoli 115 e 116 del TUIR.
> 2. Gli utili derivanti da partecipazioni non inferiori al 10 per cento in società che esercitano un'attività d'impresa effettiva, come definita dal comma 7, percepiti dalla holding personale a decorrere dal periodo d'imposta 2029, ovvero dal periodo d'imposta successivo a quello in corso alla data di entrata in vigore della presente legge se successivo, che entro i tre periodi d'imposta successivi a quello di percezione non sono distribuiti né reinvestiti ai sensi del comma 5, si considerano distribuiti alle persone fisiche che, da sole o con il proprio gruppo familiare, controllano la holding o ne determinano le distribuzioni, in proporzione alla loro quota, e sono soggetti alla ritenuta a titolo d'imposta del 26 per cento. Le riserve formate con utili percepiti in periodi precedenti non sono in alcun caso soggette al presente articolo.
> 3. Concorrono alla formazione della base di cui al comma 2: a) le somme ricevute dalle società di cui al comma 2 a titolo di rimborso di riserve di capitale, recesso, riduzione del capitale o liquidazione, per la parte eccedente il costo fiscale della partecipazione; b) le plusvalenze escluse ai sensi dell'articolo 87 del TUIR realizzate con la cessione di partecipazioni a società o persone del medesimo gruppo familiare; c) i finanziamenti erogati dalle società di cui al comma 2 alla holding personale o ai suoi soci, anche nell'ambito di rapporti di tesoreria accentrata, non destinati ai reinvestimenti del comma 5, salvo prova che il rapporto è concluso a condizioni di mercato e per esigenze dell'impresa.
> 4. La holding personale residente versa la ritenuta di cui al comma 2 in qualità di responsabile d'imposta, con obbligo di rivalsa; la somma versata è imputata in conto ai futuri utili spettanti al socio e non costituisce distribuzione. Le riserve corrispondenti agli utili assoggettati alla ritenuta non concorrono a formare il reddito di chi possiede le partecipazioni al momento della distribuzione effettiva o della liquidazione. Per le holding personali non residenti l'imposta è dovuta dal socio, con le stesse regole e con un credito per le imposte pagate all'estero sugli stessi utili.
> 5. Sono reinvestiti gli importi, al netto dei rimborsi ricevuti nel medesimo periodo, destinati a: a) conferimenti o finanziamenti a società, residenti o non residenti, che esercitano un'attività d'impresa effettiva, controllate o collegate ai sensi dell'articolo 2359 del codice civile; b) acquisto del controllo o di partecipazioni non inferiori al 20 per cento in tali società; c) beni strumentali utilizzati da società del gruppo che esercitano un'attività d'impresa effettiva; d) nei limiti dell'articolo 21 del regolamento (UE) n. 651/2014 o della disciplina che lo sostituisce, sottoscrizione di azioni o quote di nuova emissione di piccole e medie imprese non quotate o di fondi europei per il venture capital; e) rimborso dei debiti contratti per l'acquisto delle partecipazioni di cui alle lettere a) e b). Non sono reinvestimenti le disponibilità liquide, gli strumenti finanziari diversi da quelli delle lettere a), b) e d), gli immobili locati a terzi, i finanziamenti ai soci e ai loro familiari, le imbarcazioni e gli aeromobili da diporto, le autovetture non strumentali, gli oggetti d'arte e da collezione e i metalli preziosi. Si applica l'articolo 3, comma 2, con termine di cinque periodi d'imposta, fino al 30 per cento degli utili di ciascun periodo e nel limite complessivo di 20 milioni di euro per gruppo familiare, comprensivo della riserva di cui allo stesso articolo 3, comma 2. Ciascun importo reinvestito è imputato a una sola base.
> 6. Non sono soggetti al comma 2 i primi [PIENA: 100.000 / ESSENZIALE: 500.000] euro annui di utili per gruppo familiare, comunque ripartiti tra più holding personali.
> 7. Esercita un'attività d'impresa effettiva la società che soddisfa le condizioni dell'articolo 167, comma 5, del TUIR. 8. [Solo PIENA] Il presente articolo si applica con le medesime regole alle holding personali non residenti controllate da persone fisiche residenti. [Solo ESSENZIALE] Il presente articolo si applica alle holding personali residenti e alle holding personali non residenti costituite, o che ricevono partecipazioni nelle società di cui al comma 2, dopo la data di entrata in vigore della presente legge, salvo prova che esercitano un'attività economica effettiva con adeguate risorse; entro il 31 dicembre 2031 il Governo trasmette alle Camere una relazione sui dati del prospetto e la legge decide se estendere il presente articolo a tutte le holding personali non residenti.
> 9. In caso di trasferimento della residenza del socio, le basi non ancora scadute restano soggette al comma 2 alla loro scadenza. In caso di successione aperta dopo l'entrata in vigore della presente legge, le basi e i crediti passano agli eredi e i termini continuano a decorrere; la determinazione del costo ai sensi dell'articolo 68, comma 6, del TUIR non estingue l'imposta già versata e non comporta un nuovo prelievo sugli stessi utili.
>
> **Art. 3 (Reinvestimento produttivo e riserva per acquisizioni e crisi).** 1. Non concorrono alla base di cui all'articolo 2 gli importi investiti, entro i tre periodi d'imposta successivi, in conferimenti o finanziamenti a società che esercitano un'attività d'impresa effettiva e sono controllate o collegate ai sensi dell'articolo 2359 del codice civile, in beni strumentali e, nei limiti dell'articolo 21 del regolamento (UE) n. 651/2014 o della disciplina che lo sostituisce, nella sottoscrizione di azioni o quote di nuova emissione di piccole e medie imprese non quotate o di fondi europei per il venture capital. 2. Non concorrono altresì alla base, fino al 30 per cento dell'attivo passivo netto e comunque fino a 20 milioni di euro, gli importi iscritti in una riserva vincolata all'acquisto del controllo o di partecipazioni non inferiori al 20 per cento in società che esercitano un'attività d'impresa effettiva, o al finanziamento e alla ricapitalizzazione di società controllate in perdita o in stato di crisi, utilizzata entro i cinque periodi d'imposta successivi. 3. In mancanza del reinvestimento o dell'utilizzo della riserva nei termini, l'imposta è dovuta con gli interessi legali.
>
> **Art. 4 (Prestiti e beni ai soci).** 1. I finanziamenti, le garanzie e i beni concessi in uso dalla holding personale passiva o dalla holding personale di cui all'articolo 2-bis ai soci o ai loro familiari si presumono utili distribuiti, salvo restituzione entro dodici mesi, corrispettivo di mercato o altra prova contraria. 2. La presunzione non si applica per la parte di beneficio già tassata ai sensi dell'articolo 67, comma 1, lettera h-ter), del TUIR.
>
> **Art. 5 (Liquidazione e recesso).** 1. Nei casi di cui all'articolo 47, comma 7, del TUIR, la parte delle somme corrispondente a riserve formate, a decorrere dal periodo d'imposta di cui all'articolo 2, comma 1, con utili e plusvalenze esclusi e non assoggettati all'imposta di cui all'articolo 2, costituisce utile, senza tenere conto della determinazione del costo ai sensi dell'articolo 68, comma 6, del TUIR. 2. Il comma 1 si applica alle partecipazioni acquisite per successioni aperte dopo la data di entrata in vigore della presente legge.
>
> **Art. 6 (Soggetti non residenti).** 1. Ai soggetti non residenti che possiedono i requisiti dell'articolo 1 e sono controllati da persone fisiche residenti si applica l'articolo 167 del TUIR, anche in deroga alle condizioni di tassazione effettiva del comma 4, lettera a), con la stessa decorrenza, base, franchigia, esclusioni, reinvestimenti e riserva previsti dagli articoli 2 e 3. 2. Resta sempre ferma l'esimente del comma 5 dell'articolo 167 del TUIR.
>
> **Art. 7 (Trasferimento della residenza).** 1. Le persone fisiche che trasferiscono la residenza fiscale all'estero dopo la data di entrata in vigore della presente legge e possiedono, anche indirettamente, partecipazioni in holding personali passive di valore superiore a 1 milione di euro realizzano, alla data del trasferimento, la plusvalenza corrispondente alle riserve formate ai sensi dell'articolo 2, comma 1, con utili e plusvalenze esclusi non assoggettati all'imposta. 2. In caso di trasferimento in uno Stato dell'Unione europea, dello Spazio economico europeo con adeguato scambio di informazioni o nella Confederazione svizzera, la riscossione è sospesa, senza interessi e senza garanzie, fino al realizzo o alla distribuzione; le minusvalenze successive non riconosciute dallo Stato di destinazione riducono l'imposta. Negli altri casi l'imposta è versata in cinque rate annuali. 3. Il comma 1 non si applica agli utili soggetti all'articolo 2-bis.
>
> **Art. 8 (Antiabuso, decorrenza e valutazione).** 1. Le soglie e le franchigie degli articoli 1, 2 e 2-bis sono calcolate per gruppo familiare. Il contribuente può presentare interpello ai sensi dell'articolo 11 della legge 27 luglio 2000, n. 212; resta fermo l'articolo 10-bis della stessa legge. 2. Gli articoli 1-7, salvo l'articolo 2-bis, si applicano dal periodo d'imposta successivo a quello in corso alla data di entrata in vigore. 3. Le holding personali presentano in dichiarazione un prospetto degli utili di cui agli articoli 2 e 2-bis percepiti, trattenuti, reinvestiti e accantonati e dei finanziamenti ai soci. 4. Entro tre anni il Dipartimento delle finanze pubblica una valutazione degli effetti su gettito, distribuzioni e investimenti, al netto delle minori entrate future dovute alla distribuzione in esenzione delle riserve tassate.

**Chi paga.**
- **Parte A.** Le famiglie con patrimoni finanziari di diversi milioni tenuti in holding che, **dopo la legge**, incassano proventi passivi e non li reinvestono nell'economia produttiva. Con la ESSENZIALE paga circa metà del vantaggio oggi goduto, come acconto restituito alla distribuzione.
- **Parte B.** Il socio che controlla, con la sua famiglia, una holding che tiene fermi **oltre la franchigia** (100.000 € PIENA, 500.000 € ESSENZIALE) i dividendi della propria società operativa senza reinvestirli in attività vere. Esempio della bozza (PIENA, utile di 1.000.000 €): con gli utili fermi nella holding passa da 28,8% a **44,7%**; con la ESSENZIALE a 34,3%; a 300.000 € di utile la ESSENZIALE non tocca nessuno.
- **Non paga** chi ha un'impresa operativa e lascia gli utili nella società (27,9%), chi riceve dividendi e li reinveste (28,8%), chi accantona per acquisizioni e crisi, chi ha una piccola società di famiglia sotto le soglie e le franchigie, chi ha riserve formate prima della legge, il socio di minoranza che non controlla.

**Costituzionalità.**
- **Art. 53.** Parte A: l'imposta colpisce un reddito che la holding ha effettivamente incassato. Parte B: si tassa il socio su un utile che non ha percepito, ma solo se lui e la sua famiglia **controllano** la holding e decidono se distribuire: è la logica già in vigore della trasparenza (artt. 115-116 TUIR) e delle società estere controllate (art. 167 TUIR). La presunzione è relativa e c'è un credito alla distribuzione vera.
- **Art. 3.** Elimina una disparità: due persone con lo stesso dividendo pagano oggi 26% o 1,2% a seconda del contenitore. Le soglie, la regola delle 5 persone e la franchigia per gruppo familiare sono criteri oggettivi. Holding italiane ed estere sono trattate allo stesso modo nella PIENA; nella ESSENZIALE la differenza è temporanea, con data di revisione.
- **Art. 23.** Definizioni (società operativa, holding personale, reinvestimenti ammessi ed esclusi), aliquota, soglie, esclusioni e riserva sono fissate per legge.
- **Irretroattività e affidamento** (artt. 3 e 10 L. 212/2000): si applica solo ai proventi incassati dal periodo d'imposta successivo; la parte B solo ai dividendi dal 2029 (o dal 2028 con legge in vigore entro il 31/12/2027), senza derogare all'art. 3 dello Statuto; mai alle riserve già formate; la regola su liquidazione e recesso vale solo per le successioni future; l'exit tax solo per i trasferimenti futuri e solo sulle riserve nuove.
- **Art. 41.** Le imprese operative, gli utili lasciati nelle società operative, i reinvestimenti e la riserva per acquisizioni e crisi sono esclusi.
- **Art. 81.** FN13 e FN14 non rendono nulla prima del 2033: non coprono spese che partono prima.

**Diritto UE.**
- **Direttiva madre-figlia (2011/96/UE).** La Corte di giustizia (C-68/15, *X*, 17/5/2017, sulla "fairness tax" belga) ha giudicato contraria alla direttiva un'imposta che colpiva oltre il 5% utili ricevuti da figlie UE e redistribuiti negli anni successivi, guardando alla sostanza. Parte A: l'art. 2 c. 3 lett. b) esclude quei dividendi **anche negli anni dopo l'incasso**, salvo costruzioni non genuine. Parte B: il debitore è il socio persona fisica, con rivalsa obbligatoria e credito in capo a lui; la direttiva non disciplina la tassazione degli azionisti persone fisiche della madre. Resta un rischio, perché il prelievo scatta sull'importo del dividendo della figlia UE: va sentito il Dipartimento per le politiche europee, con il ripiego del punto 24 già scritto.
- **Discriminazione alla rovescia** (art. 53 L. 234/2012). L'esclusione dei dividendi di tutte le partecipate operative di almeno il 10%, italiane ed estere (art. 2 c. 3 lett. a), e delle holding già soggette all'imposta (lett. c), mette i dividendi italiani sullo stesso piano di quelli UE. **Resta da verificare con il Dipartimento per le politiche europee** il caso residuo delle partecipate italiane non operative e non soggette all'imposta. Il giurista raccomanda, in prospettiva, di portare anche la parte A sulla tassazione del socio con la holding sostituto: oggi non è nella proposta.
- **Libertà di stabilimento e dei capitali (artt. 49 e 63 TFUE).** Parte A: la regola estera non è più dura di quella interna, con esimente sempre disponibile. Parte B (PIENA): parità piena con credito per le imposte estere e reinvestimenti ammessi anche all'estero; senza differenze l'esimente non serve.
- **Exit tax.** Sospensione senza interessi e garanzie verso UE, SEE e Svizzera e riconoscimento delle minusvalenze successive (C-9/02, C-470/04, C-581/17). L'art. 5 ATAD vale solo per le società: per le persone valgono i Trattati. Per la parte B nessun anticipo all'uscita (punto 22).
- **Aiuti di Stato.** L'esclusione per chi reinveste in PMI non quotate e fondi EuVECA è inquadrata nell'art. 21 del regolamento generale di esenzione (o nel successore dal 2027), con i suoi limiti; i reinvestimenti nelle controllate operative sono una misura generale. Il limite delle 5 persone ha una ragione interna al tributo (il controllo sulla distribuzione), da scrivere nella relazione (sentenze *Gibraltar*, C-106/09 P e C-107/09 P).
- **ATAD** (2016/1164): fissa un minimo; una regola più severa è ammessa (art. 3).

**Rischi e mitigazioni.**
- **Fuga di residenza dei soci.** Coperta dall'exit tax minima del punto 11 per la parte A; per la parte B il conto prosegue dopo il trasferimento. È volutamente stretta: **chi si trasferisce porta con sé senza imposta le riserve formate prima della legge e le altre partecipazioni**. È un rischio che resta e va misurato (KPI sotto).
- **Gettito che cresce piano.** Parte A: primo versamento nel 2030 sui proventi del 2028, pieno dal 2031 (FN05, FN06). Parte B: primo gettito nel 2033, pieno dal 2034 (FN13, FN14); la base non è pubblicata e la risposta più semplice, lasciare gli utili nella società operativa, è legittima e coerente con la regola.
- **Riorganizzazioni artificiali** (holding "operative di facciata", proventi spostati sotto soglia, partecipazioni portate al 10% per far rientrare i dividendi nell'esclusione, dividendi trasformati in plusvalenze o rimborsi di capitale, prestiti dalla operativa, catene e più holding nella stessa famiglia). Soglie e franchigie per gruppo familiare; test dell'attività d'impresa effettiva (art. 167 c. 5); base della parte B estesa a riserve di capitale, recesso, liquidazione, PEX tra parti correlate e prestiti; reinvestimento netto; natura degli utili conservata nelle catene; interpello.
- **Holding che accantonano per acquisizioni o rilanci** (rilievo dei valutatori A e B). Riserva vincolata per 5 anni; reinvestimenti anche in fondi EuVECA e in società estere.
- **Direttiva madre-figlia sulla parte B.** Parere del Dipartimento per le politiche europee prima della legge; ripiego pronto (punto 24).
- **Costi di adempimento.** Un prospetto in più per le holding sopra soglie e franchigie (numero **da verificare** con il DF); nessun adempimento per le altre.
- **Liquidità della holding per pagare l'imposta.** L'imposta colpisce utili incassati e non distribuiti: la liquidità c'è; per la parte B la holding si rivale sul socio. In caso di reinvestimento mancato, rateazione automatica (01-P12).
- **Gettito in parte anticipato.** Le riserve tassate saranno distribuite in esenzione: le coperture contano solo la parte strutturale (FN05, FN06, FN13, FN14).

**Indicatori**

| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Holding personali passive censite e utili esclusi trattenuti | non pubblicato, 2026 (DF) | pubblicato ogni anno | pubblicato, con serie |
| Utili distribuiti dalle holding passive ai soci persone fisiche | da rilevare, 2027 | +20% sulla base | +30% |
| Reinvestimenti produttivi e riserve per acquisizioni e crisi dichiarati e usati | 0, 2027 | pubblicato | in crescita |
| Dividendi operativi incassati da holding personali, fermi e reinvestiti (parte B) | non pubblicato, 2026 | pubblicato | serie |
| Trasferimenti di residenza di soci di holding passive, con e senza exit tax | non rilevato | pubblicato | pubblicato, con valore delle riserve pregresse uscite |
| Aliquota effettiva del top 0,1% (statistica di 01-P23) | 32,6-36%, 2015 (stime accademiche) | prima misura ufficiale | +2/+4 punti |

**Coordinamento.** Con **01-P25** (24% sugli utili lasciati nelle imprese di persone): la parte B ne è il secondo lato e ne condivide la logica di neutralità tra forme d'impresa; le due proposte restano separate e hanno coperture diverse. Con **01-P22** (eredità): i conti della parte B passano agli eredi con il credito; nessun doppio conteggio tra FN10 e FN13. Con **01-P23** (statistica): il prospetto alimenta la statistica sulle aliquote effettive. Con **01-P24** (imposta minima sui grandi patrimoni): le imposte pagate con 01-P19 si scalano dall'imposta minima.

**Da verificare prima dell'uso pubblico** (dal giurista): numerazione nel testo unico d.lgs. 117/2026; testo vigente dell'art. 73 c. 5-bis TUIR; regolamento di esenzione dal 2027; C-581/17 sul testo ufficiale; parere del Dipartimento per le politiche europee sulla parte B.

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

---

*Scheda aggiunta il 16 novembre 2026 (scelte di chi guida il progetto, verifica giuridica, panel indipendente). Fonte: `benchmark/finale_proposta_patrimoniale.md`.*

## 01-P24 — Grandi patrimoni: un'imposta minima solo in cima, per chi paga poco rispetto a quello che ha

**Problema in un dato.** Il 10% delle famiglie ha il **60,6%** della ricchezza netta, la metà più povera il **7,2%** (Banca d'Italia, conti distributivi, fine 2025). Il top 0,1% degli adulti, circa 50.000 persone, ha il **9,3%** della ricchezza (Acciari, Alvaredo, Morelli, JEEA 2024, dati 2016), soprattutto in attività finanziarie e partecipazioni. Le imposte patrimoniali esistenti (IMU 18,2 mld, bollo 0,2% sui prodotti finanziari, IVIE e IVAFE 0,25 mld, successioni 1,1 mld) sono **proporzionali** e cadono soprattutto su case e risparmio di massa: **la partecipazione in una società non quotata, dove sta la ricchezza più alta, non paga nessuna imposta annua sul patrimonio.** Secondo il rapporto al G20 del 2024 le imposte personali dei miliardari valgono circa lo **0,3%** del loro patrimonio. Nessuna statistica ufficiale dice quante persone hanno più di 5, 10 o 50 milioni.

**Evidenze.**
- OCSE 2018: le imposte sul patrimonio sono passate da 12 Paesi nel 1990 a 4 nel 2017; servono **soglie alte, base ampia, poche esenzioni**; gli argomenti a favore sono più forti dove redditi da capitale e successioni sono tassati poco (è il caso italiano oggi).
- G20 2024: proposta di un minimo del **2%** sui miliardari (Zucman), cioè un'imposta che si paga solo per la parte non già coperta dalle imposte sul reddito; nessun accordo; nessuna proposta UE. La ESSENZIALE segue questo modello.
- Spagna: imposta di solidarietà sopra 3 mln, **623 mln** da **12.010** persone nel 2023.
- Svizzera: un punto di aliquota in meno fa salire del **43%** la ricchezza dichiarata in sei anni, soprattutto per evasione ed elusione (Brülhart et al. 2022).
- Norvegia 2022: aliquota all'1,1% sopra circa 20 mln NOK; **al massimo circa 100 partenze**, gettito +71,5% invece di +75%, nessun calo degli investimenti delle imprese (Ring, NBER 2026). La Norvegia ha un'exit tax.
- Francia: abolizione dell'ISF nel 2018, perdita di gettito 3-4,5 mld; **nessuna prova chiara** di più investimenti (Comité d'évaluation 2023; CAE 2025).
- Colombia: due quinti del top 0,01% evadevano l'imposta sul patrimonio nascondendo un terzo della ricchezza all'estero (Londoño-Vélez e Ávila-Mahecha 2021).
- Germania 1995: l'imposta sul patrimonio è stata bocciata dalla Corte costituzionale perché immobili e altri beni erano valutati con criteri diversi (BVerfG 2 BvL 37/91): **la valutazione deve essere omogenea**.

**Soluzione (ESSENZIALE).**
1. **Chi paga.** Le persone fisiche residenti con **patrimonio netto mondiale oltre 50 mln €** al 31 dicembre. Unità: la persona, non la famiglia (la Corte ha bocciato il cumulo dei coniugi, sent. 179/1976). I beni dei figli minori sono **attribuiti pro quota ai genitori**, metà ciascuno, non sommati per intero a ciascuno. Dichiarazione annuale **precompilata** con i dati che l'Agenzia ha già (archivio dei rapporti finanziari, catasto, registro delle imprese, quadro RW, CRS).
2. **Quanto.** **1%** sulla parte tra 50 mln e 1 mld; **2%** sulla parte oltre 1 mld.
3. **Meno le imposte sul reddito già pagate.** Dall'imposta si scalano le imposte personali sul reddito pagate nell'anno, definite in legge: IRPEF e addizionali, imposte sostitutive, ritenute a titolo d'imposta, la quota delle holding personali di 01-P19 (parte A e parte B) e le **imposte estere sul reddito** effettivamente pagate e comparabili. Ogni imposta si scala **una sola volta**. Paga quindi solo chi oggi paga poco rispetto al patrimonio.
4. **Valutazione omogenea degli attivi** (art. 3 Cost., lezione tedesca del 1995), con criteri fissati in legge (art. 23):
   - titoli quotati, fondi, depositi: valore al 31 dicembre comunicato dagli intermediari;
   - **società operative non quotate:** il **maggiore** tra il **patrimonio netto rettificato** dell'ultimo bilancio (immobili sociali a valori OMI, partecipazioni a patrimonio netto guardando attraverso le holding) e un **valore reddituale semplificato fissato per legge**. La relazione illustrativa motiva la differenza che resta rispetto al valore di mercato con l'art. 41 e con la mancanza di un mercato (Corte cost. ord. 250/2002);
   - **holding passive** (definizione di 01-P19): si guarda **attraverso**, al valore delle attività che contengono;
   - immobili: **valore OMI** con una regola di scelta nell'intervallo fissata in legge e **prova contraria con perizia**; fino alla riforma del catasto (SF13) non si usa la rendita catastale;
   - polizze vita: valore di riscatto (coordinato con 01-P21);
   - arte, gioielli, barche, auto da collezione sopra 50.000 € per oggetto: valore assicurato o dichiarato, con una regola di prova e controlli;
   - trust: attribuiti al disponente se li controlla, altrimenti ai beneficiari con diritti certi, altrimenti al trust, con la stessa soglia e un'**aliquota proporzionale scritta in legge** pari al 2% sulla parte oltre la soglia;
   - debiti: deducibili solo se reali e legati a beni inclusi.
5. **Esclusioni.** Previdenza complementare e TFR maturati; beni culturali vincolati e aperti al pubblico; **il primo milione** di valore dell'abitazione principale.
6. **Niente doppia imposta.**
   - Si scalano bollo 0,2%, IVAFE e IVIE pagati sui beni inclusi.
   - **Credito per tutte le imposte patrimoniali estere** sui beni inclusi (non solo sugli immobili), nel limite dell'imposta italiana proporzionale su quei beni.
   - L'IMU **non** si scala: è un tributo dei Comuni con un presupposto diverso; la legge lo motiva.
   - Elenco delle convenzioni contro le doppie imposizioni che coprono il patrimonio (art. 22 del Modello OCSE; per la Svizzera, convenzione del 9/3/1976) prima dell'approvazione.
7. **Imprese di famiglia: nessuna esenzione, ma tempo per pagare.** La parte di imposta riferita a partecipazioni di almeno il 10% in società operative in cui la persona lavora si può pagare in **rate fino a 10 anni** con gli interessi legali, o rinviare fino a vendita, donazione o successione, con garanzia sulle quote. È una misura generale, valida per tutte le società operative: un'esenzione delle sole imprese di famiglia richiederebbe un'analisi di aiuti di Stato.
8. **Exit tax per le persone fisiche, scritta in questa legge** (al posto del rinvio a 01-P20, esclusa).
   - **Chi:** i contribuenti dell'imposta, o chi la pagava in uno dei due anni precedenti, che trasferiscono la residenza all'estero **dopo l'entrata in vigore**.
   - **Su cosa:** le plusvalenze latenti delle **partecipazioni qualificate** (art. 67 c. 1 lett. c TUIR) alla data del trasferimento.
   - **Come:** imposta **accertata alla partenza**; verso UE e SEE con scambio di informazioni, e verso la Svizzera per chi vi esercita un'attività economica, riscossione **sospesa senza interessi e senza garanzie** fino alla vendita effettiva; le **minusvalenze successive** non riconosciute dallo Stato di arrivo riducono l'imposta (CGUE C-9/02 *de Lasteyrie du Saillant*, C-470/04 *N*, C-581/17 *Wächtler*). Verso gli altri Paesi si paga, anche in **5 rate annuali**: l'art. 64 TFUE non copre una norma nuova.
   - **Coordinamento** con l'exit tax minima di 01-P19 (punto 11): le stesse riserve non pagano due volte.
9. **Presunzione di residenza solo relativa e limitata.** Chi si trasferisce in uno Stato della lista dei regimi fiscali privilegiati, **che non scambia informazioni con l'Italia e con cui non c'è una convenzione che copre il patrimonio**, si presume residente ai fini di questa imposta per **non più di 5 anni**, con **prova contraria effettiva**, e solo per i trasferimenti successivi all'entrata in vigore (modello art. 2 c. 2-bis TUIR).
10. **Controlli.** Criteri di residenza del d.lgs. 209/2023 applicati dall'unità grandi patrimoni di 01-P23; dati CRS e DAC; norma antielusione, con prova contraria, per i trasferimenti di beni a familiari non residenti o a entità estere nei mesi prima della data di valutazione (periodo fissato in legge).
11. **Gestione e tempi.** Unità dell'Agenzia per i grandi patrimoni (con 01-P23), valutatori, sistema informatico Sogei; accertamento per 5 anni; adesione e interpello preventivo per le valutazioni delle imprese. **Prima applicazione:** patrimonio al 31/12/2028, versamento nel 2029; la legge entra in vigore prima. **Valutazione** dopo 3 anni del Dipartimento delle finanze, sentito l'UPB, su gettito, residenze, investimenti e imprese. **Clausola di salvaguardia** nella legge, perché il gettito copre spese permanenti (condizione del giurista su FN12).

**Varianti**

| Variante | Contenuto | Costo di attuazione 2027 / 2028 / 2029 / regime | Intensità | Gettito (copertura) |
|---|---|---|---|---|
| ESSENZIALE | Punti 1-11: imposta minima **1%** oltre 50 mln e **2%** oltre 1 mld, meno le imposte sul reddito pagate; valutazione omogenea; credito per le imposte patrimoniali estere; rate o rinvio per le quote d'impresa; exit tax per le persone fisiche nella legge | 0,005 / 0,015 / 0,02 / **0,02** (2029) | 0,45 | **FN12: 0,3-1,5** a regime (2030), primo versamento 2029; paga 01-P25 ESSENZIALE |
| ZERO | Solo **misura**: registro statistico con dichiarazione patrimoniale annuale sopra 10 mln, precompilata, senza imposta; statistica ufficiale dei grandi patrimoni con 01-P23; adesione dell'Italia allo standard G20 di imposta minima effettiva sui miliardari e sostegno a un registro europeo degli attivi; decisione rinviata al 2029 con i dati | 0,002 / 0,005 / 0,005 / **0,005** | 0,1 | nessuna |

**Motivazione delle intensità.**
- **ESSENZIALE 0,45:** colpisce circa 2.100 persone, ma tra loro c'è circa il 40% della base di un'imposta sopra 5 mln; lo scomputo delle imposte sul reddito la concentra su chi oggi paga meno, cioè sul problema della diagnosi equità. Non ha progressività tra 5 e 50 mln.
- **ZERO 0,1:** nessun effetto sull'equità; costruisce la base informativa e la posizione internazionale. In gran parte coincide con 01-P23: se 01-P23 è attiva il costo aggiuntivo è quasi nullo.

**Costi.** Stima GovernAI della bozza: unità grandi patrimoni, valutatori, IT Sogei per la precompilata. L'exit tax e la presunzione di residenza sono gestite dalla stessa unità: nessun costo aggiuntivo contato.

**Gettito: FN12 rifatta senza 01-P20** (`benchmark/finale_coperture_patrimoniale.csv`).
- La bozza stimava **0,6-2,0** a regime con l'exit tax di 01-P20, che non c'è più.
- I tre valutatori del panel (`benchmark/panel_patrimoniale_*_cop.csv`) la giudicano troppo alta: base tutta sopra 50 mln, la più mobile; erosione per residenza oltre il 5-15% stimato; credito più alto con 01-P19 attiva. Stime: **A** "plausibile sotto 0,6"; **B** 0,3-1,5; **C** 0,3-1,5.
- **Valore finale, prudente: 0,3-1,5**, primo versamento nel **2029**, pieno dal **2030**. L'exit tax ora scritta in questa legge riduce l'erosione per residenza, ma **la stima non è stata alzata**: resta al livello dei valutatori senza exit tax. Il minimo tiene conto anche delle imposte di 01-P19 (parti A e B) che si scalano dall'imposta.

**Articolato normativo essenziale** (disegno di legge collegato alla manovra)

> **Art. 1 (Imposta minima sui grandi patrimoni).** 1. È istituita un'imposta annuale sul patrimonio netto delle persone fisiche residenti nel territorio dello Stato, ovunque detenuto, al 31 dicembre di ciascun anno, per la parte eccedente 50 milioni di euro. 2. L'imposta si applica con l'aliquota dell'1 per cento sulla parte da 50 milioni a 1 miliardo di euro e del 2 per cento sulla parte eccedente 1 miliardo di euro. 3. I beni dei figli minori sono attribuiti a ciascun genitore per la metà.
>
> **Art. 2 (Base e valutazione).** 1. Il patrimonio netto è la somma dei beni e dei diritti di contenuto economico, al netto dei debiti effettivi relativi a beni inclusi. 2. I beni sono valutati: a) gli strumenti quotati, le quote di organismi di investimento e i depositi al valore al 31 dicembre; b) le partecipazioni in società non quotate che esercitano un'attività d'impresa effettiva al maggiore tra la quota del patrimonio netto risultante dall'ultimo bilancio approvato, rettificato con la valutazione degli immobili ai sensi della lettera d) e delle partecipazioni ai sensi della presente lettera e della lettera c), e il valore reddituale determinato capitalizzando il reddito medio dell'ultimo triennio al tasso fissato dall'allegato alla presente legge; c) le partecipazioni nelle holding personali passive di cui all'articolo [01-P19] in proporzione al valore normale delle attività possedute; d) gli immobili al valore medio delle quotazioni dell'Osservatorio del mercato immobiliare per zona e tipologia, salvo prova di un valore inferiore con perizia giurata; e) i contratti di assicurazione al valore di riscatto; f) i beni mobili di valore unitario superiore a 50.000 euro al valore assicurato o, in mancanza, al valore dichiarato, salvo rettifica dell'ufficio. 3. Sono esclusi le posizioni di previdenza complementare, il trattamento di fine rapporto maturato, i beni culturali vincolati aperti al pubblico e l'abitazione principale fino a 1 milione di euro. 4. I beni in trust sono attribuiti al disponente che ne mantiene il controllo, altrimenti ai beneficiari con diritti certi; in mancanza, il trust è soggetto all'imposta con aliquota del 2 per cento sulla parte eccedente la soglia dell'articolo 1.
>
> **Art. 3 (Crediti).** 1. Dall'imposta si scomputano, una sola volta: a) le imposte personali sul reddito dovute per il periodo d'imposta, comprese le addizionali, le imposte sostitutive, le ritenute a titolo d'imposta e le imposte di cui all'articolo [01-P19]; b) le imposte sul reddito pagate all'estero, comparabili a quelle della lettera a), nei limiti dell'articolo 165 del TUIR; c) l'imposta di bollo di cui all'articolo 13, commi 2-bis e 2-ter, della Tariffa allegata al DPR 642/1972, l'IVAFE e l'IVIE relative ai beni inclusi; d) le imposte patrimoniali pagate all'estero sui beni inclusi, nel limite dell'imposta proporzionalmente riferibile a tali beni.
>
> **Art. 4 (Imprese).** 1. La parte di imposta riferibile a partecipazioni non inferiori al 10 per cento in società che esercitano un'attività d'impresa effettiva, nelle quali il contribuente presta la propria attività, può essere versata in dieci rate annuali con gli interessi legali o sospesa fino alla cessione, alla donazione o alla successione, previa garanzia sulle partecipazioni.
>
> **Art. 5 (Trasferimento della residenza).** 1. Le persone fisiche soggette all'imposta nel periodo d'imposta in corso o in uno dei due precedenti che trasferiscono la residenza fiscale all'estero dopo la data di entrata in vigore della presente legge realizzano, alla data del trasferimento, le plusvalenze sulle partecipazioni di cui all'articolo 67, comma 1, lettera c), del TUIR, determinate in base al valore normale. 2. In caso di trasferimento in uno Stato dell'Unione europea o dello Spazio economico europeo con adeguato scambio di informazioni, o nella Confederazione svizzera quando vi è esercitata un'attività economica, la riscossione è sospesa, senza interessi e senza garanzie, fino al realizzo; le minusvalenze successive non riconosciute dallo Stato di destinazione riducono l'imposta. Negli altri casi l'imposta è versata, a scelta, in cinque rate annuali. 3. Il comma 1 non si applica alle plusvalenze già assoggettate all'articolo [exit tax minima di 01-P19]. 4. Le persone che trasferiscono la residenza in Stati o territori a regime fiscale privilegiato che non assicurano un adeguato scambio di informazioni e con i quali non è in vigore una convenzione relativa alle imposte sul patrimonio si presumono residenti ai fini della presente legge per i cinque periodi d'imposta successivi, salvo prova contraria.
>
> **Art. 6 (Dichiarazione, controlli e valutazione).** 1. Le persone con patrimonio netto superiore a 50 milioni di euro presentano una dichiarazione annuale, predisposta dall'Agenzia delle entrate con i dati in suo possesso. 2. Sono inefficaci ai fini dell'imposta, salvo prova contraria, i trasferimenti di beni a familiari non residenti o a entità non residenti effettuati nei [periodo da fissare] mesi precedenti la data di valutazione. 3. La prima data di valutazione è il 31 dicembre 2028. 4. Dopo tre anni il Dipartimento delle finanze, sentito l'Ufficio parlamentare di bilancio, pubblica una valutazione degli effetti su gettito, residenze, investimenti e imprese. 5. Se il gettito è inferiore alla previsione, si applica la clausola di salvaguardia dell'articolo 17, comma 12, della legge 31 dicembre 2009, n. 196.

Il tasso di capitalizzazione del valore reddituale (art. 2 c. 2 lett. b) e il periodo dell'art. 6 c. 2 sono da fissare in legge: la bozza e il giurista non danno un numero.

**Chi paga.** Circa **2.100 persone** sopra 50 mln (stima GovernAI della bozza), e solo quelle che pagano imposte sul reddito sotto l'1% del patrimonio. **Non paga** il resto della popolazione, né chi ha una casa, un'impresa piccola o media o un risparmio normale, né chi ha un grande patrimonio e paga già imposte sul reddito adeguate.

**Costituzionalità** (verifica del giurista: condizionato, nessuna linea rossa).
- **Art. 53.** Il patrimonio è un indice di capacità contributiva ammesso, nel limite della non arbitrarietà (sent. 111/1997); la progressività si valuta sul sistema (sent. 21/1996).
- **Art. 3.** Un'imposta generale sopra una soglia è più solida di un prelievo di categoria (sent. 116/2013). Valutazione omogenea: patrimonio netto rettificato o valore reddituale minimo per le non quotate, OMI con prova contraria per gli immobili.
- **Art. 23.** Soggetti, base, aliquote e criteri di valutazione in legge; il decreto solo per l'attuazione.
- **Art. 42.** Aliquote dell'1-2% sopra 50 mln, al netto delle imposte sul reddito, non hanno effetto espropriativo.
- **Art. 41.** Giustifica rate e rinvio per le quote d'impresa, non uno scarto senza limiti nella valutazione.
- **Irretroattività** (art. 3 L. 212/2000): prima valutazione al 31/12/2028 con legge già in vigore; exit tax e presunzione solo per i trasferimenti futuri.
- **Art. 81:** FN12 copre spese permanenti solo al valore minimo, con clausola di salvaguardia.

**Diritto UE.**
- **Circolazione dei capitali e stabilimento (artt. 63 e 49 TFUE).** Base mondiale per i residenti e nessuna imposta sui beni mobili dei non residenti; crediti per le imposte estere sul reddito e sul patrimonio trattate come quelle italiane.
- **Exit tax:** sospensione senza interessi e garanzie verso UE, SEE e Svizzera; minusvalenze successive riconosciute (C-9/02, C-470/04, C-581/17). La direttiva ATAD riguarda le società: per le persone è solo un modello.
- **Presunzione di residenza:** solo relativa, limitata ai Paesi senza scambio di informazioni e senza convenzione sul patrimonio, 5 anni al massimo. Dentro l'UE una "coda" sarebbe una restrizione difficile da giustificare: per questo non vale verso UE e SEE.
- **Aiuti di Stato:** rate e rinvio valgono per tutte le società operative: misura generale.
- **Nessuna competenza UE** per un'imposta comune: la ZERO usa G20, OCSE, registro europeo degli attivi, DAC.

**Rischi e mitigazioni.**
- **Base piccola e mobile** (2.100 persone, la cima più mobile). Exit tax nella legge; presunzione di residenza limitata; controlli dell'unità di 01-P23; gettito contato al minimo.
- **Elusione con valutazioni basse** (ricchezza spostata in società non quotate). Patrimonio netto rettificato o valore reddituale minimo; holding passive guardate attraverso; antiabuso sui trasferimenti prima della data di valutazione.
- **Evasione all'estero.** CRS, DAC, quadro RW; nessun condono (01-P12).
- **Imposte sul reddito in crescita con 01-P19.** Più imposte sul reddito vuol dire meno imposta minima: è l'effetto voluto, già nel minimo di FN12.
- **Gettito incerto.** Intervallo largo, minimo prudente, clausola di salvaguardia, valutazione dopo 3 anni.
- **Annuncio e fughe anticipate.** Data di valutazione certa e vicina all'approvazione; exit tax solo per i trasferimenti dopo l'entrata in vigore, quindi la legge va approvata in fretta.

**Indicatori**

| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Statistica ufficiale dei patrimoni sopra 10 e 50 mln (numero, composizione) | non esiste, 2026 | pubblicata ogni anno | serie con 01-P23 |
| Gettito effettivo / gettito statico (tasso di erosione) | n.d. | misurato | stabile o in calo |
| Partenze nette dei contribuenti dell'imposta, con e senza exit tax | n.d. | sotto 0,5% l'anno | sotto 0,5% l'anno |
| Investimenti e occupazione delle imprese dei contribuenti (confronto con imprese simili) | n.d. | nessun calo significativo | nessun calo significativo |
| Aliquota effettiva complessiva del top 0,1% (01-P23) | 32,6-36%, 2015 (stime accademiche) | prima misura ufficiale | in aumento |

**Interazioni con le altre misure (niente doppioni).**
- **01-P25 ESSENZIALE:** la paga questa imposta (scelta del 16/11/2026).
- **01-P19 (holding):** imposte scalate dall'imposta minima; exit tax coordinate; holding passive guardate attraverso.
- **01-P23 (statistica e unità grandi patrimoni):** la ZERO vi si fonde; l'unità di 01-P23 gestisce l'imposta.
- **SF13 (catasto):** finché manca si usano i valori OMI. Nessun effetto sull'IMU.
- **SF14 e 01-P22 (successioni):** prelievo una volta per generazione contro prelievo annuo minimo: gettiti separati.
- **01-P21 (polizze e trust):** valutazione al riscatto e attribuzione dei trust coerenti.
- **01-P20:** esclusa; nessun rinvio.

**Da verificare prima dell'uso pubblico** (dal giurista): testo vigente dell'art. 16 c. 1 lett. b d.lgs. 346/1990 dopo il d.lgs. 139/2024; articoli sul patrimonio delle convenzioni italiane; testo vigente dell'art. 166 e dell'art. 2 c. 2-bis TUIR; BVerfG 2006 (2 BvR 2194/99).

---

*Scheda aggiunta il 16 novembre 2026 (scelte di chi guida il progetto, verifica giuridica, panel indipendente). Fonte: `benchmark/finale_proposta_neutralita.md`.*

## 01-P25 — Imprese di persone come le SRL: chi lascia gli utili in azienda paga il 24%, chi li porta a casa paga come persona

### Perché

**Problema in un dato.** Due imprese con lo stesso utile di 1.000.000 di euro, lasciato tutto in azienda per investire, oggi pagano imposte molto diverse:
- **SRL: 27,9%** (IRAP e IRES);
- **socio di SNC: 47,3%**, perché paga subito l'IRPEF progressiva su tutto l'utile, anche se non lo preleva (art. 5 TUIR);
- **ditta individuale: 43,4%**.

Fonte: `analisi/chi_paga/neutralita.csv`, con le regole 2026 di `calcola.py`. L'UPB misura una distanza tra le aliquote marginali sugli utili non distribuiti delle due forme che "può raggiungere 19 punti percentuali" ([Memoria sul DDL delega fiscale, luglio 2023, par. 4.3, p. 30](https://www.upbilancio.it/wp-content/uploads/2023/07/Memoria-UPB-DDL-riforma-fiscale.pdf)).

Chi è coinvolto (MEF-DF, a.i. 2024; vedi `analisi/chi_paga/popolazione.md`):
- **892.638** persone hanno come reddito principale una quota di SNC o SAS (reddito medio 41.028 €, aliquota sul dichiarato 23,7%);
- **861.423** sono imprenditori individuali (reddito medio 37.829 €);
- in contabilità ordinaria il reddito medio dell'imprenditore è **58.700 €** ([Sintesi IRPEF a.i. 2024, nota 4](https://www1.finanze.gov.it/finanze/analisi_stat/public/v_4_0_0/contenuti/sintesi_analisi_dati_2024_irpef_iva.pdf));
- le dichiarazioni delle società di persone sono **652.832**, il 2,9% in meno in un anno.

Chi lavora in forma di SNC non può rinviare l'imposta, chi ha una SRL sì. Il risultato è che **la forma giuridica la sceglie il fisco, non l'impresa**.

**Evidenze.**
- **OCSE.** Il sistema fiscale ideale è neutrale rispetto alla nascita, alla forma e alla crescita delle piccole imprese, ma molti Paesi spingono a costituire società di capitali per pagare meno ([OECD, *Taxation of SMEs in OECD and G20 Countries*, Tax Policy Studies n. 23, 2015](https://doi.org/10.1787/9789264243507-en)).
- **Italia, delega del 2014.** La L. 23/2014, art. 11 c. 1 lett. a, chiedeva già un'imposta proporzionale sugli utili trattenuti dalle imprese IRPEF. La delega è scaduta il 27/6/2015 senza essere attuata (dossier Camera AC 4127-bis, art. 68, p. 348-349).
- **Italia, IRI 2017-2018.** Era il precedente diretto (ex art. 55-bis TUIR, L. 232/2016, c. 547-548): un'**opzione** per imprenditori individuali, SNC e SAS in contabilità ordinaria, 24% sugli utili trattenuti, prelievi deducibili e tassati con l'IRPEF, contributi come prima ([dossier Camera AC 4127-bis, art. 68](https://documenti.camera.it/leg17/dossier/pdf/ID0026s1.pdf)).
- **Italia, delega del 2023.** Ripropone lo stesso schema (DDL delega, art. 5 c. 1 lett. g; numerazione nella L. 111/2023 da verificare). Il regime non risulta attuato (**da verificare** sui decreti attuativi e sul testo unico d.lgs. 117/2026).
- **Germania.** Il §34a EStG prevede un'aliquota ridotta sugli utili non prelevati delle imprese di persone (citato dal giurista come modello).

### Cosa insegna la storia dell'IRI

1. **Il costo era vero e noto.** La relazione tecnica (RT) alla L. 232/2016 stimava −1.212,1 mln nel 2017, −1.231,3 nel 2018, −1.255,8 dal 2019 di competenza e **−1.986,6 mln di cassa nel 2018** (saldo più acconto); il Servizio Bilancio lo giudicava forse **sottostimato** ([Verifica delle quantificazioni AC 4127-bis](https://documenti.camera.it/leg17/dossier/Testi/VQ4127.htm)).
2. **Rinviata per fare cassa** dalla L. 205/2017, c. 1063 ([lavoce.info](https://lavoce.info/archives/49647/iri-buona-riforma-rinviata-far-cassa/)).
3. **Abrogata prima di partire, con effetto retroattivo**, dalla L. 145/2018, art. 1 c. 1055, "in deroga all'articolo 3 della legge 27 luglio 2000, n. 212" ([dossier Camera L. 145/2018, vol. III, p. 1267-1268](https://documenti.camera.it/Leg18/Dossier/Pdf/ID0006i_vol_III.Pdf)).
4. **Problemi tecnici rimasti aperti:** riserve formate prima del regime, perdite, uscite dal regime, prelievi mascherati.

**Lezioni applicate qui:** costo dichiarato per intero anno per anno e coperto prima (con FN12); clausola di stabilità scritta nello Statuto del contribuente; antiabuso sui prelievi mascherati e tassazione delle riserve all'uscita, perché il 24% sia un **rinvio** e non un'esenzione; regole transitorie per riserve e perdite.

### Come (ESSENZIALE)

Il regime si scrive come **articolo nuovo e completo** nel testo unico delle imposte sui redditi (d.lgs. 117/2026, numerazione da verificare), **con deroga espressa all'imputazione per trasparenza dell'art. 5 TUIR solo per chi opta**. **Non rinvia all'art. 55-bis TUIR**, abrogato dalla L. 145/2018: le sue regole e quelle di uscita del DL 50/2017, art. 58 (contenuto da verificare) servono solo da modello e sono riscritte.

1. **Chi.** Imprenditori individuali, SNC e SAS in **contabilità ordinaria**, anche per scelta di chi oggi è in semplificata. Opzione **per cinque periodi d'imposta**, rinnovabile, esercitata in dichiarazione. **I forfettari restano fuori** (L. 190/2014). Il regime è aperto anche alle **stabili organizzazioni in Italia di imprenditori UE** (libertà di stabilimento).
2. **Cosa paga l'impresa.** L'utile che resta nell'impresa paga il **24%** (aliquota IRES, art. 77 TUIR) **fino a 100.000 € l'anno per socio o imprenditore**; oltre il tetto, IRPEF ordinaria come oggi. I familiari che non lavorano nell'impresa contano con il titolare: la legge dice chi sono e a quale scopo, e coordina la regola con l'impresa familiare (art. 5 c. 4 TUIR). I prelievi si deducono dalla base e pagano l'**IRPEF progressiva**. Chi preleva tutto paga come oggi; chi lascia in azienda fino al tetto paga come una SRL.
3. **Contributi INPS invariati.** Si calcolano sull'intero reddito d'impresa, come nell'IRI (comma della L. 232/2016 da verificare). Nessuna pensione più bassa.
4. **Regole transitorie per le riserve: due conti.** Un conto per le **riserve al 24%** formate nel regime e uno per le **riserve già tassate con l'IRPEF** (formate prima dell'opzione o oltre il tetto). I prelievi dal secondo conto non si tassano di nuovo e non si deducono. **Ordine legale dei prelievi:** prima gli utili dell'anno, poi le riserve al 24%, poi quelle già tassate; è la stessa logica della presunzione dell'art. 47 c. 1 TUIR. Il prospetto in dichiarazione tiene i due conti.
5. **Regole transitorie per le perdite.**
   - Le perdite formate **prima dell'opzione** restano ai soci (art. 8 TUIR) e non riducono la base al 24%: niente perdite "da IRPEF" usate contro un reddito al 24%.
   - Le perdite formate **nel regime** si riportano senza limiti di tempo; all'uscita riducono prima le riserve considerate prelevate, poi passano ai soci per quota.
6. **Niente rinvio infinito.** In questi casi le riserve al 24% si considerano **prelevate** e pagano l'IRPEF, con **credito del 24%** già pagato:
   - uscita dal regime;
   - cessione o cessazione dell'impresa;
   - morte dell'imprenditore o del socio senza continuazione da parte degli eredi.

   In caso di **trasformazione in società di capitali**, le riserve al 24% diventano riserve di utili della società e pagano il 26% quando sono distribuite, come per tutte le SRL. Con la continuazione degli eredi le riserve passano con il credito.
7. **Prelievi mascherati.** Beni dell'impresa in uso a soci e familiari, prestiti e garanzie a loro favore si **presumono prelievo**, salvo restituzione entro 12 mesi, corrispettivi di mercato o altra prova contraria. La regola è **coordinata con l'art. 85 c. 2 TUIR** (beni destinati al consumo personale o familiare) e **con l'art. 67 c. 1 lett. h-ter TUIR** (beni in godimento ai soci): lo stesso beneficio non si tassa due volte.
8. **Concordato preventivo biennale.** La legge dice come si applica il 24% alla parte trattenuta del reddito concordato (**da verificare** con l'Agenzia).
9. **Interpello** (art. 11 L. 212/2000) per chi è in dubbio.
10. **Decorrenza.** Dal periodo d'imposta 2028; acconti 2028 con le regole previgenti, primo effetto di cassa nel 2029. Il regime è favorevole e opzionale: l'art. 3 dello Statuto non pone problemi.
11. **Clausola di stabilità.** Inserita nello **Statuto del contribuente**, come nuovo comma dell'art. 3 o dell'art. 10, così si può derogare solo espressamente (art. 1 c. 1 Statuto). Il regime non si può cambiare per periodi d'imposta già iniziati né per opzioni già esercitate, se non a favore del contribuente. **Regola di uscita:** se il regime cambia, le opzioni in corso arrivano alla scadenza del quinquennio, oppure il contribuente esce con le riserve tassate al 24% più il credito, senza aggravi. Lo Statuto non ha rango costituzionale (l'IRI fu abrogata proprio "in deroga all'articolo 3"): la clausola rafforza l'affidamento delle opzioni in corso, che è la tutela concreta.
12. **Solo insieme a 01-P24 ESSENZIALE.** La legge che introduce il regime indica la copertura anno per anno (art. 81 Cost.; art. 17 L. 196/2009): l'imposta minima sui grandi patrimoni (FN12) e, per la parte che FN12 non copre nel caso prudente, le coperture del paragrafo "Saldo".

### Che cosa (varianti)

| Variante | Contenuto | Costo 2027 / 2028 / 2029 / regime (2033) | Intensità | Copertura |
|---|---|---|---|---|
| ESSENZIALE | Punti 1-12: 24% fino a **100.000 €** l'anno di utile trattenuto per socio o imprenditore; oltre, IRPEF ordinaria | 0,002 / 0,01 / **1,26** / **0,63** | 0,55 | **FN12** (01-P24 ESSENZIALE), più altre coperture nel caso prudente |
| ZERO | Microsimulazione ufficiale del Dipartimento delle finanze che aggiorna la RT del 2017 con i dati 2024-2026 (platea in ordinaria, utili trattenuti, effetto del tetto); pubblicazione dei risultati; decisione nella legge di bilancio 2030 con i dati; nessun cambio di imposta | 0 | 0,1 | nessuna |

I costi sono valori centrali e comprendono l'attuazione (0,002 nel 2027, 0,01 dal 2028: modelli, prospetto dei due conti di riserva, controlli sui prelievi mascherati, sistemi Sogei; stima GovernAI della bozza).

**Perché non c'è la PIENA.** Scelta di chi guida il progetto: il 24% senza tetto costerebbe circa 1 mld l'anno a regime e 2 mld nel 2029 (bozza), troppo per una copertura sola.

**Perché non c'è una PILOTA.** Un'imposta non si sperimenta su un campione di imprese senza violare l'art. 3 Cost.; una versione temporanea per tutti avrebbe il difetto che ha rovinato l'IRI.

**Motivazione delle intensità.**
- **ESSENZIALE 0,55.** Per la grande maggioranza delle imprese di persone la parità è piena: il reddito medio dei soci è 41.028 € e quello degli imprenditori in ordinaria 58.700 €. Non lo è per le più grandi, che oltre 100.000 € trattenuti restano all'IRPEF.
- **ZERO 0,1.** Nessun effetto sulla parità, ma costruisce i dati che oggi mancano.

### Quanto costa, anno per anno

**Metodo** (stima GovernAI della bozza; funzione `profilo_costo_a` in `analisi/chi_paga/neutralita.py`; verificata dal panel: "1,256 x fattori x 1,64").
- **Base.** RT 2017: 1,256 mld di competenza a regime, aggiornata per platea (0,80-1,00), aliquote 2026 (0,95-1,05) e crescita al 2028 (1,06-1,10).
- **Rientro del rinvio.** Ogni anno si preleva il 5-10% delle riserve al 24%, che pagano allora l'IRPEF meno il 24% già versato (**da verificare**: secondo un valutatore questa ipotesi da sola riduce il costo a regime di un terzo).
- **Cassa.** Nel primo anno di cassa il costo è 1,64 volte quello di competenza (saldo più acconto, come nella RT).
- **Tetto di 100.000 €.** La ESSENZIALE costa il 50-70% del 24% senza tetto. È un'ipotesi: la distribuzione degli utili trattenuti non è pubblicata. **Da rifare con la microsimulazione del DF** (la ZERO è anche il primo passo della ESSENZIALE).

**Profilo di cassa della ESSENZIALE, minor gettito** (mld; più 0,01 di attuazione dal 2028):

| | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 (regime) |
|---|---|---|---|---|---|---|---|
| Basso | 0 | 0 | 0,83 | 0,46 | 0,41 | 0,37 | 0,33 |
| Alto | 0 | 0 | 1,66 | 0,98 | 0,96 | 0,93 | 0,91 |
| Centrale | 0 | 0 | 1,25 | 0,72 | 0,69 | 0,65 | 0,62 |
| **Con attuazione (centrale)** | **0,002** | **0,01** | **1,26** | **0,73** | **0,70** | **0,66** | **0,63** |

I valori centrali del 2029 e del 2033 sono quelli della bozza; quelli del 2030-2032 sono il punto medio dell'intervallo. Il panel avverte che l'intervallo alto non comprende il rialzo da comportamento (semplificati che passano in ordinaria, più utili trattenuti), segnalato come sottostima già nel 2016.

### Saldo: chi paga la ESSENZIALE

**La paga la patrimoniale minima 01-P24 ESSENZIALE** (FN12: **0,3-1,5** mld l'anno, primo versamento nel 2029, pieno dal 2030; stima prudente dei valutatori, `benchmark/finale_coperture_patrimoniale.csv`). Il motore conta il valore minimo e, per la gradualità, la metà nel 2029.

| mld | 2029 | 2030 | 2033 (regime) |
|---|---|---|---|
| Costo 01-P25 ESSENZIALE con attuazione (basso - alto) | 0,84 - 1,67 | 0,47 - 0,99 | 0,34 - 0,92 |
| FN12 contata dal motore (minimo prudente) | 0,15 | 0,3 | 0,3 |
| FN12 (intervallo) | 0,15 - 0,75 | 0,3 - 1,5 | 0,3 - 1,5 |
| **Da coprire in più nel caso prudente** (costo alto, FN12 minima) | **circa 1,5** | **circa 0,7** | **circa 0,6** |
| Da coprire in più con valori centrali (costo centrale, FN12 centrale 0,9; 0,45 nel 2029) | circa 0,8 | nulla | nulla |

**Che cosa vuol dire.** Con valori centrali, dal 2030 FN12 basta a pagare 01-P25. Nel 2029, primo anno di cassa con saldo più acconto, e in ogni anno nel caso prudente, **FN12 da sola non basta**. Come chiede il giurista (art. 81), la legge indica per ogni anno le coperture della differenza. Le più vicine per tema, se non già usate nello scenario, sono quelle sulle agevolazioni alle imprese a bassa addizionalità (bozza): **SF10** (iperammortamento non qualificato, 0,2-0,4), **SF16** (patent box, 0,2-0,24), **SF04** (cooperative grandi, 0,05-0,15). In alternativa, decorrenza della regola spostata al periodo d'imposta 2029, così il primo anno di cassa (2030) coincide con FN12 piena. Nel programma l'ottimizzatore copre comunque l'intero costo con le coperture disponibili; il legame con 01-P24 assicura che 01-P25 non entri senza la patrimoniale minima.

### Chi ci guadagna e chi paga

**Aliquota effettiva di sole imposte, utile lasciato tutto in impresa** (`analisi/chi_paga/neutralita.csv`; regole 2026; al netto dei contributi; in parentesi imposte più contributi). Nella ESSENZIALE il 24% vale fino a 100.000 € trattenuti per socio.

| Reddito lordo | Socio di SNC oggi | Socio di SNC con il 24% senza tetto | Ditta individuale oggi | Ditta con il 24% senza tetto | SRL (utili nella società) |
|---|---|---|---|---|---|
| 50.000 | 24,7 (49,2) | 21,6 (46,1) | 20,6 (45,1) | 18,1 (42,6) | 27,3 |
| 100.000 | 30,3 (55,2) | 21,9 (46,8) | 26,4 (51,3) | 18,0 (42,9) | 27,6 |
| 1.000.000 | 47,3 | 27,2 senza tetto; **45,1 con il tetto della ESSENZIALE** | 43,4 | 23,3 senza tetto | 27,9 |

Fino a 100.000 € di utile trattenuto la ESSENZIALE coincide con il 24% senza tetto. Se l'imprenditore preleva tutto, **nulla cambia** (caso di prova 1 di `neutralita.py`).

- **Guadagna** chi ha un'impresa di persone in ordinaria, guadagna oltre circa 50.000 € e lascia utili in azienda. Secondo la RT 2017 conviene a circa 2 imprese in ordinaria su 3, con un risparmio medio di 4.000-5.000 € l'anno (da aggiornare: il numero di imprese è sceso).
- **Sotto i 28.000-35.000 €** di reddito il 24% non conviene: per questo il regime è un'opzione e nessuno ci perde.
- **Paga** chi ha patrimoni oltre 50 mln e paga poche imposte sul reddito rispetto al patrimonio, con l'imposta minima di 01-P24 ESSENZIALE.
- **La SRL non cambia.** Chi tiene fermi nella holding i dividendi della propria SRL è regolato dalla parte B di 01-P19.

**Due asimmetrie che restano** (non fanno parte della proposta e si dichiarano): l'**IRAP** (le persone fisiche ne sono esenti dal 2022, le SNC no: dopo la regola la ditta che trattiene paga il 23,3% contro il 27,9% della SRL) e i **contributi** (chi ha un'impresa di persone li paga sull'intero reddito; il socio di capitale che non lavora nella società no; danno però una pensione).

### Chi decide e chi attua

- **Decide** il Parlamento con la legge di bilancio, con un articolo nuovo nel testo unico delle imposte sui redditi (d.lgs. 117/2026; numerazione **da verificare**) e un nuovo comma dello Statuto del contribuente; nella stessa legge l'imposta minima di 01-P24.
- **Attuano** l'Agenzia delle entrate (modelli, prospetto dei due conti di riserva, controlli sui prelievi, interpelli) e Sogei.
- **Il DF** fa la microsimulazione prima della legge e la valutazione dopo 3 anni.
- **L'INPS** non cambia nulla.

### Coordinamento con le altre proposte

- **01-P19 parte B (dividendi fermi nelle holding).** È il secondo lato della neutralità: toglie il vantaggio opposto a chi ha una SRL e una holding. Gettito in FN13 e FN14, separato.
- **01-P24 ESSENZIALE.** La paga (FN12); vincolo nell'ottimizzatore.
- **01-P22 (eredità).** Le quote di SNC e le ditte passate a figli e coniuge restano esenti per la parte operativa (art. 3 c. 4-ter TUS); la liquidità accumulata al 24% oltre il 20% dell'attivo o un anno di costi è un attivo passivo anche per 01-P22: stesso trattamento per SNC e SRL. Alla morte senza continuazione le riserve al 24% si considerano prelevate.
- **Forfettari.** Restano fuori. Per chi cresce e trattiene utili, il regime rende un po' meno caro lasciare il forfettario per l'ordinaria.
- **01-P23 (statistica).** Il prospetto dei due conti alimenta la statistica sulle aliquote effettive.

### Costituzionalità e diritto UE (verifica del giurista: condizionato, nessuna linea rossa)

- **Art. 53.** Con il credito del 24% sulle riserve considerate prelevate all'uscita, alla cessione e alla morte senza continuazione, il 24% è un rinvio e non un'esenzione. La progressività si chiede al sistema nel suo insieme, e il reddito torna all'IRPEF quando esce dall'impresa.
- **Art. 3.** Toglie una disparità tra forme giuridiche che non ha ragioni economiche ed è opzionale: nessuno sta peggio. Il tetto di 100.000 € per socio è un criterio oggettivo e ragionevole come gradualità.
- **Art. 23.** Tetto, gruppo familiare, conti di riserva, ordine dei prelievi, perdite e presunzioni sono in legge.
- **Art. 81.** Coperture indicate anno per anno: FN12 e, per la differenza, le coperture del paragrafo "Saldo".
- **Affidamento** (artt. 3 e 10 L. 212/2000). Regime favorevole e futuro; clausola di stabilità nello Statuto con salvezza delle opzioni in corso.
- **Aiuti di Stato.** Aperta a tutte le imprese IRPEF in contabilità ordinaria, scelta disponibile a tutti, e allinea l'aliquota all'IRES: nella Comunicazione 2016/C 262/01 la neutralità tra forme è la logica del sistema. Rischio basso. Aperta alle stabili organizzazioni di imprenditori UE.

### Rischi principali e mitigazioni

| Rischio | Mitigazione |
|---|---|
| **Costo sottostimato** (aliquota implicita bassa nella RT, più utili trattenuti, più imprese in ordinaria) | Tetto di 100.000 €; microsimulazione del DF prima della legge; valutazione dopo 3 anni |
| **Primo anno di cassa pesante** (1,26 nel 2029, centrale) mentre FN12 parte a metà | Coperture anno per anno nella legge; in alternativa decorrenza al 2029 |
| **FN12 piccola e fragile** (2.100 contribuenti molto mobili) | Copertura contata al minimo (0,3); exit tax nella legge di 01-P24; coperture aggiuntive indicate |
| **Consumo personale nell'impresa al 24%** | Punti 4, 6 e 7: prelievi presunti, ordine dei prelievi, riserve tassate all'uscita |
| **Abrogazione o rinvio come nel 2017-2018** | Clausola di stabilità nello Statuto con regola di uscita; copertura nella stessa legge |
| **Complessità per le piccole imprese** | Solo opzione; nessun adempimento per chi preleva tutto o resta forfettario |

### Indicatori

| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Imprese di persone in ordinaria che optano per il 24%, utili trattenuti | 0 nel 2027 (RT 2017: 280.000 imprese potenziali) | pubblicato | serie annuale |
| Patrimonio netto delle imprese di persone in ordinaria | da rilevare (DF, Redditi SP) | in crescita | in crescita |
| Trasformazioni da SNC o ditta a SRL per motivi fiscali | da rilevare (Registro imprese) | in calo | in calo |
| Distanza di aliquota effettiva tra SNC e SRL sugli utili trattenuti, a 100.000 € | 2,7 punti (30,3 contro 27,6), 2026 | SNC non oltre la SRL (21,9 contro 27,6 con il 24%) | stabile |

### Da verificare prima dell'uso pubblico

- L. 232/2016: comma esatto sui contributi IRI; contenuto dell'art. 58 DL 50/2017;
- numerazione degli articoli nel testo unico d.lgs. 117/2026;
- orientamento della Corte costituzionale sul rango dello Statuto (estremi);
- regola per il concordato preventivo biennale, con l'Agenzia;
- ipotesi di rientro del 5-10% l'anno delle riserve al 24%, sul testo della RT 2017.

### Fonti

- L. 11/12/2016 n. 232, art. 1 c. 547-548: [Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2016-12-11;232); L. 27/12/2017 n. 205, art. 1 c. 1063: [Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2017-12-27;205); L. 30/12/2018 n. 145, art. 1 c. 1055: [Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2018-12-30;145).
- Camera, Servizio Bilancio, [Verifica delle quantificazioni AC 4127-bis](https://documenti.camera.it/leg17/dossier/Testi/VQ4127.htm); dossier [AC 4127-bis](https://documenti.camera.it/leg17/dossier/pdf/ID0026s1.pdf) e [Legge di bilancio 2019, vol. III](https://documenti.camera.it/Leg18/Dossier/Pdf/ID0006i_vol_III.Pdf).
- UPB, [Memoria sul DDL delega per la riforma fiscale](https://www.upbilancio.it/wp-content/uploads/2023/07/Memoria-UPB-DDL-riforma-fiscale.pdf), luglio 2023.
- MEF-DF, [Sintesi dei dati IRPEF e IVA a.i. 2024](https://www1.finanze.gov.it/finanze/analisi_stat/public/v_4_0_0/contenuti/sintesi_analisi_dati_2024_irpef_iva.pdf); statistiche per reddito prevalente in `analisi/chi_paga/popolazione.md`.
- OECD, [Taxation of SMEs in OECD and G20 Countries](https://doi.org/10.1787/9789264243507-en), 2015.
- lavoce.info, [Iri: quando una buona riforma è rinviata per far cassa](https://lavoce.info/archives/49647/iri-buona-riforma-rinviata-far-cassa/).

### Righe da aggiornare in altri file (per il coordinatore)

- `motore/proposte.csv`: riga 01-P25 del blocco in testa; riga 01-P24 da `benchmark/finale_proposta_patrimoniale.md`; riga 01-P19 con costo `0.011,0.016` (attuazione della parte B; titolo invariato).
- `programma/coperture_menu.csv`: FN13 e FN14 da `benchmark/finale_coperture_holding.csv` (legate a 01-P19), FN12 da `benchmark/finale_coperture_patrimoniale.csv`; FN11 non entra (niente PIENA di 01-P24).
- `programma/ottimizza.py`: i legami FN12, FN13, FN14 e `01-P25:ESSENZIALE → 01-P24:ESSENZIALE` sono già scritti.
- `programma/quattro_domande_01_03.yaml`: blocchi 01-P19, 01-P24, 01-P25 da `benchmark/finale_quattro_domande.yaml`.
