---
name: serie-peaky-shelby
description: Produz um episódio da série @shelby.explica (Peaky Blinders em animação 3D estilizada, 9:16, 3–4 min), da análise da cena de referência até o mp4 final, capas YouTube/TikTok e legenda com hashtags. Receita aprovada pelo autor nos ep. 1 ("O homem que não piscava") e ep. 2 ("A cova"). Enredo com missão (começo, desenrolar, fim e gancho), lições "O QUE ELE SABIA", falas com boca pelo Grok, narrador ElevenLabs, cenas de ação bem animadas e CTA "comenta PARTE N". Use quando o autor pedir "faz a parte 3 do Tommy", "próximo episódio do Peaky", "episódio do shelby.explica", "faz igual ao ep. 2", "série do Thomas Shelby" ou mandar uma cena da série para virar episódio.
---

# Série @shelby.explica: receita completa

Projeto-modelo: `C:\LAILLA_AUTOMACAO\raea-projetos\peaky-temporada-1\` (`episodio-1\`, `episodio-2\`, `thumbs\`, `legendas-tiktok.md`).
Os scripts do ep. 2, prontos para copiar, ficam em `modelos\` nesta skill.

## Regras fixas do autor (não negociáveis)

1. **Tudo dentro de `C:\LAILLA_AUTOMACAO`.** Cada episódio fica em `raea-projetos\peaky-temporada-1\episodio-N\`.
2. **Missão com direção.** O episódio precisa ter começo, desenrolar e fim, além de um gancho para o próximo. O autor reclamou que o ep. 1 parecia "só uma abertura" antes de ganhar uma missão.
3. **Sempre fechar com CTA.** O Tommy (ou o narrador) provoca a próxima parte, e o último beat diz "Comenta PARTE N+1 aqui embaixo". O CTA aparece na fala e também na tela, como etiqueta vermelha `COMENTA "PARTE N+1"`.
4. **Cenas de ação bem animadas.** Tiros, quedas e perseguições usam Grok com som do próprio clipe e nunca ficam em imagem parada.
5. **Personagens sempre estilizados em 3D cartoon, nunca rosto realista de ator.** Se um clipe sair com close realista, refaça.
6. **"Praticamente tudo animado".** O padrão aprovado é Grok em todos os beats, sem Ken Burns. Use Ken Burns (kb) só se o saldo não der.
7. **Chaves só no `.env`** (`C:\LAILLA_AUTOMACAO\Fabrica-de-Criativos\.env`), nunca no chat. Não faça pagamentos: o autor recarrega o xAI sozinho.
8. **Orçamento antes de gastar.** Passe o custo previsto, respeite o teto que o autor der e anote tudo em `custos.csv`, no projeto `peaky-epN`.
9. **O Space fica sempre aberto** (`http://localhost:8770/?p=peaky-temporada-1/episodio-N`, ver memória `space-sempre-aberto`). Atualize `space.json` e `estado.json` a cada etapa, e abra o painel de progresso nos renders longos.
10. Sempre com legenda palavra a palavra.

## Fórmula do enredo (o que fez o ep. 2 funcionar)

Duração: 3,5 a 4 min, com cerca de 40 beats, e cada beat é uma cena na tela.

| Bloco | Tempo | O que acontece |
|---|---|---|
| **GANCHO** | 0:00–0:15 | Abre **no momento mais tenso do episódio** (flash-forward). Primeiro o Tommy fala uma frase curta com boca, depois o narrador pergunta "como ele foi parar aqui?" e volta no tempo. |
| **ATO 1 · A missão** | ~35 s | Alguém poderoso impõe a missão ao Tommy, que aceita com calma (cigarro, poucas palavras) e já tem o próprio plano. Termina em **LIÇÃO**. |
| **ATO 2 · O plano dele** | ~45 s | O Tommy monta a jogada e recruta aliados perigosos, com uma troca de falas curta entre dois personagens. Termina em **LIÇÃO**. |
| **ATO 3 · O que ele tem a perder** | ~35 s | Família ou amor. Uma fala emocional dá a ele um motivo para sobreviver. |
| **ATO 4 · O clímax da missão** | ~35 s | Tudo dá certo, seguido de **LIÇÃO**. Feche com a virada: "e foi exatamente aí que ele baixou a guarda". |
| **ATO 5 · A virada** | ~50 s | É a cena mais animada, com 2 ou 3 beats `acao` de 5 a 6 s cada, som do próprio Grok e sem narração. Cada beat traz uma fala curta de outro personagem e termina em **LIÇÃO**. |
| **FECHO + CTA** | ~25 s | O Tommy sobrevive ou recomeça. O narrador faz uma **pergunta ao espectador** sobre a vida dele. O Tommy olha para a câmera e diz uma frase que promete a próxima parte, como "Eu saí da cova. Agora... eu vou atrás de quem cavou." Depois vem o CTA "Comenta PARTE N+1". |

- **Lições:** são 3 ou 4 por episódio, sempre como etiqueta `O QUE ELE SABIA` e narração "O que ele sabia: …". Cada uma é uma frase de mentalidade ou estratégia aplicável à vida.
- **Falas:** são de 7 a 9 por episódio, curtas (até 12 palavras) e em PT-BR natural. Uma delas ecoa a frase icônica da cena original, adaptada.
- **Narrador:** tem tom de contador de história, segunda pessoa às vezes ("Lembra do inspetor…?") e frases curtas.
- **Roteiro para aprovar:** escreva `roteiro.md` no formato do ep. 2, com 🗣️ para falas, 🎙️ para narração, 💡 para lições, `[Ação: …]` e `[Cena: …]`, mais as seções "Sons" e "Quem faz o quê". **Mostre o roteiro, o custo previsto e as capas ao autor antes de gerar vídeo.**
- **Cena de referência:** quando o autor manda um link do YouTube, use `assistir-video-de-referencia` (frames e STT) para captar o enquadramento, a ação e a frase icônica. Em seguida, reconte a cena com o elenco 3D.
- **Continuidade:** o gancho no fim do episódio N tem que ser cumprido no começo do N+1. Se o autor pedir, edite o final do episódio anterior para o Tommy provocar a próxima parte. No ep. 1, isso foi feito trocando a fala do b40 e acrescentando o beat CTA b41.

## Pipeline técnico (passo a passo)

Na pasta do episódio, copie os arquivos de `modelos\` (`plano.py`, `narrar.py`, `animar_ep.py`, `montar_ep.py`) e troque:
- em `montar_ep.py`, a etiqueta do CTA (`'COMENTA "PARTE N+1"'`), a lista de SFX e os IDs que abafam a música na ação (`em('b31')`/`em('b35')`);
- em `animar_ep.py`, o nome do projeto (`peaky-epN`).

### 1. Elenco 3D (Codex, grátis)
- Reaproveite `episodio-2\ref\3d-*.png`: tommy, arthur, polly, grace, ada, freddie, inspetor, campbell, alfie, sabini e soldado.
- Para um personagem novo, gere a folha 3D no Codex (skill `codex-imagens`) usando `3d-tommy.png` como referência de estilo. Siga o modelo `modelos\pedido-elenco.json`.

### 2. `plano.py`
É a fonte única do episódio:
- `TITULO`, `SAIDA`;
- a lista `B` de tuplas `(id, tipo, quem, texto, cena, anim, refs, movimento, tag)`:
  - `tipo`: `narr` (narrador ElevenLabs), `fala` (o personagem fala pelo Grok, com boca) ou `acao` (sem narração, só o som do clipe; nesse caso `texto` é a duração em segundos);
  - `cena`: prompt em inglês da imagem, com personagens em MAIÚSCULAS conforme os refs;
  - `anim`: `"720"` (closes, rostos e ação) ou `"480"` (planos abertos e cenas lentas, que saem mais baratos). `"kb"` é só para economizar;
  - `movimento`: prompt em inglês do que se mexe (câmera e personagens). Nos beats `acao`, inclua `Sound: …` e `No music, no speech.`;
  - `tag`: `"LICAO"`, `"CTA"` ou `None`;
- `VOZ_DESC` (como cada personagem fala) e `QUEM` (como o Grok identifica quem fala na imagem, por aparência).

### 3. Cenas (Codex, grátis)
- Monte um `cenas\pedido.json` com uma cena por beat e os refs de cada uma (veja `modelos\pedido-cenas.json`). Rode `python ferramentas\codex-imagens\gerar.py pedido.json --saida cenas`; ele gera 5 imagens em paralelo.
- Monte uma folha de contato e **confira a continuidade**: o mesmo cenário em toda a sequência de ação, sem cemitério, lápides ou elementos que o roteiro não pede. Na ação, gere a imagem seguinte com a anterior como referência, para manter o mesmo campo, caminhão e céu.

### 4. Narração (ElevenLabs, grátis no plano free)
- Rode `python narrar.py`. Ele usa o modelo `eleven_multilingual_v2` com stability 0.45, similarity 0.8, style 0.35 e speed 1.0, a voz definida em `ELEVENLABS_VOICE_ID` e `previous_text`/`next_text` para dar fluidez.
- Ele grava `audio\bXX.mp3`, `.json` (os tempos por letra) e `duracoes.json`. Rode antes de animar, porque a duração do clipe depende da narração.
- O plano free tem cerca de 10 mil caracteres por mês, e um episódio gasta uns 2.500.

### 5. Animação (Grok Imagine video 1.5-lite)
Rode `PYTHONIOENCODING=utf-8 python animar_ep.py --paralelo 4`. Se a rede cair, rode de novo: ele pula os clipes que já existem. Para refazer só alguns, use `--so b33`.
- **Duração do clipe por tipo:**
  - narr: ceil(narração + 0,4), entre 2 e 15 s;
  - fala: ceil(palavras × 0,45 + 1,6), entre 3 e 8 s;
  - acao: o número que está no plano.
- **Prompt de fala:** `{QUEM} says in Brazilian Portuguese, {VOZ_DESC}: "frase" Clear lip movement… Only this character speaks. No music.` A boca sai sincronizada em PT-BR.
- **Sufixo de estilo em todo prompt:** `Keep exactly the same 3D cartoon art style, characters and faces. No text on screen.`
- **Se o clipe sair errado,** primeiro corrija a **imagem** (o Grok obedece à imagem mais do que ao texto) e só então reanime. Antes de refazer, guarde o clipe velho em `clipes\kb-v1\` (ou `-v2`).

### 6. Montagem (`montar_ep.py`)
Faz tudo de uma vez:
- STT `scribe_v1` nas falas;
- linha do tempo (narração + pausa de 0,25 s; a fala usa o próprio áudio do Grok; o beat `acao` usa o som do clipe com duração fixa);
- vídeo em 1080×1920 a 30 fps;
- legenda ASS palavra a palavra (Arial Black para o narrador, Georgia itálica para as falas);
- título no início (`{TITULO}`);
- etiquetas `O QUE ELE SABIA` e `COMENTA "PARTE N+1"`;
- trilha do acervo a volume 0,11, abafada para 0,15 durante a ação;
- SFX (stinger de porta nas viradas e riser de trem antes do clímax);
- loudnorm em −14 LUFS.

Depois da montagem, **ajuste o volume** até chegar a cerca de −13,4 LUFS. Copie o vídeo com `-c:v copy` e passe o áudio por `-af "volume=2.3dB,alimiter=limit=0.89"` (ajuste o ganho medindo com `ebur128`). Por fim, gere a cópia de celular: 720×1280, ~900 kbps, abaixo de 30 MB, chamada `episodio-N-celular.mp4`. Mande essa cópia ao autor com SendUserFile.

### 7. Conferência
- Extraia uma folha de quadros por beat e confira a continuidade e o estilo (nenhum rosto realista).
- Ouça a região da ação.
- **Gere a prévia de novo** depois de cada correção, porque uma prévia velha engana.

### 8. Capas e legenda
- **Capas:**
  - copie `modelos\pedido-capas-yt.json` e `pedido-capas-tt.json` para `thumbs\` e gere a arte sem texto no Codex;
  - coloque o texto com ffmpeg `drawtext` em fonte Impact (amarelo e branco com contorno preto);
  - YouTube 1280×720: `TÍTULO CURTO / SUBTÍTULO / PEAKY BLINDERS · EP. N`;
  - TikTok 1080×1920: o texto no terço de cima, para não ficar sob a interface;
  - saídas: `yt-epN-final.jpg` e `tt-epN-final.jpg`.
- **Legenda TikTok** (acrescente ao `peaky-temporada-1\legendas-tiktok.md`):
  - uma primeira linha que prende sozinha;
  - de 2 a 3 linhas de história;
  - a lição;
  - uma pergunta ao espectador;
  - `Comenta "PARTE N+1"`;
  - de 10 a 14 hashtags: `#peakyblinders #thomasshelby #tommyshelby #shelby #peakyblindersedit #mentalidade #estrategia #<tema> #animacao3d #historias #licoesdevida #fyp #foryou #viral`.
- Perfil `@shelby.explica`.

## Custos de referência (Grok, nov/2026)

| Item | Custo |
|---|---|
| Grok lite 720p | ≈ US$ 0,032/s |
| Grok lite 480p | ≈ US$ 0,023/s |
| Episódio de 3,5 min **todo animado** | ≈ US$ 7 (ep. 2 = US$ 7,01, contando os refazimentos) |
| Versão econômica (só falas + ação no Grok, resto em kb) | ≈ US$ 3 |
| Refazer 1 clipe | US$ 0,15 a 0,25 |
| Codex (imagens) | grátis |
| ElevenLabs (plano free) | grátis |

**Runway:** a conta do autor está no plano Free. Os 1.492 créditos do app não geram vídeo sem plano pago, porque o botão mostra "Upgrade". Os créditos da API são separados (US$ 0,01 cada, mínimo de US$ 10), e o Gen-4 Turbo custa 5 créditos por segundo. O Codex não controla o Chrome do autor. Só considere o Runway se o autor assinar um plano.

## Armadilhas já resolvidas
- **Erro `UnicodeEncodeError` (cp1252) no Windows:** rode os scripts com `PYTHONIOENCODING=utf-8`/`PYTHONUTF8=1`. Para patches com acento, use um arquivo `.py` em vez de colar no stdin.
- **Falha de rede no Grok (`RemoteDisconnected`, timeout):** não é moderação. Rode `animar_ep.py` de novo.
- **Ao editar `plano.py` com regex,** confira a vírgula entre a lista de refs e o movimento. Teste com `python -c "exec(open('plano.py').read())"`.
- **Erro "Device or resource busy" ao mover o mp4:** o Space está com o vídeo aberto. Leve o painel para `http://localhost:8770/` antes de mover.
- **Mexer no final de um episódio já pronto:** faça backup antes (`episodio-N-v1.mp4`, `clipes\bXX-v1.mp4`).
