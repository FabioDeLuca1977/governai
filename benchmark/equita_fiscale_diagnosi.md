*Bozza scritta da un agente AI il 16 novembre 2026; da valutare con il panel e da approvare; non rivista da una persona.*

# Equità fiscale: chi paga davvero, e come fanno i redditi più alti a pagare meno in modo legale

**Domanda di partenza** (chi guida il progetto, in sintesi): come impedire evasione ed elusione per arrivare a una tassazione equa, dato che chi è ricco "si fa la holding" e con strumenti legali paga meno, mentre paga tutto solo chi non può scegliere.

**Perimetro.** Questo documento tratta la parte fiscale: evasione ed elusione. La corruzione è trattata da un altro agente. Le proposte sono in `benchmark/bozza_proposte_equita_fiscale.md`.

**Convenzioni.** Importi in miliardi di euro (mld) salvo diversa indicazione. "Stima GovernAI" vuol dire stima propria, senza quantificazione ufficiale. "Da verificare" vuol dire dato o norma non riscontrati sul testo originale.

---

## 1. La risposta breve

1. **Evasione ed elusione sono due problemi diversi, con due "geografie" diverse.**
   - **L'evasione (illegale)** è concentrata dove il fisco non ha un terzo che trattiene l'imposta: lavoro autonomo e piccola impresa, IVA, IMU. Nel 2023 il gap tributario è di **98,7-100,1 mld**. La voce più grande è l'IRPEF di autonomi e imprese: **38,4 mld, il 59,7% dell'imposta dovuta**. Sul lavoro dipendente regolare la propensione è sotto il **2,3%**.
   - **L'elusione e la pianificazione legale** sono concentrate in alto. Chi ha redditi da capitale e patrimoni grandi può scegliere **la forma** del reddito (dividendo, plusvalenza, utile trattenuto in società), **il momento** in cui tassarlo (anche mai) e **il contenitore** (holding, polizza, trust). Chi vive di stipendio o pensione non può scegliere nulla.
2. **Il risultato si vede nei numeri.** Gli studi sui conti nazionali distributivi trovano un sistema fiscale italiano **progressivo fino al 93°-95° percentile e regressivo sopra**: il top 0,1% paga in media il **32,6-36%** di tutte le imposte sul proprio reddito, meno di quanto pagano molte famiglie del ceto medio (Guzzardi et al. 2024; Dalle Luche et al. 2026, dati 2015).
3. **Il canale più potente è il più semplice: la holding personale.** Un dividendo incassato da una persona paga il **26%**. Lo stesso dividendo incassato da una società holding della stessa persona paga l'**1,2%** (95% esente, il resto all'IRES del 24%). Il 26% si paga solo quando la holding distribuisce: si può rinviare per decenni. E alla morte del socio il costo fiscale delle quote si "rivaluta" al valore dichiarato in successione: in caso di liquidazione o recesso l'imposta rinviata può non arrivare mai.
4. **La lezione francese.** La Francia ha introdotto nel 2025 un'imposta minima del 20% sui redditi molto alti (CDHR). Attesa: 1,9 mld. Incassata nel 2025: circa **0,4 mld**, anche perché chi poteva ha trattenuto i dividendi nelle società. **Un'imposta minima sui soli redditi incassati non funziona se gli utili restano nella holding.** Per questo la Francia nel 2026 ha aggiunto una tassa sulle holding patrimoniali.
5. **Cosa propone GovernAI** (vedi le schede): neutralità tra possedere direttamente e possedere tramite holding passive (01-P19); una scala sui redditi finanziari molto alti che lascia invariato il piccolo risparmio (01-P20); fine dei "contenitori" che servono solo a rinviare o non pagare (polizze senza rischio assicurativo, trust opachi: 01-P21); eredità di patrimoni passivi trattati come patrimoni e non come imprese (01-P22); e un'unità e una statistica sui grandi patrimoni, perché oggi nessuno sa quanto paga davvero il top 0,1% (01-P23). **Le PMI familiari che lavorano sono protette in modo esplicito in tutte le schede.**

---

## 2. Evasione: dove si concentra (dati ufficiali)

Fonte: MEF, *Relazione sull'economia non osservata e sull'evasione fiscale e contributiva 2026*, tabelle I.1 e I.2 (testo in `dati/raw/01_mef_relazione_evasione_2026.txt`; [mef.gov.it](https://www.mef.gov.it/documenti-pubblicazioni/rapporti-relazioni/)).

| Imposta (2023) | Gap (mln €) | Propensione (gap / imposta dovuta) |
|---|---|---|
| IRPEF lavoro autonomo e impresa | 38.387 | **59,7%** |
| IVA | 34.355 | 20,3% |
| IRES | 11.963 | 19,8% |
| IMU-TASI | 4.908 | 20,8% |
| IRAP | 3.347 | 10,4% |
| IRPEF lavoro dipendente irregolare | 3.003-4.173 | 1,6-2,3% |
| Accise prodotti energetici | 1.132 | 5,7% |
| Locazioni (cedolare e IRPEF) | 773 | 8,6% |
| **Totale tributi** | **98.716-100.095** | **17,1-17,3%** |
| Contributi | 9.205-12.730 | — |

**Lettura.**
- La propensione all'evasione scende: **-2,4 punti dal 2019**. La fatturazione elettronica e i dati di terzi funzionano.
- L'evasione **non** è soprattutto un fenomeno "dei ricchissimi": è diffusa in milioni di piccole posizioni senza un sostituto d'imposta. Questo fronte è già coperto da **01-P3** (IVA in tempo reale), **01-P10** (controlli mirati con garanzie), **01-P11** e **01-P12** (riscossione, niente condoni). Non lo duplichiamo.
- **Evasione dei grandi patrimoni tramite l'estero.** Lo scambio automatico CRS funziona, ma la Relazione 2026 (cap. V.2) mostra i limiti: nel campione analizzato (anno 2018), chi non compila il quadro RW ha **1,9 mld** su conti correnti esteri, con sanzioni potenziali per **68 mln**; per il **45%** delle posizioni manca perfino il codice che dice di che prodotto si tratta. È un'informazione utile ma parziale: riguarda solo i conti correnti, non polizze, trust e partecipazioni.

---

## 3. Chi paga quanto: distribuzione delle imposte

| Dato | Valore | Fonte |
|---|---|---|
| Contribuenti IRPEF con reddito complessivo oltre 300.000 € | **0,2%** del totale; dichiarano il **6,6%** dell'imposta netta (7,1% nel 2023) | MEF-DF, [*Sintesi dati dichiarazioni 2024*](https://www1.finanze.gov.it/finanze/analisi_stat/public/v_4_0_0/contenuti/sintesi_analisi_dati_2024_irpef_iva.pdf) |
| Contribuenti fino a 35.000 € | 76,6% del totale; 34,9% dell'imposta netta | idem |
| Redditi di capitale | "la quasi totalità" è soggetta a imposta sostitutiva e **non compare nell'IRPEF** | idem |
| Aliquota effettiva media su tutte le imposte, top 0,1% | **32,6%** (stima con rendimenti eterogenei), 36% nella stima precedente; regressività dal **93° percentile** | Dalle Luche, Guzzardi, Palagi, Roventini, Santoro, [LEM WP 2024/26](https://www.lem.sssup.it/WPLem/files/2024-26.pdf), poi *Review of Income and Wealth* 2026; Guzzardi et al., *JEEA* 2024; dati 2015 |
| Rendimento medio della ricchezza | **2,5%** per il 90% più povero, **5%** per il 10% più ricco | idem |
| Aliquota sul patrimonio dei miliardari nel mondo | **0-0,5%** del patrimonio l'anno, soprattutto grazie alle holding personali | EU Tax Observatory, [*Global Tax Evasion Report 2024*](https://halshs.archives-ouvertes.fr/halshs-04563948v1/file/global_tax_evasion_report_24.pdf) |

**Cosa vuol dire.** Le statistiche IRPEF **non vedono** proprio i redditi che contano in alto: dividendi, interessi, plusvalenze (imposte sostitutive) e soprattutto gli **utili trattenuti nelle società**. Il 6,6% dell'IRPEF pagato dallo 0,2% più alto dice poco sull'equità del sistema, perché manca la parte più grande del reddito di quel gruppo. Lo stesso limite vale per le stime accademiche: sono ricostruzioni su dati 2015, non conti ufficiali. **Manca una statistica ufficiale delle aliquote effettive per reddito e patrimonio** (proposta 01-P23).

---

## 4. I canali legali con cui i redditi alti pagano meno

### 4.1 Gettito delle imposte sostitutive (per dare la scala)

MEF-DF, [*Bollettino delle entrate tributarie*, gennaio-dicembre 2025](https://www.astrid-online.it/static/upload/boll/bollettino-entrate-dicembre2025.pdf) (n. 286):

| Voce (2025) | mln € |
|---|---|
| IRES | 60.085 |
| Ritenute su utili distribuiti dalle persone giuridiche (dividendi, 26%) | **6.695** |
| Sostitutiva su redditi da capitale e plusvalenze | **6.581** (+98% sul 2024, anno di mercati favorevoli) |
| Sostitutive e ritenute su interessi e altri redditi di capitale (cap. 1026) | 21.055 |
| Cedolare secca sugli affitti | 4.692 |
| Imposta sulle riserve matematiche vita | 2.238 |
| Imposta di successione e donazione | **1.081** |
| Imposta di bollo (comprende lo 0,2% sui prodotti finanziari) | 10.998 |

Ordine di grandezza (stima GovernAI): 6,7 mld di ritenute al 26% corrispondono a circa **25 mld di dividendi** soggetti a ritenuta, compresi quelli pagati a non residenti con aliquote ridotte dai trattati. Il dato **non** comprende i dividendi incassati da società (holding), che non pagano ritenuta.

### 4.2 Canale per canale

| Canale | Come funziona oggi | Chi lo usa | Quanto vale | Già nel programma? |
|---|---|---|---|---|
| **1. Holding personali e casseforti di famiglia** | Dividendi e plusvalenze su partecipazioni incassati da una società: 95% esclusi (art. 89 e art. 87 TUIR, PEX; artt. 96 e 98 del nuovo testo unico d.lgs. 117/2026, **da verificare**). Imposta effettiva **1,2%** (5% × 24%). Il 26% personale si paga solo alla distribuzione. La L. 199/2025 aveva limitato l'esenzione alle partecipazioni ≥5% o ≥500.000 €; il **DL 38/2026** l'ha ripristinata senza soglie dal 1/1/2026 ([Fiscomania](https://fiscomania.com/ripristinata-pex/); conversione **da verificare**) | Famiglie imprenditoriali e grandi patrimoni finanziari | **Non quantificato da nessuna fonte ufficiale.** Il vantaggio è il rinvio di un'imposta del 24,8% sui dividendi (26% - 1,2%), per anni o per sempre (vedi canale 6) | No |
| **2. Redditi finanziari a tassa piatta** | 26% su dividendi, interessi, plusvalenze; 12,5% su titoli di Stato; contro un'IRPEF fino al 43% più addizionali sul lavoro | Tutti i risparmiatori; ma i redditi finanziari sono molto concentrati in alto | Gettito 2025 delle sostitutive: tabella 4.1. Quota pagata da chi ha redditi finanziari molto alti: **non nota** (le ritenute sono anonime) | SF21 (PIR) |
| **3. Plusvalenze tassate solo se realizzate** | Il 26% si paga solo alla vendita. Chi non ha bisogno di vendere rinvia senza limite | Chi ha grandi portafogli e partecipazioni | Non quantificato | No |
| **4. Polizze vita usate come contenitori** (unit-linked, polizze "dedicate", spesso emesse all'estero) | Rendimenti tassati solo al riscatto (26% / 12,5%); somme pagate in caso di morte **escluse dall'imposta di successione** (art. 12 d.lgs. 346/1990) e, per la parte di rischio demografico, dall'IRPEF; bollo 0,2% annuo (prelievo spesso differito: **da verificare** la disciplina vigente). La Cassazione ha più volte riqualificato come prodotti finanziari le polizze senza vero rischio assicurativo (estremi **da verificare**) | Patrimoni finanziari medio-alti e alti | Riserve e flussi per tipo di polizza: dati IVASS/ANIA **da raccogliere**. Imposta sulle riserve vita 2025: 2,2 mld (è un acconto, non un costo per lo Stato) | No |
| **5. Trust** | Trust "opaco": reddito tassato al 24% IRES nel trust; distribuzioni ai beneficiari residenti di norma non tassate se il reddito è già stato tassato. Dal 2020 tassate le distribuzioni da trust esteri in Paesi a fiscalità privilegiata (DL 124/2019, art. 13); circolare AdE 34/E del 20/10/2022. Successione: d.lgs. 139/2024 (opzione per pagare all'apporto) | Grandi patrimoni, pianificazione successoria | Non quantificato | No |
| **6. Successione: rivalutazione del costo e esenzione del controllo** | Gli eredi ricevono le partecipazioni al valore dichiarato in successione (art. 68 c. 6 TUIR): le plusvalenze maturate in vita **non sono mai tassate**. Le partecipazioni di controllo passate a figli e coniuge sono **esenti** se il controllo è tenuto 5 anni (art. 3 c. 4-ter d.lgs. 346/1990), anche quando la società è una holding (risposta AdE n. 152 del 31/7/2026, via [FiscoeTasse](https://www.fiscoetasse.com/approfondimenti/17512-holdiNG-statica-che-non-distribuisce-i-dividendi-e-abuso-del-diritto.html)). Franchigia 1 mln per erede in linea retta, aliquota 4% | Famiglie con grandi patrimoni, anche solo finanziari dentro una holding | Gettito successioni 2025: 1,08 mld (Francia, Germania e Regno Unito: diverse volte di più, **da verificare** le cifre esatte) | **SF14** (franchigia 500.000 €, aliquote 4-7%) |
| **7. Regime dei neo-residenti** | Imposta fissa sui redditi esteri: 100.000 € fino al 10/8/2024, 200.000 € fino al 2025, **300.000 €** per chi opta dal 2026 (L. 199/2025); nessun obbligo RW né IVAFE/IVIE sui beni esteri | Poche centinaia o migliaia di persone molto ricche (circa un migliaio di opzioni nel 2022 secondo fonti di stampa: **da verificare** con il MEF) | Spesa fiscale **74,9 mln/anno** (MEF, *Rapporto spese fiscali 2025*, misura 520, `dati/raw/01_mef_rapporto_spese_fiscali_2025.txt`) | SF20 tratta gli impatriati, non i neo-residenti |
| **8. Cedolare secca** | 21% (10% a canone concordato) invece dell'IRPEF | Proprietari di immobili in affitto | 4,69 mld di gettito 2025 | **SF01, SF11** |
| **9. Forfettario** | 15% fino a 85.000 € di ricavi | Circa 2 milioni di piccole partite IVA: **non** è un canale dei ricchi, ma crea un gradino | — | **SF02** |
| **10. Rendite catastali vecchie** | Valori catastali molto sotto il mercato: IMU, IRPEF sui non locati e imposte di successione e registro calcolate su basi basse | Chi possiede immobili di pregio, soprattutto nei centri storici | — | **SF13** |
| **11. Società di comodo** (strumento di contrasto esistente) | Reddito minimo presunto e IRES maggiorata di 10,5 punti per le società non operative (art. 30 L. 724/1994; DL 138/2011). Una holding che incassa dividendi **di norma supera** il test: lo strumento non colpisce il rinvio | — | — | — |

### 4.3 Un esempio numerico (canale 1)

Una società operativa guadagna 1.000.000 € e li distribuisce tutti. IRES della società operativa: 240.000 €. Restano 760.000 €.

| | Socio persona fisica | Socio = holding di famiglia |
|---|---|---|
| Imposta sul dividendo di 760.000 € | 197.600 € (26%) | 9.120 € (1,2%) |
| Restano da investire | 562.400 € | 750.880 € |
| Prelievo totale sull'utile, oggi | **43,8%** | **24,9%** |
| Quando si paga il resto | — | solo se e quando la holding distribuisce; con la liquidazione dopo una successione, la parte rivalutata non paga |

Per confronto: chi ha un lavoro dipendente da 60.000 € lordi ha un'aliquota marginale IRPEF del 43% più addizionali, più i contributi. Lo stesso euro di reddito in più paga molto di più. **È questo lo scarto che chi ha posto la domanda ha visto.**

Il rinvio non è di per sé un abuso. L'atto di indirizzo MEF del 27/2/2025 sull'abuso del diritto dice che il rinvio conta come vantaggio indebito solo se è "sine die" o molto lungo, e va dimostrato caso per caso (via FiscoeTasse, articolo citato). Le risposte dell'Agenzia vanno in direzioni diverse (n. 215/2022, n. 496/2022, n. 155/2026). **Risultato: incertezza per chi è in buona fede e poco effetto su chi pianifica.** Una regola chiara di legge funziona meglio della clausola generale dell'art. 10-bis L. 212/2000.

---

## 5. Confronto internazionale: cosa funziona

| Strumento | Paese | Come funziona | Risultato, lezione |
|---|---|---|---|
| **Imposta minima sui redditi molto alti** | Francia, *contribution différentielle sur les hauts revenus* (CDHR), dal 2025 | Prelievo minimo del **20%** sul reddito fiscale di riferimento oltre 250.000 € (single) o 500.000 € (coppia) | Attesi 1,9 mld, incassati circa **0,4 mld** nel 2025; prorogata dalla legge di bilancio 2026 fino al ritorno del deficit sotto il 3% con stima ridotta a circa 0,65 mld ([LegiFiscal, 24/3/2026](https://www.legifiscal.fr/actualites-fiscales/4455-contribution-differentielle-hauts-revenus-04-md-recettes-lieu-19-prevu.html); [impots.gouv.fr](https://www.impots.gouv.fr/cdhr-guide); IPP). **Lezione:** i dividendi si possono trattenere nelle società; un minimo sui soli redditi incassati si aggira |
| **Tassa sulle holding patrimoniali** | Francia, loi de finances 2026 (loi n. 2026-103 del 19/2/2026), art. 235 ter C CGI | Il progetto prevedeva il 2% su tutti gli attivi non professionali delle holding sopra 5 mln controllate da famiglie; il testo approvato colpisce al **20%** solo i beni di lusso (yacht, auto, opere d'arte e simili) detenuti dalle holding passive; dagli esercizi chiusi dal 31/12/2026 (dettagli **da verificare** sul testo: [Avnear](https://avnear.fr/blog/structurer/holdings-et-societes-patrimoniales/taxe-holding-2026-conditions-assiette-et-risques-cgi-art-235-ter-c); [LCP](https://lcp.fr/actualites/taxation-des-holdings-patrimoniales-les-deputes-restreignent-la-taxe-prevue-par-le)) | Il Parlamento ha ristretto molto la misura. **Lezione:** distinguere holding "animatrici" (che guidano imprese) da holding passive è possibile e il Conseil constitutionnel l'ha accettato (décision 2026-901 DC, **da verificare**) |
| **Apporto a holding con obbligo di reinvestimento** | Francia, art. 150-0 B ter CGI | Chi conferisce partecipazioni a una holding che controlla rinvia la plusvalenza; se la holding vende entro 3 anni deve reinvestire una quota (60%, soglia in revisione: **da verificare**) in attività economiche | **Modello per la protezione delle PMI**: il rinvio è ammesso se il denaro torna nell'economia produttiva |
| **"Buffett rule" / imposta minima dei miliardari** | Stati Uniti, proposta (non approvata) | 25% minimo su reddito **comprese le plusvalenze non realizzate** per chi ha oltre 100 mln $ di patrimonio; stima del Tesoro circa 500 mld $ in 10 anni (Green Book FY2025, via [Treasury](https://home.treasury.gov/news/press-releases/jy2169); cifra **da verificare** sul Green Book) | Mai approvata; problemi di valutazione e di liquidità. **Lezione:** per funzionare l'imposta minima deve guardare oltre il reddito incassato |
| **Imposta sulle holding personali** | Stati Uniti, *personal holding company tax* (IRC §541) e *accumulated earnings tax* (§531) | 20% sugli utili passivi **non distribuiti** delle società con 5 o meno persone che ne hanno più della metà e con almeno il 60% di redditi passivi | In vigore da decenni; spinge a distribuire. **Modello diretto per 01-P19** |
| **Società chiuse e prestiti ai soci** | Regno Unito: *close investment-holding companies* (niente aliquota ridotta per piccole società: CTA 2010 s. 18N); *loans to participators* (s. 455 CTA 2010: 33,75% sui prestiti ai soci, restituito quando il prestito si chiude) | Impedisce di consumare gli utili della società con prestiti invece che con dividendi | **Modello per 01-P19** (prestiti e beni ai soci) |
| **Società patrimoniali** | Spagna: *entidad patrimonial* (art. 5.2 Ley 27/2014): niente aliquota ridotta e altre limitazioni per le società con più della metà dell'attivo non destinato ad attività economiche. Imposta sul risparmio delle persone **progressiva**: 19%, 21%, 23%, 27%, **30% oltre 300.000 €** (dal 2025) | Distingue società operative e patrimoniali; scala sul risparmio | **Modello per 01-P20** (scala sui redditi finanziari molto alti) |
| **Esenzione dei dividendi tra società solo per partecipazioni rilevanti** | Germania: dal 2013 i dividendi da partecipazioni sotto il 10% sono tassati per intero anche tra società (§8b c. 4 KStG) | Il portafoglio "di investimento" tenuto in una società non gode del 95% | Tentativo italiano simile (L. 199/2025) ritirato dopo due mesi: serve un disegno che non colpisca i gruppi industriali |
| **Successione: niente sconto sui beni passivi** | Germania: le agevolazioni per le imprese escludono il *Verwaltungsvermögen* (attivi passivi: liquidità, titoli, immobili dati in affitto) (§13b ErbStG); la Corte costituzionale (BVerfG, 1 BvL 21/12, 17/12/2014) ha giudicato **incostituzionali** agevolazioni troppo larghe per i grandi patrimoni | Gli eredi mantengono il costo fiscale del defunto (niente rivalutazione gratuita) | **Modello per 01-P22** |
| **Exit tax per le persone fisiche** | Germania, §6 AStG: plusvalenze latenti su partecipazioni ≥1% tassate al trasferimento all'estero; pagamento in 7 rate (riforma 2022) | Nell'UE serve una sospensione senza garanzie onerose (CGUE C-9/02 *de Lasteyrie du Saillant*, C-470/04 *N*) | **Modello per 01-P20** (protezione della base) |
| **Imposta minima globale sulle multinazionali (Pillar 2)** | UE, direttiva 2022/2523; Italia, d.lgs. 209/2023 | 15% minimo per i gruppi con ricavi ≥750 mln | Già recepita. Gettito italiano modesto (imposta minima integrativa circa 49 mln/anno secondo una relazione tecnica citata da [ItaliaOggi](https://www.italiaoggi.it/diritto-e-fisco/minimum-tax-lo-scudo-ocse-salva-le-multinazionali-usa-litalia-si-adegua-j6hdsvvp), **da verificare**); accordo "side by side" in sede OCSE per i gruppi USA. **Non riguarda le persone fisiche** |
| **Registro dei titolari effettivi** | UE, direttive antiriciclaggio; CGUE 22/11/2022, C-37/20 e C-601/20 (*WM e Sovim*): niente accesso pubblico generalizzato | Italia: registro **sospeso** per contenzioso; CGUE 21/5/2026 (C-684/24 e C-685/24) ha dato ragione all'Italia sui mandati fiduciari; d.lgs. 122/2026 su accesso a tre livelli; riapertura **senza data** ([Studio Pizzano](https://www.studiopizzano.it/registro-titolari-effettivi-dlgs-122-2026-scaduti-60-giorni-decreti-mimit-riapertura/); [A&O Shearman](https://www.aoshearman.com/it-it/insights/operation-of-the-register-of-beneficial-owners-have-we-finally-reached-a-turning-point)) | **Lezione:** l'accesso per l'amministrazione fiscale non è in discussione; il ritardo è un problema di attuazione |
| **Scambio automatico (CRS, DAC6-DAC8)** | OCSE e UE | Dati sui conti esteri, sugli schemi transfrontalieri e (DAC8) sulle cripto | Funziona sui conti; non vede bene polizze, trust e partecipazioni non quotate |
| **Grandi patrimoni in adempimento collaborativo e analisi dei gruppi privati** | Australia, ATO *Top 500* e *Next 5,000 private groups*; Regno Unito, HMRC *Wealthy* team | Unità dedicate che guardano insieme persona, società controllate e trust | Esempio per 01-P23 (dati di risultato **da verificare** sui rapporti ATO) |

---

## 6. Strade valutate e non proposte (o rinviate)

| Strada | Perché no, o non ora |
|---|---|
| **Imposta minima sui redditi incassati (modello CDHR)** | In Italia i redditi finanziari incassati pagano già il 26% o il 12,5%: un minimo del 20% morderebbe poco. Il problema è il reddito **non incassato** (utili in holding, plusvalenze latenti). Va prima chiuso il canale holding (01-P19) e costruita la statistica (01-P23). Rivalutare a metà legislatura con i dati |
| **Imposta patrimoniale generale** | È una **scelta politica** che spetta a chi guida il progetto e al Parlamento. Esistono già prelievi patrimoniali parziali (IMU, bollo 0,2% sui prodotti finanziari, IVAFE, IVIE). Lo studio Dalle Luche et al. mostra che un'imposta progressiva dello 0,11-1,5% avrebbe effetti simili a un'IRPEF più alta in cima. **Da sottoporre a chi guida il progetto, non proposta qui** |
| **Abolire l'esenzione del 95% (PEX) per tutti** | Creerebbe doppia tassazione nelle catene di gruppi industriali, colpirebbe le PMI organizzate in gruppo e, per le partecipazioni UE ≥10%, contrasterebbe con la direttiva madre-figlia (2011/96/UE). Il tentativo del 2025-26 è durato due mesi |
| **Alzare il 26% per tutti, titoli di Stato compresi** | Colpirebbe il piccolo risparmio. Linea rossa EQU della Carta |
| **Eliminare il regime dei neo-residenti** | Spesa fiscale piccola (74,9 mln) e già ritoccata due volte (2024, 2026). Si propone solo la trasparenza (01-P23) e il monitoraggio |

---

## 7. Cosa non sappiamo (e serve sapere prima di legiferare)

1. **Quante sono le holding personali passive** e quanto incassano ogni anno in dividendi e plusvalenze esenti. Il Dipartimento delle Finanze ha i dati (quadro RF del modello Redditi SC, variazioni in diminuzione per utili e plusvalenze esenti) ma non li pubblica per tipo di società e di socio.
2. **La distribuzione per persona dei redditi finanziari**: le ritenute sono anonime. L'Archivio dei rapporti finanziari e le segnalazioni degli intermediari permetterebbero di ricostruirla in forma statistica.
3. **L'aliquota effettiva ufficiale per classe di reddito e di patrimonio**, che sommi IRPEF, sostitutive e la quota di imposte societarie e di utili trattenuti. Oggi esistono solo stime accademiche su dati 2015.
4. **Polizze vita**: quanto valgono le riserve delle polizze unit-linked e multiramo con componente di rischio trascurabile, e quante sono emesse da compagnie estere in libera prestazione.
5. **Trust**: quanti trust opachi con beneficiari residenti esistono e quanto patrimonio contengono (dipende dalla riapertura del registro dei titolari effettivi).
6. **Successioni**: quanta parte delle esenzioni dell'art. 3 c. 4-ter riguarda holding passive e quanto valgono le plusvalenze latenti che si annullano con la rivalutazione in successione.

Per questo **tutte le stime di gettito delle proposte sono stime GovernAI con intervalli larghi** e un minimo prudente. La prima azione dei 100 giorni è chiedere al Dipartimento delle Finanze e all'UPB queste elaborazioni (01-P23, variante ZERO, che costa poco e serve comunque).

---

## 8. Fonti principali

- MEF, *Relazione sull'economia non osservata e sull'evasione fiscale e contributiva 2026*, tab. I.1, I.2, cap. V.2 (`dati/raw/01_mef_relazione_evasione_2026.txt`).
- MEF-DF, *Bollettino delle entrate tributarie* n. 286, gennaio-dicembre 2025 ([copia Astrid](https://www.astrid-online.it/static/upload/boll/bollettino-entrate-dicembre2025.pdf)).
- MEF-DF, *Sintesi dati dichiarazioni IRPEF e IVA, anno d'imposta 2024* ([finanze.gov.it](https://www1.finanze.gov.it/finanze/analisi_stat/public/v_4_0_0/contenuti/sintesi_analisi_dati_2024_irpef_iva.pdf)).
- MEF, *Rapporto annuale sulle spese fiscali 2025* (`dati/raw/01_mef_rapporto_spese_fiscali_2025.txt`), misura 520 (neo-residenti).
- Dalle Luche, Guzzardi, Palagi, Roventini, Santoro, *Tackling the regressivity of the Italian tax system*, LEM WP 2024/26 ([pdf](https://www.lem.sssup.it/WPLem/files/2024-26.pdf)); Guzzardi, Palagi, Roventini, Santoro, *Journal of the European Economic Association* 2024.
- EU Tax Observatory, *Global Tax Evasion Report 2024* ([taxobservatory.eu](https://halshs.archives-ouvertes.fr/halshs-04563948v1/file/global_tax_evasion_report_24.pdf)).
- Francia: [impots.gouv.fr, guida CDHR](https://www.impots.gouv.fr/cdhr-guide); [LegiFiscal 24/3/2026](https://www.legifiscal.fr/actualites-fiscales/4455-contribution-differentielle-hauts-revenus-04-md-recettes-lieu-19-prevu.html); loi n. 2026-103 (art. 235 ter C CGI) via [Avnear](https://avnear.fr/blog/structurer/holdings-et-societes-patrimoniales/taxe-holding-2026-conditions-assiette-et-risques-cgi-art-235-ter-c).
- Stati Uniti: Treasury, [Green Book FY2025](https://home.treasury.gov/news/press-releases/jy2169); Internal Revenue Code §§531, 541.
- Regno Unito: Corporation Tax Act 2010, ss. 18N e 455.
- Germania: §8b KStG, §13b ErbStG, §6 AStG; BVerfG 1 BvL 21/12 del 17/12/2014.
- Spagna: Ley 27/2014, art. 5.2; Ley 35/2006 (IRPF), scala della base del risparmio.
- CGUE: C-37/20 e C-601/20 (22/11/2022); C-684/24 e C-685/24 (21/5/2026); C-196/04 *Cadbury Schweppes*; C-9/02; C-470/04.
- Italia, prassi su holding e abuso del diritto: atto di indirizzo MEF 27/2/2025; risposte AdE n. 215/2022, 496/2022, 152/2026, 155/2026 (via [FiscoeTasse, 2/11/2026](https://www.fiscoetasse.com/approfondimenti/17512-holdiNG-statica-che-non-distribuisce-i-dividendi-e-abuso-del-diritto.html)); DL 38/2026 su PEX e dividendi (via [Fiscomania](https://fiscomania.com/ripristinata-pex/)).
