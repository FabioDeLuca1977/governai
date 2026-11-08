"""GovernAI - Benchmark internazionale (agente "confronto internazionale e fisco").

Scarica da Eurostat un indicatore chiave per area di governo, per tutti i Paesi UE,
e lo salva in dati/serie/ con prefisso "bm_" (registro: dati/serie/_registro_bm.csv).
Stampa la classifica UE27 dell'ultimo anno disponibile, con il dato dell'Italia.
Eseguire da dati/script/:
    python bm_benchmark.py

Gli indicatori non presenti in Eurostat (giustizia civile, aiuto allo sviluppo, VAT gap)
sono trascritti in benchmark/confronto.md con fonte e link (EU Justice Scoreboard, OCSE DAC,
Commissione UE): non sono salvati qui per non duplicare cifre non scaricate dalla fonte.
"""
from __future__ import annotations

from fonti import eurostat, salva

AREA = "bm"
UE27 = ["AT", "BE", "BG", "CY", "CZ", "DE", "DK", "EE", "EL", "ES", "FI", "FR", "HR", "HU", "IE",
        "IT", "LT", "LU", "LV", "MT", "NL", "PL", "PT", "RO", "SE", "SI", "SK"]

INDICATORI = [
    # nome, dataset, filtri, descrizione, ordine (True = più alto è meglio)
    ("bm_02_occupazione_20_64", "lfsi_emp_a",
     dict(since="2019", indic_em="EMP_LFS", sex=["T", "F"], age="Y20-64", unit="PC_POP"),
     "Tasso di occupazione 20-64 anni (%), totale e donne", True),
    ("bm_03_rinnovabili_quota", "nrg_ind_ren", dict(since="2019", nrg_bal="REN", unit="PC"),
     "Quota di rinnovabili nel consumo finale lordo di energia (%)", True),
    ("bm_04_sovraccarico_abitativo", "ilc_lvho07c", dict(since="2019", unit="PC"),
     "Sovraccarico del costo abitativo (>40% del reddito disponibile) per titolo di godimento (%)", False),
    ("bm_05_laureati_25_34", "edat_lfse_03",
     dict(since="2019", isced11="ED5-8", age="Y25-34", sex="T", unit="PC"),
     "Popolazione 25-34 anni con istruzione terziaria (%)", True),
    ("bm_06_bisogni_cure_insoddisfatti", "hlth_silc_08",
     dict(since="2019", reason="TXP_TFAR_WLIST", age="Y_GE16", sex="T", quant_inc=["TOTAL", "QU1"], unit="PC"),
     "Bisogni di cure mediche non soddisfatti per costo, distanza o liste d'attesa, 16+ anni (%), totale e primo quintile", False),
    ("bm_09_egov_uso", "isoc_ciegi_ac",
     dict(since="2022", indic_is="I_IUGOV1", ind_type="IND_TOTAL", unit="PC_IND"),
     "Persone 16-74 che hanno interagito online con la PA negli ultimi 12 mesi (%)", True),
    ("bm_01_produttivita_ora", "nama_10_lp_ulc",
     dict(since="2015", na_item="RLPR_HW", unit="I15"),
     "Produttività reale del lavoro per ora lavorata, indice 2015=100", True),
]


def classifica(df, filtro, alto_meglio, n=4):
    d = df.copy()
    for k, v in filtro.items():
        d = d[d[k] == v]
    d = d[d["geo"].isin(UE27)]
    anno = d["time"].max()
    d = d[d["time"] == anno].sort_values("valore", ascending=not alto_meglio)
    it = d[d["geo"] == "IT"]["valore"]
    rank = list(d["geo"]).index("IT") + 1 if "IT" in list(d["geo"]) else None
    top = ", ".join(f"{g} {v:g}" for g, v in zip(d["geo"][:n], d["valore"][:n]))
    return anno, top, (it.iloc[0] if len(it) else None), rank, len(d)


if __name__ == "__main__":
    for nome, ds, filtri, descr, alto in INDICATORI:
        try:
            df = eurostat(ds, **filtri)
        except Exception as e:  # una fonte irraggiungibile non blocca lo script
            print(f"! {nome}: {e}")
            continue
        salva(df, nome, f"Eurostat {ds}", df.attrs["url"], descr, area=AREA)
        sotto = []
        if "sex" in df.columns and df["sex"].nunique() > 1:
            sotto = [{"sex": "T"}, {"sex": "F"}]
        elif "tenure" in df.columns:
            sotto = [{"tenure": "RENT_MKT"}, {"tenure": "TOTAL"}]
        elif "quant_inc" in df.columns:
            sotto = [{"quant_inc": "TOTAL"}, {"quant_inc": "QU1"}]
        for f in (sotto or [{}]):
            anno, top, it, rank, n = classifica(df, f, alto)
            print(f"{nome} {f}: {anno} | migliori: {top} | IT {it} ({rank}° su {n})")
