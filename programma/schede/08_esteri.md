# Schede pronte — Area 08: Esteri, Europa, Riforme istituzionali, Rapporti con il Parlamento

*Agente ministeriale 08 di GovernAI, 7 novembre 2026. Consigliere, non decisore. Varianti e coperture in `programma/varianti/08_esteri.csv`. Dati in `dati/serie/08_*.csv` e `dati/verifiche/08_esteri.md`. Importi in mld €/anno, salvo diversa indicazione. "Stima GovernAI" indica una stima senza equivalente ufficiale.*

**Regole di copertura rispettate.** Nessuna variante usa DEFICIT, RISPARMI_ATTESI, IVA_EVASIONE, ETS o ALTRO. Le spese permanenti sono coperte solo da fondi del menu (SAD, SPESE_FISCALI, RIALLOCAZIONE). COESIONE_2127 copre solo spesa triennale una tantum. Due misure nuove vanno segnalate all'agente coperture:
1. **contributo di solidarietà internazionale sui biglietti aerei**, fondo SAD, stima 0,4–0,8 mld, da verificare;
2. **taglio della spesa per consulenze e incarichi esterni dei ministeri**, fondo RIALLOCAZIONE, 0,02–0,04 mld.

| Proposta | Variante | Intensità | Costo a regime | Anno regime | Fondi |
|---|---|---|---|---|---|
| 08-P1 Consulenza algoritmica pubblica | PIENA | 1 | 0,035 | 2029 | RIALLOCAZIONE |
| | ESSENZIALE | 0,6 | 0,015 | 2029 | RIALLOCAZIONE |
| | PILOTA | 0,2 | 0,006 | 2028 | RIALLOCAZIONE |
| 08-P2 Patto per la buona legge | PIENA | 1 | 0,008 | 2028 | RIALLOCAZIONE |
| | ESSENZIALE | 0,5 | 0,002 | 2028 | RIALLOCAZIONE |
| | ZERO | 0,2 | 0 | 2027 | — |
| 08-P3 Votare dove si vive, regole stabili | PIENA | 1 | 0,025 | 2027 | RIALLOCAZIONE |
| | ESSENZIALE | 0,6 | 0,015 | 2027 | RIALLOCAZIONE |
| | ZERO | 0,3 | 0 | 2027 | — |
| 08-P4 Beni pubblici europei | PIENA | 1 | 0 | 2027 | — |
| | ESSENZIALE | 0,6 | 0 | 2027 | — |
| 08-P5 Cooperazione che si misura | PIENA | 1 | 4,5 | 2035 | SAD 2,5; SPESE_FISCALI 1,5; RIALLOCAZIONE 0,5 |
| | ESSENZIALE | 0,4 | 1,13 | 2031 | SAD 0,6; SPESE_FISCALI 0,33; RIALLOCAZIONE 0,2 |
| | ZERO | 0,15 | 0 | 2027 | — |
| 08-P6 Export resiliente | PIENA | 1 | 0,4 | 2029 | RIALLOCAZIONE 0,3; COESIONE_2127 0,1 |
| | ESSENZIALE | 0,45 | 0,15 | 2029 | RIALLOCAZIONE 0,08; COESIONE_2127 0,07 |
| | PILOTA | 0,1 | 0,03 | 2028 | RIALLOCAZIONE |

---

## 08-P1 — Legge sulla consulenza algoritmica pubblica

### Problema in un dato
Le regole europee sull'AI ora hanno date certe:
- il Reg. (UE) 2026/1744 (Digital Omnibus on AI) è in vigore dal 27 luglio 2026 e rinvia gli obblighi per i sistemi ad alto rischio al **2 dicembre 2027** (Allegato III) e al 2 agosto 2028 (Allegato I) (EUR-Lex; verifica 08, righe 21–22);
- in Italia sono in vigore la l. 132/2025 (dal 10 ottobre 2025) e il D.Lgs. 179/2026 (dal 23 ottobre 2026).

Eppure **nessuna norma disciplina l'uso dell'AI come consulente del processo legislativo e di governo**: chi la configura, con quali valori, con quale trasparenza e con quale responsabilità. Intanto la fiducia nelle istituzioni rappresentative è bassa. L'affluenza alle politiche 2022 è stata del **63,9%**, minimo storico (Ministero dell'Interno, Eligendo; verifica 08, riga 18).

### Soluzione in 3 righe
Una legge ordinaria istituisce presso le Camere un Ufficio indipendente, sul modello dell'UPB. L'Ufficio pubblica una Valutazione d'impatto pubblica (VIP-AI) degli atti principali, su sette valori e tre orizzonti di tempo. I pesi tra i valori li fissa un'Assemblea di cittadini sorteggiati. Il parere non è mai vincolante: il Governo che se ne discosta lo spiega in Parlamento (*comply or explain*). Il sistema è trattato volontariamente "come se" fosse ad alto rischio secondo l'AI Act.

### Varianti
- **PIENA** (intensità 1; 0,035 mld a regime nel 2029): Ufficio di circa 70 unità; VIP-AI obbligatoria sopra soglia e a richiesta di un quinto di una commissione; Assemblea di 150 persone; *comply or explain* su tutti gli atti valutati.
- **ESSENZIALE** (0,6; 0,015 mld): una sezione dentro l'UPB, VIP-AI solo sugli atti finanziari maggiori, Assemblea di 100 persone.
- **PILOTA** (0,2; 0,006 mld nel 2027–28): sperimentazione biennale sulla legge di bilancio 2028 e su 10 provvedimenti, poi valutazione indipendente.

**Copertura.** Riallocazione: taglio reale della spesa per consulenze esterne dei ministeri e risparmi di funzionamento nei bilanci interni delle Camere, senza aumentare la dotazione.

**Raccordo normativo.**
- *AI Act* (Reg. UE 2024/1689, come modificato dal Reg. UE 2026/1744): un sistema consultivo legislativo non rientra con certezza nell'Allegato III. La legge sceglie comunque la conformità volontaria agli obblighi per l'alto rischio:
  - gestione del rischio, governance dei dati, documentazione tecnica, registrazione degli eventi (*log*);
  - sorveglianza umana (art. 14) e trasparenza (art. 50);
  - valutazione d'impatto sui diritti fondamentali sul modello dell'art. 27;
  - adeguamento alle scadenze rinviate dal Reg. 2026/1744, anticipandole: a regime prima del 2 dicembre 2027.
- *Legge 132/2025*: rispetta il principio per cui l'AI nella PA è strumentale e di supporto, e decisione e responsabilità restano alla persona. Usa AgID e ACN come autorità nazionali per l'AI.
- *D.Lgs. 179/2026*: per i poteri di vigilanza delle autorità.
- *Altre fonti*: GDPR e Garante; CAD (d.lgs. 82/2005) per il codice aperto e il riuso.

### Articolato normativo essenziale
**Disegno di legge "Disciplina della consulenza algoritmica pubblica e dell'Assemblea dei cittadini sui valori"**

**Art. 1 (Finalità e principi).**
1. In attuazione degli articoli 1, 3, secondo comma, 95, 97 e 118, quarto comma, della Costituzione, la presente legge disciplina l'uso di sistemi di intelligenza artificiale a supporto della valutazione degli atti normativi. Ne assicura la trasparenza, la verificabilità, l'imparzialità e il controllo democratico.
2. I pareri resi ai sensi della presente legge non sono vincolanti. Non incidono sulla validità degli atti né sulle prerogative delle Camere, del Governo e dei loro componenti (artt. 67, 70, 77 e 95 Cost.). La decisione resta in ogni caso agli organi costituzionali, secondo il principio di sorveglianza umana di cui all'articolo 14 del regolamento (UE) 2024/1689 e all'articolo 14 della legge 23 settembre 2025, n. 132.
3. È vietato l'uso dei sistemi di cui alla presente legge per profilare persone fisiche, per valutare singoli parlamentari o elettori, o per finalità di propaganda.

**Art. 2 (Definizioni).** Ai fini della presente legge si intende per:
- a) "sistema di consulenza algoritmica pubblica" (SCAP): il sistema di IA, ai sensi dell'articolo 3 del regolamento (UE) 2024/1689, impiegato per produrre valutazioni d'impatto di atti normativi;
- b) "valutazione d'impatto pubblica" (VIP-AI): il documento di cui all'articolo 5;
- c) "matrice dei valori": i pesi relativi tra i valori di riferimento e il tasso di sconto intergenerazionale, fissati ai sensi dell'articolo 6;
- d) "Ufficio": l'Ufficio indipendente di valutazione algoritmica di cui all'articolo 3.

**Art. 3 (Ufficio indipendente di valutazione algoritmica).**
1. È istituito presso le Camere l'Ufficio indipendente di valutazione algoritmica, con autonomia funzionale e organizzativa.
2. L'Ufficio è retto da un Consiglio di tre membri. Sono nominati d'intesa dai Presidenti delle Camere, entro una rosa di dieci nomi indicata dalle Commissioni competenti a maggioranza dei due terzi. Il mandato è di sei anni e non è rinnovabile. I membri sono scelti tra persone di riconosciuta indipendenza e competenza in valutazione delle politiche pubbliche, informatica, diritto o statistica.
3. L'Ufficio si avvale di personale nel limite di settanta unità, reclutato con procedure pubbliche o in comando dalle amministrazioni, dall'ISTAT, dall'UPB e dalle università. Si avvale inoltre di convenzioni con enti di ricerca.
4. Per quanto non previsto, si applicano in quanto compatibili le disposizioni sull'Ufficio parlamentare di bilancio (legge 24 dicembre 2012, n. 243, Capo VII).

**Art. 4 (Requisiti del sistema).**
1. Il SCAP è sviluppato e gestito nel rispetto, su base volontaria, dei requisiti che il regolamento (UE) 2024/1689, come modificato dal regolamento (UE) 2026/1744, prevede per i sistemi ad alto rischio: gestione dei rischi, qualità e governance dei dati, documentazione tecnica, registrazione degli eventi, trasparenza, sorveglianza umana, accuratezza, robustezza e cibersicurezza.
2. Prima dell'entrata in esercizio, e poi a ogni modifica sostanziale, l'Ufficio effettua una valutazione d'impatto sui diritti fondamentali sul modello dell'articolo 27 del regolamento (UE) 2024/1689.
3. Sono pubblicati in formato aperto, ai sensi degli articoli 68 e 69 del decreto legislativo 7 marzo 2005, n. 82:
   - il codice;
   - le istruzioni di sistema (*prompt*);
   - la matrice dei valori;
   - le fonti dei dati;
   - il registro delle versioni del modello.
   Sono esclusi i soli elementi la cui diffusione pregiudica la sicurezza, secondo il parere dell'Agenzia per la cybersicurezza nazionale.
4. I dati e le elaborazioni sono trattati su infrastrutture soggette alla giurisdizione dell'Unione europea.
5. Ogni VIP-AI è sottoscritta da un funzionario responsabile, che ne verifica fonti e coerenza.

**Art. 5 (Valutazione d'impatto pubblica).**
1. La VIP-AI è obbligatoria per:
   - i disegni di legge del Governo, i decreti-legge e gli schemi di decreto legislativo con effetti finanziari superiori allo 0,1 per cento del prodotto interno lordo o che incidono su diritti fondamentali;
   - il disegno di legge di bilancio.
2. La VIP-AI è inoltre resa:
   - su richiesta di un quinto dei componenti di una Commissione permanente, su qualunque progetto di legge;
   - su richiesta della Conferenza delle Regioni, per le materie di legislazione concorrente.
3. La VIP-AI contiene:
   - a) l'effetto atteso su ciascuno dei valori della matrice, nel breve, medio e lungo periodo, con il grado di confidenza;
   - b) chi guadagna e chi perde, per reddito, territorio, età e genere;
   - c) l'analisi di sensitività ai pesi;
   - d) le fonti, le ipotesi e le incertezze.
   La VIP-AI non contiene raccomandazioni prescrittive.
4. La VIP-AI è pubblicata entro quindici giorni dalla trasmissione dell'atto alle Camere. Per i decreti-legge una versione sintetica è pubblicata entro cinque giorni. Il termine non sospende né condiziona l'iter parlamentare.
5. La VIP-AI integra l'analisi di impatto della regolamentazione di cui all'articolo 14 della legge 28 novembre 2005, n. 246, e non la sostituisce.

**Art. 6 (Assemblea dei cittadini sui valori).**
1. È istituita l'Assemblea dei cittadini sui valori. È composta da centocinquanta persone sorteggiate tra gli iscritti nelle liste elettorali, con campionamento stratificato per età, genere, territorio, titolo di studio e condizione occupazionale. Il sorteggio è certificato dall'ISTAT.
2. L'Assemblea resta in carica due anni e si rinnova per metà ogni anno. I componenti ricevono un'indennità giornaliera e il rimborso delle spese. Hanno diritto al permesso dal lavoro senza perdita della retribuzione.
3. Dopo audizioni pubbliche di esperti e di portatori di interessi, con materiali validati da un comitato scientifico pluralista, l'Assemblea delibera la matrice dei valori e il tasso di sconto intergenerazionale. La delibera vincola la configurazione predefinita del SCAP. Non vincola le Camere né il Governo.
4. I principi e i diritti costituzionali non sono oggetto di ponderazione.

**Art. 7 (Motivazione dello scostamento).**
1. Il Governo trasmette alle Commissioni competenti una relazione motivata, entro trenta giorni dall'approvazione definitiva, quando l'atto approvato presenta nella VIP-AI un effetto di lungo periodo negativo o peggiorativo rispetto al testo iniziale. Le Commissioni la esaminano in un'apposita seduta.
2. L'omissione della relazione è registrata e pubblicata dall'Ufficio. Non incide sulla validità o sull'efficacia dell'atto.

**Art. 8 (Vigilanza, audit e responsabilità).**
1. L'Ufficio sottopone il SCAP ogni anno a un audit indipendente e a prove di robustezza e di imparzialità (*red teaming*). Ne pubblica gli esiti e il registro degli errori corretti.
2. Restano ferme le competenze dell'Agenzia per l'Italia digitale e dell'Agenzia per la cybersicurezza nazionale, quali autorità nazionali per l'intelligenza artificiale ai sensi della legge 23 settembre 2025, n. 132, e del decreto legislativo 7 ottobre 2026, n. 179. Restano ferme anche le competenze del Garante per la protezione dei dati personali.
3. Le amministrazioni dello Stato che usano sistemi di IA per predisporre atti normativi ne danno comunicazione all'Ufficio e ne pubblicano le caratteristiche essenziali.

**Art. 9 (Periodo elettorale).** Nei quarantacinque giorni che precedono le elezioni politiche ed europee, l'Ufficio:
- sospende le VIP-AI su iniziativa;
- valuta, con lo stesso metodo, i programmi di tutte le liste che ne fanno richiesta;
- pubblica gli esiti contemporaneamente.

**Art. 10 (Sperimentazione, revisione e copertura finanziaria).**
1. Nel primo biennio di applicazione la VIP-AI è obbligatoria solo per il disegno di legge di bilancio e per i decreti-legge. Al termine, la Corte dei conti e un comitato accademico indipendente presentano alle Camere una valutazione.
2. La presente legge cessa di avere efficacia dopo cinque anni dall'entrata in vigore, salvo conferma con legge.
3. Agli oneri, pari a 12 milioni di euro per il 2027, 28 milioni per il 2028 e 35 milioni annui dal 2029, si provvede così:
   - per 20 milioni annui, mediante corrispondente riduzione degli stanziamenti per studi, consulenze e incarichi esterni dei Ministeri, secondo il decreto del Ministro dell'economia e delle finanze di cui al comma 4;
   - per la parte restante, nell'ambito dei bilanci interni delle Camere, senza incremento delle dotazioni.
4. Il decreto del Ministro dell'economia e delle finanze è adottato entro sessanta giorni.

### Cronoprogramma
| Fase | Chi | Cosa |
|---|---|---|
| Primi 100 giorni | Ministro per le Riforme istituzionali e Ministro per i Rapporti con il Parlamento | DDL in Consiglio dei ministri, dopo consultazione pubblica di 30 giorni; parere di AgID, ACN e Garante privacy; intesa preliminare con i Presidenti delle Camere sulla collocazione dell'Ufficio |
| Primi 100 giorni | MEF | Ricognizione della spesa per consulenze esterne dei ministeri e schema del decreto di riduzione |
| 12 mesi | Parlamento | Approvazione della legge; modifica dei regolamenti di Camera e Senato (art. 64 Cost.) per allegare la VIP-AI |
| 12 mesi | Presidenti delle Camere, ISTAT | Nomina del Consiglio; primo sorteggio dell'Assemblea; prima VIP-AI sul DDL di bilancio 2028, in sperimentazione |
| Fine legislatura | Ufficio, Corte dei conti | Messa a regime prima del 2 dicembre 2027 per i requisiti AI Act; valutazione del biennio; primo rapporto sulle relazioni motivate |

### Indicatori
| KPI | Base | Obiettivo a 3 anni | Obiettivo a 5 anni |
|---|---|---|---|
| Quota di atti obbligati con VIP-AI pubblicata nei termini | 0% (2026, nessuna norma) | ≥ 80% | ≥ 95% |
| Quota di scostamenti rilevanti con relazione motivata | 0% (2026) | ≥ 70% | ≥ 95% |
| Inviti al sorteggio accettati | n.d. (Ostbelgien e Irlanda come riferimento, valore non verificato) | ≥ 10% | ≥ 15% |
| Affluenza alle politiche (indicatore di contesto, non attribuibile alla sola misura) | 63,9% (2022, Eligendo) | — (elezioni 2027) | inversione del calo alle elezioni successive |

### Rischi e mitigazione
- **Tecnocrazia ("lo dice l'AI").** Parere non vincolante, divieto di linguaggio prescrittivo, sensitività ai pesi sempre pubblica.
- **Errori o bias del modello.** Audit annuale, *red teaming*, registro pubblico degli errori, firma di un funzionario responsabile.
- **Cattura politica.** Nomina a maggioranza dei due terzi, mandato unico di sei anni, collocazione presso le Camere e non presso Palazzo Chigi.
- **Conflitto con l'AI Act.** Conformità volontaria anticipata; eventuale classificazione futura come alto rischio già assorbita; nessuna funzione di influenza sul voto, grazie all'art. 9.
- **Ritualizzazione.** Clausola di scadenza a 5 anni e valutazione indipendente.
- **Dipendenza da fornitori extra UE.** Infrastruttura sotto giurisdizione UE; codice aperto; possibilità di cambiare modello.

---

## 08-P2 — Patto per la buona legge

### Problema in un dato
Il Governo in carica ha posto la questione di fiducia **91 volte** dall'inizio della XIX legislatura, in media **2,85 al mese**. È un dato Openpolis riportato dalla stampa ([La Notizia](https://www.lanotiziagiornale.it/?p=379119)), a data non certa e **non verificato su fonte primaria** (verifica 08, riga 17). Lo stesso articolo indica che 38 decreti-legge sono stati convertiti con doppia fiducia, alla Camera e al Senato. Per questa scheda non esiste una serie `08_*` verificata. **Primo atto**: far pubblicare il dato ufficiale dal Comitato per la legislazione.

### Soluzione in 3 righe
1. Al Governo si offre un **binario veloce con voto a data certa** per i suoi disegni di legge, così perde l'incentivo a usare il decreto-legge per avere tempi certi.
2. In cambio, gli emendamenti eterogenei in conversione diventano inammissibili, come chiede la Corte costituzionale (sent. 22/2012 e 32/2014).
3. Ogni legge costosa dichiara come e quando sarà valutata.

### Varianti
- **PIENA** (intensità 1; 0,008 mld dal 2028): legge ordinaria + regolamenti parlamentari + rafforzamento degli uffici studi.
- **ESSENZIALE** (0,5; 0,002 mld): solo regolamenti parlamentari e circolare del DAGL.
- **ZERO** (0,2; 0): protocollo Governo–Camere con monitoraggio trimestrale.

**Copertura**: riallocazione nei bilanci interni delle Camere e della PCM.

### Articolato normativo essenziale
**Disegno di legge "Disposizioni per la qualità della legislazione e la programmazione dei lavori parlamentari"**

**Art. 1 (Finalità).** La presente legge promuove la chiarezza, l'omogeneità e la valutabilità degli atti normativi e riconduce la decretazione d'urgenza ai casi straordinari di necessità e urgenza (art. 77 Cost.).

**Art. 2 (Omogeneità dei decreti-legge).**
1. Il decreto-legge contiene misure di immediata applicazione, di contenuto specifico, omogeneo e corrispondente al titolo, ai sensi dell'articolo 15 della legge 23 agosto 1988, n. 400.
2. Nella relazione illustrativa il Governo indica, per ciascun articolo, il presupposto di necessità e urgenza.
3. Il Governo si avvale dei disegni di legge con voto a data certa, di cui ai regolamenti parlamentari, per le misure che non presentano tali requisiti.

**Art. 3 (Clausola valutativa).**
1. Le leggi e i decreti legislativi con oneri superiori a 100 milioni di euro annui contengono una clausola valutativa. La clausola indica:
   - gli obiettivi misurabili;
   - gli indicatori e la fonte dei dati;
   - il soggetto valutatore;
   - la data di presentazione della valutazione alle Camere, non oltre il quinto anno.
2. La mancata presentazione della valutazione è segnalata nella relazione di cui all'articolo 4.

**Art. 4 (Relazione annuale sulla legislazione).** Entro il 31 marzo di ogni anno il Comitato per la legislazione e il Dipartimento per gli affari giuridici e legislativi pubblicano in formato aperto:
- il numero dei decreti-legge, delle questioni di fiducia e dei maxiemendamenti;
- i decreti attuativi pendenti;
- le valutazioni presentate e quelle omesse.

**Art. 5 (Applicazione).** Le disposizioni dell'articolo 2 si applicano dal primo giorno della legislatura successiva a quella in corso all'entrata in vigore della presente legge. Le altre disposizioni si applicano dall'entrata in vigore.

**Art. 6 (Copertura finanziaria).** Agli oneri, pari a 3 milioni di euro per il 2027 e a 8 milioni annui dal 2028, si provvede nell'ambito dei bilanci interni delle Camere e del bilancio della Presidenza del Consiglio dei ministri, mediante riallocazione delle risorse disponibili e senza nuovi o maggiori oneri per la finanza pubblica.

*Parallelamente, con modifiche ai regolamenti di Camera e Senato (art. 64 Cost.):*
- *voto finale a data certa entro 60–90 giorni per non più di un DDL governativo al mese;*
- *inammissibilità degli emendamenti estranei per materia, con criterio scritto e motivato;*
- *contingentamento per i decreti-legge che rinunciano alla fiducia.*

### Cronoprogramma
| Fase | Chi | Cosa |
|---|---|---|
| Primi 100 giorni | Ministro per i Rapporti con il Parlamento, DAGL | Protocollo Governo–Camere (variante ZERO, subito); primo report trimestrale; DDL in CdM |
| 12 mesi | Giunte per il regolamento di Camera e Senato | Modifiche regolamentari (binario veloce, inammissibilità); approvazione della legge |
| Fine legislatura | Comitato per la legislazione | Prima relazione annuale; clausole valutative in tutte le leggi sopra soglia; art. 2 pronto per la legislatura successiva (velo d'ignoranza) |

### Indicatori
| KPI | Base | Obiettivo a 3 anni | Obiettivo a 5 anni |
|---|---|---|---|
| Questioni di fiducia al mese | 2,85 (XIX leg., Openpolis via stampa, **non verificato**) | ≤ 2 | ≤ 1 |
| Quota di leggi sopra 100 mln con clausola valutativa attuata | n.d. (da misurare nella prima relazione, 2027) | ≥ 60% | ≥ 90% |
| Decreti attuativi pendenti oltre 12 mesi | n.d. (prima relazione) | −30% | −50% |

### Rischi e mitigazione
- **Elusione con decreti più piccoli e numerosi.** Monitoraggio trimestrale; omogeneità valutata anche sul numero di decreti.
- **Resistenza della maggioranza.** Applicazione dalla legislatura successiva (velo d'ignoranza); il binario veloce è un vantaggio per qualsiasi Governo.
- **Vere emergenze.** Deroga esplicita per calamità e sicurezza nazionale.

---

## 08-P3 — Votare dove si vive, regole che non cambiano a ridosso del voto *(ridefinita)*

### Problema in un dato
1. L'affluenza alle politiche 2022 è stata del **63,9%**, il minimo storico (Eligendo; verifica 08, riga 18).
2. La legge elettorale **l. 180/2026** è in vigore dal 24 ottobre 2026 e si applicherà alle politiche del 2027, quindi **entro 12 mesi dall'approvazione**, contro il Codice di buona condotta della Commissione di Venezia (2002). È la **quarta riforma in circa vent'anni**: l. 270/2005, l. 52/2015, l. 165/2017, l. 180/2026 (Normattiva; verifica 08, righe 19–20).

**Cosa cambia rispetto al dossier.** La formula elettorale è decisa e non viene rimessa in discussione: una nuova modifica ravvicinata violerebbe lo stesso principio di stabilità. Restano da fare due cose:
- (a) **far votare chi vive lontano dalla residenza**;
- (b) **impedire che si ripeta** il cambio delle regole a ridosso del voto.

### Soluzione in 3 righe
1. Voto fuorisede strutturale, per motivi di studio, lavoro e cura, nel comune di domicilio, superando le sperimentazioni caso per caso.
2. Una clausola di stabilità che vale solo per il futuro, quindi neutra rispetto ai rapporti di forza attuali.
3. Dopo ogni elezione, un rapporto pubblico su proporzionalità e rappresentanza.

### Varianti
- **PIENA** (intensità 1; 0,025 mld/anno): fuorisede per tutte le consultazioni, voto anticipato presidiato, clausola di stabilità con doppio consenso dei 3/5, rapporto post-elettorale.
- **ESSENZIALE** (0,6; 0,015 mld): fuorisede per consultazioni nazionali ed europee, clausola di stabilità, rapporto.
- **ZERO** (0,3; 0): solo clausola di stabilità, rapporto e simulazioni obbligatorie.

**Copertura**: capitolo spese elettorali del Ministero dell'Interno, con riallocazione.

### Articolato normativo essenziale
**Disegno di legge "Disposizioni per l'esercizio del voto nel luogo di domicilio e per la stabilità delle regole elettorali"**

**Art. 1 (Finalità).** In attuazione degli articoli 3, secondo comma, 48 e 51 della Costituzione, la presente legge:
- rende effettivo il diritto di voto degli elettori temporaneamente domiciliati, per motivi di studio, lavoro o cura, in un comune di altra provincia;
- garantisce la stabilità delle regole elettorali.

**Art. 2 (Voto nel comune di domicilio).**
1. Gli elettori di cui all'articolo 1 votano nel comune di domicilio temporaneo per le elezioni politiche, europee e per i referendum. Devono presentare domanda, anche in via telematica tramite l'Anagrafe nazionale della popolazione residente, entro il trentacinquesimo giorno precedente il voto.
2. Il voto è espresso in sezioni speciali istituite nei capoluoghi di provincia, per le liste della circoscrizione di iscrizione elettorale. Si applicano le garanzie di segretezza e di scrutinio previste per le sezioni ordinarie.

**Art. 3 (Voto anticipato presidiato).** *Solo variante PIENA.*
1. Nei dieci giorni precedenti la consultazione, gli elettori possono votare presso uffici comunali individuati con decreto del Ministro dell'interno, alla presenza di personale con funzioni di presidente di seggio e di rappresentanti di lista.
2. Le schede sono custodite in plichi sigillati e scrutinate con quelle del giorno di voto.

**Art. 4 (Stabilità delle regole elettorali).**
1. Le modifiche alle leggi elettorali di Camera e Senato che riguardano formula, soglie, premi, circoscrizioni o collegi non si applicano alle elezioni che si svolgono entro dodici mesi dalla loro entrata in vigore.
2. Le modifiche approvate in via definitiva da meno dei tre quinti dei componenti di ciascuna Camera si applicano a partire dalla seconda legislatura successiva. *Solo variante PIENA.*
3. Il presente articolo si applica alle leggi approvate dopo l'entrata in vigore della presente legge e non riguarda la legge 9 ottobre 2026, n. 180.

**Art. 5 (Trasparenza degli effetti).**
1. Ogni progetto di legge elettorale è accompagnato da simulazioni pubbliche su almeno tre scenari di voto.
2. Entro novanta giorni da ogni elezione politica, l'Ufficio di cui alla legge sulla consulenza algoritmica pubblica (08-P1), o in sua assenza l'ISTAT, pubblica:
   - l'indice di disproporzionalità;
   - la quota di voti non rappresentati;
   - la composizione degli eletti per genere, età e territorio.

**Art. 6 (Copertura finanziaria).** Agli oneri derivanti dagli articoli 2 e 3, valutati in 25 milioni di euro annui (15 milioni nella variante essenziale), si provvede mediante corrispondente riduzione delle dotazioni di parte corrente dello stato di previsione del Ministero dell'interno, missione "Relazioni finanziarie con le autonomie territoriali", esclusi i trasferimenti agli enti locali. *Programma da individuare con la RGS.*

### Cronoprogramma
| Fase | Chi | Cosa |
|---|---|---|
| Primi 100 giorni | Ministro per le Riforme, Ministero dell'Interno | DDL con un tavolo bipartisan: per applicarsi alle politiche 2027, il voto fuorisede richiede un consenso ampio. Non tocca gli elementi fondamentali, quindi è compatibile con la Commissione di Venezia (valutazione GovernAI). Verificare se e come la l. 180/2026 già disciplina il voto fuorisede. |
| 12 mesi | Interno, Comuni, ANPR | Sezioni speciali e domanda telematica operative per le politiche 2027; rapporto post-elettorale |
| Fine legislatura | Parlamento | Clausola di stabilità in vigore; avvio di una revisione costituzionale bipartisan per renderla stabile |

### Indicatori
| KPI | Base | Obiettivo a 3 anni | Obiettivo a 5 anni |
|---|---|---|---|
| Affluenza alle politiche | 63,9% (2022, Eligendo) | ≥ 64% (2027) | ≥ 66% (elezioni successive) |
| Elettori fuorisede che votano nel comune di domicilio | n.d. (sperimentazioni 2024–25, dato non verificato) | ≥ 300.000 (stima GovernAI) | ≥ 500.000 |
| Modifiche agli elementi fondamentali nei 12 mesi prima del voto | 1 (l. 180/2026) | 0 | 0 |

### Rischi e mitigazione
- **Accusa di voler bloccare la l. 180/2026.** Esclusione esplicita (art. 4, c. 3); applicazione solo futura.
- **Una legge ordinaria non vincola le maggioranze future.** Primo passo verso una revisione costituzionale; costo politico reso visibile dal rapporto.
- **Sicurezza e segretezza del voto anticipato.** Presidio fisico, nessun voto elettronico, plichi sigillati.
- **Tempi stretti prima del 2027.** La variante ESSENZIALE è la più realistica; il voto anticipato slitta alla tornata successiva.

---

## 08-P4 — Beni pubblici europei: capacità fiscale UE permanente e condizionata

### Problema in un dato
Sul solo bilancio pluriennale UE l'Italia è **contributore netto per 4,1 mld nel 2025** (−2,5 mld nel 2024). Con le sovvenzioni NGEU diventa **beneficiaria netta per 6,0 mld**. È un saldo semplificato (Commissione UE, *EU spending and revenue 2000–2025*; serie `08_saldo_it_bilancio_ue.csv`; calcolo GovernAI, non l'*operating budgetary balance* ufficiale). Con la fine del PNRR (2026) e l'inizio del rimborso NGEU (2028), il saldo con NGEU tende verso quello senza: **un'oscillazione di circa 10 mld/anno** in gioco nel negoziato QFP 2028–2034. La proposta è di 1.763,1 mld a prezzi 2025; quella della Presidenza cipriota di 1.730,2 mld (Consiglio UE, ST 10058/26).

### Soluzione in 3 righe
L'Italia negozia nuove risorse proprie UE come condizione per il rimborso NGEU, invece di difendere soltanto le quote nazionali. Propone un fondo per beni pubblici europei (difesa comune, reti, ricerca, adattamento) con condizionalità sullo stato di diritto. Il Parlamento controlla ogni anno il mandato negoziale.

### Varianti
- **PIENA** (intensità 1; costo nazionale 0): mandato negoziale, modifica della l. 234/2012 (sessione europea con VIP-AI), proposta SAFE come programmi comuni, clausole passerella.
- **ESSENZIALE** (0,6; 0): solo risoluzione parlamentare e coalizione negoziale.

Non si iscrive come copertura alcun beneficio atteso dal negoziato.

### Articolato normativo essenziale
**Disegno di legge "Modifiche alla legge 24 dicembre 2012, n. 234, per il controllo parlamentare dei negoziati sul bilancio dell'Unione"**

**Art. 1 (Finalità).** La presente legge rafforza la partecipazione delle Camere alla definizione della posizione italiana:
- sul quadro finanziario pluriennale dell'Unione europea;
- sulle risorse proprie;
- sugli strumenti di debito comune.

**Art. 2 (Mandato negoziale).**
1. Il Governo trasmette alle Camere una relazione sugli obiettivi negoziali:
   - prima di ogni Consiglio europeo che discute il quadro finanziario pluriennale o le risorse proprie;
   - prima di ogni nuovo strumento di debito comune.
2. La relazione indica, per ciascuna opzione, gli effetti stimati sul saldo netto dell'Italia, sul debito pubblico nazionale e sui beni pubblici europei finanziati. È accompagnata dalla valutazione d'impatto pubblica, ove istituita.
3. Le Camere possono adottare atti di indirizzo. Il Governo riferisce sugli esiti e motiva gli eventuali scostamenti.

**Art. 3 (Sessione europea annuale).** La sessione europea di cui all'articolo 13 della legge n. 234 del 2012 comprende un esame specifico:
- dei saldi finanziari dell'Italia con il bilancio dell'Unione;
- dello stato di attuazione degli strumenti di debito comune, incluso lo strumento SAFE.

**Art. 4 (Indirizzi per il negoziato).** Nel rispetto delle attribuzioni del Governo (art. 95 Cost.), la posizione italiana persegue in via prioritaria:
- l'introduzione di nuove risorse proprie che non gravino sui bilanci nazionali, per il rimborso del debito NGEU;
- il finanziamento a livello europeo di beni pubblici con valore aggiunto europeo, con vincolo di destinazione agli investimenti e condizionalità sullo stato di diritto;
- la trasformazione dei prestiti per la difesa in programmi comuni di acquisto e interoperabilità.

**Art. 5 (Clausola di invarianza finanziaria).** Dall'attuazione della presente legge non derivano nuovi o maggiori oneri per la finanza pubblica. Le amministrazioni interessate vi provvedono con le risorse disponibili a legislazione vigente.

### Cronoprogramma
| Fase | Chi | Cosa |
|---|---|---|
| Primi 100 giorni | Ministro per gli Affari europei, MAECI, MEF | Documento di posizione italiana sul *Negotiating Box* del giugno 2026; contatti di coalizione (FR, ES, PT, EL, BE e nordici su clima e ricerca); risoluzione parlamentare |
| 12 mesi | Governo nel Consiglio UE; Parlamento | Negoziato QFP nei Consigli europei; approvazione della legge; prima sessione europea rafforzata |
| Fine legislatura | Governo | Esito QFP (accordo atteso entro il 2027 per l'avvio nel 2028); revisione intermedia prevista nel 2031 |

### Indicatori
| KPI | Base | Obiettivo a 3 anni | Obiettivo a 5 anni |
|---|---|---|---|
| Saldo netto Italia sul solo QFP | −4,1 mld (2025, Commissione UE, calcolo GovernAI) | non peggiore di −4 mld | ≥ −3 mld |
| Quota del QFP 2028–34 finanziata da nuove risorse proprie | 0% del rimborso NGEU coperto da nuove risorse concordate (2026) | accordo su almeno 2 nuove risorse proprie | risorse in riscossione |
| Quota del prestito SAFE italiano trasformata in programmi comuni | 0 su "poco più di 8 mld" richiesti (ott. 2026) | ≥ 25% | ≥ 50% |

### Rischi e mitigazione
- **Veto dei Paesi frugali.** Insistere su risorse proprie che non pesano sui bilanci nazionali e accettare controlli rafforzati sulla spesa.
- **Spostamento di fondi da coesione e PAC.** Soglie minime per categoria nel mandato.
- **Percezione di cessione di sovranità.** Mandato parlamentare esplicito e trasparenza sui saldi.
- **Difesa che spiazza clima e coesione.** Vincolo di destinazione e soglie.

---

## 08-P5 — Cooperazione che si misura *(copertura riscritta)*

### Problema in un dato
- L'aiuto pubblico allo sviluppo (APS) italiano è lo **0,30% del RNL nel 2025** (6,46 mld € in equivalente dono, dati preliminari), contro l'obiettivo dello 0,7% richiamato dalla l. 125/2014.
- Di questo aiuto, **1,33 mld (18,5% dell'APS netto) sono costi per l'accoglienza dei rifugiati in Italia**, che non arrivano ai Paesi partner (OCSE DAC1, misure 11002 e 1820; serie `08_aps_ocse_dac.csv`).
- La media DAC è lo 0,26%, ma è scesa per i tagli degli altri donatori.

### Soluzione in 3 righe
1. Una traiettoria di legge dell'APS, graduale e coperta da una fonte dedicata: un contributo di solidarietà sui biglietti aerei, sul modello francese.
2. Contabilità separata dei costi di accoglienza.
3. Il 2% del budget destinato a valutazione indipendente, anche per il Piano Mattei.

### Varianti
- **PIENA** (intensità 1): 0,50% del RNL nel 2035, +0,02 punti l'anno. Costo +0,45 mld/anno cumulativi, **4,5 mld nel 2035** a RNL 2025 costante. Copertura: SAD 2,5; SPESE_FISCALI 1,5; RIALLOCAZIONE 0,5.
- **ESSENZIALE** (0,4): 0,35% nel 2031. Costo 0,23 / 0,45 / 0,68 mld nel 2027–29, **1,13 mld a regime**. Copertura: SAD 0,6, cioè il contributo di solidarietà sui biglietti aerei; SPESE_FISCALI 0,33; RIALLOCAZIONE 0,2.
- **ZERO** (0,15): non arretramento in valore nominale, contabilità separata, valutazione finanziata entro l'APS esistente.

**Perché la nuova copertura.**
- I proventi ETS (2,6 mld nel 2025) sono **interamente destinati per legge**: il fondo ETS ha capienza nulla e non è usato.
- Il contributo di solidarietà sui biglietti aerei è una **misura discrezionale di entrata** (DRM), quindi crea spazio sotto il tetto della spesa netta.
- Colpisce un settore che gode di sussidi ambientalmente dannosi: esenzione dell'accisa sul cherosene e IVA sui voli internazionali.
- Ha un precedente diretto: la *taxe de solidarité sur les billets d'avion* francese (2006), destinata allo sviluppo.
- **Gettito**: stima GovernAI di 0,4–0,8 mld. L'ordine di grandezza è circa 110 mln di passeggeri in partenza per un contributo medio di 4–7 €. Il dato va verificato con i dati Assaeroporti/ENAC dall'agente coperture.
- **Chi paga**: i passeggeri, in modo progressivo per classe e tratta, con aliquota alta per l'aviazione privata. Le tratte di continuità territoriale con le isole sono esentate.

### Articolato normativo essenziale
**Disegno di legge "Modifiche alla legge 11 agosto 2014, n. 125, e istituzione del contributo di solidarietà internazionale sul trasporto aereo"**

**Art. 1 (Finalità).** La presente legge stabilisce una traiettoria pluriennale dell'aiuto pubblico allo sviluppo, coerente con gli impegni internazionali dell'Italia e con la sostenibilità della finanza pubblica. Ne rafforza la trasparenza e la valutazione d'impatto.

**Art. 2 (Traiettoria dell'APS).**
1. Il documento triennale di programmazione di cui all'articolo 12 della legge n. 125 del 2014 assicura un rapporto tra APS e reddito nazionale lordo:
   - non inferiore allo 0,35 per cento entro il 2031;
   - *variante piena:* non inferiore allo 0,50 per cento entro il 2035, con un incremento minimo di 0,02 punti percentuali annui.
2. In caso di mancato rispetto, il Governo presenta alle Camere una relazione motivata con le misure correttive.

**Art. 3 (Contabilità separata).** I costi per l'accoglienza dei rifugiati e dei richiedenti asilo nel territorio nazionale, contabilizzati come APS secondo le regole OCSE-DAC:
- sono riportati separatamente nella relazione annuale;
- non concorrono al raggiungimento della traiettoria di cui all'articolo 2.

**Art. 4 (Valutazione indipendente).**
1. Una quota non inferiore al 2 per cento degli stanziamenti dell'Agenzia italiana per la cooperazione allo sviluppo è destinata alla valutazione e ai dati.
2. Ogni anno almeno il 10 per cento dei programmi è valutato con metodi controfattuali da soggetti indipendenti, e gli esiti sono pubblicati in formato aperto.
3. Le stesse disposizioni si applicano agli interventi del Piano Mattei.
4. Nessun finanziamento è destinato a forze di sicurezza di Paesi terzi in assenza di garanzie verificabili sul rispetto dei diritti umani.

**Art. 5 (Contributo di solidarietà internazionale).**
1. È istituito un contributo di solidarietà internazionale, dovuto dai passeggeri in partenza dagli aeroporti nazionali e riscosso dai vettori. Il contributo è graduato:
   - per destinazione: Unione europea / extra UE;
   - per classe di viaggio;
   - in misura maggiorata per l'aviazione d'affari e privata.
2. Sono esenti:
   - i voli in regime di continuità territoriale;
   - i passeggeri in transito;
   - i minori di due anni.
3. Le misure sono stabilite con decreto del Ministro dell'economia e delle finanze, di concerto con il Ministro degli affari esteri e della cooperazione internazionale, in modo da assicurare un gettito annuo non inferiore a 600 milioni di euro a regime.
4. Il gettito affluisce all'entrata del bilancio dello Stato ed è destinato agli stanziamenti di cui all'articolo 2.

**Art. 6 (Copertura finanziaria).** Agli oneri derivanti dall'articolo 2, pari a 230 milioni di euro per il 2027, 450 milioni per il 2028, 680 milioni per il 2029 e 1.130 milioni annui dal 2031, si provvede:
- a) mediante le maggiori entrate di cui all'articolo 5;
- b) per 330 milioni annui a regime, mediante la soppressione o la riduzione di spese fiscali individuate nell'allegato, nell'ambito del riordino di cui al menu delle coperture;
- c) per 200 milioni annui a regime, mediante riduzione degli stanziamenti di programmi di cooperazione e promozione con valutazione negativa, individuati con decreto del Ministro degli affari esteri e della cooperazione internazionale.

### Cronoprogramma
| Fase | Chi | Cosa |
|---|---|---|
| Primi 100 giorni | MAECI (Vice Ministro cooperazione), MEF | DDL; stima ufficiale del gettito del contributo con dati ENAC/Assaeroporti; avvio della contabilità separata nella relazione APS 2026 |
| 12 mesi | AICS, Comitato interministeriale per la cooperazione (CICS) | Documento triennale 2027–29 con la traiettoria; piano di valutazione; Piano Mattei agli stessi standard |
| Fine legislatura | AICS, valutatori indipendenti, OCSE-DAC | Prime valutazioni controfattuali pubblicate; APS ≥ 0,32% del RNL; *peer review* DAC |

### Indicatori
| KPI | Base | Obiettivo a 3 anni | Obiettivo a 5 anni |
|---|---|---|---|
| APS/RNL (equivalente dono) | 0,30% (2025, OCSE DAC1, prelim.) | 0,33% (ESS.) / 0,36% (PIENA) | 0,35% (ESS.) / 0,40% (PIENA) |
| Quota APS spesa per rifugiati in Italia | 18,5% dell'APS netto (2025, OCSE DAC1) | riportata a parte; ≤ 15% | ≤ 12% |
| Programmi con valutazione controfattuale pubblicata | n.d. (valutazione qualitativa: poche e non sistematiche) | 5% | 10% |

### Rischi e mitigazione
- **Effetto del contributo su turismo e connettività.** Importo contenuto, esenzione per la continuità territoriale, progressività per classe; monitoraggio dei flussi dopo 2 anni.
- **Capacità di spesa di AICS.** Crescita graduale; personale finanziato entro la quota del 2% e delle spese di funzionamento.
- **Aiuto usato come leva migratoria a scapito dei diritti umani.** Vincolo dell'art. 4, c. 4.
- **Reversibilità**, come nel caso del Regno Unito. Relazione motivata obbligatoria e fonte di gettito dedicata.
- **La variante PIENA dipende da coperture SAD contese.** L'ESSENZIALE è finanziata quasi interamente dalla fonte dedicata.

---

## 08-P6 — Export resiliente

### Problema in un dato
Nel 2025 i primi tre mercati (Germania 72,2 mld, Stati Uniti 69,6, Francia 65,0) assorbono il **32,2% dell'export italiano di beni** (643,2 mld). I mercati extra UE diversi dagli USA pesano il **37,8%**, contro il 38,7% del 2024 (Eurostat Comext DS-045409; serie `08_commercio_it_partner.csv`; calcolo GovernAI). Le importazioni dagli USA sono cresciute del 35,9% in un anno: sono riequilibri negoziati, non diversificazione.

### Soluzione in 3 righe
1. Voucher triennali alle PMI che entrano in mercati nuovi, con un piano di export.
2. Uno sportello unico digitale ICE–SACE–SIMEST.
3. Una valutazione d'impatto per settore e territorio di ogni accordo commerciale UE, con compensazioni mirate e temporanee invece di veti.

### Varianti
- **PIENA** (intensità 1; 0,4 mld nel 2029): voucher, sportello unico, supporto CBAM e due diligence, VIP-AI sugli accordi. Copertura: RIALLOCAZIONE 0,3 + COESIONE_2127 0,1 per le PMI del Mezzogiorno fino al 2029.
- **ESSENZIALE** (0,45; 0,15 mld): voucher solo per prime esportazioni extra UE + sportello unico.
- **PILOTA** (0,1; 0,03 mld): 3 mercati, circa 2.000 PMI, assegnazione in parte casuale per una valutazione controfattuale.

### Articolato normativo essenziale
**Articoli da inserire nel disegno di legge di bilancio 2028**

**Art. 1 (Finalità).** Al fine di ridurre la concentrazione geografica delle esportazioni e di sostenere l'ingresso delle piccole e medie imprese in nuovi mercati, è istituito per il triennio 2027–2029 il programma "Export resiliente".

**Art. 2 (Voucher per nuovi mercati).**
1. Alle PMI che presentano un piano di export almeno triennale verso mercati diversi dall'Unione europea e dagli Stati Uniti è concesso un voucher. Il voucher copre fino al 50% dei costi di ingresso (consulenza, certificazioni, fiere, temporary export manager), entro un massimale stabilito con decreto.
2. È data priorità alle imprese alla prima esportazione extra UE e a quelle con sede nelle regioni del Mezzogiorno.
3. Una quota dei voucher è assegnata con procedura in parte casuale tra domande ammissibili, al fine della valutazione d'impatto.

**Art. 3 (Sportello unico).** L'Agenzia ICE, SACE e SIMEST istituiscono, senza nuovi oneri, uno sportello unico digitale per i servizi di promozione, assicurazione e finanziamento all'export. Vi integrano il supporto agli obblighi derivanti dal meccanismo di adeguamento del carbonio alle frontiere (CBAM) e dalle norme UE su deforestazione e dovere di diligenza.

**Art. 4 (Valutazione degli accordi commerciali).**
1. Per ogni accordo commerciale dell'Unione europea sottoposto al Consiglio, il Governo trasmette alle Camere una valutazione degli effetti per settore e territorio, con le eventuali misure compensative temporanee e decrescenti.
2. La valutazione precede la definizione della posizione italiana.

**Art. 5 (Valutazione e copertura finanziaria).**
1. Il programma è valutato entro il 30 giugno 2030 con metodi controfattuali.
2. Agli oneri, pari a 150 milioni di euro per il 2027, 300 milioni per il 2028 e 400 milioni per il 2029, si provvede:
   - per 300 milioni annui a regime, mediante riduzione delle dotazioni del Fondo per la promozione integrata e della quota a fondo perduto delle risorse gestite da SIMEST, destinate a mercati e imprese già serviti;
   - per 100 milioni annui, a valere sulle risorse dei programmi FESR 2021–2027 non ancora selezionate, previa riprogrammazione approvata dalla Commissione europea, per le imprese delle regioni meno sviluppate.

### Cronoprogramma
| Fase | Chi | Cosa |
|---|---|---|
| Primi 100 giorni | MAECI (DG promozione), MIMIT, ICE | Disegno dei voucher e del protocollo di valutazione; avvio della riprogrammazione FESR con l'Agenzia per la coesione |
| 12 mesi | ICE, SACE, SIMEST | Primo bando; sportello unico operativo; prima VIP-AI su un accordo (es. Mercosur o India) |
| Fine legislatura | MAECI, valutatori indipendenti | Valutazione controfattuale; decisione su prosecuzione con copertura nuova o chiusura |

### Indicatori
| KPI | Base | Obiettivo a 3 anni | Obiettivo a 5 anni |
|---|---|---|---|
| Quota dell'export verso mercati extra UE diversi dagli USA | 37,8% (2025, Eurostat Comext) | 39% | 40% |
| Quota dei primi tre mercati (DE, US, FR) | 32,2% (2025, Eurostat Comext) | ≤ 31% | ≤ 30% |
| Esportazioni aggiuntive delle PMI con voucher rispetto al gruppo di controllo | n.d. (nessuna valutazione controfattuale esistente) | effetto stimato e pubblicato | effetto ≥ 2 € di export per 1 € pubblico, altrimenti chiusura |

### Rischi e mitigazione
- **Peso morto** (export che sarebbe avvenuto comunque). Priorità alla prima esportazione, assegnazione in parte casuale, valutazione controfattuale.
- **Conflitti con le filiere agricole sugli accordi.** Compensazioni temporanee e decrescenti, decise sulla base della VIP-AI.
- **Fine dei fondi di coesione nel 2029.** Programma triennale con clausola di valutazione; nessuna prosecuzione automatica.
- **Competenza UE esclusiva sul commercio** (art. 3 TFUE). La misura agisce solo su promozione nazionale e posizione nel Consiglio.
