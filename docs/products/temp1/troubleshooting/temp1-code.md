---
title: Factory re-flash TEMP-1
description: Step-by-step guide to re-flashing the TEMP-1 back to its factory firmware from Chrome, Edge, or another Chromium-based browser.
---
# Factory re-flash TEMP-1

If your Apollo TEMP-1 becomes unresponsive and you've exhausted the other troubleshooting methods, you can reflash the factory firmware by following this guide.

!!! note "Before you start"

    - Use Chrome, Edge, or another Chromium-based browser. The installer needs one of them.
    - If your TEMP-1 has already been connected to Home Assistant, <a href="https://wiki.apolloautomation.com/products/general/troubleshooting/removing-device-from-home-assistant" target="_blank" rel="noreferrer nofollow noopener">remove it from the ESPHome integration</a> and the ESPHome Device Builder before continuing.

Follow these steps to put your TEMP-1 in boot mode, flash the factory firmware from the installer page, and set it up again.

1\. <a href="https://wiki.apolloautomation.com/products/temp1/troubleshooting/temp1-boot-mode/" target="_blank" rel="noopener">Put your TEMP-1 in boot mode</a>: hold down the boot button, then plug in the USB cable.

2\. Open the [Apollo TEMP-1 Installer](https://apolloautomation.github.io/TEMP-1/) page.

3\. Under the **Non Battery Firmware** option, click **Connect** for Revision 2 (R2). Non Battery Firmware is the right choice because you're using a TEMP-1.

![Apollo TEMP-1 Installer page with the Non Battery Firmware Revision 2 Connect button clicked](/assets/temp-1-reflash-pic-1-1.png)

!!! tip "Use R2 unless support tells you to use R1"

    R2 is what all of our devices use, except a very small batch of TEMP-1 and TEMP-1B boards. Support will tell you if yours needs R1.

4\. In the browser's serial port pop-up, select the open COM port (**USB JTAG/serial debug unit** in the screenshot below), then click **Connect**.

![Browser serial port dialog with the USB JTAG/serial debug unit port selected and Connect clicked](/assets/temp-1-reflash-pic-2.png)

5\. Click **Install ApolloAutomation.TEMP-1**.

![Device Dashboard dialog with Install ApolloAutomation.TEMP-1 highlighted](/assets/temp-1-reflash-pic-3.png)

6\. Click **INSTALL**.

![Install ApolloAutomation.TEMP-1 confirmation dialog with the Install button highlighted](/assets/temp-1-reflash-pic-4.png)

7\. When the installer shows **Installation complete!**, the flash is finished. Click **Next**, then close the browser window.

![Installer dialog showing Installation complete! with a Next button](/assets/temp-1b-reflash-pic-7.png)

!!! warning "Power cycle your TEMP-1 before doing anything else"

    Your TEMP-1 is still in boot mode. Remove its power by unplugging the USB cable, then plug it back in so it starts in normal mode.

8\. <a href="https://wiki.apolloautomation.com/products/general/setup/getting-started-temp1/" target="_blank" rel="noopener">Go to the getting started guide</a> and set up your TEMP-1 as a new device.

Once it's set up, your TEMP-1 is back on its factory firmware and ready to use.
