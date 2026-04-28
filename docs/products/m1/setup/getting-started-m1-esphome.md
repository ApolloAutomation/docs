---
title: Getting Started (ESPHome)
description: Getting started with your new M-1 running the hub75-studio ESPHome firmware
---
# Getting Started (ESPHome)

!!! tip "Running WLED-MM instead?"

    If you're using the stock WLED-MoonModules firmware that ships pre-flashed, head to the [WLED-MM Getting Started page](../getting-started-m1/) instead.

This guide walks you through replacing the stock WLED-MM firmware with [hub75-studio](https://github.com/pavlov-net/hub75-studio), an ESPHome firmware tailored for the M-1, and getting it onto your home network and into Home Assistant.

#### Attach M-1 LED Controller

Your M-1 LED Matrix and M-1 controller were shipped separately to minimize damage in shipping. Gently attach the controller to the back of the M-1 LED Matrix panel as shown in the GIF below.

![](/assets/m1-matrix-attach-controller.webp)

#### Flash the firmware

!!! success "Use the Rev6 build"

    All M-1 units currently being sold are Rev6. On the <a href="https://pavlov-net.github.io/hub75-studio/" target="_blank" rel="noreferrer nofollow noopener">hub75-studio installer</a>, select the **Rev6** firmware before clicking **Connect**.

1\. Open <a href="https://pavlov-net.github.io/hub75-studio/" target="_blank" rel="noreferrer nofollow noopener">https://pavlov-net.github.io/hub75-studio/</a> in Chrome, Edge, or another Chromium-based browser.

2\. Pick the **Rev6** firmware, click **Connect**, select the M-1's COM port, and follow the installer prompts to flash.

![](/assets/m-1-esphome-flash.gif)

#### Confirm the M-1 BIOS screen

Once the firmware finishes installing, the panel displays the **M-1 BIOS** splash showing the CPU, RAM, and the last 6 characters of the controller's MAC address. Seeing this screen confirms the firmware booted successfully. Take note of those 6 characters, you'll need them in the next step.

![](/assets/m-1-esphome-bios-screen.png)

#### Connect to Wi-Fi

1\. On your phone, open Wi-Fi settings and join the network **apollo-m1-r6-XXXXXX**, where the last 6 characters match the MAC suffix shown on the BIOS screen.

2\. The captive portal opens automatically. Either pick your home network from the scanned list and enter the password, or scroll down and type your SSID and password manually.

3\. Tap **Save**. The M-1 reboots and joins your home network.

![](/assets/m-1-esphome-captive-portal.png)

#### Join to Home Assistant

!!! tip "Your device should be auto-discovered by Home Assistant using the ESPHome Integration as shown below!"

    Head to the <a href="http://homeassistant.local:8123/config/integrations" target="_blank" rel="noreferrer nofollow noopener">Integrations page in Home Assistant</a> and accept the discovery prompt for your M-1.

![](/assets/m-1-esphome-ha-discovery.gif)

#### Optional: Adopt into ESPHome Device Builder

!!! tip "Advanced, only needed if you want to edit YAML"

    You can adopt the M-1 into the <a href="https://esphome.io/guides/getting_started_hassio.html" target="_blank" rel="noreferrer nofollow noopener">ESPHome Device Builder</a> add-on to customize its YAML configuration (custom effects, additional sensors, etc.). This is **not required** for normal use, skip this section unless you specifically want to edit the firmware configuration.
