# -*- coding: utf-8 -*-
"""Story de captação (gancho + CTA), sem depender de print/depoimento, na marca da Larissa."""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
BG = (11, 11, 14)        # #0b0b0e
BRAND = (255, 25, 64)    # #FF1940
LIGHT = (255, 92, 122)   # #FF5C7A
WHITE = (245, 246, 248)  # #f5f6f8
GRAY = (150, 152, 160)

FONTS = r"C:\Windows\Fonts"
def F(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)

black = lambda s: F("ariblk.ttf", s)   # Arial Black
bold  = lambda s: F("arialbd.ttf", s)
reg   = lambda s: F("arial.ttf", s)

img = Image.new("RGB", (W, H), BG)

# ---- fundo: brilho vermelho diagonal no topo ----
glow = Image.new("RGB", (W, H), BG)
gd = ImageDraw.Draw(glow)
for i in range(260):
    a = i / 260
    c = (int(BG[0] + (BRAND[0]-BG[0]) * (1-a) * 0.30),
         int(BG[1] + (BRAND[1]-BG[1]) * (1-a) * 0.30),
         int(BG[2] + (BRAND[2]-BG[2]) * (1-a) * 0.30))
    gd.line([(0, i*2), (W, i*2)], fill=c)
img = Image.blend(img, glow, 0.6)
d = ImageDraw.Draw(img)

def center(y, text, font, fill, ls=0):
    if ls:
        total = sum((d.textbbox((0,0), ch, font=font)[2]) + ls for ch in text) - ls
        x = (W - total) / 2
        for ch in text:
            d.text((x, y), ch, font=font, fill=fill)
            x += d.textbbox((0,0), ch, font=font)[2] + ls
    else:
        w = d.textbbox((0,0), text, font=font)[2]
        d.text(((W - w)/2, y), text, font=font, fill=fill)

# ---- kicker ----
center(210, "CONSULTORIA ESPORTIVA ONLINE", bold(30), LIGHT, ls=7)

# ---- headline (o gancho na dor) ----
center(280, "CANSADA DE", black(88), WHITE)
center(374, "COMEÇAR", black(88), WHITE)
center(468, "E PARAR?", black(88), BRAND)

# ---- linha divisória fina ----
d.line([(340, 610), (740, 610)], fill=(255,255,255,40), width=2)

# ---- promessa ----
center(660, "SUA MELHOR VERSÃO", bold(46), WHITE)
center(720, "COMEÇA AQUI", black(52), LIGHT)

# ---- painel de credenciais ----
px0, px1, py0, py1 = 90, 990, 840, 1230
d.rounded_rectangle([px0, py0, px1, py1], radius=32, outline=(255,255,255,50), width=2)

rows = [
    ("20", "anos de prática"),
    ("10", "anos de formada"),
    ("+100", "alunas treinadas"),
]
col_w = (px1 - px0) // 3
for i, (num, label) in enumerate(rows):
    cx = px0 + col_w * i + col_w // 2
    nw = d.textbbox((0,0), num, font=black(58))[2]
    d.text((cx - nw/2, py0 + 60), num, font=black(58), fill=BRAND)
    # label pode quebrar em 2 linhas
    words = label.split(" ")
    line1, line2 = words[0], " ".join(words[1:])
    lw1 = d.textbbox((0,0), line1, font=reg(24))[2]
    d.text((cx - lw1/2, py0 + 140), line1, font=reg(24), fill=GRAY)
    if line2:
        lw2 = d.textbbox((0,0), line2, font=reg(24))[2]
        d.text((cx - lw2/2, py0 + 172), line2, font=reg(24), fill=GRAY)
if len(rows) > 1:
    d.line([(px0 + col_w, py0+55), (px0 + col_w, py1-45)], fill=(255,255,255,30), width=1)
    d.line([(px0 + col_w*2, py0+55), (px0 + col_w*2, py1-45)], fill=(255,255,255,30), width=1)

# ---- diferencial ----
center(1290, "Treino 100% online, acompanhado", reg(32), WHITE)
center(1335, "em tempo real pelo seu app", reg(32), WHITE)

# ---- CTA ----
center(1430, "Vagas abertas essa semana", bold(36), LIGHT)
bx0, bx1, by0, by1 = 140, 940, 1490, 1592
d.rounded_rectangle([bx0, by0, bx1, by1], radius=51, fill=BRAND)
btn = "CHAMA NO WHATSAPP"
bw = d.textbbox((0,0), btn, font=black(42))[2]
d.text(((W-bw)/2, by0 + 30), btn, font=black(42), fill=WHITE)

# ---- rodapé ----
center(1720, "@trainer_larissacampos", bold(40), WHITE)
center(1780, "Larissa de Campos  ·  Consultoria Esportiva", reg(28), GRAY)
center(1820, "CREF 076634-G/RJ", reg(28), GRAY)

out_dir = r"C:\Users\Larissa\Desktop\MINHA PLATAFORMA\02 - MARKETING\STORIES PRA POSTAR HOJE"
os.makedirs(out_dir, exist_ok=True)
out = os.path.join(out_dir, "STORY - Chamada Novos Clientes.png")
img.save(out, "PNG")
print("Salvo em:", out)
