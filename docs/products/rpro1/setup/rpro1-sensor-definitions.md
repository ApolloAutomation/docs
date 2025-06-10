---
title: R-PRO-1 Sensor Definitions
description: These are all of the entities exposed by the R-PRO-1 to automate on!
---
# Sensor Definitions

This serves as a list of all sensor definitions to help understand what each entity does for your new R-PRO-1!

???+ info "Controls"

    **RGB Light**

    * One RGB Neopixel LED. Click on the light bulb or color wheel to change the color. Click on the toggle to turn on or off.

    **Calibrate SCD40 to 420ppm**

    * A control option to <a href="https://wiki.apolloautomation.com/products/general/calibrating-and-updating/co2-calibration/" target="_blank" rel="noopener">calibrate the SCD40 CO₂ sensor</a> to <a href="https://climate.nasa.gov/vital-signs/carbon-dioxide/?intent=121" target="_blank" rel="noopener">outdoor baseline levels.</a> (disabled by default)

???+ info "Sensors"

    **CO<sub>2</sub>**

    * CO<sub>2</sub> reading from the SCD40. This will be Unknown if you do not have the CO<sub>2</sub> module. SDC40 can be calibrated <a href="https://wiki.apolloautomation.com/products/general/calibrating-and-updating/co2-calibration/" title="CO<sub>2</sub> Calibration" target="_blank" rel="noopener">following this guide</a>. (disabled by default)

    **ESP Temperature**

    * This is the temperature of the internal microcontroller. Think of it like your measured CPU temp on your PC. (disabled by default)

    **LD2412 Moving Target**

    * Displays a status of "Detected" or "Clear" determined by whether the sensor identifies only a moving target.

    **LD2412 Presence**

    * Displays a status of "Detected" or "Clear" determined by whether the sensor observes a moving or stationary target.

    **LD2412 Still Target**

    * Displays a status of "Detected" or "Clear" determined by whether the sensor identifies only a still target.

    **LD2412 Detection Distance**

    * Displays the distance of the target being tracked. Known to not work properly at this time. (disabled by default)

    **LD2412 Move Energy**

    * Displays the energy of the moving target being tracked. (disabled by default)

    **LD2412 Moving Distance**

    * Displays the distance of the moving target being tracked. Known to not work properly at this time. (disabled by default)

    **LD2412 Still Distance**

    * Displays the distance of the still target being tracked. Known to not work properly at this time. (disabled by default)

    **LD2412 Still Energy**

    * Displays the energy of the still target being tracked. (disabled by default)

    **LD2450 Moving Target Count**

    * Count of all moving targets. (max 3)

    **LD2450 Presence Target Count**

    * Count of all presence targets. (max 3)

    **LD2450 Still Target Count**

    * Count of all still targets. (max 3)

    **LD2450 Target-1 Angle**

    * Angle of target in `degrees (°)` relative to the `ld2450` sensor.

    **LD2450 Target-1 Direction**

    * Direction of the target relative to the `ld2450` sensor. Possible values are: `Stationary`, `Moving away`, `Approaching`, `NA`.

    **LD2450 Target-1 Distance**

    * Distance in `millimeter (mm)` of the target from the `ld2450` sensor along the X-axis (negative for left side of the sensor, positive for right side of the sensor). The `ld2450` module can detect targets from -3000 to 3000 mm in `X` direction.

    **LD2450 Target-1 Resolution**

    * The `ld2450` target detection range resolution in `millimeter (mm)`. (disabled by default)

    **LD2450 Target-1 Speed**

    * Speed of the moving target in `mm/s`.

    **LD2450 Target-1 X**

    * Distance in `millimeter (mm)` of the target from the `ld2450` sensor along the X-axis (negative for left side of the sensor, positive for right side of the sensor). The `ld2450` module can detect targets from -3000 to 3000 mm in `X` direction.

    **LD2450 Target-1 Y**

    * Distance in `millimeter (mm)` of the target from the `ld2450` sensor in the Y direction (near/far). The `ld2450` module can detect targets from 0 to 6000 mm in `Y` direction.

    **LD2450 Target-2 Angle**

    * Angle of target in `degrees (°)` relative to the `ld2450` sensor.

    **LD2450 Target-2 Direction**

    * Direction of the target relative to the `ld2450` sensor. Possible values are: `Stationary`, `Moving away`, `Approaching`, `NA`.

    **LD2450 Target-2 Distance**

    * Distance in `millimeter (mm)` of the target from the `ld2450` sensor along the X-axis (negative for left side of the sensor, positive for right side of the sensor). The `ld2450` module can detect targets from -3000 to 3000 mm in `X` direction.

    **LD2450 Target-2 Resolution**

    * The `ld2450` target detection range resolution in `millimeter (mm)`. (disabled by default)

    **LD2450 Target-2 Speed**

    * Speed of the moving target in `mm/s`.

    **LD2450 Target-2 X**

    * Distance in `millimeter (mm)` of the target from the `ld2450` sensor along the X-axis (negative for left side of the sensor, positive for right side of the sensor). The `ld2450` module can detect targets from -3000 to 3000 mm in `X` direction.

    **LD2450 Target-2 Y**

    * Distance in `millimeter (mm)` of the target from the `ld2450` sensor in the Y direction (near/far). The `ld2450` module can detect targets from 0 to 6000 mm in `Y` direction.

    **LD2450 Target-3 Angle**

    * Angle of target in `degrees (°)` relative to the `ld2450` sensor.

    **LD2450 Target-3 Direction**

    * Direction of the target relative to the `ld2450` sensor. Possible values are: `Stationary`, `Moving away`, `Approaching`, `NA`.

    **LD2450 Target-3 Distance**

    * Distance in `millimeter (mm)` of the target from the `ld2450` sensor along the X-axis (negative for left side of the sensor, positive for right side of the sensor). The `ld2450` module can detect targets from -3000 to 3000 mm in `X` direction.

    **LD2450 Target-3 Resolution**

    * The `ld2450` target detection range resolution in `millimeter (mm)`. (disabled by default)

    **LD2450 Target-3 Speed**

    * Speed of the moving target in `mm/s`.

    **LD2450 Target-3 X**

    * Distance in `millimeter (mm)` of the target from the `ld2450` sensor along the X-axis (negative for left side of the sensor, positive for right side of the sensor). The `ld2450` module can detect targets from -3000 to 3000 mm in `X` direction.

    **LD2450 Target-3 Y**

    * Distance in `millimeter (mm)` of the target from the `ld2450` sensor in the Y direction (near/far). The `ld2450` module can detect targets from 0 to 6000 mm in `Y` direction.

    **LD2450 Zone-1 All Target Count**

    * Total targets detected in the zone, whether they are stationary or in motion.

    **LD2450 Zone-1 Moving Target Count**

    * Count of moving targets in the zone.

    **LD2450 Zone-1 Still Target Count**

    * Count of stationary targets in the zone.

    **LD2450 Zone-2 All Target Count**

    * Total targets detected in the zone, whether they are stationary or in motion.

    **LD2450 Zone-2 Moving Target Count**

    * Count of moving targets in the zone.

    **LD2450 Zone-2 Still Target Count**

    * Count of stationary targets in the zone.

    **LD2450 Zone-3 All Target Count**

    * Total targets detected in the zone, whether they are stationary or in motion.

    **LD2450 Zone-3 Moving Target Count**

    * Count of moving targets in the zone.

    **LD2450 Zone-3 Still Target Count**

    * Count of stationary targets in the zone.

    **LTR390 Light**

    * Light level measured in lux by LTR390.

    **LTR390 UV Index**

    * UV index measured by LTR390.

    **SCD40 Humidity**

    * Humidity reading from the optional SCD40 CO2 sensor.

    **SCD40 Temperature**

    * Temperature reading from the optional SCD40 CO2 sensor.

???+ info "Configuration"

    **ESP Reboot**

    * Performs a restart of the sensor.

    **Firmware Type**

    * Drop-down selector with "WiFi" or "Ethernet" option. Allows you to switch between firmware without re-flashing the device manually. Once you choose the firmware you'd like to use, you then need to click the "PRESS" button next to "Firmware Update".

    **Firmware Update**

    * Button which begins the firmware update process to switch between Wi-Fi and Ethernet firmware options. Process takes around 5 minutes and the sensor reboots with the new firmware once it finishes.

    **Firmware Update**

    * Shows whether a firmware update is available.

    **LD2412 Bluetooth**

    * This allows you to turn on the LD2412 Bluetooth module. This allows you to connect to the HLK Radar Tool phone app [used for tuning](https://wiki.apolloautomation.com/products/msr2/calibrating-and-updating/zones-hlk/).

    **LD2412 Factory Reset**

    * Sets the radar's move and still thresholds back to their original values from the manufacturer.

    **LD2412 g0-g13 Move & Still Threshold Sliders**

    * Sliders which can tune out false positives in 0.75 meter increment "gates" starting at zero meters and going up to 9 meters for the g13 slider.

    **LD2412 Max Move Distance**

    * Maximum distance gate for movement detection. Value between 2 and 13 inclusive.

    **LD2412 Max Still Distance**

    * Maximum distance gate for still detection. Value between 2 and 13 inclusive.

    **LD2412 Mode**

    * Drop-down selector for the mode for the LD2412. Choices are Normal, Engineering, or Dynamic background correction. (Defaults to normal)

    **LD2412 Timeout**

    * Time in seconds before the LD2412 Radar detection entities switch from Occupied to Clear.

    **LD2450 Bluetooth**

    * This allows you to turn on the LD2450 Bluetooth module. This allows you to connect to the HLK Radar Tool phone app [used for tuning](https://wiki.apolloautomation.com/products/msr2/calibrating-and-updating/zones-hlk/).

    **LD2450 Factory Reset**

    * Sets the radar's move and still thresholds back to their original values from the manufacturer.

    **LD2450 Multi Target Tracking**

    * Turn on/off the Multi Target Tracking option. The initial state set based on the corresponding setting as read from LD2450 module at boot.

    **LD2450 Timeout**

    * Time in seconds before the LD2450 Radar detection entities switch from Occupied to Clear.

    **LD2450 Zone Type**

    * Drop-down of the zone detection modes. It can be set to `Disabled`, `Detection` or `Filter`. Selecting the `Disabled` option will disable zone area detection. `Detection` mode is used to detect only targets in the specified area, while `Filter` mode can be used to exclude an area from detection.

    **LD2450 Zone-1 X1**

    * Start X coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the X-axis (negative for left side (-3000) of the sensor, positive for right side (3000) of the sensor).

    **LD2450 Zone-1 X2**

    * End X coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the X-axis (negative for left side (-3000) of the sensor, positive for right side (3000) of the sensor).

    **LD2450 Zone-1 Y1**

    * Start Y coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the Y-axis, values range from 0 to 6000.

    **LD2450 Zone-1 Y2**

    * Start Y coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the Y-axis, values range from 0 to 6000.

    **LD2450 Zone-2 X1**

    * Start X coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the X-axis (negative for left side (-3000) of the sensor, positive for right side (3000) of the sensor).

    **LD2450 Zone-2 X2**

    * End X coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the X-axis (negative for left side (-3000) of the sensor, positive for right side (3000) of the sensor).

    **LD2450 Zone-2 Y1**

    * Start Y coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the Y-axis, values range from 0 to 6000.

    **LD2450 Zone-2 Y2**

    * Start Y coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the Y-axis, values range from 0 to 6000.

    **LD2450 Zone-3 X1**

    * Start X coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the X-axis (negative for left side (-3000) of the sensor, positive for right side (3000) of the sensor).

    **LD2450 Zone-3 X2**

    * End X coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the X-axis (negative for left side (-3000) of the sensor, positive for right side (3000) of the sensor).

    **LD2450 Zone-3 Y1**

    * Start Y coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the Y-axis, values range from 0 to 6000.

    **LD2450 Zone-3 Y2**

    * Start Y coordinate in `millimeter (mm)` of the zone from the `ld2450` sensor along the Y-axis, values range from 0 to 6000.

    **Reduce DB Reporting**

    * A toggle to enable or disable reduced reporting from various entities on the r-pro-1. This will make multiple entities use filters and not update their state unless a threshold is met - ultimately using less Wi-Fi airtime and less database usage in Home Assistant.

    **LD2412 Baud Rate**

    * Baud rate for LD2412 sensor to talk to the R-PRO-1. Defaults to 115200 (disabled by default) no need to ever edit this.

    **LD2412 Distance Resolution**

    * Distance Resolution for LD2412. Disabled by default.

    **LD2412 Hardware output pin level**

    * Hardware outpin pin level for LD2412. Disabled by default.

    **LD2450 Baud Rate**

    * Baud rate for LD2450 sensor to talk to the R-PRO-1. Defaults to 256000 (disabled by default) no need to ever edit this.

    **SCD40 Humidity Offset**

    * Humidity Offset fill in the blank for the optional SCD40 CO2 sensor addon.

    **SCD40 Temperature Offset**

    * Temperature Offset fill in the blank for the optional SCD40 CO2 sensor addon.

    **Radar Engineering Mode**

    * Used to enable g0-g13 threshold sliders for <a href="https://wiki.apolloautomation.com/products/msr2/calibrating-and-updating/zones-ha/" target="_blank" rel="noopener">mmWave tuning</a>.

    ???+ info "Radar Gate Distance Tuning and Timeout"

        ???+ example "Radar Max Move Distance"

            * Maximum distance gate for movement detection. Value between 2 and 8 inclusive
            * Useful in a bathroom or other scenario where you want to avoid detection after a certain gate number (distance).
            * Useful for triggering on "radar target" instead of triggering on zone 1/2/3 occupancy instead.

        ???+ example "Radar Max Still Distance "

            * Maximum distance gate for still detection. Value between 2 and 8 inclusive. Defaults to 8.
            * Useful in a bathroom or other scenario where you want to avoid detection after a certain gate number (distance).
            * Useful for triggering on "radar target" instead of triggering on zone 1/2/3 occupancy instead.

        ???+ info "Radar Timeout"

            The time in seconds that the radar's presence will stay high after the target is lost.

??? info "Radar Gate Configuration"

    !!! warning "Keeping these enabled permanently is bad"

        Please toggle ld2412 Bluetooth on, configure your sensor, then turn ld2412 Bluetooth back off. Otherwise, your Wi-Fi and database could become overwhelmed with excessive traffic.

    **g0 Move Threshold**

    * Configures the movement sensitivity threshold for gate 0.

    **g0 Still Threshold**

    * Configures the stillness sensitivity threshold for gate 0.

    **g1 Move Threshold**

    * Configures the movement sensitivity threshold for gate 1.

    **g1 Still Threshold**

    * Configures the stillness sensitivity threshold for gate 1.

    **g2 Move Threshold**

    * Configures the movement sensitivity threshold for gate 2.

    **g2 Still Threshold**

    * Configures the stillness sensitivity threshold for for gate 2.

    **g3 Move Threshold**

    * Configures the movement sensitivity threshold for gate 3.

    **g3 Still Threshold**

    * Configures the stillness sensitivity threshold for gate 3.

    **g4 Move Threshold**

    * Configures the movement sensitivity threshold for gate 4.

    **g4 Still Threshold**

    * Configures the stillness sensitivity threshold for gate 4.

    **g5 Move Threshold**

    * Configures the movement sensitivity threshold for gate 5.

    **g5 Still Threshold**

    * Configures the stillness sensitivity threshold for gate 5.

    **g6 Move Threshold**

    * Configures the movement sensitivity threshold for gate 6.

    **g6 Still Threshold**

    * Configures the stillness sensitivity threshold for gate 6.

    **g7 Move Threshold**

    * Configures the movement sensitivity threshold for gate 7.

    **g7 Still Threshold**

    * Configures the stillness sensitivity threshold for gate 7.

    **g8 Move Threshold**

    * Configures the movement sensitivity threshold for gate 8.

    **g8 Still Threshold**

    * Configures the stillness sensitivity threshold for gate 8.

    **g9 Move Threshold**

    * Configures the movement sensitivity threshold for gate 8.

    **g9 Still Threshold**

    * Configures the stillness sensitivity threshold for gate 8.

    **g10 Move Threshold**

    * Configures the movement sensitivity threshold for gate 8.

    **g10 Still Threshold**

    * Configures the stillness sensitivity threshold for gate 8.

    **g11 Move Threshold**

    * Configures the movement sensitivity threshold for gate 8.

    **g11 Still Threshold**

    * Configures the stillness sensitivity threshold for gate 8.

    **g12 Move Threshold**

    * Configures the movement sensitivity threshold for gate 8.

    **g12 Still Threshold**

    * Configures the stillness sensitivity threshold for gate 8.

    **g13 Move Threshold**

    * Configures the movement sensitivity threshold for gate 8.

    **g13 Still Threshold**

    * Configures the stillness sensitivity threshold for gate 8.

??? info "Diagnostic"

    **ESP Temperature**

    * Displays the current temperature of the ESP32 chip. (Disabled by Default)

    **LD2412 g0 move energy to g13 move energy**

    * Displays the move energy levels for gates g0 through g13

    **LD2412 g0 move energy to g13 still energy**

    * Displays the still energy levels for gates g0 through g13

    **Online**

    * Shows the connection status.

    **LD2412 Query Params**

    * Button to query parameters for debugging or advanced configurations.

    **LD2412 BT MAC**

    * Displays the Bluetooth MAC Address for the LD2412. (Disabled by Default)

    **LD2412 Firmware**

    * Displays the current firmware version for the LD2412 radar. (Disabled by Default)

    **LD2450 BT MAC**

    * Displays the Bluetooth MAC Address for the LD2450. (Disabled by Default)

    **LD2450 Firmware**

    * Displays the current firmware version for the LD2450 radar. (Disabled by Default)

    **LD2412 Restart Radar**

    * Button to restart the radar sensor.

    **RSSI**

    * Displays the Wi-Fi signal strength.

    **Uptime**

    * Shows the time since last reboot.

[Join our Discord if you need more help! :simple-discord:](https://dsc.gg/apolloautomation){                       .md-button }