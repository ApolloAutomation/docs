---
title: Reflashing The CAST-1
description: Step by step guide for reflashing The CAST-1.
---
# Reflashing The CAST-1

!!! info "Use this to put your CAST-1 back on the latest factory firmware."

    Reflash if your device becomes unresponsive and you've exhausted the other troubleshooting methods, or to get onto the latest firmware.

1\. Plug a USB-C cable that supports power and data into your computer and connect the other end to your CAST-1.

2\. Locate the **boot** and **reset** buttons on your CAST-1. (1)
{ .annotate }

1.  Prefer to boot with a single button? Follow [Method 1 on the Boot Mode page](https://wiki.apolloautomation.com/products/cast1/troubleshooting/cast1-boot-mode/#method-1-boot-button-only) instead.

![](/assets/cast-1-boot-reset-buttons.webp)

3\. Put the CAST-1 into boot mode. Hold down the **boot** button (on the left), then press and release the **reset** button (on the right) while keeping the boot button pressed. Finally, release the boot button.

![](/assets/cast-1-boot-mode-method-2.webp)

4\. Open the <a href="https://install.apolloautomation.com/#/cast-1" target="_blank" rel="noreferrer nofollow noopener">Apollo CAST-1 Installer</a>.

5\. Click **Connect & Install**. In the browser popup, select **USB JTAG/serial debug unit** and click **Allow**. When the installer opens, click **Install** to flash the firmware, then click **Install** again to confirm.

![](/assets/cast-1-reflash-firmware.gif)

6\. Once you see "**Installation complete!**" you are finished. Click **Next** then close out of the browser window.

!!! warning "Power cycle your device before doing anything else!"

    Your device is still in boot mode and needs to be power cycled, meaning power removed, to make it boot in a normal mode!

[Head to the Getting Started article to setup your CAST-1 as a new device!](https://wiki.apolloautomation.com/products/cast1/setup/getting-started/){ .md-button .md-button--primary }
