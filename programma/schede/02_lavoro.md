# Schede pronte — Area 02 Lavoro, Welfare, Famiglia, Disabilità

*Agente ministeriale area 02, 7 novembre 2026. Fonti: dossier `ministeri/02_lavoro_welfare_famiglia.md`, verifica `dati/verifiche/02_lavoro.md`, serie `dati/serie/02_*.csv`, registro `registro/fondi.csv`, esito del panel `motore/esito.md`. Varianti in `programma/varianti/02_lavoro.csv`.*

Importi in mld €/anno. Tutti i costi sono **stime GovernAI**: non esistono stime UPB, RGS o INPS sul disegno proposto, salvo dove è indicato. Le coperture usano solo fondi ammessi per la spesa permanente: SPESE_FISCALI, RIORDINO_BONUS, SAD, ACCISE_SALUTE, RIALLOCAZIONE e PENSIONI. Nessuna variante usa DEFICIT, RISPARMI_ATTESI, IVA_EVASIONE, ETS o ALTRO. Rispetto al registro sono cambiate due coperture:
- l'aumento contributivo CUAF (02-C2) non è più usato, perché il suo avanzo non è documentato;
- le sanzioni del collocamento mirato e i risparmi da minore istituzionalizzazione (02-C5) non contano più come copertura, perché sono incerti.

## Quadro delle varianti

| Proposta | Giudizio del panel (Carta 2.0) | PIENA | ESSENZIALE | PILOTA / ZERO | Raccomandazione dell'agente |
|---|---|---|---|---|---|
| 02-C1 Soglia di dignità | dipende dai valori | 0,35 (i=1) | 0,20 (i=0,65) | ZERO 0 (i=0,35) | ESSENZIALE |
| 02-C2 Nido + congedo paterno | **nucleo robusto** | 4,50 (i=1) | **2,00 (i=0,6)** | PILOTA 0,40 (i=0,2) | ESSENZIALE |
| 02-C3 Patto previdenziale | dipende dai valori; **linea rossa** | 0,60 dal 2036 (i=1) | 0,35 dal 2036 (i=0,75) | ZERO 0 (i=0,45) | PIENA riformata o ESSENZIALE |
| 02-C4 Reddito di inclusione | dipende dai valori | 3,00 (i=1) | 1,50 (i=0,55) | PILOTA 0,10 (i=0,05) | ESSENZIALE |
| 02-C5 Progetto di vita | **nucleo robusto** | 1,50 (i=1) | 0,80 (i=0,6) | ZERO 0 (i=0,25) | ESSENZIALE |
| 02-C6 Bilancio generazionale | in coda | 0,40 (i=1) | 0,10 (i=0,5) | ZERO 0 (i=0,3) | ESSENZIALE |

Il pacchetto con tutte le ESSENZIALI costa **4,6 mld/anno a regime** (2030), contro i 10,4 mld delle versioni piene. A questi si aggiungono 0,35 mld dal 2036 per la pensione di garanzia.

---

## 02-C1 — Soglia di dignità: salario minimo contrattuale garantito

**Problema in un dato.** Il **10,2%** degli occupati con 18 anni e più è a rischio di povertà nel 2025, contro l'8,3% nella UE (Eurostat, EU-SILC `ilc_iw01`, serie `02_working_poor`). Le retribuzioni contrattuali orarie reali sono **−10,2%** a settembre 2026 rispetto a gennaio 2021 (elaborazione GovernAI su ISTAT, *Retribuzioni contrattuali* 30/10/2026, ed Eurostat HICP; serie `02_retribuzioni_contrattuali_reali`).

**Soluzione.**
- Per legge, il trattamento economico complessivo (TEC) del CCNL più rappresentativo del settore è la retribuzione «proporzionata e sufficiente» dell'art. 36 Cost., per tutti i dipendenti.
- Una Commissione indipendente propone ogni anno una soglia oraria di garanzia, con i criteri della Direttiva 2022/2041.
- Si rafforzano i controlli INL, così che il pavimento valga davvero.

**Varianti**

| Variante | Contenuto | Costo 2027 / 2028 / 2029 / regime | Intensità | Copertura |
|---|---|---|---|---|
| PIENA | TEC + soglia vincolante + 1.500 ispettori + sgravio temporaneo per le micro-imprese 2028-30 | 0,15 / 0,35 / 0,50 / **0,35** (2031) | 1 | RIALLOCAZIONE 0,15 + SPESE_FISCALI 0,20 |
| **ESSENZIALE** | TEC + soglia dove manca un CCNL rappresentativo o dove il suo minimo è sotto soglia + 750 ispettori | 0,10 / 0,18 / 0,20 / **0,20** (2029) | 0,65 | RIALLOCAZIONE 0,10 + SPESE_FISCALI 0,10 |
| ZERO | Solo certificazione della rappresentatività e TEC come parametro; Commissione consultiva senza oneri | 0 | 0,35 | invarianza |

**Articolato normativo essenziale (variante ESSENZIALE)**

> **Art. 1 (Finalità).** 1. In attuazione degli articoli 36 e 39 della Costituzione e della direttiva (UE) 2022/2041, la presente legge assicura a ogni lavoratore subordinato una retribuzione proporzionata e sufficiente e contrasta l'applicazione di contratti collettivi stipulati da soggetti privi di effettiva rappresentatività.
>
> **Art. 2 (Retribuzione minima di riferimento).** 1. Per ciascun settore, il trattamento economico complessivo previsto dal contratto collettivo nazionale stipulato dalle associazioni comparativamente più rappresentative, individuato ai sensi dell'articolo 3, costituisce la retribuzione proporzionata e sufficiente ai sensi dell'articolo 36 della Costituzione per i lavoratori del settore, qualunque sia il contratto applicato. 2. Il comma 1 si applica anche ai lavoratori impiegati negli appalti pubblici e privati e nei subappalti.
>
> **Art. 3 (Misurazione della rappresentatività).** 1. Il CNEL e l'INPS certificano ogni anno la rappresentatività delle organizzazioni sindacali e datoriali, sulla base dei dati sugli iscritti, sui voti nelle elezioni delle RSU e sui lavoratori a cui si applica ciascun contratto, e pubblicano l'elenco dei contratti di riferimento per codice ATECO. 2. Le modalità sono definite con decreto del Ministro del lavoro, sentite le parti sociali, entro 120 giorni.
>
> **Art. 4 (Commissione per la soglia di garanzia).** 1. È istituita presso il CNEL la Commissione per la retribuzione di garanzia, composta da tre rappresentanti dei lavoratori, tre dei datori di lavoro e tre esperti indipendenti nominati dal Presidente della Repubblica su proposta dei Presidenti delle Camere. 2. Entro il 30 giugno di ogni anno la Commissione propone una soglia oraria lorda di garanzia, motivata sulla base degli indicatori dell'articolo 5 della direttiva (UE) 2022/2041. 3. La soglia si applica ai rapporti di lavoro dei settori privi di un contratto di riferimento e a quelli in cui il TEC del contratto di riferimento è inferiore alla soglia. 4. Il Governo può discostarsi dalla proposta solo con una relazione motivata alle Camere.
>
> **Art. 5 (Controlli).** 1. La dotazione organica dell'Ispettorato nazionale del lavoro è aumentata di 750 unità di personale ispettivo, da assumere nel biennio 2027-2028. 2. L'INPS e l'Agenzia delle entrate trasmettono all'INL, attraverso la piattaforma nazionale dati, le anomalie retributive individuate con controlli incrociati.
>
> **Art. 6 (Copertura finanziaria).** 1. Agli oneri, pari a 0,10 mld nel 2027, 0,18 mld nel 2028 e 0,20 mld annui dal 2029, si provvede per 0,10 mld annui con la riduzione delle autorizzazioni di spesa per incentivi all'assunzione non selettivi iscritti nello stato di previsione del Ministero del lavoro e per la parte restante con le maggiori entrate derivanti dal riordino delle spese fiscali di cui alla legge di bilancio.

**Cronoprogramma**
- **Primi 100 giorni.** Il Consiglio dei ministri approva il ddl. Il Ministero del lavoro (MLPS) convoca le parti sociali sul metodo di misurazione. CNEL e INPS avviano l'incrocio delle banche dati sui contratti, oltre 1.000 CCNL depositati.
- **Entro 12 mesi.** Il Parlamento approva la legge. Il MLPS adotta il DM sulla rappresentatività e nomina la Commissione. L'INL bandisce il concorso per 750 ispettori. Il CNEL pubblica il primo elenco dei contratti di riferimento.
- **Entro fine legislatura.** La Commissione propone tre soglie annuali. Gli ispettori sono tutti in servizio. Dopo 36 mesi UPB e INAPP fanno una valutazione controfattuale su salari e occupazione delle micro-imprese, e il Parlamento decide se passare alla variante PIENA.

**Indicatori**

| KPI | Base | Obiettivo a 3 anni (2029) | Obiettivo a 5 anni (2031) |
|---|---|---|---|
| Occupati 18+ a rischio di povertà | 10,2%, 2025 (Eurostat `ilc_iw01`) | 9,5% | 8,5% (media UE 2025: 8,3%) |
| Retribuzioni contrattuali orarie reali rispetto a gen. 2021 | −10,2%, set. 2026 (ISTAT + HICP, elaborazione GovernAI) | −6% | −3% |
| Dipendenti pagati sotto il contratto di riferimento o la soglia | base da costruire con INPS-CNEL entro il 2027 | −50% rispetto alla base | sotto il 2% |

**Rischi di attuazione e mitigazione**
- *Art. 39 Cost.*: un'estensione erga omnes «diretta» dei contratti è a rischio. La norma usa invece il TEC come parametro dell'art. 36, che è la strada seguita dalla giurisprudenza di legittimità.
- *Sommerso nelle micro-imprese del Sud*: soglia applicata solo dove serve, più controlli incrociati INPS-Entrate. Lo sgravio della PIENA resta come opzione dopo la valutazione.
- *Opposizione di parte delle parti sociali*: la soglia è un pavimento e non sostituisce il contratto. La Commissione ha composizione paritetica.
- *Misurazione contestata*: dati e metodo sono pubblici, con ricorso al giudice amministrativo sull'elenco.

---

## 02-C2 — Tempo e servizi per chi ha figli: nido esigibile e congedo paterno vero

**Problema in un dato.** Nel 2023/24 i posti nei nidi sono **31,6 ogni 100 bambini** di 0-2 anni, ma solo **19,0 al Sud** e 19,5 nelle Isole (ISTAT, *Offerta di nidi*, 2/2/2026). Il 59,5% dei nidi ha liste d'attesa. La fecondità è a **1,14** figli per donna nel 2025 (ISTAT, *Natalità e fecondità 2025*). L'occupazione femminile 20-64 è al **58,0%** nel 2025 (Eurostat `lfsi_emp_a`).

**Soluzione.**
- Il LEP del 33% previsto dalla L. 234/2021 diventa reale dove manca: un fondo finanzia la spesa corrente, cioè gli educatori e non solo gli edifici, negli ambiti sotto soglia, con nido gratuito per le famiglie a basso ISEE.
- Il congedo di paternità sale da 10 giorni a 2 mesi all'80%, non trasferibili.
- Il bonus nido si converte gradualmente in offerta di posti.

**Varianti**

| Variante | Contenuto | Costo 2027 / 2028 / 2029 / regime | Intensità | Copertura |
|---|---|---|---|---|
| PIENA | 33% ovunque e 45% nazionale al 2032; gratuità per ISEE fino a 30.000 €; congedo paterno di 3 mesi all'80% | 1,0 / 2,0 / 3,0 / **4,5** (2031) | 1 | RIORDINO_BONUS 1,5 + SPESE_FISCALI 2,0 + SAD 1,0 |
| **ESSENZIALE** | Spesa corrente solo negli ambiti sotto il 33% (circa 65 mila posti); gratuità per ISEE fino a 25.000 € in quegli ambiti; congedo paterno di 1 mese dal 2028 e 2 mesi dal 2030 | 0,4 / 0,9 / 1,4 / **2,0** (2030) | 0,6 | RIORDINO_BONUS 1,0 + SPESE_FISCALI 1,0 |
| PILOTA | Nidi gratuiti in 30 ambiti sotto il 20%, con valutazione; paternità da 10 a 20 giorni | 0,15 / 0,35 / 0,40 / **0,40** | 0,2 | RIORDINO_BONUS 0,4 |

Come è costruita l'ESSENZIALE (stima GovernAI):
- **Nidi, 0,8 mld.** Servono circa 65 mila posti, a 9 mila € l'uno al netto delle rette. Il conto parte dagli 1,1 mld del Fondo di solidarietà comunale già destinati al LEP dal 2027, non da zero.
- **Congedo, 1,2 mld.** Sono 2/3 della stima di 1,5-2 mld per 3 mesi, riproporzionata dalla relazione tecnica RGS sul congedo paritario. È una stima prudente, perché il ddl bilancio 2027 riserva già al padre un mese di congedo parentale all'80%.
- **CUAF.** L'aumento contributivo **non è usato**: l'avanzo della CUAF non è documentato. Se l'INPS lo certifica, l'agente coperture lo potrà inserire nel menu come nuova misura di entrata.
- **Formazione degli educatori 2027-29.** Va sul FSE+ (COESIONE_2127): è spesa una tantum e non è conteggiata nel costo a regime.

**Articolato normativo essenziale (variante ESSENZIALE)**

> **Art. 1 (Finalità).** 1. Al fine di garantire il diritto dei bambini all'educazione nella prima infanzia, sostenere l'occupazione dei genitori e la condivisione delle responsabilità di cura, la presente legge rende esigibile il livello essenziale delle prestazioni per i servizi educativi 0-2 anni di cui all'articolo 1, comma 172, della legge 30 dicembre 2021, n. 234, e rafforza il congedo di paternità.
>
> **Art. 2 (Fondo per la gestione dei nidi negli ambiti sotto soglia).** 1. È istituito presso il Ministero dell'economia e delle finanze, per il successivo trasferimento ai Comuni, il Fondo per la gestione dei servizi educativi 0-2, con una dotazione di 0,4 mld nel 2027, 0,5 mld nel 2028 e 0,8 mld annui dal 2029. Gli oneri del congedo di cui all'articolo 4 sono valutati in 0,4 mld nel 2028, 0,6 mld nel 2029 e 1,2 mld annui dal 2030. 2. Il Fondo finanzia esclusivamente la spesa corrente, compresa quella di personale, dei Comuni, singoli o associati, il cui bacino ha una copertura inferiore al 33%, in proporzione ai posti aggiuntivi effettivamente attivati. 3. Il riparto è disposto con decreto del Ministro dell'economia, di concerto con i Ministri dell'istruzione e dell'interno, previa intesa in Conferenza unificata. 4. Nei Comuni beneficiari l'accesso è gratuito per i nuclei con ISEE fino a 25.000 euro. Per questi nuclei il contributo di cui all'articolo 1, comma 355, della legge 11 dicembre 2016, n. 232, è sostituito dalla gratuità.
>
> **Art. 3 (Supporto alla gestione).** 1. I Comuni sotto i 5.000 abitanti possono affidare la gestione all'unione di Comuni o all'ambito territoriale sociale. Il supporto tecnico è assicurato dalla struttura di progettazione nazionale per i piccoli enti, prevista dalla proposta 09-C3.
>
> **Art. 4 (Congedo di paternità).** 1. All'articolo 27-bis del decreto legislativo 26 marzo 2001, n. 151, le parole «dieci giorni lavorativi» sono sostituite, dal 1° gennaio 2028, dalle parole «un mese» e, dal 1° gennaio 2030, dalle parole «due mesi». 2. Per il periodo eccedente i dieci giorni l'indennità è pari all'80% della retribuzione. Il congedo non è trasferibile e si perde se non fruito entro i dodici mesi dalla nascita. 3. Il congedo è esteso, con indennità commisurata al reddito, ai lavoratori autonomi e agli iscritti alla Gestione separata. 4. Per le imprese con meno di 15 dipendenti che assumono un sostituto è riconosciuto l'esonero contributivo previsto dall'articolo 4 del medesimo decreto.
>
> **Art. 5 (Monitoraggio).** 1. ISTAT e INPS pubblicano ogni anno la copertura per ambito e la quota di padri che fruiscono del congedo. La relazione al Parlamento del 2029 valuta il passaggio al 45% nazionale e ai tre mesi di congedo.
>
> **Art. 6 (Copertura finanziaria).** 1. Agli oneri, pari a 0,4 mld nel 2027, 0,9 mld nel 2028, 1,4 mld nel 2029 e 2,0 mld annui dal 2030, si provvede:
> - a) per 1,0 mld annui a regime, con la soppressione delle misure di sostegno monetario alla natalità a carattere frammentario individuate nell'allegato (tra cui la decontribuzione per le lavoratrici madri e il contributo per il nido nei Comuni beneficiari), le cui risorse confluiscono nel Fondo di cui all'articolo 2;
> - b) per 1,0 mld annui a regime, con le maggiori entrate derivanti dal riordino delle spese fiscali disposto dalla legge di bilancio.

**Cronoprogramma**
- **Primi 100 giorni.** In legge di bilancio entrano il fondo e la norma sul congedo. ISTAT e Dipartimento per le politiche della famiglia pubblicano l'elenco degli ambiti sotto il 33%. Il Ministero dell'università e della ricerca (MUR) e le Regioni programmano le borse per lauree L-19 su FSE+.
- **Entro 12 mesi.** Intesa in Conferenza unificata sul riparto. I Comuni pubblicano i piani di attivazione, collegati agli edifici PNRR completati. L'INPS adegua le procedure: un mese di paternità dal 1/1/2028.
- **Entro fine legislatura.** Almeno 45 mila posti aggiuntivi attivi entro il 2029, poi circa 65 mila. Due mesi di paternità dal 2030. Valutazione nel 2029 per decidere il passaggio alla PIENA (45% nazionale, 3 mesi).

**Indicatori**

| KPI | Base | Obiettivo a 3 anni (2029) | Obiettivo a 5 anni (2031) |
|---|---|---|---|
| Posti nido ogni 100 bambini 0-2 al Sud | 19,0, a.e. 2023/24 (ISTAT) | 27 | 33 |
| Posti nido ogni 100 bambini 0-2, Italia | 31,6, a.e. 2023/24 (ISTAT) | 36 | 40 |
| Tasso di occupazione femminile 20-64 | 58,0%, 2025 (Eurostat `lfsi_emp_a`) | 60,5% | 62,5% |
| Padri che fruiscono del congedo di paternità | base INPS da acquisire (Osservatorio prestazioni a sostegno della famiglia) | 60% | 75% |

**Rischi di attuazione e mitigazione**
- *Mancano educatori*: borse L-19 vincolate a 3 anni di servizio nei territori sotto soglia, finanziate su FSE+. Il fondo paga solo i posti effettivamente attivati.
- *Comuni senza capacità amministrativa*: gestione associata per ambito e supporto della struttura tecnica nazionale (09-C3).
- *Piccole imprese e assenza dei padri*: esonero contributivo per chi assume un sostituto. Il congedo cresce in due tappe.
- *Aspettative eccessive sulla natalità*: gli obiettivi dichiarati sono la copertura e l'occupazione, non il numero di nascite.
- *Doppio conteggio con il ddl bilancio 2027*: il mese di congedo parentale riservato al padre viene assorbito. La stima va verificata sul testo bollinato.

---

## 02-C3 — Patto previdenziale tra generazioni (ridisegnato per la linea rossa)

**Problema in un dato.** La spesa pensionistica è al **15,2% del PIL** nel 2025 e sale al picco del **17,1%** nel 2041-44 (RGS, *Tendenze di medio-lungo periodo*, aggiornamento 2026). Senza l'aggancio all'aspettativa di vita il picco sarebbe il 18,0%. Il rapporto tra persone con 65 anni e più e persone di 15-64 anni passa dal **39% nel 2025 al 63% nel 2050** (Eurostat, EUROPOP2025 `proj_25ndbi`).

**Soluzione.**
- Si esce prima solo pagando il costo vero della scelta: flessibilità attuariale da 64 anni e aggancio all'aspettativa di vita mantenuto, con tutela dei lavori gravosi.
- I contributivi puri con carriere discontinue hanno una pensione di garanzia.
- Il contributo di equità decennale è **sostituito** da un contributo di solidarietà **triennale** che serve solo ad avviare il fondo. La copertura permanente arriva da una **perequazione differenziata**, già vagliata dalla Corte.

**Come è stata risolta la linea rossa (RIS, valutatore C).** La Corte costituzionale (sent. 234/2020) ha ritenuto legittimo il contributo sulle pensioni elevate della L. 145/2018, ma ne ha dichiarato illegittima la durata quinquennale oltre il triennio. Ha richiesto ragionevolezza, proporzionalità, finalità solidaristica interna al sistema e temporaneità. Il nuovo disegno:
- dura **3 anni (2027-29)**, allineato al bilancio triennale, e non si rinnova automaticamente: una proroga richiede una nuova legge, preceduta da una relazione UPB;
- colpisce **solo la quota di pensione non coperta da contributi**, solo per gli assegni **sopra 10 volte il minimo**, con **aliquote progressive dal 3% al 12%**;
- destina il gettito, stimato in 0,15-0,3 mld/anno, **solo al Fondo per la pensione di garanzia**, cioè a una finalità interna al circuito previdenziale;
- non si somma, negli stessi anni, ad altri tagli sugli stessi assegni;
- non finanzia spesa permanente. La copertura stabile della garanzia viene dalla **perequazione al 50% sulla quota di pensione sopra 6 volte il minimo**, strumento già ritenuto legittimo dalla Corte (sentt. 250/2017 e 234/2020).

La **ESSENZIALE elimina del tutto il contributo**: è la scelta se si vuole azzerare il rischio.

**Varianti**

| Variante | Contenuto | Costo 2027 / 2028 / 2029 / regime | Intensità | Copertura |
|---|---|---|---|---|
| PIENA (riformata) | Flessibilità attuariale; aggancio; contributo triennale verso il Fondo di garanzia; pensione di garanzia a 1,5 volte l'assegno sociale con 20 anni di contributi; adesione automatica alla previdenza complementare | 0,03 / 0,03 / 0,03 / **0,60** (2036) | 1 | PENSIONI 0,60 (perequazione differenziata, nuova misura per il menu) |
| ESSENZIALE | Come la PIENA ma **senza contributo**; garanzia a 1,3 volte l'assegno sociale, con valorizzazione dei periodi di cura | 0,02 / 0,02 / 0,02 / **0,35** (2036) | 0,75 | PENSIONI 0,35 |
| ZERO | Solo regole: flessibilità attuariale, aggancio, gravosi su dati INAIL, adesione automatica, trasparenza UPB; garanzia rinviata | 0 | 0,45 | invarianza |

La flessibilità attuariale anticipa cassa nei primi anni. L'anticipo si finanzia con il fondo flessibilità in uscita del ddl bilancio 2027 (850 mln/anno secondo la stampa, da verificare sul testo), che la nuova norma sostituisce. La chiusura delle «quote» **non** è contata come risparmio, perché il ddl 2027 non le proroga e il risparmio è già nel tendenziale.

**Articolato normativo essenziale (variante PIENA riformata)**

> **Art. 1 (Finalità).** 1. Al fine di assicurare la sostenibilità del sistema pensionistico, l'equità tra generazioni e un trattamento adeguato ai lavoratori con carriere discontinue, ai sensi degli articoli 3, 38 e 81 della Costituzione, la presente legge disciplina l'uscita flessibile, la pensione di garanzia e un contributo temporaneo di solidarietà interno al sistema previdenziale.
>
> **Art. 2 (Uscita flessibile e aggancio all'aspettativa di vita).** 1. Dal 1° gennaio 2028 i lavoratori con almeno 64 anni di età e 25 anni di contributi possono accedere alla pensione con calcolo interamente contributivo o con una riduzione attuariale, determinata con decreto del Ministro del lavoro di concerto con il Ministro dell'economia, che rende neutrale per il bilancio pubblico l'anticipo dell'uscita. 2. È confermato l'adeguamento dei requisiti all'aspettativa di vita di cui all'articolo 12 del decreto-legge 31 maggio 2010, n. 78. 3. Per le attività gravose, individuate ogni tre anni con decreto sulla base dei dati INAIL su infortuni e malattie professionali, l'adeguamento è ridotto della metà. 4. Il fondo per la flessibilità in uscita istituito dalla legge di bilancio 2027 è destinato agli oneri di cassa del comma 1.
>
> **Art. 3 (Contributo temporaneo di solidarietà).** 1. Per gli anni 2027, 2028 e 2029 i trattamenti pensionistici diretti di importo complessivo superiore a 10 volte il trattamento minimo INPS sono soggetti a un contributo di solidarietà, calcolato sulla sola quota di trattamento non corrispondente a contributi versati, determinata dall'INPS mediante ricalcolo contributivo o, se mancano dati, con coefficienti forfettari per anno di decorrenza e gestione. 2. Il contributo è pari al 3% per la quota di importo tra 10 e 15 volte il minimo, al 7% tra 15 e 20 volte e al 12% oltre 20 volte. 3. Sono esclusi i trattamenti di invalidità, le pensioni ai superstiti e le pensioni delle vittime del dovere e del terrorismo. 4. Il contributo non è prorogabile se non con una legge, preceduta da una relazione dell'Ufficio parlamentare di bilancio sui suoi effetti. 5. Le somme affluiscono al Fondo dell'articolo 4.
>
> **Art. 4 (Pensione di garanzia).** 1. È istituito presso l'INPS il Fondo per la pensione di garanzia. 2. Dal 1° gennaio 2036 ai pensionati con primo accredito contributivo successivo al 31 dicembre 1995 e almeno 20 anni di contributi effettivi o figurativi è riconosciuta un'integrazione fino a 1,5 volte l'importo dell'assegno sociale, ridotta in proporzione al reddito, secondo i criteri dell'assegno sociale. 3. Ai fini del comma 2 sono valorizzati i periodi di cura di figli fino a 6 anni e di familiari non autosufficienti, di disoccupazione indennizzata e di formazione certificata, fino a 5 anni complessivi.
>
> **Art. 5 (Adesione automatica e trasparenza).** 1. Dal 1° luglio 2028 i lavoratori dipendenti neoassunti aderiscono alla forma di previdenza complementare prevista dal contratto applicato, salvo rinuncia espressa entro sei mesi. 2. Ogni disegno di legge in materia previdenziale è accompagnato da una relazione dell'UPB sul costo per coorte di nascita.
>
> **Art. 6 (Copertura finanziaria).** 1. Agli oneri amministrativi, pari a 0,03 mld annui nel 2027-2029, si provvede con le risorse del Fondo dell'articolo 4. 2. Agli oneri dell'articolo 4, valutati in 0,6 mld annui dal 2036, si provvede con le minori spese derivanti dalla rivalutazione al 50% della quota di trattamento eccedente 6 volte il minimo, disposta dal 2030 con modifica dell'articolo 34 della legge 23 dicembre 1998, n. 448. Le eventuali eccedenze sono accantonate nel Fondo.

**Cronoprogramma**
- **Primi 100 giorni.** Il CdM approva il ddl, collegato alla manovra. L'INPS stima la quota di pensione non coperta da contributi per gli assegni sopra 10 volte il minimo e quantifica il gettito. L'UPB pubblica la prima relazione sul costo per generazione delle misure vigenti.
- **Entro 12 mesi.** Approvazione della legge. DM sui coefficienti attuariali e sull'elenco dei gravosi (INAIL). Il contributo si applica dal primo rateo utile del 2027. COVIP e Ministero del lavoro preparano l'adesione automatica.
- **Entro fine legislatura.** Il contributo si chiude il 31/12/2029, senza rinnovo automatico. La perequazione differenziata parte dal 2030. Alla prima verifica demografica ISTAT si rivede la soglia della garanzia, che entra in funzione nel 2036.

**Indicatori**

| KPI | Base | Obiettivo a 3 anni (2029) | Obiettivo a 5 anni (2031) |
|---|---|---|---|
| Spesa pensionistica / PIL rispetto allo scenario RGS | 15,2%, 2025 (RGS agg. 2026) | non oltre lo scenario RGS base | non oltre lo scenario RGS base, con picco 2041-44 ≤ 17,1% |
| Leggi previdenziali con relazione UPB sul costo per generazione | 0%, 2026 | 100% | 100% |
| Neoassunti iscritti alla previdenza complementare | base COVIP da acquisire | +20 punti | +30 punti |

**Rischi di attuazione e mitigazione**
- *Ricorsi sul contributo*: è triennale, progressivo, ha soglia alta e base solo non contributiva, e il gettito resta nel circuito previdenziale. Se la Corte lo sospende, la ESSENZIALE resta in piedi, perché la garanzia è coperta dalla perequazione.
- *Calcolo della quota non coperta da contributi*: ricalcolo INPS dove ci sono i dati, coefficienti forfettari pubblicati altrove.
- *Uscita anticipata più costosa del previsto*: coefficienti attuariali rivisti ogni due anni dalla RGS.
- *Lavori usuranti trascurati*: elenco dei gravosi fondato sulle evidenze INAIL e non sulla contrattazione politica.
- *Consenso*: clausola di trasparenza UPB e comunicazione del costo per generazione.

---

## 02-C4 — Reddito di inclusione universale con «lavoro che conviene»

**Problema in un dato.** Nel 2025 sono in povertà assoluta **5,4 milioni di persone (9,3%)** e **2,1 milioni di famiglie**. I minori poveri sono 1,136 milioni (12,5%) (ISTAT, *La povertà in Italia 2025*). L'ADI raggiunge **690 mila nuclei** a giugno 2026 (INPS), circa un terzo delle famiglie in povertà assoluta.

**Soluzione.**
- L'ADI si apre ai nuclei in povertà grave senza requisito categoriale, cioè anche senza figli, disabili o anziani in casa.
- Chi trova lavoro perde solo il 50% del beneficio per ogni euro guadagnato, per 12 mesi.
- La residenza richiesta scende a 2 anni, compatibile con il diritto UE. La scala di equivalenza migliora per le famiglie numerose.

**Varianti**

| Variante | Contenuto | Costo 2027 / 2028 / 2029 / regime | Intensità | Copertura |
|---|---|---|---|---|
| PIENA | Universale sotto le soglie ADI; scala più favorevole ai minori; decalage al 50-60% per 18 mesi | 0,5 / 2,0 / 3,0 / **3,0** (2029) | 1 | RIORDINO_BONUS 1,0 + SPESE_FISCALI 1,0 + SAD 1,0 |
| **ESSENZIALE** | Universale per ISEE fino a 6.000 €, importo ridotto per gli adulti soli; decalage al 50% per 12 mesi; residenza 2 anni; scala migliore per nuclei con 3 o più figli | 0,3 / 1,2 / 1,5 / **1,5** (2029) | 0,55 | RIORDINO_BONUS 0,5 + SPESE_FISCALI 0,5 + SAD 0,5 |
| PILOTA | Sperimentazione randomizzata in 12 ambiti | 0,03 / 0,10 / 0,10 / **0,10** | 0,05 | RIORDINO_BONUS 0,1 |

La quota a carico della riforma SAD compensa le famiglie povere per l'aumento dei prezzi energetici che la riforma stessa produce (sinergia con l'area 03). Rispetto al registro non sono più usati come copertura la lotta all'evasione e i risparmi dalle «quote».

**Articolato normativo essenziale (variante ESSENZIALE)**

> **Art. 1 (Finalità).** 1. Al fine di contrastare la povertà assoluta, in attuazione degli articoli 3 e 38 della Costituzione, l'Assegno di inclusione di cui al decreto-legge 4 maggio 2023, n. 48, è esteso ai nuclei in condizione di grave disagio economico, indipendentemente dalla loro composizione, e reso compatibile con il lavoro.
>
> **Art. 2 (Accesso universale per la povertà grave).** 1. Dal 1° luglio 2027 hanno diritto all'Assegno anche i nuclei privi dei componenti di cui all'articolo 1, comma 1, del decreto-legge n. 48 del 2023, con ISEE non superiore a 6.000 euro e che rispettano i requisiti patrimoniali vigenti. 2. Per i nuclei composti da un solo adulto l'importo base è pari al 75% di quello ordinario.
>
> **Art. 3 (Lavoro che conviene).** 1. Il reddito da lavoro percepito durante la fruizione dell'Assegno riduce il beneficio nella misura del 50%, per i primi dodici mesi dall'avvio del rapporto. 2. La comunicazione obbligatoria di assunzione aggiorna automaticamente il beneficio, senza nuova domanda.
>
> **Art. 4 (Residenza e scala di equivalenza).** 1. All'articolo 2, comma 2, lettera a), del decreto-legge n. 48 del 2023, il requisito di residenza è ridotto a due anni, anche non continuativi, in conformità alla sentenza della Corte di giustizia UE del 29 luglio 2024, cause riunite C-112/22 e C-223/22. 2. Il parametro della scala di equivalenza per il terzo figlio minore e i successivi è aumentato a 0,25.
>
> **Art. 5 (Patto di inclusione e garanzie).** 1. I servizi sociali degli ambiti e i centri per l'impiego assegnano a ciascun nucleo un case manager. 2. Gli strumenti automatizzati di profilazione hanno solo funzione di supporto. Ogni decisione sul beneficio è adottata da un operatore, che la motiva, nel rispetto del regolamento (UE) 2024/1689.
>
> **Art. 6 (Copertura finanziaria).** 1. Agli oneri, pari a 0,3 mld nel 2027, 1,2 mld nel 2028 e 1,5 mld annui dal 2029, si provvede:
> - a) per 0,5 mld con la soppressione delle carte e dei contributi monetari selettivi elencati nell'allegato, le cui risorse confluiscono nell'Assegno;
> - b) per 0,5 mld con il riordino delle spese fiscali;
> - c) per 0,5 mld con quota delle maggiori entrate derivanti dalla riforma dei sussidi ambientalmente dannosi.

**Cronoprogramma**
- **Primi 100 giorni.** La norma entra nella legge di bilancio o in un ddl collegato. L'INPS adegua la piattaforma SIISL. Il Ministero del lavoro definisce con ANCI gli standard dei case manager.
- **Entro 12 mesi.** Avvio dal 1/7/2027. Il decalage diventa automatico grazie alle comunicazioni obbligatorie. Parte la valutazione INAPP-Banca d'Italia con gruppi di confronto.
- **Entro fine legislatura.** Dopo 36 mesi c'è il rapporto di valutazione: povertà, take-up e lavoro dopo 12 mesi. Il Parlamento decide se estendere l'universalità alla soglia piena dell'ADI (variante PIENA).

**Indicatori**

| KPI | Base | Obiettivo a 3 anni (2029) | Obiettivo a 5 anni (2031) |
|---|---|---|---|
| Incidenza della povertà assoluta, individui | 9,3%, 2025 (ISTAT) | 8,6% | 8,0% |
| Incidenza della povertà assoluta, minori | 12,5%, 2025 (ISTAT) | 11,5% | 10,5% |
| Nuclei beneficiari con reddito da lavoro 12 mesi dopo l'ingresso | base INPS-SIISL da acquisire nel 2027 | +10 punti | +15 punti |

**Rischi di attuazione e mitigazione**
- *Frodi*: controlli incrociati INPS, Entrate e catasto prima dell'erogazione.
- *Pochi operatori nei CPI e nei servizi sociali*: case manager finanziati con la quota servizi del Fondo povertà e con il FSE+ già programmato.
- *Aliquote marginali implicite cumulate con AUU e IRPEF*: simulazione INPS-MEF pubblicata prima dell'avvio.
- *Percezione di assistenzialismo*: dati pubblici sui minori e sul lavoro dei beneficiari.
- *Requisito di residenza*: scelta valoriale, perché dipende dalla politica migratoria. I 2 anni sono il minimo prudente dopo la sentenza CGUE; il Parlamento può fissare un valore diverso entro i limiti UE.

---

## 02-C5 — Progetto di vita esigibile e lavoro per le persone con disabilità

**Problema in un dato.** Nel 2025 il tasso di occupazione delle persone con limitazioni gravi è inferiore di **43,4 punti** a quello delle persone senza limitazioni (Eurostat `tepsr_sp200`, serie `02_divario_occupazione_disabilita`). In ISTAT, l'occupazione 15-64 delle persone con limitazioni gravi è al **32,5%** contro il 58,9% (dato 2021). Le persone con limitazioni gravi sono 2,9 milioni (ISTAT, 2023).

**Soluzione.**
- La riforma del d.lgs. 62/2024 si completa su tutto il territorio dal 2027: valutazione di base, progetto di vita e unità di valutazione dotate di personale.
- Un budget di progetto unico segue la persona.
- Il collocamento mirato diventa effettivo: banca dati delle quote scoperte, sanzioni automatiche, rimborso dell'accomodamento ragionevole.

**Varianti**

| Variante | Contenuto | Costo 2027 / 2028 / 2029 / regime | Intensità | Copertura |
|---|---|---|---|---|
| PIENA | Tutto, compresi il LEP domiciliare e il rafforzamento del «Dopo di noi» | 0,4 / 0,9 / 1,5 / **1,5** (2029) | 1 | RIALLOCAZIONE 0,5 + SPESE_FISCALI 0,5 + ACCISE_SALUTE 0,5 |
| **ESSENZIALE** | Progetto di vita ovunque dal 2027 con circa 3.000 operatori per le UVM; budget di progetto; accomodamento ragionevole; LEP domiciliare dal 2030 | 0,3 / 0,6 / 0,8 / **0,8** (2029) | 0,6 | RIALLOCAZIONE 0,4 + ACCISE_SALUTE 0,4 |
| ZERO | Solo riforma del collocamento mirato e fusione amministrativa dei fondi | 0 | 0,25 | invarianza |

**Articolato normativo essenziale (variante ESSENZIALE, decreto legislativo integrativo del d.lgs. 62/2024)**

> **Art. 1 (Finalità).** 1. In attuazione della Convenzione ONU sui diritti delle persone con disabilità e della legge 22 dicembre 2021, n. 227, il presente decreto rende esigibile su tutto il territorio il progetto di vita individuale, personalizzato e partecipato, e rafforza l'inclusione lavorativa.
>
> **Art. 2 (Unità di valutazione multidimensionale).** 1. Dal 1° gennaio 2027 il progetto di vita è garantito in ogni ambito territoriale sociale. 2. Per dotare le unità di valutazione di personale sociale e sanitario dedicato, è assegnato alle Regioni un contributo di 0,2 mld annui, ripartito in base alla popolazione con disabilità certificata, per l'assunzione di circa 3.000 operatori.
>
> **Art. 3 (Budget di progetto).** 1. Il budget di progetto riunisce le risorse sanitarie, sociali e previdenziali destinate alla persona. La persona può sceglierne la gestione diretta, con un sostegno alla gestione. 2. È istituito il Fondo per il budget di progetto, con una dotazione di 0,4 mld annui dal 2029, alimentato anche dal riordino del Fondo per le non autosufficienze e del Fondo unico per l'inclusione. 3. L'attivazione del budget non può ridurre le prestazioni già in godimento.
>
> **Art. 4 (Collocamento mirato).** 1. L'INPS e l'INL gestiscono la banca dati nazionale degli obblighi di cui alla legge 12 marzo 1999, n. 68. Le sanzioni per le quote scoperte da oltre dodici mesi sono applicate automaticamente. 2. Ai datori di lavoro è rimborsato fino al 60% dei costi documentati per l'accomodamento ragionevole, nel limite di 0,1 mld annui.
>
> **Art. 5 (Monitoraggio).** 1. L'Osservatorio nazionale sulla condizione delle persone con disabilità pubblica ogni anno, per ambito, il numero di progetti di vita attivi e i tempi di attivazione.
>
> **Art. 6 (Copertura finanziaria).** 1. Agli oneri, pari a 0,3 mld nel 2027, 0,6 mld nel 2028 e 0,8 mld annui dal 2029, si provvede per 0,4 mld con la riduzione di autorizzazioni di spesa del Ministero del lavoro e delle politiche sociali e dell'Autorità politica delegata in materia di disabilità, e per 0,4 mld con quota delle maggiori entrate derivanti dall'aumento delle accise sui prodotti del tabacco.

**Cronoprogramma**
- **Primi 100 giorni.** Schema di decreto legislativo integrativo. Il Ministero per le disabilità e l'INPS consolidano i risultati della sperimentazione nelle province, estesa dal 1/3/2026.
- **Entro 12 mesi.** Avvio nazionale dal 1/1/2027, come previsto dal DL 202/2024. Le Regioni assumono il personale delle UVM. La banca dati L. 68/99 è operativa.
- **Entro fine legislatura.** Il Fondo per il budget di progetto va a regime. Nel 2029 c'è la valutazione e, dal 2030, si decide il LEP domiciliare (variante PIENA).

**Indicatori**

| KPI | Base | Obiettivo a 3 anni (2029) | Obiettivo a 5 anni (2031) |
|---|---|---|---|
| Divario occupazionale per limitazioni gravi (punti) | 43,4, 2025 (Eurostat `tepsr_sp200`) | 40 | 37 |
| Occupazione 15-64 delle persone con limitazioni gravi | 32,5%, 2021 (ISTAT) | 36% | 38% (40% al 2032) |
| Progetti di vita attivi | base INPS-Osservatorio da acquisire (sperimentazione 2025-26) | 150 mila | 300 mila |

**Rischi di attuazione e mitigazione**
- *Divari regionali*: riparto vincolato e monitoraggio pubblico per ambito, con poteri sostitutivi in caso di inerzia.
- *Il budget come taglio mascherato*: la norma vieta di ridurre le prestazioni già in godimento.
- *Scaricabarile tra ASL e Comuni*: UVM integrate e accordo di programma obbligatorio per ambito.
- *Imprese inadempienti*: sanzioni automatiche, ma anche rimborso dell'accomodamento e convenzioni con le cooperative sociali.

---

## 02-C6 — Bilancio generazionale e strategia demografica

**Problema in un dato.** Nel 2025 i nati sono **355.772** (−3,8%) e la fecondità è **1,14** (ISTAT). Il rapporto tra persone con 65 anni e più e persone di 15-64 anni sale dal **39% nel 2025 al 63,1% nel 2050** (Eurostat EUROPOP2025, `proj_25ndbi`). Nessuna legge oggi dichiara quanto costa a ciascuna generazione.

**Soluzione.**
- Le leggi con effetti oltre 0,5 mld hanno una valutazione d'impatto generazionale dell'UPB, unificata con la proposta 01-P1.
- Il Paese adotta una Strategia demografica decennale con obiettivi pubblici: natalità, rientro dei giovani, occupazione.
- Gli ingressi per lavoro si programmano ogni tre anni sui fabbisogni delle imprese. La scelta del livello degli ingressi resta esplicitamente politica.

**Varianti**

| Variante | Contenuto | Costo 2027 / 2028 / 2029 / regime | Intensità | Copertura |
|---|---|---|---|---|
| PIENA | Valutazione generazionale + Strategia + rientro dei giovani con tetto di reddito + formazione pre-partenza e riconoscimento dei titoli | 0,15 / 0,30 / 0,40 / **0,40** (2029) | 1 | RIALLOCAZIONE 0,2 + SPESE_FISCALI 0,2 (tetto al regime impatriati) |
| **ESSENZIALE** | Valutazione generazionale (con 01-P1) + Strategia + programmazione triennale; formazione all'estero solo con fondi AMIF | 0,05 / 0,10 / 0,10 / **0,10** (2028) | 0,5 | RIALLOCAZIONE 0,1 |
| ZERO | Solo Strategia per DPCM | 0 | 0,3 | invarianza |

**Articolato normativo essenziale (variante ESSENZIALE)**

> **Art. 1 (Finalità).** 1. Al fine di tutelare l'interesse delle future generazioni, ai sensi degli articoli 9 e 81 della Costituzione, la presente legge introduce la valutazione d'impatto generazionale e la Strategia demografica nazionale.
>
> **Art. 2 (Valutazione d'impatto generazionale).** 1. I disegni di legge e gli emendamenti del Governo con effetti finanziari superiori a 0,5 mld annui sono accompagnati da una valutazione d'impatto generazionale. La valutazione indica il saldo per coorte di nascita e l'effetto sul debito implicito. 2. L'Ufficio parlamentare di bilancio redige la valutazione o ne verifica la redazione, secondo una metodologia pubblica. La disciplina è coordinata con quella prevista dalla proposta 01-P1.
>
> **Art. 3 (Strategia demografica nazionale).** 1. Entro il 30 giugno 2027 il Governo adotta, con decreto del Presidente del Consiglio dei ministri e previo parere delle Commissioni parlamentari, una Strategia demografica decennale. La Strategia fissa obiettivi quantitativi su natalità, occupazione femminile e giovanile, rientro dei cittadini emigrati e integrazione dei lavoratori stranieri, e include scenari alternativi sui flussi migratori. 2. Il Governo riferisce ogni anno al Parlamento sullo stato di attuazione.
>
> **Art. 4 (Programmazione degli ingressi per lavoro).** 1. Il documento di programmazione triennale dei flussi d'ingresso per lavoro si fonda sui fabbisogni rilevati dal sistema informativo Excelsior e dai dati INPS sulle assunzioni non coperte. Il livello complessivo degli ingressi è determinato dal Parlamento con atto d'indirizzo.
>
> **Art. 5 (Copertura finanziaria).** 1. Agli oneri, pari a 0,05 mld nel 2027 e a 0,1 mld annui dal 2028, si provvede con la riduzione delle autorizzazioni di spesa del Ministero del lavoro e delle politiche sociali. All'Ufficio parlamentare di bilancio si applica l'articolo 19 della legge 24 dicembre 2012, n. 243.

**Cronoprogramma**
- **Primi 100 giorni.** Il ddl è presentato insieme a 01-P1. Il Dipartimento per le politiche della famiglia, ISTAT e UPB definiscono la metodologia del costo per coorte.
- **Entro 12 mesi.** Approvazione della legge. DPCM sulla Strategia entro il 30/6/2027. Prima programmazione triennale dei flussi fondata sui fabbisogni (2028-30).
- **Entro fine legislatura.** Tutte le leggi oltre 0,5 mld hanno la valutazione generazionale. Due relazioni annuali sulla Strategia. Revisione degli obiettivi con le nuove previsioni ISTAT.

**Indicatori**

| KPI | Base | Obiettivo a 3 anni (2029) | Obiettivo a 5 anni (2031) |
|---|---|---|---|
| Leggi oltre 0,5 mld con valutazione generazionale | 0%, 2026 | 100% | 100% |
| Tasso di occupazione 20-64 | 67,6%, 2025 (Eurostat `lfsi_emp_a`) | 69,0% | 70,5% |
| NEET 15-29 (obiettivo condiviso con l'area 05) | 13,3%, 2025 (Eurostat `edat_lfse_20`; UE 11,0%) | 12,0% | 11,0% |

**Rischi di attuazione e mitigazione**
- *Valutazione formalistica*: è pubblica, ha un'audizione obbligatoria e un metodo unico UPB.
- *Strumentalizzazione del tema migratorio*: la Strategia presenta scenari alternativi con dati ISTAT e INPS pubblici. Il livello degli ingressi è deciso dal Parlamento, non dai tecnici.
- *Sovrapposizione con 01-P1*: articolato unico. La variante ESSENZIALE costa poco proprio perché usa la stessa struttura UPB.

---

## Note per il coordinatore e per l'agente coperture

1. **Nuove misure da inserire nel menu (fondo PENSIONI):**
   - *perequazione differenziata*: rivalutazione al 50% della quota di pensione sopra 6 volte il minimo, dal 2030. Il gettito è da stimare con l'INPS; serve almeno 0,35-0,6 mld/anno dal 2036;
   - *contributo di solidarietà triennale 2027-29*: 0,15-0,3 mld/anno, solo come dotazione una tantum del Fondo garanzia e **non per spesa permanente**.
2. **CUAF**: il registro la conteggiava come copertura di 02-C2 (fondo ALTRO); l'ho tolta. Se l'INPS documenta l'avanzo della CUAF, l'aumento contributivo dello 0,1-0,2% è una DRM da valutare nel menu.
3. **02-C2 e il calendario LEP**: la variante ESSENZIALE si allinea al LEP del 33% già previsto entro il 2027 dalla L. 234/2021 e lo rende finanziato, perché paga la spesa corrente. La versione piena porta la copertura al 45% entro il 2032.
4. **Sovrapposizioni**:
   - il congedo di 02-C2 assorbe il mese di congedo parentale per il padre previsto dal ddl bilancio 2027;
   - la flessibilità di 02-C3 sostituisce il fondo flessibilità del ddl 2027 (850 mln, da verificare);
   - 02-C6 si fonde con 01-P1.
5. **Coperture tolte dal registro** (registro 02-C1, C2, C4, C5): RISPARMI_ATTESI, IVA_EVASIONE, ALTRO e i risparmi già nel tendenziale dalle «quote». Ora tutte le varianti sono finanziate da fondi generali o da PENSIONI.
