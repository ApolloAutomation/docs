"""One-time prep: crop the EasyEDA board renders to the PCB and knock out the background.

Reads renders/apollo-dev-N-image-1.png and writes devN-board.png next to this script,
which make_pinout.py then uses. Only rerun this when a render changes. Needs Pillow.
"""
from pathlib import Path

from PIL import Image, ImageDraw

HERE = Path(__file__).parent

# regions painted over with the module shield's flat white (the EasyEDA logo on DEV-2)
ERASE = {"dev2-board.png": [(398, 438, 526, 488)]}


def is_blue(p):
    r, g, b = p[:3]
    return p[3] > 0 and b > r + 40 and b > g + 20


def prep(src, out):
    im = Image.open(src).convert("RGBA")
    px = im.load()
    w, h = im.size
    # per row, everything between the outermost blue pixels is PCB; median-smoothed
    # over neighbouring rows so edge pads don't notch the outline
    spans = []
    for y in range(h):
        blue = [x for x in range(w) if is_blue(px[x, y])]
        spans.append((blue[0], blue[-1]) if len(blue) > w // 10 else None)
    for y in range(h):
        near = [s for s in spans[max(0, y - 40):y + 41] if s]
        if spans[y] is None or len(near) < 20:
            lo, hi = w, -1
        else:
            lo = sorted(s[0] for s in near)[len(near) // 2] - 2
            hi = sorted(s[1] for s in near)[len(near) // 2] + 2
        for x in range(w):
            if x < lo or x > hi:
                px[x, y] = (0, 0, 0, 0)
    im = im.crop(im.getbbox())
    im = im.resize((round(im.width * 1000 / im.height), 1000), Image.LANCZOS)
    for box in ERASE.get(out, []):
        ImageDraw.Draw(im).rectangle(box, fill=(255, 255, 255, 255))
    im.save(HERE / out)
    print("wrote", out, im.size)


if __name__ == "__main__":
    prep(HERE / "renders" / "apollo-dev-1-image-1.png", "dev1-board.png")
    prep(HERE / "renders" / "apollo-dev-2-image-1.png", "dev2-board.png")
