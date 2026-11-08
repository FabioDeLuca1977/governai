"""Ricerca nell'archivio della Gazzetta Ufficiale costruito da `scarica_gu.py`.

Uso da riga di comando:
  python cerca.py "caregiver familiare"                     # parole chiave (tutte) in titolo e testo
  python cerca.py "spese fiscali" --tipo legge "decreto legislativo" --dal 2026-10-01 --al 2026-11-08
  python cerca.py --solo-titolo "IVA"                       # solo intestazione e titolo
  python cerca.py --cita "legge 31 dicembre 2009, n. 196"   # atti che citano una norma
  python cerca.py --cita "d.lgs. 82/2005" --articolo 68     # ... e in particolare un suo articolo
  python cerca.py --atto "decreto-legge 6 novembre 2026, n. 200"   # l'atto è in archivio?

Uso da Python (per gli agenti):
  from cerca import cerca, citanti, trova_atto
  cerca("salario minimo", tipi=["legge"], dal="2026-01-01")
  citanti("legge 23 agosto 1988, n. 400", articolo="17")
"""
from __future__ import annotations

import argparse
import re
import sys
from functools import lru_cache

import pandas as pd

sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))  # anche con python -I
from norme import ARCHIVIO, INDICE, Riferimento, trova_riferimenti

# tipo del riferimento (norme.TIPI) -> tipo nell'indice (scarica_gu.classifica)
TIPO_INDICE = {"legge": "legge", "decreto-legge": "decreto-legge", "decreto legislativo": "decreto legislativo",
               "decreto del Presidente della Repubblica": "DPR", "legge costituzionale": "legge costituzionale",
               "decreto del Presidente del Consiglio dei ministri": "DPCM"}


def carica_indice() -> pd.DataFrame:
    if not INDICE.exists():
        raise SystemExit("Archivio vuoto: eseguire prima `python scarica_gu.py`.")
    return pd.read_csv(INDICE, dtype=str, keep_default_na=False)


@lru_cache(maxsize=4096)
def testo_atto(percorso: str) -> str:
    if not percorso:
        return ""
    f = ARCHIVIO / percorso
    return f.read_text(encoding="utf-8") if f.exists() else ""


def _norm(s: str) -> str:
    # la GU scrive le vocali accentate con l'apostrofo ("attivita'"): uniformiamo per la ricerca
    s = s.lower()
    for a, b in (("à", "a'"), ("è", "e'"), ("é", "e'"), ("ì", "i'"), ("ò", "o'"), ("ù", "u'")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s)


def _estratto(testo: str, parola: str, larghezza: int = 110) -> str:
    t = re.sub(r"\s+", " ", testo)
    i = _norm(t).find(_norm(parola))
    if i < 0:
        return ""
    return ("…" if i > larghezza else "") + t[max(0, i - larghezza): i + len(parola) + larghezza] + "…"


def cerca(parole: str = "", tipi: list[str] | None = None, dal: str | None = None, al: str | None = None,
          solo_titolo: bool = False, limite: int = 50) -> pd.DataFrame:
    """Atti che contengono TUTTE le parole (o le frasi tra virgolette) in intestazione, titolo o testo."""
    d = carica_indice()
    if tipi:
        d = d[d.tipo.str.lower().isin([t.lower() for t in tipi])]
    if dal:
        d = d[d.data_gu >= dal]
    if al:
        d = d[d.data_gu <= al]
    termini = [a or b for a, b in re.findall(r'"([^"]+)"|(\S+)', parole)]
    if not termini:
        return d.head(limite)
    righe = []
    for r in d.itertuples():
        base = _norm(f"{r.intestazione} {r.titolo} {r.emettitore}")
        corpo = "" if solo_titolo else _norm(testo_atto(r.testo))
        if all(_norm(t) in base or _norm(t) in corpo for t in termini):
            dove = "titolo" if all(_norm(t) in base for t in termini) else "testo"
            righe.append({**r._asdict(), "trovato_in": dove,
                          "estratto": "" if dove == "titolo" else _estratto(testo_atto(r.testo), termini[0])})
    out = pd.DataFrame(righe)
    if out.empty:
        return out
    out["_p"] = (out.trovato_in == "titolo").astype(int)
    return out.sort_values(["_p", "data_gu"], ascending=False).drop(columns=["_p", "Index"]).head(limite)


def _rif(norma: str | Riferimento) -> Riferimento:
    if isinstance(norma, Riferimento):
        return norma
    r = trova_riferimenti(norma)
    if not r:
        raise ValueError(f"Norma non riconosciuta: {norma!r}. Esempi: 'legge 31 dicembre 2009, n. 196', 'd.lgs. 82/2005'.")
    return r[0]


def citanti(norma: str | Riferimento, articolo: str | None = None, dal: str | None = None) -> pd.DataFrame:
    """Atti dell'archivio il cui testo cita la norma (stesso tipo, anno e numero, in forma completa o breve).
    Con `articolo` richiede che "articolo N" (o "art. N") preceda il riferimento entro poche parole."""
    rif = _rif(norma)
    d = carica_indice()
    if dal:
        d = d[d.data_gu >= dal]
    righe = []
    for r in d.itertuples():
        t = testo_atto(r.testo)
        if not t or rif.numero not in t:
            continue
        colpi = [x for x in trova_riferimenti(t)
                 if x.tipo == rif.tipo and x.numero == rif.numero and (x.anno == rif.anno or rif.anno is None)]
        if articolo:
            pat = re.compile(rf"\bart(?:icol[oi]|t?\.)\s*{re.escape(articolo)}\b[^.;]{{0,160}}$", re.I)
            colpi = [x for x in colpi if pat.search(t[max(0, x.pos - 200): x.pos])]
        if colpi:
            x = colpi[0]
            righe.append({"codice": r.codice, "data_gu": r.data_gu, "tipo": r.tipo, "intestazione": r.intestazione,
                          "titolo": r.titolo, "citazioni": len(colpi), "url_gu": r.url_gu,
                          "estratto": re.sub(r"\s+", " ", t[max(0, x.pos - 120): x.pos + len(x.testo) + 80])})
    out = pd.DataFrame(righe)
    return out.sort_values("data_gu", ascending=False) if not out.empty else out


def trova_atto(norma: str | Riferimento) -> pd.DataFrame:
    """Righe dell'indice corrispondenti all'atto citato (tipo, numero e anno o data)."""
    rif = _rif(norma)
    d = carica_indice()
    t = TIPO_INDICE.get(rif.tipo)
    if not t:
        return d.iloc[0:0]
    d = d[(d.tipo == t) & (d.numero_atto == rif.numero)]
    if rif.data:
        d = d[d.data_atto == rif.data.isoformat()]
    elif rif.anno:
        d = d[d.data_atto.str[:4] == str(rif.anno)]
    return d


def _stampa(df: pd.DataFrame, colonne: list[str]) -> None:
    if df.empty:
        print("Nessun risultato.")
        return
    for r in df.to_dict("records"):
        print(f"- {r['data_gu']} | {r['tipo']} | {r['intestazione']} — {r['titolo'][:160]}")
        for c in colonne:
            if r.get(c):
                print(f"    {c}: {r[c]}")
    print(f"\n{len(df)} risultati.")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Ricerca nell'archivio della Gazzetta Ufficiale")
    ap.add_argument("parole", nargs="?", default="", help='parole chiave; "frase esatta" tra virgolette')
    ap.add_argument("--tipo", nargs="*", help="legge, decreto-legge, decreto legislativo, DPR, DPCM, DM, delibera, comunicato…")
    ap.add_argument("--dal")
    ap.add_argument("--al")
    ap.add_argument("--solo-titolo", action="store_true")
    ap.add_argument("--cita", help="trova gli atti che citano questa norma")
    ap.add_argument("--articolo", help="con --cita: articolo della norma citata")
    ap.add_argument("--atto", help="cerca un atto per estremi")
    ap.add_argument("--limite", type=int, default=50)
    a = ap.parse_args()
    if a.cita:
        _stampa(citanti(a.cita, a.articolo, a.dal), ["citazioni", "estratto", "url_gu"])
    elif a.atto:
        _stampa(trova_atto(a.atto), ["url_gu", "url_normattiva", "testo"])
    else:
        _stampa(cerca(a.parole, a.tipo, a.dal, a.al, a.solo_titolo, a.limite), ["trovato_in", "estratto", "url_gu"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
