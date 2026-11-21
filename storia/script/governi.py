"""Confronto tra governi della Repubblica (1979-2025) con le serie di storia/serie/.

Uso:  python storia/script/governi.py

Legge:   storia/governi.csv, storia/serie/*.csv, storia/decisioni_1977_2026.csv
Scrive:  storia/governi_confronto.csv, storia/governi_confronto.md

Metodo: storia/governi_metodo.md. Lo script e' deterministico: non scarica nulla,
non usa numeri casuali e non dipende dalla data del computer (la data di riferimento
per il governo in carica e' fissata in DATA_RIFERIMENTO).
"""
from __future__ import annotations

import csv
import statistics
from collections import defaultdict
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent          # storia/
SERIE = BASE / "serie"

PRIMO_ANNO = 1979           # primo anno del confronto
ULTIMO_ANNO = 2025          # ultimo anno con dati osservati (2026 = previsione, escluso)
DATA_RIFERIMENTO = date(2026, 11, 19)   # "oggi" per la durata del governo in carica
VICINI = ["FR", "DE", "ES"]
MIN_VICINI = 2              # media dei vicini calcolata solo se ci sono almeno 2 paesi

# ---------------------------------------------------------------------------
# Indicatori
#   tipo: "media" (media degli anni del mandato) o "variazione" (fine - anno prima)
#   verso: +1 = piu' alto e' meglio, -1 = piu' basso e' meglio, 0 = solo descrittivo
#   vicini: True se esiste un confronto omogeneo con Francia, Germania, Spagna
# ---------------------------------------------------------------------------
INDICATORI = [
    dict(id="pil_pc", nome="Crescita media annua del PIL pro capite reale", file="pil_pro_capite_crescita",
         tipo="media", verso=+1, ambito="crescita", unita="% annua", vicini=True),
    dict(id="produttivita", nome="Crescita media annua della produttività oraria", file="produttivita_oraria_crescita",
         tipo="media", verso=+1, ambito="crescita", unita="% annua", vicini=True),
    dict(id="invest_pubblici", nome="Investimenti pubblici medi", file="investimenti_pubblici_pil",
         tipo="media", verso=+1, ambito="crescita", unita="% PIL", vicini=True),
    dict(id="occupazione", nome="Variazione del tasso di occupazione 15-64", file="occupazione_15_64",
         tipo="variazione", verso=+1, ambito="lavoro", unita="punti", vicini=True),
    dict(id="occ_femminile", nome="Variazione del tasso di occupazione femminile 15-64", file="occupazione_femminile_15_64",
         tipo="variazione", verso=+1, ambito="lavoro", unita="punti", vicini=True),
    dict(id="disocc_giovanile", nome="Variazione della disoccupazione giovanile 15-24", file="disoccupazione_giovanile",
         tipo="variazione", verso=-1, ambito="lavoro", unita="punti", vicini=True),
    dict(id="tempo_determinato", nome="Variazione della quota di dipendenti a tempo determinato", file="dipendenti_tempo_determinato",
         tipo="variazione", verso=-1, ambito="qualità del lavoro", unita="punti", vicini=True),
    dict(id="part_time_involontario", nome="Variazione del part-time involontario", file="part_time_involontario",
         tipo="variazione", verso=-1, ambito="qualità del lavoro", unita="punti", vicini=True),
    dict(id="salario_reale", nome="Crescita media annua del salario reale per dipendente", file="salario_reale_crescita",
         tipo="media", verso=+1, ambito="qualità del lavoro", unita="% annua", vicini=True),
    dict(id="ore_occupato", nome="Variazione delle ore lavorate per occupato", file="ore_per_occupato",
         tipo="variazione", verso=0, ambito="qualità del lavoro", unita="ore annue", vicini=True),
    dict(id="debito", nome="Variazione del debito pubblico", file="debito_pil",
         tipo="variazione", verso=-1, ambito="conti", unita="punti di PIL", vicini=True),
    dict(id="saldo_primario", nome="Saldo primario medio", file="saldo_primario_pil",
         tipo="media", verso=+1, ambito="conti", unita="% PIL", vicini=True),
    dict(id="deficit", nome="Deficit medio", file="deficit_pil", segno=-1,
         tipo="media", verso=-1, ambito="conti", unita="% PIL", vicini=True),
    dict(id="pressione_fiscale", nome="Variazione della pressione fiscale", file="pressione_fiscale_ocse",
         tipo="variazione", verso=0, ambito="conti", unita="punti di PIL", vicini=True),
    dict(id="spread", nome="Spread medio con la Germania", file="spread_bund", germania_zero=True,
         tipo="media", verso=-1, ambito="prezzi e mercati", unita="punti base", vicini=True),
    dict(id="inflazione", nome="Inflazione media", file="inflazione",
         tipo="media", verso=-1, ambito="prezzi e mercati", unita="% annua", vicini=True),
    dict(id="poverta_assoluta", nome="Variazione della povertà assoluta (persone)", file="poverta_assoluta",
         tipo="variazione", verso=-1, ambito="società", unita="punti", vicini=False, rottura=(2013, 2014)),
    dict(id="emigrazione", nome="Emigrazione media annua di cittadini italiani", file="emigrazione_cittadini",
         tipo="media", verso=-1, ambito="società", unita="migliaia", vicini=False),
]
AMBITI = ["conti", "crescita", "lavoro", "qualità del lavoro", "prezzi e mercati", "società"]

# Shock esterni (anni) usati come contesto, non come correzione dei numeri.
SHOCK = [
    ((1979, 1980), "secondo shock petrolifero"),
    ((1992, 1993), "crisi valutaria del 1992 e uscita della lira dallo SME"),
    ((2008, 2009), "crisi finanziaria mondiale"),
    ((2011, 2012), "crisi dei debiti sovrani nell'area euro"),
    ((2020, 2020), "pandemia"),
    ((2022, 2023), "shock dei prezzi dell'energia e rialzo dei tassi BCE"),
]
MESI = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]


# ---------------------------------------------------------------------------
# Lettura dati
# ---------------------------------------------------------------------------
def leggi_serie(nome: str) -> dict:
    """{paese: {anno: valore}}; esclude previsioni e anni oltre ULTIMO_ANNO."""
    out: dict = defaultdict(dict)
    with open(SERIE / f"{nome}.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            a = int(r["anno"])
            if a > ULTIMO_ANNO or "previsione" in r.get("fonte", "").lower():
                continue
            if r["valore"] in ("", "nan"):
                continue
            out[r["paese"]][a] = float(r["valore"])
    return out


def leggi_governi() -> list[dict]:
    with open(BASE / "governi.csv", encoding="utf-8") as f:
        g = list(csv.DictReader(f))
    for x in g:
        x["inizio"] = date.fromisoformat(x["giuramento"])
        x["termine"] = date.fromisoformat(x["fine"]) if x["fine"] else DATA_RIFERIMENTO
        x["in_carica"] = not x["fine"]
        x["lungo"] = x["termine"] >= aggiungi_mesi(x["inizio"], 12)
    return g


def aggiungi_mesi(d: date, m: int) -> date:
    y, mo = divmod(d.month - 1 + m, 12)
    return date(d.year + y, mo + 1, min(d.day, 28))


def etichetta_governo(x: dict) -> str:
    a, b = x["inizio"], x["termine"]
    if x["in_carica"]:
        return f"governo {a.year}-oggi"
    if a.year == b.year:
        return f"governo {a.year} ({MESI[a.month - 1]}-{MESI[b.month - 1]})"
    return f"governo {a.year}-{b.year}"


# ---------------------------------------------------------------------------
# Unita' di confronto
# ---------------------------------------------------------------------------
def costruisci_unita(gov: list[dict]) -> list[dict]:
    """Governi con >= 12 mesi = unita' proprie. Governi brevi consecutivi della stessa
    legislatura, nessuno dei quali arriva a 12 mesi, uniti in un 'periodo di governo'.
    Un governo breve isolato resta unita' propria ma 'non confrontabile'."""
    unita, i = [], 0
    while i < len(gov):
        g = gov[i]
        if g["lungo"]:
            unita.append(dict(governi=[g])); i += 1; continue
        j = i
        while j + 1 < len(gov) and not gov[j + 1]["lungo"] and gov[j + 1]["legislatura"] == g["legislatura"]:
            j += 1
        unita.append(dict(governi=gov[i:j + 1])); i = j + 1
    for u in unita:
        gs = u["governi"]
        u["inizio"], u["termine"] = gs[0]["inizio"], gs[-1]["termine"]
        u["in_carica"] = gs[-1]["in_carica"]
        if len(gs) > 1:
            u["tipo"] = "periodo"
            u["etichetta"] = f"periodo di governo {u['inizio'].year}-{u['termine'].year}"
        else:
            u["tipo"] = "governo" if gs[0]["lungo"] else "breve"
            u["etichetta"] = etichetta_governo(gs[0])
        u["id"] = "+".join(x["id"] for x in gs)
        u["numeri"] = ", ".join(x["numero"].replace("governo ", "") for x in gs)
        u["mesi"] = round((u["termine"] - u["inizio"]).days / 30.44, 1)
    return unita


def giorni_nell_anno(ini: date, fin: date, anno: int) -> int:
    a, b = max(ini, date(anno, 1, 1)), min(fin, date(anno + 1, 1, 1))
    return max(0, (b - a).days)


def assegna_anni(unita: list[dict]) -> dict:
    """Ogni anno va all'unita' con piu' giorni in carica in quell'anno."""
    per_anno = {}
    for anno in range(PRIMO_ANNO, ULTIMO_ANNO + 1):
        giorni = [(sum(giorni_nell_anno(g["inizio"], g["termine"], anno) for g in u["governi"]), k)
                  for k, u in enumerate(unita)]
        gmax, k = max(giorni)
        per_anno[anno] = k
    for k, u in enumerate(unita):
        u["anni"] = [a for a, kk in per_anno.items() if kk == k]
        u["confrontabile"] = u["tipo"] in ("governo", "periodo") and bool(u["anni"])
    return per_anno


# ---------------------------------------------------------------------------
# Calcolo indicatori
# ---------------------------------------------------------------------------
def fmt_anni(anni: list[int]) -> str:
    if not anni:
        return ""
    return str(anni[0]) if len(anni) == 1 else f"{anni[0]}-{anni[-1]}"


def calcola(ind: dict, s: dict, anni: list[int]) -> dict:
    segno = ind.get("segno", 1)
    paesi = ["IT"] + (VICINI if ind["vicini"] else [])
    dati = {p: {a: segno * v for a, v in s.get(p, {}).items()} for p in paesi}
    if ind.get("germania_zero"):
        dati["DE"] = {a: 0.0 for a in dati["IT"]}
    res = dict(it=None, vic=None, diff=None, anni_eff="", nota="")
    if not anni:
        return res
    note = []
    if ind["tipo"] == "media":
        aa = [a for a in anni if a in dati["IT"]]
        if not aa:
            return res
        res["it"] = statistics.mean(dati["IT"][a] for a in aa)
        if ind["vicini"]:
            medie = []
            for a in aa:
                v = [dati[p][a] for p in VICINI if a in dati[p]]
                if len(v) >= MIN_VICINI:
                    medie.append(statistics.mean(v))
                    if len(v) < 3:
                        note.append(f"{a}: vicini {len(v)} su 3")
            if len(medie) == len(aa):
                res["vic"] = statistics.mean(medie)
        res["anni_eff"] = fmt_anni(aa)
        if len(aa) < len(anni):
            note.append(f"dato italiano solo per {fmt_anni(aa)}")
    else:
        inizio = anni[0] - 1
        fine_cand = [a for a in anni if a in dati["IT"]]
        if inizio not in dati["IT"] or not fine_cand:
            return dict(res, nota="serie non disponibile per l'anno di partenza o di arrivo")
        fine = max(fine_cand)
        rott = ind.get("rottura")
        if rott and inizio <= rott[0] and fine >= rott[1]:
            return dict(res, nota="il periodo attraversa il cambio di metodo ISTAT 2013/2014: non calcolato")
        res["it"] = dati["IT"][fine] - dati["IT"][inizio]
        if ind["vicini"]:
            v = [dati[p][fine] - dati[p][inizio] for p in VICINI if fine in dati[p] and inizio in dati[p]]
            if len(v) >= MIN_VICINI:
                res["vic"] = statistics.mean(v)
                if len(v) < 3:
                    note.append(f"vicini {len(v)} su 3")
        res["anni_eff"] = f"{inizio}->{fine}"
        if fine < anni[-1]:
            note.append(f"serie ferma al {fine}")
    if res["it"] is not None and res["vic"] is not None:
        res["diff"] = res["it"] - res["vic"]
    res["nota"] = "; ".join(note)
    return res


def ranghi(valori: dict, verso: int) -> dict:
    """valori: {chiave: numero}. Rango 1 = migliore (verso +1: piu' alto; -1: piu' basso;
    0: ordinamento descrittivo dal valore piu' basso)."""
    v = {k: x for k, x in valori.items() if x is not None}
    if not v:
        return {}
    chiave = (lambda k: -v[k]) if verso == +1 else (lambda k: v[k])
    ordinati = sorted(v, key=chiave)
    out = {}
    for k in ordinati:
        out[k] = 1 + sum(1 for j in v if chiave(j) < chiave(k) - 1e-12)
    return out


def contesto(u: dict, serie: dict) -> dict:
    a0 = u["anni"][0] - 1 if u["anni"] else None
    def val(nome, paese="IT"):
        return serie[nome].get(paese, {}).get(a0) if a0 else None
    shock = [t for (da, a), t in SHOCK if u["anni"] and not (a < u["anni"][0] or da > u["anni"][-1])]
    return dict(anno_partenza=a0, debito0=val("debito_pil"), deficit0=(-val("deficit_pil") if val("deficit_pil") is not None else None),
                spread0=val("spread_bund"), shock=shock)


# ---------------------------------------------------------------------------
# Decisioni del catalogo
# ---------------------------------------------------------------------------
def decisioni_per_unita(gov: list[dict], unita: list[dict]) -> dict:
    with open(BASE / "decisioni_1977_2026.csv", encoding="utf-8") as f:
        dec = list(csv.DictReader(f))
    gov_to_u = {g["id"]: k for k, u in enumerate(unita) for g in u["governi"]}
    out = defaultdict(list)
    for d in dec:
        anno, pc = int(d["anno"]), d["presidente_consiglio"].strip()
        cand = [(giorni_nell_anno(g["inizio"], g["termine"], anno), g) for g in gov
                if g["presidente_consiglio"] == pc and giorni_nell_anno(g["inizio"], g["termine"], anno) > 0]
        if not cand:
            continue                      # governi precedenti al 1978
        cand.sort(key=lambda t: (-t[0], t[1]["id"]))
        d["_ambiguo"] = len(cand) > 1
        out[gov_to_u[cand[0][1]["id"]]].append(d)
    return out


# ---------------------------------------------------------------------------
# Principale
# ---------------------------------------------------------------------------
def esegui() -> dict:
    gov = leggi_governi()
    unita = costruisci_unita(gov)
    assegna_anni(unita)
    serie = {ind["file"]: leggi_serie(ind["file"]) for ind in INDICATORI}
    for extra in ("debito_pil", "deficit_pil", "spread_bund"):
        serie.setdefault(extra, leggi_serie(extra))

    righe = []
    risultati = defaultdict(dict)       # (versione, ind_id) -> {k: res}
    for versione, sposta in (("base", 0), ("ritardo_1_anno", 1)):
        for ind in INDICATORI:
            for k, u in enumerate(unita):
                anni = [a + sposta for a in u["anni"] if a + sposta <= ULTIMO_ANNO]
                risultati[(versione, ind["id"])][k] = calcola(ind, serie[ind["file"]], anni) | {"anni": anni}
            conf = {k: r for k, r in risultati[(versione, ind["id"])].items() if unita[k]["confrontabile"]}
            base_rango = "diff" if ind["vicini"] else "it"
            rk = ranghi({k: r[base_rango] for k, r in conf.items()}, ind["verso"])
            rk_it = ranghi({k: r["it"] for k, r in conf.items()}, ind["verso"])
            n, n_it = len(rk), len(rk_it)
            for k, r in risultati[(versione, ind["id"])].items():
                r["rango"], r["n"] = rk.get(k), n
                r["rango_it"], r["n_it"] = rk_it.get(k), n_it
    return dict(gov=gov, unita=unita, serie=serie, risultati=risultati,
                decisioni=decisioni_per_unita(gov, unita))


def num(x, d=2):
    return "" if x is None else f"{x:.{d}f}"


def scrivi_csv(R: dict) -> None:
    campi = ["unita_id", "governo_periodo", "governi_inclusi", "tipo_unita", "confrontabile", "versione",
             "anni", "ambito", "indicatore", "unita_misura", "verso", "anni_effettivi",
             "valore_italia", "valore_vicini", "differenza", "rango", "n_confrontati",
             "base_del_rango", "rango_solo_italia", "n_confrontati_italia", "nota"]
    verso_txt = {1: "più alto è meglio", -1: "più basso è meglio", 0: "descrittivo (rango 1 = calo maggiore)"}
    with open(BASE / "governi_confronto.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(campi)
        for versione in ("base", "ritardo_1_anno"):
            for k, u in enumerate(R["unita"]):
                for ind in INDICATORI:
                    r = R["risultati"][(versione, ind["id"])][k]
                    nota = r["nota"]
                    if not u["confrontabile"]:
                        nota = "; ".join(x for x in ["non confrontabile: governo sotto i 12 mesi o senza anni assegnati", nota] if x)
                    w.writerow([u["id"], u["etichetta"], u["numeri"], u["tipo"], "sì" if u["confrontabile"] else "no",
                                versione, fmt_anni(r["anni"]), ind["ambito"], ind["nome"], ind["unita"],
                                verso_txt[ind["verso"]], r["anni_eff"],
                                num(r["it"], 3), num(r["vic"], 3), num(r["diff"], 3),
                                r["rango"] or "", r["n"] if r["rango"] else "",
                                ("Italia meno vicini" if ind["vicini"] else "solo Italia (nessun confronto omogeneo)") if r["rango"] else "",
                                r["rango_it"] or "", r["n_it"] if r["rango_it"] else "", nota])


# ---------------------------------------------------------------------------
# Rapporto in Markdown
# ---------------------------------------------------------------------------
def it(x, d=1, segno=False):
    """Numero in formato italiano."""
    if x is None:
        return "n.d."
    s = f"{x:+.{d}f}" if segno else f"{x:.{d}f}"
    return s.replace(".", ",")


def punteggio(r: dict) -> float | None:
    """Posizione 0-100 (100 = primo) a partire dal rango."""
    if not r.get("rango") or r["n"] < 2:
        return None
    return 100 * (r["n"] - r["rango"]) / (r["n"] - 1)


def sintesi_ambiti(R: dict, versione: str = "base") -> dict:
    """{k: {ambito: mediana dei punteggi}}, solo indicatori con un verso normativo."""
    out = {}
    for k, u in enumerate(R["unita"]):
        if not u["confrontabile"]:
            continue
        out[k] = {}
        for amb in AMBITI:
            p = [punteggio(R["risultati"][(versione, i["id"])][k]) for i in INDICATORI
                 if i["ambito"] == amb and i["verso"] != 0]
            p = [x for x in p if x is not None]
            out[k][amb] = statistics.median(p) if p else None
    return out


def fascia(p):
    if p is None:
        return "n.d."
    return "primo terzo" if p >= 200 / 3 else ("terzo centrale" if p >= 100 / 3 else "ultimo terzo")


def rango_multi_anno(R, ind, k_corr, versione="base"):
    """Rango del governo in carica tra le sole unita' con almeno 2 anni assegnati."""
    ris = R["risultati"][(versione, ind["id"])]
    chiave = "diff" if ind["vicini"] else "it"
    v = {k: r[chiave] for k, r in ris.items()
         if R["unita"][k]["confrontabile"] and len(R["unita"][k]["anni"]) >= 2}
    rk = ranghi(v, ind["verso"])
    return rk.get(k_corr), len(rk)


def rk_txt(r, chiave="rango", n="n"):
    return f"{r[chiave]}° su {r[n]}" if r.get(chiave) else "n.d."


def scrivi_rapporto(R: dict) -> None:
    U, RIS, serie = R["unita"], R["risultati"], R["serie"]
    kc = max(k for k, u in enumerate(U) if u["in_carica"])
    corr = U[kc]
    kp = max(k for k, u in enumerate(U) if u["confrontabile"] and k != kc)
    conf = [k for k, u in enumerate(U) if u["confrontabile"]]
    S = sintesi_ambiti(R)
    S_rit = sintesi_ambiti(R, "ritardo_1_anno")

    def r_(ind_id, k=kc, v="base"):
        return RIS[(v, ind_id)][k]

    def sv(nome, anno, paese="IT"):
        if nome not in serie:
            serie[nome] = leggi_serie(nome)
        return serie[nome].get(paese, {}).get(anno)

    def dec(i):
        return 0 if i["id"] in ("spread", "emigrazione") else 2

    a0, a1 = corr["anni"][0] - 1, corr["anni"][-1]
    L = []
    w = L.append

    w("# Il governo 2022-oggi a confronto con i governi dal 1979")
    w("")
    w("*Rapporto generato da `storia/script/governi.py` con le serie di `storia/serie/`. Metodo: "
      "`storia/governi_metodo.md`. Dati osservati fino al 2025; il 2026 è una previsione ed è escluso. "
      "I governi sono indicati con le date; numeri d'ordine e altre informazioni sono in `storia/governi.csv`.*")
    w("")
    w("**Come leggere.** La misura principale è la **differenza rispetto ai vicini**: il risultato dell'Italia "
      "meno la media di Francia, Germania e Spagna negli stessi anni. Così si toglie una parte degli shock "
      "comuni (crisi dell'euro, pandemia, energia, politica della BCE). Il **rango** dice in che posizione è "
      "un governo tra quelli confrontabili (1° = risultato migliore rispetto ai vicini). Non c'è un voto con pesi "
      "scelti da noi: la sintesi è per ambito e il punteggio complessivo da più punti di vista è in storia/punti_di_vista.md. Nessun numero di questo rapporto prova che un risultato sia stato causato da un governo.")
    w("")

    # ---------------- In breve
    w("## In breve")
    w("")
    w(f"Il {corr['etichetta']} ha dati osservati per **{fmt_anni(corr['anni'])}** ({len(corr['anni'])} anni solari: "
      f"il {a0} va al governo in carica per la maggior parte di quell'anno). È confrontato con "
      f"{len(conf) - 1} governi o periodi di governo dal 1979 al {a0}.")
    w("")
    w("| Ambito | Posizione mediana (0-100, 100 = primo) | Fascia | Indicatori (rango rispetto ai vicini) |")
    w("|---|---|---|---|")
    for amb in AMBITI:
        det = []
        for i in INDICATORI:
            if i["ambito"] != amb:
                continue
            r = r_(i["id"])
            extra = ("" if i["vicini"] else ", solo dato italiano") + (", solo ordinamento" if i["verso"] == 0 else "")
            det.append(f"{i['nome']}: {rk_txt(r)}{extra}")
        ordine = [S[k][amb] for k in conf if S[k][amb] is not None]
        pos = S[kc][amb]
        pos_txt = (f"{it(pos, 0)} ({1 + sum(1 for x in ordine if x > pos + 1e-9)}° su {len(ordine)})"
                   if pos is not None else "n.d.")
        w(f"| {amb} | {pos_txt} | {fascia(pos)} | {'; '.join(det)} |")
    w("")
    w("La posizione mediana è la mediana delle posizioni (0 = ultimo, 100 = primo) degli indicatori "
      "dell'ambito con un verso chiaro; la pressione fiscale è esclusa perché salire o scendere non è in sé "
      "un risultato migliore o peggiore. Tra parentesi, il posto del governo in carica se si ordinano tutti i governi "
      "per questa mediana. Per l'ambito società i ranghi usano il solo dato italiano.")
    w("")
    senza = [punteggio(r_(i["id"])) for i in INDICATORI
             if i["ambito"] == "crescita" and i["verso"] != 0 and i["id"] != "invest_pubblici"]
    senza = [x for x in senza if x is not None]
    if senza:
        w(f"**Sensibilità.** Nell'ambito crescita il primo posto per investimenti pubblici dipende in larga parte dal PNRR, "
          f"deciso e finanziato prima del mandato; senza questo indicatore la posizione mediana in crescita scende a "
          f"{it(statistics.median(senza), 0)} ({fascia(statistics.median(senza))}). Con gli anni spostati di uno "
          f"(sezione 5) le posizioni mediane diventano: " +
          "; ".join(f"{a} {it(S_rit[kc][a], 0)}" for a in AMBITI) +
          ". I ranghi tra i soli governi con almeno due anni sono nella sezione 3.")
        w("")

    # ---------------- Governi confrontati
    w("## 1. Governi confrontati")
    w("")
    w("Regole: un governo entra nel confronto se resta in carica almeno 12 mesi; ogni anno solare va al governo "
      "(o periodo) in carica per più giorni in quell'anno; i governi brevi consecutivi della stessa legislatura, "
      "nessuno dei quali arriva a 12 mesi, sono uniti in un *periodo di governo*. Un governo breve che non si può "
      "unire resta fuori dalla classifica, ma i suoi numeri sono nel file CSV.")
    w("")
    w("| Governo o periodo | Governi inclusi (n.) | Dal | Al | Mesi | Anni assegnati | Nel confronto |")
    w("|---|---|---|---|---|---|---|")
    for u in U:
        stato = "sì" if u["confrontabile"] else ("no: meno di 12 mesi" if u["tipo"] == "breve" else "no: nessun anno dal 1979")
        al = "in carica" if u["in_carica"] else u["termine"].isoformat()
        w(f"| {u['etichetta']} | {u['numeri']} | {u['inizio'].isoformat()} | {al} | {it(u['mesi'], 0)} | "
          f"{fmt_anni(u['anni']) or '-'} | {stato} |")
    w("")
    w("**Unioni dichiarate.** " + " ".join(
        f"Il {u['etichetta']} unisce i governi {u['numeri']} (stessa legislatura, nessuno arriva a 12 mesi; "
        f"in tutto {it(u['mesi'], 0)} mesi)." for u in U if u["tipo"] == "periodo"))
    w("")
    persi = [str(a) for u in U if not u["confrontabile"] for a in u["anni"]]
    uno = [u["etichetta"] for u in U if u["confrontabile"] and u["tipo"] == "governo" and len(u["anni"]) == 1 and u["mesi"] >= 18]
    w("**Effetti della regola sugli anni.** " +
      (f"Gli anni {', '.join(persi)} vanno a governi sotto i 12 mesi e restano fuori dalla classifica. " if persi else "") +
      (f"Alcuni governi lunghi ricevono un solo anno perché negli anni di confine erano in carica per meno giorni "
       f"del governo vicino ({', '.join(uno)})." if uno else ""))
    w("")

    # ---------------- Tabelle per ambito
    w("## 2. Tabella principale per ambito")
    w("")
    w("In ogni cella: **differenza Italia meno vicini** (rango). Per povertà assoluta ed emigrazione non esiste un "
      "confronto omogeneo con gli altri paesi: la cella riporta il valore italiano (rango sul solo dato italiano). "
      "Unità: punti percentuali o punti di PIL; punti base per lo spread; migliaia di persone per "
      "l'emigrazione. Il governo in carica è in grassetto. *n.d.* = serie assente per quegli anni.")
    w("")
    for amb in AMBITI:
        inds = [i for i in INDICATORI if i["ambito"] == amb]
        w(f"### {amb[0].upper() + amb[1:]}")
        w("")
        w("| Governo o periodo | Anni | " + " | ".join(f"{i['nome']} ({i['unita']})" for i in inds) + " |")
        w("|---|---|" + "---|" * len(inds))
        for k in conf:
            u = U[k]
            if all((RIS[("base", i["id"])][k]["diff"] if i["vicini"] else RIS[("base", i["id"])][k]["it"]) is None for i in inds):
                continue
            celle = []
            for i in inds:
                r = RIS[("base", i["id"])][k]
                v = r["diff"] if i["vicini"] else r["it"]
                celle.append(f"{it(v, dec(i), segno=i['vicini'])} ({r['rango']})" if v is not None else "n.d.")
            nome = f"**{u['etichetta']}**" if k == kc else u["etichetta"]
            w(f"| {nome} | {fmt_anni(u['anni'])} | " + " | ".join(celle) + " |")
        w("")
    w("Verso: crescita, produttività, investimenti pubblici, occupazione e saldo primario, più alto è meglio; "
      "disoccupazione giovanile, debito, deficit, spread, inflazione, povertà ed emigrazione, più basso è meglio. "
      "Per la pressione fiscale il rango è solo un ordinamento (1 = calo maggiore rispetto ai vicini), non un giudizio.")
    w("")

    # ---------------- Governo in carica: dettaglio
    w("## 3. Il governo in carica, indicatore per indicatore")
    w("")
    w("| Indicatore (unità, anni) | Italia | Vicini | Differenza | Rango | Rango tra i governi con almeno 2 anni | Rango sul solo dato italiano |")
    w("|---|---|---|---|---|---|---|")
    for i in INDICATORI:
        r = r_(i["id"])
        rm, nm = rango_multi_anno(R, i, kc)
        w(f"| {i['nome']} ({i['unita']}, {r['anni_eff']}) | {it(r['it'], dec(i))} | {it(r['vic'], dec(i))} | "
          f"{it(r['diff'], dec(i), True)} | {rk_txt(r)} | {f'{rm}° su {nm}' if rm else 'n.d.'} | "
          f"{rk_txt(r, 'rango_it', 'n_it')} |")
    w("")
    w("La colonna \"solo dato italiano\" mostra quanto cambia il quadro se non si tolgono gli shock comuni: per esempio "
      "l'occupazione italiana sale molto in assoluto, ma sale anche nei paesi vicini.")
    w("")
    pf = r_("pressione_fiscale")
    am = leggi_serie("pressione_fiscale")
    if all(a1 in am[p] and a0 in am[p] for p in ["IT"] + VICINI):
        it_am = am["IT"][a1] - am["IT"][a0]
        vic_am = statistics.mean(am[p][a1] - am[p][a0] for p in VICINI)
        w(f"*Pressione fiscale, controllo.* La serie OCSE, usata perché copre tutti i governi dal 1979, si ferma al 2024 "
          f"(Italia {it(pf['it'], 1, True)} punti nel {pf['anni_eff']}, vicini {it(pf['vic'], 1, True)}). Con la serie AMECO, "
          f"che arriva al {a1}, l'Italia passa da {it(am['IT'][a0])}% a {it(am['IT'][a1])}% del PIL ({it(it_am, 1, True)} punti) "
          f"contro {it(vic_am, 1, True)} punti in media nei vicini: il segno del confronto non cambia.")
        w("")

    # ---------------- Eredita' e contesto
    w("## 4. Punto di partenza e contesto di ogni governo")
    w("")
    w("Il punto di partenza è l'anno prima del primo anno assegnato. Gli shock sono quelli esterni che cadono negli anni "
      "assegnati; non correggono i numeri, servono a leggerli.")
    w("")
    w("| Governo o periodo | Anno di partenza | Debito (% PIL) | Deficit (% PIL) | Spread (p.b.) | Shock esterni nel mandato |")
    w("|---|---|---|---|---|---|")
    ctx = {k: contesto(U[k], serie) for k in conf}
    for k in conf:
        c = ctx[k]
        nome = f"**{U[k]['etichetta']}**" if k == kc else U[k]["etichetta"]
        w(f"| {nome} | {c['anno_partenza']} | {it(c['debito0'])} | {it(c['deficit0'])} | {it(c['spread0'], 0)} | "
          f"{'; '.join(c['shock']) or '-'} |")
    w("")
    cc = ctx[kc]
    debiti = [ctx[k]["debito0"] for k in conf if ctx[k]["debito0"] is not None]
    pos_deb = 1 + sum(1 for x in debiti if x > cc["debito0"])
    kmax = max(conf, key=lambda k: ctx[k]["debito0"] or 0)
    w("### Cosa ha ereditato il governo in carica")
    w("")
    w(f"- **Debito**: {it(cc['debito0'])}% del PIL nel {cc['anno_partenza']}, il {pos_deb}° punto di partenza più alto "
      f"tra i {len(debiti)} governi confrontati (il più alto è il {it(ctx[kmax]['debito0'])}% trovato dal {U[kmax]['etichetta']}).")
    w(f"- **Deficit**: {it(cc['deficit0'])}% del PIL nel {cc['anno_partenza']}, gonfiato dai crediti per i bonus edilizi "
      f"decisi nel 2020-2021 (catalogo D105), registrati nei conti dal 2020 al 2023 dopo la riclassificazione Eurostat. "
      f"Anche il deficit del {a0 + 1} ({it(-sv('deficit_pil', a0 + 1))}%) contiene una quota rilevante di questi crediti.")
    w(f"- **Spread**: {it(cc['spread0'], 0)} punti base di media nel {cc['anno_partenza']}, salito con il rialzo dei tassi BCE.")
    w(f"- **Inflazione**: {it(sv('inflazione', a0))}% nel {a0}, per lo shock energetico.")
    w(f"- **Lavoro**: occupazione 15-64 al {it(sv('occupazione_15_64', a0))}% nel {a0}, già in salita dal 2021.")
    w("- **Decisioni già prese**: il Piano nazionale di ripresa e resilienza (D107), deciso nel 2021, con spesa concentrata "
      "negli anni 2023-2026; i crediti edilizi già maturati, che pesano sul debito negli anni in cui vengono usati in "
      "compensazione; dal 2024 le nuove regole europee sui conti pubblici (D120).")
    w("")
    w("### Contesto esterno nel mandato")
    w("")
    w("- 2023: coda dello shock energetico e tassi BCE ai livelli più alti da oltre quindici anni; inflazione in calo in tutta l'area euro.")
    w(f"- {fmt_anni(corr['anni'])}: crescita debole nei paesi vicini (in Germania il PIL pro capite cala nel 2023 e nel 2024), "
      "il che rende più facile un buon risultato *relativo* dell'Italia; spesa del PNRR in aumento.")
    w("- Nessuna crisi finanziaria o sanitaria paragonabile a quelle del 1992, 2008-09, 2011-12 o 2020.")
    w("")

    # ---------------- Ritardi
    w("## 5. Ritardi degli effetti: versione con gli anni spostati di uno")
    w("")
    w("Le misure agiscono con ritardo. Qui a ogni governo si assegnano gli anni spostati in avanti di uno (per il governo "
      f"in carica: {fmt_anni(r_('pil_pc', v='ritardo_1_anno')['anni'])}, perché il 2026 è solo una previsione).")
    w("")
    w("| Indicatore | Differenza (anni propri) | Rango | Differenza (anni +1) | Rango |")
    w("|---|---|---|---|---|")
    for i in INDICATORI:
        a, b = r_(i["id"]), r_(i["id"], v="ritardo_1_anno")
        va = a["diff"] if i["vicini"] else a["it"]
        vb = b["diff"] if i["vicini"] else b["it"]
        w(f"| {i['nome']}{'' if i['vicini'] else ' (solo Italia)'} | {it(va, dec(i), i['vicini'])} | {rk_txt(a)} | "
          f"{it(vb, dec(i), i['vicini'])} | {rk_txt(b)} |")
    w("")
    w("| Ambito | Posizione mediana, anni propri | Posizione mediana, anni +1 |")
    w("|---|---|---|")
    for amb in AMBITI:
        w(f"| {amb} | {it(S[kc][amb], 0)} ({fascia(S[kc][amb])}) | {it(S_rit[kc][amb], 0)} ({fascia(S_rit[kc][amb])}) |")
    w("")

    # ---------------- Sintesi per ambito
    w("## 6. Sintesi per ambito di tutti i governi")
    w("")
    w("Posizione mediana 0-100 (100 = primo in tutti gli indicatori dell'ambito). Un governo può andare bene sui "
      "conti e male sulla crescita, e il peso da dare a ciascun ambito è una scelta politica: per questo il punteggio "
      "complessivo si calcola con tutte le combinazioni di pesi (storia/punti_di_vista.md).")
    w("")
    w("| Governo o periodo | Anni | " + " | ".join(AMBITI) + " |")
    w("|---|---|" + "---|" * len(AMBITI))
    for k in conf:
        nome = f"**{U[k]['etichetta']}**" if k == kc else U[k]["etichetta"]
        w(f"| {nome} | {fmt_anni(U[k]['anni'])} | " + " | ".join(it(S[k][a], 0) for a in AMBITI) + " |")
    w("")
    w("Attenzione: i governi con un solo anno assegnato hanno posizioni più estreme (in alto o in basso) anche per semplice "
      "variabilità; i governi lunghi tendono verso il centro. L'ambito società ha dati solo dal 2002-2005.")
    w("")

    # ---------------- Merito e responsabilita'
    dd = [-sv("deficit_pil", a) for a in corr["anni"]]
    sp = [sv("saldo_primario_pil", a) for a in corr["anni"]]
    spr = [sv("spread_bund", a) for a in [a0] + corr["anni"]]
    emi = RIS[("base", "emigrazione")]
    emi_max = max((r["it"] for k, r in emi.items() if U[k]["confrontabile"] and r["it"] is not None), default=None)
    w("## 7. Cosa è merito o responsabilità plausibile, e cosa no")
    w("")
    w("Questa parte è un giudizio prudente, non una misura. \"Plausibile\" vuol dire che i tempi e il meccanismo sono "
      "coerenti con una scelta del governo, non che l'effetto sia dimostrato.")
    w("")
    w("**Plausibilmente legato, in tutto o in parte, a scelte del governo in carica**")
    w("")
    w(f"- *Rientro del deficit*: da {it(dd[0])}% ({corr['anni'][0]}) a {it(dd[-1])}% ({corr['anni'][-1]}) del PIL, con "
      f"il saldo primario tornato positivo ({it(sp[-1], 1, True)}% nel {corr['anni'][-1]}). Ha contribuito lo stop alla cessione "
      "dei crediti edilizi (D112), insieme alla fine delle misure temporanee contro il caro energia. Una parte del miglioramento "
      "è però meccanica: i crediti decisi nel 2020-2021 erano già stati contabilizzati negli anni precedenti, e pesano "
      f"ancora sul {corr['anni'][0]}, che abbassa la media del mandato.")
    w(f"- *Pressione fiscale in aumento mentre nei vicini scende* ({rk_txt(pf)} nell'ordinamento dal calo maggiore "
      "all'aumento maggiore rispetto ai vicini). Una parte dipende da scelte (le modifiche all'IRPEF e il taglio dei contributi "
      "riducono il prelievo, D116), una parte dall'aumento degli occupati e dal drenaggio fiscale (scaglioni non adeguati "
      "all'inflazione). I dati qui non separano le due parti.")
    w(f"- *Spread*: la discesa da {it(spr[0], 0)} ({a0}) a {it(spr[-1], 0)} punti base ({a1}) è coerente con un percorso dei "
      "conti giudicato credibile dai mercati, ma avviene mentre la BCE dispone di uno strumento contro gli aumenti "
      "ingiustificati degli spread (dal 2022) e mentre lo spread francese sale per ragioni interne alla Francia: il "
      "confronto relativo ne risulta favorito.")
    w("")
    w("**Plausibilmente non (o non solo) dovuto al governo in carica**")
    w("")
    w("- *Inflazione più bassa dei vicini*: dipende soprattutto dal calo dei prezzi dell'energia, a cui l'Italia è più esposta "
      "(i prezzi salgono di più nel 2022 e scendono di più dopo), e dalla politica monetaria della BCE.")
    w("- *Occupazione ai massimi e disoccupazione giovanile in calo*: la crescita parte nel 2021; il calo della popolazione in età "
      "da lavoro alza il tasso anche a parità di occupati. Il vantaggio rispetto ai vicini resta positivo, ma si riduce con gli "
      "anni spostati di uno.")
    w("- *Investimenti pubblici ai massimi della serie*: spinti dal PNRR, deciso e finanziato prima (D107). La responsabilità "
      "del governo in carica riguarda l'attuazione, che la Corte dei conti (citata nel catalogo) giudica in ritardo sulla spesa effettiva.")
    w("- *Debito quasi stabile*: aiutato dall'inflazione del 2022-2023, che fa crescere il PIL nominale, e frenato dai crediti "
      "edilizi già decisi, che pesano sul debito quando vengono usati in compensazione.")
    w("- *Produttività in calo*: è il dato peggiore del governo in carica rispetto ai vicini. Riflette in parte proprio la "
      "crescita delle ore lavorate più rapida della produzione, e un problema strutturale aperto da oltre vent'anni (rottura "
      "del 2001 in `serie_lunghe.md`); non è attribuibile a un singolo mandato.")
    w(f"- *Emigrazione di italiani*: la media annua ({it(r_('emigrazione')['it'], 0)} mila) "
      f"{'è la più alta' if emi_max is not None and r_('emigrazione')['it'] >= emi_max else 'è tra le più alte'} "
      "tra i governi dal 2002, ma la serie sale quasi ogni anno dal 2008: il rango riflette soprattutto la tendenza di lungo "
      "periodo e i cambiamenti nelle registrazioni all'anagrafe, non un effetto del mandato.")
    w(f"- *Povertà assoluta*: {it(sv('poverta_assoluta', a0))}% nel {a0}, {it(sv('poverta_assoluta', a1))}% nel {a1}. La "
      "variazione è piccola, vicina all'errore statistico dell'indagine. La sostituzione del Reddito di cittadinanza con "
      "l'Assegno di inclusione (D114), secondo le stime della Banca d'Italia riportate nel catalogo, riduce la povertà meno "
      "della misura precedente: il lieve calo è quindi più probabilmente legato a lavoro e prezzi.")
    w("")

    # ---------------- Decisioni del catalogo
    w("## 8. Decisioni del catalogo per governo")
    w("")
    w("**Avvertenza.** Il catalogo `decisioni_1977_2026.csv` è una selezione di 120 decisioni fatta da chi ha costruito "
      "la base dati. La scelta di cosa includere è soggettiva e il numero di decisioni per governo dipende da quella scelta. "
      "**Non va usato come voto ai governi**: serve solo a ricordare quali misure di rilievo cadono in ciascun mandato e cosa "
      "dicono le valutazioni disponibili. Ogni decisione è assegnata al governo dello stesso presidente del Consiglio "
      "in carica per più giorni in quell'anno (quando lo stesso presidente guida due governi nello stesso anno l'assegnazione "
      "è segnata con *). Le decisioni del 1977 sono di un governo precedente al periodo esaminato.")
    w("")
    w("| Governo o periodo | Decisioni | Efficace | Efficace in parte | Evidenza insufficiente | Inefficace | Effetti negativi |")
    w("|---|---|---|---|---|---|---|")
    cat = ["efficace", "efficace in parte", "evidenza insufficiente", "inefficace", "effetti negativi"]
    for k, u in enumerate(U):
        ds = R["decisioni"].get(k, [])
        if not ds:
            continue
        cnt = [sum(1 for d in ds if d["giudizio"] == c) for c in cat]
        nome = f"**{u['etichetta']}**" if k == kc else u["etichetta"]
        w(f"| {nome}{'' if u['confrontabile'] else ' (fuori classifica)'} | {len(ds)} | " + " | ".join(map(str, cnt)) + " |")
    w("")
    for k in (kp, kc):
        w(f"**Decisioni del catalogo nel {U[k]['etichetta']}**")
        w("")
        w("| Id | Anno | Decisione | Giudizio | Solidità dell'evidenza |")
        w("|---|---|---|---|---|")
        for d in R["decisioni"].get(k, []):
            w(f"| {d['id']}{'*' if d.get('_ambiguo') else ''} | {d['anno']} | {d['decisione']} | {d['giudizio']} | "
              f"{d['solidita_evidenza']} |")
        w("")
    w("Per il governo in carica quasi tutte le decisioni hanno \"evidenza insufficiente\" perché sono recenti, non perché "
      "siano state valutate male. Alcune decisioni con effetti nel mandato in corso (PNRR, crediti edilizi) appartengono ai "
      "governi precedenti.")
    w("")

    # ---------------- Cosa non sappiamo
    w("## 9. Cosa non sappiamo e limiti")
    w("")
    w(f"1. **Mandato in corso.** Il governo in carica ha {len(corr['anni'])} anni di dati ({fmt_anni(corr['anni'])}); il 2025 "
      "è ancora un consuntivo provvisorio e il 2026 è escluso perché è una previsione. Il giudizio su un mandato in corso "
      "può cambiare con i dati del 2026 e con le revisioni.")
    w("2. **Ritardi.** Molte misure agiscono dopo anni (pensioni, istruzione, giustizia, investimenti). La versione con gli "
      "anni spostati di uno coglie solo i ritardi brevi; quelli lunghi non sono misurabili con questo metodo.")
    w("3. **Pochi anni.** Molti governi hanno uno o due anni assegnati: un anno buono o cattivo pesa moltissimo. Per questo "
      "il rapporto mostra anche il rango tra i soli governi con almeno due anni.")
    w("4. **Nessuna causalità.** La differenza con i vicini toglie gli shock comuni, non quelli che colpiscono l'Italia più "
      "degli altri (energia, debito alto quando salgono i tassi, calo demografico). Non dice cosa sarebbe successo con scelte diverse.")
    w("5. **Eredità.** I risultati di un governo dipendono anche dalle decisioni dei governi precedenti (bonus edilizi, PNRR, "
      "riforme delle pensioni) e dal punto di partenza (debito, spread). La tabella del punto di partenza aiuta a leggerli, "
      "ma non li corregge.")
    w("6. **Dati non omogenei.** Prima del 1991 la Germania è la Germania Ovest; per deficit e saldo primario la Spagna manca "
      "prima del 1995 (media su Francia e Germania); gli investimenti pubblici partono dal 1995; la pressione fiscale OCSE "
      "si ferma al 2024; povertà assoluta ed emigrazione non hanno un confronto omogeneo con gli altri paesi; la povertà "
      "assoluta cambia metodo nel 2014 (il governo 2014-2016 non ha un valore); lo spread prima del 1999 misura anche il "
      "rischio di cambio.")
    w("7. **Indicatori scelti.** Gli indicatori coprono conti, crescita, lavoro, prezzi e società, ma non misurano qualità "
      "dei servizi, giustizia, ambiente, sicurezza o istruzione: un governo può andare meglio o peggio su aspetti che qui "
      "non compaiono.")
    w("8. **Verso degli indicatori.** Dire che \"più basso è meglio\" per deficit, debito, inflazione o emigrazione è una "
      "convenzione largamente condivisa, ma non vale in ogni circostanza (un deficit alto durante una recessione può essere "
      "la scelta giusta). Per la pressione fiscale non si dà alcun verso.")
    w("")
    w("## Fonti")
    w("")
    w("- Elenco e date dei governi: Presidenza del Consiglio dei ministri, *I Governi nelle Legislature* "
      "(https://www.governo.it/it/i-governi-dal-1943-ad-oggi/i-governi-nelle-legislature/192) per i governi dal 2001; "
      "Camera dei deputati, dati aperti (https://dati.camera.it, classe ocd:governo) per le date dei governi 1978-2001. "
      "Numerazione: secondo governo De Gasperi (13 luglio 1946) = n. 1, coerente con i 68 governi della Repubblica "
      "indicati dalla Presidenza del Consiglio.")
    w("- Serie: `storia/serie/_registro.csv` (AMECO, FMI, OCSE, Eurostat, ISTAT).")
    w("- Decisioni: `storia/decisioni_1977_2026.csv`.")
    w("")
    (BASE / "governi_confronto.md").write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    R = esegui()
    scrivi_csv(R)
    scrivi_rapporto(R)
    print("Scritti: storia/governi_confronto.csv, storia/governi_confronto.md")
