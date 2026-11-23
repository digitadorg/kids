"""3 variações agressivas do anúncio de homenagem (estilos 3, 1 e 19), reaproveitando as cenas da amostra.
Uso: python -I fazer.py [v1|v2|v3 ...]   (sem argumento = as três)"""
import base64, json, pathlib, re, subprocess, sys, urllib.request

sys.stdout.reconfigure(encoding="utf-8")
AQUI = pathlib.Path(__file__).resolve().parent
FAB = pathlib.Path.home() / "Fabrica-de-Criativos"
AM = FAB / "acervo/referencias/ad-1649926543212861/amostra"
SONS = FAB / "acervo/sons"
ENV = {l.split("=", 1)[0].strip(): l.split("=", 1)[1].strip().strip('"')
       for l in (FAB / ".env").read_text(encoding="utf-8").splitlines() if "=" in l and not l.lstrip().startswith("#")}
SRC = {"A": AM / "v1-jardim.mp4", "B": AM / "v2-subida.mp4", "C": AM / "v3-abraco.mp4",
       "imgA": AM / "a-jardim.jpg", "imgC": AM / "c-abraco.jpg"}
SFX = {"whoosh": SONS / "03-sons-livres/efeitos/whoosh/whoosh-cinematico-rapido-01.wav",
       "impacto": SONS / "03-sons-livres/efeitos/impacto/impacto-cinematico-grande-01.wav",
       "riser": SONS / "03-sons-livres/efeitos/riser/riser-sintetico-curto-01.wav",
       "hit": SONS / "03-sons-livres/efeitos/hit-cta/hit-batida-coracao-grave-01.wav",
       "fita": SONS / "01-efeitos-hardcopy/analogicos/analogicos-004-audio-track-forward-and-track-back.wav"}

# Cada frase: (texto, [tomadas], palavra gigante ou None, sfx no começo ou None)
# Tomada: (fonte, entrada, saída, zoom, efeito)   efeito: none | flash | antes | split | vhs | bw
VAR = {
 "v1": {"nome": "estilo-3-letreiro", "musica": SONS / "02-trilhas/05-drop-dramatico/Departed__Humblebee.wav", "frases": [
   ("Para de rolar.", [("imgA", 0, 0, 1.25, "bw")], "PARE", "impacto"),
   ("Você ainda tem uma foto de quem partiu?", [("A", 0, 2.5, 1.0, "none"), ("A", 2.5, 5, 1.15, "none")], None, "whoosh"),
   ("Então olha isso.", [("B", 0, 1.8, 1.1, "flash")], None, "whoosh"),
   ("Uma única foto... virou esse momento.", [("B", 1.8, 3.6, 1.0, "none"), ("B", 3.6, 4.6, 1.2, "none")], "UMA FOTO", "impacto"),
   ("Ela sobe. Ela vira. E acena pra você.", [("B", 4.6, 6.6, 1.15, "none")], None, None),
   ("É o adeus que você nunca teve.", [("C", 0, 3, 1.05, "flash")], "ADEUS", "impacto"),
   ("Você só manda a foto. A gente faz o resto.", [("C", 3, 5, 1.2, "none")], None, "riser"),
   ("Toque em Saiba mais agora.", [("imgC", 0, 0, 1.1, "none")], "AGORA", "hit")]},
 "v2": {"nome": "estilo-1-antes-depois", "musica": SONS / "02-trilhas/07-cinematografico-suave/Cloudbreak__Jobii.wav", "frases": [
   ("Isso aqui é só uma foto parada.", [("imgA", 0, 0, 1.0, "antes")], None, "impacto"),
   ("Agora olha a mesma foto... depois.", [("A", 0, 5, 1.0, "split")], None, "whoosh"),
   ("Sorrindo de novo. Acenando pra você.", [("B", 3.4, 6.6, 1.15, "flash")], None, "impacto"),
   ("Não deixa a lembrança de quem você ama presa numa gaveta.", [("B", 6.6, 10, 1.0, "none")], "GAVETA", "whoosh"),
   ("Uma foto vira uma homenagem que a família inteira vai guardar pra sempre.", [("C", 0, 5, 1.1, "flash")], "PRA SEMPRE", "riser"),
   ("Toque em Saiba mais e manda a foto hoje.", [("imgC", 0, 0, 1.15, "none")], "HOJE", "hit")]},
 "v3": {"nome": "estilo-19-documentario", "musica": SONS / "02-trilhas/04-cta-epico/Ascent__Henry_Miles.wav", "frases": [
   ("Lembra desse sorriso?", [("imgA", 0, 0, 1.3, "vhs")], None, "fita"),
   ("Lembra do jeito que ela te olhava?", [("A", 0, 5, 1.2, "vhs")], None, None),
   ("Agora imagina ver isso de novo.", [("B", 0, 2.5, 1.0, "flash")], None, "impacto"),
   ("Ela subindo... virando... e acenando, como quem diz: eu tô bem.", [("B", 2.5, 4.2, 1.1, "none"), ("B", 4.2, 6.6, 1.2, "none")], None, "whoosh"),
   ("Quantas vezes você quis dizer tchau?", [("B", 6.6, 10, 1.05, "bw")], "TCHAU", "impacto"),
   ("Agora você pode. Manda uma foto. Toque em Saiba mais.", [("C", 0, 5, 1.1, "flash")], None, "hit")]},
 "v4": {"nome": "estilo-10-quem-perdeu-a-mae", "musica": SONS / "02-trilhas/07-cinematografico-suave/Fade__Ever_So_Blue.wav", "frases": [
   ("Se você perdeu a sua mãe, esse vídeo é pra você.", [("imgA", 0, 0, 1.2, "bw")], "MÃE", "impacto"),
   ("Ela não senta mais na mesa do domingo.", [("A", 0, 5, 1.1, "bw")], None, "whoosh"),
   ("Mas ela pode sorrir pra você mais uma vez.", [("B", 0, 3.4, 1.0, "flash")], None, "impacto"),
   ("Subir... virar... e acenar, como quem diz: filho, eu tô bem.", [("B", 3.4, 6.6, 1.15, "none")], None, None),
   ("Manda uma foto dela. A gente transforma nessa homenagem.", [("C", 0, 5, 1.05, "flash")], None, "riser"),
   ("Toque em Saiba mais e faz isso por ela.", [("imgC", 0, 0, 1.1, "none")], "POR ELA", "hit")]},
 "v5": {"nome": "estilo-20-tres-passos", "musica": SONS / "02-trilhas/08-corporate-uplifting/Rising__Origo.wav", "frases": [
   ("Como uma foto vira essa homenagem, em três passos.", [("B", 3.4, 6.6, 1.1, "flash")], "3 PASSOS", "impacto"),
   ("Passo um: você manda uma foto de quem partiu.", [("imgA", 0, 0, 1.0, "polaroid")], "1 · FOTO", "whoosh"),
   ("Passo dois: a gente dá vida a ela. Ela sorri.", [("A", 0, 5, 1.05, "flash")], "2 · VIDA", "whoosh"),
   ("Sobe a escada do céu e acena pra você.", [("B", 0, 6.6, 1.0, "none")], None, None),
   ("Passo três: você recebe o vídeo pronto pra mostrar pra família.", [("C", 0, 5, 1.05, "flash")], "3 · PRONTO", "riser"),
   ("Toque em Saiba mais e manda a foto.", [("imgC", 0, 0, 1.1, "none")], None, "hit")]},
 "v6": {"nome": "estilo-18-presente-de-luto", "musica": SONS / "02-trilhas/07-cinematografico-suave/Everything_Is_Working_Out__Sarah_the_Illstrumentalist.wav", "frases": [
   ("Tá sem saber o que dar pra quem tá de luto?", [("imgA", 0, 0, 1.0, "polaroid")], None, "impacto"),
   ("Flor murcha. Mensagem passa.", [("A", 0, 3, 1.1, "bw")], None, "whoosh"),
   ("Mas isso aqui... a pessoa guarda pra sempre.", [("B", 0, 3.4, 1.0, "flash")], "PRA SEMPRE", "impacto"),
   ("A foto de quem partiu, sorrindo e acenando de novo.", [("B", 3.4, 6.6, 1.15, "none")], None, None),
   ("O presente mais bonito que você pode dar.", [("C", 0, 5, 1.05, "flash")], "PRESENTE", "riser"),
   ("Toque em Saiba mais e manda a foto.", [("imgC", 0, 0, 1.1, "none")], None, "hit")]},
 "v7": {"nome": "estilo-4-plantao", "musica": SONS / "02-trilhas/01-tensao-dark/One_Step_Away__Dian_Shuai.wav", "extra": "plantao", "frases": [
   ("Atenção. Essa é a notícia que ninguém quer receber.", [("imgA", 0, 0, 1.15, "bw")], "URGENTE", "impacto"),
   ("Um dia, a última foto vai ser só isso: uma foto.", [("A", 0, 5, 1.1, "bw")], None, "whoosh"),
   ("Mas ela ainda pode sorrir pra você.", [("B", 0, 3.4, 1.0, "flash")], None, "impacto"),
   ("Subir... virar... e acenar, como quem diz: eu tô bem.", [("B", 3.4, 6.6, 1.15, "none")], None, None),
   ("Imagina a sua família vendo isso no próximo almoço de domingo.", [("C", 0, 5, 1.05, "flash")], None, "riser"),
   ("Toque em Saiba mais antes que essa foto fique esquecida numa gaveta.", [("imgC", 0, 0, 1.1, "none")], "AGORA", "hit")]},
 "v8": {"nome": "estilo-22-hardcopy-noir", "musica": SONS / "02-trilhas/05-drop-dramatico/Exile__Henry_Miles.wav", "giga_y": 1560, "frases": [
   # narração reaproveitada da V3 (cota do ElevenLabs acabou)
   ("Lembra desse sorriso?", [("imgA", 0, 0, 1.2, "noir")], "SAUDADE", "impacto"),
   ("Lembra do jeito que ela te olhava?", [("A", 0, 5, 1.15, "noir")], None, "whoosh"),
   ("Agora imagina ver isso de novo.", [("B", 0, 2.5, 1.0, "noirleve")], None, "impacto"),
   ("Ela subindo... virando... e acenando, como quem diz: eu tô bem.", [("B", 2.5, 4.2, 1.1, "noirleve"), ("B", 4.2, 6.6, 1.2, "noirleve")], None, "whoosh"),
   ("Quantas vezes você quis dizer tchau?", [("imgA", 0, 0, 1.35, "noir")], "TCHAU", "impacto"),
   ("Agora você pode. Manda uma foto. Toque em Saiba mais.", [("C", 0, 5, 1.05, "noirleve")], "AGORA", "hit")]},
 "v9": {"nome": "estilo-34-dossie-documental", "musica": SONS / "02-trilhas/01-tensao-dark/Out_There__Out_To_The_World.wav", "extra": "dossie", "frases": [
   # narração reaproveitada da V4 (cota do ElevenLabs acabou)
   ("Se você perdeu a sua mãe, esse vídeo é pra você.", [("imgA", 0, 0, 1.0, "preto")], None, "fita"),
   ("Ela não senta mais na mesa do domingo.", [("imgA", 0, 0, 1.0, "polaroidpb")], None, "impacto"),
   ("Mas ela pode sorrir pra você mais uma vez.", [("A", 0, 5, 1.1, "flash")], None, "impacto"),
   ("Subir... virar... e acenar, como quem diz: filho, eu tô bem.", [("B", 2.4, 6.6, 1.1, "none")], None, "whoosh"),
   ("Manda uma foto dela. A gente transforma nessa homenagem.", [("C", 0, 5, 1.08, "flash")], "O ABRAÇO", "riser"),
   ("Toque em Saiba mais e faz isso por ela.", [("imgC", 0, 0, 1.1, "none")], "POR ELA", "hit")]},
}
ROTULO_ESTILO = {"v7": "Estilo 4 · Plantão", "v8": "Estilo 22 · Hard Copy noir", "v9": "Estilo 34 · Dossiê documental", "v1": "Estilo 3 · Letreiro", "v2": "Estilo 1 · Antes e depois", "v3": "Estilo 19 · Documentário",
                 "v4": "Estilo 10 · Por quem você perdeu", "v5": "Estilo 20 · Didático em 3 passos",
                 "v6": "Estilo 18 · Colagem / presente"}


ETAPAS = ["copy", "voz", "cortes", "legenda", "mix", "pronto"]


def marca(chave, etapa, **extra):
    """Atualiza estado.json, que o Space (space.html) lê a cada 2 s."""
    p = AQUI / "estado.json"
    try:
        est = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        est = {}
    v = est.setdefault(chave, {"nome": VAR[chave]["nome"], "copy": [f[0] for f in VAR[chave]["frases"]]})
    v["estilo"] = ROTULO_ESTILO.get(chave, "")
    v["etapa"] = etapa
    v.update(extra)
    p.write_text(json.dumps(est, ensure_ascii=False, indent=1), encoding="utf-8")


def sh(args, cwd=None):
    # tempo máximo: se o ffmpeg travar, para e avisa (nunca fica parado em silêncio)
    subprocess.run(args, cwd=cwd, check=True, timeout=240)


def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                                capture_output=True, text=True).stdout.strip())


def narrar(texto, out):
    mp3, js = out / "voz.mp3", out / "voz.json"
    if mp3.exists() and js.exists():
        return json.loads(js.read_text(encoding="utf-8"))
    body = {"text": texto, "model_id": "eleven_multilingual_v2",
            "voice_settings": {"stability": 0.4, "similarity_boost": 0.8, "style": 0.5, "speed": 1.02}}
    req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{ENV['ELEVENLABS_VOICE_ID']}/with-timestamps",
                                 data=json.dumps(body).encode(), method="POST",
                                 headers={"xi-api-key": ENV["ELEVENLABS_API_KEY"], "Content-Type": "application/json"})
    r = json.load(urllib.request.urlopen(req, timeout=180))
    mp3.write_bytes(base64.b64decode(r["audio_base64"]))
    al = r["alignment"]
    js.write_text(json.dumps(al), encoding="utf-8")
    return al


def palavras(al):
    ch, st, en = al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]
    out, cur = [], None
    for i, c in enumerate(ch):
        if c.isspace():
            if cur: out.append(cur); cur = None
            continue
        if cur is None: cur = {"w": "", "s": st[i], "e": en[i], "i": i}
        cur["w"] += c; cur["e"] = en[i]
    if cur: out.append(cur)
    return out


def tomada(fonte, ent, sai, zoom, fx, d, arq):
    W, H = 1080, 1920
    zw, zh = int(W * zoom) // 2 * 2, int(H * zoom) // 2 * 2
    base = f"scale={zw}:{zh}:force_original_aspect_ratio=increase,crop={W}:{H}"
    if fonte.startswith("img"):
        frames = int(d * 30) + 1
        vf = (f"scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,"
              f"zoompan=z='{zoom}+0.12*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s={W}x{H}:fps=30")
        inp = ["-loop", "1", "-t", f"{d:.3f}", "-i", str(SRC[fonte])]
    else:
        disp = sai - ent
        fator = max(d / disp, 0.5)
        lento = min(fator, 2.2)
        vf = f"trim={ent}:{sai},setpts=(PTS-STARTPTS)*{lento:.4f},{base},fps=30"
        if fator > 2.2:
            vf += f",tpad=stop_mode=clone:stop_duration={d - disp * 2.2 + 0.1:.3f}"
        inp = ["-i", str(SRC[fonte])]
    if fx == "flash":
        vf += ",fade=t=in:st=0:d=0.18:color=white"
    elif fx == "bw":
        vf += ",hue=s=0,eq=contrast=1.15"
    elif fx == "vhs":
        vf += (",curves=preset=vintage,noise=alls=22:allf=t,rgbashift=rh=6:bh=-6,"
               "drawgrid=w=iw:h=4:t=1:c=black@0.25,vignette=PI/4")
    elif fx == "antes":
        vf += ",hue=s=0.35,eq=brightness=-0.04"
    elif fx in ("noir", "noirleve"):  # Hard Copy noir: imagem escura em cima, degradê para o preto embaixo
        s = "0.15" if fx == "noir" else "0.75"
        vf += (f",eq=brightness=-0.06:contrast=1.25:saturation={s},vignette=PI/3.5,"
               "drawbox=y=ih*0.60:w=iw:h=ih*0.40:c=black@0.55:t=fill,drawbox=y=ih*0.70:w=iw:h=ih*0.30:c=black@0.75:t=fill")
    elif fx == "preto":  # cartão preto com grão (data digitada vem na legenda)
        sh(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i",
            f"color=c=0x0d0d0d:s=1080x1920:d={d:.3f}:r=30,noise=alls=18:allf=t,vignette=PI/4,format=yuv420p",
            "-t", f"{d:.3f}", "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", str(arq)])
        return
    elif fx == "polaroidpb":  # foto P&B recortada sobre fundo escuro, com carimbo
        frames = int(d * 30) + 1
        fc = (f"[0:v]scale=760:-2,hue=s=0,eq=contrast=1.2,pad=iw+60:ih+200:30:30:0xEEEEEE,format=rgba,"
              f"rotate=0.05:c=none:ow=rotw(0.05):oh=roth(0.05)[p];"
              f"color=c=0x1a1714:s=1080x1920:d={d:.3f}:r=30,noise=alls=16:allf=t[bg];"
              f"[bg][p]overlay=x=(W-w)/2:y=(H-h)/2-110:shortest=1,vignette=PI/4,"
              f"zoompan=z='1+0.05*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,format=yuv420p")
        sh(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-t", f"{d:.3f}", "-i", str(SRC[fonte]),
            "-filter_complex", fc, "-t", f"{d:.3f}", "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", str(arq)])
        return
    elif fx == "polaroid":  # foto com borda branca, torta, sobre papel kraft (colagem)
        frames = int(d * 30) + 1
        fc = (f"[0:v]scale=760:-2,pad=iw+60:ih+200:30:30:white,format=rgba,rotate=-0.06:c=none:ow=rotw(-0.06):oh=roth(-0.06)[p];"
              f"color=c=0xC8A27A:s=1080x1920:d={d:.3f}:r=30,noise=alls=14:allf=t[bg];"
              f"[bg][p]overlay=x=(W-w)/2:y=(H-h)/2-90:shortest=1,"
              f"zoompan=z='1+0.06*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,format=yuv420p")
        sh(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-t", f"{d:.3f}", "-i", str(SRC[fonte]),
            "-filter_complex", fc, "-t", f"{d:.3f}", "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", str(arq)])
        return
    elif fx == "split":
        img = str(SRC["imgA"]).replace("\\", "/").replace(":", "\\:")
        vf = (f"[0:v]trim={ent}:{sai},setpts=(PTS-STARTPTS)*{max(d / (sai - ent), 0.5):.4f},"
              f"scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:960:0:300,fps=30[bx];"
              f"movie='{img}',loop=-1:1,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:960:0:300,"
              f"hue=s=0.35,fps=30,trim=0:{d:.3f},setpts=PTS-STARTPTS[tp];[tp][bx]vstack,drawbox=y=957:w=iw:h=6:c=white:t=fill")
        sh(["ffmpeg", "-y", "-loglevel", "error", *inp, "-filter_complex", vf, "-t", f"{d:.3f}", "-an",
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", str(arq)])
        return
    vf += ",format=yuv420p,setsar=1"
    sh(["ffmpeg", "-y", "-loglevel", "error", *inp, "-vf", vf, "-t", f"{d:.3f}", "-an", "-r", "30",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", str(arq)])


def ass_tempo(t):
    h, r = divmod(max(t, 0), 3600); m, s = divmod(r, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"


def extras(tipo, frases_t, fim):
    """Camadas fixas de cada estilo, desenhadas na legenda (ASS)."""
    E = []
    if tipo == "plantao":  # tarja URGENTE, manchete e letreiro correndo
        E.append(f"Dialogue: 4,{ass_tempo(0)},{ass_tempo(fim - 2.7)},Tarja,,0,0,0,,{{\\an7\\pos(48,150)}} URGENTE ")
        E.append(f"Dialogue: 4,{ass_tempo(0.4)},{ass_tempo(fim - 2.7)},Manchete,,0,0,0,,"
                 "{\\an1\\q2\\pos(40,1590)\\fad(200,0)} FOTO DE QUEM PARTIU GANHA VIDA ")
        tick = "MANDA A FOTO   ●   ELA SORRI   ●   ELA ACENA   ●   A FAMÍLIA SE EMOCIONA   ●   TOQUE EM SAIBA MAIS   ●   "
        E.append(f"Dialogue: 4,{ass_tempo(0)},{ass_tempo(fim - 2.7)},Ticker,,0,0,0,,"
                 f"{{\\an4\\q2\\move(1080,1668,-2600,1668)}}{tick * 2}")
    elif tipo == "dossie":  # data digitada letra a letra no cartão preto
        ini, fimf = frases_t[0]
        data = "12 DE MARÇO"
        passo = min(0.09, (fimf - ini - 0.6) / len(data))
        for k in range(1, len(data) + 1):
            E.append(f"Dialogue: 4,{ass_tempo(ini + 0.2 + k * passo)},{ass_tempo(ini + 0.2 + (k + 1) * passo if k < len(data) else fimf)},"
                     f"Data,,0,0,0,,{{\\an5\\pos(540,760)}}{data[:k]}{'_' if k < len(data) else ''}")
        E.append(f"Dialogue: 4,{ass_tempo(frases_t[1][0] + 0.5)},{ass_tempo(frases_t[1][1])},Carimbo,,0,0,0,,"
                 "{\\an5\\pos(560,880)\\frz12\\fscx170\\fscy170\\t(0,120,\\fscx100\\fscy100)} SEM DESPEDIDA ")
    return E


def legenda(ws, frases_t, gigantes, rotulos, fim, out, giga_y=700, extra=None):
    L = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "WrapStyle: 0", "",
         "[V4+ Styles]",
         "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, "
         "StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
         "Style: Leg,Arial Black,74,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,7,3,2,60,60,560,1",
         "Style: Giga,Impact,210,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,2,0,1,10,0,5,40,40,0,1",
         "Style: Rot,Arial Black,70,&H00000000,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,1,0,0,0,100,100,2,0,3,18,0,8,40,40,220,1",
         "Style: Cta,Arial Black,78,&H00000000,&H00000000,&H0000D4FF,&H0000D4FF,1,0,0,0,100,100,0,0,3,26,0,2,40,40,330,1",
         "Style: Tarja,Arial Black,64,&H00FFFFFF,&H00FFFFFF,&H001E1ED8,&H001E1ED8,1,0,0,0,100,100,3,0,3,16,0,7,0,0,0,1",
         "Style: Manchete,Arial Black,44,&H00FFFFFF,&H00FFFFFF,&H001E1ED8,&H001E1ED8,1,0,0,0,100,100,0,0,3,18,0,1,0,0,0,1",
         "Style: Ticker,Arial Black,42,&H00000000,&H00000000,&H00FFFFFF,&H00FFFFFF,1,0,0,0,100,100,1,0,3,14,0,4,0,0,0,1",
         "Style: Data,Courier New,120,&H00F0F0F0,&H00F0F0F0,&H00000000,&H00000000,1,0,0,0,100,100,6,0,1,0,0,5,0,0,0,1",
         "Style: Carimbo,Impact,110,&H001C1CE0,&H001C1CE0,&H00FFFFFF,&H00000000,1,0,0,0,100,100,4,0,1,5,0,5,0,0,0,1",
         "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    grupos, g = [], []
    for w in ws:
        g.append(w)
        if len(g) == 3 or re.search(r"[.?!:,]$", w["w"]):
            grupos.append(g); g = []
    if g: grupos.append(g)
    for gi, g in enumerate(grupos):
        prox = grupos[gi + 1][0]["s"] if gi + 1 < len(grupos) else g[-1]["e"] + 0.4
        for k, w in enumerate(g):
            fimw = g[k + 1]["s"] if k + 1 < len(g) else min(prox, w["e"] + 0.6)
            txt = " ".join(("{\\c&H00D4FF&\\fscx112\\fscy112}" + x["w"].upper() + "{\\r}") if j == k else x["w"].upper()
                           for j, x in enumerate(g))
            pop = "{\\fad(0,0)\\t(0,80,\\fscx104\\fscy104)\\t(80,160,\\fscx100\\fscy100)}" if k == 0 else ""
            L.append(f"Dialogue: 1,{ass_tempo(w['s'])},{ass_tempo(fimw)},Leg,,0,0,0,,{pop}{txt}")
    for (ini, fimf), giga in zip(frases_t, gigantes):
        if giga:
            L.append(f"Dialogue: 2,{ass_tempo(ini)},{ass_tempo(min(ini + 1.3, fimf))},Giga,,0,0,0,,"
                     f"{{\\an5\\pos(540,{giga_y})\\fscx160\\fscy160\\t(0,140,\\fscx100\\fscy100)\\fad(0,150)}}" + giga)
    L += extras(extra, frases_t, fim)
    for ini, fimr, txt in rotulos:
        L.append(f"Dialogue: 2,{ass_tempo(ini)},{ass_tempo(fimr)},Rot,,0,0,0,,{txt}")
    L.append(f"Dialogue: 3,{ass_tempo(fim - 2.6)},{ass_tempo(fim)},Cta,,0,0,0,,"
             "{\\t(0,300,\\fscx108\\fscy108)\\t(300,600,\\fscx100\\fscy100)\\t(600,900,\\fscx108\\fscy108)\\t(900,1200,\\fscx100\\fscy100)}"
             "TOQUE EM SAIBA MAIS ↓")
    (out / "legenda.ass").write_text("\n".join(L), encoding="utf-8-sig")


def fazer(chave):
    cfg = VAR[chave]
    out = AQUI / chave
    out.mkdir(exist_ok=True)
    textos = [f[0] for f in cfg["frases"]]
    texto = " ".join(textos)
    sem_voz = cfg.get("sem_voz") or "--sem-voz" in sys.argv
    if sem_voz:  # sem narração: cada palavra entra no ritmo de leitura, trilha mais alta
        marca(chave, "voz", agora="Sem narração: texto no tempo de leitura")
        ws, t, pos = [], 0.3, 0
        for frase in textos:
            base = texto.index(frase, pos); pos = base + len(frase)
            for m in re.finditer(r"\S+", frase):
                d = 0.30 + 0.035 * len(m.group())
                ws.append({"w": m.group(), "s": t, "e": t + d, "i": base + m.start()}); t += d
            t += 0.9  # respiro entre as frases
        sh(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono", "-t", f"{t:.2f}",
            "-c:a", "libmp3lame", "voz.mp3"], cwd=out)
        cfg["vol_musica"] = 0.5
    else:
        marca(chave, "voz", agora="Gravando a narração no ElevenLabs")
        ws = palavras(narrar(texto, out))
    marca(chave, "cortes", agora="Cortando as cenas no ritmo da " + ("leitura" if sem_voz else "voz"))
    # início de cada frase = início da 1ª palavra cujo índice >= offset da frase
    offs, pos = [], 0
    for t in textos:
        offs.append(texto.index(t, pos)); pos = offs[-1] + len(t)
    inicios = [next(w["s"] for w in ws if w["i"] >= o) for o in offs]
    total = dur(out / "voz.mp3") + 1.8
    PRE = 0.25
    marcas = [0.0] + [s + PRE for s in inicios[1:]] + [total + PRE]
    frases_t = list(zip(marcas[:-1], marcas[1:]))
    lista, sfx_t = [], []
    n = 0
    for (ini, fim), (txt, tomadas, giga, sfx) in zip(frases_t, cfg["frases"]):
        dtotal = fim - ini
        pesos = [max(t[2] - t[1], 1.0) for t in tomadas]
        for t, p in zip(tomadas, pesos):
            d = dtotal * p / sum(pesos)
            n += 1; arq = out / f"s{n:02d}.mp4"
            tomada(*t, d, arq); lista.append(arq.name)
        if sfx: sfx_t.append((sfx, ini))
    (out / "lista.txt").write_text("".join(f"file '{x}'\n" for x in lista), encoding="utf-8")
    sh(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", "lista.txt", "-c", "copy", "base.mp4"], cwd=out)
    fim_v = dur(out / "base.mp4")
    ws_off = [{**w, "s": w["s"] + PRE, "e": w["e"] + PRE} for w in ws]
    rot = [(0, frases_t[0][1], "ANTES"), (frases_t[1][0], frases_t[1][1], "ANTES  ↑   ↓  DEPOIS")] if chave == "v2" else \
          [(0, frases_t[1][1], "1987")] if chave == "v3" else []
    marca(chave, "legenda", agora="Legenda palavra a palavra e palavras gigantes")
    legenda(ws_off, frases_t, [f[2] for f in cfg["frases"]], rot, fim_v, out,
            giga_y=cfg.get("giga_y", 700), extra=cfg.get("extra"))
    marca(chave, "mix", agora="Juntando voz, trilha e efeitos sonoros (-14 LUFS)")
    # 1) áudio sozinho (num comando só com o vídeo, o ffmpeg travava no fim)
    ins = ["-i", "voz.mp3", "-i", str(cfg["musica"])]
    fc = [f"[0:a]adelay={int(PRE*1000)}|{int(PRE*1000)}[voz]",
          f"[1:a]atrim=0:{fim_v:.2f},asetpts=PTS-STARTPTS,volume={cfg.get("vol_musica", 0.2)},afade=t=in:d=0.6,afade=t=out:st={fim_v-1.5:.2f}:d=1.5[mus]"]
    mix = ["[mus]", "[voz]"]
    for k, (nome, t) in enumerate(sfx_t):
        ins += ["-i", str(SFX[nome])]
        ms = int(max(t - (0.35 if nome == "riser" else 0.05), 0) * 1000)
        fc.append(f"[{2+k}:a]volume={0.55 if nome != 'riser' else 0.4},adelay={ms}|{ms}[x{k}]"); mix.append(f"[x{k}]")
    fc.append("".join(mix) + f"amix=inputs={len(mix)}:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11")
    sh(["ffmpeg", "-y", "-loglevel", "error", *ins, "-filter_complex", ";".join(fc), "-t", f"{fim_v:.2f}",
        "-ar", "48000", "mix.wav"], cwd=out)
    # 2) vídeo com a legenda queimada + o áudio pronto
    final = AQUI / f"homenagem-{chave}-{cfg['nome']}.mp4"
    sh(["ffmpeg", "-y", "-loglevel", "error", "-i", "base.mp4", "-i", "mix.wav", "-vf", "subtitles=legenda.ass",
        "-map", "0:v", "-map", "1:a", "-shortest", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(final)], cwd=out)
    sh(["ffmpeg", "-y", "-loglevel", "error", "-i", str(final), "-vf", "fps=1/1.6,scale=160:-2,tile=8x2", "-frames:v", "1",
        str(AQUI / f"folha-{chave}.jpg")])
    marca(chave, "pronto", agora=f"Pronto · {fim_v:.1f} s", video=final.name, folha=f"folha-{chave}.jpg")
    print(f"PRONTO {final.name} · {fim_v:.1f} s · {len(texto)} caracteres de voz", flush=True)


for c in (sys.argv[1:] or ["v1", "v2", "v3"]):
    try:
        fazer(c)
    except Exception as e:
        marca(c, "erro", agora=f"ERRO: {type(e).__name__} — o Claude vai corrigir")
        print(f"ERRO {c}: {e}", flush=True)
