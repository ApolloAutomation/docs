---
title: TEMP-1B Sensor Definitions
description: Full list of definitions for the TEMP-1B and its various sensors.
---
# Sensor Definitions

Once added to Home Assistant you can configure different settings for your TEMP-1B. Use the tabs below to see what each entity does, grouped the same way Home Assistant displays them.

!!! note "How often readings update"

    The **Default Update** column is how often each entity refreshes while the TEMP-1B is awake. The TEMP-1B is a battery deep-sleep device. By default **Prevent Sleep** is on, so it stays awake and reports continuously at these intervals. If you turn **Prevent Sleep** off, the device wakes, reports its values, then deep-sleeps for the **Sleep Duration** before waking again.

=== "Controls"

    | Control | What it does |
    |---------|--------------|
    | **RGB Light** | <a href="https://esphome.io/components/light/index.html#light-effects" target="_blank" rel="noopener">One RGB Neopixel LED</a>. Click the light bulb or color wheel to change the color. Use the toggle to turn it on or off. |
    | **Alarm Outside Temp Range** | Sounds the onboard buzzer when the selected probe's temperature crosses the **Min Probe Temp** or **Max Probe Temp** thresholds. Defaults to off. |
    | **Select Probe** | Chooses which probe the TEMP-1B reads: `Temperature` (the Dallas DS18B20 probe, available in long or short versions) or `Food` (the stainless steel, food-safe probe for grilling and cooking). |

=== "Sensors"

    | Sensor | Default Update | Details |
    |--------|:--------------:|---------|
    | **Temperature Probe** | 60s | Reading from the Dallas DS18B20 probe. Active when **Select Probe** is set to `Temperature`. Good for fridge/freezer, aquariums, hot tubs, and covered pools. Adjusted by the **Temp Probe Offset**. |
    | **Food Probe** | 3s | Reading from the stainless steel food-safe NTC probe for grilling, baking, and other cooking. Active when **Select Probe** is set to `Food`. Adjusted by the **Food Probe Offset**. |
    | **Board Temperature** | 60s | Onboard temperature from the AHT20 sensor. Adjusted by the **Board Temperature Offset**. |
    | **Board Humidity** | 60s | Onboard relative humidity from the AHT20 sensor. Adjusted by the **Board Humidity Offset**. |
    | **Battery level** | 60s | Remaining battery charge from the MAX17048, reported 0-100%. |
    | **Battery voltage** | 60s | Current battery voltage from the MAX17048 for real-time monitoring. |

=== "Configuration"

    | Setting | Default | What it does |
    |---------|:-------:|--------------|
    | **ESP Reboot** | — | Restarts the device. Helpful for troubleshooting or refreshing the connection. |
    | **Firmware Update** | — | Shows whether a firmware update is available and lets you update from inside Home Assistant. |
    | **Board Temperature Offset** | 0.0 °C | Calibration offset applied to the **Board Temperature** reading. |
    | **Board Humidity Offset** | 0 % | Calibration offset applied to the **Board Humidity** reading. |
    | **Temp Probe Offset** | 0.0 °C | Calibration offset for the **Temperature Probe** reading. Disabled by default. |
    | **Food Probe Offset** | 0.0 °C | Calibration offset for the **Food Probe** reading. Disabled by default. |
    | **Max Probe Temp** | 125.0 °C | Upper temperature threshold used by the **Alarm Outside Temp Range** toggle. |
    | **Min Probe Temp** | -55.0 °C | Lower temperature threshold used by the **Alarm Outside Temp Range** toggle. |
    | **Probe Temp Difference Threshold** | 0.0 °C | How much the probe temperature must change to trigger the **Notify Only Outside Temp Difference** wake. Disabled by default. |
    | **Notify Only Outside Temp Difference** | Off | When on, the device only wakes and reports when the probe temperature changes by more than the **Probe Temp Difference Threshold**. Disabled by default. |
    | **Prevent Sleep** | On | Keeps the device awake instead of deep-sleeping, so it reports continuously. Required for OTA updates and live readings; turn it off to save power on battery. While sleeping the TEMP-1B will not respond to Home Assistant until it wakes again. |
    | **Sleep Duration** | 12 h | How many hours the device stays in deep sleep between wake cycles (only used when **Prevent Sleep** is off). |
    | **Factory Reset ESP** | — | Erases settings and returns the device to factory firmware defaults. Disabled by default. |

=== "Diagnostic"

    | Entity | Default Update | What it shows |
    |--------|:--------------:|---------------|
    | **Apollo Firmware Version** | on boot | The Apollo firmware build installed on the device (for example, `26.3.2.1`). |
    | **ESPHome Version** | on boot | The ESPHome version the firmware was compiled with. |
    | **IP Address** | on connect | The device's IP address on your network. |
    | **Online** | on change | Connection status of the device to Home Assistant. |
    | **RSSI** | 60s | Wi-Fi signal strength in dBm. Values closer to 0 are stronger; a weak signal can affect reliability. |
    | **ESP Temperature** | 60s | Internal temperature of the ESP32 chip. Runs warmer than the room because of the processor and Wi-Fi radio. |
    | **Uptime** | 60s | How long the device has been running since its last reboot. |

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
