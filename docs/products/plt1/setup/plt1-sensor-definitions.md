---
title: PLT-1 Sensor Definitions
description: Full list of definitions for the PLT-1 and its various sensors.
---
# Sensor Definitions

Once added to Home Assistant you can configure different settings for your PLT-1. Use the tabs below to see what each entity does, grouped the same way Home Assistant displays them.

![PLT-1 Sensor Data](/assets/screenshot-2024-10-03-at-4-10-25-pm.png)

!!! tip "Automate your plant care"

    Want soil-moisture alerts and watering reminders? Import the [PLT-1 Plant Sensor Alerts blueprint](https://wiki.apolloautomation.com/products/plt1/examples/blueprint/) to get low-moisture notifications and automations without building them by hand.

=== "Controls"

    | Control | What it does |
    |---------|--------------|
    | **RGB Light** | One RGB Neopixel LED. Click the light bulb or color wheel to change the color. Use the toggle to turn it on or off. Useful for visual plant-health alerts (for example, green when fine, red when soil is too dry). |

=== "Sensors"

    | Sensor | Default Update | Details |
    |--------|:--------------:|---------|
    | **Soil Moisture** | 60s | Water content of the soil as a percentage, calculated from the soil voltage against the **100% Water Voltage** and **Dry Voltage** calibration values. Ideal range depends on the plant. |
    | **Soil Temperature** | 60s | Reading from the optional DS18B20 soil temperature probe. Shows *Unknown* if no probe is connected. |
    | **Air Temperature** | 60s | Air temperature around the plant from the AHT20 sensor. Adjusted by the **Air Temperature Offset**. |
    | **Air Humidity** | 60s | Relative humidity of the air around the plant from the AHT20 sensor. Adjusted by the **Air Humidity Offset**. |
    | **LTR390 Light** | 60s* | Ambient light level in lux. *Polls at the **LTR390 Update Interval** (60s by default). |
    | **LTR390 UV Index** | 60s* | UV index measured by the LTR390. *Polls at the **LTR390 Update Interval**. |
    | **Soil ADC** | 5s | Raw soil voltage from the ADC, used to calculate **Soil Moisture**. Diagnostic, disabled by default. |

=== "Configuration"

    | Setting | Default | What it does |
    |---------|:-------:|--------------|
    | **ESP Reboot** | — | Restarts the device. Helpful for troubleshooting or refreshing the connection. |
    | **100% Water Voltage** | 1.55 | Soil voltage that corresponds to fully saturated (wet) soil. Lowers the **Soil Moisture** scale. Tune this for your plant and probe. |
    | **Dry Voltage** | 2.7 | Soil voltage that corresponds to completely dry soil. Sets the point where **Soil Moisture** reads 0%. |
    | **Air Temperature Offset** | 0.0 °C | Calibration offset applied to the **Air Temperature** reading. |
    | **Air Humidity Offset** | 0 % | Calibration offset applied to the **Air Humidity** reading. |
    | **LTR390 Update Interval** | 60 s | How often the LTR390 light and UV sensors poll (1 to 300 seconds). |
    | **Sleep Duration** | 5 min | How long the PLT-1 deep-sleeps between readings when **Prevent Sleep** is off. |
    | **Prevent Sleep** | On | Keeps the device awake instead of deep-sleeping, so it reports continuously. Turn it off to let the PLT-1 deep-sleep between readings for more accurate onboard AHT20 temperature and humidity. |
    | **Factory Reset ESP** | — | Erases settings and returns the device to factory firmware defaults. Disabled by default. |

=== "Diagnostic"

    | Entity | Default Update | What it shows |
    |--------|:--------------:|---------------|
    | **Apollo Firmware Version** | on boot | The Apollo firmware build installed on the device (for example, `26.3.2.1`). |
    | **ESPHome Version** | on boot | The ESPHome version the firmware was compiled with. |
    | **Firmware Update** | — | Shows whether a firmware update is available. Click **Update** and it installs the next time the device wakes; the optional [OTA helper](https://wiki.apolloautomation.com/products/general/battery-sensors/awake-ha-helper/) overrides **Prevent Sleep** to keep the device awake on demand. Separate from the **Apollo Firmware Version** and **ESPHome Version** sensors. |
    | **IP Address** | on connect | The device's IP address on your network. |
    | **Online** | on change | Connection status of the device to Home Assistant. |
    | **RSSI** | 60s | Wi-Fi signal strength in dBm. Values closer to 0 are stronger; a weak signal can affect reliability. |
    | **ESP Temperature** | 60s | Internal temperature of the ESP32 chip. Runs warmer than the room because of the processor and Wi-Fi radio. |
    | **Uptime** | 60s | How long the device has been running since its last reboot. |

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
