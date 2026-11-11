/* GovernAI · interfaccia web. Legge window.GOVERNAI (data.js, generato da sistema/esporta_web.py).
   Design: design/04_design_system.md; template scelto con il confronto in design/confronto/. */
(function () {
  "use strict";
  const D = window.GOVERNAI;
  const main = document.getElementById("contenuto");
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const nf = (n, d = 2) => n == null || n === "" || Number.isNaN(+n) ? "—" : Number(n).toLocaleString("it-IT", { minimumFractionDigits: d, maximumFractionDigits: d });
  const MESI = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"];
  const MESI_LUNGHI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"];
  const dataBreve = (iso) => { const [a, m, g] = String(iso).slice(0, 10).split("-"); return g ? `${+g} ${MESI[+m - 1]} ${a}` : String(iso); };
  const dataLunga = (iso) => new Date(String(iso).slice(0, 10) + "T12:00").toLocaleDateString("it-IT", { day: "numeric", month: "long", year: "numeric" });
  const piano = (s) => String(s || "").replace(/\*\*|`/g, "").replace(/\[([^\]]+)\]\([^)]+\)/g, "$1").trim();
  const valoreBreve = (v) => { const m = String(v).match(/^(-?[\d.]+,\d+)\s*(.*)$/); if (!m) return v; const n = parseFloat(m[1].replace(/\./g, "").replace(",", ".")); return nf(n, 1) + (m[2] === "%" ? "%" : " " + m[2]); };
  const periodoBreve = (p) => { const m = String(p).match(/^(\d{4})-(\d{2})$/); if (m) return MESI[+m[2] - 1] + " " + m[1]; const q = String(p).match(/^(\d{4})-Q(\d)$/); return q ? ["I", "II", "III", "IV"][+q[2] - 1] + " trim " + q[1] : p; };
  const del_ = (iso) => (/^(8|11) /.test(dataBreve(iso)) ? "dell'" : "del ") + dataBreve(iso);
  const ACC = { a: "à", e: "è", i: "ì", o: "ò", u: "ù" };
  const tit = (s) => String(s || "").replace(/"/g, "").replace(/([aeiou])'(?=[\s,.;:)]|$)/g, (m, v) => ACC[v]);
  const breveEResto = (s, max = 200) => { const x = piano(s); if (x.length <= max + 60) return esc(x); const frasi = x.split(/(?<=[.;])\s+/); let b = ""; while (frasi.length && (b + frasi[0]).length <= max) b += (b ? " " : "") + frasi.shift(); if (!b) b = frasi.shift(); return esc(b) + (frasi.length ? ` <details class="leggi"><summary>Leggi tutto</summary>${esc(frasi.join(" "))}</details>` : ""); };
  const icona = (n) => `<i data-lucide="${n}" aria-hidden="true"></i>`;
  const ext = (url, testo) => `<a href="${esc(url)}" target="_blank" rel="noopener">${testo}<span class="vh"> (si apre in una nuova scheda)</span> ${icona("external-link")}</a>`;

  if (!D) {
    main.innerHTML = `<div class="avviso alto" role="alert"><div class="avviso-titolo">${icona("triangle-alert")}Non riusciamo a caricare i dati.</div>
      <p>Il sito legge <code>docs/data.js</code>: genera il file con <code>python sistema/esporta_web.py</code>.</p></div>`;
    return;
  }

  // ---------- vocabolari del design system ----------
  const CLASSE = {
    "robusta": ["favorevole", "shield-check", "Nucleo robusto"],
    "dipendente dai valori": ["info", "scale", "Dipende dai valori"],
    "in coda": ["", "clock", "In coda"],
    "sfavorevole": ["alto", "circle-arrow-down", "Sfavorevole"],
  };
  const ESITO_GIUR = {
    compatibile: ["favorevole", "circle-check", "Compatibile"],
    condizionato: ["attenzione", "circle-alert", "Condizionato"],
    richiede_notifica: ["attenzione", "circle-alert", "Richiede notifica"],
    incompatibile: ["critico", "octagon-x", "Incompatibile"],
  };
  const GRAVITA_GIUR = { compatibile: 0, condizionato: 1, richiede_notifica: 1, incompatibile: 3 };
  const AMBITO = { FIS: "Fiscale", COS: "Costituzionale", UE: "Europeo" };
  const ESITO_DEC = { adottata: ["favorevole", "check", "Adottata"], respinta: ["alto", "x", "Respinta"], rinviata: ["", "calendar-clock", "Rinviata"] };
  const DOSE = { PIENA: 3, ESSENZIALE: 2, PILOTA: 1, ZERO: 0 };
  const GRAVITA = { critica: ["critico", "octagon-x", "Critica"], alta: ["alto", "triangle-alert", "Alta"], media: ["attenzione", "circle-alert", "Media"], bassa: ["", "circle-dashed", "Bassa"], info: ["info", "info", "Info"] };

  const chip = ([cls, ic, testo], extra = "") => `<span class="chip ${cls} ${extra}">${icona(ic)}${esc(testo)}</span>`;
  const chipClasse = (c) => chip(CLASSE[c] || ["", "circle-dashed", c]);
  const misuratore = (v) => {
    if (!v) return `<span class="chip tratteggio">${icona("circle-dashed")}Non inclusa</span>`;
    const n = DOSE[v] ?? 0, nome = v.charAt(0) + v.slice(1).toLowerCase();
    return `<span class="misuratore" aria-label="Variante ${nome}, intensità ${n} su 3"><span aria-hidden="true">${nome}</span><span class="pallini" aria-hidden="true">${[1, 2, 3].map((i) => `<i class="${i <= n ? "pieno" : ""}"></i>`).join("")}</span></span>`;
  };
  // Badge di verifica: solo sulle cifre che vengono da fonti esterne o da stime (design/confronto/valutazione_P3.md)
  const BADGE = { verificato: ["favorevole", "badge-check", "Verificato"], stima: ["info", "calculator", "Stima GovernAI"], verificare: ["attenzione", "circle-help", "Da verificare"], provvisorio: ["neutro", "hourglass", "Provvisorio"] };
  const badge = (tipo, fonte, url = "") => { const [c, i, t] = BADGE[tipo]; return `<button type="button" class="badge ${c}" data-fonte="${esc(fonte)}" ${url ? `data-url="${esc(url)}"` : ""} aria-haspopup="dialog">${icona(i)}<span>${t}</span></button>`; };
  const STIMA = "Stima GovernAI: calcolata dal modello, non certificata dalla Ragioneria generale dello Stato (RGS). Fonte: registro delle coperture e ottimizzatore del programma.";
  const md = (t) => window.marked && window.DOMPurify ? DOMPurify.sanitize(marked.parse(t || "")) : `<p>${esc(t)}</p>`;
  const proposta = (id) => D.proposte.find((p) => p.id === id);
  const scenario = (id) => D.scenari.find((s) => s.id === id) || D.scenari[0];
  const momento = scenario("momento");
  const linkP = (id) => `#/programma/${encodeURIComponent(id)}`;
  const linkSeduta = (id) => `#/governo/sedute/${encodeURIComponent(id)}`;
  const codici = (s) => String(s || "").replace(/\b(\d{2}-[PC]\d{1,2})\b/g, (m) => proposta(m) ? `<a href="${linkP(m)}">${m}</a>` : m);
  const OGGI = String(D.generato).slice(0, 10);
  const traGiorni = (iso) => Math.round((new Date(iso + "T12:00") - new Date(OGGI + "T12:00")) / 864e5);
  const bannerSim = (tipo = "") => `<div class="banner-sim ${tipo}" role="note">${icona("flask-conical")}<span><strong>Governo ombra · simulazione:</strong> le decisioni non sono in vigore.</span></div>`;
  const schede = (voci, attiva) => `<nav class="schede" aria-label="Sezioni">${voci.map(([k, t, href, conta]) => `<a href="${href}" ${k === attiva ? 'aria-current="page"' : ""}>${esc(t)}${conta != null ? ` <span class="conta">${conta}</span>` : ""}</a>`).join("")}</nav>`;
  const vuoto = (testo) => `<p class="vuoto">${esc(testo)}</p>`;
  const repo = D.repo || "https://github.com/FabioDeLuca1977/governai";
  // Comunità su invito (comunita.js): il programma resta pubblico, la discussione è per gli iscritti
  const C = window.Comunita;
  if (C) C.init({ md, D, icone: () => icone() });

  // ---------- testi generati ----------
  function sezioni(testo) {
    const out = { _testa: "" };
    String(testo || "").split(/\n(?=## )/).forEach((blocco, i) => {
      if (i === 0 && !blocco.startsWith("## ")) { out._testa = blocco; return; }
      const nl = blocco.indexOf("\n");
      out[blocco.slice(3, nl < 0 ? undefined : nl).trim()] = nl < 0 ? "" : blocco.slice(nl + 1).trim();
    });
    return out;
  }
  function verbale(v) {
    const S = sezioni(v.testo);
    const dec = (S["Decisioni"] || "").split("\n").filter((r) => r.startsWith("| ") && !r.startsWith("| Proposta") && !r.startsWith("|---"))
      .map((r) => { const c = r.slice(2, -2).split(" | "); const id = c[0].split(" ")[0]; return { id, titolo: c[0].slice(id.length).trim(), variante: c[1], esito: c[2], regola: c[3], motivo: c.slice(4).join(" | ") }; });
    const deroghe = (S["Deroghe dall'esito del motore"] || "").split("\n").map((r) => r.match(/^- \*\*([^*]+)\*\*: (.*)/)).filter(Boolean).map((m) => ({ id: m[1], testo: m[2] }));
    const obiezioni = [];
    (S["Obiezioni dell'opposizione e risposte"] || "").split("\n").forEach((r) => {
      let m = r.match(/^- \*\*(.+?)\*\* — (.*)/);
      if (m) { obiezioni.push({ titolo: m[1], testo: m[2] }); return; }
      const u = obiezioni[obiezioni.length - 1];
      if (!u) return;
      if ((m = r.match(/^\s+- Prova: (.*)/))) u.prova = m[1];
      if ((m = r.match(/^\s+- Cosa le farebbe cambiare idea: (.*)/))) u.cambia = m[1];
      if ((m = r.match(/^\s+- Risposta del capo: (.*)/))) u.risposta = m[1];
    });
    const sotto = (t) => (t || "").split(/\n(?=### )/).filter((x) => x.startsWith("### ")).map((x) => { const nl = x.indexOf("\n"); return { titolo: x.slice(4, nl).trim(), testo: x.slice(nl + 1).trim() }; });
    const mandati = (S["Mandati"] || "").split("\n").map((r) => r.match(/^- (M\d+) — (.+?), entro il (\d{4}-\d{2}-\d{2}): (.*)/)).filter(Boolean).map((m) => ({ id: m[1], chi: m[2], scadenza: m[3], compito: m[4] }));
    const prev = (S["Mandati"] || "").match(/\*\*Previsioni registrate:\*\* (\d+)/);
    const dom = (S["Domanda posta al Consiglio"] || "").split("\n").map((r) => r.replace(/^> ?/, "")).join("\n");
    const domTitolo = (dom.match(/^# (.+)/m) || [])[1];
    const domanda = ((dom.match(/\*\*Domanda:\*\*\s*([^\n]+)/) || [])[1] || "").replace(/^(.*?\?).*$/, "$1") || undefined;
    const motivo = (S._testa.match(/\*\*Motivo della convocazione\.\*\* (.*)/) || [])[1] || "";
    const ver = (D.governo.verifiche || []).find((x) => x.seduta === v.seduta);
    return {
      id: v.seduta, data: v.seduta.slice(0, 10), S, dec, deroghe, obiezioni, mandati, previsioni: prev ? +prev[1] : null,
      pareri: sotto(S["Pareri degli esperti"]), ministri: sotto(S["Posizioni dei ministri"]),
      tipo: motivo.startsWith("Richiesta") ? "Seduta a richiesta" : "Seduta ordinaria",
      titolo: (ver && ver.titolo) || domTitolo || piano(motivo).replace(/\.$/, ""), domanda, dom, motivo, verifica: ver,
      rilievi: (S["Rilievi formali"] || "").split("\n").filter((r) => r.startsWith("- ")).length,
    };
  }
  const VERBALI = ((D.governo && D.governo.verbali) || []).map(verbale).sort((a, b) => b.id.localeCompare(a.id));

  // allerte attive: regole di sistema/config.yaml con il valore dell'indicatore
  const IND = Object.fromEntries((D.indicatori || []).map((i) => [i.id, i]));
  const ALLERTE = (D.regole || []).filter((r) => (D.allerte_attive || []).includes(r.id)).map((r) => ({ ...r, ind: IND[r.indicatore] || {} }));
  const gravAllerta = (r) => (r.sospendi || []).length || /valore/.test(r.condizione || "") ? GRAVITA.alta : GRAVITA.media;

  // scadenze europee da europa/scadenze.csv
  const breveUE = (t) => {
    let b = String(t || "").replace(/\s*\(Testo rilevante ai fini del SEE\)\s*/i, "").replace(/\s*\(rifusione\)/i, "");
    b = b.replace(/^.*?,\s*(?:del|dell[’']|dello)\s*\d{1,2}\s+\S+\s+\d{4},\s*/i, "");
    const pq = b.match(/per quanto (?:riguarda|concerne)\s+(.*)$/i);
    if (pq) b = pq[1];
    b = b.split(/,\s*(?:che (?:abroga|modifica)|e che)\s/)[0].replace(/,\s*$/, "");
    b = b.replace(/^(?:riguardante|relativ[ao]|concernente|recante|in materia di)\s+/i, "").replace(/^che\s+/i, "")
      .replace(/^(?:il|lo|la|i|gli|le|al|allo|alla|ai|agli|alle|sul|sullo|sulla|sui|sugli|sulle|un|una|uno)\s+|^(?:l|all|sull)[’']/i, "");
    b = b.charAt(0).toUpperCase() + b.slice(1);
    return b.length > 110 ? b.slice(0, 108).replace(/\s\S*$/, "") + "…" : b;
  };
  const attoUE = (t) => (String(t).match(/^(Direttiva|Regolamento|Decisione)[^,]*?\d{4}\/\d+/) || [String(t).slice(0, 40)])[0].replace(/ del Parlamento europeo e del Consiglio| del Consiglio/, "");
  const SCADENZE = ((D.europa && D.europa.scadenze) || []).map((x) => ({
    data: x.termine_recepimento, pr: x.priorita, breve: breveUE(x.titolo), atto: attoUE(x.titolo), titolo: x.titolo, celex: x.celex,
    stato: x.stato, infrazione: x.infrazione, url: x.url_eurlex || `https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX:${x.celex}`,
    proposte: String(x.proposte || "").split(",").map((s) => s.trim()).filter(Boolean), aree: String(x.aree || "").split(",").filter(Boolean),
  })).sort((a, b) => a.data.localeCompare(b.data));
  const FUTURE = SCADENZE.filter((s) => s.data >= OGGI);

  // ---------- componenti ----------
  function contatore(dec) {
    const n = (e) => dec.filter((d) => d.esito === e).length, a = n("adottata"), r = n("respinta"), v = n("rinviata"), t = dec.length || 1;
    return `<div class="contatore"><div class="barra" aria-hidden="true">
        <span style="width:${a / t * 100}%;background:var(--c-favorevole)"></span><span style="width:${r / t * 100}%;background:var(--c-alto)"></span><span style="width:${v / t * 100}%;background:var(--c-neutro)"></span></div>
      <div class="legenda"><span style="color:var(--c-favorevole)">${icona("circle-check")}<b>${a}</b> adottate</span><span style="color:var(--c-alto)">${icona("circle-x")}<b>${r}</b> respinte</span><span>${icona("clock")}<b>${v}</b> ${v === 1 ? "rinviata" : "rinviate"}</span></div></div>`;
  }
  function cardProposta(p, motivo = "", sc = momento) {
    const m = sc.misure[p.id];
    return `<a class="card card-proposta" href="${linkP(p.id)}">
      <div class="testa-card"><p class="etichetta">${esc(D.aree[p.area])} · ${esc(p.id)}</p></div>
      <h3 class="titolo-card">${esc(tit(p.titolo))}</h3>
      <div class="chips">${chipClasse(p.classe)}${p.linea_rossa ? chip(["critico", "octagon-x", "Linea rossa in alcune versioni"]) : ""}</div>
      <div class="riga-dati">${misuratore(m && m.variante)}${m ? `<span>${nf(m.costo)} mld/anno</span>` : ""}${motivo ? `<span>${esc(motivo)}</span>` : ""}</div>
    </a>`;
  }
  const voceIndice = (voci) => voci.map(([id, t]) => `<li><a href="#${id}" data-ancora>${esc(t)}</a></li>`).join("");
  const indiceMobile = (voci) => `<details class="indice-mobile"><summary>${icona("list")}In questa pagina</summary><ol>${voceIndice(voci)}</ol></details>`;
  const indiceLaterale = (voci, azioni) => `<aside class="indice" aria-label="In questa pagina"><p class="etichetta">In questa pagina</p><ol>${voceIndice(voci)}</ol><div class="azioni">${azioni}</div></aside>`;
  const linkErrore = () => `${repo}/issues/new?title=${encodeURIComponent("[Errore] " + document.title)}&body=${encodeURIComponent("Pagina: " + location.href + "\n\nChe cosa non torna:\n")}`;
  const azioniCondividi = () => `<button class="btn s" type="button" data-azione="copia">${icona("link-2")}<span>Copia link permanente</span></button>
    <a class="btn terziario s" href="${esc(linkErrore())}" target="_blank" rel="noopener">${icona("flag")}Segnala un errore<span class="vh"> (si apre in una nuova scheda)</span></a>`;

  function trend(i, campo = "delta") {
    const d = i[campo];
    if (d == null) return "";
    const buona = i.meglio === "su" ? d > 0 : i.meglio === "giu" ? d < 0 : null;
    const parola = d === 0 ? "stabile" : buona == null ? "" : buona ? "favorevole" : "sfavorevole";
    const cifre = Math.abs(d) < 0.1 && d !== 0 ? 2 : 1;
    return `<span class="trend ${d === 0 || buona == null ? "" : buona ? "buona" : "cattiva"}">${icona(d > 0 ? "arrow-up-right" : d < 0 ? "arrow-down-right" : "minus")}${d > 0 ? "+" : d < 0 ? "−" : ""}${nf(Math.abs(d), cifre)} ${parola}</span>`;
  }
  const valoreInd = (i) => nf(i.valore, i.id === "fecondita" ? 2 : 1);
  const unitaInd = (i) => ({ "%": "%", "% PIL": "% del PIL", pb: "punti base", indice: "2021 = 100", saldo: "saldo", "": "figli per donna" }[i.unita] ?? i.unita);
  const nomeInd = (i) => String(i.nome).replace(/\s*\((?:%|% annua|punti base|% PIL[^)]*|2021=100|saldo|figli per donna|% sul trimestre prec\.)\)/, "").replace(/\(HICP, % annua\)/, "(HICP)");
  function badgeInd(i) {
    const f = i.fonte || {};
    const testo = `${f.fonte || "Fonte ufficiale"} · dato ${periodoBreve(i.periodo)}${i.provvisorio ? ", provvisorio: può essere rivisto" : ""}. Scaricato ogni giorno dalla sentinella dei dati.`;
    return badge(i.provvisorio ? "provvisorio" : "verificato", testo, f.url || "");
  }
  function sparkline(i) {
    const s = i.serie;
    if (!s || !s.v || s.v.filter((x) => x != null).length < 2) return "";
    const v = s.v.filter((x) => x != null), min = Math.min(...v), max = Math.max(...v), span = max - min || 1, n = s.v.length;
    const pts = s.v.map((y, k) => y == null ? null : [k / (n - 1) * 200, 40 - ((y - min) / span) * 34]).filter(Boolean);
    const dd = pts.map((p, k) => (k ? "L" : "M") + p[0].toFixed(1) + " " + p[1].toFixed(1)).join(" ");
    const u = pts[pts.length - 1];
    return `<svg class="sparkline" viewBox="0 0 200 44" preserveAspectRatio="none" role="img" aria-label="Andamento da ${esc(periodoBreve(s.t[0]))} a ${esc(periodoBreve(s.t[n - 1]))}: minimo ${nf(min, 1)}, massimo ${nf(max, 1)}"><path d="${dd}" vector-effect="non-scaling-stroke"/><circle cx="${u[0]}" cy="${u[1]}" r="2.5"/></svg>`;
  }
  function cardIndicatore(i) {
    return `<article class="card indicatore">
      <div class="sinistra"><h3>${esc(nomeInd(i))}</h3><p class="nota" style="margin:0">${esc(periodoBreve(i.periodo))} · ${esc(unitaInd(i))}</p></div>
      <div class="destra"><div class="riga"><span class="numero">${valoreInd(i)}${i.unita.startsWith("%") ? "%" : ""}</span>${badgeInd(i)}</div>${trend(i)}</div>
      ${sparkline(i)}
      <p class="fonte">Fonte: ${i.fonte && i.fonte.url ? ext(i.fonte.url, esc(i.fonte.fonte)) : esc((i.fonte || {}).fonte || "—")}</p>
    </article>`;
  }
  function avvisoAllerta(r, conAzione = false) {
    const g = gravAllerta(r), i = r.ind;
    const [titolo, ...resto] = String(r.messaggio).split(": ");
    return `<div class="avviso ${g[0]}"><div class="avviso-titolo">${chip(g)}<span>${esc(titolo.replace(/\.$/, ""))}</span></div>
      ${i.valore != null ? `<p><strong>${esc(nomeInd(i))}: ${valoreInd(i)}${i.unita.startsWith("%") ? "%" : " " + esc(unitaInd(i))}</strong> · ${esc(periodoBreve(i.periodo))} ${trend(i)}</p>` : ""}
      ${resto.length ? `<p>${esc(resto.join(": ").replace(/^./, (x) => x.toUpperCase()))}</p>` : ""}
      ${conAzione && r.azione ? `<p><strong>Che cosa fa il programma:</strong> ${codici(esc(r.azione))}</p>` : ""}
      ${(r.priorita || []).length ? `<div class="mini-codici">Diventano prioritarie: ${r.priorita.map((c) => `<a href="${linkP(c)}">${c}</a>`).join("")}</div>` : ""}
      ${(r.sospendi || []).length ? `<div class="mini-codici">Sospesa: ${r.sospendi.map((c) => `<a href="${linkP(c)}">${c}</a>`).join("")}</div>` : ""}</div>`;
  }
  function rigaScadenza(s) {
    const t = traGiorni(s.data);
    return `<li><span class="data">${dataBreve(s.data).split(" ").slice(0, 2).join(" ")}<small>${t >= 0 ? `tra ${t} giorni` : `scaduta da ${-t} giorni`}</small></span>
      <span class="testo"><span class="chips">${chip(GRAVITA[s.pr] || GRAVITA.media)}<strong>${esc(s.breve)}</strong></span>
        <span class="nota">${s.url ? ext(s.url, esc(s.atto)) : esc(s.atto)}${s.celex ? ` · <span class="mono">CELEX ${esc(s.celex)}</span>` : ""} · ${esc(s.stato)}</span>
        ${s.proposte.length ? `<span class="mini-codici">Collegata a: ${s.proposte.map((c) => proposta(c) ? `<a href="${linkP(c)}">${c}</a>` : esc(c)).join("")}</span>` : ""}</span></li>`;
  }

  // ---------- Mappa dei ministeri (home) ----------
  const TIPO_REL = { sinergia: ["favorevole", "handshake", "Sinergia"], tensione: ["attenzione", "scale", "Tensione"], entrambe: ["", "arrow-left-right", "Sinergia e tensione"] };
  const MAPPA = D.mappa || {};
  const relazioniDi = (k) => (MAPPA.relazioni || []).filter((r) => r.aree.includes(k));
  function mappaMinisteri(perArea) {
    const aree = MAPPA.aree || {};
    if (!Object.keys(aree).length) return `<section class="sezione" aria-labelledby="t-temi">
        <div class="sezione-testa"><h2 id="t-temi">Le proposte per tema</h2><a href="#/programma">Tutte e ${D.proposte.length}</a></div>
        <div class="temi">${perArea.map(([k, nome, c]) => `<a href="#/programma?tema=${k}">${esc(nome)}<span>${c}</span></a>`).join("")}</div></section>`;
    const pos = {};
    perArea.forEach(([k], i) => { const a = (-90 + i * 360 / perArea.length) * Math.PI / 180; pos[k] = [50 + 39 * Math.cos(a), 50 + 39 * Math.sin(a)]; });
    const linee = (MAPPA.relazioni || []).filter((r) => pos[r.aree[0]] && pos[r.aree[1]]).map((r) => {
      const [[x1, y1], [x2, y2]] = r.aree.map((k) => pos[k]);
      return `<line class="rel-${esc(r.tipo)}" data-a="${r.aree[0]}" data-b="${r.aree[1]}" x1="${x1.toFixed(2)}" y1="${y1.toFixed(2)}" x2="${x2.toFixed(2)}" y2="${y2.toFixed(2)}"/>`;
    }).join("");
    const nodi = perArea.map(([k, nome, c]) => { const a = aree[k] || {}; return `<button type="button" class="nodo" data-ministero="${k}" aria-pressed="false" style="left:${pos[k][0].toFixed(2)}%;top:${pos[k][1].toFixed(2)}%"><span class="nodo-icona">${icona(a.icona || "landmark")}</span><span class="nodo-nome">${esc(a.breve || nome)}</span><span class="vh">: ${c} proposte, ${relazioniDi(k).length} collegamenti con altri ministeri</span></button>`; }).join("");
    return `<section class="sezione" aria-labelledby="t-mappa">
        <div class="sezione-testa"><h2 id="t-mappa">La mappa del governo</h2><a href="#/programma">Tutte le ${D.proposte.length} proposte</a></div>
        <p class="nota" style="margin-top:-8px">Nove ministeri, i temi di cui si occupano e dove lavorano insieme o si contendono le risorse. Scegli un ministero per approfondire.</p>
        <div class="mappa">
          <div class="mappa-rete" id="mappa-rete">
            <svg viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true" focusable="false">${linee}</svg>
            <a class="mappa-centro" href="#/governo">${icona("users-round")}<span>Consiglio dei ministri</span></a>
            ${nodi}
          </div>
          <div class="card mappa-scheda" id="mappa-scheda" aria-live="polite">${mappaScheda(null)}</div>
        </div>
      </section>`;
  }
  function mappaLegenda() {
    return `<ul class="mappa-legenda" aria-label="Legenda dei collegamenti">${Object.entries(TIPO_REL).map(([t, [, , testo]]) => `<li><svg viewBox="0 0 40 8" aria-hidden="true"><line class="rel-${t}" x1="2" y1="4" x2="38" y2="4"/></svg>${testo}</li>`).join("")}</ul>`;
  }
  function mappaScheda(k) {
    const aree = MAPPA.aree || {};
    if (!k) return `<p class="etichetta">Come leggere la mappa</p>
      <h3>Scegli un ministero</h3>
      <p>Ogni ministero mostra i temi di cui si occupa, le sue proposte e i collegamenti con gli altri ministeri, ricavati dai dossier ministeriali.</p>
      ${mappaLegenda()}
      <p class="nota">Le linee indicano dove due ministeri lavorano sugli stessi problemi (sinergia) o dove le loro scelte si limitano a vicenda, di solito per le risorse (tensione).</p>`;
    const a = aree[k] || {}, rel = relazioniDi(k), n = D.proposte.filter((p) => p.area === k).length;
    const altro = (r) => r.aree[0] === k ? r.aree[1] : r.aree[0];
    const ordine = { tensione: 0, entrambe: 1, sinergia: 2 };
    rel.sort((x, y) => (ordine[x.tipo] ?? 3) - (ordine[y.tipo] ?? 3) || altro(x).localeCompare(altro(y)));
    return `<p class="etichetta">${icona(a.icona || "landmark")} Ministero</p>
      <h3 tabindex="-1" id="mappa-titolo">${esc(D.aree[k])}</h3>
      ${a.domanda ? `<p>${esc(a.domanda)}</p>` : ""}
      ${(a.temi || []).length ? `<p class="etichetta">Di che cosa si occupa</p><ul class="mappa-temi">${a.temi.map((t) => `<li>${esc(t)}</li>`).join("")}</ul>` : ""}
      <div class="azioni"><a class="btn s primario" href="#/programma?tema=${k}">Le ${n} proposte ${icona("arrow-right")}</a>${a.dossier ? `<span class="btn s">${ext(repo + "/blob/main/" + a.dossier, "Il dossier completo")}</span>` : ""}</div>
      <p class="etichetta">Collegamenti con gli altri ministeri (${rel.length})</p>
      ${rel.length ? `<ul class="mappa-rel">${rel.map((r) => { const o = altro(r), t = TIPO_REL[r.tipo] || TIPO_REL.entrambe; return `<li>
        <div class="mappa-rel-testa">${chip(t)}<button type="button" class="mappa-vai" data-ministero="${o}">${icona((aree[o] || {}).icona || "landmark")}${esc((aree[o] || {}).breve || D.aree[o])}<span class="vh"> (apri questo ministero)</span></button></div>
        <strong>${esc(r.tema)}</strong>
        ${r.spiegazione ? `<p>${esc(r.spiegazione)}</p>` : ""}
        ${(r.proposte || []).length ? `<div class="mini-codici">Proposte: ${r.proposte.map((c) => proposta(c) ? `<a href="${linkP(c)}" title="${esc(proposta(c).titolo)}">${c}</a>` : esc(c)).join("")}</div>` : ""}</li>`; }).join("")}</ul>` : `<p class="nota">Nessun collegamento indicato nei dossier.</p>`}
      ${mappaLegenda()}`;
  }
  function mappaSeleziona(k, dalPannello) {
    const rete = $("#mappa-rete"), scheda = $("#mappa-scheda");
    if (!rete || !scheda) return;
    const gia = rete.dataset.sel === k;
    const sel = gia ? "" : k;
    rete.dataset.sel = sel;
    const vicini = new Set(sel ? relazioniDi(sel).flatMap((r) => r.aree) : []);
    $$(".nodo", rete).forEach((b) => { b.setAttribute("aria-pressed", b.dataset.ministero === sel); b.classList.toggle("vicino", !!sel && b.dataset.ministero !== sel && vicini.has(b.dataset.ministero)); b.classList.toggle("lontano", !!sel && !vicini.has(b.dataset.ministero) && b.dataset.ministero !== sel); });
    $$(":scope > svg > line", rete).forEach((l) => { const on = sel && (l.dataset.a === sel || l.dataset.b === sel); l.classList.toggle("attiva", !!on); l.classList.toggle("spenta", !!sel && !on); });
    scheda.innerHTML = mappaScheda(sel || null);
    icone();
    if (dalPannello && sel) { $("#mappa-titolo").focus({ preventScroll: true }); if (innerWidth < 900) scheda.scrollIntoView({ block: "start", behavior: "smooth" }); }
    else if (sel && innerWidth < 900) scheda.scrollIntoView({ block: "nearest", behavior: "smooth" });
  }

  // ---------- Oggi ----------
  function home() {
    const n = D.numeri || {};
    const nucleo = D.proposte.filter((p) => p.classe === "robusta");
    const coperto = nucleo.filter((p) => momento.misure[p.id] && ["PIENA", "ESSENZIALE"].includes(momento.misure[p.id].variante)).length;
    const integra = D.integrita && !D.integrita.errori.length;
    const ult = VERBALI[0];
    const mandato = (D.governo.mandati || []).filter((m) => m.stato === "aperto" && m.scadenza >= OGGI).sort((a, b) => a.scadenza.localeCompare(b.scadenza))[0];
    const scad = FUTURE.filter((s) => ["critica", "alta"].includes(s.pr)).slice(0, 4).map((s) => ({ ...s }));
    if (mandato) scad.push({ data: mandato.scadenza, pr: "media", breve: `Mandato ${mandato.id} al ministro: ${D.aree[mandato.area] || mandato.area}`, atto: piano(mandato.compito).slice(0, 120) + "…", stato: "mandato aperto del governo ombra", proposte: (mandato.compito.match(/\b\d{2}-[PC]\d{1,2}\b/g) || []).slice(0, 3), celex: "", url: "" });
    scad.sort((a, b) => a.data.localeCompare(b.data));
    const perArea = Object.keys(D.aree).map((k) => [k, D.aree[k], D.proposte.filter((p) => p.area === k).length]);
    const solide = [...nucleo].sort((a, b) => b.p_prima_meta - a.p_prima_meta).slice(0, 6);
    return `
      <section class="hero" aria-labelledby="titolo-home">
        <div>
          <p class="etichetta sopratitolo">Un programma di governo aperto, basato su dati e valori dichiarati</p>
          <h1 id="titolo-home">Governare con i dati,<br>scegliere con i valori.</h1>
          <p class="risposta">${n.proposte} proposte valutate su ${n.valori} valori, finanziate senza deficit e controllate su Costituzione e regole europee. <span class="firma">L'AI propone e verifica. Le persone decidono.</span></p>
          <div class="azioni"><a class="btn primario" href="#/programma/una-pagina">Il programma in una pagina ${icona("arrow-right")}</a><a class="btn" href="#/programma/sintesi">Le idee in 10 minuti</a><a class="btn terziario" href="#/metodo">Come funziona</a></div>
        </div>
        <div class="oggi-box" aria-label="Oggi in breve">
          <p class="etichetta">Oggi, ${dataLunga(D.generato)}</p>
          <ul>
            <li>${icona("bell-ring")}<a href="#/dati/allerte">${ALLERTE.length ? chip(["alto", "triangle-alert", `${ALLERTE.length} allerte attive`]) : chip(["favorevole", "circle-check", "Nessuna allerta"])}</a></li>
            ${ult ? `<li>${icona("users-round")}<span>Ultima seduta: <a href="${linkSeduta(ult.id)}">${ult.data === OGGI ? "oggi" : dataBreve(ult.data)}</a></span></li>` : ""}
            <li>${icona("link-2")}<a href="#/controlli/integrita">${integra ? chip(["favorevole", "circle-check", `Catena integra · ${D.integrita.anelli} anelli`]) : chip(["critico", "octagon-x", "Catena da verificare"])}</a></li>
          </ul>
        </div>
      </section>

      <section class="sezione" aria-label="Il giorno in quattro numeri" style="margin-top:32px">
        <div class="griglia g2 g4-d">
          <div class="card kpi"><p class="etichetta">Programma del momento</p><p class="numero">${nf(momento.spesa)}<small>mld/anno</small></p><p class="nota">senza deficit</p>${badge("stima", STIMA)}</div>
          <div class="card kpi"><p class="etichetta">Misure incluse</p><p class="numero">${Object.keys(momento.misure).length}<small>su ${D.proposte.length}</small></p><p class="nota">nucleo robusto finanziato: ${coperto} su ${nucleo.length}</p></div>
          <div class="card kpi"><p class="etichetta">Cifre verificate</p><p class="numero">${n.cifre_verificate}</p><p class="nota">controllate una per una su fonte primaria</p></div>
          <div class="card kpi"><p class="etichetta">Serie di dati</p><p class="numero">${n.serie}</p><p class="nota">aggiornate ogni giorno da fonti ufficiali</p></div>
        </div>
      </section>

      ${mappaMinisteri(perArea)}

      <div class="griglia g2-d sezione">
        <section aria-labelledby="t-allerte">
          <div class="sezione-testa"><h2 id="t-allerte">Allerte attive (${ALLERTE.length})</h2><a href="#/dati/allerte">Tutte</a></div>
          ${ALLERTE.length ? ALLERTE.map((r) => avvisoAllerta(r)).join("") : `<div class="avviso favorevole"><div class="avviso-titolo">${icona("circle-check")}Nessuna allerta attiva: gli indicatori sono nelle soglie.</div></div>`}
        </section>
        <section aria-labelledby="t-seduta">
          <div class="sezione-testa"><h2 id="t-seduta">Ultima seduta del Consiglio</h2><a href="#/governo">Tutte</a></div>
          ${ult ? `<div class="card seduta-card">
            ${bannerSim("piccolo")}
            <p class="etichetta">${dataBreve(ult.data)} · ${esc(ult.tipo)}</p>
            <h3>${esc(ult.titolo)}</h3>
            ${contatore(ult.dec)}
            <p class="nota">${ult.dec.length} decisioni · ${ult.deroghe.length} deroghe dichiarate · ${ult.obiezioni.length} obiezioni dell'opposizione leale${ult.previsioni ? ` · ${ult.previsioni} previsioni registrate` : ""} · ${ult.mandati.length} mandati</p>
            <a class="btn" href="${linkSeduta(ult.id)}">Leggi il verbale ${icona("arrow-right")}</a>
          </div>` : vuoto("Il Consiglio non si è ancora riunito.")}
        </section>
      </div>

      <section class="sezione" aria-labelledby="t-scadenze">
        <div class="sezione-testa"><h2 id="t-scadenze">Prossime scadenze</h2><a href="#/controlli/europa">Tutte</a></div>
        <div class="card" style="padding-top:4px;padding-bottom:4px"><ul class="scadenze">${scad.map(rigaScadenza).join("")}</ul></div>
      </section>


      <section class="sezione" aria-labelledby="t-solide">
        <div class="sezione-testa"><h2 id="t-solide">Il nucleo robusto: le più solide</h2><a href="#/programma?classe=robusta">Tutte e ${nucleo.length}</a></div>
        <p class="nota" style="margin-top:-8px">Restano nella prima metà della classifica con quasi ogni combinazione di pesi tra i valori.</p>
        <div class="proposte-lista">${solide.map((p) => cardProposta(p, `prima metà nel ${Math.round(p.p_prima_meta * 100)}% dei casi`)).join("")}</div>
      </section>

      <section class="sezione" aria-labelledby="t-fiducia">
        <div class="sezione-testa"><h2 id="t-fiducia">Fiducia verificabile</h2><a href="#/metodo">Metodo</a></div>
        <div class="fiducia">
          <div class="card">${icona("link-2")}<div><h3>Catena ${integra ? "integra" : "da verificare"}</h3><p>${D.integrita.anelli} anelli di impronte crittografiche: una modifica nascosta a dati, regole o risultati si vede subito.</p></div></div>
          <div class="card">${icona("octagon-x")}<div><h3>Linee rosse automatiche</h3><p>Le proposte che violano diritti o scaricano costi sulle persone con redditi bassi o in condizioni di fragilità sono escluse da regole fisse.</p></div></div>
          <div class="card">${icona("repeat")}<div><h3>Tutto riproducibile</h3><p>Codice, dati, punteggi e regole sono pubblici: chiunque può rifare il calcolo.</p></div></div>
        </div>
      </section>

      <section class="sezione partecipa-box" aria-labelledby="t-partecipa">
        <div><h2 id="t-partecipa">Vuoi ragionarci insieme?</h2><p>Il programma è aperto a tutti. Nella comunità, su invito, si discutono le proposte con altre persone e con l'AI: qui nessuno decide, si prendono appunti e si migliorano le idee.</p></div>
        <div class="azioni"><a class="btn primario" href="#/comunita">${icona("messages-square")}Entra nella comunità</a><a class="btn" href="#/partecipa">Altri modi di partecipare</a></div>
      </section>`;
  }

  // ---------- Programma ----------
  const schedeProgramma = (k) => `<h1>Programma</h1>${schede([["una-pagina", "In una pagina", "#/programma/una-pagina"], ["sintesi", "In sintesi", "#/programma/sintesi"], ["equita", "Equità", "#/programma/equita"], ["proposte", "Proposte", "#/programma", D.proposte.length], ["coperture", "Come si paga", "#/programma/coperture"], ["valori", "I tuoi valori", "#/programma/valori"], ["confronti", "Confronti", "#/programma/confronti"]], k)}`;

  function elenco(params) {
    const sc = scenario(params.get("scenario") || "momento");
    const nucleo = D.proposte.filter((p) => p.classe === "robusta");
    const coperto = nucleo.filter((p) => sc.misure[p.id] && ["PIENA", "ESSENZIALE"].includes(sc.misure[p.id].variante)).length;
    return `${schedeProgramma("proposte")}
      <p class="risposta">Nel <strong>${esc(sc.nome.toLowerCase())}</strong> entrano ${Object.keys(sc.misure).length} misure su ${D.proposte.length}, per ${nf(sc.spesa)} mld l'anno senza deficit ${badge("stima", STIMA)}. Il nucleo robusto è finanziato per ${coperto} su ${nucleo.length}.</p>
      <div class="segmenti" role="group" aria-label="Scenario">${D.scenari.map((x) => `<button type="button" data-scenario="${x.id}" aria-pressed="${x.id === sc.id}" title="${esc(x.descrizione)}">${esc(x.nome)}</button>`).join("")}</div>
      <p class="nota" style="margin-top:8px">${esc(sc.descrizione)}.</p>
      <form class="filtri-barra" role="search" onsubmit="return false">
        <label class="campo largo">Cerca<input type="search" id="f-cerca" value="${esc(params.get("q") || "")}" placeholder="Parola o codice, es. asili, 01-P3"></label>
        <label class="campo">Tema<select id="f-tema"><option value="">Tutti i temi</option>${Object.entries(D.aree).map(([k, v]) => `<option value="${k}" ${k === params.get("tema") ? "selected" : ""}>${esc(v)}</option>`).join("")}</select></label>
        <label class="campo">Classe<select id="f-classe"><option value="">Tutte le classi</option>${Object.entries(CLASSE).map(([k, v]) => `<option value="${esc(k)}" ${k === params.get("classe") ? "selected" : ""}>${esc(v[2])}</option>`).join("")}</select></label>
        <label class="spunta"><input type="checkbox" id="f-incluse" ${params.get("incluse") ? "checked" : ""}>Solo incluse</label>
      </form>
      <p class="nota" id="f-conta" role="status" aria-live="polite"></p>
      <div class="tabella-box"><table class="tabella a-card"><thead><tr><th>Proposta</th><th>Classe</th><th>Variante</th><th class="num">mld/anno</th><th>Robustezza</th><th>Controlli</th></tr></thead><tbody id="f-corpo"></tbody></table></div>`;
  }
  function aggiornaElenco() {
    const q = ($("#f-cerca").value || "").trim().toLowerCase(), tema = $("#f-tema").value, classe = $("#f-classe").value, incl = $("#f-incluse").checked;
    const sc = scenario(new URLSearchParams(location.hash.split("?")[1] || "").get("scenario") || "momento");
    const righe = D.proposte.filter((p) => (!tema || p.area === tema) && (!classe || p.classe === classe) && (!incl || sc.misure[p.id])
      && (!q || (p.id + " " + p.titolo + " " + D.aree[p.area]).toLowerCase().includes(q)));
    let html = "", area = null;
    for (const p of righe) {
      if (p.area !== area) { area = p.area; html += `<tr class="gruppo"><td colspan="6">${esc(D.aree[area])}</td></tr>`; }
      const m = sc.misure[p.id];
      const g = (p.giuridico || []).filter((r) => r.tipo === "proposta" || (m && r.id === `${p.id}:${m.variante}`));
      const peggiore = g.reduce((a, r) => (GRAVITA_GIUR[r.esito] ?? 0) > (GRAVITA_GIUR[a] ?? -1) ? r.esito : a, null);
      html += `<tr class="${m ? "" : "esclusa"}"><td class="principale"><a class="riga" href="${linkP(p.id)}">${esc(tit(p.titolo))}</a> <span class="nota mono">${esc(p.id)}</span>${p.linea_rossa ? " " + chip(["critico", "octagon-x", "Linea rossa in alcune versioni"]) : ""}</td>
        <td data-etichetta="Classe">${chipClasse(p.classe)}</td><td data-etichetta="Variante">${misuratore(m && m.variante)}</td>
        <td class="num" data-etichetta="mld/anno">${m ? nf(m.costo) : "—"}</td>
        <td data-etichetta="Robustezza">${m ? `<span class="robustezza" aria-hidden="true"><span style="width:${Math.round(m.robustezza * 100)}%"></span></span>${Math.round(m.robustezza * 100)}%` : "—"}</td>
        <td data-etichetta="Controlli">${peggiore ? chip(ESITO_GIUR[peggiore]) : chip(["", "circle-dashed", "Non valutato"])}</td></tr>`;
    }
    $("#f-corpo").innerHTML = html || `<tr><td colspan="6" class="vuoto">Nessuna proposta con questi filtri.</td></tr>`;
    $("#f-conta").textContent = `${righe.length} proposte mostrate`;
    const pr = new URLSearchParams();
    if (q) pr.set("q", q); if (tema) pr.set("tema", tema); if (classe) pr.set("classe", classe); if (incl) pr.set("incluse", "1"); if (sc.id !== "momento") pr.set("scenario", sc.id);
    history.replaceState(null, "", "#/programma" + (pr.toString() ? "?" + pr : ""));
    icone();
  }

  function schedaProposta(id) {
    const p = proposta(id);
    if (!p) return nonTrovato(`Nessuna proposta con codice «${id}».`);
    const m = momento.misure[p.id];
    const S = p.scheda || "";
    const para = (etichetta) => { const r = S.match(new RegExp("\\*\\*" + etichetta + "\\.?\\*\\*\\.?\\s*([^\\n]+)")); return r ? r[1] : ""; };
    const problema = para("Problema in un dato"), soluzione = para("Soluzione");
    const grande = (problema.match(/\*\*([^*]+)\*\*/) || [])[1];
    const fonteProb = (problema.match(/\(([^()]*(?:\([^()]*\)[^()]*)*)\)[^(]*$/) || [])[1];
    const titoloLungo = (S.match(/^## [^—]+— (.+)$/m) || [])[1];
    let dec = null, seduta = null, deroga = null;
    for (const v of VERBALI) { const d = v.dec.find((x) => x.id === p.id); if (d) { dec = d; seduta = v; deroga = v.deroghe.find((x) => x.id === p.id); break; } }
    const mandati = (D.governo.mandati || []).filter((x) => x.stato === "aperto" && x.compito.includes(p.id));
    const obiettivi = (D.obiettivi || []).filter((o) => o.proposta === p.id);
    const scadenze = SCADENZE.filter((s) => s.proposte.includes(p.id));
    const medie = p.punteggi ? D.valori.map((v, j) => ({ nome: v.nome, id: v.id, m: p.punteggi[j].reduce((a, b) => a + b, 0) / 3 })) : [];
    const nonZero = medie.filter((x) => Math.abs(x.m) >= 0.05).sort((a, b) => b.m - a.m), zero = medie.filter((x) => Math.abs(x.m) < 0.05);
    const giur = p.giuridico || [];
    const peggiore = giur.reduce((a, r) => (GRAVITA_GIUR[r.esito] ?? 0) > (GRAVITA_GIUR[a] ?? -1) ? r.esito : a, null);
    const voci = [["in-breve", "In breve"], ["valori", "Effetto sui valori"], ["varianti", "Varianti"], ["controlli", "Controlli"], ["obiettivi", "Obiettivi"], ["governo", "Governo ombra"], ["testo", "Testo completo"], ["fonti", "Fonti e metodo"]];
    const esitoDec = dec ? (deroga ? ["attenzione", "git-branch", "Adottata con deroga"] : ESITO_DEC[dec.esito] || ["", "circle-dashed", dec.esito]) : null;
    const collegati = [
      ...scadenze.map((s) => `<li>${icona("landmark")}<a href="#/controlli/europa">${esc(s.atto)}</a> <span class="nota">scadenza UE ${dataBreve(s.data)}</span></li>`),
      ...mandati.map((x) => `<li>${icona("clipboard-check")}<a href="${linkSeduta(VERBALI.find((v) => v.mandati.some((y) => y.id === x.id))?.id || "")}">Mandato ${x.id}</a> <span class="nota">entro il ${dataBreve(x.scadenza)}</span></li>`),
      ...(seduta ? [`<li>${icona("users-round")}<a href="${linkSeduta(seduta.id)}">${esc(seduta.titolo)}</a> <span class="nota">seduta ${del_(seduta.data)}</span></li>`] : []),
      ...ALLERTE.filter((r) => (r.priorita || []).includes(p.id) || (r.sospendi || []).includes(p.id)).map((r) => `<li>${icona("bell-ring")}<a href="#/dati/allerte">${esc(String(r.messaggio).split(":")[0])}</a></li>`),
    ].slice(0, 6);

    return `
      <nav class="briciole" aria-label="Briciole di pane"><a href="#/programma">Programma</a><span aria-hidden="true">›</span><a href="#/programma?tema=${p.area}">${esc(D.aree[p.area])}</a><span aria-hidden="true">›</span><span aria-current="page">${esc(p.id)}</span></nav>
      <div class="con-indice">
        <article>
          <header class="intestazione">
            <p class="etichetta">${esc(D.aree[p.area])} · ${esc(p.id)}</p>
            <h1>${esc(tit(p.titolo))}</h1>
            <div class="chips">${chipClasse(p.classe)}${p.linea_rossa ? chip(["critico", "octagon-x", "Linea rossa in alcune versioni"]) : ""}${peggiore ? chip(ESITO_GIUR[peggiore]) : ""}</div>
            <div class="stato">Nel programma del momento: ${misuratore(m && m.variante)}${m ? `<span>· ${nf(m.costo)} mld/anno · robustezza ${Math.round(m.robustezza * 100)}%</span>` : `<span>· non inclusa</span>`}</div>
            ${indiceMobile(voci)}
          </header>
          ${p.linea_rossa ? `<div class="avviso critico" role="alert"><div class="avviso-titolo">${icona("octagon-x")}Linea rossa in alcune versioni</div><p>Almeno una versione di questa proposta supera una linea rossa della Carta dei valori ed è esclusa in automatico. Le altre versioni restano possibili: vedi le varianti e il programma.</p></div>` : ""}

          <section class="card in-breve blocco" id="in-breve" aria-labelledby="h-breve" style="margin-top:0">
            <h2 id="h-breve" class="vh">In breve</h2>
            <h3>Il problema in un dato</h3>
            ${grande ? `<p class="dato-grande">${esc(grande)}</p>` : ""}
            <p class="testo-lettura">${esc(piano(problema))} ${badge(fonteProb ? "verificato" : "verificare", fonteProb ? piano(fonteProb) : "La fonte non è indicata nel testo della scheda.")}</p>
            <h3>La soluzione</h3>
            <p class="testo-lettura">${esc(piano(soluzione)) || esc(titoloLungo || "")}</p>
            <h3>Costo e chi paga</h3>
            <p>${m ? `<strong>${nf(m.costo)} mld/anno</strong> nella variante ${esc(m.variante.toLowerCase())}` : `Costo pieno ${nf(p.costo_pieno)} mld/anno; non inclusa nel programma del momento`} ${badge("stima", STIMA)}</p>
            <h3>Il governo ombra</h3>
            ${dec ? `${bannerSim("piccolo")}<p>${chip(esitoDec)} in variante ${esc(String(dec.variante).toLowerCase())} nella seduta <a href="${linkSeduta(seduta.id)}">«${esc(seduta.titolo)}»</a> (${dataBreve(seduta.data)}).</p>
              ${deroga ? `<p class="nota">${codici(esc(piano(deroga.testo)))}</p>` : ""}
              ${mandati.length ? `<p>${mandati.map((x) => `Mandato <strong class="mono">${x.id}</strong> entro il ${dataBreve(x.scadenza)}`).join(" · ")}</p>` : ""}`
              : `<p class="nota">Non ancora all'ordine del giorno del Consiglio.</p>`}
          </section>

          <section class="blocco" id="valori" aria-labelledby="h-valori">
            <h2 id="h-valori">Effetto sui 10 valori <small>mediana del panel indipendente, media di breve, medio e lungo periodo, da −3 a +3</small></h2>
            ${medie.length ? `<div class="valori" role="img" aria-label="Effetto sui valori: ${nonZero.map((x) => `${x.nome} ${x.m > 0 ? "più" : "meno"} ${nf(Math.abs(x.m), 1)}`).join("; ")}${zero.length ? `; ${zero.length} valori a zero` : ""}.">
                <span aria-hidden="true"></span><div class="asse-testa" aria-hidden="true"><span>−3 peggiora</span><span>0</span><span>migliora +3</span></div><span aria-hidden="true"></span>
                ${nonZero.map((x) => `<span>${esc(x.nome)}</span><div class="traccia" title="breve, medio, lungo: ${p.punteggi[D.valori.findIndex((v) => v.id === x.id)].join(", ")}"><span class="${x.m >= 0 ? "pos" : "neg"}" style="width:${Math.abs(x.m) / 3 * 50}%"></span></div><span class="num">${x.m > 0 ? "+" : "−"}${nf(Math.abs(x.m), 1)}</span>`).join("")}
                ${zero.length ? `<p class="zero">A zero: ${zero.map((x) => esc(x.nome)).join(", ")}.</p>` : ""}
              </div>
              <p class="nota">Prima metà della classifica nel ${Math.round(p.p_prima_meta * 100)}% delle combinazioni di pesi; posizione tra ${p.rango[0]}ª e ${p.rango[1]}ª.${p.trainanti ? ` Sale se si dà più peso a: ${esc(p.trainanti)}.` : ""} <a href="#/programma/valori">Prova i tuoi pesi</a></p>`
              : vuoto("Il panel non ha ancora valutato questa proposta.")}
          </section>

          <section class="blocco" id="varianti" aria-labelledby="h-varianti">
            <h2 id="h-varianti">Varianti <small>la dose della misura, non un giudizio · costi: stime GovernAI</small></h2>
            <div class="varianti">${p.varianti.map((v) => `<div class="variante ${m && m.variante === v.variante ? "scelta" : ""}">
              <div class="chips">${misuratore(v.variante)} ${m && m.variante === v.variante ? chip(["info", "check", "Nel programma"]) : ""}</div>
              <p class="costo">${nf(v.costo)} mld/anno</p><p>${esc(v.descrizione)}</p><p class="nota">Strumento: ${esc(v.strumento || "—")}</p></div>`).join("")}</div>
          </section>

          <section class="blocco" id="controlli" aria-labelledby="h-controlli">
            <h2 id="h-controlli">Controlli <small>fiscale, costituzionale, europeo</small></h2>
            ${giur.length ? `<div class="card" style="padding-top:4px;padding-bottom:4px">${giur.map((r) => `<details class="controllo">
                <summary><span class="ambito">${esc(AMBITO[r.ambito] || r.ambito)}${r.tipo === "variante" ? ` · variante ${esc((r.id.split(":")[1] || "").toLowerCase())}` : ""}<small>${esc(String(r.norme).slice(0, 90))}${String(r.norme).length > 90 ? "…" : ""}</small></span>${chip(ESITO_GIUR[r.esito] || ["", "circle-dashed", r.esito])}<span class="freccia">${icona("chevron-down")}</span></summary>
                <div class="corpo"><p><strong>Norme:</strong> ${esc(r.norme)}</p><p>${esc(r.motivazione)}</p>${r.condizioni ? `<p><strong>Condizioni:</strong> ${esc(r.condizioni)}</p>` : ""}
                  <p>${String(r.fonti || "").split(/[\s;,]+/).filter((u) => /^https?:/.test(u)).map((u, i) => ext(u, `Fonte ${i + 1}`)).join(" · ")}</p></div></details>`).join("")}</div>`
              : `<p>${chip(["", "circle-dashed", "Non valutato"])} La verifica giuridica non è ancora disponibile.</p>`}
            ${scadenze.map((s) => `<div class="avviso ${s.pr === "critica" ? "critico" : "attenzione"}" style="margin-top:12px"><div class="avviso-titolo">${icona("calendar")}Scadenza europea collegata: ${dataBreve(s.data)}</div><p>${esc(s.breve)} · ${ext(s.url, esc(s.atto))} · ${esc(s.stato)}</p></div>`).join("")}
          </section>

          <section class="blocco" id="obiettivi" aria-labelledby="h-obiettivi">
            <h2 id="h-obiettivi">Obiettivi misurabili</h2>
            ${obiettivi.length ? tabellaObiettivi(obiettivi, false) : vuoto("Obiettivi non ancora definiti per questa proposta.")}
          </section>

          <section class="blocco" id="governo" aria-labelledby="h-governo">
            <h2 id="h-governo">Che cosa ha deciso il governo ombra</h2>
            ${dec ? `${bannerSim()}<div class="card decisione"><p class="etichetta">${dataBreve(seduta.data)} · ${esc(seduta.tipo)}</p>
                <div class="testa">${misuratore(DOSE[dec.variante] != null ? dec.variante : null)}${chip(ESITO_DEC[dec.esito] || ["", "circle-dashed", dec.esito])}<span class="nota">Regola: ${esc(dec.regola)}</span></div>
                <p class="motivo">${codici(esc(piano(dec.motivo)))}</p>
                ${deroga ? `<div class="deroga" style="margin-top:12px"><p class="etichetta">Deroga dall'esito del motore</p>${codici(esc(piano(deroga.testo)))}</div>` : ""}
                <p><a href="${linkSeduta(seduta.id)}">Apri il verbale della seduta ${icona("arrow-right")}</a></p></div>
                ${mandati.map((x) => `<div class="avviso" style="margin-top:12px"><div class="avviso-titolo">${icona("clipboard-check")}Mandato ${x.id} · entro il ${dataBreve(x.scadenza)}</div><p>${codici(esc(x.compito))}</p></div>`).join("")}`
              : vuoto("Non ancora all'ordine del giorno del Consiglio.")}
          </section>

          <section class="blocco" id="testo" aria-labelledby="h-testo">
            <h2 id="h-testo" class="vh">Testo completo</h2>
            <details class="richiudibile" data-md="scheda"><summary>${icona("scroll-text")}Testo completo <span class="conta">articolato normativo, cronoprogramma, indicatori</span><span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo md"></div></details>
          </section>
          <section class="blocco" id="fonti" aria-labelledby="h-fonti" style="margin-top:12px">
            <h2 id="h-fonti" class="vh">Fonti e metodo</h2>
            <details class="richiudibile"><summary>${icona("book-open")}Fonti e metodo<span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo">
              <p>Punteggi assegnati da un panel di ${D.valutatori.length} valutatori indipendenti che non hanno scritto le proposte. Classe calcolata provando migliaia di combinazioni di pesi tra i 10 valori.</p>
              <p>Costi: stime GovernAI, non certificate dalla Ragioneria generale dello Stato.</p>
              <p>Dati ${del_(D.generato)} · anello n. ${D.integrita.ultimi[0].n} della catena di integrità · impronta <span class="impronta">${esc(D.integrita.ultimi[0].hash)}</span></p></div></details>
          </section>
          ${collegati.length ? `<section class="blocco"><h2>Collegato a</h2><ul class="mandati">${collegati.join("")}</ul></section>` : ""}
          ${C ? C.sezione("proposta:" + id) : ""}
          <div class="azioni" style="margin-top:24px">${azioniCondividi()}</div>
        </article>
        ${indiceLaterale(voci, azioniCondividi())}
      </div>`;
  }

  function tabellaObiettivi(lista, conProposta) {
    const STATO = { raggiunto: ["favorevole", "circle-check", "Raggiunto"], "in linea": ["info", "trending-up", "In linea"], "in ritardo": ["attenzione", "circle-alert", "In ritardo"], peggiorato: ["alto", "trending-down", "Peggiorato"], "in osservazione": ["", "eye", "In osservazione"], manuale: ["", "pencil-ruler", "Si misura a mano"] };
    return `<div class="tabella-box"><table class="tabella a-card"><thead><tr>${conProposta ? "<th>Proposta</th>" : ""}<th>Obiettivo</th><th class="num">Base</th><th class="num">Ultimo</th><th class="num">Traguardo</th><th>Stato</th></tr></thead><tbody>
      ${lista.map((o) => `<tr>${conProposta ? `<td class="principale"><a href="${linkP(o.proposta)}" class="mono">${esc(o.proposta)}</a></td>` : ""}<td ${conProposta ? 'data-etichetta="Obiettivo"' : 'class="principale"'}>${esc(o.nome)} <span class="nota">${esc(o.unita || "")}</span></td><td class="num" data-etichetta="Base">${nf(o.base, 1)}${o.periodo_base ? ` <span class="nota">(${esc(o.periodo_base)})</span>` : ""}</td><td class="num" data-etichetta="Ultimo">${nf(o.ultimo, 1)}${o.periodo ? ` <span class="nota">(${esc(periodoBreve(o.periodo))})</span>` : ""}</td><td class="num" data-etichetta="Traguardo">${nf(o.obiettivo, 1)}</td>
        <td data-etichetta="Stato">${chip(STATO[o.stato] || ["", "circle-dashed", o.stato])}</td></tr>`).join("")}</tbody></table></div>`;
  }

  function coperture() {
    const base = new Set(scenario("base").coperture), comp = new Set(scenario("completo").coperture), mom = new Set(momento.coperture);
    const fondi = [...new Set(D.coperture.map((c) => c.fondo_id))].sort();
    const tot = (set) => D.coperture.filter((c) => set.has(c.misura_id)).reduce((a, c) => a + (c.gettito_min || 0), 0);
    const punti = (c) => `<span class="punti" role="img" aria-label="${D.valori.map((v) => v.nome + " " + (c[v.id] > 0 ? "+" : "") + c[v.id]).join(", ")}">${D.valori.map((v) => `<span class="${c[v.id] > 0 ? "p" : c[v.id] < 0 ? "n" : ""}"></span>`).join("")}</span>`;
    return `${schedeProgramma("coperture")}
      <p class="risposta">Il programma si finanzia con ${D.coperture.length} coperture concrete: un registro unico impedisce di contare due volte gli stessi soldi. Nel programma del momento ne sono attive ${mom.size}.</p>
      <div class="griglia g2 g4-d">${D.scenari.map((s) => `<div class="card kpi"><p class="etichetta">${esc(s.nome)}</p><p class="numero">${nf(s.spesa)}<small>mld/anno</small></p><p class="nota">${s.coperture.length} coperture · gettito minimo ${nf(s.gettito)} mld + fondi vincolati</p></div>`).join("")}</div>
      <p style="margin-top:12px">${badge("stima", STIMA)} <span class="nota">Gettito minimo delle coperture: programma base ${nf(tot(base))} mld, completo ${nf(tot(comp))} mld.</span></p>
      <form class="filtri-barra" role="search" onsubmit="return false">
        <label class="campo largo">Cerca<input type="search" id="c-cerca" placeholder="es. gasolio, IVA, tabacco"></label>
        <label class="campo">Fondo<select id="c-fondo"><option value="">Tutti i fondi</option>${fondi.map((f) => `<option>${esc(f)}</option>`).join("")}</select></label>
        <label class="campo">Livello<select id="c-livello"><option value="">Tutti</option><option value="1">1 · basso costo sociale</option><option value="2">2 · strutturali</option></select></label>
      </form>
      <div class="tabella-box"><table class="tabella a-card"><thead><tr><th>Copertura</th><th>Fondo</th><th class="num">Gettito min–max</th><th>Chi paga</th><th>Effetto sui valori</th><th>Nel momento</th></tr></thead>
        <tbody id="c-corpo">${D.coperture.map((c) => `<tr data-testo="${esc((c.misura_id + " " + c.descrizione + " " + c.chi_paga).toLowerCase())}" data-fondo="${esc(c.fondo_id)}" data-livello="${c.livello ?? 1}">
          <td class="principale"><span class="mono nota">${esc(c.misura_id)} · livello ${c.livello ?? 1}</span><br>${esc(c.descrizione)}</td><td data-etichetta="Fondo">${esc(c.fondo_id)}</td>
          <td class="num" data-etichetta="Gettito min–max">${nf(c.gettito_min)}–${nf(c.gettito_max)} mld</td><td data-etichetta="Chi paga">${esc(c.chi_paga)}</td>
          <td data-etichetta="Valori">${punti(c)}</td><td data-etichetta="Nel momento">${mom.has(c.misura_id) ? chip(["info", "check", "Attiva"]) : "—"}</td></tr>`).join("")}</tbody></table></div>`;
  }

  const ORIZZ = ["breve", "medio", "lungo"];
  function simulatore() {
    return `${schedeProgramma("valori")}
      <p class="risposta">Il programma non sceglie un unico peso tra i valori: qui puoi provare il tuo. La classifica si ricalcola con i punteggi del panel indipendente. Le proposte del nucleo robusto restano in alto con <em>qualunque</em> combinazione.</p>
      <div class="simulatore">
        <div class="card">
          <h2 style="font-size:20px">I tuoi pesi</h2>
          <div class="segmenti" role="group" aria-label="Pesi predefiniti">
            <button type="button" data-preset="uguali">Pesi uguali</button>${["FUT", "EQU", "BEN", "INN", "SIC"].map((id) => `<button type="button" data-preset="${id}">Più ${esc((D.valori.find((v) => v.id === id) || {}).nome || id).split(" ")[0].toLowerCase()}</button>`).join("")}
          </div>
          ${D.valori.map((v) => `<div class="cursore"><label for="w-${v.id}">${esc(v.nome)} <output id="wv-${v.id}" for="w-${v.id}"></output></label><input type="range" id="w-${v.id}" data-peso="${v.id}" min="0" max="100" value="50"></div>`).join("")}
          <h3 style="margin-top:16px;font-size:16px">Orizzonti di tempo</h3>
          ${ORIZZ.map((o) => `<div class="cursore"><label for="h-${o}">${o[0].toUpperCase() + o.slice(1)} periodo <output id="hv-${o}" for="h-${o}"></output></label><input type="range" id="h-${o}" data-orizzonte="${o}" min="0" max="100" value="${o === "lungo" ? 40 : 30}"></div>`).join("")}
          <p class="nota">Regola della Carta: il lungo periodo pesa almeno quanto il breve. Il cursore si adegua da solo.</p>
        </div>
        <div class="card"><h2 style="font-size:20px">Classifica</h2><p class="nota">Effetto pesato sui valori; le frecce indicano lo spostamento rispetto ai pesi uguali.</p><ol class="classifica" id="classifica" aria-live="polite"></ol></div>
      </div>`;
  }
  function aggiornaClassifica() {
    const w = {}, h = {};
    D.valori.forEach((v) => { w[v.id] = +$("#w-" + v.id).value; $("#wv-" + v.id).textContent = w[v.id]; });
    if (+$("#h-lungo").value < +$("#h-breve").value) $("#h-lungo").value = $("#h-breve").value;
    ORIZZ.forEach((o) => { h[o] = +$("#h-" + o).value; $("#hv-" + o).textContent = h[o]; });
    const sw = Object.values(w).reduce((a, b) => a + b, 0) || 1, sh = Object.values(h).reduce((a, b) => a + b, 0) || 1;
    const punteggio = (p, pesi, oriz) => D.valori.reduce((acc, v, j) => acc + pesi[v.id] * ORIZZ.reduce((a, o, k) => a + oriz[o] * p.punteggi[j][k], 0), 0);
    const uguali = Object.fromEntries(D.valori.map((v) => [v.id, 1 / D.valori.length])), oU = { breve: 1 / 3, medio: 1 / 3, lungo: 1 / 3 };
    const pw = Object.fromEntries(Object.entries(w).map(([k, x]) => [k, x / sw])), ph = Object.fromEntries(Object.entries(h).map(([k, x]) => [k, x / sh]));
    const con = D.proposte.filter((p) => p.punteggi);
    const base = con.map((p) => [p.id, punteggio(p, uguali, oU)]).sort((a, b) => b[1] - a[1]).map((x) => x[0]);
    const lista = con.map((p) => ({ p, u: punteggio(p, pw, ph) })).sort((a, b) => b.u - a.u);
    const max = Math.max(...lista.map((x) => Math.abs(x.u)), 0.01);
    $("#classifica").innerHTML = lista.map((x, i) => {
      const salto = base.indexOf(x.p.id) - i;
      return `<li><span class="pos">${i + 1}</span><span><a href="${linkP(x.p.id)}">${esc(tit(x.p.titolo))}</a> <span class="nota mono">${esc(x.p.id)}</span> ${x.p.classe === "robusta" ? chipClasse("robusta") : ""}</span>
        <span class="salto ${salto > 0 ? "su" : salto < 0 ? "giu" : ""}" aria-label="${salto > 0 ? `sale di ${salto}` : salto < 0 ? `scende di ${-salto}` : "stessa posizione"}">${salto > 0 ? "▲ " + salto : salto < 0 ? "▼ " + -salto : "="}</span>
        <div class="barra" aria-hidden="true"><span style="width:${Math.max(0, x.u) / max * 100}%"></span></div></li>`;
    }).join("");
    icone();
  }

  // ---------- Il programma in una pagina: perché, come, cosa misuriamo, chi ne beneficia ----------
  const QUATTRO = [["perche", "heart", "Perché", "Il valore che vogliamo dare"], ["come", "route", "Come", "Le misure e come si pagano"],
    ["cosa", "target", "Cosa misuriamo", "Come sapremo se ce l'abbiamo fatta"], ["chi", "users-round", "Chi ne beneficia", "Le persone avvantaggiate"]];
  const testaQuattro = (k) => { const q = QUATTRO.find((x) => x[0] === k); return `<p class="q-etichetta q-${k}">${icona(q[1])}${q[2]}</p>`; };
  const nomeValore = (id) => (D.valori.find((v) => v.id === id) || {}).nome || id;
  const numIndic = (x) => x == null || x === "" ? null : Number(x).toLocaleString("it-IT", { maximumFractionDigits: 2 });
  function rigaIndicatore(id) {
    const o = (D.schema.indicatori || {})[id];
    if (!o) return "";
    const un = String(o.unita || "");
    const u = !un ? "" : un === "%" ? "%" : un.startsWith("%") ? "% " + esc(un.slice(1).trim()) : " " + esc(un);
    const b = numIndic(o.base), t = numIndic(o.obiettivo_5a);
    const freccia = o.direzione === "giu" ? "trending-down" : "trending-up";
    const da = b != null ? `${b}${u}` : `<span class="nota">${esc(piano(o.testo_base) || "da rilevare")}</span>`;
    const a = t != null ? `<strong>${t}${u}</strong>` : `<strong>${esc(piano(o.testo_5a) || "—")}</strong>`;
    const fonte = [o.fonte, o.periodo].filter(Boolean).join(", ");
    return `<li><span class="q-ind-nome">${esc(piano(o.nome))}</span>
      <span class="q-ind-valori">${da} ${icona(freccia)} ${a} <span class="nota">in 5 anni</span></span>
      <span class="nota">${fonte ? `Base: ${esc(fonte)} · ` : ""}<a href="${linkP(o.proposta)}">${esc(o.proposta)}</a></span></li>`;
  }
  function unaPagina(params) {
    const S = D.schema || {};
    if (!S.missioni) return `${schedeProgramma("una-pagina")}${vuoto("Lo schema del programma non è ancora disponibile.")}`;
    const sc = scenario(params.get("scenario") || S.scenario || "momento");
    const P = S.programma || {};
    const costo = (ids) => ids.reduce((a, id) => a + ((sc.misure[id] || {}).costo || 0), 0);
    const cop = D.coperture.filter((c) => sc.coperture.includes(c.misura_id) && c.gettito_min > 0).sort((a, b) => (b.gettito_min || 0) - (a.gettito_min || 0));
    const dose = (m) => !m ? misuratore(null) : m.variante === "ZERO" ? `<span class="chip">${icona("scroll-text")}Solo regole, costo zero</span>` : misuratore(m.variante) + `<span class="nota">${nf(m.costo)} mld</span>`;
    const misura = (id) => { const p = proposta(id), m = sc.misure[id]; if (!p) return ""; return `<li class="${m ? "" : "fuori"}"><a href="${linkP(id)}">${esc(tit(p.titolo))}</a> <span class="nota mono">${esc(id)}</span><span class="q-dose">${dose(m)}</span></li>`; };
    const missione = (m) => {
      const dentro = m.proposte.filter((id) => sc.misure[id]).sort((a, b) => sc.misure[b].costo - sc.misure[a].costo);
      const fuori = m.proposte.filter((id) => !dentro.includes(id));
      const prime = dentro.filter((id) => sc.misure[id].variante !== "ZERO").slice(0, 5), altre = dentro.filter((id) => !prime.includes(id));
      const fonteChi = (g) => !g.fonte ? "" : /da stimare/i.test(g.fonte) ? badge("verificare", "Numero da stimare: la fonte non è ancora disponibile.") : badge(/stima|elaborazione|calcol/i.test(g.fonte) ? "stima" : "verificato", g.fonte);
      return `<article class="card missione" id="${esc(m.id)}" aria-labelledby="t-${esc(m.id)}">
        <header class="missione-testa">${icona(m.icona || "circle")}<div><h2 id="t-${esc(m.id)}">${esc(m.titolo)}</h2>
          <p class="nota">${dentro.length} misure su ${m.proposte.length} · ${nf(costo(m.proposte))} mld l'anno ${badge("stima", STIMA)}</p></div></header>
        <div class="quattro">
          <section class="q-cella">${testaQuattro("perche")}<p>${esc(m.perche)}</p><div class="chips">${(m.valori || []).map((v) => `<span class="chip info">${esc(nomeValore(v))}</span>`).join("")}</div></section>
          <section class="q-cella">${testaQuattro("come")}<p>${esc(m.come)}</p>
            <p class="q-sotto">Le misure con più risorse</p>
            <ul class="q-misure">${prime.map(misura).join("")}</ul>
            ${altre.length ? `<details class="leggi"><summary>Altre ${altre.length} ${altre.length === 1 ? "misura" : "misure"} nel programma</summary><ul class="q-misure">${altre.map(misura).join("")}</ul></details>` : ""}
            ${fuori.length ? `<details class="leggi"><summary>${fuori.length} ${fuori.length === 1 ? "misura fuori" : "misure fuori"} da questa versione</summary><ul class="q-misure">${fuori.map(misura).join("")}</ul></details>` : ""}
            <p class="q-sostenibile">${icona("scale")}<span><strong>Sostenibilità.</strong> ${esc(m.sostenibilita)}</span></p></section>
          <section class="q-cella">${testaQuattro("cosa")}<ul class="q-ind">${(m.indicatori || []).map(rigaIndicatore).join("")}</ul></section>
          <section class="q-cella">${testaQuattro("chi")}<ul class="q-lista-chi">${(m.chi || []).map((g) => `<li><strong>${esc(g.gruppo)}</strong>${g.quanti ? `<span class="q-quanti">${esc(g.quanti)} ${fonteChi(g)}</span>` : ""}<span>${esc(g.cosa_cambia)}</span></li>`).join("")}</ul></section>
        </div></article>`;
    };
    return `${schedeProgramma("una-pagina")}
      <p class="risposta">Il programma in una pagina. Per ogni missione: <strong>perché</strong> la facciamo, <strong>come</strong> e con quali soldi, <strong>cosa misuriamo</strong> per dire che ce l'abbiamo fatta, e <strong>chi ne beneficia</strong>.</p>
      <div class="filtri-barra"><label class="campo">Versione del programma<select id="schema-scenario">${D.scenari.map((x) => `<option value="${x.id}" ${x.id === sc.id ? "selected" : ""}>${esc(x.nome)}${x.id === S.scenario ? " (scelto)" : ""}</option>`).join("")}</select></label></div>
      <p class="nota" style="margin-top:8px">${esc(sc.descrizione)}.</p>

      <section class="tela" aria-label="Il programma in quattro domande">
        ${QUATTRO.map(([k, ic, t, sotto]) => `<div class="tela-cella q-${k}"><p class="q-etichetta">${icona(ic)}${t}</p><p class="nota">${sotto}</p><p class="tela-testo">${esc(P[k] || "")}</p></div>`).join("")}
      </section>

      <section class="sezione" aria-labelledby="t-conti">
        <div class="sezione-testa"><h2 id="t-conti">I conti in una riga</h2><a href="#/programma/coperture">Come si paga</a></div>
        <div class="griglia g2 g4-d">
          <div class="card kpi"><p class="etichetta">Spesa nuova</p><p class="numero">${nf(sc.spesa)}<small>mld/anno</small></p><p class="nota">a regime</p>${badge("stima", STIMA)}</div>
          <div class="card kpi"><p class="etichetta">Coperture</p><p class="numero">${nf(sc.gettito)}<small>mld/anno</small></p><p class="nota">gettito minimo, più i fondi vincolati</p></div>
          <div class="card kpi"><p class="etichetta">Nuovo deficit</p><p class="numero">0<small>mld</small></p><p class="nota">nessuna spesa a debito</p></div>
          <div class="card kpi"><p class="etichetta">Misure</p><p class="numero">${Object.keys(sc.misure).length}<small>su ${D.proposte.length}</small></p><p class="nota">in ${S.missioni.length} missioni; ${Object.values(sc.misure).filter((m) => m.variante === "ZERO").length} sono solo regole, a costo zero</p></div>
        </div>
      </section>

      ${(P.indicatori_chiave || []).length ? `<section class="sezione" aria-labelledby="t-chiave">
        <div class="sezione-testa"><h2 id="t-chiave">Ce l'avremo fatta se…</h2><a href="#/dati/obiettivi">Tutti gli obiettivi</a></div>
        <ul class="q-ind griglia g2-d">${P.indicatori_chiave.map(rigaIndicatore).join("")}</ul></section>` : ""}

      <section class="sezione" aria-labelledby="t-missioni">
        <div class="sezione-testa"><h2 id="t-missioni">Le ${S.missioni.length} missioni</h2></div>
        <nav class="temi nav-missioni" aria-label="Missioni">${S.missioni.map((m) => `<a href="#${esc(m.id)}" data-ancora>${esc(m.titolo)}<span>${nf(costo(m.proposte), 1)} mld</span></a>`).join("")}</nav>
        <div class="missioni">${S.missioni.map(missione).join("")}</div>
      </section>

      <section class="sezione" aria-labelledby="t-contribuisce">
        <div class="sezione-testa"><h2 id="t-contribuisce">Chi contribuisce</h2><a href="#/programma/coperture">Tutte le coperture</a></div>
        <p class="nota" style="margin-top:-8px">Le coperture attive in questa versione, dalla più grande. Ogni euro di spesa ha una copertura certa: niente deficit, niente recupero di evasione non ancora incassato.</p>
        <div class="tabella-box"><table class="tabella a-card"><thead><tr><th>Copertura</th><th>Chi paga o rinuncia</th><th class="num">Gettito minimo</th></tr></thead><tbody>
          ${cop.map((c) => `<tr><td class="principale"><span class="mono nota">${esc(c.misura_id)}</span><br>${esc(c.descrizione)}</td><td data-etichetta="Chi paga">${esc(c.chi_paga)}</td><td class="num" data-etichetta="Gettito minimo">${nf(c.gettito_min)} mld</td></tr>`).join("")}
        </tbody></table></div>
      </section>
      <div class="azioni" style="margin-top:24px"><a class="btn primario" href="#/programma">Tutte le ${D.proposte.length} proposte ${icona("arrow-right")}</a>${azioniCondividi()}</div>`;
  }

  function equita() {
    return `${schedeProgramma("equita")}
      <div class="md documento">${md((D.documenti.equita || "*Capitolo non ancora disponibile.*").replace(/^# .*\n/, ""))}</div>
      <div class="azioni" style="margin-top:24px"><a class="btn primario" href="#/programma/una-pagina">Il programma in una pagina ${icona("arrow-right")}</a>${azioniCondividi()}</div>`;
  }

  function sintesi() {
    return `${schedeProgramma("sintesi")}
      <div class="md documento">${md((D.documenti.sintesi || "*Sintesi non ancora disponibile.*").replace(/^# .*\n/, ""))}</div>
      <div class="azioni" style="margin-top:24px"><a class="btn primario" href="#/programma">Tutte le ${D.proposte.length} proposte ${icona("arrow-right")}</a>${azioniCondividi()}</div>`;
  }

  function confronti(params) {
    const doc = params.get("doc") === "partiti" ? "partiti" : "confronto";
    return `${schedeProgramma("confronti")}
      <div class="segmenti" role="group" aria-label="Confronto"><a class="btn s ${doc === "confronto" ? "primario" : ""}" href="#/programma/confronti">Altri Paesi</a><a class="btn s ${doc === "partiti" ? "primario" : ""}" href="#/programma/confronti?doc=partiti">Governo e partiti</a></div>
      <div class="md documento" style="margin-top:24px">${md(D.documenti[doc] || "*Documento non ancora disponibile.*")}</div>`;
  }

  // ---------- Governo ----------
  const nomeRuolo = (a) => { const e = (D.governo.esperti || {}); return a === "capo" ? "Capo di governo" : a === "opposizione" ? "Opposizione leale" : a.startsWith("esperto_") ? (e[a.slice(8)] || a.slice(8)) : a.startsWith("ministro_") ? "Ministro · " + (D.aree[a.slice(9)] || a.slice(9)) : a; };
  const linkConsiglio = () => `${repo}/issues/new?template=consiglio.yml`;
  const linkRiesame = (seduta, titolo) => `${repo}/new/main/governo/richieste?filename=${encodeURIComponent(OGGI + "-riesame-" + seduta + ".md")}&value=${encodeURIComponent(`# Riesame: ${titolo}\n\nRiesame della seduta: ${seduta}\n\nMotivi del riesame:\n- verifica dello stato dell'arte richiesta da un membro del progetto\n`)}`;
  const schedeGoverno = (k) => `${bannerSim("fisso")}<h1>Governo</h1>${schede([["sedute", "Sedute", "#/governo", VERBALI.length], ["decisioni", "Decisioni in vigore", "#/governo/decisioni"], ["mandati", "Mandati", "#/governo/mandati", (D.governo.mandati || []).filter((m) => m.stato === "aperto").length], ["credibilita", "Credibilità", "#/governo/credibilita"], ["regolamento", "Chi siede e regole", "#/governo/regolamento"]], k)}`;

  function governo() {
    const decisioni = VERBALI.reduce((a, v) => a + v.dec.length, 0);
    return `${schedeGoverno("sedute")}
      <p class="risposta">Un governo ombra che decide con regole verificabili: esperti di ogni materia, nove ministri, un'opposizione leale e un capo di governo. Si è riunito ${VERBALI.length} volte e ha preso ${decisioni} decisioni.</p>
      <div class="azioni" style="margin-bottom:8px"><a class="btn primario" href="${esc(linkConsiglio())}" target="_blank" rel="noopener">${icona("message-circle-question")}Fai una domanda al Consiglio<span class="vh"> (si apre in una nuova scheda)</span></a><a class="btn" href="#/partecipa">Altri modi di partecipare</a></div>
      <p class="nota">Il Consiglio si riunisce ogni lunedì, quando scatta un'allerta nuova e su richiesta approvata da una persona del progetto.</p>
      <div class="griglia" style="margin-top:24px">${VERBALI.map((x) => `<a class="card" href="${linkSeduta(x.id)}"><p class="etichetta">${dataBreve(x.data)} · ${esc(x.tipo)}</p><h2 class="titolo-card" style="font-size:22px">${esc(x.titolo)}</h2>${x.domanda ? `<p class="nota">«${esc(x.domanda)}»</p>` : ""}${contatore(x.dec)}<p class="nota">${x.deroghe.length} deroghe · ${x.obiezioni.length} obiezioni · ${x.mandati.length} mandati</p></a>`).join("") || vuoto("Il Consiglio non si è ancora riunito.")}</div>`;
  }
  function decisioniInVigore() {
    const V = D.governo.verifiche || [];
    return `${schedeGoverno("decisioni")}
      <p class="risposta">Ogni giorno il sistema riverifica, con un controllo ripetibile, se le decisioni ancora valide reggono sui dati di oggi. Se una non regge, il riesame si mette in coda da solo.</p>
      ${V.length ? `<div class="griglia">${V.map((v) => `<div class="card"><div class="chips">${v.esito === "confermata" ? chip(["favorevole", "circle-check", "Confermata"]) : chip(["attenzione", "refresh-ccw", "Da riesaminare"])}${v.riesame_accodato ? chip(["", "clock", "Riesame in coda"]) : ""}</div>
          <h2 style="font-size:20px;margin-top:8px"><a href="${linkSeduta(v.seduta)}">${esc(v.titolo)}</a></h2>
          <p class="nota">Seduta ${del_(v.seduta)} · verificata il ${dataBreve(v.verificata)} · ${v.eta_giorni} giorni</p>
          ${[...(v.motivi || []), ...(v.note || [])].map((x) => `<p>${esc(x)}</p>`).join("")}
          <a class="btn s" href="${esc(linkRiesame(v.seduta, v.titolo))}" target="_blank" rel="noopener">${icona("refresh-ccw")}Chiedi un riesame<span class="vh"> (membri del progetto, si apre in una nuova scheda)</span></a></div>`).join("")}</div>` : vuoto("Nessuna verifica ancora.")}`;
  }
  function mandatiVista() {
    const M = (D.governo.mandati || []).slice().sort((a, b) => a.scadenza.localeCompare(b.scadenza));
    const aperti = M.filter((m) => m.stato === "aperto"), chiusi = M.filter((m) => m.stato !== "aperto");
    const riga = (m) => { const t = traGiorni(m.scadenza); return `<li><div class="chips"><b>${esc(m.id)}</b>${m.stato === "aperto" ? (t < 0 ? chip(["alto", "triangle-alert", `Scaduto da ${-t} giorni`]) : chip(["", "calendar", `Entro il ${dataBreve(m.scadenza)}`])) : chip(["favorevole", "circle-check", `Chiuso ${m.chiuso_il ? "il " + dataBreve(m.chiuso_il) : ""}`])}<span class="nota">Ministro · ${esc(D.aree[m.area] || m.area)} · seduta ${del_(m.seduta)}</span></div><p style="margin:6px 0 0">${codici(esc(m.compito))}</p></li>`; };
    return `${schedeGoverno("mandati")}
      <p class="risposta">I mandati sono compiti con una scadenza affidati ai ministri. ${aperti.length} sono aperti.</p>
      <ul class="mandati">${aperti.map(riga).join("") || "<li>Nessun mandato aperto.</li>"}</ul>
      ${chiusi.length ? `<details class="richiudibile"><summary>Mandati chiusi <span class="conta">${chiusi.length}</span><span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo"><ul class="mandati">${chiusi.map(riga).join("")}</ul></div></details>` : ""}`;
  }
  function credibilita() {
    const C = D.governo.credibilita || [];
    return `${schedeGoverno("credibilita")}
      <p class="risposta">Ogni decisione porta con sé previsioni scritte, confrontate alla scadenza con i dati ufficiali. Così si misura chi legge meglio la realtà.</p>
      <p class="nota">Punteggio di Brier sulle previsioni scadute: 0 = perfetta, 0,25 = come tirare a caso, 1 = sempre sbagliata.</p>
      ${C.length ? `<div class="tabella-box"><table class="tabella a-card"><thead><tr><th>Ruolo</th><th class="num">Verificate</th><th class="num">In attesa</th><th class="num">Brier medio</th></tr></thead><tbody>${C.map((c) => `<tr><td class="principale">${esc(nomeRuolo(c.autore))}</td><td class="num" data-etichetta="Verificate">${esc(c.verificate)}</td><td class="num" data-etichetta="In attesa">${esc(c.in_attesa)}</td><td class="num" data-etichetta="Brier medio">${c.brier_medio === "" || c.brier_medio == null ? "non ancora" : nf(+c.brier_medio, 3)}</td></tr>`).join("")}</tbody></table></div>` : vuoto("Nessuna previsione ancora.")}`;
  }
  function regolamento() {
    const e = D.governo.esperti || {};
    return `${schedeGoverno("regolamento")}
      <section><h2>Il collegio degli esperti <small class="nota">${Object.keys(e).length}</small></h2><div class="chips">${Object.values(e).map((x) => chip(["", "graduation-cap", x])).join("")}</div></section>
      <div class="md documento sezione">${md(D.governo.regolamento || "")}</div>`;
  }

  function schedaSeduta(id) {
    const v = VERBALI.find((x) => x.id === id);
    if (!v) return nonTrovato(`Nessuna seduta «${id}».`);
    const ver = v.verifica;
    const risposta = v.S["Risposta del Consiglio"] || "";
    const indirizzo = v.S["Indirizzo del capo di governo"] || "";
    const breve = (indirizzo || risposta).split(/\n\n/)[0];
    const voci = [["domanda", v.domanda ? "La domanda" : "Il motivo"], ["risposta", "La risposta"], ["decisioni", `Decisioni (${v.dec.length})`], ["deroghe", `Deroghe (${v.deroghe.length})`], ["obiezioni", `Obiezioni (${v.obiezioni.length})`], ["pareri", `Pareri (${v.pareri.length})`], ["ministri", `Ministri (${v.ministri.length})`], ["mandati", `Mandati (${v.mandati.length})`]];
    const altri = VERBALI.filter((x) => x !== v);
    const filtri = [["tutte", `Tutte ${v.dec.length}`], ...["adottata", "respinta", "rinviata"].map((e) => [e, `${ESITO_DEC[e][2].replace(/a$/, "e")} ${v.dec.filter((d) => d.esito === e).length}`])];
    const riesame = `<a class="btn s" href="${esc(linkRiesame(v.id, v.titolo))}" target="_blank" rel="noopener">${icona("refresh-ccw")}Chiedi un riesame<span class="vh"> (si apre in una nuova scheda)</span></a><span class="nota">Riesame: membri del progetto</span>`;
    return `
      ${bannerSim("fisso")}
      <nav class="briciole" aria-label="Briciole di pane"><a href="#/governo">Governo</a><span aria-hidden="true">›</span><a href="#/governo">Sedute</a><span aria-hidden="true">›</span><span aria-current="page">${dataBreve(v.data)}</span></nav>
      <div class="con-indice">
        <article>
          <header class="intestazione">
            <p class="etichetta">${esc(v.tipo)} · ${dataLunga(v.data)}</p>
            <h1>${esc(v.titolo)}</h1>
            <div class="chips">${ver ? chip(ver.esito === "confermata" ? ["favorevole", "circle-check", `Confermata dalla verifica ${del_(ver.verificata)}`] : ["attenzione", "refresh-ccw", "Da riesaminare"]) : chip(["", "circle-dashed", "Superata dalla seduta successiva"])}</div>
            <ol class="percorso" aria-label="Come si è svolta la seduta">
              <li><a href="#pareri"><b>Esperti</b><span>${v.pareri.length} pareri, scritti da soli</span></a></li>
              <li><a href="#ministri"><b>Ministri</b><span>${v.ministri.length} posizioni</span></a></li>
              <li><a href="#obiezioni"><b>Opposizione leale</b><span>${v.obiezioni.length} obiezioni</span></a></li>
              <li><a href="#decisioni"><b>Capo di governo</b><span>${v.dec.length} decisioni</span></a></li>
            </ol>
            ${indiceMobile(voci)}
          </header>

          <section class="blocco" id="domanda" aria-labelledby="h-domanda" style="margin-top:8px">
            <h2 id="h-domanda">${v.domanda ? "La domanda" : "Il motivo della convocazione"}</h2>
            ${v.domanda ? `<blockquote class="citazione">${esc(v.domanda)}</blockquote>
              <details class="richiudibile" data-md-testo="${esc(v.dom.replace(/^# .*\n/, ""))}"><summary>Perché ora e vincoli<span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo md"></div></details>`
              : `<blockquote class="citazione">${esc(piano(v.motivo))}</blockquote>`}
          </section>

          <section class="blocco" id="risposta" aria-labelledby="h-risposta">
            <h2 id="h-risposta">La risposta in breve</h2>
            <p class="testo-lettura">${breveEResto(breve, 760)}</p>
            ${risposta ? `<details class="richiudibile" data-md-testo="${esc(risposta)}"><summary>Risposta completa del Consiglio<span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo md"></div></details>` : ""}
          </section>

          <section class="blocco" id="decisioni" aria-labelledby="h-decisioni">
            <h2 id="h-decisioni">Decisioni <small>${v.dec.length} proposte esaminate</small></h2>
            ${contatore(v.dec)}
            <div class="filtri" role="group" aria-label="Filtra le decisioni">${filtri.map(([k, t], i) => `<button type="button" data-filtro="${k}" aria-pressed="${i === 0}">${esc(t)}</button>`).join("")}</div>
            <p class="vh" aria-live="polite" id="esito-filtro"></p>
            <ul class="decisioni">${v.dec.map((d, i) => { const p = proposta(d.id); return `<li class="card decisione" data-esito="${esc(d.esito)}" ${i >= 6 ? "data-oltre hidden" : ""}>
              <h3 class="titolo-card"><a href="${linkP(d.id)}">${esc(tit(p ? p.titolo : d.titolo))}</a> <span class="nota mono">${esc(d.id)}</span></h3>
              <div class="testa">${misuratore(DOSE[d.variante] != null ? d.variante : null)}${chip(ESITO_DEC[d.esito] || ["", "circle-dashed", d.esito])}${v.deroghe.some((x) => x.id === d.id) ? chip(["attenzione", "git-branch", "Con deroga"]) : ""}<span class="nota">Regola: ${esc(d.regola)}</span></div>
              <details><summary>Motivazione</summary><p class="motivo">${codici(esc(piano(d.motivo)))}</p></details></li>`; }).join("")}</ul>
            ${v.dec.length > 6 ? `<p class="altre"><button class="btn" type="button" data-azione="altre">Mostra tutte le ${v.dec.length} decisioni</button></p>` : ""}
          </section>

          <section class="blocco" id="deroghe" aria-labelledby="h-deroghe">
            <h2 id="h-deroghe">Deroghe dall'esito del motore <small>quando il capo di governo si discosta dal calcolo, lo dichiara</small></h2>
            ${v.deroghe.length ? v.deroghe.map((d) => `<div class="deroga"><b><a href="${linkP(d.id)}">${esc(d.id)}</a></b> · ${esc(tit((proposta(d.id) || {}).titolo))}<p style="margin:4px 0 0">${codici(esc(piano(d.testo)))}</p></div>`).join("") : `<p class="nota">Nessuna deroga: le decisioni seguono l'esito del motore.</p>`}
          </section>

          <section class="blocco" id="obiezioni" aria-labelledby="h-obiezioni">
            <h2 id="h-obiezioni">Obiezioni dell'opposizione leale <small>cerca il punto debole, con prove</small></h2>
            ${v.obiezioni.length ? `<div class="griglia">${v.obiezioni.map((o) => `<div class="card obiezione">
                <h3>${codici(esc(o.titolo))}</h3>
                <dl><dt>Obiezione</dt><dd>${breveEResto(o.testo)}</dd>
                ${o.prova ? `<dt>Prova</dt><dd>${breveEResto(o.prova, 140)}</dd>` : ""}
                ${o.cambia ? `<dt>Cambierebbe idea se</dt><dd>${breveEResto(o.cambia)}</dd>` : ""}
                <dt>Risposta del capo</dt><dd>${o.risposta && o.risposta !== "—" && o.risposta !== "non registrata" ? codici(esc(piano(o.risposta))) : `${chip(["attenzione", "circle-alert", "Non registrata"])} <span class="nota">La regola 7 chiede una risposta scritta: nel verbale manca.</span>`}</dd></dl></div>`).join("")}</div>`
              : `<p class="nota">L'opposizione leale non ha sollevato obiezioni in questa seduta.</p>`}
          </section>

          <section class="blocco" id="pareri" aria-labelledby="h-pareri">
            <h2 id="h-pareri">Pareri degli esperti <small>${v.pareri.length}</small></h2>
            ${v.pareri.map((x, i) => `<details class="richiudibile" data-sez="pareri" data-i="${i}"><summary>${icona("graduation-cap")}${esc(x.titolo)}<span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo md"></div></details>`).join("") || `<p class="nota">Nessun parere registrato.</p>`}
          </section>
          <section class="blocco" id="ministri" aria-labelledby="h-ministri">
            <h2 id="h-ministri">Posizioni dei ministri <small>${v.ministri.length}</small></h2>
            ${v.ministri.map((x, i) => `<details class="richiudibile" data-sez="ministri" data-i="${i}"><summary>${icona("user-round")}${esc(x.titolo)}<span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo md"></div></details>`).join("")}
          </section>

          <section class="blocco" id="mandati" aria-labelledby="h-mandati">
            <h2 id="h-mandati">Mandati <small>compiti con scadenza affidati ai ministri</small></h2>
            ${v.mandati.length ? `<ul class="mandati">${v.mandati.map((x) => `<li><b>${x.id}</b> · ${esc(x.chi)} · entro il ${dataBreve(x.scadenza)}<br>${codici(esc(x.compito))}</li>`).join("")}</ul>` : `<p class="nota">Nessun mandato in questa seduta.</p>`}
            ${v.previsioni ? `<p class="nota" style="margin-top:12px">${icona("target")} ${v.previsioni} previsioni registrate, verificate alla scadenza con i dati ufficiali.</p>` : ""}
            ${v.rilievi ? `<p class="nota">${v.rilievi} ${v.rilievi === 1 ? "rilievo formale annotato" : "rilievi formali annotati"} dal sistema.</p>` : ""}
            <p class="nota">Registrata nella catena di integrità · <a href="#/controlli/integrita">vedi il registro</a></p>
          </section>
          ${altri.length ? `<section class="blocco"><h2>Altre sedute</h2>${altri.map((x) => `<a class="card" href="${linkSeduta(x.id)}" style="margin-top:12px"><p class="etichetta">${dataBreve(x.data)} · ${esc(x.tipo)}</p><h3 class="titolo-card">${esc(x.titolo)}</h3>${contatore(x.dec)}</a>`).join("")}</section>` : ""}
          <div class="azioni" style="margin-top:24px">${azioniCondividi()}${riesame}</div>
        </article>
        ${indiceLaterale(voci, azioniCondividi() + riesame)}
      </div>`;
  }

  // ---------- Dati ----------
  const GRUPPI = [["Prezzi e conti pubblici", ["inflazione", "debito_trimestrale", "debito_annuo", "deficit_annuo", "interessi", "spread", "rendimento_btp"]], ["Lavoro e giovani", ["disoccupazione", "disoccupazione_giovani", "neet"]], ["Crescita", ["pil_trimestrale", "produzione_industriale", "fiducia_consumatori"]], ["Società", ["fecondita"]]];
  const schedeDati = (k) => `<h1>Dati</h1>${schede([["indicatori", "Indicatori", "#/dati", (D.indicatori || []).length], ["allerte", "Allerte", "#/dati/allerte", ALLERTE.length], ["obiettivi", "Obiettivi e risultati", "#/dati/obiettivi", (D.obiettivi || []).length], ["diario", "Diario quotidiano", "#/dati/diario"]], k)}`;
  function datiVista() {
    const ok = (D.indicatori || []).filter((i) => i.stato === "ok");
    const salgono = ALLERTE.map((r) => nomeInd(r.ind).split(" (")[0].toLowerCase()).filter((x, i, a) => x && a.indexOf(x) === i);
    return `${schedeDati("indicatori")}
      <p class="risposta">${ALLERTE.length ? `${ALLERTE.length} allerte attive su ${D.indicatori.length} indicatori: ${esc(salgono.join(", "))}.` : `Nessuna allerta: i ${D.indicatori.length} indicatori sono nelle soglie.`} Ultimo dato disponibile e variazione sul periodo precedente.</p>
      ${ALLERTE.length ? `<div class="griglia g2-d">${ALLERTE.slice(0, 2).map((r) => avvisoAllerta(r, true)).join("")}</div><p><a href="#/dati/allerte">Tutte le allerte ${icona("arrow-right")}</a></p>` : ""}
      ${GRUPPI.map(([nome, ids]) => { const l = ids.map((id) => ok.find((i) => i.id === id)).filter(Boolean); return l.length ? `<section class="sezione"><div class="sezione-testa"><h2>${esc(nome)}</h2></div><div class="indicatori">${l.map(cardIndicatore).join("")}</div></section>` : ""; }).join("")}
      <p class="nota sezione">HICP: indice armonizzato dei prezzi al consumo. PIL: prodotto interno lordo. NEET: giovani che non lavorano, non studiano e non seguono una formazione. Spread IT-DE: differenza di rendimento tra titoli decennali italiani e tedeschi.</p>`;
  }
  function allerteVista() {
    return `${schedeDati("allerte")}
      <p class="risposta">Le allerte scattano da regole fisse e pubbliche (<code>sistema/config.yaml</code>). Quando una è attiva, il programma del momento cambia priorità.</p>
      ${ALLERTE.map((r) => avvisoAllerta(r, true)).join("") || `<div class="avviso favorevole"><div class="avviso-titolo">${icona("circle-check")}Nessuna allerta attiva.</div></div>`}
      <section class="sezione"><div class="sezione-testa"><h2>Tutte le regole</h2></div>
      <div class="tabella-box"><table class="tabella a-card"><thead><tr><th>Regola</th><th>Condizione</th><th>Stato</th></tr></thead><tbody>${(D.regole || []).map((r) => `<tr><td class="principale">${esc(String(r.messaggio).split(":")[0])}</td><td data-etichetta="Condizione"><span class="mono">${esc(nomeInd(IND[r.indicatore] || { nome: r.indicatore }))}: ${esc(r.condizione)}</span></td><td data-etichetta="Stato">${(D.allerte_attive || []).includes(r.id) ? chip(gravAllerta(r).slice(0, 2).concat("Attiva")) : chip(["favorevole", "circle-check", "Non attiva"])}</td></tr>`).join("")}</tbody></table></div></section>`;
  }
  function obiettiviVista(params) {
    const O = D.obiettivi || [];
    const tema = params.get("tema") || "";
    const conta = O.reduce((a, x) => (a[x.stato] = (a[x.stato] || 0) + 1, a), {});
    const lista = O.filter((o) => !tema || o.proposta.startsWith(tema));
    return `${schedeDati("obiettivi")}
      <p class="risposta">Ogni misura ha obiettivi misurabili, con valore di partenza e traguardo. Il sistema li segue sulle serie ufficiali e impara dagli scostamenti.</p>
      <div class="chips">${Object.entries(conta).map(([k, v]) => chip(["", "circle-dot", `${k}: ${v}`])).join("")}</div>
      <form class="filtri-barra" onsubmit="return false"><label class="campo">Tema<select id="o-tema"><option value="">Tutti i temi</option>${Object.entries(D.aree).map(([k, v]) => `<option value="${k}" ${k === tema ? "selected" : ""}>${esc(v)}</option>`).join("")}</select></label></form>
      ${tabellaObiettivi(lista, true)}
      ${D.lezioni ? `<details class="richiudibile sezione" data-md-testo="${esc(D.lezioni)}"><summary>${icona("lightbulb")}Lezioni apprese<span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo md"></div></details>` : ""}`;
  }
  function diario(data) {
    const B = D.bollettini || [];
    const sel = B.find((b) => b.data === data) || B[0];
    return `${schedeDati("diario")}
      <p class="risposta">Ogni giorno la sentinella scarica i dati ufficiali, ricalcola il programma e scrive un bollettino.</p>
      ${sel ? `<div class="diario"><nav aria-label="Bollettini"><ul class="elenco">${B.map((b) => `<li><a href="#/dati/diario/${b.data}" ${b === sel ? 'aria-current="page"' : ""}>${dataLunga(b.data)}</a></li>`).join("")}</ul></nav>
        <div class="card md documento">${md(sel.testo)}</div></div>` : vuoto("Nessun bollettino ancora.")}`;
  }

  // ---------- Controlli ----------
  const schedeControlli = (k) => `<h1>Controlli</h1><p class="nota" style="margin:0">Prima i vincoli, poi i valori: Costituzione, diritto europeo e integrità non si pesano, si rispettano.</p>${schede([["costituzione", "Costituzione", "#/controlli/costituzione"], ["europa", "Europa", "#/controlli/europa"], ["integrita", "Integrità", "#/controlli/integrita"]], k)}`;
  const AVVERTENZA_COST = `<div class="avviso info"><div class="avviso-titolo">${icona("info")}Controllo preventivo automatico con revisione umana.</div><p>Non è un giudizio: sulla legittimità delle leggi decide solo la Corte costituzionale.</p></div>`;
  function barraRischio(s) {
    const nessuno = s.articoli - s.alto - s.medio;
    return `<div class="barra-rischio" aria-hidden="true"><span style="flex:${nessuno};background:var(--c-favorevole)"></span><span style="flex:${s.medio};background:var(--c-attenzione)"></span><span style="flex:${s.alto};background:var(--c-alto)"></span></div>
      <div class="chips">${chip(["favorevole", "circle-check", `Nessun rilievo ${nessuno}`])}${chip(["attenzione", "circle-alert", `Attenzione ${s.medio}`])}${chip(["alto", "triangle-alert", `Rischio alto ${s.alto}`])}${chip(["critico", "octagon-x", "Critico 0"])}</div>`;
  }
  const NOMI_ESAMI = { AC3174_manovra_2027: "A.C. 3174 · Disegno di legge di bilancio 2027-2029", governai_conti_2027_2029: "Le decisioni di GovernAI sui conti 2027-2029" };
  function costituzioneVista(esame) {
    const C = D.costituzione || {};
    if (esame) {
      const e = (C.esami || []).find((x) => x.id === esame);
      if (!e) return nonTrovato(`Nessun esame «${esame}».`);
      return `<nav class="briciole" aria-label="Briciole di pane"><a href="#/controlli">Controlli</a><span aria-hidden="true">›</span><a href="#/controlli/costituzione">Costituzione</a><span aria-hidden="true">›</span><span aria-current="page">${esc(NOMI_ESAMI[e.id] || e.id)}</span></nav>
        ${AVVERTENZA_COST}<div class="md documento sezione" style="margin-top:24px">${md(e.testo)}</div><div class="azioni" style="margin-top:24px">${azioniCondividi()}</div>`;
    }
    const cos = D.proposte.flatMap((p) => (p.giuridico || []).filter((r) => r.ambito === "COS" && r.tipo === "proposta"));
    const conta = cos.reduce((a, r) => (a[r.esito] = (a[r.esito] || 0) + 1, a), {});
    return `${schedeControlli("costituzione")}
      ${AVVERTENZA_COST}
      ${(C.screening || []).map((s) => { const e = (C.esami || []).find((x) => x.id.startsWith(s.id + "_")); return `<section class="sezione card"><p class="etichetta">Leggi e manovre</p><h2>${esc(e ? NOMI_ESAMI[e.id] || e.id : s.id)}</h2>
        <p class="nota">Screening automatico di ${s.articoli} articoli; l'esame approfondito ne verifica i segnali con la giurisprudenza.</p>${barraRischio(s)}
        ${e ? `<p style="margin-top:12px"><a class="btn" href="#/controlli/costituzione/${esc(e.id)}">Leggi l'esame approfondito ${icona("arrow-right")}</a></p>` : ""}</section>`; }).join("")}
      <section class="sezione"><div class="sezione-testa"><h2>Le proposte di GovernAI</h2></div>
        <p>Controllo costituzionale delle ${cos.length} proposte del programma:</p>
        <div class="chips">${Object.entries(conta).map(([k, v]) => chip((ESITO_GIUR[k] || ["", "circle-dashed", k]).slice(0, 2).concat(`${(ESITO_GIUR[k] || [0, 0, k])[2]} ${v}`))).join("")}</div>
        <div class="griglia g2-d" style="margin-top:16px">${(C.esami || []).map((e) => `<a class="card" href="#/controlli/costituzione/${esc(e.id)}"><p class="etichetta">Esame approfondito</p><h3 class="titolo-card">${esc(NOMI_ESAMI[e.id] || e.id)}</h3><p class="nota">${esc(piano((e.testo.match(/^\*([^*]+)\*/m) || [])[1] || "").slice(0, 180))}…</p></a>`).join("")}</div></section>
      ${(C.gu_alti || []).length ? `<section class="sezione"><div class="sezione-testa"><h2>Gazzetta Ufficiale: atti con segnali alti</h2></div><ul class="mandati">${C.gu_alti.map((g) => `<li><span class="mono nota">${esc(g.codice)} · GU ${dataBreve(g.data_gu)}</span><br>${esc(g.titolo)}<div class="chips" style="margin-top:4px">${chip(["alto", "triangle-alert", `Segnali alti: art. ${(g.alto || []).join(", ")}`])}${(g.medio || []).length ? chip(["attenzione", "circle-alert", `Attenzione: art. ${g.medio.join(", ")}`]) : ""}</div></li>`).join("")}</ul></section>` : ""}
      <p class="nota sezione">${C.pronunce_verificate || 0} pronunce della Corte costituzionale verificate sui dati aperti ufficiali e usate negli esami.</p>`;
  }
  function europaVista(sotto, params) {
    const E = D.europa || {}, st = E.stato || {}, tot = st.totali || {};
    const entro60 = FUTURE.filter((s) => traGiorni(s.data) <= 60);
    const scadute = SCADENZE.filter((s) => s.data < OGGI);
    const inf = E.infrazioni || [];
    const sentenza = inf.filter((x) => /Sentenza/.test(x.fase)).length;
    const pde = (st.semestre || {}).procedura_disavanzo || "";
    const pdeChip = /sospes/i.test(pde) ? chip(["attenzione", "circle-pause", "Sospesa"]) : /chius|abrogat/i.test(pde) ? chip(["favorevole", "circle-check", "Chiusa"]) : chip(["alto", "triangle-alert", "In corso"]);
    const tab = sotto || "scadenze";
    const testa = `${schedeControlli("europa")}
      <p class="risposta">Nei prossimi 60 giorni scadono ${entro60.length} obblighi di recepimento. Infrazioni aperte: ${tot.infrazioni_aperte ?? inf.length}. Procedura per disavanzo eccessivo: ${esc(pde.replace(/^procedura per disavanzo eccessivo\s*/i, "") || "—")}.</p>
      <div class="griglia g2 g4-d">
        <div class="card kpi"><p class="etichetta">In scadenza entro 60 giorni</p><p class="numero">${entro60.length}</p><p class="nota">${entro60.filter((s) => /nessuna misura/.test(s.stato)).length} senza misure italiane notificate</p></div>
        <div class="card kpi"><p class="etichetta">Già scadute</p><p class="numero">${scadute.length}</p><p class="nota">${scadute.filter((s) => /completezza non verificata/.test(s.stato)).length} con completezza da verificare</p></div>
        <div class="card kpi"><p class="etichetta">Infrazioni aperte</p><p class="numero">${tot.infrazioni_aperte ?? inf.length}</p><p class="nota">${sentenza} arrivate a sentenza</p></div>
        <div class="card kpi"><p class="etichetta">Disavanzo eccessivo</p><p style="margin:8px 0">${pdeChip}</p><p class="nota">${esc(pde)}</p></div>
      </div>
      <nav class="schede" aria-label="Sezioni Europa" style="margin-top:24px">${[["scadenze", "Scadenze", tot.scadenze], ["infrazioni", "Infrazioni", inf.length], ["semestre", "Semestre europeo"]].map(([k, t, c]) => `<a href="#/controlli/europa${k === "scadenze" ? "" : "/" + k}" ${k === tab ? 'aria-current="page"' : ""}>${t}${c != null ? ` <span class="conta">${c}</span>` : ""}</a>`).join("")}</nav>`;
    const fonti = `<p class="nota sezione">Fonti: EUR-Lex e CELLAR (Ufficio delle pubblicazioni dell'UE), EUR-Infra (Dipartimento per le politiche europee), Commissione europea. Aggiornato ${del_(st.aggiornato || OGGI)}; ${tot.novita_30g ?? 0} atti europei nuovi negli ultimi 30 giorni.</p>`;
    if (tab === "infrazioni") {
      const FASI = [["Messa in mora", /^Messa in mora (complementare )?Art\. 258/], ["Parere motivato", /^Parere motivato/], ["Ricorso", /^Ricorso Art\. 258/], ["Sentenza", /^Sentenza Art\. 258/], ["Messa in mora art. 260", /^Messa in mora Art\. 260/], ["Ricorso o sentenza art. 260", /Art\. 260/]];
      const conteggi = FASI.map(([n, re], i) => [n, inf.filter((x) => re.test(x.fase) && (i < 5 || !/^Messa in mora Art\. 260/.test(x.fase))).length]);
      const max = Math.max(...conteggi.map((x) => x[1]), 1);
      const area = params.get("tema") || "";
      const lista = inf.filter((x) => !area || String(x.aree).split(",").includes(area));
      return `${testa}
        <section><div class="sezione-testa"><h2>Fasi delle procedure</h2></div><div class="fasi">${conteggi.map(([n, c], i) => `<div class="fase"><p class="nota" style="margin:0;min-height:40px">${esc(n)}${i < conteggi.length - 1 ? " →" : ""}</p><div class="traccia" aria-hidden="true"><span style="width:${c / max * 100}%"></span></div><b>${c}</b></div>`).join("")}</div></section>
        <section class="sezione"><div class="sezione-testa"><h2>Elenco delle procedure</h2></div>
        <form class="filtri-barra" onsubmit="return false"><label class="campo">Tema<select id="i-tema"><option value="">Tutti i temi</option>${Object.entries(D.aree).map(([k, v]) => `<option value="${k}" ${k === area ? "selected" : ""}>${esc(v)}</option>`).join("")}</select></label></form>
        <div class="tabella-box"><table class="tabella a-card"><thead><tr><th>Oggetto</th><th>Materia</th><th>Fase</th></tr></thead><tbody>${lista.map((x) => `<tr><td class="principale"><span class="mono nota">${esc(x.numero.replace("_", "/"))}</span><br>${esc(x.oggetto)}</td><td data-etichetta="Materia">${esc(x.materia)}</td><td data-etichetta="Fase">${chip(/Sentenza|260/.test(x.fase) ? ["critico", "octagon-x", x.fase] : /Parere|Ricorso/.test(x.fase) ? ["alto", "triangle-alert", x.fase] : ["attenzione", "circle-alert", x.fase])}</td></tr>`).join("") || `<tr><td colspan="3" class="vuoto">Nessuna procedura per questo tema.</td></tr>`}</tbody></table></div></section>${fonti}`;
    }
    if (tab === "semestre") return `${testa}<div class="md documento">${md(E.semestre_md || "*Non disponibile.*")}</div>${fonti}`;
    const prossimi90 = FUTURE.filter((s) => traGiorni(s.data) <= 90);
    const pr = params.get("priorita") || "";
    const perMese = {};
    FUTURE.filter((s) => !pr || s.pr === pr).forEach((s) => { const k = s.data.slice(0, 7); (perMese[k] = perMese[k] || []).push(s); });
    return `${testa}
      <section><div class="sezione-testa"><h2>Prossimi 90 giorni</h2></div>
        <ol class="linea-tempo">${prossimi90.map((s) => `<li class="${esc(s.pr)}"><time datetime="${s.data}">${dataBreve(s.data)}</time>${esc(s.atto)}<br><span class="nota">${esc(s.breve.slice(0, 60))}${s.breve.length > 60 ? "…" : ""}</span></li>`).join("") || "<li>Nessuna scadenza.</li>"}</ol></section>
      <section class="sezione"><div class="sezione-testa"><h2>Obblighi in arrivo</h2></div>
        <div class="segmenti" role="group" aria-label="Priorità">${[["", "Tutte"], ["critica", "Critica"], ["alta", "Alta"], ["media", "Media"]].map(([k, t]) => `<a class="btn s ${k === pr ? "primario" : ""}" href="#/controlli/europa${k ? "?priorita=" + k : ""}">${t}</a>`).join("")}</div>
        ${Object.entries(perMese).map(([k, l]) => `<h3 class="etichetta" style="margin-top:24px">${MESI_LUNGHI[+k.slice(5) - 1]} ${k.slice(0, 4)}</h3><div class="card" style="padding-top:4px;padding-bottom:4px"><ul class="scadenze">${l.map(rigaScadenza).join("")}</ul></div>`).join("") || vuoto("Nessun obbligo con questa priorità.")}
      </section>
      <details class="richiudibile sezione"><summary>${icona("history")}Termini già scaduti <span class="conta">${scadute.length}</span><span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo"><ul class="scadenze">${scadute.slice().reverse().map(rigaScadenza).join("")}</ul></div></details>
      ${fonti}`;
  }
  function integritaVista() {
    const g = D.integrita || { anelli: 0, errori: [], ultimi: [] };
    const ok = !g.errori.length;
    return `${schedeControlli("integrita")}
      <p class="risposta">Ogni esecuzione aggiunge un anello a una catena di impronte crittografiche (SHA-256). Le impronte coprono regole, dati in ingresso e risultati, e ogni anello contiene l'impronta del precedente: cambiare di nascosto qualcosa nel passato spezza la catena.</p>
      <div class="griglia g2 g4-d">
        <div class="card kpi"><p class="etichetta">Stato della catena</p><p style="margin:8px 0">${ok ? chip(["favorevole", "circle-check", "Integra"]) : chip(["critico", "octagon-x", "Problemi"])}</p><p class="nota">${ok ? "nessuna manomissione rilevata" : esc(g.errori.join("; "))}</p></div>
        <div class="card kpi"><p class="etichetta">Anelli registrati</p><p class="numero">${g.anelli}</p></div>
        <div class="card kpi" style="grid-column:span 2"><p class="etichetta">Verifica indipendente</p><p class="nota">Chiunque può ricontrollare la catena con <code>python integrita/catena.py --verifica</code>. Git aggiunge una seconda catena, con autore e data di ogni modifica.</p></div>
      </div>
      <section class="sezione"><div class="sezione-testa"><h2>Ultimi anelli</h2></div>
      <div class="tabella-box"><table class="tabella a-card"><thead><tr><th>#</th><th>Data (UTC)</th><th>Evento</th><th>Impronta</th><th>Regole cambiate</th></tr></thead><tbody>
        ${g.ultimi.map((x) => `<tr><td class="principale">Anello ${x.n}</td><td data-etichetta="Data">${esc((x.data || "").replace("T", " ").slice(0, 16))}</td><td data-etichetta="Evento">${esc(x.evento)} <span class="nota">${esc(x.nota || "")}</span></td>
          <td data-etichetta="Impronta"><span class="impronta" title="${esc(x.hash)}">${esc((x.hash || "").slice(0, 16))}…</span></td><td data-etichetta="Regole cambiate">${x.n === 0 ? "genesi" : (x.regole_cambiate || []).map((r) => `<span class="mono nota">${esc(r)}</span>`).join("<br>") || "—"}</td></tr>`).join("")}
      </tbody></table></div></section>`;
  }

  // ---------- Metodo ----------
  const DOCUMENTI = { programma: "Programma", metodo: "Metodo degli agenti", sistema: "Sistema dinamico", giuridico: "Quadro giuridico e UE", trasparenza: "Rischio negli appalti", legislazione: "Legislazione e redazione" };
  const schedeMetodo = (k) => `<h1>Metodo</h1>${schede([["come", "Come funziona", "#/metodo"], ["carta", "Carta dei valori", "#/metodo/carta"], ["documenti", "Documenti", "#/metodo/documenti"], ["glossario", "Glossario", "#/metodo/glossario"]], k)}`;
  function metodo() {
    const n = D.numeri || {};
    const passi = [
      ["Dati ufficiali, ogni giorno", "Una sentinella controlla Eurostat, ISTAT, MEF, Banca d'Italia, UPB e altre fonti, scarica solo ciò che è cambiato e ne conserva la storia."],
      ["Valori dichiarati", `Una Carta di ${n.valori || 10} valori, dal rispetto delle diversità alla responsabilità verso il futuro. Nessuna etichetta di destra, di sinistra o di centro.`],
      ["Panel indipendente", "Tre valutatori, che non hanno scritto le proposte, danno un punteggio a ogni misura su ogni valore. Il loro disaccordo diventa incertezza dichiarata."],
      ["Robustezza, non un peso unico", "Il motore prova migliaia di combinazioni di pesi e separa ciò che conviene con quasi tutti i pesi da ciò che è una scelta politica."],
      ["Senza deficit", "Ogni misura preleva da coperture concrete: un registro unico impedisce di contare due volte gli stessi soldi."],
      ["Controlli che non si pesano", "Costituzione, diritto europeo e linee rosse sono verificati prima di ogni decisione. Il governo ombra decide solo dentro questi limiti."],
      ["Verificabile e capace di imparare", "Ogni esecuzione aggiunge un anello alla catena di integrità. Ogni misura ha obiettivi misurabili: quando i risultati si discostano, il sistema ricalibra."],
    ];
    return `${schedeMetodo("come")}
      <p class="risposta">GovernAI è un prototipo: agenti di intelligenza artificiale analizzano i problemi del Paese, propongono opzioni con costi e coperture e rendono espliciti i compromessi. <strong>Le decisioni restano alle persone.</strong></p>
      <ol class="passi sezione">${passi.map(([t, d]) => `<li><strong>${esc(t)}</strong><span>${esc(d)}</span></li>`).join("")}</ol>
      <section class="sezione"><div class="sezione-testa"><h2>Limiti dichiarati</h2></div>
        <ul class="mandati"><li>Le stime di costo sono stime GovernAI: nessuna è certificata dalla Ragioneria generale dello Stato.</li><li>Il governo ombra è una simulazione con agenti AI: le sue decisioni non sono in vigore e non rappresentano persone reali.</li><li>Il controllo costituzionale è preventivo e automatico, con revisione umana: non sostituisce la Corte costituzionale.</li><li>Alcuni dati sono provvisori e possono essere rivisti dalla fonte.</li></ul></section>`;
  }
  function carta() {
    return `${schedeMetodo("carta")}
      <p class="risposta">I ${D.valori.length} valori della Carta sono il metro con cui si valutano tutte le proposte. Non hanno un peso fisso: il motore prova migliaia di combinazioni.</p>
      <div class="carta">${D.valori.map((v) => `<article class="card" id="${esc(v.id)}"><h3><code>${esc(v.id)}</code> ${esc(v.nome)}</h3><div class="md nota">${md(String(v.definizione || "").split("\n\n")[0])}</div></article>`).join("")}</div>
      <details class="richiudibile sezione" data-md-testo="${esc(D.documenti.carta || "")}"><summary>${icona("scroll-text")}Testo completo della Carta<span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo md"></div></details>`;
  }
  function documenti(doc) {
    const k = DOCUMENTI[doc] ? doc : "programma";
    return `${schedeMetodo("documenti")}
      <div class="segmenti" role="group" aria-label="Documento">${Object.entries(DOCUMENTI).map(([id, t]) => `<a class="btn s ${id === k ? "primario" : ""}" href="#/metodo/documenti/${id}" ${id === k ? 'aria-current="page"' : ""}>${esc(t)}</a>`).join("")}</div>
      <div class="md documento sezione">${md(D.documenti[k] || "*Documento non ancora disponibile.*")}</div>`;
  }
  function glossario() {
    const voci = [["A.C.", "Atto della Camera: numero con cui la Camera dei deputati identifica un progetto di legge."], ["AI", "Intelligenza artificiale."], ["Brier (punteggio di)", "Misura la qualità delle previsioni: 0 è perfetta, 0,25 come tirare a caso, 1 sempre sbagliata."], ["Catena di integrità", "Registro di impronte crittografiche: ogni anello contiene l'impronta del precedente, così una modifica nascosta si vede."], ["CELEX", "Codice che identifica un atto nella banca dati del diritto europeo EUR-Lex."], ["Deroga", "Decisione del capo di governo che si discosta dall'esito del motore, sempre dichiarata e motivata."], ["Governo ombra", "Simulazione di un Consiglio dei ministri fatto di agenti AI con ruoli distinti. Le decisioni non sono in vigore."], ["HICP", "Indice armonizzato dei prezzi al consumo, misura europea dell'inflazione."], ["ISTAT", "Istituto nazionale di statistica."],["Linea rossa", "Limite della Carta che nessuna proposta può superare: se lo supera, è esclusa automaticamente."], ["Mandato", "Compito con scadenza affidato a un ministro dal Consiglio."], ["MEF", "Ministero dell'economia e delle finanze."], ["NEET", "Giovani che non lavorano, non studiano e non seguono una formazione."],["Nucleo robusto", "Proposte che restano nella prima metà della classifica con quasi ogni combinazione di pesi tra i valori."], ["Opposizione leale", "Ruolo che cerca il punto debole di ogni decisione, con prove; il capo di governo deve rispondere per iscritto."], ["PIL", "Prodotto interno lordo."], ["RGS", "Ragioneria generale dello Stato."], ["Spread", "Differenza di rendimento tra titoli di Stato italiani e tedeschi a 10 anni, in punti base."], ["Stima GovernAI", "Cifra calcolata dal modello, non certificata dalla Ragioneria."], ["UE", "Unione europea."], ["UPB", "Ufficio parlamentare di bilancio."], ["Variante", "La dose di una misura: Piena, Essenziale, Pilota o Zero."]];
    return `${schedeMetodo("glossario")}<div class="obiezione card"><dl>${voci.map(([t, d]) => `<dt>${esc(t)}</dt><dd>${esc(d)}</dd>`).join("")}</dl></div>`;
  }

  // ---------- Partecipa ----------
  function partecipa(id) {
    const A = D.analisi || [];
    const sel = A.find((x) => x.id === id);
    const nuovoFile = (cartella, nome, testo) => `${repo}/new/main/${cartella}?filename=${encodeURIComponent(OGGI + "-" + nome + ".md")}&value=${encodeURIComponent(testo)}`;
    if (sel) return `<nav class="briciole" aria-label="Briciole di pane"><a href="#/partecipa">Partecipa</a><span aria-hidden="true">›</span><span aria-current="page">Analisi</span></nav><div class="md documento card">${md(sel.testo)}</div>`;
    return `<h1>Partecipa</h1>
      <p class="risposta">GovernAI è un progetto aperto a scopo sociale. Il modo principale per partecipare è la <a href="#/comunita">comunità su invito</a>: si discutono le proposte, si prendono appunti, si confrontano idee con le altre persone e con l'AI. Chi ha un account GitHub può anche proporre analisi e segnalare errori direttamente nel repository.</p>
      <div class="card comunita-porta sezione"><p>${icona("messages-square")} <strong>Comunità:</strong> aperta a ogni cittadino curioso, su invito, con regole pubbliche e moderazione registrata.</p><div class="azioni"><a class="btn primario s" href="#/comunita">Vai alla comunità</a><a class="btn s" href="#/comunita/richiedi">Chiedi un invito</a></div></div>
      <h2 class="sezione">Con un account GitHub</h2>
      <div class="griglia g3-d">
        <div class="card"><h2 style="font-size:20px">${icona("lightbulb")} Proponi un'idea</h2><p>Descrivi un problema o una proposta. GovernAI risponde con una diagnosi e tre opzioni, valutate sui valori della Carta con costi e coperture.</p><a class="btn primario" href="${repo}/issues/new?template=analisi.yml" target="_blank" rel="noopener">Proponi un'idea<span class="vh"> (si apre in una nuova scheda)</span></a></div>
        <div class="card"><h2 style="font-size:20px">${icona("message-circle-question")} Fai una domanda al Consiglio</h2><p>Il governo ombra si riunisce sulla tua domanda, con esperti, ministri e opposizione leale.</p><a class="btn" href="${esc(linkConsiglio())}" target="_blank" rel="noopener">Fai una domanda<span class="vh"> (si apre in una nuova scheda)</span></a></div>
        <div class="card"><h2 style="font-size:20px">${icona("flag")} Segnala un errore</h2><p>Un numero che non torna, una fonte sbagliata, un testo poco chiaro: ogni pagina ha il suo link per segnalarlo.</p><a class="btn" href="${repo}/issues/new" target="_blank" rel="noopener">Segnala un errore<span class="vh"> (si apre in una nuova scheda)</span></a></div>
      </div>
      <section class="sezione"><div class="sezione-testa"><h2>Richieste e analisi</h2></div>
        ${A.length ? `<ul class="risultati">${A.map((x) => `<li><a href="#/partecipa/${encodeURIComponent(x.id)}"><strong>${esc(x.titolo)}</strong><small>${dataBreve(x.id.slice(0, 10))}${x.issue ? " · richiesta n. " + esc(x.issue) : ""}</small></a></li>`).join("")}</ul>` : `<p class="nota">Nessuna analisi pubblicata ancora: la prima la avvii tu.</p>`}</section>
      <details class="richiudibile sezione"><summary>${icona("key-round")}Per i membri del progetto<span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo">
        <p>I membri del progetto possono scrivere direttamente un file di richiesta, senza passare dall'approvazione.</p>
        <div class="azioni"><a class="btn s" href="${esc(nuovoFile("governo/richieste", "domanda", "# Titolo della domanda\n\n**Domanda:** \n\n**Perché ora:** \n\n**Vincoli o attenzioni:** \n\nMinistri: \n"))}" target="_blank" rel="noopener">Convoca il Consiglio</a><a class="btn s" href="${esc(nuovoFile("analisi/richieste", "nuova-richiesta", "# Titolo del problema\n\n### Problema\n\n### Obiettivo\n\n### Area principale\n\n### Vincoli o attenzioni\n"))}" target="_blank" rel="noopener">Richiesta di analisi diretta</a><a class="btn s" href="#/governo/decisioni">Chiedi un riesame</a></div></div></details>`;
  }

  // ---------- Cerca ----------
  let INDICE = null;
  function indiceRicerca() {
    if (INDICE) return INDICE;
    INDICE = [
      ...D.proposte.map((p) => ({ tipo: "Proposta", t: `${tit(p.titolo)}`, s: `${p.id} · ${D.aree[p.area]}`, href: linkP(p.id), testo: (p.id + " " + p.titolo + " " + D.aree[p.area] + " " + piano(p.scheda)).toLowerCase() })),
      ...(D.indicatori || []).map((i) => ({ tipo: "Indicatore", t: nomeInd(i), s: `${valoreInd(i)} · ${periodoBreve(i.periodo)}`, href: "#/dati", testo: (i.nome + " " + i.id).toLowerCase() })),
      ...VERBALI.map((v) => ({ tipo: "Seduta", t: v.titolo, s: dataBreve(v.data), href: linkSeduta(v.id), testo: (v.titolo + " " + (v.domanda || "")).toLowerCase() })),
      ...SCADENZE.map((s) => ({ tipo: "Obbligo UE", t: s.breve, s: `${s.atto} · ${dataBreve(s.data)}`, href: "#/controlli/europa", testo: (s.titolo + " " + s.celex).toLowerCase() })),
      ...D.coperture.map((c) => ({ tipo: "Copertura", t: c.descrizione, s: c.misura_id, href: "#/programma/coperture", testo: (c.misura_id + " " + c.descrizione).toLowerCase() })),
      ...D.valori.map((v) => ({ tipo: "Valore", t: v.nome, s: v.id, href: `#/metodo/carta`, testo: (v.id + " " + v.nome + " " + v.definizione).toLowerCase() })),
    ];
    return INDICE;
  }
  function cerca(params) {
    return `<h1>Cerca</h1><form class="cerca-campo" role="search" onsubmit="return false"><label for="q" class="vh">Cerca in GovernAI</label><input id="q" type="search" value="${esc(params.get("q") || "")}" placeholder="Proposte, indicatori, sedute, direttive…" autocomplete="off"></form>
      <p class="nota" id="q-conta" role="status" aria-live="polite"></p><ul class="risultati" id="q-risultati"></ul>`;
  }
  function aggiornaRicerca() {
    const q = $("#q").value.trim().toLowerCase();
    history.replaceState(null, "", "#/cerca" + (q ? "?q=" + encodeURIComponent(q) : ""));
    if (q.length < 2) { $("#q-risultati").innerHTML = ""; $("#q-conta").textContent = "Scrivi almeno due lettere."; return; }
    const parole = q.split(/\s+/);
    const r = indiceRicerca().filter((x) => parole.every((p) => x.testo.includes(p))).slice(0, 40);
    $("#q-conta").textContent = !r.length ? "Nessun risultato." : r.length === 1 ? "1 risultato" : `${r.length}${r.length === 40 ? "+" : ""} risultati`;
    $("#q-risultati").innerHTML = r.map((x) => `<li><a href="${x.href}"><span class="etichetta">${esc(x.tipo)}</span><strong>${esc(x.t)}</strong><small>${esc(x.s)}</small></a></li>`).join("");
  }

  function nonTrovato(msg) { return `<div class="vuoto">${icona("search-x")}<h1 style="font-size:28px;margin-top:12px">Pagina non trovata</h1><p>${esc(msg)}</p><a class="btn primario" href="#/">Torna a Oggi</a></div>`; }

  // ---------- instradamento ----------
  const VECCHI = { racconto: "/", cruscotto: "/dati", programma: "/programma", governo: "/governo", valori: "/programma/valori", obiettivi: "/dati/obiettivi", analisi: "/partecipa", coperture: "/programma/coperture", bollettini: "/dati/diario", integrita: "/controlli/integrita", metodo: "/metodo" };
  function vista() {
    const vecchio = location.hash.match(/^#([a-z]+)$/);
    if (vecchio && VECCHI[vecchio[1]]) { history.replaceState(null, "", "#" + VECCHI[vecchio[1]]); }
    const [percorso, query] = (location.hash.slice(1) || "/").split("?");
    const parti = percorso.split("/").filter(Boolean).map(decodeURIComponent);
    const params = new URLSearchParams(query || "");
    const [a, b, c] = parti;
    let html, titolo;
    if (!a) { html = home(); titolo = "Oggi"; }
    else if (a === "programma") {
      if (b && /^\d{2}-[PC]\d+$/.test(b)) { html = schedaProposta(b); titolo = tit((proposta(b) || {}).titolo || "Proposta"); }
      else if (b === "coperture") { html = coperture(); titolo = "Come si paga"; }
      else if (b === "valori") { html = simulatore(); titolo = "I tuoi valori"; }
      else if (b === "confronti") { html = confronti(params); titolo = "Confronti"; }
      else if (b === "sintesi") { html = sintesi(); titolo = "Le idee in sintesi"; }
      else if (b === "equita") { html = equita(); titolo = "Equità e linguaggio inclusivo"; }
      else if (b === "una-pagina") { html = unaPagina(params); titolo = "Il programma in una pagina"; }
      else { html = elenco(params); titolo = "Programma"; }
    } else if (a === "governo") {
      if (b === "sedute" && c) { html = schedaSeduta(c); titolo = "Seduta " + del_(c); }
      else if (b === "decisioni") { html = decisioniInVigore(); titolo = "Decisioni in vigore"; }
      else if (b === "mandati") { html = mandatiVista(); titolo = "Mandati"; }
      else if (b === "credibilita") { html = credibilita(); titolo = "Credibilità"; }
      else if (b === "regolamento") { html = regolamento(); titolo = "Regolamento del Consiglio"; }
      else { html = governo(); titolo = "Governo"; }
    } else if (a === "dati") {
      if (b === "allerte") { html = allerteVista(); titolo = "Allerte"; }
      else if (b === "obiettivi") { html = obiettiviVista(params); titolo = "Obiettivi e risultati"; }
      else if (b === "diario") { html = diario(c); titolo = "Diario quotidiano"; }
      else { html = datiVista(); titolo = "Dati"; }
    } else if (a === "controlli") {
      if (b === "europa") { html = europaVista(c, params); titolo = "Europa"; }
      else if (b === "integrita") { html = integritaVista(); titolo = "Integrità"; }
      else { html = costituzioneVista(b === "costituzione" ? c : null); titolo = "Costituzione"; }
    } else if (a === "metodo") {
      if (b === "carta") { html = carta(); titolo = "Carta dei valori"; }
      else if (b === "documenti") { html = documenti(c); titolo = DOCUMENTI[c] || "Documenti"; }
      else if (b === "glossario") { html = glossario(); titolo = "Glossario"; }
      else { html = metodo(); titolo = "Metodo"; }
    } else if (a === "partecipa") { html = partecipa(b); titolo = "Partecipa"; }
    else if (a === "comunita" && C) { html = C.vista(b, c); titolo = { entra: "Entra", invito: "Iscrizione", richiedi: "Chiedi un invito", profilo: "Profilo", moderazione: "Moderazione", registro: "Registro della moderazione", regole: "Regole della comunità" }[b] || "Comunità"; }
    else if (a === "cerca") { html = cerca(params); titolo = "Cerca"; }
    else { html = nonTrovato("L'indirizzo non corrisponde a nessuna pagina."); titolo = "Pagina non trovata"; }
    const voce = !a ? "oggi" : a;
    main.innerHTML = html;
    if (C) C.monta(main);
    document.title = `${titolo} · GovernAI`;
    $$("[data-voce]").forEach((x) => { if (x.dataset.voce === voce) x.setAttribute("aria-current", "page"); else x.removeAttribute("aria-current"); });
    // comportamenti delle viste interattive
    if ($("#f-corpo")) { ["#f-cerca", "#f-tema", "#f-classe", "#f-incluse"].forEach((s) => $(s).addEventListener("input", aggiornaElenco)); aggiornaElenco(); }
    if ($("#c-corpo")) { const filtra = () => { const t = $("#c-cerca").value.toLowerCase(), f = $("#c-fondo").value, l = $("#c-livello").value; $$("#c-corpo tr").forEach((tr) => { tr.hidden = (t && !tr.dataset.testo.includes(t)) || (f && tr.dataset.fondo !== f) || (l && tr.dataset.livello !== l); }); }; ["#c-cerca", "#c-fondo", "#c-livello"].forEach((s) => $(s).addEventListener("input", filtra)); }
    if ($("#classifica")) { $$("input[type=range]", main).forEach((el) => el.addEventListener("input", aggiornaClassifica)); aggiornaClassifica(); }
    if ($("#q")) { $("#q").addEventListener("input", aggiornaRicerca); aggiornaRicerca(); $("#q").focus(); }
    if ($("#schema-scenario")) $("#schema-scenario").addEventListener("change", (e) => { location.hash = "#/programma/una-pagina" + (e.target.value === (D.schema || {}).scenario ? "" : "?scenario=" + e.target.value); });
    if ($("#o-tema")) $("#o-tema").addEventListener("change", (e) => { location.hash = "#/dati/obiettivi" + (e.target.value ? "?tema=" + e.target.value : ""); });
    if ($("#i-tema")) $("#i-tema").addEventListener("change", (e) => { location.hash = "#/controlli/europa/infrazioni" + (e.target.value ? "?tema=" + e.target.value : ""); });
    icone();
    osservaIndice();
  }
  function icone() {
    if (!window.lucide) return;
    lucide.createIcons();
    const scuro = document.documentElement.dataset.tema ? document.documentElement.dataset.tema === "scuro" : matchMedia("(prefers-color-scheme: dark)").matches;
    $$(".tema").forEach((t) => { t.setAttribute("aria-label", scuro ? "Attiva il tema chiaro" : "Attiva il tema scuro"); t.innerHTML = icona(scuro ? "sun" : "moon"); });
    lucide.createIcons();
  }

  // contenuti richiusi: si generano solo all'apertura (i verbali superano le 300 mila battute)
  main.addEventListener("toggle", (e) => {
    const d = e.target;
    if (!(d instanceof HTMLDetailsElement) || !d.open) return;
    const corpo = $(":scope > .corpo", d);
    if (!corpo || corpo.dataset.pronto || !corpo.classList.contains("md")) return;
    if (d.dataset.md === "scheda") { const p = proposta(decodeURIComponent(location.hash.split(/[/?]/)[2] || "")); corpo.innerHTML = md((p.scheda || "").replace(/^## .*\n/, "")); }
    else if (d.dataset.mdTesto != null) corpo.innerHTML = md(d.dataset.mdTesto);
    else if (d.dataset.sez) { const v = VERBALI.find((x) => x.id === decodeURIComponent(location.hash.split("/")[3] || "")); corpo.innerHTML = md(v[d.dataset.sez][+d.dataset.i].testo); }
    corpo.dataset.pronto = "1";
  }, true);

  // popover delle fonti, filtri, azioni
  let pop = null;
  const chiudiPop = () => { if (pop) { pop._da.setAttribute("aria-expanded", "false"); pop.remove(); pop = null; } };
  document.addEventListener("click", (e) => {
    const b = e.target.closest("[data-fonte]");
    if (b) {
      e.preventDefault(); const gia = pop && pop._da === b; chiudiPop(); if (gia) return;
      pop = document.createElement("div"); pop._da = b; pop.className = "popover"; pop.setAttribute("role", "dialog"); pop.setAttribute("aria-label", "Da dove viene questo numero");
      pop.innerHTML = `<strong>Da dove viene questo numero</strong>${esc(b.dataset.fonte)}${b.dataset.url ? `<br>${ext(b.dataset.url, "Apri la fonte")}` : ""}`;
      document.body.appendChild(pop);
      const r = b.getBoundingClientRect(), w = Math.min(320, innerWidth - 32);
      pop.style.width = w + "px"; pop.style.left = Math.max(16, Math.min(r.left + scrollX, innerWidth - w - 16)) + "px"; pop.style.top = (r.bottom + scrollY + 6) + "px";
      b.setAttribute("aria-expanded", "true"); icone(); return;
    }
    if (pop && !e.target.closest(".popover")) chiudiPop();
    const mi = e.target.closest("[data-ministero]");
    if (mi) { mappaSeleziona(mi.dataset.ministero, mi.classList.contains("mappa-vai")); return; }
    const f = e.target.closest("[data-filtro]");
    if (f) {
      $$("[data-filtro]").forEach((x) => x.setAttribute("aria-pressed", x === f));
      const tutte = f.dataset.filtro === "tutte"; let n = 0;
      $$(".decisioni > li").forEach((li) => { const ok = tutte || li.dataset.esito === f.dataset.filtro; li.hidden = !ok || (tutte && li.hasAttribute("data-oltre") && !main.dataset.tutte); if (!li.hidden) n++; });
      const altre = $(".altre"); if (altre) altre.hidden = !tutte || !!main.dataset.tutte;
      $("#esito-filtro").textContent = `${n} decisioni mostrate`;
    }
    const s = e.target.closest("[data-scenario]");
    if (s) { const pr = new URLSearchParams(location.hash.split("?")[1] || ""); pr.set("scenario", s.dataset.scenario); if (s.dataset.scenario === "momento") pr.delete("scenario"); location.hash = "#/programma" + (pr.toString() ? "?" + pr : ""); }
    const p = e.target.closest("[data-preset]");
    if (p) { D.valori.forEach((v) => { $("#w-" + v.id).value = p.dataset.preset === "uguali" ? 50 : v.id === p.dataset.preset ? 100 : 35; }); aggiornaClassifica(); }
    const a = e.target.closest("[data-azione]");
    if (!a) return;
    if (a.dataset.azione === "altre") { main.dataset.tutte = "1"; $$(".decisioni > li[data-oltre]").forEach((li) => li.hidden = false); a.closest(".altre").hidden = true; }
    if (a.dataset.azione === "tema") {
      e.preventDefault();
      const scuro = document.documentElement.dataset.tema ? document.documentElement.dataset.tema === "scuro" : matchMedia("(prefers-color-scheme: dark)").matches;
      document.documentElement.dataset.tema = scuro ? "chiaro" : "scuro";
      try { localStorage.setItem("governai-tema", document.documentElement.dataset.tema); } catch (err) { /* memoria non disponibile */ }
      icone();
    }
    if (a.dataset.azione === "copia") { try { navigator.clipboard.writeText(location.href); a.lastElementChild.textContent = "Link copiato"; } catch (err) { a.lastElementChild.textContent = location.href; } }
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && pop) { const b = pop._da; chiudiPop(); b.focus(); }
    if (e.key === "/" && !/input|textarea|select/i.test(document.activeElement.tagName) && !e.ctrlKey && !e.metaKey) { e.preventDefault(); location.hash = "#/cerca"; }
  });
  // ancore interne senza cambiare l'instradamento
  main.addEventListener("click", (e) => {
    const a = e.target.closest('a[href^="#"]:not([href^="#/"])');
    if (!a) return;
    e.preventDefault();
    const t = document.getElementById(a.getAttribute("href").slice(1));
    if (t) { t.scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth" }); t.setAttribute("tabindex", "-1"); t.focus({ preventScroll: true }); }
    const d = a.closest("details.indice-mobile"); if (d) d.open = false;
  });
  function osservaIndice() {
    const link = $$(".indice a[data-ancora]");
    if (!link.length || !("IntersectionObserver" in window)) return;
    const io = new IntersectionObserver((voci) => voci.forEach((v) => { if (v.isIntersecting) link.forEach((l) => l.classList.toggle("attivo", l.getAttribute("href") === "#" + v.target.id)); }), { rootMargin: "-90px 0px -65% 0px" });
    link.forEach((l) => { const t = document.getElementById(l.getAttribute("href").slice(1)); if (t) io.observe(t); });
  }

  $("#aggiornato").textContent = `Dati aggiornati al ${dataLunga(D.generato)}, ore ${String(D.generato).slice(11, 16)}.`;
  window.addEventListener("hashchange", () => { chiudiPop(); delete main.dataset.tutte; vista(); window.scrollTo(0, 0); if (!$("#q")) main.focus({ preventScroll: true }); });
  // marked, DOMPurify e Lucide arrivano dalla CDN: se sono lenti si ridisegna quando sono pronti
  window.addEventListener("load", () => { if (main.querySelector(".md:not(.corpo)")) vista(); else icone(); });
  vista();
})();
