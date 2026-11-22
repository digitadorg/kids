---
name: estilo-aluno-100-homenagem-ceu
description: Estilo 100 do aluno, "Homenagem no céu". A foto de quem partiu vira um filme 9:16 (jardim, clarão, subida da escada no céu com aceno, abraço no topo), animado pelo Grok Imagine, sem narração, com trilha emotiva e caixa de texto branca. Use quando pedirem "estilo 100", "homenagem no céu", "vídeo de homenagem", "vídeo de luto", "subida ao céu" ou mandarem a foto de alguém que faleceu para virar homenagem.
---

# Estilo 100 · Homenagem no céu

Receita completa (tempos, prompts, montagem): `~/Fabrica-de-Criativos/acervo/efeitos-e-estilos/meus-estilos/100-homenagem-ceu/RECEITA.md`. Leia antes de começar.
Amostra aprovada (22/11/2026): `~/Fabrica-de-Criativos/acervo/referencias/ad-1649926543212861/amostra/amostra-v2.mp4`.

## Fluxo
1. **Entrada:** foto da pessoa (de frente, da cintura para cima ou inteira), nome ou apelido opcional, textos do anúncio. Sem foto, gere uma pessoa fictícia.
2. **Custo:** cerca de US$ 0,75 por pessoa (3 imagens + 20 s de vídeo). Diga o valor e espere o "pode".
3. **Imagens** (pasta do pedido em `~/Fabrica-de-Criativos/saidas/<slug>/`):
   - A (jardim): se a foto é do cliente, ela precisa de uma URL pública para o Grok. Gere A com `images/edits` a partir da foto, ou peça ao autor um link. Sem foto: `python -I grok.py img a.jpg "<prompt A>"`.
   - B e C: `python -I grok.py img b.jpg "<prompt B>" <URL de A>` e `... c.jpg "<prompt C>" <URL de B>`. O script imprime a URL de cada imagem; guarde as URLs.
   - Confira as imagens (mesma pessoa e mesma roupa) antes de animar.
4. **Vídeo:** `python -I grok.py vid v1.mp4 <URL A> 5 "<prompt>"`, `v2.mp4 <URL B> 10`, `v3.mp4 <URL C> 5`. Pode rodar os três em paralelo.
   Use `PYTHONIOENCODING=utf-8`. O `grok.py` está nesta pasta da skill e lê `XAI_API_KEY` do `.env` sem mostrar o valor.
5. **Montagem:** ffmpeg conforme a RECEITA (fadewhite, caixas de texto a 56% da altura, trilha, −14 LUFS). Para 2 pessoas, emende os dois blocos com um clarão.
6. **Entrega:** folha de contato para conferir, depois mande o mp4 com SendUserFile. Para anúncio, entregue em par (ADS "Toque em Saiba mais" e ORG "Comenta HOMENAGEM").

## Regras
- Cores e fontes da seção "Minha identidade" do CLAUDE.md da Fábrica; vazio = Arial Bold, preto no branco.
- Não usar texto, música nem imagens da referência original. Escassez só se for real.
- Foto de pessoa real só com autorização da família.
- Se a figura religiosa não combinar com o público, troque por "a warm figure of light" no topo.
