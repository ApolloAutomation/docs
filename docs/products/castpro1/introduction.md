---
title: Introduction
description: Documentation for CAST PRO-1, including setup, usage, and best practices.
---
# Introduction

**Make Any Speakers Smart:** Connect the CAST PRO-1 to your speakers, receiver, or soundbar, add it to Home Assistant, and it shows up in Music Assistant as a player you can stream to. It needs Music Assistant 2.10.7 or newer.

**Analog or Optical Output:** Use the analog output for powered speakers, or the optical output for a receiver or soundbar. Pick which one plays with the **Audio Output** setting on the device page.

**Line In:** Plug a turntable, TV, or other source into the Line In jack, and it becomes a source in Music Assistant. Play it on any speaker or group, in sync across every room. See [Play Line In with Music Assistant](examples/line-in.md).

**Built-In Ethernet:** The CAST PRO-1 has an Ethernet port on board, so it can run on a wired connection with no addon. Without a cable, it works over WiFi.

**Multi-Room Audio:** Group the CAST PRO-1 with other CAST players to play the same music in sync across every room. Streaming runs locally through Music Assistant and Sendspin, so there's no cloud account and no subscription. If a soundbar or receiver makes one room play a little late, go to **Settings → Players** in Music Assistant, open that CAST PRO-1, and raise **Static playback delay (ms)** until the rooms line up. It starts at 0.

**LED Strip Terminals:** Connect an addressable LED strip to the terminals, with no soldering. It shows up in Home Assistant as a light with effects and a Music Mode that follows playback. See [Add an LED strip](examples/led-strip.md).

**Status Check:** Hold the boot button for a few seconds, and the onboard LEDs show whether your CAST PRO-1 is connected. See [Status check and factory reset](troubleshooting/castpro1-status-check.md).

**WizMote Control:** Pair a WizMote for physical control over playback without opening an app. Each button is configurable in Home Assistant.

!!! note "Needs firmware 26.11.3.2"

    Line In, the LED strip, the status check, and the playback delay setting arrive in CAST PRO-1 firmware 26.11.3.2. Update from the **Firmware Update** entity on the device page. Until this release reaches the Stable channel, [switch to the Beta channel](../general/setup/switch-to-beta-branch.md) first.

## Device page controls

You'll find these on your CAST PRO-1's device page in Home Assistant.

| Entity | What it does |
| --- | --- |
| **Audio Output** | Plays through **Analog** or **Optical**. |
| **Line In Streaming** | How Line In travels over your network: **Compressed (best for WiFi)** or **Lossless (Ethernet or strong WiFi)**. Changing it restarts your CAST PRO-1. |
| **Firmware Channel** | Gets updates from **Stable** or **Beta**. |
| **LED Strip** entities | Hidden until you turn them on. See [Add an LED strip](examples/led-strip.md). |

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
