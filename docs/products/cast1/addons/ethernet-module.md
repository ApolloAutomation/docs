---
title: Add the Ethernet Module to CAST-1
description: "How to install the Ethernet add-on module on your CAST-1."
---
# Adding the Ethernet Module

The Ethernet add-on gives your CAST-1 a wired network connection. It's a small header board that presses onto the top of the CAST-1, so there's no case to open and nothing to solder.

1\. Unplug your CAST-1 from power.

2\. Find the two rows of female header pins on the top of the case.

3\. Line the module's pins up with those two rows, pin side down, and press it straight down until it sits flat. (1)
{ .annotate }

1.  Press evenly on both ends. If the module won't sit flat against the case, lift it off and line the pins up again rather than forcing it.

![](/assets/cast-1-connect-ethernet-module.webp)

4\. Plug an Ethernet cable into the module, then plug the CAST-1 back into power.

That's it. Your CAST-1 picks the wired connection up on its own. Check the **Network Connection** sensor on the device page to confirm it reads **Ethernet**. (1)
{ .annotate }

1.  It reads **Ethernet + WiFi** if your CAST-1 is on both at once, which is what you want. Home Assistant keeps talking to the device that way while you plug or unplug the cable.

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
