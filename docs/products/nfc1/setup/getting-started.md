---
title: NFC-1 getting started
description: Step by step guide to getting your Apollo NFC-1 on Wi-Fi, adding it to Home Assistant, and scanning your first tag.
---
# NFC-1 getting started

This guide takes your Apollo NFC-1 from the box to a working tag reader in Home Assistant: you'll get it on your Wi-Fi, add it through the ESPHome integration, and scan your first tag.

## Connect to your network

There are three ways to get your NFC-1 on Wi-Fi. Pick whichever suits you, you only need to do one.

- **Improv via BLE** sets the NFC-1 up over Bluetooth straight from Home Assistant. It needs Bluetooth on your Home Assistant host or an ESP32 Bluetooth proxy.
- **USB** uses the Apollo installer in your browser. It also installs the latest firmware, so it's the way to go if you want to reflash the NFC-1.
- **Hotspot** works on any phone or computer. The NFC-1 broadcasts its own Wi-Fi network, you join it, then enter your Wi-Fi details.

=== "Improv via BLE"

    !!! note "Pre-requirement: Bluetooth proxy or Bluetooth Home Assistant hardware required"

        Bluetooth built in, such as on a Raspberry Pi, or at least one [ESP32 Bluetooth proxy](../../general/setup/bluetooth-proxy.md) is required to set up your NFC-1 this way.

    1\. Plug in your NFC-1 and keep it within Bluetooth range of your Home Assistant host or proxy.

    2\. Open your integrations page in Home Assistant (**Settings → Devices & services**).

    [![Open your Home Assistant instance and show your integrations.](https://my.home-assistant.io/badges/integrations.svg)](https://my.home-assistant.io/redirect/integrations/)

    3\. Click **Add** on the discovered NFC-1, type in your Wi-Fi SSID and password, then click **Submit**. The NFC-1 doesn't ask you to press a button to approve the setup.

    4\. Click **Submit** again, give it an **Area**, then click **Finish**.

    Improv adds your NFC-1 to Home Assistant as part of setup, so skip ahead to [scan your first tag](#scan-your-first-tag).

=== "USB"

    !!! note "Use Chrome, Edge, or Firefox on a computer"

        The installer needs a browser that can talk to the USB serial port, and a USB cable that carries data, not only power.

    1\. Plug the NFC-1 into your computer with a USB data cable.

    2\. Open the [Apollo installer for the NFC-1](https://install.apolloautomation.com/#/nfc-1) and click **Connect & Install**.

    3\. Pick the NFC-1's serial port in the browser popup and click **Connect**. (1)
    { .annotate }

    1.  If no port appears, try a different USB cable. Many cables only carry power.

    4\. If the installer shows a menu, click **Install ApolloAutomation.NFC-1** (it reads **Update ApolloAutomation.NFC-1** if the NFC-1 already runs Apollo's firmware). Click **Install** to confirm.

    5\. When you see **Installation complete!**, click **Next**. If the installer shows its menu again, click **Connect to Wi-Fi**. Under **Configure Wi-Fi**, pick your **Network**, type the **Password**, and click **Connect**.

    6\. Once you see **Device connected to the network!**, click **Add to Home Assistant** or carry on with [Add to Home Assistant](#add-to-home-assistant) below.

=== "Hotspot"

    1\. Plug in your NFC-1.

    2\. On your phone or computer, open the Wi-Fi settings and connect to **Apollo NFC1 Hotspot**.

    !!! tip "Setup page didn't open?"

        Your phone should open the Wi-Fi setup page on its own after you join the hotspot. If it doesn't, go to [http://192.168.4.1](http://192.168.4.1).

    3\. Select the Wi-Fi network you want your NFC-1 to join, type in your Wi-Fi password, then click **Save**.

    4\. Once the NFC-1 joins your Wi-Fi, its hotspot goes away and your phone switches back to your own network. Your NFC-1 is now on your Wi-Fi.

## Add to Home Assistant

Once the NFC-1 is on your Wi-Fi, Home Assistant discovers it through the ESPHome integration. This is where it becomes a real, working device on your dashboard.

1\. Open the ESPHome integration in Home Assistant (**Settings → Devices & services → ESPHome**).

[![Open your Home Assistant instance and show an integration.](https://my.home-assistant.io/badges/integration.svg)](https://my.home-assistant.io/redirect/integration/?domain=esphome)

2\. Find the discovered **Apollo NFC-1** and click **Add**, then **Submit**.

3\. Edit the name if you like, choose an **Area**, then click **Finish**.

Your NFC-1 now has its own device page with controls, sensors, and settings. [Sensor definitions](sensor-definitions.md) explains each one.

## Check the status light

Each time the NFC-1 starts up, its LED shows how it's connected for 5 seconds, then turns off:

| Color | What it means |
| --- | --- |
| Blue | Connected to Home Assistant |
| Green | Connected to Wi-Fi, but not to Home Assistant yet |
| Yellow | Not connected to Wi-Fi |

On its first start after a fresh install, the LED stays a soft green instead, until you scan your first tag. If it lights red, the NFC reader didn't start. Reach out on [Discord](https://link.apolloautomation.com/discord) or at support@apolloautomation.com so we can help.

## Scan your first tag

1\. Hold an NFC tag or card flat against the NFC-1. NTAG, MIFARE Ultralight, and MIFARE Classic tags all work.

2\. The LED flashes green and the buzzer beeps once.

3\. On the NFC-1's device page, **Last Tag UID** shows the tag's UID and **Tag Present** turns on while the tag stays on the reader.

Home Assistant also lists the tag under **Settings → Tags**, so you can name it and use it to trigger automations.

[![Open your Home Assistant instance and show your tags.](https://my.home-assistant.io/badges/tags.svg)](https://my.home-assistant.io/redirect/tags/)

!!! success "Next step: read and write tags"

    Your NFC-1 is reading tags. Next, run an automation from a tap, write your own tags, and turn on card emulation.

    [Read and write tags](../examples/read-and-write-tags.md){ .md-button .md-button--primary }
