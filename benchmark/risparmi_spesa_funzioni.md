*Bozza scritta da un agente AI con il ruolo di esperto di finanza pubblica (spending review) il 15 novembre 2026; da valutare con il panel e con la verifica giuridica; non rivista da una persona.*

# Spesa per funzione: dove l'Italia spende più dei Paesi simili, e che cosa si può tagliare davvero

Legenda: **[Fatto]** con fonte; **[Stima]** calcolo proprio con ipotesi scritte; **[Valutazione]** giudizio dell'autore. Le righe proposte sono in `benchmark/bozza_risparmi_spesa_funzioni.csv` (RA50-RA52).

## In breve

- **Senza interessi e pensioni, l'Italia spende meno degli altri, non di più.** Nel 2024 la spesa pubblica totale è al 50,4% del PIL, ma si scende al **30,1%** togliendo interessi (4,0), vecchiaia (13,9) e superstiti (2,4). Con lo stesso calcolo la media UE è al 34,9%, la Germania al 36,5% e la Spagna al 30,4% [Stima su Eurostat].
- **I pochi scarti veri stanno quasi tutti fuori dal perimetro utile:**
  - sussidi ai trasporti: esclusi dall'incarico, e il programma li vuole aumentare;
  - crediti d'imposta all'industria: in esaurimento o già nel tendenziale;
  - Superbonus: crediti già maturati;
  - rifiuti: spesa locale pagata con la TARI;
  - polizia: scarto piccolo, e un taglio peserebbe sulla sicurezza.
- **Molte voci classiche della spending review (Cottarelli 2014, Giarda) sono già fatte o già nel programma:**
  - Consip (RA01);
  - auto blu e consulenze (RA03);
  - affitti (RA02);
  - partecipate (RP07);
  - Corpo forestale, assorbito nei Carabinieri nel 2016;
  - incentivi alle imprese (RA04, RA14).
- **Proposte: 3, piccole ma certificabili.** Insieme valgono **0,06-0,12 mld l'anno** a regime (2029-2030). Sono tagli di capitoli precisi del rendiconto 2025, al netto di RA04.
- **[Valutazione] Da questo ambito non arrivano miliardi.** I 5,3 mld mancanti vanno cercati sulle entrate e sulle spese fiscali, oppure riducendo le misure. Non negli sprechi per funzione.

## Metodo

1. **Confronto per funzione.** Fonte: Eurostat, `gov_10a_exp` (COFOG), interrogato via API il 15/11/2026 (aggiornamento del 21/10/2026). Settore: amministrazioni pubbliche (S13). Anni 2023 e 2024, in % del PIL. Transazioni guardate:
   - spesa totale (TE);
   - redditi da lavoro (D1);
   - consumi intermedi (P2);
   - sussidi (D3).

   Paesi: Francia, Germania, Spagna, Paesi Bassi, Austria, Svezia, Danimarca, Portogallo e UE27. Agenti di polizia: Eurostat, `crim_just_job`.
2. **Ricerca dei capitoli.** Per ogni funzione in cui l'Italia è sopra la media, abbiamo cercato i capitoli corrispondenti nel rendiconto 2025 dello Stato. Fonte: OpenBDAP, impegni di competenza, `dati/raw/00b_openbdap_rendiconto_2025_spese_capitolo.csv`. Il metodo è quello di `verifica_coperture_rendiconto.md`: le voci si classificano per categoria e per codice economico, non per parole nel titolo.
3. **Controlli su ogni voce:**
   - che non sia già nel tendenziale. Fonti: DDL di bilancio 2027 A.C. 3174, relazioni illustrativa e tecnica; DPB 2027;
   - che non si sovrapponga alle 73 coperture di `programma/coperture_menu.csv`;
   - che non tocchi LEA, LEP o diritti.
4. **Che cosa abbiamo contato.** Solo i tagli di stanziamento decisi per legge. Niente efficienze attese e niente recupero di evasione.

## Il confronto (Eurostat COFOG, % del PIL, 2024 salvo dove indicato)

| Funzione (codice COFOG) | IT | FR | DE | ES | NL | AT | SE | DK | PT | UE27 | Lettura |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Spesa totale** | 50,4 | 57,3 | 49,4 | 45,5 | 44,4 | 55,2 | 50,0 | 47,3 | 42,4 | 48,8 | |
| Interessi (01.7) | **4,0** | 2,0 | 1,1 | 2,5 | 0,7 | 1,7 | 0,8 | 0,8 | 2,2 | 1,9 | escluso |
| Vecchiaia (10.2) | **13,9** | 13,4 | 9,9 | 10,4 | 6,1 | 14,3 | 10,9 | 7,2 | 10,8 | 10,6 | escluso (pensioni) |
| Superstiti (10.3) | **2,4** | 1,4 | 1,9 | 2,2 | 0,0 | 1,4 | 0,1 | 0,0 | 1,7 | 1,4 | escluso (pensioni di reversibilità) |
| **Resto della spesa** [Stima] | **30,1** | 40,5 | 36,5 | 30,4 | 37,6 | 37,8 | 38,2 | 39,3 | 27,7 | 34,9 | l'Italia è sotto la media |
| Organi esecutivi, affari finanziari e fiscali (01.1) | 2,0 | 1,5 | 2,1 | 1,3 | 2,0 | 2,1 | 1,9 | 1,7 | 3,0 | 1,9 | in media; consumi intermedi 0,4 contro 0,3 (aggi sui giochi, compensi CAF) |
| Difesa (02) | 1,3 | 1,9 | 1,4 | 0,9 | 1,6 | 0,7 | 1,9 | 1,8 | 0,9 | 1,5 | sotto la media; personale 0,7 contro 0,6, consumi intermedi 0,1 contro 0,4 |
| Polizia (03.1) | 1,0 | 1,0 | 0,8 | 1,1 | 0,8 | 0,7 | 0,8 | 0,5 | 0,9 | 0,9 | poco sopra; consumi intermedi 0,2 contro 0,1 |
| Tribunali (03.3) | 0,4 | 0,3 | 0,4 | 0,3 | 0,3 | 0,3 | 0,3 | 0,2 | 0,3 | 0,3 | poco sopra |
| Affari economici (04) | 5,1 | 5,7 | 5,4 | 5,1 | 4,4 | 7,1 | 4,8 | 3,1 | 3,6 | 5,3 | in media |
| di cui sussidi (D3) | **1,6** | 1,8 | 0,9 | 1,1 | 0,8 | 1,5 | 1,0 | 0,9 | 0,5 | 1,2 | sopra |
| Sussidi ai trasporti (04.5, D3) | **0,6** | 0,5 | 0,1 | 0,3 | 0,2 | 0,2 | 0,4 | 0,4 | 0,1 | 0,3 | sopra; escluso (FS, TPL, continuità territoriale) |
| Industria e costruzioni (04.4) | **0,5** | 0,1 | 0,2 | 0,2 | 0,0 | 0,0 | 0,1 | 0,0 | 0,2 | 0,2 | sopra (crediti d'imposta; 0,8 nel 2023) |
| Rifiuti (05.1), consumi intermedi | **0,5** | 0,3 | 0,1 | 0,4 | 0,3 | 0,0 | 0,1 | 0,0 | 0,1 | 0,2 | sopra; spesa dei comuni pagata con la TARI |
| Sviluppo abitativo (06.1) | **0,4** | 0,3 | 0,1 | 0,2 | 0,3 | 0,2 | 0,2 | 0,3 | 0,2 | 0,2 | sopra (Superbonus; 4,1 nel 2023) |
| Sanità (07) | 6,6 | 8,9 | 7,6 | 6,5 | 7,3 | 9,5 | 7,4 | 8,3 | 6,8 | 7,3 | sotto |
| Cultura (08.2) | 0,3 | 0,6 | 0,4 | 0,5 | 0,4 | 0,6 | 0,5 | 0,6 | 0,3 | 0,5 | sotto |
| Radio, TV, editoria (08.3) | 0,1 | 0,3 | 0,3 | 0,2 | 0,1 | 0,3 | 0,2 | 0,2 | 0,1 | 0,2 | sotto |
| Istruzione (09) | 4,0 | 5,1 | 4,5 | 4,1 | 5,1 | 5,3 | 7,2 | 5,6 | 4,3 | 4,7 | sotto |
| Malattia e disabilità (10.1) | 1,7 | 2,9 | 3,3 | 2,8 | 4,3 | 1,8 | 3,5 | 4,8 | 1,1 | 2,8 | sotto |
| Famiglia (10.4) | 1,5 | 2,3 | 1,9 | 1,0 | 2,4 | 2,1 | 2,3 | 4,1 | 1,8 | 2,0 | sotto |

Altri indicatori:

| Indicatore | IT | FR | DE | ES | NL | AT | SE | DK | PT |
|---|---|---|---|---|---|---|---|---|---|
| Agenti di polizia ogni 100.000 abitanti (Eurostat `crim_just_job`) | 399 (2020) | 361 (2022) | 320 (2024) | 379 (2024) | 291 (2024) | 358 (2024) | 226 (2024) | 194 (2024) | 438 (2024) |

Fonti:

- Eurostat, `gov_10a_exp`: https://ec.europa.eu/eurostat/databrowser/view/gov_10a_exp/default/table
- API: https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/gov_10a_exp
- Eurostat, `crim_just_job`: https://ec.europa.eu/eurostat/databrowser/view/crim_just_job/default/table

Per l'Italia gli agenti dopo il 2020 non sono pubblicati.

## Le proposte

### RA50. Ippica: meno sovvenzioni dal bilancio dello Stato (0,025-0,05 mld, a regime nel 2030)

- **Che cosa.** Le sovvenzioni del MASAF al settore ippico scendono del 25-40% in 3 anni dal 2028. I capitoli sono due:
  - cap. 2295, interventi per lo sviluppo del settore ippico (montepremi e premi all'allevamento): 99,5 mln;
  - cap. 2297, sovvenzioni alle società di corse: 37,1 mln.

  Restano vigilanza, antidoping e benessere dei cavalli (cap. 2298, 23,6 mln). [Fatto, rendiconto 2025]
- **Perché è credibile.** È un taglio di due capitoli identificati, e la Ragioneria può certificarlo. Nei Paesi confrontati il settore si finanzia con le scommesse, non con il bilancio dello Stato:
  - in Francia i profitti del PMU finanziano corse e allevamento (Cour des comptes, *L'institution des courses*, 2018);
  - nel Regno Unito c'è un prelievo di legge sui bookmaker (Horserace Betting Levy Board).

  [Valutazione] In Italia lo Stato ha preso il posto delle scommesse in calo dopo la soppressione dell'ASSI (DL 95/2012).
- **Chi paga.** Società di corse e ippodromi, proprietari e allevatori, con premi più bassi. In parte i lavoratori degli ippodromi.
- **Sovrapposizioni.** La base di RA04 comprende l'ippica (circa 0,14 mld) e ne taglia il 3-5%. Il valore netto oltre RA04 è 0,027-0,048. Il cap. 7763 (ippodromi, 7 mln in conto capitale) resta in RA14.
- **Rischi.** Chiusura degli ippodromi minori e opposizione locale. Mitigazione: gradualità in 3 anni e riforma del prodotto di scommessa.
- **Che cosa non sappiamo.** Se ci sono impegni pluriennali nei contratti con gli ippodromi. Quante società sono coinvolte (n.d.).

### RA51. TV e radio locali: contributi solo a chi fa informazione (0,025-0,04 mld, a regime nel 2029)

- **Che cosa.** Il contributo all'emittenza locale scende del 25-35% dal 2028. È la quota MIMIT del Fondo per il pluralismo e l'innovazione dell'informazione (L. 198/2016, criteri nel DPR 146/2017; cap. 3125, 129,6 mln nel 2025 [Fatto]). Il resto va solo alle emittenti che producono informazione locale con giornalisti assunti. Chi trasmette soprattutto televendite non riceve più nulla.
- **Perché è credibile.** È un capitolo identificato, ripartito ogni anno con decreto, quindi il taglio si attua per legge di bilancio.
- **Attenzione, non è un eccesso di spesa.** In COFOG l'Italia spende meno della media UE per radio, TV ed editoria (0,1% contro 0,2% del PIL). La ragione del taglio è il basso valore pubblico di una parte dei contributi.
- **Chi paga.** Le emittenti commerciali con poca informazione propria, e in parte i loro dipendenti.
- **Sovrapposizioni.** La base di RA04 comprende le emittenti locali per circa 0,13 mld. Il valore netto oltre RA04 è 0,026-0,041.
- **Rischi.**
  - Pluralismo dell'informazione (art. 21 Cost.): per questo i contributi restano a chi produce notizie locali.
  - Il Fondo è alimentato in parte da una quota del canone RAI. Se la parte tagliata viene dal canone, la norma deve riversarla all'entrata dello Stato, altrimenti non è copertura.
- **Che cosa non sappiamo.** La composizione delle fonti del Fondo. Il numero delle emittenti beneficiarie (n.d.). Il sostegno nei Paesi confrontati, che non abbiamo verificato con fonti primarie.

### RA52. Compensi ai CAF: metà per il 730 precompilato inviato senza modifiche (0,01-0,03 mld, a regime nel 2029)

- **Che cosa.** Lo Stato paga ai CAF e ai professionisti un compenso per ogni 730 trasmesso (art. 38 d.lgs. 241/1997; cap. 3845, 216,9 mln nel 2025 [Fatto]). Dal 2029 il compenso si dimezza per i 730 precompilati trasmessi senza nessuna modifica ai dati dell'Agenzia. Resta pieno per le dichiarazioni modificate o integrate. Resta gratuito il canale assistito dell'Agenzia delle entrate.
- **Perché è credibile.** Il compenso unitario è fissato per legge e decreto, quindi la Ragioneria può certificare il risparmio una volta noto il numero di 730 senza modifiche.
- **Legame con il confronto.** I consumi intermedi per gli affari fiscali sono più alti della media UE (0,4% contro 0,3% del PIL). In parte dipendono da questi compensi e dagli aggi sui giochi.
- **Chi paga.** CAF e professionisti. Rischio: che chiedano la differenza ai contribuenti, soprattutto alle persone anziane. Mitigazione: il canale gratuito dell'Agenzia.
- **Sovrapposizioni.** Il conto fiscale 01-P7 ridurrebbe i compensi ai CAF ex post e non li conta come copertura. RA52 conta solo la parte decisa per legge. Se 01-P7 parte nella variante PIENA, RA52 va ricalcolata sulla base che resta.
- **Che cosa non sappiamo.**
  - **La quota di 730 senza modifiche è n.d.** Abbiamo ipotizzato il 10-25% dei 730 compensati. Il dato va chiesto all'Agenzia delle entrate.
  - La L. 199/2025 ha già ridotto i compensi: la base del 2028 può essere più bassa. Per questo il minimo è a 0,01.
  - L'assenza di compensi di questo tipo in Spagna e nei Paesi nordici non è verificata con una fonte primaria.

**Totale RA50-RA52: 0,06-0,12 mld l'anno a regime**, tutto nel fondo RIALLOCAZIONE, livello 1.

## Idee scartate e perché

| Idea | Dato | Perché scartata |
|---|---|---|
| Personale o servizi comuni delle forze di polizia | Polizia 1,0% del PIL contro 0,9 UE; 399 agenti ogni 100.000 abitanti (2020) contro 361-379 di Francia e Spagna. Consumi intermedi delle forze statali circa 1,7 mld nel 2025, senza i servizi di informazione [Stima sul rendiconto] | Lo scarto è piccolo. I consumi intermedi sono già nella base di RA01 e gli affitti delle caserme in RA02. Un taglio del personale peserebbe sulla sicurezza (SIC) senza un piano dei presidi. Da riprendere solo con una mappa ufficiale dei presidi doppi |
| Difesa: troppo personale, poche spese di esercizio | Personale 0,7% del PIL contro 0,6 UE; consumi intermedi 0,1 contro 0,4 | Con 07-C5 ZERO un risparmio interno resterebbe alla Difesa. I nuovi fondi del DDL 2027 (art. 92, Forze di riserva, 423 mln nel 2028; art. 96, ausiliari delle polizie) sono finanziati in deficit con la clausola nazionale. Il programma non la usa già oggi: non toglierli non libera spazio, come dice la stessa scheda 07-C5 |
| Sussidi ai trasporti | 0,6% del PIL contro 0,3 UE | Sono FS, TPL e continuità territoriale, esclusi dall'incarico e da rafforzare nel programma. Gli sconti sui pedaggi dell'autotrasporto sono già riallocati nell'area 04 |
| Crediti d'imposta all'industria (ZES unica, Transizione 4.0 e 5.0) | 0,5% del PIL contro 0,2 (2024) | Il DDL 2027 (art. 85) rifinanzia il credito ZES solo per il 2027 (1,4 mld) e il 2028 (0,5 mld): non c'è un risparmio strutturale per il 2029-2033. Transizione 4.0 e 5.0 sono in esaurimento. L'iperammortamento è già in SF10 |
| Superbonus (sviluppo abitativo) | 0,4% del PIL nel 2024, 4,1% nel 2023 | Sono crediti già maturati, non si tagliano |
| Rifiuti | Consumi intermedi 0,5% del PIL contro 0,2 | È spesa dei comuni coperta dalla TARI: un risparmio abbassa la tariffa, non copre misure statali |
| Fondo di garanzia PMI | 4,35 mld nel rendiconto 2025 | Il DDL 2027 lo riduce già di 1 mld nel tendenziale. L'effetto sull'indebitamento delle garanzie standardizzate è incerto |
| Tax credit cinema | Cap. 7765, 2,0 mld di regolazioni contabili; Fondo cinema e audiovisivo | Il Fondo è già sceso a 500 mln l'anno dal 2027 (L. 199/2025, dato da fonte secondaria, da verificare). L'Italia spende per la cultura meno della media UE |
| Patronati | Cap. 4331, 565 mln | L'aliquota vigente non è verificata con una fonte primaria. È un servizio gratuito per le persone più fragili, già tagliato nel 2015-2016 |
| Correzioni finanziarie UE non riconosciute | Cap. 2817, 700 mln | La rivalsa sulle Regioni sposta il costo dentro la PA e non migliora l'indebitamento netto |
| Aggi sui giochi | Cap. 3926, 3,17 mld | Il Lotto è stato riaffidato nel 2025 per 9 anni (aggio del 6%, fonte stampa). Le altre concessioni sono a metà durata. Possibile solo alla scadenza (Superenalotto, data da verificare), quindi per ora gettito minimo zero |
| Economie di bilancio 2025 | Circa 20 mld non spesi nei trasferimenti a INPS e alle Regioni | Sono stime di spesa obbligatoria troppo alte, non risparmi. Il tendenziale ESA ne tiene già conto |
| Scuole paritarie | Cap. 1477, 803 mln | Sono legate all'art. 33 Cost. e al costo per le famiglie. Non c'è base comparativa |
| Pensioni ai superstiti | 2,4% del PIL contro 1,4 UE | Sono pensioni, escluse dall'incarico |
| Contributi a enti, istituti e associazioni | Circa 150 mln | Sono capitoli frammentati e in gran parte culturali, e l'Italia spende per la cultura meno della media. Valgono 0,01-0,02, già dentro RA13 |

## Che cosa serve per salire di livello

1. Agenzia delle entrate: numero di 730 trasmessi da intermediari senza modifiche (RA52).
2. MASAF: contratti con gli ippodromi e decreto delle sovvenzioni 2025 (RA50).
3. MIMIT e Dipartimento editoria: fonti del Fondo per il pluralismo, quota canone e quota bilancio (RA51).
4. Ministero dell'interno: mappa dei presidi di polizia nello stesso comune, per rivalutare l'idea scartata sulle forze di polizia.

## Fonti principali

- Eurostat, `gov_10a_exp` e `crim_just_job`, API di diffusione: https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/
- RGS-OpenBDAP, Rendiconto 2025 per capitolo: https://bdap-opendata.rgs.mef.gov.it/ (copia in `dati/raw/00b_openbdap_rendiconto_2025_spese_capitolo.csv`)
- DDL di bilancio 2027, A.C. 3174, relazioni illustrativa e tecnica, art. 85 e art. 92-96 (copia in `dati/raw/00b_ddl_bilancio_2027_AC3174_relazioni.txt`)
- Cour des comptes, *L'institution des courses* (18/6/2018): https://www.ccomptes.fr/fr/publications/linstitution-des-courses
- Horserace Betting Levy Board: https://www.hblb.org.uk/
- L. 198/2016: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2016-10-26;198
- DPR 146/2017: https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:2017-08-23;146
- d.lgs. 241/1997, art. 38: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-07-09;241
- Fonti secondarie, da verificare:
  - Pagella Politica sul Fondo cinema: https://pagellapolitica.it/articoli/governo-meloni-fondi-cinema
  - ItaliaOggi sulla concessione del Lotto: https://www.italiaoggi.it/diritto-e-fisco/gioco-del-lotto-igt-vince-la-gara-per-la-concessione-di-altri-9-anni-con-un-offerta-di-2-2-miliardi-q39ibfy8
