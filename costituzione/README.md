# Costituzione: controllo di costituzionalità di leggi, emendamenti e manovre

Questa cartella fa per GovernAI il lavoro di un costituzionalista, in due tempi:

1. **Screening automatico** (`controllo.py`). Cerca nel testo i segnali di rischio per 11 parametri costituzionali e li ordina per livello: alto, medio, basso. È deterministico, veloce e ripetibile. Gira da solo sugli atti nuovi della Gazzetta.
2. **Esame approfondito** (`istruzioni_costituzionalista.md`). Un agente costituzionalista legge lo screening e il testo integrale, verifica la giurisprudenza e classifica ogni rilievo in tre esiti: *illegittimità probabile*, *dubbio serio*, *rischio basso*. Per ogni rilievo propone una riformulazione conforme.

Vale per le leggi del Governo e per le proposte di GovernAI, **con lo stesso rigore**. Si valuta la conformità alla Costituzione, non l'opportunità politica. È un supporto alla decisione, non un parere legale.

## File

| File | Cosa fa |
|---|---|
| `parametri.yaml` | 11 parametri. Per ciascuno: articoli, principio, giurisprudenza essenziale con sintesi, segnali testuali (regex), domande di controllo |
| `controllo.py` | Screening di un file .txt, .md o .pdf, di una scheda del programma (`--scheda`) o degli atti nuovi della Gazzetta (`--gu`). Scrive `esami/<nome>.md` e `.json` |
| `giurisprudenza.py` | Scarica i dati aperti della Corte, verifica le pronunce citate (`--verifica`, `--verifica-parametri`) e cerca nel testo delle pronunce (`--cerca`) |
| `giurisprudenza_verificata.json` | Esito della verifica: per ogni pronuncia citata, ECLI, date, oggetto e dispositivo in breve, link |
| `istruzioni_costituzionalista.md` | Metodo dell'esame approfondito. Lo usano anche il Consiglio dei ministri e la revisione dei testi |
| `testi/AC3174_articolato.txt` | Articolato del DDL di bilancio 2027-2029 (A.C. 3174, Tomo II), convertito dall'HTML della Camera |
| `esami/` | Rapporti: screening (`*_screening.md`), esami approfonditi, `governai/` (una scheda per misura adottata), `gu/` (atti della Gazzetta e `stato.json`) |
| `cache/` | Archivi JSON dei dati aperti della Corte (non versionati, vedi `.gitignore`) |

## Uso

```bash
cd costituzione
python giurisprudenza.py --scarica                    # la prima volta (circa 105 MB); poi una volta a settimana con --forza
python giurisprudenza.py --verifica-parametri         # verifica tutte le pronunce di parametri.yaml
python giurisprudenza.py --verifica 10/2015 182/2026
python giurisprudenza.py --cerca "livelli essenziali" "intesa" --dal 2024 --tipo S

python controllo.py testi/AC3174_articolato.txt --articoli 1-137 --data 2027-01-01 --nome AC3174_screening
python controllo.py ../programma/schede/01_economia.md --scheda 01-P2 --data 2027-01-01
python controllo.py emendamento.pdf --nome em_5_12
python controllo.py --gu                              # atti con forza di legge nuovi in legislazione/archivio
```

L'opzione `--data` è la data di riferimento per la retroattività: di solito l'entrata in vigore prevista. Se manca vale la data di oggi. Con `--gu` si usa l'entrata in vigore indicata nell'indice della Gazzetta.

## Parametri

| Parametro | Articoli | Pronunce |
|---|---|---|
| `bilancio` | 81, 97, 119; L. 243/2012; L. 196/2009 | 1/1966, 70/2012, 26/2013, 88/2014, 184/2016, 18/2019, 4/2020, 10/2015, ord. 17/2019 |
| `tributi` | 53, 3, 23, 41; L. 212/2000 | 10/2015, 111/2024, 180/2025, 135/2026, 223/2012, 116/2013, 262/2020, 140/2024 |
| `regioni` | 117, 118, 119, 120, 5 | 370/2003, 423/2004, 222/2005, 251/2016, 137/2018, 220/2021, 223/2023, 192/2024, 195/2024, 152/2025, 182/2026, 425/2004, 33/2019 |
| `diritti_sociali` | 32, 34, 38, 36, 2, 3 | 80/2010, 275/2016, 169/2017, 62/2020, 152/2020, 70/2015, 250/2017, 234/2020, 19/2025, 52/2026, 178/2015, 31/2025 |
| `decreti_legge` | 77, 72; L. 400/1988 art. 15 | 29/1995, 360/1996, 171/2007, 128/2008, 22/2012, 220/2013, 32/2014, 247/2019 |
| `procedimento_deleghe` | 70, 72, 76, 64, 81 c. 6 | 340/2007, 280/2004, 251/2016, 192/2024, ord. 17/2019, ord. 60/2020, 129/1981, 120/2014 |
| `ue_internazionale` | 11, 117 c. 1; TFUE 107-108; CEDU | 170/1984, 348/2007, 349/2007, 311/2009, 269/2017, ord. 21/2025 |
| `giustizia` | 24, 25, 111, 113 | 364/1988, 393/2006, 236/2011, 32/2020, 170/2013, 78/2012, 137/2026 |
| `pubblica_amministrazione` | 97, 98, 51 | 103/2007, 104/2007, 293/2009, 37/2015, 108/2016 |
| `affidamento_retroattivita` | 3, 2, 41, 117 c. 1; L. 212/2000 | 349/1985, 822/1988, 525/2000, 264/2005, 236/2009, 16/2017, 108/2016, 170/2013, 140/2024 |
| `referendum` | 75 | 16/1978, 2/1994, 6/2015 |

**81 pronunce distinte, tutte verificate** sui dati aperti della Corte. Per ognuna sono stati controllati:
- esistenza;
- tipo (sentenza o ordinanza);
- presenza nel testo delle parole che caratterizzano la sintesi.

Altre 6 pronunce sono citate negli esami e verificate con `--verifica`: 139/2024, 114/2025, 28/2025, 184/2025, 20/2019, 21/2025.

## Fonti e perché

Le fonti sono state provate l'8 novembre 2026.

| Fonte | Uso | Note |
|---|---|---|
| **dati.cortecostituzionale.it** («Scarica i dati», archivio delle pronunce in JSON, licenza CC BY-SA 3.0) | Verifica dei numeri, oggetto, dispositivo e motivazione; ricerca per parole | Fonte ufficiale della Corte, aggiornata ogni settimana. L'archivio scaricato arriva alla pronuncia 191/2026 (deposito del 6/11/2026). Tre file: 1956-1980, 1981-2000, 2001-oggi |
| **www.cortecostituzionale.it** | Link alla scheda della pronuncia (`url` nel file di verifica) | Il sito risponde alle richieste automatiche con un CAPTCHA (Radware): **non si aggira**. Si usano i dati aperti, che sono pubblicati dalla stessa Corte |
| **Normattiva** (risolutore URN, tramite `legislazione/norme.py`) | Esistenza e intestazione degli atti citati; testo vigente | Esempio: d.lgs. 147/2026, art. 33 (soppressione del Fondo TPL) |
| **camera.it / documenti.camera.it** | Testi dei disegni di legge, stralci, dossier, resoconti | A.C. 3174: Tomo II in HTML (articolato); Tomo I (relazioni) già in `dati/raw/` |
| **legislazione/archivio** (Gazzetta Ufficiale) | Atti con forza di legge nuovi, per lo screening `--gu` | Testo originario, non vigente |

## Metodo dello screening

Per ogni articolo e comma, `controllo.py`:
1. applica le espressioni regolari dei `segnali` di ciascun parametro;
2. applica regole combinate, che hanno bisogno di più segnali o di un confronto con la data di riferimento:
   - **prelievo settoriale**: codici ATECO o settore indicato, più un aumento di aliquota o un contributo → alto;
   - **regime settoriale**: deduzioni diverse per settore → medio;
   - **atto statale in materia regionale senza intesa** → medio; alto se ripartisce risorse;
   - **fondo soppresso o ridotto in materia regionale** → alto;
   - **delega** senza principi e criteri nell'articolo → alto; delega in una legge di bilancio → alto;
   - **decorrenza anteriore** alla data di riferimento → medio; alto se in materia tributaria;
   - **periodo d'imposta in corso** o già chiuso → medio o alto;
   - **obblighi riferiti ad annualità passate** (ripiani, versamenti, tetti) → alto;
   - **norma organizzatoria senza effetti finanziari** in una legge di bilancio → medio;
3. scarta i segnali di solo contesto (es. «materia regionale», «decreto del Ministro») e i duplicati. I segnali dei decreti-legge valgono solo se il testo è un decreto-legge;
4. sull'intero testo:
   - legge di bilancio: contenuto proprio e art. 75;
   - decreto-legge: omogeneità delle rubriche;
   - atti UE richiamati;
   - per i testi che non sono leggi di bilancio, i controlli di copertura e di attuazione di `legislazione/verifica_testo.py`.

Il livello di un articolo è il massimo dei suoi segnali. Il rapporto mostra per esteso i rilievi alti e medi (parametro, segnale, comma, estratto, giurisprudenza, domande) e in tabella quelli bassi.

## Prove reali (8 novembre 2026)

### A. Manovra 2027 (A.C. 3174)

- **Screening** su 137 articoli: 13 con segnali alti, 23 medi ([`esami/AC3174_screening.md`](esami/AC3174_screening.md)).
- **Esame approfondito** in [`esami/AC3174_manovra_2027.md`](esami/AC3174_manovra_2027.md): nessuna illegittimità probabile incondizionata, sei dubbi seri.
  1. **Art. 21**, IRAP +5/+3 punti sull'energia, con divieto di traslazione non verificabile (sent. 10/2015 e 111/2024).
  2. **Artt. 76 e 91**, spesa in disavanzo «tenuto conto» della clausola nazionale UE. Diventa illegittimità probabile se manca l'autorizzazione delle Camere a maggioranza assoluta (art. 81, secondo comma; art. 6 L. 243/2012). Gli oneri permanenti dal 2029 non hanno copertura ordinaria.
  3. **Art. 73**, payback dei dispositivi medici 2019-2023: concorso statale al 35% contro il 52% ritenuto proporzionato per il 2015-2018 (sent. 140/2024), tetti regionali fissati retroattivamente.
  4. **Art. 131**, LEP ASACOM e ATS a carico delle risorse già nei bilanci di regioni ed enti; testo non allineato alla sent. 182/2026 (intesa).
  5. **Fondo TPL**, soppresso dal d.lgs. 147/2026 e sostituito da una compartecipazione IRPEF da fissare con DPCM entro il 31/12/2026, senza clausola di continuità.
  6. **Art. 71**, riduzione del payback farmaceutico legata a investimenti in Italia (aiuti di Stato).

### B. Decisioni di GovernAI

Esame in [`esami/governai_conti_2027_2029.md`](esami/governai_conti_2027_2029.md), sulle 46 misure adottate il 8/11/2026. Screening per misura in `esami/governai/`. Tre dubbi seri:
- **01-P2 PIENA**: la scadenza automatica colpisce anche componenti strutturali dell'IRPEF; delega con criteri solo procedurali.
- **04-P3 PILOTA**: rivaluta un Fondo TPL che dal 2027 non esiste più. Un nuovo fondo vincolato in materia residuale senza il titolo dell'art. 119, quinto comma, sarebbe illegittimo.
- **Coperture certificate**: le «salite con atto ricognitivo» e le coperture che dipendono da un'altra legge vanno riscritte come limite massimo condizionato nella stessa legge (art. 81, terzo comma).

Rilievi minori:
- 09-C8 in legge di bilancio (stralcio);
- testo unico UPB a maggioranza assoluta;
- 02-C3, 06-C1, 03-P2 (silenzio-assenso paesaggistico).

### Gazzetta Ufficiale

`controllo.py --gu` sui 20 atti con forza di legge dell'archivio (9/10-8/11/2026), in circa 11 secondi. Un atto con segnali alti (d.lgs. 188/2026, art. 3), da esaminare.

## Limiti

- **Lo screening non è un giudizio.**
  - I segnali sono testuali. Falsi positivi tipici: la retroattività favorevole, le parole citate in rubriche altrui, la «riduzione» di oneri a favore delle imprese.
  - Falsi negativi tipici:
    - coperture condizionate;
    - fondi soppressi da altre leggi;
    - norme nella legge sbagliata;
    - sentenze o leggi recenti che cambiano il quadro.
  - Nelle prove reali i rischi più importanti di GovernAI sono emersi solo dall'esame approfondito.
- **Sintesi delle sentenze.** Sono nostre e brevi: prima di usarle in un parere si rilegge la motivazione. La verifica automatica controlla numero, tipo e parole chiave, non l'esattezza di ogni sfumatura.
- **Dati aperti.** Le ordinanze hanno la motivazione nel campo `epigrafe`. Alcuni caratteri accentati dei file più vecchi possono essere sostituiti. L'aggiornamento è settimanale: le pronunce degli ultimi giorni possono mancare.
- **Testi.** L'articolato della Camera è convertito da HTML: tabelle e allegati (es. l'allegato 2 con i codici ATECO) vanno letti nel PDF ufficiale. Per i PDF si usa pypdf, che può spezzare le righe.
- **Fatti da accertare.** Alcuni esiti dipendono da fatti non verificabili dal testo:
  - esito di votazioni a maggioranza assoluta;
  - adozione dei DPCM;
  - dati di redditività di un settore.
  Gli esami li indicano come condizioni.

## Integrazione (a cura del manutentore)

Nessun file fuori da `costituzione/` è stato modificato. Righe da aggiungere.

### `sistema/pipeline.py`

Nella funzione `main()`, subito dopo il blocco «3d. legislazione» e prima di «3e. governo ombra»:

```python
    # 3d-bis. costituzione: screening costituzionale degli atti con forza di legge nuovi della Gazzetta
    #         (leggi, decreti-legge, decreti legislativi in legislazione/archivio); il lunedi' aggiorna la giurisprudenza
    if (RADICE / "costituzione" / "controllo.py").exists():
        if not a.senza_download and date.today().weekday() == 0:
            ok, msg = esegui(["giurisprudenza.py", "--scarica", "--forza", "--verifica-parametri"],
                             RADICE / "costituzione", timeout=1800)
            log.append(f"giurisprudenza: {msg}" if ok else f"ERRORE giurisprudenza: {msg}")
        ok, msg = esegui(["controllo.py", "--gu"], RADICE / "costituzione", timeout=1800)
        log.append(msg if ok else f"ERRORE costituzione: {msg}")
```

(`date` è già importato in `pipeline.py`. Lo screening `--gu` non richiede la cache della Corte.) L'ultima riga stampata, ad esempio `costituzione: 3 atti con forza di legge esaminati; con segnali alti 1: …`, finisce nel registro del bollettino. Su GitHub Actions la cache non è versionata: il primo lunedì la scarica (circa 105 MB, meno di un minuto).

### `governo/esperti.yaml`

Aggiungere in fondo all'elenco `esperti:`:

```yaml
  - id: costituzionalista
    nome: Costituzionalista
    competenze: Legittimità costituzionale di leggi, emendamenti e manovre; copertura ed equilibrio di bilancio (artt. 81, 97), capacità contributiva (art. 53), riparto Stato-Regioni e LEP (artt. 117-120), diritti sociali, decreti-legge e deleghe (artt. 72, 76, 77), vincoli UE, affidamento e retroattività. Applica costituzione/istruzioni_costituzionalista.md e lo screening di costituzione/controllo.py; classifica ogni rilievo come illegittimità probabile, dubbio serio o rischio basso e propone la riformulazione. Non esprime preferenze politiche.
    fonti: [Corte costituzionale (dati aperti), Normattiva, Camera dei deputati, Senato della Repubblica, EUR-Lex]
    parole: [costituzione, costituzionale, incostituzionale, legittimità, corte, sentenza, manovra, legge di bilancio, delega, decreto-legge, emendamento, regioni, lep, retroattività, copertura, intesa]
```

Per farlo partecipare a ogni seduta sui conti, aggiungere `sempre: true` oppure convocarlo con `consiglio.py --prepara --esperti costituzionalista,…`. Il giurista generale resta: il costituzionalista ne approfondisce la parte costituzionale.

### `sistema/istruzioni_claude.md`

Dopo la sezione «2c. Leggi ed emendamenti», aggiungere:

```markdown
## 2c-bis. Controllo di costituzionalità

Per ogni testo di legge, emendamento o manovra, e per ogni proposta del Consiglio prima dell'adozione:
1. Lancia `python costituzione/controllo.py FILE --data <entrata in vigore>` (per le schede: `--scheda <id>`; per le leggi di bilancio: `--articoli 1-N`).
2. Esamina i rilievi alti e medi secondo `costituzione/istruzioni_costituzionalista.md`: verifica ogni sentenza con `python costituzione/giurisprudenza.py --verifica N/AAAA`, classifica (illegittimità probabile, dubbio serio, rischio basso) e proponi la riformulazione.
3. Scrivi l'esame in `costituzione/esami/<nome>.md`. Un'illegittimità probabile in una misura adottata è una linea rossa da segnalare al capo di governo.
4. Ogni giorno controlla in `costituzione/esami/gu/stato.json` gli atti nuovi con segnali `alto`: se toccano misure del programma, apri il riesame.
```

### `sistema/esporta_web.py`

1. Aggiungere la funzione, ad esempio dopo `obiettivi()`:

```python
def costituzione() -> dict:
    c = RADICE / "costituzione"
    if not c.exists():
        return {}
    esami = [{"id": f.stem, "testo": leggi(f)} for f in sorted((c / "esami").glob("*.md"))
             if not f.stem.endswith("_screening")]
    gu = json.loads(leggi(c / "esami" / "gu" / "stato.json")) if (c / "esami" / "gu" / "stato.json").exists() else {}
    return {"esami": esami,
            "gu_alti": [{"codice": k, **v} for k, v in gu.get("esaminati", {}).items() if v.get("alto")][-30:],
            "pronunce_verificate": len(json.loads(leggi(c / "giurisprudenza_verificata.json")))
                                   if (c / "giurisprudenza_verificata.json").exists() else 0}
```

2. Nel dizionario `dati` di `main()`, dopo `"governo": governo(),`:

```python
        "costituzione": costituzione(),
```

3. In `"documenti"`, dopo `"legislazione": …`:

```python
                      "costituzione": leggi(RADICE / "costituzione" / "README.md"),
```

L'interfaccia (`docs/`) può mostrare gli esami approfonditi in una scheda «Costituzione», accanto a «Legislazione».

### `integrita/catena.py`

Aggiungere i file del modulo alla catena delle impronte:
- in `REGOLE`, dopo `"governo/esperti.yaml"`: `"costituzione/parametri.yaml", "costituzione/controllo.py", "costituzione/istruzioni_costituzionalista.md"`;
- in `INPUT`, dopo `"dati/serie/*.csv"`: `"costituzione/giurisprudenza_verificata.json", "costituzione/testi/*.txt"`;
- in `OUTPUT`, dopo `"governo/mandati.csv"`: `"costituzione/esami/*.md"`.

Così ogni cambiamento ai parametri, alle regole dello screening o agli esami lascia un'impronta verificabile.
