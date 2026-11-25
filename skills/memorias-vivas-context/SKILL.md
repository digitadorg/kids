---
name: memorias-vivas-context
description: Contexto específico do Memórias Vivas (memoriasvivas.app.br) — homenagens com IA (pessoa querida no céu com Jesus), prévia grátis e vídeo entregue pelo WhatsApp; versões comerciais (funil de anúncios e atendimento WhatsApp R$49,90/R$67,90), situação do site no ar, onde ficam código, backups e documentação. Use sempre que o assunto for Memórias Vivas, a página de homenagem, a prévia com Jesus, o funil Cakto/Mercado Pago do projeto ou as páginas de atendimento.
---

# Memórias Vivas — contexto

Só dados públicos aqui (o repo de skills é público). Detalhes completos, histórico e auditoria: pasta do projeto.

**Pasta:** `%USERPROFILE%\Downloads\TITI-AI\Lailla\MEMORIAS-VIVAS\` → leia `LEIA-ME-PRIMEIRO.md` e `00-CONTEXTO-MESTRE\STATUS-ATUAL.md` antes de agir.

## Negócio

- Cliente manda foto de alguém que faleceu → prévia grátis com IA (pessoa ao pé de uma escadaria celestial, Jesus no alto de braços abertos) → compra o vídeo completo, entregue depois pelo WhatsApp.
- Público: adultos 35+, cristãos, enlutados. Tom acolhedor, sem explorar a dor, sem promessa espiritual.
- Domínio: https://memoriasvivas.app.br · Pixel Meta `964640486589755` · WhatsApp `559881692723`.
- Modelo de imagem: `gpt-image-2.6-sunburst` (desde 25/11/2026, pedido do dono), qualidade `medium`. Cenário: Jesus de braços abertos na escadaria de mármore com portão dourado; estilo UGC realista. Não trocar sem autorização.
- O vídeo final é feito com as skills `estilo-aluno-101-vhc` (cliente) e `estilo-aluno-100-vhj` (anúncio).

## Versões (separadas; uma não substitui a outra)

| Versão | Preço | Pagamento | Rastreamento |
|---|---|---|---|
| A — funil de anúncios | **no ar desde 25/11/2026: R$67,90, checkout Cakto** (antes: R$19,90 Mercado Pago) | checkout Cakto | FOP (Pixel + CAPI) + webhook Cakto |
| B — atendimento WhatsApp | R$49,90, 1 pessoa | volta ao WhatsApp | não |
| C — atendimento WhatsApp | R$67,90, 1 pessoa | volta ao WhatsApp | não |

## Situação (25/11/2026)

- No ar: versão Cakto R$67,90 com FOP puro, painel `/painel` (senha só no computador do dono), carrossel, obrigado sem WhatsApp.
- Publicar: rodar `09-PUBLICACAO/preparar_publicacao.py` e depois o deploy da pasta `09-PUBLICACAO/memoriasvivas-app-br` (já vinculada ao projeto Netlify `bobiegoodscristao`). Rascunho antes, produção só com o "pode publicar".
- Pendente: ZapData (número desconectado, fluxo inativo criado) e chave da API da Cakto.
- Nada de deploy, preço, gateway, Pixel ou modelo sem o "pode" do dono.

Skills técnicas: `mestre-saas` coordena as demais; rastreamento = `fop-tracking` (prioridade); métricas = `metricas-80-10-10`.
