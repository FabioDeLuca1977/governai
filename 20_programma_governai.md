# Programma GovernAI

*Versione 2.0, 8 novembre 2026, sulla Carta dei valori 2.0 (dieci valori). Un programma di governo né di destra né di sinistra né di centro: ogni misura è giudicata sui valori dichiarati nella Carta, è finanziata senza deficit e ha una scheda pronta per l'attuazione.*

*Le cifre in tabella sono generate da `programma/documento.py` a partire dal motore e dall'ottimizzatore: non si correggono a mano. I dati aggiornati ogni giorno sono nel sito (`docs/`).*

## 1. In sintesi

Due versioni del programma, entrambe finanziate senza deficit nello scenario prudente: gettito minimo delle coperture, nessun risparmio non certificato, nessun recupero di evasione usato come copertura. Accanto, il programma che il governo ombra ha adottato nella seduta «Conti in ordine» (simulazione: le decisioni non sono in vigore).

<!-- auto:totali -->
- **Programma base: 8,23 mld l'anno**, 65 misure su 78, con 22 su 23 del nucleo robusto almeno in versione essenziale. Usa solo coperture a basso costo sociale.
- **Programma completo: 13,57 mld l'anno**, 69 misure, nucleo robusto 23 su 23. Aggiunge coperture strutturali più impegnative.
- **Programma intermedio: 9,03 mld l'anno**, 66 misure, nucleo robusto 21 su 23. Nessun aumento di tasse su casa, eredità, affitti e IVA, nessun contributo straordinario sulle pensioni; più istruzione e servizi sociali, con tagli di spesa e di personale nei ministeri. Per scelta politica restano tutte le sette misure su ricerca, innovazione e logistica verde (alcune in versione ridotta) e la squadra per la produttività pubblica con l'AI (09-C9) in versione essenziale; dal 12 novembre 2026 entrano, senza tasse in più oltre quelle già nel programma, le Case della Comunità (06-C3), 500 squadre infermieristiche di quartiere (06-C8) e la riqualificazione degli amministrativi della sanità (06-C10). Restano accise su tabacco, alcol e bevande zuccherate, il riordino di alcune agevolazioni fiscali e dei sussidi dannosi, e dal 2030 una rivalutazione ridotta sulla quota più alta delle pensioni (`programma/selezione_intermedio.md`).
- **Programma adottato dal governo ombra** (simulazione, `governo/`): 11,63 mld l'anno, 55 misure, coperture al minimo per 11,12 mld più i fondi vincolati.
<!-- /auto:totali -->

- **Il nucleo robusto viene prima.** Sono le misure (oggi 23) prioritarie con quasi ogni combinazione di pesi tra i valori: si finanziano almeno in versione essenziale prima di ottimizzare il resto.
- **L'eccezione del programma base è il nido (02-C2).** È l'unica misura del nucleo che il base non finanzia. La sua versione essenziale costa 2,0 mld l'anno e si paga con il riordino dei bonus familiari e delle spese fiscali. Nel base queste risorse non bastano, anche perché la linea rossa sull'equità esclude la soppressione del bonus lavoratrici madri (RB05). Entra nel programma completo e nella decisione del governo ombra.
- **L'impianto istituzionale costa poco**: legge sulla consulenza algoritmica pubblica (08-P1), "Stato a vetro" (09-C1), bilancio generazionale (01-P1), spese fiscali a scadenza (01-P2), valutazione indipendente delle grandi opere (04-P4).
- **Restano decisioni politiche**, presentate con il loro prezzo (§6): la traiettoria della Difesa, il dividendo climatico, l'adozione delle coperture strutturali.

## 2. Come è stato costruito

| Passo | Cosa | Dove |
|---|---|---|
| 1 | 9 dossier ministeriali e 76 proposte: 11 su fisco semplice, evasione, PA produttiva e integrità degli appalti, 6 nate dal confronto con il Nord Europa su scuola, servizi sociali e cultura (`benchmark/proposte_nord_europa.md`), 4 su ricerca e innovazione (`benchmark/ricerca_innovazione.md`) e 3 sulla logistica verde (`benchmark/logistica_green.md`) | `ministeri/`, `programma/schede/` |
| 2 | Verifica di 334 cifre su fonte primaria; base dati riproducibile | `dati/` |
| 3 | Vincolo di bilancio ufficiale: margine in deficit zero | `dati/verifiche/00_vincolo_bilancio.md` |
| 4 | Carta dei 10 valori: Rispetto e diversità, Fiducia e trasparenza, Innovazione, Benessere, Apprendimento e cultura, Bellezza patrimonio e accoglienza, Responsabilità verso il futuro, Equità, Sicurezza senza controllo assoluto, Cittadinanza responsabile | `01_carta_valori.md` |
| 5 | Panel di 3 valutatori (agenti AI distinti da chi ha scritto le proposte; alfa di Krippendorff 0,85) e motore SMAA su 20.000 combinazioni di pesi | `motore/` |
| 6 | 184 varianti (piena, essenziale, pilota, zero) e 63 misure di copertura concrete, con verifica fiscale, costituzionale ed europea | `programma/varianti/`, `programma/coperture_menu.csv`, `giuridico/` |
| 7 | Ottimizzazione: il massimo valore secondo la Carta, interamente finanziato, con priorità al nucleo robusto | `programma/ottimizza.py` |
| 8 | Governo ombra: esperti, 9 ministri, opposizione leale e capo di governo decidono con regole verificabili | `governo/` |

**Un limite da dichiarare.** I tre valutatori del panel sono agenti AI, indipendenti da chi ha scritto le proposte ma non da chi ha progettato il sistema. L'accordo alto tra loro dipende anche dai molti punteggi a zero. La revisione esterna di persone con orientamenti diversi resta il passo successivo (§7).

## 3. Le misure

**Classe** indica il giudizio del motore:
- **Nucleo**: prioritaria con quasi ogni combinazione di pesi;
- **Valori**: la priorità dipende dai valori;
- **Coda**: utile ma in fondo alla classifica;
- **Sfav.**: sfavorevole.

**Linea rossa in alcune versioni**: almeno una versione della proposta supera una linea rossa della Carta ed è esclusa in automatico; le altre versioni restano possibili. Per la Difesa (07-C5) sono escluse le versioni finanziate in deficit.

Costi in mld €/anno a regime. "—" = non inclusa. L'ultima colonna è la decisione del governo ombra, che può discostarsi dall'ottimizzatore dichiarando la deroga nel verbale.

<!-- auto:misure -->
| # | Misura | Classe | Programma base | Programma completo | Governo ombra |
|---|---|---|---|---|---|
| **Economia, Imprese, Turismo** | [schede](programma/schede/01_economia.md) | | | | |
| 01-P1 | Bilancio generazionale: ogni legge dichiara chi paga e quando | Coda | Piena 0,02 | Piena 0,02 | Essenziale 0,01 |
| 01-P2 | Spese fiscali a scadenza (sunset 5 anni) | Valori | Piena 0,01 | Piena 0,01 | Piena 0,01 |
| 01-P3 | IVA in tempo reale | **Nucleo** | Essenziale 0,08 | Piena 0,15 | Essenziale 0,08 |
| 01-P4 | Crescere conviene: eliminare i gradini dimensionali | Coda | Zero 0,01 | Zero 0,01 | Zero 0,01 |
| 01-P5 | Energia a prezzo stabile per le PMI (PPA rinnovabili) | Coda | Essenziale 0,15 | Essenziale 0,15 | Essenziale 0,15 |
| 01-P6 | Turismo che ripaga i territori: tassa di soggiorno intelligente | Valori | Zero 0,00 | Piena 0,15 | Zero 0,00 |
| 01-P7 | Dichiarazione zero: lo Stato fa il conto, chi dichiara controlla | **Nucleo** | Essenziale 0,15 | Piena 0,30 | Essenziale 0,15 |
| 01-P8 | Meno scontrini: riordino delle detrazioni del 19% | Coda | Zero 0,00 | Zero 0,00 | Essenziale 0,20 |
| 01-P9 | Una sola detrazione per il lavoro, senza scalini | Coda | Zero 0,00 | Zero 0,00 | Zero 0,00 |
| 01-P10 | Controlli mirati con garanzie: usare meglio i dati che il fisco ha già, senza sorvegliare tutti | Valori | Piena 0,10 | Piena 0,10 | Essenziale 0,06 |
| 01-P11 | Lo scontrino che conviene: un incentivo mirato al posto di lotterie e cashback | Coda | Zero 0,00 | Zero 0,00 | Zero 0,00 |
| 01-P12 | Pagare è semplice, condonare no: semplificazione, riscossione efficace, sanzioni proporzionate | **Nucleo** | Piena 0,06 | Piena 0,06 | Essenziale 0,04 |
| 01-P13 | Un solo credito per la ricerca: stabile, più forte per le piccole imprese, certificato prima di spendere | Coda | Zero 0,01 | Zero 0,01 | — |
| 01-P14 | Sfide Italia: la pubblica amministrazione compra innovazione in tre fasi | Coda | Pilota 0,03 | Pilota 0,03 | — |
| 01-P15 | Dalla scoperta all'impresa: prove di fattibilità, regole per gli spin-off, fondo di fondi deep tech | Coda | Zero 0,00 | Piena 0,10 | — |
| **Lavoro, Welfare, Famiglia** | [schede](programma/schede/02_lavoro.md) | | | | |
| 02-C1 | Salario minimo contrattuale garantito | Valori | Zero 0,00 | Zero 0,00 | Essenziale 0,20 |
| 02-C2 | Nido esigibile + congedo paterno | **Nucleo** | — | Essenziale 2,00 | Essenziale 2,00 |
| 02-C3 | Patto previdenziale tra generazioni | Valori | Essenziale 0,35 | Essenziale 0,35 | Essenziale 0,35 |
| 02-C4 | Reddito di inclusione universale | Valori | — | — | Pilota 0,10 |
| 02-C5 | Progetto di vita esigibile e lavoro per le persone con disabilità | **Nucleo** | Essenziale 0,80 | Essenziale 0,80 | Essenziale 0,80 |
| 02-C6 | Bilancio generazionale e strategia demografica | Coda | Zero 0,00 | Zero 0,00 | Zero 0,00 |
| 02-C7 | Housing First dopo il PNRR | **Nucleo** | Essenziale 0,09 | Piena 0,15 | — |
| **Ambiente, Energia, Agricoltura** | [schede](programma/schede/03_ambiente.md) | | | | |
| 03-P1 | Dividendo climatico: riforma SAD restituita alla cittadinanza | Valori | Zero 0,00 | Zero 0,00 | Essenziale 1,20 |
| 03-P2 | Elettricità rinnovabile a prezzo rinnovabile (CfD) | Valori | Zero 0,00 | Piena 0,15 | Essenziale 0,07 |
| 03-P3 | Ogni goccia conta: reti idriche e riuso | **Nucleo** | Essenziale 0,60 | Essenziale 0,60 | — |
| 03-P4 | Prevenire costa meno: fondo prevenzione e assicurazione catastrofale | **Nucleo** | Essenziale 0,80 | Essenziale 0,80 | Essenziale 0,80 |
| 03-P5 | Contratto agro-climatico | Valori | — | Essenziale 0,25 | Pilota 0,05 |
| **Infrastrutture e Territori** | [schede](programma/schede/04_infrastrutture.md) | | | | |
| 04-P1 | Patto di continuità post-PNRR | Coda | — | — | — |
| 04-P2 | Casa a canone giusto | Valori | — | — | Essenziale 0,48 |
| 04-P3 | Prima il treno di chi viaggia ogni giorno: fondo TPL e abbonamento unico | Valori | — | — | Pilota 0,62 |
| 04-P4 | Nessuna grande opera senza prova dei numeri | Valori | Piena 0,03 | Piena 0,03 | Piena 0,03 |
| 04-P5 | LEP prima: autonomia differenziata reversibile | Valori | Zero 0,00 | Zero 0,00 | Zero 0,00 |
| 04-P6 | Restare è possibile: servizi essenziali aree interne | **Nucleo** | Essenziale 0,42 | Essenziale 0,42 | Essenziale 0,42 |
| 04-P7 | Dal porto al treno: più merci sul ferro | Coda | — | Pilota 0,06 | — |
| 04-P8 | Camion a zero emissioni: patto per la transizione dell'autotrasporto | Coda | Zero 0,00 | Piena 0,15 | — |
| 04-P9 | Consegne pulite in città: zone a emissioni zero per le merci | Coda | Zero 0,00 | Piena 0,07 | — |
| **Istruzione, Ricerca, Cultura** | [schede](programma/schede/05_istruzione.md) | | | | |
| 05-C1 | Nessuna esclusione: squadre di prossimità contro la dispersione | **Nucleo** | Essenziale 0,13 | Piena 0,25 | Piena 0,25 |
| 05-C2 | Conto personale di competenze | **Nucleo** | Essenziale 0,45 | Essenziale 0,45 | Essenziale 0,45 |
| 05-C3 | Carriere della ricerca | Valori | Zero 0,00 | Zero 0,00 | Zero 0,00 |
| 05-C4 | Più persone con laurea o diploma terziario: ITS, lauree professionalizzanti, residenze | **Nucleo** | Essenziale 0,45 | Essenziale 0,45 | Essenziale 0,45 |
| 05-C5 | Scuole aperte come presidi di comunità | **Nucleo** | Essenziale 0,20 | Piena 0,40 | Essenziale 0,20 |
| 05-C6 | AI a scuola | Valori | Zero 0,00 | Piena 0,22 | Essenziale 0,08 |
| 05-C7 | Quota svantaggio nel finanziamento delle scuole | **Nucleo** | Essenziale 0,19 | Essenziale 0,19 | — |
| 05-C8 | Biblioteche di comunità | Valori | Pilota 0,03 | Piena 0,33 | — |
| 05-C9 | Zaino culturale a scuola e tariffa sociale della cultura | Valori | Pilota 0,02 | Piena 0,20 | — |
| 05-C10 | Rete nazionale per la ricerca applicata sul modello Fraunhofer | Coda | Pilota 0,05 | Pilota 0,05 | — |
| **Salute** | [schede](programma/schede/06_salute.md) | | | | |
| 06-C1 | Tempo garantito o rimborso | Valori | Zero 0,00 | Zero 0,00 | Zero 0,00 |
| 06-C2 | Patto per il personale infermieristico e la medicina generale | Valori | — | — | Pilota 0,35 |
| 06-C3 | Case della Comunità vive | **Nucleo** | Essenziale 0,80 | Essenziale 0,80 | — |
| 06-C4 | Budget di cura per la non autosufficienza | Valori | — | — | — |
| 06-C5 | Salute mentale al 5% | Valori | — | — | — |
| 06-C6 | Dividendo della prevenzione e budget unico del farmaco | Coda | Zero 0,00 | Zero 0,00 | Zero 0,00 |
| 06-C8 | Squadre infermieristiche autonome di quartiere per l'ADI | Valori | Pilota 0,02 | Piena 0,25 | — |
| 06-C9 | Equipe di benessere scolastico in rete con la Casa della Comunità | Coda | Pilota 0,03 | Piena 0,20 | — |
| 06-C10 | Meno burocrazia, più cura: automazione degli uffici sanitari e riqualificazione del personale amministrativo | Coda | Piena 0,04 | Piena 0,04 | — |
| **Giustizia, Interno, Difesa** | [schede](programma/schede/07_giustizia.md) | | | | |
| 07-C1 | Giustizia a regime: Ufficio per il processo e triage digitale | **Nucleo** | Essenziale 0,32 | Essenziale 0,32 | Essenziale 0,32 |
| 07-C2 | Pena utile: misure di comunità contro il sovraffollamento | **Nucleo** | Essenziale 0,25 | Piena 0,45 | Essenziale 0,25 |
| 07-C3 | Governance dei flussi migratori fondata sui dati | **Nucleo** | Essenziale 0,25 | Essenziale 0,25 | Essenziale 0,25 |
| 07-C4 | Dal bene confiscato al bene comune | **Nucleo** | Essenziale 0,07 | Piena 0,15 | Essenziale 0,07 |
| 07-C5 | Difesa: percorso NATO 3,5% vincolato a efficienza europea | Sfav. · linea rossa in alcune versioni | — | — | — |
| 07-C6 | Scudo cyber territoriale | Valori | — | Piena 0,35 | Essenziale 0,18 |
| **Esteri, Europa, Istituzioni** | [schede](programma/schede/08_esteri.md) | | | | |
| 08-P1 | Legge sulla consulenza algoritmica pubblica | Valori | Piena 0,04 | Piena 0,04 | Essenziale 0,01 |
| 08-P2 | Patto per la buona legge | Coda | Piena 0,01 | Piena 0,01 | Zero 0,00 |
| 08-P3 | Regole del gioco stabili (legge elettorale, voto fuorisede) | Valori | Essenziale 0,01 | Essenziale 0,01 | Essenziale 0,01 |
| 08-P4 | Beni pubblici europei: capacità fiscale UE | Coda | Piena 0,00 | Piena 0,00 | Piena 0,00 |
| 08-P5 | Cooperazione che si misura: traiettoria APS | Coda | Zero 0,00 | Zero 0,00 | Zero 0,00 |
| 08-P6 | Export resiliente | Coda | — | — | — |
| 08-P7 | Appalti a vetro: cruscotto pubblico dei rischi e dati aperti completi | Valori | Piena 0,01 | Piena 0,01 | Piena 0,01 |
| **PA e Digitale** | [schede](programma/schede/09_pa_digitale.md) | | | | |
| 09-C1 | Stato a vetro: infrastruttura aperta per l'analisi delle politiche | Valori | Piena 0,07 | Piena 0,07 | Essenziale 0,04 |
| 09-C2 | Chiedilo una volta sola: once-only con rimborso automatico | Valori | Piena 0,35 | Essenziale 0,14 | Essenziale 0,14 |
| 09-C3 | Squadre tecniche della Repubblica: pool di competenze per i piccoli enti | **Nucleo** | Essenziale 0,22 | Essenziale 0,22 | Essenziale 0,22 |
| 09-C4 | Cloud pubblico sostenibile e Patto per la manutenzione digitale | Coda | Zero 0,00 | Zero 0,00 | Essenziale 0,12 |
| 09-C5 | AI nella PA con le mani sul volante | **Nucleo** | Essenziale 0,08 | Piena 0,22 | Piena 0,22 |
| 09-C6 | Lavoro pubblico misurato e giusto: organizzazione, valutazione vera e responsabilità | Valori | Piena 0,03 | Piena 0,03 | Piena 0,03 |
| 09-C7 | Automazione dei processi ripetitivi con riallocazione garantita | Valori | Piena 0,20 | Piena 0,20 | Essenziale 0,07 |
| 09-C8 | Staffetta delle competenze: il ricambio generazionale come occasione di riqualificazione | **Nucleo** | Essenziale 0,08 | Piena 0,23 | Essenziale 0,08 |
| 09-C9 | Squadra per la produttività pubblica con l'AI: meno lavoro ripetitivo, più servizi alle persone | Valori | Piena 0,09 | Piena 0,09 | — |
| 09-C10 | Bandi pubblici con istruttoria assistita: domande compilate una volta, controlli in giorni invece che in mesi | **Nucleo** | Piena 0,04 | Piena 0,04 | — |
| | **Totale** | | **8,23** | **13,57** | **11,63** |
<!-- /auto:misure -->

Come leggere le varianti:
- **Zero**: riforma di metodo senza costo, ad esempio un obbligo, una regola o un riordino;
- **Pilota**: sperimentazione con valutazione;
- **Essenziale**: il cuore della misura, graduale o mirato;
- **Piena**: la misura completa.

Il dettaglio di ogni variante è nelle schede. La robustezza della selezione al variare dei pesi è in `programma/selezione_livello1.md` e `selezione_livello2.md`.

## 4. Le coperture

Il dettaglio è in `programma/coperture_menu.csv`: 63 misure con gettito, chi paga, fonte ed effetto sui dieci valori. I valori sono in mld €/anno, gettito minimo.

<!-- auto:coperture -->
| Fondo | Programma base | Programma completo |
|---|---|---|
| Riordino delle spese fiscali oltre quanto già previsto nel Piano strutturale di bilancio | 1,70 | 4,50 |
| Riallocazione interna al bilancio del ministero | 1,57 | 2,69 |
| Riforma dei sussidi ambientalmente dannosi riformabili a livello nazionale | 1,08 | 2,53 |
| Accise e tasse su prodotti nocivi (tabacco, bevande zuccherate) | 0,97 | 0,97 |
| Rivalutazione ridotta delle pensioni più alte e risparmi dall'uscita dalle quote | 0,41 | 0,41 |
| Riordino di bonus e carte frammentati | 0,31 | 0,21 |
| Gettito aggiuntivo della tassa di soggiorno (Comuni) | 0,11 | 0,11 |
| **Totale coperture nuove (gettito minimo)** | **6,15** | **11,42** |
<!-- /auto:coperture -->

Il resto della spesa si finanzia con fondi già vincolati: coesione 2021-27 (solo investimenti una tantum), tariffe del servizio idrico e corrispettivi GSE.

**Escluse dalle verifiche.** Le linee rosse della Carta escludono le coperture regressive senza compensazione, come l'ulteriore aumento delle accise sul tabacco (AS05) e la soppressione del bonus lavoratrici madri (RB05). La verifica giuridica esclude l'IVA ridotta dal 10% al 12% (SF15, vietata dalla direttiva 2006/112/CE) e il contributo sui biglietti aerei differenziato tra voli nazionali e UE (SAD11, contrario all'art. 56 TFUE).

**Le misure di copertura più rilevanti**
- *Programma base*:
  - accisa sulle sigarette di circa 0,50 € a pacchetto (AS01);
  - detrazione per spese sanitarie decrescente tra 50.000 e 120.000 € di reddito, salve disabilità e patologie (SF06);
  - rimborso del gasolio per l'autotrasporto escluso per i veicoli Euro 5 dal 2028 (SAD01);
  - rivalutazione ridotta sulla sola quota delle pensioni più alte, dal 2030 (PE04);
  - regime forfetario al 20% tra 50.000 e 85.000 € di ricavi (SF02).
- *In più, nel programma completo* (circa 5,3 mld):
  - uscita entro il 2035 dal rimborso del gasolio per autotrasporto e agricoltura (SAD13);
  - revisione degli estimi catastali e IMU sulle abitazioni principali di valore alto (SF13);
  - abolizione della cedolare secca a canone libero (SF11);
  - revisione strutturale della spesa dei ministeri (RA13) e riordino degli incentivi alle imprese (RA14);
  - detrazioni per istruzione privata e interessi sui mutui futuri (FN01, FN03);
  - IVA ordinaria sulle abitazioni nuove non prima casa (SAD14) e sul gas domestico con bonus sociale (SAD12);
  - franchigia di successione ridotta da 1 milione a 500.000 € per erede (SF14).

## 5. Primi 100 giorni

Ogni scheda riporta il cronoprogramma dettagliato: 100 giorni, 12 mesi, fine legislatura, con chi fa cosa. In sintesi:

1. **Legge GovernAI** (08-P1) e **Stato a vetro** (09-C1) in Consiglio dei ministri. Nascono l'Ufficio per la consulenza algoritmica presso le Camere, il registro pubblico delle analisi e l'assemblea civica di persone sorteggiate, che fisserà i pesi tra i valori.
2. **Legge di bilancio**:
   - i fondi delle misure del nucleo;
   - le coperture del livello scelto, contate al minimo e con il profilo annuale;
   - la regola "nessun rinnovo automatico" per le misure temporanee;
   - il bilancio generazionale allegato a ogni provvedimento (01-P1).
3. **Decreti attuativi**:
   - piattaforma "tempo garantito" per le liste d'attesa;
   - soglie di carenza del personale sanitario;
   - elenco degli ambiti con meno del 33% di posti al nido;
   - censimento degli alloggi pubblici vuoti.
4. **Disegni di legge delega**: salario minimo contrattuale, patto previdenziale, riordino degli incentivi.

## 6. Le decisioni politiche che restano

Il sistema non decide al posto della cittadinanza. Su questi punti presenta le opzioni con il loro prezzo, calcolato con lo stesso ottimizzatore.

**1. Difesa.** Oggi la spesa è al 2,09% del PIL secondo la NATO (luglio 2026). Il panel classifica sfavorevole il percorso al 3,5%, perché senza deficit toglierebbe risorse a quasi tutte le altre misure: è un giudizio sul costo, non sulla sicurezza, e chi dà più peso alla sicurezza esterna può arrivare a una scelta diversa. Le versioni finanziate in deficit superano la linea rossa della Carta sulla responsabilità verso il futuro e sono escluse in automatico; le versioni senza deficit restano scelte possibili.

| Opzione | Costo aggiuntivo a regime | Effetto sul programma completo |
|---|---|---|
| Stabilizzazione al ~2,1% con efficienza e acquisti comuni UE | 0 | Programma completo invariato |
| Traiettoria graduale legata al debito (2,5% nel 2034) | +9,1 mld | Vedi l'elenco qui sotto |
| Obiettivo NATO 3,5% al 2035 | +32 mld | **Non finanziabile** senza deficit: supera tutte le coperture disponibili |

Con la traiettoria al 2,5%:

<!-- auto:difesa -->
- **Escono (11):** 01-P4 Crescere conviene: eliminare i gradini dimensionali; 01-P10 Controlli mirati con garanzie: usare meglio i dati che il fisco ha già, senza sorvegliare tutti; 01-P13 Un solo credito per la ricerca: stabile, più forte per le piccole imprese, certificato prima di spendere; 02-C2 Nido esigibile + congedo paterno; 03-P4 Prevenire costa meno: fondo prevenzione e assicurazione catastrofale; 03-P5 Contratto agro-climatico; 04-P7 Dal porto al treno: più merci sul ferro; 05-C4 Più persone con laurea o diploma terziario: ITS, lauree professionalizzanti, residenze; 07-C1 Giustizia a regime: Ufficio per il processo e triage digitale; 07-C3 Governance dei flussi migratori fondata sui dati; 07-C6 Scudo cyber territoriale.
- **Cambiano variante (31):** 01-P1 piena → zero; 01-P3 piena → essenziale; 01-P6 piena → zero; 01-P7 piena → essenziale; 01-P15 piena → zero; 02-C5 essenziale → zero; 02-C7 piena → essenziale; 03-P2 piena → zero; 04-P8 piena → zero; 04-P9 piena → zero; 05-C1 piena → essenziale; 05-C2 essenziale → pilota; 05-C5 piena → essenziale; 05-C6 piena → zero; 05-C8 piena → pilota; 05-C9 piena → pilota; 06-C3 essenziale → pilota; 06-C8 piena → pilota; 06-C9 piena → pilota; 06-C10 piena → pilota; 07-C2 piena → essenziale; 07-C4 piena → essenziale; 08-P1 piena → essenziale; 08-P3 essenziale → zero; 09-C1 piena → pilota; 09-C2 essenziale → zero; 09-C5 piena → essenziale; 09-C6 piena → essenziale; 09-C7 piena → pilota; 09-C8 piena → essenziale; 09-C9 piena → pilota.
<!-- /auto:difesa -->

**2. Dividendo climatico.** L'ottimizzatore usa il gettito dei sussidi dannosi per i servizi e non per il dividendo. Imporre il dividendo compensativo per redditi bassi e settori esposti (1,2 mld) cambia il programma completo così:

<!-- auto:dividendo -->
- **Escono (1):** 04-P7 Dal porto al treno: più merci sul ferro.
- **Cambiano variante (8):** 01-P6 piena → essenziale; 03-P1 zero → essenziale; 03-P5 essenziale → pilota; 04-P8 piena → zero; 05-C8 piena → essenziale; 06-C9 piena → pilota; 07-C2 piena → essenziale; 07-C6 piena → essenziale.
<!-- /auto:dividendo -->

**3. Coperture strutturali** (programma completo, circa 5,3 mld in più del base). Le pagano soprattutto chi possiede case di valore alto, chi affitta a canone libero, chi eredita patrimoni oltre 500.000 € per erede, le famiglie capienti con spese di istruzione privata, l'autotrasporto e l'agricoltura (fino al 2035), chi consuma gas (con un bonus per i redditi bassi). È la scelta più politica del programma: il sistema la presenta, non la impone.

**4. Ricerca, innovazione e logistica verde.** Le sette proposte nuove (01-P13, 01-P14, 01-P15, 05-C10, 04-P7, 04-P8, 04-P9) hanno benefici attesi positivi per tutti e tre i valutatori, ma con la Carta attuale finiscono in coda: per euro speso valgono meno di scuola, cura e Stato che funziona. Lasciato fare all'ottimizzatore, il programma intermedio le includeva solo in forma minima. Il 9 novembre 2026 chi guida il progetto ha scelto di imporle tutte almeno in versione essenziale nel programma intermedio. Costano circa 1 mld l'anno nello stesso tetto di spesa del programma intermedio. Il prezzo, dichiarato:
- **esce** 06-C3 Case della Comunità vive (0,8 mld in versione essenziale), che fa parte del nucleo robusto (dal 12 novembre 2026 rientra: vedi il punto 6);
- **scendono di variante** 09-C7 Automazione dei processi ripetitivi, 09-C1 Stato a vetro e 08-P3 Regole del gioco stabili.

È una scelta politica, non un risultato del motore: dà più peso alla crescita e all'innovazione di quanto faccia la Carta attuale. Gli altri scenari restano calcolati senza vincoli.

**5. Squadra per la produttività pubblica con l'AI (09-C9).** Il 10 novembre 2026 chi guida il progetto ha chiesto una squadra dedicata alle efficienze che l'AI può dare alla PA: togliere lavoro ripetitivo, ridurre nel tempo i posti non più necessari solo con i pensionamenti e dopo certificazione, e spostare chi lo desidera, nello stesso comune e con formazione pagata, verso lavori utili alla comunità (servizi sociali, sanità amministrativa, controlli, uffici giudiziari). Nessun licenziamento e nessun trasferimento senza consenso. Il panel la giudica positiva su tutti i valori tranne patrimonio e sicurezza (neutri); l'ottimizzatore la inseriva solo come pilota da 25 persone. Per scelta politica entra nel programma intermedio in versione essenziale (circa 70 persone, 0,045 mld al picco, 0,03 a regime). Il prezzo, dichiarato:
- **scendono al minimo** 04-P4 Nessuna grande opera senza prova dei numeri (resta l'obbligo di pubblicare le analisi) e 09-C6 Lavoro pubblico misurato e giusto (resta la direttiva);
- **esce** il pilota di 09-C1 Stato a vetro;
- **sale** 01-P12 Pagare è semplice, da essenziale a piena.

La verifica giuridica è «condizionata»: la legge deve derogare espressamente alle regole su eccedenze e trasferimenti (artt. 30, 33-34 d.lgs. 165/2001), rispettare l'AI Act e quantificare la nuova copertura R12-2 (posta, stampa e archivi cartacei dello Stato) su capitoli certificati dalla RGS.

**6. La sanità senza tasse in più.** Il 12 novembre 2026 chi guida il progetto ha chiesto di far entrare la sanità nel programma intermedio **senza tasse in più oltre quelle già previste** (accise su tabacco, alcol e bevande zuccherate, forfettario, rivalutazione ridotta delle pensioni più alte), perché giudica il sistema fiscale già iniquo, e di distribuire i sacrifici senza togliere troppo a nessuna funzione. Un agente ha studiato più combinazioni con l'ottimizzatore; la scelta è caduta sulla più equilibrata. Entrano:
- 06-C3 Case della Comunità vive, in versione essenziale (0,80 mld);
- 06-C8 Squadre infermieristiche di quartiere, da pilota a essenziale: 500 squadre per l'assistenza a domicilio (0,10 mld);
- 06-C10 Meno burocrazia, più cura, nuova proposta: automazione degli uffici sanitari e riqualificazione volontaria degli amministrativi (0,02 mld a regime), con la nuova copertura RP08 (ricambio selettivo degli amministrativi del SSN, 0,05-0,13 mld).

Il prezzo, dichiarato: nessuna misura del nucleo robusto esce (tutte e 22 restano nel programma, 21 con spesa: 02-C5 è solo regole), ma molte scendono di un gradino:
- **scuola**: 05-C4 più persone con laurea o diploma ITS e 05-C5 scuole aperte, da piena a essenziale;
- **innovazione**: 05-C10 rete per la ricerca applicata, 04-P7 dal porto al treno e 01-P14 Sfide Italia diventano pilota; 01-P15 spin-off resta solo come regole; 04-P8 camion a zero emissioni scende a essenziale; restano pieni 01-P13 credito per la ricerca e 04-P9 consegne pulite;
- **fisco e istituzioni**: 01-P12 da piena a essenziale; ritocchi minimi a 01-P2, 08-P2, 08-P7.

Tre limiti, dichiarati: il margine sulle risorse generali è nullo (coprono la spesa esatta; il margine mostrato nei totali è di fondi vincolati non spostabili); circa 1,7 mld di spesa sono pagati con i fondi europei di coesione 2021-2027, che finiscono nel 2029 e andranno sostituiti; il personale infermieristico nuovo (06-C2) resta fuori, e senza di esso le Case della Comunità perdono efficacia; il ricambio selettivo di RP08 cresce negli anni e potrà finanziarne una parte. Ricerca di confronto in `benchmark/nord_europa_efficienza_spesa.md`.

**7. Bandi pubblici con istruttoria assistita (09-C10).** Il 12 novembre 2026 chi guida il progetto ha proposto di portare a livello nazionale un'esperienza diretta in un ufficio regionale, descritta in forma anonima: uno strumento costruito in tre giorni con l'AI, che fa i controlli ripetitivi di un bando e lascia la decisione al funzionario. I tre valutatori la giudicano positiva su quasi tutti i valori, soprattutto fiducia e innovazione, e il motore la mette nel **nucleo robusto** (prima metà della classifica nell'89% delle combinazioni di pesi). Il problema che affronta è misurato: al 31 agosto 2025 l'Italia aveva pagato l'8,03% dei fondi strutturali europei 2021-2027 (RGS). Nel programma intermedio entra come **pilota** (10 bandi in 3 Regioni, 0,01 mld su fondi europei di assistenza tecnica): non toglie risorse ad altre misure e parte misurando il tempo risparmiato, che oggi non è ancora noto. La versione essenziale costerebbe 0,02 mld l'anno di risorse generali, oggi senza margine. Verifica giuridica condizionata: articolato corretto su responsabile del procedimento, preavviso di rigetto, dati e AI Act (`giuridico/conformita_BANDI.csv`).

## 7. Cosa manca e cosa fare dopo

- **Costi stimati, non certificati.** I costi delle varianti e molti gettiti sono "stime GovernAI". Il passo successivo è la verifica con la Ragioneria o con l'UPB, e microsimulazioni distributive su microdati, che richiedono un accesso istituzionale.
- **Doppioni da escludere.** Le spese fiscali del menu vanno confrontate voce per voce con la lista dei 7,37 mld già nel Piano strutturale.
- **Utilità delle varianti.** È calcolata come intensità × utilità della proposta piena. Il panel dovrebbe valutare direttamente le varianti essenziali e le misure di copertura.
- **Proposte escluse o ridotte, ma di valore.** Salute mentale e nuovo personale infermieristico restano fuori; non autosufficienza e reddito di inclusione sono solo sperimentazioni. Il motivo è la mancanza di risorse certificate, non il poco valore.
- **Revisione esterna.** Una prima analisi politica, scritta da un agente AI, è in `revisioni/2026-11-08_analista_politico.md`. Serve ora una revisione critica di persone con orientamenti politici diversi, e un confronto tra i punteggi degli agenti e quelli di un panel di persone.
