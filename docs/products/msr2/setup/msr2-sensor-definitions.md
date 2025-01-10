# Sensor Definitions

Once added to Home Assistant you can configure different settings for your sensor. Below is what each setting does.

!!! info "Controls"

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

    **Radar Detection Distance**

    * The last detected distance by the radar. This will stay at the last known value so sometimes can be misleading.

    **Radar Move Energy**

    * The amount of movement measured by the LD2410B. Faster movements have higher percentage.

    **Radar Moving Target**

    * Does the radar have a moving target it is tracking.

    **Radar Still Distance**

    * The last measured distance of a still target. It will hold the last value so sometimes can be misleading.

    **Radar Still Energy**

    * The energy of the current still target.

    **Radar Still Target**

    * Does the radar have a still target.

    **Radar Target**

    * Does the radar have a still or moving target. Good for triggering automation.

    **Radar Zone 1 Occupancy**

    * This is a configurable zone. Think of zones like distances from the radar unit. Zone 1 might be from 0 cm to 100 cm from the sensor. This is telling you if there is someone in that zone. The zones can be defined in the configuration section with “Radar End Zone 1”

    **Radar Zone 2 Occupancy**

    * This is a configurable zone. Think of zones like distances from the radar unit. Zone 2 might be from 100 cm to 200 cm from the sensor. This is telling you if there is someone in that zone. The zones can be defined in the configuration section with “Radar End Zone 2”

    **Radar Zone 3 Occupancy**

    * This is a configurable zone. Think of zones like distances from the radar unit. Zone 3 might be from 200 cm to 300 cm from the sensor. This is telling you if there is someone in that zone. The zones can be defined in the configuration section with “Radar End Zone 3”

???+ info "Configuration"

    **ESP Reboot**

    * Performs a restart of the sensor

    **Factory Reset Radar**

    * Sets the radar's move thresholds back to their original values from the manufacturer

    **g0-g8 Move & Still Threshold**

    * Please refer to the radar tuning guide: [Here](https://wiki.apolloautomation.com/products/mtr1/setup/zones-ha/)

    **Radar Control Bluetooth**

    * This allows you to turn on the LD2410's Bluetooth. This allows you to connect to the HLK Radar phone app if you wanted to upload new firmware to the radar unit (Not the MSR-1 in general, just the radar chip)

    **Radar Zone 1 Start**

    * This sets the starting distance for Zone 1 in cm. This is the distance from the sensor to the start of Zone 1

    **DPS Temperature Offset**

    * Offsets the heat from the ESP chip for a more accurate temperature.

    **ESP Reboot**

    * A control to reboot the ESP32 system.

    **Factory Reset Radar**

    * Resets the radar to its factory settings.

    Firmware Update

    * Shows the status of the firmware update.

???+ info "Radar End Zones"

    Radar End Zone 1

    * This defines “Zone 1” of the radar. It is a distance from the sensor that specifies what “Zone 1” is. It connects to the “Radar Zone 1 Occupancy” sensor. So if this number is set to “100” that means from 0 to 100 centimeters from the sensor is zone 1.

    Radar End Zone 2

    * This defines “Zone 2” of the radar. It is a distance from the sensor that specifies what “Zone 2” is. It connects to the “Radar Zone 2 Occupancy” sensor. So if this number is set to “200” that means from zone 2 end distance to 200 centimeters from the sensor is zone 2.

    Radar End Zone 3

    * It is a distance from the sensor that specifies what “Zone 3” is. It connects to the “Radar Zone 3 Occupancy” sensor. So if this number is set to “300” that means from zone 2 end distance to 300 centimeters from the sensor is zone 3.

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

??? success "Radar Sensors"

    **Radar Detection Distance**

    * Shows the distance to the detected target, measured in inches.

    **Radar Move Energy**

    * Displays the energy of movement detected by the radar, represented as a percentage.

    **Radar Moving Distance**

    * Displays the distance of a moving target, measured in inches.

    **Radar Moving Target**

    * Detects whether a moving target is present.

    **Radar Still Distance**

    * Displays the distance of a still target, measured in inches.

    **Radar Still Energy**

    * Displays the energy detected from still objects.

    **Radar Still Target**

    * Detects whether a still target is present.

    **Radar Target**

    * Overall detection of a target by the radar.

    **Radar Zone 1 Occupancy**

    * Indicates whether Zone 1 is occupied or clear.

    **Radar Zone 2 Occupancy**

    * Indicates whether Zone 2 is occupied or clear.

    **Radar Zone 3 Occupancy**

    * Indicates whether Zone 3 is occupied or clear.

??? info "Radar Zone Configuration"

    !!! warning "Keeping these enabled permanently is bad"

        Please toggle ld2410 Bluetooth on, configure your sensor, then turn ld2410 Bluetooth back off. Otherwise, your Wi-Fi and database could become overwhelmed with excessive traffic.

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

#### Bluetooth:

•	ld2410 Bluetooth: A toggle to enable or disable Bluetooth functionality for the sensor.

#### Radar Zone Configuration:

•	Radar End Zone 1: Sets the end distance for Zone 1, shown as 50.0 cm.

•	Radar End Zone 2: Sets the end detection range for Zone 2, shown as 150.0 cm.

•	Radar End Zone 3: Sets the end detection range for Zone 3, shown as 250.0 cm.

•	Radar Engineering Mode: A toggle for advanced radar settings adjustments.

•	Radar Max Move Energy: Adjusts the maximum movement energy threshold.

•	Radar Max Still Energy: Adjusts the maximum stillness energy threshold.

•	Radar Timeout: Configures the timeout for the radar in seconds, shown as 5.0 seconds.

•	Radar Zone Boundary: Adjusts the radar zone boundary, shown as 0.0 cm.

•	Startup Light Blink: A toggle to enable or disable the blinking of the startup light.

??? info "Diagnostic"

    **ESP Temperature**

    * Displays the current temperature of the ESP32 chip.

    **g0 move energy to g8 move energy**

    * Displays the move energy levels for gates g0 through g8

    **g0 move energy to g8 still energy**

    * Displays the still energy levels for gates g0 through g8

    **Online**

    * Shows the connection status.

    **Query Params**

    * Button to query parameters for debugging or advanced configurations.

    **Radar Firmware Version**

    * Displays the current firmware version for the radar.

    **Restart Radar**

    * Button to restart the radar sensor.

    **RSSI**

    * Displays the Wi-Fi signal strength.

    **Uptime**

    * Shows the time since last reboot.