---
title: TEMP-PRO-1 Sensor Definitions
description: Full list of definitions for the TEMP-PRO-1 and its various sensors.
---
# Sensor Definitions

Once added to Home Assistant you can configure different settings for your TEMP-PRO-1. Use the tabs below to see what each entity does, grouped the same way Home Assistant displays them.

!!! note "How often readings update"

    The **Default Update** column is how often each sensor refreshes while the TEMP-PRO-1 is awake. By default **Prevent Sleep** is on, so the device stays awake and reports continuously at these intervals. If you turn **Prevent Sleep** off (for battery use), the TEMP-PRO-1 wakes for about 90 seconds, reports, then deep-sleeps for the **Sleep Duration**.

=== "Controls"

    | Control | What it does |
    |---------|--------------|
    | **RGB Light** | Four RGB Neopixel LEDs. Click the light bulb or color wheel to change the color. Use the toggle to turn them on or off. Also used to signal alarm and connection status. |
    | **Alarm Outside Temp Range** | Sounds the onboard buzzer and pulses the RGB Light red when a temperature reading falls outside the **Min Temperature** to **Max Temperature** range. Defaults to off. |
    | **Alarm Outside Humidity Range** | Sounds the onboard buzzer and pulses the RGB Light red when a humidity reading falls outside the **Min Humidity** to **Max Humidity** range. Defaults to off. |

=== "Sensors"

    | Sensor | Default Update | Details |
    |--------|:--------------:|---------|
    | **SHT Temperature** | 60s | Ambient temperature from the onboard SHT30 sensor. |
    | **SHT Relative Humidity** | 60s | Relative humidity from the onboard SHT30 sensor. |
    | **Dallas Temperature Probe** | 60s | Temperature from the attached DS18B20 stainless-steel probe. Reads *Unknown* if no probe is connected. |
    | **Battery voltage** | 60s | Battery voltage measured by the onboard MAX17048 fuel gauge. |
    | **Battery level** | 60s | Estimated battery charge percentage from the MAX17048, capped at 100%. |
    | **Temperature Within Range** | on change | On when every active temperature reading is between **Min Temperature** and **Max Temperature**. Used by the **Alarm Outside Temp Range** control. |
    | **Humidity Within Range** | on change | On when the humidity reading is between **Min Humidity** and **Max Humidity**. Used by the **Alarm Outside Humidity Range** control. |
    | **Alarm Active** | on change | On while either alarm condition is met. Turns off the RGB Light when it clears. |

=== "Configuration"

    | Setting | Default | What it does |
    |---------|:-------:|--------------|
    | **Min Temperature** | -20 °C | Low temperature threshold for the **Alarm Outside Temp Range** control. Range -60 to 100 °C. |
    | **Max Temperature** | 100 °C | High temperature threshold for the **Alarm Outside Temp Range** control. Range -60 to 100 °C. |
    | **Min Humidity** | 0 % | Low humidity threshold for the **Alarm Outside Humidity Range** control. Range 0 to 100%. |
    | **Max Humidity** | 100 % | High humidity threshold for the **Alarm Outside Humidity Range** control. Range 0 to 100%. |
    | **Prevent Sleep** | On | Keeps the device awake instead of deep-sleeping, so it reports continuously. Required for OTA updates and live readings; turn it off to save power on battery. |
    | **Sleep Duration** | 12 h | How long the TEMP-PRO-1 stays in deep sleep between wake cycles (only used when **Prevent Sleep** is off). Range 0 to 800 hours. |
    | **Firmware Type** | WiFi | Selects which firmware build OTA updates pull from: `WiFi` or `Ethernet`. |
    | **Update Firmware** | — | Checks for and installs the latest firmware over the air. |
    | **ESP Reboot** | — | Restarts the device. Helpful for troubleshooting or refreshing the connection. |
    | **Factory Reset ESP** | — | Erases settings and returns the device to factory firmware defaults. Disabled by default. |

=== "Diagnostic"

    | Entity | Default Update | What it shows |
    |--------|:--------------:|---------------|
    | **Firmware Update** | — | Shows whether a firmware update is available and lets you update from inside Home Assistant. |
    | **Online** | on change | Connection status of the device to Home Assistant. |
    | **ESP Temperature** | 60s | Internal temperature of the ESP32 chip. Runs warmer than the room because of the processor and Wi-Fi radio. Disabled by default. |
    | **Uptime** | 60s | How long the device has been running since its last reboot. |

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
