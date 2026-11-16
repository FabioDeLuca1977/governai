*Bozza scritta da un agente AI il 16 novembre 2026; da valutare con il panel e da approvare; non rivista da una persona.*

# Bozza di scheda: stessa regola per tutte le imprese (01-P25)

Riga proposta per `motore/proposte.csv` (formato `proposta_id,titolo,costo_min,costo_max,costo_opportunita`; da aggiungere solo dopo l'approvazione):

```csv
01-P25,"Stessa regola per tutte le imprese: 24% sugli utili lasciati in azienda anche per ditte, SNC e SAS; i dividendi fermi nella holding personale pagano come se distribuiti",0.63,0.99,0.0
```

Varianti: `benchmark/bozza_varianti_neutralita.csv`. Coperture nuove: `benchmark/bozza_coperture_neutralita.csv` (FN13, FN14). Calcoli: `analisi/chi_paga/neutralita.py`, risultati in `analisi/chi_paga/neutralita.csv`. Importi in mld €/anno salvo diversa indicazione. "Stima GovernAI" = stima propria su dati ufficiali; "da verificare" = dato o norma non riscontrati sul testo originale.

**Questa bozza non dà punteggi sui valori.** Li daranno panel indipendenti con `motore/rubrica.md`. Per questo le colonne RIS ... CIT delle coperture sono vuote.

**La scelta politica è già fatta** da chi guida il progetto (16/11/2026): "stessa regola per tutti", cioè neutralità tra forme d'impresa. La bozza descrive come farla bene e quanto costa davvero. **Il punto da decidere resta uno: la proposta non si paga da sola.** Il gettito della regola (b) copre una piccola parte del costo della regola (a). Servono altre coperture (par. "Saldo").

**Regole applicate (come nelle schede di `programma/schede/`).**
- Nessuna variante usa DEFICIT, RISPARMI_ATTESI, IVA_EVASIONE, ETS o ALTRO. Il minor gettito di (a) è imputato a SPESE_FISCALI, come le altre riduzioni d'imposta del programma (01-P4, 01-P9). I costi di attuazione vanno su RIALLOCAZIONE.
- Il gettito di (b) è un'entrata decisa per legge, nelle coperture **FN13** (con ESSENZIALE o PIENA) e **FN14** (solo con PIENA, in aggiunta). Vanno nel fondo SPESE_FISCALI come fondo più vicino, come FN05-FN10.
- **Vincoli da inserire in `programma/ottimizza.py` (LEGAMI):** `"FN13": ["01-P25:PIENA", "01-P25:ESSENZIALE"], "FN14": ["01-P25:PIENA"]`.
- **Verifica degli id (16/11/2026).** Ho cercato 01-P25, FN13 e FN14 in tutti i file `.md` e `.csv` del repository e non sono usati. FN11 e FN12 sono nella bozza della patrimoniale (01-P24). Il coordinatore controlli di nuovo prima di unire le bozze di altri agenti.
- **Quattro domande e oceano blu:** il blocco YAML per `programma/quattro_domande_01_03.yaml` è in fondo alla scheda.

---

## 01-P25 — Stessa regola per tutte le imprese: chi lascia gli utili in azienda paga il 24%, chi li porta a casa paga come persona

### Perché

**Problema in un dato.** Due imprese con lo stesso utile di 1.000.000 di euro, lasciato tutto in azienda per investire, oggi pagano imposte molto diverse:
- **SRL: 27,9%** (IRAP e IRES);
- **socio di SNC: 47,3%**, perché paga subito l'IRPEF progressiva su tutto l'utile, anche se non lo preleva (art. 5 TUIR);
- **ditta individuale: 43,4%**.

Se poi il socio di SRL porta i dividendi nella sua holding e li tiene fermi, paga il **28,8%** e può non pagare mai il resto. Fonte: `analisi/chi_paga/neutralita.csv`, con le regole 2026 di `calcola.py`.

L'UPB misura una distanza tra le aliquote marginali sugli utili non distribuiti delle due forme che "può raggiungere 19 punti percentuali" ([Memoria sul DDL delega fiscale, luglio 2023, par. 4.3, p. 30](https://www.upbilancio.it/wp-content/uploads/2023/07/Memoria-UPB-DDL-riforma-fiscale.pdf)).

Chi è coinvolto (MEF-DF, a.i. 2024; vedi `analisi/chi_paga/popolazione.md`):
- **892.638** persone hanno come reddito principale una quota di SNC o SAS (reddito medio 41.028 €, aliquota sul dichiarato 23,7%);
- **861.423** sono imprenditori individuali (reddito medio 37.829 €);
- in contabilità ordinaria il reddito medio dell'imprenditore è **58.700 €** ([Sintesi IRPEF a.i. 2024, nota 4](https://www1.finanze.gov.it/finanze/analisi_stat/public/v_4_0_0/contenuti/sintesi_analisi_dati_2024_irpef_iva.pdf));
- le dichiarazioni delle società di persone sono **652.832**, il 2,9% in meno in un anno.

Una ragione c'è: chi lavora in forma di SNC non può rinviare l'imposta, chi ha una SRL o una holding sì. Il risultato è che **la forma giuridica la sceglie il fisco, non l'impresa**.

**Perché la regola va scritta in due parti.** Se si abbassa solo l'imposta sugli utili lasciati nelle SNC, si rende più facile l'accumulo, non la parità. Se si colpisce solo la holding, si penalizza chi ha una SRL e lascia invariata la SNC. La regola giusta è una sola, con due lati:
- l'utile che **resta nell'impresa** paga il 24%, qualunque sia la forma;
- l'utile che **esce dall'impresa** e non finanzia attività vere paga come reddito della persona, cioè IRPEF per chi preleva da una SNC e 26% per i dividendi.

La holding che tiene fermi i dividendi della propria società operativa è, nei fatti, un prelievo che non si chiama prelievo.

**Evidenze.**
- **OCSE.** Il sistema fiscale ideale è neutrale rispetto alla nascita, alla forma e alla crescita delle piccole imprese, ma molti Paesi spingono a costituire società di capitali per pagare meno ([OECD, *Taxation of SMEs in OECD and G20 Countries*, Tax Policy Studies n. 23, 2015](https://doi.org/10.1787/9789264243507-en)).
- **Italia, delega del 2014.** La L. 23/2014, art. 11 c. 1 lett. a, chiedeva già di assimilare all'IRES i redditi d'impresa IRPEF, con un'imposta proporzionale sugli utili trattenuti. La delega è scaduta il 27/6/2015 senza essere attuata (dossier Camera AC 4127-bis, art. 68, p. 348-349).
- **Italia, IRI 2017-2018.** Era il precedente diretto: art. 55-bis TUIR, introdotto dalla L. 232/2016, c. 547-548. Era un'**opzione** per imprenditori individuali, SNC e SAS in contabilità ordinaria: 24% sugli utili trattenuti, prelievi deducibili e tassati con l'IRPEF, contributi calcolati come prima. Lo scopo dichiarato era l'"uniformità di trattamento con le società di capitali" e la patrimonializzazione delle piccole imprese ([dossier Camera AC 4127-bis, art. 68](https://documenti.camera.it/leg17/dossier/pdf/ID0026s1.pdf)).
- **Italia, delega del 2023.** Ripropone lo stesso schema (DDL delega, art. 5 c. 1 lett. g; numerazione nella L. 111/2023 da verificare). Il regime opzionale non risulta attuato (**da verificare** sui decreti attuativi e sul testo unico d.lgs. 117/2026).
- **Esempi esteri di reinvestimento obbligato e di tassa sugli utili fermi** (da `benchmark/equita_fiscale_diagnosi.md`):
  - in Francia, nell'apporto di quote a una holding (art. 150-0 B ter CGI), chi vende entro 3 anni deve reinvestire una quota in attività economiche, altrimenti l'imposta rinviata si paga (soglia del 60% da verificare);
  - negli Stati Uniti l'*accumulated earnings tax* (IRC §531) colpisce gli utili trattenuti oltre i bisogni ragionevoli dell'impresa.
- **Corte dei conti.** Non ho trovato una valutazione specifica sull'IRI. È da cercare nei Rapporti sul coordinamento della finanza pubblica 2017-2019.

### Cosa insegna la storia dell'IRI (perché è stata abrogata)

1. **Il costo stimato era vero e noto.** La relazione tecnica (RT) alla L. 232/2016 stimava questi effetti, come riportati dal [Servizio Bilancio della Camera, Verifica delle quantificazioni AC 4127-bis](https://documenti.camera.it/leg17/dossier/Testi/VQ4127.htm).

   **Platea.**

   | | Imprese | Optano | Imposta IRI | Risparmio |
   |---|---|---|---|---|
   | Società di persone in ordinaria | circa 280.000 | 184.000 | 1,23 mld su 5,1 di imponibile | **761 mln** (circa 4.100 € a impresa) |
   | Imprese individuali in ordinaria | circa 147.000 | 96.000 | 0,686 mld | **451 mln** (circa 4.700 €) |

   **Effetto sul gettito.**

   | | 2017 | 2018 | Dal 2019 |
   |---|---|---|---|
   | Competenza | −1.212,1 mln | −1.231,3 mln | −1.255,8 mln |
   | Cassa | — | **−1.986,6 mln** (saldo più acconto) | −1.238,1 mln, poi circa −1.250 |

   Il Servizio Bilancio osservava che l'aliquota media implicita a legislazione vigente (17,6%) era bassa per imprese in utile. Il costo poteva quindi essere **sottostimato**.
2. **Rinviata per fare cassa.** La L. 205/2017, c. 1063, l'ha spostata al 2018. Il motivo era recuperare circa 2 mld di cassa nel 2018. Le categorie hanno parlato di "violazione dello Statuto del contribuente" ([lavoce.info](https://lavoce.info/archives/49647/iri-buona-riforma-rinviata-far-cassa/); [informazionefiscale, tabella della RT del rinvio](https://www.informazionefiscale.it/rinvio-iri-2018-pragmatismo-ragioneria-di-stato)).
3. **Abrogata prima di partire, con effetto retroattivo.** La L. 145/2018, art. 1 c. 1055, "in deroga all'articolo 3 della legge 27 luglio 2000, n. 212", l'ha abrogata dal periodo d'imposta 2018. In quel periodo l'IRI era già in vigore e le imprese si erano già organizzate. La RT dell'abrogazione conta lo stesso importo come maggior gettito: 1.212,1 mln nel 2018, 1.231,3 nel 2019, 1.255,7 dal 2020. Le risorse sono andate all'estensione del forfettario e alla "mini-IRES" (NADEF 2018; [dossier Camera L. 145/2018, vol. III, p. 1267-1268](https://documenti.camera.it/Leg18/Dossier/Pdf/ID0006i_vol_III.Pdf)). La mini-IRES è stata poi abrogata a sua volta (**da verificare** la norma).
4. **Problemi tecnici rimasti aperti** (dossier Camera; DL 50/2017, art. 58):
   - le riserve formate prima del regime;
   - le perdite;
   - le uscite dal regime;
   - i prelievi mascherati, cioè beni e prestiti dell'impresa ai soci.

**Lezioni per GovernAI.**
- **(i)** Dichiarare il costo per intero, compreso il primo anno di cassa più pesante, e coprirlo prima.
- **(ii)** Scrivere nella legge una clausola di stabilità (punto 19): niente rinvii o abrogazioni retroattive. Nel programma non c'è oggi una clausola fiscale generale; 01-P16 riguarda i tetti di spesa.
- **(iii)** Scrivere nella legge l'antiabuso sui prelievi mascherati e la tassazione delle riserve all'uscita, così che il 24% sia un **rinvio** e non un'esenzione.
- **(iv)** Far partire, nello stesso momento, la regola (b), che toglie il vantaggio opposto a chi ha la holding.

### Come (PIENA)

**Regola (a): utili lasciati nelle imprese di persone.**
1. **Chi.** Imprenditori individuali, SNC e SAS in **contabilità ordinaria**, anche per scelta di chi oggi è in semplificata. Si entra con **opzione per cinque periodi d'imposta**, rinnovabile, esercitata in dichiarazione. **I forfettari restano fuori** (L. 190/2014): il loro regime non cambia.
2. **Cosa paga l'impresa.** L'utile che resta nell'impresa paga il **24%** (aliquota IRES, art. 77 TUIR). I prelievi dell'imprenditore e dei soci, a carico degli utili dell'anno o delle riserve formate nel regime, si deducono dalla base e pagano l'**IRPEF progressiva** in capo alla persona. Così chi preleva tutto paga come oggi; chi lascia in azienda paga come una SRL.
3. **Contributi INPS invariati.** Si calcolano sull'intero reddito d'impresa, come prevedeva l'IRI (L. 232/2016, c. 548). Nessuna perdita per l'INPS, nessuna pensione più bassa.
4. **Riserve di prima del regime.** I prelievi da queste riserve restano non tassati, perché l'IRPEF è già stata pagata, e non si deducono. Per legge **i prelievi si imputano prima agli utili dell'anno e alle riserve formate nel regime**.
5. **Perdite.** Si riportano senza limiti di tempo nel regime e si imputano ai soci per quota all'uscita (modello art. 55-bis c. 2).
6. **Niente rinvio infinito.** In questi casi le riserve al 24% si considerano **prelevate** e pagano l'IRPEF, con **credito del 24%** già pagato (modello DL 50/2017, art. 58):
   - uscita dal regime;
   - cessione o cessazione dell'impresa;
   - morte dell'imprenditore o del socio senza continuazione da parte degli eredi.

   In caso di **trasformazione in società di capitali**, le riserve al 24% diventano riserve di utili della società e pagano il 26% quando sono distribuite, come per tutte le SRL.

**Regola (b): dividendi fermi nella holding personale.**
7. **Chi.** I soci di controllo di una **holding personale**, cioè una società o un ente controllato, anche indirettamente, da non più di 5 persone fisiche. Coniuge, parenti entro il terzo grado e affini entro il secondo contano come una persona: è la stessa definizione di 01-P19, art. 1 c. 1 lett. a. **Non serve che la holding sia passiva.**
8. **Su cosa.** I **dividendi delle partecipazioni di almeno il 10% in società operative** (italiane o estere) **incassati dal periodo d'imposta 2028**. Ogni anno di dividendi apre un "conto di reinvestimento". Le riserve già formate prima della legge **non si toccano mai**.
9. **Cosa conta come attività vera (reinvestimento), entro 3 anni:**
   - capitale o finanziamenti a società operative controllate o collegate (almeno 20%), anche la stessa che ha pagato il dividendo;
   - acquisto del controllo o di almeno il 20% di società operative;
   - beni strumentali usati da società operative del gruppo, compresi gli immobili strumentali;
   - nuove azioni di PMI non quotate e quote di fondi EuVECA, **nei limiti dell'art. 21 del regolamento generale di esenzione** (aiuti al finanziamento del rischio, o il regolamento che lo sostituisce);
   - rimborso del debito contratto per acquistare partecipazioni operative.

   **Non contano** liquidità, titoli, fondi, immobili dati in affitto a terzi, beni di lusso, prestiti ai soci.

   Riserva per acquisizioni e crisi: la holding può vincolare fino al 30% del conto (massimo 20 mln €) per **5 anni**. Vale per l'acquisto di partecipazioni operative o per sostenere controllate in perdita o in crisi, come in 01-P19, punto 6.
10. **Cosa paga.** Alla fine dei 3 anni (o dei 5 per la riserva), la parte del conto **né distribuita né reinvestita** si considera **distribuita ai soci di controllo** e paga il **26%**. È la stessa imposta che il socio avrebbe pagato incassando direttamente. La holding versa l'imposta come sostituto, per conto dei soci, e questo versamento non è una distribuzione ulteriore.
    - Quando la holding distribuisce davvero quelle somme, non si paga di nuovo: c'è un **credito che segue le quote** in caso di vendita, donazione o successione.
    - I reinvestimenti si misurano **al netto** dei rimborsi ricevuti nello stesso periodo, così i giri circolari non contano.
11. **Franchigia per le piccole realtà.** I primi **100.000 €** l'anno di dividendi fermi, **per gruppo familiare** (non per holding), non pagano.
12. **Holding estere.** Stessa regola per i soci residenti di holding estere: stessa base, franchigia, reinvestimenti e riserva. Si tassa sempre il socio, quindi il trattamento è uguale per holding italiane ed estere.

**Antiabuso comune (a) e (b).**
13. **Beni e prestiti ai soci.** Beni dell'impresa o della holding in uso a soci e familiari, prestiti e garanzie a loro favore si **presumono prelievo** (regola a) o **distribuzione** (regola b). La presunzione non vale se il prestito è restituito entro 12 mesi, se ci sono interessi o corrispettivi di mercato o se il contribuente dà un'altra prova contraria. Non si paga due volte quanto è già tassato come reddito diverso (art. 67 c. 1 lett. h-ter TUIR). Il modello è 01-P19, art. 4, esteso a tutte le holding personali. Nel Regno Unito una regola simile vale per i *loans to participators* (s. 455 CTA 2010).
14. **Prestiti dalla società operativa alla holding o ai soci**, compreso il cash pooling: se il prestito non va a un reinvestimento ammesso, conta come dividendo entrato nel conto. Altrimenti la regola (b) si aggira non distribuendo e prestando.
15. **Frazionamento.** Tetti e franchigie si calcolano per gruppo familiare. Nelle catene di holding la regola (b) si applica una volta sola, al livello più alto controllato dalle persone.
16. **Interpello preventivo** (art. 11 L. 212/2000) per chi è in dubbio, e prospetto in dichiarazione con prelievi, conti di reinvestimento e prestiti ai soci.
17. **Trasferimento di residenza.** Chi va all'estero con conti di reinvestimento aperti paga il 26% sulla parte non ancora reinvestita, come nell'exit tax minima di 01-P19, punto 11. Verso UE, SEE e Svizzera il pagamento è sospeso senza interessi e senza garanzie.
18. **Solo per il futuro.**
    - (a) vale dal periodo d'imposta 2028;
    - (b) vale per i dividendi incassati dal 2028;
    - nessuna regola tocca riserve, prelievi o dividendi già formati.
19. **Clausola di stabilità.** Le regole (a) e (b) non si possono cambiare per periodi d'imposta già iniziati né per opzioni già esercitate, se non a favore del contribuente. Una modifica peggiorativa vale solo dal periodo successivo alla scadenza del quinquennio in corso. Così l'articolo 3 dello Statuto del contribuente non viene di nuovo derogato, come accadde con l'IRI.

### Che cosa (varianti)

| Variante | Contenuto | Costo 2027 / 2028 / 2029 / regime (2033) | Intensità | Copertura legata |
|---|---|---|---|---|
| PIENA | Punti 1-19 | 0,002 / 0,01 / **2,03** / **0,99** | 1 | FN13 + FN14: 0,04-0,33 a regime, niente prima del 2032 |
| ESSENZIALE | (a) solo fino a **100.000 €** l'anno di utile lasciato in impresa per socio o imprenditore; oltre, IRPEF ordinaria. (b) solo holding residenti, franchigia **500.000 €** l'anno per gruppo familiare | 0,002 / 0,01 / **1,26** / **0,63** | 0,55 | FN13: 0,03-0,23 a regime, niente prima del 2032 |
| ZERO | Microsimulazione DF che aggiorna la RT del 2017; prospetto in dichiarazione per le holding personali (dividendi operativi incassati, fermi e reinvestiti; prestiti ai soci) con statistica solo aggregata; decisione nella legge di bilancio 2030 con i dati | 0 | 0,1 | nessuna |

I costi sono valori centrali e comprendono 0,01 di attuazione; gli intervalli sono nel paragrafo successivo.

**Perché non c'è una variante PILOTA.** Un'imposta non si sperimenta su un campione di imprese senza violare l'art. 3 Cost. (stessa scelta di 01-P19). Una versione temporanea per tutti avrebbe il difetto che ha rovinato l'IRI: le imprese si organizzano e la regola sparisce.

**Motivazione delle intensità.**
- **ESSENZIALE 0,55.** Per la grande maggioranza delle imprese di persone la parità è piena: il reddito medio dei soci è 41.028 € e quello degli imprenditori in ordinaria 58.700 €. Non lo è per le più grandi. La regola (b) tocca solo chi tiene fermi più di 500.000 € l'anno.
- **ZERO 0,1.** Nessun effetto sulla parità, ma costruisce i dati che oggi mancano.

### Quanto costa la regola (a), anno per anno

**Metodo** (stima GovernAI; la funzione `profilo_costo_a` è in `neutralita.py`).
- **Base.** RT 2017: 1,256 mld di competenza a regime.
- **Aggiornamenti** (moltiplicatori, intervallo basso-alto):

  | Fattore | Intervallo | Motivo |
  |---|---|---|
  | Platea | 0,80-1,00 | Meno società di persone. Il numero in ordinaria del 2024 non è pubblicato: **da verificare** |
  | Aliquote | 0,95-1,05 | Con gli scaglioni 2026 (23/33/43 contro 23/27/38/41/43 del 2017) il vantaggio scende tra 28.000 e 50.000 € e sale tra 50.000 e 75.000 € |
  | Crescita al 2028 | 1,06-1,10 | Redditi medi in ordinaria stabili: 58.700 € nel 2024 contro circa 59.400 € nella RT |

- **Rientro del rinvio.** Ogni anno si preleva il 5-10% delle riserve al 24%, che pagano allora l'IRPEF meno il 24% già versato. Le cifre della RT sono quasi costanti nel tempo e non sembrano contare questo rientro (**da verificare** sul testo della RT).
- **Cassa.** Nel primo anno di cassa il costo è 1,64 volte quello di competenza (saldo più acconto, come nella RT). Gli acconti 2028 si calcolano con le regole previgenti.

| mld, cassa | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 |
|---|---|---|---|---|---|---|---|
| PIENA (basso - alto) | 0 | 0 | 1,66 - 2,38 | 0,91 - 1,41 | 0,82 - 1,37 | 0,74 - 1,33 | 0,66 - 1,29 |
| ESSENZIALE (basso - alto) | 0 | 0 | 0,83 - 1,66 | 0,46 - 0,98 | 0,41 - 0,96 | 0,37 - 0,93 | 0,33 - 0,91 |

La ESSENZIALE costa il 50-70% della PIENA. È un'ipotesi: i 7.185 soci di società di persone con reddito di partecipazione oltre 300.000 € (a.i. 2024) pesano molto sul costo, ma la distribuzione degli utili trattenuti non è pubblicata. **Da rifare con la microsimulazione del DF.**

### Quanto rende la regola (b): FN13 e FN14

**La base non è pubblicata.** Nessuna fonte ufficiale dice quanti dividendi delle società operative arrivano alle holding personali e quanti restano fermi.
- Il DF ha il dato nel modello Redditi SC (quadro RF, utili esclusi art. 89 TUIR) ma non lo pubblica.
- L'[analisi IRES a.i. 2023](https://www1.finanze.gov.it/finanze/analisi_stat/public/v_4_0_0/contenuti/analisi_dati_2023_ires.pdf) dà solo il totale delle variazioni in diminuzione (351,5 mld), senza separare i dividendi.
- L'unico riferimento è indiretto: **6.695 mln** di ritenute sugli utili nel 2025, cioè circa 25,7 mld di dividendi pagati a persone e non residenti (Bollettino entrate n. 286).
- I dati del quadro RW (attività estere delle persone) non dicono nulla sui dividendi intersocietari.

**Catena prudente** (ipotesi GovernAI, basso-alto):

| Passaggio | Valore |
|---|---|
| Dividendi operativi incassati da holding personali | 5-12 mld l'anno |
| Fermi dopo 3 anni | 20-35% |
| Oltre la franchigia | 50-65% (500.000 €) o 75-85% (100.000 €) |
| Imposta | 25,7% |
| Meno comportamenti | 50-60% |
| Solo parte strutturale | 55-65% |

Tra i comportamenti, il principale è lasciare gli utili nella società operativa: è legittimo e coerente con la regola. Si conta solo la parte strutturale perché il credito alla distribuzione vera riduce le ritenute future. È la stessa condizione posta dal giurista su FN05 (`giuridico/note_equita.md`).

| Copertura | Gettito a regime (2033) | Primo anno |
|---|---|---|
| FN13 (ESSENZIALE o PIENA) | 0,03 - 0,23 | 2032 (dividendi 2028 non reinvestiti entro il 2031), a metà |
| FN14 (solo PIENA, in più) | 0,02 - 0,10 | 2032 |

**Nessun doppio conteggio con FN05 e FN06.** 01-P19 esclude per legge dalla sua base i dividendi delle partecipate operative di almeno il 10% (art. 2 c. 3 lett. a). Questi sono **esattamente** la base di FN13 e FN14. I redditi passivi restano solo in 01-P19.

### Saldo: la proposta non sta in piedi da sola

| mld | 2029 | 2032 | 2033 (regime) |
|---|---|---|---|
| PIENA: costo di (a) più attuazione | 1,67 - 2,39 | 0,75 - 1,34 | 0,67 - 1,30 |
| PIENA: gettito di (b) (FN13 + FN14) | 0 | 0,02 - 0,16 | 0,04 - 0,33 |
| **PIENA: altre coperture necessarie** | **circa 2,0** | **circa 0,9 (fino a 1,3)** | **circa 0,8 (fino a 1,25)** |
| ESSENZIALE: costo di (a) più attuazione | 0,84 - 1,67 | 0,38 - 0,94 | 0,34 - 0,92 |
| ESSENZIALE: gettito di (b) (FN13) | 0 | 0,01 - 0,11 | 0,03 - 0,23 |
| **ESSENZIALE: altre coperture necessarie** | **circa 1,25** | **circa 0,6 (fino a 0,9)** | **circa 0,6 (fino a 0,9)** |
| ZERO | 0 | 0 | 0 |

In ogni cella "circa" è il valore centrale e "fino a" è il caso prudente: costo alto e gettito minimo.

**Quali altre coperture.** Nessuna copertura del menu è legata per tema a questa proposta. Le più vicine sono quelle sulle agevolazioni alle imprese a bassa addizionalità, se non sono già usate nello scenario:
- **SF10**, iperammortamento non qualificato: 0,2-0,4;
- **SF16**, patent box: 0,2-0,24;
- **SF04**, cooperative grandi: 0,05-0,15.

Insieme fanno circa 0,45-0,8 a regime, il che basta per la ESSENZIALE ma non per la PIENA. **Il picco del 2029** viene dal primo anno di cassa (saldo più acconto), come nel 2018 per l'IRI. Lo coprono coperture con gettito già pieno nel 2029, oppure una decorrenza spostata di un anno. **È una scelta politica:** la neutralità tra forme d'impresa costa circa 1 mld l'anno a regime nella PIENA e circa 0,6 nella ESSENZIALE, e va finanziata togliendo altro.

### Chi ci guadagna e chi paga

**Aliquota effettiva di sole imposte, PIENA** (`analisi/chi_paga/neutralita.csv`; regole 2026; utile lasciato tutto in impresa, al netto dei contributi; in parentesi imposte più contributi).

| Reddito lordo | Socio di SNC prima → dopo | Ditta individuale prima → dopo | SRL (utili nella società) | SRL tramite holding, utili fermi prima → dopo | SRL tramite holding, utili reinvestiti |
|---|---|---|---|---|---|
| 50.000 | 24,7 → 21,6 (49,2 → 46,1) | 20,6 → 18,1 (45,1 → 42,6) | 27,3 | 28,2 → 28,2 (sotto franchigia) | 28,2 |
| 100.000 | 30,3 → 21,9 (55,2 → 46,8) | 26,4 → 18,0 (51,3 → 42,9) | 27,6 | 28,5 → 28,5 (sotto franchigia) | 28,5 |
| 300.000 | 42,2 → **25,5** (52,4 → 35,7) | 38,3 → **21,6** (48,5 → 31,8) | 27,9 | 28,8 → **38,6** | 28,8 |
| 1.000.000 | 47,3 → **27,2** (50,3 → 30,2) | 43,4 → **23,3** (46,4 → 26,3) | 27,9 | 28,8 → **44,7** | 28,8 |

Con la ESSENZIALE:
- il socio di SNC a 1.000.000 € scende solo a 45,1%, per il tetto di 100.000 € al 24%;
- la holding paga in più solo a 1.000.000 € (28,8 → 34,3); a 300.000 € resta sotto la franchigia di 500.000 €.

Se l'imprenditore preleva tutto, **nulla cambia**: prima e dopo coincidono (caso di prova 1 di `neutralita.py`).

**Come leggere la tabella.**
- **Guadagna** chi ha un'impresa di persone, guadagna oltre circa 50.000 € e lascia utili in azienda. È lo stesso trattamento della SRL. Secondo la RT 2017 conviene a circa 2 imprese in ordinaria su 3, con un risparmio medio di 4.000-5.000 € l'anno. Da aggiornare: il numero di imprese è sceso.
- **Sotto i 28.000-35.000 €** di reddito il 24% non conviene: l'IRPEF marginale (23% più addizionali, meno le detrazioni) è già vicina o inferiore. Per questo il regime è un'opzione e nessuno ci perde.
- **Paga** solo chi tiene fermi nella holding oltre la franchigia i dividendi della propria SRL, senza reinvestirli in attività vere. Chi reinveste resta al 28,8%. Chi lascia gli utili nella società operativa resta al 27,9%.
- **La SRL non cambia.**
- **Per livello di reddito:**
  - i soci di società di persone hanno in media 41.028 €; l'aliquota sul dichiarato è 23,7%;
  - nella classe oltre 300.000 € i redditi da partecipazione in società di persone sono il 15% e l'impresa in ordinaria il 4,5% (DF a.i. 2024);
  - il guadagno in valore assoluto si concentra quindi sopra 100.000 €;
  - la regola (b) pesa quasi solo sopra 300.000 € di utile.

**Due asimmetrie che restano** (non fanno parte della proposta e si dichiarano):
- **IRAP.** Le persone fisiche ne sono esenti dal 2022 e le SNC no. Dopo (a) la ditta che trattiene paga il 23,3% contro il 27,9% della SRL.
- **Contributi.** Chi ha un'impresa di persone li paga sull'intero reddito fino al massimale. Il socio di capitale che non lavora nella società non li paga sui dividendi. Pesano sul reddito di oggi, ma danno una pensione.

### Chi decide e chi attua

- **Decide** il Parlamento con la legge di bilancio, con nuovi articoli nel testo unico delle imposte sui redditi (d.lgs. 117/2026; numerazione **da verificare**).
- **Attuano** l'Agenzia delle entrate (modelli, prospetti, controlli sui prelievi e sui conti di reinvestimento, interpelli) e Sogei.
- **Il DF** fa la microsimulazione prima della legge e la valutazione dopo 3 anni.
- **L'INPS** non cambia nulla: i contributi restano sull'intero reddito.

### Coordinamento con le altre proposte

- **01-P19 (holding passive): una proposta distinta, non un'integrazione.**

  *Perché distinta.*
  - **Oggetto diverso.** 01-P19 colpisce i proventi passivi e esclude espressamente i dividendi delle partecipate operative. (b) prende proprio quelli, e solo se restano fermi.
  - **Platea diversa.** (b) vale anche per le holding a capo di gruppi operativi, che 01-P19 non tocca.
  - **Logica diversa.** (b) è il secondo lato di (a), cioè neutralità tra forme d'impresa. 01-P19 riguarda il possesso diretto o indiretto di patrimoni passivi.
  - **Lavoro già fatto.** 01-P19 è già passata dal panel e dal giurista: cambiarne l'esclusione riaprirebbe tutto.
  - **Gettito separato.** Si evita il doppio conteggio con FN05 e FN06.

  *Cosa condividono.* La definizione di holding personale (01-P19, art. 1 c. 1 lett. a), il prospetto in dichiarazione, l'interpello, la regola su prestiti e beni ai soci e la riserva per acquisizioni e crisi.

  *Regole di confine.*
  - Un euro reinvestito conta una sola volta: la holding dichiara a quale conto lo imputa.
  - Se una holding è passiva per 01-P19 e incassa anche dividendi operativi, 01-P19 si applica ai proventi passivi e (b) ai dividendi operativi.
  - I dividendi pagati da una holding già soggetta a (b) non rientrano di nuovo nella base di 01-P19, che già li esclude (art. 2 c. 3 lett. c).

  *Domanda per il giurista.* 01-P19 tassa la holding, (b) tassa il socio. Conviene allineare 01-P19 alla tassazione del socio? La nota di verifica la indica già come soluzione alla discriminazione alla rovescia.
- **01-P22 (eredità).**
  - Le quote di SNC e le ditte passate a figli e coniuge restano esenti per la parte operativa (art. 3 c. 4-ter TUS).
  - La liquidità accumulata al 24% oltre il 20% dell'attivo o un anno di costi è un attivo passivo anche per 01-P22: stesso trattamento per SNC e SRL.
  - Alla morte senza continuazione le riserve al 24% si considerano prelevate (punto 6). Quando c'è continuazione passano agli eredi con il credito.
  - I conti di reinvestimento di (b) passano agli eredi con il termine che continua a decorrere, e il credito segue le quote.
  - Imposta di successione e imposta sul reddito sono diverse: nessun doppio conteggio tra FN10 e FN13.
- **Forfettari (SF02 e regime vigente).** Restano fuori. Per chi cresce e trattiene utili, (a) rende un po' meno caro lasciare il forfettario per l'ordinaria. Non cambia nulla sotto 85.000 € di ricavi.
- **Concordato preventivo biennale.** Va scritto come si applica il 24% alla parte trattenuta del reddito concordato (**da verificare** con l'Agenzia).
- **01-P23 (statistica).** Il prospetto di (b) alimenta la statistica sulle aliquote effettive.

### Costituzionalità e diritto UE (da far verificare al giurista)

- **Art. 3 e 53 Cost.** (a) toglie una disparità tra forme giuridiche che non ha ragioni economiche. (b) colpisce una ricchezza effettivamente incassata da una società **controllata** dal socio, che decide se distribuire. Per questo si tassano solo i **soci di controllo**: i soci di minoranza della holding sono esclusi. Lo schema per presunzione relativa esiste già nella trasparenza (art. 116 TUIR) e nelle società controllate estere (art. 167 TUIR).
- **Affidamento e irretroattività** (art. 3 L. 212/2000). Solo periodi d'imposta, prelievi e dividendi futuri; nessuna riserva pregressa. È la lezione opposta all'abrogazione retroattiva dell'IRI.
- **Direttiva madre-figlia** (2011/96/UE; CGUE C-68/15). (b) non tassa la holding sui dividendi ricevuti, ma i soci persone fisiche su una distribuzione presunta. La direttiva riguarda la società madre, quindi in linea di principio non si applica. Resta **da verificare** con il Dipartimento politiche europee che una tassazione del socio fatta scattare dal dividendo della figlia non sia letta come un aggiramento.
- **Libertà di stabilimento e dei capitali** (artt. 49 e 63 TFUE). Stessa regola per holding italiane ed estere, sempre in capo al socio, quindi non c'è un trattamento peggiore per l'estero. Da verificare se serve comunque l'esimente dell'attività economica effettiva per le holding UE/SEE con sostanza (Cadbury Schweppes, C-196/04). Se serve, va data anche alle holding italiane con la stessa prova, per non creare una discriminazione alla rovescia.
- **Aiuti di Stato.**
  - (a) è aperta a tutte le imprese di persone in ordinaria e allinea l'aliquota all'IRES: è una misura generale, che segue la logica del sistema. Il rischio è basso ma va controllato.
  - Il reinvestimento in PMI non quotate di (b) va inquadrato nell'art. 21 GBER, come per 01-P19.
- **Exit tax** (punto 17). Sospensione senza interessi e senza garanzie verso UE, SEE e Svizzera (C-9/02, C-470/04, C-581/17), come per 01-P19.

### Rischi principali e mitigazioni

| Rischio | Mitigazione |
|---|---|
| **Costo sottostimato.** Nel 2016 il Servizio Bilancio giudicava bassa l'aliquota implicita della RT. Il comportamento può cambiare: più utili lasciati in azienda e più imprese in ordinaria | Intervallo alto nelle varianti; microsimulazione del DF prima della legge (variante ZERO come primo passo); valutazione dopo 3 anni |
| **Primo anno di cassa pesante** (circa 2 mld nella PIENA nel 2029) | Coperture già piene nel 2029 o decorrenza spostata; dichiararlo prima, a differenza del 2017 |
| **Consumo personale nell'impresa al 24%** (prelievi mascherati) | Punti 4, 6 e 13: prelievi presunti, ordine dei prelievi fissato per legge, riserve tassate all'uscita, alla cessione e alla morte senza continuazione |
| **Gettito di (b) piccolo e lento**: la base non è pubblicata e la risposta più semplice, lasciare gli utili nella società operativa, è legittima | Conta solo come copertura minima; FN13 e FN14 legate; dati dal prospetto |
| **Aggiramento di (b)** con prestiti dalla società operativa, catene di holding, più holding nella stessa famiglia, reinvestimenti circolari | Punti 14-15, reinvestimento netto, franchigia per gruppo familiare, interpello |
| **Abrogazione o rinvio come nel 2017-2018** | Clausola di stabilità (punto 19); coperture legate nella stessa legge |
| **Complessità per le piccole imprese** | Solo opzione; nessun adempimento per chi preleva tutto o resta forfettario; prospetto solo per chi opta o ha una holding sopra la franchigia |

### Indicatori

| KPI | Base | Obiettivo 3 anni | Obiettivo 5 anni |
|---|---|---|---|
| Imprese di persone in ordinaria che optano per il 24%, utili trattenuti | 0 nel 2027 (RT 2017: 280.000 imprese potenziali) | pubblicato | serie annuale |
| Patrimonio netto delle imprese di persone in ordinaria | da rilevare (DF, Redditi SP) | in crescita | in crescita |
| Trasformazioni da SNC/ditta a SRL per motivi fiscali | da rilevare (Registro imprese) | in calo | in calo |
| Dividendi operativi incassati da holding personali, fermi e reinvestiti | non pubblicato, 2026 | pubblicato | serie |
| Distanza di aliquota effettiva tra SNC e SRL sugli utili trattenuti, a 300.000 € | 14,3 punti (42,2 contro 27,9), 2026 | sotto 3 punti (PIENA) | stabile |

### Domande per chi guida il progetto e per il panel

1. **Variante e coperture.** PIENA, che costa circa 1 mld l'anno a regime e 2 mld nel 2029, oppure ESSENZIALE, che costa 0,6 e 1,25? E con quali coperture del menu?
2. **Il tetto della ESSENZIALE** (100.000 € trattenuti per socio): va bene, o serve più alto o più basso?
3. **La franchigia di (b)** (100.000 € nella PIENA, 500.000 € nella ESSENZIALE) e il **termine di 3 anni**: vanno bene?
4. **IRAP.** Si vuole togliere anche l'asimmetria tra ditta (esente) e SNC o SRL? Non è in questa proposta e costerebbe di più.

### Fonti

**Norme.**
- L. 11/12/2016 n. 232, art. 1 c. 547-548 (IRI, art. 55-bis TUIR): [Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2016-12-11;232).
- L. 27/12/2017 n. 205, art. 1 c. 1063 (rinvio al 2018): [Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2017-12-27;205).
- L. 30/12/2018 n. 145, art. 1 c. 1055 (abrogazione): [Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2018-12-30;145).
- DL 50/2017, art. 58 (uscita dal regime IRI): citato dal dossier Camera ID0006i, vol. III.

**Relazioni tecniche e dossier parlamentari.**
- Relazione tecnica IRI (L. 232/2016): Camera, Servizio Bilancio, [Verifica delle quantificazioni AC 4127-bis](https://documenti.camera.it/leg17/dossier/Testi/VQ4127.htm), art. 68. Contiene platea, metodo e tabelle di competenza e di cassa.
- Dossier Camera, *Legge di bilancio 2017, schede di lettura AC 4127-bis*, art. 68, p. 348-354: [pdf](https://documenti.camera.it/leg17/dossier/pdf/ID0026s1.pdf).
- Dossier Camera, *Legge di bilancio 2019*, vol. III, art. 1 c. 1055, p. 1267-1268 (RT dell'abrogazione): [pdf](https://documenti.camera.it/Leg18/Dossier/Pdf/ID0006i_vol_III.Pdf).
- Relazione tecnica del rinvio (L. 205/2017), tabella di cassa: [informazionefiscale](https://www.informazionefiscale.it/rinvio-iri-2018-pragmatismo-ragioneria-di-stato).

**UPB, MEF-DF, OCSE.**
- UPB, *Memoria sul DDL delega per la riforma fiscale*, luglio 2023, par. 4.3, p. 30: [pdf](https://www.upbilancio.it/wp-content/uploads/2023/07/Memoria-UPB-DDL-riforma-fiscale.pdf).
- MEF-DF, *Sintesi dei dati IRPEF e IVA a.i. 2024*: [pdf](https://www1.finanze.gov.it/finanze/analisi_stat/public/v_4_0_0/contenuti/sintesi_analisi_dati_2024_irpef_iva.pdf).
- MEF-DF, statistiche per reddito prevalente a.i. 2024: in `analisi/chi_paga/popolazione.md`.
- MEF-DF, *Analisi dei dati IRES a.i. 2023*: [pdf](https://www1.finanze.gov.it/finanze/analisi_stat/public/v_4_0_0/contenuti/analisi_dati_2023_ires.pdf).
- MEF-DF, *Bollettino delle entrate tributarie* n. 286: [copia Astrid](https://www.astrid-online.it/static/upload/boll/bollettino-entrate-dicembre2025.pdf).
- OECD, *Taxation of SMEs in OECD and G20 Countries*, OECD Tax Policy Studies n. 23, 2015: [doi](https://doi.org/10.1787/9789264243507-en).

**Commenti.**
- lavoce.info, *Iri: quando una buona riforma è rinviata per far cassa*: [link](https://lavoce.info/archives/49647/iri-buona-riforma-rinviata-far-cassa/).

**Corte dei conti.** Nessuna valutazione specifica trovata. È **da cercare** nei Rapporti sul coordinamento della finanza pubblica 2017-2019.

---

### Blocco per `programma/quattro_domande_01_03.yaml` (da aggiungere solo dopo l'approvazione)

```yaml
  01-P25:
    perche: "Sullo stesso utile di 1 milione lasciato in azienda per investire, una SRL paga il 27,9%, il socio di una SNC il 47,3% e una ditta individuale il 43,4%, perché le imprese di persone pagano subito l'imposta progressiva anche sugli utili che non prelevano. Chi ha una SRL può anche portare i dividendi in una holding e tenerli fermi pagando il 28,8%. Così la forma giuridica la sceglie il fisco, non l'impresa."
    come: "Ditte, SNC e SAS in contabilità ordinaria possono scegliere per cinque anni di pagare il 24% sugli utili lasciati in azienda, come una SRL, e l'imposta progressiva solo su quello che prelevano; i contributi restano sull'intero reddito, i forfettari restano fuori. Dall'altra parte, i dividendi della propria società operativa incassati da una holding di famiglia dal 2028 e non reinvestiti in imprese, beni strumentali o piccole imprese entro 3 anni sono tassati ai soci di controllo come se fossero distribuiti, con un credito quando poi lo sono davvero; i primi 100.000 euro l'anno per famiglia sono esenti. Prestiti e beni ai soci contano come prelievi. La proposta costa circa 1 miliardo l'anno a regime e va coperta con altre misure del programma."
    cosa: "Stessa imposta sugli utili che restano nell'impresa, qualunque sia la forma, e stessa imposta sugli utili che ne escono. Obiettivi: distanza di aliquota tra SNC e SRL sugli utili trattenuti sotto 3 punti in 3 anni (oggi 14 punti a 300.000 euro); patrimonio netto delle imprese di persone in crescita; dati pubblici sui dividendi fermi nelle holding. Costo a regime: circa 1 mld €/anno di minor gettito nella versione piena, meno 0,04-0,33 di gettito dalla regola sulle holding."
    chi: "Decide il Parlamento con la legge di bilancio; attuano Agenzia delle entrate e Sogei, con una microsimulazione del Dipartimento delle finanze prima della legge. Ne beneficiano le imprese di persone che reinvestono, soprattutto sopra 50.000 euro di reddito. Paga chi tiene fermi nella holding, oltre la franchigia, i dividendi della propria società senza reinvestirli; non paga chi preleva tutto, chi reinveste, chi resta forfettario, le SRL che lasciano gli utili nella società."
    oceano_blu:
      eliminare: "Il vantaggio fiscale di chiudere la SNC e aprire una SRL solo per pagare meno sugli utili reinvestiti."
      ridurre: "La distanza di imposta tra forme d'impresa e il rinvio senza fine dei dividendi fermi nella holding."
      aumentare: "La patrimonializzazione delle piccole imprese di persone e la stabilità della regola, che l'IRI non ha avuto."
      creare: "Un conto di reinvestimento per i dividendi della holding: chi investe non paga, chi tiene fermo paga come se avesse incassato."
```
