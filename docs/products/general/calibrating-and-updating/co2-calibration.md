# CO2 Calibration

!!! tip "This should be done every 1-2 years."

    The [SCD40 CO2 sensor](https://sensirion.com/products/catalog/SCD40 "Docmentation on SCD40 CO2 Sensor!") has a long lifetime but it requires re-calibration after 1-2 years back to a 420ppm baseline!

![AIR-1 Shown Outdoors for CO2 Calibration Portrait Image](assets/air-1-co2-calibration-portrait-image-1.jpg "AIR-1 Shown Outdoors for CO2 Calibration")

1\. Bring your sensor outside and plug it in. You might need a USB battery bank if you live in an apartment or otherwise cannot get power outside of your building.

2\. Head to the [ESPHome Integrations page](http://homeassistant.local:8123/config/integrations/integration/esphome "Click me to go to the ESPHome integrations page").

3\. Click device as shown in the image below

![](assets/air-1-co2-calibration-image-2-1.jpg)

4\. Click the "Press" button next to Calibrate SCD40 to 420ppmbutton and you should see the CO2 readings at 420ppm or near it.

![](assets/air-1-co2-calibration-image-3.jpg)

It can take a few times clicking the calibrate for it to equalize correctly sometimes. If you don't see the SCD40 reporting 400-500 ppm then click the button again.

5\. Now your CO2 sensor should be calibrated! Be sure to setup some nice cards on your dashboard so you can monitor the CO2 levels.

![Image of CO2ppm on a graph](assets/air-1-co2-calibration-image-4.jpg)

!!! danger "Dangerous CO2 level considerations"

    The CO2 levels in a bedroom with the door closed and no ventilation can easily spike to levels where you lose focus or worse!

Note the steep decline in CO2 ppm due to opening door, window and running fan.

![CO2_8.jpg](assets/air-1-co2-calibration-image-5.jpg)

[Wisconsin Department of Health CO2 Level Chart](https://www.dhs.wisconsin.gov/chemical/carbondioxide.htm)

![CO2 Health Department.png](assets/air-1-co2-calibration-image-6.jpg)

CO2 levels staying below 1500 ppm after changing HVAC fan schedule to circulate air more frequently. This could be improved by  increasing air exchange to get below 1000 ppm for a safer environment.

![Plotly CO2 Graph.png](../assets/plotly-co2-graph.png)