"""Costruisce le serie dati/serie/obi_*.csv usate da apprendimento/obiettivi.yaml.

Due tipi di serie:
- scaricate da Eurostat (fonti.eurostat) e trasformate nel KPI della scheda;
- derivate da serie già presenti in dati/serie (rapporti e quote), così il KPI
  è una sola colonna `valore` per anno e il confronto con la base è diretto.
Ogni serie è registrata in dati/serie/_registro_obi.csv tramite fonti.salva(area="obi").

Uso:  python -I apprendimento/aggiorna_obi.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "dati" / "script"))
from fonti import SERIE, eurostat, salva  # noqa: E402


def _leggi(nome: str) -> pd.DataFrame:
    return pd.read_csv(SERIE / f"{nome}.csv")


def presenze_lug_ago() -> None:
    """01-P6-a: quota di presenze (notti) in luglio e agosto sul totale annuo; solo anni completi."""
    df = eurostat("tour_occ_nim", since="2015-01", geo="IT", c_resid="TOTAL", unit="NR", nace_r2="I551-I553")
    url = df.attrs["url"]
    df["anno"] = df["time"].str[:4].astype(int)
    df["mese"] = df["time"].str[5:7]
    righe = []
    for anno, d in df.groupby("anno"):
        if d["mese"].nunique() < 12:
            continue
        q = d.loc[d["mese"].isin(["07", "08"]), "valore"].sum() / d["valore"].sum() * 100
        righe.append({"geo": "IT", "time": anno, "valore": round(q, 2)})
    out = pd.DataFrame(righe)
    out.attrs["aggiornato"] = df.attrs.get("aggiornato", "")
    salva(out, "obi_presenze_quota_lug_ago", fonte="Eurostat tour_occ_nim (elaborazione GovernAI)", url=url,
          nota="% presenze lug+ago sul totale annuo, strutture I551-I553, residenti+non residenti; solo anni completi", area="obi")


def rimpatri_su_ordini() -> None:
    """07-C3-a: rimpatri eseguiti / ordini di allontanamento (stesso anno), %."""
    r = eurostat("migr_eirtn", since="2015", geo="IT", citizen="TOTAL", age="TOTAL", sex="T", c_dest="TOTAL")
    o = eurostat("migr_eiord", since="2015", geo="IT", citizen="TOTAL", age="TOTAL", sex="T")
    m = r[["geo", "time", "valore"]].merge(o[["geo", "time", "valore"]], on=["geo", "time"], suffixes=("_rimp", "_ord"))
    m["valore"] = (m["valore_rimp"] / m["valore_ord"] * 100).round(2)
    m["time"] = m["time"].astype(int)
    m.attrs["aggiornato"] = r.attrs.get("aggiornato", "")
    salva(m[["geo", "time", "valore", "valore_rimp", "valore_ord"]], "obi_rimpatri_su_ordini",
          fonte="Eurostat migr_eirtn / migr_eiord (elaborazione GovernAI)", url=r.attrs["url"] + " ; " + o.attrs["url"],
          nota="rapporto % tra rimpatri e ordini di allontanamento nello stesso anno (non è un tasso per coorte)", area="obi")


def infermieri_su_medici() -> None:
    """06-C2-b: rapporto infermieri/medici praticanti (per 100.000 ab.)."""
    df = eurostat("hlth_rs_prs2", since="2010", geo="IT", unit="P_HTHAB", wstatus="PRACT", med_spec=["NRS", "PHYS"])
    p = df.pivot_table(index=["geo", "time"], columns="med_spec", values="valore").reset_index()
    p = p.dropna(subset=["NRS", "PHYS"])
    p["valore"] = (p["NRS"] / p["PHYS"]).round(3)
    p["time"] = p["time"].astype(int)
    p.attrs["aggiornato"] = df.attrs.get("aggiornato", "")
    salva(p[["geo", "time", "valore", "NRS", "PHYS"]], "obi_rapporto_infermieri_medici",
          fonte="Eurostat hlth_rs_prs2 (elaborazione GovernAI)", url=df.attrs["url"],
          nota="infermieri praticanti / medici praticanti, per 100.000 abitanti", area="obi")


def export_quote() -> None:
    """08-P6-a/b: quote dell'export (derivate da 08_commercio_it_partner, Eurostat Comext)."""
    df = _leggi("08_commercio_it_partner")
    e = df[df["flusso"] == "export"].pivot_table(index="time", columns="partner", values="valore")
    righe = []
    for t, r in e.iterrows():
        righe.append({"geo": "IT", "indicatore": "extra_ue_no_usa", "time": int(t),
                      "valore": round((r["EXT_EU27_2020"] - r["US"]) / r["WORLD"] * 100, 2)})
        righe.append({"geo": "IT", "indicatore": "top3_de_us_fr", "time": int(t),
                      "valore": round((r["DE"] + r["US"] + r["FR"]) / r["WORLD"] * 100, 2)})
    salva(pd.DataFrame(righe), "obi_export_quote_mercati", fonte="Elaborazione GovernAI su dati/serie/08_commercio_it_partner (Eurostat Comext DS-045409)",
          url="dati/serie/08_commercio_it_partner.csv", nota="% dell'export totale (WORLD)", area="obi")


def aps_rifugiati() -> None:
    """08-P5-b: spesa APS per rifugiati nel paese donatore / APS netto (flussi, USD)."""
    df = _leggi("08_aps_ocse_dac")
    d = df[(df["DONOR"] == "ITA") & (df["UNIT_MEASURE"] == "USD") & (df["MEASURE"].isin([1010, 1820]))]
    p = d.pivot_table(index="TIME_PERIOD", columns="MEASURE", values="OBS_VALUE").dropna()
    out = pd.DataFrame({"geo": "IT", "time": p.index.astype(int), "valore": (p[1820] / p[1010] * 100).round(2).values})
    salva(out, "obi_aps_quota_rifugiati", fonte="Elaborazione GovernAI su dati/serie/08_aps_ocse_dac (OCSE DAC1)",
          url="dati/serie/08_aps_ocse_dac.csv", nota="% APS netto (misura 1820 / 1010, USD correnti)", area="obi")


def regioni_perdite() -> None:
    """03-P3-b: numero di regioni/province autonome (NUTS2) con perdite idriche > 50%."""
    df = _leggi("03_acqua_perdite")
    n2 = df[df["REF_AREA"].str.len() == 4]
    out = (n2.assign(sopra=n2["perdite_pct"] > 50).groupby("TIME_PERIOD")["sopra"].sum()
             .reset_index().rename(columns={"TIME_PERIOD": "time", "sopra": "valore"}))
    out.insert(0, "geo", "IT")
    out["aree"] = [", ".join(n2[(n2["TIME_PERIOD"] == t) & (n2["perdite_pct"] > 50)]["REF_AREA"]) for t in out["time"]]
    salva(out, "obi_regioni_perdite_oltre_50", fonte="Elaborazione GovernAI su dati/serie/03_acqua_perdite (ISTAT Censimento acque)",
          url="dati/serie/03_acqua_perdite.csv", nota="conteggio NUTS2 (Trento e Bolzano separate) con perdite totali > 50%", area="obi")


def disposition_time() -> None:
    """07-C1-a/c: disposition time annuale tre gradi (esclude le rilevazioni semestrali)."""
    df = _leggi("07_disposition_time_pnrr")
    df = df[df["periodo"].str.fullmatch(r"(Baseline )?\d{4}")].copy()
    df["time"] = df["periodo"].str[-4:].astype(int)
    out = pd.concat([
        pd.DataFrame({"geo": "IT", "indicatore": "civile_tre_gradi", "time": df["time"], "valore": df["dt_civile_gg"]}),
        pd.DataFrame({"geo": "IT", "indicatore": "penale_tre_gradi", "time": df["time"], "valore": df["dt_penale_gg"]}),
    ])
    salva(out, "obi_disposition_time_annuale", fonte="Elaborazione GovernAI su dati/serie/07_disposition_time_pnrr (Min. Giustizia)",
          url="dati/serie/07_disposition_time_pnrr.csv", nota="giorni; solo dati annuali (2019 = baseline PNRR)", area="obi")


PASSI = [presenze_lug_ago, rimpatri_su_ordini, infermieri_su_medici, export_quote, aps_rifugiati, regioni_perdite, disposition_time]

if __name__ == "__main__":
    for f in PASSI:
        try:
            f()
            print("ok ", f.__name__)
        except Exception as e:  # una fonte giù non blocca le altre
            print("ERR", f.__name__, e)
