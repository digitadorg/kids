---
name: metricas-80-10-10
description: Complemento da skill fop-tracking (que é a PRIORIDADE para Pixel, CAPI e métricas FOP) — acrescenta a régua do autor 80 × 10 × 10 (Connect Rate 80%, conversão da página 10%, conversão do checkout 10%, conversão global 1%) integrada às métricas FOP (Hook Rate, Hold Rate, Qualify Rate, Close Rate) e às métricas de micro-SaaS com prévia grátis (custo de prévia por venda, CPA máximo, custo máximo por visita). Use ao analisar campanha, achar o gargalo do funil, montar colunas personalizadas no Gerenciador de Anúncios, calcular se a oferta paga o tráfego, ou quando o autor falar "80 10 10", "1% de conversão", "connect rate", "onde está travando".
---

# Métricas — régua 80 × 10 × 10 (complemento do FOP)

**A skill `fop-tracking` é a prioridade**: hierarquia de eventos, Pixel + CAPI, Advanced Matching, EMQ e as métricas FOP (Hook, Hold, Connect, Qualify, Close). Esta skill só acrescenta o que o FOP não tem: a régua 80 × 10 × 10 com o **1% de conversão global**, os degraus de um funil com prévia grátis, a conta do dinheiro e a leitura de atribuição. Em conflito, vale o FOP.

## 1. A régua completa

| Etapa | Métrica | Fórmula (colunas do Meta) | Meta | Se estiver abaixo, mexer em… |
|---|---|---|---|---|
| Criativo | **Hook Rate** (FOP) | Visualizações de 3 s ÷ Impressões | > 30% | primeiros 3 s do vídeo |
| Criativo | **Hold Rate** (FOP) | ThruPlays ÷ Impressões | > 15% | meio do vídeo |
| Criativo | CTR (link) | Cliques no link ÷ Impressões | referência da conta | promessa/CTA do anúncio |
| Página | **Connect Rate** (80) | Visualizações da página de destino ÷ Cliques no link | **≥ 80%** | velocidade, peso, redirecionamento, pixel |
| Página | **Conversão da página** (10) | InitiateCheckout ÷ Visualizações da página de destino | **≥ 10%** | página, oferta, prova |
| Checkout | **Conversão do checkout** (10) | Purchase ÷ InitiateCheckout | **≥ 10%** | checkout, meio de pagamento, preço |
| Global | **Conversão global** | Purchase ÷ Visualizações da página de destino | **≥ 1%** | (é 10% × 10%) |

Conta de bolso: 100 cliques → 80 visitas → 8 checkouts → **0,8 compra** (0,8% clique→compra; 1% visita→compra). Número fracionado = expectativa, não venda.

## 2. Métricas FOP de lead (quando o funil tem Lead forte)

| Métrica | Fórmula | Meta FOP |
|---|---|---|
| **Qualify Rate** | Lead ÷ Visualizações da página | > 10% |
| **Close Rate** | Purchase ÷ Lead | > 3% |

**Não misture as duas réguas.** 80×10×10 usa **InitiateCheckout** no meio; FOP usa **Lead**. Elas se encontram na conversão global:

```
Global = (Lead ÷ LPV) × (Purchase ÷ Lead)  =  (IC ÷ LPV) × (Purchase ÷ IC)
```
Com as metas mínimas do FOP (10% × 3%) a global dá **0,3%** — abaixo do 1% da régua do autor. Para bater 1% com Qualify de 10%, o Close precisa ser **10%**; com Qualify de 25%, Close de 4%. **A meta que manda é o 1% global**; Qualify/Close dizem em qual metade está a perda.

## 3. Diagnóstico entre degraus (funil com prévia grátis)

| Métrica | Fórmula | Leitura |
|---|---|---|
| Taxa de lead | Lead ÷ LPV | quantos mandam a foto (= Qualify Rate) |
| Conclusão da prévia | CustomizeProduct ÷ Lead | **< ~90% = problema técnico** (IA, Blobs, timeout) |
| CTA pós-prévia | AddToCart ÷ CustomizeProduct | a prévia + oferta convencem? |
| Transferência ao checkout | InitiateCheckout ÷ AddToCart | ~100%; abaixo = botão/checkout lento ou quebrado |
| Avanço no pagamento | AddPaymentInfo ÷ InitiateCheckout | gerou PIX/boleto? |
| Pagamento do PIX | Purchase ÷ AddPaymentInfo | PIX gerado e não pago = recuperar pelo WhatsApp |

## 4. Dinheiro (o que decide se escala)

```
CPA máximo (empate)      = ticket − taxa do gateway − custo de produção da entrega
Custo de prévias/venda   = custo por prévia ÷ (Purchase ÷ CustomizeProduct)
CPA máximo real          = CPA máximo − custo de prévias/venda
Custo máx. por visita    = CPA máximo real × conversão global
CPC máximo               = custo máx. por visita × Connect Rate
ROAS de empate           = ticket ÷ CPA máximo real
```
ROAS do Meta não é lucro: não desconta taxa, IA, produção, imposto, reembolso.

## 5. Regras de leitura

1. **Mesma fonte, mesmo período, mesma janela de atribuição.** Não misturar Gerenciador de Eventos (contagem bruta) com Gerenciador de Anúncios (atribuído).
2. Eventos são ocorrências, não pessoas. Taxa > 100% → investigar duplicação/perda antes de chamar de bug.
3. **Antes de ler a régua, confira se cada evento existe** no funil atual (trocar de gateway costuma apagar InitiateCheckout/AddPaymentInfo). Sem IC, use provisoriamente AddToCart no lugar e avise.
4. Volume mínimo antes de concluir: pelo menos ~1.000 impressões por criativo para Hook/Hold, ~100 visitas para Connect, ~20 checkouts para conversão do checkout.
5. Ataque **um gargalo por vez**, o mais alto da régua primeiro (criativo → página → checkout).
6. Otimização da campanha: Purchase. Os demais eventos são diagnóstico e sinal; não há garantia de que mais eventos melhoram a entrega.

## 6. Atribuição (o FOP não cobre)

- UTM padrão do autor em todo anúncio, inclusive duplicados: `utm_source=fb&utm_medium=paid&utm_campaign={{campaign.id}}&utm_content={{ad.id}}&utm_term={{adset.id}}`.
- Orgânico: `utm_medium=organic`; atendimento: `utm_source=whatsapp&utm_medium=atendimento`.
- `fbp` sozinho não prova anúncio; `fbclid` não prova pago; sem UTM = origem desconhecida.
- Venda aprovada no gateway ≠ Purchase enviado ≠ recebido pela Meta ≠ atribuído a anúncio. O gateway é a verdade do dinheiro; a Meta, da atribuição (dentro das janelas dela). Nunca forçar atribuição.
- Purchase vem do webhook do gateway (skill `cakto-webhook`) com `event_id` igual ao do navegador, se o navegador também mandar. Trocou de gateway? Confira se InitiateCheckout e AddPaymentInfo continuam existindo.

## 7. Colunas personalizadas sugeridas (Gerenciador de Anúncios)

`HOOK %` · `HOLD %` · `CONNECT %` · `% PÁGINA (IC/LPV)` · `% CHECKOUT (PUR/IC)` · `% GLOBAL (PUR/LPV)` · `% LEAD` · `% PRÉVIA OK (CP/LEAD)` · `% CTA PÓS-PRÉVIA (ATC/CP)` · `CPA` · `ROAS`.
CustomizeProduct aparece como "Personalizações de produto"; conferir o nome exato na conta.
