"""GovernAI - Area 09 (Pubblica amministrazione, Digitale): verifica dati del dossier.

Scarica le serie da fonte primaria e le salva in dati/serie/ con prefisso "09_"
(registro: dati/serie/_registro_09.csv). Eseguire da dati/script/:
    python 09_pa_digitale.py

Note tecniche:
- fonti.istat() ha timeout fisso di 60 s: il flusso SDMX della popolazione comunale
  (22_289) va in timeout anche a 450 s. Per la popolazione per comune si usa quindi il
  file bulk ISTAT demo.istat.it (POSAS), scaricato con fonti.scarica().
- Alcuni dati (ANAC, AgID, DTD, Digital Decade) esistono solo in comunicati/report PDF:
  il file grezzo viene scaricato in dati/raw/ quando raggiungibile e i valori sono
  trascritti in tabelle salvate con salva(), con fonte e URL nel registro.
"""
from __future__ import annotations

import io
import zipfile

import pandas as pd

from fonti import eurostat, salva, scarica

AREA = "09"


def prova(fn, *a, **k):
    try:
        return fn(*a, **k)
    except Exception as e:  # una fonte irraggiungibile non deve bloccare lo script
        print(f"  ! {getattr(fn, '__name__', fn)} fallita: {e}")
        return None


# 1. Competenze digitali almeno di base (Decennio digitale, target 80% al 2030)
df = eurostat("isoc_sk_dskl_i21", since="2021", geo=["IT", "EU27_2020"],
              indic_is="I_DSK2_BAB", ind_type="IND_TOTAL", unit="PC_IND")
salva(df, "09_competenze_digitali_base", "Eurostat isoc_sk_dskl_i21 (I_DSK2_BAB, 16-74 anni)",
      df.attrs["url"], "Rilevazione biennale: 2021, 2023, 2025 (nessun dato 2024)", area=AREA)

# 2. Uso dell'e-government (interazione con la PA via internet, ultimi 12 mesi)
df = eurostat("isoc_ciegi_ac", since="2022", geo=["IT", "EU27_2020"], ind_type="IND_TOTAL",
              unit="PC_IND", indic_is=["I_IUGOV1", "I_IGOVANYS", "I_IGOVIDB"])
salva(df, "09_egov_uso_cittadini", "Eurostat isoc_ciegi_ac", df.attrs["url"],
      "I_IUGOV1 = interazione con autorità pubbliche (definizione dal 2022)", area=AREA)

# 3. Specialisti ICT sull'occupazione totale (proxy: nessun dato ufficiale per la sola PA)
df = eurostat("isoc_sks_itspt", since="2021", geo=["IT", "EU27_2020"], unit="PC_EMP")
salva(df, "09_specialisti_ict_occupati", "Eurostat isoc_sks_itspt", df.attrs["url"],
      "Intera economia, non solo PA", area=AREA)

# 4. Redditi da lavoro dipendente delle AP (D.1 uscite, S13), mln € e % PIL
df = eurostat("gov_10a_main", since="2019", geo=["IT"], unit=["MIO_EUR", "PC_GDP"],
              na_item="D1PAY", sector="S13")
salva(df, "09_redditi_lavoro_dipendente_pa", "Eurostat gov_10a_main (D1PAY, S13)", df.attrs["url"],
      "Contabilità nazionale SEC 2010", area=AREA)

# 5. Comuni per classe di ampiezza demografica (ISTAT, popolazione al 1.1.2026)
p = prova(scarica, "https://demo.istat.it/data/posas/POSAS_2026_it_Comuni.zip", "09_POSAS_2026_it_Comuni.zip")
if p is not None:
    with zipfile.ZipFile(p) as z:
        testo = z.read(z.namelist()[0]).decode("utf-8-sig")
    pop = pd.read_csv(io.StringIO(testo), sep=";", skiprows=1, dtype={"Codice comune": str})
    tot = pop[pop["Età"] == 999] if (pop["Età"] == 999).any() else pop.groupby(["Codice comune"], as_index=False)["Totale"].sum()
    tot = tot.groupby("Codice comune", as_index=False)["Totale"].sum()
    classi = pd.cut(tot["Totale"], [0, 1000, 5000, 15000, 60000, 1e8],
                    labels=["<1.000", "1.000-4.999", "5.000-14.999", "15.000-59.999", ">=60.000"], right=False)
    out = tot.groupby(classi, observed=False).agg(comuni=("Totale", "size"), popolazione=("Totale", "sum")).reset_index()
    out = out.rename(columns={"Totale": "classe"})
    out.columns = ["classe", "comuni", "popolazione"]
    out["quota_comuni_pct"] = (100 * out["comuni"] / out["comuni"].sum()).round(1)
    out["quota_pop_pct"] = (100 * out["popolazione"] / out["popolazione"].sum()).round(1)
    out.loc[len(out)] = ["TOTALE", out["comuni"].sum(), out["popolazione"].sum(), 100.0, 100.0]
    salva(out, "09_comuni_classi_ampiezza", "ISTAT, Popolazione residente al 1° gennaio 2026 (stima) per comune - POSAS",
          "https://demo.istat.it/data/posas/POSAS_2026_it_Comuni.zip", "Elaborazione GovernAI per classi", area=AREA)
    print(out)

# 6. Qualificazione stazioni appaltanti (ANAC, report trimestrale) - valori trascritti
prova(scarica, "https://www.lavoripubblici.it/documenti2026/lvpb3/report-anac-qualificazione-sa-I-trimestre-2026.pdf",
      "09_anac_report_qualificazione_SA_I_trim_2026.pdf")
anac = pd.DataFrame([
    ("2026-03-31", "Qualificate progettazione e affidamento (artt. 62-63), totale", 3919),
    ("2026-03-31", "  di cui Lavori", 3066),
    ("2026-03-31", "  di cui Servizi e forniture", 3210),
    ("2026-03-31", "Centrali di committenza qualificate - Lavori", 425),
    ("2026-03-31", "Centrali di committenza qualificate - Servizi e forniture", 400),
    ("2026-03-31", "Qualificate per l'esecuzione (almeno un settore)", 6348),
    ("2026-03-31", "Istanze qualificate con riserva", 48),
    ("2026-03-31", "Enti distinti qualificati con riserva", 37),
    ("2026-06-30", "Qualificate per l'esecuzione (almeno un settore)", 6510),
], columns=["data_riferimento", "voce", "valore"])
salva(anac, "09_anac_qualificazione_sa", "ANAC, Report trimestrale qualificazione stazioni appaltanti (I trim. 2026; dato esecuzione al 30.6.2026)",
      "https://portale-servizi.anticorruzione.it/qualificazione",
      "Esclusi i soggetti qualificati di diritto. Report I trim. 2026 ripubblicato da lavoripubblici.it; dato 30.6.2026 da comunicato ANAC ripreso da terzi", area=AREA)

# 7. Identità digitali (AgID, comunicato stampa 8.10.2025)
prova(scarica, "https://www.agid.gov.it/sites/agid/files/2025-10/2025.10.08_CS_Rinnovo_convenzioni_Spid.pdf",
      "09_agid_cs_2025-10-08_spid.pdf")
idd = pd.DataFrame([
    ("2025-10-08", "Identità digitali rilasciate (SPID + CIE)", 96_000_000),
    ("2025-10-08", "Identità SPID rilasciate", 41_000_000),
    ("2025-10-08", "CIE rilasciate", 55_000_000),
    ("2025-10-08", "Credenziali CIE (CieID) attivate", 9_000_000),
    ("2025-10-08", "Utenti IT-Wallet (app IO)", 6_400_000),
], columns=["data", "voce", "valore"])
salva(idd, "09_identita_digitali", "AgID, comunicato stampa 8 ottobre 2025 (rinnovo convenzioni SPID)",
      "https://www.agid.gov.it/sites/agid/files/2025-10/2025.10.08_CS_Rinnovo_convenzioni_Spid.pdf",
      "Convenzioni SPID prorogate di 2 anni (fino a 2027), estendibili fino a 36 mesi", area=AREA)

# 8. PDND, PSN, cloud (Dipartimento per la trasformazione digitale) - valori trascritti
dtd = pd.DataFrame([
    ("2026-05-31", "PDND", "Enti aderenti", 9400, "DTD, scheda di rendicontazione impegno trasformativo (open.gov.it, lug. 2026)"),
    ("2026-05-31", "PDND", "E-service pubblicati", 14000, "DTD, scheda di rendicontazione impegno trasformativo (open.gov.it, lug. 2026)"),
    ("2026-05-31", "PDND", "Connessioni tra enti (circa)", 45000, "DTD, scheda di rendicontazione impegno trasformativo (open.gov.it, lug. 2026)"),
    ("2026-06", "PDND", "Scambi di dati via API (miliardi)", 1.1, "DTD, notizia 22.6.2026 su State of the Digital Decade"),
    ("2026-06", "PSN (PNRR M1C1 inv. 1.1)", "PA centrali e strutture sanitarie migrate (target 280 al 30.6.2026)", 280, "DTD, dichiarazioni luglio 2026 (via Corriere Comunicazioni 21.7.2026): 'oltre 280'"),
    ("2026-06", "Cloud (inv. 1.1+1.2)", "PA migrate in totale (circa)", 13000, "DTD/Sottosegretario Butti, luglio 2026; target inv. 1.2 = 12.464 PA locali"),
    ("2026-06", "Cloud (inv. 1.1+1.2)", "Dotazione PNRR (mld €)", 1.9, "PNRR: inv. 1.1 0,9 mld + inv. 1.2 1,0 mld"),
], columns=["data", "ambito", "voce", "valore", "fonte"])
salva(dtd, "09_dtd_pdnd_psn_cloud", "Dipartimento per la trasformazione digitale (comunicazioni 2026)",
      "https://innovazione.gov.it/", "Valori arrotondati 'oltre'; documenti open.gov.it non raggiungibili (503) al 7.11.2026", area=AREA)

# 9. State of the Digital Decade 2026 - KPI Italia vs UE (Commissione UE)
dd = pd.DataFrame([
    ("Servizi pubblici digitali per i cittadini (punteggio 0-100)", 86.11, 84.64, 100),
    ("Servizi pubblici digitali per i cittadini nazionali", 96.77, 94.01, 100),
    ("Servizi pubblici digitali transfrontalieri", 75.45, None, 100),
    ("Accesso ai dati sanitari elettronici (e-health, 0-100)", 89.93, 86.51, 100),
    ("Competenze digitali almeno di base (% 16-74)", 54.27, 60.40, 80),
    ("Specialisti ICT (% occupati)", 3.8, 5.0, None),
], columns=["indicatore", "IT", "UE27", "target_2030"])
salva(dd, "09_digital_decade_2026", "Commissione UE, State of the Digital Decade 2026 - Italy country report (SWD(2026) 155)",
      "https://digital-strategy.ec.europa.eu/en/factpages/italys-2026-digital-decade-country-report",
      "Valori da DTD 22.6.2026 e Eurostat; target ICT UE = 20 mln specialisti (non in %)", area=AREA)

print("Fatto: serie 09_ salvate in dati/serie/ e registrate in _registro_09.csv")
