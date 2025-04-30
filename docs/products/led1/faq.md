---
title: LED-1 FAQ
description: Frequently asked questions about the LED-1 controller.
---
1\. **What is the maximum power output of the LED-1?**

* The LED-1 is able to safely offer 10 amps of power using either 5 V, 12 V, or a 24 V when using an external power supply.
* The device can also be powered via USB-C-PD (Power Delivery) with 5 V or 12 V at 3 amps.
* The device can also be powered by USB-C with 5 V at 3 Amps.
* The device has a built-in replaceable fuse that will trip if 10 Amps is exceeded. The output voltage is the same as the input voltage, so please make sure you buy the same 5 V, or 12 V, or 24 V power supply and LED strips.

2\. **How long of an LED strip can I use with the LED-1?**

* The length of LED strips depends more on other factors like voltage drop. Ultimately, we suggest going 3 meters with 5 V for each output, so 3 meters + 3 meters connected to separate outputs. You can go up to 5 meters at 24 V without seeing much voltage drop though!

3\. **Can I use a remote with the LED-1?**

* Although the device does not come with IR, it does <a href="https://www.amazon.com/dp/B091TGDS6F" target="_blank" rel="noreferrer nofollow noopener">support the WizMote</a> over "ESP-NOW" and this works great inside of WLED!

4\. **How does the microphone work?**

* Audio-reactive WLED is built into the WLED firmware we ship with the LED-1. Just make sure to enable it from the "info" pane and then try using an effect with the little Musical Note Image next to them!

5\. **My LEDs are the wrong color how do I fix it?**

* You might have SK6812 or some other leds other than the default WS2812B and WLED needs to be configured to know that you are using a different type of LEDs. Head to the <a href="https://kno.wled.ge/features/settings/#led-outputs" target="_blank" rel="noreferrer nofollow noopener">LED Outputs section of wled docs to learn more</a>.

6\. **Can I use the LED-1 without Home Assistant or even Wi-Fi? Even on my boat/RV?**

* Yes! You can directly connect to the access point of your WLED device without a network using a phone or laptop. Look for "WLED-AP" in your Wi-Fi client list and enter in the password "wled1234", head to [http://4.3.2.1](http://4.3.2.1) or [http://wled.me](http://wled.me) then control your device!

7\. **My LEDs are very dim how do I fix it?**

* Head to the settings of WLED and make sure the brightness limiter is off. You also might have a very long LED strip and you might <a href="https://kno.wled.ge/advanced/wiring/" target="_blank" rel="noreferrer nofollow noopener">need power injection to make it work properly.</a>

8\. **How much power does it use?**

* The LED-1 uses under 1 Amp of power for itself but will use up to 10amps at 5-24 Volts based on the power supply used.

9\. **Can I reflash this with stock WLED firmware?**

* Yes! Our devices do not need custom compiled firmware, any esp32 8MB or technically 4MB firmware should work.

&nbsp;