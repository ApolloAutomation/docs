---
title: Adding the Apollo Starter Module
description: >-
  Wire up the ESPHome Starter Kit Breakout Module, add it through ESPHome Device
  Builder, and verify it in the web server.
---
# Adding the Apollo Starter Module

The Breakout Module gives your starter kit room to grow. It breaks the ESP32-C6's pins out so you can wire up your own parts, the components the kit doesn't include. By the end of this tutorial you'll have it attached to your ESP32-C6 and be ready to build something of your own.

!!! note "More detail coming soon"

    This page covers the basics for getting the Breakout Module attached and online. We'll fill out the module-specific wiring, pinout, and example automations in a follow-up update.

!!! note "Before you start"

    Work through the two prerequisites first:

    * [Start Here](/products/ESPHome-Starter-Kit/start-here/) to snap the module off the panel.
    * [First Steps](/products/ESPHome-Starter-Kit/setup/first-steps/) to install ESPHome Device Builder and create your starter kit device.

#### Prerequisite

The <a href="https://esphome.io/components/web_server/" target="_blank" rel="noreferrer nofollow noopener">Web Server</a> is used to broadcast a local website using your device. This allows you to navigate to the IP address of your device or hostname such as <a href="http://esphome-starter-kit.local/" target="_blank" rel="noreferrer nofollow noopener">esphome-starter-kit.local</a> to easily control your new device!

1. In the ESPHome Device Builder, navigate to the **Core configuration** section.
2. Click **Add component**.
3. Scroll to **Web Server** and click **Add**.
4. Click **Add** once more to confirm.
5. Toggle **Show advanced settings**.
6. Scroll down to **Version** and select **3** from the dropdown.

![](../../../assets/device-builder-install-web-server-v3.gif)

## Attach Breakout module

Connect the Breakout Module to the ESP32-C6 using one of the FPC ribbon cables that came with the kit. Either FPC connector on the ESP32-C6 works, top or bottom.

1\. Unplug the USB-C cable from the ESP32-C6 so it is powered off.

![](../../../assets/esphome-starter-kit-remove-usb.webp)

!!! warning "Handle the FPC connectors gently"

    The latches are small and the ribbon cable is fragile. Lift the latch with a fingernail, slide the cable in, and press the latch down. Never pull on the cable itself.

2\. Flip up the latch on the FPC connector then gently slide the ribbon cable in to the connector. Gently press the latch down to lock it in place.

![](../../../assets/esphome-starter-kit-attach-top-fpc-ribbon.webp)

3\. Slide the ribbon cable into the Breakout Module with the blue side facing upwards then press the latch down to lock it in place.

4\. Plug the ESP32-C6 back into your computer.

## Wire up your own components

The Breakout Module is different from the other starter kit modules. Instead of a single fixed sensor with a ready-made component in Device Builder, it breaks the ESP32-C6's pins out to the module so you can wire up your own buttons, sensors, LEDs, and other parts. This is the module for tinkering and building something that isn't in the kit.

Because the wiring is up to you, there's no **Add Component** entry to select. You decide what to connect, then add the matching ESPHome component to your YAML by hand. The <a href="https://esphome.io/components/" target="_blank" rel="noreferrer nofollow noopener">ESPHome component index</a> lists every supported sensor, switch, light, and more, along with the config each one needs.

!!! note "Pinout coming soon"

    We'll add the Breakout Module pinout (which module pin maps to which ESP32-C6 GPIO) and a worked example or two once the module-specific docs are ready. For now, match your wiring to the GPIO numbers in your component's ESPHome config.

## Install the firmware

Once you've added the component for whatever you wired up, flash the device so your changes go live.

1. Click **Install** on your device card in ESPHome Device Builder.
2. Choose **Plug into the computer running ESPHome Device Builder** for the first flash, or **On The Network** if the device is already on your Wi-Fi.
3. Wait for the compile and flash to finish. First builds can take a few minutes.
4. The device reboots and reconnects to your Wi-Fi on its own.

## Test your wiring

With the device back online, whatever you wired up shows up on the web server alongside your other entities. <a href="http://esphome-starter-kit.local/" target="_blank" rel="noreferrer nofollow noopener">Open it in a browser</a> on the same network and watch it react in real time.

1. In a browser, open `http://<your-device-name>.local/`. If you used `esphome-starter-kit` as the device name in Getting Started, that's `http://esphome-starter-kit.local/`.
2. Find the entity for the component you added in the list.
3. Trigger it (press your button, cover your sensor, and so on) and watch the value update.

!!! success "Your Breakout Module is wired up and ready!"

    From here, the Breakout Module is your sandbox. Mix in any ESPHome component and build something that's all your own.

--8<-- "_snippets/community-help.md"
