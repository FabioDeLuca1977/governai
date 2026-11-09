# Schede pronte — Area 12 (Pubblica amministrazione produttiva)

*Agente "PA produttiva" — 8 novembre 2026. Integra l'area 09 (`programma/schede/09_pa_digitale.md`, proposte 09-C1…09-C5) senza duplicarla. Le nuove proposte mantengono la numerazione dell'area 09: **09-C6, 09-C7, 09-C8**. Varianti: `programma/varianti/12_pa_produttiva.csv`. Confronto costi/risparmi: `benchmark/nuove_proposte_pa.csv`. Importi in mld €/anno; "stima GovernAI" quando non esiste una stima ufficiale.*

## La domanda e come la affrontiamo

> *"Ci sono proposte concrete per ridurre i dipendenti pubblici che non lavorano e attivare soluzioni automatizzate?"*

Sì, ma i dati chiedono di separare quattro questioni che nel dibattito pubblico si confondono:

| Questione | Cosa dicono i dati | Risposta GovernAI |
|---|---|---|
| **(a) Produttività e organizzazione** | Il problema principale è organizzativo: la valutazione non distingue. Secondo il Ministro per la PA il **98%** del personale riceve il punteggio massimo (citato da OCPI, Univ. Cattolica, 2026). La Corte dei conti (delibera 62/2024/G) parla di "appiattimento verso l'alto" delle valutazioni nelle PA centrali (2020-22; fonte secondaria, testo da verificare) | 09-C6, parte organizzativa |
| **(b) Chi non svolge il proprio lavoro** | È una minoranza, e le regole per sanzionarla esistono già. Nel 2024: **11.328 procedimenti disciplinari avviati, 590 licenziamenti, 2.177 sospensioni**, su circa 3,37 milioni di dipendenti, cioè lo 0,34% e lo 0,018% (Funzione pubblica, *Procedimenti disciplinari 2024*, dati al 30.6.2025). Le giornate di malattia nel pubblico sono **8,3 per dipendente** contro 8,6 nel privato (2023; CGIA su dati INPS, fonte secondaria) | 09-C6, parte disciplinare: applicare bene le regole che ci sono, non inventarne di nuove |
| **(c) Automazione e riallocazione** | Il lavoro d'ufficio è il più esposto all'IA generativa (ILO, *Working Paper 140*, 2025), ma l'"esposizione" è un limite superiore, non una previsione. In Italia solo 45 enti su 108 censiti hanno iniziative di IA, con 120 progetti (AgID, censimento 2025) | 09-C7 |
| **(d) Ricambio generazionale** | Fino a **un terzo** degli oltre 3,7 milioni di lavoratori pubblici può andare in pensione entro 10 anni (INPS, Osservatorio sui lavoratori pubblici, novembre 2025). Età media dei dipendenti stabili: **49 anni e 4 mesi** (RGS, Conto annuale 2024, via stampa; primario non verificato) | 09-C8: l'uscita naturale è l'occasione per riqualificare, non per licenziare |

**Il punto di partenza.** L'Italia ha **5,7 dipendenti pubblici ogni 100 abitanti**, contro 8,3 in Francia e 6,3 in Germania (dossier 09; confronto FPA non verificato su fonte primaria). Il problema non sono "troppi statali", ma tre cose: lavoro mal organizzato e mal misurato, poche competenze tecniche e molti compiti ripetitivi che le macchine possono fare meglio. Ridurre la spesa licenziando non è né necessario né realistico. Le uscite per pensionamento, fino a circa 120.000 l'anno, permettono di ridisegnare gli organici in modo **selettivo**, decidendo posto per posto se sostituire, riqualificare o automatizzare.

**Valori in gioco.** RIS: nessuna generalizzazione; chi lavora bene, cioè la grande maggioranza, non deve pagare per i pochi che non lo fanno. EQU: stesse regole in ogni ente, piccolo o grande. FID: dati pubblici su procedimenti, tempi e risultati. CIT: diritti e doveri dei dipendenti e dei dirigenti. INN: tecnologia che toglie lavoro ripetitivo, non dignità.

## Quadro dell'area

| Proposta | PIENA | ESSENZIALE | PILOTA / ZERO | Fondi |
|---|---|---|---|---|
| 09-C6 Lavoro pubblico misurato e giusto | 0,03 (int. 1) | 0,012 (0,6) | ZERO 0 (0,3) | RIALLOCAZIONE |
| 09-C7 Automazione con riallocazione garantita | 0,20 al picco 2028-29, poi 0,05 (1) | 0,07 al picco, poi 0,02 (0,5) | PILOTA 0,02 solo 2027-29 (0,15) | COESIONE_2127 (una tantum); RIALLOCAZIONE |
| 09-C8 Staffetta delle competenze | 0,23 fino al 2029, poi 0,18 (1) | 0,08, poi 0,06 (0,4) | ZERO 0 (0,25) | RIALLOCAZIONE; COESIONE_2127 (FSE+ fino al 2029) |
| **Totale** | **0,46 al picco; 0,26 permanenti** | **0,162 al picco; 0,092 permanenti** | | |

**Regole rispettate.** Nessun prelievo da DEFICIT, RISPARMI_ATTESI, IVA_EVASIONE, ETS o ALTRO. Nessun risparmio dell'automazione o del turnover è usato come copertura: i risparmi attesi sono stimati solo nelle note e in `benchmark/nuove_proposte_pa.csv`. Diventano utilizzabili soltanto **dopo la certificazione ex post** (art. 17 L. 196/2009; `giuridico/quadro.md`, §3). La coesione 2021-27 finanzia solo investimenti e formazione **una tantum** fino al 2029, **mai personale stabile**.

**Coperture da proporre al menu (fondo RIALLOCAZIONE).** R09-1, R09-2 e R09-3 sono già usate da 09-C2…C5: R09-3 è impegnata per 0,40 su un massimo di 0,42. Per non contare due volte la stessa risorsa propongo una misura nuova e indico RA13 come riserva:

| Misura | Cosa si taglia | Gettito stimato | Chi paga |
|---|---|---|---|
| **R12-1 Esternalizzazioni di back-office** (nuova) | Contratti delle amministrazioni centrali per data entry, dematerializzazione documentale, contact center di primo livello e caricamento di pratiche. Si riducono del 15-20% man mano che 09-C2 (once-only) e 09-C7 (automazione) eliminano il lavoro a monte. Taglio corrispondente degli stanziamenti, non risparmio atteso | 0,05-0,12 (stima GovernAI; la spesa di base va censita da Consip/RGS) | Fornitori di servizi esternalizzati. Rischio occupazionale per i loro addetti: clausola sociale e priorità nei percorsi di 09-C8 |
| RA13 (già nel menu) | Revisione strutturale della spesa dei ministeri | quota 0,1-0,15 | — |

Uso nelle PIENE: 0,26 su RIALLOCAZIONE (R12-1 fino a 0,12, RA13 per il resto). Uso nelle ESSENZIALI: 0,092, coperto da R12-1.

**Raccordi.** 09-C3 riserva una quota del turnover ai tecnici (R09-1/RA07): 09-C8 non tocca quella quota, governa il resto del turnover. 09-C5 fissa le regole sull'IA (albo, valutazione d'impatto, assistente condiviso, 24 ore di formazione): 09-C7 le usa e non le ripete. 09-C2 elimina le richieste di dati inutili: 09-C7 automatizza ciò che resta del lavoro ripetitivo interno.

---

## 09-C6 — "Lavoro pubblico misurato e giusto": organizzazione, valutazione vera e responsabilità

*In una frase: si misurano i risultati degli uffici per la cittadinanza, si valuta davvero chi lavora, si aiuta chi è in difficoltà e si applicano fino in fondo le regole che già esistono contro chi non lavora, con tempi certi e senza processi sommari.*

**Problema in un dato.** Nel 2024 i procedimenti disciplinari avviati sono stati **11.328**, pari allo 0,34% dei dipendenti. Si sono chiusi con **590 licenziamenti**: 230 per assenze ingiustificate o false certificazioni, 29 per falsa attestazione della presenza, 162 per reati e 153 per negligenza e inosservanza degli obblighi di servizio. Altri **979 procedimenti erano ancora in corso** a sei mesi dalla fine dell'anno, e 768 erano sospesi in attesa del giudizio penale (Funzione pubblica, *Procedimenti disciplinari 2024*). La rilevazione **non conta a parte** i licenziamenti per insufficiente rendimento (art. 55-quater, c. 1, lett. f-quinquies). Intanto la valutazione della performance dà il massimo a quasi tutti: 98% secondo il Ministro. Lo strumento contro lo scarso rendimento esiste dal 2017, ma senza una valutazione credibile non si può usare, né per premiare né per correggere.

**Diagnosi senza generalizzazioni.** I casi gravi sono pochi, ma pesano molto sulla fiducia dei cittadini e sul morale dei colleghi che lavorano. Il problema più diffuso non è il "fannullone", è l'ufficio senza obiettivi misurabili, dove nessuno, nemmeno il dirigente, risponde dei risultati. Per questo la proposta parte dall'**organizzazione** e solo dopo arriva alla **responsabilità individuale**.

**Soluzione in 4 punti.**
1. **Indicatori di servizio pubblici per ufficio.** Il PIAO di ogni amministrazione con più di 50 dipendenti contiene da 3 a 5 indicatori di servizio, cioè tempi, arretrati, errori e soddisfazione degli utenti, calcolati dai sistemi informativi e non autodichiarati. Sono pubblicati in formato aperto, con un cruscotto nazionale presso la Funzione pubblica, collegato a 09-C1. La valutazione organizzativa precede quella individuale.
2. **Valutazione individuale credibile.** Si attua la legge sul merito del luglio 2026 (ddl AS 1778, approvazione definitiva del Senato 30.6/1.7.2026; numero e GU da verificare): le valutazioni massime vanno a non più del 30% del personale per ufficio dirigenziale generale. Il dirigente che non valuta o non avvia l'azione disciplinare dovuta ne risponde in base all'art. 55-sexies, c. 3, d.lgs. 165/2001, oggi poco applicato. La sua inerzia entra nella sua valutazione.
3. **Percorso di miglioramento prima della sanzione per scarso rendimento.** Se un dipendente riceve una valutazione negativa motivata, scatta un **piano di miglioramento** di 6-12 mesi, scritto con lui: obiettivi chiari, formazione, eventuale cambio di mansione o di ufficio, verifica della salute e dei carichi di lavoro. Solo dopo un piano fallito, e con valutazioni negative ripetute nel triennio, si apre il procedimento della lett. f-quinquies. Così la regola diventa usabile e giusta: protegge chi è in difficoltà per ragioni di salute, familiari o organizzative, e non protegge chi rifiuta di lavorare.
4. **Uffici disciplinari professionali e tempi certi.** I piccoli enti spesso non hanno un Ufficio per i procedimenti disciplinari (UPD) competente, e i procedimenti decadono o si perdono. Gli UPD si gestiscono **in forma associata** a livello provinciale o di unione di comuni, con personale formato. Restano fermi i termini già previsti: per la falsa attestazione della presenza, sospensione cautelare entro 48 ore e procedimento entro 30 giorni (d.lgs. 116/2016). La Funzione pubblica pubblica **ogni anno, per ente**, dati aggregati su procedimenti avviati, conclusi, decaduti e tempi medi, con le categorie troppo piccole oscurate per tutelare la privacy.

**Cosa NON si fa (linee rosse).** Nessuna sorveglianza dei dipendenti con IA, biometria o tracciamento continuo. Le norme sulla rilevazione biometrica delle presenze della l. 56/2019 sono già state abrogate e non si reintroducono. L'AI Act vieta il riconoscimento delle emozioni sul luogo di lavoro (art. 5) e classifica ad alto rischio i sistemi che valutano o monitorano i lavoratori (allegato III, punto 4). Nessun sistema automatico decide valutazioni o sanzioni (art. 22 GDPR; art. 4 l. 300/1970; l. 132/2025). Nessuna nuova fattispecie di licenziamento, nessun indebolimento del contraddittorio e del diritto di difesa.

| Variante | Contenuto | Costo a regime | Intensità | Fondo |
|---|---|---|---|---|
| PIENA | Indicatori di servizio obbligatori sopra i 50 dipendenti, cruscotto nazionale, piani di miglioramento, UPD associati in tutte le province (circa 100 nuclei per 2-3 persone, da organici esistenti, più formazione e piattaforma), pubblicazione dei dati per ente | 0,03 (dal 2028) | 1 | RIALLOCAZIONE (R12-1) |
| ESSENZIALE | Indicatori e cruscotto solo per amministrazioni centrali, Regioni e comuni sopra i 60.000 abitanti; UPD associati solo per i comuni sotto i 5.000 abitanti | 0,012 | 0,6 | RIALLOCAZIONE |
| ZERO | Direttiva del Ministro: applicazione della legge sul merito, piani di miglioramento come buona prassi, pubblicazione dei dati disciplinari per ente | 0 | 0,3 | — |

### Articolato normativo essenziale (disegno di legge "Disposizioni per la misurazione dei servizi pubblici e l'effettività della responsabilità nel lavoro pubblico")

**Art. 1 (Indicatori di servizio).** 1. All'articolo 6 del decreto-legge 9 giugno 2021, n. 80, convertito dalla legge 6 agosto 2021, n. 113, dopo il comma 2 è inserito il seguente: «2-bis. Le amministrazioni con più di cinquanta dipendenti indicano nel Piano da tre a cinque indicatori di servizio per ciascuna struttura che eroga servizi a cittadini o imprese: tempi di conclusione, arretrati, tasso di errore o di riesame, soddisfazione degli utenti. Gli indicatori sono calcolati dai sistemi informativi dell'amministrazione e sono pubblicati trimestralmente in formato aperto. La performance organizzativa misurata con tali indicatori costituisce il primo elemento della valutazione dei dirigenti responsabili.»

**Art. 2 (Piano di miglioramento).** 1. All'articolo 55-quater del decreto legislativo 30 marzo 2001, n. 165, dopo il comma 1 è inserito il seguente: «1-bis. Ai fini del comma 1, lettera f-quinquies), la prima valutazione negativa motivata dà luogo a un piano individuale di miglioramento della durata da sei a dodici mesi, definito dal dirigente con il dipendente, che può farsi assistere da un rappresentante sindacale. Il piano indica obiettivi, formazione, eventuali misure organizzative e di cambio di mansione, e tiene conto delle condizioni di salute e delle esigenze di cura. Il procedimento disciplinare per insufficiente rendimento può essere avviato solo dopo l'esito negativo del piano.»

**Art. 3 (Uffici per i procedimenti disciplinari in forma associata).** 1. All'articolo 55-bis del decreto legislativo n. 165 del 2001, dopo il comma 2 è inserito il seguente: «2-bis. I comuni con popolazione inferiore a 15.000 abitanti esercitano le funzioni dell'ufficio per i procedimenti disciplinari in forma associata, tramite le unioni di comuni o convenzioni ai sensi dell'articolo 30 del decreto legislativo 18 agosto 2000, n. 267, oppure avvalendosi dell'ufficio costituito presso la provincia o la città metropolitana.»

**Art. 4 (Trasparenza dei dati disciplinari).** 1. Il Dipartimento della funzione pubblica pubblica ogni anno, per ciascuna amministrazione, i dati aggregati sui procedimenti disciplinari avviati, conclusi, decaduti per inosservanza dei termini e sui tempi medi di conclusione, distinti per tipo di infrazione, compresa l'insufficienza di rendimento. Le celle con meno di cinque casi sono oscurate. 2. Il mancato esercizio dell'azione disciplinare e la decadenza per inerzia sono valutati ai sensi dell'articolo 55-sexies, comma 3, del decreto legislativo n. 165 del 2001 e incidono sulla retribuzione di risultato del dirigente responsabile.

**Art. 5 (Garanzie).** 1. La misurazione e la valutazione della prestazione individuale non possono essere effettuate mediante sistemi di riconoscimento biometrico, di riconoscimento delle emozioni o di monitoraggio continuo dell'attività. Nessuna valutazione o sanzione è adottata sulla base di un trattamento automatizzato. Restano fermi l'articolo 4 della legge 20 maggio 1970, n. 300, e il Regolamento (UE) 2024/1689.

**Art. 6 (Copertura finanziaria).** 1. Agli oneri, pari a 15 milioni per il 2027 e a 30 milioni annui dal 2028, si provvede mediante riduzione degli stanziamenti delle amministrazioni centrali per servizi esternalizzati di supporto amministrativo, individuati in apposito allegato.

### Cronoprogramma

| Fase | Chi | Cosa |
|---|---|---|
| Primi 100 giorni | Ministro PA; Funzione pubblica | Direttiva sull'attuazione della legge sul merito nel ciclo 2027; pubblicazione per ente dei dati disciplinari 2024-25; modello di piano di miglioramento concordato con ARAN e sindacati |
| 12 mesi | Parlamento; Funzione pubblica; ANCI e UPI | Legge approvata; primi indicatori di servizio nei PIAO 2028; UPD associati costituiti nelle province pilota |
| Fine legislatura | Tutte le amministrazioni sopra i 50 dipendenti | Cruscotto completo; primo triennio di valutazioni differenziate; rapporto pubblico su piani di miglioramento ed esiti |

### Indicatori

| KPI | Base | Obiettivo a 3 anni | Obiettivo a 5 anni |
|---|---|---|---|
| Quota di personale con valutazione massima | 98% (dichiarazione del Ministro, ripresa da OCPI 2026; dato ufficiale da costruire) | ≤ 30% per ufficio dirigenziale generale (legge sul merito) | ≤ 30%, con distribuzione pubblicata per ente |
| Procedimenti disciplinari ancora in corso o decaduti a 6 mesi dall'anno di avvio | 979 in corso su 11.328 (8,6%; 2024, Funzione pubblica) | ≤ 5% | ≤ 3% |
| Amministrazioni con indicatori di servizio pubblicati | non misurato (2026) | 60% di quelle sopra i 50 dipendenti | 100% |
| Piani di miglioramento conclusi positivamente | non esiste (2026) | dato rilevato | ≥ 60% |

*Volutamente non c'è un obiettivo di "più licenziamenti" né di "meno giorni di malattia". La malattia è un diritto; il numero di licenziamenti dipende da quanti illeciti avvengono. Si misurano invece la tempestività e l'effettività delle regole.*

### Rischi e garanzie per i lavoratori
- **Quota del 30% vissuta come arbitraria** → la quota riguarda il punteggio massimo, non le valutazioni negative. Chi non è nel 30% non è "bocciato". Albo dei valutatori e criteri pubblici.
- **Piano di miglioramento usato come strumento di pressione** → assistenza sindacale, obiettivi scritti e verificabili, ricorso al Comitato unico di garanzia. Il piano non è una sanzione e non compare nel fascicolo disciplinare se va a buon fine.
- **Mobbing o uso discriminatorio** → dati sui piani disaggregati per genere, età e disabilità; verifica del CUG.
- **Indicatori "truccati"** → calcolo automatico dai sistemi informativi, verifica a campione dell'OIV, pubblicazione dei dati grezzi (09-C1).
- **Privacy dei dati disciplinari** → solo aggregati per ente, celle sotto 5 casi oscurate, parere del Garante.

---

## 09-C7 — Automazione dei processi ripetitivi con riallocazione garantita

*In una frase: le macchine fanno il lavoro ripetitivo, come protocollare, ricopiare dati e controllare documenti standard, e le persone si spostano dove servono di più: sportello, controlli, arretrati, assistenza alle persone più fragili; nessuna persona perde il posto per l'automazione.*

**Problema in un dato.** Nei Paesi ad alto reddito il **9,6%** dei posti di lavoro femminili rientra nella fascia di massima esposizione all'IA generativa, contro il 3,5% di quelli maschili. Le mansioni d'ufficio sono le più esposte (ILO, *WP 140*, 2025). Nella PA italiana l'adozione è appena iniziata e frammentata: **45 enti su 108** censiti hanno iniziative di IA, con 120 progetti in tutto (AgID, censimento 2025). Non esiste una mappa dei processi ripetitivi né una regola su dove va il tempo liberato.

**Lezioni dall'estero.**
- **Regno Unito**: il Governo stima 45 mld £ l'anno di risparmi potenziali dalla digitalizzazione. In Parlamento la stima è stata criticata perché ipotizza che il 100% dei compiti di routine sia automatizzabile (Commissione della Camera dei Comuni, ottobre 2025). La sperimentazione di assistenti IA su circa 20.000 dipendenti ha misurato un risparmio di quasi due settimane l'anno a testa (gov.uk, 2025). **Lezione**: misurare prima di promettere tagli.
- **Danimarca**: i servizi semplici sono stati concentrati in un'unità centrale e i casi complessi restano agli enti, con il coinvolgimento dei sindacati, che hanno accompagnato i cambiamenti (OSE, *Digiqualpub*, 2023). **Lezione**: riconfigurare il lavoro, non sostituirlo.
- **Estonia**: Bürokratt è una rete di assistenti virtuali interoperabili per i servizi pubblici. I servizi "proattivi", che partono da un evento della vita del cittadino senza domanda, avevano un obiettivo di 10 entro il 2025 (RIA; Ministero della Giustizia e del Digitale). **Lezione**: l'automazione utile parte dai dati già posseduti, cioè dall'once-only (09-C2).
- **Portogallo**: SIMPLEX è un programma annuale di semplificazione con misure pubbliche e tassi di esecuzione dichiarati, per esempio l'85% nel 2020-21 (stampa nazionale). **Lezione**: un calendario pubblico misura dopo misura.
- **OCSE** (*Governing with AI*, 2025): la maggior parte delle iniziative resta pilota. Avverte del rischio di usare l'IA per sostituire invece che potenziare il personale e chiede un dialogo trasparente con dipendenti e sindacati.

**Soluzione in 4 punti.**
1. **Mappa nazionale dei processi ripetitivi.** In 12 mesi ogni amministrazione centrale, e ogni Regione o grande comune che aderisce, censisce i processi di back-office ad alto volume con un metodo comune AgID/Funzione pubblica: protocollo, data entry, verifiche documentali standard, rendicontazioni, risposte a domande frequenti. Per ciascuno stima le ore impiegate.
2. **Fondo per l'automazione 2027-29** su programmi di coesione: progetti di automazione (RPA, IA generativa per bozze e sintesi tramite l'assistente condiviso di 09-C5, regole decisionali trasparenti) scelti per **ore liberate per euro**. Le soluzioni sono riusabili, open source su Developers Italia, e iscritte nell'albo di 09-C5.
3. **Patto di riallocazione** firmato con ARAN e sindacati prima di ogni progetto. Il tempo liberato va per almeno il 70% a funzioni a contatto con i cittadini o di controllo; chi cambia mansione riceve formazione retribuita (09-C8). **Nessun licenziamento e nessun trasferimento d'ufficio fuori dal comune di servizio a causa dell'automazione.**
4. **Contabilità delle ore e dei risparmi certificati.** Ogni anno AgID e RGS certificano le ore liberate e come sono state riallocate. Solo i posti di turnover che risultano **non più necessari dopo la certificazione** possono non essere sostituiti, e il risparmio si registra **ex post**. Prima della certificazione non copre nulla.

| Variante | Contenuto | Costo | Intensità | Fondi |
|---|---|---|---|---|
| PIENA | Mappa per tutte le amministrazioni centrali, Regioni e comuni sopra i 60.000 abitanti; fondo da 0,15 l'anno nel 2028-29; centro di competenza AgID/DTD permanente, manutenzione delle soluzioni, certificazione | 0,20 al picco 2028-29 (0,15 coesione + 0,05 permanenti); 0,05 dal 2030 | 1 | COESIONE_2127 0,15 (una tantum); RIALLOCAZIONE 0,05 (R12-1) |
| ESSENZIALE | Solo amministrazioni centrali ed enti previdenziali e fiscali (INPS, Agenzie), dove i volumi sono più alti | 0,07 al picco (0,05 + 0,02); 0,02 dal 2030 | 0,5 | COESIONE_2127 0,05; RIALLOCAZIONE 0,02 |
| PILOTA | 3 amministrazioni (un ministero, una Regione del Mezzogiorno, un grande comune) per 3 anni, con valutazione indipendente delle ore liberate | 0,02 solo 2027-29 | 0,15 | COESIONE_2127 |

### Articolato normativo essenziale (decreto legislativo, su delega nel DDL di 09-C6, e accordo quadro ARAN)

**Art. 1 (Finalità).** 1. Il presente decreto promuove l'automazione delle attività ripetitive delle pubbliche amministrazioni per migliorare la qualità e la tempestività dei servizi e per riallocare il lavoro verso le funzioni a maggior valore per i cittadini, nel rispetto dell'articolo 97 della Costituzione, della legge 23 settembre 2025, n. 132, e del Regolamento (UE) 2024/1689.

**Art. 2 (Mappa dei processi).** 1. Entro dodici mesi le amministrazioni di cui all'articolo 1, comma 2, della legge 31 dicembre 2009, n. 196, censiscono i processi di supporto ad alto volume secondo il metodo definito con decreto del Ministro per la pubblica amministrazione, sentita l'AgID. Il censimento, comprensivo delle ore di lavoro stimate, è allegato al Piano integrato di attività e organizzazione e pubblicato in formato aperto.

**Art. 3 (Fondo per l'automazione).** 1. È istituito presso il Dipartimento per la trasformazione digitale il Fondo per l'automazione dei processi amministrativi, alimentato per il triennio 2027-2029 dalle risorse dei programmi della politica di coesione 2021-2027, obiettivo strategico 1. 2. I progetti sono selezionati in base alle ore di lavoro liberate per euro investito. Il codice sorgente è rilasciato con licenza aperta ai sensi dell'articolo 69 del decreto legislativo 7 marzo 2005, n. 82.

**Art. 4 (Riallocazione e garanzie).** 1. L'avvio di un progetto di automazione è preceduto dall'informazione e dal confronto con le organizzazioni sindacali ai sensi del contratto collettivo e dell'articolo 26, paragrafo 7, del Regolamento (UE) 2024/1689. 2. Almeno il 70 per cento delle ore liberate è destinato a funzioni di sportello, assistenza, controllo o smaltimento degli arretrati, secondo un piano di riallocazione allegato al progetto. 3. L'automazione non costituisce causa di licenziamento né di collocamento in disponibilità ai sensi dell'articolo 33 del decreto legislativo 30 marzo 2001, n. 165. Il personale interessato ha diritto a un percorso di riqualificazione retribuito. 4. I sistemi automatizzati non adottano provvedimenti con effetti giuridici senza la revisione motivata di un funzionario, ai sensi della disciplina di cui alla proposta 09-C5.

**Art. 5 (Certificazione).** 1. L'AgID e la Ragioneria generale dello Stato certificano ogni anno le ore liberate e la loro riallocazione. 2. Le minori esigenze di personale accertate in sede di certificazione possono essere considerate nella determinazione delle facoltà assunzionali dell'anno successivo. Le relative economie non sono utilizzate a copertura di nuove spese prima della certificazione.

**Art. 6 (Copertura finanziaria).** 1. Agli oneri per il centro di competenza e la manutenzione, pari a 50 milioni annui dal 2028, si provvede mediante riduzione degli stanziamenti delle amministrazioni centrali per servizi esternalizzati di supporto amministrativo, quali data entry, dematerializzazione e contact center di primo livello. Agli oneri di cui all'articolo 3 si provvede nei limiti delle risorse della coesione riprogrammate d'intesa con la Commissione europea.

### Cronoprogramma

| Fase | Chi | Cosa |
|---|---|---|
| Primi 100 giorni | Ministro PA, DTD, ARAN, sindacati | Accordo quadro sul patto di riallocazione; metodo di mappatura AgID; scelta delle 3 amministrazioni pilota; avvio della riprogrammazione della coesione |
| 12 mesi | Tutte le amministrazioni centrali | Mappa pubblicata; primi 20 progetti finanziati; primo rapporto sulle ore liberate nel pilota |
| Fine legislatura | AgID, RGS, Funzione pubblica | Seconda certificazione; soluzioni riusate da almeno 100 enti; decisione sul passaggio dal pilota alla variante ESSENZIALE o PIENA |

### Indicatori

| KPI | Base | Obiettivo a 3 anni | Obiettivo a 5 anni |
|---|---|---|---|
| Processi ad alto volume mappati con ore stimate | 0 (nessuna mappa nazionale, 2026) | 100% delle amministrazioni centrali | anche Regioni e grandi comuni aderenti |
| Ore liberate certificate e riallocate verso servizi | non misurato (2026) | ≥ 2% delle ore di back-office censite | ≥ 5% |
| Quota delle ore liberate destinata a sportello, controlli e arretrati | — | ≥ 70% | ≥ 70% |
| Licenziamenti o collocamenti in disponibilità per automazione | 0 | 0 | 0 |
| Tempi medi dei procedimenti automatizzati | da rilevare nella mappa | -20% | -30% |

### Rischi e garanzie per i lavoratori
- **Automazione usata come pretesto per tagli lineari** → nessun risparmio contato prima della certificazione; garanzia di legge contro licenziamenti e disponibilità; patto firmato prima di ogni progetto.
- **Promesse gonfiate (caso britannico)** → obiettivi in ore misurate, non in miliardi stimati; valutazione indipendente del pilota.
- **Errori automatici sui diritti dei cittadini** → albo e valutazione d'impatto di 09-C5; revisione umana; ricorso semplice. I sistemi per l'accesso a prestazioni pubbliche sono ad alto rischio (AI Act, allegato III, punto 5): gli obblighi valgono dal 2.12.2027 dopo il rinvio del *Digital Omnibus* (Reg. UE 2026/1744, da verificare), ma GovernAI li applica da subito.
- **Effetto sproporzionato sulle donne**, più presenti nelle mansioni impiegatizie esposte (ILO 2025) → la riqualificazione dà priorità al personale delle aree più esposte; dati disaggregati per genere.
- **Lavoratori delle ditte esternalizzate** (R12-1) → clausola sociale nei nuovi affidamenti e accesso ai percorsi di riqualificazione e ai concorsi con riserva nei limiti dell'art. 97 Cost.

---

## 09-C8 — "Staffetta delle competenze": il ricambio generazionale come occasione di riqualificazione

*In una frase: nei prossimi dieci anni andrà in pensione fino a un terzo del personale pubblico; invece di sostituire ogni uscita con lo stesso profilo, ogni posto si ripensa: si assume chi serve davvero, si riqualifica chi c'è, e chi va in pensione trasmette ciò che sa.*

**Problema in un dato.** Gli oltre **3,7 milioni** di lavoratori pubblici con almeno una giornata retribuita nel 2024 hanno un'età media alta: il **76,6%** ha almeno 40 anni e **661.919** (17,7%) sono nella fascia 55-59. L'INPS stima che **al massimo un terzo** andrà in pensione entro dieci anni (Osservatorio sui lavoratori pubblici, 11.11.2025). Oggi i fabbisogni si programmano soprattutto per sostituzione del profilo uscente. La formazione prevista, 40 ore annue per dipendente secondo la direttiva del Ministro per la PA del 14.1.2025 (dato da verificare sul testo), non è legata ai cambi di mansione.

**Soluzione in 4 punti.**
1. **Fabbisogni per competenze, non per sostituzione.** Ogni cessazione prevista nei 3 anni del PIAO si accompagna a una decisione motivata e pubblica: (i) sostituire con lo stesso profilo; (ii) assumere un profilo diverso, tecnico o digitale; (iii) coprire con personale interno riqualificato; (iv) non sostituire, perché l'attività è automatizzata e certificata secondo 09-C7. La quota per i tecnici di 09-C3 resta riservata.
2. **Affiancamento sui posti critici.** Per i posti con competenze uniche, come il responsabile di un sistema informativo, l'ultimo esperto di un procedimento o il tecnico di un piccolo comune, il successore è assunto **4 mesi prima** dell'uscita. Il trasferimento delle conoscenze è documentato, anche con l'assistente di 09-C5 per costruire manuali e basi di conoscenza.
3. **Diritto e dovere di riqualificazione.** Chi cambia mansione per riorganizzazione o automazione ha diritto a un percorso certificato (Syllabus, SNA, università) dentro l'orario di lavoro e le 40 ore annue già previste, e il dovere di seguirlo. Nell'"Accademia delle competenze pubbliche" (SNA + Funzione pubblica) servono percorsi brevi su dati, appalti, front-office e assistenza digitale.
4. **Mobilità facilitata.** Le posizioni libere per riqualificazione sono pubblicate su inPA prima dei concorsi esterni, con priorità per il personale delle funzioni automatizzate. È sempre volontaria fuori dal comune di servizio.

| Variante | Contenuto | Costo | Intensità | Fondi |
|---|---|---|---|---|
| PIENA | Fabbisogni per competenze in tutti i PIAO; affiancamento su circa 7.500 posti critici l'anno; Accademia nazionale; formazione aggiuntiva su FSE+ fino al 2029 | 0,23 fino al 2029 (0,18 + 0,05 FSE+); 0,18 dal 2030 | 1 | RIALLOCAZIONE 0,18 (R12-1 + RA13); COESIONE_2127 0,05 |
| ESSENZIALE | Fabbisogni per competenze; affiancamento su circa 2.250 posti critici l'anno, con priorità a piccoli comuni, sanità amministrativa e sistemi informativi; Accademia ridotta | 0,08 (0,06 + 0,02 FSE+); 0,06 dal 2030 | 0,4 | RIALLOCAZIONE 0,06; COESIONE_2127 0,02 |
| ZERO | Solo regole: fabbisogni per competenze nel PIAO, priorità di mobilità interna, diritto alla riqualificazione nelle 40 ore esistenti | 0 | 0,25 | — |

**Come si stima il costo (stima GovernAI).** Costo medio per dipendente: 203,3 mld di redditi da lavoro dipendente (Eurostat 2025) diviso circa 3,37 milioni di dipendenti, cioè circa 60.000 € l'anno. Quattro mesi di sovrapposizione valgono circa 20.000 € per posto. 7.500 posti × 20.000 € = 0,15 mld, più 0,03 per l'Accademia = 0,18. I 7.500 posti sono circa il 6% delle uscite annue stimate (fino a circa 120.000 l'anno sulla base INPS).

### Articolato normativo essenziale (articolo della legge di bilancio 2027 e modifiche al d.lgs. 165/2001)

**Art. 1 (Piano dei fabbisogni per competenze).** 1. All'articolo 6 del decreto legislativo 30 marzo 2001, n. 165, dopo il comma 2 è inserito il seguente: «2-bis. Per ciascuna cessazione prevista nel triennio il piano indica, con motivazione pubblica, se il posto è coperto con lo stesso profilo, con un profilo diverso, mediante riqualificazione del personale in servizio o non è coperto in ragione dell'automazione certificata delle relative attività. Restano ferme le riserve a favore dei profili tecnici previste dalla legge.»

**Art. 2 (Affiancamento sui posti critici).** 1. In deroga ai limiti di cui all'articolo 3 del decreto-legge 24 giugno 2014, n. 90, convertito dalla legge 11 agosto 2014, n. 114, le amministrazioni possono assumere il successore fino a quattro mesi prima della cessazione programmata di personale titolare di posizioni individuate come critiche nel piano di cui all'articolo 6, comma 2-bis, del decreto legislativo n. 165 del 2001, nei limiti del Fondo di cui al comma 2. 2. È istituito presso il Dipartimento della funzione pubblica il Fondo per l'affiancamento generazionale, con una dotazione di 150 milioni annui dal 2029 (60 milioni nel 2027, 120 milioni nel 2028), ripartito tra le amministrazioni con priorità per i comuni con meno di 5.000 abitanti.

**Art. 3 (Diritto alla riqualificazione).** 1. Il dipendente le cui mansioni sono modificate per riorganizzazione o automazione ha diritto a un percorso di riqualificazione certificato, svolto in orario di lavoro, e ha l'obbligo di seguirlo. 2. La Scuola nazionale dell'amministrazione, d'intesa con il Dipartimento della funzione pubblica, istituisce l'Accademia delle competenze pubbliche.

**Art. 4 (Mobilità interna prioritaria).** 1. Le posizioni da coprire mediante riqualificazione sono pubblicate sul Portale del reclutamento inPA prima dell'avvio di procedure esterne. Il personale interessato da processi di automazione ha priorità. La mobilità fuori dal comune di servizio richiede il consenso del dipendente.

**Art. 5 (Copertura finanziaria).** 1. Agli oneri, pari a 60 milioni nel 2027, 150 milioni nel 2028 e 180 milioni annui dal 2029, si provvede mediante riduzione degli stanziamenti per servizi esternalizzati di supporto amministrativo e nell'ambito della revisione della spesa dei Ministeri. Agli oneri formativi aggiuntivi, pari a 50 milioni annui nel triennio 2027-2029, si provvede a valere sul FSE+ 2021-2027.

### Cronoprogramma

| Fase | Chi | Cosa |
|---|---|---|
| Primi 100 giorni | Funzione pubblica, INPS, RGS | Stima ente per ente delle cessazioni 2027-2031 dai dati INPS e del Conto annuale; modello del piano dei fabbisogni per competenze; individuazione dei primi posti critici |
| 12 mesi | Tutte le amministrazioni; SNA | PIAO 2028 con fabbisogni per competenze; Fondo per l'affiancamento operativo; primi percorsi dell'Accademia |
| Fine legislatura | Funzione pubblica | Rapporto pubblico: posti ripensati, riqualificati, affiancati; età media e quota di profili tecnici; decisione sul passaggio alla variante PIENA |

### Indicatori

| KPI | Base | Obiettivo a 3 anni | Obiettivo a 5 anni |
|---|---|---|---|
| Cessazioni con decisione motivata nel piano dei fabbisogni | non rilevato (2026) | 80% | 100% |
| Posti critici coperti con affiancamento | 0 (istituto inesistente, 2026) | ≥ 5.000 l'anno (PIENA) | ≥ 7.500 l'anno |
| Personale riqualificato e ricollocato su nuove mansioni | non misurato | ≥ 20.000 cumulati | ≥ 50.000 cumulati |
| Età media dei dipendenti stabili | 49 anni e 4 mesi (RGS, Conto annuale 2024, via stampa) | in calo | ≤ 47 anni |

### Rischi e garanzie per i lavoratori
- **"Non sostituire" diventa un taglio occulto** → l'opzione (iv) vale solo dopo la certificazione di 09-C7, ed è motivata e pubblica. Ogni anno si pubblica il saldo tra uscite e ingressi per funzione, con attenzione a scuola e sanità, dove i servizi non vanno ridotti.
- **Riqualificazione di facciata** → percorsi certificati con verifica delle competenze; indicatore di ricollocazione effettiva.
- **Lavoratrici e lavoratori più anziani spinti all'uscita** → nessun incentivo all'esodo e nessuna pressione: l'affiancamento riguarda chi esce per requisiti già maturati.
- **Divari territoriali** → priorità del Fondo ai piccoli comuni e al Mezzogiorno, dove l'uscita di una sola persona può fermare un ufficio.
- **Coesione non riprogrammabile** → la parte FSE+ è solo aggiuntiva: senza di essa la formazione resta nelle 40 ore esistenti.

---

## Fonti principali

- Dipartimento della Funzione pubblica, *Procedimenti disciplinari 2024*, dati al 30.6.2025 — https://www.funzionepubblica.gov.it/media/tsnma1ts/procedimentidisciplinari2024.pdf (verificato sul testo).
- INPS, Osservatorio sui lavoratori pubblici, 11.11.2025 (via Sky TG24, ANSA, informazionefiscale.it; primario non consultato).
- RGS, Conto annuale 2024 (età media, dipendenti; via stampa, primario non raggiungibile — vedi `dati/verifiche/09_pa_digitale.md`).
- CGIA su dati INPS, giornate di malattia 2023 (via lentepubblica.it; secondaria).
- OCPI, *La riforma del merito nella PA*, 2026; Corte dei conti, delib. 62/2024/G (via stampa); ddl AS 1778 "merito", approvazione definitiva 30.6/1.7.2026 (lentepubblica.it; numero di legge da verificare in GU).
- AgID, censimento IA nella PA, 2025 (via lentepubblica.it).
- ILO, *Generative AI and jobs: a refined global index of occupational exposure*, WP 140, 2025.
- OCSE, *Governing with Artificial Intelligence*, 2025.
- Regno Unito: gov.uk (sperimentazione degli assistenti IA, 2025); The Register e Computer Weekly sull'audizione parlamentare dell'ottobre 2025 sui 45 mld £.
- Danimarca: OSE, *Digiqualpub* Research Paper 53, 2023. Estonia: RIA, Bürokratt; servizi proattivi. Portogallo: SIMPLEX, rapporti di esecuzione (stampa).
- Reg. UE 2024/1689 (AI Act), art. 5, 26, 27, allegato III; *Digital Omnibus* sull'IA (rinvio dell'allegato III al 2.12.2027; estremi da verificare in GUUE).
- Normativa: d.lgs. 165/2001 artt. 6, 33, 55-bis, 55-quater, 55-quinquies, 55-sexies; d.lgs. 150/2009 e d.lgs. 74/2017; d.lgs. 116/2016; d.lgs. 75/2017; d.lgs. 118/2017; d.l. 80/2021 art. 6 (PIAO); l. 56/2019; l. 300/1970 art. 4; l. 132/2025.
