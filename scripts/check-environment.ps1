# Diagnóstico no invasivo: no instala herramientas, no cambia archivos y no autentica.
$ErrorActionPreference = 'Continue'
Write-Host "Verificación del entorno (solo lectura)" -ForegroundColor Cyan
Write-Host "Ruta: $(Get-Location)"
$commands = @('git', 'node', 'npm', 'python', 'skillshare', 'openspec', 'codex', 'claude', 'opencode', 'graft')
foreach ($name in $commands) {
  $cmd = Get-Command $name -ErrorAction SilentlyContinue
  if ($null -eq $cmd) {
    Write-Host "[PENDIENTE] $name no encontrado en PATH"
    continue
  }
  Write-Host "[EN PATH] $name -> $($cmd.Source)"
  if ($name -in @('git', 'node', 'npm', 'skillshare', 'openspec', 'codex', 'claude', 'opencode', 'graft')) {
    try {
      $version = & $name --version 2>&1 | Select-Object -First 2
      foreach ($line in $version) { Write-Host "  $line" }
    } catch { Write-Host "  No se pudo obtener version: $_" }
  }
}
if (Get-Command node -ErrorAction SilentlyContinue) {
  try {
    $v = (& node --version).TrimStart('v')
    $parsed = [version]$v
    if ($parsed -lt [version]'20.19.0') { Write-Warning "OpenSpec requiere Node >= 20.19.0; encontrado $v" }
  } catch { Write-Warning 'No se pudo comparar la version de Node.' }
}
if (Get-Command git -ErrorAction SilentlyContinue) {
  & git status --short
  & git branch --show-current
}
Write-Host 'Pendiente: comprobar plugins/hooks/permisos/sesiones reales manualmente.'
