# Regolamento del Consiglio dei ministri di GovernAI

GovernAI simula un governo: un capo di governo, nove ministri, un'opposizione leale e un collegio di esperti di ogni materia. È un **governo ombra**: le sue decisioni non sono in vigore, ma vengono prese come se lo fossero e restano scritte, così si può verificare chi aveva ragione.

Il regolamento serve a rendere il modo di decidere migliore di quello abituale. Le regole sono applicate da `governo/consiglio.py`: una decisione che non le rispetta non entra nel verbale.

## I ruoli

| Ruolo | Compito | Cosa non può fare |
|---|---|---|
| **Esperti** (collegio di 19 materie) | Danno pareri tecnici indipendenti, con fonti, grado di certezza e limiti di ciò che si sa. Giudicano le proposte della loro materia | Decidere. Esprimere preferenze politiche. Proporre misure fuori dal programma |
| **Ministri (9)** | Ognuno legge i dati e il dossier della sua area e presenta richieste motivate. Indica anche gli effetti sugli altri ministeri e a cosa è disposto a rinunciare | Valutare le proprie proposte. Decidere |
| **Opposizione leale** | Cerca il punto debole di ogni richiesta, con prove, e dice quale fatto le farebbe cambiare idea | Proporre misure proprie fuori dal programma. Decidere |
| **Capo di governo** | Arbitra i conflitti, decide e fissa i mandati ai ministri | Ignorare la Carta senza motivare. Superare una linea rossa |
| **Ragioneria** (deterministica) | Verifica che le decisioni siano finanziabili senza deficit | Essere scavalcata |
| **Ufficio legislativo** (deterministico) | Verifica la conformità giuridica, la redazione dei testi e, con lo screening costituzionale, i rischi di illegittimità | Essere scavalcato |
| **Osservatorio UE** (deterministico) | Porta in seduta gli obblighi UE in scadenza, le infrazioni e il Semestre europeo per le aree convocate | Essere ignorato |
| **Garante dei valori** (deterministico) | Applica le linee rosse della Carta | Essere scavalcato |

Ogni ruolo affidato all'AI è svolto da un agente distinto, che non vede il lavoro degli altri finché non ha consegnato il proprio. L'ordine è questo:
1. gli **esperti** scrivono i pareri, ognuno per conto suo;
2. i **ministri** leggono i pareri e scrivono le loro richieste;
3. l'**opposizione** legge pareri e richieste;
4. il **capo di governo** legge tutto e decide.

In ogni seduta partecipano sempre l'economista di finanza pubblica, il giurista e il costituzionalista. L'esperto di affari europei entra quando le aree convocate hanno obblighi UE critici o infrazioni. Gli altri esperti, fino a sette in tutto, sono scelti in base alla domanda e alle allerte. L'elenco completo è in `governo/esperti.yaml`.

## Le regole

1. **Ruoli separati.** Chi propone non valuta, chi valuta non decide. I punteggi delle proposte restano quelli del panel indipendente: il Consiglio non li modifica.
2. **Ogni decisione è una scommessa scritta.** Chi chiede o decide dichiara cosa succederà: quale indicatore, quale soglia, entro quale periodo e con quale probabilità. Alla scadenza il sistema confronta la previsione con il dato ufficiale.
3. **Credibilità misurata.** Ogni previsione verificata riceve un punteggio (Brier: 0 = perfetta, 0,25 = come tirare a caso, 1 = sempre sbagliata). La credibilità di esperti, ministri, opposizione e capo è pubblica e il capo ne tiene conto.
4. **Pre-mortem obbligatorio.** Ogni richiesta dichiara il motivo più probabile per cui potrebbe fallire.
5. **Effetti sugli altri.** Ogni richiesta indica quali altri ministeri tocca e in che modo. Un effetto negativo non dichiarato, se emerso dopo, pesa sulla credibilità.
6. **Arbitrato con regole note.** Il capo decide in base alla Carta: prima le linee rosse, poi il nucleo robusto (regola 8), poi le priorità del momento, poi i valori. Se si discosta dall'esito del motore lo dichiara come **deroga** e lo motiva.
7. **Risposta all'opposizione.** Il capo risponde per iscritto a ogni obiezione sulle misure che adotta.
8. **Nessuna linea rossa, nessun deficit.** Una decisione che supera una linea rossa o non è finanziabile viene respinta da `consiglio.py` e annotata nel verbale.
9. **Verbale pubblico e immutabile.** Ogni seduta produce un verbale pubblicato sul sito e registrato nella catena di integrità.
10. **Mandati con scadenza.** Il capo affida compiti ai ministri con una data. Il mandato non svolto resta all'ordine del giorno finché non viene chiuso.
11. **Rispetto della competenza.** Se il capo adotta una proposta su cui un esperto ha dato parere contrario, risponde per iscritto al parere. Un parere senza fonti, senza grado di certezza o senza i limiti di ciò che si sa non viene considerato.
12. **Costituzione e Unione europea vengono prima.** Se il giurista o il costituzionalista segnalano un'**illegittimità probabile**, con una sentenza verificata, la misura è sospesa finché il capo di governo non la riformula per iscritto. Gli obblighi UE in scadenza o in infrazione nelle aree convocate si affrontano nella seduta, con una misura di recepimento o un mandato. Le raccomandazioni del Semestre europeo valgono come vincolo per le misure di bilancio.

## Quando si riunisce

- **A richiesta**, su una domanda precisa, che può arrivare in tre modi:
  - da chiunque, con il modulo "Domanda al Consiglio" sul sito, dopo l'approvazione di un membro del progetto;
  - da un membro del progetto, con un file in `governo/richieste/`;
  - in chat, chiedendolo a Claude.

  Per una domanda circoscritta si possono convocare solo i ministri interessati.

- Quando scatta un'allerta nuova o un dato cambia in modo rilevante.
- Quando un suggerimento approvato riguarda più ministeri.
- In ogni caso il lunedì, per la seduta ordinaria.

## Verifica continua e riesame

Le decisioni non valgono per sempre: ogni giorno il sistema verifica, con un controllo **deterministico e ripetibile** (`consiglio.py --verifica`), che ogni seduta ancora valida regga sui dati di oggi:
- gli indicatori sono cambiati oltre la soglia fissata (`governo_soglia_riesame` in `sistema/config.yaml`, oggi il 15%)?
- ci sono allerte nuove o rientrate?
- sono cambiate le regole (Carta, rubrica, motore, regolamento, ruoli), secondo la catena di integrità?
- il programma in vigore viola una linea rossa o non è più finanziabile senza deficit?
- ci sono obblighi UE critici nuovi per le aree della seduta?
- la seduta ha superato l'età massima (`governo_riesame_giorni`, oggi 90 giorni)?

Se una risposta è sì, la seduta è **da riesaminare** e il sistema scrive da solo la richiesta di riesame, una alla volta. Si può anche chiedere un riesame in qualsiasi momento: dal sito, con un file in `governo/richieste/`, o in chat.

Il **riesame** rifà la stessa seduta: stessa domanda, stessi ministri ed esperti, stesse regole, dati di oggi. Ogni ruolo parte dalla propria posizione di allora e dichiara cosa cambia e perché. Il verbale del riesame contiene il **confronto** con la seduta precedente: decisioni confermate, decisioni cambiate, riserva al deficit, e se nel frattempo sono cambiate le regole.

La parte deterministica (Ragioneria, linee rosse, conformità, verifica) dà sempre lo stesso risultato sugli stessi dati. Il giudizio degli agenti può variare: per questo ogni cambiamento va motivato e resta scritto nel confronto.

## Cosa resta umano

Il Consiglio consiglia. Le scelte politiche vere, cioè i pesi dei valori, l'approvazione dei suggerimenti e ogni pubblicazione verso l'esterno, restano alle persone.
