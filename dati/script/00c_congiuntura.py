"""Indicatori congiunturali ad alta frequenza (mensili e trimestrali): il "polso" del Paese.

Sono le serie che cambiano più spesso e su cui il sistema dinamico reagisce:
inflazione, disoccupazione, spread, PIL trimestrale, debito trimestrale, produzione, fiducia.
"""
from fonti import eurostat, salva

SERIE = [
    # nome, dataset, inizio, filtri, nota
    ("00c_inflazione_annua", "prc_hicp_minr", "2021-01",
     dict(geo=["IT", "EA20"], unit="RCH_A", coicop18="TOTAL"),
     "HICP, variazione % annua (ECOICOP v2, dal 2026)"),
    ("00c_disoccupazione_mensile", "une_rt_m", "2021-01",
     dict(geo=["IT", "EA20"], s_adj="SA", age=["TOTAL", "Y_LT25"], sex="T", unit="PC_ACT"),
     "tasso di disoccupazione destagionalizzato"),
    ("00c_rendimenti_decennali", "irt_lt_mcby_m", "2021-01",
     dict(geo=["IT", "DE"]),
     "rendimento dei titoli di Stato a lungo termine (criterio di Maastricht); spread = IT - DE"),
    ("00c_pil_trimestrale", "namq_10_gdp", "2021-Q1",
     dict(geo=["IT", "EA20"], unit="CLV_PCH_PRE", s_adj="SCA", na_item="B1GQ"),
     "PIL reale, variazione % sul trimestre precedente"),
    ("00c_debito_trimestrale", "gov_10q_ggdebt", "2021-Q1",
     dict(geo="IT", unit="PC_GDP", na_item="GD", sector="S13"),
     "debito delle AP in % del PIL, trimestrale"),
    ("00c_produzione_industriale", "sts_inpr_m", "2021-01",
     dict(geo="IT", s_adj="SCA", unit="I21", nace_r2="B-D"),
     "indice della produzione industriale (2021=100)"),
    ("00c_fiducia_consumatori", "ei_bsco_m", "2021-01",
     dict(geo="IT", indic="BS-CSMCI", s_adj="SA", unit="BAL"),
     "clima di fiducia dei consumatori (saldo)"),
]

for nome, ds, since, filtri, nota in SERIE:
    df = eurostat(ds, since=since, **filtri)
    salva(df, nome, fonte=f"Eurostat {ds}", url=df.attrs["url"], nota=nota, area="00c")
    ult = df[df.geo == "IT"].sort_values("time").tail(1)
    print(f"{nome:30s} IT {ult.time.item()}: {ult.valore.item()} {ult.flag.item() or ''}")
