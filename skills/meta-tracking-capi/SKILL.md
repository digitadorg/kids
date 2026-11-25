---
name: meta-tracking-capi
description: Meta Pixel + Conversions API em micro-SaaS — mapa de eventos do funil (PageView, ViewContent, Lead, CustomizeProduct, AddToCart, InitiateCheckout, AddPaymentInfo, Purchase), deduplicação navegador/servidor por event_id, hash SHA-256, fbp/fbc, UTMs e leitura de atribuição. Use ao criar ou auditar eventos, quando compra não aparece no Gerenciador de Anúncios, quando há Purchase duplicado, ou ao montar UTMs de anúncio.
---

# Meta Pixel + CAPI

## Deduplicação

- Mesmo evento pelo navegador e pelo servidor: **mesmo `event_name` e mesmo `event_id`** nos dois (`fbq('track', nome, dados, {eventID})` + CAPI com `event_id`).
- Purchase: **uma fonte de verdade** (webhook do gateway, servidor). Se o navegador também mandar, usar o mesmo ID que o servidor. Desligar Pixel nativo do gateway quando o webhook já envia.
- Nunca Purchase em PIX/boleto gerado (isso é AddPaymentInfo). Nunca Purchase na página de obrigado.

## Funil padrão

| Evento | Gatilho honesto |
|---|---|
| PageView | carregou |
| ViewContent | ~4 s visível ou primeira interação |
| Lead | backend **aceitou** a foto/dado (não um clique qualquer) |
| CustomizeProduct | personalização (prévia) concluída |
| AddToCart | clique no CTA de compra |
| InitiateCheckout | gateway avisou início de checkout |
| AddPaymentInfo | PIX/boleto gerado |
| Purchase | pagamento **aprovado**, valor real, BRL |

Eventos de diagnóstico (PaymentFailed, CheckoutAbandoned, Refund, Chargeback, OrderBumpPurchase) não são objetivo de otimização.

## Dados do usuário

- Hash SHA-256 depois de normalizar: `em` (minúsculo), `ph` (só dígitos com 55), `fn`, `ln`, `ct`, `st`, `zp`, `country`, `external_id`.
- **Sem hash:** `fbp`, `fbc`, `client_ip_address`, `client_user_agent`.
- `fbc` = cookie `_fbc` ou `fb.1.<timestamp>.<fbclid>`.
- Nunca mandar foto, conteúdo sensível ou dado desnecessário. LGPD.
- Token só em variável; `META_TEST_EVENT_CODE` só durante teste.

## Atribuição

- Guardar first touch + last touch no navegador (~30 dias) e repassar ao checkout (UTMs + IDs internos `src`/`sck`).
- No servidor, recuperar por ID do funil ou hash do telefone.
- UTM padrão de anúncio: `utm_source=fb&utm_medium=paid&utm_campaign={{campaign.id}}&utm_content={{ad.id}}&utm_term={{adset.id}}`.
- `fbp` sozinho não prova anúncio; `fbclid` não prova pago; sem UTM = desconhecido.
- Venda aprovada ≠ Purchase enviado ≠ recebido ≠ atribuído. Nunca forçar atribuição.

## Diagnóstico

Gateway aprovou → webhook 200 → log de envio com `events_received` → Gerenciador de Eventos (servidor, valor, moeda) → Gerenciador de Anúncios (atribuição, janela).
