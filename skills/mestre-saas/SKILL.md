---
name: mestre-saas
description: Coordena a construção, diagnóstico, manutenção e evolução de micro-SaaS com IA (geração de imagem), Netlify Functions/Blobs, pagamentos por webhook (Cakto, Mercado Pago, Kiwify), Meta Pixel/CAPI e atribuição. Use quando o autor pedir para mexer, auditar, corrigir, publicar ou criar uma nova versão de um micro-SaaS — por exemplo o Memórias Vivas — ou disser "mestre saas", "audita o funil", "o webhook parou", "a prévia não gera", "faz uma versão nova do site". Diz qual skill modular carregar para cada parte.
---

# Mestre SaaS — coordenação

Conhecimento **genérico**. Dados de um projeto específico (marca, preço, Pixel, checkout) ficam numa skill de contexto própria (ex.: `memorias-vivas-context`). Nunca reaproveite dados comerciais de um projeto em outro sem autorização.

## Ordem de trabalho (sempre)

1. **Ler o contexto do projeto** (skill de contexto + `LEIA-ME-PRIMEIRO.md` da pasta do projeto).
2. **Auditar antes de alterar:** achar ZIPs/pastas, extrair em pasta isolada, ler o código, comparar com o site publicado (GET de leitura) — o site no ar pode ser outra versão.
3. **Separar fato de hipótese.** "Funcionou no passado" ≠ "está no ar hoje".
4. **Copiar antes de mexer.** Backup original somente leitura; experimento em pasta nova.
5. **Mudar só o que foi pedido.** Registrar cada arquivo alterado.
6. **Testar de verdade** (ver `saas-qa`). Nunca simular teste.
7. **Publicar só com o "pode" do dono**, seguindo `saas-deploy-safe`.
8. **Responder no formato:** pedido · achado · versão usada · mudanças · preservado · testes feitos · testes faltando · riscos · próximo passo · onde estão os arquivos.

## Qual skill carregar

| Assunto | Skill |
|---|---|
| Functions, Background Functions, Blobs, variáveis, logs | `netlify-serverless` |
| Upload, Sharp, prompt, OpenAI imagem, marca-d'água, progresso | `ai-image-pipeline` |
| Pixel, CAPI, eventos, EMQ, deduplicação | **`fop-tracking`** (prioridade) |
| Métricas, gargalo, 80×10×10, 1% global, CPA/ROAS de empate, atribuição | `metricas-80-10-10` (complemento do FOP) |
| Webhook de gateway (Cakto e similares), idempotência | `cakto-webhook` |
| Página, oferta, CTA, provas sociais, métricas de conversão | `funnel-cro` |
| Deploy, vínculo Netlify, rollback | `saas-deploy-safe` |
| Testes, regressão, homologação | `saas-qa` |

## Regras de ouro

- `getStore()` **dentro** do handler, nunca global.
- Upload separado da geração; a Background Function recebe só IDs.
- Purchase só com pagamento aprovado e `event_id` deduplicável; nunca em PIX gerado; nunca na página de obrigado.
- Segredos só em variável de ambiente. Repo `digitadorg/kids` é público.
- Não copiar `.netlify/` entre projetos. `netlify status` antes de todo deploy.
- Não trocar modelo de IA, qualidade, preço, gateway ou Pixel sem autorização.
