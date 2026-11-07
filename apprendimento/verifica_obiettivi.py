"""Verifica apprendimento/obiettivi.yaml e mostra l'ultimo valore di ogni KPI con serie.

Controlli: campi obbligatori, direzione, codici valori della Carta, id unici;
per ogni `serie`: file esistente, filtro che restituisce una sola serie temporale
(nessun periodo duplicato), ultimo valore confrontato con la base della scheda.

Uso:  python -I apprendimento/verifica_obiettivi.py  [--csv percorso_output]
La funzione `ultimo_valore(obiettivo)` è riusabile dal ciclo di apprendimento.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
SERIE = ROOT / "dati" / "serie"
VALORI = {"RIS", "FID", "INN", "BEN", "APC", "BPA", "FUT", "EQU", "SIC", "CIT"}


def carica() -> list[dict]:
    with open(ROOT / "apprendimento" / "obiettivi.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)["obiettivi"]


def serie_kpi(o: dict) -> pd.DataFrame:
    """Restituisce la serie del KPI come DataFrame [periodo, valore] ordinata."""
    sp = o["serie"]
    df = pd.read_csv(SERIE / f"{sp['file']}.csv")
    for k, v in (sp.get("filtro") or {}).items():
        df = df[df[k].astype(str) == str(v)]
    t, c = sp.get("tempo", "time"), sp.get("colonna", "valore")
    out = pd.DataFrame({"periodo": df[t].astype(str), "valore": df[c].astype(float) * sp.get("scala", 1)})
    return out.sort_values("periodo").reset_index(drop=True)


def ultimo_valore(o: dict) -> tuple[str, float] | None:
    s = serie_kpi(o).dropna()
    return None if s.empty else (s["periodo"].iloc[-1], float(s["valore"].iloc[-1]))


def main() -> int:
    ob = carica()
    errori, righe = [], []
    ids = [o["id"] for o in ob]
    if len(ids) != len(set(ids)):
        errori.append("id duplicati")
    for o in ob:
        for campo in ("id", "proposta", "nome", "unita", "direzione", "base", "obiettivo_3a", "obiettivo_5a", "valori"):
            if campo not in o:
                errori.append(f"{o.get('id')}: manca {campo}")
        if o["direzione"] not in ("su", "giu"):
            errori.append(f"{o['id']}: direzione {o['direzione']}")
        if not set(o["valori"]) <= VALORI:
            errori.append(f"{o['id']}: valori {o['valori']}")
        if ("serie" in o) == (o.get("misurazione") == "manuale"):
            errori.append(f"{o['id']}: serve 'serie' oppure 'misurazione: manuale'")
        if "serie" not in o:
            continue
        s = serie_kpi(o)
        if s.empty:
            errori.append(f"{o['id']}: filtro vuoto su {o['serie']['file']}")
            continue
        if s["periodo"].duplicated().any():
            errori.append(f"{o['id']}: più serie per lo stesso periodo in {o['serie']['file']}")
        per, val = s["periodo"].iloc[-1], s["valore"].iloc[-1]
        b = o["base"]["valore"]
        sb = s[s["periodo"].str[:4] == str(o["base"]["periodo"])[:4]]["valore"]
        val_base = float(sb.iloc[-1]) if len(sb) else None
        scarto = None if (b is None or val_base is None) else round(val_base - b, 3)
        righe.append({"id": o["id"], "file": o["serie"]["file"], "n": len(s), "ultimo_periodo": per, "ultimo_valore": round(val, 3),
                      "base": b, "periodo_base": o["base"]["periodo"], "serie_al_periodo_base": val_base, "scarto": scarto})
    r = pd.DataFrame(righe)
    pd.set_option("display.width", 200)
    print(r.to_string(index=False))
    print(f"\nKPI: {len(ob)}  con serie: {len(r)}  manuali: {sum(o.get('misurazione') == 'manuale' for o in ob)}")
    if "--csv" in sys.argv:
        r.to_csv(sys.argv[sys.argv.index("--csv") + 1], index=False)
    for e in errori:
        print("ERRORE", e)
    return 1 if errori else 0


if __name__ == "__main__":
    sys.exit(main())
