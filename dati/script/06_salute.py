"""Area 06 - Salute: serie e documenti di fonte primaria usati nel dossier ministeri/06_salute.md.

Esecuzione:  python 06_salute.py   (dalla cartella dati/script)
Usa la libreria comune fonti.py; non riscarica le serie macro (usa dati/serie/pil_mld_eur.csv).
Le tabelle estratte da documenti ufficiali (DPFP 2026, DDL bilancio 2027, AIFA) sono salvate
con i valori letti dal PDF; dove il PDF non è leggibile si usano i valori trascritti (verificati
il 7/11/2026) e lo si segnala nella nota del registro.
"""
from __future__ import annotations

import re

import pandas as pd

from fonti import RAW, SERIE, eurostat, salva, scarica

AREA = "06"
GEO = ["IT", "EU27_2020"]


def _testo_pdf(percorso) -> str:
    """Estrae il testo di un PDF con PyMuPDF, se installato; altrimenti stringa vuota."""
    try:
        import pymupdf  # type: ignore
    except ImportError:
        try:
            import fitz as pymupdf  # type: ignore
        except ImportError:
            return ""
    with pymupdf.open(percorso) as doc:
        return "\n".join(p.get_text() for p in doc)


def _num(s: str) -> float:
    return float(s.replace(".", "").replace(",", "."))


# --- 1. Eurostat (ripubblica i conti SHA ISTAT, personale, EU-SILC) -------------

def serie_eurostat():
    # Spesa sanitaria per regime di finanziamento (SHA 2011): HF1 pubblica/obbligatoria,
    # HF2 volontaria, HF3 out-of-pocket delle famiglie.
    df = eurostat("hlth_sha11_hf", since="2015", geo="IT", unit=["MIO_EUR", "PC_CHE", "PC_GDP"],
                  icha11_hf=["TOT_HF", "HF1", "HF2", "HF3"])
    salva(df, "06_spesa_sanitaria_finanziamento", "Eurostat hlth_sha11_hf (conti SHA, fonte nazionale ISTAT)",
          df.attrs["url"], "HF3 = spesa diretta delle famiglie (out-of-pocket)", area=AREA)
    piv = df.pivot_table(index=["unit", "icha11_hf"], columns="time", values="valore")
    print("SHA - out-of-pocket (HF3):\n", piv.loc[[("MIO_EUR", "HF3"), ("PC_CHE", "HF3"), ("PC_GDP", "HF1")]].iloc[:, -3:])

    # Spesa per funzione: HC6 prevenzione, HC3 lungodegenza (LTC sanitaria)
    df = eurostat("hlth_sha11_hc", since="2015", geo="IT", unit=["MIO_EUR", "PC_CHE"],
                  icha11_hc=["TOT_HC", "HC6", "HC3"])
    salva(df, "06_spesa_sanitaria_funzioni", "Eurostat hlth_sha11_hc (conti SHA, fonte nazionale ISTAT)",
          df.attrs["url"], "HC6 = prevenzione; HC3 = assistenza a lungo termine (componente sanitaria)", area=AREA)
    print("SHA - prevenzione HC6 (% spesa corrente):",
          df[(df.unit == "PC_CHE") & (df.icha11_hc == "HC6")].sort_values("time").tail(3)[["time", "valore"]].values.tolist())

    # Personale sanitario (medici, infermieri, ecc.) per 100.000 ab.
    df = eurostat("hlth_rs_prs2", since="2015", geo="IT", unit=["P_HTHAB", "NR"])
    salva(df, "06_personale_sanitario", "Eurostat hlth_rs_prs2", df.attrs["url"],
          "PRACT = professionisti in attività clinica (definizione OCSE 'practising'); rottura di serie 2021 per i medici", area=AREA)
    p = df[(df.unit == "P_HTHAB") & (df.wstatus == "PRACT")].pivot_table(index="med_spec", columns="time", values="valore")
    print("Personale praticante per 100.000 ab.:\n", p.loc[["NRS", "PHYS"]].iloc[:, -3:])

    # Bisogni di cure mediche non soddisfatti (EU-SILC): costo, distanza, attesa
    df = eurostat("hlth_silc_08", since="2015", geo=GEO, sex="T", age="Y_GE16", quant_inc="TOTAL")
    salva(df, "06_bisogni_non_soddisfatti", "Eurostat hlth_silc_08 (EU-SILC)", df.attrs["url"],
          "TXP_TFAR_WLIST = troppo costoso, troppo lontano o lista d'attesa; % popolazione 16+", area=AREA)
    u = df[df.reason.isin(["TXP_TFAR_WLIST", "TXP", "WLIST"])].pivot_table(index=["geo", "reason"], columns="time", values="valore")
    print("Bisogni non soddisfatti:\n", u.iloc[:, -3:])


# --- 2. DPFP 2026 (MEF, ottobre 2026): spesa sanitaria della PA ----------------

DPFP_URL = "https://www.mef.gov.it/export/sites/MEF/inevidenza/2026/article_00390/DPFP26.pdf"
# Valori trascritti dalla Tavola II.1.1A/B (conto PA a legislazione vigente), usati se il parsing fallisce
DPFP_SPESA_SAN = {2025: 141539, 2026: 148836, 2027: 151668, 2028: 155647, 2029: 160035}
DPFP_PIL = {2025: 2265002, 2026: 2326150, 2027: 2393639, 2028: 2459360, 2029: 2524049}


def dpfp_2026():
    pdf = scarica(DPFP_URL, "06_DPFP26_MEF.pdf")
    testo = _testo_pdf(pdf)
    spesa, pil, fonte_valori = dict(DPFP_SPESA_SAN), dict(DPFP_PIL), "trascritti"
    m = re.search(r"TAVOLA II\.1\.1A.*?di cui: Spesa sanitaria\s+((?:[\d.]+\s+){5})", testo, re.S)
    g = re.search(r"TAVOLA II\.1\.1A.*?PIL nominale tendenziale \(x 1\.000\)\s+((?:[\d.]+\s+){5})", testo, re.S)
    if m and g:
        anni = range(2025, 2030)
        spesa = dict(zip(anni, (_num(x) for x in m.group(1).split())))
        pil = dict(zip(anni, (_num(x) for x in g.group(1).split())))
        fonte_valori = "estratti dal PDF"
        for a in anni:  # controllo di coerenza con la trascrizione manuale
            assert abs(spesa[a] - DPFP_SPESA_SAN[a]) < 1, (a, spesa[a])
    df = pd.DataFrame({"anno": list(spesa), "spesa_sanitaria_mln": list(spesa.values()),
                       "pil_tendenziale_mln": [pil[a] for a in spesa]})
    df["spesa_sanitaria_pc_pil"] = (df.spesa_sanitaria_mln / df.pil_tendenziale_mln * 100).round(2)
    salva(df, "06_dpfp2026_spesa_sanitaria", "MEF, Documento programmatico di finanza pubblica 2026, Tav. II.1.1A-B",
          DPFP_URL, f"Conto PA a legislazione vigente (prima della manovra 2027); valori {fonte_valori}. "
          "Il DPFP pubblica 6,2-6,4-6,3-6,3-6,3% del PIL (2025-2029).", area=AREA)
    print("DPFP 2026 spesa sanitaria PA:\n", df)
    return pil


# --- 3. FSN: livello vigente + DDL bilancio 2027 (A.C. 3174, art. 69) ---------

DDL_URL = "https://documenti.camera.it/leg19/pdl/pdf/leg.19.pdl.camera.3174.19PDL0221140.pdf"
CAMERA_SSN_URL = "https://temi.camera.it/leg19/temi/19_tl18_organizzazione_ssn"
# Livello vigente prima del DDL 2027 (Camera dei deputati, tema "Organizzazione SSN", 31/7/2026,
# su dati Corte dei conti; 2025 = riparto CIPESS 29/1/2026). Il 2029 vigente non è pubblicato:
# il valore 2029 totale (148,2) è quello Gimbe, non verificato su fonte primaria.
FSN_VIGENTE = {2025: 136540, 2026: 142900, 2027: 143900, 2028: 144800}
DDL_INCREMENTO = {2027: 2365, 2028: 2352, 2029: 2399}  # art. 69, c. 1, A.C. 3174
FSN_2029_GIMBE = 148200


def fsn_pil(pil: dict):
    pdf = scarica(DDL_URL, "06_AC3174_DDL_bilancio_2027_relazioni.pdf")
    testo = _testo_pdf(pdf)
    if testo:
        m = re.search(r"incrementa il livello di finanziamento del fabbisogno sanitario nazionale standard cui\s+"
                      r"concorre lo Stato dell.importo di ([\d.]+) milioni di euro per l.anno 2027, di ([\d.]+) milioni di euro\s+"
                      r"per l.anno 2028 e di ([\d.]+) milioni", testo)
        if m:
            letti = dict(zip([2027, 2028, 2029], (_num(x) for x in m.groups())))
            assert letti == DDL_INCREMENTO, letti
            print("DDL art. 69 c.1 confermato dal PDF:", letti)
    righe = []
    for a in range(2025, 2030):
        vig = FSN_VIGENTE.get(a)
        inc = DDL_INCREMENTO.get(a, 0)
        tot = (vig + inc) if vig else FSN_2029_GIMBE
        righe.append({"anno": a, "fsn_vigente_mln": vig, "incremento_ddl2027_mln": inc, "fsn_totale_mln": tot,
                      "pil_dpfp_tendenziale_mln": pil[a], "fsn_pc_pil": round(tot / pil[a] * 100, 2),
                      "stato": "verificato" if vig else "livello Gimbe, base vigente 2029 non verificata"})
    df = pd.DataFrame(righe)
    salva(df, "06_fsn_pil", "Camera dei deputati (livello vigente, da Corte dei conti) + DDL bilancio 2027 A.C. 3174 art. 69 + PIL DPFP 2026",
          f"{CAMERA_SSN_URL} ; {DDL_URL} ; {DPFP_URL}",
          "Rapporto FSN/PIL calcolato da GovernAI sul PIL tendenziale DPFP 2026; il DPFP non pubblica un FSN/PIL programmatico", area=AREA)
    print("FSN / PIL:\n", df)

    misure = pd.DataFrame([
        ("art. 69 c.1", "Incremento FSN 2027-2029", 2365, 2352, 2399),
        ("art. 69 c.4", "Prestazioni aggiuntive per liste d'attesa (a valere sul FSN)", 300, 0, 0),
        ("art. 69 c.6", "Indennità pronto soccorso (a valere sul FSN)", 380, 380, 380),
        ("art. 71 c.2-6", "Riduzione payback acquisti diretti / Fondo compensazione", 160, 160, 160),
        ("art. 53 c.1", "Carta valore 300 euro over 75 per beni e prestazioni sanitarie", 1645, 0, 0),
        ("art. 40 c.1 b", "Rinvio sugar tax al 1/7/2027: minor gettito (cassa, netto)", -170.1, 60.2, -26.2),
    ], columns=["norma", "misura", "2027_mln", "2028_mln", "2029_mln"])
    salva(misure, "06_ddl_bilancio_2027_sanita", "DDL bilancio 2027, A.C. 3174, relazione illustrativa e tecnica",
          DDL_URL, "Prestazione universale anziani prorogata al 31/12/2027 con ISEE 12.000 euro (art. 53 c.3)", area=AREA)


# --- 4. AIFA: monitoraggio spesa farmaceutica 2025 consuntivo -----------------

AIFA_URL = "https://www.aifa.gov.it/documents/20142/3073807/Monitoraggio_Spesa_gennaio-dicembre-2025_consuntivo.pdf"
# Valori del PDF consuntivo (dati NSIS al 14/5/2026, FSN 2025 definitivo 135.364,9 mln), usati se il parsing fallisce
AIFA_2025 = {"spesa_complessiva": 24950.2, "disavanzo_acquisti_diretti_netto_gas": 4767.1,
             "incidenza_acquisti_diretti_pc_fsn": 11.82, "convenzionata_netto_payback": 8691.5,
             "avanzo_convenzionata": 513.3, "fsn_2025_definitivo": 135364.9}
AIFA_RE = {
    "spesa_complessiva": r"spesa complessiva del periodo Gennaio-\s*Dicembre 2025 si . attestata a ([\d.,]+) mln",
    "disavanzo_acquisti_diretti_netto_gas": r"disavanzo rispetto alla spesa programmata di \+([\d.,]+) mln",
    "incidenza_acquisti_diretti_pc_fsn": r"evidenzia un.incidenza dell.([\d,]+)%, pari ad un disavanzo",
    "convenzionata_netto_payback": r"pari a ([\d.,]+) milioni di euro che incide sul FSN",
    "avanzo_convenzionata": r"generando un avanzo di ([\d.,]+) milioni",
}


def aifa():
    valori, nota = dict(AIFA_2025), "valori trascritti"
    try:
        pdf = scarica(AIFA_URL, "06_AIFA_monitoraggio_spesa_2025_consuntivo.pdf")
        testo = re.sub(r"\s+", " ", _testo_pdf(pdf))
        letti = {k: _num(m.group(1)) for k, rx in AIFA_RE.items() if (m := re.search(rx, testo))}
        valori.update(letti)
        nota = f"estratti dal PDF: {sorted(letti)}; payback acquisti diretti = 50% del disavanzo (ripiano a carico aziende)"
    except Exception as e:  # il sito AIFA a volte rifiuta client non-browser
        nota = f"PDF non scaricato ({type(e).__name__}); valori trascritti"
    valori["payback_50pc_stimato"] = round(valori["disavanzo_acquisti_diretti_netto_gas"] / 2, 1)
    df = pd.DataFrame([{"voce": k, "valore_2025": v} for k, v in valori.items()])
    salva(df, "06_aifa_spesa_farmaceutica_2025", "AIFA, Monitoraggio spesa farmaceutica gen-dic 2025 (consuntivo)",
          AIFA_URL, nota, area=AREA)
    print("AIFA:", valori, nota)


if __name__ == "__main__":
    serie_eurostat()
    pil = dpfp_2026()
    # controllo: il PIL 2025 del DPFP coincide con la serie macro già scaricata
    macro = pd.read_csv(SERIE / "pil_mld_eur.csv")
    pil25 = macro[(macro.geo == "IT") & (macro.time == 2025)].valore.item()
    print(f"PIL 2025 Eurostat {pil25:,.0f} mln vs DPFP {pil[2025]:,.0f} mln")
    fsn_pil(pil)
    aifa()
