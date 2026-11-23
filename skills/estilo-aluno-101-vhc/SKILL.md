---
name: estilo-aluno-101-vhc
description: Modelo 101 · VHC (Vídeo Homenagem para Cliente). Prestação do serviço: quando uma família/cliente encomenda a homenagem, a foto de quem partiu vira o vídeo do VHJ (jardim, escada do céu, aceno, abraço em Jesus), SEM anúncio e SEM narração, com o nome, as datas e uma mensagem da família, trilha suave e fade final; sai em alta e em versão WhatsApp. Use quando o autor disser "VHC", "pedido de cliente", "pedido da família", "faz o vídeo do cliente", "entrega", "vídeo pra pessoa real", ou mandar foto + nome/datas de alguém que encomendou.
---

# 101 · VHC — Vídeo Homenagem para Cliente (entrega do serviço)

A mesma essência do **100 · VHJ**, mas é o **produto entregue** a quem pagou: nada de "Toque em Saiba mais", nada de copy
de venda. Usa o mesmo gerador do VHJ, em modo cliente.

## Pedido que chega
- **Obrigatório:** a foto (de frente, da cintura para cima ou inteira) e o **nome** como deve aparecer.
- **Opcional:** datas (ex. `1948 – 2025`), mensagem final da família (padrão: "Para sempre / em nossos corações").
- Faltou o nome? Pergunte só isso, em 1 linha. O resto tem padrão.

## Fazer
1. Salve a foto em `~/Fabrica-de-Criativos/saidas/clientes/_fotos/<nome-curto>.jpg`.
2. Avise: "Fazendo o VHC de <nome>. Custo ~R$ 4 (Grok)." (gasto por foto já autorizado; pergunte só se forem várias
   de uma vez ou se o saldo do xAI acabar).
3. Rode a partir de `~/.claude/skills/estilo-aluno-100-vhj/` (timeout 10 min):
   `PYTHONIOENCODING=utf-8 python -I homenagem.py "<foto>" --cliente --nome <nome-curto> --pessoa "<Nome Completo>" --datas "<1948 – 2025>" [--mensagem "Linha 1\nLinha 2"]`
   Saída em `~/Fabrica-de-Criativos/saidas/clientes/<nome-curto>/`: `homenagem.mp4` (1080×1920, ~19 s) e
   `homenagem-whatsapp.mp4` (leve, para mandar à família).
4. Confira `imagens.jpg` e `folha.jpg`: **o rosto precisa parecer com a foto** (é a mãe/pai de alguém). Se não parecer,
   refaça a imagem `a` (apague `a.jpg`, `b.jpg`, `c.jpg`, `v1..v3.mp4` e as chaves do `estado.json`) e avise o custo.
5. Copie a versão WhatsApp para `Downloads\VHC-<nome-curto>.mp4` e mande as duas ao autor com SendUserFile.

## Como fica
0–4 s jardim com o **nome** (serifa branca) e as **datas**; clarão; subida, aceno; abraço com a **mensagem** da família;
fade para o branco. Trilha `Cloudbreak` (acervo) a −14 LUFS, sem narração.

## Regras
- Só com autorização da família. Nunca publicar nem mandar a ninguém além do autor.
- Nome e datas exatamente como o cliente escreveu (acentos inclusive).
