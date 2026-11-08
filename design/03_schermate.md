# GovernAI · Schermate

*Versione 1.0, 8 novembre 2026. Presuppone `01_brief.md`, `02_architettura.md` e usa i componenti di `04_design_system.md` (nomi in `MonospazioCosì`). Esempi presi da `docs/data.js` dell'8/11/2026 e dalla cartella `europa/`; la sezione Costituzione usa l'esame reale di `costituzione/esami/` (screening automatico e esame approfondito del ddl di bilancio 2027).*

## 0. Convenzioni dei wireframe

```
[Testo]        pulsante            (•) / ( )   scelta singola
[≡] [⌕] [☾]    icone (menu, cerca, tema)        ▲ ▼ ■    trend su / giù / stabile
‹chip›         chip di stato o gravità          ●●○      misuratore della variante (dose)
▸ Titolo       sezione richiudibile (chiusa)    ▾        aperta
░░░            scheletro di caricamento          ┆        divisore
~~~            testo continuo                   ⓘ        badge di verifica (apre la fonte)
```
Larghezze: **mobile 375 px** (margini 16 px), **desktop 1280 px** (contenuto massimo 1200 px, 12 colonne).

### Struttura comune a tutte le schermate

```
DESKTOP
┌──────────────────────────────────────────────────────────────────────────────────┐
│ ◐ GovernAI   Oggi  Programma  Governo  Dati  Controlli      [⌕ Cerca…  /] Metodo [Partecipa] [☾] │  Testata (64 px, fissa)
├──────────────────────────────────────────────────────────────────────────────────┤
│ (solo Governo) ◇ Governo ombra · simulazione: le decisioni non sono in vigore    │  BannerSimulazione
├──────────────────────────────────────────────────────────────────────────────────┤
│ Briciole › …                                                                     │
│ Titolo pagina (H1)                                                               │  IntestazionePagina
│ Risposta in una frase                                   Aggiornato 8/11 14:22 ⓘ  │
│ [Scheda 1] [Scheda 2] [Scheda 3]                                                  │  SottoNavigazione
├──────────────────────────────────────────────────────────────────────────────────┤
│ … contenuto …                                                                    │
├──────────────────────────────────────────────────────────────────────────────────┤
│ Piè: Metodo · Integrità · Glossario · Documenti · Repository · Licenze ·          │
│ Segnala un errore — Prototipo di ricerca: l'AI propone e verifica, le persone decidono │
└──────────────────────────────────────────────────────────────────────────────────┘

MOBILE (375)
┌─────────────────────────────────┐
│ ◐ GovernAI        [⌕] [Partecipa]│  Testata compatta (56 px)
├─────────────────────────────────┤
│ … contenuto …                    │
│                                  │
├─────────────────────────────────┤
│  ☀      ☰       ◎      📈      ✓  │  BarraNavigazione (64 px + area sicura)
│ Oggi Programma Governo Dati Controlli│  icona 24 px + etichetta 12 px, sempre visibile
└─────────────────────────────────┘
```
Metodo e tema su mobile stanno nel menu del logo (tocco su "GovernAI") e nel piè di pagina.

### Stati comuni (valgono per ogni schermata salvo indicazione)

| Stato | Comportamento |
|---|---|
| **Caricamento** | `Scheletro` con le stesse dimensioni del contenuto finale (niente salti di layout). Dopo 8 s: "Il caricamento è lento. I dati pesano circa 1,4 MB." Nessuno spinner a pagina intera. |
| **Errore dati** | `Avviso` di gravità *alto*: "Non riusciamo a caricare i dati di oggi." + [Riprova] + "Ultima copia disponibile: 7/11/2026" se in cache. Mai pagina bianca. |
| **Dati non aggiornati** | Se `generato` è più vecchio di 36 ore: `Avviso` *attenzione* sotto la testata: "Dati fermi al 6/11/2026: l'aggiornamento automatico non è andato a buon fine." |
| **Vuoto** | Frase che spiega *perché* è vuoto + un'azione. Mai solo "Nessun dato". |
| **Offline** | Testata con chip ‹Offline› e contenuti già visti disponibili. |
| **Catena di integrità con errori** | `Avviso` *critico* fisso in tutte le pagine finché non è risolto, con link a Controlli › Integrità. |

---

## 1. Oggi (home)

**Obiettivo.** In 20 secondi: che cos'è GovernAI, che cosa è successo oggi, da dove partire. Per chi torna: che cosa è cambiato da ieri.

**Gerarchia dei contenuti**
1. Promessa e definizione (3 righe) + "L'AI propone e verifica. Le persone decidono." + 2 azioni.
2. Il giorno in 4 numeri (`NumeroChiave` × 4) con badge di verifica.
3. Allerte attive (4) con le proposte che diventano prioritarie.
4. Ultima seduta del governo ombra (`CardSeduta`).
5. Prossime scadenze (UE, semestre, mandati) — `ListaScadenze`.
6. Proposte per tema (9 aree) — `GrigliaTemi`.
7. Fiducia verificabile (integrità, cifre verificate, limiti) — `StrisciaFiducia`.
8. Partecipa.

**Componenti**: `Hero`, `NumeroChiave`, `Avviso` (variante allerta), `CardSeduta`, `ListaScadenze`, `GrigliaTemi`, `StrisciaFiducia`, `ChipGravita`, `BadgeVerifica`.

**Stati specifici**: nessuna allerta → riquadro *favorevole* "Nessuna allerta attiva: gli indicatori sono nelle soglie." • nessuna seduta → "Il Consiglio non si è ancora riunito. Si riunisce ogni lunedì e quando scatta un'allerta." • prima visita vs ritorno: dalla seconda visita (memoria locale del browser) l'hero si riduce a una riga e compare "Da ieri: 1 seduta nuova, 0 allerte nuove".

**Desktop**
```
┌───────────────────────────────────────────────────────────────────────────────────────┐
│ UN PROGRAMMA DI GOVERNO APERTO, BASATO SU DATI E VALORI DICHIARATI                     │
│ Governare con i dati,                                    ┌───────────────────────────┐ │
│ scegliere con i valori.                                  │ Oggi, 8 novembre 2026     │ │
│ ~~~ 62 proposte valutate su 10 valori, finanziate senza  │ ‹4 allerte attive›        │ │
│ deficit e controllate su Costituzione e regole UE. ~~~   │ Ultima seduta: oggi       │ │
│ L'AI propone e verifica. Le persone decidono.            │ Catena integra ✓ 9 anelli │ │
│ [Esplora il programma]  [Come funziona]                  └───────────────────────────┘ │
├───────────────────────────────────────────────────────────────────────────────────────┤
│ ┌───────────────────┐ ┌───────────────────┐ ┌───────────────────┐ ┌───────────────────┐│
│ │ PROGRAMMA DEL     │ │ MISURE INCLUSE    │ │ CIFRE VERIFICATE  │ │ SERIE DI DATI     ││
│ │ MOMENTO           │ │                   │ │                   │ │                   ││
│ │ 12,99 mld/anno    │ │ 53 su 62          │ │ 334               │ │ 118               ││
│ │ senza deficit ⓘ   │ │ nucleo robusto    │ │ su fonte primaria │ │ aggiornate ogni   ││
│ │ Stima GovernAI    │ │ 18 su 18 finanz.  │ │ ⓘ Verificato      │ │ giorno            ││
│ └───────────────────┘ └───────────────────┘ └───────────────────┘ └───────────────────┘│
├──────────────────────────────────────────────┬────────────────────────────────────────┤
│ Allerte attive (4)                    Tutte ›│ Ultima seduta del Consiglio      Tutte ›│
│ ┃‹Alto› Inflazione sopra il 3%               │ 8 nov 2026 · Seduta a richiesta         │
│ ┃ 5,6% (ott 2026, provvisorio) ▲ +1,4        │ Conti in ordine senza tagliare i        │
│ ┃ Diventano prioritarie: 02-C1 02-C4 04-P2 … │ servizi essenziali                      │
│ ┃‹Alto› Inflazione in forte aumento          │ 53 decisioni: 46 adottate · 6 respinte  │
│ ┃‹Alto› Debito/PIL +1,3 punti in un trimestre│ · 1 rinviata   · 30 deroghe dichiarate   │
│ ┃ 139,9% (II trim 2026) · Sospesa: 07-C5     │ 57 previsioni registrate · 9 mandati    │
│ ┃‹Attenzione› Fiducia consumatori in calo    │ [Leggi la sintesi]                      │
├──────────────────────────────────────────────┴────────────────────────────────────────┤
│ Prossime scadenze                                                                Tutte ›│
│ 23 nov  ‹Alto› Dir. (UE) 2024/1260 recupero e confisca dei beni · tra 15 giorni · 07-C2│
│ 30 nov  ‹Info› Parere della Commissione sul documento programmatico di bilancio       │
│ 02 dic  ‹Alto› Dir. (UE) 2024/2831 lavoro tramite piattaforme digitali · tra 24 giorni │
│ 31 dic  ‹Attenzione› Mandato M003 · Ministro dell'ambiente · riscrivere art. 4 di 03-P2│
├───────────────────────────────────────────────────────────────────────────────────────┤
│ Le proposte per tema                                                                  │
│ ┌─────────────┐┌─────────────┐┌─────────────┐┌─────────────┐┌─────────────┐           │
│ │Economia,    ││Lavoro,      ││Ambiente,    ││Infrastrut-  ││Istruzione,  │  … 9 temi │
│ │Imprese,     ││Welfare,     ││Energia,     ││ture e       ││Ricerca,     │           │
│ │Turismo  12  ││Famiglia  6  ││Agricoltura 5││Territori  6 ││Cultura   6  │           │
│ └─────────────┘└─────────────┘└─────────────┘└─────────────┘└─────────────┘           │
├───────────────────────────────────────────────────────────────────────────────────────┤
│ Fiducia verificabile                                                                  │
│ ✓ Catena integra · 9 anelli   ✓ Linee rosse automatiche   ✓ Tutto riproducibile  [Metodo]│
├───────────────────────────────────────────────────────────────────────────────────────┤
│ Hai un'idea o una domanda?  Serve un account GitHub gratuito.  [Proponi un'idea]       │
└───────────────────────────────────────────────────────────────────────────────────────┘
```

**Mobile (375)**
```
┌─────────────────────────────────┐
│ ◐ GovernAI        [⌕] [Partecipa]│
├─────────────────────────────────┤
│ Governare con i dati,            │
│ scegliere con i valori.          │
│ 62 proposte, 10 valori, nessun   │
│ deficit. L'AI propone e verifica.│
│ Le persone decidono.             │
│ [Esplora il programma        →]  │
│ Come funziona ›                  │
├─────────────────────────────────┤
│ ┌──────────────┐┌──────────────┐ │  2 × 2
│ │12,99 mld/anno││53 su 62      │ │
│ │senza deficit ││misure incluse│ │
│ └──────────────┘└──────────────┘ │
│ ┌──────────────┐┌──────────────┐ │
│ │4 allerte     ││✓ Catena      │ │
│ │attive        ││integra       │ │
│ └──────────────┘└──────────────┘ │
├─────────────────────────────────┤
│ Allerte attive (4)        Tutte ›│
│ ┃‹Alto› Inflazione sopra il 3%   │
│ ┃ 5,6% ▲ +1,4 · ott 2026        │
│ ┃‹Alto› Debito/PIL in salita     │
│ + altre 2                        │
├─────────────────────────────────┤
│ Ultima seduta · 8 nov            │
│ Conti in ordine senza tagliare   │
│ i servizi essenziali             │
│ 46 adottate · 6 respinte · 1 rinv│
│ [Leggi la sintesi]               │
├─────────────────────────────────┤
│ Prossime scadenze         Tutte ›│
│ 23 nov ‹Alto› Dir. 2024/1260     │
│ 30 nov ‹Info› Parere Commissione │
├─────────────────────────────────┤
│ Le proposte per tema             │
│ [Economia 12][Lavoro 6][Ambiente…│ ← scorrimento orizzontale
├─────────────────────────────────┤
│ ☀  ☰  ◎  📈  ✓                    │
└─────────────────────────────────┘
```

---

## 2. Programma (elenco delle proposte)

**Obiettivo.** Trovare una proposta per tema o parola e capire a colpo d'occhio classe, inclusione, costo e controlli.

**Gerarchia**: risposta ("53 misure su 62 nel programma del momento: 12,99 mld l'anno, coperti da 11,02 mld di gettito minimo più fondi vincolati, senza deficit") → selettore di scenario → filtri → elenco per tema.

**Componenti**: `ControlloSegmentato` (scenario: Programma base 7,90 · Completo 12,99 · Del momento 12,99 · + dividendo climatico 13,15 · + Difesa al 2,5% 12,25), `CampoRicerca`, `Filtro` (tema, classe, controlli, solo incluse), `CardProposta` (mobile) / `TabellaDati` (desktop, commutabile), `LegendaClassi`.

**Stati**: filtri senza risultati → "Nessuna proposta con questi filtri. [Togli i filtri]" • scenario che esclude la proposta → riga in grigio con chip ‹Non inclusa› (mai nascosta in silenzio) • ricerca con codice esatto (es. "02-C2") → apre la scheda.

**Desktop**
```
Programma
53 misure su 62 nel programma del momento: 12,99 mld l'anno, senza deficit. ⓘ Stima GovernAI
[Proposte] [Come si paga] [I tuoi valori] [Confronti]
Scenario: (Base 7,90) (Completo 12,99) (•Del momento 12,99) (+Dividendo 13,15) (+Difesa 2,5% 12,25)
┌ Cerca una proposta… ──────────┐ [Tema ▾] [Classe ▾] [Controlli ▾] [✓ solo incluse]   Vista: [▤ card][☰ tabella]
Classi: ‹Nucleo robusto› buona con ogni peso dei valori · ‹Dipende dai valori› scelta politica ·
        ‹In coda› · ‹Sfavorevole›                                                Cos'è? ›
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ ECONOMIA, IMPRESE, TURISMO · 12                                                       │
├──────┬───────────────────────────────────────┬────────────────┬──────────┬──────┬──────┤
│ 01-P3│ IVA in tempo reale                    │‹Nucleo robusto›│ Piena ●●●│ 0,15 │‹Cond.›│
│ 01-P7│ Dichiarazione zero: lo Stato fa il    │‹Nucleo robusto›│ Piena ●●●│  …   │  …   │
│      │ conto, il cittadino controlla         │                │          │      │      │
│ 01-P1│ Bilancio generazionale: ogni legge    │‹In coda›       │ Piena ●●●│ 0,02 │  …   │
│      │ dichiara chi paga e quando            │                │          │      │      │
│ …    │                                       │ Classe         │ Variante │mld/a │Contr.│
└──────┴───────────────────────────────────────┴────────────────┴──────────┴──────┴──────┘
```

**Mobile**
```
┌─────────────────────────────────┐
│ Programma                        │
│ 53 su 62 · 12,99 mld/anno ·      │
│ senza deficit ⓘ                  │
│ [Proposte][Come si paga][Valori›│
│ Scenario: [Del momento ▾]        │
│ [⌕ Cerca una proposta…        ]  │
│ [Tema ▾] [Classe ▾] [Filtri 1]   │
├─────────────────────────────────┤
│ ECONOMIA, IMPRESE, TURISMO · 12  │
│ ┌─────────────────────────────┐ │
│ │ IVA in tempo reale           │ │  CardProposta
│ │ 01-P3                        │ │
│ │ ‹Nucleo robusto› ‹Cond. ⚖›   │ │
│ │ Piena ●●● · 0,15 mld/anno    │ │
│ └─────────────────────────────┘ │
│ ┌─────────────────────────────┐ │
│ │ Dichiarazione zero: lo Stato │ │
│ │ fa il conto, il cittadino    │ │
│ │ controlla · 01-P7            │ │
│ └─────────────────────────────┘ │
└─────────────────────────────────┘
```

---

## 3. Scheda della proposta (oggetto centrale)

**Obiettivo.** Rispondere in una pagina a: che cosa, perché, quanto costa, chi paga, è legittima, che cosa ne ha deciso il governo ombra, come si misura il risultato. Tre livelli di lettura.

**Esempio reale**: **01-P3 · IVA in tempo reale** — area Economia, Imprese, Turismo; ‹Nucleo robusto› (prima metà della classifica nel 76% delle combinazioni di pesi; posizione tra 3ª e 44ª); variante nel programma del momento: Piena, 0,15 mld/anno, robustezza 99%; problema: gap IVA 34,4 mld nel 2023 (MEF, Relazione evasione 2026, tab. III.1); controlli: Costituzionale ‹Condizionato›, Europeo ‹Condizionato›, variante Piena ‹Richiede notifica› (deroga art. 395 dir. 2006/112/CE); obiettivi: gap IVA da 34,4 a 28,5 mld, rimborsi entro 60 giorni, zero condoni; governo ombra: deroga del capo di governo, avvio senza la parte che richiede l'autorizzazione UE, mandato M001 entro 28/2/2027.

**Gerarchia**
1. Intestazione: tema › codice, **titolo**, chip classe, chip linea rossa (se presente), stato nel programma (variante + costo).
2. **In breve** (sempre aperto): *Il problema in un dato* · *La soluzione* (2 frasi) · *Costo e chi paga* · *Che cosa ha deciso il governo ombra*.
3. **Effetto sui 10 valori**: `GraficoValori` divergente −3…+3, con incertezza del panel.
4. **Varianti** (Piena / Essenziale / Pilota): `ConfrontoVarianti`.
5. **Controlli**: Fiscale, Costituzionale, Europeo — `RigaControllo` con norme, motivazione, condizioni, fonti.
6. **Obiettivi misurabili**: `IndicatoreObiettivo`.
7. **Decisioni e mandati** del governo ombra (cronologia).
8. **Testo completo** (articolato normativo, cronoprogramma) — richiuso.
9. **Fonti e metodo**: robustezza, posizione, valutatori, versione, impronta.
10. **Collegato a** (max 6) + azioni: Condividi, Copia link permanente, Segnala un errore.

**Componenti**: `IntestazioneScheda`, `BloccoInBreve`, `BadgeVerifica`, `GraficoValori`, `ConfrontoVarianti`, `MisuratoreVariante`, `RigaControllo`, `ChipGravita`, `IndicatoreObiettivo`, `TimelineDecisioni`, `Sezione richiudibile`, `IndicePagina`, `CollegatoA`.

**Stati**: proposta senza punteggi → "Il panel non ha ancora valutato questa proposta." al posto del grafico • controllo giuridico assente → chip ‹Non valutato› + "La verifica giuridica non è ancora disponibile." • proposta mai discussa dal Consiglio → "Non ancora all'ordine del giorno del Consiglio." • obiettivi "manuali" → "Si misura a mano: dato non ancora disponibile nelle serie automatiche." • linea rossa → `Avviso` critico in testa, prima di ogni altro contenuto.

**Desktop** (contenuto 8 colonne + indice 3 colonne)
```
Programma › Economia, Imprese, Turismo › 01-P3
┌───────────────────────────────────────────────────────────────┬──────────────────────┐
│ IVA in tempo reale                                            │ IN QUESTA PAGINA     │
│ ‹✓ Nucleo robusto›  Nel programma del momento: Piena ●●●      │ In breve             │
│ 0,15 mld/anno · robustezza 99%                                │ Effetto sui valori   │
│ ┌───────────────────────────────────────────────────────────┐ │ Varianti             │
│ │ IN BREVE                                                  │ │ Controlli            │
│ │ Il problema in un dato                                    │ │ Obiettivi            │
│ │ 34,4 mld  di IVA non versata nel 2023, +3,6 mld sul 2022  │ │ Governo ombra        │
│ │ ⓘ Verificato · MEF, Relazione evasione 2026, tab. III.1   │ │ Testo completo       │
│ │ La soluzione                                              │ │ Fonti e metodo       │
│ │ L'Agenzia delle entrate incrocia fatture elettroniche,    │ ├──────────────────────┤
│ │ corrispettivi e pagamenti e blocca i crediti anomali      │ │ [Condividi]          │
│ │ prima che il denaro sparisca. Rimborsi in 60 giorni a chi │ │ [Copia link]         │
│ │ è affidabile. Nessun nuovo condono.                       │ │ Segnala un errore    │
│ │ Costo e chi paga                                          │ └──────────────────────┘
│ │ 0,15 mld/anno ⓘ Stima GovernAI · riallocazione di spese   │
│ │ Il governo ombra                                          │
│ │ ‹Adottata con deroga› in versione ridotta finché l'UE non │
│ │ autorizza la parte Piena · Mandato M001 entro 28/2/2027 › │
│ └───────────────────────────────────────────────────────────┘ │
│ Effetto sui 10 valori        mediana del panel, 3 orizzonti   │
│            peggiora  −3 ───────── 0 ───────── +3  migliora     │
│ Fiducia e trasparenza          │██████████   +2,0             │
│ Responsabilità futuro          │████████     +1,7             │
│ Equità                         │████████     +1,7             │
│ Cittadinanza responsabile      │████████     +1,7             │
│ Innovazione                    │████         +1,0             │
│ Sicurezza senza controllo   ▒▒│             −0,3             │
│ Benessere                      │█            +0,3             │
│ … altri 3 a zero  ▸ mostra                                    │
│ Varianti                                                      │
│ ┌──────────────┬──────────────┬──────────────┐                │
│ │ Piena ●●●    │Essenziale ●●○│ Pilota ●○○   │                │
│ │ 0,15 mld     │ 0,08 mld     │ 0,04 mld     │                │
│ │ ✓ nel progr. │              │              │                │
│ │ + reverse    │ senza revers.│ 3 settori,   │                │
│ │ charge (UE)  │ charge       │ 2 anni       │                │
│ └──────────────┴──────────────┴──────────────┘                │
│ Controlli                                                     │
│ Costituzionale  ‹! Condizionato›  artt. 3, 23, 24, 41, 53, 97 ▸│
│ Europeo         ‹! Condizionato›  Dir. 2006/112/CE; ViDA ▸    │
│ Fiscale · Essenziale ‹! Condizionato› ▸                       │
│ Variante Piena  ‹! Richiede notifica› deroga art. 395 ▸       │
│ Scadenza UE collegata: Dir. (UE) 2025/516 (ViDA) · 31/12/2026 │
│ Obiettivi                                                     │
│ Gap IVA        base 34,4 mld (2023) → traguardo 28,5  ‹Manuale›│
│ Rimborsi IVA   → 60 giorni                           ‹Manuale›│
│ ▸ Testo completo (articolato, cronoprogramma)                 │
│ ▸ Fonti e metodo                                              │
│ Collegato a: [◎ Seduta 8/11 Conti in ordine] [⚑ M001] [€ Dir. 2025/516] │
└───────────────────────────────────────────────────────────────┘
```

**Mobile**
```
┌─────────────────────────────────┐
│ ‹ Programma                      │
│ ECONOMIA · 01-P3                 │
│ IVA in tempo reale               │
│ ‹✓ Nucleo robusto›               │
│ Piena ●●● · 0,15 mld/anno        │
│ [In questa pagina ▾]             │
├─────────────────────────────────┤
│ IN BREVE                         │
│ 34,4 mld                         │
│ di IVA non versata nel 2023      │
│ ⓘ Verificato · MEF 2026          │
│ ~~ soluzione in 2 frasi ~~       │
│ Costo: 0,15 mld/anno ⓘ Stima     │
│ Governo ombra: ‹Adottata con     │
│ deroga› · M001 entro 28/2/2027 › │
├─────────────────────────────────┤
│ Effetto sui valori               │
│ Fiducia       │█████  +2,0       │
│ Futuro        │████   +1,7       │
│ Sicurezza    ▒│       −0,3       │
│ Mostra tutti i 10 ›              │
├─────────────────────────────────┤
│ ▸ Varianti (3)                   │
│ ▸ Controlli  ‹! 2 condizionati›  │
│ ▸ Obiettivi (3)                  │
│ ▸ Governo ombra                  │
│ ▸ Testo completo                 │
│ ▸ Fonti e metodo                 │
├─────────────────────────────────┤
│ [Condividi]  [Segnala errore]    │
└─────────────────────────────────┘
```

---

## 4. Governo (sedute) e verbale di seduta

### 4.1 Governo — elenco delle sedute

**Obiettivo.** Vedere che cosa ha deciso il governo ombra, quando e su quale domanda; capire che è una simulazione.

**Gerarchia**: `BannerSimulazione` → risposta ("2 sedute, 96 decisioni, 19 mandati aperti, 0 previsioni ancora verificabili") → azioni (Fai una domanda al Consiglio; Convoca, membri) → `TimelineSedute` → stato delle decisioni in vigore → collegamenti a Mandati, Credibilità, Regole.

**Componenti**: `BannerSimulazione`, `TimelineSedute`, `CardSeduta`, `ChipEsito` (confermata, da riesaminare, superata), `ContatoreDecisioni`.

**Stati**: nessuna seduta → "Il Consiglio non si è ancora riunito." • verifica quotidiana con esito "da riesaminare" → chip ‹Attenzione› e "Riesame in coda".

```
DESKTOP
◇ Governo ombra · simulazione: le decisioni non sono in vigore. Perché? ›
Governo
Il governo ombra si è riunito 2 volte: 96 decisioni, 19 mandati aperti.
[Sedute] [Decisioni in vigore] [Mandati 19] [Credibilità] [Chi siede e regole]
[Fai una domanda al Consiglio]  Convoca il Consiglio (membri del progetto) ›
────────────────────────────────────────────────────────────────────────────
 8 NOV 2026 ●── Seduta a richiesta                              ‹✓ Confermata oggi›
           │   Conti in ordine senza tagliare i servizi essenziali
           │   53 decisioni: 46 adottate · 6 respinte · 1 rinviata · 30 deroghe
           │   9 ministri · 8 esperti · opposizione leale: 8 obiezioni
           │   [Apri il verbale]
 8 NOV 2026 ●── Prima seduta (allerte)                          ‹✓ Confermata oggi›
           │   Allerte attive: inflazione al 5,6% e in salita, debito/PIL in aumento,
           │   fiducia in calo, PIL fermo nel terzo trimestre
           │   43 decisioni: 40 adottate · 1 respinta · 2 rinviate
           ○   Prossima seduta ordinaria: lunedì 9 novembre 2026
```
Mobile: stessa timeline a una colonna, la linea verticale a 16 px dal bordo; il banner è una riga compatta con "Perché?".

### 4.2 Verbale di seduta

**Obiettivo.** Leggere una seduta lunga (il verbale reale "conti in ordine" supera le 335 mila battute) in 3 livelli: *la domanda e la risposta* → *le decisioni e chi era contrario* → *pareri e posizioni integrali*.

**Esempio reale**: seduta **2026-11-08-1-conti-in-ordine** — domanda "Qual è il piano 2027-2029 per riportare il debito pubblico su una traiettoria discendente senza tagliare i servizi essenziali?"; indirizzo del capo di governo: riserva per il risanamento di 1,15 mld l'anno; 53 decisioni; 30 deroghe dall'esito del motore (tra cui 07-C1, 07-C2, 07-C3, 07-C4, 09-C3, 01-P3); pareri di 8 esperti (finanza pubblica, tributario, giurista, integrità, macroeconomia, PA e digitale, sanità, valutazione); posizioni di 9 ministri; mandati M011-M019; 57 previsioni; 1 rilievo formale.

**Gerarchia**
1. Banner simulazione; intestazione: data, tipo (a richiesta / ordinaria / allerta), **titolo-domanda**, esito della verifica quotidiana.
2. `PercorsoSeduta`: i 4 passi del regolamento (Esperti → Ministri → Opposizione → Capo) con conteggi; ogni passo è un'ancora.
3. **La domanda** (citazione, con *Perché ora* e *Vincoli*).
4. **La risposta in breve** + **Indirizzo del capo di governo**.
5. **Decisioni** (`ContatoreDecisioni` + elenco filtrabile per esito: adottata / respinta / rinviata; `RigaDecisione`).
6. **Deroghe dall'esito del motore** (sempre visibili, mai richiuse: principio 5).
7. **Obiezioni dell'opposizione e risposte** (`CardObiezione`: obiezione → prova → che cosa le farebbe cambiare idea → risposta del capo).
8. Pareri degli esperti (richiusi, uno per esperto, con grado di certezza).
9. Posizioni dei ministri (richiuse).
10. Mandati (con scadenza) e previsioni registrate.
11. Rilievi formali, fonti, impronta nella catena, "Chiedi un riesame".

**Componenti**: `BannerSimulazione`, `PercorsoSeduta`, `Citazione`, `ContatoreDecisioni`, `RigaDecisione`, `ChipEsito`, `MisuratoreVariante`, `CardObiezione`, `CardParere` (con `ChipCertezza`), `ListaMandati`, `Sezione richiudibile`, `IndicePagina`.

**Stati**: risposta del capo assente (oggi tutte le 8 obiezioni della seduta hanno "Risposta del capo: —") → chip ‹Attenzione · Non registrata› e link alla decisione collegata: la regola 7 del Regolamento chiede una risposta scritta, e il design deve rendere visibile quando manca • verbale molto lungo → si visualizzano le sezioni 1-7, il resto si carica all'apertura della sezione • seduta senza obiezioni → "L'opposizione leale non ha sollevato obiezioni su questa seduta." (raro: va detto) • decisione superata da una seduta successiva → chip ‹Superata› con link alla nuova.

**Desktop**
```
◇ Governo ombra · simulazione: le decisioni non sono in vigore.
Governo › Sedute › 8 novembre 2026
SEDUTA A RICHIESTA · 8 NOV 2026                              ‹✓ Confermata dalla verifica di oggi›
Conti in ordine senza tagliare i servizi essenziali
┌────────────────────────────────────────────────────────────────┬─────────────────────┐
│  ① Esperti 8  ──▶  ② Ministri 9  ──▶  ③ Opposizione 8  ──▶  ④ Capo │ IN QUESTA PAGINA   │
│  scrivono da soli   leggono i pareri   cerca i punti deboli  decide │ La domanda         │
├────────────────────────────────────────────────────────────────┤ La risposta        │
│ LA DOMANDA                                                      │ Decisioni (53)     │
│ ┃ Qual è il piano 2027-2029 per riportare il debito pubblico su │ Deroghe (30)       │
│ ┃ una traiettoria discendente senza tagliare i servizi          │ Obiezioni (8)      │
│ ┃ essenziali?   Perché ora ▸   Vincoli ▸                        │ Pareri (8)         │
│ LA RISPOSTA IN BREVE                                            │ Ministri (9)       │
│ Riserva per il risanamento di 1,15 mld l'anno a regime; le      │ Mandati (9)        │
│ coperture si contano al minimo; il gettito della lotta          │ Fonti e integrità  │
│ all'evasione va al deficit; sanità, scuola e sicurezza si       │                     │
│ riorganizzano, non si riducono.  Leggi l'indirizzo del capo ▸   │ [Chiedi un riesame] │
├────────────────────────────────────────────────────────────────┤ membri del progetto │
│ DECISIONI   ███████████████████████████████████░░░░▒           └─────────────────────┘
│             46 adottate          6 respinte  1 rinviata
│ [Tutte 53] [Adottate 46] [Respinte 6] [Rinviate 1]   [⌕ filtra per proposta]
│ ┌──────────────────────────────────────────────────────────────┐
│ │ 02-C2 Nido esigibile + congedo paterno                        │
│ │ Essenziale ●●○  ‹✓ Adottata›  Regola: nucleo robusto (n. 8)   │
│ │ Cambia la copertura dell'art. 6: niente soppressione della    │
│ │ decontribuzione per le madri (linea rossa Equità)… Leggi ▸    │
│ └──────────────────────────────────────────────────────────────┘
│ DEROGHE DALL'ESITO DEL MOTORE (30)
│ ┃ 01-P3  Il motore indicava Piena → Essenziale. "La parte che la distingue
│ ┃        non può partire prima dell'autorizzazione UE." Libera 0,07 mld/anno.
│ OBIEZIONI DELL'OPPOSIZIONE LEALE (8)
│ ┌──────────────────────────────────────────────────────────────┐
│ │ 02-C2 Essenziale · copertura art. 6 su RIORDINO_BONUS 1,0 mld │
│ │ OBIEZIONE  Copertura non certificabile, costo spostato sui    │
│ │            redditi medio-bassi senza compensazione piena.     │
│ │ PROVA      coperture_menu.csv RB05 · Carta, linea rossa EQU ▸ │
│ │ CAMBIEREBBE IDEA SE  un allegato RGS arriva a 1,0 mld senza…  │
│ │ RISPOSTA DEL CAPO  ‹! Non registrata› vedi decisione 02-C2 ›  │
│ └──────────────────────────────────────────────────────────────┘
│ ▸ Pareri degli esperti (8)    ▸ Posizioni dei ministri (9)
│ MANDATI (9)  M011 Ministro dell'economia · entro 31/1/2027 · riconciliazione 7,37 mld ▸
│ 57 previsioni registrate, verificate alla scadenza con i dati ufficiali › Credibilità
│ Registrato nella catena di integrità · anello n. 8 · f9ecf15b4ac3… ⓘ
```

**Mobile**
```
┌─────────────────────────────────┐
│ ◇ Simulazione · non in vigore  ⓘ│
│ ‹ Sedute                         │
│ 8 NOV 2026 · A RICHIESTA         │
│ Conti in ordine senza tagliare   │
│ i servizi essenziali             │
│ ‹✓ Confermata oggi›              │
│ ①──②──③──④  Esperti › Capo       │
│ [In questa pagina ▾]             │
├─────────────────────────────────┤
│ La domanda                       │
│ ┃ Qual è il piano 2027-2029 per  │
│ ┃ riportare il debito…  Altro ▸  │
│ La risposta in breve             │
│ ~~ 3 righe ~~                    │
├─────────────────────────────────┤
│ Decisioni                        │
│ ████████████████░▒  46 · 6 · 1   │
│ [Tutte][Adottate][Respinte][Rinv]│ ← scorre
│ ┌─────────────────────────────┐ │
│ │02-C2 Nido esigibile…         │ │
│ │Essenziale ●●○ ‹✓ Adottata›   │ │
│ │Regola 8 · nucleo robusto  ›  │ │
│ └─────────────────────────────┘ │
├─────────────────────────────────┤
│ Deroghe (30)           sempre    │
│ Obiezioni (8)          aperte    │
│ ▸ Pareri degli esperti (8)       │
│ ▸ Posizioni dei ministri (9)     │
│ ▸ Mandati (9)                    │
└─────────────────────────────────┘
```

---

## 5. Dati (cruscotto)

**Obiettivo.** Come sta l'Italia secondo i dati ufficiali più recenti, che cosa preoccupa (allerte), che cosa ne fa il programma.

**Esempio reale**: 14 indicatori. Inflazione 5,6% (ott 2026, provvisorio, ▲ +1,4; +4,3 in 12 periodi) · Disoccupazione 6,3% (set 2026, ▲ +0,1) · Disoccupazione under 25 19,9% (▼ −0,4, favorevole) · Rendimento BTP decennale 4,36% · Spread IT-DE 88,9 pb (▲ +8,8) · PIL reale 0,0% sul trimestre (III trim 2026) · Debito 139,9% del PIL (II trim 2026, provvisorio) · Produzione industriale 92,8 (2021=100) · Fiducia dei consumatori −23,3 · Debito annuo 136,7% (2025) · Saldo di bilancio −3,1% · Spesa per interessi 3,8% · NEET 13,3% (▼ −1,9) · Fecondità 1,18 figli per donna. Allerte: inflazione alta, inflazione in salita, debito in salita, fiducia in calo.

**Gerarchia**: risposta ("4 allerte attive su 14 indicatori: inflazione e debito in salita, fiducia in calo") → allerte (con effetto sul programma) → indicatori raggruppati per tema (Prezzi e conti pubblici · Lavoro e giovani · Crescita · Società) → nota del giorno → obiettivi e diario.

**Componenti**: `CardIndicatore` (valore, unità, periodo, trend con segno e giudizio "favorevole/sfavorevole", minigrafico, fonte, badge *Provvisorio*), `Avviso` (allerta), `GraficoSerie` (pagina dell'indicatore), `TabellaDati` con [Scarica CSV].

**Stati**: indicatore con `stato` diverso da "ok" → card grigia "Dato non disponibile: la fonte non ha risposto il 8/11. Ultimo valore: …" • serie storica assente → si mostra solo il valore, senza minigrafico (mai una linea inventata) • nessuna allerta → riquadro favorevole.

```
DESKTOP
Dati
4 allerte attive su 14 indicatori: inflazione e debito in salita, fiducia in calo.
[Indicatori] [Allerte 4] [Obiettivi e risultati] [Diario quotidiano]
┌────────────────────────────────────────────┬─────────────────────────────────────────┐
│┃‹Alto› Inflazione sopra il 3%              │┃‹Alto› Debito/PIL +1,3 punti in un trim. │
│┃ Che cosa fa il programma: rivaluta le     │┃ Applicata la regola Futuro: nessuna     │
│┃ varianti a sostegno dei redditi.          │┃ variante a debito. Sospesa: 07-C5       │
│┃ Priorità: 02-C1 02-C4 04-P2 04-P3         │┃                                         │
└────────────────────────────────────────────┴─────────────────────────────────────────┘
PREZZI E CONTI PUBBLICI
┌──────────────────────┐┌──────────────────────┐┌──────────────────────┐┌──────────────────────┐
│Inflazione (HICP)     ││Debito pubblico       ││Spread IT-DE          ││Spesa per interessi   │
│ott 2026 · Provvisorio││II trim 2026 · Provv. ││set 2026              ││2025                  │
│5,6 %                 ││139,9 % PIL           ││88,9 pb               ││3,8 % PIL             │
│▲ +1,4 sfavorevole    ││▲ +1,3 sfavorevole    ││▲ +8,8 sfavorevole    ││▼ −0,1 favorevole     │
│╱╲__╱‾‾  minigrafico  ││                      ││                      ││                      │
│Eurostat ⓘ            ││Banca d'Italia ⓘ      ││BCE ⓘ                 ││Eurostat ⓘ            │
└──────────────────────┘└──────────────────────┘└──────────────────────┘└──────────────────────┘
LAVORO E GIOVANI   …   CRESCITA   …   SOCIETÀ   …
Nota del giorno (livello AI) · 8/11/2026 · ⓘ generata automaticamente, controllata da regole ▸
```
Mobile: allerte come elenco compatto; indicatori in **una colonna** di card orizzontali (nome e periodo a sinistra, valore e trend a destra), minigrafico sotto; gruppi richiudibili.

```
┌─────────────────────────────────┐
│ Inflazione (HICP)       5,6 %   │
│ ott 2026 · Provv.   ▲ +1,4 sfav.│
│ ╱╲__╱‾‾                    ⓘ   │
└─────────────────────────────────┘
```

---

## 6. Controlli › Europa

**Obiettivo.** Che cosa chiede l'Unione europea all'Italia, entro quando, dove siamo in ritardo, che cosa c'entra con il programma.

**Esempio reale** (`europa/`, 8/11/2026): **143 direttive** con termine di recepimento monitorate (23 a priorità critica, 10 alta, 94 media, 16 bassa); **84 procedure d'infrazione** aperte (48 messe in mora di cui 3 complementari, 19 pareri motivati, 4 ricorsi, 10 sentenze, 3 messe in mora per mancata esecuzione di sentenza; 21 per mancato recepimento, 63 per violazione del diritto UE); **procedura per disavanzo eccessivo aperta** dal 26/7/2024 (Decisione (UE) 2024/2124); tetto di crescita della spesa netta 1,9% nel 2027; **298 atti** UE negli ultimi 30 giorni (88 *obbligo*, 10 *opportunità*, 1 *vincolo di bilancio*, 199 *informativo*).

**Gerarchia**
1. Risposta: "Nei prossimi 60 giorni scadono 6 obblighi di recepimento; l'Italia ha 84 procedure d'infrazione aperte; la procedura per disavanzo eccessivo è in corso."
2. Schede: **Scadenze** · **Infrazioni** · **Semestre europeo** · **Novità**.
3. Scadenze: `TimelineScadenze` (prossimi 90 giorni) + elenco filtrabile per priorità, stato (in termine / scaduto / infrazione aperta), area, proposta collegata.
4. Infrazioni: `ScalaFasi` (messa in mora → parere motivato → ricorso → sentenza → sentenza art. 260, con sanzioni) + elenco.
5. Semestre: stato della procedura per disavanzo, percorso della spesa netta (grafico a barre: tetto vs previsione), raccomandazioni, calendario del ciclo di bilancio.
6. Novità: atti per impatto (obbligo, vincolo di bilancio, opportunità, informativo) e per area.

**Componenti**: `ChipGravita` (critica/alta/media/bassa = critico/alto/attenzione/neutro), `ChipStatoUE`, `TimelineScadenze`, `ScalaFasi`, `RigaAtto` (titolo breve in italiano semplice + titolo ufficiale richiudibile + CELEX + link EUR-Lex e misure nazionali), `GraficoBarre`.

**Regola di linguaggio**: i titoli UE sono lunghissimi ("Direttiva (UE) 2024/2831 del Parlamento europeo e del Consiglio, del 23 ottobre 2024, relativa al miglioramento…"). Si mostra un **titolo breve in italiano semplice** ("Lavoro tramite piattaforme digitali") e il titolo ufficiale sotto, richiuso.

**Stati**: fonte non raggiunta (es. EUR-Infra) → chip ‹Fonte non aggiornata› sulla scheda e data dell'ultimo dato • nessuna scadenza nei 90 giorni → "Nessun obbligo di recepimento scade nei prossimi 90 giorni." • completezza non verificata (80 casi "termine scaduto, misure notificate") → chip ‹Da verificare› con spiegazione: "L'Italia ha notificato misure, ma nessuno ha ancora verificato che siano complete."

```
DESKTOP
Controlli › Europa
Nei prossimi 60 giorni scadono 6 obblighi di recepimento. Infrazioni aperte: 84.
Procedura per disavanzo eccessivo: in corso.                       Aggiornato 8/11 14:33 ⓘ
[Scadenze 143] [Infrazioni 84] [Semestre europeo] [Novità 298]
┌──────────────────┐┌──────────────────┐┌──────────────────┐┌──────────────────┐
│ IN SCADENZA ≤60 g ││ GIÀ SCADUTE       ││ INFRAZIONI        ││ DISAVANZO        │
│ 6                 ││ 103               ││ 84 aperte         ││ ‹Alto› in corso  │
│ 5 senza misure IT ││ 80 da verificare  ││ 10 a sentenza     ││ dal 26/7/2024    │
└──────────────────┘└──────────────────┘└──────────────────┘└──────────────────┘
PROSSIMI 90 GIORNI
 nov ───────●──────────●──── dic ──●─────●────────────────●── gen ───────────
           23/11      30/11       2/12  9/12             31/12
        Dir. 2024/1260  parere   2024/2831 2024/2853      ViDA 2025/516
[Priorità ▾] [Stato ▾] [Tema ▾] [Collegate al programma ✓]
┌───────────────────────────────────────────────────────────────────────────────────────┐
│ ‹Alto› 23 nov 2026 · tra 15 giorni                         ‹In termine · nessuna misura│
│ Recupero e confisca dei beni                               italiana notificata›        │
│ Direttiva (UE) 2024/1260 · CELEX 32024L1260 ▸ titolo ufficiale                         │
│ Collegata a: 07-C2 Pena utile · 07-C4 Dal bene confiscato al bene comune               │
│ EUR-Lex ↗  Misure nazionali ↗                                                          │
├───────────────────────────────────────────────────────────────────────────────────────┤
│ ‹Critico› Termine scaduto il 30/12/2024 · 678 giorni fa      ‹Infrazione aperta:      │
│ Antiriciclaggio · Direttiva (UE) 2015/849                    messa in mora›           │
│ Procedure 2025/0276, 2022/2150 · Collegata a: 06-C6                                   │
└───────────────────────────────────────────────────────────────────────────────────────┘
INFRAZIONI — a che punto sono
Messa in mora ████████████████████████ 48 → Parere motivato ██████████ 19 → Ricorso ██ 4
→ Sentenza ███ 5 → Messa in mora art. 260 ██ 3 → Sentenza art. 260 (sanzioni) ███ 5
```
Mobile: le 4 cifre in griglia 2×2; la timeline diventa un **elenco per data** con intestazioni di mese; ogni scadenza è una card con chip gravità, data relativa ("tra 15 giorni") e collegamenti.

---

## 7. Controlli › Costituzione

**Obiettivo.** Sapere se proposte, leggi e manovre rispettano la Costituzione, con quale livello di rischio, su quali articoli e con quali precedenti della Corte costituzionale. L'AI **segnala** rischi; solo la Corte decide.

**Livelli di rischio** (scala unica, `04_design_system.md` §5.3):

| Livello | Chip | Significato | Equivalente nella verifica attuale |
|---|---|---|---|
| 0 | ‹✓ Nessun rilievo› favorevole | Nessun profilo critico individuato | *compatibile* |
| 1 | ‹! Attenzione› ambra | Regge a condizioni precise (da scrivere nel testo) | *condizionato*, *richiede notifica* |
| 2 | ‹▲ Rischio alto› mattone | Profili seri, precedenti della Corte sfavorevoli | — |
| 3 | ‹⨯ Rischio critico› vinaccia | Probabile illegittimità; per le proposte GovernAI è linea rossa | *incompatibile* |
| — | ‹○ Non esaminato› neutro | Esame non ancora svolto | — |

**Esempi**: proposte del programma — controllo costituzionale per proposta: 3 *compatibili*, 30 *condizionate*, 29 *richiedono notifica*; per variante: 2 *incompatibili* (04-P3 Piena, 08-P3 Piena), quindi escluse automaticamente. Leggi e manovre — **A.C. 3174, disegno di legge di bilancio 2027**, presentato il 30/10/2026, articolato in `costituzione/testi/AC3174_articolato.txt` **(esame reale: lo screening automatico segnala 13 articoli a rischio alto e 23 da approfondire su 137; l'esame approfondito conferma 5 dubbi seri e nessuna illegittimità certa)**.

**Gerarchia**
1. Avvertenza fissa: "Questo è un controllo preventivo automatico con revisione umana. Non è un giudizio: solo la Corte costituzionale decide."
2. Risposta: "A.C. 3174: esaminati N articoli, X con rischio alto, Y con attenzione."
3. Schede: **Leggi e manovre** · **Proposte del programma** · **Come leggiamo** (metodo e fonti).
4. Pagina di un atto: `BarraRischio` (distribuzione degli articoli per livello) → elenco articoli ordinati per rischio → per ciascuno: articoli della Costituzione coinvolti, ragionamento, **precedenti della Corte** verificati sui dati aperti (`dati.cortecostituzionale.it`, licenza CC BY-SA 3.0), condizioni per rimediare.

**Componenti**: `ChipRischio`, `BarraRischio`, `RigaEsame`, `CitazioneNorma` (art. 81 Cost. → testo al tocco), `CardPrecedente` (numero/anno, ECLI, esito in una frase, badge *Verificato sui dati della Corte*), `Avviso` informativo.

**Stati**: atto non ancora esaminato → "Esame in corso. Di solito richiede 1-2 giorni dalla pubblicazione del testo." • precedente non verificato → badge ‹Da verificare›, mai mostrato come certo • testo dell'atto cambiato dopo l'esame → ‹Attenzione› "Il testo è cambiato il …: l'esame si riferisce alla versione precedente."

```
DESKTOP
Controlli › Costituzione › Leggi e manovre
ⓘ Controllo preventivo automatico con revisione umana. Non è un giudizio: decide solo la Corte costituzionale.
A.C. 3174 · Disegno di legge di bilancio 2027
Presentato il 30/10/2026 · Esame del 8/11/2026 · testo: documenti.camera.it ↗
┌──────────────────────────────────────────────────────────────────────────────────┐
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓█                        │ BarraRischio
│ Nessun rilievo 101      Attenzione 23       Rischio alto 13  Critico 0            │ (testo sempre)
└──────────────────────────────────────────────────────────────────────────────────┘
[Tutti] [Rischio alto 13] [Attenzione 23]   Ordina: per rischio ▾   [⌕ articolo o parola]
┌──────────────────────────────────────────────────────────────────────────────────┐
│ ‹▲ Dubbio serio›  Art. 21 · Maggiorazione IRAP per le imprese energetiche          │
│ Costituzione: art. 53 (capacità contributiva) · art. 3 (uguaglianza)               │
│ Perché: colpisce tutto il valore della produzione, non gli extraprofitti; il       │
│ divieto di scaricare il costo sui prezzi non ha controlli né sanzioni.             │
│ Precedenti: Corte cost. 10/2015 ✓ (Robin tax) · 111/2024 ✓                        │
│ Come rimediare: base imponibile sugli extraprofitti e vigilanza ARERA. Dettagli ▸ │
└──────────────────────────────────────────────────────────────────────────────────┘
```
Mobile: barra del rischio a tutta larghezza con legenda sotto **in elenco** (mai solo colori); articoli come card; i precedenti in un cassetto dal basso.

---

## 8. Programma › I tuoi valori (simulatore)

**Obiettivo.** Provare quanto conta ciascuno dei 10 valori e vedere come cambia la classifica, capendo che il *nucleo robusto* resta in cima con qualunque peso.

**Gerarchia**: spiegazione in 2 righe → preimpostazioni (Pesi uguali, Più futuro, Più benessere, Più equità, Più sicurezza…) → 10 cursori + 3 orizzonti (breve, medio, lungo; regola della Carta: il lungo pesa almeno quanto il breve) → classifica con spostamenti (▲3, ▼2, =) → messaggio di sintesi (spostamenti nel wireframe **[illustrativi]**; "Con i tuoi pesi le prime 10 includono 8 proposte del nucleo robusto") → [Condividi i miei pesi] (nell'URL, nessun dato salvato).

**Componenti**: `Cursore` (con valore numerico e definizione del valore al tocco), `ControlloSegmentato` (preimpostazioni), `RigaClassifica` (posizione, titolo, chip classe, barra, spostamento), `Avviso` informativo.

**Neutralità**: le preimpostazioni hanno nomi di **valori**, mai di schieramenti ("Più equità", non "Profilo progressista"). Ordine delle preimpostazioni = ordine della Carta.

**Stati**: tutti i cursori a zero → "Dai almeno un po' di peso a un valore per vedere la classifica." • lungo < breve → il cursore si adegua e lo dice ("Lungo periodo portato a 30: la Carta chiede che pesi almeno quanto il breve.") con `aria-live`.

```
DESKTOP                                                   MOBILE
┌─────────────────────────┬──────────────────────────────┐ ┌──────────────────────────────┐
│ I TUOI PESI              │ CLASSIFICA                    │ │ I tuoi valori                │
│ [Uguali][Più futuro]…    │  1 Prevenire costa meno ‹✓› ▲2│ │ [Uguali][Più futuro][Più …›  │
│ Rispetto e diversità  50 │  2 Restare è possibile  ‹✓›  =│ │ ▸ Regola i 10 pesi (aperto)  │
│ ──────●─────────         │  3 Nessuno escluso      ‹✓› ▼1│ │ ──────────────────────────── │
│ Fiducia e trasparenza 50 │  4 IVA in tempo reale   ‹✓› ▲4│ │ Classifica                   │
│ …                        │  …                            │ │ 1 Prevenire costa meno ‹✓›▲2 │
│ ORIZZONTI                │ Con i tuoi pesi 8 delle prime │ │ 2 Restare è possibile  ‹✓› = │
│ Breve 30 Medio 30 Lungo 40│ 10 sono del nucleo robusto.   │ │ …                            │
│ [Condividi i miei pesi]  │                               │ │ [Condividi i miei pesi]      │
└─────────────────────────┴──────────────────────────────┘ └──────────────────────────────┘
```
Su mobile i cursori stanno in un pannello richiudibile sopra la classifica; mentre si trascina, una barra fissa in basso mostra "Prime 3: …" per vedere l'effetto senza scorrere.

---

## 9. Partecipa

**Obiettivo.** Fare una proposta o una domanda in meno di 3 minuti e sapere che fine fa.

**Gerarchia**
1. Risposta: "Chiunque può proporre un'idea o fare una domanda al Consiglio. Serve un account GitHub gratuito. Un membro del progetto legge ogni richiesta."
2. Tre azioni come card grandi: **Proponi un'idea** (→ analisi con diagnosi e 3 opzioni) · **Fai una domanda al Consiglio** (→ seduta) · **Segnala un errore** (→ correzione).
3. `PercorsoRichiesta`: Invii → Revisione umana → In coda → Analizzata/Discussa → Pubblicata. Con tempi indicativi.
4. Che cosa scrivere (esempio compilato).
5. Richieste e analisi pubblicate (stato vuoto oggi: 0 analisi).
6. Per i membri del progetto (richiesta diretta, convoca, riesame) — sezione distinta, stile secondario.
7. Regole: niente dati personali di terzi, rispetto, cosa non viene accettato.

**Componenti**: `CardAzione`, `PercorsoRichiesta`, `ChipStatoRichiesta`, `Avviso` informativo ("Si apre GitHub in una nuova scheda"), `ElencoRichieste`.

**Stati**: nessuna analisi pubblicata (oggi) → "Ancora nessuna analisi pubblicata: la prima la avvii tu." + [Proponi un'idea] • link GitHub non configurato → pulsanti disattivati con spiegazione.

```
MOBILE                               DESKTOP: le 3 card affiancate, percorso orizzontale
┌─────────────────────────────────┐
│ Partecipa                        │
│ Chiunque può proporre. Serve un  │
│ account GitHub gratuito ⓘ        │
│ ┌─────────────────────────────┐ │
│ │ 💡→ icona lightbulb          │ │
│ │ Proponi un'idea              │ │
│ │ Ricevi una diagnosi e tre    │ │
│ │ opzioni con costi e valori.  │ │
│ │ [Proponi un'idea ↗]          │ │
│ └─────────────────────────────┘ │
│ ┌ Fai una domanda al Consiglio ┐ │
│ ┌ Segnala un errore            ┐ │
│ Che fine fa la tua richiesta     │
│ ① Invii  ② Revisione umana       │
│ ③ In coda ④ Analisi ⑤ Pubblicata │
│ Richieste pubblicate (0)         │
│ Ancora nessuna: la prima la      │
│ avvii tu.                        │
│ ▸ Per i membri del progetto      │
└─────────────────────────────────┘
```

---

## 10. Metodo e Controlli › Integrità

### 10.1 Metodo

**Obiettivo.** Capire come funziona in 7 passi e trovare il documento giusto per approfondire.

**Gerarchia**: "L'AI propone e verifica. Le persone decidono." → `PassiMetodo` (7: Dati ufficiali ogni giorno · Valori dichiarati · Panel indipendente · Robustezza, non un peso unico · Senza deficit · Impara dai risultati · Verificabile) → Carta dei 10 valori (card per valore con definizione breve e linea rossa) → Documenti (Programma, Carta, Quadro giuridico e UE, Confronto internazionale, Confronto con i partiti, Rischio negli appalti, Legislazione, Metodo degli agenti, Sistema dinamico) → **Limiti dichiarati** (i costi sono stime da validare con UPB e Ragioneria; le analisi distributive richiedono microdati; i punteggi del panel sono giudizi strutturati) → Glossario.

**Componenti**: `PassiMetodo`, `CardValore` (codice, nome, definizione, ‹Linea rossa›), `LettoreDocumento` (indice a lato, tabelle scorrevoli), `ElencoLimiti`, `Glossario`.

### 10.2 Integrità

**Obiettivo.** Dimostrare che nessuno ha cambiato di nascosto dati, regole o risultati.

**Esempio reale**: catena **integra**, **9 anelli**, ultimo anello n. 8 del 8/11/2026 13:04 UTC, evento *aggiornamento* (allerte 4), impronta `f9ecf15b4ac376140d24a0aa38fd82a2eeb11c6086ee0a15185a0a93893164dd`, precedente `35cb75fa44b3…`, regole cambiate: nessuna.

**Gerarchia**: stato in grande (‹✓ Catena integra› / ‹⨯ Problemi rilevati›) → che cosa significa in 2 righe → `CatenaAnelli` (ultimi anelli come blocchi collegati) → come verificare da soli (`python integrita/catena.py --verifica`, con [Copia]) → regole cambiate nel tempo.

**Componenti**: `StatoIntegrita`, `CatenaAnelli` (n., data, evento, impronta abbreviata con [Copia], radici regole/input/output richiudibili), `BloccoCodice`, `ChipGravita`.

**Stati**: errori nella catena → `Avviso` critico in **tutte** le pagine + elenco errori; nessun anello → "La catena parte con il primo aggiornamento."

```
DESKTOP
Controlli › Integrità
┌───────────────────────────────┐  Ogni aggiornamento aggiunge un anello con l'impronta
│ ✓ Catena integra              │  (SHA-256) di regole, dati e risultati, e l'impronta
│ 9 anelli · nessuna            │  dell'anello precedente. Cambiare il passato spezza la
│ manomissione rilevata         │  catena. Le regole che cambiano sono sempre dichiarate.
└───────────────────────────────┘
 ┌────────────┐   ┌────────────┐   ┌────────────┐
 │ n. 8       │◀──│ n. 7       │◀──│ n. 6       │◀── …
 │ 8/11 13:04 │   │ …          │   │ …          │
 │ aggiorna-  │   │            │   │            │
 │ mento      │   │            │   │            │
 │ f9ecf15b…⧉ │   │ 35cb75fa…⧉ │   │            │
 │ regole: =  │   │            │   │            │
 └────────────┘   └────────────┘   └────────────┘
Verifica da solo:  $ python integrita/catena.py --verifica        [Copia]
```
Mobile: gli anelli diventano un elenco verticale con connettore a sinistra; impronte troncate a 12 caratteri con [Copia] (impronta completa nel valore copiato e nell'`aria-label`).

---

## 11. Matrice componenti × schermate

| Componente | Oggi | Programma | Scheda | Governo | Verbale | Dati | Europa | Costituzione | Valori | Partecipa | Metodo/Integrità |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ChipGravita / ChipRischio | ● | ● | ● | ● | ● | ● | ● | ● | | | ● |
| BadgeVerifica | ● | ● | ● | | ● | ● | ● | ● | | | ● |
| CardProposta | ● | ● | | | | | | | ● | | |
| MisuratoreVariante | | ● | ● | | ● | | | | | | |
| CardIndicatore | ● | | ● | | | ● | | | | | |
| Timeline (sedute/scadenze/anelli) | ● | | ● | ● | ● | | ● | | | ● | ● |
| BannerSimulazione | | | ● | ● | ● | | | | | | |
| Sezione richiudibile + IndicePagina | | | ● | | ● | | | ● | ● | | ● |
| CollegatoA | | | ● | | ● | ● | ● | ● | | | |
