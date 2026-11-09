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
