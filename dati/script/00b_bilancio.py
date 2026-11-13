"""00b - Vincolo di bilancio comune di GovernAI.

Scarica i documenti ufficiali usati per il vincolo (DPB 2027, DPFP 2026, DDL bilancio 2027,
audizione UPB sul DPFP 2026, dossier Camera sul Rendiconto 2025), i dati aperti del
Rendiconto 2025 per capitolo (OpenBDAP-RGS) e lo stato di attuazione della coesione 2021-27
(Commissione UE, Cohesion Open Data). Controlla che le cifre trascritte compaiano davvero nei
PDF, salva le serie in dati/serie/00b_*.csv e scrive registro/vincolo.csv e registro/fondi.csv.

Esecuzione:  python 00b_bilancio.py   (dalla cartella dati/script)
"""
from __future__ import annotations

import csv
import io
import re
import sys
from pathlib import Path

import pandas as pd
import requests

from fonti import HEADERS, RAW, salva, scarica

AREA = "00b"
REGISTRO = Path(__file__).resolve().parents[2] / "registro"

DOC = {
    "00b_mef_dpb_2027.pdf": "https://www.mef.gov.it/export/sites/MEF/inevidenza/2026/article_00393/Italys-DBP-2027.pdf",
    "00b_mef_dpfp_2026.pdf": "https://www.mef.gov.it/export/sites/MEF/inevidenza/2026/article_00390/DPFP26.pdf",
    "00b_ddl_bilancio_2027_AC3174_relazioni.pdf": "https://documenti.camera.it/leg19/pdl/pdf/leg.19.pdl.camera.3174.19PDL0221140.pdf",
    "00b_upb_audizione_dpfp_2026.pdf": "https://www.upbilancio.it/wp-content/uploads/2026/10/UPB-Audizione-DPFP-2026.pdf",
    "00b_camera_dossier_rendiconto_2025_BI0295.pdf": "https://documenti.camera.it/leg19/dossier/Pdf/BI0295.pdf",
}
URL_RND = "https://bdap-opendata.rgs.mef.gov.it/SpodCkanApi/api/3/datastore/dump/a7625ae5-79f7-41c5-b7ca-2e45dc40ea21.csv"
URL_COES = "https://cohesiondata.ec.europa.eu/resource/3git-md5z.json"

# Cifre trascritte dai PDF: (file, frase attesa). Il controllo ignora spazi e a-capo.
CONTROLLI = [
    ("00b_mef_dpb_2027.pdf", "pari a 1,9 per cento nel 2027, 1,7 per cento nel 2028 e 1,5 per cento nel 2029"),
    ("00b_mef_dpb_2027.pdf", "pari al 3,3 per cento nel 2027, all'1,7 per cento nel 2028 e allo 0,2 per cento nel 2029"),
    ("00b_mef_dpb_2027.pdf", "IMPATTO COMPLESSIVO -0,54 -0,56 -0,15"),
    ("00b_mef_dpb_2027.pdf", "4. Debito lordo (1) 136,7 138,1 138,5 137,9 136,6"),
    ("00b_mef_dpb_2027.pdf", "1. Accreditamento/indebitamento netto -3,1 -2,9 -3,4 -3,2 -2,3"),
    ("00b_mef_dpb_2027.pdf", "Revisione spesa ministeri no s 0,05 0,08 0,08"),
    ("00b_mef_dpb_2027.pdf", "Misure a carico del settore finanziario no e 0,21 0,13 0,10"),
    ("00b_mef_dpfp_2026.pdf", "a fine periodo il tasso di crescita cumulato si attesta al"),
    ("00b_upb_audizione_dpfp_2026.pdf", "permarrebbe una deviazione cumulata pari a 0,1 punti percentuali di PIL"),
    ("00b_upb_audizione_dpfp_2026.pdf", "nel 2027 non vi sono spazi di bilancio oltre alle"),
    ("00b_upb_audizione_dpfp_2026.pdf", "I margini consentiti dal percorso di spesa netta sarebbero utilizzati per intero"),
    ("00b_upb_audizione_dpfp_2026.pdf", "pari a circa 29 miliardi nel biennio"),
    ("00b_camera_dossier_rendiconto_2025_BI0295.pdf", "passivi per 197.198,6 milioni"),
    ("00b_camera_dossier_rendiconto_2025_BI0295.pdf", "residui di stanziamento (113,6 miliardi"),
    ("00b_ddl_bilancio_2027_AC3174_relazioni.pdf", "incrementa di 520 milioni di euro per l'anno"),
    ("00b_ddl_bilancio_2027_AC3174_relazioni.pdf", "Anche per il 2027 si stanziano risorse pari a 1,9 miliardi"),
    ("00b_ddl_bilancio_2027_AC3174_relazioni.pdf", "TOTALE                  112,19"),
]


def testo_pdf(path: Path) -> str:
    """Estrae il testo con PyMuPDF; lo salva accanto al PDF (.txt)."""
    import pymupdf  # PyMuPDF
    with pymupdf.open(path) as doc:
        t = "\n".join(p.get_text() for p in doc)
    path.with_suffix(".txt").write_text(t, encoding="utf-8")
    return t


def _norm(s: str) -> str:
    s = s.replace("’", "'").replace("‘", "'")
    return re.sub(r"\s+", "", s)


def scarica_documenti() -> dict[str, str]:
    testi = {}
    for nome, url in DOC.items():
        p = RAW / nome
        try:
            if not p.exists():
                scarica(url, nome)
            testi[nome] = testo_pdf(p)
            print(f"OK  {nome}")
        except Exception as e:  # sito che blocca: segnalare, non fermarsi
            print(f"ERR {nome}: {e}")
    return testi


def controlla(testi: dict[str, str]) -> None:
    ok = 0
    for nome, frase in CONTROLLI:
        t = testi.get(nome)
        trovata = t is not None and _norm(frase) in _norm(t)
        ok += trovata
        print(f"  [{'OK' if trovata else '??'}] {nome}: {frase[:70]}")
    print(f"Controlli cifre nei PDF: {ok}/{len(CONTROLLI)} trovati")


# --- Rendiconto 2025 per capitolo (OpenBDAP) --------------------------------

def residui_ministeri() -> pd.DataFrame:
    dest = RAW / "00b_openbdap_rendiconto_2025_spese_capitolo.csv"
    if not dest.exists():
        r = requests.get(URL_RND, headers=HEADERS, timeout=300)
        r.raise_for_status()
        dest.write_bytes(r.content)
    d = pd.read_csv(dest, sep=";", encoding="latin1", dtype=str)
    num = list(d.columns[20:])
    for c in num:
        d[c] = pd.to_numeric(d[c], errors="coerce")
    d = d[d["Codice Titolo"] != "3"]  # esclude rimborso passività finanziarie
    g = d.groupby("Amministrazione").agg(
        residui_passivi_31_12=("RS al 31/12", "sum"),
        rimasto_da_pagare_residui_pregressi=("Rimasto da Pagare RS", "sum"),
        rimasto_da_pagare_competenza=("Rimasto da Pagare CP", "sum"),
        stanziamenti_definitivi_cp=("Previsioni Definitive CP", "sum"),
        impegni_cp=("Totale CP", "sum"),
        economie_cp=("Economie-Maggiori Spese CP", "sum"),
    ) / 1e9
    g["economie_cp"] = -g["economie_cp"]
    g = g.round(3).sort_values("residui_passivi_31_12", ascending=False).reset_index()
    g.loc[len(g)] = ["TOTALE (Titoli I e II)"] + list(g.iloc[:, 1:].sum().round(3))
    g.attrs["url"] = URL_RND
    return g


# --- Coesione 2021-27 (Cohesion Open Data, UE) ------------------------------

def coesione_2127() -> pd.DataFrame:
    q = {
        "$select": "tod_cycle,fund,sum(total_amount) as programmato,"
                   "sum(total_eligiblecost_of_selectedoperations) as selezionato,"
                   "sum(totalspendeligibleexpenditure_declared) as speso",
        "ms": "IT", "dimension_type": "Intervention Field",
        "$group": "tod_cycle,fund", "$order": "tod_cycle,fund", "$limit": "5000",
    }
    r = requests.get(URL_COES, params=q, headers=HEADERS, timeout=120)
    r.raise_for_status()
    df = pd.DataFrame(r.json())
    for c in ("programmato", "selezionato", "speso"):
        df[c] = pd.to_numeric(df[c]) / 1e9
    df = df.round(3)
    df.attrs["url"] = r.url
    return df


# --- Quadro programmatico (trascritto dai documenti, controllato sopra) -----

PIL_2025 = 2265.002          # mld, DPB/DPFP Tav. I.3.3
CRESCITA_PIL_NOM = {2026: 2.7, 2027: 3.2, 2028: 3.0, 2029: 2.6}   # programmatico, DPFP Tav. I.3.3

TETTO = {2025: 1.3, 2026: 1.6, 2027: 1.9, 2028: 1.7, 2029: 1.5}         # Raccomandazione Consiglio 21/1/2025
TETTO_CUM = {2025: -0.7, 2026: 0.9, 2027: 2.8, 2028: 4.6, 2029: 6.2}     # DPFP Tav. II.1.5
PROG = {2025: 1.5, 2026: 1.6, 2027: 3.3, 2028: 1.7, 2029: 0.2}          # DPB Tab. III.1-1
PROG_NEC = {2025: 1.5, 2026: 1.6, 2027: 1.9, 2028: 1.7, 2029: 1.5}      # DPB Tab. III.1-1 (netto clausola)
TEND = {2027: 2.1, 2028: 1.3, 2029: 1.1}                                # DPB par. I.4
DEFICIT = {2025: -3.1, 2026: -2.9, 2027: -3.4, 2028: -3.2, 2029: -2.3}  # DPB Tab. III.1-2
DEBITO = {2025: 136.7, 2026: 138.1, 2027: 138.5, 2028: 137.9, 2029: 136.6}
DEV_CUM_UPB = {2024: 0.0, 2025: 0.1, 2026: 0.1, 2027: 0.1}              # UPB tab. 4.4, % PIL dopo flessibilità

# DPB Tab. I.6-1, % PIL (impieghi negativi = maggior deficit)
IMPIEGHI = {2027: 0.98, 2028: 0.99, 2029: 0.65}
RISORSE = {2027: 0.43, 2028: 0.45, 2029: 0.50}
NETTO = {2027: -0.54, 2028: -0.56, 2029: -0.15}

F_DPB = "MEF, Documento programmatico di bilancio 2027 (13/10/2026), " + DOC["00b_mef_dpb_2027.pdf"]
F_DPFP = "MEF, DPFP 2026 (2/10/2026), Tav. II.1.5, " + DOC["00b_mef_dpfp_2026.pdf"]
F_UPB = "UPB, Audizione sul DPFP 2026 (12/10/2026), par. 3.1.1 e 4.3, " + DOC["00b_upb_audizione_dpfp_2026.pdf"]
F_DDL = "Camera, A.C. 3174 DDL bilancio 2027, Relazione illustrativa e tecnica (30/10/2026), " + DOC["00b_ddl_bilancio_2027_AC3174_relazioni.pdf"]
F_RND = "Camera, Dossier BI0295 Rendiconto 2025 (Corte dei conti, parifica 24/6/2026), " + DOC["00b_camera_dossier_rendiconto_2025_BI0295.pdf"]

# Politiche invariate: misure del DDL 2027 limitate al 2027 (o al 2027-28) che andrebbero rinnovate.
# Importi dalla Relazione illustrativa A.C. 3174, cap. I; "annuo" = stima GovernAI del costo di un anno di rinnovo.
POLITICHE_INVARIATE = [
    ("IRPEF: secondo scaglione esteso a 55.000 euro (solo 2027)", 1.4, "1,4 mld nel triennio per un solo anno d'imposta"),
    ("Imposta sostitutiva 15% trattamento accessorio PA (solo 2027)", 0.4, "0,4 mld nel triennio"),
    ("Imposta sostitutiva 15% notturno/festivo privati (solo 2027)", 0.3, "0,3 mld nel triennio"),
    ("Imposta sostitutiva 5% su aumenti da rinnovi contrattuali (solo 2027)", 1.0, "1 mld nel triennio"),
    ("Imposta 1% su redditi incrementali under 30 (solo 2027)", 0.4, "0,4 mld nel triennio"),
    ("Forfettario: soglia reddito dipendente 35.000 euro (solo 2027)", 0.3, "quota GovernAI dell'1 mld triennale comprensivo della soglia 100.000 permanente"),
    ("Proroga detrazioni edilizie 50/36% e bonus mobili (solo 2027)", 0.5, "1,5 mld nel triennio; la detrazione si ripartisce in 10 anni, il costo di ogni proroga cresce"),
    ("Esenzione IRPEF redditi agrari (solo 2027)", 0.1, "0,13 mld nel 2028-29"),
    ("Carta 300 euro over 75 e proroga prestazione universale (solo 2027)", 1.8, "1,8 mld nel 2027"),
    ("Ape sociale accessi 2027", 0.3, "0,9 mld nel triennio, costo per coorte che si cumula"),
    ("Credito d'imposta ZES unica", 1.4, "1,4 mld nel 2027, 0,5 nel 2028"),
    ("Sostegno temporaneo al costo dell'energia delle imprese (2027-28)", 1.7, "3,4 mld nel biennio"),
    ("Esonero contributivo assunzioni 2027", 0.3, "0,65 mld nel triennio, costo per coorte che si cumula"),
    ("Missioni internazionali (fondo l. 145/2016)", 0.8, "520 mln nel 2027, 804 mln nel 2028; art. 95"),
    ("Fondo contenziosi nazionali ed europei", 1.9, "1,9 mld anche per il 2027, rifinanziato ogni anno"),
]


def pil(anno: int) -> float:
    v = PIL_2025
    for a in range(2026, anno + 1):
        v *= 1 + CRESCITA_PIL_NOM[a] / 100
    return v


def scrivi_vincolo(res: pd.DataFrame) -> pd.DataFrame:
    R = []
    add = lambda voce, anno, val, unita, fonte, note="": R.append(dict(voce=voce, anno=anno, valore=val, unita=unita, fonte=fonte, note=note))
    for a in range(2026, 2030):
        add("pil_nominale_programmatico", a, round(pil(a), 1), "mld_eur", "calcolo GovernAI su DPFP 2026 Tav. I.3.3 (PIL 2025 = 2.265,0 mld e crescite nominali programmatiche)")
    for a in TETTO:
        add("tetto_crescita_spesa_netta", a, TETTO[a], "pct_annuo", "Raccomandazione del Consiglio UE 21/1/2025 (PSB 2025-29), riportata in " + F_DPB, "limite massimo annuo; vincolante anche ai fini della PDE")
        add("tetto_crescita_spesa_netta_cumulata", a, TETTO_CUM[a], "pct_dal_2023", F_DPFP)
        add("crescita_spesa_netta_programmata", a, PROG[a], "pct_annuo", F_DPB, "include le spese finanziate con la clausola nazionale (NEC)")
        add("crescita_spesa_netta_programmata_netto_NEC", a, PROG_NEC[a], "pct_annuo", F_DPB, "uguale al tetto in ogni anno 2026-29: nessun margine")
    for a in TEND:
        add("crescita_spesa_netta_tendenziale", a, TEND[a], "pct_annuo", F_DPB, "legislazione vigente, prima della manovra")
    add("crescita_spesa_netta_cumulata_netto_NEC", 2029, 6.6, "pct_dal_2023", F_UPB, "contro 6,2% raccomandato: lo scostamento 2024-25 non viene riassorbito")
    for a, v in DEV_CUM_UPB.items():
        add("conto_controllo_deviazione_cumulata", a, v, "pct_pil", F_UPB, "saldo a debito; soglia di tolleranza 0,3 annua e 0,6 cumulata. UPB: resta 0,1 fino al 2029")
    add("conto_controllo_deviazione_cumulata", 2027, round(0.1 * pil(2027) / 100, 1), "mld_eur", "calcolo GovernAI: 0,1% x PIL 2027", "prima della flessibilità NEC sarebbe 0,7% del PIL")
    add("clausola_NEC_difesa", 2027, 0.3, "pct_pil", F_DPB, "anche 2028; limite UE 1,5% PIL annuo")
    add("clausola_NEC_energia", 2027, 0.3, "pct_pil", F_DPB, "anche 2028; tetto UE 0,3 annuo e 0,6 complessivo")
    add("clausola_NEC_totale_biennio", "2027-2028", 29, "mld_eur", F_UPB, "0,6% PIL l'anno, flessibilità interamente usata; dal 2029 non c'è più, ma la UE chiede di mantenere il livello della spesa per la difesa")
    for a in DEFICIT:
        add("indebitamento_netto_programmatico", a, DEFICIT[a], "pct_pil", F_DPB + " Tab. III.1-2", "al netto della NEC il DPB lo stima sotto il 3% in tutto l'orizzonte")
        add("debito_pil_programmatico", a, DEBITO[a], "pct_pil", F_DPB + " Tab. III.1-2")
    add("spesa_interessi", 2027, 4.3, "pct_pil", F_DPB + " Tab. III.1-5", "4,6-4,7% nel 2029 secondo UPB")
    for a in IMPIEGHI:
        p = pil(a)
        add("manovra_impieghi", a, round(IMPIEGHI[a] * p / 100, 1), "mld_eur", F_DPB + " Tab. I.6-1", f"{IMPIEGHI[a]}% PIL; calcolo GovernAI in mld")
        add("manovra_coperture", a, round(RISORSE[a] * p / 100, 1), "mld_eur", F_DPB + " Tab. I.6-1", f"{RISORSE[a]}% PIL; settore finanziario, revisione spesa ministeri, giochi, altre entrate")
        add("manovra_impatto_netto_deficit", a, round(NETTO[a] * p / 100, 1), "mld_eur", F_DPB + " Tab. I.6-1", f"{NETTO[a]}% PIL")
    p27 = pil(2027)
    for voce, pct in [("copertura_settore_finanziario", 0.21), ("copertura_revisione_spesa_ministeri", 0.05),
                      ("copertura_giochi", 0.03), ("copertura_altre_entrate", 0.07), ("copertura_altre_spese", 0.07)]:
        add(voce, 2027, round(pct * p27 / 100, 1), "mld_eur", F_DPB + " Tab. I.6-1", f"{pct}% PIL")
    tot_pi = round(sum(v for _, v, _ in POLITICHE_INVARIATE), 1)
    for nome, v, nota in POLITICHE_INVARIATE:
        add("politica_invariata: " + nome, 2028, v, "mld_eur_anno", F_DDL, "stima GovernAI del costo annuo di rinnovo; " + nota)
    add("costo_politiche_invariate_totale", 2028, tot_pi, "mld_eur_anno", "stima GovernAI su " + F_DDL,
        "range prudente 10-14 mld; non include rinnovi contrattuali PA 2028-30 (non quantificati) né il mantenimento della spesa per la difesa dopo la NEC")
    add("costo_mantenimento_difesa_post_NEC", 2029, round(0.3 * pil(2029) / 100, 1), "mld_eur_anno", "calcolo GovernAI: 0,3% PIL 2029; impegno UE richiamato da " + F_UPB,
        "da assorbire entro il tetto dal 2029; il DPB programma crescita della spesa netta dello 0,2% nel 2029")
    tot = res[res.Amministrazione.str.startswith("TOTALE")].iloc[0]
    add("residui_passivi_totali", 2025, 197.2, "mld_eur", F_RND, "195,2 al netto del rimborso prestiti; 113,6 residui di stanziamento, 83,6 residui propri; perenti 46,3")
    add("economie_di_competenza", 2025, round(tot.economie_cp, 1), "mld_eur", "OpenBDAP-RGS, Rendiconto 2025 per capitolo, " + URL_RND, "Titoli I e II; risorse non impegnate e decadute: già fuori dai tendenziali")
    for a in (2027, 2028, 2029):
        add("margine_residuo_spesa_netta", a, 0.0, "mld_eur", "UPB audizione DPFP 2026; DPB 2027", "il percorso netto NEC coincide con il tetto; con la deviazione cumulata 0,1% PIL il margine è di fatto negativo (circa -2,4 mld)")
    df = pd.DataFrame(R)
    df.to_csv(REGISTRO / "vincolo.csv", index=False, quoting=csv.QUOTE_MINIMAL, encoding="utf-8")
    return df


# --- Fondi ------------------------------------------------------------------
INF = float("inf")
FONDI = [
    # fondo_id, descrizione, cap_min, cap_max, gia_impegnato, natura, certificazione, in_bilancio, fonte, note
    ("SAD", "Riforma dei sussidi ambientalmente dannosi riformabili a livello nazionale", 2.0, 8.0, 4.5, "permanente", "no", "si",
     "MASE, Catalogo SAD/SAF VIII ed. (14/7/2026), https://www.camera.it/temiap/2026/07/16/OCD177-9133.pdf; verifica 03_ambiente.md; MEF RSF 2025 (target PNRR)",
     "stima GovernAI: riforma graduale (5-7 anni) di parte dei 17,1 mld riformabili; i valori del Catalogo sono teorici a comportamento invariato. Gia_impegnato = target PNRR/REPowerEU di 4,5 mld, che include l'allineamento accise gasolio/benzina (L. 199/2025). È una DRM: crea spazio sul tetto. Conflitto aperto: dividendo ai cittadini o servizi"),
    ("SPESE_FISCALI", "Riordino delle spese fiscali oltre quanto già previsto nel Piano strutturale di bilancio", 0.0, 3.0, 7.37, "permanente", "no", "si",
     "MEF, Rapporto spese fiscali 2025 (giugno 2026), https://www.mef.gov.it/export/sites/MEF/documenti-allegati/2025/RSF-2025-bis.pdf; verifica 01_economia.md",
     "stima GovernAI per la parte oltre i 7,37 mld già contati nel PSB. Le spese fiscali scendono da 129,7 (2026) a 87,6 mld (2028) per la scadenza dei bonus edilizi: la base residua è più rigida. DRM: crea spazio sul tetto"),
    ("ETS", "Proventi aste ETS (sistema attuale)", 0.0, 0.3, 2.6, "permanente", "no", "si",
     "GSE, Rapporto aste CO2 2025; d.lgs. 47/2020 art. 23; verifica 03_ambiente.md",
     "2.598,6 mln nel 2025 tutti già destinati per legge e nei tendenziali. Solo la quota MASE (circa 0,65 mld) è riprogrammabile tra finalità climatiche, ed è in parte già usata (DM MASE 266/2026). Ogni altro uso toglie risorse al fondo ammortamento titoli (effetto equivalente sul deficit)"),
    ("ETS2_FSC", "Proventi ETS2 e Fondo sociale per il clima (dal 2027-28)", 0.0, 1.0, 1.3, "temporanea", "no", "si",
     "MASE, Piano sociale per il clima approvato dal CdM il 4/8/2026: 9,3 mld 2026-32 (7 UE + 2,3 cofinanziamento), via QualEnergia/Teleborsa; GSE (avvio ETS2 rinviato al 2028)",
     "gia_impegnato = 9,3 mld del Piano sociale per il clima ripartiti su 7 anni (circa 1,3/anno), già programmati. Capienza nuova = stima GovernAI della quota nazionale dei proventi ETS2 dal 2028, vincolata a finalità climatiche e sociali e in parte necessaria per il cofinanziamento. Spesa finanziata dalla UE esclusa dalla spesa netta; quella da proventi nazionali no"),
    ("IVA_EVASIONE", "Recupero dell'evasione IVA, solo dopo certificazione", 0.0, 6.9, 0.0, "incerta", "si", "si",
     "MEF, Relazione evasione 2026 (gap IVA 34,4 mld nel 2023); verifica 01_economia.md (15-20% del gap = 5,2-6,9 mld)",
     "copre solo ex post e dopo certificazione. Le maggiori entrate da contrasto all'evasione sono già in parte usate come copertura dal DDL 2027 e per legge affluiscono al fondo per la riduzione della pressione fiscale (non quantificato qui). Un maggior gettito da adempimento non è una DRM: riduce il deficit ma di norma non crea spazio sul tetto alla spesa netta"),
    ("FSN", "Incremento programmato del Fondo sanitario nazionale", 0.0, 0.5, 2.4, "permanente", "no", "si",
     "DDL bilancio 2027 A.C. 3174 art. 69 c. 1 (+2.365/2.352/2.399 mln); Camera, tema Organizzazione SSN; verifica 06_salute.md",
     "FSN 142,9 (2026) -> 146,3 (2027) -> 147,2 (2028) -> 148,2 (2029, non verificato). L'incremento del DDL è già destinato (tariffe ospedaliere, Alzheimer, liste d'attesa 300 mln, indennità di primo soccorso, tetti farmaceutica). Dopo il 2027 la crescita è inferiore a 1 mld/anno. Capienza nuova: stima GovernAI, quasi nulla. Ogni proposta sanitaria è nuova spesa da coprire"),
    ("COESIONE_2127", "Risorse coesione 2021-27 (FESR, FSE+, JTF) non ancora selezionate", 2.0, 5.0, 47.4, "una_tantum", "no", "si",
     "Commissione UE, Cohesion Open Data 3git-md5z (ciclo ago. 2026): programmato 75,8 mld, operazioni selezionate 47,4, spesa dichiarata 14,3; https://cohesiondata.ec.europa.eu/resource/3git-md5z.json",
     "circa 28,5 mld non ancora selezionati (stock, non flusso). Capienza annua 2027-29 = stima GovernAI della quota riprogrammabile verso finalità del programma, entro i vincoli UE (obiettivi, regioni, n+3, spesa entro il 2029-30). Spesa finanziata dalla UE e cofinanziamento esclusi dalla spesa netta. Solo spesa una tantum, non personale stabile. FSC nazionale 2021-27 non incluso (già assegnato con gli Accordi per la coesione)"),
    ("COESIONE_2834", "Risorse coesione del prossimo ciclo (QFP 2028-34)", 0.0, 3.0, 0.0, "incerta", "no", "si",
     "Commissione UE, proposta QFP 2028-34 (Fondo piani di partenariato 865 mld); stima IFEL per l'Italia 86,6 mld inclusa la PAC (fonte secondaria)",
     "stima GovernAI. Negoziato non concluso; la cifra italiana include PAC e Fondo clima ed è quindi in gran parte già prenotata. Spesa effettiva non prima del 2029. Nessun valore nei documenti di finanza pubblica"),
    ("PENSIONI", "Contributo di equità sulle pensioni più alte e risparmi dall'uscita dalle quote", 0.3, 1.0, 0.0, "permanente", "no", "si",
     "verifica 02_lavoro.md (C3: nessuna stima ufficiale); DDL bilancio 2027 (proroga solo Ape sociale, 0,9 mld nel triennio)",
     "stima GovernAI solo per il contributo di equità sulle pensioni alte. Il DDL 2027 non proroga le quote: il risparmio dall'uscita è già nel tendenziale, quindi non è una risorsa nuova (capienza 0). Il gettito di un contributo è una DRM"),
    ("TASSA_SOGGIORNO", "Gettito aggiuntivo della tassa di soggiorno (Comuni)", 0.1, 0.4, 1.0, "permanente", "no", "si",
     "gettito circa 1,0 mld nel 2024 e circa 1,2 mld stimati per il 2026 (Osservatorio JFC, IRPET; fonti non ufficiali)",
     "stima GovernAI dell'aumento da estensione e tariffe più alte. Entrata dei Comuni, vincolata al turismo e ai servizi locali: non finanzia spesa statale"),
    ("ACCISE_SALUTE", "Accise e tasse su prodotti nocivi (tabacco, bevande zuccherate)", 0.5, 1.5, 0.45, "permanente", "no", "si",
     "DDL bilancio 2027 art. 33 (accise tabacchi +112,2 mln nel 2027) e art. 40 (sugar tax dal 1/7/2027, circa 340 mln/anno); verifica 06_salute.md",
     "gia_impegnato = 0,11 accise tabacchi + 0,34 sugar tax (già nei saldi). Capienza nuova: stima GovernAI per ulteriori aumenti delle accise sui tabacchi verso i livelli UE più alti; il gettito cala nel tempo se i consumi scendono (effetto voluto). DRM"),
    ("RIORDINO_BONUS", "Riordino di bonus e carte frammentati", 0.3, 1.5, 0.0, "permanente", "no", "si",
     "DDL bilancio 2027, Relazione illustrativa (carta 300 euro over 75: 1.645 mln solo 2027; bonus mamme 0,8 mld/anno; voucher autonomi; Valore nuovi nati)",
     "stima GovernAI. Molti bonus sono già temporanei: la loro scadenza è già nel tendenziale e non è un risparmio. È un risparmio solo il taglio di bonus permanenti o la loro fusione in strumenti universali"),
    ("FONDI_UE", "Fondi UE a gestione diretta o prestiti (SAFE, AMIF, Horizon, BEI)", 0.0, 1.0, 8.0, "temporanea", "no", "no",
     "Commissione UE, piano SAFE italiano approvato il 13/10/2026 (poco più di 8 mld), via Eunews; verifica 08_esteri.md",
     "SAFE: prestito (è debito) solo per la difesa, già richiesto. Horizon, AMIF: bandi competitivi, non programmabili. Capienza = stima GovernAI. I prestiti BEI/SAFE aumentano il debito e la loro spesa conta nella spesa netta (salvo la NEC)"),
    ("RIALLOCAZIONE", "Riallocazione interna al bilancio del ministero", 0.5, 2.0, 1.2, "permanente", "no", "si",
     "OpenBDAP-RGS Rendiconto 2025 per capitolo (residui 195,2 mld; economie di competenza 38,6 mld); Camera dossier BI0295; DPB 2027 Tab. I.6-1 (revisione spesa ministeri 0,05% PIL nel 2027, 0,08% nel 2028-29)",
     "stima GovernAI. Gia_impegnato = revisione della spesa dei ministeri già usata dal DDL 2027. Spendere residui o stanziamenti che non si sarebbero spesi aumenta la spesa netta: non è copertura. Conta solo il taglio di spese che si sarebbero effettivamente fatte"),
    ("RISPARMI_ATTESI", "Risparmi attesi dalla misura stessa, non certificati", 0.0, INF, 0.0, "incerta", "si", "si",
     "—", "capienza teoricamente illimitata ma non ammessa come copertura ex ante (art. 81 Cost., L. 196/2009 art. 17): si usa solo dopo verifica. Va usata con prudenza nel saldo"),
    ("TARIFFE", "Copertura fuori bilancio (bollette, tariffe idriche)", 0.0, INF, 0.0, "incerta", "no", "no",
     "—", "fuori dal bilancio pubblico ma pagata da famiglie e imprese: va dichiarato l'effetto distributivo. Le componenti tariffarie regolate (ARERA) possono essere riclassificate nella PA da Eurostat"),
    ("DEFICIT", "Nuovo deficit, cioè debito", -2.4, 0.0, 0.0, "incerta", "no", "si",
     "UPB, Audizione DPFP 2026 par. 4.3 (deviazione cumulata 0,1% PIL fino al 2029); DPB 2027 Tab. III.1-1",
     "nessun margine: la crescita della spesa netta programmata, al netto della NEC, coincide con il tetto UE in ogni anno 2026-29 e resta una deviazione cumulata di circa 0,1% PIL (-2,4 mld). Nuova spesa in deficit significherebbe deviare dal percorso e mettere a rischio l'uscita dalla PDE. Unica eccezione giuridica: la NEC per la difesa ammette fino all'1,5% PIL, il Governo ne usa 0,3"),
    ("ALTRO", "Da specificare in note", 0.0, 0.0, 0.0, "incerta", "no", "si",
     "DPB 2027 Tab. I.6-1", "le misure sul settore finanziario (0,21% PIL nel 2027) e sui giochi (0,03%) sono già usate dal DDL 2027. Ogni altra fonte va dichiarata e verificata"),
]


def scrivi_fondi() -> pd.DataFrame:
    cols = ["fondo_id", "descrizione", "capienza_min", "capienza_max", "gia_impegnato", "natura",
            "certificazione", "in_bilancio", "fonte_dato", "note"]
    df = pd.DataFrame(FONDI, columns=cols)
    df.to_csv(REGISTRO / "fondi.csv", index=False, quoting=csv.QUOTE_MINIMAL, encoding="utf-8")
    return df


def main() -> None:
    testi = scarica_documenti()
    controlla(testi)

    try:
        res = residui_ministeri()
        salva(res, "00b_residui_ministeri_2025", fonte="OpenBDAP-RGS, Rendiconto 2025 pubblicato elaborabile, spese per capitolo",
              url=res.attrs["url"], nota="mld euro, Titoli I e II; economie_cp = stanziamenti di competenza non impegnati", area=AREA)
        print(res.head(16).to_string(index=False))
    except Exception as e:
        print("ERR OpenBDAP:", e)
        res = pd.DataFrame({"Amministrazione": ["TOTALE (Titoli I e II)"], "economie_cp": [38.6]})

    try:
        co = coesione_2127()
        salva(co, "00b_coesione_2127_attuazione", fonte="Commissione UE, Cohesion Open Data 3git-md5z, Italia",
              url=co.attrs["url"], nota="mld euro; programmato, costo delle operazioni selezionate, spesa dichiarata per ciclo e fondo", area=AREA)
        ult = co[co.tod_cycle == co.tod_cycle.max()][["programmato", "selezionato", "speso"]].sum()
        print(f"Coesione 2021-27 ciclo {co.tod_cycle.max()}: programmato {ult.programmato:.1f}, selezionato {ult.selezionato:.1f}, speso {ult.speso:.1f} mld")
    except Exception as e:
        print("ERR Cohesion Open Data:", e)

    sn = pd.DataFrame({"anno": list(TETTO), "tetto_annuo": list(TETTO.values()), "tetto_cumulato": list(TETTO_CUM.values()),
                       "programmato": list(PROG.values()), "programmato_netto_NEC": list(PROG_NEC.values()),
                       "tendenziale": [None, None] + list(TEND.values())})
    salva(sn, "00b_spesa_netta_percorso", fonte="MEF DPB 2027 Tab. III.1-1, DPFP 2026 Tav. II.1.5", url=DOC["00b_mef_dpb_2027.pdf"],
          nota="tassi di crescita % della spesa netta; trascritti e controllati nel testo PDF", area=AREA)
    qp = pd.DataFrame({"anno": list(DEFICIT), "indebitamento_netto_pil": list(DEFICIT.values()), "debito_pil": list(DEBITO.values()),
                       "pil_nominale_mld": [round(PIL_2025, 1)] + [round(pil(a), 1) for a in range(2026, 2030)]})
    salva(qp, "00b_quadro_programmatico", fonte="MEF DPB 2027 Tab. III.1-2; PIL da DPFP 2026 Tav. I.3.3", url=DOC["00b_mef_dpb_2027.pdf"],
          nota="PIL 2026-29 = calcolo GovernAI dalle crescite nominali programmatiche", area=AREA)

    v = scrivi_vincolo(res)
    f = scrivi_fondi()
    inb = f[(f.in_bilancio == "si") & (f.capienza_max != INF) & (f.fondo_id != "DEFICIT")]
    print(f"\nvincolo.csv: {len(v)} righe; fondi.csv: {len(f)} righe")
    print(f"Politiche invariate (stima): {sum(x[1] for x in POLITICHE_INVARIATE):.1f} mld/anno")
    print(f"Capienza fondi in bilancio (esclusi DEFICIT e illimitati): {inb.capienza_min.sum():.1f} - {inb.capienza_max.sum():.1f} mld/anno")
    perm = inb[inb.natura == "permanente"]
    print(f"  di cui permanenti: {perm.capienza_min.sum():.1f} - {perm.capienza_max.sum():.1f} mld/anno")


if __name__ == "__main__":
    sys.exit(main())
