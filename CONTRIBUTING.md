# Contributing to Apollo Docs

Thank you for contributing to Apollo Docs! 🎉 We welcome all contributions.

## How to Contribute

### 🐛 Reporting Doc Bugs
- Check existing issues first
- Include: page URL, what's wrong (typo, broken link, outdated info, missing step), and what you expected to see

### 💡 Doc Improvements
- Check existing issues first
- Describe the gap and what would help (new page, clearer wording, screenshots, missing product, etc.)
- Be open to discussion

### 🔧 Doc Contributions
1. Fork the repository and create a branch from `dev` (not `main`)
2. Make changes following our standards
3. Preview locally with `mkdocs serve`
4. Submit a Pull Request **targeting `dev`** (PRs to `main` will not be merged)

## Quick Setup
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/docs.git
cd docs

# Create branch FROM dev
git fetch origin dev
git checkout -b docs/your-change origin/dev

# Install MkDocs and required plugins
pip install -r requirements.txt

# Live preview at http://127.0.0.1:8000
mkdocs serve
```

## Pull Request Process
1. **Target the `dev` branch** when opening your PR. The `main` branch is updated by maintainers from `dev`.
2. If you moved or renamed a page, add a redirect in the `redirects` plugin section of `mkdocs.yml` so external links keep working.
3. If you added a new page, add it to the nav in `mkdocs.yml`.
4. Verify the build is clean (no broken links or missing-plugin errors) via `mkdocs build`.
5. Fill out the PR template and link any related issues.
6. Use PR title format: `<type>: <description>` (types: `docs`, `fix`, `feat`, `chore`)

## Key files and folders

If you're new to the repo, these are the places that matter:

- **`mkdocs.yml`** — site config, navigation, theme, plugins (including
  redirects). If you add a new page, you also add it here. If you move
  a page, you add a `redirects` entry here.
- **`docs/products/`** — the Home Assistant tree. One subdirectory per
  product (`air1/`, `mtr1/`, etc.), each with its own `setup/`,
  `addons/`, `troubleshooting/`, `faq/` sections.
- **`docs/homey/products/`** — the Homey mirror of the same structure.
  When you edit a page in `docs/products/`, check whether the matching
  page in `docs/homey/products/` needs the same update.
- **`docs/assets/`** — images, screenshots, and other static files.
  Keep filenames kebab-case (`air1-boot-button.jpg`) and source images
  under 750px wide where possible.
- **`STYLE_GUIDE.md`** — the writing and formatting rules. Read before
  any non-trivial edit.
- **`AGENTS.md`** — instructions for AI tools editing the repo
  (Claude, Cursor, Codex, Copilot). `CLAUDE.md` is a pointer to this
  file.
- **`.github/PULL_REQUEST_TEMPLATE.md`** — the PR template. Fill it out
  completely, don't delete sections.

## Doc Standards

The full writing and formatting rules live in [STYLE_GUIDE.md](STYLE_GUIDE.md). Read it before opening a non-trivial PR. The highlights:

- **Tone**: respectful, confident, direct, empowering. Avoid corporate filler ("powerful", "seamlessly", "simply").
- **Voice**: second person, imperative. "Click **Save**", not "you should click save".
- **Product naming**: `AIR-1`, `MTR-1`, `MSR-2`, etc. uppercase with hyphen, always.
- **Terminology**: Apollo hardware **addons** and Home Assistant software **apps** are different things; use each in its own context.
- **ESPHome** is the only correct casing.
- **No em dashes** anywhere in user-facing copy.
- **Automation pages** carry a difficulty pill (`Level 1` (beginner) to `Level 3` (advanced)) under the title; harder pages can link easier ones in a stepping-stone box. See [Automation difficulty](STYLE_GUIDE.md#10-automation-difficulty).
- **Starter-kit pages** end with the community CTA snippet (`--8<-- "_snippets/community-help.md"`). Edit the snippet, not the page, when the CTA copy changes. See [Community CTA on starter-kit pages](STYLE_GUIDE.md#11-community-cta-on-starter-kit-pages).

Mechanical conventions:
- MkDocs Material: see https://squidfunk.github.io/mkdocs-material/ for admonitions, tabs, and content tabs syntax
- Snippets: when including parts of a file with `--8<-- "file.md:N:"`, start at line 5 to skip YAML front matter
- Images: place in `docs/assets/`, keep under 750px wide where possible (CI auto-resizes, but smaller source files render faster)
- Internal links: use site-relative paths so they work in the published site
- Front matter: every page needs at least `title:` and `description:`

If your PR establishes a new convention that isn't in [STYLE_GUIDE.md](STYLE_GUIDE.md) (a new product name, a new formatting pattern you'll want others to follow, a clarification of an ambiguous rule), update the style guide in the same PR. Keeping the guide ahead of the docs is how it stays useful.

## Contact & Support
- **Issues**: GitHub Issues for bugs and improvement requests
- **Email**: support@apolloautomation.com
- **Live site**: https://wiki.apolloautomation.com

Thank you for making Apollo Docs better! 💙
