# Quattro scelte politiche aperte: una proposta equa (valutatore Y)

*Proposta scritta da un agente AI (valutatore Y), 13 novembre 2026; non è una decisione.*

Questa è una proposta motivata. Decide chi guida il progetto. Ho lavorato da solo, senza vedere il lavoro degli altri due valutatori.

**Il mio punto di vista.** Ho dato un peso particolare a due cose: la responsabilità verso le generazioni future (valore FUT) e la credibilità dei conti. Ho tenuto conto anche dell'equità (EQU). In pratica ho seguito tre regole:

- nessuna promessa senza un euro certo dietro;
- nessun conto lasciato a chi viene dopo;
- quando qualcuno perde, lo scrivo.

**Come leggere il testo.**

- [Fatto]: un dato del repository o di una fonte esterna, sempre citata.
- [Stima mia]: un calcolo mio sui file del repository, con il metodo.
- [Valutazione]: un mio giudizio.

Tutti gli importi sono in miliardi di euro l'anno a regime, se non è scritto altro.

**Vincoli rispettati.**

- Nessuna tassa in più oltre quelle già nel programma intermedio.
- Nuovo deficit zero.
- Punteggi del panel, Carta e rubrica invariati.
- Le misure del nucleo robusto restano almeno in versione essenziale, salvo le due eccezioni già dichiarate (09-C10 e 02-C5).
- Nessun personale stabile pagato con fondi europei.

**Verifiche con l'ottimizzatore.** Le ho fatte solo con etichette `prova_y_*`, e alla fine ho cancellato i file.

---

## Un problema di credibilità che riguarda tutte e quattro le scelte

[Fatto] L'ottimizzatore confronta spesa e coperture "a regime" e non usa le colonne `anno_regime` e `gradualita` del menu delle coperture (`programma/ottimizza.py`, che non legge queste colonne; `programma/coperture_menu.csv`). Alcune coperture arrivano a regime tardi:

- SAD13 (0,80) nel 2035, in 8 anni;
- PE04 (0,30) nel 2035;
- RP01 e RP08 nel 2031.

La spesa invece arriva a regime nel 2029-2030.

[Stima mia] Ho ipotizzato che ogni copertura cresca in modo lineare negli anni di gradualità indicati nel menu. Il gettito minimo sulle risorse generali sarebbe allora:

- circa 5,6 nel 2029, contro una spesa di circa 6,5;
- circa 6,4 nel 2030, contro una spesa che si avvicina a 7,0;
- 7,01 solo nel 2035.

Il saldo "a regime" è in pareggio. Negli anni di passaggio può mancare tra 0,4 e 0,9 l'anno. È una stima grezza: va rifatta con il profilo vero di ogni misura, insieme alla RGS. Ma indica una cosa: **ogni euro di spesa in più nel 2029-2031 pesa più di quanto mostri il saldo a regime**. Ne tengo conto nelle scelte 3 e 4 e nella regola sull'eccedenza (scelta 2).

[Fatto] C'è anche un problema di calendario sulla coesione. L'ottimizzatore conta 1,90 di fondi di coesione 2021-2027 come se fossero a regime, ma il fondo finisce nel 2029 (2030 per alcuni programmi) (`benchmark/fondi_coesione_bandi.md`, "Rischi trasversali").

---

## Scelta 1. Responsabilità e garanzia

### Proposta

**A. Una persona responsabile del programma, con nome e cognome.**

- **Ruolo.** Firma ogni scelta politica:
  - le varianti imposte, come quelle del 9, 10, 12 e 13 novembre;
  - le deroghe all'esito del motore;
  - le eccezioni alla regola del nucleo.

  Per ognuna pubblica il prezzo, cioè chi scende e chi perde, come già si fa nel punto 6 del programma.
- **Doveri.**
  - Risponde per iscritto, entro 30 giorni, ai rilievi del comitato di garanzia e alle obiezioni dell'opposizione leale.
  - Pubblica ogni anno un rendiconto con le scelte fatte, le previsioni sbagliate (punteggio di Brier, già previsto in `governo/regolamento.md`), i finanziamenti ricevuti e i propri interessi economici.
- **Limiti.**
  - Non cambia da sola Carta, rubrica, regole del motore, regolamento e istruzioni degli agenti.
  - Non modera la comunità.
  - Non fa parte del comitato di garanzia.
  - Non modifica i punteggi del panel.
- **Durata.** Due anni, rinnovabili una volta. Nomina una persona vice con un percorso professionale diverso, che la sostituisce se ha un conflitto di interessi.
- **Chi la sceglie.** All'inizio il gruppo che ha avviato il progetto, con un atto pubblico e motivato. Quando nascerà un'associazione, la sceglierà l'assemblea dei soci. Il comitato ne verifica i requisiti, cioè le incompatibilità qui sotto, ma non ne giudica le idee.

**B. Un comitato di garanzia di 7 persone.**

| Componente | Quante | Come si sceglie | Durata |
|---|---|---|---|
| Persone sorteggiate | 3 | Sorteggio pubblico tra chi si candida (comunità e cittadinanza), con quote per genere, fascia d'età e macro-area (Nord, Centro, Sud e isole) | 18 mesi, non rinnovabili |
| Persone esperte indipendenti | 4 | Avviso pubblico. Le 3 persone sorteggiate formano una rosa di 8 candidature e scelgono 4 nomi a maggioranza. Servono competenze diverse: diritto costituzionale, finanza pubblica, statistica e valutazione delle politiche, etica dei dati e dell'AI | 3 anni, non rinnovabili subito; rinnovo sfalsato |

- Almeno 3 componenti per genere.
- La presidenza ruota ogni anno tra i componenti. Una persona sorteggiata la tiene almeno un anno su tre.
- Il pluralismo si verifica sui percorsi pubblici delle persone, non sulle tessere. Non si usano etichette di partito.

**Poteri: garanzia, non indirizzo.**

1. **Approva le modifiche alle regole** con i due terzi dei voti, dopo almeno 30 giorni di commento pubblico. Le regole sono: Carta, rubrica, regole del motore, regolamento del Consiglio, ruoli e istruzioni degli agenti, regole della comunità. Se almeno il 10% delle persone iscritte attive si oppone, la modifica va all'assemblea di persone sorteggiate (08-P1) quando esisterà, e fino ad allora a un referendum interno.
2. **Controlla che le scelte politiche siano dichiarate.** Se una scelta del responsabile non ha la motivazione o il prezzo dichiarato, il comitato può sospenderne la pubblicazione per 15 giorni, finché arriva la motivazione. Non giudica il merito della scelta.
3. **Fa controllare dall'esterno.** Ogni anno affida a soggetti esterni un controllo delle istruzioni degli agenti e test di parzialità sui temi divisivi, come prevede 08-P1, art. 8. Avvia anche il panel umano che affiancherà quello AI.
4. **Decide in ultima istanza sui ricorsi** sulla moderazione e sui conflitti di interesse.
5. **Pubblica i registri** di finanziamenti, interessi e modifiche.

Il comitato **non** scrive proposte, non cambia i punteggi e non sceglie tra le opzioni politiche.

**Incompatibilità.** Non possono far parte del comitato:

- persone con cariche di partito, cariche elettive o candidature negli ultimi 3 anni, e per 2 anni dopo il mandato;
- persone che fanno lobbying registrato;
- persone con contratti o rapporti economici con il progetto, con la persona responsabile o con le sue società;
- persone che fanno parte del panel di valutazione o della moderazione.

**Conflitti di interesse.**

- Dichiarazione pubblica degli interessi all'ingresso e ogni anno.
- Obbligo di astenersi sulle questioni in cui c'è un interesse.
- Registro pubblico delle astensioni.
- Le persone sorteggiate ricevono un rimborso spese e un gettone, così possono partecipare anche le persone che non hanno tempo libero pagato. Le fonti di questo denaro sono pubbliche.

**Rapporto con la frase "sul sito nessuno decide".** La regola resta valida per lo spazio della comunità: lì si discute e si prendono appunti con l'AI (`comunita/regole.md`). La proposta la completa:

- le decisioni sul contenuto avvengono fuori dal sito, in luoghi dichiarati: la persona responsabile per le scelte politiche, il motore e il panel per le valutazioni, in futuro l'assemblea sorteggiata per i pesi;
- il comitato non decide il contenuto: garantisce che le regole siano uguali per tutti e che chi decide abbia un nome.

Così "nessuno decide sul sito" non diventa "nessuno risponde".

### Motivazione con la Carta

- **FID** (fiducia e trasparenza). La domanda della Carta "chi decide ne risponde?" oggi non ha risposta. Tutte e quattro le revisioni politiche chiedono persone vere (`revisioni/2026-11-08_sintesi_red_team.md`, punto 8). La revisione civica avverte che chi possiede il repository possiede il movimento (`revisioni/2026-11-08_red_team_civico.md`, sez. 6).
- **CIT** (cittadinanza responsabile). Il sorteggio e il potere di opposizione della comunità.
- **FUT** (responsabilità verso il futuro). Le regole durano oltre chi le ha scritte: rinnovi sfalsati, maggioranza dei due terzi.

### Conto

- **0 mld** sul bilancio pubblico: è il governo interno del progetto.
- Il costo interno (gettoni, avvisi, controlli esterni) è un dato da acquisire, da pubblicare nel registro dei finanziamenti.

### Chi guadagna e chi perde

- **Guadagnano:** chi usa il programma e deve potersi fidare; la comunità, che ottiene un potere di opposizione alle modifiche.
- **Perde:** chi guida oggi il progetto, che rinuncia a cambiare da solo Carta, rubrica e istruzioni degli agenti e diventa una persona che risponde in pubblico.

### Rischi

- **Lentezza:** 30 giorni per ogni modifica alle regole. Si mitiga con una procedura d'urgenza solo per correzioni di errori materiali, ratificata dopo.
- **Comitato catturato da chi lo nomina.** Si mitiga perché le persone esperte le scelgono le persone sorteggiate.
- **Poche candidature al sorteggio.** Si mitiga con il gettone e con un modulo che non richiede GitHub.

### Alternativa scartata

**Comitato di soli esponenti delle "aree culturali"**, una persona per area, come propone `revisioni/2026-11-08_analista_politico.md`. L'ho scartato per due motivi:

- reintroduce le etichette che il progetto vuole superare;
- spinge ogni persona a fare da rappresentante della propria area invece che da garante.

Il pluralismo resta, ma come requisito verificato sui percorsi delle persone.

---

## Scelta 2. Coperture regressive

### I fatti

[Fatto] Le coperture regressive valgono circa 2,3, il 30% di 7,42 (`23_equita_e_linguaggio.md`, sez. 4):

| Copertura | Gettito minimo | Compensazione oggi |
|---|---|---|
| AS01 tabacco | 0,60 | nessuna |
| AS02 tabacco riscaldato e sigarette elettroniche | 0,15 | nessuna |
| AS03 bevande zuccherate | 0,15 | nessuna |
| SAD13 + SAD01 gasolio per autotrasporto e agricoltura | 1,10 | rinnovo delle flotte, già sottratto dal gettito: circa 0,4 in SAD13 e 0,10-0,15 in SAD01 (note in `coperture_menu.csv`) |
| SAD02 gasolio agricolo | 0,15 | credito per piccole aziende e montagna (0,05) |
| SAD10 gasolio e GPL da riscaldamento | 0,02 | salvaguardia per ISEE fino a 15.000 € |
| RP01 e RP08 ricambio del personale | 0,09 | clausole di ritorno al 100% se i servizi peggiorano |

Senza compensazione restano quindi le tre accise sulla salute: **0,90**.

[Stima mia] Dal lato della spesa il programma va soprattutto a chi ha meno: 5,12 dei 9,17 di spesa vanno a misure con punteggio di equità di almeno +1,5. Le principali:

- 02-C2 nidi: 2,00;
- 06-C3 Case della Comunità: 0,80;
- 05-C4 lauree e diplomi terziari: 0,45;
- 04-P6 aree interne: 0,42;
- 05-C1 squadre contro la dispersione: 0,25.

Fonte: `motore/esito_proposte.csv` e `programma/selezione_intermedio.csv`. Il bilancio complessivo è quindi più progressivo delle singole coperture. Però la Carta chiede una compensazione legata alla misura, non solo un saldo generale.

[Fatto esterno] Secondo la Banca Mondiale, i forti aumenti di prezzo delle sigarette possono essere progressivi nel medio e lungo periodo. Il motivo: le famiglie con redditi bassi riducono di più il consumo e ricevono i benefici di salute maggiori. Il gettito aggiuntivo può finanziare il controllo del tabacco e l'equità. Fonte: Fuchs, Márquez, Dutta, González Icaza, *Is Tobacco Taxation Regressive?*, World Bank, 2019 ([pagina](https://openknowledge.worldbank.org/entities/publication/2e280cba-5002-573e-be74-337c23a22803), [PDF](https://documents1.worldbank.org/curated/en/893811554737147697/pdf/Is-Tobacco-Taxation-Regressive-Evidence-on-Public-Health-Domestic-Resource-Mobilization-and-Equity-Improvements.pdf)). Il beneficio arriva però solo a chi smette, e chi smette ha bisogno di aiuto.

### Proposta, misura per misura

| Copertura | Proposta | Costo nuovo | Da dove |
|---|---|---|---|
| AS01, AS02 (0,75) | **Servizio gratuito per smettere di fumare** in ogni Casa della Comunità hub (1.038): consulenza e farmaci gratuiti per chi ha un ISEE fino a 25.000 €, con priorità ai distretti con reddito più basso. Diventa un servizio minimo del contratto di prossimità (06-C3, art. 3) | circa 0,03 [stima mia: circa 10 milioni di persone che fumano (`23_equita_e_linguaggio.md`) × 1% di presa in carico all'anno × circa 300 € a percorso] | Dentro il fondo di 06-C3 (0,80): circa il 4% del fondo |
| AS01, AS02, AS03 (0,90) | **Vincolo di destinazione scritto in legge**: il gettito delle tre accise è destinato a 06-C3 e 06-C8 (0,80 + 0,10 = 0,90). Se il gettito scende sotto il minimo, la differenza non si recupera tagliando quei servizi | 0 | Contabile: le risorse generali sono fungibili. Il vincolo rende visibile la compensazione e protegge i servizi |
| AS01, AS02, AS03 | **Regola dell'eccedenza**: il gettito certificato dalla RGS sopra il minimo (fino a +0,40 per AS01, +0,20 per AS02, +0,10 per AS03 secondo i massimi del menu) va, in quest'ordine: 1) a chiudere l'eventuale scopertura degli anni di passaggio, senza deficit; 2) fino a 0,05 per estendere il servizio per smettere di fumare e la prevenzione nei distretti più poveri; 3) alla riserva per il dopo 2029 (scelta 4); 4) a riduzione del debito | 0 prima di incassare | Solo gettito incassato e certificato |
| AS03 bevande zuccherate (0,15) | Nessun trasferimento in denaro. Acqua potabile gratuita nelle scuole aperte di 05-C5, dentro il bilancio di quella misura. Monitoraggio dei prezzi e della riformulazione dei prodotti | 0 | Dentro 05-C5 |
| SAD13, SAD01, SAD02 (1,25) | **Spostare le compensazioni che esistono già**, senza aumentarle, verso le imprese con 1-3 veicoli, le aziende agricole piccole e di montagna, il Mezzogiorno e le isole. Per le famiglie l'effetto passa dai prezzi ed è diffuso: [stima mia] 1,25 su consumi delle famiglie di oltre 1.100 mld l'anno (ISTAT, conti nazionali, ordine di grandezza) vale circa lo 0,1% dei consumi, distribuito su 8 anni | 0 | Compensazioni già nette nel gettito |
| SAD10 (0,02) | Restano la salvaguardia per ISEE fino a 15.000 € e il contributo per le pompe di calore. Nessun cambio | 0 | — |
| RP01, RP08 (0,09) | Restano le clausole di ritorno al 100% se i servizi peggiorano. Si rende pubblico ogni anno, per Regione, il numero di posti non sostituiti, perché pesano di più su chi cerca lavoro al Sud | 0 | — |

Da segnalare per l'equità di genere, senza nuove proposte: RB03, cioè la soglia del bonus per le lavoratrici madri da 40.000 a 32.000 € (0,10), e PE03, la chiusura di Opzione donna. Restano come sono, con un indicatore di genere obbligatorio (regola R1 di `23_equita_e_linguaggio.md`).

### Motivazione con la Carta

- **EQU.** Linea rossa: nessun costo su chi ha meno senza compensazione (art. 3 c. 2 e art. 53 Cost.). La compensazione qui è in servizi, cioè l'aiuto a smettere, ed è legata alla misura.
- **FUT e BEN.** Le accise sulla salute e l'uscita dai sussidi dannosi riducono malattie ed emissioni future. Ridurle per "compensare" toglierebbe benefici proprio alle generazioni future e alle persone con redditi bassi che smettono.
- **Credibilità dei conti.** Non si spende gettito che non è ancora entrato.

### Conto

- **Spesa nuova: 0.**
- Riallocazione interna: circa 0,03 dentro 06-C3.
- Eventuale aggiunta di 0,05 solo se il gettito sopra il minimo viene incassato e certificato.

### Chi guadagna e chi perde

- **Guadagnano:**
  - le persone che fumano con ISEE basso, che ottengono un aiuto gratuito per smettere;
  - i distretti più poveri;
  - le piccole imprese di trasporto e le piccole aziende agricole, che ricevono una quota più alta delle compensazioni.
- **Perdono:**
  - gli altri servizi delle Case della Comunità, per circa 0,03;
  - le imprese di trasporto più grandi, che ricevono una quota più bassa delle compensazioni;
  - nel breve periodo, chi continua a fumare e ha un reddito basso: paga circa 0,50 € a pacchetto in più. È un costo vero e lo dichiaro.

### Rischi

- La quota di persone che fumano per fascia di reddito è un dato da acquisire: la stima del servizio può essere sbagliata.
- Il vincolo di destinazione può sembrare solo un'etichetta, perché le risorse sono fungibili. Diventa sostanziale solo con la clausola che protegge i servizi se il gettito cala.
- Contrabbando: è già considerato nel gettito minimo di AS01.

### Alternativa scartata

**Compensazione in denaro alle famiglie con ISEE basso**, per esempio una maggiorazione dell'Assegno unico o di 02-C4.

- Per coprire 0,90 servirebbero 0,90 di risorse che non ci sono.
- Arriverebbe anche a chi non fuma e quindi non paga l'accisa.
- Ridurrebbe lo scopo di salute.

Ho scartato anche **togliere AS01**: vorrebbe dire rinunciare a 0,60 e al beneficio di salute, che va soprattutto a chi ha meno.

---

## Scelta 3. Personale infermieristico nuovo (06-C2)

### I fatti

[Fatto] Il problema:

- 6,9 infermiere e infermieri ogni 1.000 abitanti, contro 9,2 della media OCSE;
- il personale infermieristico e medico delle Case della Comunità è contato in 06-C2, non in 06-C3. Quindi 06-C3 (0,80, nucleo robusto) paga gestione, servizi e assistenza a domicilio, ma non il personale nuovo.

Fonte: `programma/schede/06_salute.md`, 06-C2 e 06-C3.

[Fatto] Le varianti di 06-C2 (`programma/varianti/06_salute.csv`):

| Variante | Costo a regime | Contenuto principale |
|---|---|---|
| PILOTA | 0,35 (2029) | 4 Regioni, almeno 2 del Mezzogiorno, e aree interne; 5.000 borse; pratica avanzata in 50 CdC; valutazione Agenas a 30 mesi |
| ESSENZIALE | 1,4 | Versione intermedia |
| PIENA | 2,5 | Pacchetto completo |

[Fatto] Il motore classifica 06-C2 come "dipendente dai valori", con valore per miliardo di 0,37 (`motore/esito_proposte.csv`). [Valutazione] Il motore somma le utilità delle misure una per una e non vede che 06-C2 rende più efficace 06-C3. È l'argomento principale per farla entrare.

[Fatto, verifiche `prova_y`]

- Aggiungere 06-C2 PILOTA al programma intermedio così com'è: **nessuna soluzione ammissibile**.
- Senza forzare le misure di innovazione, l'ottimizzatore fa entrare il pilota togliendo del tutto 01-P13 e azzerando 04-P8. Così però resta attiva SF16, cioè la chiusura del patent box, che il menu vincola proprio a 01-P13: le imprese perderebbero un incentivo alla ricerca senza riceverne un altro.
- Con 01-P13 in versione essenziale, 04-P8 a zero, 09-C9 pilota e 04-P9 essenziale, l'ottimizzatore lascia libere **esattamente 0,25** di risorse generali: è ammissibile con `--riserva 0,25`, non con 0,26. La coesione 2021-2027 scende a 1,86 su 2,00 di capienza.

### Proposta

**06-C2 entra in versione PILOTA dal 2028, per 3 anni (2028-2030), con 0,35 l'anno così finanziati:**

| Fonte | Importo | Cosa paga |
|---|---|---|
| Risorse generali liberate (verificato) | 0,25 | Indennità di area disagiata nelle 4 Regioni pilota e nelle aree interne, e la parte nazionale delle borse |
| Fondi di coesione 2021-2027 (FSE+), entro il margine di 0,14 | 0,10 | Solo borse di studio e formazione alla pratica avanzata. **Nessuno stipendio e nessuna indennità**: la regola sul personale stabile è rispettata |

[Fatto] Il FSE+ paga fino al 2029, o fino al 2030 per i programmi che hanno spostato almeno il 10% delle risorse sulle nuove priorità. L'Italia lo ha fatto in 35 programmi su 48 (`benchmark/fondi_coesione_bandi.md`). Il pilota dura fino al 2030, quindi resta dentro questi tempi se si usano i programmi prorogati.

[Valutazione] L'ammissibilità delle borse per infermieristica al FSE+ va verificata con le autorità di gestione.

**Le 0,25 di risorse generali si liberano così:**

| Misura | Da | A | Risorse generali liberate |
|---|---|---|---|
| 01-P13 credito unico per la ricerca | PIENA | ESSENZIALE | 0,14 |
| 04-P8 camion a zero emissioni | ESSENZIALE | ZERO (restano le regole) | 0,06 (più 0,02 di coesione) |
| 09-C9 squadra per la produttività con l'AI | ESSENZIALE | PILOTA | 0,03 |
| 04-P9 consegne pulite in città | PIENA | ESSENZIALE | 0,02 (più 0,01 di coesione) |
| **Totale** | | | **0,25** |

SF16 resta coerente con il suo vincolo: 01-P13 in versione essenziale usa 0,15 di spese fiscali, dentro gli 0,20 di SF16.

**Regola per passare alla versione essenziale.** Si passa a ESSENZIALE (1,4, cioè 1,05 in più) solo se:

1. la valutazione Agenas a 30 mesi, fatta da soggetti diversi da chi attua il pilota, mostra più iscrizioni e meno dimissioni nelle aree pilota;
2. ci sono risorse certificate per farlo.

La prima fonte indicata è la crescita di RP08: da 0,05 a un massimo di 0,13 nel 2031, già destinata per legge a personale infermieristico e Case della Comunità (`programma/coperture_personale.md`). Lo dico con chiarezza: **oggi la versione essenziale non ha copertura**. Il pilota non è una promessa di arrivarci.

### Motivazione con la Carta

- **Regola 7, prima il nucleo robusto.** Senza personale, la spesa per le Case della Comunità (0,80, nucleo robusto) rende meno. Il pilota protegge una spesa già decisa.
- **FUT.** Le borse con vincolo di servizio nel SSN formano personale per i prossimi 30 anni. La carenza cresce con l'invecchiamento della popolazione.
- **EQU.** Le Regioni pilota sono almeno per metà del Mezzogiorno, più le aree interne.
- **Credibilità dei conti.** Il passaggio alla versione essenziale è condizionato, e la parte pagata con fondi europei finisce con il pilota.

### Conto

| Voce | Importo |
|---|---|
| Spesa nuova | +0,35 |
| Risorse generali liberate | −0,25 |
| Coesione usata in più | +0,10 (su un margine di 0,14) |
| Spesa totale del programma | da 9,17 a circa 9,24 |
| Risorse generali | in pareggio, 7,01 |

### Chi guadagna e chi perde

- **Guadagnano:**
  - il personale infermieristico delle Regioni pilota e delle aree interne;
  - circa 5.000 studentesse e studenti l'anno con borsa;
  - chi vive dove le Case della Comunità oggi sono vuote.
- **Perdono:**
  - le piccole imprese che fanno ricerca: il credito unico cresce meno, 0,16 invece di 0,30;
  - l'autotrasporto, che perde il sostegno ai camion a zero emissioni (restano le regole);
  - le città, che avranno meno micro-hub per le consegne;
  - la PA: la squadra per la produttività con l'AI resta pilota, circa 25 persone invece di circa 70.

Queste ultime sono scelte politiche del 9 e 10 novembre che qui si annullano in parte. Lo dichiaro.

### Rischi

- La parte di stima sui costi interni del pilota è mia: il file delle varianti non separa borse e indennità.
- Le indennità possono spostare personale da una Regione all'altra senza aumentarlo. Per questo sono legate alla permanenza in servizio (art. 3 della scheda).
- Il pilota aggiunge 0,35 nel 2028-2030, proprio negli anni in cui le coperture sono ancora in salita (vedi l'inizio del documento).
- Le borse già assegnate pesano anche nel 2031: circa 0,025 [stima mia: 5.000 borse × 5.000 €], da pagare con le 0,25 di risorse generali.

### Alternative scartate

- **ESSENZIALE subito (1,4).** Richiederebbe di abbassare il nucleo robusto o di introdurre tasse nuove.
- **Togliere 01-P13 del tutto**, come fa l'ottimizzatore senza vincoli. Chiude il patent box senza rafforzare il credito per la ricerca: è un taglio netto agli incentivi per l'innovazione (valori INN e FUT) e rompe il vincolo di SF16.
- **Usare RA11**, cioè ridurre il personale della scuola seguendo il calo delle alunne e degli alunni, per pagare il personale infermieristico. Sposta il costo sulla scuola, quindi sulle generazioni più giovani, verso la sanità.

---

## Scelta 4. Fondi europei dopo il 2029

### I fatti

[Fatto] Servono 0,50 l'anno anche dopo il 2029 (`programma/coesione_dopo_2029.csv`):

| Misura | Importo |
|---|---|
| 03-P4 prevenzione dei rischi | 0,25 |
| 05-C2 conto personale di competenze | 0,15 |
| 05-C1 squadre contro la dispersione | 0,08 |
| 09-C8 staffetta delle competenze | 0,02 |
| **Totale** | **0,50** |

[Fatto] La situazione del nuovo bilancio europeo:

- per il 2028-2034 la Commissione propone un fondo unico da 865 mld, con almeno il 14% per gli obiettivi sociali;
- a giugno 2026 il Consiglio ha trovato un accordo sui regolamenti, ma senza importi;
- la dotazione per l'Italia è un dato da acquisire;
- i primi anni di un nuovo ciclo di solito spendono poco.

Fonte: `benchmark/fondi_coesione_bandi.md`, sezione "Dopo il 2029".

### Proposta

**Decidere ora una riserva nazionale, che si attiva solo se mancano i fondi europei.**

1. **Una clausola di subentro nella prima legge di bilancio (2027).** Per ognuna delle quattro misure la legge indica:
   - il fondo europeo che dovrebbe subentrare;
   - una riserva nazionale con un nome preciso.
2. **Un controllo a data fissa.** Entro il 31 marzo 2029, in tempo per il Documento di finanza pubblica di aprile, il governo pubblica misura per misura quanto il piano italiano 2028-2034 copre davvero, e da quando.
3. **Attivazione automatica.** Se la copertura europea manca o parte dopo il 2030, la legge di bilancio 2030 attiva la riserva nazionale per la parte scoperta. Mai deficit, mai rinnovi automatici.

| Misura | Primo successore europeo | Riserva nazionale, solo su importi certificati dalla RGS |
|---|---|---|
| 05-C2 conto competenze (0,15) | FSE+ 2028-2034: la formazione è il suo campo tipico | Gettito di RA12 sopra il minimo (fondo Nuove Competenze e quota dello 0,30%, intervallo 0,15-0,40), già vincolato al conto competenze. Se non basta, la dote scende alla sola parte nazionale (0,30) |
| 09-C8 staffetta (0,02) | FSE+ | Gettito di RP01 sopra il minimo (intervallo 0,04-0,10): è il "risparmio del turnover" già indicato nel file |
| 05-C1 squadre contro la dispersione (0,08) | FSE+ | Riorganizzazione dell'organico scolastico seguendo il calo delle alunne e degli alunni, limitata a 0,08 (circa 1.800 posti tramite pensionamenti, a 45.000 €; [stima mia] sulla base di RA11). Il risparmio resta tutto nella scuola. È il successore già indicato in `coesione_dopo_2029.csv` |
| 03-P4 prevenzione dei rischi (0,25) | FESR 2028-2034, obiettivo adattamento | Riprogrammazione di risorse del Fondo sviluppo e coesione (FSC) 2021-2027 già stanziate e non ancora impegnate: 37,47 mld, impegni al 29,5%. Opere contro il dissesto, nel rispetto della quota per il Mezzogiorno. Va verificato con la RGS che le quote dopo il 2029 siano già nei conti a legislazione vigente: in quel caso non c'è deficit in più. Dato da acquisire |
| Ultima istanza | — | Riduzione in ordine fisso delle misure che non sono nel nucleo: prima 01-P13 da essenziale a zero (0,15), poi 04-P7 e i piloti di innovazione. Il nucleo robusto resta protetto |

Tutte le riserve si alimentano anche con la regola dell'eccedenza della scelta 2 (passo 3).

### Motivazione con la Carta

- **FUT, la linea rossa dell'art. 81.** Aspettare vuol dire lasciare un buco di 0,50 nel 2030, proprio negli anni in cui le coperture sono ancora in salita. È un conto lasciato a chi governerà dopo.
- **Credibilità dei conti.** Ogni riserva è indicata per nome e si attiva solo su importi certificati.
- **EQU.** La dispersione scolastica e la prevenzione nel Mezzogiorno restano protette.
- **SIC.** Il dissesto idrogeologico è un rischio misurato.

### Conto

| Voce | Importo |
|---|---|
| Spesa nuova oggi | 0 |
| Riserva potenziale dal 2030 | fino a 0,50 |
| di cui da coperture già vincolate alle stesse finalità (RA12, RP01) | 0,17 |
| di cui dalla scuola alla scuola | 0,08 |
| di cui dal FSC già stanziato | 0,25 |

### Chi guadagna e chi perde

- **Guadagnano:**
  - chi studia o si forma da adulto;
  - le scuole più fragili;
  - i territori a rischio di frane e alluvioni;
  - chi governerà dopo il 2029, che non trova un buco.
- **Perdono, solo se la riserva si attiva:**
  - chi si candida ai concorsi della scuola, con circa 1.800 posti in meno tramite pensionamenti;
  - i progetti FSC non ancora impegnati, che vengono spostati;
  - le imprese che usano il fondo Nuove Competenze.

### Rischi

- Il FSC conta nella spesa netta delle regole europee: va usato solo per spesa già nei conti a legislazione vigente.
- La riduzione dell'organico scolastico, anche se piccola, contraddice la scelta di non usare RA11. Per questo la limito a 0,08 e la tengo dentro la scuola.
- I primi anni del ciclo 2028-2034 possono avere un vuoto di cassa: il controllo del 31 marzo 2029 serve proprio a vederlo in tempo.

### Alternative scartate

- **Aspettare senza regola.** Lascia il buco del 2030.
- **Spostare subito 0,50 sulle risorse generali.** Oggi il margine è zero: vorrebbe dire tagliare il nucleo robusto per una spesa che il FSE+ probabilmente finanzierà, uno spreco certo contro un rischio possibile.

---

## Prossimi passi tecnici, da segnalare a chi guida il progetto (non li ho fatti)

1. Far leggere all'ottimizzatore `anno_regime` e `gradualita` e mostrare il saldo anno per anno dal 2027 al 2031.
2. Limitare COESIONE_2127 agli anni 2027-2029 (o 2030), come propone `benchmark/fondi_coesione_bandi.md`.
3. Se la proposta 3 viene accettata, aggiungere a 06-C2 PILOTA una riga di finanziamento su COESIONE_2127 da 0,10, limitata a borse e formazione. Così l'ottimizzatore può verificare direttamente lo scenario: io l'ho verificato solo in modo indiretto, con `--riserva 0,25`.
