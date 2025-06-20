---
title: R-Pro-1 HLKRadarTool app Zone Configuration
description: Tutorial for R-Pro-1 HLKRadarTool app Zone Configuration.
---
# How To Tune mmWave Using HLKRadarTool

<div class="cms-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/-w_GFURyx-A?si=SSRovumabCvHeXwo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen=""></iframe></div>

###### LD2450 Configuration

!!! note "Ensure that the LD2450 firmware version is V2.02.23090617 or later for proper integration functionality. "

    The newer version of the firmware includes an "auto calibrate" function so you might want to test it out!

The <a href="https://www.hlktech.net/index.php?id=1157" target="_blank" rel="noreferrer nofollow noopener">HLK-LD2450</a> mmWave sensor is used in the R-PRO-1. <a href="https://drive.google.com/drive/folders/1aItrdziwnEqI-ovDWf24Lj6ioALaljFA?usp=sharing" target="_blank" rel="noreferrer nofollow noopener">Click Here</a> for the datasheet.

=== "iPhone"

    <a href="https://apps.apple.com/us/app/hlkradartool/id1638651152" target="_blank" rel="noreferrer nofollow noopener">Click here to download</a>

=== "Android"

    <a href="https://play.google.com/store/apps/details?id=com.hlk.hlkradartool&amp;hl=en_US" target="_blank" rel="noreferrer nofollow noopener">Click here to download</a>

1\. Head to the <a href="http://homeassistant.local:8123/config/integrations/integration/esphome" title="Click me to go to the ESPHome integrations page" target="_blank" rel="noreferrer nofollow noopener">ESPHome Integrations page</a> then select your R-PRO-1 and scroll down until you see LD2450 Bluetooth.

![](../../../assets/mtr-1-toggle-on-ld2450-bluetooth.png)

2\. Open the HLKRadarTool App and select your device.

!!! success "You need to be close to your device!"

    The LD2450 mmWave sensor is a very tiny sensor with no external antenna, which means it cannot connect to bluetooth devices unless they are very close. Sometimes this means you need to be within a few feet of the sensor to connect directly to it!

![](../../../assets/r-pro-1-select-ld2450-module.png)

3\. Select Set in the top right.

![](../../../assets/r-pro-1-hlk-app-select-set.png)

4\. Enable Area Detection, then toggle Area 1, 2, and 3 to display a colored box with the matching number. You can press and hold the box to move or resize it as needed. Once your zones are configured, click **Submit** — you should see a confirmation message: **"Setup successfully."**

!!! tip "There are three ways to use your R-PRO-1!"

    You can use any of these three choices to control your R-PRO-1 differently. The most common option is "Detection" which lets you setup three areas and track three targets within them.<br>**Disabled**: Disable multi-zone area detection and just tracks one big area.<br>**Detection**: Only detects targets within each of the three zones.<br>**Filter**: Excludes a zone from detection and detects presence everywhere else.

    Disabled allows you to just use the sensor as a "basic" presence sensor and "Filter" lets you filter out an area and detect everything else, which is useful to avoid a fan!

![](../../../assets/r-pro-1-hlk-app-setup-zones.png)

!!! tip "Helpful Hints to understand zones better!"

    * X1 must always be less than X2, and Y1 must always be less than Y2.

    * The Y axis is easier since it's never negative.

      &nbsp;

    * The X axis is where you can get tripped up, especially when both values are negative: -3456 is less than -2345.
    * The Plotly chart will still render the rectangles even if the X1/X2 and Y1/Y2 values are reversed.
    * The zones cannot overlap.

###### Dashboard Card Setup

1\. Install [HACS](https://hacs.xyz/docs/use/).

2\. Install [Plotly](https://github.com/dbuezas/lovelace-plotly-graph-card "Click here to install Plotly!") inside HACS.

3\. Copy the code below and add a Home Assistant card to visualize your zones. You will need to replace "apollo\_r\_pro\_1\_eth\_593904" to match your R-PRO-1 device. This can be done quickly by using a code editor or ChatGPT.

3\. Enter your device's full name and optionally name each of the three zones using the tool below then click Generate YAML and then Copy YAML.

<iframe src="/snippets/rpro1-plotly-yaml-generator.html" width="100%" height="700" style="border: none;"></iframe>

4\. Head to a dashboard view and click the pencil icon to edit dashboard then click one of the large "+" signs, type in manual, and click on it.

![](../../../assets/ld2450-add-plotly-graph-gif.gif)

5\. Delete any text in the custom card then paste the YAML you copied above and click save when finished. You should now have a custom card that looks just like the card below!

![](../../../assets/r-pro-1-plotly-graph-image.png)

###### LD2412 Configuration

&nbsp;

&nbsp;

&nbsp;

&nbsp;