"""Controllo a campione dell'archivio europa/ contro EUR-Lex (pagina «Tutte le informazioni» di ogni atto).

Confronta titolo italiano, tipo, data del documento, data di pubblicazione nella GU L e termine di recepimento
registrati in archivio (da CELLAR) con quanto mostra EUR-Lex. Scrive archivio/verifica_campione.csv e stampa
una tabella markdown.

Uso:
  python verifica_campione.py                      # campione predefinito di 10 atti
  python verifica_campione.py 32026L2250 32024L1275
"""
from __future__ import annotations

import csv
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rete import ARCHIVIO, EURLEX, Rete, pulisci_spazi


def leggi(nome: str) -> dict[str, dict]:
    p = ARCHIVIO / nome
    with p.open(encoding="utf-8", newline="") as f:
        return {r["celex"]: r for r in csv.DictReader(f)}


def campione(atti: dict, direttive: dict) -> list[str]:
    """4 direttive nuove, 3 direttive con termine (scadenze), 3 regolamenti o decisioni nuovi di tipi diversi."""
    nuove = [c for c, r in atti.items() if r["tipo_codice"].startswith("DIR")][:4]
    vecchie = [c for c in ("32024L1275", "32024L1260", "32025L0516") if c in direttive]
    altri, tipi = [], set()
    for c, r in atti.items():
        if r["tipo_codice"] in ("REG", "REG_IMPL", "REG_DEL", "DEC", "DEC_IMPL") and r["tipo_codice"] not in tipi:
            altri.append(c)
            tipi.add(r["tipo_codice"])
        if len(altri) == 3:
            break
    return nuove + vecchie + altri


def norm(s: str) -> str:
    s = html.unescape(s or "").replace("’", "'").replace(" ", " ")
    return re.sub(r"\s+", " ", s).strip().lower()


def data_it(s: str) -> str:
    m = re.search(r"(\d{1,2})[./](\d{1,2})[./](\d{4})", s or "")
    return f"{m.group(3)}-{int(m.group(2)):02d}-{int(m.group(1)):02d}" if m else ""


def eurlex(rete: Rete, celex: str) -> dict:
    t = rete.get(f"{EURLEX}/ALL/?uri=CELEX:{celex}", timeout=90).content.decode("utf-8", errors="replace")
    campo = lambda nome: (re.search(rf"{nome}:\s*</dt>\s*<dd[^>]*>(.*?)</dd>", t, re.S) or [None, ""])[1]
    titolo = re.search(r'<p id="title"[^>]*>(.*?)</p>', t, re.S)
    recep = re.findall(r"Date of transposition:\s*</dt>\s*<dd[^>]*>(.*?)</dd>", t, re.S)
    rec = [(data_it(x), pulisci_spazi(re.sub(r"<[^>]+>", " ", x))) for x in recep]
    adoz = [d for d, x in rec if "adozione" in x]
    gu = re.search(r"GU L,\s*[\w/ ]+,\s*(\d{1,2}\.\d{1,2}\.\d{4})", t)
    return {"titolo": pulisci_spazi(re.sub(r"<[^>]+>", " ", html.unescape(titolo.group(1)))) if titolo else "",
            "tipo": pulisci_spazi(re.sub(r"<[^>]+>", " ", campo("Form"))),
            "data_atto": data_it(campo("Date of document")), "data_gu": data_it(gu.group(1)) if gu else "",
            "termini": [d for d, _ in rec], "termine": min(adoz) if adoz else (rec[0][0] if rec else "")}


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    atti, direttive = leggi("atti.csv"), leggi("direttive.csv")
    tutti = {**direttive, **atti}
    scelti = sys.argv[1:] or campione(atti, direttive)
    rete = Rete(1.0)
    righe = []
    for c in scelti:
        a = tutti[c]
        try:
            e = eurlex(rete, c)
        except Exception as ex:  # noqa: BLE001 - il controllo continua sugli altri atti
            righe.append({"celex": c, "esito": f"EUR-Lex non raggiungibile ({ex.__class__.__name__})"})
            continue
        termine_arch = a.get("termine_recepimento", "")
        controlli = {
            "titolo": norm(a["titolo"]) == norm(e["titolo"]),
            "tipo": norm(a["tipo"]) == norm(e["tipo"]),
            "data_atto": a["data_atto"] == e["data_atto"],
            "data_gu": (not a.get("data_gu")) or a["data_gu"] == e["data_gu"],
            # per le direttive con più termini l'archivio sceglie quello nella finestra: basta che sia tra quelli di EUR-Lex
            "termine": (termine_arch == "" and not e["termini"]) or termine_arch in e["termini"],
        }
        diff = [k for k, ok in controlli.items() if not ok]
        righe.append({"celex": c, "tipo": a["tipo"], "data_atto": a["data_atto"], "data_gu": a.get("data_gu", ""),
                      "termine_archivio": termine_arch, "termine_eurlex": e["termine"],
                      "termini_eurlex": " ".join(e["termini"]),
                      "esito": "coincide" if not diff else "DIVERSO: " + ", ".join(diff),
                      "titolo_eurlex": e["titolo"][:300], "tipo_eurlex": e["tipo"], "data_atto_eurlex": e["data_atto"],
                      "data_gu_eurlex": e["data_gu"]})
    campi = list(dict.fromkeys(k for r in righe for k in r))
    with (ARCHIVIO / "verifica_campione.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campi)
        w.writeheader()
        w.writerows(righe)
    print("| CELEX | Tipo | Data atto | GU L | Termine (archivio) | Termine (EUR-Lex) | Esito |")
    print("|---|---|---|---|---|---|---|")
    for r in righe:
        print(f"| {r['celex']} | {r.get('tipo', '')} | {r.get('data_atto', '')} | {r.get('data_gu', '') or '—'} | "
              f"{r.get('termine_archivio') or '—'} | {r.get('termine_eurlex') or '—'} | {r['esito']} |")
    ok = sum(1 for r in righe if r["esito"] == "coincide")
    print(f"\n{ok}/{len(righe)} atti coincidono in tutti i campi controllati (titolo, tipo, data, GU, termine).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
