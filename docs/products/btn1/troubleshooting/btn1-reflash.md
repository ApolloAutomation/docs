---
title: Reflashing the BTN-1.
description: Step by step guide for reflashing The BTN-1.
---
# Reflashing the BTN-1

!!! info "If your device becomes unresponsive and you've exhausted the other troubleshooting methods you can reflash the factory firmware by following the steps below."

    This factory re-flash needs to be done in Chrome, Edge, or another Chromium based browser.

1\. Plug in a USB cable that supports power and data into your computer and connect the other end to your BTN-1.

![Plugging a USB-C cable into the port on the back of the BTN-1](/assets/btn-1-plug-in-usb-c.webp)

2\. With the device facing you, locate the reset (left) and boot (right) buttons.

![Back of the BTN-1 with arrows labeling the reset button on the left and the boot button on the right](/assets/btn-1-reset-boot-buttons.png)

3\. Put your BTN-1 in boot mode. Use both buttons, in this order:

- Press and hold the **boot** button (the right button). Keep holding it.
- While you're still holding **boot**, press and release the **reset** button (the left button).
- Let go of **boot**.

!!! warning "Keep holding boot the whole time"

    Pressing **reset** by itself only restarts the BTN-1. It goes into boot mode only when **boot** is held down while you press and release **reset**.

![Animation with step captions: press and hold boot on the BTN-1, keep holding it while you tap reset, then let go of boot](/assets/btn-1-boot-mode-method-2.webp)

4\. Open the <a href="https://install.apolloautomation.com/#/btn-1" target="_blank" rel="noreferrer nofollow noopener">Apollo BTN-1 installer</a> in a Chromium-based browser such as Chrome or Edge and click **Connect & Install**. Select the open com port and click **Connect**.

![BTN-1 page of the Apollo installer with the Connect & Install button outlined in red](/assets/installer-btn-1.png)

5\. Click **Install ApolloAutomation.BTN-1**, then click **Install** again.

![Clicking Install ApolloAutomation.BTN-1 in the Device Dashboard, then Install to confirm](/assets/btn-1-reflash-install.gif)

6\. Once you see "Installation complete!" you are finished. Click Next then close out of the browser window.

![Web installer showing Installation complete with the Next button](/assets/pump-1-reflash-install-complete.png)

!!! warning "Power cycle your device before doing anything else!"

    Your device is still in boot mode and needs to be power cycled aka power removed to make it boot in a normal mode!

[Head to the Getting Started article to set up your BTN-1 as a new device!](https://wiki.apolloautomation.com/products/btn1/setup/getting-started/){          .md-button .md-button--primary }