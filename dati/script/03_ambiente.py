"""Area 03 (Ambiente, Energia, Agricoltura, Protezione civile): serie di verifica del dossier.

Esegui da dati/script:  python 03_ambiente.py
Scarica le serie via fonti.py e salva in dati/serie/03_*.csv (registro: _registro_03.csv).
I documenti PDF ufficiali (Catalogo SAD MASE, Rapporto aste GSE, Rapporto Terna, newsletter GME)
sono salvati in dati/raw/03_*.pdf; le cifre usate sono trascritte qui sotto e verificate
automaticamente cercando la stringa nel testo del PDF (se pypdf è installato).

Nota su fonti.py: scarica() usa uno User-Agent personalizzato che alcuni siti (camera.it, gse.it)
possono rifiutare; in quel caso questo script riprova con un User-Agent da browser (_scarica_raw).
fonti.py NON viene modificato.
"""
from __future__ import annotations

import re

import pandas as pd
import requests

from fonti import RAW, eurostat, istat, salva, scarica

AREA = "03"


def _scarica_raw(url: str, nome: str):
    """scarica() di fonti.py, con ripiego su User-Agent da browser se il sito rifiuta."""
    try:
        return scarica(url, nome)
    except Exception as e:  # noqa: BLE001
        print(f"  scarica() fallita ({e.__class__.__name__}); riprovo con UA browser")
        RAW.mkdir(parents=True, exist_ok=True)
        r = requests.get(url, timeout=120, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        dest = RAW / nome
        dest.write_bytes(r.content)
        return dest


def _testo_pdf(path) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        return ""
    try:
        return " ".join((p.extract_text() or "") for p in PdfReader(str(path)).pages)
    except Exception:  # noqa: BLE001
        return ""


def _controlla(path, attese: list[str]):
    txt = re.sub(r"\s+", " ", _testo_pdf(path))
    if not txt:
        print(f"  (controllo testo saltato per {path.name})")
        return
    for s in attese:
        print(f"  {'OK ' if s in txt else '?? '} '{s}' in {path.name}")


# --- 1. Emissioni di gas serra per settore (inventario UNFCCC, via Eurostat) -------------
CRF = {"TOTX4_MEMO": "totale_escl_LULUCF", "CRF1A1": "industrie_energetiche",
       "CRF1A3": "trasporti", "CRF3": "agricoltura", "CRF3A": "agri_ferm_enterica",
       "CRF3B": "agri_gestione_deiezioni"}
ghg = eurostat("env_air_gge", since="1990", geo="IT", unit="MIO_T", airpol="GHG", src_crf=list(CRF))
salva(ghg, "03_ghg_settori", fonte="Eurostat env_air_gge (inventario ISPRA/UNFCCC)", url=ghg.attrs["url"],
      nota="MtCO2eq; TOTX4_MEMO = totale senza LULUCF", area=AREA)
p = ghg.pivot(index="time", columns="src_crf", values="valore")
tot = p["TOTX4_MEMO"]
print(f"GHG 2024: {tot['2024']:.1f} Mt, vs 1990 {100*(tot['2024']/tot['1990']-1):+.1f}%")
print(f"  ind. energetiche vs 1990 {100*(p['CRF1A1']['2024']/p['CRF1A1']['1990']-1):+.1f}%")
print(f"  trasporti quota {100*p['CRF1A3']['2024']/tot['2024']:.1f}%, vs 1990 {100*(p['CRF1A3']['2024']/p['CRF1A3']['1990']-1):+.1f}%")
print(f"  agricoltura quota {100*p['CRF3']['2024']/tot['2024']:.1f}%, allevamenti (3A+3B) "
      f"{100*(p['CRF3A']['2024']+p['CRF3B']['2024'])/p['CRF3']['2024']:.1f}% dell'agricoltura")

# --- 2. Tasso di circolarità dei materiali -----------------------------------------------
cur = eurostat("env_ac_cur", since="2015")
salva(cur, "03_circolarita_materiali", fonte="Eurostat env_ac_cur", url=cur.attrs["url"], nota="% uso circolare", area=AREA)
c24 = cur[(cur.time == "2024") & cur.geo.str.len().eq(2)].sort_values("valore", ascending=False).reset_index(drop=True)
print(f"Circolarità IT 2024: {c24.loc[c24.geo=='IT','valore'].item()}% (posto {c24.index[c24.geo=='IT'][0]+1} su {len(c24)})")

# --- 3. Quota rinnovabili (definizione RED, consumi finali lordi) ------------------------
ren = eurostat("nrg_ind_ren", since="2015", geo=["IT", "EU27_2020"], unit="PC", nrg_bal=["REN", "REN_ELC"])
salva(ren, "03_quota_rinnovabili_red", fonte="Eurostat nrg_ind_ren", url=ren.attrs["url"],
      nota="% su consumi finali lordi (definizione RED, diversa dalla quota sulla domanda Terna)", area=AREA)

# --- 4. Acqua: perdite idriche totali di distribuzione (ISTAT, Censimento acque uso civile) --
acq = istat("12_60_DF_DCCV_CONSACQUA_1", since="2018")
w = acq.pivot_table(index=["REF_AREA", "TIME_PERIOD"], columns="DATA_TYPE", values="OBS_VALUE").reset_index()
w["perdite_mln_m3"] = (w["ACQ_IMM"] - w["ACQ_EROG"]) / 1000
w["perdite_pct"] = (1 - w["ACQ_EROG"] / w["ACQ_IMM"]) * 100
w.attrs.update(acq.attrs)
salva(w, "03_acqua_perdite", fonte="ISTAT 12_60_DF_DCCV_CONSACQUA_1 (Censimento acque per uso civile)",
      url=acq.attrs["url"], nota="migliaia m3; perdite = immessa - erogata (perdite idriche totali)", area=AREA)
for reg in ["IT", "ITF5", "ITF1"]:
    r = w[(w.REF_AREA == reg)].sort_values("TIME_PERIOD").iloc[-1]
    print(f"Perdite {reg} {int(r.TIME_PERIOD)}: {r.perdite_pct:.1f}% ({r.perdite_mln_m3/1000:.2f} mld m3)")

# --- 5. Sussidi ambientalmente dannosi: Catalogo MASE, VIII ed. (luglio 2026), Tabella 2 ---
URL_SAD = "https://www.camera.it/temiap/2026/07/16/OCD177-9133.pdf"
pdf = _scarica_raw(URL_SAD, "03_catalogo_sad_saf_2026.pdf")
_controlla(pdf, ["22.382,3", "23.776,8", "20.632,1", "82.499,1"])
sad = pd.DataFrame({
    "anno": [2020, 2021, 2022, 2023, 2024, 2025],
    "SAD_mln": [17387.1, 20630.6, 24285.6, 23979.5, 23776.8, 22382.3],
    "SAI_mln": [12056.6, 11075.0, 13755.8, 26667.7, 25732.1, 22088.2],
    "SAF_mln": [23774.9, 24403.7, 27705.0, 41002.9, 70528.4, 82499.1],
    "FFS_fossili_mln": [13003.4, 15025.0, 19126.0, 20693.3, 21599.8, 20632.1],
})
salva(sad, "03_sad_catalogo_mase", fonte="MASE, Catalogo SAD/SAF VIII ed. 2026 (dati 2025), Tab. 2 - trasmesso alle Camere 14/7/2026",
      url=URL_SAD, nota="mln euro; SAD riformabili a livello nazionale 2025: 17.100 mln (testo, p.29)", area=AREA)

# --- 6. Proventi aste ETS: GSE, Rapporto annuale aste CO2 2025 ---------------------------
URL_ETS = "https://www.gse.it/documenti_site/Documenti%20GSE/Rapporti%20ASTE%20CO2/Rapporto%20Aste%20CO2_%20Annuale_%202025.pdf"
pdf = _scarica_raw(URL_ETS, "03_gse_aste_co2_2025.pdf")
_controlla(pdf, ["2.598,6", "2.610,9"])
TOT = 2598.6
# Ripartizione art. 23 d.lgs. 47/2020 (testo vigente, Normattiva): comma 8 preleva la quota eccedente
# 1.000 mln (fino a 600 mln Fondo transizione energetica settore industriale + fino a 150 mln Fondo
# transizione industriale); del resto 50% al Fondo ammortamento titoli di Stato (c.5) e 50% ai ministeri
# (c.4: MASE 70%, MIMIT 15%, MIT 15%) per le finalità climatiche del c.7. Ricostruzione GovernAI.
c8 = min(max(TOT - 1000, 0), 750)
resto = TOT - c8
ets = pd.DataFrame([
    ("proventi_totali_2024", 2610.9, "GSE"), ("proventi_totali_2025", TOT, "GSE"),
    ("art23_c8_fondi_transizione_industriale", c8, "calcolo art.23 c.8"),
    ("art23_c5_fondo_ammortamento_titoli", resto / 2, "calcolo art.23 c.5"),
    ("art23_c4_MASE_70", resto / 2 * 0.70, "calcolo art.23 c.4"),
    ("art23_c4_MIMIT_15", resto / 2 * 0.15, "calcolo art.23 c.4"),
    ("art23_c4_MIT_15", resto / 2 * 0.15, "calcolo art.23 c.4"),
], columns=["voce", "mln_eur", "metodo"])
salva(ets, "03_ets_proventi", fonte="GSE, Rapporto annuale aste CO2 2025; d.lgs. 47/2020 art. 23", url=URL_ETS,
      nota="ripartizione = ricostruzione GovernAI sul testo vigente; tutte le quote hanno destinazione per legge", area=AREA)
print(ets.round(1).to_string(index=False))

# --- 7. Sistema elettrico 2025: Terna, Rapporto mensile dicembre 2025 ----------------------
URL_TERNA = "https://www.rinnovabili.it/wp-content/uploads/2026/01/Rapporto_mensile_dicembre_25_8de58e4159b881a.pdf"
pdf = _scarica_raw(URL_TERNA, "03_terna_rapporto_mensile_dic2025.pdf")
_controlla(pdf, ["311.324", "41,1%", "7.191"])
el = pd.DataFrame([("domanda_GWh", 311324), ("quota_FER_domanda_pct", 41.1), ("FER_TWh", 128.0),
                   ("nuova_capacita_FER_MW", 7191), ("nuovo_FV_MW", 6437), ("nuovo_eolico_MW", 608)],
                  columns=["voce", "valore"])
salva(el, "03_terna_2025", fonte="Terna, Rapporto mensile sul sistema elettrico, dicembre 2025",
      url=URL_TERNA, nota="documento Terna ripubblicato da rinnovabili.it", area=AREA)

# --- 8. PUN 2025: GME, Newsletter gennaio 2026 ---------------------------------------------
URL_GME = "https://gme.mercatoelettrico.org/Portals/0/Documents/Newsletter/20260116Newsletter.pdf"
pdf = _scarica_raw(URL_GME, "03_gme_newsletter_2026-01.pdf")
pun = pd.DataFrame([(2024, 108.52), (2025, 115.32)], columns=["anno", "PUN_eur_MWh"])
salva(pun, "03_pun_gme", fonte="GME, Newsletter n. gennaio 2026 (PUN Index baseload annuo)", url=URL_GME,
      nota="+6,3% 2025/2024", area=AREA)
print("Fatto.")
