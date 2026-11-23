---
name: estilo-aluno-100-vhj
description: Modelo de criativo 100 · VHJ (Vídeos Homenagem com Jesus). A foto de uma pessoa vira um anúncio 9:16 de ~18 s com a essência fixa (jardim → clarão → sobe a escada do céu → vira e acena → abraça Jesus no topo), animado pelo Grok, com narração na voz do autor, trilha e CTA "Toque em Saiba mais". É o modelo de ANÚNCIO do serviço. Use quando ele pedir "VHJ", "estilo 100", "vídeos homenagem com Jesus", "anúncio de homenagem", "faz um criativo da homenagem", "variação do VHJ". Para pedido de cliente real use o 101 · VHC.
---

# 100 · VHJ — Vídeos Homenagem com Jesus (modelo de anúncio)

Combinado com o autor em 22/11/2026. A **essência** é sempre a mesma: a pessoa sorri no jardim, a cena clareia,
ela sobe a escada do céu, **vira e acena**, e no topo **abraça Jesus**. O que muda entre criativos é a copy e a edição.
Receita e tempos: `~/Fabrica-de-Criativos/acervo/efeitos-e-estilos/meus-estilos/100-vhj/RECEITA.md`.
Para entrega a cliente (família que pagou), NÃO use este: use **101 · VHC** (`estilo-aluno-101-vhc`), que roda o mesmo
`homenagem.py` desta pasta com `--cliente`.

## Criativo novo a partir de uma foto
1. Salve a foto em `~/Fabrica-de-Criativos/saidas/homenagem/_fotos/<nome>.jpg`.
2. Avise em 1 linha: "Gerando o VHJ de <nome>. Custo ~R$ 4 (Grok)." (gasto por foto já autorizado; pergunte só se forem várias de uma vez ou se o saldo do xAI acabar).
3. Rode a partir desta pasta (timeout 10 min):
   `PYTHONIOENCODING=utf-8 python -I homenagem.py "<foto>" --nome <nome>`
   Gera 3 imagens e 3 clipes no Grok e monta com a narração fixa (`assets/n1..n3.mp3`). Caiu? Rode de novo: pula o que existe.
4. Confira `imagens.jpg` (mesma pessoa nas 3 cenas) e `folha.jpg` (aceno e abraço aparecem). Cena errada: apague o arquivo
   dela (ex. `b.jpg` + `v2.mp4` + a chave `b` do `estado.json`) e rode de novo (~R$ 1 a 2).
5. Entregue com SendUserFile e uma cópia leve (720×1280) na pasta Downloads para o WhatsApp.

## Variações de copy/edição (sem gastar Grok)
Reaproveite as cenas prontas e mude só copy e edição, um estilo oficial da Fábrica por variação (já feitas: 3 Letreiro,
1 Antes e depois, 19 Documentário, 10 Por nicho, 20 Três passos, 18 Colagem/presente, 4 Plantão, 22 Hard Copy noir,
34 Dossiê). Script de referência: `~/Fabrica-de-Criativos/saidas/homenagem/variacoes/fazer.py` (legenda palavra a palavra,
palavras gigantes, SFX, Space ao vivo em `index.html`). As variações não viram modelos novos: são todas VHJ.
Narração nova gasta cota do ElevenLabs; sem cota, reaproveite uma narração já gravada (copie `voz.mp3` + `voz.json`).

## Regras
- Foto de pessoa real só com autorização da família. Nunca usar texto, música ou imagem da referência original.
- Escassez/prazo só se forem reais. Todo ffmpeg com tempo máximo; depois de erro, confira se nada ficou parado.
- Se a figura religiosa não combinar com o público, troque "Jesus in a white robe…" por "a warm figure of light".
