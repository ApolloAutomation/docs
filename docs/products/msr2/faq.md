---
title: MSR-2 FAQ
description: "Answers to common questions about the MSR-2 mmWave multisensor: its sensors, the radar, setup in Home Assistant, accessories, and support."
---
# MSR-2 FAQ

Answers to common questions about the Apollo MSR-2, grouped by topic.

## Sensors and features

1\. **What sensors are included in the MSR-2?**

* The MSR-2 has an mmWave radar for motion detection, a LUX and UV sensor, and a temperature and pressure sensor built in. An optional CO2 sensor is also available.

2\. **What's new in the MSR-2 compared to the MSR-1?**

* The MSR-2 introduces several improvements: a smaller form factor, an additional expansion slot for future accessories, an updated DPS310 pressure sensor for more accurate readings, and improved temperature and pressure tracking.

3\. **What makes the MSR-2 stand out from other motion sensors?**

* Its mmWave radar can detect still motion (like someone sitting still), and it reports presence in configurable distance zones. It's also compact, combines several sensors in one device (motion, LUX, UV, CO2, temperature, and pressure), and is open source, so you can customize it.

4\. **What is the benefit of the LUX and UV sensor?**

* The LUX sensor measures the amount of light in a room, and the UV sensor tracks the ultraviolet index from the sun. Use these readings to automate your lighting, such as turning lights on or off based on the ambient brightness, or to measure how much sunlight a room gets.

5\. **How does the optional CO2 sensor work?**

* The optional SCD-40 CO2 sensor provides accurate carbon dioxide measurements, which helps you track air quality in enclosed spaces. Use it to automate your HVAC system, send alerts when CO2 levels are too high, and know when to ventilate the area.

6\. **How does the temperature and pressure sensor work?**

* The DPS310 sensor provides precise readings of air temperature and pressure. These are especially useful alongside the optional CO2 sensor for air quality monitoring. Heat from the ESP32 can affect the temperature reading, so you may need to adjust the temperature offset in the configuration.

7\. **My DPS310 Pressure or DPS310 Temperature shows as "unknown" in Home Assistant. Is something wrong?**

* No, your device is fine. A small subset of units shipped without the DPS310 sensor because the part was discontinued by the manufacturer. If you see those entities reporting "unknown," your unit is one of these. Every other sensor on the device works normally.

8\. **What are the RGB LED and piezo buzzer used for?**

* The RGB LED provides visual alerts, while the <a href="https://wiki.apolloautomation.com/products/general/piezo/" title="Click here to go to the piezo buzzer wiki tutorial" target="_blank" rel="noreferrer nofollow noopener">piezo buzzer offers audio notifications</a> for events like high CO2 levels or high UV exposure.

## mmWave radar

9\. **How does the mmWave radar sensor work?**

* The mmWave radar sends out radar waves that reflect off objects, and it detects motion from the change in the reflected signal. It picks up even subtle motion, like someone sitting still in a room. The sensor is highly effective at detecting people in a room, even through light walls.

10\. **What is the maximum detection range of the mmWave radar?**

* The HLK-LD2410B mmWave radar sensor has a maximum detection range of about 6 meters (19.7 feet), which makes it ideal for monitoring a whole room.

11\. **Can the MSR-2 detect multiple people?**

* No. The MSR-2 supports single-target tracking only. It does have better still detection than the MTR-1, which makes it uniquely suited to tracking a very still target, such as someone on a bed or couch.

12\. **Can the MSR-2 track the exact location of people in a room?**

* No. The LD2410B reports how far away a moving or still target is, not where it is in the room. The MSR-2 uses that distance to tell you which of three configurable distance zones is occupied, and whether the target is moving or still.

13\. **Does the mmWave sensor detect through walls?**

* Yes. The mmWave sensor can detect movement through certain materials, such as thin walls. That helps in larger spaces, but if movement in an adjacent room causes false positives, you may need to adjust the sensitivity (see question 14).

14\. **How do I adjust the sensitivity of the presence detection?**

* Adjust it from the <a href="https://wiki.apolloautomation.com/products/msr2/setup/zones-ha/" target="_blank" rel="noreferrer nofollow noopener">Home Assistant Device Page</a> or the <a href="https://wiki.apolloautomation.com/products/msr2/setup/zones-hlk/" target="_blank" rel="noreferrer nofollow noopener">HLK Radar Tool app</a>. Both let you fine-tune the radar to avoid false positives, or increase its sensitivity for more precise detection.

## Setup and use

15\. **How do I install and configure the MSR-2?**

* Power the MSR-2 over USB-C, then connect it to Home Assistant over Wi-Fi. You configure it in ESPHome, where you can set sensor parameters, adjust automations, and more. Apollo provides detailed documentation, plus support through the Apollo Discord community and GitHub.

16\. **What kind of power supply is required for the MSR-2?**

* The MSR-2 is powered over USB-C. Plug it into a standard wall outlet with a 5V adapter.

17\. **How do I connect the MSR-2 to Home Assistant?**

* The MSR-2 connects to your Home Assistant instance through ESPHome over Wi-Fi. Once it's connected, you can monitor data from all the sensors and set up automations.

18\. **Can I use multiple MSR-2 sensors in my Home Assistant setup?**

* Yes, you can have multiple MSR-2 sensors connected to the same Home Assistant instance. Each one shows up as its own device with its own set of entities, so you can monitor and automate different rooms or areas in your home.

19\. **Is the MSR-2 compatible with other smart home platforms?**

* The MSR-2 is designed specifically for Home Assistant through ESPHome, and its primary functionality is optimized for Home Assistant. It could be compatible with other platforms through custom integrations.

20\. **What kind of automations can I create with the MSR-2?**

* You can create a variety of automations, such as turning on lights when motion is detected, adjusting ventilation when CO2 levels rise, or triggering alarms based on motion or environmental changes.

21\. **How often does the MSR-2 report sensor data?**

* You can customize the reporting frequency in the ESPHome YAML configuration. Set it to report data as often as every second, or reduce the frequency to save energy or bandwidth.

22\. **Can the MSR-2 be used outdoors?**

* No. The MSR-2 is designed primarily for indoor use. High humidity, or temperatures that are too high or too low, could damage the device.

## Customization and accessories

23\. **Can I customize the MSR-2 functionality?**

* Yes. You can modify the firmware and settings with ESPHome, and you can print custom cases for the MSR-2. The <a href="https://github.com/ApolloAutomation/MSR-2" target="_blank" rel="noreferrer nofollow noopener">YAML is on GitHub</a>, and the <a href="https://www.printables.com/@Apollo_1187039" target="_blank" rel="noreferrer nofollow noopener">.STEP and .STL CAD files</a> are available for community use.

24\. **What accessories are available for the MSR-2?**

* The MSR-2 has an additional expansion slot for future accessories. Available accessories include a USB-C wall plug mount and a ball mount for flexible positioning. Apollo is also working on new expansion boards for future updates.

## Privacy and support

25\. **Is the MSR-2 secure?**

* The MSR-2 communicates over your local network using ESPHome, which provides a secure, local connection without the need for cloud services. No data is sent to external servers, so your data stays private.

26\. **What is the warranty for the MSR-2?**

* The MSR-2 comes with a standard one-year warranty. If you run into an issue, Apollo's support team can help with troubleshooting or a replacement through Discord, email, or the website.
