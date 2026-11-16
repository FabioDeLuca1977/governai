"""Serie del lavoro (OCSE, indagini sulle forze di lavoro) e fecondita' (Banca Mondiale).
Per l'UE27 si aggiungono i dati Eurostat (dal 1995/2002), segnalati nella colonna fonte.

Uso:  python storia/script/scarica_ocse_bm.py
(eseguire dopo scarica_eurostat.py, che sovrascrive alcune serie con la sola versione Eurostat)
"""
from __future__ import annotations

import io
import json

import pandas as pd

from comune import eurostat, salva, scarica, GEO_EUROSTAT

OCSE_MAP = {"ITA": "IT", "FRA": "FR", "DEU": "DE", "ESP": "ES"}
OCSE_PAG = "https://data-explorer.oecd.org/ (Employment and unemployment by five-year age group and sex - indicators, DF_LFS_INDIC)"


def ocse_lfs(misura: str, sesso: str, eta: str, stato: str) -> pd.DataFrame:
    url = ("https://sdmx.oecd.org/public/rest/data/OECD.ELS.SAE,DSD_LFS@DF_LFS_INDIC,/"
           f"ITA+FRA+DEU+ESP.{misura}..{sesso}.{eta}.{stato}?startPeriod=1970")
    txt = scarica(url, f"ocse_lfs_{misura}_{sesso}_{eta}.csv",
                  headers={"Accept": "application/vnd.sdmx.data+csv"})
    d = pd.read_csv(io.StringIO(txt))
    d["paese"] = d.REF_AREA.map(OCSE_MAP)
    d = d.rename(columns={"TIME_PERIOD": "anno", "OBS_VALUE": "valore"})
    d["fonte"] = "OCSE, Labour Force Statistics (DF_LFS_INDIC)"
    d.loc[(d.paese == "DE") & (d.anno < 1991), "fonte"] += " - Germania Ovest prima del 1991"
    return d[["anno", "paese", "valore", "fonte"]]


def eurostat_ue(ds: str, filtri: dict) -> pd.DataFrame:
    f = dict(filtri)
    f["geo"] = ["EU27_2020", "EA20"]
    d = eurostat(ds, f).rename(columns={"time": "anno"})
    d["paese"] = d.geo.map(GEO_EUROSTAT)
    d["anno"] = d.anno.astype(int)
    d["fonte"] = f"Eurostat ({ds})"
    return d[["anno", "paese", "valore", "fonte"]]


def main():
    lfs = "lfsa_ergan"
    e = ocse_lfs("EMP_RATIO", "_T", "Y15T64", "EMP")
    e = pd.concat([e, eurostat_ue(lfs, {"sex": "T", "age": "Y15-64", "citizen": "TOTAL", "unit": "PC"})])
    salva("occupazione_15_64", e, "Tasso di occupazione 15-64 anni (indagini sulle forze di lavoro; OCSE per i paesi, Eurostat per UE/area euro)",
          "% popolazione 15-64", "OCSE LFS; Eurostat lfsa_ergan per UE27", OCSE_PAG)

    f = ocse_lfs("EMP_RATIO", "F", "Y15T64", "EMP")
    f = pd.concat([f, eurostat_ue(lfs, {"sex": "F", "age": "Y15-64", "citizen": "TOTAL", "unit": "PC"})])
    salva("occupazione_femminile_15_64", f, "Tasso di occupazione femminile 15-64 anni (OCSE per i paesi, Eurostat per UE/area euro)",
          "% donne 15-64", "OCSE LFS; Eurostat lfsa_ergan per UE27", OCSE_PAG)

    g = ocse_lfs("UNE_RATE", "_T", "Y15T24", "UNE")
    g = pd.concat([g, eurostat_ue("lfsa_urgan", {"sex": "T", "age": "Y15-24", "citizen": "TOTAL", "unit": "PC"})])
    salva("disoccupazione_giovanile", g, "Tasso di disoccupazione 15-24 anni (OCSE per i paesi, Eurostat per UE/area euro)",
          "% forza lavoro 15-24", "OCSE LFS; Eurostat lfsa_urgan per UE27", OCSE_PAG)

    # Fecondita': Banca Mondiale (serie omogenea dal 1960 per tutti e quattro i paesi)
    righe = []
    for cod, p in {"ITA": "IT", "FRA": "FR", "DEU": "DE", "ESP": "ES", "EMU": "EA", "EUU": "UE27"}.items():
        url = f"https://api.worldbank.org/v2/country/{cod}/indicator/SP.DYN.TFRT.IN?format=json&per_page=200"
        js = json.loads(scarica(url, f"bm_tfr_{cod}.json"))
        for r in js[1] or []:
            if r["value"] is not None:
                righe.append({"anno": int(r["date"]), "paese": p, "valore": r["value"],
                              "fonte": "Banca Mondiale (SP.DYN.TFRT.IN, da Eurostat e uffici statistici nazionali)"})
    salva("fecondita", pd.DataFrame(righe), "Tasso di fecondita' totale (figli per donna)", "figli per donna",
          "Banca Mondiale, World Development Indicators", "https://data.worldbank.org/indicator/SP.DYN.TFRT.IN")

    # Saldo migratorio: Eurostat, Francia metropolitana (FX) prima del 1998, Germania DE_TOT
    d = eurostat("demo_gind", {"indic_de": "CNMIGRATRT",
                               "geo": ["IT", "FR", "FX", "DE_TOT", "ES", "EA20", "EU27_2020"]})
    d = d.rename(columns={"time": "anno"})
    d["anno"] = d.anno.astype(int)
    d = d[~((d.geo == "FX") & (d.anno >= 1998))]
    d["paese"] = d.geo.map({**GEO_EUROSTAT, "FX": "FR", "DE_TOT": "DE"})
    d["fonte"] = "Eurostat (demo_gind)"
    d.loc[d.geo == "FX", "fonte"] = "Eurostat (demo_gind) - Francia metropolitana"
    salva("saldo_migratorio", d[["anno", "paese", "valore", "fonte"]],
          "Saldo migratorio (con aggiustamento statistico) per 1.000 abitanti; Francia metropolitana prima del 1998",
          "per 1.000 abitanti", "Eurostat (demo_gind)",
          "https://ec.europa.eu/eurostat/databrowser/view/demo_gind/default/table")


if __name__ == "__main__":
    main()
