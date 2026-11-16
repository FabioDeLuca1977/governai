"""Chi paga quanto: prelievo su uno stesso reddito lordo prodotto, per gruppo di persone (regole 2026).

Calcolatore deterministico. Tutti i parametri fiscali stanno in parametri.yaml (con fonte):
il codice contiene solo le formule. Uso:

    python analisi/chi_paga/calcola.py            # verifica i casi di prova e scrive risultati.csv
    python analisi/chi_paga/calcola.py --solo-prove

Ogni funzione `gruppo_*` riceve il reddito lordo prodotto e restituisce una o piu' righe con:
imposte (tutte: IRPEF, addizionali, sostitutive, IRAP, IRES, ritenute), contributi obbligatori che
finanziano prestazioni proprie (pensione), contributi a carico del datore (solo dipendenti, a parte).
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

import yaml

QUI = Path(__file__).resolve().parent
P = yaml.safe_load((QUI / "parametri.yaml").read_text(encoding="utf-8"))


# ---------------------------------------------------------------- IRPEF e addizionali
def irpef_lorda(imponibile: float) -> float:
    imposta, inferiore = 0.0, 0.0
    for limite, aliquota in P["irpef"]["scaglioni"]["valore"]:
        superiore = imponibile if limite is None else min(imponibile, limite)
        if superiore > inferiore:
            imposta += (superiore - inferiore) * aliquota
        if limite is None or imponibile <= limite:
            break
        inferiore = limite
    return imposta


def _detrazione_tre_fasce(r: float, d: dict, k1: str, k2: str, k3: str, soglia1: float) -> float:
    if r <= soglia1:
        return d[k1]
    f2 = d[k2]
    if r <= f2["soglia"]:
        return f2["base"] + f2["variabile"] * (f2["soglia"] - r) / f2["ampiezza"]
    f3 = d[k3]
    if r <= f3["soglia"]:
        return f3["base"] * (f3["soglia"] - r) / f3["ampiezza"]
    return 0.0


def detrazione_dipendente(r: float) -> float:
    d = P["irpef"]["detrazione_lavoro_dipendente"]
    det = _detrazione_tre_fasce(r, d, "fino_15000", "tra_15000_28000", "tra_28000_50000", 15000)
    if 25000 < r <= 35000:
        det += d["maggiorazione_25000_35000"]
    return det


def ulteriore_detrazione_cuneo(r: float) -> float:
    c = P["irpef"]["ulteriore_detrazione_cuneo"]
    if r <= c["da"] or r > c["azzera_a"]:
        return 0.0
    if r <= c["pieno_fino"]:
        return c["importo"]
    return c["importo"] * (c["azzera_a"] - r) / (c["azzera_a"] - c["pieno_fino"])


def detrazione_pensione(r: float) -> float:
    return _detrazione_tre_fasce(r, P["irpef"]["detrazione_pensione"],
                                 "fino_8500", "tra_8500_28000", "tra_28000_50000", 8500)


def detrazione_autonomo(r: float) -> float:
    return _detrazione_tre_fasce(r, P["irpef"]["detrazione_autonomo_impresa_minore"],
                                 "fino_5500", "tra_5500_28000", "tra_28000_55000", 5500)


def irpef_e_addizionali(imponibile: float, detrazioni: float) -> tuple[float, float]:
    """Restituisce (IRPEF netta, addizionali). Le addizionali non sono dovute se l'IRPEF netta e' zero."""
    netta = max(0.0, irpef_lorda(imponibile) - detrazioni)
    st = P["irpef"]["sterilizzazione_oltre_200k"]
    if st["applica_senza_oneri"] and imponibile > st["soglia"]:
        netta += st["importo"]
    a = P["addizionali"]
    add = imponibile * (a["regionale"]["valore"] + a["comunale"]["valore"]) if netta > 0 else 0.0
    return netta, add


# ---------------------------------------------------------------- contributi
def massimale() -> float:
    return P["inps"]["massimale_post_1995"]["valore"]


def contributi_dipendente(ral: float) -> tuple[float, float]:
    d = P["inps"]["dipendente"]
    base = min(ral, massimale())
    lav = base * d["aliquota_lavoratore"] + max(0.0, base - d["soglia_aggiuntiva"]) * d["aliquota_aggiuntiva_lavoratore"]
    return lav, base * d["aliquota_datore_ivs"]


def contributi_artcom(reddito: float, gestione: str = "commercianti") -> float:
    g = P["inps"][gestione]
    base = min(max(reddito, g["minimale_reddito"]), massimale())
    c = min(base, g["soglia"]) * g["aliquota"] + max(0.0, base - g["soglia"]) * g["aliquota_oltre_soglia"]
    return max(c, g["contributo_minimo"])


def contributi_gs_professionista(reddito: float) -> float:
    return min(reddito, massimale()) * P["inps"]["gestione_separata"]["professionisti"]


def irap_societa(base: float, tipo: str) -> float:
    i = P["irap"]
    deduzione = 0.0
    for soglia, importo in i["deduzione_forfettaria"][tipo]:
        if base <= soglia:
            deduzione = importo
            break
    return max(0.0, base - deduzione) * i["aliquota"]


# ---------------------------------------------------------------- riga di risultato
def riga(gruppo, variante, reddito, imposte, contributi, contributi_datore=0.0, note=""):
    return {
        "gruppo": gruppo,
        "variante": variante,
        "reddito_lordo": reddito,
        "imposte": round(imposte, 2),
        "contributi": round(contributi, 2),
        "prelievo_totale": round(imposte + contributi, 2),
        "aliquota_effettiva_imposte": round(100 * imposte / reddito, 2),
        "aliquota_effettiva_totale": round(100 * (imposte + contributi) / reddito, 2),
        "contributi_a_carico_datore": round(contributi_datore, 2),
        "note": note,
    }


def eur(x: float) -> str:
    return f"{x:,.0f}".replace(",", ".")


# ---------------------------------------------------------------- gruppi
def gruppo_dipendente(r: float) -> list[dict]:
    lav, dat = contributi_dipendente(r)
    imp = r - lav
    det = detrazione_dipendente(imp) + ulteriore_detrazione_cuneo(imp)
    irpef, add = irpef_e_addizionali(imp, det)
    note = (f"IRPEF {eur(irpef)} (detrazioni {eur(det)}), addizionali {eur(add)}; "
            f"INPS lavoratore {eur(lav)}; INPS datore (IVS, a parte, non nel prelievo) {eur(dat)}")
    return [riga("1 Dipendente privato", "RAL", r, irpef + add, lav, dat, note)]


def gruppo_pensione(r: float) -> list[dict]:
    det = detrazione_pensione(r)
    irpef, add = irpef_e_addizionali(r, det)
    return [riga("2 Pensione", "pensione lorda", r, irpef + add, 0.0,
                 note=f"IRPEF {eur(irpef)} (detrazione {eur(det)}), addizionali {eur(add)}")]


def gruppo_forfettario(r: float) -> list[dict]:
    f = P["forfettario"]
    righe = []
    for variante, coeff, contr_fn in (
        ("professionista, gestione separata", f["coefficiente_professionisti"], contributi_gs_professionista),
        ("commercio, INPS commercianti", f["coefficiente_commercio"], lambda x: contributi_artcom(x, "commercianti")),
    ):
        ricavi = r / coeff
        if ricavi > f["limite_ricavi"]:
            continue  # regime non applicabile: ricavi oltre 85.000 euro
        contr = contr_fn(r)
        imposta = max(0.0, r - contr) * f["aliquota"]
        righe.append(riga("3 Forfettario 15%", variante, r, imposta, contr,
                          note=f"ricavi {eur(ricavi)} (coeff. {coeff:.0%}); sostitutiva 15% {eur(imposta)}; "
                               f"contributi deducibili {eur(contr)}; niente addizionali, niente IVA"))
    return righe


def gruppo_ordinario(r: float) -> list[dict]:
    righe = []
    for variante, contr in (
        ("professionista, gestione separata", contributi_gs_professionista(r)),
        ("impresa individuale, INPS commercianti", contributi_artcom(r, "commercianti")),
    ):
        imp = r - contr
        det = detrazione_autonomo(imp)
        irpef, add = irpef_e_addizionali(imp, det)
        righe.append(riga("4 Partita IVA ordinaria", variante, r, irpef + add, contr,
                          note=f"IRPEF {eur(irpef)} (detrazione {eur(det)}), addizionali {eur(add)}; "
                               f"contributi {eur(contr)}; IRAP non dovuta (persone fisiche esenti dal 2022)"))
    return righe


def gruppo_snc(r: float) -> list[dict]:
    n = P["snc"]["numero_soci"]
    irap = irap_societa(r * n, "societa_persone") / n
    contr = contributi_artcom(r, "commercianti")
    imp = r - contr
    irpef, add = irpef_e_addizionali(imp, 0.0)
    return [riga("5 Socio di SNC", f"{n} soci al 50%, INPS commercianti", r, irpef + add + irap, contr,
                 note=f"IRPEF {eur(irpef)}, addizionali {eur(add)}, quota IRAP della societa' {eur(irap)}; "
                      f"contributi {eur(contr)}")]


def srl_conti(utile: float, compenso: float) -> dict:
    """Conti di una SRL senza dipendenti con utile ante imposte e ante compenso = `utile`."""
    gs = P["inps"]["gestione_separata"]
    contr_tot = min(compenso, massimale()) * gs["amministratori"]
    contr_amm = contr_tot * gs["quota_carico_amministratore"]
    contr_soc = contr_tot - contr_amm
    irap = irap_societa(utile, "societa_capitali")      # compensi agli amministratori non deducibili IRAP
    base_ires = utile - compenso - contr_soc
    ires = max(0.0, base_ires) * P["ires"]["aliquota"]
    dividendo = utile - compenso - contr_soc - irap - ires
    return dict(contr_tot=contr_tot, contr_amm=contr_amm, contr_soc=contr_soc, irap=irap, ires=ires,
                base_ires=base_ires, dividendo=dividendo)


def srl_socio(utile: float, compenso: float) -> dict:
    c = srl_conti(utile, compenso)
    imp = compenso - c["contr_amm"]
    irpef, add = irpef_e_addizionali(imp, detrazione_dipendente(imp) if compenso > 0 else 0.0)
    rit = max(0.0, c["dividendo"]) * P["dividendi"]["ritenuta_persona_fisica"]
    c.update(irpef=irpef, add=add, ritenuta=rit,
             imposte=c["irap"] + c["ires"] + rit + irpef + add, contributi=c["contr_tot"])
    return c


def gruppo_srl(r: float) -> list[dict]:
    a = srl_socio(r, 0.0)
    righe = [riga("6 Socio di SRL", "tutto in dividendi", r, a["imposte"], 0.0,
                  note=f"IRAP {eur(a['irap'])}, IRES {eur(a['ires'])}, ritenuta 26% sul dividendo "
                       f"{eur(a['ritenuta'])}; nessun contributo")]
    passo = P["srl"]["passo_ricerca_compenso"]
    migliore, comp_m = None, 0.0
    compenso = 0.0
    while compenso <= r:
        c = srl_socio(r, compenso)
        if c["base_ires"] >= 0:
            tot = c["imposte"] + c["contributi"]
            if migliore is None or tot < migliore["imposte"] + migliore["contributi"] - 1e-9:
                migliore, comp_m = c, compenso
        compenso += passo
    b = migliore
    righe.append(riga("6 Socio di SRL", "compenso amministratore + dividendi (mix che paga meno)", r,
                      b["imposte"], b["contributi"],
                      note=f"compenso {eur(comp_m)}: IRPEF {eur(b['irpef'])}, addizionali {eur(b['add'])}; "
                           f"IRAP {eur(b['irap'])}, IRES {eur(b['ires'])}, ritenuta {eur(b['ritenuta'])}; "
                           f"gestione separata 35,03% {eur(b['contributi'])}"))
    return righe


def gruppo_holding(r: float) -> list[dict]:
    c = srl_conti(r, 0.0)
    d = c["dividendo"]
    ires_holding = d * P["dividendi"]["quota_imponibile_holding"] * P["ires"]["aliquota"]
    trattenuto = d - ires_holding
    base = c["irap"] + c["ires"] + ires_holding
    h = P["holding"]
    n, t = h["anni_prima_della_distribuzione"], h["tasso_sconto"]
    rit_nominale = trattenuto * P["dividendi"]["ritenuta_persona_fisica"]
    rit_attuale = rit_nominale / (1 + t) ** n
    comune = f"IRAP {eur(c['irap'])}, IRES {eur(c['ires'])}, IRES holding su 5% del dividendo {eur(ires_holding)}"
    return [
        riga("7 SRL tramite holding", "utili lasciati nella holding", r, base, 0.0,
             note=f"{comune}; restano nella holding {eur(trattenuto)} da reinvestire"),
        riga("7 SRL tramite holding", f"distribuisce dopo {n} anni (valore di oggi, sconto {t:.0%})", r,
             base + rit_attuale, 0.0,
             note=f"{comune}; ritenuta 26% fra {n} anni {eur(rit_nominale)}, oggi vale {eur(rit_attuale)}"),
        riga("7 SRL tramite holding", "quote passate agli eredi (nessuna imposta personale)", r, base, 0.0,
             note=f"{comune}; costo fiscale degli eredi = valore di successione, esenzione art. 3 c. 4-ter TUS"),
    ]


def gruppo_rendite(r: float) -> list[dict]:
    f = P["rendite_finanziarie"]
    bollo = r / f["rendimento_ipotetico"] * f["bollo_su_capitale"]
    return [
        riga("8 Rendite finanziarie", "azioni, fondi, obbligazioni 26%", r, r * f["aliquota_ordinaria"], 0.0,
             note="ritenuta o imposta sostitutiva 26%"),
        riga("8 Rendite finanziarie", "titoli di Stato 12,5%", r, r * f["aliquota_titoli_stato"], 0.0,
             note="imposta sostitutiva 12,5%"),
        riga("8 Rendite finanziarie", "26% + bollo 0,2% sul capitale (rendimento 4%)", r,
             r * f["aliquota_ordinaria"] + bollo, 0.0,
             note=f"capitale {eur(r / f['rendimento_ipotetico'])}, bollo {eur(bollo)}"),
    ]


def gruppo_affitti(r: float) -> list[dict]:
    f = P["affitti"]
    imp = r * f["quota_imponibile_irpef"]
    irpef, add = irpef_e_addizionali(imp, 0.0)
    return [
        riga("9 Affitti", "cedolare secca 21%", r, r * f["cedolare_ordinaria"], 0.0, note="IMU esclusa"),
        riga("9 Affitti", "cedolare secca 10% (canone concordato)", r, r * f["cedolare_concordato"], 0.0,
             note="IMU esclusa"),
        riga("9 Affitti", "IRPEF ordinaria", r, irpef + add, 0.0,
             note=f"imponibile 95% del canone; IRPEF {eur(irpef)}, addizionali {eur(add)}; IMU esclusa"),
    ]


GRUPPI = [gruppo_dipendente, gruppo_pensione, gruppo_forfettario, gruppo_ordinario, gruppo_snc,
          gruppo_srl, gruppo_holding, gruppo_rendite, gruppo_affitti]


def calcola_tutto() -> list[dict]:
    out = []
    for g in GRUPPI:
        for r in P["livelli_reddito"]:
            out.extend(g(float(r)))
    return out


# ---------------------------------------------------------------- casi di prova
def prove() -> None:
    def vicino(a, b, tol=0.6):
        assert abs(a - b) <= tol, (a, b)

    # 1. Dipendente, RAL 25.000: conto a mano con le regole 2026
    #    INPS 9,19% = 2.297,50; imponibile 22.702,50; IRPEF lorda 23% = 5.221,58
    #    detrazione art. 13 c.1 = 1.910 + 1.190 x (28.000-22.702,50)/13.000 = 2.394,95; cuneo 1.000
    #    IRPEF netta 1.826,63; addizionali 2,53% x 22.702,50 = 574,37
    lav, _ = contributi_dipendente(25000)
    vicino(lav, 2297.50)
    vicino(irpef_lorda(22702.50), 5221.58)
    vicino(detrazione_dipendente(22702.50), 2394.95)
    irpef, add = irpef_e_addizionali(22702.50, detrazione_dipendente(22702.50) + ulteriore_detrazione_cuneo(22702.50))
    vicino(irpef, 1826.63)
    vicino(add, 574.37)
    # 2. Il taglio della legge di bilancio 2026 vale al massimo 440 euro (2 punti su 22.000 euro)
    vicino(irpef_lorda(50000) - irpef_lorda(28000), 22000 * 0.33)
    vicino(irpef_lorda(60000), 28000 * 0.23 + 22000 * 0.33 + 10000 * 0.43)
    # 3. Detrazioni: continuita' alle soglie
    vicino(detrazione_dipendente(15000), 1955)
    vicino(detrazione_dipendente(28000.01), 1910 + 65, 0.01)  # con la maggiorazione 25-35 mila
    vicino(detrazione_pensione(8500.01), 1955, 0.01)
    vicino(detrazione_autonomo(55000), 0)
    # 4. Commercianti sul minimale: contributo fisso della circolare INPS 14/2026
    vicino(contributi_artcom(10000), 4611.64)
    # 5. Holding: dividendo alla holding tassato all'1,2% (5% x 24%)
    vicino(1000 * P["dividendi"]["quota_imponibile_holding"] * P["ires"]["aliquota"], 12.0)
    # 6. SRL, tutto dividendi, 1.000.000: IRAP 3,9% + IRES 24% + 26% sul resto = 46,64%
    a = srl_socio(1_000_000, 0)
    vicino(a["imposte"], 39000 + 240000 + 0.26 * (1_000_000 - 39000 - 240000))
    print("Casi di prova: tutti superati.")


def main() -> None:
    prove()
    if "--solo-prove" in sys.argv:
        return
    righe = calcola_tutto()
    with open(QUI / "risultati.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(righe[0].keys()))
        w.writeheader()
        w.writerows(righe)
    print(f"Scritte {len(righe)} righe in {QUI / 'risultati.csv'}")
    for x in righe:
        print(f"{x['gruppo'][:24]:24} {x['variante'][:42]:42} {x['reddito_lordo']:>10,.0f} "
              f"imp {x['aliquota_effettiva_imposte']:6.2f}%  tot {x['aliquota_effettiva_totale']:6.2f}%")


if __name__ == "__main__":
    main()
