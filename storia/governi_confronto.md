# Il governo 2022-oggi a confronto con i governi dal 1979

*Rapporto generato da `storia/script/governi.py` con le serie di `storia/serie/`. Metodo: `storia/governi_metodo.md`. Dati osservati fino al 2025; il 2026 è una previsione ed è escluso. I governi sono indicati con le date; numeri d'ordine e altre informazioni sono in `storia/governi.csv`.*

**Come leggere.** La misura principale è la **differenza rispetto ai vicini**: il risultato dell'Italia meno la media di Francia, Germania e Spagna negli stessi anni. Così si toglie una parte degli shock comuni (crisi dell'euro, pandemia, energia, politica della BCE). Il **rango** dice in che posizione è un governo tra quelli confrontabili (1° = risultato migliore rispetto ai vicini). Non c'è un voto unico: la sintesi è per ambito. Nessun numero di questo rapporto prova che un risultato sia stato causato da un governo.

## In breve

Il governo 2022-oggi ha dati osservati per **2023-2025** (3 anni solari: il 2022 va al governo in carica per la maggior parte di quell'anno). È confrontato con 23 governi o periodi di governo dal 1979 al 2022.

| Ambito | Posizione mediana (0-100, 100 = primo) | Fascia | Indicatori (rango rispetto ai vicini) |
|---|---|---|---|
| conti | 52 (11° su 24) | terzo centrale | Variazione del debito pubblico: 12° su 24; Saldo primario medio: 12° su 24; Deficit medio: 9° su 24; Variazione della pressione fiscale: 23° su 24, solo ordinamento |
| crescita | 70 (8° su 24) | primo terzo | Crescita media annua del PIL pro capite reale: 8° su 24; Crescita media annua della produttività oraria: 20° su 24; Investimenti pubblici medi: 1° su 15 |
| lavoro | 83 (5° su 24) | primo terzo | Variazione del tasso di occupazione 15-64: 5° su 24; Variazione del tasso di occupazione femminile 15-64: 5° su 24; Variazione della disoccupazione giovanile 15-24: 5° su 24 |
| prezzi e mercati | 83 (3° su 24) | primo terzo | Spread medio con la Germania: 8° su 24; Inflazione media: 2° su 24 |
| società | 43 (8° su 11) | terzo centrale | Variazione della povertà assoluta (persone): 2° su 8, solo dato italiano; Emigrazione media annua di cittadini italiani: 11° su 11, solo dato italiano |

La posizione mediana è la mediana delle posizioni (0 = ultimo, 100 = primo) degli indicatori dell'ambito con un verso chiaro; la pressione fiscale è esclusa perché salire o scendere non è in sé un risultato migliore o peggiore. Tra parentesi, il posto del governo in carica se si ordinano tutti i governi per questa mediana. Per l'ambito società i ranghi usano il solo dato italiano.

**Sensibilità.** Nell'ambito crescita il primo posto per investimenti pubblici dipende in larga parte dal PNRR, deciso e finanziato prima del mandato; senza questo indicatore la posizione mediana in crescita scende a 43 (terzo centrale). Con gli anni spostati di uno (sezione 5) le posizioni mediane diventano: conti 74; crescita 57; lavoro 70; prezzi e mercati 87; società 50. I ranghi tra i soli governi con almeno due anni sono nella sezione 3.

## 1. Governi confrontati

Regole: un governo entra nel confronto se resta in carica almeno 12 mesi; ogni anno solare va al governo (o periodo) in carica per più giorni in quell'anno; i governi brevi consecutivi della stessa legislatura, nessuno dei quali arriva a 12 mesi, sono uniti in un *periodo di governo*. Un governo breve che non si può unire resta fuori dalla classifica, ma i suoi numeri sono nel file CSV.

| Governo o periodo | Governi inclusi (n.) | Dal | Al | Mesi | Anni assegnati | Nel confronto |
|---|---|---|---|---|---|---|
| governo 1978-1979 | n. 34 | 1978-03-11 | 1979-03-20 | 12 | - | no: nessun anno dal 1979 |
| governo 1979 (mar-ago) | n. 35 | 1979-03-20 | 1979-08-04 | 4 | - | no: meno di 12 mesi |
| periodo di governo 1979-1981 | n. 36, n. 37, n. 38 | 1979-08-04 | 1981-06-28 | 23 | 1979-1980 | sì |
| governo 1981-1982 | n. 39 | 1981-06-28 | 1982-08-23 | 14 | 1981-1982 | sì |
| periodo di governo 1982-1983 | n. 40, n. 41 | 1982-08-23 | 1983-08-04 | 11 | 1983 | sì |
| governo 1983-1986 | n. 42 | 1983-08-04 | 1986-08-01 | 36 | 1984-1986 | sì |
| periodo di governo 1986-1987 | n. 43, n. 44 | 1986-08-01 | 1987-07-28 | 12 | 1987 | sì |
| governo 1987-1988 | n. 45 | 1987-07-28 | 1988-04-13 | 8 | - | no: meno di 12 mesi |
| governo 1988-1989 | n. 46 | 1988-04-13 | 1989-07-22 | 15 | 1988-1989 | sì |
| governo 1989-1991 | n. 47 | 1989-07-22 | 1991-04-12 | 21 | 1990 | sì |
| governo 1991-1992 | n. 48 | 1991-04-12 | 1992-06-28 | 15 | 1991 | sì |
| governo 1992-1993 | n. 49 | 1992-06-28 | 1993-04-28 | 10 | 1992 | no: meno di 12 mesi |
| governo 1993-1994 | n. 50 | 1993-04-28 | 1994-05-10 | 12 | 1993 | sì |
| governo 1994-1995 | n. 51 | 1994-05-10 | 1995-01-17 | 8 | 1994 | no: meno di 12 mesi |
| governo 1995-1996 | n. 52 | 1995-01-17 | 1996-05-17 | 16 | 1995 | sì |
| governo 1996-1998 | n. 53 | 1996-05-17 | 1998-10-21 | 29 | 1996-1998 | sì |
| governo 1998-1999 | n. 54 | 1998-10-21 | 1999-12-22 | 14 | 1999 | sì |
| governo 1999-2000 | n. 55 | 1999-12-22 | 2000-04-25 | 4 | - | no: meno di 12 mesi |
| governo 2000-2001 | n. 56 | 2000-04-25 | 2001-06-11 | 14 | 2000 | sì |
| governo 2001-2005 | n. 57 | 2001-06-11 | 2005-04-23 | 46 | 2001-2004 | sì |
| governo 2005-2006 | n. 58 | 2005-04-23 | 2006-05-17 | 13 | 2005 | sì |
| governo 2006-2008 | n. 59 | 2006-05-17 | 2008-05-06 | 24 | 2006-2007 | sì |
| governo 2008-2011 | n. 60 | 2008-05-08 | 2011-11-16 | 42 | 2008-2011 | sì |
| governo 2011-2013 | n. 61 | 2011-11-16 | 2013-04-27 | 17 | 2012 | sì |
| governo 2013-2014 | n. 62 | 2013-04-28 | 2014-02-21 | 10 | 2013 | no: meno di 12 mesi |
| governo 2014-2016 | n. 63 | 2014-02-22 | 2016-12-12 | 34 | 2014-2016 | sì |
| governo 2016-2018 | n. 64 | 2016-12-12 | 2018-06-01 | 18 | 2017 | sì |
| governo 2018-2019 | n. 65 | 2018-06-01 | 2019-09-04 | 15 | 2018-2019 | sì |
| governo 2019-2021 | n. 66 | 2019-09-05 | 2021-02-13 | 17 | 2020 | sì |
| governo 2021-2022 | n. 67 | 2021-02-13 | 2022-10-22 | 20 | 2021-2022 | sì |
| governo 2022-oggi | n. 68 | 2022-10-22 | in carica | 49 | 2023-2025 | sì |

**Unioni dichiarate.** Il periodo di governo 1979-1981 unisce i governi n. 36, n. 37, n. 38 (stessa legislatura, nessuno arriva a 12 mesi; in tutto 23 mesi). Il periodo di governo 1982-1983 unisce i governi n. 40, n. 41 (stessa legislatura, nessuno arriva a 12 mesi; in tutto 11 mesi). Il periodo di governo 1986-1987 unisce i governi n. 43, n. 44 (stessa legislatura, nessuno arriva a 12 mesi; in tutto 12 mesi).

**Effetti della regola sugli anni.** Gli anni 1992, 1994, 2013 vanno a governi sotto i 12 mesi e restano fuori dalla classifica. Alcuni governi lunghi ricevono un solo anno perché negli anni di confine erano in carica per meno giorni del governo vicino (governo 1989-1991).

## 2. Tabella principale per ambito

In ogni cella: **differenza Italia meno vicini** (rango). Per povertà assoluta ed emigrazione non esiste un confronto omogeneo con gli altri paesi: la cella riporta il valore italiano (rango sul solo dato italiano). Unità: punti percentuali o punti di PIL; punti base per lo spread; migliaia di persone per l'emigrazione. Il governo in carica è in grassetto. *n.d.* = serie assente per quegli anni.

### Conti

| Governo o periodo | Anni | Variazione del debito pubblico (punti di PIL) | Saldo primario medio (% PIL) | Deficit medio (% PIL) | Variazione della pressione fiscale (punti di PIL) |
|---|---|---|---|---|---|
| periodo di governo 1979-1981 | 1979-1980 | -5,03 (4) | -3,24 (20) | +5,93 (17) | +1,44 (19) |
| governo 1981-1982 | 1981-1982 | +0,31 (11) | -3,61 (22) | +7,22 (18) | +2,68 (24) |
| periodo di governo 1982-1983 | 1983 | +3,26 (18) | -2,16 (19) | +7,35 (19) | +1,09 (16) |
| governo 1983-1986 | 1984-1986 | +8,90 (24) | -3,89 (23) | +9,71 (24) | -1,07 (3) |
| periodo di governo 1986-1987 | 1987 | +2,42 (16) | -4,29 (24) | +9,57 (22) | -0,83 (4) |
| governo 1988-1989 | 1988-1989 | +4,76 (23) | -3,50 (21) | +9,66 (23) | +1,24 (17) |
| governo 1989-1991 | 1990 | +0,30 (10) | -1,85 (18) | +9,24 (21) | +1,33 (18) |
| governo 1991-1992 | 1991 | +3,51 (20) | +0,25 (15) | +8,36 (20) | +0,21 (11) |
| governo 1993-1994 | 1993 | +2,56 (17) | +4,17 (4) | +5,29 (16) | +1,51 (21) |
| governo 1995-1996 | 1995 | -3,36 (6) | +7,03 (1) | +0,09 (4) | +0,14 (10) |
| governo 1996-1998 | 1996-1998 | -8,40 (2) | +4,83 (3) | +0,67 (7) | +0,89 (14) |
| governo 1998-1999 | 1999 | -0,41 (9) | +2,95 (6) | +0,22 (5) | +0,33 (13) |
| governo 2000-2001 | 2000 | -2,37 (7) | +1,98 (8) | +1,02 (11) | -0,36 (7) |
| governo 2001-2005 | 2001-2004 | -4,13 (5) | +1,61 (9) | +0,86 (10) | -0,16 (9) |
| governo 2005-2006 | 2005 | +1,26 (14) | -0,13 (16) | +2,22 (14) | -0,69 (5) |
| governo 2006-2008 | 2006-2007 | +1,57 (15) | +0,34 (14) | +1,93 (13) | +1,76 (22) |
| governo 2008-2011 | 2008-2011 | -8,30 (3) | +3,92 (5) | -1,75 (2) | +1,48 (20) |
| governo 2011-2013 | 2012 | -1,35 (8) | +5,06 (2) | -2,59 (1) | +0,90 (15) |
| governo 2014-2016 | 2014-2016 | +3,57 (21) | +2,20 (7) | -0,21 (3) | -2,01 (1) |
| governo 2016-2018 | 2017 | +1,01 (13) | +1,15 (11) | +0,81 (8) | -0,67 (6) |
| governo 2018-2019 | 2018-2019 | +3,31 (19) | +1,23 (10) | +0,63 (6) | +0,28 (12) |
| governo 2019-2021 | 2020 | +4,57 (22) | +0,40 (13) | +1,64 (12) | -0,26 (8) |
| governo 2021-2022 | 2021-2022 | -10,31 (1) | -1,63 (17) | +3,88 (15) | -1,10 (2) |
| **governo 2022-oggi** | 2023-2025 | +0,54 (12) | +1,11 (12) | +0,85 (9) | +1,77 (23) |

### Crescita

| Governo o periodo | Anni | Crescita media annua del PIL pro capite reale (% annua) | Crescita media annua della produttività oraria (% annua) | Investimenti pubblici medi (% PIL) |
|---|---|---|---|---|
| periodo di governo 1979-1981 | 1979-1980 | +2,53 (2) | +0,20 (6) | n.d. |
| governo 1981-1982 | 1981-1982 | -0,12 (9) | -3,37 (24) | n.d. |
| periodo di governo 1982-1983 | 1983 | -0,42 (11) | -2,58 (23) | n.d. |
| governo 1983-1986 | 1984-1986 | +0,72 (4) | -0,68 (13) | n.d. |
| periodo di governo 1986-1987 | 1987 | +0,17 (7) | +0,64 (4) | n.d. |
| governo 1988-1989 | 1988-1989 | -0,34 (10) | +0,34 (5) | n.d. |
| governo 1989-1991 | 1990 | -1,18 (20) | -0,88 (16) | n.d. |
| governo 1991-1992 | 1991 | -0,89 (18) | -1,96 (22) | n.d. |
| governo 1993-1994 | 1993 | +0,38 (5) | +0,07 (7) | n.d. |
| governo 1995-1996 | 1995 | +0,82 (3) | +1,15 (2) | -1,37 (15) |
| governo 1996-1998 | 1996-1998 | -0,61 (15) | -0,47 (11) | -0,83 (14) |
| governo 1998-1999 | 1999 | -1,35 (22) | -0,04 (8) | -0,72 (9) |
| governo 2000-2001 | 2000 | +0,17 (6) | +1,05 (3) | -0,75 (11) |
| governo 2001-2005 | 2001-2004 | -0,52 (13) | -0,93 (17) | -0,68 (8) |
| governo 2005-2006 | 2005 | -1,10 (19) | -0,60 (12) | -0,48 (2) |
| governo 2006-2008 | 2006-2007 | -1,39 (23) | -1,26 (19) | -0,59 (5) |
| governo 2008-2011 | 2008-2011 | -1,33 (21) | -0,71 (14) | -0,75 (12) |
| governo 2011-2013 | 2012 | -2,44 (24) | -1,70 (21) | -0,76 (13) |
| governo 2014-2016 | 2014-2016 | -0,83 (17) | -0,82 (15) | -0,56 (4) |
| governo 2016-2018 | 2017 | -0,53 (14) | -1,03 (18) | -0,60 (6) |
| governo 2018-2019 | 2018-2019 | -0,45 (12) | -0,19 (9) | -0,73 (10) |
| governo 2019-2021 | 2020 | -0,68 (16) | +2,91 (1) | -0,64 (7) |
| governo 2021-2022 | 2021-2022 | +2,93 (1) | -0,29 (10) | -0,49 (3) |
| **governo 2022-oggi** | 2023-2025 | +0,12 (8) | -1,60 (20) | +0,11 (1) |

### Lavoro

| Governo o periodo | Anni | Variazione del tasso di occupazione 15-64 (punti) | Variazione del tasso di occupazione femminile 15-64 (punti) | Variazione della disoccupazione giovanile 15-24 (punti) |
|---|---|---|---|---|
| periodo di governo 1979-1981 | 1979-1980 | +1,52 (3) | +1,47 (3) | -3,32 (3) |
| governo 1981-1982 | 1981-1982 | +2,02 (2) | +2,37 (2) | -3,23 (4) |
| periodo di governo 1982-1983 | 1983 | +0,10 (9) | -0,82 (20) | +0,56 (15) |
| governo 1983-1986 | 1984-1986 | +0,32 (7) | +0,39 (6) | +2,48 (22) |
| periodo di governo 1986-1987 | 1987 | -0,57 (19) | -0,21 (11) | +2,43 (21) |
| governo 1988-1989 | 1988-1989 | -1,06 (24) | -0,92 (21) | +2,29 (20) |
| governo 1989-1991 | 1990 | +0,02 (10) | -0,01 (8) | -1,24 (10) |
| governo 1991-1992 | 1991 | -0,92 (21) | -1,43 (23) | -0,82 (11) |
| governo 1993-1994 | 1993 | +1,49 (4) | -0,34 (14) | -8,21 (1) |
| governo 1995-1996 | 1995 | -0,90 (20) | -0,72 (17) | +2,85 (23) |
| governo 1996-1998 | 1996-1998 | -0,51 (16) | -0,11 (10) | +1,91 (19) |
| governo 1998-1999 | 1999 | -0,44 (15) | -0,43 (15) | +1,14 (17) |
| governo 2000-2001 | 2000 | -0,36 (14) | -0,33 (12) | +1,00 (16) |
| governo 2001-2005 | 2001-2004 | +2,05 (1) | +2,52 (1) | -7,73 (2) |
| governo 2005-2006 | 2005 | -0,96 (22) | -1,26 (22) | +0,37 (14) |
| governo 2006-2008 | 2006-2007 | -1,04 (23) | -1,51 (24) | -1,57 (9) |
| governo 2008-2011 | 2008-2011 | -0,21 (12) | -0,80 (19) | -0,59 (12) |
| governo 2011-2013 | 2012 | +0,47 (6) | +0,85 (4) | +3,52 (24) |
| governo 2014-2016 | 2014-2016 | -0,56 (18) | -0,79 (18) | +1,76 (18) |
| governo 2016-2018 | 2017 | -0,17 (11) | +0,04 (7) | -0,20 (13) |
| governo 2018-2019 | 2018-2019 | -0,35 (13) | -0,33 (13) | -2,38 (6) |
| governo 2019-2021 | 2020 | +0,26 (8) | -0,10 (9) | -2,07 (7) |
| governo 2021-2022 | 2021-2022 | -0,53 (17) | -0,67 (16) | -1,71 (8) |
| **governo 2022-oggi** | 2023-2025 | +0,96 (5) | +0,78 (5) | -2,72 (5) |

### Prezzi e mercati

| Governo o periodo | Anni | Spread medio con la Germania (punti base) | Inflazione media (% annua) |
|---|---|---|---|
| periodo di governo 1979-1981 | 1979-1980 | +274 (18) | +7,11 (24) |
| governo 1981-1982 | 1981-1982 | +606 (24) | +6,25 (22) |
| periodo di governo 1982-1983 | 1983 | +546 (23) | +6,34 (23) |
| governo 1983-1986 | 1984-1986 | +313 (19) | +3,13 (21) |
| periodo di governo 1986-1987 | 1987 | +116 (10) | +1,82 (16) |
| governo 1988-1989 | 1988-1989 | +232 (16) | +2,01 (18) |
| governo 1989-1991 | 1990 | +242 (17) | +2,25 (19) |
| governo 1991-1992 | 1991 | +354 (21) | +1,85 (17) |
| governo 1993-1994 | 1993 | +336 (20) | +0,91 (14) |
| governo 1995-1996 | 1995 | +366 (22) | +2,51 (20) |
| governo 1996-1998 | 1996-1998 | +117 (11) | +0,95 (15) |
| governo 1998-1999 | 1999 | +12 (1) | +0,52 (12) |
| governo 2000-2001 | 2000 | +19 (4) | +0,35 (11) |
| governo 2001-2005 | 2001-2004 | +18 (3) | +0,31 (8) |
| governo 2005-2006 | 2005 | +18 (2) | -0,24 (6) |
| governo 2006-2008 | 2006-2007 | +24 (5) | -0,26 (4) |
| governo 2008-2011 | 2008-2011 | +87 (7) | +0,32 (9) |
| governo 2011-2013 | 2012 | +219 (15) | +0,90 (13) |
| governo 2014-2016 | 2014-2016 | +86 (6) | -0,14 (7) |
| governo 2016-2018 | 2017 | +121 (12) | -0,27 (3) |
| governo 2018-2019 | 2018-2019 | +176 (14) | -0,54 (1) |
| governo 2019-2021 | 2020 | +126 (13) | -0,24 (5) |
| governo 2021-2022 | 2021-2022 | +115 (9) | +0,32 (10) |
| **governo 2022-oggi** | 2023-2025 | +92 (8) | -0,31 (2) |

### Società

| Governo o periodo | Anni | Variazione della povertà assoluta (persone) (punti) | Emigrazione media annua di cittadini italiani (migliaia) |
|---|---|---|---|
| governo 2001-2005 | 2001-2004 | n.d. | 38 (1) |
| governo 2005-2006 | 2005 | n.d. | 42 (3) |
| governo 2006-2008 | 2006-2007 | -0,20 (3) | 41 (2) |
| governo 2008-2011 | 2008-2011 | 1,30 (6) | 42 (4) |
| governo 2011-2013 | 2012 | 1,50 (7) | 68 (5) |
| governo 2014-2016 | 2014-2016 | n.d. | 102 (7) |
| governo 2016-2018 | 2017 | 0,50 (4) | 115 (8) |
| governo 2018-2019 | 2018-2019 | -0,80 (1) | 119 (9) |
| governo 2019-2021 | 2020 | 1,60 (8) | 121 (10) |
| governo 2021-2022 | 2021-2022 | 0,60 (5) | 97 (6) |
| **governo 2022-oggi** | 2023-2025 | -0,40 (2) | 121 (11) |

Verso: crescita, produttività, investimenti pubblici, occupazione e saldo primario, più alto è meglio; disoccupazione giovanile, debito, deficit, spread, inflazione, povertà ed emigrazione, più basso è meglio. Per la pressione fiscale il rango è solo un ordinamento (1 = calo maggiore rispetto ai vicini), non un giudizio.

## 3. Il governo in carica, indicatore per indicatore

| Indicatore (unità, anni) | Italia | Vicini | Differenza | Rango | Rango tra i governi con almeno 2 anni | Rango sul solo dato italiano |
|---|---|---|---|---|---|---|
| Crescita media annua del PIL pro capite reale (% annua, 2023-2025) | 0,79 | 0,66 | +0,12 | 8° su 24 | 4° su 12 | 17° su 24 |
| Crescita media annua della produttività oraria (% annua, 2023-2025) | -1,36 | 0,24 | -1,60 | 20° su 24 | 11° su 12 | 24° su 24 |
| Investimenti pubblici medi (% PIL, 2023-2025) | 3,53 | 3,42 | +0,11 | 1° su 15 | 1° su 8 | 1° su 15 |
| Variazione del tasso di occupazione 15-64 (punti, 2022->2025) | 2,38 | 1,42 | +0,96 | 5° su 24 | 4° su 12 | 2° su 24 |
| Variazione del tasso di occupazione femminile 15-64 (punti, 2022->2025) | 2,67 | 1,89 | +0,78 | 5° su 24 | 4° su 12 | 2° su 24 |
| Variazione della disoccupazione giovanile 15-24 (punti, 2022->2025) | -3,14 | -0,42 | -2,72 | 5° su 24 | 4° su 12 | 6° su 24 |
| Variazione del debito pubblico (punti di PIL, 2022->2025) | -1,25 | -1,79 | +0,54 | 12° su 24 | 7° su 12 | 7° su 24 |
| Saldo primario medio (% PIL, 2023-2025) | -0,73 | -1,84 | +1,11 | 12° su 24 | 6° su 12 | 15° su 24 |
| Deficit medio (% PIL, 2023-2025) | 4,52 | 3,67 | +0,85 | 9° su 24 | 5° su 12 | 12° su 24 |
| Variazione della pressione fiscale (punti di PIL, 2022->2024) | 0,74 | -1,03 | +1,77 | 23° su 24 | 11° su 12 | 14° su 24 |
| Spread medio con la Germania (punti base, 2023-2025) | 141 | 50 | +92 | 8° su 24 | 5° su 12 | 6° su 24 |
| Inflazione media (% annua, 2023-2025) | 2,71 | 3,02 | -0,31 | 2° su 24 | 2° su 12 | 12° su 24 |
| Variazione della povertà assoluta (persone) (punti, 2022->2025) | -0,40 | n.d. | n.d. | 2° su 8 | 2° su 5 | 2° su 8 |
| Emigrazione media annua di cittadini italiani (migliaia, 2023-2025) | 121 | n.d. | n.d. | 11° su 11 | 7° su 7 | 11° su 11 |

La colonna "solo dato italiano" mostra quanto cambia il quadro se non si tolgono gli shock comuni: per esempio l'occupazione italiana sale molto in assoluto, ma sale anche nei paesi vicini.

*Pressione fiscale, controllo.* La serie OCSE, usata perché copre tutti i governi dal 1979, si ferma al 2024 (Italia +0,7 punti nel 2022->2024, vicini -1,0). Con la serie AMECO, che arriva al 2025, l'Italia passa da 41,7% a 43,0% del PIL (+1,3 punti) contro -0,1 punti in media nei vicini: il segno del confronto non cambia.

## 4. Punto di partenza e contesto di ogni governo

Il punto di partenza è l'anno prima del primo anno assegnato. Gli shock sono quelli esterni che cadono negli anni assegnati; non correggono i numeri, servono a leggerli.

| Governo o periodo | Anno di partenza | Debito (% PIL) | Deficit (% PIL) | Spread (p.b.) | Shock esterni nel mandato |
|---|---|---|---|---|---|
| periodo di governo 1979-1981 | 1978 | 57,5 | 8,5 | 687 | secondo shock petrolifero |
| governo 1981-1982 | 1980 | 54,3 | 7,0 | 676 | - |
| periodo di governo 1982-1983 | 1982 | 61,0 | 10,0 | 1125 | - |
| governo 1983-1986 | 1983 | 67,0 | 10,1 | 1028 | - |
| periodo di governo 1986-1987 | 1986 | 82,0 | 12,0 | 558 | - |
| governo 1988-1989 | 1987 | 85,7 | 11,5 | 450 | - |
| governo 1989-1991 | 1989 | 89,5 | 11,4 | 544 | - |
| governo 1991-1992 | 1990 | 91,4 | 11,4 | 481 | - |
| governo 1993-1994 | 1992 | 101,1 | 10,4 | 544 | crisi valutaria del 1992 e uscita della lira dallo SME |
| governo 1995-1996 | 1994 | 116,6 | 9,1 | 365 | - |
| governo 1996-1998 | 1995 | 119,1 | 7,2 | 536 | - |
| governo 1998-1999 | 1998 | 113,9 | 3,0 | 31 | - |
| governo 2000-2001 | 1999 | 113,1 | 1,8 | 24 | - |
| governo 2001-2005 | 2000 | 108,7 | 2,4 | 32 | - |
| governo 2005-2006 | 2004 | 104,7 | 3,5 | 22 | - |
| governo 2006-2008 | 2005 | 106,2 | 4,1 | 21 | - |
| governo 2008-2011 | 2007 | 103,5 | 1,3 | 27 | crisi finanziaria mondiale; crisi dei debiti sovrani nell'area euro |
| governo 2011-2013 | 2011 | 119,1 | 3,5 | 281 | crisi dei debiti sovrani nell'area euro |
| governo 2014-2016 | 2013 | 131,9 | 2,9 | 275 | - |
| governo 2016-2018 | 2016 | 134,2 | 2,4 | 140 | - |
| governo 2018-2019 | 2017 | 133,7 | 2,5 | 179 | - |
| governo 2019-2021 | 2019 | 133,9 | 1,4 | 220 | pandemia |
| governo 2021-2022 | 2020 | 154,4 | 9,4 | 168 | shock dei prezzi dell'energia e rialzo dei tassi BCE |
| **governo 2022-oggi** | 2022 | 138,4 | 8,1 | 202 | shock dei prezzi dell'energia e rialzo dei tassi BCE |

### Cosa ha ereditato il governo in carica

- **Debito**: 138,4% del PIL nel 2022, il 2° punto di partenza più alto tra i 24 governi confrontati (il più alto è il 154,4% trovato dal governo 2021-2022).
- **Deficit**: 8,1% del PIL nel 2022, gonfiato dai crediti per i bonus edilizi decisi nel 2020-2021 (catalogo D105), registrati nei conti dal 2020 al 2023 dopo la riclassificazione Eurostat. Anche il deficit del 2023 (7,1%) contiene una quota rilevante di questi crediti.
- **Spread**: 202 punti base di media nel 2022, salito con il rialzo dei tassi BCE.
- **Inflazione**: 8,2% nel 2022, per lo shock energetico.
- **Lavoro**: occupazione 15-64 al 60,1% nel 2022, già in salita dal 2021.
- **Decisioni già prese**: il Piano nazionale di ripresa e resilienza (D107), deciso nel 2021, con spesa concentrata negli anni 2023-2026; i crediti edilizi già maturati, che pesano sul debito negli anni in cui vengono usati in compensazione; dal 2024 le nuove regole europee sui conti pubblici (D120).

### Contesto esterno nel mandato

- 2023: coda dello shock energetico e tassi BCE ai livelli più alti da oltre quindici anni; inflazione in calo in tutta l'area euro.
- 2023-2025: crescita debole nei paesi vicini (in Germania il PIL pro capite cala nel 2023 e nel 2024), il che rende più facile un buon risultato *relativo* dell'Italia; spesa del PNRR in aumento.
- Nessuna crisi finanziaria o sanitaria paragonabile a quelle del 1992, 2008-09, 2011-12 o 2020.

## 5. Ritardi degli effetti: versione con gli anni spostati di uno

Le misure agiscono con ritardo. Qui a ogni governo si assegnano gli anni spostati in avanti di uno (per il governo in carica: 2024-2025, perché il 2026 è solo una previsione).

| Indicatore | Differenza (anni propri) | Rango | Differenza (anni +1) | Rango |
|---|---|---|---|---|
| Crescita media annua del PIL pro capite reale | +0,12 | 8° su 24 | -0,19 | 11° su 24 |
| Crescita media annua della produttività oraria | -1,60 | 20° su 24 | -1,56 | 20° su 24 |
| Investimenti pubblici medi | +0,11 | 1° su 15 | +0,26 | 1° su 15 |
| Variazione del tasso di occupazione 15-64 | +0,96 | 5° su 24 | +0,20 | 9° su 24 |
| Variazione del tasso di occupazione femminile 15-64 | +0,78 | 5° su 24 | +0,14 | 8° su 24 |
| Variazione della disoccupazione giovanile 15-24 | -2,72 | 5° su 24 | -2,15 | 5° su 24 |
| Variazione del debito pubblico | +0,54 | 12° su 24 | +2,28 | 13° su 24 |
| Saldo primario medio | +1,11 | 12° su 24 | +2,41 | 7° su 24 |
| Deficit medio | +0,85 | 9° su 24 | -0,42 | 3° su 24 |
| Variazione della pressione fiscale | +1,77 | 23° su 24 | +1,03 | 17° su 24 |
| Spread medio con la Germania | +92 | 8° su 24 | +72 | 7° su 24 |
| Inflazione media | -0,31 | 2° su 24 | -0,88 | 1° su 24 |
| Variazione della povertà assoluta (persone) (solo Italia) | -0,40 | 2° su 8 | -0,40 | 1° su 10 |
| Emigrazione media annua di cittadini italiani (solo Italia) | 121 | 11° su 11 | 125 | 11° su 11 |

| Ambito | Posizione mediana, anni propri | Posizione mediana, anni +1 |
|---|---|---|
| conti | 52 (terzo centrale) | 74 (primo terzo) |
| crescita | 70 (primo terzo) | 57 (terzo centrale) |
| lavoro | 83 (primo terzo) | 70 (primo terzo) |
| prezzi e mercati | 83 (primo terzo) | 87 (primo terzo) |
| società | 43 (terzo centrale) | 50 (terzo centrale) |

## 6. Sintesi per ambito di tutti i governi

Posizione mediana 0-100 (100 = primo in tutti gli indicatori dell'ambito). Gli ambiti non si sommano: un governo può andare bene sui conti e male sulla crescita, e il peso da dare a ciascun ambito è una scelta politica.

| Governo o periodo | Anni | conti | crescita | lavoro | prezzi e mercati | società |
|---|---|---|---|---|---|---|
| periodo di governo 1979-1981 | 1979-1980 | 30 | 87 | 91 | 13 | n.d. |
| governo 1981-1982 | 1981-1982 | 26 | 33 | 96 | 4 | n.d. |
| periodo di governo 1982-1983 | 1983 | 22 | 30 | 39 | 4 | n.d. |
| governo 1983-1986 | 1984-1986 | 0 | 67 | 74 | 17 | n.d. |
| periodo di governo 1986-1987 | 1987 | 9 | 80 | 22 | 48 | n.d. |
| governo 1988-1989 | 1988-1989 | 4 | 72 | 13 | 30 | n.d. |
| governo 1989-1991 | 1990 | 26 | 26 | 61 | 26 | n.d. |
| governo 1991-1992 | 1991 | 17 | 17 | 13 | 22 | n.d. |
| governo 1993-1994 | 1993 | 35 | 78 | 87 | 30 | n.d. |
| governo 1995-1996 | 1995 | 87 | 91 | 17 | 13 | n.d. |
| governo 1996-1998 | 1996-1998 | 91 | 39 | 35 | 48 | n.d. |
| governo 1998-1999 | 1999 | 78 | 43 | 39 | 76 | n.d. |
| governo 2000-2001 | 2000 | 70 | 78 | 43 | 72 | n.d. |
| governo 2001-2005 | 2001-2004 | 65 | 48 | 100 | 80 | 100 |
| governo 2005-2006 | 2005 | 43 | 52 | 9 | 87 | 80 |
| governo 2006-2008 | 2006-2007 | 43 | 22 | 4 | 85 | 81 |
| governo 2008-2011 | 2008-2011 | 91 | 21 | 52 | 70 | 49 |
| governo 2011-2013 | 2012 | 96 | 13 | 78 | 43 | 37 |
| governo 2014-2016 | 2014-2016 | 74 | 39 | 26 | 76 | 40 |
| governo 2016-2018 | 2017 | 57 | 43 | 57 | 72 | 44 |
| governo 2018-2019 | 2018-2019 | 61 | 52 | 48 | 72 | 60 |
| governo 2019-2021 | 2020 | 48 | 57 | 70 | 65 | 5 |
| governo 2021-2022 | 2021-2022 | 39 | 86 | 35 | 63 | 46 |
| **governo 2022-oggi** | 2023-2025 | 52 | 70 | 83 | 83 | 43 |

Attenzione: i governi con un solo anno assegnato hanno posizioni più estreme (in alto o in basso) anche per semplice variabilità; i governi lunghi tendono verso il centro. L'ambito società ha dati solo dal 2002-2005.

## 7. Cosa è merito o responsabilità plausibile, e cosa no

Questa parte è un giudizio prudente, non una misura. "Plausibile" vuol dire che i tempi e il meccanismo sono coerenti con una scelta del governo, non che l'effetto sia dimostrato.

**Plausibilmente legato, in tutto o in parte, a scelte del governo in carica**

- *Rientro del deficit*: da 7,1% (2023) a 3,1% (2025) del PIL, con il saldo primario tornato positivo (+0,8% nel 2025). Ha contribuito lo stop alla cessione dei crediti edilizi (D112), insieme alla fine delle misure temporanee contro il caro energia. Una parte del miglioramento è però meccanica: i crediti decisi nel 2020-2021 erano già stati contabilizzati negli anni precedenti, e pesano ancora sul 2023, che abbassa la media del mandato.
- *Pressione fiscale in aumento mentre nei vicini scende* (23° su 24 nell'ordinamento dal calo maggiore all'aumento maggiore rispetto ai vicini). Una parte dipende da scelte (le modifiche all'IRPEF e il taglio dei contributi riducono il prelievo, D116), una parte dall'aumento degli occupati e dal drenaggio fiscale (scaglioni non adeguati all'inflazione). I dati qui non separano le due parti.
- *Spread*: la discesa da 202 (2022) a 100 punti base (2025) è coerente con un percorso dei conti giudicato credibile dai mercati, ma avviene mentre la BCE dispone di uno strumento contro gli aumenti ingiustificati degli spread (dal 2022) e mentre lo spread francese sale per ragioni interne alla Francia: il confronto relativo ne risulta favorito.

**Plausibilmente non (o non solo) dovuto al governo in carica**

- *Inflazione più bassa dei vicini*: dipende soprattutto dal calo dei prezzi dell'energia, a cui l'Italia è più esposta (i prezzi salgono di più nel 2022 e scendono di più dopo), e dalla politica monetaria della BCE.
- *Occupazione ai massimi e disoccupazione giovanile in calo*: la crescita parte nel 2021; il calo della popolazione in età da lavoro alza il tasso anche a parità di occupati. Il vantaggio rispetto ai vicini resta positivo, ma si riduce con gli anni spostati di uno.
- *Investimenti pubblici ai massimi della serie*: spinti dal PNRR, deciso e finanziato prima (D107). La responsabilità del governo in carica riguarda l'attuazione, che la Corte dei conti (citata nel catalogo) giudica in ritardo sulla spesa effettiva.
- *Debito quasi stabile*: aiutato dall'inflazione del 2022-2023, che fa crescere il PIL nominale, e frenato dai crediti edilizi già decisi, che pesano sul debito quando vengono usati in compensazione.
- *Produttività in calo*: è il dato peggiore del governo in carica rispetto ai vicini. Riflette in parte proprio la crescita delle ore lavorate più rapida della produzione, e un problema strutturale aperto da oltre vent'anni (rottura del 2001 in `serie_lunghe.md`); non è attribuibile a un singolo mandato.
- *Emigrazione di italiani*: la media annua (121 mila) è la più alta tra i governi dal 2002, ma la serie sale quasi ogni anno dal 2008: il rango riflette soprattutto la tendenza di lungo periodo e i cambiamenti nelle registrazioni all'anagrafe, non un effetto del mandato.
- *Povertà assoluta*: 9,7% nel 2022, 9,3% nel 2025. La variazione è piccola, vicina all'errore statistico dell'indagine. La sostituzione del Reddito di cittadinanza con l'Assegno di inclusione (D114), secondo le stime della Banca d'Italia riportate nel catalogo, riduce la povertà meno della misura precedente: il lieve calo è quindi più probabilmente legato a lavoro e prezzi.

## 8. Decisioni del catalogo per governo

**Avvertenza.** Il catalogo `decisioni_1977_2026.csv` è una selezione di 120 decisioni fatta da chi ha costruito la base dati. La scelta di cosa includere è soggettiva e il numero di decisioni per governo dipende da quella scelta. **Non va usato come voto ai governi**: serve solo a ricordare quali misure di rilievo cadono in ciascun mandato e cosa dicono le valutazioni disponibili. Ogni decisione è assegnata al governo dello stesso presidente del Consiglio in carica per più giorni in quell'anno (quando lo stesso presidente guida due governi nello stesso anno l'assegnazione è segnata con *). Le decisioni del 1977 sono di un governo precedente al periodo esaminato.

| Governo o periodo | Decisioni | Efficace | Efficace in parte | Evidenza insufficiente | Inefficace | Effetti negativi |
|---|---|---|---|---|---|---|
| governo 1978-1979 (fuori classifica) | 5 | 0 | 3 | 0 | 1 | 1 |
| periodo di governo 1979-1981 | 1 | 0 | 1 | 0 | 0 | 0 |
| governo 1981-1982 | 1 | 0 | 0 | 1 | 0 | 0 |
| governo 1983-1986 | 5 | 0 | 2 | 1 | 1 | 1 |
| governo 1987-1988 (fuori classifica) | 1 | 0 | 0 | 1 | 0 | 0 |
| governo 1988-1989 | 2 | 0 | 0 | 2 | 0 | 0 |
| governo 1989-1991 | 2 | 0 | 2 | 0 | 0 | 0 |
| governo 1991-1992 | 1 | 0 | 1 | 0 | 0 | 0 |
| governo 1992-1993 (fuori classifica) | 8 | 3 | 4 | 1 | 0 | 0 |
| governo 1993-1994 | 3 | 0 | 1 | 2 | 0 | 0 |
| governo 1994-1995 (fuori classifica) | 1 | 0 | 0 | 0 | 0 | 1 |
| governo 1995-1996 | 2 | 0 | 2 | 0 | 0 | 0 |
| governo 1996-1998 | 9 | 1 | 5 | 2 | 1 | 0 |
| governo 1998-1999 | 3 | 0 | 3 | 0 | 0 | 0 |
| governo 1999-2000 (fuori classifica) | 1 | 0 | 1 | 0 | 0 | 0 |
| governo 2000-2001 | 2 | 0 | 0 | 0 | 1 | 1 |
| governo 2001-2005 | 9 | 0 | 3 | 4 | 0 | 2 |
| governo 2005-2006 | 2 | 0 | 1 | 0 | 0 | 1 |
| governo 2006-2008 | 5 | 2 | 3 | 0 | 0 | 0 |
| governo 2008-2011 | 8 | 1 | 3 | 1 | 2 | 1 |
| governo 2011-2013 | 8 | 0 | 6 | 2 | 0 | 0 |
| governo 2014-2016 | 11 | 0 | 7 | 1 | 1 | 2 |
| governo 2016-2018 | 4 | 0 | 2 | 2 | 0 | 0 |
| governo 2018-2019 | 5 | 0 | 1 | 3 | 1 | 0 |
| governo 2019-2021 | 4 | 0 | 1 | 2 | 0 | 1 |
| governo 2021-2022 | 5 | 0 | 2 | 3 | 0 | 0 |
| **governo 2022-oggi** | 9 | 1 | 1 | 7 | 0 | 0 |

**Decisioni del catalogo nel governo 2021-2022**

| Id | Anno | Decisione | Giudizio | Solidità dell'evidenza |
|---|---|---|---|---|
| D107 | 2021 | PNRR: circa 190 miliardi tra sovvenzioni e prestiti UE legati a riforme e investimenti | evidenza insufficiente | media |
| D108 | 2021 | Riforme Cartabia del processo penale e civile (obiettivi PNRR) | efficace in parte | bassa |
| D109 | 2021 | Assegno unico e universale per i figli | efficace in parte | media |
| D110 | 2021 | Riforma IRPEF da 5 a 4 aliquote e revisione delle detrazioni | evidenza insufficiente | media |
| D111 | 2021 | Quote 102 e 103: uscite anticipate temporanee dopo Quota 100 | evidenza insufficiente | media |

**Decisioni del catalogo nel governo 2022-oggi**

| Id | Anno | Decisione | Giudizio | Solidità dell'evidenza |
|---|---|---|---|---|
| D112 | 2023 | Stop alla cessione dei crediti e allo sconto in fattura per i bonus edilizi | efficace | media |
| D113 | 2023 | Decreto Cutro: flussi programmati triennali e restrizioni alla protezione speciale | evidenza insufficiente | bassa |
| D114 | 2023 | Assegno di inclusione e Supporto per la formazione e il lavoro al posto del Reddito di cittadinanza | efficace in parte | media |
| D115 | 2023 | Nuovo codice dei contratti pubblici | evidenza insufficiente | bassa |
| D116 | 2023 | IRPEF a tre aliquote (23-35-43%) e taglio contributivo per i redditi bassi | evidenza insufficiente | media |
| D117 | 2024 | Concordato preventivo biennale per autonomi e piccole imprese | evidenza insufficiente | media |
| D118 | 2024 | Legge quadro sull'autonomia differenziata delle Regioni | evidenza insufficiente | bassa |
| D119 | 2024 | Abrogazione del reato di abuso d'ufficio e modifiche al traffico di influenze | evidenza insufficiente | bassa |
| D120 | 2024 | Applicazione delle nuove regole europee: tetto alla crescita della spesa netta su sette anni | evidenza insufficiente | bassa |

Per il governo in carica quasi tutte le decisioni hanno "evidenza insufficiente" perché sono recenti, non perché siano state valutate male. Alcune decisioni con effetti nel mandato in corso (PNRR, crediti edilizi) appartengono ai governi precedenti.

## 9. Cosa non sappiamo e limiti

1. **Mandato in corso.** Il governo in carica ha 3 anni di dati (2023-2025); il 2025 è ancora un consuntivo provvisorio e il 2026 è escluso perché è una previsione. Il giudizio su un mandato in corso può cambiare con i dati del 2026 e con le revisioni.
2. **Ritardi.** Molte misure agiscono dopo anni (pensioni, istruzione, giustizia, investimenti). La versione con gli anni spostati di uno coglie solo i ritardi brevi; quelli lunghi non sono misurabili con questo metodo.
3. **Pochi anni.** Molti governi hanno uno o due anni assegnati: un anno buono o cattivo pesa moltissimo. Per questo il rapporto mostra anche il rango tra i soli governi con almeno due anni.
4. **Nessuna causalità.** La differenza con i vicini toglie gli shock comuni, non quelli che colpiscono l'Italia più degli altri (energia, debito alto quando salgono i tassi, calo demografico). Non dice cosa sarebbe successo con scelte diverse.
5. **Eredità.** I risultati di un governo dipendono anche dalle decisioni dei governi precedenti (bonus edilizi, PNRR, riforme delle pensioni) e dal punto di partenza (debito, spread). La tabella del punto di partenza aiuta a leggerli, ma non li corregge.
6. **Dati non omogenei.** Prima del 1991 la Germania è la Germania Ovest; per deficit e saldo primario la Spagna manca prima del 1995 (media su Francia e Germania); gli investimenti pubblici partono dal 1995; la pressione fiscale OCSE si ferma al 2024; povertà assoluta ed emigrazione non hanno un confronto omogeneo con gli altri paesi; la povertà assoluta cambia metodo nel 2014 (il governo 2014-2016 non ha un valore); lo spread prima del 1999 misura anche il rischio di cambio.
7. **Indicatori scelti.** Gli indicatori coprono conti, crescita, lavoro, prezzi e società, ma non misurano qualità dei servizi, giustizia, ambiente, sicurezza o istruzione: un governo può andare meglio o peggio su aspetti che qui non compaiono.
8. **Verso degli indicatori.** Dire che "più basso è meglio" per deficit, debito, inflazione o emigrazione è una convenzione largamente condivisa, ma non vale in ogni circostanza (un deficit alto durante una recessione può essere la scelta giusta). Per la pressione fiscale non si dà alcun verso.

## Fonti

- Elenco e date dei governi: Presidenza del Consiglio dei ministri, *I Governi nelle Legislature* (https://www.governo.it/it/i-governi-dal-1943-ad-oggi/i-governi-nelle-legislature/192) per i governi dal 2001; Camera dei deputati, dati aperti (https://dati.camera.it, classe ocd:governo) per le date dei governi 1978-2001. Numerazione: secondo governo De Gasperi (13 luglio 1946) = n. 1, coerente con i 68 governi della Repubblica indicati dalla Presidenza del Consiglio.
- Serie: `storia/serie/_registro.csv` (AMECO, FMI, OCSE, Eurostat, ISTAT).
- Decisioni: `storia/decisioni_1977_2026.csv`.
