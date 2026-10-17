---
title: Reflashing The PUMP-1.
description: Step by step guide for reflashing The PUMP-1.
---
# Reflashing The PUMP-1

!!! info "If your device becomes unresponsive and you've exhausted the other troubleshooting methods you can reflash the factory firmware by following the steps below."

    This factory re-flash needs to be done in Chrome, Edge, or another Chromium based browser.

1\. Disconnect your PUMP-1 from power. With the device facing you, locate the boot button. It’s the button on the right.

!!! danger "Empty the water reservoir and make sure no water is present in the tubes"

    Make sure that there is no water which is able to damage the device. This is a precautionary measure to be safe!

2\. Plug in a USB cable that supports power and data into your computer.

3\. Push and hold the boot button (the right button). While still holding the button down, plug in a USB-C cable into the USB-C port of your PUMP-1 then let go of the button.

![Holding the PUMP-1 boot button while plugging in the USB-C cable](/assets/pump-1-hold-boot-button-video.webp)

4\. Navigate to our installer page and click connect under <a href="https://apolloautomation.github.io/PUMP-1/" target="_blank" rel="noreferrer nofollow noopener">Apollo PUMP-1 Installer</a>.

![Apollo PUMP-1 Installer page with the cursor on the Connect button](/assets/pump-1-reflash-connect-button.png)

5\. Select the open com port then click Connect.

![Browser serial port prompt with USB JTAG/serial debug unit selected and the cursor on Connect](/assets/pump-1-reflash-com-port.png)

6\. Click Install PUMP-1.

![Device Dashboard menu with the cursor on Install ApolloAutomation.PUMP-1](/assets/pump-1-reflash-click-install.png)

7\. Click Install.

![Install ApolloAutomation.PUMP-1 confirmation dialog with the cursor on Install](/assets/pump-1-reflash-click-install-confirm.png)

8\. Once you see "Installation complete!" you are finished. Click Next then close out of the browser window.

![Installer dialog showing Installation complete! with a Next button](/assets/pump-1-reflash-install-complete.png)

!!! warning "Power cycle your device before doing anything else!"

    Your device is still in boot mode and needs to be power cycled aka power removed to make it boot in a normal mode!

[Head to the Getting Started article to set up your PUMP-1 as a new device!](https://wiki.apolloautomation.com/products/general/setup/getting-started-pump1/){      .md-button .md-button--primary }