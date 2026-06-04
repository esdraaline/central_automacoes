@echo off
set "SCRIPT_DIR=%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPT_DIR%automacoes\sincronizar_projetos\pull_todos_projetos.ps1"
