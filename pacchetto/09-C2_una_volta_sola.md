# 09-C2 — "Chiedilo una volta sola": il diritto a non fornire due volte i dati che lo Stato ha già

*Testo preparato da un agente AI per GovernAI il 13 novembre 2026, a partire dalle schede e dai controlli giuridici del programma. Non è stato rivisto da una persona esperta: va verificato prima di essere presentato.*

Variante del programma intermedio: **ZERO** (solo regole, nessun fondo dedicato; indennizzo dopo 36 mesi). Fonti interne: `programma/schede/09_pa_digitale.md` (09-C2), `programma/varianti/09_pa_digitale.csv`, `giuridico/conformita*.csv` (righe 09-C2, ambiti COS e UE), `giuridico/note_COS.md`, `dati/verifiche/09_pa_digitale.md`.

---

## 1. Scheda in breve

- **Che cosa fa.** Rende esigibile un principio che esiste dal 2000 ma non si applica: l'amministrazione non può chiedere a una persona o a un'impresa un dato che un'altra amministrazione ha già e che è disponibile sulla Piattaforma digitale nazionale dati (PDND). Un decreto fissa, per un elenco di procedimenti a maggior volume (fino a cento), la data da cui i dati si acquisiscono solo via PDND. Dopo 36 mesi, chi se li vede chiedere di nuovo ha diritto a un indennizzo forfettario: 30 euro la persona, 100 euro l'impresa, pagati dall'ente inadempiente, con un tetto annuo per ente.
- **Perché.** Nel 2025 solo il 43,5% dei 16-74enni ha usato online i servizi della PA, contro il 57,7% della media UE. L'infrastruttura c'è già (oltre 14.000 servizi sulla PDND). Manca l'obbligo di usarla.
- **Costo per lo Stato.** Zero. Le regole usano strutture e piattaforme esistenti. Gli indennizzi sono eventuali e restano nei bilanci degli enti inadempienti, con un tetto.
- **Veicolo consigliato.** Proposta di legge autonoma con norme direttamente applicative (novelle al Codice dell'amministrazione digitale e al d.P.R. 445/2000). In alternativa, emendamento a un disegno di legge di semplificazione o a un decreto-legge in materia di PA digitale, se la materia è omogenea. **Non** un decreto legislativo: oggi non c'è una delega vigente adatta (controllo giuridico COS).
- **Chi la può presentare.** Ogni parlamentare o gruppo; il Governo come disegno di legge.
- **Tempi.** Presentazione subito; decreto con l'elenco entro 6 mesi dall'entrata in vigore; date di passaggio tra il 12° e il 36° mese; indennizzo dal 37° mese.

---

## 2. Relazione illustrativa

### Il problema (fatti)

- **Uso dei servizi digitali.** Nel 2025 il 43,5% delle persone tra 16 e 74 anni ha interagito online con la PA; la media UE è del 57,7% (Eurostat, tabella `isoc_ciegi_ac`, indicatore I_IUGOV1; serie GovernAI `09_egov_uso_cittadini`). L'offerta di servizi digitali italiani è invece sopra la media UE (86,1 contro 84,6; Commissione europea, *State of the Digital Decade 2026*, come riportato nella scheda).
- **L'infrastruttura esiste.** Al 31 maggio 2026 la PDND contava oltre 9.400 enti aderenti, oltre 14.000 servizi (e-service), circa 45.000 connessioni e oltre 1,1 miliardi di scambi via API (Dipartimento per la trasformazione digitale, dati riportati in `dati/verifiche/09_pa_digitale.md`, riga 17).
- **Il principio esiste.** L'[art. 43 del d.P.R. 445/2000](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:2000-12-28;445~art43) obbliga le amministrazioni ad acquisire d'ufficio i dati già in possesso della PA, per via telematica. L'[art. 50-ter del CAD](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82~art50ter) istituisce la PDND, obbliga gli enti ad accreditarsi e a rendere disponibili le proprie basi dati, e prevede già la tracciatura degli accessi (comma 2).
- **Che cosa manca.** Non è misurata la quota di procedimenti in cui i dati sono davvero acquisiti dalla PDND e non chiesti alle persone (dato da acquisire: il DTD pubblica le adesioni, non l'uso nei procedimenti). E la persona a cui si chiede di nuovo un documento non ha alcun rimedio pratico: l'unica sanzione esistente riguarda la retribuzione di risultato dei dirigenti che non rendono disponibili i dati (art. 50-ter, comma 5, CAD), non chi li richiede senza motivo.

### Giudizio (separato dai fatti)

Il collo di bottiglia non è la tecnologia ma l'incentivo: oggi chiedere il documento alla persona non costa nulla all'ufficio. Un diritto con un rimedio semplice, che costa all'ente solo se l'ente non si adegua, sposta l'incentivo senza spesa pubblica nuova.

### La soluzione

1. Un elenco ufficiale di procedimenti a maggior volume (fino a cento; per primi ISEE, prestazioni sociali, anagrafe e stato civile, iscrizioni scolastiche, SUAP, cambio di residenza), con la base giuridica di ogni flusso di dati e una data di passaggio per ciascuno.
2. Dopo la data, l'ente acquisisce i dati solo dalla PDND. Se li chiede di nuovo, dal 37° mese paga un indennizzo forfettario, con un tetto annuo dello 0,5% delle spese correnti.
3. Un cruscotto pubblico trimestrale, ente per ente, costruito con i dati di tracciatura che la PDND già raccoglie. Ogni persona può vedere, in modo graduale e dove la tracciatura lo consente, quali amministrazioni hanno consultato i suoi dati.

### Articolo per articolo

- **Art. 1** dichiara la finalità e il titolo di competenza statale (coordinamento informatico dei dati, art. 117, secondo comma, lett. r), Cost.).
- **Art. 2** inserisce nel CAD l'art. 50-quinquies: elenco dei procedimenti, data di passaggio, divieto di richiesta, indennizzo, tetto, imputazione all'ente titolare quando l'inadempimento è suo, cruscotto, consultazione degli accessi, rettifica.
- **Art. 3** coordina l'art. 43 del d.P.R. 445/2000 con il nuovo articolo.
- **Art. 4** prevede la relazione al Parlamento e la revisione a 48 mesi.
- **Art. 5** contiene la clausola di invarianza finanziaria.

---

## 3. Articolato

**Proposta di legge — "Disposizioni per l'esigibilità del principio "una volta sola" nei rapporti tra amministrazioni pubbliche, persone e imprese"**

**Art. 1** *(Finalità)*

1. La presente legge rende esigibile il diritto delle persone fisiche e delle imprese a non fornire alle pubbliche amministrazioni dati e documenti già in possesso di un'altra amministrazione e disponibili tramite la Piattaforma digitale nazionale dati di cui all'articolo 50-ter del decreto legislativo 7 marzo 2005, n. 82. Essa costituisce esercizio della competenza esclusiva dello Stato in materia di coordinamento informativo statistico e informatico dei dati dell'amministrazione statale, regionale e locale, ai sensi dell'articolo 117, secondo comma, lettera r), della Costituzione, e attua il principio di cui all'articolo 43 del decreto del Presidente della Repubblica 28 dicembre 2000, n. 445, in coerenza con il regolamento (UE) 2018/1724 e con il regolamento (UE) 2024/903.

**Art. 2** *(Diritto a non fornire dati già in possesso delle amministrazioni. Inserimento dell'articolo 50-quinquies del decreto legislativo 7 marzo 2005, n. 82)*

1. Dopo l'articolo 50-ter del decreto legislativo 7 marzo 2005, n. 82, è inserito il seguente:

«Art. 50-quinquies *(Diritto a non fornire dati già in possesso delle amministrazioni)*. — 1. Con decreto del Presidente del Consiglio dei ministri o del Ministro delegato per l'innovazione tecnologica e la transizione digitale, di concerto con il Ministro per la pubblica amministrazione, previa intesa in sede di Conferenza unificata di cui all'articolo 8 del decreto legislativo 28 agosto 1997, n. 281, sentiti l'AgID e il Garante per la protezione dei dati personali, da adottare entro sei mesi dalla data di entrata in vigore della presente disposizione, è approvato l'elenco dei procedimenti amministrativi a maggior volume, in numero non superiore a cento, per i quali si applica il presente articolo. Sono inclusi in via prioritaria i procedimenti relativi alla dichiarazione sostitutiva unica ai fini ISEE, alle prestazioni sociali agevolate, all'anagrafe e allo stato civile, alle iscrizioni scolastiche, allo sportello unico per le attività produttive e al cambio di residenza.

2. Per ciascun procedimento il decreto di cui al comma 1 indica:
a) i dati e i documenti che l'amministrazione procedente acquisisce d'ufficio;
b) l'amministrazione titolare di ciascun dato e il servizio della Piattaforma digitale nazionale dati che lo rende disponibile;
c) la disposizione di legge o di regolamento che costituisce la base giuridica del trattamento e dello scambio, nel rispetto del principio di limitazione della finalità di cui all'articolo 5, paragrafo 1, lettera b), del regolamento (UE) 2016/679;
d) la data a decorrere dalla quale i dati sono acquisiti esclusivamente tramite la Piattaforma, compresa tra il dodicesimo e il trentaseiesimo mese dalla data di entrata in vigore della presente disposizione.

3. Dalla data di cui al comma 2, lettera d), l'amministrazione procedente non richiede all'interessato i dati e i documenti indicati nel decreto, salvo che l'interessato, informato della possibilità dell'acquisizione d'ufficio, scelga di produrli direttamente. Restano fermi gli obblighi di indicazione degli elementi indispensabili per il reperimento delle informazioni di cui all'articolo 43, comma 1, del decreto del Presidente della Repubblica 28 dicembre 2000, n. 445.

4. Decorsi trentasei mesi dalla data di entrata in vigore della presente disposizione, e comunque non prima della data di cui al comma 2, lettera d), l'amministrazione che, in violazione del comma 3, richiede all'interessato un dato o un documento disponibile tramite la Piattaforma corrisponde all'interessato, su istanza presentata anche in via telematica entro novanta giorni dalla richiesta, un indennizzo forfettario per ciascun procedimento pari a 30 euro per le persone fisiche e a 100 euro per le imprese. L'indennizzo è corrisposto entro sessanta giorni dall'istanza, anche mediante la piattaforma di cui all'articolo 5, comma 2.

5. Se il dato non è disponibile sulla Piattaforma per inadempimento dell'amministrazione titolare agli obblighi di cui all'articolo 50-ter, comma 2, l'indennizzo è a carico di quest'ultima. L'amministrazione procedente che lo ha corrisposto ha diritto di rivalsa.

6. L'importo complessivo degli indennizzi corrisposti in ciascun anno da ciascuna amministrazione non supera lo 0,5 per cento delle spese correnti risultanti dall'ultimo rendiconto approvato. Raggiunto il limite, le istanze successive sono soddisfatte nell'esercizio seguente, con precedenza rispetto a quelle sopravvenute.

7. Gli indennizzi sono corrisposti a valere sulle risorse disponibili nei bilanci delle amministrazioni tenute al pagamento. La mancata adozione delle misure necessarie al rispetto del comma 3 è valutata ai fini della responsabilità dirigenziale e della retribuzione di risultato dei dirigenti responsabili, ai sensi dell'articolo 50-ter, comma 5.

8. Il Dipartimento per la trasformazione digitale della Presidenza del Consiglio dei ministri pubblica in formato aperto, con cadenza trimestrale, un cruscotto con lo stato di attuazione del presente articolo per ciascuna amministrazione e per ciascun procedimento, elaborato a partire dalle informazioni sugli accessi e sulle transazioni raccolte dalla Piattaforma ai sensi dell'articolo 50-ter, comma 2, e dagli indennizzi comunicati dalle amministrazioni.

9. Progressivamente, secondo le modalità stabilite con il decreto di cui al comma 1 e nei limiti delle informazioni di tracciatura disponibili, ciascun interessato può consultare, tramite il punto di accesso telematico di cui all'articolo 64-bis, l'elenco delle amministrazioni che hanno acquisito i suoi dati tramite la Piattaforma per i procedimenti di cui al comma 1. Restano fermi i diritti di cui agli articoli 15 e seguenti del regolamento (UE) 2016/679.

10. La rettifica di un dato effettuata dall'amministrazione titolare è resa disponibile tramite la Piattaforma alle amministrazioni che lo hanno acquisito per i procedimenti in corso, secondo le linee guida adottate dall'AgID ai sensi dell'articolo 50-ter, comma 2.

11. Per i procedimenti che rientrano nell'ambito del regolamento (UE) 2018/1724 lo scambio transfrontaliero di prove avviene tramite il sistema tecnico di cui all'articolo 14 del medesimo regolamento.».

**Art. 3** *(Coordinamento con il testo unico in materia di documentazione amministrativa)*

1. All'articolo 43 del decreto del Presidente della Repubblica 28 dicembre 2000, n. 445, dopo il comma 1 è inserito il seguente: «1-bis. Per i procedimenti individuati ai sensi dell'articolo 50-quinquies del decreto legislativo 7 marzo 2005, n. 82, si applicano le disposizioni del medesimo articolo.».

**Art. 4** *(Relazione e revisione)*

1. Entro quarantotto mesi dalla data di entrata in vigore della presente legge, il Ministro delegato per l'innovazione tecnologica e la transizione digitale trasmette alle Camere una relazione sull'attuazione dell'articolo 50-quinquies del decreto legislativo n. 82 del 2005, con l'indicazione, per ciascuna categoria di enti, dei procedimenti adeguati, degli indennizzi corrisposti e delle cause dei ritardi, ai fini di eventuali interventi di supporto agli enti di minori dimensioni.

**Art. 5** *(Clausola di invarianza finanziaria)*

1. Dall'attuazione della presente legge non devono derivare nuovi o maggiori oneri a carico della finanza pubblica. Le amministrazioni interessate provvedono agli adempimenti previsti con le risorse umane, strumentali e finanziarie disponibili a legislazione vigente.

> **Verifiche sul testo vigente (Normattiva, 13 novembre 2026):** nel CAD esistono gli artt. 50-ter (commi 1, 2, 2-bis, 3-8) e 50-quater (dati generati nei servizi in concessione); l'art. 50-quinquies è libero. L'art. 43 d.P.R. 445/2000 ha i commi 1-6, senza comma 1-bis. Il riferimento all'art. 5, comma 2, CAD per pagoPA è [da verificare sul testo vigente].

---

## 4. Relazione tecnica (art. 17, comma 3, L. 196/2009)

**Art. 1.** Norma di principio. Nessun effetto finanziario.

**Art. 2.**
- *Commi 1-2 (decreto ed elenco).* Il decreto è predisposto dal Dipartimento per la trasformazione digitale (DTD) e dal Dipartimento della funzione pubblica con il personale in servizio. La ricognizione dei flussi usa il catalogo dei servizi già pubblicato sulla PDND. Nessun onere.
- *Comma 3 (divieto di richiesta).* Specifica un obbligo già vigente (art. 43 d.P.R. 445/2000; art. 50-ter, comma 2, CAD). L'accreditamento alla PDND e l'esposizione delle basi dati sono già dovuti «senza nuovi o maggiori oneri per la finanza pubblica» (art. 50-ter, commi 2 e 8, CAD). Nessun onere aggiuntivo.
- *Commi 4-7 (indennizzo).* Onere **eventuale**, che sorge solo se l'ente viola un obbligo vigente e solo dopo 36 mesi. È a carico dei bilanci delle amministrazioni inadempienti, entro un tetto annuo dello 0,5% delle spese correnti, e si paga con le risorse disponibili. Per gli enti territoriali vale l'equilibrio di bilancio (art. 9 L. 243/2012; d.lgs. 118/2011): l'indennizzo non può essere finanziato con maggiore indebitamento. Non si iscrivono effetti sui saldi. **Punto debole da dichiarare:** il volume delle richieste indebite dopo 36 mesi non è stimabile oggi (dato da acquisire: numero annuo di pratiche per procedimento e quota già once-only). La Ragioneria generale potrebbe chiedere di quantificarlo, perché un indennizzo pagato da un ente pubblico peggiora, in principio, l'indebitamento netto della PA. Argomenti a sostegno dell'invarianza: (i) l'onere è evitabile con un adempimento già obbligatorio e già finanziato (fondi PNRR per l'adesione alla PDND); (ii) il tetto rende l'onere massimo finito per ente; (iii) l'indennizzo è pagato a valere su stanziamenti esistenti, senza autorizzazione di spesa nuova. Se la Ragioneria non accetta, si può ripiegare su uno di questi correttivi: indennizzo pagato entro un apposito limite di spesa per ente, oppure indennizzo sostituito da una sanzione sulla retribuzione di risultato dei dirigenti (a effetto finanziario nullo).
- *Comma 8 (cruscotto).* Il DTD elabora i dati di tracciatura che la PDND già raccoglie (art. 50-ter, comma 2) e li pubblica sul sito esistente. Si fa con il personale del Dipartimento e con i contratti di gestione della Piattaforma già in essere. Nessun onere.
- *Comma 9 (consultazione degli accessi).* Attuazione **progressiva** e «nei limiti delle informazioni di tracciatura disponibili»: se la tracciatura non registra la persona interessata, la funzione si attiva con le evoluzioni già programmate della Piattaforma e del punto di accesso telematico. Nessun onere aggiuntivo; resta da verificare con il DTD la fattibilità tecnica (dato da acquisire).
- *Commi 10-11.* Usano la Piattaforma e il sistema tecnico UE già esistenti. Nessun onere.

**Art. 3.** Coordinamento. Nessun effetto.
**Art. 4.** Relazione predisposta dal DTD con dati già disponibili. Nessun onere.
**Art. 5.** Clausola di invarianza.

**Prospetto riepilogativo (milioni di euro)**

| Articolo | Saldo netto da finanziare 2027 | 2028 | 2029 | Fabbisogno 2027 | 2028 | 2029 | Indebitamento netto 2027 | 2028 | 2029 |
|---|---|---|---|---|---|---|---|---|---|
| Artt. 1-5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Totale** | **0** | **0** | **0** | **0** | **0** | **0** | **0** | **0** | **0** |

Coerenza con il programma: variante ZERO di 09-C2, costo 0 in tutti gli anni (`programma/varianti/09_pa_digitale.csv`). L'indennizzo parte nel 2030 (37° mese, se la legge entra in vigore nel 2027), quindi fuori dal triennio 2027-2029.

---

## 5. Analisi tecnico-normativa (sintesi)

- **Norme modificate.** CAD, d.lgs. 82/2005: inserimento dell'art. 50-quinquies. D.P.R. 445/2000: inserimento dell'art. 43, comma 1-bis. Nessuna abrogazione.
- **Norme richiamate.** [Art. 50-ter CAD](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82~art50ter) (PDND, tracciatura, sanzione dirigenziale, invarianza); art. 64-bis CAD (punto di accesso telematico); [art. 43 d.P.R. 445/2000](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:2000-12-28;445~art43); [art. 2-bis L. 241/1990](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1990-08-07;241~art2bis) (modello dell'indennizzo da ritardo, comma 1-bis: indennizzo «per il mero ritardo», importi rinviati a legge o regolamento).
- **Costituzione.** Titolo statale: art. 117, secondo comma, lett. r) (coordinamento informatico dei dati), che vincola anche Regioni ed enti locali; art. 97 (buon andamento). Autonomia finanziaria degli enti (artt. 114 e 119): l'indennizzo a carico degli enti è proporzionato grazie al tetto dello 0,5% (controllo COS). Intesa in Conferenza unificata sul decreto, prevista nel testo (condizione COS recepita).
- **Strumento.** Legge ordinaria con norme direttamente applicative al posto del decreto legislativo indicato nella scheda, perché manca una delega vigente (condizione COS, `giuridico/note_COS.md`). Se il Governo preferisce un decreto legislativo, serve prima una delega (per esempio nella legge annuale di semplificazione) [da verificare: deleghe in corso].
- **Diritto UE.**
  - [Reg. (UE) 2018/1724](https://eur-lex.europa.eu/eli/reg/2018/1724/oj), art. 14: per i procedimenti transfrontalieri si usa il sistema tecnico once-only (comma 11).
  - [Reg. (UE) 2024/903](https://eur-lex.europa.eu/eli/reg/2024/903/oj) (Europa interoperabile): il DTD effettua la valutazione d'interoperabilità sul decreto [da verificare se l'obbligo dell'art. 3 si applica a questo atto].
  - [Reg. (UE) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj): ogni flusso ha una base giuridica indicata nel decreto (comma 2, lett. c); limitazione della finalità rispettata; nessuna banca dati unica (art. 50-ter, comma 3, CAD). Condizione UE recepita: catalogo delle basi giuridiche.
- **Notifiche alla Commissione europea.** Nessuna. Non è una regola tecnica su prodotti o servizi della società dell'informazione ai sensi della [direttiva (UE) 2015/1535](https://eur-lex.europa.eu/eli/dir/2015/1535/oj): disciplina rapporti tra amministrazioni e persone. Non è un aiuto di Stato.
- **Parere del Garante** sul decreto attuativo (previsto al comma 1).

---

## 6. Analisi d'impatto (sintesi)

**Obiettivi.** Meno adempimenti ripetuti per persone e imprese; più uso dei servizi digitali; misurazione pubblica dell'uso reale della PDND.

**Indicatori** (da `apprendimento/obiettivi.yaml`, righe 09-C2)

| Indicatore | Base | Obiettivo a 3 anni | Obiettivo a 5 anni |
|---|---|---|---|
| 16-74enni che hanno interagito online con la PA | 43,5% (2025, Eurostat `isoc_ciegi_ac`) | 52% | 60% (media UE 2025: 57,7%) |
| Procedimenti dell'elenco con acquisizione esclusiva via PDND | non misurato (2026; il DTD pubblica solo le adesioni) | 50 su 100 | 100 su 100 |
| Indennizzi pagati per 10.000 pratiche | 0 (diritto non vigente, 2026) | in calo per 4 trimestri consecutivi | meno della metà del primo anno di applicazione |

Avvertenza: con la variante ZERO la scheda attribuisce intensità 0,3; gli obiettivi sopra sono quelli della scheda completa e vanno considerati un tetto, non un'attesa.

**Chi ne beneficia.** Persone e imprese che presentano domande ripetute (ISEE, prestazioni, iscrizioni, SUAP); gli uffici che smettono di verificare documenti cartacei.

**Chi ne sopporta i costi.** Gli enti che non si adeguano entro 36 mesi (indennizzi, entro il tetto). Il rischio è maggiore per i comuni piccoli: 5.522 comuni sotto i 5.000 abitanti (ISTAT 2026, come riportato in `programma/varianti/09_pa_digitale.csv`). Per questo il programma abbina la misura alle squadre tecniche per i piccoli enti (09-C3, variante ESSENZIALE nel programma intermedio).

---

## 7. Note per chi presenta

- **Rischi politici.** L'ANCI e le Regioni possono leggerla come una sanzione sugli enti. *Risposta:* 36 mesi di tempo, tetto dello 0,5%, l'indennizzo ricade su chi detiene il dato se l'inadempimento è suo, intesa in Conferenza unificata sull'elenco e sulle date.
- **Obiezione "costa agli enti".** *Risposta:* costa solo a chi viola un obbligo vigente dal 2000 e finanziato con il PNRR. L'obiettivo dichiarato è che gli indennizzi tendano a zero.
- **Obiezione "sorveglianza".** *Risposta:* nessuna banca dati unica; scambi puntuali con base giuridica pubblicata; la persona vede chi ha consultato i suoi dati.
- **Rischio di attuazione.** Senza fondi (variante ZERO) i piccoli enti arrivano in ritardo. Il passaggio successivo naturale è la variante ESSENZIALE (30 procedimenti con supporto finanziato), quando ci sono risorse. La relazione a 48 mesi (art. 4) serve a decidere.
- **Rischio Ragioneria.** L'indennizzo potrebbe essere contestato in sede di bollinatura (vedi relazione tecnica). Tenere pronta la versione di ripiego (sanzione sulla retribuzione di risultato).
- **Alleanze possibili.** Associazioni dei consumatori e delle imprese (semplificazione), Ordini professionali (commercialisti, consulenti del lavoro), comunità degli sviluppatori della PA.
- **Passaggi successivi.** Decreto con l'elenco entro 6 mesi (intesa in Conferenza unificata, parere Garante, AgID); linee guida AgID sulla rettifica; primo cruscotto entro 12 mesi; relazione a 48 mesi.
