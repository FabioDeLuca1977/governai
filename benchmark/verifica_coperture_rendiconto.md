# Verifica delle coperture che tagliano spesa dello Stato sul rendiconto 2025

Verifica del 13/11/2026, fatta con lo stesso metodo usato per RA03.

Fonte principale: OpenBDAP-RGS, Rendiconto 2025 per capitolo (`dati/raw/00b_openbdap_rendiconto_2025_spese_capitolo.csv`, 5.395 capitoli), colonna "Totale CP" (impegni di competenza). Abbiamo controllato che Totale CP = Pagato CP + Rimasto da pagare CP: la differenza massima è sotto 1 euro. Le voci sono classificate con "Categoria" e "Codice Puntato CE", non con le parole dei titoli. Le parole dei titoli servono solo a riconoscere voci estranee dentro una categoria.

Altre fonti nel repository: DPB 2027 (`00b_mef_dpb_2027.txt`, Tab. I.6-1); DDL di bilancio 2027 A.C. 3174, relazioni illustrativa e tecnica (`00b_ddl_bilancio_2027_AC3174_relazioni.txt`); MEF, Rapporto spese fiscali 2025 (`01_mef_rapporto_spese_fiscali_2025.txt`); `benchmark/invitalia_incentivi_imprese.md`. Una sola fonte esterna: INPS, Assestamento del bilancio preventivo 2024, conto economico (il PDF già citato in RP06).

## In breve

- **Coperture verificate:** 21 RIALLOCAZIONE attive nell'intermedio (PE04 esclusa) più RA11, che nell'intermedio non è attiva. Abbiamo controllato anche la base delle coperture SAD e SPESE_FISCALI attive che si appoggiano sul Rapporto spese fiscali o su capitoli del bilancio.
- **Confermate: 5 riallocazioni** (RA03, RA05, RP01, RP02 e RP06), più tutte le SAD e SF controllate: la loro base sul Rapporto spese fiscali coincide, al decimale, con il testo del Rapporto.
- **Da ridurre: 9.** Sono RA01, RA04, RA08, RA09, RA13, RA14, RP03 e RP05, più RA11, che però non è attiva.
- **Non verificabili con i dati disponibili: 8.** Sono RA02, RA06, RA07, RA10, RA12, RP04, RP07 e RP08: per ora restano invariate.
- **Errore ricorrente**, lo stesso di RA03: basi prese da una categoria intera o da parole nei titoli, che contengono voci di natura diversa. Gli esempi più grandi:
  - i 9,8 mld di trasferimenti correnti alle imprese contengono 2,64 mld di crediti d'imposta alle banche (imposte anticipate, DTA) e 1,44 mld di rimborso accise agli autotrasportatori (cioè SAD01);
  - gli 81,8 mld di contributi agli investimenti alle imprese sono per il 71% regolazioni contabili di crediti d'imposta (58,2 mld);
  - i 17,3 mld di consumi intermedi contengono 3,3 mld di aggi sui giochi, 1,8 mld del sistema di informazione per la sicurezza e 1,9 mld di spese di giustizia.
- **Effetto sulle 21 riallocazioni attive nell'intermedio:**

| | Gettito minimo (mld) | Gettito massimo (mld) |
|---|---|---|
| Oggi | 2,46 | 5,56 |
| Proposto | 1,74 | 3,97 |
| Differenza | **-0,72** | **-1,59** |

  Le SAD e le SPESE_FISCALI controllate non cambiano.

## Tabella per copertura

Importi in miliardi di euro; "rend. 2025" significa impegni di competenza 2025 dal file OpenBDAP.

### Coperture attive nell'intermedio

| Codice | Gettito attuale | Base dichiarata | Base verificata (fonte) | Giudizio | Gettito proposto | Motivo e calcolo |
|---|---|---|---|---|---|---|
| RA13 | 0,6-1,2 | 0,05% del PIL oltre il DPB (circa 1,3 mld) | DPB 2027 Tab. I.6-1: la revisione della spesa dei ministeri vale 0,05% del PIL nel 2027 e 0,08% nel 2028-29. Nel DDL 2027 (art. 135) la parte **permanente di spesa corrente** è solo di 234/242/265 mln (c. 2), più 60 mln versati dalla PCM. Il resto (334/866/1.025 mln di indebitamento) è una **rimodulazione in conto capitale** che torna indietro nel 2030-2032 (allegati 5 e 6) | da ridurre | **0,4-1,0** | Lo Stato stesso ha trovato circa 0,3 mld l'anno di tagli correnti permanenti. Chiedere altri 0,6 come minimo, più le misure specifiche sullo stesso perimetro (RA01, RA04, RA09, RA14 e RP01-RP05: circa 0,4-0,5 di minimo dopo le correzioni), vuol dire 3-4 volte lo sforzo del DDL. Inoltre, se i ministeri raggiungono l'obiettivo di RA13 con gli stessi tagli, il doppio conteggio è sicuro. Proposta: minimo -0,2, massimo ridotto a 1,0, e base di RA13 definita al netto delle voci delle altre coperture |
| RA14 | 0,4-1,0 | Contributi agli investimenti a imprese 81,8 mld | Rend. 2025, categoria 23 = 81,8 mld, di cui: **regolazioni di crediti d'imposta 58,2** (cap. 7780 MEF 42,8 bonus edilizi; 7800 credito Mezzogiorno 6,8; 7493 Industria 4.0 3,2; 7765 cinema 2,0; 7828 1,8); infrastrutture e contratti di programma 9,6 (FS 7,0, Ponte sullo Stretto, Torino-Lione); programmi della Difesa al MIMIT 3,0 (FREMM, aerospazio); garanzie e fondi rotativi 6,3 (Fondo di garanzia PMI 4,35, SIMEST 1,6); PNRR 0,3. **Incentivi veri a fondo perduto o agevolati: 4,4 mld** (contratti di sviluppo 1,19; transizione energetica industriale 0,76; Nuova Sabatini 0,61; alta tecnologia 0,36; cinema 0,28; IPCEI 0,25) | da ridurre | **0,2-0,5** | Base aggredibile senza spese fiscali: 4,4 + 6,3 = 10,7 mld. Il 2-5% di 10,7 fa 0,21-0,54. Togliere linee di credito d'imposta è una misura di spese fiscali e si sovrappone a SF05 e SF10. Industria 4.0 e Transizione 5.0 sono in esaurimento e già nel tendenziale. Il DDL 2027 (art. 86) attua il d.lgs. 138/2026 a saldo zero: nessun risparmio già scontato, ma nemmeno uno già trovato |
| RA06 | 0,2-0,4 | Scheda area 06; Consip | Non è nel bilancio dello Stato: è spesa degli enti SSN, finanziata col FSN | non verificabile | 0,2-0,4 (invariato) | Serve la spesa SSN per beni e servizi non sanitari (RGS, Monitoraggio della spesa sanitaria; conti economici CE degli enti). Il DL 95/2012 art. 15 ha già ridotto i contratti per beni e servizi non sanitari: una parte del risparmio è già nel tendenziale. Diventa copertura statale solo con il taglio del FSN per legge |
| RA05 | 0,16 | DDL 2027 art. 71, 160 mln | Relazione tecnica art. 71 c. 2-8: oneri di 160 mln annui; lo Stato li versa alle Regioni | confermata | 0,16 | Con l'abrogazione lo Stato risparmia direttamente, senza bisogno di ridurre il FSN: la nota del menu va corretta su questo punto. Vale solo se l'art. 71 resta nel testo approvato |
| RA01 | 0,15-0,4 | Consumi intermedi Stato 17,3 mld | Rend. 2025, categoria 2 = 17,27 mld. Fuori dal perimetro degli acquisti: aggi e compensi su giochi e riscossione (CE 2.2.12) 3,29; sistema di informazione per la sicurezza (cap. 1670 MEF) 1,83; spese di giustizia, magistrati onorari e detenuti 1,90; servizi finanziari del debito (CE 2.2.9) 0,96; CAF, Poligrafico e Covid 0,99; missioni internazionali della Difesa 0,72; canoni al Demanio 0,07 (in RA02); consulenze 0,06 (in RA03). **Spesa acquistabile: 7,44 mld**, di cui circa 0,5 di ICT (RA09) e 0,04 di manutenzione degli immobili (RP05) | da ridurre | **0,07-0,17** | 1-2,5% di 6,9 mld (7,44 meno ICT e immobili) = 0,069-0,17. Le amministrazioni statali sono già obbligate alle convenzioni Consip dal 2007 (L. 296/2006, c. 449): l'estensione a nuove categorie aggiunge poco |
| RA04 | 0,15-0,4 | Trasferimenti correnti a imprese 9,8 mld | Rend. 2025, categoria 6 = 9,79 mld, di cui: **crediti d'imposta e rimborsi 4,34** (cap. 3887 MEF, DTA delle banche, 2,64; cap. 3820 MEF, rimborso accise agli autotrasportatori, 1,44); **contratti di servizio 2,17** (FS 1,66, Poste 0,26, TPL, ENIT, ENAV); **non incentivi 2,35** (scuole paritarie 0,80, aiuti PAC non riconosciuti dall'UE 0,70, ricerca sanitaria e 5 per mille 0,33, vittime di reati 0,19, Giubileo, compensazioni Covid). **Linee di incentivo vere: 0,92 mld** (85 capitoli: Albo autotrasportatori 0,15, emittenti locali 0,13, ippica 0,14, incentivi al trasporto merci su ferro 0,10, spettacolo dal vivo 0,06) | da ridurre | **0,03-0,06** | 3-5% di 0,92-1,19 mld (1,19 = linee di incentivo più crediti d'imposta minori diversi da DTA e autotrasporto) = 0,03-0,06. Il cap. 3820 è la stessa spesa di SAD01 e SAD13: contarla anche in RA04 sarebbe un doppio conteggio |
| RA07 | 0,15-0,35 | Scheda area 09 | Non verificabile sul rendiconto: dipende dalle assunzioni generiche che si sarebbero fatte | non verificabile | 0,15-0,35 (invariato) | Copre solo 09-C3, quindi non è un risparmio libero. Il DDL 2027 (art. 66 c. 1) porta il turnover dei ministeri al 75% solo per il 2027 e torna al 100% dal 2028: nessuna sovrapposizione dal 2028 |
| RA12 | 0,15-0,4 | Scheda area 05 | Nel rendiconto non c'è nessun capitolo per il Fondo Nuove Competenze, e il cap. 1233 del Lavoro (rimborso ai fondi interprofessionali) è a zero. Il Fondo è cofinanziato dal FSE+ (PN Giovani, donne e lavoro; vedi `giuridico/conformita.csv`). La quota 0,30% passa per l'INPS | non verificabile | 0,15-0,4 (invariato) | Regge solo come fonte vincolata a 05-C2 (risorse FSE+ ammissibili), non come risparmio nazionale. Va certificata con INPS e Ministero del lavoro |
| RA09 | 0,12-0,3 | AgID, spesa ICT PA (5-7 mld) | Rend. 2025: spesa ICT corrente dei ministeri riconoscibile per capitolo **0,52 mld** (di cui 0,33 nei codici CE 2.2.5, 2.2.19 e 2.2.8); ICT in conto capitale 1,26. I dati AgID comprendono INPS, INAIL, agenzie ed enti, che non sono bilancio dello Stato | da ridurre | **0,04-0,09** | 4-6% di una base statale di 1,0-1,5 mld (0,52 identificati più ICT nascosta in capitoli generici e nelle convenzioni delle agenzie fiscali) = 0,04-0,09. La parte degli enti si sovrappone a RP06 (beni e servizi INPS e INAIL); quella sugli accordi quadro Consip si sovrappone a RA01 |
| RA02 | 0,08-0,15 | Demanio, PSI 2025-2028: 769 mln | Rend. 2025: solo 0,15 mld riconoscibili per capitolo (canoni al Demanio CE 2.3.4 71 mln; cap. 3891 MEF 67 mln tramite l'Agenzia delle entrate; altri 13). Il resto dei fitti sta nei piani gestionali dei capitoli generici di funzionamento | non verificabile | 0,08-0,15 (invariato) | Il calcolo regge (20% di 0,77 = 0,154). Serve il dettaglio per piano gestionale, o il dato Demanio solo per le amministrazioni statali, al netto dei risparmi già nel PSI. Il DL 95/2012 art. 3 ha già ridotto i canoni del 15% |
| RA10 | 0,05-0,12 | Scheda area 07 | È un'entrata (contributo unificato), non una spesa | non verificabile | 0,05-0,12 (invariato) | Fuori dal metodo del rendiconto. Serve il gettito del contributo unificato per classe di litigante (Ministero della giustizia) |
| RP08 | 0,05-0,13 | Agenas 701.170 dipendenti SSN | Spesa SSN, fuori dal bilancio dello Stato | non verificabile | 0,05-0,13 (invariato) | Il calcolo torna: 42.000 × 5% × 15% × 4 × 40 mila = 50 mln; 42.000 × 7% × 25% × 4 × 45 mila = 132 mln. Diventa copertura statale solo con il taglio del FSN. Da confermare la quota amministrativa del 9,7% |
| RP01 | 0,04-0,1 | Conto annuale 2024 | Non si vede sul rendiconto. Il DDL 2027 art. 66 c. 1 fissa il 75% solo per il 2027 e torna al 100% dal 2028: RP01 (2028-2031) non è nel tendenziale | confermata | 0,04-0,1 | Il calcolo torna: 32.000 × 5% × 15% × 4 × 41 mila = 39 mln; 32.000 × 7% × 25% × 4 × 45 mila = 101 mln |
| RP06 | 0,03-0,06 | INPS B.06.B 885,9 mln | INPS, Assestamento 2024, conto economico: B.06.B "Spese per acquisto beni di consumo e servizi" = 885.869.766 euro (confermato) | confermata (il minimo) | 0,03-0,06 | 4% × 886 = 35 mln. Da verificare la composizione: se la voce contiene compensi ai CAF o commissioni postali per il pagamento delle pensioni, è lo stesso errore di RA03 (con 100-150 mln da togliere il minimo resta 0,03). Il massimo poggia su una base di 1,4 mld non verificata |
| RA08 | 0,03-0,1 | Scheda area 09; "RA03 consulenze 189 mln" | Rend. 2025: tutta la categoria CE 2.2.2 (consulenze e studi) vale 59 mln ed è già in RA03 (non 189). I capitoli di assistenza tecnica con fondi nazionali valgono circa 1-2 mln. Il resto dell'assistenza tecnica è pagato con fondi UE o FSC, fuori dal bilancio ordinario | da ridurre | **0,01-0,03** | Quasi nessuna base nazionale "oltre RA03". La nota del menu cita ancora i 189 mln: è un dato superato. Il gettito residuo serve solo se si tagliano le quote di assistenza tecnica dell'FSC con un definanziamento |
| RP07 | 0,02-0,06 | Corte dei conti (via stampa) | Partecipate degli enti territoriali, fuori dal bilancio dello Stato | non verificabile | 0,02-0,06 (invariato) | Serve il referto della Corte dei conti letto alla fonte |
| RP03 | 0,02-0,05 | Programma "Indirizzo politico" 260 mln | Rend. 2025: 260,0 mln confermati, di cui 214,7 di redditi da lavoro, 27,8 di consumi intermedi e 14,0 di IRAP | da ridurre | **0,01-0,03** | Il massimo (20% di 260) conta anche il personale di ruolo, che secondo la stessa nota non è un risparmio. Minimo: 20% × (27,8 + circa un quarto dei 214,7 come indennità ed esterni) ≈ 16 mln. Massimo: 20% × (27,8 + metà dei 214,7 + 7 di IRAP) ≈ 28 mln |
| RA03 | 0,02-0,03 | CE 2.2.2, 59 mln | Rend. 2025: 58,7 mln in 57 capitoli (confermato) | confermata | 0,02-0,03 | Già corretta il 13/11/2026 |
| RP04 | 0,015-0,05 | Elenco ISTAT S13; spesa degli enti da verificare | Bilanci degli enti, fuori dal rendiconto | non verificabile | 0,015-0,05 (invariato) | Servono i bilanci degli enti candidati all'accorpamento |
| RP05 | 0,015-0,04 | 205 mln trovati con parole chiave | Rend. 2025: rifatta la ricerca per parole chiave (59 capitoli, 205,3 mln), **164,6 mln sono estranei**: sistemi informativi (cap. 2696 MEF 81,4; cap. 1392 MAECI 19,7; altri), vigilanza di settore (ippica 23,6; ambiente marino; rifiuti), mezzi operativi. **Costi degli immobili veri: 40,6 mln** (Fondo manutenzione ordinaria del MEF 33,0) | da ridurre | **0,005-0,02** | 8-12% di una base tra 0,04 (verificata) e 0,2 (ipotesi con i piani gestionali) = 0,003-0,024. Utenze e pulizie stanno nei piani gestionali dei capitoli generici: dato da acquisire. La parte ICT è già in RA09 |
| RP02 | 0,012-0,03 | Conto annuale 2024 | Non si vede sul rendiconto | confermata | 0,012-0,03 | Il calcolo torna: 8-12% di 2.569 = 205-308 posti × 60-80 mila = 12-25 mln. I 2.569 comprendono anche la prima fascia: piccola sovrastima |

### Copertura non attiva nell'intermedio

| Codice | Gettito attuale | Base dichiarata | Base verificata (fonte) | Giudizio | Gettito proposto | Motivo e calcolo |
|---|---|---|---|---|---|---|
| RA11 | 0,2-0,3 | 6.700 posti × 45 mila | DDL 2027 art. 66 c. 5: dal 2027/28 taglia già **4.925 posti** dell'organico dell'autonomia e 2.049 posti ATA. Sono nel tendenziale dopo la manovra | da ridurre | **0-0,08** | Restano al massimo 6.700 - 4.925 = 1.775 posti × 45 mila = 0,08 |

### SAD e SPESE_FISCALI con base sul Rapporto spese fiscali o su capitoli

Tutte le basi citate coincidono, al decimale, con il testo del Rapporto spese fiscali 2025 (`01_mef_rapporto_spese_fiscali_2025.txt`):

| Codice | Valore citato | Dove si trova nel Rapporto |
|---|---|---|
| SF02 | forfetario 3.490,8 mln, beneficio medio 1.717 euro | riga 7597 |
| SF03 | tonnage tax 484,7; credito alle imprese armatoriali 250,4 | righe 777 e 789 |
| SF04 | cooperative, utili a riserva 500,9 | riga 2194 |
| SF06 | spese sanitarie 4.873,9 | riga 4230 |
| SF07 | fondi sanitari integrativi 838,3 | riga 4224 |
| SF08 | sport dei ragazzi 74,2 | riga 7725 |
| FN02 | premi assicurativi 282,3; spese veterinarie 76,5 | righe 5165 e 5131 |
| FN04 | premi di produttività 815,3 | riga 6429 |
| SF16 | patent box 244,5 | riga 778 |
| SAD01 | EN.SI.19, autotrasporto, 1.231,8 | riga 1900 |
| SAD02 | EN.SI.21, gasolio agricolo, 1.107,2 | riga 1366 |

Giudizio per tutte queste righe: **confermata**, gettito invariato. Due controlli in più fatti sul rendiconto:

- **SAD01:** il rimborso agli autotrasportatori (cap. 3820 MEF) vale 1.438,0 mln di impegni 2025, più dei 1.282,6 del Catalogo SAD. La base dichiarata è quindi prudente, come dice la nota.
- **SAD09:** il fondo per gli impianti di risalita (cap. 8601 del Ministero del turismo, conto capitale) vale 80,0 mln, contro i 70 del Catalogo. Il 50% fa 35-40 mln: il gettito di 0,02-0,035 è confermato. Da verificare che il fondo sia finanziato anche dopo il 2027.

SF05, SF09 e SF10 non hanno una base sul rendiconto da ricalcolare: restano gli avvisi già scritti nel menu (sovrapposizione con la lista PSB; costo dell'iperammortamento non pubblicato).

## Doppi conteggi trovati

1. **RA04 e SAD01/SAD13.** Il cap. 3820 MEF (rimborso accise agli autotrasportatori, 1,44 mld) sta dentro i 9,8 mld di base di RA04. Un taglio del 3-5% su quella base conterebbe due volte il sussidio già toccato da SAD01 e SAD13. Risolto con la nuova base di RA04.
2. **RA14 e le spese fiscali (SF05, SF10).** Il 71% della base di RA14 (58,2 mld) sono regolazioni contabili di crediti d'imposta. Abrogarli è una misura di spese fiscali: chi tocca l'iperammortamento o i crediti minori non può contarli anche in RA14. Risolto escludendo le regolazioni dalla base.
3. **RA13 con RA01, RA04, RA09, RA14 e RP01-RP05.** RA13 è un obiettivo generico sullo stesso perimetro dei ministeri. Senza una regola esplicita, i ministeri raggiungono l'obiettivo con gli stessi tagli. Proposta: la base di RA13 esclude le voci delle altre coperture. RP02 dice già che i suoi tagli non contano per RA13; la stessa regola va estesa alle altre.
4. **RA09 con RP06 e RA01.** La base AgID comprende INPS e INAIL, la cui spesa per beni e servizi è già in RP06. Gli accordi quadro Consip per l'ICT sono anche in RA01. Risolto limitando RA09 alla spesa ICT statale.
5. **RP05 con RA09.** 120 mln dei 205 di base di RP05 sono sistemi informativi, cioè spesa ICT. Risolto con la nuova base di RP05.
6. **RA08 con RA03.** Tutta la categoria consulenze e studi (59 mln) è già in RA03. Risolto riducendo RA08.
7. **RA04 e RA14 con il riordino del d.lgs. 138/2026.** È lo stesso perimetro, come già scritto in `benchmark/invitalia_incentivi_imprese.md`. Il DDL 2027 (art. 86) non scarica risparmi, quindi niente è già nel tendenziale. Ma non si possono sommare altri risparmi dello stesso riordino.
8. **Risparmi già nel tendenziale.**
   - RA11: il DDL 2027 art. 66 c. 5 taglia già 4.925 posti.
   - RA13: il DPB conta già 0,05-0,08% del PIL di revisione della spesa.
   - RA02: il PSI del Demanio ha già i suoi risparmi.
   - RA06: il DL 95/2012 ha già tagliato i contratti per beni e servizi non sanitari.

## Dati da acquisire

1. **Rendiconto 2025 per piano gestionale** (OpenBDAP, "spese per piano gestionale"). Serve per RA02 (fitti), RP05 (utenze e pulizie), RA09 (ICT nei capitoli generici) e per le consulenze dentro i capitoli generici (RA03).
2. **Agenzia del Demanio:** locazioni passive delle sole amministrazioni statali, con i risparmi già previsti dal PSI 2025-2028 (RA02).
3. **RGS, Monitoraggio della spesa sanitaria, o conti economici CE degli enti SSN:** spesa per beni e servizi non sanitari (RA06); quota del personale amministrativo (RP08).
4. **INPS, bilancio consuntivo 2025, dettaglio di B.06.B:** compensi ai CAF, servizi postali e bancari, ICT (RP06). Dati simili per INAIL e gli altri EPNE (massimo di RP06).
5. **AgID, spesa ICT 2025 per amministrazione**, solo amministrazioni statali (RA09).
6. **MIMIT, Relazione sugli interventi di sostegno alle attività produttive (Doc. LVIII):** spesa per linea di incentivo statale e valutazioni di addizionalità (RA04, RA14).
7. **MEF-RGS, allegato 7 del DDL 2027:** riparto per ministero delle riduzioni dell'art. 135 c. 2, per escluderle dalla base di RA13.
8. **INPS e Ministero del lavoro:** quota 0,30% non destinata ai fondi interprofessionali e fonti di finanziamento del Fondo Nuove Competenze 2025-2027 (RA12).
9. **Ministero della giustizia:** gettito del contributo unificato per classe di litigante (RA10).
10. **Corte dei conti, Sezione autonomie, referto sugli organismi partecipati, letto alla fonte** (RP07); bilanci degli enti candidati all'accorpamento (RP04).
11. **Ministero del turismo:** stanziamenti 2027-2029 del cap. 8601 (SAD09).

## Correzioni proposte per `programma/coperture_menu.csv`

Questo rapporto non modifica il menu. Le correzioni da applicare sono queste:

| Codice | Da | A |
|---|---|---|
| RA01 | 0,15-0,4 | 0,07-0,17 |
| RA04 | 0,15-0,4 | 0,03-0,06 |
| RA08 | 0,03-0,1 | 0,01-0,03 (e la nota "189 mln" va aggiornata a 59 mln) |
| RA09 | 0,12-0,3 | 0,04-0,09 |
| RA13 | 0,6-1,2 | 0,4-1,0 (con la regola di esclusione) |
| RA14 | 0,4-1,0 | 0,2-0,5 |
| RP03 | 0,02-0,05 | 0,01-0,03 |
| RP05 | 0,015-0,04 | 0,005-0,02 |
| RA11 (non attiva) | 0,2-0,3 | 0-0,08 |

Altre due correzioni:

- **RA05:** correggere la nota. Non serve ridurre il FSN, perché i 160 mln sono una spesa dello Stato.
- **RA04 e SAD01:** aggiungere nelle note l'esclusione del cap. 3820.

Calcolo dell'effetto sulle 21 riallocazioni attive nell'intermedio:

| | Gettito minimo (mld) | Gettito massimo (mld) |
|---|---|---|
| Oggi | 2,462 | 5,560 |
| Correzioni | -0,08 RA01, -0,12 RA04, -0,02 RA08, -0,08 RA09, -0,20 RA13, -0,20 RA14, -0,01 RP03, -0,01 RP05 | -0,23 RA01, -0,34 RA04, -0,07 RA08, -0,21 RA09, -0,20 RA13, -0,50 RA14, -0,02 RP03, -0,02 RP05 |
| Totale correzioni | **-0,72** | **-1,59** |
| Dopo le correzioni | **1,74** | **3,97** |

Gli script di calcolo sono stati eseguiti fuori dal repository e non sono salvati.
