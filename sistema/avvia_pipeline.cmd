@echo off
rem Avvio della pipeline dinamica di GovernAI (usato dall'Utilità di pianificazione di Windows)
cd /d "%~dp0"
python -I pipeline.py >> "stato\pipeline.log" 2>&1
