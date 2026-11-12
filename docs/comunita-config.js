/* Collegamento al servizio della comunità su invito (guida: comunita/README.md).
   La chiave "publishable" di Supabase è fatta per stare nel sito: da sola non apre i dati, perché tabelle
   e permessi sono chiusi in comunita/schema.sql. Le chiavi segrete ("secret" o "service_role") NON vanno mai qui né nel repository.
   Finché url e chiave sono vuoti, il sito mostra la comunità "in preparazione". */
window.GOVERNAI_COMUNITA = { url: "https://qdqytvntlvovtviaaymo.supabase.co", chiave: "sb_publishable_p8VXqQ3a4J1eFMpGt8q4vg_GU7dxElV" };
