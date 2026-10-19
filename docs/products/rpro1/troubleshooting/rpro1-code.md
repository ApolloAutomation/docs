---
title: Factory re-flash R PRO-1
description: Re-flash your R PRO-1 with its factory firmware from a Chromium-based browser when the device stops responding.
---
# Factory re-flash R PRO-1

If your Apollo R PRO-1 becomes unresponsive and you've exhausted the other troubleshooting methods, you can re-flash the factory firmware by following the steps below. You'll put the R PRO-1 in boot mode, flash it from the Apollo installer in your browser, and then set it up as a new device.

!!! note "Before you start"

    * Do this factory re-flash in Chrome, Edge, or another Chromium-based browser.
    * If your device has already been connected to Home Assistant, <a href="https://wiki.apolloautomation.com/products/general/troubleshooting/removing-device-from-home-assistant" target="_blank" rel="noreferrer nofollow noopener">remove it from the ESPHome integration</a> and the ESPHome Device Builder before continuing.

1\. Put your R PRO-1 in boot mode. The boot button is on the bottom right of the board, so first unplug the R PRO-1, remove the back, and take the board out of the case. The <a href="https://wiki.apolloautomation.com/products/rpro1/troubleshooting/rpro1-boot-mode/" rel="noreferrer nofollow">boot mode guide</a> shows each part.

![Tool pointing to the SW6 boot button at the bottom right of the R PRO-1 PCB](/assets/r-pro-1-boot-button.jpg)

With the board out of the case:

- Push and hold the boot button.
- While still holding the button down, plug a USB-C cable into the USB-C port of your R PRO-1.
- Let go of the button.

2\. Open the <a href="https://install.apolloautomation.com/#/r-pro-1" target="_blank" rel="noreferrer nofollow noopener">Apollo R PRO-1 installer</a>.

3\. Under **Choose your firmware**, pick **WiFi** if your R PRO-1 connects over Wi-Fi, or **Ethernet** if it connects over PoE or Ethernet. Then click **Connect & Install**.

![R PRO-1 page of the Apollo installer with the WiFi variant and the Connect & Install button outlined in red](/assets/installer-r-pro-1-wifi.png)

4\. In the browser pop-up, select the open COM port (the R PRO-1's serial port, shown as USB JTAG/serial debug unit in the example below), then click **Connect**.

![Browser serial port prompt with the USB JTAG serial debug unit COM port and Connect button](/assets/r-pro-1-reflash-connect-comp-port.png)

5\. Click **Install ApolloAutomation.R-PRO-1-W** if you chose **WiFi**, or **Install ApolloAutomation.R-PRO-1-ETH** if you chose **Ethernet**.

![Installer Device Dashboard with the install R PRO-1 Ethernet firmware option highlighted](/assets/r-pro-1-reflash-click-install.png)

6\. Click **INSTALL**.

![Install confirmation dialog for the R PRO-1 Ethernet firmware with the INSTALL button](/assets/r-pro-1-reflash-click-install-to-install.png)

7\. When you see **Installation complete!**, you're finished. Click **Next**, then close the browser window.

![Installer showing Installation complete with the NEXT button highlighted](/assets/r-pro-1-reflash-installation-complete.png)

Your R PRO-1 now has the factory firmware again.

!!! warning "Power cycle your device before doing anything else"

    Your R PRO-1 is still in boot mode. Unplug it, then plug it back in so it starts in normal mode.

8\. <a href="https://wiki.apolloautomation.com/products/general/setup/getting-started-rpro1" rel="noreferrer nofollow">Follow the getting started guide</a> to set up your R PRO-1 as a new device.
