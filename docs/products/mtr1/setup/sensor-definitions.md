---
title: MTR-1 Sensor Definitions
description: These are all of the entities exposed by the MTR-1 to automate on!
---
# Sensor Definitions

Once added to Home Assistant you can configure different settings for your MTR-1. Use the tabs below to see what each entity does, grouped the same way Home Assistant displays them.

!!! note "How often readings update"

    The **Default Update** column is how often each entity refreshes. Radar entities update in real time as targets move. The **LTR390 Light** and **LTR390 UV Index** sensors use the interval set by the **LTR390 Update Interval** number (60s by default).

=== "Controls"

    | Control | What it does |
    |---------|--------------|
    | **RGB Light** | One RGB Neopixel LED. Click the light bulb or color wheel to change the color. Use the toggle to turn it on or off. |
    | **Calibrate SCD40 To 420ppm** | Forces a fresh-air calibration of the SCD40 CO₂ sensor to the <a href="https://wiki.apolloautomation.com/products/general/calibrating-and-updating/co2-calibration/" target="_blank" rel="noopener">outdoor baseline</a> (about <a href="https://climate.nasa.gov/vital-signs/carbon-dioxide/?intent=121" target="_blank" rel="noopener">420 ppm</a>). Run it outdoors or next to an open window. Only needed when **CO2 Auto Calibration** is off. |

=== "Sensors"

    #### Air quality &amp; light

    | Sensor | Default Update | Details |
    |--------|:--------------:|---------|
    | **CO2** | 60s | True NDIR reading from the SCD40. Shows *Unknown* if you do not have the CO₂ module. You can <a href="https://wiki.apolloautomation.com/products/general/calibrating-and-updating/co2-calibration/" target="_blank" rel="noopener">re-calibrate it to the outdoor baseline</a>. |
    | **DPS310 Pressure** | 30s | Barometric air pressure. A small subset of devices do not include a DPS310 sensor. If this reads *Unknown*, your device may be one of these units. |
    | **DPS310 Temperature** | 30s | Ambient air temperature from the DPS310. A small subset of devices do not include a DPS310 sensor. |
    | **LTR390 Light** | 60s* | Ambient light level in lux. *Polls at the **LTR390 Update Interval** (60s by default). |
    | **LTR390 UV Index** | 60s* | UV index measured by the LTR390. *Polls at the **LTR390 Update Interval**. |
    | **SCD40 Temperature** | 60s | Temperature from the SCD40. Disabled by default. Adjusted by the **SCD40 Temperature Offset**. |
    | **SCD40 Humidity** | 60s | Humidity from the SCD40. Disabled by default. Adjusted by the **SCD40 Humidity Offset**. |

    #### Radar (LD2450 mmWave)

    | Sensor | Default Update | Details |
    |--------|:--------------:|---------|
    | **LD2450 Presence** | real-time | Whether the radar currently detects any target. Great for occupancy automations. |
    | **LD2450 Moving Target** | real-time | Whether a moving target is detected. |
    | **LD2450 Still Target** | real-time | Whether a stationary target is detected. |
    | **Presence Target Count** | real-time | Count of all presence targets (max 3). |
    | **Moving Target Count** | real-time | Count of all moving targets (max 3). |
    | **Still Target Count** | real-time | Count of all still targets (max 3). |
    | **Target-1 / Target-2 / Target-3 X** | real-time | Distance in mm of the target from the sensor along the X-axis (negative = left, positive = right, range -3000 to 3000). |
    | **Target-1 / Target-2 / Target-3 Y** | real-time | Distance in mm of the target from the sensor in the Y direction (near/far, range 0 to 6000). |
    | **Target-1 / Target-2 / Target-3 Speed** | real-time | Speed of the moving target in mm/s. |
    | **Target-1 / Target-2 / Target-3 Angle** | real-time | Angle of the target in degrees relative to the sensor. |
    | **Target-1 / Target-2 / Target-3 Distance** | real-time | Straight-line distance of the target from the sensor. |
    | **Target-1 / Target-2 / Target-3 Resolution** | real-time | Target detection range resolution in mm. |
    | **Target-1 / Target-2 / Target-3 Direction** | real-time | Direction of the target: `Stationary`, `Moving away`, `Approaching`, or `NA`. |
    | **Zone-1 / Zone-2 / Zone-3 All Target Count** | real-time | Total targets in the zone, stationary or moving. |
    | **Zone-1 / Zone-2 / Zone-3 Moving Target Count** | real-time | Count of moving targets in the zone. |
    | **Zone-1 / Zone-2 / Zone-3 Still Target Count** | real-time | Count of stationary targets in the zone. |

=== "Configuration"

    | Setting | Default | What it does |
    |---------|:-------:|--------------|
    | **ESP Reboot** | — | Restarts the device. Helpful for troubleshooting or refreshing the connection. |
    | **Multi Target Tracking** | from module | Turns multi-target tracking on or off. Initial state is read from the LD2450 at boot. |
    | **Timeout** | 5 s | How long presence stays detected after the target is lost. See the <a href="https://esphome.io/components/sensor/ld2450.html#ld2450-binary-sensors" target="_blank" rel="noopener">ESPHome LD2450 docs</a>. |
    | **Zone Type** | Disabled | Zone detection mode: `Disabled`, `Detection` (only detect targets inside the zone), or `Filter` (exclude the zone from detection). |
    | **Zone-1 / Zone-2 / Zone-3 X1, X2** | — | Start and end X coordinates of the zone in mm (-3000 left to 3000 right). |
    | **Zone-1 / Zone-2 / Zone-3 Y1, Y2** | — | Start and end Y coordinates of the zone in mm (0 to 6000). |
    | **DPS310 Pressure Offset** | 0.0 hPa | Calibration offset for the DPS310 pressure reading. Disabled by default. |
    | **DPS310 Temperature Offset** | — | Calibration offset for the DPS310 temperature reading. |
    | **SCD40 Temperature Offset** | — | Calibration offset for the SCD40 temperature reading. Disabled by default. |
    | **SCD40 Humidity Offset** | — | Calibration offset for the SCD40 humidity reading. Disabled by default. |
    | **CO2 Auto Calibration** | On | Keeps the SCD40 CO₂ sensor calibrated automatically. The sensor assumes it sees fresh air (about <a href="https://climate.nasa.gov/vital-signs/carbon-dioxide/?intent=121" target="_blank" rel="noopener">420 ppm</a>) at least once a week and corrects its baseline to match. Turn it off if the device sits in a space that rarely gets fresh air, then calibrate manually with **Calibrate SCD40 To 420ppm** every 1 to 2 years. |
    | **LTR390 Update Interval** | 60 s | How often the LTR390 light and UV sensors poll (1 to 300 seconds). |
    | **LD2450 Bluetooth** | — | Toggles the LD2450's Bluetooth so you can connect with the HLK Radartool phone app. |
    | **Baud rate** | from module | Serial baud rate for the LD2450 module. |
    | **Factory Reset ESP** | — | Erases settings and returns the device to factory firmware defaults. Disabled by default. |
    | **Factory Reset LD2450** | — | Resets the LD2450 radar module to its factory settings. |

=== "Diagnostic"

    | Entity | Default Update | What it shows |
    |--------|:--------------:|---------------|
    | **Apollo Firmware Version** | on boot | The Apollo firmware build installed on the device (for example, `26.3.2.1`). |
    | **ESPHome Version** | on boot | The ESPHome version the firmware was compiled with. |
    | **Firmware Update** | — | Shows whether a firmware update is available and lets you update from inside Home Assistant. Separate from the **Apollo Firmware Version** and **ESPHome Version** sensors above. |
    | **IP Address** | on connect | The device's IP address on your network. |
    | **Online** | on change | Connection status of the device to Home Assistant. |
    | **RSSI** | 60s | Wi-Fi signal strength in dBm. Values closer to 0 are stronger; a weak signal can affect reliability. |
    | **ESP Temperature** | 60s | Internal temperature of the ESP32 chip. Runs warmer than the room because of the processor and Wi-Fi radio. |
    | **Uptime** | 60s | How long the device has been running since its last reboot. |
    | **LD2450 Firmware** | on boot | Firmware version installed on the LD2450 radar module. |
    | **LD2450 BT MAC** | on boot | Bluetooth MAC address of the LD2450 radar module. |

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
