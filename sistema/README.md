# GovernAI — Sistema dinamico

Un unico sistema in Python tiene il programma agganciato alla realtà. Rileva quando le fonti ufficiali pubblicano dati nuovi e li scarica. Poi ricalcola indicatori e programma, legge con l'AI i documenti nuovi e propone le opzioni sostenibili adatte al momento.

Per farlo partire basta un comando, lanciato ogni giorno dall'Utilità di pianificazione di Windows. Non serve tenere aperta nessuna app.

## Come funziona

```
pipeline.py
 ├─ 1. sentinella.py      rileva gli aggiornamenti e scarica solo ciò che è cambiato
 ├─ 2. indicatori         cruscotto di 14 indicatori, con storico
 ├─ 3. allerte            8 regole (inflazione, spread, debito, PIL, ...)
 ├─ 4. ricalcolo          registro delle coperture → motore dei valori → programma del momento
 ├─ 5. bollettino         sistema/bollettini/AAAA-MM-GG.md
 └─ 6. revisione_ai.py    livello AI con l'API di Claude:
                            - legge i documenti ufficiali nuovi e propone modifiche verificabili
                            - applica solo quelle che superano le salvaguardie
                            - scrive la "Nota del livello AI" con le opzioni del momento
```

**Quando interviene il livello AI.** Interviene quando la sentinella trova documenti nuovi o quando scatta una nuova allerta. In ogni caso interviene una volta a settimana, il lunedì, per la nota del momento.

## Salvaguardie del livello AI

L'AI non scrive liberamente nei file. Restituisce proposte strutturate (file, riga, campo, valore attuale, valore nuovo, citazione), e Python le applica solo se superano questi controlli:

1. **Campi ammessi.** Si possono modificare solo le capienze dei fondi (`registro/fondi.csv`) e i gettiti delle coperture (`programma/coperture_menu.csv`). Carta dei valori e punteggi del panel non si toccano.
2. **Valore attuale.** Il valore attuale dichiarato deve coincidere con quello nel file, così si evitano modifiche basate su dati vecchi.
3. **Citazione verificata.** La citazione deve comparire davvero nel testo del documento ufficiale. Una cifra senza fonte viene scartata.
4. **Variazioni grandi.** Oltre il 25% di variazione, la modifica resta in attesa di approvazione umana. La soglia si regola in `config.yaml`.
5. **Tracciabilità.** Ogni modifica, applicata o in attesa, è registrata in `stato/modifiche_ai.csv` con fonte e citazione. Prima di ogni modifica si salva una copia del file in `dati/storico/_input/`.

Il testo dei documenti è trattato come dato, mai come istruzione. Il modello usato è Claude Opus 5.5. In caso di rifiuto, l'API ripiega automaticamente su un altro modello.

## Configurazione

### Credenziali dell'API di Claude (una sola volta)

La chiave si crea su console.anthropic.com. Poi va salvata come variabile d'ambiente dell'utente Windows con questo comando in PowerShell:

```powershell
[Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "la-tua-chiave", "User")
```

Senza chiave, il sistema funziona lo stesso: il bollettino segnala solo che il livello AI non è stato eseguito.

### Parametri

Si impostano in `config.yaml`:

| Parametro | Cosa regola |
|---|---|
| `indicatori` | Il cruscotto |
| `regole` | Allerte, misure da privilegiare e da sospendere |
| `pagine` | Le pagine ufficiali osservate |
| `ai_attivo` | Accende o spegne il livello AI |
| `ai_modifiche` | `applica` oppure `proponi`; con `proponi` tutto resta in attesa di approvazione |
| `ai_soglia_modifica_automatica` | La soglia oltre cui una modifica resta in attesa |
| `ai_giorno_nota_settimanale` | Il giorno della nota settimanale |

## Uso manuale

Dalla cartella `sistema`:

```bash
python pipeline.py
```

| Opzione | Effetto |
|---|---|
| `--completo` | Rilancia tutti gli script di download |
| `--senza-download` | Usa i dati già presenti |
| `--ricalcola` | Ricalcola i modelli anche senza dati nuovi |
| `--senza-ai` | Salta il livello AI |

Per il solo livello AI:

```bash
python revisione_ai.py
```

| Opzione | Effetto |
|---|---|
| `--proponi` | Non applica nulla: tutte le modifiche restano in attesa |
| `--solo-nota` | Scrive solo la nota, senza leggere i documenti |
| `--prova` | Non chiama l'API |

## Esecuzione automatica

I compiti sono divisi così, per non pagare due volte l'API e non creare conflitti:

| Dove | Quando | Cosa fa | Costo |
|---|---|---|---|
| **GitHub Actions** (`.github/workflows/aggiorna.yml`) | Ogni giorno alle 6:00 UTC | Pipeline completa: dati, programma, livello AI, interfaccia, salvataggio nel repository | Gratuito entro i 2.000 minuti al mese dei repository privati (circa 5–10 minuti al giorno); l'API di Claude si paga una sola volta |
| **Computer locale** (attività Windows "GovernAI - pipeline giornaliera") | Ogni giorno alle 9:00 | `avvia_pipeline.cmd` → `sincronizza.py --ripiego`: scarica da GitHub i risultati. **Ripiego:** GitHub non garantisce l'orario delle esecuzioni programmate e a volte le salta; se manca il bollettino del giorno, la pipeline gira in locale e carica i risultati su GitHub | Nullo |

**Prima di scaricare.** Se in locale ci sono output generati, la sincronizzazione li accantona con `git stash` e li tiene recuperabili, conservando gli ultimi 7. Le modifiche ai file sorgente restano al loro posto.

**Pipeline completa in locale.** Per rieseguirla a mano, ad esempio per riscaricare un documento da un sito che blocca GitHub:

```bash
python pipeline.py --completo
```

Il registro delle esecuzioni locali è in `stato/pipeline.log`.

## File

| File | Contenuto |
|---|---|
| `config.yaml` | Indicatori, allerte, pagine osservate, parametri |
| `sentinella.py` | Rilevamento aggiornamenti e download mirato |
| `pipeline.py` | Orchestrazione, cruscotto, programma del momento, bollettino |
| `revisione_ai.py` | Livello AI con salvaguardie |
| `revisione_ai.md` | Istruzioni equivalenti per una revisione manuale con Claude |
| `stato/` | Memoria tra le esecuzioni: firme delle fonti, indicatori, allerte, compiti, modifiche AI |
| `bollettini/` | Bollettini datati; `ultimo.md` è sempre il più recente |

## Limiti

- **Pagine osservate.** Le home page segnalano anche novità non pertinenti. Il livello AI le valuta e le scarta.
- **Documenti non testuali.** Excel e archivi non vengono letti dal livello AI: li aggiornano gli script di area.
- **Documenti lunghissimi.** Oltre circa 1,5 milioni di caratteri il documento non viene troncato: viene segnalato per una lettura a mano.
- **Costi delle chiamate all'API.** Hanno un costo. Una revisione tipica, cioè qualche documento più la nota, costa nell'ordine di qualche decina di centesimi, a seconda della lunghezza dei documenti.
