---
title: PLT-1B Sensor Definitions
description: Full list of definitions for the PLT-1B and its various sensors.
---
# Sensor Definitions

Once added to Home Assistant you can configure different settings for your PLT-1B. Use the tabs below to see what each entity does, grouped the same way Home Assistant displays them.

![PLT-1B Sensor Data](/assets/screenshot-2024-10-03-at-4-10-25-pm.png)

!!! note "How often readings update"

    The **Default Update** column is how often each sensor refreshes while the PLT-1B is awake. The PLT-1B is the 18650-battery variant, so by default it deep-sleeps to save power. By default **Prevent Sleep** is on, which keeps the device awake and reporting continuously at these intervals. If you turn **Prevent Sleep** off, the PLT-1B wakes for about 90 seconds, reports its readings, then deep-sleeps for the **Sleep Duration** before waking again.

=== "Controls"

    | Control | What it does |
    |---------|--------------|
    | **RGB Light** | One RGB Neopixel LED. Click the light bulb or color wheel to change the color. Use the toggle to turn it on or off. Useful for visual alerts tied to plant health, such as green when readings are fine and red when moisture is low. |
    | **Accessory Power** | Controls power delivery to the sensors. On sends power to the whole device. Off powers only the ESP chip, and while off you cannot turn on the RGB Light. |

=== "Sensors"

    | Sensor | Default Update | Details |
    |--------|:--------------:|---------|
    | **Air Temperature** | 60s | Air temperature around the plant, from the AHT20. Adjusted by the **Air Temperature Offset**. |
    | **Air Humidity** | 60s | Relative humidity of the air around the plant, from the AHT20. Adjusted by the **Air Humidity Offset**. |
    | **Soil Moisture** | 60s | Water content of the soil as a percentage, calculated from the soil probe voltage using the **100% Water Voltage** and **Dry Voltage** calibration values. |
    | **Soil Temperature** | 60s | Reading from the optional DS18B20 soil temperature probe. Shows *Unknown* if the probe is not connected. |
    | **LTR390 Light** | 60s* | Ambient light level in lux. *Polls at the interval set by the **LTR390 Update Interval** number (60s by default). |
    | **LTR390 UV Index** | 60s* | UV index measured by the LTR390. *Polls at the **LTR390 Update Interval**. |
    | **Battery level** | on wake | Remaining 18650 battery charge as a percentage, from the MAX17048 fuel gauge. |
    | **Battery voltage** | on wake | Current 18650 battery voltage, from the MAX17048 fuel gauge. |

=== "Configuration"

    | Setting | Default | What it does |
    |---------|:-------:|--------------|
    | **ESP Reboot** | — | Restarts the device. Helpful for troubleshooting or refreshing the connection. |
    | **Air Temperature Offset** | 0.0 °C | Calibrates the AHT20 air temperature reading to a known value. Range is -70 to 70 °C in 0.1 steps. |
    | **Air Humidity Offset** | 0 % | Calibrates the AHT20 air humidity reading to a known value. Range is -70 to 70 % in 0.1 steps. |
    | **100% Water Voltage** | 1.55 | Soil probe voltage that corresponds to fully saturated (100% wet) soil. Tune this to calibrate the **Soil Moisture** reading. Range is 0 to 5 V in 0.01 steps. |
    | **Dry Voltage** | 2.7 | Soil probe voltage that corresponds to completely dry soil. Tune this to calibrate the **Soil Moisture** reading and to trigger low-moisture automations. Range is 0 to 5 V in 0.01 steps. |
    | **LTR390 Update Interval** | 60 s | How often the LTR390 light and UV sensors poll (1 to 300 seconds). |
    | **Sleep Duration** | 12 h | How long the PLT-1B stays in deep sleep between wake cycles (only used when **Prevent Sleep** is off). Range is 0 to 800 hours. |
    | **Prevent Sleep** | On | Keeps the device awake instead of deep-sleeping, so it reports continuously. Required for OTA updates and live readings; turn it off to save battery. |
    | **Accessory Power** | On | Powers the sensors. Turn off to power only the ESP chip. |
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
    | **Soil ADC** | 5s | Raw soil probe voltage used to calculate **Soil Moisture**. Disabled by default. |

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
