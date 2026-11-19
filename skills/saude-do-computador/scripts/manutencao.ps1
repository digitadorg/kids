param([string]$Saida = "$env:USERPROFILE\Downloads\TITI-AI\manutencao-pc")
New-Item -ItemType Directory -Force $Saida | Out-Null
$log = Join-Path $Saida 'manutencao.log'
function L($m) { $linha = (Get-Date -Format 'HH:mm:ss') + '  ' + $m; Add-Content -Path $log -Value $linha -Encoding UTF8; Write-Host $linha }
Set-Content -Path $log -Value '' -Encoding UTF8
$env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User')

# 1. Ponto de restauracao (se falhar, para tudo)
L 'ETAPA 1/4: criando ponto de restauracao'
try {
  Checkpoint-Computer -Description 'Antes da manutencao (Claude)' -RestorePointType MODIFY_SETTINGS -ErrorAction Stop
  $rp = Get-ComputerRestorePoint | Sort-Object SequenceNumber | Select-Object -Last 1
  L "OK ponto de restauracao: '$($rp.Description)' em $($rp.ConvertToDateTime($rp.CreationTime))"
} catch {
  L "ERRO ponto de restauracao: $($_.Exception.Message)"
  L 'PARADO: nada foi atualizado, porque o ponto de restauracao nao foi criado.'
  L 'FIM'
  exit 1
}

# 2. Windows Update (so software, sem os drivers antigos)
L 'ETAPA 2/4: Windows Update (sem drivers)'
try {
  $s = New-Object -ComObject Microsoft.Update.Session
  $r = $s.CreateUpdateSearcher().Search("IsInstalled=0 and IsHidden=0 and Type='Software'")
  $col = New-Object -ComObject Microsoft.Update.UpdateColl
  foreach ($u in $r.Updates) { if (-not $u.EulaAccepted) { $u.AcceptEula() }; [void]$col.Add($u); L "  na fila: $($u.Title)" }
  if ($col.Count -gt 0) {
    L "  baixando $($col.Count) atualizacao(oes)... (a 26H2 pode levar bastante tempo)"
    $d = $s.CreateUpdateDownloader(); $d.Updates = $col; $dr = $d.Download()
    L "  download terminou (codigo $($dr.ResultCode); 2 = ok)"
    L '  instalando...'
    $i = $s.CreateUpdateInstaller(); $i.Updates = $col; $ir = $i.Install()
    for ($k = 0; $k -lt $col.Count; $k++) { L "  $($col.Item($k).Title) -> codigo $($ir.GetUpdateResult($k).ResultCode) (2 = ok)" }
    L "OK Windows Update. Precisa reiniciar: $($ir.RebootRequired)"
  } else { L 'OK nada pendente' }
} catch { L "ERRO Windows Update: $($_.Exception.Message)" }

# 3. winget upgrade --all
L 'ETAPA 3/4: winget upgrade --all'
winget upgrade --all --silent --accept-package-agreements --accept-source-agreements --disable-interactivity *>&1 | Where-Object { $_ -match 'Successfully|Found|failed|Falha|No installed|instal' } | ForEach-Object { L "  $_" }
L "OK winget (codigo $LASTEXITCODE)"

# 4. Intel DSA e Samsung Update
L 'ETAPA 4/4: Intel Driver & Support Assistant e Samsung Update'
winget install --id Intel.IntelDriverAndSupportAssistant -e --source winget --silent --accept-package-agreements --accept-source-agreements --disable-interactivity *>&1 | Where-Object { $_ -match 'Successfully|Found|failed|already' } | ForEach-Object { L "  $_" }
L "  Intel DSA codigo $LASTEXITCODE"
winget install --id 9NQ3HDB99VBF --source msstore --accept-package-agreements --accept-source-agreements --disable-interactivity *>&1 | Where-Object { $_ -match 'Successfully|Found|failed|already' } | ForEach-Object { L "  $_" }
L "  Samsung Update codigo $LASTEXITCODE"
L 'FIM'
