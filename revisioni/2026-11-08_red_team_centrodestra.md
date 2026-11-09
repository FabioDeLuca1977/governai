# Red team di area centrodestra (liberal-conservatrice)

*8 novembre 2026. Lettura di parte, dichiarata come tale. Legenda: [Fatto] = verificato nei documenti, con file; [Valutazione] = lettura dell'area; [Ipotesi] = congettura da verificare. Non sono stati letti gli altri pareri in `revisioni/`.*

## Giudizio in 5 righe

GovernAI è serio, onesto sui propri limiti e rigoroso sui conti: questo un elettore di centrodestra lo rispetta.
Ma la Carta e le coperture hanno un'inclinazione: casa, eredità, affitti, autotrasporto e agricoltura pagano; nessuna misura riduce le tasse.
La Difesa al 3,5% è classificata "sfavorevole" e la sicurezza è definita soprattutto come limite al controllo.
Il metodo è una garanzia formale, ma i valutatori sono tutti AI e l'opposizione non può proporre alternative.
Con cinque correzioni mirate il programma diventerebbe discutibile, e in parte votabile, anche a destra.

| Voto (1-10) | | Motivazione in una riga |
|---|---|---|
| Utilità | **7** | Bilancio generazionale, conti senza deficit e niente spesa non coperta sono strumenti che servono a chiunque governi. |
| Credibilità | **6** | Conti prudenti e limiti dichiarati; ma molti gettiti sono "stime GovernAI" e alcune misure sono politicamente irrealizzabili. |
| Neutralità percepita | **4** | Le coperture strutturali colpiscono quasi solo il blocco sociale del centrodestra; le parole della Carta sono quelle del centrosinistra riformista. |
| Idee | **5** | Ottime su semplificazione, giustizia e PA; deboli o respinte su fisco, famiglia, casa, Difesa e immigrazione. |

---

## 1. Prima impressione: neutrale, vicino o ostile?

[Valutazione] La prima reazione sarebbe di **sospetto educato**: "è il programma di un tecnocrate prudente di centrosinistra, con una buona contabilità". Non ostile nei toni, ma vicino a un'altra area nelle scelte. Gli esempi che un dirigente di centrodestra noterebbe subito:

- [Fatto] Il programma non riduce le aliquote legali. Il benchmark lo dice in chiaro: "GovernAI non riduce le aliquote legali" (`benchmark/programmi/fisco_conti.csv`, riga su +Europa) e classifica come "divergenti" la flat tax per le partite IVA, la riduzione del secondo scaglione IRPEF e l'abolizione dell'imposta di successione (stesso file).
- [Fatto] Le coperture strutturali del programma completo (circa 5,3 mld) "le pagano soprattutto proprietarie e proprietari di case di valore alto, locatori a canone libero, eredi di patrimoni oltre 500.000 €..., autotrasporto e agricoltura" (`20_programma_governai.md`, §6.3).
- [Fatto] La Difesa al 3,5% è "Sfav. · linea rossa" nella tabella delle misure (`20_programma_governai.md`, §3), anche se il testo precisa che è un giudizio sul costo e non sulla sicurezza (§6.1).
- [Fatto] Il governo ombra, nella prima seduta, ha messo **al primo posto** tra le spese fiscali da tagliare le successioni (SF14), la prima casa di pregio (SF12) e la cedolare a canone libero (SF11 e SF01) (`governo/verbali/2026-11-08-1-conti-in-ordine.md`, "Risposta del Consiglio").
- [Fatto] Sul Ponte sullo Stretto GovernAI è "divergente" rispetto alla maggioranza (`benchmark/programmi/ambiente_territori_europa.csv`).

[Valutazione] A favore della neutralità pesano invece cose vere: nessun deficit, nessuna nuova "quota" pensionistica ma anche nessuna patrimoniale generale, il salario minimo sul contratto più rappresentativo (lo stesso criterio del DL 62/2026, `benchmark/confronto_programmi.md`), il rifiuto del deficit per la Difesa coerente con l'art. 81. Il tono è sobrio e il sito dichiara i limiti (stime non certificate, simulazione). Questa onestà è il miglior capitale del progetto.

## 2. La Carta dei valori

**Che cosa l'area condivide** [Valutazione]
- **Responsabilità verso il futuro (FUT)** con l'art. 81 come linea rossa: è il linguaggio del rigore di bilancio e della demografia. Bene che il tasso di fecondità sia un indicatore.
- **Cittadinanza responsabile (CIT)**: "Lo Stato dà strumenti e fiducia, non tutela paternalistica. In cambio chiede reciprocità" (`01_carta_valori.md`). È quasi una definizione di sussidiarietà e di patto doveri-diritti.
- **Fiducia (FID)**: legalità, regole stabili, meno decreti e proroghe. Condiviso.
- **Bellezza, patrimonio e accoglienza (BPA)**: il *made in Italy* "come espressione di identità". Unico punto in cui la parola identità compare.
- La linea rossa contro la sorveglianza di massa e i punteggi sociali: l'area liberale la condivide, soprattutto verso il fisco.

**Che cosa sembra sbilanciato** [Valutazione]
- **Equità (EQU)** chiede che "chi ha di più contribuisca in proporzione" e ha come linea rossa lo spostamento dei costi sulle persone con redditi bassi o in condizioni di fragilità. Manca la linea rossa simmetrica: **nessun aumento della pressione fiscale complessiva** sul ceto medio che già paga. Così ogni copertura "progressiva" passa, ogni riduzione di tasse fatica.
- **Sicurezza "senza controllo assoluto" (SIC)**: già il nome mette l'accento sul limite e non sul diritto a vivere sicuri. Gli indicatori sono giusti, ma le domande sono quasi tutte sulle garanzie. L'area la chiamerebbe "Sicurezza e legalità", con le garanzie dentro la definizione.
- **Rispetto e diversità (RIS)** è largo: contiene diritti, diversità, ambiente "come casa comune", autonomie locali. Un valore che contiene tutto pesa molto nel motore.

**Che cosa manca** [Valutazione]
- **Famiglia** come valore o almeno come domanda esplicita: oggi è solo un indicatore demografico in FUT.
- **Libertà economica e proprietà**: nessun valore premia una riduzione del carico fiscale in sé, né la tutela del risparmio e della casa. Una misura di riduzione delle tasse può guadagnare punti solo indirettamente, via Innovazione o Benessere.
- **Merito**: compare nei testi della PA (09-C6), non nella Carta.
- **Sovranità e interesse nazionale dentro l'UE**: la Carta è silenziosa; il programma invece propone capacità fiscale UE (08-P4) e preferenza europea nella Difesa.

**Parole che suonano "di parte"** [Valutazione]: "casa comune", "dividendo climatico", "sussidi ambientalmente dannosi" (per l'autotrasportatore è un rimborso, non un sussidio), "chi non ha voce né rappresentanza", "sicurezza senza controllo assoluto". Non sono sbagliate, ma sono il lessico di un'area.

[Valutazione] Il punto metodologico chiave: il motore SMAA prova "tutte le combinazioni di pesi" (`01_carta_valori.md`, regola 3), ma **non prova insiemi diversi di valori**. Se tre dei dieci valori (EQU, RIS, FUT) premiano la redistribuzione e l'ambiente e nessuno premia la libertà economica, la neutralità sui pesi non corregge l'inclinazione della lista.

## 3. Le proposte

### Le 5 che l'area sosterrebbe

1. **01-P7 Dichiarazione zero.** Lo Stato fa il conto, il cittadino controlla: meno commercialisti, meno carte, meno errori. È semplificazione amica del contribuente (`programma/schede/10_fisco_semplice.md`).
2. **01-P4 Crescere conviene.** Tre anni per adeguarsi oltre i 15 e i 50 addetti e un premio a chi cresce o si fonde: è un tema storico delle PMI (`programma/schede/01_economia.md`). Da rafforzare, non da tenere in variante "Zero" come oggi (`20_programma_governai.md`, §3).
3. **07-C1 Giustizia a regime.** Processi più rapidi sono certezza del diritto per imprese e cittadine e cittadini. Bene che sia nel nucleo robusto.
4. **09-C6 Lavoro pubblico misurato e giusto** (con 09-C8). Indicatori di servizio, valutazione vera, responsabilità: è il merito nella PA (`programma/schede/12_pa_produttiva.md`).
5. **07-C4 Dal bene confiscato al bene comune.** Legalità concreta contro le mafie, misurabile (19.414 immobili ancora in gestione ANBSC, `programma/schede/07_giustizia.md`).

Accettabili anche: 03-P4 (prevenzione e assicurazione catastrofale, purché i premi non diventino una tassa sulla casa), 02-C5 (disabilità), 04-P4 (valutazione delle grandi opere, se non diventa un veto travestito), 01-P1 (bilancio generazionale).

### Le 5 che l'area contesterebbe di più

1. **07-C5 Difesa.** [Fatto] Classificata sfavorevole; la variante "Zero" stabilizza al ~2,1% e "non rispetta l'impegno NATO" (`programma/schede/07_giustizia.md`). [Valutazione] Per l'area la Difesa è una precondizione, non una politica tra le altre. Metterla in concorrenza con nidi e treni regionali è un errore di categoria. La scelta di presentare tre opzioni senza raccomandazione è corretta; la classe "Sfav." in tabella no.
2. **01-P8 Meno scontrini, con FN01 e FN03.** [Fatto] Abolisce la detrazione per le spese di istruzione e quella degli interessi sui nuovi mutui prima casa (`programma/schede/10_fisco_semplice.md`). [Valutazione] Colpisce le famiglie che scelgono la scuola paritaria e le giovani coppie che comprano casa: due bandiere dell'area. La compensazione AUU per ISEE bassi non tocca il ceto medio che paga.
3. **07-C2 Pena utile.** [Fatto] Valutazione d'ufficio delle misure alternative per pene residue fino a 2 anni (esclusi i reati 4-bis). [Valutazione] Sarà letta come "svuotacarceri". L'area risponde al sovraffollamento con più posti e con l'espulsione delle persone detenute straniere dove possibile (20.856 persone straniere detenute, stesso file). Accetterebbe la parte su lavoro e recidiva.
4. **04-P5 Autonomia differenziata reversibile.** [Fatto] Nessuna intesa su materie LEP prima della loro quantificazione e finanziamento; voto parlamentare vincolante e clausola di rientro (`programma/schede/04_infrastrutture.md`). [Valutazione] Per una parte dell'area (soprattutto al Nord) è un modo elegante di fermare la riforma.
5. **08-P4 Capacità fiscale UE.** [Valutazione] Tasse europee e debito comune strutturale toccano la sovranità di bilancio. L'area accetta acquisti comuni per la Difesa, non un bilancio federale.

Da correggere, più che respingere:
- **02-C2 Nido e congedo paterno**: l'area vuole libertà di scelta delle famiglie (trasferimento o servizio), non un congedo paterno "non trasferibile" imposto. [Fatto] La copertura originaria sopprimeva la decontribuzione delle lavoratrici madri; il governo ombra l'ha tolta su obiezione dell'opposizione (`governo/verbali/2026-11-08-1-conti-in-ordine.md`). Bene, ma il segnale iniziale resta.
- **07-C3 Flussi migratori**: la cornice è ragionevole e il KPI sui rimpatri (dal 22% al 35%) è condivisibile. Ma gli strumenti sono quasi solo integrazione (SAI al posto dei CAS, italiano per tutti, tutori). Mancano trattenimento, procedure di frontiera, accordi con i Paesi terzi come leva principale.
- **01-P10 Controlli mirati**: usa l'Archivio dei rapporti finanziari. Le garanzie ci sono, ma l'elettore autonomo lo leggerà come "il fisco guarda nel conto".

### Dove il programma è ingenuo [Valutazione]

- **Abolire la cedolare a canone libero (SF11)** riporta affitti in nero e toglie case dal mercato. Il gettito di 0,6-1,1 mld (`programma/coperture_menu.csv`) è statico. [Ipotesi] L'effetto di comportamento può ridurlo molto.
- **IMU sulla prima casa di valore alto e revisione degli estimi (SF13)**: politicamente è la misura più tossica d'Italia. Il benchmark stesso cita come idea "catasto con invarianza sulla prima casa".
- **Asilo in 6 mesi e quote motivate da un Osservatorio al CNEL**: l'Osservatorio sposta la scelta politica verso un tecnico.
- **Tassare il gasolio agricolo e dell'autotrasporto** in un Paese di piccole aziende e padroncini, mentre l'inflazione è al 5,6% (dato usato nel verbale), apre un fronte sociale.

## 4. Coperture: chi paga

[Fatto] Coperture nuove: 5,77 mld nel base, 11,02 nel completo (`20_programma_governai.md`, §4). Nel completo le voci aggiuntive sono: rimborso gasolio (SAD13, 0,8-1,1), estimi e IMU prima casa alta (SF13, 0,8-1,5), cedolare libera abolita (SF11, 0,6-1,1), successioni (SF14, 0,4-0,8), IVA sulle case nuove non prima casa (SAD14, 0,4-0,9), IVA gas domestico al 22% (SAD12, 0,25-0,32), detrazioni istruzione e mutui (FN01, FN03) (`programma/coperture_menu.csv`).

[Valutazione] Il giudizio dell'area è netto: **la distribuzione dei sacrifici ricade sul mattone, sul risparmio familiare e sul lavoro autonomo**. Quasi metà del gettito strutturale aggiuntivo viene dalla casa (SF13, SF11, SF12, SAD14, FN03). Il ceto medio proprietario, che in Italia è maggioranza, è il pagatore principale. Il programma lo fa con onestà, presentandola come "la scelta più politica" (§6.3): è un merito di trasparenza, non di neutralità.

Su alcune voci l'area è d'accordo:
- tagli alle consulenze, agli affitti passivi della PA, agli incentivi senza effetto dimostrato (RA01-RA04, RA14);
- revisione della spesa dei ministeri (RA13);
- perequazione ridotta solo sulla quota di pensione oltre 6 volte il minimo (PE04): accettabile, purché non si cumuli con il contributo sulle pensioni alte;
- le accise sul tabacco (AS01): non entusiasma, ma non è una battaglia.

Che cosa proporrebbe al posto [Valutazione, cifre da stimare]:
1. **Spesa prima delle entrate**: portare RA13 e RA14 al livello alto della forbice, aggiungere una revisione delle società partecipate locali e la vendita o valorizzazione del patrimonio immobiliare pubblico non usato (una tantum, quindi solo per investimenti o debito). [Ipotesi] Gettito da stimare con la RGS.
2. **Nessuna voce sulla casa di abitazione, sulle successioni in linea diretta e sulla cedolare**: sono linee rosse politiche dell'area. Il catasto si può aggiornare solo a invarianza di gettito sulla prima casa.
3. **Riordino delle spese fiscali sì, ma mirato alle agevolazioni d'impresa senza effetto e ai regimi di nicchia**, non alle detrazioni delle famiglie.
4. **Sussidi ambientali**: gradualità più lunga e restituzione automatica e integrale alle categorie colpite (autotrasporto, agricoltura), non al fondo generale.
5. **Una regola di "pressione fiscale non crescente"**: ogni nuova entrata strutturale finanzia anche una riduzione dell'IRPEF sul ceto medio, almeno in parte.

## 5. Il metodo: garanzia o rischio?

[Fatto] I tre valutatori sono agenti AI "indipendenti da chi ha scritto le proposte ma non da chi ha progettato il sistema", e l'accordo alto dipende "anche dai molti punteggi a zero" (`20_programma_governai.md`, §2). L'opposizione leale non può "proporre misure proprie fuori dal programma" (`governo/regolamento.md`). Nel verbale, le obiezioni dell'opposizione riguardano quasi solo il rigore delle coperture, non la direzione politica (`governo/verbali/2026-11-08-1-conti-in-ordine.md`).

[Valutazione] L'area vede **una garanzia formale e un rischio sostanziale**:
- Garanzia: tracciabilità, coperture contate al minimo, nessun recupero di evasione usato come copertura, verbali pubblici. Chiunque può controllare. È più di quanto fanno molti governi.
- Rischio 1, **tecnocrazia**: il "nucleo robusto" si presenta come ciò che è buono "qualunque sia il peso". Ma dipende dalla lista dei valori, dalla rubrica e dagli autori delle proposte. Chiamarlo "robusto" lo sottrae al dibattito.
- Rischio 2, **opposizione addomesticata**: un'opposizione che non può proporre è un revisore dei conti, non un'opposizione politica. Nessuno porta mai al tavolo una riduzione delle tasse o una linea di contenimento migratorio.
- Rischio 3, **modelli linguistici**: [Ipotesi] i modelli AI addestrati su testi pubblici possono avere un'inclinazione culturale media che non è quella dell'elettore di centrodestra. Va misurata, non presunta.

Per fidarsi servirebbero:
1. un panel umano plurale (almeno un valutatore per grande area) affiancato agli agenti, con confronto pubblico dei punteggi;
2. un'opposizione che può portare **alternative intere**, finanziate con le stesse regole;
3. un test di "inversione": riscrivere la Carta con valori di area diversa e mostrare quanto cambia il nucleo robusto;
4. la certificazione RGS o UPB dei gettiti principali prima di usarli.

## 6. Che cosa l'area potrebbe prendere

[Valutazione] Molto, sul metodo e sulla macchina dello Stato:
- **bilancio generazionale (01-P1) e spese fiscali a scadenza (01-P2)**: disciplina di bilancio che un governo di centrodestra può rivendicare;
- **dichiarazione zero (01-P7) e precompilata per le partite IVA (01-P12)**: semplificazione per il popolo delle partite IVA;
- **giustizia rapida (07-C1), merito nella PA (09-C6), tecnici per i piccoli Comuni (09-C3)**;
- **prevenzione del dissesto (03-P4)** e **valutazione delle opere (04-P4)**, purché decida comunque il Governo;
- la **regola "nessun deficit per la Difesa"** è difficile da accettare oggi, ma la **legge decennale con relazione alla Corte dei conti** è un buon impianto.

Le modifiche che renderebbero il programma accettabile senza perdere coerenza:
1. **Carta**: aggiungere "famiglia" e "libertà economica" alle domande di Benessere o Cittadinanza; rinominare SIC in "Sicurezza e legalità"; aggiungere la linea rossa "nessun aumento della pressione fiscale complessiva".
2. **Coperture**: togliere dal menu prima casa, successioni in linea diretta e cedolare; sostituirle con più revisione della spesa.
3. **Difesa**: togliere la classe "Sfav." e presentare la traiettoria al 2,5% come opzione pienamente legittima, con le coperture.
4. **Famiglia**: libertà di scelta tra nido e trasferimento; congedo paterno incentivato, non imposto.
5. **Immigrazione**: affiancare agli strumenti di integrazione quelli di controllo (frontiera, rimpatri, accordi), con gli stessi KPI.

## 7. Voti

| | Voto | Motivazione |
|---|---|---|
| Utilità | 7 | Strumenti di disciplina e trasparenza utili a qualsiasi maggioranza. |
| Credibilità | 6 | Conti prudenti e limiti dichiarati; gettiti non certificati e misure sulla casa politicamente irrealizzabili. |
| Neutralità percepita | 4 | Nessuna riduzione di tasse, coperture sul ceto medio proprietario, Difesa "sfavorevole", lessico di un'area. |
| Idee | 5 | Eccellenti su semplificazione, giustizia, PA; respinte su fisco, casa, famiglia, Difesa, migrazioni. |

*Testo rivisto il 9 novembre 2026 per un linguaggio inclusivo, senza cambiare il contenuto.*
