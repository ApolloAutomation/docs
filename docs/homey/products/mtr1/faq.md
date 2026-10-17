---
title: MTR-1 FAQ
description: "Answers to common questions about the MTR-1 multi-target mmWave sensor with Homey: sensors, radar regions, flows, reporting, and firmware."
---
# MTR-1 FAQ

1\. **What sensors are included in the MTR-1?**

* The MTR-1 includes a multi-target mmWave radar sensor for detecting motion and positioning, as well as LUX, UV, temperature, and pressure sensors. There’s also an optional CO2 sensor available.

2\. **How does the mmWave radar sensor work?**

* The MTR-1’s mmWave radar sensor tracks movement by emitting radar waves and detecting changes in reflected signals. This sensor can detect multiple targets and their locations within a room, offering more precise tracking than traditional motion sensors. It can even detect through light walls.

3\. **How many targets can the MTR-1 track?**

* The MTR-1 can track up to three targets simultaneously, allowing it to monitor multiple people in a room and provide their positions within defined zones.

4\. **What is the maximum detection range of the mmWave radar?**

* The mmWave radar sensor in the MTR-1 has a maximum detection range of 6 meters (about 19.7 feet), making it ideal for monitoring large rooms or spaces.

5\. **Can the MTR-1 be used to track the exact location of people in a room?**

* Yes, the MTR-1 can detect people’s positions within zones, such as distinguishing if someone is near a door, on the couch, or standing by the kitchen counter. This enables precise automation based on a person’s location within the room.

6\. **What is the benefit of the LUX and UV sensor?**

* The LUX sensor measures the ambient light in the room, while the UV sensor tracks ultraviolet light exposure. This data can be used for automations like adjusting lighting levels, or providing alerts when sunlight is strong.

7\. **How does the optional CO2 sensor work?**

* The optional CO2 sensor measures the concentration of carbon dioxide in the air, which is important for monitoring air quality in enclosed spaces. High CO2 levels can lead to poor sleep, drowsiness, and other health issues, and the sensor can trigger automations to turn on fans or open windows.

8\. **What are some common use cases for the MTR-1?**

* The MTR-1 can be used to automate lights based on people’s presence in a room, trigger alarms or notifications when someone enters a space, and adjust HVAC settings based on CO2 levels. Its precise tracking capabilities also make it great for monitoring multiple zones within a room, such as distinguishing when someone is at the stove versus the sink.

9\. **How do I connect the MTR-1 to Homey?**

* The MTR-1 joins your Wi-Fi, and the Apollo Automation app for Homey talks to it directly over your local network through the ESPHome native API, with no cloud account. Once you add it, every sensor's readings show up on the device in Homey, ready for flows and Insights. The app runs on Homey Pro; Homey Cloud isn't supported.

10\. **What kind of flows can I set up with the MTR-1?**

* Flows can start from presence, from a region of the room, or from any reading. Turn lights on and off as people come and go, run an air purifier when CO2 rises (with the CO2 addon), or get a notification when someone walks into a doorway.
* Draw regions with the **Radar regions** widget, and every detect region works with the region flow cards **A region became occupied**, **A region became empty**, and **A region is occupied**. Because the MTR-1 tracks up to three people, a region can react to someone walking over to the desk even while someone else is on the couch.

!!! success "Next step: build your first region flow"

    Draw a region with the [Zone Mapper tool](../setup/mtr-1-zone-mapper-tool/), then make it do something: the step-by-step guide walks you through a flow that turns a light on when someone enters a region and off when they leave.

    [Turn on a light when someone enters a region](../../general/tutorials/region-light-flow-example/){ .md-button .md-button--primary }

11\. **How do I adjust the sensitivity of the motion detection?**

* The MTR-1's LD2450 radar has no sensitivity settings to tune, unlike the radar in the MSR-2. Shape detection with regions instead: draw the areas you care about in the **Radar regions** widget, and mark spots that cause false detections, such as a fan or a curtain, as **Ignore this area**. An ignored area hides targets from your detect regions, so build your flows on the regions.
* To change how long presence holds after someone leaves, set **Timeout** (in seconds) under **Radar tuning (MTR-1 / R PRO-1)** in the device's **Settings** in the Homey app.

12\. **Can the MTR-1 detect motion through walls?**

* Yes, the mmWave radar in the MTR-1 can detect movement through certain materials, such as light walls or thin furniture. If a neighboring room triggers it, keep your detect regions inside the room, or draw a region set to **Ignore this area** over the spot. See the [Zone Mapper tool](../setup/mtr-1-zone-mapper-tool/) guide.

13\. **Can the MTR-1 be used outdoors?**

* While the MTR-1 is primarily designed for indoor use, with proper weatherproofing and environmental protection, it could be used in sheltered outdoor environments. Be cautious of exposure to moisture or extreme weather.

14\. **Does the MTR-1 work with other smart home platforms?**

* Yes. Besides Homey (through the Apollo Automation app), the MTR-1 works with Home Assistant and with other platforms that support the <a href="https://esphome.io/components/api.html" target="_blank" rel="noreferrer nofollow noopener">ESPHome API</a>. See [Supported platforms](../../general/supported-platforms/).

15\. **How does the temperature and pressure sensor work?**

* The temperature and pressure sensor provides accurate measurements for air temperature and barometric pressure. This data can be used in automations, such as controlling heating/cooling systems or monitoring environmental conditions.

16\. **How is the MTR-1 powered?**

* The MTR-1 is powered through a USB-C connection and can be plugged into a standard wall outlet using a 5V adapter.

17\. **What is the purpose of the RGB LED and piezo buzzer?**

* The RGB LED is the MTR-1's light in Homey. Turn it on or off, dim it, or change its color from the device or in a flow, for example red when CO2 is high or green for a general notification.
* The piezo buzzer is played through an ESPHome action, and the Apollo Automation app has no flow card for it, so Homey can't sound the buzzer. If you also run Home Assistant, it can: see the [piezo buzzer guide](../../../../products/general/piezo/).

18\. **Can I customize the MTR-1’s features?**

* Yes, the MTR-1 is fully customizable through ESPHome. You can modify sensor settings, change reporting intervals, and create custom automations based on the sensor readings.

19\. **What is the reporting frequency of the MTR-1’s sensors?**

* The radar reports as people move. The other sensors report on intervals set in the firmware: by default, CO2 every 60 seconds and pressure and temperature every 30 seconds. Homey has no setting for these intervals.
* The light and UV interval is the one you can change without editing the firmware: set **LTR390 Update Interval** (1 to 300 seconds, 60 by default) on the sensor's own web page. In a browser, open `http://apollo-mtr-1-xxxxxx.local`, where `xxxxxx` is the last 6 characters of the device's name in Homey. Changing the other intervals means editing the firmware with ESPHome.

20\. **Can I use multiple MTR-1 sensors in my smart home setup?**

* Yes. Add each MTR-1 with the Apollo Automation app. Each one shows up as its own device in Homey with its own readings, so you can monitor several rooms at the same time. The **Radar regions** widget works per device, so add one widget for each MTR-1.

21\. **What’s the difference between the MTR-1 and MSR-2?**

* The MTR-1 features multi-target radar tracking, allowing it to detect multiple people in a room and track their positions. The MSR-2, on the other hand, is designed more for single-target detection and has a slightly different sensor set, though both sensors offer robust environmental monitoring capabilities.

22\. **What accessories are available for the MTR-1?**

* Accessories for the MTR-1 include mounting brackets, stands, and a variety of expansion options, like additional sensor modules. These allow for greater flexibility in where and how you use the sensor.

23\. **What are the primary advantages of the MTR-1 over other motion sensors?**

* The MTR-1’s mmWave radar is significantly more advanced than traditional PIR (Passive Infrared) motion sensors. It can detect subtle movements, track multiple targets, and monitor precise locations within a room, making it ideal for sophisticated home automations. Its additional sensors (LUX, UV, temperature, pressure, optional CO2) also provide greater environmental awareness.

24\. **How do I install the MTR-1?**

* Power the MTR-1 over USB-C, connect it to your Wi-Fi through its hotspot, then add it in Homey with the Apollo Automation app. The [getting started guide](../../general/setup/getting-started-mtr1/) walks you through each step, and we offer support via our Discord community.

25\. **How secure is the MTR-1?**

* The MTR-1 operates entirely on your local network, using ESPHome, which means no data is sent to external servers. This ensures that your home automation data remains private and secure.

26\. **Does the MTR-1 require cloud connectivity?**

* No. The MTR-1 talks to Homey directly over your local network through the ESPHome native API. You don’t need cloud access or a subscription to use the sensor.

27\. **How do I update the firmware on the MTR-1?**

* Homey doesn't install firmware updates: the Apollo Automation app reads and controls the MTR-1 but has no update action. To put new firmware on, flash it over USB with the Apollo installer, as described in [Factory re-flash MTR-1](../troubleshooting/mtr1-code/), then add the sensor to Homey again.
* If you also run Home Assistant, ESPHome can update the MTR-1 over the air instead. See [Updating firmware](../../../../products/general/calibrating-and-updating/updating-firmware/).

28\. **What is the warranty on the MTR-1?**

* The MTR-1 comes with a one-year warranty. If you encounter any issues, we provide comprehensive support via email, Discord, or our website to ensure you’re fully satisfied with the product.

29\. **How long does it take to set up the MTR-1?**

* Plan on 10 to 15 minutes to connect the MTR-1 to your Wi-Fi and add it to Homey.

30\. **What’s in the box?**

* Each MTR-1 package includes the assembled board, case, support stand, and a link to documentation, open-source code, and CAD models. Additionally, you’ll receive an Apollo Automation sticker.
