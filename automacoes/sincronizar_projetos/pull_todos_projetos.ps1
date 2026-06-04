param([switch]$NoPause)

$ErrorActionPreference = "Continue"

function Pause-IfNeeded {
  if (-not $NoPause) {
    Read-Host "Pressione Enter para sair"
  }
}

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$centralRoot = git -C $scriptDir rev-parse --show-toplevel 2>$null

if (-not $centralRoot) {
  Write-Host "Nao foi possivel localizar o repositorio central_automacoes." -ForegroundColor Red
  Pause-IfNeeded
  exit 1
}

$projectsRoot = Split-Path -Parent $centralRoot

function Get-GitProjects {
  param([string]$Root)

  $excludedNames = @(".git", "node_modules", "dist", "build", ".next", ".vite", "__pycache__", "_relatorios_comparacao")
  $queue = New-Object System.Collections.Queue
  $queue.Enqueue((Get-Item -LiteralPath $Root))

  while ($queue.Count -gt 0) {
    $current = $queue.Dequeue()
    $gitPath = Join-Path $current.FullName ".git"

    if (Test-Path -LiteralPath $gitPath) {
      $current
      continue
    }

    Get-ChildItem -LiteralPath $current.FullName -Directory -Force -ErrorAction SilentlyContinue |
      Where-Object { $excludedNames -notcontains $_.Name } |
      ForEach-Object { $queue.Enqueue($_) }
  }
}

$projects = Get-GitProjects -Root $projectsRoot | Sort-Object FullName -Unique

if (-not $projects) {
  Write-Host "Nenhum repositorio Git encontrado em $projectsRoot" -ForegroundColor Yellow
  Pause-IfNeeded
  exit 0
}

Write-Host "Atualizando repositorios em $projectsRoot" -ForegroundColor Cyan

foreach ($project in $projects) {
  Write-Host ""
  $relativePath = $project.FullName
  if ($relativePath.StartsWith($projectsRoot)) {
    $relativePath = $relativePath.Substring($projectsRoot.Length).TrimStart("\")
  }
  Write-Host "==> $relativePath" -ForegroundColor Cyan

  $status = git -C $project.FullName status --short
  if ($status) {
    Write-Host "Alteracoes locais detectadas:" -ForegroundColor Yellow
    $status | ForEach-Object { Write-Host "  $_" }
  }

  git -C $project.FullName pull --ff-only
  if ($LASTEXITCODE -ne 0) {
    Write-Host "Falha ao atualizar $relativePath. Verifique as mensagens acima." -ForegroundColor Red
  }
}

Write-Host ""
Write-Host "Concluido." -ForegroundColor Green
Pause-IfNeeded
