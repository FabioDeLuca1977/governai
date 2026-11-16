*Bozza scritta da un agente AI il 16 novembre 2026 e corretta lo stesso giorno con le scelte di chi guida il progetto, le condizioni della verifica giuridica e i rilievi dei tre valutatori. Versione da inserire nel programma; non rivista da una persona.*

# Schede: equità fiscale in cima alla scala dei redditi (01-P19, 01-P21, 01-P22, 01-P23)

**Righe per `motore/proposte.csv`** (stesse colonne: `proposta_id,titolo,costo_min,costo_max,costo_opportunita`). 01-P20 non c'è più: è uscita per scelta di chi guida il progetto (16/11/2026).

```csv
01-P19,"Holding personali: sugli utili parcheggiati la stessa imposta che possedendo direttamente, con le imprese operative e chi reinveste esclusi",0.007,0.011,0.0
01-P21,"Fine dei contenitori: polizze vita senza rischio assicurativo e trust esteri opachi tassati come investimenti",0.002,0.004,0.0
01-P22,"Eredità: l'impresa che lavora resta esente, il patrimonio passivo no; gli eredi mantengono il costo fiscale oltre 1 mln",0.002,0.003,0.0
01-P23,"Sapere chi paga quanto: statistica ufficiale delle aliquote effettive e unità per i grandi patrimoni con adempimento collaborativo",0.002,0.015,0.0
```

Diagnosi e fonti: `benchmark/equita_fiscale_diagnosi.md`. Varianti: `benchmark/bozza_varianti_equita_fiscale.csv`. Coperture nuove: `benchmark/bozza_coperture_equita_fiscale.csv`. Verifica giuridica: `giuridico/conformita_equita.csv` e `giuridico/note_equita.md`. Importi in mld €/anno salvo diversa indicazione. "Stima GovernAI" vuol dire stima propria senza quantificazione ufficiale; "da verificare" vuol dire dato o norma non riscontrati sul testo originale.

**Le schede non danno punteggi sui valori.** Li danno i panel indipendenti con `motore/rubrica.md` (`benchmark/panel_equita_A.csv`, `_B.csv`, `_C.csv`). Per lo stesso motivo le colonne RIS ... CIT del CSV delle coperture sono vuote.

## 0. Quadro

| Proposta | Cosa fa | Costo di attuazione a regime (PIENA / ESSENZIALE / PILOTA o ZERO) | Gettito deciso per legge (copertura) |
|---|---|---|---|
| **01-P19** Holding personali: stessa imposta che possedendo direttamente | Chi tiene in una holding **passiva** proventi esenti incassati dopo la legge e non li reinveste paga, sulla parte trattenuta, quanto avrebbe pagato da persona fisica; i dividendi delle società operative partecipate restano fuori; riserva per acquisizioni e crisi; exit tax minima sulle sole partecipazioni in holding passive | 0,011 / 0,007 / ZERO 0 | **FN05** 0,03-0,11; **FN06** (oltre FN05) 0,03-0,10 |
| **01-P21** Fine dei contenitori: polizze senza rischio e trust opachi | Le polizze senza vera copertura del rischio entrano nell'attivo ereditario (solo premi nuovi); le polizze "dedicate" pagano ogni anno sui redditi realizzati; le distribuzioni dei trust esteri poco tassati sono tassate con credito per l'imposta estera | 0,004 / 0,002 / ZERO 0 | **FN09** 0,02-0,10 |
| **01-P22** Eredità: l'impresa che lavora resta esente, il patrimonio passivo no | L'esenzione per il passaggio del controllo (art. 3 c. 4-ter TUS) non copre gli attivi passivi, definiti nella legge; liquidità passiva solo oltre il 20% dell'attivo o un anno di costi; esenzione estesa alle società UE e SEE; gli eredi mantengono il costo fiscale oltre 1 mln, con credito per l'imposta di successione | 0,003 / 0,002 / ZERO 0 | **FN10** 0,02-0,08 (al 2032) |
| **01-P23** Sapere chi paga quanto | Statistica annuale DF-ISTAT-Banca d'Italia (con consultazione BCE e garanzie dell'art. 89 GDPR); unità AdE per i grandi patrimoni con adempimento collaborativo a trasparenza piena; trasparenza sui regimi speciali | 0,015 / 0,006 / PILOTA 0,002 | nessuna (il recupero atteso non è copertura) |

**Gettito totale delle coperture: 0,10-0,39 mld** a regime (2031-2032), tutte **stime GovernAI** con base imponibile non nota. È più basso della prima bozza (0,34-1,15) perché: 01-P20 è uscita (FN07 e FN08 tolte); le riserve già formate non si tassano più; i dividendi delle società operative sono esclusi; la parte di gettito che è solo anticipo di imposte future non è contata. Il minimo è volutamente basso.

**Regole applicate (come nelle schede di `programma/schede/`).**
- Nessuna variante usa DEFICIT, RISPARMI_ATTESI, IVA_EVASIONE, ETS o ALTRO. I costi di attuazione sono su RIALLOCAZIONE (spese di funzionamento di MEF e agenzie fiscali).
- **Il recupero di evasione atteso non è copertura** (01-P23): va al deficit, come stabilito per 01-P10.
- **Le coperture FN05, FN06, FN09 e FN10 sono entrate decise per legge** (nuove regole d'imposta), non recupero di evasione: sono coperture ammesse (art. 17 L. 196/2009). Sono imputate al fondo **SPESE_FISCALI** come "fondo più vicino", come già fatto per SF14. **Proposta al coordinatore:** un fondo dedicato `EQUITA_FISCALE` in `registro/fondi.csv`, perché queste misure non sono spese fiscali del Rapporto MEF e la capienza di SPESE_FISCALI (0-3 mld) è già molto usata. Non ho modificato `registro/fondi.csv`.
- **Coperture legate.** FN05 vale con 01-P19 ESSENZIALE o PIENA; FN06 solo con 01-P19 PIENA; FN09 con 01-P21 ESSENZIALE (circa metà) o PIENA; FN10 con 01-P22 ESSENZIALE (circa metà) o PIENA. Servono vincoli nell'ottimizzatore come per 01-P8 e FN01.
- **Niente doppioni.** Non toccano: SF01 e SF11 (cedolare), SF02 (forfettario), SF13 (catasto), SF14 (aliquote e franchigie di successione), SF20 (impatriati), SF21 (PIR), SF22 (previdenza complementare), 01-P10 (controlli su autonomi e imprese), 01-P12 (riscossione, niente condoni). FN10 e SF14 si sommano solo in parte: vedi la scheda 01-P22.
- **Verifica degli id (16/11/2026).** 01-P19, 01-P21, 01-P22, 01-P23 e FN05, FN06, FN09, FN10 non sono usati altrove nel repository. **01-P20, FN07 e FN08 sono liberi** e non vanno riusati per altro senza dirlo.

**Protezione delle PMI familiari (vale per tutte le schede).**
1. Nessuna proposta tocca gli utili che restano **nella società operativa**: chi reinveste nell'impresa continua a pagare solo l'IRES. Per coerenza, anche i **dividendi che la holding riceve dalle sue società operative** restano fuori da 01-P19.
2. Le holding che guidano imprese operative non pagano nulla su ciò che **reinvestono** entro 3 anni, e possono accantonare una **riserva per acquisizioni e crisi** usabile entro 5 anni.
3. Franchigie alte (100.000-250.000 € l'anno di proventi passivi trattenuti; 2-5 mln di attivo passivo) lasciano fuori le piccole casseforti di famiglia.
4. Il passaggio generazionale dell'**azienda operativa** resta esente (art. 3 c. 4-ter TUS, confermato anche da SF14), con una soglia di liquidità che protegge le imprese prudenti.
5. **Nessuna norma tocca il passato**: si tassano solo proventi, premi, successioni e trasferimenti successivi all'entrata in vigore.

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

---

## Nota per il coordinatore

- **Scelte di chi guida il progetto già applicate** (16/11/2026): 01-P20 esce. Resta da decidere, se lo si vuole, se l'imposta di 01-P19 debba pareggiare il 26% (PIENA) o essere un acconto del 13% (ESSENZIALE). L'imposta patrimoniale resta esclusa (diagnosi, par. 6).
- **Pacchetto che l'autore ritiene coerente:** 01-P19 ESSENZIALE + 01-P21 ESSENZIALE + 01-P22 ESSENZIALE + 01-P23 PIENA. Costo di attuazione circa 0,026 mld; coperture FN05, FN09 (circa metà), FN10 (circa metà): circa 0,05-0,20 mld. Con le varianti ESSENZIALE di 01-P21 e 01-P22 il gettito è circa metà di FN09 e FN10: va gestito nell'ottimizzatore o con righe separate, da decidere.
- **Vincoli da aggiungere all'ottimizzatore e a `sistema/coerenza.py`:** FN05 solo con 01-P19 ESSENZIALE o PIENA; FN06 solo con 01-P19 PIENA; FN09 solo con 01-P21 ESSENZIALE o PIENA; FN10 solo con 01-P22 ESSENZIALE o PIENA. Il vincolo "01-P20 solo con 01-P19" non serve più.
- **Da verificare prima dell'uso pubblico:** numerazione nel testo unico d.lgs. 117/2026; testo dell'art. 235 ter C CGI; estremi delle sentenze della Cassazione sulle polizze; norma tedesca sulla copertura minima delle polizze e soglia di liquidità del §13b ErbStG; sentenza CGUE del 21/5/2026 (C-684/24 e C-685/24); limitazione dell'art. 3 c. 4-ter TUS alle società residenti; numero di holding passive e utili esclusi (DF, quadro RF); quota dei dividendi delle holding che viene da partecipate operative (serve per FN05 e FN06); riserve delle polizze unit-linked e multiramo (IVASS); caso residuo di discriminazione alla rovescia in 01-P19 (Dipartimento politiche europee).

---

## Modifiche del 16/11/2026

**A. Scelte di chi guida il progetto**
1. **01-P20 esce** (addizionale di 4 punti sui redditi finanziari): tolta la riga dal blocco csv, tolte la scheda, le tre varianti e le coperture FN07 e FN08. Tolti il vincolo "01-P20 solo con 01-P19" e i rimandi nelle altre schede.
2. **Exit tax spostata in 01-P19** (punto 11, art. 7), in forma minima: solo per chi possiede quote di holding passive oltre 1 mln, solo sulle riserve formate dopo la legge e non ancora tassate, solo per i trasferimenti futuri; sospensione senza interessi e garanzie verso UE, SEE e Svizzera, credito per le minusvalenze successive, 5 rate verso gli altri Paesi. Nei rischi è scritto che chi parte porta con sé le riserve pregresse e le altre partecipazioni.

**B. Condizioni del giurista**
3. **01-P19:** base solo sui proventi dal periodo d'imposta successivo, mai le riserve già formate (art. 2 c. 1; prima la bozza tassava gli utili vecchi "se trattenuti dopo"); regola su liquidazione e recesso solo per successioni future (art. 5); esclusione dei dividendi della direttiva madre-figlia anche negli anni successivi; holding estere con esimente sempre disponibile e stessa base, franchigia, reinvestimenti e riserva; il beneficio delle riserve tassate e il credito d'acconto (ESSENZIALE) seguono le quote; presunzione relativa sui prestiti coordinata con l'art. 67 lett. h-ter; antiabuso con interpello; reinvestimenti in PMI non quotate nei limiti dell'art. 21 del regolamento di esenzione; valutazione al netto delle minori entrate future.
4. **01-P21:** norma espressa sulle polizze senza rischio come attivo ereditario (art. 1 c. 3); solo premi versati dal 2028, anche nei contratti in corso; tassazione annua solo dei redditi realizzati, con scomputo al riscatto; trust: tassata solo la parte di reddito, con credito per l'imposta estera; soglia del 10% cambiabile solo per legge; oneri uguali per le compagnie estere; nella ESSENZIALE soglia calcolata su tutti i contratti; registro dei titolari effettivi conforme alla sentenza del 21/5/2026.
5. **01-P22:** criteri degli attivi passivi scritti nella legge, decreto solo tecnico; solo successioni e donazioni future; credito per l'imposta di successione sulla plusvalenza; esenzione estesa alle società UE e SEE; rate che decadono solo se l'impresa è ceduta.
6. **01-P23:** consultazione della BCE; garanzie dell'art. 89 GDPR nella legge (pseudonimizzazione, ambiente sicuro, soglie di frequenza, divieto di uso per l'accertamento, parere del Garante); sanzioni ridotte solo per i rischi comunicati in anticipo, con esclusione e revoca per chi omette e interpello aperto a tutti negli stessi tempi.

**C. Rilievi dei tre valutatori**
7. **01-P19:** i dividendi delle partecipazioni di almeno il 10% in società operative non contano nel test dei proventi passivi e non entrano nella base (risolve anche la discriminazione alla rovescia segnalata dal giurista); nuova **riserva per acquisizioni e crisi** (fino al 30% dell'attivo passivo, massimo 20 mln, 5 anni); reinvestimenti anche in fondi EuVECA.
8. **01-P22:** soglia di liquidità passiva **dal 10% al maggiore tra il 20% dell'attivo e un anno di costi operativi**, su liquidità netta dai debiti a breve, con la motivazione (PMI prudenti, stagionalità, crediti lenti, crisi). Effetto blocco attenuato: 5 rate per chi vende il controllo di un'impresa operativa, rideterminazione sempre possibile in 3 rate, credito per l'imposta di successione.

**D. Coperture**
9. **FN05** da 0,08-0,25 (2029, gradualità 2) a **0,03-0,11 (2031, gradualità 2)**; **FN06** da 0,07-0,25 (2029, 2) a **0,03-0,10 (2031, 2)**: niente riserve pregresse, dividendi delle partecipate operative esclusi, riserva per acquisizioni, e solo la parte strutturale (non l'anticipo di imposte future). **FN09** da 0,03-0,15 (2030, 3) a **0,02-0,10 (2032, 4)**: solo redditi realizzati, al netto del minor gettito al riscatto, credito estero sui trust. **FN10** da 0,04-0,15 (2030, 3) a **0,02-0,08 (2032, 4)**: soglia di liquidità più alta, esenzione estesa a UE e SEE, rate decennali che rinviano il gettito. Totale da 0,34-1,15 a **0,10-0,39 mld**. Nella colonna note di ogni copertura è scritta la proposta e la variante a cui è legata.
10. **Costi:** 01-P19 PIENA da 0,010 a 0,011 e ESSENZIALE da 0,006 a 0,007 (exit tax e controllo della riserva); le altre invariate.
11. Il blocco ```csv è ora in testa al file.
