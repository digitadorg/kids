---
name: saude-do-computador
description: Faz a verificação de saúde completa e a manutenção do notebook Windows do autor — varredura só leitura (espaço, lixo, drivers, segurança, desempenho, erros), saúde do SSD/bateria/hardware (temperatura, desgaste, erros SMART), atualizações (Windows Update sem drivers velhos, winget, Intel DSA, Samsung Update), limpeza, DISM/sfc e varredura completa do Defender, com relatório simples em PT-BR. Use quando o autor pedir "verifica a saúde do computador", "faz uma varredura", "deixa o PC mais rápido", "limpa o lixo", "atualiza tudo", "confere o SSD", "check-up do notebook", "manutenção do Windows" ou "continua a manutenção".
---

# Saúde e manutenção do computador

Receita usada em 18 e 19/11/2026 no notebook Samsung Galaxy Book2 do autor (ver `CLAUDE.md` do repo `digitadorg/kids` para o histórico do SSD NVMe com defeito). O autor não é programador: explique em português simples, com tabelas curtas e ✅ / ⚠️.

Scripts em `scripts\` nesta skill. Todos gravam relatórios e logs em `%USERPROFILE%\Downloads\TITI-AI\manutencao-pc\` (parâmetro `-Saida` muda a pasta). Nunca grave logs na pasta Temp: a limpeza apaga.

## Regras (não negociáveis)

1. **Primeiro olhar, depois mexer.** Comece sempre pela varredura só leitura e mostre o relatório antes de mudar qualquer coisa.
2. **Ponto de restauração antes de mudanças grandes.** O Windows só cria 1 por 24 h: se já existe um de hoje, ele reaproveita (avise o autor, não é erro).
3. **Pergunte antes** de desinstalar programas, desligar serviços ou apagar dados do autor. Apps de fábrica só com a lista aprovada.
4. **Nunca mexa** em BIOS, partições, BitLocker ou no SSD NVMe antigo (não formatar, não inicializar). Se aparecer atualização de BIOS no Samsung Update, peça para o autor avisar antes.
5. **Configurações do sistema e de segurança** (modo de energia, inicialização rápida, programas que abrem com o Windows, Defender, Otimização de Entrega, PCIe ASPM): **você não altera**. Abra a tela certa (`Start-Process 'ms-settings:...'`, `devmgmt.msc`, `powercfg.cpl`) e diga exatamente onde clicar. Depois confira se foi salvo (ex.: `HiberbootEnabled` no registro).
6. **Não instale os drivers opcionais antigos do Windows Update** (Intel de 2018/2019, "Xeon", data 1968). Drivers vêm do **Intel DSA** e do **Samsung Update**.
7. Mostre o progresso durante tarefas longas (etapa N/M, tempo esperado) sem o autor pedir.

## Pegadinhas do ambiente (importante)

- A ferramenta PowerShell do Claude roda num **ambiente isolado**: `npm -g` e algumas gravações ali não chegam ao PC real, e leituras de sistema dão "Acesso negado". **Rode os scripts pelo terminal do app** (`run_in_terminal`), não pela ferramenta PowerShell.
- Para administrador: `Start-Process powershell -Verb RunAs -ArgumentList '-NoProfile','-ExecutionPolicy','Bypass','-File','<script>'`. Aparece a janela do UAC e **o autor precisa clicar em "Sim"** (às vezes ela fica atrás do app). Se der "operação cancelada pelo usuário", peça para clicar e tente de novo.
- `run_in_terminal` não aceita pipes, variáveis nem `$(...)`: coloque a lógica num `.ps1` e rode o arquivo.
- No terminal real, `codex`/scripts `.ps1` do npm são bloqueados pela política de execução: use `codex.cmd`.
- Depois de instalar algo com winget, atualize o PATH da sessão: `$env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User')`.

## Passo a passo

### 1. Varredura só leitura (sem admin)
`powershell -NoProfile -ExecutionPolicy Bypass -File scripts\varredura.ps1` → `varredura.txt`:
espaço (pastas grandes, caches, hiberfil, Windows Update), drivers com problema e versões, segurança (firewall, UAC, integridade de memória, VBS, Secure Boot, ativação), programas instalados e apps da Store, desempenho (RAM, processos, serviços de terceiros), erros do sistema em 48 h, desligamentos inesperados e erros de disco em 7 dias.

### 2. Saúde do hardware (admin)
`scripts\saude-disco.ps1` → `saude-disco-AAAA-MM-DD.txt`: temperatura, desgaste (%), horas ligado e erros de leitura/escrita de cada SSD; estado dos controladores de armazenamento; eventos de NVMe, disco, WHEA, NTFS e desligamentos em 14 dias; capacidade da bateria (`bateria.html`); resultado do teste de memória.

**Sinais de alerta** (avise o autor na hora): desgaste > 80 %; erros não corrigidos > 0; temperatura do SSD > 70 °C; qualquer evento `stornvme 11`, `disk 7/51/153`, WHEA ou NTFS 55; bateria < 70 % da capacidade de fábrica.

### 3. Velocidade da internet (opcional)
`scripts\velocidade.ps1` → ping roteador/Cloudflare/Google e 2 downloads de 50 MB. Rode no terminal real (no ambiente isolado a medição sai falsa, ~8 Mbps). Lentidão durante download grande do Windows Update é normal.

### 4. Atualizações (admin) — `scripts\manutencao.ps1`
1/4 ponto de restauração (se falhar, para tudo) · 2/4 Windows Update **só software** (sem drivers) · 3/4 `winget upgrade --all` · 4/4 instala Intel DSA (`Intel.IntelDriverAndSupportAssistant`) e Samsung Update (Store `9NQ3HDB99VBF`).
Acompanhe `manutencao.log`. Atualização de versão (ex.: 26H2) baixa ~5 GB e instala em ~20 min; **não reinicie antes do `FIM`**. Depois, peça para o autor reiniciar e dizer "voltei".

### 5. Apps de fábrica (sem admin, só com OK do autor)
`scripts\remover-apps.ps1 [-Apps nome1,nome2]`. A lista padrão: Bing Notícias/Clima, Paciência, Clipchamp, Power Automate, Hub de Comentários, Obter Ajuda, To Do, app Xbox e componentes. **Mantenha a Xbox Game Bar** (grava tela, útil para os vídeos) a menos que o autor peça.

### 6. Depois do reinício (admin) — `scripts\pos-reinicio.ps1`
1/5 apaga instaladores do Windows Update e cache de entrega · 2/5 temporários (preserva a pasta `Temp\claude`) · 3/5 `DISM /StartComponentCleanup` · 4/5 `DISM /RestoreHealth` + `sfc /scannow` · 5/5 Defender `FullScan` (30–90 min). Mostra quanto espaço liberou.
**Nunca** apague `SoftwareDistribution\Download` nem rode DISM com reinício pendente.
Se o autor precisar desligar no meio, pode: sfc e Defender aguentam interrupção. Para retomar, rode só o que faltou (sfc + Defender) e anote na memória o que ficou pendente.

### 7. Telas para o autor ajustar (você guia, ele clica)
- **Inicialização rápida:** Painel de Controle → Opções de Energia → "Escolher a função dos botões de energia" → "Alterar configurações não disponíveis" → desmarcar → **Salvar alterações**. Conferir `HiberbootEnabled = 0`.
- **Botão de energia = Desligar** (mesma tela), para o desligamento de verdade à noite.
- **PCIe ASPM:** Opções de Energia → plano → avançadas → PCI Express → Gerenciamento de Energia do Estado de Link: Desativado (tomada) / Economia moderada (bateria).
- **Programas na inicialização:** `ms-settings:startupapps` (tirar Teams, Office, Edge).
- **Hibernação menor:** Terminal (Administrador) → `powercfg /h /type reduced`.
- **Dispositivo com defeito (ex.: NVMe antigo):** Gerenciador de Dispositivos → botão direito → **Desabilitar** (nunca "Desinstalar").

### 8. Relatório final
Tabela ✅/⚠️ com: o que foi atualizado, espaço liberado, resultado do sfc/DISM/Defender, saúde dos discos, o que o autor ainda precisa fazer e se precisa reiniciar. Guarde uma cópia em `manutencao-pc\`.

## Rotina recomendada
- **Toda semana:** desligar de verdade pelo menos uma vez; deixar o Windows Update rodar.
- **Todo mês:** passos 1, 2 e 4 (varredura, saúde do hardware, atualizações) + Samsung Update e Intel DSA.
- **A cada 3 meses:** passo 6 completo (limpeza, DISM, sfc, Defender completo) e backup da pasta `TITI-AI`.
