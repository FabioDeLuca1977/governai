-- Discussione fra iscritti sugli atti del governo di oggi (pagina "Governo di oggi" del sito).
-- Da eseguire una volta nell'SQL Editor di Supabase. Non tocca i dati: amplia solo i temi ammessi
-- con "atto:<id>", dove <id> è il codice di un commento in osservatorio/atti/.
-- È già compreso in schema.sql: chi riesegue tutto schema.sql non deve eseguire anche questo file.
alter table public.interventi drop constraint if exists interventi_tema_check;
alter table public.interventi add constraint interventi_tema_check
  check (tema ~ '^(generale|metodo|proposta:[0-9]{2}-[PC][0-9]{1,2}|area:[0-9]{2}|scenario:[a-z0-9-]{1,40}|atto:[a-z0-9-]{1,60})$');
