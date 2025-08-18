---
title: R-PRO-1 Home Assistant Zone Configuration
description: Tutorial for R-PRO-1 Home Assistant Zone Configuration.
---
# How To Tune The R-PRO-1 Using Home Assistant

!!! info "Your R-PRO-1 has two unique mmWave sensors that both need to be tuned!"

    The R-PRO-1 comes with an LD2450 mmwave sensor and an optional secondary LD2412 mmWave sensor.

    The LD2450 allows for up to three targets tracked in up to three zones but can have issues with "still detection".

    The optional LD2412 mmWave sensor allows you to have perfect still detection for one target at up to 9 meters so it's a great addition to the sensor.

Manually enter in the X and Y coordinates for each zone in Home Assistant or directly from the device's webserver by visiting the IP address or hostname.local. It's much easier to <a href="https://wiki.apolloautomation.com/products/rpro1/calibrating-and-updating/zones-hlk/" rel="noreferrer nofollow">tune using the HLK Radartool App</a> and we suggest using that to set up your R-PRO-1 LD2450.

###### LD2450 Configuration

1\. Install [HACS](https://hacs.xyz/docs/use/).

2\. Download [Plotly](https://github.com/dbuezas/lovelace-plotly-graph-card "Click here to install Plotly!") inside HACS.

3\. Enter your device’s full name and optionally customize the names of the three zones using the tool below. Then click **Generate YAML** and **Copy YAML.**<br>If you're unsure of your device name, go to the <a href="http://homeassistant.local:8123/config/integrations/integration/esphome" target="_blank" rel="noreferrer nofollow noopener">ESPHome Integrations page</a>, select your device, and look for the full name. Unless you’ve renamed it, it will likely be something like "apollo\_r\_pro\_1\_eth\_593904", with six random characters at the end.

<iframe src="/snippets/rpro1-plotly-yaml-generator.html" width="100%" height="700" style="border: none;"></iframe>

&nbsp;

4\. Head to a dashboard view and click the pencil icon to edit dashboard then click one of the large "+" signs, type in manual, and click on it.

![](../../../assets/ld2450-add-plotly-graph-gif.gif)

5\. Delete any text in the custom card then paste the YAML you copied above and click save when finished. You should now have a custom card that looks just like the card below!

![](../../../assets/r-pro-1-plotly-graph-image.png)

6\. Head to the [ESPHome Integrations page](http://homeassistant.local:8123/config/integrations/integration/esphome "Click me to go to the ESPHome integrations page")

7\. Click device as shown in the image below

![](../../../assets/select-r-pro-1-device.png)

8\. Scroll down until you get to the Configuration section and you see the empty boxes for zones 1-3 for both X and Y coordinates.

!!! tip "Suggested settings"

    * Multi Target Tracking toggled on helps it detect up to three targets better.
    * Zone Type allows you to select Disabled, Detection, or Filter.
    * Disabled: Disable zone area detection.
    * Detection: Only detects targets in the specified zone.
    * Filter: Excludes a zone from detection.

9\. Now we can input our Zone 1-3 X and Y values to make our zones. Using the visual card from above, we can walk, sit, or stand in the area where we want to create a detection or non-detection zone. Input values for X are -7000 mm to 7000 mm, and the Y values are 0 mm to 7000 mm.

![](../../../assets/ld2450-zone-input.png)

!!! tip "Helpful Hints to understand zones better!"

    * X1 must always be less than X2, and Y1 must always be less than Y2.

    * The Y axis is easier since it's never negative.

      &nbsp;

    * The X axis is where you can get tripped up, especially when both values are negative: -3456 is less than -2345.
    * The Plotly chart will still render the rectangles even if the X1/X2 and Y1/Y2 values are reversed.
    * The zones cannot overlap.

10\. If you use the imperial system (Freedom Units) then you will need to do this step. Metric users can skip this. For the targets to show up correctly we first need to update the Target 1-3 X and Y measurements from inches (in) to millimeters (mm). Find Target 1-3 X and Y under the Sensors section and select them. You will want to update all 3 X and Y target values.

![](../../../assets/r-pro-1-card-change-units-from-inches.png)

11\. Select the Settings cog in the top right.

![](../../../assets/r-pro-1-card-change-units-settings.png)

12\. Change the unit of measurement to mm and select Update.

![](../../../assets/r-pro-1-card-change-units-select-mm.png)

13\. Your X and Y Targets will now look like this.

![](../../../assets/r-pro-1-card-change-units-all-changed-to-mm.png)

14\. Now you should see targets on the card.

![](../../../assets/r-pro-1-card-working-targets.png)

15\. Now we can make zones around the targets where you want to Detect presence or filter them out.

!!! tip tip "Tip for zone configuration resetting"

    If your zone configurations are not saved when restarting the device then try turning on the LD2450 Bluetooth for a few seconds and then turning it off again. You can also try to toggle on Multi Target Radar. This should wake up the mmWave module and retrieve your saved zones

###### LD2412 Configuration

1\. Navigate to the ESPHome integration by going to settings -&gt; <a href="http://homeassistant.local:8123/config/integrations/integration/esphome" target="_blank" rel="noopener">esphome integration</a> -&gt; click on "1 device" below the Apollo R-PRO-1.

![](../../../assets/select-r-pro-1-device.png)

2\. Scroll down until you see "LD2412 Mode" and change it from "Normal" to "Engineering".

!!! tip "The LD2412 can be tuned using the steps below to work perfectly in your environment!"

    The LD2412 has "gates" at 0.75meter increments starting at g0 and ending at g13. These gates allow you to raise the threshold needed to trigger occupancy in each 0.75meter increment.

    This is very useful in scenarios where you want to tune out a fan, a cat sitting on the stairs, etc.

3\. Scroll down to the Diagnostic section and you will see "LD2412 g00 move energy" through "LD2412 g13 still energy" are showing percentages from 0-100%.

![](../../../assets/r-pro-1-ld2412-move-still-energy.png)

4\. Scroll up to the Configuration section and identify the threshold sliders for g0-g13 for both moving and still energy.

Moving the gate still and move threshold slider to the right increases the amount of energy needed to trigger the sensor. Do this if you want the gate to be less sensitive.

![](../../../assets/ld2412-less-sensitive.png)

Moving the gate still and move threshold slider to the left decreases the amount of energy needed to trigger the sensor. Do this if you want the gate to be more sensitive.

![](../../../assets/ld2412-more-sensitive.png)