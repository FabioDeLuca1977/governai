# GovernAI — Registro unico delle coperture

Il registro rende **impossibile contare due volte la stessa risorsa**. Ogni fonte di copertura (un "fondo") ha una capienza verificata. Ogni proposta "preleva" da uno o più fondi. Lo script `controlla.py` somma i prelievi, segnala i fondi esauriti e calcola il saldo del programma rispetto al vincolo di bilancio.

## File

| File | Contenuto | Chi lo compila |
|---|---|---|
| `fondi.csv` | Le fonti di copertura con capienza verificata | Agente "vincolo di bilancio", da fonti ufficiali |
| `vincolo.csv` | Il vincolo complessivo: tetto alla spesa netta, politiche invariate, margini | Agente "vincolo di bilancio" |
| `prelievi.csv` | Per ogni proposta: costo e fondi da cui preleva | Agente "mappatura", dai dossier |
| `controlla.py` | Controllo automatico; scrive `bilancio.md` | — |
| `bilancio.md` | Risultato: fondi in eccesso, saldo, proposte scoperte | Generato |

Tutti gli importi sono in **miliardi di euro all'anno, a regime**, salvo diversa indicazione nella colonna `anno`.

## Schema di `fondi.csv`

| Colonna | Significato |
|---|---|
| `fondo_id` | Identificativo (vedi elenco sotto) |
| `descrizione` | Cosa è |
| `capienza_min`, `capienza_max` | Risorsa **nuova** disponibile per il programma, al netto di ciò che è già impegnato a legislazione vigente |
| `gia_impegnato` | Quanto è già destinato per legge o già contato nei documenti ufficiali |
| `natura` | `permanente` / `una_tantum` / `temporanea` / `incerta` |
| `certificazione` | `si` se la risorsa può coprire spese solo dopo certificazione ex post (es. lotta all'evasione) |
| `in_bilancio` | `si` se passa dal bilancio pubblico; `no` se è fuori bilancio (tariffe, bollette, fondi UE a gestione diretta) |
| `fonte_dato` | Ente, documento, anno, URL |
| `note` | Vincoli d'uso |

## Schema di `prelievi.csv`

| Colonna | Significato |
|---|---|
| `proposta_id` | Area e numero, es. `02-C2`, `06-C5` |
| `titolo` | Titolo breve |
| `costo_min`, `costo_max` | Costo lordo a regime |
| `anno_regime` | Anno in cui si raggiunge il costo a regime |
| `fondo_id` | Fondo da cui preleva (una riga per ogni fondo) |
| `prelievo_min`, `prelievo_max` | Quota del costo coperta da quel fondo |
| `fonte_costo` | `stima GovernAI` oppure fonte ufficiale |
| `note` | |

## Fondi ammessi (`fondo_id`)

| fondo_id | Descrizione |
|---|---|
| `SAD` | Riforma dei sussidi ambientalmente dannosi riformabili a livello nazionale |
| `SPESE_FISCALI` | Riordino delle spese fiscali **oltre** quanto già previsto nel Piano strutturale di bilancio |
| `ETS` | Proventi aste ETS (sistema attuale) |
| `ETS2_FSC` | Proventi ETS2 e Fondo sociale per il clima (dal 2027–28) |
| `IVA_EVASIONE` | Recupero dell'evasione IVA, solo dopo certificazione |
| `FSN` | Incremento programmato del Fondo sanitario nazionale |
| `COESIONE_2127` | Risorse coesione 2021–27 (FSC, FESR, FSE+) non ancora impegnate |
| `COESIONE_2834` | Risorse coesione del prossimo ciclo (QFP 2028–34) |
| `PENSIONI` | Contributo di equità sulle pensioni più alte e risparmi dall'uscita dalle "quote" |
| `TASSA_SOGGIORNO` | Gettito aggiuntivo della tassa di soggiorno (Comuni) |
| `ACCISE_SALUTE` | Accise e tasse su prodotti nocivi (tabacco, bevande zuccherate) |
| `RIORDINO_BONUS` | Riordino di bonus e carte frammentati |
| `FONDI_UE` | Fondi UE a gestione diretta o prestiti (SAFE, AMIF, Horizon, BEI) |
| `RIALLOCAZIONE` | Riallocazione interna al bilancio del ministero |
| `RISPARMI_ATTESI` | Risparmi attesi dalla misura stessa, non certificati |
| `TARIFFE` | Copertura fuori bilancio (bollette, tariffe idriche) |
| `DEFICIT` | Nuovo deficit, cioè debito |
| `ALTRO` | Da specificare in `note` |
