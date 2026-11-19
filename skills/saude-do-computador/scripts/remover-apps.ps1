param([string]$Saida = "$env:USERPROFILE\Downloads\TITI-AI\manutencao-pc", [string[]]$Apps)
New-Item -ItemType Directory -Force $Saida | Out-Null
$out = Join-Path $Saida 'remover-apps.txt'
$ProgressPreference = 'SilentlyContinue'
$padrao = @(
  'Microsoft.BingNews',
  'Microsoft.BingWeather',
  'Microsoft.MicrosoftSolitaireCollection',
  'Clipchamp.Clipchamp',
  'Microsoft.PowerAutomateDesktop',
  'Microsoft.WindowsFeedbackHub',
  'Microsoft.GetHelp',
  'Microsoft.Todos',
  'Microsoft.GamingApp',
  'Microsoft.XboxSpeechToTextOverlay',
  'Microsoft.XboxIdentityProvider',
  'Microsoft.Xbox.TCUI'
)
if (-not $Apps) { $Apps = $padrao }
$r = @()
foreach ($a in $Apps) {
  $p = Get-AppxPackage -Name $a
  if (-not $p) { $r += "ja nao estava: $a"; continue }
  try { $p | Remove-AppxPackage -ErrorAction Stop; $r += "REMOVIDO: $a" } catch { $r += "FALHOU: $a -> $($_.Exception.Message)" }
}
$r | Set-Content $out -Encoding UTF8
$r
