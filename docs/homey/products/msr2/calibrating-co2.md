---
title: CO2 Calibration Tutorial (quick)
description: Step by step guide for re-calibrating your SCD40 CO2 sensor
---
# CO<sub>2</sub> Calibration - The Quick method - Desktop Only not mobile

!!! info "Your MSR-2 calibrates itself"

    The latest MSR-2 firmware enables the SCD40's automatic self-calibration by default. As long as the sensor sees fresh air (about 420 ppm) at least once a week, it corrects its own baseline and you never need to calibrate manually. You only need this guide if the device sits in a space that rarely gets fresh air (a sealed office, a basement, a grow room), where auto calibration slowly drags the readings down. In that case, turn off the **CO2 Auto Calibration** switch in your device's settings and calibrate manually with the steps below.

!!! tip "Calibrate manually every 1 to 2 years when auto calibration is off"

    The <a href="https://sensirion.com/products/catalog/SCD40" title="Documentation on SCD40 CO<sub>2</sub> Sensor!" target="_blank" rel="noreferrer nofollow noopener">SCD40 CO<sub>2</sub> sensor</a> has a long lifetime (<a href="https://sensirion.com/media/documents/48C4B7FB/66E05452/CD_DS_SCD4x_Datasheet_D1.pdf" title="scd10 datasheet showing lifetime over 10 years" target="_blank" rel="noreferrer nofollow noopener">over 10 years</a>), but with automatic self-calibration turned off it needs re-calibration back to the 420 ppm baseline every 1 to 2 years.

This article will guide you through a simple calibration of your CO<sub>2</sub> sensor for any Apollo Automation device!

1\. Plug in your sensor outdoors and leave it for at least 5 minutes to allow the readings to stabilize. This should be around <a href="https://climate.nasa.gov/vital-signs/carbon-dioxide/?intent=121" title="NASA CO<sub>2</sub> levels" target="_blank" rel="noreferrer nofollow noopener">420 ppm per NASA</a>.

![](/assets/air-1-co2-calibration-portrait-quick-pic-3.jpg)

2\. Go to your Home Assistant dashboard and hit the letter "e" - It will pop up with an entity filter then type in "Calibrate CO<sub>2</sub>" and select the correct device.

!!! tip "Hint"

    If you cannot get this menu to pop-up, click somewhere on the <a href="https://www.home-assistant.io/" target="_blank" rel="noreferrer nofollow noopener">Home Assistant</a> dashboard then press your "e" key.

![Image of popup with CO2 calibration choice circled in red](/assets/co2-calibration-quick-pic-1.png)

3\. Click on the button that says "PRESS" and then you are done.

![Image of popup with CO2 calibration press button circled in red](/assets/co2-calibration-quick-pic-2.png)
