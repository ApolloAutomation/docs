---
title: MSR-2 Sensor Definitions
description: These are all of the entities exposed by the MSR-2 to automate on!
---
# Sensor Definitions

Once added to Home Assistant you can configure different settings for your MSR-2. Use the tabs below to see what each entity does, grouped the same way Home Assistant displays them.

!!! note "How often readings update"

    The **Default Update** column is how often each entity refreshes. Radar entities update in real time as targets move. The **LTR390 Light** and **LTR390 UV Index** sensors use the interval set by the **LTR390 Update Interval** number (60s by default).

!!! note "Ensure that the LD2410 firmware version is V2.04.23022511 or later for proper integration functionality."

    The newer version of the firmware includes an "auto calibrate" function, so you might want to test it out.

=== "Controls"

    | Control | What it does |
    |---------|--------------|
    | **RGB Light** | Three RGB Neopixel LEDs. Click the light bulb or color wheel to change the color. Use the toggle to turn them on or off. |
    | **Calibrate SCD40 To 420ppm** | Forces a fresh-air calibration of the SCD40 CO₂ sensor to the <a href="https://wiki.apolloautomation.com/products/general/calibrating-and-updating/co2-calibration/" target="_blank" rel="noopener">outdoor baseline</a> (about <a href="https://climate.nasa.gov/vital-signs/carbon-dioxide/?intent=121" target="_blank" rel="noopener">420 ppm</a>). Run it outdoors or next to an open window. |

=== "Sensors"

    #### Air quality &amp; light

    | Sensor | Default Update | Details |
    |--------|:--------------:|---------|
    | **CO2** | 60s | True NDIR reading from the SCD40. Shows *Unknown* if you do not have the CO₂ module. You can <a href="https://wiki.apolloautomation.com/products/general/calibrating-and-updating/co2-calibration/" target="_blank" rel="noopener">re-calibrate it to the outdoor baseline</a>. |
    | **DPS310 Pressure** | 30s | Barometric air pressure. A small subset of devices do not include a DPS310 sensor. If this reads *Unknown*, your device may be one of these units. |
    | **DPS310 Temperature** | 30s | Ambient air temperature from the DPS310. Adjusted by the **DPS Temperature Offset**. A small subset of devices do not include a DPS310 sensor. |
    | **LTR390 Light** | 60s* | Ambient light level in lux. *Polls at the **LTR390 Update Interval** (60s by default). |
    | **LTR390 UV Index** | 60s* | UV index measured by the LTR390. *Polls at the **LTR390 Update Interval**. |

    #### Radar (LD2410)

    | Sensor | Default Update | Details |
    |--------|:--------------:|---------|
    | **Radar Target** | real-time | Whether the radar detects a still or moving target. Good for triggering occupancy automations. |
    | **Radar Moving Target** | real-time | Whether a moving target is currently detected. |
    | **Radar Still Target** | real-time | Whether a stationary target is currently detected. |
    | **Radar Moving Distance** | real-time | Distance to a moving target in cm. Reports *Unknown* when no moving target is present. |
    | **Radar Still Distance** | real-time | Distance to a still target in cm. Reports *Unknown* when no still target is present. |
    | **Radar Detection Distance** | real-time | Last detected distance from the radar in cm. Holds the last value, so it can be misleading when nothing is present. |
    | **Radar Move Energy** | real-time | Amount of movement measured by the LD2410. Faster movement reads as a higher percentage. |
    | **Radar Still Energy** | real-time | Energy of the current still target. |
    | **Radar Zone 1 Occupancy** | real-time | Whether someone is in Zone 1. Zones are distance bands from the sensor, set with **Radar Zone 1 Start** and **Radar End Zone 1**. |
    | **Radar Zone 2 Occupancy** | real-time | Whether someone is in Zone 2, from the end of Zone 1 to **Radar End Zone 2**. |
    | **Radar Zone 3 Occupancy** | real-time | Whether someone is in Zone 3, from the end of Zone 2 to **Radar End Zone 3**. |
    | **Radar Zone Occupancy** | real-time | Whether any of Zone 1, 2, or 3 is occupied. |

=== "Configuration"

    | Setting | Default | What it does |
    |---------|:-------:|--------------|
    | **ESP Reboot** | — | Restarts the device. Helpful for troubleshooting or refreshing the connection. |
    | **Factory Reset ESP** | — | Erases settings and returns the device to factory firmware defaults. Disabled by default. |
    | **Factory Reset Radar** | — | Resets the LD2410 radar to its factory move and still thresholds. |
    | **Restart Radar** | — | Restarts the LD2410 radar module. |
    | **Radar Timeout** | — | How long presence stays detected, in seconds, after the target is lost. |
    | **Radar Max Move Distance** | — | Maximum distance gate for movement detection (gate 2 to 8). Use it to ignore movement past a chosen distance. |
    | **Radar Max Still Distance** | — | Maximum distance gate for still detection (gate 2 to 8). Use it to ignore still targets past a chosen distance. |
    | **Radar Zone 1 Start** | 0 cm | Start distance of Zone 1 from the sensor, in cm (0 to 800). |
    | **Radar End Zone 1** | 50 cm | End distance of Zone 1 from the sensor, in cm. From **Radar Zone 1 Start** to this value is Zone 1. |
    | **Radar End Zone 2** | 150 cm | End distance of Zone 2, in cm. From the end of Zone 1 to this value is Zone 2. |
    | **Radar End Zone 3** | 250 cm | End distance of Zone 3, in cm. From the end of Zone 2 to this value is Zone 3. |
    | **Radar Engineering Mode** | — | Enables the g0-g8 threshold sliders for <a href="https://wiki.apolloautomation.com/products/msr2/setup/zones-ha/" target="_blank" rel="noopener">mmWave tuning</a>. |
    | **g0-g8 move threshold** | — | Movement sensitivity threshold for each gate (g0 through g8). See the <a href="https://wiki.apolloautomation.com/products/msr2/setup/zones-ha/" target="_blank" rel="noopener">radar tuning guide</a>. |
    | **g0-g8 still threshold** | — | Stillness sensitivity threshold for each gate (g0 through g8). See the <a href="https://wiki.apolloautomation.com/products/msr2/setup/zones-ha/" target="_blank" rel="noopener">radar tuning guide</a>. |
    | **ld2410 Gate Size** | — | Distance resolution per gate on the LD2410. Disabled by default. |
    | **ld2410 Bluetooth** | Off | Turns on the LD2410's Bluetooth so you can connect with the HLK Radartool phone app for <a href="https://wiki.apolloautomation.com/products/msr2/setup/zones-hlk/" target="_blank" rel="noopener">tuning</a>. Turned off at boot. |
    | **LTR390 Update Interval** | 60 s | How often the LTR390 light and UV sensors poll (1 to 300 seconds). Disabled by default. |
    | **DPS310 Pressure Offset** | 0.0 hPa | Calibration offset for the DPS310 pressure reading (-100 to +100 hPa in 0.1 hPa steps). Disabled by default. A small subset of devices do not include a DPS310 sensor; if this reads *Unknown*, your device may be one of these units. |
    | **DPS Temperature Offset** | 14.54 °C | Offsets heat from the ESP chip for a more accurate DPS310 temperature reading. A small subset of devices do not include a DPS310 sensor. |
    | **Reduce DB Reporting** | Off | Applies filters so many entities only report when they cross a threshold, using less Wi-Fi airtime and less Home Assistant database space. |
    | **Startup Light Blink** | On | Blinks the RGB LED during the MSR-2's initial boot. |

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
    | **Radar Firmware Version** | on boot | Firmware version installed on the LD2410 radar module. |
    | **query params** | — | Queries the LD2410's current parameters for debugging and advanced tuning. |
    | **g0 move energy to g8 move energy** | real-time | Live move-energy level for each gate (g0 through g8). |
    | **g0 still energy to g8 still energy** | real-time | Live still-energy level for each gate (g0 through g8). |

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
