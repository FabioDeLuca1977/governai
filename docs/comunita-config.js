/* Collegamento al servizio della comunità su invito (guida: comunita/README.md).
   La chiave "anon" di Supabase è fatta per stare nel sito: da sola non apre i dati, perché tabelle
   e permessi sono chiusi in comunita/schema.sql. La chiave "service_role" NON va mai qui né nel repository.
   Finché url e chiave sono vuoti, il sito mostra la comunità "in preparazione". */
window.GOVERNAI_COMUNITA = { url: "", chiave: "" };
