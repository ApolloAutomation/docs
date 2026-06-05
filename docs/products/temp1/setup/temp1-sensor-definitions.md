---
title: TEMP-1 Sensor Definitions
description: Full list of definitions for the TEMP-1 and its various sensors.
---
# Sensor Definitions

Once added to Home Assistant you can configure different settings for your TEMP-1. Use the tabs below to see what each entity does, grouped the same way Home Assistant displays them.

!!! note "How often readings update"

    The **Default Update** column is how often each sensor refreshes while the TEMP-1 is awake. By default **Prevent Sleep** is on, so the device stays awake and reports continuously at these intervals. Turn **Prevent Sleep** off to let the TEMP-1 deep-sleep between readings for more accurate onboard AHT20 temperature and humidity (the ESP chip's heat skews them while it is awake); it then wakes for about 90 seconds, reports, and sleeps for the **Sleep Duration**.

    To update firmware on a sleeping device, just click **Update** on the **Firmware Update** entity and it installs the next time the device wakes (the firmware keeps itself awake until the update finishes, so you don't need to do anything else). The optional [OTA helper](https://wiki.apolloautomation.com/products/general/battery-sensors/awake-ha-helper/) is a separate toggle that overrides **Prevent Sleep** to keep a device awake on demand.

=== "Controls"

    | Control | What it does |
    |---------|--------------|
    | **RGB Light** | One RGB Neopixel LED. Click the light bulb or color wheel to change the color. Use the toggle to turn it on or off. |
    | **Alarm Outside Temp Range** | Sounds the onboard buzzer when the selected probe reads outside the **Min Probe Temp** to **Max Probe Temp** range. Use the toggle to turn it on or off. Defaults to off. |
    | **Select Probe** | Chooses which probe the TEMP-1 reads: `Temperature` (the Dallas DS18B20 probe, available in long or short versions) or `Food` (the stainless steel, food-safe probe for grilling and cooking). |

=== "Sensors"

    | Sensor | Default Update | Details |
    |--------|:--------------:|---------|
    | **Board Temperature** | 60s | Onboard air temperature from the AHT20. Adjusted by the **Board Temperature Offset**. |
    | **Board Humidity** | 60s | Onboard relative humidity from the AHT20. Adjusted by the **Board Humidity Offset**. |
    | **Temperature Probe** | 60s | Reading from the Dallas DS18B20 probe. Active when **Select Probe** is set to `Temperature`. Adjusted by the **Temp Probe Offset**. Ideal for fridge/freezer and aquatic monitoring. |
    | **Food Probe** | 3s | Reading from the stainless steel, food-safe NTC probe. Active when **Select Probe** is set to `Food`. Adjusted by the **Food Probe Offset**. Designed for grilling, baking, and other cooking. |
    | **Temperature Probe 2** | 60s | Second Dallas DS18B20 probe on the one-wire bus. Disabled by default. |
    | **Temperature Probe 3** | 60s | Third Dallas DS18B20 probe on the one-wire bus. Disabled by default. |
    | **Temperature Probe 4** | 60s | Fourth Dallas DS18B20 probe on the one-wire bus. Disabled by default. |

=== "Configuration"

    | Setting | Default | What it does |
    |---------|:-------:|--------------|
    | **ESP Reboot** | — | Restarts the device. Helpful for troubleshooting or refreshing the connection. |
    | **Board Temperature Offset** | 0.0 °C | Calibrates the **Board Temperature** reading to a known value. Range is -70 to +70 °C. |
    | **Board Humidity Offset** | 0 % | Calibrates the **Board Humidity** reading to a known value. Range is -70 to +70 %. |
    | **Temp Probe Offset** | 0.0 °C | Calibrates the **Temperature Probe** reading to a known value. Range is -70 to +70 °C. Disabled by default. |
    | **Food Probe Offset** | 0.0 °C | Calibrates the **Food Probe** reading to a known value. Range is -70 to +70 °C. Disabled by default. |
    | **Max Probe Temp** | 125.0 °C | Upper threshold for the **Alarm Outside Temp Range** toggle. |
    | **Min Probe Temp** | -55.0 °C | Lower threshold for the **Alarm Outside Temp Range** toggle. |
    | **Probe Temp Difference Threshold** | 0.0 °C | Temperature change that triggers a report when **Notify Only Outside Temp Difference** is on. Disabled by default. |
    | **Notify Only Outside Temp Difference** | Off | Wakes the device to report only when the probe temperature changes by more than the **Probe Temp Difference Threshold**, instead of every wake cycle. Disabled by default. |
    | **Sleep Duration** | 8 min | How long the TEMP-1 stays in deep sleep between wake cycles (only used when **Prevent Sleep** is off). |
    | **Prevent Sleep** | On | Keeps the device awake instead of deep-sleeping, so it reports continuously. Turn it off to let the TEMP-1 deep-sleep between readings for more accurate onboard AHT20 temperature and humidity. |
    | **Factory Reset ESP** | — | Erases settings and returns the device to factory firmware defaults. Disabled by default. |

=== "Diagnostic"

    | Entity | Default Update | What it shows |
    |--------|:--------------:|---------------|
    | **Apollo Firmware Version** | on boot | The Apollo firmware build installed on the device (for example, `26.3.2.1`). |
    | **ESPHome Version** | on boot | The ESPHome version the firmware was compiled with. |
    | **Firmware Update** | — | Shows whether a firmware update is available and lets you update from inside Home Assistant. |
    | **IP Address** | on connect | The device's IP address on your network. |
    | **Online** | on change | Connection status of the device to Home Assistant. |
    | **RSSI** | 60s | Wi-Fi signal strength in dBm. Values closer to 0 are stronger; a weak signal can affect reliability. |
    | **ESP Temperature** | 60s | Internal temperature of the ESP32 chip. Runs warmer than the room because of the processor and Wi-Fi radio. |
    | **Uptime** | 60s | How long the device has been running since its last reboot. |

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
