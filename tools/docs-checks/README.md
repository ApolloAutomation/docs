# Docs checks

These scripts run on every pull request into `dev` or `main`
(`.github/workflows/docs-checks.yml`). Problems show up as comments on the
changed lines in the PR. Fix them and push again; the checks re-run.

They run again before every deploy to the live wiki
(`.github/workflows/ci.yml`), and the deploy publishes the same build the
link check looked at. If any check fails, nothing is published, the live wiki
stays as it was, and the team gets a Discord alert. This catches problems
that appear between the PR and the deploy, such as a build package update
that drops images or breaks links. The build itself also fails if a
`--8<--` snippet include points at a missing file (`check_paths` in
`mkdocs.yml`).

| Check | Fails the PR on | How to fix |
| --- | --- | --- |
| `check_markdown.py` | Missing front matter `title:` or `description:`, heading levels that skip (`##` to `####`), more than one `#` H1, images without alt text, snippet includes that point at a missing file or start inside the included page's front matter | Add the field, use the next heading level, describe the image inside `![...]`, or start the include after the included page's closing `---` |
| `check_secrets.py` | ESPHome API encryption keys, generated OTA passwords, passwords typed into YAML, and access tokens | Use `!secret` (or a placeholder like `your-wifi-password`). If the value was real, change it on the device or account too |
| `check_images.py` | Photos with GPS location data (phones add it by default) | `exiftool -gps:all= -overwrite_original docs/assets/<file>` |
| `check_links.py` | Broken links, links to a missing `#anchor`, filename case mismatches (GitHub Pages is case-sensitive), and images without alt text, checked on the built site. Also stylesheets, scripts, and menu links that point at missing files, redirects in `mkdocs.yml` whose target is missing, and images the build dropped: a page that should have images but has none, or a site with less than 90% of the images its Markdown should produce | Fix the link target or anchor; match the file name's case exactly. If images went missing, look for a recently updated build package and pin it in `requirements.txt` |

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
