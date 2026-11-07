# Rubrica di valutazione per il panel indipendente

Ogni valutatore assegna, per **ogni proposta** (`motore/proposte.csv`, 52 proposte) e **ogni valore** della Carta (`01_carta_valori.md`: RIS, FID, INN, BEN, APC, BPA, FUT), un punteggio sui tre orizzonti.

## Scala (identica per tutti i valori e orizzonti)

| Punteggio | Significato |
|---|---|
| +3 | Effetto molto positivo, ampio e documentato da evidenze solide |
| +2 | Effetto positivo chiaro |
| +1 | Effetto positivo modesto o limitato a pochi |
| 0 | Nessun effetto rilevante su questo valore, oppure effetti che si compensano |
| −1 | Effetto negativo modesto |
| −2 | Effetto negativo chiaro |
| −3 | Effetto molto negativo, o rischio di violare una linea rossa |

## Regole

1. **Valuta l'effetto sul valore, non la bontà generale della proposta.** Una buona riforma della giustizia può valere 0 su *Bellezza, patrimonio e accoglienza*: è corretto.
2. **Il costo non entra nel punteggio**: lo gestisce il motore, che calcola il valore per euro. Considera però gli effetti del modo di finanziarla. Ad esempio, una copertura in deficit pesa su FUT; un'accisa pesa su BEN di chi la paga.
3. **Considera chi perde.** Se una proposta danneggia un gruppo, il punteggio su RIS o BEN deve rifletterlo, anche se la media migliora.
4. **Orizzonti**: Breve 0–2 anni, Medio 3–10, Lungo 10–30+. Valuta l'effetto atteso in quel periodo, inclusi i rischi di attuazione (una proposta che probabilmente fallisce in attuazione vale meno).
5. **Neutralità**: non premiare o penalizzare una proposta perché appartiene a una tradizione politica. Chiediti: "Una persona di qualunque orientamento, con questi dati, darebbe lo stesso punteggio?"
6. **Confidenza**: A (alta, evidenze solide), M (media), B (bassa, effetti incerti o dati insufficienti).
7. **Linea rossa**: se una proposta rischia di violare la Costituzione o un diritto fondamentale, scrivi `si` nella colonna `linea_rossa` e spiega.
8. Fonti: i dossier `ministeri/*.md` (già corretti con dati verificati) e le verifiche `dati/verifiche/*.md`. Non fidarti dei punteggi complessivi scritti nei dossier: sono stati dati dagli stessi autori delle proposte.

## Formato di uscita (CSV, una riga per proposta × valore = 364 righe)

```
proposta_id,valore,breve,medio,lungo,confidenza,linea_rossa,motivazione
01-P1,RIS,0,0,1,M,no,"Migliora la trasparenza verso le future generazioni ma effetto indiretto"
```

- `valore` ∈ {RIS, FID, INN, BEN, APC, BPA, FUT}
- `breve`, `medio`, `lungo`: interi da −3 a +3
- `motivazione`: una frase, al massimo 25 parole
- Separatore virgola, testo tra virgolette.
