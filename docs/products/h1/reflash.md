---
title: Factory Re-Flash H-1
description: Step by step guide for re-flashing the H-1 back to factory firmware.
---
If your device becomes unresponsive and you've exhausted the other troubleshooting methods you can upload a fresh set of firmware by following the below guide. The utility does need to be run from Chrome or Edge.

If your device has already been connected to Home Assistant previously please refer to Removing Device From Home Assistant first before proceeding

1. Hold the boot button then plug your sensor into your computer with a quality USB-C cable that supports data transfer. Let go of the boot button once you plug the USB cable in!
2. Navigate to our installer page and click connect [\*\* Install Page \*\*](https://apolloautomation.github.io/H-1/)
3. Select your Apollo device, it will show with a similar name to the one below, and click connect. If you aren't sure which device it is, you can unplug the sensor and see which disappears.

![Browser serial port dialog listing the USB JTAG/serial debug unit to connect](/assets/comselection.png)

If no device shows, click cancel and then install the recommended driver that shows on the popup. If you have installed the driver, tried different cables, and it still won't work refer [here](https://wiki.apolloautomation.com/products/h1/boot-mode/) for putting the sensor in bootloader mode and then retry step 3.

4\. Choose to install the new firmware

![Web installer Device Dashboard dialog with the Install option and Logs and Console](/assets/image-1698806750134.png)

*Shown with the MSR-1 installer; the H-1 installer looks the same.*

5\. Wait for the installer to finish - if you see "ERROR Logger is not configured!" that is totally expected! The logger is disabled to make more room for other components on the microcontroller.

![Web installer dialog showing a spinner while preparing the installation](/assets/image-1698806082666.png)

*Shown with the MSR-1 installer; the H-1 installer looks the same.*

6\. VERY IMPORTANT - you need to unplug your device and plug it back in to leave boot mode!

1. After finishing, check for the Apollo hotspot and connect. This might not show if you previously had the H-1 connected to your Wi-Fi
2. Log into Home Assistant and go to the ESPHome app check to see if you can adopt the device.

    [![Open your Home Assistant instance and show the dashboard of an app.](https://my.home-assistant.io/badges/supervisor_app.svg)](https://my.home-assistant.io/redirect/supervisor_app/?app=5c53de3b_esphome&repository_url=https%3A%2F%2Fgithub.com%2Fesphome%2Fhome-assistant-addon)

If you encounter the below error, please complete the [Putting H-1 In Boot Mode Document](https://wiki.apolloautomation.com/products/h1/boot-mode/) and go back to step 3.

![Web installer error: Failed to initialize, try holding the BOOT button while clicking Install](/assets/image-1698806793309.png)

*Shown with the MSR-1 installer; the H-1 shows the same error.*