---
title: Factory re-flash MTR-1
description: Step by step guide for re-flashing the MTR-1 back to factory firmware.
---
# Factory re-flash MTR-1

!!! info "If your device becomes unresponsive and you've exhausted the other troubleshooting methods you can reflash the factory firmware by following the steps below."

    This factory re-flash needs to be done in Chrome, Edge, or another Chromium based browser.

If your device has already been connected to Home Assistant please <a href="https://wiki.apolloautomation.com/products/general/troubleshooting/removing-device-from-home-assistant" target="_blank" rel="noreferrer nofollow noopener">remove it from the ESPHome integration</a> and the ESPHome Device Builder before continuing.

Follow these steps to put your device in boot mode and install the factory firmware.

1\. Position the MTR-1 as shown in the image below and locate the small opening to press the boot button (the right button).

![Tool pointing to the MTR-1 boot button opening, the right of the two small slots](/assets/mtr-1-boot-button.jpg)

2\. Push and hold the boot button. While still holding the button down, plug in a USB-C cable into the USB-C port of your MTR-1 then let go of the button.

3\. Open the <a href="https://install.apolloautomation.com/#/mtr-1" target="_blank" rel="noreferrer nofollow noopener">Apollo MTR-1 installer</a>.

4\. Click **Connect & Install**.

![MTR-1 page of the Apollo installer with the Connect & Install button outlined in red](/assets/installer-mtr-1.png)

5\. Select the open com port then click Connect.

![Browser serial port prompt with the USB JTAG/serial debug unit selected and Connect clicked](/assets/mtr-1-reflash-pic-2.png)

6\. Click **Install ApolloAutomation.MTR-1**.

![Device Dashboard menu with the Install MTR-1 option selected](/assets/mtr-1-reflash-pic-3.png)

7\. Click "INSTALL".

![Install MTR-1 confirmation dialog with the Install button selected](/assets/mtr-1-reflash-pic-4.png)

8\. Once you see "Installation complete!" you are finished. Click Next then close out of the browser window.

![Installation complete message with the Next button outlined in red](/assets/air-1-reflash-pic-5.png)

!!! warning "Power cycle your device before doing anything else!"

    Your device is still in boot mode and needs to be power cycled aka power removed to make it boot in a normal mode!

9\. Please <a href="https://wiki.apolloautomation.com/products/general/setup/getting-started-mtr1/" target="_blank" rel="noreferrer nofollow noopener">proceed to the getting started guide</a> and set up your sensor as a new device!