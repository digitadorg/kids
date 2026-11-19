param([string]$Saida = "$env:USERPROFILE\Downloads\TITI-AI\manutencao-pc")
New-Item -ItemType Directory -Force $Saida | Out-Null
$out = Join-Path $Saida 'velocidade.txt'
$r = @()
$p = Test-Connection 8.8.8.8 -Count 5 | Measure-Object ResponseTime -Average -Maximum
$r += "Ping Google: media {0:N0} ms, max {1} ms" -f $p.Average, $p.Maximum
$p2 = Test-Connection 1.1.1.1 -Count 5 | Measure-Object ResponseTime -Average
$r += "Ping Cloudflare: media {0:N0} ms" -f $p2.Average
$gw = (Get-NetRoute -DestinationPrefix '0.0.0.0/0' | Select-Object -First 1).NextHop
$p3 = Test-Connection $gw -Count 5 | Measure-Object ResponseTime -Average
$r += "Ping roteador ($gw): media {0:N0} ms" -f $p3.Average
$ProgressPreference = 'SilentlyContinue'
foreach ($n in 1..2) {
  $sw = [Diagnostics.Stopwatch]::StartNew()
  try { $w = Invoke-WebRequest 'https://speed.cloudflare.com/__down?bytes=50000000' -UseBasicParsing -TimeoutSec 90; $sw.Stop(); $r += "Download teste ${n}: {0:N0} Mbps" -f ($w.RawContentLength*8/$sw.Elapsed.TotalSeconds/1e6) } catch { $r += "Download teste ${n} falhou: $($_.Exception.Message)" }
}
$a = Get-NetAdapter -Name 'Ethernet 2'
$r += "Cabo: $($a.LinkSpeed), $($a.Status)"
try { $d = Get-DeliveryOptimizationStatus | Measure-Object -Property FileSizeInCache -Sum; $r += "Otimizacao de Entrega ativa: $((Get-DeliveryOptimizationStatus).Count) arquivo(s)" } catch {}
$r | Set-Content $out -Encoding UTF8
$r
