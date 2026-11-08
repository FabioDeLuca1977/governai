# Rischio negli appalti pubblici: indicatori per stazione appaltante (2024)

*Generato da `trasparenza/indicatori.py` il 2026-11-08. Fonte: ANAC, BDNCP open data (CIG pubblicati nel 2024, aggiudicazioni, aggiudicatari, varianti, anagrafe stazioni appaltanti).*

> **Avviso.** Questi indicatori **non sono prove né accuse**. Misurano quanto le procedure di un ente si discostano dalla media nazionale per lo stesso tipo di contratti. Molti scostamenti hanno spiegazioni legittime: urgenze reali, mercati con un solo fornitore qualificato, errori o ritardi nella compilazione dei dati ANAC. L'elenco serve a **orientare** controlli interni, ANAC e Corte dei conti e a chiedere trasparenza; ogni caso va verificato da persone competenti, sentendo l'ente.

## Campione

- CIG analizzati (esclusi cancellati, adesioni a convenzioni/accordi quadro senza confronto, in house): **904.301**
- Stazioni appaltanti: **23.910**; in graduatoria (enti pubblici con almeno 50 CIG e 4 indicatori valutabili): **2.291**
- Valore a base di gara: **377,7 mld €**

## Indicatori, pesi e media nazionale

| Indicatore | Peso | Casi valutabili | Media nazionale |
|---|---|---|---|
| Offerta unica in procedure con confronto competitivo (`offerta_unica`) | 0.30 | 56.365 | 54.8% |
| Affidamento diretto oltre le soglie dell'art. 50 o negoziata senza bando oltre la soglia UE (`non_competitiva`) | 0.25 | 80.768 | 19.5% |
| Termine per le offerte sotto i 15 giorni in procedure aperte o ristrette (`termini_brevi`) | 0.10 | 79.312 | 12.6% |
| Ricorso dichiarato a somma o estrema urgenza (`urgenza`) | 0.05 | 904.301 | 1.0% |
| Affidamenti diretti allo stesso operatore. stesso ente e stessa categoria CPV. ciascuno sotto soglia ma con somma oltre soglia (`frazionamento`) | 0.10 | 687.161 | 5.4% |
| Affidamento diretto a un operatore che ha ricevuto almeno 3 affidamenti diretti dallo stesso ente nella stessa categoria CPV (rotazione) (`riaffidamento`) | 0.10 | 687.161 | 12.3% |
| Contratti da 40.000 euro in su con almeno una variante o modifica comunicata (`varianti`) | 0.05 | 194.607 | 1.4% |
| Ribasso inferiore all'1% in procedure con almeno 2 offerte (`ribasso_minimo`) | 0.05 | 22.962 | 8.9% |

**Indice composito.** Per ogni indicatore si confrontano i segnali osservati (O) con quelli attesi (E) se l'ente avesse i tassi nazionali del suo stesso mix di contratti (lavori/servizi/forniture × fascia d'importo). Rapporto di rischio = (O+1)/(E+1); l'indice è la media geometrica pesata dei rapporti (1 = in linea con la media nazionale; 2 = il doppio dei segnali attesi). L'intervallo al 90% assume indipendenza tra indicatori ed è quindi ottimistico. La graduatoria usa il **limite inferiore** dell'intervallo, per non premiare gli scostamenti dovuti al caso nei piccoli numeri.

## Quadro per tipo di ente e per regione (nessun ente nominato)

La versione pubblica non nomina singoli enti: un indicatore di rischio non è un accertamento e può dipendere da urgenze reali, mercati con pochi operatori o errori nei dati. L'elenco nominativo serve solo a orientare verifiche da parte di persone competenti e resta fuori dalla pubblicazione.

| Tipo di ente | Enti in graduatoria | Indice medio | Enti sopra l'atteso (IC 90%) |
|---|---|---|---|
| Enti Pubblici Non Economici | 1444 | 0.74 | 95 |
| Amministrazioni Pubbliche | 565 | 0.76 | 40 |
| Enti Pubblici Economici | 126 | 0.74 | 11 |
| Enti Ospedalieri | 78 | 0.80 | 11 |
| Aziende Regionali, Provinciali, Comunali E Loro Consorzi | 49 | 0.72 | 4 |
| Consorzi Ai Sensi Della L.142/90 | 19 | 0.71 | 0 |
| Enti Ed Istituti Di Previdenza E Di Assistenza Sociale | 7 | 0.65 | 0 |
| Azienda Speciale Di Ente Locale | 1 | 0.63 | 0 |
| Ente Diritto Pubblico | 1 | 0.83 | 0 |
| Aziende Autonome Di Cura, Soggiorno E Turismo | 1 | 0.66 | 0 |

| Regione | Enti in graduatoria | Indice medio | Enti sopra l'atteso (IC 90%) |
|---|---|---|---|
| Liguria | 63 | 0.91 | 9 |
| Sicilia | 157 | 0.87 | 14 |
| Emilia Romagna | 162 | 0.87 | 16 |
| Puglia | 139 | 0.85 | 12 |
| Basilicata | 32 | 0.84 | 3 |
| Centrale | 345 | 0.82 | 43 |
| Marche | 74 | 0.81 | 5 |
| Calabria | 59 | 0.76 | 4 |
| Umbria | 29 | 0.75 | 2 |
| Non Classificato | 76 | 0.73 | 8 |
| Campania | 143 | 0.73 | 8 |
| Lazio | 113 | 0.72 | 4 |
| Friuli Venezia Giulia | 43 | 0.72 | 5 |
| Abruzzo | 41 | 0.71 | 2 |
| Molise | 10 | 0.67 | 0 |
| Provincia Autonoma Di Bolzano | 69 | 0.67 | 4 |
| Veneto | 185 | 0.67 | 4 |
| Piemonte | 129 | 0.66 | 5 |
| Provincia Autonoma Di Trento | 35 | 0.66 | 2 |
| Sardegna | 47 | 0.62 | 0 |
| Toscana | 123 | 0.61 | 5 |
| Lombardia | 199 | 0.60 | 5 |
| Valle D'Aosta | 18 | 0.57 | 1 |

Tassi nazionali per settore (divisione CPV): `trasparenza/rischio_settori.csv`.

## Settori con i tassi più alti di offerta unica (almeno 200 casi valutabili)

| Contratto | CPV (divisione) | CIG | Valore (mln €) | Offerta unica | Non competitiva oltre soglia |
|---|---|---|---|---|---|
| Servizi | 60 | 8464 | 7008 | 84.1% (N=842) | 21.9% |
| Servizi | 72 | 29817 | 10639 | 76.7% (N=1274) | 36.3% |
| Forniture | 38 | 11496 | 2443 | 75.0% (N=908) | 22.4% |
| Servizi | 92 | 13428 | 2058 | 71.1% (N=543) | 17.6% |
| Forniture | 48 | 5117 | 3247 | 67.8% (N=385) | 22.0% |
| Servizi | 50 | 28378 | 13786 | 66.1% (N=1675) | 27.0% |
| Servizi | 85 | 20764 | 23599 | 65.8% (N=1863) | 25.2% |
| Servizi | 79 | 54348 | 6759 | 65.2% (N=2181) | 26.5% |
| Forniture | 33 | 94783 | 97495 | 65.2% (N=16565) | 11.9% |
| Forniture | 35 | 4476 | 1278 | 59.2% (N=201) | 31.1% |

## Come leggere (e come non leggere) questa tabella

- Un ente in cima non è un ente corrotto: è un ente le cui procedure **meritano una domanda**. La prima verifica è chiedere all'ente le motivazioni (determine a contrarre, motivazione dell'urgenza, indagini di mercato, deroghe alla rotazione).
- Grandi centrali di committenza e aziende sanitarie hanno mix di acquisti particolari (farmaci, dispositivi esclusivi): l'offerta unica può dipendere dal mercato.
- Difesa, Vigili del fuoco, prefetture (accoglienza) e protezione civile operano spesso con deroghe di legge (segretezza, somma urgenza, emergenze): lo scostamento va letto alla luce della norma applicata.
- Nei comuni piccoli e nelle aree interne gli operatori locali sono pochi: affidamenti ripetuti allo stesso operatore possono dipendere dal mercato, ma la deroga alla rotazione va comunque motivata (art. 49).
- I valori a base di gara possono contenere errori di compilazione (importi anomali): il valore in milioni è indicativo e non entra nell'indice.
- Gli enti che **non comunicano** i dati ad ANAC risultano meno a rischio di quanto siano: la mancanza di dati è a sua volta un segnale (UIF, Quaderno 23/2024) e va letta a parte.
- Nessuna persona fisica è valutata. I codici degli operatori economici sono usati solo come codici anonimi per contare ripetizioni dentro lo stesso ente.
