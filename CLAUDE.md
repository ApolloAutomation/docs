# Claude Code instructions for Apollo Docs

When working in this repository, read [STYLE_GUIDE.md](STYLE_GUIDE.md)
before writing or editing any page content. It is the source of truth
for tone, language, terminology, and formatting on
[wiki.apolloautomation.com](https://wiki.apolloautomation.com).

For workflow (branching, previewing, opening PRs), see
[CONTRIBUTING.md](CONTRIBUTING.md). Key points:

- All edits target the **`dev`** branch, never `main`.
- Maintainers merge `dev → main` to publish to the live wiki.
- Run `mkdocs serve` to preview locally before opening a PR.
- Run `mkdocs build` to catch broken internal links before pushing.

A few of the highest-impact rules from the style guide that AI tools
get wrong most often:

- Product IDs are uppercase with a hyphen: **AIR-1**, **MTR-1**, never
  `Air-1` or `air1`.
- **Apollo addons** (hardware modules) and **Home Assistant apps**
  (formerly add-ons) are different things. Get them right.
- **ESPHome** is the only correct casing.
- No em dashes anywhere.
- Second person, imperative voice for action copy. Wrap numbered steps
  with framing copy (what the reader unlocks, what success looks like).

Read the full guide before making non-trivial changes.
