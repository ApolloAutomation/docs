---
title: Apollo Battery Devices - Sensor Connection Check
description: Restart your Apollo battery device and read its RGB light to see whether it's connected to Wi-Fi, Homey, or nothing.
---
# Sensor connection check

Not sure whether your battery device is online? Run this quick check. You restart the device and press its boot button, and the RGB light flashes a color that shows whether it's connected to Wi-Fi, to Homey, or to nothing. Select your device below. Each button name links to a page that shows where that button is.

=== "TEMP-1B"

    1\. Press the <a href="https://wiki.apolloautomation.com/homey/products/temp1b/troubleshooting/temp1b-boot-mode" target="_blank" rel="noopener">reset button</a> and let go to restart the device.

    ![TEMP-1B board with the lid off and a tool pointing at the reset button](/assets/temp-1-reset-button-lid-off.jpg)

    2\. Then press the <a href="https://wiki.apolloautomation.com/homey/products/temp1b/troubleshooting/temp1b-boot-mode" target="_blank" rel="noopener">boot button</a> and let go.

    ![TEMP-1B board with the lid off and a tool pointing at the boot button](/assets/temp-1b-boot-button-lid-off.jpg)

=== "PLT-1B"

    1\. Press the <a href="https://wiki.apolloautomation.com/homey/products/plt1b/troubleshooting/plt1b-boot-mode/" target="_blank" rel="noopener">reset button</a> and let go to restart the device.

    ![PLT-1B board with a tool pointing at the reset button](/assets/plt-boot-mode-pic-6-1.jpg)

    2\. Then press the <a href="https://wiki.apolloautomation.com/homey/products/plt1b/troubleshooting/plt1b-boot-mode/" target="_blank" rel="noopener">boot button</a> and let go.

    ![PLT-1B board with a tool pointing at the boot button near the USB-C port](/assets/plt-boot-mode-pic-2.jpg)

The RGB light on your device then flashes a color that shows its connection status:

- **Blue**: connected to Wi-Fi and Homey
- **Green**: connected to Wi-Fi only, not to Homey
- **Yellow**: no Wi-Fi connection

!!! tip "Read the first flash, not the second"

    A few seconds later the light flashes a second time, green or red. That second flash is the device's built-in sensor self-test, not its connection status, so read the connection status from the first color.

!!! tip "Keep your sensor awake with Prevent Sleep"

    To keep your sensor awake for extended periods of time, open the device in Homey, go to its settings, and turn on **Prevent sleep** under **Battery settings (if battery is present)**. Homey can only change this setting while the sensor is awake, so press the reset button first. To learn more, see the Prevent Sleep guide for the [TEMP-1](https://wiki.apolloautomation.com/homey/products/temp1/setup/prevent-sleep/), [TEMP-1B](https://wiki.apolloautomation.com/homey/products/temp1b/setup/prevent-sleep/), or [PLT-1B](https://wiki.apolloautomation.com/homey/products/plt1b/setup/prevent-sleep/).
