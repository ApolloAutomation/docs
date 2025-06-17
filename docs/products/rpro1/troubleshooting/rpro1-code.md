---
title: Factory Re-Flash R-PRO-1
description: Step by step guide for re-flashing the R-PRO-1 back to factory firmware.
---
# Factory Re-Flash R-PRO-1

!!! info "If your device becomes unresponsive and you've exhausted the other troubleshooting methods you can reflash the factory firmware by following the steps below."

    This factory re-flash needs to be done in Chrome, Edge, or another Chromium based browser.

If your device has already been connected to Home Assistant please <a href="https://wiki.apolloautomation.com/products/general/troubleshooting/removing-device-from-home-assistant" target="_blank" rel="noreferrer nofollow noopener">remove it from the ESPHome integration</a> and the ESPHome Device Builder before continuing.

1\. Locate the boot button <a href="https://wiki.apolloautomation.com/products/rpro1/troubleshooting/rpro1-boot-mode.md" rel="noreferrer nofollow">as shown here</a>. Push and hold the boot button. While still holding the button down, plug in a USB-C cable into the USB-C port of your R-PRO-1 then let go of the button.

![](../../../assets/r-pro-1-boot-button.jpg)

3\. Navigate to our installer page and click connect under <a href="https://apolloautomation.github.io/R_PRO-1/" target="_blank" rel="noreferrer nofollow noopener">Apollo R-PRO-1 Installer</a>.

3\. Click the big "Connect" button.

![](../../../assets/r-pro-1-reflash-connect-button.png)

3\. Select the open com port then click Connect.

![](../../../assets/r-pro-1-reflash-connect-comp-port.png)

4\. Click "Install R-PRO-1".

![](../../../assets/r-pro-1-reflash-click-install.png)

5\. Click "INSTALL".

![](../../../assets/r-pro-1-reflash-click-install-to-install.png)

6\. Once you see "Installation complete!" you are finished. Click Next then close out of the browser window.

![](../../../assets/r-pro-1-reflash-installation-complete.png)

!!! warning "Power cycle your device before doing anything else!"

    Your device is still in boot mode and needs to be power cycled aka power removed to make it boot in a normal mode!

7\. Please <a href="https://wiki.apolloautomation.com/products/general/setup/getting-started-rpro1" rel="noreferrer nofollow">proceed to the getting started guide</a> and setup your sensor as a new device!