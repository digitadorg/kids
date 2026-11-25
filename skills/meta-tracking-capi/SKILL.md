---
name: meta-tracking-capi
description: Complemento da skill fop-tracking para micro-SaaS com prévia grátis e pagamento por gateway (Cakto, Mercado Pago, Kiwify) — hierarquia de eventos do funil com quiz → foto → prévia → checkout → PIX, Purchase só pelo servidor via webhook com event_id deduplicado, atribuição por UTMs/fbp/fbc/IDs internos e leitura de vendas sem atribuição. Use junto com fop-tracking ao criar ou auditar Pixel/CAPI de um SaaS, quando compra não aparece no Gerenciador de Anúncios, quando Purchase duplica ou some, ou ao trocar de gateway.
---

# Meta Pixel + CAPI em micro-SaaS (complemento do FOP)

**Carregue primeiro a skill `fop-tracking`** — ela é a base: hierarquia, Advanced Matching, parâmetros obrigatórios e proibidos, deduplicação, EMQ, persistência e checklist. Aqui fica só o que o FOP não cobre: funil com prévia gerada por IA + gateway externo com webhook. Métricas: skill `metricas-80-10-10`.

## Template F — "Quiz + prévia grátis + gateway" (adaptação do template A do FOP)

| # | Evento | Gatilho honesto | Origem | Parâmetros-chave |
|---|---|---|---|---|
| 1 | PageView | carregou | navegador + CAPI | AM no `init` (o que já houver) |
| 2 | ViewContent | 25% de rolagem ou 10 s visível (FOP) | navegador + CAPI | content_name, content_category, value, currency |
| 3 | Lead | **backend aceitou a foto** (não um clique) | navegador + CAPI | ph (do quiz), external_id |
| 4 | CustomizeProduct | prévia gerada com sucesso | navegador + CAPI | value, currency |
| 5 | AddToCart | clique no CTA pós-prévia | navegador + CAPI | value, currency |
| 6 | InitiateCheckout | checkout aberto (redirect **ou** modal de PIX aberto) | navegador + CAPI, ou webhook do gateway | value, currency |
| 7 | AddPaymentInfo | PIX/boleto **gerado** | servidor (webhook ou API do gateway) | payment_method |
| 8 | Purchase | pagamento **aprovado** | **servidor** (webhook) | value real, currency, order_id |
| — | Contact | clique no WhatsApp | navegador + CAPI | — |

CustomizeProduct é evento padrão da Meta — usar em vez de evento personalizado (regra 3 do FOP). AddToWishlist (rolagem 50%/30 s) é opcional; só incluir se for usado em análise.

Eventos de diagnóstico do gateway (PaymentFailed, CheckoutAbandoned, Refund, Chargeback, OrderBumpPurchase) são personalizados de propósito: **nunca** usar como objetivo de campanha.

## Purchase: uma fonte de verdade

- Purchase nasce do **webhook do gateway** (aprovado), com `event_id = <gateway>:Purchase:<id do pagamento>` e o **valor real** da transação.
- Se o navegador também mandar (ex.: tela de "pagamento confirmado"), usar **o mesmo `event_name` e `event_id`** do servidor — aí deduplica e o servidor cobre quem fechou a tela antes.
- Nunca Purchase em PIX/boleto gerado. Nunca na página de obrigado. Desligar o Pixel nativo do gateway se o webhook já envia.
- **Trocou de gateway?** Refazer o mapa: InitiateCheckout e AddPaymentInfo costumam sumir junto com o webhook antigo, e a régua 80×10×10 quebra sem ninguém perceber.

## Advanced Matching no navegador (regra 10 do FOP)

Funil com quiz já tem telefone/nome antes da compra: depois que o cliente preencher, reinicializar o AM (`fbq('init', PIXEL, {ph, fn, external_id})` com hash) e persistir em cookie + localStorage para os próximos eventos. Sem isso o EMQ dos eventos do meio fica baixo.

## Atribuição

- Guardar first touch + last touch (~30 dias) e repassar ao checkout: UTMs + IDs internos (`src`/`sck`/`funnel_id`).
- No servidor, recuperar por ID do funil ou hash do telefone; `external_id` igual no navegador e no servidor.
- UTM padrão do autor: `utm_source=fb&utm_medium=paid&utm_campaign={{campaign.id}}&utm_content={{ad.id}}&utm_term={{adset.id}}`.
- `fbp` sozinho não prova anúncio; `fbclid` não prova pago; sem UTM = origem desconhecida.
- Venda aprovada ≠ Purchase enviado ≠ recebido ≠ atribuído. Nunca forçar atribuição.

## Parâmetros custom

O FOP chama de lixo parâmetro sem propósito. Em SaaS, `funnel_id`, `utm_*` e `source_button` têm propósito (atribuição e diagnóstico) — manter. Não mandar foto, nome do falecido, texto da homenagem ou qualquer dado sensível (LGPD).

## Diagnóstico de compra sumida

Gateway aprovou → webhook entregue (200) → log da função "event sent" com `events_received` → Gerenciador de Eventos (Purchase, servidor, valor, BRL, EMQ) → Gerenciador de Anúncios (janela, campanha).
