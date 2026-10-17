---
title: Apollo Battery Devices - Sensor Connection Check
description: How to check if your device is connected to Wi-Fi, Homey, or nothing.
---
# Sensor Connection Check

1\. Press the reset button and let go to restart the device<br><a href="https://wiki.apolloautomation.com/homey/products/temp1b/troubleshooting/temp1b-boot-mode" target="_blank" rel="noopener"><strong>TEMP-1B reset button</strong></a>

![TEMP-1B board with the lid off and a tool pointing at the reset button](/assets/temp-1-reset-button-lid-off.jpg)

<a href="https://wiki.apolloautomation.com/homey/products/plt1b/troubleshooting/plt1b-boot-mode/" target="_blank" rel="noopener"><strong>PLT-1B reset button</strong></a>

![PLT-1B board with a tool pointing at the reset button](/assets/plt-boot-mode-pic-6-1.jpg)

2\. Press the boot button and let go<br><a href="https://wiki.apolloautomation.com/homey/products/temp1b/troubleshooting/temp1b-boot-mode" target="_blank" rel="noopener"><strong>TEMP-1B boot button</strong></a>

![TEMP-1B board with the lid off and a tool pointing at the boot button](/assets/temp-1b-boot-button-lid-off.jpg)

<a href="https://wiki.apolloautomation.com/homey/products/plt1b/troubleshooting/plt1b-boot-mode/" target="_blank" rel="noopener"><strong>PLT-1B boot button</strong></a>

![PLT-1B board with a tool pointing at the boot button near the USB-C port](/assets/plt-boot-mode-pic-2.jpg)

The RGB light on your device flashes a color that shows its connection status: blue if it's connected to Wi-Fi and Homey, green if it's connected to Wi-Fi but not to Homey, or yellow if it isn't connected to Wi-Fi.

Blue: Connected to Wi-Fi and Homey<br>Green: Connected to Wi-Fi only, not to Homey<br>Yellow: No Wi-Fi connection

A few seconds later the light flashes a second time, green or red. That second flash is the device's built-in sensor self-test, not its connection status, so read the connection status from the first color.

!!! tip "Keep your sensor awake with Prevent Sleep"

    If you need to keep your sensor awake for extended periods of time, open the device in Homey, go to its settings, and turn on **Prevent sleep** under **Battery settings (if battery is present)**. Homey can only change this setting while the sensor is awake, so press the reset button first. To learn more, see the Prevent Sleep guide for the [TEMP-1](https://wiki.apolloautomation.com/homey/products/temp1/setup/prevent-sleep/), [TEMP-1B](https://wiki.apolloautomation.com/homey/products/temp1b/setup/prevent-sleep/), or [PLT-1B](https://wiki.apolloautomation.com/homey/products/plt1b/setup/prevent-sleep/).