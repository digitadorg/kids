param([string]$Imagem)
Set-ItemProperty 'HKCU:\Control Panel\Desktop' WallpaperStyle '10'
Set-ItemProperty 'HKCU:\Control Panel\Desktop' TileWallpaper '0'
Add-Type @'
using System.Runtime.InteropServices;
public class WP2 { [DllImport("user32.dll", CharSet=CharSet.Unicode)] public static extern int SystemParametersInfo(int a, int b, string c, int d); }
'@
$ok = [WP2]::SystemParametersInfo(20, 0, $Imagem, 3)
if ($ok) { "PAPEL_TROCADO: $Imagem" } else { "FALHOU" }
