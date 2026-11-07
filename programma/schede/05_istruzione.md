# Schede pronte — Area 05: Istruzione, Università e Ricerca, Cultura, Sport e Giovani

*Agente ministeriale GovernAI, 7 novembre 2026. Fonti: dossier `ministeri/05_istruzione_ricerca_cultura.md`, verifica `dati/verifiche/05_istruzione.md`, serie `dati/serie/05_*.csv` e `02_demografia_nati_decessi_pop.csv`. Varianti e coperture: `programma/varianti/05_istruzione.csv`. Importi in mld €/anno, salvo diversa indicazione. "Stima GovernAI" = stima propria da verificare.*

## Premessa: il dividendo demografico, unica risorsa interna dell'area

- **Dato**: i nati in Italia passano da **485.780 (2015) a 355.435 (2025)**, -26,8% (Eurostat/ISTAT, `02_demografia_nati_decessi_pop.csv`). Chi entra in prima primaria dal 2031 è una coorte di circa 130 mila bambini più piccola di quella entrata nel 2021.
- **Cosa è già speso**: la L. 207/2024 (c. 828) ha già tagliato 5.660 posti comuni dall'a.s. 2025/26, e la nota MIM 10164/2026 toglie altri 1.407 posti di potenziamento nel 2026/27 (fonti di stampa specializzata). Questi risparmi sono **già nei tendenziali**: non li usiamo come copertura.
- **Cosa usiamo**: una **misura di copertura nuova (RIALLOCAZIONE)**, cioè un ulteriore adeguamento dei posti comuni al calo degli alunni, **solo tramite turnover** (nessun licenziamento), per circa 6.700 posti a regime × 45 mila € = **0,30 mld/anno**. Il ricavato viene reinvestito per intero nella scuola: 0,17 in 05-C1 (squadre anti-dispersione) e 0,13 in 05-C4 (ITS). L'adeguamento è una quota piccola del calo atteso degli alunni. La RGS deve certificare che conta solo la parte non già scontata nei tendenziali.
- **Altre coperture nuove proposte al menu**: Carta Valore resa selettiva con ISEE (RIORDINO_BONUS, 0,09); una quota della Carta del docente vincolata alla formazione su AI (RIORDINO_BONUS, 0,08-0,12); la trasformazione della detrazione per le spese sportive dei ragazzi (SPESE_FISCALI, 0,10, da verificare); la confluenza del Fondo Nuove Competenze e della quota 0,30% non optata nel Conto competenze (RIALLOCAZIONE, 0,3-0,5, da certificare).

---

## 05-C1 — "Nessuno escluso": squadre di prossimità contro la dispersione

**Problema in un dato.** L'abbandono precoce (ELET 18-24) è all'8,2% in Italia, ma al **13,7% nelle Isole** e al **10,1% tra i maschi** nel 2025 (Eurostat edat_lfse_16 ed edat_lfse_14; `05_elet_18_24_nuts1.csv`, `05_elet_18_24_sesso.csv`). Arriva al 44,1% tra gli stranieri arrivati a 16-24 anni (ISTAT 2026).

**Soluzione.** Un indice di fragilità di istituto individua le scuole a più alto rischio. In ciascuna lavora una squadra stabile: un tutor (docente riconvertito dal dividendo demografico), un educatore e un mediatore a rete. Si aggiungono il tutoraggio intensivo di matematica alla primaria, un percorso ponte con i CPIA per i neo-arrivati 16-24 e un sistema di allerta precoce che segnala ma non decide. Una valutazione controfattuale al terzo anno condiziona il rifinanziamento.

| Variante | Contenuto | Costo 2027/28/29 → regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | ~1.500 scuole (quintile più fragile) | 0,03 / 0,15 / 0,25 → **0,25** (2029) | 1 | RIALLOCAZIONE 0,17 (dividendo demografico), COESIONE_2127 0,08 (FSE+) |
| ESSENZIALE | ~750 scuole (decile più fragile) | 0,02 / 0,08 / 0,13 → **0,13** | 0,6 | RIALLOCAZIONE 0,10, COESIONE_2127 0,03 |
| PILOTA | 150 scuole randomizzate in 3 Regioni | 0,01 / 0,03 / 0,03 → 0,03 | 0,1 | COESIONE_2127 0,03 |

*Costo ricalibrato, come chiesto dalla verifica (0,2-0,3)*: educatori 0,06; mediatori 0,02; ponte CPIA 0,03; allerta e valutazione 0,01; esoneri dei tutor e tutoraggio di matematica 0,13 (stima GovernAI).

**Articolato normativo essenziale** (da inserire nella legge di bilancio, capo "Istruzione")

> **Art. 1 (Finalità).** Al fine di ridurre l'abbandono scolastico precoce e la dispersione implicita nei contesti a più alta concentrazione di svantaggio, in attuazione degli articoli 3 e 34 della Costituzione, è istituito il programma nazionale "Nessuno escluso".
>
> **Art. 2 (Indice di fragilità).** 1. Con decreto del Ministro dell'istruzione e del merito, sentito l'INVALSI e acquisito il parere del Garante per la protezione dei dati personali, da adottare entro novanta giorni dall'entrata in vigore della presente legge, è definito l'indice di fragilità delle istituzioni scolastiche, basato almeno sull'indice ESCS medio, sulla quota di alunni con background migratorio di recente arrivo e sui tassi di ripetenza e abbandono. 2. L'indice è usato esclusivamente per la ripartizione delle risorse e non è pubblicato in forma nominativa.
>
> **Art. 3 (Squadre di prossimità).** 1. Alle istituzioni scolastiche del quintile più fragile è assegnata una squadra composta da un docente tutor con esonero parziale, da un educatore professionale e da una quota di mediazione linguistico-culturale organizzata in rete. 2. I docenti tutor sono individuati prioritariamente tra i docenti in esubero o in soprannumero per effetto della riduzione della popolazione scolastica. 3. Le squadre attuano interventi di tutoraggio intensivo in matematica nella scuola primaria.
>
> **Art. 4 (Percorsi ponte e allerta precoce).** 1. Con accordo in Conferenza Stato-Regioni sono istituiti percorsi ponte biennali tra CPIA e istruzione e formazione professionale per i giovani di 16-24 anni di recente arrivo. 2. I sistemi di segnalazione precoce del rischio di abbandono sono conformi al regolamento (UE) 2024/1689. Sono preceduti da una valutazione d'impatto sui diritti fondamentali. Non possono essere usati per decisioni di valutazione, sanzione o orientamento, che restano in capo al personale scolastico. I dati non sono conservati oltre il ciclo di studi.
>
> **Art. 5 (Valutazione).** L'INVALSI, con una o più università selezionate con procedura pubblica, effettua una valutazione controfattuale al terzo anno di attuazione. Il rifinanziamento oltre il 2030 è subordinato a un effetto statisticamente significativo sull'abbandono o sulla dispersione implicita.
>
> **Art. 6 (Copertura finanziaria).** 1. Agli oneri, pari a 30 milioni di euro per il 2027, 150 milioni per il 2028 e 250 milioni annui dal 2029, si provvede: a) per 170 milioni annui dal 2029, mediante corrispondente adeguamento della consistenza dell'organico dell'autonomia per i posti comuni al calo della popolazione scolastica, realizzato esclusivamente attraverso il mancato reintegro delle cessazioni dal servizio; b) per la quota restante e fino al 2029, a valere sulle risorse del FSE+ 2021-2027 dei programmi nazionali e regionali, previa riprogrammazione. 2. Il Ministro dell'economia e delle finanze monitora gli oneri ai sensi dell'articolo 17 della legge 31 dicembre 2009, n. 196.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | Norma in legge di bilancio; bozza del DM sull'indice di fragilità; parere del Garante; riprogrammazione FSE+ con la Commissione | MIM, MEF-RGS, Dipartimento coesione, Garante |
| 12 mesi | DM indice adottato; avvio in 150 scuole pilota e nelle scuole già PNRR "divari" (a.s. 2027/28); accordo Stato-Regioni sui percorsi ponte; disegno della valutazione con gruppo di controllo | MIM, USR, Regioni, CPIA, INVALSI |
| Fine legislatura | 1.500 scuole a regime dal 2028/29; valutazione al 3° anno (2030); rifinanziamento condizionato | MIM, INVALSI, università |

**Indicatori**

| KPI | Base | Obiettivo a 3 anni (dato 2029) | Obiettivo a 5 anni (dato 2031) |
|---|---|---|---|
| ELET 18-24 Isole | 13,7% (2025, Eurostat edat_lfse_16) | 11,5% | 9,5% |
| ELET 18-24 maschi | 10,1% (2025, Eurostat edat_lfse_14) | 8,8% | 7,5% |
| Alunni di V primaria almeno al livello base in matematica | 63% (2026, INVALSI) | 66% (divario scuole target/media dimezzato) | 68% |

**Rischi e mitigazione.** *Stigma* delle scuole fragili → indice non pubblico. *Profilazione* degli studenti → allerta solo interna, FRIA, audit annuale, nessuna conservazione dei dati. *Resistenza sindacale all'adeguamento degli organici* → solo turnover, risorse reinvestite nella scuola, priorità ai soprannumerari come tutor. *Turnover degli educatori* → contratti triennali e indennità per le sedi disagiate. *Fine del FSE+ nel 2029* → subentro del FSE+ 2028-34 o aumento della quota demografica (clausola già nella norma).

---

## 05-C2 — Conto personale di competenze (priorità competenze di base e AI)

**Problema in un dato.** Solo il **10,8%** degli adulti 25-64 anni ha fatto formazione nelle ultime 4 settimane nel 2025, contro il 13,7% UE; nelle aree rurali il 9,4% (Eurostat trng_lfse_01 e trng_lfs_14; `05_formazione_adulti_25_64.csv`, `05_formazione_adulti_degurba.csv`). Il 35% degli adulti è al livello 1 o inferiore in literacy (OCSE PIAAC 2023).

**Soluzione.** Un conto individuale portabile su app IO con una dote annua: base, oppure maggiorata per chi non ha il diploma, per i NEET over 25 e per chi lavora in mestieri esposti alla sostituzione da AI. La dote è spendibile solo presso enti accreditati con certificazione delle competenze, e una parte del pagamento è legata al completamento. I CPIA diventano centri serali di literacy, numeracy e uso critico dell'AI.

| Variante | Contenuto | Costo 2027/28/29 → regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | Dote base 300 € + maggiorata 900 €, congedo 40 ore | 0,10 / 0,50 / 0,90 → **1,20** (2030) | 1 | RIALLOCAZIONE 0,50, SPESE_FISCALI 0,40, COESIONE_2127 0,30 |
| ESSENZIALE | Solo dote maggiorata per i gruppi target + CPIA serali | 0,05 / 0,25 / 0,45 → **0,45** (2029) | 0,45 | RIALLOCAZIONE 0,30, COESIONE_2127 0,15 |
| PILOTA | 3 Regioni, adulti senza diploma | 0,02 / 0,05 / 0,05 → 0,05 | 0,05 | COESIONE_2127 0,05 |

*La copertura RIALLOCAZIONE va certificata*: confluenza del Fondo Nuove Competenze e della quota del contributo 0,30% (art. 25 L. 845/1978) non destinata ai fondi interprofessionali. La base è il dato ✅ della verifica, n. 35. Gli importi sono da certificare con INPS e Ministero del Lavoro.

**Articolato normativo essenziale** (disegno di legge delega)

> **Art. 1 (Finalità).** Al fine di garantire a ogni persona adulta il diritto all'apprendimento permanente e di ridurre il divario di competenze di base e digitali, con priorità per chi ha bassi livelli di istruzione, è istituito il Conto personale di competenze.
>
> **Art. 2 (Delega).** Il Governo è delegato ad adottare, entro dodici mesi, uno o più decreti legislativi nel rispetto dei seguenti principi: a) titolarità individuale e portabilità del conto, gestito dall'INPS e accessibile tramite il punto di accesso telematico di cui all'art. 64-bis del d.lgs. 82/2005; b) dote annua base e dote maggiorata almeno tripla per gli adulti privi di diploma, per i giovani NEET oltre i 25 anni e per i lavoratori delle professioni ad alta esposizione alla sostituzione da sistemi di intelligenza artificiale, individuate ogni due anni da INAPP e Banca d'Italia; c) spendibilità esclusiva presso enti accreditati che rilasciano micro-credenziali conformi alla raccomandazione UE 2022 e pubblicano gli esiti occupazionali; d) pagamento dell'ente legato per una quota al completamento e alla certificazione.
>
> **Art. 3 (Competenze di base).** I CPIA organizzano percorsi serali e a distanza di literacy, numeracy e alfabetizzazione critica all'intelligenza artificiale. Ai lavoratori dipendenti privi di diploma spetta un congedo formativo retribuito di 40 ore annue, a carico del Conto.
>
> **Art. 4 (Raccordo).** Le risorse del Fondo Nuove Competenze e la quota del contributo di cui all'art. 25 della legge 845/1978 non destinata ai fondi interprofessionali confluiscono nel Conto. L'accreditamento degli enti è disciplinato d'intesa con le Regioni in Conferenza Stato-Regioni.
>
> **Art. 5 (Valutazione e copertura).** 1. L'INAPP valuta al terzo anno gli esiti occupazionali e salariali a dodici mesi; i corsi con esiti nulli sono esclusi. 2. Agli oneri, nel limite di 100 milioni di euro per il 2027, 500 milioni per il 2028, 900 milioni per il 2029 e 1.200 milioni annui dal 2030, si provvede con le risorse di cui all'art. 4, con quota del FSE+ 2021-2027 fino al 2029 e con le maggiori entrate derivanti dal riordino delle spese fiscali disposto dalla legge di bilancio. La dote è riconosciuta nel limite delle risorse; un meccanismo di monitoraggio adegua l'importo della dote base.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | DDL delega in Consiglio dei ministri; tavolo con le parti sociali sui fondi interprofessionali; avvio dei piloti FSE+ in 3 Regioni | MIM, Ministero del Lavoro, INPS, Regioni |
| 12 mesi | Legge delega approvata; piattaforma su app IO; standard di accreditamento e micro-credenziali; CPIA serali avviati | Lavoro, MIM, INPS, PagoPA, INAPP |
| Fine legislatura | Conto a regime (2030); valutazione INAPP (2030); PIAAC ciclo 3 come verifica | INAPP, Regioni |

**Indicatori**

| KPI | Base | 3 anni (2029) | 5 anni (2031) |
|---|---|---|---|
| Adulti 25-64 in formazione (4 settimane) | 10,8% (2025, Eurostat trng_lfse_01) | 13,7% (media UE 2025) | 16% (verso il 18% nel 2032) |
| Idem, aree rurali | 9,4% (2025, Eurostat trng_lfs_14) | 12% | 14% |
| Quota di titolari della dote maggiorata tra gli utilizzatori | n.d. (rilevata dal primo anno) | ≥40% | ≥45% |

**Rischi e mitigazione.** *Frodi e corsi inutili*, come per il CPF francese → accreditamento stretto, pagamento legato agli esiti, controlli a campione. *Effetto San Matteo* → la dote maggiorata e l'orientamento attivo via CPI, sindacati e terzo settore. *Opposizione delle parti sociali sui fondi interprofessionali* → gestione cogestita e confluenza solo della quota non optata. *Copertura FSE+ in scadenza nel 2029* → dote base indicizzata alle risorse disponibili.

---

## 05-C3 — Carriere della ricerca: legge di programmazione decennale

**Problema in un dato.** La R&S finanziata dalla PA vale lo **0,54% del PIL** nel 2024, contro lo 0,68% UE (2023). La spesa totale in R&S è all'1,41% (UE 2,26%) e scende all'1,37% nel 2025, dato preliminare (Eurostat rd_e_gerdfund e rd_e_gerdtot; `05_rs_gerd_finanziata_pa.csv`). Gli stanziamenti di bilancio (GBARD) calano dallo 0,61% (2024) allo 0,58% (2025, provvisorio) (`05_rs_gbard.csv`).

**Soluzione.** Una legge di programmazione blinda un sentiero di +0,3 mld l'anno fino a +3,2 mld nel 2035 (0,68% del PIL). Un'Agenzia nazionale della ricerca indipendente gestisce i bandi con peer review internazionale e calendario fisso. Un tenure track unico prevede un ponte selettivo per i ricercatori PNRR. Il pacchetto rientri è legato alla permanenza. Il sentiero prosegue solo se migliorano almeno 2 indicatori su 4.

| Variante | Contenuto | Costo 2027/28/29 → regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | Sentiero allo 0,68% PIL nel 2035 | 0,30 / 0,60 / 0,90 → **3,20** (2035) | 1 | SPESE_FISCALI 2,20, SAD 1,00 (ricerca su clima ed energia) |
| ESSENZIALE | Riforme + ponte per ~2.000 ricercatori PNRR + sentiero dimezzato | 0,20 / 0,40 / 0,60 → **1,50** (2032) | 0,5 | SPESE_FISCALI 1,00, SAD 0,50 |
| ZERO | Solo Agenzia, tenure track e calendario, con fondi PRIN/FIS esistenti | 0 → 0 | 0,15 | — |

*Ritmo delle coperture nella PIENA*: SPESE_FISCALI 0,2 / 0,4 / 0,6 e SAD 0,1 / 0,2 / 0,3 nel 2027-29. Il prelievo cresce con il sentiero, quindi nel triennio la pressione sui fondi resta sotto 1 mld.

**Articolato normativo essenziale** (legge di programmazione)

> **Art. 1 (Finalità e sentiero).** 1. In attuazione dell'art. 9 e dell'art. 33 della Costituzione, la presente legge programma per il periodo 2027-2035 le risorse pubbliche per la ricerca. L'obiettivo è portare la spesa in ricerca e sviluppo finanziata dalle amministrazioni pubbliche dallo 0,54 per cento del PIL del 2024 allo 0,68 per cento nel 2035. 2. Gli stanziamenti aggiuntivi sono fissati nella tabella A, con un incremento annuo non inferiore a 300 milioni di euro a prezzi 2024.
>
> **Art. 2 (Agenzia nazionale della ricerca).** È istituita l'Agenzia nazionale della ricerca, dotata di autonomia scientifica, organizzativa e contabile. È governata da un consiglio scientifico in maggioranza composto da studiosi in servizio all'estero, a rotazione. L'Agenzia gestisce i programmi PRIN e FIS e i bandi sulle priorità strategiche con peer review internazionale e calendario annuale fisso. Almeno un terzo delle risorse aggiuntive è destinato a ricerca su clima, energia e adattamento.
>
> **Art. 3 (Tenure track unico).** 1. Il reclutamento universitario e degli enti di ricerca avviene mediante un contratto di ricercatore in tenure track di durata massima di sei anni, con valutazione per il passaggio a professore associato o primo ricercatore. 2. Per il biennio 2027-2028 è riservata una quota dei posti ai titolari di contratti finanziati dal PNRR che hanno avuto una valutazione positiva.
>
> **Art. 4 (Rientri).** Il regime fiscale agevolato per ricercatori e docenti che rientrano in Italia è subordinato alla permanenza per almeno sei anni. Ai vincitori di grant ERC e MSCA che scelgono un ente italiano è riconosciuto un contributo di avvio laboratorio.
>
> **Art. 5 (Clausola di revisione).** Ogni tre anni l'ANVUR e l'Agenzia trasmettono alle Camere un rapporto sugli indicatori di cui all'allegato B. L'incremento previsto dalla tabella A per il triennio successivo si applica solo se almeno due indicatori su quattro sono migliorati.
>
> **Art. 6 (Copertura finanziaria).** Agli oneri, pari a 300 milioni di euro per il 2027, 600 milioni per il 2028, 900 milioni per il 2029 e crescenti fino a 3.200 milioni annui dal 2035, si provvede: a) per due terzi, mediante le maggiori entrate derivanti dal riordino delle spese fiscali disposto annualmente con la legge di bilancio, ai sensi dell'art. 21, comma 11-bis, della legge 196/2009; b) per un terzo, mediante quota delle maggiori entrate derivanti dalla rimodulazione dei sussidi ambientalmente dannosi, vincolata alle finalità di cui all'art. 2, ultimo periodo.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | Ponte per i ricercatori PNRR in legge di bilancio; DDL di programmazione in CdM; censimento dei contratti PNRR in scadenza (oggi nessun dato ufficiale) | MUR, MEF, CRUI, EPR |
| 12 mesi | Legge approvata; statuto e consiglio dell'Agenzia; primo bando con calendario fisso; decreto sul tenure track | MUR, Agenzia, ANVUR |
| Fine legislatura | Sentiero a +1,5 mld (2032); primo rapporto triennale (2030) e decisione sul triennio successivo | Agenzia, ANVUR, Parlamento |

**Indicatori**

| KPI | Base | 3 anni (2029) | 5 anni (2031) |
|---|---|---|---|
| R&S finanziata dalla PA, % PIL | 0,54% (2024, Eurostat rd_e_gerdfund) | 0,58% | 0,61% |
| Spesa totale in R&S, % PIL | 1,41% (2024; 1,37% nel 2025, preliminare; Eurostat rd_e_gerdtot) | 1,50% | 1,60% |
| Saldo migratorio dei laureati italiani 25-34 | -78.000 nel 2019-2024, cioè -13.000/anno (ISTAT, ago. 2026) | -9.000/anno | -6.000/anno |

**Rischi e mitigazione.** *Spesa che non diventa ricerca* → quota minima per progetti e infrastrutture. *Cattura accademica dell'Agenzia* → consiglio internazionale a rotazione. *Divario Nord-Sud* → bandi di capacità per gli atenei del Mezzogiorno, con valutazione separata. *Taglio nelle leggi di bilancio future* (breve negativo, ⚠️) → legge pluriennale con tabella vincolante. *Coperture incerte* (spese fiscali e SAD sono misure del menu) → clausola di revisione triennale e variante ESSENZIALE già pronta come ripiego.

---

## 05-C4 — Più laureati e diplomati terziari: borse, ITS Academy, residenze

**Problema in un dato.** I laureati tra 25 e 34 anni sono il **31,1%** nel 2025, contro il 44,8% UE e il target UE del 45% al 2030 (Eurostat edat_lfse_03; `05_laureati_25_34.csv`).

**Soluzione.** Una borsa di studio garantita a tutti gli idonei con un LEP nazionale, perché alla fine del PNRR (150 mln sui 708 mln delle borse 2025/26, fonte stampa, da verificare) gli idonei non beneficiari tornerebbero. Gli iscritti agli ITS Academy si triplicano, con passerelle verso la laurea. Le residenze pubbliche a canone legato all'ISEE nascono su immobili pubblici dismessi, con una quota riservata al Mezzogiorno.

| Variante | Contenuto | Costo 2027/28/29 → regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | Borse + ITS ×3 (~100.000 iscritti) + residenze per 2,4 mld in 8 anni | 0,45 / 0,60 / 0,75 → **0,85** (2030) | 1 | SPESE_FISCALI 0,42, COESIONE_2127 0,30 (residenze), RIALLOCAZIONE 0,13 (dividendo demografico) |
| ESSENZIALE | Borse + ITS ×2 + residenze per 1 mld in 10 anni | 0,30 / 0,40 / 0,45 → **0,45** (2029) | 0,55 | SPESE_FISCALI 0,22, RIALLOCAZIONE 0,13, COESIONE_2127 0,10 |
| PILOTA | Solo tenuta delle borse + residenze pilota in 3 città del Sud | 0,20 → **0,20** | 0,25 | RIALLOCAZIONE 0,10, SPESE_FISCALI 0,05, COESIONE_2127 0,05 |

**Articolato normativo essenziale**

> **Art. 1 (Finalità).** Al fine di elevare la quota di giovani con titolo terziario e di rimuovere gli ostacoli economici al diritto allo studio, ai sensi dell'art. 34, terzo comma, della Costituzione, la presente legge garantisce la borsa di studio a tutti gli studenti idonei e potenzia l'istruzione terziaria professionalizzante.
>
> **Art. 2 (LEP del diritto allo studio).** 1. La borsa di studio a tutti gli studenti in possesso dei requisiti costituisce livello essenziale delle prestazioni ai sensi dell'art. 117, secondo comma, lettera m), della Costituzione. 2. Il Fondo integrativo statale per la concessione delle borse di studio è incrementato in misura tale da assicurare la copertura integrale degli idonei. Il riparto premia le Regioni che cofinanziano oltre il minimo.
>
> **Art. 3 (ITS Academy).** 1. Il Fondo per l'istruzione tecnologica superiore è incrementato con l'obiettivo di triplicare gli iscritti entro il 2032. Una quota del 30% è ripartita in base agli esiti occupazionali a un anno rilevati dal monitoraggio INDIRE. 2. Sono garantite passerelle verso le lauree professionalizzanti, con riconoscimento dei crediti. 3. L'orientamento agli ITS è obbligatorio negli ultimi due anni della scuola secondaria di secondo grado.
>
> **Art. 4 (Residenze pubbliche).** L'Agenzia del demanio, d'intesa con il MUR e con gli enti regionali per il diritto allo studio, individua entro sei mesi immobili pubblici dismessi da destinare a residenze universitarie a canone commisurato all'ISEE, ristrutturate secondo standard di alta efficienza energetica. Almeno il 40% dei posti è riservato agli atenei del Mezzogiorno.
>
> **Art. 5 (Copertura finanziaria).** Agli oneri, pari a 450 milioni di euro per il 2027, 600 milioni per il 2028, 750 milioni per il 2029 e 850 milioni annui dal 2030, si provvede: a) per 300 milioni annui, relativi agli investimenti per le residenze, a valere sulle risorse della politica di coesione 2021-2027 e, dal 2030, del ciclo 2028-2034; b) per 130 milioni annui, mediante adeguamento dell'organico dei posti comuni al calo della popolazione scolastica, attraverso il mancato reintegro delle cessazioni; c) per la quota restante, mediante le maggiori entrate derivanti dal riordino delle spese fiscali.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | Copertura delle borse 2027/28 al posto del PNRR (evita il ritorno degli idonei non beneficiari); mappatura degli immobili del Demanio | MUR, MEF, Agenzia del demanio, Regioni |
| 12 mesi | Decreto LEP DSU; riparto premiale del fondo ITS; primi 3 cantieri di residenze; campagna di orientamento ITS nelle superiori | MUR, MIM, Regioni, enti DSU, ITS Academy |
| Fine legislatura | Zero idonei non beneficiari ogni anno; ITS a ~66-100 mila iscritti; 8-10 mila nuovi posti letto pubblici (stima GovernAI) | MUR, MIM, Regioni |

**Indicatori**

| KPI | Base | 3 anni (2029) | 5 anni (2031) |
|---|---|---|---|
| Laureati e diplomati terziari 25-34 | 31,1% (2025, Eurostat edat_lfse_03) | 33% | 35% (verso il 40% nel 2035) |
| Iscritti ITS Academy | ~33.400 (1/2/2026, stampa, da confermare con MIM/INDIRE) | 55.000 | 85.000 |
| Idonei non beneficiari | copertura 99,8% nel 2024/25, con fondi PNRR (Avvenire, da verificare) | 0 | 0 |

**Rischi e mitigazione.** *ITS di qualità disomogenea* → riparto premiale sugli esiti. *Più laureati che poi emigrano* → combinare con 05-C3 e con le politiche salariali (area 02). *Ritardi edilizi* → procedure standard e commissario unico. *Fondi di coesione dopo il 2029* → BEI come ripiego, sapendo che i prestiti sono debito. *Conflitto con le dismissioni del Demanio a fini di riduzione del debito* → priorità agli immobili con valore di mercato basso.

---

## 05-C5 — Scuole aperte come presidi di comunità

**Problema in un dato.** Il **30,8%** della popolazione da 3 anni in su non pratica né sport né attività fisica (ISTAT, *Fattori di rischio per la salute*, 2025). I NEET 15-29 sono il 13,3% nel 2025, quartultimo valore UE (Eurostat edat_lfse_20; `05_neet_15_29.csv`).

**Soluzione.** Una norma quadro rende standard l'apertura extra-orario delle scuole con patti di comunità tra dirigente, Comune e ASD o associazioni, e risolve il nodo dell'assicurazione e della responsabilità a livello nazionale. Le attività sono gratuite per gli under 18 a basso ISEE. I giovani NEET del Servizio civile fanno da animatori. Le risorse si spostano dai voucher individuali all'offerta di prossimità.

| Variante | Contenuto | Costo 2027/28/29 → regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | ~3.000 plessi | 0,15 / 0,30 / 0,40 → **0,40** (2029) | 1 | ACCISE_SALUTE 0,15, SPESE_FISCALI 0,10 (detrazione sport ragazzi), RIORDINO_BONUS 0,09 (Carta Valore con ISEE), RIALLOCAZIONE 0,06 (Fondo sport e periferie) |
| ESSENZIALE | ~1.500 scuole fragili (le stesse di 05-C1) | 0,10 / 0,20 / 0,20 → **0,20** (2028) | 0,5 | RIORDINO_BONUS 0,09, ACCISE_SALUTE 0,08, RIALLOCAZIONE 0,03 |
| PILOTA | 300 scuole in 10 città e aree interne | 0,02 / 0,04 / 0,04 → 0,04 | 0,1 | COESIONE_2127 0,04 |

**Articolato normativo essenziale**

> **Art. 1 (Finalità).** Al fine di promuovere l'attività fisica, la partecipazione culturale e la coesione sociale dei minori e dei giovani, gli edifici scolastici statali sono aperti oltre l'orario delle lezioni come presidi di comunità.
>
> **Art. 2 (Patti di comunità).** Il dirigente scolastico, il Comune e gli enti del Terzo settore e le associazioni sportive dilettantistiche iscritte ai rispettivi registri stipulano patti di comunità secondo lo schema tipo adottato con decreto del Ministro dell'istruzione e del merito, di concerto con il Ministro per lo sport e i giovani e con il Ministro della cultura, sentita l'ANCI. Gli enti sono selezionati con avviso pubblico.
>
> **Art. 3 (Responsabilità e assicurazione).** Durante le attività svolte in base ai patti, la custodia e la responsabilità per i danni sono in capo all'ente gestore. La copertura assicurativa è garantita da una polizza nazionale stipulata da Sport e Salute S.p.A. Il personale ATA impiegato oltre l'orario è retribuito a carico del fondo di cui all'art. 4.
>
> **Art. 4 (Fondo "Scuole aperte").** È istituito presso Sport e Salute S.p.A. il Fondo "Scuole aperte", ripartito con priorità secondo l'indice di fragilità di cui alla legge istitutiva del programma "Nessuno escluso". Le attività sono gratuite per i minori appartenenti a nuclei con ISEE fino a 25.000 euro. Gli operatori volontari del Servizio civile universale possono essere impiegati come animatori, con attestazione delle competenze.
>
> **Art. 5 (Copertura finanziaria).** Agli oneri, pari a 150 milioni di euro per il 2027, 300 milioni per il 2028 e 400 milioni annui dal 2029, si provvede: a) per 90 milioni, mediante riduzione dell'autorizzazione di spesa della Carta Valore di cui alla legge 199/2025, la cui erogazione è subordinata a un ISEE non superiore a 35.000 euro; b) per 100 milioni, mediante soppressione della detrazione per le spese di attività sportive dei ragazzi; c) per 150 milioni, mediante quota delle maggiori entrate da accisa sui tabacchi lavorati; d) per 60 milioni, mediante corrispondente riduzione del Fondo sport e periferie.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | Norma quadro (responsabilità e assicurazione) nel primo veicolo utile; schema tipo dei patti con ANCI | MIM, Ministro Sport e Giovani, MiC, ANCI |
| 12 mesi | Fondo operativo; 1.500 scuole fragili aperte per l'estate e per l'a.s. 2028/29; Servizio civile con progetti dedicati | Sport e Salute, USR, Comuni, Dipartimento politiche giovanili |
| Fine legislatura | 3.000 plessi; valutazione partecipata dopo 2 anni; risorse spostate dove gli spazi restano vuoti | Sport e Salute, Comuni, ISTAT |

**Indicatori**

| KPI | Base | 3 anni (2029) | 5 anni (2031) |
|---|---|---|---|
| Sedentarietà (3 anni e più) | 30,8% (2025, ISTAT) | 29% | 27,5% (con obiettivo specifico per 6-17 anni da fissare sulla rilevazione ISTAT per età) |
| NEET 15-29 | 13,3% (2025, Eurostat edat_lfse_20) | 12,0% (insieme a 05-C1, C2 e C4) | 11,0% (media UE 2025) |
| Ore di apertura extra-curricolare per plesso e partecipanti under 18 con ISEE basso | n.d. (rilevazione dal primo anno) | ≥300 ore/anno nei plessi aderenti | ≥400 ore/anno |

**Rischi e mitigazione.** *Carico sulle scuole* → la gestione spetta all'ente terzo e l'ATA è pagato a parte. *Edifici inadeguati* → priorità a quelli già messi a norma con il PNRR. *Clientelismo* → avvisi pubblici e valutazione partecipata. *Impopolarità del taglio della Carta Valore e della detrazione* → gradualità e prova di efficacia; la Carta resta per l'ISEE medio-basso. *Consumi energetici* → aperture concentrate negli edifici efficienti.

---

## 05-C6 — AI a scuola: alfabetizzazione critica, strumenti per i docenti, regole chiare

**Problema in un dato.** Usa l'AI il **16,4%** delle imprese italiane con almeno 10 addetti nel 2025, il doppio del 2024 (UE 20,0%) (Eurostat isoc_eb_ai; `05_imprese_ai.csv`): lavoro e scuola cambiano in fretta. Intanto alla primaria cala la matematica: il 63% degli alunni di V raggiunge il livello base nel 2026, contro il 66% del 2025 (INVALSI 2026). Il rischio è che una delega non guidata all'AI peggiori gli apprendimenti di base (Bastani et al., 2024).

**Soluzione.** L'alfabetizzazione critica all'AI entra nel curricolo di educazione civica e tecnologia dalla secondaria di primo grado. La formazione docenti diventa obbligatoria: 20 ore per triennio, pagate con una quota vincolata della Carta del docente. Gli strumenti pubblici sono conformi all'AI Act e al GDPR. Regola di base: l'AI non decide voti, ammissioni, orientamento o sanzioni; le prove si riformano con più scritto in classe e più orali.

| Variante | Contenuto | Costo 2027/28/29 → regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | Curricolo + formazione + piattaforma pubblica + referenti | 0,08 / 0,18 / 0,22 → **0,22** (2029) | 1 | RIORDINO_BONUS 0,12 (Carta del docente), RIALLOCAZIONE 0,05, COESIONE_2127 0,05 (piattaforma) |
| ESSENZIALE | Curricolo + formazione + regole, strumenti tramite accordi quadro Consip | 0,04 / 0,08 / 0,08 → **0,08** (2028) | 0,45 | RIORDINO_BONUS 0,08 |
| ZERO | Solo regole e curricolo | 0 → 0 | 0,2 | — |

**Articolato normativo essenziale**

> **Art. 1 (Finalità).** Al fine di sviluppare negli studenti una comprensione critica dei sistemi di intelligenza artificiale e di garantirne un uso conforme al regolamento (UE) 2024/1689 e al regolamento (UE) 2016/679, la presente legge disciplina l'insegnamento e l'uso dell'intelligenza artificiale nelle istituzioni scolastiche.
>
> **Art. 2 (Curricolo).** Con decreto del Ministro dell'istruzione e del merito, le linee guida per l'insegnamento dell'educazione civica e della tecnologia sono integrate, dalla scuola secondaria di primo grado, con competenze su funzionamento, limiti, verifica delle fonti, bias e tutela dei dati nei sistemi di intelligenza artificiale, in coerenza con il quadro europeo DigComp.
>
> **Art. 3 (Garanzia della decisione umana).** Nessuna decisione relativa a valutazione, ammissione, orientamento o provvedimenti disciplinari può essere adottata da un sistema di intelligenza artificiale. Questi sistemi possono solo fornire suggerimenti, e il docente ne documenta l'uso e la decisione. Nella scuola primaria l'uso degli strumenti generativi da parte degli alunni è escluso, salvo attività guidate.
>
> **Art. 4 (Formazione e strumenti).** 1. La formazione dei docenti in servizio sull'intelligenza artificiale è obbligatoria, per almeno 20 ore nel triennio. Una quota della Carta elettronica del docente, fissata con decreto, è vincolata a questa formazione. 2. Il Ministero rende disponibili strumenti selezionati con procedure che richiedono conformità al regolamento (UE) 2024/1689, trattamento dei dati nell'Unione e divieto di usare i dati degli studenti per l'addestramento commerciale.
>
> **Art. 5 (Valutazione e copertura).** 1. L'INVALSI valuta al secondo anno gli effetti sugli apprendimenti di base con un disegno controllato; gli strumenti che hanno effetti negativi sono sospesi. 2. Agli oneri, pari a 80 milioni di euro per il 2027, 180 milioni per il 2028 e 220 milioni annui dal 2029, si provvede: per 120 milioni mediante vincolo di destinazione di quota della Carta elettronica del docente; per 50 milioni mediante riorientamento delle risorse per la formazione in servizio; per 50 milioni, fino al 2029, a valere sulla programmazione FESR 2021-2027.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | DM sulla garanzia della decisione umana (variante ZERO subito operativa); linee guida del curricolo in consultazione | MIM, Garante, autorità nazionali AI (AgID/ACN) |
| 12 mesi | Curricolo in vigore dall'a.s. 2028/29; formazione avviata; gara per gli strumenti conformi all'AI Act | MIM, INDIRE, Consip |
| Fine legislatura | 100% dei docenti formati; valutazione INVALSI al 2° anno; PISA 2029 come verifica | INVALSI, INDIRE |

**Indicatori**

| KPI | Base | 3 anni (2029) | 5 anni (2031) |
|---|---|---|---|
| Docenti con formazione AI certificata | n.d. (2026; rilevazione INDIRE dal primo anno) | 60% | 100% |
| PISA matematica | 468 (2025, OCSE, da ricontrollare sulla nota OCSE) | non inferiore a 468 (PISA 2029) | ≥ media OCSE |
| Alunni di V primaria almeno al livello base in matematica (vincolo di "non danno") | 63% (2026, INVALSI) | ≥66% | ≥68% |

**Rischi e mitigazione.** *Calo delle competenze di base per delega all'AI* → niente strumenti generativi alla primaria e prove senza AI. *Lock-in tecnologico* → standard aperti e più fornitori. *Privacy* → valutazione d'impatto e Garante. *Resistenza dei docenti al vincolo sulla Carta* → la quota resta nella disponibilità del docente, solo vincolata a un fine. *Timori delle famiglie* → trasparenza e opt-out per gli strumenti non essenziali.

---

## Riepilogo dell'area

| Proposta | PIENA (regime) | ESSENZIALE | PILOTA/ZERO |
|---|---|---|---|
| 05-C1 Nessuno escluso | 0,25 | 0,13 (int. 0,6) | 0,03 (0,1) |
| 05-C2 Conto competenze | 1,20 | 0,45 (0,45) | 0,05 (0,05) |
| 05-C3 Carriere della ricerca | 3,20 al 2035 (0,9 nel 2029) | 1,50 al 2032 (0,5) | ZERO 0 (0,15) |
| 05-C4 Terziario | 0,85 | 0,45 (0,55) | 0,20 (0,25) |
| 05-C5 Scuole aperte | 0,40 | 0,20 (0,5) | 0,04 (0,1) |
| 05-C6 AI a scuola | 0,22 | 0,08 (0,45) | ZERO 0 (0,2) |
| **Totale** | **6,12** | **2,81** | 0,32 |

Prelievo a regime per fondo nella combinazione tutta PIENA: SPESE_FISCALI 3,12; SAD 1,00; RIALLOCAZIONE 0,91; COESIONE_2127 0,73; RIORDINO_BONUS 0,21; ACCISE_SALUTE 0,15. Nessun prelievo da DEFICIT, RISPARMI_ATTESI, IVA_EVASIONE, ETS o ALTRO.

**Segnalazioni al coordinatore e all'agente coperture.**
1. Misure nuove da inserire nel menu: adeguamento dell'organico al calo demografico via turnover (RIALLOCAZIONE, 0,30); Carta Valore con ISEE (RIORDINO_BONUS, 0,09); quota vincolata della Carta del docente (RIORDINO_BONUS, 0,08-0,12); detrazione per lo sport dei ragazzi (SPESE_FISCALI, 0,10, da verificare); Fondo Nuove Competenze e quota 0,30% non optata (RIALLOCAZIONE, 0,3-0,5, da certificare).
2. SPESE_FISCALI è il fondo più usato per via di 05-C3. Senza misure del menu che lo alimentino, la scelta ragionevole per 05-C3 è la ESSENZIALE o una PIENA che nel triennio 2027-29 pesa solo 0,9.
3. COESIONE_2127 copre solo avvio e investimenti fino al 2029, mai personale stabile. Dal 2030 le note indicano chi subentra.
