# GovernAI — Confronto internazionale: chi fa meglio e cosa possiamo trasferire

*Agente "confronto internazionale e fisco", 8 novembre 2026. Serie Eurostat scaricate con `dati/script/bm_benchmark.py` e salvate in `dati/serie/bm_*.csv` (registro `dati/serie/_registro_bm.csv`). Le cifre non Eurostat hanno fonte e link riga per riga. "Stima GovernAI" indica una valutazione propria; "da verificare" indica un dato trovato solo in fonti secondarie. Documento di consulenza: non sostituisce le valutazioni d'impatto degli uffici tecnici.*

## Come leggere il confronto

Per ognuna delle 9 aree di governo:
- un **indicatore chiave** misurabile e ufficiale;
- i **2-3 Paesi UE** con i risultati migliori, e la **politica** che spiega gran parte del loro risultato;
- il **dato dell'Italia**;
- che cosa è **trasferibile** e che cosa no.

**Tre avvertenze.**
1. **Il primo della classifica non è sempre il modello giusto.** Ad esempio, Lussemburgo e Malta hanno risultati legati alla dimensione o alla posizione geografica. In quei casi indichiamo il Paese più comparabile.
2. **Un indicatore non spiega un sistema.** La "politica che lo spiega" è quella che la letteratura e le istituzioni del Paese indicano come decisiva, non l'unica causa.
3. **Trasferibilità.** Una politica si trasferisce se dipende da regole che l'Italia può cambiare: legge, organizzazione, incentivi. Non si trasferisce se dipende da dotazioni naturali, dimensione, storia istituzionale o livelli di fiducia che non si creano per legge.

## Quadro di sintesi

| Area | Indicatore (fonte, anno) | Migliori | Italia | Posizione Italia |
|---|---|---|---|---|
| 01 Economia | Divario di adempimento IVA, % dell'IVA teorica (Commissione UE, 2023) | Austria ~1%, Finlandia ~3% | ~15% (media UE 9,5%) | nel gruppo con i divari più alti |
| 02 Lavoro | Tasso di occupazione 20-64 anni, % (Eurostat lfsi_emp_a, 2025) | Paesi Bassi 83,4; Svezia 81,8 (donne: Estonia 81,4; Svezia 79,8) | 67,6 (donne 58,0) | 27ª su 27 |
| 03 Ambiente | Quota di rinnovabili nel consumo finale di energia, % (Eurostat nrg_ind_ren, 2025 provv.) | Svezia 65,4; Finlandia 53,0; Danimarca 48,2 | 20,5 (UE 26,2) | 19ª su 27 |
| 04 Casa | Inquilini a canone di mercato che spendono >40% del reddito per la casa, % (Eurostat ilc_lvho07c, 2025) | Finlandia 12,3; Germania 13,2; Austria 14,5 | 22,3 (UE 18,5) | 13ª su 27 |
| 05 Istruzione | Laureati 25-34 anni, % (Eurostat edat_lfse_03, 2025) | Irlanda 66,8; Paesi Bassi 56,1; Francia 55,8 | 31,1 (UE 44,8) | 26ª su 27 |
| 06 Salute | Bisogni di cure non soddisfatti per costo, distanza o attesa, % 16+ (Eurostat hlth_silc_08, 2025) | Rep. Ceca 0,3; Paesi Bassi 0,5; Germania 1,0 | 2,5 (primo quintile 4,4) | 15ª su 27 |
| 07 Giustizia | Durata stimata dei processi civili e commerciali in primo grado, giorni (EU Justice Scoreboard / CEPEJ) | Rep. Ceca 2ª e Lettonia 3ª nello Scoreboard 2026 (dati 2024) | 584 giorni contro una mediana UE di 248 (scheda CEPEJ); 435 giorni nei tribunali nel 2025 (Ministero) | tra i più lenti |
| 08 Esteri | Aiuto pubblico allo sviluppo, % del reddito nazionale lordo (OCSE DAC, 2025 prelim.) | Norvegia 1,03; Svezia 0,85; Danimarca 0,72 | 0,30 (DAC 0,26) | 17ª tra i membri DAC |
| 09 PA digitale | Persone che hanno interagito online con la PA, % 16-74 (Eurostat isoc_ciegi_ac, 2025) | Finlandia 91,4; Danimarca 91,0; Paesi Bassi 84,9 | 43,5 (UE 57,7) | 25ª su 27 |

---

## 01 — Economia: fedeltà fiscale (IVA)

**Indicatore.** Divario di adempimento IVA (*VAT compliance gap*), cioè l'IVA dovuta e non versata in percentuale di quella teorica. È il miglior indicatore confrontabile della lealtà fiscale.
- **Italia:** circa 15% nel 2023, dal 31,5% del 2009, contro una media UE del 9,5% (MEF, *Relazione sull'economia non osservata e sull'evasione fiscale e contributiva 2026*, in `dati/raw/01_mef_relazione_evasione_2026.txt`, su dati della Commissione).
- **Migliori:** Austria (circa 1%) e Finlandia (circa 3%), secondo il rapporto della Commissione UE *VAT Gap in the EU* (dicembre 2025, dati 2023). Fonte secondaria: [Banqup](https://www.banqup.com/resources/blog/eu-vat-gap-report-2025); pagina della Commissione: [VAT gap](https://taxation-customs.ec.europa.eu/taxation/vat/fight-against-vat-fraud/vat-gap_en). Valori per Paese **da verificare** sulle tavole originali.

**Contesto (produttività).** Produttività reale per ora lavorata, indice 2015=100, nel 2025 (Eurostat nama_10_lp_ulc, serie `bm_01_produttivita_ora`):

| Paese | Indice |
|---|---|
| Italia | 100,4 (25ª su 27) |
| UE | 107,4 |
| Danimarca | 113,2 |
| Polonia | 134,6 |

Il dato polacco riflette soprattutto la convergenza di un Paese che parte più in basso, quindi non è un modello trasferibile.

**Politica che spiega il risultato.**
- **Finlandia.** Un registro nazionale dei redditi in tempo reale (*Tulorekisteri*, dal 2019) e una tradizione di alta fiducia verso l'amministrazione fiscale. Il contribuente riceve una dichiarazione precompilata che, se è corretta, non richiede alcuna azione.
- **Austria.** Registratori di cassa con firma elettronica antimanomissione, obbligatori dal 2016-17, controlli mirati sul rischio e un'economia sommersa contenuta.

**Trasferibile.**
- L'Italia ha già fatturazione elettronica e corrispettivi telematici, che sono la parte tecnica.
- Si può trasferire **l'uso dei dati per la prevenzione** (proposta 01-P3) e la **semplificazione per chi è in regola**: il cittadino che vede lo Stato precompilare e rimborsare in fretta è più leale. È la logica della scheda `programma/schede/10_fisco_semplice.md`.

**Non trasferibile a breve.**
- I livelli di fiducia nordici e la bassa quota di lavoro autonomo e micro-imprese, che in Italia è strutturalmente più alta.

---

## 02 — Lavoro: quante persone lavorano

**Indicatore.** Tasso di occupazione 20-64 anni nel 2025 (Eurostat lfsi_emp_a, serie `bm_02_occupazione_20_64`).

| | Totale | Donne |
|---|---|---|
| **Italia** | **67,6% (27ª su 27)** | **58,0% (27ª su 27)** |
| UE | 76,1% | 71,3% |
| Paesi Bassi | 83,4% | 79,6% |
| Svezia | 81,8% | 79,8% |
| Estonia | 81,7% | 81,4% |

Malta, al primo posto (83,6%), ha alzato l'occupazione femminile in un decennio con i nidi gratuiti per i genitori che lavorano (2014), ma la sua dimensione la rende un riferimento più di metodo che di scala.

**Politica che spiega il risultato.**
- **Svezia.** Tassazione individuale, nidi universali con tetto alla retta (*maxtaxa*) e congedo parentale con mesi riservati a ciascun genitore.
- **Paesi Bassi.** Contratti a tempo parziale tutelati e reversibili, e politiche attive con presa in carico rapida.

**Trasferibile.**
- **Nidi come diritto** (LEP finanziato) con tetto alla retta.
- **Congedo di paternità** riservato e ben retribuito.
- **Gradualità del prelievo** sul secondo percettore. L'IRPEF è già individuale, ma le detrazioni per familiari e l'ISEE creano aliquote implicite alte (vedi 10_fisco_semplice, 01-P9).

**Non trasferibile.**
- La cultura olandese del tempo parziale: in Italia il part-time è spesso involontario (ISTAT), quindi va evitato di incentivarlo come tale.
- La spesa nordica per servizi all'infanzia, oltre l'1% del PIL, non è replicabile per intero con il vincolo di bilancio attuale (`dati/verifiche/00_vincolo_bilancio.md`).

---

## 03 — Ambiente ed energia: quanta energia è rinnovabile

**Indicatore.** Quota di rinnovabili nel consumo finale lordo di energia nel 2025, dato provvisorio (Eurostat nrg_ind_ren, serie `bm_03_rinnovabili_quota`).

| Paese | Quota |
|---|---|
| **Italia** | **20,5% (19ª su 27)** |
| UE | 26,2% |
| Svezia | 65,4% |
| Finlandia | 53,0% |
| Danimarca | 48,2% |
| Austria | 44,2% |

**Politica che spiega il risultato.**
- **Svezia.** Carbon tax dal 1991, alzata gradualmente e compensata con tagli ad altre imposte, e teleriscaldamento a biomassa.
- **Danimarca.** Aste per l'eolico con contratti di lungo periodo e pianificazione pubblica delle aree.
- **Finlandia.** Bioenergia forestale.

**Trasferibile.**
- **Prezzo del carbonio sui settori non-ETS** restituito alla cittadinanza: è coerente con la riforma dei sussidi ambientalmente dannosi (fondo SAD del menu coperture).
- **Aste con contratti per differenza**, obbligatori nella UE dal 2027.
- **Aree di accelerazione** con tempi autorizzativi certi (RED III).

**Non trasferibile.**
- La dotazione idroelettrica e forestale dei Paesi nordici.
- Una carbon tax piena introdotta in un solo colpo: l'Italia parte da accise già alte sui carburanti e da prezzi elettrici legati al gas.

---

## 04 — Casa: quanto pesa l'affitto

**Indicatore.** Quota di inquilini a canone di mercato che spendono più del 40% del reddito disponibile per la casa nel 2025 (Eurostat ilc_lvho07c, serie `bm_04_sovraccarico_abitativo`).

| Paese | Quota |
|---|---|
| **Italia** | **22,3%** (19,4% nel 2024) |
| UE | 18,5% |
| Finlandia | 12,3% |
| Germania | 13,2% |
| Austria | 14,5% |

Sull'intera popolazione l'Italia sta meglio della media (5,0%, 7ª su 27) grazie all'alta quota di proprietari: il problema si concentra sugli inquilini.

**Politica che spiega il risultato.**
- **Austria.** Edilizia a "profitto limitato" (*gemeinnützige Bauvereinigungen*): finanziamento pubblico dedicato e stabile, affitti legati ai costi e utili reinvestiti per legge.
- **Finlandia.** Edilizia sociale con prestiti pubblici a lungo termine (ARA) e programma *Housing First* per le persone senza dimora.
- **Germania.** Contributo all'affitto (*Wohngeld*) legato al reddito e aggiornato ogni due anni.

**Trasferibile.**
- **Soggetti gestori a profitto limitato** con vincolo di reinvestimento, e un fondo rotativo di lungo periodo al posto dei bonus una tantum.
- **Contributo affitto strutturale** al posto di fondi intermittenti.
- **Housing First**, già sperimentato in alcune città italiane.

**Non trasferibile a breve.**
- Lo stock pubblico e cooperativo accumulato in un secolo, come a Vienna.
- In Italia l'ERP è sotto il 4% delle abitazioni (stima da verificare): servono decenni, non una legislatura.

---

## 05 — Istruzione: quante persone giovani hanno la laurea

**Indicatore.** Popolazione 25-34 anni con istruzione terziaria nel 2025 (Eurostat edat_lfse_03, serie `bm_05_laureati_25_34`).

| Paese | Quota |
|---|---|
| **Italia** | **31,1% (26ª su 27)** |
| UE | 44,8% (obiettivo UE 2030: 45%) |
| Irlanda | 66,8% |
| Paesi Bassi | 56,1% |
| Francia | 55,8% |

**Politica che spiega il risultato.**
- Una **terziaria professionalizzante di massa**, accanto all'università:
  - Francia: BTS e BUT, in 2-3 anni;
  - Paesi Bassi: HBO, le università di scienze applicate, che rilasciano circa due terzi dei titoli di primo livello;
  - Irlanda: istituti tecnologici, ora università tecnologiche, e tasse universitarie basse.

**Trasferibile.**
- **Scalare gli ITS Academy**: oggi sono una frazione minima degli iscritti alla terziaria (dato da verificare con INDIRE).
- Titoli brevi riconosciuti nel quadro europeo delle qualifiche e passerelle verso la laurea.
- Diritto allo studio esteso ai fuori sede.

**Non trasferibile.**
- Il risultato del Lussemburgo (65,2%), dovuto a lavoratrici e lavoratori laureati di origine straniera.
- In parte quello irlandese, legato agli investimenti esteri ad alta qualificazione.

---

## 06 — Salute: chi rinuncia alle cure

**Indicatore.** Persone di 16 anni e più che dichiarano bisogni di cure mediche non soddisfatti per costo, distanza o liste d'attesa, nel 2025 (Eurostat hlth_silc_08, serie `bm_06_bisogni_cure_insoddisfatti`).

| Paese | Totale | Primo quintile di reddito |
|---|---|---|
| **Italia** | **2,5% (1,8% nel 2023), 15ª su 27** | **4,4%** |
| UE | 2,4% | 3,7% |
| Rep. Ceca | 0,3% | |
| Paesi Bassi | 0,5% | |
| Germania | 1,0% | |

**Politica che spiega il risultato.**
- **Paesi Bassi.** Medico di famiglia come porta d'ingresso obbligata, con studi associati e assistenza fuori orario organizzata, assicurazione obbligatoria con premi regolati e franchigia non applicata alle cure primarie.
- **Germania.** Ampia offerta ambulatoriale e libera scelta dello specialista, senza liste d'attesa centralizzate.
- **Rep. Ceca.** Alta densità di medici e copertura quasi totale delle prestazioni.

**Trasferibile.**
- **Cure primarie in team** con orari estesi.
- **Garanzia di tempo massimo** con diritto a un erogatore alternativo a carico del SSN, che è il modello della garanzia di trattamento danese e norvegese.
- **Agende uniche** pubbliche e private accreditate.

**Non trasferibile.**
- Il modello assicurativo olandese e tedesco: cambierebbe la natura universalistica e fiscale del SSN (art. 32 Cost., L. 833/1978).
- Livelli di spesa per abitante più alti di circa un terzo, non replicabili con il vincolo attuale.

---

## 07 — Giustizia: quanto dura una causa civile

**Indicatore.** Durata stimata (*disposition time*) delle cause civili e commerciali contenziose in primo grado, cioè i giorni necessari a smaltire le pendenze al ritmo attuale.
- **Italia:**
  - 584 giorni, contro una mediana UE di 248 (scheda paese CEPEJ per l'EU Justice Scoreboard, [rm.coe.int](https://rm.coe.int/italy-country-fiche/1680a77898); anno dei dati da verificare);
  - 435 giorni nei tribunali nel 2025, -21,8% rispetto al 2019 (Ministero della Giustizia, *Continuous Monitoring PNRR 2025*, verificato in `dati/verifiche/07_giustizia.md`).
- **Migliori:** nell'EU Justice Scoreboard 2026 (dati 2024), la Repubblica Ceca è **seconda** ([Corte suprema ceca](https://www.nsoud.cz/en/press-releases/detail/podle-srovnavaciho-prehledu-eu-o-soudnictvi-pro-rok-2026-si-ceska-republika-ve-vetsine-ukazatelu-vede-vyborne)) e la Lettonia **terza** ([Consiglio giudiziario lettone](https://www.tieslietupadome.lv/en/article/latvia-ranks-third-among-eu-countries-shortest-length-proceedings-civil-commercial-and-administrative-cases-courts-first-instance)). Il primo Paese e i giorni esatti sono **da verificare** sulla tavola della Commissione.

**Politica che spiega il risultato.**
- **Rep. Ceca.** Ingiunzione di pagamento elettronica per i crediti non contestati e giudici assistiti da funzionari con competenze decisorie delegate.
- **Lettonia.** Fascicolo interamente digitale, riforma della geografia giudiziaria e specializzazione dei tribunali.

**Trasferibile.**
- **Ufficio per il processo stabile**, non a termine PNRR.
- **Delega ai funzionari** delle attività non decisorie.
- Procedimento monitorio interamente telematico e **pesatura dei carichi** per distribuire le risorse.

**Non trasferibile.**
- La minore litigiosità e il numero più basso di avvocati per abitante di questi Paesi: dipendono da fattori culturali ed economici, e dal costo dell'accesso alla giustizia, che non va alzato a danno di chi ha meno mezzi.

---

## 08 — Esteri: aiuto pubblico allo sviluppo

**Indicatore.** Aiuto pubblico allo sviluppo (APS) in percentuale del reddito nazionale lordo, dati preliminari 2025 (OCSE DAC, aprile 2026, [OCSE](https://read.oecd-ilibrary.org/en/about/news/press-releases/2026/04/international-aid-fell-sharply-in-2025-says-oecd.html)).

| Paese | APS/RNL |
|---|---|
| **Italia** | **0,30%** (`dati/verifiche/08_esteri.md`) |
| Media DAC | 0,26% |
| Norvegia | 1,03% |
| Lussemburgo | 0,99% |
| Svezia | 0,85% |
| Danimarca | 0,72% |

**Politica che spiega il risultato.**
- Un **obiettivo pluriennale vincolante** nel bilancio:
  - Lussemburgo: 1% del RNL, sancito da un impegno di legge;
  - Norvegia e Svezia: storicamente 1%;
  - Danimarca: almeno 0,7%.
- Agenzie con **valutazione indipendente** dei programmi.

**Trasferibile.**
- Un **percorso pluriennale di legge** verso lo 0,7% previsto dalla L. 125/2014, con tappe annuali e valutazione indipendente pubblica.
- Un **tetto alla quota contabilizzata come costi dei rifugiati nel Paese donatore**, che in Italia è il 18,5% dell'APS nel 2025.

**Non trasferibile.**
- Il margine fiscale norvegese, dovuto al fondo petrolifero.
- La Svezia stessa ha ridotto l'obiettivo dal 2023: anche nei Paesi modello l'impegno è politico, non irreversibile.

---

## 09 — PA digitale: quante persone usano i servizi online

**Indicatore.** Persone di 16-74 anni che hanno interagito online con la PA negli ultimi 12 mesi, nel 2025 (Eurostat isoc_ciegi_ac, I_IUGOV1, serie `bm_09_egov_uso`).

| Paese | Quota |
|---|---|
| **Italia** | **43,5% (25ª su 27)** |
| UE | 57,7% |
| Finlandia | 91,4% |
| Danimarca | 91,0% |
| Paesi Bassi | 84,9% |

**Politica che spiega il risultato.**
- **Danimarca.** "Digitale per default": casella postale digitale obbligatoria per tutta la popolazione dal 2014 (*Digital Post*), con esenzione su richiesta per chi non può usarla, e una sola identità digitale (MitID).
- **Finlandia.** Portale unico Suomi.fi e principio "una sola volta" sui dati.
- **Paesi Bassi.** DigiD unica per tutti i servizi.

**Trasferibile.**
- **Domicilio digitale come canale ordinario**: INAD e App IO esistono già. Va accompagnato da un **canale assistito** (sportelli, CAF, uffici postali) per chi non è digitale, come l'esenzione danese.
- **Un solo accesso e un solo fascicolo.**
- **Servizi proattivi**, in cui lo Stato agisce senza domanda del cittadino: la dichiarazione dei redditi automatica (01-P7) ne è l'esempio più grande.

**Non trasferibile a breve.**
- Le competenze digitali nordiche: in Italia ha competenze digitali di base il 46% circa della popolazione (serie `09_competenze_digitali_base`), contro oltre il 70% dei Paesi nordici (dato da verificare).
- L'alta fiducia nelle istituzioni, che rende accettabile l'obbligo digitale.

---

## Cosa insegna il confronto, trasversalmente

1. **I Paesi migliori fanno meno cose, ma stabili.** Obiettivi pluriennali per legge (APS, edilizia austriaca, carbon tax svedese) e strumenti che durano più di una legislatura. È il valore FID della Carta.
2. **Lo Stato che agisce senza domanda.** Dichiarazione automatica, servizi proattivi, garanzia di tempo massimo in sanità: il cittadino riceve il diritto senza doverlo chiedere. È la leva più trasferibile e la meno costosa, perché i dati in Italia esistono già.
3. **Gradualità e compensazione.** Le riforme di prezzo che hanno funzionato (Svezia, Danimarca) sono state introdotte in 10-20 anni, con restituzione del gettito. Le riforme copiate "in un colpo" falliscono sul consenso.
4. **Dove l'Italia è ultima (occupazione, laureati, PA digitale), il divario è di sistema.** Nessuna singola misura lo chiude: servono pacchetti coerenti e valutati.

## Limiti

- I dati 2025 di Eurostat sono in parte provvisori (flag `p` nelle serie).
- Per giustizia e IVA i valori dei Paesi migliori vengono da fonti secondarie o da comunicati nazionali: vanno verificati sulle tavole originali della Commissione prima di citarli.
- Le "politiche che spiegano" sono una sintesi qualitativa: non è stata fatta una valutazione d'impatto controfattuale.

Ricerche web usate per tutto il lavoro (benchmark e fisco): 15, più 2 letture di pagine.
