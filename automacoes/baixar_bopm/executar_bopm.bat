@echo off
:: ============================================================
:: executar_bopm.bat — Launcher da Automacao BOPM/SIOPM PMESP
:: Modo supervisionado: Edge fica visível para acompanhamento.
:: ============================================================

echo.
echo ============================================================
echo   AUTOMACAO BOPM - PMESP / SIOPM Web
echo   Modo: Supervisionado (janela do Edge visivel)
echo ============================================================
echo.

:: Muda para o diretório do script
cd /d "%~dp0"

:: Verifica Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado. Execute instalar.bat primeiro.
    pause
    exit /b 1
)

:: Menu de opcoes
echo Opcoes de execucao:
echo   [1] Padrao - ultimos 4 dias (recomendado)
echo   [2] Ultimos 7 dias
echo   [3] Ja estou conectado na VPN (pular etapa VPN)
echo   [4] Debug completo (mais detalhes no log)
echo   [5] Sair
echo.
set /p OPCAO="Escolha uma opcao [1-5]: "

if "%OPCAO%"=="1" (
    set CMD=python main.py --days 4
) else if "%OPCAO%"=="2" (
    set CMD=python main.py --days 7
) else if "%OPCAO%"=="3" (
    set CMD=python main.py --no-vpn --days 4
) else if "%OPCAO%"=="4" (
    set CMD=python main.py --log-level DEBUG --days 4
) else if "%OPCAO%"=="5" (
    exit /b 0
) else (
    echo Opcao invalida. Executando modo padrao...
    set CMD=python main.py --days 4
)

echo.
echo Executando: %CMD%
echo.
echo AVISO: NAO feche esta janela durante a execucao!
echo Para interromper com seguranca: pressione Ctrl+C
echo.

%CMD%

set EXIT_CODE=%errorlevel%

echo.
if %EXIT_CODE%==0 (
    echo ============================================================
    echo   AUTOMACAO CONCLUIDA COM SUCESSO!
    echo   PDFs salvos em: %USERPROFILE%\Downloads
    echo   Logs em: %USERPROFILE%\Downloads\logs_bopm
    echo ============================================================
) else if %EXIT_CODE%==1 (
    echo ============================================================
    echo   AUTOMACAO CONCLUIDA COM FALHAS PARCIAIS.
    echo   Verifique os logs em: %USERPROFILE%\Downloads\logs_bopm
    echo ============================================================
) else (
    echo ============================================================
    echo   ERRO CRITICO - Automacao interrompida.
    echo   Verifique os logs em: %USERPROFILE%\Downloads\logs_bopm
    echo ============================================================
)

echo.
echo Pressione qualquer tecla para abrir a pasta Downloads...
pause >nul
explorer "%USERPROFILE%\Downloads"
