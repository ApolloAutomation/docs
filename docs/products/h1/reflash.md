---
title: Factory Re-Flash H-1
description: Step-by-step guide to re-flashing the H-1 back to its factory firmware from Chrome or Edge.
---
# Factory re-flash H-1

If your Apollo H-1 becomes unresponsive and you've exhausted the other troubleshooting methods, you can upload a fresh set of firmware to it by following this guide.

!!! note "Before you start"

    - Use Chrome or Edge. The install utility needs to run from one of them.
    - Already added this H-1 to Home Assistant? [Remove it from Home Assistant](../../general/troubleshooting/removing-device-from-home-assistant/) first, then come back here.

Follow these steps to flash fresh firmware onto your H-1 and find it again in Home Assistant.

1\. Hold the boot button, then plug your H-1 into your computer with a quality USB-C cable that supports data transfer. Let go of the boot button once the USB cable is plugged in.

2\. Open our [H-1 install page](https://apolloautomation.github.io/H-1/) and click **Connect**.

3\. Select your Apollo device and click **Connect**. It shows with a name similar to the one below. If you aren't sure which device it is, unplug the H-1 and see which one disappears.

![Browser serial port dialog listing the USB JTAG/serial debug unit to connect](/assets/comselection.png)

!!! tip "No device in the list?"

    Click **Cancel**, then install the recommended driver that shows on the popup. If you've installed the driver and tried different cables and it still won't work, [put the H-1 in bootloader mode](https://wiki.apolloautomation.com/products/h1/boot-mode/) and then retry step 3.

4\. Choose to install the new firmware.

![Web installer Device Dashboard dialog with the Install option and Logs and Console](/assets/image-1698806750134.png)

*Shown with the MSR-1 installer; the H-1 installer looks the same.*

!!! warning "Seeing the error below?"

    If the installer shows this error, complete the [H-1 boot mode guide](https://wiki.apolloautomation.com/products/h1/boot-mode/) and go back to step 3.

    ![Web installer error: Failed to initialize, try holding the BOOT button while clicking Install](/assets/image-1698806793309.png)

    *Shown with the MSR-1 installer; the H-1 shows the same error.*

5\. Wait for the installer to finish. If you see "ERROR Logger is not configured!", that's expected: the logger is disabled to make more room for other components on the microcontroller.

![Web installer dialog showing a spinner while preparing the installation](/assets/image-1698806082666.png)

*Shown with the MSR-1 installer; the H-1 installer looks the same.*

6\. Unplug your H-1 and plug it back in to leave boot mode. **Don't skip this step.** The H-1 stays in boot mode until you do.

7\. Check for the Apollo hotspot and connect to it. The hotspot might not show if your H-1 was connected to your Wi-Fi before.

8\. Log into Home Assistant, go to the ESPHome app, and check whether you can adopt the device.

[![Open your Home Assistant instance and show the dashboard of an app.](https://my.home-assistant.io/badges/supervisor_app.svg)](https://my.home-assistant.io/redirect/supervisor_app/?app=5c53de3b_esphome&repository_url=https%3A%2F%2Fgithub.com%2Fesphome%2Fhome-assistant-addon)

Your H-1 is now running a fresh set of firmware.
