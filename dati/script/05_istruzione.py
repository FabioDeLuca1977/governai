"""GovernAI - Area 05 (Istruzione, Universita e Ricerca, Cultura, Sport e Giovani).

Script riproducibile di verifica dati del dossier ministeri/05_istruzione_ricerca_cultura.md.
Scarica le serie usate (Eurostat, che ripubblica i dati ISTAT LFS/R&S/COFOG) e i documenti
ufficiali in PDF (INVALSI, ISTAT, MIM, OCSE/INAPP), controlla che le cifre citate compaiano
nel testo del documento e salva tutto con salva(..., area="05").

Uso:  python 05_istruzione.py   (dalla cartella dati/script)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fonti import eurostat, salva, scarica  # noqa: E402

AREA = "05"
G = ["IT", "EU27_2020"]
UE27 = ["BE", "BG", "CZ", "DK", "DE", "EE", "IE", "EL", "ES", "FR", "HR", "IT", "CY", "LV", "LT", "LU", "HU",
        "MT", "NL", "AT", "PL", "PT", "RO", "SI", "SK", "FI", "SE"]


def es(nome, dataset, nota="", since=None, **filtri):
    df = eurostat(dataset, since=since, **filtri)
    salva(df, nome, fonte=f"Eurostat {dataset}", url=df.attrs["url"], nota=nota, area=AREA)
    print(f"[ok] {nome}: {len(df)} righe (agg. {df.attrs.get('aggiornato')})")
    return df


def v(df, **q):
    m = pd.Series(True, index=df.index)
    for k, x in q.items():
        m &= df[k].astype(str) == str(x)
    s = df.loc[m, "valore"]
    return s.iloc[0] if len(s) else None


# --- 1. Serie Eurostat -------------------------------------------------------
elet = es("05_elet_18_24_sesso", "edat_lfse_14", "ELET 18-24 (%), totale/maschi/femmine",
          since="2015", geo=G, sex=["T", "M", "F"], wstatus="POP", unit="PC")
elet_r = es("05_elet_18_24_nuts1", "edat_lfse_16", "ELET 18-24 per macro-area NUTS1 (ITC NO, ITH NE, ITI Centro, ITF Sud, ITG Isole)",
            since="2018", geo=["IT", "ITC", "ITH", "ITI", "ITF", "ITG"], sex="T", age="Y18-24", unit="PC")
neet = es("05_neet_15_29", "edat_lfse_20", "NEET 15-29 (%) per condizione: NEMP totale, UNE disoccupati, INAC inattivi, WANT vorrebbero lavorare",
          since="2015", sex="T", age="Y15-29", unit="PC")
laur = es("05_laureati_25_34", "edat_lfse_03", "Popolazione 25-34 con titolo terziario ISCED 5-8 (%)",
          since="2015", geo=G, sex="T", age="Y25-34", isced11="ED5-8", unit="PC")
adl = es("05_formazione_adulti_25_64", "trng_lfse_01", "Adulti 25-64 in istruzione/formazione nelle ultime 4 settimane (%)",
         since="2015", geo=G, sex="T", age="Y25-64", unit="PC")
adu = es("05_formazione_adulti_degurba", "trng_lfs_14", "Adulti 25-64 in formazione (4 settimane) per grado di urbanizzazione (DEG1 citta, DEG2 periferie/piccole citta, DEG3 rurale)",
         since="2023", geo=G, sex="T", age="Y25-64", unit="PC")
gerd = es("05_rs_gerd_settore", "rd_e_gerdtot", "Spesa R&S (GERD) per settore esecutore: TOTAL, BES imprese, GOV PA, HES universita, PNP non profit",
          since="2015", geo=G, sectperf=["TOTAL", "BES", "GOV", "HES", "PNP"], unit=["PC_GDP", "MIO_EUR"])
gfund = es("05_rs_gerd_finanziata_pa", "rd_e_gerdfund", "GERD finanziata dal settore pubblico (sectfund GOV), % PIL",
           since="2015", geo=G, sectfund="GOV", sectperf="TOTAL", unit="PC_GDP")
gbard = es("05_rs_gbard", "gba_nabsfin07", "Stanziamenti pubblici di bilancio per R&S (GBARD), % PIL",
           since="2015", geo=G, nabs07="TOTAL", unit="PC_GDP")
cofog = es("05_cofog_istruzione_cultura", "gov_10a_exp", "Spesa AP (S13) per funzione COFOG: GF09 istruzione, GF08 ricreazione-cultura-religione, GF0801 sport/ricreazione, GF0802 cultura",
           since="2015", geo=G, sector="S13", na_item="TE", cofog99=["TOTAL", "GF09", "GF08", "GF0801", "GF0802"], unit=["MIO_EUR", "PC_GDP", "PC_TOT"])
ai = es("05_imprese_ai", "isoc_eb_ai", "Imprese >=10 addetti che usano almeno una tecnologia di AI (%)",
        since="2021", geo=G, indic_is="E_AI_TANY", size_emp="GE10", unit="PC_ENT")
pop = es("05_pop_15_29_it", "demo_pjangroup", "Popolazione residente al 1 gennaio, classi 15-19, 20-24, 25-29 (per stimare il numero di NEET)",
         since="2024", geo="IT", sex="T", age=["Y15-19", "Y20-24", "Y25-29"], unit="NR")

# --- 2. Documenti ufficiali (PDF) e controllo delle cifre ---------------------
DOCS = {
    "05_invalsi_comunicato_2026.pdf": ("https://www.invalsi.it/wp-content/uploads/2026/07/COMUNICATO-STAMPA.pdf",
                                       ["8,7% nel 2025, il 6,3% nel 2026", "potrebbe scendere al 7,3% nel 2026",
                                        "II primaria: 67% nel 2025; 64% nel 2026", "V primaria: 75% nel 2025; 73% nel 2026"]),
    "05_istat_livelli_istruzione_2025.pdf": ("https://www.istat.it/wp-content/uploads/2026/11/Report_LivelliRitorniOccupazionali_Anno-2025.pdf",
                                             ["8,2% (-1,6 punti", "44,1%", "10,1% dei 18-24enni nel Mezzogiorno", "35,0% dei NEET"]),
    "05_istat_migrazioni_2024-2025.pdf": ("https://www.istat.it/wp-content/uploads/2026/08/Statistica-report_Migrazioni-interne-e-internazionali-della-popolazione-residente_ANNI-2024-2025.pdf",
                                          ["netta di 78mila giovani laureati italiani", "+88mila", "29,2%"]),
    "05_istat_fattori_rischio_2025.pdf": ("https://www.istat.it/wp-content/uploads/2026/04/Report_Fattori-di-rischio-per-la-salute-peso-sedentarieta-fumo-e-alcol_Anno-2025.pdf",
                                          ["30,8%", "-2,4 punti"]),
    "05_mim_focus_avvio_as2024-25.pdf": ("https://www.mim.gov.it/documents/20182/8426729/Principali+dati+della+scuola+-+Focus+avvio+anno+scolastico+2024-2025.pdf",
                                         ["7.473 Istituzioni scolastiche", "127 Centri"]),
    "05_piaac_country_note_italia.pdf": ("https://inapp.gov.it/wp-content/uploads/Non-organizzati/PIAAC_IIc_Country-note_EN.pdf",
                                         ["245 points in literacy", "244 points in numeracy", "231 points in adaptive problem solving",
                                          "35% of adults (OECD average: 26%)", "5% of adults (OECD average: 12%)"]),
}


def testo_pdf(p: Path) -> str:
    try:
        import pymupdf as fitz  # PyMuPDF
    except ImportError:
        import fitz
    with fitz.open(p) as d:
        t = "\n".join(pg.get_text() for pg in d)
    return re.sub(r"\s+", " ", t)


righe = []
for nome, (url, frasi) in DOCS.items():
    try:
        p = scarica(url, nome)
        t = testo_pdf(p)
        for f in frasi:
            ok = re.sub(r"\s+", " ", f) in t
            righe.append({"documento": nome, "url": url, "cifra_cercata": f, "trovata": ok})
            print(f"[{'ok' if ok else '!!'}] {nome}: {f}")
    except Exception as e:  # documento non raggiungibile: lo segnalo, non blocco lo script
        righe.append({"documento": nome, "url": url, "cifra_cercata": "(download fallito)", "trovata": False})
        print(f"[!!] {nome}: {e}")
chk = pd.DataFrame(righe)
salva(chk, "05_controllo_documenti", fonte="INVALSI, ISTAT, MIM, OCSE/INAPP (PDF ufficiali)",
      url="vedi colonna url", nota="Controllo testuale delle cifre citate nel dossier 05", area=AREA)

# --- 3. Riepilogo dei valori usati nel dossier --------------------------------
it_neet = neet[(neet.geo == "IT") & (neet.wstatus == "NEMP")].set_index("time")["valore"]
n25 = neet[(neet.time == "2025") & (neet.wstatus == "NEMP") & (neet.geo.isin(UE27))]
rank = n25.sort_values("valore", ascending=False).reset_index(drop=True)
pos_it = int(rank.index[rank.geo == "IT"][0]) + 1 if (rank.geo == "IT").any() else None
pop25 = pop[pop.time == "2025"]["valore"].sum()
neet_mln = pop25 * v(neet, geo="IT", time="2025", wstatus="NEMP") / 100 / 1e6
want = v(neet, geo="IT", time="2025", wstatus="WANT") / v(neet, geo="IT", time="2025", wstatus="NEMP")

riep = [
    ("ELET 18-24 IT 2025 (%)", v(elet, geo="IT", sex="T", time="2025")),
    ("ELET 18-24 UE27 2025 (%)", v(elet, geo="EU27_2020", sex="T", time="2025")),
    ("ELET maschi IT 2025", v(elet, geo="IT", sex="M", time="2025")),
    ("ELET femmine IT 2025", v(elet, geo="IT", sex="F", time="2025")),
    ("ELET Sud ITF 2025", v(elet_r, geo="ITF", time="2025")),
    ("ELET Isole ITG 2025", v(elet_r, geo="ITG", time="2025")),
    ("NEET 15-29 IT 2025 (%)", it_neet.get("2025")),
    ("NEET 15-29 IT 2015 (%)", it_neet.get("2015")),
    ("NEET 15-29 UE27 2025 (%)", v(neet, geo="EU27_2020", time="2025", wstatus="NEMP")),
    ("NEET IT 2025: posizione (1 = peggiore) nella UE27", pos_it),
    ("NEET IT 2025: numero stimato (mln, pop. 1/1/2025)", round(neet_mln, 2)),
    ("NEET IT 2025: quota che vorrebbe lavorare", round(want, 3)),
    ("Laureati 25-34 IT 2025 (%)", v(laur, geo="IT", time="2025")),
    ("Laureati 25-34 UE27 2025 (%)", v(laur, geo="EU27_2020", time="2025")),
    ("Formazione adulti 25-64 IT 2025 (%)", v(adl, geo="IT", time="2025")),
    ("Formazione adulti 25-64 UE27 2025 (%)", v(adl, geo="EU27_2020", time="2025")),
    ("Formazione adulti IT 2025 citta DEG1", v(adu, geo="IT", deg_urb="DEG1", time="2025")),
    ("Formazione adulti IT 2025 rurale DEG3", v(adu, geo="IT", deg_urb="DEG3", time="2025")),
    ("NEET UE27 2025: paesi con valore piu alto dell'Italia", ", ".join(f"{g} {x}" for g, x in rank.loc[rank.valore > it_neet.get("2025"), ["geo", "valore"]].values)),
    ("GERD IT 2024 (mln EUR)", v(gerd, geo="IT", sectperf="TOTAL", unit="MIO_EUR", time="2024")),
    ("GERD IT 2024 (% PIL)", v(gerd, geo="IT", sectperf="TOTAL", unit="PC_GDP", time="2024")),
    ("GERD IT 2025 (% PIL, prelim.)", v(gerd, geo="IT", sectperf="TOTAL", unit="PC_GDP", time="2025")),
    ("GERD UE27 2024 (% PIL)", v(gerd, geo="EU27_2020", sectperf="TOTAL", unit="PC_GDP", time="2024")),
    ("GERD eseguita da universita HES IT 2024 (% PIL)", v(gerd, geo="IT", sectperf="HES", unit="PC_GDP", time="2024")),
    ("GERD eseguita da universita HES UE 2024 (% PIL)", v(gerd, geo="EU27_2020", sectperf="HES", unit="PC_GDP", time="2024")),
    ("GERD eseguita da PA GOV IT 2024 (% PIL)", v(gerd, geo="IT", sectperf="GOV", unit="PC_GDP", time="2024")),
    ("GERD eseguita da PA GOV UE 2024 (% PIL)", v(gerd, geo="EU27_2020", sectperf="GOV", unit="PC_GDP", time="2024")),
    ("GERD finanziata dalla PA IT 2024 (% PIL)", v(gfund, geo="IT", time="2024")),
    ("GERD finanziata dalla PA UE27 2023 (% PIL)", v(gfund, geo="EU27_2020", time="2023")),
    ("GBARD IT 2024 (% PIL)", v(gbard, geo="IT", time="2024")),
    ("GBARD UE27 2024 (% PIL)", v(gbard, geo="EU27_2020", time="2024")),
    ("Spesa istruzione AP IT 2024 (mln EUR)", v(cofog, geo="IT", cofog99="GF09", unit="MIO_EUR", time="2024")),
    ("Spesa istruzione AP IT 2024 (% PIL)", v(cofog, geo="IT", cofog99="GF09", unit="PC_GDP", time="2024")),
    ("Spesa istruzione AP IT 2024 (% spesa tot.)", v(cofog, geo="IT", cofog99="GF09", unit="PC_TOT", time="2024")),
    ("Spesa istruzione AP UE27 2024 (% PIL)", v(cofog, geo="EU27_2020", cofog99="GF09", unit="PC_GDP", time="2024")),
    ("Spesa ricreazione-cultura-religione IT 2024 (mln EUR)", v(cofog, geo="IT", cofog99="GF08", unit="MIO_EUR", time="2024")),
    ("Spesa ricreazione-cultura-religione IT 2024 (% PIL)", v(cofog, geo="IT", cofog99="GF08", unit="PC_GDP", time="2024")),
    ("Spesa ricreazione-cultura-religione UE27 2024 (% PIL)", v(cofog, geo="EU27_2020", cofog99="GF08", unit="PC_GDP", time="2024")),
    ("di cui servizi ricreativi e sportivi IT 2024 (mln EUR)", v(cofog, geo="IT", cofog99="GF0801", unit="MIO_EUR", time="2024")),
    ("di cui servizi culturali IT 2024 (mln EUR)", v(cofog, geo="IT", cofog99="GF0802", unit="MIO_EUR", time="2024")),
    ("Imprese con AI IT 2024 (%)", v(ai, geo="IT", time="2024")),
    ("Imprese con AI UE27 2024 (%)", v(ai, geo="EU27_2020", time="2024")),
    ("Imprese con AI IT 2025 (%)", v(ai, geo="IT", time="2025")),
    ("Imprese con AI UE27 2025 (%)", v(ai, geo="EU27_2020", time="2025")),
]
r = pd.DataFrame(riep, columns=["indicatore", "valore"])
salva(r, "05_riepilogo_verifiche", fonte="Eurostat (varie serie, vedi registro 05)", url="vedi _registro_05.csv",
      nota="Valori chiave usati nella verifica del dossier 05", area=AREA)
print(r.to_string(index=False))
