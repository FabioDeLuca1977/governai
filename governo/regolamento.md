# Regolamento del Consiglio dei ministri di GovernAI

GovernAI simula un governo: un capo di governo, nove ministri e un'opposizione leale. È un **governo ombra**: le sue decisioni non sono in vigore, ma vengono prese come se lo fossero e restano scritte, così si può verificare chi aveva ragione.

Il regolamento serve a rendere il modo di decidere migliore di quello abituale. Le regole sono applicate da `governo/consiglio.py`: una decisione che non le rispetta non entra nel verbale.

## I ruoli

| Ruolo | Compito | Cosa non può fare |
|---|---|---|
| **Ministri (9)** | Ognuno legge i dati e il dossier della sua area e presenta richieste motivate. Indica anche gli effetti sugli altri ministeri e a cosa è disposto a rinunciare | Valutare le proprie proposte. Decidere |
| **Opposizione leale** | Cerca il punto debole di ogni richiesta, con prove, e dice quale fatto le farebbe cambiare idea | Proporre misure proprie fuori dal programma. Decidere |
| **Capo di governo** | Arbitra i conflitti, decide e fissa i mandati ai ministri | Ignorare la Carta senza motivare. Superare una linea rossa |
| **Ragioneria** (deterministica) | Verifica che le decisioni siano finanziabili senza deficit | Essere scavalcata |
| **Ufficio legislativo** (deterministico) | Verifica la conformità giuridica e la redazione dei testi | Essere scavalcato |
| **Garante dei valori** (deterministico) | Applica le linee rosse della Carta | Essere scavalcato |

Ogni ruolo affidato all'AI è svolto da un agente distinto, che non vede il lavoro degli altri finché non ha consegnato il proprio. Prima scrivono i ministri; poi l'opposizione, che legge i ministri; per ultimo il capo, che legge tutto.

## Le regole

1. **Ruoli separati.** Chi propone non valuta, chi valuta non decide. I punteggi delle proposte restano quelli del panel indipendente: il Consiglio non li modifica.
2. **Ogni decisione è una scommessa scritta.** Chi chiede o decide dichiara cosa succederà: quale indicatore, quale soglia, entro quale periodo e con quale probabilità. Alla scadenza il sistema confronta la previsione con il dato ufficiale.
3. **Credibilità misurata.** Ogni previsione verificata riceve un punteggio (Brier: 0 = perfetta, 0,25 = come tirare a caso, 1 = sempre sbagliata). La credibilità di ministri, opposizione e capo è pubblica e il capo ne tiene conto.
4. **Pre-mortem obbligatorio.** Ogni richiesta dichiara il motivo più probabile per cui potrebbe fallire.
5. **Effetti sugli altri.** Ogni richiesta indica quali altri ministeri tocca e in che modo. Un effetto negativo non dichiarato, se emerso dopo, pesa sulla credibilità.
6. **Arbitrato con regole note.** Il capo decide in base alla Carta: prima le linee rosse, poi il nucleo robusto (regola 8), poi le priorità del momento, poi i valori. Se si discosta dall'esito del motore lo dichiara come **deroga** e lo motiva.
7. **Risposta all'opposizione.** Il capo risponde per iscritto a ogni obiezione sulle misure che adotta.
8. **Nessuna linea rossa, nessun deficit.** Una decisione che supera una linea rossa o non è finanziabile viene respinta da `consiglio.py` e annotata nel verbale.
9. **Verbale pubblico e immutabile.** Ogni seduta produce un verbale pubblicato sul sito e registrato nella catena di integrità.
10. **Mandati con scadenza.** Il capo affida compiti ai ministri con una data. Il mandato non svolto resta all'ordine del giorno finché non viene chiuso.

## Quando si riunisce

- Quando scatta un'allerta nuova o un dato cambia in modo rilevante.
- Quando un suggerimento approvato riguarda più ministeri.
- In ogni caso il lunedì, per la seduta ordinaria.

## Cosa resta umano

Il Consiglio consiglia. Le scelte politiche vere, cioè i pesi dei valori, l'approvazione dei suggerimenti e ogni pubblicazione verso l'esterno, restano alle persone.
