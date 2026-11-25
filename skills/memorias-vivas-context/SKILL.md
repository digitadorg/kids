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
- Modelo de imagem escolhido: `gpt-image-2`, qualidade `medium` (não trocar sem autorização).
- O vídeo final é feito com as skills `estilo-aluno-101-vhc` (cliente) e `estilo-aluno-100-vhj` (anúncio).

## Versões (separadas; uma não substitui a outra)

| Versão | Preço | Pagamento | Rastreamento |
|---|---|---|---|
| A — funil de anúncios | **oficial: R$19,90 + foto bônus, PIX Mercado Pago** (confirmado pelo dono em 25/11/2026; antes R$67,90 Cakto) | PIX na página | Pixel + CAPI + webhook |
| B — atendimento WhatsApp | R$49,90, 1 pessoa | volta ao WhatsApp | não |
| C — atendimento WhatsApp | R$67,90, 1 pessoa | volta ao WhatsApp | não |

## Avisos (auditoria 25/11/2026)

- A versão no ar é a Cakto com **só valor e gateway trocados** pelo dono. O código local ainda é a versão Cakto R$67,90; o código da versão Mercado Pago não está no computador.
- Página de obrigado no ar mostra R$39,90 (diferente dos R$19,90) — pendente de decisão.
- Na troca para o Mercado Pago, o site parou de disparar **InitiateCheckout e AddPaymentInfo** (vinham do webhook da Cakto) e o Purchase ficou só no navegador → a régua 80×10×10 está incompleta. Ler com AddToCart no lugar de IC até corrigir (skill `metricas-80-10-10`).
- Mídias do Cloudinary (`res.cloudinary.com/pgy61ab9`) respondem 401.
- Versões B e C: arquivos não encontrados.
- Nada de deploy, preço, gateway ou Pixel sem o "pode" do dono.

Skills técnicas: `mestre-saas` coordena as demais; rastreamento = `fop-tracking` (prioridade); métricas = `metricas-80-10-10`.
