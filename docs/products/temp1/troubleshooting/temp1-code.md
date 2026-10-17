---
title: Factory Re-Flash TEMP-1
description: Step by step guide for re-flashing the TEMP-1 back to factory firmware.
---
# Factory Re-Flash TEMP-1

!!! info "If your device becomes unresponsive and you've exhausted the other troubleshooting methods you can reflash the factory firmware by following the below guide."

    This needs to be done in Chrome, Edge, or another Chromium based browser.

If your device has already been connected to Home Assistant please <a href="https://wiki.apolloautomation.com/products/general/troubleshooting/removing-device-from-home-assistant" target="_blank" rel="noreferrer nofollow noopener">remove it from the ESPHome integration</a> and the ESPHome Device Builder before continuing.

1\. <a href="https://wiki.apolloautomation.com/products/temp1/troubleshooting/temp1-boot-mode/" target="_blank" rel="noopener">Put your device in boot mode</a> by holding down the boot button and then plugging in the USB cable.

2\. Navigate to our [Apollo TEMP-1 Installer](https://apolloautomation.github.io/TEMP-1/) page.

3\. Click "Connect" under the Non Battery Firmware option since you are using a TEMP-1.

!!! tip "Use R2 version unless instructed to use R1 by support!"

    R2 is what all of our devices use except a very small batch of TEMP-1 and TEMP-1B

![Apollo TEMP-1 Installer page with the Non Battery Firmware Revision 2 Connect button clicked](/assets/temp-1-reflash-pic-1-1.png)

4\. Select the open com port then click Connect.

![Browser serial port dialog with the USB JTAG/serial debug unit port selected and Connect clicked](/assets/temp-1-reflash-pic-2.png)

5\. Click "Install ApolloAutomation.TEMP-1".

![Device Dashboard dialog with Install ApolloAutomation.TEMP-1 highlighted](/assets/temp-1-reflash-pic-3.png)

6\. Click "INSTALL".

![Install ApolloAutomation.TEMP-1 confirmation dialog with the Install button highlighted](/assets/temp-1-reflash-pic-4.png)

7\. Once you see "Installation complete!" you are finished. Click Next then close out of the browser window.

![Installer dialog showing Installation complete! with a Next button](/assets/temp-1b-reflash-pic-7.png)

!!! warning "Power cycle your device before doing anything else!"

    Your device is still in boot mode and needs to be power cycled aka power removed to make it boot in a normal mode!

8\. Please <a href="https://wiki.apolloautomation.com/products/general/setup/getting-started-temp1/" target="_blank" rel="noopener">proceed to the getting started guide</a> and set up your sensor as a new device!