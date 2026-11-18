"""Gera imagens em lote pelo Codex (conta do ChatGPT), varias ao mesmo tempo.

Uso:
  python gerar.py pedido.json [--paralelo 5] [--saida PASTA] [--refazer]

pedido.json:
{
  "estilo": "texto colado no inicio de TODO prompt (estilo e personagens)",
  "formato": "9:16",                      # 9:16 (stories), 16:9, 1:1, 4:5
  "referencias": ["ref/menino.png"],       # imagens enviadas em todo pedido (opcional)
  "cenas": [
    {"id": "cena_01", "prompt": "o que aparece nesta cena",
     "referencias": ["ref/jesus.png"]}     # referencias extras so desta cena (opcional)
  ]
}

Cada cena vira um `codex exec` separado. O Codex gera a imagem e a deixa em
~/.codex/generated_images/<sessao>/; este script acha o arquivo e copia para
<saida>/<id>.png. Cenas que ja tem arquivo sao puladas (use --refazer para gerar de novo).
O log de cada cena fica em <saida>/_logs/<id>.log e o resumo em <saida>/_resultado.json.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

GEN_DIR = Path.home() / ".codex" / "generated_images"
FORMATOS = {
    "9:16": "vertical portrait 9:16 (Instagram Stories / Reels), the subject framed for a tall phone screen",
    "16:9": "horizontal landscape 16:9",
    "1:1": "square 1:1",
    "4:5": "vertical portrait 4:5 (Instagram feed)",
}
TIMEOUT_S = 600
lock = threading.Lock()


def log(msg):
    with lock:
        print(time.strftime("%H:%M:%S"), msg, flush=True)


def montar_prompt(pedido, cena):
    fmt = FORMATOS.get(pedido.get("formato", "9:16"), pedido.get("formato", "9:16"))
    partes = [
        "Use your image generation tool to create exactly ONE image. Do not run shell commands, "
        "do not read or write files, do not ask questions. When the image is done, reply only with DONE.",
        f"Format: {fmt}.",
    ]
    if pedido.get("referencias") or cena.get("referencias"):
        partes.append("The attached image(s) are character/style references: keep the same characters "
                      "(face, hair, clothes, proportions) and the same drawing style exactly.")
    if pedido.get("estilo"):
        partes.append("Style and characters: " + pedido["estilo"].strip())
    partes.append("Scene: " + cena["prompt"].strip())
    return "\n\n".join(partes)


# ---------------------------------------------------------------------------
# Daqui para baixo o codigo foi reconstruido em 18/11/2026: o original se perdeu
# junto com o computador e so as linhas de cima apareceram nas conversas.
# O comportamento segue o que estava documentado e o que aparecia nos logs.
# ---------------------------------------------------------------------------

def achar_codex():
    for nome in ("codex", "codex.cmd", "codex.exe"):
        caminho = shutil.which(nome)
        if caminho:
            return caminho
    sys.exit("Codex CLI nao encontrado. Instale com: npm install -g @openai/codex  e depois rode: codex login")


def resolver_refs(pedido, cena, base):
    refs = list(pedido.get("referencias") or []) + list(cena.get("referencias") or [])
    saida = []
    for r in refs:
        p = (base / r).resolve()
        if not p.exists():
            raise FileNotFoundError(f"referencia nao encontrada: {r}")
        if p not in saida:
            saida.append(p)
    return saida


def pngs_novos(desde, sessao=None):
    if not GEN_DIR.exists():
        return []
    pasta = GEN_DIR / sessao if sessao and (GEN_DIR / sessao).is_dir() else GEN_DIR
    achados = [f for f in pasta.rglob("*") if f.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")
               and f.stat().st_mtime >= desde]
    return sorted(achados, key=lambda f: f.stat().st_mtime)


def gerar_cena(codex, pedido, cena, base, saida, usados):
    cid = cena["id"]
    destino = saida / f"{cid}.png"
    log_cena = saida / "_logs" / f"{cid}.log"
    refs = resolver_refs(pedido, cena, base)
    cmd = [codex, "exec", "--skip-git-repo-check", "--sandbox", "read-only", "-C", str(saida)]
    for r in refs:
        cmd += ["-i", str(r)]
    cmd.append("-")
    inicio = time.time()
    with open(log_cena, "w", encoding="utf-8") as lf:
        try:
            proc = subprocess.run(cmd, input=montar_prompt(pedido, cena), capture_output=True,
                                  text=True, encoding="utf-8", errors="replace", timeout=TIMEOUT_S)
        except subprocess.TimeoutExpired:
            lf.write(f"TIMEOUT depois de {TIMEOUT_S}s\n")
            raise RuntimeError(f"timeout ({TIMEOUT_S}s)")
        texto = (proc.stdout or "") + "\n" + (proc.stderr or "")
        lf.write(texto)
    m = re.search(r"session id:\s*([0-9a-fA-F-]{8,})", texto)
    sessao = m.group(1) if m else None
    with lock:
        candidatos = [f for f in pngs_novos(inicio, sessao) if f not in usados]
        if not candidatos:
            raise RuntimeError(f"o Codex nao devolveu imagem (codigo {proc.returncode}); veja _logs/{cid}.log")
        img = candidatos[-1]
        usados.add(img)
    shutil.copy2(img, destino)
    return destino, time.time() - inicio


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="Gera imagens em lote pelo Codex.")
    ap.add_argument("pedido")
    ap.add_argument("--paralelo", type=int, default=5)
    ap.add_argument("--saida", default=None, help="pasta das imagens (padrao: pasta do pedido.json)")
    ap.add_argument("--refazer", action="store_true", help="gera de novo mesmo se a imagem ja existe")
    a = ap.parse_args()

    arq = Path(a.pedido).resolve()
    pedido = json.loads(arq.read_text(encoding="utf-8-sig"))
    base = arq.parent
    saida = Path(a.saida).resolve() if a.saida else base
    (saida / "_logs").mkdir(parents=True, exist_ok=True)
    codex = achar_codex()

    cenas = pedido.get("cenas") or []
    fila = [c for c in cenas if a.refazer or not (saida / f"{c['id']}.png").exists()]
    pulos = len(cenas) - len(fila)
    log(f"{len(fila)} cena(s) para gerar, {pulos} ja pronta(s), {a.paralelo} ao mesmo tempo")

    resultado, usados, feitos = {}, set(), 0
    with ThreadPoolExecutor(max_workers=max(1, a.paralelo)) as ex:
        futuros = {ex.submit(gerar_cena, codex, pedido, c, base, saida, usados): c["id"] for c in fila}
        for fut in as_completed(futuros):
            cid = futuros[fut]
            feitos += 1
            try:
                destino, seg = fut.result()
                resultado[cid] = {"ok": True, "arquivo": destino.name, "segundos": round(seg)}
                log(f"[{feitos}/{len(fila)}] OK  {cid}: {destino.name} em {seg:.0f}s")
            except Exception as e:
                resultado[cid] = {"ok": False, "erro": str(e)}
                log(f"[{feitos}/{len(fila)}] ERRO {cid}: {e}")

    (saida / "_resultado.json").write_text(json.dumps(resultado, ensure_ascii=False, indent=1), encoding="utf-8")
    ok = sum(1 for r in resultado.values() if r["ok"])
    log(f"FIM: {ok} ok, {len(resultado) - ok} com erro")
    sys.exit(0 if ok == len(resultado) else 1)


if __name__ == "__main__":
    main()
