"""Check internal links, anchors, and images in the built Apollo Docs site.

Usage: mkdocs build -d site && python tools/docs-checks/check_links.py site docs

MkDocs only validates links written as .md files. The wiki uses site-style
links (../page/, https://wiki.apolloautomation.com/...), so this checks every
link, #anchor, image, and video in page content against the built site.
Filename case must match exactly, because GitHub Pages is case-sensitive.
Fails on any broken link, missing anchor, or image without alt text. Also
fails when the build lost something without saying so:
- images: a page that should have images has none, or the site has less
  than 90% of the images its Markdown (with snippet includes expanded) has.
  In October 2026, selectolax 1.0.1 made mkdocs-glightbox drop every image.
- stylesheets, scripts, and menu links that point at missing files
- redirects in mkdocs.yml whose page wasn't generated (missing target)
"""
import os, re, sys, posixpath
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

SITE = sys.argv[1] if len(sys.argv) > 1 else "site"
DOCS = sys.argv[2] if len(sys.argv) > 2 else "docs"
OWN_HOSTS = {"wiki.apolloautomation.com"}


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.refs, self.site_refs = set(), [], []
        self.in_article, self.stack = False, 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and "name" in a:
            self.ids.add(a["name"])
        if tag == "article" and "md-content__inner" in (a.get("class") or ""):
            self.in_article, self.stack = True, 0
        if tag == "link" and "stylesheet" in (a.get("rel") or "") and a.get("href"):
            self.site_refs.append(("stylesheet", a["href"]))
        elif tag == "script" and a.get("src"):
            self.site_refs.append(("script", a["src"]))
        elif tag == "a" and "md-nav__link" in (a.get("class") or "") and a.get("href"):
            self.site_refs.append(("menu link", a["href"]))
        if not self.in_article:
            return
        if tag == "article":
            self.stack += 1
        if tag == "a" and a.get("href") is not None and "headerlink" not in (a.get("class") or ""):
            self.refs.append(("a", a["href"], None))
        elif tag == "img":
            self.refs.append(("img", a.get("src", ""), a.get("alt")))
        elif tag in ("video", "source", "audio") and a.get("src"):
            self.refs.append((tag, a["src"], None))
        if tag == "video" and a.get("poster"):
            self.refs.append(("poster", a["poster"], None))

    def handle_endtag(self, tag):
        if self.in_article and tag == "article":
            self.stack -= 1
            if self.stack <= 0:
                self.in_article = False


ALL = set()
for r, _, fs in os.walk(SITE):
    for f in fs:
        ALL.add("/" + os.path.relpath(os.path.join(r, f), SITE).replace(os.sep, "/"))
LOWER = {f.lower(): f for f in ALL}

pages = {}
for f in ALL:
    if not f.endswith(".html") or f.startswith(("/assets/", "/search/")) or f == "/404.html":
        continue
    html = open(SITE + f, encoding="utf-8", errors="replace").read()
    if 'http-equiv="refresh"' in html[:2000] and "md-content" not in html:
        continue
    p = Page()
    p.feed(html)
    pages[f] = p


def resolve(base, ref):
    sp = urlsplit(ref)
    if sp.scheme in ("mailto", "tel", "javascript", "data"):
        return None
    if sp.scheme in ("http", "https"):
        if sp.netloc.lower() not in OWN_HOSTS:
            return None
        path = sp.path or "/"
    elif sp.scheme or sp.netloc:
        return None
    elif not sp.path:
        return base, unquote(sp.fragment)
    elif sp.path.startswith("/"):
        path = sp.path
    else:
        path = posixpath.normpath(posixpath.join(posixpath.dirname(base), sp.path))
        if sp.path.endswith("/") and not path.endswith("/"):
            path += "/"
    return unquote(path), unquote(sp.fragment)


case_mismatch = []


def exists(path):
    p = "/" + path.lstrip("/")
    cands = [p + "index.html"] if p.endswith("/") else [p, p + "/index.html"]
    for c in cands:
        if c in ALL:
            return c
    for c in cands:
        if c.lower() in LOWER:
            case_mismatch.append((path, LOWER[c.lower()]))
    return None


def src_md(url):
    rel = url.lstrip("/")
    rel = rel[: -len("/index.html")] if rel.endswith("/index.html") else rel
    for cand in (rel + ".md", rel + "/index.md"):
        if os.path.isfile(os.path.join(DOCS, cand)):
            return "docs/" + cand
    return "?" + url


broken, bad_anchor, missing_alt = [], [], []
for url, pr in pages.items():
    for kind, ref, alt in pr.refs:
        if kind == "img" and (alt is None or not alt.strip()):
            missing_alt.append({"page": src_md(url), "src": ref})
        r = resolve(url, ref)
        if r is None:
            continue
        path, frag = r
        t = exists(path)
        if not t:
            broken.append({"page": src_md(url), "kind": kind, "ref": ref})
            continue
        if frag and kind == "a" and t in pages and frag not in pages[t].ids:
            bad_anchor.append({"page": src_md(url), "ref": ref})

# Stylesheets, scripts, and menu links are on every page, so report each once.
broken_site = {}
for url, pr in pages.items():
    for kind, ref in pr.site_refs:
        r = resolve(url, ref)
        if r is not None and not exists(r[0]):
            broken_site.setdefault((kind, r[0]), src_md(url))


# Images the Markdown should produce, with --8<-- snippet includes expanded
# and fenced code blocks skipped.
INCLUDE = re.compile(r'^\s*--8<--\s+"([^"]+)"\s*$')
FENCE = re.compile(r"^\s*(```|~~~)")
IMAGE = re.compile(r"!\[[^\]]*\]\(|<img\s", re.I)


def expand(rel, start=None, end=None, depth=0):
    path = os.path.join(DOCS, rel)
    if depth > 10 or not os.path.isfile(path):
        return []
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    lines = lines[(start - 1 if start else 0):(end if end else None)]
    out = []
    for line in lines:
        m = INCLUDE.match(line)
        if not m:
            out.append(line)
            continue
        parts = m.group(1).split(":")
        s = int(parts[1]) if len(parts) > 1 and parts[1] else None
        e = int(parts[2]) if len(parts) > 2 and parts[2] else None
        out.extend(expand(parts[0], s, e, depth + 1))
    return out


def expected_images(rel):
    n, fenced = 0, False
    for line in expand(rel):
        if FENCE.match(line):
            fenced = not fenced
        elif not fenced:
            n += len(IMAGE.findall(line))
    return n


expected_total = built_total = 0
pages_without_images = []
for url, pr in pages.items():
    src = src_md(url)
    if not src.startswith("docs/"):
        continue
    want = expected_images(src[len("docs/"):])
    got = sum(1 for kind, _, _ in pr.refs if kind == "img")
    expected_total += want
    built_total += got
    if want and not got:
        pages_without_images.append((src, want))
images_dropped = expected_total > 0 and built_total < 0.9 * expected_total

# Redirect pages that mkdocs-redirects didn't generate (it skips missing targets).
missing_redirects = []
if os.path.isfile("mkdocs.yml"):
    in_maps = False
    for line in open("mkdocs.yml", encoding="utf-8").read().splitlines():
        if line.strip().startswith("redirect_maps:"):
            in_maps, indent = True, len(line) - len(line.lstrip())
            continue
        if in_maps:
            if line.strip() and not line.strip().startswith("#") and len(line) - len(line.lstrip()) <= indent:
                break
            m = re.match(r"""\s*['"]?([^'":]+\.md)['"]?\s*:""", line)
            if m:
                key = m.group(1)
                page = key[: -len("index.md")] if key.endswith("index.md") else key[:-3] + "/"
                if ("/" + page + "index.html").replace("//", "/") not in ALL:
                    missing_redirects.append(key)

for b in broken:
    print(f"::error file={b['page']}::Broken {b['kind']} link: {b['ref']}")
for a in bad_anchor:
    print(f"::error file={a['page']}::Link to a missing #anchor: {a['ref']}")
for m in missing_alt:
    print(f"::error file={m['page']}::Image without alt text: {m['src']}")
for (kind, path), page in sorted(broken_site.items()):
    print(f"::error file=mkdocs.yml::Broken {kind} on every page (first seen on {page}): {path}")
for src, want in pages_without_images:
    print(f"::error file={src}::The Markdown has {want} image(s), but the built page has none.")
if images_dropped:
    print(f"::error::The built site has {built_total} images, but the Markdown should produce about {expected_total}. A build plugin is probably removing images; check recently updated packages.")
for key in missing_redirects:
    print(f"::error file=mkdocs.yml::The redirect for {key} wasn't generated. Its target page is probably missing.")
for wrong, right in sorted(set(case_mismatch)):
    print(f"::error::Link case doesn't match the file (GitHub Pages is case-sensitive): {wrong} should be {right}")
total = (len(broken) + len(bad_anchor) + len(missing_alt) + len(set(case_mismatch)) + len(broken_site)
         + len(pages_without_images) + images_dropped + len(missing_redirects))
print(f"check_links: {len(pages)} pages, {built_total} of {expected_total} expected images, {len(broken)} broken, "
      f"{len(bad_anchor)} bad anchors, {len(missing_alt)} missing alt, {len(set(case_mismatch))} case mismatches, "
      f"{len(broken_site)} broken stylesheets/scripts/menu links, {len(pages_without_images)} pages missing images, "
      f"{len(missing_redirects)} missing redirects")
sys.exit(1 if total else 0)
