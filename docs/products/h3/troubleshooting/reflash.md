---
title: Factory Re-Flash H-3
description: "Step by step guide for re-flashing the H-3 back to factory firmware."
---
# Reflashing The H-3

!!! info "Reflash the H-3 if it stops responding, or to move between the basic and smart firmware."

    Do this in Chrome, Edge, or Firefox. The installer needs a browser that can talk to the USB serial port.

1\. Put the ornament in [boot mode](https://wiki.apolloautomation.com/products/h3/troubleshooting/boot-mode/) and leave it plugged into your computer.

2\. Open the [Apollo installer](https://install.apolloautomation.com/#/h-3) and pick which firmware you want. **Smart (Wi-Fi)** joins your Wi-Fi and Home Assistant. **Basic (No Wi-Fi)** is the firmware the ornament ships with, where the buttons play the built-in tunes.

3\. Click **Connect & Install**, then pick the serial port for your ornament. (1)
{ .annotate }

1.  If no port appears, the ornament is not in boot mode or the USB cable is charge-only. Try a different cable.

4\. Follow the prompts to install. Once you see "Installation complete!" you are finished.

!!! warning "Power cycle your device before doing anything else!"

    Your device is still in boot mode and needs to be power cycled aka power removed to make it boot in a normal mode!

[Head to the Getting Started article to setup your H-3 as a new device!](https://wiki.apolloautomation.com/products/h3/setup/getting-started/){                .md-button .md-button--primary }
