---
title: R-PRO-1 Sensor Definitions
description: These are all of the entities exposed by the R-PRO-1 to automate on!
---
# Sensor Definitions

Once added to Home Assistant you can configure different settings for your R-PRO-1. Use the tabs below to see what each entity does, grouped the same way Home Assistant displays them.

The R-PRO-1 pairs two radars: an **LD2450** that tracks the position of up to three targets and reports zone occupancy, and an **LD2412** that handles presence and per-gate sensitivity tuning. It also carries an LTR390 light sensor and an optional SCD40 CO₂ module.

!!! note "How often readings update"

    The **Default Update** column is how often each entity refreshes. Radar entities update in real time as targets move. The SCD40 and LTR390 sensors report every 60s.

=== "Controls"

    | Control | What it does |
    |---------|--------------|
    | **RGB Light** | Four RGB Neopixel LEDs. Click the light bulb or color wheel to change the color. Use the toggle to turn them on or off. |
    | **Calibrate SCD40 To 420ppm** | Forces a fresh-air calibration of the SCD40 CO₂ sensor to the <a href="https://wiki.apolloautomation.com/products/general/calibrating-and-updating/co2-calibration/" target="_blank" rel="noopener">outdoor baseline</a> (about <a href="https://climate.nasa.gov/vital-signs/carbon-dioxide/?intent=121" target="_blank" rel="noopener">420 ppm</a>). Run it outdoors or next to an open window. |

=== "Sensors"

    #### Air quality &amp; light

    | Sensor | Default Update | Details |
    |--------|:--------------:|---------|
    | **CO2** | 60s | True NDIR reading from the SCD40. Shows *Unknown* if you do not have the CO₂ module. You can <a href="https://wiki.apolloautomation.com/products/general/calibrating-and-updating/co2-calibration/" target="_blank" rel="noopener">re-calibrate it to the outdoor baseline</a>. |
    | **SCD40 Temperature** | 60s | Temperature from the optional SCD40 module. Disabled by default. Adjusted by the **SCD40 Temperature Offset**. |
    | **SCD40 Humidity** | 60s | Humidity from the optional SCD40 module. Disabled by default. Adjusted by the **SCD40 Humidity Offset**. |
    | **LTR390 Light** | 60s | Ambient light level in lux from the LTR390. |
    | **LTR390 UV Index** | 60s | UV index measured by the LTR390. |

    #### Combined presence

    | Sensor | Default Update | Details |
    |--------|:--------------:|---------|
    | **Combined Presence** | real-time | Combined occupancy: shows **Detected** when either the LD2450 or the LD2412 radar sees a target, and **Clear** when neither does. Use this entity for automations and dashboards instead of the individual radar presence sensors. |

    #### Radar presence (LD2412 mmWave)

    | Sensor | Default Update | Details |
    |--------|:--------------:|---------|
    | **LD2412 Presence** | real-time | Whether the LD2412 detects any target, moving or still. |
    | **LD2412 Moving Target** | real-time | Whether the LD2412 detects only a moving target. |
    | **LD2412 Still Target** | real-time | Whether the LD2412 detects only a still target. |
    | **LD2412 Detection Distance** | real-time | Distance of the target being tracked. Disabled by default. |
    | **LD2412 Moving Distance** | real-time | Distance of the moving target being tracked. Disabled by default. |
    | **LD2412 Still Distance** | real-time | Distance of the still target being tracked. Disabled by default. |
    | **LD2412 Move Energy** | real-time | Energy level of the moving target being tracked. Disabled by default. |
    | **LD2412 Still Energy** | real-time | Energy level of the still target being tracked. Disabled by default. |
    | **LD2412 Light** | real-time | Light level reported by the LD2412. Disabled by default. |

    #### Radar tracking (LD2450 mmWave)

    | Sensor | Default Update | Details |
    |--------|:--------------:|---------|
    | **LD2450 Presence** | real-time | Whether the radar currently detects any target. Great for occupancy automations. |
    | **LD2450 Moving Target** | real-time | Whether a moving target is detected. |
    | **LD2450 Still Target** | real-time | Whether a stationary target is detected. |
    | **LD2450 Presence Target Count** | real-time | Count of all presence targets (max 3). |
    | **LD2450 Moving Target Count** | real-time | Count of all moving targets (max 3). |
    | **LD2450 Still Target Count** | real-time | Count of all still targets (max 3). |
    | **LD2450 Target-1 / Target-2 / Target-3 X** | real-time | Distance in mm of the target from the sensor along the X-axis (negative = left, positive = right, range -3000 to 3000). |
    | **LD2450 Target-1 / Target-2 / Target-3 Y** | real-time | Distance in mm of the target from the sensor in the Y direction (near/far, range 0 to 6000). |
    | **LD2450 Target-1 / Target-2 / Target-3 Speed** | real-time | Speed of the moving target in mm/s. |
    | **LD2450 Target-1 / Target-2 / Target-3 Angle** | real-time | Angle of the target in degrees relative to the sensor. |
    | **LD2450 Target-1 / Target-2 / Target-3 Distance** | real-time | Straight-line distance of the target from the sensor. |
    | **LD2450 Target-1 / Target-2 / Target-3 Resolution** | real-time | Target detection range resolution in mm. Disabled by default. |
    | **LD2450 Target-1 / Target-2 / Target-3 Direction** | real-time | Direction of the target: `Stationary`, `Moving away`, `Approaching`, or `NA`. |
    | **LD2450 Zone-1 / Zone-2 / Zone-3 All Target Count** | real-time | Total targets in the zone, stationary or moving. |
    | **LD2450 Zone-1 / Zone-2 / Zone-3 Moving Target Count** | real-time | Count of moving targets in the zone. |
    | **LD2450 Zone-1 / Zone-2 / Zone-3 Still Target Count** | real-time | Count of stationary targets in the zone. |

=== "Configuration"

    #### General

    | Setting | Default | What it does |
    |---------|:-------:|--------------|
    | **ESP Reboot** | — | Restarts the device. Helpful for troubleshooting or refreshing the connection. |
    | **Firmware Type** | WiFi / Ethernet | Switches between the Wi-Fi and Ethernet firmware without re-flashing. After picking the firmware you want, press **Firmware Update** to apply it. |
    | **Reduce DB Reporting** | Off | Filters several entities so they only report when a threshold is met, using less Wi-Fi airtime and less Home Assistant database space. |
    | **SCD40 Temperature Offset** | 18.86 °C | Calibration offset for the SCD40 temperature reading. Disabled by default. |
    | **SCD40 Humidity Offset** | 0 % | Calibration offset for the SCD40 humidity reading. Disabled by default. |
    | **SCD40 Automatic Self Calibration** | On | Lets the SCD40 self-calibrate over time against the lowest CO₂ it sees. Disabled by default. |

    #### LD2412 radar

    | Setting | Default | What it does |
    |---------|:-------:|--------------|
    | **LD2412 Bluetooth** | — | Toggles the LD2412's Bluetooth so you can connect with the <a href="https://wiki.apolloautomation.com/products/msr2/setup/zones-hlk/" target="_blank" rel="noopener">HLK Radartool phone app</a> for tuning. Turn it back off when finished. |
    | **LD2412 Engineering Mode** | — | Enables the g00 to g13 move and still energy readouts used for <a href="https://wiki.apolloautomation.com/products/msr2/setup/zones-ha/" target="_blank" rel="noopener">mmWave tuning</a>. |
    | **LD2412 Timeout** | — | Seconds the LD2412 presence stays detected after the target is lost. |
    | **LD2412 min distance gate** | — | Minimum distance gate for detection. |
    | **LD2412 max distance gate** | — | Maximum distance gate for detection. |
    | **LD2412 g00 to g13 move threshold** | — | Movement sensitivity threshold for each 0.75 m gate, from gate 0 (nearest) to gate 13. Raise a gate's value to tune out false motion at that distance. |
    | **LD2412 g00 to g13 still threshold** | — | Stillness sensitivity threshold for each 0.75 m gate, from gate 0 (nearest) to gate 13. |
    | **LD2412 Factory Reset** | — | Restores the LD2412's move and still thresholds to the manufacturer defaults. |
    | **LD2412 Light Threshold** | — | Light level threshold for the LD2412. Disabled by default. |
    | **LD2412 Light Function** | — | Selects how the LD2412 uses its light reading. Disabled by default. |
    | **LD2412 Hardware output pin level** | — | Output pin level for the LD2412. Disabled by default. |
    | **LD2412 Distance resolution** | — | Distance resolution for the LD2412. Disabled by default. |
    | **LD2412 baud rate** | from module | Serial baud rate the LD2412 uses to talk to the R-PRO-1 (default 115200). Disabled by default; no need to change. |

    #### LD2450 radar

    | Setting | Default | What it does |
    |---------|:-------:|--------------|
    | **LD2450 Bluetooth** | — | Toggles the LD2450's Bluetooth so you can connect with the <a href="https://wiki.apolloautomation.com/products/msr2/setup/zones-hlk/" target="_blank" rel="noopener">HLK Radartool phone app</a> for tuning. Turn it back off when finished. |
    | **LD2450 Multi Target Tracking** | from module | Turns multi-target tracking on or off. Initial state is read from the LD2450 at boot. Disabled by default. |
    | **LD2450 Timeout** | — | Seconds the LD2450 presence stays detected after the target is lost. |
    | **LD2450 Zone Type** | Disabled | Zone detection mode: `Disabled`, `Detection` (only detect targets inside the zone), or `Filter` (exclude the zone from detection). |
    | **LD2450 Zone-1 / Zone-2 / Zone-3 X1, X2** | — | Start and end X coordinates of the zone in mm (-3000 left to 3000 right). |
    | **LD2450 Zone-1 / Zone-2 / Zone-3 Y1, Y2** | — | Start and end Y coordinates of the zone in mm (0 to 6000). |
    | **LD2450 Factory Reset** | — | Resets the LD2450 radar module to its factory settings. |
    | **LD2450 Baud rate** | from module | Serial baud rate the LD2450 uses to talk to the R-PRO-1 (default 256000). Disabled by default; no need to change. |

=== "Diagnostic"

    | Entity | Default Update | What it shows |
    |--------|:--------------:|---------------|
    | **Apollo Firmware Version** | on boot | The Apollo firmware build installed on the device (for example, `26.3.2.1`). |
    | **ESPHome Version** | on boot | The ESPHome version the firmware was compiled with. |
    | **Firmware Update** | — | Shows whether a firmware update is available and lets you update from inside Home Assistant. |
    | **IP Address** | on connect | The device's IP address on your network (Wi-Fi firmware). |
    | **Online** | on change | Connection status of the device to Home Assistant. |
    | **ESP Temperature** | 60s | Internal temperature of the ESP32 chip. Runs warmer than the room because of the processor and Wi-Fi radio. Disabled by default. |
    | **Uptime** | 60s | How long the device has been running since its last reboot. |
    | **LD2412 Dynamic Background Correction Status** | real-time | Whether the LD2412 is running dynamic background correction. |
    | **LD2412 Out Pin** | real-time | State of the LD2412 hardware output pin. Disabled by default. |
    | **LD2412 Firmware** | on boot | Firmware version installed on the LD2412 radar module. Disabled by default. |
    | **LD2412 BT MAC** | on boot | Bluetooth MAC address of the LD2412 radar module. Disabled by default. |
    | **LD2412 g00 to g13 move energy** | real-time | Live move energy for each gate (g00 to g13), used when tuning with Engineering Mode. |
    | **LD2412 g00 to g13 still energy** | real-time | Live still energy for each gate (g00 to g13), used when tuning with Engineering Mode. |
    | **LD2412 Query params** | — | Queries the LD2412's current parameters for debugging or advanced setup. |
    | **LD2412 Restart** | — | Restarts the LD2412 radar module. |
    | **LD2412 Start Dynamic Background Correction** | — | Kicks off a dynamic background correction pass on the LD2412. |
    | **LD2450 Firmware** | on boot | Firmware version installed on the LD2450 radar module. Disabled by default. |
    | **LD2450 BT MAC** | on boot | Bluetooth MAC address of the LD2450 radar module. Disabled by default. |
    | **LD2450 Restart** | — | Restarts the LD2450 radar module. |

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
