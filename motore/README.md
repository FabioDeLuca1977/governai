# GovernAI — Motore decisionale

Applica la Carta dei valori (`../01_carta_valori.md`) alle 52 proposte. Non sceglie un'unica combinazione di pesi "giusta": distingue ciò che è buono **qualunque** sia la sensibilità politica da ciò che dipende dai valori di chi decide.

## Come funziona

1. **Panel indipendente.** Tre valutatori (A, B, C): agenti AI distinti da quelli che hanno scritto le proposte. Non sono valutatori umani: è un limite dichiarato. Danno un punteggio a ogni proposta sui 10 valori della Carta × 3 orizzonti con la stessa rubrica (`rubrica.md`). Lavorano in ordini diversi per ridurre gli effetti di ancoraggio. L'accordo tra loro si misura con l'alfa di Krippendorff.
2. **SMAA (analisi di accettabilità multicriterio stocastica).** Il motore estrae decine di migliaia di combinazioni di pesi tra i valori e tra gli orizzonti. Vale il vincolo della Carta: il lungo periodo pesa almeno quanto il breve. A ogni estrazione usa il punteggio di uno dei valutatori scelto a caso, cella per cella. Per ogni proposta calcola:
   - la **probabilità di essere utile**;
   - la probabilità di stare nel primo quarto;
   - l'intervallo di rango.
3. **Classi.**
   - **Robusta**: utile in ≥95% delle combinazioni.
   - **Dipendente dai valori**: utile tra il 50% e il 95%. Il motore indica quali valori la rendono utile.
   - **Sfavorevole**: utile in meno della metà delle combinazioni.
4. **Pacchetti per budget.** Per ogni livello di risorse permanenti il motore sceglie il pacchetto con più valore che sta nel budget (problema dello zaino), e conta quanto spesso ogni proposta entra al variare dei pesi. I livelli predefiniti sono 4, 10 e 18 mld l'anno, cioè i valori minimo, centrale e massimo stimati nel `registro/`.

## Uso

```bash
python decidi.py
```

Opzioni: `--n 20000` (numero di estrazioni), `--budget 4 10 18`, `--seed 42`. I risultati sono in `esito.md` (leggibile) e `esito_proposte.csv` (dati).

## File

| File | Contenuto |
|---|---|
| `proposte.csv` | Le 52 proposte, con costo dal registro e costo opportunità (es. il dividendo climatico) |
| `rubrica.md` | Istruzioni per i valutatori |
| `punteggi_A.csv`, `_B`, `_C` | Punteggi del panel |
| `decidi.py` | Il motore |
| `esito.md`, `esito_proposte.csv` | Risultati generati |

## Quando arriveranno i pesi dell'assemblea dei cittadini

Diventeranno lo scenario centrale, ma l'analisi di robustezza resta pubblica. Un buon governo deve sapere quanto le sue scelte dipendono dai pesi.
