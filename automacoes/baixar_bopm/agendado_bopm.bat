@echo off
:: ============================================================
:: agendado_bopm.bat — Execucao automatica (seg-sex 08h)
:: Modo headless: Edge invisivel. Hiberna ao terminar.
:: ============================================================

cd /d "%~dp0"

:: Redireciona saida para log adicional de execucao agendada
set LOG=%USERPROFILE%\Downloads\logs_bopm\agendado_%date:~6,4%%date:~3,2%%date:~0,2%.log
echo [%date% %time%] Automacao agendada iniciada >> "%LOG%"

python main.py --days 4 --headless

set EXIT_CODE=%errorlevel%
echo [%date% %time%] Automacao concluida. Codigo: %EXIT_CODE% >> "%LOG%"

:: Hiberna o notebook apos concluir
echo [%date% %time%] Hibernando... >> "%LOG%"
shutdown /h
