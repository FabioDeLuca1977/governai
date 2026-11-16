# Chi paga quanto sullo stesso reddito (regole 2026)

**Domanda.** Su uno stesso reddito lordo prodotto, quanto prende lo Stato da una dipendente, da un pensionato, da una partita IVA, da chi ha una società, da chi ha una holding, da chi vive di rendite o di affitti? E quale gruppo riesce a pagare meno?

**Come.** Un calcolatore deterministico (`calcola.py`) applica le regole di legge in vigore nel 2026. Tutti i numeri fiscali stanno in `parametri.yaml`, ciascuno con la norma e il link. Il codice contiene solo le formule. Si rifà tutto con:

```
python analisi/chi_paga/calcola.py
```

Il comando esegue prima i casi di prova (vedi in fondo), poi scrive `risultati.csv` (83 righe: gruppo, variante, livello di reddito, imposte, contributi, prelievo totale, aliquote effettive, contributi del datore, note con il dettaglio).

**Due misure diverse.**
- **Solo imposte**: IRPEF, addizionali, imposte sostitutive, IRAP, IRES, ritenute. Sono soldi che finanziano lo Stato e non tornano alla persona.
- **Imposte + contributi**: i contributi INPS obbligatori finanziano la *propria* pensione. Pesano sul reddito di oggi, ma danno un diritto domani. Per questo li teniamo separati.

## Tabella principale: aliquota effettiva (% del reddito lordo prodotto)

Ogni cella mostra **solo imposte / imposte + contributi**. Un solo numero vuol dire nessun contributo. "n.a." vuol dire che il regime non si può usare a quel reddito (il forfettario ha un limite di 85.000 euro di ricavi).

| Gruppo | Variante | 25.000 | 50.000 | 100.000 | 300.000 | 1.000.000 |
|---|---|---|---|---|---|---|
| 1 Dipendente privato | RAL (quota del datore a parte) | 9,6 / 18,8 | 25,9 / 35,1 | 33,4 / 43,0 | 41,1 / 45,1 | 44,2 / 45,4 |
| 2 Pensione | pensione lorda | 22,0 | 29,9 | 37,7 | 42,9 | 44,8 |
| 3 Forfettario 15% | professionista, gestione separata | 11,1 / 37,2 | 11,1 / 37,2 | n.a. | n.a. | n.a. |
| 3 Forfettario 15% | commercio, INPS commercianti | 11,3 / 35,8 | n.a. | n.a. | n.a. | n.a. |
| 4 Partita IVA ordinaria | professionista, gestione separata | 15,6 / 41,6 | 20,0 / 46,1 | 25,9 / 51,9 | 38,1 / 48,7 | 43,3 / 46,5 |
| 4 Partita IVA ordinaria | impresa individuale, INPS commercianti | 16,0 / 40,5 | 20,6 / 45,1 | 26,4 / 51,3 | 38,3 / 48,5 | 43,4 / 46,4 |
| 5 Socio di SNC | 2 soci al 50%, INPS commercianti | 22,4 / 46,8 | 24,7 / 49,2 | 30,3 / 55,2 | 42,2 / 52,4 | 47,3 / 50,3 |
| 6 Socio di SRL | tutto in dividendi | 45,7 | 46,2 | 46,4 | 46,6 | 46,6 |
| 6 Socio di SRL | compenso da amministratore + dividendi (il mix che paga meno) | 12,0 / 35,8 | 29,3 / 41,2 | 38,0 / 43,9 | 43,8 / 45,8 | 45,8 / 46,4 |
| 7 SRL tramite holding | utili lasciati nella holding | 27,5 | 28,1 | 28,5 | **28,8** | **28,8** |
| 7 SRL tramite holding | distribuisce dopo 10 anni (valore di oggi, sconto 3%) | 41,5 | 42,0 | 42,3 | 42,5 | 42,5 |
| 7 SRL tramite holding | quote passate agli eredi | 27,5 | 28,1 | 28,5 | **28,8** | **28,8** |
| 8 Rendite finanziarie | azioni, fondi, obbligazioni 26% | 26,0 | 26,0 | 26,0 | 26,0 | 26,0 |
| 8 Rendite finanziarie | titoli di Stato 12,5% | 12,5 | 12,5 | 12,5 | **12,5** | **12,5** |
| 8 Rendite finanziarie | 26% + bollo 0,2% sul capitale (rendimento 4%) | 31,0 | 31,0 | 31,0 | 31,0 | 31,0 |
| 9 Affitti | cedolare secca 21% | 21,0 | 21,0 | 21,0 | **21,0** | **21,0** |
| 9 Affitti | cedolare secca 10% (canone concordato) | 10,0 | 10,0 | 10,0 | **10,0** | **10,0** |
| 9 Affitti | IRPEF ordinaria | 24,2 | 28,1 | 35,5 | 40,6 | 42,5 |

**Quanto pesa il datore di lavoro.** Per la dipendente, il "reddito lordo" è la RAL. L'azienda versa in più il 23,81% per la pensione (IVS), fino al massimale. Se si misura sul costo del lavoro (RAL + quota IVS del datore), imposte e contributi valgono il 34,4% a 25.000 di RAL, il 47,5% a 50.000, il 53,9% a 100.000 e il 46,9% a 1.000.000.

## Cosa dicono i numeri

1. **Sopra i 100.000 euro, chi vive di lavoro paga tra il 41% e il 47% di sole imposte.** Vale per dipendenti, pensionati, professionisti, imprese individuali e soci di SNC. Chi ha redditi di capitale paga molto meno: dal 10% al 29%. A 1.000.000 di euro un dipendente paga il 44,2%, chi tiene gli utili in una holding il 28,8%, chi ha titoli di Stato il 12,5%, chi affitta a canone concordato il 10%.
2. **Il socio di SNC è il gruppo più tassato.** A 1.000.000 paga il 47,3% di imposte, contro il 44,2% del dipendente. Paga l'IRPEF piena, i contributi sull'intero reddito d'impresa fino al massimale e l'IRAP della società. Le persone fisiche invece non pagano l'IRAP dal 2022. Il professionista ordinario a 100.000 euro arriva al 51,9% tra imposte e contributi. La frase "le partite IVA normali e le SNC pagano già tanto" è confermata dai conti.
3. **La holding è il canale più forte per chi ha molto.** Gli utili restano nella holding con il 28,8% in tutto: IRAP 3,9%, IRES 24% e circa lo 0,9% sul dividendo che arriva alla holding (il 5% imponibile al 24%, art. 89 TUIR). La stessa SRL che distribuisce tutto alla persona paga il 46,6%. Se la holding passa agli eredi, l'imposta personale del 26% non arriva mai. Grazie al valore di successione, gli eredi possono vendere o liquidare senza plusvalenze, e il passaggio di quote di controllo ai figli è esente dall'imposta di successione. Il passaggio è quindi permanente.
4. **Le rendite pagano aliquote fisse, che non salgono con il reddito.** La cedolare secca e il 26% sulle rendite finanziarie restano uguali a 25.000 e a 1.000.000 di euro. Già a 25.000 euro di affitti la cedolare conviene: 21% contro il 24,2% dell'IRPEF. Il vantaggio cresce con il reddito: 19,6 punti a 300.000 e 21,5 punti a 1.000.000.

## I canali che fanno pagare meno ai più ricchi (quanto valgono, in punti di imposta)

Confronto a 300.000 e 1.000.000 di euro, rispetto a quanto pagherebbe lo stesso reddito tassato come lavoro dipendente (41,1% e 44,2% di sole imposte).

| Canale | Come funziona | 300.000 | 1.000.000 |
|---|---|---|---|
| Holding che trattiene gli utili (PEX, art. 87 e 89 TUIR) | Sui dividendi alla holding l'imposta è circa dell'1,2%; il 26% personale si rinvia | −12,3 punti (28,8%) | −15,4 punti (28,8%) |
| … rispetto alla stessa SRL senza holding | Il rinvio vale 17,9 punti; con il passaggio agli eredi diventa definitivo | −17,9 | −17,9 |
| Rinvio di 10 anni con la holding | Il 26% pagato fra 10 anni vale oggi il 26%/1,03^10 | −4,1 rispetto alla SRL che distribuisce subito | −4,1 |
| Cedolare secca 21% sugli affitti | Aliquota fissa invece degli scaglioni IRPEF | −19,6 rispetto all'IRPEF sugli affitti | −21,5 |
| Cedolare 10% a canone concordato | Come sopra, nei Comuni ad alta tensione abitativa | −30,6 | −32,5 |
| Rendite finanziarie al 26% | Aliquota fissa | −15,1 rispetto al dipendente | −18,2 |
| Titoli di Stato al 12,5% | Aliquota agevolata | −28,6 | −31,7 |
| Massimale contributivo (122.295 € nel 2026) | Oltre il massimale non si versano contributi | Contributi del dipendente: 4,0% del reddito (9,6% a 100.000) | 1,2% |
| SRL con compenso da amministratore (17.000 €) + dividendi | Il compenso basso usa le aliquote IRPEF basse, il resto va all'IRES | −0,8 punti di prelievo totale rispetto a "tutto dividendi" | −0,3 |

E per i redditi medi:
- **Forfettario**: a 50.000 euro paga l'11,1% di imposte contro il 20,0% della partita IVA ordinaria (−8,9 punti). Il regime vale solo fino a 85.000 euro di ricavi, quindi non è un canale dei redditi alti. I contributi restano alti (26%).
- **SRL con compenso + dividendi**: a 100.000 euro il totale è il 43,9%, contro il 51,9% del professionista ordinario (−8 punti, soprattutto contributi più bassi).

Altri canali non calcolati qui, ma da tenere presenti: la plusvalenza sulla vendita della società operativa, che tramite holding è esente al 95% (PEX, circa 1,2% contro 26% per la persona); le spese personali messe a carico della società (auto, immobili); i prestiti dei soci; la residenza all'estero; il regime per i nuovi residenti (flat tax).

## Limiti (da leggere prima di usare i numeri)

- **I contributi danno una pensione, le imposte no.** Chi versa il 26% alla gestione separata matura una pensione contributiva. Chi passa dalla holding non versa contributi e non matura nulla. Un'aliquota "totale" più alta non vuol dire automaticamente pagare di più a fondo perduto.
- **Il reddito lordo non è lo stesso tipo di reddito.** 1.000.000 di rendite richiede un patrimonio di circa 25 milioni. Un dipendente con la stessa RAL non ha quel patrimonio. Il confronto riguarda il prelievo sul flusso di reddito, non sul patrimonio. L'IMU sugli immobili e il bollo sui conti (mostrato in una sola variante) tassano il patrimonio.
- **Le ipotesi semplificano** (tutte sono in `parametri.yaml` e si possono cambiare):
  - addizionali al 1,73% regionale e allo 0,8% comunale, senza fasce;
  - persone assicurate dopo il 1995 (massimale contributivo per tutti);
  - nessun onere detraibile né familiare a carico;
  - SRL e SNC senza dipendenti e senza debiti;
  - nel forfettario i costi veri sono pari alla quota forfettaria;
  - socio di SRL non iscritto alla gestione commercianti;
  - costi della holding non considerati.
- **Punti incerti**:
  - la detrazione dell'art. 13 c. 5 per il socio di SNC (non applicata; vale al massimo circa 600 euro a 25.000);
  - la tassazione della liquidazione della holding in capo agli eredi (art. 47 c. 7 TUIR: lettura prevalente, ma non pacifica);
  - la sterilizzazione dei 440 euro oltre 200.000 euro di reddito (non opera senza oneri detraibili; parametro `applica_senza_oneri`).
- **Cosa non è un calcolo di legge**: il "mix che paga meno" della SRL è una ricerca numerica del compenso (a passi di 1.000 euro) che riduce al minimo imposte + contributi. Non è un consiglio fiscale.

## Controlli dei conti (casi di prova in `calcola.py`)

| Caso | Conto a mano (regole 2026) | Calcolatore |
|---|---|---|
| Dipendente, RAL 25.000 | INPS 9,19% = 2.297,50; imponibile 22.702,50; IRPEF lorda 23% = 5.221,58; detrazione art. 13 = 1.910 + 1.190 × (28.000 − 22.702,50)/13.000 = 2.394,95; ulteriore detrazione (L. 207/2024) 1.000; **IRPEF netta 1.826,63**; addizionali 574,37 | uguale |
| Taglio della legge di bilancio 2026 | 2 punti su 22.000 euro = 440 euro al massimo | uguale |
| Commercianti sul minimale | contributo fisso di 4.611,64 € (circolare INPS 14/2026) | uguale |
| SRL, 1.000.000, tutto in dividendi | 3,9% + 24% + 26% × 72,1% = 46,65% | uguale |
| Continuità delle detrazioni alle soglie (15.000, 28.000, 8.500, 55.000) | importi di legge | uguale |

Confronto esterno: per la RAL di 25.000 euro un simulatore indipendente ([stipendionettocalcolatore.it](https://stipendionettocalcolatore.it/ral-25000-stipendio-netto-2026/)) indica un'IRPEF netta di 1.827 euro, uguale al nostro conto. Non è stato possibile interrogare in automatico un simulatore ufficiale dell'Agenzia delle entrate: il conto a mano sopra segue le formule dell'art. 13 TUIR.

## Fonti principali

- L. 30/12/2025 n. 199 (legge di bilancio 2026), art. 1 c. 3-4: [Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199); scheda [ecnews](https://www.ecnews.it/lavoro/news-del-giorno/legge-bilancio-2026-revisione-aliquote-irpef/)
- TUIR (DPR 917/1986), art. 11, 13, 37, 47, 77, 87, 89: [Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917)
- L. 207/2024, art. 1 c. 4-9 (cuneo fiscale): [Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207)
- INPS, circolare n. 8/2026 (gestione separata, massimale 122.295 €): [informazionefiscale](https://www.informazionefiscale.it/Aliquote-gestione-separata-INPS-2026-importo-contributi); circolare n. 14/2026 (artigiani e commercianti): [ecnews](https://www.ecnews.it/lavoro/imposte-contributi-e-premi/contributi-e-premi/artigiani-commercianti-valori-contributivi-anno-2026/)
- d.lgs. 446/1997 (IRAP) e L. 234/2021 art. 1 c. 8 (esenzione IRAP delle persone fisiche); L. 190/2014 (forfettario); d.lgs. 23/2011 (cedolare secca); DL 66/2014 (26% e 12,5%); d.lgs. 346/1990 art. 3 c. 4-ter (successioni). Tutti i link sono in `parametri.yaml`.
