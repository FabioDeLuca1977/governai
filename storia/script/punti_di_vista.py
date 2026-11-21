"""Punteggio complessivo dei governi e delle legislature visto da più punti di vista.

Uso:  python storia/script/punti_di_vista.py   (dopo governi.py e legislature.py)

Scrive: storia/punti_di_vista.csv          una riga per governo o legislatura
        storia/punti_di_vista_ambiti.csv   posizione per ambito (serve alla pagina per i pesi del lettore)
        storia/punti_di_vista.md           rapporto leggibile

Perché. Le posizioni per ambito (conti, crescita, lavoro, ...) non si sommano da sole: dare più peso ai conti o al
lavoro è una scelta politica. Un solo punteggio con un solo peso premierebbe chi ha scelto i pesi. Qui il
punteggio si calcola da molti punti di vista e si mostra quanto cambia.

Come.
1. Punto di partenza: la posizione 0-100 di ogni unità in ogni ambito (mediana degli indicatori con un verso,
   la stessa della pagina). Un ambito senza dati (società prima del 2001) resta fuori e i pesi degli altri si
   riproporzionano.
2. Punti di vista dichiarati: pesi uguali; poi, uno per volta, ogni ambito che conta il doppio degli altri.
   Ognuno con gli anni del mandato e con gli anni spostati di uno: 14 punti di vista.
3. Tutti i pesi possibili: 2.000 combinazioni di pesi estratte a caso in modo uniforme (distribuzione di
   Dirichlet con parametri tutti uguali a 1, seme fisso, quindi ripetibile) per ciascuna delle due versioni
   degli anni: 4.000 punti di vista. È l'analisi di sensibilità raccomandata dal manuale OCSE-JRC sugli
   indicatori compositi.
4. Per ogni punto di vista: media pesata delle posizioni per ambito, poi posto tra le unità e posizione 0-100.
   Punteggio equo = mediana delle posizioni sui 4.000 punti di vista; intervallo = 10° e 90° percentile;
   quota dei punti di vista in cui l'unità è nel primo terzo e nell'ultimo terzo.

Chi. Lo script non sceglie i pesi: li prova tutti. Nella pagina il lettore può fissare i propri.
"""
from __future__ import annotations

import csv
import statistics
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import governi as G  # noqa: E402
import legislature as L  # noqa: E402

N_CASUALI = 2000
SEME = 20261121
VERSIONI = ("base", "ritardo_1_anno")
NOMI_AMBITI = {"conti": "prima i conti", "crescita": "prima la crescita", "lavoro": "prima il lavoro",
               "qualità del lavoro": "prima la qualità del lavoro", "prezzi e mercati": "prima prezzi e mercati",
               "società": "prima la società"}


def punti_dichiarati() -> list[tuple[str, dict]]:
    pv = [("pesi uguali", {a: 1.0 for a in G.AMBITI})]
    for a in G.AMBITI:
        pv.append((NOMI_AMBITI[a], {b: (2.0 if b == a else 1.0) for b in G.AMBITI}))
    return pv


def punteggi(S: dict, pesi: np.ndarray) -> dict:
    """S: {k: {ambito: pos}}; pesi: matrice (n_punti_di_vista, n_ambiti). Restituisce {k: vettore punteggi}."""
    out = {}
    for k, amb in S.items():
        v = np.array([np.nan if amb[a] is None else amb[a] for a in G.AMBITI])
        ok = ~np.isnan(v)
        w = pesi[:, ok]
        out[k] = (w @ v[ok]) / w.sum(axis=1)
    return out


def posizioni(P: dict) -> dict:
    """Da punteggi a posizione 0-100 (100 = primo) per ogni punto di vista; a pari merito, posto medio."""
    ks = list(P)
    M = np.vstack([P[k] for k in ks])               # unità x punti di vista
    n = len(ks)
    rank = np.zeros_like(M)
    for j in range(M.shape[1]):
        col = M[:, j]
        # posto 1 = punteggio più alto; pari merito -> posto medio
        ordine = (-col).argsort(kind="stable")
        r = np.empty(n)
        r[ordine] = np.arange(1, n + 1)
        for val in np.unique(col):
            idx = np.where(col == val)[0]
            if len(idx) > 1:
                r[idx] = r[idx].mean()
        rank[:, j] = r
    pos = 100 * (n - rank) / (n - 1)
    return {k: (pos[i], rank[i]) for i, k in enumerate(ks)}


def chi_da(rd: np.ndarray, valore: float, nomi: list) -> str:
    """Il punto di vista che dà quel posto; se sono più d'uno, quanti sono."""
    idx = np.where(rd == valore)[0]
    return nomi[idx[0]] if len(idx) == 1 else f"{len(idx)} punti di vista su {len(nomi)}"


def analizza(R: dict) -> tuple[list, list]:
    unita = R["unita"]
    S = {v: G.sintesi_ambiti(R, v) for v in VERSIONI}
    ks = sorted(S["base"])
    dich = punti_dichiarati()
    Wd = np.array([[w[a] for a in G.AMBITI] for _, w in dich])
    rng = np.random.default_rng(SEME)
    Wc = rng.dirichlet(np.ones(len(G.AMBITI)), size=N_CASUALI)

    # punteggi e posizioni, per versione
    pos_d, rk_d, pos_c, sc_d = {}, {}, {}, {}
    for v in VERSIONI:
        Sv = {k: S[v][k] for k in ks}
        Pd = punteggi(Sv, Wd)
        Pc = punteggi(Sv, Wc)
        for k, (p, r) in posizioni(Pd).items():
            pos_d.setdefault(k, []).extend(p)
            rk_d.setdefault(k, []).extend(r)
        for k in ks:
            sc_d.setdefault(k, []).extend(Pd[k])
        for k, (p, _) in posizioni(Pc).items():
            pos_c.setdefault(k, []).extend(p)
    nomi_d = [f"{nome}, {'anni del mandato' if v == 'base' else 'anni spostati di uno'}" for v in VERSIONI for nome, _ in dich]

    n = len(ks)
    righe = []
    for k in ks:
        u = unita[k]
        pc = np.array(pos_c[k])
        rd = np.array(rk_d[k])
        amb_mancanti = [a for a in G.AMBITI if S["base"][k][a] is None]
        righe.append(dict(
            id=u["id"], etichetta=u["etichetta"], anni=G.fmt_anni(u["anni"]),
            n_unita=n,
            pesi_uguali=round(float(sc_d[k][0]), 1),           # media semplice delle posizioni per ambito
            posto_pesi_uguali=float(rd[0]),
            punteggio_equo=round(float(np.median(pc)), 1),
            p10=round(float(np.percentile(pc, 10)), 1), p90=round(float(np.percentile(pc, 90)), 1),
            primo_terzo=round(float((pc >= 200 / 3).mean() * 100), 1),
            ultimo_terzo=round(float((pc < 100 / 3).mean() * 100), 1),
            posto_migliore=float(rd.min()), punto_migliore=chi_da(rd, rd.min(), nomi_d),
            posto_peggiore=float(rd.max()), punto_peggiore=chi_da(rd, rd.max(), nomi_d),
            ambiti_mancanti="; ".join(amb_mancanti),
        ))
    # posto per punteggio equo
    ordine = sorted(righe, key=lambda r: -r["punteggio_equo"])
    for i, r in enumerate(ordine, 1):
        r["posto_equo"] = i
    amb = [dict(id=unita[k]["id"], versione=v, ambito=a,
                posizione="" if S[v][k][a] is None else round(S[v][k][a], 1))
           for v in VERSIONI for k in ks for a in G.AMBITI]
    return righe, amb


def fmt_posto(x: float) -> str:
    return f"{x:g}".replace(".", ",")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    tutte, ambiti = [], []
    for tipo, R in (("governo", G.esegui()), ("legislatura", L.esegui())):
        r, a = analizza(R)
        tutte += [x | {"tipo": tipo} for x in r]
        ambiti += [x | {"tipo": tipo} for x in a]
    campi = ["tipo", "id", "etichetta", "anni", "n_unita", "punteggio_equo", "p10", "p90", "posto_equo",
             "primo_terzo", "ultimo_terzo", "pesi_uguali", "posto_pesi_uguali", "posto_migliore", "punto_migliore",
             "posto_peggiore", "punto_peggiore", "ambiti_mancanti"]
    with open(G.BASE / "punti_di_vista.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, campi, lineterminator="\n")
        w.writeheader()
        w.writerows(tutte)
    with open(G.BASE / "punti_di_vista_ambiti.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, ["tipo", "id", "versione", "ambito", "posizione"], lineterminator="\n")
        w.writeheader()
        w.writerows(ambiti)

    L_ = ["# Punteggio da più punti di vista", "",
          "Generato da `storia/script/punti_di_vista.py`. Metodo nella docstring dello script e in "
          "`storia/governi_metodo.md`.", "",
          f"Punteggio equo = mediana della posizione (0-100, 100 = primo) su {2 * N_CASUALI:,} punti di vista "
          "(tutte le combinazioni di pesi tra gli ambiti, con gli anni del mandato e spostati di uno). "
          "Intervallo = dal 10° al 90° percentile. I posti dei 14 punti di vista dichiarati (pesi uguali, un ambito "
          "che conta il doppio) vanno dal migliore al peggiore indicato.".replace(",", "."), ""]
    for tipo, titolo in (("governo", "Governi"), ("legislatura", "Legislature")):
        rr = sorted((r for r in tutte if r["tipo"] == tipo), key=lambda r: r["posto_equo"])
        L_ += [f"## {titolo}", "",
               "| Posto | " + ("Governo o periodo" if tipo == "governo" else "Legislatura") +
               " | Anni | Punteggio equo | Intervallo | Primo terzo | Ultimo terzo | Pesi uguali (posto) | Posto migliore | Posto peggiore | Ambiti mancanti |",
               "|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in rr:
            L_.append(f"| {r['posto_equo']} | {r['etichetta']} | {r['anni']} | {fmt_posto(r['punteggio_equo'])} | "
                      f"{fmt_posto(r['p10'])}-{fmt_posto(r['p90'])} | {fmt_posto(r['primo_terzo'])}% | "
                      f"{fmt_posto(r['ultimo_terzo'])}% | {fmt_posto(r['posto_pesi_uguali'])}° | "
                      f"{fmt_posto(r['posto_migliore'])}° ({r['punto_migliore']}) | "
                      f"{fmt_posto(r['posto_peggiore'])}° ({r['punto_peggiore']}) | {r['ambiti_mancanti'] or '—'} |")
        L_.append("")
    (G.BASE / "punti_di_vista.md").write_text("\n".join(L_), encoding="utf-8")
    print(f"scritti storia/punti_di_vista.csv, punti_di_vista_ambiti.csv e .md ({len(tutte)} unità)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
