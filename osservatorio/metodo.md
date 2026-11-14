# Osservatorio sul governo di oggi: il metodo

*Scritto il 14 novembre 2026. Vale per ogni commento in `osservatorio/atti/`.*

L'osservatorio commenta gli atti del Governo in carica e del Parlamento: la legge di bilancio 2027-2029 e i decreti e le leggi della fine del 2026. Lo scopo è aiutare chi vota a capire **che cosa cambia per la propria vita e per il Paese**, con lo stesso metro che GovernAI usa per il proprio programma.

## Le regole

1. **Prima i fatti, poi i valori, e sempre separati.** Ogni commento dice prima che cosa fa l'atto, con i numeri delle relazioni tecniche e delle fonti ufficiali. Il giudizio arriva dopo, in una sezione a parte, ed è riferito ai dieci valori della Carta (`01_carta_valori.md`), non a schieramenti.
2. **Lo stesso metro per tutti.** Gli atti del Governo si giudicano con le stesse regole usate per il programma GovernAI: niente deficit per la spesa corrente, coperture verificabili, valutazione prima e dopo, rispetto della Costituzione. Quando GovernAI ha lo stesso difetto, il commento lo dice.
3. **Nessun favoritismo, verso nessuna categoria.** Ogni commento risponde a due domande: *chi ci guadagna* e *chi paga*. Vale per tutti i gruppi organizzati: imprese e banche, sindacati e ordini professionali, dirigenza pubblica, enti territoriali, la politica stessa. Un vantaggio concentrato su pochi, pagato da molti, si segnala sempre, chiunque ne benefici.
4. **Il criterio è il benessere di chi vota.** La domanda guida è: questa norma migliora la vita delle persone, oggi e domani, a un costo giusto e chiaro? Non conta chi l'ha proposta.
5. **Si riconosce ciò che va bene.** Un atto si può approvare in tutto o in parte. Un commento che trova solo difetti, o solo pregi, va rivisto.
6. **Nessun colore, nessun nome.** Si parla del Governo, dei ministeri e del Parlamento come istituzioni. Niente partiti, niente persone, niente aggettivi polemici.
7. **Ogni affermazione ha una fonte.** Testo dell'atto, relazione tecnica, dossier dei Servizi studi, Ragioneria, UPB, Corte dei conti, ISTAT. Quello che non è verificato si scrive come stima o come domanda aperta.
8. **Due revisioni prima di pubblicare.** Ogni commento viene scritto da un agente AI e rivisto da altri due, con sensibilità politiche diverse, che controllano fatti, equilibrio e linguaggio. Non sostituisce la revisione di una persona esperta, che oggi manca: è scritto in testa a ogni commento. I rapporti della prima revisione, del 14 novembre 2026, sono in `revisioni/2026-11-14_osservatorio_revisione_liberale.md` e `revisioni/2026-11-14_osservatorio_revisione_sociale.md`.
9. **Si corregge in chiaro.** Se un fatto cambia (emendamenti, conversione in legge, nuovi dati), il commento si aggiorna e la modifica resta scritta in fondo.

## Il formato di un commento

Ogni atto è un file YAML in `osservatorio/atti/`, con questi campi:

| Campo | Contenuto |
|---|---|
| `id` | Codice breve, per esempio `manovra-2027-irap-energia` |
| `titolo` | Che cosa fa, in parole semplici |
| `atto` | Riferimento ufficiale (articoli compresi) |
| `tipo` | legge di bilancio, decreto-legge, legge, decreto legislativo |
| `data` | Data di presentazione o di pubblicazione |
| `stato` | Dove si trova l'atto (all'esame, in vigore, da convertire entro…) |
| `fonte` | Link al testo ufficiale |
| `tema` | Una delle aree del programma (`01`…`09`) |
| `in_breve` | Una o due frasi |
| `cosa_fa` | Elenco dei contenuti principali |
| `numeri` | Voce, valore, fonte |
| `chi_guadagna`, `chi_paga` | Elenchi, con le categorie organizzate dette per nome |
| `rischi_giuridici` | Esito dei controlli di costituzionalità e UE, con link agli esami di GovernAI |
| `valori` | Per ciascun valore toccato: segno (`+`, `-`, `=`) e motivo |
| `bilancio` | Una frase: nel complesso, che cosa va bene e che cosa no |
| `governai` | Proposte GovernAI sullo stesso problema e confronto onesto, compresi i difetti di GovernAI |
| `cosa_cambieremmo` | Correttivi concreti, anche piccoli |
| `domande_aperte` | Ciò che non si sa ancora |
| `fonti` | Elenco delle fonti |
| `revisioni` | Chi ha scritto e rivisto, e le modifiche nel tempo |

## La discussione

Sotto ogni commento la comunità su invito può discutere, con le regole e la moderazione di `comunita/regole.md`. I commenti della comunità non cambiano il commento di GovernAI: le osservazioni fondate entrano con una revisione scritta.
