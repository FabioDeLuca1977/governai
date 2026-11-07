"""Area 08 (Esteri, Europa, Istituzioni): serie di fonte primaria usate nella verifica del dossier.

Fonti:
  1. Eurostat Comext DS-045409 (commercio estero Italia per partner, concetto comunitario)
  2. OCSE DAC1 (APS Italia e DAC: % RNL, equivalente dono, costi rifugiati nel Paese donatore)
  3. Eurostat nasa_10_nf_tr (RNL a prezzi correnti, Italia e UE27)
  4. Commissione UE, "EU spending and revenue 2000-2025" (xlsx)
  5. Serie macro gia' presenti in dati/serie (debito_pil): solo lettura

Note tecniche (fonti.py non e' modificato):
  - fonti.eurostat() usa solo l'endpoint "statistics": i dataset Comext (DS-xxxx) stanno su
    un endpoint diverso (/api/comext/...). Qui c'e' un piccolo parser JSON-stat equivalente.
  - fonti.salva() salva df.attrs["aggiornato"] solo se presente: lo impostiamo a mano.
Eseguire da dati/script:  python 08_esteri.py
"""
from __future__ import annotations

import io
import itertools

import pandas as pd
import requests

from fonti import HEADERS, SERIE, eurostat, salva, scarica

AREA = "08"


def jsonstat_df(url: str) -> pd.DataFrame:
    js = requests.get(url, timeout=120, headers=HEADERS).json()
    dims = js["id"]
    cats = [sorted(js["dimension"][d]["category"]["index"].items(), key=lambda kv: kv[1]) for d in dims]
    righe = []
    for i, combo in enumerate(itertools.product(*cats)):
        v = js["value"].get(str(i))
        if v is not None:
            righe.append({**{d: c[0] for d, c in zip(dims, combo)}, "valore": v})
    df = pd.DataFrame(righe)
    df.attrs.update(url=url, aggiornato=js.get("updated", ""))
    return df


# --- 1. Commercio estero Italia per partner (Comext) ---------------------------
COMEXT = ("https://ec.europa.eu/eurostat/api/comext/dissemination/statistics/1.0/data/DS-045409"
          "?freq=A&reporter=IT&partner=US&partner=DE&partner=FR&partner=WORLD&partner=EU27_2020"
          "&partner=EXT_EU27_2020&product=TOTAL&flow=1&flow=2&indicators=VALUE_IN_EUROS"
          "&time=2023&time=2024&time=2025")
tr = jsonstat_df(COMEXT)
tr["flusso"] = tr["flow"].map({"1": "import", "2": "export"})
tr["mld_eur"] = tr["valore"] / 1e9
salva(tr, "08_commercio_it_partner", fonte="Eurostat Comext DS-045409 (concetto comunitario)", url=COMEXT,
      nota="Valori in euro; differiscono dai dati ISTAT (concetto nazionale) per trattamento del transito", area=AREA)
pv = tr.pivot_table(index=["flusso", "partner"], columns="time", values="mld_eur")
print("Commercio IT (mld EUR, Comext):\n", pv.round(1))
tot_exp = pv.loc[("export", "WORLD")] if ("export", "WORLD") in pv.index else None
if tot_exp is not None:
    for p in ["US", "DE", "FR"]:
        if ("export", p) in pv.index:
            print(f"  quota export {p} 2025: {100 * pv.loc[('export', p), '2025'] / tot_exp['2025']:.1f}%")
    if ("import", "US") in pv.index:
        print(f"  var. import da US 2025/24: {100 * (pv.loc[('import', 'US'), '2025'] / pv.loc[('import', 'US'), '2024'] - 1):.1f}%")
        print(f"  var. export verso US 2025/24: {100 * (pv.loc[('export', 'US'), '2025'] / pv.loc[('export', 'US'), '2024'] - 1):.1f}%")
    if ("import", "WORLD") in pv.index:
        print(f"  saldo 2025: {tot_exp['2025'] - pv.loc[('import', 'WORLD'), '2025']:.1f} mld")

# --- 2. APS Italia (OCSE DAC1) -------------------------------------------------
DAC = ("https://sdmx.oecd.org/public/rest/data/OECD.DCD.FSD,DSD_DAC1@DF_DAC1,/ITA+DAC.........."
       "?startPeriod=2018&dimensionAtObservation=AllDimensions&format=csvfilewithlabels")
raw = requests.get(DAC, timeout=180, headers=HEADERS).text
(SERIE.parent / "raw").mkdir(exist_ok=True)
(SERIE.parent / "raw" / "08_oecd_dac1_ita_dac.csv").write_text(raw, encoding="utf-8")
dac = pd.read_csv(io.StringIO(raw))
dac["MEASURE"] = dac["MEASURE"].astype(str)
sel = dac[(dac.PRICE_BASE == "V") & (
    ((dac.MEASURE == "11002") & (dac.UNIT_MEASURE == "PT_B5G")) |
    ((dac.MEASURE == "11010") & dac.UNIT_MEASURE.isin(["USD", "XDC"])) |
    ((dac.MEASURE == "1820") & (dac.FLOW_TYPE == 1140) & dac.UNIT_MEASURE.isin(["USD", "XDC"])) |
    ((dac.MEASURE == "1010") & (dac.FLOW_TYPE == 1140) & dac.UNIT_MEASURE.isin(["USD", "XDC"]))
)][["DONOR", "MEASURE", "Measure", "FLOW_TYPE", "UNIT_MEASURE", "TIME_PERIOD", "OBS_VALUE"]]
sel.attrs["aggiornato"] = "OCSE DAC1 (2025 = dati preliminari, apr. 2026)"
salva(sel, "08_aps_ocse_dac", fonte="OCSE DAC1 (Data Explorer, DF_DAC1)", url=DAC,
      nota="11002=APS/RNL equivalente dono; 11010=APS equiv. dono; 1820=rifugiati nel Paese donatore (flussi netti); 1010=APS flussi netti; XDC=mln EUR", area=AREA)
k = sel.pivot_table(index=["DONOR", "MEASURE", "UNIT_MEASURE"], columns="TIME_PERIOD", values="OBS_VALUE")
print("\nAPS (OCSE DAC1):\n", k.round(2))
it = lambda m, u, y: k.loc[("ITA", m, u), y]
for y in [2024, 2025]:
    print(f"  {y}: APS/RNL {it('11002', 'PT_B5G', y):.2f}% | DAC {k.loc[('DAC', '11002', 'PT_B5G'), y]:.2f}% | "
          f"rifugiati {it('1820', 'XDC', y):.0f} mln EUR = {100 * it('1820', 'XDC', y) / it('1010', 'XDC', y):.1f}% APS netto "
          f"({100 * it('1820', 'XDC', y) / it('11010', 'XDC', y):.1f}% equiv. dono)")

# --- 3. RNL Italia e UE27 (Eurostat) -------------------------------------------
rnl = eurostat("nasa_10_nf_tr", since="2019", geo=["IT", "EU27_2020"], unit="CP_MEUR", na_item="B5G",
               sector="S1", direct="PAID")
salva(rnl, "08_rnl_it_ue", fonte="Eurostat nasa_10_nf_tr (B5G, S1)", url=rnl.attrs["url"], area=AREA)
r = rnl.pivot_table(index="time", columns="geo", values="valore")
r25 = r.loc["2025"]
print(f"\nRNL 2025: IT {r25['IT'] / 1e3:.1f} mld; quota UE27 {100 * r25['IT'] / r25['EU27_2020']:.2f}%")
print(f"  gap APS 0,30%->0,70%: {r25['IT'] / 1e3 * 0.0040:.1f} mld; +0,02 pt = {r25['IT'] / 1e3 * 0.0002:.2f} mld; "
      f"0,30%->0,50% = {r25['IT'] / 1e3 * 0.0020:.1f} mld (a RNL 2025 costante)")

# --- 4. Saldo Italia-bilancio UE (Commissione, EU spending and revenue) --------
XLS = ("https://commission.europa.eu/document/download/9f334bee-d097-4b68-8f93-2225eabeb631_en"
       "?filename=eu_budget_spending_and_revenue_2000-2025.xlsx")
p = scarica(XLS, "08_eu_spending_revenue_2000-2025.xlsx")
VOCI = {"spesa_qfp": "TOTAL EXPENDITURE", "spesa_ngeu": "TOTAL NGEU", "risorse_proprie": "TOTAL Own resources",
        "dazi": "Customs duties", "aggiustamenti": "TOTAL Balances and adjustments"}
righe = []
for anno in ["2021", "2022", "2023", "2024", "2025"]:
    sh = pd.read_excel(p, sheet_name=anno, header=None)
    col = next(j for j, v in enumerate(sh.iloc[2].tolist()) if str(v).strip() == "IT")
    lab = sh.iloc[:, :4].astype(str).agg(" ".join, axis=1)
    rec = {"anno": anno}
    for k_, testo in VOCI.items():
        idx = [i for i, s in enumerate(lab) if testo.lower() in s.lower()]
        rec[k_] = pd.to_numeric(sh.iloc[idx[0], col], errors="coerce") if idx else float("nan")
    righe.append(rec)
eu = pd.DataFrame(righe).fillna({"spesa_ngeu": 0.0, "aggiustamenti": 0.0})
eu["contributo_nazionale"] = eu.risorse_proprie - eu.dazi + eu.aggiustamenti  # esclusi dazi (risorse proprie tradizionali)
eu["saldo_netto_qfp"] = eu.spesa_qfp - eu.contributo_nazionale
eu["saldo_netto_con_ngeu"] = eu.saldo_netto_qfp + eu.spesa_ngeu
eu.attrs["aggiornato"] = "file Commissione del 29-09-2026"
salva(eu, "08_saldo_it_bilancio_ue", fonte="Commissione UE, EU spending and revenue 2000-2025", url=XLS,
      nota="mln EUR; saldo semplificato GovernAI (spesa in IT - contributi nazionali esclusi dazi); "
           "non coincide con l'operating budgetary balance ufficiale (che esclude spese amministrative)", area=AREA)
print("\nItalia-bilancio UE (mln EUR):\n", eu.round(0).to_string(index=False))

# --- 5. Debito/PIL gia' scaricato (solo lettura) -------------------------------
deb = pd.read_csv(SERIE / "debito_pil.csv")
print("\nDebito/PIL IT:", deb[deb.geo == "IT"].sort_values("time").tail(3)[["time", "valore"]].to_dict("records"))
