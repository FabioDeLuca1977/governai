"""Motore decisionale di GovernAI: valutazione robusta ai valori (SMAA) e pacchetti per budget.

Applica le regole della Carta dei valori (01_carta_valori.md):
  - consolida i punteggi del panel di valutatori indipendenti e misura il loro accordo;
  - esplora tutte le combinazioni di pesi tra i 7 valori (pesi uniformi sul simplesso)
    e tra gli orizzonti, con il lungo periodo che pesa almeno quanto il breve;
  - a ogni estrazione campiona, cella per cella, il punteggio di uno dei valutatori,
    così il disaccordo del panel entra nell'incertezza;
  - classifica le proposte per robustezza: robuste, dipendenti dai valori, sfavorevoli;
  - per ogni livello di budget sceglie il pacchetto con più valore (problema dello zaino)
    e conta quanto spesso ogni proposta entra nel pacchetto al variare dei pesi.

Uso:  python decidi.py [--n 10000] [--budget 4 10 18] [--seed 42]
Scrive esito.md e esito_proposte.csv accanto a questo file.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

QUI = Path(__file__).resolve().parent


def _valori_dalla_carta() -> dict[str, str]:
    """La Carta dei valori è l'unica fonte dell'elenco dei valori (codice -> nome)."""
    testo = (QUI.parent / "01_carta_valori.md").read_text(encoding="utf-8")
    return {m.group(2): m.group(1) for m in re.finditer(r"^### \d+\. (.+?) \((\w{3})\)$", testo, re.M)}


NOMI = _valori_dalla_carta()
VALORI = list(NOMI)
ORIZZ = ["breve", "medio", "lungo"]
CONF = {"A": 1.0, "M": 0.75, "B": 0.5}
PASSO = 0.05  # granularità del budget nel problema dello zaino (mld)
SOGLIA_ROBUSTA = 0.95  # quota di combinazioni di pesi in cui una proposta deve essere utile
SOGLIA_NUCLEO = 0.75   # P(prima metà della classifica) per il nucleo robusto
SOGLIA_CODA = 0.25     # sotto questa soglia la proposta è stabilmente in coda


# --- Dati -------------------------------------------------------------------

def carica_panel() -> tuple[np.ndarray, pd.DataFrame, list[str], list[str]]:
    """Restituisce S[r, p, v, h], la tabella lunga dei punteggi, valutatori e proposte."""
    file = sorted(QUI.glob("punteggi_*.csv"))
    if len(file) < 2:
        sys.exit("Servono almeno due file punteggi_*.csv del panel.")
    prop = pd.read_csv(QUI / "proposte.csv")
    ids = prop.proposta_id.tolist()
    tabelle, valutatori = [], []
    for f in file:
        t = pd.read_csv(f)
        t["valutatore"] = f.stem.split("_", 1)[1]
        valutatori.append(t.valutatore.iloc[0])
        mancanti = set((p, v) for p in ids for v in VALORI) - set(zip(t.proposta_id, t.valore))
        if mancanti:
            sys.exit(f"{f.name}: mancano {len(mancanti)} coppie proposta×valore, es. {sorted(mancanti)[:3]}")
        tabelle.append(t)
    lunga = pd.concat(tabelle, ignore_index=True)
    S = np.zeros((len(file), len(ids), len(VALORI), 3), dtype=np.int8)
    pi = {p: i for i, p in enumerate(ids)}
    vi = {v: i for i, v in enumerate(VALORI)}
    ri = {r: i for i, r in enumerate(valutatori)}
    for r in lunga.itertuples(index=False):
        if r.proposta_id in pi:
            S[ri[r.valutatore], pi[r.proposta_id], vi[r.valore]] = [r.breve, r.medio, r.lungo]
    return S, lunga, valutatori, ids


def alfa_krippendorff(S: np.ndarray) -> float:
    """Alfa di Krippendorff per dati a intervalli, senza dati mancanti. Unità = celle p×v×h."""
    X = S.reshape(S.shape[0], -1).T.astype(float)  # unità × valutatori
    m = X.shape[1]
    d_oss = np.mean([((X[:, i] - X[:, j]) ** 2).mean() for i in range(m) for j in range(m) if i != j])
    tutti = X.ravel()
    d_att = 2 * tutti.var(ddof=1)  # media delle differenze quadratiche tra tutte le coppie
    return 1 - d_oss / d_att if d_att > 0 else float("nan")


# --- SMAA --------------------------------------------------------------------

def pesi_orizzonte(rng: np.random.Generator, n: int) -> np.ndarray:
    """Pesi (breve, medio, lungo) uniformi sul simplesso, con lungo >= breve (Carta, regola 2)."""
    out = np.empty((0, 3))
    while len(out) < n:
        h = rng.dirichlet(np.ones(3), size=2 * n)
        out = np.vstack([out, h[h[:, 2] >= h[:, 0]]])
    return out[:n]


def calibrazione(ids: list[str]) -> np.ndarray:
    """Fattori per proposta dall'apprendimento (apprendimento/calibrazione.csv, per area): 1 se non ci sono esiti."""
    f = QUI.parent / "apprendimento" / "calibrazione.csv"
    per_area = dict(pd.read_csv(f, dtype={"area": str})[["area", "fattore"]].values) if f.exists() else {}
    return np.array([float(per_area.get(p[:2], 1.0)) for p in ids])


def simula(S: np.ndarray, n: int, rng: np.random.Generator, fattori: np.ndarray | None = None) -> dict:
    R, P, V, H = S.shape
    W = rng.dirichlet(np.ones(V), size=n)          # pesi tra i valori
    Hw = pesi_orizzonte(rng, n)                    # pesi tra gli orizzonti
    U = np.empty((n, P), dtype=np.float32)
    for a in range(0, n, 1000):
        b = min(a + 1000, n)
        k = b - a
        scelta = rng.integers(0, R, size=(k, P, V, H))
        cell = np.take_along_axis(S[None].repeat(k, 0).transpose(0, 2, 3, 4, 1),
                                  scelta[..., None], axis=-1)[..., 0].astype(np.float32)  # k,P,V,H
        per_valore = np.einsum("kpvh,kh->kpv", cell, Hw[a:b])
        U[a:b] = np.einsum("kpv,kv->kp", per_valore, W[a:b])
    if fattori is not None:
        # l'esperienza ridimensiona (o rafforza) i benefici attesi delle aree che rendono meno (o più) del previsto
        U = np.where(U > 0, U * fattori[None, :].astype(np.float32), U)
    rango = (-U).argsort(1).argsort(1) + 1
    return {"W": W, "H": Hw, "U": U, "rango": rango}


def valori_trainanti(W: np.ndarray, u: np.ndarray, k: int = 2) -> str:
    """I valori il cui peso fa crescere di più il giudizio sulla proposta."""
    if u.std() == 0:
        return ""
    c = [np.corrcoef(W[:, j], u)[0, 1] for j in range(W.shape[1])]
    top = [VALORI[j] for j in np.argsort(c)[::-1][:k] if c[j] > 0.1]
    return ", ".join(NOMI[v] for v in top)


# --- Pacchetti per budget ----------------------------------------------------

def zaino(valore: np.ndarray, costo: np.ndarray, budget: float) -> np.ndarray:
    """Massimizza la somma dei valori positivi con costo totale <= budget. Restituisce la selezione."""
    c = np.ceil(costo / PASSO - 1e-9).astype(int)
    C = int(round(budget / PASSO))
    P = len(valore)
    dp = np.zeros(C + 1)
    tieni = np.zeros((P, C + 1), dtype=bool)
    for i in range(P):
        if valore[i] <= 0 or c[i] > C:
            continue
        cand = np.full(C + 1, -np.inf)
        cand[c[i]:] = dp[: C + 1 - c[i]] + valore[i]
        migliore = cand > dp
        tieni[i] = migliore
        dp = np.where(migliore, cand, dp)
    sel = np.zeros(P, dtype=bool)
    cap = C
    for i in range(P - 1, -1, -1):
        if tieni[i, cap]:
            sel[i] = True
            cap -= c[i]
    return sel


def frequenze_pacchetto(U: np.ndarray, costo: np.ndarray, budget: float, campioni: int,
                        rng: np.random.Generator) -> np.ndarray:
    idx = rng.choice(len(U), size=min(campioni, len(U)), replace=False)
    conta = np.zeros(U.shape[1])
    for i in idx:
        conta += zaino(U[i].astype(float), costo, budget)
    return conta / len(idx)


# --- Uscita ------------------------------------------------------------------

def num(v: float, dec: int = 2) -> str:
    return f"{v:,.{dec}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def pct(v: float) -> str:
    return f"{v * 100:.0f}%"


def tabella(df: pd.DataFrame, col: dict[str, str]) -> str:
    righe = ["| " + " | ".join(col.values()) + " |", "|" + "|".join("---" for _ in col) + "|"]
    for _, r in df.iterrows():
        righe.append("| " + " | ".join(str(r[c]) for c in col) + " |")
    return "\n".join(righe)


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=10000, help="estrazioni SMAA")
    ap.add_argument("--budget", type=float, nargs="+", default=[4, 10, 18], help="mld €/anno")
    ap.add_argument("--campioni-zaino", type=int, default=1500)
    ap.add_argument("--seed", type=int, default=42)
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)

    S, lunga, valutatori, ids = carica_panel()
    prop = pd.read_csv(QUI / "proposte.csv").set_index("proposta_id").loc[ids]
    # Il costo opportunità conta le risorse che una proposta sottrae al programma senza spenderle:
    # il dividendo climatico (03-P1) restituisce ai cittadini il gettito SAD che altrimenti finanzierebbe servizi.
    opp = prop.get("costo_opportunita", pd.Series(0.0, index=prop.index)).fillna(0)
    costo = ((prop.costo_min + prop.costo_max) / 2 + opp).clip(lower=0).to_numpy()

    # Accordo del panel
    alfa = alfa_krippendorff(S)
    escursione = S.max(0).astype(int) - S.min(0).astype(int)    # p, v, h
    lunga["conf_num"] = lunga.confidenza.map(CONF)
    conf = lunga.groupby("proposta_id").conf_num.mean().reindex(ids)
    rosse = lunga[lunga.linea_rossa.astype(str).str.lower().eq("si")]

    # SMAA
    sim = simula(S, a.n, rng, fattori=calibrazione(ids))
    U, rango, W = sim["U"], sim["rango"], sim["W"]
    P = len(ids)
    quartile = int(np.ceil(P / 4))
    mediana = np.median(S, axis=0)  # p, v, h

    ris = pd.DataFrame({
        "proposta_id": ids,
        "titolo": prop.titolo.to_numpy(),
        "costo_medio": costo,
        "utilita_attesa": U.mean(0),
        "p_beneficio": (U > 0).mean(0),
        "p_primo_quartile": (rango <= quartile).mean(0),
        "p_prima_meta": (rango <= P / 2).mean(0),
        "rango_p5": np.percentile(rango, 5, axis=0).astype(int),
        "rango_p95": np.percentile(rango, 95, axis=0).astype(int),
        "disaccordo_medio": escursione.reshape(P, -1).mean(1),
        "confidenza_media": conf.to_numpy(),
    })
    for j, v in enumerate(VALORI):
        ris[v] = mediana[:, j, :].mean(1)
    # Quasi tutte le proposte sono utili in sé: ciò che conta, con risorse scarse, è la priorità relativa.
    # Le classi si basano quindi sulla probabilità di stare nella prima metà della classifica.
    ris["classe"] = np.select(
        [ris.p_beneficio < 0.5, ris.p_prima_meta >= SOGLIA_NUCLEO, ris.p_prima_meta > SOGLIA_CODA],
        ["sfavorevole", "robusta", "dipendente dai valori"], "in coda")
    ris["valori_trainanti"] = [valori_trainanti(W, -rango[:, i].astype(float)) if ris.classe[i] != "robusta" else ""
                               for i in range(P)]
    ris["valore_per_mld"] = np.where(costo > 0.05, ris.utilita_attesa / np.maximum(costo, 0.05), np.nan)
    ris["linea_rossa"] = ris.proposta_id.isin(rosse.proposta_id)

    for B in a.budget:
        ris[f"pacchetto_{num(B, 0)}"] = frequenze_pacchetto(U, costo, B, a.campioni_zaino, rng)

    ris.sort_values(["classe", "utilita_attesa"], ascending=[True, False]).to_csv(
        QUI / "esito_proposte.csv", index=False)

    # --- esito.md
    out = ["# GovernAI — Esito del motore decisionale", "",
           "*Generato da `motore/decidi.py`. Metodo: analisi di accettabilità multicriterio stocastica (SMAA) "
           "sui 7 valori della Carta, con il panel indipendente come fonte dei punteggi.*", "",
           f"- Valutatori: **{', '.join(valutatori)}**. Estrazioni: **{num(a.n, 0)}** combinazioni di pesi tra valori e orizzonti "
           "(lungo periodo ≥ breve).",
           f"- Accordo del panel (alfa di Krippendorff, intervalli): **{num(alfa)}**. "
           "Sopra 0,67 l'accordo è accettabile per conclusioni provvisorie; sopra 0,80 è buono.",
           f"- Celle con disaccordo forte (escursione ≥ 3 punti): **{int((escursione >= 3).sum())}** su {escursione.size}.",
           f"- Proposte utili (effetto netto positivo) con almeno il {pct(SOGLIA_ROBUSTA)} delle combinazioni di pesi: "
           f"**{int((ris.p_beneficio >= SOGLIA_ROBUSTA).sum())} su {P}**. Quasi tutto è utile in sé: con risorse scarse conta la **priorità relativa**.",
           f"- Classi per priorità, in base alla probabilità di stare nella prima metà della classifica, P(1ª metà): "
           f"**nucleo robusto** ≥ {pct(SOGLIA_NUCLEO)}; **dipendente dai valori** tra {pct(SOGLIA_CODA)} e {pct(SOGLIA_NUCLEO)}; "
           f"**in coda** ≤ {pct(SOGLIA_CODA)}; **sfavorevole** se è utile in meno della metà delle combinazioni.", ""]

    ris_v = ris.copy()
    ris_v["U"] = ris_v.utilita_attesa.map(num)
    ris_v["P(utile)"] = ris_v.p_beneficio.map(pct)
    ris_v["P(top 25%)"] = ris_v.p_primo_quartile.map(pct)
    ris_v["P(1ª metà)"] = ris_v.p_prima_meta.map(pct)
    ris_v["Valore/mld"] = ris_v.valore_per_mld.map(lambda x: "—" if pd.isna(x) else num(x))
    ris_v["Rango"] = ris_v.rango_p5.astype(str) + "–" + ris_v.rango_p95.astype(str)
    ris_v["Costo"] = ris_v.costo_medio.map(lambda c: num(c, 1))
    ris_v["Disacc."] = ris_v.disaccordo_medio.map(lambda x: num(x, 1))
    for B in a.budget:
        ris_v[f"B{num(B, 0)}"] = ris_v[f"pacchetto_{num(B, 0)}"].map(pct)
    col = {"proposta_id": "Proposta", "titolo": "Titolo", "U": "Utilità attesa", "P(1ª metà)": "P(1ª metà)",
           "P(top 25%)": "P(top 25%)", "Rango": "Rango 5–95%", "Costo": "Costo", "Valore/mld": "Valore/mld",
           "Disacc.": "Disacc."}
    col_b = {f"B{num(B, 0)}": f"Pacchetto {num(B, 0)} mld" for B in a.budget}

    for classe, titolo_sez, intro in [
        ("robusta", "Nucleo robusto", "In cima alla classifica qualunque sia il peso dato ai valori: il **nucleo condiviso** del programma."),
        ("dipendente dai valori", "Priorità dipendente dai valori", "La posizione in classifica cambia molto con i pesi: **qui la scelta è politica**. "
         "La colonna finale indica quali valori la fanno salire."),
        ("in coda", "In coda", "Utili, ma stabilmente in fondo alla classifica: **da migliorare o rinviare**."),
        ("sfavorevole", "Sfavorevoli", "Effetto netto negativo con la maggior parte delle combinazioni di pesi: **da ripensare**."),
    ]:
        sub = ris_v[ris_v.classe == classe].sort_values("utilita_attesa", ascending=False)
        out += [f"## {titolo_sez} ({len(sub)})", "", intro, ""]
        if len(sub):
            c = dict(col)
            if classe != "robusta":
                c["valori_trainanti"] = "Dipende soprattutto da"
            out += [tabella(sub, {**c, **col_b}), ""]

    out += ["## Pacchetti per livello di budget", "",
            "Per ogni livello di risorse permanenti (mld €/anno a regime) il motore sceglie l'insieme di proposte con più valore "
            "che sta nel budget, per ogni combinazione di pesi. La percentuale indica quanto spesso la proposta entra nel pacchetto.",
            "Le proposte a costo zero o che generano risorse entrano sempre, se utili. "
            "Il budget va inteso **al netto** delle politiche invariate (10–14 mld/anno, `registro/`).",
            "Il dividendo climatico (03-P1) ha un costo opportunità di 5 mld, cioè il gettito SAD che non finanzia altre proposte. "
            "Proposte più costose dell'intero budget (es. la Difesa, 32 mld) non possono entrare: la loro traiettoria è una decisione a parte.", ""]
    for B in a.budget:
        f = ris[f"pacchetto_{num(B, 0)}"]
        nucleo = ris[f >= 0.8].sort_values("utilita_attesa", ascending=False)
        variabile = ris[(f >= 0.2) & (f < 0.8)].sort_values(f"pacchetto_{num(B, 0)}", ascending=False)
        out += [f"### Budget {num(B, 0)} mld/anno", "",
                f"- **Entrano quasi sempre (≥80%)** — costo {num(nucleo.costo_medio.sum(), 1)} mld: "
                + (", ".join(f"{r.proposta_id} {r.titolo}" for r in nucleo.itertuples()) or "nessuna"),
                f"- **Entrano a seconda dei valori (20–80%)**: "
                + (", ".join(f"{r.proposta_id} ({pct(getattr(r, f'pacchetto_{num(B, 0)}'))})" for r in variabile.itertuples()) or "nessuna"),
                ""]

    if len(rosse):
        out += ["## Linee rosse segnalate dal panel", "",
                tabella(rosse[["proposta_id", "valore", "valutatore", "motivazione"]],
                        {"proposta_id": "Proposta", "valore": "Valore", "valutatore": "Valutatore", "motivazione": "Motivazione"}), ""]

    forte = [(ids[p], VALORI[v], ORIZZ[h], int(escursione[p, v, h]))
             for p, v, h in zip(*np.where(escursione >= 3))]
    if forte:
        out += ["## Celle con disaccordo forte del panel", "",
                "Da discutere nella prossima tornata: i valutatori vedono effetti molto diversi.", "",
                ", ".join(f"{p} {v} {h} (±{e})" for p, v, h, e in forte[:60]) + (" …" if len(forte) > 60 else ""), ""]

    out += ["## Limiti", "",
            "- I punteggi sono giudizi esperti strutturati, non misure: la loro qualità dipende dai dossier e dal panel.",
            "- Il costo usato è il punto medio della stima; budget e costi a regime si riferiscono ad anni diversi.",
            "- La scala da −3 a +3 è limitata: un grande programma nazionale e una piccola riforma possono ricevere punteggi simili. "
            "Il pacchetto per budget tende quindi a favorire le misure economiche. È coerente con la Carta (regola 6), "
            "ma le proposte costose con utilità alta vanno lette come **\"entrano con più risorse\"**, non come proposte di poco valore.",
            "- L'alfa di Krippendorff è alto anche perché molte celle valgono 0 per tutti i valutatori: l'accordo sui punteggi diversi da zero è più basso.",
            "- Il pacchetto rispetta il budget complessivo; la compatibilità con i singoli fondi va verificata con `registro/controlla.py`.",
            "- La distribuzione dei pesi è uniforme: quando l'assemblea dei cittadini esprimerà i suoi pesi, diventeranno lo scenario centrale.", ""]
    (QUI / "esito.md").write_text("\n".join(out), encoding="utf-8")

    print(f"alfa Krippendorff {alfa:.2f}; classi: {ris.classe.value_counts().to_dict()}")
    print("-> esito.md, esito_proposte.csv")
    return 0


if __name__ == "__main__":
    sys.exit(main())
