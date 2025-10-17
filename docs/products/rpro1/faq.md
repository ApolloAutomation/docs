---
title: R-Pro-1 FAQ
description: Frequently asked questions about the R-Pro-1 PoE mmWave sensor.
---
1\. **What sensors are included in the R-PRO-1?**

* The R-PRO-1 includes several built-in sensors such as a LD2450 mmWave radar sensor and optional LD2412 mmWave radar for presence detection, a LUX and UV sensor, and an optional CO<sub>2</sub> sensor.

2\. **How does the mmWave radar sensor work?**

* The LD2450 emits **millimeter-wave radar signals (at 24GHz)** into the environment. When these signals hit a person or object, they bounce back. The sensor detects these returned signals and calculates key information.

3\. **What is the maximum detection range of the mmWave radar?**

* The <a href="https://www.hlktech.net/index.php?id=1157" target="_blank" rel="noreferrer nofollow noopener">HLK-LD2450</a> mmWave radar sensor has a maximum detection range of about 6 meters (19.6 feet) with multi-target tracking capabilities, making it ideal for room-wide monitoring.
* The optional <a href="https://www.hlktech.net/index.php?id=1076" target="_blank" rel="noreferrer nofollow noopener">HLK-LD2412</a> mmWave radar sensor has a maximum detection range of about 9 meters (29.5 feet) with single tracking capabilities and ability to tune moving and still energy which is perfect for still targets like sleeping in a bed, laying on a couch, etc.

4\. **Can the R-PRO-1 detect multiple people?**

* Yes, the R-PRO-1 comes with a LD2450 which can detect 3 people in up to 3 zones. The optional ld2412 addon will only detect one person.

5\. **What is the benefit of the LUX and UV sensor?**

* The LUX sensor measures the amount of light in a room, while the UV sensor tracks the ultraviolet index from the sun. These readings can be used to automate lighting systems, such as turning on or off lights depending on the ambient brightness, or to measure sunlight exposure in a room.
* !!! tip "Mounting behind a faceplate or using ceiling mount removes ability for lux or UV to work properly"

          There is no way for the lux or UV index to work properly if there is no light or uv able to hit the sensor.

6\. **How does the optional CO<sub>2</sub> sensor work?**

* The optional SCD-40 CO<sub>2</sub> sensor provides accurate carbon dioxide measurements and is useful for tracking air quality in enclosed spaces. This sensor can be used to automate HVAC systems, sending alerts when CO<sub>2</sub> levels are too high and suggesting when to ventilate the area.

7\. **How do I connect the R-PRO-1 to Home Assistant?**

* The R-PRO-1 connects to your Home Assistant instance through ESPHome using WiFi. Once connected, you can switch to using the ethernet firmware. You can also reflash it to Ethernet firmware <a href="https://apolloautomation.github.io/R_PRO-1/" target="_blank" rel="noreferrer nofollow noopener">here</a>.

8\. **What kind of automations can I create with the R-PRO-1?**

* You can create a variety of automations, such as turning on lights when motion is detected, adjusting ventilation when CO<sub>2</sub> levels rise, or triggering alarms based on motion or environmental changes.

9\. **What is the RGB LED used for?**

* The RGB LED provides visual alerts like high CO<sub>2</sub> levels!

10\. **How do I adjust the sensitivity of the presence detection?**

* Sensitivity adjustments can be made through the device's webserver which you can reach from its ip address or hostname.local in a browser, or <a href="https://wiki.apolloautomation.com/products/msr2/calibrating-and-updating/zones-ha/" target="_blank" rel="noreferrer nofollow noopener">Home Assistant Device Page</a>, or <a href="https://wiki.apolloautomation.com/products/msr2/calibrating-and-updating/zones-hlk/" target="_blank" rel="noreferrer nofollow noopener">HLK Radar Tool app </a>allowing you to fine-tune the radar to avoid false positives or to increase its sensitivity for more precise detections.

11\. **Does the mmWave sensor detect through walls?**

* Yes, the mmWave sensor can detect movement through certain materials like drywall and thin wood. In some instances it will need to be tuned to make sure adjacent rooms are not triggering the sensor.

12\. **Can the R-PRO-1 be used outdoors?**

* No, the R-PRO-1 is primarily designed for indoor use and high humidity or temperatures too high or low could damage the device.

13\. **Can the R-PRO-1 track the exact location of people in a room?**

* Yes with the LD2450 mmWave sensor, it is able to reliably detect people in x/y coordinate 'zones' that you setup <a href="https://wiki.apolloautomation.com/products/msr2/calibrating-and-updating/zones-hlk/" target="_blank" rel="noreferrer nofollow noopener">here</a>.
* Yes, the R-PRO-1 uses multi-zone mmWave radar technology to track the approximate location of people within a room. It can determine whether someone is sitting, walking, or standing in different areas of the space.

14\. **What kind of power supply is required for the R-PRO-1?**

* The R-PRO-1 is powered via Ethernet (802.3 compliant) or USB-C and can be plugged into a standard wall outlet using a 5V 2A or bigger power supply.

15\. **Can I customize the R-PRO-1 functionality?**

* Absolutely! With ESPHome, users can modify firmware, settings, and even print custom cases for the R-PRO-1. Our <a href="https://github.com/ApolloAutomation/R_PRO-1" target="_blank" rel="noreferrer nofollow noopener">YAML is on Github</a> and our <a href="https://www.printables.com/@Apollo_1187039" target="_blank" rel="noreferrer nofollow noopener">.STEP and .STL CAD files</a> are available for community use.

16\. **How often does the R-PRO-1 report sensor data?**

* The reporting frequency can be customized through the ESPHome YAML configuration. You can set it to report data as frequently as every second or reduce the frequency to save energy or bandwidth. Defaults will be 60 seconds for most sensors, but the mmWave sensors will report immediately on change.

17\. **Is the R-PRO-1 compatible with other smart home platforms?**

* Yes, it is compatible with any system that can integrate with the ESPHome API. We also have a <a href="https://wiki.apolloautomation.com/products/general/supported-platforms/" target="_blank" rel="noreferrer nofollow noopener">list of supported platforms</a>.

18\. **Can I use multiple R-PRO-1 sensors in my Home Assistant setup?**

* Yes, you can have multiple R-PRO-1 sensors connected to the same Home Assistant instance. Each R-PRO-1 will show up as a separate device with a lot of entities to configure and automate on, allowing you to monitor and automate different rooms or areas in your home.

19\. **What addons are available for the R-PRO-1?**

* The R-PRO-1 has a mezzanine port for an optional SCD40 CO<sub>2</sub> sensor. We also sell a gang box mount and a ceiling mount kit.

20\. **Is the R-PRO-1 secure?**

* The R-PRO-1 communicates over your local network using encrypted traffic with the ESPHome API. This provides a secure, local connection without the need for cloud services. No data is sent to external servers, ensuring privacy.

21\. **What makes the R-PRO-1 stand out from other motion sensors?**

* The R-PRO-1 is the only dual mmWave sensor with PoE and ability to integrate with multiple smart home platforms seamlessly. It combines the MSR-2's ability to detect still detection perfectly and the MTR-1's ability to detect up to three targets in three zones!

22\. **What is the warranty for the R-PRO-1?**

* The R-PRO-1 comes with a standard one-year warranty. If you experience any issues, our support team is available through Discord, email, or the website to assist with troubleshooting or replacement.