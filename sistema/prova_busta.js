// Casi di prova del calcolatore della busta paga (docs/busta.js). Esecuzione: node sistema/prova_busta.js
// 1) Con le regole di oggi deve dare gli stessi numeri di analisi/chi_paga/risultati.csv (dipendente privato).
// 2) Casi costruiti a mano per somma esente, trattamento integrativo, detrazioni e misure del programma.
"use strict";
const fs = require("fs");
const path = require("path");
const B = require("../docs/busta.js");
const radice = path.join(__dirname, "..");
const testo = fs.readFileSync(path.join(radice, "docs", "data.js"), "utf8");
const D = JSON.parse(testo.slice(testo.indexOf("=") + 1).trim().replace(/;\s*$/, ""));
const Q = D.busta;
let errori = 0;
const vicino = (nome, a, b, tol = 1) => {
  const ok = Math.abs(a - b) <= tol;
  if (!ok) errori++;
  console.log(`${ok ? "ok " : "ERR"} ${nome}: ${a.toFixed(2)} (atteso ${b.toFixed(2)})`);
};

// 1) confronto con «Chi paga quanto»
const righe = fs.readFileSync(path.join(radice, "analisi", "chi_paga", "risultati.csv"), "utf8").split(/\r?\n/).filter((l) => l.startsWith("1 Dipendente privato"));
for (const l of righe) {
  const c = l.match(/^[^,]+,[^,]+,([\d.]+),([\d.]+),([\d.]+),/);
  const ral = +c[1], imposte = +c[2], contr = +c[3];
  const x = B.calcola(Q, { ral }, false);
  vicino(`RAL ${ral}: imposte`, x.irpef + x.addizionali, imposte);
  vicino(`RAL ${ral}: contributi`, x.inps, contr);
}

// 2) casi a mano
const P = Q.regole;
// 12.000 euro di RAL: reddito 12.000 - 9,19% = 10.897,20; somma esente 5,3% = 577,55; trattamento integrativo 1.200
let x = B.calcola(Q, { ral: 12000 }, false);
vicino("12.000: somma esente", x.se, 10897.2 * 0.053);
vicino("12.000: trattamento integrativo", x.ti, 1200);
vicino("12.000: IRPEF netta (2.506,36 - 1.955 = 551,36)", x.irpef, 10897.2 * 0.23 - 1955);
// 40.000 euro: spese sanitarie 1.129,11 => detrazione 190 oggi; con il programma piena (reddito sotto 50.000)
x = B.calcola(Q, { ral: 40000, sanitarie: 1129.11 }, false);
const y = B.calcola(Q, { ral: 40000, sanitarie: 1129.11 }, true, "Centrale");
vicino("40.000: detrazione sanitarie oggi", x.oneri.sanitarie, 190);
vicino("40.000: detrazione sanitarie con il programma", y.oneri.sanitarie, 190);
// 70.000 euro: reddito 70.000 - contributi; coefficiente (120.000 - r) / 70.000
const r70 = 70000 - B.contributi(P, 70000);
const z = B.calcola(Q, { ral: 70000, sanitarie: 1129.11 }, true, "Centrale");
vicino("70.000: detrazione sanitarie con il programma", z.oneri.sanitarie, 190 * (120000 - r70) / 70000);
const zc = B.calcola(Q, { ral: 70000, sanitarie: 1129.11, cronica: true }, true, "Centrale");
vicino("70.000: malattia cronica, detrazione piena", zc.oneri.sanitarie, 190);
// 70.000 euro e 5.000 di fondo pensione: oggi risparmio al 43% (2.150), con il programma al 33% (1.650): +500
const f = B.calcola(Q, { ral: 70000, fondo: 5000 }, true, "Centrale");
vicino("70.000: tetto al 33% sul fondo pensione", f.tettoFondo, 500);
// 30.000 euro e 5.000 di fondo pensione: nessun cambiamento (sotto 50.000)
vicino("30.000: fondo pensione invariato", B.calcola(Q, { ral: 30000, fondo: 5000 }, true, "Centrale").tettoFondo, 0);
// premi vita 530 => 100,70; veterinarie 550 => 79,97; sport 2 figli 500 => 79,80 (limite 420)
x = B.calcola(Q, { ral: 35000, premi: 600, veterinarie: 700, sport: 500, figli: 2 }, false);
vicino("premi vita e infortuni", x.oneri.premi, 100.7);
vicino("spese veterinarie", x.oneri.veterinarie, 0.19 * (550 - 129.11));
vicino("sport figli", x.oneri.sport, 79.8);
// dividendo centrale: (2,35 + 0,45) mld / 23.072.978 dipendenti
vicino("dividendo centrale per dipendente", B.calcola(Q, { ral: 30000 }, true, "Centrale").dividendo, 2.8e9 / 23072978);

console.log(errori ? `\n${errori} casi sbagliati` : "\nTutti i casi sono corretti");
process.exit(errori ? 1 : 0);
