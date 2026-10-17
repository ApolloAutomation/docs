---
title: Factory re-flash TEMP Pro-1
description: Step-by-step guide to re-flashing the TEMP Pro-1 back to its factory firmware from Chrome, Edge, or another Chromium-based browser.
---
# Factory re-flash TEMP Pro-1

If your Apollo TEMP Pro-1 becomes unresponsive and you've exhausted the other troubleshooting methods, you can reflash the factory firmware by following this guide.

!!! note "Before you start"

    - Use Chrome, Edge, or another Chromium-based browser. The installer needs one of them.
    - If your TEMP Pro-1 has already been connected to Home Assistant, <a href="https://wiki.apolloautomation.com/products/general/troubleshooting/removing-device-from-home-assistant" target="_blank" rel="noreferrer nofollow noopener">remove it from the ESPHome integration</a> and the ESPHome Device Builder before continuing.

Follow these steps to put your TEMP Pro-1 in boot mode, flash the factory firmware from the installer page, and set it up again.

1\. <a href="https://wiki.apolloautomation.com/products/temppro1/troubleshooting/temp-pro1-boot-mode/" target="_blank" rel="noopener">Put your TEMP Pro-1 in boot mode</a>: hold down the boot button, then plug in the USB cable.

2\. Open the [Apollo TEMP Pro-1 Installer](https://apolloautomation.github.io/TEMP_PRO-1/) page.

3\. Pick the firmware that matches how your TEMP Pro-1 connects:

* **Wi-Fi:** click **Connect** under **Wifi Firmware**.
* **Ethernet (PoE):** click **Connect** under **Ethernet Firmware**.

4\. In the browser's serial port pop-up, select the open COM port (**USB JTAG/serial debug unit** in the screenshot below), then click **Connect**.

![Browser serial port dialog with the USB JTAG/serial debug unit port selected, cursor on Connect](/assets/temp-1-reflash-pic-2.png)

5\. Click **Install ApolloAutomation.TEMP_PRO-1-W**. If you picked Ethernet Firmware, click **Install ApolloAutomation.TEMP_PRO-1-ETH** instead.

6\. Click **INSTALL**.

7\. When the installer shows **Installation complete!**, the flash is finished. Click **Next**, then close the browser window.

![Installation complete! message with the Next button](/assets/temp-1b-reflash-pic-7.png)

!!! warning "Power cycle your TEMP Pro-1 before doing anything else"

    Your TEMP Pro-1 is still in boot mode. Remove all power from it, then reconnect the power so it starts in normal mode.

8\. <a href="https://wiki.apolloautomation.com/products/general/setup/getting-started-temp1/" target="_blank" rel="noopener">Go to the getting started guide</a> and set up your TEMP Pro-1 as a new device.

Once it's set up, your TEMP Pro-1 is back on its factory firmware and ready to use.
