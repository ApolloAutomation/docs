---
title: Factory re-flash LED-1
description: Step by step guide for re-flashing the LED-1 with regular WLED from your browser.
---
# Factory re-flash LED-1

Follow these steps to flash your Apollo LED-1 with regular WLED from the official WLED web installer. Use Chrome or Edge, since the installer needs a browser that can talk to the USB serial port.

1\. Plug in a USB cable that supports power and data into your computer.

2\. Push and hold the boot button (the right button). While still holding the button down, plug in a USB-C cable into the USB-C port of your LED-1 then let go of the button.

&nbsp;

3\. Open the <a href="https://install.wled.me/" target="_blank" rel="noreferrer nofollow noopener">WLED web installer</a>. Leave **Mode** on **Basic**, keep the newest version selected in the version dropdown, and keep **Plain** selected. Basic installs a 4MB build, which works on the LED-1.

![WLED web installer in Basic mode with version 16.0.1 in the version dropdown, Plain selected and highlighted, and the Install button highlighted](/assets/wled-installer-plain.png)

4\. Click **Install**, pick your LED-1's serial port, and follow the prompts. When the installer shows that installation is complete, close it.

5\. The device is still in **boot mode** and needs to be power cycled. To reboot it, either unplug the power cable or press the **reset button** labeled **RST** (the left button; the boot button **BT** is on the right).

6\. Set the LED-1's pins in WLED. Regular WLED doesn't know how the LED-1 is wired, so it needs the GPIO numbers from the [LED-1 pinout guide](../../setup/led1-pinout-guide/). Open your LED-1 in WLED (the [Connect to Wi-Fi](../../setup/getting-started-led1/#connect-to-wi-fi) steps show how), click **Config**, and set the pins in this order:

- Under **Usermods**, in the **AudioReactive** section, set the microphone pins: SD to GPIO 12, WS to GPIO 27, and SCK to GPIO 14. Check **Reboot after save?** and click **Save**. Do this first, because WLED's default microphone settings use GPIO 15, which Output 2 needs.
- After the LED-1 restarts, open **Config → LED & Hardware**. Set the LED outputs to GPIO 13 (Output 1) and GPIO 15 (Output 2), clicking **+** to add the second output. Set the relay to GPIO 22 and the button to GPIO 0, then click **Save**. If your LEDs stay dark while WLED shows them on, check **Invert** under **Relay** and save again.

[Head to the Getting Started article to set up your LED-1 as a new device!](/products/led1/setup/getting-started-led1.md){ .md-button .md-button--primary }