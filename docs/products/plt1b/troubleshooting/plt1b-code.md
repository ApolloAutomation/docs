---
title: Factory Re-Flash PLT-1B
description: Step by step guide for re-flashing the PLT-1B back to factory firmware.
---
# Factory Re-Flash PLT-1B

!!! info "If your device becomes unresponsive and you've exhausted the other troubleshooting methods you can reflash the factory firmware by following the below guide."

    This needs to be done in Chrome, Edge, or another Chromium based browser.

If your device has already been connected to Home Assistant please <a href="https://wiki.apolloautomation.com/products/general/troubleshooting/removing-device-from-home-assistant" target="_blank" rel="noreferrer nofollow noopener">remove it from the ESPHome integration</a> and the ESPHome Device Builder before continuing.

1\. <a href="https://wiki.apolloautomation.com/products/plt1b/troubleshooting/plt1b-boot-mode/" target="_blank" rel="noreferrer nofollow noopener">Put your device in boot mode</a> by holding down the boot button and then plugging in the USB cable.

![Closed PLT-1B case with tweezers inserted into the boot button opening on the side](/assets/plt-boot-mode-pic-4.jpg)

2\. Navigate to our installer page and click connect under Battery Firmware <a href="https://apolloautomation.github.io/PLT-1/" target="_blank" rel="noreferrer nofollow noopener">Apollo PLT-1B Installer</a>

!!! failure "Remove the battery!"

    This will not work properly if the battery is still supplying power to the PLT-1B. Please remove the battery if you are having issues!

3\. Click the big "Connect" button.

![Apollo PLT-1 Installer with the cursor on the Battery Firmware Connect button](/assets/plt-1b-reflash-pic-1.png)

4\. Select the open com port then click Connect.

![Browser serial port prompt with USB JTAG/serial debug unit selected and Connect highlighted](/assets/plt-1b-reflash-pic-2.png)

5\. Click "Install ApolloAutomation.PLT-1B".

![Device Dashboard menu with Install ApolloAutomation.PLT-1B highlighted](/assets/plt-1b-reflash-pic-3.png)

6\. Click "INSTALL".

![Install ApolloAutomation.PLT-1B confirmation dialog with the Install button highlighted](/assets/plt-1b-reflash-pic-4.png)

7\. Once you see "Installation complete!" you are finished. Click Next then close out of the browser window.

![Installer dialog showing Installation complete! with a Next button](/assets/plt-1-reflash-pic-5.png)

!!! warning "Power cycle your device before doing anything else!"

    Your device is still in boot mode and needs to be power cycled aka power removed to make it boot in a normal mode!

8\. Please <a href="https://wiki.apolloautomation.com/products/general/setup/getting-started-plt1/" target="_blank" rel="noopener">proceed to the getting started guide</a> and set up your sensor as a new device!