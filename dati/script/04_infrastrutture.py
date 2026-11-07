"""Area 04 - Infrastrutture, Trasporti, Casa, Affari regionali, Sud, Coesione, PNRR.

Scarica le serie usate per verificare il dossier ministeri/04_infrastrutture_territori.md
e le salva in dati/serie/04_*.csv con registro in _registro_04.csv.
Verifica: dati/verifiche/04_infrastrutture.md

Uso (dalla cartella dati/script):  python 04_infrastrutture.py
"""
from __future__ import annotations

import re

import pandas as pd
import requests

from fonti import HEADERS, RAW, eurostat, salva, scarica

AREA = "04"


def es(nome, ds, nota="", **kw):
    df = eurostat(ds, **kw)
    salva(df, nome, fonte=f"Eurostat {ds}", url=df.attrs["url"], nota=nota, area=AREA)
    return df


def ultimo(df, **filtri):
    d = df
    for k, v in filtri.items():
        d = d[d[k] == v]
    r = d.sort_values("time").iloc[-1]
    return r["time"], r["valore"]


# --- B3 Mobilità -------------------------------------------------------------
auto = es("04_auto_per_1000_abitanti", "road_eqs_carhab", since="2015",
          nota="Autovetture ogni 1.000 abitanti, tutti i paesi")
for g in ["IT", "EU27_2020"]:
    print("auto/1000", g, ultimo(auto, geo=g))

es("04_parco_auto_per_alimentazione", "road_eqs_carpda", since="2020", geo="IT", unit="NR",
   nota="Parco autovetture per alimentazione (PET/DIE includono ibridi; *_X_HYB esclusi ibridi)")

gge = es("04_emissioni_gas_serra_trasporti", "env_air_gge", since="1990", geo="IT", unit="MIO_T",
         airpol="GHG", src_crf=["TOTX4_MEMO", "CRF1A3", "CRF1A3B"],
         nota="TOTX4_MEMO=totale nazionale escl. LULUCF; CRF1A3=trasporti; CRF1A3B=trasporto stradale (inventario UNFCCC/ISPRA)")
p = gge.pivot_table(index="time", columns="src_crf", values="valore")
for anno in ["1990", "2024"]:
    print(f"trasporti {anno}: {p.loc[anno,'CRF1A3']/p.loc[anno,'TOTX4_MEMO']:.1%}  stradale {p.loc[anno,'CRF1A3B']/p.loc[anno,'TOTX4_MEMO']:.1%}")
print(f"stradale 1990-2024: {p.loc['2024','CRF1A3B']/p.loc['1990','CRF1A3B']-1:+.1%}; totale {p.loc['2024','TOTX4_MEMO']/p.loc['1990','TOTX4_MEMO']-1:+.1%}")

# --- B4 Casa -----------------------------------------------------------------
ov = es("04_sovraccarico_costo_abitativo_per_titolo", "ilc_lvho07c", since="2015",
        geo=["IT", "EU27_2020", "DE", "FR", "ES", "PL", "NL"],
        nota="Housing cost overburden rate (>40% reddito disponibile) per titolo di godimento, EU-SILC")
print("overburden RENT_MKT IT", ultimo(ov, geo="IT", tenure="RENT_MKT"))

hpi = es("04_prezzi_abitazioni_indice", "prc_hpi_a", since="2010", geo="IT", purchase="TOTAL", unit="I15_A_AVG",
         nota="House price index, 2015=100 (ISTAT IPAB)")
aff = es("04_affitti_hicp_indice", "prc_hicp_aind", since="2010", geo="IT", coicop="CP041", unit="INX_A_AVG",
         nota="HICP affitti effettivi (CP041), 2015=100; include contratti in essere, sottostima i nuovi canoni")
h = hpi.set_index("time")["valore"]; a = aff.set_index("time")["valore"]
print(f"2010-2024: affitti {a['2024']/a['2010']-1:+.1%}, prezzi case {h['2024']/h['2010']-1:+.1%}")

# --- B2 Coesione: dotazioni (OpenCoesione) e attuazione (Commissione UE) -----
URL_OC = "https://opencoesione.gov.it/media/opendata/Dotazioni_2021-2027_SIE.xlsx"
x = pd.read_excel(scarica(URL_OC, "04_oc_dotazioni_2021_2027_SIE.xlsx"), sheet_name="Dotazioni")
dot = x.groupby("AMBITO")[["RISORSE", "RISORSE_UE"]].sum().reset_index()
dot.loc[len(dot)] = ["TOTALE", dot.RISORSE.sum(), dot.RISORSE_UE.sum()]
salva(dot, "04_coesione_dotazioni_2021_2027", fonte="PCM-OpenCoesione, Dotazioni programmi 2021-2027 SIE",
      url=URL_OC, nota="Euro; FESR+FSE++JTF, UE + cofinanziamento nazionale", area=AREA)
print("dotazione 2021-27 (mld):", round(dot.iloc[-1].RISORSE / 1e9, 2))

URL_CD = "https://cohesiondata.ec.europa.eu/resource/3git-md5z.json"
params = {"$select": "tod_cycle,fund,sum(total_amount) as dotazione,sum(totalspendeligibleexpenditure_declared) as spesa_dichiarata,"
                     "sum(total_eligiblecost_of_selectedoperations) as costo_operazioni_selezionate",
          "$where": "ms='IT' AND dimension_type='Intervention Field'", "$group": "tod_cycle,fund", "$limit": 1000}
r = requests.get(URL_CD, params=params, headers=HEADERS, timeout=120); r.raise_for_status()
att = pd.DataFrame(r.json())
for c in ["dotazione", "spesa_dichiarata", "costo_operazioni_selezionate"]:
    att[c] = pd.to_numeric(att[c])
salva(att, "04_coesione_attuazione_2021_2027", fonte="Commissione europea, Cohesion Open Data, 2021-2027 Finances Detailed Planned vs Implemented",
      url=r.url, nota="Euro; cumulato per ciclo di trasmissione (tod_cycle); NON sommare cicli", area=AREA)
sie = att[att.fund.isin(["ERDF", "ESF+", "JTF"])].groupby("tod_cycle")[["dotazione", "spesa_dichiarata"]].sum()
sie["quota"] = sie.spesa_dichiarata / sie.dotazione
print((sie / [1e9, 1e9, 1]).round(3).tail(4))

# --- B1 PNRR: cifre dalla Relazione della Corte dei conti (Doc. XIII-bis n. 7) -
URL_CDC = "https://documenti.camera.it/_dati/leg19/lavori/documentiparlamentari/indiceetesti/013bis/007_RS/INTERO_COM.pdf"


def testo_pdf(path):
    import pymupdf  # PyMuPDF
    with pymupdf.open(path) as d:
        return [pg.get_text().replace("\n", " ") for pg in d]


pag = testo_pdf(scarica(URL_CDC, "04_cdc_relazione_pnrr_mag2026.pdf"))
CIFRE_CDC = [  # (dato, valore, unità, frase di controllo nel PDF)
    ("Spesa sostenuta PNRR fine febbraio 2026", 113.5, "mld EUR", "la soglia di 113,5 miliardi"),
    ("Spesa sostenuta / risorse del Piano", 58, "%", "oltre il 58 per cento"),
    ("Spesa sostenuta agosto 2025", 83, "mld EUR", "83 miliardi il valore ad agosto 2025"),
    ("Spesa prevista oltre il 2026", 24.2, "mld EUR", "circa 24,2 miliardi"),
    ("Misure con spesa oltre il 2026", 66, "n.", "circa 66  misure"),
    ("Importi rendicontati marzo 2026", 20.5, "mld EUR", "20,5 miliardi rendicontati"),
    ("Valore totale del Piano", 194.43, "mld EUR", "194,43 miliardi"),
]
righe = []
for dato, v, u, frase in CIFRE_CDC:
    pagine = [i + 1 for i, t in enumerate(pag) if re.sub(r"\s+", " ", frase) in re.sub(r"\s+", " ", t)]
    righe.append({"dato": dato, "valore": v, "unita": u, "pagine_pdf": ",".join(map(str, pagine[:3])), "trovato": bool(pagine)})
cdc = pd.DataFrame(righe)
salva(cdc, "04_pnrr_corte_conti_mag2026", fonte="Corte dei conti, Relazione sullo stato di attuazione del PNRR (dati al 31.3.2026), Doc. XIII-bis n. 7",
      url=URL_CDC, nota="Cifre estratte dal PDF; colonna 'trovato' = frase verificata nel testo", area=AREA)
print(cdc.to_string(index=False))

# Decima rata (Italia Domani, news 7.10.2026): valori dalla pagina ufficiale
URL_ID = "https://www.italiadomani.gov.it/content/sogei-ng/it/it/news/presentata-alla-commissione-eu-richiesta-pagamento-10a-e-ultima-.html"
rata = pd.DataFrame([{"dato": "Richiesta decima rata (29.9.2026)", "valore": 28.4, "unita": "mld EUR"},
                     {"dato": "Obiettivi della decima rata", "valore": 156, "unita": "n."},
                     {"dato": "Obiettivi totali del Piano", "valore": 576, "unita": "n."}])
salva(rata, "04_pnrr_decima_rata", fonte="Italia Domani (PCM), news 7.10.2026", url=URL_ID,
      nota="Valori trascritti dalla pagina ufficiale", area=AREA)

# --- B5 Demografia: ISTAT, Previsioni della popolazione base 1.1.2025 --------
URL_PREV = "https://www.istat.it/wp-content/uploads/2026/08/Previsioni-popolazione-residente-famiglie-forze-lavoro.pdf"
t = " ".join(testo_pdf(scarica(URL_PREV, "04_istat_previsioni_ago2026.pdf")))
t = re.sub(r"\s+", " ", t)
PREV = [
    ("Popolazione Italia", "2025", 58.9, "da 58,9 milioni di residenti al 1° gennaio 2025"),
    ("Popolazione Italia", "2050", 55.0, "55,0 milioni nel 2050"),
    ("Popolazione Italia", "2080", 45.8, "45,8 milioni nel 2080"),
    ("Aree interne Italia", "2025", 13.3, "contro 13,3 milioni nelle aree interne"),
    ("Aree interne Italia", "2050", 11.8, "le aree interne scendono a 11,8 milioni"),
    ("Aree interne Mezzogiorno", "2025", 7.1, "le prime contano 7,1 milioni di residenti"),
    ("Aree interne Mezzogiorno", "2050", 6.0, "fino a 6,0 milioni nel 2050"),
    ("Aree interne Nord, variazione 2025-2050", "2050", -0.122, "il Nord ne perde circa 122mila"),
]
prev = pd.DataFrame([{"aggregato": a, "anno": y, "milioni": v, "trovato": f in t} for a, y, v, f in PREV])
salva(prev, "04_istat_previsioni_aree_interne", fonte="ISTAT, Previsioni della popolazione residente, base 1.1.2025 (agosto 2026)",
      url=URL_PREV, nota="Scenario mediano; classificazione SNAI 2021-27; cifre estratte dal PDF", area=AREA)
print(prev.to_string(index=False))
