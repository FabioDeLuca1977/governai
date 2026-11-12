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
            "nei ministeri. Per scelta politica restano tutte le sette misure su ricerca, innovazione e logistica verde "
            "(alcune in versione ridotta) e la squadra per la produttività pubblica con l'AI (09-C9) in versione essenziale; "
            "dal 12 novembre 2026 entrano senza nuove tasse le Case della Comunità (06-C3), 500 squadre infermieristiche "
            "di quartiere (06-C8) e la riqualificazione degli amministrativi della sanità (06-C10). Restano accise su tabacco, alcol e bevande zuccherate, il riordino di alcune agevolazioni "
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
UNA_PAGINA = RADICE / "22_programma_in_una_pagina.md"


def una_pagina() -> str | None:
    """Il programma in una pagina (perché, come, cosa misuriamo, chi), interamente generato da programma/schema.yaml,
    dallo scenario scelto e da apprendimento/obiettivi.yaml."""
    import yaml
    f = QUI / "schema.yaml"
    if not f.exists():
        return None
    s = yaml.safe_load(f.read_text(encoding="utf-8"))
    obi = {o["id"]: o for o in yaml.safe_load((RADICE / "apprendimento" / "obiettivi.yaml").read_text(encoding="utf-8"))["obiettivi"]}
    semplici = s.get("indicatori_semplici") or {}
    nomi_val = dict(re.findall(r"^### \d+\. (.+?) \((\w{3})\)", (RADICE / "01_carta_valori.md").read_text(encoding="utf-8"), re.M))
    nomi_val = {v: k for k, v in nomi_val.items()}
    titoli = pd.read_csv(RADICE / "motore" / "proposte.csv").set_index("proposta_id").titolo
    sel = pd.read_csv(QUI / f"selezione_{s['scenario']}.csv")
    v = sel[(sel.tipo == "variante") & (sel.scelta == 1)].set_index("proposta_id")
    c = sel[(sel.tipo == "copertura") & (sel.scelta == 1) & (sel.gettito_min > 0)].sort_values("gettito_min", ascending=False)

    def unita(o, sem):
        u = str(sem.get("unita", o.get("unita") or ""))
        return "" if not u else "%" if u == "%" else "% " + u[1:].strip() if u.startswith("%") else " " + u

    def ind(i):
        o, sem = obi[i], semplici.get(i, {})
        u = unita(o, sem)
        base = (o.get("base") or {}).get("valore")
        t5 = sem.get("obiettivo_5a", o.get("obiettivo_5a"))
        n = lambda x: num(float(x), 2).rstrip("0").rstrip(",") if x is not None else None
        da = f"{n(base)}{u}" if base is not None else "da rilevare"
        a = f"{n(t5)}{u}" if t5 is not None else str((o.get("scheda") or {}).get("obiettivo_5a") or "—")
        fonte = (o.get("base") or {}).get("fonte")
        return f"- **{sem.get('nome', o['nome'])}**: da {da} a **{a}** in 5 anni ({o['proposta']}{'; base: ' + fonte if fonte else ''})"

    P = s["programma"]
    out = ["# Il programma in una pagina", "",
           f"*Generato da `programma/documento.py` da `programma/schema.yaml` e dallo scenario «{s['scenario']}» "
           f"(`programma/selezione_{s['scenario']}.md`). Costi in mld € l'anno a regime, stime GovernAI non certificate.*", "",
           "| Perché | Come | Cosa misuriamo | Chi ne beneficia |", "|---|---|---|---|",
           f"| {P['perche']} | {P['come']} | {P['cosa']} | {P['chi']} |", "",
           f"**I conti:** {num(v.costo_regime.sum())} mld l'anno di spesa nuova, {len(v)} misure su {len(titoli)}, "
           f"coperture per {num(c.gettito_min.sum())} mld al minimo più i fondi vincolati. Nuovo deficit: zero.", "",
           "## Ce l'avremo fatta se…", "", *[ind(i) for i in P.get("indicatori_chiave", []) if i in obi], ""]
    for m in s["missioni"]:
        dentro = [p for p in m["proposte"] if p in v.index]
        costo = v.loc[dentro].costo_regime.sum() if dentro else 0.0
        out += [f"## {m['titolo']}", "", f"*{len(dentro)} misure su {len(m['proposte'])} · {num(costo)} mld l'anno*", "",
                f"**Perché.** {m['perche']} *Valori: {', '.join(nomi_val.get(x, x) for x in m.get('valori', []))}.*", "",
                f"**Come.** {m['come']}", ""]
        for p in sorted(dentro, key=lambda p: -v.loc[p].costo_regime):
            r = v.loc[p]
            dose = "solo regole, costo zero" if r.variante == "ZERO" else f"{r.variante.lower()}, {num(r.costo_regime)} mld"
            out.append(f"- {p} {tit(titoli[p])} ({dose})")
        fuori = [p for p in m["proposte"] if p not in v.index]
        if fuori:
            out.append(f"- *Fuori da questa versione:* " + "; ".join(f"{p} {tit(titoli[p])}" for p in sorted(fuori, key=chiave)))
        out += ["", f"**Sostenibilità.** {m['sostenibilita']}", "", "**Cosa misuriamo.**", "",
                *[ind(i) for i in m.get("indicatori", []) if i in obi], "", "**Chi ne beneficia.**", ""]
        for g in m.get("chi", []):
            out.append(f"- **{g['gruppo']}** ({g.get('quanti', 'da stimare')}): {g['cosa_cambia']}")
        out.append("")
    out += ["## Chi contribuisce", "", "| Copertura | Chi paga o rinuncia | Gettito minimo |", "|---|---|---|"]
    for r in c.itertuples():
        out.append(f"| {r.chiave} {str(r.descrizione).replace('|', '/')} | {str(r.chi_paga).replace('|', '/')} | {num(r.gettito_min)} |")
    return "\n".join(out) + "\n"


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
    pagina = una_pagina()
    if pagina is not None:
        vecchio = UNA_PAGINA.read_text(encoding="utf-8") if UNA_PAGINA.exists() else ""
        da_aggiornare |= pagina != vecchio
        if not a.controlla and pagina != vecchio:
            UNA_PAGINA.write_text(pagina, encoding="utf-8")
        print(f"{UNA_PAGINA.name}: {'da aggiornare' if a.controlla and pagina != vecchio else 'aggiornato' if pagina != vecchio else 'già aggiornato'}")
    return 1 if a.controlla and (da_aggiornare or avvisi) else 0


if __name__ == "__main__":
    raise SystemExit(main())
