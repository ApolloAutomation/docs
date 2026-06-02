---
title: BTN-1 Sensor Definitions
description: These are all of the entities exposed by the BTN-1 to automate on!
---
# Sensor Definitions

Once added to Home Assistant you can configure different settings for your BTN-1. Use the tabs below to see what each entity does, grouped the same way Home Assistant displays them.

!!! note "How often readings update"

    The BTN-1 is a battery-powered device that deep-sleeps by default. The **Default Update** column is how often each entity refreshes while the BTN-1 is awake. With **Prevent Sleep** off, the BTN-1 wakes for about 90 seconds (on a button press or after the **Sleep Duration**), reports its values, then deep-sleeps again. While asleep it does not respond to Home Assistant. Turn **Prevent Sleep** on to keep it awake and reporting continuously, which is required for OTA updates.

=== "Controls"

    | Control | What it does |
    |---------|--------------|
    | **BTN 1 Light** | RGB light behind the first button. Click the light bulb or color wheel to change the color, or use the toggle to turn it on or off. Defaults to off. |
    | **BTN 2 Light** | RGB light behind the second button. Click the light bulb or color wheel to change the color, or use the toggle to turn it on or off. Defaults to off. |
    | **BTN 3 Light** | RGB light behind the third button. Click the light bulb or color wheel to change the color, or use the toggle to turn it on or off. Defaults to off. |
    | **BTN 4 Light** | RGB light behind the fourth button. Click the light bulb or color wheel to change the color, or use the toggle to turn it on or off. Defaults to off. |

=== "Sensors"

    | Sensor | Default Update | Details |
    |--------|:--------------:|---------|
    | **Battery level** | per wake cycle | Remaining battery charge as a percentage, from 0 to 100%. Read from the MAX17048 fuel gauge. |
    | **Battery voltage** | per wake cycle | Current battery voltage, for real-time monitoring of the cell. |
    | **Wake-up Button Pressed** | per wake cycle | Which button woke the device from deep sleep (1 to 4). Resets to 0 after the press is handled. |

=== "Events"

    | Event | What it reports |
    |-------|-----------------|
    | **Button 1** | Fires a `click`, `double_click`, `triple_click`, or `hold` event for the first button. Great for automating. |
    | **Button 2** | Fires a `click`, `double_click`, `triple_click`, or `hold` event for the second button. Great for automating. |
    | **Button 3** | Fires a `click`, `double_click`, `triple_click`, or `hold` event for the third button. Great for automating. |
    | **Button 4** | Fires a `click`, `double_click`, `triple_click`, or `hold` event for the fourth button. Great for automating. |

=== "Configuration"

    | Setting | Default | What it does |
    |---------|:-------:|--------------|
    | **ESP Reboot** | — | Restarts the device. Helpful for troubleshooting or refreshing the connection. |
    | **Sleep Duration** | 24 h | How many hours the BTN-1 stays in deep sleep between wake cycles (only used when **Prevent Sleep** is off). Range is 0 to 800 hours. |
    | **Prevent Sleep** | On | Keeps the device awake instead of deep-sleeping, so it responds to Home Assistant continuously. Required for OTA updates; turn it off to save battery. While the device is asleep it does not respond to Home Assistant until it wakes again. |
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
    | **ESP Temperature** | 60s | Internal temperature of the ESP32 chip. Runs warmer than the room because of the processor and Wi-Fi radio. Disabled by default. |
    | **Uptime** | 60s | How long the device has been running since its last reboot. |

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
