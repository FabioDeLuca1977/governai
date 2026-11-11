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

- **Accesso senza password**: l'iscritto scrive la sua email e riceve un codice di 6 cifre.
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
4. **Email con il codice**: *Authentication → Emails → Templates*, modelli *Magic Link* e *Confirm signup*. Oggetto: `Il tuo codice GovernAI`. Testo:

   ```html
   <p>Il tuo codice di accesso alla comunità GovernAI è:</p>
   <p style="font-size:28px;font-weight:bold;letter-spacing:4px">{{ .Token }}</p>
   <p>Vale un'ora. Se non hai chiesto tu il codice, ignora questa email.</p>
   ```

5. **Invio delle email**: il servizio di posta incluso in Supabase manda pochissime email all'ora ed è pensato per le prove. Collega un servizio SMTP con piano gratuito (per esempio Brevo, 300 email al giorno) in *Authentication → SMTP Settings*, con mittente su un indirizzo del progetto.
6. **Indirizzo del sito**: *Authentication → URL Configuration* → *Site URL* = `https://fabiodeluca1977.github.io/governai/`.
7. **Collega il sito**: *Project Settings → API*, copia *Project URL* e la chiave **anon public** in `docs/comunita-config.js`. La chiave *service_role* non va mai nel sito né nel repository.
8. **Primo iscritto (fondatore)**: *Authentication → Users → Add user* con la tua email; copia l'*UID* e nell'*SQL Editor* esegui:

   ```sql
   select public.crea_fondatore('UID-copiato', 'Il tuo nome pubblico');
   ```

   Poi entra dal sito (*Comunità → Entra*) e crea i primi inviti dal profilo.
9. **Completa `privacy.md`**: titolare, contatto, servizio email, regione; poi fallo rivedere da un consulente privacy prima di aprire.

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
