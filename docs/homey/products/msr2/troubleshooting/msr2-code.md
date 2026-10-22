---
title: Factory re-flash MSR-2
description: "Step by step guide for re-flashing the MSR-2 back to factory firmware."
---
# Factory re-flash MSR-2

!!! info "If your device becomes unresponsive and you've exhausted the other troubleshooting methods you can reflash the factory firmware by following the steps below."

    This factory re-flash needs to be done in Chrome, Edge, or another Chromium based browser.

If your device has already been added to Homey, please <a href="https://wiki.apolloautomation.com/homey/products/general/troubleshooting/removing-device-from-homey/" target="_blank" rel="noreferrer nofollow noopener">remove it from Homey</a> before continuing.

1\. Position the MSR-2 as shown in the image below and locate the small opening to press the boot button (the right button).

![MSR-2 case side with a tool pointing at the right opening for the boot button](/assets/msr-2-boot-button.jpg)

2\. Push and hold the boot button. While still holding the button down, plug in a USB-C cable into the USB-C port of your MSR-2 then let go of the button.

3\. Open the <a href="https://install.apolloautomation.com/#/msr-2" target="_blank" rel="noreferrer nofollow noopener">Apollo MSR-2 installer</a>.

4\. Click **Connect & Install**.

![MSR-2 page of the Apollo installer with the Connect & Install button outlined in red](/assets/installer-msr-2.png)

5\. Select the open com port then click Connect.

![Browser serial port dialog listing the USB JTAG serial debug unit with the Connect button](/assets/msr-2-reflash-pic-2.png)

6\. Click **Install ApolloAutomation.MSR-2_Factory**.

![Installer Device Dashboard menu with INSTALL MSR-2 highlighted](/assets/msr-2-reflash-pic-3.png)

7\. Click "INSTALL".

![Install msr-2 confirmation dialog with the INSTALL button highlighted](/assets/msr-2-reflash-pic-4.png)

8\. Once you see "Installation complete!" you are finished. Click Next then close out of the browser window.

![Installer showing Installation complete with the NEXT button highlighted](/assets/air-1-reflash-pic-5.png)

!!! warning "Power cycle your device before doing anything else!"

    Your device is still in boot mode and needs to be power cycled aka power removed to make it boot in a normal mode!

9\. Please <a href="https://wiki.apolloautomation.com/homey/products/general/setup/getting-started-msr2" target="_blank" rel="noreferrer nofollow noopener">proceed to the getting started guide</a> and setup your sensor as a new device!