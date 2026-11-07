"""Area 01 - Economia, Imprese, Turismo: serie e documenti usati per verificare il dossier.

Uso (dalla cartella dati/script):  python 01_economia.py
Scarica le serie Eurostat e i documenti ufficiali (PDF) in dati/raw/, estrae le cifre
citate nel dossier controllando che compaiano testualmente nel documento, e registra
tutto in dati/serie/_registro_01.csv.

Nota su fonti.py: eurostat() non conserva i flag di stato (p = provvisorio, b = rottura
di serie). Per le presenze turistiche 2025 lo segnaliamo a mano nella nota.
"""
from __future__ import annotations

import re

import pandas as pd
import pypdf

from fonti import eurostat, salva, scarica

AREA = "01"


def ultimo(df, geo="IT", **filtri):
    d = df[df.geo == geo]
    for k, v in filtri.items():
        d = d[d[k] == v]
    r = d.sort_values("time").tail(1)
    return r.time.item(), r.valore.item()


# --- 1. Serie Eurostat -------------------------------------------------------

# Pressione fiscale (imposte + contributi sociali, % PIL). ISTAT pubblica 42,9% per il 2025
# (definizione nazionale); Eurostat 43,0%.
pf = eurostat("gov_10a_taxag", since="2005", geo=["IT", "EU27_2020"], unit="PC_GDP",
              sector="S13_S212", na_item="D2_D5_D91_D61_M_D995")
salva(pf, "01_pressione_fiscale_pil", "Eurostat gov_10a_taxag (D2_D5_D91_D61_M_D995)", pf.attrs["url"],
      "Pressione fiscale, % PIL. Definizione Eurostat, può differire di 0,1 pp da ISTAT", AREA)

# Stock del debito e spesa per interessi in milioni di euro
deb = eurostat("gov_10dd_edpt1", since="2015", geo="IT", unit="MIO_EUR", na_item="GD", sector="S13")
salva(deb, "01_debito_mio_eur", "Eurostat gov_10dd_edpt1 (GD, MIO_EUR)", deb.attrs["url"],
      "Debito lordo PA (Maastricht), milioni di euro", AREA)
inte = eurostat("gov_10a_main", since="2015", geo="IT", unit="MIO_EUR", na_item="D41PAY", sector="S13")
salva(inte, "01_interessi_mio_eur", "Eurostat gov_10a_main (D41PAY, MIO_EUR)", inte.attrs["url"],
      "Spesa per interessi PA, milioni di euro", AREA)

# Produttività: PIL reale per ora lavorata (proxy riproducibile; ISTAT usa il valore aggiunto
# per ora lavorata con un campo di osservazione più ristretto)
lp = eurostat("nama_10_lp_ulc", since="1995", geo=["IT", "EU27_2020"], unit="I15", na_item="RLPR_HW")
salva(lp, "01_produttivita_ora_i15", "Eurostat nama_10_lp_ulc (RLPR_HW, I15)", lp.attrs["url"],
      "PIL reale per ora lavorata, indice 2015=100", AREA)
cagr = {}
for g in ["IT", "EU27_2020"]:
    s = lp[lp.geo == g].set_index("time").valore
    cagr[g] = ((s["2024"] / s["1995"]) ** (1 / 29) - 1) * 100

# Occupazione per classe di addetti (SBS): quota micro e piccole imprese (0-49 addetti)
sbs = eurostat("sbs_sc_ovw", since="2021", geo=["IT", "FR", "DE"], indic_sbs="EMP_NR", nace_r2="B-S_X_O_S94")
anno = sbs.time.max()
quote = []
for g in ["IT", "FR", "DE"]:
    d = sbs[(sbs.geo == g) & (sbs.time == anno)].set_index("size_emp").valore
    quote.append({"geo": g, "time": anno, "quota_0_49": round(100 * d[["0-9", "10-19", "20-49"]].sum() / d["TOTAL"], 1),
                  "quota_0_9": round(100 * d["0-9"] / d["TOTAL"], 1)})
quote = pd.DataFrame(quote)
salva(sbs, "01_occupati_classe_addetti", "Eurostat sbs_sc_ovw (EMP_NR)", sbs.attrs["url"],
      "Occupati per classe di addetti, economia di mercato esclusi servizi finanziari", AREA)
q = quote.copy(); q.attrs["aggiornato"] = sbs.attrs.get("aggiornato")
salva(q, "01_quota_occupati_micro_piccole", "Elaborazione su Eurostat sbs_sc_ovw", sbs.attrs["url"],
      "Quota % occupati in imprese 0-49 e 0-9 addetti", AREA)

# Turismo: presenze negli esercizi ricettivi
tur = eurostat("tour_occ_ninat", since="2019", geo="IT", unit="NR", nace_r2="I551-I553", c_resid=["TOTAL", "FOR"])
salva(tur, "01_presenze_turistiche", "Eurostat tour_occ_ninat (dati ISTAT)", tur.attrs["url"],
      "Presenze (notti) negli esercizi ricettivi. 2025: forte salto (+15%), possibile discontinuità di campo "
      "di osservazione (ISTAT: dato 2025 al netto degli alloggi privati non imprenditoriali)", AREA)
try:
    sar = eurostat("tour_occ_nin2", since="2019", geo="ITG2", unit="NR", nace_r2="I551-I553", c_resid="TOTAL")
    salva(sar, "01_presenze_sardegna", "Eurostat tour_occ_nin2 (ITG2)", sar.attrs["url"], "Presenze Sardegna", AREA)
    sard = ultimo(sar, geo="ITG2")
except Exception as e:  # dataset regionale non sempre disponibile
    sard = ("n.d.", str(e))

# --- 2. Documenti ufficiali: download ed estrazione controllata ---------------

DOC = {
    "dpb": ("01_mef_dpb_2027.pdf", "https://www.mef.gov.it/export/sites/MEF/inevidenza/2026/article_00393/Italys-DBP-2027.pdf",
            "MEF, Documento programmatico di bilancio 2027 (13/10/2026)"),
    "eva": ("01_mef_relazione_evasione_2026.pdf",
            "https://www.mef.gov.it/export/sites/MEF/inevidenza/2026/article_00390/Relazione-evasione-fiscale-e-contributiva-2026_09_30.pdf",
            "MEF, Relazione sull'economia non osservata e sull'evasione fiscale e contributiva 2026"),
    "rsf": ("01_mef_rapporto_spese_fiscali_2025.pdf", "https://www.mef.gov.it/export/sites/MEF/documenti-allegati/2025/RSF-2025-bis.pdf",
            "MEF, Rapporto annuale sulle spese fiscali 2025 (giugno 2026)"),
    "upb": ("01_upb_focus_4_2024_cs.pdf", "https://www.upbilancio.it/wp-content/uploads/2024/04/Comunicato-stampa-Focus-4_2024.pdf",
            "UPB, Focus 4/2024, comunicato stampa"),
    "prod": ("01_istat_produttivita_2024.pdf", "https://www.istat.it/wp-content/uploads/2025/12/REPORT_PRODUTTIVITA_2024.pdf",
             "ISTAT, Misure di produttività 1995-2024 (dicembre 2025)"),
    "eno": ("01_istat_eno_2023.pdf", "https://www.istat.it/wp-content/uploads/2025/10/Report-ECONOMIA-NON-OSSERVATA-NEI-CONTI-NAZIONALI_ANNO2023.pdf",
            "ISTAT, Economia non osservata nei conti nazionali 2023 (ottobre 2025)"),
}
testi = {}
for k, (nome, url, _) in DOC.items():
    try:
        p = scarica(url, nome)
        t = "\n".join(pg.extract_text() or "" for pg in pypdf.PdfReader(p).pages)
        p.with_suffix(".txt").write_text(t, encoding="utf-8")
        testi[k] = re.sub(r"\s+", " ", t)
    except Exception as e:
        print(f"ATTENZIONE: {nome} non scaricato ({e})")
        testi[k] = ""

# (documento, dato, valore, frase da trovare nel testo)
ESTRATTI = [
    ("dpb", "Debito/PIL 2025-2029 (%)", "136,7 / 138,1 / 138,5 / 137,9 / 136,6", "Debito lordo (1) 136,7 138,1 138,5 137,9 136,6"),
    ("dpb", "Debito lordo 2025 (mln EUR)", "3.097.093", "Debito lordo (2) 3.097.093"),
    ("dpb", "Indebitamento netto 2025/2026/2027 (% PIL)", "-3,1 / -2,9 / -3,4", "-69.736 -3,1 -2,9 -3,4"),
    ("dpb", "Spesa per interessi 2025/2026/2027 (% PIL)", "3,8 / 4,2 / 4,3", "Spesa per interessi D.41 87.158 3,8 4,2 4,3"),
    ("dpb", "Clausola nazionale: 0,3 difesa + 0,3 energia = 0,6 pp su limite 1,5", "0,6", "può quindi raggiungere 0,6 punti percentuali"),
    ("dpb", "Stima debito/PIL 2026 di primavera (DFP)", "138,6", "quello stimato in primavera (138,6 per cento)"),
    ("dpb", "Impatto complessivo manovra su indebitamento 2027 (% PIL)", "-0,54", "IMPATTO COMPLESSIVO -0,54 -0,56 -0,15"),
    ("eva", "Tax gap complessivo 2023 (mld)", "107,9-112,8", "compreso fra 107,9 e 112,8 miliardi"),
    ("eva", "Gap IVA 2019-2023 (mln)", "31.766 28.473 29.915 30.736 34.355", "IVA 31.766 28.473 29.915 30.736 34.355"),
    ("rsf", "Numero spese fiscali erariali (RSF 2025)", "573", "censisce 573 misure"),
    ("rsf", "Effetti spese fiscali 2026/2027/2028 (mld)", "129,7 / 104,8 / 87,6", "Totale complessivo 573 -129.749,4 -104.760,1 -87.625,0"),
    ("rsf", "Obiettivo PSBMT riordino spese fiscali (mld)", "7,37", "pari a 7,37 miliardi di euro a fronte di un benchmark pari a 49,1"),
    ("rsf", "Target PNRR/REPowerEU riduzione SAD (mld, anticipato al 2026)", "4,5", "rideterminato in 4,5 miliardi"),
    ("upb", "Spese fiscali UPB 2018 -> 2024", "466 -> 625; 54 -> 105 mld", "passando da 466 a 625"),
    ("prod", "Produttività lavoro 1995-2024 IT vs UE27 (% medio annuo)", "+0,3 vs +1,5", "Italia ( +0,3%) è stata"),
    ("prod", "Produttività lavoro 2024 e 2023 (%)", "-1,9 / -2,7", "Nel 2024 la produttività del lavoro diminuisce dell’1,9%"),
    ("eno", "Economia non osservata 2023 (mld; % PIL)", "217,5; 10,2%", "si è attestato a 217,5 miliardi"),
]
righe = []
for k, dato, valore, frase in ESTRATTI:
    trovato = re.sub(r"\s+", " ", frase) in testi[k] or re.sub(r"\s+", "", frase) in testi[k].replace(" ", "")
    righe.append({"dato": dato, "valore": valore, "documento": DOC[k][2], "url": DOC[k][1],
                  "file_raw": DOC[k][0], "verificato_nel_testo": trovato})
estr = pd.DataFrame(righe)
salva(estr, "01_estratti_documenti", "Documenti ufficiali MEF, UPB, ISTAT (vedi colonna url)", "vari: colonna url",
      "Cifre estratte dai PDF in dati/raw/; verificato_nel_testo=True se la frase compare nel PDF", AREA)

# --- 3. Riepilogo ------------------------------------------------------------
print("Pressione fiscale IT", ultimo(pf))
print("Debito IT mln", ultimo(deb), "| Interessi IT mln", ultimo(inte))
print(f"Produttività/ora CAGR 1995-2024: IT {cagr['IT']:.2f}%  UE27 {cagr['EU27_2020']:.2f}%")
print(quote.to_string(index=False))
print(tur.pivot(index="time", columns="c_resid", values="valore").to_string())
print("Sardegna", sard)
print(estr[["dato", "verificato_nel_testo"]].to_string(index=False))
