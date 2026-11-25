---
name: netlify-serverless
description: Padrões validados de Netlify Functions modernas, Background Functions, Netlify Blobs e variáveis de ambiente para micro-SaaS, incluindo a correção do erro "BlobsInternalError Failed to decode token". Use ao criar ou consertar uma function, rota /api, background function, store do Blobs, ou ao ler logs de função na Netlify.
---

# Netlify serverless

## Function moderna

```js
export default async (request) => {
  if (request.method !== "POST") return json(405, { ok:false });
  const store = getStore({ name: "meu-store", consistency: "strong" }); // DENTRO do handler
  ...
  return new Response(JSON.stringify(body), { status: 200, headers: { "content-type": "application/json" } });
};
```
- Recebeu `Request` → devolva `Response`. Nunca o formato legado `{statusCode, body}` (isso quebrou webhooks: gateway marcava "zero entregues").
- `getStore()` global causa `BlobsInternalError … Failed to decode token`. Sempre dentro da execução.

## Background Function

- Nome terminando em `-background` **ou** `[functions."nome"] background = true` no `netlify.toml`, e/ou `export const config = { background: true, path: "/api/..." }`.
- Responde 202 na hora; roda até 15 min. O status que ela retorna **não volta** para quem chamou. Erros só aparecem nos logs.
- Receba só identificadores pequenos (jobId). Dados grandes vão antes para o Blobs.
- Chamada interna entre funções: header com segredo (`x-...-internal-secret`) + `timingSafeEqual`.

## Blobs

- `consistency: "strong"` quando outra função vai ler logo em seguida.
- Use stores separados por finalidade (entradas, jobs, leads, atribuição, ledger de webhook).
- Apague entradas temporárias depois do sucesso.

## Variáveis

- Ficam por site. Site novo não herda nada. Mudou variável → novo deploy.
- Nunca logar valor de segredo. Logar só nomes/razões (`missing_X`, `invalid_secret`).

## Diagnóstico

1. `GET` na rota: 405 = função existe e só aceita POST; 404 = não publicada; 202 = background.
2. Painel Netlify → Logs → Functions → filtrar pela função.
3. Problema de token/variável/Blobs é infraestrutura: rollback de código não resolve.
