# Skills salvas

Cópia de segurança das skills do Claude, para não se perderem se o computador der problema.

| Skill | O que faz | Situação |
|---|---|---|
| [`serie-peaky-shelby`](skills/serie-peaky-shelby/SKILL.md) | Produz um episódio da série @shelby.explica, do roteiro ao vídeo final, com capas e legenda | ✅ Salva |
| [`codex-imagens`](skills/codex-imagens/SKILL.md) | O Claude orquestra e o Codex gera imagens em lote (5 de cada vez) pela assinatura do ChatGPT | ✅ Salva, reconstruída |

## De onde veio

A skill `serie-peaky-shelby` foi recuperada da conversa "Grok API integração vídeo Apocalipse", de 17 e 18 de novembro de 2026. É o texto exato que foi gravado em `C:\LAILLA_AUTOMACAO\skills\serie-peaky-shelby\SKILL.md`.

**Falta:** a pasta `modelos\` da skill, com `plano.py`, `narrar.py`, `animar_ep.py`, `montar_ep.py` e os arquivos `pedido-*.json`. Esses arquivos foram copiados do `episodio-2` direto no computador, e o conteúdo deles não apareceu na conversa.

## Como instalar de novo num computador

1. Baixe a pasta `skills/serie-peaky-shelby` deste repositório.
2. Coloque essa pasta dentro de `C:\Users\<seu usuário>\.claude\skills\`.
3. Abra o Claude Code. A skill aparece com o nome `serie-peaky-shelby`.

A skill `codex-imagens` foi reconstruída em 18/11/2026. Só o começo do texto original e as primeiras 60 linhas do programa `gerar.py` apareceram nas conversas. O resto foi reescrito seguindo como ela era usada: os comandos, os `pedido.json` e os logs. O `gerar.py` agora fica dentro da pasta da skill, e foi testado com um Codex simulado, mas ainda não com o Codex de verdade.
