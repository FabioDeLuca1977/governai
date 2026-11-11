-- GovernAI · comunità su invito (Supabase / PostgreSQL)
--
-- Il programma resta leggibile da chiunque; la partecipazione (discussione, appunti, segnalazioni)
-- è riservata a chi entra con un invito. Regole: comunita/regole.md. Dati personali: comunita/privacy.md.
--
-- Principio di sicurezza: le tabelle non sono accessibili direttamente dal sito (RLS attiva e nessuna
-- policy). Tutto passa da funzioni che controllano chi chiama, applicano i limiti e scrivono il registro
-- pubblico della moderazione. La chiave "anon" pubblicata nel sito non dà accesso ad altro.
--
-- Si esegue una volta nell'editor SQL del progetto Supabase (vedi comunita/README.md).
-- Ripetibile: ricrea funzioni e permessi senza toccare i dati.

create extension if not exists pgcrypto;

-- ---------------------------------------------------------------- tabelle

create table if not exists public.profili (
  id              uuid primary key references auth.users(id) on delete cascade,
  nome_pubblico   text not null unique
                  check (char_length(nome_pubblico) between 3 and 40
                         and nome_pubblico ~ '^[[:alnum:]][[:alnum:] ._''-]*$'),
  invitato_da     uuid references public.profili(id) on delete set null,
  stato           text not null default 'prova' check (stato in ('prova', 'attivo', 'sospeso')),
  moderatore      boolean not null default false,
  inviti_residui  int not null default 3 check (inviti_residui >= 0),
  approvati       int not null default 0,
  consenso_at     timestamptz not null,
  creato_at       timestamptz not null default now()
);

create table if not exists public.richieste_invito (
  id            bigint generated always as identity primary key,
  nome          text not null check (char_length(nome) between 2 and 80),
  email         text not null check (char_length(email) <= 200 and email ~* '^[^@\s]+@[^@\s]+\.[^@\s]+$'),
  motivazione   text not null check (char_length(motivazione) between 20 and 1500),
  consenso_at   timestamptz not null default now(),
  creato_at     timestamptz not null default now(),
  esito         text not null default 'in_attesa' check (esito in ('in_attesa', 'accolta', 'non_accolta')),
  esito_motivo  text,
  esito_da      uuid references public.profili(id) on delete set null,
  esito_at      timestamptz
);

create table if not exists public.inviti (
  codice         text primary key default encode(gen_random_bytes(9), 'hex'),
  creato_da      uuid references public.profili(id) on delete set null,
  per_richiesta  bigint references public.richieste_invito(id) on delete set null,
  creato_at      timestamptz not null default now(),
  scade_at       timestamptz not null default now() + interval '30 days',
  usato_da       uuid references public.profili(id) on delete set null,
  usato_at       timestamptz,          -- è questo a dire che l'invito è stato usato
  revocato       boolean not null default false
);

create table if not exists public.interventi (
  id             bigint generated always as identity primary key,
  autore         uuid not null references public.profili(id) on delete cascade,
  tema           text not null
                 check (tema ~ '^(generale|metodo|proposta:[0-9]{2}-[PC][0-9]{1,2}|area:[0-9]{2}|scenario:[a-z0-9-]{1,40})$'),
  risponde_a     bigint references public.interventi(id) on delete set null,
  testo          text not null check (char_length(btrim(testo)) between 2 and 4000),
  stato          text not null default 'in_revisione' check (stato in ('visibile', 'in_revisione', 'nascosto')),
  creato_at      timestamptz not null default now()
);
create index if not exists interventi_tema on public.interventi (tema, creato_at);
create index if not exists interventi_autore on public.interventi (autore, creato_at);

create table if not exists public.segnalazioni (
  intervento  bigint not null references public.interventi(id) on delete cascade,
  autore      uuid not null references public.profili(id) on delete cascade,
  motivo      text not null check (motivo in ('offesa', 'odio', 'spam', 'dati_personali', 'fuori_tema', 'falso')),
  nota        text check (char_length(nota) <= 500),
  creato_at   timestamptz not null default now(),
  primary key (intervento, autore)
);

-- Registro pubblico (per gli iscritti) di ogni azione di moderazione: chi, cosa, perché.
create table if not exists public.registro_moderazione (
  id          bigint generated always as identity primary key,
  moderatore  uuid references public.profili(id) on delete set null,   -- null = regola automatica
  azione      text not null,
  oggetto     text not null,
  motivo      text not null,
  creato_at   timestamptz not null default now()
);

alter table public.profili              enable row level security;
alter table public.richieste_invito     enable row level security;
alter table public.inviti               enable row level security;
alter table public.interventi           enable row level security;
alter table public.segnalazioni         enable row level security;
alter table public.registro_moderazione enable row level security;
revoke all on all tables in schema public from anon, authenticated;

-- ---------------------------------------------------------------- funzioni di servizio (non esposte)

create or replace function public._io() returns public.profili
language sql stable security definer set search_path = public, pg_temp as $$
  select * from profili where id = auth.uid()
$$;

create or replace function public._membro() returns public.profili
language plpgsql stable security definer set search_path = public, pg_temp as $$
declare p profili;
begin
  select * into p from profili where id = auth.uid();
  if p.id is null then raise exception 'Questa funzione è riservata agli iscritti.'; end if;
  if p.stato = 'sospeso' then raise exception 'Il tuo account è sospeso: vedi il registro della moderazione.'; end if;
  return p;
end $$;

create or replace function public._moderatore() returns public.profili
language plpgsql stable security definer set search_path = public, pg_temp as $$
declare p profili := public._membro();
begin
  if not p.moderatore or p.stato <> 'attivo' then raise exception 'Funzione riservata ai moderatori.'; end if;
  return p;
end $$;

create or replace function public._registra(p_moderatore uuid, p_azione text, p_oggetto text, p_motivo text) returns void
language sql security definer set search_path = public, pg_temp as $$
  insert into registro_moderazione (moderatore, azione, oggetto, motivo) values (p_moderatore, p_azione, p_oggetto, p_motivo)
$$;

create or replace function public._motivo(p text) returns text
language plpgsql immutable as $$
begin
  if p is null or char_length(btrim(p)) < 3 then raise exception 'Serve una motivazione (almeno 3 caratteri): finisce nel registro pubblico.'; end if;
  return left(btrim(p), 500);
end $$;

-- ---------------------------------------------------------------- chiunque

-- Chiedere un invito, anche senza account. Limiti contro gli abusi; le richieste esaminate
-- si cancellano dopo 180 giorni (privacy.md).
create or replace function public.chiedi_invito(p_nome text, p_email text, p_motivazione text) returns text
language plpgsql security definer set search_path = public, pg_temp as $$
begin
  delete from richieste_invito where esito <> 'in_attesa' and esito_at < now() - interval '180 days';
  if exists (select 1 from richieste_invito where lower(email) = lower(btrim(p_email)) and creato_at > now() - interval '30 days') then
    raise exception 'Con questa email c''è già una richiesta negli ultimi 30 giorni.';
  end if;
  if (select count(*) from richieste_invito where creato_at > now() - interval '1 day') >= 100 then
    raise exception 'Oggi sono arrivate troppe richieste: riprova domani.';
  end if;
  insert into richieste_invito (nome, email, motivazione) values (btrim(p_nome), lower(btrim(p_email)), btrim(p_motivazione));
  return 'Richiesta ricevuta. Se viene accolta, riceverai un invito all''indirizzo indicato.';
end $$;

-- Controllare un codice prima di iscriversi (non rivela chi l'ha creato).
create or replace function public.verifica_invito(p_codice text) returns boolean
language sql stable security definer set search_path = public, pg_temp as $$
  select exists (select 1 from inviti i left join profili c on c.id = i.creato_da
                 where i.codice = lower(btrim(p_codice)) and i.usato_at is null and not i.revocato
                   and i.scade_at > now() and coalesce(c.stato, 'attivo') <> 'sospeso')
$$;

-- ---------------------------------------------------------------- iscrizione e profilo

create or replace function public.usa_invito(p_codice text, p_nome text, p_consenso boolean) returns public.profili
language plpgsql security definer set search_path = public, pg_temp as $$
declare inv inviti; p profili;
begin
  if auth.uid() is null then raise exception 'Prima conferma la tua email.'; end if;
  if exists (select 1 from profili where id = auth.uid()) then raise exception 'Sei già iscritto.'; end if;
  if not coalesce(p_consenso, false) then raise exception 'Per iscriverti serve il consenso al trattamento dei dati.'; end if;
  select * into inv from inviti where codice = lower(btrim(p_codice)) for update;
  if inv.codice is null or inv.usato_at is not null or inv.revocato or inv.scade_at <= now() then
    raise exception 'Invito non valido, già usato o scaduto.';
  end if;
  if exists (select 1 from profili where id = inv.creato_da and stato = 'sospeso') then
    raise exception 'Invito non valido, già usato o scaduto.';
  end if;
  if exists (select 1 from profili where lower(nome_pubblico) = lower(btrim(p_nome))) then
    raise exception 'Questo nome pubblico è già in uso: scegline un altro.';
  end if;
  insert into profili (id, nome_pubblico, invitato_da, consenso_at)
    values (auth.uid(), btrim(p_nome), inv.creato_da, now()) returning * into p;
  update inviti set usato_da = p.id, usato_at = now() where codice = inv.codice;
  return p;
end $$;

create or replace function public.mio_profilo() returns json
language sql stable security definer set search_path = public, pg_temp as $$
  select json_build_object(
    'nome_pubblico', p.nome_pubblico, 'stato', p.stato, 'moderatore', p.moderatore,
    'inviti_residui', p.inviti_residui, 'approvati', p.approvati, 'creato_at', p.creato_at,
    'invitato_da', (select nome_pubblico from profili where id = p.invitato_da))
  from profili p where p.id = auth.uid()
$$;

create or replace function public.crea_invito() returns text
language plpgsql security definer set search_path = public, pg_temp as $$
declare p profili := public._membro(); c text;
begin
  if p.stato <> 'attivo' then raise exception 'Si può invitare dopo il periodo di prova (3 interventi approvati).'; end if;
  if p.inviti_residui <= 0 then raise exception 'Hai esaurito i tuoi inviti.'; end if;
  update profili set inviti_residui = inviti_residui - 1 where id = p.id;
  insert into inviti (creato_da) values (p.id) returning codice into c;
  return c;
end $$;

create or replace function public.miei_inviti() returns table (codice text, creato_at timestamptz, scade_at timestamptz,
  usato boolean, revocato boolean, invitato text)
language sql stable security definer set search_path = public, pg_temp as $$
  select i.codice, i.creato_at, i.scade_at, i.usato_at is not null, i.revocato, u.nome_pubblico
  from inviti i left join profili u on u.id = i.usato_da
  where i.creato_da = (public._membro()).id order by i.creato_at desc
$$;

create or replace function public.revoca_invito(p_codice text) returns void
language plpgsql security definer set search_path = public, pg_temp as $$
declare p profili := public._membro();
begin
  update inviti set revocato = true where codice = p_codice and creato_da = p.id and usato_at is null and not revocato;
  if found then update profili set inviti_residui = inviti_residui + 1 where id = p.id; end if;
end $$;

-- Diritto di accesso e portabilità (art. 15 e 20 GDPR).
create or replace function public.miei_dati() returns json
language sql stable security definer set search_path = public, pg_temp as $$
  select json_build_object(
    'profilo', (select row_to_json(p) from profili p where id = auth.uid()),
    'email', (select email from auth.users where id = auth.uid()),
    'interventi', (select coalesce(json_agg(i order by creato_at), '[]') from interventi i where autore = auth.uid()),
    'segnalazioni', (select coalesce(json_agg(s), '[]') from segnalazioni s where autore = auth.uid()),
    'inviti', (select coalesce(json_agg(v), '[]') from inviti v where creato_da = auth.uid()))
$$;

-- Diritto alla cancellazione (art. 17 GDPR): elimina account, profilo, interventi e segnalazioni.
-- Le risposte di altri restano, senza il collegamento all'intervento cancellato.
create or replace function public.cancella_account() returns void
language plpgsql security definer set search_path = public, auth, pg_temp as $$
begin
  if auth.uid() is null then raise exception 'Non hai effettuato l''accesso.'; end if;
  update registro_moderazione set oggetto = 'iscritto cancellato'
    where oggetto = 'iscritto ' || (select nome_pubblico from public.profili where id = auth.uid());
  delete from auth.users where id = auth.uid();
end $$;

-- ---------------------------------------------------------------- discussione

create or replace function public.scrivi(p_tema text, p_testo text, p_risponde_a bigint default null) returns json
language plpgsql security definer set search_path = public, pg_temp as $$
declare p profili := public._membro(); n int; lim int; st text; r interventi;
begin
  lim := case when p.stato = 'attivo' then 40 else 5 end;
  select count(*) into n from interventi where autore = p.id and creato_at > now() - interval '1 day';
  if n >= lim then raise exception 'Hai raggiunto il limite di % interventi in 24 ore.', lim; end if;
  if p_risponde_a is not null and not exists (select 1 from interventi where id = p_risponde_a and tema = p_tema and stato = 'visibile') then
    raise exception 'L''intervento a cui rispondi non è disponibile.';
  end if;
  st := case when p.stato = 'attivo' then 'visibile' else 'in_revisione' end;
  insert into interventi (autore, tema, risponde_a, testo, stato) values (p.id, p_tema, p_risponde_a, btrim(p_testo), st) returning * into r;
  return json_build_object('id', r.id, 'stato', r.stato);
end $$;

create or replace function public.leggi(p_tema text) returns table (id bigint, autore text, testo text, stato text,
  creato_at timestamptz, risponde_a bigint, mio boolean, segnalato boolean)
language sql stable security definer set search_path = public, pg_temp as $$
  with io as (select * from public._membro())
  select i.id, a.nome_pubblico, i.testo, i.stato, i.creato_at, i.risponde_a, i.autore = io.id,
         exists (select 1 from segnalazioni s where s.intervento = i.id and s.autore = io.id)
  from interventi i join profili a on a.id = i.autore, io
  where i.tema = p_tema and (i.stato = 'visibile' or i.autore = io.id or (io.moderatore and io.stato = 'attivo'))
  order by i.creato_at
$$;

create or replace function public.ultimi(p_limite int default 20) returns table (id bigint, tema text, autore text, testo text, creato_at timestamptz)
language sql stable security definer set search_path = public, pg_temp as $$
  select i.id, i.tema, a.nome_pubblico, left(i.testo, 280), i.creato_at
  from interventi i join profili a on a.id = i.autore
  where i.stato = 'visibile' and (public._membro()).id is not null
  order by i.creato_at desc limit least(greatest(p_limite, 1), 50)
$$;

create or replace function public.cancella_intervento(p_id bigint) returns void
language plpgsql security definer set search_path = public, pg_temp as $$
declare p profili := public._io();
begin
  delete from interventi where id = p_id and autore = p.id;
end $$;

-- Tre segnalazioni di persone diverse mettono l'intervento in revisione, senza attendere un moderatore.
create or replace function public.segnala(p_id bigint, p_motivo text, p_nota text default null) returns void
language plpgsql security definer set search_path = public, pg_temp as $$
declare p profili := public._membro(); n int;
begin
  if not exists (select 1 from interventi where id = p_id and stato = 'visibile' and autore <> p.id) then
    raise exception 'Questo intervento non si può segnalare.';
  end if;
  insert into segnalazioni (intervento, autore, motivo, nota) values (p_id, p.id, p_motivo, nullif(btrim(p_nota), ''))
    on conflict (intervento, autore) do nothing;
  select count(*) into n from segnalazioni where intervento = p_id;
  if n >= 3 then
    update interventi set stato = 'in_revisione' where id = p_id and stato = 'visibile';
    if found then perform public._registra(null, 'in revisione', 'intervento ' || p_id, '3 segnalazioni di iscritti diversi'); end if;
  end if;
end $$;

-- ---------------------------------------------------------------- moderazione

create or replace function public.da_moderare() returns table (id bigint, tema text, autore text, stato_autore text, testo text,
  creato_at timestamptz, segnalazioni bigint, motivi text)
language sql stable security definer set search_path = public, pg_temp as $$
  select i.id, i.tema, a.nome_pubblico, a.stato, i.testo, i.creato_at,
         (select count(*) from segnalazioni s where s.intervento = i.id),
         (select string_agg(distinct s.motivo, ', ') from segnalazioni s where s.intervento = i.id)
  from interventi i join profili a on a.id = i.autore
  where i.stato = 'in_revisione' and (public._moderatore()).id is not null
  order by i.creato_at
$$;

-- Approvare porta l'autore verso la fine del periodo di prova (3 interventi approvati).
create or replace function public.modera(p_id bigint, p_azione text, p_motivo text) returns void
language plpgsql security definer set search_path = public, pg_temp as $$
declare m profili := public._moderatore(); i interventi; mot text := public._motivo(p_motivo);
begin
  select * into i from interventi where id = p_id;
  if i.id is null then raise exception 'Intervento non trovato.'; end if;
  if i.autore = m.id then raise exception 'Non si moderano i propri interventi.'; end if;
  if p_azione = 'approva' then
    update interventi set stato = 'visibile' where id = p_id;
    update profili set approvati = approvati + 1,
                       stato = case when stato = 'prova' and approvati + 1 >= 3 then 'attivo' else stato end
      where id = i.autore;
  elsif p_azione = 'nascondi' then
    update interventi set stato = 'nascosto' where id = p_id;
  else
    raise exception 'Azione non prevista.';
  end if;
  perform public._registra(m.id, p_azione, 'intervento ' || p_id, mot);
end $$;

create or replace function public.richieste_in_attesa() returns table (id bigint, nome text, email text, motivazione text, creato_at timestamptz)
language sql stable security definer set search_path = public, pg_temp as $$
  select r.id, r.nome, r.email, r.motivazione, r.creato_at from richieste_invito r
  where r.esito = 'in_attesa' and (public._moderatore()).id is not null order by r.creato_at
$$;

-- Se accolta restituisce il codice d'invito da mandare alla persona (nel registro non finiscono nome ed email).
create or replace function public.esamina_richiesta(p_id bigint, p_accolta boolean, p_motivo text) returns text
language plpgsql security definer set search_path = public, pg_temp as $$
declare m profili := public._moderatore(); c text; mot text := public._motivo(p_motivo);
begin
  update richieste_invito set esito = case when p_accolta then 'accolta' else 'non_accolta' end,
         esito_motivo = mot, esito_da = m.id, esito_at = now()
    where id = p_id and esito = 'in_attesa';
  if not found then raise exception 'Richiesta già esaminata o inesistente.'; end if;
  if p_accolta then insert into inviti (creato_da, per_richiesta) values (m.id, p_id) returning codice into c; end if;
  perform public._registra(m.id, case when p_accolta then 'richiesta accolta' else 'richiesta non accolta' end, 'richiesta ' || p_id, mot);
  return c;
end $$;

-- Sospendere un iscritto. Con p_ramo si azzerano anche gli inviti di chi lo ha invitato
-- e si revocano quelli non usati della persona sospesa.
create or replace function public.sospendi(p_nome text, p_motivo text, p_ramo boolean default false) returns void
language plpgsql security definer set search_path = public, pg_temp as $$
declare m profili := public._moderatore(); u profili; mot text := public._motivo(p_motivo);
begin
  select * into u from profili where nome_pubblico = p_nome;
  if u.id is null then raise exception 'Iscritto non trovato.'; end if;
  if u.id = m.id then raise exception 'Non puoi sospendere te stesso.'; end if;
  update profili set stato = 'sospeso', moderatore = false where id = u.id;
  update inviti set revocato = true where creato_da = u.id and usato_at is null;
  perform public._registra(m.id, 'sospensione', 'iscritto ' || u.nome_pubblico, mot);
  if p_ramo and u.invitato_da is not null then
    update profili set inviti_residui = 0 where id = u.invitato_da;
    perform public._registra(m.id, 'inviti azzerati', 'iscritto ' || (select nome_pubblico from profili where id = u.invitato_da), mot);
  end if;
end $$;

create or replace function public.riattiva(p_nome text, p_motivo text) returns void
language plpgsql security definer set search_path = public, pg_temp as $$
declare m profili := public._moderatore(); mot text := public._motivo(p_motivo);
begin
  update profili set stato = case when approvati >= 3 then 'attivo' else 'prova' end where nome_pubblico = p_nome and stato = 'sospeso';
  if not found then raise exception 'Nessun iscritto sospeso con questo nome.'; end if;
  perform public._registra(m.id, 'riattivazione', 'iscritto ' || p_nome, mot);
end $$;

create or replace function public.registro(p_limite int default 100) returns table (azione text, oggetto text, motivo text,
  moderatore text, creato_at timestamptz)
language sql stable security definer set search_path = public, pg_temp as $$
  select r.azione, r.oggetto, r.motivo, coalesce(m.nome_pubblico, 'regola automatica'), r.creato_at
  from registro_moderazione r left join profili m on m.id = r.moderatore
  where (public._membro()).id is not null
  order by r.creato_at desc limit least(greatest(p_limite, 1), 500)
$$;

-- ---------------------------------------------------------------- solo dall'editor SQL (amministrazione)

-- Primo iscritto: non ha invito. Uso: select public.crea_fondatore('<uuid dell'utente>', 'Nome pubblico');
create or replace function public.crea_fondatore(p_id uuid, p_nome text) returns void
language sql security definer set search_path = public, pg_temp as $$
  insert into profili (id, nome_pubblico, stato, moderatore, inviti_residui, consenso_at)
  values (p_id, p_nome, 'attivo', true, 10, now())
$$;

-- Nomina o revoca di un moderatore, sempre con motivazione nel registro.
create or replace function public.imposta_moderatore(p_nome text, p_valore boolean, p_motivo text) returns void
language plpgsql security definer set search_path = public, pg_temp as $$
begin
  update profili set moderatore = p_valore where nome_pubblico = p_nome and stato = 'attivo';
  if not found then raise exception 'Iscritto attivo non trovato.'; end if;
  perform public._registra(null, case when p_valore then 'nomina moderatore' else 'revoca moderatore' end,
                           'iscritto ' || p_nome, public._motivo(p_motivo));
end $$;

-- ---------------------------------------------------------------- permessi

revoke execute on all functions in schema public from public, anon, authenticated;

grant execute on function public.chiedi_invito(text, text, text)       to anon, authenticated;
grant execute on function public.verifica_invito(text)                  to anon, authenticated;
grant execute on function public.usa_invito(text, text, boolean)        to authenticated;
grant execute on function public.mio_profilo()                          to authenticated;
grant execute on function public.crea_invito()                          to authenticated;
grant execute on function public.miei_inviti()                          to authenticated;
grant execute on function public.revoca_invito(text)                    to authenticated;
grant execute on function public.miei_dati()                            to authenticated;
grant execute on function public.cancella_account()                     to authenticated;
grant execute on function public.scrivi(text, text, bigint)             to authenticated;
grant execute on function public.leggi(text)                            to authenticated;
grant execute on function public.ultimi(int)                            to authenticated;
grant execute on function public.cancella_intervento(bigint)            to authenticated;
grant execute on function public.segnala(bigint, text, text)            to authenticated;
grant execute on function public.da_moderare()                          to authenticated;
grant execute on function public.modera(bigint, text, text)             to authenticated;
grant execute on function public.richieste_in_attesa()                  to authenticated;
grant execute on function public.esamina_richiesta(bigint, boolean, text) to authenticated;
grant execute on function public.sospendi(text, text, boolean)          to authenticated;
grant execute on function public.riattiva(text, text)                   to authenticated;
grant execute on function public.registro(int)                          to authenticated;
-- crea_fondatore e imposta_moderatore restano eseguibili solo dall'editor SQL (ruolo postgres).
