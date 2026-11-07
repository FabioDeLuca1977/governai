@echo off
rem GovernAI sul computer locale (Utilità di pianificazione di Windows).
rem L'aggiornamento completo (dati, programma, livello AI, interfaccia) gira ogni giorno su GitHub Actions:
rem qui si scaricano solo i risultati, così la copia locale resta aggiornata senza costi doppi né conflitti.
rem Per rieseguire tutto in locale (es. fonti che bloccano GitHub): python pipeline.py --completo
cd /d "%~dp0"
python -I sincronizza.py >> "stato\pipeline.log" 2>&1
