---
title: AIR-1 temperature calibration
description: "Calibrate the AIR-1 temperature reading from its SEN55 to your room using a temperature offset in Home Assistant."
---
# AIR-1 temperature calibration

The Apollo AIR-1 reads temperature from its SEN55 sensor. If that reading doesn't match your room, set the **SEN55 Temperature Offset** on the AIR-1's device page in Home Assistant to bring it in line.

!!! note "Before you start"

    You need a reference thermometer you trust to compare against the AIR-1's temperature reading.

Follow these steps to set the offset.

1\. Place your reference thermometer next to the AIR-1 and compare the two temperature readings.

2\. In Home Assistant, go to **Settings → Devices & services → ESPHome** and select your AIR-1 to open its device page.

[![Open your Home Assistant instance and show an integration.](https://my.home-assistant.io/badges/integration.svg)](https://my.home-assistant.io/redirect/integration/?domain=esphome)

3\. In the **Configuration** card, find **SEN55 Temperature Offset** and adjust it until the AIR-1's temperature matches your reference thermometer. The screenshots below show an example offset of 5.0 °C.

![AIR-1 device page in Home Assistant with the SEN55 temperature offset set to 5.0 °C and circled](/assets/air-1-temperature-offset.png)

The card can cut the entity name short. Hover over the field to confirm it's **SEN55 Temperature Offset**.

![AIR-1 Configuration card close-up with the SEN55 Temperature Offset field set to 5.0 °C](/assets/air-1-temperature-offset-2.png)

Your AIR-1 now applies the offset to its SEN55 temperature reading. For more on how offsets work, and for advanced calibration options, see the [temperature and humidity calibration guide](../../../general/temp-hum-calibration/).
