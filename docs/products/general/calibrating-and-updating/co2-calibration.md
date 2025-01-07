# CO2 Calibration

1\. Take your sensor outside (for a walk :D) and plug it in. Make sure it is connected to Home Assistant and let it sit powered on for 3-5 minutes outside before starting the calibration.

!!! tip "This should be done every 1-2 years."

    The [SCD40 CO2 sensor](https://sensirion.com/products/catalog/SCD40 "Docmentation on SCD40 CO2 Sensor!") has a long lifetime but it requires re-calibration after 1-2 years back to a 420ppm baseline!

![AIR-1 Shown Outdoors for CO2 Calibration Portrait Image](assets/air-1-co2-calibration-portrait-image-1.jpg "AIR-1 Shown Outdoors for CO2 Calibration")

1\. Bring your sensor outside and plug it in. You might need a USB battery bank if you live in an apartment or otherwise cannot get power outside of your building.

2\. Head to the [ESPHome Integrations page](http://homeassistant.local:8123/config/integrations/integration/esphome "Click me to go to the ESPHome integrations page")

3\. Click device as shown in the image below

![](assets/air-1-co2-calibration-image-2-1.jpg)

4\. Click the "Press" button next to Calibrate SCD40 to 420ppmbutton and you should see the CO2 readings at 420ppm or near it.

![](assets/air-1-co2-calibration-image-3.jpg)

It can take a few times clicking the calibrate for it to equalize correctly sometimes. If you don't see the SCD40 reporting 400-500 ppm then click it again.

![Button CO2 Calibration.png](../assets/button-co2-calibration.png)

7\. Now your CO2 sensor should be calibrated! Be sure to setup some nice cards on your dashboard so you can monitor the CO2 levels. My bedroom's CO2 levels got dangerously high and I had to run my HVAC more frequently at night to circulate the air. See examples of cards and data below.

Example Home Assistant Card

![CO2_7.png](../assets/co2-7.png)

Dangerous CO2 levels in bedroom. Steep decline in level due to opening door, window and running fan.

![CO2_8.jpg](../assets/co2-8.jpg)

Wisconsin Department of Health CO2 Level Chart

![CO2 Health Department.png](../assets/co2-health-department.png)

CO2 levels staying below 1500 ppm after changing HVAC fan schedule to circulate air more frequently. Need to increase air exchange to get below 1000 ppm for a safer environment.

![Plotly CO2 Graph.png](../assets/plotly-co2-graph.png)