# Sensors

#### <a href="https://optoelectronics.liteon.com/upload/download/DS86-2015-0004/LTR-390UV_Final_%20DS_V1%201.pdf" target="_blank" rel="noopener">LTR390 UV</a>

* **uv\_index** (*Optional*): UV index (UVI). All options from [Sensor](https://esphome.io/components/sensor/#config-sensor).
* **uv** (*Optional*): Sensor counts for the UV sensor (#). All options from [Sensor](https://esphome.io/components/sensor/#config-sensor).
* **light** (*Optional*): Lux of ambient light (lx). All options from [Sensor](https://esphome.io/components/sensor/#config-sensor).
* **ambient\_light** (*Optional*): Sensor counts for the Ambient light sensor (#). All options from [Sensor](https://esphome.io/components/sensor/#config-sensor).
* **gain** (*Optional*, string): Adjusts the sensitivity of the sensor. A larger value means higher sensitivity. Default is `"X18"`, see table below for options.
* **resolution** (*Optional*, int): ADC resolution. Higher resolutions require longer sensor integration times. Default is `20`, see table below for options.
* **window\_correction\_factor** (*Optional*, float): Window correction factor. Use larger values when using under tinted windows. Default is `1.0`, must be `>= 1.0`.
* **address** (*Optional*, int): Manually specify the I²C address of the sensor. Default is `0x53`.
* **update\_interval** (*Optional*, [Time](https://esphome.io/guides/configuration-types#config-time)): The interval to check the sensor. Defaults to `60s`. It is recommended that the update interval is at least 1 second since updates can take up to 800ms when using a high resolution value.

#### <a href="https://files.seeedstudio.com/wiki/Grove-AHT20_I2C_Industrial_Grade_Temperature_and_Humidity_Sensor/AHT20-datasheet-2020-4-16.pdf" target="_blank" rel="noopener">AHT20-F</a>

* **variant** (*Optional*, enum): Set the variant of the device in use. Defaults to `AHT10`.
  * `AHT10` - For AHT10 devices.
  * `AHT20` - For AHT20 and AHT30 devices.
* **temperature** (**Required**): The information for the temperature sensor.
  * All options from [Sensor](https://esphome.io/components/sensor/#config-sensor).
* **humidity** (**Required**): The information for the humidity sensor
  * All options from [Sensor](https://esphome.io/components/sensor/#config-sensor).
* **update\_interval** (*Optional*, [Time](https://esphome.io/guides/configuration-types#config-time)): The interval to check the sensor. Defaults to `60s`.

#### <a href="https://www.analog.com/media/en/technical-documentation/data-sheets/ds18b20.pdf" target="_blank" rel="noopener">DS18B20</a>

* **address** (*Optional*, int): The address of the sensor. Required if there is more than one device on the bus.
* **resolution** (*Optional*, int): An optional resolution from 9 to 12. Higher means more accurate. Defaults to the maximum for most Dallas temperature sensors: 12.
* **update\_interval** (*Optional*, [Time](https://esphome.io/guides/configuration-types#config-time)): The interval that the sensors should be checked. Defaults to 60 seconds.
* **one\_wire\_id** (*Optional*, [1-Wire Bus](https://esphome.io/components/one_wire#one-wire)): The ID of the 1-Wire bus to use. Required if there is more than one bus.
* All other options from [Sensor](https://esphome.io/components/sensor/#config-sensor).

# Sensor Definitions

&nbsp;