# Istruzioni per la revisione di un articolato (Claude nell'app, senza API)

`verifica_testo.py` fa i controlli che si possono fare con regole fisse. Questa guida dice a Claude come completare la revisione **con giudizio**, lavorando nell'app sui file del repository (nessuna chiamata API, nessuna chiave).

La revisione è un supporto alla decisione, non un parere legale. Le decisioni restano alle persone.

## 0. Preparazione

1. Eseguire il controllo automatico e leggere il rapporto:
   ```bash
   cd legislazione
   python verifica_testo.py <file.md> [--scheda 06-C2] -o prove/<nome>.md
   ```
2. Leggere, nell'ordine:
   - `01_carta_valori.md`: i 10 valori, le domande e le **linee rosse**;
   - `giuridico/quadro.md`: vincoli tributari, costituzionali ed europei;
   - `legislazione/regole_redazione.md`: le regole di tecnica legislativa (con le fonti);
   - se il testo riguarda una scheda: la scheda in `programma/schede/` e le righe di `giuridico/conformita.csv` con lo stesso `id`.
3. Aggiornare l'archivio, se non è stato fatto oggi: `python scarica_gu.py`.

## 1. Verificare i rilievi automatici

Per ogni rilievo del rapporto:

- **confermare** o **scartare** (falso positivo), con una riga di motivazione;
- per gli errori confermati, scrivere la **riformulazione** esatta del comma.

Falsi positivi tipici del controllo automatico:
- una sigla definita in un articolo precedente o in una legge citata;
- un «entro N giorni» la cui decorrenza è nella frase precedente;
- un decreto attuativo il cui termine è in un altro comma;
- un riferimento interno a un articolo di un atto citato poco prima.

Dove il rapporto segnala **«❌ non trovato»** o **«Data errata»**, aprire il link Normattiva e correggere gli estremi. Dove dice **«— non verificabile»** (atti UE, codici, testi unici citati per sigla), controllare a mano su Normattiva o EUR-Lex. Per vedere se l'atto è stato modificato di recente, usare:

```bash
python cerca.py --cita "legge 31 dicembre 2009, n. 196" --articolo 17
```

## 2. Controlli che richiedono giudizio

### 2.1 Tecnica legislativa (oltre il controllo automatico)
- **La norma esiste ancora nella forma citata?** Se l'articolato novella un comma, verificare su Normattiva (versione vigente) che le parole da sostituire ci siano davvero.
- **Novella o norma autonoma?** Se il testo modifica una disciplina esistente senza novellarla, proporre la novella (RR 2001, n. 9).
- **Abrogazioni implicite.** Elencare le norme che il testo rende inapplicabili e proporre l'abrogazione espressa (RR 2001, n. 3).
- **Atti attuativi.** Per ogni decreto o regolamento: chi lo adotta, con chi (concerto, intesa), entro quando, che cosa succede se non viene adottato.
- **Deleghe.** Oggetto definito, principi e criteri direttivi specifici (Corte cost. 192/2024 in `giuridico/quadro.md`), termine, pareri parlamentari, clausola finanziaria.
- **Copertura.** I mezzi devono essere quelli dell'art. 17, comma 1, L. 196/2009, quantificati per anno e nello stesso atto. Non valgono: entrate da riforme future o da recupero dell'evasione, risparmi non certi, fondi delle Camere, risorse UE già programmate per altro. Confrontare gli importi con il costo della variante nella scheda e in `registro/`.

### 2.2 Coerenza con la Carta dei 10 valori
Per ogni articolo, rispondere alle domande della Carta solo dove sono pertinenti. Non dare punteggi: li dà il panel di valutatori (`motore/`).

| Valore | Domanda di controllo sul testo normativo |
|---|---|
| RIS Rispetto e diversità | Il testo tratta in modo diverso persone in situazioni uguali? I criteri sono oggettivi (art. 3 Cost.)? Funziona anche per chi non è il cittadino «medio»? |
| FID Fiducia e trasparenza | Dati, criteri e risultati sono pubblici? Chi decide è individuato e ne risponde? La norma è stabile o rinvia tutto a decreti? |
| INN Innovazione | Semplifica o aggiunge adempimenti? La tecnologia ha una supervisione umana? |
| BEN Benessere | L'effetto sulla vita concreta delle persone è dichiarato e misurabile? |
| APC Apprendimento e cultura | Le misure su scuola e formazione raggiungono prima chi parte svantaggiato? |
| BPA Bellezza, patrimonio, accoglienza | Il testo prevede silenzio-assenso su paesaggio e beni culturali (vietato, art. 9)? |
| FUT Futuro | Chi paga e quando? Ci sono oneri che crescono dopo il triennio senza copertura? |
| EQU Equità | Chi guadagna e chi perde, per reddito, territorio, genere, età? I costi pesano in proporzione alla capacità contributiva (art. 53)? |
| SIC Sicurezza senza controllo assoluto | Nuovi trattamenti di dati personali hanno base di legge, proporzionalità, durata limitata, DPIA e controllo indipendente? |
| CIT Cittadinanza responsabile | Prevede reciprocità e partecipazione, senza condizionalità che neghino diritti? |

### 2.3 Linee rosse (bloccanti)
Segnalare come **BLOCCANTE** ogni disposizione che:
1. viola diritti fondamentali (artt. 2 e 3 Cost., Carta UE) — RIS;
2. riduce la trasparenza o l'indipendenza degli organi di controllo — FID;
3. affida a una tecnologia pubblica decisioni sui diritti senza supervisione umana (AI Act; L. 132/2025) — INN;
4. scarica costi sulle generazioni future senza copertura o viola l'equilibrio di bilancio (artt. 9 e 81 Cost.) — FUT;
5. sposta costi sui più deboli senza compensazione (art. 3, secondo comma, e art. 53 Cost.) — EQU;
6. introduce sorveglianza biometrica generalizzata, profilazione dei cittadini o punteggi sociali, o limita libertà senza base di legge, proporzionalità, durata limitata e controllo giudiziario (artt. 13-15 Cost.; art. 8 CEDU) — SIC;
7. usa la responsabilità civica per escludere da diritti fondamentali — CIT.

Una linea rossa non si compensa con benefici su altri valori: va riformulata la norma.

### 2.4 Conformità con `giuridico/quadro.md`
Controllare almeno:
- **riparto di competenze** (art. 117): niente comandi di dettaglio alle Regioni; intesa per fondi vincolati in materie regionali e per decreti legislativi su materie intrecciate;
- **strumento giusto** (tabella § 5): un DM non può fare ciò che spetta alla legge; un d.lgs. serve una delega vigente;
- **tributi**: art. 23 (limiti fissati in legge), Statuto del contribuente (niente retroattività), direttive IVA e accise, aiuti di Stato (GBER in scadenza il 31/12/2026);
- **regole UE di bilancio**: le coperture creano spazio solo con nuove entrate per legge o tagli effettivi;
- **autonomia delle Camere** (art. 64): uffici presso le Camere solo con il loro consenso e modifica dei regolamenti;
- **dati e IA**: GDPR, AI Act (alto rischio dal 2/12/2027), L. 132/2025.

Se una misura è `incompatibile` o `condizionato` in `giuridico/conformita.csv`, verificare che l'articolato rispetti le condizioni indicate.

### 2.5 Chiarezza per i cittadini
- Il **titolo** dice di che cosa parla la legge.
- Ogni comma contiene **un solo precetto**; i periodi sono brevi.
- Chi ha diritti o obblighi è **nominato** (non «i soggetti interessati»).
- Le **date** sono certe; gli importi sono in euro, per anno.
- Proporre una **sintesi in linguaggio semplice** di 3-5 righe: chi ne beneficia, chi paga, da quando, chi controlla.

## 3. Formato dell'esito

Aggiungere in fondo al rapporto in `legislazione/prove/` (o in un file nuovo accanto) una sezione:

```markdown
## Revisione con giudizio (Claude, AAAA-MM-GG)

**Esito:** pronto | da correggere | bloccato (linea rossa)

### Rilievi automatici
| Rilievo | Confermato? | Motivo | Riformulazione |

### Linee rosse e quadro giuridico
- …

### Valori
- RIS: … (solo i valori toccati)

### Testo riformulato
Art. 1 (…)
1. …

### Sintesi per i cittadini
…

### Limiti della revisione
Che cosa non è stato verificato e chi deve farlo (uffici legislativi, Ragioneria, Avvocatura).
```

Regole di comportamento:
- citare solo norme verificate (Normattiva, EUR-Lex, archivio GU); se non si riesce a verificarle, scriverlo;
- non inventare articoli, commi o importi: se manca un dato, lasciare un segnaposto evidente e dirlo;
- non modificare le schede o altri file fuori da `legislazione/` senza richiesta esplicita.
