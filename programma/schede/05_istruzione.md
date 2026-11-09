# Schede pronte — Area 05: Istruzione, Università e Ricerca, Cultura, Sport e Giovani

*Agente ministeriale GovernAI, 7 novembre 2026. Fonti: dossier `ministeri/05_istruzione_ricerca_cultura.md`, verifica `dati/verifiche/05_istruzione.md`, serie `dati/serie/05_*.csv` e `02_demografia_nati_decessi_pop.csv`. Varianti e coperture: `programma/varianti/05_istruzione.csv`. Importi in mld €/anno, salvo diversa indicazione. "Stima GovernAI" = stima propria da verificare.*

## Premessa: il dividendo demografico, unica risorsa interna dell'area

- **Dato**: i nati in Italia passano da **485.780 (2015) a 355.435 (2025)**, -26,8% (Eurostat/ISTAT, `02_demografia_nati_decessi_pop.csv`). Chi entra in prima primaria dal 2031 è una coorte con circa 130 mila bambine e bambini in meno rispetto a quella entrata nel 2021.
- **Cosa è già speso**: la L. 207/2024 (c. 828) ha già tagliato 5.660 posti comuni dall'a.s. 2025/26, e la nota MIM 10164/2026 toglie altri 1.407 posti di potenziamento nel 2026/27 (fonti di stampa specializzata). Questi risparmi sono **già nei tendenziali**: non li usiamo come copertura.
- **Cosa usiamo**: una **misura di copertura nuova (RIALLOCAZIONE)**, cioè un ulteriore adeguamento dei posti comuni al calo della popolazione scolastica, **solo tramite turnover** (nessun licenziamento), per circa 6.700 posti a regime × 45 mila € = **0,30 mld/anno**. Il ricavato viene reinvestito per intero nella scuola: 0,17 in 05-C1 (squadre anti-dispersione) e 0,13 in 05-C4 (ITS). L'adeguamento è una quota piccola del calo atteso della popolazione scolastica. La RGS deve certificare che conta solo la parte non già scontata nei tendenziali.
- **Altre coperture nuove proposte al menu**: Carta Valore resa selettiva con ISEE (RIORDINO_BONUS, 0,09); una quota della Carta del docente vincolata alla formazione su AI (RIORDINO_BONUS, 0,08-0,12); la trasformazione della detrazione per le spese sportive di ragazze e ragazzi (SPESE_FISCALI, 0,10, da verificare); la confluenza del Fondo Nuove Competenze e della quota 0,30% non optata nel Conto competenze (RIALLOCAZIONE, 0,3-0,5, da certificare).

---

## 05-C1 — "Nessuna esclusione": squadre di prossimità contro la dispersione

**Problema in un dato.** L'abbandono precoce (ELET 18-24) è all'8,2% in Italia, ma al **13,7% nelle Isole** e al **10,1% tra i maschi** nel 2025 (Eurostat edat_lfse_16 ed edat_lfse_14; `05_elet_18_24_nuts1.csv`, `05_elet_18_24_sesso.csv`). Arriva al 44,1% tra le persone straniere arrivate in Italia a 16-24 anni (ISTAT 2026).

**Soluzione.** Un indice di fragilità di istituto individua le scuole a più alto rischio. In ciascuna lavora una squadra stabile: docente tutor (dal personale liberato dal dividendo demografico), personale educativo e mediazione culturale in rete. Si aggiungono il tutoraggio intensivo di matematica alla primaria, un percorso ponte con i CPIA per chi è arrivato da poco in Italia tra i 16 e i 24 anni e un sistema di allerta precoce che segnala ma non decide. Una valutazione controfattuale al terzo anno condiziona il rifinanziamento.

| Variante | Contenuto | Costo 2027/28/29 → regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | ~1.500 scuole (quintile più fragile) | 0,03 / 0,15 / 0,25 → **0,25** (2029) | 1 | RIALLOCAZIONE 0,17 (dividendo demografico), COESIONE_2127 0,08 (FSE+) |
| ESSENZIALE | ~750 scuole (decile più fragile) | 0,02 / 0,08 / 0,13 → **0,13** | 0,6 | RIALLOCAZIONE 0,10, COESIONE_2127 0,03 |
| PILOTA | 150 scuole randomizzate in 3 Regioni | 0,01 / 0,03 / 0,03 → 0,03 | 0,1 | COESIONE_2127 0,03 |

*Costo ricalibrato, come chiesto dalla verifica (0,2-0,3)*: personale educativo 0,06; mediazione 0,02; ponte CPIA 0,03; allerta e valutazione 0,01; esoneri per la funzione di tutor e tutoraggio di matematica 0,13 (stima GovernAI).

**Articolato normativo essenziale** (da inserire nella legge di bilancio, capo "Istruzione")

> **Art. 1 (Finalità).** Al fine di ridurre l'abbandono scolastico precoce e la dispersione implicita nei contesti a più alta concentrazione di svantaggio, in attuazione degli articoli 3 e 34 della Costituzione, è istituito il programma nazionale "Nessuna esclusione".
>
> **Art. 2 (Indice di fragilità).** 1. Con decreto del Ministro dell'istruzione e del merito, sentito l'INVALSI e acquisito il parere del Garante per la protezione dei dati personali, da adottare entro novanta giorni dall'entrata in vigore della presente legge, è definito l'indice di fragilità delle istituzioni scolastiche, basato almeno sull'indice ESCS medio, sulla quota di alunne e alunni con background migratorio di recente arrivo e sui tassi di ripetenza e abbandono. 2. L'indice è usato esclusivamente per la ripartizione delle risorse e non è pubblicato in forma nominativa.
>
> **Art. 3 (Squadre di prossimità).** 1. Alle istituzioni scolastiche del quintile più fragile è assegnata una squadra composta da personale docente con funzione di tutor ed esonero parziale, da personale educativo professionale e da una quota di mediazione linguistico-culturale organizzata in rete. 2. Il personale docente con funzione di tutor è individuato prioritariamente tra il personale docente in esubero o in soprannumero per effetto della riduzione della popolazione scolastica. 3. Le squadre attuano interventi di tutoraggio intensivo in matematica nella scuola primaria.
>
> **Art. 4 (Percorsi ponte e allerta precoce).** 1. Con accordo in Conferenza Stato-Regioni sono istituiti percorsi ponte biennali tra CPIA e istruzione e formazione professionale per le persone di 16-24 anni di recente arrivo. 2. I sistemi di segnalazione precoce del rischio di abbandono sono conformi al regolamento (UE) 2024/1689. Sono preceduti da una valutazione d'impatto sui diritti fondamentali. Non possono essere usati per decisioni di valutazione, sanzione o orientamento, che restano in capo al personale scolastico. I dati non sono conservati oltre il ciclo di studi.
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

**Rischi e mitigazione.** *Stigma* delle scuole fragili → indice non pubblico. *Profilazione* di studentesse e studenti → allerta solo interna, FRIA, audit annuale, nessuna conservazione dei dati. *Resistenza sindacale all'adeguamento degli organici* → solo turnover, risorse reinvestite nella scuola, priorità al personale in soprannumero come tutor. *Turnover del personale educativo* → contratti triennali e indennità per le sedi disagiate. *Fine del FSE+ nel 2029* → subentro del FSE+ 2028-34 o aumento della quota demografica (clausola già nella norma).

---

## 05-C2 — Conto personale di competenze (priorità competenze di base e AI)

**Problema in un dato.** Solo il **10,8%** delle persone adulte di 25-64 anni ha fatto formazione nelle ultime 4 settimane nel 2025, contro il 13,7% UE; nelle aree rurali il 9,4% (Eurostat trng_lfse_01 e trng_lfs_14; `05_formazione_adulti_25_64.csv`, `05_formazione_adulti_degurba.csv`). Il 35% delle persone adulte è al livello 1 o inferiore in literacy (OCSE PIAAC 2023).

**Soluzione.** Un conto individuale portabile su app IO con una dote annua: base, oppure maggiorata per chi non ha il diploma, per chi è NEET oltre i 25 anni e per chi lavora in mestieri esposti alla sostituzione da AI. La dote è spendibile solo presso enti accreditati con certificazione delle competenze, e una parte del pagamento è legata al completamento. I CPIA diventano centri serali di literacy, numeracy e uso critico dell'AI.

| Variante | Contenuto | Costo 2027/28/29 → regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | Dote base 300 € + maggiorata 900 €, congedo 40 ore | 0,10 / 0,50 / 0,90 → **1,20** (2030) | 1 | RIALLOCAZIONE 0,50, SPESE_FISCALI 0,40, COESIONE_2127 0,30 |
| ESSENZIALE | Solo dote maggiorata per i gruppi target + CPIA serali | 0,05 / 0,25 / 0,45 → **0,45** (2029) | 0,45 | RIALLOCAZIONE 0,30, COESIONE_2127 0,15 |
| PILOTA | 3 Regioni, persone adulte senza diploma | 0,02 / 0,05 / 0,05 → 0,05 | 0,05 | COESIONE_2127 0,05 |

*La copertura RIALLOCAZIONE va certificata*: confluenza del Fondo Nuove Competenze e della quota del contributo 0,30% (art. 25 L. 845/1978) non destinata ai fondi interprofessionali. La base è il dato ✅ della verifica, n. 35. Gli importi sono da certificare con INPS e Ministero del Lavoro.

**Articolato normativo essenziale** (disegno di legge delega)

> **Art. 1 (Finalità).** Al fine di garantire a ogni persona adulta il diritto all'apprendimento permanente e di ridurre il divario di competenze di base e digitali, con priorità per chi ha bassi livelli di istruzione, è istituito il Conto personale di competenze.
>
> **Art. 2 (Delega).** Il Governo è delegato ad adottare, entro dodici mesi, uno o più decreti legislativi nel rispetto dei seguenti principi: a) titolarità individuale e portabilità del conto, gestito dall'INPS e accessibile tramite il punto di accesso telematico di cui all'art. 64-bis del d.lgs. 82/2005; b) dote annua base e dote maggiorata almeno tripla per le persone adulte prive di diploma, per le persone NEET oltre i 25 anni e per chi lavora nelle professioni ad alta esposizione alla sostituzione da sistemi di intelligenza artificiale, individuate ogni due anni da INAPP e Banca d'Italia; c) spendibilità esclusiva presso enti accreditati che rilasciano micro-credenziali conformi alla raccomandazione UE 2022 e pubblicano gli esiti occupazionali; d) pagamento dell'ente legato per una quota al completamento e alla certificazione.
>
> **Art. 3 (Competenze di base).** I CPIA organizzano percorsi serali e a distanza di literacy, numeracy e alfabetizzazione critica all'intelligenza artificiale. Al personale dipendente privo di diploma spetta un congedo formativo retribuito di 40 ore annue, a carico del Conto.
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
| Quota di titolari della dote maggiorata tra le persone che usano il conto | n.d. (rilevata dal primo anno) | ≥40% | ≥45% |

**Rischi e mitigazione.** *Frodi e corsi inutili*, come per il CPF francese → accreditamento stretto, pagamento legato agli esiti, controlli a campione. *Effetto San Matteo* → la dote maggiorata e l'orientamento attivo via CPI, sindacati e terzo settore. *Opposizione delle parti sociali sui fondi interprofessionali* → gestione cogestita e confluenza solo della quota non optata. *Copertura FSE+ in scadenza nel 2029* → dote base indicizzata alle risorse disponibili.

---

## 05-C3 — Carriere della ricerca: legge di programmazione decennale

**Problema in un dato.** La R&S finanziata dalla PA vale lo **0,54% del PIL** nel 2024, contro lo 0,68% UE (2023). La spesa totale in R&S è all'1,41% (UE 2,26%) e scende all'1,37% nel 2025, dato preliminare (Eurostat rd_e_gerdfund e rd_e_gerdtot; `05_rs_gerd_finanziata_pa.csv`). Gli stanziamenti di bilancio (GBARD) calano dallo 0,61% (2024) allo 0,58% (2025, provvisorio) (`05_rs_gbard.csv`).

**Soluzione.** Una legge di programmazione blinda un sentiero di +0,3 mld l'anno fino a +3,2 mld nel 2035 (0,68% del PIL). Un'Agenzia nazionale della ricerca indipendente gestisce i bandi con peer review internazionale e calendario fisso. Un tenure track unico prevede un ponte selettivo per chi ha un contratto di ricerca PNRR. Il pacchetto rientri è legato alla permanenza. Il sentiero prosegue solo se migliorano almeno 2 indicatori su 4.

| Variante | Contenuto | Costo 2027/28/29 → regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | Sentiero allo 0,68% PIL nel 2035 | 0,30 / 0,60 / 0,90 → **3,20** (2035) | 1 | SPESE_FISCALI 2,20, SAD 1,00 (ricerca su clima ed energia) |
| ESSENZIALE | Riforme + ponte per ~2.000 contratti di ricerca PNRR + sentiero dimezzato | 0,20 / 0,40 / 0,60 → **1,50** (2032) | 0,5 | SPESE_FISCALI 1,00, SAD 0,50 |
| ZERO | Solo Agenzia, tenure track e calendario, con fondi PRIN/FIS esistenti | 0 → 0 | 0,15 | — |

*Ritmo delle coperture nella PIENA*: SPESE_FISCALI 0,2 / 0,4 / 0,6 e SAD 0,1 / 0,2 / 0,3 nel 2027-29. Il prelievo cresce con il sentiero, quindi nel triennio la pressione sui fondi resta sotto 1 mld.

**Articolato normativo essenziale** (legge di programmazione)

> **Art. 1 (Finalità e sentiero).** 1. In attuazione dell'art. 9 e dell'art. 33 della Costituzione, la presente legge programma per il periodo 2027-2035 le risorse pubbliche per la ricerca. L'obiettivo è portare la spesa in ricerca e sviluppo finanziata dalle amministrazioni pubbliche dallo 0,54 per cento del PIL del 2024 allo 0,68 per cento nel 2035. 2. Gli stanziamenti aggiuntivi sono fissati nella tabella A, con un incremento annuo non inferiore a 300 milioni di euro a prezzi 2024.
>
> **Art. 2 (Agenzia nazionale della ricerca).** È istituita l'Agenzia nazionale della ricerca, dotata di autonomia scientifica, organizzativa e contabile. È governata da un consiglio scientifico in maggioranza composto da studiosi in servizio all'estero, a rotazione. L'Agenzia gestisce i programmi PRIN e FIS e i bandi sulle priorità strategiche con peer review internazionale e calendario annuale fisso. Almeno un terzo delle risorse aggiuntive è destinato a ricerca su clima, energia e adattamento.
>
> **Art. 3 (Tenure track unico).** 1. Il reclutamento universitario e degli enti di ricerca avviene mediante un contratto di ricercatore in tenure track di durata massima di sei anni, con valutazione per il passaggio a professore associato o primo ricercatore. 2. Per il biennio 2027-2028 è riservata una quota dei posti a chi è titolare di contratti finanziati dal PNRR che hanno avuto una valutazione positiva.
>
> **Art. 4 (Rientri).** Il regime fiscale agevolato per il personale di ricerca e docente che rientra in Italia è subordinato alla permanenza per almeno sei anni. A chi vince grant ERC e MSCA e sceglie un ente italiano è riconosciuto un contributo di avvio laboratorio.
>
> **Art. 5 (Clausola di revisione).** Ogni tre anni l'ANVUR e l'Agenzia trasmettono alle Camere un rapporto sugli indicatori di cui all'allegato B. L'incremento previsto dalla tabella A per il triennio successivo si applica solo se almeno due indicatori su quattro sono migliorati.
>
> **Art. 6 (Copertura finanziaria).** Agli oneri, pari a 300 milioni di euro per il 2027, 600 milioni per il 2028, 900 milioni per il 2029 e crescenti fino a 3.200 milioni annui dal 2035, si provvede: a) per due terzi, mediante le maggiori entrate derivanti dal riordino delle spese fiscali disposto annualmente con la legge di bilancio, ai sensi dell'art. 21, comma 11-bis, della legge 196/2009; b) per un terzo, mediante quota delle maggiori entrate derivanti dalla rimodulazione dei sussidi ambientalmente dannosi, vincolata alle finalità di cui all'art. 2, ultimo periodo.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | Ponte per il personale di ricerca PNRR in legge di bilancio; DDL di programmazione in CdM; censimento dei contratti PNRR in scadenza (oggi nessun dato ufficiale) | MUR, MEF, CRUI, EPR |
| 12 mesi | Legge approvata; statuto e consiglio dell'Agenzia; primo bando con calendario fisso; decreto sul tenure track | MUR, Agenzia, ANVUR |
| Fine legislatura | Sentiero a +1,5 mld (2032); primo rapporto triennale (2030) e decisione sul triennio successivo | Agenzia, ANVUR, Parlamento |

**Indicatori**

| KPI | Base | 3 anni (2029) | 5 anni (2031) |
|---|---|---|---|
| R&S finanziata dalla PA, % PIL | 0,54% (2024, Eurostat rd_e_gerdfund) | 0,58% | 0,61% |
| Spesa totale in R&S, % PIL | 1,41% (2024; 1,37% nel 2025, preliminare; Eurostat rd_e_gerdtot) | 1,50% | 1,60% |
| Saldo migratorio delle persone laureate italiane di 25-34 anni | -78.000 nel 2019-2024, cioè -13.000/anno (ISTAT, ago. 2026) | -9.000/anno | -6.000/anno |

**Rischi e mitigazione.** *Spesa che non diventa ricerca* → quota minima per progetti e infrastrutture. *Cattura accademica dell'Agenzia* → consiglio internazionale a rotazione. *Divario Nord-Sud* → bandi di capacità per gli atenei del Mezzogiorno, con valutazione separata. *Taglio nelle leggi di bilancio future* (breve negativo, ⚠️) → legge pluriennale con tabella vincolante. *Coperture incerte* (spese fiscali e SAD sono misure del menu) → clausola di revisione triennale e variante ESSENZIALE già pronta come ripiego.

---

## 05-C4 — Più persone con laurea o diploma terziario: borse, ITS Academy, residenze

**Problema in un dato.** Le persone laureate tra 25 e 34 anni sono il **31,1%** nel 2025, contro il 44,8% UE e il target UE del 45% al 2030 (Eurostat edat_lfse_03; `05_laureati_25_34.csv`).

**Soluzione.** Una borsa di studio garantita a tutte le persone idonee con un LEP nazionale, perché alla fine del PNRR (150 mln sui 708 mln delle borse 2025/26, fonte stampa, da verificare) tornerebbero le persone idonee senza borsa. Le iscrizioni agli ITS Academy si triplicano, con passerelle verso la laurea. Le residenze pubbliche a canone legato all'ISEE nascono su immobili pubblici dismessi, con una quota riservata al Mezzogiorno.

| Variante | Contenuto | Costo 2027/28/29 → regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | Borse + ITS ×3 (~100.000 iscrizioni) + residenze per 2,4 mld in 8 anni | 0,45 / 0,60 / 0,75 → **0,85** (2030) | 1 | SPESE_FISCALI 0,42, COESIONE_2127 0,30 (residenze), RIALLOCAZIONE 0,13 (dividendo demografico) |
| ESSENZIALE | Borse + ITS ×2 + residenze per 1 mld in 10 anni | 0,30 / 0,40 / 0,45 → **0,45** (2029) | 0,55 | SPESE_FISCALI 0,22, RIALLOCAZIONE 0,13, COESIONE_2127 0,10 |
| PILOTA | Solo tenuta delle borse + residenze pilota in 3 città del Sud | 0,20 → **0,20** | 0,25 | RIALLOCAZIONE 0,10, SPESE_FISCALI 0,05, COESIONE_2127 0,05 |

**Articolato normativo essenziale**

> **Art. 1 (Finalità).** Al fine di elevare la quota di giovani con titolo terziario e di rimuovere gli ostacoli economici al diritto allo studio, ai sensi dell'art. 34, terzo comma, della Costituzione, la presente legge garantisce la borsa di studio a tutta la popolazione studentesca idonea e potenzia l'istruzione terziaria professionalizzante.
>
> **Art. 2 (LEP del diritto allo studio).** 1. La borsa di studio a tutte le persone iscritte in possesso dei requisiti costituisce livello essenziale delle prestazioni ai sensi dell'art. 117, secondo comma, lettera m), della Costituzione. 2. Il Fondo integrativo statale per la concessione delle borse di studio è incrementato in misura tale da assicurare la copertura integrale delle persone idonee. Il riparto premia le Regioni che cofinanziano oltre il minimo.
>
> **Art. 3 (ITS Academy).** 1. Il Fondo per l'istruzione tecnologica superiore è incrementato con l'obiettivo di triplicare le iscrizioni entro il 2032. Una quota del 30% è ripartita in base agli esiti occupazionali a un anno rilevati dal monitoraggio INDIRE. 2. Sono garantite passerelle verso le lauree professionalizzanti, con riconoscimento dei crediti. 3. L'orientamento agli ITS è obbligatorio negli ultimi due anni della scuola secondaria di secondo grado.
>
> **Art. 4 (Residenze pubbliche).** L'Agenzia del demanio, d'intesa con il MUR e con gli enti regionali per il diritto allo studio, individua entro sei mesi immobili pubblici dismessi da destinare a residenze universitarie a canone commisurato all'ISEE, ristrutturate secondo standard di alta efficienza energetica. Almeno il 40% dei posti è riservato agli atenei del Mezzogiorno.
>
> **Art. 5 (Copertura finanziaria).** Agli oneri, pari a 450 milioni di euro per il 2027, 600 milioni per il 2028, 750 milioni per il 2029 e 850 milioni annui dal 2030, si provvede: a) per 300 milioni annui, relativi agli investimenti per le residenze, a valere sulle risorse della politica di coesione 2021-2027 e, dal 2030, del ciclo 2028-2034; b) per 130 milioni annui, mediante adeguamento dell'organico dei posti comuni al calo della popolazione scolastica, attraverso il mancato reintegro delle cessazioni; c) per la quota restante, mediante le maggiori entrate derivanti dal riordino delle spese fiscali.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | Copertura delle borse 2027/28 al posto del PNRR (evita il ritorno delle persone idonee senza borsa); mappatura degli immobili del Demanio | MUR, MEF, Agenzia del demanio, Regioni |
| 12 mesi | Decreto LEP DSU; riparto premiale del fondo ITS; primi 3 cantieri di residenze; campagna di orientamento ITS nelle superiori | MUR, MIM, Regioni, enti DSU, ITS Academy |
| Fine legislatura | Nessuna persona idonea senza borsa ogni anno; ITS a ~66-100 mila iscrizioni; 8-10 mila nuovi posti letto pubblici (stima GovernAI) | MUR, MIM, Regioni |

**Indicatori**

| KPI | Base | 3 anni (2029) | 5 anni (2031) |
|---|---|---|---|
| Persone di 25-34 anni con titolo terziario | 31,1% (2025, Eurostat edat_lfse_03) | 33% | 35% (verso il 40% nel 2035) |
| Iscritti ITS Academy | ~33.400 (1/2/2026, stampa, da confermare con MIM/INDIRE) | 55.000 | 85.000 |
| Persone idonee alla borsa ma senza borsa | copertura 99,8% nel 2024/25, con fondi PNRR (Avvenire, da verificare) | 0 | 0 |

**Rischi e mitigazione.** *ITS di qualità disomogenea* → riparto premiale sugli esiti. *Più persone laureate che poi emigrano* → combinare con 05-C3 e con le politiche salariali (area 02). *Ritardi edilizi* → procedure standard e commissario unico. *Fondi di coesione dopo il 2029* → BEI come ripiego, sapendo che i prestiti sono debito. *Conflitto con le dismissioni del Demanio a fini di riduzione del debito* → priorità agli immobili con valore di mercato basso.

---

## 05-C5 — Scuole aperte come presidi di comunità

**Problema in un dato.** Il **30,8%** della popolazione da 3 anni in su non pratica né sport né attività fisica (ISTAT, *Fattori di rischio per la salute*, 2025). Le persone NEET di 15-29 anni sono il 13,3% nel 2025, quartultimo valore UE (Eurostat edat_lfse_20; `05_neet_15_29.csv`).

**Soluzione.** Una norma quadro rende standard l'apertura extra-orario delle scuole con patti di comunità tra dirigente, Comune e ASD o associazioni, e risolve il nodo dell'assicurazione e della responsabilità a livello nazionale. Le attività sono gratuite per gli under 18 a basso ISEE. Ragazze e ragazzi NEET del Servizio civile animano le attività. Le risorse si spostano dai voucher individuali all'offerta di prossimità.

| Variante | Contenuto | Costo 2027/28/29 → regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | ~3.000 plessi | 0,15 / 0,30 / 0,40 → **0,40** (2029) | 1 | ACCISE_SALUTE 0,15, SPESE_FISCALI 0,10 (detrazione sport di ragazze e ragazzi), RIORDINO_BONUS 0,09 (Carta Valore con ISEE), RIALLOCAZIONE 0,06 (Fondo sport e periferie) |
| ESSENZIALE | ~1.500 scuole fragili (le stesse di 05-C1) | 0,10 / 0,20 / 0,20 → **0,20** (2028) | 0,5 | RIORDINO_BONUS 0,09, ACCISE_SALUTE 0,08, RIALLOCAZIONE 0,03 |
| PILOTA | 300 scuole in 10 città e aree interne | 0,02 / 0,04 / 0,04 → 0,04 | 0,1 | COESIONE_2127 0,04 |

**Articolato normativo essenziale**

> **Art. 1 (Finalità).** Al fine di promuovere l'attività fisica, la partecipazione culturale e la coesione sociale dei minori e dei giovani, gli edifici scolastici statali sono aperti oltre l'orario delle lezioni come presidi di comunità.
>
> **Art. 2 (Patti di comunità).** Il dirigente scolastico, il Comune e gli enti del Terzo settore e le associazioni sportive dilettantistiche iscritte ai rispettivi registri stipulano patti di comunità secondo lo schema tipo adottato con decreto del Ministro dell'istruzione e del merito, di concerto con il Ministro per lo sport e i giovani e con il Ministro della cultura, sentita l'ANCI. Gli enti sono selezionati con avviso pubblico.
>
> **Art. 3 (Responsabilità e assicurazione).** Durante le attività svolte in base ai patti, la custodia e la responsabilità per i danni sono in capo all'ente gestore. La copertura assicurativa è garantita da una polizza nazionale stipulata da Sport e Salute S.p.A. Il personale ATA impiegato oltre l'orario è retribuito a carico del fondo di cui all'art. 4.
>
> **Art. 4 (Fondo "Scuole aperte").** È istituito presso Sport e Salute S.p.A. il Fondo "Scuole aperte", ripartito con priorità secondo l'indice di fragilità di cui alla legge istitutiva del programma "Nessuna esclusione". Le attività sono gratuite per i minori appartenenti a nuclei con ISEE fino a 25.000 euro. Gli operatori volontari del Servizio civile universale possono svolgere attività di animazione, con attestazione delle competenze.
>
> **Art. 5 (Copertura finanziaria).** Agli oneri, pari a 150 milioni di euro per il 2027, 300 milioni per il 2028 e 400 milioni annui dal 2029, si provvede: a) per 90 milioni, mediante riduzione dell'autorizzazione di spesa della Carta Valore di cui alla legge 199/2025, la cui erogazione è subordinata a un ISEE non superiore a 35.000 euro; b) per 100 milioni, mediante soppressione della detrazione per le spese di attività sportive di ragazze e ragazzi; c) per 150 milioni, mediante quota delle maggiori entrate da accisa sui tabacchi lavorati; d) per 60 milioni, mediante corrispondente riduzione del Fondo sport e periferie.

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

## 05-C6 — AI a scuola: alfabetizzazione critica, strumenti per chi insegna, regole chiare

**Problema in un dato.** Usa l'AI il **16,4%** delle imprese italiane con almeno 10 addetti nel 2025, il doppio del 2024 (UE 20,0%) (Eurostat isoc_eb_ai; `05_imprese_ai.csv`): lavoro e scuola cambiano in fretta. Intanto alla primaria cala la matematica: il 63% di alunne e alunni di V raggiunge il livello base nel 2026, contro il 66% del 2025 (INVALSI 2026). Il rischio è che una delega non guidata all'AI peggiori gli apprendimenti di base (Bastani et al., 2024).

**Soluzione.** L'alfabetizzazione critica all'AI entra nel curricolo di educazione civica e tecnologia dalla secondaria di primo grado. La formazione docenti diventa obbligatoria: 20 ore per triennio, pagate con una quota vincolata della Carta del docente. Gli strumenti pubblici sono conformi all'AI Act e al GDPR. Regola di base: l'AI non decide voti, ammissioni, orientamento o sanzioni; le prove si riformano con più scritto in classe e più orali.

| Variante | Contenuto | Costo 2027/28/29 → regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | Curricolo + formazione + piattaforma pubblica + referenti | 0,08 / 0,18 / 0,22 → **0,22** (2029) | 1 | RIORDINO_BONUS 0,12 (Carta del docente), RIALLOCAZIONE 0,05, COESIONE_2127 0,05 (piattaforma) |
| ESSENZIALE | Curricolo + formazione + regole, strumenti tramite accordi quadro Consip | 0,04 / 0,08 / 0,08 → **0,08** (2028) | 0,45 | RIORDINO_BONUS 0,08 |
| ZERO | Solo regole e curricolo | 0 → 0 | 0,2 | — |

**Articolato normativo essenziale**

> **Art. 1 (Finalità).** Al fine di sviluppare in studentesse e studenti una comprensione critica dei sistemi di intelligenza artificiale e di garantirne un uso conforme al regolamento (UE) 2024/1689 e al regolamento (UE) 2016/679, la presente legge disciplina l'insegnamento e l'uso dell'intelligenza artificiale nelle istituzioni scolastiche.
>
> **Art. 2 (Curricolo).** Con decreto del Ministro dell'istruzione e del merito, le linee guida per l'insegnamento dell'educazione civica e della tecnologia sono integrate, dalla scuola secondaria di primo grado, con competenze su funzionamento, limiti, verifica delle fonti, bias e tutela dei dati nei sistemi di intelligenza artificiale, in coerenza con il quadro europeo DigComp.
>
> **Art. 3 (Garanzia della decisione umana).** Nessuna decisione relativa a valutazione, ammissione, orientamento o provvedimenti disciplinari può essere adottata da un sistema di intelligenza artificiale. Questi sistemi possono solo fornire suggerimenti, e il personale docente ne documenta l'uso e la decisione. Nella scuola primaria l'uso degli strumenti generativi da parte di alunne e alunni è escluso, salvo attività guidate.
>
> **Art. 4 (Formazione e strumenti).** 1. La formazione del personale docente in servizio sull'intelligenza artificiale è obbligatoria, per almeno 20 ore nel triennio. Una quota della Carta elettronica del docente, fissata con decreto, è vincolata a questa formazione. 2. Il Ministero rende disponibili strumenti selezionati con procedure che richiedono conformità al regolamento (UE) 2024/1689, trattamento dei dati nell'Unione e divieto di usare i dati di studentesse e studenti per l'addestramento commerciale.
>
> **Art. 5 (Valutazione e copertura).** 1. L'INVALSI valuta al secondo anno gli effetti sugli apprendimenti di base con un disegno controllato; gli strumenti che hanno effetti negativi sono sospesi. 2. Agli oneri, pari a 80 milioni di euro per il 2027, 180 milioni per il 2028 e 220 milioni annui dal 2029, si provvede: per 120 milioni mediante vincolo di destinazione di quota della Carta elettronica del docente; per 50 milioni mediante riorientamento delle risorse per la formazione in servizio; per 50 milioni, fino al 2029, a valere sulla programmazione FESR 2021-2027.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | DM sulla garanzia della decisione umana (variante ZERO subito operativa); linee guida del curricolo in consultazione | MIM, Garante, autorità nazionali AI (AgID/ACN) |
| 12 mesi | Curricolo in vigore dall'a.s. 2028/29; formazione avviata; gara per gli strumenti conformi all'AI Act | MIM, INDIRE, Consip |
| Fine legislatura | 100% del personale docente formato; valutazione INVALSI al 2° anno; PISA 2029 come verifica | INVALSI, INDIRE |

**Indicatori**

| KPI | Base | 3 anni (2029) | 5 anni (2031) |
|---|---|---|---|
| Docenti con formazione AI certificata | n.d. (2026; rilevazione INDIRE dal primo anno) | 60% | 100% |
| PISA matematica | 468 (2025, OCSE, da ricontrollare sulla nota OCSE) | non inferiore a 468 (PISA 2029) | ≥ media OCSE |
| Alunni di V primaria almeno al livello base in matematica (vincolo di "non danno") | 63% (2026, INVALSI) | ≥66% | ≥68% |

**Rischi e mitigazione.** *Calo delle competenze di base per delega all'AI* → niente strumenti generativi alla primaria e prove senza AI. *Lock-in tecnologico* → standard aperti e più fornitori. *Privacy* → valutazione d'impatto e Garante. *Resistenza del personale docente al vincolo sulla Carta* → la quota resta nella disponibilità del docente, solo vincolata a un fine. *Timori delle famiglie* → trasparenza e opt-out per gli strumenti non essenziali.

---

## Riepilogo dell'area

| Proposta | PIENA (regime) | ESSENZIALE | PILOTA/ZERO |
|---|---|---|---|
| 05-C1 Nessuna esclusione | 0,25 | 0,13 (int. 0,6) | 0,03 (0,1) |
| 05-C2 Conto competenze | 1,20 | 0,45 (0,45) | 0,05 (0,05) |
| 05-C3 Carriere della ricerca | 3,20 al 2035 (0,9 nel 2029) | 1,50 al 2032 (0,5) | ZERO 0 (0,15) |
| 05-C4 Terziario | 0,85 | 0,45 (0,55) | 0,20 (0,25) |
| 05-C5 Scuole aperte | 0,40 | 0,20 (0,5) | 0,04 (0,1) |
| 05-C6 AI a scuola | 0,22 | 0,08 (0,45) | ZERO 0 (0,2) |
| **Totale** | **6,12** | **2,81** | 0,32 |

Prelievo a regime per fondo nella combinazione tutta PIENA: SPESE_FISCALI 3,12; SAD 1,00; RIALLOCAZIONE 0,91; COESIONE_2127 0,73; RIORDINO_BONUS 0,21; ACCISE_SALUTE 0,15. Nessun prelievo da DEFICIT, RISPARMI_ATTESI, IVA_EVASIONE, ETS o ALTRO.

**Segnalazioni al coordinatore e all'agente coperture.**
1. Misure nuove da inserire nel menu: adeguamento dell'organico al calo demografico via turnover (RIALLOCAZIONE, 0,30); Carta Valore con ISEE (RIORDINO_BONUS, 0,09); quota vincolata della Carta del docente (RIORDINO_BONUS, 0,08-0,12); detrazione per lo sport di ragazze e ragazzi (SPESE_FISCALI, 0,10, da verificare); Fondo Nuove Competenze e quota 0,30% non optata (RIALLOCAZIONE, 0,3-0,5, da certificare).
2. SPESE_FISCALI è il fondo più usato per via di 05-C3. Senza misure del menu che lo alimentino, la scelta ragionevole per 05-C3 è la ESSENZIALE o una PIENA che nel triennio 2027-29 pesa solo 0,9.
3. COESIONE_2127 copre solo avvio e investimenti fino al 2029, mai personale stabile. Dal 2030 le note indicano chi subentra.

---

## 05-C7 — Quota svantaggio nel finanziamento delle scuole, con menu di interventi provati

*Proposta nata dal confronto con il Nord Europa (`benchmark/proposte_nord_europa.md`, codice provvisorio NE-1; analisi in `benchmark/nord_europa_scuola_welfare_cultura.md`, par. 2.1-2.2). Inserita l'8 novembre 2026. I giudizi sui valori spettano al panel indipendente.*

**Problema in un dato.** Nel 2026 solo il **63%** di alunne e alunni di V primaria raggiunge almeno il livello base in matematica, contro il 66% del 2025. L'abbandono precoce è al **13,7% nelle Isole** contro l'8,2% nazionale. L'Italia non ha una regola stabile che dia più risorse alle scuole con più popolazione scolastica in condizioni di svantaggio: i fondi arrivano a bandi temporanei (PNRR "divari", Agenda Sud, FSE+) (INVALSI 2026; Eurostat edat_lfse_16, 2025, `05_elet_18_24_nuts1.csv`).

**Soluzione.** Ogni anno le scuole statali del 20% più svantaggiato ricevono una **quota fissa in euro pro capite**, senza bando e senza domanda. L'indice lo calcola l'INVALSI (lo stesso indice di fragilità di 05-C1) e non si pubblica per nome. Almeno il **70%** della quota va a interventi di un **menu nazionale** con prove di efficacia, curato da INVALSI e INDIRE: tutoraggio in piccoli gruppi in italiano e matematica, formazione al feedback e osservazione tra colleghi, programmi strutturati di lettura. Ogni scuola rendiconta in dati aperti che cosa ha comprato e con quali esiti. La valutazione è già nel disegno: si confrontano le scuole appena sopra e appena sotto la soglia dell'indice. La lezione olandese è che i soldi senza vincolo d'uso non bastano (CPB 2017): per questo il menu è obbligatorio. **Nessun taglio all'organico**: la quota è una risorsa aggiuntiva e non usa il calo della popolazione scolastica né come copertura né per spostare posti.

| Variante | Contenuto | Costo 2027/28/29 → regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | 300 € pro capite nelle scuole del 20% più svantaggiato (circa 1,4 milioni di alunne e alunni) | 0,05 / 0,25 / 0,43 → **0,43** (2029) | 1 | SPESE_FISCALI 0,33; RIALLOCAZIONE 0,10 |
| ESSENZIALE | 250 € pro capite nelle scuole del 10% più svantaggiato (circa 0,7 milioni di alunne e alunni) | 0,03 / 0,12 / 0,19 → **0,19** (2029) | 0,55 | SPESE_FISCALI 0,14; RIALLOCAZIONE 0,05 |
| PILOTA | 3 Regioni (almeno 2 del Mezzogiorno), con valutazione a soglia | 0,01 / 0,03 / 0,03 → 0,03 (2028) | 0,1 | COESIONE_2127 0,03 (FSE+, temporaneo) |

*Come è costruito il costo (stima GovernAI)*: popolazione scolastica delle scuole statali circa 7 milioni (MIM, da verificare), il 20% è circa 1,4 milioni × 300 € = 0,42; menu, dati aperti e valutazione INVALSI-INDIRE 0,01. Totale 0,43. ESSENZIALE: 0,7 milioni × 250 € = 0,175 + 0,01 = 0,19. **Rispetto alla proposta d'origine** il costo sale da 0,40 a 0,43 (PIENA) e da 0,18 a 0,19 (ESSENZIALE), perché il conto pro capite dà 0,42 più i costi di gestione. Le coperture cambiano: tolta la "seconda quota del dividendo demografico" (scelta di chi guida il progetto: nessun taglio all'organico) e tolta la coesione dalle varianti stabili, perché i fondi UE 2021-27 finiscono nel 2029 e la quota è spesa permanente.

**Articolato normativo essenziale** (da inserire nella legge di bilancio, capo "Istruzione")

> **Art. 1 (Finalità).** Al fine di ridurre i divari negli apprendimenti di base legati alle condizioni sociali ed economiche, in attuazione degli articoli 3 e 34 della Costituzione, è istituita la quota per lo svantaggio nel finanziamento delle istituzioni scolastiche statali.
>
> **Art. 2 (Quota per lo svantaggio).** 1. A decorrere dall'anno scolastico 2027/2028 alle istituzioni scolastiche statali collocate nel quintile più svantaggiato [ESSENZIALE: nel decile] dell'indice di cui al comma 2 è assegnata ogni anno una quota pari a 300 euro [ESSENZIALE: 250 euro] pro capite. 2. L'indice è calcolato dall'INVALSI sulla base almeno dell'indice ESCS medio, della quota di alunne e alunni di recente arrivo e dei tassi di ripetenza. Coincide con l'indice di fragilità, se istituito. È usato solo per il riparto e non è pubblicato in forma nominativa. 3. La quota è assegnata d'ufficio, senza domanda. Le risorse non concorrono alla determinazione delle dotazioni organiche e non ne riducono la consistenza.
>
> **Art. 3 (Menu degli interventi).** 1. Con decreto del Ministro dell'istruzione e del merito, su proposta di INVALSI e INDIRE, è adottato il menu nazionale degli interventi con le relative schede di efficacia, aggiornato ogni due anni. 2. Almeno il 70 per cento della quota è destinato a interventi del menu. La parte restante è spesa con delibera motivata del collegio dei docenti.
>
> **Art. 4 (Trasparenza).** Ogni istituzione scolastica pubblica ogni anno, in formato aperto, gli interventi finanziati, la spesa e gli esiti rilevati. Il Ministero pubblica il quadro nazionale.
>
> **Art. 5 (Valutazione).** L'INVALSI valuta l'effetto della quota al terzo anno confrontando le istituzioni prossime alla soglia dell'indice. Se l'effetto non è significativo, il Ministro propone la revisione del menu e dei criteri di riparto.
>
> **Art. 6 (Copertura finanziaria).** Agli oneri, pari a 50 milioni di euro per il 2027, 250 milioni per il 2028 e 430 milioni annui dal 2029 [ESSENZIALE: 30, 120 e 190 milioni], si provvede: a) per 330 milioni annui dal 2029 [ESSENZIALE: 140] mediante il riordino delle agevolazioni fiscali individuate nell'allegato; b) per la parte restante mediante corrispondente riduzione delle autorizzazioni di spesa del Ministero dell'istruzione e del merito diverse da quelle per il personale. È esclusa ogni riduzione delle dotazioni organiche.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | Norma in legge di bilancio; mandato a INVALSI per l'indice e a INDIRE per il menu; parere del Garante sull'uso dei dati | MIM, MEF-RGS, INVALSI, INDIRE, Garante |
| 12 mesi | Indice e menu adottati; prima assegnazione per l'a.s. 2027/28; piattaforma di rendicontazione in dati aperti | MIM, INVALSI, INDIRE, scuole |
| Fine legislatura | Quota a regime dal 2029; prima valutazione a soglia (2030); revisione del menu | MIM, INVALSI, università |

**Indicatori**

| KPI | Base | Obiettivo a 3 anni (dato 2029) | Obiettivo a 5 anni (dato 2031) |
|---|---|---|---|
| Divario tra scuole beneficiarie e media nazionale nella quota di alunne e alunni di V primaria almeno al livello base in matematica | da calcolare su INVALSI 2026 (media nazionale 63%) | divario −20% | divario −35% |
| ELET 18-24 Isole | 13,7% (2025, Eurostat edat_lfse_16) | 11,5% (insieme a 05-C1) | 9,5% |
| Quota della spesa delle scuole beneficiarie su interventi del menu, in dati aperti | n.d. (misura nuova) | ≥70% | ≥80% |

**Rischi e mitigazione.** *Effetto nullo come nei Paesi Bassi* (CPB 2017) → vincolo del 70% al menu e valutazione a soglia già prevista; senza effetto si cambia il menu. *Soldi spesi in contratti precari* (il caso del programma olandese NPO) → quota pluriennale e stabile, che permette di programmare. *Stigma delle scuole* → indice non pubblico, quota automatica. *Doppio conteggio con 05-C1* → le squadre di 05-C1 restano finanziate da 05-C1; questa proposta aggiunge il canale ordinario e il menu. *Coperture incerte* → le spese fiscali e la revisione della spesa MIM vanno individuate dall'agente coperture; senza di esse resta la ESSENZIALE o la PILOTA.

**Fonti.** INVALSI, Rapporto 2026 (citato in 05-C1 e 05-C6); Eurostat edat_lfse_16 (`dati/serie/05_elet_18_24_nuts1.csv`); CPB, *Empirische evaluatie onderwijsachterstandenbeleid*, 21/4/2017, https://www.cpb.nl/sites/default/files/omnidownload/CPB-Notitie-21apr2017-Empirische-evaluatie-onderwijsachterstandenbeleid.pdf; CBS, indicatore di svantaggio 2019, https://www.cbs.nl/-/media/_pdf/2019/45/de-nieuwe-onderwijsachterstandenindicator-primair-onderwijs.pdf; EEF Teaching and Learning Toolkit (tutoraggio in piccoli gruppi circa +4 mesi, feedback circa +6 mesi; da ricontrollare sulle singole schede), https://educationendowmentfoundation.org.uk/education-evidence/teaching-learning-toolkit. Numero di alunne e alunni: MIM, da verificare.

---

## 05-C8 — Biblioteche di comunità: servizio minimo, biblioteca a scuola, orari estesi

*Proposta nata dal confronto con il Nord Europa (`benchmark/proposte_nord_europa.md`, codice provvisorio NE-5; analisi in `benchmark/nord_europa_scuola_welfare_cultura.md`, par. 4.1 e 4.6). Inserita l'8 novembre 2026. I giudizi sui valori spettano al panel indipendente.*

**Problema in un dato.** Nel 2022 le biblioteche di pubblica lettura hanno servito **4,9 milioni** di persone, circa l'8% della popolazione residente. La spesa pubblica per "ricreazione, cultura e religione" è lo **0,9% del PIL** contro l'1,2% UE. Nessuna regola nazionale dice quante ore deve aprire una biblioteca (ISTAT, *Focus biblioteche di pubblica lettura*, 2024; Eurostat gov_10a_exp, 2024, in `dati/verifiche/05_istruzione.md`).

**Soluzione.** La biblioteca diventa un servizio di base dei Comuni, con un **obiettivo di servizio** nel Fondo di solidarietà comunale, come per i nidi: almeno una biblioteca per Comune o per unione di Comuni, con ore minime di apertura con personale e servizi gratuiti (prestito, wifi, aiuto digitale, spazi studio). Un **fondo nazionale** di circa 5 € per abitante va solo ai Comuni che **cofinanziano**: 1 a 1 al Centro-Nord, 1 a 0,3 nel Mezzogiorno e nelle aree interne. La biblioteca civica gestisce con un bibliotecario di rete la **biblioteca delle scuole** primarie e medie, partendo da quelle dell'indice di fragilità. Gli **orari si allungano in autoservizio** (accesso con tessera sanitaria o CIE), ma solo **in aggiunta** alle ore con personale. Il modello viene da Paesi Bassi, Finlandia e Danimarca.

| Variante | Contenuto | Costo 2027/28/29 → regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | Obiettivo di servizio in tutti i Comuni; fondo di 5 € per abitante; biblioteca a scuola nel 20% più fragile; autoservizio in 1.000 sedi | 0,08 / 0,20 / 0,33 → **0,33** (2029) | 1 | SPESE_FISCALI 0,20; RIALLOCAZIONE 0,13 |
| ESSENZIALE | Fondo solo per i Comuni sotto l'obiettivo di servizio (soprattutto Sud e aree interne); biblioteca a scuola nel 10% più fragile; autoservizio in 300 sedi | 0,03 / 0,09 / 0,14 → **0,14** (2029) | 0,5 | RIALLOCAZIONE 0,07; SPESE_FISCALI 0,07 |
| PILOTA | 3 Regioni; 100 biblioteche con autoservizio; 200 scuole con biblioteca di rete | 0,01 / 0,03 / 0,03 → 0,03 (2028) | 0,1 | COESIONE_2127 0,03 (FESR/FSE+, temporaneo) |

*Come è costruito il costo (stima GovernAI)*: 5 € × circa 59 milioni di persone residenti = 0,295; biblioteca a scuola in circa 1.500 istituzioni (20% di 7.473) con una figura bibliotecaria di rete ogni 4 istituzioni (circa 375 × 40.000 € = 0,015) e 5.000 € di libri per istituzione (0,0075); gestione dell'autoservizio e monitoraggio 0,01. Totale 0,33. ESSENZIALE: circa 25 milioni di abitanti nei Comuni sotto obiettivo (stima, da verificare con il censimento) × 5 € = 0,125; scuole 0,01; gestione 0,005. Totale 0,14. L'impianto per l'autoservizio (circa 50.000 € per sede, 0,05 in tutto nella PIENA) è un investimento una tantum 2027-29 su FESR, fuori dal costo a regime. **La quota dei Comuni non è un costo per lo Stato.** **Rispetto alla proposta d'origine** la PIENA sale da 0,30 a 0,33: il solo fondo per abitante vale già 0,295, e la biblioteca a scuola e la gestione dell'autoservizio vanno aggiunte. La ESSENZIALE scende da 0,15 a 0,14. La coesione resta solo nella PILOTA e per l'investimento iniziale.

**Articolato normativo essenziale**

> **Art. 1 (Finalità).** Al fine di garantire l'accesso alla lettura, alla conoscenza e alle competenze digitali, in attuazione degli articoli 3 e 9 della Costituzione e della legge 13 febbraio 2020, n. 15, la biblioteca di pubblica lettura è riconosciuta come servizio di base dei Comuni.
>
> **Art. 2 (Obiettivo di servizio).** 1. Con decreto del Ministro della cultura, d'intesa in Conferenza unificata, sono fissati gli obiettivi di servizio delle biblioteche di pubblica lettura: almeno una biblioteca per Comune o per unione di Comuni, ore minime di apertura con personale, servizi di base gratuiti. 2. Gli obiettivi sono inseriti tra quelli del Fondo di solidarietà comunale e monitorati con l'ISTAT.
>
> **Art. 3 (Fondo per le biblioteche di comunità).** 1. È istituito presso il Ministero della cultura il Fondo per le biblioteche di comunità, con una dotazione di 80 milioni di euro per il 2027, 200 milioni per il 2028 e 330 milioni annui dal 2029 [ESSENZIALE: 30, 90 e 140 milioni, solo per i Comuni sotto l'obiettivo di servizio]. 2. Il Fondo finanzia solo spesa corrente ed è assegnato ai Comuni che cofinanziano almeno in pari misura, ridotta al 30 per cento nelle Regioni del Mezzogiorno e nelle aree interne. 3. Il Comune che riduce le ore di apertura con personale perde il contributo.
>
> **Art. 4 (Biblioteca a scuola).** Le istituzioni scolastiche del primo ciclo stipulano convenzioni con la biblioteca civica per la gestione della biblioteca scolastica, con priorità per le scuole a più alto indice di fragilità. Le convenzioni sono parte dei Patti locali per la lettura.
>
> **Art. 5 (Orari estesi).** Le biblioteche possono aprire in autoservizio con accesso tramite tessera sanitaria o carta d'identità elettronica, solo in aggiunta alle ore con personale previste dall'obiettivo di servizio.
>
> **Art. 6 (Copertura finanziaria).** Agli oneri si provvede: a) per 200 milioni annui dal 2029 [ESSENZIALE: 70] mediante il riordino delle agevolazioni fiscali individuate nell'allegato; b) per la parte restante mediante corrispondente riduzione delle autorizzazioni di spesa del Ministero della cultura indicate nell'allegato. Gli investimenti per l'autoservizio sono a valere sui programmi FESR 2021-2027, previa riprogrammazione.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | Norma in legge di bilancio; censimento ISTAT delle biblioteche rispetto agli standard; avvio dell'intesa in Conferenza unificata | MiC, MEF, ISTAT, ANCI, Regioni |
| 12 mesi | Decreto sugli obiettivi di servizio; primo riparto del fondo; prime convenzioni biblioteca-scuola; bando FESR per l'autoservizio | MiC, MIM, Comuni, sistemi bibliotecari |
| Fine legislatura | Fondo a regime dal 2029; 70% dei Comuni sopra l'obiettivo; rapporto pubblico su uso e ore | MiC, ISTAT, Comuni |

**Indicatori**

| KPI | Base | Obiettivo a 3 anni (dato 2029) | Obiettivo a 5 anni (dato 2031) |
|---|---|---|---|
| Utenti delle biblioteche di pubblica lettura | 4,9 milioni (2022, ISTAT) | 5,8 milioni | 6,5 milioni |
| Comuni (o unioni) che rispettano l'obiettivo di servizio | n.d. (censimento ISTAT al primo anno) | 70% | 90% |
| Persone di 6 anni e più che hanno letto almeno un libro in 12 mesi | 57,1% (2024, ISTAT, *Libri e biblioteche*; definizione da verificare) | +2 punti | +4 punti, con divario Sud-Nord ridotto di un terzo |

**Rischi e mitigazione.** *Comuni con poche risorse che non cofinanziano* → cofinanziamento ridotto al Sud e nelle aree interne, gestione in unione. *Autoservizio usato per tagliare il personale* → il contributo si perde se scendono le ore con personale. *Spesa in edifici invece che in servizi* → il fondo paga solo spesa corrente; gli investimenti vanno su FESR. *Effetto solo su chi già legge* → biblioteca a scuola con priorità alle scuole fragili. *Coperture incerte* → le misure su spese fiscali e bilancio MiC vanno individuate dall'agente coperture.

**Fonti.** ISTAT, *Focus biblioteche di pubblica lettura* (2024), https://www.istat.it/wp-content/uploads/2024/07/Focus_Biblioteche_pubblica_lettura.pdf; ISTAT, *Report biblioteche in Italia* (2021, iscritti al prestito 15,2% nel 2019), https://www.istat.it/it/files/2021/04/REPORT_BIBLIOTECHE-IN-ITALIA.pdf; ISTAT, *Libri e biblioteche, anni 2024-2025*, https://www.istat.it/wp-content/uploads/2026/07/Report_Libri-e-biblioteche_Anni-2024-2025.pdf; Eurostat gov_10a_exp, GF08 (in `dati/verifiche/05_istruzione.md`, che verifica anche le 7.473 istituzioni scolastiche); Finlandia, legge 1492/2016, https://www.finlex.fi/en/laki/kaannokset/2016/en20161492; Paesi Bassi, Kamerstuk 36 902 n. 2 (stato dell'approvazione da verificare); Danimarca, biblioteche aperte, https://slks.dk/fileadmin/publikationer/rapporter_oevrige/AAbne_biblioteker._Rapport.pdf. Popolazione residente circa 59 milioni (ISTAT, da verificare all'ultimo dato).

---

## 05-C9 — Zaino culturale a scuola e tariffa sociale della cultura

*Proposta nata dal confronto con il Nord Europa (`benchmark/proposte_nord_europa.md`, codice provvisorio NE-6; analisi in `benchmark/nord_europa_scuola_welfare_cultura.md`, par. 4.2, 4.4 e 4.5). Inserita l'8 novembre 2026. I giudizi sui valori spettano al panel indipendente.*

**Problema in un dato.** La spesa pubblica per i servizi culturali è di **7,6 mld €** nel 2024 e l'intera funzione cultura e ricreazione vale lo **0,9% del PIL** contro l'1,2% UE. Una parte degli aiuti ai giovani passa per carte individuali per i diciottenni: nel 2025 la Carta cultura giovani e la Carta del merito avevano 180 milioni stanziati e ne sono stati impegnati 140 (Eurostat gov_10a_exp, in `dati/verifiche/05_istruzione.md`; OpenBDAP-RGS, Rendiconto 2025, MiC cap. 1430).

**Soluzione.** Ogni alunna e ogni alunno, ogni anno, vive **almeno due esperienze culturali professionali dentro l'orario scolastico**: teatro, musica, danza, cinema, mostre, archivi, siti del patrimonio. Almeno una riguarda il patrimonio del territorio. I soggetti culturali sono scelti con avviso pubblico regionale e criteri di qualità; i luoghi della cultura statali partecipano gratis. È il modello norvegese dello "zaino culturale". Accanto c'è una **tariffa sociale della cultura** su app IO, sul modello fiammingo: per minori e giovani fino a 25 anni con ISEE fino a 15.000 €, sconto dell'**80%** su biglietti e corsi dei soggetti culturali che aderiscono; lo Stato paga il 60% dello sconto, il soggetto culturale o il Comune il 40%. Il diritto si attiva da solo con l'ISEE. Dopo una valutazione pubblica dell'uso delle carte individuali, il Parlamento può spostarne una parte su zaino e tariffa sociale.

| Variante | Contenuto | Costo 2027/28/29 → regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | Zaino a 20 € pro capite dalla primaria alle superiori; tariffa sociale nazionale | 0,05 / 0,15 / 0,20 → **0,20** (2029) | 1 | SPESE_FISCALI 0,10; RIALLOCAZIONE 0,10 |
| ESSENZIALE | Zaino a 15 € pro capite in primaria e secondaria di primo grado; tariffa sociale nei Comuni capoluogo e nelle aree interne | 0,03 / 0,08 / 0,10 → **0,10** (2029) | 0,5 | RIALLOCAZIONE 0,05; SPESE_FISCALI 0,05 |
| PILOTA | 3 Regioni, tutti i gradi, con tariffa sociale nei loro capoluoghi | 0,01 / 0,02 / 0,02 → 0,02 (2028) | 0,1 | COESIONE_2127 0,02 (FSE+, temporaneo) |

*Come è costruito il costo (stima GovernAI)*: alunne e alunni dalla primaria alle superiori, statali e paritari, tra 6,5 e 7 milioni (MIM, da verificare) × 20 € = 0,13-0,14; tariffa sociale circa 0,05 (partecipazione del 30% degli aventi diritto, da verificare); coordinamento nazionale e piattaforma 0,01. Totale 0,20, come nella proposta d'origine. ESSENZIALE: circa 4,2 milioni di alunne e alunni del primo ciclo (da verificare) × 15 € = 0,06; tariffa sociale ridotta 0,03; coordinamento 0,01. Totale 0,10. **Rispetto alla proposta d'origine** i costi restano uguali, cambiano le coperture: la quota delle carte culturali individuali (RIORDINO_BONUS 0,06-0,10) **non è usata**. La Carta Valore dal 2027 è già usata da RB01 e da 05-C5, la sua dotazione 2027 (180 milioni) è nota solo da fonti di stampa e manca un dato sull'uso per fascia ISEE. Il dato verificato del 2025 (MiC cap. 1430: 180,3 milioni iniziali, 140,3 definitivi, 132,1 pagati) mostra stanziamenti non spesi, e spendere stanziamenti che non si sarebbero spesi non è una copertura. Se l'agente coperture certifica una misura nuova sulle carte, potrà sostituire una parte di SPESE_FISCALI.

**Articolato normativo essenziale**

> **Art. 1 (Finalità).** Al fine di garantire a tutta la popolazione scolastica l'accesso all'arte, allo spettacolo e al patrimonio culturale, in attuazione degli articoli 3, 9 e 34 della Costituzione, sono istituiti lo zaino culturale scolastico e la tariffa sociale della cultura.
>
> **Art. 2 (Zaino culturale).** 1. A decorrere dall'anno scolastico 2027/2028 ogni alunna e ogni alunno delle scuole primarie e secondarie [ESSENZIALE: del primo ciclo] partecipa ad almeno due esperienze culturali professionali all'anno nell'orario scolastico, di cui almeno una sul patrimonio culturale del territorio. 2. Le Regioni formano il catalogo dei soggetti culturali con avviso pubblico, secondo criteri di qualità fissati con decreto del Ministro della cultura e del Ministro dell'istruzione e del merito. 3. I luoghi della cultura statali accolgono gratuitamente le attività. 4. Le esperienze sono preparate in classe con il personale docente.
>
> **Art. 3 (Tariffa sociale della cultura).** 1. I minori e i giovani fino a 25 anni appartenenti a nuclei con ISEE non superiore a 15.000 euro hanno diritto a uno sconto dell'80 per cento sui titoli di accesso e sui corsi dei soggetti culturali aderenti [ESSENZIALE: nei Comuni capoluogo e nelle aree interne]. 2. Lo Stato rimborsa il 60 per cento dello sconto; il restante 40 per cento è a carico del soggetto culturale o del Comune. 3. Il diritto è riconosciuto d'ufficio tramite l'ISEE e reso disponibile sull'app IO, senza domanda.
>
> **Art. 4 (Valutazione).** Il Ministero della cultura, con l'ISTAT, valuta ogni anno la partecipazione culturale per fascia ISEE e pubblica una valutazione dell'uso delle carte culturali individuali, anche ai fini del loro riordino.
>
> **Art. 5 (Coordinamento).** Presso il Ministero della cultura opera un nucleo di coordinamento con il Ministero dell'istruzione e del merito, senza nuove assunzioni.
>
> **Art. 6 (Copertura finanziaria).** Agli oneri, pari a 50 milioni di euro per il 2027, 150 milioni per il 2028 e 200 milioni annui dal 2029 [ESSENZIALE: 30, 80 e 100 milioni], si provvede per metà mediante il riordino delle agevolazioni fiscali individuate nell'allegato e per metà mediante corrispondente riduzione delle autorizzazioni di spesa dei Ministeri della cultura e dell'istruzione indicate nell'allegato, escluse quelle per il personale scolastico.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | Norma in legge di bilancio; decreto sui criteri di qualità; progetto della tariffa sociale su app IO con INPS (ISEE) | MiC, MIM, PagoPA, INPS |
| 12 mesi | Cataloghi regionali; zaino attivo dall'a.s. 2027/28; tariffa sociale attiva; prima rilevazione MIM delle esperienze | Regioni, scuole, soggetti culturali, Comuni |
| Fine legislatura | Regime dal 2029; valutazione pubblica sulla partecipazione per ISEE e sulle carte individuali | MiC, ISTAT, Parlamento |

**Indicatori**

| KPI | Base | Obiettivo a 3 anni (dato 2029) | Obiettivo a 5 anni (dato 2031) |
|---|---|---|---|
| Alunni con almeno 2 esperienze culturali professionali nell'anno scolastico | n.d. (rilevazione MIM dal primo anno) | 70% | 95% (PIENA) |
| Divario di partecipazione culturale fuori casa dei 6-17 anni tra primo e ultimo quintile ISEE | n.d. (da calcolare sull'indagine ISTAT *Aspetti della vita quotidiana*) | −15% | −30% |
| Aventi diritto che usano la tariffa sociale almeno una volta l'anno | 0 (misura nuova) | 25% | 35% |

**Rischi e mitigazione.** *Spettacoli senza legame con la didattica* (la critica norvegese) → preparazione in classe e criteri di qualità. *Offerta poco controllata* (la critica francese alla parte collettiva del Pass Culture) → avviso pubblico e controllo regionale. *Aree interne senza offerta* → spettacoli itineranti e trasporto pagato dallo zaino. *Operatori che non aderiscono alla tariffa sociale* → rimborso rapido su piattaforma unica. *Conflitto sulle carte individuali* → nessun taglio prima della valutazione pubblica; la proposta non dipende da quel riordino.

**Fonti.** Eurostat gov_10a_exp, GF08/GF0802 (in `dati/verifiche/05_istruzione.md`); OpenBDAP-RGS, Rendiconto 2025 per capitolo, MiC cap. 1430 (`dati/raw/00b_openbdap_rendiconto_2025_spese_capitolo.csv`); Kulturtanken, lettera di assegnazione 2024, https://cms12.regjeringen.no/contentassets/89353a08c9c74f0abad39907ccb24939/kulturtanken-den-kulturelle-skolesekken-norge-tildelingsbrev-2024.pdf; Città di Gand, UiTPAS con statuto di opportunità, https://stad.gent/nl/cultuur-vrije-tijd/uitpas-met-kansenstatuut; Cour des comptes sul Pass Culture (dicembre 2024), sintesi https://www.artcena.fr/fil-vie-pro/pass-culture-un-bilan-severe-dresse-par-la-cour-des-comptes. Numero di alunne e alunni: MIM, da verificare.

---

*Le proposte che seguono nascono dal confronto sulla ricerca e l'innovazione nelle imprese (`benchmark/ricerca_innovazione.md`), 9 novembre 2026.*

## 05-C10 — Rete nazionale per la ricerca applicata: i centri nati con il PNRR lavorano per le imprese, sul modello Fraunhofer

**Problema in un dato.** Con il PNRR sono nati **5 Centri nazionali** (1,6 mld), **11 Ecosistemi dell'innovazione** (1,3 mld) e **14 Partenariati estesi** (1,61 mld): circa **4,5 mld** in tutto, con scadenza nel 2026 e nessuna regola di finanziamento dopo il PNRR (Camera, monitoraggio PNRR M4C2; MUR, DD 475/2026). Le fondazioni che li gestiscono chiedono ora contributi annuali a università ed enti. In Germania la Fraunhofer ha un bilancio di **3,6 mld €** e riceve il finanziamento di base solo fino a **un terzo** del bilancio per la ricerca a contratto; nel 2024 ha incassato **867 milioni** dalle imprese (Fraunhofer, 2024).

**Soluzione.** Una legge crea la **Rete nazionale per la ricerca applicata**. Ne fanno parte da 15 a 20 nodi, scelti con una valutazione internazionale tra i Centri nazionali, gli Ecosistemi, i Partenariati del PNRR, i centri di competenza e gli istituti applicati degli enti pubblici di ricerca. Ogni nodo è una fondazione con imprese nel consiglio.
- **Regola di finanziamento.** Lo Stato paga **un euro di finanziamento di base per ogni euro di contratti con le imprese**, fino a un terzo del bilancio del nodo. Il resto arriva da contratti e da bandi competitivi (Horizon Europe, PRIN, regioni). Chi non trova clienti riceve meno; dopo tre anni sotto soglia esce dalla rete.
- **PMI.** I contratti con le PMI contano il doppio ai fini del finanziamento di base, per un tetto del 30% della base.
- **Dottorati industriali.** I nodi ospitano **1.500 dottorati industriali l'anno**, cofinanziati al 50% dalle imprese, come i dottorati innovativi del PNRR (DM 117/2023), che non hanno più fondi.
- **Regole comuni.** Contratti tipo per la proprietà intellettuale, tariffe pubbliche, bilancio e risultati in dati aperti.

La valutazione può essere affidata all'Agenzia nazionale della ricerca di 05-C3, se istituita. La rete è il luogo dove le imprese spendono il credito di 01-P13 e dove nascono le prove di fattibilità di 01-P15.

| Variante | Contenuto | Costo 2027/28/29 → regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | 15-20 nodi; base fino a 0,35 mld legata ai contratti con imprese; 1.500 dottorati industriali l'anno | 0,10 / 0,20 / 0,30 → **0,40** (2031) | 1 | RIALLOCAZIONE 0,10 (quota del FOE); SPESE_FISCALI 0,15; COESIONE_2834 0,10; SAD 0,05 (nodi su energia e clima) |
| ESSENZIALE | 8 nodi; base fino a 0,17 mld; 750 dottorati industriali l'anno | 0,05 / 0,10 / 0,15 → **0,20** (2030) | 0,5 | RIALLOCAZIONE 0,08; SPESE_FISCALI 0,05; COESIONE_2834 0,05; SAD 0,02 |
| PILOTA | Voucher per le PMI che comprano ricerca da 5 centri PNRR (almeno 2 nel Mezzogiorno), 2027-2029 | 0,02 / 0,05 / 0,05 → 0,05 (2028) | 0,12 | COESIONE_2127 0,05 (FESR, temporaneo) |

*Nota del coordinamento (9 novembre 2026): le quote indicate su COESIONE_2834 sono contate come RIALLOCAZIONE, perché nel registro dei fondi COESIONE_2834 ha capienza minima zero e non è una copertura certa. Se i fondi di coesione 2028-34 saranno assegnati, potranno sostituire la riallocazione.*

*Come è costruito il costo (stima GovernAI)*: la Fraunhofer incassa dalle imprese 867 milioni con un PIL tedesco circa doppio di quello italiano; una rete italiana che arrivi a circa 350 milioni di contratti con imprese nel 2031 riceve fino a 0,35 di base. Dottorati: 1.500 l'anno × 10.000 € l'anno di quota pubblica (metà di una borsa di circa 60.000 € in tre anni) × 3 coorti = 0,045. Valutazione internazionale e segreteria 0,005. Totale 0,40. ESSENZIALE: base 0,17 + dottorati 0,0225 + segreteria 0,005 = 0,20. *Ritmo delle coperture nella PIENA*: 2027 COESIONE_2127 0,05 (attrezzature e voucher PMI, non personale) e RIALLOCAZIONE 0,05; 2028 COESIONE_2127 0,10, RIALLOCAZIONE 0,08, SAD 0,02; 2029 COESIONE_2127 0,10, RIALLOCAZIONE 0,10, SAD 0,05, SPESE_FISCALI 0,05; dal 2031 la composizione a regime. La RIALLOCAZIONE è una quota del Fondo ordinario degli enti di ricerca (FOE, 1.686,5 mln nel 2025, OpenBDAP cap. 7236 MUR), circa il 6%: gli istituti degli enti che entrano nella rete la recuperano solo se trovano clienti.

**Articolato normativo essenziale**

> **Art. 1 (Finalità).** Al fine di collegare la ricerca pubblica alle esigenze delle imprese e di rendere stabili le infrastrutture di ricerca realizzate con il Piano nazionale di ripresa e resilienza, in attuazione degli articoli 9 e 33 della Costituzione, è istituita la Rete nazionale per la ricerca applicata.
>
> **Art. 2 (Nodi della rete).** 1. Possono chiedere di far parte della Rete le fondazioni dei Centri nazionali, degli Ecosistemi dell'innovazione e dei Partenariati estesi finanziati dal PNRR, i centri di competenza ad alta specializzazione e gli istituti di ricerca applicata degli enti pubblici di ricerca. 2. I nodi sono selezionati da un comitato di valutazione composto in maggioranza da persone esperte in servizio all'estero, sulla base della qualità scientifica, della domanda delle imprese e di un piano di attività a cinque anni. I nodi sono non più di venti [ESSENZIALE: otto]. 3. Almeno un terzo dei nodi ha sede principale nel Mezzogiorno.
>
> **Art. 3 (Finanziamento di base condizionato).** 1. Ogni nodo riceve ogni anno un finanziamento di base pari ai ricavi da contratti di ricerca con imprese dell'anno precedente, fino a un terzo del proprio bilancio. 2. I ricavi da contratti con micro, piccole e medie imprese sono conteggiati per il doppio, entro il 30 per cento del finanziamento di base. 3. Il nodo che per tre anni consecutivi non raggiunge una soglia minima di ricavi da imprese, fissata con decreto, esce dalla Rete.
>
> **Art. 4 (Dottorati industriali).** Il Ministero dell'università e della ricerca cofinanzia ogni anno fino a 1.500 [ESSENZIALE: 750] borse di dottorato industriale svolte presso i nodi della Rete e presso imprese, a condizione che l'impresa finanzi almeno la metà della borsa.
>
> **Art. 5 (Regole comuni e trasparenza).** 1. Con decreto sono adottati contratti tipo per la proprietà intellettuale e le tariffe di riferimento. 2. Ogni nodo pubblica in formato aperto bilancio, contratti con imprese per classe dimensionale, brevetti, licenze e dottorati. 3. Ogni cinque anni la Rete è valutata da un comitato internazionale; l'esito è trasmesso alle Camere.
>
> **Art. 6 (Copertura finanziaria).** Agli oneri, pari a 100 milioni di euro per il 2027, 200 milioni per il 2028, 300 milioni per il 2029 e crescenti fino a 400 milioni annui dal 2031 [ESSENZIALE: 50, 100, 150 e 200 milioni dal 2030], si provvede: a) nel triennio 2027-2029, per attrezzature e voucher alle imprese, a valere sui programmi FESR 2021-2027 e, dal 2030, sulla programmazione 2028-2034; b) mediante riduzione della quota del Fondo ordinario per gli enti e le istituzioni di ricerca non legata a programmi, per 100 milioni annui a regime; c) per la parte destinata ai nodi su energia, clima ed economia circolare, mediante quota delle maggiori entrate dalla rimodulazione dei sussidi ambientalmente dannosi; d) per la parte restante mediante il riordino delle agevolazioni fiscali individuate nell'allegato.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| Primi 100 giorni | Norma in legge di bilancio; ponte di 12 mesi per i centri PNRR che presentano un piano di attività con imprese; avvio del comitato di valutazione | MUR, MIMIT, MEF, fondazioni PNRR |
| 12 mesi | Selezione dei nodi; contratti tipo; primo finanziamento di base sui contratti 2027; primo bando dottorati industriali | MUR, comitato internazionale, nodi |
| Fine legislatura | Rete a regime (2031); prima valutazione quinquennale; uscita dei nodi sotto soglia | MUR, Agenzia nazionale della ricerca (05-C3), Parlamento |

**Indicatori**

| KPI | Base | 3 anni (2029) | 5 anni (2031) |
|---|---|---|---|
| Ricavi dei nodi da contratti con imprese | n.d. (rilevazione dal primo anno) | 200 mln | 350 mln |
| Entrate di università ed enti pubblici di ricerca da licenze | 5,87 mln (2023, Netval 2025) | 8 mln | 12 mln |
| Dottorati industriali avviati nell'anno con cofinanziamento d'impresa | dottorati innovativi PNRR esauriti (DM 117/2023; dato annuo da verificare) | 1.000 | 1.500 |

**Rischi e mitigazione.** *Salvare tutto il PNRR per inerzia* → selezione internazionale e numero massimo di nodi; chi non trova clienti esce. *Contratti fittizi o con imprese collegate* → contratti con imprese controllate dai soci del nodo conteggiati al 50%; audit annuale. *Ricerca di base trascurata* → la rete riguarda solo la ricerca applicata; la ricerca di base resta in 05-C3. *Divario Nord-Sud* → un terzo dei nodi nel Mezzogiorno e contratti con PMI conteggiati il doppio. *Opposizione degli enti di ricerca alla quota del FOE* → la quota resta agli istituti che entrano nella rete e trovano clienti. *Coperture incerte* (spese fiscali e SAD sono misure del menu) → variante ESSENZIALE pronta come ripiego.

**Fonti.** Camera dei deputati, monitoraggio PNRR M4C2, https://temi.camera.it/leg19/pnrr/politiche/OCD54-9/universita-e-ricerca.html; MUR, Focus Centri nazionali, Ecosistemi, Partenariati estesi, https://www.mur.gov.it/sites/default/files/2023-12/M4C2_1.4%20Focus%20per%20Centri%20nazionali.pdf; MUR, DD 475 del 23/4/2026, https://www.mur.gov.it/sites/default/files/2026-04/Decreto%20Direttoriale%20n.%20475%20del%2023-04-2026.pdf; Fraunhofer, finanze, https://www.fraunhofer.de/en/about-fraunhofer/profile-structure/facts-and-figures/finances.html; Comin, Licht, Pellens, Schubert, *Do Companies Benefit from Public Research Organizations? The Impact of the Fraunhofer Society in Germany*, ZEW DP 19-006, 2019, https://www.zew.de/PU80724; UK Catapult Network Review 2023, https://assets.publishing.service.gov.uk/media/6503184897d3960014482f14/catapult-network-review-2023-update.pdf; Netval 2025; MUR, DM 117/2023 (dottorati innovativi, borsa circa 60.000 €, 50% impresa), https://www.mur.gov.it/it/pnrr/misure-e-componenti/m4c2/investimento-33-introduzione-di-dott-innovativi-che; OpenBDAP-RGS, Rendiconto 2025, cap. 7236 MUR. Da verificare: numero esatto degli Ecosistemi (11 secondo il MUR, alcune fonti ne citano 12-13); fondi post-PNRR già decisi per i centri; numero di dottorati innovativi attivati per ciclo.
