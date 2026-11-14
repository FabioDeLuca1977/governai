/* GovernAI · comunità su invito. Il programma resta leggibile da chiunque; discussione e appunti sono
   per gli iscritti. Database e regole di accesso: comunita/schema.sql; guida: comunita/README.md.
   La libreria Supabase si carica solo quando serve (chi legge e basta non contatta nessun servizio esterno). */
(function () {
  "use strict";
  const CFG = window.GOVERNAI_COMUNITA || {};
  const ATTIVA = !!(CFG.url && CFG.chiave);
  const SDK = {
    src: "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/dist/umd/supabase.js",
    integrity: "sha384-0w2KAL2YHP6wKOkUDzkCDGgVvfmHnj02DHeQ6XcHOgTfFsGyonKOpShMH1x6nk9o",
  };
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const icona = (n) => `<i data-lucide="${n}" aria-hidden="true"></i>`;
  const quando = (iso) => new Date(iso).toLocaleString("it-IT", { day: "numeric", month: "short", year: "numeric", hour: "2-digit", minute: "2-digit" });
  let ctx = { md: (t) => `<p>${esc(t)}</p>`, D: {}, icone: () => {} };

  // ---------- servizio ----------
  let client = null, caricamento = null, profilo; // profilo: undefined = da leggere, null = non iscritto
  function sdk() {
    if (client) return Promise.resolve(client);
    if (!caricamento) caricamento = new Promise((ok, ko) => {
      const s = document.createElement("script");
      s.src = SDK.src; s.integrity = SDK.integrity; s.crossOrigin = "anonymous";
      s.onload = () => { client = window.supabase.createClient(CFG.url, CFG.chiave, { auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: false } }); ok(client); };
      s.onerror = () => { caricamento = null; ko(new Error("Non riusciamo a raggiungere il servizio della comunità. Riprova tra poco.")); };
      document.head.appendChild(s);
    });
    return caricamento;
  }
  const haSessione = () => { try { return Object.keys(localStorage).some((k) => /^sb-.+-auth-token$/.test(k)); } catch (e) { return false; } };
  const ERRORI = [
    [/signups not allowed|user not found/i, "Questa email non risulta iscritta. Per entrare serve un invito."],
    [/token has expired|invalid.*(otp|token)/i, "Codice non valido o scaduto: chiedine uno nuovo."],
    [/link is invalid|has expired|otp_expired/i, "Il codice o il link di accesso non è valido o è scaduto: chiedine uno nuovo."],
    [/rate limit|too many|security purposes/i, "Troppi tentativi in poco tempo: aspetta qualche minuto e riprova."],
    [/failed to fetch|network/i, "Connessione non riuscita: controlla la rete e riprova."],
    [/nome_pubblico_check/, "Nome pubblico non valido: da 3 a 40 caratteri, con lettere, numeri, spazi, punto, trattino o apostrofo."],
    [/interventi_testo_check/, "Il testo deve avere da 2 a 4.000 caratteri."],
    [/email_check/, "L'indirizzo email non è valido."],
    [/motivazione_check/, "La motivazione deve avere da 20 a 1.500 caratteri."],
    [/richieste_invito_nome_check/, "Il nome deve avere da 2 a 80 caratteri."],
    [/check constraint|violates/i, "Alcuni dati non sono validi: controlla i campi e riprova."],
  ];
  const messaggio = (e) => { const m = String((e && e.message) || e); const t = ERRORI.find(([r]) => r.test(m)); return t ? t[1] : m; };
  async function rpc(nome, args) {
    const c = await sdk();
    const { data, error } = await c.rpc(nome, args || {});
    if (error) throw new Error(error.message);
    return data;
  }
  async function utente() { const c = await sdk(); const { data } = await c.auth.getSession(); return data.session ? data.session.user : null; }
  async function mioProfilo(forza) {
    if (profilo !== undefined && !forza) return profilo;
    profilo = (await utente()) ? await rpc("mio_profilo") : null;
    return profilo;
  }
  const linkInvito = (codice) => `${location.origin}${location.pathname}#/comunita/invito/${codice}`;
  const RITORNO = "governai-ritorno";
  // localStorage e non sessionStorage: il link dell'email si apre spesso in un'altra scheda
  const ricorda = () => { try { localStorage.setItem(RITORNO, location.hash); } catch (e) { /* non disponibile */ } };
  const torna = () => { let h = ""; try { h = localStorage.getItem(RITORNO) || ""; localStorage.removeItem(RITORNO); } catch (e) { /* non disponibile */ } location.hash = h && !h.startsWith("#/comunita/entra") ? h : "#/comunita"; };

  // Accesso dal link nell'email: Supabase torna al sito con i gettoni nell'indirizzo (#access_token=...).
  // Si tolgono subito dall'indirizzo, prima che il sito disegni la pagina, e si apre la sessione.
  let accesso = null;
  if (ATTIVA && /(^#|&)(access_token|error_description)=/.test(location.hash)) {
    const q = new URLSearchParams(location.hash.slice(1));
    const rit = new URLSearchParams(location.search).get("ritorno");
    if (rit && rit.startsWith("#/")) try { localStorage.setItem(RITORNO, rit); } catch (e) { /* non disponibile */ }
    history.replaceState(null, "", location.pathname + "#/comunita/entra");
    accesso = (async () => {
      if (!q.get("access_token")) throw new Error(q.get("error_description") || "Il link di accesso non è valido o è scaduto.");
      const c = await sdk();
      const { error } = await c.auth.setSession({ access_token: q.get("access_token"), refresh_token: q.get("refresh_token") });
      if (error) throw error;
    })();
  }

  // ---------- pezzi comuni ----------
  const errore = (testo) => `<div class="avviso alto" role="alert"><p>${esc(testo)}</p></div>`;
  const esito = (el, testo, tipo = "favorevole") => { if (el) el.innerHTML = `<div class="avviso ${tipo}" role="status"><p>${esc(testo)}</p></div>`; };
  const attesa = `<p class="nota" role="status">${icona("loader")} Caricamento…</p>`;
  const briciole = (pagina) => `<nav class="briciole" aria-label="Briciole di pane"><a href="#/comunita">Comunità</a><span aria-hidden="true">›</span><span aria-current="page">${esc(pagina)}</span></nav>`;
  const porta = (testo = "La discussione è riservata agli iscritti, che entrano su invito. Il programma, i dati e i controlli restano leggibili da tutti.") => `
    <div class="card comunita-porta">
      <p>${icona("lock")} ${esc(testo)}</p>
      <div class="azioni"><a class="btn primario s" href="#/comunita/entra" data-cazione="ricorda">Entra</a><a class="btn s" href="#/comunita/richiedi">Chiedi un invito</a><a class="btn terziario s" href="#/comunita/regole">Regole</a></div>
    </div>`;
  const inPreparazione = `<div class="card comunita-porta"><p>${icona("hourglass")} La comunità su invito è in preparazione: presto qui si potrà discutere ogni proposta. Intanto il programma è leggibile da tutti.</p><div class="azioni"><a class="btn s" href="#/comunita/regole">Leggi le regole</a></div></div>`;
  const TEMI = { generale: "Discussione generale", metodo: "Il metodo e le regole" };
  const nomeTema = (t) => {
    if (TEMI[t]) return TEMI[t];
    const p = t.match(/^proposta:(.+)$/); if (p) { const x = (ctx.D.proposte || []).find((q) => q.id === p[1]); return x ? `${p[1]} · ${x.titolo}` : p[1]; }
    const o = t.match(/^atto:(.+)$/); if (o) { const x = (((ctx.D.osservatorio || {}).atti) || []).find((q) => q.id === o[1]); return x ? `Governo di oggi · ${x.titolo}` : t; }
    const a = t.match(/^area:(\d{2})$/); if (a) { const x = ((ctx.D.mappa || {}).aree || {})[a[1]]; return x ? `Ministero: ${x.breve || a[1]}` : t; }
    return t;
  };
  const linkTema = (t) => { const p = t.match(/^proposta:(.+)$/); if (p) return `#/programma/${encodeURIComponent(p[1])}`; const o = t.match(/^atto:(.+)$/); return o ? `#/osservatorio/${encodeURIComponent(o[1])}` : `#/comunita/tema/${encodeURIComponent(t)}`; };

  // ---------- viste (HTML subito, i dati arrivano dopo in monta) ----------
  function vista(b, c) {
    if (b === "regole") return `${briciole("Regole e privacy")}<h1>Regole della comunità</h1><div class="md documento card">${ctx.md((ctx.D.comunita || {}).regole || "")}</div>
      <h2 class="sezione" id="privacy">Informativa sul trattamento dei dati</h2><div class="md documento card">${ctx.md((ctx.D.comunita || {}).privacy || "")}</div>`;
    if (!ATTIVA) return `<h1>Comunità</h1>${inPreparazione}`;
    if (b === "entra") return `${briciole("Entra")}<h1>Entra nella comunità</h1>
      <p class="risposta">Scrivi l'email con cui ti sei iscritto: ti mandiamo un codice di accesso. Nessuna password da ricordare.</p>
      <div data-c="entra" class="comunita-modulo"></div>`;
    if (b === "invito") return `${briciole("Iscrizione")}<h1>Hai ricevuto un invito</h1>
      <p class="risposta">Con l'iscrizione puoi discutere le proposte, prendere appunti con gli altri e segnalare errori. Qui nessuno decide: si ragiona insieme, persone e AI.</p>
      <div data-c="invito" data-codice="${esc(c || "")}" class="comunita-modulo"></div>`;
    if (b === "richiedi") return `${briciole("Chiedi un invito")}<h1>Chiedi un invito</h1>
      <p class="risposta">La comunità è aperta a ogni cittadino curioso. Si entra su invito per tenere la discussione rispettosa: dicci in due righe perché ti interessa. Un moderatore esamina la richiesta secondo le <a href="#/comunita/regole">regole pubbliche</a>.</p>
      <form class="card comunita-modulo" data-cform="richiedi">
        <label class="campo">Nome e cognome (non viene pubblicato)<input name="nome" required minlength="2" maxlength="80" autocomplete="name"></label>
        <label class="campo">Email<input name="email" type="email" required maxlength="200" autocomplete="email"></label>
        <label class="campo">Perché vuoi partecipare<textarea name="motivazione" required minlength="20" maxlength="1500" rows="4"></textarea></label>
        <label class="spunta"><input type="checkbox" name="consenso" required><span>Ho letto l'<a href="#/comunita/regole" target="_blank">informativa</a> e acconsento al trattamento dei miei dati per esaminare la richiesta.</span></label>
        <div class="azioni"><button class="btn primario" type="submit">Invia la richiesta</button></div>
        <div class="esito" aria-live="polite"></div>
      </form>`;
    if (b === "profilo") return `${briciole("Il tuo profilo")}<h1>Il tuo profilo</h1><div data-c="profilo">${attesa}</div>`;
    if (b === "moderazione") return `${briciole("Moderazione")}<h1>Moderazione</h1>
      <p class="risposta">Ogni azione richiede una motivazione e finisce nel <a href="#/comunita/registro">registro pubblico</a>. Si modera il comportamento, non le opinioni.</p><div data-c="moderazione">${attesa}</div>`;
    if (b === "registro") return `${briciole("Registro della moderazione")}<h1>Registro della moderazione</h1>
      <p class="risposta">Tutte le azioni dei moderatori e delle regole automatiche, con il motivo. Visibile a ogni iscritto.</p><div data-c="registro">${attesa}</div>`;
    if (b === "tema" && c) return `${briciole(nomeTema(c))}<h1>${esc(nomeTema(c))}</h1><section data-c="discussione" data-tema="${esc(c)}"></section>`;
    return `<h1>Comunità</h1>
      <p class="risposta">Uno spazio per ragionare sul programma: si discute, si prendono appunti, si confrontano idee con le altre persone e con l'AI. <strong>Qui nessuno decide</strong>, nemmeno chi ha avviato il progetto: le idee migliori diventano proposte che passano dagli stessi controlli di tutte le altre.</p>
      <div data-c="home">${attesa}</div>`;
  }

  // Sezione di discussione da inserire in altre pagine (scheda proposta, ministeri).
  const sezione = (tema, titolo = "Discussione fra iscritti") => `<section class="sezione" aria-labelledby="t-disc"><div class="sezione-testa"><h2 id="t-disc">${esc(titolo)}</h2><a href="#/comunita/regole">Regole</a></div><div data-c="discussione" data-tema="${esc(tema)}"></div></section>`;

  // ---------- riempimento asincrono ----------
  function monta(radice) {
    $$("[data-c]", radice).forEach((el) => {
      const tipo = el.dataset.c;
      if (tipo === "discussione") return montaDiscussione(el);
      if (!ATTIVA) return;
      const f = { home: montaHome, entra: montaEntra, invito: montaInvito, profilo: montaProfilo, moderazione: montaModerazione, registro: montaRegistro }[tipo];
      if (f) f(el).catch((e) => { el.innerHTML = errore(messaggio(e)); }).finally(() => ctx.icone());
    });
  }

  async function montaHome(el) {
    if (!haSessione()) { el.innerHTML = porta("Per partecipare serve un invito. Chi è già iscritto entra con la propria email."); return; }
    const p = await mioProfilo();
    if (!p) { el.innerHTML = porta("Hai confermato l'email ma non risulti iscritto: per iscriverti apri il link d'invito che hai ricevuto."); return; }
    const ultimi = await rpc("ultimi", { p_limite: 15 });
    el.innerHTML = `
      ${statoProfilo(p)}
      <div class="griglia g3-d sezione">
        <a class="card comunita-voce" href="#/comunita/tema/generale">${icona("messages-square")}<strong>Discussione generale</strong><span class="nota">Idee, domande, appunti sul programma nel suo insieme.</span></a>
        <a class="card comunita-voce" href="#/programma">${icona("list-checks")}<strong>Discuti una proposta</strong><span class="nota">Ogni scheda del programma ha la sua discussione in fondo alla pagina.</span></a>
        <a class="card comunita-voce" href="#/comunita/tema/metodo">${icona("scale")}<strong>Metodo e regole</strong><span class="nota">Come lavora l'AI, i pesi tra i valori, le regole della comunità.</span></a>
      </div>
      <section class="sezione"><div class="sezione-testa"><h2>Ultimi interventi</h2><a href="#/comunita/registro">Registro della moderazione</a></div>
        ${ultimi.length ? `<ul class="risultati">${ultimi.map((x) => `<li><a href="${linkTema(x.tema)}"><strong>${esc(nomeTema(x.tema))}</strong><small>${esc(x.autore)} · ${quando(x.creato_at)}</small><span class="comunita-estratto">${esc(x.testo)}</span></a></li>`).join("")}</ul>` : `<p class="nota">Ancora nessun intervento: apri tu la discussione.</p>`}
      </section>`;
  }
  const statoProfilo = (p) => `<div class="card comunita-io">
      <p><strong>${esc(p.nome_pubblico)}</strong> · ${p.stato === "prova" ? `in prova: i tuoi interventi compaiono dopo una revisione (${p.approvati} su 3 approvati)` : p.stato === "attivo" ? "iscritto" : "account sospeso"}${p.moderatore ? " · moderatore" : ""}</p>
      <div class="azioni"><a class="btn s" href="#/comunita/profilo">${icona("user-round")}Profilo e inviti</a>${p.moderatore ? `<a class="btn s" href="#/comunita/moderazione">${icona("shield")}Moderazione</a>` : ""}<button class="btn terziario s" type="button" data-cazione="esci">Esci</button></div>
    </div>`;

  // Accesso con codice via email (OTP): niente password, funziona anche aprendo la posta su un altro dispositivo.
  function moduloEmail(crea) {
    return `<form class="card" data-cform="otp" data-crea="${crea ? 1 : 0}">
      <label class="campo">Email<input name="email" type="email" required autocomplete="email"></label>
      <div class="azioni"><button class="btn primario" type="submit">Mandami l'email di accesso</button></div>
      <div class="esito" aria-live="polite"></div></form>`;
  }
  const moduloCodice = (email) => `<form class="card" data-cform="verifica" data-email="${esc(email)}">
      <p>Ti abbiamo scritto a <strong>${esc(email)}</strong>. Scrivi qui sotto il codice che trovi nell'email, oppure clicca il link nell'email: tornerai qui già collegato. Valgono un'ora; se non trovi l'email, guarda nella posta indesiderata.</p>
      <label class="campo">Codice ricevuto via email<input name="codice" inputmode="numeric" autocomplete="one-time-code" pattern="[0-9]{6,8}" maxlength="8" required></label>
      <div class="azioni"><button class="btn primario" type="submit">Entra</button><button class="btn terziario s" type="button" data-cazione="altra-email">Usa un'altra email</button></div>
      <div class="esito" aria-live="polite"></div></form>`;
  async function montaEntra(el) {
    if (accesso) {
      el.innerHTML = `<p class="nota" role="status">${icona("loader")} Accesso in corso…</p>`;
      try { await accesso; accesso = null; profilo = undefined; torna(); return; }
      catch (e) { accesso = null; el.innerHTML = errore(messaggio(e)); el.insertAdjacentHTML("beforeend", moduloEmail(false)); return; }
    }
    if (haSessione() && await mioProfilo()) { torna(); return; }
    el.innerHTML = `${moduloEmail(false)}<p class="nota">Non sei iscritto? <a href="#/comunita/richiedi">Chiedi un invito</a>.</p>`;
  }
  async function montaInvito(el) {
    const codice = el.dataset.codice;
    if (!codice || !(await rpc("verifica_invito", { p_codice: codice }))) {
      el.innerHTML = errore("Questo invito non è valido, è già stato usato o è scaduto. Puoi chiederne uno nuovo.") + `<div class="azioni sezione"><a class="btn" href="#/comunita/richiedi">Chiedi un invito</a></div>`;
      return;
    }
    const p = haSessione() ? await mioProfilo() : null;
    if (p) { el.innerHTML = `<div class="avviso info"><p>Sei già iscritto come <strong>${esc(p.nome_pubblico)}</strong>.</p></div><div class="azioni sezione"><a class="btn primario" href="#/comunita">Vai alla comunità</a></div>`; return; }
    const u = haSessione() ? await utente() : null;
    el.innerHTML = u ? moduloIscrizione(codice, u.email) : `<ol class="comunita-passi"><li><strong>Conferma la tua email</strong>: ti mandiamo un codice di accesso.</li><li>Scegli il <strong>nome pubblico</strong> con cui compari nelle discussioni.</li></ol>${moduloEmail(true)}`;
  }
  const moduloIscrizione = (codice, email) => `<form class="card" data-cform="iscrizione" data-codice="${esc(codice)}">
      <p class="nota">Email confermata: ${esc(email)} (non viene mostrata agli altri).</p>
      <label class="campo">Nome pubblico (da 3 a 40 caratteri; puoi usare uno pseudonimo)<input name="nome" required minlength="3" maxlength="40" pattern="[\\p{L}\\p{N}][\\p{L}\\p{N} ._'\\-]*" autocomplete="nickname"></label>
      <label class="spunta"><input type="checkbox" name="eta" required><span>Ho almeno 14 anni.</span></label>
      <label class="spunta"><input type="checkbox" name="regole" required><span>Accetto le <a href="#/comunita/regole" target="_blank">regole della comunità</a>.</span></label>
      <label class="spunta"><input type="checkbox" name="consenso" required><span>Ho letto l'<a href="#/comunita/regole" target="_blank">informativa</a>. Acconsento esplicitamente al trattamento dei miei dati, compreso il fatto che l'iscrizione può rivelare un interesse politico (art. 9 del GDPR).</span></label>
      <div class="azioni"><button class="btn primario" type="submit">Iscriviti</button></div>
      <div class="esito" aria-live="polite"></div></form>`;

  async function montaProfilo(el) {
    const p = haSessione() ? await mioProfilo(true) : null;
    if (!p) { el.innerHTML = porta(); return; }
    const inviti = await rpc("miei_inviti");
    el.innerHTML = `${statoProfilo(p)}
      <section class="sezione"><div class="sezione-testa"><h2>I tuoi inviti</h2><span class="nota">${p.inviti_residui} disponibili</span></div>
        <p class="nota">Ogni invito è personale e vale 30 giorni. Chi entra risulta invitato da te: invita persone che rispetteranno le regole.${p.invitato_da ? ` Tu sei entrato con l'invito di ${esc(p.invitato_da)}.` : ""}</p>
        ${p.stato === "attivo" && p.inviti_residui > 0 ? `<div class="azioni"><button class="btn primario s" type="button" data-cazione="crea-invito">${icona("send")}Crea un invito</button></div>` : p.stato === "prova" ? `<p class="nota">Potrai invitare altre persone dopo il periodo di prova.</p>` : ""}
        <div class="esito" id="esito-invito" aria-live="polite"></div>
        ${inviti.length ? `<ul class="risultati comunita-inviti">${inviti.map((i) => `<li><div><strong>${i.usato ? `Usato da ${esc(i.invitato || "un iscritto")}` : i.revocato ? "Revocato" : new Date(i.scade_at) < new Date() ? "Scaduto" : "Da usare"}</strong><small>creato il ${quando(i.creato_at)}</small></div>
          ${!i.usato && !i.revocato && new Date(i.scade_at) > new Date() ? `<div class="azioni"><button class="btn s" type="button" data-cazione="copia-invito" data-codice="${esc(i.codice)}">Copia il link</button><button class="btn terziario s" type="button" data-cazione="revoca-invito" data-codice="${esc(i.codice)}">Revoca</button></div>` : ""}</li>`).join("")}</ul>` : ""}
      </section>
      <section class="sezione"><div class="sezione-testa"><h2>I tuoi dati</h2><a href="#/comunita/regole">Informativa</a></div>
        <div class="azioni"><button class="btn s" type="button" data-cazione="scarica-dati">${icona("download")}Scarica i tuoi dati</button><button class="btn s" type="button" data-cazione="cancella-account">${icona("trash-2")}Cancella il tuo account</button></div>
        <div class="esito" id="esito-dati" aria-live="polite"></div>
      </section>`;
  }

  async function montaModerazione(el) {
    const p = haSessione() ? await mioProfilo(true) : null;
    if (!p || !p.moderatore) { el.innerHTML = errore("Questa pagina è riservata ai moderatori."); return; }
    const [coda, richieste] = await Promise.all([rpc("da_moderare"), rpc("richieste_in_attesa")]);
    const motivo = (id) => `<label class="campo largo">Motivo (finisce nel registro)<input name="motivo" required minlength="3" maxlength="500" data-per="${id}"></label>`;
    el.innerHTML = `
      <section class="sezione"><div class="sezione-testa"><h2>Interventi da rivedere</h2><span class="nota">${coda.length}</span></div>
        ${coda.length ? coda.map((x) => `<form class="card comunita-mod" data-cform="modera" data-id="${x.id}">
          <p class="nota"><a href="${linkTema(x.tema)}">${esc(nomeTema(x.tema))}</a> · ${esc(x.autore)} (${esc(x.stato_autore)}) · ${quando(x.creato_at)}${x.segnalazioni ? ` · ${x.segnalazioni} segnalazioni: ${esc(x.motivi)}` : ""}</p>
          <p class="comunita-testo">${esc(x.testo)}</p>
          <div class="filtri-barra">${motivo(x.id)}<button class="btn primario s" name="azione" value="approva">Approva</button><button class="btn s" name="azione" value="nascondi">Nascondi</button></div>
          <div class="esito" aria-live="polite"></div></form>`).join("") : `<p class="nota">Niente da rivedere.</p>`}
      </section>
      <section class="sezione"><div class="sezione-testa"><h2>Richieste di invito</h2><span class="nota">${richieste.length}</span></div>
        ${richieste.length ? richieste.map((r) => `<form class="card comunita-mod" data-cform="richiesta" data-id="${r.id}" data-email="${esc(r.email)}" data-nome="${esc(r.nome)}">
          <p><strong>${esc(r.nome)}</strong> · <span class="nota">${esc(r.email)} · ${quando(r.creato_at)}</span></p>
          <p class="comunita-testo">${esc(r.motivazione)}</p>
          <div class="filtri-barra">${motivo(r.id)}<button class="btn primario s" name="azione" value="si">Accogli</button><button class="btn s" name="azione" value="no">Non accogliere</button></div>
          <div class="esito" aria-live="polite"></div></form>`).join("") : `<p class="nota">Nessuna richiesta in attesa.</p>`}
      </section>
      <section class="sezione"><div class="sezione-testa"><h2>Sospendere o riattivare un iscritto</h2></div>
        <form class="card" data-cform="sospendi">
          <div class="filtri-barra"><label class="campo">Nome pubblico<input name="nome" required></label><label class="campo largo">Motivo<input name="motivo" required minlength="3" maxlength="500"></label></div>
          <label class="spunta"><input type="checkbox" name="ramo"><span>Azzera anche gli inviti di chi lo ha invitato</span></label>
          <div class="azioni"><button class="btn s" name="azione" value="sospendi">Sospendi</button><button class="btn s" name="azione" value="riattiva">Riattiva</button></div>
          <div class="esito" aria-live="polite"></div></form>
      </section>`;
  }

  async function montaRegistro(el) {
    const p = haSessione() ? await mioProfilo() : null;
    if (!p) { el.innerHTML = porta(); return; }
    const righe = await rpc("registro", { p_limite: 200 });
    el.innerHTML = righe.length ? `<div class="tabella-box"><table class="tabella"><thead><tr><th scope="col">Quando</th><th scope="col">Azione</th><th scope="col">Su</th><th scope="col">Motivo</th><th scope="col">Chi</th></tr></thead><tbody>
      ${righe.map((r) => `<tr><td>${quando(r.creato_at)}</td><td>${esc(r.azione)}</td><td>${esc(r.oggetto)}</td><td>${esc(r.motivo)}</td><td>${esc(r.moderatore)}</td></tr>`).join("")}</tbody></table></div>` : `<p class="nota">Nessuna azione di moderazione finora.</p>`;
  }

  // ---------- discussione ----------
  async function montaDiscussione(el) {
    if (!ATTIVA) { el.innerHTML = inPreparazione; return ctx.icone(); }
    if (!haSessione()) { el.innerHTML = porta(); return ctx.icone(); }
    el.innerHTML = attesa;
    try {
      const p = await mioProfilo();
      if (!p) { el.innerHTML = porta("Hai confermato l'email ma non risulti iscritto: apri il link d'invito che hai ricevuto."); return; }
      if (p.stato === "sospeso") { el.innerHTML = errore("Il tuo account è sospeso: puoi leggere il motivo nel registro della moderazione."); return; }
      const voci = await rpc("leggi", { p_tema: el.dataset.tema });
      const figli = {}; voci.forEach((v) => { (figli[v.risponde_a || 0] = figli[v.risponde_a || 0] || []).push(v); });
      const visti = new Set(voci.map((v) => v.id));
      const radici = voci.filter((v) => !v.risponde_a || !visti.has(v.risponde_a));
      const albero = (v, liv) => `<li class="interv" id="i-${v.id}">
          <div class="interv-testa"><strong>${esc(v.autore)}</strong><small>${quando(v.creato_at)}</small>${v.stato === "in_revisione" ? `<span class="chip attenzione">${icona("hourglass")}In revisione</span>` : v.stato === "nascosto" ? `<span class="chip alto">${icona("eye-off")}Nascosto</span>` : ""}</div>
          <p class="comunita-testo">${esc(v.testo)}</p>
          <div class="azioni interv-azioni">
            ${v.stato === "visibile" && liv < 3 ? `<button class="btn terziario s" type="button" data-cazione="rispondi" data-id="${v.id}">Rispondi</button>` : ""}
            ${!v.mio && v.stato === "visibile" ? (v.segnalato ? `<span class="nota">Segnalato da te</span>` : `<button class="btn terziario s" type="button" data-cazione="segnala" data-id="${v.id}">Segnala</button>`) : ""}
            ${v.mio ? `<button class="btn terziario s" type="button" data-cazione="elimina" data-id="${v.id}">Elimina</button>` : ""}
          </div>
          <div class="interv-spazio"></div>
          ${(figli[v.id] || []).length ? `<ul class="interv-lista">${figli[v.id].map((f) => albero(f, liv + 1)).join("")}</ul>` : ""}
        </li>`;
      el.innerHTML = `${p.stato === "prova" ? `<div class="avviso info"><p>Sei nel periodo di prova: i tuoi interventi compaiono a tutti dopo la revisione di un moderatore.</p></div>` : ""}
        ${radici.length ? `<ul class="interv-lista">${radici.map((v) => albero(v, 1)).join("")}</ul>` : `<p class="nota">Nessun intervento ancora. Apri tu la discussione: un dubbio, un dato da verificare, un'idea per migliorare la proposta.</p>`}
        ${moduloScrivi()}`;
    } catch (e) { el.innerHTML = errore(messaggio(e)); }
    ctx.icone();
  }
  const moduloScrivi = (risponde = "") => `<form class="card comunita-scrivi" data-cform="scrivi" data-risponde="${risponde}">
      <label class="campo">${risponde ? "La tua risposta" : "Il tuo intervento"}<textarea name="testo" required minlength="2" maxlength="4000" rows="${risponde ? 3 : 4}" placeholder="Argomenta con fatti e fonti; critica le idee, non le persone."></textarea></label>
      <div class="azioni"><button class="btn primario s" type="submit">Pubblica</button>${risponde ? `<button class="btn terziario s" type="button" data-cazione="annulla">Annulla</button>` : ""}<span class="nota">Massimo 4.000 caratteri.</span></div>
      <div class="esito" aria-live="polite"></div></form>`;
  const moduloSegnala = (id) => `<form class="card comunita-scrivi" data-cform="segnala" data-id="${id}">
      <label class="campo">Perché lo segnali<select name="motivo" required><option value="">Scegli…</option><option value="offesa">Offende una persona</option><option value="odio">Incita all'odio o discrimina</option><option value="spam">Pubblicità o spam</option><option value="dati_personali">Contiene dati personali di altri</option><option value="falso">Afferma il falso in modo deliberato</option><option value="fuori_tema">Fuori tema</option></select></label>
      <label class="campo">Nota per i moderatori (facoltativa)<input name="nota" maxlength="500"></label>
      <div class="azioni"><button class="btn primario s" type="submit">Segnala</button><button class="btn terziario s" type="button" data-cazione="annulla">Annulla</button></div>
      <div class="esito" aria-live="polite"></div></form>`;
  const ricarica = (el) => { const d = el.closest('[data-c="discussione"]'); if (d) montaDiscussione(d); };

  // ---------- moduli ----------
  document.addEventListener("submit", async (e) => {
    const f = e.target.closest("[data-cform]");
    if (!f) return;
    e.preventDefault();
    const out = $(".esito", f), dati = new FormData(f), bottone = e.submitter, azione = bottone && bottone.value;
    $$("button", f).forEach((b) => { b.disabled = true; });
    try {
      const tipo = f.dataset.cform;
      if (tipo === "richiedi") {
        const r = await rpc("chiedi_invito", { p_nome: dati.get("nome"), p_email: dati.get("email"), p_motivazione: dati.get("motivazione") });
        f.reset(); esito(out, r);
      } else if (tipo === "otp") {
        const email = String(dati.get("email")).trim().toLowerCase();
        const c = await sdk();
        ricorda();
        const { error } = await c.auth.signInWithOtp({ email, options: { shouldCreateUser: f.dataset.crea === "1", emailRedirectTo: location.origin + location.pathname + "?ritorno=" + encodeURIComponent(location.hash) } });
        if (error) throw error;
        f.outerHTML = moduloCodice(email); $("[name=codice]").focus(); return;
      } else if (tipo === "verifica") {
        const c = await sdk();
        const { error } = await c.auth.verifyOtp({ email: f.dataset.email, token: String(dati.get("codice")).trim(), type: "email" });
        if (error) throw error;
        profilo = undefined;
        const box = f.closest('[data-c="invito"]');
        if (box) { f.outerHTML = moduloIscrizione(box.dataset.codice, f.dataset.email); $("[name=nome]").focus(); return; }
        if (!(await mioProfilo())) { esito(out, "Email confermata, ma non risulti iscritto: per iscriverti apri il link d'invito.", "attenzione"); return; }
        torna(); return;
      } else if (tipo === "iscrizione") {
        await rpc("usa_invito", { p_codice: f.dataset.codice, p_nome: String(dati.get("nome")).trim(), p_consenso: dati.get("consenso") === "on" });
        profilo = undefined; location.hash = "#/comunita"; return;
      } else if (tipo === "scrivi") {
        const r = await rpc("scrivi", { p_tema: f.closest('[data-c="discussione"]').dataset.tema, p_testo: dati.get("testo"), p_risponde_a: f.dataset.risponde ? +f.dataset.risponde : null });
        if (r.stato !== "visibile") { f.reset(); esito(out, "Ricevuto: comparirà a tutti dopo la revisione di un moderatore.", "info"); }
        ricarica(f); return;
      } else if (tipo === "segnala") {
        await rpc("segnala", { p_id: +f.dataset.id, p_motivo: dati.get("motivo"), p_nota: dati.get("nota") || null });
        ricarica(f); return;
      } else if (tipo === "modera") {
        await rpc("modera", { p_id: +f.dataset.id, p_azione: azione, p_motivo: dati.get("motivo") });
        f.innerHTML = `<p class="nota">${azione === "approva" ? "Approvato" : "Nascosto"} · registrato.</p>`; return;
      } else if (tipo === "richiesta") {
        const codice = await rpc("esamina_richiesta", { p_id: +f.dataset.id, p_accolta: azione === "si", p_motivo: dati.get("motivo") });
        if (codice) {
          const link = linkInvito(codice);
          const corpo = `Ciao ${f.dataset.nome},\n\nla tua richiesta di partecipare alla comunità GovernAI è stata accolta. Questo è il tuo invito personale, valido 30 giorni:\n\n${link}\n\nA presto.`;
          f.innerHTML = `<p>Accolta. Manda questo invito personale a ${esc(f.dataset.email)}:</p><p class="mono comunita-link">${esc(link)}</p>
            <div class="azioni"><a class="btn primario s" href="mailto:${encodeURIComponent(f.dataset.email)}?subject=${encodeURIComponent("Il tuo invito alla comunità GovernAI")}&body=${encodeURIComponent(corpo)}">Scrivi l'email</a></div>`;
        } else f.innerHTML = `<p class="nota">Non accolta · registrato.</p>`;
        return;
      } else if (tipo === "sospendi") {
        if (azione === "sospendi") await rpc("sospendi", { p_nome: String(dati.get("nome")).trim(), p_motivo: dati.get("motivo"), p_ramo: dati.get("ramo") === "on" });
        else await rpc("riattiva", { p_nome: String(dati.get("nome")).trim(), p_motivo: dati.get("motivo") });
        f.reset(); esito(out, azione === "sospendi" ? "Sospensione registrata." : "Riattivazione registrata.");
      }
    } catch (err) { if (out) out.innerHTML = errore(messaggio(err)); }
    finally { $$("button", f).forEach((b) => { b.disabled = false; }); ctx.icone(); }
  });

  // ---------- azioni ----------
  document.addEventListener("click", async (e) => {
    const a = e.target.closest("[data-cazione]");
    if (!a) return;
    const az = a.dataset.cazione;
    if (az === "ricorda") return ricorda();
    try {
      if (az === "esci") { const c = await sdk(); await c.auth.signOut(); profilo = undefined; location.hash = "#/comunita"; window.dispatchEvent(new HashChangeEvent("hashchange")); }
      else if (az === "altra-email") { const f = a.closest("form"); f.outerHTML = moduloEmail(!!a.closest('[data-c="invito"]')); }
      else if (az === "rispondi") { const s = $(".interv-spazio", a.closest(".interv")); s.innerHTML = moduloScrivi(a.dataset.id); $("textarea", s).focus(); }
      else if (az === "segnala") { const s = $(".interv-spazio", a.closest(".interv")); s.innerHTML = moduloSegnala(a.dataset.id); $("select", s).focus(); }
      else if (az === "annulla") { a.closest("form").remove(); }
      else if (az === "elimina") { if (confirm("Eliminare definitivamente questo intervento?")) { await rpc("cancella_intervento", { p_id: +a.dataset.id }); ricarica(a); } }
      else if (az === "crea-invito") { const c = await rpc("crea_invito"); await navigator.clipboard.writeText(linkInvito(c)).catch(() => {}); profilo = undefined; await montaProfilo($('[data-c="profilo"]')); esito($("#esito-invito"), "Invito creato e link copiato: mandalo alla persona che vuoi invitare."); }
      else if (az === "copia-invito") { await navigator.clipboard.writeText(linkInvito(a.dataset.codice)); a.textContent = "Link copiato"; }
      else if (az === "revoca-invito") { await rpc("revoca_invito", { p_codice: a.dataset.codice }); profilo = undefined; await montaProfilo($('[data-c="profilo"]')); }
      else if (az === "scarica-dati") {
        const d = await rpc("miei_dati");
        const url = URL.createObjectURL(new Blob([JSON.stringify(d, null, 2)], { type: "application/json" }));
        const l = document.createElement("a"); l.href = url; l.download = "governai-miei-dati.json"; document.body.appendChild(l); l.click(); l.remove(); URL.revokeObjectURL(url);
      } else if (az === "cancella-account") {
        const p = await mioProfilo();
        const conferma = prompt(`La cancellazione elimina account, profilo, interventi e segnalazioni e non si può annullare.\nPer confermare scrivi il tuo nome pubblico: ${p.nome_pubblico}`);
        if (conferma === null) return;
        if (conferma.trim() !== p.nome_pubblico) { esito($("#esito-dati"), "Il nome non corrisponde: account non cancellato.", "attenzione"); return; }
        await rpc("cancella_account"); const c = await sdk(); await c.auth.signOut({ scope: "local" }); profilo = undefined;
        location.hash = "#/comunita"; alert("Account cancellato.");
      }
    } catch (err) { const box = a.closest(".comunita-modulo, [data-c]"); const out = box && $(".esito", box); if (out) out.innerHTML = errore(messaggio(err)); else alert(messaggio(err)); }
    ctx.icone();
  });

  window.Comunita = { attiva: ATTIVA, init: (c) => { ctx = { ...ctx, ...c }; }, vista, sezione, monta };
})();
