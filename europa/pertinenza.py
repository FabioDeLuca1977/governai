"""Pertinenza degli atti UE per GovernAI: aree dei ministeri, proposte del programma, esperti, tipo di impatto.

Regole trasparenti e deterministiche, tutte in regole.yaml (aree, parole, capitoli del repertorio, impatto)
più due fonti del repository lette senza modificarle:
  - governo/esperti.yaml: le "parole" di ogni esperto (stesso criterio di governo/consiglio.py);
  - programma/schede/*.md: gli atti UE citati nella scheda di ogni proposta (es. "Reg. (UE) 2024/1747" -> 03-P2).

Uso da riga di comando, per capire perché un atto è stato classificato così:
  python pertinenza.py 32026L2250
"""
from __future__ import annotations

import re
import sys
from functools import lru_cache
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rete import QUI, RADICE

TIPI_OBBLIGO_RECEPIMENTO = {"DIR", "DIR_DEL", "DIR_IMPL"}
TIPI_OBBLIGO_DIRETTO = {"REG", "REG_DEL", "REG_IMPL", "DEC", "DEC_DEL", "DEC_IMPL"}
TIPI_INFORMATIVI = {"CORRIGENDUM", "DEC_ADOPT_INTERNATION", "REG_ADOPT_INTERNATION", "AGREE_INTERNATION", "AGREE_PROT",
                    "PROC_RULES", "RES", "GUIDELINE"}
ETICHETTE_AREE = {"01": "Economia e imprese", "02": "Lavoro, welfare e famiglia", "03": "Ambiente, energia e agricoltura",
                  "04": "Infrastrutture e territori", "05": "Istruzione, ricerca e cultura", "06": "Salute",
                  "07": "Giustizia, interno e difesa", "08": "Esteri, Europa e istituzioni", "09": "PA e digitale"}

# Riferimenti ad atti UE: "Reg. (UE) 2024/1747", "direttiva 2006/112/CE", "regolamento (UE) n. 1303/2013", "Dir. UE 2024/1275"
RE_RIF_UE = re.compile(
    r"\b(?:reg(?:olamento)?|dir(?:ettiva)?|decisione)\.?\s*(?:delegat[oa]\s+|di esecuzione\s+)?(?:\(?\s*(?:UE|CE|CEE|EU)\s*\)?\s*)?"
    r"(?:n\.\s*)?(\d{1,4})/(\d{1,4})", re.I)


def chiave_atto(a: str, b: str) -> str:
    """Normalizza 'anno/numero' anche per la vecchia forma 'numero/anno' dei regolamenti (es. 1303/2013 -> 2013/1303)."""
    x, y = int(a), int(b)
    anno = lambda v: 1950 <= v <= 2035
    if anno(x) and not anno(y):
        return f"{x}/{y}"
    if anno(y) and not anno(x):
        return f"{y}/{x}"
    if len(a) == 2 and anno(1900 + x if x > 50 else 2000 + x):  # 98/34/CE
        return f"{1900 + x if x > 50 else 2000 + x}/{y}"
    return f"{x}/{y}"


def chiave_celex(celex: str) -> str:
    m = re.match(r"3(\d{4})[A-Z]{1,2}(\d{4})", celex or "")
    return f"{m.group(1)}/{int(m.group(2))}" if m else ""


def compila(parole: list[str], intera: bool = False) -> list[tuple[str, re.Pattern]]:
    """Radici (inizio di parola) oppure, con intera=True, parole intere come in governo/consiglio.py."""
    out = []
    for p in parole or []:
        p = str(p)
        if p.startswith("re:"):
            out.append((p[3:], re.compile(p[3:], re.I)))
        else:
            out.append((p, re.compile(r"(?<![\w])" + re.escape(p.lower()) + (r"(?![\w])" if intera else ""), re.I)))
    return out


def togli_intestazione(t: str) -> str:
    """'Regolamento (UE) 2026/1 del Parlamento europeo e del Consiglio, del 3 ottobre 2026, che ...' -> 'che ...'."""
    return RE_INTESTAZIONE.sub("", t or "", count=1)


RE_INTESTAZIONE = re.compile(r"^.{0,220}?\b(?:del|dell['’])\s*\d{1,2}\s*(?:o\s+)?[a-z]+\s+\d{4}\s*,?\s*")



def trova(regole: list[tuple[str, re.Pattern]], testo: str) -> list[str]:
    return [p for p, rx in regole if rx.search(testo)]


class Regole:
    def __init__(self):
        r = yaml.safe_load((QUI / "regole.yaml").read_text(encoding="utf-8"))
        self.finestre = r["finestre"]
        self.aree = {k: {"nome": v["nome"], "capitoli": [str(c) for c in v.get("capitoli", [])], "parole": compila(v.get("parole"))}
                     for k, v in r["aree"].items()}
        self.materie_infrazioni = r["materie_infrazioni"]
        self.proposte = {k: compila(v) for k, v in r["proposte"].items()}
        imp = r["impatto"]
        self.vincolo = compila(imp["vincolo_bilancio"])
        self.opportunita = compila(imp["opportunita"])
        self.routine = [x.lower() for x in imp["routine"]]
        self.opp_esclusioni = [x.lower() for x in imp.get("opportunita_esclusioni", [])]
        self.altri_stati = r["altri_stati"]
        self.esperti_per_impatto = r["esperti_per_impatto"]
        self.esperto_infrazioni = r["esperto_infrazioni"]
        self.esperti = [(e["id"], compila(e.get("parole", []), intera=True))
                        for e in yaml.safe_load((RADICE / "governo" / "esperti.yaml").read_text(encoding="utf-8"))["esperti"]]
        self.titoli_proposte = titoli_proposte()
        self.citazioni = citazioni_schede()

    # --- singoli criteri ---------------------------------------------------------------------------
    def aree_da_repertorio(self, repertorio: str) -> dict[str, str]:
        out = {}
        for voce in filter(None, (repertorio or "").split("|")):
            codice = voce.split("=", 1)[0]
            for area, a in self.aree.items():
                for cap in a["capitoli"]:
                    if codice.startswith(cap):
                        # la sezione (4 cifre) vince sul capitolo (2 cifre) di un'altra area
                        if len(cap) == 2 and any(codice.startswith(c) for x in self.aree.values() for c in x["capitoli"] if len(c) == 4):
                            continue
                        out.setdefault(area, f"repertorio {codice}")
        return out

    def valuta(self, atto: dict) -> dict:
        """Restituisce aree, proposte, esperti, impatto, rilevanza, riguarda_italia e il motivo di ogni scelta."""
        titolo = (atto.get("titolo") or "").replace("’", "'")
        testo = " | ".join([togli_intestazione(titolo), (atto.get("eurovoc") or "").replace("|", " | "),
                            " | ".join(v.split("=", 1)[-1] for v in (atto.get("repertorio") or "").split("|"))]).lower()
        motivi = []
        aree = self.aree_da_repertorio(atto.get("repertorio", ""))
        for area, a in self.aree.items():
            hit = trova(a["parole"], testo)
            if hit:
                aree.setdefault(area, "parole: " + ", ".join(hit[:3]))
        # proposte: parole chiave e atti UE citati nelle schede
        proposte = {}
        for pid, regole in self.proposte.items():
            hit = trova(regole, testo)
            if hit:
                proposte[pid] = "parole: " + ", ".join(hit[:2])
        chiavi = {chiave_atto(m.group(1), m.group(2)) for m in RE_RIF_UE.finditer(titolo)} | {chiave_celex(atto.get("celex", ""))}
        for k in chiavi - {""}:
            for pid in self.citazioni.get(k, []):
                proposte.setdefault(pid, f"la scheda cita l'atto {k}")
        for pid in proposte:  # l'area della proposta collegata è sempre tra le aree dell'atto
            aree.setdefault(pid[:2], f"proposta {pid}")

        riguarda_italia = bool(re.search(r"\bItali[ae]\b|\bitalian[aoie]?\b", titolo))
        altri = [s for s in self.altri_stati if re.search(rf"\b{re.escape(s)}\b", titolo)]
        cod = atto.get("tipo_codice", "")
        proposta = cod.startswith("PROP_")
        if proposta:  # una proposta della Commissione si valuta come l'atto che diventerà (obbligo futuro)
            cod = cod[5:]
            motivi.append("proposta della Commissione: impatto atteso se adottata")
        tl = titolo.lower()
        routine = [r for r in self.routine if r in tl]

        if cod == "CORRIGENDUM" or "R(" in atto.get("celex", ""):
            impatto, perche = "informativo", "rettifica di un atto già pubblicato"
        elif altri and not riguarda_italia:
            impatto, perche = "informativo", "riguarda altri Stati: " + ", ".join(altri[:3])
        elif trova(self.vincolo, testo):
            impatto, perche = "vincolo di bilancio", "parole: " + ", ".join(trova(self.vincolo, testo)[:3])
        elif trova(self.opportunita, testo) and not any(x in tl for x in self.opp_esclusioni):
            impatto, perche = "opportunità", "parole: " + ", ".join(trova(self.opportunita, testo)[:3])
        elif cod in TIPI_OBBLIGO_RECEPIMENTO:
            impatto, perche = "obbligo", "direttiva: va recepita entro il termine"
        elif routine:
            impatto, perche = "informativo", "atto di gestione corrente: " + routine[0]
        elif cod in TIPI_OBBLIGO_DIRETTO:
            impatto, perche = "obbligo", "atto direttamente applicabile o rivolto agli Stati membri"
        else:
            impatto, perche = "informativo", f"tipo di atto {cod or 'non indicato'}"
        motivi.append(f"impatto: {perche}")

        legislativo = ((any(x in (atto.get("autori") or "") for x in ("Parlamento europeo", "Consiglio")) or proposta)
                       and cod in {"DIR", "REG", "DEC"} and not routine)
        if proposta and cod == "DEC" and not riguarda_italia:
            legislativo = False  # le proposte di decisione sono quasi sempre posizioni in organismi internazionali o atti singoli
        if impatto == "informativo":
            rilevanza = "media" if riguarda_italia else "bassa"
        elif riguarda_italia or impatto == "vincolo di bilancio" or cod in TIPI_OBBLIGO_RECEPIMENTO or legislativo:
            rilevanza = "alta"
        else:
            rilevanza = "media" if (aree or proposte) else "bassa"
        if proposte and rilevanza == "bassa" and impatto != "informativo":
            rilevanza = "media"

        esperti = [eid for eid, regole in self.esperti if trova(regole, testo)]
        for e in self.esperti_per_impatto.get(impatto, []):
            if e not in esperti:
                esperti.append(e)
        return {"aree": ",".join(sorted(aree)), "proposte": ",".join(sorted(proposte, key=ordine_proposta)),
                "esperti": ",".join(esperti), "impatto": impatto, "rilevanza": rilevanza,
                "riguarda_italia": "sì" if riguarda_italia else "",
                "motivo": "; ".join(motivi + [f"area {k}: {v}" for k, v in sorted(aree.items())] +
                                    [f"{k}: {v}" for k, v in sorted(proposte.items())])}

    def valuta_infrazione(self, r: dict) -> dict:
        testo = f"{r.get('oggetto', '')} | {r.get('materia', '')} | {r.get('norme', '')}".lower().replace("’", "'")
        aree = {a: "materia EUR-Infra" for a in self.materie_infrazioni.get(r.get("materia", ""), [])}
        for area, a in self.aree.items():
            if trova(a["parole"], testo):
                aree.setdefault(area, "parole")
        proposte = [pid for pid, regole in self.proposte.items() if trova(regole, testo)]
        for m in RE_RIF_UE.finditer(r.get("oggetto", "") + " " + r.get("norme", "")):
            proposte += self.citazioni.get(chiave_atto(m.group(1), m.group(2)), [])
        esperti = [eid for eid, regole in self.esperti if trova(regole, testo)]
        esperti += [e for e in self.esperto_infrazioni if e not in esperti]
        return {"aree": ",".join(sorted(aree)), "proposte": ",".join(sorted(set(proposte), key=ordine_proposta)),
                "esperti": ",".join(esperti)}


def ordine_proposta(pid: str):
    m = re.match(r"(\d{2})-([PC])(\d+)", pid)
    return (m.group(1), int(m.group(3))) if m else (pid, 0)


@lru_cache(maxsize=1)
def titoli_proposte() -> dict[str, str]:
    import csv
    with (RADICE / "motore" / "proposte.csv").open(encoding="utf-8", newline="") as f:
        return {r["proposta_id"]: r["titolo"] for r in csv.DictReader(f)}


@lru_cache(maxsize=1)
def citazioni_schede() -> dict[str, list[str]]:
    """{'2024/1747': ['03-P2'], ...}: atti UE citati nella sezione di ogni proposta delle schede del programma."""
    out: dict[str, list[str]] = {}
    for f in sorted((RADICE / "programma" / "schede").glob("*.md")):
        md = f.read_text(encoding="utf-8")
        parti = re.split(r"^## (\d{2}-[PC]\d+)\b", md, flags=re.M)
        for pid, corpo in zip(parti[1::2], parti[2::2]):
            for m in RE_RIF_UE.finditer(corpo):
                k = chiave_atto(m.group(1), m.group(2))
                if pid not in out.setdefault(k, []):
                    out[k].append(pid)
    return out


if __name__ == "__main__":
    import csv
    sys.stdout.reconfigure(encoding="utf-8")
    R = Regole()
    righe = {}
    for nome in ("atti.csv", "direttive.csv", "proposte_ue.csv"):
        p = QUI / "archivio" / nome
        if p.exists():
            with p.open(encoding="utf-8", newline="") as fh:
                righe.update({r["celex"]: r for r in csv.DictReader(fh)})
    for celex in sys.argv[1:] or []:
        r = righe.get(celex)
        if not r:
            print(f"{celex}: non in archivio")
            continue
        print(celex, "-", r["titolo"][:200])
        for k, v in R.valuta(r).items():
            print(f"  {k}: {v}")
    if len(sys.argv) == 1:
        print(f"{len(R.citazioni)} atti UE citati nelle schede; esempi: "
              + ", ".join(f"{k}->{'/'.join(v)}" for k, v in list(R.citazioni.items())[:8]))
