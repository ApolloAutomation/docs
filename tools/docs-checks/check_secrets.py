"""Scan docs text for credentials that should never be published.

Usage: python tools/docs-checks/check_secrets.py [docs_dir]

Fails on:
  - ESPHome API encryption keys (a 44-character base64 key after key:)
  - OTA passwords that look generated (32 hex characters)
  - Wi-Fi or other passwords typed in YAML instead of !secret
  - common access token formats (GitHub, Slack, AWS, JWT, long bearer tokens)

Placeholders are allowed: !secret references, values containing words like
your/example/password/changeme/xxx, and known public defaults (for example
WLED's own hotspot password). Screenshots can't be scanned automatically;
check those by eye before adding them.
"""
import os
import re
import sys

DOCS = sys.argv[1] if len(sys.argv) > 1 else "docs"
EXTS = (".md", ".html", ".htm", ".yaml", ".yml", ".txt", ".json")
PLACEHOLDER = re.compile(r"(?i)your|example|password|passw|changeme|change_me|placeholder|secret|xxx|<|>|\$\{|_here|abc123|12345678|wled1234")
PATTERNS = [
    ("ESPHome API encryption key", re.compile(r"""\bkey:\s*["']?([A-Za-z0-9+/]{43}=)["']?""")),
    ("generated OTA password", re.compile(r"""\bpassword:\s*["']?([0-9a-f]{32})["']?\s*$""", re.I)),
    ("password typed in YAML", re.compile(r"""^\s*(?:password|ap_password|wifi_password):\s*["']([^"'\n]{6,})["']""", re.I)),
    ("GitHub token", re.compile(r"\b(gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,})\b")),
    ("Slack token", re.compile(r"\b(xox[abposr]-[A-Za-z0-9-]{10,})\b")),
    ("AWS access key", re.compile(r"\b(AKIA[0-9A-Z]{16})\b")),
    ("JSON Web Token", re.compile(r"\b(eyJ[A-Za-z0-9_-]{15,}\.eyJ[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,})")),
    ("bearer token", re.compile(r"(?i)\bbearer\s+([A-Za-z0-9._~+/-]{32,}=*)")),
]

found = 0
for root, _, files in os.walk(DOCS):
    for name in sorted(files):
        if not name.endswith(EXTS):
            continue
        path = os.path.join(root, name)
        for n, line in enumerate(open(path, encoding="utf-8", errors="replace"), 1):
            for label, pat in PATTERNS:
                for m in pat.finditer(line):
                    value = m.group(1)
                    if "!secret" in line or PLACEHOLDER.search(value):
                        continue
                    found += 1
                    shown = value[:4] + "..." if len(value) > 8 else "..."
                    print(f"::error file={path},line={n}::Possible {label} ({shown}). Replace it with !secret or a placeholder, and rotate it if it was real.")

print(f"check_secrets: {found} possible secret(s)")
sys.exit(1 if found else 0)
