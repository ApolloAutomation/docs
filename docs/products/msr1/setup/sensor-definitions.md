---
title: MSR-1 Sensor Definitions
description: Full list of definitions for the MSR-1 and its various sensors.
---
# Sensor Definitions

Once added to Home Assistant you can configure different settings for your MSR-1. Use the tabs below to see what each entity does, grouped the same way Home Assistant displays them.

!!! note "How often readings update"

    The **Default Update** column is how often each entity refreshes. Radar entities update in real time as targets move. The **LTR390 Light** and **LTR390 UV Index** sensors use the interval set by the **LTR390 Update Interval** number (60s by default).

=== "Controls"

    | Control | What it does |
    |---------|--------------|
    | **RGB Light** | Three RGB Neopixel LEDs. Click the light bulb or color wheel to change the color. Use the toggle to turn them on or off. |
    | **Calibrate SCD40 To 420ppm** | Forces a fresh-air calibration of the SCD40 CO₂ sensor to the <a href="https://wiki.apolloautomation.com/products/general/calibrating-and-updating/co2-calibration/" target="_blank" rel="noopener">outdoor baseline</a> (about <a href="https://climate.nasa.gov/vital-signs/carbon-dioxide/?intent=121" target="_blank" rel="noopener">420 ppm</a>). Run it outdoors or next to an open window. |
    | **Restart Radar** | Restarts the LD2410 radar module without rebooting the whole device. |

=== "Sensors"

    #### Air quality &amp; light

    | Sensor | Default Update | Details |
    |--------|:--------------:|---------|
    | **CO2** | 60s | True NDIR reading from the SCD40. Shows *Unknown* if you do not have the CO₂ module. You can <a href="https://wiki.apolloautomation.com/products/general/calibrating-and-updating/co2-calibration/" target="_blank" rel="noopener">re-calibrate it to the outdoor baseline</a>. |
    | **BME280 Temperature** | 60s | Ambient air temperature from the BME280. Adjusted by the **BME280 Temperature Offset**. |
    | **BME280 Humidity** | 60s | Relative humidity from the BME280. Adjusted by the **BME280 Humidity Offset**. |
    | **BME280 Pressure** | 60s | Barometric air pressure from the BME280. |
    | **LTR390 Light** | 60s* | Ambient light level in lux. *Polls at the **LTR390 Update Interval** (60s by default). |
    | **LTR390 UV Index** | 60s* | UV index measured by the LTR390. *Polls at the **LTR390 Update Interval**. |

    #### Radar (LD2410 mmWave)

    | Sensor | Default Update | Details |
    |--------|:--------------:|---------|
    | **Radar Target** | real-time | Whether the radar detects a still or moving target. Good for triggering occupancy automations. |
    | **Radar Moving Target** | real-time | Whether the radar currently has a moving target it is tracking. |
    | **Radar Still Target** | real-time | Whether the radar currently has a still target. |
    | **Radar Moving Distance** | real-time | Distance to the moving target. Holds the last value when no moving target is present, so it can be misleading. |
    | **Radar Still Distance** | real-time | Distance to the still target. Holds the last value when no still target is present, so it can be misleading. |
    | **Radar Detection Distance** | real-time | The last detected distance by the radar. Holds the last known value, so it can sometimes be misleading. |
    | **Radar Move Energy** | real-time | The amount of movement measured by the LD2410. Faster movements report a higher percentage. |
    | **Radar Still Energy** | real-time | The energy of the current still target. |
    | **Radar Zone 1 Occupancy** | real-time | Whether someone is in Zone 1, a configurable distance band from the sensor. Defined by **Radar Zone 1 Start** and **Radar End Zone 1**. |
    | **Radar Zone 2 Occupancy** | real-time | Same as Zone 1, for the second distance band (from **Radar End Zone 1** to **Radar End Zone 2**). |
    | **Radar Zone 3 Occupancy** | real-time | Same as Zones 1 and 2, for the third distance band (from **Radar End Zone 2** to **Radar End Zone 3**). |
    | **Radar Zone Occupancy** | real-time | Whether any of the three zones is currently occupied. |
    | **g0-g8 move energy** | real-time | Live move-energy reading for each distance gate (g0 to g8). Used when tuning the radar. |
    | **g0-g8 still energy** | real-time | Live still-energy reading for each distance gate (g0 to g8). Used when tuning the radar. |

=== "Configuration"

    | Setting | Default | What it does |
    |---------|:-------:|--------------|
    | **ESP Reboot** | — | Restarts the device. Helpful for troubleshooting or refreshing the connection. |
    | **BME280 Temperature Offset** | 14.54 °C | Calibrates the BME280 temperature reading to a known value. See the <a href="https://wiki.apolloautomation.com/products/general/temp-hum-calibration/" target="_blank" rel="noopener">temperature &amp; humidity calibration guide</a>. |
    | **BME280 Humidity Offset** | -18.86 % | Calibrates the BME280 humidity reading to a known value. See the <a href="https://wiki.apolloautomation.com/products/general/temp-hum-calibration/" target="_blank" rel="noopener">temperature &amp; humidity calibration guide</a>. |
    | **LTR390 Update Interval** | 60 s | How often the LTR390 light and UV sensors poll (1 to 300 seconds). Disabled by default. |
    | **Radar Timeout** | — | The time in seconds that the radar's presence stays detected after the target is lost. |
    | **Radar Max Move Distance** | — | Maximum distance gate for movement detection. Value between 2 and 8 inclusive. |
    | **Radar Max Still Distance** | — | Maximum distance gate for still detection. Value between 2 and 8 inclusive. |
    | **Radar Distance Resolution** | — | Best kept at 0.75 m in most cases. At 0.25 m the first few gates become very sensitive and the maximum detection distance shrinks a lot. Disabled by default. |
    | **Radar Zone 1 Start** | 0 cm | Starting distance for Zone 1, measured in cm from the sensor. |
    | **Radar End Zone 1** | 50 cm | Ending distance for Zone 1 in cm. Sets the band reported by **Radar Zone 1 Occupancy** (for example, 0 to 50 cm from the sensor). |
    | **Radar End Zone 2** | 150 cm | Ending distance for Zone 2 in cm, measured from the sensor. |
    | **Radar End Zone 3** | 250 cm | Ending distance for Zone 3 in cm, measured from the sensor. |
    | **g0-g8 move threshold** | from module | Move-detection sensitivity for each distance gate (g0 to g8). See the <a href="https://wiki.apolloautomation.com/products/msr1/setup/zones-ha/" target="_blank" rel="noopener">radar tuning guide</a>. |
    | **g0-g8 still threshold** | from module | Still-detection sensitivity for each distance gate (g0 to g8). See the <a href="https://wiki.apolloautomation.com/products/msr1/setup/zones-ha/" target="_blank" rel="noopener">radar tuning guide</a>. |
    | **Radar Control Bluetooth** | Off | Turns on the LD2410's Bluetooth so you can connect with the HLK Radar phone app (for example, to update the radar chip's own firmware, not the MSR-1 in general). |
    | **Radar Engineering Mode** | — | Enables the radar's engineering mode, which exposes the per-gate energy readings used for tuning. |
    | **Startup Light Blink** | On | Blinks the RGB LED on startup to show the device's connection status. |
    | **Reduce DB Reporting** | Off | Filters out small sensor changes so fewer values are logged to your Home Assistant database. |
    | **query params** | — | Queries the LD2410 for its current parameters. |
    | **Factory Reset Radar** | — | Sets the radar's move and still thresholds back to the manufacturer's original values. |
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
    | **Radar Firmware Version** | on boot | Firmware version installed on the LD2410 radar module. |

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
