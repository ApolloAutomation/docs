# Sensors

### <a href="https://optoelectronics.liteon.com/upload/download/DS86-2015-0004/LTR-390UV_Final_%20DS_V1%201.pdf" target="_blank" rel="noopener">LTR390 UV</a>

* **uv\_index** (*Optional*): UV index (UVI). All options from [Sensor](https://esphome.io/components/sensor/#config-sensor).
* **uv** (*Optional*): Sensor counts for the UV sensor (#). All options from [Sensor](https://esphome.io/components/sensor/#config-sensor).
* **light** (*Optional*): Lux of ambient light (lx). All options from [Sensor](https://esphome.io/components/sensor/#config-sensor).
* **ambient\_light** (*Optional*): Sensor counts for the Ambient light sensor (#). All options from [Sensor](https://esphome.io/components/sensor/#config-sensor).
* **gain** (*Optional*, string): Adjusts the sensitivity of the sensor. A larger value means higher sensitivity. Default is `"X18"`, see table below for options.
* **resolution** (*Optional*, int): ADC resolution. Higher resolutions require longer sensor integration times. Default is `20`, see table below for options.
* **window\_correction\_factor** (*Optional*, float): Window correction factor. Use larger values when using under tinted windows. Default is `1.0`, must be `>= 1.0`.
* **address** (*Optional*, int): Manually specify the I²C address of the sensor. Default is `0x53`.
* **update\_interval** (*Optional*, [Time](https://esphome.io/guides/configuration-types#config-time)): The interval to check the sensor. Defaults to `60s`. It is recommended that the update interval is at least 1 second since updates can take up to 800ms when using a high resolution value.

### <a href="https://files.seeedstudio.com/wiki/Grove-AHT20_I2C_Industrial_Grade_Temperature_and_Humidity_Sensor/AHT20-datasheet-2020-4-16.pdf" target="_blank" rel="noopener">AHT20-F</a>

* **variant** (*Optional*, enum): Set the variant of the device in use. Defaults to `AHT10`.
  * `AHT10` - For AHT10 devices.
  * `AHT20` - For AHT20 and AHT30 devices.
* **temperature** (**Required**): The information for the temperature sensor.
  * All options from [Sensor](https://esphome.io/components/sensor/#config-sensor).
* **humidity** (**Required**): The information for the humidity sensor
  * All options from [Sensor](https://esphome.io/components/sensor/#config-sensor).
* **update\_interval** (*Optional*, [Time](https://esphome.io/guides/configuration-types#config-time)): The interval to check the sensor. Defaults to `60s`.

### <a href="https://www.analog.com/media/en/technical-documentation/data-sheets/ds18b20.pdf" target="_blank" rel="noopener">DS18B20</a>

* **address** (*Optional*, int): The address of the sensor. Required if there is more than one device on the bus.
* **resolution** (*Optional*, int): An optional resolution from 9 to 12. Higher means more accurate. Defaults to the maximum for most Dallas temperature sensors: 12.
* **update\_interval** (*Optional*, [Time](https://esphome.io/guides/configuration-types#config-time)): The interval that the sensors should be checked. Defaults to 60 seconds.
* **one\_wire\_id** (*Optional*, [1-Wire Bus](https://esphome.io/components/one_wire#one-wire)): The ID of the 1-Wire bus to use. Required if there is more than one bus.
* All other options from [Sensor](https://esphome.io/components/sensor/#config-sensor).

# Sensor Definitions

![](../../assets/screenshot-2024-10-03-at-4-10-25-pm.png)

![](../../assets/screenshot-2024-10-03-at-2-25-47-pm.png)

### Controls:

#### Accessory Power:

* This allows you to control the power delivery to the sensor. Toggled ON sends power to the entire device. Toggled OFF only sends power to the ESP chip. When in the OFF position you will be unable turn on the LED light.

#### RGB Light:

* This allows you to control the RGB LED on the PLT-1. You can toggle it on or off directly from the ESPHome dashboard, which can be useful for creating visual alerts or indications related to plant health (e.g., turning green if everything is fine, red if moisture is too low, etc.).

### Sensors:

#### Air Humidity: 48.73%

* This sensor measures the relative humidity of the air surrounding your plant. Ideal humidity levels are crucial for maintaining optimal growth conditions for indoor plants. The reading here shows 48.73%, which might be within a reasonable range depending on the plant type. Too low or too high humidity can stress the plant and affect its ability to absorb nutrients and water properly.

#### Air Temperature: 80.58°F

* This sensor monitors the air temperature around the plant. The temperature is critical to maintaining a suitable growing environment. This current reading of 80.58°F is quite warm, which might be suitable for tropical or heat-loving plants but could be a bit high for others. The ideal temperature range depends on the plant species, and you can set automations to trigger alerts if the temperature goes beyond a specified range.

#### LTR390 Light: 3.4 lx

* This is the light intensity sensor, measured in lux (lx). The light sensor helps you track how much light your plant is receiving. 3.4 lux indicates that the plant is currently in low light conditions, which could be fine for shade-loving plants or indicate that it’s not receiving enough light. For sun-loving plants, you may need to increase light exposure.

#### LTR390 UV Index: 0.00043 UVI

* This sensor measures ultraviolet light (UV Index). UV is another aspect of the light spectrum, important for photosynthesis and general plant health. The low UV Index here indicates very minimal UV radiation, which could be acceptable for most indoor plants since they usually do not require strong UV exposure. However, some plants may benefit from higher levels of UV for robust growth.

#### Soil Moisture: 59%

* The soil moisture sensor measures the water content in the soil as a percentage. A reading of 59% means the soil has a moderate amount of moisture, but depending on the plant species, you may need to adjust watering. The ideal moisture level varies by plant; for instance, succulents prefer drier soil, while tropical plants may require consistently moist soil.

#### Soil Temperature: Unknown

* This field represents the reading from the optional soil temperature probe. It currently shows as “Unknown” because the soil temperature probe may not be connected or is not currently returning data. Soil temperature is crucial for root health and affects the plant’s ability to take up water and nutrients. This optional feature can give deeper insights into the root zone environment.

### Configuration:

#### 100% Water Voltage: 1.5

* This setting defines the voltage that corresponds to 100% soil saturation (completely wet soil). A voltage of 1.5V is being used as the threshold for completely moist soil. This parameter can be tuned based on your plant’s needs, and it’s helpful in creating accurate alerts or automations when soil moisture is low.

#### Dry Voltage: 2.7

* This value represents the voltage at which the soil is considered completely dry. A dry voltage of 2.7V indicates the sensor has defined this threshold for when your plant needs watering. Automations can be created to alert you when the voltage rises to this point, signaling that the soil is too dry.

#### Sleep Duration: 480-720 minutes

* This setting specifies how long the PLT-1 will remain in sleep mode between connection intervals. A 480-720 minute sleep duration is a good balance between battery life and update frequency. You can adjust this depending on how often you want the sensor to wake up and report new data.

#### Sleep After Connecting: Enabled

* This configuration means the PLT-1 will enter sleep mode after it finishes sending data during each connection. Enabling sleep mode helps conserve battery life, making it ideal for a battery-powered setup. This will override the Run Duration setting. Toggling this off will default to the Run Duration setting.

#### Prevent Sleep: Enabled

* With this option enabled, the PLT-1 will not enter sleep mode under certain conditions, ensuring continuous operation. This is useful if you want the sensor to remain active for extended periods, perhaps for monitoring changes in real-time without interruptions.

### Diagnostic:

#### ESP Temperature: 89.8°F

* The ESP module’s internal temperature is displayed here. An ESP temperature of 89.8°F could be a result of the WiFi module being continuously active. While this might not directly impact plant health, it’s useful to monitor as it can affect the accuracy of nearby temperature sensors.

#### Status: Online

* This confirms that the PLT-1 is currently online and connected to the WiFi network, communicating with Home Assistant.

#### RSSI: -56 dBm

* The Received Signal Strength Indicator (RSSI) shows the strength of the WiFi signal. A reading of -56 dBm is fairly decent, indicating that the PLT-1 has a strong enough connection to the WiFi router. Lower RSSI values (closer to zero) represent better signal strength.

#### Uptime: 13 hours 37 minutes

* This shows how long the PLT-1 has been running continuously since its last reboot or power-up. An uptime of 13 hours and 37 minutes indicates that the device has been stable and working for a decent period without any issues.

## Buttons

When looking at the PLT-1 in the below orientation, the boot button is on the left and the reset is on the right by the USB-C port

![](../../assets/plt-1-buttons.png)