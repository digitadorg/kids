"""Chamadas mínimas ao Grok (xAI). Uso:
  grok.py img  <saida.jpg> "<prompt>" [url_ref]
  grok.py vid  <saida.mp4> <url_imagem> <segundos> "<prompt>"
A chave vem do .env da Fábrica e nunca é impressa."""
import json, pathlib, sys, time, urllib.request

ENV = pathlib.Path.home() / "Fabrica-de-Criativos" / ".env"
KEY = next(l.split("=", 1)[1].strip().strip('"') for l in ENV.read_text(encoding="utf-8").splitlines() if l.startswith("XAI_API_KEY="))
H = {"Authorization": "Bearer " + KEY, "Content-Type": "application/json", "User-Agent": "fabrica-cli"}


def call(method, url, body=None):
    req = urllib.request.Request(url, method=method, headers=H, data=json.dumps(body).encode() if body else None)
    try:
        return json.load(urllib.request.urlopen(req, timeout=120))
    except urllib.error.HTTPError as e:
        print("HTTP", e.code, e.read().decode()[:400]); sys.exit(1)


def baixar(url, saida):
    print("URL", url, flush=True)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    pathlib.Path(saida).write_bytes(urllib.request.urlopen(req, timeout=300).read())


modo, saida = sys.argv[1], sys.argv[2]
if modo == "img":
    prompt = sys.argv[3]
    ref = sys.argv[4] if len(sys.argv) > 4 else None
    if ref:
        r = call("POST", "https://api.x.ai/v1/images/edits", {"model": "grok-imagine-image", "prompt": prompt, "image": {"url": ref, "type": "image_url"}, "aspect_ratio": "9:16"})
    else:
        r = call("POST", "https://api.x.ai/v1/images/generations", {"model": "grok-imagine-image", "prompt": prompt, "n": 1, "aspect_ratio": "9:16"})
    url = r["data"][0]["url"]
    baixar(url, saida)
    print("URL", url)
else:
    img, seg, prompt = sys.argv[3], int(sys.argv[4]), sys.argv[5]
    r = call("POST", "https://api.x.ai/v1/videos/generations", {"model": "grok-imagine-video-1.5-lite", "prompt": prompt, "image": {"url": img}, "duration": seg, "resolution": "720p", "aspect_ratio": "9:16"})
    rid = r["request_id"]
    print("pedido", rid, flush=True)
    for _ in range(120):
        time.sleep(5)
        s = call("GET", f"https://api.x.ai/v1/videos/{rid}")
        if s.get("status") in ("done", "failed", "expired"):
            break
    if s.get("status") != "done":
        print("FALHOU", json.dumps(s)[:400]); sys.exit(1)
    baixar(s["video"]["url"], saida)
    print("OK", saida, {k: v for k, v in s.items() if k not in ("video",)})
