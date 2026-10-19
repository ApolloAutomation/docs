# Docs checks

These scripts run on every pull request into `dev` or `main`
(`.github/workflows/docs-checks.yml`). Problems show up as comments on the
changed lines in the PR. Fix them and push again; the checks re-run.

| Check | Fails the PR on | How to fix |
| --- | --- | --- |
| `check_markdown.py` | Missing front matter `title:` or `description:`, heading levels that skip (`##` to `####`), more than one `#` H1, images without alt text, snippet includes that point at a missing file or start inside the included page's front matter | Add the field, use the next heading level, describe the image inside `![...]`, or start the include after the included page's closing `---` |
| `check_secrets.py` | ESPHome API encryption keys, generated OTA passwords, passwords typed into YAML, and access tokens | Use `!secret` (or a placeholder like `your-wifi-password`). If the value was real, change it on the device or account too |
| `check_images.py` | Photos with GPS location data (phones add it by default) | `exiftool -gps:all= -overwrite_original docs/assets/<file>` |
| `check_links.py` | Broken links, links to a missing `#anchor`, filename case mismatches (GitHub Pages is case-sensitive), and images without alt text, checked on the built site | Fix the link target or anchor; match the file name's case exactly |

Warnings (shown, but they don't fail the PR): em dashes and the filler words
the style guide bans, and images or recordings over 1.5 MB that the PR adds
or changes.

The checks can't read text inside screenshots or recordings. Before adding
one, look through it for passwords, API keys, email addresses, and other
personal details, and crop or trim them out (see the style guide).

## Run them locally

```bash
pip install -r requirements.txt
python tools/docs-checks/check_markdown.py docs
python tools/docs-checks/check_secrets.py docs
python tools/docs-checks/check_images.py docs/assets
mkdocs build -d site
python tools/docs-checks/check_links.py site docs
```

`check_images.py` needs exiftool (`brew install exiftool` on macOS,
`sudo apt install libimage-exiftool-perl` on Debian or Ubuntu).
