"""Serie macroeconomiche e di finanza pubblica da AMECO (Commissione europea),
FMI (Public Finances in Modern History, dataset FPP) e OCSE (Revenue Statistics).

Uso:  python storia/script/scarica_ameco_fmi_ocse.py

Note di metodo
- AMECO: file completo ameco0.zip (edizione corrente). Gli anni dopo l'ultima
  annata consuntiva sono previsioni della Commissione: il 2026 resta nelle serie
  con "previsione" nella colonna fonte; il 2027 e' escluso.
- Germania prima del 1991: AMECO pubblica le serie della sola Germania Ovest
  (codice D_W). Le usiamo solo per tassi di variazione e tassi (mai per livelli),
  segnalandolo nella colonna fonte.
- Finanza pubblica: AMECO (SEC 2010, procedura per deficit eccessivi) parte dal
  1995 per Italia, Germania (1991) e Spagna. Prima usiamo FMI FPP (Mauro et al.,
  "Public Finances in Modern History"), segnalato nella colonna fonte: le due
  fonti non sono perfettamente omogenee e al 1995 puo' esserci un salto.
"""
from __future__ import annotations

import io
import json
import zipfile

import pandas as pd

from comune import ANNO_FINE, salva, scarica

AMECO_URL = "https://ec.europa.eu/economy_finance/db_indicators/ameco/documents/ameco0.zip"
AMECO_PAG = "https://economy-finance.ec.europa.eu/economic-research-and-databases/economic-databases/ameco-database_en"
FPP_PAG = "https://www.imf.org/external/datamapper/datasets/FPP"
OCSE_PAG = "https://data-explorer.oecd.org/ (Revenue Statistics - OECD countries: comparative tables)"

AMECO_PAESI = {"ITA": "IT", "FRA": "FR", "DEU": "DE", "ESP": "ES", "EA20": "EA", "EU27": "UE27"}
ULTIMO_CONSUNTIVO = 2025  # edizione AMECO in uso: il 2025 e' consuntivo, dal 2026 previsioni


def carica_ameco() -> pd.DataFrame:
    z = zipfile.ZipFile(io.BytesIO(scarica(AMECO_URL, "ameco0.zip", binario=True)))
    parti = []
    for n in z.namelist():
        if n.upper().endswith(".TXT"):
            d = pd.read_csv(z.open(n), sep=";", dtype=str, encoding="latin-1")
            parti.append(d.loc[:, ~d.columns.str.startswith("Unnamed")])
    d = pd.concat(parti, ignore_index=True)
    d["CODE"] = d["CODE"].str.strip()
    return d


AM = None


def ameco(codice_completo_senza_paese: str, paesi=AMECO_PAESI) -> pd.DataFrame:
    """Restituisce anno,paese,valore per un codice AMECO (es. '1.1.0.0.OVGD')."""
    righe = []
    for cod, p in paesi.items():
        r = AM[AM.CODE == f"{cod}.{codice_completo_senza_paese}"]
        if r.empty:
            continue
        r = r.iloc[0]
        for a in range(1960, ANNO_FINE + 1):
            v = r.get(str(a))
            if v is None or str(v) in ("NA", "nan", ""):
                continue
            righe.append({"anno": a, "paese": p, "valore": float(v)})
    return pd.DataFrame(righe)


def etichetta_fonte(df: pd.DataFrame, base: str) -> pd.DataFrame:
    df = df.copy()
    df["fonte"] = base
    df.loc[df.anno > ULTIMO_CONSUNTIVO, "fonte"] = base + " (previsione)"
    return df


def variazione(df: pd.DataFrame) -> pd.DataFrame:
    out = []
    for p, g in df.groupby("paese"):
        g = g.sort_values("anno").set_index("anno")["valore"]
        g = g.reindex(range(g.index.min(), g.index.max() + 1))
        v = (g / g.shift(1) - 1) * 100
        out.append(pd.DataFrame({"anno": v.index, "paese": p, "valore": v.values}))
    return pd.concat(out).dropna()


def con_germania_ovest(df_unificata: pd.DataFrame, df_ovest: pd.DataFrame, fonte: str,
                       primo_anno_unificata: int = 1992) -> pd.DataFrame:
    """Aggiunge alla Germania gli anni precedenti presi dalla Germania Ovest."""
    ow = df_ovest[df_ovest.anno < primo_anno_unificata].copy()
    ow["paese"] = "DE"
    ow["fonte"] = fonte + " - Germania Ovest (D_W) prima del " + str(primo_anno_unificata)
    return pd.concat([df_unificata, ow], ignore_index=True)


def fpp(indicatore: str) -> pd.DataFrame:
    url = f"https://www.imf.org/external/datamapper/api/v1/{indicatore}"
    js = json.loads(scarica(url, f"imf_fpp_{indicatore}.json"))
    v = js["values"][indicatore]
    righe = []
    for cod, p in {"ITA": "IT", "FRA": "FR", "DEU": "DE", "ESP": "ES"}.items():
        for a, x in v.get(cod, {}).items():
            if x is not None:
                righe.append({"anno": int(a), "paese": p, "valore": float(x)})
    return pd.DataFrame(righe)


def unisci_ameco_fpp(am: pd.DataFrame, fp: pd.DataFrame, base_am: str) -> pd.DataFrame:
    """AMECO dove c'e'; FMI FPP per gli anni precedenti al primo anno AMECO del paese."""
    am = etichetta_fonte(am, base_am)
    parti = [am]
    # Solo Italia e Germania: per Francia (prima del 1978) e Spagna (prima del 1995)
    # FPP riporta il solo bilancio dello Stato centrale (es. spesa Francia 1977 = 21% del
    # PIL, Spagna 1994 = 33% contro 45% AMECO nel 1995): non confrontabile, lasciato vuoto.
    for p in ["IT", "DE"]:
        primo = am[am.paese == p].anno.min() if (am.paese == p).any() else 9999
        f = fp[(fp.paese == p) & (fp.anno < primo)].copy()
        f["fonte"] = "FMI, Public Finances in Modern History (FPP)"
        if p == "DE":
            f["fonte"] += " - Germania Ovest prima del 1991"
        parti.append(f)
    return pd.concat(parti, ignore_index=True)


def main():
    global AM
    print("AMECO: caricamento...")
    AM = carica_ameco()
    FA = "AMECO (Commissione europea)"
    PIL = "1.1.0.0.OVGD"

    # 1. PIL reale: crescita annua
    g = etichetta_fonte(variazione(ameco(PIL)), FA)
    g = con_germania_ovest(g, variazione(ameco(PIL, {"D_W": "DE"})), FA)
    salva("pil_reale_crescita", g, "Crescita annua del PIL reale (prezzi costanti)",
          "% annua", FA, AMECO_PAG)

    # 2. PIL pro capite reale: livello (migliaia di euro, prezzi 2020) e crescita
    pc = ameco("1.1.0.0.RVGDP")
    salva("pil_pro_capite_reale", etichetta_fonte(pc, FA),
          "PIL pro capite reale, migliaia di euro a prezzi 2020 (valuta nazionale convertita al tasso fisso dell'euro; Germania solo dal 1991)",
          "migliaia di euro 2020", FA, AMECO_PAG)
    gpc = etichetta_fonte(variazione(pc), FA)
    gpc = con_germania_ovest(gpc, variazione(ameco("1.1.0.0.RVGDP", {"D_W": "DE"})), FA)
    salva("pil_pro_capite_crescita", gpc, "Crescita annua del PIL pro capite reale",
          "% annua", FA, AMECO_PAG)
    pps = ameco("1.0.212.327.HVGDPR")
    salva("pil_pro_capite_pps_ue27", etichetta_fonte(pps, FA),
          "PIL pro capite a parita' di potere d'acquisto, UE27 = 100", "indice UE27=100", FA, AMECO_PAG)

    # 3. Produttivita' del lavoro per ora lavorata: crescita (PIL reale / ore lavorate)
    def prod(paesi):
        y = ameco(PIL, paesi).set_index(["anno", "paese"])["valore"]
        h = ameco("1.0.0.0.NLHT", paesi).set_index(["anno", "paese"])["valore"]
        return (y / h).dropna().rename("valore").reset_index()
    pr = etichetta_fonte(variazione(prod(AMECO_PAESI)), FA)
    pr = con_germania_ovest(pr, variazione(prod({"D_W": "DE"})), FA)
    salva("produttivita_oraria_crescita", pr,
          "Crescita annua della produttivita' del lavoro: PIL reale per ora lavorata (calcolata da OVGD/NLHT)",
          "% annua", FA, AMECO_PAG)

    # 4. Disoccupazione
    u = etichetta_fonte(ameco("1.0.0.0.ZUTN"), FA)
    u = con_germania_ovest(u, ameco("1.0.0.0.ZUTN", {"D_W": "DE"}), FA, 1991)
    salva("disoccupazione", u, "Tasso di disoccupazione (definizione Eurostat), % della forza lavoro",
          "% forza lavoro", FA, AMECO_PAG)

    # 5. Inflazione: variazione indice nazionale dei prezzi al consumo
    inf = etichetta_fonte(variazione(ameco("3.0.0.0.ZCPIN")), FA)
    salva("inflazione", inf, "Inflazione: variazione annua dell'indice nazionale dei prezzi al consumo (per area euro e UE: indice aggregato AMECO)",
          "% annua", FA, AMECO_PAG)

    # 6. Debito pubblico / PIL (serie collegata con le definizioni precedenti)
    d = etichetta_fonte(ameco("1.0.319.0.UDGGL"), FA)
    dw = ameco("1.0.319.0.UDGGL", {"D_W": "DE"})
    d = con_germania_ovest(d, dw, FA, 1991)
    salva("debito_pil", d, "Debito pubblico lordo consolidato (Maastricht), % del PIL; serie AMECO collegata con le definizioni precedenti",
          "% PIL", FA, AMECO_PAG)

    # 7-10. Saldi e spesa: AMECO (SEC 2010) + FMI FPP prima
    pb = fpp("pb")
    ie = fpp("ie")
    defi_fpp = pb.merge(ie, on=["anno", "paese"], suffixes=("_pb", "_ie"))
    defi_fpp["valore"] = defi_fpp.valore_pb - defi_fpp.valore_ie
    salva("deficit_pil", unisci_ameco_fpp(ameco("1.0.319.0.UBLGE"), defi_fpp[["anno", "paese", "valore"]], FA),
          "Indebitamento (-) o accreditamento (+) netto delle amministrazioni pubbliche, % del PIL. Valori negativi = deficit. Prima del primo anno AMECO (Italia 1995, Germania 1991; Francia gia' dal 1960/1978) FMI FPP calcolato come saldo primario meno interessi; Spagna prima del 1995 non disponibile in modo omogeneo",
          "% PIL", FA + " dal 1995; FMI FPP prima", AMECO_PAG + " ; " + FPP_PAG)
    salva("saldo_primario_pil", unisci_ameco_fpp(ameco("1.0.319.0.UBLGIE"), pb, FA),
          "Saldo primario (al netto degli interessi) delle amministrazioni pubbliche, % del PIL",
          "% PIL", FA + " dal 1995; FMI FPP prima", AMECO_PAG + " ; " + FPP_PAG)
    salva("interessi_pil", unisci_ameco_fpp(ameco("1.0.319.0.UYIGE"), ie, FA),
          "Spesa per interessi delle amministrazioni pubbliche, % del PIL",
          "% PIL", FA + " dal 1995; FMI FPP prima", AMECO_PAG + " ; " + FPP_PAG)
    salva("spesa_pubblica_pil", unisci_ameco_fpp(ameco("1.0.319.0.UUTGE"), fpp("exp"), FA),
          "Spesa totale delle amministrazioni pubbliche, % del PIL",
          "% PIL", FA + " dal 1995; FMI FPP prima", AMECO_PAG + " ; " + FPP_PAG)
    # 11. Pressione fiscale: AMECO 1995+ (tutti) e OCSE Revenue Statistics 1965+ (4 paesi)
    salva("pressione_fiscale", etichetta_fonte(ameco("1.0.319.0.UTAT"), FA),
          "Pressione fiscale: imposte e contributi sociali effettivi, % del PIL (AMECO UTAT, SEC 2010)",
          "% PIL", FA, AMECO_PAG)
    url = ("https://sdmx.oecd.org/public/rest/data/OECD.CTP.TPS,DSD_REV_COMP_OECD@DF_RSOECD,/"
           "ITA+FRA+DEU+ESP.TAX_REV.S13._T._T.PT_B1GQ.A?startPeriod=1965")
    txt = scarica(url, "ocse_rev_tot.csv", headers={"Accept": "application/vnd.sdmx.data+csv"})
    o = pd.read_csv(io.StringIO(txt))
    o = o.rename(columns={"TIME_PERIOD": "anno", "OBS_VALUE": "valore"})
    o["paese"] = o.REF_AREA.map({"ITA": "IT", "FRA": "FR", "DEU": "DE", "ESP": "ES"})
    salva("pressione_fiscale_ocse", o[["anno", "paese", "valore"]],
          "Gettito fiscale totale (imposte e contributi), % del PIL, OCSE Revenue Statistics (Germania: dati della Germania Ovest prima del 1991 secondo l'OCSE)",
          "% PIL", "OCSE, Revenue Statistics", OCSE_PAG)

    # 12. Investimenti pubblici
    salva("investimenti_pubblici_pil", etichetta_fonte(ameco("1.0.319.0.UIGG0"), FA),
          "Investimenti fissi lordi delle amministrazioni pubbliche, % del PIL", "% PIL", FA, AMECO_PAG)

    # 13. Tassi a lungo termine e spread verso la Germania
    il = etichetta_fonte(ameco("1.1.0.0.ILN"), FA)
    salva("tasso_lungo", il, "Rendimento nominale dei titoli di Stato a lungo termine (circa 10 anni), media annua",
          "%", FA, AMECO_PAG)
    de = il[il.paese == "DE"].set_index("anno")["valore"]
    sp = il[il.paese.isin(["IT", "FR", "ES"])].copy()
    sp["valore"] = (sp.valore - sp.anno.map(de)) * 100
    salva("spread_bund", sp, "Differenziale di rendimento a lungo termine rispetto alla Germania (punti base, media annua)",
          "punti base", FA, AMECO_PAG)


if __name__ == "__main__":
    main()
