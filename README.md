# GovernAI

**Un programma di governo né di destra né di sinistra, guidato da valori dichiarati, costruito sui dati ufficiali e finanziato senza deficit.**

GovernAI è un prototipo di ricerca. Un sistema di agenti AI fa da consigliere al governo: analizza i dati, propone opzioni, ne calcola costi e coperture e rende espliciti i compromessi. **Le decisioni restano alle persone**, come vogliono la Costituzione e l'AI Act europeo.

L'interfaccia web pubblicata in `docs/` contiene:
- un cruscotto degli indicatori;
- il programma con le schede pronte;
- un simulatore dei pesi tra i valori;
- le coperture;
- i bollettini quotidiani.

## Cosa contiene

| Cartella / file | Contenuto |
|---|---|
| `00_metodo.md` | Metodo comune degli agenti ministeriali |
| `01_carta_valori.md` | Carta dei 10 valori: Rispetto e diversità, Fiducia e trasparenza, Innovazione, Benessere, Apprendimento e cultura, Bellezza patrimonio e accoglienza, Responsabilità verso il futuro, Equità, Sicurezza senza controllo assoluto, Cittadinanza responsabile |
| `ministeri/` | 9 dossier ministeriali e 75 proposte |
| `dati/` | Base dati ufficiale: script di download (Eurostat, ISTAT, MEF, …), serie, verifiche di 334 cifre su fonte primaria, storico |
| `registro/` | Registro unico delle coperture e vincolo di bilancio |
| `motore/` | Panel di 3 valutatori indipendenti e analisi di robustezza ai valori (SMAA) |
| `programma/` | 152 varianti, 59 misure di copertura, ottimizzatore senza deficit, schede pronte (articolato normativo, cronoprogramma, indicatori) |
| `20_programma_governai.md` | Il programma completo: versioni base, completa e intermedia, tutte senza deficit, verificate giuridicamente |
| `21_idee_in_sintesi.md` | Le idee in dieci minuti |
| `22_programma_in_una_pagina.md` | Il programma in una pagina: perché, come, cosa misuriamo, chi ne beneficia (generato da `programma/schema.yaml`) |
| `governo/` | Il Consiglio dei ministri ombra: regolamento, ruoli (9 ministri, opposizione leale, capo di governo), sedute, verbali, previsioni e credibilità |
| `benchmark/` | Confronto con i Paesi che funzionano meglio e con i programmi del governo e dei partiti italiani (`confronto_programmi.md`, rapporti in `programmi/`) |
| `trasparenza/` | Indicatori di rischio negli appalti pubblici (dati ANAC); il rapporto pubblico è aggregato, gli elenchi nominativi restano riservati |
| `europa/` | Monitoraggio quotidiano dell'Unione europea: atti della Gazzetta UE, obblighi di recepimento in scadenza, infrazioni contro l'Italia, Semestre europeo |
| `costituzione/` | Controllo di costituzionalità di leggi, emendamenti e manovre: screening automatico, giurisprudenza verificata della Corte, esami approfonditi (manovra 2027, misure GovernAI) |
| `legislazione/` | Archivio quotidiano della Gazzetta Ufficiale, ricerca negli atti e verifica della redazione di leggi ed emendamenti |
| `apprendimento/` | Obiettivi misurabili, registro delle decisioni, esiti e calibrazione: il modello impara da successi e insuccessi |
| `integrita/` | Catena di impronte crittografiche (stile blockchain) che rende visibile ogni manomissione |
| `giuridico/` | Verifica di conformità fiscale, costituzionale ed europea di ogni misura e copertura; le incompatibilità sono linee rosse automatiche |
| `analisi/` | Analisi su richiesta, avviate da una issue GitHub con l'etichetta "analisi" |
| `sistema/` | Sistema dinamico: sentinella delle fonti ufficiali, cruscotto, allerte, programma del momento, livello AI, bollettini; `sincronizza.py` allinea la copia locale a GitHub |
| `docs/` | Interfaccia web statica, pronta per GitHub Pages |

## Avvio rapido

```bash
pip install -r requirements.txt
cd sistema
python pipeline.py
```

La pipeline svolge questi passi:
- scarica i dati ufficiali cambiati;
- ricalcola indicatori, allerte e programma del momento;
- scrive il bollettino in `sistema/bollettini/`;
- aggiorna l'interfaccia in `docs/data.js`.

Per vedere l'interfaccia basta aprire `docs/index.html` nel browser.

Il **livello AI**, cioè la lettura dei documenti nuovi e la nota del momento, usa l'API di Claude e richiede la variabile d'ambiente `ANTHROPIC_API_KEY`. Senza chiave, tutto il resto funziona lo stesso. I dettagli sono in [`sistema/README.md`](sistema/README.md).

## Pubblicazione su GitHub

1. **GitHub Pages.** In *Settings → Pages* scegli *Deploy from a branch*, ramo `main`, cartella `/docs`. L'interfaccia sarà online all'indirizzo `https://<utente>.github.io/<repository>/`.
2. **Aggiornamento automatico.** Il workflow [`.github/workflows/aggiorna.yml`](.github/workflows/aggiorna.yml) esegue la pipeline ogni giorno e salva dati, bollettino e interfaccia nel repository. Si può avviare anche a mano dalla scheda *Actions*.
3. **Livello AI su GitHub.** In *Settings → Secrets and variables → Actions* aggiungi il secret `ANTHROPIC_API_KEY`. **Non inserire mai la chiave nei file del repository.**

I documenti grezzi scaricati (`dati/raw/`, oltre 100 MB) non vengono salvati nel repository: li riscaricano gli script.

## Principi

- **Prima i vincoli, poi i valori.** Costituzione e vincolo di bilancio non si pesano: si rispettano.
- **Nessun peso unico.** Le proposte si classificano per robustezza, provando tutte le combinazioni di pesi tra i valori:
  - *robuste*: prioritarie con ogni combinazione;
  - *dipendenti dai valori*: la scelta è politica e va a cittadini e Parlamento.
- **Dati verificabili.** Ogni cifra rimanda a una serie o a un documento ufficiale. Le stime di costo sono etichettate "stima GovernAI" e non sono quantificazioni della Ragioneria.
- **Trasparenza dell'AI.** Le modifiche del livello AI passano salvaguardie automatiche: citazione verificata nel documento, soglie, registro delle modifiche.

## Limiti

GovernAI è un prototipo:
- i costi sono stime da validare con UPB e Ragioneria;
- le analisi distributive richiedono microdati ad accesso istituzionale;
- i punteggi del panel sono giudizi esperti strutturati, non misure.

Prima di qualunque uso pubblico serve una revisione critica da prospettive politiche diverse (red team).

## Licenza

- **Codice:** MIT (vedi [`LICENSE`](LICENSE)).
- **Contenuti:** Carta dei valori, dossier, schede, analisi e bollettini sono distribuiti con [CC BY 4.0](LICENSE-CONTENUTI.md): si possono riusare liberamente citando GovernAI.
- **Dati:** restano soggetti alle condizioni delle fonti ufficiali.

GovernAI è un prototipo a scopo sociale. Contributi, critiche e richieste di analisi sono benvenuti.
