---
title: M-1 FAQ
description: Frequently asked questions about the M-1 controller.
---
1\. **Why am I seeing half a screen worth of color? Is my new M-1 Broken?**

* It is not broken, the matrix settings need to be set. Units on WLED arrive already configured, so this usually means the device was reflashed or its settings were wiped. Run through <a href="https://wiki.apolloautomation.com/products/m1/setup/m1-matrix-settings/" target="_blank" rel="noreferrer nofollow noopener">Matrix Settings</a> and pick your firmware tab.

2\. **Why am I seeing vertical sideways lines? Is my new M-1 Broken?**

* Re-seat the M-1 controller on the back of your M-1 matrix and it should now be working reliably!

3\. **What is the maximum power output of the M-1?**

* The M-1 is able to safely offer 3 Amps of power using 5 Volts when using the usb-c cable and stock power supply. That covers one 64x64 panel, so every extra panel needs its own <a href="https://apolloautomation.com/products/m-1-led-matrix-power-module" target="_blank" rel="noreferrer nofollow noopener">power module</a>.

4\. **Scrolling Text does not show as an effect, what am I doing wrong?**

* The 2D setup has not been configured, so WLED does not know it is driving a matrix. Check **Config** then **2D Configuration** is set to a 64 x 64 panel. Full steps for both firmwares are on <a href="https://wiki.apolloautomation.com/products/m1/setup/m1-matrix-settings/" target="_blank" rel="noreferrer nofollow noopener">Matrix Settings</a>.

5\. **Can I use a remote with the M-1?**

* Although the device does not come with IR, it does <a href="https://www.amazon.com/dp/B091TGDS6F" target="_blank" rel="noreferrer nofollow noopener">support the WizMote</a> over "ESP-NOW" and this works great inside of WLED! On WLED this works with the firmware your M-1 already ships with. On the older WLED-MM 14.5.1 it needed a specially compiled build, so if you want a remote and you are still on 14.5.1, <a href="https://wiki.apolloautomation.com/products/m1/setup/upgrade-to-wled/" target="_blank" rel="noreferrer nofollow noopener">migrate to WLED</a> first. See <a href="https://wiki.apolloautomation.com/products/m1/addons/wizmote-remote/" target="_blank" rel="noreferrer nofollow noopener">Add a WizMote Remote</a> for the pairing steps.

6\. **How does the microphone work?**

* Audio-reactive WLED is built into the firmware we ship with the M-1, and on WLED it is on from the factory with the pins already set. Plug in the add-on and pick an effect with the little Musical Note Image next to it. The microphone is an optional add-on and needs a Rev6 or newer controller. See <a href="https://wiki.apolloautomation.com/products/m1/addons/adding-microphone-to-m-1/" target="_blank" rel="noreferrer nofollow noopener">Add Microphone</a>.

7\. **Can I use the M-1 without Home Assistant or even Wi-Fi? Even on my boat/RV?**

* Yes! The M-1 broadcasts its own open Wi-Fi network named **Apollo M-1**, with no password. Join it from a phone or laptop, head to [http://4.3.2.1](http://4.3.2.1), and control the device from there. Builds older than 16.0.1 add a serial number to the end of the network name.

8\. **How much power does it use?**

* The M-1 uses under 1 Amp of power for itself but will use up to 3amps at 5v for one panel.

9\. **Can I reflash this with stock WLED firmware?**

* Yes, as of WLED 16.0.1. HUB75 matrix support is now part of upstream WLED, so the M-1 no longer needs the MoonModules fork. Flash it from the <a href="https://install.apolloautomation.com/#/m-1" target="_blank" rel="noreferrer nofollow noopener">Apollo installer</a>, which offers WLED 16.0.1 alongside the older WLED-MM builds. WLED 16.0.1 requires a Rev6 controller.

10\. **I am on WLED-MM 14.5.1. Should I update?**

* If you have a Rev6 controller, yes. You get Pixel Forge, panel-grid layouts like 2x2, and everything upstream WLED ships from here on. The update is over the air and keeps your settings. See <a href="https://wiki.apolloautomation.com/products/m1/setup/upgrade-to-wled/" target="_blank" rel="noreferrer nofollow noopener">Upgrade to WLED</a>.

11\. **How do I factory reset the M-1?**

* On WLED, hold the button for ten seconds. That restores every factory setting including the display size, and you reconnect it to Wi-Fi afterward. On WLED-MM a reset does not restore the display settings, so use the <a href="https://wiki.apolloautomation.com/products/m1/troubleshooting/m1-reflash/" target="_blank" rel="noreferrer nofollow noopener">reflash guide</a> instead.

12\. **Why can't I upload a GIF from the WLED phone app?**

* The app's file picker greys out image files, which is a bug in the app rather than anything on the M-1. Open the device in any browser instead and use <a href="https://wiki.apolloautomation.com/products/m1/examples/pixel-forge/" target="_blank" rel="noreferrer nofollow noopener">Pixel Forge</a>.

13\. **Part of my panel is dark or the colors look wrong.**

* Work through the <a href="https://wiki.apolloautomation.com/products/m1/troubleshooting/m1-panel-faults/" target="_blank" rel="noreferrer nofollow noopener">panel troubleshooting table</a>, which matches what you are seeing to the likely cause.

&nbsp;
