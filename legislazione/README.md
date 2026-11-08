# Legislazione: archivio della Gazzetta Ufficiale e assistente redazionale

Questa cartella serve a tre cose:

1. **Conoscere** la legislazione pubblicata in Gazzetta Ufficiale: un archivio locale che cresce ogni giorno.
2. **Capire** come si scrivono i testi normativi: le regole ufficiali di tecnica legislativa, con le fonti.
3. **Aiutare** chi propone leggi o emendamenti a scriverli bene: un controllo automatico e una guida per la revisione con giudizio.

> **Il sistema non "memorizza" il diritto nei pesi del modello.** Un modello linguistico conosce le leggi solo fino alla data del suo addestramento, e in modo impreciso. GovernAI costruisce invece un **archivio consultabile**, aggiornato ogni giorno dalla fonte ufficiale. Gli agenti lo **interrogano** (`cerca.py`) e verificano ogni citazione su Normattiva prima di usarla. Quello che non è nell'archivio o su Normattiva non va dato per certo.

## File

| File | Cosa fa |
|---|---|
| `scarica_gu.py` | Archivio incrementale degli atti della GU, Serie generale (indice + testi) |
| `cerca.py` | Ricerca per parole, tipo e date; atti che citano una norma; ricerca di un atto per estremi |
| `verifica_testo.py` | Assistente redazionale deterministico: rapporto markdown con errori, avvisi e suggerimenti |
| `norme.py` | Libreria comune: riconoscimento delle citazioni, URN Normattiva, rete con pause |
| `regole_redazione.md` | Regole ufficiali di tecnica legislativa, con fonti verificate e checklist |
| `istruzioni_revisione.md` | Come Claude (nell'app, senza API) completa la revisione con giudizio |
| `archivio/` | `indice.csv`, `testi/AAAA/<codice>.txt`, `stato.json`, `cache_normattiva.json` |
| `prove/` | Rapporti di verifica sugli articolati delle 52 schede del programma |

## Uso

```bash
cd legislazione

# 1. archivio: la prima volta scarica gli ultimi 30 giorni, poi solo i fascicoli nuovi
python scarica_gu.py
python scarica_gu.py --giorni 90             # finestra iniziale più ampia
python scarica_gu.py --testi normativi       # testi solo di leggi, decreti e regolamenti (più veloce)
python scarica_gu.py --riprova-testi         # riprova i testi non ottenuti

# 2. ricerca
python cerca.py "caregiver familiare"
python cerca.py "spese fiscali" --tipo legge "decreto legislativo" --dal 2026-10-01
python cerca.py --cita "legge 23 agosto 1988, n. 400" --articolo 17
python cerca.py --atto "decreto-legge 6 novembre 2026, n. 200"

# 3. verifica di un testo
python verifica_testo.py mia_proposta.md -o prove/mia_proposta.md
python verifica_testo.py ../programma/schede/06_salute.md --scheda 06-C2 -o prove/06-C2.md
python verifica_testo.py bozza.md --senza-rete      # senza interrogare Normattiva
```

Da Python, per gli agenti:

```python
from cerca import cerca, citanti, trova_atto
cerca("salario minimo", tipi=["legge"], dal="2026-01-01")
citanti("legge 31 dicembre 2009, n. 196", articolo="17")
```

## Fonti scelte e perché

Le fonti sono state provate l'8 novembre 2026.

| Fonte | Uso | Affidabilità |
|---|---|---|
| **gazzettaufficiale.it**: archivio per anno (`/ricercaArchivioCompleto/serie_generale/AAAA`) e sommario di ogni fascicolo (`/gazzetta/serie_generale/caricaDettaglio?...`) | Elenco **completo** degli atti, compresi i supplementi ordinari: rubrica, emettitore, intestazione, titolo, pagina, codice redazionale | Alta: è la fonte ufficiale. L'HTML è stabile da anni, ma non è un'API: un cambio di impaginazione richiede di aggiornare le espressioni regolari di `leggi_sommario()` |
| **gazzettaufficiale.it**: pagine dell'atto, testo originario articolo per articolo | Testo integrale come pubblicato, data di entrata in vigore | Alta per gli atti normativi. Il sito richiede una sessione (si apre prima la pagina dell'atto) e serve una richiesta per ogni articolo o allegato |
| **Normattiva, API open data** (`api.normattiva.it/.../ricerca/avanzata`, la stessa usata da dati.normattiva.it) | Controllo incrociato degli atti normativi numerati; recupero di quelli assenti dai sommari | Buona, ma l'API non è documentata pubblicamente e una richiesta GET di prova è stata bloccata dal firewall (HTTP 409). La ricerca POST funziona |
| **Normattiva, risolutore URN** (`normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2009-12-31;196`; accetta anche il solo anno) | Verifica che un atto citato esista e recupero della sua intestazione ufficiale (data esatta) | Alta. Un URN errato restituisce la pagina «Normattiva - Errore» |
| **Feed RSS** della GU (`/rss/SG`) | Scartato | Contiene solo l'ultimo fascicolo: se un giorno l'esecuzione salta, si perdono atti |
| **ELI** della GU (`/eli/id/AAAA/MM/GG/<codice>/sg`) | Identificatore stabile salvato nell'indice | Alta |

Comportamento verso i siti:
- User-Agent dichiarato (`GovernAI-legislazione/0.1 …`);
- almeno 1 secondo tra due richieste (`--pausa`, minimo 0,5);
- tre tentativi con attesa crescente sugli errori 429/5xx;
- nessun download parallelo;
- l'aggiornamento giornaliero richiede circa 60-80 richieste (2-3 minuti).

### Contenuto dell'indice (`archivio/indice.csv`)

`codice` (codice redazionale, chiave), `data_gu`, `numero_gu`, `supplemento`, `rubrica`, `emettitore`, `tipo` (legge, decreto-legge, decreto legislativo, DPR, DPCM, DM, delibera CdM, delibera, determina, ordinanza, comunicato, testo coordinato, …), `intestazione`, `data_atto`, `numero_atto`, `titolo`, `pagina`, `url_gu`, `eli_gu`, `url_normattiva` (URN per leggi, decreti-legge, d.lgs. e DPR; pagina per codice redazionale per gli altri atti normativi), `entrata_in_vigore`, `testo` (percorso), `testo_stato` (ok, parziale, assente, errore, da_scaricare), `caratteri`, `fonte`, `scaricato`.

### Stato dell'archivio

Prima esecuzione dell'8/11/2026, finestra 9 ottobre – 8 novembre 2026:
- **26 fascicoli e 576 atti**, di cui 21 nella rubrica «Leggi ed altri atti normativi»: 9 decreti legislativi, 7 leggi, 4 decreti-legge e 1 regolamento ministeriale, più 7 DPR;
- per tipo: 331 comunicati, 137 decreti ministeriali, 48 determine;
- il controllo incrociato con Normattiva ha trovato tutti gli atti normativi numerati già presenti nei sommari, nessuno mancante;
- **testo integrale per tutti i 576 atti** (7 MB): circa 2.800 richieste in circa 75 minuti. Un secondo passaggio con `--riprova-testi` ha recuperato i 2 testi falliti per errore di connessione;
- un aggiornamento senza fascicoli nuovi richiede 2 richieste.

## Limiti

- **Testo originario, non vigente.** L'archivio conserva gli atti come pubblicati. Per sapere com'è una norma oggi dopo le modifiche serve Normattiva (versione vigente), a cui rimandano i link `url_normattiva`.
- **Solo Serie generale.** Non sono archiviate le serie speciali: Corte costituzionale, UE, Regioni, concorsi, contratti.
- **Allegati e tabelle.** Il testo arriva dall'HTML della GU: le tabelle sono in testo semplice e gli allegati grafici mancano. Oltre 400 articoli o allegati il testo è marcato `parziale`; il PDF ufficiale resta la fonte certa.
- **Ritmo di download.** Il primo scaricamento completo (circa 600 atti) richiede circa un'ora con la pausa di 1 secondo. L'aggiornamento giornaliero richiede pochi minuti.
- **Dipendenza dall'HTML.** Né gazzettaufficiale.it né l'API di Normattiva hanno un contratto pubblico di stabilità. Se cambiano, lo script registra l'errore in `stato.json` e la pipeline continua.
- **Siti che bloccano server esteri.** Come per altre fonti (vedi `dati/script/fonti.py`), i siti istituzionali potrebbero rifiutare le richieste dai server di GitHub Actions. In quel caso conviene aggiornare l'archivio dalla copia locale (`sistema/sincronizza.py`).
- **Il controllo automatico non è un giurista.**
  - Riconosce le citazioni di atti statali con regole fisse: leggi, decreti-legge, d.lgs., DPR, regi decreti, nelle forme completa e breve.
  - Gli atti UE sono solo elencati: non vengono verificati.
  - Non controlla che l'articolo o il comma citato esista né che le parole da sostituire ci siano davvero.
  - Può dare falsi positivi, ad esempio una sigla definita altrove o un termine la cui decorrenza è nella frase prima.
  - Il giudizio sui valori, sulle linee rosse e sul quadro giuridico spetta alla revisione guidata da `istruzioni_revisione.md` e, alla fine, agli uffici legislativi.
- **Peso nel repository.** I testi occupano circa 7 MB al mese. Si può versionare solo `indice.csv` e lasciare `archivio/testi/` fuori dal repository, rigenerabile con `--dal`.

## Prova sulle schede del programma

`verifica_testo.py` è stato eseguito sull'«Articolato normativo essenziale» di **tutte le 52 schede** in `programma/schede/`. I rapporti sono in `prove/<id>.md`. In totale il controllo ha prodotto 108 errori, 245 avvisi e 101 suggerimenti.

### Le tre schede richieste

| Scheda | Esito | Rilievi principali |
|---|---|---|
| **01-P2** Spese fiscali a scadenza | 0 errori, 7 avvisi, 3 suggerimenti | Copertura (art. 5): l'onere di 5 e 10 milioni convive con la frase «non derivano nuovi o maggiori oneri», senza raccordo («Fatto salvo quanto previsto dal comma 1 …»). La «riduzione delle spese di funzionamento del MEF» non indica l'autorizzazione di spesa ridotta e l'onere non è qualificato come limite di spesa. Nella delega mancano la decorrenza del termine («entro dodici mesi» da quando?), i pareri parlamentari e la disciplina degli oneri dei decreti (art. 17, c. 2, L. 196/2009). L'art. 3 modifica la Commissione spese fiscali in modo non testuale («è integrata da»). La L. 196/2009 è citata correttamente ed esiste. |
| **06-C2** Infermieri e medicina generale | 4 errori, 9 avvisi, 2 suggerimenti | Varianti nel testo («[PIENA]» all'art. 5 e «[PIENA: 600, 1.200 …]» nella copertura). Importi abbreviati («400 mln»). Commi non numerati in 4 articoli su 6. L'art. 4 delega il Governo senza principi e criteri direttivi, senza pareri e senza decorrenza del termine. Il decreto sulla soglia di carenza (art. 3) non ha termine. Sigla SSN non definita. La copertura si basa su «maggiori entrate derivanti dalla rimodulazione» di agevolazioni che il testo non dispone e non quantifica. Nessun riferimento normativo: il testo non dice quali leggi modifica, per esempio la disciplina della formazione in medicina generale. |
| **08-P1** Consulenza algoritmica pubblica | 5 errori, 8 avvisi, 3 suggerimenti | Elenchi con trattini negli artt. 2, 4, 5, 9 e 10: vanno trasformati in lettere a), b) …. Copertura in parte «nell'ambito dei bilanci interni delle Camere», che la legge non può disporre (art. 64 Cost.). Decreto MEF con «entro sessanta giorni» senza decorrenza. «Entro cinque giorni» senza decorrenza (art. 5). Rinvio «in quanto compatibili» alla L. 243/2012. Sigla UPB non definita. Le 6 citazioni di 5 atti statali (L. 132/2025, L. 243/2012, d.lgs. 82/2005, L. 246/2005, d.lgs. 179/2026) sono complete ed esistono su Normattiva. |

### Errori più frequenti (su 52 schede)

1. **Coperture finanziarie scritte in modo non conforme all'art. 17 L. 196/2009.**
   - In 47 schede l'onere non è qualificato come limite di spesa o come previsione di spesa.
   - In 41 schede gli importi sono abbreviati («mln», «mld») o senza «di euro».
   - In 8 schede gli oneri non sono quantificati per anno.
   - In 8 schede la copertura usa entrate di misure non scritte nel testo.
   - In 5 schede c'è una clausola di invarianza contraddittoria.
   - In 2 schede la copertura grava sui bilanci delle Camere.
2. **Varianti e segnaposto dentro l'articolato** in 25 schede: «[PIENA: …; ESSENZIALE: …]», «allegato X», «allegato Y». Un testo normativo ha una sola versione: serve un articolato per variante.
3. **Struttura non conforme.**
   - In 30 schede i commi non sono numerati.
   - In 12 schede ci sono elenchi con trattini al posto delle lettere a), b).
   - In 44 schede compaiono sigle non definite: SSN, PNRR, UPB, ISEE, MEF-RGS.

Altri rilievi ricorrenti:
- **Termini senza decorrenza** («entro dodici mesi»): 20 schede.
- **Decreti attuativi senza termine**: 20 schede.
- **Nessuna clausola di entrata in vigore o decorrenza**: 51 schede su 52. È ammesso, ma per le misure fiscali e di spesa conviene una data certa.
- **Prima citazione in forma abbreviata** («d.lgs. 23/2011», «DPR 115/2002»): 9 schede.
- **Novelle senza testo tra virgolette** o modifiche non testuali: 07-C5 scrive «All'articolo 13 del DPR 115/2002 è aggiunto un comma: …».
- **Deleghe senza principi e criteri direttivi**: 3 schede, tra cui 06-C2.

**Riferimenti verificati.** Le 60 citazioni di atti statali trovate nelle schede corrispondono tutte ad atti esistenti su Normattiva, con date esatte. Gli errori riguardano la **forma** dell'articolato, non gli estremi delle leggi citate.

Le schede sono «articolati essenziali», cioè schemi di principio e non testi pronti per il deposito: molti rilievi sono attesi. Prima di presentare una proposta servono un articolato per variante, la copertura nella forma dell'art. 17 e la revisione con `istruzioni_revisione.md`.

## Integrazione nella pipeline (da fare a cura del manutentore)

Nessun file fuori da `legislazione/` è stato modificato. Per aggiornare l'archivio ogni giorno, in `sistema/pipeline.py`, nella funzione `main()`, aggiungere dopo il passo «3c. verifica giuridica» e prima di «# 4. ricalcolo»:

```python
    # 3d. legislazione: archivio incrementale della Gazzetta Ufficiale (solo i fascicoli nuovi)
    if not a.senza_download:
        ok, msg = esegui(["scarica_gu.py"], RADICE / "legislazione", timeout=3600)
        log.append(f"legislazione: {msg}" if ok else f"ERRORE legislazione: {msg}")
```

Comando equivalente da riga di comando: `python legislazione/scarica_gu.py`, eseguito dalla radice del repository o da qualsiasi cartella, perché i percorsi sono assoluti.

L'ultima riga stampata dallo script, ad esempio `archivio GU: 600 atti, 590 con testo; nuovi 24; …`, finisce nel registro tecnico del bollettino.
