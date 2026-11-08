/* GovernAI · prototipo del design (home, scheda della proposta, verbale di seduta).
   Legge window.GOVERNAI da ../../docs/data.js. Non è il sito definitivo: serve a validare design/04_design_system.md. */
(function () {
  "use strict";
  const D = window.GOVERNAI;
  const main = document.getElementById("contenuto");
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const nf = (n, d = 2) => n == null || n === "" ? "—" : Number(n).toLocaleString("it-IT", { minimumFractionDigits: d, maximumFractionDigits: d });
  const MESI = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"];
  const dataBreve = (iso) => { const [a, m, g] = String(iso).slice(0, 10).split("-"); return `${+g} ${MESI[+m - 1]} ${a}`; };
  const dataLunga = (iso) => new Date(String(iso).slice(0, 10) + "T12:00").toLocaleDateString("it-IT", { day: "numeric", month: "long", year: "numeric" });
  const piano = (s) => String(s || "").replace(/\*\*|`/g, "").replace(/\[([^\]]+)\]\([^)]+\)/g, "$1").trim();
  const valoreBreve = (v) => { const m = String(v).match(/^(-?[\d.]+,\d+)\s*(.*)$/); if (!m) return v; const n = parseFloat(m[1].replace(/\./g, "").replace(",", ".")); return nf(n, Math.abs(n) >= 100 ? 1 : (Math.round(n * 10) === n * 10 ? 1 : 2)) + (m[2] === "%" ? "%" : " " + m[2]); };
  const periodoBreve = (p) => { const m = String(p).match(/^(\d{4})-(\d{2})$/); if (m) return MESI[+m[2] - 1] + " " + m[1]; const q = String(p).match(/^(\d{4})-Q(\d)$/); return q ? ["I", "II", "III", "IV"][+q[2] - 1] + " trim " + q[1] : p; };
  const del_ = (iso) => (/^(8|11) /.test(dataBreve(iso)) ? "dell'" : "del ") + dataBreve(iso);
  const ACC = { a: "à", e: "è", i: "ì", o: "ò", u: "ù" };
  const tit = (s) => String(s || "").replace(/"/g, "").replace(/([aeiou])'(?=[\s,.;:)]|$)/g, (m, v) => ACC[v]);
  const breveEResto = (s, max = 200) => { const x = piano(s); if (x.length <= max + 60) return esc(x); const frasi = x.split(/(?<=[.;])\s+/); let b = ""; while (frasi.length && (b + frasi[0]).length <= max) b += (b ? " " : "") + frasi.shift(); if (!b) b = frasi.shift(); return esc(b) + (frasi.length ? ` <details class="leggi"><summary>Leggi tutto</summary>${esc(frasi.join(" "))}</details>` : ""); };
  const icona = (n) => `<i data-lucide="${n}" aria-hidden="true"></i>`;

  if (!D) {
    main.innerHTML = `<div class="avviso alto" role="alert"><div class="avviso-titolo">${icona("triangle-alert")}Non riusciamo a caricare i dati.</div>
      <p>Il prototipo legge <code>../../docs/data.js</code>: avvia un server dalla cartella principale del repository (<code>python -m http.server 8791</code>) e apri <code>/design/prototipo/</code>.</p></div>`;
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
  const GRAVITA = { critica: ["critico", "octagon-x", "Critico"], alta: ["alto", "triangle-alert", "Alto"], media: ["attenzione", "circle-alert", "Attenzione"], bassa: ["", "circle-dashed", "Basso"], info: ["info", "info", "Info"] };

  const chip = ([cls, ic, testo], extra = "") => `<span class="chip ${cls} ${extra}">${icona(ic)}${esc(testo)}</span>`;
  const chipClasse = (c) => chip(CLASSE[c] || ["", "circle-dashed", c]);
  const misuratore = (v) => {
    if (!v) return `<span class="chip tratteggio">Non inclusa</span>`;
    const n = DOSE[v] ?? 0, nome = v.charAt(0) + v.slice(1).toLowerCase();
    return `<span class="misuratore" aria-label="Variante ${nome}, intensità ${n} su 3"><span aria-hidden="true">${nome}</span><span class="pallini" aria-hidden="true">${[1, 2, 3].map((i) => `<i class="${i <= n ? "pieno" : ""}"></i>`).join("")}</span></span>`;
  };
  const BADGE = { verificato: ["favorevole", "badge-check", "Verificato"], stima: ["info", "calculator", "Stima GovernAI"], verificare: ["attenzione", "circle-help", "Da verificare"], provvisorio: ["", "hourglass", "Provvisorio"] };
  const badge = (tipo, fonte) => { const [c, i, t] = BADGE[tipo]; return `<button type="button" class="badge ${c}" data-fonte="${esc(fonte)}" aria-haspopup="dialog">${icona(i)}<span>${t}</span></button>`; };
  const STIMA = "Stima GovernAI: calcolata dal modello, non certificata dalla Ragioneria generale dello Stato (RGS). Fonte: registro delle coperture e ottimizzatore del programma.";
  const md = (t) => window.marked && window.DOMPurify ? DOMPurify.sanitize(marked.parse(t || "")) : `<p>${esc(t)}</p>`;
  const proposta = (id) => D.proposte.find((p) => p.id === id);
  const scenario = (id) => D.scenari.find((s) => s.id === id) || D.scenari[0];
  const momento = scenario("momento");
  const linkP = (id) => `#/programma/${encodeURIComponent(id)}`;
  const linkSeduta = (id) => `#/governo/sedute/${encodeURIComponent(id)}`;
  const codici = (s) => String(s || "").replace(/\b(\d{2}-[PC]\d{1,2})\b/g, (m) => proposta(m) ? `<a href="${linkP(m)}">${m}</a>` : m);

  // Istantanea di europa/scadenze.csv dell'8/11/2026 (la sezione Europa non è ancora in data.js)
  const SCADENZE_UE = [
    { data: "2026-11-23", pr: "alta", breve: "Recupero e confisca dei beni", atto: "Direttiva (UE) 2024/1260", celex: "32024L1260", stato: "In termine, nessuna misura italiana notificata", proposte: ["07-C2", "07-C4"] },
    { data: "2026-11-30", pr: "info", breve: "Parere della Commissione sul documento programmatico di bilancio", atto: "Reg. (UE) n. 473/2013, art. 7", stato: "Semestre europeo", proposte: [] },
    { data: "2026-12-02", pr: "alta", breve: "Lavoro tramite piattaforme digitali", atto: "Direttiva (UE) 2024/2831", celex: "32024L2831", stato: "In termine, nessuna misura italiana notificata", proposte: [] },
    { data: "2026-12-31", pr: "alta", breve: "IVA nell'era digitale (ViDA)", atto: "Direttiva (UE) 2025/516", celex: "32025L0516", stato: "In termine, nessuna misura italiana notificata", proposte: ["01-P3", "01-P10"] },
  ];

  // ---------- lettura dei testi generati ----------
  function sezioni(testo) {
    const out = { _testa: "" };
    String(testo || "").split(/\n(?=## )/).forEach((blocco, i) => {
      if (i === 0 && !blocco.startsWith("## ")) { out._testa = blocco; return; }
      const nl = blocco.indexOf("\n");
      out[blocco.slice(3, nl < 0 ? undefined : nl).trim()] = nl < 0 ? "" : blocco.slice(nl + 1).trim();
    });
    return out;
  }
  function allerte() {
    const b = (D.bollettini || [])[0];
    if (!b) return [];
    const s = sezioni(b.testo)["3. Allerte attive"] || "";
    const out = [];
    s.split("\n").forEach((r) => {
      let m = r.trim().match(/^- \*\*([^*]+)\*\*: (.*?)\s*(?:\(valore (.+?), ([^,)]+)\))?$/);
      if (m) { out.push({ id: m[1], msg: m[2], valore: m[3], periodo: m[4], priorita: [], sospese: [] }); return; }
      const u = out[out.length - 1];
      if (!u) return;
      if ((m = r.match(/^\s+- Azione: (.*)/))) u.azione = m[1];
      if ((m = r.match(/^\s+- Priorità: (.*?); sospese: (.*)/))) {
        u.priorita = m[1].split(/,\s*/).filter((x) => x && x !== "—");
        u.sospese = m[2].split(/,\s*/).filter((x) => x && x !== "—");
      }
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
    const domanda = (dom.match(/\*\*Domanda:\*\*\s*([^\n]+)/) || [])[1];
    const motivo = (S._testa.match(/\*\*Motivo della convocazione\.\*\* (.*)/) || [])[1] || "";
    const ver = (D.governo.verifiche || []).find((x) => x.seduta === v.seduta);
    return {
      id: v.seduta, data: v.seduta.slice(0, 10), S, dec, deroghe, obiezioni, mandati, previsioni: prev ? +prev[1] : null,
      pareri: sotto(S["Pareri degli esperti"]), ministri: sotto(S["Posizioni dei ministri"]),
      tipo: motivo.startsWith("Richiesta") ? "Seduta a richiesta" : "Seduta per allerte",
      titolo: (ver && ver.titolo) || domTitolo || motivo, domanda, dom, motivo, verifica: ver,
      rilievi: (S["Rilievi formali"] || "").split("\n").filter((r) => r.startsWith("- ")).length,
    };
  }
  const VERBALI = (D.governo && D.governo.verbali || []).map(verbale);

  // ---------- componenti ----------
  function contatore(dec) {
    const n = (e) => dec.filter((d) => d.esito === e).length, a = n("adottata"), r = n("respinta"), v = n("rinviata"), t = dec.length || 1;
    return `<div class="contatore"><div class="barra" aria-hidden="true">
        <span style="width:${a / t * 100}%;background:var(--c-favorevole)"></span><span style="width:${r / t * 100}%;background:var(--c-alto)"></span><span style="width:${v / t * 100}%;background:var(--c-neutro)"></span></div>
      <div class="legenda"><span><b>${a}</b> adottate</span><span><b>${r}</b> respinte</span><span><b>${v}</b> ${v === 1 ? "rinviata" : "rinviate"}</span></div></div>`;
  }
  function cardProposta(p, motivo = "") {
    const m = momento.misure[p.id];
    return `<a class="card card-proposta" href="${linkP(p.id)}">
      <p class="etichetta">${esc(D.aree[p.area])} · ${esc(p.id)}</p>
      <h3 class="titolo-card">${esc(tit(p.titolo))}</h3>
      <div class="chips">${chipClasse(p.classe)}${p.linea_rossa ? chip(["critico", "octagon-x", "Linea rossa"]) : ""}</div>
      <div class="riga-dati">${misuratore(m && m.variante)}${m ? `<span>${nf(m.costo)} mld/anno</span>` : ""}${motivo ? `<span>${esc(motivo)}</span>` : ""}</div>
    </a>`;
  }
  function intestazioneIndice(voci, azioni) {
    return `<details class="indice-mobile"><summary>${icona("list")}In questa pagina</summary><ol>${voci.map(([id, t]) => `<li><a href="#${id}" data-ancora>${esc(t)}</a></li>`).join("")}</ol></details>`;
  }
  function indiceLaterale(voci, azioni) {
    return `<aside class="indice" aria-label="In questa pagina"><p class="etichetta">In questa pagina</p>
      <ol>${voci.map(([id, t]) => `<li><a href="#${id}" data-ancora>${esc(t)}</a></li>`).join("")}</ol>
      <div class="azioni">${azioni}</div></aside>`;
  }
  const azioniCondividi = `<button class="btn s" type="button" data-azione="copia">${icona("link-2")}Copia link permanente</button>
    <a class="btn terziario s" href="#/partecipa">${icona("flag-triangle-right")}Segnala un errore</a>`;
  const bannerSim = (piccolo) => `<div class="banner-sim ${piccolo ? "piccolo" : ""}" role="note">${icona("flask-conical")}<span><strong>Governo ombra · simulazione:</strong> le decisioni non sono in vigore.</span></div>`;

  // ---------- schermate ----------
  function home() {
    const n = D.numeri || {};
    const nucleo = D.proposte.filter((p) => p.classe === "robusta");
    const coperto = nucleo.filter((p) => momento.misure[p.id] && ["PIENA", "ESSENZIALE"].includes(momento.misure[p.id].variante)).length;
    const integra = D.integrita && !D.integrita.errori.length;
    const al = allerte();
    const ult = VERBALI[0];
    const mandato = (D.governo.mandati || []).filter((m) => m.stato === "aperto").sort((a, b) => a.scadenza.localeCompare(b.scadenza))[0];
    const oggi = new Date(D.generato.slice(0, 10) + "T12:00");
    const tra = (iso) => Math.round((new Date(iso + "T12:00") - oggi) / 864e5);
    const scad = [...SCADENZE_UE];
    if (mandato) scad.push({ data: mandato.scadenza, pr: "media", breve: `Mandato ${mandato.id} · area ${D.aree[mandato.area] || mandato.area}`, atto: piano(mandato.compito).slice(0, 110) + "…", stato: "Mandato aperto del governo ombra", proposte: [] });
    scad.sort((a, b) => a.data.localeCompare(b.data));
    const perArea = Object.keys(D.aree).map((k) => [k, D.aree[k], D.proposte.filter((p) => p.area === k).length]);
    const solide = [...nucleo].sort((a, b) => b.p_prima_meta - a.p_prima_meta).slice(0, 6);
    const gravAllerta = (id) => /calo/.test(id) ? GRAVITA.media : GRAVITA.alta;
    return `
      <section class="hero" aria-labelledby="titolo-home">
        <div>
          <p class="etichetta sopratitolo">Un programma di governo aperto, basato su dati e valori dichiarati</p>
          <h1 id="titolo-home">Governare con i dati,<br>scegliere con i valori.</h1>
          <p class="risposta">${n.proposte} proposte valutate su ${n.valori} valori, finanziate senza deficit e controllate su Costituzione e regole europee. <span class="firma">L'AI propone e verifica. Le persone decidono.</span></p>
          <div class="azioni"><a class="btn primario" href="#/programma">Esplora il programma ${icona("arrow-right")}</a><a class="btn" href="#/metodo">Come funziona</a></div>
        </div>
        <div class="oggi-box" aria-label="Oggi in breve">
          <p class="etichetta">Oggi, ${dataLunga(D.generato)}</p>
          <ul>
            <li>${icona("bell-ring")}${chip(GRAVITA.alta.slice(0, 2).concat(`${al.length} allerte attive`))}</li>
            <li>${icona("users-round")}<span>Ultima seduta: <a href="${linkSeduta(ult.id)}">${dataBreve(ult.data)}</a></span></li>
            <li>${icona("link-2")}${integra ? chip(["favorevole", "circle-check", `Catena integra · ${D.integrita.anelli} anelli`]) : chip(["critico", "octagon-x", "Catena da verificare"])}</li>
          </ul>
        </div>
      </section>

      <section class="sezione" aria-label="Il giorno in quattro numeri" style="margin-top:32px">
        <div class="griglia g2 g4-d">
          <div class="card kpi"><p class="etichetta">Programma del momento</p><p class="numero">${nf(momento.spesa)}<small>mld/anno</small></p><p class="nota">senza deficit</p>${badge("stima", STIMA)}</div>
          <div class="card kpi"><p class="etichetta">Misure incluse</p><p class="numero">${Object.keys(momento.misure).length}<small>su ${D.proposte.length}</small></p><p class="nota">nucleo robusto finanziato: ${coperto} su ${nucleo.length}</p>${badge("stima", STIMA)}</div>
          <div class="card kpi"><p class="etichetta">Cifre verificate</p><p class="numero">${n.cifre_verificate}</p><p class="nota">su fonte primaria</p>${badge("verificato", "334 cifre del programma controllate una per una sul documento o sulla serie ufficiale (cartella dati/verifiche).")}</div>
          <div class="card kpi"><p class="etichetta">Serie di dati</p><p class="numero">${n.serie}</p><p class="nota">aggiornate ogni giorno</p>${badge("verificato", "Eurostat, ISTAT, MEF/RGS, Banca d'Italia, UPB e documenti ufficiali, scaricati dalla sentinella quotidiana.")}</div>
        </div>
      </section>

      <div class="griglia g2-d sezione">
        <section aria-labelledby="t-allerte">
          <div class="sezione-testa"><h2 id="t-allerte">Allerte attive (${al.length})</h2><a href="#/dati">Tutte</a></div>
          ${al.length ? al.map((a) => {
            const g = gravAllerta(a.id);
            const [tit, ...resto] = a.msg.split(": ");
            return `<div class="avviso ${g[0]}"><div class="avviso-titolo">${chip(g)}<span>${esc(tit.replace(/\.$/, ""))}</span></div>
              ${a.valore ? `<p><strong>${esc(valoreBreve(a.valore))}</strong> · ${esc(periodoBreve(a.periodo))}${resto.length ? " · " + esc(resto.join(": ")) : ""}</p>` : ""}
              ${a.priorita.length ? `<div class="mini-codici">Diventano prioritarie: ${a.priorita.map((c) => `<a href="${linkP(c)}">${c}</a>`).join("")}</div>` : ""}
              ${a.sospese.length ? `<div class="mini-codici">Sospesa: ${a.sospese.map((c) => `<a href="${linkP(c)}">${c}</a>`).join("")}</div>` : ""}</div>`;
          }).join("") : `<div class="avviso favorevole"><div class="avviso-titolo">${icona("circle-check")}Nessuna allerta attiva: gli indicatori sono nelle soglie.</div></div>`}
        </section>
        <section aria-labelledby="t-seduta">
          <div class="sezione-testa"><h2 id="t-seduta">Ultima seduta del Consiglio</h2><a href="#/governo">Tutte</a></div>
          <div class="card seduta-card">
            ${bannerSim(true)}
            <p class="etichetta">${dataBreve(ult.data)} · ${esc(ult.tipo)}</p>
            <h3>${esc(ult.titolo)}</h3>
            ${contatore(ult.dec)}
            <p class="nota">${ult.dec.length} decisioni · ${ult.deroghe.length} deroghe dichiarate · ${ult.obiezioni.length} obiezioni dell'opposizione leale${ult.previsioni ? ` · ${ult.previsioni} previsioni registrate` : ""} · ${ult.mandati.length} mandati</p>
            <a class="btn" href="${linkSeduta(ult.id)}">Leggi la sintesi ${icona("arrow-right")}</a>
          </div>
        </section>
      </div>

      <section class="sezione" aria-labelledby="t-scadenze">
        <div class="sezione-testa"><h2 id="t-scadenze">Prossime scadenze</h2><a href="#/controlli">Tutte</a></div>
        <div class="card" style="padding-top:4px;padding-bottom:4px"><ul class="scadenze">${scad.map((s) => `<li>
          <span class="data">${dataBreve(s.data).split(" ").slice(0, 2).join(" ")}<small>tra ${tra(s.data)} giorni</small></span>
          <span class="testo"><span class="chips">${chip(GRAVITA[s.pr])}<strong>${esc(s.breve)}</strong></span>
            <span class="nota">${esc(s.atto)}${s.celex ? ` · <span class="mono">CELEX ${s.celex}</span>` : ""} · ${esc(s.stato)}</span>
            ${s.proposte.length ? `<span class="mini-codici">Collegata a: ${s.proposte.map((c) => `<a href="${linkP(c)}">${c}</a>`).join("")}</span>` : ""}</span></li>`).join("")}</ul></div>
        <p class="nota">Scadenze europee da <code>europa/scadenze.csv</code> (8/11/2026); la sezione Europa non è ancora nei dati del sito.</p>
      </section>

      <section class="sezione" aria-labelledby="t-temi">
        <div class="sezione-testa"><h2 id="t-temi">Le proposte per tema</h2></div>
        <div class="temi">${perArea.map(([k, nome, c]) => `<a href="#/programma?tema=${k}">${esc(nome)}<span>${c}</span></a>`).join("")}</div>
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
          <div class="card">${icona("octagon-x")}<div><h3>Linee rosse automatiche</h3><p>Le proposte che violano diritti o scaricano costi sui più deboli sono escluse da regole fisse.</p></div></div>
          <div class="card">${icona("repeat")}<div><h3>Tutto riproducibile</h3><p>Codice, dati, punteggi e regole sono pubblici: chiunque può rifare il calcolo.</p></div></div>
        </div>
      </section>

      <section class="sezione partecipa-box" aria-labelledby="t-partecipa">
        <div><h2 id="t-partecipa">Hai un'idea o una domanda?</h2><p>Chiunque può proporre. Serve un account GitHub gratuito; un membro del progetto legge ogni richiesta.</p></div>
        <a class="btn primario" href="#/partecipa">${icona("message-square-plus")}Proponi un'idea</a>
      </section>`;
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
    // governo ombra
    let dec = null, seduta = null, deroga = null;
    for (const v of VERBALI) { const d = v.dec.find((x) => x.id === p.id); if (d) { dec = d; seduta = v; deroga = v.deroghe.find((x) => x.id === p.id); break; } }
    const mandati = (D.governo.mandati || []).filter((x) => x.stato === "aperto" && x.compito.includes(p.id));
    const obiettivi = (D.obiettivi || []).filter((o) => o.proposta === p.id);
    const scadenze = SCADENZE_UE.filter((s) => s.proposte.includes(p.id));
    // valori
    const medie = p.punteggi ? D.valori.map((v, j) => ({ nome: v.nome, id: v.id, m: p.punteggi[j].reduce((a, b) => a + b, 0) / 3, min: Math.min(...p.punteggi[j]), max: Math.max(...p.punteggi[j]) })) : [];
    const nonZero = medie.filter((x) => Math.abs(x.m) >= 0.05).sort((a, b) => b.m - a.m), zero = medie.filter((x) => Math.abs(x.m) < 0.05);
    const giur = p.giuridico || [];
    const peggiore = giur.reduce((a, r) => (GRAVITA_GIUR[r.esito] ?? 0) > (GRAVITA_GIUR[a] ?? -1) ? r.esito : a, null);
    const voci = [["in-breve", "In breve"], ["valori", "Effetto sui valori"], ["varianti", "Varianti"], ["controlli", "Controlli"], ["obiettivi", "Obiettivi"], ["governo", "Governo ombra"], ["testo", "Testo completo"], ["fonti", "Fonti e metodo"]];
    const esitoDec = dec ? (deroga ? ["attenzione", "git-branch", "Adottata con deroga"] : ESITO_DEC[dec.esito] || ["", "circle-dashed", dec.esito]) : null;

    return `
      <nav class="briciole" aria-label="Briciole di pane"><a href="#/programma">Programma</a><span aria-hidden="true">›</span><a href="#/programma?tema=${p.area}">${esc(D.aree[p.area])}</a><span aria-hidden="true">›</span><span aria-current="page">${esc(p.id)}</span></nav>
      <div class="con-indice">
        <article>
          <header class="intestazione">
            <p class="etichetta">${esc(D.aree[p.area])} · ${esc(p.id)}</p>
            <h1>${esc(tit(p.titolo))}</h1>
            <div class="chips">${chipClasse(p.classe)}${p.linea_rossa ? chip(["critico", "octagon-x", "Linea rossa"]) : ""}${peggiore ? chip(ESITO_GIUR[peggiore]) : ""}</div>
            <div class="stato">Nel programma del momento: ${misuratore(m && m.variante)}${m ? `<span>· ${nf(m.costo)} mld/anno · robustezza ${Math.round(m.robustezza * 100)}%</span>` : `<span>· non inclusa</span>`}</div>
            ${intestazioneIndice(voci)}
          </header>
          ${p.linea_rossa ? `<div class="avviso critico" role="alert"><div class="avviso-titolo">${icona("octagon-x")}Linea rossa segnalata</div><p>Questa proposta viola almeno una linea rossa della Carta dei valori ed è esclusa automaticamente dal programma.</p></div>` : ""}

          <section class="card in-breve blocco" id="in-breve" aria-labelledby="h-breve" style="margin-top:0">
            <h2 id="h-breve" class="vh">In breve</h2>
            <h3>Il problema in un dato</h3>
            ${grande ? `<p class="dato-grande">${esc(grande)}</p>` : ""}
            <p class="testo-lettura">${esc(piano(problema))}</p>
            ${badge(fonteProb ? "verificato" : "verificare", fonteProb ? piano(fonteProb) : "La fonte non è indicata nel testo della scheda.")}
            <h3>La soluzione</h3>
            <p class="testo-lettura">${esc(piano(soluzione)) || esc(titoloLungo || "")}</p>
            <h3>Costo e chi paga</h3>
            <p>${m ? `<strong>${nf(m.costo)} mld/anno</strong> nella variante ${esc(m.variante.toLowerCase())}` : `Costo pieno ${nf(p.costo_pieno)} mld/anno; non inclusa nel programma del momento`} ${badge("stima", STIMA)}</p>
            <h3>Il governo ombra</h3>
            ${dec ? `${bannerSim(true)}<p>${chip(esitoDec)} in variante ${esc(dec.variante.toLowerCase())} nella seduta <a href="${linkSeduta(seduta.id)}">«${esc(seduta.titolo)}»</a> (${dataBreve(seduta.data)}).</p>
              ${deroga ? `<p class="nota">${esc(piano(deroga.testo))}</p>` : ""}
              ${mandati.length ? `<p>${mandati.map((x) => `Mandato <strong class="mono">${x.id}</strong> entro il ${dataBreve(x.scadenza)}`).join(" · ")}</p>` : ""}`
              : `<p class="nota">Non ancora all'ordine del giorno del Consiglio.</p>`}
          </section>

          <section class="blocco" id="valori" aria-labelledby="h-valori">
            <h2 id="h-valori">Effetto sui 10 valori <small>mediana del panel indipendente, media di breve, medio e lungo periodo, da −3 a +3</small></h2>
            ${medie.length ? `<div class="valori" role="img" aria-label="Effetto sui valori: ${nonZero.map((x) => `${x.nome} ${x.m > 0 ? "+" : ""}${nf(x.m, 1)}`).join("; ")}${zero.length ? `; ${zero.length} valori a zero` : ""}.">
                <span aria-hidden="true"></span><div class="asse-testa" aria-hidden="true"><span>−3 peggiora</span><span>0</span><span>migliora +3</span></div><span aria-hidden="true"></span>
                ${nonZero.map((x) => `<span>${esc(x.nome)}</span><div class="traccia" title="breve, medio, lungo: ${p.punteggi[D.valori.findIndex((v) => v.id === x.id)].join(", ")}"><span class="${x.m >= 0 ? "pos" : "neg"}" style="width:${Math.abs(x.m) / 3 * 50}%"></span></div><span class="num">${x.m > 0 ? "+" : "−"}${nf(Math.abs(x.m), 1)}</span>`).join("")}
                ${zero.length ? `<p class="zero">A zero: ${zero.map((x) => esc(x.nome)).join(", ")}.</p>` : ""}
              </div>
              <p class="nota">Prima metà della classifica nel ${Math.round(p.p_prima_meta * 100)}% delle combinazioni di pesi; posizione tra ${p.rango[0]}ª e ${p.rango[1]}ª.${p.trainanti ? ` Sale se si dà più peso a: ${esc(p.trainanti)}.` : ""}</p>`
              : `<p class="vuoto">Il panel non ha ancora valutato questa proposta.</p>`}
          </section>

          <section class="blocco" id="varianti" aria-labelledby="h-varianti">
            <h2 id="h-varianti">Varianti <small>la dose della misura, non un giudizio</small></h2>
            <div class="varianti">${p.varianti.map((v) => `<div class="variante ${m && m.variante === v.variante ? "scelta" : ""}">
              ${misuratore(v.variante)} ${m && m.variante === v.variante ? chip(["info", "check", "Nel programma"]) : ""}
              <p class="costo">${nf(v.costo)} mld/anno</p><p>${esc(v.descrizione)}</p><p class="nota">Strumento: ${esc(v.strumento || "—")}</p></div>`).join("")}</div>
          </section>

          <section class="blocco" id="controlli" aria-labelledby="h-controlli">
            <h2 id="h-controlli">Controlli <small>fiscale, costituzionale, europeo</small></h2>
            ${giur.length ? `<div class="card" style="padding-top:4px;padding-bottom:4px">${giur.map((r) => `<details class="controllo">
                <summary><span class="ambito">${esc(AMBITO[r.ambito] || r.ambito)}${r.tipo === "variante" ? ` · variante ${esc((r.id.split(":")[1] || "").toLowerCase())}` : ""}<small>${esc(r.norme.slice(0, 90))}${r.norme.length > 90 ? "…" : ""}</small></span>${chip(ESITO_GIUR[r.esito] || ["", "circle-dashed", r.esito])}<span class="freccia">${icona("chevron-down")}</span></summary>
                <div class="corpo"><p><strong>Norme:</strong> ${esc(r.norme)}</p><p>${esc(r.motivazione)}</p>${r.condizioni ? `<p><strong>Condizioni:</strong> ${esc(r.condizioni)}</p>` : ""}
                  <p>${String(r.fonti || "").split(/[\s;,]+/).filter((u) => /^https?:/.test(u)).map((u, i) => `<a href="${esc(u)}" target="_blank" rel="noopener">Fonte ${i + 1}<span class="vh"> (si apre in una nuova scheda)</span> ${icona("external-link")}</a>`).join(" · ")}</p></div></details>`).join("")}</div>`
              : `<p>${chip(["", "circle-dashed", "Non valutato"])} La verifica giuridica non è ancora disponibile.</p>`}
            ${scadenze.map((s) => `<div class="avviso attenzione" style="margin-top:12px"><div class="avviso-titolo">${icona("calendar")}Scadenza europea collegata: ${dataBreve(s.data)}</div><p>${esc(s.breve)} · ${esc(s.atto)} · ${esc(s.stato)}</p></div>`).join("")}
          </section>

          <section class="blocco" id="obiettivi" aria-labelledby="h-obiettivi">
            <h2 id="h-obiettivi">Obiettivi misurabili</h2>
            ${obiettivi.length ? `<table class="tabella a-card"><thead><tr><th>Obiettivo</th><th class="num">Base</th><th class="num">Ultimo</th><th class="num">Traguardo</th><th>Stato</th></tr></thead><tbody>
              ${obiettivi.map((o) => `<tr><td>${esc(o.nome)} <span class="nota">${esc(o.unita || "")}</span></td><td class="num" data-etichetta="Base">${nf(o.base, 1)}${o.periodo_base ? ` <span class="nota">(${esc(o.periodo_base)})</span>` : ""}</td><td class="num" data-etichetta="Ultimo">${nf(o.ultimo, 1)}</td><td class="num" data-etichetta="Traguardo">${nf(o.obiettivo, 1)}</td>
                <td data-etichetta="Stato">${o.stato === "manuale" ? chip(["", "pencil-ruler", "Si misura a mano"]) : chip(["info", "eye", o.stato])}</td></tr>`).join("")}</tbody></table>`
              : `<p class="vuoto">Obiettivi non ancora definiti per questa proposta.</p>`}
          </section>

          <section class="blocco" id="governo" aria-labelledby="h-governo">
            <h2 id="h-governo">Che cosa ha deciso il governo ombra</h2>
            ${dec ? `${bannerSim()}<div class="card decisione"><p class="etichetta">${dataBreve(seduta.data)} · ${esc(seduta.tipo)}</p>
                <div class="testa">${misuratore(dec.variante)}${chip(ESITO_DEC[dec.esito] || ["", "circle-dashed", dec.esito])}<span class="nota">Regola: ${esc(dec.regola)}</span></div>
                <p class="motivo">${esc(piano(dec.motivo))}</p>
                ${deroga ? `<div class="deroga" style="margin-top:12px"><p class="etichetta">Deroga dall'esito del motore</p>${esc(piano(deroga.testo))}</div>` : ""}
                <p><a href="${linkSeduta(seduta.id)}">Apri il verbale della seduta ${icona("arrow-right")}</a></p></div>
                ${mandati.map((x) => `<div class="avviso" style="margin-top:12px"><div class="avviso-titolo">${icona("clipboard-check")}Mandato ${x.id} · entro il ${dataBreve(x.scadenza)}</div><p>${codici(esc(x.compito))}</p></div>`).join("")}`
              : `<p class="vuoto">Non ancora all'ordine del giorno del Consiglio.</p>`}
          </section>

          <section class="blocco" id="testo" aria-labelledby="h-testo">
            <h2 id="h-testo" class="vh">Testo completo</h2>
            <details class="richiudibile" data-md="scheda"><summary>${icona("scroll-text")}Testo completo <span class="conta">articolato normativo, cronoprogramma, indicatori</span><span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo md"></div></details>
          </section>
          <section class="blocco" id="fonti" aria-labelledby="h-fonti" style="margin-top:12px">
            <h2 id="h-fonti" class="vh">Fonti e metodo</h2>
            <details class="richiudibile"><summary>${icona("book-open")}Fonti e metodo<span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo">
              <p>Punteggi assegnati da un panel di ${D.valutatori.length} valutatori indipendenti (${esc(D.valutatori.join(", "))}) che non hanno scritto le proposte. Classe calcolata provando migliaia di combinazioni di pesi tra i 10 valori.</p>
              <p>Costi: stime GovernAI, non certificate dalla Ragioneria generale dello Stato.</p>
              <p>Dati ${del_(D.generato)} · anello n. ${D.integrita.ultimi[0].n} della catena di integrità · impronta <span class="impronta">${esc(D.integrita.ultimi[0].hash)}</span></p></div></details>
          </section>
          <div class="azioni" style="margin-top:24px">${azioniCondividi}</div>
        </article>
        ${indiceLaterale(voci, azioniCondividi)}
      </div>`;
  }

  function schedaSeduta(id) {
    const v = VERBALI.find((x) => x.id === id);
    if (!v) return nonTrovato(`Nessuna seduta «${id}».`);
    const ver = v.verifica;
    const risposta = v.S["Risposta del Consiglio"] || "";
    const indirizzo = v.S["Indirizzo del capo di governo"] || "";
    const breve = (indirizzo || risposta).split(/(?<=\.)\s/).slice(0, 2).join(" ");
    const voci = [["domanda", "La domanda"], ["risposta", "La risposta"], ["decisioni", `Decisioni (${v.dec.length})`], ["deroghe", `Deroghe (${v.deroghe.length})`], ["obiezioni", `Obiezioni (${v.obiezioni.length})`], ["pareri", `Pareri (${v.pareri.length})`], ["ministri", `Ministri (${v.ministri.length})`], ["mandati", `Mandati (${v.mandati.length})`]];
    const altri = VERBALI.filter((x) => x !== v);
    const filtri = [["tutte", `Tutte ${v.dec.length}`], ...["adottata", "respinta", "rinviata"].map((e) => [e, `${ESITO_DEC[e][2].replace(/a$/, "e")} ${v.dec.filter((d) => d.esito === e).length}`])];
    return `
      ${bannerSim()}
      <nav class="briciole" aria-label="Briciole di pane"><a href="#/governo">Governo</a><span aria-hidden="true">›</span><a href="#/governo">Sedute</a><span aria-hidden="true">›</span><span aria-current="page">${dataBreve(v.data)}</span></nav>
      <div class="con-indice">
        <article>
          <header class="intestazione">
            <p class="etichetta">${esc(v.tipo)} · ${dataLunga(v.data)}</p>
            <h1>${esc(v.titolo)}</h1>
            <div class="chips">${ver ? chip(ver.esito === "confermata" ? ["favorevole", "circle-check", `Confermata dalla verifica ${del_(ver.verificata)}`] : ["attenzione", "refresh-ccw", "Da riesaminare"]) : chip(["", "circle-dashed", "Non ancora verificata"])}</div>
            <ol class="percorso" aria-label="Come si è svolta la seduta">
              <li><a href="#pareri"><b>Esperti</b><span>${v.pareri.length} pareri, scritti da soli</span></a></li>
              <li><a href="#ministri"><b>Ministri</b><span>${v.ministri.length} posizioni</span></a></li>
              <li><a href="#obiezioni"><b>Opposizione leale</b><span>${v.obiezioni.length} obiezioni</span></a></li>
              <li><a href="#decisioni"><b>Capo di governo</b><span>${v.dec.length} decisioni</span></a></li>
            </ol>
            ${intestazioneIndice(voci)}
          </header>

          <section class="blocco" id="domanda" aria-labelledby="h-domanda" style="margin-top:8px">
            <h2 id="h-domanda">La domanda</h2>
            ${v.domanda ? `<blockquote class="citazione">${esc(v.domanda)}</blockquote>
              <details class="richiudibile" data-md-testo="${esc(v.dom.replace(/^# .*\n/, ""))}"><summary>Perché ora e vincoli<span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo md"></div></details>`
              : `<blockquote class="citazione">${esc(v.motivo)}</blockquote><p class="nota">Seduta convocata automaticamente dalle allerte: non c'è una domanda scritta.</p>`}
          </section>

          <section class="blocco" id="risposta" aria-labelledby="h-risposta">
            <h2 id="h-risposta">La risposta in breve</h2>
            <p class="testo-lettura">${esc(piano(breve))}</p>
            ${risposta ? `<details class="richiudibile" data-md-testo="${esc(risposta)}"><summary>Risposta completa del Consiglio<span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo md"></div></details>` : ""}
            ${indirizzo ? `<details class="richiudibile" data-md-testo="${esc(indirizzo)}"><summary>Indirizzo del capo di governo<span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo md"></div></details>` : ""}
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
                <dt>Risposta del capo</dt><dd>${o.risposta && o.risposta !== "—" ? esc(piano(o.risposta)) : `${chip(["attenzione", "circle-alert", "Non registrata"])} <span class="nota">La regola 7 chiede una risposta scritta: nel verbale manca. Vedi la motivazione della decisione collegata.</span>`}</dd></dl></div>`).join("")}</div>`
              : `<p class="nota">L'opposizione leale non ha sollevato obiezioni in questa seduta.</p>`}
          </section>

          <section class="blocco" id="pareri" aria-labelledby="h-pareri">
            <h2 id="h-pareri">Pareri degli esperti <small>${v.pareri.length}</small></h2>
            ${v.pareri.map((x, i) => `<details class="richiudibile" data-sez="pareri" data-i="${i}"><summary>${icona("graduation-cap")}${esc(x.titolo)}<span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo md"></div></details>`).join("")}
          </section>
          <section class="blocco" id="ministri" aria-labelledby="h-ministri">
            <h2 id="h-ministri">Posizioni dei ministri <small>${v.ministri.length}</small></h2>
            ${v.ministri.map((x, i) => `<details class="richiudibile" data-sez="ministri" data-i="${i}"><summary>${icona("user-round")}${esc(x.titolo)}<span class="freccia">${icona("chevron-down")}</span></summary><div class="corpo md"></div></details>`).join("")}
          </section>

          <section class="blocco" id="mandati" aria-labelledby="h-mandati">
            <h2 id="h-mandati">Mandati <small>compiti con scadenza affidati ai ministri</small></h2>
            ${v.mandati.length ? `<ul class="mandati">${v.mandati.map((x) => `<li><b>${x.id}</b> · ${esc(x.chi)} · entro il ${dataBreve(x.scadenza)}<br>${codici(esc(x.compito))}</li>`).join("")}</ul>` : `<p class="nota">Nessun mandato in questa seduta.</p>`}
            ${v.previsioni ? `<p class="nota" style="margin-top:12px">${icona("target")} ${v.previsioni} previsioni registrate, verificate alla scadenza con i dati ufficiali.</p>` : ""}
            ${v.rilievi ? `<p class="nota">${v.rilievi} rilievo formale annotato dal sistema.</p>` : ""}
            <p class="nota">Registrato nella catena di integrità · anello n. ${D.integrita.ultimi[0].n} · <span class="impronta">${esc(D.integrita.ultimi[0].hash.slice(0, 16))}…</span></p>
          </section>
          ${altri.length ? `<section class="blocco"><h2>Altre sedute</h2>${altri.map((x) => `<a class="card" href="${linkSeduta(x.id)}" style="margin-top:12px"><p class="etichetta">${dataBreve(x.data)} · ${esc(x.tipo)}</p><h3 class="titolo-card">${esc(x.titolo)}</h3>${contatore(x.dec)}</a>`).join("")}</section>` : ""}
          <div class="azioni" style="margin-top:24px">${azioniCondividi}</div>
        </article>
        ${indiceLaterale(voci, azioniCondividi + `<a class="btn s" href="#/partecipa">${icona("refresh-ccw")}Chiedi un riesame</a><span class="nota">Riesame: membri del progetto</span>`)}
      </div>`;
  }

  function elenco(params) {
    const tema = params.get("tema"), classe = params.get("classe");
    const lista = D.proposte.filter((p) => (!tema || p.area === tema) && (!classe || p.classe === classe));
    return `<h1>Programma</h1>
      <p class="risposta">${Object.keys(momento.misure).length} misure su ${D.proposte.length} nel programma del momento: ${nf(momento.spesa)} mld l'anno, senza deficit.</p>
      <div class="avviso" style="margin:16px 0 24px"><div class="avviso-titolo">${icona("info")}Elenco semplificato</div><p>Il prototipo valida solo home, scheda della proposta e verbale. Filtri, scenari e tabella sono descritti in <code>design/03_schermate.md</code> §2.</p></div>
      <p class="etichetta">${tema ? esc(D.aree[tema]) : classe ? "Nucleo robusto" : "Tutte le proposte"} · ${lista.length}</p>
      <div class="proposte-lista">${lista.map((p) => cardProposta(p)).join("")}</div>`;
  }
  function governo() {
    return `${bannerSim()}<h1>Governo</h1><p class="risposta">Il governo ombra si è riunito ${VERBALI.length} volte: ${VERBALI.reduce((a, v) => a + v.dec.length, 0)} decisioni, ${(D.governo.mandati || []).filter((m) => m.stato === "aperto").length} mandati aperti.</p>
      ${VERBALI.map((x) => `<a class="card" href="${linkSeduta(x.id)}" style="margin-top:16px"><p class="etichetta">${dataBreve(x.data)} · ${esc(x.tipo)}</p><h3 class="titolo-card">${esc(x.titolo)}</h3>${contatore(x.dec)}</a>`).join("")}`;
  }
  function segnaposto(nome) {
    return `<div class="vuoto">${icona("layout-template")}<h1 style="font-size:28px;margin-top:12px">${esc(nome)}</h1>
      <p>Questa schermata non fa parte del prototipo. È specificata in <code>design/03_schermate.md</code>.</p>
      <div class="azioni" style="justify-content:center"><a class="btn primario" href="#/">Torna a Oggi</a><a class="btn" href="${linkP("01-P3")}">Esempio di scheda</a><a class="btn" href="${linkSeduta(VERBALI[0].id)}">Esempio di verbale</a></div></div>`;
  }
  function nonTrovato(msg) { return `<div class="vuoto">${icona("search-x")}<h1 style="font-size:28px;margin-top:12px">Pagina non trovata</h1><p>${esc(msg)}</p><a class="btn primario" href="#/">Torna a Oggi</a></div>`; }

  // ---------- instradamento ----------
  function vista() {
    const [percorso, query] = (location.hash.slice(1) || "/").split("?");
    const parti = percorso.split("/").filter(Boolean).map(decodeURIComponent);
    const params = new URLSearchParams(query || "");
    let html, voce = parti[0] || "oggi", titolo = "Oggi";
    if (!parti.length) html = home();
    else if (parti[0] === "programma" && parti[1]) { html = schedaProposta(parti[1]); titolo = (proposta(parti[1]) || {}).titolo || "Proposta"; }
    else if (parti[0] === "programma") { html = elenco(params); titolo = "Programma"; }
    else if (parti[0] === "governo" && parti[1] === "sedute" && parti[2]) { html = schedaSeduta(parti[2]); titolo = "Seduta " + del_(parti[2]); }
    else if (parti[0] === "governo") { html = governo(); titolo = "Governo"; }
    else { const nomi = { dati: "Dati", controlli: "Controlli", metodo: "Metodo", partecipa: "Partecipa", cerca: "Cerca" }; titolo = nomi[parti[0]] || "Pagina"; html = segnaposto(titolo); }
    main.innerHTML = html;
    document.title = `${titolo} · GovernAI (prototipo)`;
    $$("[data-voce]").forEach((a) => { if (a.dataset.voce === voce) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current"); });
    if (window.lucide) lucide.createIcons();
    osservaIndice();
  }

  // contenuti richiusi: si generano solo all'apertura (i verbali superano le 300 mila battute)
  main.addEventListener("toggle", (e) => {
    const d = e.target;
    if (!(d instanceof HTMLDetailsElement) || !d.open) return;
    const corpo = $(":scope > .corpo", d);
    if (!corpo || corpo.dataset.pronto) return;
    if (d.dataset.md === "scheda") { const p = proposta(decodeURIComponent(location.hash.split("/")[2] || "")); corpo.innerHTML = md((p.scheda || "").replace(/^## .*\n/, "")); }
    else if (d.dataset.mdTesto != null) corpo.innerHTML = md(d.dataset.mdTesto);
    else if (d.dataset.sez) { const v = VERBALI.find((x) => x.id === decodeURIComponent(location.hash.split("/")[3] || "")); corpo.innerHTML = md(v[d.dataset.sez][+d.dataset.i].testo); }
    corpo.dataset.pronto = "1";
  }, true);

  // popover delle fonti, filtri, azioni
  let pop = null;
  const chiudiPop = () => { if (pop) { pop.remove(); pop = null; } };
  document.addEventListener("click", (e) => {
    const b = e.target.closest("[data-fonte]");
    if (b) {
      e.preventDefault(); const gia = pop && pop._da === b; chiudiPop(); if (gia) return;
      pop = document.createElement("div"); pop._da = b; pop.className = "popover"; pop.setAttribute("role", "dialog"); pop.setAttribute("aria-label", "Da dove viene questo numero");
      pop.innerHTML = `<strong>Da dove viene questo numero</strong>${esc(b.dataset.fonte)}`;
      document.body.appendChild(pop);
      const r = b.getBoundingClientRect(), w = Math.min(320, innerWidth - 32);
      pop.style.width = w + "px"; pop.style.left = Math.max(16, Math.min(r.left + scrollX, innerWidth - w - 16)) + "px"; pop.style.top = (r.bottom + scrollY + 6) + "px";
      b.setAttribute("aria-expanded", "true"); return;
    }
    if (pop && !e.target.closest(".popover")) chiudiPop();
    const f = e.target.closest("[data-filtro]");
    if (f) {
      $$("[data-filtro]").forEach((x) => x.setAttribute("aria-pressed", x === f));
      const tutte = f.dataset.filtro === "tutte"; let n = 0;
      $$(".decisioni > li").forEach((li) => { const ok = tutte || li.dataset.esito === f.dataset.filtro; li.hidden = !ok || (tutte && li.hasAttribute("data-oltre") && !main.dataset.tutte); if (!li.hidden) n++; });
      const altre = $(".altre"); if (altre) altre.hidden = !tutte || !!main.dataset.tutte;
      $("#esito-filtro").textContent = `${n} decisioni mostrate`;
    }
    const a = e.target.closest("[data-azione]");
    if (!a) return;
    if (a.dataset.azione === "altre") { main.dataset.tutte = "1"; $$(".decisioni > li[data-oltre]").forEach((li) => li.hidden = false); a.closest(".altre").hidden = true; }
    if (a.dataset.azione === "tema") {
      e.preventDefault();
      const scuro = document.documentElement.dataset.tema ? document.documentElement.dataset.tema === "scuro" : matchMedia("(prefers-color-scheme: dark)").matches;
      document.documentElement.dataset.tema = scuro ? "chiaro" : "scuro";
      try { localStorage.setItem("governai-tema", document.documentElement.dataset.tema); } catch (err) { /* memoria non disponibile */ }
    }
    if (a.dataset.azione === "copia") { try { navigator.clipboard.writeText(location.href); } catch (err) { /* nessun appunti */ } a.lastChild.textContent = "Link copiato"; }
    if (a.dataset.azione === "cerca") location.hash = "#/cerca";
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") chiudiPop();
    if (e.key === "/" && !/input|textarea/i.test(document.activeElement.tagName)) { e.preventDefault(); location.hash = "#/cerca"; }
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

  $("#aggiornato").textContent = `Dati aggiornati al ${dataLunga(D.generato)}, ore ${D.generato.slice(11, 16)}.`;
  window.addEventListener("hashchange", () => { chiudiPop(); delete main.dataset.tutte; vista(); window.scrollTo(0, 0); main.focus({ preventScroll: true }); });
  window.addEventListener("load", () => { if (window.lucide) lucide.createIcons(); });
  vista();
})();
