# Saude dos discos e do hardware. Rodar COMO ADMINISTRADOR (Start-Process powershell -Verb RunAs ...).
# So le informacoes: temperatura, desgaste, horas ligado, erros do SSD, bateria e eventos de hardware.
param([string]$Saida = "$env:USERPROFILE\Downloads\TITI-AI\manutencao-pc")
New-Item -ItemType Directory -Force $Saida | Out-Null
$out = Join-Path $Saida ('saude-disco-' + (Get-Date -Format 'yyyy-MM-dd') + '.txt')
Start-Transcript -Path $out -Force | Out-Null

"=== DISCOS (SMART / confiabilidade) ==="
foreach ($d in Get-PhysicalDisk) {
  "--- $($d.FriendlyName) | $($d.BusType) | $($d.MediaType) | saude: $($d.HealthStatus) | $([math]::Round($d.Size/1GB)) GB"
  try {
    $c = $d | Get-StorageReliabilityCounter -ErrorAction Stop
    "  Temperatura agora: $($c.Temperature) C (max registrada: $($c.TemperatureMax) C)"
    "  Desgaste: $($c.Wear) %   (0 = novo, 100 = fim da vida util)"
    "  Horas ligado: $($c.PowerOnHours)   | Ciclos liga/desliga: $($c.StartStopCycleCount)"
    "  Erros de leitura (corrigidos/nao corrigidos): $($c.ReadErrorsCorrected) / $($c.ReadErrorsUncorrected)"
    "  Erros de escrita (corrigidos/nao corrigidos): $($c.WriteErrorsCorrected) / $($c.WriteErrorsUncorrected)"
  } catch { "  Contadores SMART indisponiveis: $($_.Exception.Message)" }
}

"=== DISPOSITIVOS NVMe / ARMAZENAMENTO ==="
Get-PnpDevice -Class SCSIAdapter, HDC, DiskDrive -ErrorAction SilentlyContinue | Select-Object Status, Problem, FriendlyName | Format-Table -AutoSize | Out-String -Width 200

"=== EVENTOS DE DISCO E ENERGIA (14 dias) ==="
$ini = (Get-Date).AddDays(-14)
foreach ($q in @(
  @{n='Erros de controlador NVMe (stornvme 11)'; f=@{LogName='System'; ProviderName='stornvme'; StartTime=$ini}},
  @{n='Erros de disco (disk 7/51/153)'; f=@{LogName='System'; ProviderName='disk'; Id=7,51,153; StartTime=$ini}},
  @{n='Resets do controlador SATA (storahci 129)'; f=@{LogName='System'; ProviderName='storahci'; Id=129; StartTime=$ini}},
  @{n='Desligamentos inesperados (41/6008)'; f=@{LogName='System'; Id=41,6008; Level=1,2; StartTime=$ini}},
  @{n='Erros de hardware WHEA (so avisos/erros, sem os informativos do boot)'; f=@{LogName='System'; ProviderName='Microsoft-Windows-WHEA-Logger'; Level=1,2,3; StartTime=$ini}},
  @{n='Corrupcao no NTFS (55, so erros)'; f=@{LogName='System'; ProviderName='Microsoft-Windows-Ntfs','Ntfs'; Id=55; Level=1,2; StartTime=$ini}}
)) {
  $ev = @(Get-WinEvent -FilterHashtable $q.f -ErrorAction SilentlyContinue)
  "$($q.n): $($ev.Count)" + $(if ($ev.Count) { "  (ultimo: $($ev[0].TimeCreated))" } else { '' })
}

"=== BATERIA ==="
try {
  $f = Join-Path $Saida 'bateria.html'
  powercfg /batteryreport /output "$f" | Out-Null
  $t = Get-Content $f -Raw
  $proj = if ($t -match 'DESIGN CAPACITY</span></td><td>([\d\.,]+)') { $Matches[1] } else { '?' }
  $real = if ($t -match 'FULL CHARGE CAPACITY</span></td><td>([\d\.,]+)') { $Matches[1] } else { '?' }
  "Capacidade de fabrica: $proj mWh | Capacidade atual: $real mWh (relatorio completo: $f)"
} catch { "Relatorio de bateria indisponivel" }

"=== TEMPERATURA DO SISTEMA (sensor ACPI, se existir) ==="
try { Get-CimInstance -Namespace root/wmi -ClassName MSAcpi_ThermalZoneTemperature -ErrorAction Stop | ForEach-Object { "$($_.InstanceName): {0:N0} C" -f (($_.CurrentTemperature / 10) - 273.15) } } catch { 'Sensor nao exposto pelo notebook' }

"=== MEMORIA RAM: resultados do Diagnostico de Memoria do Windows ==="
$m = @(Get-WinEvent -FilterHashtable @{LogName='System'; ProviderName='Microsoft-Windows-MemoryDiagnostics-Results'} -MaxEvents 3 -ErrorAction SilentlyContinue)
if ($m.Count) { $m | ForEach-Object { "$($_.TimeCreated): $(($_.Message -split "`n")[0])" } } else { 'Nunca rodou (mdsched.exe agenda o teste no proximo reinicio)' }
Stop-Transcript | Out-Null
