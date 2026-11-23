/* Calcolatore «La tua busta paga con GovernAI»: regole 2026 per una lavoratrice o un lavoratore dipendente,
   e gli effetti a regime delle misure del programma. Nessun numero fiscale è scritto qui: arrivano da
   analisi/chi_paga/parametri.yaml e programma/busta_paga.yaml (esportati in data.js come D.busta).
   Usabile anche da Node per i casi di prova (sistema/prova_busta.js). */
(function (radice) {
  "use strict";

  function irpefLorda(P, imp) {
    let tot = 0, inf = 0;
    for (const [lim, aliq] of P.irpef.scaglioni.valore) {
      const sup = lim == null ? imp : Math.min(imp, lim);
      if (sup > inf) tot += (sup - inf) * aliq;
      if (lim == null || imp <= lim) break;
      inf = lim;
    }
    return tot;
  }
  function detLavoro(P, r) {
    const d = P.irpef.detrazione_lavoro_dipendente;
    let det;
    if (r <= 15000) det = d.fino_15000;
    else if (r <= d.tra_15000_28000.soglia) { const f = d.tra_15000_28000; det = f.base + f.variabile * (f.soglia - r) / f.ampiezza; }
    else if (r <= d.tra_28000_50000.soglia) { const f = d.tra_28000_50000; det = f.base * (f.soglia - r) / f.ampiezza; }
    else det = 0;
    if (r > 25000 && r <= 35000) det += d.maggiorazione_25000_35000;
    return det;
  }
  function ulterioreCuneo(P, r) {
    const c = P.irpef.ulteriore_detrazione_cuneo;
    if (r <= c.da || r > c.azzera_a) return 0;
    if (r <= c.pieno_fino) return c.importo;
    return c.importo * (c.azzera_a - r) / (c.azzera_a - c.pieno_fino);
  }
  function contributi(P, ral) {
    const d = P.inps.dipendente, base = Math.min(ral, P.inps.massimale_post_1995.valore);
    return base * d.aliquota_lavoratore + Math.max(0, base - d.soglia_aggiuntiva) * d.aliquota_aggiuntiva_lavoratore;
  }
  function sommaEsente(R, r) {
    const s = R.somma_esente;
    if (r > s.fino_a_reddito) return 0;
    for (const [lim, p] of s.fasce) if (r <= lim) return r * p;
    return 0;
  }

  // x: { ral, sanitarie, cronica, premi, veterinarie, sport, figli, fondo }; con: applica le misure del programma
  function calcola(B, x, con, scenario) {
    const P = B.regole, R = B.regole_2026, O = R.oneri_19, G = B.programma;
    const ral = Math.max(0, +x.ral || 0);
    const inps = contributi(P, ral);
    const r = Math.max(0, ral - inps);                 // reddito di lavoro dipendente (e complessivo)
    const ded = Math.min(Math.max(0, +x.fondo || 0), R.fondo_pensione.limite_deduzione);
    const coeffAlti = r > O.riduzione_da ? Math.max(0, (O.riduzione_a - r) / (O.riduzione_a - O.riduzione_da)) : 1;
    const m = Object.fromEntries((G.misure || []).map((q) => [q.id, q]));
    let coeffSan = 1;
    if (con && !x.cronica && m.SF06) coeffSan = r <= m.SF06.da ? 1 : r >= m.SF06.a ? 0 : (m.SF06.a - r) / (m.SF06.a - m.SF06.da);
    const oneri = {
      sanitarie: O.aliquota * Math.max(0, (+x.sanitarie || 0) - O.franchigia_sanitarie) * coeffSan,
      premi: con ? 0 : O.aliquota * Math.min(+x.premi || 0, O.limite_premi_vita_infortuni) * coeffAlti,
      veterinarie: con ? 0 : O.aliquota * Math.max(0, Math.min(+x.veterinarie || 0, O.limite_veterinarie) - O.franchigia_veterinarie) * coeffAlti,
      sport: con ? 0 : O.aliquota * Math.min(+x.sport || 0, O.limite_sport_per_figlio * Math.max(0, +x.figli || 0)) * coeffAlti,
    };
    const totOneri = oneri.sanitarie + oneri.premi + oneri.veterinarie + oneri.sport;
    const detL = detLavoro(P, r), ult = ulterioreCuneo(P, r);
    const netta = (imp) => Math.max(0, irpefLorda(P, imp) - detL - ult - totOneri);
    const imp = Math.max(0, r - ded);
    let irpef = netta(imp);
    let tettoFondo = 0;
    if (con && m.SF22 && ded > 0 && r > m.SF22.soglia) {
      const risparmio = netta(r) - irpef;                // quanto fa risparmiare oggi la deduzione
      tettoFondo = Math.max(0, risparmio - m.SF22.aliquota_max * ded);
      irpef += tettoFondo;
    }
    const a = P.addizionali;
    const addizionali = irpef > 0 ? imp * (a.regionale.valore + a.comunale.valore) : 0;
    const T = R.trattamento_integrativo;
    const ti = r <= T.fino_a_reddito && irpefLorda(P, imp) > detL - T.riduzione_capienza ? T.importo : 0;
    const se = sommaEsente(R, r);
    let dividendo = 0;
    if (con) {
      const s = (G.dividendo || []).find((d) => d.scenario === scenario) || (G.dividendo || [])[1] || { mld_09C11: 0, mld_09C12: 0 };
      dividendo = (s.mld_09C11 + s.mld_09C12) * 1e9 / G.dipendenti;
    }
    const netto = ral - inps - irpef - addizionali + ti + se + dividendo;
    return { ral, inps, reddito: r, deduzione: ded, imponibile: imp, irpef, addizionali, ti, se, dividendo, oneri, tettoFondo, netto };
  }

  const API = { calcola, irpefLorda, detLavoro, ulterioreCuneo, contributi, sommaEsente };
  if (typeof module === "object" && module.exports) module.exports = API; else radice.BUSTA = API;
})(typeof window !== "undefined" ? window : globalThis);
