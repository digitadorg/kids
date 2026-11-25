# Skills salvas

Cópia de segurança das skills do Claude, para não se perderem se o computador der problema.

| Skill | O que faz | Situação |
|---|---|---|
| [`serie-peaky-shelby`](skills/serie-peaky-shelby/SKILL.md) | Produz um episódio da série @shelby.explica, do roteiro ao vídeo final, com capas e legenda | ✅ Salva |
| [`codex-imagens`](skills/codex-imagens/SKILL.md) | O Claude orquestra e o Codex gera imagens em lote (5 de cada vez) pela assinatura do ChatGPT | ✅ Salva, reconstruída |
| [`codex-ajudante`](skills/codex-ajudante/SKILL.md) | O Claude orquestra e manda tarefas básicas para o Codex (`codex exec`) em segundo plano, depois confere | ✅ Salva, testada |
| [`saude-do-computador`](skills/saude-do-computador/SKILL.md) | Check-up e manutenção do notebook: varredura, saúde do SSD e da bateria, atualizações, limpeza, DISM/sfc e Defender | ✅ Salva, testada em 18 e 19/11/2026 |
| [`estilo-aluno-100-vhj`](skills/estilo-aluno-100-vhj/SKILL.md) | **VHJ** · Vídeos Homenagem com Jesus: a foto vira anúncio 9:16 (jardim, escada do céu, aceno, abraço), Grok + narração | ✅ Salva, 22/11/2026 |
| [`estilo-aluno-101-vhc`](skills/estilo-aluno-101-vhc/SKILL.md) | **VHC** · Vídeo Homenagem para Cliente: entrega para a família, com nome, datas e mensagem, sem anúncio | ✅ Salva, testada sem custo em 22/11/2026 |
| [`mestre-saas`](skills/mestre-saas/SKILL.md) | Coordena micro-SaaS com IA + Netlify + pagamentos + Meta: auditar antes de mexer, qual skill usar, regras de ouro | ✅ Criada 25/11/2026 |
| [`netlify-serverless`](skills/netlify-serverless/SKILL.md) | Functions modernas, Background Functions, Blobs (getStore dentro do handler), variáveis e diagnóstico | ✅ Criada 25/11/2026 |
| [`ai-image-pipeline`](skills/ai-image-pipeline/SKILL.md) | Upload → Sharp → Blobs → OpenAI images/edits → marca-d'água → status/progresso | ✅ Criada 25/11/2026 |
| [`meta-tracking-capi`](skills/meta-tracking-capi/SKILL.md) | Complemento da `fop-tracking` (Fábrica) para SaaS com prévia + gateway: Template F de eventos, Purchase pelo webhook, atribuição | ✅ Criada 25/11/2026, alinhada ao FOP |
| [`metricas-80-10-10`](skills/metricas-80-10-10/SKILL.md) | Régua 80 × 10 × 10 + métricas FOP (Hook, Hold, Qualify, Close) + conta do CPA/ROAS de empate | ✅ Criada 25/11/2026 |
| [`cakto-webhook`](skills/cakto-webhook/SKILL.md) | Webhook de pagamento com resposta rápida + background, segredo, idempotência | ✅ Criada 25/11/2026 |
| [`funnel-cro`](skills/funnel-cro/SKILL.md) | Página, oferta, pós-prévia, provas sociais e versão WhatsApp (métricas na `metricas-80-10-10`) | ✅ Criada 25/11/2026 |
| [`saas-deploy-safe`](skills/saas-deploy-safe/SKILL.md) | Deploy e rollback na Netlify conferindo site, Site ID e variáveis | ✅ Criada 25/11/2026 |
| [`saas-qa`](skills/saas-qa/SKILL.md) | Testes, homologação, regressão e segurança | ✅ Criada 25/11/2026 |
| [`memorias-vivas-context`](skills/memorias-vivas-context/SKILL.md) | Contexto público do Memórias Vivas e onde ficam código e documentação | ✅ Criada 25/11/2026 |

## De onde veio

A skill `serie-peaky-shelby` foi recuperada da conversa "Grok API integração vídeo Apocalipse", de 17 e 18 de novembro de 2026. É o texto exato que foi gravado em `C:\LAILLA_AUTOMACAO\skills\serie-peaky-shelby\SKILL.md`.

**Falta:** a pasta `modelos\` da skill, com `plano.py`, `narrar.py`, `animar_ep.py`, `montar_ep.py` e os arquivos `pedido-*.json`. Esses arquivos foram copiados do `episodio-2` direto no computador, e o conteúdo deles não apareceu na conversa.

## Como instalar de novo num computador

1. Baixe a pasta `skills/serie-peaky-shelby` deste repositório.
2. Coloque essa pasta dentro de `C:\Users\<seu usuário>\.claude\skills\`.
3. Abra o Claude Code. A skill aparece com o nome `serie-peaky-shelby`.

A skill `codex-imagens` foi reconstruída em 18/11/2026. Só o começo do texto original e as primeiras 60 linhas do programa `gerar.py` apareceram nas conversas. O resto foi reescrito seguindo como ela era usada: os comandos, os `pedido.json` e os logs. O `gerar.py` agora fica dentro da pasta da skill. Foi testado com um Codex simulado e, em 18/11/2026, com o Codex de verdade: gerou 1 imagem 9:16 em 42 segundos pela conta do ChatGPT.
