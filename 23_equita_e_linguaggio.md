# GovernAI — Equità e linguaggio inclusivo

*Capitolo del programma, scritto il 9 novembre 2026 e aggiornato il 12 e il 13 novembre 2026 dopo le scelte sulla sanità, sui bandi e sulla disabilità. Scenario di riferimento: intermedio (`programma/selezione_intermedio.md`), 9,4 mld l'anno. Tutti i numeri vengono da file del repository, con la fonte indicata. Dove un dato manca, lo scriviamo: "dato da acquisire".*

## In breve

- L'equità per GovernAI è un **criterio di valutazione**: ogni proposta deve dire chi guadagna e chi perde, per reddito, territorio, genere, età, disabilità e origine.
- In Italia i divari più grandi sono tra **territori**, tra **chi ha un lavoro stabile e chi no**, tra **famiglie italiane e straniere** e tra **persone con e senza disabilità**.
- Il programma intermedio interviene su quasi tutti i divari, ma spesso in **versione ridotta o sperimentale**. Lo diciamo in modo esplicito.
- Dal 13 novembre il **progetto di vita per le persone con disabilità** (02-C5) passa dalla sola riforma del collocamento a un pilota con personale e budget nel quarto degli ambiti con meno servizi, pagato con fondi europei fino al 2029 e senza togliere risorse ad altre misure.
- Dal 12 novembre entrano le **Case della Comunità** e le **squadre infermieristiche di quartiere**, che aiutano soprattutto chi vive lontano dai servizi e chi è anziano o fragile. Il prezzo è un gradino in meno su due misure di scuola con forte effetto sull'equità (ITS e scuole aperte): **l'equità non guadagna in assoluto, si sposta dalla scuola alla salute**.
- Circa il 30% del gettito delle coperture (2,3 mld su 7,4) viene da prelievi **regressivi**, cioè che pesano di più su chi ha meno. Alcuni sono compensati, altri no. La scelta di non aggiungere tasse non ha cambiato questa quota.
- Non abbiamo ancora una **microsimulazione per decili di reddito**. Senza, nessun giudizio sull'equità complessiva è definitivo.
- Proponiamo **cinque regole di metodo** a costo quasi zero e **undici indicatori di divario**.
- Proponiamo regole di **linguaggio chiaro e inclusivo** per lo Stato, e le applichiamo per prime in questo testo.

---

## 1. Perché l'equità è un criterio, non un'etichetta

### Che cosa intende la Carta

La Carta dei valori (`01_carta_valori.md`, versione 2.0) contiene due valori che riguardano direttamente l'equità.

- **Equità (EQU).** Pari opportunità reali e una distribuzione giusta di costi e benefici tra persone e territori. Chi parte svantaggiato deve poter recuperare. Chi ha di più contribuisce in proporzione. La domanda chiave è: *chi guadagna e chi perde, per reddito, territorio, genere ed età?*
- **Rispetto e diversità (RIS).** La dignità di ogni persona e il rispetto per le differenze di origine, genere, orientamento, religione, disabilità, età, condizione sociale e territorio. La domanda chiave è: *la proposta funziona per persone diverse, o solo per il cittadino "medio"?*

L'equità tra generazioni sta in un terzo valore, **Responsabilità verso il futuro (FUT)**, che chiede: *chi paga, e quando?*

### Le linee rosse

- **EQU:** nessuna proposta che sposti i costi su chi ha meno mezzi senza compensazione (art. 3, comma 2, e art. 53 Cost.).
- **RIS:** nessuna proposta che violi i diritti fondamentali (artt. 2 e 3 Cost., Carta dei diritti fondamentali dell'Unione europea), anche se migliora gli altri valori.

### La regola sulle coperture regressive

Il motore decisionale esclude in automatico le coperture con un punteggio di equità pari o inferiore a −2 se non hanno una compensazione. Nello scenario intermedio questa regola ha escluso due coperture:

- **AS05**, un ulteriore aumento delle accise sul tabacco;
- **RB05**, il taglio completo del bonus per le lavoratrici madri, che avrebbe tolto circa 1.200 euro l'anno a madri con redditi medio-bassi.

Le coperture con punteggio −1 restano ammesse. Le analizziamo nella sezione 4.

### Opportunità e risultato, in parole semplici

- **Equità di opportunità**: tutte le persone partono con possibilità simili. Esempio: un posto al nido o una buona scuola, ovunque si nasca.
- **Equità di risultato**: le differenze finali, come reddito, salute e casa, non diventano troppo grandi. Esempio: un reddito minimo per chi resta indietro.

GovernAI non sceglie una delle due. Le misura entrambe. Quanto peso dare all'una o all'altra è una scelta politica, e la lasciamo alle persone (sezione 8).

---

## 2. Le disuguaglianze che contano in Italia, con i dati

### 2.1 Reddito e povertà

| Indicatore | Valore | Fonte |
|---|---|---|
| Persone in povertà assoluta | **5,4 milioni (9,3%)**, 2025 | ISTAT, *La povertà in Italia 2025* (`dati/serie/02_cifre_puntuali_documenti.csv`) |
| Minorenni in povertà assoluta | **1,136 milioni (12,5%)**, 2025 | idem |
| Famiglie operaie in povertà assoluta | **14,3%**, 2025 | idem |
| Persone occupate a rischio di povertà | **10,2%** (UE 8,3%), 2025; **18,8%** tra chi lavora in proprio | Eurostat `ilc_iw01` (`02_working_poor.csv`) |
| Retribuzioni contrattuali orarie reali | **−10,2%** rispetto a gennaio 2021, settembre 2026 | ISTAT e HICP, elaborazione GovernAI (`dati/verifiche/02_lavoro.md`) |
| Indice di Gini, rapporto tra quintili | **dato da acquisire** | — |

I minorenni sono la fascia più povera. Lavorare non basta sempre a uscire dalla povertà.

### 2.2 Territorio: Mezzogiorno e aree interne

| Indicatore | Valore | Fonte |
|---|---|---|
| Posti al nido ogni 100 bambine e bambini sotto i 3 anni | **Sud 19,0**, Isole 19,5, Centro 40,4, Italia 31,6 (2023/24) | ISTAT, *Offerta di nidi* (`dati/verifiche/02_lavoro.md`) |
| Giovani 18-24 che lasciano presto la scuola | **Isole 13,7%**, Nord-Ovest 7,0%, Italia 8,2% (2025) | Eurostat `edat_lfse_16` (`05_elet_18_24_nuts1.csv`) |
| Giovani 15-29 che non studiano e non lavorano (NEET) | **Sicilia 22,8%**, Lombardia 8,5%, Italia 13,3% (2025) | Eurostat (`02_neet_15_29_regioni.csv`) |
| Abitanti delle aree interne | **13,3 milioni** nel 2025; nel Mezzogiorno da 7,1 a **6,0 milioni** nel 2050 | ISTAT, previsioni base 1/1/2025 (`04_istat_previsioni_aree_interne.csv`) |
| Povertà assoluta per ripartizione | **dato da acquisire** nel repository | — |

Il divario territoriale si vede già nei primi anni di vita: al Sud i posti al nido sono meno della metà che al Centro.

### 2.3 Genere

| Indicatore | Valore | Fonte |
|---|---|---|
| Donne 20-64 anni occupate | **58,0%** (UE 71,3%), 2025 | Eurostat `lfsi_emp_a` (`02_tasso_occupazione.csv`) |
| Occupazione totale 20-64 | 67,6%, 2025 | idem |
| Tasso di occupazione degli uomini 20-64 | **dato da acquisire** (non è nella serie del repository) | — |
| Divario retributivo di genere (gender pay gap) | **dato da acquisire** | — |
| Ore di lavoro di cura non pagato, per genere | **dato da acquisire** | — |
| Padri che usano il congedo di paternità | **dato da acquisire** (INPS) | `apprendimento/obiettivi.yaml`, 02-C2-d |

Il divario con le donne europee è di oltre 13 punti. Mancano nel repository i dati su salari e lavoro di cura. È una lacuna da colmare subito.

### 2.4 Generazioni

| Indicatore | Valore | Fonte |
|---|---|---|
| Debito pubblico | **3.097 miliardi**, 136,7% del PIL, 2025 | Eurostat (`01_debito_mio_eur.csv`; `dati/verifiche/02_lavoro.md`) |
| Spesa per pensioni | **15,2% del PIL** nel 2025; picco **17,1%** nel 2041-2044 | RGS, aggiornamento 2026 (`02_cifre_puntuali_documenti.csv`) |
| Persone con 65 anni e più ogni 100 in età da lavoro | da **39** (2025) a **63** (2050) | Eurostat, proiezioni (`02_dipendenza_proiezioni.csv`) |
| NEET 15-29 | **13,3%** (UE 11,0%), 2025 | Eurostat `edat_lfse_20` |
| Saldo migratorio delle persone laureate 25-34 | circa **−13.000 l'anno** (2019-2024) | ISTAT, agosto 2026 (`obiettivi.yaml`, 05-C3-c) |

Ogni generazione giovane è più piccola e trova un debito più alto. È un divario di risorse, non di colpe.

### 2.5 Disabilità

| Indicatore | Valore | Fonte |
|---|---|---|
| Persone con limitazioni gravi | **2,9 milioni**, 2023 | ISTAT, 3/12/2025 (`dati/verifiche/02_lavoro.md`) |
| Divario di occupazione tra persone con limitazioni gravi e le altre | **43,4 punti** (UE 46,1), 2025 | Eurostat `tepsr_sp200` (`02_divario_occupazione_disabilita.csv`) |
| Occupazione 15-64 con limitazioni gravi | **32,5%** contro 58,9%, dato 2021 | ISTAT |

Una persona con disabilità grave ha circa la metà delle probabilità di lavorare rispetto alle altre persone.

### 2.6 Origine e cittadinanza

| Indicatore | Valore | Fonte |
|---|---|---|
| Residenti con cittadinanza straniera | circa **5,37 milioni** (1,37 UE + 4,00 extra UE), 2025 | Eurostat (`07_residenti_per_cittadinanza.csv`) |
| Occupati con cittadinanza straniera | **2,58 milioni** su 24,05 (10,7%), 2025 | Eurostat (`07_occupati_per_cittadinanza.csv`) |
| Povertà assoluta, famiglie di sole persone straniere | **29,4%**, contro **5,9%** delle famiglie di sole persone italiane, 2025 | ISTAT (`02_cifre_puntuali_documenti.csv`) |
| Tasso di occupazione per cittadinanza | **dato da acquisire** | — |

È il divario più ampio tra quelli misurati: la povertà assoluta è cinque volte più frequente.

### 2.7 Salute, casa e altre fragilità

| Indicatore | Valore | Fonte |
|---|---|---|
| Persone che rinunciano a cure per costo, distanza o attesa | **2,5%** in media, **4,4%** nel quinto più povero, 2025 | Eurostat `hlth_silc_08` (`benchmark/confronto.md`) |
| Spesa per la casa oltre il 40% del reddito | **22,3%** di chi è in affitto a prezzo di mercato, contro **5,0%** del totale, 2025 | Eurostat (`04_sovraccarico_costo_abitativo_per_titolo.csv`) |
| Persone senza dimora iscritte in anagrafe | **96.197**, 2021 | ISTAT (`programma/schema.yaml`) |
| Persone detenute | **66.063** per 51.295 posti, 30/9/2026 | DAP (`07_detenuti_dap.csv`) |

Chi ha meno rinuncia alle cure quasi il doppio della media. Chi è in affitto paga la casa molto di più di chi è proprietario.

---

## 3. Che cosa fa il programma, divario per divario

Legenda delle versioni (dal file `programma/selezione_intermedio.md`):
- **PIENA**: misura completa;
- **ESSENZIALE**: misura ridotta;
- **ZERO**: solo regole, senza spesa;
- **PILOTA**: sperimentazione limitata;
- **FUORI**: non inclusa per mancanza di coperture.

| Divario | Misure nel programma | Versione | Onestà sui limiti |
|---|---|---|---|
| **Povertà** | 02-C4 Reddito di inclusione universale | PILOTA (12 ambiti) | Per ora nessun cambiamento generale per 5,4 milioni di persone |
| | 02-C7 Housing First dopo il PNRR | ESSENZIALE | Circa 6.000 persone senza dimora in casa, su 96.197 |
| | 02-C1 Salario minimo contrattuale | ZERO | Solo regole: nessuna soglia di legge, nessuna nuova ispezione |
| | 04-P2 Casa a canone giusto | FUORI | Il divario dell'affitto resta senza risposta |
| **Territorio** | 04-P6 Servizi essenziali nelle aree interne | ESSENZIALE | 500 presidi e indennità per circa 35.000 persone tra personale medico, infermieristico e docente |
| | 05-C1 Squadre contro la dispersione; 05-C7 Quota svantaggio alle scuole | PIENA; ESSENZIALE | Risorse alle scuole più fragili, molte al Sud |
| | 05-C5 Scuole aperte come presidi di comunità | ESSENZIALE | Scesa da piena il 12 novembre per far posto alla sanità: restano le circa 1.500 scuole del quinto più fragile, si perdono le altre 1.500 |
| | 09-C3 Squadre tecniche della Repubblica per i piccoli Comuni | ESSENZIALE | Aiuto mirato a Mezzogiorno e aree interne |
| | 04-P5 LEP prima dell'autonomia differenziata | ZERO | Regole sui livelli essenziali; il fabbisogno aggiuntivo non è finanziato |
| | 03-P3 Reti idriche | ESSENZIALE | 5 regioni perdono oltre metà dell'acqua |
| | 04-P3 Treni per pendolari | FUORI | |
| | 09-C10 Bandi pubblici con istruttoria assistita | PILOTA (10 bandi) | Domande più semplici per piccoli Comuni e imprese senza consulenti; utile alle Regioni in ritardo di spesa dei fondi europei, se aderiscono |
| **Genere** | 02-C2 Nido esigibile e congedo paterno | ESSENZIALE | 60-70 mila posti in più, gratis fino a ISEE 25.000 euro; 2 mesi ai padri invece di 3 |
| | 02-C6 Bilancio generazionale e strategia demografica | ZERO | Obiettivi su occupazione femminile, senza spesa |
| | 06-C4 Budget di cura per la non autosufficienza | PILOTA | Il lavoro di cura pesa soprattutto sulle donne: solo 20 ambiti |
| **Generazioni** | 01-P1 Bilancio generazionale; 02-C3 Patto previdenziale | ZERO | Trasparenza su chi paga e quando |
| | 05-C4 Più persone laureate e ITS | ESSENZIALE | Scesa da piena il 12 novembre: borsa garantita resta, crescono meno i posti ITS e le residenze |
| | 05-C2 Conto personale di competenze | ESSENZIALE | Dote di 900 euro per adulti |
| **Disabilità** | 02-C5 Progetto di vita e lavoro | PILOTA (dal 13 novembre) | Collocamento mirato con banca dati e sanzioni ovunque; personale e budget di progetto solo nel quarto degli ambiti con meno servizi, fino al 2029: negli altri il progetto di vita resta senza risorse aggiuntive |
| **Origine** | 07-C3 Governance dei flussi fondata sui dati | ESSENZIALE | Più orientata a ingressi e rimpatri che all'inclusione |
| | 05-C1 Mediatori nelle scuole fragili | PIENA | Effetto indiretto |
| | Misura specifica per l'inclusione lavorativa delle persone straniere | assente | **Lacuna del programma** |
| **Salute** | 06-C1 Tempo garantito; 06-C6 Prevenzione | ZERO | Nessun rimborso automatico in questo scenario |
| | 06-C3 Case della Comunità vive | ESSENZIALE | Entrata il 12 novembre: servizi di base vicino a casa, utili soprattutto nelle aree con pochi servizi |
| | 06-C8 Squadre infermieristiche di quartiere | ESSENZIALE (500 squadre) | Priorità alle Regioni con meno ore di assistenza a domicilio per assistito |
| | 06-C10 Meno burocrazia, più cura | ESSENZIALE | Amministrativi verso l'accoglienza nelle Case della Comunità, su base volontaria |
| | 06-C9 Benessere a scuola | PILOTA | |
| | 06-C2 Personale infermieristico e medicina di famiglia | PILOTA (dal 13 novembre) | 4 Regioni, almeno 2 del Mezzogiorno, e aree interne: indennità di area disagiata, borse di studio, infermiere di pratica avanzata |
| | 06-C5 Salute mentale | FUORI | Resta la lacuna più grande della missione salute |
| **Persone detenute** | 07-C2 Pena utile: misure di comunità | ESSENZIALE | Obiettivo: affollamento da 128,8% a 105% in 5 anni |

### Il bilancio onesto

- **Pieno** dove l'equità passa dalla scuola più fragile: squadre contro la dispersione.
- **Ridotto** dove servono molti soldi: nidi, aree interne, Housing First, ITS e scuole aperte, Case della Comunità e cure a domicilio.
- **Sperimentale** dove l'incertezza è alta: povertà, non autosufficienza, bandi con istruttoria assistita.
- **Fuori** su casa, trasporto di chi viaggia ogni giorno, nuovo personale sanitario e salute mentale.
- **Lacune vere**: inclusione lavorativa delle persone straniere, divario salariale di genere, progetto di vita per le persone con disabilità.

### Le scelte del 12 novembre, viste dall'equità

Per far entrare la sanità **senza tasse in più oltre quelle già previste**, alcune misure sono scese di un gradino. Il conto, con i punteggi di equità del panel (EQU, media dei tre valutatori, da −3 a +3):

| Che cosa cambia | Spesa (mld) | EQU | Spesa × EQU | Effetto sull'equità |
|---|---|---|---|---|
| Entra 06-C3 Case della Comunità (essenziale) | +0,80 | +1,7 | +1,34 | Servizi di base vicino a casa, soprattutto dove oggi mancano |
| 06-C8 Squadre di quartiere da pilota a essenziale | +0,08 | +0,7 | +0,05 | Più ore di assistenza a casa nelle Regioni più indietro |
| Entrano 06-C10 (essenziale) e 09-C10 (pilota) | +0,03 | +0,3; +0,7 | +0,01 | Effetti indiretti: più accoglienza, domande di contributo più semplici |
| 05-C4 ITS e lauree professionalizzanti da piena a essenziale | −0,40 | +2,0 | −0,80 | Meno posti ITS e residenze per chi studia dopo il diploma; la borsa garantita resta |
| 05-C5 Scuole aperte da piena a essenziale | −0,20 | +1,7 | −0,33 | Restano aperte le circa 1.500 scuole del quinto più fragile; si perdono le altre 1.500 |
| 05-C10, 01-P12, 01-P2, 08-P7 scendono di un gradino | −0,19 | da +0,3 a +1,3 | −0,09 | Ricerca applicata, riscossione, agevolazioni a scadenza, appalti trasparenti |
| 01-P14, 01-P15, 04-P7, 04-P8, 08-P2 scendono di un gradino | −0,28 | da −0,3 a 0 | +0,04 | Effetto sull'equità nullo o lievemente positivo |

**Bilancio**: sommando spesa per punteggio, il guadagno (circa +1,4) supera di poco la perdita (circa −1,2). L'equità complessiva resta quindi all'incirca la stessa, con un leggero vantaggio, ma cambia chi ne beneficia: più le persone anziane, fragili e chi vive lontano dai servizi; meno chi studia dopo il diploma e le scuole fragili fuori dal quinto più svantaggiato. È una scelta politica, e la dichiariamo. Le scuole più svantaggiate restano protette da 05-C1 (piena), 05-C7 e 05-C5 (essenziali). Il calcolo è indicativo: i punteggi EQU sono giudizi qualitativi, non misure.

---

## 4. Chi paga: l'equità delle coperture

Lo scenario intermedio attiva coperture per un gettito minimo di **7,42 miliardi** l'anno a regime. Le abbiamo classificate con il punteggio EQU del panel (colonna `EQU` in `programma/selezione_intermedio.csv`) e con la colonna `chi_paga`. Le somme sono un nostro calcolo sul file.

### Coperture progressive (pesano di più su chi ha di più): circa 1,5 miliardi

| Codice | Chi paga | Gettito min. (mld) | EQU |
|---|---|---|---|
| SF06 | Detrazione sanitaria decrescente tra 50.000 e 120.000 euro di reddito (salve disabilità, malattie croniche gravi, non autosufficienza) | 0,35 | +2 |
| SF07 | Persone iscritte ai fondi sanitari con reddito oltre 75.000 euro | 0,08 | +2 |
| PE04 | Pensioni oltre circa 3.700 euro lordi al mese (rivalutazione ridotta sulla sola quota alta) | 0,30 | +1 |
| SF02 | Forfettari con ricavi tra 50.000 e 85.000 euro | 0,20 | +1 |
| SAD05 | Auto aziendali a combustione | 0,15 | +1 |
| SAD03 | Passeggeri dei voli nazionali, escluse le rotte di continuità con le isole | 0,12 | +1 |
| RB02, RB01 | Bonus nuovi nati e Carta Valore solo sotto una soglia ISEE | 0,13 | +1 |
| SF03, SF08, SF09, RA10, FN04 | Armatori, detrazione per lo sport dei ragazzi oltre una soglia di reddito, seconde case, grandi litiganti, premi di produttività oltre 50.000 euro | 0,19 | +1 |

### Coperture neutre o non classificabili: circa 3,6 miliardi

Tagli di spesa dei ministeri (RA13, RA01-RA09), riordino degli incentivi alle imprese (RA14, RA04), patent box (SF16), detrazioni per polizze vita e animali (FN02). L'effetto distributivo dipende da **quali programmi** si tagliano. Per RA13 la colonna `chi_paga` dice: "da individuare". È un rischio: un taglio lineare può colpire servizi usati da chi ha meno.

### Coperture regressive (pesano di più su chi ha meno): circa 2,3 miliardi, il 30%

| Codice | Chi paga | Gettito min. (mld) | Compensazione prevista |
|---|---|---|---|
| AS01 | Circa 10 milioni di persone che fumano (+0,50 euro a pacchetto) | 0,60 | **Nessuna dedicata** |
| AS02 | Chi usa tabacco riscaldato e sigarette elettroniche | 0,15 | Nessuna dedicata |
| AS03 | Chi consuma bevande zuccherate | 0,15 | Nessuna dedicata |
| SAD13, SAD01 | Autotrasporto e agricoltura; in parte chi consuma, tramite i prezzi | 1,10 | Fondi per il rinnovo delle flotte (circa 0,4-0,55 mld) |
| SAD02 | Aziende agricole che usano gasolio agevolato | 0,15 | Credito per piccole aziende e montagna |
| SAD10 | Famiglie in montagna e nelle isole che si scaldano a gasolio o GPL | 0,02 | Contributo per pompe di calore; salvaguardia per ISEE fino a 15.000 euro |
| RP01 | Giovani candidate e candidati ai concorsi generici, soprattutto al Sud | 0,04 | Esclusi servizi sociali e sportelli; ritorno al 100% se i tempi dei servizi peggiorano |
| RP08 | Giovani candidate e candidati ai concorsi amministrativi della sanità (dal 12 novembre) | 0,05 | Esclusi sportelli e profili tecnici; risorse destinate a infermieri e Case della Comunità; ritorno al 100% se i servizi peggiorano |

Tra le coperture neutre c'è anche **RB03**: la soglia del bonus per le lavoratrici madri scende da 40.000 a 32.000 euro di reddito (0,10 mld). Il panel la valuta neutra, ma riguarda il divario di genere e la segnaliamo.

### Come si compensano, dal 13 novembre 2026

Tre valutatori AI indipendenti hanno proposto le stesse regole, adottate da chi guida il progetto:

- **Tabacco (AS01, AS02):** un importo pari al gettito va per legge alla sanità vicino a casa (Case della Comunità, squadre di quartiere, personale infermieristico), con priorità ai distretti più poveri. In più, **servizi gratuiti per smettere di fumare** per chi ha un ISEE basso, con farmaci gratuiti: 0,04 mld l'anno dal margine delle risorse generali. Chi fuma e ha un reddito basso paga di più nel breve periodo; è il gruppo che guadagna di più se smette.
- **Bevande zuccherate (AS03):** nessuna compensazione in denaro; il peso medio è di pochi euro l'anno a persona.
- **Gasolio (SAD13, SAD01, SAD02):** i fondi per il rinnovo delle flotte e il credito agricolo già previsti vanno prima alle piccole imprese, alla montagna, alle aree interne e alle isole. Le misure di logistica verde 04-P7 e 04-P8 restano, perché sono la compensazione del taglio al gasolio agevolato.
- **Nessuna compensazione in denaro alle persone che fumano:** richiederebbe di profilare i comportamenti delle persone, che la Carta esclude.

Resta vero che queste coperture pesano di più su chi ha meno. Le compensazioni lo attenuano, non lo annullano; senza una microsimulazione non sappiamo di quanto.

PE03 (fine delle "quote" e di Opzione donna) ha punteggio −1 ma gettito zero, perché il risparmio è già nella legislazione vigente. La segnaliamo per trasparenza: chiude un'uscita anticipata usata soprattutto dalle donne.

### Il caso delle accise su tabacco e bevande

Le accise sul tabacco sono **regressive sul reddito**: chi ha meno spende per il fumo una quota più alta del proprio reddito. Ci sono tre argomenti che ne attenuano il peso, ma non lo annullano:

1. lo scopo è ridurre il consumo, e il beneficio di salute va a chi smette;
2. il prelievo dipende da un comportamento, non da una condizione;
3. il punteggio −1 resta sopra la soglia di esclusione automatica.

Però una compensazione dedicata **non c'è**. Il gettito va alle risorse generali. La quota di persone che fumano per fascia di reddito è un **dato da acquisire**. Proponiamo al panel di valutare un vincolo: una parte del gettito di AS01 va ai programmi per smettere di fumare nei distretti più poveri (proposta da valutare, non inserita).

### Il limite principale: manca una microsimulazione

Questa analisi è **qualitativa**. Non sappiamo quanto perde o guadagna, in euro, ciascun decimo della popolazione ordinato per reddito (decile). Per saperlo servono:

- **accesso ai microdati** delle indagini EU-SILC e sui consumi delle famiglie ISTAT, e dei dati fiscali anonimizzati dell'Agenzia delle entrate;
- **un modello di microsimulazione** fiscale e dei trasferimenti, come EUROMOD (Commissione europea, Centro comune di ricerca) o i modelli di UPB, Banca d'Italia, MEF e INPS;
- un modulo per le **imposte indirette** (accise, IVA), che EUROMOD copre solo in parte;
- ipotesi esplicite su **chi sopporta davvero** i prelievi sulle imprese: le imprese stesse, chi lavora o chi compra.

L'obiettivo 09-C1-c (`apprendimento/obiettivi.yaml`) prevede da 3 a 6 modelli pubblici di microsimulazione con licenza aperta in 5 anni. Anche l'indicatore 03-P1-c chiede una microsimulazione UPB, ancora da costruire.

---

## 5. Regole nuove proposte

Sono impegni di metodo. Costano poco, perché usano uffici che esistono già.

| # | Regola | Chi la attua | Quando |
|---|---|---|---|
| R1 | **Valutazione di impatto distributivo, di genere e territoriale** per ogni misura con effetti sopra 0,05% del PIL, con tabella per decile di reddito, genere, ripartizione e classe d'età. Si aggiunge alla relazione tecnica, come la valutazione generazionale di 01-P1 | RGS e UPB, con dati ISTAT e INPS | Dalla legge di bilancio del primo anno |
| R2 | **Bilancio di genere** obbligatorio e con effetti: riclassificazione della spesa già prevista per il rendiconto dello Stato (d.lgs. 90/2016), estesa alla legge di bilancio in fase di proposta | MEF-RGS, con ogni ministero | Entro 12 mesi |
| R3 | **Indicatori di divario obbligatori**: ogni obiettivo del programma ha almeno una versione disaggregata, cioè per genere, territorio o reddito (sezione 6) | Ufficio per la consulenza algoritmica pubblica (08-P1) | Entro 6 mesi |
| R4 | **Dati disaggregati per default**: le banche dati amministrative pubbliche (INPS, Agenzia delle entrate, MIM, Salute) pubblicano statistiche per genere, età, cittadinanza, disabilità e territorio, nel rispetto della privacy | ISTAT come coordinamento del Sistema statistico nazionale | Entro 24 mesi |
| R5 | **Partecipazione delle persone interessate**: le misure con impatto distributivo rilevante si discutono con le organizzazioni delle persone coinvolte (persone con disabilità, persone migranti, persone in povertà) e con l'assemblea sorteggiata (08-P1) | Ministero proponente | A ogni misura sopra soglia |

Il costo è quasi zero: si tratta di analisi in più dentro processi che esistono già. Il costo esatto è un **dato da acquisire** dalla RGS.

---

## 6. Indicatori di equità

Indicatori di **divario**, non solo medie. Base e obiettivi vengono da `apprendimento/obiettivi.yaml` dove esistono.

| # | Indicatore | Base | Fonte | Obiettivo a 5 anni |
|---|---|---|---|---|
| 1 | Posti al nido ogni 100 bambine e bambini sotto i 3 anni, **Sud** (Italia 31,6) | 19,0 (2023/24) | ISTAT; 02-C2-a | **33** |
| 2 | Abbandono precoce della scuola 18-24, **Isole** (Italia 8,2%) | 13,7% (2025) | Eurostat; 05-C1-a | **9,5%** |
| 3 | Occupazione delle **donne** 20-64 | 58,0% (2025) | Eurostat; 02-C2-c | **62,5%** |
| 4 | **Divario di occupazione** per limitazioni gravi | 43,4 punti (2025) | Eurostat; 02-C5-a | **37 punti** |
| 5 | Povertà assoluta dei **minorenni** | 12,5% (2025) | ISTAT; 02-C4-b | **10,5%** |
| 6 | Persone occupate a rischio di povertà | 10,2% (2025) | Eurostat; 02-C1-a | **8,5%** |
| 7 | Rinuncia alle cure nel **quinto più povero** (media 2,5%) | 4,4% (2025) | Eurostat `hlth_silc_08` | **2,5%**, proposta di obiettivo |
| 8 | Rapporto tra povertà assoluta delle famiglie di sole persone straniere e di sole persone italiane | 5,0 (29,4% / 5,9%, 2025) | ISTAT | **4,0**, proposta di obiettivo |
| 9 | Spesa per la casa oltre il 40% del reddito, persone in affitto a prezzo di mercato | 22,3% (2025) | Eurostat; 04-P2-a | **17,5%** (misura 04-P2 fuori dal programma: obiettivo a rischio) |
| 10 | NEET 15-29, **Sicilia** (Italia 13,3%) | 22,8% (2025) | Eurostat | **18%**, proposta di obiettivo |
| 11 | Divario retributivo di genere | dato da acquisire | Eurostat o ISTAT | da fissare dopo la base |

Due avvertenze:
- l'indicatore 9 ha un obiettivo che il programma intermedio **non** finanzia; lo teniamo visibile proprio per questo;
- gli obiettivi 7, 8 e 10 sono **proposte di obiettivo**: vanno validati dal panel.

---

## 7. Linguaggio inclusivo e chiaro

### Perché conta

Le parole dello Stato non sono neutre. Un modulo difficile scoraggia chi ha meno istruzione. Un avviso solo in italiano esclude chi lo parla poco. Un testo che parla solo "ai cittadini" fa sentire escluse le cittadine. Le parole orientano **l'accesso ai diritti**. Per questo il linguaggio è una questione di equità, non di stile.

Le regole che seguono hanno un limite chiaro: chiedono **rispetto e chiarezza**, non impongono un pensiero. Valgono per i testi pubblici dello Stato. Non riguardano il modo di parlare delle persone private.

### Le regole che GovernAI segue e propone per la PA

**1. Genere**
- Usare **forme doppie** ("cittadine e cittadini") o **forme neutre e collettive** ("la cittadinanza", "le persone", "chi lavora", "il personale").
- Usare il **femminile per ruoli e professioni** quando la persona è una donna: "la ministra", "l'assessora", "la sindaca", "la direttrice".
- **Niente schwa (ə), asterischi o chiocciole** nei testi pubblici. Le sintesi vocali usate da persone cieche o ipovedenti non li leggono bene. L'Accademia della Crusca, nel parere del 2023 sulla scrittura rispettosa della parità di genere negli atti giudiziari, chiesto dal Comitato pari opportunità della Corte di cassazione, li sconsiglia nei testi giuridici.
- Fonti: *Linee guida per l'uso del genere nel linguaggio amministrativo* (Cecilia Robustelli, 2012, progetto "Genere e linguaggio" con il Comune di Firenze e l'Accademia della Crusca); *Linee guida per l'uso del genere nel linguaggio amministrativo del MIUR* (2018).

**2. Disabilità**
- Scrivere "**persone con disabilità**", come la Convenzione ONU sui diritti delle persone con disabilità, ratificata dall'Italia con la legge 3 marzo 2009, n. 18.
- Non scrivere "disabili", "handicappati", "costretti in carrozzina", "affetti da".
- Restano i termini giuridici quando sono nomi di istituti: "invalidità civile", "legge 104" e i nomi di leggi e uffici.

**3. Origine**
- Scrivere "persone migranti", "persone straniere", "persone senza permesso di soggiorno".
- Non scrivere "clandestini".
- Scrivere "rom e sinti", non "nomadi": la maggior parte non vive in modo nomade. Fonte: Carta di Roma, protocollo deontologico per un'informazione corretta sui temi dell'immigrazione (2008) e sue linee guida.

**4. Povertà e marginalità**
- Scrivere "persone senza dimora", "persone in povertà", "persone detenute", "persone con dipendenze".
- Scrivere "assistenti familiari" invece di "badanti".
- Mettere **prima la persona**, poi la condizione.

**5. Età**
- Scrivere "persone anziane". Non usare espressioni che presentano l'età come un peso, per esempio "il peso degli anziani". Il dato demografico si descrive con i numeri.

**6. Linguaggio chiaro**
- Frasi brevi, circa 20 parole al massimo.
- Una sola idea per frase.
- Sigle spiegate alla prima occorrenza.
- Numeri sempre con fonte e anno.
- Verbi attivi: "l'ufficio risponde entro 30 giorni", non "la risposta verrà fornita".

**7. Accessibilità**
- **Testi alternativi** per immagini e grafici.
- **Contrasto** sufficiente tra testo e sfondo, come chiedono le linee guida europee sull'accessibilità del web (WCAG), richiamate dalle Linee guida AgID sull'accessibilità.
- Versione in **lettura facile** (easy-to-read) per i testi essenziali: moduli per prestazioni, avvisi di scadenza, diritti fondamentali.
- Informazioni sui servizi essenziali anche **nelle lingue più diffuse tra chi risiede in Italia**. Quali lingue scegliere è un **dato da acquisire** dalle statistiche ISTAT sui residenti per cittadinanza.

### Una misura concreta per la PA (proposta da valutare dal panel, non inserita nel programma)

**"Moduli che si capiscono"**
- **Linee guida aggiornate** sul linguaggio amministrativo chiaro e inclusivo, adottate dal Dipartimento della funzione pubblica, che riprendono le regole di questa sezione.
- **Obbligo di versione in lettura facile** per i **100 moduli più usati** della PA centrale e di INPS e Agenzia delle entrate, entro 3 anni.
- **Prova con le persone utenti**: ogni modulo riscritto si prova con un gruppo che comprende persone con disabilità intellettiva, persone anziane e persone che parlano poco l'italiano.
- **Traduzione** delle istruzioni dei 20 servizi essenziali nelle 5-6 lingue più diffuse.

**Costo stimato (stima GovernAI, ordine di grandezza):** circa **10-20 milioni di euro l'anno** per 3 anni, poi una manutenzione più bassa. La stima si basa su un costo ipotizzato di 50-100 mila euro per modulo (riscrittura, prova con chi usa i servizi, traduzioni, adeguamento dei sistemi). Non ci sono fonti ufficiali nel repository: va verificata.

**Da dove viene il denaro:** RIALLOCAZIONE, cioè una quota dei risparmi su consulenze e assistenza tecnica esterna (RA03, RA08). Nello scenario intermedio le risorse generali, di cui RIALLOCAZIONE fa parte, coprono la spesa senza margine. Quindi la misura entra solo **al posto di qualcos'altro** o con una copertura nuova. Per questo la proponiamo al panel e **non** la inseriamo nel programma.

---

## 8. Che cosa resta aperto

### Limiti

- **Nessuna microsimulazione per decili.** È il limite più grande. Senza, non sappiamo se il programma nel suo insieme riduce o aumenta le disuguaglianze di reddito.
- **Dati mancanti** nel repository: indice di Gini, divario retributivo di genere, lavoro di cura non pagato, occupazione per cittadinanza, povertà per ripartizione, persone che fumano per reddito.
- **Punteggi EQU qualitativi**: li dà un panel con una rubrica comune. Sono utili, ma non sono misure.
- **Tagli di spesa non ancora individuati** (RA13): l'effetto sull'equità dipende da dove si taglia.
- **Lacune del programma**: inclusione lavorativa delle persone straniere, casa, salute mentale, personale infermieristico oltre il pilota, progetto di vita delle persone con disabilità.
- **Fondi che scadono**: dei circa 1,9 mld pagati con la coesione, 0,5 servono anche dopo il 2029 (prevenzione dei rischi, conto competenze, ponte contro la dispersione, staffetta nella PA) e oggi non hanno una copertura garantita; il resto sono investimenti che finiscono o sperimentazioni da valutare (`programma/coesione_dopo_2029.csv`). In tutto, circa 1,9 mld di spesa sono pagati con i fondi europei di coesione 2021-2027, ammessi fino al 2029; molte di queste misure riguardano territori e persone più fragili, e andranno rifinanziate.

### Scelte politiche che questo capitolo non prende

- **Quanto pesa l'equità rispetto alla crescita e agli altri valori.** La Carta non fissa un peso: il motore prova tutte le combinazioni. Le persone e l'assemblea sorteggiata decideranno il peso centrale (Carta, regola 8).
- **Opportunità o risultato.** Investire nei primi anni di vita o sostenere i redditi oggi? Servono tutti e due, ma le risorse sono scarse.
- **Accise sulla salute.** È accettabile un prelievo regressivo se riduce comportamenti dannosi? Con quale compensazione?
- **Universale o selettivo.** Molte coperture introducono soglie ISEE. Le soglie aiutano chi ha meno, ma possono creare "trappole" vicino alla soglia e meno consenso per il welfare.
- **Equità tra territori e autonomia regionale.** Quanto deve garantire lo Stato in modo uguale ovunque (LEP) e quanto possono decidere le Regioni?

---

## Allegato: guida rapida al linguaggio chiaro e inclusivo

### Tabella "invece di → scrivi"

| # | Invece di | Scrivi |
|---|---|---|
| 1 | i cittadini (riferito a tutte e tutti) | le cittadine e i cittadini; la cittadinanza; le persone |
| 2 | i lavoratori | chi lavora; le lavoratrici e i lavoratori; il personale |
| 3 | gli utenti | le persone che usano il servizio; l'utenza |
| 4 | i dipendenti pubblici | il personale pubblico; chi lavora nella PA |
| 5 | i candidati | chi si candida; le candidate e i candidati |
| 6 | gli studenti | studentesse e studenti; la popolazione studentesca |
| 7 | il ministro (se è una donna) | la ministra |
| 8 | l'assessore (se è una donna) | l'assessora |
| 9 | il sindaco (se è una donna) | la sindaca |
| 10 | il direttore (se è una donna) | la direttrice |
| 11 | tutt\*, tuttə, tutt@ | tutte e tutti; ogni persona |
| 12 | i disabili | le persone con disabilità |
| 13 | handicappato, portatore di handicap | persona con disabilità |
| 14 | costretto in carrozzina | persona che usa la sedia a rotelle |
| 15 | affetto da (una malattia) | persona con (una malattia) |
| 16 | normodotati | persone senza disabilità |
| 17 | clandestini | persone senza permesso di soggiorno; persone migranti |
| 18 | extracomunitari | persone con cittadinanza non UE; persone straniere |
| 19 | nomadi (per rom e sinti) | rom e sinti; persone rom e sinte |
| 20 | i barboni, i senzatetto | le persone senza dimora |
| 21 | i poveri | le persone in povertà; le famiglie in povertà |
| 22 | i carcerati | le persone detenute |
| 23 | i drogati, i tossicodipendenti | le persone con dipendenze |
| 24 | le badanti | le assistenti familiari e gli assistenti familiari |
| 25 | il peso degli anziani | l'aumento delle persone anziane (con il dato) |
| 26 | i vecchi | le persone anziane |
| 27 | le quote rosa | la parità di genere nelle nomine; la rappresentanza equilibrata |
| 28 | la casalinga | chi si occupa della casa e della cura familiare |
| 29 | si comunica che la S.V. è tenuta a | deve; le chiediamo di |
| 30 | entro e non oltre | entro |
| 31 | in data odierna | oggi |
| 32 | ISEE (alla prima occorrenza, senza spiegazione) | ISEE, l'indicatore che misura la situazione economica della famiglia |
| 33 | la risposta verrà fornita | l'ufficio risponde entro 30 giorni |

### Eccezioni

- **Termini giuridici.** Si usano i nomi degli istituti come sono scritti nella legge: "invalidità civile", "indennità di accompagnamento", "permesso di soggiorno", "persona detenuta" o "internato" quando la legge distingue. Nel testo che spiega si usa il linguaggio di questa guida.
- **Nomi propri di leggi, enti e documenti.** Non si cambiano: "legge 5 febbraio 1992, n. 104", "Garante nazionale dei diritti delle persone private della libertà personale", "Bonus lavoratrici madri".
- **Citazioni testuali.** Si riportano come sono, tra virgolette, con la fonte. Se contengono termini superati, si può aggiungere una nota.
- **Dati statistici.** Si usano le categorie della fonte (per esempio "limitazioni gravi" di ISTAT ed Eurostat) e si spiega che cosa misurano.
- **Testi brevi e moduli.** Quando le forme doppie appesantiscono troppo, si preferiscono le forme neutre ("chi richiede", "la persona richiedente") o la seconda persona ("lei", "voi").
- **Maschile non marcato.** Il parere della Crusca del 2023 lo considera corretto, se usato con consapevolezza. GovernAI preferisce le forme doppie o neutre quando non appesantiscono il testo, come suggeriscono le linee guida di Robustelli e del MIUR. Il maschile plurale resta accettabile quando le alternative rendono il testo meno chiaro, e resta nelle norme in vigore e nelle citazioni.

### Fonti della guida

- Cecilia Robustelli, *Linee guida per l'uso del genere nel linguaggio amministrativo*, progetto "Genere e linguaggio", Comune di Firenze e Accademia della Crusca, 2012: https://accademiadellacrusca.it/sites/www.accademiadellacrusca.it/files/page/2015/03/04/linee_guida.pdf
- MIUR, *Linee guida per l'uso del genere nel linguaggio amministrativo del MIUR*, 2018, gruppo di lavoro coordinato da Cecilia Robustelli (copia ospitata dall'Università di Messina): https://unime.it/sites/default/files/2022-07/Linee_Guida_%20per_l_uso_del_genere_nel_linguaggio_amministrativo_del_MIUR_2018.pdf
- Accademia della Crusca, parere del 9 marzo 2023 al Comitato pari opportunità del Consiglio direttivo della Corte di cassazione sulla scrittura rispettosa della parità di genere negli atti giudiziari. Esclude asterisco e schwa nel linguaggio giuridico e raccomanda i femminili delle professioni. Resoconto: https://tg24.sky.it/cronaca/2023/03/20/schwa-accademia-della-crusca/ (testo integrale sul sito accademiadellacrusca.it, link diretto da verificare).
- Convenzione ONU sui diritti delle persone con disabilità, ratificata con legge 3 marzo 2009, n. 18.
- Carta di Roma, protocollo deontologico sui temi dell'immigrazione, 2008: https://www.cartadiroma.org (link da verificare).
- Linee guida AgID sull'accessibilità degli strumenti informatici; WCAG 2.1 (link da verificare).

*Nota sul dibattito.* Sullo schwa il dibattito tra linguiste e linguisti è aperto. La scelta di non usarlo nei testi pubblici si basa su due motivi pratici: leggibilità con le sintesi vocali e coerenza con le fonti istituzionali. Non è un giudizio sull'uso privato o sperimentale.
