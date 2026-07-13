---
title: SEN65 Air Quality Sensor
description: >-
  Add a Sensirion SEN65 air quality sensor to your ESPHome Starter Kit Breakout
  Module, then learn what each reading means and what to automate on.
---
# SEN65 Air Quality Sensor

The <a href="https://sensirion.com/products/catalog/SEN65" target="_blank" rel="noreferrer nofollow noopener">Sensirion SEN65</a> is an all-in-one air quality sensor. One module measures particulate matter, temperature, humidity, volatile organic compounds (VOCs), and nitrogen oxides (NOx), and it plugs straight into the Breakout Module's SEN6x port. Grab one from the <a href="https://apolloautomation.com/products/sen65-particulate-matter-sensor" target="_blank" rel="noreferrer nofollow noopener">Apollo store</a>.

It's part of Sensirion's SEN6x family. The SEN65 does not read CO₂ or formaldehyde, those are on other variants like the SEN66 (adds CO₂) and SEN68 (adds formaldehyde).

## Attach SEN65

The SEN65 comes with its own ribbon cable. Plug it into the **SEN6x** port at the bottom right of the [Breakout Module](/products/ESPHome-Starter-Kit/modules/apollo-breakout-module.md#pinout), latch side facing up. The connector is keyed, so it only fits one way.

![](/assets/esphome-starter-kit-breakout-module-sen6x.webp)

The SEN6x port is on the same I2C bus as the other connectors: **SCL on GPIO0**, **SDA on GPIO1**.

## Add to ESPHome Device Builder

In your device config, add the <a href="https://esphome.io/components/sensor/sen6x/" target="_blank" rel="noreferrer nofollow noopener">SEN6x</a> component. It sits on the I2C bus at address `0x6B`. Set **SCL to pin 0** and **SDA to pin 1**, and turn on the pullup toggle for both pins, the same as any other I2C sensor on the breakout.

New to adding I2C parts? The [Breakout Module](/products/ESPHome-Starter-Kit/modules/apollo-breakout-module.md#add-to-esphome-device-builder) page walks through it. Flash the device once you've added the component, and the SEN65's readings show up alongside your other entities.

??? note "What the SEN65 YAML does"

    Adding the SEN6x component, plus an AQI sensor for the [NowCast AQI](#nowcast-aqi) below, gives you a config like this:

    ```yaml
    i2c:
      sda: GPIO1
      scl: GPIO0
      scan: true

    sensor:
      - platform: sen6x
        type: SEN65
        address: 0x6B
        update_interval: 60s
        pm_1_0:
          name: "PM <1µm"
        pm_2_5:
          id: sen65_pm_2_5
          name: "PM <2.5µm"
        pm_4_0:
          name: "PM <4µm"
        pm_10_0:
          id: sen65_pm_10_0
          name: "PM <10µm"
        temperature:
          name: "Temperature"
        humidity:
          name: "Humidity"
        voc:
          name: "VOC Index"
        nox:
          name: "NOx Index"

      - platform: aqi
        name: "NowCast AQI"
        pm_2_5: sen65_pm_2_5
        pm_10_0: sen65_pm_10_0
        calculation_type: AQI
    ```

    Each option does something specific:

    | Option | What it does |
    | --- | --- |
    | **I2C bus** | |
    | `i2c.sda: GPIO1` / `scl: GPIO0` | The breakout's shared I2C data and clock pins. |
    | `i2c.scan: true` | Logs any I2C devices found on boot, handy for confirming the SEN65 is detected. |
    | **SEN65 sensor** | |
    | `platform: sen6x` | The ESPHome component for Sensirion's SEN6x family. |
    | `type: SEN65` | Tells the component which variant you have, so it reads only the sensors the SEN65 has. |
    | `address: 0x6B` | The SEN65's fixed I2C address. |
    | `update_interval: 60s` | How often it takes a reading. |
    | `pm_2_5.id` / `pm_10_0.id` | Internal handles so the AQI sensor can read these two PM values. |
    | **NowCast AQI** | |
    | `platform: aqi` | Calculates a single Air Quality Index number from PM readings. |
    | `pm_2_5` / `pm_10_0` | Point the AQI sensor at the two PM handles above. |
    | `calculation_type: AQI` | Use the US EPA AQI formula. |
    | `name: NowCast AQI` | Named this way because it's based only on PM, not the full pollutant set a real AQI uses. |

    The SEN65 needs about a minute after boot to warm up before the VOC and NOx readings settle.

## Sensor readings

| Reading | Details |
|---------|---------|
| **PM &lt;1µm** | Ultra-fine particles smaller than 1 micrometer, often from smoke, cooking, or exhaust. |
| **PM &lt;2.5µm** | PM2.5, fine particles from combustion and industrial activity. The most widely tracked for health. |
| **PM &lt;4µm** | Particles smaller than 4 micrometers. |
| **PM &lt;10µm** | PM10, includes dust, pollen, and mold. |
| **Temperature** | Ambient air temperature. Runs a little warm right after power-on while the sensor settles. |
| **Humidity** | Relative humidity in the air. |
| **VOC Index** | Volatile organic compounds from paints, cleaning products, and cooking, on a relative scale where 100 is your recent average. <a href="https://sensirion.com/media/documents/02232963/6294E043/Info_Note_VOC_Index.pdf" target="_blank" rel="noreferrer nofollow noopener">How the VOC Index works</a>. |
| **NOx Index** | Nitrogen oxides from gas stoves and other combustion, on the same kind of relative scale where 1 is the baseline. <a href="https://sensirion.com/media/documents/9F289B95/6294DFFC/Info_Note_NOx_Index.pdf" target="_blank" rel="noreferrer nofollow noopener">How the NOx Index works</a>. |

## Safe levels

### Particulate matter

<a href="https://www.epa.gov/pm-pollution/particulate-matter-pm-basics" target="_blank" rel="noreferrer nofollow noopener">Per the EPA</a>, particulate matter is a mix of solid particles and liquid droplets in the air. The smaller the particle, the deeper it reaches into your lungs, so PM1 and PM2.5 matter most indoors where cooking, candles, and poor ventilation are the usual sources. (1)
{ .annotate }

1.  Trigger a fan, air purifier, or HVAC when PM2.5 climbs. Keeping PM2.5 below **12 µg/m³** indoors is a good general target, below **5 µg/m³** for ideal long-term health.

| PM2.5 (µg/m³) | AQI Category | What it means |
|---|---|---|
| 0.0 – 12.0 | Good | Air quality is satisfactory. |
| 12.1 – 35.4 | Moderate | Acceptable; some risk for sensitive people. |
| 35.5 – 55.4 | Unhealthy for Sensitive Groups | Risk for those with heart or lung issues, children, older adults. |
| 55.5 – 150.4 | Unhealthy | Everyone may start to feel effects. |
| 150.5+ | Very Unhealthy to Hazardous | Health alert. |

### NowCast AQI

Comparing µg/m³ values across PM1, PM2.5, PM4, and PM10 gets fiddly. The <a href="https://esphome.io/components/sensor/aqi/" target="_blank" rel="noreferrer nofollow noopener">AQI</a> component folds your PM2.5 and PM10 into a single 0-500 number that maps to the categories in the table above: bigger is worse. Add it in Device Builder pointed at your SEN65's PM2.5 and PM10 sensors.

!!! tip "Rename the entity to NowCast AQI"

    A real Air Quality Index also factors in ozone, carbon monoxide, and other gases the SEN65 doesn't measure. Naming the entity **NowCast AQI** keeps it honest about what it's based on. It's still the easiest single value to automate on: fire an alert at 100 (Moderate) or 150 (Unhealthy for Sensitive Groups) and anyone in the house understands why.

### VOC and NOx

Both are relative scales that behave like your nose, comparing the current air to the sensor's recent history rather than reporting an absolute amount. On the <a href="https://sensirion.com/media/documents/02232963/6294E043/Info_Note_VOC_Index.pdf" target="_blank" rel="noreferrer nofollow noopener">VOC Index</a>, **100** is your recent average, so a reading above 100 means more VOCs from cooking, cleaning, or breathing. (1) The <a href="https://sensirion.com/media/documents/9F289B95/6294DFFC/Info_Note_NOx_Index.pdf" target="_blank" rel="noreferrer nofollow noopener">NOx Index</a> uses **1** as its baseline, and anything above it usually means combustion like a gas stove. (2)
{ .annotate }

1.  Run a fan or send an alert when the VOC Index rises above 100. It reacts to the change in your space rather than an absolute number.
2.  Kick on the range hood or a fan when the NOx Index climbs past 1, handy while cooking on gas.

--8<-- "_snippets/community-help.md"
