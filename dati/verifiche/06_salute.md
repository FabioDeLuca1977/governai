# Verifica dati: area 06 (Salute)

*Verificatore dati GovernAI, 7 novembre 2026. Dossier: `ministeri/06_salute.md`. Script riproducibile: `dati/script/06_salute.py`. Serie: `dati/serie/06_*.csv`, con registro in `dati/serie/_registro_06.csv`. Documenti grezzi: `dati/raw/06_*.pdf`.*

## Quadro programmatico: FSN e spesa sanitaria in rapporto al PIL

Il documento ufficiale più recente è il **Documento programmatico di finanza pubblica 2026** (MEF, approvato il 2/10/2026). Non pubblica un rapporto FSN/PIL né un obiettivo per il FSN. Pubblica la **spesa sanitaria della PA a legislazione vigente** (Tav. II.1.1A-B, prima della manovra 2027):

| | 2025 | 2026 | 2027 | 2028 | 2029 |
|---|---|---|---|---|---|
| Spesa sanitaria PA (mln €) | 141.539 | 148.836 | 151.668 | 155.647 | 160.035 |
| % del PIL (DPFP) | 6,2 | 6,4 | 6,3 | 6,3 | 6,3 |
| PIL nominale tendenziale (mln €) | 2.265.002 | 2.326.150 | 2.393.639 | 2.459.360 | 2.524.049 |
| FSN (mln €) | 136.540 | 142.900 | 146.265 | 147.152 | 148.200 ❓ |
| FSN / PIL (calcolo GovernAI) | 6,03% | 6,14% | 6,11% | 5,98% | 5,87% ❓ |

FSN: livello vigente secondo la Camera dei deputati (tema "Organizzazione del SSN", 31/7/2026, su dati Corte dei conti; 2025 = riparto CIPESS), più gli incrementi dell'art. 69, c. 1, del DDL bilancio 2027 (A.C. 3174): +2.365, +2.352 e +2.399 mln. Per il 2029 la base vigente non è pubblicata, quindi resta il valore Gimbe (148,2 mld). Il PIL 2025 del DPFP coincide con la serie Eurostat già scaricata (`pil_mld_eur.csv`, 2.265 mld).

## Tabella di verifica

| Dato | Valore nel dossier | Valore verificato | Fonte primaria (ente, documento/serie, anno, URL) | Esito |
|---|---|---|---|---|
| FSN 2027 | 146,3 mld | 146,27 mld (143,9 vigente + 2,365) | Camera dei deputati, tema Organizzazione SSN, 2026, https://temi.camera.it/leg19/temi/19_tl18_organizzazione_ssn ; DDL bilancio 2027 A.C. 3174 art. 69, https://documenti.camera.it/leg19/pdl/pdf/leg.19.pdl.camera.3174.19PDL0221140.pdf | ✅ |
| FSN 2028 | 147,1 mld | 147,15 mld | come sopra | ✅ |
| FSN 2029 | 148,2 mld | base vigente 2029 non pubblicata; incremento DDL 2,399 mld confermato | come sopra | ❓ |
| Fondi nuovi per anno | circa 2,4 mld/anno | 2.365 / 2.352 / 2.399 mln | DDL bilancio 2027, art. 69 c. 1 | ✅ |
| Fondi nuovi nel triennio | 7,1 mld | 7,116 mld | DDL bilancio 2027, art. 69 c. 1 | ✅ |
| Richiesta delle Regioni | oltre 18 mld | non trovata su fonte primaria | (Gimbe, stampa) | ❓ |
| FSN/PIL 2026 | 6,14% | 6,14% | FSN Camera/Corte dei conti; PIL MEF DPFP 2026 Tav. II.1.1A, https://www.mef.gov.it/export/sites/MEF/inevidenza/2026/article_00390/DPFP26.pdf | ✅ |
| FSN/PIL 2029 | 5,87% | 5,87% solo se il FSN 2029 è 148,2 mld | come sopra | ❓ |
| "Il quadro programmatico porta il FSN al 5,87% nel 2029" (sez. D) | 5,87% | il DPFP non fissa il FSN/PIL; la spesa sanitaria della PA è al 6,4% nel 2026 e al 6,3% nel 2027-2029 | MEF, DPFP 2026, Tav. II.1.1B | ✏️ |
| Spesa out-of-pocket | 41,3 mld (2024), 22,3% | 42,8 mld e 23,0% nel 2024 (rivisto); **42,4 mld e 22,3% nel 2025** | ISTAT, conti SHA, via Eurostat hlth_sha11_hf (HF3), agg. 4/11/2026, serie `06_spesa_sanitaria_finanziamento` | ✏️ |
| Quota out-of-pocket fuori LEA | circa tre quarti | non verificato | (Quotidiano Sanità/OASI) | ❓ |
| Rinuncia alle cure in Sardegna | 13,7% | non verificato sulle tavole ISTAT; altre fonti citano 17,2% (2024) | ISTAT BES (non trovato nei flussi BES territoriali scaricabili) | ❓ |
| Rinuncia alle cure, Italia | "stima, da verificare" | bisogni non soddisfatti (costo, distanza, attesa): **2,5% nel 2025** (1,9% nel 2024; UE 2,4%) | Eurostat hlth_silc_08 (EU-SILC), 2025, serie `06_bisogni_non_soddisfatti` | ✏️ |
| Liste d'attesa, I semestre 2026 | +1,6 mln nei tempi; 2,8 mln fuori soglia | confermati solo da stampa; bollettino al 30/9: circa 4 mln oltre o vicino alla soglia (stampa) | Agenas, bollettino (PDF originale non recuperato) | ❓ |
| Liste d'attesa, gen.-apr. 2026 | 2,4 mln su 12 mln | solo stampa | Agenas via LaPresse | ❓ |
| 16 Regioni su 21 migliorano | 16/21 | solo stampa | Agenas via stampa | ❓ |
| Personale infermieristico per 1.000 ab. | 6,9 contro 9,2 OCSE (2023) | 6,9 contro 9,2 (2023); Eurostat: 6,83 (2023), 6,92 (2024) | OCSE, Health at a Glance 2025, profilo Italia, https://www.oecd.org/en/publications/health-at-a-glance-2025_15a55280-en/italy_c737c936-en.html ; Eurostat hlth_rs_prs2 | ✅ |
| Rapporto personale infermieristico/medico | 1,3 contro circa 2,5 OCSE | 1,3 (6,9/5,4) contro 2,4 (9,2/3,9); Eurostat 1,2 | OCSE, HaaG 2025; Eurostat hlth_rs_prs2 | ✅ |
| Persone laureate in infermieristica | 16,4 contro 44,9 per 100.000 (2022) | non verificato | (Gimbe su OCSE) | ❓ |
| MMG mancanti | oltre 5.500 | non verificato | (Gimbe, VIII Rapporto) | ❓ |
| Personale medico "in linea con l'OCSE" | in linea | **5,4 per 1.000 contro 3,9 OCSE**: sopra la media; Eurostat 5,75 (2024) | OCSE, HaaG 2025; Eurostat hlth_rs_prs2 | ✏️ |
| Età media elevata del personale medico | stima | non verificato (dataset Eurostat per età non disponibile via API) | | ❓ |
| CdC pienamente operative | 66 su 1.715 | 66 su 1.715 (3,9%) | Agenas, Report nazionale DM 77, II semestre 2025 (mar. 2026) | ✅ |
| CdC con almeno un servizio | circa 45% | 781 su 1.715 (45,5%) | Agenas, Report DM 77, II sem. 2025 | ✅ |
| OdC con almeno un servizio | 163 su 594 | 163 su 594 (27,4%) | Agenas, Report DM 77, II sem. 2025 | ✅ |
| Target PNRR CdC/OdC | 1.038 e 307 | 1.038 e 307 | PNRR riveduto (Decisione di esecuzione del Consiglio, dic. 2023), M6C1 | ✅ |
| Lista d'attesa RSA / posti letto | 243.000 / 266.000 | non verificato | (Quotidiano Sanità) | ❓ |
| Prestazione universale | sperimentale fino al 31/12/2026; 500 mln nel biennio | 500 mln 2025-2026 confermati; **prorogata al 31/12/2027**, soglia ISEE 2027 a 12.000 € | D.Lgs. 29/2024; DDL bilancio 2027 art. 53 c. 3 | ✏️ |
| Target ADI over 65 | 10% | 10% | PNRR M6C1 | ✅ |
| Livello ADI effettivo | stima | non verificato | | ❓ |
| Spesa salute mentale / FSN | 2,7–3% (2024) | fonti secondarie tra 2,5% e 3,5%; Rapporto SISM non recuperato | Ministero della Salute, Rapporto salute mentale | ❓ |
| Costo per arrivare al 5% | 2,3 mld/anno | **2,9–3,4 mld/anno** sul FSN 2027 (2–2,3 punti di 146,3 mld) | calcolo GovernAI su FSN verificato | ✏️ |
| Personale DSM e carenza | 30.101 (2022); carenza oltre 14.000 | non verificato | | ❓ |
| Mobilità interregionale | 5,04 mld (2022); 94,1% a LOM-ER-VEN | non verificato su fonte primaria | (Gimbe su dati riparto) | ❓ |
| Spesa farmaceutica pubblica 2025 | 24,94 mld (+5,4%) | 24,95 mld (consuntivo, dati NSIS al 14/5/2026); +5,4% nel comunicato AIFA | AIFA, Monitoraggio spesa gen.-dic. 2025 consuntivo, https://www.aifa.gov.it/documents/20142/3073807/Monitoraggio_Spesa_gennaio-dicembre-2025_consuntivo.pdf | ✅ |
| Sforamento acquisti diretti | circa 4,7 mld | **4,767 mld** (incidenza 11,82% contro tetto 8,30%) | AIFA, consuntivo 2025 | ✏️ |
| Payback a carico delle aziende | 2,385 mld | 2,384 mld (50% di 4,767) | AIFA, consuntivo 2025; ripiano al 50% | ✅ |
| Avanzo convenzionata | circa 460 mln | 459 mln ai fini del tetto; 513 mln al netto dei payback | AIFA, consuntivo 2025 e comunicato | ✅ |
| Voucher per persone anziane, manovra 2027 | 1,6 mld (ItaliaOggi) | Carta valore 300 € per over 75 con pensione fino a 28.000 €: **1.645 mln, solo per il 2027** | DDL bilancio 2027 art. 53 c. 1 | ✏️ |
| Quota della spesa per prevenzione | "piccola quota" (stima) | **4,5% della spesa sanitaria corrente, 8,56 mld (2025)** | ISTAT-SHA via Eurostat hlth_sha11_hc (HC6), serie `06_spesa_sanitaria_funzioni` | ✏️ |
| Gettito della sugar tax | qualche centinaio di milioni (stima) | circa 340 mln/anno (rinvio di 6 mesi = -170,1 mln nel 2027); entrata in vigore rinviata al 1/7/2027 | DDL bilancio 2027 art. 40 e relazione tecnica | ✅ |
| Costo C1 (tempo garantito) | 0,5–1 mld (stima) | nessuna stima ufficiale; confronto: 300 mln nel 2027 per prestazioni aggiuntive | DDL bilancio 2027 art. 69 c. 4 | ❓ (stima GovernAI) |
| Costo C2, C3, C4, C6 (riallocazione) | stime | nessuna stima ufficiale | | ❓ (stima GovernAI) |
| Iter fine vita in Senato | da verificare | non verificato (fuori perimetro numerico) | | ❓ |

**Riepilogo: 43 righe controllate: 15 ✅, 9 ✏️, 19 ❓ (di cui 2 sono stime di costo GovernAI senza equivalente ufficiale).**

## Impatto sulle proposte

1. **Conflitto con Economia (sezione D) e coperture basate sull'incremento del FSN (C2, C3, C5).** La frase "il quadro programmatico porta il FSN al 5,87%" era imprecisa. Il DPFP non fissa un FSN programmatico e tiene la spesa sanitaria della PA stabile al 6,3% del PIL. Il calo del FSN/PIL (6,14% → 5,98% nel 2028) è un calcolo sul FSN di legge e sul PIL tendenziale. Il dato nuovo che conta per le coperture è il profilo: +3,4 mld nel 2027, poi meno di 1 mld l'anno nel 2028-2029 (+0,9 mld, poi circa +1,0 mld se il 2029 è confermato). C2, C3 e C5 indicano tutte come copertura una "quota dell'incremento annuo del FSN": dal 2028 quel margine non basta per tutte e tre. La copertura va considerata fragile e da negoziare nel piano di medio termine. Nessun punteggio cambia, perché i punteggi valutano gli effetti delle misure e la fragilità era già segnalata nella sezione D.
2. **C5 (salute mentale al 5%): costo corretto da 2,3 a 2,9–3,4 mld/anno.** Portare la quota dal 2,7–3% al 5% di un FSN da 146,3 mld costa 2–2,3 punti, cioè 2,9–3,4 mld. La stima del Collegio DSM (2,3 mld) sottostima il fabbisogno rispetto al FSN attuale. La crescita di 0,4 punti l'anno vale circa 0,6 mld l'anno e assorbirebbe da sola circa due terzi dell'incremento annuo del FSN nel 2028-2029. **Punteggi invariati; la confidenza dell'orizzonte Medio passa da Media a Bassa**, perché la sostenibilità finanziaria del percorso è meno certa.
3. **C4 (budget di cura).** (a) La Prestazione universale non scade il 31/12/2026: il DDL bilancio 2027 la proroga al 31/12/2027. Ho riscritto la motivazione del punteggio Breve (+1, invariato): la misura serve ancora, ma come soluzione strutturale a una proroga di un solo anno, non per coprire un vuoto immediato. (b) Il "voucher anziani 1,6 mld" è una Carta valore una tantum per il solo 2027 (1.645 mln). Può finanziare l'avvio, non la spesa a regime, quindi la copertura strutturale di C4 poggia di più sull'emersione del lavoro di cura e sul riordino delle altre misure. Punteggi invariati.
4. **C6 (accise salute e budget del farmaco).** Il gettito della sugar tax è ora quantificato su fonte ufficiale (circa 340 mln/anno, coerente con "qualche centinaio di milioni"). La tassa viene rinviata ancora, al 1/7/2027. Lo sforamento degli acquisti diretti è 4,77 mld. Il DDL 2027 va in parte nella direzione di C6 (tetto acquisti diretti +0,2% dal 2028) ma introduce anche una riduzione del payback legata agli investimenti (160 mln/anno), che complica il superamento del payback. La prevenzione vale il 4,5% della spesa corrente (8,6 mld): la riallocazione proposta di 1–1,5 mld la aumenterebbe del 12–18%. Punteggi invariati.
5. **C1 e B3.** Il confronto con i 300 mln del DDL 2027 per prestazioni aggiuntive conferma che 0,5–1 mld è un ordine di grandezza plausibile per una garanzia generalizzata (stima GovernAI). La correzione sul personale medico (sopra la media OCSE, non "in linea") rafforza la diagnosi di C2: lo squilibrio è sul personale infermieristico e sulla distribuzione del personale medico, non sul numero totale. Punteggi invariati.
6. **Out-of-pocket.** Con i dati SHA rivisti la quota è 23,0% nel 2024 e 22,3% nel 2025 (42,4 mld). Il livello è più alto di quello indicato, ma la diagnosi non cambia. Nessun effetto su punteggi o costi.

## Note tecniche

- `fonti.py` funziona per tutte le chiamate usate; nessun bug da aggirare. L'API Eurostat non espone `hlth_rs_physage` (404), quindi l'età del personale medico resta ❓.
- Il PDF AIFA consuntivo scaricato (dati NSIS al 14/5/2026) riporta 24.950,2 mln di spesa totale e 4.767,1 mln di disavanzo. Il comunicato AIFA riportava 24.965,3 e 4.702,2 mln, con una diversa base di calcolo (incluso o escluso il fondo innovativi e i gas medicinali). Nel dossier ho usato il PDF.
- Nei flussi ISTAT BES territoriali (`DF_BES_TERRIT_1` e `_12`) non c'è l'indicatore di rinuncia alle prestazioni. Il dato Sardegna resta ❓.
- Le fonti che richiedono accesso riservato non sono state consultate (nessuna incontrata).
