---
title: Factory re-flash MSR-2
description: Step by step guide for re-flashing the MSR-2 back to factory firmware.
---
# Factory re-flash MSR-2

!!! info "If your device becomes unresponsive and you've exhausted the other troubleshooting methods you can reflash the factory firmware by following the steps below."

    This factory re-flash needs to be done in Chrome, Edge, or another Chromium based browser.

If your device has already been connected to Home Assistant please <a href="https://wiki.apolloautomation.com/products/general/troubleshooting/removing-device-from-home-assistant" target="_blank" rel="noreferrer nofollow noopener">remove it from the ESPHome integration</a> and the ESPHome Device Builder before continuing.

1\. Position the MSR-2 as shown in the image below and locate the small opening to press the boot button (the right button).

![Tool pointing to the MSR-2 boot button opening, the right of the two small slots](/assets/msr-2-boot-button.jpg)

2\. Push and hold the boot button. While still holding the button down, plug in a USB-C cable into the USB-C port of your MSR-2 then let go of the button.

3\. Navigate to our installer page and click connect under <a href="https://apolloautomation.github.io/MSR-2/" target="_blank" rel="noreferrer nofollow noopener">Apollo MSR-2 Installer</a>.

4\. Click the big "Connect" button.

![Apollo MSR-2 Installer page with the Connect button outlined in red](/assets/msr-2-reflash-pic-1.png)

5\. Select the open com port then click Connect.

![Browser serial port prompt with the USB JTAG/serial debug unit selected and Connect clicked](/assets/msr-2-reflash-pic-2.png)

6\. Click "Install MSR-2".

![Device Dashboard menu with the Install MSR-2 option selected](/assets/msr-2-reflash-pic-3.png)

7\. Click "INSTALL".

![Install MSR-2 confirmation dialog with the Install button selected](/assets/msr-2-reflash-pic-4.png)

8\. Once you see "Installation complete!" you are finished. Click Next then close out of the browser window.

![Installation complete message with the Next button outlined in red](/assets/air-1-reflash-pic-5.png)

!!! warning "Power cycle your device before doing anything else!"

    Your device is still in boot mode and needs to be power cycled aka power removed to make it boot in a normal mode!

9\. Please <a href="https://wiki.apolloautomation.com/products/general/setup/getting-started-msr2" target="_blank" rel="noreferrer nofollow noopener">proceed to the getting started guide</a> and set up your sensor as a new device!