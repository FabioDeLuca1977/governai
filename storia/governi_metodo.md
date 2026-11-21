# Confronto tra governi: metodo

Questo documento descrive come `storia/script/governi.py` confronta il governo in carica (dal 22 ottobre 2022) con i governi precedenti dal 1979. Lo script legge solo file del repository, non scarica nulla e dà sempre lo stesso risultato con gli stessi dati. Per rigenerare tutto: `python storia/script/governi.py`.

**Domanda.** Rispetto ai governi precedenti, come vanno i principali indicatori economici e sociali durante il mandato del governo in carica, tenendo conto degli shock esterni, del ciclo, dell'eredità ricevuta e dei ritardi con cui le misure agiscono?

**Cosa il metodo non fa.** Non stima l'effetto causale di un governo. Descrive cosa è successo in Italia durante ciascun mandato, confrontato con quello che è successo negli stessi anni in Francia, Germania e Spagna.

## 1. File

| File | Contenuto |
|---|---|
| `storia/governi.csv` | Elenco dei governi dal 1978 al 2026: id, numero d'ordine, data di giuramento (o di inizio) e di fine, legislatura, presidente del Consiglio, fonte |
| `storia/serie/*.csv` | Serie annuali (anno, paese, valore) per Italia, Francia, Germania, Spagna |
| `storia/decisioni_1977_2026.csv` | Catalogo di 120 decisioni con giudizio e solidità dell'evidenza |
| `storia/script/governi.py` | Calcoli e rapporto |
| `storia/governi_confronto.csv` | Risultati per governo, indicatore e versione (base e con ritardo di un anno) |
| `storia/governi_confronto.md` | Rapporto |
| `storia/script/punti_di_vista.py`, `storia/punti_di_vista.csv`, `storia/punti_di_vista_ambiti.csv`, `storia/punti_di_vista.md` | Punteggio da più punti di vista (21/11/2026) |

**Fonti dell'elenco dei governi.** Per i governi dal 2001: Presidenza del Consiglio, *I Governi nelle Legislature* (https://www.governo.it/it/i-governi-dal-1943-ad-oggi/i-governi-nelle-legislature/192), date di giuramento. Per i governi 1978-2001 la pagina della Presidenza non riporta le date: si usano i dati aperti della Camera dei deputati (https://dati.camera.it, classe `ocd:governo`), che registrano la data di inizio e di fine del governo; può differire di un giorno dal giuramento, il che non cambia l'assegnazione degli anni. Numero d'ordine: il secondo governo De Gasperi (13 luglio 1946), primo della Repubblica, è il n. 1; il governo in carica è il n. 68, in linea con i 68 governi della Repubblica indicati dalla Presidenza del Consiglio. Nel rapporto i governi sono indicati solo con le date.

## 2. Unità di confronto

1. **Governi di almeno 12 mesi.** Un governo che resta in carica almeno 12 mesi è un'unità di confronto.
2. **Periodi di governo.** I governi brevi (meno di 12 mesi) consecutivi della stessa legislatura sono uniti in un "periodo di governo", ma solo se nessuno di loro arriva a 12 mesi. Unioni risultanti:
   - periodo 1979-1981: governi n. 36, 37, 38 (VIII legislatura);
   - periodo 1982-1983: governi n. 40, 41 (VIII legislatura);
   - periodo 1986-1987: governi n. 43, 44 (IX legislatura).
3. **Governi brevi isolati.** Un governo breve che non si può unire (perché il vicino nella stessa legislatura supera i 12 mesi, o perché è solo nella legislatura) resta fuori dalla classifica; i suoi valori sono comunque nel CSV. Sono i governi n. 35, 45, 49, 51, 55, 62. Il governo n. 34 supera i 12 mesi ma è in carica soprattutto nel 1978, prima del periodo esaminato.
4. **Anni.** Ogni anno solare dal 1979 al 2025 va all'unità in carica per più giorni in quell'anno (per un periodo di governo si sommano i giorni dei governi che lo compongono). Quando nessuno supera la metà dell'anno (per esempio il 1979) vince chi ha più giorni. Conseguenze: il 2022 va al governo 2021-2022; il governo in carica ha gli anni 2023, 2024 e 2025. Gli anni 1992, 1994 e 2013 vanno a governi brevi e restano fuori dalla classifica.
5. **Previsioni escluse.** Si usano solo dati osservati fino al 2025 (il 2025 AMECO è un consuntivo provvisorio). Il 2026 è una previsione e non entra mai nei calcoli.

## 3. Indicatori

| Ambito | Indicatore | Serie | Calcolo | Verso |
|---|---|---|---|---|
| conti | Variazione del debito/PIL | `debito_pil` (AMECO) | ultimo anno meno anno prima del mandato | più basso è meglio |
| conti | Saldo primario medio | `saldo_primario_pil` (FMI, AMECO) | media degli anni | più alto è meglio |
| conti | Deficit medio | `deficit_pil` (FMI, AMECO), col segno cambiato | media degli anni | più basso è meglio |
| conti | Variazione della pressione fiscale | `pressione_fiscale_ocse` (OCSE, fino al 2024) | ultimo anno disponibile meno anno prima | nessun verso: solo ordinamento |
| crescita | Crescita media annua del PIL pro capite reale | `pil_pro_capite_crescita` (AMECO) | media dei tassi annui | più alto è meglio |
| crescita | Crescita media della produttività oraria | `produttivita_oraria_crescita` (AMECO) | media dei tassi annui | più alto è meglio |
| crescita | Investimenti pubblici medi/PIL | `investimenti_pubblici_pil` (AMECO, Italia dal 1995) | media degli anni | più alto è meglio |
| lavoro | Variazione del tasso di occupazione 15-64 | `occupazione_15_64` (OCSE) | fine meno anno prima | più alto è meglio |
| lavoro | Variazione dell'occupazione femminile 15-64 | `occupazione_femminile_15_64` (OCSE) | fine meno anno prima | più alto è meglio |
| lavoro | Variazione della disoccupazione giovanile 15-24 | `disoccupazione_giovanile` (OCSE) | fine meno anno prima | più basso è meglio |
| qualità del lavoro | Variazione della quota di dipendenti a tempo determinato | `dipendenti_tempo_determinato` (Eurostat lfsa_etgar, dal 1983; Spagna dal 1987) | fine meno anno prima | più basso è meglio |
| qualità del lavoro | Variazione del part-time involontario | `part_time_involontario` (Eurostat lfsa_eppgai, % degli occupati part-time; Francia dal 1992) | fine meno anno prima | più basso è meglio |
| qualità del lavoro | Crescita media annua del salario reale per dipendente | `salario_reale_crescita` (AMECO RWCDC: redditi da lavoro dipendente per dipendente, deflatore dei consumi privati) | media dei tassi annui | più alto è meglio |
| qualità del lavoro | Variazione delle ore lavorate per occupato | `ore_per_occupato` (AMECO NLHA; Germania Ovest prima del 1991) | fine meno anno prima, ore annue | nessun verso: solo ordinamento |
| prezzi e mercati | Spread medio con la Germania | `spread_bund` (AMECO) | media degli anni | più basso è meglio |
| prezzi e mercati | Inflazione media | `inflazione` (AMECO) | media degli anni | più basso è meglio |
| società | Variazione della povertà assoluta (persone) | `poverta_assoluta` (ISTAT, dal 2005) | fine meno anno prima | più basso è meglio |
| società | Emigrazione media annua di italiani | `emigrazione_cittadini` (ISTAT, dal 2002) | media degli anni, migliaia | più basso è meglio |

Scelte:

- **Variazioni.** Per un governo con anni assegnati da A a B la variazione è valore(B) meno valore(A-1). Così le variazioni di governi consecutivi si sommano senza buchi né doppi conteggi. Se l'ultimo anno manca (pressione fiscale OCSE nel 2025), si usa l'ultimo anno disponibile e lo si segnala.
- **Pressione fiscale.** Si usa la serie OCSE perché copre tutti i governi dal 1979 in modo omogeneo; il rapporto riporta come controllo la serie AMECO per il governo in carica (che arriva al 2025). Non si dà un verso: un aumento o un calo non è in sé un risultato migliore o peggiore. Il rango ordina dal calo maggiore all'aumento maggiore rispetto ai vicini ed è escluso dalla sintesi per ambito.
- **Investimenti pubblici** sono nell'ambito crescita perché misurano l'accumulazione di capitale pubblico, non la disciplina dei conti.
- **Povertà assoluta.** La serie ISTAT cambia metodo nel 2014: una variazione che attraversa il passaggio 2013/2014 non è calcolata (governo 2014-2016).
- **Qualità del lavoro (aggiunta il 20/11/2026).** Il tasso di occupazione conta le persone, non il tipo di contratto. Per questo si confrontano anche la quota di dipendenti a tempo determinato e il part-time involontario (chi lavora a tempo parziale ma vorrebbe il tempo pieno). Un calo è considerato un miglioramento. È un ambito a parte, così il dato sulla quantità del lavoro e quello sulla qualità restano visibili separatamente. Nel 2021 l'indagine europea sulle forze di lavoro ha cambiato regolamento: piccola rottura di serie, non corretta. Dal 21/11/2026 l'ambito comprende anche il salario reale per dipendente (redditi da lavoro dipendente divisi per i dipendenti, deflazionati con i prezzi dei consumi privati: misura il potere d'acquisto medio, compresi i contributi a carico del datore di lavoro) e le ore lavorate per occupato. Le ore non hanno un verso e sono escluse dalla sintesi, come la pressione fiscale: meno ore può voler dire più tempo libero o sottoccupazione. Per i governi prima del 1987 la sintesi dell'ambito si basa sul solo salario.
- **Emigrazione.** I dati italiani (ISTAT, cancellazioni anagrafiche) e quelli degli altri paesi (Eurostat) hanno definizioni diverse e la base dati non contiene la popolazione per rapportarli: non si fa il confronto con i vicini. La serie cresce quasi ogni anno dal 2008, quindi il rango riflette in buona parte la tendenza.

## 4. Misura principale: rispetto ai vicini

Per ogni indicatore con un confronto omogeneo: **differenza = valore Italia meno media di Francia, Germania e Spagna sugli stessi anni** (differenza nelle differenze per le variazioni: variazione italiana meno variazione media dei vicini). Toglie la parte comune degli shock (crisi dell'euro, pandemia, energia, politica della BCE, ciclo europeo).

- La media dei vicini si calcola anno per anno con i paesi disponibili, se sono almeno 2 su 3 (per deficit e saldo primario prima del 1995 manca la Spagna; il CSV lo segnala).
- Per lo spread la Germania vale 0 per definizione (è il riferimento): la media dei vicini è (spread Francia + spread Spagna + 0) / 3.
- Prima del 1991 i dati della Germania sono quelli della Germania Ovest.

## 5. Ranghi e sintesi per ambito

- **Rango.** Per ogni indicatore si ordinano tutte le unità confrontabili con un valore disponibile: 1° = risultato migliore rispetto ai vicini (per povertà ed emigrazione: sul dato italiano). Il numero di unità cambia da indicatore a indicatore (per esempio 24 per la crescita, 15 per gli investimenti pubblici). Il CSV riporta anche il rango sul solo dato italiano, per mostrare l'effetto della correzione.
- **Nessun punteggio con pesi scelti da noi.** Il peso di conti, crescita, lavoro, qualità del lavoro, prezzi e società è una scelta politica. Il punteggio complessivo si calcola quindi da molti punti di vista (sezione «Punteggio da più punti di vista»).
- **Sintesi per ambito.** Per ogni indicatore con un verso, la posizione si trasforma in una scala 0-100 (100 = primo, 0 = ultimo: 100 × (N − rango) / (N − 1)); la sintesi dell'ambito è la mediana di queste posizioni. Fasce: primo terzo (≥ 66,7), terzo centrale, ultimo terzo (< 33,3).
- **Controllo per pochi anni.** Il rapporto mostra anche il rango del governo in carica tra le sole unità con almeno due anni assegnati, perché un'unità con un solo anno ha valori più estremi per semplice variabilità.

## 6. Contesto ed eredità

- **Punto di partenza ereditato**: debito, deficit e spread dell'anno prima del primo anno assegnato.
- **Shock esterni** (solo per la lettura, non correggono i numeri): secondo shock petrolifero 1979-80 (aggiunto per completezza), crisi valutaria 1992-93, crisi finanziaria 2008-09, crisi dei debiti sovrani 2011-12, pandemia 2020, energia e rialzo dei tassi 2022-23.
- **Decisioni già prese** dai governi precedenti con effetti nel mandato (per il governo in carica: crediti edilizi, PNRR) sono richiamate nel testo.

## 7. Ritardi

Versione "ritardo_1_anno": a ogni unità si assegnano gli anni spostati in avanti di uno (A+1 … B+1), sempre senza previsioni. Per il governo in carica gli anni diventano 2024-2025. I ranghi si ricalcolano su questa versione. Coglie solo i ritardi brevi.

## 8. Decisioni del catalogo

Ogni decisione del catalogo è assegnata al governo dello stesso presidente del Consiglio in carica per più giorni nell'anno della decisione; quando lo stesso presidente guida due governi nello stesso anno l'assegnazione è segnata come incerta. Per ogni governo si contano i giudizi. **Avvertenza**: la selezione del catalogo è soggettiva e il numero di decisioni per governo dipende da essa; non va usata come voto.

## 9. Limiti

1. Mandato in corso: tre anni di dati (2023-2025), con il 2025 provvisorio; il 2026 è escluso perché è una previsione.
2. Ritardi lunghi (pensioni, istruzione, investimenti) non misurabili con questo metodo.
3. Molti governi hanno uno o due anni assegnati: i ranghi sono instabili.
4. Nessuna causalità: la differenza con i vicini non toglie gli shock che colpiscono l'Italia più degli altri (energia, debito alto con tassi in salita, demografia).
5. Eredità e decisioni precedenti pesano sui risultati di ogni mandato.
6. Dati non omogenei tra paesi e nel tempo (Germania Ovest, Spagna prima del 1995, cambio di metodo della povertà, rischio di cambio nello spread prima del 1999).
7. Indicatori limitati: non coprono qualità dei servizi, giustizia, ambiente, istruzione, sicurezza.
8. Il verso "più basso è meglio" per deficit, debito, inflazione ed emigrazione è una convenzione, non sempre valida (un deficit alto in recessione può essere appropriato).

## Vista per legislatura (20/11/2026)

Lo stesso confronto si può leggere per legislatura (`storia/script/legislature.py`, risultati in
`storia/legislature_confronto.csv` e `.md`). Cambia solo l'unità: una legislatura comprende i governi che
`storia/governi.csv` le attribuisce, compresi quelli rimasti in carica per gli affari correnti dopo le elezioni;
ogni anno solare va alla legislatura con più giorni di governo. La VII legislatura, iniziata prima del 1979, resta
fuori perché ne entrerebbe solo la parte finale. Indicatori, confronto con i vicini, posti e versione con gli anni
spostati di uno sono identici. Lo script va rilanciato a mano dopo `governi.py`.

## Punteggio da più punti di vista (21/11/2026)

**Perché.** Un punteggio unico richiede di decidere quanto pesa ogni ambito. Chi sceglie i pesi sceglie anche il vincitore. Un giudizio equo è quello che resta valido cambiando punto di vista.

**Come** (`python storia/script/punti_di_vista.py`, dopo `governi.py` e `legislature.py`):

1. Base: la posizione 0-100 di ogni unità in ogni ambito (mediana degli indicatori con un verso, sezione 5). Un ambito senza dati resta fuori e i pesi degli altri si riproporzionano.
2. 14 punti di vista dichiarati: pesi uguali e, uno per volta, ciascun ambito con peso doppio; ognuno con gli anni del mandato e con gli anni spostati di uno.
3. 4.000 punti di vista casuali: 2.000 combinazioni di pesi estratte in modo uniforme tra tutte quelle possibili (Dirichlet con parametri pari a 1, seme 20261121) per ciascuna delle due versioni degli anni. È l'analisi di sensibilità raccomandata dal manuale OCSE-JRC sugli indicatori compositi (*Handbook on Constructing Composite Indicators*, 2008).
4. Per ogni punto di vista: media pesata delle posizioni per ambito, posto tra le unità (a pari merito, posto medio), posizione 0-100.
5. **Punteggio equo** = mediana delle posizioni sui 4.000 punti di vista casuali; intervallo = 10° e 90° percentile; quota dei punti di vista nel primo e nell'ultimo terzo; posto migliore e peggiore nei 14 dichiarati.

**Che cosa.** Il punteggio dice quanto un governo o una legislatura sta in alto rispetto agli altri, con quasi tutti i pesi o solo con alcuni. Non dice se un risultato è stato causato dal governo.

**Chi.** Lo script non sceglie i pesi. Nella pagina il lettore può fissare i propri (da «non conta» a «conta il triplo») e vedere subito l'ordine che ne risulta.

**Limiti.** Le posizioni sono relative agli altri governi, non assolute. Gli ambiti hanno un numero diverso di indicatori. Prima del 2001 manca la società e prima del 1987 la qualità del lavoro si basa sul solo salario. Le combinazioni casuali danno in media lo stesso peso a ogni ambito.
