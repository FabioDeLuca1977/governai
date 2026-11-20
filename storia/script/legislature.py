"""Confronto tra legislature della Repubblica (1979-2025), con lo stesso metodo di governi.py.

Uso:  python storia/script/legislature.py   (dopo governi.py, se cambiano serie o governi)

Legge:   storia/governi.csv, storia/serie/*.csv
Scrive:  storia/legislature_confronto.csv, storia/legislature_confronto.md

Metodo: identico al confronto tra governi (storia/governi_metodo.md), cambia solo l'unità.
- Una legislatura comprende i governi che il file storia/governi.csv le attribuisce, compresi quelli rimasti
  in carica per gli affari correnti dopo le elezioni.
- Ogni anno solare va alla legislatura con più giorni di governo in quell'anno.
- Per ogni indicatore: valore italiano, media di Francia, Germania e Spagna, differenza; il posto si calcola
  sulla differenza (sul solo dato italiano per povertà ed emigrazione).
- La VII legislatura è iniziata prima del 1979: ne entrerebbe solo la parte finale, quindi resta fuori.
"""
from __future__ import annotations

import csv
import statistics
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import governi as G  # noqa: E402

ROMANI = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV",
          "XVI", "XVII", "XVIII", "XIX", "XX"]


def costruisci_legislature(gov: list[dict]) -> list[dict]:
    per = defaultdict(list)
    for g in gov:
        per[g["legislatura"]].append(g)
    out = []
    for leg in sorted(per, key=ROMANI.index):
        gs = per[leg]
        u = dict(governi=gs, inizio=gs[0]["inizio"], termine=gs[-1]["termine"], in_carica=gs[-1]["in_carica"])
        u["id"] = "L" + leg
        u["numeri"] = ", ".join(x["numero"].replace("governo ", "") for x in gs)
        fine = "oggi" if u["in_carica"] else str(u["termine"].year)
        u["etichetta"] = f"{leg} legislatura ({u['inizio'].year}-{fine})"
        u["n_governi"] = len(gs)
        out.append(u)
    return out


def assegna_anni(unita: list[dict]) -> None:
    for u in unita:
        u["anni"] = []
    for anno in range(G.PRIMO_ANNO, G.ULTIMO_ANNO + 1):
        giorni = [(sum(G.giorni_nell_anno(g["inizio"], g["termine"], anno) for g in u["governi"]), k)
                  for k, u in enumerate(unita)]
        unita[max(giorni)[1]]["anni"].append(anno)
    for u in unita:
        # una legislatura iniziata prima del 1979 entrerebbe solo con la sua parte finale: resta fuori
        u["confrontabile"] = bool(u["anni"]) and u["inizio"].year >= G.PRIMO_ANNO


def esegui() -> dict:
    gov = G.leggi_governi()
    unita = costruisci_legislature(gov)
    assegna_anni(unita)
    serie = {ind["file"]: G.leggi_serie(ind["file"]) for ind in G.INDICATORI}
    ris = defaultdict(dict)
    for versione, sposta in (("base", 0), ("ritardo_1_anno", 1)):
        for ind in G.INDICATORI:
            for k, u in enumerate(unita):
                anni = [a + sposta for a in u["anni"] if a + sposta <= G.ULTIMO_ANNO]
                ris[(versione, ind["id"])][k] = G.calcola(ind, serie[ind["file"]], anni) | {"anni": anni}
            conf = {k: r for k, r in ris[(versione, ind["id"])].items() if unita[k]["confrontabile"]}
            base = "diff" if ind["vicini"] else "it"
            rk = G.ranghi({k: r[base] for k, r in conf.items()}, ind["verso"])
            for k, r in ris[(versione, ind["id"])].items():
                r["rango"], r["n"] = rk.get(k), len(rk)
    return dict(unita=unita, risultati=ris)


def scrivi_csv(R: dict) -> None:
    campi = ["unita_id", "governo_periodo", "governi_inclusi", "tipo_unita", "confrontabile", "versione",
             "anni", "ambito", "indicatore", "unita_misura", "verso", "anni_effettivi",
             "valore_italia", "valore_vicini", "differenza", "rango", "n_confrontati", "base_del_rango", "nota"]
    verso_txt = {1: "più alto è meglio", -1: "più basso è meglio", 0: "descrittivo (rango 1 = calo maggiore)"}
    with open(G.BASE / "legislature_confronto.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(campi)
        for versione in ("base", "ritardo_1_anno"):
            for k, u in enumerate(R["unita"]):
                for ind in G.INDICATORI:
                    r = R["risultati"][(versione, ind["id"])][k]
                    nota = r["nota"] if u["confrontabile"] else "legislatura iniziata prima del 1979: nel confronto entrerebbe solo la parte finale"
                    w.writerow([u["id"], u["etichetta"], u["numeri"], "legislatura", "sì" if u["confrontabile"] else "no",
                                versione, G.fmt_anni(r["anni"]), ind["ambito"], ind["nome"], ind["unita"],
                                verso_txt[ind["verso"]], r["anni_eff"],
                                G.num(r["it"], 3), G.num(r["vic"], 3), G.num(r["diff"], 3),
                                r["rango"] or "", r["n"] if r["rango"] else "",
                                ("Italia meno vicini" if ind["vicini"] else "solo Italia (nessun confronto omogeneo)") if r["rango"] else "",
                                nota])


def posizione(r: dict) -> float | None:
    if r["rango"] is None or not r["n"]:
        return None
    return 100.0 if r["n"] == 1 else (r["n"] - r["rango"]) / (r["n"] - 1) * 100


def scrivi_rapporto(R: dict) -> None:
    U = [(k, u) for k, u in enumerate(R["unita"]) if u["confrontabile"]]
    L = ["# Legislature a confronto (1979-2025)", "",
         "*Generato da `storia/script/legislature.py`. Stesso metodo del confronto tra governi "
         "(`storia/governi_metodo.md`): conta quanto l'Italia ha fatto meglio o peggio della media di Francia, "
         "Germania e Spagna negli stessi anni. Nessun nome di persona o di partito.*", "",
         "## Posizione per ambito", "",
         "Mediana delle posizioni degli indicatori dell'ambito, da 0 (ultima) a 100 (prima), tra "
         f"{len(U)} legislature. La pressione fiscale è esclusa: salire o scendere non è in sé meglio o peggio.", ""]
    for versione, titolo in (("base", "Anni della legislatura"), ("ritardo_1_anno", "Anni spostati di uno (effetti in ritardo)")):
        L += [f"### {titolo}", "", "| Legislatura | Governi | Anni | " + " | ".join(a.capitalize() for a in G.AMBITI) + " |",
              "|---|---|---|" + "---|" * len(G.AMBITI)]
        for k, u in U:
            celle = []
            for a in G.AMBITI:
                p = [posizione(R["risultati"][(versione, i["id"])][k]) for i in G.INDICATORI if i["ambito"] == a and i["verso"] != 0]
                p = [x for x in p if x is not None]
                celle.append(str(round(statistics.median(p))) if p else "—")
            anni = R["risultati"][(versione, G.INDICATORI[0]["id"])][k]["anni"]
            L.append(f"| {u['etichetta']} | {u['n_governi']} | {G.fmt_anni(anni)} | " + " | ".join(celle) + " |")
        L.append("")
    L += ["## Indicatore per indicatore (anni della legislatura)", "",
          "Posto calcolato sulla differenza con i vicini; per povertà ed emigrazione sul solo dato italiano.", ""]
    for ind in G.INDICATORI:
        L += [f"### {ind['nome']} ({ind['unita']})", "", "| Legislatura | Anni | Italia | Vicini | Differenza | Posto |", "|---|---|---|---|---|---|"]
        for k, u in U:
            r = R["risultati"][("base", ind["id"])][k]
            posto = f"{r['rango']}° su {r['n']}" if r["rango"] else "—"
            L.append(f"| {u['etichetta']} | {r['anni_eff']} | {G.it(r['it'])} | {G.it(r['vic'])} | {G.it(r['diff'], segno=True)} | {posto} |")
        L.append("")
    L += ["## Limiti", "",
          "- Una legislatura somma governi anche molto diversi tra loro: il dato dice com'è andato il Paese in quegli anni, "
          "non giudica un singolo governo.",
          "- I governi rimasti in carica dopo le elezioni contano nella legislatura precedente, come nel file dei governi.",
          "- La XIX legislatura è in corso: contano gli anni 2023-2025, con il 2025 ancora provvisorio.",
          "- Con 12 legislature i posti sono pochi: una differenza di un posto conta poco.",
          "- Il confronto con i vicini toglie gli shock comuni, non quelli che colpiscono l'Italia più degli altri. "
          "Nessun numero qui dimostra una causa.", ""]
    (G.BASE / "legislature_confronto.md").write_text("\n".join(L), encoding="utf-8")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    R = esegui()
    scrivi_csv(R)
    scrivi_rapporto(R)
    n = sum(u["confrontabile"] for u in R["unita"])
    print(f"legislature confrontabili: {n}; scritti storia/legislature_confronto.csv e .md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
