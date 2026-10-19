"""Markdown checks for Apollo Docs pull requests.

Usage: python tools/docs-checks/check_markdown.py [docs_dir]

Errors (fail the check):
  - front matter missing, or missing title or description
  - heading levels that skip (## straight to ####) or more than one H1
  - images without alt text (![](...) or <img> with no alt)
  - snippet includes whose target is missing or whose line offset starts
    inside the target's front matter (it would render as page text)
Warnings (shown on the PR, do not fail):
  - em dashes in prose and the filler words the style guide bans

Output uses GitHub Actions annotations, so problems show up on the
changed lines in the PR.
"""
import os
import re
import sys

DOCS = sys.argv[1] if len(sys.argv) > 1 else "docs"
FILLER = re.compile(r"\b(simply|seamlessly|powerful)\b", re.I)
errors = warnings = 0


def note(kind, path, line, msg):
    global errors, warnings
    if kind == "error":
        errors += 1
    else:
        warnings += 1
    print(f"::{kind} file={path},line={line}::{msg}")


def front_matter_end(lines):
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return i
    return None


for root, _, files in os.walk(DOCS):
    for name in sorted(files):
        if not name.endswith(".md"):
            continue
        path = os.path.join(root, name)
        is_snippet = "/_snippets" in path.replace(os.sep, "/")
        lines = open(path, encoding="utf-8", errors="replace").read().split("\n")
        end = front_matter_end(lines)

        if not is_snippet:
            if end is None:
                note("error", path, 1, "Missing front matter. Add title: and description: between --- lines.")
            else:
                fm = "\n".join(lines[1:end])
                if not re.search(r"^title:\s*\S", fm, re.M):
                    note("error", path, 1, "Front matter is missing title:.")
                if not re.search(r"^description:\s*\S", fm, re.M):
                    note("error", path, 1, "Front matter is missing description:.")

        start = (end + 1) if end is not None else 0
        fence = None
        last_level = 0
        h1_count = 0
        for n, line in enumerate(lines[start:], start=start + 1):
            m = re.match(r"^\s*(`{3,}|~{3,})", line)
            if m:
                tok = m.group(1)
                if fence is None:
                    fence = tok
                elif tok[0] == fence[0] and len(tok) >= len(fence) and line.strip() == tok:
                    fence = None
                continue
            if fence:
                continue

            h = re.match(r"^(#{1,6})\s", line)
            if h:
                level = len(h.group(1))
                h1_count += level == 1
                if last_level and level > last_level + 1:
                    note("error", path, n, f"Heading jumps from level {last_level} to {level}. Use level {last_level + 1}.")
                last_level = level

            for img in re.finditer(r"!\[\s*\]\(([^)\s]+)", line):
                note("error", path, n, f"Image has no alt text: {img.group(1)}. Describe what it shows inside the brackets.")
            for tag in re.finditer(r"<img\b[^>]*>", line, re.I):
                if not re.search(r'\balt\s*=\s*"[^"]+"', tag.group(0)):
                    note("error", path, n, "<img> tag has no alt text. Add alt=\"...\" describing the image.")

            inc = re.search(r'--8<--\s+"([^":]+)((?::\d*){0,2})"', line)
            if inc:
                target = os.path.join(DOCS, inc.group(1))
                if not os.path.exists(target):
                    note("error", path, n, f"Snippet include target not found: {inc.group(1)}")
                else:
                    tlines = open(target, encoding="utf-8", errors="replace").read().split("\n")
                    tend = front_matter_end(tlines)
                    nums = re.findall(r":(\d*)", inc.group(2))
                    first = int(nums[0]) if nums and nums[0] else 1
                    if tend is not None and first <= tend + 1:
                        note("error", path, n, f"Include starts at line {first}, inside {inc.group(1)}'s front matter (ends at line {tend + 1}). Start at line {tend + 2} or later.")

            if "—" in line and not line.lstrip().startswith("|"):
                note("warning", path, n, "Em dash in prose. The style guide asks for a comma, period, colon, or parentheses instead.")
            if FILLER.search(line):
                note("warning", path, n, f"Filler word '{FILLER.search(line).group(0)}'. The style guide asks to drop it or say what it does.")

        if h1_count > 1:
            note("error", path, 1, f"{h1_count} H1 headings. A page should have one.")

print(f"check_markdown: {errors} error(s), {warnings} warning(s)")
sys.exit(1 if errors else 0)
