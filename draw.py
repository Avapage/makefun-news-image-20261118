#!/usr/bin/env python3
"""Draw the 18 November 2026 world-news front page (1024x1024 PNG). v2.

Stories (all reported 18 Nov 2026):
  HERO  Shenzhen: Xi meets Putin at APEC; Trump lands for US-China-Russia talks
  1     Gulf: Iran drones target US bases in Kuwait/Bahrain; US strikes Qeshm Island
  2     Ukraine: 141 Russian drones overnight, 126 downed, six hurt in Dnipro
  3     Alaska: Peltola flips Senate seat; Democrats 56-44; first Alaska Native senator
  4     Health: US loses measles elimination status after 26 years
"""
import math

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (244, 239, 228)
INK = (20, 24, 31)
RED = (193, 39, 45)
GOLD = (232, 177, 14)
WHITE = (250, 248, 242)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FS = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def text_w(d, s, f):
    return d.textbbox((0, 0), s, font=f)[2]


def fit(d, s, path, size, max_w):
    while size > 10 and text_w(d, s, font(path, size)) > max_w:
        size -= 2
    return font(path, size)


def center(d, cx, y, s, f, fill):
    d.text((cx - text_w(d, s, f) / 2, y), s, font=f, fill=fill)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img, "RGBA")

# ---------------- masthead ----------------
d.rectangle([0, 0, W, 8], fill=INK)
center(d, W // 2, 20, "T H E   W O R L D   I N   O N E   I M A G E", font(FB, 27), INK)
fdate = fit(d, "WEDNESDAY 18 NOVEMBER 2026", FS, 56, 980)
center(d, W // 2, 52, "WEDNESDAY 18 NOVEMBER 2026", fdate, RED)
d.rectangle([24, 122, W - 24, 128], fill=INK)

# ---------------- hero: Shenzhen summit ----------------
HX0, HY0, HX1, HY1 = 24, 142, 1000, 516
d.rectangle([HX0, HY0, HX1, HY1], fill=(18, 38, 66))
d.ellipse([412, 162, 612, 362], fill=GOLD)
d.ellipse([432, 182, 592, 342], fill=(240, 196, 60))
# ground line the flags stand on
d.rectangle([HX0 + 30, 330, HX1 - 30, 336], fill=(120, 150, 190))


def flag(x, kind):
    d.rectangle([x, 190, x + 6, 332], fill=WHITE)
    if kind == "cn":
        d.rectangle([x + 6, 190, x + 96, 250], fill=(222, 41, 16))
        d.ellipse([x + 16, 200, x + 30, 214], fill=GOLD)
        for (sx, sy) in [(40, 198), (44, 210), (40, 222)]:
            d.ellipse([x + sx, sy, x + sx + 6, sy + 6], fill=GOLD)
    elif kind == "ru":
        d.rectangle([x + 6, 190, x + 96, 210], fill=(245, 245, 245))
        d.rectangle([x + 6, 210, x + 96, 230], fill=(0, 57, 166))
        d.rectangle([x + 6, 230, x + 96, 250], fill=(213, 43, 30))
    else:
        for i in range(6):
            col = (178, 34, 52) if i % 2 == 0 else (245, 245, 245)
            d.rectangle([x + 6, 190 + i * 10, x + 96, 200 + i * 10], fill=col)
        d.rectangle([x + 6, 190, x + 46, 222], fill=(10, 49, 97))


flag(150, "cn")
flag(466, "ru")
flag(782, "us")
d.rectangle([HX0, 356, HX1, HY1], fill=(10, 20, 36, 242))
fh = fit(d, "THREE POWERS MEET IN SHENZHEN", FB, 63, 940)
center(d, W // 2, 368, "THREE POWERS MEET IN SHENZHEN", fh, WHITE)
cap = "Xi hosts Putin at APEC  •  Trump lands for first US–China–Russia talks"
center(d, W // 2, 450, cap, fit(d, cap, FR, 27, 940), (255, 224, 150))
d.rectangle([HX0, HY0, HX1, HY1], outline=INK, width=3)

# ---------------- panels ----------------
PW, PH = 482, 208
ART = 74  # art strip height at top of each panel


def panel(x0, y0, bg):
    d.rectangle([x0, y0, x0 + PW, y0 + PH], fill=bg)
    d.rectangle([x0, y0, x0 + PW, y0 + PH], outline=INK, width=3)
    return x0, y0


def panel_text(x0, y0, line1, line2, caption, head_fill=WHITE, cap_fill=(235, 232, 222)):
    inner = PW - 28
    f1 = fit(d, line1, FB, 40, inner)
    d.text((x0 + 14, y0 + ART + 6), line1, font=f1, fill=head_fill)
    f2 = fit(d, line2, FB, 40, inner)
    d.text((x0 + 14, y0 + ART + 52), line2, font=f2, fill=head_fill)
    fc = fit(d, caption, FR, 24, inner)
    d.text((x0 + 14, y0 + ART + 100), caption, font=fc, fill=cap_fill)


def drone(cx, cy, s, col=(12, 16, 24)):
    d.polygon([(cx - 24 * s, cy), (cx + 24 * s, cy), (cx + 9 * s, cy + 11 * s),
               (cx - 9 * s, cy + 11 * s)], fill=col)
    d.rectangle([cx - 3 * s, cy - 7 * s, cx + 3 * s, cy], fill=col)


# Panel 1: Gulf drones (top-left)
x0, y0 = panel(24, 530, (122, 32, 24))
for (cx, cy, s) in [(110, 552, 1.0), (225, 544, 0.8), (330, 554, 0.9)]:
    drone(x0 + cx - 24, y0 + cy - 530, s, col=(25, 22, 20))
for r in (30, 48, 66):
    d.arc([x0 + 408 - r, y0 + 62 - r, x0 + 408 + r, y0 + 62 + r], start=180, end=305,
          fill=(255, 200, 90), width=5)
d.polygon([(x0 + 384, y0 + 40), (x0 + 432, y0 + 40), (x0 + 408, y0 + 12)], fill=(255, 200, 90))
panel_text(x0, y0, "IRAN DRONES HIT", "AT US GULF BASES",
           "Kuwait & Bahrain intercept; US hits Qeshm")

# Panel 2: Ukraine drones (top-right)
x0, y0 = panel(518, 530, (24, 62, 110))
d.rectangle([x0, y0 + PH - 40, x0 + PW, y0 + PH], fill=(214, 164, 10))
for i in range(6):
    drone(x0 + 52 + i * 62, y0 + 26, 0.75, col=(10, 16, 26))
cx, cy = x0 + 408, y0 + 38
for k in range(8):
    a = k * math.pi / 4
    d.line([cx, cy, cx + 30 * math.cos(a), cy + 30 * math.sin(a)], fill=(255, 170, 40), width=6)
d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=(255, 120, 30))
panel_text(x0, y0, "141 DRONES OVER", "UKRAINE IN ONE NIGHT",
           "Kyiv downs 126; six hurt in Dnipro", cap_fill=(235, 232, 222))

# Panel 3: Alaska Senate (bottom-left)
x0, y0 = panel(24, 752, (28, 44, 84))
d.polygon([(x0 + 36, y0 + 66), (x0 + 196, y0 + 66), (x0 + 184, y0 + 48), (x0 + 48, y0 + 48)],
          fill=(226, 230, 238))
d.pieslice([x0 + 70, y0 - 6, x0 + 162, y0 + 78], 180, 360, fill=(226, 230, 238))
d.rectangle([x0 + 111, y0 + 0, x0 + 121, y0 + 10], fill=(226, 230, 238))
d.ellipse([x0 + 109, y0 - 4, x0 + 123, y0 + 4], fill=GOLD)
for i in range(4):  # dome ribs
    d.line([x0 + 116, y0 + 8, x0 + 84 + i * 22, y0 + 62], fill=(170, 178, 196), width=3)
d.text((x0 + 226, y0 + 4), "56–44", font=font(FB, 62), fill=GOLD)
panel_text(x0, y0, "PELTOLA FLIPS ALASKA", "SENATE SEAT",
           "First Alaska Native senator; Dems' 9th flip")

# Panel 4: measles (bottom-right)
x0, y0 = panel(518, 752, (238, 231, 214))


def virus(cx, cy, r):
    for k in range(10):
        a = k * math.pi / 5
        x2, y2 = cx + (r + 10) * math.cos(a), cy + (r + 10) * math.sin(a)
        d.line([cx, cy, x2, y2], fill=RED, width=5)
        d.ellipse([x2 - 5, y2 - 5, x2 + 5, y2 + 5], fill=RED)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=RED)
    for (sx, sy) in [(-0.35, -0.2), (0.3, 0.25), (0.05, -0.45)]:
        d.ellipse([cx + sx * r - 5, cy + sy * r - 5, cx + sx * r + 5, cy + sy * r + 5],
                  fill=(244, 200, 200))


virus(x0 + 70, y0 + 38, 20)
virus(x0 + 140, y0 + 30, 14)
virus(x0 + 196, y0 + 44, 10)
d.text((x0 + 246, y0 + 16), "5,412 CASES", font=fit(d, "5,412 CASES", FB, 34, PW - 260), fill=RED)
panel_text(x0, y0, "US LOSES MEASLES-", "FREE STATUS",
           "Held for 26 years; worst toll since 1991",
           head_fill=INK, cap_fill=(70, 60, 50))

# ---------------- footer ----------------
d.rectangle([24, 974, W - 24, 978], fill=INK)
center(d, W // 2, 986, "18 NOVEMBER 2026  •  FIVE STORIES  •  ONE DAY", font(FB, 25), INK)

img.save("/home/hatch/workspace/agent-gigs/makefun/newsimg-20261118-entry/entry.png", optimize=True)
print("saved A v2")
