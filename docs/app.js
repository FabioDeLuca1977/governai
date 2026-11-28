/* GovernAI · interfaccia web. Legge window.GOVERNAI (data.js, generato da sistema/esporta_web.py).
   Design: design/04_design_system.md; template scelto con il confronto in design/confronto/. */
(function () {
  "use strict";
  const D = window.GOVERNAI;
  const main = document.getElementById("contenuto");
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  // Costo annuo arrotondato: sotto il miliardo in milioni (multipli di 5), sopra con un decimale
  const euro = (x) => x == null ? "—" : !+x ? "costo zero" : x < 0.0475 ? `${Math.max(1, Math.round(x * 1000))} mln` : x < 0.9975 ? `${Math.round(x * 200) * 5} mln` : `${(+x).toLocaleString("it-IT", { minimumFractionDigits: 1, maximumFractionDigits: 1 })} mld`;
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
  // le stesse classi dette in parole semplici (testata e bilancio delle schede)
  const CLASSE_SEMPLICE = { "robusta": "Utile con quasi ogni peso dei valori", "dipendente dai valori": "Utile secondo i valori che contano di più", "in coda": "Utile solo con alcuni pesi dei valori", "sfavorevole": "Più costi che benefici" };
  const GIUR_SEMPLICE = { compatibile: "In regola con Costituzione e UE", condizionato: "Si può fare, con condizioni giuridiche", richiede_notifica: "Va comunicata prima alla Commissione UE", incompatibile: "Una versione non è ammessa" };
  const solidita = (r) => r >= 0.995 ? "resta nel programma in tutte le simulazioni" : r >= 0.9 ? "resta nel programma in quasi tutte le simulazioni" : `resta nel programma in ${Math.round(r * 100)} simulazioni su 100`;
  const GRAVITA_GIUR = { compatibile: 0, condizionato: 1, richiede_notifica: 1, incompatibile: 3 };
  const AMBITO = { FIS: "Fiscale", COS: "Costituzionale", UE: "Europeo" };
  const ESITO_DEC = { adottata: ["favorevole", "check", "Accolta"], respinta: ["alto", "x", "Respinta"], rinviata: ["", "calendar-clock", "Rinviata"] };
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
  const BADGE = { verificato: ["favorevole", "badge-check", "Verificato"], stima: ["info", "calculator", "Stima GovernAI"], verificare: ["attenzione", "circle-help", "Da verificare"], provvisorio: ["neutro", "hourglass", "Provvisorio"], fonte: ["neutro", "file-text", "Fonte"] };
  const badge = (tipo, fonte, url = "") => { const [c, i, t] = BADGE[tipo]; return `<button type="button" class="badge ${c}" data-fonte="${esc(fonte)}" ${url ? `data-url="${esc(url)}"` : ""} aria-haspopup="dialog">${icona(i)}<span>${t}</span></button>`; };
  const STIMA = "Stima GovernAI: calcolata dal modello, non certificata dalla Ragioneria generale dello Stato (RGS). Fonte: registro delle coperture e ottimizzatore del programma.";
  const md = (t) => window.marked && window.DOMPurify ? DOMPurify.sanitize(marked.parse(t || "")) : `<p>${esc(t)}</p>`;
  const proposta = (id) => D.proposte.find((p) => p.id === id);
  const scenario = (id) => D.scenari.find((s) => s.id === id) || D.scenari[0];
  const RIF_ID = (D.schema && D.schema.scenario) || "intermedio";
  const rif = scenario(RIF_ID); // versione di riferimento dei documenti: la stessa in ogni pagina
  // Da dove vengono i soldi: coperture nuove + risorse già stanziate nei fondi vincolati + tariffe (calcolato in sistema/esporta_web.py)
  const fontiSoldi = (sc) => [`${nf(sc.gettito, 1)} da coperture nuove`, ...(sc.gia_stanziati || []).map((f) => `${nf(f.mld, 1)} da ${f.nome} già stanziati${/2021-2027/.test(f.nome) ? " (fino al 2029)" : ""}`),
    ...(sc.tariffe ? [`${nf(sc.tariffe, 1)} da tariffe pagate da chi usa il servizio`] : [])].join(" + ") +
    (sc.risorse - sc.spesa > 0.05 ? ` (in tutto ${nf(sc.risorse, 1)} mld di risorse: ${nf(sc.risorse - sc.spesa, 1)} non sono spesi${sc.margine_generali > 0.005 ? `, di cui ${nf(sc.margine_generali, 2)} tenuti da parte` : ""}${sc.vincolati_non_usati > 0.005 ? ` e ${nf(sc.vincolati_non_usati, 2)} di fondi vincolati non spostabili` : ""})` : "");
  // Barre impilate sulla stessa scala: da dove vengono i soldi di ogni versione, con la spesa segnata da una linea
  function barreSoldi(scs, titolo = true) {
    const max = Math.max(...scs.map((x) => Math.max(x.risorse ?? x.gettito, x.spesa)));
    const parti = (x) => [["nuove", x.gettito, "coperture nuove"], ...(x.gia_stanziati || []).map((f) => ["stanziati", f.mld, `${f.nome} già stanziati`]), ...(x.tariffe ? [["tariffe", x.tariffe, "tariffe pagate da chi usa il servizio"]] : [])];
    const riga = (x) => { const tot = x.risorse ?? x.gettito; const desc = parti(x).map(([, v, t]) => `${nf(v, 1)} da ${t}`).join(", ");
      return `<div class="bs-riga"><span class="bs-nome">${esc(x.nome)}${x.id === RIF_ID ? ` <span class="nota">riferimento</span>` : ""}</span>
        <span class="bs-barra" role="img" aria-label="${esc(x.nome)}: ${nf(tot, 1)} mld di risorse (${esc(desc)}); spesa ${nf(x.spesa, 1)} mld">${parti(x).map(([k, v, t]) => `<span class="bs-${k}" style="width:${(v / max * 100).toFixed(2)}%" title="${esc(nf(v, 1) + " mld da " + t)}">${v / max > 0.1 ? nf(v, 1) : ""}</span>`).join("")}<span class="bs-spesa" style="left:${(x.spesa / max * 100).toFixed(2)}%" title="spesa ${nf(x.spesa, 1)} mld"></span></span>
        <span class="bs-tot">${nf(x.spesa, 1)} <span class="nota">spesa</span></span></div>`; };
    return `<div class="barre-soldi">${titolo ? `<p class="etichetta">Da dove vengono i soldi, in miliardi l'anno</p>` : ""}
      <p class="bs-legenda nota" aria-hidden="true"><span><i class="bs-nuove"></i>coperture nuove</span><span><i class="bs-stanziati"></i>fondi europei già stanziati</span><span><i class="bs-tariffe"></i>tariffe</span><span><i class="bs-linea"></i>spesa</span></p>
      ${scs.map(riga).join("")}</div>`;
  }
  const linkP = (id) => `#/programma/${encodeURIComponent(id)}`;
  const linkSeduta = (id) => `#/governo/sedute/${encodeURIComponent(id)}`;
  const codici = (s) => String(s || "").replace(/\b(\d{2}-[PC]\d{1,2})\b/g, (m) => proposta(m) ? `<a href="${linkP(m)}">${m}</a>` : m);
  const OGGI = String(D.generato).slice(0, 10);
  const traGiorni = (iso) => Math.round((new Date(iso + "T12:00") - new Date(OGGI + "T12:00")) / 864e5);
  const bannerSim = (tipo = "") => `<div class="banner-sim ${tipo}" role="note">${icona("flask-conical")}<span><strong>Governo ombra · simulazione:</strong> tutti i ruoli, capo di governo compreso, sono agenti AI. Nessuna decisione è in vigore e nessuna persona l'ha presa.</span></div>`;
  // testata delle sezioni: il titolo è il nome della pagina aperta, la sezione resta sopra come etichetta
  const schede = (voci, attiva, sez, nota = "") => `${sez ? `<p class="etichetta sez-etichetta">${esc(sez)}</p><h1>${esc((voci.find((v) => v[0] === attiva) || [])[1] || sez)}</h1>${nota}` : ""}<nav class="schede" aria-label="Sezioni">${voci.map(([k, t, href, conta]) => `<a href="${href}" ${k === attiva ? 'aria-current="page"' : ""}>${esc(t)}${conta != null ? ` <span class="conta">${conta}</span>` : ""}</a>`).join("")}</nav>`;
  const vuoto = (testo) => `<p class="vuoto">${esc(testo)}</p>`;
  const repo = D.repo || "https://github.com/FabioDeLuca1977/governai";
  const RAW = repo.replace("https://github.com/", "https://raw.githubusercontent.com/") + "/main/";
  const SCENARI_FILE = new Set(["intermedio", "momento", "dividendo", "difesa", "riferimento", "livello1", "livello2", "senza_tasse", "senza_tasse_istruzione"]);
  // «Scarica i dati»: i file del repository da cui viene la pagina, scaricabili così come sono
  const linkFile = (f) => `<a href="${esc(RAW + f)}" download>${esc(f.split("/").pop())}</a>`;
  const scaricaDati = (files) => { const l = [...new Set(files.filter(Boolean))]; return l.length ? `<p class="scarica-dati">${icona("download")}<span><strong>Scarica i dati:</strong> ${l.map(linkFile).join(" · ")}. <a href="${esc(repo)}/tree/main" target="_blank" rel="noopener">Tutto il repository</a>.</span></p>` : ""; };
  function fileDiPagina(a, b, params) {
    if (a === "programma") {
      const p = b && /^\d{2}-[PC]\d+$/.test(b) ? proposta(b) : null;
      if (p) return [p.file_varianti, "motore/proposte.csv", "motore/esito_proposte.csv", "motore/punteggi_A.csv", "motore/punteggi_B.csv", "motore/punteggi_C.csv", "giuridico/conformita.csv"];
      if (b === "coperture") return ["programma/coperture_menu.csv", "giuridico/conformita.csv"];
      if (b === "ai") return ["programma/ai_pagina.yaml", "dati/serie/09_personale_funzioni_centrali.csv"];
      if (b === "busta-paga") return ["programma/busta_paga.yaml", "analisi/chi_paga/parametri.yaml", "docs/busta.js"];
      const sc = params.get("scenario") || RIF_ID;
      if (b === "una-pagina") return ["programma/schema.yaml", SCENARI_FILE.has(sc) ? `programma/selezione_${sc}.csv` : ""];
      if (!b) return ["motore/proposte.csv", "motore/esito_proposte.csv", SCENARI_FILE.has(sc) ? `programma/selezione_${sc}.csv` : ""];
      return [];
    }
    if (a === "dati") {
      if (!b) return ["sistema/stato/indicatori.json", "sistema/config.yaml"];
      if (b === "allerte") return ["sistema/config.yaml", "sistema/stato/allerte.json"];
      if (b === "obiettivi") return ["apprendimento/obiettivi.yaml", "apprendimento/esiti.csv"];
      if (b === "storia") return ["storia/decisioni_1977_2026.csv", "storia/periodi.yaml"];
      if (b === "governi" || b === "verifica") return ["storia/governi_confronto.csv", "storia/legislature_confronto.csv", "storia/punti_di_vista.csv", "storia/punti_di_vista_ambiti.csv"];
      if (b === "fonti") return ["sistema/stato/fonti.json", "sistema/stato/ultima_sentinella.json"];
      return [];
    }
    if (a === "controlli" && b === "integrita") return ["integrita/catena.jsonl"];
    return [];
  }
  // Comunità su invito (comunita.js): il programma resta pubblico, la discussione è per le persone iscritte
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
      <div class="legenda"><span style="color:var(--c-favorevole)">${icona("circle-check")}<b>${a}</b> accolte</span><span style="color:var(--c-alto)">${icona("circle-x")}<b>${r}</b> respinte</span><span>${icona("clock")}<b>${v}</b> ${v === 1 ? "rinviata" : "rinviate"}</span></div></div>`;
  }
  function cardProposta(p, motivo = "", sc = rif) {
    const m = sc.misure[p.id];
    return `<a class="card card-proposta" href="${linkP(p.id)}">
      <div class="testa-card"><p class="etichetta">${esc(D.aree[p.area])} · ${esc(p.id)}</p></div>
      <h3 class="titolo-card">${esc(tit(p.titolo))}</h3>
      <div class="chips">${chipClasse(p.classe)}${p.linea_rossa ? chip(["critico", "octagon-x", "Linea rossa in alcune versioni"]) : ""}</div>
      <div class="riga-dati">${misuratore(m && m.variante)}${m ? `<span>${euro(m.costo)} l'anno</span>` : ""}${motivo ? `<span>${esc(motivo)}</span>` : ""}</div>
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
  // date accanto alla fonte: quando la fonte ha pubblicato il dato e quando lo abbiamo scaricato
  const datiFonte = (f) => !f ? "" : [f.aggiornato ? `aggiornata il ${dataBreve(f.aggiornato)}` : "", f.scaricato ? `scaricata il ${dataBreve(f.scaricato)}` : ""].filter(Boolean).map((x) => " · " + x).join("");
  function cardIndicatore(i) {
    return `<article class="card indicatore">
      <div class="sinistra"><h3>${esc(nomeInd(i))}</h3><p class="nota" style="margin:0">${esc(periodoBreve(i.periodo))} · ${esc(unitaInd(i))}</p></div>
      <div class="destra"><div class="riga"><span class="numero">${valoreInd(i)}${i.unita.startsWith("%") ? "%" : ""}</span>${badgeInd(i)}</div>${trend(i)}</div>
      ${sparkline(i)}
      <p class="fonte">Fonte: ${i.fonte && i.fonte.url ? ext(i.fonte.url, esc(i.fonte.fonte)) : esc((i.fonte || {}).fonte || "—")}${datiFonte(i.fonte)}${i.fonte && i.fonte.file ? ` · <a href="${esc(RAW + i.fonte.file)}" download>Scarica i dati</a>` : ""}</p>
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
  // Allerta in parole semplici, per la home: niente codici, solo misure del programma di riferimento
  function allertaHome(r) {
    const i = r.ind, titolo = String(r.messaggio).split(": ")[0].replace(/\.$/, "");
    const pr = (r.priorita || []).filter((c) => rif.misure[c] && proposta(c)).map((c) => `<a href="${linkP(c)}">${esc(tit(proposta(c).titolo))}</a>`);
    return `<li><p><strong>${esc(titolo)}</strong>${i.valore != null ? ` <span class="nota">(${esc(nomeInd(i))}: ${valoreInd(i)}${i.unita.startsWith("%") ? "%" : " " + esc(unitaInd(i))}, ${esc(periodoBreve(i.periodo))})</span>` : ""}</p>${pr.length ? `<p class="nota">Il programma dà la precedenza a: ${pr.join(" · ")}</p>` : ""}</li>`;
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
        <p class="nota" style="margin-top:-8px">Nove ministeri, i temi di cui si occupano e dove lavorano insieme o si contendono le risorse. Passa sopra un ministero per vedere i suoi collegamenti, sceglilo per approfondire.</p>
        <div class="mappa">
          <div class="mappa-rete" id="mappa-rete">
            <style>${perArea.map(([k]) => `.mappa-rete:not([data-sel]):has(.nodo[data-ministero="${k}"]:hover) line[data-a="${k}"],.mappa-rete:not([data-sel]):has(.nodo[data-ministero="${k}"]:hover) line[data-b="${k}"],.mappa-rete[data-sel=""]:has(.nodo[data-ministero="${k}"]:hover) line[data-a="${k}"],.mappa-rete[data-sel=""]:has(.nodo[data-ministero="${k}"]:hover) line[data-b="${k}"]{opacity:1;stroke-width:3.5}`).join("")}</style>
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

  // Calendario di avvio: la spesa sulle risorse generali segue il gettito di ogni anno, con un ponte di fondi UE nel 2027-29
  function calendarioAvvio(sc) {
    const c = sc.calendario || {};
    if (!(c.anni || []).length) return "";
    const pct = (x) => `${Math.round(x * 100)}%`;
    const nome = (id) => (D.proposte.find((p) => p.id === id) || {}).titolo || id;
    const gruppi = {};
    Object.entries(c.pieno_dal || {}).sort((a, b) => a[1] - b[1] || a[0].localeCompare(b[0])).forEach(([id, a]) => { (gruppi[a] = gruppi[a] || []).push(id); });
    const a1 = c.anni[0] || {}, a2 = c.anni[1] || {};
    const tab = `<div class="tabella-box"><table class="tabella"><thead><tr><th>Anno</th><th>Spesa prevista</th><th>Avviata</th><th>Rinviata</th><th>di cui nucleo</th><th>Riforme a costo quasi zero</th><th>Nucleo, sperimentazioni, 04-P8 e 06-C8</th><th>Altre misure</th></tr></thead><tbody>${c.anni.map((x) => `<tr><td>${x.anno}</td><td>${nf(x.prevista, 2)}</td><td>${nf(x.avviata, 2)}</td><td>${nf(x.rinviata, 2)}</td><td>${nf(x.rinviata_nucleo, 2)}</td><td>${pct(x.quota_riforme)}</td><td>${pct(x.quota_nucleo)}</td><td>${pct(x.quota_altre)}</td></tr>`).join("")}</tbody></table></div>`;
    return `<p><strong>Come si chiude: un calendario di avvio</strong> (scelte del 13 novembre 2026). Ogni anno la spesa sulle risorse generali non supera il gettito dell'anno, con l'ipotesi prudente, tenendo da parte i servizi per smettere di fumare dal 2028 e la riserva per il dopo 2029 dal 2030. I fondi europei 2021-2027 pagano solo spese una tantum, non spesa corrente.</p>
      <ul>
        <li><strong>Partono subito, per intero, le ${(c.riforme_subito || []).length} riforme a costo quasi zero</strong> (al massimo 20 milioni l'anno ciascuna).</li>
        <li><strong>Il ${a1.anno} è un anno di preparazione:</strong> quasi tutte le coperture rendono dal ${a2.anno}, quindi il nucleo robusto parte al ${pct(a1.quota_nucleo)} e arriva al ${pct(a2.quota_nucleo)} nel ${a2.anno}; è a pieno dal ${c.nucleo_pieno || "—"}.</li>
        ${Object.keys(c.pieno_dal || {}).length ? `<li><strong>Le altre misure partono dopo</strong>, tutte nello stesso modo.</li>` : `<li><strong>Non ci sono altre misure da rinviare:</strong> dopo la verifica delle coperture il programma contiene il nucleo, le sperimentazioni e le riforme a costo quasi zero.</li>`}
        <li>Negli anni di passaggio slittano ${nf(c.rinviata_totale, 1)} mld di spesa, <strong>di cui ${nf(c.rinviata_nucleo, 1)} del nucleo</strong>: nessun anno chiude in deficit, ma il programma arriva a regime più tardi.</li>
      </ul>
      <details><summary>Calendario anno per anno e misure che partono più tardi</summary>${tab}${Object.entries(gruppi).map(([a, ids]) => `<p><strong>A pieno dal ${a}:</strong> ${ids.map((id) => `<a href="#/programma/${encodeURIComponent(id)}">${esc(id)}</a> ${esc(nome(id))}${c.inizio && c.inizio[id] ? ` (comincia nel ${c.inizio[id]})` : ""}`).join("; ")}</p>`).join("")}</details>`;
  }

  // Conti anno per anno 2027-2035 (programma/annuale.py): il vincolo "senza deficit" vale a regime, qui si vede ogni anno
  function avvisoAnnuale(sc) {
    const a = sc.annuale || [];
    const neg = a.filter((x) => x.saldo < -0.005), negf = a.filter((x) => x.saldo_favorevole < -0.005);
    const segno = (x) => (x < -0.005 ? `<strong>${nf(x, 2)}</strong>` : nf(x, 2));
    const tab = `<div class="tabella-box"><table class="tabella"><thead><tr><th>Anno</th><th>Spesa</th><th>Risorse generali: spesa</th><th>Gettito</th><th>Saldo (prudente)</th><th>Saldo (favorevole)</th></tr></thead><tbody>${a.map((x) => `<tr><td>${x.anno}</td><td>${nf(x.spesa, 2)}</td><td>${nf(x.spesa_generali, 2)}</td><td>${nf(x.gettito_generali, 2)}</td><td>${segno(x.saldo)}</td><td>${segno(x.saldo_favorevole)}</td></tr>`).join("")}</tbody></table></div>`;
    const cal = (sc.calendario || {}).anni || [];
    const titolo = !neg.length ? "Anno per anno le risorse generali coprono la spesa." : cal.length ? `Anno per anno: senza calendario mancherebbero fino a ${nf(-Math.min(...neg.map((x) => x.saldo)), 1)} mld; con il calendario di avvio i conti tornano ogni anno.` : `Anno per anno i conti non tornano ancora: negli anni di passaggio mancano fino a ${nf(-Math.min(...neg.map((x) => x.saldo)), 1)} mld.`;
    return `<div class="avviso ${neg.length && !cal.length ? "attenzione" : ""}" style="margin-top:12px"><div class="avviso-titolo">${icona("calendar")}${titolo}</div>
      <p>"Senza deficit" è verificato a regime, quando tutte le coperture rendono a pieno. Alcune però crescono piano: il taglio graduale del gasolio agevolato per l'autotrasporto arriva al pieno in 8 anni, la rivalutazione ridotta delle pensioni più alte in 6. Intanto le spese partono prima. ${negf.length ? `Anche con l'ipotesi favorevole, coperture attive dal primo anno, restano scoperti ${negf.map((x) => x.anno).join(", ")}, per ${nf(-negf.reduce((t, x) => t + x.saldo_favorevole, 0), 1)} mld in tutto.` : ""}${cal.length ? "" : " Va deciso come chiudere questo scarto: è scritto tra le scelte aperte."}</p>
      ${calendarioAvvio(sc)}
      <details><summary>Tabella 2027-2035 senza calendario (mld di euro)</summary>${tab}<p class="nota">Stima di <code>programma/annuale.py</code>: spese anno per anno dalle varianti, coperture che crescono in modo lineare fino all'anno di regime. Da verificare con la Ragioneria.</p></details></div>`;
  }

  // Spesa pagata con la coesione 2021-2027: che cosa succede dopo il 2029, misura per misura
  function avvisoDopo2029(sc) {
    const d = sc.dopo_2029 || {};
    const nome = (id) => (D.proposte.find((p) => p.id === id) || {}).titolo || id;
    const gruppo = (es) => (d.voci || []).filter((x) => x.esito === es);
    const riga = (x) => `<li><a href="#/programma/${encodeURIComponent(x.id)}">${esc(x.id)}</a> ${esc(nome(x.id))}: ${euro(x.mld)}. ${esc(x.motivo.charAt(0).toUpperCase() + x.motivo.slice(1))}${x.successore ? `. <strong>Dopo il 2029:</strong> ${esc(x.successore)}` : ""}</li>`;
    const blocco = (es, titolo) => gruppo(es).length ? `<p><strong>${titolo}</strong></p><ul>${gruppo(es).map(riga).join("")}</ul>` : "";
    return `<div class="avviso attenzione" style="margin-top:12px"><div class="avviso-titolo">${icona("hourglass")}${nf(sc.temporanei_2029, 1)} mld di questa spesa sono pagati con i fondi europei di coesione 2021-2027, ammessi fino al 2029.</div>
      <p>Per ogni misura diciamo prima che cosa succede dopo: <strong>${nf(d.fine || 0, 2)} mld finiscono</strong> perché sono investimenti fatti una volta; <strong>${nf(d.valutazione || 0, 2)} mld sono sperimentazioni</strong> che proseguono solo con una valutazione positiva e risorse nuove; <strong>${nf(d.successore || 0, 2)} mld servono anche dopo</strong> e hanno bisogno di un fondo che li sostituisca. Il successore indicato è soprattutto il ciclo europeo 2028-2034, i cui importi per l'Italia non sono ancora noti: oggi la loro copertura dopo il 2029 non è garantita. Senza nuove decisioni, dal 2030 la spesa del programma scende quindi a circa ${nf(sc.spesa - (d.fine || 0) - (d.valutazione || 0), 1)} mld l'anno, di cui ${nf(d.successore || 0, 1)} da rifinanziare.${d.da_decidere > 0 ? ` <strong>${nf(d.da_decidere, 2)} mld non sono ancora classificati.</strong>` : ""}</p>
      <details><summary>Misura per misura</summary>${blocco("successore", "Servono anche dopo il 2029")}${blocco("valutazione", "Sperimentazioni")}${blocco("fine", "Finiscono nel 2029")}${blocco("da_decidere", "Da classificare")}</details></div>`;
  }

  // Misure del nucleo sotto la versione essenziale, con lo stato della scelta (programma/schema.yaml)
  function eccezioniNucleo(sc) {
    const ecc = (D.schema && D.schema.eccezioni_nucleo) || {};
    const fuori = D.proposte.filter((p) => p.classe === "robusta" && !(sc.misure[p.id] && ["PIENA", "ESSENZIALE"].includes(sc.misure[p.id].variante)));
    if (!fuori.length) return "";
    const voce = (p) => {
      const e = ecc[p.id];
      const stato = !e ? "non ancora spiegata" : e.stato === "dichiarata" ? "eccezione dichiarata: " + e.motivo : "scelta aperta: " + e.motivo;
      return `<a href="#/programma/${encodeURIComponent(p.id)}" title="${esc(stato)}">${esc(p.id)}</a> ${e && e.stato === "dichiarata" ? "(eccezione dichiarata)" : "(scelta aperta)"}`;
    };
    return `; sotto: ${fuori.map(voce).join(", ")}`;
  }

  // ---------- Oggi ----------
  function home() {
    const n = D.numeri || {};
    const nucleo = D.proposte.filter((p) => p.classe === "robusta");
    const coperto = nucleo.filter((p) => rif.misure[p.id] && ["PIENA", "ESSENZIALE"].includes(rif.misure[p.id].variante)).length;
    const spese = D.scenari.map((s) => s.spesa);
    const integra = D.integrita && !D.integrita.errori.length;
    const ult = VERBALI[0];
    const perArea = Object.keys(D.aree).map((k) => [k, D.aree[k], D.proposte.filter((p) => p.area === k).length]);
    const solide = [...nucleo].sort((a, b) => b.p_prima_meta - a.p_prima_meta).slice(0, 6);
    return `
      <section class="hero" aria-labelledby="titolo-home">
        <div>
          <p class="etichetta sopratitolo">Un programma di governo aperto, basato su dati e valori dichiarati</p>
          <h1 id="titolo-home">Governare con i dati,<br>scegliere con i valori.</h1>
          <p class="risposta">${n.proposte} proposte valutate su ${n.valori} valori, finanziate senza deficit e controllate su Costituzione e regole europee. <span class="firma">L'AI propone e verifica. Le persone decidono.</span></p>
          <div class="azioni porte"><a class="btn primario" href="#/programma/per-me">Che cosa cambia per me ${icona("arrow-right")}</a><a class="btn" href="#/programma/una-pagina">Il programma in una pagina</a><a class="btn" href="#/osservatorio">Il governo di oggi</a></div>
          <p class="nota porte-nota"><a href="#/metodo">Come funziona GovernAI</a> · <a href="#/programma/sintesi">Le idee in 10 minuti</a></p>
        </div>
        <div class="oggi-box" aria-label="Oggi in breve">
          <p class="etichetta">Oggi, ${dataLunga(D.generato)}</p>
          <ul>
            <li>${icona("activity")}<a href="#t-allerte" data-ancora>${ALLERTE.length ? `${ALLERTE.length} segnali da seguire nei dati di oggi` : "Gli indicatori sono nelle soglie"}</a></li>
            ${ult ? `<li>${icona("users-round")}<span>Ultima seduta del governo ombra: <a href="${linkSeduta(ult.id)}">${ult.data === OGGI ? "oggi" : dataBreve(ult.data)}</a></span></li>` : ""}
          </ul>
        </div>
      </section>

      <section class="sezione" aria-label="Il giorno in quattro numeri" style="margin-top:32px">
        <div class="griglia g2 g4-d">
          <div class="card kpi"><p class="etichetta"><a href="#/programma/una-pagina">Programma di riferimento</a></p><p class="numero">${nf(rif.spesa, 1)}<small>mld/anno</small></p><p class="nota">${rif.deficit > 0 ? `deficit ${nf(rif.deficit, 1)} mld` : "senza deficit"} · le ${D.scenari.length} versioni vanno da ${nf(Math.min(...spese), 1)} a ${nf(Math.max(...spese), 1)} mld</p>${badge("stima", STIMA)}</div>
          <div class="card kpi"><p class="etichetta">Misure incluse</p><p class="numero">${Object.keys(rif.misure).length}<small>su ${D.proposte.length}</small></p><p class="nota">delle ${nucleo.length} misure più solide, ${coperto} sono finanziate per intero${nucleo.length > coperto ? `; le altre ${nucleo.length - coperto} partono in versione ridotta, <a href="#/programma/una-pagina">dichiarata</a>` : ""}</p></div>
          <div class="card kpi"><p class="etichetta">Cifre verificate</p><p class="numero">${n.cifre_verificate}</p><p class="nota">controllate una per una su fonte primaria</p></div>
          <div class="card kpi"><p class="etichetta">Serie di dati</p><p class="numero">${n.serie}</p><p class="nota">aggiornate ogni giorno da fonti ufficiali</p></div>
        </div>
      </section>

      <section class="sezione" aria-labelledby="t-solide">
        <div class="sezione-testa"><h2 id="t-solide">Le proposte più solide</h2><a href="#/programma?classe=robusta">Tutte e ${nucleo.length}</a></div>
        <p class="nota" style="margin-top:-8px">Restano nella prima metà della classifica con quasi ogni combinazione di pesi tra i valori.</p>
        <div class="proposte-lista">${solide.map((p) => cardProposta(p, `prima metà nel ${Math.round(p.p_prima_meta * 100)}% dei casi`)).join("")}</div>
      </section>

      <section class="sezione" aria-labelledby="t-allerte">
          <div class="sezione-testa"><h2 id="t-allerte">Che cosa ci preoccupa nei dati di oggi</h2><a href="#/dati/allerte">Il dettaglio</a></div>
          ${ALLERTE.length ? `<div class="card"><ul class="allerte-home">${ALLERTE.map(allertaHome).join("")}</ul><p class="nota">Ogni giorno confrontiamo i dati ufficiali con soglie fissate prima. Quando una soglia scatta, il programma cambia le priorità, senza spendere di più.</p></div>` : `<div class="avviso"><div class="avviso-titolo">${icona("circle-check")}Gli indicatori sono nelle soglie.</div></div>`}
        </section>

      ${osservatorioHome()}

      <section class="sezione" aria-labelledby="t-fiducia">
        <div class="sezione-testa"><h2 id="t-fiducia">Fiducia verificabile</h2><a href="#/metodo">Metodo</a></div>
        <div class="fiducia">
          <div class="card">${icona("link-2")}<div><h3>Registro a prova di modifica${integra ? "" : ": da verificare"}</h3><p>Ogni aggiornamento di dati, regole e risultati lascia un'impronta crittografica (${D.integrita.anelli} finora): una modifica nascosta si vede subito.</p></div></div>
          <div class="card">${icona("octagon-x")}<div><h3>Linee rosse automatiche</h3><p>Le proposte che violano diritti o scaricano costi sulle persone con redditi bassi o in condizioni di fragilità sono escluse da regole fisse.</p></div></div>
          <div class="card">${icona("repeat")}<div><h3>Tutto riproducibile</h3><p>Codice, dati, punteggi e regole sono pubblici: chiunque può rifare il calcolo.</p></div></div>
        </div>
      </section>

      <p class="partecipa-riga">${icona("messages-square")}<span><strong>Vuoi ragionarci insieme?</strong> Nella comunità, su invito, si discutono le proposte con altre persone e con l'AI. <a href="#/comunita">Entra nella comunità</a> · <a href="#/partecipa">Altri modi di partecipare</a></span></p>`;
  }

  // ---------- Programma ----------
  // Programma: quattro gruppi al posto di 14 schede; sotto, le pagine del gruppo aperto
  const GRUPPI_PROG = [
    ["Per te", [["per-me", "Che cosa cambia per me", "#/programma/per-me"], ["busta-paga", "La tua busta paga", "#/programma/busta-paga"], ["valori", "I tuoi valori", "#/programma/valori"]]],
    ["Il programma", [["una-pagina", "In una pagina", "#/programma/una-pagina"], ["sintesi", "In sintesi", "#/programma/sintesi"], ["proposte", "Tutte le proposte", "#/programma", () => D.proposte.length], ["mappa", "La mappa dei ministeri", "#/programma/mappa"], ["pronto", "Pronto domani", "#/programma/pronto"]]],
    ["I conti", [["coperture", "Come si paga", "#/programma/coperture"], ["chi-paga", "Chi paga davvero", "#/programma/chi-paga"]]],
    ["Approfondimenti", [["ai", "AI e Stato", "#/programma/ai"], ["equita", "Equità", "#/programma/equita"], ["strategia", "Strategia", "#/programma/strategia"], ["confronti", "Confronti", "#/programma/confronti"], ["proponi", "Proponi un programma", "#/programma/proponi"]]],
  ];
  const schedeProgramma = (k) => {
    const g = GRUPPI_PROG.find((x) => x[1].some((v) => v[0] === k)) || GRUPPI_PROG[1];
    const v = g[1].find((x) => x[0] === k) || g[1][0];
    const voce = (x) => `<a href="${x[2]}" ${x[0] === k ? 'aria-current="page"' : ""}>${esc(x[1])}${x[3] ? ` <span class="conta">${x[3]()}</span>` : ""}</a>`;
    return `<p class="etichetta sez-etichetta">Programma · ${esc(g[0])}</p><h1>${esc(v[1])}</h1>
      <nav class="schede" aria-label="Sezioni del programma">${GRUPPI_PROG.map((x) => `<a href="${x[1][0][2]}" ${x === g ? 'aria-current="page"' : ""}>${esc(x[0])}</a>`).join("")}</nav>
      ${g[1].length > 1 ? `<nav class="sottoschede" aria-label="${esc(g[0])}">${g[1].map(voce).join("")}</nav>` : ""}`;
  };

  // apertura di «In una pagina» e «Tutte le proposte»: prima che cosa contiene il programma, poi (a richiesta)
  // le altre versioni e la cronologia delle scelte
  function aperturaProgramma(sc, selettore, extraCronologia = "") {
    const rif = sc.id === RIF_ID;
    const min = D.scenari.reduce((a, x) => x.spesa < a.spesa ? x : a, D.scenari[0]), max = D.scenari.reduce((a, x) => x.spesa > a.spesa ? x : a, D.scenari[0]);
    return `<p class="risposta">${rif ? "Il programma che proponiamo" : `Stai guardando il <strong>${esc(sc.nome.toLowerCase())}</strong>`}: <strong>${Object.keys(sc.misure).length} misure su ${D.proposte.length}</strong>, per <strong>${nf(sc.spesa, 1)} mld l'anno</strong> ${sc.deficit > 0 ? `con ${nf(sc.deficit, 1)} mld di deficit` : "senza deficit"} ${badge("stima", STIMA)}. Si paga con coperture nuove, fondi europei già stanziati e tariffe: <a href="#/programma/coperture">come si paga</a>.</p>
      <details class="richiudibile versioni" ${rif ? "" : "open"}><summary>${icona("layers")}${rif ? "Altre versioni del programma" : "Cambia versione del programma"}<span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo">
        <p class="nota">Lo stesso programma esiste in ${D.scenari.length} versioni, dalla più piccola (${esc(min.nome.toLowerCase())}, ${nf(min.spesa, 1)} mld l'anno) alla più ampia (${esc(max.nome.toLowerCase())}, ${nf(max.spesa, 1)} mld). Tutte senza deficit: cambiano quante misure si fanno e con quali coperture. Quella di riferimento è il ${esc(scenario(RIF_ID).nome.toLowerCase())}.</p>
        ${selettore}</div></details>
      <details class="richiudibile"><summary>${icona("history")}Come ci siamo arrivati: le scelte fatte su questa versione<span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo"><p>${esc(sc.descrizione)}.</p>${extraCronologia}</div></details>`;
  }
  function elenco(params) {
    const sc = scenario(params.get("scenario") || RIF_ID);
    const nucleo = D.proposte.filter((p) => p.classe === "robusta");
    const coperto = nucleo.filter((p) => sc.misure[p.id] && ["PIENA", "ESSENZIALE"].includes(sc.misure[p.id].variante)).length;
    return `${schedeProgramma("proposte")}
      ${aperturaProgramma(sc, `<div class="segmenti" role="group" aria-label="Versione del programma">${D.scenari.map((x) => `<button type="button" data-scenario="${x.id}" aria-pressed="${x.id === sc.id}" title="${esc(x.descrizione)}">${esc(x.nome)}</button>`).join("")}</div>`,
        `<p class="nota">Le ${nucleo.length} proposte più solide (nucleo robusto) sono finanziate almeno in versione essenziale per ${coperto} su ${nucleo.length}${eccezioniNucleo(sc)}.</p><p class="nota">Da dove vengono i soldi: ${fontiSoldi(sc)}.</p>`)}
      <form class="filtri-barra" role="search" onsubmit="return false">
        <label class="campo largo">Cerca<input type="search" id="f-cerca" value="${esc(params.get("q") || "")}" placeholder="Parola o codice, es. asili, 01-P3"></label>
        <label class="campo">Tema<select id="f-tema"><option value="">Tutti i temi</option>${Object.entries(D.aree).map(([k, v]) => `<option value="${k}" ${k === params.get("tema") ? "selected" : ""}>${esc(v)}</option>`).join("")}</select></label>
        <label class="campo">Classe<select id="f-classe"><option value="">Tutte le classi</option>${Object.entries(CLASSE).map(([k, v]) => `<option value="${esc(k)}" ${k === params.get("classe") ? "selected" : ""}>${esc(v[2])}</option>`).join("")}</select></label>
        <label class="spunta"><input type="checkbox" id="f-incluse" ${params.get("incluse") ? "checked" : ""}>Solo incluse</label>
      </form>
      <details class="leggi"><summary>Come leggere la tabella</summary><ul class="nota">
        <li><strong>Classe</strong>: <em>nucleo robusto</em> = conviene con quasi tutti i pesi tra i valori; <em>dipende dai valori</em> = entra solo con alcuni pesi, quindi è una scelta politica; <em>in coda</em> e <em>sfavorevole</em> = conviene poco o peggiora i valori.</li>
        <li><strong>Variante</strong>: <em>piena</em>, <em>essenziale</em> (ridotta), <em>pilota</em> (sperimentazione) o <em>zero</em> (solo regole, senza spesa).</li>
        <li><strong>Costo l'anno</strong>: stima GovernAI a regime, arrotondata.</li>
        <li><strong>Robustezza</strong>: in quante combinazioni di pesi tra i valori la proposta entra nel programma con questa variante. Per le misure inserite per <em>scelta politica</em> non si calcola: ci sono perché lo ha deciso chi guida il progetto.</li>
        <li><strong>Controlli</strong>: l'esito peggiore dei controlli su Costituzione, diritto europeo e fisco. <em>Richiede notifica</em> = va comunicata alla Commissione europea come aiuto di Stato prima di partire; <em>condizionato</em> = compatibile se rispetta alcune condizioni.</li></ul></details>
      <p class="nota" id="f-conta" role="status" aria-live="polite"></p>
      <div class="tabella-box"><table class="tabella a-card"><thead><tr><th>Proposta</th><th>Classe</th><th>Variante</th><th class="num">Costo l'anno</th><th>Robustezza</th><th>Controlli</th></tr></thead><tbody id="f-corpo"></tbody></table></div>`;
  }
  function aggiornaElenco() {
    const q = ($("#f-cerca").value || "").trim().toLowerCase(), tema = $("#f-tema").value, classe = $("#f-classe").value, incl = $("#f-incluse").checked;
    const sc = scenario(new URLSearchParams(location.hash.split("?")[1] || "").get("scenario") || RIF_ID);
    const righe = D.proposte.filter((p) => (!tema || p.area === tema) && (!classe || p.classe === classe) && (!incl || sc.misure[p.id])
      && (!q || (p.id + " " + p.titolo + " " + D.aree[p.area]).toLowerCase().includes(q)));
    let html = "", area = null;
    for (const p of righe) {
      if (p.area !== area) { area = p.area; html += `<tr class="gruppo"><td colspan="6">${esc(D.aree[area])}</td></tr>`; }
      const m = sc.misure[p.id];
      const g = (p.giuridico || []).filter((r) => r.tipo === "proposta" || (m && r.id === `${p.id}:${m.variante}`));
      const peggiore = g.reduce((a, r) => (GRAVITA_GIUR[r.esito] ?? 0) > (GRAVITA_GIUR[a] ?? -1) ? r.esito : a, null);
      html += `<tr class="${m ? "" : "esclusa"}"><td class="principale"><a class="riga" href="${linkP(p.id)}">${esc(tit(p.titolo))}</a> <span class="codice">${esc(p.id)}</span>${p.linea_rossa ? " " + chip(["critico", "octagon-x", "Linea rossa in alcune versioni"]) : ""}</td>
        <td data-etichetta="Classe">${chipClasse(p.classe)}</td><td data-etichetta="Variante">${misuratore(m && m.variante)}</td>
        <td class="num" data-etichetta="Costo l'anno">${m ? euro(m.costo) : "—"}</td>
        <td data-etichetta="Robustezza">${!m ? "—" : m.imposta ? `<span class="nota">scelta politica</span>` : `<span class="robustezza" aria-hidden="true"><span style="width:${Math.round(m.robustezza * 100)}%"></span></span>${Math.round(m.robustezza * 100)}%`}</td>
        <td data-etichetta="Controlli">${peggiore ? chip(ESITO_GIUR[peggiore]) : chip(["", "circle-dashed", "Non valutato"])}</td></tr>`;
    }
    $("#f-corpo").innerHTML = html || `<tr><td colspan="6" class="vuoto">Nessuna proposta con questi filtri.</td></tr>`;
    $("#f-conta").textContent = `${righe.length} proposte mostrate`;
    const pr = new URLSearchParams();
    if (q) pr.set("q", q); if (tema) pr.set("tema", tema); if (classe) pr.set("classe", classe); if (incl) pr.set("incluse", "1"); if (sc.id !== RIF_ID) pr.set("scenario", sc.id);
    history.replaceState(null, "", "#/programma" + (pr.toString() ? "?" + pr : ""));
    icone();
  }

  // Ogni soluzione ragionata: perché, come, che cosa, chi, e griglia oceano blu (programma/quattro_domande_*.yaml)
  const Q4 = [["perche", "Perché", "circle-help", "Il problema e il dato"], ["come", "Come", "settings-2", "Il meccanismo e come si paga"], ["cosa", "Che cosa", "target", "Risultati e come li misuriamo"], ["chi", "Chi", "users-round", "Chi decide, chi ne beneficia, chi paga"]];
  const ERRC = [["eliminare", "Elimina", "x"], ["ridurre", "Riduce", "arrow-down"], ["aumentare", "Aumenta", "arrow-up"], ["creare", "Crea", "sparkles"]];
  function grigliaErrc(o, titolo) {
    return `<div class="errc" aria-label="${esc(titolo)}">${ERRC.map(([k, t, ic]) => {
      const v = o[k], lista = Array.isArray(v) ? v : [v];
      const vuota = !v || (lista.length === 1 && /^niente\.?$/i.test(String(lista[0]).trim()));
      return `<div class="errc-c ${k}${vuota ? " vuota" : ""}"><p class="errc-t">${icona(ic)}${t}</p>${vuota ? `<p class="nota">Niente</p>` : lista.length > 1 ? `<ul>${lista.map((x) => `<li>${codici(esc(x))}</li>`).join("")}</ul>` : `<p>${codici(esc(lista[0]))}</p>`}</div>`;
    }).join("")}</div>`;
  }
  function sezioneQuattro(q) {
    return `<section class="blocco" id="ragionamento" aria-labelledby="h-ragionamento">
      <h2 id="h-ragionamento">La soluzione ragionata <small>perché, come, che cosa, chi</small></h2>
      <div class="quattro">${Q4.map(([k, t, ic, sub]) => `<div class="card q4"><p class="q4-t">${icona(ic)}${t}<small>${sub}</small></p><p>${codici(esc(q[k] || ""))}</p></div>`).join("")}</div>
      ${q.oceano_blu ? `<h3 class="q4-sotto">Rispetto a come fa oggi lo Stato <small>griglia della strategia oceano blu</small></h3>${grigliaErrc(q.oceano_blu, "Elimina, riduce, aumenta, crea")}` : ""}
    </section>`;
  }
  // ---------- «Il bilancio in breve»: che cosa cambia, che cosa si ottiene, chi ci guadagna e chi paga, costo, valori, solidità
  const frasi = (t) => String(t || "").replace(/\s+/g, " ").trim().split(/(?<=\.)\s+(?=[A-ZÀÈÉÌÒÙ«])/);
  const corto = (t, max = 260) => { let o = ""; for (const f of String(t || "").replace(/\s+/g, " ").trim().split(/(?<=[.;])\s+/)) { if (o && (o + " " + f).length > max) break; o = o ? o + " " + f : f; } if (o.length > max + 60) o = o.slice(0, o.lastIndexOf(" ", max)) + "…"; return o.replace(/;$/, ".").replace(/^./, (c) => c.toUpperCase()); };
  function bilancio(p, m, q4, medie, peggiore, S) {
    const soluzione = (S.match(/\*\*Soluzione\.?\*\*\.?\s*([^\n]+)/) || [])[1];
    const M = ((D.bilancio_breve || {}).schede || {})[p.id] || {};   // testi scritti a mano (programma/bilancio_breve.yaml)
    const RE_OB = /Obiettiv[oi][^:.;]{0,50}:\s*/;
    const cosaQ = q4 && q4.cosa ? q4.cosa.split(RE_OB)[0] : "";
    const frase = (S.match(/\*In una frase:\s*([^*\n]+)\*/) || [])[1];
    const titoloLungo = ((S.match(/^## [^—]+— (.+)$/m) || [])[1]) || tit(p.titolo);
    const sol = soluzione && piano(soluzione).replace(/^[-–]\s*/, "");
    // ordine: la frase riassuntiva della scheda, poi la soluzione (se non ripete il titolo), poi la lettura ragionata
    const cambia = M.cambia ? M.cambia : frase ? corto(piano(frase)) : sol && sol.trim() !== titoloLungo.trim() ? corto(sol) : cosaQ ? corto(cosaQ) : corto(((p.varianti || []).find((v) => m && v.variante === m.variante) || (p.varianti || [])[0] || {}).descrizione || titoloLungo, 220);
    const ob = M.obiettivo || (q4 && q4.cosa ? (q4.cosa.match(new RegExp(RE_OB.source + "([^;.]+(?:\\.\\d[^;.]*)*)")) || [])[1] : "");
    // «chi»: una frase su chi decide e attua, una su chi ne beneficia, le altre su chi paga o ci perde
    const chi = q4 ? frasi(q4.chi) : [];
    const eBeneficio = (f) => /^(Ne )?benefic/i.test(f), eAttore = (f) => /^(Decid|Attua|Propon|Controll|Certific|Valut|Approv)/i.test(f);
    const guadagna = M.guadagna ? [M.guadagna] : chi.filter(eBeneficio).map((f) => f.replace(/^Ne benefic\w*\s*/i, "").replace(/^./, (c) => c.toUpperCase()));
    const paga = M.paga ? [M.paga] : chi.filter((f) => !eBeneficio(f) && !eAttore(f));
    const pos = medie.filter((x) => x.m >= 0.25).sort((a, b) => b.m - a.m).slice(0, 3), neg = medie.filter((x) => x.m <= -0.25).sort((a, b) => a.m - b.m).slice(0, 2);
    const v = (x) => `${esc(x.nome)} <span class="num">${x.m > 0 ? "+" : "−"}${nf(Math.abs(x.m), 1)}</span>`;
    const costo = m ? (m.costo > 0 ? `<strong>${euro(m.costo)} l'anno</strong> nella versione ${esc(String(m.variante).toLowerCase())}, pagati con le <a href="#/programma/coperture">coperture del programma</a>, senza deficit` : `<strong>Costo zero o quasi</strong>: sono regole, non spesa`) : `Non è nel programma di riferimento; la versione piena costerebbe ${euro(p.costo_pieno)} l'anno`;
    const solid = [CLASSE_SEMPLICE[p.classe] ? `${CLASSE_SEMPLICE[p.classe]}${p.classe === "dipendente dai valori" && p.trainanti ? ` (soprattutto ${esc(p.trainanti)})` : ""}` : "", peggiore ? GIUR_SEMPLICE[peggiore] : "", m && !m.imposta ? solidita(m.robustezza) : m && m.imposta ? "inserita per scelta politica" : ""].filter(Boolean).join(" · ");
    return [
      ["sparkles", "Che cosa cambia", esc(cambia)],
      ...(ob ? [["target", "Che cosa si vuole ottenere", esc(corto(ob, 220).replace(/^./, (c) => c.toUpperCase()))]] : []),
      ...(guadagna.length ? [["thumbs-up", "Chi ci guadagna", esc(corto(guadagna.join(" "), 240))]] : []),
      ...(paga.length ? [["wallet", "Chi paga o ci perde", esc(corto(paga.join(" "), 240))]] : []),
      ["coins", "Quanto costa", costo],
      ["scale", "Valori", pos.length || neg.length ? `${pos.length ? `Aiuta soprattutto ${pos.map(v).join(", ")}` : "Nessun valore migliora in modo netto"}${neg.length ? `; pesa su ${neg.map(v).join(", ")}` : "; non pesa in modo netto su nessun valore"}` : "Effetti piccoli su tutti i valori"],
      ["shield-check", "Quanto è solida", esc(solid)],
    ];
  }
  // ---------- le versioni di una proposta affiancate
  function tabellaVarianti(p, m, medie) {
    const vs = (p.varianti || []).slice().sort((a, b) => (b.intensita || 0) - (a.intensita || 0));
    const piena = vs[0] || {};
    const top = medie.filter((x) => x.m >= 0.25).sort((a, b) => b.m - a.m).slice(0, 2), giu = medie.filter((x) => x.m <= -0.25).sort((a, b) => a.m - b.m).slice(0, 1);
    const pct = (a, b) => b > 0 ? Math.round(a / b * 100) : null;
    return `<div class="tabella-scorre"><table class="tabella a-card var-tab"><thead><tr><th>Versione</th><th class="num">Costo l'anno</th><th>Che cosa si ottiene</th><th>Che cosa fa</th></tr></thead><tbody>
      ${vs.map((v) => {
        const k = piena.intensita ? (v.intensita || 0) / piena.intensita : 1;
        const pe = pct(v.intensita || 0, piena.intensita || 0), pc = pct(v.costo || 0, piena.costo || 0);
        const valori = [...top.map((x) => `${esc(x.nome)} +${nf(x.m * (v.intensita || 0), 1)}`), ...giu.map((x) => `${esc(x.nome)} −${nf(Math.abs(x.m) * (v.intensita || 0), 1)}`)].join(", ");
        const rapporto = v === piena ? "Tutto l'effetto previsto" : `${pe}% dell'effetto${pc != null && piena.costo > 0 ? ` con il ${pc}% del costo` : ""}`;
        return `<tr class="${m && m.variante === v.variante ? "scelta" : ""}"><td class="principale">${misuratore(v.variante)}${m && m.variante === v.variante ? ` ${chip(["info", "check", "Nel programma"])}` : ""}</td>
          <td class="num" data-etichetta="Costo l'anno">${v.costo > 0 ? euro(v.costo) : "costo zero"}</td>
          <td data-etichetta="Che cosa si ottiene"><strong>${rapporto}</strong>${valori && k > 0 ? `<small>${valori}</small>` : ""}</td>
          <td data-etichetta="Che cosa fa">${breveEResto(v.descrizione, 160)}${v.strumento ? `<small>Strumento: ${esc(v.strumento)}</small>` : ""}</td></tr>`;
      }).join("")}</tbody></table></div>`;
  }
  function schedaProposta(id) {
    const p = proposta(id);
    if (!p) return nonTrovato(`Nessuna proposta con codice «${id}».`);
    const m = rif.misure[p.id];
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
    const q4 = (D.quattro_domande || {})[p.id];
    const B = bilancio(p, m, q4, medie, peggiore, S);
    const voci = [["bilancio", "Il bilancio in breve"], ["in-breve", "In breve"], ...(q4 ? [["ragionamento", "Perché, come, chi"]] : []), ["valori", "Effetto sui valori"], ["varianti", "Varianti"], ["controlli", "Controlli"], ["obiettivi", "Obiettivi"], ["governo", "Governo ombra"], ["testo", "Testo completo"], ["fonti", "Fonti e metodo"]];
    const esitoDec = dec ? (deroga ? ["attenzione", "git-branch", "Accolta con deroga"] : ESITO_DEC[dec.esito] || ["", "circle-dashed", dec.esito]) : null;
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
            <div class="chips">${chip([...CLASSE[p.classe] || ["", "circle-dot", p.classe]].map((x, i) => i === 2 ? CLASSE_SEMPLICE[p.classe] || x : x))}${p.linea_rossa ? chip(["critico", "octagon-x", "Una versione è esclusa"]) : ""}${peggiore ? chip([...ESITO_GIUR[peggiore]].map((x, i) => i === 2 ? GIUR_SEMPLICE[peggiore] || x : x)) : ""}</div>
            <div class="stato">Nel programma di riferimento: ${misuratore(m && m.variante)}${m ? `<span>· ${euro(m.costo)} l'anno · ${m.imposta ? "inserita per scelta politica" : solidita(m.robustezza)}</span>` : `<span>· non inclusa</span>`}</div>
            ${indiceMobile(voci)}
          </header>
          ${p.linea_rossa ? `<div class="avviso critico" role="alert"><div class="avviso-titolo">${icona("octagon-x")}Linea rossa in alcune versioni</div><p>Almeno una versione di questa proposta supera una linea rossa della Carta dei valori ed è esclusa in automatico. Le altre versioni restano possibili: vedi le varianti e il programma.</p></div>` : ""}

          <section class="card bilancio blocco" id="bilancio" aria-labelledby="h-bilancio" style="margin-top:0">
            <h2 id="h-bilancio">Il bilancio in breve</h2>
            <dl>${B.map(([ic, t, v]) => `<div><dt>${icona(ic)}${t}</dt><dd>${v}</dd></div>`).join("")}</dl>
            <p class="nota">Riassunto delle sezioni qui sotto: obiettivi e «chi» dalla lettura ragionata, effetti sui valori dai tre valutatori, costo dal programma di riferimento ${badge("stima", STIMA)}.</p>
          </section>

          <section class="card in-breve blocco" id="in-breve" aria-labelledby="h-breve">
            <h2 id="h-breve" class="vh">In breve</h2>
            <h3>Il problema in un dato</h3>
            ${grande ? `<p class="dato-grande">${esc(grande)}</p>` : ""}
            <p class="testo-lettura">${esc(piano(problema))} ${badge(fonteProb ? "verificato" : "verificare", fonteProb ? piano(fonteProb) : "La fonte non è indicata nel testo della scheda.")}</p>
            <h3>La soluzione</h3>
            <p class="testo-lettura">${esc(piano(soluzione)) || esc(titoloLungo || "")}</p>
            <h3>Costo e chi paga</h3>
            <p>${m ? `<strong>${euro(m.costo)} l'anno</strong> nella variante ${esc(m.variante.toLowerCase())}` : `Costo pieno ${euro(p.costo_pieno)} l'anno; non inclusa nel programma di riferimento`} ${badge("stima", STIMA)}</p>
            <h3>Il governo ombra</h3>
            ${dec ? `${bannerSim("piccolo")}<p>${chip(esitoDec)} in variante ${esc(String(dec.variante).toLowerCase())} nella seduta <a href="${linkSeduta(seduta.id)}">«${esc(seduta.titolo)}»</a> (${dataBreve(seduta.data)}).</p>
              ${deroga ? `<p class="nota">${codici(esc(piano(deroga.testo)))}</p>` : ""}
              ${mandati.length ? `<p>${mandati.map((x) => `Mandato <strong class="mono">${x.id}</strong> entro il ${dataBreve(x.scadenza)}`).join(" · ")}</p>` : ""}`
              : `<p class="nota">Non ancora all'ordine del giorno del Consiglio.</p>`}
          </section>

          ${q4 ? sezioneQuattro(q4) : ""}

          <section class="blocco" id="valori" aria-labelledby="h-valori">
            <h2 id="h-valori">Effetto sui 10 valori <small>mediana dei tre valutatori AI, media di breve, medio e lungo periodo, da −3 a +3</small></h2>
            ${medie.length ? `<div class="valori" role="img" aria-label="Effetto sui valori: ${nonZero.map((x) => `${x.nome} ${x.m > 0 ? "più" : "meno"} ${nf(Math.abs(x.m), 1)}`).join("; ")}${zero.length ? `; ${zero.length} valori a zero` : ""}.">
                <span aria-hidden="true"></span><div class="asse-testa" aria-hidden="true"><span>−3 peggiora</span><span>0</span><span>migliora +3</span></div><span aria-hidden="true"></span>
                ${nonZero.map((x) => `<span>${esc(x.nome)}</span><div class="traccia" title="breve, medio, lungo: ${p.punteggi[D.valori.findIndex((v) => v.id === x.id)].join(", ")}"><span class="${x.m >= 0 ? "pos" : "neg"}" style="width:${Math.abs(x.m) / 3 * 50}%"></span></div><span class="num">${x.m > 0 ? "+" : "−"}${nf(Math.abs(x.m), 1)}</span>`).join("")}
                ${zero.length ? `<p class="zero">A zero: ${zero.map((x) => esc(x.nome)).join(", ")}.</p>` : ""}
              </div>
              <p class="nota">Prima metà della classifica nel ${Math.round(p.p_prima_meta * 100)}% delle combinazioni di pesi; posizione tra ${p.rango[0]}ª e ${p.rango[1]}ª.${p.trainanti ? ` Sale se si dà più peso a: ${esc(p.trainanti)}.` : ""} <a href="#/programma/valori">Prova i tuoi pesi</a></p>`
              : vuoto("Il panel non ha ancora valutato questa proposta.")}
          </section>

          <section class="blocco" id="varianti" aria-labelledby="h-varianti">
            <h2 id="h-varianti">Le versioni a confronto <small>quanto si fa, quanto costa, che cosa si ottiene · costi: stime GovernAI</small></h2>
            <p class="nota">Ogni versione dà una parte dell'effetto della versione piena: i valutatori giudicano la proposta, il motore moltiplica il giudizio per la «dose» della versione.</p>
            ${tabellaVarianti(p, m, medie)}
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
              <p>Punteggi assegnati da ${D.valutatori.length} valutatori AI, distinti dagli agenti che hanno scritto le proposte; non sono persone, ed è un limite dichiarato. Classe calcolata provando migliaia di combinazioni di pesi tra i 10 valori.</p>
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

  // stato degli obiettivi in parole semplici (apprendimento/valuta.py: «in osservazione» = seguito sui dati ufficiali
  // finché la misura non è in vigore; «manuale» = nessuna serie ufficiale, si misura a mano)
  const STATO = { raggiunto: ["favorevole", "circle-check", "Raggiunto"], "in linea": ["info", "trending-up", "In linea"], "in ritardo": ["attenzione", "circle-alert", "In ritardo"], peggiorato: ["alto", "trending-down", "Peggiorato"], "in osservazione": ["", "eye", "Seguito sui dati ufficiali"], manuale: ["", "pencil-ruler", "Senza dato ufficiale: si misura a mano"] };
  function tabellaObiettivi(lista, conProposta) {
    return `<div class="tabella-box"><table class="tabella a-card"><thead><tr>${conProposta ? "<th>Proposta</th>" : ""}<th>Obiettivo</th><th class="num">Base</th><th class="num">Ultimo</th><th class="num">Traguardo</th><th>Stato</th></tr></thead><tbody>
      ${lista.map((o) => `<tr>${conProposta ? `<td class="principale"><a href="${linkP(o.proposta)}">${esc(tit((proposta(o.proposta) || {}).titolo || o.proposta).split(":")[0])}</a> <span class="codice">${esc(o.proposta)}</span></td>` : ""}<td ${conProposta ? 'data-etichetta="Obiettivo"' : 'class="principale"'}>${esc(o.nome)} <span class="nota">${esc(o.unita || "")}</span></td><td class="num" data-etichetta="Base">${nf(o.base, 1)}${o.periodo_base ? ` <span class="nota">(${esc(o.periodo_base)})</span>` : ""}</td><td class="num" data-etichetta="Ultimo">${nf(o.ultimo, 1)}${o.periodo ? ` <span class="nota">(${esc(periodoBreve(o.periodo))})</span>` : ""}</td><td class="num" data-etichetta="Traguardo">${nf(o.obiettivo, 1)}</td>
        <td data-etichetta="Stato">${chip(STATO[o.stato] || ["", "circle-dashed", o.stato])}</td></tr>`).join("")}</tbody></table></div>`;
  }

  // «Come si paga» in breve: quanto vale, da dove arriva, chi paga di più
  function riassuntoCoperture(attive) {
    const att = D.coperture.filter((c) => attive.has(c.misura_id));
    const tot = att.reduce((a, c) => a + (c.gettito_min || 0), 0);
    const perFondo = {};
    att.forEach((c) => { perFondo[c.fondo_id] = (perFondo[c.fondo_id] || 0) + (c.gettito_min || 0); });
    const nomi = (MOT && MOT.nomi_fondi) || {};
    const fondi = Object.entries(perFondo).sort((a, b) => b[1] - a[1]).slice(0, 4);
    const grandi = att.slice().sort((a, b) => (b.gettito_min || 0) - (a.gettito_min || 0)).slice(0, 5);
    const nomeC = (c) => { let t = String(c.descrizione || "").split(/:\s/)[0].replace(/\s*\([^)]*\)/g, "").trim(); return t.length > 110 ? t.slice(0, t.lastIndexOf(" ", 107)) + "…" : t; };
    return `<section class="card blocco riassunto-coperture" aria-labelledby="h-rc"><h2 id="h-rc">In breve</h2>
      <ul class="elenco-punti">
        <li>Le ${att.length} coperture attive valgono almeno <strong>${nf(tot, 1)} mld l'anno</strong> ${badge("stima", STIMA)}, ognuna contata una sola volta. Le altre ${D.coperture.length - att.length} restano pronte per i programmi più ampi.</li>
        <li><strong>Da dove arrivano:</strong> ${fondi.map(([f, v]) => `${esc(NOMI_FONDI_CORTI[f] || nomi[f] || f)} ${nf(v, 1)} mld`).join(" · ")}.</li>
        <li><strong>Le cinque più grandi:</strong></li>
      </ul>
      <ol class="elenco-punti">${grandi.map((c) => `<li>${esc(nomeC(c))} <span class="nota">(${nf(c.gettito_min, 2)}–${nf(c.gettito_max, 2)} mld · paga: ${esc(String(c.chi_paga || "").split(/[;(]/)[0].trim())})</span></li>`).join("")}</ol>
      <p class="nota">Chi paga di più e chi di meno, per reddito: <a href="#/programma/equita">Equità, capitolo «Chi paga»</a> · confronto tra lavoro, capitale e rendite: <a href="#/programma/chi-paga">Chi paga davvero</a>.</p></section>`;
  }
  function coperture() {
    const base = new Set(scenario("base").coperture), comp = new Set(scenario("completo").coperture), mom = new Set(rif.coperture);
    const fondi = [...new Set(D.coperture.map((c) => c.fondo_id))].sort();
    const tot = (set) => D.coperture.filter((c) => set.has(c.misura_id)).reduce((a, c) => a + (c.gettito_min || 0), 0);
    // caselle con + e − dentro: il giudizio si legge anche senza distinguere i colori
    const punti = (c) => `<span class="punti" role="img" aria-label="${D.valori.map((v) => v.nome + " " + (c[v.id] > 0 ? "+" : "") + c[v.id]).join(", ")}">${D.valori.map((v) => `<span class="${c[v.id] > 0 ? "p" : c[v.id] < 0 ? "n" : ""}" aria-hidden="true">${c[v.id] > 0 ? "+" : c[v.id] < 0 ? "−" : ""}</span>`).join("")}</span>`;
    return `${schedeProgramma("coperture")}
      <p class="risposta">Il programma si finanzia con ${D.coperture.length} coperture concrete: un registro unico impedisce di contare due volte gli stessi soldi. Nel programma di riferimento ne sono attive ${mom.size}.</p>
      ${riassuntoCoperture(mom)}
      <h2 class="sezione">I sei programmi a confronto</h2>
      <div class="griglia g2 g4-d">${D.scenari.map((s) => `<div class="card kpi"><p class="etichetta">${esc(s.nome)}</p><p class="numero">${nf(s.spesa, 1)}<small>mld/anno</small></p><p class="nota">${s.id === RIF_ID ? "<strong>riferimento</strong> · " : ""}${s.coperture.length} coperture · deficit ${s.deficit > 0 ? nf(s.deficit, 1) + " mld" : "zero"}</p></div>`).join("")}</div>
      <div class="card" style="margin-top:16px">${barreSoldi(D.scenari)}<details class="leggi"><summary>Il dettaglio in parole</summary><ul>${D.scenari.map((x) => `<li class="nota"><strong>${esc(x.nome)}:</strong> ${fontiSoldi(x)}</li>`).join("")}</ul></details></div>
      <p style="margin-top:12px">${badge("stima", STIMA)} <span class="nota">Gettito minimo delle coperture: programma base ${nf(tot(base))} mld, completo ${nf(tot(comp))} mld.</span></p>
      <details class="richiudibile sezione" id="c-tutte"><summary>${icona("table")}Tutte le ${D.coperture.length} coperture, con ricerca e filtri<span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo">
      <form class="filtri-barra" role="search" onsubmit="return false">
        <label class="campo largo">Cerca<input type="search" id="c-cerca" placeholder="es. gasolio, IVA, tabacco"></label>
        <label class="campo">Fondo<select id="c-fondo"><option value="">Tutti i fondi</option>${fondi.map((f) => `<option>${esc(f)}</option>`).join("")}</select></label>
        <label class="campo">Livello<select id="c-livello"><option value="">Tutti</option><option value="1">1 · basso costo sociale</option><option value="2">2 · strutturali</option></select></label>
      </form>
      <div class="tabella-box"><table class="tabella a-card"><thead><tr><th>Copertura</th><th>Fondo</th><th class="num">Gettito min–max</th><th>Chi paga</th><th>Effetto sui valori</th><th>Nel riferimento</th></tr></thead>
        <tbody id="c-corpo">${D.coperture.map((c) => `<tr data-testo="${esc((c.misura_id + " " + c.descrizione + " " + c.chi_paga).toLowerCase())}" data-fondo="${esc(c.fondo_id)}" data-livello="${c.livello ?? 1}">
          <td class="principale"><span class="mono nota">${esc(c.misura_id)} · livello ${c.livello ?? 1}</span><br>${esc(c.descrizione)}</td><td data-etichetta="Fondo">${esc(c.fondo_id)}</td>
          <td class="num" data-etichetta="Gettito min–max">${nf(c.gettito_min)}–${nf(c.gettito_max)} mld</td><td data-etichetta="Chi paga">${esc(c.chi_paga)}</td>
          <td data-etichetta="Valori">${punti(c)}</td><td data-etichetta="Nel riferimento">${mom.has(c.misura_id) ? chip(["info", "check", "Attiva"]) : "—"}</td></tr>`).join("")}</tbody></table></div></div></details>`;
  }

  // ---------- Proponi un programma ----------
  // Stesse regole dell'ottimizzatore (programma/ottimizza.py): un vincolo per le risorse generali, uno per ogni
  // fondo vincolato, coperture legate, linee rosse automatiche. I conti anno per anno li fa la validazione completa.
  const MOT = D.motore || { prelievi: {}, capienze: {}, generali: [], fuori_bilancio: [], legami: {}, linee_rosse: {}, nomi_fondi: {} };
  const VLET = { PIENA: "P", ESSENZIALE: "E", PILOTA: "T", ZERO: "Z" }, LETV = { P: "PIENA", E: "ESSENZIALE", T: "PILOTA", Z: "ZERO" };
  const NOME_V = { PIENA: "Piena", ESSENZIALE: "Essenziale", PILOTA: "Prova", ZERO: "Solo regole" };
  const PP = { nome: "", m: {}, c: new Set() };
  // codice compatto e leggibile: n=nome&m=01-P1.E,02-C2.P&c=AS01,SF06 (P piena, E essenziale, T prova, Z solo regole)
  const ppCodice = () => (PP.nome ? "n=" + encodeURIComponent(PP.nome) + "&" : "") +
    "m=" + Object.entries(PP.m).sort().map(([p, v]) => p + "." + VLET[v]).join(",") + "&c=" + [...PP.c].sort().join(",");
  const ppLink = () => location.href.split("#")[0] + "#/programma/proponi?" + ppCodice();
  function ppCarica(params) {
    PP.m = {}; PP.c = new Set(); PP.nome = params.get("n") || "";
    const da = params.get("da");
    const sc = da ? D.scenari.find((s) => s.id === da) : null;
    if (sc) { Object.entries(sc.misure).forEach(([p, x]) => { PP.m[p] = x.variante; }); (sc.coperture || []).forEach((c) => PP.c.add(c)); return; }
    (params.get("m") || "").split(",").filter(Boolean).forEach((t) => { const [p, l] = t.split("."); if (proposta(p) && LETV[l]) PP.m[p] = LETV[l]; });
    (params.get("c") || "").split(",").filter(Boolean).forEach((c) => { if (D.coperture.some((x) => x.misura_id === c)) PP.c.add(c); });
  }
  function ppConti(misure, cop) {
    const G = new Set(MOT.generali), FB = new Set(MOT.fuori_bilancio), spesa = {}, gett = {};
    let totale = 0, tariffe = 0;
    Object.entries(misure).forEach(([p, v]) => Object.entries(MOT.prelievi[p + ":" + v] || {}).forEach(([f, x]) => { spesa[f] = (spesa[f] || 0) + x; totale += x; if (FB.has(f)) tariffe += x; }));
    const cs = D.coperture.filter((c) => cop.has(c.misura_id));
    cs.forEach((c) => { const f = String(c.fondo_id).toUpperCase().trim(); gett[f] = (gett[f] || 0) + (+c.gettito_min || 0); });
    const somma = (o, filtro) => Object.entries(o).filter(([f]) => filtro(f)).reduce((a, [, x]) => a + x, 0);
    const gen = { spesa: somma(spesa, (f) => G.has(f)), gettito: somma(gett, (f) => G.has(f)) };
    const vincolati = Object.keys(spesa).filter((f) => !G.has(f) && !FB.has(f)).map((f) => ({ f, spesa: spesa[f], disp: (MOT.capienze[f] || 0) + (gett[f] || 0) }));
    const avvisi = [];
    if (gen.spesa > gen.gettito + 1e-6) avvisi.push(`Mancano ${nf(gen.spesa - gen.gettito)} mld di coperture sulle risorse generali: così il programma fa deficit.`);
    vincolati.filter((x) => x.spesa > x.disp + 1e-6).forEach((x) => avvisi.push(`Il fondo «${MOT.nomi_fondi[x.f] || x.f}» non basta: servono ${nf(x.spesa)} mld, ce ne sono ${nf(x.disp)}${D.coperture.some((c) => String(c.fondo_id).toUpperCase() === x.f) ? ". Attiva le coperture di questo fondo o scegli una versione più leggera" : ""}.`));
    Object.entries(misure).forEach(([p, v]) => { const m = MOT.linee_rosse[p + ":" + v] || MOT.linee_rosse[p]; if (m) avvisi.push(`Linea rossa: ${tit((proposta(p) || {}).titolo || p)} (${(NOME_V[v] || v).toLowerCase()}), ${m}.`); });
    cs.forEach((c) => { const m = MOT.linee_rosse[c.misura_id]; if (m) avvisi.push(`Linea rossa: copertura ${c.misura_id}, ${m}.`); });
    Object.entries(MOT.legami).forEach(([c, ok]) => {
      if (cop.has(c) && !ok.some((k) => { const [p, v] = k.split(":"); return misure[p] === v; }))
        avvisi.push(`La copertura ${c} si può usare solo insieme a ${[...new Set(ok.map((k) => tit((proposta(k.split(":")[0]) || {}).titolo || k.split(":")[0])))].join(", ")} (${ok.map((k) => (NOME_V[k.split(":")[1]] || "").toLowerCase()).join(" o ")}).`);
    });
    // profilo sui valori: punteggio mediano del panel (media dei tre orizzonti) × intensità della variante, più i valori delle coperture
    const val = D.valori.map((vv, j) => {
      let s = 0;
      Object.entries(misure).forEach(([p, v]) => { const pr = proposta(p), va = pr && pr.varianti.find((x) => x.variante === v); if (pr && pr.punteggi && va) s += (pr.punteggi[j].reduce((a, b) => a + b, 0) / 3) * (+va.intensita || 0); });
      cs.forEach((c) => { s += +c[vv.id] || 0; });
      return s;
    });
    const regressive = cs.filter((c) => (+c.EQU || 0) < 0).reduce((a, c) => a + (+c.gettito_min || 0), 0);
    return { totale, tariffe, gen, vincolati, avvisi, val, regressive, gettitoTot: cs.reduce((a, c) => a + (+c.gettito_min || 0), 0), n: Object.keys(misure).length, nc: cs.length };
  }
  const NOMI_FONDI_CORTI = { SAD: "Sussidi dannosi per l'ambiente", SPESE_FISCALI: "Agevolazioni fiscali", ACCISE_SALUTE: "Accise sulla salute", RIORDINO_BONUS: "Riordino dei bonus", RIALLOCAZIONE: "Risparmi di spesa", PENSIONI: "Pensioni", TASSA_SOGGIORNO: "Tassa di soggiorno" };
  function proponi(params) {
    ppCarica(params);
    const rif = D.scenari.find((s) => s.id === "intermedio") || D.scenari[0];
    const perArea = Object.entries(D.aree).map(([a, nome]) => [a, nome, D.proposte.filter((p) => p.area === a)]);
    const fondi = [...new Set(D.coperture.map((c) => String(c.fondo_id).toUpperCase()))];
    return `${schedeProgramma("proponi")}
      <p class="risposta">Componi il tuo programma con le stesse regole del nostro: scegli le misure e la loro versione, poi le coperture con cui pagarle. La pagina controlla subito se i conti tornano senza deficit, se tocchi una linea rossa e che effetto ha sui 10 valori. Si usano solo le ${D.coperture.length} coperture verificate: una copertura nuova si propone a parte e passa dallo stesso esame.</p>
      ${(D.proposte_validate || []).length ? `<details class="pp-gruppo pp-validati"><summary>Programmi già validati (${D.proposte_validate.length})</summary><ul class="pp-lista">${D.proposte_validate.slice().reverse().map((e) => `<li><span class="pp-nome"><strong>${esc(e.nome)}</strong> <span class="nota">${esc(dataBreve(e.data))} · ${e.misure} misure · ${nf(e.spesa)} mld · ${e.esito === "valido" ? "conti in ordine" : "da sistemare"} · regge sui valori in ${Math.round(e.robustezza * 100)} casi su 100 rispetto all'intermedio</span></span><span><a class="btn s" href="#/programma/proponi?${esc(e.codice)}">Apri</a> ${ext(repo + "/blob/main/proposte/" + encodeURIComponent(e.file), "Rapporto")}</span></li>`).join("")}</ul></details>` : ""}
      <div class="pp" id="pp-app" data-rif="${esc(rif.id)}">
        <div class="pp-scelte">
          <div class="card pp-avvio">
            <label for="pp-nome">Nome del programma</label><input id="pp-nome" type="text" maxlength="80" placeholder="Per esempio: più scuola e più treni" value="${esc(PP.nome)}">
            <label for="pp-da">Parti da</label>
            <select id="pp-da"><option value="">Scegli un punto di partenza</option><option value="vuoto">Un programma vuoto</option>${D.scenari.map((s) => `<option value="${esc(s.id)}">${esc(s.nome)} (${nf(s.spesa, 1)} mld)</option>`).join("")}</select>
            <label for="pp-cerca">Cerca tra misure e coperture</label><input id="pp-cerca" type="search" placeholder="scuola, treni, pensioni, IMU…">
          </div>
          <h2 class="pp-titolo">${icona("list-checks")}Le misure</h2>
          ${perArea.map(([a, nome, ps]) => `<details class="pp-gruppo"><summary>${esc(nome)} <span class="nota" data-conta-area="${a}"></span></summary><ul class="pp-lista">${ps.map((p) => `<li data-testo="${esc((p.id + " " + p.titolo).toLowerCase())}"><span class="pp-nome"><a href="${linkP(p.id)}" title="${esc(p.id)}">${esc(tit(p.titolo))}</a>${p.classe === "robusta" ? " " + chipClasse("robusta") : ""}</span>
              <select data-pp-misura="${esc(p.id)}" aria-label="Versione di ${esc(tit(p.titolo))}"><option value="">Non inclusa</option>${p.varianti.map((v) => `<option value="${esc(v.variante)}">${NOME_V[v.variante] || esc(v.variante)} · ${nf(v.costo)} mld${MOT.linee_rosse[p.id + ":" + v.variante] ? " · linea rossa" : ""}</option>`).join("")}</select></li>`).join("")}</ul></details>`).join("")}
          <h2 class="pp-titolo">${icona("coins")}Le coperture</h2>
          ${fondi.map((f) => `<details class="pp-gruppo"><summary>${esc(NOMI_FONDI_CORTI[f] || MOT.nomi_fondi[f] || f)} <span class="nota" data-conta-fondo="${esc(f)}"></span></summary><ul class="pp-lista">${D.coperture.filter((c) => String(c.fondo_id).toUpperCase() === f).map((c) => `<li data-testo="${esc((c.misura_id + " " + c.descrizione + " " + (c.chi_paga || "")).toLowerCase())}"><label class="pp-cop"><input type="checkbox" data-pp-cop="${esc(c.misura_id)}"><span><span class="pp-desc">${esc(c.descrizione)}</span><span class="nota">${esc(c.misura_id)} · ${nf(c.gettito_min)}–${nf(c.gettito_max)} mld · paga: ${esc(c.chi_paga || "—")}${(+c.EQU || 0) < 0 ? " · pesa di più su chi ha meno" : ""}${MOT.linee_rosse[c.misura_id] ? " · linea rossa" : ""}</span></span></label></li>`).join("")}</ul></details>`).join("")}
        </div>
        <aside class="card pp-esito" aria-live="polite"><div id="pp-esito"></div></aside>
      </div>`;
  }
  function ppEsito() {
    const k = ppConti(PP.m, PP.c), rif = D.scenari.find((s) => s.id === $("#pp-app").dataset.rif);
    const kr = ppConti(Object.fromEntries(Object.entries(rif.misure).map(([p, x]) => [p, x.variante])), new Set(rif.coperture || []));
    const ok = !k.avvisi.length && k.n > 0, manca = k.gen.spesa > k.gen.gettito + 1e-6;
    const max = Math.max(...k.val.map(Math.abs), ...kr.val.map(Math.abs), 1);
    const barra = (x, cls) => `<span class="pp-b ${cls}${x < 0 ? " neg" : ""}" style="width:${(Math.abs(x) / max * 50).toFixed(1)}%"></span>`;
    const corpo = `Nome: ${PP.nome || "Senza nome"}\n\nLink: ${ppLink()}\n\nMisure: ${k.n}, spesa a regime ${nf(k.totale)} mld. Coperture: ${k.nc}, ${nf(k.gettitoTot)} mld.\n\nPerché propongo questo programma (facoltativo):\n`;
    $("#pp-esito").innerHTML = `
      <h2>${ok ? icona("circle-check") + "I conti tornano" : k.n ? icona("triangle-alert") + "Da sistemare" : icona("circle-dashed") + "Il tuo programma"}</h2>
      <dl class="pp-cifre">
        <div><dt>Misure</dt><dd>${k.n}</dd></div><div><dt>Spesa a regime</dt><dd>${nf(k.totale)} mld</dd></div>
        <div><dt>Coperture</dt><dd>${k.nc} · ${nf(k.gettitoTot)} mld</dd></div>
        <div><dt>Risorse generali</dt><dd class="${manca ? "rosso" : "verde"}">${nf(Math.abs(k.gen.gettito - k.gen.spesa))} mld ${manca ? "mancanti" : "di margine"}</dd></div>
      </dl>
      ${k.vincolati.length ? `<p class="nota">Fondi vincolati: ${k.vincolati.map((x) => `${esc(MOT.nomi_fondi[x.f] || x.f)} ${nf(x.spesa)} su ${nf(x.disp)}`).join(" · ")}${k.tariffe ? `. Pagati con tariffe, fuori bilancio: ${nf(k.tariffe)} mld` : ""}.</p>` : ""}
      ${k.avvisi.length ? `<ul class="pp-avvisi">${k.avvisi.map((t) => `<li>${icona("octagon-x")}<span>${esc(t)}</span></li>`).join("")}</ul>` : ""}
      ${k.nc ? `<p class="nota">Coperture che pesano di più su chi ha meno: ${nf(k.regressive)} mld su ${nf(k.gettitoTot)} (${Math.round(k.regressive / (k.gettitoTot || 1) * 100)}%).</p>` : ""}
      <h3>Effetto sui 10 valori</h3><p class="nota">Barra scura: il tuo programma. Barra chiara: il ${esc(rif.nome.toLowerCase())}. Punteggio indicativo dai tre valutatori del panel.</p>
      <ul class="pp-valori">${D.valori.map((v, j) => `<li><span class="pp-v">${esc(v.nome)}</span><span class="pp-asse"><span class="pp-zero"></span>${barra(kr.val[j], "rif")}${barra(k.val[j], "tuo")}</span><span class="num">${nf(k.val[j], 1)}</span></li>`).join("")}</ul>
      <div class="azioni"><button class="btn primario s" type="button" id="pp-copia">${icona("link-2")}Copia il link</button>
        ${ok ? `<a class="btn s" href="${esc(repo + "/issues/new?title=" + encodeURIComponent("[Programma proposto] " + (PP.nome || "Senza nome")) + "&body=" + encodeURIComponent(corpo))}" target="_blank" rel="noopener">${icona("send")}Invia per la validazione</a>` : `<button class="btn s" type="button" disabled>${icona("send")}Invia per la validazione</button>`}</div>
      <p class="nota">${ok ? "La validazione completa rifà i conti anno per anno dal 2027 al 2035 e controlla la robustezza con migliaia di pesi diversi tra i valori. L'esito viene pubblicato accanto agli altri programmi. Per inviare serve un account GitHub gratuito." : k.n ? "Per inviarlo, sistema prima i punti in rosso." : "Scegli almeno una misura."}</p>`;
    icone();
    $("#pp-copia").addEventListener("click", async () => { try { await navigator.clipboard.writeText(ppLink()); $("#pp-copia").innerHTML = icona("check") + "Link copiato"; icone(); } catch (e) { prompt("Copia il link:", ppLink()); } });
    Object.keys(D.aree).forEach((a) => { const n = Object.keys(PP.m).filter((p) => p.startsWith(a + "-")).length; const el = $(`[data-conta-area="${a}"]`); if (el) el.textContent = n ? `· ${n} ${n === 1 ? "scelta" : "scelte"}` : ""; });
    $$("[data-conta-fondo]").forEach((el) => { const n = D.coperture.filter((c) => String(c.fondo_id).toUpperCase() === el.dataset.contaFondo && PP.c.has(c.misura_id)).length; el.textContent = n ? `· ${n} ${n === 1 ? "attiva" : "attive"}` : ""; });
    history.replaceState(null, "", "#/programma/proponi?" + ppCodice());
  }
  function montaProponi() {
    const sincronizza = () => {
      $$("[data-pp-misura]").forEach((s) => { s.value = PP.m[s.dataset.ppMisura] || ""; });
      $$("[data-pp-cop]").forEach((c) => { c.checked = PP.c.has(c.dataset.ppCop); });
      ppEsito();
    };
    $$("[data-pp-misura]").forEach((s) => s.addEventListener("change", () => { if (s.value) PP.m[s.dataset.ppMisura] = s.value; else delete PP.m[s.dataset.ppMisura]; ppEsito(); }));
    $$("[data-pp-cop]").forEach((c) => c.addEventListener("change", () => { if (c.checked) PP.c.add(c.dataset.ppCop); else PP.c.delete(c.dataset.ppCop); ppEsito(); }));
    $("#pp-nome").addEventListener("input", (e) => { PP.nome = e.target.value.trim(); ppEsito(); });
    $("#pp-da").addEventListener("change", (e) => {
      const v = e.target.value; if (!v) return;
      if ((Object.keys(PP.m).length || PP.c.size) && !confirm("Sostituire le scelte fatte finora?")) { e.target.value = ""; return; }
      const nome = $("#pp-nome").value.trim();
      ppCarica(new URLSearchParams(v === "vuoto" ? "" : "da=" + v)); PP.nome = nome; e.target.value = ""; sincronizza();
    });
    $("#pp-cerca").addEventListener("input", (e) => {
      const t = e.target.value.toLowerCase().trim();
      $$(".pp-lista li").forEach((li) => { li.hidden = !!t && !li.dataset.testo.includes(t); });
      $$(".pp-gruppo").forEach((d) => { const vis = [...d.querySelectorAll("li")].some((li) => !li.hidden); d.hidden = !vis; if (t && vis) d.open = true; });
    });
    sincronizza();
  }

  function strategia() {
    const O = D.oceano_blu || {}, F = O.fattori || [];
    const W = 760, H = 320, sx = 40, dx = 130, top = 16, bot = 130, n = F.length;
    const x = (i) => sx + (n > 1 ? i * (W - sx - dx) / (n - 1) : 0), y = (v) => top + (10 - v) * (H - top - bot) / 10;
    const curva = (k, cls) => `<polyline class="sc-l ${cls}" points="${F.map((f, i) => `${x(i).toFixed(1)},${y(+f[k] || 0).toFixed(1)}`).join(" ")}"/>${F.map((f, i) => `<circle class="sc-p ${cls}" cx="${x(i).toFixed(1)}" cy="${y(+f[k] || 0).toFixed(1)}" r="4"><title>${esc(f.nome)}: ${f[k]}</title></circle>`).join("")}`;
    return `${schedeProgramma("strategia")}
      <p class="risposta">Dove compete oggi la politica e dove sceglie di stare GovernAI. Analisi con il metodo della strategia oceano blu: non battere gli altri sugli stessi fattori, ma cambiare i fattori.</p>
      ${O.slogan ? `<p class="dato-grande">«${esc(O.slogan)}»</p>` : ""}
      <section class="card"><h2>Il canvas strategico <small>quanto ciascuno investe su ogni fattore, da 0 a 10</small></h2>
        <div class="sc-leg"><span class="gov">Manovra tipica del governo</span><span class="par">Programmi tipici dei partiti</span><span class="gai">GovernAI</span></div>
        <div class="sc-scroll"><svg class="canvas-strategico" viewBox="0 0 ${W} ${H}" role="img" aria-label="Canvas strategico: ${esc(F.map((f) => `${f.nome}: governo ${f.governo}, partiti ${f.partiti}, GovernAI ${f.governai}`).join("; "))}">
          ${[0, 5, 10].map((v) => `<line class="sc-g" x1="${sx}" x2="${W - dx}" y1="${y(v)}" y2="${y(v)}"/><text class="sc-a" x="${sx - 8}" y="${y(v) + 4}" text-anchor="end">${v}</text>`).join("")}
          ${curva("governo", "gov")}${curva("partiti", "par")}${curva("governai", "gai")}
          ${F.map((f, i) => `<text class="sc-x" transform="translate(${x(i).toFixed(1)},${H - bot + 14}) rotate(40)">${esc(f.nome.length > 30 ? f.nome.slice(0, 29) + "…" : f.nome)}</text>`).join("")}
        </svg></div>
        <details><summary>Perché questi punteggi</summary><ul class="elenco">${F.map((f) => `<li><strong>${esc(f.nome)}</strong> (governo ${f.governo}, partiti ${f.partiti}, GovernAI ${f.governai}): ${codici(esc(f.perche || ""))}</li>`).join("")}</ul></details>
      </section>
      ${O.errc ? `<section class="blocco"><h2>Che cosa cambia GovernAI <small>elimina, riduce, aumenta, crea</small></h2>${grigliaErrc(O.errc, "Griglia del programma")}</section>` : ""}
      ${(O.non_clienti || []).length ? `<section class="blocco"><h2>Chi oggi la politica non raggiunge</h2><div class="griglia g3">${O.non_clienti.map((c) => `<div class="card"><p class="etichetta">${esc(c.fascia)}</p><h3>${esc(c.chi)}</h3><p>${codici(esc(c.offerta))}</p></div>`).join("")}</div></section>` : ""}
      <p class="nota">Il rapporto completo, con rischi e punti deboli dichiarati: ${ext(repo + "/blob/main/programma/oceano_blu.md", "programma/oceano_blu.md")}. Ogni proposta ha la sua griglia nella scheda.</p>`;
  }

  // ---------- L'AI come chiave per l'Italia (programma/ai_pagina.yaml) ----------
  function aiPagina() {
    const P = D.ai || {};
    if (!P.in_breve) return `${schedeProgramma("ai")}${vuoto("Pagina non ancora disponibile.")}`;
    const prop = (P.proposte || []).map((id) => proposta(id)).filter(Boolean);
    return `${schedeProgramma("ai")}
      <p class="risposta">${esc(P.in_breve)}</p>
      <section class="blocco"><h2>Da dove partiamo <small>dati ufficiali, fonte in ogni riquadro</small></h2>
        <div class="griglia g3 ai-dati">${(P.dati || []).map((x) => `<div class="card"><p class="ai-num">${esc(x.numero)}</p><p>${esc(x.testo)}</p><p class="nota">${esc(x.fonte)}</p></div>`).join("")}</div></section>
      <section class="card blocco"><h2>Le macchine e le persone</h2><p>${esc(P.tesi || "")}</p></section>
      <section class="blocco"><h2>La lettura ragionata</h2>
        <div class="quattro">${Q4.map(([k, t, ic]) => `<div class="card q4"><p class="q4-t">${icona(ic)}${t}</p><p>${codici(esc(P[k] || ""))}</p></div>`).join("")}</div>
        ${P.oceano_blu ? `<h3 class="q4-sotto">Che cosa cambia <small>griglia della strategia oceano blu</small></h3>${grigliaErrc(P.oceano_blu, "Elimina, riduce, aumenta, crea")}` : ""}
      </section>
      ${P.elusione ? `<section class="blocco"><h2>Contro chi ama aggirare le regole</h2><p>${esc(P.elusione.intro || "")}</p>
        <div class="tabella-scorre"><table class="tabella a-card"><thead><tr><th>Il trucco</th><th>La regola che lo chiude</th></tr></thead>
        <tbody>${(P.elusione.righe || []).map((r) => `<tr><td class="principale">${esc(r.trucco)}</td><td data-etichetta="Regola">${esc(r.regola)}</td></tr>`).join("")}</tbody></table></div></section>` : ""}
      ${P.tasse ? `<section class="blocco"><h2>Quanto si risparmierebbe in tasse <small>stima indicativa, a regime</small></h2><p>${esc(P.tasse.intro || "")}</p>
        <div class="tabella-scorre"><table class="tabella a-card"><thead><tr><th>Scenario</th><th class="num">Posti non sostituiti</th><th class="num">Risparmio lordo</th><th class="num">Taglio delle tasse l'anno</th><th class="num">Per contribuente IRPEF</th><th class="num">Rispetto all'IRPEF</th></tr></thead>
        <tbody>${(P.tasse.righe || []).map((r) => `<tr><td class="principale">${esc(r.scenario)}</td><td class="num" data-etichetta="Posti non sostituiti">${esc(r.posti)}</td><td class="num" data-etichetta="Risparmio lordo">${esc(r.lordo)}</td><td class="num" data-etichetta="Taglio delle tasse"><strong>${esc(r.tasse)}</strong></td><td class="num" data-etichetta="Per contribuente">${esc(r.persona)}</td><td class="num" data-etichetta="Rispetto all'IRPEF">${esc(r.irpef)}</td></tr>`).join("")}</tbody></table></div>
        <details class="pv-metodo"><summary>Le ipotesi del calcolo</summary><ul>${(P.tasse.ipotesi || []).map((x) => `<li>${esc(x)}</li>`).join("")}</ul></details>
        ${P.tasse.riesame ? `<h3>In più, il riesame delle funzioni (09-C12) <small>dopo i suoi tre anni</small></h3><p>${esc(P.tasse.riesame.intro || "")}</p>
        <div class="tabella-scorre"><table class="tabella a-card"><thead><tr><th>Scenario</th><th class="num">Persone ricollocate</th><th class="num">Risparmio netto</th><th class="num">Alle tasse (50%)</th><th class="num">Ai servizi (25%)</th><th class="num">Al debito (25%)</th><th class="num">Per contribuente IRPEF</th></tr></thead>
        <tbody>${(P.tasse.riesame.righe || []).map((r) => `<tr><td class="principale">${esc(r.scenario)}</td><td class="num" data-etichetta="Persone ricollocate">${esc(r.persone)}</td><td class="num" data-etichetta="Risparmio netto">${esc(r.netto)}</td><td class="num" data-etichetta="Alle tasse"><strong>${esc(r.tasse)}</strong></td><td class="num" data-etichetta="Ai servizi">${esc(r.servizi)}</td><td class="num" data-etichetta="Al debito">${esc(r.debito)}</td><td class="num" data-etichetta="Per contribuente">${esc(r.persona)}</td></tr>`).join("")}</tbody></table></div>
        <details class="pv-metodo"><summary>Le ipotesi del calcolo del riesame</summary><ul>${(P.tasse.riesame.ipotesi || []).map((x) => `<li>${esc(x)}</li>`).join("")}</ul></details>` : ""}</section>` : ""}
      ${P.stime ? `<section class="blocco"><h2>Quanti posti ripetitivi si possono risparmiare</h2><p>${esc(P.stime.intro || "")}</p>
        <div class="tabella-scorre"><table class="tabella a-card"><thead><tr><th>Chi lo dice</th><th>Che cosa dice</th></tr></thead>
        <tbody>${(P.stime.righe || []).map((r) => `<tr><td class="principale">${esc(r.chi)}</td><td data-etichetta="Stima">${esc(r.cosa)}</td></tr>`).join("")}</tbody></table></div>
        <p class="nota">Fonti: ${esc(P.stime.fonti || "")}</p></section>` : ""}
      ${prop.length ? `<section class="blocco"><h2>Le proposte <small>${prop.length} nel programma</small></h2>
        <ul class="ai-prop">${prop.map((p) => `<li><a href="${linkP(p.id)}">${esc(tit(p.titolo))}</a> <span class="codice">${esc(p.id)}</span></li>`).join("")}</ul></section>` : ""}
      ${(P.limiti || []).length ? `<div class="avviso"><div class="avviso-titolo">${icona("info")}Limiti da tenere presenti</div><ul>${P.limiti.map((x) => `<li>${esc(x)}</li>`).join("")}</ul></div>` : ""}
      <p class="nota">Testi e fonti: ${ext(repo + "/blob/main/programma/ai_pagina.yaml", "programma/ai_pagina.yaml")}. Le proposte 09-C11 e 09-C12, con l'articolato e il controllo giuridico, sono nelle loro schede.</p>`;
  }

  // ---------- 50 anni di scelte (cartella storia/) ----------
  const ST = D.storia || { periodi: [], decisioni: [], serie: {} };
  const PAESI = { IT: "Italia", FR: "Francia", DE: "Germania", ES: "Spagna", EA: "Area euro", UE27: "Unione europea", Nord: "Nord", Centro: "Centro", Mezzogiorno: "Mezzogiorno" };
  const GIUDIZIO = { "efficace": ["favorevole", "circle-check", "Efficace"], "efficace in parte": ["info", "circle-dot", "Efficace in parte"], "inefficace": ["attenzione", "circle-minus", "Inefficace"], "effetti negativi": ["critico", "circle-x", "Effetti negativi"], "evidenza insufficiente": ["", "circle-dashed", "Prove insufficienti"] };
  const SERIE_TITOLI = { pil_pro_capite_indice: "Ricchezza prodotta per abitante (1977 = 100)", pil_pro_capite_pps_ue27: "Ricchezza per abitante a parità di potere d'acquisto (UE = 100)", produttivita_oraria_crescita: "Crescita della produttività per ora lavorata (% l'anno)", debito_pil: "Debito pubblico (% del PIL)", saldo_primario_pil: "Saldo primario, al netto degli interessi (% del PIL)", pressione_fiscale_ocse: "Tasse e contributi (% del PIL)", spesa_pubblica_pil: "Spesa pubblica (% del PIL)", occupazione_15_64: "Persone occupate tra 15 e 64 anni (%)", occupazione_femminile_15_64: "Donne occupate tra 15 e 64 anni (%)", disoccupazione_giovanile: "Disoccupazione tra 15 e 24 anni (%)", spread_bund: "Differenza di rendimento con i titoli tedeschi (punti base)", inflazione: "Inflazione (% l'anno)", fecondita: "Figli per donna", emigrazione_cittadini: "Cittadine e cittadini che emigrano (persone l'anno)", laureati_25_34: "Laureate e laureati tra 25 e 34 anni (%)", poverta_assoluta: "Persone in povertà assoluta (%)", divario_nord_sud: "Ricchezza per abitante del Mezzogiorno (% del Centro-Nord)" };
  const periodoDi = (anno) => ST.periodi.find((x) => +anno >= +x.da && +anno <= +x.a);
  function graficoStoria(nome) {
    const S = ST.serie[nome]; if (!S) return vuoto("Serie non disponibile.");
    let dati = Object.entries(S.dati).filter(([k]) => ["IT", "FR", "DE", "ES", "Nord", "Centro", "Mezzogiorno"].includes(k) || (k === "IT"));
    const tutti = dati.flatMap(([, v]) => v.map((x) => x[1])); if (!tutti.length) return vuoto("Serie non disponibile.");
    let lo = Math.min(...tutti), hi = Math.max(...tutti); const marg = (hi - lo) * 0.08 || 1; lo -= marg; hi += marg; if (lo > 0 && lo < (hi - lo) * 0.5) lo = 0;
    const W = 760, H = 300, sx = 46, dx = 14, top = 26, bot = 28, A0 = 1970, A1 = 2025;
    const x = (a) => sx + (a - A0) * (W - sx - dx) / (A1 - A0), y = (v) => top + (hi - v) * (H - top - bot) / (hi - lo);
    const passo = (hi - lo) > 80 ? 20 : (hi - lo) > 30 ? 10 : (hi - lo) > 8 ? 2 : (hi - lo) > 3 ? 1 : 0.5;
    const tacche = []; for (let t = Math.ceil(lo / passo) * passo; t <= hi; t += passo) tacche.push(t);
    const bande = ST.periodi.map((pp, i) => `<rect class="st-banda ${i % 2 ? "b" : "a"}" x="${x(Math.max(+pp.da, A0)).toFixed(1)}" y="${top - 18}" width="${(x(Math.min(+pp.a, A1) + 1) - x(Math.max(+pp.da, A0))).toFixed(1)}" height="${H - bot - top + 18}"/><text class="st-bt" x="${(x(Math.max(+pp.da, A0)) + 4).toFixed(1)}" y="${top - 6}">${pp.da}</text>`).join("");
    const linee = dati.map(([k, v]) => `<polyline class="st-l ${k === "IT" || k === "Mezzogiorno" ? "it" : "alt " + k}" points="${v.filter((q) => q[0] >= A0).map(([a, val]) => `${x(a).toFixed(1)},${y(val).toFixed(1)}`).join(" ")}"><title>${esc(PAESI[k] || k)}</title></polyline>`).join("");
    const ultimi = dati.map(([k, v]) => { const u = v[v.length - 1]; return u ? `<span class="st-leg ${k === "IT" || k === "Mezzogiorno" ? "it" : "alt " + k}">${esc(PAESI[k] || k)} <strong>${nf(u[1], Math.abs(u[1]) >= 100 ? 0 : 1)}</strong> <small>(${u[0]})</small></span>` : ""; }).join("");
    return `<div class="st-legenda">${ultimi}</div>
      <div class="sc-scroll"><svg class="st-grafico" data-serie="${esc(nome)}" viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(SERIE_TITOLI[nome] || nome)}, dal 1970 al 2025: ${esc(dati.map(([k, v]) => `${PAESI[k] || k} da ${nf((v[0] || [])[1], 1)} nel ${(v[0] || [])[0]} a ${nf((v[v.length - 1] || [])[1], 1)} nel ${(v[v.length - 1] || [])[0]}`).join("; "))}">
        ${bande}${tacche.map((t) => `<line class="sc-g" x1="${sx}" x2="${W - dx}" y1="${y(t).toFixed(1)}" y2="${y(t).toFixed(1)}"/><text class="sc-a" x="${sx - 6}" y="${(y(t) + 4).toFixed(1)}" text-anchor="end">${nf(t, passo < 1 ? 1 : 0)}</text>`).join("")}
        ${lo < 0 && hi > 0 ? `<line class="st-zero" x1="${sx}" x2="${W - dx}" y1="${y(0).toFixed(1)}" y2="${y(0).toFixed(1)}"/>` : ""}
        ${[1970, 1980, 1990, 2000, 2010, 2020].map((a) => `<text class="sc-a" x="${x(a).toFixed(1)}" y="${H - 8}" text-anchor="middle">${a}</text>`).join("")}
        ${linee}<line class="st-cursore" x1="0" x2="0" y1="${top - 18}" y2="${H - bot}" visibility="hidden"/>
      </svg></div><p class="nota st-valori" aria-live="polite">Passa sul grafico per leggere i valori di un anno.</p>
      <p class="nota">${esc(S.descrizione)} Fonte: ${S.url ? ext(S.url, esc(S.fonte)) : esc(S.fonte)}. Le bande colorate sono i sei periodi.</p>`;
  }
  function storiaVista(params) {
    if (!ST.decisioni.length) return `${schedeDati("storia")}${vuoto("La storia non è ancora disponibile.")}`;
    const pid = params.get("p") || "", P = ST.periodi.find((x) => x.id === pid);
    const serie = ST.serie[params.get("s")] ? params.get("s") : "pil_pro_capite_indice";
    const conta = (lista) => Object.keys(GIUDIZIO).map((g) => [g, lista.filter((d) => d.giudizio === g).length]);
    const decP = P ? ST.decisioni.filter((d) => +d.anno >= +P.da && +d.anno <= +P.a) : ST.decisioni;
    const ambiti = [...new Set(ST.decisioni.map((d) => d.ambito))].sort();
    const q4p = (pp) => `<div class="quattro">${Q4.map(([k, t, ic]) => `<div class="card q4"><p class="q4-t">${icona(ic)}${t}</p><p>${linkDec(esc(pp[k] || ""))}</p></div>`).join("")}</div>`;
    return `${schedeDati("storia")}
      <p class="risposta">Dal 1977 a oggi: ${ST.decisioni.length} decisioni dei governi e i loro effetti misurati, ${Object.keys(ST.serie).length} serie di dati confrontate con Francia, Germania e Spagna. Si giudicano le decisioni, non le persone o i partiti. Le coincidenze tra una decisione e un cambio nei dati sono ipotesi, non prove.</p>
      <nav class="st-periodi" aria-label="Periodi"><a href="#/dati/storia${serie !== "pil_pro_capite_indice" ? "?s=" + serie : ""}" class="st-p ${P ? "" : "attivo"}" ${P ? "" : 'aria-current="page"'}><span class="st-anni">1977-2026</span><span>Tutti i periodi</span></a>${ST.periodi.map((pp) => `<a href="#/dati/storia?p=${esc(pp.id)}${serie !== "pil_pro_capite_indice" ? "&s=" + serie : ""}" class="st-p ${pp.id === pid ? "attivo" : ""}" ${pp.id === pid ? 'aria-current="page"' : ""}><span class="st-anni">${pp.da}-${pp.a}</span><span>${esc(pp.titolo)}</span></a>`).join("")}</nav>
      ${P ? `<section class="blocco"><h2>${P.da}-${P.a}: ${esc(P.titolo)}</h2><p class="testo-lettura">${esc(P.in_breve || "")}</p>
          ${(P.dati || []).length ? `<div class="st-dati">${P.dati.map((d) => `<div class="card kpi"><p class="etichetta">${esc(d.etichetta)}</p><p class="st-num">${esc(d.valore)}</p><p class="nota">${esc(String(d.fonte || "").replace(/^([a-z0-9_]+)\s*/, (m, k) => SERIE_TITOLI[k] ? "" : m).replace(/^\((.*)\)$/, "Fonte: $1"))}</p></div>`).join("")}</div>` : ""}
          ${q4p(P)}
          ${P.lezione ? `<div class="avviso" style="margin-top:12px"><div class="avviso-titolo">${icona("lightbulb")}La lezione per oggi</div><p>${linkDec(esc(P.lezione))}</p></div>` : ""}
        </section>`
        : `<section class="blocco"><h2>I sei periodi</h2><div class="griglia g3">${ST.periodi.map((pp) => `<a class="card st-card" href="#/dati/storia?p=${esc(pp.id)}"><p class="etichetta">${pp.da}-${pp.a}</p><h3>${esc(pp.titolo)}</h3><p>${esc(pp.in_breve || "")}</p></a>`).join("")}</div></section>`}
      <section class="card blocco"><h2>I dati in 50 anni</h2>
        <label for="st-serie" class="vh">Indicatore</label>
        <select id="st-serie" class="st-sel">${Object.keys(ST.serie).map((k) => `<option value="${esc(k)}" ${k === serie ? "selected" : ""}>${esc(SERIE_TITOLI[k] || k)}</option>`).join("")}</select>
        <div id="st-grafico">${graficoStoria(serie)}</div>
      </section>
      <section class="blocco"><h2>Le decisioni${P ? ` del periodo ${P.da}-${P.a}` : ""} <small>${decP.length} · ${conta(decP).filter(([, n]) => n).map(([g, n]) => `${n} ${GIUDIZIO[g][2].toLowerCase()}`).join(" · ")}</small></h2>
        <div class="filtri"><label class="vh" for="st-cerca">Cerca</label><input id="st-cerca" type="search" placeholder="Cerca: pensioni, condono, euro…">
          <label class="vh" for="st-ambito">Ambito</label><select id="st-ambito"><option value="">Tutti gli ambiti</option>${ambiti.map((a) => `<option>${esc(a)}</option>`).join("")}</select>
          <label class="vh" for="st-giudizio">Giudizio</label><select id="st-giudizio"><option value="">Tutti i giudizi</option>${Object.entries(GIUDIZIO).map(([g, c]) => `<option value="${esc(g)}">${esc(c[2])}</option>`).join("")}</select></div>
        <ul class="st-dec" id="st-dec">${decP.map((d) => `<li id="${esc(d.id)}" data-testo="${esc((d.decisione + " " + d.cosa_cambia + " " + d.atto + " " + d.ambito + " " + d.anno).toLowerCase())}" data-ambito="${esc(d.ambito)}" data-giudizio="${esc(d.giudizio)}"><details>
          <summary><span class="st-a">${esc(d.anno)}</span><span class="st-t">${esc(d.decisione)}<small>${esc(d.ambito)} · ${esc(d.atto)}</small></span>${chip(GIUDIZIO[d.giudizio] || ["", "circle-dashed", d.giudizio])}</summary>
          <div class="corpo"><p><strong>Che cosa cambia.</strong> ${esc(d.cosa_cambia)}</p>${d.effetto_conti && d.effetto_conti !== "n.d." ? `<p><strong>Effetto sui conti.</strong> ${esc(d.effetto_conti)}</p>` : ""}
            <p><strong>Effetti misurati.</strong> ${esc(d.effetti_misurati)}</p>
            <p class="nota">Solidità delle prove: ${esc(d.solidita_evidenza)} · ${esc(d.governo_anno)}${d.presidente_consiglio ? ` (presidenza del Consiglio: ${esc(d.presidente_consiglio)})` : ""} · ${esc(d.id)}</p>
            <p class="nota">${String(d.fonti || "").split(" | ").filter(Boolean).map((f, i) => { const u = (f.match(/https?:\/\/\S+/) || [])[0]; return u ? ext(u.replace(/[).,;]+$/, ""), `Fonte ${i + 1}`) : esc(f); }).join(" · ")}</p></div></details></li>`).join("")}</ul>
      </section>
      <p class="nota">File completi: ${ext(repo + "/blob/main/storia/decisioni_1977_2026.md", "catalogo delle decisioni")} · ${ext(repo + "/blob/main/storia/serie_lunghe.md", "serie lunghe")} · ${ext(repo + "/tree/main/storia", "dati e script")}.</p>`;
  }
  const linkDec = (t) => String(t).replace(/\b(D\d{3})\b/g, (m) => ST.decisioni.some((d) => d.id === m) ? `<a href="#/dati/storia?d=${m}" data-dec="${m}">${m}</a>` : m);
  function montaStoria() {
    const filtra = () => { const t = $("#st-cerca").value.toLowerCase().trim(), a = $("#st-ambito").value, g = $("#st-giudizio").value;
      $$("#st-dec li").forEach((li) => { li.hidden = (t && !li.dataset.testo.includes(t)) || (a && li.dataset.ambito !== a) || (g && li.dataset.giudizio !== g); }); };
    ["#st-cerca", "#st-ambito", "#st-giudizio"].forEach((x) => $(x).addEventListener("input", filtra));
    const agganciaGrafico = () => {
      const svg = $(".st-grafico"); if (!svg) return; const nome = svg.dataset.serie, S = ST.serie[nome];
      const cur = $(".st-cursore", svg), out = $(".st-valori");
      svg.addEventListener("mousemove", (e) => {
        const r = svg.getBoundingClientRect(), vb = svg.viewBox.baseVal, px = (e.clientX - r.left) * vb.width / r.width;
        const anno = Math.round(1970 + (px - 46) * (2025 - 1970) / (760 - 46 - 14)); if (anno < 1970 || anno > 2025) return;
        const xx = 46 + (anno - 1970) * (760 - 46 - 14) / 55; cur.setAttribute("x1", xx); cur.setAttribute("x2", xx); cur.setAttribute("visibility", "visible");
        const val = Object.entries(S.dati).map(([k, v]) => { const q = v.find((z) => z[0] === anno); return q && PAESI[k] && !["EA", "UE27"].includes(k) ? `${PAESI[k]} ${nf(q[1], Math.abs(q[1]) >= 100 ? 0 : 1)}` : ""; }).filter(Boolean);
        const pp = periodoDi(anno); out.textContent = `${anno}${pp ? " · " + pp.titolo : ""}: ${val.join(" · ") || "nessun dato"}`;
      });
      svg.addEventListener("mouseleave", () => cur.setAttribute("visibility", "hidden"));
    };
    $("#st-serie").addEventListener("change", (e) => {
      $("#st-grafico").innerHTML = graficoStoria(e.target.value); icone(); agganciaGrafico();
      const q = new URLSearchParams(location.hash.split("?")[1] || ""); q.set("s", e.target.value); q.delete("d"); history.replaceState(null, "", "#/dati/storia?" + q.toString());
    });
    agganciaGrafico();
    const d = new URLSearchParams(location.hash.split("?")[1] || "").get("d");
    if (d && $("#" + d)) { $("#" + d + " details").open = true; $("#" + d).scrollIntoView({ block: "center" }); }
  }

  // ---------- Chi paga davvero (analisi/chi_paga) ----------
  const CP = D.chi_paga || {};
  const LIVELLI = ["25000", "50000", "100000", "300000", "1000000"];
  function barreChiPaga(livello) {
    const righe = (CP.gruppi || []).map((g) => ({ g, v: (g.valori || {})[livello] })).filter((x) => x.v);
    if (!righe.length) return vuoto("Nessun gruppo con dati a questo livello di reddito.");
    righe.sort((a, b) => b.v[0] - a.v[0]);
    return `<ul class="cp-barre">${righe.map(({ g, v }) => `<li class="${esc(g.tipo)}"><span class="cp-nome">${esc(g.etichetta)}</span>
      <span class="cp-asse"><span class="cp-tot" style="width:${Math.min(v[1] || v[0], 70) / 70 * 100}%"></span><span class="cp-imp" style="width:${Math.min(v[0], 70) / 70 * 100}%"></span></span>
      <span class="num"><strong>${nf(v[0], 1)}%</strong>${v[1] && Math.abs(v[1] - v[0]) > 0.05 ? ` <small>${nf(v[1], 1)}% con i contributi</small>` : ""}</span></li>`).join("")}</ul>`;
  }
  // Prima e dopo le scelte del 16/11/2026: parità per le imprese di persone (01-P25 essenziale, con la patrimoniale minima)
  // e dividendi parcheggiati nelle holding (dentro 01-P19 piena). Utile lasciato tutto in impresa.
  function primaDopo() {
    const N = CP.neutralita || []; if (!N.length) return "";
    const RIGHE = [["Socio di SNC (2 soci al 50%)", "ESSENZIALE", "Socio di SNC"], ["Ditta individuale in ordinaria", "ESSENZIALE", "Ditta individuale"], ["Socio di SRL (senza holding)", "PIENA", "Socio di SRL"], ["SRL tramite holding, utili fermi", "PIENA", "SRL tramite holding, utili fermi"], ["SRL tramite holding, utili reinvestiti", "PIENA", "SRL tramite holding, utili reinvestiti"]];
    const LIV = [50000, 100000, 300000, 1000000];
    const cella = (g, v, r) => { const x = N.find((y) => y.gruppo === g && y.variante_proposta === v && +y.reddito_lordo === r && +y.quota_lasciata_in_impresa === 1); if (!x) return "<td>—</td>"; const d = +x.aliquota_imposte_dopo - +x.aliquota_imposte_prima;
      return `<td class="num" data-etichetta="${nf(r, 0)} €">${nf(+x.aliquota_imposte_prima, 1)}% ${Math.abs(d) < 0.05 ? `<span class="nota">invariata</span>` : `→ <strong class="${d < 0 ? "giu" : "su"}">${nf(+x.aliquota_imposte_dopo, 1)}%</strong>`}</td>`; };
    return `<section class="blocco"><h2>Prima e dopo le scelte del programma <small>solo imposte, utile lasciato tutto nell'impresa</small></h2>
      <div class="tabella-scorre"><table class="tabella cp-pd"><thead><tr><th>Forma d'impresa</th>${LIV.map((r) => `<th class="num">${nf(r, 0)} €</th>`).join("")}</tr></thead>
      <tbody>${RIGHE.map(([g, v, et]) => `<tr><td class="principale">${esc(et)}</td>${LIV.map((r) => cella(g, v, r)).join("")}</tr>`).join("")}</tbody></table></div>
      <p class="nota">SNC e ditta individuale: parità con le società (${codici("01-P25")}, versione essenziale, 24% fino a 100.000 € trattenuti per socio), attiva solo insieme alla patrimoniale minima (${codici("01-P24")}). Holding: dividendi della propria società fermi e non reinvestiti oltre la franchigia di 100.000 € l'anno per famiglia (${codici("01-P19")}). Chi preleva tutto non vede cambiamenti. Calcolo: ${ext(repo + "/blob/main/analisi/chi_paga/neutralita.py", "neutralita.py")}.</p></section>`;
  }
  function chiPaga(params) {
    if (!CP.gruppi) return `${schedeProgramma("chi-paga")}${vuoto("Analisi non ancora disponibile.")}`;
    const liv = LIVELLI.includes(params.get("r")) ? params.get("r") : "1000000";
    const pop = (CP.popolazione || []).filter((x) => x.numero && x.numero !== "n.d.");
    return `${schedeProgramma("chi-paga")}
      <p class="risposta">${esc(CP.in_breve || "")}</p>
      <section class="card blocco"><h2>Quante imposte paga lo stesso reddito <small>regole di legge del 2026, aliquota effettiva sul reddito lordo prodotto</small></h2>
        <div class="segmenti" role="group" aria-label="Reddito lordo prodotto">${LIVELLI.map((l) => `<a class="btn s ${l === liv ? "primario" : ""}" href="#/programma/chi-paga?r=${l}" ${l === liv ? 'aria-current="true"' : ""}>${nf(+l, 0)} €</a>`).join("")}</div>
        <div class="cp-leg"><span class="lavoro">Lavoro e pensione</span><span class="impresa">Impresa</span><span class="capitale">Capitale e holding</span><span class="contr">Parte più chiara: contributi, che danno una pensione</span></div>
        ${barreChiPaga(liv)}
        <p class="nota">Ipotesi principali: addizionali regionali e comunali medie, nessuna detrazione per spese, società senza dipendenti. Calcolatore, parametri e fonti: ${ext(repo + "/tree/main/analisi/chi_paga", "analisi/chi_paga")}. Alcuni gruppi non esistono a ogni livello: il forfettario arriva fino a 85.000 € di ricavi.</p>
      </section>
      <section class="blocco"><h2>La lettura ragionata</h2>
        <div class="quattro">${Q4.map(([k, t, ic]) => `<div class="card q4"><p class="q4-t">${icona(ic)}${t}</p><p>${codici(esc(CP[k] || ""))}</p></div>`).join("")}</div>
        ${CP.oceano_blu ? `<h3 class="q4-sotto">Che cosa vogliamo cambiare <small>griglia della strategia oceano blu</small></h3>${grigliaErrc(CP.oceano_blu, "Elimina, riduce, aumenta, crea")}` : ""}
      </section>
      ${CP.evasione ? `<div class="avviso attenzione"><div class="avviso-titolo">${icona("scale")}Il dato scomodo, detto con equilibrio</div><p>${codici(esc(CP.evasione))}</p></div>` : ""}
      ${pop.length ? `<section class="blocco"><h2>Chi c'è in ogni gruppo <small>dichiarazioni 2024, Ministero dell'economia</small></h2>
        <div class="tabella-scorre"><table class="tabella"><thead><tr><th>Gruppo</th><th class="num">Persone</th><th class="num">Reddito medio dichiarato</th><th class="num">Imposta media</th><th class="num">Quota dell'IRPEF</th></tr></thead>
        <tbody>${pop.map((x) => `<tr><td class="principale">${esc(x.gruppo)}</td><td class="num" data-etichetta="Persone">${/^\d+$/.test(x.numero) ? nf(+x.numero, 0) : esc(x.numero)}</td><td class="num" data-etichetta="Reddito medio">${/^\d+$/.test(x.reddito_dichiarato_medio_eur) ? nf(+x.reddito_dichiarato_medio_eur, 0) + " €" : esc(x.reddito_dichiarato_medio_eur)}</td><td class="num" data-etichetta="Imposta media">${/^\d+$/.test(x.imposta_netta_media_eur) ? nf(+x.imposta_netta_media_eur, 0) + " €" : esc(x.imposta_netta_media_eur)}</td><td class="num" data-etichetta="Quota IRPEF">${/^[\d.]+$/.test(x.quota_irpef_totale_pct) ? nf(+x.quota_irpef_totale_pct, 1) + "%" : esc(x.quota_irpef_totale_pct)}</td></tr>`).join("")}</tbody></table></div>
        <p class="nota">Medie su tutte le persone del gruppo, comprese quelle con imposta zero. Per dividendi, rendite e holding non esistono dati ufficiali per persona: per questo quei gruppi non sono in tabella. Dettagli e fonti: ${ext(repo + "/blob/main/analisi/chi_paga/popolazione.md", "popolazione.md")}.</p></section>` : ""}
      ${primaDopo()}
      ${(CP.proposte || []).length ? `<section class="blocco"><h2>Che cosa fa il programma</h2><ul class="elenco">${CP.proposte.filter((x) => proposta(x)).map((x) => `<li><a href="${linkP(x)}">${esc(tit(proposta(x).titolo))}</a> <span class="nota">${esc(x)}${rif.misure[x] ? " · nel programma intermedio" : ""}</span></li>`).join("")}</ul></section>` : ""}`;
  }

  // ---------- Governi a confronto (storia/governi_confronto.csv) ----------
  const GV = D.governi || { righe: [] };
  const AMBITI_GV = [["conti", "Conti pubblici"], ["crescita", "Crescita"], ["lavoro", "Lavoro"], ["qualità del lavoro", "Qualità del lavoro"], ["prezzi e mercati", "Prezzi e mercati"], ["società", "Società"]];
  const conVerso = (r) => r.rango != null && r.n && !String(r.verso).startsWith("descrittivo");
  const pos = (r) => r.n > 1 ? (r.n - r.rango) / (r.n - 1) * 100 : 100;
  function mediana(a) { const b = a.slice().sort((x, y) => x - y); const m = Math.floor(b.length / 2); return b.length ? (b.length % 2 ? b[m] : (b[m - 1] + b[m]) / 2) : null; }
  function governiVista(params) {
    if (!GV.righe.length) return `${schedeDati("governi")}${vuoto("Confronto non ancora disponibile.")}`;
    const ver = params.get("v") === "spostata" ? "spostata" : "base";
    const LG = GV.legislature && (GV.legislature.righe || []).length ? GV.legislature : null;
    const leg = !!LG && params.get("per") === "legislatura";
    const T = leg ? { ...GV, ...LG } : GV;   // testi della vista: per legislatura prendono quelli propri
    const R = (leg ? LG.righe : GV.righe).filter((r) => r.v === (ver === "spostata" ? "ritardo_1_anno" : "base"));
    const unita = [...new Map(R.map((r) => [r.u, r.g])).entries()];
    const sel = unita.find(([u]) => u === params.get("g")) ? params.get("g") : unita[unita.length - 1][0];
    const nomeSel = (unita.find(([u]) => u === sel) || [])[1] || "";
    const sintesi = (u) => Object.fromEntries(AMBITI_GV.map(([a]) => [a, mediana(R.filter((r) => r.u === u && r.amb === a && conVerso(r)).map(pos))]));
    const tutte = unita.map(([u, g]) => [u, g, sintesi(u), (R.find((r) => r.u === u) || {}).anni]);
    const classe = (x) => x == null ? "nd" : x >= 66.7 ? "alto" : x >= 33.3 ? "medio" : "basso";
    const righeSel = R.filter((r) => r.u === sel);
    const fmt = (x, um) => x == null ? "—" : `${nf(x, Math.abs(x) >= 100 ? 0 : 1)}${um && um.startsWith("%") ? "%" : um === "punti" ? " punti" : ""}`;
    const qp = leg ? "&per=legislatura" : "";
    const qv = (ver === "spostata" ? "&v=spostata" : "") + qp;
    const nome = leg ? ["legislatura", "Legislatura", "Tutte le legislature", "ultima", "prima"] : ["governo", "Governo", "Tutti i governi", "ultimo", "primo"];
    return `${schedeDati("governi")}
      <p class="risposta">${esc(T.in_breve || "")}</p>
      ${LG ? `<div class="segmenti" role="group" aria-label="Unità di confronto"><a class="btn s ${leg ? "" : "primario"}" href="#/dati/governi${ver === "spostata" ? "?v=spostata" : ""}">Per governo</a><a class="btn s ${leg ? "primario" : ""}" href="#/dati/governi?per=legislatura${ver === "spostata" ? "&v=spostata" : ""}">Per legislatura</a></div>` : ""}
      <div class="segmenti" role="group" aria-label="Versione"><a class="btn s ${ver === "base" ? "primario" : ""}" href="#/dati/governi?g=${esc(sel)}${qp}">Anni ${leg ? "della legislatura" : "del mandato"}</a><a class="btn s ${ver === "spostata" ? "primario" : ""}" href="#/dati/governi?g=${esc(sel)}&v=spostata${qp}">Anni spostati di uno (effetti in ritardo)</a></div>
      <p class="nota">Hai sentito un confronto e non sai se è giusto? ${`<a href="#/dati/verifica?g=${esc(sel)}${qp}">Verificalo indicatore per indicatore</a>`}.</p>
      <section class="card blocco"><h2>${nome[2]}, ambito per ambito <small>posizione rispetto ai vicini, da 0 (${nome[3]}) a 100 (${nome[4]})</small></h2>
        <div class="tabella-scorre"><table class="tabella gv-mappa"><thead><tr><th>${nome[1]}</th><th>Anni contati</th>${AMBITI_GV.map(([, t]) => `<th class="num">${esc(t)}</th>`).join("")}</tr></thead>
        <tbody>${tutte.map(([u, g, sx, anni]) => `<tr class="${u === sel ? "gv-sel" : ""}"><td class="principale"><a href="#/dati/governi?g=${esc(u)}${qv}">${esc(g)}</a></td><td data-etichetta="Anni">${esc(anni || "")}</td>${AMBITI_GV.map(([a, t]) => `<td class="num gv-c ${classe(sx[a])}" data-etichetta="${esc(t)}">${sx[a] == null ? "—" : Math.round(sx[a])}</td>`).join("")}</tr>`).join("")}</tbody></table></div>
        <p class="nota">Verde: primo terzo; giallo: terzo centrale; arancio: ultimo terzo. Ogni cella è la mediana delle posizioni degli indicatori dell'ambito; la pressione fiscale non entra, perché salire o scendere non è in sé meglio o peggio. Per la società il confronto usa solo il dato italiano.</p>
      </section>
      ${sezionePV(leg)}
      ${((leg ? LG.emerge : GV.emerge) || []).length ? `<section class="blocco"><h2>Che cosa emerge <small>${leg ? "tra le legislature" : "tra i governi"}, anni ${leg ? "della legislatura" : "del mandato"}</small></h2>
        <ol class="gv-emerge">${(leg ? LG.emerge : GV.emerge).map((x) => `<li class="card"><strong>${esc(x.titolo)}</strong><p>${esc(x.testo)}</p></li>`).join("")}</ol></section>` : ""}
      <section class="blocco"><h2>${esc(nomeSel)}, indicatore per indicatore</h2>
        <label class="vh" for="gv-sel">Scegli ${leg ? "la legislatura" : "il governo"}</label><select id="gv-sel" class="st-sel">${unita.map(([u, g]) => `<option value="${esc(u)}" ${u === sel ? "selected" : ""}>${esc(g)}</option>`).join("")}</select>
        <ul class="gv-ind">${righeSel.map((r) => `<li><span class="gv-nome">${esc(r.ind)}<small>${esc(r.amb)}</small></span>
          <span class="gv-scala" aria-hidden="true">${r.rango != null && r.n ? `<span class="gv-punto ${conVerso(r) ? classe(pos(r)) : "nd"}" style="left:${(r.n > 1 ? (r.rango - 1) / (r.n - 1) : 0) * 100}%"></span>` : ""}</span>
          <span class="gv-val">${r.rango != null ? `<strong>${r.rango}° su ${r.n}</strong>` : "—"}<small>Italia ${fmt(r.it, r.um)}${r.vic != null ? ` · vicini ${fmt(r.vic, r.um)}` : ""}${String(r.verso).startsWith("descrittivo") ? " · 1° = calo maggiore" : ""}</small></span></li>`).join("")}</ul>
        <p class="nota">La scala va dal 1° posto (a sinistra) all'ultimo (a destra). Il posto è calcolato sulla differenza con la media di Francia, Germania e Spagna; per povertà ed emigrazione sul solo dato italiano.</p>
      </section>
      <section class="blocco"><h2>La lettura ragionata</h2>
        <div class="quattro">${Q4.map(([k, t, ic]) => `<div class="card q4"><p class="q4-t">${icona(ic)}${t}</p><p>${codici(esc(T[k] || ""))}</p></div>`).join("")}</div>
        ${GV.oceano_blu ? `<h3 class="q4-sotto">Perché questo confronto è diverso <small>griglia della strategia oceano blu</small></h3>${grigliaErrc(GV.oceano_blu, "Elimina, riduce, aumenta, crea")}` : ""}
      </section>

      ${(GV.verifica || {}).ind ? `<section class="blocco" id="dati-usati"><h2>I dati usati <small>${GV.verifica.ind.length} indicatori, gli stessi per tutti</small></h2>
        <p class="nota">Ogni indicatore è una serie ufficiale scaricata con uno script ripetibile. «Media» vuol dire media degli anni contati; «variazione» vuol dire differenza tra l'anno prima dell'inizio e l'ultimo anno contato. Il confronto è sempre con la media di Francia, Germania e Spagna, tranne dove è indicato.</p>
        <div class="tabella-scorre"><table class="tabella gv-dati"><thead><tr><th>Indicatore</th><th>Che cosa misura</th><th>Come si conta</th><th>Fonte e anni</th></tr></thead>
        <tbody>${GV.verifica.ind.map((x) => `<tr><td class="principale" data-etichetta="Indicatore"><a href="#/dati/verifica?i=${esc(x.id)}${leg ? "&per=legislatura" : ""}">${esc(x.nome)}</a><small>${esc(x.ambito)}</small></td>
          <td data-etichetta="Che cosa misura">${esc(x.descr || "")}</td>
          <td data-etichetta="Come si conta">${x.tipo === "media" ? "media" : "variazione"}; ${x.verso === 1 ? "più alto è meglio" : x.verso === -1 ? "più basso è meglio" : "solo descrittivo"}${x.vicini ? "" : "; solo dato italiano"}</td>
          <td data-etichetta="Fonte e anni">${x.url && x.url.startsWith("http") ? ext(x.url.split(" ; ")[0], x.fonte) : esc(x.fonte)}<small>${esc(x.anni_dati || "")}</small><small>${ext(repo + "/blob/main/storia/serie/" + x.file + ".csv", "serie scaricata")}</small></td></tr>`).join("")}</tbody></table></div>
      </section>` : ""}
      ${(T.limiti || []).length ? `<div class="avviso"><div class="avviso-titolo">${icona("info")}Limiti da tenere presenti</div><ul>${T.limiti.map((x) => `<li>${esc(x)}</li>`).join("")}</ul></div>` : ""}
      <p class="nota">${leg ? `Tabelle complete e limiti: ${ext(repo + "/blob/main/storia/legislature_confronto.md", "rapporto per legislatura")} · ${ext(repo + "/blob/main/storia/governi_metodo.md", "metodo")} · ${ext(repo + "/blob/main/storia/script/legislature.py", "script")}.` : `Metodo, punto di partenza di ogni governo, shock esterni e decisioni del catalogo: ${ext(repo + "/blob/main/storia/governi_confronto.md", "rapporto completo")} · ${ext(repo + "/blob/main/storia/governi_metodo.md", "metodo")} · ${ext(repo + "/blob/main/storia/script/governi.py", "script")}.`}</p>`;
  }

  // ---------- Verifica un confronto (stessi dati di Governi a confronto) ----------
  function verificaVista(params) {
    const VF = GV.verifica || {};
    if (!GV.righe.length || !VF.ind) return `${schedeDati("verifica")}${vuoto("Verifica non ancora disponibile.")}`;
    const leg = params.get("per") === "legislatura" && GV.legislature && (GV.legislature.righe || []).length;
    const tutte = leg ? GV.legislature.righe : GV.righe;
    const base = tutte.filter((r) => r.v === "base"), rit = tutte.filter((r) => r.v === "ritardo_1_anno");
    const unita = [...new Map(base.map((r) => [r.u, r.g])).entries()];
    const u = unita.some(([x]) => x === params.get("g")) ? params.get("g") : unita[unita.length - 1][0];
    const I = VF.ind.find((x) => x.id === params.get("i")) || VF.ind.find((x) => x.id === "debito") || VF.ind[0];
    const rb = base.find((r) => r.u === u && r.ind === I.nome) || {}, rr = rit.find((r) => r.u === u && r.ind === I.nome) || {};
    const nomeU = (unita.find(([x]) => x === u) || [])[1] || "";
    const parola = leg ? "legislature" : "governi";
    const descr = I.verso === 0;
    const fmt = (x, um = I.unita) => x == null ? "n.d." : `${nf(x, Math.abs(x) >= 100 ? 0 : 1)}${um === "% del PIL" ? "% del PIL" : um.startsWith("%") ? "%" : um.startsWith("punti di PIL") ? " punti di PIL" : um === "punti" ? " punti" : um === "punti base" ? " punti base" : um === "migliaia" ? " mila" : ""}`;
    const maiu = (t) => t.charAt(0).toUpperCase() + t.slice(1);
    // il livello si misura in % (debito, occupazione...), la variazione in punti
    const fmtLiv = (x) => fmt(x, I.tipo === "variazione" && (I.unita === "punti" || I.unita.startsWith("punti di PIL")) ? (I.unita === "punti" ? "%" : "% del PIL") : I.unita);
    const segnato = (x) => x == null ? "n.d." : (x > 0 ? "+" : "") + fmt(x);
    const posiz = (k, n) => n > 1 ? (n - k) / (n - 1) * 100 : 100;
    const terzo = (x) => x == null ? "" : x >= 66.7 ? "nel primo terzo" : x >= 33.3 ? "nel terzo centrale" : "nell'ultimo terzo";
    const classe = (x) => x == null ? "nd" : x >= 66.7 ? "alto" : x >= 33.3 ? "medio" : "basso";
    // 1. assoluto: posto del solo dato italiano tra tutte le unità
    const conIt = base.filter((r) => r.ind === I.nome && r.it != null);
    const rkIt = rb.it == null || descr ? null : [1 + conIt.filter((r) => I.verso > 0 ? r.it > rb.it + 1e-9 : r.it < rb.it - 1e-9).length, conIt.length];
    const pAbs = rkIt ? posiz(...rkIt) : null;
    const pRel = !descr && I.vicini && rb.rango ? posiz(rb.rango, rb.n) : null;
    const pRit = !descr && rr.rango ? posiz(rr.rango, rr.n) : null;
    // 3. livello: valori dell'anno di partenza e dell'ultimo anno
    const S = (VF.serie || {})[I.file] || {};
    const val = (p, a) => { const x = (S[p] || []).find((q) => q[0] === a); return x ? x[1] : null; };
    const [a0, a1x] = String(rb.anni || "").split("-").map(Number); const a1 = a1x || a0;
    const vic = (a) => { const v = ["FR", "DE", "ES"].map((p) => val(p, a)).filter((x) => x != null); return I.vicini && v.length >= 2 ? v.reduce((x, y) => x + y, 0) / v.length : null; };
    const storiaIt = (S.IT || []).filter((q) => q[0] >= VF.primo && q[0] <= VF.ultimo);
    const fineIt = val("IT", a1);
    const rkLiv = fineIt == null ? null : 1 + storiaIt.filter((q) => q[1] > fineIt + 1e-9).length;
    const livTxt = rkLiv == null ? "" : rkLiv === 1 ? `il valore più alto dal ${VF.primo}` : rkLiv === storiaIt.length ? `il valore più basso dal ${VF.primo}` : `il ${rkLiv}° valore più alto su ${storiaIt.length} anni dal ${VF.primo}`;
    // 4. gli altri indicatori della stessa unità
    const altri = base.filter((r) => r.u === u && r.ind !== I.nome && r.rango && r.n && !String(r.verso).startsWith("descrittivo"))
      .map((r) => [r, posiz(r.rango, r.n)]).sort((x, y) => y[1] - x[1]);
    const lista = (xs) => xs.map(([r]) => `<li><a href="#/dati/verifica?g=${esc(u)}&i=${esc((VF.ind.find((q) => q.nome === r.ind) || {}).id || "")}${leg ? "&per=legislatura" : ""}">${esc(r.ind)}</a>: ${r.rango}° su ${r.n}</li>`).join("");
    // verdetto: le tre letture vanno nella stessa direzione?
    const letture = [["in assoluto", pAbs], ["rispetto ai vicini", pRel], ["con gli anni spostati", pRit]].filter(([, x]) => x != null);
    const xs = letture.map(([, x]) => x);
    const opposte = xs.length > 1 && Math.max(...xs) - Math.min(...xs) >= 50;
    const concordi = xs.length > 1 && new Set(xs.map(classe)).size === 1;
    const verdetto = descr ? `<div class="avviso info"><p><strong>Indicatore descrittivo.</strong> Per ${esc(I.nome.toLowerCase())} salire o scendere non è in sé meglio o peggio: chi lo presenta come un successo o un fallimento sta aggiungendo un giudizio, non un dato.</p></div>`
      : opposte ? `<div class="avviso attenzione" role="status"><p><strong>Attenzione: questi numeri si prestano a letture opposte.</strong> ${maiu(letture.map(([t, x]) => `${t} ${terzo(x)}`).join("; "))}. Chi cita solo una lettura può dire una cosa vera e dare un'idea sbagliata.</p></div>`
      : concordi ? `<div class="avviso favorevole" role="status"><p><strong>Le letture vanno nella stessa direzione:</strong> ${letture.map(([t]) => t).join(", ")}, sempre ${terzo(xs[0])}. Qui è difficile che due persone oneste arrivino a conclusioni opposte.</p></div>`
      : `<div class="avviso info" role="status"><p><strong>Letture in parte diverse:</strong> ${letture.map(([t, x]) => `${t} ${terzo(x)}`).join("; ")}. Conta dire quale lettura si usa.</p></div>`;
    const frase = `${nomeU}, ${I.nome.toLowerCase()} (anni ${rb.anni || "n.d."}): Italia ${fmt(rb.it)}${rb.vic != null ? `, media di Francia, Germania e Spagna ${fmt(rb.vic)}` : ""}.${rkIt ? ` In assoluto è ${rkIt[0]}° su ${rkIt[1]} ${parola}` : ""}${pRel != null ? `; rispetto ai vicini ${rb.rango}° su ${rb.n}` : ""}${pRit != null ? `; con gli anni spostati di uno ${rr.rango}° su ${rr.n}` : ""}${rkIt || pRel != null ? "." : ""} Fonte: ${I.fonte}.`;
    const opz = (xs, cur) => xs.map(([v, t]) => `<option value="${esc(v)}" ${v === cur ? "selected" : ""}>${esc(t)}</option>`).join("");
    const carta = (n, t, corpo) => `<div class="card vf-carta"><p class="vf-n">${n}</p><h3>${t}</h3>${corpo}</div>`;
    return `${schedeDati("verifica")}
      <p class="risposta">${esc(VF.in_breve || "")}</p>
      <div class="card vf-scelte">
        <label class="campo">Che cosa confronti<select id="vf-per">${opz([["governo", "Governi"], ["legislatura", "Legislature"]], leg ? "legislatura" : "governo")}</select></label>
        <label class="campo">${leg ? "Legislatura" : "Governo"}<select id="vf-g">${opz(unita, u)}</select></label>
        <label class="campo">Indicatore<select id="vf-i">${opz(VF.ind.map((x) => [x.id, x.nome]), I.id)}</select></label>
      </div>
      ${verdetto}
      <div class="vf-carte">
        ${carta(1, "Assoluto o confrontato?", `<p><strong>Solo Italia:</strong> ${fmt(rb.it)} ${I.tipo === "media" ? "di media negli anni contati" : `di variazione dal ${a0 - 1} al ${a1}`}${rkIt ? `, ${rkIt[0]}° su ${rkIt[1]} ${parola}` : ""}.</p>
          <p><strong>Rispetto ai vicini:</strong> ${I.vicini ? `media di Francia, Germania e Spagna ${fmt(rb.vic)}, differenza ${segnato(rb.diff)}${rb.rango ? `, ${rb.rango}° su ${rb.n}${descr ? " (1° = calo maggiore, non un giudizio)" : ""}` : ""}.` : "per questo indicatore non esiste un confronto omogeneo con gli altri Paesi."}</p>`)}
        ${carta(2, "Quali anni?", `<p><strong>Anni ${leg ? "della legislatura" : "del mandato"} (${esc(rb.anni || "n.d.")}):</strong> ${rb.rango ? `${rb.rango}° su ${rb.n}` : fmt(rb.it)}.</p>
          <p><strong>Spostati di uno (${esc(rr.anni || "n.d.")}):</strong> ${rr.rango ? `${rr.rango}° su ${rr.n}` : fmt(rr.it)}. Le misure agiscono spesso in ritardo: se le due righe sono molto diverse, chi cita una sola versione sceglie anche il risultato.</p>`)}
        ${carta(3, "Livello o variazione?", fineIt == null ? `<p>Serie annuale non disponibile per questi anni.</p>` : `<p><strong>Livello italiano:</strong> ${fmtLiv(val("IT", a0 - 1))} nel ${a0 - 1}, ${fmtLiv(fineIt)} nel ${a1}${vic(a1) != null ? ` (vicini ${fmtLiv(vic(a1))})` : ""}.</p>
          <p>Nel ${a1} era ${livTxt}. «Record» parla del livello, «è migliorato» della variazione: possono essere veri o falsi in modo indipendente.</p>`)}
        ${carta(4, "Che cosa resta fuori?", altri.length ? `<p>Gli altri indicatori dello stesso ${leg ? "periodo" : "governo"}, rispetto ai vicini:</p><p class="vf-sotto">Migliori</p><ul>${lista(altri.slice(0, 2))}</ul><p class="vf-sotto">Peggiori</p><ul>${lista(altri.slice(-2).reverse())}</ul>` : "<p>Nessun altro indicatore disponibile.</p>")}
        ${carta(5, "Qual è la fonte?", `<p>${esc(I.fonte)}${I.anni_dati ? ` (${esc(I.anni_dati)})` : ""}.</p>${I.descr ? `<p><strong>Che cosa misura:</strong> ${esc(I.descr)}.</p>` : ""}<p>${ext(repo + "/blob/main/storia/serie/" + I.file + ".csv", "Serie annuale completa")} · ${ext(repo + "/blob/main/storia/governi_metodo.md", "metodo")}</p>`)}
      </div>
      <section class="blocco"><h2>Come dirlo correttamente</h2>
        <p class="card vf-frase" id="vf-frase">${esc(maiu(frase))}</p>
        <div class="azioni"><button class="btn s" type="button" id="vf-copia">${icona("copy")}Copia la frase</button><a class="btn s" href="#/dati/governi?g=${esc(u)}${leg ? "&per=legislatura" : ""}">Tutti gli indicatori di questo ${leg ? "periodo" : "governo"}</a></div>
      </section>
      <section class="blocco"><h2>La lettura ragionata</h2>
        <div class="quattro">${Q4.map(([k, t, ic]) => `<div class="card q4"><p class="q4-t">${icona(ic)}${t}</p><p>${esc(VF[k] || "")}</p></div>`).join("")}</div>
        ${VF.oceano_blu ? `<h3 class="q4-sotto">Perché questa verifica è diversa <small>griglia della strategia oceano blu</small></h3>${grigliaErrc(VF.oceano_blu, "Elimina, riduce, aumenta, crea")}` : ""}
      </section>
      ${(VF.limiti || []).length ? `<div class="avviso"><div class="avviso-titolo">${icona("info")}Limiti da tenere presenti</div><ul>${VF.limiti.map((x) => `<li>${esc(x)}</li>`).join("")}</ul></div>` : ""}`;
  }
  // ---------- Punteggio da più punti di vista (storia/script/punti_di_vista.py) ----------
  const PV_PESI = ["non conta", "peso normale", "conta il doppio", "conta il triplo"];
  function sezionePV(leg) {
    const P = GV.punti_di_vista;
    const tipo = leg ? "legislatura" : "governo";
    if (!P || !P.righe || !(P.righe[tipo] || []).length) return "";
    const rr = P.righe[tipo], n = rr[0].n_unita;
    const qp = leg ? "&per=legislatura" : "";
    const pc = (x) => `${nf(x, x > 0 && x < 1 ? 1 : 0)}%`;
    const posto = (x) => `${nf(x, Number.isInteger(x) ? 0 : 1)}°`;
    return `<section class="card blocco" id="punti-di-vista"><h2>Punteggio da più punti di vista <small>${n} ${leg ? "legislature" : "governi"}, 4.014 combinazioni di pesi</small></h2>
      <p>${esc(P.in_breve || "")}</p>
      <p class="risposta">${esc((leg ? P.cosa_legislature : P.cosa) || "")}</p>
      <div class="tabella-scorre"><table class="tabella pv-tab a-card"><thead><tr><th>${leg ? "Legislatura" : "Governo"}</th><th class="num">Punteggio equo</th><th>Quanto cambia con i pesi</th><th class="num">Nel primo terzo</th><th class="num">Con pesi uguali</th><th>Nei 14 punti di vista dichiarati</th></tr></thead>
      <tbody>${rr.map((r) => `<tr><td class="principale"><span class="pv-posto">${r.posto_equo}°</span> <a href="#/dati/governi?g=${esc(r.id)}${qp}">${esc(r.etichetta)}</a><small>anni ${esc(r.anni)}${r.ambiti_mancanti ? ` · senza dati: ${esc(r.ambiti_mancanti)}` : ""}</small></td>
        <td class="num" data-etichetta="Punteggio equo"><span><strong>${Math.round(r.punteggio_equo)}</strong></span></td>
        <td data-etichetta="Quanto cambia con i pesi"><span class="pv-v"><span class="pv-int" role="img" aria-label="da ${Math.round(r.p10)} a ${Math.round(r.p90)}"><span class="pv-fascia" style="left:${r.p10}%;width:${Math.max(r.p90 - r.p10, 1)}%"></span><span class="pv-med" style="left:${r.punteggio_equo}%"></span></span><small>da ${Math.round(r.p10)} a ${Math.round(r.p90)}</small></span></td>
        <td class="num" data-etichetta="Nel primo terzo"><span>${pc(r.primo_terzo)}<small>ultimo terzo ${pc(r.ultimo_terzo)}</small></span></td>
        <td class="num" data-etichetta="Con pesi uguali"><span>${posto(r.posto_pesi_uguali)}</span></td>
        <td data-etichetta="Nei 14 punti di vista"><span class="pv-v">${r.posto_migliore === r.posto_peggiore ? `sempre ${posto(r.posto_migliore)}` : `dal ${posto(r.posto_migliore)} al ${posto(r.posto_peggiore)}`}<small>peggiore: ${esc(r.punto_peggiore)}</small></span></td></tr>`).join("")}</tbody></table></div>
      <p class="nota">Punteggio equo: posizione mediana da 0 (ultimo) a 100 (primo) su tutte le combinazioni di pesi tra gli ambiti, con gli anni ${leg ? "della legislatura" : "del mandato"} e con quelli spostati di uno. La barra va dal 10° al 90° percentile: più è corta, più il giudizio non dipende dai pesi.</p>
      <h3 class="q4-sotto">Il tuo punto di vista <small>scegli quanto conta ogni ambito</small></h3>
      <div class="simulatore pv-sim" data-pv-tipo="${tipo}">
        <div class="card">
          <div class="segmenti" role="group" aria-label="Pesi predefiniti"><button type="button" data-pv-preset="">Pesi uguali</button>${AMBITI_GV.map(([a, t]) => `<button type="button" data-pv-preset="${esc(a)}">Prima ${esc(t.toLowerCase())}</button>`).join("")}</div>
          ${AMBITI_GV.map(([a, t], j) => `<div class="cursore"><label for="pv-w${j}">${esc(t)} <output id="pv-o${j}" for="pv-w${j}"></output></label><input type="range" id="pv-w${j}" data-pv-amb="${esc(a)}" min="0" max="3" step="1" value="1"></div>`).join("")}
          <label class="pv-check"><input type="checkbox" id="pv-ritardo"> Anni spostati di uno (effetti in ritardo)</label>
          <p class="nota">Con i tuoi pesi il punteggio è la media pesata delle posizioni per ambito della tabella sopra; un ambito senza dati resta fuori.</p>
        </div>
        <div class="card"><h4 class="pv-h">Ordine con i tuoi pesi</h4><p class="nota">Le frecce indicano lo spostamento rispetto ai pesi uguali.</p><ol class="classifica" id="pv-lista" aria-live="polite"></ol></div>
      </div>
      <details class="pv-metodo"><summary>Come si calcola e limiti</summary>
        <p><strong>Perché.</strong> ${esc(P.perche || "")}</p><p><strong>Come.</strong> ${esc(P.come || "")}</p><p><strong>Chi sceglie.</strong> ${esc(P.chi || "")}</p>
        ${P.oceano_blu ? grigliaErrc(P.oceano_blu, "Elimina, riduce, aumenta, crea") : ""}
        <ul>${(P.limiti || []).map((x) => `<li>${esc(x)}</li>`).join("")}</ul>
        <p>${ext(repo + "/blob/main/storia/punti_di_vista.md", "Tabella completa")} · ${ext(repo + "/blob/main/storia/script/punti_di_vista.py", "script del calcolo")}</p>
      </details>
    </section>`;
  }

  function montaPV() {
    const box = $(".pv-sim"), P = GV.punti_di_vista, tipo = box.dataset.pvTipo;
    const A = P.ambiti[tipo] || {}, nomi = Object.fromEntries(P.righe[tipo].map((r) => [r.id, r]));
    const qp = tipo === "legislatura" ? "&per=legislatura" : "";
    const cursori = $$("[data-pv-amb]", box);
    const calcola = (pesi, ver) => Object.keys(nomi).map((id) => {
      const s = (A[id] || {})[ver] || {};
      let num = 0, den = 0;
      AMBITI_GV.forEach(([a]) => { if (s[a] != null && pesi[a] > 0) { num += pesi[a] * s[a]; den += pesi[a]; } });
      return { id, v: den ? num / den : null };
    }).filter((x) => x.v != null).sort((a, b) => b.v - a.v);
    const aggiorna = () => {
      const pesi = {};
      cursori.forEach((c, j) => { pesi[c.dataset.pvAmb] = +c.value; $("#pv-o" + j).textContent = PV_PESI[+c.value]; });
      const ver = $("#pv-ritardo").checked ? "ritardo_1_anno" : "base";
      const base = calcola(Object.fromEntries(AMBITI_GV.map(([a]) => [a, 1])), ver).map((x) => x.id);
      const lista = calcola(pesi, ver);
      $("#pv-lista").innerHTML = lista.length ? lista.map((x, i) => {
        const salto = base.indexOf(x.id) - i;
        return `<li><span class="pos">${i + 1}</span><span><a href="#/dati/governi?g=${esc(x.id)}${qp}">${esc(nomi[x.id].etichetta)}</a></span>
          <span class="salto ${salto > 0 ? "su" : salto < 0 ? "giu" : ""}" aria-label="${salto > 0 ? `sale di ${salto}` : salto < 0 ? `scende di ${-salto}` : "stessa posizione"}">${salto > 0 ? "▲ " + salto : salto < 0 ? "▼ " + -salto : "="}</span>
          <div class="barra" aria-hidden="true"><span style="width:${Math.max(0, x.v)}%"></span></div></li>`;
      }).join("") : `<li>Dai un peso ad almeno un ambito.</li>`;
    };
    cursori.forEach((c) => c.addEventListener("input", aggiorna));
    $("#pv-ritardo").addEventListener("change", aggiorna);
    $$("[data-pv-preset]", box).forEach((b) => b.addEventListener("click", () => { cursori.forEach((c) => { c.value = !b.dataset.pvPreset ? 1 : c.dataset.pvAmb === b.dataset.pvPreset ? 2 : 1; }); aggiorna(); }));
    aggiorna();
  }

  function montaVerifica() {
    const vai = (k, v) => { const q = new URLSearchParams(location.hash.split("?")[1] || ""); q.set(k, v); if (k === "per") q.delete("g"); location.hash = "#/dati/verifica?" + q.toString(); };
    $("#vf-per").addEventListener("change", (e) => vai("per", e.target.value));
    $("#vf-g").addEventListener("change", (e) => vai("g", e.target.value));
    $("#vf-i").addEventListener("change", (e) => vai("i", e.target.value));
    $("#vf-copia").addEventListener("click", async (e) => { try { await navigator.clipboard.writeText($("#vf-frase").textContent); e.currentTarget.lastChild.textContent = "Frase copiata"; } catch (err) { /* appunti non disponibili */ } });
  }

  const ORIZZ = ["breve", "medio", "lungo"];
  function simulatore() {
    return `${schedeProgramma("valori")}
      <p class="risposta">Il programma non sceglie un unico peso tra i valori: qui puoi provare il tuo. La classifica si ricalcola con i punteggi dei tre valutatori AI. Le proposte del nucleo robusto restano in alto con <em>qualunque</em> combinazione.</p>
      <div class="simulatore">
        <div class="card">
          <h2 style="font-size:20px">In tre passi</h2>
          <fieldset class="passi-valori"><legend><span class="passo">1</span>Quali valori contano di più per te? Scegline fino a tre.</legend>
            <div class="scelte-valori" data-passo="su">${D.valori.map((v) => `<button type="button" class="scelta-valore" data-valore="${v.id}" aria-pressed="false">${esc(v.nome)}</button>`).join("")}</div></fieldset>
          <fieldset class="passi-valori"><legend><span class="passo">2</span>Ce n'è uno che per te conta meno? Facoltativo.</legend>
            <div class="scelte-valori" data-passo="giu">${D.valori.map((v) => `<button type="button" class="scelta-valore" data-valore="${v.id}" aria-pressed="false">${esc(v.nome)}</button>`).join("")}</div></fieldset>
          <p class="passi-valori"><span class="passo">3</span><span id="passi-esito">Guarda come cambia la classifica.</span> <button type="button" class="btn terziario s" data-azione-valori="azzera">Ricomincia</button></p>
          <details class="richiudibile"><summary>Regola tu i pesi, uno per uno<span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo">
          <div class="segmenti" role="group" aria-label="Pesi predefiniti">
            <button type="button" data-preset="uguali">Pesi uguali</button>${["FUT", "EQU", "BEN", "INN", "SIC"].map((id) => `<button type="button" data-preset="${id}">Più ${esc((D.valori.find((v) => v.id === id) || {}).nome || id).split(" ")[0].toLowerCase()}</button>`).join("")}
          </div>
          ${D.valori.map((v) => `<div class="cursore"><label for="w-${v.id}">${esc(v.nome)} <output id="wv-${v.id}" for="w-${v.id}"></output></label><input type="range" id="w-${v.id}" data-peso="${v.id}" min="0" max="100" value="50"></div>`).join("")}
          <h3 style="margin-top:16px;font-size:16px">Orizzonti di tempo</h3>
          ${ORIZZ.map((o) => `<div class="cursore"><label for="h-${o}">${o[0].toUpperCase() + o.slice(1)} periodo <output id="hv-${o}" for="h-${o}"></output></label><input type="range" id="h-${o}" data-orizzonte="${o}" min="0" max="100" value="${o === "lungo" ? 40 : 30}"></div>`).join("")}
          <p class="nota">Regola della Carta: il lungo periodo pesa almeno quanto il breve. Il cursore si adegua da solo.</p>
        </div></details>
        </div>
        <div class="card"><h2 style="font-size:20px">Classifica</h2><p class="nota">Effetto pesato sui valori; le frecce indicano lo spostamento rispetto ai pesi uguali.</p><ol class="classifica" id="classifica" aria-live="polite"></ol></div>
      </div>`;
  }
  // tre passi: i valori scelti pesano 90, quello che conta meno 10, gli altri 40 (sulla stessa scala dei cursori)
  function applicaPassiValori() {
    const su = $$('[data-passo="su"] .scelta-valore[aria-pressed=true]').map((x) => x.dataset.valore);
    const giu = $$('[data-passo="giu"] .scelta-valore[aria-pressed=true]').map((x) => x.dataset.valore);
    $$('[data-passo="giu"] .scelta-valore').forEach((x) => { x.disabled = su.includes(x.dataset.valore); });
    D.valori.forEach((v) => { $("#w-" + v.id).value = !su.length && !giu.length ? 50 : su.includes(v.id) ? 90 : giu.includes(v.id) && !su.includes(v.id) ? 10 : 40; });
    const nome = (id) => (D.valori.find((v) => v.id === id) || {}).nome || id;
    $("#passi-esito").textContent = su.length || giu.length ? `Classifica ricalcolata: conta di più ${su.map(nome).join(", ") || "—"}${giu.length ? `, conta meno ${nome(giu[0])}` : ""}. Le frecce mostrano chi sale e chi scende.` : "Guarda come cambia la classifica.";
    aggiornaClassifica();
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
      return `<li><span class="pos">${i + 1}</span><span><a href="${linkP(x.p.id)}">${esc(tit(x.p.titolo))}</a> <span class="codice">${esc(x.p.id)}</span> ${x.p.classe === "robusta" ? chipClasse("robusta") : ""}</span>
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
      <span class="nota">${fonte ? `Base: ${esc(fonte)} · ` : ""}<a href="${linkP(o.proposta)}" title="${esc(o.proposta)}">la misura</a></span></li>`;
  }
  function unaPagina(params) {
    const S = D.schema || {};
    if (!S.missioni) return `${schedeProgramma("una-pagina")}${vuoto("Lo schema del programma non è ancora disponibile.")}`;
    const sc = scenario(params.get("scenario") || RIF_ID);
    const P = S.programma || {};
    const costo = (ids) => ids.reduce((a, id) => a + ((sc.misure[id] || {}).costo || 0), 0);
    const cop = D.coperture.filter((c) => sc.coperture.includes(c.misura_id) && c.gettito_min > 0).sort((a, b) => (b.gettito_min || 0) - (a.gettito_min || 0));
    const dose = (m) => !m ? misuratore(null) : m.variante === "ZERO" ? `<span class="chip">${icona("scroll-text")}Solo regole, costo zero</span>` : misuratore(m.variante) + `<span class="nota">${euro(m.costo)}</span>`;
    const misura = (id) => { const p = proposta(id), m = sc.misure[id]; if (!p) return ""; return `<li class="${m ? "" : "fuori"}"><a href="${linkP(id)}" title="${esc(id)}">${esc(tit(p.titolo))}</a><span class="q-dose">${dose(m)}</span></li>`; };
    const missione = (m) => {
      const dentro = m.proposte.filter((id) => sc.misure[id]).sort((a, b) => sc.misure[b].costo - sc.misure[a].costo);
      const fuori = m.proposte.filter((id) => !dentro.includes(id));
      const prime = dentro.filter((id) => sc.misure[id].variante !== "ZERO").slice(0, 5), altre = dentro.filter((id) => !prime.includes(id));
      const fonteChi = (g) => !g.fonte ? "" : /da stimare/i.test(g.fonte) ? badge("verificare", "Numero da stimare: la fonte non è ancora disponibile.") : badge(/stima|elaborazione|calcol/i.test(g.fonte) ? "stima" : "verificato", g.fonte);
      return `<article class="card missione" id="${esc(m.id)}" aria-labelledby="t-${esc(m.id)}">
        <header class="missione-testa">${icona(m.icona || "circle")}<div><h2 id="t-${esc(m.id)}">${esc(m.titolo)}</h2>
          <p class="nota">${dentro.length} misure su ${m.proposte.length} · ${euro(costo(m.proposte))} l'anno ${badge("stima", STIMA)}</p></div></header>
        <details class="missione-apri"><summary>Apri la missione: perché, come si paga, che cosa misuriamo, chi ne beneficia</summary><div class="quattro">
          <section class="q-cella">${testaQuattro("perche")}<p>${esc(m.perche)}</p><div class="chips">${(m.valori || []).map((v) => `<span class="chip info">${esc(nomeValore(v))}</span>`).join("")}</div></section>
          <section class="q-cella">${testaQuattro("come")}<p>${esc(m.come)}</p>
            <p class="q-sotto">Le misure con più risorse</p>
            <ul class="q-misure">${prime.map(misura).join("")}</ul>
            ${altre.length ? `<details class="leggi"><summary>Altre ${altre.length} ${altre.length === 1 ? "misura" : "misure"} nel programma</summary><ul class="q-misure">${altre.map(misura).join("")}</ul></details>` : ""}
            ${fuori.length ? `<details class="leggi"><summary>${fuori.length} ${fuori.length === 1 ? "misura fuori" : "misure fuori"} da questa versione</summary><ul class="q-misure">${fuori.map(misura).join("")}</ul></details>` : ""}
            <p class="q-sostenibile">${icona("scale")}<span><strong>Sostenibilità.</strong> ${esc(m.sostenibilita)}</span></p></section>
          <section class="q-cella">${testaQuattro("cosa")}<ul class="q-ind">${(m.indicatori || []).map(rigaIndicatore).join("")}</ul></section>
          <section class="q-cella">${testaQuattro("chi")}<ul class="q-lista-chi">${(m.chi || []).map((g) => `<li><strong>${esc(g.gruppo)}</strong>${g.quanti ? `<span class="q-quanti">${esc(g.quanti)} ${fonteChi(g)}</span>` : ""}<span>${esc(g.cosa_cambia)}</span></li>`).join("")}</ul></section>
        </div></details></article>`;
    };
    return `${schedeProgramma("una-pagina")}
      ${aperturaProgramma(sc, `<div class="filtri-barra"><label class="campo">Versione del programma<select id="schema-scenario">${D.scenari.map((x) => `<option value="${x.id}" ${x.id === sc.id ? "selected" : ""}>${esc(x.nome)}${x.id === RIF_ID ? " (riferimento)" : ""}</option>`).join("")}</select></label></div>`)}
      <p class="nota">Qui sotto, per ogni missione: <strong>perché</strong> la facciamo, <strong>come</strong> e con quali soldi, <strong>che cosa misuriamo</strong> per dire che ce l'abbiamo fatta e <strong>chi ne beneficia</strong>.</p>

      <section class="tela" aria-label="Il programma in quattro domande">
        ${QUATTRO.map(([k, ic, t, sotto]) => `<div class="tela-cella q-${k}"><p class="q-etichetta">${icona(ic)}${t}</p><p class="nota">${sotto}</p><p class="tela-testo">${esc(P[k] || "")}</p></div>`).join("")}
      </section>

      <section class="sezione" aria-labelledby="t-conti">
        <div class="sezione-testa"><h2 id="t-conti">I conti in una riga</h2><a href="#/programma/coperture">Come si paga</a></div>
        <div class="griglia g2 g4-d">
          <div class="card kpi"><p class="etichetta">Spesa nuova</p><p class="numero">${nf(sc.spesa, 1)}<small>mld/anno</small></p><p class="nota">a regime</p>${badge("stima", STIMA)}</div>
          <div class="card kpi"><p class="etichetta">Risorse</p><p class="numero">${nf(sc.risorse ?? sc.gettito, 1)}<small>mld/anno</small></p><p class="nota">coperture nuove, fondi europei già stanziati e tariffe, con il gettito al minimo: il dettaglio è nelle barre qui sotto</p></div>
          <div class="card kpi"><p class="etichetta">Nuovo deficit</p><p class="numero">${sc.deficit > 0 ? nf(sc.deficit, 1) : "0"}<small>mld</small></p><p class="nota">${sc.deficit > 0 ? "spesa non coperta" : `margine sulle risorse generali: ${nf(sc.margine_generali ?? sc.margine ?? 0, 1)} mld${sc.vincolati_non_usati > 0 ? ` (più ${nf(sc.vincolati_non_usati, 1)} di fondi vincolati non spostabili)` : ""}`}</p></div>
          <div class="card kpi"><p class="etichetta">Misure</p><p class="numero">${Object.keys(sc.misure).length}<small>su ${D.proposte.length}</small></p><p class="nota">in ${S.missioni.length} missioni; ${Object.values(sc.misure).filter((m) => m.variante === "ZERO").length} sono solo regole, a costo zero</p></div>
        </div>
        <div class="card" style="margin-top:16px">${barreSoldi([sc])}<details class="leggi"><summary>Il dettaglio in parole</summary><p class="nota">${fontiSoldi(sc)}.</p></details></div>
        ${sc.temporanei_2029 > 0 ? avvisoDopo2029(sc) : ""}
        ${(sc.annuale || []).length ? avvisoAnnuale(sc) : ""}
      </section>

      ${(P.indicatori_chiave || []).length ? `<section class="sezione" aria-labelledby="t-chiave">
        <div class="sezione-testa"><h2 id="t-chiave">Ce l'avremo fatta se…</h2><a href="#/dati/obiettivi">Tutti gli obiettivi</a></div>
        <ul class="q-ind griglia g2-d">${P.indicatori_chiave.map(rigaIndicatore).join("")}</ul></section>` : ""}

      <section class="sezione" aria-labelledby="t-missioni">
        <div class="sezione-testa"><h2 id="t-missioni">Le ${S.missioni.length} missioni</h2></div>
        <nav class="temi nav-missioni" aria-label="Missioni">${S.missioni.map((m) => `<a href="#${esc(m.id)}" data-ancora>${esc(m.titolo)}<span>${euro(costo(m.proposte))}</span></a>`).join("")}</nav>
        <div class="missioni">${S.missioni.map(missione).join("")}</div>
      </section>

      <section class="sezione" aria-labelledby="t-contribuisce">
        <div class="sezione-testa"><h2 id="t-contribuisce">Chi contribuisce</h2><a href="#/programma/coperture">Tutte le coperture</a></div>
        <p class="nota" style="margin-top:-8px">Le coperture attive in questa versione, dalla più grande. Ogni euro di spesa ha una copertura certa: niente deficit, niente recupero di evasione non ancora incassato.</p>
        ${(() => { const tab = (v) => `<div class="tabella-box"><table class="tabella a-card"><thead><tr><th>Copertura</th><th>Chi paga o rinuncia</th><th class="num">Gettito minimo</th></tr></thead><tbody>${v.map((c) => `<tr><td class="principale"><span class="mono nota">${esc(c.misura_id)}</span><br>${esc(c.descrizione)}</td><td data-etichetta="Chi paga">${esc(c.chi_paga)}</td><td class="num" data-etichetta="Gettito minimo"><span class="barretta" aria-hidden="true"><span style="width:${(c.gettito_min / cop[0].gettito_min * 100).toFixed(1)}%"></span></span>${nf(c.gettito_min)} mld</td></tr>`).join("")}</tbody></table></div>`;
          return tab(cop.slice(0, 5)) + (cop.length > 5 ? `<details class="leggi"><summary>Le altre ${cop.length - 5} coperture</summary>${tab(cop.slice(5))}</details>` : ""); })()}
      </section>
      <div class="azioni" style="margin-top:24px"><a class="btn primario" href="#/programma">Tutte le ${D.proposte.length} proposte ${icona("arrow-right")}</a>${azioniCondividi()}</div>`;
  }

  // Che cosa cambia per me: profili tipo (programma/profili.yaml), con stato e tempi presi dal programma di riferimento
  // ---------- La tua busta paga con GovernAI (calcolo in docs/busta.js, regole in programma/busta_paga.yaml) ----------
  const eur0 = (n) => `${n < -0.5 ? "−" : ""}${String(Math.abs(Math.round(n))).replace(/\B(?=(\d{3})+(?!\d))/g, ".")} €`;
  const segno = (n) => Math.round(n) === 0 ? "0 €" : (n > 0 ? "+" : "−") + eur0(Math.abs(n));
  function bustaPaga(params) {
    const Q = D.busta || {};
    if (!Q.programma || !window.BUSTA) return `${schedeProgramma("busta-paga")}${vuoto("Il calcolatore non è ancora disponibile.")}`;
    const G = Q.programma, ral = params.get("ral") || "30000";
    const campo = (id, etich, aiuto, val = "") => `<label class="campo">${etich}<input type="number" inputmode="decimal" min="0" step="1" id="${id}" value="${esc(val)}" placeholder="0">${aiuto ? `<small>${aiuto}</small>` : ""}</label>`;
    return `${schedeProgramma("busta-paga")}
      <p class="risposta">Quanto cambierebbe il tuo stipendio netto con il programma, a regime? Inserisci la retribuzione annua lorda (RAL). Il calcolo usa le regole IRPEF del 2026 e le misure del programma ${esc(G.scenario || "intermedio")} che toccano la busta paga. È una stima: non sostituisce il cedolino né un CAF.</p>
      <form class="busta-form" onsubmit="return false">
        <div class="busta-campi">
          ${campo("bp-ral", "Retribuzione annua lorda (RAL)", "Lavoro dipendente, tempo indeterminato, tutto l'anno.", ral)}
          <label class="campo">Quanto vale il taglio delle tasse<select id="bp-scen">${(G.dividendo || []).map((d) => `<option ${d.scenario === "Centrale" ? "selected" : ""}>${esc(d.scenario)}</option>`).join("")}</select><small>Dipende da quanto lavoro ripetitivo si automatizza davvero.</small></label>
        </div>
        <details class="richiudibile"><summary>${icona("receipt")}Le tue spese detraibili e il fondo pensione (facoltativo)<span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo busta-campi">
          ${campo("bp-san", "Spese sanitarie l'anno", "Visite, farmaci, esami.")}
          <label class="campo campo-spunta"><input type="checkbox" id="bp-cron"> Spese per disabilità, malattia cronica grave o non autosufficienza</label>
          ${campo("bp-premi", "Premi di assicurazioni vita e infortuni", "Fino a 530 € detraibili.")}
          ${campo("bp-vet", "Spese veterinarie", "Fino a 550 € detraibili.")}
          ${campo("bp-sport", "Spese per lo sport di figlie e figli 5-18 anni", "Fino a 210 € per ciascuno.")}
          ${campo("bp-figli", "Quante figlie e figli fanno sport", "")}
          ${campo("bp-fondo", "Contributi al fondo pensione", "Quelli che versi tu e il datore, fino a 5.164 €.")}
        </div></details>
      </form>
      <div id="bp-esito" aria-live="polite"></div>
      <section class="sezione"><h2>Come leggere il risultato</h2>
        <ul class="elenco-punti">
          <li><strong>Taglio delle tasse sul lavoro:</strong> ${esc(G.dividendo_ipotesi || "")} <a href="#/programma/ai">Le stime nella pagina AI e Stato</a>.</li>
          <li><strong>Dal quando:</strong> le detrazioni cambiano dal ${Math.min(...(G.misure || []).map((m) => m.dal))}; il taglio delle tasse arriva al più presto dal 2030. «Con GovernAI» indica il risultato quando tutto è a regime, con le regole del 2026 per il resto.</li>
          <li><strong>Che cosa non è nel calcolo:</strong></li>
        </ul>
        <ul class="elenco-punti">${(G.non_calcolate || []).map((x) => `<li>${esc(x)}</li>`).join("")}</ul>
        <p class="nota">Ipotesi: addizionali regionale e comunale al ${nf(Q.regole.addizionali.regionale.valore * 100, 2)}% e ${nf(Q.regole.addizionali.comunale.valore * 100, 1)}% (valori tipici: nella tua Regione e nel tuo Comune possono essere diversi); nessun familiare a carico, mutuo o altro reddito; contributi INPS del lavoratore al ${nf(Q.regole.inps.dipendente.aliquota_lavoratore * 100, 2)}%. Le regole sono verificate norma per norma in <code>analisi/chi_paga/parametri.yaml</code> e <code>programma/busta_paga.yaml</code>; il calcolo, in <code>docs/busta.js</code>, dà gli stessi numeri del calcolatore <a href="#/programma/chi-paga">Chi paga davvero</a>.</p>
      </section>`;
  }
  function aggiornaBusta() {
    const Q = D.busta, v = (id) => +(($(id) || {}).value || 0);
    const x = { ral: v("#bp-ral"), sanitarie: v("#bp-san"), cronica: $("#bp-cron").checked, premi: v("#bp-premi"), veterinarie: v("#bp-vet"), sport: v("#bp-sport"), figli: v("#bp-figli"), fondo: v("#bp-fondo") };
    const sc = $("#bp-scen").value;
    const o = BUSTA.calcola(Q, x, false), g = BUSTA.calcola(Q, x, true, sc);
    const M = Object.fromEntries((Q.programma.misure || []).map((m) => [m.id, m]));
    if (!x.ral) { $("#bp-esito").innerHTML = `<p class="nota">Inserisci la retribuzione annua lorda.</p>`; return; }
    const riga = (t, a, b, fmt = eur0, cls = "") => `<tr class="${cls}"><td class="principale">${t}</td><td class="num" data-etichetta="Oggi">${fmt(a)}</td><td class="num" data-etichetta="Con GovernAI">${fmt(b)}</td><td class="num" data-etichetta="Differenza">${segno(b - a)}</td></tr>`;
    const dNetto = g.netto - o.netto;
    const voci = [
      ["Taglio delle tasse sul lavoro (09-C11 e 09-C12)", g.dividendo, "dal 2030, a regime in circa dieci anni"],
      [M.SF06 ? M.SF06.titolo : "Spese sanitarie", g.oneri.sanitarie - o.oneri.sanitarie, M.SF06 ? `dal ${M.SF06.dal}. ${M.SF06.nota || ""}` : ""],
      [M.FN02 ? M.FN02.titolo : "Premi e veterinarie", g.oneri.premi + g.oneri.veterinarie - o.oneri.premi - o.oneri.veterinarie, M.FN02 ? `dal ${M.FN02.dal}. ${M.FN02.nota || ""}` : ""],
      [M.SF08 ? M.SF08.titolo : "Sport", g.oneri.sport - o.oneri.sport, M.SF08 ? `dal ${M.SF08.dal}` : ""],
      [M.SF22 ? M.SF22.titolo : "Fondo pensione", -g.tettoFondo, M.SF22 ? `dal ${M.SF22.dal}` : ""],
    ].filter(([, d], i) => i === 0 || Math.abs(d) >= 0.5);
    $("#bp-esito").innerHTML = `<div class="card busta-risultato"><p class="etichetta">Netto in più o in meno ogni anno, a regime</p>
        <p class="busta-cifra ${dNetto >= 0 ? "su" : "giu"}">${segno(dNetto)}</p>
        <p>${segno(dNetto / 12)} al mese su 12 mensilità · scenario ${esc(sc.toLowerCase())} del taglio delle tasse</p></div>
      <div class="tabella-scorre"><table class="tabella a-card busta-tab"><thead><tr><th>Ogni anno</th><th class="num">Oggi (regole 2026)</th><th class="num">Con GovernAI, a regime</th><th class="num">Differenza</th></tr></thead><tbody>
        ${riga("Retribuzione annua lorda", o.ral, g.ral)}
        ${riga("Contributi INPS a tuo carico", -o.inps, -g.inps)}
        ${riga("IRPEF", -o.irpef, -g.irpef)}
        ${riga("Addizionali regionale e comunale", -o.addizionali, -g.addizionali)}
        ${o.se || o.ti ? riga("Somma esente e trattamento integrativo", o.se + o.ti, g.se + g.ti) : ""}
        ${riga("Taglio delle tasse sul lavoro", o.dividendo, g.dividendo)}
        ${riga("<strong>Netto l'anno</strong>", o.netto, g.netto, eur0, "totale")}
        ${riga("Netto al mese (12 mensilità)", o.netto / 12, g.netto / 12)}
      </tbody></table></div>
      <h3>Che cosa cambia per te</h3>
      <ul class="elenco-punti">${voci.map(([t, d, q]) => `<li><strong>${segno(d)}</strong> · ${esc(t)}${q ? ` <span class="nota">(${esc(q)})</span>` : ""}</li>`).join("")}</ul>`;
  }
  function perMe(params) {
    const P = D.profili || [];
    if (!P.length) return `${schedeProgramma("per-me")}${vuoto("I profili non sono ancora disponibili.")}`;
    const sel = P.find((p) => p.id === params.get("profilo")) || null;
    const cal = (rif.calendario || {}).pieno_dal || {};
    const cop = Object.fromEntries((D.coperture || []).map((c) => [c.misura_id, c]));
    const attive = new Set(rif.coperture || []);
    const LIV = { PIENA: "versione piena", ESSENZIALE: "versione essenziale", PILOTA: "solo sperimentazione", ZERO: "solo regole, a costo zero" };
    const scheda = (p) => `<a class="card profilo ${sel && sel.id === p.id ? "attivo" : ""}" href="#/programma/per-me?profilo=${encodeURIComponent(p.id)}" ${sel && sel.id === p.id ? 'aria-current="true"' : ""}><p class="etichetta">${icona(p.icona || "user")}${esc(p.titolo)}</p><p class="nota">${esc(p.in_breve || "")}</p></a>`;
    const voceG = (g) => {
      const pr = proposta(g.proposta) || {};
      const m = rif.misure[g.proposta];
      const ini = ((rif.calendario || {}).inizio || {})[g.proposta];
      const quando = m && cal[g.proposta] ? ` · comincia nel ${ini || "—"}, a pieno dal ${cal[g.proposta]}` : "";
      const stato = m ? `${LIV[m.variante] || esc(m.variante.toLowerCase())}${m.costo > 0 ? `, ${euro(m.costo)} l'anno` : ""}${quando}` : "non è nel programma di riferimento";
      return `<li><p><a href="${linkP(g.proposta)}"><strong>${esc(tit(pr.titolo || g.proposta))}</strong></a> <span class="nota">(${esc(g.proposta)} · ${stato})</span></p><p>${esc(g.testo)}</p></li>`;
    };
    // titolo leggibile della copertura: la descrizione fino ai due punti, senza i codici tecnici tra parentesi; il codice va nella nota
    const nomeCop = (c, id) => { let t = String(c.descrizione || "").split(/:\s/)[0].replace(/\s*\((?=[^)]*\b[A-Z][A-Z0-9]+[.\-]\w)[^)]*\)/g, "").trim(); if (t.length > 140) t = t.slice(0, t.lastIndexOf(" ", 137)) + "…"; return t || id; };
    const voceP = (x) => {
      const c = cop[x.copertura] || {};
      return `<li><p><strong>${esc(nomeCop(c, x.copertura))}</strong> <span class="nota">(${esc(x.copertura)} · ${attive.has(x.copertura) ? `${c.gettito_min ? `${euro(c.gettito_min)} l'anno in tutto, ` : ""}attiva nel programma di riferimento` : "non attiva nel programma di riferimento"})</span></p><p>${esc(x.testo)}</p></li>`;
    };
    const dettaglio = sel ? `<section class="sezione" aria-labelledby="t-profilo"><h2 id="t-profilo">${icona(sel.icona || "user")}${esc(sel.titolo)}</h2>
        <p class="risposta">${esc(sel.in_breve || "")}</p>
        ${sel.chi ? `<p class="nota">${esc(sel.chi)}</p>` : ""}
        ${(() => { const q = sel.in_30_secondi || {}, e = q.esempi || []; return e.length || q.quando ? `<div class="card riassunto-profilo"><h3>${icona("timer")}In 30 secondi, con qualche esempio in euro</h3>
          <ul class="esempi-euro">${e.map((x) => `<li><span>${esc(x.testo)}</span> ${badge(x.stima ? "stima" : "fonte", x.fonte ? String(x.fonte) : STIMA)}</li>`).join("")}</ul>
          ${q.quando ? `<p class="quando">${icona("calendar")}<span><strong>Quando:</strong> ${esc(q.quando)}</span></p>` : ""}
          <p class="nota">Esempi semplici calcolati sui numeri del programma, non una simulazione del tuo caso.</p></div>` : ""; })()}
        <div class="griglia g2-d">
          <div class="card"><h3>${icona("circle-plus")}Che cosa ci guadagni</h3><ul class="voci-profilo">${(sel.guadagna || []).map(voceG).join("") || "<li>Nessuna misura dedicata.</li>"}</ul></div>
          <div class="card"><h3>${icona("circle-minus")}Che cosa ti può costare</h3><ul class="voci-profilo">${(sel.paga || []).map(voceP).join("") || "<li>Nessuna copertura che ti riguardi direttamente.</li>"}</ul></div>
        </div>
        ${(sel.da_sapere || []).length ? `<div class="avviso" style="margin-top:12px"><div class="avviso-titolo">${icona("info")}Da sapere</div><ul>${sel.da_sapere.map((t) => `<li>${esc(t)}</li>`).join("")}</ul></div>` : ""}
      </section>` : "";
    return `${schedeProgramma("per-me")}
      <p class="risposta">Scegli il profilo più vicino a te: vedi che cosa ti dà il <strong>${esc(rif.nome ? rif.nome.toLowerCase() : "programma di riferimento")}</strong>, che cosa ti può costare e che cosa è ancora incerto. Le misure partono in modo graduale tra il 2027 e il 2035, secondo il <a href="#/programma/una-pagina">calendario di avvio</a>.</p>
      ${dettaglio}
      ${sel ? `<h2 style="margin-top:24px">Altri profili</h2>` : ""}<div class="griglia g2 g4-d">${P.filter((p) => !sel || p.id !== sel.id).map(scheda).join("")}</div>
      <p class="nota" style="margin-top:16px">Testi scritti da un agente AI a partire dai dati del programma (<code>programma/profili.yaml</code>); stato, costi e tempi sono letti dal programma di riferimento e si aggiornano da soli. Sono profili tipo: per sapere quanto cambia in euro per ciascuna famiglia serve una microsimulazione, che non abbiamo ancora.</p>
      <div class="azioni" style="margin-top:24px"><a class="btn primario" href="#/programma/una-pagina">Il programma in una pagina ${icona("arrow-right")}</a>${azioniCondividi()}</div>`;
  }

  // Pacchetto "pronto domani": testi in formato parlamentare per misure a costo zero o quasi (cartella pacchetto/)
  function prontoDomani(params) {
    const P = D.pacchetto || [];
    if (!P.length) return `${schedeProgramma("pronto")}${vuoto("Il pacchetto non è ancora disponibile.")}`;
    const sel = P.find((x) => x.id === params.get("misura"));
    const breve = (t) => { const m = t.match(/##+\s*1\.?\s*Scheda in breve[^\n]*\n([\s\S]*?)(?=\n##+\s)/i); return m ? m[1].trim() : ""; };
    if (sel) {
      const pr = proposta(sel.id) || {};
      return `${schedeProgramma("pronto")}
        <p><a href="#/programma/pronto">${icona("arrow-left")}Tutto il pacchetto</a></p>
        <div class="avviso" style="margin:12px 0"><div class="avviso-titolo">${icona("triangle-alert")}Testo preparato da agenti AI</div><p>Va verificato da una persona esperta prima di essere presentato. Il testo sorgente è <code>${esc(sel.file)}</code>${D.repo ? `, ${ext(D.repo + "/blob/main/" + sel.file, "su GitHub")}` : ""}.</p></div>
        <div class="md documento">${md(sel.testo)}</div>
        <div class="azioni" style="margin-top:24px"><a class="btn" href="${linkP(sel.id)}">Scheda della misura ${esc(sel.id)}</a>${azioniCondividi()}</div>`;
    }
    return `${schedeProgramma("pronto")}
      <p class="risposta">Testi che una parlamentare, un parlamentare o un ufficio legislativo potrebbe presentare domani: misure a costo zero o quasi, già passate dal controllo giuridico preventivo. Per ognuna: scheda in breve, relazione illustrativa, articolato, relazione tecnica, analisi tecnico-normativa e d'impatto, note per chi presenta.</p>
      <div class="griglia g2-d">${P.map((x) => { const pr = proposta(x.id) || {}; const m = rif.misure[x.id]; return `<div class="card"><p class="etichetta"><a href="#/programma/pronto?misura=${encodeURIComponent(x.id)}">${icona("file-text")}${esc(((x.testo.match(/^#\s+(.+)$/m) || [])[1]) || (x.id + " · " + tit(pr.titolo || x.id)))}</a></p><div class="md">${md(breve(x.testo).split("\n").slice(0, 4).join("\n"))}</div><p><a class="btn s" href="#/programma/pronto?misura=${encodeURIComponent(x.id)}">Leggi il testo completo ${icona("arrow-right")}</a></p></div>`; }).join("")}</div>
      <p class="nota" style="margin-top:16px">Testi preparati da agenti AI il 13 novembre 2026 a partire dalle schede e dai controlli giuridici del programma; non sono stati rivisti da una persona esperta.</p>`;
  }

  // Osservatorio sul governo di oggi (cartella osservatorio/): commenti di GovernAI agli atti del Governo in carica
  const SEGNO = { "+": ["p", "a favore"], "-": ["n", "contro"], "=": ["z", "neutro"], "±": ["m", "in parte a favore, in parte contro"] };
  // un valore può avere più giudizi nello stesso atto: + e − insieme diventano "±"
  const segniAtto = (x) => { const g = {}; (x.valori || []).forEach((v) => { (g[v.valore] = g[v.valore] || new Set()).add(v.segno); }); return Object.fromEntries(Object.entries(g).map(([k, q]) => [k, q.has("+") && q.has("-") ? "±" : q.has("+") ? "+" : q.has("-") ? "-" : "="])); };
  const BREVE_V = { RIS: "Rispetto", FID: "Fiducia", INN: "Innovazione", BEN: "Benessere", APC: "Cultura", BPA: "Bellezza", FUT: "Futuro", EQU: "Equità", SIC: "Sicurezza", CIT: "Cittadinanza" };
  const TIPI_ATTO = [["tutti", "Tutti"], ["legge di bilancio", "Legge di bilancio 2027"], ["decreto-legge", "Decreti-legge"], ["legge", "Leggi"], ["decreto legislativo", "Decreti legislativi"]];
  const tessera = (segno, extra = "") => `<span class="sv ${SEGNO[segno] ? SEGNO[segno][0] : "nt"}" ${extra}><i aria-hidden="true"></i></span>`;
  // striscia dei 10 valori nell'ordine della Carta: triangolo su = a favore, giù = contro, punto = neutro, tratteggio = non toccato
  function strisciaValori(x, conNomi) {
    const m = segniAtto(x);
    const desc = D.valori.map((v) => `${v.nome}: ${SEGNO[m[v.id]] ? SEGNO[m[v.id]][1] : "non toccato"}`).join("; ");
    return `<div class="striscia-valori${conNomi ? " con-nomi" : ""}" role="img" aria-label="Giudizio sui valori della Carta. ${esc(desc)}">${D.valori.map((v) => `<span class="sv-col" title="${esc(v.nome)}: ${SEGNO[m[v.id]] ? SEGNO[m[v.id]][1] : "non toccato"}">${tessera(m[v.id])}${conNomi ? `<b>${esc(BREVE_V[v.id] || v.id)}</b>` : ""}</span>`).join("")}</div>`;
  }
  const legendaValori = () => `<p class="legenda-valori nota" aria-hidden="true">${tessera("+")} a favore ${tessera("-")} contro ${tessera("=")} neutro ${tessera("±")} in parte sì, in parte no ${tessera("")} non toccato <span>· caselle nell'ordine della Carta: ${D.valori.map((v) => esc(BREVE_V[v.id] || v.id)).join(", ")}</span></p>`;
  // divide "Soggetto: resto" per mettere in evidenza il gruppo
  const gruppo = (t) => { const k = String(t).indexOf(": "); return k > 0 && k < 90 ? `<strong>${esc(String(t).slice(0, k))}</strong>: ${esc(String(t).slice(k + 2))}` : esc(t); };
  const colonnaBilancia = (cls, ic, titolo, v) => { const a = v.slice(0, 3), b = v.slice(3); return `<div class="piatto ${cls}"><p class="etichetta">${icona(ic)}${esc(titolo)} <span class="conta">${v.length}</span></p><ul>${a.map((y) => `<li>${gruppo(y)}</li>`).join("")}</ul>${b.length ? `<details><summary>Altri ${b.length}</summary><ul>${b.map((y) => `<li>${gruppo(y)}</li>`).join("")}</ul></details>` : ""}</div>`; };
  function barreValori(A) {
    const n = A.length || 1;
    const righe = D.valori.map((v) => { const c = (g) => A.filter((x) => (x.valori || []).some((y) => y.valore === v.id && y.segno === g)).length; return { v, piu: c("+"), meno: c("-") }; });
    return `<div class="qv"><div class="qv-riga qv-testa" aria-hidden="true"><span></span><span>contro</span><span>a favore</span></div>${righe.map((r) => `<div class="qv-riga" role="img" aria-label="${esc(r.v.nome)}: ${r.meno} atti contro, ${r.piu} a favore"><span class="qv-nome" aria-hidden="true">${esc(BREVE_V[r.v.id] || r.v.nome)}</span><span class="qv-neg" aria-hidden="true"><span style="width:${r.meno / n * 100}%"></span><b>${r.meno || ""}</b></span><span class="qv-pos" aria-hidden="true"><span style="width:${r.piu / n * 100}%"></span><b>${r.piu || ""}</b></span></div>`).join("")}</div>`;
  }
  function osservatorioHome() {
    const A = (D.osservatorio || {}).atti || [];
    if (!A.length) return "";
    const recenti = [...A].sort((a, b) => String(b.data).localeCompare(String(a.data)) || (a.tipo === "legge di bilancio") - (b.tipo === "legge di bilancio")).slice(0, 3);
    return `<section class="sezione" aria-labelledby="t-osserv">
        <div class="sezione-testa"><h2 id="t-osserv">Il governo di oggi, con il nostro metro</h2><a href="#/osservatorio">Tutti i ${A.length} atti</a></div>
        <p class="nota" style="margin-top:-8px">Legge di bilancio 2027 e decreti di fine 2026, commentati su fatti e valori: chi ci guadagna, chi paga. Nessun partito.</p>
        <div class="griglia g2-d">
          <a class="card" href="#/osservatorio"><p class="etichetta">I ${A.length} atti sui 10 valori della Carta</p>${barreValori(A)}</a>
          <div class="osserv-recenti">${recenti.map((x) => `<a class="card atto-card" href="#/osservatorio/${encodeURIComponent(x.id)}"><p class="etichetta">${esc(x.tipo || "")}</p><h3 class="titolo-card">${esc(x.titolo)}</h3>${strisciaValori(x, false)}</a>`).join("")}</div>
        </div>
      </section>`;
  }
  function quadroValori(A) {
    const n = A.length;
    const barre = barreValori(A);
    const matrice = `<div class="tabella-box"><table class="tabella matrice-valori"><caption class="vh">Giudizio di ogni atto su ogni valore</caption><thead><tr><th scope="col">Atto</th>${D.valori.map((v) => `<th scope="col" title="${esc(v.nome)}"><span>${esc(BREVE_V[v.id] || v.id)}</span></th>`).join("")}</tr></thead><tbody>${A.map((x) => { const m = segniAtto(x); return `<tr><th scope="row"><a href="#/osservatorio/${encodeURIComponent(x.id)}">${esc(x.titolo)}</a></th>${D.valori.map((v) => `<td>${tessera(m[v.id], `role="img" aria-label="${esc(v.nome)}: ${SEGNO[m[v.id]] ? SEGNO[m[v.id]][1] : "non toccato"}"`)}</td>`).join("")}</tr>`; }).join("")}</tbody></table></div>`;
    return `<section class="card quadro-valori" aria-labelledby="h-quadro"><h2 id="h-quadro">Il quadro: ${n} atti sui 10 valori</h2>
      <p class="nota">Per ogni valore della Carta, quanti atti lo peggiorano (a sinistra) e quanti lo migliorano (a destra), secondo i nostri commenti.</p>
      ${barre}
      <details class="sezione"><summary>Atto per atto</summary>${legendaValori()}${matrice}</details></section>`;
  }
  function osservatorio(id, params) {
    const O = D.osservatorio || {}, A = O.atti || [];
    const testa = `<h1>Osservatorio sul governo di oggi</h1>
      <p class="risposta testo-lettura">Che cosa stanno facendo il Governo e il Parlamento per la fine del 2026 e per il 2027, commentato con lo stesso metro che GovernAI usa per sé: prima i fatti, poi un giudizio sui valori della Carta, chiedendosi sempre chi ci guadagna e chi paga. Nessun partito, nessun favoritismo.</p>`;
    const avviso = `<div class="avviso" style="margin:16px 0"><div class="avviso-titolo">${icona("triangle-alert")}Commenti scritti e rivisti da agenti AI</div><p>Non sono ancora stati rivisti da una persona esperta. Il metodo è pubblico: <a href="#/osservatorio/metodo">come scriviamo i commenti</a>. Se trovi un errore, <a href="#/partecipa">segnalalo</a>.</p></div>`;
    if (id === "metodo") return `<p><a href="#/osservatorio">${icona("arrow-left")}Tutti gli atti</a></p><h1>Il metodo dell'Osservatorio</h1><div class="md documento testo-lettura">${md((O.metodo || "").replace(/^# .*\n/, ""))}</div>`;
    if (!A.length) return `${testa}${vuoto("I commenti non sono ancora disponibili.")}`;
    const sel = id && A.find((x) => x.id === id);
    if (sel) {
      const voce = (y) => md(String(y)).replace(/^\s*<p>/, "").replace(/<\/p>\s*$/, "");
      const lista = (v) => `<ul class="testo-lettura">${v.map((y) => `<li>${voce(y)}</li>`).join("")}</ul>`;
      const g = sel.governai || {}, val = sel.valori || [], cg = sel.chi_guadagna || [], cp = sel.chi_paga || [];
      const sa = segniAtto(sel), conta = (x) => Object.values(sa).filter((y) => y === x).length;
      const voci = [["in-30", "In 30 secondi"], ["fatti", "I fatti"], ["chi", "Chi guadagna, chi paga"], ...(sel.rischi_giuridici ? [["rischi", "Rischi giuridici"]] : []), ["giudizio", "Il giudizio sui valori"], ["governai", "GovernAI sullo stesso tema"], ...((sel.cosa_cambieremmo || []).length ? [["cambieremmo", "Che cosa cambieremmo"]] : []), ...((sel.fonti || []).length ? [["fonti", "Fonti"]] : []), ["discussione", "Discussione"]];
      const ordine = ["+", "-", "="];
      const giudizio = [...val].sort((a, b) => ordine.indexOf(a.segno) - ordine.indexOf(b.segno));
      return `<nav class="briciole" aria-label="Briciole di pane"><a href="#/osservatorio">Governo di oggi</a><span aria-hidden="true">›</span><a href="#/osservatorio?tipo=${encodeURIComponent(sel.tipo || "")}">${esc(sel.tipo || "")}</a></nav>
      <div class="con-indice">
        <article>
          <header class="intestazione">
            <p class="etichetta">${esc(sel.tipo || "")}${sel.tema && D.aree[sel.tema] ? " · " + esc(D.aree[sel.tema]) : ""}</p>
            <h1>${esc(sel.titolo)}</h1>
            <p class="nota">${esc(sel.atto || "")}${sel.data ? " · " + esc(dataBreve(sel.data)) : ""}${sel.stato ? " · " + esc(sel.stato) : ""}${sel.fonte ? " · " + ext(sel.fonte, "testo ufficiale") : ""}</p>
            ${indiceMobile(voci)}
          </header>
          <section class="card riassunto blocco" id="in-30" aria-labelledby="h-30" style="margin-top:0">
            <h2 id="h-30">In 30 secondi</h2>
            <p class="testo-lettura grande">${esc(sel.in_breve || "")}</p>
            ${(sel.cifre_chiave || []).length ? `<div class="cifre-chiave">${sel.cifre_chiave.map((c) => `<div class="cifra-k"><p class="numero">${esc(c.numero)}<small>${esc(c.unita || "")}</small></p><p class="cifra-etichetta">${esc(c.etichetta || "")}</p>${c.fonte ? `<p class="nota cifra-fonte">${esc(c.fonte)}</p>` : ""}</div>`).join("")}</div>` : ""}
            <p class="etichetta" style="margin-top:16px">Il giudizio sui 10 valori della Carta</p>
            ${strisciaValori(sel, true)}
            <p class="nota">${conta("+")} a favore · ${conta("-")} contro${conta("±") ? ` · ${conta("±")} in parte sì e in parte no` : ""}${conta("=") ? ` · ${conta("=")} ${conta("=") === 1 ? "neutro" : "neutri"}` : ""} · ${D.valori.length - Object.keys(sa).length} non toccati. <a href="#giudizio" data-ancora>Il perché di ogni giudizio</a></p>
            <div class="riassunto-cifre">
              <a href="#chi" data-ancora class="cifra"><span class="numero">${cg.length}</span><span>gruppi ci guadagnano</span></a>
              <a href="#chi" data-ancora class="cifra"><span class="numero">${cp.length}</span><span>gruppi pagano</span></a>
            </div>
            ${sel.bilancio ? `<div class="nel-complesso"><p class="etichetta">${icona("scale")}Nel complesso</p><p class="testo-lettura">${esc(sel.bilancio)}</p></div>` : ""}
          </section>
          ${avviso}
          <section class="blocco" id="fatti" aria-labelledby="h-fatti">
            <h2 id="h-fatti">I fatti</h2>
            ${(sel.cosa_fa || []).length ? `<h3>Che cosa fa</h3>${lista(sel.cosa_fa)}` : ""}
            ${(sel.numeri || []).length ? `<h3>I numeri</h3><div class="tabella-box"><table class="tabella a-card numeri-atto"><thead><tr><th>Voce</th><th>Valore</th></tr></thead><tbody>${sel.numeri.map((n) => `<tr><td class="principale">${esc(n.voce)}${n.fonte ? `<span class="nota fonte-num">${esc(n.fonte)}</span>` : ""}</td><td data-etichetta="Valore" class="valore-num">${esc(n.valore)}</td></tr>`).join("")}</tbody></table></div>` : ""}
          </section>
          <section class="blocco" id="chi" aria-labelledby="h-chi">
            <h2 id="h-chi">Chi ci guadagna e chi paga</h2>
            <div class="bilancia">${colonnaBilancia("guadagna", "trending-up", "Ci guadagna", cg)}${colonnaBilancia("paga", "wallet", "Paga", cp)}</div>
          </section>
          ${sel.rischi_giuridici ? `<section class="blocco" id="rischi" aria-labelledby="h-rischi"><h2 id="h-rischi">Rischi giuridici</h2><div class="md testo-lettura">${md(String(sel.rischi_giuridici))}</div></section>` : ""}
          <section class="blocco" id="giudizio" aria-labelledby="h-giudizio">
            <h2 id="h-giudizio">Il giudizio sui valori</h2>
            <ul class="giudizi">${giudizio.map((v) => `<li class="${SEGNO[v.segno] ? SEGNO[v.segno][0] : ""}">${tessera(v.segno)}<div><p class="giudizio-nome"><strong>${esc(nomeValore(v.valore))}</strong> <span class="nota">${SEGNO[v.segno] ? SEGNO[v.segno][1] : ""}</span></p><p class="testo-lettura">${esc(v.perche || "")}</p></div></li>`).join("")}</ul>
          </section>
          <section class="blocco" id="governai" aria-labelledby="h-governai">
            <h2 id="h-governai">GovernAI sullo stesso tema</h2>
            ${(g.proposte || []).length ? `<div class="chips">${g.proposte.map((q) => proposta(q) ? `<a class="chip info" href="${linkP(q)}">${icona("list-checks")}${esc(q)} · ${esc(tit(proposta(q).titolo))}</a>` : `<a class="chip info" href="#/programma/coperture">${icona("coins")}${esc(q)} · copertura</a>`).join("")}</div>` : ""}
            <p class="testo-lettura">${esc(g.confronto || "")}</p>
          </section>
          ${(sel.cosa_cambieremmo || []).length ? `<section class="blocco" id="cambieremmo" aria-labelledby="h-camb"><h2 id="h-camb">Che cosa cambieremmo</h2>${lista(sel.cosa_cambieremmo)}</section>` : ""}
          ${(sel.domande_aperte || []).length ? `<section class="blocco" aria-labelledby="h-dom"><h2 id="h-dom">Domande ancora aperte</h2>${lista(sel.domande_aperte)}</section>` : ""}
          ${(sel.fonti || []).length ? `<details class="blocco" id="fonti"><summary>Fonti (${sel.fonti.length})</summary><ul>${sel.fonti.map((f) => { const u = String(f).match(/https?:\/\/\S+/); return `<li class="nota">${u ? esc(String(f).replace(u[0], "").replace(/[,:;\s(]+$/, "")) + " " + ext(u[0].replace(/[).,;]+$/, ""), "link") : esc(f)}</li>`; }).join("")}</ul></details>` : ""}
          ${(sel.revisioni || []).length ? `<p class="nota">${sel.revisioni.map((r) => `${esc(dataBreve(r.data))}: ${esc(r.nota)}`).join(" · ")} Sorgente: <code>${esc(sel.file)}</code>${D.repo ? `, ${ext(D.repo + "/blob/main/" + sel.file, "su GitHub")}` : ""}.</p>` : ""}
          <div id="discussione">${C ? C.sezione("atto:" + sel.id, "Discussione della comunità su questo atto") : ""}</div>
        </article>
        ${indiceLaterale(voci, azioniCondividi())}
      </div>`;
    }
    const tipo = params.get("tipo") || "tutti";
    const vis = A.filter((x) => tipo === "tutti" || x.tipo === tipo);
    return `${testa}${avviso}
      ${quadroValori(vis)}
      <nav class="schede" aria-label="Tipo di atto">${TIPI_ATTO.filter(([k]) => k === "tutti" || A.some((x) => x.tipo === k)).map(([k, t]) => `<a href="#/osservatorio${k === "tutti" ? "" : "?tipo=" + encodeURIComponent(k)}" ${k === tipo ? 'aria-current="page"' : ""}>${esc(t)} <span class="conta">${k === "tutti" ? A.length : A.filter((x) => x.tipo === k).length}</span></a>`).join("")}</nav>
      ${legendaValori()}
      <div class="griglia g2-d">${vis.map((x) => `<a class="card atto-card" href="#/osservatorio/${encodeURIComponent(x.id)}"><p class="etichetta">${esc(x.tipo || "")}${x.tema && D.aree[x.tema] ? " · " + esc(D.aree[x.tema]) : ""}</p><h3 class="titolo-card">${esc(x.titolo)}</h3>${strisciaValori(x, false)}<p class="nota riga2">${esc(x.in_breve || "")}</p></a>`).join("")}</div>
      <p class="nota" style="margin-top:16px"><a href="#/osservatorio/metodo">Il metodo</a> · ${A.length} atti commentati · ultimo aggiornamento ${esc(dataBreve(A.flatMap((x) => (x.revisioni || []).map((r) => r.data)).sort().pop() || ""))}</p>`;
  }

  // documenti lunghi: si legge subito il riassunto, i capitoli si aprono uno alla volta
  function documentoACapitoli(testo, aperto) {
    const parti = String(testo).replace(/^# .*\n/, "").split(/^(?=## )/m);
    const testa = parti[0].startsWith("## ") ? "" : parti.shift();
    const cap = parti.map((x) => { const t = x.match(/^## (.+)\n/)[1]; return [t, x.replace(/^## .+\n/, "")]; });
    const primo = cap.find((c) => c[0].trim() === aperto);
    return `<div class="md documento">${testa ? md(testa) : ""}${primo ? md("## " + primo[0] + "\n" + primo[1]) : ""}</div>
      <p class="nota">${cap.length - (primo ? 1 : 0)} capitoli: aprili uno alla volta.</p>
      ${cap.filter((c) => c !== primo).map((c) => `<details class="richiudibile capitolo"><summary>${esc(c[0])}<span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo md documento">${md(c[1])}</div></details>`).join("")}`;
  }
  function equita() {
    return `${schedeProgramma("equita")}
      ${documentoACapitoli(D.documenti.equita || "*Capitolo non ancora disponibile.*", "In breve")}
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
  const schedeGoverno = (k) => `${bannerSim("fisso")}${schede([["sedute", "Sedute", "#/governo", VERBALI.length], ["decisioni", "Esiti ancora validi", "#/governo/decisioni"], ["mandati", "Mandati", "#/governo/mandati", (D.governo.mandati || []).filter((m) => m.stato === "aperto").length], ["credibilita", "Credibilità", "#/governo/credibilita"], ["regolamento", "Chi siede e regole", "#/governo/regolamento"]], k, "Governo ombra")}`;

  function governo() {
    const decisioni = VERBALI.reduce((a, v) => a + v.dec.length, 0);
    return `${schedeGoverno("sedute")}
      <p class="risposta">Una simulazione di governo con agenti AI e regole verificabili: esperti di ogni materia, nove ministri, un'opposizione leale e un capo di governo, tutti agenti AI. Serve a mettere alla prova le proposte, non a decidere: in ${VERBALI.length} sedute ha esaminato ${decisioni} proposte.</p>
      <div class="azioni" style="margin-bottom:8px"><a class="btn primario" href="${esc(linkConsiglio())}" target="_blank" rel="noopener">${icona("message-circle-question")}Fai una domanda al Consiglio<span class="vh"> (si apre in una nuova scheda)</span></a><a class="btn" href="#/partecipa">Altri modi di partecipare</a></div>
      <p class="nota">Il Consiglio si riunisce ogni lunedì, quando scatta un'allerta nuova e su richiesta approvata da una persona del progetto.</p>
      <div class="griglia" style="margin-top:24px">${VERBALI.map((x) => `<a class="card" href="${linkSeduta(x.id)}"><p class="etichetta">${dataBreve(x.data)} · ${esc(x.tipo)}</p><h2 class="titolo-card" style="font-size:22px">${esc(x.titolo)}</h2>${x.domanda ? `<p class="nota">«${esc(x.domanda)}»</p>` : ""}${contatore(x.dec)}<p class="nota">${x.deroghe.length} deroghe · ${x.obiezioni.length} obiezioni · ${x.mandati.length} mandati</p></a>`).join("") || vuoto("Il Consiglio non si è ancora riunito.")}</div>`;
  }
  function decisioniInVigore() {
    const V = D.governo.verifiche || [];
    return `${schedeGoverno("decisioni")}
      <p class="risposta">Ogni giorno il sistema riverifica, con un controllo ripetibile, se gli esiti della simulazione ancora validi reggono sui dati di oggi. Se una non regge, il riesame si mette in coda da solo.</p>
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
              <li><a href="#decisioni"><b>Capo di governo</b><span>${v.dec.length} esiti</span></a></li>
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
              <h3 class="titolo-card"><a href="${linkP(d.id)}">${esc(tit(p ? p.titolo : d.titolo))}</a> <span class="codice">${esc(d.id)}</span></h3>
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
  const schedeDati = (k) => `${schede([["indicatori", "Indicatori", "#/dati", (D.indicatori || []).length], ["allerte", "Allerte", "#/dati/allerte", ALLERTE.length], ["obiettivi", "Obiettivi e risultati", "#/dati/obiettivi", (D.obiettivi || []).length], ["diario", "Diario quotidiano", "#/dati/diario"], ["storia", "50 anni di scelte", "#/dati/storia"], ["governi", "Governi a confronto", "#/dati/governi"], ["verifica", "Verifica un confronto", "#/dati/verifica"], ["fonti", "Stato delle fonti", "#/dati/fonti", ((D.fonti || {}).serie || []).length]], k, "Dati")}`;
  function datiVista() {
    const ok = (D.indicatori || []).filter((i) => i.stato === "ok");
    const salgono = ALLERTE.map((r) => nomeInd(r.ind).split(" (")[0].toLowerCase()).filter((x, i, a) => x && a.indexOf(x) === i);
    return `${schedeDati("indicatori")}
      <p class="risposta">${ALLERTE.length ? `${ALLERTE.length} allerte attive su ${D.indicatori.length} indicatori: ${esc(salgono.join(", "))}.` : `Nessuna allerta: i ${D.indicatori.length} indicatori sono nelle soglie.`} Ultimo dato disponibile e variazione sul periodo precedente.</p>
      ${ALLERTE.length ? `<div class="griglia g2-d">${ALLERTE.slice(0, 2).map((r) => avvisoAllerta(r, true)).join("")}</div><p><a href="#/dati/allerte">Tutte le allerte ${icona("arrow-right")}</a></p>` : ""}
      ${GRUPPI.map(([nome, ids]) => { const l = ids.map((id) => ok.find((i) => i.id === id)).filter(Boolean); return l.length ? `<section class="sezione"><div class="sezione-testa"><h2>${esc(nome)}</h2></div><div class="indicatori">${l.map(cardIndicatore).join("")}</div></section>` : ""; }).join("")}
      <p class="nota sezione">HICP: indice armonizzato dei prezzi al consumo. PIL: prodotto interno lordo. NEET: giovani che non lavorano, non studiano e non seguono una formazione. Spread IT-DE: differenza di rendimento tra titoli decennali italiani e tedeschi.</p>`;
  }
  function fontiVista(params) {
    const F = D.fonti || { serie: [], controllo: {} }, K = F.controllo || {};
    const area = params.get("area") || "";
    const lista = F.serie.filter((x) => !area || x.area.startsWith(area)).sort((x, y) => (y.aggiornato || "").localeCompare(x.aggiornato || "") || x.nome.localeCompare(y.nome));
    const conData = F.serie.filter((x) => x.aggiornato).length;
    const aree = [...new Set(F.serie.map((x) => x.area.slice(0, 2)))].sort();
    const nomeArea = (a) => (D.aree || {})[a] || ({ "00": "Quadro generale", bm: "Confronti internazionali", ob: "Obiettivi" })[a] || a;
    const modo = { mirato: "Controllo mirato: rilanciati solo gli script delle fonti cambiate", completo: "Controllo completo: rilanciati tutti gli script" }[K.modalita] || "Nessuna fonte cambiata";
    return `${schedeDati("fonti")}
      <p class="risposta">${F.serie.length} serie ufficiali alla base del programma. Per ognuna: chi la pubblica, quando la fonte l'ha aggiornata e quando l'abbiamo scaricata. Ogni giorno una sentinella controlla se le fonti hanno pubblicato dati nuovi e rilancia gli script che li scaricano.</p>
      <div class="griglia g3">
        <div class="card"><p class="etichetta">Ultimo controllo</p><h3>${K.data ? dataBreve(K.data) : "—"}</h3><p>${esc(modo)}${K.ultimo_completo ? `; ultimo controllo completo il ${dataBreve(K.ultimo_completo)}` : ""}.</p></div>
        <div class="card"><p class="etichetta">Che cosa controlla</p><h3>${(K.eurostat || 0) + (K.file || 0) + (K.pagine || 0)} fonti</h3><p>${K.eurostat || 0} tabelle Eurostat, ${K.file || 0} file di ministeri ed enti, ${K.pagine || 0} pagine istituzionali dove escono documenti nuovi.</p></div>
        <div class="card"><p class="etichetta">Esito</p><h3>${(K.errori || []).length ? `${K.errori.length} problemi` : "Nessun errore"}</h3><p>Nell'ultimo controllo: ${K.aggiornati === 1 ? "1 fonte aggiornata" : `${K.aggiornati || 0} fonti aggiornate`}, ${K.documenti_nuovi === 1 ? "1 documento nuovo" : `${K.documenti_nuovi || 0} documenti nuovi`}.${(K.errori || []).length ? " " + esc(K.errori.join("; ")) : ""}</p></div>
      </div>
      <form class="filtri-barra" onsubmit="return false"><label class="campo">Tema<select id="fo-area"><option value="">Tutti i temi</option>${aree.map((a) => `<option value="${a}" ${a === area ? "selected" : ""}>${esc(nomeArea(a))}</option>`).join("")}</select></label></form>
      <div class="tabella-scorre"><table class="tabella a-card fo-tab"><thead><tr><th>Serie</th><th>Fonte</th><th>Aggiornata dalla fonte</th><th>Scaricata da noi</th><th>Dati</th></tr></thead>
      <tbody>${lista.map((x) => `<tr><td class="principale">${esc(String(x.nota || x.nome).replace(/^./, (c) => c.toUpperCase()))}<small class="mono">${esc(x.nome)}</small></td><td data-etichetta="Fonte">${x.url ? ext(x.url, esc(x.fonte)) : esc(x.fonte)}</td><td data-etichetta="Aggiornata dalla fonte">${x.aggiornato ? dataBreve(x.aggiornato) : "non indicato"}</td><td data-etichetta="Scaricata da noi">${x.scaricato ? dataBreve(x.scaricato) : "—"}</td><td data-etichetta="Dati">${x.file ? `<a href="${esc(RAW + x.file)}" download>CSV</a>` : "—"}</td></tr>`).join("")}</tbody></table></div>
      <p class="nota">${conData} serie su ${F.serie.length} hanno la data di aggiornamento della fonte; per le altre (documenti PDF, cifre trascritte da relazioni) conta la data del documento citato nella scheda. Un dato vecchio non è un errore: molte statistiche escono una volta l'anno. Registri: <code>dati/serie/_registro_*.csv</code>; sentinella: <code>sistema/sentinella.py</code>.</p>`;
  }
  function allerteVista() {
    return `${schedeDati("allerte")}
      <p class="risposta">Le allerte scattano da regole fisse e pubbliche (<code>sistema/config.yaml</code>). Quando una è attiva, la versione «Completo adattato ai dati di oggi» cambia priorità: mostra che cosa suggerirebbero i dati, senza cambiare il programma di riferimento.</p>
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
      <p class="risposta">Ogni misura ha obiettivi misurabili, con un valore di partenza e un traguardo. Il programma non è in vigore: per ora seguiamo come va il Paese su questi numeri, così quando una misura partirà si vedrà subito se funziona.</p>
      <div class="chips">${Object.entries(conta).map(([k, v]) => chip([...(STATO[k] || ["", "circle-dot", k])].map((x, i) => i === 2 ? `${x}: ${v}` : x))).join("")}</div>
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
  const schedeControlli = (k) => `${schede([["costituzione", "Costituzione", "#/controlli/costituzione"], ["europa", "Europa", "#/controlli/europa"], ["integrita", "Integrità", "#/controlli/integrita"]], k, "Controlli", `<p class="nota" style="margin:0">Prima i vincoli, poi i valori: Costituzione, diritto europeo e integrità non si pesano, si rispettano.</p>`)}`;
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
  const DOCUMENTI = { programma: "Programma", garanzie: "Garanzie e responsabilità", metodo: "Metodo degli agenti", sistema: "Sistema dinamico", giuridico: "Quadro giuridico e UE", trasparenza: "Rischio negli appalti", legislazione: "Legislazione e redazione" };
  const schedeMetodo = (k) => `${schede([["come", "Come funziona", "#/metodo"], ["carta", "Carta dei valori", "#/metodo/carta"], ["documenti", "Documenti", "#/metodo/documenti"], ["glossario", "Glossario", "#/metodo/glossario"]], k, "Metodo")}`;
  function metodo() {
    const n = D.numeri || {};
    const passi = [
      ["Dati ufficiali, ogni giorno", "Una sentinella controlla Eurostat, ISTAT, MEF, Banca d'Italia, UPB e altre fonti, scarica solo ciò che è cambiato e ne conserva la storia."],
      ["Valori dichiarati", `Una Carta di ${n.valori || 10} valori, dal rispetto delle diversità alla responsabilità verso il futuro. Nessuna etichetta di destra, di sinistra o di centro.`],
      ["Tre valutatori AI", "Tre agenti AI, distinti da quelli che hanno scritto le proposte, danno un punteggio a ogni misura su ogni valore. Il loro disaccordo diventa incertezza dichiarata. Non sono persone: la revisione di persone con orientamenti diversi è il passo successivo."],
      ["Robustezza, non un peso unico", "Il motore prova migliaia di combinazioni di pesi e separa ciò che conviene con quasi tutti i pesi da ciò che è una scelta politica."],
      ["Senza deficit", "Ogni misura preleva da coperture concrete, contate al gettito minimo, o da fondi europei già stanziati: un registro unico impedisce di contare due volte gli stessi soldi."],
      ["Controlli che non si pesano", "Costituzione, diritto europeo e linee rosse sono verificati prima di ogni decisione. Il governo ombra simulato lavora solo dentro questi limiti."],
      ["Verificabile e capace di imparare", "Ogni esecuzione lascia un'impronta nel registro di integrità. Ogni misura ha obiettivi misurabili: quando i risultati si discostano, il sistema ricalibra."],
    ];
    return `${schedeMetodo("come")}
      <p class="risposta">GovernAI è un prototipo: agenti di intelligenza artificiale analizzano i problemi del Paese, propongono opzioni con costi e coperture e rendono espliciti i compromessi. <strong>Le decisioni restano alle persone.</strong></p>
      <ol class="passi sezione">${passi.map(([t, d]) => `<li><strong>${esc(t)}</strong><span>${esc(d)}</span></li>`).join("")}</ol>
      <section class="sezione"><div class="sezione-testa"><h2>Limiti dichiarati</h2></div>
        <ul class="mandati"><li>Le stime di costo sono stime GovernAI: nessuna è certificata dalla Ragioneria generale dello Stato.</li><li>Il governo ombra è una simulazione con agenti AI: le sue decisioni non sono in vigore e non rappresentano persone reali.</li><li>I tre valutatori che danno i punteggi sono agenti AI, non persone: sono distinti da chi ha scritto le proposte, ma non da chi ha progettato il sistema. Il loro accordo misura la coerenza, non la correttezza.</li><li>Il controllo costituzionale è preventivo e automatico, con revisione umana: non sostituisce la Corte costituzionale.</li><li>Alcuni dati sono provvisori e possono essere rivisti dalla fonte.</li></ul></section>`;
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
  const GLOSSARIO = [["A.C.", "Atto della Camera: numero con cui la Camera dei deputati identifica un progetto di legge."], ["Accisa", "Imposta su alcuni prodotti, come carburanti, energia, alcolici e tabacchi, calcolata sulla quantità venduta."], ["AI", "Intelligenza artificiale."], ["APE sociale", "Anticipo pensionistico: un assegno pagato dallo Stato a chi, in alcune condizioni difficili, lascia il lavoro prima dell'età della pensione."], ["ARERA", "Autorità di regolazione per energia reti e ambiente: fissa regole e tariffe per luce, gas, acqua e rifiuti."], ["Brier (punteggio di)", "Misura la qualità delle previsioni: 0 è perfetta, 0,25 come tirare a caso, 1 sempre sbagliata."], ["Catena di integrità", "Registro di impronte crittografiche: ogni anello contiene l'impronta del precedente, così una modifica nascosta si vede."], ["CELEX", "Codice che identifica un atto nella banca dati del diritto europeo EUR-Lex."], ["Clausola nazionale", "Regola europea che permette a uno Stato di spendere di più per la difesa senza violare il percorso di spesa concordato con l'UE."], ["Copertura", "Il modo in cui si paga una misura: un'entrata nuova o un taglio di spesa, indicato prima di spendere."], ["Decreto-legge (DL)", "Atto con forza di legge che il Governo adotta in casi di urgenza. Vale subito, ma perde effetto se il Parlamento non lo converte in legge entro 60 giorni."], ["Decreto legislativo (d.lgs.)", "Atto del Governo con forza di legge, adottato su delega del Parlamento ed entro i limiti fissati dalla legge di delega."], ["Deroga", "Decisione del capo di governo che si discosta dall'esito del motore, sempre dichiarata e motivata."], ["Detrazione", "Somma che si toglie dall'imposta da pagare, per esempio una parte delle spese sanitarie."], ["Disegno di legge (DDL)", "Proposta di legge presentata alle Camere, per esempio dal Governo. Diventa legge solo se Camera e Senato la approvano."], ["DPB", "Documento programmatico di bilancio: il testo che ogni autunno il Governo manda alla Commissione europea con i conti dell'anno successivo."], ["DPFP", "Documento programmatico di finanza pubblica: il documento con cui il Governo presenta il quadro dei conti pubblici e gli obiettivi dei prossimi anni."], ["Governo ombra", "Simulazione di un Consiglio dei ministri fatto di agenti AI con ruoli distinti. Le decisioni non sono in vigore."], ["HICP", "Indice armonizzato dei prezzi al consumo, misura europea dell'inflazione."], ["INPS", "Istituto nazionale della previdenza sociale: paga le pensioni e molte prestazioni sociali."], ["IRAP", "Imposta regionale sulle attività produttive: la pagano le imprese sul valore della produzione."], ["IRES", "Imposta sul reddito delle società."], ["IRPEF", "Imposta sul reddito delle persone fisiche: la principale imposta su stipendi, pensioni e altri redditi delle persone."], ["ISEE", "Indicatore della situazione economica equivalente: misura reddito e patrimonio della famiglia e decide l'accesso a molti aiuti."], ["ISTAT", "Istituto nazionale di statistica."], ["IVA", "Imposta sul valore aggiunto: si paga su beni e servizi acquistati."], ["LEP", "Livelli essenziali delle prestazioni: i servizi minimi che lo Stato deve garantire allo stesso modo in tutto il Paese."], ["Linea rossa", "Limite della Carta che nessuna proposta può superare: se lo supera, è esclusa automaticamente."], ["Mandato", "Compito con scadenza affidato a un ministro dal Consiglio."], ["MEF", "Ministero dell'economia e delle finanze."], ["NEET", "Giovani che non lavorano, non studiano e non seguono una formazione."], ["Nucleo robusto", "Proposte che restano nella prima metà della classifica con quasi ogni combinazione di pesi tra i valori."], ["Opposizione leale", "Ruolo che cerca il punto debole di ogni decisione, con prove; il capo di governo deve rispondere per iscritto."], ["Payback", "Restituzione che le imprese di farmaci e dispositivi medici versano alle Regioni quando la spesa pubblica supera il tetto fissato."], ["PIL", "Prodotto interno lordo."], ["PNRR", "Piano nazionale di ripresa e resilienza: il piano di investimenti e riforme finanziato dall'Unione europea dopo la pandemia."], ["Relazione tecnica", "Documento che accompagna una legge e ne stima costi ed effetti sui conti pubblici; la verifica la Ragioneria generale dello Stato."], ["RGS", "Ragioneria generale dello Stato."], ["Spread", "Differenza di rendimento tra titoli di Stato italiani e tedeschi a 10 anni, in punti base."], ["Stima GovernAI", "Cifra calcolata dal modello, non certificata dalla Ragioneria."], ["TFUE", "Trattato sul funzionamento dell'Unione europea: contiene, tra l'altro, le regole sugli aiuti di Stato (artt. 107-108)."], ["TPL", "Trasporto pubblico locale: autobus, tram, metropolitane e treni regionali."], ["UE", "Unione europea."], ["UPB", "Ufficio parlamentare di bilancio."], ["Variante", "La dose di una misura: Piena, Essenziale, Pilota o Zero."], ["ZES", "Zona economica speciale: area con agevolazioni per chi investe. Oggi c'è una ZES unica per il Mezzogiorno."]];
  GLOSSARIO.push(["A regime", "Quando una misura è partita del tutto, dopo gli anni di avvio: il costo o l'effetto «a regime» è quello di ogni anno da lì in poi."], ["Scenario", "Una delle versioni complete del programma (base, intermedio, completo…): ognuna sceglie quali misure fare e con quali coperture, sempre senza deficit."], ["Versione piena, essenziale, pilota", "La «dose» di una misura: piena è tutta, essenziale è la parte più importante, pilota è una prova in pochi luoghi, solo regole costa quasi zero."], ["Fondi di coesione", "Fondi europei per ridurre i divari tra territori, già assegnati all'Italia per il 2021-2027 e spendibili fino al 2029."], ["Spese fiscali", "Sconti sulle tasse (detrazioni, deduzioni, esenzioni, aliquote ridotte): lo Stato rinuncia a un'entrata invece di fare una spesa."], ["Sussidi dannosi per l'ambiente", "Agevolazioni che rendono più conveniente inquinare, per esempio sconti sul gasolio; il Ministero dell'ambiente le elenca ogni anno."]);
  GLOSSARIO.sort((a, b) => a[0].localeCompare(b[0], "it"));
  // parole cercate nelle pagine: la voce del glossario e le forme con cui compare nel testo
  const TERMINI = [["Accisa", "accis[ae]"], ["Copertura", "coperture"], ["Detrazione", "detrazion[ei]"], ["Linea rossa", "line[ae] ross[ae]"], ["Nucleo robusto", "nucleo robusto"], ["Variante", "variant[ei]"], ["Spread", "spread"], ["PIL", "PIL"], ["PNRR", "PNRR"], ["ISEE", "ISEE"], ["LEP", "LEP"], ["NEET", "NEET"], ["HICP", "HICP"], ["IRES", "IRES"], ["IRAP", "IRAP"], ["UPB", "UPB"], ["RGS", "RGS"], ["DPB", "DPB"], ["DPFP", "DPFP"], ["ZES", "ZES"], ["TPL", "TPL"], ["Payback", "payback"], ["Clausola nazionale", "clausola nazionale"], ["Relazione tecnica", "relazion[ei] tecnich?[ae]"], ["Governo ombra", "governo ombra"], ["A regime", "a regime"], ["Scenario", "scenari[o]?"], ["Fondi di coesione", "fondi (?:europei )?(?:di|della) coesione"], ["Spese fiscali", "spese fiscali"], ["Sussidi dannosi per l'ambiente", "sussidi dannosi"]];
  const RE_TERMINI = new RegExp("(^|[^\\p{L}\\d])(" + TERMINI.map(([, r]) => r).join("|") + ")(?![\\p{L}\\d])", "iu");
  const definizione = (parola) => { const t = TERMINI.find(([, r]) => new RegExp("^(?:" + r + ")$", "iu").test(parola)); const g = t && GLOSSARIO.find((x) => x[0] === t[0]); return g ? g : null; };
  function segnaCodici(radice) {
    const salta = "a,button,h1,h2,h3,h4,summary,label,code,.mono,.codice,nav,select,option,textarea,input,.chip,.etichetta,script,style,[data-c]";
    const w = document.createTreeWalker(radice, NodeFilter.SHOW_TEXT, { acceptNode: (n) => /\b\d{2}-[PC]\d{1,2}\b/.test(n.nodeValue) && !n.parentElement.closest(salta) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT });
    const nodi = []; while (w.nextNode()) nodi.push(w.currentNode);
    for (const n of nodi) {
      const parti = n.nodeValue.split(/\b(\d{2}-[PC]\d{1,2})\b/);
      if (parti.length < 2) continue;
      const f = document.createDocumentFragment();
      parti.forEach((t, i) => {
        if (i % 2 && proposta(t)) { const a = document.createElement("a"); a.className = "codice"; a.href = linkP(t); a.textContent = t; a.title = tit(proposta(t).titolo); f.appendChild(a); }
        else if (t) f.appendChild(document.createTextNode(t));
      });
      n.replaceWith(f);
    }
  }
  function segnaTermini(radice) {
    const visti = new Set();
    const salta = "a,button,h1,h2,h3,h4,summary,label,code,.mono,nav,select,option,textarea,input,.chip,.badge,.etichetta,dt,th,svg,script,style,.termine,.popover,[data-c]";
    const w = document.createTreeWalker(radice, NodeFilter.SHOW_TEXT, { acceptNode: (n) => n.nodeValue.trim().length > 2 && !n.parentElement.closest(salta) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT });
    const nodi = []; while (w.nextNode()) nodi.push(w.currentNode);
    for (const n of nodi) {
      const m = n.nodeValue.match(RE_TERMINI); if (!m) continue;
      const g = definizione(m[2]); if (!g || visti.has(g[0])) continue;
      visti.add(g[0]);
      const inizio = m.index + m[1].length, dopo = n.splitText(inizio); dopo.splitText(m[2].length);
      const b = document.createElement("button"); b.type = "button"; b.className = "termine"; b.dataset.def = g[1]; b.dataset.termine = g[0]; b.setAttribute("aria-haspopup", "dialog");
      b.textContent = dopo.nodeValue; dopo.replaceWith(b);
      if (visti.size >= 12) break;
    }
  }
  function glossario() {
    const voci = GLOSSARIO;
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
        <div class="azioni"><a class="btn s" href="${esc(nuovoFile("governo/richieste", "domanda", "# Titolo della domanda\n\n**Domanda:** \n\n**Perché ora:** \n\n**Vincoli o attenzioni:** \n\nMinistri: \n"))}" target="_blank" rel="noopener">Convoca il Consiglio<span class="vh"> (si apre in una nuova scheda)</span></a><a class="btn s" href="${esc(nuovoFile("analisi/richieste", "nuova-richiesta", "# Titolo del problema\n\n### Problema\n\n### Obiettivo\n\n### Area principale\n\n### Vincoli o attenzioni\n"))}" target="_blank" rel="noopener">Richiesta di analisi diretta<span class="vh"> (si apre in una nuova scheda)</span></a><a class="btn s" href="#/governo/decisioni">Chiedi un riesame</a></div></div></details>`;
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
      else if (b === "proponi") { html = proponi(params); titolo = "Proponi un programma"; }
      else if (b === "strategia") { html = strategia(); titolo = "Strategia oceano blu"; }
      else if (b === "ai") { html = aiPagina(); titolo = "L'AI come chiave per l'Italia"; }
      else if (b === "chi-paga") { html = chiPaga(params); titolo = "Chi paga davvero"; }
      else if (b === "confronti") { html = confronti(params); titolo = "Confronti"; }
      else if (b === "sintesi") { html = sintesi(); titolo = "Le idee in sintesi"; }
      else if (b === "equita") { html = equita(); titolo = "Equità e linguaggio inclusivo"; }
      else if (b === "una-pagina") { html = unaPagina(params); titolo = "Il programma in una pagina"; }
      else if (b === "mappa") { html = `${schedeProgramma("mappa")}${mappaMinisteri(Object.keys(D.aree).map((k) => [k, D.aree[k], D.proposte.filter((p) => p.area === k).length]))}`; titolo = "La mappa dei ministeri"; }
      else if (b === "per-me") { html = perMe(params); titolo = "Che cosa cambia per me"; }
      else if (b === "busta-paga") { html = bustaPaga(params); titolo = "La tua busta paga con GovernAI"; }
      else if (b === "pronto") { html = prontoDomani(params); titolo = "Pronto domani"; }
      else { html = elenco(params); titolo = "Programma"; }
    } else if (a === "osservatorio") {
      html = osservatorio(b, params); titolo = b && b !== "metodo" ? tit((((D.osservatorio || {}).atti || []).find((x) => x.id === b) || {}).titolo || "Atto") : b === "metodo" ? "Il metodo dell'Osservatorio" : "Osservatorio sul governo di oggi";
    } else if (a === "governo") {
      if (b === "sedute" && c) { html = schedaSeduta(c); titolo = "Seduta " + del_(c); }
      else if (b === "decisioni") { html = decisioniInVigore(); titolo = "Esiti ancora validi"; }
      else if (b === "mandati") { html = mandatiVista(); titolo = "Mandati"; }
      else if (b === "credibilita") { html = credibilita(); titolo = "Credibilità"; }
      else if (b === "regolamento") { html = regolamento(); titolo = "Regolamento del Consiglio"; }
      else { html = governo(); titolo = "Governo ombra"; }
    } else if (a === "dati") {
      if (b === "allerte") { html = allerteVista(); titolo = "Allerte"; }
      else if (b === "obiettivi") { html = obiettiviVista(params); titolo = "Obiettivi e risultati"; }
      else if (b === "diario") { html = diario(c); titolo = "Diario quotidiano"; }
      else if (b === "storia") { html = storiaVista(params); titolo = "50 anni di scelte"; }
      else if (b === "governi") { html = governiVista(params); titolo = "Governi a confronto"; }
      else if (b === "verifica") { html = verificaVista(params); titolo = "Verifica un confronto"; }
      else if (b === "fonti") { html = fontiVista(params); titolo = "Stato delle fonti"; }
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
    html += scaricaDati(fileDiPagina(a, b, params));
    main.innerHTML = html;
    if (["programma", "dati", "osservatorio", "governo", "controlli"].includes(a)) { segnaCodici(main); segnaTermini(main); }
    if (C) C.monta(main);
    document.title = `${titolo} · GovernAI`;
    $$("[data-voce]").forEach((x) => { if (x.dataset.voce === voce) x.setAttribute("aria-current", "page"); else x.removeAttribute("aria-current"); });
    // comportamenti delle viste interattive
    if ($("#f-corpo")) { ["#f-cerca", "#f-tema", "#f-classe", "#f-incluse"].forEach((s) => $(s).addEventListener("input", aggiornaElenco)); aggiornaElenco(); }
    if ($("#c-corpo")) { const filtra = () => { const t = $("#c-cerca").value.toLowerCase(), f = $("#c-fondo").value, l = $("#c-livello").value; $$("#c-corpo tr").forEach((tr) => { tr.hidden = (t && !tr.dataset.testo.includes(t)) || (f && tr.dataset.fondo !== f) || (l && tr.dataset.livello !== l); }); }; ["#c-cerca", "#c-fondo", "#c-livello"].forEach((s) => $(s).addEventListener("input", filtra)); }
    if ($("#pp-app")) montaProponi();
    if ($("#st-dec")) montaStoria();
    if ($("#vf-per")) montaVerifica();
    if ($("#pv-lista")) montaPV();
    if ($("#gv-sel")) $("#gv-sel").addEventListener("change", (e) => { const q = new URLSearchParams(location.hash.split("?")[1] || ""); q.set("g", e.target.value); location.hash = "#/dati/governi?" + q.toString(); });
    if ($("#classifica")) { $$("input[type=range]", main).forEach((el) => el.addEventListener("input", aggiornaClassifica)); aggiornaClassifica(); }
    if ($("#q")) { $("#q").addEventListener("input", aggiornaRicerca); aggiornaRicerca(); $("#q").focus(); }
    if ($("#schema-scenario")) $("#schema-scenario").addEventListener("change", (e) => { location.hash = "#/programma/una-pagina" + (e.target.value === (D.schema || {}).scenario ? "" : "?scenario=" + e.target.value); });
    if ($("#bp-esito")) { $$(".busta-form input, .busta-form select", main).forEach((el) => el.addEventListener("input", aggiornaBusta)); aggiornaBusta(); }
    if ($("#fo-area")) $("#fo-area").addEventListener("change", (e) => { location.hash = "#/dati/fonti" + (e.target.value ? "?area=" + e.target.value : ""); });
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
    const td = e.target.closest("[data-def]");
    if (td) {
      e.preventDefault(); const gia = pop && pop._da === td; chiudiPop(); if (gia) return;
      pop = document.createElement("div"); pop._da = td; pop.className = "popover"; pop.setAttribute("role", "dialog"); pop.setAttribute("aria-label", "Che cosa vuol dire");
      pop.innerHTML = `<strong>${esc(td.dataset.termine)}</strong>${esc(td.dataset.def)}<br><a href="#/metodo/glossario">Tutto il glossario</a>`;
      document.body.appendChild(pop);
      const r = td.getBoundingClientRect(), w = Math.min(320, innerWidth - 32);
      pop.style.width = w + "px"; pop.style.left = Math.max(16, Math.min(r.left + scrollX, innerWidth - w - 16)) + "px"; pop.style.top = (r.bottom + scrollY + 6) + "px";
      td.setAttribute("aria-expanded", "true"); return;
    }
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
    if (s) { const pr = new URLSearchParams(location.hash.split("?")[1] || ""); pr.set("scenario", s.dataset.scenario); if (s.dataset.scenario === RIF_ID) pr.delete("scenario"); location.hash = "#/programma" + (pr.toString() ? "?" + pr : ""); }
    const sv = e.target.closest(".scelta-valore");
    if (sv) {
      const gruppo = sv.closest("[data-passo]"), su = gruppo.dataset.passo === "su";
      const premuti = $$(".scelta-valore[aria-pressed=true]", gruppo);
      if (sv.getAttribute("aria-pressed") === "true") sv.setAttribute("aria-pressed", "false");
      else if (su && premuti.length >= 3) { $("#passi-esito").textContent = "Al massimo tre: togline uno prima di sceglierne un altro."; return; }
      else { if (!su) premuti.forEach((x) => x.setAttribute("aria-pressed", "false")); sv.setAttribute("aria-pressed", "true"); }
      applicaPassiValori(); return;
    }
    if (e.target.closest("[data-azione-valori=azzera]")) { $$(".scelta-valore").forEach((x) => x.setAttribute("aria-pressed", "false")); applicaPassiValori(); return; }
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
