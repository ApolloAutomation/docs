---
title: MTR-1 Sensor Definitons
description: These are all of the entities exposed by the MTR-1 to automate on!
---
# Sensor Definitions

!!! note "Ensure that the LD2450 firmware version is V2.02.23090617 or later for proper integration functionality. "

    The newer version of the firmware includes an "auto calibrate" function so you might want to test it out!

The [HLK-LD2450](https://www.hlktech.net/index.php?id=1157) mmWave sensor is used in the MTR-1. <a href="https://drive.google.com/drive/folders/1aItrdziwnEqI-ovDWf24Lj6ioALaljFA?usp=sharing" target="_blank" rel="noreferrer nofollow noopener">Click Here</a> for the datasheet.

=== "Android"

    1. Open the Play Store.
    2. Search for "HLK RadarTool" or <a href="https://play.google.com/store/apps/details?id=com.hlk.hlkradartool" target="_blank" rel="noreferrer nofollow noopener">click this link!</a>
    3. Tap **Install**.

=== "iPhone"

    1. Open the App Store.
    2. Search for "HLK RadarTool" or <a href="https://apps.apple.com/us/app/hlkradartool/id1638651152" target="_blank" rel="noreferrer nofollow noopener">click this link!</a>
    3. Tap **Get**.


???+ info "Controls"

    **RGB Light**

    * One RGB Neopixel LED. Click on the light bulb or color wheel to change the color. Click on the toggle to turn on or off.

    **Calibrate SCD40 to 420ppm**

    * A control option to <a href="https://wiki.apolloautomation.com/products/general/calibrating-and-updating/co2-calibration/" target="_blank" rel="noopener">calibrate the SCD40 CO₂ sensor</a> to <a href="https://climate.nasa.gov/vital-signs/carbon-dioxide/?intent=121" target="_blank" rel="noopener">outdoor baseline levels.</a>

???+ info "Sensors"

    **CO<sub>2</sub>**

    * True CO<sub>2</sub> reading from the SCD40. This will be Unknown if you do not have the CO<sub>2</sub> module. SDC40 can be calibrated <a href="https://wiki.apolloautomation.com/products/general/calibrating-and-updating/co2-calibration/" title="CO<sub>2</sub> Calibration" target="_blank" rel="noopener">following this guide</a>.

    **ESP Temperature**

    * This is the temperature of the internal microcontroller. Think of it like your measured CPU temp on your PC.

    **DPS310 Pressure**

    * Measures the air pressure in the environment.

    **DPS310 Temperature**

    * Measures the ambient air temperature using the DPS310 sensor.

    **LTR390 Light**

    * Light level measured in lux by LTR390.

    **LTR390 UV Index**

    * UV index measured by LTR390.

    **Moving Target Count**

    * Count of all moving targets. (max 3)

    **Presence Target Count**

    * Count of all presence targets. (max 3)

    **Still Target Count**

    * Count of all still targets. (max 3)

    **Target-1 Angle**

    * Angle of target in `degrees (°)` relative to the `ld2450` sensor.

    **Target-1 Direction**

    * Direction of the target relative to the `ld2450` sensor. Possible values are: `Stationary`, `Moving away`, `Approaching`, `NA`.

    **Target-1 Distance**

    * Distance in `millimeter (mm)` of the target from the `ld2450` sensor along the X-axis (negative for left side of the sensor, positive for right side of the sensor). The `ld2450` module can detect targets from -3000 to 3000 mm in `X` direction.

    **Target-1 Resolution**

    * The `ld2450` target detection range resolution in `millimeter (mm)`.

    **Target-1 Speed**

    * Speed of the moving target in `mm/s`.

    **Target-1 X**

    * Distance in `millimeter (mm)` of the target from the `ld2450` sensor along the X-axis (negative for left side of the sensor, positive for right side of the sensor). The `ld2450` module can detect targets from -3000 to 3000 mm in `X` direction.

    **Target-1 Y**

    * Distance in `millimeter (mm)` of the target from the `ld2450` sensor in the Y direction (near/far). The `ld2450` module can detect targets from 0 to 6000 mm in `Y` direction.

    **Target-2 Angle**

    * Angle of target in `degrees (°)` relative to the `ld2450` sensor.

    **Target-2 Direction**

    * Direction of the target relative to the `ld2450` sensor. Possible values are: `Stationary`, `Moving away`, `Approaching`, `NA`.

    **Target-2 Distance**

    * Distance in `millimeter (mm)` of the target from the `ld2450` sensor along the X-axis (negative for left side of the sensor, positive for right side of the sensor). The `ld2450` module can detect targets from -3000 to 3000 mm in `X` direction.

    **Target-2 Resolution**

    * The `ld2450` target detection range resolution in `millimeter (mm)`.

    **Target-2 Speed**

    * Speed of the moving target in `mm/s`.

    **Target-2 X**

    * Distance in `millimeter (mm)` of the target from the `ld2450` sensor along the X-axis (negative for left side of the sensor, positive for right side of the sensor). The `ld2450` module can detect targets from -3000 to 3000 mm in `X` direction.

    **Target-2 Y**

    * Distance in `millimeter (mm)` of the target from the `ld2450` sensor in the Y direction (near/far). The `ld2450` module can detect targets from 0 to 6000 mm in `Y` direction.

    **Target-3 Angle**

    * Angle of target in `degrees (°)` relative to the `ld2450` sensor.

    **Target-3 Direction**

    * Direction of the target relative to the `ld2450` sensor. Possible values are: `Stationary`, `Moving away`, `Approaching`, `NA`.

    **Target-3 Distance**

    * Distance in `millimeter (mm)` of the target from the `ld2450` sensor along the X-axis (negative for left side of the sensor, positive for right side of the sensor). The `ld2450` module can detect targets from -3000 to 3000 mm in `X` direction.

    **Target-3 Resolution**

    * The `ld2450` target detection range resolution in `millimeter (mm)`.

    **Target-3 Speed**

    * Speed of the moving target in `mm/s`.

    **Target-3 X**

    * Distance in `millimeter (mm)` of the target from the `ld2450` sensor along the X-axis (negative for left side of the sensor, positive for right side of the sensor). The `ld2450` module can detect targets from -3000 to 3000 mm in `X` direction.

    **Target-3 Y**

    * Distance in `millimeter (mm)` of the target from the `ld2450` sensor in the Y direction (near/far). The `ld2450` module can detect targets from 0 to 6000 mm in `Y` direction.

    **Zone-1 All Target Count**

    * Total targets detected in the zone, whether they are stationary or in motion.

    **Zone-1 Moving Target Count**

    * Count of moving targets in the zone.

    **Zone-1 Still Target Count**

    * Count of stationary targets in the zone.

    **Zone-2 All Target Count**

    * Total targets detected in the zone, whether they are stationary or in motion.

    **Zone-2 Moving Target Count**

    * Count of moving targets in the zone.

    **Zone-2 Still Target Count**

    * Count of stationary targets in the zone.

    **Zone-3 All Target Count**

    * Total targets detected in the zone, whether they are stationary or in motion.

    **Zone-3 Moving Target Count**

    * Count of moving targets in the zone.

    **Zone-3 Still Target Count**

    * Count of stationary targets in the zone.

???+ info "Configuration"

    **DPS310 Temperature Offset**

    * Offset value of the DPS310 Temperature.

    **ESP Reboot**

    * Performs a restart of the sensor.

    **Firmware**

    * Shows available updates and allows updating inside of Home Assistant.

    **LD2450 Bluetooth**

    * Toggles the Bluetooth of the LD2450 to directly connect with a phone to the HLK Radartool App.

    **Multi Target Tracking**

    * Turn on/off the Multi Target Tracking option. The initial state set based on the corresponding setting as read from LD2450 module at boot.

    **Timeout**

    * The duration, in seconds, for which the [presence states](https://esphome.io/components/sensor/ld2450.html#ld2450-binary-sensors) will persist even after the detection is cleared. Default is `5` seconds.

    **Zone Type**

    * Control the zone detection modes. It can be set to `Disabled`, `Detection` or `Filter`. Selecting the `Disabled` option will disable zone area detection. `Detection` mode is used to detect only targets in the specified area, while `Filter` mode can be used to exclude an area from detection.

    **Zone-1 X1**

    * Start X coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the X-axis (negative for left side (-3000) of the sensor, positive for right side (3000) of the sensor).

    **Zone-1 X2**

    * End X coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the X-axis (negative for left side (-3000) of the sensor, positive for right side (3000) of the sensor).

    **Zone-1 Y1**

    * Start Y coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the Y-axis, values range from 0 to 6000.

    **Zone-1 Y2**

    * Start Y coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the Y-axis, values range from 0 to 6000.

    **Zone-2 X1**

    * Start X coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the X-axis (negative for left side (-3000) of the sensor, positive for right side (3000) of the sensor).

    **Zone-2 X2**

    * End X coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the X-axis (negative for left side (-3000) of the sensor, positive for right side (3000) of the sensor).

    **Zone-2 Y1**

    * Start Y coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the Y-axis, values range from 0 to 6000.

    **Zone-2 Y2**

    * Start Y coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the Y-axis, values range from 0 to 6000.

    **Zone-3 X1**

    * Start X coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the X-axis (negative for left side (-3000) of the sensor, positive for right side (3000) of the sensor).

    **Zone-3 X2**

    * End X coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the X-axis (negative for left side (-3000) of the sensor, positive for right side (3000) of the sensor).

    **Zone-3 Y1**

    * Start Y coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the Y-axis, values range from 0 to 6000.

    **Zone-3 Y2**

    * Start Y coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the Y-axis, values range from 0 to 6000.

??? info "Diagnostic"

    **ESP Temperature**

    * Displays the current temperature of the ESP32 chip.

    **LD2450 BT MAC**

    * Bluetooth MAC Address of the LD2450 mmWave sensor.

    **LD2450 Firmware**

    * Firmware version installed on the LD2450. Defaults to 2.04.23101915

    **Online**

    * Shows the connection status.

    **Uptime**

    * Shows the time since last reboot.

    **RSSI**

    * Displays the Wi-Fi signal strength.

[Join our Discord if you need more help! :simple-discord:](https://dsc.gg/apolloautomation){                   .md-button }