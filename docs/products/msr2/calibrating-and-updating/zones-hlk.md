---
title: MSR-2 HLKRadarTool app Zone Configuration
description: Tutorial for MSR-2 HLKRadarTool app Zone Configuration.
---
# How To Tune MSR-2 Using HLKRadarTool

###### **Auto-Calibration**

1\. Download the HLKRadarTool app.

=== "iPhone"

    <a href="https://apps.apple.com/us/app/hlkradartool/id1638651152" target="_blank" rel="noreferrer nofollow noopener">Click Here to download</a>

=== "Android"

    <a href="https://play.google.com/store/apps/details?id=com.hlk.hlkradartool&amp;hl=en_US" target="_blank" rel="noreferrer nofollow noopener">Click here to download</a>

The default password to connect to the HLKRadarTool is "HiLink".

1\. Head to the <a href="http://homeassistant.local:8123/config/integrations/integration/esphome" title="Click me to go to the ESPHome integrations page" target="_blank" rel="noreferrer nofollow noopener">ESPHome Integrations page</a> then select your MSR-2 and scroll down until you see LD2410 Bluetooth.

![](../../../assets/msr-2-toggle-on-ld2410-bluetooth.png)

2\. Open the app and select your device

![Find Device.png](../assets/find-device.png)

3\. Turn on Engineering Mode

![EM.png](../assets/em.png)

4\. Select More and then select Parameter settings

![More and PS.png](../assets/more-and-ps.png)

5\. Select Detect background noise

![DBN.png](../assets/dbn.png)

6\. Insert Delay detection and Detection time values. (For iPhone users Delay detection cannot be 0). Then select Start. This will give us our reference values so we can auto-calibrate the mmWave sensor.

![DD, DT and Start.png](../assets/dd-dt-and-start.png)

7\. Select Back to navigate to the Parameter settings. Then select one of the auto-calibration buttons.

**Average** - Sets the gate sensitivity to the average move and still energy

![Average.png](../assets/average.png)

**Maximum** - Sets the gate sensitivity to the maximum move and still energy

![Max.png](../assets/max.png)

**Intelligent** - Sets the gate sensitivity equal to or just above the maximum move and still energy.

**![Intelligent.png](../assets/intelligent.png)**

###### Manual Calibration

1\. Repeat steps 1-5 above.

2\. Select Motion or Static sensitivity, change it to your desired value, and select Set.

![Manual.png](../assets/manual.png)

3\. Now your MSR-2 should be tuned to your environment!