# Schede pronte — Area 09 (Pubblica amministrazione, Digitale)

*Agente ministeriale 09 — 7 novembre 2026. Fonti: `ministeri/09_pa_digitale.md`, `dati/verifiche/09_pa_digitale.md`, serie `dati/serie/09_*.csv`. Varianti e coperture: `programma/varianti/09_pa_digitale.csv`. Importi in mld €/anno; "stima GovernAI" quando non esiste una stima ufficiale.*

## Quadro dell'area

| Proposta | Esito del panel (Carta 2.0) | PIENA | ESSENZIALE | PILOTA / ZERO |
|---|---|---|---|---|
| 09-C1 Stato a vetro | dipende dai valori | 0,07 (int. 1) | 0,035 (0,6) | PILOTA 0,012 (0,25) |
| 09-C2 Chiedilo una volta sola | dipende dai valori | 0,35 (1) | 0,14 (0,6) | ZERO 0 (0,3) |
| 09-C3 Squadre tecniche della Repubblica | **nucleo robusto** | 0,55 (1) | 0,22 (0,5) | PILOTA 0,04 (0,1) |
| 09-C4 Manutenzione digitale | in coda | 0,40 (1) | 0,12 (0,45) | ZERO 0 (0,15) |
| 09-C5 IA nella PA | **nucleo robusto** | 0,22 (1) | 0,08 (0,55) | ZERO 0 (0,3) |
| **Totale** | | **1,59** | **0,595** | |

**Regole rispettate.** Nessun prelievo da DEFICIT, RISPARMI_ATTESI, IVA_EVASIONE, ETS o ALTRO. I fondi usati sono due:
- **RIALLOCAZIONE** per tutta la spesa permanente: 1,02 mld nelle PIENE, 0,455 nelle ESSENZIALI;
- **COESIONE_2127** solo per investimenti una tantum 2027-29: 0,57 nelle PIENE, 0,14 nelle ESSENZIALI. Mai per il personale stabile.

**Doppio conteggio corretto.** Prima 09-C5 prelevava una "quota del fondo di 09-C4" (su ALTRO), cioè la stessa risorsa. Ora le due misure hanno coperture separate e nessuna usa i risparmi attesi del consolidamento: questi entrano solo dopo la certificazione, come riduzione della quota statale di C4.

**Coperture da proporre al menu (fondo RIALLOCAZIONE).** RIALLOCAZIONE è un fondo del menu: la sua capienza dipende dalle misure attivate. Propongo tre misure concrete, ognuna un taglio di spese che si sarebbero effettivamente fatte:

| Misura | Cosa si taglia | Gettito stimato | Chi paga |
|---|---|---|---|
| R09-1 Riserva di facoltà assunzionali | Una quota del turnover già autorizzato (Stato e enti aderenti) va al ruolo tecnico invece che a profili amministrativi generici | 0,18-0,45 (uso nelle PIENE: 0,45) | Chi si candida a profili generici; uffici che non sostituiscono il personale |
| R09-2 Consulenze esterne | Incarichi esterni, assistenza tecnica e studi d'impatto sostituiti dai pool (C3) e dall'infrastruttura pubblica (C1) | 0,05-0,2 (uso nelle PIENE: 0,17) | Società di consulenza |
| R09-3 Spesa ICT corrente | -4/6% della spesa ICT della PA (oltre 7 mld nel 2022, stima AgID; 5 mld nel 2025 sul solo panel rilevato): CED residui, hosting locale, licenze duplicate, acquisti via accordi quadro Consip | 0,28-0,42 (uso nelle PIENE: 0,40; nelle ESSENZIALI: 0,20) | Fornitori di hosting e licenze legacy |

Fonte del dato ICT: AgID, rilevazioni sulla spesa ICT nella PA (gennaio 2022 e maggio 2025, con il Politecnico di Milano); dato da aggiornare sul report integrale.

---

## 09-C1 — "Stato a vetro": infrastruttura pubblica aperta per l'analisi delle politiche

**Problema in un dato.** Nessuna AIR governativa è oggi accompagnata per obbligo da dati e codice riproducibili. Intanto la PA ha già costruito l'infrastruttura per scambiare dati: **oltre 14.000 e-service** e **oltre 9.400 enti** sulla PDND (DTD, 31.5.2026, serie `09_dtd_pdnd_psn_cloud`). I dati esistono e circolano tra enti, ma le analisi su cui si decide non sono pubbliche.

**Soluzione in 3 righe.**
1. Ogni atto del Governo sottoposto a valutazione d'impatto (VIP-AI, 08-P1) pubblica dati, codice e ipotesi in formato aperto; i microdati sensibili restano in ambienti sicuri ISTAT e Banca d'Italia.
2. I modelli pubblici di microsimulazione (RGS, Finanze, INPS) diventano software aperto su Developers Italia. Un registro unico traccia le analisi e gli algoritmi della PA: finalità, dati, versione, prompt, chi ha deciso.
3. **Raccordo con 08-P1.** C1 è il "lato Governo": produce e pubblica. L'Ufficio indipendente presso le Camere previsto da 08-P1 è il "lato controllo": verifica e fa audit. Lo strato di audit previsto nel dossier passa all'Ufficio, così non si paga due volte. **GovernAI gira su questa infrastruttura**: ogni suo parere è un'analisi iscritta nel registro.

| Variante | Contenuto | Costo a regime | Intensità | Fondo |
|---|---|---|---|---|
| PIENA | Tre strati (dati, modelli, registro) per tutti gli atti VIP-AI e tutti i sistemi IA della PA; circa 120-150 unità | 0,07 (dal 2029) | 1 | RIALLOCAZIONE (R09-2) |
| ESSENZIALE | Solo atti sopra soglia VIP-AI e sistemi IA che incidono su provvedimenti; modelli già esistenti | 0,035 | 0,6 | RIALLOCAZIONE |
| PILOTA | Tre aree (fisco, pensioni, clima) per 2 anni, con valutazione | 0,012 | 0,25 | RIALLOCAZIONE |

### Articolato normativo essenziale (disegno di legge "Disposizioni per la trasparenza delle analisi a supporto delle decisioni pubbliche")

**Art. 1 (Finalità).** 1. La presente legge assicura che le analisi, i dati e i modelli, compresi i sistemi di intelligenza artificiale, utilizzati dal Governo e dalle amministrazioni centrali per predisporre atti normativi e decisioni di rilevante impatto siano pubblici, riproducibili e verificabili, in attuazione degli articoli 97 e 118 della Costituzione, dell'articolo 14 della legge 23 settembre 2025, n. 132, e nel rispetto del Regolamento (UE) 2016/679.

**Art. 2 (Pubblicazione di dati e codice).** 1. All'articolo 14 della legge 28 novembre 2005, n. 246, dopo il comma 5 è inserito il seguente: «5-bis. L'analisi di impatto della regolamentazione degli atti sottoposti alla valutazione d'impatto pubblica di cui alla legge [08-P1] è corredata dai dati, dal codice di calcolo e dalle ipotesi utilizzati, pubblicati in formato aperto sul portale nazionale dei dati entro la data di trasmissione dell'atto alle Camere.» 2. I dati personali e i microdati soggetti a segreto statistico non sono pubblicati. Sono resi accessibili per finalità di verifica e di ricerca in ambienti sicuri gestiti dall'ISTAT e dalla Banca d'Italia, secondo le regole sentito il Garante per la protezione dei dati personali.

**Art. 3 (Modelli pubblici aperti).** 1. All'articolo 69 del decreto legislativo 7 marzo 2005, n. 82, è aggiunto il seguente comma: «2-ter. I modelli di microsimulazione e di previsione utilizzati dalle amministrazioni centrali per quantificare gli effetti finanziari e distributivi degli atti normativi sono rilasciati con licenza aperta, salvo le parti coperte da segreto statistico o di sicurezza nazionale individuate con decreto del Presidente del Consiglio dei ministri.»

**Art. 4 (Registro pubblico delle analisi e degli algoritmi).** 1. È istituito presso il Dipartimento per la trasformazione digitale il Registro pubblico delle analisi e degli algoritmi. Vi sono iscritti: a) le analisi di cui all'articolo 2; b) i sistemi di intelligenza artificiale utilizzati dalle pubbliche amministrazioni che incidono su provvedimenti; c) i pareri degli strumenti di consulenza algoritmica pubblica. 2. Per ogni iscrizione il Registro indica finalità, fonti dei dati, versione del modello, istruzioni di sistema, ipotesi, misure di incertezza e il soggetto umano che ha assunto la decisione. 3. Il Registro è consultabile dall'Ufficio di cui alla legge [08-P1], che ne verifica a campione la riproducibilità e riferisce annualmente alle Camere.

**Art. 5 (Attuazione).** 1. Entro dodici mesi un decreto del Presidente del Consiglio dei ministri, sentiti il Garante, l'ISTAT e l'AgID, fissa gli standard minimi di pubblicazione e i formati. 2. In sede di prima applicazione, gli obblighi si applicano per diciotto mesi agli atti in materia fiscale, previdenziale e climatica.

**Art. 6 (Copertura finanziaria).** 1. Agli oneri, pari a 40 milioni di euro per il 2027, 60 milioni per il 2028 e 70 milioni annui dal 2029, si provvede mediante corrispondente riduzione delle autorizzazioni di spesa per incarichi di consulenza, studio e ricerca delle amministrazioni centrali e degli stanziamenti per la realizzazione del Piano triennale per l'informatica, come individuati in apposito allegato.

### Cronoprogramma

| Fase | Chi | Cosa |
|---|---|---|
| Primi 100 giorni | Sottosegretario all'innovazione, DTD, DAGL | DDL in Consiglio dei ministri insieme a 08-P1; avvio del pilota (fisco, pensioni, clima) con RGS, Dipartimento Finanze, INPS e MASE; primo prototipo del registro su PSN |
| 12 mesi | Parlamento; DTD con ISTAT e Garante | Legge approvata; DPCM sugli standard; primi tre modelli aperti su Developers Italia; ambiente sicuro ISTAT per i microdati |
| Fine legislatura | Tutte le amministrazioni centrali; Ufficio 08-P1 | Obbligo esteso a tutti gli atti VIP-AI; registro con tutti i sistemi IA della PA; secondo rapporto di riproducibilità dell'Ufficio |

### Indicatori

| KPI | Base | Obiettivo a 3 anni | Obiettivo a 5 anni |
|---|---|---|---|
| Quota di atti VIP-AI con dati e codice pubblicati | 0% (2026: nessun obbligo vigente; dossier 09) | 60% | 90% |
| Quota di analisi del campione riprodotte dall'Ufficio 08-P1 | non misurata (2026) | ≥ 50% (sotto questa soglia si riprogetta) | ≥ 80% |
| Modelli pubblici di microsimulazione con licenza aperta | 0 tra quelli di RGS, Finanze e INPS (2026, dossier 09) | 3 | 6 |

### Rischi e mitigazione
- **Esposizione di dati personali** → mai microdati in chiaro; ambienti sicuri; parere preventivo del Garante.
- **Trasparenza di facciata**, cioè file pubblicati ma inutilizzabili → standard minimi nel DPCM; test di riproducibilità dell'Ufficio 08-P1 con soglia del 50%.
- **Pubblicare solo gli scenari favorevoli** → obbligo di registrare tutte le analisi eseguite, non solo quelle allegate.
- **Sovrapposizione con 08-P1** → divisione netta: C1 produce e pubblica, 08-P1 verifica. Nessuno dei due paga l'audit dell'altro.

---

## 09-C2 — "Chiedilo una volta sola": diritto esigibile all'once-only

**Problema in un dato.** Nel 2025 solo il **43,5%** dei 16-74enni ha interagito online con la PA, contro il **57,7%** della media UE (Eurostat, isoc_ciegi_ac, I_IUGOV1; serie `09_egov_uso_cittadini`). Eppure l'offerta di servizi digitali è sopra la media UE (86,1 contro 84,6; *State of the Digital Decade 2026*). La PDND ha oltre 14.000 e-service, ma la quota di procedimenti davvero "once only" non è misurata. Il problema non è l'infrastruttura, è il suo uso.

**Soluzione in 3 righe.**
1. Per i 100 procedimenti a maggior volume, un decreto fissa la data entro cui l'ente deve acquisire i dati via PDND invece di chiederli alle persone.
2. Dopo quella data, se l'ente chiede un dato che lo Stato già possiede, scatta un indennizzo forfettario: 30 € alla persona, 100 € all'impresa, pagati dall'ente inadempiente.
3. Un cruscotto pubblico mostra, ente per ente, i procedimenti once-only. Ogni persona può vedere chi ha consultato i suoi dati.

| Variante | Contenuto | Costo | Intensità | Fondi |
|---|---|---|---|---|
| PIENA | 100 procedimenti; supporto ai comuni con centri di competenza regionali | 0,35 al picco 2028 (0,3 coesione 2027-29 + 0,05 permanenti) | 1 | COESIONE_2127 0,30 (una tantum); RIALLOCAZIONE 0,05 (R09-3) |
| ESSENZIALE | 30 procedimenti (ISEE, prestazioni, anagrafe, iscrizioni scolastiche, SUAP, residenza); indennizzo dopo 24 mesi | 0,14 al picco (0,11 + 0,03) | 0,6 | COESIONE_2127 0,11; RIALLOCAZIONE 0,03 |
| ZERO | Solo il diritto e il cruscotto, senza fondi; indennizzo dopo 36 mesi | 0 | 0,3 | — |

Gli indennizzi non sono contati come costo per lo Stato: sono pagati dai bilanci degli enti inadempienti, che sono soggetti all'equilibrio di bilancio. Il primo anno c'è una franchigia e c'è un tetto annuo per ente. L'obiettivo è che tendano a zero.

### Articolato normativo essenziale (decreto legislativo, su delega per l'attuazione del Reg. UE 2024/903 e del CAD)

**Art. 1 (Finalità).** 1. Il presente decreto rende esigibile il diritto delle persone e delle imprese a non fornire alle pubbliche amministrazioni dati e documenti già in possesso di un'altra amministrazione. Dà attuazione all'articolo 43 del d.P.R. 28 dicembre 2000, n. 445, all'articolo 50-ter del d.lgs. 7 marzo 2005, n. 82, e al Regolamento (UE) 2024/903.

**Art. 2 (Procedimenti e calendario).** 1. Con decreto del Ministro per la pubblica amministrazione, d'intesa in Conferenza unificata, sono individuati i cento procedimenti a maggior volume. Per ciascuno sono fissati la data dalla quale i dati sono acquisiti esclusivamente tramite la Piattaforma digitale nazionale dati e l'amministrazione titolare del dato. 2. Le date sono comprese tra il dodicesimo e il trentaseiesimo mese dall'entrata in vigore del presente decreto.

**Art. 3 (Indennizzo once-only).** 1. Dopo la data di cui all'articolo 2, l'amministrazione che richiede un dato già disponibile tramite la Piattaforma corrisponde alla persona interessata, su istanza anche telematica, un indennizzo forfettario: 30 euro per le persone fisiche, 100 euro per le imprese, per ciascun procedimento. Si applica l'articolo 2-bis, comma 1-bis, della legge 7 agosto 1990, n. 241, in quanto compatibile. 2. L'indennizzo non è dovuto se il dato non è disponibile per inadempimento dell'amministrazione titolare: in quel caso è a carico di quest'ultima. 3. Per i primi dodici mesi da ciascuna data si applica una franchigia; l'importo complessivo annuo a carico di ciascun ente non supera lo 0,5 per cento delle sue spese correnti.

**Art. 4 (Trasparenza e diritti della persona interessata).** 1. Il Dipartimento per la trasformazione digitale pubblica un cruscotto, aggiornato ogni trimestre, con lo stato di attuazione per ciascun ente e gli indennizzi corrisposti. 2. Ogni persona interessata può consultare, tramite il punto di accesso telematico nazionale, l'elenco delle amministrazioni che hanno acquisito i suoi dati. La rettifica di un dato presso l'amministrazione titolare si propaga a tutte le amministrazioni che lo utilizzano.

**Art. 5 (Supporto agli enti).** 1. Le amministrazioni regionali, d'intesa con il Dipartimento per la trasformazione digitale, costituiscono centri di competenza per supportare gli enti locali nell'integrazione con la Piattaforma. Hanno priorità i comuni con meno di 5.000 abitanti.

**Art. 6 (Copertura finanziaria).** 1. Agli oneri di cui all'articolo 5, pari a 250 milioni per il 2027, 350 milioni per il 2028 e 300 milioni per il 2029, si provvede a valere sulle risorse dei programmi della politica di coesione 2021-2027, obiettivo strategico 1, previa riprogrammazione concordata con la Commissione europea. Agli oneri a regime, pari a 50 milioni annui dal 2028, si provvede mediante riduzione degli stanziamenti per spesa ICT corrente delle amministrazioni centrali. 2. Gli indennizzi di cui all'articolo 3 sono a carico dei bilanci delle amministrazioni inadempienti e non comportano nuovi o maggiori oneri per la finanza pubblica.

### Cronoprogramma

| Fase | Chi | Cosa |
|---|---|---|
| Primi 100 giorni | Ministro PA e DTD; Conferenza unificata | Delega nel primo DDL di semplificazione; elenco dei 100 procedimenti con i volumi annui; avvio della riprogrammazione della coesione con le Regioni |
| 12 mesi | DTD, AgID, centri di competenza regionali | Decreto legislativo in vigore; cruscotto online; primi 30 procedimenti once-only (ISEE, anagrafe, iscrizioni scolastiche) |
| Fine legislatura | Tutte le amministrazioni | 100 procedimenti once-only; indennizzi in calo; servizi "proattivi" (prestazioni erogate senza domanda) su almeno 5 prestazioni |

### Indicatori

| KPI | Base | Obiettivo a 3 anni | Obiettivo a 5 anni |
|---|---|---|---|
| 16-74enni che hanno interagito online con la PA | 43,5% (2025, Eurostat isoc_ciegi_ac) | 52% | 60% (media UE 2025: 57,7%) |
| Procedimenti dell'elenco con acquisizione esclusiva via PDND | non misurato (2026; DTD pubblica solo le adesioni) | 50 su 100 | 100 su 100 |
| Indennizzi pagati per 10.000 pratiche | 0 (diritto non vigente, 2026) | in calo per 4 trimestri consecutivi | meno della metà del primo anno di applicazione |

### Rischi e mitigazione
- **Indennizzi che drenano le risorse degli enti fragili** → franchigia, tetto dello 0,5% della spesa corrente, priorità ai centri di competenza e ai pool di C3. Revisione a 24 mesi: se gli indennizzi non calano si interviene sulla capacità degli enti, non si abolisce il diritto.
- **Sorveglianza e accentramento dei dati** → nessuna banca dati unica; scambi puntuali tracciati; ogni persona vede chi ha usato i suoi dati.
- **Errori che si propagano** → rettifica unica presso l'ente titolare del dato, propagata a tutti.
- **Coesione non riprogrammabile in tempo** → si ripiega sull'ESSENZIALE, che usa un terzo delle risorse.

---

## 09-C3 — "Squadre tecniche della Repubblica": pool di competenze condivise per i piccoli enti

**Problema in un dato.** Al 31.3.2026 le amministrazioni qualificate da ANAC per bandire gare sono **3.919** (ANAC, serie `09_anac_qualificazione_sa`), a fronte di **7.896 comuni**, di cui **5.522 (69,9%) sotto i 5.000 abitanti** (ISTAT, 1.1.2026, serie `09_comuni_classi_ampiezza`). Il personale specializzato in ICT è il 3,8% delle persone occupate in Italia, contro il 5,0% UE (Eurostat 2025). La maggior parte dei comuni non ha né un ufficio gare qualificato né personale informatico.

**Soluzione in 3 righe.**
1. Nasce un ruolo unico nazionale di personale tecnico pubblico (ICT, cybersicurezza, appalti, progettazione, dati) con carriera tecnica e indennità di specialità.
2. Il personale tecnico lavora in pool regionali che, con una convenzione, fanno da stazione appaltante qualificata e da presidio cyber per i comuni aderenti. L'adesione è volontaria e il presidio cyber è il braccio territoriale di 07-C6.
3. **Il costo è coperto senza nuovi fondi**: una quota delle assunzioni già autorizzate per turnover va al personale tecnico invece che a profili generici, e i pool sostituiscono le consulenze esterne.

| Variante | Contenuto | Costo a regime | Intensità | Fondo |
|---|---|---|---|---|
| PIENA | 8.000 unità di personale tecnico entro il 2031 in tutte le regioni | 0,55 (2031) | 1 | RIALLOCAZIONE (R09-1 0,45 + R09-2 0,1) |
| ESSENZIALE | 3.000 unità di personale tecnico per i comuni sotto i 5.000 abitanti di Mezzogiorno e aree interne; priorità al personale esperto PNRR valutato positivamente | 0,22 (2029) | 0,5 | RIALLOCAZIONE |
| PILOTA | 600 unità di personale tecnico a termine per 3 anni in 4 regioni, con valutazione controfattuale | 0,04 (solo 2027-29) | 0,1 | COESIONE_2127 (capacità amministrativa) |

### Articolato normativo essenziale (legge delega e decreto legislativo)

**Art. 1 (Finalità).** 1. Per rafforzare la capacità tecnica delle amministrazioni, in particolare dei comuni con meno di 5.000 abitanti, nel rispetto dell'articolo 118 della Costituzione e dell'autonomia degli enti locali, è istituito il ruolo unico delle Squadre tecniche della Repubblica presso il Dipartimento della funzione pubblica.

**Art. 2 (Ruolo e pool territoriali).** 1. Il ruolo comprende profili ICT, di cybersicurezza, di contratti pubblici, di progettazione e di analisi dei dati. 2. Il personale tecnico è assegnato a pool territoriali, costituiti d'intesa con ciascuna Regione e con l'ANCI. I pool operano per gli enti locali che vi aderiscono tramite convenzione ai sensi dell'articolo 30 del d.lgs. 18 agosto 2000, n. 267. 3. I pool possono essere qualificati come stazioni appaltanti e centrali di committenza ai sensi dell'articolo 63 del d.lgs. 31 marzo 2023, n. 36. Svolgono inoltre funzioni di presidio di sicurezza informatica per gli enti aderenti, in raccordo con l'Agenzia per la cybersicurezza nazionale.

**Art. 3 (Reclutamento e carriera).** 1. Il reclutamento avviene con concorsi nazionali per profili, banditi ogni anno. Una riserva fino al 40% dei posti è destinata al personale con contratto a termine nei progetti PNRR che ha ricevuto una valutazione positiva. 2. Il contratto collettivo definisce una carriera tecnica parallela a quella dirigenziale, un'indennità di specialità e una valutazione annuale con indicatori pubblici.

**Art. 4 (Facoltà assunzionali).** 1. Dal 2027 al 2031 una quota delle facoltà assunzionali delle amministrazioni centrali derivanti da cessazioni, determinata ogni anno con decreto del Ministro per la pubblica amministrazione di concerto con il Ministro dell'economia e delle finanze, è riservata al ruolo di cui all'articolo 1. Le assunzioni corrispondenti per altri profili non sono effettuate. 2. Gli enti locali aderenti possono trasferire al pool quote delle proprie facoltà assunzionali.

**Art. 5 (Governance e valutazione).** 1. Ogni pool ha un comitato paritetico Stato-Regione-ANCI. 2. Dopo quattro anni il Dipartimento della funzione pubblica pubblica una valutazione controfattuale tra enti aderenti e non aderenti, su tempi di gara e di esecuzione, capacità di spesa e incidenti informatici.

**Art. 6 (Copertura finanziaria).** 1. Agli oneri, pari a 80 milioni per il 2027, 200 milioni per il 2028, 320 milioni per il 2029 e 550 milioni annui dal 2031, si provvede: a) per l'80% con le risorse delle facoltà assunzionali riservate ai sensi dell'articolo 4, comma 1; b) per il 20% con la riduzione degli stanziamenti delle amministrazioni centrali per incarichi di consulenza e assistenza tecnica esterna.

### Cronoprogramma

| Fase | Chi | Cosa |
|---|---|---|
| Primi 100 giorni | Ministro PA, Conferenza unificata, ARAN | DDL delega; censimento del personale esperto PNRR in scadenza da trattenere; scelta delle 4 regioni pilota; atto di indirizzo ARAN sulla carriera tecnica |
| 12 mesi | Funzione pubblica, Regioni, ANAC | Decreto legislativo; primo concorso nazionale (circa 1.000 posti); primi pool costituiti e qualificati da ANAC; prime convenzioni con le unioni di comuni |
| Fine legislatura | Pool regionali; Funzione pubblica | 8.000 unità di personale tecnico (PIENA) o 3.000 (ESSENZIALE); valutazione controfattuale pubblicata; decisione sull'estensione |

### Indicatori

| KPI | Base | Obiettivo a 3 anni | Obiettivo a 5 anni |
|---|---|---|---|
| Comuni sotto i 5.000 abitanti serviti da un pool qualificato | 0 su 5.522 (2026; ISTAT 2026, ANAC I trim. 2026) | 2.000 | 4.000 |
| Amministrazioni qualificate per progettazione e affidamento, pool inclusi, con copertura dei comuni aderenti | 3.919 qualificate (31.3.2026, ANAC) | tutti i comuni aderenti coperti | tutti i comuni aderenti coperti, con tempi di aggiudicazione -20% rispetto ai non aderenti |
| Tempo medio ponderato di pagamento delle fatture negli enti aderenti | 30 giorni nel 2024, media nazionale (MEF-RGS; OCPI segnala sottostima) | ≤ 27 giorni, con misura dei tempi effettivi | ≤ 25 giorni |

### Rischi e mitigazione
- **Centralismo e conflitto con le Regioni (Titolo V)** → adesione volontaria, comitati paritetici, intesa in Conferenza unificata.
- **Fuga verso il privato** → indennità di specialità, mobilità tra pool, lavoro agile.
- **Il turnover riservato non basta o lascia scoperti servizi amministrativi** → quota decisa ogni anno con il MEF; si parte dalle amministrazioni centrali con più cessazioni nei profili generici. Se la riserva non è sostenibile, si resta all'ESSENZIALE.
- **Resistenze sindacali alle differenze retributive** → carriera tecnica negoziata nel contratto e criteri di accesso trasparenti.
- **Sovrapposizione con 07-C6** → il presidio cyber dei pool è l'esecuzione territoriale di 07-C6; i costi del personale stanno qui, quelli tecnologici in 07-C6.

---

## 09-C4 — Cloud pubblico sostenibile e "Patto per la manutenzione digitale"

**Problema in un dato.** Con il PNRR (1,9 mld, investimenti 1.1 e 1.2) sono migrate al cloud **circa 13.000 PA**, oltre il target di 12.464 PA locali (DTD, luglio 2026, serie `09_dtd_pdnd_psn_cloud`). Dal 2027 i canoni diventano spesa corrente dei singoli enti, e non esiste una stima ufficiale del fabbisogno. Il rischio è che i servizi tornino su server locali non sicuri. Intanto l'Italia ha subito il 10,2% degli incidenti cyber gravi nel mondo (Clusit, I semestre 2025).

**Soluzione in 3 righe.**
1. Un fondo presso il DTD cofinanzia i canoni con una quota statale decrescente (dal 70% al 30% in 5 anni), solo per gli enti che rispettano gli standard NIS2.
2. Ogni contratto cloud contiene una clausola di uscita: portabilità di dati e carichi, formati aperti, PSN incluso. Un accordo quadro Consip fissa prezzi massimi.
3. I risparmi (server dismessi, energia, licenze) sono certificati. Solo dopo la certificazione riducono la quota statale: non coprono nulla in anticipo.

| Variante | Contenuto | Costo | Intensità | Fondi |
|---|---|---|---|---|
| PIENA | Tutte le circa 13.000 PA migrate | 0,40 nel 2027-28, poi 0,25 dal 2030 | 1 | RIALLOCAZIONE 0,25 (R09-3); COESIONE_2127 0,15 (solo 2027-29) |
| ESSENZIALE | Comuni sotto i 5.000 abitanti, ASL e servizi critici; quota statale dal 60% al 30% | 0,12 | 0,45 | RIALLOCAZIONE (R09-3) |
| ZERO | Clausola di uscita, accordo quadro Consip, canoni iscritti nei bilanci, risparmi pubblicati | 0 | 0,15 | — |

**Nota sul giudizio del panel (in coda).** La PIENA costa molto rispetto al valore visibile nel breve periodo. Raccomando l'**ESSENZIALE**, che protegge il capitale costruito con il PNRR dove il rischio di abbandono è reale, oppure almeno lo **ZERO**, che non costa nulla e va fatto in ogni caso.

### Articolato normativo essenziale (articolo della legge di bilancio 2027)

**Art. 1 (Finalità e istituzione del Fondo).** 1. Per assicurare la continuità e la sicurezza dei servizi digitali pubblici realizzati con il PNRR, è istituito presso la Presidenza del Consiglio dei ministri, Dipartimento per la trasformazione digitale, il Fondo per la manutenzione digitale, con una dotazione di 400 milioni per il 2027 e il 2028, 350 milioni per il 2029 e 250 milioni annui dal 2030.

**Art. 2 (Beneficiari e cofinanziamento).** 1. Il Fondo concorre ai canoni dei servizi cloud qualificati delle amministrazioni migrate. La quota statale è pari al 70% nel 2027 e si riduce di 10 punti l'anno fino al 30%. 2. L'accesso è subordinato al rispetto delle misure minime di sicurezza adottate dall'Agenzia per la cybersicurezza nazionale ai sensi del d.lgs. 4 settembre 2024, n. 138, e alla pubblicazione dei risparmi conseguiti secondo il modello dell'AgID.

**Art. 3 (Clausola di uscita e portabilità).** 1. I contratti per servizi cloud stipulati o rinnovati dalle pubbliche amministrazioni, compresi quelli con il Polo strategico nazionale, prevedono a pena di nullità la portabilità dei dati e dei carichi di lavoro in formati aperti, senza costi di uscita superiori a quelli determinati dall'AgID. 2. Consip stipula un accordo quadro con prezzi massimi dei canoni per le amministrazioni locali.

**Art. 4 (Risparmi certificati).** 1. L'AgID certifica ogni anno i risparmi derivanti dal consolidamento: data center dismessi, energia, licenze. 2. I risparmi certificati riducono la quota statale di cui all'articolo 2 per l'anno successivo. Non sono utilizzati a copertura di nuove spese prima della certificazione.

**Art. 5 (Copertura finanziaria).** 1. Agli oneri si provvede: a) per 250 milioni annui mediante riduzione degli stanziamenti per spesa corrente in tecnologie dell'informazione delle amministrazioni centrali, in particolare per hosting non qualificato e licenze duplicate; b) per 150 milioni annui nel triennio 2027-2029 a valere sui programmi della politica di coesione 2021-2027, obiettivo strategico 1, per le spese di migrazione e rifattorizzazione ammissibili.

### Cronoprogramma

| Fase | Chi | Cosa |
|---|---|---|
| Primi 100 giorni | DTD, ACN, Consip | Censimento dei canoni in scadenza degli enti migrati; avvio dell'accordo quadro Consip; clausola di uscita nel primo veicolo normativo utile |
| 12 mesi | DTD, AgID | Fondo operativo con i primi riparti; modello per la certificazione dei risparmi; requisiti NIS2 verificati sugli enti beneficiari |
| Fine legislatura | AgID, ACN, enti | Quota statale al 30%; risparmi certificati pubblicati; revisione: la quota scende solo se i risparmi coprono almeno il 50% dei canoni |

### Indicatori

| KPI | Base | Obiettivo a 3 anni | Obiettivo a 5 anni |
|---|---|---|---|
| PA su infrastrutture cloud qualificate | circa 13.000, oltre il 75% delle amministrazioni (DTD, luglio 2026) | nessun ritorno a server locali; ≥ 85% | ≥ 95% |
| Incidenti cyber gravi noti in Italia | 245 nel I semestre 2026 (Clusit) | quota del settore pubblico in calo | -30% sugli enti beneficiari rispetto al 2026 |
| Risparmi certificati sui canoni | 0 (nessuna certificazione, 2026) | ≥ 25% dei canoni | ≥ 50% dei canoni |

### Rischi e mitigazione
- **Lock-in verso il PSN o hyperscaler extra-UE** → clausola di uscita a pena di nullità; audit AgID.
- **Fondo usato come "bancomat"** → erogazione legata agli standard NIS2 e alla certificazione dei risparmi.
- **Fabbisogno sottostimato** (13.000 enti, non 4.000) → l'ESSENZIALE concentra le risorse sui più fragili; censimento dei canoni nei primi 100 giorni.
- **Consumi energetici dei data center** → reporting obbligatorio del PUE e criteri ambientali minimi.

---

## 09-C5 — IA nella PA "con le mani sul volante"

**Problema in un dato.** Nel 2025 il **54,3%** dei 16-74enni aveva competenze digitali almeno di base, contro il **60,4%** UE e un target 2030 dell'80% (Eurostat, isoc_sk_dskl_i21, serie `09_competenze_digitali_base`). Nella PA l'uso dell'IA è disomogeneo e spesso avviene con strumenti non autorizzati, e non esiste un albo pubblico dei sistemi in uso.

**Soluzione in 3 righe.**
1. Ogni sistema di IA che incide su provvedimenti è iscritto in un albo AgID, collegato al registro di C1, con la valutazione d'impatto sui diritti pubblicata. Nessuna decisione con effetti giuridici senza revisione umana motivata.
2. Un assistente pubblico condiviso, su infrastruttura qualificata e con modelli aperti dove possibile, sostituisce le licenze sparse.
3. Formazione su IA e dati per ogni dipendente, dentro le ore di formazione già previste; Punti digitali facilitati per gli over 65.

| Variante | Contenuto | Costo a regime | Intensità | Fondi |
|---|---|---|---|---|
| PIENA | Albo, valutazione d'impatto, assistente condiviso, formazione, facilitazione nazionale | 0,22 (2028) | 1 | RIALLOCAZIONE 0,10 (R09-3); COESIONE_2127 0,12 (FSE+, fino al 2029) |
| ESSENZIALE | Stesse garanzie e assistente condiviso; facilitazione solo in aree interne e Mezzogiorno | 0,08 | 0,55 | RIALLOCAZIONE 0,05; COESIONE_2127 0,03 |
| ZERO | Solo regole (direttiva, albo, divieto, formazione nelle ore esistenti) | 0 | 0,3 | — |

**Doppio conteggio eliminato.** La versione del registro prelevava da "una quota del fondo di 09-C4" (ALTRO) e da risparmi attesi su licenze. Ora C5 non tocca il fondo di C4. Il taglio delle licenze duplicate entra come riallocazione concreta (R09-3), dentro un'unica misura di menu che C2, C4 e C5 condividono senza superarne il gettito: 0,05 + 0,25 + 0,10 = 0,40 nelle PIENE, entro il massimo stimato di R09-3 (0,42); se il menu ne attiva meno, si scende alle ESSENZIALI (0,20).

### Articolato normativo essenziale (DPCM su base dell'art. 14 l. 132/2025, con direttiva del Ministro per la PA)

**Art. 1 (Finalità).** 1. Il presente decreto disciplina l'uso dei sistemi di intelligenza artificiale nelle pubbliche amministrazioni, in attuazione dell'articolo 14 della legge 23 settembre 2025, n. 132, e del Regolamento (UE) 2024/1689. L'obiettivo è garantire che l'intelligenza artificiale sia uno strumento di supporto e che la decisione resti sempre in capo a un funzionario responsabile.

**Art. 2 (Albo e valutazione d'impatto).** 1. È istituito presso l'AgID l'albo dei sistemi di intelligenza artificiale in uso nelle pubbliche amministrazioni, collegato al Registro di cui alla legge [09-C1]. 2. Prima della messa in uso di un sistema che incide sull'adozione di provvedimenti, l'amministrazione effettua una valutazione d'impatto sui diritti fondamentali secondo il modello dell'articolo 27 del Regolamento (UE) 2024/1689 e ne pubblica l'esito nell'albo.

**Art. 3 (Supervisione umana).** 1. Nessun provvedimento con effetti giuridici nei confronti di una persona è adottato sulla sola base di un trattamento automatizzato. Il funzionario responsabile motiva l'esito della propria revisione. 2. Se il tasso di errori rilevati supera la soglia definita all'iscrizione, l'uso del sistema è sospeso d'ufficio.

**Art. 4 (Strumenti condivisi e formazione).** 1. Il Dipartimento per la trasformazione digitale mette a disposizione delle amministrazioni un assistente pubblico condiviso su infrastrutture qualificate, con divieto di addestramento sui dati delle amministrazioni e con registri di utilizzo consultabili in sede di verifica. 2. Ogni dipendente segue almeno 24 ore di formazione su intelligenza artificiale e dati nell'arco di tre anni, nell'ambito delle ore di formazione già previste. 3. Le Regioni, con le risorse del FSE+, potenziano i Punti digitali facilitati, con priorità per le persone con più di 65 anni. È garantito il diritto a un canale non digitale.

**Art. 5 (Copertura finanziaria).** 1. Agli oneri di cui all'articolo 4, comma 1, pari a 100 milioni annui dal 2028, si provvede con la riduzione degli stanziamenti delle amministrazioni centrali per licenze software e servizi di intelligenza artificiale acquisiti singolarmente. Agli oneri di cui all'articolo 4, comma 3, pari a 120 milioni annui nel 2028-2029, si provvede a valere sui programmi FSE+ 2021-2027.

### Cronoprogramma

| Fase | Chi | Cosa |
|---|---|---|
| Primi 100 giorni | Ministro PA (direttiva), AgID | Direttiva sul divieto di decisione automatizzata e sulla dichiarazione dei sistemi in uso; censimento della "shadow AI" e delle licenze IA |
| 12 mesi | DTD, AgID, Scuola nazionale dell'amministrazione | DPCM; albo online con le prime valutazioni d'impatto; assistente condiviso in produzione per redazione di atti e sintesi; percorso formativo su Syllabus |
| Fine legislatura | Tutte le amministrazioni; Regioni | Tutti i sistemi che incidono su provvedimenti iscritti nell'albo; formazione completata da ogni dipendente; rete di facilitazione stabile nei territori con il divario maggiore |

### Indicatori

| KPI | Base | Obiettivo a 3 anni | Obiettivo a 5 anni |
|---|---|---|---|
| 16-74enni con competenze digitali almeno di base | 54,27% (2025, Eurostat; UE 60,4%) | 64% (rilevazione 2029) | 72% (verso il 70% al 2030 e l'80% al 2032 del dossier) |
| Sistemi IA che incidono su provvedimenti iscritti nell'albo con valutazione d'impatto pubblica | 0 (albo inesistente, 2026) | 100% dei sistemi censiti | 100%, con verifica a campione dell'Ufficio 08-P1 |
| Personale che ha completato 24 ore su IA e dati | non misurato (2026) | 60% | 100% |

### Rischi e mitigazione
- **Discriminazioni ed errori algoritmici** (caso olandese *toeslagenaffaire*) → valutazione d'impatto, sospensione automatica oltre la soglia di errore, ricorso semplice.
- **Dati personali ceduti ai fornitori** → divieto di addestramento, infrastrutture UE, registri consultabili.
- **Timori sindacali** → accordo per cui i guadagni di tempo vanno ai servizi allo sportello e non diventano tagli di organico per 5 anni.
- **Fine del FSE+ nel 2029** → la facilitazione passa al ciclo 2028-34 se finanziato, altrimenti si scende all'ESSENZIALE. Nessun impegno permanente senza copertura.
