---
title: How To Add Temp And Humidity From SCD40
description: Tutorial for How To Add Temp And Humidity entities From the SCD40 CO2 sensor.
---
# How To Add Temp And Humidity From SCD40

You add YAML in ESPHome Builder to get SCD40 temperature and humidity entities, with offsets you can adjust in Home Assistant.

1\. Select the ESPHome Builder in the sidebar then click "EDIT" on the device you want to change. If it isn't in your sidebar, the button below opens the app.

[![Open your Home Assistant instance and show the dashboard of an app.](https://my.home-assistant.io/badges/supervisor_app.svg)](https://my.home-assistant.io/redirect/supervisor_app/?app=5c53de3b_esphome&repository_url=https%3A%2F%2Fgithub.com%2Fesphome%2Fhome-assistant-addon)

![ESPHome Builder in the Home Assistant sidebar with the Edit button on an AIR-1 card outlined](/assets/add-temp-hum-scd40-pic-1.png)

2\. Copy the YAML below and put it at the bottom on a new line with no spaces before it.

!!! note "This example is for the AIR-1"

    It also works on the MSR-2 once the CO2 addon is installed. The MTR-1 firmware already includes **SCD40 Temperature** and **SCD40 Humidity** entities with their offsets (disabled by default), so on an MTR-1 with the CO2 addon, enable those entities on the device page instead of adding this YAML.

```yaml
sensor:
  - id: !extend scd40
    temperature:
      name: "SCD40 Temperature"
      id: "temperature"
      filters:
        - lambda: return x - id(scd40_temperature_offset).state;
    humidity:
      name: "SCD40 Humidity"
      id: "humidity"
      filters:
        - lambda: return x - id(scd40_humidity_offset).state;

number:
  - platform: template
    name: SCD40 Temperature Offset
    id: scd40_temperature_offset
    restore_value: true
    initial_value: 14.54
    min_value: -70.0
    max_value: 70.0
    entity_category: "CONFIG"
    unit_of_measurement: "°C"
    optimistic: true
    update_interval: never
    step: 0.1
    mode: box
  - platform: template
    name: SCD40 Humidity Offset
    id: scd40_humidity_offset
    restore_value: true
    initial_value: -18.86
    min_value: -70.0
    max_value: 70.0
    entity_category: "CONFIG"
    unit_of_measurement: "%"
    optimistic: true
    update_interval: never
    step: 0.1
    mode: box
```

![AIR-1 YAML in ESPHome Device Builder with the SCD40 sensor and offset number code outlined](/assets/add-temp-hum-scd40-pic-4.png)

3\. In the top right of the same screen click "SAVE" and then "INSTALL".

4\. Once you see "INFO OTA successful" you are done. Click "STOP" to exit.

![ESPHome Device Builder install log with INFO OTA successful and the Stop button circled](/assets/add-temp-hum-scd40-pic-3.png)

5\. Once you are finished, you will have two new boxes inside the Home Assistant ESPHome integration device page for your device where you can fill in an offset. Give them up to 1 minute to take effect!

[![Open your Home Assistant instance and show an integration.](https://my.home-assistant.io/badges/integration.svg)](https://my.home-assistant.io/redirect/integration/?domain=esphome)

![SCD40 Humidity and SCD40 Temperature offset boxes on the device page in Home Assistant](/assets/add-temp-hum-scd40-pic-5.png)