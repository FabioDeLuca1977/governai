"""Area 07 (Giustizia, Interno/immigrazione, Difesa): verifica dati del dossier.

Scarica e salva (prefisso "07_") le serie usate in dati/verifiche/07_giustizia.md.
Esecuzione: python 07_giustizia.py   (dalla cartella dati/script)

Fonti:
- Eurostat: COFOG (gov_10a_exp), rimpatri (migr_eirtn), ordini di allontanamento (migr_eiord),
  domande d'asilo (migr_asyappctza), residenti per cittadinanza (migr_pop1ctz),
  occupati per cittadinanza (lfsa_egan).
- NATO: Defence Expenditure of NATO Countries (2014-2025), marzo 2026 (PDF testuale);
  Defence Investment of NATO Countries (2014-2026), luglio 2026 (PDF solo grafico: valori
  dell'Italia trascritti a mano dalle tabelle 1 e 3, vedi NATO_2026).
- Ministero dell'Interno, cruscotto statistico giornaliero 31/12/2025 e 30/9/2026.
- Ministero della Giustizia: Continuous Monitoring PNRR 2025; Relazione attuazione PNRR ago 2026;
  statistiche DAP detenuti presenti al 30/9/2026.
- ANBSC: Relazione sulla performance 2025 (giugno 2026).
- Governo/MEF: Relazione al Parlamento ex art. 6 L. 243/2012 (2 ottobre 2026), clausola nazionale.

Nota su fonti.py: scarica() usa lo User-Agent "GovernAI-ricerca/0.1"; alcuni siti istituzionali
(giustizia.it) rispondono in modo diverso a UA non da browser. Qui si usa un wrapper che ritenta
con UA da browser senza modificare fonti.py.
"""
from __future__ import annotations

import html
import re
import sys

import pandas as pd
import requests

from fonti import RAW, eurostat, salva, scarica

AREA = "07"
UA_BROWSER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}


def scarica_robusto(url: str, nome: str):
    """scarica() di fonti.py; se fallisce o restituisce HTML al posto di un PDF, ritenta con UA browser."""
    try:
        p = scarica(url, nome)
        if nome.endswith(".pdf") and not p.read_bytes()[:5].startswith(b"%PDF"):
            raise ValueError("non è un PDF")
        return p
    except Exception as e:  # noqa: BLE001
        print(f"  [scarica] ritento con UA browser ({e})")
        r = requests.get(url, headers=UA_BROWSER, timeout=120)
        r.raise_for_status()
        p = RAW / nome
        p.write_bytes(r.content)
        return p


def testo_pdf(path) -> str:
    import pypdf
    return "\n".join((pg.extract_text() or "") for pg in pypdf.PdfReader(str(path)).pages)


def num(s: str) -> float:
    return float(s.replace(".", "").replace(",", "."))


def log(msg: str):
    sys.stdout.buffer.write((msg + "\n").encode("utf-8", "replace"))


# --- 1. Eurostat --------------------------------------------------------------

EUROSTAT = [
    ("07_cofog_difesa_ordine_pubblico", "gov_10a_exp",
     dict(geo="IT", unit=["MIO_EUR", "PC_GDP"], sector="S13", na_item="TE",
          cofog99=["GF02", "GF0201", "GF03", "GF0301", "GF0303", "GF0304"]), "2015",
     "GF02 difesa, GF0201 difesa militare, GF03 ordine pubblico e sicurezza, GF0301 polizia, GF0303 tribunali, GF0304 carceri"),
    ("07_rimpatri_eurostat", "migr_eirtn",
     dict(geo=["IT", "EU27_2020"], citizen="TOTAL", age="TOTAL", sex="T", c_dest="TOTAL"), "2019",
     "Cittadini di paesi terzi effettivamente rimpatriati"),
    ("07_ordini_allontanamento_eurostat", "migr_eiord",
     dict(geo=["IT", "EU27_2020"], citizen="TOTAL", age="TOTAL", sex="T"), "2019",
     "Cittadini di paesi terzi destinatari di ordine di lasciare il territorio"),
    ("07_asilo_prime_domande", "migr_asyappctza",
     dict(geo=["IT", "EU27_2020"], citizen="TOTAL", age="TOTAL", sex="T", applicant="FRST"), "2019",
     "Richiedenti asilo per la prima volta"),
    ("07_residenti_per_cittadinanza", "migr_pop1ctz",
     dict(geo="IT", citizen=["TOTAL", "NAT", "EU27_2020_FOR", "NEU27_2020_FOR", "STLS"], age="TOTAL", sex="T"), "2019",
     "Popolazione al 1/1; stranieri = TOTAL - NAT"),
    ("07_occupati_per_cittadinanza", "lfsa_egan",
     dict(geo="IT", citizen=["TOTAL", "FOR"], age="Y15-74", sex="T"), "2019",
     "Occupati 15-74 anni (migliaia), RCFL ISTAT via Eurostat"),
]

log("== Eurostat")
ultimi = {}
for nome, ds, filtri, since, nota in EUROSTAT:
    df = eurostat(ds, since=since, **filtri)
    salva(df, nome, fonte=f"Eurostat {ds}", url=df.attrs["url"], nota=nota, area=AREA)
    ultimi[nome] = df
    log(f"  {nome}: {len(df)} righe, aggiornato {df.attrs.get('aggiornato')}")

cof = ultimi["07_cofog_difesa_ordine_pubblico"]
log(cof.pivot_table(index=["unit", "cofog99"], columns="time", values="valore").iloc[:, -3:].to_string())
rim, ordi = ultimi["07_rimpatri_eurostat"], ultimi["07_ordini_allontanamento_eurostat"]
for g in ["IT", "EU27_2020"]:
    r25 = rim[(rim.geo == g) & (rim.time == "2025")].valore.sum()
    o25 = ordi[(ordi.geo == g) & (ordi.time == "2025")].valore.sum()
    log(f"  rimpatri/ordini 2025 {g}: {r25:.0f}/{o25:.0f} = {r25 / o25:.1%}")
res = ultimi["07_residenti_per_cittadinanza"]
r25 = res[res.time == "2025"].set_index("citizen").valore
log(f"  stranieri 1/1/2025: {r25['TOTAL'] - r25['NAT']:.0f} = {(r25['TOTAL'] - r25['NAT']) / r25['TOTAL']:.2%}")
occ = ultimi["07_occupati_per_cittadinanza"]
o25 = occ[occ.time == "2025"].set_index("citizen").valore
log(f"  occupati stranieri 2025: {o25['FOR']:.0f} mila = {o25['FOR'] / o25['TOTAL']:.2%}")

# Costo medio per detenuto (ordine di grandezza): spesa COFOG carceri / presenze medie DAP
spesa_carceri_2024 = cof[(cof.unit == "MIO_EUR") & (cof.cofog99 == "GF0304") & (cof.time == "2024")].valore.item()
presenze_medie_2024 = (60166 + 61861) / 2  # DAP: detenuti presenti al 31/12/2023 e al 31/12/2024
log(f"  costo detenuto/giorno 2024 (COFOG GF0304 / presenze medie DAP): {spesa_carceri_2024 * 1e6 / presenze_medie_2024 / 365:.0f} EUR")

# --- 2. NATO -------------------------------------------------------------------

log("== NATO")
URL_NATO25 = "https://www.nato.int/content/dam/nato/webready/documents/finance/def-exp-2025-en.pdf"
URL_NATO26 = "https://www.nato.int/content/dam/nato/webready/documents/finance/def-exp-2026-en.pdf"
p25 = scarica_robusto(URL_NATO25, "07_nato_def_exp_2025.pdf")
scarica_robusto(URL_NATO26, "07_nato_def_exp_2026.pdf")

anni = list(range(2014, 2026))
righe = []
etichette = {6: "spesa_mln_eur_correnti", 8: "pct_pil"}
import pypdf  # noqa: E402

reader = pypdf.PdfReader(str(p25))
for pagina, var in etichette.items():
    riga = [ln for ln in reader.pages[pagina].extract_text().splitlines() if ln.startswith("Italy")][0]
    valori = [float(x.replace(",", "")) for x in riga.split()[-12:]]
    righe += [{"rapporto": "NATO 2014-2025 (mar 2026)", "variabile": var, "anno": a, "valore": v}
              for a, v in zip(anni, valori)]

# Rapporto luglio 2026 (PDF senza testo): valori Italia trascritti da Tab. 1 (core defence, mln EUR
# correnti) e Tab. 3 (core defence in % del PIL reale, prezzi 2021). Cut-off dati 3/7/2026.
NATO_2026 = {
    "spesa_mln_eur_correnti": {2024: 33402, 2025: 47183, 2026: 48310},
    "pct_pil": {2024: 1.52, 2025: 2.09, 2026: 2.10},
}
for var, d in NATO_2026.items():
    righe += [{"rapporto": "NATO 2014-2026 (lug 2026)", "variabile": var, "anno": a, "valore": v} for a, v in d.items()]
nato = pd.DataFrame(righe)
salva(nato, "07_nato_spesa_difesa_italia", fonte="NATO, Defence Expenditure/Investment of NATO Countries 2014-2025 e 2014-2026",
      url=f"{URL_NATO25} ; {URL_NATO26}",
      nota="2025-2026 stime NATO; valori 2026 trascritti a mano (PDF senza livello testo)", area=AREA)
log(nato.pivot_table(index=["rapporto", "variabile"], columns="anno", values="valore").iloc[:, -4:].to_string())

# Traiettoria programmata: Relazione al Parlamento 2/10/2026 (clausola nazionale di salvaguardia)
URL_REL = "https://www.qualenergia.it/wp-content/uploads/2026/10/Relazione-P.pdf"  # copia del documento MEF
try:
    t = testo_pdf(scarica_robusto(URL_REL, "07_relazione_parlamento_clausola_2026.pdf"))
    m = re.search(r"difesa, previsto fino a un massimo dello\s+([\d,]+) per cento del PIL", t.replace("\n", " "))
    log(f"  clausola difesa: fino a {m.group(1) if m else '?'}% PIL per il 2027 e il 2028")
except Exception as e:  # noqa: BLE001
    log(f"  Relazione al Parlamento non scaricata: {e}")
traiettoria = pd.DataFrame([
    {"anno": 2025, "pct_pil_core": 2.09, "tipo": "stima NATO lug 2026"},
    {"anno": 2026, "pct_pil_core": 2.10, "tipo": "stima NATO lug 2026"},
    {"anno": 2027, "pct_pil_core": None, "tipo": "programmato: fino a +0,3 pp PIL via clausola nazionale (Relazione al Parlamento 2/10/2026)"},
    {"anno": 2028, "pct_pil_core": None, "tipo": "programmato: fino a +0,3 pp PIL via clausola nazionale (Relazione al Parlamento 2/10/2026)"},
    {"anno": 2035, "pct_pil_core": 3.5, "tipo": "impegno NATO L'Aia 2025 (core), + 1,5% sicurezza/resilienza"},
])
salva(traiettoria, "07_difesa_traiettoria_programmata", fonte="NATO; Governo, Relazione al Parlamento ex art. 6 L. 243/2012 (2/10/2026)",
      url=URL_REL, nota="Valori 2027-2028 espressi come incremento massimo autorizzabile, non come livello", area=AREA)

# --- 3. Ministero dell'Interno: sbarchi -----------------------------------------

log("== Sbarchi (cruscotto Viminale)")
URL_CR25 = "https://www.immigrazione.it/docs/2026/cruscotto-statistico-giornaliero-31-dicembre-2025.pdf"
URL_CR26 = "https://www.immigrazione.it/docs/2026/cruscotto-statistico-giornaliero-30-settembre-2026.pdf"
t25 = testo_pdf(scarica_robusto(URL_CR25, "07_viminale_cruscotto_31dic2025.pdf"))
t26 = testo_pdf(scarica_robusto(URL_CR26, "07_viminale_cruscotto_30set2026.pdf"))
mesi = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto",
        "settembre", "ottobre", "novembre", "dicembre"]
righe = []
for anno in ("2024", "2025", "2026"):
    cand = re.findall(rf"^{anno} ((?:[\d.]+ ?)+)$", t26, re.M)
    vals = [num(x) for x in max(cand, key=lambda c: len(c.split())).split()]  # riga della tabella mensile
    righe += [{"anno": int(anno), "mese": mesi[i], "sbarchi": v} for i, v in enumerate(vals)]
sb = pd.DataFrame(righe)
msna = re.search(r"Anno 2025: ([\d.]+)", t25)
tot25_provv = re.search(r"TOTALE [\d.]+ [\d.]+ ([\d.]+)", t25)
log(f"  2025 consolidato (somma mensile, cruscotto 30/9/2026): {sb[sb.anno == 2025].sbarchi.sum():.0f}; "
    f"provvisorio al 31/12/2025: {tot25_provv.group(1) if tot25_provv else '?'}; MSNA 2025: {msna.group(1) if msna else '?'}")
cum = sb[sb.mese.isin(mesi[:9])].groupby("anno").sbarchi.sum()
log(f"  gen-set: {cum.to_dict()}")
salva(sb, "07_sbarchi_mensili", fonte="Ministero dell'Interno - Dip. PS, cruscotto statistico giornaliero 30/9/2026",
      url=URL_CR26, nota="Dati suscettibili di consolidamento; copia del PDF ufficiale su immigrazione.it", area=AREA)
acc = re.search(r"Totale complessivo ([\d.]+) ([\d.]+) ([\d.]+) ([\d.]+)", t26)
if acc:
    log(f"  migranti in accoglienza al 30/9/2026: {acc.group(4)}")

# --- 4. Ministero della Giustizia: disposition time, arretrato, detenuti --------

log("== Giustizia")
URL_REL_GIU = "https://www.giustizia.it/cmsresources/cms/documents/pnrr_relazione_su_attuazione_interventi_ago2026.pdf"
URL_CM25 = "https://datiestatistiche.giustizia.it/cmsresources/cms/documents/2025_Continuous_Monitoring_PNRR.pdf"
scarica_robusto(URL_CM25, "07_giustizia_continuous_monitoring_2025.pdf")
tg = testo_pdf(scarica_robusto(URL_REL_GIU, "07_giustizia_pnrr_relazione_ago2026.pdf"))
righe = []
sez = tg[tg.find("Tempi di trattazione"):]
for m in re.finditer(r"^(Baseline 2019|20\d\d|I semestre 2026)\s+([\d.]+)\s+(?:([+-][\d,]+)%\s+)?([\d.]+)", sez, re.M):
    righe.append({"periodo": m.group(1), "dt_civile_gg": num(m.group(2)), "dt_penale_gg": num(m.group(4))})
dt = pd.DataFrame(righe).drop_duplicates("periodo")
base = dt[dt.periodo == "Baseline 2019"].iloc[0]
dt["var_civile_pct"] = (dt.dt_civile_gg / base.dt_civile_gg - 1) * 100
dt["var_penale_pct"] = (dt.dt_penale_gg / base.dt_penale_gg - 1) * 100
log(dt.round(1).to_string(index=False))
salva(dt, "07_disposition_time_pnrr", fonte="Ministero della Giustizia, Relazione su attuazione interventi PNRR (agosto 2026)",
      url=URL_REL_GIU, nota="DT complessivo = somma dei tre gradi; target PNRR -40% civile, -25% penale entro 30/6/2026", area=AREA)
pend = re.search(r"I semestre 2026 ([\d.]+) (-[\d,]+)% ([\d.]+) (-[\d,]+)%", tg)
if pend:
    log(f"  pendenze civili iscritte fino al 2022, I sem 2026: Tribunali {pend.group(1)} ({pend.group(2)}%), Corti d'appello {pend.group(3)} ({pend.group(4)}%)")

URL_DAP = "https://www.giustizia.it/giustizia/en/mg_1_14_1.page?contentId=SST1522518"
r = requests.get(URL_DAP, headers=UA_BROWSER, timeout=60)
(RAW / "07_dap_detenuti_30set2026.html").write_bytes(r.content)
t = re.sub(r"<script.*?</script>|<style.*?</style>", "", r.text, flags=re.S)
t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))
m = re.search(r"Totale (\d+) ([\d.]+) ([\d.]+) ([\d.]+) ([\d.]+)", t)
det = pd.DataFrame([{"data": "2026-09-30", "istituti": int(m.group(1)), "capienza_regolamentare": num(m.group(2)),
                     "presenti": num(m.group(3)), "donne": num(m.group(4)), "stranieri": num(m.group(5))}])
det["affollamento_regolamentare_pct"] = det.presenti / det.capienza_regolamentare * 100
log(det.round(1).to_string(index=False))
salva(det, "07_detenuti_dap", fonte="Ministero della Giustizia - DAP, Detenuti presenti al 30/9/2026", url=URL_DAP,
      nota="Capienza regolamentare (9 mq + 5 mq); non tiene conto dei posti inagibili", area=AREA)

# --- 5. ANBSC: beni confiscati ----------------------------------------------------

log("== ANBSC")
URL_ANBSC = ("https://benisequestraticonfiscati.it/wp-content/uploads/2026/06/"
             "ANBSC-2026-0053431-Allegato-Relazione-performance-anno-2025-uv-226_Firmato.pdf")
ta = re.sub(r"\s+", " ", testo_pdf(scarica_robusto(URL_ANBSC, "07_anbsc_relazione_performance_2025.pdf")))
dest = re.search(r"complessivamente destinati ([\d.]+) beni, di cui ([\d.]+)\s*terreni", ta)
gest = re.search(r"31 dicembre 2025\s+risultavano complessivamente in gestione\s+([\d.]+) beni, di cui ([\d.]+)\s*terreni", ta)
dest25 = re.search(r"Nel corso del 2025 sono stati complessivamente destinati ([\d.]+) beni", ta)
opz = re.search(r"al ([\d,]+)% del 2025\)", ta)
aziende = re.search(r"incluso\s+([\d.]+) realtà aziendali", ta)
anbsc = pd.DataFrame([
    {"indicatore": "immobili destinati (cumulato al 31/12/2025)", "valore": num(dest.group(1))},
    {"indicatore": "  di cui terreni", "valore": num(dest.group(2))},
    {"indicatore": "immobili in gestione ANBSC al 31/12/2025", "valore": num(gest.group(1))},
    {"indicatore": "  di cui terreni", "valore": num(gest.group(2))},
    {"indicatore": "immobili destinati nel 2025", "valore": num(dest25.group(1))},
    {"indicatore": "beni opzionati / proposti nel 2025 (%)", "valore": num(opz.group(1)) if opz else None},
    {"indicatore": "realtà aziendali nel portafoglio della Direzione aziende (2025)", "valore": num(aziende.group(1)) if aziende else None},
])
tot = anbsc.valore[0] + anbsc.valore[2]
log(anbsc.to_string(index=False))
log(f"  totale immobili (destinati + in gestione): {tot:.0f}; quota destinati {anbsc.valore[0] / tot:.1%}")
salva(anbsc, "07_anbsc_beni_confiscati", fonte="ANBSC, Relazione sulla performance anno 2025 (giugno 2026)", url=URL_ANBSC,
      nota="Valori estratti dal testo del PDF", area=AREA)

log("Fatto.")
