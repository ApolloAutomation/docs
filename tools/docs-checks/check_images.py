"""Image checks for Apollo Docs pull requests.

Usage: python tools/docs-checks/check_images.py [assets_dir]

Fails on: photos that carry GPS location metadata (phones add it by
default, and it publishes where the photo was taken).
Warns on: images over 1.5 MB, which slow pages down. Set CHANGED_FILES
(newline-separated paths) to limit this warning to the files a PR changes.

Needs exiftool (apt install libimage-exiftool-perl, brew install exiftool).
To fix a GPS error:  exiftool -gps:all= -overwrite_original <file>
"""
import os
import shutil
import subprocess
import sys

ASSETS = sys.argv[1] if len(sys.argv) > 1 else "docs/assets"
EXTS = (".jpg", ".jpeg", ".png", ".webp", ".heic", ".tif", ".tiff")
LIMIT = 1.5 * 1024 * 1024

if not shutil.which("exiftool"):
    print("::error::exiftool is not installed, so GPS metadata can't be checked.")
    sys.exit(1)

r = subprocess.run(
    ["exiftool", "-q", "-q", "-r", "-if", "$GPSLatitude or $GPSLongitude", "-p", "$Directory/$FileName",
     *sum((["-ext", e.lstrip(".")] for e in EXTS), []), ASSETS],
    capture_output=True, text=True,
)
gps = [l for l in r.stdout.splitlines() if l.strip()]
for path in gps:
    print(f"::error file={path}::Photo contains GPS location data. Remove it with: exiftool -gps:all= -overwrite_original \"{path}\"")

changed = os.environ.get("CHANGED_FILES")
only = {os.path.normpath(f) for f in changed.split()} if changed is not None else None
big = 0
for root, _, files in os.walk(ASSETS):
    for name in files:
        p = os.path.join(root, name)
        if only is not None and os.path.normpath(p) not in only:
            continue
        if os.path.getsize(p) > LIMIT and name.lower().endswith(EXTS + (".gif", ".mp4")):
            big += 1
            print(f"::warning file={p}::{os.path.getsize(p) / 1048576:.1f} MB. Consider resizing (750 px wide is plenty for most images) or compressing.")

print(f"check_images: {len(gps)} image(s) with GPS data, {big} large file warning(s)")
sys.exit(1 if gps else 0)
