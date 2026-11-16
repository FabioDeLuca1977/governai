# L'Italia in quasi cinquant'anni: serie storiche lunghe a confronto (1977-2025)

Questo rapporto mette in fila i numeri dell'Italia dal 1977 (o dal primo anno disponibile) a oggi e li confronta con Francia, Germania e Spagna, più l'area euro e l'Unione europea a 27 quando esistono. Serve a vedere **come è andata** e **quando le tendenze cambiano**. Non spiega le cause: gli anni di rottura sono messi accanto agli shock e alle decisioni che coincidono, come **ipotesi da verificare**. Le decisioni dei governi sono catalogate in un lavoro separato.

Tutti i numeri vengono da fonti ufficiali scaricate con script ripetibili (`storia/script/`). Nessun numero è stimato a mano: dove una serie manca, la cella è vuota e lo diciamo.

## Come leggere

- **Dati**: una serie per file in `storia/serie/` (formato `anno,paese,valore,unita,fonte`); l'elenco completo con fonti, link e anni coperti è in `storia/serie/_registro.csv`. Medie per decennio in `_decenni.csv`, rotture in `_rotture.csv`.
- **Paesi**: IT Italia, FR Francia, DE Germania, ES Spagna, EA area euro (composizione attuale a 20), UE27 Unione europea a 27. La riga **"IT - media FR/DE/ES"** è la distanza dell'Italia dalla media semplice degli altri tre: negativa vuol dire "sotto".
- **Germania prima del 1991**: sono dati della sola Germania Ovest (segnalato nella colonna `fonte`).
- **2025 e 2026**: per le serie AMECO il 2025 è un consuntivo provvisorio, il **2026 è una previsione** della Commissione europea (primavera 2026) ed è segnato come tale; le tabelle per decennio si fermano al 2025.
- **Decennio 2020-25**: comprende la pandemia (2020) e il rimbalzo (2021), quindi le medie sono più "rumorose".
- **Rotture**: per ogni serie dell'Italia, e per la distanza Italia-confronto, cerchiamo fino a tre anni in cui la serie cambia media (per crescite, saldi, tassi) o tendenza (per livelli come debito e occupazione). Usiamo un test semplice (somma minima dei quadrati dei residui con soglia F di Andrews al 5%). Con dati annuali autocorrelati il test tende a trovare rotture anche dove il cambiamento è graduale: gli anni indicati vanno presi come "qui la serie cambia passo", con un margine di uno-due anni.

## Calendario degli shock e delle decisioni con cui confrontare le rotture (ipotesi, non cause)

| Anni | Evento che coincide |
|---|---|
| 1979 | Ingresso della lira nel Sistema monetario europeo (SME) |
| 1981 | "Divorzio" tra Tesoro e Banca d'Italia (la banca centrale non è più obbligata a comprare i titoli invenduti) |
| 1984-86 | Accordi sulla scala mobile (1984), referendum (1985), calo del prezzo del petrolio (1986) |
| 1992-93 | Crisi valutaria e uscita della lira dallo SME, manovra straordinaria, riforma Amato delle pensioni, accordi sul costo del lavoro (luglio 1992 e 1993), privatizzazioni |
| 1995-98 | Riforma Dini delle pensioni (1995), rientro nello SME (1996), risanamento per entrare nell'euro, pacchetto Treu sul lavoro (1997) |
| 1999-2002 | Nascita dell'euro (1999) e delle banconote (2002); Cina nell'OMC (2001); riforma del Titolo V (2001) |
| 2003-04 | Legge Biagi sul lavoro (2003) |
| 2008-09 | Crisi finanziaria globale |
| 2011-12 | Crisi dei debiti sovrani, governo Monti, riforma Fornero, "whatever it takes" della BCE (2012) |
| 2014-15 | Acquisti di titoli della BCE (dal 2015), Jobs Act (2015) |
| 2019 | Reddito di cittadinanza e "quota 100" |
| 2020-21 | Pandemia, sospensione delle regole di bilancio europee, PNRR (dal 2021), superbonus edilizio |
| 2022-23 | Shock dei prezzi dell'energia, rialzo dei tassi BCE |
| 2024 | Nuove regole di bilancio europee; Assegno di inclusione al posto del Reddito di cittadinanza |

## In sintesi: dieci fatti

1. **Crescita**: fino all'inizio degli anni Novanta l'Italia cresce come Francia, Germania e Spagna (PIL pro capite 1977-1991: +40%, il migliore dei quattro). Dagli anni Novanta cresce circa 1 punto l'anno in meno; il test colloca l'inizio del distacco tra la fine degli anni Ottanta e i primi Novanta.
2. **Trent'anni persi in termini relativi**: dal 1995 al 2025 il PIL pro capite reale sale del 18% in Italia, contro il 36-37% di Francia e Germania, il 47% della Spagna e il 42% dell'area euro. Tra il 2007 e il 2013 l'Italia perde oltre il 10% e torna ai livelli di fine anni Novanta.
3. **Produttività ferma dal 2000**: il PIL per ora lavorata cresceva dell'1,9% l'anno nel 1977-2000 e di circa 0% dal 2001 (rottura nel 2001). Dal 1995 al 2025: Italia +6%, Germania +34%, Francia +28%, Spagna +19%.
4. **Ricchezza relativa**: a parità di potere d'acquisto il PIL pro capite italiano passa da 123 (1999) a 96 (2025) con la media UE27 = 100; dal 2014 è sotto la media dei tre paesi di confronto.
5. **Lavoro**: l'occupazione 15-64 anni sale dal 51-53% (fino al 1999) al 62,5% (2025, record), ma la distanza dagli altri tre si allarga fino a quasi 10 punti; per le donne è di circa 15 punti. La disoccupazione giovanile tocca il 40% nel 2013 e scende al 20-21% nel 2024-25.
6. **Prezzi e tassi**: inflazione dal 15% (1977-85) al 5% (1986-96) e al 2% (dal 1997), con rotture nel 1986 e nel 1997; lo spread sul Bund crolla dal 1996-97 e risale dal 2010 (media 191 punti base nel 2010-25 contro 63 nel 1996-2009).
7. **Debito e avanzo primario**: il debito passa dal 53% del PIL (1977) al 119% (1995) e al 137% (2025). Dal 1992 al 2019 l'Italia ha un avanzo primario ogni anno tranne il 2009 (rottura nel 1991), ma la spesa per interessi resta circa il doppio di quella degli altri paesi.
8. **Tasse**: la pressione fiscale sale di circa 15 punti tra il 1977 (26%) e il 1999 (41%), con rottura nel 1992; prima era sotto la media dei tre paesi, dal 1998 è sopra di 2,5-4 punti.
9. **Povertà e disuguaglianza**: la disuguaglianza dei redditi sale nei primi anni Novanta (Gini OCSE da 28 a 33) e poi resta ferma, sopra Francia e Germania; la povertà assoluta quasi triplica, dal 3,3% (2005) al 9-10% (2022-25), con una rottura nel 2012.
10. **Demografia, studio e territorio**: figli per donna da 1,93 (1977) a 1,18 (2024); immigrazione netta dal 1988, ma gli italiani che si cancellano per l'estero passano da circa 40 mila l'anno (2002-10) a 141 mila (2024); laureati 25-34enni al 31%, 14-19 punti sotto gli altri tre per tutto il periodo; il PIL pro capite del Mezzogiorno resta al 55-57% di quello del Centro-Nord dal 1995 al 2024, senza convergenza.

---

## 1. Crescita, reddito e produttività

**Crescita PIL reale, %, media per periodo**

| Paese | 1970-79 | 1980-89 | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|---:|---:|
| IT | 3,8 | 2,3 | 1,5 | 0,5 | 0,2 | 1,2 |
| FR | 4,1 | 2,4 | 2,1 | 1,6 | 1,4 | 0,9 |
| DE | 3,3 | 2,0 | 2,3 | 0,8 | 2,0 | 0,1 |
| ES | 3,9 | 2,7 | 2,6 | 2,6 | 1,1 | 1,8 |
| EA |  |  | 2,6 | 1,4 | 1,4 | 1,1 |
| UE27 |  |  | 2,6 | 1,5 | 1,6 | 1,2 |
| IT - media FR/DE/ES | 0,0 | -0,0 | -0,8 | -1,1 | -1,3 | 0,2 |

**Crescita PIL pro capite reale, %, media per periodo**

| Paese | 1970-79 | 1980-89 | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|---:|---:|
| IT | 3,2 | 2,3 | 1,4 | 0,1 | 0,2 | 1,4 |
| FR | 3,5 | 1,8 | 1,6 | 0,9 | 1,0 | 0,6 |
| DE | 3,1 | 1,8 | 1,7 | 0,9 | 1,8 | -0,2 |
| ES | 2,8 | 2,3 | 2,2 | 1,2 | 0,9 | 1,0 |
| EA |  |  | 2,4 | 1,0 | 1,2 | 0,8 |
| UE27 |  |  | 2,5 | 1,3 | 1,4 | 1,0 |
| IT - media FR/DE/ES | 0,2 | 0,3 | -0,4 | -0,9 | -1,0 | 0,9 |

**PIL pro capite reale, indice 1977 = 100**

| Anno | IT | FR | DE | ES | EA | UE27 |
|---|---:|---:|---:|---:|---:|---:|
| 1991 | 140 | 132 | 138 | 132 |  |  |
| 1999 | 156 | 151 | 153 | 155 | 110 | 110 |
| 2007 | 169 | 171 | 174 | 184 | 127 | 130 |
| 2013 | 150 | 170 | 182 | 165 | 123 | 128 |
| 2019 | 160 | 181 | 198 | 191 | 136 | 144 |
| 2025 | 172 | 187 | 196 | 200 | 142 | 152 |

**PIL pro capite reale, indice 1995 = 100**

| Anno | IT | FR | DE | ES | EA | UE27 |
|---|---:|---:|---:|---:|---:|---:|
| 2007 | 116 | 124 | 122 | 135 | 127 | 130 |
| 2013 | 103 | 124 | 127 | 121 | 123 | 128 |
| 2019 | 109 | 131 | 139 | 140 | 136 | 144 |
| 2025 | 118 | 136 | 137 | 147 | 142 | 152 |

**PIL pro capite PPA, UE27=100, media per periodo**

| Paese | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|
| IT | 125,0 | 114,1 | 99,7 | 96,4 |
| FR | 116,3 | 112,7 | 106,4 | 99,4 |
| DE | 130,2 | 122,0 | 125,5 | 119,2 |
| ES | 93,6 | 101,2 | 91,5 | 88,1 |
| EA | 114,0 | 111,7 | 107,1 | 104,4 |
| UE27 | 100,0 | 100,0 | 100,0 | 100,0 |
| IT - media FR/DE/ES | 11,6 | 2,1 | -8,1 | -5,9 |

**Crescita produttivita' oraria, %, media per periodo**

| Paese | 1970-79 | 1980-89 | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|---:|---:|
| IT | 4,0 | 1,7 | 1,4 | 0,1 | 0,3 | -0,2 |
| FR | 4,4 | 2,9 | 1,8 | 1,1 | 0,9 | -0,2 |
| DE | 4,1 | 2,1 | 2,3 | 0,9 | 1,2 | 0,3 |
| ES | 4,6 | 3,3 | 0,9 | 0,6 | 1,0 | 0,4 |
| EA |  |  | 1,4 | 0,9 | 1,0 | 0,3 |
| UE27 |  |  | 1,8 | 1,2 | 1,2 | 0,5 |
| IT - media FR/DE/ES | -0,3 | -1,1 | -0,3 | -0,8 | -0,7 | -0,4 |

**Il grafico, a parole.** Se si disegna il PIL pro capite reale con il 1977 a 100, le quattro linee salgono insieme fino ai primi anni Novanta; nel 1991 l'Italia è anzi leggermente davanti (140 contro 132-138). Dalla metà degli anni Novanta la linea italiana si appiattisce, nel 2008-2013 scende (da 169 a 150, tornando al livello della fine degli anni Novanta), poi risale lentamente. Nel 2025 è a 172, contro 187 della Francia, 196 della Germania e 200 della Spagna. Con base 1995 il quadro è ancora più netto: +18% per l'Italia in trent'anni, +36/37% per Francia e Germania, +47% per la Spagna, +42% per l'area euro.

**Rotture.**
- Crescita del PIL, distanza Italia-media degli altri tre: il test indica un cambio intorno al **1988** (da circa +0,3 a circa **-1,1 punti l'anno** fino al 2019) e un nuovo cambio nel **2020** (distanza vicina a zero nel 2020-25, anche per il rimbalzo dopo la pandemia e per la debolezza tedesca). Guardando i decenni, il distacco diventa chiaro negli anni Novanta (-0,8 punti l'anno) e si allarga negli anni Duemila e Duemiladieci (-1,1 e -1,3).
- Produttività oraria dell'Italia: rottura nel **2001**. Prima cresceva in media dell'1,9% l'anno (1977-2000), dopo di circa **0%** (2001-2025). Dal 1995 al 2025 il PIL per ora lavorata in Italia sale del 6% in tutto; in Germania del 34%, in Francia del 28%, in Spagna del 19%.
- PIL pro capite a parità di potere d'acquisto (UE27 = 100): l'Italia passa da 123 nel 1999 a 96 nel 2025. Rotture nel **2004** e nel **2014**: dal 2014 l'Italia è sotto la media dei tre paesi di confronto di circa 8 punti, mentre fino al 2013 era sopra. Attenzione: il calo vale in parte per tutti i paesi "vecchi" dell'Unione, perché i nuovi membri crescono più in fretta; ma il calo italiano è il più forte.

**Coincidenze da verificare.** La frattura della produttività intorno al 2000 coincide con l'ingresso nell'euro, l'entrata della Cina nel commercio mondiale e le riforme del lavoro di fine anni Novanta (che hanno fatto crescere l'occupazione più del prodotto). La caduta 2008-2013 coincide con due crisi in sequenza (2008-09 e 2011-12).

## 2. Lavoro

**Tasso di occupazione 15-64, %, media per periodo**

| Paese | 1970-79 | 1980-89 | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|---:|---:|
| IT | 52,0 | 52,6 | 52,1 | 56,9 | 57,1 | 60,4 |
| FR | 65,8 | 62,5 | 60,9 | 63,4 | 64,1 | 67,9 |
| DE | 65,5 | 62,8 | 65,0 | 66,9 | 74,1 | 76,7 |
| ES | 57,3 | 49,1 | 50,5 | 62,3 | 59,6 | 65,5 |
| UE27 |  |  |  | 62,8 | 65,0 | 69,6 |
| IT - media FR/DE/ES | -9,7 | -5,6 | -6,7 | -7,3 | -8,9 | -9,6 |

**Occupazione femminile 15-64, %, media per periodo**

| Paese | 1970-79 | 1980-89 | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|---:|---:|
| IT | 29,0 | 34,0 | 36,4 | 44,3 | 47,7 | 51,5 |
| FR | 51,2 | 51,2 | 53,3 | 58,0 | 60,5 | 65,3 |
| DE | 47,6 | 48,7 | 55,4 | 60,7 | 69,8 | 73,2 |
| ES | 31,0 | 27,6 | 33,7 | 50,2 | 54,3 | 60,6 |
| UE27 |  |  |  | 55,4 | 59,5 | 64,9 |
| IT - media FR/DE/ES | -12,7 | -8,5 | -11,1 | -12,0 | -13,8 | -14,9 |

**Disoccupazione, %, media per periodo**

| Paese | 1970-79 | 1980-89 | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|---:|---:|
| IT | 6,0 | 8,5 | 10,7 | 8,2 | 10,9 | 7,9 |
| FR | 4,4 | 8,6 | 9,7 | 8,4 | 9,6 | 7,6 |
| DE | 2,0 | 5,8 | 7,4 | 8,5 | 4,5 | 3,4 |
| ES | 4,5 | 16,4 | 19,5 | 11,4 | 20,5 | 12,9 |
| EA |  |  |  | 9,7 | 10,2 | 7,0 |
| UE27 |  |  | 10,4 | 9,2 | 9,6 | 6,4 |
| IT - media FR/DE/ES | 2,4 | -1,8 | -1,5 | -1,2 | -0,7 | -0,1 |

**Disoccupazione 15-24, %, media per periodo**

| Paese | 1970-79 | 1980-89 | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|---:|---:|
| IT | 15,9 | 31,4 | 31,4 | 24,6 | 34,9 | 24,4 |
| FR | 8,8 | 16,9 | 19,9 | 19,4 | 23,1 | 18,7 |
| DE | 3,2 | 7,9 | 7,7 | 11,1 | 7,5 | 6,6 |
| ES | 9,9 | 36,6 | 35,5 | 23,1 | 44,7 | 30,5 |
| UE27 |  |  |  | 18,8 | 20,6 | 15,5 |
| IT - media FR/DE/ES | 11,4 | 11,0 | 10,3 | 6,7 | 9,8 | 5,8 |

**Tasso di occupazione 15-64, %, anni chiave**

| Anno | IT | FR | DE | ES | UE27 |
|---|---:|---:|---:|---:|---:|
| 1977 | 53,4 | 66,0 | 64,2 | 57,3 |  |
| 1991 | 52,6 | 61,2 | 67,1 | 51,8 |  |
| 1999 | 52,9 | 61,6 | 65,2 | 55,0 |  |
| 2007 | 58,6 | 63,8 | 69,0 | 66,8 | 64,3 |
| 2013 | 55,5 | 63,5 | 73,5 | 55,6 | 63,1 |
| 2019 | 59,1 | 65,5 | 76,7 | 64,3 | 68,4 |
| 2024 | 62,2 | 69,0 | 77,5 | 67,2 | 70,7 |
| 2025 | 62,5 | 69,4 | 77,2 | 68,1 | 71,0 |

**Occupazione femminile 15-64, %, anni chiave**

| Anno | IT | FR | DE | ES | UE27 |
|---|---:|---:|---:|---:|---:|
| 1977 | 31,8 | 51,5 | 47,6 | 30,9 |  |
| 1991 | 36,5 | 52,4 | 56,3 | 32,5 |  |
| 1999 | 38,3 | 55,0 | 57,4 | 39,1 |  |
| 2007 | 46,6 | 59,1 | 63,2 | 56,0 | 57,0 |
| 2013 | 46,5 | 59,8 | 69,0 | 51,0 | 57,7 |
| 2019 | 50,2 | 62,4 | 72,8 | 58,8 | 63,1 |
| 2024 | 53,3 | 66,4 | 74,1 | 62,6 | 66,2 |
| 2025 | 53,8 | 66,9 | 74,1 | 63,7 | 66,6 |

**Il grafico, a parole.** Il tasso di occupazione italiano resta fermo tra il 51% e il 53% per venticinque anni (1977-1999), sale fino al 58,6% nel 2007, ricade al 55,5% nel 2013 e riparte fino al 62,5% nel 2025, il valore più alto della serie. Ma anche gli altri salgono: la distanza dalla media di Francia, Germania e Spagna è di circa 6-7 punti negli anni Ottanta e Novanta e di quasi **10 punti** nel 2020-25. Per le donne la distanza è ancora più ampia (circa -15 punti nel 2020-25). La disoccupazione giovanile italiana è sempre stata molto sopra quella francese e tedesca; tocca il 40% nel 2013 e scende al 20-21% nel 2024-25.

**Rotture.**
- Occupazione: cambi di tendenza nel **2000** (inizio della salita) e nel **2010** (crisi). Per le donne nel **2001**, **2009** e **2020**.
- Distanza dagli altri paesi: il test indica il **1986-1988** come l'inizio di un divario più ampio, soprattutto per le donne (da -9 a -12,5 punti in media).
- Disoccupazione: rotture nel **2001**, **2007** e **2013**; il punto più alto è il 2013-2014.

**Coincidenze da verificare.** La salita dal 2000 coincide con il pacchetto Treu (1997), la legge Biagi (2003) e con l'aumento dell'immigrazione regolarizzata; quella dopo il 2013 con il Jobs Act (2015) e con l'innalzamento dell'età di pensione (2011). Una parte della crescita dell'occupazione dopo il 2019 dipende anche dal calo della popolazione in età di lavoro (il tasso è un rapporto). Le indagini sulle forze di lavoro hanno cambiato metodo nel 1992-93, nel 2004 e nel 2021: piccoli salti in quegli anni possono essere statistici.

## 3. Prezzi, tassi e spread

**Inflazione, %, media per periodo**

| Paese | 1970-79 | 1980-89 | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|---:|---:|
| IT | 12,3 | 11,2 | 4,2 | 2,3 | 1,2 | 3,0 |
| FR | 8,8 | 7,4 | 1,9 | 1,7 | 1,1 | 2,5 |
| DE | 4,9 | 2,9 | 2,6 | 1,6 | 1,3 | 3,4 |
| ES | 14,4 | 10,2 | 4,2 | 3,0 | 1,2 | 3,4 |
| EA |  |  | 2,2 | 2,2 | 1,3 | 3,3 |
| UE27 |  |  | 6,2 | 2,6 | 1,4 | 3,9 |
| IT - media FR/DE/ES | 2,9 | 4,4 | 1,3 | 0,2 | -0,1 | -0,1 |

**Tasso a 10 anni, %, media per periodo**

| Paese | 1970-79 | 1980-89 | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|---:|---:|
| IT | 10,1 | 14,8 | 10,0 | 4,5 | 3,2 | 2,8 |
| FR | 9,0 | 11,8 | 7,0 | 4,3 | 1,6 | 1,8 |
| DE | 8,1 | 7,6 | 6,6 | 4,1 | 1,1 | 1,3 |
| ES | 12,7 | 14,4 | 9,4 | 4,4 | 3,0 | 2,1 |
| EA |  |  |  | 4,1 | 2,1 | 1,8 |
| UE27 |  |  |  | 4,2 | 2,2 | 2,0 |
| IT - media FR/DE/ES | 3,3 | 3,5 | 2,3 | 0,3 | 1,3 | 1,1 |

**Spread sul Bund, punti base, media per periodo**

| Paese | 1970-79 | 1980-89 | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|---:|---:|
| IT | 201 | 719 | 336 | 39 | 214 | 152 |
| FR | 88 | 414 | 41 | 13 | 52 | 54 |
| ES | 578 | 678 | 278 | 22 | 189 | 86 |
| IT - media FR/DE/ES | 185 | 173 | 177 | 22 | 93 | 82 |

**Spread sul Bund, punti base, anni chiave**

| Anno | IT | FR | ES |
|---|---:|---:|---:|
| 1977 | 808 | 324 |  |
| 1991 | 472 | 60 | 293 |
| 1999 | 24 | 12 | 24 |
| 2007 | 27 | 8 | 9 |
| 2013 | 275 | 63 | 299 |
| 2019 | 220 | 38 | 91 |
| 2024 | 139 | 65 | 83 |
| 2025 | 100 | 76 | 62 |

**Il grafico, a parole.** L'inflazione italiana è al 17% nel 1977 e al 21% nel 1980, scende sotto il 10% a metà anni Ottanta e intorno al 2% dal 1997. Da allora è allineata a quella degli altri paesi (anzi un po' più bassa nel 2010-25), salvo la fiammata del 2022 (8,2%). Il rendimento dei titoli a dieci anni segue la stessa discesa. Lo spread sul Bund tedesco era di 800 punti base nel 1977, 470 nel 1991, scende a 18-39 punti tra il 1998 e il 2007, risale a 275 nel 2013 e a 100 nel 2025 (media annua).

**Rotture.**
- Inflazione: rotture nel **1986** (da circa 15% a 5%) e nel **1997** (a 2%), sia per l'Italia sia per la sua distanza dagli altri.
- Spread: rotture nel **1986**, **1996** e **2010**. Dopo il 2010 lo spread medio (191 punti) è circa tre volte quello del 1996-2009 (63 punti).

**Coincidenze da verificare.** 1979-1986: SME, "divorzio" 1981, fine della scala mobile piena, calo del petrolio. 1996-97: rientro nello SME e convergenza verso l'euro. 2010-12: crisi dei debiti sovrani; 2012 e 2015: interventi della BCE. Prima dell'euro lo spread misurava anche il rischio di svalutazione della lira, quindi non è direttamente confrontabile con quello di oggi.

## 4. Conti pubblici

**Debito pubblico, % PIL, media per periodo**

| Paese | 1970-79 | 1980-89 | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|---:|---:|
| IT | 49,6 | 73,4 | 109,6 | 107,1 | 130,1 | 140,7 |
| FR | 21,8 | 30,0 | 51,9 | 66,5 | 94,8 | 112,8 |
| DE | 22,1 | 37,8 | 50,4 | 64,0 | 71,4 | 64,7 |
| ES | 12,9 | 32,7 | 55,7 | 46,6 | 92,7 | 108,6 |
| EA |  |  | 72,4 | 69,9 | 90,5 | 91,9 |
| UE27 |  |  | 70,7 | 66,7 | 84,4 | 85,0 |
| IT - media FR/DE/ES | 34,9 | 39,9 | 56,9 | 48,0 | 43,8 | 45,3 |

**Debito pubblico, % PIL, anni chiave**

| Anno | IT | FR | DE | ES | EA | UE27 |
|---|---:|---:|---:|---:|---:|---:|
| 1977 | 53,5 | 20,9 | 26,3 | 12,5 |  |  |
| 1991 | 94,5 | 37,6 | 38,7 | 42,2 |  |  |
| 1999 | 113,1 | 61,4 | 60,3 | 60,9 | 71,6 | 69,6 |
| 2007 | 103,5 | 65,5 | 63,7 | 35,7 | 65,9 | 62,4 |
| 2013 | 131,9 | 94,6 | 77,5 | 100,0 | 95,1 | 88,8 |
| 2019 | 133,9 | 98,2 | 58,7 | 97,7 | 85,5 | 79,1 |
| 2024 | 134,7 | 112,6 | 62,2 | 101,6 | 88,4 | 81,9 |
| 2025 | 137,1 | 115,6 | 63,5 | 100,7 | 89,2 | 82,8 |

**Saldo di bilancio, % PIL, media per periodo**

| Paese | 1970-79 | 1980-89 | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|---:|---:|
| IT | -6,9 | -10,8 | -7,4 | -3,2 | -2,7 | -6,7 |
| FR | -0,8 | -2,4 | -3,8 | -3,4 | -4,3 | -6,1 |
| DE | -1,7 | -2,2 | -3,4 | -2,5 | 0,2 | -2,9 |
| ES |  |  | -4,1 | -1,3 | -6,2 | -5,0 |
| EA |  |  | -3,8 | -2,6 | -2,6 | -4,2 |
| UE27 |  |  | -3,7 | -2,4 | -2,4 | -4,0 |
| IT - media FR/DE/ES |  |  | -0,5 | -0,8 | 0,7 | -2,0 |

**Saldo primario, % PIL, media per periodo**

| Paese | 1970-79 | 1980-89 | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|---:|---:|
| IT | -4,3 | -3,3 | 2,9 | 1,8 | 1,5 | -2,9 |
| FR | -0,1 | -0,2 | -0,6 | -0,5 | -2,1 | -4,3 |
| DE | -0,4 | 0,6 | -0,2 | 0,4 | 1,8 | -2,0 |
| ES |  |  | 0,3 | 0,8 | -3,5 | -2,7 |
| EA |  |  | 1,0 | 0,6 | -0,2 | -2,5 |
| UE27 |  |  | 1,1 | 0,6 | -0,1 | -2,4 |
| IT - media FR/DE/ES |  |  | 4,9 | 1,6 | 2,7 | 0,1 |

**Spesa per interessi, % PIL, media per periodo**

| Paese | 1970-79 | 1980-89 | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|---:|---:|
| IT | 2,7 | 7,5 | 10,3 | 5,0 | 4,2 | 3,7 |
| FR | 1,1 | 2,2 | 3,2 | 2,8 | 2,1 | 1,8 |
| DE | 1,3 | 2,7 | 3,2 | 2,8 | 1,6 | 0,8 |
| ES |  |  | 4,4 | 2,1 | 2,8 | 2,3 |
| EA |  |  | 4,8 | 3,2 | 2,4 | 1,7 |
| UE27 |  |  | 4,8 | 3,1 | 2,3 | 1,6 |
| IT - media FR/DE/ES |  |  | 5,4 | 2,4 | 2,0 | 2,1 |

**Spesa per interessi, % PIL, anni chiave**

| Anno | IT | FR | DE | ES | EA | UE27 |
|---|---:|---:|---:|---:|---:|---:|
| 1977 | 3,5 |  | 1,6 |  |  |  |
| 1991 | 11,3 | 2,8 | 2,7 |  |  |  |
| 1999 | 6,4 | 3,1 | 3,1 | 3,4 | 4,0 | 3,9 |
| 2007 | 4,7 | 2,7 | 2,7 | 1,6 | 2,9 | 2,7 |
| 2013 | 4,8 | 2,3 | 1,8 | 3,6 | 2,8 | 2,7 |
| 2019 | 3,3 | 1,5 | 0,8 | 2,3 | 1,6 | 1,5 |
| 2024 | 3,9 | 2,0 | 1,1 | 2,4 | 1,9 | 1,9 |
| 2025 | 3,9 | 2,2 | 1,1 | 2,4 | 1,9 | 1,9 |

**Pressione fiscale (OCSE), % PIL, media per periodo**

| Paese | 1970-79 | 1980-89 | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|---:|---:|
| IT | 24,9 | 32,6 | 39,1 | 40,3 | 42,5 | 42,2 |
| FR | 35,5 | 41,5 | 43,0 | 43,0 | 44,9 | 44,7 |
| DE | 34,7 | 36,0 | 35,5 | 34,9 | 37,1 | 38,2 |
| ES | 17,9 | 26,6 | 32,0 | 33,5 | 33,0 | 36,8 |
| IT - media FR/DE/ES | -4,5 | -2,1 | 2,2 | 3,1 | 4,1 | 2,3 |

**Pressione fiscale (AMECO), % PIL, media per periodo**

| Paese | 1970-79 | 1980-89 | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|---:|---:|
| IT |  |  | 40,5 | 40,0 | 42,2 | 42,2 |
| FR | 38,4 | 41,4 | 42,5 | 42,9 | 45,1 | 44,6 |
| DE |  |  | 39,3 | 38,2 | 38,8 | 40,1 |
| ES |  |  | 32,1 | 33,6 | 33,2 | 37,1 |
| EA |  |  | 39,7 | 38,7 | 39,8 | 40,2 |
| UE27 |  |  | 40,0 | 38,8 | 39,5 | 39,8 |
| IT - media FR/DE/ES |  |  | 2,0 | 1,7 | 3,2 | 1,6 |

**Spesa pubblica, % PIL, media per periodo**

| Paese | 1970-79 | 1980-89 | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|---:|---:|
| IT | 37,0 | 48,2 | 51,9 | 47,4 | 49,6 | 53,8 |
| FR | 45,8 | 50,9 | 54,1 | 54,2 | 57,4 | 58,4 |
| DE | 45,5 | 47,0 | 48,5 | 46,8 | 45,2 | 49,8 |
| ES |  |  | 41,9 | 39,7 | 44,3 | 47,2 |
| EA |  |  | 50,0 | 47,5 | 48,9 | 50,7 |
| UE27 |  |  | 50,3 | 47,6 | 48,5 | 50,1 |
| IT - media FR/DE/ES |  |  | 0,4 | 0,5 | 0,6 | 2,0 |

**Spesa pubblica, % PIL, anni chiave**

| Anno | IT | FR | DE | ES | EA | UE27 |
|---|---:|---:|---:|---:|---:|---:|
| 1977 | 38,5 |  | 49,0 |  |  |  |
| 1991 | 53,9 | 51,7 | 46,3 |  |  |  |
| 1999 | 47,1 | 53,7 | 48,5 | 39,9 | 48,1 | 48,4 |
| 2007 | 46,6 | 53,6 | 43,5 | 39,2 | 45,9 | 45,8 |
| 2013 | 50,9 | 58,6 | 45,2 | 46,2 | 50,3 | 50,0 |
| 2019 | 48,4 | 55,3 | 45,5 | 42,0 | 47,0 | 46,6 |
| 2024 | 50,4 | 57,0 | 49,4 | 45,5 | 49,4 | 49,1 |
| 2025 | 51,2 | 57,2 | 50,5 | 45,3 | 49,8 | 49,5 |

**Spesa per vecchiaia, % PIL, media per periodo**

| Paese | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|
| IT |  | 11,8 | 13,5 | 14,0 |
| FR | 10,9 | 11,4 | 13,4 | 13,5 |
| DE |  | 9,5 | 9,2 | 9,8 |
| ES | 6,6 | 6,2 | 8,8 | 10,4 |
| EA |  |  | 10,6 | 10,9 |
| UE27 |  |  | 10,4 | 10,6 |
| IT - media FR/DE/ES |  | 2,7 | 3,0 | 2,8 |

**Investimenti pubblici, % PIL, media per periodo**

| Paese | 1970-79 | 1980-89 | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|---:|---:|
| IT |  |  | 2,7 | 3,0 | 2,5 | 3,1 |
| FR | 4,0 | 4,4 | 4,5 | 4,4 | 4,2 | 4,2 |
| DE |  |  | 2,8 | 2,4 | 2,5 | 3,0 |
| ES |  |  | 3,9 | 4,3 | 2,7 | 2,8 |
| EA |  |  | 3,3 | 3,4 | 3,1 | 3,3 |
| UE27 |  |  | 3,3 | 3,5 | 3,2 | 3,5 |
| IT - media FR/DE/ES |  |  | -0,9 | -0,6 | -0,7 | -0,2 |

**Il grafico, a parole.** Il debito italiano sale da poco più del 50% del PIL alla fine degli anni Settanta al 119% nel 1995. Scende al 103,5% nel 2007, risale al 132% nel 2013, al 154% nel 2020 (pandemia) e torna al 137% nel 2025. Gli altri tre paesi partono molto più in basso (12-26% nel 1977); la Spagna arriva al 100% nel 2013 e la Francia lo supera nel 2020. Il deficit italiano è tra il 7% e il 12,4% del PIL fino al 1994, scende al 3% intorno al 1997 e ci resta (con oscillazioni) fino al 2019; nel 2020-23 torna tra il 7% e il 9,4%, poi scende intorno al 3% nel 2024-25. Il **saldo primario** (il bilancio senza gli interessi) è negativo fino al 1990, poi **positivo ogni anno dal 1992 al 2019, tranne il 2009**: negli anni Novanta e Duemila l'Italia ha l'avanzo primario più alto dei quattro paesi; negli anni Dieci è simile alla Germania. La spesa per interessi sta tra l'11% e il 12,7% del PIL nel 1991-1996 e scende a 3-5% dopo l'euro, ma resta il doppio della media degli altri.

**Rotture.**
- Saldo primario: rotture nel **1991** (da -3,3% a +3,3% in media), nel **2003** (avanzo più piccolo, +1,4%) e nel **2020** (-2,9%).
- Deficit: rotture nel **1983**, **1996** e **2020**.
- Interessi: calo a gradini dopo il **1997** e il **2003**.
- Pressione fiscale (serie OCSE, dal 1965): rottura nel **1992**. Prima del 1992 l'Italia era sotto la media dei tre paesi; dal 1998 è sopra di 2,5-4 punti. Era il 25,8% nel 1977, il 36,6% nel 1991, il 40,7% nel 1999, il 42-44% dal 2010.
- Spesa pubblica: rotture nel **1995**, **2009** e **2020**. Al netto degli interessi la spesa italiana è sempre sotto quella francese e, per quasi tutto il periodo, sotto la media dell'area euro (40% contro 48% nel 1995; 47,3% contro 47,9% nel 2025): la distanza si chiude dopo il 2008.
- Spesa per vecchiaia (in gran parte pensioni, dal 2001): sale di circa 2 punti di PIL con la crisi del **2009** (anche perché il PIL cala) e si stabilizza intorno al 13,5-14%; è la più alta dei quattro insieme alla Francia.
- Investimenti pubblici (dal 1995): l'Italia è quasi sempre sotto la media degli altri; scende al 2,1% nel 2018 (minimo della serie), poi risale al 3,6-3,8% nel 2024-26, sopra la Germania e la Spagna.

**Coincidenze da verificare.** Il passaggio all'avanzo primario nel 1991-92 coincide con la crisi della lira e le manovre di quegli anni; l'aumento della pressione fiscale nel 1992-93 con le stesse manovre (che comprendevano anche prelievi straordinari). Il calo degli interessi dal 1997 coincide con la convergenza verso l'euro. La salita degli investimenti pubblici dal 2021 coincide con il PNRR. La fiammata dei deficit 2020-23 coincide con la pandemia, la sospensione delle regole europee e i crediti d'imposta edilizi (che Eurostat contabilizza come spesa).

## 5. Disuguaglianza e povertà

**Gini reddito disponibile (OCSE), media per periodo**

| Paese | 1980-89 | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|---:|
| IT | 29,1 | 30,3 | 32,3 | 32,8 | 32,6 |
| FR |  | 27,9 | 28,8 | 30,6 | 29,3 |
| DE | 25,1 | 26,1 | 28,4 | 29,1 | 30,8 |
| ES |  |  | 32,4 | 33,7 | 31,9 |
| IT - media FR/DE/ES |  |  | 1,3 | 1,6 | 1,9 |

**Gini reddito disponibile (EU-SILC), media per periodo**

| Paese | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|
| IT | 32,1 | 32,6 | 32,1 |
| FR | 28,3 | 29,5 | 29,7 |
| DE | 28,5 | 29,6 | 29,9 |
| ES | 32,1 | 34,0 | 31,8 |
| UE27 |  | 30,5 | 29,7 |
| IT - media FR/DE/ES | 2,3 | 1,6 | 1,6 |

**Rischio di poverta' relativa, %, media per periodo**

| Paese | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|
| IT | 19,0 | 18,9 | 19,8 | 19,4 |
| FR | 15,0 | 13,2 | 13,6 | 15,3 |
| DE | 12,6 | 13,1 | 16,0 | 15,5 |
| ES | 18,8 | 19,6 | 21,3 | 20,4 |
| UE27 |  |  | 17,0 | 16,4 |
| IT - media FR/DE/ES | 3,5 | 3,5 | 2,8 | 2,4 |

**Poverta' assoluta individui, %, media per periodo**

| Paese | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|
| IT | 3,4 | 6,8 | 9,4 |
| Mezzogiorno | 4,8 | 9,2 | 12,0 |
| Nord | 2,6 | 5,5 | 8,5 |
| Centro | 2,6 | 5,8 | 7,4 |

**Poverta' assoluta individui, %, anni chiave**

| Anno | IT | Nord | Centro | Mezzogiorno |
|---|---:|---:|---:|---:|
| 2007 | 3,1 | 2,6 | 2,8 | 3,8 |
| 2013 | 7,3 | 5,5 | 5,9 | 10,6 |
| 2019 | 7,5 | 6,2 | 6,0 | 10,3 |
| 2024 | 9,8 | 8,8 | 7,6 | 12,5 |
| 2025 | 9,3 | 8,5 | 7,4 | 11,5 |

**Il grafico, a parole.** La disuguaglianza dei redditi in Italia (indice di Gini, 0 = tutti uguali, 100 = uno solo ha tutto) passa da circa 28-29 negli anni Ottanta a circa 33 dalla metà degli anni Novanta, e da allora è quasi ferma tra 31 e 33. È più alta che in Francia e Germania (28-30), simile alla Spagna. La quota di persone a rischio di povertà relativa (reddito sotto il 60% della mediana) è stabile intorno al 19-20% da trent'anni, 2-6 punti sopra Francia e Germania. La **povertà assoluta** (persone che non possono permettersi un paniere di beni essenziali, misura solo italiana) è invece più che raddoppiata: 3,3% nel 2005, 7,3% nel 2013, 9,8% nel 2024 e 9,3% nel 2025; cresce soprattutto al Nord dopo il 2013, anche se il livello più alto resta nel Mezzogiorno.

**Rotture.**
- Gini OCSE: il salto è tra il 1991 (27,9) e il 1995 (32,7); il test, con pochi anni prima del 2003, indica genericamente il 2005, ma il cambio di livello è chiaramente nei primi anni Novanta.
- Povertà assoluta: rottura nel **2012** (da una media del 3,6% a una dell'8,3%). Nel 2014 cambia anche il metodo ISTAT (nuova serie): i valori prima e dopo non sono del tutto confrontabili.

**Coincidenze da verificare.** Aumento della disuguaglianza 1992-95 con la crisi del 1992-93 e la fine della scala mobile; aumento della povertà assoluta con la doppia recessione 2008-2013 e l'inflazione del 2022-23 (che pesa di più sui beni essenziali). Il Reddito di cittadinanza (2019) coincide con un piccolo calo nel 2019, poi la pandemia; il passaggio all'Assegno di inclusione (2024) va verificato con i dati 2024-26.

## 6. Demografia e migrazioni

**Fecondita', figli per donna, media per periodo**

| Paese | 1970-79 | 1980-89 | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|---:|---:|
| IT | 2,14 | 1,45 | 1,25 | 1,34 | 1,37 | 1,22 |
| FR | 2,17 | 1,84 | 1,76 | 1,94 | 1,95 | 1,74 |
| DE | 1,58 | 1,40 | 1,32 | 1,35 | 1,49 | 1,46 |
| ES | 2,74 | 1,73 | 1,22 | 1,32 | 1,31 | 1,15 |
| EA | 2,08 | 1,64 | 1,44 | 1,50 | 1,55 | 1,44 |
| UE27 | 2,12 | 1,74 | 1,48 | 1,48 | 1,54 | 1,44 |
| IT - media FR/DE/ES | -0,02 | -0,20 | -0,19 | -0,20 | -0,21 | -0,23 |

**Fecondita', figli per donna, anni chiave**

| Anno | IT | FR | DE | ES | EA | UE27 |
|---|---:|---:|---:|---:|---:|---:|
| 1977 | 1,93 | 1,94 | 1,40 | 2,65 | 1,92 | 1,99 |
| 1991 | 1,30 | 1,75 | 1,33 | 1,33 | 1,49 | 1,58 |
| 1999 | 1,23 | 1,81 | 1,36 | 1,17 | 1,43 | 1,41 |
| 2007 | 1,39 | 1,98 | 1,37 | 1,38 | 1,54 | 1,51 |
| 2013 | 1,39 | 1,99 | 1,42 | 1,27 | 1,53 | 1,51 |
| 2019 | 1,27 | 1,86 | 1,54 | 1,23 | 1,51 | 1,53 |
| 2024 | 1,18 | 1,61 | 1,36 | 1,10 | 1,35 | 1,34 |

**Saldo migratorio per 1.000 ab., media per periodo**

| Paese | 1970-79 | 1980-89 | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|---:|---:|
| IT | -0,2 | -0,3 | 0,6 | 5,0 | 2,0 | 3,2 |
| FR | 1,4 | 0,9 | 0,4 | 2,3 | 0,6 | 3,4 |
| DE | 1,2 | 2,1 | 4,8 | 1,2 | 5,7 | 4,2 |
| ES | 0,2 | -0,4 | 3,2 | 12,0 | 1,4 | 10,4 |
| EA |  |  |  | 3,9 | 2,4 | 5,5 |
| UE27 | 0,5 | 0,4 | 1,5 | 2,5 | 1,9 | 4,6 |
| IT - media FR/DE/ES | -1,1 | -1,1 | -2,2 | -0,2 | -0,6 | -2,8 |

**Emigrati con cittadinanza, migliaia, media per periodo**

| Paese | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|
| IT |  | 39,5 | 89,9 | 113,1 |
| FR |  | 205,1 | 227,6 | 160,7 |
| DE | 116,4 | 141,0 | 132,8 | 140,9 |
| ES |  | 25,3 | 73,3 | 125,3 |
| IT - media FR/DE/ES |  | -89,0 | -54,7 | -28,4 |

**Il grafico, a parole.** Nel 1977 le donne italiane avevano in media 1,93 figli, come in Francia. Dieci anni dopo erano meno di 1,4; un primo minimo è 1,19 nel 1995, poi una piccola risalita fino a 1,44 nel 2008-2010 e un nuovo calo fino al minimo storico di **1,18 nel 2024**, tra i valori più bassi d'Europa (la Spagna è a 1,10). La Francia resta sempre sopra 1,6. Il saldo migratorio italiano è vicino a zero alla fine degli anni Settanta e negativo nel 1981-1987; diventa stabilmente positivo dal **1988**: l'Italia passa da paese di emigrazione a paese di immigrazione. Il picco degli ingressi netti è nel 2002-2008 (8-8,5 per mille abitanti nel 2003 e nel 2007, anche per le regolarizzazioni), poi un crollo fino a quasi zero nel 2015-2019 e una ripresa a 4-5 per mille nel 2022-2025. Intanto crescono gli **italiani che si cancellano per l'estero**: circa 35-45 mila l'anno nel 2002-2010, circa 95-122 mila l'anno dal 2015, **141 mila nel 2024** (109 mila nel 2025, dato provvisorio).

**Rotture.**
- Fecondità: rotture nel **1987**, **1994** e **2006**. Il divario con la media dei tre paesi è stabile (circa -0,2 figli per donna) dagli anni Ottanta.
- Saldo migratorio: rotture nel **1988**, **1996** e **2002**. Rispetto agli altri tre, l'Italia attira più persone nel 2007-2014 e meno dal **2015** (la Spagna e la Germania hanno avuto forti ingressi).
- Emigrazione di italiani: nessuna rottura secca, ma una salita continua dal **2011**: il numero triplica in dieci anni.

**Coincidenze da verificare.** Regolarizzazioni degli stranieri del 2002-03 e allargamento dell'Unione del 2004 e 2007 (Romania). Aumento delle partenze di italiani dal 2011 con la crisi del 2011-13 e la disoccupazione giovanile. Una parte delle cancellazioni riflette anche la regolarizzazione anagrafica di chi era già all'estero.

## 7. Istruzione

**Laureati 25-34, %, media per periodo**

| Paese | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|
| IT | 8,1 | 15,4 | 24,5 | 29,9 |
| FR | 25,3 | 38,3 | 44,5 | 51,8 |
| DE | 20,6 | 22,7 | 29,8 | 37,8 |
| ES | 26,9 | 38,4 | 41,9 | 50,5 |
| UE27 |  | 27,4 | 36,0 | 42,7 |
| IT - media FR/DE/ES | -16,2 | -17,7 | -14,2 | -16,8 |

**Laureati 25-34, %, anni chiave**

| Anno | IT | FR | DE | ES | UE27 |
|---|---:|---:|---:|---:|---:|
| 1999 | 10,0 | 29,8 | 21,5 | 32,3 |  |
| 2007 | 18,8 | 41,4 | 22,6 | 40,0 | 28,9 |
| 2013 | 22,9 | 43,9 | 29,9 | 41,1 | 35,2 |
| 2019 | 27,9 | 48,2 | 33,3 | 46,5 | 39,6 |
| 2024 | 31,6 | 53,1 | 39,1 | 52,6 | 43,9 |
| 2025 | 31,1 | 55,8 | 40,9 | 52,5 | 44,8 |

**Il grafico, a parole.** Nel 1999 solo il 10% dei 25-34enni italiani aveva una laurea o un titolo terziario, contro il 21-32% degli altri tre. Nel 2025 sono il 31%: la quota è triplicata, ma gli altri sono saliti ancora di più (Francia 56%, Spagna 52%, Germania 41%, UE27 45%). La distanza dalla media dei tre resta tra 14 e 19 punti per tutto il periodo.

**Rotture.** Accelerazione nel **1998-2004**. **Coincidenze da verificare**: riforma universitaria "3+2" (1999, in vigore dal 2001), che ha introdotto la laurea triennale; nel 2014 il passaggio alla classificazione ISCED 2011 crea un piccolo salto statistico in tutti i paesi.

## 8. Divario Nord-Sud

**PIL pc Mezzogiorno, % Centro-Nord, media per periodo**

| Paese | 1990-99 | 2000-09 | 2010-19 | 2020-25 |
|---|---:|---:|---:|---:|
| IT | 55,0 | 56,1 | 55,7 | 56,1 |

**PIL pc Mezzogiorno, % Centro-Nord, anni chiave**

| Anno | IT |
|---|---:|
| 1999 | 55,5 |
| 2007 | 56,4 |
| 2013 | 56,3 |
| 2019 | 54,9 |
| 2024 | 56,9 |

**Il grafico, a parole.** Il PIL per abitante del Mezzogiorno è poco più della metà di quello del Centro-Nord e non si muove da trent'anni: 54,8% nel 1995, 56,4% nel 2007, 54,7% nel 2018 (minimo recente), 56,9% nel 2024. Le oscillazioni sono di uno-due punti e in parte "meccaniche": nelle crisi il Centro-Nord, più legato all'industria e all'export, perde di più (2009), e il rapporto sale senza che il Sud stia meglio. Il test indica un cambio nel 2014, ma con differenze di pochi decimi: nella sostanza la serie è piatta.

**Coincidenze da verificare.** La lieve risalita dal 2019 coincide con i maggiori trasferimenti e investimenti pubblici (decontribuzione Sud dal 2020, PNRR con quota minima del 40% al Mezzogiorno) e con il calo della popolazione del Sud (meno abitanti a parità di prodotto alzano il pro capite).

---

## Cosa non sappiamo (e dove le serie sono deboli)

- **Conti pubblici prima del 1995.** AMECO (definizioni europee attuali) parte dal 1995 per Italia e Spagna e dal 1991 per la Germania. Prima, per Italia e Germania Ovest, usiamo la banca dati storica del FMI (*Public Finances in Modern History*): al punto di giunzione ci sono scarti di 0,2-2 punti di PIL. Per la **Spagna prima del 1995** e la **Francia prima del 1978** quella banca dati riporta solo lo Stato centrale (per esempio, spesa francese 1977 al 21% del PIL): non è confrontabile e abbiamo lasciato le celle vuote. Per questo la riga "IT - media FR/DE/ES" dei conti pubblici parte dal 1995.
- **Investimenti pubblici prima del 1995** (Italia, Spagna, Germania) e **pressione fiscale AMECO prima del 1995**: non scaricati da fonte omogenea. La pressione fiscale lunga è coperta dalla serie OCSE (dal 1965), che usa una definizione un po' diversa da quella ISTAT (le differenze sono di qualche decimo).
- **Spesa per pensioni**: la serie europea per funzione (COFOG, "vecchiaia") per l'Italia parte dal 2001. Serie più lunghe esistono (Ragioneria generale dello Stato, INPS, OCSE SOCX dal 1980) ma non sono state ancora integrate. La voce "vecchiaia" non coincide con la "spesa pensionistica" dei documenti italiani (che include anche invalidità e superstiti).
- **Disuguaglianza prima del 1984**: la Banca d'Italia (Indagine sui bilanci delle famiglie) ha dati dal 1977 ma vanno calcolati dai microdati; non è stato fatto. La serie OCSE ha anni sparsi prima del 2003 e cambia definizione di reddito nel 2012.
- **Povertà assoluta**: esiste solo per l'Italia, parte dal 2005 e ha una rottura di metodo nel 2014. Per il confronto internazionale c'è solo la povertà relativa (EU-SILC dal 2003-04, ECHP 1995-2001).
- **Emigrazione di italiani prima del 2002**: le tavole storiche ISTAT esistono ma non sono nel servizio dati usato. Le cancellazioni anagrafiche **sottostimano** le partenze reali (molti non si cancellano subito). Per Francia, Germania e Spagna i dati Eurostat partono tra il 1998 e il 2006 e non sono perfettamente confrontabili.
- **Laureati 25-34**: dal 1992; prima non c'è una serie armonizzata.
- **Divario Nord-Sud prima del 1995**: le ricostruzioni di lungo periodo (SVIMEZ, Banca d'Italia, studi storici) non sono disponibili come dati scaricabili; il divario era intorno al 55-60% anche negli anni Settanta-Ottanta secondo la letteratura, ma non lo inseriamo senza una tabella ufficiale.
- **Area euro e UE27**: gli aggregati partono in genere dal 1995 (dal 2002 per i tassi); per l'UE27 il PIL pro capite a parità di potere d'acquisto è 100 per costruzione.
- **Germania**: prima del 1991 sono dati della Germania Ovest; la riunificazione crea salti in livelli (debito, spesa nel 1995 per il trasferimento dei debiti della Treuhand).
- **Revisioni**: i conti nazionali vengono rivisti; rilanciando gli script tra qualche mese alcuni valori recenti cambieranno. Il 2026 è una previsione.
- **Causalità**: le coincidenze tra rotture e decisioni non dimostrano un effetto. Molti cambiamenti (euro, Cina, crisi globali, invecchiamento) colpiscono tutti i paesi insieme; per questo guardiamo soprattutto la **distanza** dell'Italia dagli altri.


## Appendice: tutte le rotture stimate

Fonte: `storia/serie/_rotture.csv`, prodotto da `analisi.py`. "media" = rottura nella media; "tendenza" = rottura nella retta di tendenza. Medie per tratto con i valori della serie.

| Indicatore | Serie | Test | Anni di rottura | Medie per tratto |
|---|---|---|---|---|
| `pil_reale_crescita` | IT | media | nessuna | 1977-2025: 1,3 |
| `pil_reale_crescita` | IT - media FR/DE/ES | media | 1988 2020 | 1977-1987: 0,3; 1988-2019: -1,1; 2020-2025: 0,2 |
| `pil_pro_capite_crescita` | IT | media | nessuna | 1977-2025: 1,2 |
| `pil_pro_capite_crescita` | IT - media FR/DE/ES | media | nessuna | 1977-2025: -0,3 |
| `pil_pro_capite_pps_ue27` | IT | tendenza | 2004 2014 | 1995-2003: 122,7; 2004-2013: 107,5; 2014-2025: 96,8 |
| `pil_pro_capite_pps_ue27` | IT - media FR/DE/ES | tendenza | 2014 | 1995-2013: 3,1; 2014-2025: -8,0 |
| `produttivita_oraria_crescita` | IT | media | 2001 | 1977-2000: 1,9; 2001-2025: -0,0 |
| `produttivita_oraria_crescita` | IT - media FR/DE/ES | media | nessuna | 1977-2025: -0,6 |
| `occupazione_15_64` | IT | tendenza | 2000 2010 | 1977-1999: 52,5; 2000-2009: 56,9; 2010-2025: 58,3 |
| `occupazione_15_64` | IT - media FR/DE/ES | tendenza | 1986 | 1977-1985: -6,6; 1986-2025: -7,7 |
| `occupazione_femminile_15_64` | IT | tendenza | 2001 2009 2020 | 1977-2000: 35,0; 2001-2008: 44,6; 2009-2019: 47,6; 2020-2025: 51,5 |
| `occupazione_femminile_15_64` | IT - media FR/DE/ES | tendenza | 1988 | 1977-1987: -9,2; 1988-2025: -12,5 |
| `disoccupazione` | IT | tendenza | 2001 2007 2013 | 1977-2000: 9,3; 2001-2006: 8,4; 2007-2012: 8,1; 2013-2025: 9,8 |
| `disoccupazione` | IT - media FR/DE/ES | tendenza | 1986 | 1977-1985: -0,9; 1986-2025: -1,0 |
| `disoccupazione_giovanile` | IT | tendenza | 1988 2006 2012 | 1977-1987: 29,1; 1988-2005: 29,9; 2006-2011: 24,3; 2012-2025: 31,3 |
| `disoccupazione_giovanile` | IT - media FR/DE/ES | tendenza | 2013 | 1977-2012: 9,4; 2013-2025: 9,2 |
| `inflazione` | IT | media | 1986 1997 | 1977-1985: 14,9; 1986-1996: 5,3; 1997-2025: 2,0 |
| `inflazione` | IT - media FR/DE/ES | media | 1986 1997 | 1977-1985: 5,2; 1986-1996: 1,7; 1997-2025: 0,1 |
| `debito_pil` | IT | tendenza | 1999 | 1977-1998: 85,6; 1999-2025: 123,3 |
| `debito_pil` | IT - media FR/DE/ES | tendenza | 1997 | 1977-1996: 45,6; 1997-2025: 46,6 |
| `deficit_pil` | IT | media | 1983 1996 2020 | 1977-1982: -8,6; 1983-1995: -10,7; 1996-2019: -3,1; 2020-2025: -6,7 |
| `deficit_pil` | IT - media FR/DE/ES | media | nessuna | 1995-2025: -0,5 |
| `saldo_primario_pil` | IT | media | 1991 2003 2020 | 1977-1990: -3,3; 1991-2002: 3,3; 2003-2019: 1,4; 2020-2025: -2,9 |
| `saldo_primario_pil` | IT - media FR/DE/ES | media | 2017 | 1995-2016: 2,9; 2017-2025: 0,5 |
| `interessi_pil` | IT | tendenza | 1997 2003 | 1977-1996: 8,3; 1997-2002: 6,8; 2003-2025: 4,2 |
| `interessi_pil` | IT - media FR/DE/ES | tendenza | 2001 | 1995-2000: 5,0; 2001-2025: 2,2 |
| `pressione_fiscale_ocse` | IT | tendenza | 1992 | 1977-1991: 31,7; 1992-2024: 41,1 |
| `pressione_fiscale_ocse` | IT - media FR/DE/ES | tendenza | 1998 2008 | 1977-1997: -1,0; 1998-2007: 2,6; 2008-2024: 3,7 |
| `pressione_fiscale` | IT | tendenza | nessuna | 1995-2025: 41,2 |
| `pressione_fiscale` | IT - media FR/DE/ES | tendenza | 2008 | 1995-2007: 1,5; 2008-2025: 2,7 |
| `spesa_pubblica_pil` | IT | tendenza | 1995 2009 2020 | 1977-1994: 48,5; 1995-2008: 47,8; 2009-2019: 49,7; 2020-2025: 53,8 |
| `spesa_pubblica_pil` | IT - media FR/DE/ES | tendenza | nessuna | 1995-2025: 0,8 |
| `spesa_pensioni_pil` | IT | tendenza | 2009 | 2001-2008: 11,6; 2009-2024: 13,6 |
| `spesa_pensioni_pil` | IT - media FR/DE/ES | tendenza | 2009 | 2001-2008: 2,6; 2009-2024: 2,9 |
| `investimenti_pubblici_pil` | IT | tendenza | 2013 2019 | 1995-2012: 2,9; 2013-2018: 2,3; 2019-2025: 3,0 |
| `investimenti_pubblici_pil` | IT - media FR/DE/ES | tendenza | nessuna | 1995-2025: -0,6 |
| `tasso_lungo` | IT | media | 1985 1997 2014 | 1977-1984: 16,2; 1985-1996: 11,9; 1997-2013: 4,8; 2014-2025: 2,5 |
| `tasso_lungo` | IT - media FR/DE/ES | media | 1984 1997 2011 | 1978-1983: 4,5; 1984-1996: 2,8; 1997-2010: 0,3; 2011-2025: 1,3 |
| `spread_bund` | IT | media | 1986 1996 2010 | 1977-1985: 803; 1986-1995: 486; 1996-2009: 63; 2010-2025: 191 |
| `spread_bund` | IT - media FR/DE/ES | media | 1997 2011 | 1978-1996: 198; 1997-2010: 26; 2011-2025: 92 |
| `gini_reddito_disponibile` | IT | tendenza | nessuna | 2004-2025: 32,4 |
| `gini_reddito_disponibile` | IT - media FR/DE/ES | tendenza | nessuna | 2005-2025: 1,8 |
| `gini_ocse` | IT | tendenza | 2005 | 1984-2004: 31,5; 2005-2023: 32,5 |
| `rischio_poverta` | IT | tendenza | nessuna | 1995-2025: 19,3 |
| `rischio_poverta` | IT - media FR/DE/ES | tendenza | nessuna | 1995-2025: 3,0 |
| `poverta_assoluta` | IT | tendenza | 2012 | 2005-2011: 3,6; 2012-2025: 8,3 |
| `fecondita` | IT | tendenza | 1987 1994 2006 | 1977-1986: 1,60; 1987-1993: 1,31; 1994-2005: 1,25; 2006-2024: 1,34 |
| `fecondita` | IT - media FR/DE/ES | tendenza | nessuna | 1977-2024: -0,20 |
| `saldo_migratorio` | IT | media | 1988 1996 2002 | 1977-1987: -0,2; 1988-1995: 0,4; 1996-2001: 0,8; 2002-2025: 3,6 |
| `saldo_migratorio` | IT - media FR/DE/ES | media | 2007 2015 | 1977-2006: -1,6; 2007-2014: 2,4; 2015-2025: -2,9 |
| `emigrazione_cittadini` | IT | tendenza | nessuna | 2002-2025: 78,9 |
| `emigrazione_cittadini` | IT - media FR/DE/ES | tendenza | nessuna | 2006-2024: -55,0 |
| `laureati_25_34` | IT | tendenza | 1998 2004 | 1992-1997: 7,6; 1998-2003: 11,0; 2004-2025: 24,2 |
| `laureati_25_34` | IT - media FR/DE/ES | tendenza | 2001 2007 2019 | 1993-2000: -16,5; 2001-2006: -18,6; 2007-2018: -14,5; 2019-2025: -16,5 |
| `divario_nord_sud` | IT | tendenza | 2014 | 1995-2013: 55,9; 2014-2024: 55,7 |

## Come rifare tutto

```
python storia/script/esegui_tutto.py          # usa i file già scaricati (storia/script/_cache/)
python storia/script/esegui_tutto.py --nuovo  # riscarica tutto dalle fonti
```

Script: `scarica_ameco_fmi_ocse.py` (PIL, produttività, disoccupazione, inflazione, conti pubblici, tassi), `scarica_eurostat.py` (Gini, povertà relativa, laureati, pensioni, emigrazione, Nord-Sud), `scarica_ocse_bm.py` (occupazione, disoccupazione giovanile, fecondità, saldo migratorio), `scarica_istat_gini.py` (povertà assoluta, emigrazione di italiani, Gini OCSE), `analisi.py` (medie per decennio, rotture, tabelle). Requisiti: Python 3.10+, `requests`, `pandas`, `numpy`.

*Dati scaricati il 16 novembre 2026. Edizione AMECO: primavera 2026.*
