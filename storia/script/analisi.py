"""Analisi delle serie lunghe: medie per decennio, divario Italia - media FR/DE/ES,
rotture strutturali (test semplice).

Uso:  python storia/script/analisi.py
Scrive:
  storia/serie/_decenni.csv   medie per periodo, per indicatore e paese
  storia/serie/_rotture.csv   anni di rottura stimati (Italia e divario Italia-confronto)
  storia/script/_cache/tabelle.md  tabelle in markdown usate per il rapporto

Metodo delle rotture (indicativo, non una prova causale)
- Serie "di flusso" (crescite, inflazione, saldi, tassi): rottura nella media.
- Serie "di livello" con tendenza (debito, quote, occupazione...): rottura nella
  tendenza lineare (cambia livello e pendenza).
- Ricerca per segmentazione binaria (fino a 3 rotture, segmenti di almeno 6 anni):
  in ogni segmento si sceglie l'anno che minimizza la somma dei quadrati dei residui
  e si tiene la rottura se la statistica F supera il valore critico di Andrews (1993)
  al 5% con trimming 15% (8,85 per 1 parametro; 11,79 per 2 parametri).
  I residui sono autocorrelati: le F sono gonfiate, quindi le rotture vanno lette
  come "anni in cui la serie cambia comportamento", da verificare.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from comune import CACHE, SERIE

PERIODI = [("1970-79", 1970, 1979), ("1980-89", 1980, 1989), ("1990-99", 1990, 1999),
           ("2000-09", 2000, 2009), ("2010-19", 2010, 2019), ("2020-25", 2020, 2025)]
CONFRONTO = ["FR", "DE", "ES"]

# nome serie -> (etichetta breve, tipo: 'media' o 'tendenza')
INDICATORI = {
    "pil_reale_crescita": ("Crescita PIL reale, %", "media"),
    "pil_pro_capite_crescita": ("Crescita PIL pro capite reale, %", "media"),
    "pil_pro_capite_pps_ue27": ("PIL pro capite PPA, UE27=100", "tendenza"),
    "produttivita_oraria_crescita": ("Crescita produttivita' oraria, %", "media"),
    "occupazione_15_64": ("Tasso di occupazione 15-64, %", "tendenza"),
    "occupazione_femminile_15_64": ("Occupazione femminile 15-64, %", "tendenza"),
    "disoccupazione": ("Disoccupazione, %", "tendenza"),
    "disoccupazione_giovanile": ("Disoccupazione 15-24, %", "tendenza"),
    "inflazione": ("Inflazione, %", "media"),
    "debito_pil": ("Debito pubblico, % PIL", "tendenza"),
    "deficit_pil": ("Saldo di bilancio, % PIL", "media"),
    "saldo_primario_pil": ("Saldo primario, % PIL", "media"),
    "interessi_pil": ("Spesa per interessi, % PIL", "tendenza"),
    "pressione_fiscale_ocse": ("Pressione fiscale (OCSE), % PIL", "tendenza"),
    "pressione_fiscale": ("Pressione fiscale (AMECO), % PIL", "tendenza"),
    "spesa_pubblica_pil": ("Spesa pubblica, % PIL", "tendenza"),
    "spesa_pensioni_pil": ("Spesa per vecchiaia, % PIL", "tendenza"),
    "investimenti_pubblici_pil": ("Investimenti pubblici, % PIL", "tendenza"),
    "tasso_lungo": ("Tasso a 10 anni, %", "media"),
    "spread_bund": ("Spread sul Bund, punti base", "media"),
    "gini_reddito_disponibile": ("Gini reddito disponibile (EU-SILC)", "tendenza"),
    "gini_ocse": ("Gini reddito disponibile (OCSE)", "tendenza"),
    "rischio_poverta": ("Rischio di poverta' relativa, %", "tendenza"),
    "poverta_assoluta": ("Poverta' assoluta individui, %", "tendenza"),
    "fecondita": ("Fecondita', figli per donna", "tendenza"),
    "saldo_migratorio": ("Saldo migratorio per 1.000 ab.", "media"),
    "emigrazione_cittadini": ("Emigrati con cittadinanza, migliaia", "tendenza"),
    "laureati_25_34": ("Laureati 25-34, %", "tendenza"),
    "divario_nord_sud": ("PIL pc Mezzogiorno, % Centro-Nord", "tendenza"),
}

F_CRIT = {"media": 8.85, "tendenza": 11.79}


def ssr_media(y):
    return float(((y - y.mean()) ** 2).sum())


def ssr_tendenza(y):
    t = np.arange(len(y))
    X = np.column_stack([np.ones_like(t), t])
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    return float(((y - X @ b) ** 2).sum())


def miglior_rottura(anni, y, tipo, min_seg=6):
    n = len(y)
    if n < 2 * min_seg:
        return None
    f_ssr = ssr_media if tipo == "media" else ssr_tendenza
    k = 1 if tipo == "media" else 2
    s0 = f_ssr(y)
    lo = max(min_seg, int(np.floor(0.15 * n)))
    hi = min(n - min_seg, n - int(np.floor(0.15 * n)))
    best = None
    for i in range(lo, hi + 1):
        s1 = f_ssr(y[:i]) + f_ssr(y[i:])
        if best is None or s1 < best[1]:
            best = (i, s1)
    if best is None:
        return None
    i, s1 = best
    p = 2 * k
    if s1 <= 0:
        return None
    F = ((s0 - s1) / k) / (s1 / (n - p))
    return {"i": i, "anno": int(anni[i]), "F": F, "significativa": F > F_CRIT[tipo]}


def rotture(anni, y, tipo, max_r=3):
    trovate = []
    segmenti = [(0, len(y))]
    while segmenti and len(trovate) < max_r:
        cand = []
        for a, b in segmenti:
            r = miglior_rottura(anni[a:b], y[a:b], tipo)
            if r and r["significativa"]:
                cand.append((r["F"], a, b, r))
        if not cand:
            break
        cand.sort(key=lambda c: -c[0])
        F, a, b, r = cand[0]
        trovate.append(r["anno"])
        segmenti.remove((a, b))
        segmenti += [(a, a + r["i"]), (a + r["i"], b)]
    return sorted(trovate)


def carica(nome):
    f = SERIE / f"{nome}.csv"
    if not f.exists():
        return None
    d = pd.read_csv(f)
    return d.pivot_table(index="anno", columns="paese", values="valore")


def fmt(x, nd=1):
    return "" if pd.isna(x) else f"{x:.{nd}f}".replace(".", ",")


ANNI_CHIAVE = [1977, 1991, 1999, 2007, 2013, 2019, 2024, 2025]
LIVELLI = ["debito_pil", "occupazione_15_64", "occupazione_femminile_15_64", "disoccupazione",
           "disoccupazione_giovanile", "pressione_fiscale_ocse", "spesa_pubblica_pil", "interessi_pil",
           "fecondita", "laureati_25_34", "pil_pro_capite_pps_ue27", "divario_nord_sud",
           "poverta_assoluta", "spread_bund"]


def indice_cumulato(base: int) -> pd.DataFrame:
    """PIL pro capite reale, indice base=100, ricostruito dalle crescite annue."""
    w = carica("pil_pro_capite_crescita")
    w = w[w.index > base]
    idx = (1 + w / 100).cumprod() * 100
    idx.loc[base] = 100.0
    return idx.sort_index()


def anni_chiave():
    md = ["\n### PIL pro capite reale cumulato (indice 1977 = 100 e 1995 = 100)\n"]
    for base, anni in [(1977, [1991, 1999, 2007, 2013, 2019, 2025]), (1995, [2007, 2013, 2019, 2025])]:
        idx = indice_cumulato(base)
        cols = [p for p in ["IT", "FR", "DE", "ES", "EA", "UE27"] if idx[p].notna().sum() > len(anni)]
        md.append(f"\nBase {base} = 100\n")
        md.append("| Anno | " + " | ".join(cols) + " |")
        md.append("|---|" + "---:|" * len(cols))
        for a in anni:
            md.append(f"| {a} | " + " | ".join(fmt(idx.loc[a, c], 0) for c in cols) + " |")
    md.append("\n### Valori in anni chiave\n")
    for nome in LIVELLI:
        w = carica(nome)
        if w is None:
            continue
        nd = 0 if nome == "spread_bund" else (2 if nome == "fecondita" else 1)
        anni = [a for a in ANNI_CHIAVE if a in w.index]
        cols = [p for p in ["IT", "FR", "DE", "ES", "EA", "UE27", "Nord", "Centro", "Mezzogiorno"] if p in w.columns]
        md.append(f"\n{INDICATORI[nome][0]} (`{nome}`)\n")
        md.append("| Anno | " + " | ".join(cols) + " |")
        md.append("|---|" + "---:|" * len(cols))
        for a in anni:
            md.append(f"| {a} | " + " | ".join(fmt(w.loc[a, c], nd) for c in cols) + " |")
    return md


def main():
    righe_dec, righe_rot, md = [], [], []
    for nome, (etich, tipo) in INDICATORI.items():
        w = carica(nome)
        if w is None:
            continue
        nd = 0 if nome in ("spread_bund",) else (2 if nome == "fecondita" else 1)
        # medie per decennio
        tab = {}
        for per, a, b in PERIODI:
            sub = w.loc[(w.index >= a) & (w.index <= b)]
            m = sub.mean()
            n = sub.count()
            for p in w.columns:
                if n.get(p, 0) > 0:
                    righe_dec.append({"indicatore": nome, "periodo": per, "paese": p,
                                      "media": round(m[p], 3), "anni_con_dati": int(n[p])})
            tab[per] = m
        tab = pd.DataFrame(tab)
        conf = [c for c in CONFRONTO if c in w.columns]
        if "IT" in w.columns and conf:
            gap = w["IT"] - w[conf].mean(axis=1, skipna=False)
            tab.loc["IT - media FR/DE/ES"] = [gap[(gap.index >= a) & (gap.index <= b)].mean()
                                              for _, a, b in PERIODI]
        ordine = [p for p in ["IT", "FR", "DE", "ES", "EA", "UE27", "Centro-Nord", "Mezzogiorno",
                              "Nord", "Centro",
                              "IT - media FR/DE/ES"] if p in tab.index]
        tab = tab.loc[ordine]
        tab = tab.loc[:, tab.notna().any()]
        md.append(f"\n#### {etich} (`{nome}`)\n")
        md.append("| Paese | " + " | ".join(tab.columns) + " |")
        md.append("|---|" + "---:|" * len(tab.columns))
        for p, r in tab.iterrows():
            md.append(f"| {p} | " + " | ".join(fmt(v, nd) for v in r.values) + " |")

        # rotture: Italia e divario Italia - confronto (dal 1977 o primo anno)
        for chi, s in [("IT", w.get("IT")),
                       ("IT - media FR/DE/ES", (w["IT"] - w[conf].mean(axis=1, skipna=False)) if ("IT" in w and conf) else None)]:
            if s is None:
                continue
            s = s.dropna()
            s = s[(s.index >= 1977) & (s.index <= 2025)]
            if len(s) < 12:
                continue
            anni = s.index.values
            y = s.values.astype(float)
            br = rotture(anni, y, tipo)
            confini = [anni[0]] + br + [anni[-1] + 1]
            medie = []
            for a, b in zip(confini[:-1], confini[1:]):
                seg = s[(s.index >= a) & (s.index < b)]
                medie.append(f"{a}-{b - 1}: {fmt(seg.mean(), nd)}")
            righe_rot.append({"indicatore": nome, "serie": chi, "tipo_test": tipo,
                              "anni_rottura": " ".join(map(str, br)) or "nessuna",
                              "medie_per_tratto": "; ".join(medie),
                              "periodo_analizzato": f"{anni[0]}-{anni[-1]}"})
    md += anni_chiave()
    pd.DataFrame(righe_dec).to_csv(SERIE / "_decenni.csv", index=False)
    r = pd.DataFrame(righe_rot)
    r.to_csv(SERIE / "_rotture.csv", index=False)
    (CACHE / "tabelle.md").write_text("\n".join(md), encoding="utf-8")
    pd.set_option("display.width", 250)
    pd.set_option("display.max_colwidth", 120)
    print(r.to_string())


if __name__ == "__main__":
    main()
