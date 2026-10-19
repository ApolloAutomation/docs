---
title: Factory re-flash AIR-1
description: Re-flash your AIR-1 with its factory firmware over USB when it becomes unresponsive.
---
# Factory re-flash AIR-1

If your Apollo AIR-1 becomes unresponsive and you've exhausted the other troubleshooting methods, you can re-flash the factory firmware by following the steps below.

!!! note "Before you start"

    - Do the factory re-flash in Chrome, Edge, or another Chromium-based browser.
    - If your AIR-1 has already been connected to Home Assistant, <a href="https://wiki.apolloautomation.com/products/general/troubleshooting/removing-device-from-home-assistant" target="_blank" rel="noreferrer nofollow noopener">remove it from the ESPHome integration</a> and the ESPHome Device Builder before continuing.

## Re-flash the factory firmware

Follow these steps to put the factory firmware back on your AIR-1 from the Apollo AIR-1 installer.

1\. <a href="https://wiki.apolloautomation.com/products/air1/troubleshooting/air1-boot-mode/" target="_blank" rel="noreferrer nofollow noopener">Put your AIR-1 in boot mode</a>: hold down the boot button (the right of the two buttons beside the USB-C port), then plug in the USB cable. Let go of the button once the cable is in.

![Tool pointing to the AIR-1 boot button, the right of two buttons beside the USB-C port](/assets/air-1-boot-button.jpg)

2\. Open the <a href="https://install.apolloautomation.com/#/air-1" target="_blank" rel="noreferrer nofollow noopener">Apollo AIR-1 installer</a>.

3\. Click **Connect & Install** on the installer page.

![AIR-1 page of the Apollo installer with the Connect & Install button outlined in red](/assets/installer-air-1.png)

4\. In the browser pop-up, select your AIR-1's open serial (COM) port, then click **Connect**. In the screenshot below, it's listed as USB JTAG/serial debug unit.

![Browser serial port dialog with the USB JTAG/serial debug unit port and the Connect button](/assets/air-1-reflash-pic-2-1.png)

5\. Click **Install ApolloAutomation.AIR-1**.

![Installer Device Dashboard with the Install AIR-1 option highlighted](/assets/air-1-reflash-pic-3.png)

6\. Click **INSTALL**.

![Install AIR-1 confirmation dialog with the Install button highlighted](/assets/air-1-reflash-pic-4.png)

7\. When you see **Installation complete!**, the factory firmware is installed. Click **Next**, then close the browser window.

![Installation complete message with the Next button highlighted](/assets/air-1-reflash-pic-5.png)

!!! warning "Power cycle your AIR-1 before doing anything else"

    Your AIR-1 is still in boot mode. Power cycle it (unplug it to remove power, then plug it back in) so it boots in normal mode.

8\. <a href="https://wiki.apolloautomation.com/products/general/setup/getting-started-air1/" target="_blank" rel="noreferrer nofollow noopener">Go to the getting started guide</a> and set up your AIR-1 as a new device.
