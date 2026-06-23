# -*- coding: utf-8 -*-
"""Gera um template de Story (1080x1920) pra depoimento/print de aluna, na marca da Larissa."""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
BG = (11, 11, 14)        # #0b0b0e
PANEL = (21, 21, 26)     # leve destaque do frame
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
d = ImageDraw.Draw(img)

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
        # com espaçamento entre letras
        total = sum((d.textbbox((0,0), ch, font=font)[2]) + ls for ch in text) - ls
        x = (W - total) / 2
        for ch in text:
            d.text((x, y), ch, font=font, fill=fill)
            x += d.textbbox((0,0), ch, font=font)[2] + ls
    else:
        w = d.textbbox((0,0), text, font=font)[2]
        d.text(((W - w)/2, y), text, font=font, fill=fill)

# ---- kicker ----
center(150, "MINHA PLATAFORMA DE TREINO", bold(30), LIGHT, ls=8)

# ---- headline ----
center(220, "O QUE MINHAS", black(82), WHITE)
center(310, "ALUNAS ESTÃO", black(82), WHITE)
center(400, "ACHANDO", black(82), BRAND)

# ---- estrelas ----
center(530, "★ ★ ★ ★ ★", F("seguisym.ttf", 46), BRAND)

# ---- frame pro print ----
fx0, fy0, fx1, fy1 = 90, 640, 990, 1380
d.rounded_rectangle([fx0, fy0, fx1, fy1], radius=40, fill=PANEL, outline=BRAND, width=5)
# texto guia dentro do frame
cy = (fy0 + fy1) // 2
center(cy - 90, "COLE AQUI O PRINT", bold(40), WHITE)
center(cy - 30, "da mensagem da sua aluna", reg(34), GRAY)
center(cy + 40, "(lembre de borrar o nome dela)", reg(30), GRAY)

# ---- CTA ----
center(1470, "Quer um acompanhamento assim?", bold(38), WHITE)
# botão
bx0, bx1, by0, by1 = 190, 890, 1540, 1640
d.rounded_rectangle([bx0, by0, bx1, by1], radius=50, fill=BRAND)
btn = "VEM TREINAR COMIGO"
bw = d.textbbox((0,0), btn, font=black(40))[2]
d.text(((W-bw)/2, by0 + 28), btn, font=black(40), fill=WHITE)

# ---- rodapé ----
center(1740, "@trainer_larissacampos", bold(40), WHITE)
center(1800, "Larissa de Campos  ·  Consultoria Esportiva", reg(28), GRAY)
center(1840, "CREF 076634-G/RJ", reg(28), GRAY)

out_dir = r"C:\Users\Larissa\Desktop\MINHA PLATAFORMA\02 - MARKETING\STORIES PRA POSTAR HOJE"
os.makedirs(out_dir, exist_ok=True)
out = os.path.join(out_dir, "STORY - O que as alunas acham.png")
img.save(out, "PNG")
print("Salvo em:", out)
