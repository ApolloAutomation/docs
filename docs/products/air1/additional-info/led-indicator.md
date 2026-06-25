---
title: AIR-1 LED Indicator
description: Color the AIR-1's onboard RGB LEDs by air quality, using NowCast AQI, CO₂, or the VOC Index.
---
# AIR-1 LED Indicator

The AIR-1's three onboard RGB LEDs can double as an air quality gauge. Pick what they track and they shift from green to red as that reading climbs, so you can read the room from across it.

!!! note "Requires firmware 26.6.25.1 or newer"

    The **LED Indicator Source** control ships in AIR-1 firmware 26.6.25.1 and later. If you don't see it, [update your firmware](../../general/calibrating-and-updating/updating-firmware.md) first.

## Pick what the LEDs track

Open the AIR-1 device in Home Assistant and find the **LED Indicator Source** dropdown.

| Option | LEDs show |
| --- | --- |
| **[NowCast AQI](../setup/general-tips.md#nowcast-aqi)** | US EPA Air Quality Index (default) |
| **[CO2](../setup/general-tips.md#scd40-co2-sensor)** | Carbon dioxide, in ppm |
| **[VOC Index](../setup/general-tips.md#voc-index)** | Sensirion VOC Index |
| **Off** | LEDs stay dark |

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

- The color refreshes about every 10 seconds. Change the dropdown and it catches up on the next reading.
- Choose **CO2** and the first color can take up to a minute on a cold start, because the CO₂ sensor reports once a minute. The firmware gives it a nudge at boot, so it's usually quicker than that.
- A sensor that's still warming up reads as *unknown*. The LEDs wait for a real value rather than flashing a false hazardous color.

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
