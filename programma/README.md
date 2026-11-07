# GovernAI — Dal ventaglio di proposte al programma finanziato

Obiettivo: arrivare a **soluzioni pronte**, cioè con norma, tempi, copertura e indicatori, **coerenti con i dati**, cioè tutte finanziate nello scenario prudente del registro.

## Il meccanismo (negoziazione strutturata)

1. **Varianti.** Ogni agente ministeriale propone per ogni sua proposta 2–3 varianti di diversa ampiezza:
   - `PIENA`: la proposta come scritta;
   - `ESSENZIALE`: il cuore della misura, graduale o mirato;
   - `PILOTA`: una sperimentazione su pochi territori, a costo minimo, con valutazione.
   
   Ogni variante dichiara costo, fondi da cui preleva, strumento normativo e **intensità**, cioè la quota dell'effetto della versione piena che realizza (da 0 a 1).
2. **Menu delle coperture.** Un agente dedicato elenca misure di copertura **concrete e verificate**. Ad esempio: quale sussidio dannoso si riforma, quale spesa fiscale si abolisce, quale razionalizzazione di spesa si fa. Per ognuna indica gettito, chi paga ed effetti sui valori della Carta.
3. **Ottimizzazione.** Il coordinatore sceglie la combinazione di varianti e coperture con più valore secondo la Carta, rispettando la capienza di ogni fondo nello **scenario prudente**. Il metodo è la programmazione lineare intera (`ottimizza.py`). La scelta si ripete su centinaia di combinazioni di pesi tra i valori, per misurare quanto è robusta.
4. **Schede pronte.** Per le misure scelte, gli agenti hanno già scritto le schede di attuazione.

## Regole

- **Nessun rinnovo automatico.** Le misure temporanee in scadenza, cioè le politiche invariate per 10–14 mld, non si rinnovano d'ufficio. Ognuna compete con le altre proposte. È coerente con la proposta 01-P2 sulle spese fiscali a scadenza.
- **Niente deficit, niente risparmi non certificati, niente recupero di evasione non certificato** come copertura di spesa permanente.
- **Per i fondi coperti dal menu** (SAD, SPESE_FISCALI, ACCISE_SALUTE, PENSIONI, RIORDINO_BONUS, TASSA_SOGGIORNO, RIALLOCAZIONE), la capienza è data **solo dalle misure di copertura attivate**. Questo evita il doppio conteggio con `registro/fondi.csv`. Per gli altri fondi vale la capienza minima di `registro/fondi.csv`.

## File

| File | Contenuto | Autore |
|---|---|---|
| `varianti/NN_area.csv` | Varianti delle proposte dell'area | Agente d'area |
| `schede/NN_area.md` | Schede pronte di attuazione | Agente d'area |
| `coperture_menu.csv` | Misure di copertura concrete | Agente coperture |
| `coperture_menu.md` | Spiegazione delle misure, fonti, chi paga | Agente coperture |
| `ottimizza.py` | Ottimizzatore | Coordinatore |
| `selezione.md`, `selezione.csv` | Programma selezionato | Generato |

## Schema `varianti/NN_area.csv` (una riga per variante × fondo)

```
proposta_id,variante,descrizione,intensita,costo_2027,costo_2028,costo_2029,costo_regime,anno_regime,fondo_id,prelievo_regime,strumento,note
```

- `variante` ∈ {PIENA, ESSENZIALE, PILOTA}. Sono ammesse anche varianti `ZERO` per riforme senza costo.
- `intensita`: 1 per PIENA; per le altre, la quota dell'effetto della piena (es. 0,5). Va motivata nelle note.
- Costi in mld €/anno. La somma di `prelievo_regime` sulle righe della variante deve essere uguale a `costo_regime`.
- `fondo_id`: solo quelli di `registro/README.md`. **Non usare** DEFICIT, RISPARMI_ATTESI, IVA_EVASIONE, ETS (esaurito) o ALTRO per spesa permanente. Se serve una copertura nuova, usa il fondo a cui appartiene (es. una nuova spesa fiscale da tagliare → SPESE_FISCALI) e segnalala nelle note: l'agente coperture potrà inserirla nel menu.
- `strumento`: legge di bilancio / disegno di legge / decreto legislativo / decreto ministeriale / atto amministrativo / accordo Stato-Regioni.

## Schema `coperture_menu.csv`

```
misura_id,descrizione,fondo_id,gettito_min,gettito_max,anno_regime,gradualita,chi_paga,soggetti_coinvolti,RIS,FID,INN,BEN,APC,BPA,FUT,strumento,fonte_dato,note
```

- Gettito in mld €/anno a regime, al netto di quanto già previsto a legislazione vigente (es. i 7,37 mld di riordino delle spese fiscali già nel Piano strutturale).
- Colonne RIS…FUT: effetto della misura di copertura su ciascun valore, da −3 a +3, nell'orizzonte medio. Di solito BEN o RIS sono negativi per chi paga, e FUT o FID positivi.
