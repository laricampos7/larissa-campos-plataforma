# -*- coding: utf-8 -*-
"""Post de feed (1080x1350) com depoimento real transcrito, sem identificar a aluna."""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
BG = (11, 11, 14)
BRAND = (255, 25, 64)
LIGHT = (255, 92, 122)
WHITE = (245, 246, 248)
GRAY = (150, 152, 160)
CARD = (245, 246, 248)
INK = (24, 24, 28)
INKSOFT = (90, 92, 100)

FONTS = r"C:\Windows\Fonts"
def F(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)
black = lambda s: F("ariblk.ttf", s)
bold  = lambda s: F("arialbd.ttf", s)
reg   = lambda s: F("arial.ttf", s)
ital  = lambda s: F("ariali.ttf", s)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# brilho vermelho no topo
glow = Image.new("RGB", (W, H), BG)
gd = ImageDraw.Draw(glow)
for i in range(190):
    a = i / 190
    c = (int(BG[0] + (BRAND[0]-BG[0]) * (1-a) * 0.30),
         int(BG[1] + (BRAND[1]-BG[1]) * (1-a) * 0.30),
         int(BG[2] + (BRAND[2]-BG[2]) * (1-a) * 0.30))
    gd.line([(0, i*2), (W, i*2)], fill=c)
img = Image.blend(img, glow, 0.6)
d = ImageDraw.Draw(img)

def center(y, text, font, fill, ls=0):
    if ls:
        total = sum(d.textbbox((0,0), ch, font=font)[2] + ls for ch in text) - ls
        x = (W - total) / 2
        for ch in text:
            d.text((x, y), ch, font=font, fill=fill)
            x += d.textbbox((0,0), ch, font=font)[2] + ls
    else:
        w = d.textbbox((0,0), text, font=font)[2]
        d.text(((W - w)/2, y), text, font=font, fill=fill)

def wrap(text, font, max_w):
    words = text.split(); lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if d.textlength(test, font=font) <= max_w: cur = test
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

center(70, "DEPOIMENTO REAL DE ALUNA", bold(26), LIGHT, ls=7)
center(120, "O QUE ELAS ACHAM", black(52), WHITE)
center(188, "DA PLATAFORMA", black(52), BRAND)
center(280, "★ ★ ★ ★ ★", F("seguisym.ttf", 40), BRAND)

cx0, cx1 = 60, 1020
cy0, cy1 = 350, 1180
d.rounded_rectangle([cx0, cy0, cx1, cy1], radius=36, fill=CARD)
d.text((cx0 + 40, cy0 + 5), "“", font=black(110), fill=BRAND)

quote = ("Estou adorando o treino com o novo aplicativo. Facilitou minha vida, "
         "pois é muito útil para transmissão das aulas e para que a professora "
         "acompanhe meus treinos diariamente. Desse modo é possível detalhar a "
         "rotina de exercícios, cargas, dificuldades e pontos para aperfeiçoamento, "
         "e me sinto motivada para ir melhorando, sem que o treinamento caia na "
         "rotina. Apesar do pouco tempo de uso, já sinto mudanças no meu corpo e "
         "quero continuar para atingir os meus objetivos.")

qf = reg(34)
inner = cx1 - cx0 - 100
lines = wrap(quote, qf, inner)
ty = cy0 + 130
lh = 46
for ln in lines:
    d.text((cx0 + 50, ty), ln, font=qf, fill=INK)
    ty += lh

att = "Lara, aluna da plataforma"
af = ital(28)
aw = d.textlength(att, font=af)
d.text((cx1 - 50 - aw, cy1 - 60), att, font=af, fill=INKSOFT)

center(1230, "@trainer_larissacampos", bold(36), WHITE)
center(1285, "Larissa de Campos  ·  Consultoria Esportiva  ·  CREF 076634-G/RJ", reg(22), GRAY)

out_dir = r"C:\Users\Larissa\Desktop\MINHA PLATAFORMA\02 - MARKETING\STORIES PRA POSTAR HOJE"
os.makedirs(out_dir, exist_ok=True)
out = os.path.join(out_dir, "POST FEED - Depoimento Lara.jpg")
img.convert("RGB").save(out, "JPEG", quality=95)
print("Salvo em:", out)
