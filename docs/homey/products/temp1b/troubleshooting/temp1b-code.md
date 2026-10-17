---
title: Factory re-flash TEMP-1B
description: "Step by step guide for re-flashing the TEMP-1B back to factory firmware."
---
# Factory re-flash TEMP-1B

!!! info "If your device becomes unresponsive and you've exhausted the other troubleshooting methods you can reflash the factory firmware by following the below guide."

    This needs to be done in Chrome, Edge, or another Chromium based browser.

If your device has already been added to Homey, please <a href="https://wiki.apolloautomation.com/homey/products/general/troubleshooting/removing-device-from-homey/" target="_blank" rel="noreferrer nofollow noopener">remove it from Homey</a> before continuing.

1\. <a href="https://wiki.apolloautomation.com/homey/products/temp1b/troubleshooting/temp1b-boot-mode/" target="_blank" rel="noopener">Put your device in boot mode</a> by holding down the boot button and then plugging in the USB cable.

2\. Navigate to our installer page and click connect under Battery Firmware [Apollo TEMP-1 Installer](https://apolloautomation.github.io/TEMP-1/)

!!! failure "Remove the battery!"

    This will not work properly if the battery is still supplying power to the TEMP-1B. Please remove the battery if you are having issues!

3\. Select the open com port then click Connect.

![Browser serial port dialog with the USB JTAG/serial debug unit port selected and the Connect button](/assets/temp-1b-reflash-pic-2-1.png)

4\. Click "Install ApolloAutomation.TEMP-1B".

![Device Dashboard dialog with Install ApolloAutomation.TEMP-1B selected](/assets/temp-1b-reflash-pic-3.png)

5\. Click "INSTALL".

![Install ApolloAutomation.TEMP-1B confirmation dialog with the cursor on the Install button](/assets/temp-1b-reflash-pic-4.png)

6\. Once you see "Installation complete!" you are finished. Click Next then close out of the browser window.

![Web installer dialog showing Installation complete after flashing the TEMP-1B, with the Next button](/assets/temp-1b-reflash-pic-7.png)

!!! warning "Power cycle your device before doing anything else!"

    Your device is still in boot mode and needs to be power cycled aka power removed to make it boot in a normal mode!

7\. Please <a href="https://wiki.apolloautomation.com/homey/products/general/setup/getting-started/" target="_blank" rel="noopener">proceed to the getting started guide</a> and set up your sensor as a new device!