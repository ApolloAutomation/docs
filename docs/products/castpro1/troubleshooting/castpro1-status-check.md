---
title: Status check and factory reset
description: Hold the boot button on your CAST PRO-1 to see whether it's connected to your network and Home Assistant, or to factory reset it.
---
# Status check and factory reset

Not sure whether your Apollo CAST PRO-1 is online? Hold its boot button, and the onboard LEDs show a color that tells you.

!!! note "Firmware 26.11.3.2 or newer"

    The green and yellow colors need firmware 26.11.3.2 or newer. Older firmware shows blue when it's connected to Home Assistant, and nothing otherwise.

## Check the connection

1\. Press and hold the boot button for about 3 seconds, then let go. Anywhere from 1 to 8 seconds works.

2\. Check the color on the onboard LEDs. It stays on for 5 seconds.

| Color | What it means | What to do |
| --- | --- | --- |
| Blue | Connected to Home Assistant. | You're all set. |
| Green | On your network (Ethernet or WiFi), but not connected to Home Assistant. | Make sure Home Assistant is running and your CAST PRO-1 is added under **Settings → Devices & services → ESPHome**. |
| Yellow | Not on a network. | Plug in an Ethernet cable, or set up WiFi: join the **Apollo CAST_PRO-1 Hotspot** network from your phone, then pick your WiFi network and enter its password. |

[![Open your Home Assistant instance and show an integration.](https://my.home-assistant.io/badges/integration.svg)](https://my.home-assistant.io/redirect/integration/?domain=esphome)

About 5 seconds after the color goes off, the LEDs flash green for 5 seconds. That's a self-test, not a status color, so go by the first color. You may also see this flash about 7 seconds after your CAST PRO-1 starts.

!!! warning "Let go before 8 seconds"

    Holding the boot button for 8 seconds or more factory resets your CAST PRO-1.

## Factory reset

A factory reset erases your CAST PRO-1's WiFi network and settings, then restarts it. Use it when it won't connect, or before you give it to someone else.

1\. Press and hold the boot button for 8 seconds or more, then let go.

2\. Connect your CAST PRO-1 again with an Ethernet cable, or set up WiFi from its **Apollo CAST_PRO-1 Hotspot** network.

## Adding it back to Home Assistant

A new CAST PRO-1 joins Home Assistant without asking for a key. If you factory reset yours, or deleted it from Home Assistant and added it again, Home Assistant may ask first:

- **It says the device disabled transport encryption:** confirm the prompt, and Home Assistant reconnects.
- **It asks for an encryption key:** factory reset your CAST PRO-1, then add it again.

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
