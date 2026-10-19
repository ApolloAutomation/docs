---
title: Factory re-flash MSR-1
description: "Reflash the MSR-1 back to factory firmware from a Chromium based browser when it stops responding."
---
# Factory re-flash MSR-1

!!! info "If your device becomes unresponsive and you've exhausted the other troubleshooting methods you can reflash the factory firmware by following the steps below."

    This factory re-flash needs to be done in Chrome, Edge, or another Chromium based browser.

If your device has already been connected to Home Assistant please <a href="https://wiki.apolloautomation.com/products/general/troubleshooting/removing-device-from-home-assistant" target="_blank" rel="noreferrer nofollow noopener">remove it from the ESPHome integration</a> and the ESPHome Device Builder before continuing.

1\. Position the MSR-1 as shown in the image below and locate the small opening to <a href="https://wiki.apolloautomation.com/products/msr1/troubleshooting/msr1-boot-mode/" target="_blank" rel="noreferrer nofollow noopener">press the boot button (the left button).</a>

![MSR-1 case with the boot button opening highlighted in red among the top vents](/assets/msr-1-top-shot-boot-button.jpg)

2\. Push and hold the boot button. While still holding the button down, plug in a USB-C cable into the USB-C port of your MSR-1 then let go of the button.

3\. Open the <a href="https://install.apolloautomation.com/#/msr-1" target="_blank" rel="noreferrer nofollow noopener">Apollo MSR-1 installer</a>.

4\. Click **Connect & Install**.

![MSR-1 page of the Apollo installer with the Connect & Install button outlined in red](/assets/installer-msr-1.png)

5\. Select the open com port then click Connect.

![Browser serial port prompt with the USB JTAG/serial debug unit selected and the Connect button](/assets/msr-1-reflash-pic-2.png)

6\. Click **Install ApolloAutomation.MSR-1_Factory**.

![Device Dashboard menu with Install MSR-1 highlighted](/assets/msr-1-reflash-pic-3.png)

7\. Click "INSTALL".

![Install msr-1 confirmation dialog warning that data will be erased, with the Install button](/assets/msr-1-reflash-pic-4.png)

8\. Once you see "Installation complete!" you are finished. Click Next then close out of the browser window.

![Installation complete message with the Next button highlighted](/assets/air-1-reflash-pic-5.png)

!!! warning "Power cycle your device before doing anything else!"

    Your device is still in boot mode and needs to be power cycled aka power removed to make it boot in a normal mode!

9\. Please <a href="https://wiki.apolloautomation.com/products/general/setup/getting-started-msr1/" target="_blank" rel="noreferrer nofollow noopener">proceed to the getting started guide</a> and set up your sensor as a new device!