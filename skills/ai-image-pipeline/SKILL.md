---
name: ai-image-pipeline
description: Pipeline validado de prévia com IA — foto do cliente normalizada no navegador e no Sharp, guardada no Netlify Blobs, gerada em Background Function pela API de imagem da OpenAI (images/edits com foto + cenário), marca-d'água determinística, status por polling e barra de progresso honesta. Use ao mexer em upload de foto, HEIC/AVIF, prompt, modelo/qualidade de imagem, marca-d'água, tamanho da prévia ou tempo de geração.
---

# Pipeline de imagem com IA

```
navegador: HEIC→JPEG (heic2any) / canvas.toBlob  →  POST multipart /api/upload
  Sharp: rotate() (EXIF) → flatten branco → máx 1536 → sRGB → JPEG q88 → Blobs inputs/<jobId>.jpg
POST /api/gerar (só jobId + textos) → Background:
  lê Blobs + cenário local → OpenAI images/edits [pessoa, cenário], size 1024x1536
  erro 429 → espera 8 s; outro → 1,5 s; 2ª tentativa com prompt simplificado
  Sharp: 820×1230 + sharpen + SVG marca-d'água → WebP q82 (se > 1,85 MB: 720×1080 q74)
  Blobs jobs/<jobId> = {status:"complete", image}
navegador consulta /status?job= até complete
```

## Regras

- Nunca base64 grande direto para a Background Function.
- Modelo e qualidade são decisão do dono (variável `OPENAI_IMAGE_MODEL`; qualidade fixa no código). Não trocar para baratear sem autorização.
- Prompt principal + prompt de contingência: não reescrever sem teste comparativo (mesmas fotos, lado a lado).
- Preservar identidade: rosto, idade, cabelo, pele, roupa. Se a foto for sentada/cortada, reconstruir corpo em pé coerente. Sem pessoas extras.
- Marca-d'água **no backend** (Sharp/SVG), determinística. Evite pedir também no prompt: a IA escreve texto torto.
- Barra de progresso por tempo, **travada abaixo de 100%** (ex.: 94%) até o status real ser `complete`. Nunca mostrar resultado falso.
- `limitInputPixels`, limite de bytes, honeypot no formulário e regex no jobId.
- Formatos: aceitar JPG/PNG/WEBP/HEIC/HEIF/AVIF no `<input>`, mas **testar** cada um antes de prometer suporte.
- Prévia ≠ produto final (o vídeo é feito depois).
