# Esame di costituzionalità: le decisioni di GovernAI sui conti 2027-2029

*Esame approfondito delle misure adottate dal Consiglio di GovernAI nella seduta «Conti in ordine senza tagliare i servizi essenziali» (`governo/verbali/2026-11-08-1-conti-in-ordine.json`, campo `decisioni`), 8 novembre 2026. Si applica lo stesso metodo e lo stesso rigore usati per la manovra del Governo ([`AC3174_manovra_2027.md`](AC3174_manovra_2027.md)). Si valuta la conformità alla Costituzione, non l'opportunità delle scelte.*

## Fonti e metodo

- **Decisioni.** 53 decisioni: 46 misure adottate, 7 respinte o rinviate. Si esaminano le 46 adottate, nella variante scelta, con le condizioni scritte nella motivazione.
- **Testi.** Per ciascuna misura, l'«Articolato normativo essenziale» della scheda in `programma/schede/`.
  - Le schede sono schemi di principio, non testi pronti per il deposito: alcuni rilievi dipendono dalla forma ancora provvisoria.
  - Quando la decisione del Consiglio modifica la scheda (ad esempio 01-P2 PIENA con ordine e calendario in legge, o 02-C3 senza contributo), vale la decisione.
- **Quadro giuridico.** Verifiche già svolte in `giuridico/conformita.csv`, ambito COS. Questo esame le aggiorna alla giurisprudenza fino al 3/11/2026 e al d.lgs. 147/2026.
- **Screening.** `python costituzione/controllo.py <scheda> --scheda <id>` su tutte le 46 misure. I rapporti sono in [`governai/`](governai/), uno per misura.
  - 4 misure hanno segnali alti; dopo l'esame:
    - 03-P1 è un falso positivo (fondo statale, non regionale);
    - 05-C2, 06-C2 e 07-C2 sono deleghe con criteri scritti in forma non standard, da riformulare come «princìpi e criteri direttivi».
  - 16 misure hanno segnali medi.
  - Lo screening **non vede** i rischi principali, che stanno nelle coperture, nella collocazione dei testi e nel quadro normativo cambiato. Per questo l'esame approfondito è necessario.
- **Giurisprudenza.** Ogni pronuncia citata è verificata sui dati aperti della Corte (`costituzione/giurisprudenza_verificata.json`).

## Sintesi

Anche GovernAI ha **rischi costituzionali concreti**: nessuna illegittimità probabile nelle varianti adottate, ma tre dubbi seri e alcuni difetti di strumento.

| # | Misura | Esito | Parametro | Problema | Riformulazione |
|---|---|---|---|---|---|
| 1 | **01-P2 PIENA**: scadenza di tutte le 573 spese fiscali, con delega | Dubbio serio | artt. 76, 53, 3, 31; affidamento | La delega fa decadere anche componenti **strutturali** dell'IRPEF che garantiscono la tassazione del reddito netto e la progressività (detrazioni per lavoro e pensione, deduzione dei contributi obbligatori): non sono «agevolazioni». Restano incerti i criteri per scegliere quali misure scadono e l'affidamento sulle agevolazioni pluriennali | Escludere per legge gli elementi strutturali del tributo; criteri di scelta e calendario in legge (già deciso); salvezza delle rate maturate; legge delega separata dalla legge di bilancio |
| 2 | **04-P3 PILOTA**: rivalutazione del «Fondo TPL» sull'IPCA, con tetto nominale | Dubbio serio. Diventa illegittimità probabile se attuata come nuovo fondo statale vincolato senza intesa | artt. 117, quarto comma, 119 | Dal 2027 il Fondo TPL **non esiste più**: il d.lgs. 147/2026 lo sostituisce con una compartecipazione IRPEF. Rivalutare un fondo soppresso è impossibile. Ricrearlo come trasferimento vincolato in una materia residuale contrasta con l'art. 119 (sent. 222/2005, 370/2003, 423/2004) | Agire sull'aliquota di compartecipazione (legge e DPCM d'intesa), oppure sulle risorse aggiuntive dell'art. 119, quinto comma, per obiettivi definiti, con intesa e criteri di riparto in legge |
| 3 | **Coperture «certificate» e spesa a gradini** (02-C2, 05-C1, 05-C2, 07-C1, 09-C3, 01-P2, 02-C5 e altre) | Dubbio serio, trasversale | art. 81, terzo comma; L. 196/2009, art. 17 | Diverse misure passano dalla variante ESSENZIALE alla PIENA «con atto ricognitivo» dopo una certificazione della Ragioneria, oppure contano coperture che dipendono da un'altra legge («RB03 solo se il DDL 2027 passa così com'è»). La spesa si autorizza per legge, con copertura contestuale. Un atto amministrativo può accertare una condizione, non aumentare la spesa | La legge autorizza il limite massimo (PIENA) con la sua copertura e lo condiziona espressamente; l'atto della Ragioneria accerta soltanto. Oppure: la legge autorizza solo l'ESSENZIALE e la PIENA arriva con una legge successiva. Le coperture vanno nella stessa legge che spende |

Altri rilievi, di minore gravità ma da correggere:
- **09-C8**: norme ordinamentali «anticipate alla legge di bilancio 2027». Saranno stralciate come gli artt. 69, comma 8, 105 e 115 dell'A.C. 3174.
- **01-P1, 08-P1, 04-P4, 02-C6**: modificano la L. 243/2012 (UPB). Serve un testo separato, approvato a maggioranza assoluta, mai inserito nella legge di bilancio. Per 08-P1 serve anche l'intesa con le Camere (art. 64).
- **02-C3**: la copertura con una perequazione al 50% dal 2030 si somma ai tagli 2023-2024 e 2027 della manovra.
- **06-C1**: la sospensione dell'intramoenia e l'agenda unica toccano l'organizzazione sanitaria regionale.
- **02-C2**: intesa sul riparto, oggi rafforzata dalla sent. 182/2026.
- **01-P10 e 01-P3**: uso dei dati fiscali e blocchi preventivi.
- Dettagli nella sezione 4.

---

## 1. 01-P2 PIENA: spese fiscali «a scadenza»

**La decisione.** Tutte le 573 spese fiscali erariali (129,7 mld) ricevono una data di scadenza, scaglionata in cinque anni, con un decreto legislativo. Il Consiglio ha accolto queste condizioni:
- ordine e calendario fissati nella legge delega, con per prime le misure di costo maggiore e senza valutazione;
- salvezza delle rate maturate;
- decorrenza dal periodo d'imposta successivo;
- esclusione degli obblighi UE;
- accesso ai microdati con base legale e valutazione d'impatto sulla protezione dei dati (DPIA).

**I profili.**

1. **Elementi strutturali del tributo (artt. 53 e 3).** Il Rapporto sulle spese fiscali (art. 21, c. 11-bis, L. 196/2009) censisce anche voci che non sono agevolazioni ma servono a misurare la capacità contributiva:
   - le detrazioni per lavoro dipendente e pensione, che costruiscono la no tax area e la progressività effettiva;
   - la deduzione dei contributi previdenziali obbligatori;
   - le detrazioni per carichi di famiglia, oggi in parte assorbite dall'assegno unico.

   Esempi da verificare voce per voce sul Rapporto. La loro decadenza automatica non elimina un privilegio: sposta la tassazione dal reddito netto al lordo. La Corte ha censurato l'incoerenza con il principio del reddito netto (sent. 262/2020 sull'IMU indeducibile) e i prelievi che colpiscono categorie a parità di capacità contributiva (sent. 223/2012). L'esclusione oggi prevista copre «salute, disabilità, famiglia, obblighi UE», ma **non gli elementi strutturali** dell'imposta sul lavoro e sulle pensioni.
2. **Delega (art. 76).** Il calendario ora sta in legge, ma la delega deve dire anche *che cosa* il Governo può fare alla scadenza: lasciar decadere, ridurre, trasformare. Deve indicare i criteri per chi scrive i decreti, i pareri parlamentari e la clausola sugli oneri (art. 17, c. 2, L. 196/2009). Una delega che rimette al Governo l'abrogazione di un insieme da 129,7 mld con criteri solo procedurali è esposta: la sent. 192/2024 ha censurato una delega sui LEP proprio per criteri troppo generici.
3. **Affidamento.** La salvezza delle rate maturate copre i bonus edilizi. Devono essere coperte anche le agevolazioni legate a investimenti già avviati con piani pluriennali, ad esempio il credito ZES. Il preavviso di 12 mesi rende la cessazione prevedibile: per la sent. 16/2017 la prevedibilità pesa a favore della legittimità.
4. **Vincolo sul rinnovo.** L'art. 3, comma 3, della scheda («il rinnovo è disposto con norma specifica, votata separatamente») non vincola il Parlamento futuro: è un auto-vincolo politico (artt. 64 e 72). Va presentato come tale.
5. **Collocazione.** La delega non può stare nella legge di bilancio (art. 21, c. 1-quinquies, L. 196/2009). La scheda prevede già un disegno di legge collegato: va mantenuto.

**Esito:** **dubbio serio** (punti 1 e 2). Regge se si accolgono le riformulazioni.

**Riformulazione (art. 2 della scheda):**
> «3. Sono escluse dalla cessazione automatica, ma non dalla valutazione: a) le detrazioni e le deduzioni che concorrono a determinare il reddito imponibile o l'imposta in ragione della natura del reddito, dei carichi di famiglia o degli oneri obbligatori per legge, ivi comprese le detrazioni di cui agli articoli [12 e 13 del testo unico] e la deduzione dei contributi previdenziali e assistenziali obbligatori; b) le agevolazioni relative a spese sanitarie, disabilità e non autosufficienza; c) le misure che attuano obblighi dell'Unione europea o accordi internazionali. 4. La cessazione non si applica alle quote di agevolazione relative a spese sostenute o a investimenti avviati prima della data di cessazione.»

## 2. 04-P3 PILOTA: «rivalutazione del Fondo TPL»

**La decisione.** Rivalutazione del Fondo TPL sull'IPCA al netto degli energetici importati, con un tetto nominale annuo (0,36 / 0,51 / 0,62 mld), un disegno quasi-sperimentale e il riparto d'intesa in Conferenza unificata.

**Il fatto nuovo.**
- L'art. 33 del d.lgs. 7 agosto 2026, n. 147 (verificato su Normattiva) sopprime dal 2027 il Fondo dell'art. 16-bis d.l. 95/2012, pari a 5.259,6 mln annui.
- Al suo posto c'è una compartecipazione regionale al gettito IRPEF, con aliquota fissata da un DPCM d'intesa entro il 31/12/2026.
- Il DDL di bilancio 2027 già registra la riduzione (-5 mld sul programma 13.6).
- La scheda e la decisione, scritte prima di questo quadro, presuppongono un fondo che non esisterà.

**Valutazione.**
- Il TPL è materia regionale residuale (sent. 222/2005). Dopo la fiscalizzazione, un nuovo trasferimento statale vincolato al TPL sarebbe un fondo a destinazione vincolata in materia regionale. È ammesso solo come risorsa aggiuntiva per scopi specifici (art. 119, quinto comma), con il coinvolgimento delle regioni (sent. 370/2003, 423/2004).
- L'intesa sul riparto, già prevista, è necessaria ma non basta: serve il titolo dell'art. 119, quinto comma, o la modifica dell'aliquota di compartecipazione.
- Anche la variante PIENA era già stata giudicata incompatibile (`giuridico/conformita.csv`: comando di dettaglio sulle tariffe).
- *Esito:* **dubbio serio**. Diventa **illegittimità probabile** se la misura è attuata come nuovo fondo statale vincolato senza intesa né titolo dell'art. 119, quinto comma.

**Riformulazione.** Due strade conformi:
- **(a) Indicizzazione della compartecipazione.** «A decorrere dall'anno 2028, l'aliquota di compartecipazione di cui all'articolo 2, comma 1, del decreto legislativo 6 maggio 2011, n. 68, è rideterminata, con il procedimento ivi previsto, in misura tale da assicurare un gettito pari a quello dell'anno precedente rivalutato secondo l'indice [IPCA al netto degli energetici importati], nel limite di [importi] milioni di euro.»
- **(b) Pilota con risorse aggiuntive (art. 119, quinto comma).** Fondo sperimentale per obiettivi di servizio (frequenze e affidabilità sulle linee pendolari) per le sole regioni che aderiscono, con riparto d'intesa e criteri in legge.

In entrambi i casi l'area 04 deve aggiornare la scheda al d.lgs. 147/2026.

## 3. Coperture «certificate» e spesa a gradini (art. 81)

**Il modello del Consiglio.** Per prudenza finanziaria, molte decisioni scelgono la variante bassa e salgono dopo una certificazione della Ragioneria. Esempi:
- 07-C1: si sale alla PIENA «con atto ricognitivo» dopo la certificazione del contributo unificato maggiorato;
- 09-C3: si sale alla PIENA dopo tre certificazioni;
- 05-C1: la platea si ferma all'ESSENZIALE se la quota certificata è sotto 0,17 mld;
- 02-C2: «RB03 solo se il DDL 2027 passa così com'è»; il resto su spese fiscali «riconciliate»;
- 05-C2: la dote si riduce in proporzione.

**Il parametro.**
- Ogni legge che importa nuovi oneri indica i mezzi per farvi fronte (art. 81, terzo comma). La copertura deve essere contestuale, certa e quantificata per anno (sent. 1/1966, 70/2012, 26/2013).
- La spesa si autorizza per legge: un atto amministrativo non può aumentarla oltre il limite autorizzato.
- Una copertura che dipende dall'approvazione di un'altra legge non è contestuale, salvo che le due norme stiano nello stesso atto.

**Valutazione.**
- Il modello è prudente e, scritto bene, è legittimo. La forma corretta esiste già: limite massimo di spesa, condizione accertata dalla Ragioneria e clausola di salvaguardia (art. 17, c. 12, L. 196/2009).
- È illegittimo se l'«atto ricognitivo» viene usato per autorizzare spesa nuova, o se la PIENA viene contata senza che la sua copertura sia nella legge.
- È fragile, per 02-C2, la copertura condizionata all'esito di un'altra legge.
- *Esito:* **dubbio serio**, trasversale.

**Riformulazione tipo:**
> «È autorizzata la spesa di [ESSENZIALE] milioni di euro per l'anno 2027 e, nel limite massimo complessivo di [PIENA] milioni di euro annui a decorrere dall'anno 2028, subordinatamente all'accertamento, con decreto del Ministro dell'economia e delle finanze da adottare entro il 31 marzo di ciascun anno, delle maggiori entrate derivanti dall'articolo [x] della presente legge in misura non inferiore a [y] milioni di euro. In caso di accertamento inferiore, il limite è ridotto in proporzione.»

La norma che produce le maggiori entrate (riordino delle spese fiscali, SAD, accise) sta **nella stessa legge**. Le coperture che dipendono dal DDL 2027 si scrivono come emendamenti a quel DDL o si sostituiscono.

## 4. Altri rilievi

| Misura | Esito | Problema | Correttivo |
|---|---|---|---|
| **09-C8 ESSENZIALE**: modifica dell'art. 6 d.lgs. 165/2001 (decisione motivata su ogni cessazione) «anticipata alla legge di bilancio 2027» | Dubbio serio sullo strumento; rischio basso sul merito | È una norma ordinamentale senza effetti finanziari diretti: è esclusa dal contenuto della legge di bilancio (art. 21, c. 1-quinquies, L. 196/2009). Lo dimostra lo stralcio dell'A.C. 3174 del 4/11/2026. Nel merito rafforza la motivazione (art. 97) | Collegato alla manovra o disegno di legge sulla PA; nella legge di bilancio solo il Fondo per le assunzioni anticipate |
| **01-P1, 08-P1, 04-P4, 02-C6**: nuove funzioni dell'UPB o uffici presso l'UPB | Rischio basso se le condizioni sono rispettate; illegittimità probabile in caso contrario | La L. 243/2012 si modifica solo in modo espresso e a maggioranza assoluta (art. 81, sesto comma; sent. 88/2014). Per 08-P1 serve anche l'intesa con le Camere (art. 64; sent. 129/1981, 120/2014). Le condizioni sono già nelle decisioni | Un solo disegno di legge «UPB», separato dalla legge di bilancio e approvato a maggioranza assoluta. 02-C3, art. 5, comma 2 («ogni DDL previdenziale è accompagnato da una relazione dell'UPB») va nello stesso testo |
| **02-C3 ESSENZIALE**: copertura con rivalutazione al 50% oltre 6 volte il minimo, dal 2030 e in via permanente | Dubbio serio, attenuato | Una perequazione parziale permanente sulle pensioni medio-alte può essere legittima se graduata. La Corte ha valutato i tagli temporanei (sent. 70/2015, 250/2017, 234/2020, 19/2025, 52/2026) e avverte sulla reiterazione. Sommata ai tagli 2023-2024 e al 2027 (art. 55 della manovra), il 50% senza fasce intermedie rischia una perdita cumulata sproporzionata | Fasce graduate (per esempio 75% tra 6 e 8 volte il minimo, 50% oltre), clausola di salvaguardia del potere d'acquisto dopo N anni, relazione INPS sulla perdita cumulata per fascia |
| **06-C1 ZERO**: agenda unica CUP con il privato accreditato, divieto di agende chiuse, sospensione dell'intramoenia nelle aziende inadempienti | Dubbio serio sullo strumento | Tocca l'organizzazione sanitaria regionale (art. 117, terzo comma). Il CSV indica un DM, ma obblighi alle Regioni e sospensione dell'intramoenia richiedono la legge e poi un DM d'intesa (`conformita.csv`). La sent. 114/2025 ha censurato limiti statali sul personale sanitario che condizionavano le Regioni oltre i principi | Norma di principio in legge; DM d'intesa in Conferenza Stato-Regioni; sospensione dell'intramoenia come potere sostitutivo graduato (diffida, art. 120) con salvezza dei contratti in essere |
| **02-C2 ESSENZIALE**: Fondo nidi per il LEP del 33% | Rischio basso, a condizione | La sent. 182/2026 conferma che standard e riparto dei LEP in materie intrecciate richiedono l'**intesa**: va mantenuta. Per la copertura vedi il punto 3 | Intesa in Conferenza unificata su riparto e standard; copertura nella stessa legge |
| **01-P10 ESSENZIALE / 01-P3 ESSENZIALE**: analisi del rischio sui dati fiscali; blocco preventivo motivato fino a 30 giorni | Rischio basso, a condizione | Trattamenti massivi di dati: servono base di legge, proporzionalità e garanzie (sent. 20/2019 sul bilanciamento tra trasparenza e riservatezza; art. 8 CEDU). Il blocco preventivo tocca artt. 24 e 41: regge se motivato, breve, impugnabile e deciso da una persona | Statuto delle garanzie in legge prima dell'avvio, già deciso; ricorso rapido contro il blocco; criteri di rischio pubblicati in forma aggregata |
| **01-P6 ZERO**: vincolo del 50% del gettito dell'imposta di soggiorno | Rischio basso | Il vincolo alla spesa comunale è coordinamento della finanza pubblica (artt. 117, terzo comma, e 119). Regge se proporzionato e se lascia ai Comuni la scelta tra gli impieghi ammessi | Elenco ampio di impieghi; nessun obbligo di dettaglio; parere della Conferenza Stato-città |
| **05-C2, 06-C2, 07-C2**: deleghe | Rischio basso | I criteri ci sono, ma scritti come «princìpi» generici o elenchi: lo screening li ha segnalati. Per 05-C2 serve l'intesa sugli schemi (sent. 251/2016); per 06-C2 vanno precisati gli ambiti della prescrizione infermieristica | «Princìpi e criteri direttivi» numerati e specifici, termine con decorrenza, pareri parlamentari, intesa dove ci sono competenze regionali |
| **07-C1 ESSENZIALE**: concorso riservato per gli addetti all'Ufficio per il processo (UPP); contributo unificato maggiorato per i grandi litiganti | Rischio basso | La riserva è ammessa se selettiva e riservata a chi è entrato per selezione pubblica (sent. 293/2009, 37/2015). Il contributo maggiorato è legittimo se non rende eccessivamente difficile agire (art. 24; cfr. sent. 137/2026) | Soglia oggettiva di «grande litigante»; esenzioni per i diritti fondamentali |
| **03-P2 ESSENZIALE**: aree idonee con potere sostitutivo; silenzio-assenso paesaggistico | Dubbio serio sul silenzio-assenso | Il potere sostitutivo è coerente con la sent. 28/2025 e la sent. 184/2025. Il silenzio-assenso sugli atti paesaggistici contrasta con l'art. 9 (`conformita.csv`) | Parere paesaggistico obbligatorio non vincolante con termine perentorio, esclusi i beni vincolati |
| **06-C6 ZERO**: ripiano farmaceutico tramite accordi negoziali | Rischio basso | Coerente con la sent. 140/2024 (proporzionalità e prevedibilità) | Criteri degli accordi in legge |

Le altre misure adottate non presentano rilievi costituzionali ulteriori rispetto a `giuridico/conformita.csv`.

## 5. Confronto con la manovra del Governo

- **Rischi simili.**
  - Entrambi i testi tendono a mettere nella legge di bilancio norme ordinamentali (A.C. 3174: stralcio; GovernAI: 09-C8).
  - Entrambi incidono sulla rivalutazione delle pensioni (art. 55; 02-C3).
  - Entrambi ignorano, o non hanno ancora recepito, novità che cambiano il quadro:
    - la manovra non recepisce la sent. 182/2026 sui LEP;
    - GovernAI non recepisce il d.lgs. 147/2026 sul TPL.
- **Rischi diversi.**
  - La manovra è più esposta sul piano tributario (prelievo settoriale e divieto di traslazione) e sul disavanzo (art. 81, secondo comma).
  - GovernAI è più esposto sulla struttura delle coperture (art. 81, terzo comma), proprio perché sceglie di non spendere a deficit e lega la spesa a entrate da certificare.
- **Lezione comune.** Ogni nuova misura va confrontata con le leggi e le sentenze dell'ultimo trimestre. Lo screening automatico degli atti della Gazzetta (`controllo.py --gu`) serve a questo.

## Azioni richieste (mandati proposti)

1. **Area 01.** Riformulare 01-P2 con l'esclusione degli elementi strutturali e i criteri di delega completi (sezione 1).
2. **Area 04.** Riscrivere 04-P3 sul nuovo quadro del d.lgs. 147/2026, via (a) o (b) (sezione 2).
3. **Ragioneria e tutte le aree.** Convertire le «salite con atto ricognitivo» nella forma «limite massimo condizionato» (sezione 3) e portare le coperture nella stessa legge.
4. **Area 09.** Spostare la parte normativa di 09-C8 in un collegato.
5. **Area 08 e mandato M005.** Un solo disegno di legge «UPB» a maggioranza assoluta per 01-P1, 08-P1, 04-P4, 02-C6 e 02-C3 (art. 5, comma 2).
6. **Area 02.** Graduare la copertura di 02-C3.
7. **Area 06.** Veicolo legislativo e intesa per 06-C1.
