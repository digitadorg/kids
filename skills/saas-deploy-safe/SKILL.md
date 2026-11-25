---
name: saas-deploy-safe
description: Deploy e rollback seguros na Netlify para micro-SaaS — conferir conta, site, Site ID, domínio, pasta, vínculo .netlify e variáveis antes de publicar, baixar o deploy atual como backup, publicar com a CLI e voltar versão pelo painel. Use sempre antes de "publica", "sobe", "faz o deploy", "volta a versão anterior" ou ao vincular uma pasta a um site novo.
---

# Deploy seguro (Netlify)

**Só publica com o "pode publicar" explícito do dono, para aquele deploy.**

## Antes

1. Pasta é uma cópia de trabalho (não o backup). Sem `.netlify/` herdada de outro projeto.
2. `npx --yes netlify-cli@latest status` → anotar conta, nome do site, **Site ID**, URL. Conferir com o dono que é o site certo para essa versão.
3. Vinculado errado → `netlify unlink` + `netlify link` (escolher pelo nome).
4. Variáveis do site conferidas no painel (o código lista quais usa em `process.env`). Teste? `META_TEST_EVENT_CODE`; produção? sem ela.
5. Preço, checkout, WhatsApp, mídias externas conferidos.
6. **Backup do que está no ar:** painel → Deploys → deploy publicado → Download. Guardar no backup do projeto.

## Publicar

`npx --yes netlify-cli@latest deploy --prod --skip-functions-cache` (conferir flags na versão da CLI). Mais seguro: `deploy` sem `--prod` → testar a URL de prévia → depois `--prod`.

## Depois

Ctrl+F5 · funções listadas no painel · checklist de homologação (`saas-qa`) · registrar data, Site ID, deploy ID e mudanças no histórico do projeto.

## Rollback

- Mais rápido: painel → Deploys → deploy bom anterior → **Publish deploy** (volta HTML e funções).
- Rollback **não** volta: variáveis, tokens, dados do Blobs, configurações de gateway/Meta/Google, vínculo da pasta.
- Voltar uma versão antiga pode mudar preço/gateway/oferta: avisar o dono antes.
