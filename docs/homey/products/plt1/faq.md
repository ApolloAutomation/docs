---
title: PLT-1 FAQ
description: "Answers to common questions about the PLT-1 plant sensor with Homey: sensors, power, connecting to Homey, flows, and how often it reports."
---
# PLT-1 FAQ

1\. **What sensors are included in the PLT-1?**

* The PLT-1 comes with sensors to measure soil moisture, air temperature, humidity, LUX, and UV. There is also an optional DS18b20 waterproof soil temperature probe available for measuring soil temperature.

2\. **How does the capacitive soil moisture sensor work?**

* The capacitive soil moisture sensor measures the water content in the soil by detecting changes in the dielectric permittivity of the soil, which is affected by moisture. It’s more durable than resistive sensors because it doesn’t corrode and is protected with a conformal coating.

3\. **How is the PLT-1 powered?**

* The PLT-1 operates with USB-C power at 5 volts using 1amp or less (5W).

4\. **What’s the difference between the battery and non-battery versions?**

* The PLT-1B is battery-operated (18650) and slightly larger, while the non-battery (NB) version is compact and requires USB-C power at 5 volts using 1amp or less (5W). They both have all of the same components for measuring soil moisture, air temp/humidity, lux/uv, etc.

5\. **How does the optional soil temperature probe work?**

* The optional DS18b20 waterproof soil temperature probe is 20 cm / 7.8 inches long. It measures the temperature directly in the soil and can be used to monitor the conditions for specific plants that require precise temperature control for optimal growth.

6\. **Is the PLT-1 weatherproof? Can I use it outdoors?**

* The PLT-1 is primarily designed for indoor use. While some components, such as the waterproof soil temperature probe, can withstand harsher environments, the main body of the sensor is not rated for outdoor use unless adequately protected.

7\. **How does the PLT-1 connect to Homey?**

* The PLT-1 joins your Wi-Fi, and the Apollo Automation app for Homey talks to it directly over your local network through the ESPHome native API, with no cloud account. Once you add it, its readings show up on the device in Homey, ready for flows and Insights. The app runs on Homey Pro; Homey Cloud isn't supported.

!!! success "Next step: add your PLT-1 to Homey"

    Connect the sensor to your Wi-Fi through its hotspot, then add it with the Apollo Automation app. The getting started guide walks you through both.

    [Get started with Homey](../../general/setup/getting-started-plt1/){ .md-button .md-button--primary }

8\. **What kind of flows can I set up with the PLT-1?**

* Any PLT-1 reading can start a flow in Homey. For example, send a notification when soil moisture drops, turn on a grow light when the light level falls, or adjust your heating or cooling based on the air temperature and humidity around your plants.

9\. **How often does the PLT-1 send sensor data?**

* Most readings update every 60 seconds by default. The intervals are set in the sensor's firmware, and Homey has no setting for them. The light and UV interval is the one you can change without editing the firmware: set **LTR390 Update Interval** (1 to 300 seconds) on the sensor's own web page. In a browser, open `http://apollo-plt-1-xxxxxx.local`, where `xxxxxx` is the last 6 characters of the device's name in Homey. Changing the other intervals means editing the firmware with ESPHome.

10\. **Can I customize the PLT-1’s functionality?**

* Absolutely! With ESPHome, users can modify firmware, settings, and even print custom cases for the PLT-1. Our <a href="https://github.com/ApolloAutomation/PLT-1" target="_blank" rel="noreferrer nofollow noopener">YAML is on GitHub</a> and our <a href="https://www.printables.com/@Apollo_1187039" target="_blank" rel="noreferrer nofollow noopener">.STEP and .STL CAD files</a> are available for community use.

11\. **What are the RGB LED and piezo buzzer used for?**

* The RGB LED is the PLT-1's light in Homey. Turn it on or off, dim it, or change its color from the device or in a flow, for example to glow red when the soil gets dry.
* The piezo buzzer is played through an ESPHome action, and the Apollo Automation app has no flow card for it, so Homey can't sound the buzzer. If you also run Home Assistant, it can: see the [piezo buzzer guide](../../../../products/general/piezo/).

12\. **What is the benefit of using a conformal coating on the soil moisture sensor?**

* The conformal coating protects the sensor from moisture-related degradation, improving its lifespan and durability.

13\. **What plants are compatible with the PLT-1?**

* The PLT-1 works with all kinds of indoor plants. Look up the light, humidity, and soil moisture your plant likes, then use those values as thresholds in your Homey flows, so you hear about it when a reading drifts out of range.

14\. **Can I monitor multiple plants with one PLT-1?**

* The PLT-1 is designed to monitor a single plant’s environment. To monitor multiple plants, additional sensors are recommended.

15\. **What makes the PLT-1 better than other plant sensors?**

* The PLT-1 pairs a durable capacitive soil moisture sensor with real-time reporting of several environmental factors, all in one compact device that works with Homey on your local network.

16\. **Is the PLT-1 compatible with other smart home platforms?**

* Yes. Besides Homey (through the Apollo Automation app), the PLT-1 works with Home Assistant, and it may work with other platforms through the <a href="https://esphome.io/components/api.html" target="_blank" rel="noreferrer nofollow noopener">ESPHome API</a> or MQTT. See [Supported platforms](../../general/supported-platforms/).

17\. **Do I need coding knowledge to use the PLT-1?**

* No. Adding the PLT-1 to Homey and building flows takes no code. YAML knowledge only matters if you want to customize the firmware with ESPHome.

18\. **Can I access data from the PLT-1 remotely?**

* Yes. The PLT-1 reports to your Homey over your local network, and the Homey app shows its readings wherever you are, as long as your Homey is reachable remotely.

19\. **Can I use multiple PLT-1 sensors with one Homey?**

* Yes. Add each PLT-1 with the Apollo Automation app. Each one shows up as its own device in Homey, so you can monitor several plants or spaces.

20\. **Optional Probe Addons:**

* 1\.5m (~5ft) Waterproof Flat Cable (DS18B20) – -55°C to 85°C (-67°F to 185°F), ±0.5°C accuracy. Ideal for fridges, freezers, fish tanks etc.

* 20cm (~8in) Waterproof Flat Cable (DS18B20) – -55°C to 85°C (-67°F to 185°F), ±0.5°C accuracy.
