# Registro obiettivi: note dell'agente "obiettivi" (7 novembre 2026)

**Copertura.** 52 schede e **158 KPI** (3 per scheda, 4 in 02-C2 e 08-P1).
- **44 con serie automatica.** 35 usano serie già presenti in `dati/serie`. 9 usano nuove serie `obi_*`: 3 scaricate da Eurostat (presenze luglio-agosto, rimpatri/ordini, infermieri/medici), 6 derivate da file esistenti (quote dell'export, APS per rifugiati, regioni con perdite idriche sopra il 50%, disposition time annuale). Le serie si rigenerano con `aggiorna_obi.py` e sono registrate in `_registro_obi.csv`.
- **114 manuali.** Le fonti sono ISTAT non scaricata, INPS, Agenas, ANBSC, ministeri, oppure dati che nascono con la misura.
- `verifica_obiettivi.py` controlla che ogni filtro restituisca una sola serie. Controlla anche che il valore all'anno base coincida con la scheda: tutti gli scarti sono inferiori a 0,05, tranne 07-C3-a (22,45 contro 22%, arrotondamento).

**Problemi trovati**
- **Basi mancanti:** 46 KPI (29%) non hanno una base numerica. Sono "da rilevare", "n.d." o in attesa di dati INPS, ACN o AGEA.
- **Obiettivi non numerici:** in 28 KPI mancano entrambi gli obiettivi. 17 KPI hanno obiettivi solo relativi a una base che non esiste ancora (ad esempio -20%, +10 punti, base × 2): sono in `obiettivo_relativo`.
- **Obiettivi che dipendono dalla variante:** 5 KPI (07-C5-a, 08-P5-a, 06-C5-a, 06-C3-a, 04-P5-c). Per la difesa (07-C5-a) la scheda non raccomanda una variante: la direzione resta una scelta politica.
- **Unità incoerenti tra base e obiettivo:** 06-C1-c (milioni di prestazioni contro %), 06-C3-a (tutte le CdC contro le sole hub), 09-C4-a (numero di PA contro %), 01-P5-c (PUN contro prezzo relativo).
- **KPI vaghi:** 01-P1-c, 02-C3-a ("non oltre lo scenario RGS"), 07-C5-c ("in calo"), 08-P4-b, 08-P6-c, 09-C2-c, 09-C3-b, 04-P6-c (confronto con una previsione).
- **Basi deboli:** fonti di stampa o non verificate in 05-C4-b, 05-C4-c, 06-C2-c, 06-C4-c, 06-C5-a/b, 08-P2-a e 05-C6-b.
- **Dati puntuali senza serie storica:** Terna (03-P2) e ANBSC (07-C4). Il filtro NATO di 07-C5-a va aggiornato a ogni nuovo rapporto. 02-C5-b non ha un equivalente Eurostat.
