# -*- coding: utf-8 -*-
"""Encaixa o print real do WhatsApp (depoimento da Lara) numa arte da marca, Story e Feed."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BG = (11, 11, 14)
BRAND = (255, 25, 64)
LIGHT = (255, 92, 122)
WHITE = (245, 246, 248)
GRAY = (150, 152, 160)

FONTS = r"C:\Windows\Fonts"
def F(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)
black = lambda s: F("ariblk.ttf", s)
bold  = lambda s: F("arialbd.ttf", s)
reg   = lambda s: F("arial.ttf", s)

PRINT = r"C:\Users\Larissa\Downloads\WhatsApp Image 2026-06-23 at 16.33.03.jpeg"

def make_bg(W, H, glow_lines):
    img = Image.new("RGB", (W, H), BG)
    glow = Image.new("RGB", (W, H), BG)
    gd = ImageDraw.Draw(glow)
    for i in range(glow_lines):
        a = i / glow_lines
        c = (int(BG[0] + (BRAND[0]-BG[0]) * (1-a) * 0.30),
             int(BG[1] + (BRAND[1]-BG[1]) * (1-a) * 0.30),
             int(BG[2] + (BRAND[2]-BG[2]) * (1-a) * 0.30))
        gd.line([(0, i*2), (W, i*2)], fill=c)
    return Image.blend(img, glow, 0.6).convert("RGBA")

def center(d, W, y, text, font, fill, ls=0):
    if ls:
        total = sum(d.textbbox((0,0), ch, font=font)[2] + ls for ch in text) - ls
        x = (W - total) / 2
        for ch in text:
            d.text((x, y), ch, font=font, fill=fill)
            x += d.textbbox((0,0), ch, font=font)[2] + ls
    else:
        w = d.textbbox((0,0), text, font=font)[2]
        d.text(((W - w)/2, y), text, font=font, fill=fill)

def rounded(im, rad):
    im = im.convert("RGBA")
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, im.size[0]-1, im.size[1]-1], radius=rad, fill=255)
    im.putalpha(mask)
    return im

def place_print(canvas, region_top, region_bottom, max_w, rad=36):
    """Escala o print pra caber na regiao e cola centralizado com sombra."""
    W = canvas.size[0]
    p = Image.open(PRINT)
    pw, ph = p.size
    rh = region_bottom - region_top
    scale = min(max_w / pw, rh / ph)
    nw, nh = int(pw * scale), int(ph * scale)
    p = p.resize((nw, nh), Image.LANCZOS)
    p = rounded(p, rad)
    x = (W - nw) // 2
    y = region_top + (rh - nh) // 2
    # sombra
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle([x, y+10, x+nw, y+nh+10], radius=rad, fill=(0, 0, 0, 150))
    shadow = shadow.filter(ImageFilter.GaussianBlur(22))
    canvas.alpha_composite(shadow)
    # borda clara fina
    border = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(border).rounded_rectangle([x-3, y-3, x+nw+3, y+nh+3], radius=rad+3,
                                             outline=(255, 255, 255, 60), width=3)
    canvas.alpha_composite(border)
    canvas.alpha_composite(p, (x, y))

def build(W, H, glow_lines, head_y, head_size, footer, out_name):
    canvas = make_bg(W, H, glow_lines)
    d = ImageDraw.Draw(canvas)
    # cabecalho
    center(d, W, head_y[0], "PROVA REAL  ·  SEM EDIÇÃO", bold(int(head_size*0.5)), LIGHT, ls=6)
    center(d, W, head_y[1], "O QUE A LARA", black(head_size), WHITE)
    center(d, W, head_y[2], "ACHOU DO APP", black(head_size), BRAND)
    # regiao do print
    place_print(canvas, footer["print_top"], footer["print_bottom"], int(W*0.86))
    # rodape
    if footer.get("cta"):
        center(d, W, footer["cta_y"], "Quer um acompanhamento assim?", bold(36), WHITE)
        bx0, bx1, by0, by1 = (W-700)//2, (W+700)//2, footer["btn_y"], footer["btn_y"]+98
        d.rounded_rectangle([bx0, by0, bx1, by1], radius=49, fill=BRAND)
        btn = "VEM TREINAR COMIGO"
        bw = d.textlength(btn, font=black(38))
        d.text(((W-bw)/2, by0 + 28), btn, font=black(38), fill=WHITE)
    center(d, W, footer["handle_y"], "@trainer_larissacampos", bold(36), WHITE)
    center(d, W, footer["cref_y"], "Larissa de Campos  ·  CREF 076634-G/RJ", reg(24), GRAY)

    out_dir = r"C:\Users\Larissa\Desktop\MINHA PLATAFORMA\02 - MARKETING\STORIES PRA POSTAR HOJE"
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, out_name)
    canvas.convert("RGB").save(out, "JPEG", quality=95)
    print("Salvo em:", out)

# STORY 1080x1920
build(1080, 1920, 260,
      head_y=(120, 175, 248), head_size=66,
      footer={"print_top": 360, "print_bottom": 1560,
              "cta": True, "cta_y": 1600, "btn_y": 1670,
              "handle_y": 1800, "cref_y": 1856},
      out_name="STORY - Print Lara.jpg")

# FEED 1080x1350
build(1080, 1350, 190,
      head_y=(70, 120, 188), head_size=56,
      footer={"print_top": 270, "print_bottom": 1170,
              "cta": False,
              "handle_y": 1240, "cref_y": 1292},
      out_name="POST FEED - Print Lara.jpg")
