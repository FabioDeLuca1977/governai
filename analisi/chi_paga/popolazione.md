*Bozza scritta da un agente AI il 16 novembre 2026; da valutare con il panel; non rivista da una persona.*

# Chi paga: quante persone, quanto reddito, quanta imposta, gruppo per gruppo

**Domanda.** Quali gruppi riescono a tenere il proprio reddito fuori dall'imposta progressiva (holding, rendite, regimi sostitutivi)? E quanto pesano e quanto pagano dipendenti, pensionati, partite IVA e soci di società di persone, che "pagano già tanto"?

**Cosa c'è qui.** I numeri ufficiali su quante persone ci sono in ogni gruppo, quanto reddito dichiarano e quanta imposta pagano. Le aliquote "di legge" per caso tipo le calcola un altro lavoro (`analisi/chi_paga/calcola.py`). I dati per gruppo sono in `analisi/chi_paga/popolazione.csv`. Non ripetiamo quanto già scritto in `benchmark/equita_fiscale_diagnosi.md` (canali legali, esperienze estere) e in `benchmark/patrimoniale_studio.md` (ricchezza).

**Convenzioni.** Anno d'imposta 2024 (dichiarazioni presentate nel 2025), salvo diversa indicazione. "Medio" vuol dire diviso per tutte le persone del gruppo, comprese quelle con imposta zero. "Aliquota sul dichiarato" = imposta netta IRPEF / reddito complessivo dichiarato. "n.d." = dato non disponibile da fonte ufficiale. "Stima GovernAI" = nostro calcolo su dati ufficiali.

---

## 1. In breve

1. **L'IRPEF la pagano soprattutto dipendenti e pensionati, perché sono quasi tutti.** Sono 36,6 milioni su 42,8 milioni di contribuenti (85,5%) e versano l'**84,8%** dell'IRPEF netta (197,4 mld). La loro aliquota media sul dichiarato è del **18-19%**.
2. **Dentro l'IRPEF, chi dichiara di più paga di più.** Il top 5% (sopra 61.431 euro) paga il 30,4% di quanto dichiara; chi dichiara oltre 300.000 euro il **38,1%**. Professionisti in regime ordinario (28,8%) e soci di società di persone (23,7%) pagano in proporzione **più** dei dipendenti, *su ciò che dichiarano*.
3. **Il problema è quello che l'IRPEF non vede.** Dividendi, interessi, plusvalenze, affitti a cedolare e reddito dei forfettari pagano imposte piatte (26%, 12,5%, 21%, 15%) fuori dall'IRPEF. Nell'IRPEF entrano appena **0,66 mld** di redditi di capitale, contro circa **25,7 mld** di dividendi tassati alla fonte con la ritenuta del 26% (stima GovernAI dal gettito). E gli utili lasciati nelle società o incassati da una holding (imposta 1,2%) non compaiono da nessuna parte.
4. **Quando si contano tutte le imposte e tutti i redditi, il sistema diventa regressivo in cima.** Le stime accademiche (dati 2015) trovano un'aliquota effettiva che sale fino al **93°-95° percentile** e poi scende: il top 0,1% paga il **32,6%**, contro una media di tutta la popolazione del **46,1%** (Dalle Luche, Guzzardi, Palagi, Roventini, Santoro 2026).
5. **Chi può scegliere la forma del reddito paga meno. Chi ha la ritenuta alla fonte non evade.** Per i dipendenti l'evasione stimata è dell'**1,6-2,3%** dell'imposta; per l'IRPEF di autonomi e imprese è del **59,7%**; per i forfettari del **41,4%** (2019). Sono due problemi diversi: **evasione** concentrata nel lavoro autonomo e nella piccola impresa; **elusione legale** concentrata nei grandi redditi da capitale.

---

## 2. Chi c'è in ogni gruppo e quanto paga (IRPEF, anno d'imposta 2024)

Fonte: MEF, Dipartimento delle Finanze (DF), [statistiche per reddito prevalente](https://www1.finanze.gov.it/finanze/analisi_stat/public/index.php?tree=2025AETPTOT040001), [regimi agevolati](https://www1.finanze.gov.it/finanze/analisi_stat/public/index.php?tree=2025ABPFMIN020101), [Analisi dei dati IRPEF 2024](https://www1.finanze.gov.it/finanze/analisi_stat/public/v_4_0_0/contenuti/analisi_dati_2024_irpef.pdf). Ogni persona è messa nel gruppo del suo reddito **più grande** ("reddito prevalente").

| Gruppo | Persone | Reddito dichiarato medio | Imposta netta media | Aliquota sul dichiarato | Quota dell'IRPEF | Evasione stimata (tipo di reddito) |
|---|---|---|---|---|---|---|
| Dipendenti | 23.072.978 | 25.862 € | 4.612 € | 17,8% | **53,9%** | 1,6-2,3% |
| Pensionati | 13.534.816 | 24.256 € | 4.503 € | 18,6% | **30,9%** | n.d. (ritenuta alla fonte) |
| Professionisti e autonomi in regime ordinario | 343.618 | 101.876 € | 29.344 € | **28,8%** | 5,1% | 59,7% |
| Soci di società di persone (snc, sas) | 892.638 | 41.028 € | 9.711 € | 23,7% | 4,4% | 59,7% |
| Imprenditori individuali (ordinari e semplificati) | 861.423 | 37.829 € | 8.001 € | 21,2% | 3,5% | 59,7% |
| Proprietari con reddito prevalente da fabbricati | 1.524.560 | 10.074 € | 1.860 € | 18,5% | 1,4% | 8,6% (affitti) |
| **Forfettari** (imposta sostitutiva, fuori IRPEF) | 1.996.469 | 17.189 € (reddito netto forfetario) | 1.899 € | **11,9%** | fuori IRPEF (3,79 mld) | **41,4%** (2019) |
| **Cedolare secca** (solo il canone; si sovrappone agli altri gruppi) | circa 3,3 mln | 7.091 € di canone | 1.242 € | 17,5% | fuori IRPEF (4,1 mld) | 8,6% |
| **Soci di società di capitali** (dividendi) | n.d. | n.d. | n.d. | 26% sul dividendo | fuori IRPEF (6,70 mld di ritenute, 2025) | n.d. (IRES delle società: 19,8%) |
| **Redditi da capitale e plusvalenze** | n.d. | n.d. | n.d. | 26% / 12,5% | fuori IRPEF (27,6 mld di sostitutive, 2025) | n.d. |

**Come leggere la tabella.**
- **Il reddito delle partite IVA non è confrontabile uno a uno con quello dei dipendenti.** I dipendenti dichiarano al netto dei contributi; gli autonomi al lordo (in media circa 10.926 euro di contributi). Il reddito dei forfettari è già al netto di costi forfettari e contributi.
- **Dipendenti e pensionati "pagano tanto" soprattutto in totale**, non in aliquota: 18-19% su un reddito medio di circa 25.000 euro. In aliquota pagano di più i professionisti ordinari (28,8%), perché dichiarano redditi più alti e l'IRPEF è progressiva.
- **Le partite IVA in regime ordinario pagano molto su quello che dichiarano**, ma secondo il MEF una parte grande del loro reddito non viene dichiarata: per l'IRPEF di autonomi e imprese il gap è il **59,7%** dell'imposta dovuta (2023). Le due cose sono vere insieme: chi dichiara tutto paga molto; in media, molti non dichiarano tutto.
- **Chi non paga IRPEF.** 8,7 milioni hanno imposta netta zero (il 63,3% sono dipendenti e pensionati a reddito basso, per le detrazioni); 11,3 milioni contando anche chi riceve il trattamento integrativo.
- I **forfettari** pagano l'**11,9%** del loro reddito netto. A parità di reddito, un dipendente o un professionista ordinario paga molto di più: è il "gradino" già trattato dalla scheda SF02.
- **Società di persone e di capitali sono trattate in modo diverso.** L'utile di una snc va ai soci e paga l'IRPEF progressiva *subito*, che venga distribuito o no. L'utile di una srl paga il 24% di IRES. Poi paga il 26% solo se e quando viene distribuito a una persona, oppure l'1,2% se lo incassa una holding. Questo è il cuore della domanda di partenza: **chi lavora in forma di snc non può rinviare; chi tiene gli utili in una srl o in una holding sì.**

---

## 3. Per livello di reddito (IRPEF, anno d'imposta 2024)

Fonte: DF, IRPEF per [classi di reddito](https://www1.finanze.gov.it/finanze/analisi_stat/public/index.php?tree=2025AAPFTOT020602) e per [ventili](https://www1.finanze.gov.it/finanze/analisi_stat/public/index.php?tree=2025AAPFTOT020603).

| Gruppo | Persone | Soglia di ingresso | Reddito medio | Imposta media | Aliquota sul dichiarato | Quota del reddito | Quota dell'IRPEF |
|---|---|---|---|---|---|---|---|
| Metà inferiore (ventili I-X) | 20,3 mln | — (fino a 21.195 €) | n.d. | n.d. | n.d. | 19,6% | **7,5%** |
| Top 5% | 2,14 mln | 61.431 € | 112.807 € | 34.286 € | 30,4% | 22,4% | **37,2%** |
| Top 1% (stima GovernAI) | circa 428.000 | circa 130.000 € | circa 230.000 € | circa 78.800 € | circa 34,3% | circa 9,2% | circa **17,1%** |
| Oltre 300.000 € (0,14%, vicino al top 0,1%) | 58.939 | 300.000 € | 582.185 € | 221.765 € | **38,1%** | 3,2% | 6,6% |

Il top 1% è stimato per interpolazione lineare dentro la classe 120.000-150.000 euro. Il top 0,1% esatto (circa 42.800 persone) non si può separare nelle tabelle pubblicate: la classe "oltre 300.000 euro" è la migliore approssimazione.

**Lettura.** Sui redditi che dichiara, l'IRPEF è **fortemente progressiva**: chi sta in cima paga di più in proporzione e porta una quota dell'imposta molto più grande della sua quota di reddito. L'UPB conferma che le riforme IRPEF degli ultimi 35 anni hanno più che raddoppiato la capacità redistributiva dell'imposta sui dipendenti privati (indice di redistribuzione da 0,028 a 0,065; [UPB, Nota di lavoro n. 1/2026](https://www.upbilancio.it/it/nota-di-lavoro-n-1-2026-la-dinamica-retributiva-e-il-ruolo-dellimposta-sul-reddito-delle-persone-fisiche/), via [Il Foglio](https://www.ilfoglio.it/economia/2026/07/22/news/le-riforme-dellirpef-hanno-aiutato-i-redditi-bassi-lo-studio-dellupb--402864)). **Ma l'IRPEF guarda solo una parte del reddito di chi sta in cima** (sezione 4).

**Chi c'è sopra 300.000 euro (reddito che entra nell'IRPEF).** 47% lavoro dipendente (dirigenti e manager), 19% lavoro autonomo, 15% partecipazione in società di persone, 4,5% impresa in contabilità ordinaria, 2,4% impresa semplificata, 2,2% fabbricati, **0,9% redditi di capitale**. Per l'IRPEF i "ricchi" sono soprattutto dirigenti e professionisti, cioè chi ha redditi che **non può spostare** fuori dall'imposta progressiva.

---

## 4. Dove l'imposta "vede" il reddito e dove no

| Reddito | Come è tassato | Lo vede l'IRPEF? | Quanto vale (gettito) | Fonte |
|---|---|---|---|---|
| Lavoro dipendente e pensioni | IRPEF progressiva 23-43% più addizionali, ritenuta alla fonte | Sì, tutto | ritenute 2025: 190,5 mld (privato 96,7, pubblico 93,7) | [Bollettino entrate n. 286](https://www.astrid-online.it/static/upload/boll/bollettino-entrate-dicembre2025.pdf) |
| Lavoro autonomo e impresa ordinaria, soci di snc e sas | IRPEF progressiva, per trasparenza | Sì, quello dichiarato | autonomi: ritenute 15,0 mld (2025) | idem |
| Forfettari | 15% (5% per chi inizia) | **No** | 3,79 mld (a.i. 2024) | DF |
| Affitti a cedolare | 21%, 10%, 26% | **No** | 4,69 mld (2025) | Bollettino |
| Dividendi a persone fisiche | 26% alla fonte | **No** (salvo pochi casi, 0,66 mld in tutto nell'IRPEF) | 6,70 mld (2025) | Bollettino; DF |
| Interessi, cedole, altri redditi di capitale | 26% o 12,5% | **No** | 21,06 mld (2025) | Bollettino |
| Plusvalenze e redditi di capitale (risparmio amministrato e gestito) | 26% o 12,5%, solo alla vendita | **No** (solo 18 mln nell'IRPEF) | 6,58 mld (2025; +98% sul 2024) | Bollettino; DF |
| **Utili trattenuti nelle società** | IRES 24% | **No**, e nemmeno le sostitutive | IRES 2025: 60,1 mld (tutte le società) | Bollettino |
| **Dividendi e plusvalenze incassati da una holding** | 95% esente: circa 1,2% | **No** | **n.d.** | — |
| Attività all'estero | IVAFE 0,2% sul valore, IVIE | Solo i redditi, se dichiarati | IVAFE 0,10 mld; IVIE 0,15 mld (a.i. 2024) | [DF, quadro RW](https://www1.finanze.gov.it/finanze/analisi_stat/public/index.php?tree=2025AETPTOT050001) |

**Che cosa vuol dire.** Le statistiche IRPEF misurano bene chi vive di stipendio, pensione o lavoro autonomo. Misurano male chi vive di capitale: i dividendi, gli interessi, le plusvalenze e soprattutto gli utili che restano nelle società o nelle holding non compaiono. Per questo la classe "oltre 300.000 euro" sembra pagare il 38%: è fatta in gran parte di dirigenti e professionisti, e chi vive di rendite finanziarie può dichiarare all'IRPEF un reddito basso o nullo.

Un segnale: le **5.962 persone** il cui reddito IRPEF prevalente è "da capitale" dichiarano in media, tra chi le ha, **3,5 milioni** di attività finanziarie estere e **5,2 milioni** di conti esteri ([DF, quadro RW](https://www1.finanze.gov.it/finanze/analisi_stat/public/index.php?tree=2025AETPTOT050001)). In tutto, 297.765 persone dichiarano **150,3 mld** di attività finanziarie all'estero.

---

## 5. Le prove sulle aliquote effettive per percentile (tutte le imposte)

Le statistiche ufficiali non sommano IRPEF, imposte sostitutive, IRES sugli utili delle società possedute, IVA e contributi per persona. Lo fanno solo gli studi accademici sui **conti nazionali distributivi**, che ripartiscono tutto il reddito nazionale e tutte le imposte fra gli adulti.

| Studio | Dati | Risultato principale | Punto di svolta |
|---|---|---|---|
| Guzzardi, Palagi, Roventini, Santoro, *Reconstructing Income Inequality in Italy*, **JEEA** 22(5), 2024, pp. 2180-2224 ([doi](https://doi.org/10.1093/jeea/jvad073); [IDEAS](https://ideas.repec.org/a/oup/jeurec/v22y2024i5p2180-2224..html)) | 2004-2015 | Sistema poco progressivo fino al 95° percentile, **regressivo per il top 5%**; regressivo in tutta la distribuzione se si ordinano le persone per ricchezza netta; top 0,1% al **36%** | **95° percentile** |
| Dalle Luche, Guzzardi, Palagi, Roventini, Santoro, *Tackling the regressivity of the Italian tax system*, LEM WP 2024/26, versione maggio 2026 ([pdf](https://www.lem.sssup.it/WPLem/files/2024-26.pdf)) | 2015, con rendimenti della ricchezza diversi per livello (conti BCE) | Rendimento medio della ricchezza **2,5%** per il 90% più povero, **5%** per il 10% più ricco; top 0,1% al **32,6%**; aliquota media di tutta la popolazione **46,1%**; regressività dal **93° percentile** | **93° percentile** |

**Perché in cima si paga meno** (sintesi degli autori, verificata sul testo del LEM WP 2024/26):
1. l'**IRPEF è l'unica imposta progressiva**, e in cima pesa meno perché una quota più grande del reddito arriva dal capitale;
2. i **redditi da capitale** pagano aliquote piatte più basse delle aliquote marginali sul lavoro;
3. i **contributi sociali** hanno un tetto e non si pagano sul capitale;
4. **IVA e imposte sui consumi** pesano di più su chi consuma tutto il reddito, cioè in basso.

**Soglie 2015 in euro per adulto** (reddito nazionale lordo, dallo stesso studio): 25° percentile 8.082; 40° 17.192; 60° 29.950; 80° 46.321; 90° 62.704; 99,9° **523.150**.

**I limiti, detti chiaramente.** Sono stime accademiche, non statistiche ufficiali, su dati **2015**. Gli autori scrivono che le riforme successive (scaglioni IRPEF, flat tax per gli autonomi, tassazione del capitale) probabilmente non cambiano il risultato, e che anzi la regressività in cima potrebbe essere aumentata (LEM WP 2024/26, nota 19 e appendice D). Il risultato dipende da come si attribuiscono alle persone gli utili trattenuti nelle società.

**Su scala mondiale**, l'EU Tax Observatory stima che i miliardari paghino in imposte personali lo **0-0,5%** del proprio patrimonio l'anno, soprattutto grazie alle holding ([Global Tax Evasion Report 2024](https://halshs.archives-ouvertes.fr/halshs-04563948v1/file/global_tax_evasion_report_24.pdf); già in `benchmark/equita_fiscale_diagnosi.md`). Non c'è una stima pubblicata specifica per l'Italia.

---

## 6. Evasione per tipo di reddito (MEF, Relazione 2026, anno 2023)

Fonte: MEF, *Relazione sull'economia non osservata e sull'evasione fiscale e contributiva 2026*, tab. I.2, I.5, III.1.1.3 e box III.1.1.2 (testo in `dati/raw/01_mef_relazione_evasione_2026.txt`).

| Reddito tipico | Propensione all'evasione (gap / imposta dovuta) |
|---|---|
| Lavoro dipendente (solo lavoro irregolare) | **1,6-2,3%** |
| Addizionali locali del lavoro dipendente | 4,4-5,8% |
| Non titolari di partita IVA: imposta dichiarata e non versata | 0,5% |
| Affitti (cedolare e IRPEF) | 8,6% |
| IRES (società) | 19,8% |
| **IRPEF lavoro autonomo e impresa** | **59,7%** (55,1% non dichiarato, 4,6% non versato) |
| **Forfettari** (ultimo anno stimato: 2019) | **41,4%** (57-58% negli anni 2015-2018) |
| Pensioni, redditi da capitale | n.d. (ritenuta alla fonte; nessuna stima separata) |

La ritenuta alla fonte quasi elimina l'evasione. Dove manca, l'evasione è alta.

---

## 7. Cosa non sappiamo

1. **Quante holding personali esistono** e quanto incassano ogni anno in dividendi e plusvalenze esenti al 95%. Il DF ha i dati (quadro RF del modello Redditi SC) ma non li pubblica per tipo di società e di socio. **n.d.**
2. **Quante persone ricevono dividendi e quanto** ciascuna: le ritenute del 26% sono anonime. Si sa solo il gettito (6,70 mld nel 2025). **n.d.**
3. **La distribuzione per persona di interessi e plusvalenze** (27,6 mld di sostitutive nel 2025). **n.d.**
4. **Il top 0,1% esatto nelle statistiche IRPEF**: le tabelle si fermano alla classe "oltre 300.000 euro".
5. **Un'aliquota effettiva ufficiale per percentile** che sommi IRPEF, sostitutive, quota di IRES e utili trattenuti. Esistono solo stime accademiche su dati 2015.
6. **I ricavi medi dei forfettari**: le tabelle DF pubblicate danno il reddito netto (17.189 euro in media), non i ricavi.
7. **La composizione del reddito per decile da fonte ufficiale recente.** Per la ricchezza, la Banca d'Italia (conti distributivi, fine 2025) dà al 10% più ricco il 60,6% della ricchezza netta, soprattutto in attività finanziarie e partecipazioni (vedi `benchmark/patrimoniale_studio.md`). Per il reddito per decile e per fonte non abbiamo trovato una tavola ufficiale recente.
8. **L'evasione dei forfettari dopo il 2019**, quando la soglia è salita a 65.000 e poi a 85.000 euro.

Tutti questi dati si potrebbero produrre in forma anonima e statistica dal Dipartimento delle Finanze, incrociando dichiarazioni, CU, quadro RF delle società e archivio dei rapporti finanziari. È la proposta **01-P23** del programma.

---

## 8. Fonti

- MEF-DF, *Sintesi dei dati IRPEF e IVA, a.i. 2024* (23/4/2026), [pdf](https://www1.finanze.gov.it/finanze/analisi_stat/public/v_4_0_0/contenuti/sintesi_analisi_dati_2024_irpef_iva.pdf).
- MEF-DF, *Sintesi: IRPEF titolari di partita IVA, reddito prevalente e ISA, a.i. 2024* (26/5/2026), [pdf](https://www1.finanze.gov.it/finanze/analisi_stat/public/v_4_0_0/contenuti/sintesi_analisi_dati_2024_irpef_isa.pdf).
- MEF-DF, *Analisi dei dati IRPEF, a.i. 2024*, [pdf](https://www1.finanze.gov.it/finanze/analisi_stat/public/v_4_0_0/contenuti/analisi_dati_2024_irpef.pdf) (par. 1.5.2.3 cedolare, 2.6 forfettari, 3 reddito prevalente).
- MEF-DF, tavole statistiche a.i. 2024: [imposta netta per reddito prevalente](https://www1.finanze.gov.it/finanze/analisi_stat/public/index.php?tree=2025AETPTOT040001); [numero per reddito prevalente](https://www1.finanze.gov.it/finanze/analisi_stat/public/index.php?tree=2025AETPTOT010001); calcolo IRPEF per gruppo: [dipendenti](https://www1.finanze.gov.it/finanze/analisi_stat/public/index.php?tree=2025AETIPLD020003), [pensionati](https://www1.finanze.gov.it/finanze/analisi_stat/public/index.php?tree=2025AETIPPE020003), [autonomi](https://www1.finanze.gov.it/finanze/analisi_stat/public/index.php?tree=2025AETIPRE020003), [imprenditori](https://www1.finanze.gov.it/finanze/analisi_stat/public/index.php?tree=2025AETIPFG020003), [soci di società di persone](https://www1.finanze.gov.it/finanze/analisi_stat/public/index.php?tree=2025AETIPRH020003), [fabbricati](https://www1.finanze.gov.it/finanze/analisi_stat/public/index.php?tree=2025AETIPRB020003); [regimi agevolati](https://www1.finanze.gov.it/finanze/analisi_stat/public/index.php?tree=2025ABPFMIN020101); [classi di reddito](https://www1.finanze.gov.it/finanze/analisi_stat/public/index.php?tree=2025AAPFTOT020602); [ventili](https://www1.finanze.gov.it/finanze/analisi_stat/public/index.php?tree=2025AAPFTOT020603); [tipologie di reddito per classe](https://www1.finanze.gov.it/finanze/analisi_stat/public/index.php?tree=2025AAPFTOT020202); [attività estere RW](https://www1.finanze.gov.it/finanze/analisi_stat/public/index.php?tree=2025AETPTOT050001). Le tavole hanno più pagine di colonne (parametro `page`).
- MEF-DF, *Analisi dei dati IRES, a.i. 2023*, [pdf](https://www1.finanze.gov.it/finanze/analisi_stat/public/v_4_0_0/contenuti/analisi_dati_2023_ires.pdf) (ultimo anno pubblicato).
- MEF-DF, *Bollettino delle entrate tributarie* n. 286, gennaio-dicembre 2025 (marzo 2026), [copia Astrid](https://www.astrid-online.it/static/upload/boll/bollettino-entrate-dicembre2025.pdf).
- MEF, *Relazione sull'economia non osservata e sull'evasione fiscale e contributiva 2026*, [mef.gov.it](https://www.mef.gov.it/documenti-pubblicazioni/rapporti-relazioni/) (copia in `dati/raw/01_mef_relazione_evasione_2026.txt`).
- Dalle Luche, Guzzardi, Palagi, Roventini, Santoro, *Tackling the regressivity of the Italian tax system*, LEM WP 2024/26, maggio 2026, [pdf](https://www.lem.sssup.it/WPLem/files/2024-26.pdf).
- Guzzardi, Palagi, Roventini, Santoro, *Reconstructing Income Inequality in Italy: New Evidence and Tax System Implications from Distributional National Accounts*, JEEA 22(5), 2024, [doi:10.1093/jeea/jvad073](https://doi.org/10.1093/jeea/jvad073).
- UPB, *Nota di lavoro n. 1/2026*, [upbilancio.it](https://www.upbilancio.it/it/nota-di-lavoro-n-1-2026-la-dinamica-retributiva-e-il-ruolo-dellimposta-sul-reddito-delle-persone-fisiche/) (cifre lette dalla sintesi del [Foglio](https://www.ilfoglio.it/economia/2026/07/22/news/le-riforme-dellirpef-hanno-aiutato-i-redditi-bassi-lo-studio-dellupb--402864); **da verificare** sul testo della nota).
- EU Tax Observatory, *Global Tax Evasion Report 2024*, [pdf](https://halshs.archives-ouvertes.fr/halshs-04563948v1/file/global_tax_evasion_report_24.pdf).
