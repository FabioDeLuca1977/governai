# Schede pronte — Area 04: Infrastrutture, Trasporti, Casa, Regioni, Sud, Coesione, PNRR

*Agente ministeriale 04, 7 novembre 2026. Varianti e coperture in `programma/varianti/04_infrastrutture.csv`. Importi in mld €/anno; "stima GovernAI" quando non esiste una quantificazione ufficiale (nessuna delle sei proposte ne ha una: vedi `dati/verifiche/04_infrastrutture.md`). Il cronoprogramma decorre dall'insediamento del Governo (T0).*

## Regole seguite per le coperture

- Solo fondi con capienza: **SAD, SPESE_FISCALI, RIALLOCAZIONE** (risorse generali, attivate dal menu coperture), **COESIONE_2127** (solo investimenti una tantum 2027-29, mai personale), **ETS2_FSC** (solo nelle varianti PIENA di 04-P2 e 04-P3, per misure ammissibili al Fondo sociale per il clima; tutte le ESSENZIALI ne fanno a meno, perché nello scenario prudente la sua capienza è 0).
- Nessuna riga su DEFICIT, RISPARMI_ATTESI, IVA_EVASIONE, ETS o ALTRO. Le righe ALTRO e RISPARMI_ATTESI del registro (04-P1, 04-P4, 04-P5, 04-P6) sono sostituite.
- Prelievo su COESIONE_2127 se si scelgono tutte le ESSENZIALI: 0,95 mld/anno, cioè circa metà della capienza prudente di tutto il programma (2,0). Con tutte le PIENE: 1,40. **Il coordinatore deve verificare il conflitto con le altre aree.**
- Sovrapposizioni dichiarate: asili nido (02-C2) e case di comunità (06-C3) sono esclusi da 04-P1; il supporto tecnico ai piccoli Comuni è in 09-C3; il gettito SAD usato da 04-P3 è in conflitto con il dividendo climatico 03-P1.

## Quadro delle varianti

| Proposta | PIENA (costo 2029 / intensità) | ESSENZIALE | PILOTA / ZERO |
|---|---|---|---|
| 04-P1 Continuità post-PNRR | 0,73 / 1 (picco 1,21 nel 2027, zero dal 2031) | 0,28 / 0,6 | PILOTA 0,09 / 0,25 |
| 04-P2 Casa a canone giusto | 0,95 / 1 | 0,48 / 0,6 | PILOTA 0,14 / 0,15 |
| 04-P3 Prima il treno dei pendolari | 2,32 / 1 | 1,17 / 0,6 | PILOTA 0,62 / 0,3 |
| 04-P4 Prova dei numeri | 0,025 / 1 | 0,012 / 0,7 | ZERO 0 / 0,35 |
| 04-P5 LEP prima | 1,0 / 1 | 0,5 / 0,7 | ZERO 0 / 0,45 |
| 04-P6 Restare è possibile | 0,80 / 1 | 0,42 / 0,6 | PILOTA 0,10 / 0,15 |
| **Totale** | **5,83** | **2,86** | **0,95** |

**Raccomandazione dell'agente**: le ESSENZIALI di P2, P3 e P6, la PIENA di P4, la ZERO di P5 e la PILOTA di P1 (2,2 mld a regime, di cui 0,85 una tantum dalla coesione). P5 PIENA ed ESSENZIALE solo se il menu coperture lascia margine dopo il nucleo robusto.

---

## 04-P1 — Patto di continuità post-PNRR

**Problema in un dato.** Le amministrazioni stimano **24,2 mld € di spesa PNRR da sostenere oltre il 2026, su 66 misure** (Corte dei conti, Relazione PNRR, Doc. XIII-bis n. 7, maggio 2026; serie `04_pnrr_corte_conti_mag2026`). Molte opere apriranno dopo la fine del Piano, senza fondi per la gestione.

**Soluzione.** Un fondo temporaneo e decrescente (80-60-40-20-0%) copre una parte dei costi di gestione delle opere PNRR degli enti locali, a condizione che siano utilizzate secondo dati amministrativi. Le opere a basso utilizzo si riconvertono con fondi di coesione. Un censimento obbligatorio impedisce nuove opere senza piano di gestione.

| Variante | Contenuto | 2027 | 2028 | 2029 | Intensità | Fondi a regime |
|---|---|---|---|---|---|---|
| PIENA | Tutti gli enti locali, 80-60-40-20-0% | 1,21 | 0,97 | 0,73 | 1 | RIALLOCAZIONE 0,24; SPESE_FISCALI 0,24; COESIONE 0,25 |
| ESSENZIALE | Comuni sotto 15.000 ab., Mezzogiorno, aree interne, 60-40-20-0% | 0,54 | 0,41 | 0,28 | 0,6 | RIALLOCAZIONE 0,13; COESIONE 0,15 |
| PILOTA | Censimento + regola del piano di gestione + fondo per Comuni sotto 5.000 ab. | 0,15 | 0,12 | 0,09 | 0,25 | RIALLOCAZIONE 0,04; COESIONE 0,05 |

**Articolato normativo essenziale** (legge di bilancio)

> **Art. 1 (Finalità).** Al fine di assicurare l'effettivo esercizio dei servizi connessi agli investimenti finanziati dal Piano nazionale di ripresa e resilienza e di evitare il sottoutilizzo delle opere realizzate, è istituito presso il Ministero dell'economia e delle finanze il Fondo di continuità dei servizi post-PNRR, di durata quinquennale.
>
> **Art. 2 (Censimento).** Entro sei mesi dall'entrata in vigore della presente legge, il Dipartimento per le politiche di coesione e per il Sud, sulla base del sistema ReGiS, pubblica il censimento delle opere realizzate dagli enti locali con il PNRR che comportano costi di gestione ricorrenti, con indicazione del costo annuo stimato e dell'utilizzo previsto. Sono esclusi gli asili nido e le case della comunità, finanziati con le risorse dedicate.
>
> **Art. 3 (Contributo decrescente e condizionato).** Il Fondo concorre ai costi di gestione delle opere censite nella misura dell'80, 60, 40 e 20 per cento rispettivamente nel primo, secondo, terzo e quarto anno, e cessa dal quinto. L'erogazione è subordinata al raggiungimento di soglie di utilizzo rilevate da fonti amministrative e definite con decreto del Ministro dell'economia e delle finanze, d'intesa con la Conferenza Stato-città ed autonomie locali.
>
> **Art. 4 (Riconversione).** Le opere con utilizzo inferiore alla soglia per due anni consecutivi sono oggetto di un piano di riconversione o di gestione associata, finanziabile con le risorse dei programmi della politica di coesione 2021-2027 nel rispetto dei regolamenti europei.
>
> **Art. 5 (Nuovi investimenti).** Dal 1° gennaio del secondo anno successivo all'entrata in vigore, nessun investimento pubblico locale superiore a 1 milione di euro è finanziato con risorse statali senza un piano di gestione che indichi costi e copertura per i primi dieci anni.
>
> **Art. 6 (Copertura finanziaria).** Agli oneri, pari a 0,96 miliardi nel 2027, 0,72 nel 2028, 0,48 nel 2029 e 0,24 nel 2030, si provvede mediante corrispondente riduzione delle spese fiscali di cui all'allegato X e delle dotazioni dei capitoli di cui all'allegato Y. La decrescenza degli oneri non può essere modificata se non con la legge di bilancio e con contestuale copertura.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| 100 giorni | Norma in legge di bilancio; avvio del censimento su ReGiS; criteri di utilizzo | MEF-RGS, Dipartimento coesione, ANCI-UPI |
| 12 mesi | Censimento pubblicato; prima erogazione all'80% in base agli indicatori; elenco delle opere da riconvertire; riprogrammazione FESR per la riconversione | Dipartimento coesione, Regioni (autorità di gestione), Comuni |
| Fine legislatura | Fondo azzerato; opere attive a carico ordinario; relazione finale della Corte dei conti e dell'UPB | Corte dei conti, UPB |

**Indicatori**

| KPI | Base | Obiettivo a 3 anni | a 5 anni |
|---|---|---|---|
| Opere PNRR locali censite con servizio in esercizio | da censimento (mese 6); oggi non misurato | ≥ 85% | ≥ 90% |
| Spesa PNRR prevista oltre il 2026 effettivamente sostenuta | 0 su 24,2 mld (Corte dei conti, 2026) | ≥ 70% | 100% |
| Quota dei costi di gestione a carico ordinario degli enti | 20% nel primo anno (da norma) | 80% | 100% |

**Rischi e mitigazioni.** *Pressione per rendere il fondo permanente* → decrescenza scritta in legge, modificabile solo con nuova copertura. *Indicatori aggirabili* → solo dati amministrativi (ReGiS, flussi SSN, anagrafe scolastica). *Doppio finanziamento con 02-C2 e 06-C3* → esclusione esplicita all'art. 2. *Picco nel 2027 quando le coperture sono ancora in fase di avvio* → se il menu non basta, si sceglie la ESSENZIALE.

---

## 04-P2 — Casa a canone giusto

**Problema in un dato.** Nel 2025 il **22,3% degli inquilini a prezzo di mercato** spende oltre il 40% del reddito per la casa, contro il 18,5% della media UE e il 19,4% del 2024 (Eurostat `ilc_lvho07c`; serie `04_sovraccarico_costo_abitativo_per_titolo`). Nel 2010-2024 gli affitti sono cresciuti del 13,9% mentre i prezzi delle case scendevano del 5,4% (serie `04_affitti_hicp_indice`, `04_prezzi_abitazioni_indice`). Circa 60.000 alloggi ERP sono vuoti per mancata manutenzione (Federcasa, memoria Camera, 19.5.2026).

**Soluzione.** Contratti quadro regionali per recuperare "a pacchetti" gli alloggi ERP vuoti, con fondi di coesione e Piano Casa. Agenzie sociali per l'affitto (ASA) che garantiscono canone e manutenzione ai proprietari e sublocano a canone concordato a famiglie in graduatoria o nella fascia grigia. La copertura viene dalle detrazioni edilizie non selettive.

| Variante | Contenuto | 2027 | 2028 | 2029 | Intensità | Fondi a regime |
|---|---|---|---|---|---|---|
| PIENA | 60.000 alloggi ERP recuperati entro il 2030; 100.000 contratti ASA | 0,45 | 0,75 | 0,95 | 1 | COESIONE 0,40; SPESE_FISCALI 0,45; ETS2_FSC 0,10 |
| ESSENZIALE | 30.000 alloggi recuperati; 50.000 contratti ASA nelle città ad alta tensione abitativa | 0,25 | 0,38 | 0,48 | 0,6 | COESIONE 0,30; SPESE_FISCALI 0,18 |
| PILOTA | ASA in 10 città (10.000 contratti); ERP in 5 Regioni | 0,08 | 0,12 | 0,14 | 0,15 | COESIONE 0,10; SPESE_FISCALI 0,04 |

**Articolato normativo essenziale** (legge di bilancio e decreto MIT attuativo del Piano Casa)

> **Art. 1 (Finalità).** Al fine di aumentare l'offerta di abitazioni a canone sostenibile e di ridurre l'incidenza del costo dell'abitazione sul reddito delle famiglie in locazione, la presente legge disciplina il recupero accelerato degli alloggi di edilizia residenziale pubblica non assegnabili e istituisce le Agenzie sociali per l'affitto.
>
> **Art. 2 (Recupero ERP a pacchetti).** Le Regioni, d'intesa con gli enti gestori, stipulano entro dodici mesi contratti quadro pluriennali di manutenzione straordinaria per lotti di alloggi non assegnabili, con obbligo di riassegnazione entro dodici mesi dalla fine dei lavori. Le risorse di cui all'articolo 2 del decreto-legge n. 66 del 2026 e quelle dei programmi della politica di coesione 2021-2027 sono assegnate in proporzione agli alloggi effettivamente riassegnati.
>
> **Art. 3 (Agenzie sociali per l'affitto).** Gli enti gestori ERP e i Comuni capoluogo possono costituire Agenzie sociali per l'affitto, che prendono in locazione alloggi privati a canone concordato ai sensi dell'articolo 2, comma 3, della legge n. 431 del 1998 e li sublocano a nuclei con ISEE entro le soglie definite con decreto. L'Agenzia garantisce al proprietario il pagamento del canone e la riconsegna dell'alloggio nello stato originario.
>
> **Art. 4 (Fondo di garanzia e incentivi).** È istituito presso il Ministero delle infrastrutture e dei trasporti il Fondo di garanzia per l'affitto sociale, che copre morosità, piccola manutenzione e un'integrazione del canone per i nuclei a basso ISEE. Per i contratti stipulati con le Agenzie per almeno otto anni, l'aliquota della cedolare secca è ridotta al 5 per cento.
>
> **Art. 5 (Monitoraggio).** Il Ministero delle infrastrutture e dei trasporti, d'intesa con l'ISTAT, istituisce la rilevazione nazionale annuale delle graduatorie ERP, degli alloggi sfitti e dei contratti delle Agenzie, i cui dati sono pubblicati in formato aperto.
>
> **Art. 6 (Copertura finanziaria).** Agli oneri di cui all'articolo 4, pari a 0,10 miliardi nel 2027, 0,25 nel 2028 e 0,45 dal 2029, si provvede mediante la riduzione delle detrazioni per interventi edilizi su unità immobiliari diverse dall'abitazione principale, non locate a canone concordato, di cui all'allegato X. Agli oneri di cui all'articolo 2 si provvede nei limiti delle risorse dei programmi della politica di coesione 2021-2027 riprogrammate nell'obiettivo di policy 4.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| 100 giorni | Norma in legge di bilancio; decreto MIT su ASA e Fondo di garanzia; richiesta alla Commissione di riprogrammare il FESR (OP4) | MIT, MEF, Dipartimento coesione |
| 12 mesi | Prime 20 ASA operative; contratti quadro in tutte le Regioni; primi 10.000 alloggi in cantiere; prima rilevazione ufficiale delle graduatorie | Regioni, enti gestori (ex IACP), Comuni capoluogo, ISTAT |
| Fine legislatura | 60.000 alloggi ERP riassegnati; 100.000 contratti ASA; valutazione indipendente dell'effetto sui canoni | MIT, UPB, università (valutazione) |

**Indicatori**

| KPI | Base | Obiettivo a 3 anni | a 5 anni |
|---|---|---|---|
| Inquilini a prezzo di mercato con costo abitativo oltre il 40% del reddito | 22,3% (2025, Eurostat `ilc_lvho07c`) | ≤ 19,5% | ≤ 17,5% (sotto la media UE) |
| Alloggi ERP non assegnabili recuperati e riassegnati | 0 su circa 60.000 (Federcasa, 2026) | 35.000 | 60.000 |
| Contratti ASA attivi | 0 (2026) | 60.000 | 100.000 |

**Rischi e mitigazioni.** *Proprietari poco fiduciosi* → garanzia pubblica e pagamenti puntuali, con tempi pubblicati. *Integrazione del canone assorbita dagli aumenti* → solo canone concordato, con tetto per zona OMI. *Imprese edili che perdono le detrazioni* → il riorientamento premia la manutenzione di alloggi messi in affitto sociale. *Sgomberi del DL 66/2026* → protocollo "da casa a casa" per le famiglie fragili, con le ASA come prima offerta. *Lentezza dei cantieri ERP* → assegnazione delle risorse in base agli alloggi riassegnati, non ai lavori avviati.

---

## 04-P3 — Prima il treno dei pendolari

**Problema in un dato.** L'Italia ha **709 auto ogni 1.000 abitanti (2025), prima nell'UE, contro 584 della media UE27**, e il dato cresce ancora (Eurostat `road_eqs_carhab`; serie `04_auto_per_1000_abitanti`). Le emissioni del trasporto stradale sono **105,0 Mt CO2eq nel 2024, +11,7% sul 1990**, mentre il totale nazionale è sceso del 30% (Eurostat `env_air_gge`; serie `04_emissioni_gas_serra_trasporti`).

**Soluzione.** Prima l'offerta, poi la tariffa. Il Fondo TPL (5,30 mld nel 2026) viene indicizzato all'inflazione e ripartito su posti-km e puntualità, e non più sulla spesa storica. Si finanziano servizi aggiuntivi e treni nuovi con priorità al Sud. Poi si introducono un abbonamento unico regionale ferro-gomma e una tariffa sociale per under 26 e famiglie a basso ISEE.

| Variante | Contenuto | 2027 | 2028 | 2029 | Intensità | Fondi a regime |
|---|---|---|---|---|---|---|
| PIENA | Indicizzazione + 0,5 mld di servizi + abbonamento unico a 39 €/mese con tariffa sociale + rotabile | 1,11 | 1,71 | 2,32 | 1 | SAD 1,42; ETS2_FSC 0,30; COESIONE 0,40; RIALLOCAZIONE 0,20 |
| ESSENZIALE | Indicizzazione + 0,2 mld di servizi al Sud + tariffa sociale (under 26, ISEE sotto 20.000 €) + rotabile in 4 regioni | 0,56 | 0,88 | 1,17 | 0,6 | SAD 0,87; COESIONE 0,30 |
| PILOTA | Indicizzazione + abbonamento unico sperimentale in 3 Regioni + rotabile mirato | 0,36 | 0,51 | 0,62 | 0,3 | SAD 0,42; COESIONE 0,20 |

**Articolato normativo essenziale** (legge di bilancio)

> **Art. 1 (Finalità).** Al fine di aumentare l'offerta di trasporto pubblico locale e regionale, ridurre le emissioni del trasporto stradale e garantire il diritto alla mobilità in tutto il territorio nazionale, la presente legge dispone l'adeguamento del Fondo nazionale per il concorso finanziario dello Stato agli oneri del trasporto pubblico locale e istituisce la tariffa sociale nazionale.
>
> **Art. 2 (Indicizzazione e riparto).** Dal 2027 la dotazione del Fondo è rivalutata annualmente in base all'indice armonizzato dei prezzi al consumo. A decorrere dallo stesso anno, una quota crescente fino al 50 per cento è ripartita tra le Regioni in base ai posti-chilometro offerti, alla puntualità e al riempimento rilevati dall'Osservatorio nazionale TPL, e non in base alla spesa storica.
>
> **Art. 3 (Servizi aggiuntivi e materiale rotabile).** È istituita una sezione del Fondo destinata ai servizi aggiuntivi nelle Regioni con offerta per abitante inferiore alla media nazionale. Il Ministero delle infrastrutture e dei trasporti adotta un programma triennale di acquisto centralizzato di treni regionali e autobus a zero emissioni, prioritariamente per Sicilia, Calabria, Campania, Sardegna e aree interne, finanziato anche con le risorse dei programmi della politica di coesione.
>
> **Art. 4 (Abbonamento unico e tariffa sociale).** Entro tre anni ogni Regione istituisce un abbonamento unico integrato valido su tutti i servizi di trasporto regionale e locale, al prezzo massimo stabilito con decreto. È istituita la tariffa sociale nazionale per i residenti di età inferiore a 26 anni e per i nuclei con ISEE inferiore a una soglia stabilita con decreto. Lo Stato compensa le minori entrate tariffarie solo nelle Regioni che hanno raggiunto gli obiettivi di offerta di cui all'articolo 3.
>
> **Art. 5 (Copertura finanziaria).** Agli oneri, pari a 1,11 miliardi nel 2027, 1,71 nel 2028 e 2,32 dal 2029, si provvede: a) mediante la progressiva riduzione dei sussidi ambientalmente dannosi di cui al Catalogo del Ministero dell'ambiente e della sicurezza energetica indicati nell'allegato X; b) nei limiti delle risorse del Fondo sociale per il clima destinate alle famiglie in condizione di povertà dei trasporti; c) nei limiti delle risorse dei programmi della politica di coesione 2021-2027, per il materiale rotabile; d) mediante riduzione delle autorizzazioni di spesa per opere stradali di cui all'allegato Y.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| 100 giorni | Indicizzazione e nuovo riparto in legge di bilancio; avvio della gara centralizzata per i treni regionali; decreto sulla soglia ISEE della tariffa sociale | MIT, MEF, Consip/RFI, Conferenza delle Regioni |
| 12 mesi | Prime gare aggiudicate; servizi aggiuntivi nei contratti di servizio del Sud; tariffa sociale attiva; abbonamento unico in almeno 5 Regioni | MIT, Regioni, aziende TPL e Trenitalia regionale |
| Fine legislatura | Primi 100 treni nuovi in servizio; abbonamento unico in tutte le Regioni; valutazione dello spostamento modale | MIT, ISTAT, Osservatorio TPL, UPB |

**Indicatori**

| KPI | Base | Obiettivo a 3 anni | a 5 anni |
|---|---|---|---|
| Passeggeri giornalieri su treni regionali | 2,54 mln (2024, Legambiente Pendolaria 2025: fonte di settore) | 2,9 mln | 3,2 mln (3,5 entro il 2032) |
| Emissioni del trasporto stradale | 105,0 Mt CO2eq (2024, Eurostat `env_air_gge`) | ≤ 102 Mt | ≤ 97 Mt |
| Auto ogni 1.000 abitanti | 709 (2025, Eurostat `road_eqs_carhab`) | ≤ 712 (crescita fermata) | ≤ 700 |

**Rischi e mitigazioni.** *Domanda senza offerta, con treni sovraffollati* → la compensazione tariffaria scatta solo dove sono raggiunti gli obiettivi di offerta (art. 4). *Opposizione alla riforma dei SAD (autotrasporto, agricoltura)* → gradualità in 5 anni e compensazioni mirate per il rinnovo delle flotte. *Conflitto con il dividendo climatico 03-P1 sugli stessi SAD* → decisione esplicita del coordinatore. *Tempi di consegna dei treni (2-4 anni)* → gara centralizzata subito e noleggio ponte. *Fondo sociale per il clima non disponibile* → la ESSENZIALE non lo usa.

---

## 04-P4 — Nessuna grande opera senza prova dei numeri

**Problema in un dato.** Quasi tutta la Missione 3 Infrastrutture del PNRR rientra nei **24,2 mld di spesa che slittano oltre il 2026** (Corte dei conti, maggio 2026; serie `04_pnrr_corte_conti_mag2026`). Per le opere oltre 500 mln non esiste oggi un'analisi costi-benefici indipendente, pubblica e confrontata con alternative. Il caso del Ponte sullo Stretto (delibera CIPESS senza visto della Corte dei conti, novembre 2025) lo mostra.

**Soluzione.** Un Ufficio valutazione investimenti presso l'UPB, indipendente, esamina ogni opera oltre 500 mln con scenari demografici ISTAT e climatici, confrontandola con le alternative, e pubblica modelli e dati. Il Governo decide comunque, ma se l'esito è negativo deve motivare la scelta in pubblico (comply or explain). La valutazione ha un termine massimo di 6 mesi.

| Variante | Contenuto | 2027 | 2028 | 2029 | Intensità | Fondi a regime |
|---|---|---|---|---|---|---|
| PIENA | Ufficio presso UPB; soglia 500 mln; anche opere in istruttoria | 0,015 | 0,025 | 0,025 | 1 | RIALLOCAZIONE 0,025 |
| ESSENZIALE | Soglia 1 mld; solo nuove opere e lotti non aggiudicati | 0,008 | 0,012 | 0,012 | 0,7 | RIALLOCAZIONE 0,012 |
| ZERO | Obbligo di pubblicare ACB e dati con le strutture esistenti (CSLP, nuclei di valutazione) | 0 | 0 | 0 | 0,35 | — |

**Articolato normativo essenziale** (legge ordinaria)

> **Art. 1 (Finalità).** Al fine di migliorare la selezione degli investimenti pubblici e di garantire ai cittadini e al Parlamento un'informazione completa sui costi, sui benefici e sulle alternative, è istituito presso l'Ufficio parlamentare di bilancio l'Ufficio per la valutazione degli investimenti pubblici.
>
> **Art. 2 (Ambito).** Sono sottoposte a valutazione le opere pubbliche, comprese quelle in concessione, di costo complessivo superiore a 500 milioni di euro, prima dell'approvazione del progetto di fattibilità o, per quelle in corso di istruttoria, prima della deliberazione del CIPESS. La valutazione non sospende i procedimenti già autorizzati.
>
> **Art. 3 (Contenuto e termini).** La valutazione comprende l'analisi costi-benefici, il confronto con almeno due alternative, l'analisi di resilienza agli scenari demografici dell'ISTAT e agli scenari climatici, e i costi di gestione per trent'anni. È resa entro sei mesi dalla richiesta ed è pubblicata insieme ai modelli e ai dati in formato aperto.
>
> **Art. 4 (Decisione motivata).** L'amministrazione può procedere anche in caso di valutazione negativa, previa deliberazione motivata del Consiglio dei ministri trasmessa alle Camere, che indica le ragioni della scelta e il costo-opportunità.
>
> **Art. 5 (Indipendenza).** Il responsabile dell'Ufficio è nominato dai Presidenti delle Camere, d'intesa, su proposta del Consiglio dell'UPB, con il parere favorevole delle Commissioni competenti a maggioranza dei due terzi.
>
> **Art. 6 (Copertura finanziaria).** Agli oneri, pari a 15 milioni di euro nel 2027 e a 25 milioni annui dal 2028, si provvede mediante corrispondente riduzione delle autorizzazioni di spesa per studi, consulenze e progettazione dello stato di previsione del Ministero delle infrastrutture e dei trasporti.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| 100 giorni | Disegno di legge approvato dal CdM; elenco pubblico delle opere oltre 500 mln in istruttoria | MIT, MEF, Presidenza del Consiglio |
| 12 mesi | Legge approvata; Ufficio operativo; prime 3 valutazioni, compreso il Ponte sullo Stretto se ancora in istruttoria | Parlamento, UPB |
| Fine legislatura | Tutte le opere sopra soglia valutate; primo rapporto sugli scostamenti di costi e tempi | UPB, ANAC, Corte dei conti |

**Indicatori**

| KPI | Base | Obiettivo a 3 anni | a 5 anni |
|---|---|---|---|
| Nuove opere oltre 500 mln con valutazione indipendente pubblica | 0% (nessun obbligo, 2026) | 100% | 100% |
| Scostamento medio dei costi finali dalle previsioni (opere oltre 500 mln) | da misurare (banca dati ANAC/BDAP, primo rapporto a 12 mesi) | −20% rispetto alla base | −33% |
| Decisioni del CdM motivate pubblicamente dopo una valutazione negativa | non applicabile | 100% | 100% |

**Rischi e mitigazioni.** *Un nuovo veto burocratico* → termine massimo di 6 mesi; la decisione finale resta politica. *Indipendenza* → nomina parlamentare a maggioranza qualificata. *Penali sui contratti in corso* → la valutazione stima anche il costo di recesso. *Percezione di un attacco al Sud (Ponte)* → le alternative valutate includono sempre opere nello stesso territorio (ferrovie siciliane e calabresi, traghettamento).

---

## 04-P5 — LEP prima: autonomia differenziata reversibile

**Problema in un dato.** Il costo del finanziamento integrale dei LEP **non ha una quantificazione ufficiale** (nessuna stima RGS, UPB o CTFS: verifica 04, novembre 2026). Le stime pubbliche vanno **da 17 a 100 mld €/anno**, secondo l'intervallo riportato dal Ministro per gli Affari regionali in risposta a un'interrogazione; SVIMEZ indica 80 mld. Intanto le aree interne del Mezzogiorno passerebbero da **7,1 a 6,0 milioni di abitanti nel 2050** (ISTAT, previsioni agosto 2026; serie `04_istat_previsioni_aree_interne`).

**Ordine di grandezza (stima GovernAI).** Il costo dipende dal perimetro. Le stime più alte includono sanità e istruzione per intero, che hanno già standard nazionali (LEA, organici). Per i LEP non sanitari con il divario più grande (servizi sociali comunali, tempo pieno nella primaria al Sud, trasporto e assistenza scolastica per gli alunni con disabilità) la stima è **3-8 mld/anno a regime**, da raggiungere in un percorso di convergenza decennale. Il primo prodotto della riforma è proprio la cifra ufficiale.

**Soluzione.** Nessuna intesa su materie LEP prima che i LEP siano quantificati con i fabbisogni standard e finanziati su tutto il territorio. Le intese su materie non-LEP durano 10 anni, hanno una valutazione quinquennale e una clausola di rientro. Il voto del Parlamento sulle intese diventa vincolante. Un Fondo di convergenza avvia il percorso.

| Variante | Contenuto | 2027 | 2028 | 2029 | Intensità | Fondi a regime |
|---|---|---|---|---|---|---|
| PIENA | Metodo + Fondo di convergenza LEP fino a 1 mld nel 2029 | 0,005 | 0,5 | 1,0 | 1 | SPESE_FISCALI 0,6; RIALLOCAZIONE 0,4 |
| ESSENZIALE | Metodo + Fondo 0,5 mld su 2 ambiti già definiti | 0,005 | 0,25 | 0,5 | 0,7 | SPESE_FISCALI 0,3; RIALLOCAZIONE 0,2 |
| ZERO | Solo metodo: quantificazione, LEP prima, reversibilità, voto vincolante | 0 | 0 | 0 | 0,45 | — |

**Articolato normativo essenziale** (disegno di legge di modifica della L. 86/2024 e decreto legislativo sui LEP)

> **Art. 1 (Finalità).** In attuazione degli articoli 3, 5, 116, terzo comma, 117, secondo comma, lettera m), e 119 della Costituzione, e in conformità alla sentenza della Corte costituzionale n. 192 del 2024, la presente legge subordina l'attribuzione di ulteriori forme di autonomia alla previa determinazione, quantificazione e copertura dei livelli essenziali delle prestazioni su tutto il territorio nazionale.
>
> **Art. 2 (Quantificazione).** Entro dodici mesi, con decreto legislativo, sono determinati per ciascuna materia i LEP, i relativi costi e fabbisogni standard e il fabbisogno finanziario aggiuntivo per Regione, sulla base dell'istruttoria della Commissione tecnica per i fabbisogni standard, validata dall'Ufficio parlamentare di bilancio. La quantificazione è pubblicata con i dati e i modelli.
>
> **Art. 3 (Clausola LEP prima).** Nessuna intesa ai sensi dell'articolo 116, terzo comma, della Costituzione può riguardare materie o funzioni riferibili ai LEP prima che la legge di bilancio abbia assicurato il loro finanziamento integrale o un percorso di convergenza pluriennale coperto.
>
> **Art. 4 (Durata, valutazione e rientro).** Le intese hanno durata massima di dieci anni. Ogni cinque anni un osservatorio indipendente presso la CTFS valuta, materia per materia, gli indicatori di qualità dei servizi. Se gli indicatori peggiorano rispetto alla media nazionale per due rilevazioni consecutive, si attiva la procedura di rientro della funzione allo Stato.
>
> **Art. 5 (Ruolo del Parlamento).** Lo schema di intesa è approvato dalle Camere con legge, a maggioranza assoluta dei componenti, previa relazione tecnica che dimostri per ciascuna funzione l'adeguatezza e l'assenza di effetti negativi sulla perequazione.
>
> **Art. 6 (Fondo di convergenza e copertura).** È istituito il Fondo per la convergenza dei LEP, con una dotazione di 0,5 miliardi nel 2028 e di 1 miliardo dal 2029, ripartito in base al divario dai fabbisogni standard (variante ESSENZIALE: 0,25 e 0,5 miliardi). Agli oneri si provvede mediante riduzione delle spese fiscali di cui all'allegato X e delle autorizzazioni di spesa di cui all'allegato Y. Nella variante ZERO la legge non comporta nuovi o maggiori oneri: le amministrazioni provvedono con le risorse umane, strumentali e finanziarie disponibili.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| 100 giorni | Disegno di legge approvato dal CdM; sospensione dell'esame delle intese sulle materie LEP; mandato alla CTFS per la quantificazione | Ministro Affari regionali, MEF, CTFS, Conferenza Stato-Regioni |
| 12 mesi | Decreto legislativo con la quantificazione ufficiale; intese non-LEP (Liguria, Lombardia, Piemonte, Veneto) riesaminate con clausola decennale e relazione per materia | Governo, Parlamento, UPB, CTFS |
| Fine legislatura | Fondo di convergenza a regime; prima valutazione delle intese; percorso decennale coperto nella programmazione di bilancio | Osservatorio LEP, Corte dei conti |

**Indicatori**

| KPI | Base | Obiettivo a 3 anni | a 5 anni |
|---|---|---|---|
| Materie LEP con costo quantificato e pubblicato | 0 (nessuna quantificazione ufficiale, 2026) | 100% delle materie | 100%, aggiornate |
| Intese con relazione tecnica per materia e clausola di rientro | 0 su 4 schemi (CdM 18.2.2026) | 100% | 100% |
| Quota del fabbisogno LEP aggiuntivo finanziata | 0% | 15-30% dei LEP non sanitari (PIENA) | 30-40% |

**Rischi e mitigazioni.** *Percezione di un "blocco" dell'autonomia* → le materie non-LEP procedono con un calendario chiaro. *LEP definiti al ribasso per contenere i costi* → validazione dell'UPB e parere della Corte dei conti. *Costo che supera le coperture disponibili* → percorso di convergenza decennale e scelta esplicita ogni anno in legge di bilancio. *Contenzioso costituzionale* → la relazione per materia applica la sentenza 192/2024.

---

## 04-P6 — Restare è possibile: servizi essenziali nelle aree interne

**Problema in un dato.** Gli abitanti delle aree interne scenderebbero da **13,3 milioni nel 2025 a 11,8 nel 2050**. Nel Mezzogiorno il calo è da 7,1 a 6,0 milioni, mentre nel Nord è di 122.000 (ISTAT, previsioni base 1.1.2025, agosto 2026; serie `04_istat_previsioni_aree_interne`).

**Soluzione.** Contratti di area tra Stato, Regione e unione di Comuni con obiettivi di servizio misurati: tempi di accesso a pronto soccorso, scuola secondaria e stazione. Presidi multiservizio sul modello France Services (quasi 2.900 strutture in Francia), indennità di sede disagiata per chi resta almeno 5 anni, trasporto a chiamata, scuole in rete e telemedicina. Gestione associata obbligatoria per i Comuni sotto i 3.000 abitanti.

| Variante | Contenuto | 2027 | 2028 | 2029 | Intensità | Fondi a regime |
|---|---|---|---|---|---|---|
| PIENA | 1.000 presidi; indennità per circa 70.000 tra medici, infermieri e insegnanti; trasporto a chiamata; gestione associata obbligatoria | 0,40 | 0,65 | 0,80 | 1 | COESIONE 0,35; RIALLOCAZIONE 0,20; SPESE_FISCALI 0,17; SAD 0,08 |
| ESSENZIALE | 72 aree progetto SNAI; 500 presidi; indennità per circa 35.000 persone nei comuni periferici e ultraperiferici | 0,20 | 0,33 | 0,42 | 0,6 | COESIONE 0,20; RIALLOCAZIONE 0,12; SPESE_FISCALI 0,06; SAD 0,04 |
| PILOTA | 10 contratti di area (almeno 6 al Sud) con valutazione a 3 anni | 0,05 | 0,08 | 0,10 | 0,15 | COESIONE 0,06; RIALLOCAZIONE 0,04 |

**Articolato normativo essenziale** (legge di bilancio e accordo Stato-Regioni)

> **Art. 1 (Finalità).** Al fine di garantire ai residenti delle aree interne l'accesso ai servizi essenziali di istruzione, salute, mobilità e connettività, la Strategia nazionale per le aree interne è dotata di risorse pluriennali ed è attuata mediante contratti di area con obiettivi di servizio misurabili.
>
> **Art. 2 (Contratti di area).** Lo Stato, la Regione e l'unione o associazione dei Comuni di ciascuna area stipulano un contratto di area che fissa, per un periodo di cinque anni, gli obiettivi relativi ai tempi di accesso ai servizi, le azioni, le risorse e gli indicatori. L'erogazione delle quote successive alla prima è subordinata al raggiungimento degli obiettivi intermedi.
>
> **Art. 3 (Presidi multiservizio).** Nei Comuni polo di area sono istituiti presidi multiservizio che offrono in un unico punto i servizi delle amministrazioni statali, dell'INPS, dell'Agenzia delle entrate e dei servizi postali e digitali, con un operatore formato e collegamenti in telemedicina con il distretto sanitario.
>
> **Art. 4 (Personale).** Al personale del Servizio sanitario nazionale, della scuola e delle amministrazioni statali che presta servizio continuativo per almeno cinque anni nei comuni classificati periferici e ultraperiferici è riconosciuta un'indennità di sede disagiata, definita in sede di contrattazione collettiva entro il limite di spesa di cui all'articolo 6, e un punteggio aggiuntivo nelle procedure di mobilità e di carriera.
>
> **Art. 5 (Gestione associata).** I Comuni con popolazione inferiore a 3.000 abitanti esercitano in forma associata le funzioni fondamentali entro tre anni. Ai Comuni che si fondono è riconosciuto un contributo straordinario decennale.
>
> **Art. 6 (Copertura finanziaria).** Agli oneri di parte corrente, pari a 0,45 miliardi annui a regime (variante ESSENZIALE: 0,22), si provvede mediante riduzione delle autorizzazioni di spesa di cui all'allegato Y, delle spese fiscali di cui all'allegato X e dei sussidi ambientalmente dannosi di cui all'allegato Z. Agli investimenti si provvede nei limiti delle risorse dei programmi della politica di coesione 2021-2027 destinate alle strategie territoriali.

**Cronoprogramma**

| Fase | Cosa | Chi |
|---|---|---|
| 100 giorni | Norma in legge di bilancio; accordo Stato-Regioni sullo schema di contratto di area; rilevazione di base dei tempi di accesso | Dipartimento coesione, Ministro Affari regionali, Conferenza Stato-Regioni, ISTAT |
| 12 mesi | Primi 30 contratti firmati; 200 presidi aperti; indennità in vigore nei contratti collettivi | Regioni, unioni di Comuni, Salute, Istruzione, Funzione pubblica, ARAN |
| Fine legislatura | Tutti i contratti di area attivi; 1.000 presidi (PIENA); fusioni e gestioni associate completate; valutazione controfattuale | Comitato tecnico aree interne, ISTAT, UPB |

**Indicatori**

| KPI | Base | Obiettivo a 3 anni | a 5 anni |
|---|---|---|---|
| Presidi multiservizio attivi | 0 (2026) | 600 | 1.000 |
| Tempo medio di accesso al pronto soccorso e alla scuola secondaria nei comuni periferici e ultraperiferici | rilevazione di base ISTAT/SNAI entro 100 giorni | −15% | −25% |
| Popolazione delle aree interne del Mezzogiorno rispetto alla previsione ISTAT | previsione mediana: da 7,1 mln (2025) a 6,0 mln (2050) | sopra la traiettoria mediana | sopra la traiettoria mediana di almeno 0,5 punti |

**Rischi e mitigazioni.** *Dispersione delle risorse* → concentrazione sui Comuni polo e quote erogate per obiettivi. *Personale che non accetta gli incarichi* → indennità, punteggio e alloggi di servizio dalle ASA (sinergia con 04-P2). *Resistenza alla gestione associata* → contributo alle fusioni e tempi di tre anni. *Aspettative di inversione demografica* → obiettivi espressi in qualità dei servizi; la popolazione è solo un indicatore di contesto. *Fine della coesione 2021-27 nel 2029* → gli investimenti successivi passano al ciclo 2028-34 (COESIONE_2834).

---

### Fonti dei dati usati

Serie in `dati/serie/04_*.csv` (Eurostat `ilc_lvho07c`, `road_eqs_carhab`, `env_air_gge`, `prc_hicp_aind`, `prc_hpi_a`; Corte dei conti Doc. XIII-bis n. 7; ISTAT previsioni agosto 2026; Cohesion Open Data), verifica in `dati/verifiche/04_infrastrutture.md`. Intervallo delle stime sul costo dei LEP: [Il Post, 7.12.2024](https://www.ilpost.it/2024/12/07/autonomia-differenziata-lep-risorse-coperture-corte-costituzionale-sentenza/); [Il Post, 19.11.2023](https://www.ilpost.it/2023/11/19/autonomia-differenziata-regioni-calderoli-lep-giorgetti/); [UPB, Audizione LEP 22.1.2026](https://www.upbilancio.it/wp-content/uploads/2026/01/CS_Audizione-LEP_22_01_2026.pdf). Sono fonti secondarie da verificare sull'atto parlamentare originale.
