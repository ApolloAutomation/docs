---
title: CAST-1 Getting Started Guide
description: Step by step guide to getting started with your CAST-1!
---
# CAST-1 Getting Started

This will guide you through connecting your CAST-1 to your speakers, adding it to your Wi-Fi and Home Assistant, and streaming to it with Music Assistant.

### Physical Setup

###### Connect Your Speakers

The CAST-1 outputs line-level audio over its 3.5mm port. Run a 3.5mm cable from the CAST-1 into the line-in on your powered speakers, receiver, or active soundbar. (1)
{ .annotate }

1.  The CAST-1 has no amplifier of its own, so it needs powered speakers or an amp. If your speakers use RCA or 6.35mm inputs, use a 3.5mm-to-RCA or 3.5mm-to-6.35mm adapter cable.

![](/assets/cast-1-connect-speakers-gif.webp)

###### Power It On

Plug the CAST-1 in via USB-C. A 5V 1A power supply is plenty.

![](/assets/cast-1-power-on.webp)

### Connecting Through Hotspot

To connect through the CAST-1's onboard hotspot follow the below:

1\. Plug the CAST-1 in via USB-C. A 5V 1A power supply will work fine.

!!! success "If your CAST-1 is restarting or not broadcasting Wi-Fi try another USB-C cable and power supply!"

    The CAST-1 is sensitive to power fluctuations and needs constant 5V power. Most quality phone chargers will work fine.

    Still no hotspot? Follow the <a href="https://wiki.apolloautomation.com/products/cast1/troubleshooting/cast1-reset-wi-fi-credentials/" target="_blank" rel="noopener">Reset Wi-Fi Credentials</a> guide to make it broadcast again.

2\. On your phone or PC, open the Wi-Fi settings and connect to "**Apollo CAST 1 Hotspot**".

![](/assets/cast-1-hotspot-wifi-list.png)

3\. Once connected it should automatically open a dashboard for your CAST-1. If this does not automatically open, please open your web browser and go to [http://192.168.4.1](http://192.168.4.1)

4\. Select the Wi-Fi network that you would like your CAST-1 to connect to or scroll to the bottom and type in your Wi-Fi network then click "**Save**".

![](/assets/cast-1-hotspot-enter-wifi.png)

!!! tip "Tip for Mesh Wi-Fi systems or multiple Access Points"

    If you have multiple access points or a mesh system please manually type in your Wi-Fi network so it will join with the strongest signal!

5\. Once connected, the dashboard will automatically close. You've successfully connected your CAST-1 to your Wi-Fi.

[Click here for next steps!](https://wiki.apolloautomation.com/products/cast1/setup/getting-started/#connecting-to-home-assistant-via-esphome-integration){ .md-button .md-button--primary }

### Connecting with <a href="https://www.home-assistant.io/integrations/improv_ble" target="_blank" rel="noopener">Improv via BLE</a>

!!! note "Pre-requirement: Bluetooth proxy or Bluetooth Home Assistant hardware required"

    Bluetooth built in such as a Raspberry Pi or at least one <a href="https://wiki.apolloautomation.com/products/general/setup/bluetooth-proxy/" target="_blank" rel="noreferrer nofollow noopener">ESP32 BLE Proxy</a> is required to use this to setup your Apollo device. If you have already followed the "Connecting through Hotspot" please skip this section.

1\. Navigate to **Settings -> Devices & Services** then click the "**ADD**" button below your new Apollo device then click **Submit**.

![](/assets/cast-1-improv-ble-add.gif)

2\. Once prompted, type in your Wi-Fi name and password in the two fields then click **Submit**. Click on **Close** once it finishes.

![](/assets/cast-1-improv-ble-wifi-setup.gif)

3\. Click on **Add** then click on **Submit**. Choose an area and then click **Finish**.

![](/assets/cast-1-improv-ble-esphome-integration.gif)

4\. Your device is now added to your Wi-Fi and to the ESPHome Integration in Home Assistant. You're ready to stream to it with Music Assistant below!

### Connecting To ESPHome Device Builder

!!! tip "Skip the ESPHome Device Builder unless..."

    Feel free to skip to the [ESPHome Integration section](https://wiki.apolloautomation.com/products/cast1/setup/getting-started/#connecting-to-home-assistant-via-esphome-integration) unless you need to rename your CAST-1 or make manual edits to the YAML.

You can add the ESPHome Device Builder app in Home Assistant to easily update your device or edit the YAML. If you don't have the ESPHome Device Builder app installed you can <a href="http://homeassistant.local:8123/hassio/store" target="_blank" rel="noreferrer nofollow noopener">search ESPHome Device Builder in the App Store</a> and install it.

Make sure to fill out your Wi-Fi details in the **secrets** section by clicking on the **secrets** button.

![](/assets/esphome-device-builder-secrets.png)

```yaml
# Your Wi-Fi SSID and password - keep the quotes and just replace the name and password between the quotes!
wifi_ssid: "your-wifi-ssid-here"
wifi_password: "your-wifi-pass-here"
```

1\. Open the <a href="http://homeassistant.local:8123/5c53de3b_esphome/ingress" target="_blank" rel="noreferrer nofollow noopener"><strong>ESPHome Device Builder</strong></a> dashboard.

![](/assets/esphome-device-builder-show-discovered-device.png)

2\. Click **Show** in the top right to show your discovered devices then click on **Take Control** then click **Install**. This can take multiple minutes or longer on low-end hardware.

![](/assets/cast-1-take-control-gif.gif)

3\. Once you see "**INFO OTA successful**" you are done. Click "**STOP**" to exit.

![](/assets/cast-1-ota-successful.png)

4\. Your CAST-1 is now adopted into the ESPHome Device Builder and you can move on to the ESPHome Integration below.

### Connecting to Home Assistant via ESPHome Integration

1\. Head to the <a href="http://homeassistant.local:8123/config/integrations/integration/esphome" target="_blank" rel="noreferrer nofollow noopener">ESPHome Integration</a> then click on **Add** then click **Submit**. When prompted click **Finish**, give it a location, and click **Finish** or **Skip and Finish**.

![](/assets/cast-1-esphome-integration-gif.gif)

2\. Your CAST-1 is now added to Home Assistant via the ESPHome integration. You can find it under **Settings -> Devices & Services -> ESPHome**.

[Now stream to it with Music Assistant! :material-cast-audio:](https://wiki.apolloautomation.com/products/cast1/setup/getting-started/#playing-audio-with-music-assistant){ .md-button .md-button--primary }

### Playing Audio with Music Assistant

The CAST-1 streams through <a href="https://www.music-assistant.io/" target="_blank" rel="noreferrer nofollow noopener">Music Assistant</a>. Once Music Assistant is running, your CAST-1 shows up as a player automatically, no extra configuration needed.

###### Install Music Assistant

1\. Open the <a href="https://my.home-assistant.io/redirect/supervisor_store/" target="_blank" rel="noreferrer nofollow noopener">App Store</a> in Home Assistant (**Settings -> Add-ons -> App Store**).

2\. Search for **Music Assistant Server**, open it, then click **Install**. Once it finishes, click **Start**.

![](/assets/cast-1-music-assistant-install.png)

3\. Home Assistant will discover the Music Assistant integration automatically. Go to **Settings -> Devices & Services**, find **Music Assistant**, and click **Add** then **Submit**.

![](/assets/cast-1-music-assistant-integration.png)

###### Stream To Your CAST-1

1\. Open **Music Assistant** from the Home Assistant sidebar.

2\. Your CAST-1 appears in the player list as **Apollo CAST-1 Player**. Select it as your player.

![](/assets/cast-1-music-assistant-select-player.gif)

3\. Pick any song, playlist, or radio station and it plays through the speakers connected to your CAST-1.

###### Play In Multiple Rooms

Have more than one CAST-1? Group them to play the same music in sync across every room.

1\. In Music Assistant, open the player you're listening on.

2\. Click the group/sync button and select the other CAST-1 players you want to join.

![](/assets/cast-1-music-assistant-multiroom.gif)

3\. All grouped CAST-1 players now play the same audio together. Adjust the volume for the whole group or per player.

[Add a WizMote for physical playback control! :material-remote:](https://wiki.apolloautomation.com/products/cast1/examples/wizmote-blueprint/){ .md-button .md-button--primary }
