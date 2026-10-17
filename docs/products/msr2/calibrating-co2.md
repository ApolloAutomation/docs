---
title: CO2 calibration tutorial (quick)
description: Step by step guide for re-calibrating your SCD40 CO2 sensor
---
# CO<sub>2</sub> calibration - the quick method - desktop only not mobile

!!! info "Your MSR-2 calibrates itself"

    The latest MSR-2 firmware enables the SCD40's automatic self-calibration by default. As long as the sensor sees fresh air (about 420 ppm) at least once a week, it corrects its own baseline and you never need to calibrate manually. You only need this guide if the device sits in a space that rarely gets fresh air (a sealed office, a basement, a grow room), where auto calibration slowly drags the readings down. In that case, turn off the **CO2 Auto Calibration** switch on the device page and calibrate manually with the steps below.

!!! tip "Calibrate manually every 1 to 2 years when auto calibration is off"

    The <a href="https://sensirion.com/products/catalog/SCD40" title="Documentation on SCD40 CO<sub>2</sub> Sensor!" target="_blank" rel="noreferrer nofollow noopener">SCD40 CO<sub>2</sub> sensor</a> has a long lifetime (<a href="https://sensirion.com/media/documents/48C4B7FB/67FE0194/CD_DS_SCD4x_Datasheet_D1.pdf" title="SCD4x datasheet showing lifetime over 10 years" target="_blank" rel="noreferrer nofollow noopener">over 10 years</a>), but with automatic self-calibration turned off it needs re-calibration back to the 420 ppm baseline every 1 to 2 years.

This article will guide you through a simple calibration of your CO<sub>2</sub> sensor for any Apollo Automation device!

1\. Plug in your sensor outdoors and leave it for at least 5 minutes to allow the readings to stabilize. This should be around <a href="https://climate.nasa.gov/vital-signs/carbon-dioxide/?intent=121" title="NASA CO<sub>2</sub> levels" target="_blank" rel="noreferrer nofollow noopener">420 ppm per NASA</a>.

![Apollo AIR-1 plugged in outdoors on concrete to read fresh air CO2 levels](/assets/air-1-co2-calibration-portrait-quick-pic-3.jpg)

*Shown with an AIR-1; set your MSR-2 outdoors the same way.*

2\. Go to your Home Assistant dashboard and hit the letter "e". It will pop up with an entity filter then type in "Calibrate CO<sub>2</sub>" and select the correct device.

!!! tip "Hint"

    If you cannot get this menu to pop-up, click somewhere on the <a href="https://www.home-assistant.io/" target="_blank" rel="noreferrer nofollow noopener">Home Assistant</a> dashboard then press your "e" key.

![Home Assistant entity search with the Calibrate SCD40 To 420ppm button circled in red](/assets/co2-calibration-quick-pic-1.png)

*Shown for an AIR-1; your MSR-2 lists the same Calibrate SCD40 To 420ppm button.*

3\. Click on the button that says "PRESS" and then you are done.

![Calibrate SCD40 To 420ppm entity dialog with the Press button circled in red](/assets/co2-calibration-quick-pic-2.png)

*Shown for an AIR-1; the MSR-2 button dialog looks the same.*