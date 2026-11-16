# Cinquant'anni di decisioni pubbliche in Italia (1977-2026): che cosa ha funzionato

Catalogo ragionato di 120 decisioni di politica pubblica, con gli effetti documentati e una lezione per GovernAI. Dati completi in `decisioni_1977_2026.csv` (una riga per decisione, con fonti).

## Metodo

- **Che cosa è una decisione.** Una legge, un decreto, un accordo o un atto di governo con effetti rilevanti e identificabili. Non sono incluse vicende giudiziarie o politiche in sé (per esempio Mani pulite), ma le norme che ne sono seguite.
- **Chi l'ha presa.** Ogni riga indica il "governo in carica nel <anno>" e il nome della o del Presidente del Consiglio come dato storico. Per le leggi si considera il governo in carica alla data dell'atto (o dell'approvazione parlamentare, quando indicato). Si valuta la decisione, non chi l'ha presa; non si indicano partiti.
- **Fatti, stime, opinioni.** Nella colonna `effetti_misurati` le frasi iniziano o sono marcate come *fatto* (dato osservato, senza nesso causale dimostrato), *stima* (risultato di un modello o di una valutazione) o *opinione* (giudizio di un'istituzione o della letteratura). Quando due fonti serie divergono sono riportate entrambe.
- **Giudizio sull'evidenza** (sulla decisione rispetto al suo obiettivo dichiarato): *efficace*; *efficace in parte* (obiettivo raggiunto con costi o effetti collaterali rilevanti, o solo in parte); *inefficace*; *effetti negativi* (danni documentati superiori ai benefici o violazioni accertate); *evidenza insufficiente* (mancano valutazioni o i dati non permettono di separare l'effetto). 
- **Solidità dell'evidenza.** *Alta*: almeno una valutazione controfattuale pubblicata (esperimento, discontinuità, differenze nelle differenze) o un accertamento giuridico definitivo. *Media*: dati ufficiali coerenti e analisi istituzionali (Banca d'Italia, UPB, Corte dei conti, RGS, ISTAT) senza un controfattuale pieno. *Bassa*: ricostruzioni descrittive, opinioni, dati parziali.
- **Cifre.** Solo cifre presenti nelle fonti citate; dove la cifra non è verificata è scritto "n.d." oppure "da verificare". Le serie lunghe (debito, crescita, occupazione) sono trattate in un lavoro parallelo e qui sono citate solo come contesto.
- **Fonti.** Testo dell'atto su Normattiva (link URN), sentenze della Corte costituzionale e della Corte di giustizia UE, pubblicazioni di Banca d'Italia, UPB, Corte dei conti, RGS, ISTAT, INPS, OCSE, Commissione UE e articoli accademici. Per alcune fonti istituzionali il link porta alla pagina dell'archivio, non al singolo documento; per tre articoli accademici è data la citazione bibliografica completa.
- **Equilibrio.** Il catalogo copre tutti i decenni e tutti i governi con decisioni di peso; il numero di righe per Presidente del Consiglio riflette la durata in carica e la densità legislativa, non un giudizio. La tabella di conteggio è in fondo.

## Il quadro in numeri

| Decennio | Decisioni | efficace | efficace in parte | inefficace | effetti negativi | evidenza insufficiente |
|---|---|---|---|---|---|---|
| 1977-1979 | 8 | 0 | 4 | 1 | 1 | 2 |
| 1980-1989 | 10 | 0 | 3 | 1 | 1 | 5 |
| 1990-1999 | 29 | 4 | 18 | 1 | 1 | 5 |
| 2000-2009 | 25 | 2 | 11 | 3 | 5 | 4 |
| 2010-2019 | 30 | 1 | 16 | 2 | 2 | 9 |
| 2020-2026 | 18 | 1 | 4 | 0 | 1 | 12 |
| **Totale** | **120** | **8** | **56** | **8** | **11** | **37** |

Solidità dell'evidenza: alta 14, media 57, bassa 49.

Un dato salta subito all'occhio: per circa un terzo delle decisioni l'evidenza è insufficiente, e solo una minoranza ha una valutazione controfattuale. Per mezzo secolo lo Stato italiano ha deciso molto e misurato poco.

## 1977-1979

Anni di inflazione a due cifre e di grandi leggi di sistema: nascono il Servizio sanitario nazionale, la legge finanziaria, l'equo canone, l'inclusione scolastica; l'Italia entra nello SME. Molte di queste scelte hanno cambiato il paese in modo duraturo, ma quasi nessuna è stata accompagnata da strumenti per misurarne gli effetti o da coperture stabili.

**D001 · 1977 · Inserimento degli alunni con disabilità nelle classi comuni**  
*L. 4 agosto 1977, n. 517* · governo in carica nel 1977 (Presidente del Consiglio: Giulio Andreotti) · ambito: scuola  
Cosa cambia: Chiude le classi differenziali; introduce l'insegnante di sostegno e la programmazione educativa.  
Conti: n.d.  
Effetti: Fatto: l'Italia è tra i pochi paesi con inclusione quasi totale nelle classi comuni. ISTAT documenta però carenze di insegnanti di sostegno specializzati e di accessibilità. Nessuna stima controfattuale sugli apprendimenti.  
Giudizio: **efficace in parte** · evidenza bassa

**D002 · 1977 · Piano straordinario per l'occupazione giovanile**  
*L. 1 giugno 1977, n. 285* · governo in carica nel 1977 (Presidente del Consiglio: Giulio Andreotti) · ambito: lavoro  
Cosa cambia: Liste speciali, incentivi alle assunzioni e contratti di formazione per giovani; una parte dei posti nella pubblica amministrazione.  
Conti: n.d.  
Effetti: Ricostruzioni storiche: pochi inserimenti nelle imprese private; molti contratti assorbiti stabilmente dalla PA con leggi successive. Nessuna valutazione controfattuale.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D003 · 1977 · Trasferimento di funzioni amministrative alle Regioni**  
*D.P.R. 24 luglio 1977, n. 616* · governo in carica nel 1977 (Presidente del Consiglio: Giulio Andreotti) · ambito: istituzioni  
Cosa cambia: Completa il passaggio alle Regioni di assistenza, sanità, urbanistica, agricoltura e altre materie.  
Conti: Spesa trasferita senza autonomia di entrata corrispondente (finanza regionale derivata).  
Effetti: Fatto: nasce un modello in cui le Regioni spendono ma non rispondono delle entrate; il nodo resterà aperto fino al federalismo fiscale del 2009 e oltre. Effetti su qualità dei servizi non misurati.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D004 · 1978 · Chiusura dei manicomi (legge Basaglia)**  
*L. 13 maggio 1978, n. 180* · governo in carica nel 1978 (Presidente del Consiglio: Giulio Andreotti) · ambito: sanità  
Cosa cambia: Abolisce il ricovero manicomiale; i trattamenti passano a servizi territoriali e reparti negli ospedali generali.  
Conti: n.d.  
Effetti: Fatto: chiusura completa degli ospedali psichiatrici solo alla fine degli anni '90 (attuazione lenta). Qualità e diffusione dei servizi territoriali molto diverse tra Regioni. Nessuna valutazione controfattuale sugli esiti di salute.  
Giudizio: **efficace in parte** · evidenza bassa

**D005 · 1978 · Equo canone per gli affitti**  
*L. 27 luglio 1978, n. 392* · governo in carica nel 1978 (Presidente del Consiglio: Giulio Andreotti) · ambito: casa  
Cosa cambia: Canoni fissati per legge in base a parametri dell'immobile; durata minima dei contratti.  
Conti: Nessun costo diretto.  
Effetti: Opinione diffusa tra gli economisti e fatto storico: l'offerta di case in affitto si è ridotta e si è diffuso il mercato non regolare; la legge è stata superata dai patti in deroga (1992) e dalla L. 431/1998. Nessuna stima controfattuale solida.  
Giudizio: **effetti negativi** · evidenza bassa

**D006 · 1978 · Istituzione del Servizio sanitario nazionale**  
*L. 23 dicembre 1978, n. 833* · governo in carica nel 1978 (Presidente del Consiglio: Giulio Andreotti) · ambito: sanità  
Cosa cambia: Sostituisce le mutue con un servizio universale finanziato dalla fiscalità generale e gestito dalle USL.  
Conti: Negli anni '80 la spesa sanitaria supera sistematicamente gli stanziamenti; i disavanzi vengono ripianati a posteriori.  
Effetti: Fatto: copertura universale. Aspettativa di vita italiana tra le più alte OCSE (dato, non effetto causale isolato). Problemi documentati: disavanzi strutturali, divari regionali di qualità.  
Giudizio: **efficace in parte** · evidenza media

**D007 · 1978 · Riforma della contabilità dello Stato e nascita della legge finanziaria**  
*L. 5 agosto 1978, n. 468* · governo in carica nel 1978 (Presidente del Consiglio: Giulio Andreotti) · ambito: conti pubblici  
Cosa cambia: Introduce bilancio pluriennale, legge finanziaria annuale e saldo netto da finanziare.  
Conti: Obiettivo: controllare la spesa. Negli anni '80 il disavanzo resta elevato.  
Effetti: Opinione prevalente (Corte dei conti, letteratura di finanza pubblica): la finanziaria diventa veicolo di micro-spese; riforme correttive nel 1988 e 1999. Nessuna misura causale.  
Giudizio: **inefficace** · evidenza bassa

**D008 · 1978 · Ingresso nello SME con banda larga di oscillazione**  
*Adesione al Sistema monetario europeo (risoluzione parlamentare dicembre 1978; operativo da marzo 1979)* · governo in carica nel 1978 (Presidente del Consiglio: Giulio Andreotti) · ambito: moneta  
Cosa cambia: Vincolo esterno sul cambio della lira; svalutazioni concordate al posto di quelle unilaterali.  
Conti: n.d.  
Effetti: Fatti: inflazione scesa gradualmente negli anni '80 con diversi riallineamenti della lira; uscita dagli accordi di cambio nel settembre 1992. Opinione diffusa: il vincolo esterno ha sostenuto la disinflazione ma non ha sostituito il risanamento dei conti.  
Giudizio: **efficace in parte** · evidenza media

## 1980-1989

Decennio con meno decisioni nel catalogo: le grandi riforme strutturali sono state poche e quasi nessuna è stata valutata. È il decennio della disinflazione e del debito. La banca centrale smette di finanziare il Tesoro, l'indicizzazione dei salari viene ridotta, ma i disavanzi primari restano alti e il debito cresce rapidamente. Compaiono i primi condoni edilizi e l'intervento straordinario nel Mezzogiorno arriva alla fase finale. Le valutazioni controfattuali sono rare.

**D009 · 1981 · Divorzio tra Tesoro e Banca d'Italia**  
*Lettera del Ministro del Tesoro al Governatore della Banca d'Italia (febbraio 1981)* · governo in carica nel 1981 (Presidente del Consiglio: Arnaldo Forlani) · ambito: conti pubblici  
Cosa cambia: La Banca d'Italia non è più obbligata ad acquistare i titoli di Stato rimasti invenduti alle aste.  
Conti: Spesa per interessi in forte crescita negli anni '80 con tassi reali positivi.  
Effetti: Fatti: inflazione da circa 19% (1981) a circa 6% (fine anni '80). Due letture: (a) critica: il divorzio ha fatto esplodere il debito; (b) Osservatorio CPI: il debito cresce soprattutto per disavanzi primari persistenti (circa 3% del PIL), non per il divorzio in sé. Le analisi accademiche sostengono in prevalenza la lettura (b).  
Giudizio: **efficace in parte** · evidenza media

**D010 · 1982 · Reati tributari (legge detta 'manette agli evasori')**  
*D.L. 10 luglio 1982, n. 429 (conv. L. 516/1982)* · governo in carica nel 1982 (Presidente del Consiglio: Giovanni Spadolini) · ambito: fisco  
Cosa cambia: Introduce sanzioni penali per frodi e omesse dichiarazioni.  
Conti: n.d.  
Effetti: Nessuna misura dell'effetto sull'evasione; la disciplina è stata riscritta nel 2000 (D.Lgs. 74/2000). Molti processi finivano in prescrizione (fatto riportato dalla dottrina).  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D011 · 1984 · Taglio di punti di scala mobile (decreto di San Valentino); referendum confermativo di fatto nel 1985**  
*D.L. 17 aprile 1984, n. 70 (conv. L. 219/1984)* · governo in carica nel 1984 (Presidente del Consiglio: Bettino Craxi) · ambito: lavoro  
Cosa cambia: Riduce per legge l'indicizzazione automatica dei salari ai prezzi.  
Conti: Effetto indiretto via minore inflazione e minore spesa indicizzata; n.d.  
Effetti: Fatti ISTAT: inflazione da circa 15% (1983) a circa 11% (1984) e 9% (1985). Concausa: calo del prezzo del petrolio e del dollaro dal 1985. Nessuna stima causale separata. Il referendum abrogativo del 1985 non passò.  
Giudizio: **efficace in parte** · evidenza media

**D012 · 1984 · Contratti di formazione e lavoro con sgravi contributivi**  
*L. 19 dicembre 1984, n. 863* · governo in carica nel 1984 (Presidente del Consiglio: Bettino Craxi) · ambito: lavoro  
Cosa cambia: Contratti a termine per giovani con formazione e contributi ridotti.  
Conti: Sgravi contributivi; costo complessivo n.d.  
Effetti: La Commissione UE giudicò parte degli sgravi aiuti di Stato non compatibili (decisione della Commissione del 1999, ricorso dell'Italia respinto dalla Corte di giustizia nel 2002). Effetti occupazionali netti non stimati in modo controfattuale.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D013 · 1985 · Primo condono edilizio generale**  
*L. 28 febbraio 1985, n. 47* · governo in carica nel 1985 (Presidente del Consiglio: Bettino Craxi) · ambito: territorio  
Cosa cambia: Sanatoria delle opere abusive dietro pagamento di un'oblazione.  
Conti: Entrate una tantum; costi per urbanizzazioni a carico dei Comuni (n.d.).  
Effetti: Fatto: seguiti da condoni nel 1994 e 2003; ISTAT (BES) misura ancora molte costruzioni abusive ogni 100 autorizzate, soprattutto nel Mezzogiorno. Opinione diffusa (Corte dei conti, urbanisti): l'attesa di nuovi condoni incentiva nuovi abusi. Nesso causale non stimato.  
Giudizio: **effetti negativi** · evidenza media

**D014 · 1985 · Vincolo paesaggistico su coste, fiumi, montagne (legge Galasso)**  
*L. 8 agosto 1985, n. 431* · governo in carica nel 1985 (Presidente del Consiglio: Bettino Craxi) · ambito: ambiente  
Cosa cambia: Tutela per categorie di beni e obbligo di piani paesistici regionali.  
Conti: Nessun costo diretto.  
Effetti: Fatto: molti piani paesistici approvati con grande ritardo; la tutela è confluita nel Codice dei beni culturali (2004). Nessuna misura di impatto sul consumo di suolo.  
Giudizio: **efficace in parte** · evidenza bassa

**D015 · 1986 · Ultima fase dell'intervento straordinario (dopo la chiusura della Cassa per il Mezzogiorno nel 1984)**  
*L. 1 marzo 1986, n. 64* · governo in carica nel 1986 (Presidente del Consiglio: Bettino Craxi) · ambito: Mezzogiorno  
Cosa cambia: Agenzia per il Mezzogiorno e piani triennali; incentivi e opere pubbliche.  
Conti: Spesa ingente; quantificazione completa n.d.  
Effetti: Letteratura divisa sull'intera esperienza: Felice e Lepore attribuiscono alla Cassa la convergenza del 1951-1973, ma non alla fase successiva; altre ricostruzioni giudicano l'intervento incapace di chiudere il divario. Concordanza ampia sul fatto che la fase finale (1986-1992) fu la meno efficace.  
Giudizio: **inefficace** · evidenza media

**D016 · 1987 · Uscita dal nucleare civile**  
*Referendum abrogativi 8-9 novembre 1987 e successive delibere CIPE* · governo in carica nel 1987 (Presidente del Consiglio: Giovanni Goria) · ambito: energia  
Cosa cambia: Fermo e poi chiusura delle centrali; stop ai nuovi impianti.  
Conti: Costi di smantellamento e gestione delle scorie pagati in bolletta per decenni (Sogin); importo complessivo n.d.  
Effetti: Fatti: aumento della quota di gas e di elettricità importata. Effetti su prezzi e sicurezza non stimati in modo controfattuale. I benefici percepiti in termini di sicurezza non sono quantificabili.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D017 · 1988 · Ordinamento della Presidenza del Consiglio e riforma della legge finanziaria**  
*L. 23 agosto 1988, n. 400 e L. 23 agosto 1988, n. 362* · governo in carica nel 1988 (Presidente del Consiglio: Ciriaco De Mita) · ambito: istituzioni  
Cosa cambia: Regole su decreti legge e regolamenti; obbligo di copertura delle leggi di spesa e contenuto più limitato della finanziaria.  
Conti: Obiettivo di disciplina della spesa; disavanzo ancora intorno al 10% del PIL fino al 1992 (dato Eurostat/Banca d'Italia).  
Effetti: Nessuna misura causale; uso dei decreti legge restato molto elevato (fatto).  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D018 · 1988 · Nuovo codice di procedura penale (rito accusatorio)**  
*D.P.R. 22 settembre 1988, n. 447* · governo in carica nel 1988 (Presidente del Consiglio: Ciriaco De Mita) · ambito: giustizia  
Cosa cambia: Separa indagini e giudizio, introduce riti alternativi.  
Conti: n.d.  
Effetti: Fatto: durata dei processi penali rimasta tra le più lunghe d'Europa (CEPEJ, Consiglio d'Europa). Riti alternativi usati meno del previsto. Nessuna stima controfattuale.  
Giudizio: **evidenza insufficiente** · evidenza bassa

## 1990-1999

Il decennio del risanamento e delle grandi riforme sotto la spinta della crisi del 1992 e dell'obiettivo euro: manovre straordinarie, fine della scala mobile, riforme pensionistiche Amato e Dini, privatizzazioni, autorità indipendenti, elezione diretta dei sindaci, flessibilità in entrata nel lavoro. È anche il decennio in cui iniziano le prime valutazioni d'impatto serie (legge 488, patti territoriali, riforma 3+2).

**D019 · 1990 · Legge antitrust e Autorità garante della concorrenza**  
*L. 10 ottobre 1990, n. 287* · governo in carica nel 1990 (Presidente del Consiglio: Giulio Andreotti) · ambito: concorrenza  
Cosa cambia: Divieto di intese e abusi di posizione dominante; controllo delle concentrazioni.  
Conti: Sanzioni come entrate; costo dell'Autorità contenuto.  
Effetti: Valutazioni OCSE (peer review) positive sull'enforcement; casi rilevanti in molti settori. Effetti su prezzi stimati solo per casi singoli.  
Giudizio: **efficace in parte** · evidenza media

**D020 · 1990 · Trasformazione delle banche pubbliche in società per azioni (legge Amato-Carli)**  
*L. 30 luglio 1990, n. 218* · governo in carica nel 1990 (Presidente del Consiglio: Giulio Andreotti) · ambito: banche  
Cosa cambia: Separa le fondazioni dalle banche; apre alle fusioni e, in seguito, alle privatizzazioni bancarie.  
Conti: Entrate da successive dismissioni; n.d.  
Effetti: Fatto: forte consolidamento del sistema negli anni '90. Letteratura (es. Sapienza, Journal of Finance 2002, su dati italiani): le fusioni hanno effetti diversi sui prestiti alle piccole imprese a seconda della dimensione delle banche coinvolte.  
Giudizio: **efficace in parte** · evidenza media

**D021 · 1991 · Riforma della cassa integrazione straordinaria e liste di mobilità**  
*L. 23 luglio 1991, n. 223* · governo in carica nel 1991 (Presidente del Consiglio: Giulio Andreotti) · ambito: lavoro  
Cosa cambia: Regole per i licenziamenti collettivi; indennità di mobilità per i lavoratori licenziati.  
Conti: Spesa per indennità; n.d.  
Effetti: Studi sulle liste di mobilità (es. Paggiaro, Rettore e Trivellato, Labour 2009): una durata più lunga del sussidio ritarda il reimpiego, soprattutto per i lavoratori più anziani.  
Giudizio: **efficace in parte** · evidenza media

**D022 · 1992 · Manovra straordinaria del 1992**  
*D.L. 11 luglio 1992, n. 333 (conv. L. 359/1992) e manovra per il 1993* · governo in carica nel 1992 (Presidente del Consiglio: Giuliano Amato) · ambito: conti pubblici  
Cosa cambia: Prelievo del 6 per mille sui depositi, imposta straordinaria sugli immobili, tagli di spesa, trasformazione di IRI, ENI, ENEL e INA in società per azioni.  
Conti: Correzione molto ampia (stima corrente: circa 90 mila miliardi di lire per il 1993).  
Effetti: Fatti: avanzo primario raggiunto e mantenuto per molti anni; crisi della lira e uscita dallo SME nel settembre 1992 non evitate. Il prelievo sui conti resta un precedente che pesa sulla fiducia (opinione diffusa).  
Giudizio: **efficace in parte** · evidenza media

**D023 · 1992 · Riforma Amato delle pensioni**  
*D.Lgs. 30 dicembre 1992, n. 503* · governo in carica nel 1992 (Presidente del Consiglio: Giuliano Amato) · ambito: pensioni  
Cosa cambia: Età di vecchiaia portata gradualmente a 65/60 anni, retribuzione di riferimento estesa, indicizzazione ai soli prezzi.  
Conti: Riduzione della spesa pensionistica futura (RGS: prima di una serie di riforme che ne hanno contenuto la crescita).  
Effetti: Effetto sui conti documentato dalla RGS nelle proiezioni; effetti su offerta di lavoro degli anziani non stimati separatamente.  
Giudizio: **efficace** · evidenza media

**D024 · 1992 · Aziendalizzazione del Servizio sanitario**  
*D.Lgs. 30 dicembre 1992, n. 502* · governo in carica nel 1992 (Presidente del Consiglio: Giuliano Amato) · ambito: sanità  
Cosa cambia: USL trasformate in aziende con direttore generale; finanziamento a quota capitaria e tariffe per prestazione; più ruolo alle Regioni.  
Conti: Obiettivo di controllo della spesa; disavanzi regionali proseguiti negli anni 2000.  
Effetti: Nessuna valutazione complessiva controfattuale; il Ministero della Salute ha segnalato a posteriori i limiti del modello nelle Regioni con disavanzi.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D025 · 1992 · Imposta comunale sugli immobili (ICI)**  
*D.Lgs. 30 dicembre 1992, n. 504* · governo in carica nel 1992 (Presidente del Consiglio: Giuliano Amato) · ambito: fisco  
Cosa cambia: Dà ai Comuni un'imposta propria sugli immobili con aliquote decise localmente.  
Conti: Gettito stabile per i Comuni; n.d.  
Effetti: Opinione di OCSE e Commissione UE: le imposte sugli immobili sono tra le meno dannose per la crescita e rafforzano la responsabilità degli amministratori locali.  
Giudizio: **efficace in parte** · evidenza media

**D026 · 1992 · Abolizione definitiva della scala mobile**  
*Protocollo tra Governo e parti sociali del 31 luglio 1992* · governo in carica nel 1992 (Presidente del Consiglio: Giuliano Amato) · ambito: lavoro  
Cosa cambia: Fine dell'indicizzazione automatica dei salari.  
Conti: Effetto indiretto via inflazione e spesa per interessi; n.d.  
Effetti: Fatto: dopo la svalutazione del 1992 l'inflazione non è ripartita come negli anni '70 (Banca d'Italia). Nessuna stima causale separata dall'accordo del 1993.  
Giudizio: **efficace** · evidenza media

**D027 · 1992 · Fine dell'intervento straordinario e incentivi agli investimenti con graduatorie (legge 488)**  
*D.L. 22 ottobre 1992, n. 415 (conv. L. 19 dicembre 1992, n. 488)* · governo in carica nel 1992 (Presidente del Consiglio: Giuliano Amato) · ambito: Mezzogiorno  
Cosa cambia: Contributi alle imprese delle aree deboli assegnati tramite bandi con punteggio.  
Conti: Diversi miliardi di euro di contributi negli anni '90 e 2000; n.d. complessivo.  
Effetti: Due valutazioni controfattuali divergono: Bronzini e de Blasio (2006) trovano investimenti anticipati e poi rallentati (sostituzione nel tempo); Cerqua e Pellegrini (2014, regression discontinuity) trovano effetti positivi su occupazione, investimenti e fatturato, ma non sulla produttività.  
Giudizio: **efficace in parte** · evidenza alta

**D028 · 1992 · Programma di privatizzazioni (banche, IRI, ENI, ENEL, Telecom, autostrade)**  
*Delibera CIPE 30 dicembre 1992 e D.L. 332/1994 (conv. L. 474/1994)* · governo in carica nel 1992 (Presidente del Consiglio: Giuliano Amato) · ambito: privatizzazioni  
Cosa cambia: Vendita di partecipazioni pubbliche in molte imprese e banche.  
Conti: Corte dei conti: circa 119 miliardi di euro di incassi tra il 1992 e il 2007 (93 operazioni), usati in gran parte per ridurre il debito.  
Effetti: Corte dei conti (2010): obiettivi di incasso raggiunti; criticità su modalità, costi di consulenza e aumenti tariffari nei settori regolati.  
Giudizio: **efficace in parte** · evidenza media

**D029 · 1993 · Elezione diretta del sindaco**  
*L. 25 marzo 1993, n. 81* · governo in carica nel 1993 (Presidente del Consiglio: Giuliano Amato) · ambito: istituzioni  
Cosa cambia: Sindaco eletto dai cittadini con premio di maggioranza; se cade il sindaco si torna al voto.  
Conti: Nessun costo diretto.  
Effetti: Fatto: giunte comunali molto più stabili rispetto agli anni '80 (dati Ministero dell'Interno sulla durata delle consiliature). Valutazioni sistematiche degli effetti sulla qualità della spesa: n.d.  
Giudizio: **efficace** · evidenza media

**D030 · 1993 · Politica dei redditi e due livelli di contrattazione**  
*Protocollo Governo-parti sociali del 23 luglio 1993* · governo in carica nel 1993 (Presidente del Consiglio: Carlo Azeglio Ciampi) · ambito: lavoro  
Cosa cambia: Salari legati all'inflazione programmata; contratto nazionale più contratto aziendale.  
Conti: Contributo alla disinflazione e al calo dei tassi; n.d. in cifre.  
Effetti: Fatto: inflazione scesa sotto il 3% nella seconda metà degli anni '90. Opinioni divergenti: per molti economisti il modello ha favorito stabilità ma anche bassa crescita dei salari reali e scarso legame salari-produttività (contrattazione aziendale poco diffusa).  
Giudizio: **efficace in parte** · evidenza media

**D031 · 1993 · Legge elettorale maggioritaria con quota proporzionale (Mattarellum)**  
*Leggi 4 agosto 1993, n. 276 e n. 277* · governo in carica nel 1993 (Presidente del Consiglio: Carlo Azeglio Ciampi) · ambito: istituzioni  
Cosa cambia: Tre quarti dei seggi in collegi uninominali.  
Conti: Nessun costo diretto.  
Effetti: Fatto: alternanza tra coalizioni dal 1994 al 2006; durata media dei governi rimasta breve. Nessuna stima causale.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D032 · 1994 · Legge quadro sui lavori pubblici dopo le inchieste sulla corruzione (legge Merloni)**  
*L. 11 febbraio 1994, n. 109* · governo in carica nel 1994 (Presidente del Consiglio: Carlo Azeglio Ciampi) · ambito: anticorruzione  
Cosa cambia: Regole rigide su gare, progettazione e varianti; Autorità di vigilanza sui lavori pubblici.  
Conti: n.d.  
Effetti: Fatto: modificata più volte in pochi anni (Merloni bis e ter) e poi sostituita dai codici del 2006, 2016 e 2023. Nessuna misura dell'effetto sulla corruzione; segnalati tempi di gara lunghi.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D033 · 1994 · Secondo condono edilizio**  
*L. 23 dicembre 1994, n. 724 (art. 39)* · governo in carica nel 1994 (Presidente del Consiglio: Silvio Berlusconi) · ambito: territorio  
Cosa cambia: Riapre la sanatoria degli abusi edilizi.  
Conti: Entrate una tantum; n.d.  
Effetti: Come per il 1985: abusivismo persistente (ISTAT BES); molte domande ancora inevase decenni dopo nei Comuni (fatto riportato da Corte dei conti e stampa specializzata).  
Giudizio: **effetti negativi** · evidenza media

**D034 · 1995 · Passaggio al sistema contributivo (riforma Dini)**  
*L. 8 agosto 1995, n. 335* · governo in carica nel 1995 (Presidente del Consiglio: Lamberto Dini) · ambito: pensioni  
Cosa cambia: Pensione calcolata sui contributi versati, con coefficienti legati all'età; transizione lunga per chi aveva già 18 anni di contributi.  
Conti: Grande effetto sulla sostenibilità di lungo periodo secondo RGS e Commissione UE (Ageing Report).  
Effetti: Fatti: sostenibilità migliorata nelle proiezioni; transizione molto lenta (pieno contributivo solo per gli assunti dal 1996); pensioni future più basse per carriere discontinue (tema di adeguatezza segnalato da INPS e OCSE).  
Giudizio: **efficace in parte** · evidenza alta

**D035 · 1995 · Autorità indipendenti per i servizi di pubblica utilità (energia)**  
*L. 14 novembre 1995, n. 481* · governo in carica nel 1995 (Presidente del Consiglio: Lamberto Dini) · ambito: regolazione  
Cosa cambia: Tariffe e qualità del servizio decise da un'autorità indipendente.  
Conti: Nessun costo diretto per il bilancio (finanziata dagli operatori).  
Effetti: Valutazioni OCSE positive sull'indipendenza del regolatore; prezzi finali influenzati soprattutto da costi delle materie prime e oneri di sistema.  
Giudizio: **efficace in parte** · evidenza media

**D036 · 1996 · Manovra per l'ingresso nell'euro con contributo straordinario ('eurotassa')**  
*L. 23 dicembre 1996, n. 662* · governo in carica nel 1996 (Presidente del Consiglio: Romano Prodi) · ambito: conti pubblici  
Cosa cambia: Prelievo straordinario sui redditi, in parte restituito negli anni successivi, più tagli e anticipi di entrate.  
Conti: Disavanzo sceso sotto il 3% del PIL nel 1997 (Eurostat).  
Effetti: Fatto: requisiti di Maastricht raggiunti; parte della correzione era temporanea (opinione della Commissione UE e della Banca d'Italia dell'epoca).  
Giudizio: **efficace** · evidenza media

**D037 · 1996 · Patti territoriali e programmazione negoziata per lo sviluppo locale**  
*L. 23 dicembre 1996, n. 662 (art. 2, comma 203: programmazione negoziata)* · governo in carica nel 1996 (Presidente del Consiglio: Romano Prodi) · ambito: Mezzogiorno  
Cosa cambia: Accordi tra enti locali, imprese e sindacati di comuni vicini, finanziati dallo Stato.  
Conti: Diversi miliardi di euro in contributi tra fine anni '90 e anni 2000; n.d.  
Effetti: Accetturo e de Blasio (Banca d'Italia 2011; Regional Science and Urban Economics 2012): nessun effetto significativo su occupazione e numero di unità locali nei comuni coinvolti rispetto a comuni simili.  
Giudizio: **inefficace** · evidenza alta

**D038 · 1997 · Riforme Bassanini: semplificazione e decentramento amministrativo**  
*L. 15 marzo 1997, n. 59 e decreti attuativi* · governo in carica nel 1997 (Presidente del Consiglio: Romano Prodi) · ambito: pubblica amministrazione  
Cosa cambia: Autocertificazione, sportello unico, trasferimento di funzioni a Regioni ed enti locali.  
Conti: n.d.  
Effetti: Fatti: autocertificazione e sportello unico entrati nell'uso. Nessuna valutazione d'impatto complessiva sugli oneri per cittadini e imprese.  
Giudizio: **efficace in parte** · evidenza bassa

**D039 · 1997 · Pacchetto Treu: lavoro interinale e flessibilità in entrata**  
*L. 24 giugno 1997, n. 196* · governo in carica nel 1997 (Presidente del Consiglio: Romano Prodi) · ambito: lavoro  
Cosa cambia: Legalizza il lavoro tramite agenzia, rafforza tirocini e contratti a termine.  
Conti: n.d.  
Effetti: Studi: crescita del lavoro temporaneo e calo della disoccupazione nelle regioni più sviluppate (studio di matching regionale); Boeri e Garibaldi (2007) descrivono un 'effetto luna di miele': più occupazione nel breve, con rischio di minore produttività e di mercato duale.  
Giudizio: **efficace in parte** · evidenza media

**D040 · 1997 · Riforma Visco: IRAP e addizionali regionali**  
*D.Lgs. 15 dicembre 1997, n. 446* · governo in carica nel 1997 (Presidente del Consiglio: Romano Prodi) · ambito: fisco  
Cosa cambia: Sostituisce contributi sanitari, ILOR, ICIAP e altri tributi con l'IRAP; introduce la DIT (premio al capitale proprio).  
Conti: Invarianza di gettito dichiarata; n.d.  
Effetti: Fatti: semplificazione dei tributi soppressi; la DIT è stata abolita nel 2003 e ripresa nel 2011 come ACE. Critiche diffuse alla base IRAP che includeva il costo del lavoro (ridotta nel 2015). Nessuna stima controfattuale complessiva.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D041 · 1997 · Decreto Ronchi sui rifiuti**  
*D.Lgs. 5 febbraio 1997, n. 22* · governo in carica nel 1997 (Presidente del Consiglio: Romano Prodi) · ambito: ambiente  
Cosa cambia: Gerarchia dei rifiuti, obiettivi di raccolta differenziata, consorzi per il riciclo.  
Conti: n.d.  
Effetti: Fatto ISPRA: raccolta differenziata cresciuta fino a oltre il 65% a livello nazionale negli anni 2020, con forti divari tra territori; crisi dei rifiuti in Campania negli anni 2000. Contributo della norma rispetto a direttive UE e tariffe non separabile.  
Giudizio: **efficace in parte** · evidenza media

**D042 · 1998 · Ingresso nella moneta unica**  
*Decisione del Consiglio UE del 3 maggio 1998 (ammissione all'euro)* · governo in carica nel 1998 (Presidente del Consiglio: Romano Prodi) · ambito: conti pubblici  
Cosa cambia: Fine del rischio di cambio; politica monetaria della BCE.  
Conti: Forte calo della spesa per interessi nella seconda metà degli anni '90 (Banca d'Italia).  
Effetti: Fatti: tassi e inflazione bassi; crescita della produttività molto debole dopo il 1999. Opinioni divergenti: per alcuni il vincolo ha tolto la svalutazione come strumento senza riforme sostitutive; per altri il risparmio sugli interessi è stato usato poco per ridurre il debito.  
Giudizio: **efficace in parte** · evidenza media

**D043 · 1998 · Testo unico sull'immigrazione**  
*D.Lgs. 25 luglio 1998, n. 286* · governo in carica nel 1998 (Presidente del Consiglio: Romano Prodi) · ambito: immigrazione  
Cosa cambia: Quote di ingresso, permessi di soggiorno, centri di permanenza per il rimpatrio.  
Conti: n.d.  
Effetti: Fatto: il sistema delle quote è stato affiancato da ripetute regolarizzazioni (1998, 2002, 2009, 2012, 2020), segno che i canali ordinari non hanno assorbito la domanda (opinione diffusa). Nessuna valutazione d'impatto complessiva.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D044 · 1998 · Indicatore ISEE per l'accesso alle prestazioni**  
*D.Lgs. 31 marzo 1998, n. 109* · governo in carica nel 1998 (Presidente del Consiglio: Romano Prodi) · ambito: welfare  
Cosa cambia: Misura unica di reddito e patrimonio familiare.  
Conti: Strumento per mirare le prestazioni; n.d.  
Effetti: Fatto: forti problemi di autodichiarazione e patrimoni non dichiarati, che hanno portato alla revisione del 2013 (DPCM 159/2013) con più dati precompilati. Oggi alla base di Assegno unico e AdI.  
Giudizio: **efficace in parte** · evidenza media

**D045 · 1998 · Patto di stabilità interno per Regioni ed enti locali**  
*L. 23 dicembre 1998, n. 448 (art. 28)* · governo in carica nel 1998 (Presidente del Consiglio: Massimo D'Alema) · ambito: conti pubblici  
Cosa cambia: Vincoli ai saldi degli enti territoriali per rispettare gli impegni europei.  
Conti: Contributo al contenimento della spesa locale.  
Effetti: Corte dei conti e letteratura: le regole, cambiate quasi ogni anno, hanno compresso soprattutto gli investimenti locali; sostituito dal pareggio di bilancio degli enti dal 2016.  
Giudizio: **efficace in parte** · evidenza media

**D046 · 1999 · Liberalizzazione del mercato elettrico (decreto Bersani)**  
*D.Lgs. 16 marzo 1999, n. 79* · governo in carica nel 1999 (Presidente del Consiglio: Massimo D'Alema) · ambito: energia  
Cosa cambia: Separazione delle reti, borsa elettrica, cessioni di capacità da parte di ENEL.  
Conti: Entrate da cessioni; n.d.  
Effetti: ARERA e AGCM: più concorrenza nella generazione; prezzo all'ingrosso legato al gas e quindi elevato in confronto europeo. Nessuna stima controfattuale semplice.  
Giudizio: **efficace in parte** · evidenza media

**D047 · 1999 · Riforma 3+2 delle lauree (processo di Bologna)**  
*D.M. 3 novembre 1999, n. 509* · governo in carica nel 1999 (Presidente del Consiglio: Massimo D'Alema) · ambito: università  
Cosa cambia: Laurea triennale più magistrale; crediti formativi.  
Conti: n.d.  
Effetti: Cappellari e Lucifora (2009): la probabilità di iscriversi all'università cresce di circa il 15% (10% nella versione di lavoro), soprattutto per studenti bravi di famiglie meno istruite; lieve calo degli abbandoni.  
Giudizio: **efficace in parte** · evidenza alta

## 2000-2009

Riforma del Titolo V, euro in circolazione, nuove regole del lavoro, condoni fiscali ed edilizi, scudi fiscali, incentivi alle rinnovabili, piani di rientro in sanità, federalismo fiscale. Le regole cambiano spesso (pensioni 2004 e 2007, leggi elettorali); emergono le prime valutazioni controfattuali di alta qualità (click day, INVALSI, cassa integrazione).

**D048 · 2000 · Legge quadro sui servizi sociali**  
*L. 8 novembre 2000, n. 328* · governo in carica nel 2000 (Presidente del Consiglio: Giuliano Amato) · ambito: welfare  
Cosa cambia: Sistema integrato di servizi, livelli essenziali delle prestazioni sociali, piani di zona.  
Conti: Fondo nazionale politiche sociali; n.d.  
Effetti: Fatto: i livelli essenziali delle prestazioni sociali sono stati definiti solo dal 2021 in poi; forti divari territoriali nella spesa sociale dei Comuni (ISTAT). Lo scopo centrale non è stato attuato per vent'anni.  
Giudizio: **inefficace** · evidenza media

**D049 · 2000 · Politica di coesione UE nelle regioni Obiettivo 1 / meno sviluppate**  
*Quadro comunitario di sostegno Obiettivo 1, 2000-2006 (e cicli successivi)* · governo in carica nel 2000 (Presidente del Consiglio: Massimo D'Alema) · ambito: Mezzogiorno  
Cosa cambia: Fondi strutturali europei con cofinanziamento nazionale per infrastrutture, imprese, formazione.  
Conti: Cofinanziamento nazionale; n.d.  
Effetti: Due risultati: Giua (Journal of Regional Science 2017, discontinuità ai confini): effetto positivo sull'occupazione, concentrato nei settori finanziati; Crescenzi e Giua (2020): in Italia gli effetti non sopravvivono alla Grande recessione. Fatto: bassa capacità di spesa e ritardi ricorrenti (Corte dei conti).  
Giudizio: **efficace in parte** · evidenza alta

**D050 · 2001 · Riforma del Titolo V della Costituzione**  
*L. cost. 18 ottobre 2001, n. 3 (approvata dal Parlamento l'8 marzo 2001; confermata dal referendum del 7 ottobre 2001)* · governo in carica nel 2001 (Presidente del Consiglio: Giuliano Amato) · ambito: istituzioni  
Cosa cambia: Ampie competenze legislative concorrenti alle Regioni; principio di sussidiarietà; autonomia finanziaria sulla carta.  
Conti: Effetti indiretti sulla spesa regionale; n.d.  
Effetti: Fatto: forte aumento dei conflitti Stato-Regioni davanti alla Corte costituzionale nel decennio successivo (relazioni annuali della Corte). Autonomia finanziaria (art. 119) attuata solo in parte. Opinione diffusa tra i costituzionalisti: riparto delle materie poco chiaro.  
Giudizio: **effetti negativi** · evidenza media

**D051 · 2001 · Nuova disciplina del contratto a termine**  
*D.Lgs. 6 settembre 2001, n. 368* · governo in carica nel 2001 (Presidente del Consiglio: Silvio Berlusconi) · ambito: lavoro  
Cosa cambia: Contratti a termine consentiti per ragioni tecniche, produttive, organizzative o sostitutive (formula generale).  
Conti: n.d.  
Effetti: Fatto: quota di lavoro a termine in crescita negli anni 2000 (ISTAT); forte contenzioso sulle causali. Nessuna valutazione controfattuale specifica trovata.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D052 · 2001 · Detassazione degli utili reinvestiti (Tremonti-bis) e primo scudo fiscale**  
*L. 18 ottobre 2001, n. 383 e D.L. 25 settembre 2001, n. 350 (conv. L. 409/2001)* · governo in carica nel 2001 (Presidente del Consiglio: Silvio Berlusconi) · ambito: fisco  
Cosa cambia: Deduzione degli investimenti incrementali; rimpatrio di capitali esteri con imposta del 2,5%.  
Conti: Costo della detassazione e gettito una tantum dello scudo: n.d.  
Effetti: Nessuna valutazione controfattuale trovata per la Tremonti-bis. Per lo scudo, nessuna misura degli effetti sulla compliance successiva.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D053 · 2002 · Condono fiscale generale e concordato per gli anni pregressi**  
*L. 27 dicembre 2002, n. 289 (artt. 7-16)* · governo in carica nel 2002 (Presidente del Consiglio: Silvio Berlusconi) · ambito: fisco  
Cosa cambia: Chiusura delle liti e delle annualità pregresse con pagamento ridotto.  
Conti: Entrate una tantum significative ma inferiori alle stime iniziali in alcune parti (Corte dei conti); importo n.d.  
Effetti: Corte di giustizia UE (2008, C-132/06): il condono IVA viola il diritto UE. IRPET e UPB: condoni ripetuti peggiorano adempimento spontaneo e gettito nel lungo periodo per effetto delle aspettative.  
Giudizio: **effetti negativi** · evidenza media

**D054 · 2002 · Legge Bossi-Fini e regolarizzazione dei lavoratori stranieri**  
*L. 30 luglio 2002, n. 189* · governo in carica nel 2002 (Presidente del Consiglio: Silvio Berlusconi) · ambito: immigrazione  
Cosa cambia: Contratto di soggiorno legato al lavoro, espulsioni più rapide; regolarizzazione di colf, badanti e lavoratori dipendenti.  
Conti: Contributi e imposte dai regolarizzati; n.d.  
Effetti: Fatto: la regolarizzazione ha ricevuto circa 650 mila domande (Ministero dell'Interno), la più grande in Europa allora. Effetti del contratto di soggiorno su irregolarità e mercato del lavoro non stimati in modo controfattuale.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D055 · 2003 · Riforma Biagi del mercato del lavoro**  
*L. 14 febbraio 2003, n. 30 e D.Lgs. 10 settembre 2003, n. 276* · governo in carica nel 2003 (Presidente del Consiglio: Silvio Berlusconi) · ambito: lavoro  
Cosa cambia: Nuove tipologie contrattuali (lavoro a progetto, somministrazione, lavoro intermittente), apertura ai servizi privati per l'impiego.  
Conti: n.d.  
Effetti: Fatti ISTAT: occupazione in crescita fino al 2008, con aumento dei contratti atipici. Letteratura (Boeri e Garibaldi 2007): riforme solo 'al margine' producono più occupazione temporanea e un mercato duale. Contributo specifico della legge non isolato.  
Giudizio: **efficace in parte** · evidenza bassa

**D056 · 2003 · Terzo condono edilizio**  
*D.L. 30 settembre 2003, n. 269 (art. 32)* · governo in carica nel 2003 (Presidente del Consiglio: Silvio Berlusconi) · ambito: territorio  
Cosa cambia: Nuova sanatoria degli abusi edilizi.  
Conti: Entrate una tantum; n.d.  
Effetti: Corte costituzionale (sent. 196/2004) lo dichiara parzialmente illegittimo per lesione delle competenze regionali. Abusivismo persistente (ISTAT BES).  
Giudizio: **effetti negativi** · evidenza media

**D057 · 2003 · Incentivi in tariffa al fotovoltaico (Conto energia)**  
*D.Lgs. 29 dicembre 2003, n. 387 e decreti 'Conto energia' (2005-2012)* · governo in carica nel 2003 (Presidente del Consiglio: Silvio Berlusconi) · ambito: energia  
Cosa cambia: Tariffe incentivanti per vent'anni per l'elettricità solare.  
Conti: Oneri in bolletta per gli incentivi al fotovoltaico nell'ordine di 6 miliardi l'anno negli anni 2010 (stima GSE/ARERA).  
Effetti: Fatti: forte crescita della capacità solare; incentivi molto generosi nel 2010-2011 rispetto al calo dei costi dei pannelli, poi tagliati. Opinione prevalente: obiettivo raggiunto a costo elevato per unità di CO2 evitata.  
Giudizio: **efficace in parte** · evidenza media

**D058 · 2004 · Riforma Maroni (scalone per le pensioni di anzianità) e Opzione donna sperimentale**  
*L. 23 agosto 2004, n. 243* · governo in carica nel 2004 (Presidente del Consiglio: Silvio Berlusconi) · ambito: pensioni  
Cosa cambia: Innalzamento brusco dal 2008 dei requisiti per la pensione di anzianità.  
Conti: Risparmi attesi; in gran parte non realizzati perché la norma è stata modificata nel 2007.  
Effetti: Fatto: lo 'scalone' non è mai entrato in vigore nella forma prevista. Esempio di regole cambiate prima dell'applicazione.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D059 · 2004 · Piani di rientro dai disavanzi sanitari regionali**  
*L. 30 dicembre 2004, n. 311 (art. 1, comma 180) e Patti per la salute successivi* · governo in carica nel 2004 (Presidente del Consiglio: Silvio Berlusconi) · ambito: sanità  
Cosa cambia: Le Regioni in disavanzo firmano un piano con lo Stato: aumento automatico delle addizionali, tagli, commissariamento in caso di inadempienza.  
Conti: Disavanzi sanitari regionali fortemente ridotti dopo il 2007 (Ministero della Salute, Corte dei conti).  
Effetti: Fonti divergenti sugli effetti di salute: Arcà, Principe e Van Doorslaer (Health Economics 2020): spesa ridotta di circa il 3,8% annuo e mortalità evitabile aumentata di circa il 3%; Bordignon, Coretti e Turati (Osservatorio CPI 2019): obiettivo finanziario raggiunto senza effetti negativi sulla salute. Ministero della Salute: LEA ancora sotto standard in diverse Regioni in piano.  
Giudizio: **efficace in parte** · evidenza alta

**D060 · 2005 · Legge elettorale proporzionale con premio di maggioranza e liste bloccate**  
*L. 21 dicembre 2005, n. 270* · governo in carica nel 2005 (Presidente del Consiglio: Silvio Berlusconi) · ambito: istituzioni  
Cosa cambia: Premio senza soglia minima e liste senza preferenze.  
Conti: Nessun costo diretto.  
Effetti: Corte costituzionale (sent. 1/2014): premio di maggioranza senza soglia e liste bloccate lunghe incostituzionali. Fatto: maggioranze diverse tra Camera e Senato nel 2006 e nel 2013.  
Giudizio: **effetti negativi** · evidenza alta

**D061 · 2005 · Conferimento del TFR alla previdenza complementare con silenzio-assenso**  
*D.Lgs. 5 dicembre 2005, n. 252 (anticipato al 2007 dalla L. 296/2006)* · governo in carica nel 2005 (Presidente del Consiglio: Silvio Berlusconi) · ambito: pensioni  
Cosa cambia: Chi non sceglie entro sei mesi vede il TFR versato al fondo pensione.  
Conti: Minori risorse per le imprese e flusso al Fondo Tesoreria INPS per le grandi imprese.  
Effetti: COVIP: adesioni cresciute ma ancora lontane dalla metà degli occupati; poche adesioni tacite rispetto alle attese. Esempio di spinta comportamentale debole.  
Giudizio: **efficace in parte** · evidenza media

**D062 · 2006 · Liberalizzazioni Bersani (farmaci da banco, tariffe professionali, costi bancari, ricariche)**  
*D.L. 4 luglio 2006, n. 223 (conv. L. 248/2006) e D.L. 31 gennaio 2007, n. 7* · governo in carica nel 2006 (Presidente del Consiglio: Romano Prodi) · ambito: concorrenza  
Cosa cambia: Vendita di farmaci senza ricetta fuori dalle farmacie, abolizione dei minimi tariffari, portabilità dei mutui.  
Conti: Nessun costo diretto.  
Effetti: Fatti AGCM: aumento dei punti vendita di farmaci da banco; effetti sui prezzi stimati solo per singoli settori. Valutazione complessiva n.d.  
Giudizio: **efficace in parte** · evidenza bassa

**D063 · 2006 · Detrazione del 55% per la riqualificazione energetica degli edifici (ecobonus)**  
*L. 27 dicembre 2006, n. 296 (commi 344-349)* · governo in carica nel 2006 (Presidente del Consiglio: Romano Prodi) · ambito: ambiente  
Cosa cambia: Detrazione in dieci anni per isolamento, caldaie efficienti, solare termico.  
Conti: Minori entrate per lo Stato su un arco decennale; n.d. in cifre consolidate.  
Effetti: ENEA: risparmi energetici misurati per intervento e costo per kWh risparmiato molto inferiore a quello del Superbonus. Beneficio concentrato su chi ha capienza fiscale (opinione UPB sui bonus edilizi pre-2020: regressivi).  
Giudizio: **efficace in parte** · evidenza media

**D064 · 2007 · Superamento dello scalone con le 'quote' (somma età più contributi)**  
*L. 24 dicembre 2007, n. 247* · governo in carica nel 2007 (Presidente del Consiglio: Romano Prodi) · ambito: pensioni  
Cosa cambia: Requisiti per l'anzianità alzati in modo graduale invece che a gradino.  
Conti: Maggiore spesa rispetto alla legge 243/2004, coperta con aumenti contributivi; importo n.d.  
Effetti: Fatto: gradualità ottenuta; nessuna valutazione degli effetti su occupazione degli anziani. Mostra il costo politico e finanziario dei cambi di regola ravvicinati.  
Giudizio: **efficace in parte** · evidenza bassa

**D065 · 2007 · Decreto flussi con domande in ordine di arrivo**  
*D.P.C.M. 30 ottobre 2007 sui flussi di ingresso ('click day')* · governo in carica nel 2007 (Presidente del Consiglio: Romano Prodi) · ambito: immigrazione  
Cosa cambia: Permessi di lavoro assegnati in base all'ora di invio online: di fatto una lotteria tra stranieri già presenti.  
Conti: Contributi e imposte dai regolarizzati; n.d.  
Effetti: Pinotti (American Economic Review 2017): ottenere lo status legale riduce di 0,6 punti percentuali il tasso di reati degli immigrati (da circa 1,1%), soprattutto i reati economici.  
Giudizio: **efficace** · evidenza alta

**D066 · 2007 · Prove INVALSI standardizzate per tutti gli studenti**  
*D.L. 7 settembre 2007, n. 147 (conv. L. 176/2007) e prove nazionali dal 2008* · governo in carica nel 2007 (Presidente del Consiglio: Romano Prodi) · ambito: scuola  
Cosa cambia: Test nazionali in italiano e matematica in più classi, con osservatori esterni in un campione.  
Conti: Costo contenuto; n.d.  
Effetti: Bertoni, Brunello e Rocco (J. Public Economics 2013, esperimento casuale): dove c'è un osservatore esterno i risultati sono più bassi del 5,5-8,5%, per minori copiature: la misura funziona solo se i controlli sono credibili. Fatto: base dati usata per individuare i divari territoriali.  
Giudizio: **efficace** · evidenza alta

**D067 · 2008 · Abolizione dell'ICI sull'abitazione principale**  
*D.L. 27 maggio 2008, n. 93* · governo in carica nel 2008 (Presidente del Consiglio: Silvio Berlusconi) · ambito: fisco  
Cosa cambia: I Comuni perdono il gettito sulla prima casa, sostituito da trasferimenti statali.  
Conti: Minore gettito compensato con trasferimenti; importo n.d.  
Effetti: Opinione di OCSE e Commissione UE: spostare il prelievo dagli immobili al lavoro è più favorevole alla crescita; la misura riduce l'autonomia fiscale dei Comuni (fatto). Nessuna stima di effetti su consumi.  
Giudizio: **effetti negativi** · evidenza bassa

**D068 · 2008 · Manovra triennale con tagli lineari ai ministeri e riduzione del personale scolastico**  
*D.L. 25 giugno 2008, n. 112 (conv. L. 133/2008)* · governo in carica nel 2008 (Presidente del Consiglio: Silvio Berlusconi) · ambito: conti pubblici  
Cosa cambia: Tagli percentuali uguali alle dotazioni; riduzione degli organici della scuola; blocco del turn-over.  
Conti: Correzione pluriennale ampia; n.d. in cifre consolidate.  
Effetti: Fatti: spesa contenuta nel breve; Corte dei conti e successive spending review segnalano che i tagli lineari non distinguono tra spesa utile e inutile e spesso vengono recuperati negli anni successivi.  
Giudizio: **efficace in parte** · evidenza media

**D069 · 2009 · Estensione della cassa integrazione a imprese e lavoratori non coperti durante la crisi**  
*Accordo Stato-Regioni 12 febbraio 2009 e D.L. 185/2008 (cassa integrazione in deroga)* · governo in carica nel 2009 (Presidente del Consiglio: Silvio Berlusconi) · ambito: lavoro  
Cosa cambia: Integrazione salariale anche per piccole imprese e settori esclusi.  
Conti: Spesa elevata nel 2009-2013; n.d.  
Effetti: Giupponi e Landais (Review of Economic Studies 2023, dati italiani): la cassa integrazione salva posti di lavoro nel breve periodo, ma può rallentare lo spostamento di lavoratori verso imprese più produttive.  
Giudizio: **efficace in parte** · evidenza alta

**D070 · 2009 · Delega sul federalismo fiscale**  
*L. 5 maggio 2009, n. 42* · governo in carica nel 2009 (Presidente del Consiglio: Silvio Berlusconi) · ambito: istituzioni  
Cosa cambia: Costi e fabbisogni standard, tributi propri, perequazione.  
Conti: Obiettivo di efficienza della spesa territoriale.  
Effetti: Fatti: fabbisogni standard dei Comuni introdotti in parte; LEP e perequazione per le Regioni non completati dopo oltre quindici anni (UPB, Corte dei conti).  
Giudizio: **inefficace** · evidenza media

**D071 · 2009 · Terzo scudo fiscale**  
*D.L. 1 luglio 2009, n. 78 (art. 13-bis, conv. L. 102/2009)* · governo in carica nel 2009 (Presidente del Consiglio: Silvio Berlusconi) · ambito: fisco  
Cosa cambia: Rimpatrio o regolarizzazione di capitali all'estero con imposta del 5% e anonimato.  
Conti: Gettito una tantum: circa 4,75-5,6 miliardi secondo fonti diverse.  
Effetti: Divergenza tra fonti: il MEF indicava circa 95 miliardi rimpatriati; la Banca d'Italia stimava circa 35 miliardi rientrati effettivamente e il resto solo regolarizzato. Effetti sulla compliance non misurati.  
Giudizio: **efficace in parte** · evidenza media

**D072 · 2009 · Ciclo della performance e premi selettivi nella PA (riforma Brunetta)**  
*D.Lgs. 27 ottobre 2009, n. 150* · governo in carica nel 2009 (Presidente del Consiglio: Silvio Berlusconi) · ambito: pubblica amministrazione  
Cosa cambia: Valutazione individuale e organizzativa, fasce di merito, organismi indipendenti di valutazione.  
Conti: n.d.  
Effetti: Fatto: le fasce di merito non sono mai state applicate pienamente; Corte dei conti e studi successivi: premi distribuiti in modo quasi uniforme. Nessuna stima dell'effetto sulla produttività.  
Giudizio: **inefficace** · evidenza media

## 2010-2019

Crisi del debito sovrano e lunga stagnazione: riforma Fornero, pareggio in Costituzione, spending review, anticorruzione; poi bonus 80 euro, Jobs Act, Industria 4.0, salvataggi bancari, rottamazioni, decreto dignità, Reddito di cittadinanza e Quota 100. È il decennio con più valutazioni d'impatto pubblicate.

**D073 · 2010 · Adeguamento automatico dei requisiti pensionistici alla speranza di vita**  
*D.L. 31 maggio 2010, n. 78 (art. 12, conv. L. 122/2010)* · governo in carica nel 2010 (Presidente del Consiglio: Silvio Berlusconi) · ambito: pensioni  
Cosa cambia: Età di pensione aggiornata periodicamente in base ai dati ISTAT.  
Conti: Contributo rilevante alla sostenibilità nelle proiezioni RGS e Commissione UE.  
Effetti: Fatto: meccanismo applicato, ma più volte sospeso o congelato per alcune categorie (es. pensioni anticipate fino al 2026). Effetto pieno dipende dalla stabilità della regola.  
Giudizio: **efficace** · evidenza media

**D074 · 2010 · Riforma Gelmini dell'università**  
*L. 30 dicembre 2010, n. 240* · governo in carica nel 2010 (Presidente del Consiglio: Silvio Berlusconi) · ambito: università  
Cosa cambia: Nuova governance degli atenei, abilitazione scientifica nazionale, ricercatori a tempo determinato, valutazione ANVUR.  
Conti: Contestuale riduzione del fondo di finanziamento ordinario (fatto).  
Effetti: Fatto: quota del finanziamento legata alla valutazione della ricerca (VQR) in crescita. Effetti su qualità della ricerca: evidenza mista e dibattuta, nessuna stima controfattuale condivisa.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D075 · 2011 · Riforma Fornero delle pensioni**  
*D.L. 6 dicembre 2011, n. 201 (art. 24, conv. L. 214/2011)* · governo in carica nel 2011 (Presidente del Consiglio: Mario Monti) · ambito: pensioni  
Cosa cambia: Contributivo pro rata per tutti, età di vecchiaia 66-67 anni, fine delle pensioni di anzianità con quote, blocco dell'indicizzazione 2012-2013.  
Conti: RGS: la maggior parte della riduzione della spesa pensionistica futura dovuta alle riforme dal 2004 deriva da questa legge.  
Effetti: Fatti e stime: forte aumento dell'occupazione 55-64 anni. Boeri, Garibaldi e Moen: circa 36 mila dei 150 mila posti per giovani persi nel periodo sono attribuibili alla riforma; Carta, D'Amuri e von Wachter (Banca d'Italia 2020) studiano gli effetti sulle imprese. Costo sociale: lavoratori 'esodati', tutelati con otto salvaguardie successive.  
Giudizio: **efficace in parte** · evidenza alta

**D076 · 2011 · Introduzione dell'IMU anche sulla prima casa e revisione delle rendite**  
*D.L. 6 dicembre 2011, n. 201 (art. 13)* · governo in carica nel 2011 (Presidente del Consiglio: Mario Monti) · ambito: fisco  
Cosa cambia: Imposta municipale sugli immobili con rivalutazione del 60% dei valori catastali.  
Conti: Gettito aggiuntivo rilevante nel 2012; importo n.d. in questo catalogo.  
Effetti: Fatto: contributo decisivo alla correzione del 2012. Opinioni divergenti: OCSE e Commissione UE la considerano un'imposta poco distorsiva; critiche sul catasto non aggiornato, che rende il prelievo poco equo tra immobili.  
Giudizio: **efficace in parte** · evidenza media

**D077 · 2012 · Riforma Fornero del mercato del lavoro**  
*L. 28 giugno 2012, n. 92* · governo in carica nel 2012 (Presidente del Consiglio: Mario Monti) · ambito: lavoro  
Cosa cambia: Modifica dell'articolo 18 (reintegra limitata), ASpI al posto dell'indennità di disoccupazione, stretta su collaborazioni e partite IVA.  
Conti: n.d.  
Effetti: Effetti difficili da separare dalla recessione 2012-2013. Nessuna valutazione controfattuale solida trovata; molte parti superate dal Jobs Act nel 2015.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D078 · 2012 · Pareggio di bilancio in Costituzione e ratifica del Fiscal compact**  
*L. cost. 20 aprile 2012, n. 1; L. 24 dicembre 2012, n. 243; L. 23 luglio 2012, n. 114 (ratifica Fiscal compact)* · governo in carica nel 2012 (Presidente del Consiglio: Mario Monti) · ambito: conti pubblici  
Cosa cambia: Equilibrio strutturale, scostamenti solo con maggioranza assoluta per eventi eccezionali, nascita dell'Ufficio parlamentare di bilancio.  
Conti: Nessun costo diretto; vincolo procedurale.  
Effetti: Fatti: UPB operativo dal 2014 con validazione delle previsioni; scostamenti autorizzati quasi ogni anno dal 2014 e in misura molto ampia nel 2020-2022. Opinione UPB e Corte dei conti: regola utile per la trasparenza, debole come vincolo effettivo.  
Giudizio: **efficace in parte** · evidenza media

**D079 · 2012 · Prima spending review strutturata**  
*D.L. 6 luglio 2012, n. 95 (conv. L. 135/2012)* · governo in carica nel 2012 (Presidente del Consiglio: Mario Monti) · ambito: conti pubblici  
Cosa cambia: Tagli a beni e servizi, centralizzazione degli acquisti (Consip), riduzione dei posti letto ospedalieri.  
Conti: Risparmi programmati; quota realizzata n.d.  
Effetti: Fatto: la centralizzazione degli acquisti produce risparmi documentati per categorie merceologiche (studi su Consip). Il Commissario alla revisione della spesa (2013-2014) segnala che molti risparmi non sono stati realizzati per mancanza di attuazione.  
Giudizio: **efficace in parte** · evidenza media

**D080 · 2012 · Legge anticorruzione, incandidabilità (Severino) e Autorità nazionale anticorruzione**  
*L. 6 novembre 2012, n. 190; D.Lgs. 235/2012; D.L. 90/2014 (poteri ANAC)* · governo in carica nel 2012 (Presidente del Consiglio: Mario Monti) · ambito: anticorruzione  
Cosa cambia: Piani triennali anticorruzione in ogni amministrazione, responsabile anticorruzione, rotazione, decadenza degli amministratori condannati.  
Conti: Costi amministrativi; n.d.  
Effetti: Nessuno studio controfattuale trovato sugli effetti dei piani sulla corruzione negli appalti. Indice di percezione della corruzione migliorato dopo il 2012 (fatto, non causale). Opinione diffusa: adempimento formale prevalente.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D081 · 2013 · Obblighi di pubblicazione e accesso civico**  
*D.Lgs. 14 marzo 2013, n. 33 (e accesso civico generalizzato, D.Lgs. 97/2016)* · governo in carica nel 2013 (Presidente del Consiglio: Mario Monti) · ambito: trasparenza  
Cosa cambia: Sezione 'Amministrazione trasparente' obbligatoria; dal 2016 diritto di accesso a dati e documenti.  
Conti: Costi amministrativi; n.d.  
Effetti: Fatto: grande mole di dati pubblicati, qualità disomogenea (ANAC). Nessuna stima d'impatto su corruzione o efficienza.  
Giudizio: **efficace in parte** · evidenza bassa

**D082 · 2013 · Pagamento dei debiti commerciali arretrati della PA**  
*D.L. 8 aprile 2013, n. 35 (conv. L. 64/2013)* · governo in carica nel 2013 (Presidente del Consiglio: Mario Monti) · ambito: conti pubblici  
Cosa cambia: Risorse straordinarie per pagare i fornitori; piattaforma di certificazione dei crediti.  
Conti: Aumento del debito pubblico con effetto neutro sul debito economico complessivo; diverse decine di miliardi nel 2013-2014 (MEF), importo preciso n.d. qui.  
Effetti: Banca d'Italia: tempi di pagamento ridotti negli anni successivi, anche grazie alla fatturazione elettronica; ritardi ancora presenti (procedura di infrazione UE, condanna 2020).  
Giudizio: **efficace in parte** · evidenza media

**D083 · 2014 · Bonus di 80 euro mensili per i lavoratori dipendenti a reddito medio-basso**  
*D.L. 24 aprile 2014, n. 66 (conv. L. 89/2014)* · governo in carica nel 2014 (Presidente del Consiglio: Matteo Renzi) · ambito: fisco  
Cosa cambia: Credito d'imposta in busta paga tra circa 8 e 26 mila euro di reddito.  
Conti: Circa 5,9 miliardi nel 2014 e circa 9-10 miliardi annui a regime (fonti MEF; ampliato a 100 euro nel 2020).  
Effetti: Neri, Rondinelli e Scoccianti (Banca d'Italia 2017): le famiglie beneficiarie hanno speso in consumi una quota rilevante del bonus, fino all'80% per i redditi più bassi. Altri economisti più cauti sull'effetto macro. Critiche sulla complessità (restituzioni per chi supera le soglie).  
Giudizio: **efficace in parte** · evidenza alta

**D084 · 2014 · Riforma delle Province e città metropolitane (legge Delrio)**  
*L. 7 aprile 2014, n. 56* · governo in carica nel 2014 (Presidente del Consiglio: Matteo Renzi) · ambito: istituzioni  
Cosa cambia: Province come enti di secondo livello, in attesa dell'abolizione costituzionale.  
Conti: Tagli ai bilanci provinciali; risparmi netti n.d.  
Effetti: Fatto: la riforma costituzionale è stata respinta dal referendum del 2016; le Province sono rimaste con funzioni su strade e scuole ma con risorse ridotte (Corte dei conti segnala manutenzione carente).  
Giudizio: **inefficace** · evidenza media

**D085 · 2014 · Jobs Act: contratto a tutele crescenti e decontribuzione per le assunzioni stabili**  
*L. 10 dicembre 2014, n. 183; D.Lgs. 4 marzo 2015, n. 23; L. 23 dicembre 2014, n. 190 (esonero contributivo)* · governo in carica nel 2014 (Presidente del Consiglio: Matteo Renzi) · ambito: lavoro  
Cosa cambia: Indennizzo crescente con l'anzianità al posto della reintegra per i nuovi assunti; esonero contributivo triennale nel 2015.  
Conti: Esonero costoso (diversi miliardi l'anno nel 2015-2018); importo consolidato n.d.  
Effetti: Sestito e Viviano (2016, Veneto): circa il 40% dell'aumento delle assunzioni stabili nel 2015 dovuto all'esonero, circa il 5% al nuovo contratto. Boeri e Garibaldi (2018): effetto del contratto visibile sopra i 15 dipendenti. Calo delle assunzioni stabili alla fine dell'esonero. La Corte costituzionale (sent. 194/2018) ha modificato il calcolo dell'indennizzo.  
Giudizio: **efficace in parte** · evidenza alta

**D086 · 2014 · Garanzia Giovani per i giovani che non studiano e non lavorano**  
*Programma Garanzia Giovani (Raccomandazione UE 2013; avvio 2014)* · governo in carica nel 2014 (Presidente del Consiglio: Matteo Renzi) · ambito: lavoro  
Cosa cambia: Offerta di tirocinio, formazione o lavoro entro quattro mesi.  
Conti: Fondi UE e cofinanziamento nazionale; n.d.  
Effetti: Rapporti ANPAL: molti tirocini, quota di inserimento stabile modesta; NEET italiani rimasti tra i più alti UE fino al calo degli anni 2020 (Eurostat). Valutazioni controfattuali limitate.  
Giudizio: **efficace in parte** · evidenza bassa

**D087 · 2014 · Collaborazione volontaria (voluntary disclosure) sui capitali all'estero**  
*L. 15 dicembre 2014, n. 186* · governo in carica nel 2014 (Presidente del Consiglio: Matteo Renzi) · ambito: fisco  
Cosa cambia: Emersione con pagamento integrale delle imposte e sanzioni ridotte, senza anonimato; in parallelo scambio automatico di informazioni OCSE.  
Conti: Gettito di alcuni miliardi (Agenzia delle Entrate; importo da verificare).  
Effetti: Differenza rispetto agli scudi: imposte pagate per intero e nessun anonimato; inserita nello scambio automatico di informazioni. Effetti sulla compliance non misurati.  
Giudizio: **efficace in parte** · evidenza bassa

**D088 · 2015 · Riforma 'Buona scuola'**  
*L. 13 luglio 2015, n. 107* · governo in carica nel 2015 (Presidente del Consiglio: Matteo Renzi) · ambito: scuola  
Cosa cambia: Piano straordinario di assunzioni di docenti, alternanza scuola-lavoro obbligatoria, bonus per la formazione docenti.  
Conti: Spesa per personale aumentata (circa 3 miliardi l'anno a regime secondo la relazione tecnica; da verificare).  
Effetti: Nessuna valutazione d'impatto sugli apprendimenti (INVALSI). Alternanza ridotta nel 2019. Mobilità dei docenti molto contestata (fatto).  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D089 · 2015 · Riforma Madia della pubblica amministrazione**  
*L. 7 agosto 2015, n. 124 e decreti attuativi* · governo in carica nel 2015 (Presidente del Consiglio: Matteo Renzi) · ambito: pubblica amministrazione  
Cosa cambia: Silenzio-assenso tra amministrazioni, SCIA, società partecipate, dirigenza.  
Conti: n.d.  
Effetti: Corte costituzionale (sent. 251/2016): illegittimi alcuni decreti per mancata intesa con le Regioni; riforma della dirigenza decaduta. Effetti sulle partecipate: riduzione del numero (Corte dei conti), effetti su efficienza n.d.  
Giudizio: **efficace in parte** · evidenza bassa

**D090 · 2015 · Abolizione della TASI sull'abitazione principale**  
*L. 28 dicembre 2015, n. 208 (commi 14 e seguenti)* · governo in carica nel 2015 (Presidente del Consiglio: Matteo Renzi) · ambito: fisco  
Cosa cambia: Eliminato il tributo sulla prima casa, compensato da trasferimenti ai Comuni.  
Conti: Minore gettito compensato (circa 3,5 miliardi annui secondo la relazione tecnica; da verificare).  
Effetti: Come per il 2008: Commissione UE e OCSE contrari (opinione); minore autonomia fiscale dei Comuni (fatto). Nessuna stima d'impatto su consumi.  
Giudizio: **effetti negativi** · evidenza bassa

**D091 · 2016 · Garanzia statale sulla cartolarizzazione delle sofferenze (GACS) e misure sui tempi di recupero**  
*D.L. 14 febbraio 2016, n. 18 (capo II, conv. L. 49/2016)* · governo in carica nel 2016 (Presidente del Consiglio: Matteo Renzi) · ambito: banche  
Cosa cambia: Garanzia pubblica a pagamento sulle tranche senior delle cartolarizzazioni di crediti deteriorati.  
Conti: Garanzia contingente; premi incassati; nel 2024 la Banca d'Italia segnala performance inferiori alle attese di alcune operazioni (rischio di escussione).  
Effetti: Fatto: forte riduzione dei crediti deteriorati delle banche tra 2016 e 2021 (Banca d'Italia), con concorso di vigilanza, cessioni di mercato e ripresa. Contributo specifico della GACS non stimato in modo controfattuale.  
Giudizio: **efficace in parte** · evidenza media

**D092 · 2016 · Industria 4.0: incentivi fiscali agli investimenti in beni digitali**  
*L. 11 dicembre 2016, n. 232 (iperammortamento) e successivi crediti d'imposta Transizione 4.0* · governo in carica nel 2016 (Presidente del Consiglio: Matteo Renzi) · ambito: industria  
Cosa cambia: Maggiorazione degli ammortamenti, poi crediti d'imposta automatici per beni 4.0.  
Conti: Costo superiore alle stime in alcune annualità (Pagella Politica su dati MEF).  
Effetti: Valutazione MEF-MIMIT-Banca d'Italia (2024) sul credito d'imposta 4.0; studio Confindustria-MEF: +11,3% di addetti in tre anni nelle imprese beneficiarie dell'iperammortamento 2017 (confronto controfattuale). Possibili effetti di anticipo degli investimenti.  
Giudizio: **efficace in parte** · evidenza media

**D093 · 2016 · Rottamazioni delle cartelle esattoriali (quattro edizioni in sei anni) e 'pace fiscale'**  
*D.L. 22 ottobre 2016, n. 193; poi D.L. 148/2017, D.L. 119/2018, L. 197/2022* · governo in carica nel 2016 (Presidente del Consiglio: Matteo Renzi) · ambito: fisco  
Cosa cambia: Pagamento dei debiti iscritti a ruolo senza sanzioni e interessi, a rate.  
Conti: Incassi inferiori agli importi definiti per decadenze diffuse (UPB); importo complessivo n.d.  
Effetti: UPB (2025): le definizioni agevolate ripetute alimentano aspettative di nuovi condoni e riducono i versamenti spontanei; quota elevata di contribuenti decaduti dalle rate. IRPET: condoni ripetuti peggiorano compliance e gettito di lungo periodo.  
Giudizio: **effetti negativi** · evidenza media

**D094 · 2017 · Reddito di inclusione (REI), prima misura nazionale contro la povertà**  
*D.Lgs. 15 settembre 2017, n. 147* · governo in carica nel 2017 (Presidente del Consiglio: Paolo Gentiloni) · ambito: welfare  
Cosa cambia: Sussidio condizionato a un progetto di inclusione, con prova dei mezzi.  
Conti: Circa 2 miliardi l'anno (stanziamento; da verificare).  
Effetti: Durata troppo breve (sostituito nel 2019) per una valutazione d'impatto; il Comitato scientifico sul RdC confronta i tassi di partecipazione dei due strumenti.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D095 · 2017 · Ricapitalizzazione precauzionale di MPS e liquidazione ordinata delle banche venete**  
*D.L. 23 dicembre 2016, n. 237 (MPS) e D.L. 25 giugno 2017, n. 99 (banche venete)* · governo in carica nel 2017 (Presidente del Consiglio: Paolo Gentiloni) · ambito: banche  
Cosa cambia: Ingresso dello Stato nel capitale di MPS; cessione delle parti sane delle venete con garanzie e contributi pubblici.  
Conti: Esposizione pubblica di diversi miliardi; parte recuperata con la vendita delle quote MPS dal 2023; consuntivo n.d.  
Effetti: Fatto: nessuna corsa agli sportelli; depositanti tutelati. Costo netto finale per lo Stato non ancora determinato in modo univoco.  
Giudizio: **efficace in parte** · evidenza bassa

**D096 · 2017 · Cooperazione con la Libia per il controllo delle partenze**  
*Memorandum d'intesa Italia-Libia del 2 febbraio 2017* · governo in carica nel 2017 (Presidente del Consiglio: Paolo Gentiloni) · ambito: immigrazione  
Cosa cambia: Sostegno alla guardia costiera libica e ai centri in Libia.  
Conti: Costi di cooperazione; n.d.  
Effetti: Fatti (Ministero dell'Interno): sbarchi da circa 181 mila (2016) a 119 mila (2017) e 23 mila (2018). Opinioni critiche documentate di organismi ONU e Consiglio d'Europa sulle condizioni nei centri libici. Effetto causale separato da altri fattori non stimato.  
Giudizio: **efficace in parte** · evidenza media

**D097 · 2017 · Legge elettorale mista (Rosatellum)**  
*L. 3 novembre 2017, n. 165* · governo in carica nel 2017 (Presidente del Consiglio: Paolo Gentiloni) · ambito: istituzioni  
Cosa cambia: Circa un terzo dei seggi in collegi uninominali, il resto proporzionale con liste bloccate corte.  
Conti: Nessun costo diretto.  
Effetti: Fatto: nel 2018 nessuna maggioranza chiara; nel 2022 maggioranza netta. Nessuna stima causale.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D098 · 2018 · Decreto dignità: limiti ai contratti a termine**  
*D.L. 12 luglio 2018, n. 87 (conv. L. 96/2018)* · governo in carica nel 2018 (Presidente del Consiglio: Giuseppe Conte) · ambito: lavoro  
Cosa cambia: Durata massima a 24 mesi, causali dopo 12 mesi, contributo addizionale sui rinnovi, indennità di licenziamento aumentate.  
Conti: Effetti contributivi minori; n.d.  
Effetti: Fonti divergenti: aumento delle trasformazioni a tempo indeterminato tra fine 2018 e inizio 2019 attribuito al decreto (REF Ricerche) oppure a incentivi e scadenze contrattuali (ADAPT). IRPET: interessa una quota minoritaria dei contratti. Calo della somministrazione (dati INPS).  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D099 · 2018 · Decreto sicurezza e immigrazione**  
*D.L. 4 ottobre 2018, n. 113 (conv. L. 132/2018)* · governo in carica nel 2018 (Presidente del Consiglio: Giuseppe Conte) · ambito: immigrazione  
Cosa cambia: Abolizione della protezione umanitaria, accoglienza diffusa (SPRAR) limitata ai titolari di protezione.  
Conti: Risparmi sull'accoglienza; n.d.  
Effetti: Stime (non misure) di centri studi indicano un aumento degli stranieri in condizione irregolare dopo l'abolizione della protezione umanitaria; norma in parte modificata nel 2020 (D.L. 130/2020). Nessuna valutazione controfattuale.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D100 · 2018 · Estensione del regime forfettario al 15% per autonomi e piccole imprese**  
*L. 30 dicembre 2018, n. 145 (soglia a 65 mila euro; poi 85 mila con L. 197/2022)* · governo in carica nel 2018 (Presidente del Consiglio: Giuseppe Conte) · ambito: fisco  
Cosa cambia: Imposta sostitutiva unica fino a 65 mila euro di ricavi (85 mila dal 2023), senza IVA.  
Conti: Minori entrate; importo n.d. in questo catalogo.  
Effetti: Banca d'Italia (audizione sulla manovra 2023): regimi molto diversi tra tipi di lavoratori creano un problema di equità orizzontale. Rischio documentato in letteratura internazionale di concentrazione dei redditi sotto la soglia; per l'Italia evidenza pubblica limitata.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D101 · 2019 · Reddito di cittadinanza**  
*D.L. 28 gennaio 2019, n. 4 (conv. L. 26/2019), artt. 1-13* · governo in carica nel 2019 (Presidente del Consiglio: Giuseppe Conte) · ambito: welfare  
Cosa cambia: Sussidio condizionato con patto per il lavoro o per l'inclusione, gestito da INPS e centri per l'impiego.  
Conti: Circa 7-8 miliardi l'anno (dati INPS sulla spesa erogata).  
Effetti: ISTAT: riduzione dell'intensità e dell'incidenza della povertà assoluta. Comitato scientifico (Ministero del Lavoro, 2021): rapporto tra spesa e risultati 'non soddisfacente' su povertà e politiche attive; più partecipazione rispetto al REI. IRPET (2025, controfattuale regionale): effetti occupazionali positivi ma contenuti. Esclusione di molti stranieri per il requisito di residenza decennale (poi ridotto dalla Corte UE nel 2024).  
Giudizio: **efficace in parte** · evidenza media

**D102 · 2019 · Quota 100 (pensione con 62 anni di età e 38 di contributi, 2019-2021)**  
*D.L. 28 gennaio 2019, n. 4, art. 14* · governo in carica nel 2019 (Presidente del Consiglio: Giuseppe Conte) · ambito: pensioni  
Cosa cambia: Uscita anticipata sperimentale per tre anni.  
Conti: Spesa inferiore agli stanziamenti per minori adesioni del previsto, ma maggiore debito pensionistico implicito (UPB, INPS).  
Effetti: INPS e Osservatorio CPI: nessun chiaro effetto di sostituzione con giovani (circa 40 assunti ogni 100 usciti secondo alcune stime, senza nesso causale); adesioni concentrate tra uomini, redditi medio-alti e settore pubblico.  
Giudizio: **inefficace** · evidenza media

## 2020-2026

Pandemia, grandi trasferimenti europei (PNRR), Superbonus e il suo stop, Assegno unico, riforme IRPEF a tappe, sostituzione del Reddito di cittadinanza, nuove regole fiscali europee. Per gran parte delle decisioni recenti l'evidenza ex post è ancora insufficiente.

**D103 · 2020 · Riduzione del numero dei parlamentari da 945 a 600**  
*L. cost. 19 ottobre 2020, n. 1 (referendum 20-21 settembre 2020)* · governo in carica nel 2020 (Presidente del Consiglio: Giuseppe Conte) · ambito: istituzioni  
Cosa cambia: Taglio di circa un terzo dei seggi di Camera e Senato.  
Conti: Risparmio stimato modesto rispetto alla spesa pubblica (Osservatorio CPI: circa 57 milioni l'anno netti; da verificare).  
Effetti: Effetti sul funzionamento delle Camere e sulla rappresentanza non ancora valutati.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D104 · 2020 · Cassa integrazione Covid estesa e blocco dei licenziamenti**  
*D.L. 17 marzo 2020, n. 18 e decreti successivi* · governo in carica nel 2020 (Presidente del Consiglio: Giuseppe Conte) · ambito: lavoro  
Cosa cambia: Integrazione salariale per quasi tutti i lavoratori dipendenti; divieto di licenziamenti economici fino al 2021.  
Conti: Diverse decine di miliardi tra 2020 e 2021 (MEF/INPS); importo preciso n.d. qui.  
Effetti: Banca d'Italia e ISTAT: perdita di posti contenuta rispetto al calo del PIL; occupati a termine e autonomi più colpiti. Effetto del blocco dei licenziamenti separato da quello della cassa integrazione: stime limitate.  
Giudizio: **efficace in parte** · evidenza media

**D105 · 2020 · Superbonus 110% con cessione del credito e sconto in fattura**  
*D.L. 19 maggio 2020, n. 34, art. 119 (conv. L. 77/2020) e proroghe* · governo in carica nel 2020 (Presidente del Consiglio: Giuseppe Conte) · ambito: ambiente  
Cosa cambia: Detrazione superiore al costo dei lavori di efficienza energetica e antisismici, trasferibile a banche e imprese.  
Conti: Costo quasi doppio rispetto alle previsioni (UPB); oltre 100 miliardi di detrazioni maturate (ENEA, ripreso da Osservatorio CPI); forte revisione del deficit 2020-2023 dopo la riclassificazione Eurostat dei crediti.  
Effetti: Fonti divergenti: UPB stima un impatto sul PIL di circa 2 punti nel periodo ma con costo per lo Stato molto superiore al gettito indotto; studi di parte del settore stimano ritorni fiscali molto più alti. Costo per tonnellata di CO2 evitata elevato; frodi rilevate sui crediti. Meno regressivo dei bonus edilizi precedenti (UPB).  
Giudizio: **effetti negativi** · evidenza alta

**D106 · 2020 · Decontribuzione Sud: sgravio del 30% sui contributi per i dipendenti delle imprese del Mezzogiorno**  
*D.L. 14 agosto 2020, n. 104, art. 27 (conv. L. 126/2020) e proroghe* · governo in carica nel 2020 (Presidente del Consiglio: Giuseppe Conte) · ambito: Mezzogiorno  
Cosa cambia: Sgravio generalizzato su tutti i rapporti, non solo sulle nuove assunzioni.  
Conti: Diversi miliardi l'anno (relazioni tecniche); importo consolidato n.d.  
Effetti: Valutazioni controfattuali pubbliche limitate; lo sgravio su tutti i lavoratori esistenti genera effetti di 'peso morto' (opinione di diversi analisti). Autorizzato dalla Commissione UE come aiuto temporaneo, poi sostituito nel 2025.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D107 · 2021 · PNRR: circa 190 miliardi tra sovvenzioni e prestiti UE legati a riforme e investimenti**  
*Piano nazionale di ripresa e resilienza (Decisione del Consiglio UE 13 luglio 2021) e D.L. 31 maggio 2021, n. 77* · governo in carica nel 2021 (Presidente del Consiglio: Mario Draghi) · ambito: conti pubblici  
Cosa cambia: Pagamenti UE solo al raggiungimento di traguardi e obiettivi; struttura di governance centrale.  
Conti: Parte a debito (prestiti UE) e parte a fondo perduto; impatto sul PIL stimato ex ante dal Governo, da verificare ex post.  
Effetti: Corte dei conti (maggio 2026): traguardi formali in gran parte raggiunti; spesa effettiva in ritardo, con circa 24 miliardi slittati oltre il 2026 e rischi sulle opere complesse; criticità su istruzione, inclusione e salute. Valutazioni d'impatto ex post: n.d.  
Giudizio: **evidenza insufficiente** · evidenza media

**D108 · 2021 · Riforme Cartabia del processo penale e civile (obiettivi PNRR)**  
*L. 27 settembre 2021, n. 134 (penale) e L. 26 novembre 2021, n. 206 (civile)* · governo in carica nel 2021 (Presidente del Consiglio: Mario Draghi) · ambito: giustizia  
Cosa cambia: Improcedibilità per durata eccessiva in appello, giustizia riparativa, ufficio per il processo, semplificazione del rito civile.  
Conti: Assunzioni temporanee per l'ufficio del processo finanziate dal PNRR.  
Effetti: Monitoraggio del Ministero della Giustizia e della Commissione UE: riduzione della durata dei procedimenti e dell'arretrato, ma obiettivi PNRR sul civile a rischio in alcuni gradi. Contributo separato di riforma e personale aggiuntivo non stimato.  
Giudizio: **efficace in parte** · evidenza bassa

**D109 · 2021 · Assegno unico e universale per i figli**  
*D.Lgs. 29 dicembre 2021, n. 230* · governo in carica nel 2021 (Presidente del Consiglio: Mario Draghi) · ambito: famiglia  
Cosa cambia: Sostituisce assegni familiari, detrazioni per figli e bonus con un assegno unico legato all'ISEE, esteso ad autonomi e incapienti.  
Conti: Circa 18 miliardi l'anno secondo l'UPB (in gran parte da riordino di misure esistenti).  
Effetti: UPB (Focus 3/2022, microsimulazione): circa il 77% dei figli ci guadagna, in media circa 672 euro l'anno; vantaggi per autonomi e incapienti; alcune famiglie con patrimonio perdono. Effetto sulla natalità: n.d.  
Giudizio: **efficace in parte** · evidenza media

**D110 · 2021 · Riforma IRPEF da 5 a 4 aliquote e revisione delle detrazioni**  
*L. 30 dicembre 2021, n. 234 (art. 1, commi 2-8)* · governo in carica nel 2021 (Presidente del Consiglio: Mario Draghi) · ambito: fisco  
Cosa cambia: Aliquote 23-25-35-43%; detrazioni per lavoro ridisegnate per ridurre le aliquote marginali effettive.  
Conti: Circa 7 miliardi l'anno (legge di bilancio 2022).  
Effetti: UPB: benefici concentrati sui redditi medi; aliquote marginali effettive meno irregolari. Nessuna valutazione ex post sull'offerta di lavoro.  
Giudizio: **evidenza insufficiente** · evidenza media

**D111 · 2021 · Quote 102 e 103: uscite anticipate temporanee dopo Quota 100**  
*L. 30 dicembre 2021, n. 234 (Quota 102) e L. 29 dicembre 2022, n. 197 (Quota 103)* · governo in carica nel 2021 (Presidente del Consiglio: Mario Draghi) · ambito: pensioni  
Cosa cambia: Pensione anticipata con 64 anni e 38 di contributi (2022), poi 62 e 41 (2023-2025) con calcolo contributivo dal 2024.  
Conti: Spesa contenuta per poche adesioni (INPS).  
Effetti: Fatto: adesioni molto inferiori a Quota 100 per requisiti più stretti. Mostra la tendenza a rinnovare ogni anno deroghe temporanee alla regola generale. Effetti sul lavoro: n.d.  
Giudizio: **evidenza insufficiente** · evidenza media

**D112 · 2023 · Stop alla cessione dei crediti e allo sconto in fattura per i bonus edilizi**  
*D.L. 16 febbraio 2023, n. 11 (conv. L. 38/2023) e D.L. 29 marzo 2024, n. 39* · governo in carica nel 2023 (Presidente del Consiglio: Giorgia Meloni) · ambito: conti pubblici  
Cosa cambia: Blocca le nuove cessioni; poi spalma in dieci anni alcune detrazioni e rafforza i controlli.  
Conti: Contenimento della crescita del costo dei bonus edilizi (UPB, memoria sul D.L. 39/2024).  
Effetti: Fatto: brusco calo dei nuovi cantieri incentivati; crediti incagliati per alcune imprese. Effetto di contenimento del costo riconosciuto da UPB.  
Giudizio: **efficace** · evidenza media

**D113 · 2023 · Decreto Cutro: flussi programmati triennali e restrizioni alla protezione speciale**  
*D.L. 10 marzo 2023, n. 20 (conv. L. 50/2023)* · governo in carica nel 2023 (Presidente del Consiglio: Giorgia Meloni) · ambito: immigrazione  
Cosa cambia: Più ingressi regolari per lavoro su base triennale; protezione speciale limitata; procedure accelerate.  
Conti: n.d.  
Effetti: Fatti: quote di ingresso molto aumentate (decreto flussi 2023-2025); quota di domande trasformate in contratti effettivi bassa secondo le organizzazioni del settore (dato da verificare). Nessuna valutazione controfattuale.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D114 · 2023 · Assegno di inclusione e Supporto per la formazione e il lavoro al posto del Reddito di cittadinanza**  
*D.L. 4 maggio 2023, n. 48 (conv. L. 85/2023)* · governo in carica nel 2023 (Presidente del Consiglio: Giorgia Meloni) · ambito: welfare  
Cosa cambia: Sussidio limitato a famiglie con minori, disabili, anziani o persone in cura; percorso separato per gli 'occupabili'.  
Conti: Spesa inferiore al RdC (stanziamenti in legge di bilancio).  
Effetti: Banca d'Italia (QEF 820, microsimulazione statica): l'AdI riduce povertà assoluta e disuguaglianza, ma meno del RdC; la Commissione UE ha ripreso queste stime. Il Ministero del Lavoro contesta le stime. Effetti sull'occupazione degli 'occupabili': n.d.  
Giudizio: **efficace in parte** · evidenza media

**D115 · 2023 · Nuovo codice dei contratti pubblici**  
*D.Lgs. 31 marzo 2023, n. 36* · governo in carica nel 2023 (Presidente del Consiglio: Giorgia Meloni) · ambito: anticorruzione  
Cosa cambia: Affidamenti diretti sotto soglie più alte, digitalizzazione completa, principio del risultato.  
Conti: n.d.  
Effetti: ANAC segnala aumento degli affidamenti diretti e minore concorrenza in alcune fasce; effetti su tempi e costi delle opere ancora da misurare.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D116 · 2023 · IRPEF a tre aliquote (23-35-43%) e taglio contributivo per i redditi bassi**  
*D.Lgs. 30 dicembre 2023, n. 216 (attuazione delega L. 111/2023)* · governo in carica nel 2023 (Presidente del Consiglio: Giorgia Meloni) · ambito: fisco  
Cosa cambia: Primo scaglione accorpato fino a 28 mila euro; decontribuzione poi resa strutturale come taglio fiscale nel 2025.  
Conti: Circa 4 miliardi l'anno per le aliquote, oltre al taglio del cuneo (stime ufficiali; da verificare).  
Effetti: UPB: benefici concentrati sui redditi medio-bassi da lavoro dipendente; parte dei guadagni assorbita dal drenaggio fiscale (inflazione non indicizzata). Nessuna valutazione ex post sull'offerta di lavoro.  
Giudizio: **evidenza insufficiente** · evidenza media

**D117 · 2024 · Concordato preventivo biennale per autonomi e piccole imprese**  
*D.Lgs. 12 febbraio 2024, n. 13* · governo in carica nel 2024 (Presidente del Consiglio: Giorgia Meloni) · ambito: fisco  
Cosa cambia: Il contribuente accetta in anticipo una proposta di reddito per due anni; eventuali redditi superiori non tassati.  
Conti: Incassi della prima adesione inferiori alle attese governative (dati MEF 2024); effetto netto sul gettito dipende dai redditi effettivi futuri.  
Effetti: UPB: rischio di perdita di gettito per selezione avversa (aderisce soprattutto chi prevede redditi maggiori della proposta); misura accompagnata da un ravvedimento sulle annualità passate, assimilabile a un condono. Evidenza ex post: n.d.  
Giudizio: **evidenza insufficiente** · evidenza media

**D118 · 2024 · Legge quadro sull'autonomia differenziata delle Regioni**  
*L. 26 giugno 2024, n. 86* · governo in carica nel 2024 (Presidente del Consiglio: Giorgia Meloni) · ambito: istituzioni  
Cosa cambia: Procedura per attribuire alle Regioni ulteriori competenze, previa definizione dei LEP.  
Conti: Effetti sui conti dipendenti dalle intese; n.d.  
Effetti: Corte costituzionale (sent. 192/2024): illegittime diverse parti della legge (tra cui criteri sui LEP e sulle risorse). Nessuna intesa attuata alla data di questo catalogo (da verificare).  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D119 · 2024 · Abrogazione del reato di abuso d'ufficio e modifiche al traffico di influenze**  
*L. 9 agosto 2024, n. 114* · governo in carica nel 2024 (Presidente del Consiglio: Giorgia Meloni) · ambito: giustizia  
Cosa cambia: Elimina il reato di abuso d'ufficio, motivato con la 'paura della firma' degli amministratori.  
Conti: Nessun costo diretto.  
Effetti: Fatto: la gran parte dei procedimenti per abuso d'ufficio si chiudeva senza condanna (dati del Ministero della Giustizia citati nel dibattito). Opinione della Commissione UE (Rule of Law Report 2024): possibile indebolimento degli strumenti anticorruzione. Effetti misurati: n.d.  
Giudizio: **evidenza insufficiente** · evidenza bassa

**D120 · 2024 · Applicazione delle nuove regole europee: tetto alla crescita della spesa netta su sette anni**  
*Piano strutturale di bilancio di medio termine 2025-2029 (nuove regole fiscali UE, Reg. UE 2024/1263)* · governo in carica nel 2024 (Presidente del Consiglio: Giorgia Meloni) · ambito: conti pubblici  
Cosa cambia: Un solo indicatore operativo (spesa primaria netta) concordato con la Commissione, con riforme che allungano il percorso.  
Conti: Percorso di aggiustamento pluriennale; deficit sotto il 3% atteso dal Governo entro il 2026 (da verificare con i dati).  
Effetti: Troppo presto per una valutazione; UPB e Commissione UE monitorano il rispetto del tetto di spesa annuale.  
Giudizio: **evidenza insufficiente** · evidenza bassa

## Lezioni trasversali per GovernAI

### 1. Condoni e definizioni agevolate ripetute danno entrate una tantum ma peggiorano l'adempimento

Ogni condono porta entrate una tantum, ma l'attesa del prossimo riduce l'adempimento spontaneo e alimenta nuovi abusi. La Corte di giustizia UE ha bocciato il condono IVA del 2002; UPB e IRPET documentano l'effetto aspettative delle rottamazioni. La collaborazione volontaria del 2014, con imposte pagate per intero e senza anonimato, è il modello meno dannoso.

- Decisioni a sostegno: D013, D033, D053, D056, D052, D071, D093, D117, D087
- Che cosa ne ricava il programma: Nessun condono, rottamazione o scudo anonimo nel programma; solo regolarizzazioni a imposta piena con scambio di informazioni.

### 2. Le riforme delle pensioni funzionano se sono graduali e stabili; le deroghe temporanee costano e non creano lavoro per i giovani

Amato, Dini, adeguamento alla speranza di vita e Fornero hanno spostato la sostenibilità nelle proiezioni RGS. Lo scalone del 2004 cancellato nel 2007 e le quote 100, 102 e 103 mostrano il costo di cambiare spesso: Quota 100 non ha prodotto sostituzione con giovani. La Fornero, brusca, ha generato gli esodati e un effetto negativo misurato sulle assunzioni di giovani.

- Decisioni a sostegno: D023, D034, D073, D075, D058, D064, D102, D111
- Che cosa ne ricava il programma: Ogni modifica pensionistica deve essere permanente, graduale e con clausole di salvaguardia scritte prima.

### 3. Un incentivo automatico senza tetto di spesa sfugge di mano

Superbonus (costo quasi doppio del previsto), Conto energia (incentivi rimasti alti mentre i pannelli costavano meno) e crediti 4.0 (costi sopra le stime) hanno lo stesso difetto: spesa aperta, legata alla domanda. Lo stop alla cessione dei crediti ha fermato la crescita del costo.

- Decisioni a sostegno: D105, D057, D092, D112, D063
- Che cosa ne ricava il programma: Ogni agevolazione nel programma ha un tetto annuo, un monitoraggio mensile e una revisione automatica se supera la stima.

### 4. Tagli mirati e monitorati battono i tagli lineari, ma vanno guardati anche gli esiti

I tagli uguali per tutti (2008) contengono la spesa nel breve ma non distinguono tra spesa utile e inutile; la spending review del 2012 e la centralizzazione degli acquisti hanno dato risparmi documentati dove sono state attuate. I piani di rientro sanitari hanno risanato i conti, ma uno studio controfattuale trova più mortalità evitabile: tagliare senza misurare gli esiti è rischioso.

- Decisioni a sostegno: D068, D079, D059, D045, D084
- Che cosa ne ricava il programma: Coperture da tagli solo con voce di spesa identificata e indicatore di esito associato (come già fanno le 93 coperture verificate).

### 5. La stabilità delle regole è una politica in sé

Quattro leggi elettorali in 24 anni (due dichiarate in parte incostituzionali), quattro codici degli appalti, quattro rottamazioni in sei anni, regole sul lavoro a termine cambiate nel 2001, 2012, 2014, 2018: ogni cambiamento riduce la credibilità del successivo e rende impossibile valutare.

- Decisioni a sostegno: D031, D060, D097, D032, D115, D051, D077, D085, D098
- Che cosa ne ricava il programma: Clausola di stabilità: le misure del programma non si toccano per almeno un ciclo di valutazione salvo evidenza contraria.

### 6. L'attuazione conta più dell'annuncio

Livelli essenziali sociali previsti nel 2000 e definiti vent'anni dopo; federalismo fiscale e Titolo V attuati a metà; fasce di merito nella PA mai applicate; spesa PNRR in ritardo pur con traguardi formali raggiunti. Le leggi quadro senza decreti, risorse e responsabili restano sulla carta.

- Decisioni a sostegno: D048, D070, D050, D072, D107, D118, D004
- Che cosa ne ricava il programma: Per ogni misura: decreto attuativo, responsabile, scadenza e indicatore di attuazione pubblicati insieme alla misura.

### 7. Gli aiuti alle imprese del Sud danno risultati misti: assegnarli con graduatorie e valutarli

Patti territoriali senza effetti misurabili; legge 488 con due valutazioni divergenti (anticipo degli investimenti contro effetti positivi su occupazione); fondi UE con effetti positivi ma non duraturi dopo la crisi; sgravi generalizzati con forte rischio di peso morto. I meccanismi a graduatoria hanno almeno permesso valutazioni rigorose.

- Decisioni a sostegno: D015, D027, D037, D049, D106, D092
- Che cosa ne ricava il programma: Incentivi territoriali solo con bandi a punteggio, gruppo di confronto e valutazione indipendente prevista ex ante.

### 8. I vincoli esterni e le istituzioni indipendenti aiutano, ma non sostituiscono l'avanzo primario

SME, divorzio, fine della scala mobile e accordi del 1993 hanno contribuito a battere l'inflazione; l'euro ha abbattuto la spesa per interessi. Ma il debito è cresciuto negli anni '80 per i disavanzi primari, e il pareggio in Costituzione è stato derogato quasi ogni anno. L'UPB è l'eredità più utile del 2012.

- Decisioni a sostegno: D008, D009, D026, D030, D036, D042, D078, D120, D022
- Che cosa ne ricava il programma: Il programma rispetta un percorso di spesa netta e fa validare le stime da un soggetto terzo (UPB o equivalente).

### 9. Contro la povertà servono strumenti universali e selettivi, con un'attivazione che funzioni davvero

Il Reddito di cittadinanza ha ridotto la povertà ma con risultati deboli sul lavoro; l'Assegno di inclusione la riduce meno (Banca d'Italia). L'Assegno unico ha razionalizzato misure frammentate. Il bonus 80 euro ha sostenuto i consumi ma non raggiungeva gli incapienti. L'ISEE è stato decisivo solo dopo la revisione con dati precompilati.

- Decisioni a sostegno: D094, D101, D114, D109, D083, D044
- Che cosa ne ricava il programma: Sostegno contro la povertà su base ISEE precompilato, con politiche attive valutate e non solo condizionalità formali.

### 10. Nel lavoro, riformare solo i nuovi contratti crea un mercato duale; gli incentivi temporanei creano picchi

Treu, Biagi e decreto 368 hanno aumentato l'occupazione soprattutto temporanea; il Jobs Act ha spinto le assunzioni stabili soprattutto grazie alla decontribuzione, con calo alla sua fine. La cassa integrazione protegge i posti nel breve ma può rallentare la riallocazione.

- Decisioni a sostegno: D039, D055, D051, D085, D098, D086, D069, D104, D012
- Che cosa ne ricava il programma: Preferire sgravi permanenti e mirati a incentivi a scadenza; ammortizzatori con durata limitata e formazione collegata.

### 11. Lo status legale riduce i reati; canali di ingresso realistici evitano sanatorie a ripetizione

La prova più solida dell'intero catalogo in materia: con il click day 2007 lo status legale ha ridotto i reati degli immigrati regolarizzati. Ripetute sanatorie (1998-2020) mostrano che le quote ordinarie non bastavano. Le strette sui permessi e gli accordi con paesi di transito hanno effetti misurati sugli sbarchi, ma costi umani documentati e nessuna valutazione controfattuale.

- Decisioni a sostegno: D065, D054, D043, D113, D099, D096
- Che cosa ne ricava il programma: Canali di ingresso per lavoro realistici e regolarizzazione legata al lavoro, valutati con dati amministrativi.

### 12. Misurare bene è già una politica: dati, controlli credibili, valutatori indipendenti

Le prove INVALSI funzionano solo con osservatori esterni (esperimento casuale); l'ISEE è migliorato con i dati precompilati; l'UPB ha reso più credibili le previsioni; trasparenza e anticorruzione senza misura degli esiti producono soprattutto adempimenti formali.

- Decisioni a sostegno: D066, D044, D078, D081, D080, D119
- Che cosa ne ricava il programma: Ogni misura del programma nasce con dati, indicatore e piano di valutazione; i risultati si pubblicano anche se negativi.

### 13. Tassare meno il lavoro e più gli immobili è la raccomandazione costante, ma la politica ha fatto spesso il contrario

ICI 1992 e IMU 2011 hanno dato ai Comuni un'entrata stabile; l'abolizione sulla prima casa (2008 e 2015) l'ha ridotta, contro il parere di OCSE e Commissione UE. Le riforme IRPEF recenti agiscono sul lavoro, ma il drenaggio fiscale ne assorbe parte. Imposte sostitutive come il forfettario (e la cedolare secca sugli affitti) creano disparità tra redditi uguali.

- Decisioni a sostegno: D025, D067, D076, D090, D100, D110, D116
- Che cosa ne ricava il programma: Spostare il prelievo verso immobili (con catasto aggiornato) e consumi dannosi, riducendo quello sul lavoro; ridurre i regimi sostitutivi.

### 14. Le grandi scelte di sistema reggono quando hanno un finanziamento credibile

Il Servizio sanitario universale del 1978 è tra le scelte più durature, ma ha generato disavanzi ripianati a posteriori per quasi trent'anni; le privatizzazioni hanno portato incassi rilevanti ma con criticità di regolazione. Le leggi di sistema durano se nascono con risorse e governance chiare.

- Decisioni a sostegno: D006, D024, D059, D028, D035, D020
- Che cosa ne ricava il programma: Le riforme di sistema del programma indicano fonte di finanziamento strutturale e regolatore responsabile.

## Cosa non sappiamo

- **Gli effetti di lungo periodo di molte leggi di sistema** (SSN, Titolo V, autonomie locali, codice di procedura penale): non esistono controfattuali credibili; i giudizi sono ricostruzioni.
- **Le decisioni più recenti** (2023-2026: AdI, concordato preventivo, IRPEF a tre aliquote e al 33%, autonomia differenziata, abolizione dell'abuso d'ufficio, nuove regole UE, PNRR): l'evidenza è ex ante o assente.
- **L'effetto netto di Superbonus e PNRR sul PIL potenziale**: le stime divergono e dipendono dal modello; servono dati microeconomici che non sono ancora pubblici.
- **Corruzione ed evasione**: mancano misure dirette affidabili, quindi l'efficacia di L. 190/2012, ANAC, condoni e concordato si può giudicare solo indirettamente.
- **Natalità**: nessuna misura del catalogo (Assegno unico incluso) ha ancora un effetto misurato sulla fecondità.
- **Costi consolidati**: per molte decisioni (Jobs Act, decontribuzione Sud, salvataggi bancari, privatizzazioni nette) manca un consuntivo pubblico unico; le cifre indicate come "da verificare" vanno controllate su relazioni tecniche e rendiconti.
- **Limiti di questo lavoro**: selezione delle decisioni inevitabilmente soggettiva; alcune fonti sono sintesi secondarie di studi originali (indicate come tali); i link istituzionali generici vanno sostituiti col documento puntuale in una revisione successiva.
