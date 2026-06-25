---
title: AIR-1 LED Indicator
description: Color the AIR-1's onboard RGB LEDs by air quality, using NowCast AQI, CO₂, or the VOC Index.
---
# AIR-1 LED Indicator

The AIR-1's three onboard RGB LEDs can double as an air quality gauge. Pick what they track and they shift from green to red as that reading climbs, so you can read the room from across it.

!!! note "Requires firmware 26.6.25.1 or newer"

    The **Air Quality LED Source** control ships in AIR-1 firmware 26.6.25.1 and later. If you don't see it, [update your firmware](../../general/calibrating-and-updating/updating-firmware.md) first.

## Turn it on

The indicator is off by default. Open the AIR-1 device in Home Assistant, find the **Air Quality LED Source** dropdown, and pick what you want the LEDs to track.

| Option | LEDs show |
| --- | --- |
| **Off** | LEDs stay dark (default) |
| **[NowCast AQI](../setup/general-tips.md#nowcast-aqi)** | US EPA Air Quality Index |
| **[CO2](../setup/general-tips.md#scd40-co2-sensor)** | Carbon dioxide, in ppm |
| **[VOC Index](../setup/general-tips.md#voc-index)** | Sensirion VOC Index |

Switch back to **Off** any time to turn the indicator off and leave the LEDs free for your own automations.

## Set the brightness

Drag the **Air Quality LED Brightness** slider to dim the LEDs, handy if the AIR-1 sits in a bedroom. It runs from 5% to 100% (default 100%) and applies the moment you change it.

## Color scale

Every source uses the same six colors, green for good through deep red for hazardous. The numbers behind each color differ because each reading has its own range.

| Color | NowCast AQI | CO₂ (ppm) | VOC Index | Meaning |
| --- | --- | --- | --- | --- |
| 🟢 Green | 0 to 50 | up to 800 | 0 to 79 | Good |
| 🟡 Yellow | 51 to 100 | 801 to 1000 | 80 to 149 | Moderate |
| 🟠 Orange | 101 to 150 | 1001 to 1500 | 150 to 249 | Unhealthy for sensitive groups |
| 🔴 Red | 151 to 200 | 1501 to 2000 | 250 to 399 | Unhealthy |
| 🟣 Purple | 201 to 300 | 2001 to 2500 | 400+ | Very unhealthy |
| 🟤 Maroon | 301+ | 2501+ | — | Hazardous |

The VOC bands line up with the **VOC Quality** sensor (Improved, Normal, Abnormal, Very abnormal, Extremely abnormal).

## Tips and quirks

- The color updates whenever the selected sensor reports a fresh reading, so NowCast AQI and VOC refresh every few seconds while CO₂ updates about once a minute.
- With **CO2** selected, the first color appears once the SCD40 has a reading, up to a minute after boot. That wait is deliberate: the sensor needs a moment to settle, and an early reading would not be trustworthy.
- A sensor that's still warming up reads as *unknown*. The LEDs stay off until there's a real value rather than flashing a false color.

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
