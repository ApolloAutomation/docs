---
title: What is I2C?
description: >-
  A beginner's guide to the I2C bus, the two-wire connection most sensor
  breakouts use, with examples drawn from the ESPHome Starter Kit.
---
# What is I2C?

I2C (pronounced "eye-squared-see" or "eye-two-see") is a way for chips to talk to each other over just two wires. One wire carries data, called **SDA**. The other carries a clock signal, called **SCL**, which keeps both sides in step. Add power and ground and you can see why so many sensor breakouts use a single 4-pin cable.

Most of the sensors you'll want to plug into your kit speak I2C: temperature, humidity, air quality, light, distance, and hundreds more. Understanding roughly how it works makes the Breakout Module's connectors and the Device Builder's I2C settings much less mysterious.

## One bus, many devices

The two I2C wires form a **bus**, a shared connection that many devices ride on at once. Think of it like a street: every house sits on the same road, and the road doesn't care how many houses there are.

This is why the [Breakout Module](/products/ESPHome-Starter-Kit/modules/apollo-breakout-module.md) can offer five I2C connectors (STEMMA QT, Grove, the 3.5mm jack, and the rest) that are all wired to the same two pins. They aren't five separate ports. They're five doorways onto one street, so you can plug in several sensors at the same time and they all share the bus.

## Addresses

If many devices share two wires, the ESP32-C6 needs a way to say which one it means. Every I2C device has an **address**, a number usually written in hex, like `0x76`. When the ESP32-C6 wants a reading, it calls out an address, and only the device with that address answers. House numbers on the street.

Each chip's address is set by its manufacturer, and that leads to the one classic I2C problem: plug in two identical sensors and they both have the same address, so they talk over each other. Many breakout boards include a solder jumper or pin that shifts the address (say from `0x76` to `0x77`) so two of the same sensor can share a bus.

The ESP32-C6 itself doesn't need an address. It's the **controller**, the side that starts every conversation. Sensors are **peripherals**; they wait to be asked. A sensor never interrupts, which is part of why such a simple two-wire setup stays orderly.

## Pullup resistors

I2C wires need a gentle electrical nudge toward "on" when nobody is talking, provided by small **pullup resistors** on the bus. That's the whole story. Most sensor breakouts include their own, and this is why the Device Builder shows a pullup toggle when you configure I2C pins: turning it on uses the ESP32-C6's built-in pullups, which covers you when a bare sensor doesn't have any. On the starter kit, turning the toggle on for both pins is the safe default.

## I2C on the starter kit

On the ESP32-C6, the I2C bus lives on two fixed pins: **SCL is GPIO0** and **SDA is GPIO1**. Every I2C connector on the Breakout Module routes to those same two pins.

In ESPHome, one `i2c` component sets up the bus, and every sensor component you add afterwards rides on it. You configure the bus once, not per sensor:

```yaml
i2c:
  scl: GPIO0
  sda: GPIO1
  scan: true
```

That `scan: true` line is worth knowing about. On boot, ESPHome calls out every possible address and prints who answered in the device logs:

```
Found i2c device at address 0x76
```

If you plug in a sensor and aren't sure of its address, the scan tells you. If the scan finds nothing, the sensor isn't wired up or powered, which makes it a handy first troubleshooting step.

Ready to plug something in? The [Breakout Module](/products/ESPHome-Starter-Kit/modules/apollo-breakout-module.md) page covers the connectors, and the ESPHome docs list every supported I2C sensor.

<a href="https://esphome.io/components/i2c/" target="_blank" rel="noreferrer nofollow noopener" class="md-button md-button--primary"><img src="/assets/esphome-logo.svg" /> ESPHome I2C docs</a>


--8<-- "_snippets/community-help.md"
