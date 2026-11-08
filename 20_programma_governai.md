# Programma GovernAI 1.0

*7 novembre 2026. Un programma di governo né di destra né di sinistra: ogni misura è giudicata sui valori dichiarati nella Carta, è finanziata senza deficit e ha una scheda pronta per l'attuazione.*

> **Aggiornamento del 7 novembre 2026: Carta dei valori 2.0, con 10 valori.**
>
> **Cosa cambia nella Carta.**
> - Nuovi valori: **Equità**, **Sicurezza senza controllo assoluto** e **Cittadinanza responsabile**.
> - Trasparenza e rispetto per le diversità sono ora esplicite dentro Fiducia e Rispetto.
> - Il panel indipendente ha rivalutato tutte le proposte, oggi 62 dopo le 10 nuove su fisco semplice, evasione, PA produttiva e integrità degli appalti (alfa di Krippendorff 0,85).
> - Si applicano le **linee rosse automatiche**. Sono escluse la Difesa nelle versioni a debito e due coperture regressive senza compensazione: l'aumento ulteriore delle accise sul tabacco (AS05) e la soppressione del bonus lavoratrici madri (RB05).
>
> **Nuovi totali**, tutti senza deficit e dopo la verifica giuridica:
> - **programma base: 7,90 mld**, con 17 misure su 18 del nucleo robusto;
> - **programma completo: 12,99 mld**, con 18 su 18.
>
> **Verifica giuridica.** Tre esperti (tributario, costituzionale, diritto UE) hanno escluso perché incompatibili:
> - l'IVA ridotta dal 10% al 12% (SF15): sarebbe una terza aliquota ridotta, vietata dalla direttiva 2006/112/CE come modificata nel 2022;
> - il contributo sui biglietti aerei con importi diversi per voli nazionali e UE (SAD11): viola l'art. 56 TFUE;
> - il prezzo massimo dell'abbonamento ai trasporti locali imposto dallo Stato (04-P3, versione piena): il trasporto pubblico locale è materia regionale;
> - il vincolo dei 3/5 sulle future leggi elettorali (08-P3, versione piena): una legge ordinaria non può vincolare le maggioranze future.
>
> Le altre misure sono compatibili, condizionate o richiedono un passaggio formale, come una notifica alla Commissione o un'intesa con le Regioni (`giuridico/`).
>
> **Nuovo nucleo robusto.** Con l'equità e la cittadinanza tra i valori, salgono:
> - inclusione e comunità: squadre contro la dispersione, scuole aperte, progetto di vita per le persone con disabilità, beni confiscati;
> - giustizia: pena utile, flussi migratori governati dai dati.
>
> **Escono dal nucleo** personale sanitario, treni per i pendolari, Case della Comunità, ricerca, casa e acqua. Restano utili e finanziate nel programma completo, ma ora la loro priorità **dipende dai valori**.
>
> Le tabelle qui sotto si riferiscono alla versione 1 (7 valori). I dati aggiornati ogni giorno sono nel sito (`docs/`) e in `programma/selezione_*.md`.

## 1. In sintesi

- **Due versioni, entrambe finanziate senza deficit** nello scenario prudente, cioè con il gettito minimo delle coperture, senza risparmi non certificati e senza recupero di evasione non certificato:
  - **Programma base: 8,7 mld l'anno.** Usa solo coperture a basso costo sociale: accise sul tabacco, sussidi dannosi minori, spesa della PA, spese fiscali minori.
  - **Programma completo: 15,0 mld l'anno.** Aggiunge coperture strutturali più impegnative, come IVA ridotta, catasto, successioni e cedolare secca.
- **Il nucleo robusto è finanziato.** Sono le 14 misure prioritarie qualunque peso si dia ai valori. Il programma base ne copre 12, quello completo tutte e 14, almeno in versione essenziale: personale sanitario, Case della Comunità, treni per i pendolari, nidi e congedo paterno, ricerca, ITS e residenze universitarie, acqua, prevenzione del dissesto, casa, aree interne, giustizia, "Chiedilo una volta sola", tecnici per i piccoli enti, valutazione delle grandi opere.
- **L'impianto istituzionale di GovernAI c'è in entrambe le versioni** e costa meno di 0,2 mld:
  - la legge sulla consulenza algoritmica pubblica;
  - lo "Stato a vetro";
  - il bilancio generazionale;
  - le spese fiscali a scadenza;
  - la valutazione indipendente delle grandi opere.
- **Restano tre decisioni politiche**, presentate con il loro prezzo esatto (§6):
  - la traiettoria della Difesa;
  - il dividendo climatico;
  - l'adozione delle coperture strutturali.

## 2. Come è stato costruito

| Passo | Cosa | Dove |
|---|---|---|
| 1 | 9 dossier ministeriali, 62 proposte | `ministeri/` |
| 2 | Verifica di 334 cifre su fonte primaria; base dati riproducibile | `dati/` |
| 3 | Vincolo di bilancio ufficiale: margine in deficit zero | `dati/verifiche/00_vincolo_bilancio.md` |
| 4 | Carta dei 7 valori: Rispetto, Fiducia, Innovazione, Benessere, Apprendimento e cultura, Bellezza patrimonio e accoglienza, Responsabilità verso il futuro | `01_carta_valori.md` |
| 5 | Panel di 3 valutatori indipendenti (alfa di Krippendorff 0,84) e motore SMAA su 20.000 combinazioni di pesi | `motore/` |
| 6 | 152 varianti (piena, essenziale, pilota) e 59 misure di copertura concrete | `programma/varianti/`, `programma/coperture_menu.md` |
| 7 | Ottimizzazione: il massimo valore secondo la Carta, interamente finanziato, con priorità al nucleo robusto | `programma/ottimizza.py` |
| 8 | Schede pronte: dato del problema, articolato normativo, cronoprogramma, indicatori | `programma/schede/` |

## 3. Le misure

**Classe** indica il giudizio del motore:
- **Nucleo**: prioritaria con ogni combinazione di pesi;
- **Valori**: la priorità dipende dai valori;
- **Coda**: utile ma in fondo alla classifica;
- **Sfav.**: sfavorevole.

Costi in mld €/anno a regime. "—" = non inclusa.

| # | Misura | Classe | Programma base | Programma completo |
|---|---|---|---|---|
| **Economia, Imprese, Turismo** | [schede](programma/schede/01_economia.md) | | | |
| 01-P1 | Bilancio generazionale: ogni legge dichiara chi paga e quando | Valori | Piena 0,02 | Piena 0,02 |
| 01-P2 | Spese fiscali a scadenza (sunset 5 anni) | Valori | Piena 0,01 | Piena 0,01 |
| 01-P3 | IVA in tempo reale | Valori | Piena 0,15 | Piena 0,15 |
| 01-P4 | Crescere conviene: eliminare i gradini dimensionali | Valori | Zero 0,01 | Zero 0,01 |
| 01-P5 | Energia a prezzo stabile per le PMI | Coda | Pilota 0,05 | — |
| 01-P6 | Turismo che ripaga i territori: tassa di soggiorno intelligente | Valori | Piena 0,15 | Piena 0,15 |
| **Lavoro, Welfare, Famiglia** | [schede](programma/schede/02_lavoro.md) | | | |
| 02-C1 | Salario minimo contrattuale garantito | Valori | Zero 0,00 | Piena 0,35 |
| 02-C2 | Nido esigibile + congedo paterno | **Nucleo** | — | Essenziale 2,00 |
| 02-C3 | Patto previdenziale tra generazioni (ridisegnato: contributo triennale) | Valori | Essenziale 0,35 | Essenziale 0,35 |
| 02-C4 | Reddito di inclusione universale | Valori | — | — |
| 02-C5 | Progetto di vita e lavoro per le persone con disabilità | Valori | Zero 0,00 | Zero 0,00 |
| 02-C6 | Strategia demografica | Valori | Zero 0,00 | Piena 0,40 |
| **Ambiente, Energia, Agricoltura** | [schede](programma/schede/03_ambiente.md) | | | |
| 03-P1 | Dividendo climatico | Valori | Zero 0,00 | Zero 0,00 |
| 03-P2 | Elettricità rinnovabile a prezzo rinnovabile (CfD) | Valori | Piena 0,15 | Piena 0,15 |
| 03-P3 | Ogni goccia conta: reti idriche e riuso | **Nucleo** | Essenziale 0,60 | Essenziale 0,60 |
| 03-P4 | Prevenire costa meno: prevenzione e assicurazione catastrofale | **Nucleo** | Essenziale 0,80 | Essenziale 0,80 |
| 03-P5 | Contratto agro-climatico | Valori | — | Essenziale 0,25 |
| **Infrastrutture, Territori** | [schede](programma/schede/04_infrastrutture.md) | | | |
| 04-P1 | Patto di continuità post-PNRR | Valori | Pilota 0,09 | Pilota 0,09 |
| 04-P2 | Casa a canone giusto | **Nucleo** | Essenziale 0,48 | Essenziale 0,48 |
| 04-P3 | Prima il treno dei pendolari | **Nucleo** | Essenziale 1,17 | Essenziale 1,17 |
| 04-P4 | Nessuna grande opera senza prova dei numeri | **Nucleo** | Piena 0,03 | Piena 0,03 |
| 04-P5 | LEP prima: autonomia differenziata reversibile | Valori | Zero 0,00 | Zero 0,00 |
| 04-P6 | Restare è possibile: servizi nelle aree interne | **Nucleo** | Essenziale 0,42 | Essenziale 0,42 |
| **Istruzione, Ricerca, Cultura** | [schede](programma/schede/05_istruzione.md) | | | |
| 05-C1 | Nessuno escluso: squadre contro la dispersione | Valori | Piena 0,25 | Piena 0,25 |
| 05-C2 | Conto personale di competenze | Valori | — | — |
| 05-C3 | Carriere della ricerca | **Nucleo** | Zero 0,00 | Essenziale 1,50 |
| 05-C4 | Più laureati e diplomati terziari: ITS e residenze | **Nucleo** | Essenziale 0,45 | Essenziale 0,45 |
| 05-C5 | Scuole aperte come presidi di comunità | Valori | Pilota 0,04 | Piena 0,40 |
| 05-C6 | AI a scuola | Coda | Zero 0,00 | Piena 0,22 |
| **Salute** | [schede](programma/schede/06_salute.md) | | | |
| 06-C1 | Tempo garantito o rimborso | Valori | Zero 0,00 | Zero 0,00 |
| 06-C2 | Patto per infermieri e medicina generale | **Nucleo** | Essenziale 1,40 | Essenziale 1,40 |
| 06-C3 | Case della Comunità vive | **Nucleo** | Essenziale 0,80 | Essenziale 0,80 |
| 06-C4 | Budget di cura per la non autosufficienza | Valori | — | — |
| 06-C5 | Salute mentale al 5% | Valori | — | — |
| 06-C6 | Dividendo della prevenzione e budget unico del farmaco | Valori | Zero 0,00 | Zero 0,00 |
| **Giustizia, Interno, Difesa** | [schede](programma/schede/07_giustizia.md) | | | |
| 07-C1 | Giustizia a regime: Ufficio per il processo | **Nucleo** | Essenziale 0,32 | Essenziale 0,32 |
| 07-C2 | Pena utile: misure di comunità | Valori | Pilota 0,06 | Piena 0,45 |
| 07-C3 | Flussi migratori governati dai dati | Valori | Pilota 0,04 | Essenziale 0,25 |
| 07-C4 | Dal bene confiscato al bene comune | Valori | Piena 0,15 | Piena 0,15 |
| 07-C5 | Difesa | Sfav. | — (stabile al 2,1%) | — (stabile al 2,1%) |
| 07-C6 | Scudo cyber territoriale | Valori | Pilota 0,03 | Piena 0,35 |
| **Esteri, Europa, Istituzioni** | [schede](programma/schede/08_esteri.md) | | | |
| 08-P1 | **Legge GovernAI** sulla consulenza algoritmica pubblica | Valori | Piena 0,04 | Piena 0,04 |
| 08-P2 | Patto per la buona legge | Coda | Piena 0,01 | Piena 0,01 |
| 08-P3 | Regole del gioco stabili, voto fuorisede | Coda | Piena 0,03 | Piena 0,03 |
| 08-P4 | Beni pubblici europei | Coda | Piena 0,00 | Piena 0,00 |
| 08-P5 | Cooperazione allo sviluppo | Coda | Zero 0,00 | Zero 0,00 |
| 08-P6 | Export resiliente | Coda | — | Pilota 0,03 |
| **PA e Digitale** | [schede](programma/schede/09_pa_digitale.md) | | | |
| 09-C1 | **Stato a vetro**: infrastruttura aperta per l'analisi delle politiche | Valori | Piena 0,07 | Piena 0,07 |
| 09-C2 | Chiedilo una volta sola | **Nucleo** | Essenziale 0,14 | Essenziale 0,14 |
| 09-C3 | Tecnici della Repubblica per i piccoli enti | **Nucleo** | Essenziale 0,22 | Piena 0,55 |
| 09-C4 | Cloud pubblico e manutenzione digitale | Coda | Zero 0,00 | Zero 0,00 |
| 09-C5 | AI nella PA con supervisione umana | Valori | Piena 0,22 | Piena 0,22 |
| | **Totale** | | **8,73** | **15,04** |

Come leggere le varianti:
- **Zero**: riforma di metodo senza costo, ad esempio un obbligo, una regola o un riordino;
- **Pilota**: sperimentazione con valutazione;
- **Essenziale**: il cuore della misura, graduale o mirato.

Il dettaglio di ogni variante è nelle schede.

**Robustezza:** l'ottimizzazione è stata ripetuta su 300 combinazioni di pesi tra i valori. Nella versione base 31 misure su 44 entrano nel programma ottimo in almeno l'80% dei casi, in quella completa 33 su 46. Il programma, cioè, cambia poco al variare della sensibilità politica (`programma/selezione_livello1.md`, `selezione_livello2.md`).

## 4. Le coperture

Il dettaglio è in `programma/coperture_menu.md`: 59 misure con gettito, chi paga e fonte. I valori sono in mld €/anno, gettito minimo.

| Fondo | Programma base | Programma completo |
|---|---|---|
| Sussidi ambientalmente dannosi (voci specifiche del Catalogo MASE) | 1,38 | 2,83 |
| Spese fiscali (oltre i 7,37 già nel Piano strutturale) | 1,25 | 4,75 |
| Accise salute (tabacco, bevande zuccherate, superalcolici) | 0,97 | 1,37 |
| Spending review (acquisti centralizzati, locazioni passive, consulenze, incentivi senza valutazione) | 1,49 | 2,49 |
| Riordino di bonus e carte | 0,98 | 0,98 |
| Pensioni (contributo triennale sopra 10 volte il minimo; rivalutazione ridotta delle pensioni più alte) | 0,38 | 0,38 |
| Tassa di soggiorno (Comuni) | 0,11 | 0,11 |
| **Totale coperture nuove** | **6,56** | **12,91** |

Il resto della spesa si finanzia con fondi già vincolati: coesione 2021-27 (solo investimenti una tantum), tariffe del servizio idrico e corrispettivi GSE.

**Le misure di copertura più rilevanti**
- *Programma base*:
  - accisa sulle sigarette +0,50 € a pacchetto in due tappe;
  - rimborso del gasolio per l'autotrasporto escluso per i veicoli Euro 5 e ridotto per gli Euro 6;
  - regime forfetario al 20% tra 50.000 e 85.000 € di ricavi;
  - acquisti centralizzati;
  - taglio degli incentivi alle imprese privi di una valutazione d'impatto positiva.
- *In più, nel programma completo*:
  - aliquota IVA ridotta dal 10% al 12%, esclusi gli alimentari di base, con compensazione per il 30% più povero;
  - revisione degli estimi catastali e IMU sulle prime case di valore alto, con salvaguardia ISEE;
  - abolizione della cedolare secca a canone libero;
  - franchigia di successione ridotta;
  - uscita dal rimborso del gasolio entro il 2035;
  - revisione strutturale della spesa dei ministeri.

## 5. Primi 100 giorni

Ogni scheda riporta il cronoprogramma dettagliato: 100 giorni, 12 mesi, fine legislatura, con chi fa cosa. In sintesi:

1. **Legge GovernAI** (08-P1, 10 articoli) e **Stato a vetro** (09-C1) in Consiglio dei ministri. Nascono l'Ufficio per la consulenza algoritmica presso le Camere, il registro pubblico delle analisi e l'assemblea dei cittadini sorteggiati, che fisserà i pesi tra i valori.
2. **Legge di bilancio**:
   - i fondi delle misure del nucleo;
   - le coperture del livello scelto;
   - la regola "nessun rinnovo automatico" per le misure temporanee;
   - il bilancio generazionale allegato a ogni provvedimento (01-P1).
3. **Decreti attuativi**:
   - piattaforma "tempo garantito" per le liste d'attesa;
   - soglie di carenza del personale sanitario;
   - elenco degli ambiti con meno del 33% di posti al nido;
   - fondo per il trasporto pubblico locale;
   - censimento degli alloggi pubblici vuoti.
4. **Disegni di legge delega**: salario minimo contrattuale, patto previdenziale, riordino degli incentivi.

## 6. Le decisioni politiche che restano

Il sistema non decide al posto dei cittadini. Su questi tre punti presenta le opzioni con il loro prezzo esatto, calcolato con lo stesso ottimizzatore.

**1. Difesa.** Oggi la spesa è al 2,09% del PIL secondo la NATO (luglio 2026).

| Opzione | Costo aggiuntivo a regime | Cosa comporta per il programma completo |
|---|---|---|
| Stabilizzazione al ~2,1% con efficienza e acquisti comuni UE | 0 | Programma completo invariato |
| Traiettoria graduale legata al debito (2,5% nel 2034) | +9,1 mld | **Escono** nidi, personale sanitario, legge GovernAI e Stato a vetro, IVA in tempo reale, misure su carceri, flussi e cyber. La ricerca scende a zero |
| Obiettivo NATO 3,5% al 2035 | +32 mld | **Non finanziabile** senza deficit: supera tutte le coperture disponibili |

**2. Dividendo climatico.** L'ottimizzatore usa il gettito dei sussidi dannosi per i servizi e non per il dividendo. Imporre il dividendo compensativo per redditi bassi e settori esposti (1,2 mld) costa al programma completo:
- il salario minimo, che passa alla sola versione di metodo;
- metà del contratto agro-climatico;
- parte dei tecnici per i piccoli enti.

**3. Coperture strutturali** (programma completo). Valgono 6,3 mld in più. Finanziano nidi, ricerca, salario minimo, scuole aperte, misure sulla giustizia e cyber. Le pagano soprattutto:
- i consumatori, con l'IVA al 12% compensata per i redditi bassi;
- i proprietari di case di valore alto;
- i locatori a canone libero;
- gli eredi di grandi patrimoni;
- l'autotrasporto, che però ha tempo fino al 2035.

## 7. Cosa manca e cosa fare dopo

- **Costi stimati, non certificati.** I costi delle varianti e molti gettiti sono "stime GovernAI". Il passo successivo è la verifica con la Ragioneria o con l'UPB, e microsimulazioni distributive su microdati, che richiedono un accesso istituzionale.
- **Doppioni da escludere.** Le spese fiscali del menu vanno confrontate voce per voce con la lista dei 7,37 mld già nel Piano strutturale.
- **Utilità delle varianti.** È calcolata come intensità × utilità della proposta piena. Il panel dovrebbe valutare direttamente le varianti essenziali e le misure di copertura, oggi valutate da un solo agente.
- **Proposte escluse ma di valore.** Salute mentale, non autosufficienza e reddito di inclusione sono escluse per mancanza di risorse, non perché siano di poco valore. Rientrano in ordine di priorità man mano che si certificano nuove coperture, ad esempio il recupero dell'evasione IVA a consuntivo.
- **Red team.** Prima della pubblicazione serve una revisione critica da prospettive politiche diverse, per verificarne la neutralità.
