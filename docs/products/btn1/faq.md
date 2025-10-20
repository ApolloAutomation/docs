---
title: BTN-1 FAQ
description: Frequently asked questions about the BTN-1 Macro Deck
---
1\. **My BTN-1 is registering single clicks but not multiple, what is wrong?**

* The BTN-1 is likely sleeping and when being woken up it only can register a single button press. We are looking into ways to avoid this but it might be an ESPHome limitation.

2\. **How long will the BTN-1 last on battery if it's not sleeping?**

* It's expected to last 18 hours on a single charge if you need to take it on the go - great for all <a href="https://esphome.io/components/espnow/" target="_blank" rel="noreferrer nofollow noopener">ESP-NOW</a> projects!

3\. **Why won't my BTN-1 multi presses work? Single press works fine!**

* The device is most likely sleeping - when sleeping, no multi clicks are supported. Only a physical button single press because that wakes the device up.

4\. **How do I connect the BTN-1 to Home Assistant?**

* The BTN-1 connects to your Home Assistant instance through the <a href="https://www.home-assistant.io/integrations/esphome/" target="_blank" rel="noreferrer nofollow noopener">ESPHome Integration</a> using WiFi.

5\. **Does the BTN-1 support Zigbee firmware?**

* The BTN-1 uses an 8MB C6 mini MCU so it technically does support zigbee - we might have official firmware for this in the future!

6\. **What kind of things can I do with the BTN-1?**

* You can do all sorts of neat things with the BTN-1 such as using it to quickly trigger an automation, a scene, a script, or anything else in Home Assistant.

7\. **What kind of power supply is required for the BTN-1?**

* The BTN-1 is powered via USB-C and can be plugged into a standard wall outlet using a 5V 1A or bigger power supply.

8\. **What addons are available for the BTN-1?**

* The BTN-1 will have an upcoming OLED screen and NFC connector addon!

9\. **Is the BTN-1 secure?**

* The BTN-1 communicates over your local network using encrypted traffic with the ESPHome API. This provides a secure, local connection without the need for cloud services. No data is sent to external servers, ensuring privacy.

10\. **What is the warranty for the BTN-1?**

* The BTN-1 comes with a standard one-year warranty. If you experience any issues, our support team is available through Discord, email, or the website to assist with troubleshooting or replacement.