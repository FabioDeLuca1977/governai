# Come contribuire a GovernAI

GovernAI è un prototipo a scopo sociale e **ogni suggerimento è ben accetto**.

## Proporre un problema o un'idea

Apri una [issue con il modulo "Suggerimento o richiesta di analisi"](../../issues/new?template=analisi.yml). Serve solo un account GitHub gratuito. Ecco cosa succede dopo:

1. **Revisione umana.** Un membro del progetto legge la proposta e controlla che sia pertinente e rispettosa.
2. **Approvazione.** Se la approva, le applica l'etichetta `analisi-approvata`.
3. **Analisi.** Il livello AI prepara una diagnosi e tre opzioni. Le opzioni hanno costi e coperture senza deficit e sono valutate da tre valutatori indipendenti sui 10 valori della [Carta](01_carta_valori.md).
4. **Pubblicazione.** Il risultato compare in `analisi/` e nella sezione "Analisi" del sito.

## Critiche al metodo, ai dati o ai valori

Le critiche sono particolarmente preziose: aiutano a capire se GovernAI è davvero neutrale e se i dati sono corretti. Puoi segnalare:
- un dato sbagliato, indicando la fonte ufficiale corretta;
- una stima di costo poco credibile;
- un valore mancante;
- un effetto non considerato.

Per tutto questo, usa lo stesso modulo e scegli l'area "Metodo di GovernAI".

## Contributi al codice

Le pull request sono benvenute.

**Requisiti.**
- Il calcolo deve restare riproducibile.
- Le modifiche alle regole (Carta, rubrica, motore) vanno spiegate nella descrizione.
- Ogni nuova fonte di dati deve essere ufficiale e citata.

**Verifica prima di proporre una modifica.**

```bash
pip install -r requirements.txt
cd sistema && python pipeline.py --senza-download --ricalcola --senza-ai
python ../integrita/catena.py --verifica
```

## Regole di convivenza

Rispetto per tutte le persone e tutte le posizioni. Le proposte si discutono con dati e argomenti, non con appartenenze.

I contenuti offensivi, discriminatori o fuori tema vengono chiusi.
