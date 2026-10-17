---
title: How to tune mmWave using HLKRadarTool
description: "Tune the mmWave radar in your MSR-2 with the HLKRadarTool phone app, using one-click auto-calibration or your own sensitivity values."
---
# How to tune mmWave using HLKRadarTool

The HLKRadarTool phone app connects to the radar in your Apollo MSR-2 over Bluetooth, so you can tune the mmWave sensor to your room. You have two options: let the app set the gate sensitivity for you from a background-noise reading (auto-calibration), or set the sensitivity values yourself (manual calibration).

## Auto-calibration (Average, Maximum, and Intelligent)

In auto-calibration, the app first measures your room's background noise, then uses that reading to set the gate sensitivity in one click. Follow these steps to connect to the radar, take the reading, and pick a calibration mode.

1\. Download the HLKRadarTool app for [Android](https://play.google.com/store/apps/details?id=com.hlk.hlkradartool&hl=en_US&gl=US) or [Apple](https://apps.apple.com/us/app/hlkradartool/id1638651152).

- The default password to connect to the HLKRadarTool is `HiLink`.

2\. Turn on the radar's Bluetooth from your MSR-2's built-in web page. In a browser, go to the device's `.local` address (see the tip below) or `http://<device IP>`, scroll down to **ld2410 Bluetooth**, and turn it on.

!!! tip "Finding your MSR-2's web page address"

    1. In Homey, open your MSR-2 device and note the last 6 characters of its name. For example, **Apollo MSR-2 c64a28** gives you `c64a28`.
    2. Build your URL: `http://apollo-msr-2-c64a28.local/`

    If the `.local` address doesn't load, use your router to find the device's IP address and go to `http://<device IP>` instead.

3\. Open the HLKRadarTool app and select your device.

![HLKRadarTool device list showing the HLK-LD2410 radar found nearby](/assets/find-device.png)

4\. Turn on **Engineering Mode**.

![HLKRadarTool device screen with the Engineering mode toggle turned on and outlined in red](/assets/em.png)

5\. Select **More**, then select **Parameter settings**.

![HLKRadarTool device screen with More and Parameter settings outlined in red](/assets/more-and-ps.png)

6\. Select **Detect background noise**.

![HLKRadarTool Parameter settings with Detect background noise outlined in red](/assets/dbn.png)

7\. Enter the **Delay detection** and **Detection time** values, then select **Start**. On iPhone, **Delay detection** can't be 0. The app measures your room's background noise, which gives it the reference values it needs to auto-calibrate the mmWave sensor.

![HLKRadarTool Bottom noise statistics with Delay detection, Detection time, and Start outlined in red](/assets/dd-dt-and-start.png)

8\. Select **Back** to return to **Parameter settings**, then select one of the auto-calibration buttons:

- **Average** sets the gate sensitivity to the average move and still energy.

    ![HLKRadarTool Parameter settings with the Average one click setting button outlined in red](/assets/average.png)

- **Maximum** sets the gate sensitivity to the maximum move and still energy.

    ![HLKRadarTool Parameter settings with the Maximum one click setting button outlined in red](/assets/max.png)

- **Intelligent** sets the gate sensitivity equal to or just above the maximum move and still energy.

    ![HLKRadarTool Parameter settings with the Intelligent one click setting button outlined in red](/assets/intelligent.png)

Your mmWave sensor is now tuned to your environment.

## Manual calibration

To choose the sensitivity values yourself, set them directly in the app's **Parameter settings**.

1\. Follow steps 1 to 5 in the auto-calibration section above.

2\. Select Motion or Static sensitivity, change it to the value you want, and select **Set**.

![HLKRadarTool Parameter settings with the 0M motion and static sensitivity values and Set outlined in red](/assets/manual.png)

Your mmWave sensor is now tuned to your environment.
