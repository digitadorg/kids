---
name: codex-imagens
description: Gera imagens em lote pelo Codex CLI usando a assinatura do ChatGPT do autor (sem custo de API), 5 ao mesmo tempo, com personagens consistentes por imagem de referência. O Claude orquestra (escreve o pedido, dispara, confere e refaz) e o Codex desenha. Use quando precisar de várias imagens/ilustrações para vídeo, stories, reels, carrossel, capas ou cenas do raea/HyperFrames/Remotion, ou quando o autor pedir "gera as imagens pelo Codex/ChatGPT", "faz as cenas no Codex", "cria o elenco" ou "imagens em massa".
---

# Imagens em lote pelo Codex

O Claude é o **orquestrador**: entende o pedido, escreve os prompts, dispara o lote, confere o resultado e manda refazer o que saiu errado. O **Codex** só desenha. Cada imagem sai pela assinatura do ChatGPT do autor, então **não tem custo por imagem**.

Ferramenta: `gerar.py`, nesta pasta da skill (Python, só biblioteca padrão). No computador antigo ficava em `C:\LAILLA_AUTOMACAO\ferramentas\codex-imagens\gerar.py`.
Cada cena vira um `codex exec` separado (sandbox read-only). O script acha a imagem em
`~/.codex/generated_images/<sessão>/` e copia para `<saida>/<id>.png`.

## Antes da primeira vez

1. Instale o Codex CLI: `npm install -g @openai/codex`.
2. Rode `codex login` e entre com a conta do ChatGPT do autor.
3. Faça um teste com um `pedido.json` de 1 cena. Se aparecer "o Codex não devolveu imagem", abra `_logs/<id>.log` para ver o que o Codex respondeu.

## Passo a passo

1. **Elenco primeiro.** Gere **uma folha de referência por personagem** (corpo inteiro ou da cintura para cima, fundo limpo, sem texto) e salve em `ref/`. Mostre ao autor antes de seguir. É isso que mantém o mesmo rosto em todas as cenas.
2. **Escreva o `pedido.json`** na pasta do projeto:

```json
{
  "estilo": "3D animated family feature film look, very rounded toy-like stylized characters, big heads and big expressive eyes, smooth simplified skin, cinematic volumetric light, cartoon CGI render. Exactly the same 3D style and the same characters as the attached reference images (keep faces, hair, clothes). Cinematic composition, no text, no letters, no logos. Characters: TOMMY (grey flat cap, pale blue eyes, dark overcoat), ARTHUR (thick dark mustache, flat cap). SCENE:",
  "formato": "9:16",
  "referencias": ["ref/3d-tommy.png"],
  "cenas": [
    {"id": "b01", "prompt": "Smoky pub at night, TOMMY alone at a corner table with a whiskey glass, cigarette smoke curling in lamp light."},
    {"id": "b02", "prompt": "Dim warehouse, TOMMY opens a long wooden crate full of rifles, ARTHUR behind him, nervous.",
     "referencias": ["ref/3d-arthur.png"]}
  ]
}
```

   - `estilo`: vai no começo de **todo** prompt. Coloque o estilo e a descrição fixa de cada personagem, com o nome em MAIÚSCULAS.
   - `formato`: `9:16` (stories e reels), `16:9`, `1:1` ou `4:5` (feed).
   - `referencias` no topo: imagens enviadas em todas as cenas, como o personagem principal ou uma imagem de estilo.
   - `referencias` dentro da cena: só os personagens que aparecem **naquela** cena. Os caminhos são relativos à pasta do `pedido.json`.
   - `prompt`: em inglês, curto e visual. Diga o lugar, quem aparece, o que está fazendo, a luz e o clima.

3. **Dispare o lote** em segundo plano, gravando o log:

```bash
PYTHONUTF8=1 python gerar.py pedido.json --saida cenas > cenas/gerar.log 2>&1
```

   - `--paralelo 5` é o padrão. Use 4 se o computador ou a conta ficarem lentos.
   - `--saida PASTA` diz onde salvar. Sem ela, salva ao lado do `pedido.json`.
   - `--refazer` gera de novo mesmo as cenas que já têm imagem.
   - As cenas que já têm `<id>.png` são puladas. Se a rede cair, é só rodar de novo.

4. **Acompanhe.** O log mostra `[3/36] OK  b07: b07.png em 154s` a cada imagem e termina com `FIM: N ok, M com erro`. O resumo fica em `_resultado.json` e o log de cada cena em `_logs/<id>.log`. Se o autor usa o Space ou o painel de progresso, atualize o painel enquanto o lote roda.
5. **Confira.** Monte uma folha de contato (todas as imagens lado a lado) e veja:
   - se o rosto e a roupa de cada personagem são os mesmos em todas as cenas;
   - se não apareceu texto, letra ou logo;
   - se o cenário é o mesmo nas cenas em sequência;
   - se não apareceu nada que o roteiro não pede.
6. **Refaça só o que saiu errado.** Renomeie a imagem ruim para `<id>-v1.png`, guardando o backup, ajuste o prompt e gere só aquela cena. Para isso, monte um `pedido-<id>.json` com só essa cena e rode o `gerar.py` com ele.

## Tempo e custo

- Cerca de **1,5 min por lote de 5**, ou de 2 a 3 min por imagem quando rodam 5 juntas.
- Um episódio com elenco e 36 a 45 cenas leva de 15 a 25 minutos.
- **Custo: US$ 0.** Usa a assinatura do ChatGPT, sem chave de API.
- Dá para animar enquanto as imagens saem. O animador pega cada cena assim que o `<id>.png` aparece.

## Dicas que funcionaram

- **Consistência:** sempre mande a folha do personagem como referência nas cenas em que ele aparece. O Codex mantém o rosto muito bem a partir da referência.
- **Continuidade em sequência de ação:** gere a imagem seguinte com a **anterior** como referência extra, para manter o mesmo campo, carro e céu. Escreva no prompt "Exactly the same location as the previous scenes" e liste o que **não** pode aparecer (por exemplo: "NO cemetery, NO gravestones").
- **Cartoon de verdade:** com fotos de uma pessoa real como referência, os estilos 3D, massinha e pintura a óleo tendem a sair como foto do ator. Nesses estilos, gere **sem as fotos**, só pela descrição, e escreva "Clearly stylized cartoon character, NOT a photo, NOT photorealistic".
- **Personagem original:** para não copiar um ator ou personagem com direitos, escreva "Invented cartoon character, not a real person" e descreva a aparência com as suas palavras.
- **Realista, quando o autor pedir:** "Ultra-photorealistic photograph, real skin texture with visible pores, natural film grain, 35mm lens, shallow depth of field".
- **Teste de estilos:** para escolher o visual de uma série nova, gere a mesma cena em 6 a 8 estilos (cartoon chapado, gibi, caricatura, anime aquarela, 3D, aquarela de livro, massinha) e mostre lado a lado.
- **Capas (YouTube e TikTok):** peça "leave clean empty space for a big title, no text" e ponha o texto depois, com ffmpeg `drawtext`.
- **Windows:** rode com `PYTHONUTF8=1` para evitar o erro `UnicodeEncodeError` (cp1252) com acentos.

## Quando der erro

| Mensagem | O que fazer |
|---|---|
| `Codex CLI nao encontrado` | Instale o Codex CLI e rode `codex login`. |
| `o Codex nao devolveu imagem` | Abra `_logs/<id>.log`. Se o Codex recusou o conteúdo, reescreva o prompt. Se não, rode de novo. |
| `timeout (600s)` | O Codex demorou demais. Rode de novo: as que já saíram são puladas. |
| `referencia nao encontrada` | O caminho em `referencias` está errado. Ele é relativo à pasta do `pedido.json`. |
