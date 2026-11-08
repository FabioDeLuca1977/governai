"""Aggiorna le parti numeriche di 20_programma_governai.md dai risultati del motore e dell'ottimizzatore.

Le parti generate stanno tra i marcatori <!-- auto:NOME --> e <!-- /auto:NOME -->: il testo intorno è scritto
a mano, i numeri no. Così il documento non resta indietro quando cambiano la Carta, il panel o le coperture.

Uso: python programma/documento.py [--controlla]
  --controlla  non scrive: esce con codice 1 se il documento non è aggiornato.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import pandas as pd

QUI = Path(__file__).resolve().parent
RADICE = QUI.parent
DOC = RADICE / "20_programma_governai.md"

AREE = {"01": "Economia, Imprese, Turismo", "02": "Lavoro, Welfare, Famiglia", "03": "Ambiente, Energia, Agricoltura",
        "04": "Infrastrutture e Territori", "05": "Istruzione, Ricerca, Cultura", "06": "Salute",
        "07": "Giustizia, Interno, Difesa", "08": "Esteri, Europa, Istituzioni", "09": "PA e Digitale"}
SCHEDE = {"01": "01_economia", "02": "02_lavoro", "03": "03_ambiente", "04": "04_infrastrutture", "05": "05_istruzione",
          "06": "06_salute", "07": "07_giustizia", "08": "08_esteri", "09": "09_pa_digitale"}
CLASSE = {"robusta": "**Nucleo**", "dipendente dai valori": "Valori", "in coda": "Coda", "sfavorevole": "Sfav."}


ACCENTI = {"a": "à", "e": "è", "i": "ì", "o": "ò", "u": "ù"}


def tit(t: str) -> str:
    """Titoli del CSV scritti in ASCII: «continuita'» diventa «continuità»."""
    return re.sub(r"([aeiou])'(?=[\s,.;:)]|$)", lambda m: ACCENTI[m.group(1)], str(t)).replace("|", "/")


def chiave(pid: str) -> tuple[str, str, int]:
    return pid[:2], pid[3], int(pid[4:])


def num(x: float, d: int = 2) -> str:
    return f"{x:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def selezione(nome: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    s = pd.read_csv(QUI / f"selezione_{nome}.csv")
    return s[(s.tipo == "variante") & (s.scelta == 1)], s[(s.tipo == "copertura") & (s.scelta == 1)]


def variante(v: pd.DataFrame, pid: str) -> str:
    r = v[v.proposta_id == pid]
    if r.empty:
        return "—"
    r = r.iloc[0]
    return f"{r.variante.capitalize()} {num(r.costo_regime)}"


def blocchi() -> dict[str, str]:
    esito = pd.read_csv(RADICE / "motore" / "esito_proposte.csv").set_index("proposta_id")
    prop = pd.read_csv(RADICE / "motore" / "proposte.csv")
    fondi = pd.read_csv(RADICE / "registro" / "fondi.csv").set_index("fondo_id")
    sc = {k: selezione(f) for k, f in [("base", "livello1"), ("completo", "livello2"), ("consiglio", "consiglio"),
                                       ("difesa", "difesa"), ("dividendo", "dividendo")]}
    nucleo = esito[esito.classe == "robusta"].index.tolist()

    def nucleo_coperto(v: pd.DataFrame) -> int:
        return int(v[v.proposta_id.isin(nucleo) & v.variante.isin(["PIENA", "ESSENZIALE"])].proposta_id.nunique())

    vb, cb = sc["base"]
    vc, cc = sc["completo"]
    vg, cg = sc["consiglio"]
    out = {}
    out["totali"] = "\n".join([
        f"- **Programma base: {num(vb.costo_regime.sum())} mld l'anno**, {vb.proposta_id.nunique()} misure su {len(prop)}, "
        f"con {nucleo_coperto(vb)} su {len(nucleo)} del nucleo robusto almeno in versione essenziale. "
        "Usa solo coperture a basso costo sociale.",
        f"- **Programma completo: {num(vc.costo_regime.sum())} mld l'anno**, {vc.proposta_id.nunique()} misure, "
        f"nucleo robusto {nucleo_coperto(vc)} su {len(nucleo)}. Aggiunge coperture strutturali più impegnative.",
        *([f"- **Programma intermedio: {num(selezione('intermedio')[0].costo_regime.sum())} mld l'anno**, "
            f"{selezione('intermedio')[0].proposta_id.nunique()} misure, nucleo robusto "
            f"{nucleo_coperto(selezione('intermedio')[0])} su {len(nucleo)}. Nessun aumento di tasse su casa, eredità, affitti "
            "e IVA, nessun contributo sulle pensioni; più istruzione e servizi sociali, con tagli di spesa e di personale "
            "nei ministeri. Restano accise su tabacco, alcol e bevande zuccherate, il riordino di alcune agevolazioni "
            "fiscali e dei sussidi dannosi, e dal 2030 una rivalutazione ridotta sulla quota più alta delle pensioni "
            "(`programma/selezione_intermedio.md`)."]
          if (QUI / "selezione_intermedio.csv").exists() else []),
        f"- **Programma adottato dal governo ombra** (simulazione, `governo/`): {num(vg.costo_regime.sum())} mld l'anno, "
        f"{vg.proposta_id.nunique()} misure, coperture al minimo per {num(cg.gettito_min.sum())} mld più i fondi vincolati.",
    ])

    righe = ["| # | Misura | Classe | Programma base | Programma completo | Governo ombra |", "|---|---|---|---|---|---|"]
    tot = {"base": 0.0, "completo": 0.0, "consiglio": 0.0}
    for area, nome in AREE.items():
        righe.append(f"| **{nome}** | [schede](programma/schede/{SCHEDE[area]}.md) | | | | |")
        for r in sorted(prop[prop.proposta_id.str.startswith(area)].itertuples(), key=lambda x: chiave(x.proposta_id)):
            e = esito.loc[r.proposta_id]
            cl = CLASSE.get(e.classe, e.classe) + (" · linea rossa in alcune versioni" if bool(e.linea_rossa) else "")
            righe.append(f"| {r.proposta_id} | {tit(r.titolo)} | {cl} | {variante(vb, r.proposta_id)} | "
                         f"{variante(vc, r.proposta_id)} | {variante(vg, r.proposta_id)} |")
    for k in tot:
        tot[k] = sc[k][0].costo_regime.sum()
    righe.append(f"| | **Totale** | | **{num(tot['base'])}** | **{num(tot['completo'])}** | **{num(tot['consiglio'])}** |")
    out["misure"] = "\n".join(righe)

    def per_fondo(c: pd.DataFrame) -> pd.Series:
        return c.groupby("fondo_id").gettito_min.sum()
    fb, fc = per_fondo(cb), per_fondo(cc)
    righe = ["| Fondo | Programma base | Programma completo |", "|---|---|---|"]
    for f in fc.sort_values(ascending=False).index:
        desc = fondi.descrizione.get(f, f) if f in fondi.index else f
        righe.append(f"| {desc} | {num(fb.get(f, 0.0))} | {num(fc.get(f, 0.0))} |")
    righe.append(f"| **Totale coperture nuove (gettito minimo)** | **{num(fb.sum())}** | **{num(fc.sum())}** |")
    out["coperture"] = "\n".join(righe)

    def differenza(v: pd.DataFrame) -> str:
        prima = {r.proposta_id: r.variante for r in vc.itertuples()}
        dopo = {r.proposta_id: r.variante for r in v.itertuples()}
        escono = [p for p in prima if p not in dopo and p != "07-C5"]
        scendono = [p for p in prima if p in dopo and prima[p] != dopo[p]]
        titoli = prop.set_index("proposta_id").titolo
        escono.sort(key=chiave)
        scendono.sort(key=chiave)
        righe = []
        if escono:
            righe.append(f"- **Escono ({len(escono)}):** " + "; ".join(f"{p} {tit(titoli[p])}" for p in escono) + ".")
        if scendono:
            righe.append(f"- **Cambiano variante ({len(scendono)}):** "
                         + "; ".join(f"{p} {prima[p].lower()} → {dopo[p].lower()}" for p in scendono) + ".")
        return "\n".join(righe) or "- Nessuna misura cambia."
    out["difesa"] = differenza(sc["difesa"][0])
    out["dividendo"] = differenza(sc["dividendo"][0])
    return out


FRASI_CLASSE = {"nucleo robusto": "robusta", "dipende dai valori": "dipendente dai valori",
                "dipendente dai valori": "dipendente dai valori", "in coda": "in coda", "sfavorevole": "sfavorevole"}


def controlla_schede() -> list[str]:
    """Righe delle schede (tabelle e titoli) che attribuiscono a una proposta una classe diversa da quella del motore."""
    classe = pd.read_csv(RADICE / "motore" / "esito_proposte.csv").set_index("proposta_id").classe
    avvisi = []
    for f in sorted((QUI / "schede").glob("*.md")):
        for i, riga in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if not riga.startswith(("|", "## ")):
                continue
            ids = [x for x in re.findall(r"\b\d{2}-[PC]\d{1,2}\b", riga) if x in classe.index]
            dette = {v for k, v in FRASI_CLASSE.items() if k in riga.lower()}
            if len(ids) == 1 and dette and classe[ids[0]] not in dette and "carta 1" not in riga.lower():
                avvisi.append(f"schede/{f.name}:{i}: {ids[0]} è «{classe[ids[0]]}» per il motore")
    return avvisi


def applica(testo: str, b: dict[str, str], nome_doc: str, tutti: bool) -> str:
    """Sostituisce i blocchi generati. Il programma deve averli tutti; gli altri documenti solo quelli che usano."""
    for nome, corpo in b.items():
        testo, n = re.subn(rf"(<!-- auto:{nome} -->\r?\n)(?:.*?\r?\n)?(<!-- /auto:{nome} -->)",
                           lambda m: m.group(1) + corpo + "\n" + m.group(2), testo, flags=re.S)
        if n > 1 or (tutti and n != 1):
            raise SystemExit(f"marcatore auto:{nome} mancante o doppio in {nome_doc}")
    return testo


# Documenti con parti generate: il programma completo e la sintesi delle idee
DOCUMENTI = [(DOC, True), (RADICE / "21_idee_in_sintesi.md", False)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--controlla", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    b = blocchi()
    avvisi = controlla_schede()
    for x in avvisi:
        print("AVVISO classe superata:", x)
    da_aggiornare = False
    for doc, tutti in DOCUMENTI:
        if not doc.exists():
            continue
        vecchio = doc.read_text(encoding="utf-8")
        nuovo = applica(vecchio, b, doc.name, tutti)
        da_aggiornare |= nuovo != vecchio
        if not a.controlla and nuovo != vecchio:
            doc.write_text(nuovo, encoding="utf-8")
        print(f"{doc.name}: {'da aggiornare' if a.controlla and nuovo != vecchio else 'aggiornato' if nuovo != vecchio else 'già aggiornato'}")
    return 1 if a.controlla and (da_aggiornare or avvisi) else 0


if __name__ == "__main__":
    raise SystemExit(main())
