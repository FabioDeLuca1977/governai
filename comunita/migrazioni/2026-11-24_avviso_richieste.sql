-- Avviso via email a chi modera quando arriva una nuova richiesta di invito.
-- Da eseguire una volta nell'SQL Editor di Supabase, DOPO aver salvato i tre segreti nel Vault (comunita/README.md,
-- "Avviso delle richieste di invito"). È già compreso in schema.sql: chi riesegue tutto schema.sql non deve eseguire
-- anche questo file.
--
-- Come funziona: dopo ogni nuova riga in richieste_invito parte una chiamata all'API di Brevo (servizio di posta già
-- usato per i codici di accesso). L'email NON contiene nome, email o motivazione di chi chiede: dice solo quante
-- richieste aspettano e rimanda alla pagina Moderazione, dove si leggono dopo l'accesso.
-- Senza segreti nel Vault non succede nulla; se Brevo non risponde la richiesta viene salvata lo stesso.
-- Per non consumare il limite di Brevo (300 email al giorno, condiviso con i codici di accesso) parte al massimo
-- un avviso ogni 15 minuti: le richieste arrivate nel frattempo si vedono nella pagina Moderazione e sono contate
-- nell'avviso successivo.

create extension if not exists pg_net;

-- quando è partito l'ultimo avviso (una sola riga; nessun dato personale)
create table if not exists public.avvisi_richieste (
  id          int primary key default 1 check (id = 1),
  inviato_at  timestamptz not null
);
alter table public.avvisi_richieste enable row level security;

create or replace function public._avvisa_richiesta() returns trigger
language plpgsql security definer set search_path = public, pg_temp as $$
declare
  chiave text; a text; da text; n int;
begin
  select decrypted_secret into chiave from vault.decrypted_secrets where name = 'brevo_api_key';
  select decrypted_secret into a      from vault.decrypted_secrets where name = 'avviso_destinatario';
  select decrypted_secret into da     from vault.decrypted_secrets where name = 'avviso_mittente';
  if chiave is null or a is null or da is null then
    return new;
  end if;
  -- un avviso ogni 15 minuti al massimo
  if exists (select 1 from avvisi_richieste where inviato_at > now() - interval '15 minutes') then
    return new;
  end if;
  insert into avvisi_richieste (id, inviato_at) values (1, now())
    on conflict (id) do update set inviato_at = excluded.inviato_at;
  select count(*) into n from richieste_invito where esito = 'in_attesa';
  perform net.http_post(
    url := 'https://api.brevo.com/v3/smtp/email',
    headers := jsonb_build_object('api-key', chiave, 'content-type', 'application/json', 'accept', 'application/json'),
    body := jsonb_build_object(
      'sender', jsonb_build_object('name', 'GovernAI comunità', 'email', da),
      'to', jsonb_build_array(jsonb_build_object('email', a)),
      'subject', 'GovernAI: nuova richiesta di invito (' || n || ' in attesa)',
      'textContent', 'È arrivata una nuova richiesta di invito alla comunità GovernAI. Richieste in attesa: ' || n || '.'
        || E'\n\nPer leggerle e decidere: https://fabiodeluca1977.github.io/governai/#/comunita/moderazione'
        || E'\n\nQuesta email non contiene i dati di chi chiede: si leggono solo dopo l''accesso.'));
  return new;
exception when others then
  -- l'avviso non deve mai impedire di salvare la richiesta
  return new;
end $$;

revoke all on function public._avvisa_richiesta() from public, anon, authenticated;

drop trigger if exists avvisa_richiesta on public.richieste_invito;
create trigger avvisa_richiesta after insert on public.richieste_invito
  for each row execute function public._avvisa_richiesta();
