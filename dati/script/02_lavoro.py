"""Area 02 - Lavoro, Welfare, Famiglia, Disabilità, demografia.

Scarica le serie e i documenti di fonte primaria usati per verificare il dossier
ministeri/02_lavoro_welfare_famiglia.md (verifica: dati/verifiche/02_lavoro.md).

Uso:  python 02_lavoro.py      (dalla cartella dati/script)

Note tecniche
- Si preferisce Eurostat quando ripubblica dati ISTAT (più rapido dell'SDMX ISTAT).
- HICP: dal 2026 Eurostat ha congelato prc_hicp_midx (fermo a 2025-12) e pubblica
  i dati correnti in prc_hicp_minr (ECOICOP v2, dimensione `coicop18`).
- Le retribuzioni contrattuali reali sono un'elaborazione GovernAI: indice ISTAT
  delle retribuzioni contrattuali orarie (base dic. 2021=100, totale economia)
  deflazionato con l'HICP/IPCA Italia (Eurostat). Il metodo riproduce il -8,8% a
  settembre 2025 pubblicato da ISTAT.
- I documenti (PDF/XLSX) sono salvati in dati/raw/ con prefisso 02_.
"""
from __future__ import annotations

import pandas as pd

from fonti import RAW, eurostat, salva, scarica

AREA = "02"
UE = "EU27_2020"


def ok(msg):
    print(f"[ok] {msg}")


def ko(nome, e):
    print(f"[ERRORE] {nome}: {e}")


def es(nome, ds, since, nota="", **filtri):
    """Scarica un dataset Eurostat e lo salva come serie 02_<nome>."""
    try:
        df = eurostat(ds, since=since, **filtri)
        salva(df, f"02_{nome}", fonte=f"Eurostat {ds}", url=df.attrs["url"], nota=nota, area=AREA)
        ok(f"02_{nome} ({ds}, {len(df)} righe, agg. {df.attrs.get('aggiornato')})")
        return df
    except Exception as e:  # noqa: BLE001
        ko(nome, e)
        return None


# --- 1. Serie Eurostat ------------------------------------------------------

# B1 demografia: nati vivi, decessi, popolazione al 1° gennaio (ISTAT via Eurostat)
es("demografia_nati_decessi_pop", "demo_gind", "2015", geo="IT",
   indic_de=["LBIRTH", "DEATH", "JAN"], nota="LBIRTH=nati vivi; DEATH=decessi; JAN=pop. 1 gennaio")
# B1 fecondità totale (Eurostat arriva al 2024; 2025 da ISTAT Natalità e fecondità, ott. 2026)
es("fecondita_tft", "demo_find", "2015", geo=["IT", UE], indic_de="TOTFERRT")
# B1 indici di dipendenza proiettati (EUROPOP; base più recente disponibile)
for ds in ("proj_25ndbi", "proj_23ndbi"):
    d = es("dipendenza_proiezioni", ds, None, nota="OLDDEP1=65+/15-64; DEPRATIO1=(0-14+65+)/15-64",
           geo="IT", projection="BSL", indic_de=["OLDDEP1", "DEPRATIO1"],
           time=["2025", "2030", "2040", "2050", "2060", "2070"])
    if d is not None:
        break

# B2 working poor (in-work at-risk-of-poverty, 18+)
es("working_poor", "ilc_iw01", "2015", geo=["IT", UE], sex="T", age="Y_GE18")

# B3 tassi di occupazione annuali (LFS)
es("tasso_occupazione", "lfsi_emp_a", "2015", geo=["IT", UE], indic_em="EMP_LFS",
   sex=["T", "F"], age=["Y20-64", "Y15-64"], unit="PC_POP")
# B3 NEET 15-29 (nazionale e regionale; ITG1 = Sicilia)
es("neet_15_29", "edat_lfse_20", "2015", geo=["IT", UE], sex="T", age="Y15-29",
   wstatus="NEMP", training="NO_FE_NO_NFE", unit="PC")
es("neet_15_29_regioni", "edat_lfse_22", "2015", sex="T", age="Y15-29",
   wstatus="NEMP", training="NO_FE_NO_NFE", unit="PC", geo=["IT", "ITG1", "ITF3", "ITF6", "ITC4"])

# A budget: prestazioni sociali in denaro della PA (D62) e spesa COFOG protezione sociale
es("prestazioni_sociali_denaro", "gov_10a_main", "2015", geo=["IT", UE], unit=["MIO_EUR", "PC_GDP"],
   na_item="D62PAY", sector="S13", nota="D62 = prestazioni sociali diverse dai trasferimenti in natura")
es("spesa_protezione_sociale_cofog", "gov_10a_exp", "2015", geo=["IT", UE], unit=["MIO_EUR", "PC_GDP"],
   cofog99=["GF10", "GF1002"], na_item="TE", sector="S13", nota="GF10 protezione sociale; GF1002 vecchiaia")

# B6 divario occupazionale per disabilità (EU-SILC, 20-64)
es("divario_occupazione_disabilita", "tepsr_sp200", "2015", geo=["IT", UE],
   nota="Punti percentuali; SEV = limitazioni gravi")

# B2 prezzi: HICP Italia, indice 2015=100 (serie corrente)
hicp = es("hicp_it", "prc_hicp_minr", "2021-01", geo="IT", unit="I15", coicop18="TOTAL")


# --- 2. Documenti di fonte primaria (dati/raw) ------------------------------

DOCUMENTI = {
    "02_istat_natalita_fecondita_2025.pdf":
        "https://www.istat.it/wp-content/uploads/2026/10/Natalita-e-fecondita-popolazione-residente-2025.pdf",
    "02_istat_occupati_disoccupati_set2026.pdf":
        "https://www.istat.it/wp-content/uploads/2026/10/CS_Occupati-e-disoccupati_SETTEMBRE_2026.pdf",
    "02_istat_nidi_2026.pdf":
        "https://www.istat.it/wp-content/uploads/2026/02/REPORT_OFFERTA-DI-NIDI-E-SERVIZI-INTEGRATIVI-PER-LA-PRIMA-INFANZIA.pdf",
    "02_istat_previsioni_base2025.pdf":
        "https://www.istat.it/wp-content/uploads/2026/08/Previsioni-popolazione-residente-famiglie-forze-lavoro.pdf",
    "02_istat_retribuzioni_set2026.pdf":
        "https://www.istat.it/wp-content/uploads/2026/10/Comunicato-LUGLIO_SETTEMBRE-2026-retribuzioni.pdf",
    "02_istat_retribuzioni_serie_set2026.xlsx":
        "https://www.istat.it/wp-content/uploads/2026/10/Serie-storiche-SETTEMBRE-retribuzioni-2026.xlsx",
    "02_istat_poverta_2025.html":
        "https://www.istat.it/comunicato-stampa/la-poverta-in-italia-anno-2025/",
    "02_inps_adi_sfl_infografica_2026_07.pdf":
        "https://www.inps.it/content/dam/inps-site/pdf/dati-analisi-bilanci/osservatori-statistici/osservatorio-adi-sfl/Infografiche_ADI_SFL_2026_07.pdf",
    "02_rgs_tendenze_pensioni_2026.pdf":
        "https://www.rgs.mef.gov.it/_Documenti/VERSIONE-I/Attivit--i/Spesa-soci/Attivita_di_previsione_RGS/2026/Ltdmlpdspess-2026.pdf",
    "02_rgs_rapporto26_nda.pdf":
        "https://www.rgs.mef.gov.it/_Documenti/VERSIONE-I/Attivit--i/Spesa-soci/Attivita_di_previsione_RGS/2025/nda/Rapporto-2025-n26-NdA.pdf",
}

for nome, url in DOCUMENTI.items():
    try:
        p = scarica(url, nome)
        ok(f"raw/{nome} ({p.stat().st_size // 1024} KB)")
        if nome.endswith(".pdf"):
            try:  # estrazione testo per ricerca rapida delle cifre
                from pypdf import PdfReader
                testo = "\n".join((pg.extract_text() or "") for pg in PdfReader(p).pages)
                (RAW / nome.replace(".pdf", ".txt")).write_text(testo, encoding="utf-8")
            except Exception as e:  # noqa: BLE001
                print(f"    (testo non estratto: {e})")
    except Exception as e:  # noqa: BLE001
        ko(nome, e)


# --- 3. Serie ricavate da documenti ----------------------------------------

MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio",
        "agosto", "settembre", "ottobre", "novembre", "dicembre"]


def retribuzioni_mensili(xlsx) -> pd.DataFrame:
    """Indice mensile delle retribuzioni contrattuali orarie, totale economia (Tabella 1)."""
    t = pd.read_excel(xlsx, sheet_name="Tabella 1", header=None)
    righe, anno = [], None
    for _, r in t.iterrows():
        a, m, v = r[2], r[3], r[5]
        if pd.notna(a) and str(a).strip().isdigit():
            anno = int(str(a).strip())
        if isinstance(m, str) and m.strip().lower() in MESI and pd.notna(v):
            righe.append({"time": f"{anno}-{MESI.index(m.strip().lower()) + 1:02d}", "indice_retrib": float(v)})
    return pd.DataFrame(righe)


try:
    xlsx = RAW / "02_istat_retribuzioni_serie_set2026.xlsx"
    w = retribuzioni_mensili(xlsx)
    h = hicp[["time", "valore"]].rename(columns={"valore": "hicp_2015"})
    df = w.merge(h, on="time")
    b = df[df.time == "2021-01"].iloc[0]
    df["reale_vs_gen2021_pct"] = ((df.indice_retrib / b.indice_retrib) / (df.hicp_2015 / b.hicp_2015) - 1) * 100
    df["reale_vs_gen2021_pct"] = df["reale_vs_gen2021_pct"].round(1)
    salva(df, "02_retribuzioni_contrattuali_reali", fonte="ISTAT retribuzioni contrattuali (Tab. 1) + Eurostat prc_hicp_minr",
          url=DOCUMENTI["02_istat_retribuzioni_serie_set2026.xlsx"],
          nota="Elaborazione GovernAI: indice orario totale economia deflazionato con HICP IT; base gen. 2021", area=AREA)
    for t in ("2025-09", "2026-09"):
        s = df[df.time == t]
        if len(s):
            ok(f"retribuzioni contrattuali reali {t} vs gen. 2021: {s.reale_vs_gen2021_pct.item():+.1f}%")
except Exception as e:  # noqa: BLE001
    ko("retribuzioni_contrattuali_reali", e)

# Cifre puntuali tratte dai documenti ufficiali (non disponibili come serie API):
# tenute in un'unica tabella con fonte e pagina, così il dossier resta tracciabile.
PUNTUALI = [
    # dato, valore, unità, anno/periodo, fonte, url
    ("nati_2025", 355772, "n.", "2025", "ISTAT Natalità e fecondità 2025 (21/10/2026), p.1", DOCUMENTI["02_istat_natalita_fecondita_2025.pdf"]),
    ("fecondita_2025", 1.14, "figli per donna", "2025", "ISTAT Natalità e fecondità 2025, p.1", DOCUMENTI["02_istat_natalita_fecondita_2025.pdf"]),
    ("tasso_occupazione_15_64", 63.0, "%", "set-2026 (provv.)", "ISTAT Occupati e disoccupati set. 2026 (29/10/2026)", DOCUMENTI["02_istat_occupati_disoccupati_set2026.pdf"]),
    ("tasso_occupazione_femminile_15_64", 54.4, "%", "set-2026 (provv.)", "ISTAT Occupati e disoccupati set. 2026, prospetto 2", DOCUMENTI["02_istat_occupati_disoccupati_set2026.pdf"]),
    ("individui_poverta_assoluta", 5.4, "mln", "2025", "ISTAT La povertà in Italia 2025 (15/10/2026)", DOCUMENTI["02_istat_poverta_2025.html"]),
    ("incidenza_poverta_assoluta_individui", 9.3, "%", "2025", "ISTAT La povertà in Italia 2025", DOCUMENTI["02_istat_poverta_2025.html"]),
    ("famiglie_poverta_assoluta", 2.1, "mln", "2025", "ISTAT La povertà in Italia 2025", DOCUMENTI["02_istat_poverta_2025.html"]),
    ("incidenza_poverta_assoluta_famiglie", 8.0, "%", "2025", "ISTAT La povertà in Italia 2025", DOCUMENTI["02_istat_poverta_2025.html"]),
    ("minori_poverta_assoluta", 1.136, "mln", "2025", "ISTAT La povertà in Italia 2025", DOCUMENTI["02_istat_poverta_2025.html"]),
    ("incidenza_poverta_minori", 12.5, "%", "2025", "ISTAT La povertà in Italia 2025", DOCUMENTI["02_istat_poverta_2025.html"]),
    ("incidenza_poverta_famiglie_operaie", 14.3, "%", "2025", "ISTAT La povertà in Italia 2025", DOCUMENTI["02_istat_poverta_2025.html"]),
    ("incidenza_poverta_famiglie_soli_stranieri", 29.4, "%", "2025", "ISTAT La povertà in Italia 2025", DOCUMENTI["02_istat_poverta_2025.html"]),
    ("incidenza_poverta_famiglie_soli_italiani", 5.9, "%", "2025", "ISTAT La povertà in Italia 2025", DOCUMENTI["02_istat_poverta_2025.html"]),
    ("nidi_posti_per_100_bambini", 31.6, "%", "2023/24", "ISTAT Offerta di nidi (2/2/2026), p.1", DOCUMENTI["02_istat_nidi_2026.pdf"]),
    ("nidi_copertura_sud", 19.0, "%", "2023/24", "ISTAT Offerta di nidi, p.1 (Isole 19,5%)", DOCUMENTI["02_istat_nidi_2026.pdf"]),
    ("nidi_quota_con_lista_attesa", 59.5, "%", "2023/24", "ISTAT Offerta di nidi, p.1", DOCUMENTI["02_istat_nidi_2026.pdf"]),
    ("quota_65piu_2050", 34.5, "%", "2050", "ISTAT Previsioni base 1/1/2025 (31/8/2026), scenario mediano", DOCUMENTI["02_istat_previsioni_base2025.pdf"]),
    ("quota_15_64_2050", 55.3, "%", "2050", "ISTAT Previsioni base 1/1/2025, scenario mediano", DOCUMENTI["02_istat_previsioni_base2025.pdf"]),
    ("popolazione_2050", 55.0, "mln", "2050", "ISTAT Previsioni base 1/1/2025, scenario mediano", DOCUMENTI["02_istat_previsioni_base2025.pdf"]),
    ("spesa_pensioni_pil_2025", 15.2, "% PIL", "2025", "RGS Tendenze medio-lungo periodo, agg. 2026 (lug. 2026), Tab. D", DOCUMENTI["02_rgs_tendenze_pensioni_2026.pdf"]),
    ("spesa_pensioni_pil_picco", 17.1, "% PIL", "2041-2044", "RGS agg. 2026, scenario nazionale base", DOCUMENTI["02_rgs_tendenze_pensioni_2026.pdf"]),
    ("spesa_pensioni_pil_2050", 16.2, "% PIL", "2050", "RGS agg. 2026, scenario nazionale base", DOCUMENTI["02_rgs_tendenze_pensioni_2026.pdf"]),
    ("spesa_pensioni_pil_2070", 14.0, "% PIL", "2070", "RGS agg. 2026, scenario nazionale base", DOCUMENTI["02_rgs_tendenze_pensioni_2026.pdf"]),
    ("adi_nuclei_almeno_una_mensilita", 1018611, "n.", "gen-2024/giu-2026", "INPS Osservatorio ADI-SFL, infografica lug. 2026", DOCUMENTI["02_inps_adi_sfl_infografica_2026_07.pdf"]),
    ("adi_nuclei_giugno_2026", 690000, "n.", "giu-2026", "INPS Osservatorio ADI-SFL via Min. Lavoro (4/8/2026)", "https://lavoro.gov.it/adi/comunicazione/news/osservatorio-adi-e-sfl-i-dati-aggiornati-giugno-2026"),
    ("adi_importo_medio_giugno_2026", 672, "EUR/mese", "giu-2026", "INPS Osservatorio ADI-SFL via Min. Lavoro (4/8/2026)", "https://lavoro.gov.it/adi/comunicazione/news/osservatorio-adi-e-sfl-i-dati-aggiornati-giugno-2026"),
]
try:
    salva(pd.DataFrame(PUNTUALI, columns=["dato", "valore", "unita", "periodo", "fonte", "url"]),
          "02_cifre_puntuali_documenti", fonte="ISTAT, INPS, RGS (documenti ufficiali)",
          url="vedi colonna url", nota="Cifre lette dai documenti in dati/raw/02_*", area=AREA)
    ok("02_cifre_puntuali_documenti")
except Exception as e:  # noqa: BLE001
    ko("cifre_puntuali", e)

print("Fatto. Registro: dati/serie/_registro_02.csv")
