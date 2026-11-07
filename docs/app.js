/* GovernAI — interfaccia web. Legge window.GOVERNAI (data.js, generato da sistema/esporta_web.py). */
(function () {
  "use strict";

  const D = window.GOVERNAI;
  const $ = (s, el = document) => el.querySelector(s);
  const main = $("#contenuto");
  const nf = (n, d = 2) => n == null ? "—" : Number(n).toLocaleString("it-IT", { minimumFractionDigits: d, maximumFractionDigits: d });
  const pct = (x) => x == null ? "—" : Math.round(x * 100) + "%";
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const NOME_CLASSE = { "robusta": "Nucleo robusto", "dipendente dai valori": "Dipende dai valori", "in coda": "In coda", "sfavorevole": "Sfavorevole" };
  const CSS_CLASSE = { "robusta": "robusta", "dipendente dai valori": "valori", "in coda": "coda", "sfavorevole": "sfavorevole" };
  const ORIZZ = ["breve", "medio", "lungo"];
  const stato = { scenario: "momento", area: "", classe: "", cerca: "", soloIncluse: false, bollettino: null, documento: "programma", analisi: null };

  if (!D) {
    main.innerHTML = '<p class="vuoto">Dati non trovati: esegui <code>python sistema/esporta_web.py</code> per generare <code>docs/data.js</code>.</p>';
    return;
  }

  // ---------- utilità ----------
  function md(testo) {
    if (window.marked && window.DOMPurify) {
      const html = DOMPurify.sanitize(marked.parse(testo || ""));
      return html.replace(/<table>/g, '<div class="tabella-md"><table>').replace(/<\/table>/g, "</table></div>");
    }
    return "<pre>" + esc(testo) + "</pre>";
  }
  const chipClasse = (c) => `<span class="chip ${CSS_CLASSE[c] || ""}">${esc(NOME_CLASSE[c] || c)}</span>`;
  const chipVariante = (v) => v ? `<span class="chip var-${esc(v)}">${esc(v.charAt(0) + v.slice(1).toLowerCase())}</span>` : '<span class="chip var-esclusa">non inclusa</span>';
  const proposta = (id) => D.proposte.find((p) => p.id === id);
  const scenario = (id) => D.scenari.find((s) => s.id === id) || D.scenari[0];
  const valoreNome = (id) => (D.valori.find((v) => v.id === id) || {}).nome || id;

  function sparkline(serie) {
    if (!serie || !serie.v || serie.v.length < 2) return "";
    const v = serie.v.filter((x) => x != null);
    const min = Math.min(...v), max = Math.max(...v), span = max - min || 1, n = serie.v.length;
    const pts = serie.v.map((y, i) => [i / (n - 1) * 200, 38 - ((y - min) / span) * 34]);
    const d = pts.map((p, i) => (i ? "L" : "M") + p[0].toFixed(1) + " " + p[1].toFixed(1)).join(" ");
    const u = pts[pts.length - 1];
    return `<svg class="sparkline" viewBox="0 0 200 42" preserveAspectRatio="none" role="img" aria-label="Andamento dal ${esc(serie.t[0])} al ${esc(serie.t[n - 1])}"><path d="${d}" vector-effect="non-scaling-stroke"/><circle cx="${u[0]}" cy="${u[1]}" r="2.5"/></svg>`;
  }

  function variazione(i, campo, etichetta) {
    const d = i[campo];
    if (d == null) return "";
    const buona = i.meglio === "su" ? d > 0 : i.meglio === "giu" ? d < 0 : null;
    const cls = d === 0 || buona == null ? "" : buona ? "buona" : "cattiva";
    const freccia = d > 0 ? "▲" : d < 0 ? "▼" : "■";
    return `<span class="var ${cls}">${freccia} ${d > 0 ? "+" : ""}${nf(d)} ${etichetta}</span>`;
  }

  function apriCassetto(html) {
    $("#cassetto-corpo").innerHTML = html;
    const c = $("#cassetto");
    c.classList.add("aperto");
    c.setAttribute("aria-hidden", "false");
    $(".chiudi", c).focus();
  }
  function chiudiCassetto() {
    const c = $("#cassetto");
    c.classList.remove("aperto");
    c.setAttribute("aria-hidden", "true");
  }
  document.addEventListener("click", (e) => { if (e.target.closest("[data-chiudi]")) chiudiCassetto(); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") chiudiCassetto(); });

  // ---------- scheda di una proposta ----------
  function mostraProposta(id) {
    const p = proposta(id);
    if (!p) return;
    const s = scenario(stato.scenario);
    const scelta = s.misure[id];
    const barre = p.punteggi ? D.valori.map((v, j) => {
      const media = p.punteggi[j].reduce((a, b) => a + b, 0) / 3;
      const w = Math.abs(media) / 3 * 50;
      const stile = media >= 0 ? `left:50%;width:${w}%;background:var(--buono)` : `left:${50 - w}%;width:${w}%;background:var(--cattivo)`;
      return `<span>${esc(v.nome)}</span><div class="asse" title="breve ${p.punteggi[j][0]}, medio ${p.punteggi[j][1]}, lungo ${p.punteggi[j][2]}"><span style="${stile}"></span></div><span class="num">${media > 0 ? "+" : ""}${nf(media, 1)}</span>`;
    }).join("") : "";
    const varianti = p.varianti.map((v) => `<tr${scelta && scelta.variante === v.variante ? ' style="font-weight:600"' : ""}><td>${chipVariante(v.variante)}</td><td class="num">${nf(v.costo)}</td><td class="num">${nf(v.intensita, 2)}</td><td>${esc(v.descrizione)}</td></tr>`).join("");
    apriCassetto(`
      <p style="margin:0 0 4px;color:var(--tenue)">${esc(p.id)} · ${esc(D.aree[p.area])}</p>
      <h2 id="cassetto-titolo" style="font-size:1.35rem">${esc(p.titolo)}</h2>
      <p>${chipClasse(p.classe)} ${p.linea_rossa ? '<span class="chip rossa">Linea rossa segnalata</span>' : ""}
        &nbsp;Nello scenario «${esc(s.nome)}»: ${chipVariante(scelta && scelta.variante)} ${scelta ? nf(scelta.costo) + " mld/anno" : ""}</p>
      <p style="color:var(--tenue);font-size:.9rem">Prima metà della classifica nel ${pct(p.p_prima_meta)} delle combinazioni di pesi; posizione tra ${p.rango[0]}ª e ${p.rango[1]}ª.
        ${p.trainanti ? "Sale se si dà più peso a: <strong>" + esc(p.trainanti) + "</strong>." : ""}</p>
      <h3>Effetto sui valori <small style="color:var(--tenue);font-weight:400">(mediana del panel, media dei tre orizzonti, da −3 a +3)</small></h3>
      <div class="valori-barre">${barre}</div>
      <h3 style="margin-top:18px">Varianti</h3>
      <div class="tabella-box"><table><thead><tr><th>Variante</th><th class="num">Costo</th><th class="num">Intensità</th><th>Descrizione</th></tr></thead><tbody>${varianti}</tbody></table></div>
      <div class="md" style="margin-top:18px">${md(p.scheda.replace(/^## .*\n/, "### Scheda pronta\n"))}</div>`);
  }

  // Le richieste sono file in analisi/richieste/: GitHub apre l'editor con il modello già compilato
  const MODELLO_RICHIESTA = [
    "# Titolo del problema", "",
    "### Problema", "Che cosa non funziona? Se puoi, indica dati o esempi concreti.", "",
    "### Obiettivo", "Che cosa vorresti ottenere, e in quanto tempo?", "",
    "### Area principale", "",
    "### Vincoli o attenzioni", "",
  ].join(String.fromCharCode(10));
  const linkAnalisi = () => {
    if (!D.repo) return "#analisi";
    const nome = new Date().toISOString().slice(0, 10) + "-nuova-richiesta.md";
    return `${D.repo}/new/main/analisi/richieste?filename=${encodeURIComponent(nome)}&value=${encodeURIComponent(MODELLO_RICHIESTA)}`;
  };

  // ---------- viste ----------
  const viste = {
    racconto() {
      const n = D.numeri || {};
      const s = scenario("momento");
      const integra = D.integrita && !D.integrita.errori.length;
      const passi = [
        ["Dati ufficiali, ogni giorno", "Una sentinella controlla Eurostat, ISTAT, MEF, Banca d'Italia, UPB e altre fonti. Scarica solo ciò che è cambiato e ne conserva la storia."],
        ["Valori dichiarati", `Una Carta di ${n.valori || 10} valori, dal rispetto delle diversità alla responsabilità verso il futuro. Nessuna etichetta di destra o di sinistra.`],
        ["Panel indipendente", "Tre valutatori, che non hanno scritto le proposte, danno il punteggio a ogni misura su ogni valore. Il loro disaccordo diventa incertezza dichiarata."],
        ["Robustezza, non un peso unico", "Il motore prova migliaia di combinazioni di pesi e separa ciò che conviene a tutti da ciò che è una scelta politica."],
        ["Senza deficit", "Ogni misura preleva da coperture concrete e verificate: un registro unico impedisce di contare due volte gli stessi soldi."],
        ["Impara dai risultati", "Ogni misura ha obiettivi misurabili. Il sistema ne segue gli indicatori e, quando le misure rendono meno o più del previsto, ricalibra le scelte."],
        ["Verificabile come una blockchain", "Ogni esecuzione aggiunge un anello a una catena di impronte crittografiche: una modifica nascosta a dati, regole o risultati si vede subito."],
      ];
      return `
        <section class="hero">
          <p class="sopratitolo">Un modello decisionale aperto, basato su competenze e dati</p>
          <h1>Governare con i dati,<br>scegliere con i valori.</h1>
          <p class="lead">GovernAI è un prototipo: agenti di intelligenza artificiale analizzano i problemi del Paese, propongono opzioni con costi e coperture e rendono espliciti i compromessi. <strong>Le decisioni restano alle persone.</strong></p>
          <div class="azioni">
            <a class="bottone primario" href="${esc(linkAnalisi())}" target="_blank" rel="noopener">Avvia un'analisi</a>
            <a class="bottone" href="#programma">Esplora il programma</a>
            <a class="bottone" href="#valori">Prova i tuoi valori</a>
          </div>
        </section>
        <div class="griglia g4 numeri">
          <div class="scheda-box kpi"><div class="numero">${n.proposte ?? "—"}</div><div class="nota">proposte in 9 aree di governo</div></div>
          <div class="scheda-box kpi"><div class="numero">${n.cifre_verificate ?? "—"}</div><div class="nota">cifre verificate su fonte ufficiale</div></div>
          <div class="scheda-box kpi"><div class="numero">${nf(s.spesa, 1)} mld</div><div class="nota">programma del momento, senza deficit</div></div>
          <div class="scheda-box kpi"><div class="numero">${n.serie ?? "—"}</div><div class="nota">serie di dati aggiornate ogni giorno</div></div>
        </div>
        <section class="sezione"><h2>Come funziona</h2>
          <ol class="passi">${passi.map(([t, d]) => `<li><strong>${esc(t)}</strong><span>${esc(d)}</span></li>`).join("")}</ol>
        </section>
        <section class="sezione"><h2>Fiducia verificabile</h2>
          <div class="griglia g3">
            <div class="scheda-box"><h3>Linee rosse automatiche</h3><p>Le proposte che violano diritti fondamentali o scaricano i costi sui più deboli senza compensazione vengono escluse da regole fisse, che nessun prompt può aggirare.</p></div>
            <div class="scheda-box"><h3>Catena di integrità</h3><p>${D.integrita ? `${D.integrita.anelli} anelli registrati, catena <strong style="color:var(${integra ? "--buono" : "--cattivo"})">${integra ? "integra" : "da verificare"}</strong>.` : "In avvio."} <a href="#integrita">Vedi il registro</a></p></div>
            <div class="scheda-box"><h3>Tutto è riproducibile</h3><p>Codice, dati, punteggi e regole sono nel repository: chiunque abbia accesso può rieseguire il calcolo e ottenere lo stesso risultato.</p></div>
          </div>
        </section>
        <section class="sezione"><h2>Partecipa</h2>
          <div class="scheda-box"><p>Hai un problema da porre? <a href="${esc(linkAnalisi())}" target="_blank" rel="noopener">Scrivi una richiesta di analisi</a>: entro un giorno GovernAI risponde con una diagnosi e tre opzioni. Sono valutate sui valori della Carta, con costi e coperture. Le analisi pubblicate sono nella sezione <a href="#analisi">Analisi</a>.</p></div>
        </section>`;
    },

    obiettivi() {
      const o = D.obiettivi || [];
      if (!o.length) return '<h1>Obiettivi</h1><p class="vuoto">Il registro degli obiettivi è in preparazione.</p>';
      const STATO = { "raggiunto": "robusta", "in linea": "valori", "in ritardo": "var-PILOTA", "peggiorato": "sfavorevole", "in osservazione": "coda", "manuale": "coda" };
      const conta = o.reduce((a, x) => (a[x.stato] = (a[x.stato] || 0) + 1, a), {});
      return `
        <h1>Obiettivi</h1>
        <p class="intro">Ogni misura ha obiettivi misurabili, con valore di partenza e traguardo a 3 e 5 anni. Il sistema li segue sulle serie ufficiali. Quando una misura viene adottata, confronta il risultato con quanto previsto e ricalibra le scelte future: è così che il modello impara da successi e insuccessi.</p>
        <div class="griglia g4">${Object.entries(conta).map(([k, v]) => `<div class="scheda-box kpi"><div class="etichetta">${esc(k)}</div><div class="numero">${v}</div></div>`).join("")}</div>
        ${D.lezioni ? `<section class="sezione"><h2>Lezioni apprese</h2><div class="scheda-box md">${md(D.lezioni)}</div></section>` : ""}
        <section class="sezione"><h2>Indicatori</h2>
        <div class="tabella-box"><table><thead><tr><th>Misura</th><th>Obiettivo</th><th class="num">Base</th><th class="num">Ultimo</th><th class="num">Traguardo</th><th>Progresso</th><th>Stato</th></tr></thead><tbody>
          ${o.map((x) => `<tr class="cliccabile" data-proposta="${esc(x.proposta)}"><td>${esc(x.proposta)}</td><td>${esc(x.nome)} <small style="color:var(--tenue)">${esc(x.unita || "")}</small></td>
            <td class="num">${nf(x.base)}<br><small>${esc(x.periodo_base || "")}</small></td><td class="num">${nf(x.ultimo)}<br><small>${esc(x.periodo || "")}</small></td><td class="num">${nf(x.obiettivo)}</td>
            <td>${x.progresso == null ? "—" : `<div class="barra" title="${pct(x.progresso)}"><span style="width:${Math.max(0, Math.min(1, x.progresso)) * 100}%;${x.progresso < 0 ? "background:var(--cattivo)" : ""}"></span></div>`}</td>
            <td><span class="chip ${STATO[x.stato] || ""}">${esc(x.stato)}</span></td></tr>`).join("")}
        </tbody></table></div></section>`;
    },

    analisi() {
      const a = D.analisi || [];
      const sel = a.find((x) => x.id === stato.analisi) || a[0];
      return `
        <h1>Analisi su richiesta</h1>
        <p class="intro">Chiunque nel team può porre un problema scrivendo una richiesta: il pulsante apre su GitHub un modello già pronto da compilare. Ogni giorno GovernAI, attraverso l'abbonamento Claude e senza costi aggiuntivi, risponde con una diagnosi e tre opzioni. Le opzioni sono valutate da un panel indipendente sui valori della Carta, con costi, coperture e robustezza.</p>
        <p><a class="bottone primario" href="${esc(linkAnalisi())}" target="_blank" rel="noopener">Avvia un'analisi</a></p>
        ${a.length ? `<div class="doppia">
          <ul class="elenco">${a.map((x) => `<li><button data-analisi="${esc(x.id)}" class="${x === sel ? "attivo" : ""}">${esc(x.titolo)}<br><small>${esc(x.id.slice(0, 10))}${x.issue ? " · #" + x.issue : ""}</small></button></li>`).join("")}</ul>
          <div class="scheda-box md">${md(sel.testo)}</div></div>` : '<p class="vuoto">Nessuna analisi ancora: la prima la avvii tu.</p>'}`;
    },

    integrita() {
      const g = D.integrita || { anelli: 0, errori: [], ultimi: [] };
      const ok = !g.errori.length;
      return `
        <h1>Integrità</h1>
        <p class="intro">Un'AI non è incorruttibile per natura: lo diventa se ogni suo passo è registrato e verificabile. Ogni esecuzione aggiunge un anello a una catena di impronte crittografiche (SHA-256), come in una blockchain. Le impronte coprono regole (Carta, rubrica, codice), dati in ingresso e risultati, e ogni anello contiene l'impronta del precedente. Cambiare di nascosto qualcosa nel passato spezza la catena. Le regole che cambiano sono sempre dichiarate.</p>
        <div class="griglia g3">
          <div class="scheda-box kpi"><div class="etichetta">Stato della catena</div><div class="numero" style="color:var(${ok ? "--buono" : "--cattivo"})">${ok ? "Integra" : "Problemi"}</div><div class="nota">${ok ? "nessuna manomissione rilevata" : esc(g.errori.join("; "))}</div></div>
          <div class="scheda-box kpi"><div class="etichetta">Anelli registrati</div><div class="numero">${g.anelli}</div></div>
          <div class="scheda-box kpi"><div class="etichetta">Verifica indipendente</div><div class="nota">Chiunque può ricontrollare la catena con <code>python integrita/catena.py --verifica</code>. Git aggiunge una seconda catena, con autore e data di ogni modifica.</div></div>
        </div>
        <section class="sezione"><h2>Ultimi anelli</h2>
        <div class="tabella-box"><table><thead><tr><th>#</th><th>Data (UTC)</th><th>Evento</th><th>Impronta</th><th>Precedente</th><th>Regole cambiate</th></tr></thead><tbody>
          ${g.ultimi.map((x) => `<tr><td>${x.n}</td><td>${esc((x.data || "").replace("T", " ").slice(0, 16))}</td><td>${esc(x.evento)} <small style="color:var(--tenue)">${esc(x.nota || "")}</small></td>
            <td><code title="${esc(x.hash)}">${esc((x.hash || "").slice(0, 12))}</code></td><td><code>${esc((x.precedente || "").slice(0, 12))}</code></td>
            <td>${x.n === 0 ? "<small>genesi</small>" : (x.regole_cambiate || []).map((r) => `<span class="chip var-PILOTA">${esc(r)}</span>`).join(" ") || "—"}</td></tr>`).join("")}
        </tbody></table></div></section>`;
    },

    cruscotto() {
      const s = scenario("momento");
      const nucleo = D.proposte.filter((p) => p.classe === "robusta");
      const coperto = nucleo.filter((p) => s.misure[p.id] && ["PIENA", "ESSENZIALE"].includes(s.misure[p.id].variante)).length;
      const attive = D.regole.filter((r) => D.allerte_attive.includes(r.id));
      const ultimo = D.bollettini[0];
      const nota = ultimo && ultimo.testo.split(/\n## 6\. Nota del livello AI[^\n]*\n/)[1];
      return `
        <h1>Cruscotto</h1>
        <p class="intro">Lo stato del Paese secondo i dati ufficiali più recenti, le allerte attive e il programma adattato al momento. Si aggiorna ogni giorno.</p>
        <div class="griglia g3">
          <div class="scheda-box kpi"><div class="etichetta">Programma del momento</div><div class="numero">${nf(s.spesa, 1)} mld</div><div class="nota">all'anno, ${Object.keys(s.misure).length} misure su ${D.proposte.length}, finanziato senza deficit</div></div>
          <div class="scheda-box kpi"><div class="etichetta">Nucleo robusto finanziato</div><div class="numero">${coperto} / ${nucleo.length}</div><div class="nota">misure prioritarie con ogni combinazione di valori</div></div>
          <div class="scheda-box kpi"><div class="etichetta">Allerte attive</div><div class="numero" style="color:${attive.length ? "var(--cattivo)" : "var(--buono)"}">${attive.length}</div><div class="nota">${attive.length ? "il programma del momento ne tiene conto" : "nessuna anomalia rilevata"}</div></div>
        </div>
        ${attive.length ? `<section class="sezione"><h2>Allerte</h2>${attive.map((r) => {
          const i = D.indicatori.find((x) => x.id === r.indicatore) || {};
          const chips = [...(r.priorita || []).map((x) => `<span class="chip valori">+ ${esc(x)}</span>`), ...(r.sospendi || []).map((x) => `<span class="chip rossa">sospesa ${esc(x)}</span>`)].join(" ");
          return `<div class="allerta"><strong>${esc(r.messaggio)}</strong><p>${esc(i.nome || r.indicatore)}: ${nf(i.valore)} ${esc(i.unita || "")} (${esc(i.periodo || "")}). ${esc(r.azione)}</p>${chips ? `<p>${chips}</p>` : ""}</div>`;
        }).join("")}</section>` : ""}
        <section class="sezione"><h2>Indicatori <small>ultimo dato disponibile e variazione sul periodo precedente</small></h2>
          <div class="griglia g4">${D.indicatori.filter((i) => i.stato === "ok").map((i) => `
            <div class="scheda-box ind">
              <div class="ind-testa"><span>${esc(i.nome)}</span><span>${esc(i.periodo)}${i.provvisorio ? " · provv." : ""}</span></div>
              <div class="ind-valore">${nf(i.valore)}<small>${esc(i.unita)}</small></div>
              <div>${variazione(i, "delta", "")} ${i.delta12 != null ? " · " + variazione(i, "delta12", "in 12 periodi") : ""}</div>
              ${sparkline(i.serie)}
            </div>`).join("")}</div>
        </section>
        ${nota ? `<section class="sezione"><h2>Nota del livello AI <small>${esc(ultimo.data)}</small></h2><div class="scheda-box md">${md(nota)}</div></section>` : ""}`;
    },

    programma() {
      const s = scenario(stato.scenario);
      const rif = scenario("completo");
      const nucleo = D.proposte.filter((p) => p.classe === "robusta");
      const coperto = nucleo.filter((p) => s.misure[p.id] && ["PIENA", "ESSENZIALE"].includes(s.misure[p.id].variante)).length;
      const cerca = stato.cerca.toLowerCase();
      const righe = D.proposte.filter((p) => (!stato.area || p.area === stato.area) && (!stato.classe || p.classe === stato.classe)
        && (!cerca || (p.id + " " + p.titolo).toLowerCase().includes(cerca)) && (!stato.soloIncluse || s.misure[p.id]));
      let corpo = "", area = null;
      for (const p of righe) {
        if (p.area !== area) { area = p.area; corpo += `<tr class="gruppo"><td colspan="6">${esc(D.aree[area])}</td></tr>`; }
        const m = s.misure[p.id], r = rif.misure[p.id];
        const diverso = s.id !== "completo" && (m && m.variante) !== (r && r.variante);
        corpo += `<tr class="cliccabile${m ? "" : " esclusa"}" data-proposta="${esc(p.id)}">
          <td>${esc(p.id)}</td><td>${esc(p.titolo)} ${p.linea_rossa ? '<span class="chip rossa">!</span>' : ""}</td><td>${chipClasse(p.classe)}</td>
          <td>${chipVariante(m && m.variante)}${diverso ? ` <small style="color:var(--tenue)">(completo: ${esc(r ? r.variante.toLowerCase() : "esclusa")})</small>` : ""}</td>
          <td class="num">${m ? nf(m.costo) : "—"}</td>
          <td><div class="barra" title="robustezza ${pct(m && m.robustezza)}"><span style="width:${m ? Math.round(m.robustezza * 100) : 0}%"></span></div></td></tr>`;
      }
      return `
        <h1>Programma</h1>
        <p class="intro">Le 52 misure con la variante scelta dall'ottimizzatore: il massimo valore secondo la Carta, interamente finanziato senza deficit, con il nucleo robusto prima. Clicca una misura per la scheda pronta (dato, articolato normativo, cronoprogramma, indicatori).</p>
        <div class="segmenti" role="tablist" aria-label="Scenario">${D.scenari.map((x) => `<button data-scenario="${x.id}" class="${x.id === s.id ? "attivo" : ""}" title="${esc(x.descrizione)}">${esc(x.nome)}</button>`).join("")}</div>
        <div class="griglia g3" style="margin-top:14px">
          <div class="scheda-box kpi"><div class="etichetta">Spesa a regime</div><div class="numero">${nf(s.spesa, 2)} mld</div><div class="nota">${esc(s.descrizione)}</div></div>
          <div class="scheda-box kpi"><div class="etichetta">Coperture attivate</div><div class="numero">${s.coperture.length}</div><div class="nota">gettito minimo ${nf(s.gettito, 2)} mld + fondi vincolati</div></div>
          <div class="scheda-box kpi"><div class="etichetta">Misure incluse</div><div class="numero">${Object.keys(s.misure).length} / ${D.proposte.length}</div><div class="nota">nucleo robusto in versione piena o essenziale: ${coperto}/${nucleo.length}</div></div>
        </div>
        <div class="controlli">
          <input type="search" id="f-cerca" placeholder="Cerca una misura…" value="${esc(stato.cerca)}" aria-label="Cerca">
          <select id="f-area" aria-label="Area"><option value="">Tutte le aree</option>${Object.entries(D.aree).map(([k, v]) => `<option value="${k}" ${k === stato.area ? "selected" : ""}>${esc(v)}</option>`).join("")}</select>
          <select id="f-classe" aria-label="Classe"><option value="">Tutte le classi</option>${Object.entries(NOME_CLASSE).map(([k, v]) => `<option value="${esc(k)}" ${k === stato.classe ? "selected" : ""}>${esc(v)}</option>`).join("")}</select>
          <label class="spunta"><input type="checkbox" id="f-incluse" ${stato.soloIncluse ? "checked" : ""}> solo incluse</label>
        </div>
        <div class="tabella-box"><table><thead><tr><th>#</th><th>Misura</th><th>Classe</th><th>Variante</th><th class="num">mld/anno</th><th>Robustezza</th></tr></thead>
          <tbody>${corpo || '<tr><td colspan="6" class="vuoto">Nessuna misura con questi filtri.</td></tr>'}</tbody></table></div>`;
    },

    valori() {
      return `
        <h1>Valori</h1>
        <p class="intro">Il programma non sceglie un unico peso tra i valori: qui puoi provare il tuo. La classifica si ricalcola con i punteggi del panel indipendente (${esc(D.valutatori.join(", "))}).
          Il bollino «Nucleo robusto» indica le misure che restano in cima con <em>qualunque</em> combinazione di pesi.</p>
        <div class="simulatore">
          <div class="scheda-box">
            <h2>I tuoi pesi</h2>
            <div class="preset">
              <button data-preset="uguali">Pesi uguali</button>
              <button data-preset="FUT">Più futuro</button>
              <button data-preset="BEN">Più benessere</button>
              <button data-preset="INN">Più innovazione</button>
              <button data-preset="RIS">Più rispetto</button>
            </div>
            ${D.valori.map((v) => `<div class="cursore"><label for="w-${v.id}" title="${esc(v.definizione)}">${esc(v.nome)} <span id="wv-${v.id}"></span></label><input type="range" id="w-${v.id}" data-peso="${v.id}" min="0" max="100" value="50"></div>`).join("")}
            <h3 style="margin-top:16px">Orizzonti di tempo</h3>
            ${ORIZZ.map((o) => `<div class="cursore"><label for="h-${o}">${o[0].toUpperCase() + o.slice(1)} periodo <span id="hv-${o}"></span></label><input type="range" id="h-${o}" data-orizzonte="${o}" min="0" max="100" value="${o === "lungo" ? 40 : 30}"></div>`).join("")}
            <p style="font-size:.8rem;color:var(--tenue)">Regola della Carta: il lungo periodo pesa almeno quanto il breve. Il cursore si adegua da solo.</p>
          </div>
          <div class="scheda-box"><h2>Classifica <small style="color:var(--tenue);font-weight:400">(effetto pesato sui valori; frecce = spostamento rispetto ai pesi uguali)</small></h2><ol class="classifica" id="classifica"></ol></div>
        </div>`;
    },

    coperture() {
      const base = new Set(scenario("base").coperture), comp = new Set(scenario("completo").coperture);
      const fondi = [...new Set(D.coperture.map((c) => c.fondo_id))].sort();
      const tot = (set) => D.coperture.filter((c) => set.has(c.misura_id)).reduce((a, c) => a + (c.gettito_min || 0), 0);
      const punti = (c) => `<span class="punti" title="${D.valori.map((v) => v.nome + " " + (c[v.id] > 0 ? "+" : "") + c[v.id]).join(", ")}">${D.valori.map((v) => `<span class="${c[v.id] > 0 ? "p" : c[v.id] < 0 ? "n" : ""}"></span>`).join("")}</span>`;
      return `
        <h1>Coperture</h1>
        <p class="intro">Le misure concrete con cui si finanzia il programma, voce per voce: gettito minimo e massimo a regime, chi paga, effetto sui sette valori (verde positivo, rosso negativo). Livello 1 = basso costo sociale, livello 2 = strutturali.</p>
        <div class="griglia g3">
          <div class="scheda-box kpi"><div class="etichetta">Misure nel menu</div><div class="numero">${D.coperture.length}</div></div>
          <div class="scheda-box kpi"><div class="etichetta">Gettito minimo · programma base</div><div class="numero">${nf(tot(base), 2)} mld</div></div>
          <div class="scheda-box kpi"><div class="etichetta">Gettito minimo · programma completo</div><div class="numero">${nf(tot(comp), 2)} mld</div></div>
        </div>
        <div class="controlli">
          <input type="search" id="c-cerca" placeholder="Cerca (es. gasolio, IVA, tabacco)…" aria-label="Cerca">
          <select id="c-fondo" aria-label="Fondo"><option value="">Tutti i fondi</option>${fondi.map((f) => `<option>${esc(f)}</option>`).join("")}</select>
          <select id="c-livello" aria-label="Livello"><option value="">Tutti i livelli</option><option value="1">Livello 1</option><option value="2">Livello 2</option></select>
        </div>
        <div class="tabella-box"><table><thead><tr><th>Misura</th><th>Descrizione</th><th>Fondo</th><th class="num">Gettito min–max</th><th>Chi paga</th><th>Valori</th><th>Base</th><th>Completo</th></tr></thead>
          <tbody id="c-corpo">${D.coperture.map((c) => `<tr data-testo="${esc((c.misura_id + " " + c.descrizione + " " + c.chi_paga).toLowerCase())}" data-fondo="${esc(c.fondo_id)}" data-livello="${c.livello ?? 1}">
            <td>${esc(c.misura_id)}<br><span class="chip">liv. ${c.livello ?? 1}</span></td><td>${esc(c.descrizione)}</td><td>${esc(c.fondo_id)}</td>
            <td class="num">${nf(c.gettito_min)}–${nf(c.gettito_max)}</td><td>${esc(c.chi_paga)}</td><td>${punti(c)}</td>
            <td>${base.has(c.misura_id) ? "✓" : ""}</td><td>${comp.has(c.misura_id) ? "✓" : ""}</td></tr>`).join("")}</tbody></table></div>`;
    },

    bollettini() {
      if (!D.bollettini.length) return '<h1>Bollettini</h1><p class="vuoto">Nessun bollettino ancora.</p>';
      const sel = D.bollettini.find((b) => b.data === stato.bollettino) || D.bollettini[0];
      return `
        <h1>Bollettini</h1>
        <p class="intro">Ogni giorno la pipeline scarica i dati ufficiali aggiornati, ricalcola il programma e scrive un bollettino; il livello AI aggiunge la sua nota quando ci sono novità.</p>
        <div class="doppia">
          <ul class="elenco">${D.bollettini.map((b) => `<li><button data-bollettino="${esc(b.data)}" class="${b === sel ? "attivo" : ""}">${new Date(b.data).toLocaleDateString("it-IT", { weekday: "short", day: "numeric", month: "long", year: "numeric" })}</button></li>`).join("")}</ul>
          <div class="scheda-box md">${md(sel.testo)}</div>
        </div>`;
    },

    metodo() {
      const doc = { programma: "Programma 1.0", carta: "Carta dei valori", metodo: "Metodo degli agenti", sistema: "Sistema dinamico" };
      return `
        <h1>Metodo</h1>
        <p class="intro">Come nasce il programma: dossier ministeriali, verifica di 334 cifre su fonte primaria, Carta dei sette valori, panel indipendente e analisi di robustezza, ottimizzazione senza deficit, aggiornamento continuo dai dati ufficiali.</p>
        <div class="segmenti">${Object.entries(doc).map(([k, v]) => `<button data-documento="${k}" class="${k === stato.documento ? "attivo" : ""}">${v}</button>`).join("")}</div>
        <div class="scheda-box md" style="margin-top:14px">${md(D.documenti[stato.documento])}</div>`;
    },
  };

  // ---------- simulatore dei valori ----------
  function aggiornaClassifica() {
    const w = {}, h = {};
    D.valori.forEach((v) => { w[v.id] = +$("#w-" + v.id).value; $("#wv-" + v.id).textContent = w[v.id]; });
    if (+$("#h-lungo").value < +$("#h-breve").value) $("#h-lungo").value = $("#h-breve").value;
    ORIZZ.forEach((o) => { h[o] = +$("#h-" + o).value; $("#hv-" + o).textContent = h[o]; });
    const sw = Object.values(w).reduce((a, b) => a + b, 0) || 1, sh = Object.values(h).reduce((a, b) => a + b, 0) || 1;
    const punteggio = (p, pesi, oriz) => D.valori.reduce((acc, v, j) =>
      acc + pesi[v.id] * ORIZZ.reduce((a, o, k) => a + oriz[o] * p.punteggi[j][k], 0), 0);
    const uguali = Object.fromEntries(D.valori.map((v) => [v.id, 1 / 7])), oUguali = { breve: 1 / 3, medio: 1 / 3, lungo: 1 / 3 };
    const pw = Object.fromEntries(Object.entries(w).map(([k, x]) => [k, x / sw])), ph = Object.fromEntries(Object.entries(h).map(([k, x]) => [k, x / sh]));
    const conPunti = D.proposte.filter((p) => p.punteggi);
    const base = conPunti.map((p) => [p.id, punteggio(p, uguali, oUguali)]).sort((a, b) => b[1] - a[1]).map((x) => x[0]);
    const lista = conPunti.map((p) => ({ p, u: punteggio(p, pw, ph) })).sort((a, b) => b.u - a.u);
    const max = Math.max(...lista.map((x) => Math.abs(x.u)), 0.01);
    $("#classifica").innerHTML = lista.map((x, i) => {
      const salto = base.indexOf(x.p.id) - i;
      return `<li data-proposta="${esc(x.p.id)}"><span class="pos">${i + 1}</span>
        <span>${esc(x.p.titolo)} <small style="color:var(--tenue)">${esc(x.p.id)}</small> ${x.p.classe === "robusta" ? '<span class="chip robusta">Nucleo robusto</span>' : ""}</span>
        <div class="barra"><span style="width:${Math.max(0, x.u) / max * 100}%;${x.u < 0 ? "background:var(--cattivo)" : ""}"></span></div>
        <span class="salto ${salto > 0 ? "su" : salto < 0 ? "giu" : ""}">${salto > 0 ? "▲" + salto : salto < 0 ? "▼" + -salto : "="}</span></li>`;
    }).join("");
  }

  // ---------- navigazione ----------
  function mostra() {
    const vista = (location.hash || "#racconto").slice(1);
    const nome = viste[vista] ? vista : "racconto";
    document.querySelectorAll(".menu a").forEach((a) => a.classList.toggle("attivo", a.dataset.vista === nome));
    main.innerHTML = viste[nome]();
    document.title = "GovernAI · " + (document.querySelector(`.menu a[data-vista="${nome}"]`)?.textContent || nome);
    if (nome === "valori") {
      main.querySelectorAll("input[type=range]").forEach((el) => el.addEventListener("input", aggiornaClassifica));
      aggiornaClassifica();
    }
    if (nome === "coperture") {
      const filtra = () => {
        const t = $("#c-cerca").value.toLowerCase(), f = $("#c-fondo").value, l = $("#c-livello").value;
        main.querySelectorAll("#c-corpo tr").forEach((tr) => {
          tr.hidden = (t && !tr.dataset.testo.includes(t)) || (f && tr.dataset.fondo !== f) || (l && tr.dataset.livello !== l);
        });
      };
      ["#c-cerca", "#c-fondo", "#c-livello"].forEach((s) => $(s).addEventListener("input", filtra));
    }
    if (nome === "programma") {
      $("#f-cerca").addEventListener("input", (e) => { stato.cerca = e.target.value; ridisegna("#f-cerca"); });
      $("#f-area").addEventListener("change", (e) => { stato.area = e.target.value; ridisegna(); });
      $("#f-classe").addEventListener("change", (e) => { stato.classe = e.target.value; ridisegna(); });
      $("#f-incluse").addEventListener("change", (e) => { stato.soloIncluse = e.target.checked; ridisegna(); });
    }
  }
  function ridisegna(fuoco) {
    const y = window.scrollY;
    mostra();
    window.scrollTo(0, y);
    if (fuoco) { const el = $(fuoco); el.focus(); el.setSelectionRange(el.value.length, el.value.length); }
  }

  main.addEventListener("click", (e) => {
    const t = e.target.closest("[data-proposta],[data-scenario],[data-bollettino],[data-documento],[data-preset],[data-analisi]");
    if (!t) return;
    if (t.dataset.proposta) mostraProposta(t.dataset.proposta);
    else if (t.dataset.scenario) { stato.scenario = t.dataset.scenario; ridisegna(); }
    else if (t.dataset.bollettino) { stato.bollettino = t.dataset.bollettino; ridisegna(); }
    else if (t.dataset.documento) { stato.documento = t.dataset.documento; ridisegna(); }
    else if (t.dataset.analisi) { stato.analisi = t.dataset.analisi; ridisegna(); }
    else if (t.dataset.preset) {
      D.valori.forEach((v) => { $("#w-" + v.id).value = t.dataset.preset === "uguali" ? 50 : v.id === t.dataset.preset ? 100 : 35; });
      aggiornaClassifica();
    }
  });
  window.addEventListener("hashchange", () => { mostra(); window.scrollTo(0, 0); });

  $("#aggiornato").textContent = "Dati aggiornati al " + new Date(D.generato).toLocaleString("it-IT", { dateStyle: "long", timeStyle: "short" });
  // marked e DOMPurify arrivano dalla CDN: se sono lenti si ridisegna quando sono pronti
  window.addEventListener("load", mostra);
  mostra();
})();
