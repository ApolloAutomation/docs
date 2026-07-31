---
title: CAST-1 Getting Started Guide
description: Step by step guide to getting started with your CAST-1!
---
# CAST-1 Getting Started

This will guide you through connecting your CAST-1 to your speakers, adding it to your Wi-Fi and Home Assistant, and streaming to it with Music Assistant.

### Physical Setup

Run a 3.5mm cable from the CAST-1 into the line-in on your powered speakers, receiver, or active soundbar, then plug the CAST-1 into power with USB-C. A 5V 1A power supply is plenty. (1)
{ .annotate }

1.  The CAST-1 has no amplifier of its own, so it needs powered speakers or an amp. If your speakers use RCA or 6.35mm inputs, use a 3.5mm-to-RCA or 3.5mm-to-6.35mm adapter cable.

![](/assets/cast-1-physical-setup.webp)

### Connect to Your Network

There are three ways to get your CAST-1 online. Pick whichever is easier, you only need to do one.

- **Hotspot** works on any phone or computer. The CAST-1 broadcasts its own Wi-Fi network, you join it, then enter your Wi-Fi details. No extra hardware needed.
- **Improv via BLE** sets the CAST-1 up over Bluetooth straight from Home Assistant. It's quick, but it needs Bluetooth on your Home Assistant host or an ESP32 Bluetooth proxy.
- **Ethernet** is for a CAST-1 with the Ethernet add-on module fitted. It connects over a network cable straight to your router or switch.

=== "Hotspot"

    1\. Plug the CAST-1 in via USB-C. A 5V 1A power supply will work fine.

    !!! success "If your CAST-1 is restarting or not broadcasting Wi-Fi try another USB-C cable and power supply!"

        The CAST-1 is sensitive to power fluctuations and needs constant 5V power. Most quality phone chargers will work fine.

        Still no hotspot? Follow the <a href="https://wiki.apolloautomation.com/products/cast1/troubleshooting/cast1-reset-wi-fi-credentials/" target="_blank" rel="noopener">Reset Wi-Fi Credentials</a> guide to make it broadcast again.

    2\. On your phone or PC, open the Wi-Fi settings and connect to "**Apollo CAST 1 Hotspot**". Once connected it should automatically open a dashboard for your CAST-1. If it doesn't, open your web browser and go to [http://192.168.4.1](http://192.168.4.1)

    3\. Select the Wi-Fi network that you would like your CAST-1 to connect to and type in your Wi-Fi password, then click "**Save**".

    ![](/assets/cast-1-connect-to-hotspot.webp)

    4\. Once connected, the dashboard will automatically close. You've successfully connected your CAST-1 to your Wi-Fi.

=== "Improv via BLE"

    !!! note "Pre-requirement: Bluetooth proxy or Bluetooth Home Assistant hardware required"

        Bluetooth built in such as a Raspberry Pi or at least one <a href="https://wiki.apolloautomation.com/products/general/setup/bluetooth-proxy/" target="_blank" rel="noreferrer nofollow noopener">ESP32 BLE Proxy</a> is required to use this to setup your Apollo device.

    1\. Open your integrations page in Home Assistant.

    <a href="https://my.home-assistant.io/redirect/integrations/" target="_blank" rel="noreferrer noopener"><img src="https://my.home-assistant.io/badges/integrations.svg" alt="Open your Home Assistant instance and show your integrations."></a>

    2\. Click the **Add** button on your discovered CAST-1, type in your Wi-Fi SSID and password, then click **Submit**.

    3\. Click **Submit** again, give it an **Area**, then click **Finish**.

    ![](/assets/cast-1-add-via-improv-ble.gif)

    Improv adds your CAST-1 to Home Assistant as part of setup, so skip ahead to [installing Music Assistant](#music-assistant).

=== "Ethernet"

    Wired setup needs the <a href="https://wiki.apolloautomation.com/products/cast1/addons/ethernet-module/" target="_blank" rel="noopener">Ethernet module</a> fitted and your CAST-1 running the Ethernet firmware.

    With the CAST-1 unplugged, line the module's pins up with the two rows of female header pins on top of the case, pin side down, and press it straight down until it sits flat.

    ![](/assets/cast-1-connect-ethernet-module.webp)

    1\. Every CAST-1 ships on Wi-Fi firmware, so flash yours over to Ethernet first. Follow the <a href="https://wiki.apolloautomation.com/products/cast1/troubleshooting/cast1-reflash/" target="_blank" rel="noopener">reflashing guide</a> and select **Ethernet** under **Variant**.

    2\. Plug an Ethernet cable into the module, then plug the CAST-1 into power.

    3\. Your CAST-1 picks up an address from your router on its own, so there's nothing to enter.

    4\. Home Assistant discovers your CAST-1 automatically. Add it below, then check the **IP Address** sensor on the device page to confirm the wired connection came up.

### Add to Home Assistant

Open the ESPHome Integration, then click **Add** and **Submit**. Edit the name and choose an **Area** then click **Finish**.

<a href="https://my.home-assistant.io/redirect/integration/?domain=esphome" target="_blank" rel="noreferrer noopener"><img src="https://my.home-assistant.io/badges/integration.svg" alt="Open your Home Assistant instance and show the ESPHome integration."></a>

![](/assets/cast-1-home-assistant-integration.gif)

### Music Assistant

The CAST-1 streams through <a href="https://www.music-assistant.io/" target="_blank" rel="noreferrer nofollow noopener">Music Assistant</a>. Once Music Assistant is running, your CAST-1 shows up as a player automatically, no extra configuration needed.

###### Install Music Assistant

1\. Head to the App Store to install Music Assistant.

<a href="https://my.home-assistant.io/redirect/supervisor_addon/?addon=d5369777_music_assistant&repository_url=https%3A%2F%2Fgithub.com%2Fmusic-assistant%2Fhome-assistant-addon" target="_blank" rel="noreferrer noopener"><img src="https://my.home-assistant.io/badges/supervisor_addon.svg" alt="Open your Home Assistant instance and show the Music Assistant Server add-on."></a>

2\. Click **Install**, then click **Start** once it finishes.

![](/assets/cast-1-start-music-assistant.gif)

3\. Home Assistant discovers the Music Assistant integration automatically. Open your integrations page, find **Music Assistant**, then click **Add** and **Submit**.

<a href="https://my.home-assistant.io/redirect/integrations/" target="_blank" rel="noreferrer noopener"><img src="https://my.home-assistant.io/badges/integrations.svg" alt="Open your Home Assistant instance and show your integrations."></a>

###### Stream To Your CAST-1

1\. Open **Music Assistant** from the Home Assistant sidebar.

2\. Your CAST-1 appears in the player list in Music Assistant. Select it as your player.

3\. Pick any song, playlist, or radio station and it plays through the speakers connected to your CAST-1.

![](/assets/cast-1-play-song.gif)

###### Play In Multiple Rooms

Have more than one CAST-1? Group them to play the same music in sync across every room.

1\. In Music Assistant, open the player you're listening on.

2\. Click the group/sync button and select the other CAST-1 players you want to join.

3\. All grouped CAST-1 players now play the same audio together. Adjust the volume for the whole group or per player.

![](/assets/cast-1-play-in-multiple-rooms.gif)

[Add a WizMote for physical playback control! :material-remote:](https://wiki.apolloautomation.com/products/cast1/examples/wizmote-blueprint/){ .md-button .md-button--primary }
