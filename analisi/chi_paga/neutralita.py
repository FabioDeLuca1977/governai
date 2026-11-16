"""Stessa regola per tutte le imprese (bozza 01-P25): aliquote effettive prima e dopo, costo e gettito.

*Bozza scritta da un agente AI il 16 novembre 2026; da valutare con il panel e da approvare; non rivista da una persona.*

Usa le formule e i parametri di `calcola.py` / `parametri.yaml` (regole 2026) e aggiunge le due regole della proposta:
 (a) SNC, SAS e ditte individuali in contabilita' ordinaria: 24% sugli utili lasciati in azienda (modello IRI,
     ex art. 55-bis TUIR), IRPEF progressiva solo su cio' che si preleva; contributi INPS sempre sull'intero reddito;
 (b) dividendi della propria societa' operativa trattenuti in una holding personale e non reinvestiti in attivita'
     vere entro 3 anni: tassati al socio come se fossero distribuiti (26%), con credito alla distribuzione vera.

Uso:
    python analisi/chi_paga/neutralita.py              # prove, scrive neutralita.csv, stampa costo e gettito
    python analisi/chi_paga/neutralita.py --solo-prove

Le ipotesi della proposta (non numeri di legge vigente) stanno nel dizionario PROPOSTA qui sotto, con la fonte.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

QUI = Path(__file__).resolve().parent
sys.path.insert(0, str(QUI))
import calcola as C  # noqa: E402  (formule e parametri 2026 del calcolatore "Chi paga quanto")

P = C.P

# ---------------------------------------------------------------- parametri della proposta (bozza)
PROPOSTA = {
    "aliquota_utili_trattenuti": P["ires"]["aliquota"],   # 24%, come l'IRES (art. 77 TUIR), come l'IRI 2017
    "tetto_essenziale_per_socio": 100_000,   # ESSENZIALE: il 24% vale solo fino a 100.000 euro l'anno di utile
                                             # trattenuto per socio o imprenditore; oltre, IRPEF ordinaria
    "franchigia_holding": {"PIENA": 100_000, "ESSENZIALE": 500_000},  # dividendi trattenuti e non reinvestiti
                                             # l'anno, per gruppo familiare, che non pagano (regola b)
    "livelli": [50_000, 100_000, 300_000, 1_000_000],
    "quote_trattenute": [0.0, 0.5, 1.0],     # quota dell'utile (al netto dei contributi) lasciata in azienda
}

# ---------------------------------------------------------------- costo della regola (a): dalla RT IRI 2017
# Relazione tecnica alla L. 232/2016 (art. 68 ddl AC 4127-bis), come riportata dal Servizio Bilancio della Camera,
# "Verifica delle quantificazioni" AC 4127-bis, https://documenti.camera.it/leg17/dossier/Testi/VQ4127.htm
# Competenza, milioni: 2017 -1.212,1; 2018 -1.231,3; dal 2019 -1.255,8. Cassa: 2018 -1.986,6; 2019 -1.238,1.
# Stessi importi (con segno opposto) nella RT dell'abrogazione, L. 145/2018 c. 1055 (dossier Camera ID0006i, p. 1268).
RT_IRI = {
    "competenza_regime": 1.2558,          # mld, dal 2019
    "rapporto_cassa_primo_anno": 1986.6 / 1212.1,   # 1,64: saldo + acconto nel primo anno di cassa
}
AGGIORNAMENTO = {   # stima GovernAI: (basso, alto)
    "platea": (0.80, 1.00),      # societa' di persone in calo (652.832 dichiarazioni a.i. 2024, -2,9% sul 2023, MEF-DF);
                                 # numero in ordinaria 2024 non pubblicato: da verificare con il DF
    "aliquote": (0.95, 1.05),    # scaglioni 2026 (23/33/43) contro 2017 (23/27/38/41/43): meno vantaggio tra 28 e 50
                                 # mila, piu' vantaggio tra 50 e 75 mila; effetto netto piccolo e incerto
    "crescita_al_2028": (1.06, 1.10),  # redditi medi in ordinaria stabili (58.700 euro a.i. 2024, MEF-DF; circa 59.400
                                 # nella RT) e crescita nominale 2024-2028 del 1,5-2,5% l'anno
    "rientro_annuo": (0.10, 0.05),     # quota delle riserve "a 24%" prelevata ogni anno (paga IRPEF meno 24%):
                                 # recupero del rinvio; la RT ha cifre quasi costanti e non sembra contarlo (da verificare)
    "crescita_annua": (0.0, 0.02),
    "quota_essenziale": (0.50, 0.70),  # costo della ESSENZIALE (tetto 100.000 per socio) rispetto alla PIENA: ipotesi,
                                 # perche' i soci oltre 300.000 euro (7.185 nel 2024) pesano molto sul costo
}
ATTUAZIONE = 0.01   # mld/anno: modelli, controlli dei prelievi, Sogei (stima GovernAI)


def profilo_costo_a(variante: str = "PIENA") -> list[dict]:
    """Minor gettito anno per anno (mld, cassa), basso e alto. Decorrenza: periodo d'imposta 2028."""
    out = []
    q = (1.0, 1.0) if variante == "PIENA" else AGGIORNAMENTO["quota_essenziale"]
    for i, (k_pl, k_al, k_cr, p, g, qq) in enumerate(zip(AGGIORNAMENTO["platea"], AGGIORNAMENTO["aliquote"],
                                                          AGGIORNAMENTO["crescita_al_2028"], AGGIORNAMENTO["rientro_annuo"],
                                                          AGGIORNAMENTO["crescita_annua"], q)):
        c2028 = RT_IRI["competenza_regime"] * k_pl * k_al * k_cr * qq
        stock, comp = 0.0, {}
        for k, anno in enumerate(range(2028, 2034)):
            trattenuto = (1 + g) ** k          # utili trattenuti dell'anno (in unita' del primo anno)
            rientro = p * stock                # riserve prelevate nell'anno: tornano all'IRPEF
            comp[anno] = c2028 * (trattenuto - rientro)
            stock = stock * (1 - p) + trattenuto
        for anno in range(2027, 2034):
            if anno <= 2028:
                v = 0.0                         # acconti 2028 calcolati con le regole previgenti
            elif anno == 2029:
                v = comp[2028] * RT_IRI["rapporto_cassa_primo_anno"]
            else:
                v = comp[anno - 1]
            out.append({"variante": variante, "scenario": "basso" if i == 0 else "alto", "anno": anno, "mld": round(v, 3)})
    return out


# ---------------------------------------------------------------- gettito della regola (b): base NON pubblicata
# Nessuna fonte ufficiale dice quanti dividendi delle societa' operative arrivano alle holding personali e quanti
# restano fermi. Il DF ha il dato (Redditi SC, quadro RF: utili esclusi art. 89; prospetto partecipazioni) ma non lo
# pubblica. Unico riferimento: ritenute 26% sugli utili 6.695 mln nel 2025 (Bollettino entrate n. 286), cioe' circa
# 25,7 mld di dividendi pagati a persone (e non residenti). Tutto sotto e' ipotesi GovernAI (basso, alto).
BASE_B = {
    "dividendi_operativi_a_holding_personali": (5.0, 12.0),   # mld/anno, ordine di grandezza
    "quota_ferma_dopo_3_anni": (0.20, 0.35),     # non distribuita e non reinvestita in attivita' vere
    "quota_oltre_franchigia": {"PIENA": (0.75, 0.85), "ESSENZIALE": (0.50, 0.65)},
    "holding_estere_in_piu_PIENA": (0.03, 0.08),  # quota di base in piu' dalle holding estere di residenti
    "aliquota": P["dividendi"]["ritenuta_persona_fisica"] * (1 - P["dividendi"]["quota_imponibile_holding"] * P["ires"]["aliquota"]),
    "riduzione_comportamenti": (0.60, 0.50),      # utili lasciati nella societa' operativa (legittimo e neutrale),
                                                  # piu' reinvestimenti, piu' distribuzioni
    "quota_strutturale": (0.55, 0.65),            # il resto e' anticipo di ritenute che si sarebbero pagate comunque
}


def gettito_b() -> dict:
    out = {}
    for v in ("ESSENZIALE", "PIENA"):
        lo_hi = []
        for i in (0, 1):
            base = BASE_B["dividendi_operativi_a_holding_personali"][i] * BASE_B["quota_ferma_dopo_3_anni"][i]
            quota = BASE_B["quota_oltre_franchigia"][v][i]
            if v == "PIENA":
                quota += BASE_B["holding_estere_in_piu_PIENA"][i]
            statico = base * quota * BASE_B["aliquota"]
            lo_hi.append(statico * (1 - BASE_B["riduzione_comportamenti"][i]) * BASE_B["quota_strutturale"][i])
        out[v] = tuple(round(x, 3) for x in lo_hi)
    out["FN13"] = out["ESSENZIALE"]
    out["FN14"] = tuple(round(p - e, 3) for p, e in zip(out["PIENA"], out["ESSENZIALE"]))
    return out


# ---------------------------------------------------------------- aliquote effettive per gruppo, prima e dopo
def _irpef(base: float, autonomo: bool) -> tuple[float, float]:
    det = C.detrazione_autonomo(base) if autonomo else 0.0
    return C.irpef_e_addizionali(base, det) if base > 0 else (0.0, 0.0)


def impresa_persone(r: float, s: float, tipo: str, variante: str) -> tuple[float, float, float, str]:
    """SNC (quota del socio, IRAP della societa' per quota) o ditta individuale (niente IRAP).
    s = quota dell'utile al netto dei contributi lasciata in azienda. Ritorna (imposte prima, dopo, contributi, nota)."""
    snc = tipo == "snc"
    irap = C.irap_societa(r * P["snc"]["numero_soci"], "societa_persone") / P["snc"]["numero_soci"] if snc else 0.0
    contr = C.contributi_artcom(r, "commercianti")          # sull'intero reddito, prima e dopo (come IRI, c. 2)
    netto = max(0.0, r - contr)
    i0, a0 = _irpef(netto, autonomo=not snc)
    prima = irap + i0 + a0
    trattenuto = s * netto
    al24 = trattenuto if variante == "PIENA" else min(trattenuto, PROPOSTA["tetto_essenziale_per_socio"])
    base_irpef = netto - al24
    i1, a1 = _irpef(base_irpef, autonomo=not snc)
    iri = al24 * PROPOSTA["aliquota_utili_trattenuti"]
    dopo = irap + iri + i1 + a1
    nota = (f"contributi {C.eur(contr)}; trattenuto {C.eur(trattenuto)} di cui al 24% {C.eur(al24)}; "
            f"IRPEF+add. prima {C.eur(i0 + a0)}, dopo {C.eur(i1 + a1)}" + (f"; IRAP {C.eur(irap)}" if snc else "; IRAP non dovuta"))
    return prima, dopo, contr, nota


def srl(r: float, s: float) -> tuple[float, float, float, str]:
    c = C.srl_conti(r, 0.0)
    imp = c["irap"] + c["ires"] + (1 - s) * c["dividendo"] * P["dividendi"]["ritenuta_persona_fisica"]
    return imp, imp, 0.0, f"IRAP {C.eur(c['irap'])}, IRES {C.eur(c['ires'])}; 26% sulla parte distribuita; nessun cambio"


def srl_holding(r: float, s: float, variante: str, reinveste: bool) -> tuple[float, float, float, str]:
    c = C.srl_conti(r, 0.0)
    d = c["dividendo"]
    ires_h = d * P["dividendi"]["quota_imponibile_holding"] * P["ires"]["aliquota"]
    disponibile = d - ires_h
    rit = P["dividendi"]["ritenuta_persona_fisica"]
    distribuito = (1 - s) * disponibile
    fermo = s * disponibile
    prima = c["irap"] + c["ires"] + ires_h + distribuito * rit
    tassato = 0.0 if reinveste else max(0.0, fermo - PROPOSTA["franchigia_holding"][variante])
    dopo = prima + tassato * rit
    nota = (f"dividendo alla holding {C.eur(d)} (IRES 1,2% {C.eur(ires_h)}); fermo nella holding {C.eur(fermo)}; "
            + ("reinvestito in attivita' vere: nessuna imposta in piu'" if reinveste else
               f"oltre la franchigia {C.eur(tassato)} tassato al 26% come distribuito, con credito alla distribuzione"))
    return prima, dopo, 0.0, nota


def riga(gruppo, variante, s, r, prima, dopo, contr, nota):
    return {
        "gruppo": gruppo, "variante_proposta": variante, "quota_lasciata_in_impresa": s, "reddito_lordo": r,
        "imposte_prima": round(prima, 2), "imposte_dopo": round(dopo, 2), "contributi": round(contr, 2),
        "aliquota_imposte_prima": round(100 * prima / r, 2), "aliquota_imposte_dopo": round(100 * dopo / r, 2),
        "aliquota_totale_prima": round(100 * (prima + contr) / r, 2),
        "aliquota_totale_dopo": round(100 * (dopo + contr) / r, 2),
        "differenza_punti": round(100 * (dopo - prima) / r, 2), "note": nota,
    }


def tabella() -> list[dict]:
    out = []
    for variante in ("PIENA", "ESSENZIALE"):
        for r in PROPOSTA["livelli"]:
            r = float(r)
            for s in PROPOSTA["quote_trattenute"]:
                out.append(riga("Socio di SNC (2 soci al 50%)", variante, s, r, *impresa_persone(r, s, "snc", variante)))
                out.append(riga("Ditta individuale in ordinaria", variante, s, r, *impresa_persone(r, s, "ditta", variante)))
                out.append(riga("Socio di SRL (senza holding)", variante, s, r, *srl(r, s)))
                out.append(riga("SRL tramite holding, utili fermi", variante, s, r, *srl_holding(r, s, variante, False)))
                out.append(riga("SRL tramite holding, utili reinvestiti", variante, s, r, *srl_holding(r, s, variante, True)))
    return out


# ---------------------------------------------------------------- prove
def prove() -> None:
    def vicino(a, b, tol=0.6):
        assert abs(a - b) <= tol, (a, b)

    # 1. Tutto prelevato: con la regola (a) non cambia nulla per SNC e ditta
    for r in (50_000.0, 1_000_000.0):
        for t in ("snc", "ditta"):
            p, d, _, _ = impresa_persone(r, 0.0, t, "PIENA")
            vicino(p, d, 0.01)
    # 2. SNC 1.000.000, tutto lasciato in azienda: IRAP + 24% dell'utile netto contributi
    contr = C.contributi_artcom(1_000_000, "commercianti")
    irap = C.irap_societa(2_000_000, "societa_persone") / 2
    _, d, _, _ = impresa_persone(1_000_000.0, 1.0, "snc", "PIENA")
    vicino(d, irap + 0.24 * (1_000_000 - contr))
    # 3. Il "prima" della SNC coincide con calcola.py (gruppo 5)
    vicino(impresa_persone(300_000.0, 0.0, "snc", "PIENA")[0], C.gruppo_snc(300_000.0)[0]["imposte"], 0.01)
    # 4. Il "prima" della holding che trattiene tutto coincide con calcola.py (gruppo 7, prima riga)
    vicino(srl_holding(1_000_000.0, 1.0, "PIENA", False)[0], C.gruppo_holding(1_000_000.0)[0]["imposte"], 0.01)
    # 5. Holding sotto franchigia (PIENA, 100.000): a 100.000 euro di utile nessun cambio
    p, d, _, _ = srl_holding(100_000.0, 1.0, "PIENA", False)
    vicino(p, d, 0.01)
    # 6. Holding a 1.000.000, utili fermi, PIENA: dopo = prima + 26% x (trattenuto - 100.000)
    p, d, _, _ = srl_holding(1_000_000.0, 1.0, "PIENA", False)
    c = C.srl_conti(1_000_000, 0.0)
    trattenuto = c["dividendo"] * (1 - 0.05 * 0.24)
    vicino(d - p, 0.26 * (trattenuto - 100_000))
    print("Casi di prova: tutti superati.")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    prove()
    if "--solo-prove" in sys.argv:
        return
    righe = tabella()
    with open(QUI / "neutralita.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(righe[0].keys()))
        w.writeheader()
        w.writerows(righe)
    print(f"Scritte {len(righe)} righe in {QUI / 'neutralita.csv'}\n")
    print("Aliquota effettiva di sole imposte (prima -> dopo), PIENA, utile tutto lasciato in impresa (s=1) e meta' (s=0,5):")
    for x in righe:
        if x["variante_proposta"] == "PIENA" and x["quota_lasciata_in_impresa"] in (0.5, 1.0):
            print(f"  {x['gruppo'][:40]:40} s={x['quota_lasciata_in_impresa']:.1f} {x['reddito_lordo']:>10,.0f}  "
                  f"{x['aliquota_imposte_prima']:6.2f} -> {x['aliquota_imposte_dopo']:6.2f}  "
                  f"(totale {x['aliquota_totale_prima']:6.2f} -> {x['aliquota_totale_dopo']:6.2f})")
    print("\nCosto della regola (a), mld di minor gettito, cassa (basso / alto):")
    for v in ("PIENA", "ESSENZIALE"):
        prof = profilo_costo_a(v)
        for anno in range(2027, 2034):
            lo = next(p["mld"] for p in prof if p["anno"] == anno and p["scenario"] == "basso")
            hi = next(p["mld"] for p in prof if p["anno"] == anno and p["scenario"] == "alto")
            print(f"  {v:10} {anno}: {lo:5.2f} - {hi:5.2f}")
    g = gettito_b()
    print("\nGettito della regola (b), mld a regime (2033), parte strutturale (basso - alto):")
    for k in ("ESSENZIALE", "PIENA", "FN13", "FN14"):
        print(f"  {k:10} {g[k][0]:5.3f} - {g[k][1]:5.3f}")


if __name__ == "__main__":
    main()
