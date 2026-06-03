# Apollo Docs Style Guide

## 1. About this guide

This guide governs the writing and formatting of pages on
[wiki.apolloautomation.com](https://wiki.apolloautomation.com). It is the
single source of truth for tone, language, and structural conventions.
Contributors, maintainers, and AI tools (Claude, Copilot, Cursor, and
others) all read from this file.

**Who the wiki is for.** Smart-home owners and tinkerers who want to
know what an Apollo device does, how to set it up, and how to make it
work inside their Home Assistant or Homey setup. They range from
first-time Home Assistant users to ESPHome contributors. The docs need
to land for both ends without patronising the first or boring the
second.

**Why these rules exist.** Without them, every contributor (human or
AI) reinvents tone, terminology, and structure on every page. Readers
feel the inconsistency even when they can't name it. The rules below
are the result of decisions already made across the existing pages,
codified so the next contributor doesn't have to make them again.

For workflow (how to fork, branch, preview, and open a PR), and for the
file layout of the repo, see [CONTRIBUTING.md](CONTRIBUTING.md).

> **A note for contributors:** this guide gives prescriptive rules to keep
> the docs consistent. The "avoid" lists below apply to **user-facing
> prose**, not to this style guide or other internal documents. Telling a
> contributor "never use em dashes" is a rule, not a violation of the
> rule.

---

## 2. Tone of voice

| Aim for | Avoid |
| --- | --- |
| Respectful | Patronising |
| Confident | Boastful |
| Enthusiastic | Breathless |
| Direct | Corporate |
| Empowering | Instructional |

The "empowering, not instructional" line is the one most contributors
trip over. Numbered steps are unavoidable in technical docs, but a wall
of imperatives reads as bossy. Wrap procedures with framing copy that
explains what the reader is about to unlock (see
[Numbered steps and framing](#numbered-steps-and-framing) below).

## 3. Language to use

Use these phrases consistently. They are part of the Apollo voice.

- **Build, learn, automate**: the organising framework
- **Your home, your way**: ownership and personalisation
- **On your own terms**: independence and choice
- **Real, working device**: tangible outcome
- **Just the beginning**: opens up possibility without overpromising
- **Local control**: an HA-audience touchstone that signals values
- **Open standards**: credibility and trust
- **Step by step**: structured, guided
- **ESPHome ecosystem**: positions the kit within a bigger world

When using **open standards** or **local control** for the first time on
a page, follow with the canonical plain-language explanation below.
Readers new to the space need the translation, and using the same line
across the wiki reinforces the message.

- **Local control**: your home runs on your own network. Your devices
  keep working even if your internet goes down or Apollo goes away.
- **Open standards**: Apollo builds on public protocols like ESPHome
  and OpenThread, so your kit is never locked to one vendor.

## 4. Language to avoid

| Don't say | Why | Use instead |
| --- | --- | --- |
| Beginner, basic | Patronising | "Getting started", "First boot" |
| Easy on its own | Vague | Qualify: "easy if you already have X" |
| Simply, just | Dismissive | Drop the word entirely |
| Powerful | Cliché | Describe what it actually does |
| Seamlessly | Cliché | Describe the specific behaviour |
| Genuinely, honestly | Undermines credibility | Drop the word entirely |
| "Coding without context" | Intimidating | Say what's actually required |
| Excessive "no" framing | Negative tone | Rephrase positively |

---

## 5. Product and terminology

### Product IDs

Product IDs are always uppercase with a hyphen: **AIR-1**, **MTR-1**,
**MSR-2**, **BTN-1**, **PLT-1**, **R-PRO-1**, **TEMP-1**, **LED-1**,
**M-1**, **PUMP-1**.

Never `Air-1`, `air1`, or `AIR1` in body copy. mkdocs.yml is the source
of truth for the canonical form.

### First mention per page

On the first mention of a product in body copy, use the full brand name:
**Apollo AIR-1**. After that, the short form **AIR-1** is fine for the
rest of the page. Very short pages (a single intro paragraph, an FAQ
entry) may use the short form throughout.

### Apollo addons vs Home Assistant apps

Two different things share the same word and they are not interchangeable:

- **Apollo addons** are physical hardware modules (the CO2 sensor for
  AIR-1, etc.). Write **addon** or **addons**, lowercase, no hyphen.
- **Home Assistant apps** are the software formerly called add-ons. Home
  Assistant renamed them to apps in 2025. Write **app** or **App Store**.

A page about installing the CO2 hardware addon AND configuring it via a
Home Assistant app will use both terms. Each is correct in its own
context.

The forms `add-on`, `Add-on`, and `Addon` should not appear in
user-facing copy unless quoting upstream documentation.

### ESPHome

Always capitalised exactly **ESPHome**. Never `esphome`, `ESPhome`,
`Esphome`, or `ESPHOME`. This matches the upstream project's own brand.

When introducing the broader project, prefer **ESPHome ecosystem** over
"the ESPHome project" or "ESPHome firmware".

### Flashing firmware

**Flash** is the preferred verb for putting firmware on a device:

> Flash your AIR-1 with the latest firmware.

**Install firmware** is acceptable when "flash" would be confusing
context (for example, when the audience may not recognise the term).
Avoid **burn** and **load**.

---

## 6. Voice and structure

### Second person, imperative

Default to second person addressed to the reader, with imperative verbs
in action copy.

> Click **Save**. Plug in your AIR-1. Open the **ESPHome Device Builder
> app** from your sidebar.

Avoid:

- First person plural: "we'll now configure..."
- Hedging modal: "you should click..."
- Passive: "the device is plugged in..."

### Headings

Every page has exactly one H1, written as the first line of the body
(`# Adding the button module`). mkdocs-material renders this as the
page heading. The front matter `title:` is used by the nav, browser
tab, and search snippets, and should match the H1.

All headings use sentence case. The first word is capitalised, and
proper nouns are capitalised. Everything else is lowercase.

| Yes | No |
| --- | --- |
| Connecting through hotspot | Connecting Through Hotspot |
| Your first automation | Your First Automation |
| Getting started with AIR-1 | Getting Started With Air-1 |

### Heading levels and the sidebar

mkdocs-material integrates each page's TOC into the left sidebar, and
`toc_depth` is set to `3` in `mkdocs.yml`. That means **only H2 and H3
headings appear in the sidebar**. Plan your headings with that in mind:

- **H1**: the page title, written as the first line of the body and
  mirrored in the front matter `title:`. Exactly one per page.
- **H2**: major sections. Each H2 becomes a sidebar entry, so use them
  for things a reader might jump to ("Connecting through hotspot",
  "Troubleshooting").
- **H3**: subsections that still deserve a sidebar entry. Use
  sparingly. A page with a dozen H3s under one H2 floods the sidebar.
- **H4 and below**: in-page detail only. They render in the body but
  stay out of the sidebar.

If you find yourself wanting an H4 to show up in the sidebar, the right
move is usually to promote it to H3, or split the page.

### Numbered steps and framing

Any sequence of three or more actions becomes a numbered list. Each step
starts with an imperative verb.

```markdown
1. Plug your AIR-1 into power. The LED turns blue.
2. Open the **Home Assistant** app on your phone.
3. Tap **Settings → Devices & services → Add integration**.
```

Sub-steps nest as bullets under the parent number. Do not use
"Step 1:", "Step 2:" headings.

**Frame the steps.** A bare list of imperatives reads as instructional.
Lead with a sentence or two on what the reader is about to unlock, and
follow with a quick success check.

> **Adding your AIR-1 to Home Assistant**
>
> Once your sensor is on Wi-Fi, Home Assistant will discover it
> automatically. This is where your AIR-1 becomes a real, working device
> in your dashboard.
>
> 1. ...
> 2. ...
> 3. ...
>
> Your AIR-1 now shows up under **Settings → Devices**. From here, every
> reading the sensor takes flows into Home Assistant in real time.

Banned softeners inside steps: **simply**, **just**, **easy**. These
either patronise the reader or pad the sentence.

### Front matter

Every page has YAML front matter with at minimum a `title` and a
`description`:

```yaml
---
title: Adding a CO2 addon to your AIR-1
description: Step-by-step guide to installing the CO2 sensor module and seeing readings in Home Assistant.
---
```

- `title` shows in the browser tab, the nav, and the H1.
- `description` is used by mkdocs for search snippets and social card
  previews. Skipping it hurts both.

---

## 7. Formatting conventions

### UI labels

Buttons, menu items, tabs, and other on-screen labels are formatted in
**bold**. Multi-step navigation uses the Unicode right arrow `→`.

> Open **Settings → Devices & services → Add integration** and search
> for **Apollo**.

Do not use backticks, quotes, or italics for UI elements.

### Code identifiers

Anything the reader types literally or sees in a code-shaped context
goes in backticks. This includes:

- Entity IDs: `sensor.air1_co2`
- YAML keys and paths: `wifi.ssid`, `esphome.name`
- File paths: `/config/configuration.yaml`
- Shell commands: `esphome run`
- Config values: `power_save_mode: none`

The distinction matters: **bold** means a thing on the screen,
`backticks` means a literal string.

### Fenced code blocks

Every fenced code block must declare a language for syntax highlighting:

````markdown
```yaml
wifi:
  ssid: !secret wifi_ssid
```
````

When the snippet belongs to a specific file, add a title:

````markdown
```yaml title="configuration.yaml"
homeassistant:
  name: My Home
```
````

### Images

- Stored under `docs/assets/`.
- Filenames in kebab-case: `air1-boot-button.jpg`.
- Every image has descriptive alt text. Alt text describes what the
  image shows, not what the file is called. Screen readers and broken
  images both depend on it.
- Keep source images under 750px wide where possible. CI auto-resizes,
  but smaller sources render faster.

```markdown
![AIR-1 boot button highlighted on the underside of the case](/assets/air1-boot-button.jpg)
```

### Internal links

Internal links use site-relative paths in wiki-URL form (trailing
slash, no `.md` extension), not absolute
`https://wiki.apolloautomation.com/...` URLs:

```markdown
See [getting started](../setup/getting-started/) for first-boot setup.
```

Relative links work in PR previews and survive a future domain change.
Links to external sites (home-assistant.io, esphome.io) stay absolute.

---

## 8. Punctuation

### Oxford comma

Always use the Oxford comma in lists of three or more items.

> AIR-1 supports Wi-Fi, MQTT, and Bluetooth.

### Em dashes

Do not use em dashes (`—`) anywhere in user-facing copy. Replace with
commas, periods, parentheses, or "X to Y" for ranges.

| Don't write | Write instead |
| --- | --- |
| `The AIR-1 — once flashed — connects automatically.` | `The AIR-1, once flashed, connects automatically.` |
| `Three sensors — CO2, VOC, and PM2.5 — ship in the kit.` | `Three sensors (CO2, VOC, and PM2.5) ship in the kit.` |
| `Run the test for 5 — 10 minutes.` | `Run the test for 5 to 10 minutes.` |

### Lists

List items that are complete sentences end with a period. Fragments do
not.

```markdown
Features:
- Real-time CO2 readings
- Onboard temperature compensation
- USB-C power

Setup steps:
- Plug in the device.
- Wait for the LED to turn green.
- Open the companion app.
```

---

## 9. Files and folders

### Filenames

All markdown filenames are kebab-case: `adding-co2-to-air-1.md`. No
camelCase, no snake_case, no spaces, no capital letters.

### Directory structure

Pages live under per-product subdirectories, mirrored across platform
trees:

```
docs/
├── products/                    Home Assistant tree
│   └── air1/
│       ├── setup/
│       ├── addons/
│       └── troubleshooting/
└── homey/products/              Homey tree
    └── air1/
        ├── setup/
        ├── addons/
        └── troubleshooting/
```

When a topic exists on both Home Assistant and Homey, use the **same
filename** in both trees. This makes cross-platform consistency obvious
to anyone editing the docs.

**When you edit a page in one tree, check the mirror in the other tree
and update it too if the change applies.** Cross-tree drift, where the
HA version of a page describes the current product behaviour and the
Homey version still describes how it worked a year ago, is the biggest
source of stale content on the wiki. If a change is platform-specific
and genuinely doesn't apply to the other tree, leave a one-line note in
the PR description explaining why so reviewers don't flag it.

For the full repo layout (where `mkdocs.yml` lives, where redirects go,
how `docs/assets/` is organised), see
[CONTRIBUTING.md](CONTRIBUTING.md#key-files-and-folders).

---

## 10. Automation difficulty

Every automation page carries a difficulty pill directly under the H1 so
readers can gauge how involved the setup is. The rating is about **setup
difficulty and skill** (steps, helpers, templating, integrations), not
runtime load.

| Level | Use it when the automation... |
| --- | --- |
| 1 | is plug-and-play, or needs only a helper or two and a few guided steps. |
| 2 | combines several entities, conditions, or a template. |
| 3 | needs templating, blueprints, multi-device logic, or is heavily custom. |

Add the pill as the first line under the title. The `lvl-N` class sets the
color (green at 1, amber at 2, red at 3):

```html
# Build a Button-Controlled RGB Light

<span class="difficulty lvl-1">Difficulty: Level 1</span>
```

### Stepping-stone box

On a harder page, point newcomers at one to three easier automations from
the **same product**. Add it under the pill at your discretion (Level 2
and up is a good rule of thumb). Use relative links so previews work:

```html
<p class="automation-steps-heading">🌱 New here? Try these first:</p>
<div class="automation-steps">
  <div class="step">
    <a class="step-title" href="../motion-activated-light/">Turn On a Light with Motion</a>
    <span class="difficulty lvl-1">Difficulty: Level 1</span>
  </div>
  <div class="step">
    <a class="step-title" href="../button-controlled-leds/">Build a Button-Controlled RGB Light</a>
    <span class="difficulty lvl-1">Difficulty: Level 1</span>
  </div>
</div>
```

The pill and box styles live in `docs/stylesheets/extra.css`; never inline
colors on the page.

---

## 11. Community CTA on starter-kit pages

Every page under the **ESPHome Starter Kit** product carries the same
community call-to-action at the bottom: a friendly note admonition titled
"New to ESPHome? We're here to help." with links to Discord and the
Community Forum. The copy and buttons live in a single snippet so the
CTA stays consistent across the product and only needs one edit to update.

**Source of truth:** `docs/_snippets/community-help.md`

**Where to include it:** at the very bottom of any starter-kit page (after
any existing "Try it in an automation" buttons, "Next Steps" buttons, or
closing success admonition). One blank line of separation from the
content above is enough.

**How to include it:**

```markdown
--8<-- "_snippets/community-help.md"
```

**When you add a new starter-kit page**, end it with this include before
opening the PR. **When you edit the CTA copy** (adding a new channel,
rewording the prompt, swapping button labels), edit the snippet file
itself, never the include line on a page.

The snippet uses the standard `note` admonition flavor for visual
consistency with the kit's other admonitions ("Before you start", tips,
warnings); don't swap it for `tip` or `info` on a per-page basis.

---

## 12. When in doubt

If a rule above conflicts with clarity for the reader, clarity wins.
Open an issue or PR proposing the rule change so the guide stays
honest.
