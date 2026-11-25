---
name: cakto-webhook
description: Webhook de gateway de pagamento (Cakto e similares como Mercado Pago/Kiwify) em Netlify — receptor que responde em menos de 5 s e repassa para Background Function, autenticação por segredo com timingSafeEqual, mapeamento de eventos para a Meta, idempotência por pedido e diagnóstico pelos logs. Use ao criar, consertar ou auditar webhook de pagamento, quando o gateway mostra "falha na entrega", ou quando Purchase duplica ou some.
---

# Webhook de pagamento (padrão Cakto)

## Arquitetura validada

```
Gateway POST → receptor (/api/<gateway>-funil)
  só POST · segredo obrigatório (header ou body) · timingSafeEqual · corpo ≤ 256 KB
  fetch interno → /api/<gateway>-funil-processar  (header x-<gateway>-internal-secret, timeout 2500 ms)
  enfileirou → 200 JSON (new Response)   falhou → 502 (gateway reenvia)
Background:
  confere segredo interno → mapeia evento → ledger Blobs "<evento>:<pedido>" (sent:true? para)
  recupera atribuição (funnel:<id>, phone:<sha256>) → monta user_data → Graph API (timeout 15 s)
  só depois do events_received grava o ledger e loga "event sent"
```

- Gateway costuma exigir resposta em ~5 s: **nunca** chamar a Meta ou fazer muito Blobs antes de responder.
- 200 do gateway = recebido; não = enviado à Meta. Conferir log da background.

## Mapa Cakto → Meta

`initiate_checkout`→InitiateCheckout · `pix_gerado`/`boleto_gerado`/`picpay_gerado`/`openfinance_nubank_gerado`→AddPaymentInfo · `purchase_approved`→Purchase (`offer_type=orderbump`→OrderBumpPurchase) · `purchase_refused`→PaymentFailed · `checkout_abandonment`→CheckoutAbandoned · `refund`→Refund · `chargeback`→Chargeback.

`event_id` = `<gateway>:<evento>:<pedido>`.

## Pontos de auditoria conhecidos

- Corrida entre dois reenvios simultâneos (checagem e gravação do ledger não são atômicas) — mitigado pelo mesmo `event_id`.
- Background que **retorna** erro não é refeita; erro só aparece no log. Avaliar `throw` ou fila de reprocessamento se perder eventos.
- Valor: usar o valor real da transação; definir política para order bump com payload real.
- Validar o contrato atual do gateway (nomes de campos) com payload real anonimizado antes de mudar a leitura.
- Segredo exposto em conversa → rotacionar no gateway e na Netlify ao mesmo tempo.
