param([string]$Saida = "$env:USERPROFILE\Downloads\TITI-AI\manutencao-pc")
New-Item -ItemType Directory -Force $Saida | Out-Null
$out = Join-Path $Saida 'varredura.txt'
Start-Transcript -Path $out -Force | Out-Null
$ProgressPreference = 'SilentlyContinue'
function GB($p) { if (Test-Path $p) { [math]::Round(((Get-ChildItem $p -Recurse -Force -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum/1GB),2) } else { 'nao existe' } }

"=== ESPACO: pastas grandes do usuario ==="
Get-ChildItem $env:USERPROFILE -Directory -Force -ErrorAction SilentlyContinue | ForEach-Object { [pscustomobject]@{Pasta=$_.Name; GB=(GB $_.FullName)} } | Where-Object { $_.GB -is [double] -and $_.GB -gt 0.1 } | Sort-Object GB -Descending | Format-Table -AutoSize | Out-String
"--- AppData\Local maiores ---"
Get-ChildItem "$env:LOCALAPPDATA" -Directory -Force -ErrorAction SilentlyContinue | ForEach-Object { [pscustomobject]@{Pasta=$_.Name; GB=(GB $_.FullName)} } | Where-Object { $_.GB -is [double] -and $_.GB -gt 0.2 } | Sort-Object GB -Descending | Select-Object -First 12 | Format-Table -AutoSize | Out-String
"--- Raiz do C: ---"
Get-ChildItem C:\ -Force -ErrorAction SilentlyContinue | Where-Object { -not $_.PSIsContainer } | Select-Object Name, @{n='GB';e={[math]::Round($_.Length/1GB,2)}} | Format-Table -AutoSize | Out-String
"--- Caches conhecidos ---"
"TEMP usuario: " + (GB $env:TEMP)
"Cache npm: " + (GB "$env:LOCALAPPDATA\npm-cache")
"Cache pip: " + (GB "$env:LOCALAPPDATA\pip\cache")
"Cache Edge: " + (GB "$env:LOCALAPPDATA\Microsoft\Edge\User Data\Default\Cache")
"Cache Firefox: " + (GB "$env:LOCALAPPDATA\Mozilla\Firefox\Profiles")
"Cache instaladores winget: " + (GB "$env:LOCALAPPDATA\Temp\WinGet")
"Downloads: " + (GB "$env:USERPROFILE\Downloads")
"Windows Update Download: " + (GB 'C:\Windows\SoftwareDistribution\Download')
"Otimizacao de Entrega: " + (GB 'C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Microsoft\Windows\DeliveryOptimization\Cache')
try { $sh = New-Object -ComObject Shell.Application; $rb = $sh.Namespace(10); "Lixeira: $($rb.Items().Count) item(ns)" } catch {}
"Arquivos grandes (>500 MB) no perfil:"
Get-ChildItem $env:USERPROFILE -Recurse -File -Force -ErrorAction SilentlyContinue | Where-Object Length -gt 500MB | Select-Object FullName, @{n='GB';e={[math]::Round($_.Length/1GB,2)}} | Format-Table -AutoSize -Wrap | Out-String -Width 220

"=== DRIVERS: dispositivos com problema ==="
Get-PnpDevice -PresentOnly -ErrorAction SilentlyContinue | Where-Object { $_.Status -ne 'OK' } | Select-Object Status, Class, FriendlyName, InstanceId | Format-Table -AutoSize -Wrap | Out-String -Width 220
"--- Drivers principais ---"
Get-CimInstance Win32_PnPSignedDriver | Where-Object { $_.DeviceClass -in 'DISPLAY','NET','MEDIA','SYSTEM','BLUETOOTH','HDC','SCSIADAPTER' -and $_.Manufacturer -notmatch 'Microsoft|Padr' } | Select-Object DeviceClass, DeviceName, DriverVersion, @{n='Data';e={$_.DriverDate.ToString('yyyy-MM-dd')}} | Sort-Object DeviceClass | Format-Table -AutoSize | Out-String -Width 220

"=== SEGURANCA ==="
Get-NetFirewallProfile | Select-Object Name, Enabled | Format-Table -AutoSize | Out-String
$uac = Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System'
"UAC ligado: $($uac.EnableLUA)  | nivel ConsentPromptBehaviorAdmin: $($uac.ConsentPromptBehaviorAdmin)"
try { "Isolamento de nucleo (integridade de memoria): " + (Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\DeviceGuard\Scenarios\HypervisorEnforcedCodeIntegrity' -ErrorAction Stop).Enabled } catch { "Isolamento de nucleo: sem registro (desligado)" }
try { "SmartScreen: " + (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer' -ErrorAction Stop).SmartScreenEnabled } catch {}
try { $dg = Get-CimInstance -Namespace root\Microsoft\Windows\DeviceGuard -ClassName Win32_DeviceGuard -ErrorAction Stop; "VBS status: $($dg.VirtualizationBasedSecurityStatus) | servicos rodando: $($dg.SecurityServicesRunning -join ',')" } catch {}
"Secure Boot (registro): " + (Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\SecureBoot\State' -ErrorAction SilentlyContinue).UEFISecureBootEnabled
"--- Ativacao do Windows ---"
Get-CimInstance SoftwareLicensingProduct -Filter "PartialProductKey IS NOT NULL AND Name LIKE 'Windows%'" | Select-Object Name, Description, LicenseStatus, ProductKeyChannel | Format-List | Out-String
"--- Programas instalados ---"
$apps = foreach ($k in 'HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*','HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*','HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*') { Get-ItemProperty $k -ErrorAction SilentlyContinue | Where-Object DisplayName | Select-Object DisplayName, DisplayVersion, Publisher }
$apps | Sort-Object DisplayName -Unique | Format-Table -AutoSize | Out-String -Width 200
"--- Apps da Store (nao Microsoft-sistema) ---"
Get-AppxPackage | Where-Object { -not $_.IsFramework -and $_.SignatureKind -eq 'Store' } | Select-Object Name | Sort-Object Name | Format-Table -HideTableHeaders | Out-String

"=== DESEMPENHO ==="
$os = Get-CimInstance Win32_OperatingSystem
"RAM livre: {0:N1} GB de {1:N1} GB" -f ($os.FreePhysicalMemory/1MB), ($os.TotalVisibleMemorySize/1MB)
"Arquivo de paginacao:"; Get-CimInstance Win32_PageFileUsage | Select-Object Name, AllocatedBaseSize, CurrentUsage | Format-Table -AutoSize | Out-String
"Hibernacao (hiberfil): " + $(if (Test-Path C:\hiberfil.sys -ErrorAction SilentlyContinue) {'existe'} else {'nao'})
"Top processos por memoria:"
Get-Process | Sort-Object WS -Descending | Select-Object -First 12 Name, @{n='MB';e={[math]::Round($_.WS/1MB)}} | Format-Table -AutoSize | Out-String
"Servicos de terceiros rodando:"
Get-CimInstance Win32_Service | Where-Object { $_.State -eq 'Running' -and $_.PathName -notmatch 'Windows\\System32|Windows\\SysWOW64|svchost' } | Select-Object Name, DisplayName, StartMode | Format-Table -AutoSize | Out-String -Width 200
try { "Efeitos visuais (VisualFXSetting): " + (Get-ItemProperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects' -ErrorAction Stop).VisualFXSetting } catch {}
try { "Inicializacao rapida (HiberbootEnabled): " + (Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\Power').HiberbootEnabled } catch {}

"=== ERROS DO SISTEMA (ultimas 48h, criticos e erros) ==="
try { Get-WinEvent -FilterHashtable @{LogName='System'; Level=1,2; StartTime=(Get-Date).AddHours(-48)} -MaxEvents 300 -ErrorAction Stop | Group-Object ProviderName, Id | Sort-Object Count -Descending | Select-Object -First 15 Count, Name, @{n='Exemplo';e={ ($_.Group[0].Message -split "`n")[0].Substring(0, [math]::Min(140, ($_.Group[0].Message -split "`n")[0].Length)) }} | Format-Table -AutoSize -Wrap | Out-String -Width 250 } catch { "Erro lendo log: $($_.Exception.Message)" }
try { "Desligamentos inesperados (41/6008) em 7 dias: " + (Get-WinEvent -FilterHashtable @{LogName='System'; Id=41,6008; StartTime=(Get-Date).AddDays(-7)} -ErrorAction Stop).Count } catch { "Desligamentos inesperados em 7 dias: 0" }
try { "Erros de disco (7/51/153/129) em 7 dias: " + (Get-WinEvent -FilterHashtable @{LogName='System'; Id=7,51,153,129; StartTime=(Get-Date).AddDays(-7)} -ErrorAction Stop).Count } catch { "Erros de disco em 7 dias: 0" }
"--- Discos fisicos ---"
Get-PhysicalDisk | Select-Object FriendlyName, MediaType, BusType, HealthStatus, OperationalStatus, @{n='GB';e={[math]::Round($_.Size/1GB)}} | Format-Table -AutoSize | Out-String
Get-Disk | Select-Object Number, FriendlyName, PartitionStyle, OperationalStatus, @{n='GB';e={[math]::Round($_.Size/1GB)}} | Format-Table -AutoSize | Out-String
Stop-Transcript | Out-Null
