# GovernAI · Brief di design

*Versione 1.0, 8 novembre 2026. Specifica indipendente dallo strumento: vale per chi disegna a mano, per ChatGPT e per Gemini. I numeri citati vengono da `docs/data.js` del 8/11/2026 alle 14:22.*

## 1. Che cosa stiamo progettando

GovernAI è un prototipo a scopo sociale di programma di governo **post-ideologico**: né destra né sinistra né centro. Un sistema scarica ogni giorno dati ufficiali, valuta 62 proposte secondo una **Carta di 10 valori**, simula un **governo ombra** con regole verificabili, controlla coperture (nessun deficit), conformità a Costituzione e diritto UE e integrità (catena di impronte crittografiche), e impara dagli esiti. **L'AI non decide: le persone decidono.**

L'app deve rendere tutto questo **bello, semplice e consultabile in 2 minuti da telefono**, senza perdere la profondità che serve a chi verifica.

Il prodotto non è il sito di un partito né un sito istituzionale. Non deve sembrare nessuno dei due (vedi §7 e §8).

## 2. Pubblici

| | Cittadino curioso | Persona attiva nel progetto | Esperto o giornalista |
|---|---|---|---|
| **Chi è** | Elettore di qualunque orientamento, arriva da un link condiviso o da un motore di ricerca | Volontario, revisore, membro del progetto con account GitHub | Economista, giurista, ricercatore, cronista politico, fact-checker |
| **Contesto** | Telefono, 2 minuti, in pausa o sui mezzi | Desktop e telefono, sessioni di 15-60 minuti, torna spesso | Desktop, sessioni lunghe, copia numeri e link |
| **Vuole** | Capire che cos'è, che cosa propone su un tema che gli sta a cuore, se si può fidare | Proporre idee e domande, controllare cosa è cambiato, verificare decisioni e mandati | Fonti primarie, numeri esatti, metodo, versioni, possibilità di riprodurre |
| **Teme** | Propaganda, gergo, muri di testo | Perdere il filo tra sedute, mandati, richieste | Numeri senza fonte, grafici che ingannano, AI non controllabile |
| **Successo** | Dopo 2 minuti sa dire in una frase che cos'è GovernAI e una proposta che lo riguarda | Trova in un clic che cosa è nuovo da ieri e cosa aspetta una sua azione | Arriva in due clic alla fonte di ogni cifra e al link permanente da citare |

Un solo prodotto serve tutti e tre con la **lettura a tre livelli** (principio 2): *In breve* → *Dettagli* → *Fonti e metodo*.

## 3. Bisogni principali

1. **Orientarsi subito**: che cos'è, che cosa è cambiato oggi, da dove partire.
2. **Trovare per tema**, non per struttura interna (nessuno cerca "02-C2", molti cercano "asili nido").
3. **Capire costi e chi paga** di ogni proposta, sempre senza deficit.
4. **Vedere il ragionamento**: chi ha proposto, chi ha obiettato, chi ha deciso e con quale regola.
5. **Verificare**: fonte, data, stato di verifica di ogni numero; regole e catena di integrità.
6. **Conoscere i vincoli**: Costituzione, obblighi UE, regole di bilancio europee.
7. **Partecipare** con un gesto semplice e sapere che fine fa la propria richiesta.

## 4. Le 8 domande che un utente si fa (compiti principali)

| # | Domanda dell'utente | Dove trova la risposta | Pubblico principale |
|---|---|---|---|
| 1 | **Che cosa propone GovernAI su un tema che mi interessa?** (sanità, casa, tasse, scuola…) | Programma → filtro per tema, ricerca → scheda della proposta | Cittadino |
| 2 | **Quanto costa e chi paga?** | Scheda della proposta (blocco *Costi e coperture*); Programma → *Come si paga* | Tutti |
| 3 | **Come sta l'Italia oggi?** | Oggi (sintesi) → Dati → Indicatori e allerte | Cittadino, giornalista |
| 4 | **Che cosa ha deciso il governo ombra, perché, e chi era contrario?** | Governo → Seduta → Decisioni, Obiezioni dell'opposizione | Giornalista, attivo |
| 5 | **È compatibile con la Costituzione e con le regole europee?** | Scheda della proposta (blocco *Controlli*); Controlli → Costituzione, Europa | Esperto |
| 6 | **Che cosa chiede l'Europa all'Italia e dove siamo in ritardo?** | Controlli → Europa (scadenze, infrazioni, semestre europeo) | Esperto, giornalista |
| 7 | **Posso fidarmi? Chi controlla l'AI?** | Metodo; Controlli → Integrità; badge di verifica su ogni numero | Tutti |
| 8 | **Come propongo un'idea o una domanda, e che fine fa?** | Partecipa (sempre visibile in testata) | Attivo, cittadino |

Domanda trasversale, servita dal simulatore: *"Che cosa cambierebbe se contasse di più ciò che conta per me?"* (Programma → I tuoi valori).

## 5. Principi di design (7)

1. **Prima la risposta, poi il ragionamento.** Ogni schermata apre con una frase che risponde alla domanda dell'utente ("53 misure su 62, 12,99 mld l'anno, senza deficit"). Il dettaglio viene dopo, mai al posto della risposta.
2. **Tre livelli di lettura nella stessa pagina.** *In breve* (cittadino, 20 secondi), *Dettagli* (attivo), *Fonti e metodo* (esperto). Si aprono, non si cambiano pagine. Nessun pubblico è servito da un sito "minore".
3. **Ogni numero porta la sua prova.** Accanto a ogni cifra: fonte, periodo e stato (*Verificato su fonte*, *Stima GovernAI*, *Da verificare*, *Provvisorio*). Una cifra senza prova non si pubblica.
4. **La proposta è il centro.** Tutto si collega alla scheda della proposta: decisioni del Consiglio, controlli di Costituzione ed Europa, coperture, obiettivi e dati. Da ogni oggetto si arriva alla proposta in un clic, e viceversa.
5. **Mostrare il disaccordo, non nasconderlo.** Obiezioni dell'opposizione leale, deroghe del capo di governo, incertezza del panel e limiti dichiarati hanno lo stesso peso visivo delle decisioni.
6. **Stesso schema ovunque.** Un solo sistema di stati e gravità (4 livelli, colore + icona + parola) vale per proposte, Europa, Costituzione, decisioni e dati. Chi impara una schermata le sa leggere tutte.
7. **Accessibile e leggero per default.** WCAG 2.2 AA, mobile-first, funziona senza animazioni, con tema scuro, con lettore di schermo e su connessione lenta. Niente che dipenda solo dal colore o dal passaggio del mouse.

## 6. Tono di voce

**Chiaro, sobrio, verificabile, rispettoso.** Il tono di un buon servizio pubblico d'informazione, non di una campagna.

| Sì | No |
|---|---|
| Frasi brevi, soggetto-verbo-complemento, voce attiva | Periodi lunghi, nominalizzazioni ("effettuazione della verifica") |
| "Costa 0,15 miliardi l'anno. Lo paga la riallocazione di spese esistenti." | "Misura a costo contenuto con copertura idonea" |
| Sigle sciolte alla prima occorrenza: "Ragioneria generale dello Stato (RGS)" | "RGS", "UPB", "SAD", "LEP" senza spiegazione |
| Verbi al condizionale per ciò che è simulato: "il governo ombra adotterebbe" quando serve chiarezza; "ha deciso, in simulazione" nei verbali | Presentare decisioni simulate come atti in vigore |
| Dire i limiti: "È una stima GovernAI, non certificata dalla Ragioneria." | Certezze non dimostrate, superlativi ("la riforma più giusta") |
| Descrivere, non giudicare le persone e i partiti | Aggettivi valutativi sui partiti, ironia, slogan |
| "Tu" nei pulsanti e negli inviti ("Proponi un'idea"), impersonale nei contenuti | Imperativi aggressivi, urgenza artificiale ("Agisci ora!") |
| Numeri all'italiana: 12,99 mld; 5,6%; 8 novembre 2026 | 12.99bn, 11/08/26 |

Formula ricorrente, da usare sempre uguale: **"L'AI propone e verifica. Le persone decidono."**

## 7. Cosa evitare

- **Estetica da partito o da campagna**: volti, folle, bandiere, mani alzate, slogan in maiuscolo, countdown elettorali, "unisciti a noi".
- **Estetica da sito istituzionale ufficiale**: niente stemma della Repubblica, niente font Titillium Web e blu #0066CC di Designers Italia, niente "Governo italiano" o "Ministero" come intestazioni. GovernAI è una simulazione: confonderla con il governo vero sarebbe ingannevole. Il banner *Governo ombra · simulazione* è obbligatorio nelle pagine del Governo.
- **Estetica "AI magica"**: gradienti viola-blu, robot, cervelli luminosi, scintille ✨, effetti al neon. L'AI qui è uno strumento di lavoro, non un personaggio.
- **Dark pattern**: pop-up di iscrizione, contatori di pressione sociale, notifiche non richieste, pulsanti che nascondono l'alternativa.
- **Grafici ingannevoli**: assi tronchi non dichiarati, torte 3D, doppi assi, scale diverse tra grafici affiancati (regole in `04_design_system.md` §8).
- **Muri di testo**: i verbali reali superano le 300 mila battute; si leggono per sezioni, con sintesi in testa.
- **Gergo e codici come titoli**: "01-P3" è un'etichetta secondaria, il titolo è "IVA in tempo reale".
- **Emoji come semafori** (🔴🟢 nei bollettini attuali): sostituite da icone e parole.

## 8. Neutralità visiva

GovernAI dichiara di non essere né di destra né di sinistra né di centro. Il design deve dimostrarlo prima ancora che si legga una parola.

### 8.1 Regole

1. **Nessun colore che identifichi un partito o uno schieramento come colore di marca.** In Italia il rosso è associato alla sinistra storica e al PD, l'azzurro e il blu a Forza Italia, Fratelli d'Italia, Lega (dopo il 2018), Azione e Noi Moderati, il verde alla Lega storica e ad Alleanza Verdi e Sinistra, il giallo al Movimento 5 Stelle e a +Europa, il fucsia-viola a Italia Viva, l'arancione ad alcune liste civiche. Nessuno di questi è il colore principale dell'app.
2. **Nessuna combinazione tricolore** (verde-bianco-rosso) in elementi vicini: evoca la fiamma e i simboli nazionali usati nella comunicazione di partito. Per questo gli stati *favorevole* e *sfavorevole* non sono verde bandiera e rosso bandiera, ma **verde abete** e **mattone**, mai affiancati come blocchi pieni su bianco.
3. **Nessun simbolo politico**: fiamme, garofani, rose, soli nascenti, stelle a cinque punte, edere, querce, ulivi, colombe, pugni, mani aperte, croci, scudi crociati, fasci, frecce stilizzate verso destra o sinistra come marchio.
4. **Destra e sinistra non hanno significato politico nell'interfaccia.** Nei grafici divergenti (effetto sui valori da −3 a +3) il negativo è a sinistra e il positivo a destra per convenzione matematica; lo diciamo in legenda e non usiamo mai le parole "destra"/"sinistra" per descriverli.
5. **I partiti si citano in modo simmetrico**: ordine alfabetico o per dimensione parlamentare dichiarata, stesso stile tipografico, nessun logo, nessun colore di partito, stessa quantità di spazio. Vale per il confronto con i programmi (`benchmark/confronto_programmi.md`, 318 misure censite).
6. **Illustrazioni e foto**: niente persone riconoscibili, niente luoghi del potere usati come icona (Montecitorio, Palazzo Chigi). Si usano dati, schemi, mappe neutre e icone lineari.
7. **Il marchio è tipografico**: "GovernAI" in Source Serif 4, con un simbolo geometrico astratto (un cerchio diviso in dieci tacche, i dieci valori), senza riferimenti a bandiere o simboli.

### 8.2 La palette scelta e perché

| Ruolo | Chiaro | Scuro | Perché |
|---|---|---|---|
| Fondo "carta" | `#F7F6F2` | `#12171C` | Bianco caldo da quotidiano: comunica lettura e documento, non pubblicità |
| Testo "inchiostro" | `#17202A` | `#E8ECEF` | Quasi nero, massimo contrasto (15,2:1) |
| Accento "blu petrolio" | `#12506B` | `#7DBAD6` | Colore di interazione (link, pulsanti, voce attiva). Il petrolio è una tonalità tra blu e verde che nessun partito italiano usa come colore principale: non è l'azzurro di Forza Italia né il blu di Fratelli d'Italia, non è il verde della Lega storica o di AVS. Ricorda la carta stampata e gli strumenti di misura |
| Favorevole "verde abete" | `#1F6B4F` | `#6DC39D` | Solo con icona e parola, solo per stati (es. *Nucleo robusto*, *Compatibile*). Lontano dal verde bandiera `#009246` |
| Attenzione "ambra" | `#865200` | `#E3B04B` | Stati intermedi (*Condizionato*, *Da verificare*). Bruno-ambra, non il giallo del M5S |
| Sfavorevole "mattone" | `#A3402A` | `#F08D72` | Rischio alto, peggioramento. Arancio-bruno, lontano dal rosso bandiera `#CE2B37` e dal rosso di partito |
| Critico "vinaccia" | `#7D1E3C` | `#EE93B1` | Livello massimo (linea rossa, incompatibile, infrazione a sentenza). Si distingue dal mattone per luminosità e icona |

Il principio: **una sola tinta di marca (petrolio) e una scala di gravità che porta significato, non appartenenza.** I colori di stato occupano poca superficie (chip, bordi, icone); il grosso della pagina è carta e inchiostro. Tutte le coppie testo/fondo superano il rapporto 4,5:1 (valori in `04_design_system.md` §2).

Per i grafici divergenti si usa l'asse **blu petrolio ↔ arancio mattone**, distinguibile anche da chi ha deuteranopia o protanopia, sempre con segno (+/−) e posizione rispetto allo zero.

## 9. Vincoli di progetto

- Sito statico (oggi GitHub Pages), dati in un unico oggetto `window.GOVERNAI` generato ogni giorno. Nessun backend: ricerca e filtri lato client.
- Partecipazione tramite GitHub (issue e file di richiesta): il design deve spiegare il passaggio senza spaventare chi non conosce GitHub.
- Due sezioni nuove in arrivo: **Europa** (dati in `europa/`: 143 scadenze di recepimento, 84 procedure d'infrazione, semestre europeo, 298 atti in 30 giorni) e **Costituzione** (controllo di costituzionalità di leggi e manovre, per esempio il disegno di legge di bilancio A.C. 3174, con livelli di rischio).
- Lingua: italiano. Predisporre l'interfaccia a una futura versione inglese (etichette in un file, nessun testo dentro le immagini).

## 10. Misure di successo del design

| Obiettivo | Misura | Soglia |
|---|---|---|
| Comprensione | Test con 5 cittadini: "che cos'è GovernAI?" in una frase corretta dopo 2 minuti | 4 su 5 |
| Trovabilità | Trovare la proposta sugli asili nido partendo dalla home, da telefono | < 30 secondi, ≤ 3 tocchi |
| Verificabilità | Dalla cifra "34,4 mld di gap IVA" alla fonte primaria | ≤ 2 clic |
| Fiducia | Test con persone di orientamento diverso: "questo sito è di parte?" | Nessuna attribuzione coerente a uno schieramento |
| Accessibilità | Audit WCAG 2.2 AA (axe + verifica manuale con lettore di schermo) | 0 errori bloccanti |
| Prestazioni | Home su 4G lento | contenuto principale < 2,5 s |
