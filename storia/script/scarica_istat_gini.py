"""Poverta' assoluta ed emigrazione di italiani (ISTAT, servizio SDMX) e Gini di lungo
periodo (OCSE, Income Distribution Database).

Uso:  python storia/script/scarica_istat_gini.py
(eseguire dopo scarica_eurostat.py: aggiorna emigrazione_cittadini con la serie ISTAT per l'Italia)
"""
from __future__ import annotations

import io

import pandas as pd

from comune import SERIE, salva, scarica

ISTAT = "https://esploradati.istat.it/SDMXWS/rest/data/IT1,"
H_ISTAT = {"Accept": "application/vnd.sdmx.data+csv;version=1.0.0"}


def istat(flusso: str, chiave: str, cache: str) -> pd.DataFrame:
    txt = scarica(f"{ISTAT}{flusso},1.0/{chiave}", cache, headers=H_ISTAT)
    return pd.read_csv(io.StringIO(txt))


def poverta():
    nuova = istat("34_727_DF_DCCV_POVERTA_1", "all", "istat_poverta_nuova.csv")
    vecchia = istat("34_728_DF_DCCV_POVERTA_BRKN1_7", "all", "istat_poverta_interrotta.csv")
    righe = []
    for df, fonte, filtro in [
        (vecchia, "ISTAT, serie interrotta 2005-2013 (non pienamente confrontabile con la nuova)", lambda a: a <= 2013),
        (nuova, "ISTAT, nuova serie dal 2014", lambda a: a >= 2014),
    ]:
        for area, nome in [("IT", "IT"), ("ITCD", "Nord"), ("ITE", "Centro"), ("ITFG", "Mezzogiorno")]:
            s = df[(df.REF_AREA == area) & (df.DATA_TYPE == "INCID_POVASS_INDIV")]
            for _, r in s.iterrows():
                if filtro(int(r.TIME_PERIOD)):
                    righe.append({"anno": int(r.TIME_PERIOD), "paese": nome, "valore": r.OBS_VALUE, "fonte": fonte})
    d = pd.DataFrame(righe)
    salva("poverta_assoluta", d,
          "Incidenza della poverta' assoluta individuale (% di persone in famiglie in poverta' assoluta); Italia, Nord, Centro, Mezzogiorno. Concetto solo italiano: non esiste un confronto internazionale omogeneo",
          "% persone", "ISTAT (dataflow 34_727 e 34_728)",
          "https://esploradati.istat.it/databrowser/#/it/dw/categories/IT1,Z0840HOU,1.0/HOU_POVERTY")


def emigrazione():
    d = istat("28_185_DF_DCIS_MIGRAZIONI_5", "A.IT..FREIGN.IT.9.TOTAL....", "istat_emigrati_cittadinanza.csv")
    if d.empty or "OBS_VALUE" not in d:
        raise RuntimeError("ISTAT: emigrati non disponibili")
    it = pd.DataFrame({"anno": d.TIME_PERIOD.astype(int), "paese": "IT",
                       "valore": d.OBS_VALUE / 1000,
                       "fonte": "ISTAT (cancellazioni anagrafiche per l'estero di cittadini italiani, dataflow 28_185)"})
    if "OBS_STATUS" in d:
        it.loc[d.OBS_STATUS.fillna("").astype(str).str.lower().eq("p").values, "fonte"] += " - dato provvisorio"
    it = it.groupby(["anno", "paese", "fonte"], as_index=False)["valore"].sum()
    f = SERIE / "emigrazione_cittadini.csv"
    altri = pd.read_csv(f)
    altri = altri[altri.paese != "IT"][["anno", "paese", "valore", "fonte"]]
    salva("emigrazione_cittadini", pd.concat([it, altri]),
          "Emigrati con la cittadinanza del paese verso l'estero (Italia: cittadini italiani cancellati dall'anagrafe per l'estero, ISTAT; altri paesi: Eurostat migr_emi1ctz), migliaia",
          "migliaia di persone", "ISTAT per l'Italia; Eurostat (migr_emi1ctz) per gli altri paesi",
          "https://esploradati.istat.it/ ; https://ec.europa.eu/eurostat/databrowser/view/migr_emi1ctz/default/table")


def gini_ocse():
    url = ("https://sdmx.oecd.org/public/rest/data/OECD.WISE.INE,DSD_WISE_IDD@DF_IDD,/"
           "ITA+FRA+DEU+ESP.A.INC_DISP_GINI.......")
    txt = scarica(url, "ocse_idd_gini.csv", headers={"Accept": "application/vnd.sdmx.data+csv"})
    d = pd.read_csv(io.StringIO(txt))
    d = d[(d.AGE == "_T") & (d.DEFINITION == "D_CUR")]
    d["paese"] = d.REF_AREA.map({"ITA": "IT", "FRA": "FR", "DEU": "DE", "ESP": "ES"})
    d["pref"] = (d.METHODOLOGY == "METH2012").astype(int)
    d = d.sort_values("pref").drop_duplicates(["paese", "TIME_PERIOD"], keep="last")
    d["fonte"] = d.METHODOLOGY.map({"METH2012": "OCSE IDD (definizione di reddito 2012)",
                                    "METH2011": "OCSE IDD (definizione precedente al 2012)"})
    out = pd.DataFrame({"anno": d.TIME_PERIOD, "paese": d.paese, "valore": d.OBS_VALUE * 100, "fonte": d.fonte})
    salva("gini_ocse", out,
          "Indice di Gini del reddito disponibile equivalente, OCSE Income Distribution Database (anni sparsi prima del 2003; anno = anno del reddito)",
          "indice 0-100", "OCSE, Income Distribution Database",
          "https://data-explorer.oecd.org/ (Income distribution database, DF_IDD)")


def main():
    poverta()
    emigrazione()
    try:
        gini_ocse()
    except RuntimeError as e:  # l'API OCSE limita il numero di richieste per ora
        print("  ATTENZIONE: Gini OCSE non scaricato (riprovare piu' tardi):", e)


if __name__ == "__main__":
    main()
