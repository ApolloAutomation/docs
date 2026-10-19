---
title: Factory re-flash TEMP-1B
description: Step by step guide for re-flashing the TEMP-1B back to factory firmware.
---
# Factory re-flash TEMP-1B

!!! info "If your device becomes unresponsive and you've exhausted the other troubleshooting methods you can reflash the factory firmware by following the below guide."

    This needs to be done in Chrome, Edge, or another Chromium based browser.

If your device has already been connected to Home Assistant please <a href="https://wiki.apolloautomation.com/products/general/troubleshooting/removing-device-from-home-assistant" target="_blank" rel="noreferrer nofollow noopener">remove it from the ESPHome integration</a> and the ESPHome Device Builder before continuing.

Follow these steps to put your device in boot mode and install the factory firmware.

1\. <a href="https://wiki.apolloautomation.com/products/temp1b/troubleshooting/temp1b-boot-mode/" target="_blank" rel="noopener">Put your device in boot mode</a> by holding down the boot button and then plugging in the USB cable.

2\. Navigate to the [Apollo TEMP-1 installer](https://install.apolloautomation.com/#/temp-1). The TEMP-1B uses the same page as the TEMP-1.

!!! failure "Remove the battery!"

    This will not work properly if the battery is still supplying power to the TEMP-1B. Please remove the battery if you are having issues!

3\. Choose **Battery Power** since you are using a TEMP-1B, then click **Connect & Install**.

![TEMP-1 page of the Apollo installer with the Battery Power variant and the Connect & Install button outlined in red](/assets/installer-temp-1-battery-power.png)

!!! tip "Use R2 version unless instructed to use R1 by support!"

    The Apollo installer installs the Revision 2 (R2) firmware. R2 is what all of our devices use except a very small batch of TEMP-1 and TEMP-1B boards. If support tells you your board needs Revision 1 (R1), click **Connect** under **Battery Firmware Revision 1** on the [classic TEMP-1 installer](https://apolloautomation.github.io/TEMP-1/) instead. In the next steps, the firmware option is named **Install ApolloAutomation.TEMP-1B**.

4\. Select the open com port then click Connect.

![Browser serial port dialog with the USB JTAG/serial debug unit port selected](/assets/temp-1b-reflash-pic-2-1.png)

5\. Click **Install Apollo.TEMP-1B_R2**.

![Device Dashboard dialog with the TEMP-1B firmware install option selected](/assets/temp-1b-reflash-pic-3.png)

6\. Click "INSTALL".

![TEMP-1B firmware install confirmation dialog with the cursor on Install](/assets/temp-1b-reflash-pic-4.png)

7\. Once you see "Installation complete!" you are finished. Click Next then close out of the browser window.

![Installation complete! message with the Next button](/assets/temp-1b-reflash-pic-7.png)

!!! warning "Power cycle your device before doing anything else!"

    Your device is still in boot mode and needs to be power cycled aka power removed to make it boot in a normal mode!

8\. Please <a href="https://wiki.apolloautomation.com/products/general/setup/getting-started/" target="_blank" rel="noopener">proceed to the getting started guide</a> and set up your sensor as a new device!