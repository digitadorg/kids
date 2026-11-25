---
name: codex-ajudante
description: O Claude orquestra e manda tarefas básicas/repetitivas para o Codex CLI (assinatura do ChatGPT do autor) rodar em segundo plano com `codex exec`, depois confere o resultado. Use quando o autor disser "manda pro Codex", "pede pro Codex", "divide com o Codex", "segunda opinião do Codex", ou quando uma tarefa simples e repetitiva (renomear/converter arquivos, variações de texto, pesquisa rápida, revisar um script ou plano) puder rodar em paralelo enquanto o Claude faz a parte difícil. Para IMAGENS em lote use a skill codex-imagens.
---

# Codex ajudante

O Claude é o orquestrador: planeja, divide, confere e entrega. O Codex é o executor das tarefas básicas.
Os dois trabalham na mesma pasta: `C:\Users\Thiago\Downloads\TITI-AI` (regras em comum no `AGENTS.md`/`CLAUDE.md` de lá).

## O que mandar para o Codex
- Tarefas repetitivas: renomear, converter, organizar arquivos.
- Variações de texto (legendas, hooks, títulos) a partir de um texto do Claude.
- Pesquisa rápida ou explicação de um arquivo.
- Segunda opinião: revisar um script, plano de vídeo ou copy ANTES de gastar crédito (Grok, RunPod, ElevenLabs).

## O que NÃO mandar
- Roteiro final, montagem, render, decisões de dinheiro ou qualquer coisa que dependa das skills/memória do Claude.
- Nada com chave de API, senha ou `.env`.
- Nunca dois agentes no mesmo arquivo ao mesmo tempo: dê ao Codex uma pasta ou arquivos só dele.

## Como chamar (sempre pelo Bash, em segundo plano se for demorar)

Só ler/responder (não mexe em nada):
```bash
codex exec --skip-git-repo-check -s read-only -C "<pasta>" -o "<pasta-scratch>/resposta.txt" "<pedido em português, completo e sem ambiguidade>"
```

Pode criar/editar arquivos dentro da pasta indicada:
```bash
codex exec --skip-git-repo-check -s workspace-write -C "<pasta só da tarefa>" -o "<pasta-scratch>/resposta.txt" "<pedido>"
```

- `-o` grava só a resposta final num arquivo: leia esse arquivo, não o log inteiro.
- Use `timeout 600` na frente e `run_in_background: true` quando passar de ~2 min.
- Várias tarefas independentes: dispare até 3–5 em paralelo, cada uma com sua pasta e seu `-o`.
- O pedido vai SEMPRE completo: o Codex não vê esta conversa. Diga o objetivo, os arquivos, o formato da resposta e "responda em português".

## Depois que o Codex termina
1. Ler o arquivo do `-o` e conferir os arquivos que ele criou/mudou.
2. Se ficou ruim, refazer o pedido mais específico (no máximo 2 vezes) ou fazer o Claude mesmo.
3. Contar ao autor em uma linha o que foi feito pelo Codex.

Testado em 25/11/2026 com Codex CLI 0.170.0 (sem modo MCP nesta versão; `codex exec` é o caminho).
