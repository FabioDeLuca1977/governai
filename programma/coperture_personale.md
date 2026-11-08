# Coperture sulla spesa di personale e di funzionamento della PA (RP01-RP07)

*Agente finanza pubblica e organizzazione della PA. 8 novembre 2026. Righe in `programma/coperture_personale.csv`, con le stesse colonne di `coperture_menu.csv`. Fondo: RIALLOCAZIONE. Importi in mld €/anno a regime. "Stima GovernAI" vuol dire che non esiste una stima ufficiale.*

**Direzione politica.** Trovare risorse senza nuove tasse. Ridurre la spesa di personale dove serve. Aumentare la spesa per istruzione, cultura e servizi sociali.

**Settori esclusi da ogni taglio.** Scuola, università, ricerca e cultura (biblioteche, musei, archivi, soprintendenze). Sanità. Forze dell'ordine, vigili del fuoco e soccorso. Servizi sociali: assistenti sociali, educatori, operatori dei servizi sociali dei comuni e degli ambiti, centri per l'impiego per la parte di inclusione. Per prudenza escludo anche giustizia, Interno e agenzie fiscali, perché le aree 07 e 11 chiedono più personale in quei settori.

## Sintesi

| ID | Misura | Min | Max | Regime | Livello | Chi paga |
|---|---|---|---|---|---|---|
| RP01 | Turnover selettivo nei profili amministrativi generici (ministeri ed EPNE) | 0,040 | 0,100 | 2031 | 2 | Giovani candidati ai concorsi generici; uffici di supporto |
| RP02 | Dirigenza: -8/12% dei posti di II fascia, meno incarichi a esterni | 0,012 | 0,030 | 2030 | 1 | Aspiranti dirigenti; dirigenti esterni |
| RP03 | Uffici di diretta collaborazione, strutture di missione e commissariali: -20% | 0,020 | 0,050 | 2028 | 1 | Esperti esterni; indennità dello staff politico |
| RP04 | Accorpamento degli enti nazionali minori e servizi comuni | 0,015 | 0,050 | 2030 | 2 | Componenti degli organi; back-office |
| RP05 | Sedi: standard di spazio, sedi uniche, meno costi di gestione | 0,015 | 0,040 | 2030 | 1 | Fornitori di pulizia, vigilanza e manutenzione |
| RP06 | INPS, INAIL e altri EPNE: -4% della spesa per beni e servizi, versata allo Stato | 0,030 | 0,060 | 2029 | 1 | Fornitori degli enti |
| RP07 | Partecipate: applicazione obbligatoria del TUSP, quota dei risparmi allo Stato | 0,020 | 0,060 | 2030 | 2 | Amministratori di società; enti locali |
| | **Totale** | **0,152** | **0,390** | | | |

**Il messaggio principale: il bacino è piccolo.** Il costo del lavoro pubblico è di 186,1 mld (2024). Le Funzioni centrali (ministeri, agenzie fiscali, EPNE) ne pesano solo 13,3 mld, il 7% (RGS, Conto annuale 2024, tab. 5.1). Il resto è soprattutto scuola e ricerca (58,4), sanità (46,7), sicurezza e difesa (39,2) e funzioni locali (24,6). Sono tutti settori protetti, oppure i loro risparmi restano agli enti locali (art. 119 Cost.). Tolto il personale protetto, sul personale statale restano risparmi nell'ordine dei decimi di miliardo, non dei miliardi. Promettere di più significherebbe fare tagli lineari o tagliare i servizi.

**Come le ho stimate.** Ogni misura taglia uno stanziamento per legge. Nessuna conta "risparmi attesi". Il minimo usa le ipotesi più basse e, dove la base non è verificata, una base ridotta.

**Sovrapposizioni con il menu, in sintesi.**
- RA07 (turnover verso i tecnici): RP01 esclude dalla base i posti già riservati ai tecnici.
- RA03 (consulenze): RP03 non tocca quei capitoli.
- RA02 (canoni): RP05 conta solo i costi di gestione delle sedi.
- RA01 e RA09 (Stato): RP06 riguarda gli enti, non lo Stato.
- RA13 (revisione dei ministeri): rischio reale di sovrapposizione con RP02, RP03 e RP05. Se si attivano insieme, la RGS deve calcolare l'obiettivo di RA13 al netto di questi tagli. Altrimenti non vanno sommati.
- 09-C7 e 09-C8: i loro risparmi si contano solo dopo la certificazione e non sono nel menu. RP01 è diverso: decide per legge una quota di posti non sostituiti. Su questo punto c'è una tensione politica con 09-C8 (vedi RP01).

**Destinazione.** Il fondo è RIALLOCAZIONE, come per le altre misure RA. La scelta politica è usarlo per scuola, cultura e servizi sociali. Il collegamento va scritto nella legge di bilancio, perché il menu non vincola la destinazione.

---

## RP01: turnover selettivo nei profili amministrativi generici

**Ragionamento.** Le Funzioni centrali stanno per avere molte uscite. Il 49% dei dipendenti ha più di 55 anni (102.557 su 211.236). Nel 2024 i cessati sono stati 17.495 e il rapporto di sostituzione è stato 1,31: ogni 100 uscite, 131 assunzioni. Questa uscita naturale permette di ridurre i profili generici senza licenziare nessuno, mentre RA07 sposta altri posti verso i tecnici.

**Dati.** RGS, Conto annuale 2024, commento 2015-2024. Ministeri 125.788 dipendenti, EPNE 38.967, agenzie fiscali 45.046 (tab. 3.2). Cessati per comparto: tab. 8.1. Età: tab. sulle classi di età. Retribuzione media delle Funzioni centrali 41.017 € lordi (tab. 6.1).

**Ipotesi.**
- Perimetro di circa 80.000 dipendenti: 164.755 tra ministeri ed EPNE, meno giustizia, Interno, MiC, MIM, MUR, ordini professionali, servizi di inclusione e sportelli INPS. La ripartizione per ministero è **da verificare**.
- Il 40% del perimetro è in profili generici dopo la quota di RA07 (**stima**).
- Le cessazioni sono il 5-7% l'anno, sotto l'8,3% del 2024.
- Non si sostituisce il 15-25% dei generici che escono, per 4 anni.
- Il costo d'ingresso è di 41-45 mila € con oneri (**da verificare** sui tabellari CCNL).
- Risultato: 0,04-0,10 a regime nel 2031.

**Rischi per i servizi.** Le persone negli uffici di supporto calano di 1.000-2.200. Il rischio è che crescano gli arretrati nei procedimenti interni. Paga anche chi si prepara ai concorsi generici, che sono più importanti al Sud: per questo EQU vale -1. Contrappesi:
- l'ente sceglie dove non sostituire e lo motiva nel PIAO;
- c'è una clausola di salvaguardia sugli indicatori di servizio di 09-C6;
- prima del concorso si usa la mobilità.

**Tensione politica.** Secondo 09-C8 si può non sostituire solo dopo la certificazione dell'automazione. Qui la non sostituzione è decisa per legge in anticipo. È coerente con la direzione politica scelta, ma va dichiarato.

**Verifica giuridica.** Limitare le facoltà assunzionali è una scelta legittima di bilancio (art. 81 e art. 97), già usata dal DL 95/2012 e dal DL 90/2014. Non tocca il rapporto di lavoro né la retribuzione (art. 36 Cost.) e lascia l'accesso per concorso (art. 97, c. 4).

## RP02: dirigenza

**Ragionamento.** Nei ministeri lavorano 2.569 dirigenti per 108.430 non dirigenti, cioè un dirigente ogni 42 persone (2024). Accorpare gli uffici piccoli riduce i posti di funzione e i costi di struttura senza togliere personale operativo.

**Dati.** RGS, Conto annuale 2024, tab. 10.4-10.5. La retribuzione media della dirigenza di II fascia non è nel commento. Il differenziale con un funzionario (60-80 mila € con oneri) è **da verificare** su Conto annuale e ARAN.

**Ipotesi.** Base di circa 2.600 posti, ministeri ed EPNE, esclusi MiC, MIM e MUR. Il numero degli EPNE è **da verificare**. Si sopprime l'8-12% dei posti man mano che si liberano: 210-310 posti, per 0,012-0,03.

**Rischi.** Pochi per i cittadini. Si rischia di creare dirigenze con "troppi riporti" e meno opportunità di carriera interna.

**Verifica giuridica.** L'organizzazione degli uffici è fissata con regolamenti (art. 97 c. 2; art. 17 L. 400/1988). Gli incarichi in corso arrivano a scadenza: nessuna revoca anticipata.

## RP03: uffici di diretta collaborazione e strutture commissariali

**Ragionamento.** È poca spesa, ma molto visibile ed esemplare. Il vertice politico dà l'esempio prima di chiedere sacrifici agli uffici.

**Dati.** OpenBDAP-RGS, Rendiconto 2025: nei ministeri il programma "Indirizzo politico" ha 260 mln impegnati, di cui 214,7 di redditi da lavoro. Conto annuale 2024, tab. 10.6-10.7: 127 dirigenti e 1.197 non dirigenti negli uffici di diretta collaborazione. Il numero degli esperti esterni **non è verificato**.

**Ipotesi.** Tetto del 20% sotto il 2025, cioè 52 mln al massimo. Il minimo di 20 mln considera che il personale di ruolo che rientra negli uffici ordinari non genera risparmio. Si risparmia su indennità, esterni e comandati. Le strutture della PCM non sono nel dato e non le conto.

**Rischi.** Minimi per i servizi. Il rischio è che si aggiri il tetto spostando lo staff in altri capitoli: serve l'organico massimo per legge.

**Verifica giuridica.** È spesa di funzionamento degli organi di governo, regolata da regolamenti (art. 14 d.lgs. 165/2001). Il tetto di spesa è legittimo.

## RP04: accorpamento degli enti nazionali minori e servizi comuni

**Ragionamento.** Molti enti nazionali piccoli hanno ciascuno il proprio consiglio di amministrazione, collegio, ufficio del personale, contabilità e gare. Accorparli e usare servizi comuni, come NoiPA per gli stipendi, riduce i costi fissi.

**Dati.** Elenco ISTAT S13. Conto annuale: 38.967 dipendenti EPNE nel 2024. **Non ho verificato** quanti siano gli enti minori né la loro spesa. Per questo la stima è bassa.

**Ipotesi.** Si accorpano 10-20 enti, con un risparmio di 1,5-2,5 mln ciascuno, per 0,015-0,05. Restano fuori enti di ricerca, culturali, sanitari, socio-assistenziali e di soccorso, oltre agli ordini professionali, che sono autofinanziati.

**Rischi.** Le fusioni costano all'inizio, tra sistemi informativi e contratti integrativi diversi. Senza una regia il risparmio slitta. Il personale non viene licenziato: cambia mansione o sede, con le tutele dell'art. 30 d.lgs. 165/2001.

**Verifica giuridica.** Riordinare gli enti nazionali è competenza statale (art. 117 c. 2 lett. g). Serve una legge delega con criteri precisi (art. 76).

## RP05: sedi degli uffici civili dello Stato

**Ragionamento.** Con il lavoro agile servono meno postazioni fisse. Concentrare gli uffici in meno immobili riduce utenze, pulizia, vigilanza e manutenzione.

**Dati.** OpenBDAP-RGS, Rendiconto 2025: 205 mln di consumi intermedi per utenze, manutenzione, pulizia e vigilanza nei ministeri civili, esclusi Interno, Difesa, Giustizia, MiC, MIM e MUR. La ricerca è per parole chiave, quindi il perimetro è **sottostimato**: molti capitoli "per il funzionamento" mescolano voci diverse.

**Ipotesi.** Riduzione dell'8-12% su una base di 0,2-0,35 mld, per 0,015-0,04. I canoni sono in RA02 e non li conto. Le vendite di immobili sono una tantum e restano fuori.

**Rischi.** Pochi per i cittadini, se gli sportelli restano accessibili. Paga chi perde la postazione fissa e paga chi fornisce i servizi, dove c'è un rischio per l'occupazione: serve una clausola sociale nei nuovi appalti.

**Verifica giuridica.** Conforme all'art. 2, c. 222, L. 191/2009 e ai piani del Demanio. Il lavoro agile resta regolato dal CCNL, senza obblighi nuovi per i dipendenti.

## RP06: INPS, INAIL e altri EPNE, spese di funzionamento

**Ragionamento.** Gli enti previdenziali comprano molti beni e servizi e sono fuori dal perimetro di RA01 e RA09, che riguardano lo Stato. Un taglio piccolo e versato allo Stato è credibile.

**Dati.** INPS, Assestamento del preventivo 2024, voce B.06.B: 885,9 mln per beni di consumo e servizi. I dati di INAIL e degli altri EPNE **non sono verificati**.

**Ipotesi.** Taglio del 4% sul 2025. Il minimo è calcolato sulla sola INPS (35 mln, arrotondato a 0,03). Il massimo usa una base di circa 1,4 mld, per 0,06.

**Rischi.** Se il taglio cade sull'ICT, i servizi digitali possono rallentare. Gli sportelli, i servizi per l'inclusione e le spese per prestazioni sono esclusi.

**Verifica giuridica.** Il meccanismo dei versamenti degli enti al bilancio dello Stato esiste già (L. 160/2019, cc. 590-602). Non ho verificato la giurisprudenza costituzionale su questi versamenti. Va rispettata l'autonomia degli enti privatizzati (casse professionali), che sono esclusi.

## RP07: società e organismi partecipati

**Ragionamento.** Il Testo unico del 2016 impone già di chiudere o fondere le società inutili, ma lo si applica poco. Un commissario ad acta rende l'obbligo effettivo.

**Dati.** La Corte dei conti, Sezione autonomie, nel referto 2024 ha analizzato 6.558 organismi degli enti territoriali per il triennio 2019-2021. Il dato l'ho preso dalla stampa (Milano Finanza, 6.6.2024): va **verificato su fonte primaria**. Non ho letto il Rapporto MEF sulle partecipazioni (dati 2022). Non ho un dato su quante società abbiano più amministratori che dipendenti.

**Ipotesi.** Gran parte del risparmio resta agli enti locali. Diventa copertura statale solo con un'intesa che versi una quota dei risparmi certificati. Stima prudente: 0,02-0,06, contata dopo la certificazione.

**Rischi.** Se si chiude una società che gestisce un servizio vero, il servizio si interrompe. Per questo sono esclusi i servizi pubblici locali essenziali e gli organismi dei servizi sociali. RIS vale -1 per l'autonomia locale compressa.

**Verifica giuridica.** Il coordinamento della finanza pubblica è competenza dello Stato (art. 117 c. 3; art. 119). Il prelievo sui risparmi locali richiede un'intesa e deve essere proporzionato, secondo la giurisprudenza costituzionale.

---

## Cosa ho escluso e perché

- **Tagli a stipendi, fondi accessori, buoni pasto**: violano i CCNL e l'art. 36, oppure colpiscono tutti senza distinguere.
- **Funzioni locali (comuni, regioni)**: i risparmi restano agli enti. Diventano copertura statale solo tagliando i trasferimenti, con rischi per i servizi sociali comunali, che ora sono protetti. Le gestioni associate dei piccoli comuni sono utili, ma non sono una copertura statale.
- **Straordinari e missioni**: nel bilancio dello Stato non si separano dalle "competenze fisse e accessorie". Senza un dato non propongo cifre.
- **Agenzie fiscali, giustizia, Interno**: le aree 07 e 11 chiedono più risorse. Tagliare qui contraddirebbe il programma.
- **Difesa**: è fuori dal mandato e dipende dalle scelte in `selezione_difesa.md`.

## Cosa non so

- La ripartizione del personale per ministero e per profilo, quindi la base di RP01. Serve il Conto annuale per amministrazione, tab. 1 e 5.
- Il costo d'ingresso di un funzionario e il differenziale di costo dei dirigenti (RP01, RP02).
- Il numero e la spesa degli enti nazionali minori (RP04).
- La spesa per beni e servizi di INAIL e degli altri EPNE (RP06).
- I dati primari sulle partecipate (RP07).
- La sovrapposizione esatta con RA13: va definita con la RGS.

## Fonti

- RGS, Conto annuale 2024, *Commento ai principali dati 2015-2024*: https://contoannuale.rgs.mef.gov.it/ext/Documents/ANALISI%20E%20COMMENTI%202015-2024.pdf
- OpenBDAP-RGS, Rendiconto 2025 per capitolo: `dati/raw/00b_openbdap_rendiconto_2025_spese_capitolo.csv`
- INPS, Assestamento del bilancio preventivo 2024, conto economico: https://www.inps.it/content/dam/inps-site/pdf/dati-analisi-bilanci/note-variazione/Ass_Bil_Prev_2024_06_Conto_Ec.pdf
- Eurostat `gov_10a_main` D1PAY (203,3 mld nel 2025): `dati/serie/09_redditi_lavoro_dipendente_pa.csv`
- Corte dei conti, Sezione autonomie, referto 2024 sugli organismi partecipati, ripreso da Milano Finanza: https://www.milanofinanza.it/news/partecipate-corte-dei-conti-con-il-covid-perdite-raddoppiate-202406061534378843 (fonte secondaria)
