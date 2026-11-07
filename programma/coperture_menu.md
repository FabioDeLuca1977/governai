# Menu delle coperture di GovernAI

*Agente "coperture", 7 novembre 2026, secondo passaggio. Dati per l'ottimizzatore in `coperture_menu.csv`: 59 misure, con lo schema di `README.md` più la colonna finale `livello`. Importi in mld €/anno a regime, al netto della legislazione vigente e delle compensazioni per i più vulnerabili.*

I due livelli:
- **Livello 1** (48 misure): le 31 del primo passaggio più 17 proposte dagli agenti d'area, verificate e spesso ridotte.
- **Livello 2** (11 misure): coperture strutturali, più grandi e più controverse.

**Fonti principali.**
- MASE, [Catalogo SAD/SAF VIII ed.](https://www.camera.it/temiap/2026/07/16/OCD177-9133.pdf), valori 2025.
- MEF, [Rapporto spese fiscali 2025](https://www.mef.gov.it/export/sites/MEF/documenti-allegati/2025/RSF-2025-bis.pdf).
- DDL bilancio 2027 A.C. 3174 e OpenBDAP-RGS, Rendiconto 2025.
- Corte cost. 234/2020.
- Fonti secondarie, indicate riga per riga: OCPI, ENAC/Assaeroporti, Agenzia del Demanio, Consip, relazione tecnica della L. 190/2014.

Ogni gettito senza una stima ufficiale è una **stima GovernAI**, con il metodo nella colonna `note`.

## Sintesi per fondo e livello

| Fondo | Livello 1: misure | Livello 1: mld | Livello 2: misure | Livello 2: mld | Capienza in `registro/fondi.csv` |
|---|---|---|---|---|---|
| SAD | 11 | 1,38-2,54 | 3 | 1,45-2,32 | 2,0-8,0 |
| SPESE_FISCALI | 10 | 1,25-2,62 | 5 | 3,50-6,00 | 0-3,0 |
| ACCISE_SALUTE | 4 | 0,97-1,70 | 1 | 0,40-0,70 | 0,5-1,5 |
| PENSIONI | 4 | 0,41-0,71 | — | — | 0,3-1,0 |
| TASSA_SOGGIORNO | 2 | 0,11-0,29 | — | — | 0,1-0,4 |
| RIORDINO_BONUS | 5 | 1,16-1,50 | — | — | 0,3-1,5 |
| RIALLOCAZIONE | 12 | 1,49-3,16 | 2 | 1,00-2,20 | 0,5-2,0 |
| **Totale** | **48** | **6,8-12,5** | **11** | **6,4-11,2** | |

Totale dei due livelli: **13,1-23,7 mld**.

Tre cautele per leggere la tabella:
- **Coperture vincolate.** Alcune valgono solo per una proposta precisa: RB04 copre 05-C6, RA07 copre 09-C3, RA11 copre 05-C1 e 05-C4, RA12 copre 05-C2. Non sono risorse libere: circa 0,6-1,2 mld del livello 1.
- **PE01 e PE02 sono temporanei**: valgono 3 anni.
- **TS01 e TS02 sono entrate dei Comuni.**

## Livello 1

### Primo passaggio (31 misure)
Le misure sono invariate, salvo AS04, portato a +20% sui superalcolici per integrare AS-SAN2.

| Fondo | Misure |
|---|---|
| SAD | SAD01 rimborso gasolio autotrasporto (0,30-0,50); SAD02 gasolio agricolo (0,15-0,20); SAD03 cherosene voli nazionali (0,12-0,20); SAD04 navigazione nazionale (0,03-0,06); SAD05 auto aziendali (0,15-0,30); SAD06 IVA sulle case nuove su suolo libero (0,15-0,45); SAD07 IVA su fertilizzanti e fitosanitari (0,04-0,10); SAD08 quattro micro-SAD energetici (0,10-0,14); SAD09 impianti di risalita (0,02-0,035); SAD10 riscaldamento in montagna (0,02-0,05) |
| SPESE_FISCALI | SF01 cedolare 21%→23% (0,15-0,25); SF02 forfetario fascia 50-85 mila (0,20-0,45); SF03 tonnage tax (0,05-0,15); SF04 grandi cooperative (0,05-0,15); SF05 spese fiscali minori (0,08-0,20) |
| ACCISE_SALUTE | AS01 sigarette +0,50 €/pacchetto (0,60-1,00); AS02 tabacco riscaldato (0,15-0,35); AS03 sugar tax ×2 (0,15-0,25); AS04 superalcolici +20% (0,07-0,10) |
| PENSIONI | PE01 contributo triennale oltre 100 mila (0,08-0,15); PE02 fascia 80-100 mila (0,03-0,06); PE03 quote (0) |
| TASSA_SOGGIORNO | TS01 +2 €/notte nei comuni ad alta pressione (0,10-0,25); TS02 contributo di accesso (0,01-0,04) |
| RIORDINO_BONUS | RB01 Carta Valore con ISEE (0,05-0,08); RB02 bonus nuovi nati nell'AUU (0,08-0,15); RB03 bonus madri con soglia a 32 mila (0,10-0,20) |
| RIALLOCAZIONE | RA01 acquisti centralizzati (0,15-0,40); RA02 locazioni passive (0,08-0,15); RA03 consulenze e auto (0,05-0,08); RA04 incentivi alle imprese −3-5% (0,15-0,40) |

### Proposte degli agenti d'area (17 misure nuove)
| ID | Origine | Misura | Gettito | Verifica |
|---|---|---|---|---|
| SAD11 | 08 | Contributo di solidarietà sui biglietti aerei (2/4/10 €) | 0,30-0,50 | L'area stimava 0,4-0,8; ricalcolato su 230 mln di passeggeri (ENAC 2025) |
| SF06 | 06 SF-SAN1 | Detrazione sanitaria decrescente tra 50 e 120 mila €, salvi cronici e disabili | 0,35-0,60 | Base RSF 4.874 mln |
| SF07 | 06 SF-SAN2 | Fondi sanitari integrativi: deduzione decrescente oltre 75 mila | 0,08-0,20 | L'area stimava 0,2-0,4; la deduzione RSF vale 838 mln con media di 84 € |
| SF08 | 05 | Detrazione per lo sport dei ragazzi trasformata in offerta gratuita | 0,04-0,07 | Tetto: costo RSF di 74 mln (l'area stimava 0,10) |
| SF09 | 04 | Detrazioni edilizie ridotte per le seconde case | 0,05-0,15 | Gettito in 10 rate, cresce lentamente |
| SF10 | 01 | Iperammortamento: maggiorazione base ridotta | 0,20-0,40 | Costo totale della misura non trovato: non verificata |
| PE04 | 02 | Perequazione al 50% sopra 6 volte il minimo, dal 2030 | 0,30-0,50 (2035) | Calcolo GovernAI; cresce di circa 0,1 l'anno |
| RB04 | 05 | Quota della Carta del docente vincolata alla formazione | 0,08-0,12 | Vincolata a 05-C6 |
| RB05 | 02-C2 | Soppressione del bonus madri oltre RB03 | 0,85-0,95 | RT DDL: 1.070 mln, 993 mila beneficiarie |
| RA05 | 06 R-SAN1 | Abrogazione della riduzione del payback (DDL art. 71) | 0,16 | Verifica 06 |
| RA06 | 06 R-SAN2 | Tetto alla spesa non sanitaria del SSN, con riduzione del FSN | 0,20-0,40 | Richiede intesa Stato-Regioni |
| RA07 | 09 R09-1 | Riserva del turnover ai profili tecnici | 0,15-0,35 | Vincolata a 09-C3 |
| RA08 | 09 R09-2 | Assistenza tecnica esterna, oltre RA03 | 0,03-0,10 | — |
| RA09 | 09 R09-3 | ICT corrente statale −4/6% | 0,12-0,30 | Solo la quota statale (l'area stimava 0,28-0,42 su tutta la PA) |
| RA10 | 07 | Contributo unificato maggiorato per i litiganti seriali | 0,05-0,12 | È una DRM; base non verificata |
| RA11 | 05 | Organico scolastico ridotto via turnover (6.700 posti) | 0,20-0,30 | Reinvestito nella scuola |
| RA12 | 05 | Fondo Nuove Competenze e quota 0,30% nel Conto competenze | 0,15-0,40 | Da certificare |

**Fuse per evitare doppioni.** Ogni proposta d'area è già contata in una misura del menu:
- AS-SAN1 coincide con AS01 + AS02; l'estensione è AS05, a livello 2;
- AS-SAN2 è in AS04;
- il taglio delle consulenze proposto dall'area 08 è in RA03;
- la Carta Valore con ISEE (area 05) è RB01;
- il contributo triennale dell'area 02 corrisponde a PE01 + PE02.

**Non inserite** perché non quantificate o fuori dal menu:
- SF-SAN3 (badanti), RB-SAN1 e RB-SAN2 (budget di cura, bonus psicologo): mancano le cifre;
- FSN-INT: riguarda il fondo FSN, non il menu;
- aumento contributivo CUAF: l'avanzo non è certificato.

## Livello 2: coperture strutturali
| ID | Misura | Gettito netto | Compensazione sottratta | Effetti negativi dichiarati |
|---|---|---|---|---|
| **SF15** | IVA 10%→12%, esclusi alimentari di base, farmaci, energia domestica e TPL | **1,50-2,20** | AUU e ADI per il 30% più povero (0,5-0,7) | BEN −2, RIS −1, BPA −1 (turismo, ristorazione) |
| **SF13** | Catasto a valori di mercato e IMU sulla prima casa solo oltre una franchigia; gettito ai Comuni compensato da minori trasferimenti statali | **0,80-1,50** | detrazione piena per ISEE ≤25 mila, rinvio per anziani a basso reddito | BEN −1, RIS −1; 3-4 anni di attuazione |
| **SAD13** | Uscita completa dai SAD del gasolio per autotrasporto e agricoltura entro il 2035 | **0,80-1,10** | rinnovo flotte e redditi agricoli (0,4) | RIS −2, BEN −1, BPA −1 (aree rurali) |
| SF11 | Abolizione della cedolare secca a canone libero (oltre SF01) | 0,60-1,10 | concordato al 10% salvo | rischio affitti più alti e nero |
| RA13 | Revisione della spesa dei ministeri: ulteriori 0,05% del PIL | 0,60-1,20 | — | rischio di tagli lineari (BEN −1) |
| SF14 | Successioni: franchigia 500 mila, aliquote 4% e 7% | 0,40-0,80 | aziende familiari esenti | RIS −1; rischio di elusione |
| SAD14 | IVA al 22% sulle case nuove non prima casa | 0,40-0,90 | — | offerta di case nuove |
| RA14 | Riordino completo degli incentivi alle imprese | 0,40-1,00 | — | resistenze settoriali |
| AS05 | Tabacchi verso il livello UE più alto (+0,50 € oltre AS01) | 0,40-0,70 | — | RIS −2 (regressiva), contrabbando |
| SAD12 | IVA gas domestico 10%→22% sui primi 480 m³ | 0,25-0,32 | bonus sociale gas (0,08-0,12) | RIS −2, BEN −2 |
| SF12 | Agevolazioni prima casa solo fino a 400.000 € | 0,20-0,40 | — | lieve |

Per il livello 2 **non propongo**:
- l'IVA sull'energia elettrica domestica e l'esenzione dall'accisa elettrica per i consumi bassi: frenerebbero l'elettrificazione e sono progressive;
- tagli alla detrazione per lavoro dipendente;
- ricalcoli retroattivi delle pensioni, contrari alla giurisprudenza costituzionale.

## Miglior rapporto tra gettito e costo sociale
**Livello 1:**
- AS01, sigarette (0,6-1,0);
- SAD01, rimborso gasolio all'autotrasporto (0,3-0,5);
- SF06, detrazione sanitaria per i redditi alti (0,35-0,6);
- RA01, acquisti centralizzati (0,15-0,4).

**Livello 2:**
- SF13, catasto e IMU sulle prime case di pregio: progressiva, protegge le famiglie con ISEE basso;
- SF14, successioni: costo sociale basso e FUT positivo;
- SF15, IVA: il gettito più alto, ma pesa sui consumi anche dopo la compensazione.

## Misure più controverse
- **SF15, IVA.**
- **SF13, IMU sulla prima casa.**
- **RB05, soppressione del bonus madri**: BEN −2, sensata solo insieme ai nidi.
- **SAD12 e SAD13, energia e gasolio**: proteste attese.
- **SF11, cedolare secca.**
- **PE01, PE02 e PE04, pensioni**: rischio di contenzioso.
- **AS01 e AS05, tabacchi**: prelievo regressivo.

## Avvertenze
**Doppio conteggio.**
- Il differenziale tra gasolio e benzina (EN.SI.24) è chiuso dal 2026.
- Il target PNRR di 4,5 mld sui SAD include già la riforma 2025 delle auto aziendali.
- Le misure SF valgono solo se i **7,37 mld del Piano strutturale** sono raggiunti con altre voci. La lista PSB non è stata consultata: SF01-SF12 possono sovrapporsi, in particolare SF06 al tetto delle detrazioni della L. 207/2024.
- Restano fuori dal gettito: i tabacchi già in legge (+0,8 mld nel 2028), la sugar tax base, le quote (PE03 = 0).
- RB03 e RB05 presuppongono il DDL 2027 approvato così com'è.
- Ci sono sovrapposizioni parziali tra SAD03 e SAD11, SAD06 e SAD14, RA01 e RA09, RA03 e RA08: ogni misura è stimata al netto dell'altra, ma insieme vanno ricontrollate.

**Cosa è incerto.**
- I valori del Catalogo sono teorici, "a comportamento invariato".
- Diverse platee non sono verificate.
- Mancano dati ufficiali su: costo dell'iperammortamento, gettito del tabacco riscaldato, distribuzione per reddito di forfetari e detrazioni, quota dei pensionati sopra 6 volte il minimo.
- SF14 e SF15 sono DRM imputate a SPESE_FISCALI perché non esiste un fondo più adatto.
- SF13, RA06 e RA05 richiedono di ridurre i trasferimenti a Comuni o SSN per liberare risorse statali.

Ricerche web usate in tutto: 19.

## Aggiornamento valori (Carta 2.0)

*Agente "coperture", 7 novembre 2026. `coperture_menu.csv` ha ora le colonne EQU, SIC e CIT subito dopo FUT (orizzonte medio, effetto della sola misura di copertura). Le altre colonne e l'ordine delle righe sono invariati, salvo le revisioni di RIS, BEN e FID elencate sotto.*

**Criteri.**
- **EQU**: positivo se il prelievo è progressivo o colpisce rendite e privilegi; negativo se regressivo o se pesa su territori svantaggiati; compensazioni per i più vulnerabili attenuano il segno.
- **SIC**: 0 per tutte le misure, salvo RA09 (+1: dismissione dei CED residui e delle licenze obsolete riduce il rischio informatico della PA).
- **CIT**: +1 dove la misura rafforza reciprocità e lealtà fiscale (PE01, PE02, PE03: corrispondenza tra contributi e prestazioni; SF02: meno incentivo a restare sotto soglia; SF13: imposta locale legata ai servizi); −1 per RB04 (vincolo paternalistico sull'uso della Carta del docente). 0 altrove.

**Revisioni per non contare due volte (regola 1 della rubrica).**
- Effetto distributivo spostato da RIS a EQU (RIS a 0): SAD01, SAD02, SAD06, SAD08, SAD10, SF02, AS01, AS02, AS03, PE03, AS05 (−2), SAD13 (−2), SF11, SF14.
- Da RIS e BEN a EQU: SAD12 (RIS −2→0, BEN −2→−1), SF15 (RIS −1→0, BEN −2→−1), RB05 (RIS −2→−1, resta l'effetto di genere; BEN −2→−1).
- SF13: RIS −1→0 (distributivo, ora EQU +2); FID 1→2 (estimi trasparenti e uguali per tutti).
- RA14: RIS −1→0 (perdita delle imprese beneficiarie compensata dall'eliminazione di rendite, EQU 0); FID 1→2 (addizionalità dimostrata e pubblica).
- RB04: RIS −1→0, l'effetto sulla libertà di scelta è ora in CIT −1.
- Restano in RIS gli effetti non distributivi: affidamento dei pensionati (PE01, PE02, PE04), effetto di genere (RB03, RB05), libertà di circolazione (TS02).
- Dove la compensazione prevista neutralizza l'effetto, EQU vale 0 anche se RIS era −1: SAD06 (salvaguardia under 36), SAD08 (perdita dei gestori contro privilegio dei grandi consumatori).

**Le 5 misure più regressive (EQU).** A parità di punteggio, ordine per gettito massimo.

| Misura | EQU | Perché |
|---|---|---|
| RB05, soppressione del bonus madri residuo | −2 | colpisce madri lavoratrici con reddito fino a 32.000 €; accettabile solo con i nidi |
| AS05, tabacchi al livello UE più alto | −2 | prelievo concentrato sui fumatori a basso reddito, trinciato incluso |
| SAD12, IVA sul gas domestico al 22% | −2 | bene essenziale; il bonus sociale copre solo ISEE ≤15.000 € |
| SF15, IVA ridotta dal 10% al 12% | −1 | IVA regressiva, attenuata da esclusioni e maggiorazione di AUU e ADI |
| SAD13, uscita completa dai SAD del gasolio | −1 | pesa su aziende agricole, aree rurali e prezzi; sostegni ai redditi agricoli |

Seguono con −1: AS01, SAD01, AS02, AS03, SAD02, SAD10, PE03.

**Le 5 misure più progressive (EQU).**

| Misura | EQU | Perché |
|---|---|---|
| SF13, catasto a valori di mercato e IMU sulle prime case di pregio | +2 | franchigia di valore, detrazione piena per ISEE ≤25.000 € |
| SF14, imposta di successione | +2 | colpisce patrimoni ereditati oltre 500.000 € per erede |
| SF06, detrazione sanitaria decrescente tra 50.000 e 120.000 € | +2 | salve disabilità, cronicità e non autosufficienza |
| SF07, deducibilità dei fondi sanitari oltre 75.000 € | +2 | beneficio concentrato sui redditi più alti |
| PE01, contributo sulle pensioni oltre 100.000 € | +2 | aliquote progressive, solo sulla quota retributiva |

Seguono con +1: SF11, SF12, SAD14, SAD05, SAD03, SAD11, SF01, SF02, SF03, SF08, SF09, PE02, PE04, RB01, RB02, RA10.
