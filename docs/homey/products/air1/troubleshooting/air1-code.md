---
title: Factory Re-Flash AIR-1
description: "Re-flash your AIR-1 back to its factory firmware from a Chromium-based browser, then set it up in Homey again."
---
# Factory re-flash AIR-1

If your Apollo AIR-1 becomes unresponsive and you've exhausted the other troubleshooting methods, you can re-flash the factory firmware. This guide walks you through it in your browser, step by step.

!!! note "Before you start"

    - Use Chrome, Edge, or another Chromium-based browser. The factory re-flash needs one.
    - If your AIR-1 has already been added to Homey, <a href="https://wiki.apolloautomation.com/homey/products/general/troubleshooting/removing-device-from-homey/" target="_blank" rel="noreferrer nofollow noopener">remove it from Homey</a> before you continue.

1\. <a href="https://wiki.apolloautomation.com/homey/products/air1/troubleshooting/air1-boot-mode/" target="_blank" rel="noreferrer nofollow noopener">Put your AIR-1 in boot mode</a>: hold down the boot button, then plug in the USB cable.

![AIR-1 case with a tool pointing at the boot button left of the USB-C port](/assets/air-1-boot-button.jpg)

2\. Go to the <a href="https://apolloautomation.github.io/AIR-1/" target="_blank" rel="noreferrer nofollow noopener">Apollo AIR-1 Installer</a> page.

3\. Click the big **Connect** button.

![Apollo AIR-1 Installer web page with the Connect button highlighted](/assets/air-1-reflash-pic-1.png)

4\. Select the open COM port, then click **Connect**.

![Browser serial port prompt with the USB JTAG serial debug unit selected and Connect](/assets/air-1-reflash-pic-2-1.png)

5\. Click **Install ApolloAutomation.AIR-1**.

![AIR-1 installer Device Dashboard with Install AIR-1 highlighted](/assets/air-1-reflash-pic-3.png)

6\. Click **INSTALL**.

![AIR-1 installer confirmation dialog with the Install button highlighted](/assets/air-1-reflash-pic-4.png)

7\. When you see **Installation complete!**, the install is finished. Click **Next**, then close the browser window.

![AIR-1 installer showing Installation complete with the Next button highlighted](/assets/air-1-reflash-pic-5.png)

Your AIR-1 is back on its factory firmware.

!!! warning "Power cycle your AIR-1 before you do anything else"

    Your AIR-1 is still in boot mode. Remove its power, then power it back on so it boots in normal mode.

!!! success "Next step: set up your AIR-1 as a new device"

    With the factory firmware on and the AIR-1 power cycled, follow the getting started guide to connect it to Wi-Fi and add it to Homey as a new device.

    <a href="https://wiki.apolloautomation.com/homey/products/general/setup/getting-started-air1/" target="_blank" rel="noreferrer nofollow noopener" class="md-button md-button--primary">Proceed to the getting started guide</a>
