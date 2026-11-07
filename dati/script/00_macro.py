"""Serie macro di base usate da tutti i dossier: debito, deficit, PIL, popolazione."""
from fonti import eurostat, salva

SERIE = [
    ("debito_pil", "gov_10dd_edpt1", dict(unit="PC_GDP", na_item="GD", sector="S13")),
    ("deficit_pil", "gov_10dd_edpt1", dict(unit="PC_GDP", na_item="B9", sector="S13")),
    ("pil_mld_eur", "nama_10_gdp", dict(unit="CP_MEUR", na_item="B1GQ")),
    ("spesa_interessi_pil", "gov_10a_main", dict(unit="PC_GDP", na_item="D41PAY", sector="S13")),
    ("popolazione", "demo_pjan", dict(sex="T", age="TOTAL")),
]

for nome, ds, filtri in SERIE:
    df = eurostat(ds, since="2015", geo=["IT", "EU27_2020"], **filtri)
    salva(df, nome, fonte=f"Eurostat {ds}", url=df.attrs["url"])
    ultimo = df[df.geo == "IT"].sort_values("time").tail(1)
    print(f"{nome:22s} IT {ultimo.time.item()}: {ultimo.valore.item()}")
