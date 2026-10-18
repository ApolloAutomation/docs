"""Check internal links, anchors, and images in the built Apollo Docs site.

Usage: mkdocs build -d site && python tools/docs-checks/check_links.py site docs

MkDocs only validates links written as .md files. The wiki uses site-style
links (../page/, https://wiki.apolloautomation.com/...), so this checks every
link, #anchor, image, and video in page content against the built site.
Filename case must match exactly, because GitHub Pages is case-sensitive.
Fails on any broken link, missing anchor, or image without alt text.
"""
import os, sys, posixpath
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

SITE = sys.argv[1] if len(sys.argv) > 1 else "site"
DOCS = sys.argv[2] if len(sys.argv) > 2 else "docs"
OWN_HOSTS = {"wiki.apolloautomation.com"}


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.refs = set(), []
        self.in_article, self.stack = False, 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and "name" in a:
            self.ids.add(a["name"])
        if tag == "article" and "md-content__inner" in (a.get("class") or ""):
            self.in_article, self.stack = True, 0
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

for b in broken:
    print(f"::error file={b['page']}::Broken {b['kind']} link: {b['ref']}")
for a in bad_anchor:
    print(f"::error file={a['page']}::Link to a missing #anchor: {a['ref']}")
for m in missing_alt:
    print(f"::error file={m['page']}::Image without alt text: {m['src']}")
for wrong, right in sorted(set(case_mismatch)):
    print(f"::error::Link case doesn't match the file (GitHub Pages is case-sensitive): {wrong} should be {right}")
total = len(broken) + len(bad_anchor) + len(missing_alt) + len(set(case_mismatch))
print(f"check_links: {len(pages)} pages, {len(broken)} broken, {len(bad_anchor)} bad anchors, {len(missing_alt)} missing alt, {len(set(case_mismatch))} case mismatches")
sys.exit(1 if total else 0)
