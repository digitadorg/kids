"""Estilo 100 · Homenagem no céu — da foto ao vídeo pronto, num comando.

Uso:  PYTHONIOENCODING=utf-8 python -I homenagem.py <foto.jpg> [--nome slug] [--res 720p|480p]

Faz: 3 imagens no Grok (jardim, escada, abraço) com a pessoa da foto → 3 clipes animados no Grok →
narração fixa (já gravada, sem custo) → montagem 9:16 com textos, trilha e −14 LUFS.
Se cair no meio, rode de novo: o que já existe é pulado. A chave vem do .env da Fábrica e nunca é impressa.
"""
import argparse, base64, datetime, json, pathlib, subprocess, sys, threading, time, urllib.request

sys.stdout.reconfigure(encoding="utf-8")
AQUI = pathlib.Path(__file__).resolve().parent
FAB = pathlib.Path.home() / "Fabrica-de-Criativos"
ENV = {l.split("=", 1)[0].strip(): l.split("=", 1)[1].strip().strip('"')
       for l in (FAB / ".env").read_text(encoding="utf-8").splitlines() if "=" in l and not l.lstrip().startswith("#")}
KEY = ENV.get("XAI_API_KEY", "")
MUSICA = FAB / "acervo/sons/02-trilhas/07-cinematografico-suave/Cloudbreak__Jobii.wav"
FONTE = "C\\:/Windows/Fonts/arialbd.ttf"
PRECO = {"720p": 0.032, "480p": 0.023}

P_A = ("Use this exact person: same face, same age, same hair, same skin, same clothes if visible (otherwise simple elegant "
       "light-colored clothes). Photorealistic vertical portrait: the person standing facing the camera, body visible to the "
       "knees, warm gentle smile, in a sunny lush garden with colorful flowers and a small pond, soft golden afternoon light, "
       "shallow depth of field, natural skin texture, no text.")
P_B = ("Same exact person, same face, hair and clothes, now seen from behind, standing at the bottom of a long wide white "
       "marble staircase that rises into heaven through soft white clouds. At the very top of the stairs, small in the "
       "distance, Jesus in a white robe with a golden-brown sash stands with open arms. Strong golden god rays from above, "
       "warm heavenly glow, mist, photorealistic, cinematic, vertical 9:16, no text.")
P_C = ("Same exact person, same hair and clothes, now at the very top of the white marble staircase, seen from behind, "
       "warmly embracing Jesus in the white robe and golden-brown sash, who hugs the person tenderly with eyes closed and a "
       "peaceful smile, his face visible over the person's shoulder. Medium shot, closer than before. Strong golden god rays, "
       "soft clouds and mist, heavenly glow, photorealistic, cinematic, vertical 9:16, no text.")
V = [
    ("v1", "a", 5, "The person stands calmly in the garden, breathes, the smile grows warmer and gives a small loving nod to "
                   "the camera. Leaves sway gently, warm golden light slowly grows brighter from above. Very slow camera "
                   "push-in. Photorealistic. No speech, soft ambient birds only, no music."),
    ("v2", "b", 10, "The person slowly climbs the white marble stairs toward the light. Halfway up, stops, turns around to face "
                    "the camera, smiles tenderly and waves goodbye with one hand, then turns back and keeps climbing toward "
                    "Jesus, who waits at the top with open arms. Golden god rays, drifting mist, slow steady camera following "
                    "from behind. Photorealistic, keep the same person and clothes. No speech, no music."),
    ("v3", "c", 5, "They hold a long, tender embrace. Jesus gently pats the person's back and smiles peacefully with eyes "
                   "closed. The golden light slowly grows brighter and warmer, soft glowing particles float upward. Very slow "
                   "camera push-in. Photorealistic, keep the same faces and clothes. No speech, no music."),
]
TEXTOS = {"t1.txt": "Tem sorrisos que a gente\nnunca esquece",
          "t2.txt": "Ver de novo aquele aceno\nde quem diz: eu tô bem",
          "t3.txt": "Transforme a foto de quem você ama\nnuma homenagem como esta",
          "t4.txt": "Toque em Saiba mais"}
gasto = [0.0]


def api(method, url, body=None):
    for tent in range(3):
        req = urllib.request.Request(url, method=method, data=json.dumps(body).encode() if body else None,
                                     headers={"Authorization": "Bearer " + KEY, "Content-Type": "application/json",
                                              "User-Agent": "fabrica-cli"})
        try:
            return json.load(urllib.request.urlopen(req, timeout=180))
        except urllib.error.HTTPError as e:
            msg = e.read().decode()[:400]
            if e.code in (400, 401, 402, 403):
                sys.exit(f"ERRO do Grok ({e.code}): {msg}")
        except Exception as e:  # rede caiu
            msg = str(e)
        time.sleep(5 * (tent + 1))
    sys.exit(f"ERRO de rede com o Grok: {msg}")


def baixar(url, destino):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    destino.write_bytes(urllib.request.urlopen(req, timeout=300).read())


def imagem(estado, nome, prompt, ref_url, out):
    if nome in estado and (out / f"{nome}.jpg").exists():
        print(f"  [pulei] imagem {nome} já existe", flush=True); return
    r = api("POST", "https://api.x.ai/v1/images/edits",
            {"model": "grok-imagine-image", "prompt": prompt, "aspect_ratio": "9:16",
             "image": {"url": ref_url, "type": "image_url"}})
    estado[nome] = r["data"][0]["url"]; gasto[0] += 0.02
    baixar(estado[nome], out / f"{nome}.jpg")
    (out / "estado.json").write_text(json.dumps(estado, indent=1), encoding="utf-8")
    print(f"  [OK] imagem {nome}", flush=True)


def video(estado, nome, img, seg, prompt, res, out, erros):
    if (out / f"{nome}.mp4").exists():
        print(f"  [pulei] clipe {nome} já existe", flush=True); return
    try:
        r = api("POST", "https://api.x.ai/v1/videos/generations",
                {"model": "grok-imagine-video-1.5-lite", "prompt": prompt, "image": {"url": estado[img]},
                 "duration": seg, "resolution": res, "aspect_ratio": "9:16"})
        rid = r["request_id"]
        for _ in range(180):
            time.sleep(5)
            s = api("GET", f"https://api.x.ai/v1/videos/{rid}")
            if s.get("status") in ("done", "failed", "expired"):
                break
        if s.get("status") != "done":
            erros.append(f"{nome}: {s.get('status')}"); return
        ticks = (s.get("usage") or {}).get("cost_in_usd_ticks")
        gasto[0] += ticks / 1e10 if ticks else seg * PRECO[res]
        baixar(s["video"]["url"], out / f"{nome}.mp4")
        print(f"  [OK] clipe {nome} ({seg} s)", flush=True)
    except SystemExit as e:
        erros.append(f"{nome}: {e}")


def montar(out):
    for k, v in TEXTOS.items():
        (out / k).write_text(v, encoding="utf-8")
    T = 18.4
    dt = (f"fontfile='{FONTE}':fontcolor=black:fontsize=52:line_spacing=10:text_align=C:box=1:"
          f"boxcolor=white@0.96:boxborderw=22:x=(w-text_w)/2:y=h*0.56")
    esc = lambda i: f"[{i}:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1,format=yuv420p"
    fc = (f"{esc(0)}[a];{esc(1)}[b];{esc(2)},tpad=stop_mode=clone:stop_duration=0.9[c];"
          "[a][b]xfade=transition=fadewhite:duration=1.4:offset=3.8[ab];"
          "[ab][c]xfade=transition=fadewhite:duration=1.0:offset=12.6,eq=brightness=0.02:saturation=1.05[x];"
          f"[x]drawtext=textfile=t1.txt:{dt}:enable='between(t,0.5,5.0)',"
          f"drawtext=textfile=t2.txt:{dt}:enable='between(t,5.5,12.1)',"
          f"drawtext=textfile=t3.txt:{dt}:enable='between(t,12.3,{T})',"
          f"drawtext=textfile=t4.txt:fontfile='{FONTE}':fontcolor=white:fontsize=46:box=1:boxcolor=black@0.85:"
          f"boxborderw=18:x=(w-text_w)/2:y=h*0.56+190:enable='between(t,14.6,{T})'[v];"
          "[0:a]volume=0.15[a0];[1:a]volume=0.12[a1];[2:a]volume=0.12,apad=pad_dur=1[a2];"
          "[a0][a1]acrossfade=d=1.4[a01];[a01][a2]acrossfade=d=1.0[amb];"
          f"[3:a]atrim=0:{T},asetpts=PTS-STARTPTS,volume=0.22,afade=t=in:d=1.2,afade=t=out:st=16.2:d=2.2[mus];"
          "[4:a]adelay=800|800[n1];[5:a]adelay=5400|5400[n2];[6:a]adelay=12400|12400[n3];"
          "[n1][n2][n3]amix=inputs=3:normalize=0[voz];"
          "[mus][amb][voz]amix=inputs=3:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[au]")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", "v1.mp4", "-i", "v2.mp4", "-i", "v3.mp4", "-i", str(MUSICA),
           "-i", str(AQUI / "assets/n1.mp3"), "-i", str(AQUI / "assets/n2.mp3"), "-i", str(AQUI / "assets/n3.mp3"),
           "-filter_complex", fc, "-map", "[v]", "-map", "[au]", "-t", str(T), "-c:v", "libx264", "-preset", "medium",
           "-crf", "19", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", "homenagem.mp4"]
    subprocess.run(cmd, cwd=out, check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "homenagem.mp4", "-vf",
                    "fps=1/2.3,scale=200:-2,tile=8x1", "-frames:v", "1", "folha.jpg"], cwd=out, check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("foto"); ap.add_argument("--nome"); ap.add_argument("--res", default="720p", choices=["720p", "480p"])
    a = ap.parse_args()
    if not KEY:
        sys.exit("Falta a chave do Grok: XAI_API_KEY no .env da Fábrica.")
    foto = pathlib.Path(a.foto).expanduser().resolve()
    slug = a.nome or f"{foto.stem}-{datetime.date.today():%Y%m%d}"
    out = FAB / "saidas" / "homenagem" / slug
    out.mkdir(parents=True, exist_ok=True)
    estado = json.loads((out / "estado.json").read_text(encoding="utf-8")) if (out / "estado.json").exists() else {}
    print(f"Homenagem · {slug} · saída: {out}", flush=True)
    print(f"Custo estimado: ~US$ {0.06 + 20 * PRECO[a.res]:.2f} ({a.res})", flush=True)

    tipo = "png" if foto.suffix.lower() == ".png" else "jpeg"
    dado = f"data:image/{tipo};base64," + base64.b64encode(foto.read_bytes()).decode()
    print("1/3 Imagens", flush=True)
    imagem(estado, "a", P_A, dado, out)
    imagem(estado, "b", P_B, estado["a"], out)
    imagem(estado, "c", P_C, estado["b"], out)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "a.jpg", "-i", "b.jpg", "-i", "c.jpg", "-filter_complex",
                    "[0]scale=300:-2[x];[1]scale=300:-2[y];[2]scale=300:-2[z];[x][y][z]hstack=3", "imagens.jpg"],
                   cwd=out, check=True)

    print("2/3 Animação (3 clipes ao mesmo tempo, 1 a 3 min)", flush=True)
    erros = []
    th = [threading.Thread(target=video, args=(estado, n, i, s, p, a.res, out, erros)) for n, i, s, p in V]
    [t.start() for t in th]; [t.join() for t in th]
    if erros:
        sys.exit("ERRO na animação: " + "; ".join(erros) + " — rode o mesmo comando de novo (o que ficou pronto é pulado).")

    print("3/3 Montagem", flush=True)
    montar(out)
    print(f"PRONTO {out / 'homenagem.mp4'}")
    print(f"GASTO_GROK ~US$ {gasto[0]:.2f} nesta rodada")


if __name__ == "__main__":
    main()
