# GovernAI · Design system "Carta e inchiostro"

*Versione 1.0, 8 novembre 2026. Tutti i valori sono normativi: chi genera un template (persona, ChatGPT, Gemini) li usa così come sono. Il prototipo in `design/prototipo/` li applica. Rapporti di contrasto calcolati con la formula WCAG 2.x.*

## 1. Fondamenti

- **Carta e inchiostro**: fondo chiaro caldo, testo quasi nero, una sola tinta di marca (blu petrolio). Il colore porta significato (stato, gravità), non decorazione.
- **Ogni significato ha tre canali**: colore + icona + parola. Mai solo colore.
- **Mobile-first**: si progetta a 375 px, poi si allarga.
- **Numeri prima di tutto**: cifre tabulari, unità sempre visibili, formato italiano (12,99 mld; 5,6%; 8 nov 2026).

## 2. Colori

### 2.1 Token di base

| Token | Uso | Chiaro | Scuro |
|---|---|---|---|
| `--c-sfondo` | Fondo pagina | `#F7F6F2` | `#12171C` |
| `--c-superficie` | Card, testata, pannelli | `#FFFFFF` | `#1A2128` |
| `--c-superficie-2` | Fondi secondari, righe di gruppo, scheletri | `#EFEDE7` | `#222A33` |
| `--c-bordo` | Bordi decorativi di card e tabelle | `#D9D5CB` | `#34404B` |
| `--c-bordo-forte` | Bordi di campi e controlli (≥ 3:1) | `#8A8F94` | `#7C8894` |
| `--c-testo` | Testo principale, titoli | `#17202A` | `#E8ECEF` |
| `--c-testo-2` | Testo secondario, etichette, note | `#4E5964` | `#A9B4BE` |
| `--c-accento` | Link, pulsante primario, voce attiva, focus | `#12506B` | `#7DBAD6` |
| `--c-accento-hover` | Hover e pressione dell'accento | `#0C3D52` | `#A3D0E4` |
| `--c-accento-tenue` | Fondo voce attiva, selezioni | `#E3EEF2` | `#173544` |
| `--c-su-accento` | Testo sopra l'accento pieno | `#FFFFFF` | `#12171C` |

### 2.2 Token semantici (stato e gravità)

Ogni stato ha un colore *pieno* (testo, icona, bordo) e un colore *tenue* (fondo del chip).

| Token | Significato | Chiaro pieno / tenue | Scuro pieno / tenue |
|---|---|---|---|
| `--c-favorevole` | Nessun rilievo, nucleo robusto, compatibile, verificato, migliora | `#1F6B4F` / `#E2F0E8` | `#6DC39D` / `#16332A` |
| `--c-attenzione` | Condizionato, da verificare, richiede notifica, priorità media | `#865200` / `#FBEFD5` | `#E3B04B` / `#3A2D12` |
| `--c-alto` | Rischio alto, sfavorevole, peggiora, priorità alta | `#A3402A` / `#F8E5DF` | `#F08D72` / `#3D211B` |
| `--c-critico` | Rischio critico, linea rossa, incompatibile, priorità critica | `#7D1E3C` / `#F6E1E8` | `#EE93B1` / `#3B1B27` |
| `--c-neutro` | Non valutato, in coda, informativo, priorità bassa | `#55606B` / `#ECEBE6` | `#A9B4BE` / `#28313A` |
| `--c-info` | Informazione, dipende dai valori | = accento / accento tenue | = accento / accento tenue |

### 2.3 Token dei grafici

| Token | Uso | Chiaro | Scuro |
|---|---|---|---|
| `--g-positivo` | Barre e linee "migliora" negli assi divergenti | `#2B6F8F` | `#6FB0CF` |
| `--g-negativo` | Barre "peggiora" negli assi divergenti | `#B4532F` | `#F09A73` |
| `--g-serie` | Serie principale (linea) | `#12506B` | `#7DBAD6` |
| `--g-confronto` | Serie di confronto, tetto, obiettivo | `#5B6670` | `#A9B4BE` |
| `--g-traccia` | Fondo di barre, banda di incertezza | `#E6E3DA` | `#2A333C` |
| `--g-griglia` | Linee di griglia | `#E6E3DA` | `#2A333C` |
| `--g-zero` | Linea dello zero | `#8A8F94` | `#7C8894` |

Asse divergente **blu petrolio ↔ arancio mattone**: distinguibile con deuteranopia, protanopia e tritanopia; in più il segno (+/−) e la posizione rispetto allo zero portano lo stesso significato.

### 2.4 Contrasti verificati (WCAG 2.2 AA)

Testo normale ≥ 4,5:1; testo grande e componenti grafici ≥ 3:1.

| Coppia | Chiaro | Scuro |
|---|---|---|
| testo su sfondo / su superficie | 15,21 / 16,45 | 15,17 / 13,68 |
| testo-2 su sfondo / su superficie / su superficie-2 | 6,61 / 7,15 / 6,11 | 8,55 / 7,71 / 6,88 |
| accento su sfondo / su superficie | 8,14 / 8,80 | 8,47 / 7,64 |
| su-accento su accento (pulsante primario) | 8,80 | 8,47 |
| favorevole su tenue (chip) | 5,46 | 6,45 |
| attenzione su tenue | 5,72 | 6,76 |
| alto su tenue | 5,19 | 6,12 |
| critico su tenue | 7,94 | 6,88 |
| neutro su tenue | 5,38 | 6,26 |
| accento su accento tenue | 7,45 | 6,06 |
| bordo-forte su superficie (campi, 3:1) | 3,26 | 4,49 |
| g-positivo / g-negativo su superficie (3:1) | 5,57 / 4,98 | 6,80 / 7,41 |
| g-confronto su superficie | 5,87 | 7,71 |

`--c-bordo` (1,47:1) è solo decorativo: nessun controllo è riconoscibile solo dal bordo decorativo.

### 2.5 Codice CSS dei token

```css
:root {
  --c-sfondo:#F7F6F2; --c-superficie:#FFFFFF; --c-superficie-2:#EFEDE7;
  --c-bordo:#D9D5CB; --c-bordo-forte:#8A8F94;
  --c-testo:#17202A; --c-testo-2:#4E5964;
  --c-accento:#12506B; --c-accento-hover:#0C3D52; --c-accento-tenue:#E3EEF2; --c-su-accento:#FFFFFF;
  --c-favorevole:#1F6B4F; --c-favorevole-tenue:#E2F0E8;
  --c-attenzione:#865200; --c-attenzione-tenue:#FBEFD5;
  --c-alto:#A3402A;       --c-alto-tenue:#F8E5DF;
  --c-critico:#7D1E3C;    --c-critico-tenue:#F6E1E8;
  --c-neutro:#55606B;     --c-neutro-tenue:#ECEBE6;
  --g-positivo:#2B6F8F; --g-negativo:#B4532F; --g-serie:#12506B; --g-confronto:#5B6670;
  --g-traccia:#E6E3DA; --g-griglia:#E6E3DA; --g-zero:#8A8F94;
  color-scheme: light;
}
/* Scuro: segue il sistema, salvo scelta esplicita dell'utente */
@media (prefers-color-scheme: dark) { :root:not([data-tema="chiaro"]) { /* stessi valori di [data-tema="scuro"] */ } }
:root[data-tema="scuro"] {
  --c-sfondo:#12171C; --c-superficie:#1A2128; --c-superficie-2:#222A33;
  --c-bordo:#34404B; --c-bordo-forte:#7C8894;
  --c-testo:#E8ECEF; --c-testo-2:#A9B4BE;
  --c-accento:#7DBAD6; --c-accento-hover:#A3D0E4; --c-accento-tenue:#173544; --c-su-accento:#12171C;
  --c-favorevole:#6DC39D; --c-favorevole-tenue:#16332A;
  --c-attenzione:#E3B04B; --c-attenzione-tenue:#3A2D12;
  --c-alto:#F08D72;       --c-alto-tenue:#3D211B;
  --c-critico:#EE93B1;    --c-critico-tenue:#3B1B27;
  --c-neutro:#A9B4BE;     --c-neutro-tenue:#28313A;
  --g-positivo:#6FB0CF; --g-negativo:#F09A73; --g-serie:#7DBAD6; --g-confronto:#A9B4BE;
  --g-traccia:#2A333C; --g-griglia:#2A333C; --g-zero:#7C8894;
  color-scheme: dark;
}
```

## 3. Tipografia

Tre famiglie gratuite della stessa superfamiglia Adobe Source (Google Fonts, licenza SIL Open Font License), coerenti tra loro e con cifre tabulari.

| Ruolo | Famiglia | Pesi | Perché |
|---|---|---|---|
| Titoli, marchio, numeri chiave | **Source Serif 4** | 600, 700 | Tono editoriale e autorevole, da giornale di qualità; non è il font dei siti della PA (Titillium Web) né di un partito |
| Testo e interfaccia | **Source Sans 3** | 400, 600, 700 | Molto leggibile a piccole dimensioni, ampia copertura di caratteri, cifre tabulari (`font-variant-numeric: tabular-nums`) |
| Codici, impronte, CELEX | **Source Code Pro** | 400, 600 | Distinguibile 0/O e 1/l nelle impronte SHA-256 e nei codici |

```html
<link href="https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@400;600&family=Source+Sans+3:wght@400;600;700&family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&display=swap" rel="stylesheet">
```
Ripiego: `Georgia, "Times New Roman", serif` / `system-ui, -apple-system, "Segoe UI", Roboto, sans-serif` / `ui-monospace, Consolas, monospace`.

### Scala (mobile → desktop ≥ 900 px)

| Token | Famiglia | Mobile | Desktop | Interlinea | Peso | Uso |
|---|---|---|---|---|---|---|
| `--t-display` | Serif | 32 px | 48 px | 1,1 | 700 | Solo titolo della home |
| `--t-h1` | Serif | 28 px | 36 px | 1,15 | 700 | Titolo di pagina |
| `--t-h2` | Serif | 22 px | 26 px | 1,25 | 600 | Sezioni |
| `--t-h3` | Sans | 18 px | 19 px | 1,3 | 700 | Sottosezioni, titoli di card |
| `--t-numero` | Serif | 30 px | 36 px | 1,1 | 700 | `NumeroChiave` |
| `--t-corpo` | Sans | 16 px | 17 px | 1,55 | 400 | Testo |
| `--t-corpo-l` | Sans | 18 px | 20 px | 1,5 | 400 | Frase-risposta in testa alla pagina |
| `--t-piccolo` | Sans | 14 px | 14 px | 1,45 | 400/600 | Note, metadati, tabelle dense |
| `--t-etichetta` | Sans | 13 px | 13 px | 1,3 | 700, maiuscoletto +0,06em | Sopratitoli, intestazioni di tabella |
| `--t-chip` | Sans | 13 px | 13 px | 1,2 | 600 | Chip e badge |
| `--t-codice` | Mono | 13 px | 14 px | 1,4 | 400 | Codici e impronte |

Regole: righe di testo di **60-75 caratteri** (max-width 68ch); mai testo sotto 13 px; maiuscolo solo per etichette brevi; corsivo solo per titoli di atti e citazioni; testo ridimensionabile al 200% senza perdita di contenuto.

## 4. Spazi, griglia, forme

### 4.1 Spaziature (base 4 px)

| Token | px | Uso tipico |
|---|---|---|
| `--s-0` | 0 | |
| `--s-1` | 4 | Tra icona e testo nei chip |
| `--s-2` | 8 | Interno dei chip, gap tra chip |
| `--s-3` | 12 | Interno delle righe di tabella |
| `--s-4` | 16 | Margine laterale mobile, interno delle card mobile |
| `--s-5` | 24 | Interno delle card desktop, gap della griglia |
| `--s-6` | 32 | Tra blocchi di una sezione |
| `--s-7` | 48 | Tra sezioni |
| `--s-8` | 64 | Tra sezioni maggiori (desktop) |
| `--s-9` | 96 | Hero desktop |

### 4.2 Griglia e breakpoint

| Breakpoint | Larghezza | Colonne | Gutter | Margine | Navigazione |
|---|---|---|---|---|---|
| `xs` (base) | 0-599 px | 4 | 16 px | 16 px | Barra in basso, 5 voci |
| `sm` | 600-899 px | 8 | 16 px | 24 px | Barra in basso, 5 voci |
| `md` | 900-1199 px | 12 | 24 px | 32 px | Testata in alto |
| `lg` | ≥ 1200 px | 12 | 24 px | auto, contenuto max **1200 px** | Testata in alto |

Colonna di lettura (testi, verbali, schede): **max 760 px** (8 colonne) + indice a lato (3 colonne) da `md`.

### 4.3 Raggi

| Token | px | Uso |
|---|---|---|
| `--r-s` | 4 | Barre dei grafici, tag di codice |
| `--r-m` | 8 | Campi, pulsanti |
| `--r-l` | 12 | Card, pannelli, avvisi |
| `--r-xl` | 20 | Cassetti dal basso (mobile), finestre |
| `--r-pill` | 999 | Chip, controlli segmentati |

### 4.4 Ombre ed elevazione

| Token | Valore (chiaro) | Valore (scuro) | Uso |
|---|---|---|---|
| `--e-0` | nessuna, solo bordo `--c-bordo` | idem | Card di default (stile "carta stampata") |
| `--e-1` | `0 1px 2px rgba(23,32,42,.06), 0 1px 3px rgba(23,32,42,.08)` | `0 1px 2px rgba(0,0,0,.5)` | Card cliccabili, testata fissa |
| `--e-2` | `0 4px 12px rgba(23,32,42,.10)` | `0 4px 12px rgba(0,0,0,.55)` | Hover di card, menu |
| `--e-3` | `0 12px 32px rgba(23,32,42,.18)` | `0 12px 32px rgba(0,0,0,.6)` | Cassetti, finestre, ricerca |

### 4.5 Movimento

Durate 120 ms (hover), 200 ms (apertura sezioni), 280 ms (cassetti); curva `cubic-bezier(.2,.7,.2,1)`. Con `prefers-reduced-motion: reduce` tutte le transizioni sono a 0 ms. Nessuna animazione decorativa o in loop.

### 4.6 Focus e bersagli

- Focus visibile: `outline: 3px solid var(--c-accento); outline-offset: 2px;` su ogni elemento interattivo; mai rimosso.
- Bersagli tattili ≥ **44 × 44 px** (WCAG 2.5.8 chiede 24, adottiamo 44); distanza minima 8 px tra bersagli.
- La testata fissa non copre l'elemento con il focus (`scroll-padding-top: 80px`, WCAG 2.4.11).

## 5. Componenti

Formato: **scopo · anatomia · varianti · stati · accessibilità**.

### 5.1 Pulsante `Pulsante`

- **Anatomia**: [icona 20 px opzionale] + etichetta (verbo all'infinito o imperativo cortese: "Proponi un'idea") + [icona ↗ se apre un sito esterno].
- **Varianti**: *Primario* (fondo accento, testo su-accento; uno per vista) · *Secondario* (fondo superficie, bordo bordo-forte, testo accento) · *Terziario* (solo testo accento sottolineato al passaggio) · *Pericolo* (solo per azioni dei membri irreversibili, bordo critico).
- **Dimensioni**: M 44 px di altezza (default), S 36 px (solo dentro tabelle, con area di tocco estesa a 44).
- **Stati**: normale · passaggio (accento-hover, `--e-2` solo sui secondari) · premuto (scala 0,98) · focus (anello 3 px) · disattivato (opacità 0,45 + `aria-disabled` + spiegazione vicino) · in corso (spinner 16 px + "Invio…").
- **Esterno**: i pulsanti che aprono GitHub hanno ↗ e testo nascosto "(si apre in una nuova scheda)".

### 5.2 Chip di stato `Chip`

- **Anatomia**: pillola, altezza 24 px, padding 2 × 8 px, icona 14 px + parola (max 3 parole). Fondo *tenue*, testo e icona *pieni*, bordo 1 px pieno al 35% di opacità.
- **Insiemi** (stessa forma, significati diversi):

| Insieme | Valori → colore + icona Lucide |
|---|---|
| Classe della proposta | *Nucleo robusto* favorevole `shield-check` · *Dipende dai valori* info `scale` · *In coda* neutro `clock` · *Sfavorevole* alto `arrow-down-circle` |
| Linea rossa | *Linea rossa* critico `octagon-x` (sempre in testa, mai abbreviato in "!") |
| Esito della decisione | *Adottata* favorevole `check` · *Adottata con deroga* attenzione `git-branch` · *Respinta* alto `x` · *Rinviata* neutro `calendar-clock` · *Superata* neutro `history` |
| Stato della decisione (verifica) | *Confermata* favorevole `check-circle` · *Da riesaminare* attenzione `refresh-ccw` · *Riesame in coda* neutro `list-restart` |
| Stato UE | *In termine* neutro `calendar` · *Termine scaduto* alto `calendar-x` · *Infrazione aperta* critico `gavel` · *Misure notificate* favorevole `send` · *Completezza da verificare* attenzione `help-circle` |
| Stato richiesta | *Inviata* · *In revisione* · *In coda* · *Analizzata* · *Pubblicata* · *Non accolta* (con motivo) |

- **Stati**: statico (default) · come filtro: selezionabile, con ✓ quando attivo e `aria-pressed`.

### 5.3 Scala di gravità e rischio `ChipGravita` / `ChipRischio`

**Un'unica scala a 4 livelli + "non valutato" per tutto il prodotto** (principio 6 del brief).

| Livello | Token | Icona | Costituzione | Europa (priorità) | Controllo giuridico attuale | Allerte |
|---|---|---|---|---|---|---|
| 0 | favorevole | `circle-check` | Nessun rilievo | — | Compatibile | — |
| 1 | attenzione | `alert-circle` | Attenzione | Media | Condizionato · Richiede notifica | Attenzione |
| 2 | alto | `alert-triangle` | Rischio alto | Alta | — | Alto |
| 3 | critico | `octagon-x` | Rischio critico | Critica | Incompatibile | Critico |
| — | neutro | `circle-dashed` | Non esaminato | Bassa | Non valutato | — |

`BarraRischio`: barra orizzontale di 12 px divisa in segmenti proporzionali (0 → 3, da sinistra a destra), separati da 2 px di fondo; sotto, **sempre** la legenda testuale con i conteggi ("Nessun rilievo 112 · Attenzione 14 · Rischio alto 3 · Critico 0"). Il segmento a zero non si disegna ma resta in legenda.

### 5.4 Badge di verifica `BadgeVerifica`

Si mette accanto a ogni cifra. Piccolo (icona 14 px + parola 13 px), cliccabile: apre un popover con fonte, documento, tabella o serie, data, link.

| Variante | Token | Icona | Testo |
|---|---|---|---|
| Verificato su fonte | favorevole | `badge-check` | "Verificato" |
| Stima GovernAI | info | `calculator` | "Stima GovernAI" (popover: "non certificata dalla Ragioneria generale dello Stato") |
| Da verificare | attenzione | `help-circle` | "Da verificare" |
| Provvisorio | neutro | `hourglass` | "Provvisorio" |
| Generato dall'AI | neutro | `bot` | "Testo dell'AI, controllato da regole" |

Popover: titolo "Da dove viene questo numero", fonte, riferimento esatto (es. "MEF, Relazione evasione 2026, tab. III.1"), data di estrazione, [Apri la fonte ↗], [Copia citazione].

### 5.5 Card della proposta `CardProposta`

- **Anatomia** (dall'alto): sopratitolo (tema · codice, `--t-etichetta`, testo-2) → titolo (`--t-h3`, max 3 righe) → fila di chip (classe, linea rossa, controllo peggiore) → riga dati: `MisuratoreVariante` + costo "0,15 mld/anno" → (facoltativo) motivo dello stato ("Priorità per l'allerta inflazione").
- **Varianti**: *Compatta* (elenco mobile, 1 colonna) · *Riga* (tabella desktop) · *In evidenza* (home, con il problema in un dato) · *Classifica* (simulatore: posizione + spostamento ▲▼=).
- **Stati**: normale · passaggio (`--e-2`, titolo sottolineato) · focus · *non inclusa nello scenario* (testo-2, chip ‹Non inclusa› con bordo tratteggiato; mai nascosta) · *linea rossa* (bordo sinistro 4 px critico).
- **Accessibilità**: tutta la card è un unico link (`<a>` sul titolo con area estesa), chip letti dopo il titolo.

### 5.6 Misuratore della variante `MisuratoreVariante`

La variante è una **dose**, non un giudizio: tre pallini pieni/vuoti in accento + parola.
`Piena ●●●` · `Essenziale ●●○` · `Pilota ●○○` · `Zero ○○○` · `Non inclusa` (solo parola, tratteggio). `aria-label="Variante Essenziale, intensità 2 su 3"`.

### 5.7 Tabelle `TabellaDati`

- Intestazione con `--t-etichetta`, fissa durante lo scorrimento; righe 48 px (dense 40 px); numeri allineati a destra, cifre tabulari, unità nell'intestazione ("mld/anno").
- **Righe di gruppo** per tema (fondo superficie-2).
- **Ordinamento** con `aria-sort` e icona `arrow-up-down`; **filtri** sopra la tabella; [Scarica CSV] in alto a destra.
- **Mobile**: le tabelle con più di 3 colonne diventano **elenchi di card** (stesso contenuto, etichetta: valore). Le tabelle numeriche necessarie scorrono in orizzontale con prima colonna fissa e ombra di scorrimento.
- Stati: vuoto (riga unica con frase e azione), caricamento (5 righe scheletro), errore (avviso sopra la tabella).

### 5.8 Indicatore con trend `CardIndicatore`

- **Anatomia**: nome in italiano semplice ("Inflazione") + sigla tra parentesi ("HICP") · periodo ("ott 2026") + badge *Provvisorio* · **valore** (`--t-numero`) + unità · trend: freccia + variazione con segno + giudizio in parola ("▲ +1,4 · sfavorevole") nel colore favorevole/alto · minigrafico (solo se esiste la serie) · fonte con `BadgeVerifica`.
- **Regola del giudizio**: "favorevole/sfavorevole" dipende dal campo `meglio` (su/giù) dell'indicatore e si scrive sempre in parola. Variazione nulla: "■ stabile", neutro.
- **Varianti**: *Card* (griglia) · *Riga* (mobile) · *Grande* (pagina dell'indicatore con `GraficoSerie`) · *Obiettivo* (`IndicatoreObiettivo`: base → ultimo → traguardo su una barra di progresso con tacca dell'atteso).
- **Stati**: dato non disponibile (grigio, "Ultimo dato: …") · provvisorio · fonte non raggiunta.

### 5.9 Timeline delle sedute `TimelineSedute`

- Linea verticale 2 px (bordo) a sinistra; nodo 12 px pieno accento per sedute passate, vuoto per la prossima.
- Ogni nodo: data (`--t-etichetta`) · tipo (A richiesta / Ordinaria del lunedì / Per allerta) · titolo-domanda (`--t-h3`) · `ContatoreDecisioni` · chip della verifica quotidiana · [Apri il verbale].
- `ContatoreDecisioni`: barra impilata 8 px (adottate favorevole, respinte alto, rinviate neutro) + testo "46 adottate · 6 respinte · 1 rinviata".
- `PercorsoSeduta`: 4 passi numerati orizzontali (verticali sotto 600 px) — Esperti → Ministri → Opposizione → Capo di governo — con conteggi; ogni passo è un'ancora.
- Varianti: *Sedute* · *Scadenze* (Europa: asse orizzontale dei mesi su desktop, elenco per mese su mobile) · *Anelli* (Integrità: blocchi collegati da frecce ◀).

### 5.10 Altri componenti

| Componente | Specifica essenziale |
|---|---|
| `Testata` | 64 px desktop / 56 mobile, superficie, bordo inferiore, `--e-1` quando si scorre. Logo + 5 voci (voce attiva: fondo accento-tenue, testo accento, `aria-current="page"`) + ricerca + Metodo + [Partecipa] + tema |
| `BarraNavigazione` (mobile) | Fissa in basso, 64 px + `env(safe-area-inset-bottom)`, 5 voci icona 24 + etichetta 12 px, attiva in accento con indicatore 3 px sopra l'icona |
| `SottoNavigazione` | Schede sottolineate (3 px accento) su desktop; su mobile riga scorrevole con sfumatura al bordo |
| `BannerSimulazione` | Riga 40 px, fondo neutro-tenue, icona `flask-conical`, testo "Governo ombra · simulazione: le decisioni non sono in vigore." + "Perché?" Sempre nelle pagine Governo e nei blocchi "governo ombra" delle schede |
| `Avviso` | Bordo sinistro 4 px del token di gravità, fondo tenue, icona, titolo in grassetto, testo, azione. `role="status"` (informativo) o `role="alert"` (critico) |
| `NumeroChiave` | Etichetta → numero serif → nota → badge. Mai più di 4 per riga |
| `Sezione richiudibile` | `<details>/<summary>` nativo, chevron che ruota, conteggio tra parentesi, stato salvato nell'URL (`#controlli`) |
| `IndicePagina` | Sommario fisso a destra da `md` con evidenza della sezione visibile; su mobile pulsante "In questa pagina ▾" |
| `CardObiezione` | 4 righe etichettate: OBIEZIONE · PROVA · CAMBIEREBBE IDEA SE · RISPOSTA DEL CAPO; bordo sinistro neutro (mai rosso: l'opposizione leale non è un errore) |
| `CardParere` | Esperto (ruolo, non nome) · grado di certezza (‹Certezza alta/media/bassa›) · sintesi · fonti · limiti |
| `CampoRicerca` | 44 px, icona lente, scorciatoia "/" mostrata come tasto, risultati raggruppati per tipo |
| `Cursore` | Traccia 6 px, maniglia 24 px (area 44), valore numerico visibile, frecce ±5, `aria-valuetext="Futuro: 60 su 100"` |
| `CollegatoA` | Fino a 6 link tipizzati: icona del tipo + tipo + titolo |
| `Scheletro` | Blocchi superficie-2 con le dimensioni finali, nessuna animazione se movimento ridotto |

## 6. Iconografia

- **Set**: **Lucide** (https://lucide.dev, licenza ISC, gratuito), tratto 2 px, angoli arrotondati, 24 px nella navigazione, 20 px nei pulsanti, 16/14 px nei chip. Colore = `currentColor`.
- **Mappa principale**: Oggi `sunrise` · Programma `list-checks` · Governo `users-round` · Dati `chart-line` · Controlli `shield-check` · Metodo `book-open` · Partecipa `message-square-plus` · Cerca `search` · Tema `sun-moon` · Fonte `badge-check` · Esterno `external-link` · Copia `copy` · Scarica `download` · Condividi `share-2` · Costituzione `scroll-text` · Europa `globe-2` (non stelle UE) · Integrità `link-2` · Mandato `clipboard-check` · Previsione `target` · Allerta `bell-ring`.
- **Vietate**: icone di partiti o simboli (`flame`, `rose`, `sun` come marchio, `star` a 5 punte come decorazione, `hand` pugno, `landmark`/edifici del potere, bandiere `flag`), `sparkles` per l'AI.
- Icone sempre con etichetta testuale visibile, o con `aria-label` se isolate (es. cerca). Decorative: `aria-hidden="true"`.

## 7. Marchio

- Logotipo "GovernAI" in Source Serif 4, 700, colore testo; "AI" non evidenziato con colori diversi (evita l'effetto "AI magica").
- Simbolo: cerchio di 10 tacche radiali (i 10 valori), tratto 2 px, colore accento; dentro nessuna lettera. Favicon: lo stesso su fondo carta.
- Firma ricorrente sotto il logo in home e nel piè: "L'AI propone e verifica. Le persone decidono."

## 8. Grafici: regole

1. **Il titolo dice la conclusione, il sottotitolo dice che cosa si misura**: "L'inflazione è salita al 5,6%" / "Inflazione armonizzata (HICP), % annua, mensile, Eurostat".
2. **Barre partono da zero, sempre.** Le linee possono non partire da zero, ma l'asse lo dichiara ("asse da 3 a 6") e il minigrafico non mostra valori di asse: serve solo per la forma.
3. **Una scala per confronto**: grafici affiancati che confrontano la stessa grandezza usano la stessa scala. Niente doppi assi.
4. **Niente 3D, torte con più di 3 fette, ciambelle decorative, aree impilate per confrontare categorie.** Per le parti di un totale: barra impilata singola con etichette.
5. **Assi divergenti** (effetto sui valori −3…+3): zero al centro marcato, negativo a sinistra (`--g-negativo`), positivo a destra (`--g-positivo`), valore numerico con segno a fine barra; incertezza del panel come segmento sottile (min-max dei tre orizzonti) sopra la traccia.
6. **Etichette dirette** al posto delle legende quando possibile; legende sempre testuali, mai solo colore.
7. **Ogni grafico ha la sua tabella**: pulsante "Mostra i dati" (tabella accessibile) e [Scarica CSV]. Il grafico SVG ha `role="img"` e un `aria-label` che dice la conclusione e gli estremi.
8. **Fonte, periodo e stato** sotto ogni grafico: "Fonte: Eurostat (prc_hicp_manr), dato di ottobre 2026 provvisorio. Estratto l'8/11/2026."
9. **Incertezza visibile**: stime come intervalli (gettito min-max "0,30-0,50 mld"), previsioni con probabilità, dati provvisori tratteggiati.
10. **Nessun colore di partito** nei confronti tra partiti: tutte le serie in `--g-confronto`, GovernAI in `--g-serie`, ordine alfabetico.
11. **Formato italiano**: virgola decimale, punto per le migliaia (118 serie, 1.282,6 mln), mesi abbreviati in italiano (ott 2026).
12. **Sobrietà dell'inchiostro**: griglia leggera (`--g-griglia`), niente bordi e sfondi nei grafici, spessore linee 2 px.

## 9. Microcopy e linguaggio

### 9.1 Regole

- **Italiano semplice**: frasi sotto le 25 parole; una idea per frase; voce attiva.
- **Sigle sciolte alla prima occorrenza in ogni pagina**, poi sigla; tutte nel Glossario e con definizione al tocco (sottolineatura a puntini).
- **Codici dopo i titoli**: "IVA in tempo reale (01-P3)", mai "01-P3" da solo come titolo.
- **Numeri**: "12,99 mld di euro l'anno" (prima occorrenza), poi "12,99 mld"; percentuali con virgola ("5,6%"); date "8 novembre 2026" nei testi, "8 nov 2026" nei metadati, "8/11/2026" nelle tabelle.
- **Simulazione dichiarata**: nelle pagine Governo "ha deciso" è sempre accompagnato dal banner; nelle schede "Il governo ombra ha adottato… (simulazione)".
- **Limiti detti con calma**: "È una stima GovernAI, da verificare con la Ragioneria." Non "attenzione!".

### 9.2 Etichette standard

| Contesto | Testo |
|---|---|
| Pulsante primario home | Esplora il programma |
| Partecipa | Proponi un'idea · Fai una domanda al Consiglio · Segnala un errore |
| Azioni membri | Convoca il Consiglio (membri del progetto) · Chiedi un riesame |
| Copia | Copia link permanente → "Link copiato" (annuncio `aria-live`) |
| Badge | Verificato · Stima GovernAI · Da verificare · Provvisorio |
| Vuoto generico | "Qui non c'è ancora niente perché [motivo]. [Azione]" |
| Errore dati | "Non riusciamo a caricare i dati di oggi. [Riprova]" |
| Dati vecchi | "Dati fermi al [data]: l'aggiornamento automatico non è andato a buon fine." |
| Esterno | "Si apre GitHub in una nuova scheda. Serve un account gratuito." |
| Banner | "Governo ombra · simulazione: le decisioni non sono in vigore." |
| Costituzione | "Controllo preventivo automatico con revisione umana. Non è un giudizio: decide solo la Corte costituzionale." |

### 9.3 Glossario di base (sigle da sciogliere)

| Sigla | Forma sciolta |
|---|---|
| RGS | Ragioneria generale dello Stato |
| UPB | Ufficio parlamentare di bilancio |
| MEF | Ministero dell'economia e delle finanze |
| ISTAT | Istituto nazionale di statistica |
| HICP | Indice armonizzato dei prezzi al consumo |
| PIL | Prodotto interno lordo |
| NEET | Giovani che non studiano, non lavorano e non sono in formazione |
| SAD | Sussidi ambientalmente dannosi |
| LEP / LEA | Livelli essenziali delle prestazioni / di assistenza |
| PNRR | Piano nazionale di ripresa e resilienza |
| TFUE | Trattato sul funzionamento dell'Unione europea |
| CELEX | Codice identificativo degli atti UE in EUR-Lex |
| DPB | Documento programmatico di bilancio |
| CGUE | Corte di giustizia dell'Unione europea |
| A.C. | Atto della Camera (progetto di legge) |
| ViDA | "IVA nell'era digitale", direttiva (UE) 2025/516 |
| Brier | Punteggio di accuratezza delle previsioni: 0 perfetta, 0,25 come tirare a caso, 1 sempre sbagliata |

## 10. Accessibilità: lista di controllo

- [ ] Contrasti della §2.4 rispettati in entrambi i temi.
- [ ] Ogni significato con colore + icona + parola.
- [ ] Navigazione completa da tastiera; ordine logico; "Salta al contenuto" come primo link.
- [ ] Un solo `<h1>` per pagina; titoli in ordine; regioni `header`, `nav`, `main`, `footer`.
- [ ] Focus visibile (3 px) e non coperto dalla testata.
- [ ] Bersagli ≥ 44 px; nessuna azione solo a passaggio del mouse o a trascinamento (i cursori hanno anche tastiera e ±).
- [ ] Testo al 200% e reflow a 320 px senza scorrimento orizzontale (tranne tabelle dati).
- [ ] `lang="it"`; sigle con `<abbr title>` alla prima occorrenza.
- [ ] Grafici con `aria-label` conclusivo e tabella alternativa.
- [ ] Aggiornamenti dinamici (filtri, simulatore) annunciati con `aria-live="polite"`.
- [ ] `prefers-reduced-motion` e `prefers-color-scheme` rispettati.
- [ ] Link esterni dichiarati; nessun contenuto che lampeggi.
