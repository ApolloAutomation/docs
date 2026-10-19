---
title: R PRO-1 FAQ
description: "Answers to common questions about the R PRO-1 PoE mmWave sensor with Homey: sensors, Ethernet firmware, radar tuning, radar regions, and flows."
---
# R PRO-1 FAQ

1\. **What sensors are included in the R PRO-1?**

* The R PRO-1 includes several built-in sensors such as an LD2450 mmWave radar sensor and optional LD2412 mmWave radar for presence detection, a LUX and UV sensor, and an optional CO<sub>2</sub> sensor.

2\. **How does the mmWave radar sensor work?**

* The LD2450 emits **millimeter-wave radar signals (at 24GHz)** into the environment. When these signals hit a person or object, they bounce back. The sensor detects these returned signals and calculates key information.

3\. **What is the maximum detection range of the mmWave radar?**

* The <a href="https://www.hlktech.net/index.php?id=1157" target="_blank" rel="noreferrer nofollow noopener">HLK-LD2450</a> mmWave radar sensor has a maximum detection range of about 6 meters (19.7 feet) with multi-target tracking capabilities, making it ideal for room-wide monitoring.
* The optional <a href="https://www.hlktech.net/index.php?id=1076" target="_blank" rel="noreferrer nofollow noopener">HLK-LD2412</a> mmWave radar sensor has a maximum detection range of about 9 meters (29.5 feet) with single tracking capabilities and ability to tune moving and still energy which is perfect for still targets like sleeping in a bed, laying on a couch, etc.

4\. **Can the R PRO-1 detect multiple people?**

* Yes, the R PRO-1 comes with an LD2450 which can detect 3 people in up to 3 zones. The optional LD2412 addon will only detect one person.

5\. **What is the benefit of the LUX and UV sensor?**

* The LUX sensor measures the amount of light in a room, while the UV sensor tracks the ultraviolet index from the sun. These readings can be used to automate lighting systems, such as turning on or off lights depending on the ambient brightness, or to measure sunlight exposure in a room.
!!! tip "Mounting behind a faceplate or using ceiling mount removes ability for lux or UV to work properly"

    There is no way for the lux or UV index to work properly if there is no light or UV able to hit the sensor.

6\. **How does the optional CO<sub>2</sub> sensor work?**

* The optional SCD-40 CO<sub>2</sub> sensor provides accurate carbon dioxide measurements and is useful for tracking air quality in enclosed spaces. This sensor can be used to automate HVAC systems, sending alerts when CO<sub>2</sub> levels are too high and suggesting when to ventilate the area.

7\. **How do I connect the R PRO-1 to Homey?**

* The R PRO-1 ships with Wi-Fi firmware. Connect it to your Wi-Fi through its hotspot, then add it in Homey with the Apollo Automation app, which talks to it directly over your local network through the ESPHome native API. The app runs on Homey Pro; Homey Cloud isn't supported. See [Getting started](../../general/setup/getting-started/).
* Once it's connected, you can switch to Ethernet firmware for PoE from the sensor's own web page: in a browser, open `http://apollo-r-pro-1-w-xxxxxx.local`, where `xxxxxx` is the last 6 characters of the device's name in Homey. Choose **Ethernet** under **Firmware Type**, then press **Firmware Update**. The sensor downloads the new firmware from GitHub, so it needs internet access. You can also reflash it to Ethernet firmware from the <a href="https://install.apolloautomation.com/#/r-pro-1" target="_blank" rel="noreferrer nofollow noopener">Apollo R PRO-1 installer</a> by choosing **Ethernet**.
* Homey recognizes the R PRO-1 by its hardware address, so after the switch it stays the same device in Homey.

8\. **What kind of flows can I create with the R PRO-1?**

* Flows can start from presence, from a region of the room, or from any reading. Turn on lights with **Presence detected**, adjust ventilation when CO<sub>2</sub> levels rise (with the CO<sub>2</sub> addon), or trigger alarms based on motion or environmental changes.
* Draw regions with the **Radar regions** widget, and every detect region works with the region flow cards **A region became occupied**, **A region became empty**, and **A region is occupied**.

!!! success "Next step: build your first region flow"

    Draw a region with the [Zone Mapper tool](../setup/r-pro-1-zone-mapper-tool/), then make it do something: the step-by-step guide walks you through a flow that turns a light on when someone enters a region and off when they leave.

    [Turn on a light when someone enters a region](../../general/tutorials/region-light-flow-example/){ .md-button .md-button--primary }

9\. **What is the RGB LED used for?**

* The RGB LED provides visual alerts like high CO<sub>2</sub> levels! It's also the R PRO-1's light in Homey, so you can turn it on or off, dim it, or change its color from the device or in a flow.

10\. **How do I adjust the sensitivity of the presence detection?**

* In the device's **Settings** in the Homey app, **Radar tuning (MTR-1 / R PRO-1)** has **LD2450 timeout** and **LD2412 timeout**: how long each radar holds presence after the last detection, in seconds.
* The LD2412's per-gate sensitivity (the move and still thresholds for each gate) and its min and max distance gates aren't in Homey. Tune them on the sensor's own web page (see question 7 for the address), or with the [HLK Radar Tool app](../setup/zones-hlk/).
* The LD2450 has no sensitivity settings. Shape its detection with regions in the **Radar regions** widget instead, and mark spots that cause false detections, such as a fan or a curtain, as **Ignore this area**. An ignored area hides targets from your detect regions, so build your flows on the regions.

11\. **Does the mmWave sensor detect through walls?**

* Yes, the mmWave sensor can detect movement through certain materials like drywall and thin wood. In some instances it will need to be tuned to make sure adjacent rooms are not triggering the sensor.

12\. **Can the R PRO-1 be used outdoors?**

* No, the R PRO-1 is primarily designed for indoor use and high humidity or temperatures too high or low could damage the device.

13\. **Can the R PRO-1 track the exact location of people in a room?**

* Yes. The LD2450 reports the X and Y position of up to three people. In Homey, draw regions on a live map of the radar's view with the **Radar regions** widget, up to 32 per device. Each detect region reports occupied or empty as its own occupancy tile and works with the region flow cards. See the [Zone Mapper tool](../setup/r-pro-1-zone-mapper-tool/) guide.

14\. **What kind of power supply is required for the R PRO-1?**

* The R PRO-1 is powered via PoE (802.3af compliant) or USB-C and can be plugged into a standard wall outlet using a 5V 2A or bigger power supply.

15\. **Can I customize the R PRO-1 functionality?**

* Absolutely! With ESPHome, users can modify firmware, settings, and even print custom cases for the R PRO-1. Our <a href="https://github.com/ApolloAutomation/R_PRO-1" target="_blank" rel="noreferrer nofollow noopener">YAML is on GitHub</a> and our <a href="https://www.printables.com/@Apollo_1187039" target="_blank" rel="noreferrer nofollow noopener">.STEP and .STL CAD files</a> are available for community use.

16\. **How often does the R PRO-1 report sensor data?**

* Most sensors report every 60 seconds by default, and the mmWave sensors report immediately on change. These intervals are set in the firmware, and Homey has no setting for them, so changing one means editing the firmware with ESPHome.

17\. **Is the R PRO-1 compatible with other smart home platforms?**

* Yes, it is compatible with any system that can integrate with the ESPHome API, including Homey through the Apollo Automation app and Home Assistant. We also have a [list of supported platforms](../../general/supported-platforms/).

18\. **Can I use multiple R PRO-1 sensors with one Homey?**

* Yes. Add each R PRO-1 with the Apollo Automation app. Each one shows up as its own device in Homey with its own readings and settings, so you can monitor and automate different rooms or areas in your home. The **Radar regions** widget works per device, so add one widget for each R PRO-1.

19\. **What addons are available for the R PRO-1?**

* The R PRO-1 has a mezzanine port for an optional SCD40 CO<sub>2</sub> sensor. We also sell a gang box mount and a ceiling mount kit.

20\. **Is the R PRO-1 secure?**

* The R PRO-1 communicates with Homey over your local network through the ESPHome API. This provides a local connection without the need for cloud services. No data is sent to external servers, ensuring privacy.

21\. **What makes the R PRO-1 stand out from other motion sensors?**

* The R PRO-1 is the only dual mmWave sensor with PoE and the ability to integrate with multiple smart home platforms. It combines the MSR-2's ability to detect still detection perfectly and the MTR-1's ability to detect up to three targets in three zones!

22\. **What is the warranty for the R PRO-1?**

* The R PRO-1 comes with a standard one-year warranty. If you experience any issues, our support team is available through Discord, email, or the website to assist with troubleshooting or replacement.
