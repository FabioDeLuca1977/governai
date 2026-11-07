# Verifica dati — Dossier 03 (Ambiente, Energia, Agricoltura, Protezione civile)

*Agente verificatore GovernAI, 7 novembre 2026. Script: `dati/script/03_ambiente.py` (serie `dati/serie/03_*.csv`, registro `_registro_03.csv`, PDF ufficiali in `dati/raw/03_*.pdf`).*

**Sintesi**: 38 cifre controllate: **26 ✅ confermate**, **3 ✏️ corrette**, **9 ❓ non verificabili** su fonte primaria.

## Tabella di verifica

| # | Dato | Valore nel dossier | Valore verificato | Fonte primaria (ente, documento/serie, anno, URL) | Esito |
|---|---|---|---|---|---|
| 1 | PNRR Missione 2, dotazione | 55–60 mld € (stima) | 56,8 mld € (feb 2026); 57,8 mld € (nov 2025) | Governo, Stato di avanzamento PNRR feb 2026 / Nota aggiornamento nov 2025 (allegati ripubblicati da CGIL: files.cgil.it). Da riconfermare su italiadomani.gov.it | ✅ (affinato a ≈57) |
| 2 | PAC Italia 2023–27 | 35–37 mld € (stima) | quasi 37 mld €, di cui ≈28 UE | Camera dei deputati, Temi "Attuazione della PAC 2023-2027" — https://temi.camera.it/leg19/post/attuazione-della-pac-2023-2027.html | ✅ |
| 3 | Proventi aste ETS | 2–3 mld €/anno (stima) | 2.598,6 mln € (2025); 2.610,9 mln € (2024) | GSE, Rapporto annuale aste CO2 2025 — URL in script; serie `03_ets_proventi` | ✅ |
| 4 | Avvio ETS2 | 2027–2028 | 2028 (accordo provvisorio UE dic. 2025, rinvio di un anno) | GSE, Rapporto annuale aste CO2 2025 | ✅ (precisato) |
| 5 | GHG totali 2024 | ≈363 Mt | 363,5 MtCO₂eq (senza LULUCF) | Eurostat env_air_gge (inventario ISPRA/UNFCCC 2026), `03_ghg_settori` | ✅ |
| 6 | Variazione GHG su 1990 | -30,2% | -30,2% | idem | ✅ |
| 7 | Settore energetico su 1990 | -53,6% | -53,6% (CRF 1A1 industrie energetiche) | idem | ✅ |
| 8 | Quota trasporti | ≈31% | 31,2% | idem (CRF 1A3) | ✅ |
| 9 | Trasporti su 1990 | oltre +10% | +10,9% | idem | ✅ |
| 10 | Stima emissioni 2025 | +0,3% | +0,3% (e -1,5% stimato per 2026) | ISPRA, Stime trimestrali 2025.4 (apr. 2026) e comunicato ott. 2026 — https://www.isprambiente.gov.it/files2026/area-stampa/comunicati-stampa/comunicato-emissioni-2026.pdf | ✅ |
| 11 | Obiettivo non-ETS 2030 mancato | non raggiunto | 200,8 Mt contro obiettivo 193,9 Mt, anche con misure PNIEC (scarto 6,9 Mt) | ISPRA, scenari emissivi 2026, letto via QualEnergia (rapporto ISPRA non scaricato) | ✅ (fonte secondaria) |
| 12 | Costo acquisto quote Effort Sharing | stima, da verificare | nessuna stima ufficiale trovata | — | ❓ |
| 13 | PUN medio 2025 | ≈115 €/MWh | 115,32 €/MWh | GME, Newsletter gennaio 2026 — `03_pun_gme` | ✅ |
| 14 | Variazione PUN | +6–7% | +6,3% (108,52 → 115,32) | idem | ✅ |
| 15 | Prezzo Spagna 2025 | ≈65 €/MWh | non estratto (tabella GME illeggibile) | OMIE / GME | ❓ |
| 16 | Domanda elettrica 2025 | ≈311 TWh | 311,3 TWh | Terna, Rapporto mensile dicembre 2025 — `03_terna_2025` | ✅ |
| 17 | Quota FER sulla domanda | ≈41% | 41,1% | idem | ✅ |
| 18 | Produzione FER | ≈128 TWh | 128,0 TWh | idem | ✅ |
| 19 | Traiettoria PNIEC FER 2025 | 47,4% | non verificata sul PNIEC | QualEnergia | ❓ |
| 20 | Nuova capacità FER 2025 | ≈7,2 GW | 7.191 MW (FV 6.437, eolico 608) | Terna, Rapporto mensile dic. 2025 | ✅ |
| 21 | Fabbisogno annuo 2030 | ≈9 GW/anno | ≈9 GW/anno | Stima Terna citata in ARERA, Presentazione consultazione Piano di sviluppo 2025 | ✅ |
| 22 | Perdite idriche % | 42,4% "dato 2020" | **42,4% è il dato 2022**; nel 2020 era 42,2% | ISTAT 12_60_DF_DCCV_CONSACQUA_1 (Censimento acque uso civile) — `03_acqua_perdite` | ✏️ (anno) |
| 23 | Volume perso | ≈3,4 mld m³ | 3,39 mld m³ (2022) | idem | ✅ |
| 24 | Basilicata e Abruzzo oltre 60% | >60% | 65,5% e 62,5% (2022) | idem | ✅ |
| 25 | Uso irriguo | ≈20 mld m³/anno | fonte primaria non trovata | ANBI (stampa) | ❓ |
| 26 | Siccità sui terreni coltivati | quota rilevante | — | Ambrosetti (non primaria) | ❓ |
| 27 | Comuni a rischio | 94,5% (7.463) | 94,5% (7.463) | ISPRA, Rapporto dissesto ed. 2024, executive summary | ✅ |
| 28 | Abitanti a rischio frane | 5,7 mln, 1,28 mln in P3–P4 | 5,7 mln; 1,28 mln (2,2% della popolazione) | idem | ✅ |
| 29 | Danni frane/alluvioni | 1–3 mld €/anno | nessun dato pubblico consolidato (come dice il dossier) | — | ❓ |
| 30 | Rapporto prevenzione/riparazione | 1:4 | non verificabile (stima di parte) | Legambiente | ❓ |
| 31 | Consumo di suolo 2025 | +102 km², record | +102 km², record; impermeabilizzato 7,19% (21.644 km²) | ISPRA–SNPA, comunicato 27/10/2026 — https://www.isprambiente.gov.it/files2026/area-stampa/comunicati-stampa/consumo-suolo-cs.pdf | ✅ |
| 32 | Imprese con polizza cat-nat | ≈16% (stampa) | 16% (IVASS, fine aprile 2026, 683 mila polizze); 16,8% (ANIA, 30/6/2026) | IVASS, rilevazione aprile 2026 (letta via Milano Finanza); ANIA | ✅ |
| 33 | Protection gap | 75–80% | non trovato come %; EIOPA dà all'Italia un punteggio di gap tra i più alti in UE, 4/4 sui terremoti | EIOPA, Dashboard protection gap nat-cat | ❓ |
| 34 | SAD 2024 / 2025 | ≈23,8 / ≈22,4 mld € | 23.776,8 / 22.382,3 mln €; fossili (FFS) 20.632,1 mln €; riformabili a livello nazionale 17,1 mld € | MASE, Catalogo SAD/SAF VIII ed., Tab. 2, trasmesso alle Camere il 14/7/2026 — https://www.camera.it/temiap/2026/07/16/OCD177-9133.pdf — `03_sad_catalogo_mase` | ✅ |
| 35 | 10 misure valgono l'88% | 88% | non trovato nel Catalogo (dato OCPI) | Osservatorio CPI 2026 | ❓ (rimane attribuito a OCPI) |
| 36 | Quota agricoltura sul totale GHG | ≈7% | **7,7%** (28,0 Mt) | Eurostat env_air_gge, 2024 | ✏️ |
| 37 | Quota allevamenti nelle emissioni agricole | 76% | **69,4%** (enterica 3A + deiezioni 3B). Il 76% ISPRA usa un perimetro più ampio, non riprodotto | Eurostat env_air_gge, 2024 | ✏️ |
| 38 | Circolarità materiali 2024 | 21,6%, terzo UE (provvisorio) | 21,6%, terzo dopo NL (32,7) e BE (22,7) | Eurostat env_ac_cur — `03_circolarita_materiali` | ✅ |

Altre correzioni nel testo (non contate sopra):
- ✏️ **Proposta 1**: l'allineamento delle accise gasolio/benzina (EN.SI.24) è **già legge** dal 1/1/2026 (L. 199/2025, art. 1, c. 129, come riportato dal Catalogo). Il dossier ora lo cita come misura avviata da completare, senza cambiare la sostanza della proposta.
- ✏️ **Proposta 3, Evidenze**: "gestori del Nord sotto il 25%" sostituito con il dato ISTAT regionale verificabile (Valle d'Aosta 29,8%, Bolzano 28,8%, Emilia-Romagna 29,7%). Il dato sui singoli gestori resta "da verificare".
- Legambiente 48,3 mld € (SAD con perimetro più ampio) non verificato; resta etichettato come stima di parte.

## Impatto sulle proposte

- **Nessun punteggio cambia.** Le correzioni sulla diagnosi sono marginali: anno del dato sulle perdite, quote agricole. Lasciano invariati la gravità dei problemi e la direzione delle proposte.
- **Coperture: cambiamento rilevante.** Il dossier usava i "proventi ETS" come copertura in quattro proposte: P2 0,1–0,2 mld; P3 parte di 0,5–1 mld; P4 parte di 1–1,5 mld; P5 parte di 0,3–0,5 mld. Il massimo cumulato era ben oltre 1 mld €/anno. La verifica mostra che i proventi ETS1 (2,6 mld €) sono **già interamente destinati per legge** (art. 23 d.lgs. 47/2020), e che la quota riprogrammabile da MASE vale circa 0,65 mld €. Una parte è già impegnata: per esempio 100 mln € per il TPL nelle zone in infrazione per la qualità dell'aria (decreto MASE 266/2026) e la copertura parziale del DL 88/2026. Le coperture sono state riscritte:
  - P2 resta coperta dalla quota MASE (importo piccolo);
  - P3 e P5 spostano il peso su coesione e riforma dei SAD agricoli;
  - P4 indica come fonti principali il riordino dei fondi per le emergenze e il contributo sulle polizze. Esplicita che un uso maggiore di ETS richiede di modificare l'art. 23, togliendo risorse al Fondo ammortamento titoli, con effetto equivalente sul deficit (≈0,92 mld €).
- **P1**: la stima di 4–8 mld €/anno è ora etichettata "stima GovernAI". È coerente con i 17,1 mld € di SAD riformabili a livello nazionale, ma il Catalogo avverte che i suoi valori sono teorici "a comportamento invariato". La prima tranche di riforma (gasolio/benzina) è già stata incassata dalla L. 199/2025: il gettito aggiuntivo disponibile per il "dividendo" è quindi inferiore a quanto si poteva leggere prima.
- Tutte le altre stime di costo (P2–P5) sono ora etichettate "stima GovernAI": non sono state trovate stime ufficiali (UPB, MEF, ARERA) per misure equivalenti.

## Coperture condivise

**Sussidi ambientalmente dannosi (SAD)**. Fonte: MASE, Catalogo VIII ed., trasmesso alle Camere il 14/7/2026.

| Voce | 2024 | 2025 |
|---|---|---|
| SAD totali | 23,78 mld € (56 misure) | **22,38 mld €** (54 misure) |
| di cui sussidi alle fonti fossili (FFS) | 21,60 mld € | 20,63 mld € |
| SAD riformabili a livello nazionale | — | **≈17,1 mld €** (Energia 6,3; IVA 9,5) |
| SAF (favorevoli) | 70,53 mld € | 82,50 mld € |

Avvertenze:
- Sono stime teoriche "a normativa vigente e comportamento invariato", non gettito recuperabile.
- La voce EN.SI.24 (gasolio/benzina) è superata dal 2026: chi la usa come copertura la conta due volte.

**Proventi aste ETS1**. Fonti: GSE, Rapporto annuale 2025; art. 23 d.lgs. 47/2020 vigente. Ripartizione: ricostruzione GovernAI.

| Voce 2025 | mln € | Vincolo |
|---|---|---|
| **Totale proventi** | **2.598,6** | 100% a finalità climatiche (Direttiva ETS dal 2023) |
| Fondi transizione energetica e transizione industriale (c. 8: quota oltre 1.000 mln, fino a 600 + 150) | 750,0 | vincolata |
| Fondo ammortamento titoli di Stato (c. 5, 50% del resto) | 924,3 | vincolata (riduzione del debito) |
| Ministeri (c. 4, 50% del resto): MASE 70% | 647,0 | vincolata alle finalità del c. 7; riprogrammabile per DM tra quelle finalità |
| MIMIT 15% / MIT 15% | 138,6 + 138,6 | vincolata (c. 7) |
| **Quota "libera"** | **0** | ogni nuovo uso richiede di riprogrammare la quota ministeriale (≈924 mln, di cui MASE ≈647) o di modificare l'art. 23 |

Note:
- La ricostruzione applica prima il c. 8 e poi il 50/50. È coerente con il DM di riparto dei proventi 2023, che ha assegnato al MASE 1.006 mln € (citato nel decreto MASE 266/2026).
- I proventi sono già nei tendenziali di bilancio.
- I volumi all'asta sono in calo (-0,5% nel 2025 nonostante prezzi più alti, da 64,7 a 73,4 €/t).
- I proventi ETS2 arrivano dal 2028 e vanno in larga parte al Fondo sociale per il clima.

## Note tecniche
- `fonti.py`: nessun bug bloccante. `scarica()` usa un User-Agent personalizzato; lo script aggiunge per prudenza un ripiego con UA da browser (`_scarica_raw`). Il ripiego scatta solo in caso di rifiuto del server.
- Le cifre trascritte dai PDF (SAD, ETS, Terna) vengono ricontrollate automaticamente nel testo del PDF scaricato (`_controlla`): tutti i controlli sono OK.
- Il documento Terna è scaricato da una ripubblicazione su rinnovabili.it: il sito terna.it non è stato raggiunto.
- Ricerche web usate: 14.
