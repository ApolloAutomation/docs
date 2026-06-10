# CO<sub>2</sub> Calibration

!!! info "Your sensor calibrates itself"

    The latest Apollo firmware enables the SCD40's automatic self-calibration by default on every device with the CO<sub>2</sub> sensor (AIR-1, R-PRO-1, MSR-2, and MTR-1). As long as the sensor sees fresh air (about 420 ppm) at least once a week, it corrects its own baseline and you never need to calibrate manually. Airing out the room once a week is enough.

    If your device sits in a space that rarely gets fresh air (a sealed office, a basement, a grow room), automatic self-calibration will slowly drag the readings down. Turn off the **CO2 Auto Calibration** switch in your device's settings and calibrate manually with the steps below instead.

!!! tip "Calibrate manually every 1 to 2 years when auto calibration is off"

    The <a href="https://sensirion.com/products/catalog/SCD40" title="Documentation on SCD40 CO<sub>2</sub> Sensor!" target="_blank" rel="noreferrer nofollow noopener">SCD40 CO<sub>2</sub> sensor</a> has a long lifetime (<a href="https://sensirion.com/media/documents/48C4B7FB/66E05452/CD_DS_SCD4x_Datasheet_D1.pdf" title="scd10 datasheet showing lifetime over 10 years" target="_blank" rel="noreferrer nofollow noopener">over 10 years</a>), but with automatic self-calibration turned off it needs re-calibration back to the 420 ppm baseline every 1 to 2 years.

![AIR-1 Shown Outdoors for CO2 Calibration Portrait Image](/assets/air-1-co2-calibration-portrait-image-1.jpg "AIR-1 Shown Outdoors for CO2 Calibration")

1\. Bring your sensor outside and plug it in. You might need a USB battery bank if you live in an apartment or otherwise cannot get power outside of your building.

2\. Open your Homey app or desktop browser and navigate to the Homey Dashboard.

3\. Navigate to your device, such as via the "Favorite Devices" section and right click (or on mobile short hold) then click on Settings.

![](/assets/co2-calibration-homey-pic-1.png)

4\. Scroll down until you see "Maintenance" and select it on mobile, then click on "Calibrate SCD40 to 420ppm" and you should see the CO<sub>2</sub> readings at 420 ppm or near it.

![](/assets/co2-calibration-homey-pic-2.png)

It might take several attempts clicking the "Press" button for it to equalize correctly. If you don't see the SCD40 reporting 400-500 ppm then click the button again.

5\. Now your CO<sub>2</sub> sensor should be calibrated! Be sure to setup some nice flows and check out the insights so you can monitor the CO<sub>2</sub> levels.

![Image of CO2ppm on a graph](/assets/co2-calibration-homey-pic-3.png)

!!! danger "Dangerous CO<sub>2</sub> level considerations"

    CO<sub>2</sub> levels in a closed, unventilated bedroom can quickly rise to concentrations that may impair focus or even pose health risks.

Note the steep decline in CO<sub>2</sub> ppm detected due to the door and window being opened and fan turned on.

![CO2_8.jpg](/assets/air-1-co2-calibration-image-5.jpg)

<a href="https://www.dhs.wisconsin.gov/chemical/carbondioxide.htm" target="_blank" rel="noreferrer nofollow noopener">Wisconsin Department of Health CO<sub>2</sub> Level Chart</a>

![CO2 Health Department.png](/assets/air-1-co2-calibration-image-6.jpg)

!!! example "CO<sub>2</sub> levels dropping due to HVAC Fan on a schedule"

    This could be improved by increasing air exchange to get below 1000 ppm for a safer environment.

![Plotly CO2 Graph.png](/assets/plotly-co2-graph.png)