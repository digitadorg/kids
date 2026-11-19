# Baixa o driver de video Intel 101.7092 (11a-14a geracao), confere o SHA512 e instala em modo silencioso (admin).
param([switch]$SoBaixar)
$dir = 'C:\Users\Thiago\Downloads\TITI-AI\drivers\intel-gfx-101.7092'
$exe = Join-Path $dir 'gfx_win_101.7092.exe'
$url = 'https://downloadmirror.intel.com/929468/gfx_win_101.7092.exe'
$sha = '35a863fc2ace37e267a1602eb992e54f909dbce6122b7224ad500301bbdb2389c38741800ffc4e389d91e1444bc96c2e26ee4283c97c4a7c7060064724385b9d'
$log = 'C:\Users\Thiago\Downloads\TITI-AI\manutencao-pc\driver-intel.log'
function L($m) { $linha = (Get-Date -Format 'HH:mm:ss') + '  ' + $m; Add-Content -Path $log -Value $linha -Encoding UTF8; Write-Host $linha }
New-Item -ItemType Directory -Force $dir | Out-Null

if ($SoBaixar) {
  Set-Content -Path $log -Value '' -Encoding UTF8
  L "Baixando $url (744,7 MB)..."
  curl.exe -L --fail --silent --show-error -o "$exe" "$url"
  if ($LASTEXITCODE -ne 0) { L "ERRO no download (codigo $LASTEXITCODE)"; exit 1 }
  L ("Baixado: {0:N1} MB" -f ((Get-Item $exe).Length/1MB))
  $h = (Get-FileHash $exe -Algorithm SHA512).Hash.ToLower()
  if ($h -eq $sha) { L 'SHA512 CONFERE com o publicado pela Intel: arquivo original.' ; L 'DOWNLOAD_OK' }
  else { L "SHA512 NAO CONFERE ($h). Arquivo apagado por seguranca."; Remove-Item $exe -Force; L 'DOWNLOAD_FALHOU'; exit 1 }
  $sig = Get-AuthenticodeSignature $exe
  L "Assinatura digital: $($sig.Status) - $($sig.SignerCertificate.Subject)"
  exit 0
}

# Instalacao (rodar como administrador)
$antes = (Get-CimInstance Win32_VideoController | Where-Object Name -match 'Intel').DriverVersion
L "Versao antes: $antes"
$h = (Get-FileHash $exe -Algorithm SHA512).Hash.ToLower()
if ($h -ne $sha) { L 'SHA512 nao confere, instalacao cancelada.'; exit 1 }
L 'Instalando em modo silencioso (a tela pode piscar ou ficar preta alguns segundos)...'
$p = Start-Process -FilePath $exe -ArgumentList '-s' -Wait -PassThru
L "Instalador terminou com codigo $($p.ExitCode)"
Start-Sleep 5
$depois = (Get-CimInstance Win32_VideoController | Where-Object Name -match 'Intel').DriverVersion
L "Versao depois: $depois"
L 'FIM_INSTALACAO'
