---
title: AIR-1 general tips
description: >-
  Learn which AIR-1 sensor readings matter most, and the safe and unsafe
  thresholds to alert or automate on.
---
# AIR-1 general tips

Your Apollo AIR-1 has several different types of sensors. This guide helps you understand which readings you should be concerned with, and the safe and unsafe thresholds to alert or automate on.

## <a href="https://sensirion.com/products/catalog/SEN55" title="SEN55 Documentation" target="_blank" rel="noreferrer nofollow noopener">SEN55 environmental sensor</a>

The SEN55 is the powerhouse of the AIR-1. It measures particulate matter, volatile organic compounds (VOCs), oxidizing gases such as nitrogen oxides (NOx), humidity, and temperature.

## Particulate matter

<a href="https://www.epa.gov/pm-pollution/particulate-matter-pm-basics" target="_blank" rel="noreferrer nofollow noopener">The EPA</a> defines particulate matter (also called particle pollution) as a mixture of solid particles and liquid droplets found in the air. Some particles, such as dust, dirt, soot, or smoke, are large or dark enough to be seen with the naked eye. Others are so small they can only be detected using an electron microscope. Read about the <a href="https://www.epa.gov/indoor-air-quality-iaq/sources-indoor-particulate-matter-pm" target="_blank" rel="noreferrer nofollow noopener">sources of indoor PM particles</a>.

The EPA describes two common sizes:

* **PM<sub>10</sub>**: inhalable particles, with diameters that are generally 10 micrometers and smaller.
* **PM<sub>2\.5</sub>**: fine inhalable particles, with diameters that are generally 2.5 micrometers and smaller.

How small is 2.5 micrometers? Think about a single hair from your head. The average human hair is about 70 micrometers in diameter, making it 30 times larger than the largest fine particle.

!!! tip "Automate when PM levels rise"

    Trigger an alert automation, your HVAC, or a fan when PM particles are rising. <a href="https://www.epa.gov/indoor-air-quality-iaq/sources-indoor-particulate-matter-pm" target="_blank" rel="noreferrer nofollow noopener">This article</a> goes over lots of ways to reduce PM particles in your home.

### What PM1, PM2.5, PM4, and PM10 mean

PM is often classified by size, because smaller particles pose greater risks to health: they can penetrate deeper into the lungs. Here's what each size means:

<table><thead><tr><th><p><strong>PM Type</strong></p></th><th><p><strong>Size (µm)</strong></p></th><th><p><strong>Description</strong></p></th></tr></thead><tbody><tr><td><p>PM1</p></td><td><p>≤ 1.0</p></td><td><p>Ultrafine particles that can reach deep into the lungs and bloodstream.</p></td></tr><tr><td><p>PM2.5</p></td><td><p>≤ 2.5</p></td><td><p>Fine particles; linked to respiratory and cardiovascular issues.</p></td></tr><tr><td><p>PM4</p></td><td><p>≤ 4.0</p></td><td><p>Less commonly regulated; typically used in industrial settings.</p></td></tr><tr><td><p>PM10</p></td><td><p>≤ 10</p></td><td><p>Inhalable particles; may irritate eyes, nose, and throat.</p></td></tr></tbody></table>

!!! note "PM2.5 and PM10 are the most common"

    PM2.5 and PM10 are the most widely monitored and regulated for public health purposes, but all four readings (PM1, PM2.5, PM4, and PM10) are useful.

## Safe PM levels

Health agencies publish limits for how much particulate matter is safe to breathe. Use these tables to pick the thresholds for your alerts and automations.

### Recommended safe exposure limits (WHO)

The **World Health Organization (WHO)** <a href="https://www.who.int/publications/i/item/9789240034228" target="_blank" rel="noreferrer nofollow noopener">provides the following exposure limits</a> for particulate matter:

<table><thead><tr><th><p><strong>PM Type</strong></p></th><th><p><strong>24-Hour Limit (µg/m³)</strong></p></th><th><p><strong>Annual Average (µg/m³)</strong></p></th></tr></thead><tbody><tr><td><p>PM2.5</p></td><td><p>≤ 15</p></td><td><p>≤ 5</p></td></tr><tr><td><p>PM10</p></td><td><p>≤ 45</p></td><td><p>≤ 15</p></td></tr></tbody></table>

### U.S. EPA Air Quality Index (AQI) for PM2.5

The **U.S. Environmental Protection Agency (EPA)** <a href="https://www.airnow.gov" target="_blank" rel="noreferrer nofollow noopener">defines safety thresholds</a> for PM2.5 based on a 24-hour average:

<table><thead><tr><th><p><strong>PM2.5 (µg/m³)</strong></p></th><th><p><strong>AQI Category</strong></p></th><th><p><strong>Health Implications</strong></p></th></tr></thead><tbody><tr><td><p>0.0 to 12.0</p></td><td><p>Good</p></td><td><p>Air quality is satisfactory.</p></td></tr><tr><td><p>12.1 to 35.4</p></td><td><p>Moderate</p></td><td><p>Acceptable; some risk for sensitive individuals.</p></td></tr><tr><td><p>35.5 to 55.4</p></td><td><p>Unhealthy for Sensitive Groups</p></td><td><p>Increased risk for those with heart/lung issues, children, and older adults.</p></td></tr><tr><td><p>55.5 to 150.4</p></td><td><p>Unhealthy</p></td><td><p>Everyone may begin to experience health effects.</p></td></tr><tr><td><p>150.5 to 250.4</p></td><td><p>Very Unhealthy</p></td><td><p>Health alert: serious effects possible.</p></td></tr><tr><td><p>&gt;250.5</p></td><td><p>Hazardous</p></td><td><p>Emergency conditions for all populations.</p></td></tr></tbody></table>

### PM safe ranges at a glance

This table sums up the WHO and EPA limits above for each PM size:

<table><thead><tr><th><p><strong>PM Size</strong></p></th><th><p><strong>Safe Range</strong></p></th><th><p><strong>Health Concern</strong></p></th></tr></thead><tbody><tr><td><p>PM1</p></td><td><p>No official limit (keep as low as possible)</p></td><td><p>Ultrafine particles (most dangerous)</p></td></tr><tr><td><p>PM2.5</p></td><td><p>≤ 12 µg/m³ (EPA), ≤ 5 µg/m³ (WHO annual)</p></td><td><p>Penetrates lungs and bloodstream</p></td></tr><tr><td><p>PM4</p></td><td><p>Industrial contexts only (no public health limits)</p></td><td><p>Less regulated</p></td></tr><tr><td><p>PM10</p></td><td><p>≤ 45 µg/m³ (WHO 24-hour)</p></td><td><p>Triggers upper respiratory irritation</p></td></tr></tbody></table>

### Indoor air quality notes

* **PM1** and **PM2.5** are especially important for indoor air monitoring, since these smaller particles are more likely to come from cooking, candles, smoking, or inadequate ventilation.
* Use an **air purifier with a HEPA filter** to reduce PM1 and PM2.5 concentrations indoors.
* Keep **PM2.5 below 12 µg/m³** indoors for general safety, and below **5 µg/m³** for ideal long-term health protection.

## NowCast AQI

<a href="https://esphome.io/components/sensor/aqi/" target="_blank" rel="noreferrer nofollow noopener">NowCast AQI</a> takes your PM2.5 and PM10 readings and converts them into a single number from 0 to 500 using the EPA's formula. That number maps directly to the categories in the EPA AQI table above: bigger means worse.

The AIR-1 calculates this automatically and exposes it as a sensor in Home Assistant.

!!! tip "NowCast AQI is easier to automate and understand than raw PM"

    Instead of comparing µg/m³ values across PM1, PM2.5, PM4, and PM10, you get one number. Set an automation to trigger at 100 (Moderate) or 150 (Unhealthy for Sensitive Groups) and anyone in your household can understand why it fired.

## <a href="https://sensirion.com/media/documents/02232963/6294E043/Info_Note_VOC_Index.pdf" target="_blank" rel="noreferrer nofollow noopener">VOC Index</a>

Per Sensirion:

> The VOC Index describes the current VOC status in a room relative to the sensor’s recent history. In this way, the VOC Index behaves like a human nose.

!!! tip "Automate when the VOC Index rises above 100"

    Trigger an alert automation, your HVAC, or a fan when the VOC Index rises above 100. Per Sensirion:

    > a VOC Index above 100 means that there are more VOCs compared to the average (e.g., induced by a VOC event from cooking, cleaning, breathing, etc.) while a VOC Index below 100 means that there are fewer VOCs compared to the average

## VOC Quality

VOC Quality uses the <a href="https://sensirion.com/media/documents/ACD82D45/6294DFC0/Info_Note_Integration_VOC_NOx_Sensor.pdf" target="_blank" rel="noreferrer nofollow noopener">VOC Index and a scale to output an easier-to-use rating</a>. Each VOC Index range maps to one rating:

| VOC Index | VOC Quality |
| --- | --- |
| 0-79 | **Improved** |
| 80-149 | **Normal** |
| 150-249 | **Abnormal** |
| 250-399 | **Very abnormal** |
| 400+ | **Extremely abnormal** |

!!! tip "Automate when VOC Quality turns Abnormal or worse"

    Trigger an alert automation, your HVAC, or a fan when VOC Quality changes to Abnormal, Very abnormal, or Extremely abnormal. This is a quick way to automate on air quality changes over the past 24 hours, but you'll still want to automate on particulate matter as well.

## <a href="https://sensirion.com/media/documents/9F289B95/6294DFFC/Info_Note_NOx_Index.pdf" target="_blank" rel="noreferrer nofollow noopener">NO<sub>x</sub> Index</a>

Per Sensirion:

> The NOx Index describes the current NOx condition in a room relative to the sensor’s recent history. In this way, the NOx Index behaves like a human nose.

!!! tip "Automate when the NO<sub>x</sub> Index rises above 1"

    Trigger an alert automation, your HVAC, or a fan when the NO<sub>x</sub> Index rises above 1. Per Sensirion:

    > On the NOx Index scale, this offset is always mapped to the value of 1, making the readout as easy as possible: an NOx Index above 1 means that there are more NOx compounds compared to the average (e.g., induced by cooking on a gas stove), while an NOx Index close to 1 means that there are (nearly) no NOx gases present, which is the case most of the time (or induced by fresh air from an open window, using an air purifier, etc.).

## <a href="https://sensirion.com/products/catalog/SCD40" target="_blank" rel="noreferrer nofollow noopener">SCD40 CO<sub>2</sub> sensor</a>

The optional CO<sub>2</sub> sensor addon lets your AIR-1 track CO<sub>2</sub>. CO<sub>2</sub> levels in a closed, poorly ventilated bedroom can quickly rise to concentrations that may impair focus or even pose health risks. In the chart below, notice the CO<sub>2</sub> levels dropping when the HVAC was turned on overnight.

![CO2 chart showing levels dropping overnight after the HVAC turns on](/assets/co2-levels-drop-after-hvac-on.png)

### Automatic calibration

The latest AIR-1 firmware keeps the SCD40 calibrated automatically. The sensor assumes it sees fresh air (about 420 ppm) at least once a week and corrects its baseline to match, so you no longer need to re-calibrate it manually every 1 to 2 years.

!!! warning "Auto calibration needs regular fresh air"

    If your AIR-1 sits in a space that rarely gets fresh air (a sealed office, a basement, a grow room), automatic self-calibration will slowly drag the CO<sub>2</sub> readings down. Turn off the **CO2 Auto Calibration** switch on the device page and follow the [manual calibration guide](../../general/calibrating-and-updating/co2-calibration.md) every 1 to 2 years instead.

### CO<sub>2</sub> levels and health effects

The <a href="https://www.dhs.wisconsin.gov/chemical/carbondioxide.htm" target="_blank" rel="noreferrer nofollow noopener">Wisconsin Department of Health CO<sub>2</sub> Level Chart</a> lists CO<sub>2</sub> levels and their health effects:

![Wisconsin health department list of CO2 levels and health effects from 400 to 40,000 ppm](/assets/air-1-co2-calibration-image-6.jpg)

!!! tip "Automate when CO<sub>2</sub> is over 1000 ppm"

    Trigger an alert automation, your HVAC, or a fan when CO<sub>2</sub> goes over 1000 ppm. Opening a window, turning on a fan, or running the HVAC in your house are all great ways to bring CO<sub>2</sub> down.

## <a href="https://wiki.dfrobot.com/_SKU_SEN0377_Gravity__MEMS_Gas_Sensor_CO__Alcohol__NO2___NH3___I2C___MiCS_4514" target="_blank" rel="noreferrer nofollow noopener">MiCS-4514 gas sensor</a>

The MiCS-4514 is a unique sensor that can distinguish between multiple gases, such as carbon monoxide, nitrogen dioxide (NO2), ethanol, hydrogen, ammonia, and methane.
