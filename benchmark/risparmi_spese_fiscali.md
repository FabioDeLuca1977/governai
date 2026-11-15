*Bozza scritta da un agente AI il 15 novembre 2026; da valutare con il panel e da approvare; non rivista da una persona.*

# Nuove coperture dalle spese fiscali (SF20-SF26)

Righe pronte per il panel: `benchmark/bozza_risparmi_spese_fiscali.csv`. Le colonne dei valori (RIS..CIT) sono vuote: le compila il panel.

## In breve

- **7 proposte** su agevolazioni che il menu attuale (SF01-SF16, FN01-FN04) non tocca.
- Gettito totale: **0,47-1,04 mld l'anno a regime**. Il minimo è sicuro solo in parte: 4 proposte su 7 sono di livello 2.
- Non bastano da sole a coprire i 5,3 mld che mancano. Sono un pezzo, accanto alle altre aree.
- Il grosso delle spese fiscali che restano è fatto di **linee rosse**: cuneo fiscale per il lavoro dipendente (8,6 mld), Assegno unico esente (5,6), pensioni di guerra e invalidità (3,9), abitazione principale (3,8). Non le abbiamo toccate.

## Metodo

1. Abbiamo letto tutte le misure del Rapporto MEF sulle spese fiscali 2025 (testo in `dati/raw/01_mef_rapporto_spese_fiscali_2025.txt`, Tavola 1) e le abbiamo ordinate per costo.
2. Abbiamo tolto tre gruppi di misure:
   - quelle già nel menu;
   - i sussidi dannosi per l'ambiente (SAD), che segue un altro agente;
   - le linee rosse (disabilità, non autosufficienza, malattie gravi, prima casa, lavoro dipendente a basso reddito).
3. Abbiamo controllato il ddl di bilancio 2027 (A.C. 3174, relazioni). Serve a evitare due errori: misure in scadenza (non rinnovarle è già nel tendenziale e non è una copertura) e norme spostate nel nuovo testo unico d.lgs. 117/2026.
4. Abbiamo tenuto le misure con almeno una di queste caratteristiche: regressive (beneficio medio alto o legato all'aliquota marginale), settoriali senza una ragione chiara, sovrapposte ad altre.
5. Come si calcola il gettito:
   - **gettito massimo**: costo indicato dal RSF per la parte toccata;
   - **gettito minimo**: stesso costo, meno i cambi di comportamento e le interazioni con altre misure. Le ipotesi sono scritte nella colonna `note`.

## Le proposte

| id | Cosa cambia | Costo RSF della misura | Gettito min-max (mld) | A regime | Livello |
|---|---|---|---|---|---|
| SF20 | Nuovo regime impatriati: per chi arriva dal 2028 la quota esente passa dal 50% al 30% e il tetto da 600.000 a 300.000 € | misura 110-111: 1.062 mln nel 2028 | 0,05-0,15 | 2032 | 2 |
| SF21 | PIR ordinari e PIR-PMI: nessuna nuova sottoscrizione agevolata dal 2028; i piani già aperti restano come sono | 121 + 136: circa 498 mln nel 2028, in crescita | 0,08-0,20 | 2033 | 1 |
| SF22 | Previdenza complementare: oltre 50.000 € di reddito il risparmio d'imposta si ferma al 33% | 391: 2.830 mln | 0,15-0,30 | 2029 | 2 |
| SF23 | Intramoenia: i compensi contano nel reddito al 100% invece che al 75% | 422: 160 mln | 0,10-0,15 | 2028 | 1 |
| SF24 | Rimborsi a chi ha cariche elettive: esclusi dal reddito solo quelli documentati | 423: 85 mln | 0,02-0,05 | 2028 | 1 |
| SF25 | Società agricole sopra 1 mln € di ricavi: fine della tassazione su base catastale e del forfait sulle attività connesse | 20 + 18: circa 280 mln | 0,04-0,09 | 2029 | 2 |
| SF26 | Sport dilettantistico: franchigia di 15.000 € piena fino a 35.000 € di altri redditi; oltre scende a 5.000 € | 425: 652 mln | 0,03-0,10 | 2028 | 2 |

## Chi paga

Il RSF non pubblica la distribuzione per fasce di reddito. Dà però il numero di persone beneficiarie e il beneficio medio, e da qui si capisce chi paga:

- **SF20**: 55.450 persone, beneficio medio **26.746 €**. È la spesa fiscale IRPEF più concentrata del Rapporto. Pagano solo le persone che arrivano dal 2028, con redditi alti.
- **SF21**: chi ha risparmio finanziario. Il numero di persone non è pubblicato. L'esenzione sui redditi finanziari favorisce chi ha patrimonio.
- **SF22**: solo chi ha più di 50.000 € di reddito. Oggi la deduzione fa risparmiare il 43% a chi guadagna di più e il 23% a chi guadagna meno: la proposta riduce questa differenza.
- **SF23**: 117.800 persone, tra medici e dirigenti sanitari, con un beneficio medio di 1.361 €.
- **SF24**: 64.573 persone, tra elette ed eletti e componenti degli organi costituzionali, con un beneficio medio di 1.316 €.
- **SF25**: imprese, non famiglie. Restano fuori le aziende agricole individuali e le società semplici.
- **SF26**: solo chi ha un lavoro principale con reddito sopra 35.000 €. Giovani e collaboratori a basso reddito non sono toccati.

Nessuna proposta tocca chi ha meno, quindi non servono compensazioni.

## Il rischio di doppio conteggio con il Piano strutturale (7,37 mld)

Secondo il RSF (cap. IV), l'obiettivo del PSB è ridurre del 15% il costo delle spese fiscali **vigenti al 31/12/2019**: 7,37 mld su una base di 49,1 mld, entro il 2028. Le misure del riordino sono descritte nella Relazione di monitoraggio di aprile, che non abbiamo letto. Di conseguenza:

- Se una misura **esisteva già nel 2019**, il gettito che produce può servire all'obiettivo PSB oppure al programma GovernAI, non a entrambi. Rischio alto per SF22, SF23, SF24, per la misura 20 di SF25 e per i PIR ordinari di SF21. Rischio medio per SF26.
- Se una misura **è nata dopo il 2019**, è fuori dalla base PSB e il rischio è basso o nullo: nuovo regime impatriati (2024), PIR-PMI (2020), estensione del forfait agricolo (2024).
- **Da fare prima dell'approvazione**: confrontare ogni riga con la Relazione di monitoraggio del PSB (aprile 2026) e con la tabella delle misure discrezionali del DPB 2027.

Il Consiglio UE raccomanda all'Italia di ridurre le spese fiscali ancora in vigore (DPFP 2026, raccomandazioni specifiche). Le proposte vanno in questa direzione.

## Rischi

- **SF20**: meno arrivi di persone qualificate, perché la scelta di residenza dei redditi alti è molto sensibile alle imposte. Per questo il regime per docenti e ricercatori resta intatto. Effetto INN da valutare.
- **SF21**: il mercato delle PMI quotate perde un canale di raccolta. Serve uno strumento diretto al suo posto (area 01, fondo di fondi CDP).
- **SF22**: i redditi alti potrebbero versare meno contributi volontari (FUT). Non cambia nulla per l'adesione automatica dei neoassunti prevista in 02-C3.
- **SF23**: meno offerta intramoenia, che 06-C1 usa come alternativa per garantire i tempi d'attesa. Da coordinare con l'area 06.
- **SF24**: potrebbe arrivare la richiesta di alzare le indennità per compensare. Per le Camere servono anche le modifiche ai regolamenti interni.
- **SF25**: settore con margini bassi. Il gettito dipende molto dalla soglia scelta.
- **SF26**: rischio di più compensi in nero nello sport di base.

## Cosa non sappiamo

- Il costo del solo nuovo regime impatriati: il RSF lo somma al vecchio, e la relazione tecnica del d.lgs. 209/2023 non è stata trovata.
- Come si distribuiscono per classe di reddito le deduzioni per la previdenza complementare (SF22) e i compensi sportivi (SF26). Sono dati da chiedere al Dipartimento delle Finanze.
- Quante persone hanno un PIR e come cresceranno i flussi; quanti rimborsi alle cariche elettive sono forfetari; quanto pesano le società agricole sopra 1 mln € di ricavi.
- L'elenco delle misure contate nel riordino PSB.
- La nuova numerazione del testo unico d.lgs. 117/2026. Gli articoli 225, 226, 246 e 287 sono citati nel ddl 2027; gli altri riferimenti sono quelli del RSF.

## Idee scartate

- **Neo-residenti con imposta fissa di 200.000 €** (misura 520, 74,9 mln). Alzarla porta poco, perché tocca solo i nuovi arrivi, e potrebbe perfino ridurre il gettito: chi rinuncia a venire non paga nemmeno l'imposta fissa. La cifra è già stata raddoppiata nel 2024.
- **Regime IVA speciale degli agricoltori** (misura 2, 500 mln) e **compensazione al 10% per il latte** (misura 23, 62,8 mln). Mancano dati sulla sovracompensazione rispetto all'IVA pagata davvero sugli acquisti. Da studiare, non da proporre ora.
- **Esenzioni IRES delle cooperative agricole e della piccola pesca** (misure 59 e 63, circa 164 mln). Si sovrappongono a SF04 e c'è la tutela dell'art. 45 Cost.
- **Buoni pasto e mense** (misura 400, 845 mln), **fringe benefit** (misura 457, in scadenza nel 2027), **detassazione delle mance**: riguardano il lavoro dipendente, anche a basso reddito. Sono linea rossa.
- **Maxi-deduzione per le nuove assunzioni** (misura 152), **bonus mobili** (misura 215), **esenzione dei redditi agrari per coltivatori diretti e IAP** (misura 24, prorogata solo per il 2027): sono temporanee, quindi non rinnovarle è già nel tendenziale.
- **Forfait del 25% per i diritti d'autore** (misura 167), **regime IVA dell'editoria** (misura 499), **utili degli enti non commerciali al 50%** (misura 556, 18 mln): costi piccoli, finalità culturali o di pluralismo, oppure c'è già un vincolo di reinvestimento.
- **Detrazione per le spese funebri** (misura 315, 147 mln): tocca famiglie in un momento difficile e il beneficio è piccolo.
- **Titoli di Stato esclusi dalla successione** e **aliquota del 12,5% sui titoli pubblici**: il RSF non li conta come spese fiscali (rientrano nel benchmark). Toccarli farebbe anche salire il costo del debito.
- **Detrazione per il rientro di docenti e ricercatori** (misura 288, 87 mln): ha un effetto positivo atteso sull'innovazione. Resta.

## Fonti

- MEF, *Rapporto annuale sulle spese fiscali 2025* (giugno 2026), Tavola 1 e cap. IV: https://www.mef.gov.it/export/sites/MEF/documenti-allegati/2025/RSF-2025-bis.pdf
- Camera dei deputati, A.C. 3174 (ddl bilancio 2027), relazioni illustrativa e tecnica, artt. 11 e 58 e regime impatriati (`dati/raw/00b_ddl_bilancio_2027_AC3174_relazioni.txt`)
- MEF, DPFP 2026 e DPB 2027, raccomandazioni del Consiglio UE sulle spese fiscali (`dati/raw/00b_mef_dpfp_2026.txt`, `dati/raw/00b_mef_dpb_2027.txt`); UPB, audizione sul DPFP 2026 (`dati/raw/00b_upb_audizione_dpfp_2026.txt`)
