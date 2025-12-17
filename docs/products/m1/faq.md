---
title: M-1 FAQ
description: Frequently asked questions about the M-1 controller.
---
1\. **Why am I seeing half a screen worth of color? Is my new M-1 Broken?**

* The firmware we use currently does not support us pre-configuring a few settings but they are required to be set for you to use the M-1 LED Matrix successfully. Please <a href="https://wiki.apolloautomation.com/products/m1/setup/getting-started-m1/#post-connect-setup" target="_blank" rel="noreferrer nofollow noopener">follow the post-connect-setup steps</a> to finish setting up your device!

2\. **Why am I seeing vertical sideways lines? Is my new M-1 Broken?**

* Re-seat the M-1 controller on the back of your M-1 matrix and it should now be working reliably!

3\. **What is the maximum power output of the M-1?**

* The LED-1 is able to safely offer 3 Amps of power using 5 Volts when using the usb-c cable and stock power supply.

3\. **Scrolling Text does not show as an effect, what am I doing wrong?**

* Scrolling text will show up once you change a few settings! Click on **Config**, then **2D Configuration**. Select **2D Matrix**, click the circle next to **Basic**, change the **Panel Dimensions** to **64 x 64** and click **Save**. Next click on **Config**, then **LED Preferences**. set **Chain Length** to **1** then uncheck the "enable automatic brightness limiter and click **Save**. <a href="https://wiki.apolloautomation.com/products/m1/setup/m1-matrix-settings/" target="_blank" rel="noreferrer nofollow noopener">Full configuration of settings here</a>.

4\. **Can I use a remote with the M-1?**

* Although the device does not come with IR, it does <a href="https://www.amazon.com/dp/B091TGDS6F" target="_blank" rel="noreferrer nofollow noopener">support the WizMote</a> over "ESP-NOW" and this works great inside of WLED! *Currently needs a special firmware compiled.*

5\. **How does the microphone work?**

* Audio-reactive WLED is built into the WLED firmware we ship with the M-1. Just make sure to enable it from the "info" pane and then try using an effect with the little Musical Note Image next to them!

6\. **Can I use the M-1 without Home Assistant or even Wi-Fi? Even on my boat/RV?**

* Yes! You can directly connect to the access point of your WLED device without a network using a phone or laptop. Look for "WLED-AP" in your Wi-Fi client list and enter in the password "wled1234", head to [http://4.3.2.1](http://4.3.2.1) or [http://wled.me](http://wled.me) then control your device!

7\. **How much power does it use?**

* The M-1 uses under 1 Amp of power for itself but will use up to 3amps at 5v for one panel

8\. **Can I reflash this with stock WLED firmware?**

* No, it needs a special fork. You can <a href="https://github.com/srg74/WLED-wemos-shield/tree/master/resources/Firmware/WLED_%20ESP_Flasher" target="_blank" rel="noreferrer nofollow noopener">flash it using this flasher tool</a> and use<a href="https://cdn.discordapp.com/attachments/1371998979369336922/1377651379237032096/WLEDMM_0.14.1-b32.40_adafruit_matrixportal_esp32s3.bin?ex=68556cd4&amp;is=68541b54&amp;hm=07c5b2ebffcc895d2f2100a9d370babf102d044739e3f1ade47cceff8581205a&amp;" target="_blank" rel="noreferrer nofollow noopener"> this firmware version</a>.

&nbsp;