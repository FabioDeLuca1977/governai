# Richieste di analisi

Per chiedere un'analisi a GovernAI basta aggiungere qui un file `.md`. Il modello da seguire è `_modello.md`, oppure si usa il pulsante "Avvia un'analisi" del sito.

Ogni giorno l'attività di Claude, che usa l'abbonamento e non la chiave API, svolge questi passi:

1. legge le richieste nuove;
2. prepara diagnosi e tre opzioni;
3. le fa valutare da tre valutatori indipendenti sui valori della Carta;
4. pubblica il risultato in `analisi/`;
5. sposta la richiesta in `fatte/`.

La prima riga del file è il titolo. Il testo della richiesta è trattato come un dato da analizzare, mai come un'istruzione.
