*Bozza scritta da un agente AI il 16 novembre 2026; da valutare con il panel e da approvare; non rivista da una persona.*

# Bozza di scheda: imposta sui patrimoni molto grandi (01-P24)

Riga proposta per `motore/proposte.csv` (formato `proposta_id,titolo,costo_min,costo_max,costo_opportunita`; da aggiungere solo dopo l'approvazione):

```csv
01-P24,"Grandi patrimoni: un'imposta annua progressiva solo sopra 5 milioni a persona, con imprese al valore contabile, tetto sul reddito ed exit tax; prima si misura",0.005,0.05,0.0
```

Diagnosi, esperienze estere e fonti: `benchmark/patrimoniale_studio.md`. Varianti: `benchmark/bozza_varianti_patrimoniale.csv`. Coperture nuove: `benchmark/bozza_coperture_patrimoniale.csv`. Importi in mld €/anno salvo diversa indicazione. "Stima GovernAI" = stima propria senza quantificazione ufficiale; "da verificare" = dato o norma non riscontrati sul testo originale.

**Questa bozza non dà punteggi sui valori.** Li daranno panel indipendenti con `motore/rubrica.md`. Per lo stesso motivo le colonne RIS ... CIT del CSV delle coperture sono vuote.

**È una scelta politica.** La bozza non raccomanda se introdurre l'imposta. Descrive come farla bene, se la si vuole, e quanto renderebbe con prudenza. Per decidere servono le risposte alle domande del par. "Scelte politiche" in fondo.

**Regole applicate (come nelle schede di `programma/schede/`).**
- Nessuna variante usa DEFICIT, RISPARMI_ATTESI, IVA_EVASIONE, ETS o ALTRO. I costi di attuazione sono su RIALLOCAZIONE (spese di funzionamento di MEF e Agenzia delle entrate).
- Il gettito è un'entrata decisa per legge (DRM), nelle coperture **FN11** (solo con la PIENA) e **FN12** (solo con la ESSENZIALE), alternative tra loro. Imputate al fondo SPESE_FISCALI come "fondo più vicino", come FN05-FN10; si ripropone al coordinatore un fondo `EQUITA_FISCALE` in `registro/fondi.csv` (non modificato).
- **La PILOTA (contributo temporaneo) non ha una riga di copertura.** Un'entrata di tre anni non può coprire spese permanenti: il suo gettito (1,4-3,8 mld l'anno nel 2028-2030) va a riduzione del debito o a spese una tantum, decise a parte.
- **Vincoli da inserire nell'ottimizzatore** (come per 01-P8 e FN01): 01-P24 PIENA, ESSENZIALE o PILOTA solo insieme a **01-P20** (qualunque variante, perché tutte contengono l'exit tax) e a **01-P23** (qualunque variante, per i dati). FN11 vale solo con 01-P24 PIENA, FN12 solo con 01-P24 ESSENZIALE.
- **Verifica degli id (16/11/2026).** Ricerca su `.md`, `.csv`, `.py` del repository: 01-P24, FN11 e FN12 non sono usati. Il coordinatore controlli prima di unire con le bozze di altri agenti.

---

## 01-P24 — Grandi patrimoni: un'imposta annua solo in cima, misurata prima e disegnata contro la fuga

**Problema in un dato.** Il 10% delle famiglie ha il **60,6%** della ricchezza netta, la metà più povera il **7,2%** (Banca d'Italia, conti distributivi, fine 2025). Il top 0,1% degli adulti, circa 50.000 persone, ha il **9,3%** della ricchezza (Acciari, Alvaredo, Morelli, JEEA 2024, dati 2016), soprattutto in attività finanziarie e partecipazioni. Le imposte patrimoniali esistenti (IMU 18,2 mld, bollo 0,2% sui prodotti finanziari, IVIE e IVAFE 0,25 mld, successioni 1,1 mld) sono **proporzionali** e cadono soprattutto su case e risparmio di massa: **la partecipazione in una società non quotata, dove sta la ricchezza più alta, non paga nessuna imposta annua sul patrimonio.** Nessuna statistica ufficiale dice quante persone hanno più di 5, 10 o 50 milioni.

**Evidenze.**
- OCSE 2018: le imposte sul patrimonio sono passate da 12 Paesi nel 1990 a 4 nel 2017; servono **soglie alte, aliquote progressive, base ampia, poche esenzioni**; gli argomenti a favore sono più forti dove redditi da capitale e successioni sono tassati poco (è il caso italiano oggi; diagnosi equità, par. 3-4).
- Spagna: imposta di solidarietà sopra 3 mln, **623 mln** da **12.010** persone nel 2023; l'imposta ordinaria esenta le imprese di famiglia e ha un **tetto**: imposte sul reddito più imposta sul patrimonio non oltre il 60% del reddito, ma si paga almeno il 20%.
- Svizzera: 9,5 mld CHF l'anno; ma un punto di aliquota in meno fa salire del **43%** la ricchezza dichiarata in sei anni, soprattutto per evasione ed elusione (Brülhart et al. 2022).
- Norvegia 2022: aliquota all'1,1% sopra circa 20 mln NOK; **al massimo circa 100 partenze**, gettito +71,5% invece di +75%, nessun calo degli investimenti delle imprese (Ring, NBER 2026).
- Francia: abolizione dell'ISF nel 2018, perdita di gettito 3-4,5 mld; **nessuna prova chiara** di più investimenti; dopo il 2018 più rientri che partenze (Comité d'évaluation 2023; CAE 2025).
- Colombia: due quinti del top 0,01% evadevano l'imposta sul patrimonio nascondendo un terzo della ricchezza all'estero (Londoño-Vélez e Ávila-Mahecha 2021).
- G20 2024: proposta di minimo del **2%** sui miliardari (Zucman), nessun accordo; nessuna proposta UE.

**Soluzione (PIENA).**
1. **Chi paga.** Le persone fisiche residenti con **patrimonio netto mondiale oltre 5 mln €** al 31 dicembre. Unità: la persona, non la famiglia. I beni intestati a figli minori si sommano a quelli dei genitori. Dichiarazione annuale obbligatoria (anche senza imposta) sopra 3 mln, **precompilata** con i dati che l'Agenzia ha già (archivio dei rapporti finanziari, catasto, registro delle imprese, quadro RW, CRS).
2. **Aliquote marginali** sulla sola parte oltre ogni soglia: **0,5%** da 5 a 10 mln; **1%** da 10 a 50 mln; **1,5%** da 50 mln a 1 mld; **2%** oltre 1 mld. Chi ha 6 mln paga 5.000 € (0,5% su 1 mln); chi ha 20 mln paga 125.000 €.
3. **Cosa entra e come si valuta** (regole semplici e uguali per tutti i beni, per non ripetere l'errore tedesco del 1995):
   - titoli quotati, fondi, depositi: valore al 31 dicembre (comunicato dagli intermediari);
   - polizze vita: valore di riscatto (coordinato con 01-P21);
   - **partecipazioni in società operative non quotate: patrimonio netto contabile** dell'ultimo bilancio, come già per le successioni (art. 16 d.lgs. 346/1990, **da verificare** il riferimento esatto), rivalutato ogni tre anni;
   - **holding passive** (definizione di 01-P19): si guarda **attraverso**, al valore delle attività che contengono;
   - immobili: valore OMI medio o, fino alla riforma del catasto (SF13), rendita catastale per coefficienti di allineamento al mercato fissati per legge;
   - arte, gioielli, barche, auto da collezione sopra 50.000 € per oggetto: valore assicurato o dichiarato, con controllo;
   - trust: attribuiti al disponente se li controlla, altrimenti ai beneficiari con diritti certi, altrimenti al trust con l'aliquota più alta;
   - debiti: deducibili solo se reali e legati a beni inclusi.
4. **Esclusioni.** Previdenza complementare e TFR maturati; beni culturali vincolati e aperti al pubblico; **il primo milione** di valore dell'abitazione principale.
5. **Niente doppia imposta.** Si scalano bollo 0,2% e IVAFE pagati sulle attività tassate; le imposte estere sul patrimonio degli immobili all'estero (e l'IVIE). L'IMU **non** si scala: è un tributo dei Comuni.
6. **Scudo per chi ha poco reddito (modello spagnolo, corretto).** Imposte personali sul reddito più patrimoniale non oltre il **60% del reddito complessivo**, compresi i redditi a tassazione sostitutiva e, con 01-P19, gli utili trattenuti dalle holding passive (così non si "abbassa" il reddito tenendolo in società). Lo sconto non supera l'80%: si paga almeno il **20%** dell'imposta.
7. **Imprese di famiglia: nessuna esenzione, ma tempo per pagare.** La parte di imposta riferita a partecipazioni di almeno il 10% in società operative in cui la persona lavora si può pagare in **rate fino a 10 anni** con gli interessi legali, o rinviare fino a vendita, donazione o successione, con ipoteca o garanzia sulle quote. Un'esenzione piena (come in Spagna e nell'ISF francese) svuoterebbe la base: in cima la ricchezza è soprattutto d'impresa.
8. **Regole contro la fuga, compatibili con il diritto UE.**
   - L'**exit tax** sulle plusvalenze latenti delle partecipazioni rilevanti di 01-P20, con pagamento sospeso senza garanzie onerose per chi va in un Paese UE/SEE (CGUE C-9/02 *de Lasteyrie*, C-470/04 *N*).
   - Per chi si trasferisce in un Paese della lista dei regimi fiscali privilegiati, resta la **presunzione di residenza** già prevista per le imposte sui redditi (art. 2 c. 2-bis TUIR), estesa alla patrimoniale per 5 anni (**da verificare** la compatibilità con l'art. 63 TFUE, che protegge anche i movimenti verso Paesi terzi).
   - Controlli rafforzati sulle residenze di comodo (criteri di residenza riformati dal d.lgs. 209/2023), con l'unità grandi patrimoni di 01-P23.
   - **Nessuna imposta sui non residenti** per la ricchezza in Italia diversa dagli immobili (già colpiti dall'IMU): niente discriminazioni e niente nuove convenzioni da negoziare.
9. **Neo-residenti (imposta fissa sui redditi esteri).** Scelta politica: (a) pagano solo sulla ricchezza in Italia per la durata dell'opzione, come oggi per IVIE e IVAFE; (b) pagano sulla ricchezza mondiale. Il gettito di FN11 è calcolato con (a).
10. **Gestione.** Unità dell'Agenzia per i grandi patrimoni (circa 250-350 persone, comprese quelle di 01-P23), valutatori, sistema informatico Sogei. Accertamento per 5 anni; sanzioni ordinarie; adesione e interpello preventivo per le valutazioni delle imprese.
11. **Valutazione e scadenza.** Il Dipartimento delle finanze e l'UPB pubblicano dopo 3 anni una valutazione su gettito, partenze, investimenti e imprese; il Parlamento conferma o modifica le aliquote. Prima applicazione: patrimonio al 31/12/2028, versamento nel 2029.

**Varianti**

| Variante | Contenuto | Costo di attuazione 2027 / 2028 / 2029 / regime | Intensità | Gettito (copertura) |
|---|---|---|---|---|
| PIENA | Punti 1-11: sopra 5 mln, 0,5% / 1% / 1,5% / 2% | 0,01 / 0,04 / 0,05 / **0,05** (2029) | 1 | **FN11: 2,0-5,0** a regime (2031) |
| ESSENZIALE | **Imposta minima** solo per chi ha oltre **50 mln**: 1% sulla parte oltre 50 mln, 2% oltre 1 mld, **meno le imposte personali sul reddito** pagate nell'anno (IRPEF, sostitutive, quota delle holding con 01-P19): paga solo chi oggi paga poco rispetto al patrimonio (modello G20 2024). Stessa valutazione, stesso scudo per le imprese, stesse regole contro la fuga | 0,005 / 0,015 / 0,02 / **0,02** (2029) | 0,45 | **FN12: 0,6-2,0** a regime (2030) |
| PILOTA | **Contributo di solidarietà per tre anni** (patrimonio al 31/12/2027, 2028, 2029) sopra **10 mln**: 0,5% fino a 50 mln, 1% fino a 1 mld, 1,5% oltre; rate in 3 anni; poi valutazione indipendente nel 2031 e decisione del Parlamento (stop, ESSENZIALE o PIENA) | 0,01 / 0,03 / 0,03 / **0,03** (2028), poi 0,005 per il registro | 0,3 | **nessuna copertura permanente**; gettito temporaneo 1,4-3,8 l'anno nel 2028-2030 |
| ZERO | Solo **misura**: dichiarazione patrimoniale annuale sopra 10 mln senza imposta (precompilata); statistica ufficiale dei grandi patrimoni con 01-P23; adesione dell'Italia allo standard G20 di imposta minima effettiva sui miliardari e sostegno a un registro europeo degli attivi; rinvio della decisione al 2029 con i dati | 0,002 / 0,005 / 0,005 / **0,005** | 0,1 | nessuna |

**Motivazione delle intensità.**
- **ESSENZIALE 0,45:** colpisce circa 2.100 persone invece di 95.000, ma tra loro c'è il 40% circa della base della PIENA; il credito per le imposte sul reddito la concentra su chi oggi paga meno, cioè sul problema della diagnosi equità. Perde la progressività tra 5 e 50 mln.
- **PILOTA 0,3:** gettito vero ma solo per tre anni; produce i dati per decidere; il rischio di "lo rifaranno" riduce la credibilità di una tassa temporanea.
- **ZERO 0,1:** nessun effetto sull'equità; costruisce la base informativa e la posizione internazionale. In gran parte coincide con 01-P23: se 01-P23 è attiva il costo aggiuntivo è quasi nullo.

**Articolato normativo essenziale** (disegno di legge collegato alla manovra; per la PIENA)

> **Art. 1 (Imposta sui grandi patrimoni).** 1. È istituita un'imposta annuale sul patrimonio netto delle persone fisiche residenti nel territorio dello Stato, ovunque detenuto, al 31 dicembre di ciascun anno, per la parte eccedente 5 milioni di euro.
> 2. L'imposta si applica con le aliquote dello 0,5 per cento sulla parte da 5 a 10 milioni, dell'1 per cento da 10 a 50 milioni, dell'1,5 per cento da 50 milioni a 1 miliardo e del 2 per cento oltre 1 miliardo di euro.
>
> **Art. 2 (Base e valutazione).** 1. Il patrimonio netto è la somma dei beni e dei diritti di contenuto economico, al netto dei debiti effettivi relativi a beni inclusi. 2. I beni sono valutati: a) gli strumenti quotati, le quote di organismi di investimento e i depositi al valore al 31 dicembre; b) le partecipazioni in società non quotate che esercitano un'attività d'impresa effettiva in proporzione al patrimonio netto risultante dall'ultimo bilancio approvato; c) le partecipazioni in società di cui all'articolo [holding personali passive, 01-P19] in proporzione al valore normale delle attività possedute; d) gli immobili al valore determinato con decreto del Ministro dell'economia sulla base delle quotazioni dell'Osservatorio del mercato immobiliare; e) i contratti di assicurazione al valore di riscatto. 3. Sono esclusi le posizioni di previdenza complementare, il trattamento di fine rapporto maturato, i beni culturali vincolati aperti al pubblico e l'abitazione principale fino a 1 milione di euro.
>
> **Art. 3 (Crediti e limite).** 1. Dall'imposta si scomputano l'imposta di bollo di cui all'articolo 13, commi 2-bis e 2-ter, della Tariffa allegata al DPR 642/1972, l'IVAFE e l'IVIE, e le imposte patrimoniali estere sugli immobili, relative ai beni inclusi. 2. La somma dell'imposta e delle imposte personali sul reddito, comprese quelle sostitutive e la quota di reddito di cui all'articolo [01-P19], non può superare il 60 per cento del reddito complessivo; la riduzione non può superare l'80 per cento dell'imposta.
>
> **Art. 4 (Imprese).** 1. La parte di imposta riferibile a partecipazioni non inferiori al 10 per cento in società che esercitano un'attività d'impresa effettiva, nelle quali il contribuente presta la propria attività, può essere versata in dieci rate annuali con gli interessi legali o sospesa fino alla cessione, alla donazione o alla successione, previa garanzia sulle partecipazioni.
>
> **Art. 5 (Trasferimento all'estero).** 1. Si applica l'articolo [exit tax di 01-P20]. 2. Le persone che trasferiscono la residenza in Stati o territori a regime fiscale privilegiato restano soggette all'imposta per i cinque periodi successivi, salvo prova contraria.
>
> **Art. 6 (Dichiarazione e valutazione).** 1. Le persone con patrimonio netto superiore a 3 milioni di euro presentano una dichiarazione annuale, predisposta dall'Agenzia delle entrate con i dati in suo possesso. 2. Dopo tre anni il Dipartimento delle finanze, sentito l'Ufficio parlamentare di bilancio, pubblica una valutazione degli effetti su gettito, residenze, investimenti e imprese.

**Chi paga.** PIENA: circa **95.000 persone** (0,2% degli adulti) hanno più di 5 mln a valori di mercato (stima GovernAI); con le imprese al valore contabile saranno meno (**n.d.**). ESSENZIALE: circa **2.100 persone** sopra 50 mln, e solo quelle che pagano imposte sul reddito sotto l'1% del patrimonio. PILOTA: circa **27.700 persone** sopra 10 mln. **Non paga** il 99,8% degli adulti, né chi ha una casa, un'impresa piccola o media o un risparmio normale.

**Costituzionalità.**
- **Art. 53 (capacità contributiva).** Il patrimonio è già usato come indice di capacità contributiva da IMU, IVIE, IVAFE e bollo. Una progressione per scaglioni rispetta il "criterio di progressività" del secondo comma. Il punto delicato è l'**aliquota rispetto al rendimento**: con il 2% su patrimoni che rendono il 5% (rendimento medio del 10% più ricco, Dalle Luche et al.) il prelievo resta sotto il reddito prodotto; il tetto del 60% del reddito evita che l'imposta superi la capacità di pagare. Pronunce specifiche della Corte sul patrimonio come indice: **da verificare** con l'ufficio giuridico.
- **Art. 3 (uguaglianza).** Il rischio maggiore: valutazioni diverse per beni diversi. La Corte tedesca ha bocciato la sua imposta nel 1995 per questo (immobili sottovalutati). Per questo la proposta usa valori OMI per gli immobili e non il catasto attuale, e guarda attraverso le holding. Il valore contabile delle imprese operative è un trattamento diverso: va giustificato con la difficoltà di valutare e con la tutela dell'impresa (art. 41), e limitato alle società operative. Contributi mirati solo su alcune categorie sono stati bocciati (Corte cost. n. 223/2012, n. 116/2013) o ammessi solo se temporanei, ragionevoli e proporzionati (n. 173/2016, n. 234/2020): un'imposta generale su tutte le persone sopra una soglia è più solida di un prelievo di categoria. Per la PILOTA vale il limite di **ragionevolezza e durata** (n. 10/2015 sulla "Robin Hood tax").
- **Art. 42 (proprietà).** Le aliquote, sotto il rendimento atteso e con tetto sul reddito, non hanno effetto di esproprio. La Corte tedesca nel 1995 aveva indicato un limite di "metà del reddito", poi abbandonato (BVerfG 2006, **da verificare**).
- **Art. 47 (tutela del risparmio).** Soglia di 5 mln (10 e 50 mln nelle altre varianti): il risparmio diffuso è fuori. Il bollo 0,2% resta com'è.
- **Art. 23 e irretroattività** (art. 3 L. 212/2000): soglie e aliquote per legge; prima data di valutazione successiva all'approvazione (31/12/2028; per la PILOTA 31/12/2027, legge approvata entro quella data).
- **Art. 81:** la copertura vale solo per il gettito permanente (FN11 o FN12); la PILOTA non copre spese permanenti.

**Diritto UE.**
- **Libera circolazione dei capitali (art. 63 TFUE) e di stabilimento (art. 49).** L'imposta tratta allo stesso modo beni italiani ed esteri e non tassa i non residenti sui beni finanziari in Italia: nessuna discriminazione. La "coda" di 5 anni per chi va in Paesi a fiscalità privilegiata è il punto più fragile: l'art. 63 vale anche verso i Paesi terzi; serve una giustificazione di contrasto all'elusione e la prova contraria (**da verificare**).
- **Exit tax:** solo con pagamento sospeso e senza garanzie onerose per i trasferimenti nell'UE/SEE (C-9/02, C-470/04). La direttiva ATAD riguarda le società, non le persone.
- **Convenzioni contro le doppie imposizioni:** alcune trattano le imposte sul patrimonio (art. 22 del Modello OCSE); vanno elencate (**da verificare**). Il credito per le imposte estere sugli immobili evita la doppia imposizione.
- **Nessuna competenza UE** per un'imposta comune (unanimità, artt. 113 e 115 TFUE). La variante ZERO usa i canali che esistono: G20, OCSE, registro europeo degli attivi, DAC.

**Rischi e mitigazioni.**
- **Elusione con valutazioni basse** (spostare ricchezza in società non quotate valutate al contabile). Guardare attraverso le holding passive (01-P19); rivalutazione triennale; clausola antiabuso specifica; controlli mirati dell'unità grandi patrimoni.
- **Evasione all'estero.** CRS e DAC; quadro RW; dopo la Colombia, programma di emersione **non** come condono (01-P12) ma con sanzioni ridotte solo se volontario e prima di un controllo.
- **Cambi di residenza.** Exit tax (01-P20), presunzione di residenza per i Paesi a fiscalità privilegiata, controlli sulle residenze di comodo. Gettito ridotto in ogni caso del 3-15% (già nelle stime).
- **Liquidità e imprese di famiglia.** Tetto sul reddito; rate o rinvio per le quote d'impresa; esclusione del primo milione della casa.
- **Annuncio e fughe anticipate.** Data di valutazione certa e vicina all'approvazione; per la PILOTA patrimonio al 31/12/2027 con legge approvata entro il 2027.
- **Costi di gestione e di adempimento.** Precompilata, valori standard (OMI, bilanci), interpello per le imprese; costo pubblico 0,05 mld a regime (1-2,5% del gettito della PIENA, **stima GovernAI**); costi per i contribuenti **n.d.**
- **Gettito incerto.** Intervalli larghi e minimo prudente; valutazione dopo 3 anni.

**Indicatori**

| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Statistica ufficiale dei patrimoni sopra 5, 10, 50 mln (numero, composizione) | non esiste, 2026 | pubblicata ogni anno | serie con 01-P23 |
| Gettito effettivo / gettito statico (tasso di erosione) | n.d. | misurato | stabile o in calo |
| Partenze nette dei contribuenti dell'imposta (per anno) | n.d. (circa 0,2% del top 1% in Francia) | sotto 0,5% l'anno | sotto 0,5% l'anno |
| Investimenti e occupazione delle imprese dei contribuenti (confronto con imprese simili) | n.d. | nessun calo significativo | nessun calo significativo |
| Aliquota effettiva complessiva del top 0,1% (01-P23) | 32,6-36%, 2015 (stime accademiche) | prima misura ufficiale | +3/+6 punti |

**Interazioni con le altre misure (niente doppioni).**
- **SF13 (catasto):** precondizione per valutare gli immobili come le altre attività; finché manca si usano i valori OMI. Nessun effetto sul gettito IMU.
- **SF14 e 01-P22 (successioni):** prelievo una volta per generazione contro prelievo annuo. Se sono attive, la patrimoniale si può fermare alla ESSENZIALE o alla ZERO (scelta politica). Gettiti separati.
- **01-P19 (holding) e 01-P20 (redditi finanziari, exit tax):** complementari e necessarie. Con la ESSENZIALE, più imposte sul reddito vuol dire meno patrimoniale: il minimo di FN12 lo tiene già in conto.
- **01-P21 (polizze e trust):** valutazione al riscatto e attribuzione dei trust coerenti.
- **01-P23 (statistica e unità grandi patrimoni):** la variante ZERO vi si fonde; l'unità di 01-P23 gestisce l'imposta.

**Scelte politiche da sottoporre a chi guida il progetto** (non decise qui):
1. Se introdurre un'imposta sul patrimonio, e quale variante.
2. Soglia e aliquote della PIENA (5 mln e 0,5-2% sono una proposta, non un dato).
3. Imprese di famiglia: valore contabile con rinvio (proposto) o esenzione (gettito molto più basso, modello spagnolo).
4. Neo-residenti: ricchezza estera inclusa o esclusa.
5. Se, con SF14 e 01-P22 attive, la patrimoniale serve ancora o basta la misura (ZERO).
