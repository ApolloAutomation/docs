---
title: Adding the motion module
description: >-
  Wire up the ESPHome Starter Kit button module, add it through ESPHome Device
  Builder, and verify presses in the web server.
---
# Adding the PIR motion module

The PIR motion module turns your starter kit into a motion sensor. By the end of this tutorial you'll have an MH-SR602 wired to your ESP32-C6, surfaced as a binary sensor in your YAML, and flipping live in the web server whenever something moves in front of it.

!!! note "Before you start"

    Work through the two prerequisites first:

    - [First Steps](../first-steps/) to snap the PIR motion module off the panel.
    - [Getting Started](../setup/getting-started/) to install ESPHome Device Builder and create your starter kit device.

## Start with your base config

The starter kit project template gets you online, but it doesn't enable the web server yet. Add it now so you have a live page to test the sensor against after flashing.

1. In ESPHome Device Builder, open your starter kit device and click **Edit**.
2. Add the `web_server` component, making sure to select version 3.
3. Click **Save**. Don't install yet, the sensor gets added in the next section.

## Install the PIR sensor into the module

The PIR sensor (the small white dome on a tiny PCB) ships separately from the PIR module board so it can be packed safely. Install it onto the module before plugging anything into the C6.

1. Take the PIR sensor out of the box.
2. Line up its pins with the matching headers on the PIR module board.
3. Press it down firmly until the pins are fully seated.

**GIF PLACEHOLDER**

## Plug in the PIR motion module

Connect the PIR motion module to the ESP32-C6 using one of the FPC ribbon cables that came with the kit. Either FPC connector on the C6 works, top or bottom.

1. Unplug the USB-C cable from the ESP32-C6 so the board is powered off.
2. Flip up the latch on the FPC connector on both the C6 and the PIR motion module.
3. Slide one end of the ribbon cable into each connector with the contacts facing the board, then press each latch back down to lock the cable in.
4. Plug the C6 back into your computer.

**GIF PLACEHOLDER**

!!! warning "Handle the FPC connectors gently" The latches are small and the ribbon cable is fragile. Lift the latch with a fingernail, slide the cable in, and press the latch down. Never pull on the cable itself.

## Add the PIR motion component in ESPHome Device Builder

ESPHome Device Builder ships an Add Component flow that knows the pin layout for every Apollo Starter Kit module. Use it instead of writing the binary sensor by hand, and you'll get the right GPIO and pin mode on the first try.

1. Open your starter kit device in Device Builder and click **Edit**.
2. Click **Add Component** in the editor toolbar.
3. Search for **PIR** and select the Apollo Starter Kit PIR motion component.
4. Click **Add**. Device Builder inserts the PIR's binary sensor block into your YAML.

??? note "What the PIR YAML does"

    The block Add Component drops into your config looks like this:

    ```yaml
    binary_sensor:
      - platform: gpio
        pin:
          number: GPIO3
          mode:
            input: true
            pulldown: false
        id: io_pir
        name: "PIR"
        device_class: motion
    ```

    Each option does something specific:

    | Option | What it does |
    | --- | --- |
    | `platform: gpio` | Reads a digital input on a GPIO pin. |
    | `number: GPIO3` | The pin the PIR module's FPC connector wires to on the ESP32-C6. |
    | `mode.input: true` | Configures the pin as an input. |
    | `mode.pulldown: false` | The MH-SR602 drives its output both high and low on its own, so no internal pulldown is needed. |
    | `id: io_pir` | Internal handle you can reference from automations and lambdas elsewhere in the config. |
    | `name: "PIR"` | The friendly name shown in Home Assistant and the web server. |
    | `device_class: motion` | Tells Home Assistant this is a motion sensor, so it shows the right icon and works in motion-related templates and blueprints. |

## Install the firmware

Flash the device so the new web server and PIR entity go live.

1. Click **Install** on your device card in ESPHome Device Builder.
2. Choose **Plug into the computer running ESPHome Device Builder** for the first flash, or **Wirelessly** if the device is already on your Wi-Fi.
3. Wait for the compile and flash to finish. First builds can take a few minutes.
4. The device reboots and reconnects to your Wi-Fi on its own.

**GIF PLACEHOLDER**

## Test it in the web server

With the device back online, the PIR entity is live on the web server. Open it in a browser on the same network and watch it react.

1. In a browser, open `http://<your-device-name>.local/`. If you used `esphome-starter-kit` as the device name in Getting Started, that's `http://esphome-starter-kit.local/`.
2. Find the **PIR** entity in the binary sensor list.
3. Wave your hand in front of the sensor. The entity flips from OFF to ON while motion is detected, then back to OFF a few seconds after motion stops.

!!! tip "Give the PIR a moment to settle" PIR sensors need a brief warm-up after powering on, usually 5 to 10 seconds, before their readings stabilize. If the sensor reports motion right after boot even when nothing is moving, give it a moment.

> Web server page showing the PIR binary sensor toggling between ON and OFF as motion is detected.

**GIF PLACEHOLDER**

!!! success "Your PIR motion module is wired up"