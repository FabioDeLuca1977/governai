# Valutazione P2 · Template desktop (5 schermate)

**A** è il primo file incollato in chat l'8 novembre 2026, **B** il secondo. Lo stile del codice indica che A è di Gemini e B di ChatGPT, come in P1. La valutazione si basa sulla lettura del codice: i file non sono stati aperti nel browser.

## Scheda di sintesi

| Criterio | Peso | A | B | Note |
|---|---|---|---|---|
| Bellezza | 15 | 4 | 3 | A: home ordinata, voci di menu con icone, numeri chiave ben gerarchizzati. B: impaginazione editoriale più elegante, ma i badge «Da verificare» ripetuti ovunque la appesantiscono. |
| Chiarezza | 20 | 4 | 3 | A apre ogni schermata con la risposta. In B la risposta c'è, ma decine di badge «Da verificare» la diluiscono e fanno sembrare dubbie anche le cifre interne. |
| Coerenza | 15 | 3 | 5 | A: alcuni chip senza icona («Priorità Alta»), sezioni richiuse fatte con pulsanti invece di elementi apri/chiudi, logo a cerchio tratteggiato invece delle 10 tacche. B: testata, chip, badge e scala di gravità identici ovunque. |
| Accessibilità | 20 | 2 | 5 | A: nessun elemento apri/chiudi vero, schede fatte con link, pulsanti alti 32–36 px, nessun «salta al contenuto». B: schede navigabili con le frecce, filtri funzionanti, tasto «/» per la ricerca, finestra di dialogo accessibile, «salta al contenuto», sigle sciolte. |
| Neutralità | 15 | 5 | 5 | Nessun colore né simbolo di parte. Il banner di simulazione c'è; in B resta fisso in alto nel verbale. |
| Fedeltà alla specifica | 15 | 2 | 4 | A inventa testi e fonti (vedi sotto) e nella timeline omette le scadenze del 15/1 e del 29/1. B non inventa nulla, ma mette «Da verificare» anche sui dati già certi e lascia «testo» dove la fonte non era scritta nel prompt. |
| **Totale /100** | | **66** | **83** | |
| Errori bloccanti | | **sì** (meno grave di P1) | no | |

## Errori di A

**Contenuti inventati presentati come reali**
- «Che cosa fa il programma: priorità alle contromisure su energia e beni primari (02-C1, 02-C4)»: il contenuto attribuito alle proposte è inventato.
- «Sospensione immediata della proposta 07-C5 e riattivazione riserva»: la seconda parte è aggiunta.
- «Proposte correlate: 01-P4, 07-C2»: il collegamento con 01-P4 non esiste.
- Fonti con il badge «Verificato» mai date nel prompt: «Verificato · BCE» (spread), «Verificato · ISTAT» e «Provvisorio · Banca d'Italia».
- Frasi aggiunte: «Tendenza sostenuta sui beni di largo consumo», «Aggiornato alle regole UE del 2026», «Senza deficit integrativo».

**Errori di testo**
- Refuso: «Costo stmato».
- Il chip «Bordo neutro verificato» riporta un'istruzione del prompt come se fosse contenuto.

## Esito

**Vince B**, come in P1: ChatGPT resta la base del template.

### Da prendere da A
- Icone Lucide accanto alle 5 voci di menu desktop, come nella barra mobile.
- Schede dei numeri chiave con l'etichetta in alto, la cifra grande e il badge in basso.
- Variante selezionata con fondo accento tenue.
- La riga «Fonte» sotto ogni indicatore, compilata con le fonti vere (le prendiamo da `dati/`).

### Da correggere in B per il sito
- **Badge solo sulle cifre esterne.** Il badge di verifica va solo sulle cifre che vengono da fonti esterne o da stime. I conteggi interni (decisioni, esperti, mandati, scadenze) non lo portano: sono la «Registro della seduta» e rimandano alla catena di integrità.
- **Fonti e periodi dai dati.** Le fonti e i periodi mancanti si riempiono automaticamente da `docs/data.js`; nessun segnaposto «testo» nel sito pubblicato.
- **Indicatori più bassi.** Togliere l'altezza minima di 300 px dalle schede indicatore quando non c'è la serie storica.
- **Riquadro inutile nel verbale.** Il riquadro «Governo ombra · L'AI propone e verifica» accanto alla domanda ripete il motto e non aggiunge informazioni: va tolto.
