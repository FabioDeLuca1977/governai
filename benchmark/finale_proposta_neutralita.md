*Testo finale scritto da un agente AI il 16 novembre 2026 dopo le scelte di chi guida il progetto ("SNC con copertura"); parte dalla bozza `benchmark/bozza_proposta_neutralita.md`, dal panel (`benchmark/panel_neutralita_*.csv`) e dalla verifica giuridica (`giuridico/note_neutralita.md`, `giuridico/conformita_neutralita.csv`); non rivisto da una persona.*

# Scheda finale: 24% sugli utili lasciati nelle imprese di persone (01-P25)

Riga per `motore/proposte.csv` (formato `proposta_id,titolo,costo_min,costo_max,costo_opportunita`; costo a regime della sola variante con costo, la ESSENZIALE):

```csv
01-P25,"Imprese di persone come le SRL: 24% sugli utili lasciati in azienda da ditte, SNC e SAS in contabilità ordinaria, IRPEF solo su ciò che si preleva; pagata dalla patrimoniale minima",0.63,0.63,0.0
```

Varianti: `benchmark/finale_varianti_neutralita.csv` (stessa intestazione di `programma/varianti/11_evasione.csv`). Calcoli: `analisi/chi_paga/neutralita.py`, risultati in `analisi/chi_paga/neutralita.csv`. Importi in mld €/anno salvo diversa indicazione. "Stima GovernAI" = stima propria su dati ufficiali; "da verificare" = dato o norma non riscontrati sul testo originale.

**Scelte di chi guida il progetto (16/11/2026).**
- **"SNC con copertura".** 01-P25 è **solo la regola (a)**: 24% sugli utili lasciati in azienda per SNC, SAS e imprese individuali in contabilità ordinaria, IRPEF su ciò che si preleva. Varianti: **ESSENZIALE** (24% fino a 100.000 € trattenuti l'anno per socio) e **ZERO** (microsimulazione ufficiale e decisione nel 2030). **Niente PIENA.**
- **Si attiva solo insieme alla patrimoniale minima 01-P24 ESSENZIALE, che la paga** con la copertura FN12 (`benchmark/finale_proposta_patrimoniale.md`). Vincolo già scritto in `programma/ottimizza.py`: `LEGAMI_VARIANTI = {"01-P25:ESSENZIALE": ["01-P24:ESSENZIALE"]}`.
- **"Holding subito".** La regola (b) della bozza (dividendi fermi nella holding personale) **non è più in 01-P25**: è la parte B di 01-P19 (`programma/schede/11_evasione.md`), con le coperture FN13 e FN14 (`benchmark/finale_coperture_holding.csv`). Le due proposte restano i due lati della stessa idea: stessa imposta sull'utile che resta nell'impresa, qualunque sia la forma, e sull'utile che ne esce.

**Regole applicate.** Nessuna variante usa DEFICIT, RISPARMI_ATTESI, IVA_EVASIONE, ETS o ALTRO. Il minor gettito è imputato a SPESE_FISCALI, come le altre riduzioni d'imposta del programma (01-P4, 01-P9); i costi di attuazione vanno su RIALLOCAZIONE. Nessuna copertura nuova per 01-P25: la paga FN12.

---

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
