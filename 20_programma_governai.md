# Programma GovernAI

*Versione 2.0, 8 novembre 2026, sulla Carta dei valori 2.0 (dieci valori). Un programma di governo né di destra né di sinistra né di centro: ogni misura è giudicata sui valori dichiarati nella Carta, è finanziata senza deficit e ha una scheda pronta per l'attuazione.*

*Le cifre in tabella sono generate da `programma/documento.py` a partire dal motore e dall'ottimizzatore: non si correggono a mano. I dati aggiornati ogni giorno sono nel sito (`docs/`).*

## 1. In sintesi

Due versioni del programma, entrambe finanziate senza deficit nello scenario prudente: gettito minimo delle coperture, nessun risparmio non certificato, nessun recupero di evasione usato come copertura. Accanto, il programma che il governo ombra ha adottato nella seduta «Conti in ordine» (simulazione: le decisioni non sono in vigore).

<!-- auto:totali -->
- **Programma base: 7,62 mld l'anno**, 80 misure su 95, con 30 su 33 del nucleo robusto almeno in versione essenziale. Usa solo coperture a basso costo sociale.
- **Programma completo: 14,06 mld l'anno**, 85 misure, nucleo robusto 33 su 33. Aggiunge coperture strutturali più impegnative.
- **Programma intermedio: 8,52 mld l'anno**, 80 misure, nucleo robusto 21 su 33 (sotto la versione essenziale: 09-C10 e 02-C5 e 07-C1 e 07-C3 per eccezioni dichiarate). Nessun aumento di aliquote su casa, eredità, affitti e IVA, nessun contributo straordinario sulle pensioni; più istruzione e servizi sociali, con tagli di spesa e di personale nei ministeri. Dopo la verifica delle coperture della sera del 13 novembre 2026 restano il nucleo robusto, le squadre infermieristiche di quartiere (06-C8) e la compensazione dell'autotrasporto (04-P8); dopo la verifica delle ultime otto coperture, il 14 novembre, l'Ufficio per il processo (07-C1) e il governo dei flussi migratori (07-C3) passano a pilota; dal 12 novembre 2026 entrano, senza tasse in più oltre quelle già nel programma, le Case della Comunità (06-C3), 500 squadre infermieristiche di quartiere (06-C8) e la riqualificazione degli amministrativi della sanità (06-C10); dal 13 novembre il progetto di vita per le persone con disabilità (02-C5) parte come pilota sui fondi europei mentre il personale infermieristico (06-C2), il credito per la ricerca (01-P13), il pilota del reddito di inclusione (02-C4) e le merci sul treno (04-P7) escono; 0,06 mld di risorse generali restano da parte per smettere di fumare e per il dopo 2029. Dal 21 novembre entra il dividendo dell'automazione (09-C11): dove le macchine fanno meglio, chi va in pensione non viene sostituito e il risparmio certificato va per l'80% a ridurre le tasse sul lavoro, con regole contro chi aggira i conti (0,015 mld l'anno). Restano accise su tabacco, alcol e bevande zuccherate, il riordino di alcune agevolazioni fiscali e dei sussidi dannosi, e dal 2030 una rivalutazione ridotta sulla quota più alta delle pensioni (`programma/selezione_intermedio.md`).
- **Programma adottato dal governo ombra** (simulazione, `governo/`): 11,63 mld l'anno, 55 misure, coperture al minimo per 11,12 mld più i fondi vincolati.
<!-- /auto:totali -->

- **Il nucleo robusto viene prima.** Sono le misure (oggi 33) prioritarie con quasi ogni combinazione di pesi tra i valori: si finanziano almeno in versione essenziale prima di ottimizzare il resto. Erano 23 fino al 15 novembre 2026 e 30 fino alle scelte del 16 novembre: il perché dei cambi è nei punti 15 e 16 di §6. Le eccezioni sono dichiarate una per una: 09-C10 resta pilota per scelta finché il pilota non ne misura i risparmi; 02-C5 (progetto di vita per le persone con disabilità) è pilota nel quarto degli ambiti con meno servizi, perché la versione essenziale costa 0,8 mld l'anno di risorse generali, oggi tutte impegnate. Nel programma intermedio restano fuori, per scelte precedenti, la casa a canone giusto (04-P2) e i treni per chi viaggia ogni giorno (04-P3), anche se ora sono nel nucleo.
- **L'eccezione del programma base è il nido (02-C2).** È l'unica misura del nucleo che il base non finanzia. La sua versione essenziale costa 2,0 mld l'anno e si paga con il riordino dei bonus familiari e delle spese fiscali. Nel base queste risorse non bastano, anche perché la linea rossa sull'equità esclude la soppressione del bonus lavoratrici madri (RB05). Entra nel programma completo e nella decisione del governo ombra.
- **L'impianto istituzionale costa poco**: legge sulla consulenza algoritmica pubblica (08-P1), bilancio generazionale (01-P1), una scheda di valutazione pubblica per ogni spesa fiscale (01-P2), prova dei numeri per le grandi opere (04-P4), appalti a vetro (08-P7). Sono tra le 38 riforme a costo quasi zero che partono subito; sei hanno già un testo pronto (`pacchetto/`).
- **Restano decisioni politiche**, presentate con il loro prezzo (§6): la traiettoria della Difesa, il dividendo climatico, l'adozione delle coperture strutturali.

## 2. Come è stato costruito

| Passo | Cosa | Dove |
|---|---|---|
| 1 | 9 dossier ministeriali e 95 proposte: 12 su fisco semplice, evasione, PA produttiva e integrità degli appalti, 9 su equità fiscale e integrità pubblica (`benchmark/equita_fiscale_diagnosi.md`, `benchmark/anticorruzione_diagnosi.md`), 6 nate dal confronto con il Nord Europa su scuola, servizi sociali e cultura (`benchmark/proposte_nord_europa.md`), 4 su ricerca e innovazione (`benchmark/ricerca_innovazione.md`) e 3 sulla logistica verde (`benchmark/logistica_green.md`); dal 16 novembre 2 su grandi patrimoni e imprese di persone (`analisi/chi_paga/`) | `ministeri/`, `programma/schede/` |
| 2 | Verifica di 334 cifre su fonte primaria; base dati riproducibile | `dati/` |
| 3 | Vincolo di bilancio ufficiale: margine in deficit zero | `dati/verifiche/00_vincolo_bilancio.md` |
| 4 | Carta dei 10 valori: Rispetto e diversità, Fiducia e trasparenza, Innovazione, Benessere, Apprendimento e cultura, Bellezza patrimonio e accoglienza, Responsabilità verso il futuro, Equità, Sicurezza senza controllo assoluto, Cittadinanza responsabile | `01_carta_valori.md` |
| 5 | Panel di 3 valutatori (agenti AI distinti da chi ha scritto le proposte; alfa di Krippendorff 0,85) e motore SMAA su 20.000 combinazioni di pesi | `motore/` |
| 6 | 284 varianti (piena, essenziale, pilota, zero) e 100 misure di copertura concrete, con verifica fiscale, costituzionale ed europea | `programma/varianti/`, `programma/coperture_menu.csv`, `giuridico/` |
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
| 01-P1 | Bilancio generazionale: ogni legge dichiara chi paga e quando | Coda | Essenziale 0,01 | Piena 0,02 | Essenziale 0,01 |
| 01-P2 | Spese fiscali a scadenza (sunset 5 anni) | Valori | Piena 0,01 | Piena 0,01 | Piena 0,01 |
| 01-P3 | IVA in tempo reale | **Nucleo** | Essenziale 0,08 | Piena 0,15 | Essenziale 0,08 |
| 01-P4 | Crescere conviene: eliminare i gradini dimensionali | Coda | — | Zero 0,01 | Zero 0,01 |
| 01-P5 | Energia a prezzo stabile per le PMI (PPA rinnovabili) | Coda | Essenziale 0,15 | — | Essenziale 0,15 |
| 01-P6 | Turismo che ripaga i territori: tassa di soggiorno intelligente | Valori | Zero 0,00 | Piena 0,15 | Zero 0,00 |
| 01-P7 | Dichiarazione zero: lo Stato fa il conto, chi dichiara controlla | **Nucleo** | Essenziale 0,15 | Piena 0,30 | Essenziale 0,15 |
| 01-P8 | Meno scontrini: riordino delle detrazioni del 19% | Coda | Zero 0,00 | Essenziale 0,20 | Essenziale 0,20 |
| 01-P9 | Una sola detrazione per il lavoro, senza scalini | Coda | Zero 0,00 | Zero 0,00 | Zero 0,00 |
| 01-P10 | Controlli mirati con garanzie: usare meglio i dati che il fisco ha già, senza sorvegliare tutti | Valori | — | Piena 0,10 | Essenziale 0,06 |
| 01-P11 | Lo scontrino che conviene: un incentivo mirato al posto di lotterie e cashback | Coda | Zero 0,00 | Zero 0,00 | Zero 0,00 |
| 01-P12 | Pagare è semplice, condonare no: semplificazione, riscossione efficace, sanzioni proporzionate | **Nucleo** | Piena 0,06 | Piena 0,06 | Essenziale 0,04 |
| 01-P13 | Un solo credito per la ricerca: stabile, più forte per le piccole imprese, certificato prima di spendere | Coda | — | Zero 0,01 | — |
| 01-P14 | Sfide Italia: la pubblica amministrazione compra innovazione in tre fasi | Coda | Pilota 0,03 | — | — |
| 01-P15 | Dalla scoperta all'impresa: prove di fattibilità, regole per gli spin-off, fondo di fondi deep tech | Coda | Zero 0,00 | Piena 0,10 | — |
| 01-P16 | Tetti di spesa triennali per ministero, con riserva e regola sulle entrate inattese | Coda | Piena 0,00 | Piena 0,00 | — |
| 01-P17 | UPB più forte: revisioni della spesa indipendenti, rispetta o spiega, analisi volontaria dei programmi elettorali | Valori | Piena 0,01 | Piena 0,01 | — |
| 01-P18 | Registro mensile dei redditi Entrate-INPS per conto fiscale e prestazioni | Valori | Piena 0,04 | Piena 0,04 | — |
| 01-P19 | Holding personali: sugli utili parcheggiati la stessa imposta che possedendo direttamente, con le imprese operative e chi reinveste esclusi | Coda | Piena 0,02 | Piena 0,02 | — |
| 01-P21 | Fine dei contenitori: polizze vita senza rischio assicurativo e trust esteri opachi tassati come investimenti | Coda | Piena 0,00 | Piena 0,00 | — |
| 01-P22 | Eredità: l'impresa che lavora resta esente, il patrimonio passivo no; gli eredi mantengono il costo fiscale oltre 1 mln | Coda | Piena 0,00 | Piena 0,00 | — |
| 01-P23 | Sapere chi paga quanto: statistica ufficiale delle aliquote effettive e unità per i grandi patrimoni con adempimento collaborativo | Valori | Piena 0,01 | Piena 0,01 | — |
| 01-P24 | Grandi patrimoni: un'imposta minima solo sopra 50 milioni, meno le imposte sul reddito già pagate, con exit tax e valutazione uguale per tutti i beni; prima si misura | Coda | — | Essenziale 0,02 | — |
| 01-P25 | Imprese di persone come le SRL: 24% sugli utili lasciati in azienda da ditte, SNC e SAS in contabilità ordinaria, IRPEF solo su ciò che si preleva; pagata dalla patrimoniale minima | Coda | Zero 0,00 | Zero 0,00 | — |
| **Lavoro, Welfare, Famiglia** | [schede](programma/schede/02_lavoro.md) | | | | |
| 02-C1 | Salario minimo contrattuale garantito | Valori | Zero 0,00 | Zero 0,00 | Essenziale 0,20 |
| 02-C2 | Nido esigibile + congedo paterno | **Nucleo** | — | Essenziale 2,00 | Essenziale 2,00 |
| 02-C3 | Patto previdenziale tra generazioni | Valori | Zero 0,00 | Zero 0,00 | Essenziale 0,35 |
| 02-C4 | Reddito di inclusione universale | Valori | — | — | Pilota 0,10 |
| 02-C5 | Progetto di vita esigibile e lavoro per le persone con disabilità | **Nucleo** | Zero 0,00 | Essenziale 0,80 | Essenziale 0,80 |
| 02-C6 | Bilancio generazionale e strategia demografica | Coda | Zero 0,00 | Zero 0,00 | Zero 0,00 |
| 02-C7 | Housing First dopo il PNRR | **Nucleo** | Essenziale 0,09 | Piena 0,15 | — |
| 02-C8 | Aggancio protetto e correttore automatico e temporaneo sulla spesa pensionistica | Coda | Piena 0,00 | Piena 0,00 | — |
| 02-C9 | Politiche attive dopo il PNRR: nucleo minimo di GOL | Valori | Pilota 0,03 | — | — |
| **Ambiente, Energia, Agricoltura** | [schede](programma/schede/03_ambiente.md) | | | | |
| 03-P1 | Dividendo climatico: riforma SAD restituita alla cittadinanza | Valori | Zero 0,00 | Zero 0,00 | Essenziale 1,20 |
| 03-P2 | Elettricità rinnovabile a prezzo rinnovabile (CfD) | **Nucleo** | Essenziale 0,07 | Piena 0,15 | Essenziale 0,07 |
| 03-P3 | Ogni goccia conta: reti idriche e riuso | **Nucleo** | Essenziale 0,60 | Essenziale 0,60 | — |
| 03-P4 | Prevenire costa meno: fondo prevenzione e assicurazione catastrofale | **Nucleo** | Essenziale 0,80 | Essenziale 0,80 | Essenziale 0,80 |
| 03-P5 | Contratto agro-climatico | **Nucleo** | Essenziale 0,25 | Essenziale 0,25 | Pilota 0,05 |
| **Infrastrutture e Territori** | [schede](programma/schede/04_infrastrutture.md) | | | | |
| 04-P1 | Patto di continuità post-PNRR | Valori | — | — | — |
| 04-P2 | Casa a canone giusto | **Nucleo** | Essenziale 0,48 | Essenziale 0,48 | Essenziale 0,48 |
| 04-P3 | Prima il treno di chi viaggia ogni giorno: fondo TPL e abbonamento unico | **Nucleo** | — | Essenziale 1,17 | Pilota 0,62 |
| 04-P4 | Nessuna grande opera senza prova dei numeri | **Nucleo** | Piena 0,03 | Piena 0,03 | Piena 0,03 |
| 04-P5 | LEP prima: autonomia differenziata reversibile | Valori | Zero 0,00 | Zero 0,00 | Zero 0,00 |
| 04-P6 | Restare è possibile: servizi essenziali aree interne | **Nucleo** | Essenziale 0,42 | Essenziale 0,42 | Essenziale 0,42 |
| 04-P7 | Dal porto al treno: più merci sul ferro | Coda | — | Pilota 0,06 | — |
| 04-P8 | Camion a zero emissioni: patto per la transizione dell'autotrasporto | Coda | Zero 0,00 | Zero 0,00 | — |
| 04-P9 | Consegne pulite in città: zone a emissioni zero per le merci | Coda | Zero 0,00 | Zero 0,00 | — |
| **Istruzione, Ricerca, Cultura** | [schede](programma/schede/05_istruzione.md) | | | | |
| 05-C1 | Nessuna esclusione: squadre di prossimità contro la dispersione | **Nucleo** | Essenziale 0,13 | Essenziale 0,13 | Piena 0,25 |
| 05-C2 | Conto personale di competenze | **Nucleo** | Essenziale 0,45 | Essenziale 0,45 | Essenziale 0,45 |
| 05-C3 | Carriere della ricerca | Valori | Zero 0,00 | Zero 0,00 | Zero 0,00 |
| 05-C4 | Più persone con laurea o diploma terziario: ITS, lauree professionalizzanti, residenze | **Nucleo** | Essenziale 0,45 | Essenziale 0,45 | Essenziale 0,45 |
| 05-C5 | Scuole aperte come presidi di comunità | **Nucleo** | Essenziale 0,20 | Piena 0,40 | Essenziale 0,20 |
| 05-C6 | AI a scuola | Valori | Zero 0,00 | Essenziale 0,08 | Essenziale 0,08 |
| 05-C7 | Quota svantaggio nel finanziamento delle scuole | **Nucleo** | Essenziale 0,19 | Essenziale 0,19 | — |
| 05-C8 | Biblioteche di comunità | **Nucleo** | Essenziale 0,14 | Piena 0,33 | — |
| 05-C9 | Zaino culturale a scuola e tariffa sociale della cultura | Valori | Pilota 0,02 | Piena 0,20 | — |
| 05-C10 | Rete nazionale per la ricerca applicata sul modello Fraunhofer | Coda | Pilota 0,05 | — | — |
| **Salute** | [schede](programma/schede/06_salute.md) | | | | |
| 06-C1 | Tempo garantito o rimborso | Valori | Zero 0,00 | Zero 0,00 | Zero 0,00 |
| 06-C2 | Patto per il personale infermieristico e la medicina generale | Valori | — | — | Pilota 0,35 |
| 06-C3 | Case della Comunità vive | **Nucleo** | Essenziale 0,80 | Essenziale 0,80 | — |
| 06-C4 | Budget di cura per la non autosufficienza | Valori | — | — | — |
| 06-C5 | Salute mentale al 5% | Valori | — | — | — |
| 06-C6 | Dividendo della prevenzione e budget unico del farmaco | Coda | Zero 0,00 | Zero 0,00 | Zero 0,00 |
| 06-C8 | Squadre infermieristiche autonome di quartiere per l'ADI | Valori | Pilota 0,02 | Piena 0,25 | — |
| 06-C9 | Equipe di benessere scolastico in rete con la Casa della Comunità | Coda | Pilota 0,03 | Piena 0,20 | — |
| 06-C10 | Meno burocrazia, più cura: automazione degli uffici sanitari e riqualificazione del personale amministrativo | Coda | Pilota 0,01 | Piena 0,04 | — |
| **Giustizia, Interno, Difesa** | [schede](programma/schede/07_giustizia.md) | | | | |
| 07-C1 | Giustizia a regime: Ufficio per il processo e triage digitale | **Nucleo** | Essenziale 0,32 | Essenziale 0,32 | Essenziale 0,32 |
| 07-C2 | Pena utile: misure di comunità contro il sovraffollamento | **Nucleo** | Essenziale 0,25 | Piena 0,45 | Essenziale 0,25 |
| 07-C3 | Governance dei flussi migratori fondata sui dati | **Nucleo** | Essenziale 0,25 | Essenziale 0,25 | Essenziale 0,25 |
| 07-C4 | Dal bene confiscato al bene comune | **Nucleo** | Essenziale 0,07 | Piena 0,15 | Essenziale 0,07 |
| 07-C5 | Difesa: percorso NATO 3,5% vincolato a efficienza europea | Sfav. · linea rossa in alcune versioni | — | — | — |
| 07-C6 | Scudo cyber territoriale | **Nucleo** | Essenziale 0,18 | Essenziale 0,18 | Essenziale 0,18 |
| 07-C7 | Direttiva anticorruzione recepita bene, con un reato stretto e tutele contro la paura della firma, e sostegno a chi segnala | Coda | Piena 0,01 | Piena 0,01 | — |
| **Esteri, Europa, Istituzioni** | [schede](programma/schede/08_esteri.md) | | | | |
| 08-P1 | Legge sulla consulenza algoritmica pubblica | Valori | Essenziale 0,01 | Piena 0,04 | Essenziale 0,01 |
| 08-P2 | Patto per la buona legge | Coda | Piena 0,01 | Piena 0,01 | Zero 0,00 |
| 08-P3 | Regole del gioco stabili (legge elettorale, voto fuorisede) | Valori | Zero 0,00 | Essenziale 0,01 | Essenziale 0,01 |
| 08-P4 | Beni pubblici europei: capacità fiscale UE | Coda | Piena 0,00 | Piena 0,00 | Piena 0,00 |
| 08-P5 | Cooperazione che si misura: traiettoria APS | Coda | Zero 0,00 | Zero 0,00 | Zero 0,00 |
| 08-P6 | Export resiliente | Coda | — | Pilota 0,03 | — |
| 08-P7 | Appalti a vetro: cruscotto pubblico dei rischi e dati aperti completi | **Nucleo** | Piena 0,01 | Piena 0,01 | Piena 0,01 |
| 08-P8 | Influenza alla luce del sole: registro obbligatorio delle lobby per tutti, parti sociali comprese, agenda pubblica e impronta legislativa | Coda | Piena 0,00 | Piena 0,00 | — |
| 08-P9 | Integrità di chi decide: dichiarazioni verificate, conflitti di interessi e porte girevoli | Coda | Piena 0,01 | Piena 0,01 | — |
| 08-P10 | Chi c'è dietro: titolare effettivo verificato per gare e fondi pubblici | Coda | Piena 0,00 | Piena 0,00 | — |
| 08-P11 | Verifiche a sorte: audit casuali sorteggiati sugli enti che spendono fondi pubblici | Valori | Piena 0,01 | Piena 0,01 | — |
| **PA e Digitale** | [schede](programma/schede/09_pa_digitale.md) | | | | |
| 09-C1 | Stato a vetro: infrastruttura aperta per l'analisi delle politiche | Valori | — | Piena 0,07 | Essenziale 0,04 |
| 09-C2 | Chiedilo una volta sola: once-only con rimborso automatico | **Nucleo** | Essenziale 0,14 | Essenziale 0,14 | Essenziale 0,14 |
| 09-C3 | Squadre tecniche della Repubblica: pool di competenze per i piccoli enti | **Nucleo** | Essenziale 0,22 | Essenziale 0,22 | Essenziale 0,22 |
| 09-C4 | Cloud pubblico sostenibile e Patto per la manutenzione digitale | Coda | Zero 0,00 | Zero 0,00 | Essenziale 0,12 |
| 09-C5 | AI nella PA con le mani sul volante | **Nucleo** | Essenziale 0,08 | Essenziale 0,08 | Piena 0,22 |
| 09-C6 | Lavoro pubblico misurato e giusto: organizzazione, valutazione vera e responsabilità | Valori | Essenziale 0,01 | Piena 0,03 | Piena 0,03 |
| 09-C7 | Automazione dei processi ripetitivi con riallocazione garantita | Valori | Pilota 0,02 | Pilota 0,02 | Essenziale 0,07 |
| 09-C8 | Staffetta delle competenze: il ricambio generazionale come occasione di riqualificazione | **Nucleo** | Essenziale 0,08 | Piena 0,23 | Essenziale 0,08 |
| 09-C9 | Squadra per la produttività pubblica con l'AI: meno lavoro ripetitivo, più servizi alle persone | **Nucleo** | Essenziale 0,04 | Piena 0,09 | — |
| 09-C10 | Bandi pubblici con istruttoria assistita: domande compilate una volta, controlli in giorni invece che in mesi | **Nucleo** | Piena 0,04 | Piena 0,04 | — |
| 09-C11 | Dividendo dell'automazione: meno posti nelle attività ripetitive, meno tasse, regole contro l'elusione | Coda | Piena 0,01 | Piena 0,01 | — |
| | **Totale** | | **7,62** | **14,06** | **11,63** |
<!-- /auto:misure -->

Come leggere le varianti:
- **Zero**: riforma di metodo senza costo, ad esempio un obbligo, una regola o un riordino;
- **Pilota**: sperimentazione con valutazione;
- **Essenziale**: il cuore della misura, graduale o mirato;
- **Piena**: la misura completa.

Il dettaglio di ogni variante è nelle schede. La robustezza della selezione al variare dei pesi è in `programma/selezione_livello1.md` e `selezione_livello2.md`.

## 4. Le coperture

Il dettaglio è in `programma/coperture_menu.csv`: 97 misure con gettito, chi paga, fonte ed effetto sui dieci valori. I valori sono in mld €/anno, gettito minimo.

<!-- auto:coperture -->
| Fondo | Programma base | Programma completo |
|---|---|---|
| Riordino delle spese fiscali oltre quanto già previsto nel Piano strutturale di bilancio | 1,90 | 5,42 |
| Riforma dei sussidi ambientalmente dannosi riformabili a livello nazionale | 1,10 | 2,63 |
| Riallocazione interna al bilancio del ministero | 1,06 | 2,52 |
| Accise e tasse su prodotti nocivi (tabacco, bevande zuccherate) | 0,97 | 0,97 |
| Riordino di bonus e carte frammentati | 0,31 | 0,21 |
| Contributo di equità sulle pensioni più alte e risparmi dall'uscita dalle quote | 0,11 | 0,11 |
| Gettito aggiuntivo della tassa di soggiorno (Comuni) | 0,11 | 0,11 |
| **Totale coperture nuove (gettito minimo)** | **5,56** | **11,98** |
<!-- /auto:coperture -->

Il resto della spesa si finanzia con fondi già vincolati: coesione 2021-27 (solo investimenti una tantum), tariffe del servizio idrico e corrispettivi GSE.

**Escluse dalle verifiche.** Le linee rosse della Carta escludono le coperture regressive senza compensazione, come l'ulteriore aumento delle accise sul tabacco (AS05) e la soppressione del bonus lavoratrici madri (RB05). La verifica giuridica esclude l'IVA ridotta dal 10% al 12% (SF15, vietata dalla direttiva 2006/112/CE) e il contributo sui biglietti aerei differenziato tra voli nazionali e UE (SAD11, contrario all'art. 56 TFUE).

**Le misure di copertura più rilevanti**
- *Programma base*:
  - accisa sulle sigarette di circa 0,50 € a pacchetto (AS01);
  - detrazione per spese sanitarie decrescente tra 50.000 e 120.000 € di reddito, salve disabilità e patologie (SF06);
  - rimborso del gasolio per l'autotrasporto escluso per i veicoli Euro 5 dal 2028 (SAD01);
  - rivalutazione ridotta sulla sola quota delle pensioni più alte, dal 2030 (PE04);
  - regime forfetario al 20% tra 50.000 e 85.000 € di ricavi (SF02);
  - dal 15 novembre 2026, piccoli risparmi nuovi: niente nuovi Piani individuali di risparmio agevolati dal 2028 (SF21), compensi della libera professione dei medici del SSN nel reddito al 100% (SF23), sovvenzioni all'ippica e contributi a TV e radio locali ridotti (RA50, RA51), compenso ai CAF dimezzato per i 730 precompilati inviati senza modifiche (RA52).
- *In più, nel programma completo* (circa 5,9 mld):
  - uscita entro il 2035 dal rimborso del gasolio per autotrasporto e agricoltura (SAD13);
  - revisione degli estimi catastali e IMU sulle abitazioni principali di valore alto (SF13);
  - abolizione della cedolare secca a canone libero (SF11);
  - revisione strutturale della spesa dei ministeri (RA13) e riordino degli incentivi alle imprese (RA14);
  - detrazioni per istruzione privata e interessi sui mutui futuri (FN01, FN03); la detrazione per istruzione si toglie solo insieme alla quota studio dell'Assegno unico (01-P8 essenziale). Nel programma base e nell'intermedio queste due detrazioni restano;
  - IVA ordinaria sulle abitazioni nuove non prima casa (SAD14) e sul gas domestico con bonus sociale (SAD12);
  - franchigia di successione ridotta da 1 milione a 500.000 € per erede (SF14);
  - dal 15 novembre 2026: un nuovo contributo di Regioni e Comuni alla finanza pubblica per il 2030-2033 (RA30, 0,5-0,9 mld, la misura più esposta davanti alla Corte costituzionale), il risparmio d'imposta sui fondi pensione limitato al 33% sopra 50.000 € di reddito (SF22) e un regime meno generoso per chi si trasferisce in Italia dal 2028 (impatriati, SF20).

## 5. Primi 100 giorni

Ogni scheda riporta il cronoprogramma dettagliato: 100 giorni, 12 mesi, fine legislatura, con chi fa cosa. Il calendario di avvio (punto 7 di "Cosa manca") dice che il 2027 è un anno di preparazione: la spesa vera parte dal 2028, quando rendono le coperture. Quindi i primi 100 giorni servono a fare le regole che costano poco e ad approvare le coperture. In sintesi:

1. **Le riforme a costo quasi zero, subito.** Partono per intero le 38 misure che costano al massimo 20 milioni l'anno. Sei hanno già un testo pronto da presentare, nel pacchetto "pronto domani" (`pacchetto/`): tempi e valutazione degli incentivi alle imprese (09-C10, art. 5), prova dei numeri per le grandi opere (04-P4), appalti a vetro (08-P7), "chiedilo una volta sola" (09-C2), una scheda di valutazione per ogni spesa fiscale (01-P2) e la legge sulla consulenza algoritmica pubblica (08-P1), con una sezione di valutazione d'impatto presso l'Ufficio parlamentare di bilancio.
2. **Legge di bilancio**:
   - le coperture del livello scelto, contate al minimo e con il loro profilo anno per anno;
   - i fondi delle misure del nucleo, con il calendario di avvio: nessun anno in deficit;
   - il vincolo del gettito del tabacco alla sanità vicino a casa e i servizi per smettere di fumare dal 2028;
   - la regola "nessun rinnovo automatico" per le misure temporanee e il bilancio generazionale allegato a ogni provvedimento (01-P1).
3. **Decreti attuativi e avvisi**:
   - piattaforma "tempo garantito" per le liste d'attesa (06-C1);
   - elenco degli ambiti con meno di 33 posti al nido ogni 100 bambine e bambini (02-C2);
   - avvisi per le sperimentazioni pagate con i fondi europei, che devono partire subito per dare risultati entro il 2029 (02-C5, 06-C4, 09-C10 e le altre).
4. **Disegni di legge delega**: salario minimo contrattuale (02-C1) e patto previdenziale (02-C3), nella versione "solo regole".

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
- **Escono (16):** 01-P4 Crescere conviene: eliminare i gradini dimensionali; 01-P10 Controlli mirati con garanzie: usare meglio i dati che il fisco ha già, senza sorvegliare tutti; 01-P13 Un solo credito per la ricerca: stabile, più forte per le piccole imprese, certificato prima di spendere; 01-P18 Registro mensile dei redditi Entrate-INPS per conto fiscale e prestazioni; 02-C2 Nido esigibile + congedo paterno; 03-P4 Prevenire costa meno: fondo prevenzione e assicurazione catastrofale; 03-P5 Contratto agro-climatico; 04-P3 Prima il treno di chi viaggia ogni giorno: fondo TPL e abbonamento unico; 04-P7 Dal porto al treno: più merci sul ferro; 05-C4 Più persone con laurea o diploma terziario: ITS, lauree professionalizzanti, residenze; 07-C1 Giustizia a regime: Ufficio per il processo e triage digitale; 07-C3 Governance dei flussi migratori fondata sui dati; 08-P1 Legge sulla consulenza algoritmica pubblica; 08-P6 Export resiliente; 09-C1 Stato a vetro: infrastruttura aperta per l'analisi delle politiche; 09-C11 Dividendo dell'automazione: meno posti nelle attività ripetitive, meno tasse, regole contro l'elusione.
- **Cambiano variante (31):** 01-P1 piena → zero; 01-P2 piena → zero; 01-P3 piena → essenziale; 01-P6 piena → zero; 01-P7 piena → essenziale; 01-P12 piena → essenziale; 01-P15 piena → zero; 01-P23 piena → pilota; 02-C5 essenziale → pilota; 02-C7 piena → essenziale; 03-P2 piena → essenziale; 04-P4 piena → essenziale; 05-C2 essenziale → pilota; 05-C5 piena → essenziale; 05-C6 essenziale → zero; 05-C8 piena → essenziale; 05-C9 piena → pilota; 06-C3 essenziale → pilota; 06-C8 piena → pilota; 06-C9 piena → pilota; 06-C10 piena → pilota; 07-C2 piena → essenziale; 07-C4 piena → essenziale; 07-C7 piena → essenziale; 08-P2 piena → essenziale; 08-P3 essenziale → zero; 08-P9 piena → zero; 09-C6 piena → zero; 09-C8 piena → essenziale; 09-C9 piena → essenziale; 09-C10 piena → essenziale.
<!-- /auto:difesa -->

**2. Dividendo climatico.** L'ottimizzatore usa il gettito dei sussidi dannosi per i servizi e non per il dividendo. Imporre il dividendo compensativo per redditi bassi e settori esposti (1,2 mld) cambia il programma completo così:

<!-- auto:dividendo -->
- **Escono (3):** 04-P7 Dal porto al treno: più merci sul ferro; 06-C9 Equipe di benessere scolastico in rete con la Casa della Comunità; 08-P6 Export resiliente.
- **Cambiano variante (7):** 01-P6 piena → essenziale; 01-P7 piena → essenziale; 03-P1 zero → essenziale; 05-C5 piena → essenziale; 05-C6 essenziale → zero; 05-C8 piena → essenziale; 07-C2 piena → essenziale.
<!-- /auto:dividendo -->

**3. Coperture strutturali** (programma completo, circa 5,9 mld in più del base). Le pagano soprattutto chi possiede case di valore alto, chi affitta a canone libero, chi eredita patrimoni oltre 500.000 € per erede, le famiglie capienti con spese di istruzione privata, l'autotrasporto e l'agricoltura (fino al 2035), chi consuma gas (con un bonus per i redditi bassi). È la scelta più politica del programma: il sistema la presenta, non la impone.

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

Il prezzo, dichiarato: nessuna misura del nucleo robusto esce (tutte e 22 di allora restano nel programma, 21 con spesa: 02-C5 era allora solo regole, dal 13 novembre è pilota), ma molte scendono di un gradino:
- **scuola**: 05-C4 più persone con laurea o diploma ITS e 05-C5 scuole aperte, da piena a essenziale;
- **innovazione**: 05-C10 rete per la ricerca applicata, 04-P7 dal porto al treno e 01-P14 Sfide Italia diventano pilota; 01-P15 spin-off resta solo come regole; 04-P8 camion a zero emissioni scende a essenziale; resta piena 04-P9 consegne pulite; 01-P13 credito per la ricerca, piena fino al 13 novembre, scende a essenziale per far posto al personale infermieristico (punto 10);
- **fisco e istituzioni**: 01-P12 da piena a essenziale; ritocchi minimi a 01-P2, 08-P2, 08-P7.

Tre limiti, dichiarati: il margine sulle risorse generali è nullo (coprono la spesa esatta; il margine mostrato nei totali è di fondi vincolati non spostabili); circa 1,9 mld di spesa (dal 13 novembre, con il pilota di 02-C5) sono pagati con i fondi europei di coesione 2021-2027, che finiscono nel 2029: 0,5 mld servono anche dopo e hanno una regola di salvaguardia (punti 9 e 10); il personale infermieristico nuovo (06-C2) è entrato il 13 novembre solo come pilota (punto 10): senza la versione essenziale le Case della Comunità rendono meno; il ricambio selettivo di RP08 cresce negli anni e potrà finanziarne una parte. Ricerca di confronto in `benchmark/nord_europa_efficienza_spesa.md`.

**7. Bandi pubblici con istruttoria assistita (09-C10).** Il 12 novembre 2026 chi guida il progetto ha proposto di portare a livello nazionale un'esperienza diretta in un ufficio regionale, descritta in forma anonima: uno strumento costruito in tre giorni con l'AI, che fa i controlli ripetitivi di un bando e lascia la decisione al funzionario. I tre valutatori la giudicano positiva su quasi tutti i valori, soprattutto fiducia e innovazione, e il motore la mette nel **nucleo robusto** (prima metà della classifica nell'89% delle combinazioni di pesi). Il problema che affronta è misurato: al 31 agosto 2026 l'Italia aveva pagato il 14,78% dei fondi strutturali europei 2021-2027 (RGS); per la Commissione europea la spesa dichiarata è al 19,1%, contro il 24,5% della media UE. Nel programma intermedio entra come **pilota** (10 bandi in 3 Regioni, 0,01 mld su fondi europei di assistenza tecnica): non toglie risorse ad altre misure e parte misurando il tempo risparmiato, che oggi non è ancora noto. **Eccezione dichiarata alla regola del nucleo** (13 novembre 2026): la versione essenziale costerebbe 0,02 mld l'anno di risorse generali, oggi senza margine, e toglierli a un'altra misura senza sapere quanto tempo si risparmia sarebbe una scommessa. Quindi 09-C10 resta pilota e passa a essenziale nella prima legge di bilancio dopo la valutazione del pilota, affidata a soggetti diversi da chi ha costruito lo strumento, se i tempi di istruttoria scendono di almeno un terzo senza più ricorsi o errori. Verifica giuridica condizionata: articolato corretto su responsabile del procedimento, preavviso di rigetto, dati e AI Act (`giuridico/conformita_BANDI.csv`). Dal 13 novembre 2026 la misura comprende anche tre regole a costo zero per gli incentivi alle imprese gestiti da Invitalia e dagli altri gestori: compenso legato al rispetto dei tempi, un cruscotto pubblico trimestrale dei tempi e niente nuove risorse con atti amministrativi, sopra i 100 milioni, senza una valutazione d'impatto pubblicata (`benchmark/invitalia_incentivi_imprese.md`); l'articolo è scritto come modifica del Codice degli incentivi e il controllo giuridico preventivo ha dato esito condizionato: le condizioni sono state recepite nel testo.

**8. Progetto di vita per le persone con disabilità (02-C5).** È nel nucleo robusto, ma fino al 12 novembre era nel programma solo nella versione a costo zero: la riforma del collocamento mirato, senza personale né risorse per il progetto di vita. Il 13 novembre 2026 abbiamo calcolato la versione essenziale: costa 0,8 mld l'anno di risorse generali, e senza tasse in più non entra, perché il nucleo da solo, in versione essenziale, costerebbe più di quanto rendono le coperture ammesse. Le alternative erano due: abbassare un'altra misura del nucleo (prevenzione e assicurazione contro le catastrofi, 03-P4) e rinunciare a parte delle misure di innovazione, oppure aggiungere tasse su detrazioni o affitti. Chi guida il progetto ha scelto una **terza strada, dichiarata come eccezione**: un pilota da 0,15 mld l'anno sul Fondo sociale europeo fino al 2029, con personale dedicato e budget di progetto nel quarto degli ambiti territoriali con meno servizi, e la riforma del collocamento mirato ovunque. Nel 2029 una valutazione controfattuale decide il passaggio a essenziale nella legge di bilancio 2030. Il prezzo: per tre anni, in tre ambiti su quattro, il progetto di vita resta un diritto senza personale e risorse aggiuntive. Il personale del pilota è assunto a tempo determinato fino al 2029, perché il programma non usa fondi europei per personale stabile; a queste condizioni il Fondo sociale europeo può pagarlo (`programma/schede/02_lavoro.md`, `benchmark/fondi_coesione_bandi.md`).

**9. Che cosa succede ai fondi europei dopo il 2029.** Nel programma intermedio 1,9 mld l'anno di spesa sono pagati con i fondi europei di coesione 2021-2027, ammessi fino al 2029 (2030 per alcuni programmi). Il 13 novembre 2026 abbiamo deciso di non lasciare il problema a dopo: per ogni misura il file `programma/coesione_dopo_2029.csv` dice se la spesa finisce o ha bisogno di un successore.
- **Finiscono (0,96 mld):** investimenti fatti una volta, come reti idriche, aree interne, garanzie per l'energia, residenze universitarie e micro-hub per le merci. Le regole che li accompagnano restano.
- **Sperimentazioni (0,44 mld):** finiscono nel 2029 e proseguono solo con una valutazione positiva e risorse nuove; tra queste i piloti di 02-C5 e 09-C10.
- **Servono anche dopo (0,50 mld):** il fondo per la prevenzione dei rischi (03-P4), il conto personale di competenze (05-C2), il ponte contro la dispersione (05-C1) e la staffetta delle competenze nella PA (09-C8). Il successore indicato è il ciclo europeo 2028-2034, i cui importi per l'Italia non sono ancora noti; per ciascuna c'è anche una seconda strada nazionale. Oggi la loro copertura dopo il 2029 **non è garantita**, e lo scriviamo.

Senza nuove decisioni, dal 2030 la spesa del programma intermedio scende quindi a circa 8,0 mld l'anno, di cui 0,5 da rifinanziare. Due avvertenze dalle ricerche del 13 novembre (`benchmark/fondi_coesione_bandi.md`): il 70% delle risorse europee non ancora impegnate è nei programmi delle Regioni, quindi serve un accordo con loro; e alcune misure usano la coesione anche negli anni di avvio (02-C2, 06-C10, 07-C4), fuori dalla spesa a regime.

**10. Le scelte eque del 13 novembre 2026.** Quattro scelte politiche erano aperte. Le hanno studiate tre valutatori AI indipendenti, ciascuno con un'attenzione diversa (chi ha meno mezzi, le generazioni future, la fattibilità e la fiducia), senza vedere il lavoro degli altri (`revisioni/2026-11-13_scelte_eque_X.md`, `_Y.md`, `_Z.md`). Chi guida il progetto ha adottato la sintesi:

- **Un prelievo senza scopo ora ha uno scopo.** La rivalutazione ridotta delle pensioni più alte (PE04, solo sulla quota oltre circa 3.700 euro lordi al mese, dal 2030) era nel programma ma andava in un fondo che non pagava nulla. Ora va alle risorse generali: 0,30 mld a regime, circa 0,1 il primo anno.
- **Entra il personale infermieristico, come pilota (06-C2, 0,35 mld)** — *poi uscito la sera stessa, vedi sotto "La verifica delle coperture".* In 4 Regioni, almeno 2 del Mezzogiorno, e nelle aree interne: indennità di area disagiata, 5.000 borse di studio con vincolo di servizio nel SSN, infermiere di pratica avanzata in 50 Case della Comunità, valutazione Agenas a 30 mesi. Il prezzo: il credito unico per la ricerca (01-P13) scende da pieno a essenziale. Tutti e tre i valutatori sono arrivati a questa scelta.
- **Un margine vero, con una destinazione.** Le risorse generali ora hanno 0,06 mld non spesi: 0,04 per servizi gratuiti per smettere di fumare per chi ha un ISEE basso, 0,02 di riserva per le misure pagate con fondi europei dopo il 2029. Erano 0,09, con una riserva di 0,05: la sera del 13 novembre una verifica sul rendiconto dello Stato ha mostrato che la copertura sulle consulenze (RA03) rendeva circa 0,02 mld, non 0,05.
- **Le accise su tabacco e bevande restano, ma tornano a chi le paga.** Un importo pari al gettito del tabacco va per legge alla sanità vicino a casa (Case della Comunità, squadre di quartiere, personale infermieristico), con priorità ai distretti più poveri. Nessuna compensazione in denaro, che richiederebbe di schedare chi fuma. Le compensazioni già previste sul gasolio vanno prima alle piccole imprese, alla montagna, alle aree interne e alle isole.
- **Dopo il 2029, la regola si decide ora.** Entro il 30 settembre 2029 la Ragioneria certifica i fondi europei del ciclo 2028-2034 misura per misura. Se mancano, si usa in quest'ordine: la riserva di 0,02; il gettito delle coperture oltre il minimo, solo se certificato; poi le misure scendono di versione, nell'ordine 03-P4, 05-C2, 05-C1.
- **Garanzie e responsabilità.** Una persona responsabile con nome firma ogni scelta politica e il suo prezzo; un comitato di garanzia di 7 persone, scelte per sorteggio tra persone idonee, controlla le regole e non il programma (`24_garanzie_e_responsabilita.md`).

Con queste scelte il programma intermedio era salito a 9,38 mld l'anno e 67 misure. Due avvertenze, che restano valide. Il controllo giuridico preventivo ritiene compatibile, a condizioni, l'uso dei risparmi sulle pensioni per la sanità (Corte cost. 19/2025 ha già ammesso usi fuori dal sistema pensionistico): durata 2030-2034 con verifica INPS-MEF al Parlamento, motivazione esplicita, mai cumulata con altri raffreddamenti, rivalutazione al 75% negli anni con inflazione oltre il 4% (`giuridico/conformita_COS.csv`). L'ottimizzatore ragiona sull'anno in cui le coperture rendono a pieno: PE04 rende 0,1 nel 2030 e 0,3 solo dal 2035, quindi negli anni di passaggio i conti vanno verificati anno per anno.

**11. La verifica delle coperture, la sera del 13 novembre 2026.** Abbiamo ricontrollato sul rendiconto 2025 dello Stato, capitolo per capitolo, le coperture che tagliano o spostano spesa dei ministeri (`benchmark/verifica_coperture_rendiconto.md`). Dieci erano sovrastimate, perché la loro base era stata costruita cercando parole nei titoli dei capitoli o prendendo categorie intere: per esempio i tagli alle consulenze (RA03) contavano anche i compensi ai centri di assistenza fiscale, e quelli agli incentivi alle imprese (RA04) i crediti fiscali alle banche e il rimborso delle accise all'autotrasporto, già contato altrove. Le coperture attive scendono di circa 0,75 mld al minimo. Senza tasse in più il programma non stava più in piedi: chi guida il progetto ha scelto di tenere **il nucleo robusto, le squadre infermieristiche di quartiere (06-C8) e la compensazione dell'autotrasporto (04-P8)**. Il prezzo, dichiarato:

- **escono** il pilota del personale infermieristico (06-C2), il credito per la ricerca (01-P13), il pilota del reddito di inclusione (02-C4) e le merci sul treno (04-P7);
- **scendono** le consegne pulite (04-P9, solo regole), la squadra per la produttività pubblica con l'AI (09-C9) e la riqualificazione degli amministrativi della sanità (06-C10), che diventano piloti;
- la riserva per il dopo 2029 scende da 0,05 a 0,02 mld; restano i 0,04 per smettere di fumare.

Con queste scelte il programma intermedio era sceso a 8,64 mld l'anno e 63 misure.

**12. Le ultime otto coperture, il 14 novembre 2026.** Le otto coperture che il rendiconto dello Stato non permetteva di controllare sono state verificate su altre fonti pubbliche primarie: Corte dei conti, Ministero della Salute, Agenzia del Demanio, ISTAT, Ministero della giustizia, INAPP (`benchmark/verifica_coperture_restanti.md`). Una è confermata (RP08, il ricambio degli amministrativi della sanità); sette erano sovrastimate:

- gli affitti della pubblica amministrazione (RA02, da 0,08 a 0,02 al minimo): il Piano del Demanio ha già in programma quasi tutto il risparmio;
- i beni e servizi non sanitari del servizio sanitario (RA06, da 0,2 a 0,1): le gare centralizzate sono già obbligatorie;
- le assunzioni riservate ai profili tecnici (RA07, da 0,15 a 0,10) e il Fondo Nuove Competenze (RA12, da 0,15 a 0,05): il Fondo è denaro europeo già contato altrove;
- il contributo unificato per chi fa molte cause (RA10, da 0,05 a 0,015), l'accorpamento degli enti minori (RP04) e le società partecipate (RP07): basi più piccole del previsto.

Al minimo mancano altri 0,37 mld. Nessuna riduzione di una sola misura bastava; chi guida il progetto ha scelto di far passare a **pilota l'Ufficio per il processo (07-C1)**, 1.500 addetti stabili in 20 tribunali critici invece di 4.500, **e il governo dei flussi migratori sui dati (07-C3)**, asilo entro 6 mesi in 3 Commissioni territoriali più l'osservatorio sul fabbisogno. Sono due eccezioni dichiarate al nucleo: tornano alla versione essenziale se i piloti funzionano e se una copertura viene certificata più alta. Restano le squadre di quartiere (06-C8) e la compensazione dell'autotrasporto (04-P8). Con lo spazio che resta, l'ottimizzatore porta alla versione piena la prova dei numeri per le grandi opere (04-P4) e il lavoro pubblico misurato (09-C6), ma con il calendario di avvio le versioni piene partono più tardi (oggi nel 2031, vedi il punto 14): fino ad allora vale la versione minima, a costo zero, come nel pacchetto "pronto domani".

Il programma intermedio è ora di **8,26 mld l'anno e 63 misure**, con coperture per 6,30 mld al minimo. Il personale infermieristico (06-C2) resta il primo della lista se una copertura viene certificata più alta, poi la versione essenziale di 07-C1. Alcune quote delle nuove stime (per esempio i litiganti seriali e la quota di profili generici) non sono pubblicate da nessuna fonte: sono stime degli agenti e andranno confermate con le amministrazioni.

**13. Quattro idee dai conti pubblici del Nord Europa e della Spagna, il 15 novembre 2026.** Un confronto con Svezia, Danimarca, Finlandia, Paesi Bassi e Spagna (`benchmark/conti_pubblici_nord_europa_spagna.md`) ha mostrato che il problema italiano non è la spesa di oggi (l'avanzo primario è tra i migliori del gruppo) ma gli interessi sul debito e la crescita bassa. Chi guida il progetto ha scelto di valutare quattro idee, scritte come cinque proposte (`programma/schede/01_economia.md`, `02_lavoro.md`) e valutate dai tre valutatori indipendenti con la rubrica di sempre (`benchmark/panel_conti_*.csv`):

- **tetti di spesa triennali per ministero (01-P16)** e **un Ufficio parlamentare di bilancio più forte (01-P17)**, con revisioni della spesa indipendenti e, come pilota, l'analisi volontaria dei programmi elettorali: costano pochi milioni;
- **un registro mensile dei redditi tra Agenzia delle entrate e INPS (01-P18)**, che rafforza la dichiarazione precompilata (01-P7), qui come pilota: i valutatori segnalano il rischio per la protezione dei dati;
- **aggancio protetto e correttore automatico e temporaneo sulle pensioni (02-C8)**, solo sulla parte oltre 6 volte il minimo, mai sotto il 50% dell'adeguamento, per al massimo 3 anni: costo zero, risparmio piccolo e non usato come copertura. Nessun valutatore vede una linea rossa, ma tutti ricordano che la Corte costituzionale guarda con più rigore i tagli ripetuti. Mentre vale la perequazione differenziata (PE04, 2030-2034) il correttore non si somma: scatta solo dopo;
- **un nucleo minimo di politiche attive del lavoro dopo il PNRR (02-C9)**, qui come pilota pagato dal Fondo sociale europeo fino al 2029 e poi dalla nuova copertura **RA15**, che riduce gli incentivi alle assunzioni senza effetto dimostrato (0,15-0,35 mld dal 2030).

Nessuna proposta esistente cambia classe. Le scelte del 14 novembre restano tutte; con il gettito di RA15 l'ottimizzatore aggiunge i controlli fiscali mirati con garanzie (01-P10, essenziale) e porta a pieno lo «Stato a vetro», l'infrastruttura aperta per analizzare le politiche (09-C1). Le versioni piene delle grandi opere (04-P4) e del lavoro pubblico misurato (09-C6) partivano allora nel 2034 (dal punto 14, nel 2031).

Il programma intermedio è ora di **8,43 mld l'anno e 70 misure**, con coperture per 6,45 mld al minimo.

**14. La ricerca dei risparmi, il 15 novembre 2026.** Per non chiedere tasse nuove, abbiamo cercato altri risparmi in quattro ambiti, ciascuno con un agente diverso: le agevolazioni fiscali non ancora toccate (`benchmark/risparmi_spese_fiscali.md`), i sussidi dannosi per l'ambiente e gli incentivi alle imprese (`benchmark/risparmi_sad_incentivi.md`), la macchina pubblica (`benchmark/risparmi_macchina_pubblica.md`) e la spesa per funzione, confrontata con i dati Eurostat degli altri Paesi europei (`benchmark/risparmi_spesa_funzioni.md`). Il confronto dice una cosa scomoda: tolti interessi e pensioni, l'Italia spende meno della media UE, non di più. Sono arrivate **20 coperture nuove, per 1,28-2,68 mld l'anno a regime**: sette agevolazioni fiscali (SF20-SF26), tre sussidi dannosi (SAD20-SAD22), tre regole sugli incentivi alle imprese (RA20-RA22), quattro risparmi nella macchina pubblica (RA30-RA33) e tre tagli di spesa per funzione (RA50-RA52). I tre valutatori indipendenti le hanno giudicate con la rubrica di sempre (`benchmark/panel_risparmi_*.csv`). La verifica giuridica (`giuridico/conformita_risparmi.csv`, `giuridico/note_risparmi.md`) non trova **nessuna linea rossa e nessuna copertura incompatibile**: 5 sono compatibili e 15 compatibili con condizioni. La più esposta è il nuovo contributo di Regioni e Comuni per il 2030-2033 (RA30): **rischio alto davanti alla Corte costituzionale**, perché i contributi arriverebbero a dieci anni di seguito; regge solo se è davvero nuovo, temporaneo e non toglie risorse a sanità e diritti sociali.

Chi guida il progetto ha scelto:

- **tutte e 20 entrano nel menu**, che ora ha 93 coperture;
- la compensazione dei costi ETS alle imprese energivore (SAD22) si usa **solo insieme ai treni per chi viaggia ogni giorno (04-P3)**, perché la legge europea vincola i proventi delle aste di CO2 al clima;
- nell'intermedio resta esclusa l'IMU sulle case nuove invendute delle imprese (SAD20), per coerenza con «nessun aumento di tasse sulla casa». Nell'intermedio non sono attivi neppure RA30 e SAD22; negli scenari completi l'ottimizzatore usa anche RA30.

Nel programma intermedio le **misure e le versioni non cambiano** (8,43 mld l'anno, 70 misure). Entrano 17 coperture nuove (SF20-SF26, SAD21, RA20-RA22, RA31-RA33, RA50-RA52) ed escono le due che toccavano le famiglie con figli: **il bonus nascita da 1.000 euro e il bonus per le lavoratrici madri restano come oggi** (RB02 e RB03 non servono più). Le coperture attive sono 70, per **6,95 mld al minimo** (prima 6,45). Il guadagno vero è nel calendario di avvio: il nucleo robusto e il primo gruppo partono al 3% nel 2027, al 73% nel 2028, al 94% nel 2029 e al 95% nel 2030, e sono **a pieno dal 2031** invece che dal 2034; le quattro misure dell'ultimo gruppo (01-P10, 04-P4, 09-C1, 09-C6) partono nel 2031 e sono a pieno nel 2032. Negli anni di passaggio slittano 4,55 mld di spesa, di cui 3,64 del nucleo (prima 6,81 e 5,31), e gli anni scoperti sulle risorse generali, con l'ipotesi prudente, sono il 2027-2031 invece che fino al 2034. Nel 2035 resta un margine di circa 0,57 mld (`programma/annuale_intermedio.md`).

I limiti, detti in chiaro. Le voci grandi erano già usate: i sussidi dannosi e gli incentivi alle imprese che restano sono piccoli, e il grosso delle agevolazioni fiscali non toccate è fatto di linee rosse (cuneo fiscale, Assegno unico, abitazione principale). Molte stime sono di livello 2, cioè con basi non pubblicate, e vanno confermate con le amministrazioni. Una copertura nuova pesa un po' su chi ha meno: il compenso ai CAF dimezzato per i 730 precompilati non modificati (RA52) può essere chiesto in parte alle persone, soprattutto anziane o con poche competenze digitali; resta gratuito il canale assistito dell'Agenzia delle entrate. Soprattutto, **i risparmi non bastano per le versioni piene**: valgono una piccola parte dei circa 5,3 mld che mancano per portarle tutte nel programma.

**15. Equità fiscale e integrità pubblica, il 16 novembre 2026.** Chi guida il progetto ha posto due domande: come fanno i redditi più alti a pagare meno in modo legale, e come prevenire la corruzione senza bloccare chi firma gli atti. Due agenti diversi hanno cercato dati e norme su fonti ufficiali e guardato agli altri Paesi (`benchmark/equita_fiscale_diagnosi.md`, `benchmark/anticorruzione_diagnosi.md`). La diagnosi fiscale distingue due problemi. L'evasione si concentra dove nessuno trattiene l'imposta: lavoro autonomo, piccola impresa, IVA. La pianificazione legale si concentra in alto: un dividendo incassato da una persona paga il 26%, lo stesso dividendo incassato dalla sua holding l'1,2%, e il 26% si può rinviare per decenni.

Entrano nove proposte:

- **equità fiscale** (`programma/schede/11_evasione.md`): sugli utili lasciati nelle **holding personali passive** la stessa imposta che si pagherebbe possedendo direttamente (01-P19); fine delle **polizze vita senza rischio e dei trust esteri** usati solo come contenitori (01-P21); nelle **eredità** l'impresa che lavora resta esente, la parte di patrimonio passivo no (01-P22); una **statistica ufficiale su chi paga quanto** e un'unità dell'Agenzia delle entrate per i grandi patrimoni (01-P23). Restano fuori, in modo esplicito, le imprese operative e i loro dividendi, chi reinveste e il passaggio ai figli di un'impresa che continua a lavorare;
- **integrità pubblica** (`programma/schede/13_integrita.md`): **registro obbligatorio delle lobby** per tutti, parti sociali comprese (08-P8); **dichiarazioni patrimoniali verificate** e regole sui conflitti d'interessi (08-P9); **titolare effettivo verificato** per gare e fondi pubblici (08-P10); **controlli a sorteggio** sugli enti che spendono fondi pubblici (08-P11); recepimento della **direttiva (UE) 2026/1021** (07-C7) con un reato stretto, solo con dolo intenzionale, e tutele contro la "paura della firma": la semplice illegittimità e le scelte discrezionali non sono reato, e chi segue un parere scritto chiesto prima è protetto.

**Che cosa resta escluso, e perché.** La maggiorazione di 4 punti sui redditi finanziari molto alti (01-P20) è uscita per scelta di chi guida il progetto: avrebbe chiesto di mandare al fisco i dati di tutti i risparmiatori, il gettito era piccolo e si poteva aggirare comprando titoli di Stato. Resta esclusa anche un'imposta patrimoniale generale: è una scelta politica, non tecnica (diagnosi, par. 6).

**Gettito.** Quattro coperture nuove, legate alle proposte (valgono solo se la proposta è nel programma): FN05 e FN06 sulle holding (0,03-0,11 e 0,03-0,10 mld), FN09 su polizze e trust (0,02-0,10) e FN10 sulle eredità (0,02-0,08). In tutto **0,10-0,39 mld l'anno a regime**, dal 2031-2032; il menu sale a 97 coperture. Sono entrate decise per legge, non recupero di evasione: quello che si recupera grazie a 01-P23 va a ridurre il deficit. 01-P22 non tocca aliquote e franchigie dell'imposta di successione: toglie l'esenzione solo alla parte passiva delle holding ereditate.

**Valutazione e verifica.** I tre valutatori indipendenti hanno giudicato proposte e coperture con la rubrica di sempre (`benchmark/panel_equita_*.csv`). La verifica giuridica (`giuridico/conformita_equita.csv`, `giuridico/note_equita.md`) non trova **nessuna linea rossa e nessun elemento incompatibile**: su 46 righe, 38 sono compatibili con condizioni, 7 compatibili e 1 richiede una notifica (va consultata la BCE, perché 01-P23 dà un compito nuovo alla Banca d'Italia). Le condizioni sono già nelle schede: nessuna retroattività (solo proventi incassati dopo la legge e solo successioni future), rispetto della direttiva madre-figlia, criteri sugli attivi passivi scritti nella legge e non in un decreto, per le polizze già in corso solo i premi nuovi.

**Le scelte di chi guida il progetto.** Tutte e nove entrano nel programma intermedio **in versione piena**; per 07-C7 è scelta la versione "reato stretto più tutele", non il recepimento minimo.

Il programma intermedio è ora di **8,50 mld l'anno e 79 misure** (prima 8,43 e 70): le nove proposte costano in tutto circa 0,07 mld l'anno. Le coperture attive sono 74, per **7,05 mld al minimo** (prima 6,95). Le misure nuove costano al massimo 20 milioni l'anno ciascuna e partono subito, mentre le loro coperture rendono tardi (sono a pieno nel 2031-2032): negli anni di passaggio tolgono un po' di spazio al nucleo. Il nucleo robusto parte al 2% nel 2027, al 71% nel 2028, al 92% nel 2029 e al 95% nel 2030, ed è sempre **a pieno dal 2031**; slittano 4,70 mld di spesa, di cui 3,88 del nucleo (prima 4,55 e 3,64). Le tre misure dell'ultimo gruppo (01-P10, 09-C1, 09-C6) partono nel 2031 (`programma/annuale_intermedio.md`).

**Il nucleo robusto sale da 23 a 30 proposte, ma nessun punteggio è cambiato.** La classe di una proposta dipende dalla sua posizione rispetto a tutte le altre. Le nove proposte nuove, utili ma piccole, si collocano soprattutto in fondo (sette sono "in coda", 01-P23 e 08-P11 "dipendenti dai valori"). Così sette proposte già esistenti salgono al nucleo: lo scudo cyber per i Comuni (07-C6), la casa a canone giusto (04-P2), i treni per chi viaggia ogni giorno (04-P3), la prova dei numeri per le grandi opere (04-P4), gli appalti a vetro (08-P7), «chiedilo una volta sola» (09-C2) e la squadra per la produttività pubblica con l'AI (09-C9). L'Ufficio parlamentare di bilancio più forte (01-P17) e il patto per le opere dopo il PNRR (04-P1) passano da "in coda" a "dipendenti dai valori" (`motore/esito.md`). È un effetto della classifica relativa, non un giudizio nuovo, e va letto con cautela. Nel programma intermedio queste sette non cambiano versione: 04-P4 e 08-P7 erano già piene, 09-C9 resta pilota e 09-C2 solo regole; la casa (04-P2) e i treni (04-P3) restano fuori per le scelte precedenti, come lo scudo cyber (07-C6).

I limiti, detti in chiaro. **La base imponibile delle holding non è pubblicata**: quante sono le holding passive e quanti utili trattengono va chiesto al Dipartimento delle finanze, e lo stesso vale per le polizze senza rischio (IVASS) e per le esenzioni sulle eredità. Per questo il gettito è una stima GovernAI **volutamente prudente**: conta solo la parte che resta nel tempo, non l'anticipo di imposte che si sarebbero pagate comunque. Resta da verificare con il Dipartimento per le politiche europee un caso residuo di trattamento diverso tra dividendi italiani ed europei in 01-P19. Il registro delle lobby e le dichiarazioni patrimoniali trattano dati personali: le schede prevedono le garanzie, ma va sentito il Garante.

**16. Chi paga davvero, e le scelte della sera del 16 novembre 2026.** Dopo il punto 15, chi guida il progetto ha chiesto di misurare quanto paga davvero lo stesso reddito a seconda di come si guadagna. Ne sono nate un'analisi pubblica (`analisi/chi_paga/calcolatore.md`, `analisi/chi_paga/popolazione.md`, pagina "Chi paga davvero" del sito), due proposte nuove e una parte nuova di 01-P19.

- **Perché.** Con le regole del 2026, a 1 milione di euro di reddito prodotto il socio di una SNC paga il 47% di imposte, chi lavora da dipendente il 44%, chi lascia gli utili della propria società in una holding il 29%, chi vive di rendite finanziarie il 26%, chi affitta con la cedolare il 21%, chi ha titoli di Stato il 12,5%. Dipendenti e pensionati pagano l'85% dell'IRPEF. La differenza non nasce dall'evasione: nasce da regole legali diverse, che solo chi ha abbastanza patrimonio può scegliere.
- **Come.** Un calcolatore pubblico con le regole di legge, che chiunque può rifare cambiando le ipotesi; tre valutatori AI indipendenti hanno rifatto il panel su proposte e coperture (`benchmark/panel_neutralita_*.csv`, `benchmark/panel_finale_*.csv`); la verifica giuridica non trova linee rosse né elementi incompatibili, solo condizioni (`giuridico/conformita_neutralita.csv`, `giuridico/conformita_patrimoniale.csv`). Le proposte complete sono in `benchmark/finale_proposta_neutralita.md` e `benchmark/finale_proposta_patrimoniale.md`.
- **Che cosa.** Tre scelte. **01-P19 si allarga**: i dividendi della propria società lasciati fermi in una holding personale e non reinvestiti in attività vere entro 3 anni (5 nella riserva per acquisizioni e crisi) pagano come se fossero distribuiti, cioè il 26%, sui dividendi incassati dal 2029; franchigia di 500.000 euro l'anno per famiglia nella versione essenziale e di 100.000 nella piena. Due coperture nuove: FN13 (0,03-0,23 mld) e FN14 (0,02-0,10), con primo gettito nel 2033. **01-P24, patrimoniale solo minima**: 1% sulla parte del patrimonio oltre 50 milioni e 2% oltre 1 miliardo, per persona, meno le imposte sul reddito già pagate, con exit tax per chi trasferisce la residenza all'estero (FN12, 0,3-1,5 mld, stima prudente); in alternativa la versione zero, che misura soltanto. **01-P25, parità per le imprese di persone**: SNC, SAS e ditte individuali in contabilità ordinaria pagano il 24% sugli utili lasciati in azienda fino a 100.000 euro l'anno per socio, come una SRL; su ciò che si preleva resta l'IRPEF. Costa 0,63 mld l'anno a regime e 1,26 nel 2029, e nel motore si attiva solo insieme alla patrimoniale minima che la paga (legame obbligatorio in `programma/ottimizza.py`). Su 07-C7 restano le due tutele: parere scritto chiesto prima, nessuna sospensione automatica per la sola indagine.
- **Chi.** Paga di più chi parcheggia nella holding gli utili della propria società senza reinvestirli e, con la patrimoniale minima, chi ha più di 50 milioni e paga poche imposte sul reddito rispetto al patrimonio (circa 2.100 persone, stima GovernAI). Paga di meno chi ha un'impresa di persone e lascia gli utili in azienda. Nulla cambia per chi preleva tutto, per le SRL che distribuiscono, per chi reinveste e per chi ha un reddito sotto le franchigie. Decide il Parlamento con la legge di bilancio; attuano Agenzia delle entrate e Sogei; il Dipartimento delle finanze fa la microsimulazione prima e la valutazione dopo 3 anni.

**Dove stanno nel programma.** 01-P24 e 01-P25 restano **fuori dal programma intermedio**, per la scelta precedente di non aggiungere tasse; nel programma completo (scenario di riferimento) il motore sceglie 01-P24 minima e 01-P25 solo in versione zero (`programma/selezione_riferimento.md`). Le eredità (01-P22) restano nell'intermedio: per questo la frase dello scenario ora dice "nessun aumento di aliquote su casa, eredità, affitti e IVA", perché 01-P22 toglie un'esenzione al patrimonio passivo ma non tocca aliquote e franchigie. Il programma intermedio è ora di **8,51 mld l'anno e 79 misure**, con 76 coperture attive per **7,10 mld al minimo** (prima 8,50 e 7,05): entrano FN13 e FN14 con 01-P19. Il menu ha 94 proposte, 281 varianti e 100 coperture.

**Il nucleo robusto sale da 30 a 33, ancora senza punteggi cambiati.** Salgono l'elettricità rinnovabile a prezzo rinnovabile (03-P2), le biblioteche di comunità (05-C8) e il contratto agro-climatico (03-P5), per lo stesso effetto della classifica relativa descritto al punto 15: le proposte nuove si collocano in coda (`motore/esito.md`). Nel programma intermedio 03-P2 resta in versione zero, 05-C8 pilota e 03-P5 fuori, per scelte precedenti.

**I limiti, detti in chiaro.**

- **01-P25 non si paga da sola.** La patrimoniale minima contata al minimo (0,3 mld, la metà nel 2029) non basta: nel caso prudente mancano circa 1,5 mld nel 2029, 0,7 nel 2030 e 0,6 a regime; con valori centrali basta dal 2030. Anno per anno resta in parte scoperta, e la legge dovrà indicare per ogni anno le coperture della differenza.
- **La regola sulle holding rende poco e tardi.** FN13 e FN14 valgono 0,05-0,33 mld l'anno e il primo gettito arriva solo nel 2033, perché si aspettano 3 anni dal dividendo. La base non è pubblicata e va chiesta al Dipartimento delle finanze; se l'UE chiede di escludere i dividendi coperti dalla direttiva madre-figlia, il gettito scende molto.
- **La base della patrimoniale è piccola e mobile.** Poche migliaia di persone, patrimoni difficili da valutare, possibilità di cambiare residenza: per questo la stima resta prudente anche con l'exit tax.
- **La parità aiuta soprattutto chi ha utili sopra 50.000 euro.** Sotto i 28.000-35.000 euro il 24% non conviene: è un'opzione, quindi nessuno ci perde, ma chi guadagna poco non ci guadagna.

**La griglia oceano blu**, una riga per voce:

- **Elimina** la convenienza a parcheggiare gli utili in una holding solo per pagare meno.
- **Riduce** il divario di imposta tra chi vive di lavoro o di impresa di persone e chi vive di capitale, a parità di reddito.
- **Aumenta** la trasparenza: si misura ogni anno chi paga quanto (01-P23, 01-P24 zero) prima di decidere.
- **Crea** una regola uguale per tutte le forme d'impresa: chi lascia gli utili in azienda paga come una società, chi li preleva o li parcheggia paga come una persona.

## 7. Cosa manca e cosa fare dopo

- **Conti anno per anno: lo scarto degli anni di passaggio.** Dal 13 novembre 2026 `programma/annuale.py` rifà il conto per ogni anno dal 2027 al 2035 (`programma/annuale_intermedio.md`). Il vincolo "senza deficit" vale a regime, ma alcune coperture crescono piano: il taglio del gasolio agevolato per l'autotrasporto (SAD13, 0,8 mld) arriva al pieno in 8 anni, la rivalutazione ridotta delle pensioni più alte (PE04, 0,3 mld) in 6. Con l'ipotesi prudente le risorse generali sono scoperte dal 2027 al 2031, fino a 2,20 mld nel 2027 e 4,49 mld in tutto; con quella favorevole, coperture attive dal primo anno, resta scoperto solo il 2030, per 0,08 mld (dati del 16 novembre 2026; prima gli anni scoperti arrivavano al 2034). **Scelta del 13 novembre 2026: un calendario di avvio**, corretto dopo il secondo giro di revisione. Ogni anno la spesa sulle risorse generali non supera il gettito dell'anno, con l'ipotesi prudente, tenendo da parte i servizi per smettere di fumare (0,04 mld dal 2028) e la riserva per il dopo 2029 (0,02 mld dal 2030). I fondi europei 2021-2027 pagano solo spese una tantum, non spesa corrente. Partono subito, per intero, le 38 riforme a costo quasi zero (al massimo 20 milioni l'anno ciascuna), compresa la legge sulla consulenza algoritmica pubblica (08-P1). Il 2027 è un anno di preparazione: quasi tutte le coperture rendono dal 2028, quindi il nucleo robusto parte al 2% nel 2027, al 71% nel 2028, al 92% nel 2029 e al 95% nel 2030, ed è a pieno dal 2031 (dato aggiornato il 16 novembre 2026, dopo le 20 coperture nuove del punto 14 e le proposte e coperture del punto 15 di §6; prima del 15 novembre era a pieno dal 2034); le sperimentazioni, la compensazione dell'autotrasporto (04-P8) e le squadre di quartiere (06-C8) seguono lo stesso passo. Le sperimentazioni pagate con i fondi europei partono invece subito. Restano due attriti da decidere: il congedo paterno (un mese dal 2028, due dal 2030) dipende dalla quota di 02-C2 avviata, e le zone a emissioni zero per le merci (04-P9) arrivano nel 2030 mentre i contributi per cargo bike e ricarica sono usciti dal programma. Negli anni di passaggio slittano circa 4,7 mld di spesa, **in gran parte del nucleo** (3,9); tre misure (01-P10, 09-C1, 09-C6) partono solo nel 2031 e sono a pieno nel 2032, mentre la prova dei numeri per le grandi opere (04-P4), ora nel nucleo, segue il passo del nucleo; nel 2035 resta un margine di circa 0,60 mld: nessun anno chiude in deficit, ma il programma arriva a regime più tardi di quanto promettono le singole schede. Le stime vanno verificate con la Ragioneria.
- **Costi stimati, non certificati.** I costi delle varianti e molti gettiti sono "stime GovernAI". Il passo successivo è la verifica con la Ragioneria o con l'UPB, e microsimulazioni distributive su microdati, che richiedono un accesso istituzionale.
- **Doppioni da escludere.** Le spese fiscali del menu vanno confrontate voce per voce con la lista dei 7,37 mld già nel Piano strutturale.
- **Utilità delle varianti.** È calcolata come intensità × utilità della proposta piena. Il panel dovrebbe valutare direttamente le varianti essenziali e le misure di copertura.
- **Proposte escluse o ridotte, ma di valore.** La salute mentale resta fuori; il nuovo personale infermieristico, la non autosufficienza e reddito di inclusione sono solo sperimentazioni. Il motivo è la mancanza di risorse certificate, non il poco valore.
- **Revisione esterna.** Una prima analisi politica, scritta da un agente AI, è in `revisioni/2026-11-08_analista_politico.md`. Serve ora una revisione critica di persone con orientamenti politici diversi, e un confronto tra i punteggi degli agenti e quelli di un panel di persone.
