---
title: Temp and humidity calibration and offset examples
description: Learn why Apollo temperature and humidity readings can be off, then correct them with simple offsets or advanced template sensors.
---
# Simple and advanced temperature and humidity offsets

Your Apollo device's temperature and humidity readings can differ from the true value. This page explains why, then shows how to correct them: simple offsets you set from the device page, or advanced template sensors that estimate the true values from all of your readings.

## Why readings can be off

The BME280 and SCD40 sensors are known for measuring temperature and humidity precisely. Like any sensor, though, they can sometimes give inaccurate readings. One significant cause is heat from the ESP chip, which warms the air inside the enclosure and skews the readings.

Temperature and humidity are also linked. When the air temperature rises, the air can hold more moisture, which can lower the relative humidity. When the temperature falls, the air can hold less moisture, so the humidity rises. This relationship plays a big part in how the sensors detect and interpret readings, which makes accurate readings even more important.

## Add simple offsets

Add two offset boxes to your device so you can correct its SCD40 temperature and humidity readings from Home Assistant.

1\. In ESPHome Device Builder, open your device's YAML and paste the following at the bottom:

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
```

2\. Click **Save**, then **Install**.

3\. In Home Assistant, open your device's page in the ESPHome integration. Fill in your offsets in the two new boxes, **SCD40 Humidity Offset** and **SCD40 Temperature Offset**.

Give the new offsets up to 1 minute to take effect. The next section explains how to choose the right values.

## How the offsets work

You can adjust the BME280 and SCD40 Temperature Offset entities by hand to match the conditions in your home. The firmware subtracts each offset from the raw temperature or humidity reading, and the result is what the sensor's entity shows in Home Assistant. For example, the `scd40_temperature` entity equals the raw SCD40 temperature reading minus `scd40_offset`.

The default offsets come from our NIST-certified thermometer and are calibrated for our environment, so they might not be accurate in your home. To fine-tune them, compare your sensor with a reference thermometer and adjust the offsets by the difference between the two readings.

You may also notice the `bme280_humidity_calibrated`, `scd40_humidity_calibrated`, `bme280_temperature_calibrated`, and `scd40_temperature_calibrated` entities. These use the linear filter in the ESPHome firmware to adjust the readings based on data we collected. Because every home is different, they might not always be precise either.

## Advanced: model the relationship between sensors

Another way to get accurate readings is to model how the ESP chip temperature and the other sensors relate to a reference temperature. A template sensor in Home Assistant does this for you: it combines your sensor's live readings into an estimated true temperature and humidity, using either a decision tree or our regression coefficients (the multipliers in the example below).

Add the example below to your Home Assistant configuration YAML. Its entity IDs belong to one Apollo MSR-1 (`apollo_msr_1_a79e24`), so replace them with your own device's entity IDs.

```plaintext
sensor:
  - platform: template
    sensors:
      estimated_reference_temperature:
        friendly_name: "Estimated Temperature"
        unit_of_measurement: '°C'
        value_template: >
          {{
            0.3228 * states('sensor.apollo_msr_1_a79e24_esp_temperature') | float +
            0.8702 * states('sensor.apollo_msr_1_a79e24_scd40_temperature') | float +
            -0.1285 * states('sensor.apollo_msr_1_a79e24_bme280_temperature') | float +
            -0.0491 * states('sensor.apollo_msr_1_a79e24_scd40_humidity') | float +
            0.0851 * states('sensor.apollo_msr_1_a79e24_bme280_humidity') | float +
            -17.4840
          }}


      estimated_reference_humidity:
        friendly_name: "Estimated Humidity"
        unit_of_measurement: '%'
        value_template: >
          {{
            -1.2468 * states('sensor.apollo_msr_1_a79e24_esp_temperature') | float +
            -2.1959 * states('sensor.apollo_msr_1_a79e24_scd40_temperature') | float +
            2.9604 * states('sensor.apollo_msr_1_a79e24_bme280_temperature') | float +
            0.2380 * states('sensor.apollo_msr_1_a79e24_scd40_humidity') | float +
            1.8283 * states('sensor.apollo_msr_1_a79e24_bme280_humidity') | float +
            40.1686
          }}
```

### Collect your own data

To gather your own data with a reference sensor and an MSR-1 in your home, we recommend logging the readings to a CSV file. The YAML below logs once a minute to match the reference sensor. As its comments show, the `notify` entry goes in `configuration.yaml` and the automation goes in `automations.yaml`.

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
            {{ states('sensor.apollo_msr_1_a79e24_esp_temperature') | default('NA') }},
            {{ states('sensor.apollo_msr_1_a79e24_scd40_temperature') | default('NA') }},
            {{ states('sensor.apollo_msr_1_a79e24_bme280_temperature') | default('NA') }},
            {{ states('sensor.apollo_msr_1_a79e24_scd40_humidity') | default('NA') }},
            {{ states('sensor.apollo_msr_1_a79e24_bme280_humidity') | default('NA') }},
            {{ states('number.apollo_msr_1_a79e24_bme280_temperature_offset') | default('NA') }},
            {{ states('number.apollo_msr_1_a79e24_scd40_humidity_offset') | default('NA') }},
            {{ states('number.apollo_msr_1_a79e24_bme280_humidity_offset') | default('NA') }},
            {{ states('number.apollo_msr_1_a79e24_scd40_temperature_offset') | default('NA') }},
            {{ states('sensor.apollo_msr_1_a79e24_uptime') | default('NA') }}
```

## Advanced accuracy with GPIO

For the highest accuracy, connect a temperature and humidity sensor to the exposed mezzanine connector on the back of your Apollo board. This modification can dramatically improve both temperature and humidity readings, giving you data that's as accurate as possible.
