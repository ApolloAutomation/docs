---
title: Control an LED strip with the GPIO Header
description: Wire a WS2812B LED strip to the AIR-1 GPIO Header and control it from Home Assistant.
---
# Control an LED strip with the GPIO Header

The GPIO Header addon brings the AIR-1's spare pins out to a row of headers, so you can hang your own hardware off the sensor. This guide wires a WS2812B strip to one of those pins and gets it into Home Assistant as its own light entity, color picker and effects included.

Click any photo to see it full size.

## What you need

- An [Apollo AIR-1](https://apolloautomation.com/products/air-1).
- The [Apollo GPIO Header](https://apolloautomation.com/products/msr-2-gpio-header) addon, which ships with a replacement AIR-1 lid.
- A WS2812B (neopixel) RGB strip. SK6812 RGBW strips work too.
- Three male-to-male DuPont wires. A set comes with the header.
- A USB-C cable and power brick.

!!! warning "Watch the current draw"

    The 5V pin supplies up to 300mA. A meter of 60 LEDs at full white draws far more than that, so anything longer than a short strip needs its own 5V supply. You can power the AIR-1 itself from the 5V and GND pins instead of the USB-C port, but use one or the other, never both.

## Choosing a data pin

IO2, IO4, IO6, and IO7 are free for LED data, and you can drive more than one strip by giving each its own pin. IO18 and IO19 are unavailable, and IO0 and IO1 are reserved for I2C sensors. This guide uses **IO7**, plus the 5V and GND pins at the top of the header for power.

![Pinout diagram of the Apollo GPIO Header showing the 5V, GND, and IO pins](/assets/gpio-header-pinout.webp){ width="480" }

## Attaching the GPIO Header

Opening an AIR-1 takes a few more steps than the other Apollo sensors, because the PCB slides out of the case. The [GPIO Header addon page](/products/air1/addons/adding-gpio-header-to-air-1.md) has photos of each one.

1.  Unplug the AIR-1, lift the lid off, and slide the PCB out to the left.

2.  Flip the PCB over and find the small black mezzanine connector in the top right corner. An X marks the corner, and the GPIO Header has a matching X on its own board.

    ![Mezzanine connector on the back of the AIR-1 PCB with the X marking](/assets/air-1-gpio-header-wiki-pic-1.webp){ width="200" } ![The matching X marking on the GPIO Header board](/assets/air-1-gpio-header-wiki-pic-2.webp){ width="200" }

3.  Line the two X markings up and press the header gently onto the connector.

    ![GPIO Header aligned over the AIR-1 mezzanine connector](/assets/air-1-gpio-header-wiki-pic-3.webp){ width="200" } ![GPIO Header being pressed onto the connector](/assets/air-1-gpio-header-wiki-pic-4.webp){ width="200" } ![GPIO Header fully seated on the AIR-1 PCB](/assets/air-1-gpio-header-wiki-pic-5.webp){ width="200" }

4.  Flip the PCB back over and slide it into the new lid that came with the addon. There are three channels in the plastic for it to run in, so it should go most of the way with light pressure.

    ![AIR-1 PCB sliding into the replacement GPIO lid](/assets/air-1-gpio-header-wiki-pic-6.webp){ width="200" } ![PCB seated in the channels of the new lid](/assets/air-1-gpio-header-wiki-pic-7.webp){ width="200" }

5.  Push the case back together.

    ![AIR-1 case being closed around the new lid](/assets/air-1-gpio-header-wiki-pic-8.webp){ width="200" } ![AIR-1 case closing with the GPIO Header inside](/assets/air-1-gpio-header-wiki-pic-9.webp){ width="200" } ![Reassembled AIR-1 with the GPIO Header pins exposed](/assets/air-1-gpio-header-wiki-pic-10.webp){ width="200" }

## Wiring the strip

1.  Run three wires from the header to the strip: 5V, GND, and data. Matching the colors to the strip's own wiring saves a lot of squinting later, so use red for 5V, white for GND, and green for data on IO7.

    ![Red, white, and green DuPont wires laid out next to the GPIO Header](/assets/gpio-led-dupont-wires-1.webp){ width="200" } ![DuPont wires pushed onto the 5V, GND, and IO7 pins](/assets/gpio-led-dupont-wires-2.webp){ width="200" } ![Close-up of the three wires seated on the GPIO Header](/assets/gpio-led-dupont-wires-3.webp){ width="200" }

2.  Plug the other end into the strip. Most strips come with a JST-SM pigtail carrying the same three colors, so the wires match up directly. The connector is rated to 3A.

    ![JST-SM connector on the end of a WS2812B strip](/assets/gpio-led-strip-jst-1.webp){ width="200" } ![DuPont wires plugged into the strip's JST-SM connector](/assets/gpio-led-strip-jst-2.webp){ width="200" }

3.  Check the direction before you power anything on. Arrows printed along the strip show which way data flows, and they need to point away from the AIR-1.

    ![Direction arrow printed on the LED strip pointing away from the sensor](/assets/gpio-led-strip-arrow-1.webp){ width="200" } ![The wired end of the strip with the arrow running down its length](/assets/gpio-led-strip-arrow-2.webp){ width="200" }

A dab of hot glue across the outer shells of the three DuPont connectors stiffens them into a single plug. (1)
{ .annotate }

1.  Keep glue out of the header's female pins. It will ruin the addon.

![Hot glue joining the outer shells of three DuPont connectors](/assets/gpio-led-dupont-hot-glue.webp){ width="200" }

## Adding the strip to your YAML

The AIR-1 knows nothing about the strip until you tell it how many LEDs there are and which pin they sit on.

1.  Open the **ESPHome Device Builder** app, find your AIR-1, and click **Edit**.

    ![The ESPHome Device Builder editor open on an Apollo device configuration](/assets/gpio-led-esphome-edit.webp){ width="480" }

2.  Add the block below at the bottom of the file, flush with the left margin so `light:` lines up with `packages:` and `wifi:`. Set `num_leds` to the number of LEDs on your strip, and change `pin` if you wired to a different port.

    ```yaml
    light:
      - platform: esp32_rmt_led_strip
        id: bed_led
        name: "Bed LED"
        pin: GPIO7
        chipset: WS2812
        rgb_order: grb
        num_leds: 60
        default_transition_length: 0s
        effects:
          - pulse:
              name: "Slow Pulse"
              transition_length: 1000ms
              update_interval: 1000ms
              min_brightness: 50%
              max_brightness: 100%
          - pulse:
              name: "Fast Pulse"
              transition_length: 100ms
              update_interval: 100ms
              min_brightness: 50%
              max_brightness: 100%
          - addressable_rainbow:
    ```

3.  Check that the editor shows no red error markers.

    ![The ESPHome editor showing the new light block with no errors flagged](/assets/gpio-led-esphome-no-errors.webp){ width="300" }

4.  Click **Save**, then **Install**, and pick **Wirelessly**. ESPHome compiles the firmware and sends it to the AIR-1. The first build takes a few minutes.

Older versions of this guide set `rmt_channel: 1` on the light. ESPHome dropped that option, and leaving it in now fails validation, so the block above does not use it.

The [ESPHome light effects reference](https://esphome.io/components/light/index.html#light-effects) covers everything else you can add under `effects:`, including `addressable_scan`.

## Controlling it from Home Assistant

Once the install finishes, the AIR-1 exposes a new light entity called **Bed LED**.

![The Bed LED entity listed on the device page in Home Assistant](/assets/gpio-led-ha-entity.webp){ width="500" }

Click the entity name to open the light card. The color wheel covers the full range, and the effects list holds the two pulses and the rainbow from the YAML above.

![Home Assistant light card for Bed LED](/assets/gpio-led-ha-color-picker.webp){ width="190" } ![Color wheel open on the Bed LED card](/assets/gpio-led-ha-color-wheel.webp){ width="195" } ![Effect list showing Slow Pulse, Fast Pulse, and rainbow](/assets/gpio-led-ha-effect-list.webp){ width="190" }

![WS2812B strip lit up in color behind a bed](/assets/gpio-led-strip-lit.webp){ width="260" }

That's all folks! Thanks to Smart Home Sellout for putting this tutorial together.
