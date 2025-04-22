---
title: AIR-1 General Tips
description: Guide to help you understand which sensors you should be concerned with and expected safe or not safe thresholds to alert or automate on.
---
# AIR-1 General Tips

The AIR-1 has multiple different types of sensors and this guide will help you understand which ones you should be concerned with and expected safe or not safe thresholds to alert or automate on.

##### <a href="https://sensirion.com/products/catalog/SEN55" title="SEN55 Documentation" target="_blank" rel="noreferrer nofollow noopener">SEN55 Environmental Sensor</a>

The SEN55 is the powerhouse of the AIR-1 with multiple sensors such as particulate matter, volatile organic compounds (VOCs), oxidizing gases, such as nitrogen oxides (NOx), as well as humidity & temperature.

###### Particulate Matter

<a href="https://www.epa.gov/pm-pollution/particulate-matter-pm-basics" target="_blank" rel="noreferrer nofollow noopener">Per the EPA</a>: particulate matter (also called particle pollution): the term for a mixture of solid particles and liquid droplets found in the air. Some particles, such as dust, dirt, soot, or smoke, are large or dark enough to be seen with the naked eye. Others are so small they can only be detected using an electron microscope. <a href="https://www.epa.gov/indoor-air-quality-iaq/sources-indoor-particulate-matter-pm" target="_blank" rel="noreferrer nofollow noopener">Sources of pm particles here</a>.

**PM<sub>10</sub>** : inhalable particles, with diameters that are generally 10 micrometers and smaller; and

**PM<sub>2\.5</sub>** : fine inhalable particles, with diameters that are generally 2.5 micrometers and smaller.

* How small is 2.5 micrometers? Think about a single hair from your head. The average human hair is about 70 micrometers in diameter – making it 30 times larger than the largest fine particle.

!!! tip "We suggest triggering alert automations, hvac or a fan turning on, etc when PM particles are rising"

    <a href="https://www.epa.gov/indoor-air-quality-iaq/sources-indoor-particulate-matter-pm" target="_blank" rel="noreferrer nofollow noopener">This article</a> goes over lots of ways to reduce pm particles in your home!

---

###### <a href="https://sensirion.com/media/documents/02232963/6294E043/Info_Note_VOC_Index.pdf" target="_blank" rel="noreferrer nofollow noopener">VOC Index</a>

Per Sensirion,

> The VOC Index
>
> describes the current VOC status in a room relative to the sensor’s
>
> recent history. In this way, the VOC Index behaves like a human nose

!!! tip "We suggest triggering alert automations, hvac or a fan turning on, etc when the VOC Index rises above 100"

    Per Sensirion:

    > a VOC Index above 100 means that there are more
    >
    > VOCs compared to the average (e.g., induced by a VOC event from
    >
    > cooking, cleaning, breathing, etc.) while a VOC Index below 100 means
    >
    > that there are fewer VOCs compared to the average

###### VOC Quality

This uses the <a href="https://sensirion.com/media/documents/ACD82D45/6294DFC0/Info_Note_Integration_VOC_NOx_Sensor.pdf" target="_blank" rel="noreferrer nofollow noopener">VOC index and a scale to output an easier to use variable</a>.

0-79: **Improved** -&gt; 80-149: **Normal** -&gt; 150-249: **Abnormal** -&gt; 250-399: **Very abnormal** -&gt; 400+: **Extremely abnormal**

!!! tip "We suggest triggering alert automations, hvac or a fan turning on, etc when the VOC Quality changes to Abnormal or Very Abnormal or Extremely Abnormal."

    This is a very easy way to automate based on the air quality changing over the past 24 hours but you will still want to automate on particulate matter as well!

###### <a href="https://sensirion.com/media/documents/9F289B95/6294DFFC/Info_Note_NOx_Index.pdf" target="_blank" rel="noreferrer nofollow noopener">NO<sub>X</sub> Index</a>

Per Sensirion,

> The NO x Index describes the current NO x condition in a
>
> room relative to the sensor’s recent history. In this way, the NO x Index
>
> behaves like a human nose.

!!! tip "We suggest triggering alert automations, hvac or a fan turning on, etc when NO<sub>x</sub> rises above 1"

    Per Sensirion:

    > On the NO x Index scale, this offset is always mapped to
    >
    > the value of 1, making the readout as easy as possible: an NO x Index
    >
    > above 1 means that there are more NO x compounds compared to the
    >
    > average (e.g., induced by cooking on a gas stove), while an NO x Index
    >
    > close to 1 means that there are (nearly) no NO x gases present, which is
    >
    > the case most of the time (or induced by fresh air from an open window,
    >
    > using an air purifier, etc.).

---

##### <a href="https://sensirion.com/products/catalog/SCD40" target="_blank" rel="noreferrer nofollow noopener">SCD40 CO<sub>2</sub> sensor</a>

The optional CO<sub>2</sub> sensor addon is a great way to add the ability to track CO<sub>2</sub>. CO<sub>2</sub> levels in a closed, poorly ventilated bedroom can quickly rise to concentrations that may impair focus or even pose health risks. Notice the CO2 levels dropping in the image below when the HVAC was turned on overnight!

![](assets/co2-levels-drop-after-hvac-on.png)

<a href="https://www.dhs.wisconsin.gov/chemical/carbondioxide.htm" target="_blank" rel="noreferrer nofollow noopener">Wisconsin Department of Health CO<sub>2</sub> Level Chart</a>

![CO2 Health Department.png](../../../homey/products/general/calibrating-and-updating/assets/air-1-co2-calibration-image-6.jpg)

!!! tip "We suggest triggering alert automations, hvac or a fan turning on, etc when CO<sub>2</sub> is over 1000"

    Opening a window, turning on a fan, the HVAC in the house, etc are all great ways to get CO<sub>2</sub> to go down!

---

##### <a href="https://wiki.dfrobot.com/_SKU_SEN0377_Gravity__MEMS_Gas_Sensor_CO__Alcohol__NO2___NH3___I2C___MiCS_4514" target="_blank" rel="noreferrer nofollow noopener">MiCS-4514 Gas Sensor</a>

The MiCS-4514 is a very unique sensor able to distinguish between multiple gases such as Carbon Monoxide, Nitrogen, Ethanol, Hydrogen, Ammonia, and Methane.