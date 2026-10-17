---
title: Re-flash the PLT-1B factory firmware
description: "Re-flash an unresponsive PLT-1B with its factory firmware using the Apollo web installer, then set it up again in Homey."
---
# Re-flash the PLT-1B factory firmware

If your PLT-1B becomes unresponsive and you've tried the other troubleshooting steps, re-flash its factory firmware. The Apollo web installer does this from your browser while the PLT-1B is plugged into your computer by USB.

!!! note "Before you start"

    - Use Chrome, Edge, or another Chromium-based browser.
    - If your PLT-1B has already been added to Homey, <a href="https://wiki.apolloautomation.com/homey/products/general/troubleshooting/removing-device-from-homey/" target="_blank" rel="noreferrer nofollow noopener">remove it from Homey</a> before you continue.

!!! warning "Remove the battery"

    The re-flash doesn't work properly while the battery is still supplying power to the PLT-1B. If you run into issues during these steps, remove the battery.

Follow these steps to put your PLT-1B in boot mode and install the factory firmware.

1\. <a href="https://wiki.apolloautomation.com/homey/products/plt1b/troubleshooting/plt1b-boot-mode/" target="_blank" rel="noreferrer nofollow noopener">Put your PLT-1B in boot mode</a>: hold down the boot button, then plug in the USB cable.

![Tool inserted into the boot button opening on the side of the closed PLT-1B case](/assets/plt-boot-mode-pic-4.jpg)

2\. Open the <a href="https://apolloautomation.github.io/PLT-1/" target="_blank" rel="noreferrer nofollow noopener">Apollo PLT-1B Installer</a>.

3\. Under **Battery Firmware**, click the big **Connect** button.

![Apollo PLT-1 Installer page with the Battery Firmware Connect button being clicked](/assets/plt-1b-reflash-pic-1.png)

4\. Select the open COM port, then click **Connect**.

![Browser serial port prompt with the USB JTAG/serial debug unit selected and Connect highlighted](/assets/plt-1b-reflash-pic-2.png)

!!! note "No device in the list?"

    If no device shows up, click **Cancel** and install the recommended driver from the pop-up.

5\. Click **Install ApolloAutomation.PLT-1B**.

![Installer Device Dashboard with the Install ApolloAutomation.PLT-1B option highlighted](/assets/plt-1b-reflash-pic-3.png)

6\. Click **INSTALL**.

![PLT-1B install confirmation dialog with the Install button highlighted](/assets/plt-1b-reflash-pic-4.png)

7\. When you see **Installation complete!**, the install is finished. Click **Next**, then close the browser window.

![Installer showing Installation complete with the Next button](/assets/plt-1-reflash-pic-5.png)

!!! warning "Power cycle your PLT-1B before anything else"

    Your PLT-1B is still in boot mode. Power cycle it (remove its power, then power it again) so it starts in normal mode.

8\. Follow the <a href="https://wiki.apolloautomation.com/homey/products/plt1b/setup/getting-started-plt1/" target="_blank" rel="noopener">getting started guide</a> to set up your PLT-1B as a new device.

Once you finish the getting started guide, your PLT-1B is running its factory firmware again and set up as a new device.
