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

## Doc Standards

The full writing and formatting rules live in [STYLE_GUIDE.md](STYLE_GUIDE.md). Read it before opening a non-trivial PR. The highlights:

- **Tone**: respectful, confident, direct, empowering. Avoid corporate filler ("powerful", "seamlessly", "simply").
- **Voice**: second person, imperative. "Click **Save**", not "you should click save".
- **Product naming**: `AIR-1`, `MTR-1`, `MSR-2`, etc. uppercase with hyphen, always.
- **Terminology**: Apollo hardware **addons** and Home Assistant software **apps** are different things; use each in its own context.
- **ESPHome** is the only correct casing.
- **No em dashes** anywhere in user-facing copy.

Mechanical conventions:
- MkDocs Material: see https://squidfunk.github.io/mkdocs-material/ for admonitions, tabs, and content tabs syntax
- Snippets: when including parts of a file with `--8<-- "file.md:N:"`, start at line 5 to skip YAML front matter
- Images: place in `docs/assets/`, keep under 750px wide where possible (CI auto-resizes, but smaller source files render faster)
- Internal links: use site-relative paths so they work in the published site
- Front matter: every page needs at least `title:` and `description:`

## Contact & Support
- **Issues**: GitHub Issues for bugs and improvement requests
- **Email**: support@apolloautomation.com
- **Live site**: https://wiki.apolloautomation.com

Thank you for making Apollo Docs better! 💙
