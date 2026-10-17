---
title: (Better) HLK Radar Tool app
description: "Tutorial for MTR-1 HLKRadarTool app Zone Configuration."
---

!!! tip "Finding your MTR-1's web server address"

    Some steps below require opening your device's web server in a browser. To find your address:

    1. In Homey, open your MTR-1 device and note the last 6 characters of its name. For example, **Apollo MTR-1 c64a28** gives you `c64a28`.
    2. Build your URL: `http://apollo-mtr-1-c64a28.local/`

    If the `.local` address doesn't load, use your router to find the device's IP address and use that instead.

## Configure zones

!!! note "Ensure that the LD2450 firmware version is V2.02.23090617 or later for proper integration functionality. "

    The newer version of the firmware includes an "auto calibrate" function so you might want to test it out!

The <a href="https://www.hlktech.net/index.php?id=1157" target="_blank" rel="noreferrer nofollow noopener">HLK-LD2450</a> mmWave sensor is used in the MTR-1. <a href="https://drive.google.com/drive/folders/1aItrdziwnEqI-ovDWf24Lj6ioALaljFA?usp=sharing" target="_blank" rel="noreferrer nofollow noopener">Click Here</a> for the datasheet.

=== "iPhone"

    <a href="https://apps.apple.com/us/app/hlkradartool/id1638651152" target="_blank" rel="noreferrer nofollow noopener">Click here to download</a>

=== "Android"

    <a href="https://play.google.com/store/apps/details?id=com.hlk.hlkradartool&amp;hl=en_US" target="_blank" rel="noreferrer nofollow noopener">Click here to download</a>

With the app installed, you'll turn on the radar's Bluetooth, connect to it from the HLKRadarTool app, and set up your zones.

1\. Open your MTR-1's web server (see address tip above), scroll down until you see **LD2450 Bluetooth**, and toggle it on.

![MTR-1 Configuration card with the LD2450 Bluetooth toggle turned on and highlighted](/assets/mtr-1-toggle-on-ld2450-bluetooth.png)

2\. Open the HLKRadarTool App and select your device.

!!! success "You need to be close to your device!"

    The LD2450 mmWave sensor is a very tiny sensor with no external antenna, which means it cannot connect to Bluetooth devices unless they are very close. Sometimes this means you need to be within a few feet of the sensor to connect directly to it!

![HLKRadarTool device list showing the HLK-LD2450 radar found over Bluetooth](/assets/screenshot-20240514-100155-hlkradartool.jpg)

3\. Select Set in the top right.

![HLKRadarTool live radar view of the LD2450 with the Set button circled in the top right](/assets/Esxscreenshot-20240514-100250-hlkradartool.jpg)

4\. Select **Area Detection**, then toggle Area 1, 2, or 3 and you will see a box with the corresponding number pop up. Then you can press and hold the box to move it and resize it. When your zones are set then select Submit and you should see Setup successfully.

!!! tip "There are three ways to use your MTR-1!"

    You can use any of these three choices to control your MTR-1 differently. The most common option is **Area Detection**, which lets you set up three areas and track three targets within them.<br>**Close detection** (Disabled on the web server): zone detection is off<br>**Area Detection** (Detection): only detects targets inside your zones<br>**Area Filtering** (Filter): ignores targets inside your zones

    Close detection lets you use the sensor as a basic presence sensor, and Area Filtering lets you filter out an area and detect everything else, which is useful to avoid a fan!

![HLKRadarTool Parameter settings with Area Detection selected, three areas drawn, and a Setup successfully message](/assets/screenshot-20240514-100512-hlkradartool.jpg)

5\. If set up correctly the zones should be saved as different colors. You should be all set!

![HLKRadarTool radar view showing three saved zones in red, green, and blue with a target in zone 1](/assets/screenshot-20240514-102430-hlkradartool.jpg)

!!! tip "Helpful Hints to understand zones better!"

    * X1 must always be less than X2, and Y1 must always be less than Y2.

    * The Y axis is easier since it's never negative.

      &nbsp;

    * The X axis is where you can get tripped up, especially when both values are negative: -3456 is less than -2345.
    * The zones cannot overlap.
