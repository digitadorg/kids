param([string]$Saida = "$env:USERPROFILE\Downloads\TITI-AI\manutencao-pc")
New-Item -ItemType Directory -Force $Saida | Out-Null
$log = Join-Path $Saida 'pos-reinicio.log'
function L($m) { $linha = (Get-Date -Format 'HH:mm:ss') + '  ' + $m; Add-Content -Path $log -Value $linha -Encoding UTF8; Write-Host $linha }
function Livre { [math]::Round((Get-PSDrive C).Free/1GB,1) }
Set-Content -Path $log -Value '' -Encoding UTF8
$antes = Livre
L "Espaco livre antes: $antes GB"

L 'ETAPA 1/5: limpando instaladores do Windows Update e cache de entrega'
Stop-Service wuauserv, bits -Force -ErrorAction SilentlyContinue
Remove-Item 'C:\Windows\SoftwareDistribution\Download\*' -Recurse -Force -ErrorAction SilentlyContinue
Start-Service bits, wuauserv -ErrorAction SilentlyContinue
try { Delete-DeliveryOptimizationCache -Force -ErrorAction Stop } catch {}
L "  livre agora: $(Livre) GB"

L 'ETAPA 2/5: limpando arquivos temporarios (os que estao em uso ficam)'
Remove-Item "$env:WINDIR\Temp\*" -Recurse -Force -ErrorAction SilentlyContinue
Get-ChildItem 'C:\Users' -Directory | ForEach-Object { Get-ChildItem "$($_.FullName)\AppData\Local\Temp" -Force -ErrorAction SilentlyContinue | Where-Object { $_.Name -ne 'claude' } | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue }
L "  livre agora: $(Livre) GB"

L 'ETAPA 3/5: DISM - limpeza de componentes antigos do Windows (demora)'
$o = DISM /Online /Cleanup-Image /StartComponentCleanup 2>&1 | Select-Object -Last 2; $o | ForEach-Object { L "  $_" }
L "  livre agora: $(Livre) GB"

L 'ETAPA 4/5: verificacao dos arquivos do Windows (DISM RestoreHealth + sfc)'
$o = DISM /Online /Cleanup-Image /RestoreHealth 2>&1 | Select-Object -Last 2; $o | ForEach-Object { L "  DISM: $_" }
$o = (sfc /scannow) -join ' ' -replace "`0", ''
if ($o -match 'n.o encontrou nenhuma viola|did not find any integrity') { L '  SFC: nenhum problema encontrado' }
elseif ($o -match 'reparou|successfully repaired') { L '  SFC: encontrou e REPAROU arquivos corrompidos' }
else { L "  SFC: $($o.Substring([math]::Max(0,$o.Length-300)))" }

L 'ETAPA 5/5: verificacao COMPLETA do Microsoft Defender (pode levar 30-90 min)'
try { Update-MpSignature -ErrorAction SilentlyContinue } catch {}
try {
  Start-MpScan -ScanType FullScan -ErrorAction Stop
  $t = Get-MpThreatDetection -ErrorAction SilentlyContinue | Where-Object { $_.InitialDetectionTime -gt (Get-Date).AddHours(-3) }
  if ($t) { L "  ATENCAO: $(@($t).Count) ameaca(s) encontrada(s):"; Get-MpThreat | ForEach-Object { L "    $($_.ThreatName)" } } else { L '  Defender: nenhuma ameaca encontrada' }
} catch { L "  ERRO Defender: $($_.Exception.Message)" }

L "Espaco livre depois: $(Livre) GB (liberou $([math]::Round((Livre)-$antes,1)) GB)"
L 'FIM'
