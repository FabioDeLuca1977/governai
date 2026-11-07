# Verifica dati: Area 01, Economia, Imprese, Turismo

*Verifica del 7 novembre 2026. Dossier: `ministeri/01_economia_imprese.md`. Script riproducibile: `dati/script/01_economia.py` (serie in `dati/serie/01_*.csv`, registro `dati/serie/_registro_01.csv`, PDF ufficiali e testo estratto in `dati/raw/01_*`). Le cifre tratte dai PDF sono in `01_estratti_documenti.csv`: lo script controlla che ogni cifra compaia davvero nel testo del documento (17 su 17 trovate).*

**Esiti:** ✅ 19 confermati · ✏️ 12 corretti · ❓ 10 non verificabili su fonte primaria (41 righe in tabella).

## Tabella di verifica

| # | Dato | Valore nel dossier | Valore verificato | Fonte primaria (ente, documento/serie, anno, URL) | Esito |
|---|---|---|---|---|---|
| 1 | Dimensione manovra 2027 | 23,5 mld lordi, ~0,98% PIL | Impieghi pari allo 0,98% del PIL 2027 (2.400,6 mld), cioè 23,5 mld; impatto netto sul deficit -0,54% | MEF, DPB 2027, tab. I.6-1 e III.1-1, ott. 2026, [PDF](https://www.mef.gov.it/export/sites/MEF/inevidenza/2026/article_00393/Italys-DBP-2027.pdf) | ✅ |
| 2 | Stanziamenti MIMIT e Turismo | "pochi miliardi" | non verificato | Bilancio dello Stato (RGS) non consultato | ❓ |
| 3 | Clausola nazionale di salvaguardia | 0,6 pp per la difesa su 1,5 | 0,6 pp l'anno nel 2027-28 = **0,3 difesa + 0,3 resilienza energetica**, su un limite di 1,5 | MEF, DPB 2027, par. I.5 | ✏️ |
| 4 | Debito/PIL 2025 | 136,7% | 136,7% | Eurostat gov_10dd_edpt1 (serie `debito_pil`); DPB 2027 tab. III.1 | ✅ |
| 5 | Debito/PIL 2026, 2027, 2029 | 138,1 / 138,5 / 136,6 | 138,1 / 138,5 / 137,9 (2028) / 136,6 | MEF, DPB 2027, tab. III.1 | ✅ |
| 6 | Debito/PIL 2026, stima UPB | 138,6% (UPB, luglio 2026) | 138,6% è la stima **di primavera del MEF (DFP 2026)**, citata come tale dal DPB e ripresa dall'UPB. Il comunicato UPB di luglio non è stato consultato | MEF, DPB 2027, par. I.7 | ✏️ (attribuzione) |
| 7 | Deficit 2026 / 2027 | 2,9% / 3,4% | -2,9% / -3,4% (2025: -3,1%) | MEF, DPB 2027, tab. III.1-5; Eurostat (serie `deficit_pil`) | ✅ |
| 8 | Spesa per interessi, % PIL | "intorno al 4%"; 4,1% nel 2027 (Unimpresa) | 3,8% (2025), **4,2% (2026), 4,3% (2027)** | MEF, DPB 2027, tab. III.1-5; Eurostat gov_10a_main | ✏️ |
| 9 | Spesa per interessi, importo | 80-90 mld l'anno | 87,2 mld nel 2025; circa 98 mld nel 2026 e 103 mld nel 2027 (calcolo GovernAI: % DPB × PIL nominale DPB) | Eurostat gov_10a_main (`01_interessi_mio_eur`); DPB 2027 | ✏️ |
| 10 | Stock del debito fine 2025 | ~3.095 mld (stampa) | **3.097,1 mld** | Eurostat gov_10dd_edpt1 (`01_debito_mio_eur`); DPB 2027 tab. III.1-5 | ✏️ (lieve) |
| 11 | Pressione fiscale 2025 | 42,9% | 42,9% (ISTAT, def. nazionale); 43,0% (Eurostat) | ISTAT, Conti economici nazionali 2010-2025, 22/9/2026 (dato riportato da più fonti, comunicato non scaricato); Eurostat gov_10a_taxag (`01_pressione_fiscale_pil`) | ✅ |
| 12 | "Livello più alto dal 2014" | dal 2014 | Nella serie Eurostat il 2015 è più alto (43,2%) e il 2020 è uguale (43,0%): è il valore più alto **dopo il 2015**, pari al 2020 | Eurostat gov_10a_taxag | ✏️ |
| 13 | Tax gap complessivo 2023 | 107,9-112,8 mld | 107,9-112,8 mld | MEF, Relazione evasione 2026, cap. I, [PDF](https://www.mef.gov.it/export/sites/MEF/inevidenza/2026/article_00390/Relazione-evasione-fiscale-e-contributiva-2026_09_30.pdf) | ✅ |
| 14 | Gap IVA 2023 e variazione | ~34,4 mld, +3,6 mld sul 2022 | 34.355 mln (2022: 30.736), +3,6 mld | MEF, Relazione evasione 2026, tab. III.1 | ✅ |
| 15 | Numero spese fiscali | 573 | 573 misure erariali | MEF, Rapporto annuale spese fiscali 2025 (giugno 2026), [PDF](https://www.mef.gov.it/export/sites/MEF/documenti-allegati/2025/RSF-2025-bis.pdf) | ✅ |
| 16 | Costo spese fiscali 2026 | ~130 mld | 129,7 mld (2027: 104,8; 2028: 87,6) | MEF, Rapporto spese fiscali 2025 | ✅ |
| 17 | Spese fiscali UPB | 625 misure, ~105 mld; 466 nel 2018 | 625 e 105 mld (2024), da 466 e 54 mld (2018) | UPB, Focus 4/2024, comunicato 11/4/2024, [PDF](https://www.upbilancio.it/wp-content/uploads/2024/04/Comunicato-stampa-Focus-4_2024.pdf) | ✅ |
| 18 | Oltre metà delle misure con meno di 30.000 contribuenti | UPB | non presente nel comunicato UPB; il Focus completo non è stato consultato | UPB, Focus 4/2024 | ❓ |
| 19 | Produttività 1995-2024: IT vs UE27 | +0,3% vs +1,5% l'anno | +0,3% vs +1,5% (valore aggiunto per ora lavorata). Controllo Eurostat su PIL per ora: +0,27% vs +1,16% | ISTAT, Misure di produttività 1995-2024, dic. 2025, [PDF](https://www.istat.it/wp-content/uploads/2025/12/REPORT_PRODUTTIVITA_2024.pdf); Eurostat nama_10_lp_ulc (`01_produttivita_ora_i15`) | ✅ |
| 20 | Produttività 2024 / 2023 | -1,9% / -2,7% | -1,9% / -2,7% | ISTAT, Misure di produttività | ✅ |
| 21 | Occupati in micro e piccole imprese | "oltre il 60%" vs ~40% FR/DE | **60,0%** (0-49 addetti) vs 41,6% FR, 39,4% DE (2024) | Eurostat sbs_sc_ovw (`01_quota_occupati_micro_piccole`) | ✏️ (lieve: "il 60%", non "oltre") |
| 22 | Investimenti intensivi in conoscenza | 18,9% nel 2025 | non verificato sul Rapporto annuale ISTAT | ISTAT, Rapporto annuale 2026 (non consultato) | ❓ |
| 23 | PUN medio 2025 Italia | 115 €/MWh | 115,32 €/MWh | GME, newsletter, tramite [QualEnergia](https://www.qualenergia.it/pro/articoli-pro/nel-2025-pun-medio-a-115-euro-mwh/) (dato GME, documento GME non scaricato) | ✅ |
| 24 | Prezzi all'ingrosso DE / ES / FR | 91 / 68 / 61 | non verificato sulle borse elettriche (EEX/OMIE/EPEX) | Confindustria, audizione marzo 2026 (fonte associativa) | ❓ |
| 25 | Spesa elettrica del terziario | +38,9% sul 2019 | non verificato | Osservatorio Confcommercio (fonte associativa) | ❓ |
| 26 | Transizione 5.0 | 6,3 → 2,5 mld; sostituita dall'iperammortamento | Cifre confermate da più fonti specializzate. Precisazione: le risorse residue sono andate **esaurite** a novembre 2025 (decreto MIMIT 6/11/2025) | Decisione UE di revisione del PNRR non consultata | ❓ (dato coerente, fonte primaria non scaricata) |
| 27 | Spesa PNRR a settembre 2026 | ~86 mld | non verificato su ReGiS/Italia Domani | Dichiarazione ministeriale | ❓ |
| 28 | Rischio PNRR secondo la Corte dei conti | ~15 mld | non verificato. La relazione delle Sezioni riunite è del 28 maggio 2026; la Sezione autonomie (del. 11/2026) parla di circa 45 mld a rischio sugli enti territoriali (dato di stampa) | Corte dei conti (non consultata) | ❓ |
| 29 | Presenze turistiche 2024 | 458,4 mln (+2,5%) | **466,2 mln (+4,2%)**, di cui 253,9 mln di stranieri | ISTAT via Eurostat tour_occ_ninat (`01_presenze_turistiche`), agg. 12/10/2026 | ✏️ |
| 30 | Presenze straniere 2025 | 271 mln (+6,7%, stima) | **301,6 mln** (Eurostat); ISTAT: totale oltre 535 mln, quota estera 55,3%. Salto del 15% sul 2024: il campo di osservazione è stato ampliato, quindi i dati non sono pienamente confrontabili | Eurostat tour_occ_ninat; ISTAT, Storie di dati Turismo, ott. 2026 | ✏️ |
| 31 | Spesa dei turisti stranieri 2025 | 57 mld | non verificato su Banca d'Italia (indagine sul turismo internazionale) | Banca d'Italia (non consultata) | ❓ |
| 32 | 75% dei turisti nel 4% del territorio | TEHA | dato TEHA citato in un documento del Ministero del Turismo; non è un dato statistico ufficiale | MiTur, presentazione gennaio 2026 | ❓ |
| 33 | Presenze in Sardegna | "oltre 22 milioni" | **15,6 mln nel 2024**; 21,7 mln nel 2025 con il nuovo campo di osservazione | Eurostat tour_occ_nin2, ITG2 (`01_presenze_sardegna`) | ✏️ |
| 34 | Economia non osservata 2023 | oltre 217 mld | 217,5 mld, 10,2% del PIL | ISTAT, Economia non osservata 2023, ott. 2025, [PDF](https://www.istat.it/wp-content/uploads/2025/10/Report-ECONOMIA-NON-OSSERVATA-NEI-CONTI-NAZIONALI_ANNO2023.pdf) | ✅ |
| 35 | Catalogo SAD MASE | "importo da verificare" | circa 22,4 mld nel 2025 (VIII edizione, luglio 2026, dato di stampa). Il PNRR/REPowerEU prevede un taglio dei SAD di 4,5 mld anticipato al 2026 | Rapporto spese fiscali 2025 (target PNRR); Catalogo MASE non scaricato | ✏️ (importo inserito, da fonte secondaria) |
| 36 | Tax gap IVA nella Proposta 3 | ~34 mld | 34,4 mld | come #14 | ✅ |
| 37 | Proposta 2: 5-8 mld = 0,25-0,35% PIL = 5-6% del costo | — | 0,22-0,35% del PIL 2025; 3,9-6,2% del costo 2026; 5,7-9,1% del costo 2028 | calcolo GovernAI su RSF 2025 e PIL Eurostat | ✏️ (aritmetica) |
| 38 | Proposta 2: obiettivo ufficiale esistente | non citato | Il Piano strutturale di bilancio prevede già un recupero di **7,37 mld** dal riordino delle spese fiscali (benchmark 49,1 mld) | MEF, Rapporto spese fiscali 2025 | ✅ (nuovo riferimento ufficiale) |
| 39 | Proposta 3: 15-20% del gap IVA = 5-7 mld | — | 5,2-6,9 mld | calcolo su #14 | ✅ |
| — | Nota di bilancio: P2 + P3 = 10-15 mld | — | 5-8 + 5-7 = 10-15 mld | coerenza aritmetica | ✅ |
| — | Data di chiusura del PNRR, 31/8/2026 | — | non ricontrollata (dato normativo noto) | — | ✅ (non modificato) |

Le stime di costo delle proposte (P1 10-20 mln; P3 0,3-0,5 mld; P4 2-3 mld; P5 0,5-1 mld; P6 0,3-0,8 e 0,1-0,2 mld) restano **stime GovernAI**: non esistono quantificazioni UPB, RGS o della Corte dei conti per queste misure. Nel dossier ora sono etichettate così. Unica eccezione: per la Proposta 2 è stato aggiunto il riferimento all'obiettivo ufficiale del Piano strutturale di bilancio (7,37 mld).

## Impatto sulle proposte

**Nessun punteggio cambia.** Le correzioni rafforzano o precisano la diagnosi, ma non cambiano la direzione né l'intensità degli effetti valutati. In dettaglio:

1. **Interessi più alti del previsto (✏️ #8-9).** Secondo il DPB la spesa sale al 4,3% del PIL nel 2027, oltre 100 mld, e non al 4,1% indicato da Unimpresa. Questo rafforza la motivazione della **Proposta 1**, il cui punteggio di lungo periodo è già al massimo (+3), e della quota della **Proposta 2** destinata al deficit. Nessuna modifica ai punteggi.
2. **Spese fiscali in calo "naturale" (#16) e obiettivo ufficiale già esistente (#38).** Il costo scende da 129,7 a 87,6 mld entro il 2028 perché scadono i bonus edilizi. Quindi l'obiettivo di 5-8 mld della **Proposta 2** pesa di più sulla base residua: il 6-9%, non il 5-6%. In più, il Piano strutturale di bilancio conta già 7,37 mld di recupero dal riordino delle spese fiscali. **Conseguenza per la copertura:** i risparmi della Proposta 2 non possono finanziare il taglio del cuneo e la riduzione del deficit *in aggiunta* a quanto già programmato nel tendenziale e nel Piano. Rischierebbero di essere contati due volte. Nel dossier ora la Proposta 2 è presentata come lo strumento per raggiungere l'obiettivo del Piano. La parte destinata al cuneo va quindi coperta solo con risparmi *oltre* i 7,37 mld, oppure riconosciuta come già scontata nei saldi. La sostanza della proposta non cambia. Il punteggio di breve periodo (-1) resta: la riforma può ancora essere percepita come un costo immediato.
3. **Clausola di salvaguardia (✏️ #3).** Solo metà dello spazio usato (0,3 pp) va alla difesa: l'altra metà va all'energia. Per la **Proposta 5**, una parte delle risorse della clausola è già destinata alla sicurezza energetica (ad esempio il sostegno ai prezzi per una quota dei consumi e gli investimenti nel fotovoltaico, DPB par. I.6). Questo è un possibile canale di coordinamento o di copertura per il fondo di garanzia dei PPA, ma non cambia il punteggio. Nella sezione D, il conflitto "Difesa ↔ bilancio" è stato precisato.
4. **Turismo (✏️ #29, #30, #33).** Le presenze sono più alte di quanto indicato, ma la serie 2025 non è pienamente confrontabile con gli anni precedenti. Il problema della concentrazione, base della **Proposta 6**, resta, ma il dato chiave del 75% nel 4% del territorio non è verificato su dati ufficiali (❓ #32). Si raccomanda di ricalcolare l'indicatore di concentrazione con i dati ISTAT comunali sulle presenze prima di usarlo come baseline. Nessuna modifica ai punteggi, la cui confidenza era già "Bassa" sul medio e lungo periodo.
5. **Pressione fiscale "più alta dal 2014" (✏️ #12).** La correzione è solo descrittiva e non ha effetti sulle proposte.

## Segnalazioni tecniche

- **fonti.py: `eurostat()` scarta i flag di stato** (p = provvisorio, b = rottura di serie). Per le presenze turistiche 2025 la rottura è emersa solo dal salto anomalo dei valori e dalla nota ISTAT. Ho aggirato il problema annotando la discontinuità nel campo `nota` del registro. Consiglio: conservare `js["status"]` in una colonna `flag`. fonti.py non è stato modificato.
- I PDF dell'Osservatorio CPI che replicano la Relazione evasione restituivano 404, quindi è stata usata la copia ufficiale sul sito MEF. Il comunicato UPB restituisce 403 a WebFetch ma si scarica con `scarica()`.
- **Nessuna fonte ha richiesto un login.** I dati ❓ dipendono da documenti non consultati per limiti di tempo (Corte dei conti PNRR, Banca d'Italia turismo, Rapporto annuale ISTAT, Catalogo MASE, bilancio RGS), non da restrizioni di accesso.
