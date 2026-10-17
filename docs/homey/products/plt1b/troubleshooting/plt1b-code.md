---
title: Factory Re-Flash PLT-1B
description: "Step by step guide for re-flashing the PLT-1B back to factory firmware."
---
# Factory Re-Flash PLT-1B

!!! info "If your device becomes unresponsive and you've exhausted the other troubleshooting methods you can reflash the factory firmware by following the below guide."

    This needs to be done in Chrome, Edge, or another Chromium based browser.

If your device has already been added to Homey, please <a href="https://wiki.apolloautomation.com/homey/products/general/troubleshooting/removing-device-from-homey/" target="_blank" rel="noreferrer nofollow noopener">remove it from Homey</a> before continuing.

1\. <a href="https://wiki.apolloautomation.com/homey/products/plt1b/troubleshooting/plt1b-boot-mode/" target="_blank" rel="noreferrer nofollow noopener">Put your device in boot mode</a> by holding down the boot button and then plugging in the USB cable.

![Tool inserted into the boot button opening on the side of the closed PLT-1B case](/assets/plt-boot-mode-pic-4.jpg)

2\. Navigate to our installer page and click connect under Battery Firmware <a href="https://apolloautomation.github.io/PLT-1/" target="_blank" rel="noreferrer nofollow noopener">Apollo PLT-1B Installer</a>

!!! failure "Remove the battery!"

    This will not work properly if the battery is still supplying power to the PLT-1B. Please remove the battery if you are having issues!

3\. Click the big "Connect" button.

![Apollo PLT-1 Installer page with the Battery Firmware Connect button being clicked](/assets/plt-1b-reflash-pic-1.png)

4\. Select the open com port then click Connect.

![Browser serial port prompt with the USB JTAG/serial debug unit selected and Connect highlighted](/assets/plt-1b-reflash-pic-2.png)

!!! note

    If no device shows, click cancel and install the recommended driver from the popup.

5\. Click "Install ApolloAutomation.PLT-1B".

![Installer Device Dashboard with the Install ApolloAutomation.PLT-1B option highlighted](/assets/plt-1b-reflash-pic-3.png)

6\. Click "INSTALL".

![PLT-1B install confirmation dialog with the Install button highlighted](/assets/plt-1b-reflash-pic-4.png)

7\. Once you see "Installation complete!" you are finished. Click Next then close out of the browser window.

![Installer showing Installation complete with the Next button](/assets/plt-1-reflash-pic-5.png)

!!! warning "Power cycle your device before doing anything else!"

    Your device is still in boot mode and needs to be power cycled aka power removed to make it boot in a normal mode!

8\. Please <a href="https://wiki.apolloautomation.com/homey/products/plt1b/setup/getting-started-plt1/" target="_blank" rel="noopener">proceed to the getting started guide</a> and set up your sensor as a new device!