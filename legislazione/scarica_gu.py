"""Archivio incrementale degli atti pubblicati nella Gazzetta Ufficiale, Serie generale.

Fonti (scelte dopo averle provate l'8/11/2026; dettagli e limiti in README.md):
  1. gazzettaufficiale.it, archivio per anno -> sommario di ogni fascicolo (anche i supplementi ordinari):
     elenco COMPLETO degli atti (leggi, decreti, delibere, comunicati...), con rubrica, emettitore,
     intestazione, titolo, pagina, codice redazionale.
  2. gazzettaufficiale.it, pagine dell'atto (testo originario, articolo per articolo): testo integrale.
  3. Normattiva, API open data (ricerca avanzata per data di pubblicazione): controllo incrociato degli
     atti normativi numerati e recupero di quelli eventualmente mancanti nei sommari.

L'archivio vive in legislazione/archivio/:
  indice.csv          una riga per atto (chiave: codice redazionale, es. 26G00223)
  testi/AAAA/<codice>.txt   testo dell'atto come pubblicato (originario), quando ottenuto
  stato.json          fascicoli già elaborati ed esito dell'ultima esecuzione

Uso:
  python scarica_gu.py                    # aggiorna: fascicoli nuovi (prima volta: ultimi 30 giorni)
  python scarica_gu.py --giorni 90        # allarga la finestra iniziale
  python scarica_gu.py --dal 2026-01-01   # da una data precisa
  python scarica_gu.py --testi normativi  # testi solo degli atti normativi (più veloce); default: tutti
  python scarica_gu.py --riprova-testi    # riprova i testi non ottenuti in passato
  python scarica_gu.py --senza-testi      # solo indice
"""
from __future__ import annotations

import argparse
import csv
import html
import json
import re
import sys
from datetime import date, datetime, timedelta

sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))  # anche con python -I
from norme import (ARCHIVIO, GU, INDICE, NORMATTIVA, NORMATTIVA_API, STATO, TESTI, Cortese, Riferimento,
                   data_da_intestazione, url_normattiva)

CAMPI = ["codice", "data_gu", "numero_gu", "supplemento", "rubrica", "emettitore", "tipo", "intestazione",
         "data_atto", "numero_atto", "titolo", "pagina", "url_gu", "eli_gu", "url_normattiva", "entrata_in_vigore",
         "testo", "testo_stato", "caratteri", "fonte", "scaricato"]
MAX_ELEMENTI = 400  # oltre questo numero di articoli/allegati il testo è salvato come "parziale"


# --- Classificazione del tipo di atto -------------------------------------------------------

def classifica(intestazione: str, emettitore: str, rubrica: str) -> str:
    i = intestazione.upper()
    e = emettitore.upper()
    regole = [
        (r"^TESTO COORDINATO", "testo coordinato"),
        (r"^LEGGE COSTITUZIONALE", "legge costituzionale"),
        (r"^LEGGE\b", "legge"),
        (r"^DECRETO-LEGGE|^DECRETO LEGGE", "decreto-legge"),
        (r"^DECRETO LEGISLATIVO", "decreto legislativo"),
        (r"^DECRETO DEL PRESIDENTE DELLA REPUBBLICA", "DPR"),
        (r"^DECRETO DEL PRESIDENTE DEL CONSIGLIO", "DPCM"),
        (r"^DELIBERA DEL CONSIGLIO DEI MINISTRI|^DELIBERAZIONE DEL CONSIGLIO DEI MINISTRI", "delibera CdM"),
        (r"^ORDINANZA", "ordinanza"),
        (r"^DELIBERA|^DELIBERAZIONE", "delibera"),
        (r"^DETERMINA|^DETERMINAZIONE", "determina"),
        (r"^PROVVEDIMENTO", "provvedimento"),
        (r"^COMUNICATO|^AVVISO|^ERRATA-CORRIGE|^RETTIFICA", "comunicato"),
        (r"^SENTENZA|^ORDINANZA DELLA CORTE", "sentenza"),
        (r"^REGOLAMENTO", "regolamento"),
        (r"^CIRCOLARE", "circolare"),
        (r"^ACCORDO|^INTESA", "accordo/intesa"),
    ]
    for pat, t in regole:
        if re.search(pat, i):
            return t
    if i.startswith("DECRETO"):
        if e.startswith("MINISTERO") or e.startswith("MINISTRO"):
            return "DM" if "DECRETO" in i and not re.search(r"DIRETTORIALE|DIRIGENZIALE", i) else "decreto dirigenziale"
        if "PRESIDENZA DEL CONSIGLIO" in e:
            return "decreto PCM"
        if "LEGGI ED ALTRI ATTI NORMATIVI" in rubrica.upper() or "SUPPLEMENT" in rubrica.upper():
            return "decreto (regolamento)"
        return "decreto"
    return "altro"


# --- Pagine della Gazzetta ------------------------------------------------------------------

def pulisci(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def fascicoli_anno(rete: Cortese, anno: int) -> list[tuple[str, int]]:
    t = rete.get(f"{GU}/ricercaArchivioCompleto/serie_generale/{anno}").text
    out = re.findall(r"caricaDettaglio\?dataPubblicazioneGazzetta=(\d{4}-\d{2}-\d{2})&(?:amp;)?numeroGazzetta=(\d+)", t)
    return sorted({(d, int(n)) for d, n in out})


RE_ATTO = re.compile(
    r'<a href="(?P<href>/atto/serie_generale/caricaDettaglioAtto/originario\?atto\.dataPubblicazioneGazzetta='
    r'(?P<data>[\d-]+)&(?:amp;)?atto\.codiceRedazionale=(?P<cod>\w+)[^"]*)">\s*<span class="data">(?P<int>.*?)</span>'
    r'\s*</a>\s*<a href="[^"]*">(?P<tit>.*?)</a>', re.S)
RE_SEGNO = re.compile(r'<span class="(?P<cl>rubrica|emettitore)">(?P<v>.*?)</span>', re.S)


def leggi_sommario(rete: Cortese, data_gu: str, numero: int) -> list[dict]:
    url = f"{GU}/gazzetta/serie_generale/caricaDettaglio?dataPubblicazioneGazzetta={data_gu}&numeroGazzetta={numero}"
    t = rete.get(url).text
    eventi = [(m.start(), "segno", m) for m in RE_SEGNO.finditer(t)] + [(m.start(), "atto", m) for m in RE_ATTO.finditer(t)]
    rubrica = emettitore = ""
    atti = []
    for _, k, m in sorted(eventi, key=lambda x: x[0]):
        if k == "segno":
            if m["cl"] == "rubrica":
                rubrica, emettitore = pulisci(m["v"]), ""
            else:
                emettitore = pulisci(m["v"])
            continue
        blocco = m["tit"]
        pag = re.search(r'<span class="pagina">(.*?)</span>', blocco, re.S)
        rif = re.search(r'<span class="riferimento">(.*?)</span>', blocco, re.S)
        titolo = pulisci(re.sub(r"<span.*?</span>", " ", blocco, flags=re.S))
        titolo = re.sub(r"\s*\(\w{8,9}\)\s*$", "", titolo)  # toglie il codice redazionale in coda
        sup = re.search(r"Suppl\.\s*(\w+)\s*n\.\s*(\d+)", pulisci(rif.group(1)) if rif else "")
        intest = pulisci(m["int"])
        dt = data_da_intestazione(intest)
        num = re.search(r"\bn\.\s*(\d+(?:/\w+)?)", intest)
        cod, dpub = m["cod"], m["data"]
        a, me, g = dpub.split("-")
        atti.append({
            "codice": cod, "data_gu": dpub, "numero_gu": numero,
            "supplemento": f"S.{sup.group(1)[0].upper()}. n. {sup.group(2)}" if sup else "",
            "rubrica": rubrica, "emettitore": emettitore, "tipo": classifica(intest, emettitore, rubrica),
            "intestazione": intest, "data_atto": dt.isoformat() if dt else "", "numero_atto": num.group(1) if num else "",
            "titolo": titolo, "pagina": pulisci(pag.group(1)).replace("Pag. ", "") if pag else "",
            "url_gu": GU + html.unescape(m["href"]).replace("&elenco30giorni=false", ""),
            "eli_gu": f"{GU}/eli/id/{a}/{me}/{g}/{cod}/sg",
            "url_normattiva": "", "entrata_in_vigore": "", "testo": "", "testo_stato": "da_scaricare", "caratteri": 0,
            "fonte": "GU sommario", "scaricato": date.today().isoformat(),
        })
    return atti


def html_a_testo(t: str) -> str:
    t = re.sub(r"<(script|style)\b.*?</\1>", "", t, flags=re.S | re.I)
    i = t.lower().find("<body")
    t = t[i:] if i >= 0 else t
    t = re.sub(r"<br\s*/?>|</p>|</div>|</h\d>|</li>|</tr>", "\n", t, flags=re.I)
    t = html.unescape(re.sub(r"<[^>]+>", "", t)).replace("\xa0", " ")
    righe = [re.sub(r"[ \t]+", " ", r).strip() for r in t.splitlines()]
    out, vuote = [], 0
    for r in righe:
        vuote = vuote + 1 if not r else 0
        if vuote <= 1:
            out.append(r)
    return "\n".join(out).strip()


def scarica_testo(rete: Cortese, atto: dict) -> tuple[str, str, str]:
    """Restituisce (testo, stato, entrata_in_vigore). Il sito richiede di aprire prima la pagina dell'atto
    (sessione), poi carica il testo per parti: premessa e primo articolo, quindi ogni articolo o allegato."""
    pag = rete.get(atto["url_gu"]).text
    if "Pagina non trovata" in pag:
        return "", "assente", ""
    eiv = re.search(r"Entrata in vigore del provvedimento:\s*([\d/]+)", pag)
    eiv = datetime.strptime(eiv.group(1), "%d/%m/%Y").date().isoformat() if eiv else ""
    src = [html.unescape(s) for s in re.findall(r'src="(/atto/[^"]+)"', pag)]
    default = next((s for s in src if "caricaArticoloDefault" in s), None)
    albero = next((s for s in src if "caricaAlberoArticoli" in s), None)
    if not default:
        return "", "assente", eiv
    parti = [html_a_testo(rete.get(GU + default).text)]
    stato = "ok"
    if albero:
        elementi = list(dict.fromkeys(html.unescape(h) for h in
                                      re.findall(r'href="(/atto/serie_generale/caricaArticolo\?[^"]+)"',
                                                 rete.get(GU + albero.split("#")[0]).text)))
        if len(elementi) > MAX_ELEMENTI:
            elementi, stato = elementi[:MAX_ELEMENTI], "parziale"
        visto = re.sub(r"\s+", " ", parti[0])
        doppi = 0
        for h in elementi:
            p = html_a_testo(rete.get(GU + h.split("#")[0]).text)
            norm = re.sub(r"\s+", " ", p)
            if norm and norm not in visto:  # il primo articolo è già nella pagina predefinita
                parti.append(p)
                visto += norm
                doppi = 0
            else:
                doppi += 1
                if doppi >= 10:  # elementi che ripetono testo già letto: inutile continuare a interrogare il sito
                    stato = "parziale" if len(elementi) > 20 else stato
                    break
    testo = "\n\n".join(x for x in parti if x)
    if "Pagina non trovata" in testo or len(testo) < 40:
        return "", "assente", eiv
    return testo, stato, eiv


# --- Normattiva (API open data) --------------------------------------------------------------

def atti_normattiva(rete: Cortese, dal: str, al: str) -> list[dict]:
    """Atti normativi numerati pubblicati in GU tra due date, secondo l'API open data di Normattiva."""
    out, pagina = [], 1
    while True:
        p = {"dataInizioPubProvvedimento": dal, "dataFinePubProvvedimento": al, "orderType": "recente",
             "paginazione": {"paginaCorrente": pagina, "numeroElementiPerPagina": 100}}
        j = rete.post(f"{NORMATTIVA_API}/ricerca/avanzata", json=p, headers={"Accept": "application/json"}).json()
        out += j.get("listaAtti") or []
        if pagina >= int(j.get("numeroPagine") or 1):
            return out
        pagina += 1


def url_normattiva_atto(data_gu: str, codice: str) -> str:
    return f"{NORMATTIVA}/atto/caricaDettaglioAtto?atto.dataPubblicazioneGazzetta={data_gu}&atto.codiceRedazionale={codice}"


TIPO_RIF = {"legge": "legge", "decreto-legge": "decreto-legge", "decreto legislativo": "decreto legislativo",
            "DPR": "decreto del Presidente della Repubblica", "legge costituzionale": "legge costituzionale"}


def link_normattiva(a: dict) -> str:
    """URN risolvibile per i tipi principali; altrimenti la pagina Normattiva per codice redazionale."""
    if a["tipo"] in TIPO_RIF and a["numero_atto"] and a["data_atto"]:
        d = date.fromisoformat(a["data_atto"])
        return url_normattiva(Riferimento(TIPO_RIF[a["tipo"]], a["numero_atto"], d.year, d))
    return url_normattiva_atto(a["data_gu"], a["codice"])


# --- Archivio ------------------------------------------------------------------------------

def leggi_indice() -> dict[str, dict]:
    if not INDICE.exists():
        return {}
    with INDICE.open(encoding="utf-8", newline="") as f:
        return {r["codice"]: r for r in csv.DictReader(f)}


def scrivi_indice(atti: dict[str, dict]) -> None:
    ARCHIVIO.mkdir(parents=True, exist_ok=True)
    righe = sorted(atti.values(), key=lambda r: (r["data_gu"], int(r["numero_gu"] or 0), r["codice"]), reverse=True)
    tmp = INDICE.with_suffix(".tmp")
    with tmp.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPI, extrasaction="ignore")
        w.writeheader()
        w.writerows(righe)
    tmp.replace(INDICE)


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--giorni", type=int, default=30, help="finestra della prima esecuzione (default 30)")
    ap.add_argument("--dal", help="data iniziale AAAA-MM-GG (ignora lo stato)")
    ap.add_argument("--testi", choices=["tutti", "normativi"], default="tutti",
                    help="normativi = solo leggi, decreti-legge, d.lgs., DPR e regolamenti (rubrica atti normativi)")
    ap.add_argument("--senza-testi", action="store_true")
    ap.add_argument("--riprova-testi", action="store_true")
    ap.add_argument("--max-testi", type=int, default=0, help="limite di testi da scaricare in questa esecuzione (0 = nessuno)")
    ap.add_argument("--pausa", type=float, default=1.0, help="secondi tra due richieste (minimo 0,5)")
    a = ap.parse_args()

    rete = Cortese(max(a.pausa, 0.5))
    stato = json.loads(STATO.read_text(encoding="utf-8")) if STATO.exists() else {}
    fatti = set(stato.get("fascicoli", []))
    atti = leggi_indice()
    oggi = date.today()
    inizio = date.fromisoformat(a.dal) if a.dal else (
        date.fromisoformat(stato["inizio"]) if stato.get("inizio") else oggi - timedelta(days=a.giorni))
    errori: list[str] = []

    # 1. fascicoli nuovi dai sommari della Gazzetta
    nuovi_fascicoli = []
    for anno in range(inizio.year, oggi.year + 1):
        try:
            for d, n in fascicoli_anno(rete, anno):
                if d >= inizio.isoformat() and f"{d}#{n}" not in fatti:
                    nuovi_fascicoli.append((d, n))
        except Exception as e:
            errori.append(f"archivio {anno}: {e}")
    nuovi_atti = 0
    for d, n in sorted(nuovi_fascicoli):
        try:
            for x in leggi_sommario(rete, d, n):
                if x["codice"] not in atti:
                    nuovi_atti += 1
                    x["url_normattiva"] = link_normattiva(x) if x["codice"][2:3] == "G" else ""
                    atti[x["codice"]] = x
            fatti.add(f"{d}#{n}")
        except Exception as e:
            errori.append(f"GU {n} del {d}: {e}")
    print(f"fascicoli nuovi: {len(nuovi_fascicoli)}; atti nuovi nell'indice: {nuovi_atti}")
    scrivi_indice(atti)

    # 2. controllo incrociato con Normattiva (atti normativi numerati)
    mancanti = 0
    try:
        for n in atti_normattiva(rete, inizio.isoformat(), oggi.isoformat()):
            cod = n["codiceRedazionale"]
            if cod in atti:
                atti[cod]["fonte"] = "GU sommario + Normattiva"
                continue
            mancanti += 1
            dt = (n.get("dataEmanazione") or "")[:10]
            intest = n.get("descrizioneAtto") or ""
            x = {k: "" for k in CAMPI}
            x.update(codice=cod, data_gu=n["dataGU"], numero_gu=n["numeroGU"],
                     supplemento="" if n.get("tipoSupplemento") in (None, "NO") else f"S.O. n. {n.get('numeroSupplemento')}",
                     rubrica="LEGGI ED ALTRI ATTI NORMATIVI", emettitore="", intestazione=intest,
                     tipo=classifica(intest, "", "LEGGI ED ALTRI ATTI NORMATIVI"), data_atto=dt,
                     numero_atto=n.get("numeroProvvedimento") or "",
                     titolo=re.sub(r"\s+", " ", (n.get("titoloAtto") or "").strip("[] ")).strip(),
                     url_gu=f"{GU}/atto/serie_generale/caricaDettaglioAtto/originario?atto.dataPubblicazioneGazzetta="
                            f"{n['dataGU']}&atto.codiceRedazionale={cod}",
                     eli_gu=f"{GU}/eli/id/{n['dataGU'].replace('-', '/')}/{cod}/sg", testo_stato="da_scaricare",
                     caratteri=0, fonte="Normattiva API", scaricato=oggi.isoformat())
            x["titolo"] = re.sub(r"\s*\(\w{8,9}\)\s*$", "", x["titolo"])
            x["url_normattiva"] = link_normattiva(x)
            atti[cod] = x
    except Exception as e:
        errori.append(f"Normattiva API: {e}")
    print(f"controllo Normattiva: {mancanti} atti normativi aggiunti perché assenti dai sommari")
    scrivi_indice(atti)

    # 3. testi
    scaricati = 0
    if not a.senza_testi:
        da_fare = [x for x in atti.values() if x["testo_stato"] == "da_scaricare"
                   or (a.riprova_testi and x["testo_stato"] in ("assente", "errore"))]
        if a.testi == "normativi":
            da_fare = [x for x in da_fare if x["codice"][2:3] == "G"]
        da_fare.sort(key=lambda x: (x["codice"][2:3] != "G", x["data_gu"]))  # prima gli atti normativi
        if a.max_testi:
            da_fare = da_fare[:a.max_testi]
        print(f"testi da scaricare: {len(da_fare)} (circa {len(da_fare) * 3 * rete.pausa / 60:.0f} minuti)")
        for i, x in enumerate(da_fare, 1):
            try:
                testo, st, eiv = scarica_testo(rete, x)
            except Exception as e:
                testo, st, eiv = "", "errore", ""
                errori.append(f"testo {x['codice']}: {e.__class__.__name__}")
            x["testo_stato"], x["entrata_in_vigore"] = st, eiv or x.get("entrata_in_vigore", "")
            if testo:
                dest = TESTI / x["data_gu"][:4] / f"{x['codice']}.txt"
                dest.parent.mkdir(parents=True, exist_ok=True)
                intest = f"{x['intestazione']}\n{x['titolo']}\n(GU Serie Generale n. {x['numero_gu']} del {x['data_gu']}" \
                         f"{', ' + x['supplemento'] if x['supplemento'] else ''}; {x['eli_gu']})\n\n"
                dest.write_text(intest + testo, encoding="utf-8")
                x["testo"], x["caratteri"] = dest.relative_to(ARCHIVIO).as_posix(), len(testo)
                scaricati += 1
            if i % 25 == 0:
                scrivi_indice(atti)
                print(f"  {i}/{len(da_fare)} testi")
    scrivi_indice(atti)

    tot = len(atti)
    con_testo = sum(1 for x in atti.values() if x["testo_stato"] in ("ok", "parziale"))
    stato.update(inizio=inizio.isoformat(), fascicoli=sorted(fatti), ultima_esecuzione=datetime.now().isoformat(timespec="seconds"),
                 ultima={"fascicoli_nuovi": len(nuovi_fascicoli), "atti_nuovi": nuovi_atti, "da_normattiva": mancanti,
                         "testi_scaricati": scaricati, "richieste": rete.richieste, "errori": errori[:50]},
                 totale_atti=tot, atti_con_testo=con_testo)
    STATO.write_text(json.dumps(stato, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"archivio GU: {tot} atti, {con_testo} con testo; nuovi {nuovi_atti}; testi scaricati {scaricati}; "
          f"richieste {rete.richieste}; errori {len(errori)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
