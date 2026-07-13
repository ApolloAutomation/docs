---
title: Temperature Probe
description: >-
  Add a waterproof DS18B20 temperature probe to your ESPHome Starter Kit
  Breakout Module using the 1Wire port.
---
# Temperature Probe

A waterproof <a href="https://cdn-shop.adafruit.com/datasheets/DS18B20.pdf" target="_blank" rel="noreferrer nofollow noopener">DS18B20</a> temperature probe plugs into the Breakout Module's 1Wire port and reads temperature from wherever you run the cable, a fridge, a freezer, a fish tank, outdoors. It's the same probe our [TEMP-1](/products/temp1/introduction.md) and [TEMP-1B](/products/temp1b/introduction.md) use.

## Choose a probe

Both probes read -55°C to 85°C (-67°F to 185°F) with ±0.5°C accuracy. Pick the cable length that fits your project.

| Probe | Cable | Good for |
|-------|-------|----------|
| <a href="https://apolloautomation.com/products/long-temperature-probe" target="_blank" rel="noreferrer nofollow noopener">**1.5m (~5ft) Waterproof Flat Cable**</a> | Long | Fridges, freezers, fish tanks, reaching across a room. |
| <a href="https://apolloautomation.com/products/short-temperature-probe" target="_blank" rel="noreferrer nofollow noopener">**20cm (~8in) Waterproof Flat Cable**</a> | Short | Tight spaces close to the device. |

## Attach the probe

Plug the probe's connector into the **1Wire** port at the top right of the [Breakout Module](/products/ESPHome-Starter-Kit/modules/apollo-breakout-module.md#pinout) with the latch side facing up.

![](/assets/esphome-starter-kit-breakout-module-dallas-probe.webp)

The probe's data line is on **GPIO6**.

## Add to ESPHome Device Builder

In your device config, add two components:

1. The <a href="https://esphome.io/components/one_wire/" target="_blank" rel="noreferrer nofollow noopener">One Wire</a> component, set to **GPIO6**. This sets up the bus the probe talks on.
2. A <a href="https://esphome.io/components/sensor/dallas_temp/" target="_blank" rel="noreferrer nofollow noopener">Dallas Temperature</a> sensor, which reads the probe on that bus.

Flash the device, and the temperature reading shows up alongside your other entities. You can wire more than one probe to the same 1Wire port and read each one separately.

??? example "Working YAML"

    Prefer editing YAML directly? This is all a single probe needs:

    ```yaml
    one_wire:
      - platform: gpio
        pin: GPIO6

    sensor:
      - platform: dallas_temp
        name: "Temperature"
        update_interval: 60s
    ```

    With one probe on the bus you can leave the address out, ESPHome finds it. Running more than one? Give each `dallas_temp` sensor its own `address:` (ESPHome logs the addresses it detects on boot) so the readings don't swap around.

--8<-- "_snippets/community-help.md"
