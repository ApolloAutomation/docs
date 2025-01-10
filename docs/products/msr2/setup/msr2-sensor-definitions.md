# Sensor Definitions

Once added to Home Assistant you can configure different settings for your sensor. Below is what each setting does.

!!! info "Controls"

    **RGB Light**

    * One RGB Neopixel LED. Click on the light bulb or color wheel to change the color. Click on the toggle to turn on or off.

???+ info "Sensors"

    **CO<sub>2</sub>**

    * True CO<sub>2</sub> reading from the SCD40. This will be Unknown if you do not have the CO<sub>2</sub> module. SDC40 can be calibrated [following this guide](https://wiki.apolloautomation.com/products/general/calibrating-and-updating/co2-calibration/ "CO<sub>2</sub> Calibration").

    **ESP Temperature**

    * This is the temperature of the internal microcontroller. Think of it like your measured CPU temp on your PC.

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

### Sensors

* **CO2**
  * True CO2 reading from the SCD40. This will be Unknown if you do not have the CO2 module. This can be calibrated following this guide but does come precalibrated: [Here](https://wiki.apolloautomation.com/products/general/calibrating-and-updating/co2-calibration/ "CO2 Calibration")
* **ESP Temperature**
  * This is the temperature of the internal ESP chip. Think of it like your measured CPU temp on your PC
* **LTR390 Light**
  * Light level measured in lux by LTR390
* **LTR390 UV Index**
  * UV index measured by LTR390
* **Radar Detection Distance**
  * The last detected distance by the radar. This will stay at the last known value so sometimes can be misleading
* **Radar Move Energy**
  * The amount of movement measured by the LD2410B. Faster movements have higher %
* **Radar Moving Target**
  * Does the radar have a moving target it is tracking
* **Radar Still Distance**
  * The last measured distance of a still target. It will hold the last value so sometimes can be misleading
* **Radar Still Energy**
  * The energy of the current still target
* **Radar Still Target**
  * Does the radar have a still target
* **Radar Target**
  * Does the radar have a still or moving target. Good for triggering automation.
* **Radar Zone 1 Occupancy**
  * This is a configurable zone. Think of zones like distances from the radar unit. Zone 1 might be from 0 cm to 120 cm from the sensor. This is telling you if there is someone in that zone. The zones can be defined in the configuration section with “Radar End Zone 1”
* **Radar Zone 2 Occupancy**
  * Same as zone 1 but just the second zone from the sensor
* **Radar Zone 3 Occupancy**
  * Same as zone 1 & 2 but with the third zone.

### Configuration

* **CO2 Calibration Number**
  * See calibrating CO2: [Here](https://wiki.apolloautomation.com/products/general/calibrating-and-updating/co2-calibration/)
* **ESP Reboot**
  * Performs a restart of the sensor
* **Factory Reset Radar**
  * Sets the radar's move thresholds back to their original values from the manufacturer
* **g0-g8 Move & Still Threshold**
  * Please refer to the radar tuning guide: [Here](https://wiki.apolloautomation.com/products/mtr1/setup/zones-ha/)
* **Radar Control Bluetooth**
  * This allows you to turn on the LD2410's Bluetooth. This allows you to connect to the HLK Radar phone app if you wanted to upload new firmware to the radar unit (Not the MSR-1 in general, just the radar chip)
* **Radar Distance Resolution**
  * Best to keep on 0.75m in many cases. If you change it to 0.25m the first few gates become very very sensitive and the maximum detection distance shrinks a lot.
* **Radar Zone 1 Start**
  * This sets the starting distance for Zone 1 in cm. This is the distance from the sensor to the start of Zone 1

??? info "Radar End Zones"

    Radar End Zone 1

    * This defines “Zone 1” of the radar. It is a distance from the sensor that specifies what “Zone 1” is. It connects to the “Radar Zone 1 Occupancy” sensor. So if this number is set to “100” that means from 0 to 100 centimeters from the sensor is zone 1.

    Radar End Zone 2

    * This defines “Zone 2” of the radar. It is a distance from the sensor that specifies what “Zone 2” is. It connects to the “Radar Zone 2 Occupancy” sensor. So if this number is set to “200” that means from zone 2 end distance to 200 centimeters from the sensor is zone 2.

    Radar End Zone 3

    * It is a distance from the sensor that specifies what “Zone 3” is. It connects to the “Radar Zone 3 Occupancy” sensor. So if this number is set to “300” that means from zone 2 end distance to 300 centimeters from the sensor is zone 3.

* **Radar Max Move Distance**
  * Maximum distance gate for movement detection. Value between 2 and 8 inclusive
  * Useful in a bathroom or other scenario where you want to avoid detection after a certain gate count.
  * Useful for triggering on "radar target" instead of triggering on zone 1/2/3 occupancy instead.
* **Radar Max Still Distance**
  * Maximum distance gate for still detection. Value between 2 and 8 inclusive. Defaults to 8.
  * Useful in a bathroom or other scenario where you want to avoid detection after a certain gate count.
  * Useful for triggering on "radar target" instead of triggering on zone 1/2/3 occupancy instead.
* **Radar Timeout**
  * The time in seconds that the radar's presence will stay high after the target is lost.

### Detailed Sensor Definitions

#### Controls:

•	Calibrate SCD40 to 420ppm: A control option to calibrate the SCD40 CO₂ sensor to outdoor baseline levels.

•	RGB Light: Control to toggle the RGB LED on or off for visual notifications.

#### Sensors:

•	CO₂: Detects CO₂ levels in the environment. In this case, the value is unknown, indicating that the reading may not be available or calibrated.

•	DPS310 Pressure: Measures the air pressure in the environment. Here, the pressure is shown as 14.36 psi.

•	DPS310 Temperature: Measures the ambient air temperature using the DPS310 sensor (89.4°F shown).

•	LTR390 Light: Measures the light intensity in lux. Here, the reading is 82.5 lx.

•	LTR390 UV Index: Detects ultraviolet (UV) light levels and provides a UV index. The current reading is 0.00000 UVI, indicating no detectable UV light.

#### Radar Sensors:

•	Radar Detection Distance: Shows the distance to the detected target, measured in inches. Here, it is shown as 52 inches.

•	Radar Move Energy: Displays the energy of movement detected by the radar, represented as a percentage. The reading is 100%, indicating high movement energy.

•	Radar Moving Distance: Measures the distance of moving targets, shown as 57 inches.

•	Radar Moving Target: Detects whether a moving target is present. The value is “Detected,” meaning a moving target is actively being tracked.

•	Radar Still Distance: Shows the distance of still targets, measured at 56 inches.

•	Radar Still Energy: Displays the energy detected from still objects. The value is 100%, showing strong detection of still objects.

•	Radar Still Target: Detects whether a still target is present. The value is “Detected,” meaning a still target is being tracked.

•	Radar Target: Overall detection of a target by the radar. The sensor shows “Detected,” indicating that a target is present.

•	Radar Zone 1 Occupancy: Indicates whether Zone 1 is occupied or clear. In this case, it is “Clear.”

•	Radar Zone 2 Occupancy: Shows whether Zone 2 is occupied. The sensor indicates “Detected,” meaning Zone 2 is occupied.

•	Radar Zone 3 Occupancy: Displays the occupancy status of Zone 3. The reading shows “Clear,” indicating no occupancy.

#### Configuration:

•	DPS Temperature Offset: Offsets the heat from the ESP chip for a more accurate temperature.

•	ESP Reboot: A control to reboot the ESP32 system.

•	Factory Reset Radar: Resets the radar to its factory settings.

•	Firmware Update: Shows the status of the firmware update.

#### Radar Zone Configuration:

•	g0 Move Threshold: Configures the movement sensitivity threshold for Zone 0.

•	g0 Still Threshold: Configures the stillness sensitivity threshold for Zone 0.

•	g1 Move Threshold: Configures the movement sensitivity threshold for Zone 1.

•	g1 Still Threshold: Configures the stillness sensitivity threshold for Zone 1.

•	g2 Move Threshold: Configures the movement sensitivity threshold for Zone 2.

•	g2 Still Threshold: Configures the stillness sensitivity threshold for Zone 2.

•	g3 Move Threshold: Configures the movement sensitivity threshold for Zone 3.

•	g3 Still Threshold: Configures the stillness sensitivity threshold for Zone 3.

•	g4 Move Threshold: Configures the movement sensitivity threshold for Zone 4.

•	g4 Still Threshold: Configures the stillness sensitivity threshold for Zone 4.

•	g5 Move Threshold: Configures the movement sensitivity threshold for Zone 5.

•	g5 Still Threshold: Configures the stillness sensitivity threshold for Zone 5.

•	g6 Move Threshold: Configures the movement sensitivity threshold for Zone 6.

•	g6 Still Threshold: Configures the stillness sensitivity threshold for Zone 6.

•	g7 Move Threshold: Configures the movement sensitivity threshold for Zone 7.

•	g7 Still Threshold: Configures the stillness sensitivity threshold for Zone 7.

•	g8 Move Threshold: Configures the movement sensitivity threshold for Zone 8.

•	g8 Still Threshold: Configures the stillness sensitivity threshold for Zone 8.

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

#### Diagnostic:

•	ESP Temperature: Displays the current temperature of the ESP32 chip, shown here as 131.0°F.

•	g0 to g8 Move Energy: Displays the move energy levels for zones g0 to g8

•	g0 to g8 Still Energy: Displays the still energy levels for zones g0 to g8

•	Online: Shows the connection status, displayed as “Connected.”

•	Query Params: Provides access to query parameters for debugging or advanced configurations.

•	Radar Firmware Version: Displays the current firmware version for the radar, shown as “2.04.23022511.”

•	Restart Radar: Button to restart the radar sensor.

•	RSSI: Displays the WiFi signal strength, currently at -68 dBm.

•	Uptime: Shows the time the device has been running continuously, currently 555:27:36 (555 hours).

•	Device Name: Displays the device’s name on the network, “apollo-msr-2”