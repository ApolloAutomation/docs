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

![](/assets/mtr-1-toggle-on-ld2450-bluetooth.png)

2\. Open the HLKRadarTool App and select your device.

!!! success "You need to be close to your device!"

    The LD2450 mmWave sensor is a very tiny sensor with no external antenna, which means it cannot connect to bluetooth devices unless they are very close. Sometimes this means you need to be within a few feet of the sensor to connect directly to it!

![](/assets/r-pro-1-select-ld2450-module.png)

3\. Select Set in the top right.

![](/assets/r-pro-1-hlk-app-select-set.png)

4\. Enable Area Detection, then toggle Area 1, 2, and 3 to display a colored box with the matching number. You can press and hold the box to move or resize it as needed. Once your zones are configured, click **Submit** — you should see a confirmation message: **"Setup successfully."**

!!! tip "There are three ways to use your R-PRO-1!"

    You can use any of these three choices to control your R-PRO-1 differently. The most common option is "Detection" which lets you setup three areas and track three targets within them.<br>**Disabled**: Disable multi-zone area detection and just tracks one big area.<br>**Detection**: Only detects targets within each of the three zones.<br>**Filter**: Excludes a zone from detection and detects presence everywhere else.

    Disabled allows you to just use the sensor as a "basic" presence sensor and "Filter" lets you filter out an area and detect everything else, which is useful to avoid a fan!

![](/assets/r-pro-1-hlk-app-setup-zones.png)

!!! tip "Helpful Hints to understand zones better!"

    * X1 must always be less than X2, and Y1 must always be less than Y2.

    * The Y axis is easier since it's never negative.

      &nbsp;

    * The X axis is where you can get tripped up, especially when both values are negative: -3456 is less than -2345.
    * The Plotly chart will still render the rectangles even if the X1/X2 and Y1/Y2 values are reversed.
    * The zones cannot overlap.

###### Dashboard Card Setup

1\. Install [HACS](https://hacs.xyz/docs/use/).

2\. Download [Plotly](https://github.com/dbuezas/lovelace-plotly-graph-card "Click here to install Plotly!") inside HACS.

3\. Enter your device’s full name and optionally customize the names of the three zones using the tool below. \*\* \*\* Then click **Generate YAML** and **Copy YAML.**<br>If you're unsure of your device name, go to the <a href="http://homeassistant.local:8123/config/integrations/integration/esphome" target="_blank" rel="noreferrer nofollow noopener">ESPHome Integrations page</a>, select your device, and look for the full name. Unless you’ve renamed it, it will likely be something like "apollo\_r\_pro\_1\_eth\_593904", with six random characters at the end.

<iframe src="/snippets/rpro1-plotly-yaml-generator.html" width="100%" height="700" style="border: none;"></iframe>

&nbsp;

4\. Head to a dashboard view and click the pencil icon to edit dashboard then click one of the large "+" signs, type in manual, and click on it.

![](/assets/ld2450-add-plotly-graph-gif.gif)

5\. Delete any text in the custom card then paste the YAML you copied above and click save when finished. You should now have a custom card that looks just like the card below!

![](/assets/r-pro-1-plotly-graph-image.png)

###### LD2412 Configuration

The LD2412 works differently than the LD2450. Instead of drawing rectangular zones on a 2D map, you work with **distance gates**. Each gate covers 0.75m of radial distance from the sensor, so Gate 0 is 0-0.75m away, Gate 1 is 0.75-1.5m, and so on up to Gate 13 at roughly 9m. You define what the sensor reacts to by setting a sensitivity threshold at each gate distance.

The same HLKRadarTool app is used for both sensors.

=== "iPhone"

    <a href="https://apps.apple.com/us/app/hlkradartool/id1638651152" target="_blank" rel="noreferrer nofollow noopener">Click here to download</a>

=== "Android"

    <a href="https://play.google.com/store/apps/details?id=com.hlk.hlkradartool&amp;hl=en_US" target="_blank" rel="noreferrer nofollow noopener">Click here to download</a>

1\. Head to the <a href="http://homeassistant.local:8123/config/integrations/integration/esphome" title="Click me to go to the ESPHome integrations page" target="_blank" rel="noreferrer nofollow noopener">ESPHome Integrations page</a> then select your R-PRO-1 and scroll down until you see **LD2412 Bluetooth**. Toggle it on.

![](/assets/r-pro-1-toggle-on-ld2412-bluetooth.gif)

2\. Open the HLKRadarTool app. Your R-PRO-1 should appear in the device list. Tap it to connect.

!!! success "You need to be close to your device!"

    The LD2412 connects over Bluetooth, which means you need to be within a few feet of the sensor for it to appear in the app. If it doesn't show up, move closer and pull down to refresh the list.

![](/assets/r-pro-1-ld2412-connect-and-eng-mode.gif)

3\. Once connected, enable **Engineering Mode** as shown above. This turns on the live energy graph, which shows you what the sensor is actually seeing at each distance gate in real time.

!!! tip "Reading the engineering mode graph"

    The horizontal axis represents distance gates (each gate = 0.75m from the sensor). Two sets of bars are shown: one for **moving targets** and one for **still targets**. The colored threshold line is the sensitivity setting you've configured for each gate. When the live energy bar at a gate exceeds that threshold, the sensor reports detection at that distance.

    Think of it like a ruler pointing away from the sensor, where each column is one step further out (0.75m per step). The taller a bar rises, the stronger the signal at that distance. When a bar crosses the threshold line, the sensor reports detection there. Walk around in front of it to see your movement show up in real time.

4\. Leave the room empty and make sure nothing is moving, then tap **Auto** in the app. The sensor scans the environment for about 10 seconds and automatically sets thresholds to filter out static interference from electronics, HVAC, and other background sources. When it's done you'll see **Completed** and the app will return to showing the detection distance. This gives you a clean baseline before any manual tuning.

![](/assets/r-pro-1-ld2412-auto-noise-detection.gif)

5\. Tap **Settings** in the top right and use the **Detection Range** slider to set which gates the sensor monitors. You can set both a start and end gate — for example, Gate 3 to Gate 6 means the sensor only looks between 2.25m and 4.5m from the device. Limiting the range prevents the sensor from picking up movement through walls or in adjacent rooms.

!!! tip "Gate to distance reference"

    Each gate is 0.75m. Gate 1 = 0.75m, Gate 2 = 1.5m, Gate 3 = 2.25m, Gate 4 = 3m, Gate 5 = 3.75m, Gate 6 = 4.5m, Gate 7 = 5.25m, Gate 8 = 6m.

![](/assets/r-pro-1-ld2412-detection-range.gif)

6\. To fine-tune which distances trigger detection, head to the <a href="http://homeassistant.local:8123/config/integrations/integration/esphome" title="Click me to go to the ESPHome integrations page" target="_blank" rel="noreferrer nofollow noopener">ESPHome Integrations page</a>, select your R-PRO-1, and use the gate sensitivity sliders on the device page.

- **Raise** a gate's sensitivity to make it harder to trigger at that distance (useful for ignoring a fan, HVAC vent, or a window where cars pass).
- **Lower** a gate's sensitivity to make it more sensitive at that distance (useful for reliably detecting someone sitting still in a chair).

![](/assets/r-pro-1-ld2412-gate-sliders-ha.gif)

7\. Tap **Settings** at the top of the app and set the **Unmanned Duration**. This controls how many seconds the sensor waits after it stops detecting before it reports "no one present." The default is 10 seconds — increase it if you're getting false "nobody home" readings in your space. In Home Assistant, this same setting is called **LD2412 Timeout**.

8\. Head back to the <a href="http://homeassistant.local:8123/config/integrations/integration/esphome" title="Click me to go to the ESPHome integrations page" target="_blank" rel="noreferrer nofollow noopener">ESPHome Integrations page</a>, select your R-PRO-1, and toggle **LD2412 Bluetooth** back off. Leaving Bluetooth on increases power consumption and can interfere with nearby Bluetooth devices.

