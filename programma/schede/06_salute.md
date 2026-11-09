# Schede pronte — Area 06 Salute

*Agente ministeriale Salute di GovernAI, 7 novembre 2026. Fonti: dossier `ministeri/06_salute.md`, verifica `dati/verifiche/06_salute.md`, serie `dati/serie/06_*.csv`, registro `registro/fondi.csv`, giudizio del panel `motore/esito.md`. Varianti e coperture: `programma/varianti/06_salute.csv`. La scheda C7 (fine vita) è valoriale e resta fuori dal programma finanziato.*

## Premessa: il vincolo che guida tutte le schede

- **Il FSN non basta.** Il DDL di bilancio 2027 porta il FSN a 146,3 mld nel 2027 (+3,4 mld), poi la crescita scende sotto 1 mld l'anno (147,2 nel 2028; serie `06_fsn_pil.csv`). Quell'incremento è già destinato (tariffe, liste d'attesa 300 mln, indennità PS 380 mln, tetti farmaceutici). La capienza nuova del FSN è 0–0,5 mld (`registro/fondi.csv`), cioè **0 nello scenario prudente**.
- **Di conseguenza** le varianti ESSENZIALE e PILOTA usano solo fondi generali (spese fiscali, accise salute, riallocazione, riordino bonus) o la coesione 2021-27 per le sperimentazioni temporanee. Il FSN compare solo nelle varianti PIENE, per piccole quote (0,5 mld in tutto), e solo se il menu attiva la misura **FSN-INT** generata da C6.
- **Nessun risparmio atteso è usato come copertura**: ricoveri evitati, appropriatezza ed emersione del lavoro di cura si contano solo ex post.
- **Priorità dell'area** (giudizio del panel): con la Carta 1 C2 personale e C3 Case della Comunità erano nel nucleo robusto. Con la Carta 2.0 (8 novembre 2026) sono «dipendenti dai valori»: C3 resta nella prima metà della classifica nel 74% delle combinazioni di pesi, appena sotto la soglia del nucleo (75%), C2 nel 55% (`motore/esito.md`). C6 è a costo quasi zero ed entra sempre. Pacchetto minimo consigliato: **C6 ZERO o PIENA + C2 ESSENZIALE + C3 ESSENZIALE + C1 ZERO**, circa 2,2–2,5 mld a regime.

### Misure di copertura che l'agente coperture dovrebbe inserire nel menu

| Codice | Misura | Fondo | Gettito (stima GovernAI) | Chi paga |
|---|---|---|---|---|
| SF-SAN1 | Detrazione IRPEF 19% delle spese sanitarie decrescente tra 50.000 e 120.000 € di reddito; salve le spese per disabilità e patologie croniche gravi | SPESE_FISCALI | 0,4–0,7 mld (da verificare sul Rapporto spese fiscali 2025) | redditi alti |
| SF-SAN2 | Tetto alla deducibilità dei contributi ai fondi sanitari integrativi (oggi 3.615,20 €) e all'esenzione dei piani sanitari aziendali oltre 75.000 € di reddito | SPESE_FISCALI | 0,2–0,4 mld (da verificare) | redditi alti, fondi integrativi |
| SF-SAN3 | Riassorbimento nel budget di cura (C4) delle agevolazioni per assistenti familiari e assistenza personale oltre una soglia di reddito | SPESE_FISCALI | da quantificare | famiglie con redditi alti |
| AS-SAN1 | Allineamento graduale delle accise su sigarette, trinciato e tabacco riscaldato verso i paesi UE con accisa più alta, oltre i 112 mln del DDL 2027 (art. 33) | ACCISE_SALUTE | 0,5–1,0 mld, decrescente | fumatori, filiera del tabacco |
| AS-SAN2 | Accisa sui superalcolici +20% | ACCISE_SALUTE | 0,1–0,2 mld | consumatori di superalcolici |
| R-SAN1 | Abrogazione della riduzione del payback per le aziende che investono (DDL 2027, art. 71) | RIALLOCAZIONE | 0,16 mld | industria farmaceutica |
| R-SAN2 | Riduzione per legge del tetto di spesa per beni e servizi non sanitari degli enti SSN, con gare centralizzate | RIALLOCAZIONE | 0,3–0,5 mld | fornitori SSN |
| RB-SAN1 | Fusione nel budget di cura di trasferimenti permanenti frammentati per persone anziane e caregiver | RIORDINO_BONUS | da quantificare con l'area 02 | nessuno perde a parità di bisogno |
| FSN-INT | Riallocazione interna al FSN da budget unico del farmaco, biosimilari e gare centralizzate, certificata con la riduzione per legge del tetto corrispondente | FSN | 0,2–0,5 mld | fornitori e industria |

Il gettito della sugar tax (circa 0,34 mld/anno dal 1/7/2027) è già nei saldi del DDL 2027 e non è conteggiato come risorsa nuova.

---

## 06-C1 — Tempo garantito o rimborso

### Problema in un dato
Il 2,5% delle persone di 16 anni e più ha rinunciato a cure mediche necessarie per costi, distanza o attese nel 2025, contro l'1,9% del 2024 e il 2,4% della media UE; la sola attesa pesa per lo 0,9% (Eurostat, EU-SILC hlth_silc_08, 2025; serie `06_bisogni_non_soddisfatti.csv`). Le famiglie pagano di tasca propria 42,4 mld, il 22,3% della spesa sanitaria corrente (ISTAT-SHA via Eurostat hlth_sha11_hf, 2025; serie `06_spesa_sanitaria_finanziamento.csv`).

### Soluzione
Se il CUP non colloca una prestazione nei tempi della classe di priorità, il sistema offre in automatico un'alternativa (altra struttura pubblica, intramoenia, privato accreditato) al costo del solo ticket. La differenza la paga l'ASL inadempiente; dopo due trimestri di ritardo si sospende l'intramoenia nelle specialità critiche. Agenda unica CUP, richiamo attivo e criteri RAO vincolanti governano l'appropriatezza.

| Variante | Contenuto | Costo a regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | Tutte le classi U, B, D, P | 1,0 mld (2029) | 1,0 | SPESE_FISCALI 0,5; RIALLOCAZIONE 0,4; FSN 0,1 |
| ESSENZIALE | Garanzia automatica per le classi B e D | 0,5 mld (2028) | 0,6 | SPESE_FISCALI 0,3; RIALLOCAZIONE 0,2 |
| ZERO | Solo agenda unica, richiamo attivo, RAO, audit, sospensione intramoenia | 0 | 0,25 | — |

### Articolato normativo essenziale
**Art. 1 (Finalità).** Al fine di rendere esigibile il diritto ai tempi massimi di attesa previsti dal Piano nazionale di governo delle liste d'attesa, il presente articolo disciplina la garanzia automatica di erogazione delle prestazioni specialistiche ambulatoriali.

**Art. 2 (Garanzia automatica).** 1. Quando il sistema di prenotazione non è in grado di assicurare la prestazione entro il tempo massimo previsto per le classi di priorità B e D [PIENA: U, B, D e P], l'azienda sanitaria propone d'ufficio, entro 48 ore, la prestazione presso altra struttura pubblica, in regime di libera professione intramuraria o presso una struttura privata accreditata, nei tempi previsti. 2. All'assistito è richiesta la sola quota di partecipazione alla spesa, se dovuta. 3. La differenza di costo è posta a carico del bilancio dell'azienda sanitaria inadempiente.

**Art. 3 (Agenda unica e appropriatezza).** 1. Entro sei mesi dall'entrata in vigore, le Regioni e le Province autonome assicurano che tutte le agende delle strutture pubbliche e private accreditate siano gestite dal CUP regionale; sono vietate le agende chiuse. 2. Le prescrizioni con classe di priorità applicano i criteri dei raggruppamenti di attesa omogenei definiti con decreto del Ministro della salute, previa intesa in Conferenza Stato-Regioni. 3. L'Agenas effettua audit sui prescrittori con quote di priorità B superiori di oltre il 50% alla media regionale.

**Art. 4 (Sanzioni organizzative).** Nelle aziende che superano le soglie di ritardo per due trimestri consecutivi è sospesa l'attività libero-professionale intramuraria nelle discipline interessate, fino al rientro nei tempi. Il Ministero della salute può esercitare i poteri sostitutivi previsti dall'articolo 120 della Costituzione.

**Art. 5 (Monitoraggio e revisione).** L'Agenas monitora l'attuazione tramite la Piattaforma nazionale delle liste d'attesa. Dopo 24 mesi Agenas e Ufficio parlamentare di bilancio valutano la misura; se la spesa per prestazioni alternative supera del 30% le previsioni senza riduzione dei tempi, il Ministro propone la revisione del meccanismo.

**Art. 6 (Copertura finanziaria).** Agli oneri, pari a 300 mln nel 2027 e 500 mln annui dal 2028 [PIENA: 500 mln nel 2027, 900 mln nel 2028 e 1.000 mln dal 2029], si provvede mediante le maggiori entrate derivanti dalla rimodulazione della detrazione per spese sanitarie di cui all'articolo 15, comma 1, lettera c), del TUIR per i redditi superiori a 50.000 euro, e mediante le minori spese derivanti dalla riduzione del limite di spesa per beni e servizi non sanitari degli enti del SSN. Le somme sono ripartite tra le Regioni in proporzione alle prestazioni fuori soglia rilevate dalla Piattaforma.

### Cronoprogramma
| Fase | Ministero della Salute | Regioni | AGENAS | ASL |
|---|---|---|---|---|
| Primi 100 giorni | Norma in legge di bilancio; schema di DM sulla garanzia e sui RAO; intesa sul Piano nazionale 2026-28 | Censimento delle agende chiuse | Estende la Piattaforma a tutte le prestazioni del nuovo Piano | Nominano il responsabile unico dell'accesso |
| 12 mesi | Adozione del DM; primo riparto delle risorse | Agenda unica CUP con il privato accreditato in tutte le Regioni | Primo rapporto trimestrale per ASL; avvio audit sui prescrittori | Garanzia automatica attiva per B e D; richiamo attivo |
| Fine legislatura | Valutazione a 24 mesi e revisione; eventuale estensione a P | Premialità legata ai tempi nella verifica LEA | Valutazione con UPB | ≥ 90% di prestazioni B e D nei tempi |

### Indicatori
| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Persone con bisogni di cure non soddisfatti per costo, distanza o attesa | 2,5% (2025, Eurostat hlth_silc_08) | ≤ 1,9% | ≤ 1,5% |
| Bisogni non soddisfatti per sola attesa | 0,9% (2025, Eurostat hlth_silc_08) | ≤ 0,6% | ≤ 0,4% |
| Prestazioni B e D erogate nei tempi | circa 2,8 mln prestazioni fuori soglia nel I semestre 2026 (Agenas via stampa, da verificare sul bollettino) | 80% nei tempi | ≥ 90% nei tempi |

### Rischi e mitigazione
- **Domanda inappropriata indotta**: RAO vincolanti, audit sui prescrittori, allarme di spesa per ASL.
- **Spostamento verso il privato**: la sospensione dell'intramoenia e l'agenda unica spingono il pubblico a riorganizzarsi; revisione triennale delle quote.
- **Resistenza delle Regioni**: misura agganciata alla verifica LEA e alla premialità; poteri sostitutivi come ultima istanza.
- **Costo sottostimato** (non c'è una stima ufficiale): clausola di revisione al 30% di scostamento.

---

## 06-C2 — Patto per il personale infermieristico e la medicina generale

### Problema in un dato
L'Italia ha 6,9 infermieri praticanti ogni 1.000 abitanti (2024: 407.750 persone) contro 9,2 della media OCSE, mentre i medici sono 5,75 ogni 1.000, sopra la media OCSE di 3,9: il rapporto infermieri/medici è 1,2 (Eurostat hlth_rs_prs2, 2024, serie `06_personale_sanitario.csv`; OCSE, *Health at a Glance 2025*). Il problema è il mix professionale e la distribuzione, non il numero totale di medici.

### Soluzione
Più infermieri formati e trattenuti dove servono (borse con vincolo SSN, indennità di area disagiata, carriera di pratica avanzata con prescrizione limitata), e medici di famiglia che lavorano in squadra nelle Case della Comunità. Il task shifting regolato libera tempo medico per i casi complessi. È la condizione perché C3 funzioni.

| Variante | Contenuto | Costo a regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | Pacchetto completo, inclusa la doppia opzione MMG (dipendenza o convenzione con ore in CdC) e la specializzazione universitaria in medicina generale | 2,5 mld (2030) | 1,0 | SPESE_FISCALI 1,0; ACCISE_SALUTE 0,8; RIALLOCAZIONE 0,55; FSN 0,15 |
| ESSENZIALE | Indennità mirata (100.000 infermieri), borse, monte ore MMG in CdC in convenzione, pratica avanzata | 1,4 mld (2029) | 0,6 | SPESE_FISCALI 0,6; ACCISE_SALUTE 0,5; RIALLOCAZIONE 0,3 |
| PILOTA | 4 Regioni e aree interne, 5.000 borse, pratica avanzata in 50 CdC | 0,35 mld (2029) | 0,2 | SPESE_FISCALI 0,2; ACCISE_SALUTE 0,15 |

### Articolato normativo essenziale
**Art. 1 (Finalità).** Al fine di colmare il divario nella dotazione di personale infermieristico e di rafforzare l'assistenza primaria, la presente legge reca misure per la formazione, la permanenza nel Servizio sanitario nazionale e l'organizzazione del lavoro delle professioni sanitarie del territorio.

**Art. 2 (Borse di studio con impegno di servizio).** 1. È istituito presso il Ministero della salute un fondo per borse di studio destinate agli studenti dei corsi di laurea in infermieristica, di importo pari a 5.000 euro annui. 2. Il beneficiario si impegna a prestare servizio nel SSN per almeno tre anni dopo il conseguimento del titolo, con priorità nelle aziende con carenza certificata; in caso di inadempimento restituisce le somme percepite.

**Art. 3 (Indennità di area disagiata).** Ai dipendenti del SSN appartenenti al profilo infermieristico in servizio nelle aree interne e nelle aziende con rapporto infermieri/abitanti inferiore alla soglia fissata con decreto del Ministro della salute, d'intesa con la Conferenza Stato-Regioni, è riconosciuta un'indennità annua lorda fino a 3.000 euro, legata alla permanenza in servizio. L'indennità non è cumulabile con l'indennità di pronto soccorso.

**Art. 4 (Infermiere di pratica avanzata).** Il Governo è delegato ad adottare, entro dodici mesi, uno o più decreti legislativi per istituire la laurea magistrale a indirizzo clinico e il profilo dell'infermiere di pratica avanzata, con facoltà di prescrizione limitata di presidi e farmaci per la cronicità secondo protocolli nazionali, definendo la responsabilità professionale.

**Art. 5 (Medicina generale nelle Case della Comunità).** 1. L'accordo collettivo nazionale della medicina generale prevede un monte ore settimanale obbligatorio presso le Case della Comunità e l'esercizio in forma aggregata. 2. [PIENA] Il medico può optare per il rapporto di lavoro dipendente presso le Case della Comunità; il corso di formazione specifica in medicina generale è trasformato in scuola di specializzazione universitaria.

**Art. 6 (Copertura finanziaria).** Agli oneri, pari a 400 mln nel 2027, 900 mln nel 2028 e 1.400 mln annui dal 2029 [PIENA: 600, 1.200, 1.800 mln e 2.500 dal 2030], si provvede mediante le maggiori entrate derivanti dalla rimodulazione delle agevolazioni fiscali sulle spese sanitarie e sui contributi ai fondi sanitari integrativi per i redditi elevati, dall'aumento delle aliquote di accisa sui tabacchi lavorati e dalla riduzione del limite di spesa per beni e servizi non sanitari degli enti del SSN.

### Cronoprogramma
| Fase | Ministero della Salute | Regioni | AGENAS | ASL |
|---|---|---|---|---|
| Primi 100 giorni | DDL delega in CdM; fondo borse in legge di bilancio; DM sulle soglie di carenza; atto di indirizzo SISAC per l'ACN | Mappa delle aree disagiate | Metodo di calcolo del fabbisogno di personale per ASL | Ricognizione dei posti vacanti |
| 12 mesi | Delega approvata; primi bandi borse (a.a. 2027/28) con il MUR | Programmazione posti nei corsi di laurea in aumento | Prima rilevazione di permanenza e dimissioni | Indennità erogata; ore MMG in CdC nei contratti |
| Fine legislatura | Decreti legislativi su pratica avanzata e (PIENA) specializzazione MMG; valutazione a 5 anni | Infermieri di pratica avanzata nelle CdC | Valutazione dell'effetto sugli iscritti | Organici territoriali allo standard DM 77 |

### Indicatori
| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Infermieri praticanti per 1.000 abitanti | 6,92 (2024, Eurostat hlth_rs_prs2) | 7,3 | 7,7 (8 entro il 2035) |
| Rapporto infermieri/medici | 1,2 (2024, Eurostat hlth_rs_prs2) | 1,3 | 1,4 |
| Posti di medicina generale scoperti | oltre 5.500 (Gimbe 2025, da verificare su dati SISAC) | -25% | -50% |

### Rischi e mitigazione
- **Conflitto con gli ordini medici sul task shifting**: protocolli nazionali condivisi, responsabilità chiarita per legge, sperimentazione valutata.
- **Incentivi che spostano personale senza aumentarlo**: indennità legate alla permanenza e ai nuovi posti; borse con vincolo SSN.
- **Effetti lenti** (3–5 anni per i laureati): la PILOTA misura presto l'effetto dell'indennità; clausola di revisione se gli iscritti non crescono del 30%.
- **Reclutamento estero non etico**: rispetto del Codice OMS.

---

## 06-C3 — Case della Comunità vive

### Problema in un dato
Al 31/12/2025 solo 66 Case della Comunità su 1.715 programmate erano pienamente operative (3,9%); 781 (45,5%) avevano almeno un servizio attivo; gli Ospedali di Comunità con almeno un servizio erano 163 su 594 (Agenas, Report nazionale DM 77, II semestre 2025; verificato in `dati/verifiche/06_salute.md`). Il target PNRR è chiuso al 30/6/2026: senza fondi di gestione restano muri senza servizi.

### Soluzione
Un "contratto di prossimità" triennale per ogni CdC: fondo nazionale vincolato con quota base e quota a risultato (ore di apertura medica e infermieristica, cronici presi in carico, ADI). Ogni hub garantisce MMG h12 (dal C2), infermiere di famiglia, prelievi e diagnostica di base, sportello sociale unico con il Comune. I costi di personale MMG e infermieristico stanno in C2 e non si contano due volte.

| Variante | Contenuto | Costo a regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | Tutte le 1.715 CdC e i 594 OdC | 1,5 mld (2030) | 1,0 | SPESE_FISCALI 0,5; RIALLOCAZIONE 0,45; ACCISE_SALUTE 0,4; FSN 0,15 |
| ESSENZIALE | Le 1.038 CdC hub del target PNRR, con perequazione per le Regioni in ritardo | 0,8 mld (2029) | 0,6 | SPESE_FISCALI 0,3; RIALLOCAZIONE 0,3; ACCISE_SALUTE 0,2 |
| PILOTA | 150 CdC hub in 5 Regioni del Mezzogiorno per 3 anni | 0,15 mld (2029) | 0,15 | COESIONE_2127 0,15 (FESR/FSE+, temporaneo) |

### Articolato normativo essenziale
**Art. 1 (Finalità).** Al fine di garantire il pieno funzionamento delle Case della Comunità e degli Ospedali di Comunità realizzati con la Missione 6 del PNRR, secondo gli standard del decreto ministeriale 23 maggio 2022, n. 77, è istituito il Fondo per i contratti di prossimità.

**Art. 2 (Fondo per i contratti di prossimità).** 1. Il Fondo, con dotazione di 300 mln nel 2027, 600 mln nel 2028 e 800 mln annui dal 2029 [PIENA: 400, 900, 1.300 mln e 1.500 dal 2030], è vincolato alle spese di gestione delle Case della Comunità hub, all'assistenza domiciliare integrata e all'integrazione socio-sanitaria. 2. Il Fondo è ripartito per il 60% come quota base, in proporzione alla popolazione servita con una quota di perequazione per le Regioni con minori strutture operative, e per il 40% come quota a risultato.

**Art. 3 (Contratto di prossimità).** 1. Per ogni Casa della Comunità hub l'azienda sanitaria, il Comune o l'ambito territoriale sociale e i medici dell'aggregazione funzionale stipulano un contratto triennale che fissa: orari di apertura medica e infermieristica, servizi minimi, numero di pazienti cronici in carico, obiettivi di assistenza domiciliare. 2. La quota a risultato è erogata in base agli indicatori rilevati da Agenas.

**Art. 4 (Assistenza domiciliare).** Le Regioni assicurano l'assistenza domiciliare integrata ad almeno il 10% della popolazione di 65 anni e più, con un'intensità minima di accessi definita con decreto del Ministro della salute.

**Art. 5 (Poteri sostitutivi).** Se entro diciotto mesi dall'assegnazione una Regione non attiva i servizi minimi in almeno il 50% delle Case della Comunità hub, il Ministro della salute, previa diffida, dispone l'affiancamento di Agenas e, in caso di persistente inadempienza, esercita i poteri sostitutivi. A tre anni le strutture sotto la soglia minima di attività sono riconvertite.

**Art. 6 (Copertura finanziaria).** Agli oneri si provvede mediante le maggiori entrate derivanti dalla rimodulazione delle agevolazioni fiscali sanitarie per i redditi elevati, dall'aumento delle accise sui tabacchi lavorati e dalla riduzione del limite di spesa per beni e servizi non sanitari degli enti del SSN. [PILOTA: a valere sui programmi regionali FESR e FSE+ 2021-2027, previa riprogrammazione.]

### Cronoprogramma
| Fase | Ministero della Salute | Regioni | AGENAS | ASL |
|---|---|---|---|---|
| Primi 100 giorni | Fondo in legge di bilancio; schema di decreto interministeriale Salute-MEF su riparto e indicatori | Elenco delle CdC hub e dei Comuni partner | Indicatori della quota a risultato; aggiornamento del monitoraggio DM 77 | Progetto di servizi per ogni hub |
| 12 mesi | Decreto adottato, primo riparto | Contratti di prossimità firmati in tutte le hub | Primo rapporto semestrale con la quota a risultato | Apertura h12 con MMG (C2); sportello sociale unico |
| Fine legislatura | Verifica a 18 mesi, poteri sostitutivi dove serve; riconversione a 3 anni | ADI al 10% degli over 65 | Valutazione su ricoveri evitabili (PNE) | 80% delle hub pienamente operative |

### Indicatori
| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| CdC pienamente operative | 66 su 1.715, 3,9% (II sem. 2025, Agenas) | 50% delle hub (ESSENZIALE) | 80% delle hub; 60% di tutte (PIENA) |
| OdC con almeno un servizio | 163 su 594, 27,4% (II sem. 2025, Agenas) | 60% | 85% |
| Over 65 in ADI | livello attuale da verificare; target PNRR 10% (M6C1) | 10% | 10% mantenuto, con intensità minima |

### Rischi e mitigazione
- **Strutture senza personale**: quota a risultato legata alle ore effettive; sinergia obbligata con C2 (se C2 non entra, la ESSENZIALE di C3 perde efficacia).
- **Duplicazione con gli studi dei MMG**: modello hub-spoke, con gli studi periferici collegati.
- **Divari Nord-Sud**: quota di perequazione; la PILOTA parte dal Mezzogiorno.
- **Doppio conteggio con C2**: i costi di MMG e infermieri sono solo in C2.

---

## 06-C4 — Budget di cura per la non autosufficienza

### Problema in un dato
La Prestazione universale per le persone anziane non autosufficienti (D.Lgs. 29/2024) resta sperimentale: 500 mln per il 2025-2026, prorogata solo al 31/12/2027 con soglia ISEE a 12.000 € (DDL bilancio 2027, art. 53 c. 3). Le famiglie pagano di tasca propria il 22,3% della spesa sanitaria corrente, 42,4 mld nel 2025 (ISTAT-SHA via Eurostat, serie `06_spesa_sanitaria_finanziamento.csv`). Circa 243.000 persone sono in lista d'attesa per una RSA (Quotidiano Sanità 2026, da verificare).

### Soluzione
Valutazione unica del bisogno (INPS + ASL + Comune) in un solo punto di accesso nella Casa della Comunità; budget di cura graduato per intensità del bisogno, con una maggiorazione se è usato per lavoro di cura regolare o servizi accreditati. Nessun beneficiario attuale dell'indennità di accompagnamento perde importo. La Prestazione universale diventa il primo livello stabile del budget.

| Variante | Contenuto | Costo a regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | Budget su 4 livelli per tutti i nuovi beneficiari, maggiorazione 40%, standard RSA | 3,0 mld (2030) | 1,0 | RIORDINO_BONUS 1,0; SPESE_FISCALI 1,0; ACCISE_SALUTE 0,5; RIALLOCAZIONE 0,5 |
| ESSENZIALE | Valutazione unica per tutti; budget solo per i bisogni gravi e gravissimi, maggiorazione 30% | 1,2 mld (2029) | 0,5 | RIORDINO_BONUS 0,5; SPESE_FISCALI 0,4; ACCISE_SALUTE 0,3 |
| PILOTA | 20 ambiti territoriali sociali per 3 anni, con valutazione dell'emersione | 0,1 mld (2028) | 0,1 | COESIONE_2127 0,1 (FSE+, temporaneo) |

### Articolato normativo essenziale
**Art. 1 (Finalità).** In attuazione della legge 23 marzo 2023, n. 33, il presente decreto legislativo istituisce il budget di cura per le persone anziane non autosufficienti, graduato secondo l'intensità del bisogno assistenziale, e il punto unico di accesso alla valutazione.

**Art. 2 (Valutazione multidimensionale unica).** 1. La valutazione del bisogno è effettuata da un'unità composta da personale dell'INPS, dell'azienda sanitaria e dell'ambito territoriale sociale, presso il punto unico di accesso della Casa della Comunità, con uno strumento nazionale unico adottato con decreto del Ministro della salute e del Ministro del lavoro. 2. L'INPS effettua audit a campione sulle valutazioni.

**Art. 3 (Budget di cura).** 1. Il budget di cura è articolato in livelli di intensità [ESSENZIALE: riservato ai nuovi beneficiari con bisogno grave e gravissimo; PIENA: quattro livelli per tutti i nuovi beneficiari]. 2. L'importo è maggiorato del 30% [PIENA: 40%] se il budget è utilizzato per lavoro di cura regolarmente contrattualizzato o per servizi accreditati. 3. La Prestazione universale di cui al D.Lgs. 29/2024 confluisce nel primo livello del budget.

**Art. 4 (Salvaguardia).** I titolari dell'indennità di accompagnamento alla data di entrata in vigore conservano l'importo in godimento. Il budget di cura si applica alle domande presentate dal 1° gennaio 2029.

**Art. 5 (Monitoraggio e revisione).** INPS e Ufficio parlamentare di bilancio valutano la misura dopo tre anni. Se la spesa supera le previsioni del 20%, i livelli sono corretti con decreto.

**Art. 6 (Copertura finanziaria).** Agli oneri, pari a 200 mln nel 2027, 700 mln nel 2028 e 1.200 mln annui dal 2029 [PIENA: 500, 1.500, 2.200 mln e 3.000 dal 2030], si provvede mediante il riordino dei trasferimenti monetari per persone anziane e caregiver che confluiscono nel budget, le maggiori entrate dalla rimodulazione delle agevolazioni fiscali per l'assistenza personale e le spese sanitarie per i redditi elevati e l'aumento delle accise sui tabacchi lavorati. Le maggiori entrate dall'emersione del lavoro di cura sono accertate ex post e destinate alla riduzione dell'onere.

### Cronoprogramma
| Fase | Ministero della Salute | Regioni | AGENAS | ASL |
|---|---|---|---|---|
| Primi 100 giorni | Schema di decreto legislativo con Lavoro e INPS; strumento nazionale di valutazione | Individuazione dei punti unici di accesso nelle CdC | Standard minimi di personale RSA | Équipe di valutazione con INPS e Comuni |
| 12 mesi | Decreto legislativo approvato; avvio PILOTA in 20 ambiti | Integrazione con i servizi sociali comunali | Monitoraggio delle valutazioni | Prime valutazioni uniche |
| Fine legislatura | Budget per le nuove domande dal 2029; valutazione a 3 anni con INPS e UPB | Standard RSA applicati | Valutazione delle liste d'attesa RSA | Valutazione unica per tutti i nuovi casi |

### Indicatori
| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Nuovi beneficiari con valutazione multidimensionale unica | 0 (nessuna valutazione unica nel 2026) | 50% | 100% |
| Quota del budget usata per lavoro regolare o servizi accreditati | da rilevare (non esiste oggi) | 40% | 60% |
| Persone in lista d'attesa per RSA | circa 243.000 (Quotidiano Sanità 2026, da verificare) | -10% | -25% |

### Rischi e mitigazione
- **Percezione di "taglio all'accompagnamento"**: salvaguardia dei diritti acquisiti per legge, avvio solo per le nuove domande.
- **Valutazioni disomogenee**: strumento nazionale unico, audit INPS.
- **Emersione inferiore alle attese**: non è usata come copertura; la PILOTA la misura prima.
- **Competenze frammentate (INPS, Comuni, SSN)**: punto unico di accesso nella CdC (sinergia con C3); regia con l'area 02.

---

## 06-C5 — Salute mentale: percorso verso il 5% del FSN

### Problema in un dato
La spesa per la salute mentale è il 2,7–3% del FSN (2024; Ministero della Salute, fonti secondarie tra 2,5% e 3,5%, da verificare sul Rapporto SISM) contro l'obiettivo del 5% fissato in Conferenza Stato-Regioni. Arrivare al 5% sul FSN 2027 di 146,3 mld costa 2,9–3,4 mld/anno (verifica `dati/verifiche/06_salute.md`; serie `06_fsn_pil.csv`).

### Soluzione
Una quota del FSN vincolata alla salute mentale e crescente ogni anno, condizionata a standard di personale. Priorità ai giovani: servizi per la transizione 14-25 anni, psicologo di base nelle Case della Comunità, organici minimi dei Dipartimenti. Poiché il FSN cresce meno di 1 mld l'anno dopo il 2027, l'incremento va coperto con risorse nuove, non solo con il vincolo di destinazione.

| Variante | Contenuto | Costo a regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | 5% del FSN nel 2031 (+0,4 punti l'anno) | 3,4 mld (2031) | 1,0 | ACCISE_SALUTE 1,0; SPESE_FISCALI 1,0; RIALLOCAZIONE 0,8; RIORDINO_BONUS 0,5; FSN 0,1 |
| ESSENZIALE | 4% del FSN nel 2030, priorità all'età evolutiva e ai 14-25 anni | 1,7 mld (2030) | 0,6 | ACCISE_SALUTE 0,6; SPESE_FISCALI 0,6; RIALLOCAZIONE 0,5 |
| PILOTA | Psicologo di base e servizi 14-25 in 200 CdC e nelle università di 6 Regioni | 0,3 mld (2029) | 0,15 | ACCISE_SALUTE 0,3 |

### Articolato normativo essenziale
**Art. 1 (Finalità).** Al fine di assicurare i livelli essenziali di assistenza per la salute mentale, con priorità per l'età evolutiva e la transizione all'età adulta, è fissata una quota minima del finanziamento del SSN destinata alla salute mentale.

**Art. 2 (Quota vincolata).** 1. A decorrere dal 2027, una quota del fabbisogno sanitario nazionale standard è vincolata alla salute mentale, in misura crescente di 0,3 punti percentuali annui fino al 4% nel 2030 [PIENA: 0,4 punti annui fino al 5% nel 2031]. 2. L'erogazione della quota è condizionata al rispetto degli standard di personale dei Dipartimenti di salute mentale ed è oggetto della verifica degli adempimenti LEA.

**Art. 3 (Servizi per i giovani).** 1. Ogni azienda sanitaria istituisce un servizio per la transizione tra 14 e 25 anni, integrato tra neuropsichiatria dell'infanzia e dell'adolescenza e psichiatria adulti. 2. Nelle Case della Comunità hub è assicurata la funzione di psicologia di base in rete con i medici di medicina generale. 3. I programmi di prevenzione nelle scuole e nelle università sono definiti con il Ministero dell'istruzione e del merito e con il MUR, sulla base di evidenze.

**Art. 4 (Personale).** Le Regioni adottano un piano di assunzioni per raggiungere gli organici minimi dei Dipartimenti; è incrementato il numero dei contratti di formazione specialistica in psichiatria e neuropsichiatria infantile. Le Regioni promuovono il superamento della contenzione meccanica.

**Art. 5 (Monitoraggio).** Il Sistema informativo salute mentale (SISM) rileva semestralmente spesa, personale e tempi di presa in carico. Ogni due anni il Ministero riferisce al Parlamento; se le risorse non sono spese per mancanza di personale, sono riorientate alla formazione.

**Art. 6 (Copertura finanziaria).** Agli oneri derivanti dall'incremento della quota, pari a 400 mln nel 2027, 900 mln nel 2028, 1.300 mln nel 2029 e 1.700 mln annui dal 2030 [PIENA: fino a 3.400 mln dal 2031], si provvede con l'incremento del FSN corrispondente, finanziato dalle maggiori entrate derivanti dall'aumento delle accise sui tabacchi lavorati e sui superalcolici, dalla rimodulazione delle agevolazioni fiscali sanitarie per i redditi elevati e dalla riduzione del limite di spesa per beni e servizi non sanitari degli enti del SSN.

### Cronoprogramma
| Fase | Ministero della Salute | Regioni | AGENAS | ASL |
|---|---|---|---|---|
| Primi 100 giorni | Norma in legge di bilancio; DM sugli standard di personale DSM; pubblicazione del Rapporto SISM | Censimento degli organici e dei servizi 14-25 | Indicatori di presa in carico | Mappatura dei percorsi età evolutiva |
| 12 mesi | Primo riparto vincolato; più contratti di specializzazione con il MUR | Piani di assunzione | Primo monitoraggio | Servizio 14-25 in ogni ASL; psicologo nelle CdC hub |
| Fine legislatura | 4% (ESSENZIALE) o 5% (PIENA) del FSN; relazione biennale al Parlamento | Organici minimi raggiunti | Valutazione sugli accessi in PS | Tempo di prima presa in carico entro 30 giorni |

### Indicatori
| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Quota del FSN destinata alla salute mentale | 2,7–3% (2024, Ministero della Salute, da verificare su SISM) | 3,6% (ESSENZIALE) / 4,1% (PIENA) | 4% / 5% |
| Personale dei DSM | 30.101 unità (2022, Ministero della Salute, da verificare) | +4.000 | +8.000 (PIENA: +14.000) |
| Accessi in PS per crisi psichiatriche di under 25 | da rilevare su flusso EMUR (base 2026) | -10% | -20% |

### Rischi e mitigazione
- **Risorse vincolate ma non spese per mancanza di personale**: piano di formazione; riorientamento automatico delle quote non spese.
- **Medicalizzazione del disagio**: priorità agli interventi psicosociali e comunitari.
- **Concorrenza con gli altri capitoli del FSN**: il vincolo è finanziato con risorse aggiuntive, non sottratte; trade-off esplicito in Conferenza Stato-Regioni.
- **Copertura da accise decrescente**: le accise calano se calano i consumi; serve una base minima garantita dal bilancio.

---

## 06-C6 — Dividendo della prevenzione e budget unico del farmaco

### Problema in un dato
La prevenzione vale il 4,5% della spesa sanitaria corrente, 8,56 mld nel 2025 (ISTAT-SHA via Eurostat hlth_sha11_hc, serie `06_spesa_sanitaria_funzioni.csv`). Gli acquisti diretti di farmaci hanno sforato il tetto dell'8,3% del FSN di 4,77 mld nel 2025 (incidenza 11,8%), con un payback a carico delle aziende di 2,38 mld, mentre la convenzionata chiude in avanzo di 0,51 mld (AIFA, consuntivo 2025; serie `06_aifa_spesa_farmaceutica_2025.csv`).

### Soluzione
Un budget unico del farmaco al posto dei tetti separati, con contratti basati sugli esiti per i farmaci ad alto costo, uso pieno dell'HTA europea e spinta su biosimilari e generici. Una quota di 1–1,5 mld del FSN si sposta verso la prevenzione a saldo invariato. Le accise salute sono una copertura del menu; un piccolo fondo aggiuntivo per screening e vaccinazioni ne usa una parte.

| Variante | Contenuto | Costo a regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | Governance del farmaco + riallocazione interna + fondo prevenzione aggiuntivo da 0,3 mld | 0,3 mld (2028) | 1,0 | ACCISE_SALUTE 0,3 |
| ZERO | Solo governance del farmaco e riallocazione interna al FSN | 0 | 0,7 | — |

La proposta genera inoltre la misura di copertura **FSN-INT** (0,2–0,5 mld), che rende finanziabili le quote FSN delle varianti PIENE di C1, C2, C3 e C5.

### Articolato normativo essenziale
**Art. 1 (Finalità).** Al fine di governare la spesa farmaceutica in base ai bisogni di salute, di ridurre il contenzioso e di rafforzare la prevenzione primaria e secondaria, il presente articolo riforma i tetti della spesa farmaceutica e istituisce il vincolo di destinazione per la prevenzione.

**Art. 2 (Budget unico del farmaco).** 1. A decorrere dal 2028 i tetti della spesa farmaceutica convenzionata e per acquisti diretti sono sostituiti da un tetto unico, determinato annualmente dall'AIFA in rapporto al FSN sulla base dei fabbisogni e delle terapie innovative attese. 2. Il ripiano dell'eventuale superamento è regolato da accordi negoziali pluriennali che tengono conto dei volumi e degli esiti.

**Art. 3 (Rimborso basato sugli esiti e HTA).** L'AIFA conclude accordi di rimborso condizionati agli esiti per i farmaci ad alto costo, utilizzando i registri di monitoraggio, e applica le valutazioni cliniche congiunte del regolamento (UE) 2021/2282. Le Regioni promuovono l'uso dei biosimilari con obiettivi minimi di prescrizione.

**Art. 4 (Prevenzione).** 1. Una quota non inferiore al 5% del fabbisogno sanitario nazionale standard è vincolata alla prevenzione collettiva e sanità pubblica, raggiunta gradualmente entro il 2030. 2. [PIENA] È istituito il Fondo per la prevenzione oncologica e vaccinale, con dotazione di 300 mln annui dal 2028, ripartito tra le Regioni con coperture degli screening e delle vaccinazioni inferiori alle soglie LEA.

**Art. 5 (Riallocazione interna).** I risparmi derivanti dalle gare centralizzate e dall'uso dei biosimilari sono accertati annualmente dall'AIFA e dal MEF e, nei limiti accertati, il corrispondente limite di spesa è ridotto e le risorse sono destinate alle finalità della presente legge.

**Art. 6 (Copertura finanziaria).** Agli oneri dell'articolo 4, comma 2, pari a 100 mln nel 2027 e 300 mln annui dal 2028, si provvede con quota delle maggiori entrate derivanti dall'aumento delle accise sui tabacchi lavorati. Le restanti disposizioni non comportano nuovi o maggiori oneri per la finanza pubblica.

### Cronoprogramma
| Fase | Ministero della Salute | Regioni | AGENAS | ASL |
|---|---|---|---|---|
| Primi 100 giorni | DDL governance del farmaco in CdM; fondo prevenzione in legge di bilancio; tavolo con AIFA e industria | Obiettivi di biosimilari | Indicatori di copertura screening per ASL | Piani di recupero degli screening |
| 12 mesi | Approvazione del DDL; AIFA calcola il primo tetto unico per il 2028 | Gare centralizzate regionali | Monitoraggio LEA prevenzione | Inviti attivi agli screening |
| Fine legislatura | Prevenzione al 5% della spesa; valutazione a 3 anni su consumi e spesa | Coperture screening sopra soglia LEA | Valutazione esiti | Coperture vaccinali sopra soglia |

### Indicatori
| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Spesa per prevenzione sulla spesa sanitaria corrente | 4,5%, 8,56 mld (2025, ISTAT-SHA via Eurostat hlth_sha11_hc) | 5,0% | 5,5% |
| Scostamento della spesa farmaceutica dal tetto | +4,77 mld sugli acquisti diretti (2025, AIFA) | scostamento dal tetto unico ≤ 1 mld | ≤ 0,5 mld, contenzioso dimezzato |
| Prevalenza di fumatori adulti | da PASSI (ISS), ultimo anno disponibile, da verificare | -2 punti | -4 punti |

### Rischi e mitigazione
- **Ricorsi delle aziende farmaceutiche**: transizione concordata, regole pluriennali stabili; coordinamento con l'area Imprese.
- **Regressività delle accise**: compensare con il fondo prevenzione nelle aree svantaggiate.
- **Gettito che cala se i consumi scendono**: è l'effetto voluto; il vincolo di destinazione ha una base minima.
- **Riallocazione che toglie risorse ad altri capitoli del FSN**: trade-off esplicitato in Conferenza Stato-Regioni.

---

## 06-C8 — Squadre infermieristiche autonome di quartiere per l'assistenza domiciliare

*Proposta nata dal confronto con il Nord Europa (`benchmark/proposte_nord_europa.md`, codice provvisorio NE-4; analisi in `benchmark/nord_europa_scuola_welfare_cultura.md`, par. 3.2). Inserita l'8 novembre 2026. I giudizi sui valori spettano al panel indipendente.*

**Problema in un dato.** Nel 2023 l'assistenza domiciliare integrata (ADI) ha dato in media **14 ore l'anno per caso trattato**, contro 16 nel 2021. L'ADI è spesso appaltata e pagata ad accesso: vince chi fa più visite brevi, non chi rende la persona più autonoma (CERGAS Bocconi, *Rapporto OASI 2025*).

**Soluzione.** Le ASL possono organizzare l'ADI in **squadre di quartiere** di 10-12 infermieri di famiglia e comunità (DM 77/2022), con autonomia su presa in carico, orari e piano di cura, in rete con il medico di famiglia e la Casa della Comunità. È il modello olandese Buurtzorg. Cambia il **modo di pagare**: tariffa a **ora di cura**, compreso il tempo per coordinarsi con famiglia, medico e assistente sociale, e non più ad accesso; vale anche per i soggetti accreditati. Ogni squadra ha un coach esterno, un sistema informatico semplice collegato al fascicolo sanitario e obiettivi pubblici. Si parte a scaglioni tra distretti, con gruppo di controllo, e si estende solo con esiti positivi. **Non è una misura di risparmio**: in Olanda il costo totale per paziente è nella media (KPMG 2015); il guadagno è di qualità e di lavoro.

| Variante | Contenuto | Costo 2027/28/29 → regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | 1.500 squadre in tutte le Regioni; fondo per le ore aggiuntive di cura | 0,03 / 0,12 / 0,20 → **0,25** (2030) | 1,0 | ACCISE_SALUTE 0,10; RIALLOCAZIONE 0,10; SPESE_FISCALI 0,05 |
| ESSENZIALE | 500 squadre nelle Regioni con meno ore ADI per assistito | 0,02 / 0,06 / 0,10 → **0,10** (2029) | 0,4 | ACCISE_SALUTE 0,05; RIALLOCAZIONE 0,05 |
| PILOTA | 60 squadre in 10 distretti, inserimento a scaglioni e valutazione | 0,01 / 0,02 / 0,02 → 0,02 (2028) | 0,1 | COESIONE_2127 0,02 (FSE+, temporaneo) |

*Come è costruito il costo (stima GovernAI)*: circa 70.000 € l'anno per squadra tra coach, formazione, sistema informatico e tempo di coordinamento riconosciuto (1.500 × 70.000 € = 0,105), più un fondo per ore di cura aggiuntive (0,15). Totale circa 0,25. ESSENZIALE: 500 × 70.000 € = 0,035 + ore aggiuntive 0,065 = 0,10. Gli stipendi degli infermieri sono già in 06-C2 e nel DM 77 e non si contano due volte. **Rispetto alla proposta d'origine** i costi restano uguali; nella PIENA il profilo annuo è corretto (0,20 nel 2029, regime nel 2030) e cambiano le coperture: tolto il FSN (le quote FSN delle PIENE dell'area valgono già 0,5 mld, il massimo della misura FSN-INT) e tolta la coesione dalla variante stabile, sostituite da RIALLOCAZIONE e SPESE_FISCALI.

**Articolato normativo essenziale**

**Art. 1 (Finalità).** Al fine di aumentare la quantità e la qualità dell'assistenza domiciliare integrata e l'autonomia delle persone assistite, il presente articolo disciplina le squadre infermieristiche di quartiere e la remunerazione a tempo di cura.

**Art. 2 (Squadre di quartiere).** 1. Le aziende sanitarie possono organizzare l'assistenza domiciliare in squadre di infermieri di famiglia e comunità, di norma non più di dodici, responsabili di un territorio definito. 2. La squadra decide la presa in carico, l'organizzazione dei turni e il piano di cura, in accordo con il medico di medicina generale e con la Casa della Comunità di riferimento.

**Art. 3 (Remunerazione a ora di cura).** Con intesa in Conferenza Stato-Regioni è definito lo standard della tariffa dell'assistenza domiciliare per ora di cura, comprensiva del tempo di coordinamento con la rete familiare e i servizi. La tariffa si applica anche agli erogatori accreditati che adottano il modello.

**Art. 4 (Sperimentazione e valutazione).** 1. Il modello è avviato con inserimento a scaglioni tra distretti, in modo da consentire il confronto con distretti di controllo. 2. L'Agenas valuta ore di cura per assistito, ricoveri evitabili, soddisfazione degli assistiti e turnover del personale, e verifica il rispetto degli standard di autonomia delle squadre.

**Art. 5 (Fondo).** È istituito il Fondo per le squadre di quartiere, con dotazione di 20 mln nel 2027, 60 mln nel 2028 e 100 mln annui dal 2029 [PIENA: 30, 120, 200 mln e 250 dal 2030], per formazione, coaching, sistemi informativi e ore di cura aggiuntive. Il Fondo è ripartito tra le Regioni con priorità per quelle con meno ore di assistenza domiciliare per assistito.

**Art. 6 (Copertura finanziaria).** Agli oneri si provvede mediante quota delle maggiori entrate derivanti dall'aumento delle accise sui tabacchi lavorati e mediante la riduzione del limite di spesa per beni e servizi non sanitari degli enti del SSN [PIENA: anche mediante la rimodulazione delle agevolazioni fiscali sanitarie per i redditi elevati]. [PILOTA: a valere sui programmi FSE+ 2021-2027, previa riprogrammazione.]

**Cronoprogramma**

| Fase | Ministero della Salute | Regioni | AGENAS | ASL |
|---|---|---|---|---|
| Primi 100 giorni | Norma in legge di bilancio; proposta di intesa sulla tariffa a ora di cura | Individuano i distretti del primo scaglione | Disegno della valutazione con distretti di controllo | Selezione delle prime squadre e dei coach |
| 12 mesi | Intesa sulla tariffa; primo riparto del Fondo | Adeguano i contratti con gli erogatori accreditati | Standard di autonomia delle squadre; prima rilevazione | Prime squadre attive; sistema informatico collegato al fascicolo |
| Fine legislatura | Estensione solo con esiti positivi | Squadre in tutte le Regioni (PIENA) o in quelle in ritardo (ESSENZIALE) | Valutazione a 3 anni pubblica | Ore per assistito in crescita, turnover sotto la media |

**Indicatori**

| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Ore ADI per caso trattato | 14 (2023, CERGAS Bocconi, OASI 2025) | 16 (insieme a 06-C3) | 18 |
| Ricoveri evitabili degli over 75 seguiti dalle squadre, rispetto ai distretti di controllo | n.d. | −5% | −10% |
| Turnover degli infermieri nelle squadre rispetto alla media regionale | n.d. (rilevazione annua pubblica) | rilevazione pubblica | sotto la media regionale |

Gli obiettivi sulle ore sono più prudenti di quelli della proposta d'origine (18 e 22): un fondo da 0,15 mld per ore aggiuntive non basta da solo a portare la media nazionale a 22.

**Rischi e mitigazione**
- **Attese di risparmio**: dichiarate nulle; la misura si giudica su ore e qualità.
- **Carenza di infermieri**: autonomia e meno burocrazia come leva per attrarre; collegamento con 06-C2.
- **Resistenza delle cooperative appaltatrici**: possono diventare squadre accreditate se accettano il modello.
- **Squadre autonome solo sulla carta**: standard di autonomia verificati da Agenas.
- **Coperture**: le accise calano se calano i consumi; la riduzione del limite di spesa per beni e servizi va certificata.

**Fonti.** CERGAS Bocconi, *Rapporto OASI 2025*, cap. B2, https://cergas.unibocconi.eu/sites/default/files/media/attach/05_Fosti_et_al_B2_OASI25.pdf; KPMG-Plexus 2015, in Kamerstuk 31 765 n. 114, https://zoek.officielebekendmakingen.nl/kst-31765-114.pdf; Commonwealth Fund 2015, https://www.commonwealthfund.org/publications/case-study/2015/may/home-care-self-governing-nursing-teams-netherlands-buurtzorg-model; DM 23 maggio 2022, n. 77.

---

## 06-C9 — Équipe di benessere scolastico in rete con la Casa della Comunità

*Proposta nata dal confronto con il Nord Europa (`benchmark/proposte_nord_europa.md`, codice provvisorio NE-2; analisi in `benchmark/nord_europa_scuola_welfare_cultura.md`, par. 2.5). Inserita l'8 novembre 2026. I giudizi sui valori spettano al panel indipendente.*

**Problema in un dato.** La spesa per la salute mentale è il **2,7-3% del FSN** contro l'obiettivo del 5%. Nelle scuole lo psicologo è finanziato a progetto o a bando annuale: non esiste un servizio stabile né un dato nazionale su quante scuole ne hanno uno. Al 31/12/2025 solo il **3,9%** delle Case della Comunità era pienamente operativo (Ministero della Salute, in 06-C5, da verificare sul Rapporto SISM; Agenas, Report DM 77, II semestre 2025, in 06-C3).

**Soluzione.** Ogni rete di scuole ha un'**équipe di benessere** collegata alla Casa della Comunità del distretto: uno psicologo, ore programmate di infermiere di famiglia e comunità, un assistente sociale del Comune come referente. È il modello svedese dell'*elevhälsa*, ma organizzato come accordo di rete tra scuola e sanità, non come nuovo ruolo dentro la scuola. Compiti: prevenzione (salute, sonno, schermi, dipendenze), ascolto, invio rapido ai servizi, sostegno ai docenti nei casi difficili. Un accordo-quadro Stato-Regioni-ANCI fissa standard minimi (ore per mille studenti) e un protocollo sulla privacy. L'équipe **non fa diagnosi a scuola** e non usa sistemi automatici di "rischio". Priorità alle secondarie e alle scuole dell'indice di fragilità.

| Variante | Contenuto | Costo 2027/28/29 → regime | Intensità | Coperture |
|---|---|---|---|---|
| PIENA | Tutte le secondarie: 1 psicologo ogni 1.500 studenti (circa 2.800), più ore infermieristiche e di servizio sociale | 0,04 / 0,12 / 0,20 → **0,20** (2029) | 1,0 | ACCISE_SALUTE 0,10; RIALLOCAZIONE 0,10 |
| ESSENZIALE | Solo le scuole del quintile fragile (le stesse di 05-C1), tutti i gradi | 0,02 / 0,06 / 0,08 → **0,08** (2029) | 0,45 | RIALLOCAZIONE 0,05; ACCISE_SALUTE 0,03 |
| PILOTA | 100 reti di scuole in 4 Regioni, con valutazione controfattuale | 0,01 / 0,03 / 0,03 → 0,03 (2028) | 0,15 | COESIONE_2127 0,03 (FSE+, temporaneo) |

*Come è costruito il costo (stima GovernAI)*: circa 4,2 milioni di studenti delle secondarie statali (da verificare su MIM) / 1.500 = circa 2.800 psicologi × 55.000 € lordi = 0,15; ore di raccordo infermieristico e sociale, formazione e protocolli 0,05. Totale 0,20. ESSENZIALE: circa 1,4 milioni di alunni del quintile fragile / 1.500 = circa 930 psicologi × 55.000 € = 0,05, più 0,03 di raccordo. Totale 0,08. Le ore di infermiere vengono in gran parte dal personale già previsto per le Case della Comunità (06-C2, 06-C3) e non si contano due volte. **Se 06-C5 è adottata**, gli psicologi di base per i 14-25 anni possono lavorare nelle équipe e il costo aggiuntivo della PIENA scende a circa 0,10. **Rispetto alla proposta d'origine** i costi restano uguali; nella ESSENZIALE la coesione (0,03 fino al 2029) è sostituita da ACCISE_SALUTE, perché si tratta di personale stabile.

**Articolato normativo essenziale**

**Art. 1 (Finalità).** Al fine di promuovere la salute e il benessere psicologico degli studenti e di prevenire il disagio e l'abbandono scolastico, il presente articolo istituisce le équipe di benessere scolastico in rete tra istituzioni scolastiche, aziende sanitarie e Comuni.

**Art. 2 (Équipe di benessere).** 1. Le aziende sanitarie assicurano a ogni rete di istituzioni scolastiche secondarie [ESSENZIALE: alle istituzioni del quintile più fragile dell'indice di fragilità] un'équipe composta da uno psicologo, da ore programmate di infermiere di famiglia e comunità e da un assistente sociale del Comune o dell'Ambito territoriale come referente. 2. L'équipe opera presso la Casa della Comunità del distretto e nelle scuole.

**Art. 3 (Standard e compiti).** 1. Con accordo in Conferenza unificata sono fissati gli standard minimi di ore per mille studenti e i compiti dell'équipe: prevenzione, ascolto, invio ai servizi, sostegno ai docenti. 2. L'équipe non effettua diagnosi a scuola e non utilizza sistemi automatizzati di valutazione del rischio individuale.

**Art. 4 (Protezione dei dati).** Il protocollo sul trattamento dei dati è adottato sentito il Garante per la protezione dei dati personali. I dati sanitari sono conservati solo nel fascicolo sanitario elettronico; per i minori si applicano le regole sul consenso dei genitori.

**Art. 5 (Valutazione).** Il Ministero della salute e il Ministero dell'istruzione e del merito, con l'ISS, valutano l'effetto delle équipe su tempi di presa in carico, benessere e abbandono, confrontando le reti avviate prima e dopo. L'estensione oltre la variante adottata è subordinata a esiti positivi.

**Art. 6 (Copertura finanziaria).** Agli oneri, pari a 20 mln nel 2027, 60 mln nel 2028 e 80 mln annui dal 2029 [PIENA: 40, 120 e 200 mln], si provvede mediante la riduzione del limite di spesa per beni e servizi non sanitari degli enti del SSN e mediante quota delle maggiori entrate derivanti dall'aumento delle accise sui tabacchi lavorati. [PILOTA: a valere sui programmi FSE+ 2021-2027, previa riprogrammazione.]

**Cronoprogramma**

| Fase | Ministero della Salute | Regioni | AGENAS | ASL |
|---|---|---|---|---|
| Primi 100 giorni | Norma in legge di bilancio; bozza di accordo-quadro con MIM e ANCI; protocollo con il Garante | Mappano reti di scuole e Case della Comunità | Disegno della rilevazione nazionale delle équipe | Censiscono psicologi e ore infermieristiche disponibili |
| 12 mesi | Accordo-quadro in Conferenza unificata; primo riparto | Avvio nelle scuole del quintile fragile o nelle reti pilota | Prima rilevazione di copertura e tempi | Équipe attive; protocolli di invio con i servizi |
| Fine legislatura | Valutazione pubblica; estensione solo con esiti positivi | Copertura di tutte le secondarie (PIENA) | Monitoraggio annuale | Tempi di primo colloquio entro 15 giorni |

**Indicatori**

| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Studenti delle secondarie coperti da un'équipe con almeno gli standard minimi | n.d. (rilevazione dal primo anno) | 50% | 90% (PIENA) |
| Tempo tra segnalazione e primo colloquio con lo psicologo | n.d. | ≤ 15 giorni | ≤ 10 giorni |
| ELET 18-24 maschi | 10,1% (2025, Eurostat edat_lfse_14) | 8,8% (insieme a 05-C1 e 05-C7) | 7,5% |

**Rischi e mitigazione**
- **Prove deboli sull'effetto**: partire dalla PILOTA con gruppo di controllo; passare alla PIENA solo con esiti positivi.
- **Medicalizzazione del disagio**: mandato preventivo e di rete, niente diagnosi in classe.
- **Privacy dei minori**: protocollo con il Garante, consenso dei genitori, dati sanitari solo nel fascicolo.
- **Mancano psicologi al Sud e nelle aree interne**: équipe di rete tra più scuole, indennità di sede di 04-P6.
- **Doppio conteggio con 06-C5**: se 06-C5 è adottata, gli psicologi di base si impiegano nelle équipe e il costo scende.

**Fonti.** Svezia, Dir. 2024:30 *En förbättrad elevhälsa*, https://www.regeringen.se/contentassets/39b4dab4d3e54fbcac52d87ab94825c4/en-forbattrad-elevhalsa-dir.-202430.pdf; Agenas, Report nazionale DM 77, II semestre 2025 (in 06-C3 e `dati/verifiche/06_salute.md`); Ministero della Salute, spesa per la salute mentale (in 06-C5, da verificare sul Rapporto SISM); Eurostat edat_lfse_14 (`dati/serie/05_elet_18_24_sesso.csv`). Numero di studenti delle secondarie: MIM, da verificare.
