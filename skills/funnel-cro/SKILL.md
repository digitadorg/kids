---
name: funnel-cro
description: Experiência e conversão de funil de micro-SaaS com prévia grátis — quiz de uma pergunta por tela, upload simples para público 35+, pós-prévia com oferta, provas sociais reais, CTA claro, WhatsApp de apoio, e leitura das métricas 80×10×10 do Meta Ads. Use ao mudar página, oferta, botões, provas sociais, pós-prévia, versão de atendimento por WhatsApp, ou ao analisar onde o funil está perdendo gente.
---

# Funil e conversão

## Página

- Mobile primeiro, botões grandes, uma pergunta por tela, emojis com moderação, pouca poluição.
- Tom acolhedor e respeitoso; não explorar sofrimento; nada de promessa espiritual ou de resultado.
- Prévia grátis antes de pagar (reduz desconfiança). Progresso honesto.
- Pós-prévia: prévia → oferta → provas sociais → CTA → (WhatsApp para dúvidas).
- Provas sociais **reais** apenas. Conferir se as mídias carregam (CDN externo pode cair; preferir arquivos locais ou plataforma estável).
- Versão de atendimento WhatsApp: página curta, sem quiz longo, sem checkout e sem rastreamento de anúncio não pedidos, botão "CONTINUAR NO WHATSAPP — R$X".
- Cada versão comercial em pasta e site Netlify próprios. Não mudar preço sem autorização.

## Métricas (régua inicial 80 × 10 × 10)

Connect Rate = LPV ÷ cliques (80%) · Conversão da página = InitiateCheckout ÷ LPV (10%) · Conversão do checkout = Purchase ÷ InitiateCheckout (10%) · Global = Purchase ÷ LPV (1%).
Diagnóstico: Lead ÷ LPV · CustomizeProduct ÷ Lead (queda = problema técnico) · AddToCart ÷ CustomizeProduct (oferta/qualidade da prévia) · InitiateCheckout ÷ AddToCart (~100%) · AddPaymentInfo ÷ InitiateCheckout · CPA · ROAS (não é lucro).

Mesma fonte, período e janela. Eventos ≠ pessoas. Se o checkout mudou de gateway, confira se InitiateCheckout/AddPaymentInfo ainda existem antes de ler as taxas.

## Teste A/B

Cópia separada, uma mudança por vez, mesma verba, tempo suficiente; registrar resultado no histórico do projeto.
