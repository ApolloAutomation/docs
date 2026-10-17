---
title: MSR-2 HLKRadarTool app zone configuration
description: Tutorial for MSR-2 HLKRadarTool app Zone Configuration.
---
# How to tune MSR-2 using HLKRadarTool

## **Auto-calibration**

You'll connect the HLKRadarTool app to your sensor, measure your room's background noise, and pick one of the auto-calibration settings.

1\. Download the HLKRadarTool app.

=== "iPhone"

    <a href="https://apps.apple.com/us/app/hlkradartool/id1638651152" target="_blank" rel="noreferrer nofollow noopener">Click Here to download</a>

=== "Android"

    <a href="https://play.google.com/store/apps/details?id=com.hlk.hlkradartool&amp;hl=en_US" target="_blank" rel="noreferrer nofollow noopener">Click here to download</a>

The default password to connect to the HLKRadarTool is "HiLink".

2\. Head to the **ESPHome** integration page (**Settings → Devices & services → ESPHome**) then select your MSR-2 and scroll down until you see LD2410 Bluetooth.

[![Open your Home Assistant instance and show an integration.](https://my.home-assistant.io/badges/integration.svg)](https://my.home-assistant.io/redirect/integration/?domain=esphome)

![Home Assistant MSR-2 device page with the LD2410 Bluetooth toggle switched on, outlined in red](/assets/msr-2-toggle-on-ld2410-bluetooth.png)

3\. Open the app and select your device

![HLKRadarTool Device list showing the HLK-LD2410 radar found over Bluetooth](/assets/find-device.png)

4\. Turn on Engineering Mode

![HLKRadarTool device screen with the Engineering mode toggle switched on, outlined in red](/assets/em.png)

5\. Select More and then select Parameter settings

![HLKRadarTool device screen with More and then Parameter settings outlined in red](/assets/more-and-ps.png)

6\. Select Detect background noise

![HLKRadarTool Parameter settings with the Detect background noise option outlined in red](/assets/dbn.png)

7\. Insert Delay detection and Detection time values. (For iPhone users Delay detection cannot be 0). Then select Start. This will give us our reference values so we can auto-calibrate the mmWave sensor.

![HLKRadarTool Bottom noise statistics with Delay detection, Detection time, and Start outlined](/assets/dd-dt-and-start.png)

8\. Select Back to navigate to the Parameter settings. Then select one of the auto-calibration buttons.

**Average**: Sets the gate sensitivity to the average move and still energy

![HLKRadarTool Parameter settings with the Average one click setting outlined in red](/assets/average.png)

**Maximum**: Sets the gate sensitivity to the maximum move and still energy

![HLKRadarTool Parameter settings with the Maximum one click setting outlined in red](/assets/max.png)

**Intelligent**: Sets the gate sensitivity equal to or just above the maximum move and still energy.

**![HLKRadarTool Parameter settings with the Intelligent one click setting outlined in red](/assets/intelligent.png)**

## Manual calibration

You'll set the motion and static sensitivity values yourself in the app.

1\. Repeat steps 1-5 above.

2\. Select Motion or Static sensitivity, change it to your desired value, and select Set.

![HLKRadarTool gate table with motion and static sensitivity values and the Set button outlined](/assets/manual.png)

3\. Now your MSR-2 should be tuned to your environment!