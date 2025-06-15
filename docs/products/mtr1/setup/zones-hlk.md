---
title: MTR-1 HLKRadarTool app Zone Configuration
description: Tutorial for MTR-1 HLKRadarTool app Zone Configuration.
---
<div class="cms-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/-w_GFURyx-A?si=SSRovumabCvHeXwo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen=""></iframe></div>

###### Configure Zones

!!! note "Ensure that the LD2450 firmware version is V2.02.23090617 or later for proper integration functionality. "

    The newer version of the firmware includes an "auto calibrate" function so you might want to test it out!

The <a href="https://www.hlktech.net/index.php?id=1157" target="_blank" rel="noreferrer nofollow noopener">HLK-LD2450</a> mmWave sensor is used in the MTR-1. <a href="https://drive.google.com/drive/folders/1aItrdziwnEqI-ovDWf24Lj6ioALaljFA?usp=sharing" target="_blank" rel="noreferrer nofollow noopener">Click Here</a> for the datasheet.

1\. Ensure the mmWave radar you want to configure has Radar Control Bluetooth turned on. Home Assistant &gt; Settings &gt; Devices & services &gt; ESPHome Devices &gt; Select Device &gt; Scroll down and toggle on Radar Control Bluetooth<br> ![Screenshot 2024-05-14 at 10.30.31 AM.png](../assets/screenshot-2024-05-14-at-10-30-31-am.png)<br> 2. Open the HLKRadarTool App and select your device<br> ![Screenshot_20240514_100155_HLKRadarTool.jpg](../assets/screenshot-20240514-100155-hlkradartool.jpg)<br> 3. Select Set in the top right<br> ![Screenshot_20240514_100250_HLKRadarTool.jpg](../assets/Esxscreenshot-20240514-100250-hlkradartool.jpg)<br> 4. Select Close Detection, Area Detection, or Area Filtering. Then toggle Area 1, 2, or 3 and you will see a box with the corresponding number pop up. Then you can press and hold the box to move it and resize it. When your zones are set then select Submit and you should see Setup successfully!<br> - Close Detection: Disable zone area detection<br> - Area Detection: Only detects targets in the specified zone<br> - Area Filtering: Excludes a zone from detection<br> ![Screenshot_20240514_100512_HLKRadarTool.jpg](../assets/screenshot-20240514-100512-hlkradartool.jpg)<br> 5. If set up correctly the zones should be saved as different colors. You can double-check that the settings are saved by looking at your HA entities (picture below). You should be all set!<br> ![Screenshot 2024-05-14 at 11.27.17 AM.png](../assets/screenshot-2024-05-14-at-11-27-17-am.png)![Screenshot_20240514_102430_HLKRadarTool.jpg](../assets/screenshot-20240514-102430-hlkradartool.jpg)

!!! tip "Helpful Hints to understand zones better!"

    * X1 must always be less than X2, and Y1 must always be less than Y2.

    * The Y axis is easier since it's never negative.

      &nbsp;

    * The X axis is where you can get tripped up, especially when both values are negative: -3456 is less than -2345.
    * The Plotly chart will still render the rectangles even if the X1/X2 and Y1/Y2 values are reversed.
    * The zones cannot overlap.

###### Dashboard Card Setup

6\. Copy the code below and add a Home Assistant card to visualize your zones. You will need to change all of the sensor\_apollo\_mtr\_1 entity IDs to match your MTR-1 device. This can be done quickly by using a code editor or ChatGPT.<br> ![Screenshot 2024-05-14 at 11.27.44 AM.png](../assets/screenshot-2024-05-14-at-11-27-44-am.png)

```
type: custom:plotly-graph
title: Target Positions
refresh_interval: 1
hours_to_show: current_day
layout:
  height: 230
  margin:
    l: 50
    r: 20
    t: 20
    b: 40
  showlegend: true
  xaxis:
    dtick: 1000
    gridcolor: RGBA(200,200,200,0.15)
    zerolinecolor: RGBA(200,200,200,0.15)
    type: number
    fixedrange: true
    range:
      - -4000
      - 4000
  yaxis:
    dtick: 1000
    gridcolor: RGBA(200,200,200,0.15)
    zerolinecolor: RGBA(200,200,200,0.15)
    scaleanchor: x
    scaleratio: 1
    fixedrange: true
    range:
      - 7500
      - 0
entities:
  - entity: ''
    name: Target1
    marker:
      size: 12
    line:
      shape: spline
      width: 5
    x:
      - $ex hass.states["sensor.apollo_mtr_1_982da4_target_1_x"].state
    'y':
      - $ex hass.states["sensor.apollo_mtr_1_982da4_target_1_y"].state
  - entity: ''
    name: Target2
    marker:
      size: 12
    line:
      shape: spline
      width: 5
    x:
      - $ex hass.states["sensor.apollo_mtr_1_982da4_target_2_x"].state
    'y':
      - $ex hass.states["sensor.apollo_mtr_1_982da4_target_2_y"].state
  - entity: ''
    name: Target3
    marker:
      size: 12
    line:
      shape: spline
      width: 5
    x:
      - $ex hass.states["sensor.apollo_mtr_1_982da4_target_3_x"].state
    'y':
      - $ex hass.states["sensor.apollo_mtr_1_982da4_target_3_y"].state
  - entity: ''
    name: Zone1
    mode: lines
    fill: toself
    fillcolor: RGBA(20,200,0,0.06)
    line:
      color: RGBA(20,200,0,0.2)
      shape: line
      width: 2
    x:
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_1_x1"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_1_x1"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_1_x2"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_1_x2"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_1_x1"].state
    'y':
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_1_y1"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_1_y2"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_1_y2"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_1_y1"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_1_y1"].state
  - entity: ''
    name: Zone2
    mode: lines
    fill: toself
    fillcolor: RGBA(200,0,255,0.06)
    line:
      color: RGBA(200,0,255,0.2)
      shape: line
      width: 2
    x:
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_2_x1"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_2_x1"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_2_x2"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_2_x2"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_2_x1"].state
    'y':
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_2_y1"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_2_y2"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_2_y2"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_2_y1"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_2_y1"].state
  - entity: ''
    name: Zone3
    mode: lines
    fill: toself
    fillcolor: RGBA(200,120,55,0.06)
    line:
      color: RGBA(200,120,55,0.2)
      shape: line
      width: 2
    x:
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_3_x1"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_3_x1"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_3_x2"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_3_x2"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_3_x1"].state
    'y':
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_3_y1"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_3_y2"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_3_y2"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_3_y1"].state
      - $ex hass.states["number.apollo_mtr_1_982da4_zone_3_y1"].state
  - entity: ''
    name: Coverage
    mode: lines
    fill: tonexty
    fillcolor: rgba(168, 216, 234, 0.15)
    line:
      shape: line
      width: 1
      dash: dot
    x:
      - 0
      - $ex 7500 * Math.sin((2 * Math.PI)/360 * 60)
      - 4500
      - 4000
      - 3000
      - 2000
      - 1000
      - 0
      - -1000
      - -2000
      - -3000
      - -4000
      - -4500
      - $ex -7500 * Math.sin((2 * Math.PI)/360 * 60)
      - 0
    'y':
      - 0
      - $ex 7500 * Math.cos((2 * Math.PI)/360 * 60)
      - $ex Math.sqrt( 7500**2 - 4500**2 )
      - $ex Math.sqrt( 7500**2 - 4000**2 )
      - $ex Math.sqrt( 7500**2 - 3000**2 )
      - $ex Math.sqrt( 7500**2 - 2000**2 )
      - $ex Math.sqrt( 7500**2 - 1000**2 )
      - 7500
      - $ex Math.sqrt( 7500**2 - 1000**2 )
      - $ex Math.sqrt( 7500**2 - 2000**2 )
      - $ex Math.sqrt( 7500**2 - 3000**2 )
      - $ex Math.sqrt( 7500**2 - 4000**2 )
      - $ex Math.sqrt( 7500**2 - 4500**2 )
      - $ex 7500 * Math.cos((2 * Math.PI)/360 * 60)
      - 0
raw_plotly_config: true
```