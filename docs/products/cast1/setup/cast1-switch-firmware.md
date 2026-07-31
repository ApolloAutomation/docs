---
title: CAST-1 Switch Firmware
description: >-
  Step by step guide to switching between Wi-Fi and Ethernet firmware on
  CAST-1.
---
# Switch Firmware

Every CAST-1 ships on Wi-Fi firmware, because not everyone has Ethernet where their speakers are. Once you've installed the [Ethernet module](https://wiki.apolloautomation.com/products/cast1/addons/ethernet-module/), switch your CAST-1 to the Ethernet firmware to use the wired connection. You can switch back whenever you want.

!!! tip "You can also switch over USB instead of from Home Assistant."

    The <a href="https://install.apolloautomation.com/#/cast-1" target="_blank" rel="noreferrer nofollow noopener">Apollo CAST-1 Installer</a> flashes either the **WiFi** or **Ethernet** variant straight from your browser. Pick the variant you want, then follow the <a href="https://wiki.apolloautomation.com/products/cast1/troubleshooting/cast1-reflash/" target="_blank" rel="noopener">reflashing guide</a> for the boot mode steps. Use this if your CAST-1 is on a network that can't reach github.com, since the steps below download the firmware image from our GitHub repo.

### Switch to Ethernet

1\. Plug the Ethernet cable into your CAST-1 before you start. (1)
{ .annotate }

1.  The Ethernet firmware has no Wi-Fi at all. If the cable isn't connected when it reboots, the CAST-1 has no way onto your network and you'll have to reflash it over USB.

2\. Open the ESPHome integration, then click through to your Apollo CAST-1 to open its device page.

<a href="https://my.home-assistant.io/redirect/integration/?domain=esphome" target="_blank" rel="noreferrer noopener"><img src="https://my.home-assistant.io/badges/integration.svg" alt="Open your Home Assistant instance and show the ESPHome integration."></a>

3\. Scroll down to the **Firmware Type** dropdown and select **Ethernet**.

4\. Find the **Firmware Update** entity and click **PRESS**.

5\. Wait a few minutes. The CAST-1 downloads the Ethernet image, installs it, and reboots onto the wired connection.

6\. Home Assistant reconnects to your CAST-1 automatically. Check the **IP Address** sensor on the device page to confirm the wired connection came up.

### Switch to Wi-Fi

1\. Open the ESPHome integration, then click through to your Apollo CAST-1 to open its device page.

<a href="https://my.home-assistant.io/redirect/integration/?domain=esphome" target="_blank" rel="noreferrer noopener"><img src="https://my.home-assistant.io/badges/integration.svg" alt="Open your Home Assistant instance and show the ESPHome integration."></a>

2\. Scroll down to the **Firmware Type** dropdown and select **WiFi**.

3\. Find the **Firmware Update** entity and click **PRESS**.

4\. Wait a few minutes while the CAST-1 downloads and installs the Wi-Fi image, then reboots.

5\. Your CAST-1 rejoins the Wi-Fi network it used before. If it doesn't come back, it will broadcast the "**Apollo CAST 1 Hotspot**" network so you can enter your Wi-Fi details again. (1)
{ .annotate }

1.  The [Getting Started guide](https://wiki.apolloautomation.com/products/cast1/setup/getting-started/) walks through connecting over the hotspot.

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
