# GovernAI · Prompt per ChatGPT e Gemini

*Versione 1.0, 8 novembre 2026. I prompt sono **identici per i due strumenti**: si incollano così come sono, uno per conversazione nuova, senza allegati. Ogni prompt è autonomo: contiene i vincoli essenziali e i contenuti reali. La specifica completa è in `01_brief.md` … `04_design_system.md`.*

## Come usarli

1. Apri una **conversazione nuova** in ChatGPT e una in Gemini (stesso giorno, modello migliore disponibile, con canvas o anteprima HTML attiva).
2. Incolla lo **stesso prompt** in entrambe. Non aggiungere altro: il confronto deve essere alla pari.
3. Se uno strumento si ferma a metà, scrivi solo: `Continua dal punto in cui ti sei fermato, senza ricominciare.`
4. Salva ogni risultato come `design/confronto/<strumento>_<prompt>.html` (e le immagini come `.png`).
5. Valuta con la griglia in fondo, prima ognuno da solo, poi insieme.

Ordine consigliato: **P1** (design system) → **P2** (mockup desktop) → **P3** (mobile). Facoltativo: **P4** (immagini statiche di presentazione).

---

## P1 · Design system visivo

```text
Sei un product designer senior specializzato in servizi pubblici digitali, accessibilità WCAG 2.2 AA e design system. Crea il DESIGN SYSTEM VISIVO di "GovernAI" come UNA SOLA PAGINA HTML autonoma (HTML + CSS in un unico file, niente framework, solo Google Fonts e icone Lucide da CDN: https://unpkg.com/lucide@0.469.0/dist/umd/lucide.min.js).

CHE COS'È GOVERNAI
Un prototipo a scopo sociale di programma di governo post-ideologico: né destra né sinistra né centro. Ogni giorno scarica dati ufficiali, valuta 62 proposte secondo una Carta di 10 valori, simula un "governo ombra" (esperti, 9 ministri, opposizione leale, capo di governo) con regole verificabili, controlla coperture senza deficit, Costituzione e diritto UE, e registra tutto in una catena di impronte crittografiche. Motto: "L'AI propone e verifica. Le persone decidono." Tono: chiaro, sobrio, verificabile, rispettoso; un buon servizio pubblico d'informazione, non una campagna.

VINCOLI NON NEGOZIABILI
1. Neutralità visiva: nessun colore di partito come colore principale (niente rosso, azzurro/blu partitico, verde bandiera, giallo, fucsia, arancione); nessuna combinazione verde-bianco-rosso; nessun simbolo politico (fiamme, rose, garofani, soli, stelle a 5 punte, pugni, mani, scudi, bandiere, edifici del potere); nessuna persona riconoscibile; niente estetica "AI magica" (gradienti viola, robot, scintille).
2. Non deve sembrare un sito istituzionale ufficiale: niente stemma della Repubblica, niente font Titillium Web, niente blu #0066CC.
3. Ogni significato con colore + icona + parola, mai solo colore.
4. Contrasto AA in tema chiaro e scuro. Bersagli tattili almeno 44 px. Focus visibile 3 px.
5. Italiano semplice, sigle sciolte, numeri in formato italiano (12,99 mld; 5,6%; 8 nov 2026).

TOKEN (usa esattamente questi valori)
Chiaro: sfondo #F7F6F2, superficie #FFFFFF, superficie-2 #EFEDE7, bordo #D9D5CB, bordo-forte #8A8F94, testo #17202A, testo-2 #4E5964, accento (blu petrolio) #12506B, accento-hover #0C3D52, accento-tenue #E3EEF2, testo su accento #FFFFFF.
Stati (pieno/tenue): favorevole #1F6B4F/#E2F0E8; attenzione #865200/#FBEFD5; alto (mattone) #A3402A/#F8E5DF; critico (vinaccia) #7D1E3C/#F6E1E8; neutro #55606B/#ECEBE6.
Grafici: positivo #2B6F8F, negativo #B4532F, serie #12506B, confronto #5B6670, traccia e griglia #E6E3DA, zero #8A8F94.
Scuro: sfondo #12171C, superficie #1A2128, superficie-2 #222A33, bordo #34404B, bordo-forte #7C8894, testo #E8ECEF, testo-2 #A9B4BE, accento #7DBAD6, accento-hover #A3D0E4, accento-tenue #173544, testo su accento #12171C; favorevole #6DC39D/#16332A; attenzione #E3B04B/#3A2D12; alto #F08D72/#3D211B; critico #EE93B1/#3B1B27; neutro #A9B4BE/#28313A; grafici positivo #6FB0CF, negativo #F09A73.
Font (Google Fonts): titoli e numeri chiave "Source Serif 4" 600/700; testo e interfaccia "Source Sans 3" 400/600/700 con cifre tabulari; codici e impronte "Source Code Pro" 400.
Scala tipografica mobile→desktop: display 32→48; h1 28→36; h2 22→26; h3 18→19; numero chiave 30→36; corpo 16→17 (interlinea 1,55); piccolo 14; etichetta 13 maiuscoletto; chip 13.
Spaziature (base 4): 4, 8, 12, 16, 24, 32, 48, 64, 96. Raggi: 4, 8, 12, 20, pillola 999. Ombre: e1 0 1px 3px rgba(23,32,42,.08); e2 0 4px 12px rgba(23,32,42,.10); e3 0 12px 32px rgba(23,32,42,.18). Griglia: 4 colonne <600 px, 8 colonne 600-899, 12 colonne ≥900, contenuto massimo 1200 px, gutter 16/24.
Scala di gravità unica a 4 livelli + "non valutato": 0 Nessun rilievo (favorevole, icona circle-check), 1 Attenzione (attenzione, alert-circle), 2 Rischio alto (alto, alert-triangle), 3 Rischio critico (critico, octagon-x), — Non valutato (neutro, circle-dashed).

CHE COSA DEVE CONTENERE LA PAGINA (in quest'ordine, con questi titoli)
1. "Principi" — 7 principi in una riga ciascuno: prima la risposta poi il ragionamento; tre livelli di lettura; ogni numero porta la sua prova; la proposta è il centro; mostrare il disaccordo; stesso schema ovunque; accessibile e leggero.
2. "Colori" — campioni di tutti i token in chiaro e scuro affiancati, con nome, esadecimale e rapporto di contrasto sul fondo.
3. "Tipografia" — scala completa con esempi reali: "Governare con i dati, scegliere con i valori." / "IVA in tempo reale" / "12,99 mld/anno".
4. "Spazi, raggi, ombre, griglia".
5. "Componenti", ciascuno con varianti e stati (normale, passaggio, focus, disattivato, caricamento, vuoto, errore):
   - Pulsanti: primario, secondario, terziario; dimensioni M (44 px) e S.
   - Chip di classe: Nucleo robusto (favorevole, shield-check), Dipende dai valori (accento, scale), In coda (neutro, clock), Sfavorevole (alto, arrow-down-circle), Linea rossa (critico, octagon-x).
   - Chip di gravità/rischio della scala unica (vedi sopra) in versione Costituzione ed Europa (priorità critica/alta/media/bassa).
   - Badge di verifica cliccabili: Verificato (badge-check), Stima GovernAI (calculator), Da verificare (help-circle), Provvisorio (hourglass), con un popover aperto "Da dove viene questo numero".
   - Misuratore della variante: Piena ●●●, Essenziale ●●○, Pilota ●○○, Zero ○○○, Non inclusa.
   - Card della proposta (esempio: "Economia, Imprese, Turismo · 01-P3", "IVA in tempo reale", Nucleo robusto, controllo Condizionato, Piena ●●● 0,15 mld/anno) nelle varianti compatta, riga di tabella, non inclusa, con linea rossa.
   - Tabella dati con intestazione fissa, numeri allineati a destra, riga di gruppo, ordinamento, "Scarica CSV".
   - Indicatore con trend: "Inflazione (HICP) · ott 2026 · Provvisorio · 5,6 % · ▲ +1,4 sfavorevole · Fonte Eurostat"; e "NEET 15-29 · 2025 · 13,3 % · ▼ −1,9 favorevole".
   - Grafico divergente "Effetto sui 10 valori" da −3 a +3 con zero al centro: Fiducia e trasparenza +2,0; Responsabilità verso il futuro +1,7; Equità +1,7; Cittadinanza responsabile +1,7; Innovazione +1,0; Benessere +0,3; Sicurezza senza controllo assoluto −0,3; Rispetto e diversità 0; Apprendimento e cultura 0; Bellezza, patrimonio e accoglienza 0.
   - Timeline delle sedute (2 sedute dell'8 nov 2026 + prossima seduta ordinaria lunedì 9 nov) con contatore decisioni "46 adottate · 6 respinte · 1 rinviata".
   - Barra del rischio con legenda testuale: "Nessun rilievo 101 · Attenzione 23 · Rischio alto 13 · Critico 0" (dati reali dello screening del ddl di bilancio 2027).
   - Avvisi: informativo, attenzione, alto, critico.
   - Banner "Governo ombra · simulazione: le decisioni non sono in vigore." (icona flask-conical, fondo neutro tenue).
   - Testata desktop con 5 voci "Oggi · Programma · Governo · Dati · Controlli" + Cerca + Metodo + pulsante "Partecipa"; barra di navigazione mobile in basso con le stesse 5 voci (icone Lucide: sunrise, list-checks, users-round, chart-line, shield-check).
6. "Iconografia" — le icone Lucide usate e l'elenco di quelle vietate.
7. "Grafici: regole" — 6 regole visive con un esempio giusto e uno sbagliato (asse tronco, doppio asse).
8. "Microcopy" — 10 etichette standard (es. "Proponi un'idea", "Copia link permanente", "Dati fermi al 6/11/2026: l'aggiornamento automatico non è andato a buon fine.").

FORMATO DELLA RISPOSTA (obbligatorio, per poter confrontare)
A. Il file HTML completo in un unico blocco di codice, con un interruttore chiaro/scuro in alto (attributo data-tema sull'elemento html).
B. Subito dopo, una tabella "Autoverifica" con 10 righe: neutralità, contrasto, colore+icona+parola, focus, bersagli 44 px, font richiesti, token esatti, tema scuro, italiano semplice, nessun contenuto inventato oltre agli esempi forniti. Per ogni riga: "rispettato / parziale / no" e una frase.
Non inventare numeri, nomi di persone o partiti. Non aggiungere loghi.
```

---

## P2 · Mockup desktop: home e 4 schermate chiave

```text
Sei un product designer senior (servizi pubblici digitali, information architecture, WCAG 2.2 AA) e un esperto di comunicazione civica neutrale. Disegna il TEMPLATE GRAFICO DESKTOP (larghezza 1440 px, contenuto massimo 1200 px) di 5 schermate dell'app "GovernAI", come UNA SOLA PAGINA HTML autonoma (HTML + CSS + poco JavaScript in un file; solo Google Fonts e icone Lucide da https://unpkg.com/lucide@0.469.0/dist/umd/lucide.min.js). Le 5 schermate stanno una sotto l'altra, ciascuna in una cornice 1440 px con il titolo "Schermata N · Nome".

CHE COS'È GOVERNAI
Prototipo a scopo sociale di programma di governo post-ideologico (né destra né sinistra né centro). Dati ufficiali ogni giorno, 62 proposte valutate su una Carta di 10 valori, un governo ombra simulato con regole verificabili, coperture senza deficit, controlli di Costituzione e diritto UE, catena di integrità. Motto: "L'AI propone e verifica. Le persone decidono." Tre pubblici: cittadini curiosi (2 minuti, telefono), persone attive nel progetto, esperti e giornalisti (fonti, numeri, metodo).

VINCOLI NON NEGOZIABILI
- Neutralità: nessun colore di partito come colore principale, nessuna combinazione verde-bianco-rosso, nessun simbolo politico, nessuna persona o edificio del potere, niente estetica "AI magica". Non deve sembrare un sito istituzionale ufficiale (niente stemma, niente Titillium Web, niente blu #0066CC).
- Stile "carta e inchiostro": fondo #F7F6F2, superfici #FFFFFF, superficie-2 #EFEDE7, bordi #D9D5CB, testo #17202A, testo secondario #4E5964, UNA sola tinta di marca: blu petrolio #12506B (hover #0C3D52, tenue #E3EEF2). Stati (pieno/tenue): favorevole #1F6B4F/#E2F0E8, attenzione #865200/#FBEFD5, alto #A3402A/#F8E5DF, critico #7D1E3C/#F6E1E8, neutro #55606B/#ECEBE6. Grafici: positivo #2B6F8F, negativo #B4532F.
- Font: Source Serif 4 (titoli, numeri chiave), Source Sans 3 (testo, cifre tabulari), Source Code Pro (codici).
- Ogni significato con colore + icona + parola. Contrasto AA. Bersagli 44 px. Focus visibile.
- Navigazione identica in tutte le schermate: testata con logo "GovernAI" (logotipo serif + cerchio di 10 tacche), 5 voci "Oggi · Programma · Governo · Dati · Controlli", campo Cerca (tasto "/"), link "Metodo", pulsante primario "Partecipa", interruttore tema. Voce attiva evidenziata.
- Scala di gravità unica: Nessun rilievo (favorevole), Attenzione, Rischio alto, Rischio critico, Non valutato (neutro).
- Ogni cifra ha accanto un badge di verifica: Verificato / Stima GovernAI / Da verificare / Provvisorio.
- Usa SOLO i contenuti qui sotto. Non inventare numeri, persone, partiti o citazioni. Dove manca un testo usa un segnaposto grigio "testo".

SCHERMATA 1 · OGGI (home)
- Sopratitolo "Un programma di governo aperto, basato su dati e valori dichiarati"; titolo "Governare con i dati, scegliere con i valori."; testo "62 proposte valutate su 10 valori, finanziate senza deficit e controllate su Costituzione e regole UE. L'AI propone e verifica. Le persone decidono."; pulsanti "Esplora il programma" (primario) e "Come funziona".
- Riquadro "Oggi, 8 novembre 2026": 4 allerte attive; ultima seduta: oggi; catena integra, 9 anelli.
- 4 numeri chiave: "12,99 mld/anno · programma del momento, senza deficit · Stima GovernAI"; "53 su 62 · misure incluse · nucleo robusto 18 su 18 finanziato"; "334 · cifre verificate su fonte primaria · Verificato"; "118 · serie di dati aggiornate ogni giorno".
- Allerte attive (4): Inflazione sopra il 3% — 5,6% (ott 2026, provvisorio) ▲ +1,4 — diventano prioritarie 02-C1, 02-C4, 04-P2, 04-P3; Inflazione in forte aumento sull'anno; Debito/PIL in aumento di oltre 1 punto in un trimestre — 139,9% (II trim 2026) — sospesa 07-C5; Fiducia dei consumatori in netto calo — −23,3.
- Ultima seduta: "8 nov 2026 · Seduta a richiesta · Conti in ordine senza tagliare i servizi essenziali · 53 decisioni: 46 adottate, 6 respinte, 1 rinviata · 30 deroghe dichiarate · 57 previsioni registrate · 9 mandati".
- Prossime scadenze: 23 nov Direttiva (UE) 2024/1260 recupero e confisca dei beni (priorità alta, tra 15 giorni, collegata a 07-C2 e 07-C4); 30 nov parere della Commissione sul documento programmatico di bilancio; 2 dic Direttiva (UE) 2024/2831 lavoro tramite piattaforme digitali (alta); 31 dic mandato M003 al Ministro dell'ambiente.
- Proposte per tema (9): Economia, Imprese, Turismo 12; Lavoro, Welfare, Famiglia 6; Ambiente, Energia, Agricoltura 5; Infrastrutture e Territori 6; Istruzione, Ricerca, Cultura 6; Salute 6; Giustizia, Interno, Difesa 6; Esteri, Europa, Istituzioni 7; PA e Digitale 8.
- Striscia "Fiducia verificabile": catena integra · linee rosse automatiche · tutto riproducibile. Riquadro finale "Hai un'idea o una domanda? Serve un account GitHub gratuito." + "Proponi un'idea".

SCHERMATA 2 · SCHEDA DELLA PROPOSTA (Programma)
- Briciole: Programma › Economia, Imprese, Turismo › 01-P3. Titolo "IVA in tempo reale". Chip "Nucleo robusto". "Nel programma del momento: Piena ●●● · 0,15 mld/anno · robustezza 99%".
- Blocco "In breve": problema in un dato "34,4 mld di IVA non versata nel 2023, +3,6 mld sul 2022" (Verificato · MEF, Relazione evasione 2026, tab. III.1); soluzione "L'Agenzia delle entrate incrocia fatture elettroniche, corrispettivi e pagamenti e blocca i crediti anomali prima che il denaro sparisca. Rimborsi entro 60 giorni a chi è affidabile. Nessun nuovo condono."; costo "0,15 mld/anno · Stima GovernAI · riallocazione di spese"; governo ombra "Adottata con deroga: parte in versione Essenziale finché l'UE non autorizza la parte Piena · mandato M001 entro il 28/2/2027". Mostra il banner "Governo ombra · simulazione" in piccolo vicino a questo blocco.
- Grafico divergente "Effetto sui 10 valori" (−3 peggiora … +3 migliora): Fiducia e trasparenza +2,0; Responsabilità verso il futuro +1,7; Equità +1,7; Cittadinanza responsabile +1,7; Innovazione +1,0; Benessere +0,3; Sicurezza senza controllo assoluto −0,3; Rispetto e diversità, Apprendimento e cultura, Bellezza patrimonio e accoglienza 0.
- Varianti in 3 colonne: Piena ●●● 0,15 mld (nel programma; con inversione contabile e split payment previa autorizzazione UE); Essenziale ●●○ 0,08 mld (senza estensione); Pilota ●○○ 0,04 mld (3 settori ad alto rischio per 2 anni).
- Controlli: Costituzionale "Attenzione · Condizionato" (artt. 3, 23, 24, 41, 53, 97 Cost.); Europeo "Attenzione · Condizionato" (Dir. 2006/112/CE; ViDA); variante Piena "Attenzione · Richiede notifica" (deroga art. 395). Scadenza UE collegata: Direttiva (UE) 2025/516 (ViDA), 31/12/2026.
- Obiettivi: Gap IVA da 34,4 a 28,5 mld; rimborsi IVA entro 60 giorni; nuovi condoni 0 — tutti "Si misura a mano".
- Sezioni richiuse: Testo completo (articolato normativo), Fonti e metodo. Indice della pagina a destra. Azioni: Condividi, Copia link permanente, Segnala un errore. Blocco "Collegato a".

SCHERMATA 3 · VERBALE DI SEDUTA (Governo)
- Banner fisso "Governo ombra · simulazione: le decisioni non sono in vigore."
- "Seduta a richiesta · 8 nov 2026"; titolo "Conti in ordine senza tagliare i servizi essenziali"; chip "Confermata dalla verifica di oggi".
- Percorso in 4 passi: Esperti (8) → Ministri (9) → Opposizione leale (8 obiezioni) → Capo di governo.
- La domanda (citazione): "Qual è il piano 2027-2029 per riportare il debito pubblico su una traiettoria discendente senza tagliare i servizi essenziali?" con "Perché ora" e "Vincoli" richiudibili.
- Risposta in breve: riserva per il risanamento di 1,15 mld l'anno a regime; coperture contate al minimo; gettito della lotta all'evasione al deficit; sanità, scuola e sicurezza si riorganizzano, non si riducono.
- Decisioni: barra impilata "46 adottate · 6 respinte · 1 rinviata", filtri, e 3 righe: "02-C2 Nido esigibile + congedo paterno · Essenziale ●●○ · Adottata · Regola 8 nucleo robusto"; "02-C5 Progetto di vita esigibile e lavoro per le persone con disabilità · Essenziale ●●○ · Adottata"; "03-P4 Prevenire costa meno: fondo prevenzione e assicurazione catastrofale · Essenziale ●●○ · Adottata".
- Deroghe dall'esito del motore (sempre visibili): "01-P3: il motore indicava Piena → Essenziale. La parte che la distingue non può partire prima dell'autorizzazione UE. Libera 0,07 mld/anno." e "07-C2: il motore indicava Piena → Essenziale; libera circa 0,20 mld per la riserva".
- Una card "Obiezione dell'opposizione leale" con 4 righe: OBIEZIONE "Copertura non certificabile e costo spostato sui redditi medio-bassi senza compensazione piena" (02-C2, copertura art. 6) · PROVA "coperture_menu.csv RB05; Carta, linea rossa Equità" · CAMBIEREBBE IDEA SE "un allegato della Ragioneria arriva a 1,0 mld senza RB05" · RISPOSTA DEL CAPO con chip attenzione "Non registrata nel verbale" e link "vedi la decisione su 02-C2". Bordo neutro, non rosso.
- Sezioni richiuse: Pareri degli esperti (8), Posizioni dei ministri (9), Mandati (9: M011-M019). Riga finale "57 previsioni registrate · anello n. 8 della catena · f9ecf15b4ac3…".

SCHERMATA 4 · DATI (cruscotto)
- Titolo "Dati"; frase "4 allerte attive su 14 indicatori: inflazione e debito in salita, fiducia in calo."; schede "Indicatori · Allerte 4 · Obiettivi e risultati · Diario quotidiano".
- 2 allerte in evidenza con "Che cosa fa il programma".
- Card indicatori per gruppi: PREZZI E CONTI PUBBLICI: Inflazione (HICP) 5,6% ott 2026 provvisorio ▲ +1,4 sfavorevole; Debito pubblico 139,9% del PIL II trim 2026 provvisorio ▲ +1,3 sfavorevole; Spread IT-DE 88,9 punti base set 2026 ▲ +8,8 sfavorevole; Spesa per interessi 3,8% del PIL 2025 ▼ −0,1 favorevole; Saldo di bilancio −3,1% del PIL 2025 ▲ +0,3 favorevole. LAVORO E GIOVANI: Disoccupazione 6,3% set 2026 ▲ +0,1 sfavorevole; Disoccupazione under 25 19,9% ▼ −0,4 favorevole; NEET 15-29 13,3% 2025 ▼ −1,9 favorevole. CRESCITA: PIL reale 0,0% sul trimestre III trim 2026 ▼ −0,2 sfavorevole; Produzione industriale 92,8 (2021=100) ▼ −1,2 sfavorevole; Fiducia dei consumatori −23,3 ▼ −0,1 sfavorevole. SOCIETÀ: Fecondità 1,18 figli per donna 2024 ▼ −0,03 sfavorevole.
- Ogni card: freccia + segno + parola "favorevole/sfavorevole", fonte con badge. Niente minigrafici inventati: disegna solo un segnaposto grigio con scritto "serie storica".

SCHERMATA 5 · CONTROLLI › EUROPA (con accesso a Costituzione)
- Sotto-navigazione "Costituzione · Europa · Integrità" (Europa attiva) e schede "Scadenze 143 · Infrazioni 84 · Semestre europeo · Novità 298".
- Frase: "Nei prossimi 60 giorni scadono 6 obblighi di recepimento. Infrazioni aperte: 84. Procedura per disavanzo eccessivo: in corso."
- 4 numeri: In scadenza entro 60 giorni 6 (5 senza misure italiane notificate); Già scadute 103 (80 con completezza da verificare); Infrazioni 84 aperte (10 a sentenza); Disavanzo eccessivo: in corso dal 26/7/2024.
- Timeline orizzontale dei prossimi 90 giorni: 23/11 Dir. 2024/1260; 30/11 parere Commissione; 2/12 Dir. 2024/2831; 5/12 Dir. 2024/2810; 9/12 Dir. 2024/2853; 11/12 Dir. 2024/2881; 31/12 Dir. 2025/516 (ViDA); 15/1 Dir. 2025/1237; 29/1 Dir. 2025/1 e 2025/2.
- 2 righe di elenco: "Alto · 23 nov 2026 · tra 15 giorni · Recupero e confisca dei beni · Direttiva (UE) 2024/1260 · CELEX 32024L1260 · In termine, nessuna misura italiana notificata · collegata a 07-C2, 07-C4 · EUR-Lex ↗"; "Critico · termine scaduto il 30/12/2024 · Antiriciclaggio · Direttiva (UE) 2015/849 · Infrazione aperta: messa in mora · collegata a 06-C6".
- Fasi delle infrazioni come barre con etichette: Messa in mora 48 → Parere motivato 19 → Ricorso 4 → Sentenza 5 → Messa in mora art. 260 3 → Sentenza art. 260 con sanzioni 5.
- In fondo, un riquadro di anteprima "Costituzione": avvertenza "Controllo preventivo automatico con revisione umana. Non è un giudizio: decide solo la Corte costituzionale." e barra del rischio dell'"A.C. 3174 · Disegno di legge di bilancio 2027" con legenda "Nessun rilievo 101 · Attenzione 23 · Rischio alto 13 · Critico 0" (screening automatico; esame approfondito: 5 dubbi seri).

FORMATO DELLA RISPOSTA (obbligatorio, per poter confrontare)
A. Il file HTML completo in un unico blocco di codice, con le 5 schermate nell'ordine dato.
B. Subito dopo, una tabella "Autoverifica" (10 righe: neutralità, contrasto, colore+icona+parola, navigazione identica, badge di verifica sui numeri, banner di simulazione, gerarchia "prima la risposta", font e token esatti, nessun contenuto inventato, accessibilità da tastiera) con "rispettato / parziale / no" e una frase.
C. Tre righe: le 3 scelte di design più importanti che hai fatto e perché.
```

---

## P3 · Varianti mobile (375 px)

```text
Sei un product designer senior mobile-first (servizi pubblici digitali, WCAG 2.2 AA). Disegna le VARIANTI MOBILE (larghezza 375 px, margini laterali 16 px) di 5 schermate dell'app "GovernAI", come UNA SOLA PAGINA HTML autonoma (HTML + CSS + poco JavaScript; solo Google Fonts e icone Lucide da https://unpkg.com/lucide@0.469.0/dist/umd/lucide.min.js). Mostra le 5 schermate AFFIANCATE, ognuna dentro una cornice di telefono 375 × 812 px che scorre in verticale, con il titolo sopra.

CHE COS'È GOVERNAI
Prototipo a scopo sociale di programma di governo post-ideologico (né destra né sinistra né centro): dati ufficiali ogni giorno, 62 proposte valutate su 10 valori, governo ombra simulato con regole verificabili, nessun deficit, controlli di Costituzione e diritto UE, catena di integrità. "L'AI propone e verifica. Le persone decidono." Pubblico principale su mobile: cittadini curiosi con 2 minuti.

VINCOLI NON NEGOZIABILI
- Neutralità: nessun colore di partito come colore principale, niente verde-bianco-rosso, nessun simbolo politico, nessuna persona, niente estetica "AI magica"; non sembrare un sito istituzionale (niente stemma, Titillium Web, blu #0066CC).
- Colori: fondo #F7F6F2, superficie #FFFFFF, superficie-2 #EFEDE7, bordo #D9D5CB, testo #17202A, testo-2 #4E5964, accento unico blu petrolio #12506B (tenue #E3EEF2). Stati pieno/tenue: favorevole #1F6B4F/#E2F0E8, attenzione #865200/#FBEFD5, alto #A3402A/#F8E5DF, critico #7D1E3C/#F6E1E8, neutro #55606B/#ECEBE6. Grafici: positivo #2B6F8F, negativo #B4532F.
- Font: Source Serif 4 (titoli 28 px, numeri 30 px), Source Sans 3 (corpo 16 px, mai sotto 13 px), Source Code Pro (codici).
- Testata compatta 56 px: logo "GovernAI", icona Cerca, pulsante "Partecipa". BARRA DI NAVIGAZIONE IN BASSO fissa, 64 px, 5 voci con icona 24 px ED etichetta: Oggi (sunrise), Programma (list-checks), Governo (users-round), Dati (chart-line), Controlli (shield-check). Voce attiva in accento con indicatore sopra l'icona.
- Bersagli tattili ≥ 44 px, nessuno scorrimento orizzontale della pagina (consentito solo in file di chip/schede scorrevoli, con l'ultima voce tagliata a metà). Sezioni lunghe richiuse (details/summary) con conteggio.
- Ogni significato con colore + icona + parola. Ogni cifra con badge: Verificato / Stima GovernAI / Da verificare / Provvisorio.
- Usa SOLO i contenuti qui sotto. Non inventare numeri, persone, partiti.

LE 5 SCHERMATE
1. OGGI — titolo "Governare con i dati, scegliere con i valori."; testo breve "62 proposte, 10 valori, nessun deficit. L'AI propone e verifica. Le persone decidono."; pulsante a tutta larghezza "Esplora il programma"; griglia 2×2: "12,99 mld/anno senza deficit", "53 su 62 misure incluse", "4 allerte attive", "Catena integra"; allerte (2 visibili + "altre 2"): Inflazione sopra il 3% 5,6% ▲ +1,4 ott 2026; Debito/PIL in salita 139,9%; ultima seduta "Conti in ordine senza tagliare i servizi essenziali · 46 adottate · 6 respinte · 1 rinviata"; prossime scadenze: 23 nov Dir. 2024/1260, 30 nov parere Commissione; chip scorrevoli dei temi (Economia 12, Lavoro 6, Ambiente 5, Infrastrutture 6, Istruzione 6, Salute 6, Giustizia 6, Esteri 7, PA 8).
2. SCHEDA DELLA PROPOSTA — "‹ Programma", "ECONOMIA · 01-P3", titolo "IVA in tempo reale", chip Nucleo robusto, "Piena ●●● · 0,15 mld/anno", pulsante "In questa pagina ▾"; blocco IN BREVE con numero grande "34,4 mld" "di IVA non versata nel 2023" (Verificato · MEF 2026), soluzione in 2 frasi, costo 0,15 mld/anno (Stima GovernAI), governo ombra "Adottata con deroga · M001 entro 28/2/2027" con mini-banner simulazione; grafico valori ridotto a 3 righe (Fiducia +2,0; Futuro +1,7; Sicurezza −0,3) + "Mostra tutti i 10"; sezioni richiuse: Varianti (3), Controlli (2 condizionati), Obiettivi (3), Governo ombra, Testo completo, Fonti e metodo; azioni Condividi e Segnala un errore.
3. VERBALE DI SEDUTA — banner compatto "Simulazione · non in vigore"; "8 NOV 2026 · A RICHIESTA"; titolo "Conti in ordine senza tagliare i servizi essenziali"; chip "Confermata oggi"; percorso ①Esperti ②Ministri ③Opposizione ④Capo; la domanda (citazione troncata con "Altro"); risposta in breve; Decisioni con barra "46 · 6 · 1" e schede filtro scorrevoli (Tutte 53, Adottate 46, Respinte 6, Rinviate 1); 2 card decisione (02-C2 Nido esigibile + congedo paterno · Essenziale ●●○ · Adottata; 03-P4 Prevenire costa meno · Essenziale ●●○ · Adottata); Deroghe (30) e Obiezioni (8) aperte; Pareri (8), Ministri (9), Mandati (9) richiusi.
4. DATI — frase "4 allerte attive su 14 indicatori"; schede scorrevoli; card indicatori in una colonna, layout orizzontale (nome e periodo a sinistra, valore e trend a destra): Inflazione (HICP) 5,6% ott 2026 provvisorio ▲ +1,4 sfavorevole; Debito pubblico 139,9% PIL ▲ +1,3 sfavorevole; Disoccupazione under 25 19,9% ▼ −0,4 favorevole; NEET 13,3% ▼ −1,9 favorevole; PIL reale 0,0% ▼ −0,2 sfavorevole; gruppi richiudibili.
5. CONTROLLI › EUROPA — sotto-schede "Costituzione · Europa · Integrità"; frase "Nei prossimi 60 giorni scadono 6 obblighi. Infrazioni aperte: 84."; griglia 2×2 (6 in scadenza; 103 già scadute; 84 infrazioni; disavanzo eccessivo in corso); elenco per mese "NOVEMBRE 2026": card "Alto · 23 nov · tra 15 giorni · Recupero e confisca dei beni · Dir. (UE) 2024/1260 · nessuna misura italiana notificata · collegata a 07-C2, 07-C4"; "DICEMBRE 2026": "Alto · 2 dic · Lavoro tramite piattaforme digitali · Dir. (UE) 2024/2831"; "Alto · 31 dic · IVA nell'era digitale (ViDA) · Dir. (UE) 2025/516 · collegata a 01-P3, 01-P10".

FORMATO DELLA RISPOSTA (obbligatorio, per poter confrontare)
A. Il file HTML completo in un unico blocco di codice.
B. Tabella "Autoverifica" (10 righe: neutralità, contrasto, bersagli 44 px, barra in basso identica, nessuno scorrimento orizzontale, testo ≥ 13 px, colore+icona+parola, badge di verifica, sezioni richiuse, nessun contenuto inventato) con "rispettato / parziale / no" e una frase.
C. Tre righe: che cosa hai sacrificato rispetto al desktop e perché.
```

---

## P4 · (Facoltativo) Immagini statiche di presentazione

Per strumenti che generano immagini. Utile per una presentazione, **non** per validare i dettagli (le immagini generate sbagliano spesso testo e numeri).

```text
Genera un'immagine 1600 × 1000 px: un'inquadratura frontale e piatta (nessuna prospettiva, nessuna mano, nessuna persona) di un laptop e uno smartphone affiancati su fondo uniforme #EFEDE7, che mostrano la home dell'app civica "GovernAI".
Stile "carta e inchiostro": fondo pagina bianco caldo #F7F6F2, card bianche con bordi sottili #D9D5CB, testo quasi nero #17202A, un solo colore di marca blu petrolio #12506B per pulsanti e voce di menu attiva; piccole etichette di stato in verde abete #1F6B4F, ambra #865200 e mattone #A3402A, sempre con icona lineare e parola. Titoli in un serif editoriale (tipo Source Serif), testo in un sans leggibile (tipo Source Sans).
Contenuto visibile sul laptop: testata con "GovernAI" e menu "Oggi · Programma · Governo · Dati · Controlli" e pulsante "Partecipa"; grande titolo "Governare con i dati, scegliere con i valori."; quattro riquadri numerici "12,99 mld/anno", "53 su 62", "334", "118". Sullo smartphone: la stessa home in colonna e una barra di navigazione in basso con 5 icone lineari ed etichette.
Vietato: bandiere, tricolore, stemmi, edifici istituzionali, persone, folle, simboli di partito, stelle UE, gradienti viola, robot, scintille, effetti neon. Atmosfera: sobria, autorevole, chiara, come un buon quotidiano digitale.
```

---

## Griglia di valutazione (ChatGPT vs Gemini)

Ogni valutatore assegna da **1** a **5** per criterio, senza sapere quale strumento ha prodotto il risultato (rinominare i file in *A* e *B* prima di valutare). Punteggio pesato su 100: `somma(voto × peso) / 5`.

| # | Criterio | Peso | 5 = eccellente | 3 = sufficiente | 1 = insufficiente |
|---|---|---|---|---|---|
| 1 | **Bellezza** | 15 | Elegante, equilibrata, editoriale; ritmo e respiro coerenti | Ordinata ma generica ("template") | Disordinata o datata |
| 2 | **Chiarezza** | 20 | In 20 secondi si capisce che cos'è e dove andare; ogni schermata apre con la risposta | Si capisce con qualche sforzo | Gerarchia confusa, muri di testo |
| 3 | **Coerenza** | 15 | Navigazione, chip, badge, scala di gravità identici in tutte le schermate | Piccole incoerenze (2-3) | Ogni schermata ha uno stile diverso |
| 4 | **Accessibilità** | 20 | Contrasti AA in chiaro e scuro, colore+icona+parola, focus visibile, bersagli 44 px, struttura dei titoli corretta | 1-2 mancanze minori | Testo illeggibile, significato solo nel colore |
| 5 | **Neutralità** | 15 | Nessun colore, simbolo o tono di parte; non sembra un sito di partito né istituzionale; banner di simulazione presente | Un elemento discutibile | Colori o simboli di parte, tono da campagna |
| 6 | **Fedeltà alla specifica** | 15 | Token, font, contenuti e numeri esatti; nessun dato inventato; formato di risposta rispettato | Qualche deviazione dichiarata | Numeri inventati, token ignorati |

**Errori bloccanti** (il risultato si scarta, qualunque sia il punteggio): numeri o citazioni inventati presentati come reali; colori di partito come tinta dominante o combinazione tricolore; testo sotto 4,5:1 nel corpo; decisioni del governo ombra presentate come in vigore (banner assente); persone o simboli politici.

**Verifiche rapide da fare su ogni file**
1. Aprire l'HTML nel browser a 1440 px e a 375 px.
2. Passare il tema scuro.
3. Navigare solo con Tab: il focus si vede sempre?
4. Controllare 5 numeri a caso contro questo documento.
5. Strumento di contrasto (es. estensione axe DevTools) sulla home.
6. Domanda a 3 persone di orientamento diverso: "Di che parte ti sembra?"

**Scheda di sintesi**

| Criterio | Peso | A (voto) | B (voto) | Note |
|---|---|---|---|---|
| Bellezza | 15 | | | |
| Chiarezza | 20 | | | |
| Coerenza | 15 | | | |
| Accessibilità | 20 | | | |
| Neutralità | 15 | | | |
| Fedeltà alla specifica | 15 | | | |
| **Totale /100** | | | | |
| Errori bloccanti | | sì/no | sì/no | |

Regola di decisione: vince il punteggio più alto senza errori bloccanti; a parità (± 5 punti), vince chi ha più alto *Chiarezza + Accessibilità*. Gli elementi migliori del perdente si annotano e si portano nel template finale.
