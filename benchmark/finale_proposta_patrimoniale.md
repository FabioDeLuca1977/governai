*Testo finale scritto da un agente AI il 16 novembre 2026 dopo le scelte di chi guida il progetto ("patrimoniale solo minima"); parte dalla bozza `benchmark/bozza_proposta_patrimoniale.md`, dal panel (`benchmark/panel_patrimoniale_*.csv`) e dalla verifica giuridica (`giuridico/note_patrimoniale.md`, `giuridico/conformita_patrimoniale.csv`); non rivisto da una persona.*

# Scheda finale: imposta minima sui patrimoni molto grandi (01-P24)

Riga per `motore/proposte.csv` (formato `proposta_id,titolo,costo_min,costo_max,costo_opportunita`; costi a regime della ZERO e della ESSENZIALE):

```csv
01-P24,"Grandi patrimoni: un'imposta minima solo sopra 50 milioni, meno le imposte sul reddito già pagate, con exit tax e valutazione uguale per tutti i beni; prima si misura",0.005,0.02,0.0
```

Diagnosi, esperienze estere e fonti: `benchmark/patrimoniale_studio.md`. Varianti: `benchmark/finale_varianti_patrimoniale.csv`. Copertura: `benchmark/finale_coperture_patrimoniale.csv` (solo FN12). Importi in mld €/anno salvo diversa indicazione. "Stima GovernAI" = stima propria senza quantificazione ufficiale; "da verificare" = dato o norma non riscontrati sul testo originale.

**Scelte di chi guida il progetto (16/11/2026).**
- **"Patrimoniale solo minima".** 01-P24 ha solo due varianti: **ESSENZIALE** (imposta minima dell'1% sopra 50 mln e del 2% sopra 1 mld, meno le imposte sul reddito già pagate) e **ZERO** (registro statistico e standard G20, coordinata con 01-P23). Escono la PIENA (sopra 5 mln, con FN11) e la PILOTA (contributo per tre anni).
- **Nessuna dipendenza da 01-P20**, esclusa dal programma: l'**exit tax per le persone fisiche è scritta in questa legge** (opzione A del giurista).
- **01-P24 ESSENZIALE paga 01-P25 ESSENZIALE** (24% sugli utili lasciati nelle imprese di persone): 01-P25 si attiva solo insieme a questa variante (`benchmark/finale_proposta_neutralita.md`; vincolo in `programma/ottimizza.py`).

**Regole applicate.** Nessuna variante usa DEFICIT, RISPARMI_ATTESI, IVA_EVASIONE, ETS o ALTRO. I costi di attuazione sono su RIALLOCAZIONE (spese di funzionamento di MEF e Agenzia delle entrate). Il gettito è un'entrata decisa per legge nella copertura **FN12**, solo con la ESSENZIALE, imputata al fondo SPESE_FISCALI come fondo più vicino, come FN05-FN10. Vincolo già in `programma/ottimizza.py`: `"FN12": ["01-P24:ESSENZIALE"]`.

---

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
