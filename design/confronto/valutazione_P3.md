# Valutazione P3 · Varianti mobile (375 px) e sintesi finale

**A** è il primo file incollato in chat (8 novembre 2026), **B** il secondo. Dallo stile del codice, A sembra Gemini e B ChatGPT. Ho letto il codice, ma non ho aperto i file nel browser.

## Scheda di sintesi

| Criterio | Peso | A | B | Note |
|---|---|---|---|---|
| Bellezza | 15 | 4 | 2 | **A:** cornici da telefono curate, schede compatte, buon ritmo. **B:** i badge «Da verificare» sono ovunque, anche sui chip dei temi, sui pulsanti dei filtri e sui titoli dei mesi, e su un telefono diventano rumore. |
| Chiarezza | 20 | 4 | 3 | **A:** la risposta in breve è completa e include la riserva di 1,15 mld. **B:** la risposta omette proprio la riserva di 1,15 mld, la cifra chiave della seduta. |
| Coerenza | 15 | 4 | 5 | **A:** il pulsante Partecipa e le sotto-schede sono alti 36 px, contro i 44 px dei pulsanti principali. **B:** tutto è uniforme. |
| Accessibilità | 20 | 2 | 5 | **A:** etichette della barra in basso a 11 px, chip a 11 px, percorso della seduta a 12 px (la regola era «mai sotto 13 px»). Pulsanti da 36 px, filtri non attivabili. **B:** testi di almeno 13 px, bersagli di 44 px, schede navigabili con le frecce, vista a dimensione reale, «salta al contenuto». |
| Neutralità | 15 | 5 | 5 | Nessun problema in nessuno dei due. Il banner di simulazione c'è. |
| Fedeltà alla specifica | 15 | 3 | 3 | **A:** etichette di riempimento non richieste («Monitora», «OK», «Aggiornate»); molte cifre senza badge. **B:** accorcia la citazione della domanda togliendo «2027-2029»; omette i costi delle varianti Essenziale e Pilota e gli obiettivi, che erano nel prompt. |
| **Totale /100** | | **72** | **77** | |
| Errori bloccanti | | no | no | Nessun contenuto inventato presentato come reale da nessuno dei due. |

Lo scarto è di 5 punti, quindi si applica la regola di parità: vince chi ha più *Chiarezza + Accessibilità*. A ha 6, B ha 8. **Vince B**, di poco.

## Sintesi dei tre confronti

| Prompt | Gemini | ChatGPT | Esito |
|---|---|---|---|
| P1 · Design system | 63, bloccante | 87 | ChatGPT |
| P2 · Desktop | 66, bloccante | 83 | ChatGPT |
| P3 · Mobile | 72 | 77 | ChatGPT, per spareggio |

### Decisione per il template finale
- **Struttura, componenti, accessibilità e comportamenti:** ChatGPT.
- **Resa visiva:** si prende da Gemini.
  - testate di sezione con filetto;
  - chip con bordo;
  - schede compatte su mobile;
  - icone nel menu desktop;
  - numeri chiave con etichetta in alto.

### Correzioni da applicare
- Il badge di verifica va **solo** sulle cifre che vengono da fonti esterne o da stime, mai sui conteggi interni, sui titoli o sui filtri.
- La risposta in breve della seduta riporta sempre la cifra chiave.
- Le citazioni si riportano integre.
- Fonti, periodi, varianti e obiettivi si compilano da `docs/data.js`; nel sito non restano segnaposto.
- Nessun testo sotto i 13 px, nessun bersaglio sotto i 44 px.
