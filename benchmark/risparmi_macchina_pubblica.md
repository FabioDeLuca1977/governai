# Risparmi nella macchina pubblica: nuove coperture possibili (RA30-RA33)

*Bozza scritta da un agente AI il 15 novembre 2026; da valutare con il panel e da approvare; non rivista da una persona.*

File collegato: `benchmark/bozza_risparmi_macchina_pubblica.csv` (4 righe, stessa intestazione di `programma/coperture_menu.csv`, colonne dei valori vuote).

## In breve

- **Il campo è già quasi tutto coperto.** Il menu ha già queste coperture, che toccano lo stesso perimetro:
  - acquisti centralizzati (RA01) e locazioni passive (RA02);
  - consulenze e auto di servizio (RA03) e assistenza tecnica (RA08);
  - spesa ICT dei ministeri (RA09) e revisione generale dei ministeri (RA13);
  - sedi (RP05), enti minori (RP04), beni e servizi di INPS e INAIL (RP06) e partecipate locali (RP07).

  Le verifiche del 13 e 14 novembre le hanno già ridotte molto. Un'altra copertura su "acquisti", "affitti" o "ICT" dello Stato sarebbe quasi solo un doppio conteggio.
- **Abbiamo cercato voci che il menu non tocca.** Le abbiamo prese dai capitoli del rendiconto 2025 e dalle leggi in vigore, con un flusso di cassa che la Ragioneria può certificare. Ne restano quattro.

| ID | In una riga | Gettito (mld/anno) | A regime | Livello |
|---|---|---|---|---|
| RA30 | Contributo di Regioni ed enti locali 2030-2033, legato agli acquisti, versato allo Stato | 0,5-0,9 | 2030 | 2 |
| RA31 | Interessi pagati a Poste sulla liquidità delle PA nei conti postali: tesoreria unica e tasso più basso | 0,03-0,10 | 2029 | 2 |
| RA32 | Canoni delle concessioni balneari legati al valore, più la riscossione dei canoni non versati | 0,03-0,10 | 2029 | 2 |
| RA33 | Custodia dei veicoli sequestrati: custode-acquirente ovunque, vendita o rottamazione rapida | 0,015-0,03 | 2029 | 1 |
| **Totale** | | **0,58-1,13** | | |

Quasi tutto il gettito viene da RA30. È una scelta politica (chi paga sono gli enti territoriali) e ha un vincolo costituzionale: è da valutare con attenzione. Senza RA30 restano 0,08-0,23 mld.

## Metodo

1. Abbiamo letto `programma/coperture_menu.csv`, `benchmark/verifica_coperture_rendiconto.md`, `benchmark/verifica_coperture_restanti.md`, `benchmark/nord_europa_efficienza_spesa.md` e `motore/rubrica.md`.
2. Abbiamo interrogato il rendiconto 2025 per capitolo (`dati/raw/00b_openbdap_rendiconto_2025_spese_capitolo.csv`, colonna "Totale CP" = impegni). Abbiamo cercato capitoli di funzionamento **fuori** dalle basi già usate: i 7,44 mld di spesa acquistabile di RA01, gli 0,15 mld di fitti di RA02, i 59 mln di consulenze di RA03, l'ICT di RA09.
3. Per Regioni ed enti locali abbiamo cercato solo meccanismi che riportano il risparmio allo Stato per legge. Li abbiamo trovati nei contributi alla finanza pubblica delle leggi 213/2023 e 207/2024 e nella relazione tecnica del DDL 2027.
4. Fonti esterne: Corte costituzionale, Corte dei conti, Ministero dell'interno. Due fonti non sono ufficiali e lo segnaliamo nel CSV: un articolo di stampa sulla convenzione MEF-Poste e una nota dell'Osservatorio CPI.
5. Le stime sono prudenti. I minimi contano solo la parte che si vede nei capitoli o nelle leggi.

## Le proposte

### RA30 - Contributo degli enti territoriali dopo il 2029, legato agli acquisti

- **Fatto.** Oggi Regioni ed enti locali versano due contributi alla finanza pubblica:
  - legge 213/2023: 350 mln l'anno per le Regioni e 250 per gli enti locali, dal 2024 al 2028;
  - legge 207/2024, commi 786 e 788: nel 2029 valgono 1.310 mln per le Regioni, 440 per i comuni e 50 per province e città metropolitane, in tutto 1,8 mld.

  **Dal 2030 non c'è niente**, quindi il tendenziale non lo conta. La Corte costituzionale ha accettato questi contributi perché sono temporanei e ragionevoli (sentenze 195/2024, 45/2025 e 152/2025).
- **Fatto.** Il DDL 2027 (art. 128) trasforma il versamento in accantonamento. La sua relazione tecnica calcola l'effetto per gli enti locali: rinunciare a 600 mln l'anno di versamento nel 2027-2028 costa 1.049 mln di indebitamento netto nel 2028-2034. Il motivo è che le somme accantonate tornano come investimenti.
- **Proposta.** Un nuovo contributo per il 2030-2033, pari al 28-50% del livello 2029:
  - si calcola sulla spesa per beni e servizi non sanitari;
  - è più basso per chi compra tramite soggetti aggregatori e prezzi di riferimento ANAC;
  - si **versa** allo Stato o si **trattiene** sui trasferimenti, senza accantonamento;
  - sono esclusi il SSN (già in RA06), gli enti in dissesto o in riequilibrio e i comuni più piccoli.
- **Chi paga.** Regioni ed enti locali, con meno spesa corrente o meno investimenti propri.
- **Perché qui.** È l'unico meccanismo esplicito che fa tornare allo Stato i risparmi di acquisto degli enti territoriali. Senza un meccanismo così, quei risparmi non si possono contare (regola del mandato).

### RA31 - Liquidità delle amministrazioni pubbliche nei conti postali

- **Fatto.** Nel rendiconto 2025 c'è il cap. 2316 MEF, "remunerazione delle giacenze dei conti correnti postali": 550 mln impegnati, 405 pagati. Lo Stato paga interessi a Poste sulla liquidità che le amministrazioni tengono nei conti postali e che Poste impiega presso il MEF. La convenzione MEF-Poste è biennale; quella del 2023-2024 è citata dalla stampa, il testo va acquisito.
- **Proposta.** Al rinnovo della convenzione:
  - gli enti già soggetti a tesoreria unica spostano lì la liquidità che non serve agli incassi;
  - il tasso riconosciuto sulle giacenze che restano scende.
- **Stima.** La spesa lorda scende del 20-50%. Si tolgono poi le minori imposte di Poste e i minori dividendi pubblici: il MEF ha il 29,3% di Poste e CDP il 35%. Restano 30-100 mln netti.
- **Chi paga.** Poste Italiane e, in parte, gli azionisti pubblici.

### RA32 - Canoni delle concessioni balneari

- **Fatto (Corte dei conti, memoria sul DL 131/2024).**
  - Nel 2023 sono stati chiesti canoni per quasi 150 mln. Il Ministero ha comunicato versamenti per quasi 120 mln su 24.658 concessioni; l'amministrazione finanziaria ha incassato circa 151 mln, 155 con i codici paralleli MA12 e MA13.
  - Il canone medio è di circa 6.000 euro l'anno.
  - Nel 2024 i canoni unitari sono stati ridotti del 4,5%.
- **Fatto, da fonte non ufficiale.** Secondo l'Osservatorio CPI, il decreto sui nuovi canoni previsto dal DL 131/2024, in scadenza il 31/3/2025, non è ancora stato adottato.
- **Proposta.** Adottare il decreto, con canoni legati al valore e alla redditività dell'area, da applicare alle concessioni assegnate con le gare. Riscuotere in via coattiva i canoni chiesti e non versati.
- **Stima.** 30-100 mln.
- **Attenzione.** È un'entrata da patrimonio, non un taglio. Come RA10, è imputata a RIALLOCAZIONE: il panel può spostarla nell'area fiscale.

### RA33 - Custodia dei veicoli sequestrati

- **Fatto.** Nel rendiconto 2025 c'è il cap. 2952 dell'Interno, "estinzione dei debiti per la custodia dei veicoli sequestrati": 108,6 mln impegnati. Una circolare dell'Interno del 2019 segnala tempi di giacenza lunghi nelle depositerie. Esiste già il custode-acquirente (art. 214-bis del Codice della strada), ma non si applica dappertutto.
- **Proposta.**
  - custode-acquirente obbligatorio in tutte le province;
  - vendita o rottamazione d'ufficio quando la custodia costa più del veicolo;
  - censimento digitale previsto dall'art. 215-bis del Codice della strada.
- **Stima.** 15-30 mln netti, oltre RA01.

## Doppi conteggi: come li abbiamo trattati

| Copertura esistente | RA30 | RA31 | RA32 | RA33 |
|---|---|---|---|---|
| RA01 acquisti dello Stato | nessuno: RA01 riguarda solo lo Stato | nessuno: interessi, CE 9.2.2, fuori dalla base di RA01 | nessuno: è un'entrata | **sì, piccolo**: il cap. 2952 sta nella spesa acquistabile di RA01. Tolti 1-3 mln (1-2,5% di 108,6) |
| RA02 locazioni passive | nessuno | nessuno | nessuno | nessuno |
| RA03 consulenze e auto | nessuno | nessuno | nessuno | nessuno |
| RA06 acquisti del SSN | escluso il SSN, quindi nessuno | nessuno | nessuno | nessuno |
| RA08 assistenza tecnica | nessuno | nessuno | nessuno | nessuno |
| RA09 ICT | nessuno | nessuno | nessuno | nessuno |
| RA13 revisione dei ministeri | nessuno: enti territoriali | nessuno: gli oneri del debito non sono nella revisione | nessuno | **il cap. 2952 va escluso dalla base di RA13**, con la stessa regola proposta in `verifica_coperture_rendiconto.md` |
| RP07 partecipate locali | possibile, ma piccolo: se gli enti usano i risparmi sulle partecipate per pagare RA30, quella parte di RP07 non si conta | nessuno | nessuno | nessuno |

## Rischi

- **RA30.** La Corte costituzionale vuole contributi temporanei e proporzionati. Dieci anni di seguito (2024-2033) possono essere letti come strutturali: serve un limite chiaro e il legame con l'efficienza degli acquisti. C'è anche il rischio di tagli ai servizi locali e di conflitto con ANCI, UPI e Regioni. Se la legge sceglie l'accantonamento invece del versamento, l'effetto sul deficit si perde in gran parte.
- **RA31.** Poste è quotata in borsa. Una remunerazione più bassa riduce i suoi utili, e Poste può chiedere più compensazioni per il servizio universale. Alcuni enti usano i conti postali per gli incassi: il passaggio a pagoPA richiede tempo.
- **RA32.** Il tema è molto conflittuale. Ci sono contenziosi, e gli indennizzi ai gestori uscenti possono ridurre il netto nei primi anni.
- **RA33.** Contenzioso con le depositerie sulle tariffe già maturate. Una parte del capitolo paga debiti vecchi.

## Cosa non sappiamo

- **RA30.** Se il quadro di finanza pubblica già ipotizza contributi dopo il 2029. In legge non ci sono. Non sappiamo neppure come la Ragioneria tratterebbe una trattenuta sui trasferimenti alle Regioni.
- **RA31.** Il testo e il tasso della convenzione MEF-Poste in vigore, le giacenze per tipo di ente, e se il cap. 2316 scende già nel 2027-2029.
- **RA32.** Se il tendenziale conta già un aumento automatico per la mancata adozione del decreto: la stampa lo cita, ma non l'abbiamo verificato nel testo. Mancano anche i canoni in contenzioso e il gettito per regione.
- **RA33.** La parte del capitolo che paga debiti pregressi e il numero di veicoli in deposito.

## Idee scartate

| Idea | Perché l'abbiamo scartata |
|---|---|
| Altri tagli ad acquisti centralizzati, auto di servizio, consulenze, ICT, affitti dei ministeri | Già in RA01, RA02, RA03, RA08 e RA09, ridotte dalle verifiche. Una nuova riga sarebbe un doppio conteggio |
| Prezzi di riferimento ANAC e differenze di prezzo nel SSN | Già in RA06. Fuori dal SSN, il risparmio degli enti torna allo Stato solo con RA30 |
| Interessi per ritardati rimborsi fiscali (cap. 4015-4016 MEF, 447 mln nel 2025) | La base è grande, ma il risparmio dipende dalla velocità dei rimborsi: è un'efficienza attesa, non un taglio certificabile. Rimborsare prima costa cassa nell'anno del passaggio. Abbassare il tasso pagato ai contribuenti non è efficienza. Da approfondire con l'Agenzia delle entrate |
| Prezzi delle forniture del Poligrafico (cap. 2189, 2188 e 1340 MEF, circa 0,4 mld) | Il Poligrafico è al 100% del MEF: un prezzo più basso riduce il suo utile e quindi il dividendo allo Stato. Il risparmio netto è vicino a zero |
| Commissioni sul collocamento dei titoli di Stato (cap. 2247 e 2242, circa 0,96 mld) | È gestione del debito, cioè lavoro del Tesoro, e il capitolo comprende le commissioni sui buoni postali. Da girare all'area conti pubblici |
| Riacquisto degli immobili dei fondi FIP e FP1 (196 mln di canoni l'anno) | L'acquisto di immobili da privati è spesa in conto capitale: peggiora il deficit di miliardi nell'anno dell'operazione. In parte è già nel perimetro di RA02 |
| Vendita di immobili pubblici | Una tantum: non conta come copertura permanente |
| Concessione o affitto di immobili statali inutilizzati | Gli incassi noti sono piccoli (circa 50 mln, dati sui livelli di servizio del Demanio) e già gestiti. Manca una base certa per un aumento |
| Fondo unico giustizia e beni confiscati | Flusso variabile, già destinato per legge a Interno e Giustizia, e in parte usato da 07-C4. Non abbiamo trovato i dati 2025 alla fonte |
| Dotazioni degli organi costituzionali (Camera 943 mln, Senato 506, Quirinale 230, Corte costituzionale 68) | Le dotazioni di Camera e Senato sono ferme da anni, quindi non c'è crescita da fermare. Gli organi costituzionali hanno autonomia: lo Stato non può certificare un taglio per legge |
| Accorpamenti di enti strumentali (Formez e SNA, ENIT e ICE) | Si sovrappone a RP04. I risparmi stimabili sono sotto i 10 mln e incerti |
| Agenzie fiscali: convenzioni e costi di funzionamento | Le agenzie sono già soggette ai tetti della L. 160/2019 (cc. 590-594) e versano allo Stato il loro avanzo: 540 mln nel 2023 per l'Agenzia delle entrate (relazione del collegio dei revisori). In più si sovrappone a RA09 e RA13 |
| Intercettazioni (cap. 1363 Giustizia, 298 mln nel 2025) | Il listino del DM 6/10/2022 è già in vigore, la spesa cresce per i volumi e c'è un rischio per la sicurezza (SIC). Lo lasciamo all'area 07 |
| Remunerazione delle giacenze di Poste come strumento di debito in generale | Teniamo solo la parte di liquidità pubblica (RA31). Il resto è gestione del debito |
| Affitti pagati dai ministeri a INPS, INAIL o Demanio | Sono pagamenti tra amministrazioni pubbliche, neutri sul conto consolidato. **Avviso per RA02:** il -20% sui canoni va calcolato solo sugli affitti pagati a privati e ai fondi FIP/FP1 |

## Fonti

- OpenBDAP-RGS, Rendiconto 2025 per capitolo: `dati/raw/00b_openbdap_rendiconto_2025_spese_capitolo.csv` (capitoli 2316, 4015, 4016, 2189, 2247, 2242 MEF; 2952 Interno; 1363 Giustizia).
- DDL di bilancio 2027 A.C. 3174, relazioni illustrativa e tecnica, artt. 127-128: `dati/raw/00b_ddl_bilancio_2027_AC3174_relazioni.txt`.
- Corte costituzionale, sentenza 152/2025: https://www.cortecostituzionale.it/scheda-pronuncia/2025/152 ; sentenza 195/2024: https://www.cortecostituzionale.it/scheda-pronuncia/2024/195 ; sentenza 45/2025: https://www.cortecostituzionale.it/scheda-pronuncia/2025/45
- Corte dei conti, Sezioni riunite in sede di controllo, Memoria sul DL 131/2024 (settembre 2024): https://documenti.camera.it/leg19/documentiAcquisiti/COM06/Progettodilegge/leg19.com06.Progettodilegge.Contributo%20Scritto.PUBBLICO.ideGes.45276.27-09-2024-16-39-25.465.pdf
- Osservatorio CPI, concessioni balneari (fonte non ufficiale): https://osservatoriocpi.unicatt.it/ocpi-pubblicazioni-concessioni-balneari-riforma-incompleta-e-canoni-da-adeguare
- Ministero dell'interno, circolare del 25/1/2019 sulla custodia dei veicoli: https://dait.interno.gov.it/documenti/circ-utg-autoloca-prot1582-25-01-2019.pdf
- Convenzione MEF-Poste 2023-2024 (stampa, da verificare): https://www.websim.it/azioni/blue-chip/poste-italiane-remunerazione-in-aumento-sui-conti-postali-della-pubblica-amministrazione-20230830051554/
- Agenzia delle entrate, Relazione del collegio dei revisori al bilancio 2023: https://www.agenziaentrate.gov.it/portale/documents/20143/5305375/All.+5+Relazione+del+Collegio+dei+Revisori+dei+Conti+al+Bilancio+d%E2%80%99esercizio+2023.pdf/4fa0702c-4122-2992-6373-d64ffa077ffa
