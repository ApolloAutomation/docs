---
title: R-Pro-1 HLKRadarTool app Zone Configuration
description: Tutorial for R-Pro-1 HLKRadarTool app Zone Configuration.
---
# How To Tune mmWave Using HLKRadarTool

###### **Auto-Calibration**

1\. Download the HLKRadarTool app for either [Android](https://play.google.com/store/apps/details?id=com.hlk.hlkradartool&amp;hl=en_US%E2%89%B7=US)or [Apple](https://apps.apple.com/us/app/hlkradartool/id1638651152).

The default password to connect to the HLKRadarTool is "HiLink"

2\. Ensure the mmWave radar you want to tune has LD2410 Bluetooth turned on. Home Assistant &gt; Settings &gt; Devices & services &gt; ESPHome Devices &gt; Select Device &gt; Scroll down and toggle on ld2410 Bluetooth.

![Radar Control Bluetooth.png](assets/msr-2-mmwave-hlk-pic-1.png)

3\. Open the app and select your device

![Find Device.png](../assets/find-device.png)

4\. Turn on Engineering Mode

![EM.png](../assets/em.png)

5\. Select More and then select Parameter settings

![More and PS.png](../assets/more-and-ps.png)

6\. Select Detect background noise

![DBN.png](../assets/dbn.png)

7\. Insert Delay detection and Detection time values. (For iPhone users Delay detection cannot be 0). Then select Start. This will give us our reference values so we can auto-calibrate the mmWave sensor.

![DD, DT and Start.png](../assets/dd-dt-and-start.png)

8\. Select Back to navigate to the Parameter settings. Then select one of the auto-calibration buttons.

**Average** - Sets the gate sensitivity to the average move and still energy

![Average.png](../assets/average.png)

**Maximum** - Sets the gate sensitivity to the maximum move and still energy

![Max.png](../assets/max.png)

**Intelligent** \- Sets the gate sensitivity equal to or just above the maximum move and still energy.

**![Intelligent.png](../assets/intelligent.png)**

###### Manual Calibration

1\. Repeat steps 1-5 above.

2\. Select Motion or Static sensitivity, change it to your desired value, and select Set.

![Manual.png](../assets/manual.png)

3\. Now your MSR-2 should be tuned to your environment!