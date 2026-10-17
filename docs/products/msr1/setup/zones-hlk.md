---
title: How to tune mmWave using HLKRadarTool
description: "Tune the MSR-1 mmWave radar over Bluetooth with the HLKRadarTool phone app, covering both auto-calibration and manual gate settings."
---
# How to tune mmWave using HLKRadarTool

The HLKRadarTool phone app connects to your mmWave radar over Bluetooth, so you can tune it to your room. You have two options: let the app set the gate sensitivity for you from a background-noise reading (auto-calibration), or set the sensitivity values yourself (manual calibration).

## Auto-calibration (Average, Maximum, and Intelligent)

In auto-calibration, the app first measures your room's background noise, then uses that reading to set the gate sensitivity in one click. Follow these steps to connect to the radar, take the reading, and pick a calibration mode.

1\. Download the HLKRadarTool app for [Android](https://play.google.com/store/apps/details?id=com.hlk.hlkradartool&hl=en_US&gl=US) or [Apple](https://apps.apple.com/us/app/hlkradartool/id1638651152).

2\. Turn on Bluetooth for the mmWave radar you want to tune. In Home Assistant, go to **Settings → Devices & services → ESPHome Devices**, select your device, scroll down, and turn on **Radar Control Bluetooth**.

[![Open your Home Assistant instance and show an integration.](https://my.home-assistant.io/badges/integration.svg)](https://my.home-assistant.io/redirect/integration/?domain=esphome)

![Radar Control Bluetooth switch turned on in the MSR-1 Home Assistant device page, outlined in red](/assets/radar-control-bluetooth.png)

3\. Open the HLKRadarTool app and select your device.

![HLKRadarTool Device list showing the HLK-LD2410 radar found over Bluetooth](/assets/find-device.png)

4\. Turn on **Engineering Mode**.

![HLKRadarTool device screen with the Engineering mode toggle turned on and outlined in red](/assets/em.png)

5\. Select **More**, then select **Parameter settings**.

![HLKRadarTool device screen with More and Parameter settings outlined in red](/assets/more-and-ps.png)

6\. Select **Detect background noise**.

![HLKRadarTool Parameter settings with Detect background noise outlined in red](/assets/dbn.png)

7\. Enter the **Delay detection** and **Detection time** values, then select **Start**. On iPhone, **Delay detection** can't be 0. The app measures your room's background noise, which gives it the reference values it needs to auto-calibrate the mmWave sensor.

![HLKRadarTool Bottom noise statistics with Delay detection, Detection time, and START outlined in red](/assets/dd-dt-and-start.png)

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

![HLKRadarTool gate sensitivity table with motion and static values and the Set button outlined in red](/assets/manual.png)

Your mmWave sensor is now tuned to your environment.
