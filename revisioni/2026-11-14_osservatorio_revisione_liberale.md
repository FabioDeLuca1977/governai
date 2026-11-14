# Revisione A dell'Osservatorio: sensibilità liberale e conservatrice

*Revisione scritta da un agente AI a cui è stata data questa sensibilità politica, non da una persona. Le correzioni sono state applicate ai commenti di `osservatorio/atti/` da un altro agente AI, che ha scartato quelle non confermate dalle fonti.*

*14 novembre 2026. Ho rivisto i 21 commenti in `osservatorio/atti/` e confrontato i punti a campione con: testo A.C. 3174, relazioni tecniche, DPB 2027, testi GU dei decreti e `giurisprudenza_verificata.json`. Nessun file del repository è stato modificato.*

## Giudizio d'insieme

1. **Equilibrio complessivo: discreto, con una tendenza costante.** I tagli di tasse (bollo, IRPEF, forfettario) vengono letti come un costo per "tutti i contribuenti". Le imposte su banche, assicurazioni ed energia vengono lette come "entrate certe pagate da chi ha più capacità". Per le misure temporanee il commento segna FID "-" perché sono incerte. Per quelle permanenti segna FUT "-" perché costano. Così l'atto perde in entrambi i casi.
2. **Punti forti.** Le sezioni `governai` sono oneste e spesso più severe con GovernAI che con il Governo. I numeri presi dalle relazioni tecniche reggono quasi sempre. In ogni commento i pregi sono detti.
3. **Rischi di fatto.** C'è qualche errore verificato: la "quarta proroga" del bingo, la "maggioranza semplice" della legge elettorale, il bollo "in deficit", la quota libera della sanità contata tra le somme vincolate, il 138,5% attribuito all'UPB. Ci sono anche omissioni che cambiano il giudizio: la clausola di salvaguardia sulle pensioni, la rinuncia agli interessi per i concessionari, i requisiti di fatto per il trattenimento di polizia.
4. **Giurisprudenza.** Nove sentenze citate non sono in `giurisprudenza_verificata.json`. Sono quasi certamente esistenti e pertinenti, ma vanno verificate e aggiunte al file prima di pubblicare.
5. **Linguaggio.** Ci sono ricorrenze polemiche ("ennesima", "per l'ennesima volta"), una frase da militante nel commento sulla difesa, parole inglesi evitabili ("plastic e sugar tax") e una cornice fuorviante: "tassa all'1%" e "tassa al 5%" per quelle che sono riduzioni di imposta.

---

## Correzioni trasversali (valgono per più file)

- TUTTI | `rischi_giuridici` e `fonti` | FATTO, da verificare: queste sentenze **non sono** in `giurisprudenza_verificata.json`: 130/2023 (pensioni), 58/2018 e 85/2013 (ex ILVA), 168/1994, 263/2019 e 24/2019 (sicurezza minori), 186/2013 (Campi Flegrei), 1/2014 e 35/2017 (elettorale) | Verificarle e aggiungerle al file. Finché non è fatto, scrivere accanto a ciascuna "(da verificare)".
- sanità, irpef-lavoro-forfettario, lavoro-giovani-e-madri | `chi_guadagna` | FATTO, affermazione senza fonte: "richiesta storica dei sindacati", "i loro ordini e associazioni chiedevano da tempo", "una misura cercata dai sindacati del pubblico impiego" (regola 7) | Citare una fonte (piattaforma, audizione) oppure togliere l'inciso e lasciare solo la categoria che guadagna.
- energia-ferrovie, irpef, bollo | `chi_paga`, `valori FUT`, `numeri` | EQUILIBRIO e FATTO: il debito al 138,5% del PIL nel 2027 è citato come effetto delle misure. Il DPB (par. I.7) dice che è "determinato in larga misura dall'impatto di cassa dei crediti d'imposta connessi ai bonus edilizi" | Quando si cita il 138,5%, aggiungere: "soprattutto per la cassa dei crediti dei bonus edilizi degli anni passati (MEF, DPB 2027, par. I.7)".
- banche vs bollo e irpef | `valori` | EQUILIBRIO, doppio standard: le maggiori entrate da banche ed energia hanno FUT "+" ed EQU "+". I tagli di imposta alle famiglie hanno FUT "-" anche quando rientrano nella copertura complessiva della manovra | Usare lo stesso metro: un taglio coperto dentro i saldi non è deficit. Un'imposta permanente su un settore va giudicata anche per gli effetti su credito, prezzi e investimenti, non solo per il gettito.
- evasione-crediti, giochi, ex-ilva, autotrasporto | vari | LINGUAGGIO: "per l'ennesima volta", "ennesima proroga", "ennesima misura", "Ennesimo decreto" | Sostituire con il dato: "la quarta proroga", "il sesto decreto del 2026 sui carburanti", oppure togliere.
- evasione-crediti | `in_breve`, `cosa_fa`, `numeri`, `chi_guadagna` | LINGUAGGIO: "plastic e sugar tax" | "imposte sulla plastica monouso e sulle bevande zuccherate".

---

## Correzioni per file

### manovra-2027-sanita-fondo-e-personale.yaml
- `numeri` (quote vincolate) e `in_breve` | FATTO: tra le quote "già vincolate" è contata la "quota libera alle Regioni 138", che per definizione non è vincolata (art. 69, c. 7). Senza di essa il vincolato è circa 1.441 mln | "circa 1.440 mln su 2.365 hanno una destinazione per legge, più 138 mln liberi per le Regioni". In `in_breve`: "Circa 1,4 miliardi hanno già una destinazione per legge".
- `in_breve` | FATTO: parla di "spesa sanitaria pubblica programmata" che scende al 5,9% nel 2029, ma il dato è il **fondo sanitario** sul PIL e per il 2029 non è verificato (la serie dice "livello Gimbe") | "Il fondo sanitario in rapporto al PIL scende dal 6,1% del 2027 a circa il 6,0% del 2028; il dato 2029 è ancora da verificare".
- `bilancio` | EQUILIBRIO: "quasi tutto l'aumento sia già speso prima di arrivare ai servizi". Tariffe dei ricoveri, indennità del pronto soccorso, ore contro le attese e Alzheimer *sono* servizi | "Non bene che due terzi dell'aumento siano già vincolati per legge, lasciando poco margine alle Regioni".
- `chi_guadagna` (secondo punto) | FATTO, senza fonte: "richiesta storica dei sindacati" | Vedi le correzioni trasversali.

### manovra-2027-payback-farmaci-dispositivi.yaml
- `chi_guadagna` (industria farmaceutica) | FATTO, senza fonte: "in pratica le più grandi" | "probabilmente le imprese con più capacità di investimento (stima: i criteri li fissa il decreto)".
- `chi_paga` (pazienti e servizi) e `valori FUT` | EQUILIBRIO: farmaci e dispositivi sono cure per i pazienti, non un'alternativa ai "servizi" | "circa 440 mln l'anno del fondo vanno a farmaci e dispositivi già consumati oltre i tetti, invece che a personale o a nuove prestazioni".
- `valori INN` | EQUILIBRIO, pregio taciuto: l'investimento produttivo e di ricerca in Italia porta lavoro qualificato | Aggiungere: "attirare produzione e ricerca farmaceutica ha valore per il lavoro e la sicurezza degli approvvigionamenti".

### manovra-2027-difesa-clausola-ue.yaml
- `chi_guadagna` (ultimo punto) | LINGUAGGIO ed EQUILIBRIO, frase da militante: "Il Governo in carica: spende oggi senza dover trovare subito la copertura con tagli o tasse" | Togliere il punto. Il concetto è già in `chi_paga` e in `valori FUT`.
- `valori EQU` | EQUILIBRIO: la difesa è un bene pubblico per tutti. Leggerla come beneficio "concentrato su poche imprese" è parziale | "Il costo futuro ricade su tutti; il beneficio di sicurezza è di tutti, quello economico immediato è concentrato su alcune imprese e territori".
- `rischi_giuridici` e `valori FID` | EQUILIBRIO: le Camere hanno votato il 13/10/2026 le risoluzioni sulla Relazione ex art. 6 L. 243/2012 (verificato: DPB, nota 20). Il problema è che il testo non le richiama e che gli importi non sono confrontati, non che manchi l'autorizzazione | In FID: "Il testo non richiama la deliberazione delle Camere del 13/10/2026 né gli importi autorizzati; manca un piano pubblico su costi e capacità".

### manovra-2027-pensioni-e-anziani.yaml
- `chi_paga` (secondo punto) e `valori EQU -` | FATTO, omissione decisiva: l'art. 55 contiene, per ogni soglia, una clausola di salvaguardia ("l'aumento di rivalutazione è comunque attribuito fino a concorrenza del predetto limite maggiorato"). Chi sta appena sopra una soglia non finisce sotto chi stava appena sotto | "Chi ha un assegno appena sopra 5 volte il minimo riceve il 53% sull'intero importo, ma una clausola gli garantisce almeno quanto spetta a chi è sul limite. Il salto resta, ma attenuato". Va rivista anche la proposta "per fasce" in `cosa_cambieremmo`: il guadagno di equità è minore di quanto suggerito.
- `chi_guadagna` (dipendenti pubblici) | FATTO, da verificare: la sent. 130/2023 non è nel file verificato | Vedi le correzioni trasversali.

### manovra-2027-scuola-universita.yaml
- `chi_paga` (ultimo punto) e `valori EQU` | EQUILIBRIO, doppio standard: "Tutti i contribuenti per il buono paritarie". Le famiglie che scelgono una paritaria pagano le tasse anche per la scuola statale. Le paritarie fanno parte del sistema nazionale di istruzione (L. 62/2000) e un alunno in paritaria costa allo Stato meno di uno in statale | Togliere il punto da `chi_paga` (20 mln). In EQU tenere solo il taglio uniforme.
- `chi_guadagna` | LINGUAGGIO: "Scuole paritarie e i loro gestori, anche religiosi" | "Scuole paritarie: più iscrizioni sostenute".
- `in_breve` | FATTO, impreciso: "i 271 mln l'anno passano al fondo ordinario". L'art. 107, c. 1 li destina a "progetti strategici delle università", ripartiti *con le modalità* del fondo ordinario | "i 271 mln l'anno vanno a progetti strategici degli atenei, ripartiti con i criteri del fondo ordinario".
- `valori INN -` | EQUILIBRIO: "i fondi si spalmano su tutti". Il riparto del fondo ordinario ha già una quota premiale legata alla valutazione della ricerca | "Finisce un premio selettivo per dipartimento; i fondi seguono i criteri del fondo ordinario, che hanno una quota premiale meno mirata".
- `rischi_giuridici` | FATTO: la sent. 80/2010 riguarda i posti di sostegno, non il tempo pieno | "non tocca i posti di sostegno (sent. 80/2010) e, per prudenza, il tempo pieno".

### manovra-2027-comuni-debiti-avanzo.yaml
- `valori BEN` | LINGUAGGIO: "soffocato dal disavanzo" | "Un Comune con meno disavanzo".
- Nessun altro rilievo: il commento è equilibrato e già severo con chi ha accumulato debiti.

### manovra-2027-lavoro-giovani-e-madri.yaml
- `in_breve`, `numeri`, `chi_paga`, `cosa_cambieremmo` | LINGUAGGIO e cornice fuorviante: "una tassa all'1%". È una riduzione: un'imposta dell'1% al posto dell'IRPEF | "imposta ridotta all'1% (al posto dell'IRPEF) sugli aumenti dei giovani".
- `titolo` | LINGUAGGIO: troppo lungo (più di 30 parole) | "Famiglie e lavoro: bonus stabile per le madri, un mese in più di congedo all'80%, sconti di un anno su giovani e assunzioni".
- `cosa_fa` (bonus madri) | FATTO, incompleto: il bonus dura fino ai 10 anni del secondo figlio (con due figli) o ai 18 del più piccolo (con tre o più); "senza scadenza" vale per la misura, non per la singola madre | Aggiungere i limiti di età dei figli.
- `chi_paga` (ultimo punto) | EQUILIBRIO: il conto "Valore nuovi nati" è un risparmio *a favore* di chi verrà dopo. Elencarlo tra chi paga è incoerente | "Il bilancio futuro: il bonus madri e il conto nuovi nati sono spese permanenti e crescenti".

### manovra-2027-lep-tpl-regioni.yaml
- Nessun rilievo di fatto o di equilibrio. Il rispetto delle autonomie è riconosciuto (RIS "+"). Si può pubblicare così.

### manovra-2027-energia-ferrovie-in-deficit.yaml
- `chi_paga` (primo punto) | FATTO: il 138,5% è attribuito all'UPB, ma è del MEF (DPB, par. I.7), ed è dovuto soprattutto ai crediti dei bonus edilizi | "aumenta il debito; nel 2027 il debito arriva al 138,5% del PIL, soprattutto per la cassa dei bonus edilizi (MEF, DPB 2027)".
- `valori FID` | FATTO, da verificare: "la variante del Terzo valico non ha una valutazione costi-benefici pubblica". L'opera nel suo insieme ha avuto analisi del Ministero | "non risulta una valutazione costi-benefici pubblica della variante (da verificare)".
- `rischi_giuridici` | EQUILIBRIO: "diventa illegittimità probabile se manca l'autorizzazione". Il commento stesso dice che le risoluzioni sono state approvate il 13/10 | "Dubbio da chiudere: verificare che gli importi per anno rientrino in quelli autorizzati dalle Camere il 13/10/2026 e richiamarli nella norma".

### manovra-2027-evasione-crediti.yaml
- `cosa_fa` (art. 38) | FATTO, incompleto: la targa personalizzata costa 10.000 euro alle imprese solo fino al 31/5/2027, poi 5.000; alle persone 1.000 e poi 500. Il gettito va ai Comuni fino a 50.000 abitanti, non ai "piccoli Comuni" | "targhe personalizzate a pagamento (imprese 10.000 euro fino a maggio 2027, poi 5.000; persone 1.000, poi 500), con gettito ai Comuni fino a 50.000 abitanti per le strade".
- `chi_guadagna` (ultimo punto) | LINGUAGGIO: "sei mesi in più senza imposta, per l'ennesima volta" | "sei mesi in più senza imposta; è un nuovo rinvio".
- `valori FID +` ed `EQU +` | EQUILIBRIO: la ritenuta del 2% colpisce anche chi paga regolarmente, e la relazione tecnica non distingue fra evasione recuperata e anticipo di imposta (lo dice la domanda aperta) | In EQU: "Se recupera evasione, rende il prelievo più giusto; se anticipa imposte già dovute, pesa sulla liquidità di chi è in regola".

### manovra-2027-giochi.yaml
- `chi_guadagna` (primo punto) | FATTO, errore verificato: "alla quarta proroga per il bingo". L'art. 27, c. 2 elenca le proroghe precedenti: L. 205/2017, L. 145/2018, d.l. 124/2019, L. 178/2020, L. 197/2022, L. 207/2024. Questa è almeno la settima | "alla settima proroga per il bingo dal 2017".
- `cosa_fa` (art. 32) e `chi_guadagna` | FATTO, omissione e favoritismo non detto: oltre allo sconto fino al 20%, l'art. 32, c. 3 prevede "la rinuncia dell'erario alla riscossione degli interessi maturati" | "chiude con uno sconto fino al 20% e senza interessi il debito residuo…"; in `chi_guadagna`: "pagano fino al 20% in meno e nessun interesse".
- `bilancio` | LINGUAGGIO ed EQUILIBRIO: "a scapito di concorrenza e legalità". I concessionari sono operatori legali; la lite sul prelievo 2015 è un contenzioso, non illegalità | "a scapito della concorrenza e della parità di trattamento con chi ha pagato".
- `valori CIT` | LINGUAGGIO: "Lo Stato spinge una attività che dovrebbe solo controllare" | "Lo Stato aumenta l'offerta di gioco che deve regolare".
- `chi_guadagna` o `valori SIC` | EQUILIBRIO, pregio taciuto: la proroga evita un vuoto di concessioni che favorirebbe il gioco illegale (finalità dichiarata nell'art. 23, c. 3 e nell'art. 26) | Aggiungere: "La continuità delle concessioni evita che la domanda passi al gioco illegale, in attesa delle gare".

### manovra-2027-irpef-lavoro-forfettario.yaml
- `titolo`, `in_breve` | LINGUAGGIO e cornice: "tassa al 5% sugli aumenti" | "imposta ridotta al 5% sugli aumenti dei contratti".
- `domande_aperte` (secondo punto) e `cosa_cambieremmo` (terzo punto) | FATTO: l'art. 6 dice testualmente "soltanto ai lavoratori del settore privato". La domanda ha già risposta | Domanda da togliere. Correttivo: "Estendere la stessa imposta ridotta ai rinnovi del pubblico impiego, oggi esclusi per legge".
- `chi_guadagna` (primo punto) e `bilancio` | EQUILIBRIO, pregio taciuto: il ceto medio tra 50.000 e 55.000 euro paga il 43% a una soglia bassa nel confronto europeo e subisce il drenaggio fiscale, che lo stesso commento cita (UPB, 1,6 mld per punto di inflazione) | In `chi_guadagna`: "…fino a 500 euro, solo nel 2027: riduce per un anno il salto al 43%, che in Italia scatta a un reddito basso". In `bilancio`: riconoscere che restituisce una parte del drenaggio al ceto medio, prima di criticarne la durata di un anno.
- `valori FUT` | FATTO e cornice: "Gettito ceduto senza copertura propria". In una legge di bilancio la copertura è complessiva: fuori dalla clausola, la manovra è coperta da entrate e tagli (DPB, Tabella I.6-1) | "Il minore gettito è coperto dentro i saldi della manovra e non da una fonte dedicata; il forfettario è permanente".

### manovra-2027-banche-assicurazioni-energia.yaml
- `valori EQU +` | EQUILIBRIO: i "margini alti con i tassi" sono ciclici, mentre l'aumento IRAP dell'art. 19 è permanente. Il commento lo nota altrove, ma in EQU lo tace | "Chiede un contributo a settori con margini alti negli ultimi anni; ma l'IRAP dell'art. 19 resta anche quando i margini scendono".
- `chi_paga` | EQUILIBRIO, omissione: un prelievo permanente sulle banche può passare nel costo del credito alle imprese, soprattutto PMI, e il commento parla solo di "clienti" | Aggiungere: "Le piccole imprese che dipendono dal credito bancario, se il maggior costo passa nei tassi".
- `cosa_fa` (art. 18) | FATTO, incompleto: l'art. 18, c. 2 alza anche il limite dell'imposta sulle riserve matematiche dei rami vita (dall'1,25 all'1,285%) | Aggiungere una riga.
- Nota di copertura (fuori da questo file): l'art. 17 (imposta in uscita per le persone che trasferiscono la residenza con patrimoni da 800.000 euro) non è commentato in nessuna scheda. Tocca libertà economica e mobilità ed è da valutare per una scheda futura.

### manovra-2027-bollo-auto.yaml
- `valori FUT` | FATTO: "Spesa permanente di 2,3 mld l'anno in deficit". Secondo il DPB (par. I.5 e Tab. I.6-1) l'aumento del deficit (+0,5 punti) viene da difesa ed energia con la clausola. Il resto della manovra è coperto | "Spesa permanente di 2,3 mld l'anno senza una copertura dedicata, e sussidio alle auto a benzina e gasolio…".
- `chi_paga` (secondo punto) | EQUILIBRIO, affermazione senza fonte: "Chi non ha l'auto, spesso persone anziane o con redditi bassi… paga con le tasse senza ricevere nulla". La misura è coperta soprattutto da banche, assicurazioni ed energia | "Chi non ha l'auto non riceve nulla da questa misura".
- `cosa_cambieremmo` (secondo punto) e `chi_paga` (auto elettriche) | FATTO, contesto mancante: le auto elettriche sono già esenti dal bollo per cinque anni e poi pagano in misura ridotta, con esenzioni regionali più lunghe (da verificare sul testo vigente) | "Chi ha un'auto elettrica è già in parte esente…"; il correttivo diventa "Coordinare l'esenzione con quella già prevista per le auto elettriche, per non premiare la combustione".
- `valori FID` | EQUILIBRIO, pregio taciuto: un'esenzione permanente e automatica dà certezza alle famiglie, cioè il contrario dei bonus di un anno che altri commenti criticano | Aggiungere: "ed è stabile e automatica, senza domande".

### manovra-2027-revisione-spesa-rinvii.yaml
- `valori SIC` | LINGUAGGIO ambiguo: "si dimezza ogni anno" | "scende da 60 a 30 mln l'anno e si allunga di due anni".
- Per il resto il commento è equilibrato e riconosce i tagli permanenti di spesa corrente.

### dl-2026-185-ex-ilva.yaml
- `in_breve` e `valori FID` | LINGUAGGIO: "l'ennesima misura caso per caso", "Ennesimo decreto sull'ex ILVA" | "un'altra misura caso per caso"; "Un altro decreto sull'ex ILVA…".
- `valori FID` | EQUILIBRIO: "una norma che interferisce con un giudizio in corso" presenta come fatto un giudizio. La norma dice di non voler aggirare la decisione e mette un termine | "una norma sugli impianti adottata mentre è pendente un giudizio".
- `chi_paga` (residenti) o `valori FUT` | EQUILIBRIO, pregio taciuto: tenere caldi gli altoforni preserva il valore degli impianti nella vendita (lo spegnimento è difficilmente reversibile) e quindi le possibilità di recupero per creditori e contribuenti | Aggiungere: "Tenere caldi gli impianti ne preserva il valore per la vendita".
- `rischi_giuridici`, `fonti` | FATTO, da verificare: le sent. 58/2018 e 85/2013 non sono nel file verificato.

### dl-2026-190-sicurezza-minori.yaml
- `cosa_fa` (art. 7), `chi_paga` (terzo punto), `valori RIS`, `cosa_cambieremmo`, `rischi_giuridici` | FATTO, rappresentazione inesatta: il nuovo c. 3-ter richiede "specifiche e concrete circostanze di tempo e di luogo e di elementi di fatto" e un "fondato motivo di ritenere" che la persona ponga in essere "condotte di concreto pericolo". Precedenti e segnalazioni sono solo uno degli elementi, limitati a certi reati e agli ultimi cinque anni. "In base a sospetti, senza un fatto preciso" non è corretto | `chi_paga`: "Persone con precedenti o segnalazioni per alcuni reati: possono essere trattenute se ci sono elementi concreti di pericolo, con una formula ampia". `rischi_giuridici`: tenere il dubbio sulla vaghezza di "luoghi con consistente afflusso" e sul peso delle sole segnalazioni.
- `domande_aperte` (secondo punto) | FATTO: il c. 3-ter richiama i commi 2, 3 e 3-bis dell'art. 11-bis, che regolano già durata e garanzie | Verificare su Normattiva e scrivere la durata massima, invece della domanda.
- `chi_paga` (quarto punto) | EQUILIBRIO: "Tutte le persone che manifestano… possono scoraggiare l'espressione del dissenso". Il reato riguarda gruppi organizzati che usano oggetti atti a offendere, con pericolo concreto e danni. L'incitamento punito è a *quelle* condotte | "Chi incita in rete alla violenza di gruppo nei cortei: pena da 4 a 12 anni, da misurare sulla proporzionalità".
- `chi_guadagna` | EQUILIBRIO, categoria taciuta: le vittime, spesso ragazzi, dei reati commessi da gruppi di minori | Aggiungere: "Chi subisce aggressioni e rapine da gruppi di minori, se le misure riducono questi reati".
- `bilancio` e `chi_paga` (genitori) | FATTO: la sanzione non è "uguale per tutti", va da 500 a 1.000 euro. Non è però legata al reddito | "multe ai genitori non proporzionate al reddito".
- `in_breve` | FATTO, da verificare: le date "17 e 18 ottobre 2026" non compaiono nel decreto (art. 8 parla di "gravi incidenti occorsi nella città di Milano"). La relazione A.C. 3159 non è nel repository | Verificare sulla relazione o scrivere "Dopo i disordini di Milano di ottobre 2026". LINGUAGGIO: "rovescia la regola" → "cambia la regola".
- `rischi_giuridici` | FATTO, da verificare: sent. 168/1994, 263/2019 e 24/2019 non sono nel file verificato.

### dl-2026-193-autotrasporto.yaml
- `cosa_cambieremmo` (sesto punto) | EQUILIBRIO, pregiudizio verso le forze dell'ordine: "Togliere dal decreto gli artt. 8 e 10" ritarderebbe il pagamento di straordinari *già svolti* dalla polizia | "Per il futuro, mettere norme come gli artt. 8 e 10 in provvedimenti coerenti; non ritardare il pagamento degli straordinari già svolti".
- `valori` e `bilancio` | EQUILIBRIO, pregio taciuto: l'art. 10 riduce oneri amministrativi per le imprese medie, in linea con la semplificazione UE | In `bilancio` aggiungere: "Va bene anche alleggerire gli obblighi di rendicontazione per le imprese medie, anche se fuori tema".
- `cosa_fa` (art. 10) | FATTO, da verificare: "come consente la direttiva (UE) 2026/470" non è nel testo del decreto | Citare la relazione oppure togliere.
- `cosa_fa` (art. 1, c. 3) e `valori FID` | FATTO, da verificare: "Rinvia per la quarta volta" il contributo sui pacchi. Il testo mostra solo il rinvio del d.l. 38/2026 | Verificare la serie dei rinvii o scrivere "rinvia ancora".
- `cosa_fa` | FATTO, omissione: l'art. 1, c. 4 sopprime parti del d.l. 162/2026 (art. 1, cc. 4-5, e art. 4) e ne riduce gli oneri di 62 mln | Aggiungere una riga su che cosa viene soppresso.

### dl-2026-205-campi-flegrei.yaml
- `valori FID` | FATTO ed EQUILIBRIO: "Il denaro è tolto ad altre zone colpite… senza dirlo con chiarezza". L'art. 8, c. 2 indica in modo esplicito i due fondi ridotti | "Il denaro è tolto al fondo nazionale per la ricostruzione, che serve anche altre zone colpite…".
- `chi_paga` (ultimo punto) | LINGUAGGIO: "i vecchi condoni diventano una porta per ricevere contributi pubblici". Il contributo spetta solo con un titolo valido o una sanatoria conclusa; i condoni del 1985, 1994 e 2003 sono istituti di legge | "In zona di massimo rischio vulcanico, edifici condonati possono ricevere contributi; è un rischio se servono ad ampliarli e non a renderli sicuri".
- `rischi_giuridici` | FATTO, da verificare: la sent. 186/2013 non è nel file verificato.

### dl-2026-207-energia.yaml
- `rischi_giuridici` | FATTO, omissione: il dubbio di affidamento sui contratti a prezzo fisso è in gran parte risolto dal nuovo c. 3-bis, lett. b), che esclude dal corrispettivo l'energia comprata prima del decreto a prezzo fisso per servire clienti a prezzo fisso | "Il decreto esclude l'energia già coperta da contratti a prezzo fisso firmati prima; resta da verificare che l'esclusione copra tutti i casi".
- `numeri` (costo per il bilancio dello Stato) | FATTO, cornice: il secondo rimborso è pagato con corrispettivi a carico degli operatori (c. 3-bis), non dal bilancio dello Stato | "Costo per il sistema elettrico: non quantificato; il decreto lo pone a carico degli operatori e non del bilancio dello Stato".
- `valori EQU` / `BEN` | EQUILIBRIO, pregio taciuto: per l'industria manifatturiera ad alto consumo di energia il prezzo è una questione di sopravvivenza e di posti di lavoro | In BEN: "…soprattutto per le imprese energivore, con effetti sulla tenuta di produzione e lavoro".

### legge-2026-180-elettorale.yaml
- `valori FID` | FATTO, errore verificato: "a maggioranza semplice". 227 sì su 400 è oltre la maggioranza assoluta (201) ma sotto i tre quinti (240) | "Regole cambiate con la maggioranza assoluta ma senza i tre quinti, a circa un anno dal voto…".
- `valori FID` | LINGUAGGIO: "le regole del gioco non dovrebbero dipendere da chi gioca" (slogan) | Togliere.
- `chi_guadagna` e `chi_paga` | EQUILIBRIO, cose vecchie attribuite alla nuova legge: soglia del 3%, candidature in cinque collegi ed esenzione dalle firme per chi è già in Parlamento esistevano già. La legge ha alzato le firme per i nuovi partiti (da 1.500-2.000 a 6.000-7.000) e ha *allargato* l'esenzione ai partiti con un gruppo in una sola Camera | Distinguere: "Novità: firme quadruple per i partiti nuovi, esenzione estesa a chi ha un gruppo in una sola Camera. Già in vigore: soglia del 3%, candidature fino a cinque collegi".
- `rischi_giuridici` (6) | FATTO, troppo certo: "si applica a meno di dodici mesi dal voto". La data delle elezioni non è nota; il commento stesso lo chiede nelle domande aperte | "rischia di applicarsi a meno di dodici mesi dal voto".
- `valori` | EQUILIBRIO, pregio taciuto: soglia e premio servono alla stabilità dei governi, un valore che la Carta riconosce | Aggiungere in FID o CIT: "Premio con soglia e tetto favorisce governi stabili per l'intera legislatura".
- `rischi_giuridici` | FATTO, da verificare: le sent. 1/2014 e 35/2017 non sono nel file verificato.

---

*Riscontri a campione con esito positivo, quindi nessuna correzione: scadenze di conversione dei cinque decreti; numeri degli artt. 3, 9, 15, 18-21, 23, 35-40, 50-55, 57-59, 66, 69, 71-73, 92, 95, 116, 124 del DDL; Tabella I.6-1 e nota 20 del DPB; soglie e premi della L. 180/2026; importi del d.l. 185, 190, 193, 205 e 207. Le sentenze 140/2024, 19/2025, 52/2026, 234/2020, 80/2010, 223/2023, 192/2024, 220/2021, 182/2026, 10/2015, 111/2024, 22/2012, 32/2014 e 16/2017 sono nel file verificato.*
