---
title: Factory Re-Flash PLT-1
description: "Step by step guide for re-flashing the PLT-1 back to factory firmware."
---
# Factory Re-Flash PLT-1

!!! info "If your device becomes unresponsive and you've exhausted the other troubleshooting methods you can reflash the factory firmware by following the below guide."

    This needs to be done in Chrome, Edge, or another Chromium based browser.

If your device has already been added to Homey, please <a href="https://wiki.apolloautomation.com/homey/products/general/troubleshooting/removing-device-from-homey/" target="_blank" rel="noreferrer nofollow noopener">remove it from Homey</a> before continuing.

Follow these steps to put your device in boot mode and install the factory firmware.

1\. <a href="https://wiki.apolloautomation.com/homey/products/plt1/troubleshooting/plt1-boot-mode/" target="_blank" rel="noopener">Put your device in boot mode</a> by holding down the boot button and then plugging in the USB cable.

![Side of the PLT-1 with the boot button opening circled](/assets/screenshot-2024-10-23-at-12-32-55-pm.png)

2\. Navigate to our installer page and click connect under Non Battery Firmware <a href="https://apolloautomation.github.io/PLT-1/" target="_blank" rel="noreferrer nofollow noopener">Apollo PLT-1 Installer</a>

3\. Click the big "Connect" button.

![Apollo PLT-1 Installer page with the Non Battery Firmware Connect button highlighted](/assets/plt-1-reflash-pic-1-1.png)

4\. Select the open com port then click Connect.

![Browser serial port prompt with the USB JTAG/serial debug unit selected and Connect clicked](/assets/plt-1-reflash-pic-2-1.png)

5\. Click "Install ApolloAutomation.PLT-1".

![Installer Device Dashboard with the Install ApolloAutomation.PLT-1 option highlighted](/assets/plt-1-reflash-pic-3.png)

6\. Click "INSTALL".

![PLT-1 install confirmation dialog with the Install button highlighted](/assets/plt-1-reflash-pic-4.png)

7\. Once you see "Installation complete!" you are finished. Click Next then close out of the browser window.

![Installer showing Installation complete with the Next button](/assets/plt-1-reflash-pic-5.png)

!!! warning "Power cycle your device before doing anything else!"

    Your device is still in boot mode and needs to be power cycled aka power removed to make it boot in a normal mode!

8\. Please <a href="https://wiki.apolloautomation.com/homey/products/general/setup/getting-started-plt1/" target="_blank" rel="noopener">proceed to the getting started guide</a> and set up your sensor as a new device!