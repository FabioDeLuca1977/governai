# -*- coding: utf-8 -*-
import csv, sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dati import R

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

GIUDIZI = ["efficace", "efficace in parte", "inefficace", "effetti negativi", "evidenza insufficiente"]
EXCL = {"ricon77","l142","tub93","risparmio05","popolari","moratti","autsc","ires","ecoreati","spazzac","dlgs29","fondaz98","l241","irpef26","cedolare"}
rows = sorted([t for t in enumerate(R) if t[1]["key"] not in EXCL], key=lambda t: (t[1]["anno"], t[0]))
rows = [r for _, r in rows]
keys = set()
for i, r in enumerate(rows, 1):
    assert r["giud"] in GIUDIZI, r["key"]
    assert r["sol"] in ("alta", "media", "bassa"), r["key"]
    assert r["key"] not in keys, r["key"]
    keys.add(r["key"])
    r["id"] = f"D{i:03d}"
ID = {r["key"]: r["id"] for r in rows}

cols = ["id", "anno", "atto", "governo_anno", "presidente_consiglio", "ambito", "decisione", "cosa_cambia",
        "effetto_conti", "effetti_misurati", "giudizio", "solidita_evidenza", "fonti"]
with open(os.path.join(OUT, "decisioni_1977_2026.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(cols)
    for r in rows:
        w.writerow([r["id"], r["anno"], r["atto"], f"governo in carica nel {r['anno']}", r["pres"], r["ambito"],
                    r["decisione"], r["cosa"], r["conti"], r["eff"], r["giud"], r["sol"], " | ".join(r["fonti"])])

def decade(a):
    if a < 1980: return "1977-1979"
    if a >= 2020: return "2020-2026"
    d = a // 10 * 10
    return f"{d}-{d+9}"
DEC = ["1977-1979", "1980-1989", "1990-1999", "2000-2009", "2010-2019", "2020-2026"]

by_dec = collections.OrderedDict((d, []) for d in DEC)
for r in rows: by_dec[decade(r["anno"])].append(r)
cnt_g = collections.Counter(r["giud"] for r in rows)
cnt_s = collections.Counter(r["sol"] for r in rows)
cnt_pm = collections.Counter(r["pres"] for r in rows)
cnt_amb = collections.Counter(r["ambito"] for r in rows)

def refs(*ks):
    for k in ks: assert k in ID, k
    return ", ".join(ID[k] for k in ks)

INTRO = {
"1977-1979": "Anni di inflazione a due cifre e di grandi leggi di sistema: nascono il Servizio sanitario nazionale, la legge finanziaria, l'equo canone, l'inclusione scolastica; l'Italia entra nello SME. Molte di queste scelte hanno cambiato il paese in modo duraturo, ma quasi nessuna è stata accompagnata da strumenti per misurarne gli effetti o da coperture stabili.",
"1980-1989": "Decennio con meno decisioni nel catalogo: le grandi riforme strutturali sono state poche e quasi nessuna è stata valutata. È il decennio della disinflazione e del debito. La banca centrale smette di finanziare il Tesoro, l'indicizzazione dei salari viene ridotta, ma i disavanzi primari restano alti e il debito cresce rapidamente. Compaiono i primi condoni edilizi e l'intervento straordinario nel Mezzogiorno arriva alla fase finale. Le valutazioni controfattuali sono rare.",
"1990-1999": "Il decennio del risanamento e delle grandi riforme sotto la spinta della crisi del 1992 e dell'obiettivo euro: manovre straordinarie, fine della scala mobile, riforme pensionistiche Amato e Dini, privatizzazioni, autorità indipendenti, elezione diretta dei sindaci, flessibilità in entrata nel lavoro. È anche il decennio in cui iniziano le prime valutazioni d'impatto serie (legge 488, patti territoriali, riforma 3+2).",
"2000-2009": "Riforma del Titolo V, euro in circolazione, nuove regole del lavoro, condoni fiscali ed edilizi, scudi fiscali, incentivi alle rinnovabili, piani di rientro in sanità, federalismo fiscale. Le regole cambiano spesso (pensioni 2004 e 2007, leggi elettorali); emergono le prime valutazioni controfattuali di alta qualità (click day, INVALSI, cassa integrazione).",
"2010-2019": "Crisi del debito sovrano e lunga stagnazione: riforma Fornero, pareggio in Costituzione, spending review, anticorruzione; poi bonus 80 euro, Jobs Act, Industria 4.0, salvataggi bancari, rottamazioni, decreto dignità, Reddito di cittadinanza e Quota 100. È il decennio con più valutazioni d'impatto pubblicate.",
"2020-2026": "Pandemia, grandi trasferimenti europei (PNRR), Superbonus e il suo stop, Assegno unico, riforme IRPEF a tappe, sostituzione del Reddito di cittadinanza, nuove regole fiscali europee. Per gran parte delle decisioni recenti l'evidenza ex post è ancora insufficiente.",
}

L = []
L.append("# Cinquant'anni di decisioni pubbliche in Italia (1977-2026): che cosa ha funzionato")
L.append("")
L.append("Catalogo ragionato di %d decisioni di politica pubblica, con gli effetti documentati e una lezione per GovernAI. Dati completi in `decisioni_1977_2026.csv` (una riga per decisione, con fonti)." % len(rows))
L.append("")
L.append("## Metodo")
L.append("")
L.append("- **Che cosa è una decisione.** Una legge, un decreto, un accordo o un atto di governo con effetti rilevanti e identificabili. Non sono incluse vicende giudiziarie o politiche in sé (per esempio Mani pulite), ma le norme che ne sono seguite.")
L.append("- **Chi l'ha presa.** Ogni riga indica il \"governo in carica nel <anno>\" e il nome della o del Presidente del Consiglio come dato storico. Per le leggi si considera il governo in carica alla data dell'atto (o dell'approvazione parlamentare, quando indicato). Si valuta la decisione, non chi l'ha presa; non si indicano partiti.")
L.append("- **Fatti, stime, opinioni.** Nella colonna `effetti_misurati` le frasi iniziano o sono marcate come *fatto* (dato osservato, senza nesso causale dimostrato), *stima* (risultato di un modello o di una valutazione) o *opinione* (giudizio di un'istituzione o della letteratura). Quando due fonti serie divergono sono riportate entrambe.")
L.append("- **Giudizio sull'evidenza** (sulla decisione rispetto al suo obiettivo dichiarato): *efficace*; *efficace in parte* (obiettivo raggiunto con costi o effetti collaterali rilevanti, o solo in parte); *inefficace*; *effetti negativi* (danni documentati superiori ai benefici o violazioni accertate); *evidenza insufficiente* (mancano valutazioni o i dati non permettono di separare l'effetto). ")
L.append("- **Solidità dell'evidenza.** *Alta*: almeno una valutazione controfattuale pubblicata (esperimento, discontinuità, differenze nelle differenze) o un accertamento giuridico definitivo. *Media*: dati ufficiali coerenti e analisi istituzionali (Banca d'Italia, UPB, Corte dei conti, RGS, ISTAT) senza un controfattuale pieno. *Bassa*: ricostruzioni descrittive, opinioni, dati parziali.")
L.append("- **Cifre.** Solo cifre presenti nelle fonti citate; dove la cifra non è verificata è scritto \"n.d.\" oppure \"da verificare\". Le serie lunghe (debito, crescita, occupazione) sono trattate in un lavoro parallelo e qui sono citate solo come contesto.")
L.append("- **Fonti.** Testo dell'atto su Normattiva (link URN), sentenze della Corte costituzionale e della Corte di giustizia UE, pubblicazioni di Banca d'Italia, UPB, Corte dei conti, RGS, ISTAT, INPS, OCSE, Commissione UE e articoli accademici. Per alcune fonti istituzionali il link porta alla pagina dell'archivio, non al singolo documento; per tre articoli accademici è data la citazione bibliografica completa.")
L.append("- **Equilibrio.** Il catalogo copre tutti i decenni e tutti i governi con decisioni di peso; il numero di righe per Presidente del Consiglio riflette la durata in carica e la densità legislativa, non un giudizio. La tabella di conteggio è in fondo.")
L.append("")
L.append("## Il quadro in numeri")
L.append("")
L.append("| Decennio | Decisioni | efficace | efficace in parte | inefficace | effetti negativi | evidenza insufficiente |")
L.append("|---|---|---|---|---|---|---|")
for d in DEC:
    c = collections.Counter(r["giud"] for r in by_dec[d])
    L.append(f"| {d} | {len(by_dec[d])} | " + " | ".join(str(c[g]) for g in GIUDIZI) + " |")
L.append(f"| **Totale** | **{len(rows)}** | " + " | ".join(f"**{cnt_g[g]}**" for g in GIUDIZI) + " |")
L.append("")
L.append("Solidità dell'evidenza: alta %d, media %d, bassa %d." % (cnt_s["alta"], cnt_s["media"], cnt_s["bassa"]))
L.append("")
L.append("Un dato salta subito all'occhio: per circa un terzo delle decisioni l'evidenza è insufficiente, e solo una minoranza ha una valutazione controfattuale. Per mezzo secolo lo Stato italiano ha deciso molto e misurato poco.")
L.append("")

for d in DEC:
    L.append(f"## {d}")
    L.append("")
    L.append(INTRO[d])
    L.append("")
    for r in by_dec[d]:
        L.append(f"**{r['id']} · {r['anno']} · {r['decisione']}**  ")
        L.append(f"*{r['atto']}* · governo in carica nel {r['anno']} (Presidente del Consiglio: {r['pres']}) · ambito: {r['ambito']}  ")
        L.append(f"Cosa cambia: {r['cosa']}  ")
        L.append(f"Conti: {r['conti']}  ")
        L.append(f"Effetti: {r['eff']}  ")
        L.append(f"Giudizio: **{r['giud']}** · evidenza {r['sol']}")
        L.append("")

LEZ = [
("Condoni e definizioni agevolate ripetute danno entrate una tantum ma peggiorano l'adempimento",
 "Ogni condono porta entrate una tantum, ma l'attesa del prossimo riduce l'adempimento spontaneo e alimenta nuovi abusi. La Corte di giustizia UE ha bocciato il condono IVA del 2002; UPB e IRPET documentano l'effetto aspettative delle rottamazioni. La collaborazione volontaria del 2014, con imposte pagate per intero e senza anonimato, è il modello meno dannoso.",
 refs("condono85", "condono94", "condono02", "condono03", "tremonti01", "scudo09", "rottam", "cpb", "vd14"),
 "Nessun condono, rottamazione o scudo anonimo nel programma; solo regolarizzazioni a imposta piena con scambio di informazioni."),
("Le riforme delle pensioni funzionano se sono graduali e stabili; le deroghe temporanee costano e non creano lavoro per i giovani",
 "Amato, Dini, adeguamento alla speranza di vita e Fornero hanno spostato la sostenibilità nelle proiezioni RGS. Lo scalone del 2004 cancellato nel 2007 e le quote 100, 102 e 103 mostrano il costo di cambiare spesso: Quota 100 non ha prodotto sostituzione con giovani. La Fornero, brusca, ha generato gli esodati e un effetto negativo misurato sulle assunzioni di giovani.",
 refs("pens92", "dini95", "speranza", "fornero11", "maroni", "l247", "quota100", "quota102"),
 "Ogni modifica pensionistica deve essere permanente, graduale e con clausole di salvaguardia scritte prima."),
("Un incentivo automatico senza tetto di spesa sfugge di mano",
 "Superbonus (costo quasi doppio del previsto), Conto energia (incentivi rimasti alti mentre i pannelli costavano meno) e crediti 4.0 (costi sopra le stime) hanno lo stesso difetto: spesa aperta, legata alla domanda. Lo stop alla cessione dei crediti ha fermato la crescita del costo.",
 refs("superbonus", "contoen", "ind40", "stopcess", "ecobonus"),
 "Ogni agevolazione nel programma ha un tetto annuo, un monitoraggio mensile e una revisione automatica se supera la stima."),
("Tagli mirati e monitorati battono i tagli lineari, ma vanno guardati anche gli esiti",
 "I tagli uguali per tutti (2008) contengono la spesa nel breve ma non distinguono tra spesa utile e inutile; la spending review del 2012 e la centralizzazione degli acquisti hanno dato risparmi documentati dove sono state attuate. I piani di rientro sanitari hanno risanato i conti, ma uno studio controfattuale trova più mortalità evitabile: tagliare senza misurare gli esiti è rischioso.",
 refs("dl112", "spending12", "pianirientro", "patto98", "delrio"),
 "Coperture da tagli solo con voce di spesa identificata e indicatore di esito associato (come già fanno le 93 coperture verificate)."),
("La stabilità delle regole è una politica in sé",
 "Quattro leggi elettorali in 24 anni (due dichiarate in parte incostituzionali), quattro codici degli appalti, quattro rottamazioni in sei anni, regole sul lavoro a termine cambiate nel 2001, 2012, 2014, 2018: ogni cambiamento riduce la credibilità del successivo e rende impossibile valutare.",
 refs("matt93", "porcellum", "rosatellum", "merloni", "appalti23", "dlgs368", "fornero12", "jobsact", "dignita"),
 "Clausola di stabilità: le misure del programma non si toccano per almeno un ciclo di valutazione salvo evidenza contraria."),
("L'attuazione conta più dell'annuncio",
 "Livelli essenziali sociali previsti nel 2000 e definiti vent'anni dopo; federalismo fiscale e Titolo V attuati a metà; fasce di merito nella PA mai applicate; spesa PNRR in ritardo pur con traguardi formali raggiunti. Le leggi quadro senza decreti, risorse e responsabili restano sulla carta.",
 refs("l328", "fedfisc", "titolov", "brunetta", "pnrr", "autdiff", "basaglia"),
 "Per ogni misura: decreto attuativo, responsabile, scadenza e indicatore di attuazione pubblicati insieme alla misura."),
("Gli aiuti alle imprese del Sud danno risultati misti: assegnarli con graduatorie e valutarli",
 "Patti territoriali senza effetti misurabili; legge 488 con due valutazioni divergenti (anticipo degli investimenti contro effetti positivi su occupazione); fondi UE con effetti positivi ma non duraturi dopo la crisi; sgravi generalizzati con forte rischio di peso morto. I meccanismi a graduatoria hanno almeno permesso valutazioni rigorose.",
 refs("sud86", "l488", "patti", "fondiue", "decsud", "ind40"),
 "Incentivi territoriali solo con bandi a punteggio, gruppo di confronto e valutazione indipendente prevista ex ante."),
("I vincoli esterni e le istituzioni indipendenti aiutano, ma non sostituiscono l'avanzo primario",
 "SME, divorzio, fine della scala mobile e accordi del 1993 hanno contribuito a battere l'inflazione; l'euro ha abbattuto la spesa per interessi. Ma il debito è cresciuto negli anni '80 per i disavanzi primari, e il pareggio in Costituzione è stato derogato quasi ogni anno. L'UPB è l'eredità più utile del 2012.",
 refs("sme79", "divorzio", "acc92", "prot93", "eurotassa", "euro98", "pareggio", "psb", "amato92"),
 "Il programma rispetta un percorso di spesa netta e fa validare le stime da un soggetto terzo (UPB o equivalente)."),
("Contro la povertà servono strumenti universali e selettivi, con un'attivazione che funzioni davvero",
 "Il Reddito di cittadinanza ha ridotto la povertà ma con risultati deboli sul lavoro; l'Assegno di inclusione la riduce meno (Banca d'Italia). L'Assegno unico ha razionalizzato misure frammentate. Il bonus 80 euro ha sostenuto i consumi ma non raggiungeva gli incapienti. L'ISEE è stato decisivo solo dopo la revisione con dati precompilati.",
 refs("rei", "rdc", "adi", "auu", "bonus80", "isee"),
 "Sostegno contro la povertà su base ISEE precompilato, con politiche attive valutate e non solo condizionalità formali."),
("Nel lavoro, riformare solo i nuovi contratti crea un mercato duale; gli incentivi temporanei creano picchi",
 "Treu, Biagi e decreto 368 hanno aumentato l'occupazione soprattutto temporanea; il Jobs Act ha spinto le assunzioni stabili soprattutto grazie alla decontribuzione, con calo alla sua fine. La cassa integrazione protegge i posti nel breve ma può rallentare la riallocazione.",
 refs("treu", "biagi", "dlgs368", "jobsact", "dignita", "garanzia", "cigd", "covidlav", "cfl84"),
 "Preferire sgravi permanenti e mirati a incentivi a scadenza; ammortizzatori con durata limitata e formazione collegata."),
("Lo status legale riduce i reati; canali di ingresso realistici evitano sanatorie a ripetizione",
 "La prova più solida dell'intero catalogo in materia: con il click day 2007 lo status legale ha ridotto i reati degli immigrati regolarizzati. Ripetute sanatorie (1998-2020) mostrano che le quote ordinarie non bastavano. Le strette sui permessi e gli accordi con paesi di transito hanno effetti misurati sugli sbarchi, ma costi umani documentati e nessuna valutazione controfattuale.",
 refs("clickday", "bossi02", "tuimm", "cutro", "dlsic18", "libia"),
 "Canali di ingresso per lavoro realistici e regolarizzazione legata al lavoro, valutati con dati amministrativi."),
("Misurare bene è già una politica: dati, controlli credibili, valutatori indipendenti",
 "Le prove INVALSI funzionano solo con osservatori esterni (esperimento casuale); l'ISEE è migliorato con i dati precompilati; l'UPB ha reso più credibili le previsioni; trasparenza e anticorruzione senza misura degli esiti producono soprattutto adempimenti formali.",
 refs("invalsi", "isee", "pareggio", "trasp13", "anticorr", "abusouff"),
 "Ogni misura del programma nasce con dati, indicatore e piano di valutazione; i risultati si pubblicano anche se negativi."),
("Tassare meno il lavoro e più gli immobili è la raccomandazione costante, ma la politica ha fatto spesso il contrario",
 "ICI 1992 e IMU 2011 hanno dato ai Comuni un'entrata stabile; l'abolizione sulla prima casa (2008 e 2015) l'ha ridotta, contro il parere di OCSE e Commissione UE. Le riforme IRPEF recenti agiscono sul lavoro, ma il drenaggio fiscale ne assorbe parte. Imposte sostitutive come il forfettario (e la cedolare secca sugli affitti) creano disparità tra redditi uguali.",
 refs("ici92", "ici08", "imu11", "tasi15", "forfett", "irpef22", "irpef24"),
 "Spostare il prelievo verso immobili (con catasto aggiornato) e consumi dannosi, riducendo quello sul lavoro; ridurre i regimi sostitutivi."),
("Le grandi scelte di sistema reggono quando hanno un finanziamento credibile",
 "Il Servizio sanitario universale del 1978 è tra le scelte più durature, ma ha generato disavanzi ripianati a posteriori per quasi trent'anni; le privatizzazioni hanno portato incassi rilevanti ma con criticità di regolazione. Le leggi di sistema durano se nascono con risorse e governance chiare.",
 refs("ssn78", "ssn92", "pianirientro", "priv92", "auth95", "amato90"),
 "Le riforme di sistema del programma indicano fonte di finanziamento strutturale e regolatore responsabile."),
]

L.append("## Lezioni trasversali per GovernAI")
L.append("")
for i, (tit, testo, rif, uso) in enumerate(LEZ, 1):
    L.append(f"### {i}. {tit}")
    L.append("")
    L.append(testo)
    L.append("")
    L.append(f"- Decisioni a sostegno: {rif}")
    L.append(f"- Che cosa ne ricava il programma: {uso}")
    L.append("")

L.append("## Cosa non sappiamo")
L.append("")
for t in [
    "**Gli effetti di lungo periodo di molte leggi di sistema** (SSN, Titolo V, autonomie locali, codice di procedura penale): non esistono controfattuali credibili; i giudizi sono ricostruzioni.",
    "**Le decisioni più recenti** (2023-2026: AdI, concordato preventivo, IRPEF a tre aliquote e al 33%, autonomia differenziata, abolizione dell'abuso d'ufficio, nuove regole UE, PNRR): l'evidenza è ex ante o assente.",
    "**L'effetto netto di Superbonus e PNRR sul PIL potenziale**: le stime divergono e dipendono dal modello; servono dati microeconomici che non sono ancora pubblici.",
    "**Corruzione ed evasione**: mancano misure dirette affidabili, quindi l'efficacia di L. 190/2012, ANAC, condoni e concordato si può giudicare solo indirettamente.",
    "**Natalità**: nessuna misura del catalogo (Assegno unico incluso) ha ancora un effetto misurato sulla fecondità.",
    "**Costi consolidati**: per molte decisioni (Jobs Act, decontribuzione Sud, salvataggi bancari, privatizzazioni nette) manca un consuntivo pubblico unico; le cifre indicate come \"da verificare\" vanno controllate su relazioni tecniche e rendiconti.",
    "**Limiti di questo lavoro**: selezione delle decisioni inevitabilmente soggettiva; alcune fonti sono sintesi secondarie di studi originali (indicate come tali); i link istituzionali generici vanno sostituiti col documento puntuale in una revisione successiva.",
]:
    L.append(f"- {t}")
L.append("")
L.append("## Appendice: decisioni per Presidente del Consiglio (dato descrittivo)")
L.append("")
L.append("| Presidente del Consiglio | Decisioni nel catalogo |")
L.append("|---|---|")
for p, n in sorted(cnt_pm.items(), key=lambda t: -t[1]):
    L.append(f"| {p} | {n} |")
L.append("")
L.append("Il numero dipende soprattutto dalla durata in carica e dal periodo; non è un indicatore di qualità.")
L.append("")

with open(os.path.join(OUT, "decisioni_1977_2026.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(L))

print("TOT", len(rows))
for d in DEC: print(d, len(by_dec[d]), dict(collections.Counter(r["giud"] for r in by_dec[d])))
print(dict(cnt_g)); print(dict(cnt_s)); print(dict(cnt_pm)); print(dict(cnt_amb))
