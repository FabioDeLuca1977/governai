"""Serie sociali, demografiche e territoriali da Eurostat (API JSON-stat).

Uso:  python storia/script/scarica_eurostat.py
"""
from __future__ import annotations

import pandas as pd

from comune import GEO_EUROSTAT, eurostat, salva

GEO = ["IT", "FR", "DE", "ES", "EA20", "EU27_2020"]
FE = "Eurostat"


def pag(ds: str) -> str:
    return f"https://ec.europa.eu/eurostat/databrowser/view/{ds}/default/table"


def prepara(df: pd.DataFrame, fonte: str) -> pd.DataFrame:
    df = df.rename(columns={"time": "anno"})
    df["paese"] = df["geo"].map(GEO_EUROSTAT)
    df = df.dropna(subset=["paese"])
    df["anno"] = df["anno"].astype(int)
    df["fonte"] = fonte
    return df[["anno", "paese", "valore", "fonte"]]


def serie(nome, ds, filtri, descr, unita, geo=GEO):
    f = dict(filtri)
    f["geo"] = geo
    df = prepara(eurostat(ds, f), f"{FE} ({ds})")
    salva(nome, df, descr, unita, f"{FE} ({ds})", pag(ds))
    return df


def main():
    # Fecondita', saldo migratorio, occupazione e disoccupazione giovanile sono in
    # scarica_ocse_bm.py (serie piu' lunghe da OCSE e Banca Mondiale).
    serie("gini_reddito_disponibile", "ilc_di12", {"age": "TOTAL", "statinfo": "GINI_HND"},
          "Indice di Gini del reddito disponibile equivalente (EU-SILC; anno = anno dell'indagine, redditi dell'anno precedente)",
          "indice 0-100")
    serie("rischio_poverta", "ilc_li02",
          {"rskpovth": "B_60", "statinfo": "MED_EI", "sex": "T", "age": "TOTAL", "unit": "PC"},
          "Rischio di poverta' relativa: persone con reddito sotto il 60% della mediana nazionale (per confronto con gli altri paesi)",
          "% popolazione")
    serie("laureati_25_34", "edat_lfse_03",
          {"sex": "T", "age": "Y25-34", "isced11": "ED5-8", "unit": "PC"},
          "Quota di persone 25-34 anni con istruzione terziaria (ISCED 5-8)", "% popolazione 25-34")
    # Qualita' del lavoro (indagine sulle forze di lavoro; nel 2021 nuovo regolamento europeo: piccola rottura di serie)
    serie("dipendenti_tempo_determinato", "lfsa_etgar",
          {"unit": "PC_SAL", "reason": "TOTAL", "sex": "T", "age": "Y15-64"},
          "Dipendenti con contratto a tempo determinato, % dei dipendenti 15-64 anni (indagine sulle forze di lavoro)",
          "% dipendenti 15-64", geo=["IT", "FR", "DE", "ES"])
    serie("part_time_involontario", "lfsa_eppgai",
          {"unit": "PC", "sex": "T", "age": "Y15-64"},
          "Part-time involontario: occupati a tempo parziale che vorrebbero un lavoro a tempo pieno, % degli occupati part-time 15-64",
          "% occupati part-time 15-64", geo=["IT", "FR", "DE", "ES"])
    serie("spesa_pensioni_pil", "gov_10a_exp",
          {"unit": "PC_GDP", "sector": "S13", "cofog99": "GF1002", "na_item": "TE"},
          "Spesa pubblica per vecchiaia (COFOG 10.2, prevalentemente pensioni), % del PIL", "% PIL")

    # Emigrazione di cittadini del paese (dal 2008 in Eurostat)
    f = {"citizen": "NAT", "age": "TOTAL", "agedef": "COMPLET", "sex": "T", "unit": "NR",
         "geo": ["IT", "FR", "DE", "ES"]}
    try:
        df = prepara(eurostat("migr_emi1ctz", f), f"{FE} (migr_emi1ctz)")
    except Exception:  # noqa: BLE001
        f.pop("agedef")
        df = prepara(eurostat("migr_emi1ctz", f), f"{FE} (migr_emi1ctz)")
    df["valore"] = df["valore"] / 1000
    salva("emigrazione_cittadini", df,
          "Emigrati con la cittadinanza del paese (per l'Italia: cittadini italiani cancellati per l'estero), migliaia",
          "migliaia di persone", f"{FE} (migr_emi1ctz)", pag("migr_emi1ctz"))

    # Divario Nord-Sud: PIL pro capite Mezzogiorno / Centro-Nord, 1995-ultimo anno.
    # PIL pro capite per ripartizione da ISTAT (conti territoriali, edizione dic. 2025);
    # il Centro-Nord si ricava da Italia e Mezzogiorno pesando con la popolazione
    # al 1 gennaio (Eurostat demo_r_d2jan): pc_CN = (pc_IT*P_IT - pc_M*P_M) / (P_IT - P_M).
    import io
    from comune import scarica
    url = ("https://esploradati.istat.it/SDMXWS/rest/data/IT1,93_1227_DF_DCCN_TNA1_6,1.0/"
           "A.IT+ITCD+ITE+ITFG.B1GQ_B_W2_S1_R_POP....V...2025M12")
    txt = scarica(url, "istat_pil_pc_ripartizioni.csv",
                  headers={"Accept": "application/vnd.sdmx.data+csv;version=1.0.0"})
    ist = pd.read_csv(io.StringIO(txt)).pivot_table(index="TIME_PERIOD", columns="REF_AREA", values="OBS_VALUE")
    pop = eurostat("demo_r_d2jan", {"sex": "T", "age": "TOTAL", "unit": "NR", "geo": ["IT", "ITF", "ITG"]})
    pop = pop.pivot(index="time", columns="geo", values="valore")
    pop.index = pop.index.astype(int)
    p_it, p_m = pop["IT"], pop["ITF"] + pop["ITG"]
    cn = (ist["IT"] * p_it - ist["ITFG"] * p_m) / (p_it - p_m)
    r = (ist["ITFG"] / cn * 100).dropna().reset_index()
    r.columns = ["anno", "valore"]
    r["paese"] = "IT"
    fonte_ns = "ISTAT (conti economici territoriali, dataflow 93_1227) e Eurostat (demo_r_d2jan) per i pesi di popolazione"
    salva("divario_nord_sud", r,
          "PIL pro capite del Mezzogiorno (Sud e Isole) in % di quello del Centro-Nord, prezzi correnti",
          "% Centro-Nord", fonte_ns, "https://esploradati.istat.it/ (Principali aggregati territoriali, valori pro capite)")
    lv = []
    for cod, nome in [("ITCD", "Nord"), ("ITE", "Centro"), ("ITFG", "Mezzogiorno")]:
        lv.append(pd.DataFrame({"anno": ist.index, "paese": nome, "valore": ist[cod].values}))
    lv.append(pd.DataFrame({"anno": cn.dropna().index, "paese": "Centro-Nord", "valore": cn.dropna().values}))
    salva("pil_pro_capite_macroaree", pd.concat(lv),
          "PIL pro capite a prezzi correnti per ripartizione (Centro-Nord calcolato con pesi di popolazione)",
          "euro correnti per abitante", fonte_ns, "https://esploradati.istat.it/")


if __name__ == "__main__":
    main()
