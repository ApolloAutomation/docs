---
title: Adding the motion module
description: Wire up the ESPHome Starter Kit motion module to turn your kit into an accurate motion sensor.
---

The motion module turns your starter kit into a motion sensor. By the end of this tutorial you'll have an MH-SR602 wired to your ESP32-C6, surfaced as a binary sensor in your YAML, and flipping live in the web server whenever something moves in front of it.

!!! note "Before you start"

    Work through the two prerequisites first.

    - [Start here](../start-here.md) to snap the motion module off the panel.
    - [First steps](../setup/first-steps.md) to install ESPHome Device Builder and create your starter kit device.

## Prerequisite, enable the Web Server

The <a href="https://esphome.io/components/web_server/" target="_blank" rel="noreferrer nofollow noopener">Web Server</a> broadcasts a local website from your device. That lets you navigate to the device's IP address or hostname (for example <a href="http://esphome-starter-kit.local/" target="_blank" rel="noreferrer nofollow noopener">esphome-starter-kit.local</a>) to control it from any browser on your network.

1. In the ESPHome Device Builder, navigate to the **Core configuration** section.
2. Click **Add component**.
3. Scroll to **Web Server** and click **Add**.
4. Click **Add** once more to confirm.
5. Toggle **Show advanced settings**.
6. Scroll down to **Version** and select **3** from the dropdown.

![Installing the Web Server v3 component in ESPHome Device Builder](../../../assets/device-builder-install-web-server-v3.gif)

## Attach the PIR

The PIR sensor (the small white dome on a tiny PCB) ships separately from the motion module so it can be packed safely. Install it onto the module before plugging anything into the C6.

1. Take the PIR sensor out of the box.
2. Line up the **Out** label on each side as shown in the animation below.
3. Press it down firmly until the pins are fully seated.

![Pressing the PIR sensor onto the motion module PCB lining up the Out labels](../../../assets/esphome-starter-kit-attach-pir-to-motion-module.webp)

## Attach the motion module

Connect the motion module to the ESP32-C6 using one of the FPC ribbon cables that came with the kit. Either FPC connector on the C6 works, top or bottom.

1. Unplug the USB-C cable from the ESP32-C6 so the board is powered off.

    ![Unplugging the USB-C cable from the ESP32-C6 main board](../../../assets/esphome-starter-kit-remove-usb.webp)

2. Flip up the latch on the FPC connector, then gently slide the ribbon cable into the connector. Gently press the latch down to lock it in place.

    ![Inserting the FPC ribbon cable into the top FPC connector on the ESP32-C6](../../../assets/esphome-starter-kit-attach-top-fpc-ribbon.webp)

3. Slide the ribbon cable into the motion module with the blue side facing upwards, then press the latch down to lock it in place.

    ![Attaching the FPC ribbon cable to the motion module with the blue side up](../../../assets/esphome-starter-kit-attach-fpc-to-motion-module.webp)

4. Plug the C6 back into your computer.

!!! warning "Handle the FPC connectors gently"

    The latches are small and the ribbon cable is fragile. Lift the latch with a fingernail, slide the cable in, and press the latch down. Never pull on the cable itself.

## Add the motion sensor in ESPHome Device Builder

ESPHome Device Builder ships an **Add Component** flow that knows the pin layout for every Apollo Starter Kit module. Use it instead of writing the binary sensor by hand, and you'll get the right GPIO and pin mode on the first try.

1. Open your starter kit device in Device Builder and click **Edit**.
2. Click **Add Component** in the editor toolbar.
3. Search for **Motion** and select the Apollo Starter Kit PIR motion component.
4. Click **Add**. Device Builder inserts the PIR's binary sensor block into your YAML.

![Adding the motion component in ESPHome Device Builder](../../../assets/esphome-device-builder-add-motion-component.gif)

??? note "What the motion YAML does"

    The block Add Component drops into your config looks like this.

    ```yaml
    binary_sensor:
      - platform: gpio
        name: Motion Module
        pin: 3
        device_class: motion
        id: motion_module
    ```

    Each option does something specific.

    | Option | What it does |
    | --- | --- |
    | `platform: gpio` | Reads a digital input on a GPIO pin. |
    | `pin: 3` | The pin the motion module's FPC connector wires to on the ESP32-C6. |
    | `device_class: motion` | Tells Home Assistant this is a motion sensor, so it shows the right icon and works in motion-related templates and blueprints. |
    | `id: motion_module` | Internal handle you can reference from automations and lambdas elsewhere in the config. |
    | `name: "Motion Module"` | The friendly name shown in Home Assistant and the web server. |

## Flash the firmware

Flash the device so the new web server and motion entity go live.

1. Click **Install** on your device card in ESPHome Device Builder.
2. Choose **Plug into the computer running ESPHome Device Builder** for the first flash, or **On The Network** if the device is already on your Wi-Fi.
3. Wait for the compile and flash to finish. First builds can take a few minutes.
4. The device reboots and reconnects to your Wi-Fi on its own.

![Compiling and installing the motion module firmware in ESPHome Device Builder](../../../assets/esphome-device-builder-install-motion-component.gif)

## Test motion

With the device back online, the motion entity is live on the web server. <a href="http://esphome-starter-kit.local/" target="_blank" rel="noreferrer nofollow noopener">Open it in a browser</a> on the same network and watch it react in real time.

1. In a browser, open `http://<your-device-name>.local/`. If you used `esphome-starter-kit` as the device name in [First steps](../setup/first-steps.md), that's `http://esphome-starter-kit.local/`.
2. Find the **Motion** entity in the binary sensor list.
3. Wave your hand in front of the sensor. The entity flips from OFF to ON while motion is detected, then back to OFF a few seconds after motion stops.

!!! tip "Give the motion sensor a moment to settle"

    PIR sensors need a brief warm-up after powering on, usually 5 to 10 seconds, before their readings stabilise. If the sensor reports motion right after boot even when nothing is moving, give it a moment.

![Web server view showing the Motion binary sensor toggling ON and OFF as motion is detected](../../../assets/esphome-device-builder-test-motion-occupancy.gif)

!!! success "Your motion module is ready"

    You're now ready to build occupancy-based automations across your home.
