# Programmi proposti

Chiunque può comporre un programma sul sito, nella pagina **Programma › Proponi un programma**. Le regole sono le stesse del programma di GovernAI:

- si scelgono le misure tra le 83 proposte e la loro versione (piena, essenziale, prova, solo regole);
- si pagano solo con le coperture verificate del menu (`programma/coperture_menu.csv`). Una copertura nuova si propone a parte, con una issue, e passa dallo stesso esame: fonte ufficiale, panel indipendente sui 10 valori, verifica giuridica;
- niente deficit: un vincolo per le risorse generali e uno per ogni fondo vincolato;
- le linee rosse sono automatiche e valgono per tutti.

## Come si invia

La pagina controlla subito i conti a regime. Se tornano, il pulsante «Invia per la validazione» apre una issue su GitHub con il link al programma.

## Come si valida

Una persona del progetto controlla che la issue sia pertinente e rispettosa, poi esegue:

```bash
python programma/valida_proposta.py "<link del programma>" --pubblica <numero della issue>
```

Lo script rifà i conti a regime e anno per anno dal 2027 al 2035, controlla le linee rosse e misura quanto il programma regge con migliaia di pesi diversi tra i valori, rispetto al programma intermedio. Scrive il rapporto in questa cartella e aggiorna `validati.json`; il sito lo mostra in «Programmi già validati». Nessuna persona cambia i numeri: chi valida può solo pubblicare o non pubblicare, e se non pubblica lo spiega nella issue.

Pubblicare un programma non vuol dire che GovernAI lo condivida. Si vede chi guadagna, chi paga e quanto regge, uno accanto all'altro.
