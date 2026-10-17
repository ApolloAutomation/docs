---
title: "MTR-1 temperature and humidity offsets"
description: "Add temperature and humidity offsets to your MTR-1 so its readings match the room it sits in."
---
# MTR-1 temperature and humidity offsets

Heat from the ESP chip inside the Apollo MTR-1 can skew the temperature and humidity readings from the DPS310 and SCD40 sensors. This page explains why, shows you how to add offsets that correct them, and covers advanced options for even better accuracy.

!!! note "Before you start"

    This guide uses ESPHome and Home Assistant. You add YAML to your MTR-1's ESPHome configuration, then enter the offsets on the MTR-1's device page in the Home Assistant ESPHome integration. The advanced options also use Home Assistant template sensors and automations.

## Why the readings need offsets

The DPS310 and SCD40 sensors are known for their precision in measuring temperature and humidity. Like any sensor, though, they can sometimes give inaccurate readings. For these two sensors, one significant cause is heat from the ESP chip, which changes the environment inside the enclosure and skews the readings.

Temperature and humidity are also linked. When the air temperature rises, the air can hold more moisture, which can lower the relative humidity. When the temperature falls, the air can hold less moisture, which raises the humidity. This relationship plays a big part in how the sensors detect and interpret readings, which makes accuracy even more important.

## How the offsets work

You can adjust the DPS310 and SCD40 temperature offset entities by hand to match the conditions in your home. The firmware subtracts each offset from the raw temperature or humidity reading, and the result is what the Home Assistant entity shows. For example:

`scd40_temperature` entity = raw SCD40 temperature reading - `scd40_offset`

By default, the offsets are preset to values based on Apollo's NIST-certified thermometer. Those values are calibrated for Apollo's environment, so they might not be accurate in your home. Use a reference thermometer, and adjust the offset by the difference between its reading and the MTR-1's.

You'll also see the `dps310_temperature_calibrated`, `scd40_humidity_calibrated`, and `scd40_temperature_calibrated` entities. These use the linear filter in the ESPHome firmware to adjust the readings based on Apollo's collected data. Because every environment is different, these might not always be precise either.

## Add simple offsets

These steps add two boxes to your MTR-1's device page in Home Assistant, one for a humidity offset and one for a temperature offset.

1\. Open your MTR-1's YAML in ESPHome Device Builder.

2\. Add this YAML to the bottom of the file:

```yaml
sensor:
  - id: !extend scd40
    humidity:
      name: "Humidity"
      id: "humidity"
      filters:
        - lambda: return x - id(scd40_humidity_offset).state;
    temperature:
      name: "Temperature"
      id: "temperature"
      filters:
        - lambda: return x - id(scd40_temperature_offset).state;
number:
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
  - platform: template
    name: SCD40 Temperature Offset
    id: scd40_temperature_offset
    initial_value: 14.54
    min_value: -70.0
    max_value: 70.0
    entity_category: "CONFIG"
    unit_of_measurement: "°C"
    optimistic: true
    update_interval: never
    step: 0.1
    mode: box
```

3\. Click **Save**, then **Install**.

4\. Open your MTR-1's device page in the Home Assistant ESPHome integration and fill in the two new offset boxes.

5\. Give the new offsets up to 1 minute to take effect.

Your MTR-1's temperature and humidity readings now include your offsets, and you can fine-tune them from the device page at any time.

## Advanced options

If simple offsets aren't accurate enough, these options go further.

### Model the relationship between sensors

Another way to get accurate readings is to model how the ESP temperature and the other sensors relate to a reference temperature. You do this with a template sensor in Home Assistant that uses a decision tree or Apollo's regression coefficients.

Add the example below to your Home Assistant configuration YAML. Replace xxxxxx with the 6-character suffix of your MTR-1. The coefficients come from Apollo's MSR-1 testing, so treat them as a starting point.

```plaintext
sensor:
  - platform: template
    sensors:
      estimated_reference_temperature:
        friendly_name: "Estimated Temperature"
        unit_of_measurement: '°C'
        value_template: >
          {{
            0.3228 * states('sensor.apollo_mtr_1_xxxxxx_esp_temperature') | float +
            0.8702 * states('sensor.apollo_mtr_1_xxxxxx_scd40_temperature') | float +
            -0.1285 * states('sensor.apollo_mtr_1_xxxxxx_dps310_temperature') | float +
            -0.0491 * states('sensor.apollo_mtr_1_xxxxxx_scd40_humidity') | float +
            0.0851
          }}


      estimated_reference_humidity:
        friendly_name: "Estimated Humidity"
        unit_of_measurement: '%'
        value_template: >
          {{
            -1.2468 * states('sensor.apollo_mtr_1_xxxxxx_esp_temperature') | float +
            -2.1959 * states('sensor.apollo_mtr_1_xxxxxx_scd40_temperature') | float +
            2.9604 * states('sensor.apollo_mtr_1_xxxxxx_dps310_temperature') | float +
            0.2380 * states('sensor.apollo_mtr_1_xxxxxx_scd40_humidity') | float +
            1.8283
          }}
```

### Log your own data

To gather your own data with a reference sensor and your MTR-1 at home, Apollo recommends logging the readings to a CSV file. The automation below writes a row every minute to match the reference sensor.

The block has two parts. Add the part under `#Configuration.yaml` to your `configuration.yaml` file, and the part under `#Automations.yaml` to your `automations.yaml` file. Replace xxxxxx with the 6-character suffix of your MTR-1 here too.

```plaintext
#Configuration.yaml
notify:
  - platform: file
    name: sensor_csv_log
    filename: /config/sensor_log.csv
    timestamp: False

#Automations.yaml
  - id: log_sensor_data_to_csv
    alias: "Log Sensor Data to CSV"
    trigger:
      platform: time_pattern
      minutes: "/1"  # Log data every minute to match reference sensor
    action:
      - service: notify.sensor_csv_log
        data_template:
          message: >
            {{ now().strftime('%Y-%m-%d %H:%M:%S') }},
            {{ states('sensor.apollo_mtr_1_xxxxxx_esp_temperature') | default('NA') }},
            {{ states('sensor.apollo_mtr_1_xxxxxx_scd40_temperature') | default('NA') }},
            {{ states('sensor.apollo_mtr_1_xxxxxx_dps310_temperature') | default('NA') }},
            {{ states('sensor.apollo_mtr_1_xxxxxx_scd40_humidity') | default('NA') }},
            {{ states('number.apollo_mtr_1_xxxxxx_dps310_temperature_offset') | default('NA') }},
            {{ states('number.apollo_mtr_1_xxxxxx_scd40_humidity_offset') | default('NA') }},
            {{ states('number.apollo_mtr_1_xxxxxx_scd40_temperature_offset') | default('NA') }},
            {{ states('sensor.apollo_mtr_1_xxxxxx_uptime') | default('NA') }}
```

### Connect an external sensor with GPIO

For the highest accuracy, connect a temperature and humidity sensor to the exposed mezzanine connector on the back of the Apollo board. This modification can dramatically improve both temperature and humidity readings, giving you data that's as accurate as possible.
