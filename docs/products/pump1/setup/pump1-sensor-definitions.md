---
title: PUMP-1 Sensor Definitions
description: These are all of the entities exposed by the PUMP-1 to automate on!
---
# Sensor Definitions

Once added to Home Assistant you can configure different settings for your PUMP-1. Use the tabs below to see what each entity does, grouped the same way Home Assistant displays them.

!!! note "How often readings update"

    The **Default Update** column is how often each entity refreshes. The **Fluid Input** and **Fluid Output** sensors are event-driven, so they report the moment water rises above or falls below the sensor rather than on a fixed interval.

=== "Controls"

    | Control | What it does |
    |---------|--------------|
    | **RGB Light** | One RGB Neopixel LED. Click the light bulb or color wheel to change the color. Use the toggle to turn it on or off. |
    | **Pump Run Seconds** | Amount of time in seconds to run the pump when you press **Run Pump**. Range is 1 to 120 seconds. Defaults to 10s. |
    | **Run Pump** | Runs the PUMP-1 pump for the number of seconds set in **Pump Run Seconds**. |
    | **Run Pump Until Output Wet** | Runs the pump until the **Fluid Output** sensor changes to **Wet**. Disabled by default. |

=== "Sensors"

    | Sensor | Default Update | Details |
    |--------|:--------------:|---------|
    | **Fluid Input** | on change | Ultrasonic sensor at the bottom of the PUMP-1 water bottle that monitors the presence of fluid. Reports **Wet** while water is present and **Dry** once the bottle is empty. |
    | **Fluid Output** | on change | Ultrasonic sensor you can mount on the exterior of any container to detect water on the other side, such as a Keurig reservoir or fish tank. Reports **Wet** when the water level is above the sensor and **Dry** when it falls below. |

=== "Configuration"

    | Setting | Default | What it does |
    |---------|:-------:|--------------|
    | **ESP Reboot** | — | Restarts the device. Helpful for troubleshooting or refreshing the connection. |
    | **Max Safe Run Time** | 60 s | Maximum time the pump will run before shutting off. Range is 5 to 600 seconds. |
    | **Pump Control** | — | Toggles the pump on and off via a switch. Still stopped by **Max Safe Run Time**. Disabled by default. |
    | **Stop Pump When Input Dry** | Off | Turns the pump off when the ultrasonic sensor at the bottom of the water bottle detects no water. This check is automatically skipped when **Invert Water Logic** is enabled. |
    | **Stop Pump When Output Wet** | Off | Turns the pump off when the **Fluid Output** sensor (mounted on a Keurig tank, fish tank, or similar container) detects that the water level has risen above its monitoring point. |
    | **Invert Water Logic** | Off | Flips the meaning of the **Fluid Input** sensor so that **Dry** = destination is low (start pumping) and **Wet** = destination is full (stop pumping). Use this when the Input sensor is placed at the low-water mark inside a destination tank (for example, a CPAP reservoir) rather than at the bottom of a supply bottle. Disabled by default. |
    | **Auto Refill** | Off | When enabled together with **Invert Water Logic**, the pump automatically starts a fill cycle whenever the **Fluid Input** sensor reads **Dry**. The pump stops when the **Fluid Output** sensor reads **Wet** or when **Max Safe Run Time** is reached, whichever comes first. Requires **Invert Water Logic**. Disabled by default. |
    | **Pump Safety Override** | Off | Disables the safety features. Disabled by default. |
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
