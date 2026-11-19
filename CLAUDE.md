# Instruções para o Claude neste repositório

Este repositório é a cópia de segurança das skills e do jeito de trabalhar do autor. Ele cria vídeos curtos com IA (séries animadas para TikTok e YouTube). Fale sempre em português do Brasil, de forma simples: o autor não é programador, então você roda os comandos e explica o resultado.

## Regra fixa: toda skill vai para o GitHub

Sempre que criar ou alterar uma skill (em `%USERPROFILE%\.claude\skills\<nome>\`):
1. Copie a pasta da skill para `skills/<nome>/` neste repositório.
2. Atualize a tabela de skills do `README.md`.
3. Faça commit e push para a `main` de `digitadorg/kids`, sem esperar o autor pedir.

Nunca coloque chaves de API, senhas ou o arquivo `.env` no repositório.

## Situação do computador (18/11/2026)

- Notebook Samsung Galaxy Book2 **NP550XED-KT3BR**: Core i3-1215U, 16 GB de RAM, BIOS P11RGK.
- **SSD NVMe interno de fábrica (256 GB) com defeito**: ele some e volta, e deu o erro `0xc0000218`. Hoje a BIOS e o Windows não enxergam esse disco como unidade; o controlador dele (`PCI\VEN_144D&DEV_A809`) aparece com erro e foi **desabilitado** no Gerenciador de Dispositivos em 18/11/2026 (não desinstalado). Inicialização rápida desligada e botão de energia = Desligar desde 18/11/2026. Ele está aguardando um técnico para reencaixar ou ler os dados com um adaptador NVMe-USB. **Não formate nem inicialize esse disco se ele aparecer**: primeiro copie a antiga pasta `C:\LAILLA_AUTOMACAO`. Não havia chave de BitLocker na conta Microsoft, então ele provavelmente está sem criptografia.
- **Disco atual:** SSD SATA 2,5" de 480 GB (aparece como "P4-480"), no espaço do HD. É o `C:`, com o Windows 11 Pro recém-instalado pela loja.
- O `C:` está "BitLocker Criptografado", mas com a proteção **desligada** (o menu oferece "Ligar BitLocker"). Não ligue o BitLocker sem o autor salvar a chave de recuperação.
- A licença de fábrica é **Windows 11 Home** (a chave fica gravada na placa). A loja instalou e ativou a **Pro**. Falta confirmar com a loja se a chave Pro é original. Se não for, o caminho é voltar para a Home, que ativa de graça.
- **Pasta de trabalho nova:** `C:\Users\<usuário>\Downloads\TITI-AI`. É aqui que ficam os projetos agora, no lugar da antiga `C:\LAILLA_AUTOMACAO`.

## Skills salvas aqui

| Skill | Situação |
|---|---|
| `skills/serie-peaky-shelby` | Completa. A pasta `modelos\` (com `plano.py`, `narrar.py`, `animar_ep.py`, `montar_ep.py` e os `pedido-*.json`) se perdeu no SSD antigo e precisa ser refeita ou recuperada. Atualize os caminhos de `C:\LAILLA_AUTOMACAO` para a pasta nova. |
| `skills/codex-imagens` | Reconstruída e testada com o Codex de verdade em 18/11/2026. Requer o Codex CLI (`npm install -g @openai/codex`) e `codex login` com a conta do ChatGPT do autor. O `gerar.py` fica dentro da pasta da skill. |
| `skills/saude-do-computador` | Criada em 19/11/2026 a partir da manutenção completa do notebook. Scripts em `scripts\`; os relatórios vão para `TITI-AI\manutencao-pc\`. |

Para instalar: copie `skills/<nome>` para `%USERPROFILE%\.claude\skills\<nome>`.

## Ferramentas que o autor usava (reinstalar quando precisar)

- **Codex CLI:** gera imagens em lote pela assinatura do ChatGPT, sem custo (skill `codex-imagens`).
- **Grok Imagine (xAI):** anima as imagens e faz as falas com boca sincronizada. A chave fica em `XAI_API_KEY` no `.env`. O autor recarrega o saldo sozinho, então nunca faça pagamentos.
- **ElevenLabs:** narração (plano free, cerca de 10 mil caracteres por mês). A chave fica em `ELEVENLABS_API_KEY` no `.env`.
- **ffmpeg:** montagem, legenda ASS palavra a palavra e loudnorm em −14 LUFS.
- **raea** e **rea-video** (engenharia reversa de vídeo) estavam instalados no SSD antigo e se perderam.
- **Fábrica de Criativos:** pacote de skills e comandos (`/fca-instalar`, `/fca-conectar`, `/fca-voz-local` e outros). Reinstalar pelo pacote original devolve dezenas de skills que não foram recuperadas.

## Preferências do autor (memórias recuperadas)

- **Tudo dentro de uma pasta de trabalho só.** Antes era `C:\LAILLA_AUTOMACAO`, agora é a `TITI-AI`. Nunca espalhe arquivos de trabalho pelo computador.
- **Painel de progresso ao vivo:** em todo render ou tarefa longa, mostre o progresso (% e tempo restante) sem esperar o autor pedir.
- **"Space" sempre aberto:** nos projetos de vídeo, o autor gosta de um quadro visual de etapas, no estilo Freepik Spaces, mostrando cada etapa ao vivo.
- **Orçamento antes de gastar:** passe o custo previsto antes de usar APIs pagas e anote os gastos.
- **Personagens sempre estilizados** (3D cartoon), nunca rosto realista de ator.
- Sempre legenda palavra a palavra nos vídeos.
- Mande uma versão leve para celular dos vídeos finais (720×1280, menos de 30 MB).

## Ao mexer no Windows

- Antes de mudanças grandes, crie um **ponto de restauração**.
- Não mexa em BIOS, partições ou BitLocker sem pedir.
- Pergunte antes de desinstalar programas ou desligar serviços.
- Mostre o que vai fazer, faça, e no fim diga o que mudou e se precisa reiniciar.
