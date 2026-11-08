"""Pipeline dinamica di GovernAI: dati nuovi → indicatori → allerte → programma del momento → bollettino.

Passi:
  1. sentinella: rileva gli aggiornamenti delle fonti ufficiali e scarica ciò che è cambiato;
  2. indicatori: calcola il cruscotto (ultimo valore, variazioni) e ne conserva lo storico;
  3. allerte: valuta le regole di config.yaml (es. inflazione > 3%, spread > 200 pb);
  4. ricalcolo: registro delle coperture, motore dei valori, ottimizzatore del programma;
     il "programma del momento" applica le priorità e le sospensioni delle allerte attive;
  5. bollettino: sistema/bollettini/AAAA-MM-GG.md, con cosa è cambiato e cosa propone il sistema;
  6. revisione AI: se ci sono documenti nuovi o variazioni rilevanti, scrive i compiti per il livello AI
     (sistema/stato/revisione_ai.json), che aggiorna stime e coperture con giudizio umano-AI.

Uso:  python pipeline.py [--completo] [--senza-download] [--ricalcola]
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

import pandas as pd
import yaml

QUI = Path(__file__).resolve().parent
RADICE = QUI.parent
SERIE = RADICE / "dati" / "serie"
STATO = QUI / "stato"
BOLL = QUI / "bollettini"
STORICO_IND = RADICE / "dati" / "storico" / "_indicatori.csv"


def esegui(cmd: list[str], cwd: Path, timeout: int = 1800) -> tuple[bool, str]:
    r = subprocess.run([sys.executable, *cmd], cwd=cwd, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=timeout)
    # il risolutore HiGHS a volte stampa messaggi diagnostici dopo il riepilogo: non sono il nostro esito
    righe = [x for x in (r.stdout if r.returncode == 0 else r.stderr).strip().splitlines() if not x.startswith("Highs")]
    return r.returncode == 0, (righe[-1] if righe else "")[:300]


# --- Indicatori ----------------------------------------------------------------

def serie_indicatore(ind: dict) -> pd.DataFrame | None:
    if ind.get("calcolo") == "spread":
        f = SERIE / "00c_rendimenti_decennali.csv"
        if not f.exists():
            return None
        d = pd.read_csv(f)
        p = d.pivot_table(index="time", columns="geo", values="valore").dropna()
        return pd.DataFrame({"time": p.index, "valore": (p["IT"] - p["DE"]) * 100}).reset_index(drop=True)
    f = SERIE / f"{ind['serie']}.csv"
    if not f.exists():
        return None
    d = pd.read_csv(f)
    for col, val in (ind.get("filtro") or {}).items():
        if col in d.columns:
            d = d[d[col].astype(str) == str(val)]
    tcol = "time" if "time" in d.columns else ("anno" if "anno" in d.columns else None)
    if tcol is None or "valore" not in d.columns:
        return None
    d = d[[tcol, "valore"] + (["flag"] if "flag" in d.columns else [])].rename(columns={tcol: "time"})
    d = d.dropna(subset=["valore"]).drop_duplicates("time", keep="last")
    return d.sort_values("time").reset_index(drop=True)


def calcola_indicatori(conf: dict) -> list[dict]:
    out = []
    for ind in conf.get("indicatori", []):
        d = serie_indicatore(ind)
        if d is None or d.empty:
            out.append({**ind, "stato": "serie non disponibile"})
            continue
        v = float(d.valore.iloc[-1])
        prec = float(d.valore.iloc[-2]) if len(d) > 1 else None
        p12 = float(d.valore.iloc[-13]) if len(d) > 12 else None
        out.append({"id": ind["id"], "nome": ind["nome"], "unita": ind.get("unita", ""), "meglio": ind.get("meglio"),
                    "valori": ind.get("valori", []), "periodo": str(d.time.iloc[-1]), "valore": round(v, 3),
                    "delta": None if prec is None else round(v - prec, 3),
                    "delta12": None if p12 is None else round(v - p12, 3),
                    "provvisorio": bool("flag" in d.columns and str(d.flag.iloc[-1]) not in ("", "nan")),
                    "stato": "ok"})
    return out


def aggiorna_storico(ind: list[dict], oggi: str) -> None:
    STORICO_IND.parent.mkdir(parents=True, exist_ok=True)
    nuovi = pd.DataFrame([{"rilevato": oggi, "id": i["id"], "periodo": i["periodo"], "valore": i["valore"]}
                          for i in ind if i.get("stato") == "ok"])
    if STORICO_IND.exists():
        vecchi = pd.read_csv(STORICO_IND, dtype={"periodo": str})
        chiave = set(zip(vecchi.id, vecchi.periodo.astype(str), vecchi.valore))
        nuovi = nuovi[[(r.id, str(r.periodo), r.valore) not in chiave for r in nuovi.itertuples()]]
        nuovi = pd.concat([vecchi, nuovi], ignore_index=True)
    nuovi.to_csv(STORICO_IND, index=False)


# --- Allerte -------------------------------------------------------------------

def valuta_regole(conf: dict, ind: list[dict]) -> list[dict]:
    per_id = {i["id"]: i for i in ind if i.get("stato") == "ok"}
    attive = []
    for r in conf.get("regole", []):
        i = per_id.get(r["indicatore"])
        if not i:
            continue
        amb = {"valore": i["valore"], "delta": i["delta"], "delta12": i["delta12"]}
        if any(v is None for k, v in amb.items() if k in r["condizione"]):
            continue
        if eval(r["condizione"], {"__builtins__": {}}, amb):  # condizioni scritte in config.yaml, non input esterni
            attive.append({**r, "valore": i["valore"], "periodo": i["periodo"], "unita": i["unita"]})
    return attive


# --- Programma del momento -----------------------------------------------------

def selezione(file: Path) -> pd.DataFrame:
    s = pd.read_csv(file)
    return s[(s.tipo == "variante") & (s.scelta == 1)][["proposta_id", "variante", "costo_regime"]].set_index("proposta_id")


def confronta(prima: pd.DataFrame, dopo: pd.DataFrame) -> list[str]:
    righe = []
    for p in sorted(set(prima.index) | set(dopo.index)):
        a = prima.loc[p, "variante"] if p in prima.index else None
        b = dopo.loc[p, "variante"] if p in dopo.index else None
        if a != b:
            righe.append(f"{p}: {a or 'esclusa'} → {b or 'esclusa'}")
    return righe


# --- Bollettino ----------------------------------------------------------------

def semaforo(i: dict) -> str:
    d = i.get("delta")
    if d is None or i.get("meglio") not in ("su", "giu") or abs(d) < 1e-9:
        return "⚪"
    buono = (d > 0) == (i["meglio"] == "su")
    return "🟢" if buono else "🔴"


def num(v, dec=2) -> str:
    if v is None:
        return "—"
    return f"{v:,.{dec}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def segno(v, dec=2) -> str:
    return "—" if v is None else (f"{v:+.{dec}f}").replace(".", ",")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--completo", action="store_true", help="rilancia tutti gli script di download")
    ap.add_argument("--senza-download", action="store_true", help="salta la sentinella (usa i dati presenti)")
    ap.add_argument("--ricalcola", action="store_true", help="ricalcola i modelli anche senza dati nuovi")
    ap.add_argument("--senza-ai", action="store_true", help="non avvia il livello AI (revisione_ai.py)")
    a = ap.parse_args()
    conf = yaml.safe_load((QUI / "config.yaml").read_text(encoding="utf-8"))
    oggi = date.today().isoformat()
    STATO.mkdir(exist_ok=True)
    BOLL.mkdir(exist_ok=True)
    log = []

    # 1. sentinella
    sent = {}
    if not a.senza_download:
        ok, msg = esegui(["sentinella.py"] + (["--completo"] if a.completo else []), QUI)
        log.append(f"sentinella: {msg}" if ok else f"ERRORE sentinella: {msg}")
        try:
            sent = json.loads((STATO / "ultima_sentinella.json").read_text(encoding="utf-8"))
        except FileNotFoundError:
            pass

    # 2-3. indicatori e allerte
    ind = calcola_indicatori(conf)
    aggiorna_storico(ind, oggi)
    prec_ind = {i["id"]: i for i in json.loads((STATO / "indicatori.json").read_text(encoding="utf-8"))} \
        if (STATO / "indicatori.json").exists() else {}
    (STATO / "indicatori.json").write_text(json.dumps(ind, ensure_ascii=False, indent=1), encoding="utf-8")
    allerte = valuta_regole(conf, ind)
    prec_allerte = set(json.loads((STATO / "allerte.json").read_text(encoding="utf-8"))) \
        if (STATO / "allerte.json").exists() else set()
    (STATO / "allerte.json").write_text(json.dumps([r["id"] for r in allerte]), encoding="utf-8")
    nuove_allerte = [r for r in allerte if r["id"] not in prec_allerte]

    # 3b. apprendimento: obiettivi raggiunti o mancati, calibrazione delle previsioni
    if (RADICE / "apprendimento" / "obiettivi.yaml").exists():
        esegui(["aggiorna_obi.py"], RADICE / "apprendimento")  # serie degli obiettivi derivate dai dati del giorno
        ok, msg = esegui(["valuta.py"], RADICE / "apprendimento")
        log.append(msg if ok else f"ERRORE apprendimento: {msg}")

    # 3c. verifica giuridica: unisce le verifiche degli esperti (le incompatibilità diventano linee rosse)
    if list((RADICE / "giuridico").glob("conformita_*.csv")):
        esegui(["unisci.py"], RADICE / "giuridico")

    # 3d. legislazione: archivio incrementale della Gazzetta Ufficiale (solo i fascicoli nuovi)
    if not a.senza_download and (RADICE / "legislazione" / "scarica_gu.py").exists():
        ok, msg = esegui(["scarica_gu.py"], RADICE / "legislazione", timeout=3600)
        log.append(f"legislazione: {msg}" if ok else f"ERRORE legislazione: {msg}")

    # 3d-bis. europa: atti UE (GU L), scadenze di recepimento, Semestre europeo, infrazioni
    if not a.senza_download and (RADICE / "europa" / "scarica_ue.py").exists():
        ok, msg = esegui(["scarica_ue.py"], RADICE / "europa", timeout=1800)
        log.append(f"europa: {msg}" if ok else f"ERRORE europa: {msg}")
    elif (RADICE / "europa" / "uscite.py").exists():
        esegui(["uscite.py"], RADICE / "europa")  # senza rete: rigenera le uscite dall'archivio

    # 3d-ter. costituzione: screening costituzionale degli atti con forza di legge nuovi della Gazzetta;
    #         il lunedì aggiorna i dati aperti della Corte costituzionale
    if (RADICE / "costituzione" / "controllo.py").exists():
        if not a.senza_download and date.today().weekday() == 0:
            ok, msg = esegui(["giurisprudenza.py", "--scarica", "--forza", "--verifica-parametri"],
                             RADICE / "costituzione", timeout=1800)
            log.append(f"giurisprudenza: {msg}" if ok else f"ERRORE giurisprudenza: {msg}")
        ok, msg = esegui(["controllo.py", "--gu"], RADICE / "costituzione", timeout=1800)
        log.append(msg if ok else f"ERRORE costituzione: {msg}")

    # 3e. governo ombra: verifica le previsioni scadute del Consiglio dei ministri e aggiorna la credibilità
    if (RADICE / "governo" / "previsioni.csv").exists():
        ok, msg = esegui(["consiglio.py", "--valuta"], RADICE / "governo")
        log.append(msg if ok else f"ERRORE consiglio: {msg}")
    # 3f. stato dell'arte: le decisioni in vigore reggono ancora? Se no, accoda il riesame della seduta
    if list((RADICE / "governo" / "verbali").glob("*.json")):
        ok, msg = esegui(["consiglio.py", "--verifica", "--accoda"], RADICE / "governo")
        log.append(msg if ok else f"ERRORE verifica consiglio: {msg}")

    # 4. ricalcolo
    dati_nuovi = bool(sent.get("serie_cambiate")) or bool(nuove_allerte)
    priorita = sorted({p for r in allerte for p in r.get("priorita", [])})
    sospese = sorted({p for r in allerte for p in r.get("sospendi", [])})
    diff_momento, diff_storico = [], []
    if dati_nuovi or a.ricalcola or not (RADICE / "programma" / "selezione_momento.csv").exists():
        for cmd, cwd in [(["controlla.py"], RADICE / "registro"),
                         (["decidi.py", "--n", "20000", "--campioni-zaino", "1000"], RADICE / "motore"),
                         (["ottimizza.py", "--n", "150", "--etichetta", "riferimento"], RADICE / "programma"),
                         (["ottimizza.py", "--n", "150", "--etichetta", "momento",
                           *(["--priorita", *priorita] if priorita else []),
                           *(["--escludi", *sospese] if sospese else [])], RADICE / "programma")]:
            ok, msg = esegui(cmd, cwd)
            nome = cmd[0] + (f" ({cmd[cmd.index('--etichetta') + 1]})" if "--etichetta" in cmd else "")
            log.append(f"{nome}: {msg}" if ok else f"ERRORE {nome}: {msg}")
        prog = RADICE / "programma"
        rif, mom = selezione(prog / "selezione_riferimento.csv"), selezione(prog / "selezione_momento.csv")
        diff_momento = confronta(rif, mom)
        prec_file = STATO / "selezione_momento_precedente.csv"
        if prec_file.exists():
            diff_storico = confronta(selezione(prec_file), mom)
        shutil.copy2(prog / "selezione_momento.csv", prec_file)
        costo_rif, costo_mom = rif.costo_regime.sum(), mom.costo_regime.sum()
    else:
        costo_rif = costo_mom = None
        log.append("modelli non ricalcolati: nessun dato nuovo e nessuna nuova allerta")

    # 6. compiti per il livello AI
    soglia = conf.get("parametri", {}).get("soglia_variazione_rilevante", 0.05)
    compiti = []
    for d in sent.get("documenti_nuovi", []):
        compiti.append({"tipo": "documento_nuovo", "aree": d["aree"], "dettaglio": f"{d['pagina']}: {d['documento']}",
                        "cosa_fare": "Leggere il documento; se cambia dati, stime o coperture usate dai dossier, "
                                     "aggiornare verifiche, registro/fondi.csv, programma/varianti o coperture_menu."})
    for i in ind:
        p = prec_ind.get(i["id"])
        if p and i.get("stato") == "ok" and p.get("valore") and p.get("periodo") != i["periodo"]:
            rel = abs(i["valore"] - p["valore"]) / max(abs(p["valore"]), 1e-9)
            if rel >= soglia:
                compiti.append({"tipo": "variazione_rilevante", "aree": [], "dettaglio":
                                f"{i['nome']}: {p['valore']} ({p['periodo']}) → {i['valore']} ({i['periodo']})",
                                "cosa_fare": "Valutare se cambiano diagnosi, costi o priorità delle proposte collegate."})
    for r in nuove_allerte:
        compiti.append({"tipo": "nuova_allerta", "aree": [], "dettaglio": r["messaggio"], "cosa_fare": r["azione"]})
    (STATO / "revisione_ai.json").write_text(json.dumps({"data": oggi, "compiti": compiti}, ensure_ascii=False, indent=1),
                                             encoding="utf-8")

    # 5. bollettino
    b = [f"# Bollettino GovernAI — {oggi}", "",
         f"*Generato automaticamente da `sistema/pipeline.py` alle {datetime.now():%H:%M}. "
         "Fonti: Eurostat, ISTAT, MEF/RGS, Banca d'Italia e documenti ufficiali osservati.*", "",
         "## 1. Cosa è cambiato nelle fonti", ""]
    if sent:
        if sent.get("prima_esecuzione"):
            b.append("- Prima esecuzione: creata la base di confronto. Dalle prossime esecuzioni il sistema segnala ogni variazione.")
        b += [f"- Modalità di aggiornamento: **{sent.get('modalita', '—')}**",
              f"- Dataset Eurostat aggiornati: {', '.join(sent.get('eurostat_aggiornati', [])) or 'nessuno'}",
              f"- File ufficiali aggiornati: {len(sent.get('file_aggiornati', []))}",
              f"- Serie cambiate e archiviate in `dati/storico/`: {', '.join(sent.get('serie_cambiate', [])) or 'nessuna'}",
              f"- Documenti nuovi sulle pagine osservate: {len(sent.get('documenti_nuovi', []))}"]
        for d in sent.get("documenti_nuovi", [])[:15]:
            b.append(f"  - {d['pagina']}: {d['documento']}")
        errori = sent.get("errori", []) + [k + ' ' + v for k, v in sent.get("script", {}).items() if v != "ok"]
        if errori:
            b.append(f"- Problemi: {'; '.join(errori)}")
    else:
        b.append("- Download non eseguito in questa esecuzione.")

    b += ["", "## 2. Cruscotto", "", "| | Indicatore | Periodo | Valore | Var. | Var. 12 periodi |", "|---|---|---|---|---|---|"]
    for i in ind:
        if i.get("stato") != "ok":
            b.append(f"| ⚪ | {i['nome']} | — | {i['stato']} | | |")
            continue
        prov = " *(provv.)*" if i["provvisorio"] else ""
        b.append(f"| {semaforo(i)} | {i['nome']} | {i['periodo']}{prov} | {num(i['valore'])} {i['unita']} | "
                 f"{segno(i['delta'])} | {segno(i['delta12'])} |")
    b += ["", "🟢 = variazione favorevole, 🔴 = sfavorevole rispetto all'osservazione precedente.", ""]

    b += ["## 3. Allerte attive", ""]
    if allerte:
        for r in allerte:
            nuovo = " **(nuova)**" if r in nuove_allerte else ""
            b += [f"- **{r['id']}**{nuovo}: {r['messaggio']} (valore {num(r['valore'])} {r['unita']}, {r['periodo']})",
                  f"  - Azione: {r['azione']}",
                  f"  - Priorità: {', '.join(r.get('priorita', [])) or '—'}; sospese: {', '.join(r.get('sospendi', [])) or '—'}"]
    else:
        b.append("Nessuna allerta attiva.")

    b += ["", "## 4. Programma del momento", ""]
    if costo_mom is not None:
        b += [f"Il programma di riferimento (tutte le coperture, nucleo robusto prima) costa **{num(costo_rif)} mld/anno**; "
              f"il programma adattato al momento costa **{num(costo_mom)} mld/anno**. Entrambi sono finanziati senza deficit.", "",
              "**Differenze rispetto al riferimento** (effetto delle allerte):", ""]
        b += [f"- {x}" for x in diff_momento] or ["- nessuna"]
        b += ["", "**Cambiamenti rispetto al bollettino precedente:**", ""]
        b += [f"- {x}" for x in diff_storico] or ["- nessuno"]
        b += ["", "Dettaglio: `programma/selezione_momento.md`."]
    else:
        b.append("Non ricalcolato: nessun dato nuovo e nessuna nuova allerta.")

    b += ["", "## 5. Revisione AI richiesta", ""]
    if compiti:
        b.append(f"**{len(compiti)} compiti** per il livello AI (`sistema/stato/revisione_ai.json`):")
        b += [f"- [{c['tipo']}] {c['dettaglio']} → {c['cosa_fare']}" for c in compiti[:25]]
    else:
        b.append("Nessuna revisione necessaria.")
    b += ["", "## Registro tecnico", "", *[f"- {x}" for x in log]]
    (BOLL / f"{oggi}.md").write_text("\n".join(b), encoding="utf-8")
    (BOLL / "ultimo.md").write_text("\n".join(b), encoding="utf-8")
    print(f"bollettino: sistema/bollettini/{oggi}.md — allerte {len(allerte)}, compiti AI {len(compiti)}")

    # 7. livello AI: con documenti nuovi o nuove allerte, e comunque una volta a settimana per la nota del momento
    par = conf.get("parametri", {})
    settimanale = date.today().weekday() == int(par.get("ai_giorno_nota_settimanale", 0))
    if not a.senza_ai and par.get("ai_attivo", True) and (compiti or settimanale):
        if not (os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN")
                or (Path.home() / ".config" / "anthropic").exists()):
            avviso = ("\n\n## 6. Nota del livello AI\n\nLivello AI non eseguito: credenziali dell'API di Claude assenti "
                      "(impostare la variabile d'ambiente ANTHROPIC_API_KEY).")
            for f in (BOLL / f"{oggi}.md", BOLL / "ultimo.md"):
                f.write_text(f.read_text(encoding="utf-8") + avviso, encoding="utf-8")
            print("livello AI non eseguito: credenziali assenti")
        else:
            ok, msg = esegui(["revisione_ai.py"], QUI, timeout=3600)
            print(f"livello AI: {msg}" if ok else f"ERRORE livello AI: {msg}")

    # 7-bis. tabelle del documento di programma, generate dagli stessi risultati
    ok, msg = esegui(["documento.py"], RADICE / "programma")
    print(f"documento di programma: {msg}" if ok else f"ERRORE documento di programma: {msg}")

    # 8. registro di integrità: un anello della catena di impronte per questa esecuzione
    ok, msg = esegui(["catena.py", "--aggiungi", "aggiornamento", "--nota", f"allerte {len(allerte)}"], RADICE / "integrita")
    print(f"integrità: {msg}" if ok else f"ERRORE integrità: {msg}")

    # 9. dati per l'interfaccia web (docs/)
    ok, msg = esegui(["esporta_web.py"], QUI)
    print(f"interfaccia web: {msg}" if ok else f"ERRORE interfaccia web: {msg}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
