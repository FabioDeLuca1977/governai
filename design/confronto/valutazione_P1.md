# Valutazione P1 · Design system visivo

Valutazione alla cieca. **A** è il primo file incollato in chat (8 novembre 2026), **B** il secondo. Dopo la valutazione: **A = Gemini, B = ChatGPT**. Griglia e regole sono in `design/05_prompt_chatgpt_gemini.md`.

Ho letto il codice di entrambi i file. Non li ho ancora aperti nel browser: mancano le verifiche rapide 1–3 (1440 e 375 px, tema scuro, navigazione con Tab).

## Scheda di sintesi

| Criterio | Peso | A | B | Note |
|---|---|---|---|---|
| Bellezza | 15 | 4 | 3 | A è più editoriale: titoli di sezione con filetto, campioni chiaro/scuro affiancati, chip con bordo. B è pulito ma più tecnico, e i badge sembrano pulsanti generici. |
| Chiarezza | 20 | 4 | 4 | Tutti e due sono ordinati. B ha un indice iniziale e un catalogo degli stati che si apre e chiude. |
| Coerenza | 15 | 3 | 4 | A cambia l'icona del "non valutato" (help-circle invece di circle-dashed) e usa le sigle L0–L3. B in un caso usa il colore "attenzione" per "Provvisorio". |
| Accessibilità | 20 | 2 | 5 | **A:** pulsante S alto 36 px, etichette della barra mobile a 11 px, contrasti dichiarati senza calcolarli, nessun collegamento "salta al contenuto". **B:** contrasti calcolati per ogni token sul fondo, bersagli di 44 px, `aria` corretti, chiusura con Esc, "salta al contenuto", movimento ridotto. |
| Neutralità | 15 | 5 | 5 | Nessun colore né simbolo di parte. Il banner di simulazione c'è in tutti e due. |
| Fedeltà alla specifica | 15 | 1 | 5 | A inventa contenuti (vedi sotto) e omette parti richieste: molti token, ombre, griglia, stati, chip Costituzione/Europa. B copre tutto e dichiara ciò che non può sapere. |
| **Totale /100** | | **63** | **87** | |
| Errori bloccanti | | **sì** | no | |

## Errore bloccante di A: contenuti inventati presentati come reali

- **«04-P2 · Sorveglianza biometrica di massa senza mandato» con linea rossa.** 04-P2 è un codice reale del nostro programma. Associarlo a una proposta inesistente e a una violazione dell'art. 13 è disinformazione.
- **Proposte e cifre senza base:** «08-P1 Esenzione pedaggi autostradali residenti», «01-P4 Fascicolo Sanitario Unico Unificato −0,40 mld».
- **Contraddizione:** 01-P3 compare come «Nessun rilievo» in tabella, mentre la specifica dice «Condizionato».
- **Fonte inventata** nel popover: «bilancio ISTAT 2025 con i flussi di cassa dell'Agenzia delle Entrate».
- **Timeline sbagliata:** una «Seduta Straordinaria · Screening del DDL di Bilancio» che non esiste.
- **Avviso inventato:** «Violazione costituzionale rilevata (Art. 81)».
- **Impronta finta:** quella mostrata è l'impronta sha256 di un file vuoto.
- **Contrasti non calcolati:** i rapporti sono scritti a mano e misurati sul colore tenue, non sul fondo.

## Esito

**Vince B.** È la base del template.

### Da prendere da A
- Testate di sezione con filetto e titolo serif.
- Coppie di campioni chiaro/scuro affiancate.
- Chip con bordo pieno, più leggibili.
- Intestazione della card proposta su una riga, con codice a sinistra e classe a destra.

### Da correggere in B
- «Provvisorio» va con il colore neutro, non con «attenzione».
- I badge di verifica devono avere uno stile proprio: oggi sono pulsanti generici.
- Il token `griglia` non è ridefinito per il tema scuro: le righe dei grafici restano chiare su fondo scuro. Proposta: #2A333C.
- Per il trend usare le frecce (arrow-up-right, arrow-down-right) invece di triangle e chevron.
- I link hanno `min-height: 44px` anche dentro il testo: va limitato ai link di navigazione.
- Il tema chiaro usa l'icona sunrise, che è già la voce «Oggi»: meglio sun.

## Riga da aggiungere ai prompt P2 e P3 (per tutti e due gli strumenti)

> Usa solo i codici di proposta, i numeri e le fonti scritti qui. Se ti serve un esempio in più, usa un segnaposto grigio "esempio" senza codice: non inventare proposte, cifre, fonti, impronte o rapporti di contrasto.
