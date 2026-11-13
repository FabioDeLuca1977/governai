"""Ottimizzatore del programma GovernAI: sceglie varianti e coperture con più valore,
interamente finanziate nello scenario prudente.

Modello (programmazione lineare intera, scipy.optimize.milp):
  variabili  x_j ∈ {0,1}  per ogni variante j di ogni proposta (al più una per proposta;
                          nessuna variante = status quo)
             y_m ∈ {0,1}  per ogni misura di copertura m del menu
  obiettivo  max Σ u_j x_j + Σ c_m y_m
             u_j = utilità della proposta (panel, SMAA) × intensità della variante
             c_m = effetto della misura di copertura sui valori (di solito negativo per chi paga)
  vincoli    - risorse generali (SAD, SPESE_FISCALI, ACCISE_SALUTE, RIORDINO_BONUS, RIALLOCAZIONE)
               sono fungibili nel bilancio: un solo vincolo, spesa ≤ gettito minimo delle misure attivate;
             - fondi vincolati (coesione, FSN, ETS2/FSC, fondi UE, tassa di soggiorno, pensioni)
               hanno ciascuno il proprio vincolo: spesa ≤ capienza minima + gettito delle misure del fondo;
             - fondi non ammessi per spesa permanente (DEFICIT, RISPARMI_ATTESI, IVA_EVASIONE, ETS, ALTRO): capienza 0;
             - TARIFFE (fuori bilancio): nessun vincolo di finanza pubblica.
La soluzione si ripete per molte combinazioni di pesi tra i valori (stesse estrazioni del motore)
per misurare quanto ogni scelta è robusta.

Uso:  python ottimizza.py [--n 400] [--forza 03-P1:ESSENZIALE ...] [--escludi 07-C5] [--etichetta scenario]
Scrive selezione[_etichetta].md e selezione[_etichetta].csv.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import Bounds, LinearConstraint, milp

QUI = Path(__file__).resolve().parent
RADICE = QUI.parent
sys.path.insert(0, str(RADICE / "motore"))
import decidi  # noqa: E402  (stesso panel, stesse estrazioni SMAA)

VALORI = decidi.VALORI
GENERALI = {"SAD", "SPESE_FISCALI", "ACCISE_SALUTE", "RIORDINO_BONUS", "RIALLOCAZIONE"}
NON_AMMESSI = {"DEFICIT", "RISPARMI_ATTESI", "IVA_EVASIONE", "ETS", "ALTRO"}
FUORI_BILANCIO = {"TARIFFE"}
PREMIO_NUCLEO = 10.0  # maggiore di qualunque somma di utilità (≤ 3 per proposta): rende la priorità lessicografica
PREMIO_MOMENTO = 1.0  # priorità segnalate dalle regole di allerta: contano, ma non scavalcano il nucleo


def carica_varianti() -> pd.DataFrame:
    file = sorted((QUI / "varianti").glob("*.csv"))
    if not file:
        sys.exit("Nessun file in programma/varianti/.")
    v = pd.concat([pd.read_csv(f).assign(file=f.name) for f in file], ignore_index=True)
    v["variante"] = v.variante.str.upper().str.strip()
    v["fondo_id"] = v.fondo_id.str.upper().str.strip()
    for c in ["intensita", "costo_regime", "prelievo_regime", "costo_2027", "costo_2028", "costo_2029"]:
        v[c] = pd.to_numeric(v.get(c), errors="coerce").fillna(0.0)
    v["chiave"] = v.proposta_id + ":" + v.variante
    return v


def carica_menu(livello_max: int | None = None, solo: list[str] | None = None,
                senza: list[str] | None = None) -> pd.DataFrame:
    m = pd.read_csv(QUI / "coperture_menu.csv")
    if senza:
        m = m[~m.misura_id.isin(senza)].reset_index(drop=True)
    if livello_max is not None and "livello" in m:
        m = m[pd.to_numeric(m.livello, errors="coerce").fillna(1) <= livello_max].reset_index(drop=True)
    if solo:
        m = m[m.misura_id.str.startswith(tuple(solo))].reset_index(drop=True)
    m["fondo_id"] = m.fondo_id.str.upper().str.strip()
    for c in ["gettito_min", "gettito_max", *VALORI]:
        m[c] = pd.to_numeric(m[c], errors="coerce").fillna(0.0)
    return m


def capienze_base(menu: pd.DataFrame) -> dict[str, float]:
    f = pd.read_csv(RADICE / "registro" / "fondi.csv")
    cap = {}
    for r in f.itertuples(index=False):
        fid = r.fondo_id.upper()
        if fid in NON_AMMESSI or fid in GENERALI:
            cap[fid] = 0.0  # i generali si finanziano solo con le misure del menu
        elif fid in set(menu.fondo_id):
            cap[fid] = 0.0  # anche un fondo vincolato coperto dal menu usa solo le misure (no doppio conteggio)
        else:
            c = pd.to_numeric(r.capienza_min, errors="coerce")
            cap[fid] = 0.0 if pd.isna(c) or str(r.certificazione).lower() == "si" else max(float(c), 0.0)
    return cap


def costruisci(var: pd.DataFrame, menu: pd.DataFrame, cap: dict[str, float]):
    """Matrici del problema; restituisce elenco varianti, vincoli e indici."""
    chiavi = var.drop_duplicates("chiave")[["chiave", "proposta_id", "variante", "intensita",
                                            "costo_regime", "descrizione"]].reset_index(drop=True)
    J, M = len(chiavi), len(menu)
    jidx = {k: i for i, k in enumerate(chiavi.chiave)}
    righe_A, lb, ub, nomi = [], [], [], []

    # al più una variante per proposta
    for pid, g in chiavi.groupby("proposta_id"):
        a = np.zeros(J + M)
        a[g.index] = 1
        righe_A.append(a); lb.append(0); ub.append(1); nomi.append(f"una variante {pid}")

    # risorse generali (fungibili)
    a = np.zeros(J + M)
    for r in var[var.fondo_id.isin(GENERALI)].itertuples():
        a[jidx[r.chiave]] += r.prelievo_regime
    for i, r in enumerate(menu.itertuples()):
        if r.fondo_id in GENERALI:
            a[J + i] -= r.gettito_min
    righe_A.append(a); lb.append(-np.inf); ub.append(0.0); nomi.append("risorse generali")

    # fondi vincolati e non ammessi
    for fid in sorted(set(var.fondo_id) - GENERALI - FUORI_BILANCIO):
        a = np.zeros(J + M)
        for r in var[var.fondo_id == fid].itertuples():
            a[jidx[r.chiave]] += r.prelievo_regime
        for i, r in enumerate(menu.itertuples()):
            if r.fondo_id == fid:
                a[J + i] -= r.gettito_min
        righe_A.append(a); lb.append(-np.inf); ub.append(cap.get(fid, 0.0)); nomi.append(f"fondo {fid}")
    return chiavi, np.array(righe_A), np.array(lb), np.array(ub), nomi


RE_COMPENSAZIONE = re.compile(r"compens|salvaguard|ISEE|esclus|esent|franchigia", re.I)


def linee_rosse(chiavi: pd.DataFrame, menu: pd.DataFrame) -> list[tuple[str, str, int]]:
    """Esclusioni automatiche: (motivo, chiave, indice nella matrice del problema)."""
    out = []
    # 1. proposta segnalata come linea rossa dalla maggioranza del panel indipendente
    file = sorted((RADICE / "motore").glob("punteggi_?.csv"))
    panel = pd.concat([pd.read_csv(f).assign(valutatore=f.stem[-1]) for f in file])
    voti = panel[panel.linea_rossa.astype(str).str.lower() == "si"].groupby("proposta_id").valutatore.nunique()
    maggioranza = {p for p, v in voti.items() if v > len(file) / 2}
    for i, r in chiavi.iterrows():
        if r.proposta_id in maggioranza and r.costo_regime > 0:
            out.append(("linea rossa segnalata dalla maggioranza del panel", r.chiave, int(i)))
    # 2. incompatibilità giuridica (Costituzione o diritto UE) secondo gli esperti di giuridico/
    conf_f = RADICE / "giuridico" / "conformita.csv"
    if conf_f.exists():
        conf = pd.read_csv(conf_f, dtype=str).fillna("")
        inc = conf[conf.esito == "incompatibile"]
        for r in inc.itertuples():
            motivo = f"incompatibile ({r.ambito}): {r.norme[:80]}"
            if r.tipo == "proposta":
                for i in chiavi.index[chiavi.proposta_id == r.id]:
                    out.append((motivo, chiavi.chiave[i], int(i)))
            elif r.tipo == "variante":
                for i in chiavi.index[chiavi.chiave == r.id]:
                    out.append((motivo, chiavi.chiave[i], int(i)))
            elif r.tipo == "copertura":
                for j in menu.index[menu.misura_id == r.id]:
                    out.append((motivo, r.id, len(chiavi) + int(j)))
    # 3. copertura che sposta costi rilevanti su chi ha meno mezzi senza compensazione (Carta, Equità)
    J = len(chiavi)
    if "EQU" in menu.columns:
        for j, r in menu.iterrows():
            if r.EQU <= -2 and not RE_COMPENSAZIONE.search(str(r.descrizione)):
                out.append(("copertura regressiva senza compensazione (Equità ≤ −2)", r.misura_id, J + int(j)))
    return out


def risolvi(obj: np.ndarray, A, lb, ub, fissa: dict[int, int]) -> np.ndarray | None:
    n = len(obj)
    lo, hi = np.zeros(n), np.ones(n)
    for i, v in fissa.items():
        lo[i] = hi[i] = v
    r = milp(c=-obj, constraints=LinearConstraint(A, lb, ub), integrality=np.ones(n),
             bounds=Bounds(lo, hi), options={"time_limit": 30})
    return None if r.x is None else np.round(r.x).astype(int)


def num(v: float, dec: int = 2) -> str:
    return f"{v:,.{dec}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=400, help="combinazioni di pesi per la robustezza")
    ap.add_argument("--forza", nargs="*", default=[], help="varianti obbligatorie, es. 03-P1:ESSENZIALE")
    ap.add_argument("--escludi", nargs="*", default=[], help="proposte escluse, es. 07-C5")
    ap.add_argument("--priorita", nargs="*", default=[], help="proposte da privilegiare in questo momento")
    ap.add_argument("--livello", type=int, default=None, help="usa solo le coperture fino a questo livello (1 o 2)")
    ap.add_argument("--senza-nucleo-prima", dest="nucleo_prima", action="store_false",
                    help="disattiva la priorità al nucleo robusto (regola 7 della Carta)")
    ap.add_argument("--riserva", type=float, default=0.0,
                    help="mld/anno di coperture generali riservati alla riduzione del deficit (non spendibili)")
    ap.add_argument("--solo-coperture", dest="solo", nargs="*", default=[],
                    help="usa solo le coperture con questi prefissi, es. RA RB (scenario senza nuove tasse)")
    ap.add_argument("--escludi-coperture", dest="senza", nargs="*", default=[],
                    help="coperture escluse per scelta di scenario, es. RA11")
    ap.add_argument("--etichetta", default="")
    ap.add_argument("--seed", type=int, default=7)
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)

    var, menu = carica_varianti(), carica_menu(a.livello, a.solo, a.senza)
    cap = capienze_base(menu)
    chiavi, A, lb, ub, nomi = costruisci(var, menu, cap)
    # Riserva per il risanamento: un programma in pareggio non riduce il debito. Con --riserva una parte delle
    # coperture generali resta a riduzione del deficit: spesa sulle risorse generali <= gettito - riserva.
    ub[nomi.index("risorse generali")] = -max(a.riserva, 0.0)
    J, M = len(chiavi), len(menu)

    # Utilità delle proposte dal panel (SMAA), riallineate alle varianti
    S, _, _, ids = decidi.carica_panel()
    sim = decidi.simula(S, max(a.n, 2000), rng, fattori=decidi.calibrazione(ids))
    U, W = sim["U"], sim["W"]
    pos = {p: i for i, p in enumerate(ids)}
    mancanti = sorted(set(chiavi.proposta_id) - set(pos))
    if mancanti:
        print(f"attenzione: proposte senza punteggio del panel (utilità 0): {mancanti}")
    col = np.array([pos.get(p, -1) for p in chiavi.proposta_id])
    inten = chiavi.intensita.to_numpy()
    Mv = menu[VALORI].to_numpy()

    # Carta, regola 7: il nucleo robusto viene prima. Le varianti PIENA/ESSENZIALE delle proposte robuste
    # ricevono un premio lessicografico: si finanzia il massimo del nucleo, poi si ottimizza il resto.
    esito = pd.read_csv(RADICE / "motore" / "esito_proposte.csv")
    nucleo = set(esito.proposta_id[esito.classe == "robusta"]) if a.nucleo_prima else set()
    premio = np.where(chiavi.proposta_id.isin(nucleo) & chiavi.variante.isin(["PIENA", "ESSENZIALE"]), PREMIO_NUCLEO, 0.0)
    # Priorità del momento (regole di allerta del sistema dinamico): premio minore di quello del nucleo
    premio += np.where(chiavi.proposta_id.isin(a.priorita) & chiavi.variante.isin(["PIENA", "ESSENZIALE"]),
                       PREMIO_MOMENTO * chiavi.intensita, 0.0)

    def obiettivo(u_prop: np.ndarray, w: np.ndarray) -> np.ndarray:
        u = np.where(col >= 0, u_prop[np.maximum(col, 0)], 0.0) * inten + premio
        return np.concatenate([u, Mv @ w])

    fissa = {}
    for f in a.forza:
        if f in set(chiavi.chiave):
            fissa[int(chiavi.index[chiavi.chiave == f][0])] = 1
        else:
            sys.exit(f"--forza {f}: variante inesistente")
    for p in a.escludi:
        for i in chiavi.index[chiavi.proposta_id == p]:
            fissa[int(i)] = 0

    # Linee rosse automatiche (Carta: i vincoli vengono prima dei valori). Regole deterministiche,
    # non aggirabili da un prompt; si possono superare solo con --forza, che resta scritto nel risultato.
    escluse_lr = linee_rosse(chiavi, menu)
    forzate = {k.split(":")[0] for k in a.forza}
    for motivo, chiave, idx in escluse_lr:
        if chiave.split(":")[0] not in forzate:
            fissa[idx] = 0

    # Soluzione centrale: utilità attesa (media su pesi e valutatori)
    centrale = risolvi(obiettivo(U.mean(0), W.mean(0)), A, lb, ub, fissa)
    if centrale is None:
        sys.exit("Nessuna soluzione ammissibile: le varianti forzate non sono finanziabili.")
    # Robustezza
    freq = np.zeros(J + M)
    campioni = rng.choice(len(U), size=a.n, replace=False)
    for k in campioni:
        x = risolvi(obiettivo(U[k], W[k]), A, lb, ub, fissa)
        if x is not None:
            freq += x
    freq /= a.n

    # --- Risultati
    sel = chiavi.assign(scelta=centrale[:J], robustezza=freq[:J])
    msel = menu.assign(scelta=centrale[J:], robustezza=freq[J:])
    usate = sel[sel.scelta == 1]
    attive = msel[msel.scelta == 1]
    spesa = usate.costo_regime.sum()
    lav = var[var.chiave.isin(usate.chiave)]
    per_fondo = lav.groupby("fondo_id").prelievo_regime.sum()
    gettito = attive.groupby("fondo_id").gettito_min.sum()
    tag = f"_{a.etichetta}" if a.etichetta else ""
    pd.concat([sel.assign(tipo="variante"), msel.rename(columns={"misura_id": "chiave"}).assign(tipo="copertura")],
              ignore_index=True).to_csv(QUI / f"selezione{tag}.csv", index=False)

    titoli = pd.read_csv(RADICE / "motore" / "proposte.csv").set_index("proposta_id").titolo
    out = [f"# GovernAI — Programma selezionato{(' — scenario ' + a.etichetta) if a.etichetta else ''}", "",
           "*Generato da `programma/ottimizza.py`. Tutto finanziato nello scenario prudente: niente deficit, "
           "niente risparmi non certificati, gettito minimo delle coperture.*", ""]
    if a.forza or a.escludi or a.livello or a.priorita or a.solo or a.senza:
        out += [f"Vincoli di scenario: forzate {a.forza or '—'}, escluse {a.escludi or '—'}, "
                f"prioritarie per il momento {a.priorita or '—'}, "
                f"coperture fino al livello {a.livello or 'tutti'}"
                + (f", solo coperture {' '.join(a.solo)}" if a.solo else "")
                + (f", coperture escluse {' '.join(a.senza)}" if a.senza else "") + ".", ""]
    out += [f"Priorità al nucleo robusto (Carta, regola 7): **{'attiva' if a.nucleo_prima else 'disattivata'}**.", ""]
    if escluse_lr:
        out += ["**Escluse dalle linee rosse automatiche** (regole deterministiche, superabili solo con una scelta esplicita):", ""]
        for motivo, chiave, idx in escluse_lr:
            superata = " — *superata con --forza*" if chiave.split(":")[0] in forzate else ""
            out.append(f"- {chiave}: {motivo}{superata}")
        out.append("")
    gen_spesa = lav[lav.fondo_id.isin(GENERALI)].prelievo_regime.sum()
    gen_gettito = attive[attive.fondo_id.isin(GENERALI)].gettito_min.sum()
    out += ["## Saldo", "",
            "| Voce | mld €/anno a regime |", "|---|---|",
            f"| Spesa delle misure scelte | {num(spesa)} |",
            f"| di cui su risorse generali | {num(gen_spesa)} |",
            f"| Gettito minimo delle coperture attivate (risorse generali) | {num(gen_gettito)} |",
            *([f"| di cui tenuto da parte e non speso (riserva: per lo scenario intermedio, smettere di fumare e dopo il 2029) | {num(a.riserva)} |"] if a.riserva > 0 else []),
            f"| Gettito minimo delle coperture attivate (totale) | {num(attive.gettito_min.sum())} |",
            f"| Proposte nel programma | {usate.proposta_id.nunique()} su {chiavi.proposta_id.nunique()} |", "",
            "La colonna **Robustezza** indica in quale quota delle combinazioni di pesi tra i valori la stessa scelta "
            "rientra nel programma ottimo. Sopra l'80% la scelta non dipende dalla sensibilità politica.", ""]

    out += ["## Misure del programma", "",
            "| Proposta | Titolo | Variante | Intensità | Costo | Robustezza |", "|---|---|---|---|---|---|"]
    for r in usate.sort_values(["robustezza", "costo_regime"], ascending=[False, False]).itertuples():
        out.append(f"| {r.proposta_id} | {titoli.get(r.proposta_id, '')} | {r.variante} | {num(r.intensita, 1)} | "
                   f"{num(r.costo_regime)} | {r.robustezza * 100:.0f}% |")
    out += ["", "## Coperture attivate", "",
            "| Misura | Descrizione | Fondo | Gettito min | Chi paga | Robustezza |", "|---|---|---|---|---|---|"]
    for r in attive.sort_values("gettito_min", ascending=False).itertuples():
        out.append(f"| {r.misura_id} | {r.descrizione} | {r.fondo_id} | {num(r.gettito_min)} | {r.chi_paga} | {r.robustezza * 100:.0f}% |")

    escluse = sorted(set(chiavi.proposta_id) - set(usate.proposta_id))
    out += ["", "## Proposte non incluse", "",
            "Restano fuori perché, con le risorse disponibili, altre misure danno più valore per euro, oppure "
            "perché il loro effetto netto sui valori è negativo. *Rientrano se si trovano coperture aggiuntive.*", ""]
    for p in escluse:
        f = sel[sel.proposta_id == p].robustezza.sum()
        out.append(f"- {p} {titoli.get(p, '')} (scelta in {f * 100:.0f}% delle combinazioni di pesi)")
    out += ["", "## Uso dei fondi", "", "| Fondo | Spesa | Gettito/capienza disponibile |", "|---|---|---|"]
    for fid in sorted(set(per_fondo.index) | set(gettito.index)):
        disp = gettito.get(fid, 0) + (0 if fid in GENERALI else cap.get(fid, 0))
        out.append(f"| {fid} | {num(per_fondo.get(fid, 0))} | {'—' if fid in FUORI_BILANCIO else num(disp)} |")
    out += ["", f"Risorse generali (fungibili): spesa {num(gen_spesa)} ≤ gettito {num(gen_gettito)}.", ""]
    (QUI / f"selezione{tag}.md").write_text("\n".join(out), encoding="utf-8")

    print(f"spesa {spesa:.2f}  coperture {attive.gettito_min.sum():.2f}  proposte {usate.proposta_id.nunique()}/{chiavi.proposta_id.nunique()}"
          f"  -> selezione{tag}.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
