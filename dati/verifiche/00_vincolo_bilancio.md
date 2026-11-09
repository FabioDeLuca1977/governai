# Il vincolo di bilancio comune di GovernAI

*Agente "vincolo di bilancio", 7 novembre 2026. Script riproducibile: `dati/script/00b_bilancio.py`. Documenti in `dati/raw/00b_*` con il testo estratto; serie in `dati/serie/00b_*.csv` (registro `_registro_00b.csv`); output in `registro/vincolo.csv` (83 righe) e `registro/fondi.csv` (18 fondi). Lo script controlla che le cifre trascritte compaiano nei PDF: 17 su 17 trovate.*

Tutti gli importi sono in miliardi di euro. Il PIL 2026-29 è calcolato da GovernAI con le crescite nominali programmatiche del DPFP 2026 (Tav. I.3.3): 2.326 mld nel 2026, 2.401 nel 2027, 2.473 nel 2028, 2.537 nel 2029.

## 1. La regola che conta: il tetto alla spesa netta

Con le regole UE in vigore dal 2024 l'indicatore che conta è uno solo, la **spesa netta**. È la spesa primaria finanziata con risorse nazionali, al netto delle misure una tantum, della spesa finanziata dalla UE e del suo cofinanziamento, della parte ciclica dei sussidi di disoccupazione e delle **misure discrezionali di entrata** (DRM). In pratica:
- una nuova spesa è ammessa solo se è coperta da un **aumento di imposte deciso per legge** (una DRM) o da un **taglio di altra spesa**;
- un maggior gettito che non deriva da una nuova legge, come il recupero dell'evasione per maggiore adempimento, riduce il deficit ma **di norma non crea spazio** sotto il tetto.

L'Italia è in procedura per disavanzo eccessivo (PDE), quindi i limiti sono vincolanti.

| Anno | Tetto UE (crescita annua) | Tetto cumulato dal 2023 | Tendenziale | Programmato | Programmato al netto della clausola nazionale (NEC) |
|---|---|---|---|---|---|
| 2025 | 1,3% | -0,7% | — | 1,5% | 1,5% |
| 2026 | 1,6% | 0,9% | — | 1,6% | 1,6% |
| 2027 | 1,9% | 2,8% | 2,1% | **3,3%** | **1,9%** |
| 2028 | 1,7% | 4,6% | 1,3% | 1,7% | **1,7%** |
| 2029 | 1,5% | 6,2% | 1,1% | 0,2% | **1,5%** |

Fonti: Raccomandazione del Consiglio UE del 21/1/2025 sul Piano strutturale di bilancio (PSB); MEF, [DPB 2027](https://www.mef.gov.it/export/sites/MEF/inevidenza/2026/article_00393/Italys-DBP-2027.pdf), Tab. III.1-1; MEF, [DPFP 2026](https://www.mef.gov.it/export/sites/MEF/inevidenza/2026/article_00390/DPFP26.pdf), Tav. II.1.5.

**Conto di controllo.** La crescita della spesa netta ha superato il tetto nel 2024 (-1,8% contro -1,9%) e nel 2025 (1,5% contro 1,3%). Secondo l'UPB la **deviazione cumulata è dello 0,1% del PIL**, circa 2,4 mld. Resta tale fino al 2029, perché il percorso programmato non la riassorbe: la crescita cumulata al netto della NEC arriva al 6,6%, contro il 6,2% raccomandato. La soglia di tolleranza UE è dello 0,6% del PIL cumulato, ma la tolleranza **non è un margine da spendere**. Fonte: UPB, [Audizione sul DPFP 2026](https://www.upbilancio.it/wp-content/uploads/2026/10/UPB-Audizione-DPFP-2026.pdf), 12/10/2026, tab. 4.4 e par. 4.3. La Commissione, a giugno 2026, registrava per il 2025 un debito di circa 0,1 punti su base annua e un saldo cumulato nullo (DPFP, nota 137).

**Clausola nazionale di salvaguardia (NEC).** Vale 0,3% del PIL per la difesa e 0,3% per la sicurezza energetica, nel 2027 e nel 2028: circa **29 mld nel biennio**. Il limite UE per la difesa è dell'1,5% del PIL annuo. Questa flessibilità è già **interamente usata** dal Governo. Dal 2029 la clausola non c'è più, ma la UE chiede di mantenere stabilmente più alta la spesa per la difesa: circa 7,6 mld/anno da assorbire entro il tetto (calcolo GovernAI: 0,3% del PIL 2029).

### Margine residuo: zero, anzi leggermente negativo

- La crescita programmata al netto della NEC **coincide con il tetto in ogni anno dal 2026 al 2029**. L'UPB lo dice così: «I margini consentiti dal percorso di spesa netta sarebbero utilizzati per intero».
- Gli spazi che il DPFP vedeva nel 2028 (0,3 punti) e nel 2029 (0,2 punti) sono già stati usati dagli effetti pluriennali del DDL 2027.
- Il margine residuo per il programma è quindi **0**, e **circa -2,4 mld** se si conta la deviazione cumulata.
- **Ogni euro di nuova spesa del programma va coperto con DRM o tagli di spesa.**

## 2. Quadro programmatico

| | 2025 | 2026 | 2027 | 2028 | 2029 |
|---|---|---|---|---|---|
| Indebitamento netto (% PIL) | -3,1 | -2,9 | -3,4 | -3,2 | -2,3 |
| Debito (% PIL) | 136,7 | 138,1 | **138,5** | 137,9 | 136,6 |
| Interessi (% PIL) | 3,8 | 4,2 | 4,3 | — | 4,6-4,7 (UPB) |

Fonte: DPB 2027, Tab. III.1-2 e III.1-5. Al netto della NEC il deficit resterebbe sotto il 3%, condizione per uscire dalla PDE.

**Manovra 2027** (DPB, Tab. I.6-1; importi in mld calcolati da GovernAI dalle % del PIL):

| | 2027 | 2028 | 2029 |
|---|---|---|---|
| Impieghi | 23,5 (0,98%) | 24,5 (0,99%) | 16,5 (0,65%) |
| Coperture | 10,3 (0,43%) | 11,1 (0,45%) | 12,7 (0,50%) |
| Effetto netto sul deficit | **-13,0** (-0,54%) | -13,8 (-0,56%) | -3,8 (-0,15%) |

Le coperture 2027 sono:
- settore finanziario: 5,0 mld;
- revisione della spesa dei ministeri: 1,2 mld;
- giochi: 0,7 mld;
- altre entrate: 1,7 mld;
- altre coperture di spesa: 1,7 mld.

Il deficit in più corrisponde in sostanza alle spese coperte dalla NEC (difesa ed energia).

## 3. Politiche invariate

Molte misure del DDL 2027 valgono **solo per il 2027** o per il 2027-28. Per mantenerle nel 2028 bisogna trovare nuove coperture, che si sommano a quelle del programma. La stima GovernAI si basa sulle cifre della Relazione illustrativa del [DDL A.C. 3174](https://documenti.camera.it/leg19/pdl/pdf/leg.19.pdl.camera.3174.19PDL0221140.pdf). Non esiste una stima ufficiale UPB o MEF a "politiche invariate": l'audizione UPB sul DDL 2027 non era ancora pubblicata al 7/11/2026.

| Misura | Costo annuo di rinnovo (mld) |
|---|---|
| Fondo contenziosi nazionali ed europei | 1,9 |
| Carta 300 € over 75 e prestazione universale | 1,8 |
| Sostegno temporaneo all'energia delle imprese | 1,7 |
| IRPEF: secondo scaglione esteso a 55.000 € | 1,4 |
| Credito d'imposta ZES | 1,4 |
| Imposta del 5% sui rinnovi contrattuali | 1,0 |
| Missioni internazionali | 0,8 |
| Detrazioni edilizie e bonus mobili | 0,5 |
| Detassazione salario accessorio PA e privati | 0,7 |
| Under 30, forfettario, Ape sociale, esoneri, redditi agrari | 1,4 |
| **Totale** | **≈ 12,6 (intervallo 10-14), cioè 0,5% del PIL** |

Il totale non comprende due voci:
- i rinnovi contrattuali della PA 2028-30, non quantificati;
- dal 2029, il **mantenimento della spesa per la difesa dopo la NEC**, circa 7,6 mld/anno.

## 4. Residui passivi e stanziamenti non spesi

Fonte: Corte dei conti, Relazione sul Rendiconto 2025, via [dossier Camera BI0295](https://documenti.camera.it/leg19/dossier/Pdf/BI0295.pdf); OpenBDAP-RGS, Rendiconto 2025 per capitolo (serie `00b_residui_ministeri_2025`). Lo stock al 31/12/2025 è di **197,2 mld**, di cui 195,2 per spese finali:
- 113,6 mld sono **residui di stanziamento**, cioè somme stanziate e mai impegnate;
- 83,6 mld sono **residui propri**, cioè somme impegnate e non pagate;
- i **perenti** sono 46,3 mld.

Le economie di competenza 2025 ammontano a 38,6 mld.

| Ministero | Residui al 31/12/2025 | Economie di competenza 2025 |
|---|---|---|
| Economia e finanze | 126,7 | 13,5 |
| Infrastrutture e trasporti | 21,1 | 0,3 |
| Lavoro e politiche sociali | 15,1 | 19,4 |
| Interno | 9,7 | 1,1 |
| Istruzione e merito | 4,3 | 0,6 |
| Imprese e made in Italy | 3,9 | 0,1 |
| Ambiente e sicurezza energetica | 2,7 | 0,1 |
| Difesa | 2,5 | 1,3 |
| Salute | 2,3 | 0,3 |
| Altri sei ministeri | 6,9 | 1,8 |

**Quanto è riprogrammabile? Poco.** Le previsioni di spesa della PA, in contabilità nazionale, stimano ciò che verrà effettivamente pagato, non ciò che è stanziato. Spendere residui o stanziamenti che altrimenti sarebbero rimasti fermi **aumenta la spesa netta** e quindi richiede una copertura. La revisione della legislazione vigente taglia già i capitoli con economie sopra il 10%. Stima GovernAI per la riallocazione vera, cioè il taglio di spese che si sarebbero effettivamente fatte, oltre agli 1,2-2 mld già usati dal DDL: **0,5-2 mld/anno**.

## 5. Capienza dei fondi

Per ogni fondo il dettaglio di fonti e vincoli è in `registro/fondi.csv`.

| fondo_id | Capienza nuova min-max (mld/anno) | Già impegnato | Natura | Nota chiave |
|---|---|---|---|---|
| SAD | 2,0-8,0 | 4,5 | permanente | stima GovernAI su 17,1 riformabili; è l'unica fonte grande |
| SPESE_FISCALI | 0-3,0 | 7,37 | permanente | solo oltre quanto già nel PSB |
| ETS | 0-0,3 | 2,6 | permanente | tutto già destinato per legge |
| ETS2_FSC | 0-1,0 | 1,3 | temporanea | Piano sociale per il clima da 9,3 mld già programmato |
| IVA_EVASIONE | 0-6,9 | — | incerta, certificazione | non crea spazio sul tetto |
| FSN | 0-0,5 | 2,4 | permanente | incremento del DDL già destinato |
| COESIONE_2127 | 2,0-5,0 | 47,4 selezionati | una tantum | 28,5 mld non ancora selezionati, fino al 2029 |
| COESIONE_2834 | 0-3,0 | — | incerta | QFP non approvato, non prima del 2029 |
| PENSIONI | 0,3-1,0 | 0 | permanente | quote già fuori dal tendenziale |
| TASSA_SOGGIORNO | 0,1-0,4 | 1,0 | permanente | entrata dei Comuni |
| ACCISE_SALUTE | 0,5-1,5 | 0,45 | permanente | tabacchi e sugar tax già nel DDL |
| RIORDINO_BONUS | 0,3-1,5 | — | permanente | solo tagli di bonus permanenti |
| FONDI_UE | 0-1,0 | 8,0 (SAFE) | temporanea | fuori bilancio o debito |
| RIALLOCAZIONE | 0,5-2,0 | 1,2 | permanente | vedi §4 |
| RISPARMI_ATTESI | 0-∞ | — | incerta | mai come copertura ex ante |
| TARIFFE | 0-∞ | — | incerta, fuori bilancio | paga l'utenza |
| DEFICIT | **-2,4-0** | — | — | nessun margine |

**Totale in bilancio** (esclusi DEFICIT e voci illimitate): **5,7-34,1 mld/anno**. La quota **permanente**, l'unica adatta a spese strutturali, è di **3,7-18,2 mld/anno**. Escludendo anche l'evasione IVA (incerta e da certificare) e la coesione (una tantum), restano risorse permanenti e certe per circa **3,7-18 mld**, di cui oltre la metà dai SAD.

## 6. Dati più incerti

1. **Costo delle politiche invariate** (10-14 mld): è una stima GovernAI sulle cifre triennali del DDL, senza una stima ufficiale UPB o MEF.
2. **Capienza dei SAD** (2-8 mld): i valori del Catalogo MASE sono teorici "a comportamento invariato". Non è chiaro quanto dei 4,5 mld del target PNRR sia già stato realizzato.
3. **Coesione** (2-5 mld/anno, una tantum): la quota realmente riprogrammabile dipende dai vincoli UE e dal rischio di disimpegno.

Sono incerti anche la quota nazionale dei proventi ETS2 dopo il 2028 e la valutazione della Commissione sul conto di controllo (autunno 2026).

## Cosa significa per il programma GovernAI

Il vincolo è stretto e semplice da enunciare: **il programma non ha margine in deficit**. Il percorso di spesa netta concordato con la UE è già usato per intero dal 2027 al 2029, e resta un piccolo scostamento da recuperare (circa 2,4 mld). La flessibilità per difesa ed energia è già spesa.

Ne derivano tre conseguenze.

1. **Ogni proposta deve portare la sua copertura**, sotto forma di nuove entrate decise per legge (riforma dei SAD, riordino delle spese fiscali oltre il Piano, accise sulla salute, contributo di equità) o di tagli di spese che si sarebbero davvero fatte. Il recupero dell'evasione IVA va bene per ridurre il debito, non per finanziare spesa permanente. Spendere i residui non spesi non è una copertura.
2. **Prima delle 52 proposte c'è un conto già aperto**: circa 10-14 mld l'anno per rinnovare le misure temporanee della manovra 2027. Dal 2029 si aggiungono circa 7,6 mld per mantenere la spesa per la difesa.
3. **Le risorse permanenti credibili valgono 4-18 mld l'anno**, contro 27-45 mld di proposte senza Difesa. Più della metà dipende dai SAD. La scelta tra dividendo alla cittadinanza e servizi decide quante proposte strutturali restano finanziabili. I fondi di coesione possono sostenere investimenti una tantum fino al 2029, non personale o prestazioni stabili.

Per i 9 agenti ministeriali la regola pratica è questa: **si negozia una torta di 4-18 mld l'anno a regime, non di più**. Se il Governo rinnova le misure temporanee, i loro 10-14 mld vanno tolti prima da questa stessa torta. Le proposte vanno ordinate per priorità.
