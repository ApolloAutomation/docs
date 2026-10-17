---
title: MSR-2 FAQ
description: "Answers to common questions about the MSR-2 mmWave sensor with Homey: sensors, radar tuning, distance zones, flows, and reporting."
---
# MSR-2 FAQ

1\. **What sensors are included in the MSR-2?**

* The MSR-2 includes several built-in sensors such as an mmWave radar for motion detection, a LUX and UV sensor, a temperature and pressure sensor, and an optional CO2 sensor.

2\. **How does the mmWave radar sensor work?**

* The mmWave radar sensor can detect movement, even subtle motions like someone sitting still in a room. It works by emitting radar waves that reflect off objects and detects motion based on the change in the signal. The sensor is highly effective in detecting people in a room, even through light walls.

3\. **What is the maximum detection range of the mmWave radar?**

* The HLK-LD2410B mmWave radar sensor has a maximum detection range of about 6 meters (19.7 feet), making it ideal for room-wide monitoring.

4\. **Can the MSR-2 detect multiple people?**

* No, the MSR-2 supports single-target tracking only but it has better still detection than the MTR-1 which makes it uniquely suited for situations where you need to track a very still target like on a bed, couch, etc.

5\. **What is the benefit of the LUX and UV sensor?**

* The LUX sensor measures the amount of light in a room, while the UV sensor tracks the ultraviolet index from the sun. These readings can be used to automate lighting systems, such as turning on or off lights depending on the ambient brightness, or to measure sunlight exposure in a room.

6\. **How does the optional CO2 sensor work?**

* The optional SCD-40 CO2 sensor provides accurate carbon dioxide measurements and is useful for tracking air quality in enclosed spaces. This sensor can be used to automate HVAC systems, sending alerts when CO2 levels are too high and suggesting when to ventilate the area.

7\. **How do I connect the MSR-2 to Homey?**

* The MSR-2 joins your Wi-Fi, and the Apollo Automation app for Homey talks to it directly over your local network through the ESPHome native API, with no cloud account. Once you add it, every sensor's readings show up on the device in Homey, ready for flows and Insights. The app runs on Homey Pro; Homey Cloud isn't supported.

!!! success "Next step: add your MSR-2 to Homey"

    Connect the sensor to your Wi-Fi through its hotspot, then add it with the Apollo Automation app. The getting started guide walks you through both.

    [Get started with Homey](../../general/setup/getting-started-msr2/){ .md-button .md-button--primary }

8\. **What kind of flows can I create with the MSR-2?**

* Flows can start from presence, from a distance zone, or from any reading. Turn on lights with **Radar target detected**, react to someone near the sensor with **Radar zone 1 becomes occupied**, adjust ventilation when CO2 levels rise (with the CO2 addon), or trigger alarms based on motion or environmental changes.

9\. **What are the RGB LED and piezo buzzer used for?**

* The RGB LED is the MSR-2's light in Homey. Turn it on or off, dim it, or change its color from the device or in a flow, for example to show detected motion or high UV exposure.
* The piezo buzzer is played through an ESPHome action, and the Apollo Automation app has no flow card for it, so Homey can't sound the buzzer. If you also run Home Assistant, it can: see the [piezo buzzer guide](../../../../products/general/piezo/).

10\. **How do I adjust the sensitivity of the presence detection?**

* In the device's **Settings** in the Homey app, the **Radar tuning (MSR-1 / MSR-2)** group has **Radar timeout** (how long presence holds after the last detection), **Radar max move distance gate**, and **Radar max still distance gate**. Each gate is 0.75 m, and gate 8 reaches 6 m, so lowering the max gates stops the radar from reacting to motion farther away.
* Per-gate sensitivity (the move and still thresholds for each gate) isn't in Homey. Tune it with the [HLK Radar Tool app](../setup/zones-hlk/), or on the sensor's own web page: in a browser, open `http://apollo-msr-2-xxxxxx.local`, where `xxxxxx` is the last 6 characters of the device's name in Homey.

11\. **Does the mmWave sensor detect through walls?**

* Yes, the mmWave sensor can detect movement through certain materials like thin walls, which is helpful in larger spaces but may require sensitivity adjustments if false positives occur due to adjacent rooms.

12\. **Can the MSR-2 be used outdoors?**

* No, the MSR-2 is primarily designed for indoor use and high humidity or temperatures too high or low could damage the device.

13\. **What’s new in the MSR-2 compared to the MSR-1?**

* The MSR-2 introduces several improvements, including a smaller form factor, an additional expansion slot for future accessories, an updated DPS310 pressure sensor for more accurate readings, and improved temperature and pressure tracking.

14\. **Can the MSR-2 track the exact location of people in a room?**

* No. The MSR-2 tracks a single target and reports how far it is from the sensor and whether it is moving or still. You can set up to three distance-based zones (Radar Zone 1 to 3) to tell roughly how far away someone is. For X/Y positions of up to three people, use the MTR-1 or R PRO-1.
* In Homey, set where zone 1 starts and where each zone ends under **Radar zones for MSR-2** in the device's **Settings**, and start flows with cards such as **Radar zone 2 becomes occupied** and **Radar zone 2 becomes clear**.

15\. **How does the temperature and pressure sensor work?**

* The DPS310 sensor provides precise readings of air temperature and pressure, which are especially useful when combined with the optional CO2 sensor to improve air quality monitoring. Keep in mind the heat generated by the ESP32 may require a temperature offset. Set it with **DPS temperature offset** under **Calibration offsets** in the device's **Settings** in the Homey app.

16\. **What kind of power supply is required for the MSR-2?**

* The MSR-2 is powered via USB-C and can be plugged into a standard wall outlet using a 5V adapter.

17\. **Can I customize the MSR-2 functionality?**

* Absolutely! With ESPHome, users can modify firmware, settings, and even print custom cases for the MSR-2. Our <a href="https://github.com/ApolloAutomation/MSR-2" target="_blank" rel="noreferrer nofollow noopener">YAML is on GitHub</a> and our <a href="https://www.printables.com/@Apollo_1187039" target="_blank" rel="noreferrer nofollow noopener">.STEP and .STL CAD files</a> are available for community use.

18\. **How often does the MSR-2 report sensor data?**

* The radar reports presence as it changes, and most other readings update every 60 seconds by default. These intervals are set in the firmware, and Homey has no setting for them.
* The light and UV interval is the one you can change without editing the firmware: set **LTR390 Update Interval** (1 to 300 seconds) on the sensor's own web page (see question 10 for the address). The page hides this setting at first, so click **Show All** to list it. Changing the other intervals means editing the firmware with ESPHome.

19\. **Is the MSR-2 compatible with other smart home platforms?**

* Yes. Besides Homey (through the Apollo Automation app), the MSR-2 works with Home Assistant and with other platforms that support the <a href="https://esphome.io/components/api.html" target="_blank" rel="noreferrer nofollow noopener">ESPHome API</a>. See [Supported platforms](../../general/supported-platforms/).

20\. **Can I use multiple MSR-2 sensors with one Homey?**

* Yes. Add each MSR-2 with the Apollo Automation app. Each one shows up as its own device in Homey with its own readings and settings, so you can monitor and automate different rooms or areas in your home.

21\. **What accessories are available for the MSR-2?**

* The MSR-2 has an additional expansion slot for future accessories. Currently, accessories such as a USB-C wall plug mount and a ball mount for flexible positioning are available. We are also working on new expansion boards for future updates.

22\. **Is the MSR-2 secure?**

* The MSR-2 communicates over your local network using ESPHome, which provides a secure, local connection without the need for cloud services. No data is sent to external servers, ensuring privacy.

23\. **How do I install and configure the MSR-2?**

* Power the MSR-2 over USB-C, connect it to your Wi-Fi through its hotspot, and add it in Homey with the Apollo Automation app. Radar tuning, distance zones, and calibration offsets are all in the device's **Settings** in Homey. We provide detailed documentation and support through our Discord community and GitHub.

24\. **What makes the MSR-2 stand out from other motion sensors?**

* The MSR-2 stands out due to its mmWave radar’s ability to detect still motion (like someone sitting still) and its three distance-based zones. Additionally, its compact size, multi-sensor integration (motion, LUX, UV, CO2, temperature, pressure), and the open-source nature of the product make it highly versatile and customizable.

25\. **What is the warranty for the MSR-2?**

* The MSR-2 comes with a standard one-year warranty. If you experience any issues, our support team is available through Discord, email, or the website to assist with troubleshooting or replacement.
