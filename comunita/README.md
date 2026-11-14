# Comunità su invito

Il programma di GovernAI resta leggibile da chiunque. La comunità è lo spazio dove gli iscritti discutono le proposte, prendono appunti e si confrontano tra loro e con l'AI. **Qui nessuno decide**: le idee che nascono nella discussione diventano proposte solo passando dagli stessi controlli di tutte le altre.

| File | Contenuto |
|---|---|
| `schema.sql` | Database, regole di accesso e funzioni (Supabase / PostgreSQL) |
| `regole.md` | Regole della comunità e della moderazione (mostrate nel sito) |
| `privacy.md` | Informativa sul trattamento dei dati (mostrata nel sito; **da completare**) |
| `../docs/comunita.js` | Pagine del sito: accesso, iscrizione, discussione, profilo, moderazione |
| `../docs/comunita-config.js` | Indirizzo e chiave pubblica del servizio (vuoti finché non è pronto) |

## Come funziona

- **Accesso senza password**: l'iscritto scrive la sua email e riceve un codice (8 cifre, valido un'ora) e, in alternativa, un link di accesso.
- **Su invito**: ogni iscritto ha 3 inviti personali (30 giorni). Chi non conosce nessuno chiede un invito; un moderatore lo esamina.
- **Periodo di prova**: i primi interventi passano dalla revisione; dopo 3 approvati l'iscritto diventa attivo e può invitare.
- **Segnalazioni**: con 3 segnalazioni di persone diverse un intervento va automaticamente in revisione.
- **Moderazione trasparente**: ogni azione richiede un motivo e finisce in un registro visibile a tutti gli iscritti.
- **Sicurezza**: le tabelle non sono raggiungibili dal sito; tutto passa da funzioni che controllano chi chiama. La chiave pubblicata nel sito ("anon") da sola non apre nessun dato.
- **Dati personali**: ogni iscritto scarica i propri dati e cancella l'account dal profilo, con effetto immediato.

Il database è stato provato con 65 casi (iscrizione, permessi, prova, segnalazioni, moderazione, sospensioni, cancellazione) su PostgreSQL.

## Attivazione (una volta sola)

Le registrazioni ai servizi le fa il titolare del progetto. Le chiavi segrete non si scrivono mai nel repository.

1. **Crea il progetto Supabase** (piano gratuito) su supabase.com: nome `governai-comunita`, regione **Europa (Frankfurt)**, password del database robusta, da conservare e non condividere.
2. **Crea il database**: *SQL Editor* → incolla tutto `schema.sql` → *Run*. Si può rieseguire senza perdere dati.
3. **Accesso via email**: *Authentication → Sign In / Providers*: lascia attivo solo *Email*, con *Confirm email* attivo. Le iscrizioni aperte servono a chi arriva con un invito: senza invito l'account resta vuoto e non può fare nulla.
4. **Email con il codice**: *Authentication → Emails → Templates*, modelli *Magic link or OTP* e *Confirm sign up* (modificabili solo dopo aver collegato l'SMTP, passo 5). Oggetto: `Il tuo accesso alla comunità GovernAI`. Testo:

   ```html
   <p>Il tuo codice di accesso alla comunità GovernAI è:</p>
   <p style="font-size:28px;font-weight:bold;letter-spacing:4px">{{ .Token }}</p>
   <p>In alternativa puoi entrare con questo link: <a href="{{ .ConfirmationURL }}">entra nella comunità</a></p>
   <p>Codice e link valgono un'ora e si usano una sola volta. Se non hai chiesto tu l'accesso, ignora questa email.</p>
   ```

5. **Invio delle email**: il servizio di posta incluso in Supabase recapita solo agli indirizzi dei membri del progetto ed è pensato per le prove. Collega un servizio SMTP con piano gratuito (in uso: Brevo, 300 email al giorno) in *Authentication → Emails → SMTP Settings*: host `smtp-relay.brevo.com`, porta `587`, utente = login SMTP di Brevo, password = chiave SMTP di Brevo (segreta: si incolla solo nel pannello). Mittente verificato in Brevo; meglio un indirizzo su un dominio del progetto. Con l'SMTP collegato il limite parte da 30 email all'ora (*Authentication → Rate Limits*).
6. **Indirizzo del sito**: *Authentication → URL Configuration* → *Site URL* = `https://fabiodeluca1977.github.io/governai/`.
7. **Collega il sito**: *Project Settings → API*, copia *Project URL* e la chiave **anon public** in `docs/comunita-config.js`. La chiave *service_role* non va mai nel sito né nel repository.
8. **Primo iscritto (fondatore)**: *Authentication → Users → Add user* con la tua email; copia l'*UID* e nell'*SQL Editor* esegui:

   ```sql
   select public.crea_fondatore('UID-copiato', 'Il tuo nome pubblico');
   ```

   Poi entra dal sito (*Comunità → Entra*) e crea i primi inviti dal profilo.
9. **Completa `privacy.md`**: titolare, contatto, servizio email, regione; poi fallo rivedere da un consulente privacy prima di aprire.

## Aggiornamenti del database

Quando il sito aggiunge un nuovo tipo di discussione serve un piccolo aggiornamento del database. Si esegue una volta nell'*SQL Editor* il file indicato; rieseguire tutto `schema.sql` produce lo stesso effetto.

| Data | File | Che cosa fa |
|---|---|---|
| 14/11/2026 | `migrazioni/2026-11-14_atti_del_governo.sql` | Permette la discussione sotto ogni atto della pagina *Governo di oggi* |

## Nominare altri moderatori

Dall'*SQL Editor*, sempre con una motivazione che finisce nel registro:

```sql
select public.imposta_moderatore('Nome pubblico', true, 'motivo della nomina');
```

L'obiettivo dichiarato nelle regole è passare a moderatori estratti a sorte fra gli iscritti attivi, a rotazione.

## Limiti del piano gratuito

- Il progetto si **mette in pausa dopo 7 giorni senza attività**; si riattiva dal pannello di Supabase.
- 500 MB di database: bastano per centinaia di migliaia di interventi.
- **Niente backup automatici**: esporta periodicamente il database dal pannello (*Database → Backups* o con `pg_dump`).
