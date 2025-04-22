---
title: Factory Re-Flash AIR-1
description: Step by step guide for re-flashing the AIR-1 back to factory firmware.
---
# Factory Re-Flash AIR-1

!!! info "If your device becomes unresponsive and you've exhausted the other troubleshooting methods you can reflash the factory firmware by following the steps below."

    This factory re-flash needs to be done in Chrome, Edge, or another Chromium based browser.

If your device has already been connected to Home Assistant please <a href="https://wiki.apolloautomation.com/products/general/troubleshooting/removing-device-from-home-assistant" target="_blank" rel="noreferrer nofollow noopener">remove it from the ESPHome integration</a> and the ESPHome Device Builder before continuing.

1\. <a href="https://wiki.apolloautomation.com/products/air1/troubleshooting/air1-boot-mode/" target="_blank" rel="noreferrer nofollow noopener">Put your device in boot mode</a> by holding down the boot button and then plugging in the USB cable. 1. Position the AIR-1 so that the USB-C port is facing you. On the left side of the USB-C port, locate a small opening to press the boot button (the right button).

![](assets/air-1-boot-button.jpg)

2\. Navigate to our installer page and click connect under Battery Firmware <a href="https://apolloautomation.github.io/AIR-1/" target="_blank" rel="noreferrer nofollow noopener">Apollo AIR-1 Installer</a>.

3\. Click the big "Connect" button.

![](assets/air-1-reflash-pic-1.png)

4\. Select the open com port then click Connect.

![](assets/air-1-reflash-pic-2-1.png)

5\. Click "Install ApolloAutomation.AIR-1".

![](assets/air-1-reflash-pic-3.png)

6\. Click "INSTALL".

![](assets/air-1-reflash-pic-4.png)

7\. Once you see "Installation complete!" you are finished. Click Next then close out of the browser window.

![](assets/air-1-reflash-pic-5.png)

!!! warning "Power cycle your device before doing anything else!"

    Your device is still in boot mode and needs to be power cycled aka power removed to make it boot in a normal mode!

8\. Please <a href="https://wiki.apolloautomation.com/products/general/setup/getting-started-air1/" target="_blank" rel="noreferrer nofollow noopener">proceed to the getting started guide</a> and setup your sensor as a new device!