"""GovernAI - Indicatori di rischio ("red flag") negli appalti pubblici per stazione appaltante e per settore.

Fonte: ANAC, Banca Dati Nazionale dei Contratti Pubblici (BDNCP), open data
(https://dati.anticorruzione.it/opendata). Campione: tutti i CIG pubblicati nel 2024
(dataset "CIG anno 2024"), incrociati con aggiudicazioni, aggiudicatari, varianti e anagrafe
delle stazioni appaltanti.

AVVISO. Un indicatore di rischio NON è una prova né un'accusa. Segnala scostamenti statistici
dalla media nazionale che possono avere spiegazioni legittime (urgenze reali, mercati con un solo
fornitore, errori di compilazione). Serve a orientare controlli e trasparenza, non a giudicare.

Principi (Carta dei valori, FID e SIC):
- unità di analisi: enti (stazioni appaltanti) e settori, MAI persone fisiche;
- i codici fiscali degli operatori economici servono solo per contare ripetizioni dentro lo stesso
  ente e restano in memoria come codici anonimi: non compaiono in nessun output;
- pesi dichiarati, intervalli di confidenza, confronto con l'atteso nazionale per lo stesso
  mix di contratti (tipo di contratto x fascia d'importo).

Uso:
    python trasparenza/indicatori.py            # scarica (se mancano) i grezzi e calcola
    python trasparenza/indicatori.py --anno 2024

Output: trasparenza/rischio_enti.csv, trasparenza/rischio_settori.csv, trasparenza/rapporto.md.
I file grezzi (oltre 500 MB) stanno in trasparenza/grezzi/, escluso da git.
"""
from __future__ import annotations

import argparse
import hashlib
import math
import sys
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd
import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "dati" / "script"))
from fonti import HEADERS  # noqa: E402  (stesso User-Agent degli altri script GovernAI)

QUI = Path(__file__).resolve().parent
GREZZI = QUI / "grezzi"
ANAC = "https://dati.anticorruzione.it/opendata/download/dataset/"
Z90 = 1.645  # intervalli di confidenza al 90%

# --- Soglie di legge (d.lgs. 36/2023) ---------------------------------------
SOGLIA_DIRETTO = {"LAVORI": 150_000, "SERVIZI": 140_000, "FORNITURE": 140_000}  # art. 50, c.1, lett. a-b
SOGLIA_UE = {"LAVORI": 5_538_000, "SERVIZI": 221_000, "FORNITURE": 221_000}     # art. 14 (enti sub-centrali, 2024-25)
SOGLIA_UE_SPECIALI = {"LAVORI": 5_538_000, "SERVIZI": 443_000, "FORNITURE": 443_000}
SOGLIA_ROTAZIONE = 5_000  # art. 49, c.6: sotto i 5.000 euro si può derogare alla rotazione
GIORNI_MINIMI = 15        # termine di offerta sotto il quale il bando è "breve" (minimo ridotto per urgenza)

# --- Indicatori e pesi dichiarati (somma = 1) --------------------------------
# I pesi più alti vanno ai due indicatori più validati in letteratura (offerta unica e assenza di
# confronto competitivo: Fazekas e Kocsis 2020; Single Market Scoreboard UE, dove pesano il triplo).
# Frazionamento e riaffidamento nascono dagli stessi gruppi di affidamenti diretti e sono correlati:
# insieme pesano 0,20, non di più, per non contare due volte lo stesso fenomeno.
INDICATORI = {
    "offerta_unica":      (0.30, "Offerta unica in procedure con confronto competitivo"),
    "non_competitiva":    (0.25, "Affidamento diretto oltre le soglie dell'art. 50 o negoziata senza bando oltre la soglia UE"),
    "termini_brevi":      (0.10, f"Termine per le offerte sotto i {GIORNI_MINIMI} giorni in procedure aperte o ristrette"),
    "urgenza":            (0.05, "Ricorso dichiarato a somma o estrema urgenza"),
    "frazionamento":      (0.10, "Affidamenti diretti allo stesso operatore, stesso ente e stessa categoria CPV, ciascuno sotto soglia ma con somma oltre soglia"),
    "riaffidamento":      (0.10, "Affidamento diretto a un operatore che ha ricevuto almeno 3 affidamenti diretti dallo stesso ente nella stessa categoria CPV (rotazione)"),
    "varianti":           (0.05, "Contratti da 40.000 euro in su con almeno una variante o modifica comunicata"),
    "ribasso_minimo":     (0.05, "Ribasso inferiore all'1% in procedure con almeno 2 offerte"),
}
assert abs(sum(w for w, _ in INDICATORI.values()) - 1) < 1e-9

FASCE = [0, 40_000, 140_000, 1_000_000, 5_538_000, float("inf")]
ETICHETTE_FASCE = ["<40k", "40-140k", "140k-1M", "1M-5,5M", ">5,5M"]

DIRETTO = {"AFFIDAMENTO DIRETTO"}
NEG_SENZA_BANDO = {"PROCEDURA NEGOZIATA SENZA PREVIA PUBBLICAZIONE", "PROCEDURA NEGOZIATA PER AFFIDAMENTI SOTTO SOGLIA"}
APERTE = {"PROCEDURA APERTA", "PROCEDURA RISTRETTA", "PROCEDURA NEGOZIATA CON PREVIA INDIZIONE DI GARA (SETTORI SPECIALI)",
          "PROCEDURA COMPETITIVA CON NEGOZIAZIONE", "DIALOGO COMPETITIVO"}
ESCLUSE = ("ADESIONE", "IN HOUSE")  # adesioni a convenzioni/accordi quadro e in house: altre regole

# Nature giuridiche considerate "ente pubblico" per la graduatoria (le società restano nel calcolo nazionale)
PUBBLICI = ("ENTI PUBBLICI", "ENTE PUBBLICO", "AMMINISTRAZIONI PUBBLICHE", "AMMINISTRAZIONI DELLO STATO", "COMUNE",
            "UNIONE DI COMUNI", "AZIENDE REGIONALI", "CONSORZI AI SENSI DELLA L.142/90", "ENTI OSPEDALIERI",
            "ENTI ED ISTITUTI DI PREVIDENZA", "ISTITUTO E SCUOLA PUBBLICA", "AZIENDA SPECIALE", "CONSORZIO DI CUI AL DLGS 267",
            "ENTE DIRITTO PUBBLICO", "CONSORZIO INTERCOMUNALE", "CONSORZIO DI DIRITTO PUBBLICO", "ENTE PARCO",
            "ENTE AMBIENTALE REGIONALE", "ORDINE E COLLEGIO PROFESSIONALE", "ISTITUTO PUBBLICO DI ASSISTENZA",
            "AZIENDE AUTONOME DI CURA")

MIN_CIG = 50          # CIG minimi per entrare nella graduatoria
MIN_INDICATORI = 4    # indicatori con almeno 10 casi valutabili


# --- Download ---------------------------------------------------------------

def scarica(percorso: str) -> Path:
    """Scarica un file ANAC in trasparenza/grezzi/ se non c'è già (i file non cambiano dopo la pubblicazione)."""
    GREZZI.mkdir(parents=True, exist_ok=True)
    dest = GREZZI / percorso.split("/")[-1]
    if dest.exists() and dest.stat().st_size > 0:
        return dest
    print(f"scarico {percorso} ...")
    with requests.get(ANAC + percorso, headers=HEADERS, timeout=900, stream=True) as r:
        r.raise_for_status()
        tmp = dest.with_suffix(".part")
        with open(tmp, "wb") as f:
            for blocco in r.iter_content(1 << 20):
                f.write(blocco)
        tmp.replace(dest)
    return dest


def leggi(path: Path, colonne: list[str], filtro_cig: set | None = None) -> pd.DataFrame:
    """Legge un CSV ANAC zippato (separatore ;) a blocchi, tenendo solo le colonne utili e i CIG del campione."""
    pezzi = []
    for blocco in pd.read_csv(path, sep=";", usecols=colonne, dtype=str, chunksize=500_000,
                              encoding="utf-8", encoding_errors="replace", on_bad_lines="skip"):
        if filtro_cig is not None:
            blocco = blocco[blocco["cig"].isin(filtro_cig)]
        pezzi.append(blocco)
    return pd.concat(pezzi, ignore_index=True)


def carica(anno: int) -> pd.DataFrame:
    cache = GREZZI / f"campione_{anno}.pkl"
    if cache.exists():
        return pd.read_pickle(cache)
    col_cig = ["cig", "importo_lotto", "oggetto_principale_contratto", "settore", "data_pubblicazione",
               "data_scadenza_offerta", "tipo_scelta_contraente", "modalita_realizzazione",
               "cf_amministrazione_appaltante", "denominazione_amministrazione_appaltante", "sezione_regionale",
               "provincia", "cod_cpv", "flag_prevalente", "DATA_CANCELLAZIONE", "MOTIVO_URGENZA", "ESITO"]
    cig = pd.concat([leggi(scarica(f"cig-{anno}/filesystem/cig_csv_{anno}_{m:02d}.zip"), col_cig) for m in range(1, 13)])
    cig = cig[cig["DATA_CANCELLAZIONE"].isna()]
    # un CIG può avere più CPV: si tiene il prevalente
    cig = cig.sort_values("flag_prevalente", ascending=False).drop_duplicates("cig")
    cigset = set(cig["cig"])

    agg = leggi(scarica("aggiudicazioni/filesystem/aggiudicazioni_csv.zip"),
                ["cig", "id_aggiudicazione", "data_aggiudicazione_definitiva", "num_imprese_offerenti",
                 "numero_offerte_ammesse", "ribasso_aggiudicazione", "importo_aggiudicazione"], cigset)
    agg = agg.sort_values("data_aggiudicazione_definitiva").drop_duplicates("cig", keep="last")

    vinc = leggi(scarica("aggiudicatari/filesystem/aggiudicatari_csv.zip"),
                 ["cig", "ruolo", "codice_fiscale", "id_aggiudicazione"], cigset)
    # per i raggruppamenti si tiene la mandataria; il codice fiscale diventa subito un codice anonimo
    vinc["ord"] = vinc["ruolo"].fillna("").str.contains("MANDATARIA").map({True: 0, False: 1})
    vinc = vinc.sort_values("ord").drop_duplicates("id_aggiudicazione")
    vinc["operatore"] = vinc["codice_fiscale"].fillna("").map(
        lambda s: hashlib.sha256(s.encode()).hexdigest()[:12] if s else np.nan)
    vinc = vinc[["id_aggiudicazione", "operatore"]]

    var = leggi(scarica("varianti/filesystem/varianti_csv.zip"), ["cig"], cigset)
    sa = pd.read_csv(scarica("stazioni-appaltanti/filesystem/stazioni-appaltanti_csv.zip"), sep=";", dtype=str,
                     usecols=["codice_fiscale", "natura_giuridica_descrizione"], encoding_errors="replace")

    df = cig.merge(agg, on="cig", how="left").merge(vinc, on="id_aggiudicazione", how="left")
    df["ha_variante"] = df["cig"].isin(set(var["cig"]))
    df = df.merge(sa.rename(columns={"codice_fiscale": "cf_amministrazione_appaltante"}),
                  on="cf_amministrazione_appaltante", how="left")
    df.to_pickle(cache)
    return df


# --- Indicatori a livello di CIG ---------------------------------------------
# Ogni indicatore è una colonna con 1 (segnale), 0 (nessun segnale) o NaN (non valutabile).

def flag_cig(df: pd.DataFrame) -> pd.DataFrame:
    tipo = df["tipo_scelta_contraente"].fillna("ND")
    df = df[~tipo.str.contains("|".join(ESCLUSE)) & ~df["modalita_realizzazione"].fillna("").str.contains(
        "SENZA SUCCESSIVO CONFRONTO|SOLA TRACCIABILIT")].copy()
    df = df[df["oggetto_principale_contratto"].isin(SOGLIA_DIRETTO)]
    tipo = df["tipo_scelta_contraente"].fillna("ND")
    ogg = df["oggetto_principale_contratto"]
    imp = pd.to_numeric(df["importo_lotto"], errors="coerce").fillna(0)
    df["importo"] = imp
    df["fascia"] = pd.cut(imp, FASCE, labels=ETICHETTE_FASCE, right=False).astype(str)
    df["cpv2"] = df["cod_cpv"].fillna("").str[:2]
    diretto, negsb, aperta = tipo.isin(DIRETTO), tipo.isin(NEG_SENZA_BANDO), tipo.isin(APERTE)
    aggiudicato = df["ESITO"].fillna("").str.startswith("AGGIUDICATA") | df["id_aggiudicazione"].notna()

    # 1. offerta unica (procedure non dirette, aggiudicate, con numero di offerte noto)
    off = pd.to_numeric(df["num_imprese_offerenti"], errors="coerce")
    off = off.fillna(pd.to_numeric(df["numero_offerte_ammesse"], errors="coerce"))
    valut = ~diretto & aggiudicato & off.notna() & (off > 0)
    df["offerta_unica"] = np.where(valut, (off == 1).astype(float), np.nan)

    # 2. procedura non competitiva oltre le soglie di legge
    s_dir = ogg.map(SOGLIA_DIRETTO)
    s_ue = np.where(df["settore"].eq("SETTORI SPECIALI"), ogg.map(SOGLIA_UE_SPECIALI), ogg.map(SOGLIA_UE))
    valut = imp >= s_dir
    segnale = (diretto & (imp >= s_dir)) | (negsb & (imp >= s_ue))
    df["non_competitiva"] = np.where(valut, segnale.astype(float), np.nan)

    # 3. termini brevi
    gg = (pd.to_datetime(df["data_scadenza_offerta"], errors="coerce")
          - pd.to_datetime(df["data_pubblicazione"], errors="coerce")).dt.days
    valut = aperta & gg.notna() & (gg >= 0)
    df["termini_brevi"] = np.where(valut, (gg < GIORNI_MINIMI).astype(float), np.nan)
    df["giorni_offerta"] = gg

    # 4. urgenza dichiarata (il FLAG_URGENZA della banca dati vale 1 nel 68% dei CIG: si usa il motivo esplicito)
    df["urgenza"] = df["MOTIVO_URGENZA"].fillna("").str.upper().str.contains("URGENZA").astype(float)

    # 5-6. affidamenti diretti ripetuti allo stesso operatore (stesso ente, stessa divisione CPV)
    d = df[diretto & df["operatore"].notna() & (imp >= SOGLIA_ROTAZIONE)]
    chiave = ["cf_amministrazione_appaltante", "operatore", "cpv2", "oggetto_principale_contratto"]
    g = d.groupby(chiave)["importo"].agg(n="size", somma="sum").reset_index()
    d = d[["cig"] + chiave + ["importo"]].merge(g, on=chiave)
    soglia_d = d["oggetto_principale_contratto"].map(SOGLIA_DIRETTO)
    fraz = set(d.loc[(d["n"] >= 2) & (d["importo"] < soglia_d) & (d["somma"] >= soglia_d), "cig"])
    riaff = set(d.loc[d["n"] >= 3, "cig"])
    valut = df["cig"].isin(set(d["cig"]))
    df["frazionamento"] = np.where(valut, df["cig"].isin(fraz).astype(float), np.nan)
    df["riaffidamento"] = np.where(valut, df["cig"].isin(riaff).astype(float), np.nan)

    # 7. varianti (obbligo di comunicazione ANAC dai 40.000 euro)
    valut = aggiudicato & (imp >= 40_000)
    df["varianti"] = np.where(valut, df["ha_variante"].astype(float), np.nan)

    # 8. ribasso minimo con almeno due offerte
    rib = pd.to_numeric(df["ribasso_aggiudicazione"], errors="coerce")
    valut = ~diretto & (off >= 2) & rib.notna() & (rib >= 0) & (rib <= 100)
    df["ribasso_minimo"] = np.where(valut, (rib < 1).astype(float), np.nan)
    return df


# --- Aggregazione ------------------------------------------------------------

def wilson(o, n, z=Z90):
    n = np.asarray(n, float)
    p = np.where(n > 0, o / np.maximum(n, 1), np.nan)
    den = 1 + z**2 / np.maximum(n, 1)
    c = (p + z**2 / (2 * np.maximum(n, 1))) / den
    h = z * np.sqrt(p * (1 - p) / np.maximum(n, 1) + z**2 / (4 * np.maximum(n, 1) ** 2)) / den
    return c - h, c + h


def per_ente(df: pd.DataFrame) -> pd.DataFrame:
    """Per ogni ente e indicatore: casi valutabili N, segnali O, attesi E (tasso nazionale dello stesso
    tipo di contratto e fascia d'importo applicato ai CIG dell'ente). Rapporto O/E con correzione +1:
    log RR = log((O+1)/(E+1)), varianza approssimata (Poisson, E noto) 1/(O+1)."""
    strato = ["oggetto_principale_contratto", "fascia"]
    ente = "cf_amministrazione_appaltante"
    righe = []
    for k in INDICATORI:
        v = df[df[k].notna()]
        tasso = v.groupby(strato)[k].mean().rename("atteso")
        v = v.join(tasso, on=strato)
        a = v.groupby(ente).agg(N=(k, "size"), O=(k, "sum"), E=("atteso", "sum"))
        a.columns = [f"{k}_{c}" for c in a.columns]
        righe.append(a)
    out = pd.concat(righe, axis=1)
    info = df.groupby(ente).agg(denominazione=("denominazione_amministrazione_appaltante", "first"),
                                natura=("natura_giuridica_descrizione", "first"),
                                regione=("sezione_regionale", "first"), provincia=("provincia", "first"),
                                n_cig=("cig", "size"), valore_mln=("importo", lambda s: s.sum() / 1e6))
    out = info.join(out)

    num = np.zeros(len(out)); var = np.zeros(len(out)); wtot = np.zeros(len(out)); n_ind = np.zeros(len(out))
    for k, (w, _) in INDICATORI.items():
        N, O, E = (out[f"{k}_{c}"].fillna(0).to_numpy() for c in "NOE")
        out[f"{k}_tasso"] = np.where(N > 0, O / np.maximum(N, 1), np.nan)
        out[f"{k}_atteso"] = np.where(N > 0, E / np.maximum(N, 1), np.nan)
        lo, hi = wilson(O, N)
        out[f"{k}_ic90_basso"], out[f"{k}_ic90_alto"] = lo, hi
        lrr = np.clip(np.log((O + 1) / (E + 1)), -math.log(10), math.log(10))
        out[f"{k}_rr"] = np.where(N > 0, np.exp(lrr), np.nan)
        usa = N >= 10
        num += np.where(usa, w * lrr, 0)
        var += np.where(usa, w**2 / (O + 1), 0)
        wtot += np.where(usa, w, 0)
        n_ind += usa
    with np.errstate(invalid="ignore", divide="ignore"):
        lc = num / wtot
        se = np.sqrt(var) / wtot
    out["indicatori_valutati"] = n_ind
    out["indice"] = np.exp(lc)                      # 1 = in linea con la media nazionale per lo stesso mix
    out["indice_ic90_basso"] = np.exp(lc - Z90 * se)
    out["indice_ic90_alto"] = np.exp(lc + Z90 * se)
    nat = out["natura"].fillna("")
    out["ente_pubblico"] = nat.map(lambda s: any(p in s for p in PUBBLICI))
    out["in_graduatoria"] = out["ente_pubblico"] & (out["n_cig"] >= MIN_CIG) & (n_ind >= MIN_INDICATORI)
    # Carta SIC: nessuna persona fisica nell'output, nemmeno se registrata come stazione appaltante
    persona = (out.index.str.len() == 16) | nat.str.contains("INDIVIDUAL|PROFESSIONIST|LAVORATORI AUTONOMI")
    out = out[~persona].sort_values("indice_ic90_basso", ascending=False)
    out.index.name = "cf_ente"
    return out


def per_settore(df: pd.DataFrame) -> pd.DataFrame:
    """Tassi nazionali per divisione CPV (settore merceologico) e tipo di contratto, con IC 90%."""
    g = df.groupby(["oggetto_principale_contratto", "cpv2"])
    out = g.agg(n_cig=("cig", "size"), valore_mln=("importo", lambda s: s.sum() / 1e6),
                descrizione=("cod_cpv", "first"))
    for k in INDICATORI:
        a = g[k].agg(["count", "sum"])
        lo, hi = wilson(a["sum"].to_numpy(), a["count"].to_numpy())
        out[f"{k}_N"] = a["count"]
        out[f"{k}_tasso"] = np.where(a["count"] > 0, a["sum"] / a["count"].clip(lower=1), np.nan)
        out[f"{k}_ic90"] = [f"{x:.3f}-{y:.3f}" if c > 0 else "" for x, y, c in zip(lo, hi, a["count"])]
    out = out.drop(columns="descrizione")
    return out[out["n_cig"] >= 200].sort_values("valore_mln", ascending=False)


# --- Rapporto ----------------------------------------------------------------

def pct(x):
    return "n.d." if pd.isna(x) else f"{100 * x:.1f}%"


def rapporto(df: pd.DataFrame, enti: pd.DataFrame, settori: pd.DataFrame, anno: int, nominativo: bool = False) -> str:
    naz = {k: df[k].mean() for k in INDICATORI}
    nval = {k: int(df[k].notna().sum()) for k in INDICATORI}
    top = enti[enti["in_graduatoria"]].head(20)
    L = [f"# Rischio negli appalti pubblici: indicatori per stazione appaltante ({anno})", "",
         f"*Generato da `trasparenza/indicatori.py` il {date.today().isoformat()}. Fonte: ANAC, BDNCP open data "
         f"(CIG pubblicati nel {anno}, aggiudicazioni, aggiudicatari, varianti, anagrafe stazioni appaltanti).*", "",
         "> **Avviso.** Questi indicatori **non sono prove né accuse**. Misurano quanto le procedure di un ente si "
         "discostano dalla media nazionale per lo stesso tipo di contratti. Molti scostamenti hanno spiegazioni "
         "legittime: urgenze reali, mercati con un solo fornitore qualificato, errori o ritardi nella compilazione "
         "dei dati ANAC. L'elenco serve a **orientare** controlli interni, ANAC e Corte dei conti e a chiedere "
         "trasparenza; ogni caso va verificato da persone competenti, sentendo l'ente.", "",
         "## Campione", "",
         "- CIG analizzati (esclusi cancellati, adesioni a convenzioni/accordi quadro senza confronto, in house): "
         + f"**{len(df):,}**".replace(",", "."),
         f"- Stazioni appaltanti: **{df['cf_amministrazione_appaltante'].nunique():,}**".replace(",", ".")
         + f"; in graduatoria (enti pubblici con almeno {MIN_CIG} CIG e {MIN_INDICATORI} indicatori valutabili): "
         + f"**{int(enti['in_graduatoria'].sum()):,}**".replace(",", "."),
         f"- Valore a base di gara: **{df['importo'].sum() / 1e9:,.1f} mld €**".replace(",", "X").replace(".", ",").replace("X", "."), "",
         "## Indicatori, pesi e media nazionale", "",
         "| Indicatore | Peso | Casi valutabili | Media nazionale |", "|---|---|---|---|"]
    for k, (w, desc) in INDICATORI.items():
        L.append(f"| {desc} (`{k}`) | {w:.2f} | {nval[k]:,} | {pct(naz[k])} |".replace(",", "."))
    L += ["", "**Indice composito.** Per ogni indicatore si confrontano i segnali osservati (O) con quelli attesi (E) "
          "se l'ente avesse i tassi nazionali del suo stesso mix di contratti (lavori/servizi/forniture × fascia "
          "d'importo). Rapporto di rischio = (O+1)/(E+1); l'indice è la media geometrica pesata dei rapporti "
          "(1 = in linea con la media nazionale; 2 = il doppio dei segnali attesi). L'intervallo al 90% assume "
          "indipendenza tra indicatori ed è quindi ottimistico. La graduatoria usa il **limite inferiore** "
          "dell'intervallo, per non premiare gli scostamenti dovuti al caso nei piccoli numeri.", "",
          ]
    if nominativo:
        L += ["## Prime 20 stazioni appaltanti pubbliche per indice (limite inferiore IC 90%)", "",
              "| # | Ente | Regione | CIG | Valore (mln €) | Indice [IC 90%] | Principali scostamenti (ente vs atteso, casi) |",
              "|---|---|---|---|---|---|---|"]
        for i, (cf, r) in enumerate(top.iterrows(), 1):
            contr = []
            for k, (w, _) in INDICATORI.items():
                N = r[f"{k}_N"]
                if pd.notna(N) and N >= 10 and r[f"{k}_rr"] > 1.5:
                    contr.append((w * math.log(r[f"{k}_rr"]),
                                  f"{k}: {pct(r[f'{k}_tasso'])} vs {pct(r[f'{k}_atteso'])} (N={int(N)})"))
            spieg = "; ".join(t for _, t in sorted(contr, reverse=True)[:3]) or "-"
            if r["urgenza_N"] >= 10 and r["urgenza_tasso"] > 0.1:
                spieg += ". *Urgenza frequente: verificare eventi calamitosi (es. alluvioni 2023) o emergenze*"
            reg = str(r["regione"]).replace("SEZIONE REGIONALE ", "").title()
            L.append(f"| {i} | {r['denominazione']} (CF {cf}) | {reg} | {int(r['n_cig'])} | {r['valore_mln']:.1f} | "
                     f"{r['indice']:.2f} [{r['indice_ic90_basso']:.2f}-{r['indice_ic90_alto']:.2f}] | {spieg} |")

    else:
        # Versione pubblica: nessun ente nominato. I dati per ente restano riservati (riservato/, escluso dal
        # repository) finché un controllo umano non ha verificato le spiegazioni legittime (urgenze, mercati, errori).
        g = enti[enti["in_graduatoria"]].copy()
        g["sopra_atteso"] = g["indice_ic90_basso"] > 1
        L += ["## Quadro per tipo di ente e per regione (nessun ente nominato)", "",
              "La versione pubblica non nomina singoli enti: un indicatore di rischio non è un accertamento e può "
              "dipendere da urgenze reali, mercati con pochi operatori o errori nei dati. L'elenco nominativo serve "
              "solo a orientare verifiche da parte di persone competenti e resta fuori dalla pubblicazione.", "",
              "| Tipo di ente | Enti in graduatoria | Indice medio | Enti sopra l'atteso (IC 90%) |", "|---|---|---|---|"]
        for nat, r in g.groupby("natura").agg(n=("indice", "size"), m=("indice", "mean"), s=("sopra_atteso", "sum"))                 .sort_values("n", ascending=False).head(12).iterrows():
            L.append(f"| {str(nat).title()} | {int(r.n)} | {r.m:.2f} | {int(r.s)} |")
        L += ["", "| Regione | Enti in graduatoria | Indice medio | Enti sopra l'atteso (IC 90%) |", "|---|---|---|---|"]
        for reg, r in g.groupby("regione").agg(n=("indice", "size"), m=("indice", "mean"), s=("sopra_atteso", "sum"))                 .sort_values("m", ascending=False).iterrows():
            L.append(f"| {str(reg).replace('SEZIONE REGIONALE ', '').title()} | {int(r.n)} | {r.m:.2f} | {int(r.s)} |")
    L += ["", ("Dati completi per tutti gli enti: `trasparenza/riservato/rischio_enti.csv` (non pubblicato). "
               if nominativo else "") + "Tassi nazionali per settore (divisione CPV): `trasparenza/rischio_settori.csv`.", "",
          "## Settori con i tassi più alti di offerta unica (almeno 200 casi valutabili)", "",
          "| Contratto | CPV (divisione) | CIG | Valore (mln €) | Offerta unica | Non competitiva oltre soglia |",
          "|---|---|---|---|---|---|"]
    s = settori[settori["offerta_unica_N"] >= 200].sort_values("offerta_unica_tasso", ascending=False).head(10)
    for (ogg, cpv), r in s.iterrows():
        L.append(f"| {ogg.title()} | {cpv} | {int(r['n_cig'])} | {r['valore_mln']:.0f} | "
                 f"{pct(r['offerta_unica_tasso'])} (N={int(r['offerta_unica_N'])}) | {pct(r['non_competitiva_tasso'])} |")
    L += ["", "## Come leggere (e come non leggere) questa tabella", "",
          "- Un ente in cima non è un ente corrotto: è un ente le cui procedure **meritano una domanda**. "
          "La prima verifica è chiedere all'ente le motivazioni (determine a contrarre, motivazione dell'urgenza, "
          "indagini di mercato, deroghe alla rotazione).",
          "- Grandi centrali di committenza e aziende sanitarie hanno mix di acquisti particolari (farmaci, dispositivi "
          "esclusivi): l'offerta unica può dipendere dal mercato.",
          "- Difesa, Vigili del fuoco, prefetture (accoglienza) e protezione civile operano spesso con deroghe di legge "
          "(segretezza, somma urgenza, emergenze): lo scostamento va letto alla luce della norma applicata.",
          "- Nei comuni piccoli e nelle aree interne gli operatori locali sono pochi: affidamenti ripetuti allo stesso "
          "operatore possono dipendere dal mercato, ma la deroga alla rotazione va comunque motivata (art. 49).",
          "- I valori a base di gara possono contenere errori di compilazione (importi anomali): il valore in milioni "
          "è indicativo e non entra nell'indice.",
          "- Gli enti che **non comunicano** i dati ad ANAC risultano meno a rischio di quanto siano: la mancanza di dati "
          "è a sua volta un segnale (UIF, Quaderno 23/2024) e va letta a parte.",
          "- Nessuna persona fisica è valutata. I codici degli operatori economici sono usati solo come codici anonimi "
          "per contare ripetizioni dentro lo stesso ente.", ""]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--anno", type=int, default=2024)
    a = ap.parse_args()
    df = flag_cig(carica(a.anno))
    enti = per_ente(df)
    settori = per_settore(df)
    cols = ["denominazione", "natura", "regione", "provincia", "ente_pubblico", "in_graduatoria", "n_cig", "valore_mln",
            "indicatori_valutati", "indice", "indice_ic90_basso", "indice_ic90_alto"]
    for k in INDICATORI:
        cols += [f"{k}_{c}" for c in ("N", "O", "E", "tasso", "atteso", "ic90_basso", "ic90_alto", "rr")]
    riservato = QUI / "riservato"  # escluso dal repository pubblico (.gitignore)
    riservato.mkdir(exist_ok=True)
    enti[cols].round(4).to_csv(riservato / "rischio_enti.csv")
    (riservato / "rapporto_enti.md").write_text(rapporto(df, enti, settori, a.anno, nominativo=True), encoding="utf-8")
    settori.round(4).to_csv(QUI / "rischio_settori.csv")
    (QUI / "rapporto.md").write_text(rapporto(df, enti, settori, a.anno), encoding="utf-8")
    print(f"CIG analizzati: {len(df):,}; enti: {len(enti):,}; in graduatoria: {int(enti['in_graduatoria'].sum()):,}")
    for k in INDICATORI:
        print(f"  {k:16s} valutabili {df[k].notna().sum():>9,}  media {df[k].mean():.3f}")


if __name__ == "__main__":
    main()
