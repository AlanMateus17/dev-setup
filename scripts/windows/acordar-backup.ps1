<#
  Acorda o Ubuntu (WSL) às 22h20 todo dia, para o backup do cron das 22h30 rodar mesmo com o terminal fechado.
  Não precisa de administrador (a tarefa é sua e roda com você logado, como o próprio WSL).
    powershell -ExecutionPolicy Bypass -File acordar-backup.ps1 [-Distro Ubuntu] [-Hora 22:20] [-Testar] [-Desfazer]

  O que faz:
    Tarefa "AMtech acordar backup": às 22h20 acorda o notebook se estiver suspenso (WakeToRun) e liga o Ubuntu
    escondido por 30 minutos (sleep 1800), o tempo de o cron disparar o backup.sh às 22h30.
    Se o computador estava desligado na hora, roda assim que ele ligar (StartWhenAvailable).
  -Testar dispara a tarefa agora e mostra o resultado.
  -Desfazer remove a tarefa.
  Complementa o manter-ligado.ps1 (tarefa "AMtech WSL", que liga o Ubuntu no login e o mantém ligado).
#>
param([string]$Distro = "Ubuntu", [string]$Hora = "22:20", [switch]$Testar, [switch]$Desfazer)
$ErrorActionPreference = "Stop"
$nome = "AMtech acordar backup"

if ($Desfazer) {
  Unregister-ScheduledTask -TaskName $nome -Confirm:$false -ErrorAction SilentlyContinue
  Write-Host "[ok] Tarefa '$nome' removida."
  exit 0
}

# Sem janela: conhost --headless (Windows 11). 30 min cobrem o cron das 22h30 com folga.
$acao = New-ScheduledTaskAction -Execute "conhost.exe" -Argument "--headless wsl.exe -d $Distro --exec /bin/sleep 1800"
$gatilho = New-ScheduledTaskTrigger -Daily -At $Hora
$ajustes = New-ScheduledTaskSettingsSet -WakeToRun -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries `
  -ExecutionTimeLimit (New-TimeSpan -Minutes 45) -MultipleInstances IgnoreNew
Register-ScheduledTask -TaskName $nome -Action $acao -Trigger $gatilho -Settings $ajustes `
  -Description "Liga o Ubuntu (WSL) para o backup restic das 22h30 (dev-setup, scripts/windows/acordar-backup.ps1)" -Force | Out-Null
Write-Host "[ok] Tarefa '$nome' criada: todo dia às $Hora."

if ($Testar) {
  Start-ScheduledTask -TaskName $nome
  Start-Sleep -Seconds 5
  $info = Get-ScheduledTaskInfo -TaskName $nome
  $estado = (Get-ScheduledTask -TaskName $nome).State
  Write-Host "[teste] estado: $estado; última execução: $($info.LastRunTime); resultado: $($info.LastTaskResult) (267009 = ainda rodando); próxima: $($info.NextRunTime)"
}
exit 0
