---
title: PUMP-1 FAQ
description: Frequently asked questions about the PUMP-1 Fluid Pump Sensor
---
# NEED TO DO THIS

1\. **What sensors are included in the MSR-2?**

* The MSR-2 includes several built-in sensors such as an mmWave radar for motion detection, a LUX and UV sensor, a temperature and pressure sensor, and an optional CO2 sensor.

2\. **How does the mmWave radar sensor work?**

* The mmWave radar sensor can detect movement, even subtle motions like someone sitting still in a room. It works by emitting radar waves that reflect off objects and detects motion based on the change in the signal. The sensor is highly effective in detecting people in a room, even through light walls.

3\. **What is the maximum detection range of the mmWave radar?**

* The HLK-LD2410B mmWave radar sensor has a maximum detection range of about 6 meters (19.6 feet) with multi-target tracking capabilities, making it ideal for room-wide monitoring.

4\. **Can the MSR-2 detect multiple people?**

* No, the MSR-2 supports single-target tracking only but it has better still detection than the MTR-1 which makes it uniquely suited for situations where you need to track a very still target like on a bed, couch, etc.

5\. **What is the benefit of the LUX and UV sensor?**

* The LUX sensor measures the amount of light in a room, while the UV sensor tracks the ultraviolet index from the sun. These readings can be used to automate lighting systems, such as turning on or off lights depending on the ambient brightness, or to measure sunlight exposure in a room.

6\. **How does the optional CO2 sensor work?**

* The optional SCD-40 CO2 sensor provides accurate carbon dioxide measurements and is useful for tracking air quality in enclosed spaces. This sensor can be used to automate HVAC systems, sending alerts when CO2 levels are too high and suggesting when to ventilate the area.

7\. **How do I connect the MSR-2 to Home Assistant?**

* The MSR-2 connects to your Home Assistant instance through ESPHome using WiFi. Once connected, you can monitor data from all the sensors and set up automations.

8\. **What kind of automations can I create with the MSR-2?**

* You can create a variety of automations, such as turning on lights when motion is detected, adjusting ventilation when CO2 levels rise, or triggering alarms based on motion or environmental changes.

9\. **What are the RGB LED and piezo buzzer used for?**

* The RGB LED provides visual alerts, while the <a href="https://wiki.apolloautomation.com/products/general/piezo/" title="Click here to go to the piezo buzzer wiki tutorial" target="_blank" rel="noreferrer nofollow noopener">piezo buzzer offers audio notifications</a> for events like low moisture levels or high UV exposure.

10\. **How do I adjust the sensitivity of the presence detection?**

* Sensitivity adjustments can be made through the <a href="https://wiki.apolloautomation.com/products/msr2/calibrating-and-updating/zones-ha/" target="_blank" rel="noreferrer nofollow noopener">Home Assistant Device Page</a> or <a href="https://wiki.apolloautomation.com/products/msr2/calibrating-and-updating/zones-hlk/" target="_blank" rel="noreferrer nofollow noopener">HLK Radar Tool app </a>allowing you to fine-tune the radar to avoid false positives or to increase its sensitivity for more precise detections.

11\. **Does the mmWave sensor detect through walls?**

* Yes, the mmWave sensor can detect movement through certain materials like thin walls, which is helpful in larger spaces but may require sensitivity adjustments if false positives occur due to adjacent rooms.

12\. **Can the MSR-2 be used outdoors?**

* No, the MSR-2 is primarily designed for indoor use and high humidity or temperatures too high or low could damage the device.

13\. **What’s new in the MSR-2 compared to the MSR-1?**

* The MSR-2 introduces several improvements, including a smaller form factor, an additional expansion slot for future accessories, an updated DPS310 pressure sensor for more accurate readings, and improved temperature and pressure tracking.

14\. **Can the MSR-2 track the exact location of people in a room?**

* Yes, the MSR-2 uses multi-zone mmWave radar technology to track the approximate location of people within a room. It can determine whether someone is sitting, walking, or standing in different areas of the space.

15\. **How does the temperature and pressure sensor work?**

* The DPS310 sensor provides precise readings of air temperature and pressure, which are especially useful when combined with the optional CO2 sensor to improve air quality monitoring. Keep in mind the heat generated by the ESP32 may require a temperature offset adjustment in the configuration.

16\. **What kind of power supply is required for the MSR-2?**

* The MSR-2 is powered via USB-C and can be plugged into a standard wall outlet using a 5V adapter.

17\. **Can I customize the MSR-2 functionality?**

* Absolutely! With ESPHome, users can modify firmware, settings, and even print custom cases for the MSR-2. Our <a href="https://github.com/ApolloAutomation/MSR-2" target="_blank" rel="noreferrer nofollow noopener">YAML is on Github</a> and our <a href="https://www.printables.com/@Apollo_1187039" target="_blank" rel="noreferrer nofollow noopener">.STEP and .STL CAD files</a> are available for community use.

18\. **How often does the MSR-2 report sensor data?**

* The reporting frequency can be customized through the ESPHome YAML configuration. You can set it to report data as frequently as every second or reduce the frequency to save energy or bandwidth.

19\. **Is the MSR-2 compatible with other smart home platforms?**

* The MSR-2 is specifically designed for Home Assistant via ESPHome. While it could be compatible with other platforms through custom integrations, its primary functionality is optimized for Home Assistant.

20\. **Can I use multiple MSR-2 sensors in my Home Assistant setup?**

* Yes, you can have multiple MSR-2 sensors connected to the same Home Assistant instance. Each device will show up as a separate entity, allowing you to monitor and automate different rooms or areas in your home.

21\. **What accessories are available for the MSR-2?**

* The MSR-2 has an additional expansion slot for future accessories. Currently, accessories such as a USB-C wall plug mount and a ball mount for flexible positioning are available. We are also working on new expansion boards for future updates.

22\. **Is the MSR-2 secure?**

* The MSR-2 communicates over your local network using ESPHome, which provides a secure, local connection without the need for cloud services. No data is sent to external servers, ensuring privacy.

23\. **How do I install and configure the MSR-2?**

* Installation is straightforward, with the MSR-2 powered via USB-C and connecting to Home Assistant through WiFi. Configuration is done in ESPHome, where you can set sensor parameters, adjust automations, and more. We provide detailed documentation and support through our Discord community and GitHub.

24\. **What makes the MSR-2 stand out from other motion sensors?**

* The MSR-2 stands out due to its mmWave radar’s ability to detect still motion (like someone sitting still) and its capability to track multiple targets and zones. Additionally, its compact size, multi-sensor integration (motion, LUX, UV, CO2, temperature, pressure), and the open-source nature of the product make it highly versatile and customizable.

25\. **What is the warranty for the MSR-2?**

* The MSR-2 comes with a standard one-year warranty. If you experience any issues, our support team is available through Discord, email, or the website to assist with troubleshooting or replacement.