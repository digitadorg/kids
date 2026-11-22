---
name: estilo-aluno-100-homenagem-ceu
description: Estilo 100 do aluno, "Homenagem no céu". O autor manda SÓ A FOTO de uma pessoa e você entrega o vídeo pronto, 9:16, ~18 s (jardim, clarão, subida da escada no céu com aceno, abraço no topo), animado pelo Grok, com a narração fixa na voz dele, trilha e caixa de texto branca. Use quando ele mandar uma foto pedindo homenagem, ou pedir "estilo 100", "homenagem no céu", "vídeo de homenagem", "vídeo de luto", "subida ao céu".
---

# Estilo 100 · Homenagem no céu (padronizado)

O autor combinou em 22/11/2026: **ele manda a foto, você faz tudo.** É sempre o mesmo vídeo; só muda a pessoa.
Receita e tempos: `~/Fabrica-de-Criativos/acervo/efeitos-e-estilos/meus-estilos/100-homenagem-ceu/RECEITA.md`.

## Quando chegar uma foto
1. Salve a foto em `~/Fabrica-de-Criativos/saidas/homenagem/_fotos/<nome>.jpg` (nome curto, sem acento; use o nome da
   pessoa se ele disser, senão `pessoa-AAAAMMDD-HHMM`).
2. Avise em 1 linha: "Gerando a homenagem de <nome>. Custo ~R$ 4 (Grok)." O autor já autorizou esse gasto por foto;
   só pare e pergunte se ele mandar várias fotos de uma vez (diga o total) ou se o saldo do Grok acabar.
3. Rode (timeout 10 min), a partir da pasta desta skill:
   `PYTHONIOENCODING=utf-8 python -I homenagem.py "<foto>" --nome <nome>`
   Ele gera as 3 imagens, confere nada sozinho, anima os 3 clipes em paralelo, monta e imprime `PRONTO <caminho>` e
   `GASTO_GROK`. Caiu no meio? Rode o mesmo comando de novo: ele pula o que já existe.
4. **Confira antes de entregar:** abra `imagens.jpg` (a mesma pessoa nas 3 cenas? rosto parecido com a foto?) e
   `folha.jpg` (aceno e abraço aparecem?). Se uma cena saiu errada, apague só o arquivo dela (ex.: `b.jpg` e `v2.mp4`, e a
   chave `b` do `estado.json`) e rode de novo. Cada refazer custa ~R$ 1 a 2.
5. Entregue o `homenagem.mp4` com SendUserFile e diga o gasto em real (US$ × ~5,50).

## O que é fixo
- Narração (voz do autor, ElevenLabs, já gravada em `assets/n1..n3.mp3`, sem custo por vídeo):
  "Tem sorrisos que a gente nunca esquece." · "E se você pudesse ver de novo... aquele aceno de quem diz: eu tô bem." ·
  "Transforme a foto de quem você ama numa homenagem. Toque em Saiba mais."
- Textos na tela iguais à fala; CTA "Toque em Saiba mais".
- Trilha `acervo/sons/02-trilhas/07-cinematografico-suave/Cloudbreak__Jobii.wav`, −14 LUFS.
- `--res 480p` deixa ~30% mais barato (pior qualidade).

## Regras
- Foto de pessoa real só com autorização da família. Nunca usar texto, música ou imagem da referência original.
- Se o autor pedir outra fala, gere os 3 mp3 novos com o ElevenLabs (avise que gasta ~200 caracteres da cota) e troque em `assets/`.
- Se a figura religiosa não combinar com o público, troque "Jesus in a white robe…" por "a warm figure of light" nos prompts.
