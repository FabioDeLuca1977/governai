# Nuove coperture da sussidi dannosi e incentivi alle imprese

*Bozza scritta da un agente AI il 15 novembre 2026; da valutare con il panel e da approvare; non rivista da una persona. Le righe sono in `benchmark/bozza_risparmi_sad_incentivi.csv`, con la stessa intestazione di `programma/coperture_menu.csv`. Le colonne dei valori (RIS..CIT) sono vuote: le compila il panel.*

## In breve

- **Sei proposte nuove**, per **0,17-0,39 mld l'anno a regime** (2029-2030). Sono tre sui sussidi ambientali (SAD20-SAD22) e tre sugli incentivi alle imprese (RA20-RA22).
- **I sussidi dannosi nazionali ancora liberi sono pochi.** SAD01-SAD14 usano già quasi tutte le voci grandi del Catalogo che si possono riformare a livello nazionale. Le voci rimaste sono piccole, oppure toccano beni essenziali (luce e acqua di casa), oppure si decidono a livello UE.
- **La voce nuova più grande è la compensazione dei costi indiretti ETS (SAD22, 0,08-0,15 mld).** Le risorse liberate sono proventi delle aste di CO2, quindi la legge europea le vincola a usi per il clima. Per questo la bozza le destina a due misure oggi escluse dal programma: **treni pendolari** ed **efficienza energetica delle case di chi ha meno**.
- **Gli incentivi alle imprese danno poco di nuovo.** Il grosso è già in RA04, RA14 e RA15. Le tre righe RA usano criteri diversi da quelli: linee che non spendono, garanzie date senza effetto aggiuntivo e compensi ai gestori. Ogni riga dichiara la parte netta "oltre RA04/RA14".
- **Con questa bozza il buco di circa 5,3 mld resta quasi intero.** Le coperture trovate qui ne valgono il 3-7%.

## Metodo

1. Ho letto i file del progetto: `programma/coperture_menu.csv` (righe SAD01-SAD14, RA04, RA14, RA15), `benchmark/invitalia_incentivi_imprese.md`, `benchmark/logistica_green.md`, `motore/rubrica.md` e `dati/verifiche/03_ambiente.md`.
2. **Catalogo SAD/SAF, VIII edizione** (MASE, trasmesso alle Camere il 14/7/2026), copia locale in `dati/raw/03_catalogo_sad_saf_2026.pdf`. Ho preso dalla Tabella 10 tutte le voci con qualifica SAD e ho tolto quelle già usate nel menu. Ho escluso anche le voci superate, come EN.SI.24: le accise su benzina e gasolio sono allineate dal 1/1/2026 (L. 199/2025).
3. **Rendiconto 2025 per capitolo** (OpenBDAP-RGS, `dati/raw/00b_openbdap_rendiconto_2025_spese_capitolo.csv`). Ho ordinato i capitoli di aiuto alle imprese (trasferimenti, contributi agli investimenti, attività finanziarie) per residui e per rapporto tra pagato e stanziato. Così ho trovato le linee che non spendono.
4. **Relazioni al DDL di bilancio 2027** (A.C. 3174). Le ho usate per capire che cosa è già nei tendenziali: per esempio il Fondo SIMEST 394/81 non viene rifinanziato e la ZES unica è rifinanziata solo per il 2027 e il 2028.
5. **Valutazioni d'impatto.** Banca d'Italia, Temi di discussione n. 1265 (Fondo di garanzia PMI), e le fonti già raccolte nel benchmark Invitalia.
6. **Regola prudente.** Conta solo un taglio di spesa che si sarebbe fatta davvero dal 2028 al 2033. Non contano: residui già impegnati, autorizzazioni che scadono prima del 2028, operazioni finanziarie (prestiti e conferimenti) e fondi UE.

## Le proposte

| ID | In una riga | mld/anno | A regime | Livello | Fonte principale |
|---|---|---|---|---|---|
| **SAD20** | Esenzione IMU sugli immobili nuovi invenduti delle imprese solo per 3 anni; poi IMU ordinaria. Esenti recupero, rigenerazione e immobili affittati | 0,015-0,035 | 2029 | 1 | Catalogo, AL.SI.03 (54,7 mln 2025) |
| **SAD21** | Pacchetto di SAD energetici minori: accisa ridotta per i taxi (con passaggio a un contributo per taxi elettrici), franchigia sulle royalties, canone sul sale, quattro esenzioni minori | 0,008-0,014 | 2030 | 1 | Catalogo, EN.SI.12, EN.SI.26, AL.SI.46, EN.SI.09/10/11/16/23 (15,5 mln quantificati) |
| **SAD22** | Compensazione dei costi indiretti ETS: tetto da 600 a 450 mln; 75% solo a chi investe nella decarbonizzazione, 50% agli altri; risorse a treni pendolari e case | 0,08-0,15 | 2030 | 2 | Catalogo EN.SD.02; rendiconto 2025 cap. 7661 (763,5 mln stanziati); art. 23 c. 8 d.lgs. 47/2020; Dir. (UE) 2023/959 |
| **RA20** | Linee di incentivo fuori dal MIMIT che pagano meno del 20% per due anni: autorizzazioni 2028-2033 ridotte della metà della quota non spesa | 0,03-0,08 | 2029 | 2 | Rendiconto 2025: cap. 2332, 7049, 7254 (Agricoltura); 8515, 7115, 8519 (Turismo) |
| **RA21** | Fondo di garanzia PMI: niente garanzia sui prestiti ordinari alle imprese più sicure (fascia 1), commissione per le medie imprese | 0,03-0,08 | 2029 | 2 | Banca d'Italia TD 1265/2020; rendiconto 2025 cap. 7345 (4,35 mld versati) |
| **RA22** | Compensi dei gestori degli incentivi: tetto dal 2% all'1,5% (1% per le misure automatiche grandi), con premio sui tempi e taglio della dotazione | 0,01-0,03 | 2029 | 1 | d.lgs. 184/2025 art. 7; Corte dei conti 57/2024/CCC e 145/2025 |
| **Totale** | | **0,17-0,39** | | | |

### Note sulle singole proposte

**SAD20, IMU sugli immobili merce.** Fino al 2021 questi immobili pagavano l'IMU allo 0,1%; dal 2022 sono del tutto esenti. Il Catalogo la classifica come SAD perché spinge a costruire su suolo nuovo. Dice anche che l'esenzione andrebbe bene se fosse limitata a recupero e rigenerazione. La proposta segue questa indicazione. Il gettito va ai Comuni: diventa copertura per lo Stato solo se si riduce della stessa somma il Fondo di solidarietà comunale. La riga non si sovrappone a SAD06 e SAD14, che riguardano l'IVA e non l'IMU.

**SAD21, pacchetto di SAD minori.** Vale poco, ma chiude quasi tutte le voci nazionali rimaste, insieme a SAD08. Per i taxi l'agevolazione sul carburante diventa per tre anni un contributo per passare all'elettrico. L'effetto sulle tariffe è di pochi centesimi a corsa e passa dall'aggiornamento tariffario dei Comuni dal 2029.

**SAD22, costi indiretti ETS.** Il Catalogo la classifica come sussidio incerto (SAI), non come SAD, e la stima in 165,5 mln. Nel rendiconto 2025 però il fondo ha 763,5 mln stanziati e 613,5 pagati. La legge gli dà fino a 600 mln l'anno dai proventi d'asta, che valgono circa 2,6 mld. La direttiva ETS chiede di usare tutti i proventi per il clima e di non superare, di norma, il 25% per queste compensazioni. Il rischio principale è la competitività: Germania e Francia compensano fino al 75%. Per questo la bozza lascia il 75% alle imprese che reinvestono almeno metà dell'aiuto nella decarbonizzazione. Va notificata alla Commissione europea.

**RA20, linee che non spendono.** Nel 2025 sei linee di Agricoltura e Turismo avevano circa 0,3 mld di stanziamenti e quasi nessun pagamento. Molte autorizzazioni però finiscono prima del 2028. Per questo la stima prende solo una piccola parte della cifra, e prima serve un censimento con la RGS. Le linee MIMIT restano in RA14.

**RA21, Fondo di garanzia PMI.** Lo studio della Banca d'Italia trova che la garanzia fa ottenere più credito alle imprese di rischio medio-basso. Le imprese "sicure" invece non pagano meno il credito. Il risparmio è piccolo perché su queste imprese la perdita attesa è bassa. Anche così è un risparmio senza costi sociali.

**RA22, compensi dei gestori.** È la misura C del benchmark Invitalia, che non era ancora nel menu. Diventa copertura solo se la stessa norma taglia le autorizzazioni di spesa.

## Chi paga

- **Imprese di costruzione** con case nuove invendute da più di 3 anni, soprattutto su suolo libero (SAD20).
- **Tassisti con auto a combustione** e **concessionari di idrocarburi e di sale** (SAD21).
- **Imprese energivore** che non investono nella decarbonizzazione (SAD22).
- **PMI solide** che oggi ottengono la garanzia anche se le banche già le finanziano (RA21).
- **Gestori pubblici degli incentivi** (RA22).
- **Potenziali beneficiari** di linee che oggi non erogano (RA20).

**Nessuna proposta pesa su famiglie a basso reddito.** Nessuna tocca autotrasporto, agricoltura, isole o montagna oltre quanto già fanno SAD01, SAD02, SAD10 e SAD13. Gli incentivi per l'agricoltura biologica e le misure cofinanziate dall'UE sono esclusi.

**Prezzi e inflazione.** L'effetto sui prezzi al consumo è trascurabile: sono tutte voci piccole o a carico delle imprese. L'unico effetto diretto è sulle tariffe dei taxi, che cambiano dal 2029. Con l'inflazione al 5,6% conviene comunque far partire SAD21 e SAD22 nel 2029, non nel 2028.

## Rischi

- **SAD22.** Rischio di perdere competitività e di spostare produzione all'estero. Dipende dal prezzo della CO2 e dalla notifica UE. Il calo dei volumi messi all'asta può ridurre da solo la quota sopra 1.000 mln, e quindi il risparmio.
- **SAD20.** Il gettito passa dai Comuni e serve la riduzione del Fondo di solidarietà comunale. Le imprese possono reagire affittando a breve o frazionando le unità.
- **RA20 e RA21.** Pressioni dei settori interessati. Effetto in contabilità nazionale da confermare: per RA21 con ISTAT sulle garanzie standardizzate, per RA20 con il censimento delle autorizzazioni.
- **Doppi conteggi.** RA20 e RA22 sono costruite per non toccare il perimetro di RA04 e RA14. Il panel deve controllare che il riordino del d.lgs. 138/2026 non conti di nuovo le stesse somme.

## Cosa non sappiamo

- Quante case nuove restano invendute da più di 3 anni (SAD20).
- Il gettito del canone sul sale e delle voci EN.SI.16 ed EN.SI.23, che il Catalogo non quantifica.
- La spesa effettiva del fondo ETS per anno di competenza dei costi: il Catalogo dice 165,5 mln, il rendiconto 613,5 mln pagati nel 2025.
- Quali autorizzazioni di RA20 durano oltre il 2027.
- Quante garanzie del Fondo PMI vanno alla fascia 1 e quanto si accantona per ogni fascia (dato del gestore, Mediocredito Centrale).
- Quante risorse sono affidate ogni anno ai gestori (RA22).

## Idee scartate

| Idea | Perché scartata |
|---|---|
| Accisa e IVA sulla luce di casa (EN.SI.02, 531 mln; IVA.07, 2.968 mln) | Pesa su chi ha meno e frena l'elettrificazione, cioè va contro l'obiettivo ambientale |
| IVA agevolata sull'acqua pubblica (IVA.06, 312 mln) | Bene essenziale, prelievo regressivo |
| Cherosene e carburanti marittimi internazionali (EN.SI.04a, 1.643 mln; EN.SI.05a, 611 mln) e quote ETS gratuite (EN.SI.43, 3.029 mln) | Si decidono a livello UE o internazionale. SAD11 compensa già in parte |
| Differenza di accisa tra benzina e gasolio (EN.SI.24) | Già superata dal 1/1/2026 (L. 199/2025): contarla sarebbe un doppione |
| Carburanti delle Forze armate (EN.SI.17, 24 mln) | Lo Stato paga sé stesso: nessun effetto netto |
| Bollo dei veicoli storici (TR.SI.09/10, 25 mln) | Il gettito è delle Regioni e la somma è piccola |
| Garanzie SACE all'export di progetti fossili (AL.SD.12) | Non quantificato e senza effetto annuo sul bilancio |
| Fondi rotativi fermi (FRI, Fondo crescita sostenibile rotativo, Fondo nazionale Made in Italy con 900 mln di residui e zero pagamenti nel 2025) | Sono prestiti e conferimenti, cioè operazioni finanziarie che non migliorano l'indebitamento netto. Recuperarli riduce il debito una volta sola, ma non copre spesa annua |
| Fondo SIMEST 394/81 | Non è rifinanziato dopo il 2026 (DDL 2027): il risparmio è già nei tendenziali |
| Credito d'imposta ZES unica (1,4 mld nel 2027, 0,5 mld nel 2028) | Ci sono prove di effetti positivi sugli investimenti nel Mezzogiorno, in parte usa fondi di coesione e solleva una questione territoriale. Il DDL lo sottopone già a valutazione |
| Sconto sui pedaggi per i camion Euro V (risorse per l'autotrasporto) | Il settore è già toccato da SAD01 e SAD13, la quota Euro V non è nota e le risorse finiscono nel 2027 |
| Tax credit per il cinema (cap. 7765, circa 2,0 mld accreditati nel 2025) | Fuori dall'ambito ambientale e imprese MIMIT. Mancano valutazioni controfattuali pubbliche. **Da approfondire** con l'area cultura |
| Contributi all'emittenza locale (130 mln) | C'entra il pluralismo dell'informazione e manca una valutazione d'impatto. Lasciato all'area competente |

## Fonti

- MASE, Catalogo dei sussidi ambientalmente dannosi e favorevoli, VIII ed., 2026: https://www.camera.it/temiap/2026/07/16/OCD177-9133.pdf (Tabelle 1, 2 e 10; schede AL.SI.03, AL.SI.46, EN.SD.02)
- RGS-OpenBDAP, Rendiconto 2025 per capitolo (copia locale `dati/raw/00b_openbdap_rendiconto_2025_spese_capitolo.csv`)
- DDL di bilancio 2027, A.C. 3174, relazioni illustrativa e tecnica (copia locale `dati/raw/00b_ddl_bilancio_2027_AC3174_relazioni.txt`): art. 85 (ZES), art. 89 (contratti di sviluppo turismo), nota sul Fondo 394/81 e sul Fondo di garanzia PMI
- GSE, Rapporto annuale sulle aste di quote di emissione 2025 (copia locale `dati/raw/03_gse_aste_co2_2025.pdf`); d.lgs. 47/2020, art. 23; ricostruzione del riparto in `dati/verifiche/03_ambiente.md`
- Camera dei deputati, dossier sul DL 19/2025 (bollette): https://documenti.camera.it/leg19/dossier/testi/D25019a.htm
- Direttiva (UE) 2023/959, che modifica la direttiva ETS: https://eur-lex.europa.eu/eli/dir/2023/959/oj
- Banca d'Italia, Temi di discussione n. 1265, *Garanzia pubblica per le PMI, accesso al credito e rischiosità di impresa*, 2020: https://www.bancaditalia.it/pubblicazioni/temi-discussione/2020/2020-1265/index.html
- Corte dei conti, delib. 57/2024/CCC: https://www.mimit.gov.it/images/stories/trasparenza/2025/2024_57CCC-DEL.pdf ; det. 145/2025 su Invitalia: https://www.camera.it/temiap/2025/12/29/OCD177-8709.pdf
- D.lgs. 27 novembre 2025, n. 184 (Codice degli incentivi), art. 7 e 21; d.lgs. 26 giugno 2026, n. 138 (riordino)
