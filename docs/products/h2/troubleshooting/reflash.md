---
title: Factory re-flash H-2
description: Step by step guide for re-flashing the H-2 back to factory firmware.
---
# Reflashing the H-2

!!! info "If your device becomes unresponsive and you've exhausted the other troubleshooting methods you can reflash the factory firmware by following the steps below."

    This factory re-flash needs to be done in Chrome, Edge, or another Chromium based browser.

1\. Disconnect your H-2 from power. With the device facing you, locate the boot button. It’s the small black button on the right.

2\. Plug in a USB cable that supports power and data into your computer.

3\. Push and hold the boot button (the right button). While still holding the button down, plug in a USB-C cable into the USB-C port of your H-2 then let go of the button.

![Holding the boot button on the H-2 while plugging a USB-C cable into it](/assets/h-2-boot-mode-method-1-boot-button.webp)

4\. Open the Apollo H-2 installer with the button below, using a Chromium-based browser such as Chrome or Edge. Under **Choose your firmware**, click **Smart (Wi-Fi)** to join your Wi-Fi and Home Assistant, or **Basic (No Wi-Fi)** to go back to the firmware the ornament ships with. Then click **Connect & Install**, select the open com port, and click **Connect**.

[Apollo H-2 installer](https://install.apolloautomation.com/#/h-2){   .md-button .md-button--primary }

![H-2 page of the Apollo installer with the Smart (Wi-Fi) variant and the Connect & Install button outlined in red](/assets/installer-h-2-smart.png)

5\. Click **Install ApolloAutomation.H-2** (Smart) or **Install ApolloAutomation.H-2D** (Basic), then click **Install** again.

![Clicking Install ApolloAutomation.H-2, confirming Install, and the installer erasing the device](/assets/h-2-reflash-install.gif)

6\. Once you see "Installation complete!" you are finished. Click Next then close out of the browser window.

![Web installer dialog showing Installation complete with a Next button](/assets/pump-1-reflash-install-complete.png)

!!! warning "Power cycle your device before doing anything else!"

    Your device is still in boot mode and needs to be power cycled aka power removed to make it boot in a normal mode!

[Head to the Getting Started article to set up your H-2 as a new device!](https://wiki.apolloautomation.com/products/h2/setup/getting-started/){                .md-button .md-button--primary }