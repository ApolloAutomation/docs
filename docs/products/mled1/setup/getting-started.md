---
title: MLED-1 getting started
description: Step by step guide to wiring an LED strip to your Apollo MLED-1, getting it on Wi-Fi, setting it up for your strip, and adding it to Home Assistant.
---
# MLED-1 getting started

This guide takes your Apollo MLED-1 from the box to a working light in Home Assistant: you'll wire up your LED strip, get the MLED-1 on your Wi-Fi, tell WLED about your strip, and add it through the WLED integration.

## Wire up your LED strip

!!! danger "Use a 5V strip"

    The MLED-1 is rated for 5V and 3A. Connect a 5V addressable LED strip, and unplug the MLED-1 before you connect or move any wires.

1\. Find your strip's three wires: power (5V), data, and ground.

2\. Insert each wire into its matching terminal on the MLED-1's WAGO connector.

The MLED-1 drives the strip's data line from GPIO 13, and the firmware already has that set, so there's no pin to choose later.

## Connect to your network

There are two ways to get your MLED-1 on Wi-Fi. Pick whichever suits you, you only need to do one.

- **USB** uses the Apollo installer in your browser. It installs the latest firmware and then sets up Wi-Fi over the same cable.
- **Hotspot** works on any phone or computer. The MLED-1 broadcasts its own Wi-Fi network, you join it, then enter your Wi-Fi details.

=== "USB"

    !!! note "Use Chrome or Edge on a computer"

        The installer needs a browser that can talk to the USB serial port, and a USB cable that carries data, not only power.

    1\. Plug the MLED-1 into your computer with a USB data cable.

    2\. Open the [Apollo installer for the MLED-1](https://install.apolloautomation.com/#/mled-1) and click **Connect & Install**.

    3\. Pick the MLED-1's serial port in the browser popup and click **Connect**. (1)
    { .annotate }

    1.  If no port appears, try a different USB cable. Many cables only carry power.

    4\. If the installer shows a menu, click **Install Apollo MLED-1**. When it asks whether to erase the device, tick **Erase device** for a fresh start, then click **Next** and **Install**.

    5\. When you see **Installation complete!**, click **Next**. If the installer shows its menu again, click **Connect to Wi-Fi**. Under **Configure Wi-Fi**, pick your **Network**, type the **Password**, and click **Connect**.

    6\. Once you see **Device connected to the network!**, your MLED-1 is on your Wi-Fi. Carry on with [Set it up for your strip](#set-it-up-for-your-strip) below.

=== "Hotspot"

    !!! tip "Set up one MLED-1 at a time"

        Every MLED-1 that isn't on Wi-Fi yet broadcasts the same hotspot name. If you have more than one, plug in and set up one at a time.

    1\. Plug in your MLED-1.

    2\. On your phone or computer, open the Wi-Fi settings and join **Apollo MLED-1 Hotspot**. It's an open network, so there's no password to type.

    3\. Wait for the **Welcome to WLED** page to open. If it doesn't, open <a href="http://4.3.2.1/" target="_blank" rel="noopener">http://4.3.2.1/</a> in a browser.

    4\. Select **WIFI SETTINGS**, click **Scan**, pick your network, and type your Wi-Fi password. Passwords are case sensitive, so take your time here.

    5\. Optionally, set the **mDNS address** to something like `apollo-mled-1`, so you can reach the MLED-1 at `http://apollo-mled-1.local` later instead of hunting for its IP address.

    6\. Click **Save & Connect**.

    Once the MLED-1 joins your Wi-Fi, its hotspot goes away and your phone switches back to your own network. If it can't connect, the hotspot comes back, so run through the steps again and double-check the network name and password.

    !!! warning "http://4.3.2.1/ stops working once the MLED-1 joins your network"

        That address only exists while you're connected to the MLED-1's own hotspot. On your Wi-Fi, use the mDNS address you set, or find the MLED-1's IP address with the WLED app or your router.

## Set it up for your strip

WLED starts out set for a 30-LED WS2812B strip. Match it to the strip you wired up so every LED lights in the right color.

1\. Open the MLED-1's WLED page in a browser at its IP address or mDNS address, or open it in the WLED app.

2\. Click **Config**, then **LED & Hardware**.

3\. Set the LED type, **Color Order**, and **Length** to match your strip. Leave **GPIO** at 13.

4\. Click **Save**.

Your whole strip now lights up. Head back to the main controls and try a few effects.

!!! tip "Match the brightness limiter to your power supply"

    WLED's automatic brightness limiter starts at 850 mA, so a long strip may look dimmer than you expect. Under **LED & Hardware**, set **Maximum PSU Current** to what your power supply delivers, up to the MLED-1's 3A rating.

## Add to Home Assistant

Once the MLED-1 is on your Wi-Fi, Home Assistant discovers it through the WLED integration. This is where it becomes a real, working light on your dashboard.

1\. Open your integrations page in Home Assistant (**Settings → Devices & services**).

[![Open your Home Assistant instance and show your integrations.](https://my.home-assistant.io/badges/integrations.svg)](https://my.home-assistant.io/redirect/integrations/)

2\. Find the discovered **WLED** device and click **Add**, then **Submit**.

3\. Edit the name if you like, choose an **Area**, then click **Finish**.

Your MLED-1 now has its own device page in Home Assistant. Switch it on and off, change the color and brightness, and pick effects and presets right from your dashboard.

!!! success "Next step: keep your firmware current"

    Your MLED-1 is lighting up your strip. When a new firmware release comes out, update it from the Apollo installer and keep your settings.

    [Update or reflash the MLED-1](../troubleshooting/reflash.md){ .md-button .md-button--primary }
