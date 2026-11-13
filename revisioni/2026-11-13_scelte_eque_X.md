# Quattro scelte aperte: una proposta equa

*Proposta scritta da un agente AI (valutatore X), 13 novembre 2026; non è una decisione.*

*Prospettiva dichiarata: questo valutatore dà peso particolare a chi oggi ha meno mezzi e ai territori con meno servizi, senza trascurare la sostenibilità dei conti. Legenda: [Fatto] con fonte; [Stima] calcolo di questo valutatore; [Giudizio] valutazione. Importi in mld €/anno a regime, gettito minimo, salvo dove indicato.*

## In breve

1. **Garanzia.** Un comitato di garanzia di 7 persone, scelte in buona parte a sorte tra persone idonee, che custodisce le regole (Carta, rubrica, motore, regolamento) ma non decide il programma. Accanto, una persona responsabile del programma, con nome pubblico, che firma ogni scelta politica e risponde per iscritto.
2. **Coperture regressive.** Nessuna copertura nuova. Si tengono le accise sulla salute, ma per legge il loro gettito paga servizi usati soprattutto da chi ha meno, e il gettito oltre il minimo, certificato a consuntivo, paga prima un programma per smettere di fumare. Le compensazioni del gasolio vanno prima alle piccole imprese e alle aree interne. Costo ex ante: **0**.
3. **Personale infermieristico (06-C2).** Entra come **pilota** (0,35) per il 2027-2029, nelle aree interne e in 4 Regioni. Le risorse vengono da: 01-P13 da piena a essenziale (−0,14), 09-C9 da essenziale a pilota (−0,03), 04-P9 a sole regole (−0,03 di risorse generali), 01-P5 fuori (libera 0,15 di coesione, usata per borse e formazione), e la rivalutazione ridotta delle pensioni alte (PE04) anticipata di un anno, al 2029.
4. **Fondi europei dopo il 2029.** Decidere **ora** una riserva nazionale: PE04, che oggi non finanzia nulla, più i risparmi delle riduzioni del punto 3. A regime coprono esattamente gli 0,50 mld. Una regola di salvaguardia in tre passi copre gli anni 2030-2032, quando PE04 rende ancora poco.

Le prove con l'ottimizzatore sono descritte nell'appendice. I file `programma/selezione_prova_x_*` creati nel repository sono stati cancellati.

---

## Un fatto che cambia i conti

[Fatto] Nel programma intermedio la copertura **PE04** (rivalutazione al 50% invece che al 75% sulla sola quota di pensione oltre 6 volte il minimo, dal 2030) è attivata con un gettito minimo di **0,30 mld**. Però sta nel fondo vincolato PENSIONI, che può pagare solo 02-C3 (patto previdenziale) o 07-C5 (difesa). Nell'intermedio 02-C3 è nella versione a costo zero. Risultato: **spesa del fondo PENSIONI 0,00, gettito disponibile 0,30** (`programma/selezione_intermedio.md`, tabella "Uso dei fondi"; `programma/varianti/02_lavoro.csv`).

[Fatto] PE04 era stata pensata per pagare la pensione di garanzia di 02-C3, che costerebbe dal 2036 (`programma/varianti/02_lavoro.csv`, note). Nel programma intermedio quella pensione di garanzia è rinviata.

[Giudizio] Quindi oggi chi ha una pensione alta paga un piccolo sacrificio già deciso, ma il denaro non finanzia nessuna misura: va solo a ridurre il deficit. Usarlo non è una tassa in più. È dare una destinazione a una copertura già ammessa. Va però verificato dal controllo giuridico che il risparmio sulla perequazione non debba restare nel sistema previdenziale: la Corte costituzionale ha ritenuto legittimo il "raffreddamento" della perequazione per le pensioni più alte (sent. 234/2020), ma il vincolo di destinazione delle risorse non è chiarito nelle fonti consultate ([Corte costituzionale, sent. 234/2020](https://www.cortecostituzionale.it/stampa-pdf-pronuncia/2020/234); [giurcost.org](https://giurcost.org/decisioni/2020/0234s-20.html)).

[Fatto] PE04 cresce piano: circa 0,1 mld il primo anno, 0,3-0,5 dopo 5-6 anni (`programma/coperture_menu.csv`, note di PE04). [Stima] Percorso al minimo usato qui: 0,10 il primo anno, poi +0,05 l'anno fino a 0,30.

[Stima] Per una pensione di 5.000 € lordi al mese la quota sopra la soglia (circa 3.700 €) è 1.300 €. Con un'inflazione dell'1,8% (ipotesi della nota PE04), la rivalutazione più bassa vale circa 6 € lordi al mese nel primo anno, e si somma negli anni successivi.

---

## Scelta 1. Responsabilità e garanzia

### Proposta

**A. La persona responsabile del programma**

- Una persona con nome e cognome pubblici, e una vice di genere diverso.
- **Che cosa fa**: firma ogni scelta politica che si discosta dal motore (come le scelte del 9, 10, 12 e 13 novembre 2026, descritte in `20_programma_governai.md`, §6), con il prezzo dichiarato; risponde per iscritto, entro 30 giorni, a ogni parere del comitato di garanzia; presenta ogni anno un rendiconto pubblico delle scelte e dei finanziamenti.
- **Che cosa non fa**: non cambia da sola Carta, rubrica, regole del motore o regolamento del governo ombra. Non modera la comunità. Non tocca i punteggi del panel.
- **Durata**: 3 anni, rinnovabile una volta. La revoca spetta all'organo che lo statuto indicherà (per esempio l'assemblea degli iscritti), con motivazione pubblica.

**B. Il comitato di garanzia**

| Elemento | Proposta |
|---|---|
| Composizione | 7 persone: 3 di sensibilità culturali diverse (ad esempio: popolare o conservatrice; liberale; sociale, laica o cattolica; ambientalista: ogni sensibilità al massimo un seggio); 2 sorteggiate tra chi partecipa alla comunità; 1 persona indicata dalle organizzazioni di persone in povertà o con disabilità; 1 persona esperta di finanza pubblica o di metodi statistici |
| Equilibri obbligatori | Almeno 3 donne e 3 uomini; almeno 2 persone residenti nel Mezzogiorno o nelle isole e 1 in un'area interna; nessuna fascia d'età con più di 3 persone |
| Come si scelgono | Avviso pubblico con requisiti scritti. Una commissione di verifica, formata da persone non candidate, controlla solo i requisiti e le incompatibilità. **Tra le persone idonee di ciascuna categoria si sorteggia**. Chi ha avviato il progetto non sceglie i membri |
| Poteri | 1) Approva con 5 voti su 7 ogni modifica di Carta, rubrica, regole del motore, regolamento e ruoli, dopo 30 giorni di commento pubblico. 2) Può chiedere un riesame del programma e una pausa di 15 giorni prima di pubblicare una scelta politica che non dichiara il prezzo. 3) Riceve e pubblica le dichiarazioni di interessi e l'elenco dei finanziamenti. 4) Ordina ogni anno un controllo esterno sui prompt degli agenti e test di parzialità sui temi divisivi. 5) Dà pareri pubblici, motivati, non vincolanti sul merito delle misure |
| Che cosa non fa | Non decide il programma, non sceglie le misure, non modera le opinioni, non cambia i punteggi |
| Durata | 3 anni, non rinnovabile subito; i 2 membri sorteggiati restano 18 mesi, con rinnovo sfalsato per evitare un ricambio totale |
| Incompatibilità | Incarichi elettivi o di partito negli ultimi 3 anni; attività di lobby o consulenza retribuita sulle materie delle misure; rapporti di lavoro o economici con chi finanzia il progetto; parentela con la persona responsabile; candidatura alle elezioni durante il mandato e nei 2 anni successivi |
| Conflitti di interesse | Dichiarazione pubblica all'ingresso e ogni anno; astensione obbligatoria su ogni modifica che tocca un interesse dichiarato; registro pubblico delle astensioni; elenco pubblico dei finanziamenti sopra 500 € |
| Costo | Lavoro volontario con rimborso spese: è un costo del progetto, non dello Stato |

**C. Rapporto con la vision "sul sito nessuno decide"**

[Fatto] Le regole della comunità dicono: "Qui nessuno decide, nemmeno chi ha avviato il progetto" (`comunita/regole.md`). [Giudizio] Il comitato non contraddice questa regola: non decide le idee, custodisce le regole con cui le idee diventano proposte. La comunità resta uno spazio per discutere e prendere appunti con l'AI. Le scelte politiche restano firmate dalla persona responsabile e, quando ci sarà, pesate dall'assemblea civica (08-P1). In più: con 300 firme di iscritte e iscritti la comunità può chiedere al comitato di riesaminare una modifica alla Carta.

### Motivazione con la Carta

- **Fiducia e trasparenza (FID)**: "Chi decide ne risponde" (Carta, valore 2). Oggi chi decide non ha nome: tutte e quattro le revisioni lo segnalano (`revisioni/2026-11-08_sintesi_red_team.md`).
- **Cittadinanza responsabile (CIT)**: sorteggio e soglia di firme coinvolgono le persone.
- **Equità (EQU)** e **Rispetto (RIS)**: un seggio riservato alle organizzazioni di chi ha meno voce, come chiede la regola R5 di `23_equita_e_linguaggio.md`.

### Conto

0 mld per lo Stato. Per il progetto: rimborsi spese e un controllo esterno annuale (dato da acquisire).

### Chi guadagna e chi perde

- **Guadagna**: chi legge il programma e vuole sapere chi ne risponde; le sensibilità oggi assenti.
- **Perde**: chi guida il progetto perde la possibilità di cambiare da solo Carta e regole; le scelte politiche diventano più lente (fino a 15 giorni di pausa).

### Rischi

- Pochi candidati idonei in alcune categorie: si riapre l'avviso, non si nomina a mano.
- Comitato che blocca tutto: i suoi poteri di blocco riguardano solo le regole, non il programma.
- Il sorteggio tra iscritti riflette una comunità ancora piccola e poco varia: si misura la composizione e si pubblica.

### Alternativa scartata

**Comitato nominato da chi ha avviato il progetto.** È più veloce, ma lascia aperta la critica principale: "chi possiede il repository possiede il movimento" (`revisioni/2026-11-08_red_team_civico.md`). Scartata anche l'**assemblea degli iscritti come garante**: oggi la comunità è su invito e piccola, quindi rappresenterebbe pochi.

---

## Scelta 2. Coperture regressive

### I fatti

[Fatto] Le coperture regressive valgono circa 2,3 mld su 7,42 (`23_equita_e_linguaggio.md`, §4):

| Codice | Chi paga | Gettito min. | Compensazione oggi |
|---|---|---|---|
| AS01, AS02 | Chi fuma (circa 10 milioni di persone, 18,6% della popolazione da 11 anni, ISTAT 2025 citato in `coperture_menu.csv`) | 0,75 | Nessuna |
| AS03 | Chi consuma bevande zuccherate | 0,15 | Nessuna |
| SAD13, SAD01 | Autotrasporto e agricoltura; in parte chi compra, tramite i prezzi | 1,10 | 0,4 per flotte e redditi agricoli (già sottratti dal gettito); 25% di SAD01 a flotte e treno merci (attuato da 04-P7 e 04-P8) |
| SAD02 | Aziende agricole | 0,15 | Credito per piccole aziende e montagna |
| SAD10 | Famiglie in montagna e isole con gasolio o GPL | 0,02 | Pompe di calore; salvaguardia ISEE ≤ 15.000 € |
| RP01, RP08 | Giovani che si candidano ai concorsi amministrativi, soprattutto al Sud | 0,09 | Esclusioni e ritorno al 100% se i servizi peggiorano |

[Fatto] L'accisa sul superalcolico (AS04, 0,07) ha punteggio EQU 0 nel menu.

[Fatto] Una tassa sul tabacco è regressiva se si guarda solo alla spesa. Se si contano anche le minori spese mediche di chi riduce il fumo, l'effetto netto può diventare favorevole a chi ha meno. Lo mostra uno studio della Banca mondiale sul Cile, che raccomanda di accompagnare la tassa con politiche per smettere di fumare in ogni fascia di reddito ([Fuchs e Meneses, World Bank WP 7988, 2017](https://documents1.worldbank.org/curated/en/919121488376958052/pdf/WPS7988.pdf)). Per l'Italia la quota di persone che fumano per fascia di reddito è un dato da acquisire.

### Proposta, misura per misura

1. **AS01, AS02, AS03 (0,90): restano, con tre regole.**
   - **Destinazione per legge, a saldo.** La legge di bilancio dichiara che un importo pari al gettito di AS01-AS03 finanzia servizi di salute di prossimità: 06-C3 Case della Comunità (0,80), 06-C8 squadre infermieristiche di quartiere (0,10), 06-C2 pilota (0,35, scelta 3). Totale 1,25, più del gettito. Sono servizi concentrati dove mancano. [Fatto] Chi è nel quinto più povero rinuncia alle cure quasi il doppio della media: 4,4% contro 2,5% (Eurostat `hlth_silc_08`, in `23_equita_e_linguaggio.md`).
   - **Clausola di coerenza.** Se questi servizi scendono sotto la versione essenziale, il secondo scalino dell'accisa di AS01 (2029) si sospende.
   - **Gettito oltre il minimo, solo a consuntivo.** [Fatto] Il gettito massimo stimato di AS01-AS03 è 1,60, il minimo 0,90 (`coperture_menu.csv`). Ogni anno la RGS certifica il gettito effettivo. La prima parte dell'eccedenza, fino a 0,05 mld, finanzia un programma per smettere di fumare: colloqui nelle Case della Comunità e farmaci gratuiti per chi ha ISEE fino a 15.000 €. [Stima] 0,05 mld bastano per circa 150.000 percorsi l'anno a circa 300 € l'uno (stima da verificare con Ministero della salute e AIFA). Il resto dell'eccedenza va alla riserva della scelta 4.
2. **SAD13, SAD01, SAD02 (1,25): restano, con priorità nelle compensazioni.** Le compensazioni già previste vanno prima alle imprese di autotrasporto fino a 5 veicoli, alle aziende agricole di montagna e delle aree interne, e alle isole. Ogni due anni una verifica: se nelle aree interne non ci sono ancora alternative (biometano, mezzi elettrici, ricarica pesante), lo scalino successivo di SAD13 slitta di un anno. 04-P7 e 04-P8, che attuano la compensazione di SAD01, **non si toccano** anche per questo nella scelta 3.
3. **SAD10 (0,02): resta.** Il contributo per le pompe di calore dà priorità alle famiglie con ISEE fino a 25.000 € nelle aree interne. Se il gettito a consuntivo supera il minimo, la salvaguardia sale da ISEE 15.000 a 20.000 €.
4. **RP01, RP08 (0,09): restano** con le salvaguardie già scritte. In più: pubblicazione semestrale delle assunzioni mancate per Regione, e ritorno al 100% del turnover nelle Regioni dove la carenza di personale amministrativo supera la media nazionale.

### Motivazione con la Carta

- **Equità (EQU)**: la linea rossa vieta di spostare costi su chi ha meno "senza compensazione". Qui la compensazione è in servizi e in aiuto a smettere, non in denaro.
- **Benessere (BEN)**: la tassa sul tabacco funziona solo se riduce il fumo; per questo il programma per smettere viene prima.
- **Responsabilità verso il futuro (FUT)**: nessun euro speso prima di essere incassato; l'eccedenza si usa solo a consuntivo.
- **Bellezza, patrimonio e accoglienza (BPA)**: territori vivi; le compensazioni vanno prima alle aree interne.

### Conto

| Voce | mld |
|---|---|
| Costo ex ante | **0** |
| Programma per smettere di fumare | fino a 0,05, solo da gettito oltre il minimo certificato |
| Salvaguardia SAD10 allargata | solo da gettito oltre il minimo; importo da acquisire |
| Effetto sul saldo | nullo |

### Chi guadagna e chi perde

- **Guadagna**: chi fuma e ha un reddito basso e vuole smettere; chi vive in aree con meno servizi; piccoli autotrasportatori e aziende agricole di montagna.
- **Perde**: le imprese di autotrasporto più grandi e le aziende agricole di pianura ricevono meno compensazioni; la riserva della scelta 4 riceve meno eccedenze; chi fuma e non usa i servizi paga comunque.

### Rischi

- La destinazione "a saldo" è un impegno politico, non un vincolo contabile forte: va scritta in legge con un allegato di verifica annuale.
- Se il consumo di tabacco cala molto, il gettito scende (effetto voluto); i servizi restano finanziati dalle risorse generali.
- Senza microsimulazione per decili il giudizio resta qualitativo (`23_equita_e_linguaggio.md`, §4).

### Alternative scartate

- **Compensazione in denaro** (per esempio un aumento dell'assegno unico per i redditi bassi): costerebbe soldi che non ci sono e annullerebbe il segnale di prezzo.
- **Togliere AS01**: mancherebbero 0,60 mld e si dovrebbero tagliare servizi usati soprattutto da chi ha meno. Per chi ha meno il saldo sarebbe peggiore.
- **Vincolo contabile rigido del gettito**: lega servizi permanenti a un'entrata che cala nel tempo.

---

## Scelta 3. Personale infermieristico (06-C2)

### I fatti

- [Fatto] L'Italia ha 6,9 infermiere e infermieri ogni 1.000 abitanti, contro 9,2 della media OCSE (Eurostat `hlth_rs_prs2`, 2024, in `programma/schede/06_salute.md`).
- [Fatto] La scheda 06-C3 dice: "se C2 non entra, la ESSENZIALE di C3 perde efficacia". Il programma spende già 0,80 mld per le Case della Comunità.
- [Fatto] Varianti di 06-C2: PILOTA 0,35 (4 Regioni, almeno 2 del Mezzogiorno, e aree interne; 5.000 borse con vincolo SSN; indennità di area disagiata; pratica avanzata in 50 Case della Comunità; valutazione Agenas a 30 mesi); ESSENZIALE 1,4 (`programma/varianti/06_salute.csv`).
- [Fatto] Il motore classifica 06-C2 "dipendente dai valori" (nella prima metà della classifica nel 62% delle combinazioni di pesi). 01-P13, 04-P9 e 09-C9 sono in coda o dipendenti dai valori e sono nell'intermedio per scelta politica (`motore/esito_proposte.csv`; `20_programma_governai.md`, §6).

### Proposta

**06-C2 entra come PILOTA per il 2027-2029.** È una sperimentazione triennale: dal 2030 continua solo con una copertura nuova o se i fondi europei liberano la riserva della scelta 4.

Da dove vengono le risorse:

| Voce | Effetto sulle risorse generali | Effetto sulla coesione 2021-27 |
|---|---|---|
| 06-C2 PILOTA: indennità di area disagiata (risorse generali) | +0,25 | — |
| 06-C2 PILOTA: borse di studio e formazione alla pratica avanzata (FSE+, solo fino al 2029, nessun personale stabile) [Stima della ripartizione] | — | +0,10 |
| 01-P13 credito per la ricerca da PIENA a ESSENZIALE: resta il 12% per le imprese sotto i 50 addetti | −0,14 | — |
| 09-C9 squadra per la produttività con l'AI da ESSENZIALE a PILOTA (da circa 70 a 25 persone) | −0,03 | −0,005 |
| 04-P9 consegne pulite: resta la legge quadro sulle zone a emissioni zero, senza micro-hub finanziati | −0,03 | −0,04 |
| 01-P5 garanzie per l'energia rinnovabile delle PMI esce | — | −0,15 |
| PE04 anticipata dal 2030 al 2029 (una copertura già ammessa che cambia data) | +0,10 nel 2029 (gettito) | — |

[Stima] Saldo sulle risorse generali nel 2029: servono 0,25; vengono circa 0,17 dalle riduzioni (0,20 a regime) e 0,10 da PE04. Margine 0,02-0,05. Sulla coesione: spesa 1,80 su una capienza minima di 2,00; il margine di 0,20 assorbe anche i prelievi non contati segnalati in `benchmark/fondi_coesione_bandi.md` (circa 0,08 tra 07-C4 e 06-C10).

[Fatto, prova dell'ottimizzatore] Con la ripartizione di 06-C2 descritta sopra e PE04 contata tra le risorse generali, il programma è finanziabile con un margine di 0,20 sulle risorse generali (spesa 7,11, gettito 7,31; spesa totale 9,18). Senza PE04, invece, 06-C2 entra solo se 01-P13 esce del tutto, oppure se escono 04-P7 e 04-P8, che sono la compensazione di SAD01 (vedi appendice).

### Motivazione con la Carta

- **Regola 7 e sinergie**: le Case della Comunità sono nel nucleo robusto. Senza personale rendono meno. Il motore non conta questa sinergia: la dichiariamo.
- **Equità (EQU) e Rispetto (RIS)**: il pilota parte dalle aree interne e dal Mezzogiorno, dove mancano infermiere e infermieri.
- **Regola 6, valore per euro**: si abbassano misure in coda o dipendenti dai valori, non misure del nucleo.
- **Responsabilità verso il futuro (FUT)**: pilota a termine, con valutazione, nessun impegno permanente senza copertura.

### Chi guadagna e chi perde

- **Guadagna**: chi vive in aree interne e in 4 Regioni (almeno 2 del Mezzogiorno); 5.000 studentesse e studenti di infermieristica con borsa; il personale infermieristico delle aree disagiate (fino a 3.000 € l'anno di indennità).
- **Perde**: le imprese con 50 addetti o più, che non hanno il credito per la ricerca del 10% né il rimborso in denaro alle imprese più piccole; le 14 città metropolitane, che non hanno micro-hub finanziati; le PMI energivore, soprattutto del Centro-Nord, senza garanzie pubbliche per i contratti di energia rinnovabile; la squadra per la produttività pubblica, più piccola; chi ha una pensione oltre circa 3.700 € lordi al mese, che perde la rivalutazione piena sulla quota alta un anno prima.

### Rischi

- Le riduzioni toccano tre scelte politiche già fatte da chi guida il progetto (9 e 10 novembre 2026): va detto apertamente.
- La quota FSE+ richiede un'operazione selezionata da un'autorità di gestione e la regola "solo servizi e formazione, non stipendi stabili".
- Anticipare PE04 aumenta il rischio di contenzioso già segnalato nel menu: serve il controllo giuridico.
- Se il pilota va bene, il passaggio a ESSENZIALE costa 1,4 mld: non è coperto e va deciso nel 2030.

### Alternative scartate

- **06-C2 ESSENZIALE (1,4)**: senza tasse in più non ci sono 1,4 mld senza togliere misure del nucleo.
- **Pagare 06-C2 abbassando 06-C8 (squadre di quartiere)**: toglierebbe infermiere e infermieri per pagare infermiere e infermieri. Inoltre 06-C8 ha più valore per euro.
- **Togliere del tutto 01-P13** (la soluzione che sceglie l'ottimizzatore): resterebbe la chiusura del patent box (SF16), il cui gettito è vincolato proprio al credito per la ricerca. Le imprese perderebbero un'agevolazione senza ricevere l'altra.
- **Togliere 04-P7 e 04-P8**: sono la compensazione della copertura regressiva SAD01; sarebbe incoerente con la scelta 2.
- **Usare PE04 per 06-C2 invece che per il dopo 2029**: PE04 incassa dal 2029-2030, il pilota spende dal 2027. Il calendario non torna e la regola 7 dà la precedenza al nucleo.

---

## Scelta 4. Fondi europei dopo il 2029

### I fatti

- [Fatto] Spesa pagata con la coesione 2021-27 che serve anche dopo il 2029: 03-P4 0,25; 05-C2 0,15; 05-C1 0,08; 09-C8 0,02. Totale **0,50**, tutte misure del nucleo robusto (`programma/varianti/*.csv`; `programma/coesione_dopo_2029.csv`).
- [Fatto] La Commissione ha proposto un fondo unico per i piani di partenariato 2028-2034 da 865 mld, con almeno il 14% agli obiettivi sociali; per l'Italia non ci sono ancora importi (`benchmark/fondi_coesione_bandi.md`).
- [Fatto] I programmi 2021-27 che hanno spostato almeno il 10% sulle nuove priorità possono spendere fino al 31 dicembre 2030; l'Italia ha riprogrammato 7,06 mld in 35 programmi su 48 (reg. UE 2025/1914, in `benchmark/fondi_coesione_bandi.md`).
- [Fatto] Il registro dà alla coesione 2028-34 capienza minima zero (`registro/fondi.csv`).

### Proposta: decidere ora, con una salvaguardia in tre passi

**1. Riserva nazionale decisa nella prima legge di bilancio.**
- PE04 esce dal fondo vincolato PENSIONI ed è destinata per legge, dal 2030, alla continuità delle quattro misure del nucleo, per la parte che i fondi europei non coprono.
- Le riduzioni della scelta 3 (01-P13, 09-C9, 04-P9: 0,20 di risorse generali) restano anche dopo il 2029. Il denaro che nel 2027-2029 paga il pilota 06-C2 passa alle quattro misure del nucleo.
- A regime: 0,30 (PE04) + 0,20 (riduzioni) = **0,50**.

[Fatto, prova dell'ottimizzatore] Simulando il dopo 2029 (quota di coesione delle quattro misure spostata sulle risorse generali, PE04 tra le risorse generali, 06-C2 concluso), il programma è finanziabile con margine zero: spesa sulle risorse generali 7,31 su un gettito di 7,31.

**2. Regola di salvaguardia.**
- **Passo 1, subito.** Le operazioni 2021-27 di 03-P4, 05-C1, 05-C2 e 09-C8 si collocano nei programmi prorogati al 2030. Il Governo chiede di inserire le quattro misure nel piano di partenariato 2028-2034: sono campi tipici del FSE+ (istruzione, competenze) e del FESR (prevenzione dei rischi).
- **Passo 2, autunno 2029.** Nella legge di bilancio 2030 la RGS certifica quanto coprono i fondi 2028-2034. Se coprono, la riserva nazionale si libera e va, in quest'ordine: a) continuità o passaggio a regime di 06-C2, se la valutazione Agenas è positiva; b) personale del progetto di vita 02-C5 dal 2030 (circa 0,033, `benchmark/fondi_coesione_bandi.md`); c) dal 2036, pensione di garanzia di 02-C3, la destinazione originaria di PE04.
- **Passo 3, se mancano risorse negli anni di avvio.** Prima l'eccedenza certificata delle accise sulla salute (scelta 2). Poi una riduzione temporanea, dichiarata, di una misura in coda: 01-P13 da essenziale a sole regole (circa 0,15). Mai deficit, mai tagli alle quattro misure del nucleo, mai tasse nuove.

**Calendario indicativo** [Stima: PE04 al minimo dal 2029, riduzioni crescenti fino a regime]

| Anno | Fabbisogno | Riduzioni | PE04 | Scarto | Come si chiude |
|---|---|---|---|---|---|
| 2029 | 0,25 (pilota 06-C2) | 0,17 | 0,10 | +0,02 | — |
| 2030 | 0,50 | 0,20 | 0,15 | −0,15 | Passo 1: programmi 2021-27 prorogati al 2030 |
| 2031 | 0,50 | 0,20 | 0,20 | −0,10 | Passo 2 (fondi 2028-34) o passo 3 |
| 2032 | 0,50 | 0,20 | 0,25 | −0,05 | Come sopra |
| dal 2033 | 0,50 | 0,20 | 0,30 | 0 | — |

### Motivazione con la Carta

- **Regola 7**: le quattro misure sono nel nucleo robusto e devono restare almeno nella versione essenziale anche dopo il 2029.
- **Responsabilità verso il futuro (FUT)**: aspettare il negoziato europeo vorrebbe dire scoprire il buco nel 2029, quando i margini saranno già impegnati.
- **Equità (EQU)**: 05-C1 lavora nelle scuole più fragili (EQU 2,0), 05-C2 con gli adulti senza diploma (EQU 1,3), 03-P4 nei Comuni a rischio di frana e alluvione (`motore/esito_proposte.csv`). PE04 è progressiva (EQU +1).

### Conto

| | mld a regime |
|---|---|
| Fabbisogno dopo il 2029 | 0,50 |
| PE04 (già ammessa, oggi senza destinazione) | 0,30 |
| Riduzioni della scelta 3 che restano | 0,20 |
| Saldo | 0 |
| Scarto negli anni di avvio | fino a 0,15 nel 2030, 0 dal 2033 |

### Chi guadagna e chi perde

- **Guadagna**: studentesse e studenti delle scuole più fragili, adulte e adulti senza diploma, chi vive in Comuni esposti a frane e alluvioni, i piccoli Comuni (staffetta delle competenze).
- **Perde**: chi ha una pensione oltre circa 3.700 € lordi al mese vede usato per altro un risparmio che era pensato per le pensioni di garanzia; le persone giovani con carriere discontinue aspettano più a lungo la pensione di garanzia (02-C3), che oggi però non è nel programma intermedio; le imprese con 50 addetti o più restano senza credito per la ricerca pieno anche dopo il 2029.

### Rischi

- Verifica giuridica su PE04 (destinazione fuori dal sistema previdenziale; durata senza scadenza).
- PE04 rende al minimo 0,30 solo verso il 2033-2035: negli anni di avvio servono i passi 1-3.
- Il nuovo ciclo europeo può legare i pagamenti a traguardi, come il PNRR: le misure vanno riscritte con obiettivi misurabili.

### Alternative scartate

- **Aspettare il negoziato europeo**: troppo rischioso. Nel 2014-2020 e nel 2021-2027 i primi due o tre anni di ogni ciclo sono stati quasi vuoti (`benchmark/fondi_coesione_bandi.md`).
- **SAD13 o altri sussidi ambientali come riserva** (indicati nella nota di 03-P4): il loro gettito è già tutto usato nell'intermedio.
- **FSC nazionale**: conta nella spesa netta delle regole europee e quello 2021-27 è già assegnato (`registro/fondi.csv`).

---

## Appendice: prove con l'ottimizzatore

Comando di riferimento del brief; profondità della robustezza ridotta (`--n 30`), perché serviva solo la fattibilità. Le prove che cambiano dati (PE04 tra le risorse generali, ripartizione di 06-C2, simulazione del dopo 2029) sono state eseguite su una **copia** di `programma/`, `motore/`, `registro/` e `giuridico/` in una cartella temporanea, senza toccare il repository.

| Prova | Dati | Esito |
|---|---|---|
| base | repository | 9,17 mld: riproduce l'intermedio |
| a1: 06-C2 PILOTA, con 01-P13, 09-C9 e 04-P9 liberi | repository | Finanziabile solo se **01-P13 esce del tutto**, 04-P9 passa a sole regole e 09-C9 a pilota (9,13) |
| a2: come a1 ma 01-P13 essenziale | repository | Non finanziabile |
| s3c: 06-C2 con quota FSE+, 01-P13 essenziale, 01-P5 fuori | copia | Finanziabile solo se escono anche 04-P7 e 04-P8 (compensazione di SAD01) |
| s1base: PE04 tra le risorse generali | copia | +0,30 spesi su misure di trasparenza (09-C1 e altre): conferma che PE04 oggi non finanzia nulla |
| s4: PE04 generale + pacchetto della scelta 3 | copia | Finanziabile; margine 0,20 sulle risorse generali (spesa 9,18) |
| s5: dopo il 2029 (coesione delle 4 misure sulle risorse generali, capienza coesione 1,5), PE04 generale, riduzioni della scelta 3, 06-C2 concluso | copia | Finanziabile con margine zero (7,31 su 7,31); con una riserva di 0,05 non è più finanziabile |

**Limite del metodo.** L'ottimizzatore ragiona a regime e non per anno: conta PE04 e SAD13 al valore del 2035, la coesione come se durasse. Il calendario della scelta 4 è una stima di questo valutatore e va verificato con la RGS sul profilo annuale dell'intero programma.

## Fonti esterne

- Corte costituzionale, sentenza 234/2020: [testo](https://www.cortecostituzionale.it/stampa-pdf-pronuncia/2020/234); [scheda giurcost.org](https://giurcost.org/decisioni/2020/0234s-20.html).
- A. Fuchs, F. Meneses, *Are Tobacco Taxes Really Regressive? Evidence from Chile*, World Bank Policy Research WP 7988, 2017: [PDF](https://documents1.worldbank.org/curated/en/919121488376958052/pdf/WPS7988.pdf).
