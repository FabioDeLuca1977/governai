"""Uscite del modulo europa/ per il resto di GovernAI, generate dall'archivio (nessuna richiesta di rete).

  europa/scadenze.csv   direttive con termine di recepimento (prossimi 24 mesi o scaduto), stato per l'Italia, aree, proposte
  europa/novita.md      atti UE degli ultimi 30 giorni, per area, in italiano chiaro
  europa/semestre.md    raccomandazioni all'Italia, procedura per disavanzo eccessivo, scadenze del ciclo di bilancio
  europa/infrazioni.csv procedure d'infrazione aperte contro l'Italia (EUR-Infra), con aree e proposte
  europa/stato.json     conteggi per area e sintesi, per il Consiglio dei ministri e per il sito

Funzioni per gli altri moduli (vedi README, "Integrazione"):
  contesto_consiglio(aree) -> dict      da mettere in contesto.json di una seduta
  odg_consiglio(aree) -> list[str]      righe markdown per l'ordine del giorno
  dati_web() -> dict                    dati compatti per docs/data.js

Uso: python uscite.py
"""
from __future__ import annotations

import csv
import re
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pertinenza import ETICHETTE_AREE, RE_RIF_UE, Regole, chiave_atto, chiave_celex, togli_intestazione
from rete import ARCHIVIO, QUI, STATO_ARCHIVIO, leggi_json, scrivi_json

CAMPI_PERT = ["aree", "proposte", "esperti", "impatto", "rilevanza", "riguarda_italia", "motivo"]
CAMPI_SCAD = ["priorita", "celex", "tipo", "titolo", "data_atto", "termine_recepimento", "giorni_al_termine", "stato",
              "misure_it_notificate", "ultima_notifica_it", "esempio_misura_it", "infrazione", "fase_infrazione",
              "altri_termini", "termine_dal_testo", "aree", "proposte", "esperti", "url_eurlex", "url_misure_nazionali", "eli"]
CAMPI_INF = ["numero", "oggetto", "dg", "materia", "norme", "inadempienza", "fase", "articolo", "mancato_recepimento",
             "direttiva_celex", "aree", "proposte", "esperti", "prima_rilevazione", "novita", "fasi_precedenti", "fonte"]
STATI = {
    "infrazione": "procedura d'infrazione aperta",
    "scaduto_senza_misure": "termine scaduto, nessuna misura italiana notificata",
    "scaduto_con_misure": "termine scaduto, misure italiane notificate (completezza non verificata)",
    "da_recepire": "in termine, nessuna misura italiana ancora notificata",
    "in_termine_con_misure": "in termine, misure italiane già notificate",
}
PRIORITA = {1: "critica", 2: "alta", 3: "media", 4: "bassa"}


def leggi_csv(p: Path) -> list[dict]:
    if not p.exists():
        return []
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def scrivi_csv(p: Path, righe: list[dict], campi: list[str]) -> None:
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campi, extrasaction="ignore")
        w.writeheader()
        w.writerows(righe)


def it(d: str) -> str:
    """AAAA-MM-GG -> GG/MM/AAAA."""
    return f"{d[8:10]}/{d[5:7]}/{d[:4]}" if re.match(r"\d{4}-\d{2}-\d{2}", d or "") else (d or "")


def titolo_breve(t: str, n: int = 240) -> str:
    """Toglie l'intestazione ('Regolamento (UE) 2026/1 della Commissione, del 3 ottobre 2026,') e accorcia."""
    t = togli_intestazione(t)
    t = t[:1].upper() + t[1:]
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0] + " …"


def numero_atto(r: dict) -> str:
    if r.get("rif_gu"):
        return r["rif_gu"]
    m = re.search(r"/(\d{4})/(\d+)/oj", r.get("eli", ""))
    return f"{m.group(1)}/{m.group(2)}" if m else r.get("celex", "")


def numero_com(s: str) -> str:
    """'COM_2026_0547_FIN' -> 'COM(2026) 547'."""
    m = re.match(r"([A-Z]+)_(\d{4})_0*(\d+)", s or "")
    return f"{m.group(1)}({m.group(2)}) {m.group(3)}" if m else (s or "")


def lista_aree(s: str) -> list[str]:
    return [x for x in (s or "").split(",") if x]


# --- Elaborazioni -------------------------------------------------------------------------------------

def classifica_atti(R: Regole) -> list[dict]:
    p = ARCHIVIO / "atti.csv"
    atti = leggi_csv(p)
    if not atti:
        return []
    for a in atti:
        a.update(R.valuta(a))
    campi = list(dict.fromkeys(list(atti[0].keys()) + CAMPI_PERT))
    scrivi_csv(p, atti, campi)
    return atti


def infrazioni(R: Regole, stato_arch: dict) -> list[dict]:
    grezze = leggi_csv(ARCHIVIO / "infrazioni_eurinfra.csv")
    storico = {r["numero"]: r for r in leggi_csv(ARCHIVIO / "infrazioni_storico.csv")}
    prima_esec = stato_arch.get("infrazioni_prima_esecuzione", "") or date.today().isoformat()
    out = []
    for g in grezze:
        r = {"numero": g.get("NumProc", ""), "oggetto": g.get("Oggetto", ""), "dg": g.get("DirGen", ""),
             "materia": g.get("Materia", ""), "norme": g.get("Norme", ""), "inadempienza": g.get("Inadempienza", ""),
             "fase": g.get("Fase", ""), "fonte": "EUR-Infra (Dipartimento per gli affari europei)"}
        art = re.search(r"Art\.?\s*(\d{3})", r["fase"])
        r["articolo"] = f"art. {art.group(1)} TFUE" if art else ""
        r["mancato_recepimento"] = "sì" if "recepimento" in r["inadempienza"].lower() else ""
        chiavi = [chiave_atto(m.group(1), m.group(2)) for m in RE_RIF_UE.finditer(r["oggetto"] + " " + r["norme"])
                  if re.match(r"dir", m.group(0), re.I)]
        r["direttiva_celex"] = " ".join(dict.fromkeys(f"3{k.split('/')[0]}L{int(k.split('/')[1]):04d}" for k in chiavi))
        r.update(R.valuta_infrazione(r))
        s = storico.get(r["numero"], {})
        r["prima_rilevazione"] = s.get("prima_rilevazione", "")
        r["fasi_precedenti"] = s.get("fasi_precedenti", "")
        # novità degli ultimi 30 giorni rispetto alle rilevazioni precedenti (la prima rilevazione fa da base)
        soglia = (date.today() - timedelta(days=30)).isoformat()
        if r["prima_rilevazione"] > prima_esec and r["prima_rilevazione"] >= soglia:
            r["novita"] = "nuova"
        elif s.get("cambio_fase", "") >= soglia:
            r["novita"] = "cambio di fase"
        else:
            r["novita"] = ""
        out.append(r)
    return out


def scadenze(R: Regole, inf: list[dict], atti: list[dict]) -> list[dict]:
    oggi = date.today()
    inf_per_dir = {}
    for r in inf:
        for c in r["direttiva_celex"].split():
            inf_per_dir.setdefault(c, []).append(r)
    termine_testo = {a["celex"]: a.get("termine_testo", "") for a in atti}
    out = []
    for d in leggi_csv(ARCHIVIO / "direttive.csv"):
        if not d.get("termine_recepimento") or d.get("in_vigore") == "0":
            continue
        pert = R.valuta(d)
        termine = date.fromisoformat(d["termine_recepimento"])
        giorni = (termine - oggi).days
        n = int(d.get("misure_it") or 0)
        procs = inf_per_dir.get(d["celex"], [])
        if procs:
            st = "infrazione"
        elif giorni < 0:
            st = "scaduto_con_misure" if n else "scaduto_senza_misure"
        else:
            st = "in_termine_con_misure" if n else "da_recepire"
        if st == "infrazione" or st == "scaduto_senza_misure":
            prio = 1
        elif st == "da_recepire" and giorni <= 183:
            prio = 2
        elif giorni <= 365:
            prio = 3
        else:
            prio = 4
        tt = termine_testo.get(d["celex"], "")
        out.append({
            "priorita": PRIORITA[prio], "_p": prio, "celex": d["celex"], "tipo": d["tipo"], "titolo": d["titolo"],
            "data_atto": d["data_atto"], "termine_recepimento": d["termine_recepimento"], "giorni_al_termine": giorni,
            "stato": STATI[st], "misure_it_notificate": n, "ultima_notifica_it": d.get("ultima_notifica_it", ""),
            "esempio_misura_it": d.get("esempio_misura_it", ""),
            "infrazione": " ".join(p["numero"] for p in procs), "fase_infrazione": "; ".join(p["fase"] for p in procs),
            "altri_termini": d.get("termini", ""),
            "termine_dal_testo": (tt + (" (coincide)" if tt == d["termine_recepimento"] else " (DIVERSO: verificare)")) if tt else "",
            "aree": pert["aree"], "proposte": pert["proposte"], "esperti": pert["esperti"],
            "url_eurlex": d["url_eurlex"], "url_misure_nazionali": d.get("url_misure_nazionali", ""), "eli": d.get("eli", ""),
        })
    out.sort(key=lambda x: (x["_p"], x["termine_recepimento"] if x["_p"] > 1 else "", x["celex"]))
    return out


# --- Testi markdown -------------------------------------------------------------------------------------

def riga_atto(a: dict) -> str:
    extra = []
    if a.get("termine_recepimento"):
        extra.append(f"recepimento entro il **{it(a['termine_recepimento'])}**")
    if a.get("proposte"):
        extra.append("proposte collegate: " + ", ".join(a["proposte"].split(",")))
    if a.get("riguarda_italia"):
        extra.append("**riguarda l'Italia**")
    return (f"- **{a['tipo']} {numero_atto(a)}** ({it(a['data_atto'])}, GU L del {it(a['data_gu'])}) — "
            f"{titolo_breve(a['titolo']) or '(titolo italiano non ancora disponibile)'} · impatto: *{a['impatto']}*"
            + ("; " + "; ".join(extra) if extra else "") + f" · [EUR-Lex]({a['url_eurlex']})")


def novita_md(atti: list[dict], prop: list[dict], inf: list[dict], scad: list[dict], R: Regole, stato_arch: dict) -> str:
    oggi = date.today()
    g = R.finestre["novita_giorni"]
    dal = (oggi - timedelta(days=g)).isoformat()
    recenti = [a for a in atti if a.get("data_gu", "") >= dal]
    rec_prop = [p for p in prop if p.get("data_atto", "") >= dal]
    per_imp = {}
    for a in recenti:
        per_imp[a["impatto"]] = per_imp.get(a["impatto"], 0) + 1
    L = [f"# Novità dall'Unione europea — ultimi {g} giorni", "",
         f"*Aggiornato al {it(oggi.isoformat())}. Atti pubblicati nella Gazzetta ufficiale dell'UE, serie L, dal {it(dal)}; "
         f"fonte: CELLAR (Ufficio delle pubblicazioni dell'UE). Generato da `europa/scarica_ue.py`: non modificare a mano.*", "",
         f"In {g} giorni l'UE ha pubblicato **{len(recenti)} atti** nella serie L: "
         + ", ".join(f"{n} con impatto *{k}*" for k, n in sorted(per_imp.items(), key=lambda x: -x[1])) + ".", "",
         "Come leggere questa pagina:",
         "- **obbligo**: una direttiva da recepire con una legge o un decreto, oppure un regolamento o una decisione che si applica direttamente;",
         "- **vincolo di bilancio**: regole o raccomandazioni sui conti pubblici (Semestre europeo, procedura per disavanzo);",
         "- **opportunità**: fondi o programmi europei a cui l'Italia può attingere;",
         "- **informativo**: rettifiche, atti di gestione corrente (autorizzazioni, registrazioni, elenchi) o rivolti ad altri Stati.", "",
         "Per ogni area sono elencati gli atti di rilevanza alta e media; quelli di rilevanza bassa sono solo contati "
         "(elenco completo in `europa/archivio/atti.csv`). Un atto può riguardare più aree e comparire più volte. "
         "Le regole che assegnano aree, proposte e impatto sono in `europa/regole.yaml`.", ""]
    urgenti = [s for s in scad if s["_p"] <= 2][:8]
    if urgenti:
        L += ["## Da tenere d'occhio: obblighi di recepimento", ""]
        L += [f"- **{s['tipo']} {chiave_celex(s['celex'])}** — {titolo_breve(s['titolo'], 160)}: termine {it(s['termine_recepimento'])}, "
              f"{s['stato']}" + (f" (procedura {s['infrazione']})" if s["infrazione"] else "") + f" · aree {s['aree'] or '—'}"
              for s in urgenti]
        L += ["", "Elenco completo con stato e priorità in `europa/scadenze.csv`.", ""]
    for area in list(ETICHETTE_AREE) + [""]:
        qui = [a for a in recenti if (area in lista_aree(a["aree"]) if area else not a["aree"])]
        if not qui:
            continue
        nome = f"{area} — {ETICHETTE_AREE[area]}" if area else "Senza area assegnata"
        alte = [a for a in qui if a["rilevanza"] == "alta"]
        medie = [a for a in qui if a["rilevanza"] == "media"]
        basse = len(qui) - len(alte) - len(medie)
        L += [f"## {nome}", "", f"{len(qui)} atti: {len(alte)} di rilevanza alta, {len(medie)} media, {basse} bassa.", ""]
        if alte:
            L += [riga_atto(a) for a in alte]
        if medie:
            mostra = medie[:12]
            L += (["", "Rilevanza media:"] if alte else ["Rilevanza media:"]) + [riga_atto(a) for a in mostra]
            if len(medie) > len(mostra):
                L += [f"- … e altri {len(medie) - len(mostra)} atti di rilevanza media (vedi l'archivio)."]
        L += [""]
    if rec_prop:
        L += [f"## Proposte legislative della Commissione (ultimi {g} giorni)", "",
              "Sono proposte in discussione: non obbligano ancora, ma anticipano obblighi futuri. "
              "Lo stato della procedura legislativa è nella pagina «Procedura» di EUR-Lex.", ""]
        for p in sorted(rec_prop, key=lambda x: (x["rilevanza"] != "alta", x["data_atto"])):
            if p["rilevanza"] == "bassa":
                continue
            L.append(f"- **{p['tipo']}** {numero_com(p.get('numero_com')) or p['celex']} ({it(p['data_atto'])}) — {titolo_breve(p['titolo'], 220)}"
                     f" · aree {p['aree'] or '—'}" + (f" · proposte collegate: {p['proposte']}" if p["proposte"] else "")
                     + f" · [procedura]({p['url_procedura']})")
        basse = sum(1 for p in rec_prop if p["rilevanza"] == "bassa")
        if basse:
            L.append(f"- … e {basse} proposte di rilevanza bassa (decisioni su posizioni in organismi internazionali, ecc.), in `europa/archivio/proposte_ue.csv`.")
        L += [""]
    L += ["## Procedure d'infrazione", ""]
    if inf:
        nuove = [r for r in inf if r["novita"]]
        L += [f"Procedure aperte contro l'Italia secondo EUR-Infra: **{len(inf)}**, di cui "
              f"{sum(1 for r in inf if r['mancato_recepimento'])} per mancato recepimento di direttive. Elenco in `europa/infrazioni.csv`.", ""]
        if nuove:
            L += ["Novità rispetto alla rilevazione precedente:"] + [f"- {r['numero']} ({r['novita']}): {r['oggetto'][:200]} — {r['fase']}" for r in nuove]
        elif stato_arch.get("infrazioni_prima_esecuzione") == oggi.isoformat():
            L += ["Prima rilevazione: le novità (nuove procedure, cambi di fase, archiviazioni) saranno segnalate dalle esecuzioni successive."]
        else:
            L += ["Nessuna novità rispetto alla rilevazione precedente."]
        agg = stato_arch.get("dpe_aggiornamenti", [])
        if agg:
            L += ["", f"Ultimo aggiornamento del Dipartimento per gli affari europei — *{agg[0]['titolo']}*: {agg[0]['sintesi']}"
                  + (f" ([pagina]({agg[0]['url']}))" if agg[0].get("url") else "")]
    else:
        L += ["La fonte EUR-Infra non ha risposto: nessun dato sulle infrazioni in questa esecuzione."]
    L += ["", "Semestre europeo e regole di bilancio: vedi `europa/semestre.md`.", ""]
    return "\n".join(L)


SCADENZE_CICLO = [
    # (mese, giorno, cosa, fonte) — scadenze ricorrenti fissate dai regolamenti; testo vigente da verificare su EUR-Lex
    (4, 30, "l'Italia presenta la relazione annuale sui progressi (spesa netta, riforme e investimenti del piano)",
     "Reg. (UE) 2024/1263, art. 21"),
    (10, 15, "l'Italia presenta alla Commissione e all'Eurogruppo il documento programmatico di bilancio per l'anno successivo",
     "Reg. (UE) n. 473/2013, art. 6"),
    (11, 30, "la Commissione adotta il parere sul documento programmatico di bilancio (entro il 30 novembre)",
     "Reg. (UE) n. 473/2013, art. 7"),
    (12, 31, "la legge di bilancio è adottata e pubblicata", "Reg. (UE) n. 473/2013, art. 4"),
]


def semestre_md(sem: dict, atti: list[dict]) -> str:
    oggi = date.today()
    L = ["# Semestre europeo e regole di bilancio: l'Italia", "",
         f"*Aggiornato al {it(oggi.isoformat())}. Fonti: CELLAR (atti e documenti UE), DG ECFIN della Commissione (cronologia "
         "della procedura per disavanzo eccessivo). Le frasi tra virgolette sono citazioni testuali degli atti. Generato da "
         "`europa/scarica_ue.py`: non modificare a mano.*", ""]
    csr = sem.get("csr", {})
    pag = sem.get("edp_pagina", {})
    docs = [d for d in sem.get("documenti", []) if d["celex"][:1] in "35"]  # atti e documenti preparatori, non giurisprudenza
    sem = {**sem, "documenti": docs}
    recenti = [d for d in docs if d["data"] >= (oggi - timedelta(days=90)).isoformat()]
    L += ["## Novità degli ultimi 90 giorni", ""]
    L += [f"- **{it(d['data'])}** — [{d['titolo']}]({d['url']}) (CELEX {d['celex']})"
          + (" — *documento della Commissione: produce effetti solo quando il Consiglio adotta l'atto*" if d["celex"].startswith("5") else "")
          for d in recenti] or ["- Nessun nuovo documento del Semestre sull'Italia."]
    L += ["", "## Procedura per disavanzo eccessivo", ""]
    dec = [d for d in sem.get("documenti", []) if "esistenza di un disavanzo eccessivo" in d["titolo"] and d["celex"].startswith("3")]
    abroga = [d for d in sem.get("documenti", []) if "abroga" in d["titolo"].lower() and "disavanzo" in d["titolo"].lower()]
    if dec:
        L.append(f"- **Apertura**: {dec[0]['titolo']} ([EUR-Lex]({dec[0]['url']})).")
    L.append("- **Chiusura**: " + (f"{abroga[0]['titolo']} ([EUR-Lex]({abroga[0]['url']}))." if abroga else
                                   "nessuna decisione del Consiglio che abroga la procedura per l'Italia risulta in CELLAR a oggi."))
    if pag:
        L.append(f"- **Commissione (DG ECFIN)**: la pagina dell'Italia elenca la procedura tra quelle *in corso* "
                 f"(«Ongoing procedure»: {'sì' if pag.get('procedura_in_corso') else 'no'}; pagina rivista il {pag.get('revisione') or 'n.d.'}). "
                 f"[Pagina]({pag.get('url')})")
    for f in csr.get("frasi_edp", [])[:3]:
        L.append(f"- Dalla raccomandazione del Consiglio del {it(csr.get('data', ''))}: «{f.strip()}»")
    if sem.get("edp_cronologia"):
        L += ["", "Cronologia della procedura in corso (DG ECFIN):", "", "| Data | Articolo | Passaggio |", "|---|---|---|"]
        L += [f"| {c['data']} | {c['articolo'] or '—'} | " + (f"[{c['passaggio']}]({c['url']})" if c["url"] else c["passaggio"]) + " |"
              for c in sem["edp_cronologia"]]
    L += ["", "## Percorso della spesa netta", ""]
    L += [f"- «{f.strip()}»" for f in csr.get("frasi_spesa_netta", [])[:4]] or ["- Nessuna frase sulla spesa netta estratta dal testo."]
    L += ["", f"## Raccomandazioni specifiche per l'Italia ({csr.get('data', '')[:4] or 'n.d.'})", ""]
    if csr.get("raccomandazioni"):
        L += [f"Fonte: [{csr['titolo']}]({csr['url']}) (CELEX {csr['celex']}). Testo integrale in `europa/archivio/{csr['testo']}`.", "",
              f"{csr.get('raccomandazioni_intro', '').strip()}", ""]
        L += [f"{i}. {r}" for i, r in enumerate(csr["raccomandazioni"], 1)]
    else:
        L += ["Testo della raccomandazione non disponibile in questa esecuzione."]
    L += ["", "## Scadenze del ciclo di bilancio europeo", "",
          "Scadenze ricorrenti fissate dai regolamenti (verificare sempre il testo vigente su EUR-Lex):", ""]
    prossime = []
    for mese, giorno, cosa, fonte in SCADENZE_CICLO:
        d = date(oggi.year, mese, giorno)
        if d < oggi:
            d = date(oggi.year + 1, mese, giorno)
        prossime.append((d, cosa, fonte))
    L += [f"- **{it(d.isoformat())}** — {cosa} ({fonte})" for d, cosa, fonte in sorted(prossime)]
    L += ["", "## Documenti del Semestre sull'Italia", "", "| Data | Documento | CELEX |", "|---|---|---|"]
    L += [f"| {it(d['data'])} | [{d['titolo'][:180]}]({d['url']}) | {d['celex']} |" for d in sem.get("documenti", [])]
    bil = [a for a in atti if a.get("impatto") == "vincolo di bilancio"]
    if bil:
        L += ["", "## Altri atti recenti con impatto sui conti pubblici (GU L)", ""] + [riga_atto(a) for a in bil[:15]]
    L += [""]
    return "\n".join(L)


# --- Funzioni per gli altri moduli ------------------------------------------------------------------------

def contesto_consiglio(aree: list[str] | None = None, limite: int = 8) -> dict:
    """Obblighi UE in scadenza, novità e infrazioni per le aree convocate (da mettere in contesto.json)."""
    st = leggi_json(QUI / "stato.json", {}) or {}
    aree = aree or list(ETICHETTE_AREE)
    tocca = lambda r: bool(set(lista_aree(r.get("aree"))) & set(aree))
    scad = [r for r in leggi_csv(QUI / "scadenze.csv") if tocca(r) and r["priorita"] in ("critica", "alta", "media")]
    inf = [r for r in leggi_csv(QUI / "infrazioni.csv") if tocca(r)]
    dal = (date.today() - timedelta(days=30)).isoformat()
    nov = [a for a in leggi_csv(ARCHIVIO / "atti.csv") if tocca(a) and a.get("data_gu", "") >= dal and a.get("rilevanza") == "alta"]
    campi_s = ["priorita", "celex", "titolo", "termine_recepimento", "stato", "infrazione", "aree", "proposte", "url_eurlex"]
    return {
        "aggiornato": st.get("aggiornato"), "aree": aree,
        "obblighi_in_scadenza": [{k: r[k] for k in campi_s} for r in scad[:limite]],
        "obblighi_totali": len(scad),
        "infrazioni": [{k: r[k] for k in ("numero", "oggetto", "fase", "aree", "proposte", "novita")} for r in inf[:limite]],
        "infrazioni_totali": len(inf),
        "novita_30_giorni": [{"celex": a["celex"], "tipo": a["tipo"], "titolo": titolo_breve(a["titolo"], 200), "impatto": a["impatto"],
                              "aree": a["aree"], "proposte": a["proposte"], "url": a["url_eurlex"]} for a in nov[:limite]],
        "semestre": st.get("semestre", {}),
        "esperto_europa_consigliato": bool(any(r["priorita"] == "critica" for r in scad) or inf),
    }


def odg_consiglio(aree: list[str] | None = None, limite: int = 6) -> list[str]:
    """Righe markdown per l'ordine del giorno di una seduta."""
    c = contesto_consiglio(aree, limite)
    L = ["## Vincoli e novità dall'Unione europea", "",
         f"Fonte: `europa/` (aggiornato al {it(c['aggiornato'] or '')}). Gli obblighi UE non si pesano: si rispettano, "
         "come la Costituzione e il vincolo di bilancio.", ""]
    L += ["**Obblighi di recepimento per le aree convocate** (priorità critica, alta e media):"]
    L += [f"- [{r['priorita']}] {r['celex']} — {titolo_breve(r['titolo'], 150)}: termine {it(r['termine_recepimento'])}, {r['stato']}"
          + (f" (procedura {r['infrazione']})" if r["infrazione"] else "") + (f"; proposte {r['proposte']}" if r["proposte"] else "")
          for r in c["obblighi_in_scadenza"]] or ["- nessuno"]
    if c["obblighi_totali"] > len(c["obblighi_in_scadenza"]):
        L += [f"- … altri {c['obblighi_totali'] - len(c['obblighi_in_scadenza'])} in `europa/scadenze.csv`."]
    L += ["", f"**Procedure d'infrazione nelle aree convocate:** {c['infrazioni_totali']}"]
    L += [f"- {r['numero']}: {r['oggetto'][:150]} — {r['fase']}" + (f" ({r['novita']})" if r["novita"] else "") for r in c["infrazioni"]]
    L += ["", "**Atti UE di rilevanza alta degli ultimi 30 giorni:**"]
    L += [f"- {a['tipo']} {a['celex']} ({a['impatto']}): {a['titolo']}" for a in c["novita_30_giorni"]] or ["- nessuno"]
    s = c.get("semestre") or {}
    if s:
        L += ["", f"**Semestre europeo:** {s.get('procedura_disavanzo', 'n.d.')}. Raccomandazioni {s.get('anno_raccomandazioni', '')}: "
              f"{s.get('numero_raccomandazioni', 0)} (testo in `europa/semestre.md`)."]
    return L


def dati_web() -> dict:
    """Dati compatti per il sito (docs/data.js)."""
    st = leggi_json(QUI / "stato.json", {}) or {}
    scad = leggi_csv(QUI / "scadenze.csv")
    campi = ["priorita", "celex", "tipo", "titolo", "termine_recepimento", "stato", "infrazione", "aree", "proposte", "url_eurlex"]
    return {"stato": st, "scadenze": [{k: r[k] for k in campi} for r in scad if r["priorita"] in ("critica", "alta", "media")],
            "infrazioni": [{k: r[k] for k in ("numero", "oggetto", "materia", "fase", "aree", "novita")}
                           for r in leggi_csv(QUI / "infrazioni.csv")],
            "novita_md": (QUI / "novita.md").read_text(encoding="utf-8") if (QUI / "novita.md").exists() else "",
            "semestre_md": (QUI / "semestre.md").read_text(encoding="utf-8") if (QUI / "semestre.md").exists() else ""}


# --- Principale -------------------------------------------------------------------------------------------

def genera() -> str:
    R = Regole()
    stato_arch = leggi_json(STATO_ARCHIVIO, {}) or {}
    atti = classifica_atti(R)
    prop = leggi_csv(ARCHIVIO / "proposte_ue.csv")
    for p in prop:
        p.update(R.valuta(p))
    inf = infrazioni(R, stato_arch)
    scad = scadenze(R, inf, atti)
    sem = leggi_json(ARCHIVIO / "semestre.json", {}) or {}

    scrivi_csv(QUI / "scadenze.csv", scad, CAMPI_SCAD)
    if inf:
        scrivi_csv(QUI / "infrazioni.csv", inf, CAMPI_INF)
    (QUI / "novita.md").write_text(novita_md(atti, prop, inf, scad, R, stato_arch), encoding="utf-8")
    (QUI / "semestre.md").write_text(semestre_md(sem, atti), encoding="utf-8")

    oggi = date.today()
    dal = (oggi - timedelta(days=R.finestre["novita_giorni"])).isoformat()
    dal_p = (oggi - timedelta(days=R.finestre["novita_giorni"])).isoformat()
    per_area = {}
    for area, nome in ETICHETTE_AREE.items():
        tocca = lambda r: area in lista_aree(r.get("aree"))
        rec = [a for a in atti if tocca(a) and a.get("data_gu", "") >= dal]
        sc = [s for s in scad if tocca(s)]
        per_area[area] = {
            "nome": nome,
            "novita_30g": len(rec), "novita_30g_alta": sum(1 for a in rec if a["rilevanza"] == "alta"),
            "obblighi_30g": sum(1 for a in rec if a["impatto"] == "obbligo"),
            "opportunita_30g": sum(1 for a in rec if a["impatto"] == "opportunità"),
            "vincoli_bilancio_30g": sum(1 for a in rec if a["impatto"] == "vincolo di bilancio"),
            "direttive_in_scadenza_12m": sum(1 for s in sc if 0 <= s["giorni_al_termine"] <= 365),
            "direttive_scadute_senza_misure": sum(1 for s in sc if s["stato"] == STATI["scaduto_senza_misure"]),
            "direttive_con_infrazione": sum(1 for s in sc if s["infrazione"]),
            "infrazioni_aperte": sum(1 for r in inf if tocca(r)),
            "proposte_ue_30g": sum(1 for p in prop if tocca(p) and p.get("data_atto", "") >= dal_p and p["rilevanza"] != "bassa"),
        }
    csr = sem.get("csr", {})
    frasi = " ".join(csr.get("frasi_edp", []))
    edp = ("sospesa (raccomandazione del Consiglio del " + it(csr.get("data", "")) + ")" if "è sospesa" in frasi else
           "in corso" if (sem.get("edp_pagina") or {}).get("procedura_in_corso") else "n.d.")
    stato = {
        "aggiornato": oggi.isoformat(),
        "fonti": stato_arch.get("fonti", {}), "ultima_esecuzione": stato_arch.get("ultima_esecuzione"),
        "archivio": {"atti_gu_l": len(atti), "dal": stato_arch.get("inizio"), "direttive_monitorate": len(leggi_csv(ARCHIVIO / "direttive.csv")),
                     "proposte_ue": len(prop), "testi": sum(1 for _ in (ARCHIVIO / "testi").rglob("*.txt")) if (ARCHIVIO / "testi").exists() else 0},
        "totali": {"novita_30g": sum(1 for a in atti if a.get("data_gu", "") >= dal),
                   "scadenze": len(scad), "scadenze_per_priorita": {v: sum(1 for s in scad if s["priorita"] == v) for v in PRIORITA.values()},
                   "infrazioni_aperte": len(inf), "infrazioni_mancato_recepimento": sum(1 for r in inf if r["mancato_recepimento"]),
                   "infrazioni_novita": sum(1 for r in inf if r["novita"])},
        "per_area": per_area,
        "semestre": {"procedura_disavanzo": f"procedura per disavanzo eccessivo {edp}",
                     "raccomandazione": csr.get("celex", ""), "anno_raccomandazioni": csr.get("data", "")[:4],
                     "numero_raccomandazioni": len(csr.get("raccomandazioni", []))},
        "scadenze_principali": [{k: s[k] for k in ("priorita", "celex", "titolo", "termine_recepimento", "stato", "infrazione", "aree", "proposte")}
                                for s in scad if s["_p"] <= 2][:10],
    }
    scrivi_json(QUI / "stato.json", stato)
    t = stato["totali"]
    return (f"europa: {len(atti)} atti GU L in archivio, {t['novita_30g']} negli ultimi 30 giorni; {len(scad)} direttive con termine "
            f"({t['scadenze_per_priorita']['critica']} critiche, {t['scadenze_per_priorita']['alta']} alte); "
            f"{len(inf)} infrazioni aperte; semestre: {stato['semestre']['procedura_disavanzo']}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    print(genera())
