# Fecha TODOS os processos do WhatsApp (principal + webview2 dele) e abre de novo.
param([string]$Saida = "$env:USERPROFILE\Downloads\TITI-AI\manutencao-pc")
New-Item -ItemType Directory -Force $Saida | Out-Null
$out = Join-Path $Saida 'reiniciar-whatsapp.txt'
$r = @()
$procs = Get-CimInstance Win32_Process | Where-Object { $_.Name -like 'WhatsApp*' -or ($_.Name -eq 'msedgewebview2.exe' -and $_.CommandLine -match 'WhatsApp') }
$r += "Antes: $(@($procs).Count) processo(s) do WhatsApp"
$procs | ForEach-Object { $r += "  $($_.ProcessId) $($_.Name)" }
foreach ($p in $procs) { try { Stop-Process -Id $p.ProcessId -Force -ErrorAction Stop } catch { $r += "  nao fechou $($p.ProcessId): $($_.Exception.Message)" } }
Start-Sleep 3
$sobra = Get-CimInstance Win32_Process | Where-Object { $_.Name -like 'WhatsApp*' -or ($_.Name -eq 'msedgewebview2.exe' -and $_.CommandLine -match 'WhatsApp') }
$r += "Depois de fechar: $(@($sobra).Count) processo(s)"
Start-Process 'shell:AppsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App'
Start-Sleep 12
$novo = Get-Process -Name 'WhatsApp*' -ErrorAction SilentlyContinue
foreach ($n in $novo) { $r += "Novo: $($n.Id) $($n.ProcessName) respondendo=$($n.Responding) janela='$($n.MainWindowTitle)' handle=$($n.MainWindowHandle)" }
$wv = @(Get-CimInstance Win32_Process | Where-Object { $_.Name -eq 'msedgewebview2.exe' -and $_.CommandLine -match 'WhatsApp' }).Count
$r += "WebView2 do WhatsApp rodando: $wv"
$r | Set-Content $out -Encoding UTF8
$r
