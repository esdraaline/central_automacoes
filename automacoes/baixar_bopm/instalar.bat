@echo off
:: ============================================================
:: instalar.bat — Instalação das dependências da Automação BOPM
:: Execute UMA VEZ antes de usar a automação.
:: Requisito: Python 3.10+ instalado e no PATH.
:: ============================================================

echo.
echo ============================================================
echo   INSTALACAO - Automacao BOPM/SIOPM PMESP
echo ============================================================
echo.

:: Verifica Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado. Instale Python 3.10+ em:
    echo        https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python encontrado:
python --version

:: Instala dependências pip
echo.
echo [1/3] Instalando dependencias pip...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERRO] Falha ao instalar dependencias.
    pause
    exit /b 1
)

:: Instala browsers do Playwright (somente Chromium/Edge)
echo.
echo [2/3] Instalando drivers do Playwright (Microsoft Edge)...
python -m playwright install msedge
if errorlevel 1 (
    echo [AVISO] Falha ao instalar msedge. Tentando chromium como fallback...
    python -m playwright install chromium
)

:: Cria pasta de logs
echo.
echo [3/3] Criando pasta de logs...
if not exist "%USERPROFILE%\Downloads\logs_bopm" (
    mkdir "%USERPROFILE%\Downloads\logs_bopm"
    echo [OK] Pasta criada: %USERPROFILE%\Downloads\logs_bopm
) else (
    echo [OK] Pasta ja existe: %USERPROFILE%\Downloads\logs_bopm
)

echo.
echo ============================================================
echo   INSTALACAO CONCLUIDA!
echo   Execute a automacao com: executar_bopm.bat
echo ============================================================
echo.
pause
