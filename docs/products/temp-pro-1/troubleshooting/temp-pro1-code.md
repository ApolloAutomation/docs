---
title: Factory Re-Flash TEMP Pro-1
description: Step by step guide for re-flashing the TEMP Pro-1 back to factory firmware.
---
# Factory Re-Flash TEMP Pro-1

!!! info "If your device becomes unresponsive and you've exhausted the other troubleshooting methods you can reflash the factory firmware by following the below guide."

    This needs to be done in Chrome, Edge, or another Chromium based browser.

If your device has already been connected to Home Assistant please <a href="https://wiki.apolloautomation.com/products/general/troubleshooting/removing-device-from-home-assistant" target="_blank" rel="noreferrer nofollow noopener">remove it from the ESPHome integration</a> and the ESPHome Device Builder before continuing.

1\. <a href="https://wiki.apolloautomation.com/products/temp1/troubleshooting/temp1-boot-mode/" target="_blank" rel="noopener">Put your device in boot mode</a> by holding down the boot button and then plugging in the USB cable.

2\. Navigate to our installer page and click connect under Battery Firmware [Apollo TEMP-1 Installer](https://apolloautomation.github.io/TEMP-1/).

3\. Click "Connect" under the Non Battery Firmware option since you are using a TEMP-1.

![](assets/temp-1-reflash-pic-1-1.png)

3\. Select the open com port then click Connect.

![](assets/temp-1-reflash-pic-2.png)

4\. Click "Install ApolloAutomation.TEMP-1".

![](assets/temp-1-reflash-pic-3.png)

5\. Click "INSTALL".

![](assets/temp-1-reflash-pic-4.png)

6\. Once you see "Installation complete!" you are finished. Click Next then close out of the browser window.

![](assets/temp-1b-reflash-pic-7.png)

!!! warning "Power cycle your device before doing anything else!"

    Your device is still in boot mode and needs to be power cycled aka power removed to make it boot in a normal mode!

7\. Please <a href="https://wiki.apolloautomation.com/products/general/setup/getting-started-temp1/" target="_blank" rel="noopener">proceed to the getting started guide</a> and setup your sensor as a new device!