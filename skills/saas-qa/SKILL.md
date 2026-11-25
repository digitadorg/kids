---
name: saas-qa
description: Testes e homologação de micro-SaaS com IA e pagamentos — teste funcional da prévia (formatos de foto, Blobs, background, status), rastreamento (Pixel/CAPI deduplicado com test_event_code), webhook (segredo, rapidez, PIX não vira Purchase, reenvio não duplica), regressão e checagem de segurança. Use antes de liberar uma versão, depois de mexer em infraestrutura, ou quando o autor perguntar "está funcionando?".
---

# QA e homologação

Regra: **marcar só o que foi testado de verdade**, com data. Teste não feito = "falta testar", nunca "ok".

## Leitura (sem efeito colateral — pode sempre)

- `GET` em cada rota: 405 (existe, só POST), 404 (não publicada), 202 (background).
- Baixar HTML publicado e comparar com o código local (hash/diff): o site no ar pode ser outra versão.
- Conferir mídias externas (HTTP 200).
- Procurar segredos no código (`sk-`, `EAA`, `nfp_`, senhas).

## Funcional (com autorização; pode gastar crédito de IA)

Upload JPG, PNG, WEBP, HEIC, AVIF → status até `complete` → prévia com marca-d'água → barra coerente → CTA com UTMs e IDs.

## Rastreamento (com `META_TEST_EVENT_CODE`)

Cada evento do navegador aparece **uma vez** (navegador + servidor deduplicados). Remover a variável e republicar ao final.

## Webhook (com autorização; usar o "enviar teste" do gateway)

Segredo errado → 401 · resposta < 5 s · PIX gerado → AddPaymentInfo, nunca Purchase · aprovado → um Purchase com valor real e BRL · reenvio → `already_processed` · logs sem erro.

## Segurança

Segredos só em variável · nada sensível nos logs · rotas internas autenticadas · dados de cliente fora de docs/exemplos · arquivos públicos por link só com consentimento (LGPD).

## Relatório

Testes feitos · resultado · evidência (log, print, hash) · testes faltando · riscos.
