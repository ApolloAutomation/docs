---
title: Adding the button module
description: >-
  Wire up the ESPHome Starter Kit button module, add it through ESPHome Device
  Builder, and verify presses in the web server.
---
# Adding the button module

The button module is the first input your starter kit gets, and the fastest way to feel ESPHome respond to a physical action. By the end of this tutorial you'll have the button wired to your ESP32-C6, surfaced as a binary sensor in your YAML, and toggling live in the web server when you press it.

!!! note "Before you start"

    Work through the two prerequisites first:

    - [First Steps](../first-steps/) to snap the button module off the panel.
    - [Getting Started](../setup/getting-started/) to install ESPHome Device Builder and create your starter kit device.

## Start with your base config

The starter kit project template gets you online, but it doesn't enable the web server yet. Add it now so you have a live page to test the button against after flashing.

1. In ESPHome Device Builder, open your starter kit device and click **Edit**.
2. Add the `web_server` component, making sure to select version 3.
3. Click **Save**. Don't install yet, the button gets added in the next section.

![](../../../assets/webserver.gif)

## Plug in the button module

Connect the button module to the ESP32-C6 using one of the FPC ribbon cables that came with the kit. Either FPC connector on the C6 works, top or bottom.

1. Unplug the USB-C cable from the ESP32-C6 so the board is powered off.
2. Flip up the latch on the FPC connector on both the C6 and the button module.
3. Slide one end of the ribbon cable into each connector with the contacts facing the board, then press each latch back down to lock the cable in.
4. Plug the C6 back into your computer.

**GIF PLACEHOLDER**

!!! warning "Handle the FPC connectors gently" The latches are small and the ribbon cable is fragile. Lift the latch with a fingernail, slide the cable in, and press the latch down. Never pull on the cable itself.

## Add the button component in ESPHome Device Builder

ESPHome Device Builder ships an Add Component flow that knows the pin layout for every Apollo Starter Kit module. Use it instead of writing the binary sensor by hand, and you'll get the right GPIO and inversion settings on the first try.

1. Open your starter kit device in Device Builder and click **Edit**.
2. Click **Add Component** in the editor toolbar.
3. Search for **Button** and select the Apollo Starter Kit button component.
4. Click **Add**. Device Builder inserts the button's binary sensor block into your YAML.

![](../../../assets/button_component.gif)

??? note "What the button YAML does"

    The block Add Component drops into your config looks like this:

    ```yaml
    binary_sensor:
      - platform: gpio
        pin:
          number: GPIO6
          inverted: true
          mode:
            input: true
            pullup: true
        id: my_button
        name: "Button"
    ```

    Each option does something specific:

    | Option | What it does |
    | --- | --- |
    | `platform: gpio` | Reads a digital input on a GPIO pin. |
    | `number: GPIO6` | The pin the button module's FPC connector wires to on the ESP32-C6. |
    | `inverted: true` | The pin reads LOW when the button is pressed, so this flips it to an intuitive on/off state. |
    | `mode.input: true` | Configures the pin as an input. |
    | `mode.pullup: true` | Enables the C6's internal pull-up so the pin doesn't float when the button isn't pressed. |
    | `id: my_button` | Internal handle you can reference from automations and lambdas elsewhere in the config. |
    | `name: "Button"` | The friendly name shown in Home Assistant and the web server. |

## Install the firmware

Flash the device so the new web server and button entity go live.

1. Click **Install** on your device card in ESPHome Device Builder.
2. Choose **Plug into the computer running ESPHome Device Builder** for the first flash, or **Wirelessly** if the device is already on your Wi-Fi.
3. Wait for the compile and flash to finish. First builds can take a few minutes.
4. The device reboots and reconnects to your Wi-Fi on its own.

**GIF PLACEHOLDER**

## Test it in the web server

With the device back online, the button entity is live on the web server. Open it in a browser on the same network and watch it react in real time.

1. In a browser, open `http://<your-device-name>.local/`. If you used `esphome-starter-kit` as the device name in Getting Started, that's `http://esphome-starter-kit.local/`.
2. Find the **Button** entity in the binary sensor list.
3. Press the button on the module. The entity flips from **OFF** to **ON** while the button is held, then back to **OFF** when you release it.

> Web server page showing the Button binary sensor toggling between ON and OFF as the button is pressed.

**GIF PLACEHOLDER**

!!! success "Your button module is wired up"
