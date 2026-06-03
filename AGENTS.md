# AI agent instructions for Apollo Docs

This file is the canonical instruction set for AI tools (Claude Code,
Cursor, Codex, Copilot, and any other agent that reads `AGENTS.md` from a
repo root) working on the Apollo documentation site at
[wiki.apolloautomation.com](https://wiki.apolloautomation.com).

If you're using Claude Code, `CLAUDE.md` exists as a pointer to this
file. Read this one.

## Before you edit a page

Read [STYLE_GUIDE.md](STYLE_GUIDE.md). It is the source of truth for
tone, language, terminology, voice, and formatting. The style guide is
prescriptive, not advisory.

For workflow (branching, previewing, opening PRs, file layout), see
[CONTRIBUTING.md](CONTRIBUTING.md). Key points:

- All edits target the **`dev`** branch, never `main`.
- Maintainers merge `dev → main` to publish to the live wiki.
- Run `mkdocs serve` to preview locally before opening a PR.
- Run `mkdocs build` to catch broken internal links before pushing.

## High-impact rules AI tools get wrong most often

Read the full style guide, but these are the ones worth checking twice:

- Product IDs are uppercase with a hyphen: **AIR-1**, **MTR-1**, never
  `Air-1` or `air1`.
- **Apollo addons** (hardware modules) and **Home Assistant apps**
  (formerly add-ons) are different things and not interchangeable.
- **ESPHome** is the only correct casing.
- **No em dashes** anywhere in user-facing copy.
- Second person, imperative voice for action copy. Wrap numbered steps
  with framing copy (what the reader unlocks, what success looks like).
- Avoid corporate filler: **simply**, **just**, **easy**, **powerful**,
  **seamlessly**.
- Automation pages must carry a difficulty pill under the H1
  (`<span class="difficulty lvl-N">Difficulty: Level N · Word</span>`,
  Level 1 Starter to Level 5 Pro). On Moderate-and-up pages, add a
  same-product stepping-stone box linking easier automations. Pill and
  box styles live in `docs/stylesheets/extra.css`; never inline colors.
  See [Automation difficulty](STYLE_GUIDE.md#10-automation-difficulty).
- Every page under the ESPHome Starter Kit product (modules, tutorials,
  automations, learn-the-basics, FAQ, start-here, first-steps) must end
  with the community CTA snippet:
  `--8<-- "_snippets/community-help.md"`. To change the CTA copy or
  buttons, edit the snippet file, never the include line on a page.
  See [Community CTA on starter-kit pages](STYLE_GUIDE.md#11-community-cta-on-starter-kit-pages).

## Keep the style guide current

If you notice a recurring pattern that should be standardized but isn't
in `STYLE_GUIDE.md`, surface it to the user before applying it in the
current edit. Examples:

- A new product name or capitalization that isn't covered by the
  naming rules.
- A formatting convention you're about to use repeatedly (a new
  admonition type, a new way of showing CLI output) that future
  contributors should follow.
- A drift between pages where the guide is ambiguous about which
  pattern wins.

Propose the addition to `STYLE_GUIDE.md` in the same PR (or a separate
follow-up if it's substantial). The goal is for the guide to stay ahead
of the docs, not behind them.

One-off stylistic choices on a single page don't need a suggestion.
This is about patterns that will repeat.
