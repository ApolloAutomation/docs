"""Build DEV board pinout diagrams from boards.json.

Tags follow boardgen's label style (https://github.com/kuba2k2/boardgen): 15 degree
skewed blocks, Consolas text, dark ink on light fills and white ink on dark ones.

Usage: python make_pinout.py [board ...]
Renders docs/assets/apollo-<board>-pinout.webp with headless Chrome or Edge. Needs Pillow.
"""
import base64
import colorsys
import json
import math
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

HERE = Path(__file__).parent
ASSETS = HERE.parent.parent / "docs" / "assets"

COLORS = {
    "power":  "#CD3C24",
    "ground": "#000000",
    "gpio":   "#4A7FC1",
    "adc":    "#8AD039",
    "i2c":    "#FF9955",
    "uart":   "#DCD4EE",
    "spi":    "#C2629A",
    "led":    "#C8C8C8",
}
LEGEND = [("power", "Power"), ("ground", "Ground"), ("gpio", "GPIO"), ("adc", "ADC"),
          ("i2c", "I2C"), ("uart", "UART"), ("spi", "SPI")]

TAG_W = 116
TAG_H = 50
TAG_GAP = 6
SKEW = 15          # degrees, same as boardgen
LEAD = 60          # leader line length from board edge
LINE_GAP = 14      # space between leader line and first tag
MARGIN = 30
MONO = "Consolas, 'DejaVu Sans Mono', monospace"
SANS = "Arial, 'Helvetica Neue', sans-serif"


def ink(fill):
    r, g, b = (int(fill[i:i + 2], 16) / 255 for i in (1, 3, 5))
    return "#423F42" if colorsys.rgb_to_hls(r, g, b)[1] > 0.5 else "#FFFFFF"


def tag_width(text):
    return max(TAG_W, 26 + 17 * len(text))


def tag(x, y, kind, text):
    fill = COLORS[kind]
    w = tag_width(text)
    shift = TAG_H * math.tan(math.radians(SKEW)) / 2
    top = y - TAG_H / 2
    return (w, f'<g transform="translate({x + shift:.1f},{top:.1f})"><rect width="{w}" height="{TAG_H}" '
               f'rx="5" fill="{fill}" transform="skewX(-{SKEW})"/></g>'
               f'<text x="{x + w / 2:.1f}" y="{y:.1f}" fill="{ink(fill)}" font-family="{MONO}" font-size="30" '
               f'text-anchor="middle" dominant-baseline="central">{text}</text>')


def row(tags):
    return [t.split(":", 1) for t in tags]


def row_width(tags):
    return sum(tag_width(t) for _, t in row(tags)) + TAG_GAP * (len(tags) - 1)


def build(name, b):
    photo = HERE / b["photo"]
    pw, ph = Image.open(photo).size
    data = base64.b64encode(photo.read_bytes()).decode()

    left_w = max(row_width(r) for r in b["pins"]["left"])
    right_w = max(row_width(r) for r in b["pins"]["right"] + [b["led"]["tags"]])
    bx = MARGIN + left_w + LINE_GAP + LEAD
    by = MARGIN
    width = bx + pw + LEAD + LINE_GAP + right_w + MARGIN
    legend_y = by + ph + 55
    height = legend_y + 40

    lines, tags = [], []

    def draw_row(side, py, px, entries, dashed=False):
        dash = ' stroke-dasharray="10 6"' if dashed else ""
        if side == "left":
            x = bx - LEAD
            lines.append(f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{x:.1f}" y2="{py:.1f}" stroke="#555" stroke-width="5"{dash}/>')
            x -= LINE_GAP
            for kind, text in row(entries):
                x -= tag_width(text)
                tags.append(tag(x, py, kind, text)[1])
                x -= TAG_GAP
        else:
            x = bx + pw + LEAD
            lines.append(f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{x:.1f}" y2="{py:.1f}" stroke="#555" stroke-width="5"{dash}/>')
            x += LINE_GAP
            for kind, text in row(entries):
                w, svg = tag(x, py, kind, text)
                tags.append(svg)
                x += w + TAG_GAP

    for side in ("left", "right"):
        geo = b[side]
        for i, entries in enumerate(b["pins"][side]):
            draw_row(side, by + geo["y0"] + geo["pitch"] * i, bx + geo["x"], entries)
    led = b["led"]
    draw_row("right", by + led["y"], bx + led["x"], led["tags"])

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.0f}" height="{height:.0f}" '
           f'viewBox="0 0 {width:.0f} {height:.0f}">',
           '<rect width="100%" height="100%" fill="#ffffff"/>',
           *lines,
           # board goes over the leader lines so they appear to run out from under each pad
           f'<image x="{bx}" y="{by}" width="{pw}" height="{ph}" href="data:image/png;base64,{data}"/>',
           *tags]

    items = [(kind, label, 30 + 10 + 14 * len(label) + 34) for kind, label in LEGEND]
    x = (width - (sum(w for *_, w in items) - 34)) / 2
    for kind, label, w in items:
        out.append(f'<rect x="{x:.1f}" y="{legend_y - 13}" width="30" height="26" rx="5" fill="{COLORS[kind]}"/>')
        out.append(f'<text x="{x + 40:.1f}" y="{legend_y}" font-family="{SANS}" font-size="24" fill="#333" '
                   f'dominant-baseline="central">{label}</text>')
        x += w
    out.append("</svg>")

    svg_path = HERE / f"{name}-pinout.svg"
    svg_path.write_text("\n".join(out), encoding="utf-8")
    return svg_path, int(round(width)), int(round(height))


def render(name, svg_path, w, h):
    browser = next((p for p in (
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        shutil.which("chromium"), shutil.which("google-chrome"),
    ) if p and Path(p).exists()), None)
    if not browser:
        sys.exit("no Chrome/Edge found to render the SVG")
    with tempfile.TemporaryDirectory() as tmp:
        png = Path(tmp) / "pinout.png"
        subprocess.run([browser, "--headless", "--disable-gpu", "--hide-scrollbars",
                        f"--window-size={w},{h}", f"--screenshot={png}", svg_path.resolve().as_uri()],
                       check=True, capture_output=True)
        # WebP, not PNG: CI shrinks every PNG to 750px wide, which blurs the labels
        webp = ASSETS / f"apollo-{name}-pinout.webp"
        Image.open(png).save(webp, quality=90, method=6)
    svg_path.unlink()
    print("wrote", webp)


if __name__ == "__main__":
    boards = json.loads((HERE / "boards.json").read_text(encoding="utf-8"))
    for name in sys.argv[1:] or boards:
        render(name, *build(name, boards[name]))
