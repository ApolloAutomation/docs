---
title: CO2 calibration tutorial (quick)
description: Step by step guide for re-calibrating your SCD40 CO2 sensor
---
# CO<sub>2</sub> calibration - the quick method - desktop only not mobile

!!! info "Your R PRO-1 calibrates itself"

    The R PRO-1 enables the SCD40's automatic self-calibration by default. As long as the sensor sees fresh air (about 420 ppm) at least once a week, it corrects its own baseline and you never need to calibrate manually. You only need this guide if the device sits in a space that rarely gets fresh air (a sealed office, a basement, a grow room), where auto calibration slowly drags the readings down. In that case, turn off the **CO2 Auto Calibration** switch on the device page and calibrate manually with the steps below.

!!! tip "Calibrate manually every 1 to 2 years when auto calibration is off"

    The <a href="https://sensirion.com/products/catalog/SCD40" title="Documentation on SCD40 CO<sub>2</sub> Sensor!" target="_blank" rel="noreferrer nofollow noopener">SCD40 CO<sub>2</sub> sensor</a> has a long lifetime (<a href="https://sensirion.com/media/documents/48C4B7FB/67FE0194/CD_DS_SCD4x_Datasheet_D1.pdf" title="SCD4x datasheet showing lifetime over 10 years" target="_blank" rel="noreferrer nofollow noopener">over 10 years</a>), but with automatic self-calibration turned off it needs re-calibration back to the 420 ppm baseline every 1 to 2 years.

This article will guide you through a simple calibration of your CO<sub>2</sub> sensor for any Apollo Automation device!

1\. Plug in your sensor outdoors and leave it for at least 5 minutes to allow the readings to stabilize. This should be around <a href="https://climate.nasa.gov/vital-signs/carbon-dioxide/?intent=121" title="NASA CO<sub>2</sub> levels" target="_blank" rel="noreferrer nofollow noopener">420 ppm per NASA</a>.

![Apollo AIR-1 plugged in by USB-C cable outdoors to read fresh air for CO2 calibration](/assets/air-1-co2-calibration-portrait-quick-pic-3.jpg)

*Shown with an AIR-1; set your R PRO-1 outdoors the same way.*

2\. Go to your Home Assistant dashboard and press the letter "e". In the entity search that pops up, type "Calibrate SCD40" and select **Calibrate SCD40 To 420ppm** under your R PRO-1. If you have several Apollo devices, add your R PRO-1's name to the search to narrow the list.

!!! tip "Hint"

    If you cannot get this menu to pop up, click somewhere on the <a href="https://www.home-assistant.io/" target="_blank" rel="noreferrer nofollow noopener">Home Assistant</a> dashboard then press your "e" key.

![Home Assistant entity search for R PRO-1 Calibrate SCD40 with the R PRO-1's Calibrate SCD40 To 420ppm button highlighted](/assets/r-pro-1-co2-calibration-search.png)

3\. Click **Press**, and you're done.

![R PRO-1 Calibrate SCD40 To 420ppm dialog with the Press button highlighted](/assets/r-pro-1-co2-calibration-press.png)