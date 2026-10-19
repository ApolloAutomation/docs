---
title: Factory re-flash PLT-1B
description: Re-flash your PLT-1B with its factory firmware from a Chromium-based browser when the device stops responding.
---
# Factory re-flash PLT-1B

If your Apollo PLT-1B becomes unresponsive and you've exhausted the other troubleshooting methods, you can re-flash the factory firmware. You'll put the PLT-1B in boot mode, flash it from the Apollo installer in your browser, and then set it up as a new device.

!!! note "Before you start"

    * Do the re-flash in Chrome, Edge, or another Chromium-based browser.
    * If your device has already been connected to Home Assistant, <a href="https://wiki.apolloautomation.com/products/general/troubleshooting/removing-device-from-home-assistant" target="_blank" rel="noreferrer nofollow noopener">remove it from the ESPHome integration</a> and the ESPHome Device Builder before continuing.

!!! warning "Remove the battery"

    The re-flash won't work properly if the battery is still supplying power to the PLT-1B. Remove the battery before you start, or as soon as you run into issues.

1\. <a href="https://wiki.apolloautomation.com/products/plt1b/troubleshooting/plt1b-boot-mode/" target="_blank" rel="noreferrer nofollow noopener">Put your PLT-1B in boot mode</a>: hold down the boot button, then plug in the USB cable.

![Closed PLT-1B case with tweezers inserted into the boot button opening on the side](/assets/plt-boot-mode-pic-4.jpg)

2\. Open the <a href="https://install.apolloautomation.com/#/plt-1" target="_blank" rel="noreferrer nofollow noopener">Apollo PLT-1 installer</a>. The PLT-1B uses the same page as the PLT-1.

3\. Choose **Battery Power**, then click **Connect & Install**.

![PLT-1 page of the Apollo installer with the Battery Power variant and the Connect & Install button outlined in red](/assets/installer-plt-1-battery-power.png)

4\. In the browser pop-up, select the open COM port (the PLT-1B's serial port, shown as USB JTAG/serial debug unit in the example below), then click **Connect**.

![Browser serial port prompt with USB JTAG/serial debug unit selected and Connect highlighted](/assets/plt-1b-reflash-pic-2.png)

5\. Click **Install ApolloAutomation.PLT-1B**.

![Device Dashboard menu with Install ApolloAutomation.PLT-1B highlighted](/assets/plt-1b-reflash-pic-3.png)

6\. Click **INSTALL**.

![Install ApolloAutomation.PLT-1B confirmation dialog with the Install button highlighted](/assets/plt-1b-reflash-pic-4.png)

7\. When you see **Installation complete!**, you're finished. Click **Next**, then close the browser window.

![Installer dialog showing Installation complete! with a Next button](/assets/plt-1-reflash-pic-5.png)

Your PLT-1B now has the factory firmware again.

!!! warning "Power cycle your device before doing anything else"

    Your PLT-1B is still in boot mode. Remove its power, then power it back on so it starts in normal mode.

8\. <a href="https://wiki.apolloautomation.com/products/general/setup/getting-started-plt1/" target="_blank" rel="noopener">Follow the getting started guide</a> to set up your sensor as a new device.
