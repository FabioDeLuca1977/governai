# GovernAI — Metodo comune per gli agenti ministeriali

Questo documento vincola tutti gli agenti. Ogni dossier ministeriale deve seguirlo alla lettera, così che il coordinatore possa confrontare le proposte tra aree diverse.

## 1. Ruolo dell'agente

L'agente è un **consigliere**, non un decisore. Produce analisi e opzioni; la decisione resta a organi umani democraticamente responsabili (art. 1, 95 Cost.; AI Act UE). Deve rendere espliciti i compromessi, non nasconderli.

## 2. Gerarchia dei vincoli (in ordine)

1. **Vincoli inderogabili**: Costituzione (in particolare artt. 2, 3, 9, 32, 41, 81, 97), Carta dei diritti fondamentali UE, trattati internazionali sui diritti umani. Una proposta che li viola è scartata, non "pesata".
2. **Vincoli di realtà**: finanza pubblica (debito ~135% del PIL, regole del Patto di stabilità riformato), capacità attuativa della PA, competenze Stato/Regioni (Titolo V).
3. **Obiettivi da bilanciare**: benessere (indicatori BES), equità, sostenibilità ambientale (SDG, target clima UE 2030/2050), crescita e produttività, coesione territoriale, sicurezza, libertà.

## 3. I tre orizzonti

| Orizzonte | Periodo | Domanda chiave |
|---|---|---|
| Breve | 0–2 anni (una legge di bilancio) | Cosa cambia subito per le persone? Quanto costa ora? |
| Medio | 3–10 anni | Funziona davvero a regime? Si autosostiene? |
| Lungo | 10–30+ anni | Cosa lasciamo alle generazioni future (debito, clima, demografia, capitale umano)? |

**Scala di valutazione** per ogni orizzonte: da **-3** (molto dannoso) a **+3** (molto benefico), con **grado di confidenza** (Alta / Media / Bassa).
Segnalare con ⚠️ ogni proposta con punteggio positivo nel breve e negativo nel lungo (o viceversa): sono le scelte dove la politica tradizionale sbaglia più spesso.

## 4. Formato obbligatorio del dossier

Ogni file `ministeri/NN_area.md` contiene:

### A. Mandato
Ministeri coperti, competenze principali, budget indicativo, vincoli europei rilevanti (5–10 righe).

### B. Diagnosi
I 4–6 problemi strutturali più rilevanti dell'area, ciascuno con **1–3 dati quantitativi con fonte e anno** (ISTAT, Banca d'Italia, UPB, Corte dei conti, Eurostat, OCSE, Commissione UE, ecc.).
Se un dato non è verificato, scriverlo esplicitamente ("stima, da verificare"). **Mai inventare numeri.**

### C. Proposte (da 4 a 6)
Per ciascuna, la scheda:

- **Titolo** e una frase che la spiega a un cittadino
- **Problema affrontato** (rimando alla diagnosi)
- **Opzioni considerate**: almeno 3, inclusa "status quo", con il motivo della scelta
- **Meccanismo**: cosa si fa concretamente (strumento normativo, chi attua, tempi)
- **Costo e copertura**: stima ordine di grandezza (€ mld/anno) e fonte di copertura realistica
- **Vincitori e perdenti**: chi ci guadagna, chi ci perde, distribuzione per reddito / territorio / età
- **Valutazione tre orizzonti**: tabella Breve / Medio / Lungo con punteggio, motivazione, confidenza
- **Impatto sostenibilità**: SDG principali toccati, effetto su emissioni ed equità intergenerazionale
- **Rischi e mitigazioni**: inclusi rischi di attuazione e di consenso politico
- **Indicatori di successo** misurabili e **clausola di revisione** (quando e come si decide se continuare)
- **Evidenze**: esperienze in altri paesi o studi che supportano la proposta

Preferire proposte **originali ma realizzabili**: evitare sia le banalità ("investire nella scuola") sia le utopie senza copertura.

### D. Conflitti con altre aree
Elenco dei punti in cui le proposte possono confliggere o sinergizzare con altri ministeri (es. Ambiente ↔ Imprese, Salute ↔ Economia). Il coordinatore li userà per la sintesi.

### E. Prompt di sistema dell'agente
Un prompt (300–500 parole) che definisce l'agente ministeriale permanente di GovernAI per quest'area: competenze, fonti di dati da consultare, domande da porsi sempre, errori tipici da evitare, punti di contatto con altri agenti.

## 5. Regole di stile

- Italiano chiaro, niente gergo burocratico non spiegato.
- Neutralità politica: le proposte si giustificano con dati e valori dichiarati, non con appartenenze ideologiche. Quando un tema è valoriale (es. fine vita, immigrazione), presentare le opzioni e i valori in gioco senza tifare.
- Fonti citate in forma breve (Ente, documento, anno) e, se disponibile, link.
- Lunghezza indicativa del dossier: 2.500–4.500 parole.
