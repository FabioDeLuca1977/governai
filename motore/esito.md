# GovernAI — Esito del motore decisionale

*Generato da `motore/decidi.py`. Metodo: analisi di accettabilità multicriterio stocastica (SMAA) sui 7 valori della Carta, con il panel indipendente come fonte dei punteggi.*

- Valutatori: **A, B, C**. Estrazioni: **20.000** combinazioni di pesi tra valori e orizzonti (lungo periodo ≥ breve).
- Accordo del panel (alfa di Krippendorff, intervalli): **0,84**. Sopra 0,67 l'accordo è accettabile per conclusioni provvisorie; sopra 0,80 è buono.
- Celle con disaccordo forte (escursione ≥ 3 punti): **0** su 1092.
- Proposte utili (effetto netto positivo) con almeno il 95% delle combinazioni di pesi: **51 su 52**. Quasi tutto è utile in sé: con risorse scarse conta la **priorità relativa**.
- Classi per priorità, in base alla probabilità di stare nella prima metà della classifica, P(1ª metà): **nucleo robusto** ≥ 75%; **dipendente dai valori** tra 25% e 75%; **in coda** ≤ 25%; **sfavorevole** se è utile in meno della metà delle combinazioni.

## Nucleo robusto (14)

In cima alla classifica qualunque sia il peso dato ai valori: il **nucleo condiviso** del programma.

| Proposta | Titolo | Utilità attesa | P(1ª metà) | P(top 25%) | Rango 5–95% | Costo | Valore/mld | Disacc. | Pacchetto 4 mld | Pacchetto 10 mld | Pacchetto 18 mld |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 03-P4 | Prevenire costa meno: fondo prevenzione e assicurazione catastrofale | 0,98 | 86% | 67% | 1–35 | 1,2 | 0,79 | 0,4 | 1% | 44% | 92% |
| 06-C2 | Patto per infermieri e medicina generale | 0,90 | 95% | 67% | 2–27 | 2,0 | 0,45 | 0,3 | 0% | 0% | 52% |
| 05-C4 | Piu' laureati e diplomati terziari: ITS, lauree professionalizzanti, residenze | 0,89 | 84% | 57% | 1–37 | 0,7 | 1,36 | 0,3 | 27% | 94% | 100% |
| 02-C2 | Nido esigibile + congedo paterno | 0,88 | 82% | 60% | 1–38 | 3,8 | 0,23 | 0,2 | 0% | 0% | 0% |
| 05-C3 | Carriere della ricerca | 0,87 | 75% | 53% | 1–40 | 3,1 | 0,28 | 0,3 | 0% | 0% | 9% |
| 09-C2 | Chiedilo una volta sola: once-only con rimborso automatico | 0,86 | 82% | 54% | 1–37 | 0,3 | 2,88 | 0,2 | 94% | 99% | 100% |
| 04-P3 | Prima il treno dei pendolari: fondo TPL e abbonamento unico | 0,84 | 86% | 54% | 2–35 | 2,2 | 0,37 | 0,4 | 0% | 0% | 18% |
| 09-C3 | Tecnici della Repubblica: pool di competenze per i piccoli enti | 0,83 | 82% | 50% | 2–36 | 0,6 | 1,51 | 0,3 | 42% | 97% | 100% |
| 04-P2 | Casa a canone giusto | 0,83 | 77% | 50% | 2–40 | 1,1 | 0,72 | 0,4 | 0% | 41% | 92% |
| 06-C3 | Case della Comunita' vive | 0,82 | 85% | 46% | 3–33 | 1,5 | 0,55 | 0,3 | 0% | 2% | 87% |
| 04-P6 | Restare e' possibile: servizi essenziali aree interne | 0,81 | 77% | 45% | 2–41 | 0,8 | 1,08 | 0,3 | 5% | 90% | 100% |
| 04-P4 | Nessuna grande opera senza prova dei numeri | 0,81 | 77% | 48% | 2–37 | 0,0 | — | 0,1 | 100% | 100% | 100% |
| 07-C1 | Giustizia a regime: Ufficio per il processo e triage digitale | 0,81 | 84% | 42% | 3–32 | 0,6 | 1,47 | 0,0 | 40% | 95% | 100% |
| 03-P3 | Ogni goccia conta: reti idriche e riuso | 0,77 | 75% | 36% | 4–37 | 0,8 | 1,03 | 0,3 | 1% | 88% | 98% |

## Priorità dipendente dai valori (29)

La posizione in classifica cambia molto con i pesi: **qui la scelta è politica**. La colonna finale indica quali valori la fanno salire.

| Proposta | Titolo | Utilità attesa | P(1ª metà) | P(top 25%) | Rango 5–95% | Costo | Valore/mld | Disacc. | Dipende soprattutto da | Pacchetto 4 mld | Pacchetto 10 mld | Pacchetto 18 mld |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 05-C1 | Nessuno escluso: squadre di prossimita' contro la dispersione | 0,85 | 75% | 51% | 1–43 | 0,2 | 3,40 | 0,3 | Apprendimento e cultura, Rispetto | 97% | 100% | 100% |
| 01-P3 | IVA in tempo reale | 0,74 | 63% | 37% | 2–42 | 0,0 | — | 0,2 | Fiducia, Responsabilità verso il futuro | 100% | 100% | 100% |
| 09-C1 | Stato a vetro: infrastruttura aperta per l'analisi delle politiche | 0,74 | 64% | 34% | 3–44 | 0,1 | 9,81 | 0,4 | Fiducia, Innovazione | 100% | 100% | 100% |
| 09-C5 | AI nella PA con le mani sul volante | 0,73 | 63% | 29% | 4–42 | 0,2 | 3,24 | 0,3 | Innovazione, Apprendimento e cultura | 96% | 99% | 100% |
| 07-C2 | Pena utile: misure di comunita' contro il sovraffollamento | 0,72 | 59% | 27% | 4–42 | 0,4 | 1,80 | 0,1 | Rispetto, Apprendimento e cultura | 63% | 99% | 100% |
| 07-C6 | Scudo cyber territoriale | 0,71 | 71% | 13% | 10–34 | 0,3 | 2,37 | 0,1 | Innovazione, Apprendimento e cultura | 95% | 100% | 100% |
| 02-C5 | Progetto di vita esigibile e lavoro per le persone con disabilita' | 0,70 | 53% | 30% | 2–46 | 1,2 | 0,56 | 0,1 | Rispetto, Benessere | 0% | 10% | 72% |
| 04-P1 | Patto di continuita' post-PNRR | 0,69 | 61% | 20% | 8–44 | 1,5 | 0,46 | 0,6 | Apprendimento e cultura, Bellezza, patrimonio e accoglienza | 0% | 2% | 71% |
| 05-C5 | Scuole aperte come presidi di comunita' | 0,68 | 57% | 21% | 7–45 | 0,4 | 1,70 | 0,1 | Apprendimento e cultura, Bellezza, patrimonio e accoglienza | 62% | 98% | 99% |
| 07-C3 | Governance dei flussi migratori fondata sui dati | 0,68 | 58% | 13% | 10–41 | 0,4 | 1,51 | 0,2 | Apprendimento e cultura, Rispetto | 30% | 98% | 100% |
| 06-C5 | Salute mentale al 5% | 0,67 | 51% | 26% | 5–48 | 3,1 | 0,21 | 0,2 | Benessere, Rispetto | 0% | 0% | 0% |
| 05-C2 | Conto personale di competenze | 0,67 | 51% | 20% | 5–46 | 1,2 | 0,54 | 0,2 | Apprendimento e cultura, Innovazione | 0% | 11% | 78% |
| 03-P1 | Dividendo climatico: riforma SAD restituita ai cittadini | 0,67 | 48% | 17% | 6–43 | 5,0 | 0,13 | 0,2 | Responsabilità verso il futuro, Innovazione | 0% | 0% | 0% |
| 02-C1 | Salario minimo contrattuale garantito | 0,65 | 46% | 18% | 6–46 | 0,4 | 1,63 | 0,3 | Rispetto, Benessere | 50% | 96% | 98% |
| 07-C4 | Dal bene confiscato al bene comune | 0,65 | 46% | 18% | 6–46 | 0,2 | 4,32 | 0,1 | Fiducia, Bellezza, patrimonio e accoglienza | 98% | 99% | 100% |
| 01-P6 | Turismo che ripaga i territori: tassa di soggiorno intelligente | 0,64 | 40% | 18% | 4–47 | 0,2 | 4,24 | 0,2 | Bellezza, patrimonio e accoglienza | 97% | 99% | 100% |
| 02-C6 | Bilancio generazionale e strategia demografica | 0,63 | 42% | 9% | 11–45 | 0,3 | 1,79 | 0,3 | Responsabilità verso il futuro, Apprendimento e cultura | 67% | 96% | 99% |
| 01-P2 | Spese fiscali a scadenza (sunset 5 anni) | 0,62 | 39% | 13% | 9–45 | 0,0 | — | 0,3 | Responsabilità verso il futuro, Fiducia | 100% | 100% | 100% |
| 02-C3 | Patto previdenziale tra generazioni | 0,62 | 38% | 20% | 3–49 | 0,0 | — | 0,0 | Responsabilità verso il futuro, Fiducia | 100% | 100% | 100% |
| 01-P1 | Bilancio generazionale: ogni legge dichiara chi paga e quando | 0,62 | 40% | 19% | 6–48 | 0,0 | — | 0,0 | Fiducia, Responsabilità verso il futuro | 99% | 100% | 100% |
| 01-P4 | Crescere conviene: eliminare i gradini dimensionali | 0,61 | 37% | 13% | 8–46 | 2,5 | 0,24 | 0,3 | Innovazione, Apprendimento e cultura | 0% | 0% | 2% |
| 06-C1 | Tempo garantito o rimborso | 0,61 | 41% | 16% | 6–48 | 0,8 | 0,81 | 0,5 | Rispetto, Benessere | 0% | 59% | 86% |
| 06-C6 | Dividendo della prevenzione e budget unico del farmaco | 0,60 | 38% | 8% | 12–47 | 0,0 | — | 0,0 | Responsabilità verso il futuro, Benessere | 100% | 100% | 100% |
| 03-P5 | Contratto agro-climatico | 0,60 | 35% | 10% | 9–47 | 0,4 | 1,49 | 0,2 | Bellezza, patrimonio e accoglienza, Innovazione | 43% | 94% | 99% |
| 03-P2 | Elettricita' rinnovabile a prezzo rinnovabile (CfD) | 0,59 | 39% | 19% | 5–51 | 0,2 | 3,91 | 0,3 | Responsabilità verso il futuro, Innovazione | 88% | 93% | 96% |
| 08-P1 | Legge sulla consulenza algoritmica pubblica | 0,57 | 30% | 5% | 13–48 | 0,0 | — | 0,3 | Innovazione, Responsabilità verso il futuro | 100% | 100% | 100% |
| 02-C4 | Reddito di inclusione universale | 0,56 | 36% | 18% | 5–51 | 2,5 | 0,23 | 0,1 | Rispetto, Benessere | 0% | 0% | 3% |
| 06-C4 | Budget di cura per la non autosufficienza | 0,56 | 30% | 10% | 10–50 | 2,0 | 0,28 | 0,1 | Benessere, Rispetto | 0% | 0% | 6% |
| 04-P5 | LEP prima: autonomia differenziata reversibile | 0,53 | 26% | 8% | 11–50 | 0,0 | — | 0,4 | Rispetto, Fiducia | 100% | 100% | 100% |

## In coda (8)

Utili, ma stabilmente in fondo alla classifica: **da migliorare o rinviare**.

| Proposta | Titolo | Utilità attesa | P(1ª metà) | P(top 25%) | Rango 5–95% | Costo | Valore/mld | Disacc. | Dipende soprattutto da | Pacchetto 4 mld | Pacchetto 10 mld | Pacchetto 18 mld |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 08-P4 | Beni pubblici europei: capacita' fiscale UE | 0,47 | 15% | 2% | 18–50 | 0,0 | — | 0,3 | Innovazione, Responsabilità verso il futuro | 100% | 99% | 100% |
| 05-C6 | AI a scuola | 0,47 | 17% | 3% | 16–51 | 0,2 | 2,07 | 0,3 | Innovazione, Apprendimento e cultura | 60% | 89% | 98% |
| 08-P2 | Patto per la buona legge | 0,47 | 17% | 5% | 14–51 | 0,0 | — | 0,2 | Fiducia, Responsabilità verso il futuro | 97% | 99% | 100% |
| 09-C4 | Cloud pubblico sostenibile e Patto per la manutenzione digitale | 0,43 | 3% | 0% | 28–50 | 0,4 | 1,07 | 0,1 | Innovazione, Responsabilità verso il futuro | 7% | 65% | 91% |
| 08-P3 | Regole del gioco stabili (legge elettorale, voto fuorisede) | 0,42 | 9% | 1% | 22–51 | 0,0 | — | 0,0 | Fiducia, Rispetto | 96% | 99% | 100% |
| 01-P5 | Energia a prezzo stabile per le PMI (PPA rinnovabili) | 0,38 | 6% | 1% | 25–51 | 0,8 | 0,51 | 0,2 | Responsabilità verso il futuro, Innovazione | 0% | 27% | 57% |
| 08-P5 | Cooperazione che si misura: traiettoria APS | 0,36 | 1% | 0% | 33–51 | 4,5 | 0,08 | 0,2 | Rispetto, Fiducia | 0% | 0% | 0% |
| 08-P6 | Export resiliente | 0,34 | 6% | 1% | 25–51 | 0,3 | 1,14 | 0,2 | Bellezza, patrimonio e accoglienza, Innovazione | 20% | 79% | 96% |

## Sfavorevoli (1)

Effetto netto negativo con la maggior parte delle combinazioni di pesi: **da ripensare**.

| Proposta | Titolo | Utilità attesa | P(1ª metà) | P(top 25%) | Rango 5–95% | Costo | Valore/mld | Disacc. | Dipende soprattutto da | Pacchetto 4 mld | Pacchetto 10 mld | Pacchetto 18 mld |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 07-C5 | Difesa: percorso NATO 3,5% vincolato a efficienza europea | -0,33 | 0% | 0% | 51–52 | 32,0 | -0,01 | 0,1 | Innovazione | 0% | 0% | 0% |

## Pacchetti per livello di budget

Per ogni livello di risorse permanenti (mld €/anno a regime) il motore sceglie l'insieme di proposte con più valore che sta nel budget, per ogni combinazione di pesi. La percentuale indica quanto spesso la proposta entra nel pacchetto.
Le proposte a costo zero o che generano risorse entrano sempre, se utili. Il budget va inteso **al netto** delle politiche invariate (10–14 mld/anno, `registro/`).
Il dividendo climatico (03-P1) ha un costo opportunità di 5 mld, cioè il gettito SAD che non finanzia altre proposte. Proposte più costose dell'intero budget (es. la Difesa, 32 mld) non possono entrare: la loro traiettoria è una decisione a parte.

### Budget 4 mld/anno

- **Entrano quasi sempre (≥80%)** — costo 1,7 mld: 09-C2 Chiedilo una volta sola: once-only con rimborso automatico, 05-C1 Nessuno escluso: squadre di prossimita' contro la dispersione, 04-P4 Nessuna grande opera senza prova dei numeri, 01-P3 IVA in tempo reale, 09-C1 Stato a vetro: infrastruttura aperta per l'analisi delle politiche, 09-C5 AI nella PA con le mani sul volante, 07-C6 Scudo cyber territoriale, 07-C4 Dal bene confiscato al bene comune, 01-P6 Turismo che ripaga i territori: tassa di soggiorno intelligente, 01-P2 Spese fiscali a scadenza (sunset 5 anni), 02-C3 Patto previdenziale tra generazioni, 01-P1 Bilancio generazionale: ogni legge dichiara chi paga e quando, 06-C6 Dividendo della prevenzione e budget unico del farmaco, 03-P2 Elettricita' rinnovabile a prezzo rinnovabile (CfD), 08-P1 Legge sulla consulenza algoritmica pubblica, 04-P5 LEP prima: autonomia differenziata reversibile, 08-P4 Beni pubblici europei: capacita' fiscale UE, 08-P2 Patto per la buona legge, 08-P3 Regole del gioco stabili (legge elettorale, voto fuorisede)
- **Entrano a seconda dei valori (20–80%)**: 02-C6 (67%), 07-C2 (63%), 05-C5 (62%), 05-C6 (60%), 02-C1 (50%), 03-P5 (43%), 09-C3 (42%), 07-C1 (40%), 07-C3 (30%), 05-C4 (27%), 08-P6 (20%)

### Budget 10 mld/anno

- **Entrano quasi sempre (≥80%)** — costo 7,6 mld: 05-C4 Piu' laureati e diplomati terziari: ITS, lauree professionalizzanti, residenze, 09-C2 Chiedilo una volta sola: once-only con rimborso automatico, 05-C1 Nessuno escluso: squadre di prossimita' contro la dispersione, 09-C3 Tecnici della Repubblica: pool di competenze per i piccoli enti, 04-P6 Restare e' possibile: servizi essenziali aree interne, 04-P4 Nessuna grande opera senza prova dei numeri, 07-C1 Giustizia a regime: Ufficio per il processo e triage digitale, 03-P3 Ogni goccia conta: reti idriche e riuso, 01-P3 IVA in tempo reale, 09-C1 Stato a vetro: infrastruttura aperta per l'analisi delle politiche, 09-C5 AI nella PA con le mani sul volante, 07-C2 Pena utile: misure di comunita' contro il sovraffollamento, 07-C6 Scudo cyber territoriale, 05-C5 Scuole aperte come presidi di comunita', 07-C3 Governance dei flussi migratori fondata sui dati, 02-C1 Salario minimo contrattuale garantito, 07-C4 Dal bene confiscato al bene comune, 01-P6 Turismo che ripaga i territori: tassa di soggiorno intelligente, 02-C6 Bilancio generazionale e strategia demografica, 01-P2 Spese fiscali a scadenza (sunset 5 anni), 02-C3 Patto previdenziale tra generazioni, 01-P1 Bilancio generazionale: ogni legge dichiara chi paga e quando, 06-C6 Dividendo della prevenzione e budget unico del farmaco, 03-P5 Contratto agro-climatico, 03-P2 Elettricita' rinnovabile a prezzo rinnovabile (CfD), 08-P1 Legge sulla consulenza algoritmica pubblica, 04-P5 LEP prima: autonomia differenziata reversibile, 08-P4 Beni pubblici europei: capacita' fiscale UE, 05-C6 AI a scuola, 08-P2 Patto per la buona legge, 08-P3 Regole del gioco stabili (legge elettorale, voto fuorisede)
- **Entrano a seconda dei valori (20–80%)**: 08-P6 (79%), 09-C4 (65%), 06-C1 (59%), 03-P4 (44%), 04-P2 (41%), 01-P5 (27%)

### Budget 18 mld/anno

- **Entrano quasi sempre (≥80%)** — costo 12,9 mld: 03-P4 Prevenire costa meno: fondo prevenzione e assicurazione catastrofale, 05-C4 Piu' laureati e diplomati terziari: ITS, lauree professionalizzanti, residenze, 09-C2 Chiedilo una volta sola: once-only con rimborso automatico, 05-C1 Nessuno escluso: squadre di prossimita' contro la dispersione, 09-C3 Tecnici della Repubblica: pool di competenze per i piccoli enti, 04-P2 Casa a canone giusto, 06-C3 Case della Comunita' vive, 04-P6 Restare e' possibile: servizi essenziali aree interne, 04-P4 Nessuna grande opera senza prova dei numeri, 07-C1 Giustizia a regime: Ufficio per il processo e triage digitale, 03-P3 Ogni goccia conta: reti idriche e riuso, 01-P3 IVA in tempo reale, 09-C1 Stato a vetro: infrastruttura aperta per l'analisi delle politiche, 09-C5 AI nella PA con le mani sul volante, 07-C2 Pena utile: misure di comunita' contro il sovraffollamento, 07-C6 Scudo cyber territoriale, 05-C5 Scuole aperte come presidi di comunita', 07-C3 Governance dei flussi migratori fondata sui dati, 02-C1 Salario minimo contrattuale garantito, 07-C4 Dal bene confiscato al bene comune, 01-P6 Turismo che ripaga i territori: tassa di soggiorno intelligente, 02-C6 Bilancio generazionale e strategia demografica, 01-P2 Spese fiscali a scadenza (sunset 5 anni), 02-C3 Patto previdenziale tra generazioni, 01-P1 Bilancio generazionale: ogni legge dichiara chi paga e quando, 06-C1 Tempo garantito o rimborso, 06-C6 Dividendo della prevenzione e budget unico del farmaco, 03-P5 Contratto agro-climatico, 03-P2 Elettricita' rinnovabile a prezzo rinnovabile (CfD), 08-P1 Legge sulla consulenza algoritmica pubblica, 04-P5 LEP prima: autonomia differenziata reversibile, 08-P4 Beni pubblici europei: capacita' fiscale UE, 05-C6 AI a scuola, 08-P2 Patto per la buona legge, 09-C4 Cloud pubblico sostenibile e Patto per la manutenzione digitale, 08-P3 Regole del gioco stabili (legge elettorale, voto fuorisede), 08-P6 Export resiliente
- **Entrano a seconda dei valori (20–80%)**: 05-C2 (78%), 02-C5 (72%), 04-P1 (71%), 01-P5 (57%), 06-C2 (52%)

## Linee rosse segnalate dal panel

| Proposta | Valore | Valutatore | Motivazione |
|---|---|---|---|
| 07-C5 | FUT | B | Fino a 32 mld annui con margine nullo e parte dichiarata a debito: rischio art. 81 ed emissioni |
| 02-C3 | RIS | C | Contributo di equità decennale sulle pensioni: rischio di incostituzionalità (sent. 234/2020 ne limitò la durata); tutela però i discontinui |
| 07-C5 | FUT | C | Circa 32 mld annui al 2035 in parte a debito senza margini di bilancio: rischio per art. 81 e generazioni future |

## Limiti

- I punteggi sono giudizi esperti strutturati, non misure: la loro qualità dipende dai dossier e dal panel.
- Il costo usato è il punto medio della stima; budget e costi a regime si riferiscono ad anni diversi.
- La scala da −3 a +3 è limitata: un grande programma nazionale e una piccola riforma possono ricevere punteggi simili. Il pacchetto per budget tende quindi a favorire le misure economiche. È coerente con la Carta (regola 6), ma le proposte costose con utilità alta vanno lette come **"entrano con più risorse"**, non come proposte di poco valore.
- L'alfa di Krippendorff è alto anche perché molte celle valgono 0 per tutti i valutatori: l'accordo sui punteggi diversi da zero è più basso.
- Il pacchetto rispetta il budget complessivo; la compatibilità con i singoli fondi va verificata con `registro/controlla.py`.
- La distribuzione dei pesi è uniforme: quando l'assemblea dei cittadini esprimerà i suoi pesi, diventeranno lo scenario centrale.
