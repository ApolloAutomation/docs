# Sensor Definitions

Once added to Home Assistant you can configure different settings for your sensor. Below is what each setting does.

### Controls

- **RGB Light**
    - A RGB Neopixel. Click on the light bulb to change the color. Click on the toggle to turn on or off

### Sensors

- **BME280 Humidity**
    - Humidity reading from the BME280. This is affected by the configuration variable "BME280 Humidity Offset". Changing the offset allows you to dial in the humidity to a known value.
- **BME280 Humidity Calibrated ****- Removed In v23.11.01.1**
    - We calibrated the BME280 against a lab-rated reference sensor. We set the linear offset values in the YAML and this variable is the output.
- **BME280 Pressure**
    - Atmospheric pressure reading from BME280
- **BME280 Temperature**
    - Temperature reading from BME280. This is affected by the configuration variable "BME280 Temperature Offset". Changing the offset allows you to dial in the temperature to a known value.
- **BME280 Temperature Calibrated ****- Removed In v23.11.01.1**
    - We calibrated the BME280 against a lab-rated reference sensor. We set the linear offset values in the YAML and this variable is the output.
- **CO2**
    - True CO2 reading from the SCD40. This will be Unknown if you do not have the CO2 module. This can be calibrated following this guide but does come precalibrated: [Here](https://wiki.apolloautomation.cloud/books/general/page/co2-calibration)
- **ESP Temperature**
    - This is the temperature of the internal ESP chip. Think of it like your measured CPU temp on your PC
- **LTR390 Ambient Light ****- Removed. Value wasn't useful**
    - Light level measured by LTR390
- **LTR390 Light**
    - Light level measured in lux by LTR390
- **LTR390 UV - Removed. Value wasn't useful**
    - UV level measured by LTR390
- **LTR390 UV Index**
    - UV index measured by LTR390
- **Radar Detection Distance**
    - The last detected distance by the radar. This will stay at the last known value so sometimes can be misleading
- **Radar Move Energy**
    - The amount of movement measured by the LD2410B. Faster movements have higher %
- **Radar Moving Target**
    - Does the radar have a moving target it is tracking
- **Radar Still Distance**
    - The last measured distance of a still target. It will hold the last value so sometimes can be misleading
- **Radar Still Energy**
    - The energy of the current still target
- **Radar Still Target**
    - Does the radar have a still target
- **Radar Target**
    - Does the radar have a still or moving target. Good for triggering automation.
- **Radar Zone 1 Occupancy**
    - This is a configurable zone. Think of zones like distances from the radar unit. Zone 1 might be from 0 cm to 120 cm from the sensor. This is telling you if there is someone in that zone. The zones can be defined in the configuration section with “Radar End Zone 1”
- **Radar Zone 2 Occupancy**
    - Same as zone 1 but just the second zone from the sensor
- **Radar Zone 3 Occupancy**
    - Same as zone 1 & 2 but with the third zone.
- **SCD40 Humidity ****- Removed In v23.11.01.1**
    - This is the humidity reading from the SCD40. Will be unknown if you do not have the CO2 module
- **SCD40 Temperature ****- Removed In v23.11.01.1**
    - This is the temperature reading from the SCD40. Will be unknown if you do not have the CO2 module

### Configuration

- **BME280 Humidity Offset**
    - Allows you to adjust the reading of the “BME280 Humidity” sensor to match a known value
- **BME280 Temperature Offset**
    - Allows you to adjust the reading of the “BME280 Temperature” sensor to match a known value
- **CO2 Calibration Number**
    - See calibrating CO2: [Here](https://wiki.apolloautomation.cloud/books/general/page/co2-calibration)
- **ESP Reboot**
    - Performs a restart of the sensor
- **Factory Reset Radar**
    - Sets the radar's move thresholds back to their original values from the manufacturer
- **g0-g8 Move & Still Threshold**
    - Please refer to the radar tuning guide: [Here](https://wiki.apolloautomation.cloud/books/msr-1/page/how-to-tune-mmwave-using-home-assistant)
- **Radar Control Bluetooth**
    - This allows you to turn on the LD2410's Bluetooth. This allows you to connect to the HLK Radar phone app if you wanted to upload new firmware to the radar unit (Not the MSR-1 in general, just the radar chip)
- **Radar Distance Resolution**
    - Best to keep on 0.75m in many cases. If you change it to 0.25m the first few gates become very very sensitive and the maximum detection distance shrinks a lot.
- **Radar Zone 1 Start**
    - This sets the starting distance for Zone 1 in cm. This is the distance from the sensor to the start of Zone 1
- **Radar End Zone 1**
    - This defines “Zone 1” of the radar. It is a distance from the sensor that specifies what “Zone 1” is. It connects to the “Radar Zone 1 Occupancy” sensor. So if this number is set to “10” that means from 0 to 10 centimeters from the sensor is zone 1.
- **Radar End Zone 2**
    - Same as Zone 1. This defines where zone 2 ends
- **Radar End Zone 3**
    - Like Zone 2, this defines where zone 3 ends
- **Radar Max Move Distance**
    - Maximum distance gate for movement detection. Value between 2 and 8 inclusive
- **Radar Max Still Distance**
    - Maximum distance gate for still detection. Value between 2 and 8 inclusive. Defaults to 8.
- **Radar Timeout**
    - The time in seconds that the radar's presence will stay high after the target is lost.
- **SCD40 Humidity Offset ****- Removed In v23.11.01.1**
    - Allows you to adjust the reading of the “SCD40 Humidity” sensor to match a known value.
- **SCD40 Temperature Offset ****- Removed In v23.11.01.1**
    - Allows you to adjust the reading of the “SCD40 Temperature” sensor to match a known value