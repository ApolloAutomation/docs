---
title: BTN-1 FAQ
description: "Answers to common questions about the BTN-1 Macro Deck with Homey: button presses, battery, connecting to Homey, and flows."
---
# BTN-1 FAQ

1\. **My BTN-1 is registering single clicks but not multiple, what is wrong?**

* The BTN-1 is likely sleeping and when being woken up it only can register a single button press. We are looking into ways to avoid this but it might be an ESPHome limitation.

2\. **How long will the BTN-1 last on battery if it's not sleeping?**

* It's expected to last 18 hours on a single charge if you need to take it on the go - great for all <a href="https://esphome.io/components/espnow/" target="_blank" rel="noreferrer nofollow noopener">ESP-NOW</a> projects!

3\. **Why won't my BTN-1 multi presses work? Single press works fine!**

* The device is most likely sleeping - when sleeping, no multi clicks are supported. Only a physical button single press because that wakes the device up.

4\. **How do I connect the BTN-1 to Homey?**

* The BTN-1 joins your Wi-Fi, and the Apollo Automation app for Homey talks to it directly over your local network through the ESPHome native API, with no cloud account. Add it the same way as any Apollo device. The app runs on Homey Pro; Homey Cloud isn't supported.

!!! success "Next step: add your BTN-1 to Homey"

    Connect the BTN-1 to your Wi-Fi through its hotspot, then add it with the Apollo Automation app.

    [Get started with Homey](../../general/setup/getting-started/){ .md-button .md-button--primary }

5\. **Does the BTN-1 support Zigbee firmware?**

* The BTN-1 uses an 8MB C6 mini MCU so it technically does support zigbee - we might have official firmware for this in the future!

6\. **What kind of things can I do with the BTN-1?**

* Each button can start any flow in Homey. The **Button pressed** card fires for **Button 1** to **Button 4** with a press type of **Click**, **Double click**, **Triple click**, or **Hold**, so one BTN-1 gives you 16 different triggers.
* Flows can also color the key lights with **Set button light color**, and switch them off with **Turn off button light**.

7\. **What kind of power supply is required for the BTN-1?**

* The BTN-1 is powered via USB-C and can be plugged into a standard wall outlet using a 5V 1A or bigger power supply.

8\. **What addons are available for the BTN-1?**

* The BTN-1 will have an upcoming OLED screen and NFC connector addon!

9\. **Is the BTN-1 secure?**

* The BTN-1 communicates with Homey over your local network through the ESPHome API. This provides a local connection without the need for cloud services. No data is sent to external servers, ensuring privacy.

10\. **What is the warranty for the BTN-1?**

* The BTN-1 comes with a standard one-year warranty. If you experience any issues, our support team is available through Discord, email, or the website to assist with troubleshooting or replacement.
