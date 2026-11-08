# GovernAI e gli attori politici italiani: servizi pubblici

*Benchmark al 8 novembre 2026. Temi: sanità, istruzione e ricerca, pubblica amministrazione e digitale, giustizia, sicurezza e difesa, anticorruzione e appalti. Dati riga per riga in `benchmark/programmi/servizi_pubblici.csv`.*

## Come leggere

- **Stato.** "approvato (legge n./anno)" indica una norma in vigore. "in discussione" indica un testo all'esame del Parlamento: per la manovra 2027 è il DDL di bilancio A.C. 3174, presentato il 30/10/2026 [S1]. "proposto" indica un programma, una proposta di legge o una dichiarazione pubblica. "da verificare" indica un dato che non è stato possibile confermare su una fonte primaria.
- **Relazione con GovernAI.** Ogni misura altrui è confrontata con una proposta GovernAI (id di `motore/proposte.csv`):
  - `convergente`: stesso obiettivo e stesso strumento;
  - `parziale`: stesso obiettivo, strumento o scala diversi;
  - `divergente`: strumento o direzione opposti;
  - `assente in GovernAI`: il programma non tratta il tema.
- **Variante decisa.** Accanto a ogni proposta GovernAI è indicata la variante decisa dal Consiglio GovernAI l'8/11/2026 (`governo/verbali/2026-11-08-1-conti-in-ordine.md`).
- **Cifre.** Gli importi sono in miliardi di euro l'anno, salvo diversa indicazione. Le stime che non vengono dal proponente sono segnalate come tali.
- **Limiti.** Per alcuni partiti (IV, +Europa, Lega e Noi Moderati su alcuni temi) non sono state trovate proposte 2025-2026 verificabili. Quelle caselle riportano "da verificare" e non significano assenza di posizione. Le fonti di stampa sono state usate solo quando mancava il documento primario.

---

## 1. Sanità

| Sotto-tema | Governo (fatto e manovra 2027) | Maggioranza (proposto) | Opposizioni (proposto) | GovernAI |
|---|---|---|---|---|
| Fondo sanitario | Il FSN cresce di 2,365 mld nel 2027, di 2,352 nel 2028 e di 2,399 dal 2029 (DDL 2027, art. 69): 146,3 mld nel 2027 secondo il Governo [S1][S3]. Secondo GIMBE il rapporto FSN/PIL passa dal 6,14% al 6,11% nel 2027 e al 5,87% nel 2029 [S4]. Il tetto per gli acquisti dai privati accreditati sale di 3 punti (art. 74); 500 mln vanno all'aggiornamento delle tariffe dei ricoveri (art. 69). | FI chiede un contributo del settore finanziario, anche da CDP, per la sanità [S16]. | **PD**: PDL Schlein per portare la spesa al 7,5% del PIL in 5 anni, con +0,21% del PIL l'anno; bloccata in commissione Bilancio nel 2024 per le coperture [S17]. **M5S**: PDL per una spesa non inferiore all'8% del PIL; oltre 30 mld secondo una stima di Pagella Politica [S18]. **AVS**: imposta dell'1,3% sui patrimoni oltre 6 mln, con 15 mld l'anno per sanità e scuola [S19]. **Azione**: 4 mld della riforma IRPEF alla sanità [S21]. **PD, M5S, AVS e IV**: 16 emendamenti comuni alla manovra 2026 [S20]. | Nessuna soglia di spesa sul PIL. **06-C6** (ZERO): budget unico del farmaco e spostamento di 1-1,5 mld del FSN verso la prevenzione a saldo invariato. Coperture da spese fiscali sanitarie, accise salute e riallocazioni. |
| Liste d'attesa | **Fatto:** DL 73/2024 conv. L. 107/2024: piattaforma nazionale Agenas e CUP unico con i privati accreditati [S40]. **Manovra:** 300 mln nel 2027 per prestazioni aggiuntive del personale (art. 69 c. 4) e un documento al paziente con la tariffa della prestazione (art. 69 c. 8) [S1]. | Accordo quadro 2022: medicina di prossimità, più medici e operatori sanitari [S28]. | Da verificare: non sono state trovate PDL specifiche 2025-2026. | **06-C1** (ZERO adottata): agenda unica CUP, criteri RAO vincolanti, divieto di agende chiuse, sospensione dell'intramoenia nelle aziende inadempienti. Nella PIENA (non adottata), alternativa automatica al costo del solo ticket, pagata dall'ASL. |
| Personale | **Fatto:** superamento del test di Medicina con il semestre filtro (L. 26/2025) [S40]; misure contro le aggressioni al personale (DL 137/2024) [S40]. **Manovra:** +380 mln l'anno per l'indennità di pronto soccorso (art. 69 c. 6) [S1]. | FI: piano in 11 punti per il SSN (personale, salute mentale, farmaci innovativi entro 120 giorni) [S15]. Noi Moderati, programma 2022: psicologo di base, rafforzamento dei pronto soccorso [S29]. | PD (PDL Schlein): sblocco delle assunzioni [S17]. AVS: più medici finanziati con la patrimoniale [S19]. | **06-C2** (PILOTA adottata): borse per infermieri con vincolo SSN, indennità per le aree disagiate, pratica avanzata. La diagnosi è un problema di mix professionale: 6,9 infermieri ogni 1.000 abitanti contro 9,2 OCSE, mentre i medici sono sopra la media. |
| Medicina territoriale | Riforma dei medici di famiglia (bozza Schillaci, aprile 2026): dipendenza volontaria e ore nelle Case della Comunità; a giugno 2026 l'iter era fermo, stato attuale da verificare [S13][S14]. Prestazione universale per gli anziani prorogata al 2027 (art. 53) [S1]. | **FdI** (Gemmato): contraria alla dipendenza dei medici di famiglia [S13]. **FI**: DDL che mantiene il rapporto autonomo con alcune ore settimanali nelle Case della Comunità [S14]. | Da verificare. | **06-C2**, variante PIENA: doppia opzione per i medici di famiglia (dipendenza o convenzione con ore in CdC). **06-C3**: Case della Comunità con contratto di prossimità, respinta nel triennio in attesa dei dati sul personale. **06-C4**: budget di cura, respinta nel triennio. |
| Farmaci e dispositivi | Payback ridotto per le aziende che investono (art. 71), accesso precoce ai farmaci innovativi (art. 72), tetto dei dispositivi al 4,7% e concorso statale di 350 mln l'anno nel 2028-2031 (art. 73) [S1]. | FI: farmaci innovativi entro 120 giorni [S15]. | Da verificare. | **06-C6**: budget unico del farmaco, contratti basati sugli esiti, HTA europea. Il menu coperture prevede l'abrogazione dell'art. 71 (R-SAN1). Nessuna proposta sui dispositivi medici. |

**Punti in comune**
- Integrare i privati accreditati nella prenotazione unica: DL 73/2024 e 06-C1.
- Coinvolgere i medici di famiglia nelle Case della Comunità: bozza Schillaci, DDL FI e 06-C2. Il DDL FI coincide con la variante ESSENZIALE di 06-C2.
- Psicologo di base: programma 2022 di Noi Moderati e 06-C5.
- Tutti gli attori collocano il problema delle liste d'attesa tra le priorità.

**Dove GovernAI si distingue**
- **Nessun aumento generale del FSN e nessuna soglia sul PIL.** È diverso dal DDL 2027, dalle PDL di PD e M5S e dalla proposta AVS. Il motivo: secondo la scheda 06, l'incremento 2027 è già destinato e la capienza nuova del FSN è 0 nello scenario prudente. Con la regola "nessun risparmio a bilancio prima della certificazione", GovernAI finanzia solo misure con coperture identificate.
- **Liste d'attesa.** GovernAI agisce su regole e responsabilità dell'ASL (garanzia, sospensione dell'intramoenia) invece che su ore aggiuntive pagate (300 mln). Il motivo: la misura deve funzionare anche a costo zero.
- **Payback farmaceutico.** GovernAI va nella direzione opposta all'art. 71: le premialità all'industria diventano una fonte di copertura.
- **Personale.** La priorità sono gli infermieri. Accesso a Medicina e aumento dei medici non sono proposte GovernAI, perché i dati indicano un problema di mix professionale.

**Idee di altri che GovernAI potrebbe valutare**
- Il documento al paziente con la tariffa della prestazione (DDL 2027, art. 69 c. 8) [S1]: costo nullo, coerente con il valore FID e con 09-C1.
- Tempi massimi di accesso ai farmaci innovativi (FI, piano in 11 punti) [S15]: indicatore misurabile da collegare a 06-C6.
- Clausola di aggancio del FSN a una grandezza macro (PDL PD e M5S) [S17][S18], in forma ridotta. Un esempio è una soglia minima reale indicizzata all'inflazione, da valutare con il motore per costo e robustezza.

---

## 2. Istruzione e ricerca

| Sotto-tema | Governo (fatto e manovra 2027) | Maggioranza (proposto) | Opposizioni (proposto) | GovernAI |
|---|---|---|---|---|
| Scuola e organici | **Fatto:** voto in condotta (L. 150/2024); filiera 4+2 (L. 121/2024); riforma della maturità (DL 127/2025, numero della legge di conversione da verificare); Agenda Sud (DL 123/2023) [S40][S41]. **Manovra:** dal 2027/28, -4.925 posti dell'organico dell'autonomia e -2.049 posti ATA (art. 66 c. 5) [S1]. | **Lega**: Salvini apre a modifiche sui tagli [S6]. **Accordo quadro 2022**: piano di assunzione dei precari, formazione dei docenti, percorso meritocratico e professionalizzante [S28]. | **PD**: contrario ai tagli; usare il calo demografico per rafforzare i servizi, a partire dall'infanzia [S5]. **Azione**: tempo pieno obbligatorio [S21]. **AVS**: circa 5 mld l'anno dalla patrimoniale alla scuola [S19]. **M5S**: spostare le risorse della difesa a scuola e sanità [S22]. | **05-C1** (PIENA adottata): il dividendo demografico finanzia squadre di prossimità (tutor, educatore, mediatore) in circa 1.500 scuole fragili, con valutazione controfattuale. **05-C5** (ESSENZIALE): scuole aperte oltre l'orario. |
| Scuole paritarie e libri | Buono fino a 1.500 euro per gli studenti delle paritarie con ISEE fino a 30.000 euro, prorogato al 2027 (art. 104, 20 mln); libri in versione digitale stampabile a prezzo inferiore di almeno il 50% (art. 105); credito d'imposta per il Fondo povertà educativa (art. 106) [S1]. | **Noi Moderati**: voucher per le paritarie (DDL Gelmini) e sostegno alle paritarie nella manovra 2026 [S30]. | Da verificare. | Assenti in GovernAI. Il Fondo povertà educativa è collegato in parte a 05-C1. |
| Università e docenti | Turn over al 75% nel 2027 per università (esclusi i ricercatori) e AFAM (art. 66) [S1]; riforma del pre-ruolo (DDL A.S. 1240), stato da verificare [S42]. | Da verificare. | Da verificare. | **05-C4** (ESSENZIALE adottata): borsa garantita a tutti gli idonei come LEP, ITS raddoppiati, residenze. **05-C6** (ESSENZIALE): formazione dei docenti sull'AI, 20 ore per triennio. |
| Ricerca | Enti di ricerca con turn over ridotto del 25% (art. 66 c. 3); i Dipartimenti di eccellenza diventano progettualità strategiche dal 2028; Programma Talenti, 15 mln l'anno dal 2029 (art. 107) [S1]. | Da verificare. | Da verificare. | **05-C3**: legge di programmazione fino allo 0,68% del PIL di R&S pubblica, Agenzia indipendente, tenure track. Nel triennio resta a ZERO per mancanza di coperture certificate. |

**Punti in comune**
- Contrasto alla dispersione nelle aree più fragili: Agenda Sud e 05-C1.
- Formazione professionalizzante terziaria: filiera 4+2 e ITS in 05-C4.
- Uso del calo demografico come leva: Governo, PD e GovernAI concordano sulla diagnosi e divergono sull'uso.

**Dove GovernAI si distingue**
- **Calo degli alunni.** Il DDL 2027 riduce gli organici. GovernAI reimpiega una parte del dividendo demografico in tutor e squadre di prossimità e certifica come risparmio solo i posti non già contati nei tendenziali. Il motivo è il valore EQU: l'abbandono è al 13,7% nelle Isole.
- **Ricerca.** Il DDL 2027 riduce il turn over degli enti di ricerca. GovernAI prevede un sentiero di crescita, oggi sospeso per le coperture. Il motivo: la R&S pubblica è allo 0,54% del PIL contro lo 0,68% UE.
- **Paritarie, condotta e maturità** non sono trattate. GovernAI ha scelto di concentrarsi su dispersione, competenze e terziario.

**Idee di altri che GovernAI potrebbe valutare**
- Libri di testo in versione digitale stampabile a prezzo ridotto (DDL 2027, art. 105) [S1]: costo nullo per lo Stato e rilevante per le famiglie a basso reddito.
- Tempo pieno (Azione) [S21]: valutare un'estensione mirata alle scuole di 05-C1, con valutazione dell'effetto sugli apprendimenti.
- Programma Talenti per i dottorandi (DDL 2027, art. 107) [S1], come tassello del ponte per i ricercatori previsto da 05-C3.

---

## 3. Pubblica amministrazione e digitale

| Sotto-tema | Governo (fatto e manovra 2027) | Maggioranza (proposto) | Opposizioni (proposto) | GovernAI |
|---|---|---|---|---|
| Assunzioni | **Fatto:** DL 25/2025 conv. L. 69/2025, con concorsi centralizzati e mobilità [S38]. **Manovra:** turn over al 75% nel 2027 per ministeri, PCM, agenzie ed enti, al 100% dal 2028; -25% per autorità indipendenti ed enti vari; deroghe con DPCM (art. 66) [S1]. | Accordo quadro 2022: riforma della PA, dettagli da verificare [S28]. | Da verificare. | **09-C8** (ESSENZIALE adottata): nessun taglio uniforme; per ogni cessazione, una decisione motivata e pubblica (stesso profilo, profilo tecnico, riqualificazione, non sostituzione se il processo è automatizzato). **09-C3** (ESSENZIALE): 3.000 tecnici per i piccoli comuni. |
| Produttività e valutazione | **Fatto:** legge sul merito (L. 119/2026, GU 4/7/2026): valutazioni massime a non più del 30% del personale, quota di posti da dirigente a selezioni interne, revisione del d.lgs. 150/2009 [S37]. | FI esprime il ministro per la PA; proposte di partito distinte da verificare. | Alla Camera il DDL merito è passato con 147 sì e 90 no; il voto per gruppo è da verificare [S37]. | **09-C6** (PIENA adottata): attua la legge sul merito e aggiunge 3-5 indicatori di servizio pubblici per ufficio, calcolati dai sistemi; piano di miglioramento prima della sanzione; uffici disciplinari associati. Nessuna sorveglianza dei dipendenti. |
| IA e digitale | **Fatto:** L. 132/2025 sull'IA (decisione umana nella PA); primo decreto attuativo D.Lgs. 179/2026. **Manovra:** cessione di 3-I a Sogei, che subentra in funzioni AgID (art. 87); Osservatorio IA e lavoro rafforzato (art. 46) [S1]. | Da verificare. | Da verificare. | **09-C5** (PIENA adottata): albo AgID dei sistemi IA, valutazione d'impatto pubblica, assistente pubblico condiviso. **09-C7** (ESSENZIALE): automazione con patto di riallocazione e nessun licenziamento. **09-C4**: canoni cloud. **09-C2**: once-only con indennizzo. |

**Punti in comune**
- Valutazione selettiva nella PA, con tetto alle valutazioni massime: L. 119/2026 e 09-C6.
- IA come supporto con decisione umana: L. 132/2025 e 09-C5.
- Qualificazione delle stazioni appaltanti (D.Lgs. 36/2023) e pool di tecnici (09-C3).

**Dove GovernAI si distingue**
- **Turn over.** Il DDL 2027 lo riduce in modo uniforme per il 2027. GovernAI programma le sostituzioni per competenze e conta come risparmio solo le ore liberate dall'automazione, dopo certificazione (09-C7, 09-C8). Il motivo: una riduzione uniforme colpisce anche i profili tecnici che mancano, con il 3,8% di specialisti ICT contro il 5,0% UE.
- **Misura dei servizi.** GovernAI pubblica indicatori per ufficio e garanzie per i lavoratori: piano di miglioramento e divieto di monitoraggio biometrico o con IA. È il valore FID applicato alla PA.
- **Once-only esigibile con indennizzo** (09-C2): nessun altro attore lo propone nelle fonti consultate.

**Idee di altri che GovernAI potrebbe valutare**
- Deroghe al turn over compensate tra amministrazioni con DPCM (DDL 2027, art. 66 c. 7) [S1], come strumento operativo per riservare quote ai tecnici di 09-C3.
- Consolidare le società digitali pubbliche (DDL 2027, art. 87) [S1]: valutarne l'effetto sui costi di manutenzione considerati in 09-C4.

---

## 4. Giustizia

| Sotto-tema | Governo (fatto e manovra 2027) | Maggioranza (proposto) | Opposizioni (proposto) | GovernAI |
|---|---|---|---|---|
| Riforme | **Legge costituzionale** sulla separazione delle carriere (due CSM, sorteggio, Alta Corte), approvata il 30/10/2025 e **respinta dal referendum** del 22-23/3/2026: No 53,74%, affluenza 58,93% [S7][S8]. **L. 114/2024**: abrogazione dell'abuso d'ufficio, interrogatorio preventivo [S40]. **L. 1/2026**: riforma della Corte dei conti e della responsabilità erariale [S12]. | FdI, Lega, FI e Noi Moderati per il Sì [S9]. Per FI è "la riforma delle riforme" [S43]. Accordo quadro 2022: riforma della giustizia [S28]. | PD, M5S e AVS per il No, con posizioni diverse dentro il PD; Azione e IV per il Sì [S9]. +Europa: voto contrario alla riforma pur condividendo il principio [S10]. | Assenti in GovernAI. La Carta pone una linea rossa (FID) su ogni riduzione dell'indipendenza degli organi di controllo; L. 114/2024 e L. 1/2026 non sono state valutate dal motore. |
| Tempi dei processi | Target PNRR raggiunto: disposition time civile -50,2% sul 2019 nel primo semestre 2026, con circa 10.000 addetti all'Ufficio per il processo finanziati fino al 30/6/2026. La stabilizzazione dopo il PNRR è da verificare (scheda 07). | Da verificare. | Da verificare. | **07-C1** (ESSENZIALE adottata): 4.500 addetti all'Ufficio per il processo resi stabili nei tribunali più lenti, triage digitale (decide sempre il giudice), cruscotto trimestrale. |
| Carceri | **Fatto:** DL 92/2024 conv. L. 112/2024 (polizia penitenziaria, liberazione anticipata, commissario). Piano di edilizia da oltre 1,3 mld nel 2025-2027 per circa 10.900 posti; commissario prorogato al 31/12/2026 [S32]. 66.063 detenuti per 51.295 posti al 30/9/2026 (DAP). | Da verificare. | **IV** (Giachetti): liberazione anticipata speciale, da 45 a 60 giorni a semestre (A.C. 552); nel 2026 PDL sull'esecuzione della pena per gli over 75 [S31]. | **07-C2** (ESSENZIALE adottata): valutazione d'ufficio delle misure alternative per pene residue fino a 2 anni (esclusi i reati 4-bis), 1.000 funzionari UEPE prima dell'allargamento, braccialetti, statistica ufficiale sulla recidiva. |

**Punti in comune**
- Ridurre i tempi dei processi resta un obiettivo condiviso. GovernAI consolida lo strumento usato con il PNRR, cioè l'Ufficio per il processo.
- Sul sovraffollamento sia il Governo sia GovernAI recuperano posti (edilizia, posti inagibili). GovernAI aggiunge le misure di comunità.

**Dove GovernAI si distingue**
- **Assetto della magistratura, abuso d'ufficio, Corte dei conti.** GovernAI non ha proposte. Sono scelte istituzionali e valoriali sulle quali i partiti si sono divisi e che non sono passate dal motore.
- **Carceri.** GovernAI non propone sconti di pena (diversamente da A.C. 552), né solo edilizia (diversamente dal piano del Governo). Propone misure alternative selettive con controllo e lavoro. Il motivo: costo per detenuto di circa 178 euro al giorno e valore SIC (recidiva).

**Idee di altri che GovernAI potrebbe valutare**
- Esecuzione della pena fuori dal carcere per i detenuti molto anziani (IV, A.C. 3143) [S31], come estensione mirata di 07-C2.
- Una valutazione GovernAI della L. 1/2026 sulla responsabilità erariale rispetto alla linea rossa FID [S12].

---

## 5. Sicurezza e difesa

| Sotto-tema | Governo (fatto e manovra 2027) | Maggioranza (proposto) | Opposizioni (proposto) | GovernAI |
|---|---|---|---|---|
| Spesa NATO | Impegno dell'Aia (giugno 2025): 3,5% del PIL per la difesa "core" più 1,5% per resilienza entro il 2035 [S44]. Italia al 2,09% nel 2025 (dati NATO, scheda 07). **Manovra:** clausola di salvaguardia nazionale fino a 0,3 punti di PIL l'anno per la difesa nel 2027-2028, in deficit (DPB; DDL art. 91) [S2][S1][S27]; fondo difesa da 26 mln nel 2027 e 423 mln nel 2028 (art. 92); missioni per 520 mln nel 2027 e GCAP (art. 95) [S1]. | **FI**: scorporo delle spese per la difesa dal Patto UE [S45]. **Lega**: servizio universale di 6 mesi e riserva volontaria (PDL) [S26]. | **PD**: difesa comune europea con debito comune, no ai fondi di coesione, contrario agli aumenti lineari nazionali, con posizioni interne diverse [S24]. **M5S**: no a qualsiasi aumento ("nemmeno un euro") [S22]. **AVS**: stop agli aumenti [S23]. Azione, IV e +Europa: da verificare. | **07-C5** rinviata a ZERO: stabilizzazione al 2,1% con efficienza e acquisti comuni UE; nessun uso della clausola nazionale né dei prestiti SAFE come copertura finché il debito non torna sul percorso UE. La variante PIENA (3,5% nel 2035) costerebbe 32 mld l'anno. |
| Decreti sicurezza e forze di polizia | **Fatto:** DL 48/2025 conv. L. 80/2025; DL 23/2026 conv. L. 54/2026 (armi da taglio, daspo urbano, tutela del personale scolastico e sanitario, rimpatri) [S11]. **Manovra:** 180 assunzioni straordinarie contro la criminalità organizzata, 45 mln l'anno per la polizia locale, 50 mln di straordinari, ausiliari della riserva volontaria (artt. 96-102) [S1]. | **Lega**: Strade Sicure oltre il 2027, fino a 10.000 militari [S25]. **Noi Moderati**: sostegno al decreto 2026 [S46]. | Da verificare: non sono state trovate PDL alternative. Il voto finale alla Camera sul DL 23/2026 è stato di 162 sì e 102 no; la ripartizione per gruppo è da verificare [S11]. | **07-C3** (ESSENZIALE): rimpatri volontari assistiti, asilo deciso entro 6 mesi. **07-C6** (ESSENZIALE): centri di sicurezza cyber per sanità e comuni, riserva cyber. Nessuna proposta sugli organici di polizia. |

**Punti in comune**
- Acquisti comuni europei per la difesa: Governo (GCAP, cooperazione), PD (difesa comune) e 07-C5.
- Riserva volontaria: DDL 2027 artt. 92 e 96 e Lega; GovernAI propone una riserva solo per il cyber (07-C6).
- Tutela del personale sanitario e scolastico: DL 23/2026 e DL 137/2024. GovernAI non ha una misura specifica.

**Dove GovernAI si distingue**
- **Coperture.** GovernAI esclude ogni aumento della difesa in deficit, mentre il Governo usa la clausola nazionale. Differisce anche da M5S e AVS, che pongono un no di principio: per GovernAI la scelta tra più sicurezza oggi e meno debito domani è politica e resta aperta, e il rinvio dipende dall'allerta sul debito (139,9% del PIL).
- **Sicurezza urbana.** GovernAI non propone più agenti o militari in città: la scheda 07 copre migrazioni, beni confiscati e cyber.

**Idee di altri che GovernAI potrebbe valutare**
- Finanziare la difesa europea con debito comune UE (PD) [S24]: compatibile con 07-C5 e con 08-P4 (capacità fiscale UE), purché non diventi debito nazionale.
- Fondo per la polizia locale con criteri di riparto (DDL 2027, art. 102) [S1], da valutare con dati sui reati per comune.

---

## 6. Anticorruzione e appalti

| Sotto-tema | Governo (fatto e manovra 2027) | Maggioranza (proposto) | Opposizioni (proposto) | GovernAI |
|---|---|---|---|---|
| Codice appalti | **Fatto:** D.Lgs. 36/2023 e correttivo D.Lgs. 209/2024: qualificazione delle stazioni appaltanti, digitalizzazione, subappalto a cascata con le stesse regole del subappalto principale [S35]. | **FI**: divieto di subappalto a cascata oltre il secondo livello [S35]. | **PD**: costi della manodopera e della sicurezza esclusi dal ribasso, divieto di subappalto della progettazione [S35]. **M5S**: procedure per autorizzare e monitorare il subappalto [S35]. | **08-P7** (PIENA adottata): cruscotto ANAC dei rischi per stazione appaltante, obbligo misurato di completezza dei dati, atti in formato aperto collegati al CIG; valuta enti, mai persone. **09-C3**: stazioni appaltanti qualificate per i piccoli comuni. |
| Abuso d'ufficio | **Fatto:** abrogato con la L. 114/2024; abrogazione ritenuta legittima dalla Corte costituzionale (numero della sentenza da verificare) [S34]. La direttiva UE 2026/1021, in vigore dal 31/5/2026, prevede il reato di "esercizio illecito di funzioni pubbliche"; recepimento entro circa 2 anni. Per FdI non serve reintrodurre il reato [S33]. | FdI: posizione indicata a sinistra [S33]. | **PD, M5S e AVS**: contrari all'abrogazione, chiedono di reintrodurre il reato in sede di recepimento [S47]. **Azione e IV**: favorevoli all'abrogazione nel 2024 [S34]. | Assente in GovernAI. |
| ANAC e controlli | La relazione ANAC 2025, presentata il 21/4/2026, segnala criticità sugli affidamenti diretti; monitoraggio digitale delle stazioni appaltanti dal 1/7/2026 [S36]. L. 1/2026 sulla Corte dei conti [S12]. | Da verificare. | Da verificare. | **08-P7** usa i dati BDNCP: nel 2024 il 54,8% delle procedure competitive si è chiuso con una sola offerta. **09-C1**: registro pubblico delle analisi. |

**Punti in comune**
- Qualificazione delle stazioni appaltanti e aggregazione della domanda: Codice e 09-C3.
- Più dati sugli appalti: monitoraggio digitale ANAC e 08-P7.
- Regole sul subappalto: FI, PD e M5S propongono vincoli, ciascuno con strumenti diversi.

**Dove GovernAI si distingue**
- **Trasparenza invece di nuovi reati o divieti.** GovernAI non prende posizione su abuso d'ufficio e subappalto. Propone di misurare i rischi in modo pubblico e verificabile, con garanzie contro l'uso automatico per sanzioni. Il motivo: il valore FID e la linea rossa sulla decisione automatizzata.
- **Il beneficio di prezzo atteso da 08-P7 non è usato come copertura.**

**Idee di altri che GovernAI potrebbe valutare**
- Recepimento della direttiva 2026/1021 [S33]: GovernAI potrebbe produrre una scheda con le opzioni (nuova fattispecie minima, illecito amministrativo, rafforzamento dei controlli) e farla passare dal motore.
- Costi della manodopera esclusi dal ribasso (PD) [S35]: da valutare con i dati BDNCP su ribassi e contenziosi.
- Limite al subappalto a cascata (FI) [S35]: aggiungerlo come indicatore di rischio nel cruscotto 08-P7.

---

## Fonti

Documenti ufficiali
- [S1] Camera dei deputati, DDL "Bilancio di previsione dello Stato per l'anno finanziario 2027 e bilancio pluriennale 2027-2029", A.C. 3174, presentato il 30/10/2026, relazione illustrativa (artt. 46, 53, 66, 69-74, 87, 91-108). Copia di lavoro: `dati/raw/00b_ddl_bilancio_2027_AC3174_relazioni.txt`.
- [S2] MEF, Documento programmatico di bilancio 2027 (ottobre 2026), sezioni sulla clausola di salvaguardia nazionale. Copia: `dati/raw/00b_mef_dpb_2027.txt`.
- [S40] Normattiva, testi vigenti: [L. 114/2024](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-08-09;114); [L. 150/2024](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-10-01;150); [DL 73/2024](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2024-06-07;73); [DL 137/2024](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2024-10-01;137); [L. 26/2025](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-03-14;26); [DL 92/2024](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2024-07-04;92); [DL 48/2025](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2025-04-11;48); [D.Lgs. 36/2023](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2023-03-31;36); [D.Lgs. 209/2024](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-12-31;209); [L. 132/2025](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-09-23;132); [DL 25/2025](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2025-03-14;25); [L. 1/2026](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2026-01-07;1). Numeri e date delle leggi di conversione di DL 137/2024 e DL 127/2025: da verificare.
- [S41] Normattiva: [L. 121/2024](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-08-08;121); [DL 123/2023](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2023-09-15;123); ItaliaOggi, "DL Maturità, via libera definitivo della Camera", ottobre 2025: https://www.italiaoggi.it/settori/scuola/dl-maturita-via-libera-definitivo-della-camera-qanmppqn
- [S11] Camera, temi dell'attività parlamentare, "D.L. 23/2026": https://temi.camera.it/leg19/provvedimento/d-l-23-2026-disposizioni-urgenti-in-materia-di-sicurezza-pubblica-di-attivit-di-indagine-dell-autorit-giudiziaria-in-presenza-di-cause-di-giustificazione-di-funzionalit-delle-forze-di-polizia-e-del.html; Normattiva, L. 24/4/2026 n. 54: https://www.normattiva.it/eli/stato/LEGGE/2026/04/24/54/ORIGINAL
- [S31] Camera, attività dell'on. Giachetti (A.C. 552, 3143, 3144): https://www.camera.it/deputati/elenco/19-300480?tab=attivita_svolta
- [S32] Ministero della Giustizia, risposta all'interrogazione Aloisio, 24/4/2026: https://www.giustizia.it/cmsresources/cms/documents/interrogazione_aloisio_risposta_24apr2026.pdf
- Dati interni GovernAI: `programma/schede/05_istruzione.md`, `06_salute.md`, `07_giustizia.md`, `09_pa_digitale.md`, `12_pa_produttiva.md`, `13_integrita.md`; `motore/proposte.csv`; `governo/verbali/2026-11-08.md` e `2026-11-08-1-conti-in-ordine.md`.

Stampa e analisi
- [S3] Sky TG24, "Manovra 2027, tagli alla sanità?", 3/11/2026: https://tg24.sky.it/economia/2026/11/03/manovra-2027-tagli-sanita
- [S4] Il Fatto Quotidiano, "Manovra 2027, GIMBE: FSN", 2/11/2026: https://www.ilfattoquotidiano.it/2026/11/02/manovra-2027-gimbe-sanita-fsn-notizie/8557662/
- [S5] Orizzonte Scuola, "Manovra 2027, il PD all'attacco: altri 7mila posti tagliati", novembre 2026: https://www.orizzontescuola.it/manovra-2027-il-pd-allattacco-altri-7mila-posti-tagliati-alla-scuola-sono-tagli-strutturali-anziche-transitori/
- [S6] Orizzonte Scuola, "7mila posti in meno nella scuola... Salvini apre a modifiche", novembre 2026: https://www.orizzontescuola.it/7mila-posti-in-meno-nella-scuola-manovra-2027-e-scontro-politico-sindacati-e-opposizione-allattacco-salvini-apre-a-modifiche/
- [S7] Il Post, "Il No ha vinto al referendum costituzionale sulla giustizia", 23/3/2026: https://www.ilpost.it/2026/03/23/referendum-costituzionale-giustizia-chi-ha-vinto-no/
- [S8] AGI, approvazione definitiva della riforma, 30/10/2025: https://www.agi.it/politica/news/2025-10-30/riforma-giustizia-separazione-carriere-senato-referendum-33917195/
- [S9] Fanpage, "Chi vota Sì e chi vota No al referendum sulla giustizia 2026", marzo 2026: https://www.fanpage.it/politica/chi-vota-si-e-chi-vota-no-al-referendum-sulla-giustizia-2026-la-posizione-dei-partiti-sul-quesito/
- [S10] Il Foglio, "I separati della separazione", 19/9/2025: https://ilfoglio.it/giustizia/2025/09/19/news/i-separati-della-separazione--119737
- [S12] Sky TG24, "Il Senato approva il ddl sulla riforma della Corte dei conti", 27/12/2025: https://tg24.sky.it/politica/2025/12/27/senato-approva-riforma-corte-dei-conti; ANCE, "In Gazzetta Ufficiale la legge di riforma della Corte dei conti", gennaio 2026: https://ance.it/2026/01/in-gazzetta-ufficiale-la-legge-di-riforma-della-corte-dei-conti/
- [S13] Sky TG24, "Medici di famiglia, la riforma Schillaci si ferma", 5/6/2026: https://tg24.sky.it/politica/2026/06/05/medici-famiglia-riforma-schillaci-fermata
- [S14] QuiFinanza, "Medici di famiglia dipendenti pubblici, Governo diviso sulla riforma Schillaci", 2026: https://quifinanza.it/salute/medici-famiglia-riforma-schillaci-governo-diviso/992068/
- [S15] Quotidiano Sanità, piano di Forza Italia per il SSN, luglio 2025 (data da verificare): https://www.quotidianosanita.it/?p=144295
- [S16] ItaliaOggi, "Manovra 2027, Tajani chiede un contributo da tutta la finanza", ottobre 2026: https://www.italiaoggi.it/economia-e-politica/manovra-2027-tajani-chiede-un-contributo-da-tutta-la-finanza-anche-da-cdp-il-nodo-sui-fondi-alla-sanita-txzapjw2
- [S17] Domani, "Più soldi alla sanità, il PD sfida Meloni con la legge Schlein", 2024: https://www.editorialedomani.it/politica/italia/piu-soldi-alla-sanita-il-pd-sfida-meloni-con-la-legge-schlein-ieafqkew; testo PD: https://deputatipd.it/files/documenti/112_Sanita%CC%80_Legge_Schlein.pdf
- [S18] Pagella Politica, "Una spesa sanitaria minima imposta per legge è davvero una buona idea?", 2025: https://pagellapolitica.it/articoli/spesa-sanitaria-minima-pil-inflazione
- [S19] Il Fatto Quotidiano, contromanovra AVS, 11/11/2025: https://www.ilfattoquotidiano.it/2025/11/11/contromanovra-legge-bilancio-meloni-tagli-news/8191078/
- [S20] Il Foglio, "Il campo largo propone tanto senza fare i conti", 20/11/2025: https://www.ilfoglio.it/economia/2025/11/20/news/il-campo-largo-propone-tanto-senza-fare-i-conti-8343134/
- [S21] LaPresse, "Cernobbio, parola alle opposizioni", 8/9/2024: https://www.lapresse.it/politica/2024/09/08/cernobbio-parola-alle-opposizioni/; Fanpage, intervista a Calenda sul tempo pieno: https://www.fanpage.it/politica/calenda-a-fanpage-it-sanita-e-istruzione-prima-di-tutto-a-scuola-serve-tempo-pieno-obbligatorio/
- [S22] Il Foglio/Adnkronos, "Conte e il no M5S al riarmo", 5/8/2026: https://www.ilfoglio.it/adnkronos/politica/2026/08/05/conte-e-il-no-m5s-al-riarmo-non-chiedeteci-nemmeno-un-euro--41en84YEZJs1ynhedHuuI0; Open, 13/10/2026: https://www.open.online/2026/10/13/conte-manovra-armi-italiani-non-mangiano-risorse-vadano-sanita-istruzione/
- [S23] Il Foglio (EN), intervista a Bonelli, 30/7/2026: https://www.ilfoglio.it/en/politics/2026/07/30/news/bonelli-re-armament-is-madness-enough-weapons-for-ukraine-von-der-leyen-is-embarrassing--403606
- [S24] Sky TG24, intervista a Schlein, 6/3/2025: https://tg24.sky.it/politica/2025/03/06/elly-schlein-pd-intervista; Pagella Politica, "Sulle spese militari il PD non trova una linea comune": https://pagellapolitica.it/articoli/pd-spese-militari-italia
- [S25] Open, "Strade sicure, la Lega...", 14/9/2026: https://www.open.online/2026/09/14/strade-sicure-lega-risoluzione-commissione-fdi-fi/
- [S26] Orizzonte Scuola, "Servizio militare universale di sei mesi: la proposta della Lega" (data da verificare): https://www.orizzontescuola.it/servizio-militare-universale-di-sei-mesi-la-proposta-della-lega-per-ragazzi-e-ragazze/
- [S27] QuiFinanza, "Ue, approvata la clausola di salvaguardia nazionale", ottobre 2026: https://quifinanza.it/politica/ok-ue-clausola-di-salvaguardia-cosa-cambia/1018849/amp/
- [S28] Pagella Politica, "Il programma del centrodestra per le elezioni 2022": https://pagellapolitica.it/articoli/programma-centrodestra-elezioni-2022; Il Foglio, "Ecco i 15 punti del programma elettorale del centrodestra", 11/8/2022: https://www.ilfoglio.it/politica/2022/08/11/news/ecco-i-15-punti-del-programma-elettorale-del-centrodestra--156629; Orizzonte Scuola, programma scuola del centrodestra 2022: https://www.orizzontescuola.it/piano-straordinario-per-assunzioni-dei-precari-piu-formazione-per-i-docenti-ecco-il-programma-per-la-scuola-del-centrodestra-scarica-pdf/
- [S29] Money.it, "Noi Moderati: il programma elettorale 2022": https://www.money.it/noi-moderati-programma-elettorale-elezioni-politiche-2022
- [S30] Orizzonte Scuola, "Legge di bilancio, Lupi: sulle paritarie un passaggio storico", dicembre 2025: https://www.orizzontescuola.it/legge-di-bilancio-lupi-sulle-paritarie-un-passaggio-storico-il-si-convinto-di-noi-moderati-alla-manovra-2026/
- [S33] Eunews, "Via libera Ue alla direttiva anti-corruzione", 26/3/2026: https://www.eunews.it/2026/03/26/via-libera-ue-alla-direttiva-anti-corruzione-in-italia-e-polemica-sulla-non-reintroduzione-dellabuso-dufficio/
- [S34] Pagella Politica, "La cancellazione del reato di abuso d'ufficio non è incostituzionale": https://pagellapolitica.it/articoli/abrogazione-reato-abuso-ufficio-costituzionale; Il Post, "Un primo voto per cancellare l'abuso d'ufficio", 10/1/2024: https://www.ilpost.it/2024/01/10/abuso-dufficio-voto-commissione-giustizia/; Pagella Politica, "Calenda non la dice tutta sull'abolizione del reato di abuso d'ufficio": https://pagellapolitica.it/articoli/calenda-abolizione-reato-abuso-ufficio
- [S35] ASMEL, riepilogo delle proposte sul correttivo del Codice dei contratti, ottobre 2024: https://asmel.eu/downloads/category_100/1_428.pdf
- [S36] Protiviti, Osservatorio Government, ottobre 2026 (relazione ANAC 2025): https://www.protiviti.com/sites/default/files/2026-10/osservatorio_government_ottobre_2026.pdf
- [S37] Teleborsa, "PA, da premi selettivi a carriere: cosa cambia", 1/7/2026: https://www.teleborsa.it/News/2026/07/01/pa-da-premi-selettivi-a-carriere-cosa-cambia-7.html; Sky TG24, "Via libera al ddl su merito e carriere", 28/1/2026: https://tg24.sky.it/politica/2026/01/28/pubblica-amministrazione-merito-carriere-zangrillo-ddl
- [S38] Lentepubblica, "Il decreto PA 2025 è legge": https://lentepubblica.it/personale-e-previdenza/il-decreto-pa-2025-e-legge-ecco-tutte-le-novita/
- [S42] Open, "Cosa prevede la riforma Bernini sulla ricerca", 8/8/2024: https://www.open.online/2024/08/08/cosa-prevede-riforma-bernini-ricerca-polemiche-precariato/
- [S43] Agenzia Nova, "Tajani: quella costituzionale è una buona riforma": https://www.agenzianova.com/news/tajani-quella-costituzionale-e-una-buona-riforma/
- [S44] Avvenire, "Spesa militare al 5% del Pil? All'Italia costerebbe 400 miliardi in 10 anni", 2025: https://www.avvenire.it/attualita/spesa-militare-al-5-del-pil-allitalia-costerebbe-400-miliardi-in-10-anni_93071
- [S45] Finanza.com, "Quanto spende l'Italia per la difesa e i nuovi obiettivi NATO": https://www.finanza.com/finanza/dati-bilancio-italia/italia-spesa-difesa-obiettivi-nato
- [S46] LaPresse, "Security decree, Lupi...", 21/4/2026: https://uk.lapresse.it/politics-en/2026/04/21/security-decree-lupi-the-issue-regarding-lawyers-will-be-resolved
- [S47] Il Fatto Quotidiano, "Direttiva anticorruzione, abuso d'ufficio: rischio infrazione", 26/3/2026: https://www.ilfattoquotidiano.it/2026/03/26/direttiva-anticorruzione-abuso-ufficio-rischio-infrazione-notizie/8337424/
