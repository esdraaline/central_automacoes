@echo off
setlocal
cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 (
    echo Python nao foi encontrado no PATH.
    echo Instale Python ou abra o terminal onde o comando "python" funcione.
    pause
    exit /b 1
)

python painel.py
if errorlevel 1 (
    echo.
    echo O painel encerrou com erro.
    pause
)
