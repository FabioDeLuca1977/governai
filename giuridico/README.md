# Verifica giuridica di GovernAI

Ogni misura del programma e ogni copertura passa una verifica di conformità da parte di tre esperti, ciascuno nel proprio ambito:

| Ambito | Cosa verifica |
|---|---|
| **FIS** – diritto tributario | IRPEF, IVA, accise, spese fiscali, contributi; limiti posti dalle direttive UE sull'IVA, sull'energia e sui tabacchi; aiuti di Stato in forma fiscale |
| **COS** – diritto costituzionale e amministrativo | Costituzione (in particolare artt. 3, 23, 38, 53, 81, 97, 117, 119); riparto di competenze Stato-Regioni; giurisprudenza della Corte costituzionale; leggi vigenti da modificare |
| **UE** – diritto e governance europea | Regole fiscali UE (Reg. 2024/1263 e percorso di spesa netta); aiuti di Stato (artt. 107-109 TFUE, GBER); AI Act, GDPR, PAC, coesione, ETS/ETS2, mercato interno; raccomandazioni del Semestre europeo |

## Esiti

| Esito | Significato | Effetto sul programma |
|---|---|---|
| `compatibile` | Nessun ostacolo giuridico | Nessuno |
| `condizionato` | Compatibile solo con le condizioni indicate (es. soglie, compensazioni, durata) | La misura va attuata rispettando le condizioni |
| `richiede_notifica` | Serve un passaggio formale: notifica alla Commissione, intesa in Conferenza Stato-Regioni, legge rinforzata | Allunga i tempi |
| `incompatibile` | Viola la Costituzione o il diritto UE nella forma proposta | **Esclusa in automatico** dall'ottimizzatore (linea rossa), salvo riformulazione |

## File

| File | Contenuto |
|---|---|
| `conformita.csv` | Una riga per elemento × ambito: `tipo` (proposta, variante o copertura), `id`, `ambito`, `esito`, `norme` (citazioni), `fonti` (link a Normattiva o EUR-Lex), `motivazione`, `condizioni` |
| `quadro.md` | I vincoli giuridici ed europei essenziali, letti dagli agenti prima di ogni nuova proposta o analisi |
| `note_*.md` | Le note di ciascun esperto |

La verifica è un supporto alla decisione, non un parere legale. Le misure da adottare richiedono comunque la valutazione degli uffici legislativi e, dove serve, dell'avvocatura.
