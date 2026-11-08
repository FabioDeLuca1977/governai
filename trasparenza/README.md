# Trasparenza: indicatori di rischio negli appalti pubblici

*Agente "integrità degli appalti" di GovernAI, 8 novembre 2026.*

> ## Avviso
> **Un indicatore di rischio NON è una prova né un'accusa.** Misura quanto le procedure di un ente si discostano dalla media nazionale per contratti simili. Molti scostamenti hanno spiegazioni legittime: urgenze vere (alluvioni, sismi), mercati con un solo fornitore qualificato, deroghe previste dalla legge (difesa, protezione civile), errori o ritardi nell'invio dei dati ad ANAC.
> Gli indicatori servono a **orientare** controlli e trasparenza: controlli interni e responsabili anticorruzione (RPCT) degli enti, ANAC, Corte dei conti, revisori, giornalisti e cittadini che chiedono spiegazioni. **Ogni caso va verificato da persone competenti**, leggendo gli atti e sentendo l'ente, prima di trarre qualsiasi conclusione.
> Come prevede la Carta dei valori (valore 9, SIC), si analizzano **enti e settori, mai persone fisiche**. Nessun punteggio è attribuito a dipendenti, dirigenti, imprenditori o professionisti.

## File

| File | Contenuto |
|---|---|
| `indicatori.py` | Scarica i dati ANAC (se mancano), calcola gli indicatori per CIG, li aggrega per ente e per settore |
| `riservato/rischio_enti.csv` | Tutte le stazioni appaltanti (circa 23.900): per ogni indicatore N, O, E, tasso, atteso, intervallo di Wilson al 90%, rapporto di rischio; indice composito con IC 90% |
| `rischio_settori.csv` | Tassi nazionali per tipo di contratto e divisione CPV (settori con almeno 200 CIG), con IC 90% |
| `rapporto.md` | Le prime 20 stazioni appaltanti pubbliche e i dati che spiegano il punteggio |
| `istruzioni_lettura_atti.md` | Come il livello AI legge un bando o una determina e segnala elementi di rischio, con un modello di rapporto prudente |
| `grezzi/` | File ANAC scaricati (circa 520 MB) e cache del campione `campione_2024.pkl` (circa 230 MB; va cancellata per ricalcolare dai grezzi). Esclusi da git |

Esecuzione: `python trasparenza/indicatori.py` (circa 2 minuti dopo il download; il primo download richiede alcuni minuti).

## Dati

Fonte: **ANAC, Banca Dati Nazionale dei Contratti Pubblici (BDNCP), open data** (`dati.anticorruzione.it/opendata`, licenza CC BY 4.0; elenco dei dataset anche su dati.gov.it). Dataset usati:

| Dataset | Uso |
|---|---|
| CIG anno 2024 (12 file mensili) | Procedura, importo, oggetto, CPV, date di pubblicazione e scadenza, motivo di urgenza, ente |
| aggiudicazioni | Numero di offerte, ribasso, data di aggiudicazione |
| aggiudicatari | Operatore aggiudicatario (solo come codice anonimo, vedi sotto) |
| varianti | Presenza di varianti o modifiche contrattuali |
| stazioni-appaltanti | Natura giuridica dell'ente (per distinguere enti pubblici e società) |

**Campione**: tutti i CIG pubblicati nel 2024 (1,21 milioni). Dopo le esclusioni restano **904.301 CIG** di **23.910 stazioni appaltanti**, per circa 378 mld € a base di gara. Esclusioni: CIG cancellati, adesioni a convenzioni o accordi quadro senza nuovo confronto competitivo, affidamenti in house, CIG di sola tracciabilità (regole diverse). Per i CIG con più CPV si usa il prevalente.

Il portale ANAC blocca le richieste automatiche alle sue pagine (catalogo CKAN). I file di download si scaricano invece normalmente: gli URL sono quelli del catalogo nazionale dati.gov.it.

## Metodo

### Indicatori (per CIG: 1 = segnale, 0 = nessun segnale, vuoto = non valutabile)

| Indicatore | Definizione | Peso | Casi valutabili | Media nazionale 2024 |
|---|---|---|---|---|
| `offerta_unica` | Una sola offerta in procedure diverse dall'affidamento diretto, aggiudicate | 0,30 | 56.365 | 54,8% |
| `non_competitiva` | Affidamento diretto oltre le soglie dell'art. 50 d.lgs. 36/2023 (150.000 € lavori, 140.000 € servizi e forniture) o negoziata senza bando oltre la soglia UE (5,538 mln lavori, 221.000 € servizi e forniture; 443.000 € nei settori speciali) | 0,25 | 80.768 | 19,5% |
| `termini_brevi` | Meno di 15 giorni tra pubblicazione e scadenza delle offerte in procedure aperte o ristrette | 0,10 | 79.312 | 12,6% |
| `urgenza` | Motivo di somma o estrema urgenza dichiarato | 0,05 | 904.301 | 1,0% |
| `frazionamento` | Affidamenti diretti (da 5.000 €) allo stesso operatore, dallo stesso ente, nella stessa divisione CPV e tipo di contratto: ciascuno sotto la soglia dell'art. 50, la somma annua sopra | 0,10 | 687.161 | 5,4% |
| `riaffidamento` | Affidamento diretto a un operatore che nell'anno ne riceve almeno 3 dallo stesso ente nella stessa divisione CPV (principio di rotazione, art. 49) | 0,10 | 687.161 | 12,3% |
| `varianti` | Contratti da 40.000 € in su con almeno una variante o modifica comunicata | 0,05 | 194.607 | 1,4% |
| `ribasso_minimo` | Ribasso sotto l'1% con almeno 2 offerte (concorrenza solo apparente) | 0,05 | 22.962 | 8,9% |

**Perché questi pesi.** Il peso maggiore va ai due indicatori più validati: offerta unica e assenza di confronto competitivo. Sono il nucleo degli indicatori di Fazekas e Kocsis (2020) e due dei tre indicatori a cui il Single Market Scoreboard della Commissione dà peso triplo. Frazionamento e riaffidamento nascono dagli stessi gruppi di affidamenti e sono correlati: insieme pesano 0,20. Urgenza, varianti e ribasso minimo sono segnali più deboli o con dati incompleti: pesano 0,05 ciascuno. I pesi sono una scelta dichiarata, non una stima. Chi li vuole cambiare modifica il dizionario `INDICATORI` in `indicatori.py`.

**Coerenza con la letteratura.** Il tasso di offerta unica nel campione (54,8%) coincide con quello trovato dall'UIF sui dati ANAC 2018-2023 (55%; Gara, Iezzi e Siino 2024).

### Confronto con la media nazionale del settore

Per ogni ente e indicatore si confrontano:
- **O**: i segnali osservati;
- **E**: i segnali attesi se l'ente avesse i tassi nazionali **dello stesso tipo di contratto** (lavori, servizi, forniture) **e della stessa fascia d'importo** (<40k, 40–140k, 140k–1M, 1M–5,5M, >5,5M). È una standardizzazione indiretta: un ente che compra soprattutto farmaci non è confrontato con uno che fa piccoli lavori.

Il **rapporto di rischio** è (O+1)/(E+1): 1 significa in linea con l'atteso, 2 il doppio dei segnali attesi. Il +1 attenua le oscillazioni dovute al caso negli enti piccoli.

### Indice composito e intervalli di confidenza

- **Indice** = media geometrica pesata dei rapporti di rischio, sugli indicatori con almeno 10 casi valutabili. I pesi si rinormalizzano se un indicatore manca. Ogni rapporto è limitato tra 0,1 e 10.
- **IC 90%**: varianza del log-rapporto approssimata con 1/(O+1) (Poisson), sommata con i pesi al quadrato **assumendo indipendenza tra indicatori**. L'ipotesi è ottimistica, perché gli indicatori sono correlati: gli intervalli veri sono più larghi.
- Per ogni singolo indicatore c'è anche l'intervallo di Wilson al 90% del tasso.
- **Graduatoria**: per il **limite inferiore** dell'IC 90%, così un ente piccolo con pochi casi sfortunati non finisce in cima. Entrano solo **enti pubblici**, per natura giuridica ANAC (sono escluse società, anche partecipate, e soggetti privati), con almeno 50 CIG e 4 indicatori valutabili: **2.291 enti**. Di questi, 161 hanno il limite inferiore sopra 1, cioè più segnali dell'atteso anche nell'ipotesi più favorevole.
- L'indice mediano degli enti in graduatoria è circa 0,66, sotto 1. I tassi nazionali sono pesati per CIG, e i grandi acquirenti hanno più segnali della maggior parte degli enti. L'indice va letto come **posizione relativa**, non come scala assoluta.

### Protezione dei dati

- I codici fiscali degli aggiudicatari si trasformano subito in un codice anonimo (hash), usato solo per contare ripetizioni dentro lo stesso ente. Non compaiono in nessun output.
- Le stazioni appaltanti con codice fiscale personale (16 caratteri) o natura giuridica individuale sono escluse dall'output.
- Le stazioni appaltanti in output compaiono con denominazione e codice fiscale dell'ente: sono dati pubblici della BDNCP.

## Fonti verificate

- **ANAC**, progetto "Misurare la corruzione". Comprende indicatori di contesto e **17 tipologie di indicatori di rischio corruttivo negli appalti**, calcolati dalla BDNCP per provincia e distinti per oggetto (lavori, servizi, forniture), settore (ordinari, speciali) e anno. Pagine: anticorruzione.it/misura-la-corruzione e anticorruzione.it/rischio-corruttivo-negli-appalti. La pagina rimanda alla scheda PDF con l'elenco, non letta qui: i nostri indicatori non replicano quelli ANAC, ne seguono l'impostazione.
- **UIF – Banca d'Italia**: M. Gara, S. Iezzi, M. Siino, *Corruption risk indicators in public procurement: A proposal using Italian open data*, Quaderni dell'antiriciclaggio, Analisi e studi n. 23, settembre 2024. Propone 12 indicatori binari per gara sui dati ANAC 2018–giugno 2023 (2,3 milioni di aggiudicazioni). Tra questi: procedura discrezionale, affidamento diretto anomalo, offerta unica, inviti sotto il minimo, richiesta di subappalto, vincitore ricorrente, comunicazioni mancanti. Li aggrega per stazione appaltante e li valida con dati UIF riservati. Osserva che i **dati mancanti non sono casuali**: dipendono da tipo, area e dimensione dell'ente, con possibile sottostima del rischio per i piccoli enti del Centro-Sud. Raccomanda quindi confronti tra enti omogenei.
- **Fazekas M., Kocsis G.** (2020), *Uncovering High-Level Corruption: Cross-National Objective Corruption Risk Indicators Using Public Procurement Data*, British Journal of Political Science 50(1), 155–164. Usa l'offerta unica nei mercati competitivi e un indice composito di red flag, su circa 2,8 milioni di contratti di 28 Paesi europei.
- **Fazekas M., Tóth I. J., King L. P.** (2016), *An Objective Corruption Risk Index Using Public Procurement Data*, European Journal on Criminal Policy and Research 22(3), 369–397. Primo indice composito di rischio su dati oggettivi. Opentender.eu (progetto Horizon 2020 DIGIWHIST, Government Transparency Institute) lo applica a 35 giurisdizioni europee, Italia compresa.
- **Commissione europea, Single Market Scoreboard (appalti pubblici)**. Gli indicatori "single bidder" (quota di contratti con una sola offerta, accordi quadro esclusi) e "no calls for bids" (aggiudicazioni senza bando) hanno peso triplo, insieme al tasso di pubblicazione. Giudizio "buono" con offerta unica fino al 10%, "scarso" sopra il 20%; per le aggiudicazioni senza bando, buono fino al 5%, scarso dal 10%.
- **Commissione europea, ARACHNE**: strumento di data mining e punteggio di rischio per i fondi UE. Ha oltre 100 indicatori in 7 categorie: appalti, gestione del contratto, ammissibilità, performance, concentrazione, altro, allerte reputazionali. Il punteggio sostiene decisioni basate sul rischio, ma **non stabilisce automaticamente un'irregolarità**.
- **OCSE**: secondo i materiali sugli strumenti di gestione del rischio negli appalti, i red flag sono schemi che *possono* segnalare irregolarità, e la loro presenza non significa che ci sia frode o corruzione.
- **Banca Mondiale**: *Warning Signs of Fraud and Corruption in Procurement*, prima *Common Red Flags*, segnali d'allarme per fase di gara; Kenny e Musatova (2010), *'Red Flags of Corruption' in World Bank Projects*.
- **Norme**: d.lgs. 36/2023, art. 50 (affidamento diretto sotto 150.000 € per i lavori e 140.000 € per servizi e forniture), art. 49 (rotazione: vieta il riaffidamento al contraente uscente con lo stesso oggetto; deroga motivata, comma 4; deroga sotto 5.000 €, comma 6). Fonti: vademecum ANAC sugli affidamenti diretti (30.7.2024) e pareri ANAC. Le soglie UE 2024-25 di 5,538 mln e 221.000 € vanno ricontrollate a ogni aggiornamento biennale.

## Limiti

1. **Dati incompleti e non casuali.** Il numero di offerte è noto solo per 56.000 procedure non dirette su circa 191.000. Chi non comunica i dati ad ANAC sembra meno a rischio: la reticenza va misurata a parte. Un indicatore di "comunicazioni mancanti", come quelli UIF, è il primo sviluppo da fare.
2. **Anno 2024, il primo della digitalizzazione completa** (piattaforme certificate, PCP). Alcuni campi sono compilati in modo poco affidabile: `FLAG_URGENZA` vale 1 nel 68% dei CIG ed è quindi inutilizzabile, per questo si usa il motivo esplicito. Varianti e fine lavori di contratti del 2024 sono in gran parte ancora da registrare, quindi l'indicatore `varianti` è sottostimato.
3. **Mancano indicatori importanti della letteratura**: vincitori costituiti da poco (serve il Registro imprese, non aperto), ritardi e contenziosi (fine contratto e collaudi ancora assenti per il 2024; i ricorsi TAR non sono in open data), legami societari e titolari effettivi, prezzi unitari fuori mercato.
4. **Soglie e definizioni semplificate.** Le soglie UE sono quelle degli enti sub-centrali; non si distinguono le deroghe legittime (art. 76, unico operatore; somma urgenza; difesa). Il frazionamento è misurato per divisione CPV e anno solare, un'approssimazione dell'"oggetto" della norma.
5. **Correlazione tra indicatori**: l'IC dell'indice è ottimistico.
6. **Valori economici**: gli importi a base di gara contengono errori di compilazione, a volte miliardari. Sono solo informativi e non entrano nell'indice.
7. **Validazione assente.** A differenza dello studio UIF, qui non c'è un confronto con casi accertati: il cruscotto proposto (scheda 08-P7) prevede una validazione indipendente prima di ogni uso operativo.
8. **Mai uso automatico.** L'indice non può fondare da solo sanzioni, esclusioni o decisioni sulle persone (AI Act; Carta, linee rosse di INN e SIC). È uno strumento per scegliere dove guardare.


## Pubblicazione e tutela degli enti

Il repository è pubblico. Per questo:
- **i risultati per singolo ente** (`riservato/rischio_enti.csv` e `riservato/rapporto_enti.md`) **non vengono pubblicati**. Restano sul computer di chi esegue l'analisi e servono a orientare verifiche fatte da persone competenti, sentendo l'ente;
- **la versione pubblica** (`rapporto.md`, `rischio_settori.csv`) mostra solo dati aggregati per settore, tipo di ente e regione.

Un ente può comparire in alto per ragioni del tutto legittime, come alluvioni, emergenze o mercati con un solo fornitore. Pubblicarne il nome senza verifica sarebbe ingiusto e contrario ai valori di Rispetto e di Sicurezza senza controllo assoluto.
