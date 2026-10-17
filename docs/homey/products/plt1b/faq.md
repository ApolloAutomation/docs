---
title: PLT-1B FAQ
description: "Answers to common questions about the PLT-1B battery plant sensor with Homey: sensors, battery, connecting to Homey, flows, and sleep settings."
---
# PLT-1B FAQ

1\. **What sensors are included in the PLT-1B?**

* The PLT-1B comes with sensors to measure soil moisture, air temperature, humidity, LUX, and UV. There is also an optional DS18b20 waterproof soil temperature probe available for measuring soil temperature.

2\. **How does the capacitive soil moisture sensor work?**

* The capacitive soil moisture sensor measures the water content in the soil by detecting changes in the dielectric permittivity of the soil, which is affected by moisture. It’s more durable than resistive sensors because it doesn’t corrode and is protected with a conformal coating.

3\. **How is the PLT-1B powered?**

* The PLT-1B operates with a **rechargeable** 18650 Flat Top battery (not included), giving it portability for plant monitoring without being tied to an outlet. Example battery to use: [https://imrbatteries.com/products/samsung-30q-18650-3000mah-15a-battery](https://imrbatteries.com/products/samsung-30q-18650-3000mah-15a-battery).

4\. **Can you charge the battery by plugging in the device?**

* No, you cannot charge the battery through the USB port. You need an external 18650 charger such as a <a href="https://imrbatteries.com/products/nitecore-sc2-2-channel-battery-charger" target="_blank" rel="noreferrer nofollow noopener">nitecore 2 or 4 bay</a>.

5\. **How long does the battery last in the PLT-1B?**

* Battery life depends on sleep/wake intervals. Waking every 8 hours provides around 6 months of battery life, and waking every 12 hours or more can extend it to about a year.

6\. **How does the optional soil temperature probe work?**

* The optional DS18b20 probe (20 cm / 7.8 inches) measures soil temperature directly, providing critical data for plants that need specific temperature conditions.

7\. **Is the PLT-1B weatherproof? Can I use it outdoors?**

* The PLT-1B is primarily designed for indoor use, but components like the waterproof soil probe are suited for harsh conditions. The main body is not rated for outdoor use without additional protection.

8\. **How does the PLT-1B connect to Homey?**

* The PLT-1B joins your Wi-Fi, and the Apollo Automation app for Homey talks to it directly over your local network through the ESPHome native API, with no cloud account. Once you add it, its readings show up on the device in Homey, ready for flows and Insights. The app runs on Homey Pro; Homey Cloud isn't supported.

!!! success "Next step: add your PLT-1B to Homey"

    Connect the sensor to your Wi-Fi through its hotspot, then add it with the Apollo Automation app. The getting started guide walks you through both.

    [Get started with Homey](../setup/getting-started-plt1/){ .md-button .md-button--primary }

9\. **What kind of flows can I set up with the PLT-1B?**

* Any PLT-1B reading can start a flow in Homey. For example, send a notification when soil moisture drops, turn on a grow light when the light level falls, or adjust your heating or cooling based on the air temperature and humidity around your plants.

10\. **How often does the PLT-1B send sensor data?**

* A new PLT-1B ships with **Prevent sleep** checked, so it stays awake and reports most readings every 60 seconds. That drains the battery fast. Once you uncheck Prevent sleep, the PLT-1B wakes up, sends all its readings to Homey, and goes back to sleep to save battery. How long it sleeps is the **Sleep duration** setting, in hours (12 by default). Both settings are under **Battery settings (if battery is present)** in the device's **Settings** in the Homey app. A shorter sleep gives fresher readings and a shorter battery life. See [Prevent sleep](../setup/prevent-sleep/) for the details.

!!! tip "Change settings while the PLT-1B is awake"

    Homey can only send a setting while the sensor is awake and connected. If it's asleep, Homey shows **The device is asleep. Settings can be changed when it next wakes up.** [Keep the sensor awake](../setup/prevent-sleep/#keep-your-plt-1b-awake-again) and try again.

11\. **Can I customize the PLT-1B functionality?**

* Absolutely! With ESPHome, users can modify firmware, settings, and even print custom cases for the PLT-1B. Our <a href="https://github.com/ApolloAutomation/PLT-1" target="_blank" rel="noreferrer nofollow noopener">YAML is on GitHub</a> and our <a href="https://www.printables.com/@Apollo_1187039" target="_blank" rel="noreferrer nofollow noopener">.STEP and .STL CAD files</a> are available for community use.

12\. **What are the RGB LED and piezo buzzer used for?**

* The RGB LED is the PLT-1B's light in Homey. Turn it on or off, dim it, or change its color from the device or in a flow, for example to glow red when the soil gets dry. Commands reach the sensor only while it's awake.
* The piezo buzzer is played through an ESPHome action, and the Apollo Automation app has no flow card for it, so Homey can't sound the buzzer. If you also run Home Assistant, it can: see the [piezo buzzer guide](../../../../products/general/piezo/).

13\. **What is the benefit of using a conformal coating on the soil moisture sensor?**

* The conformal coating protects the sensor from moisture-related degradation, improving its lifespan and durability.

14\. **What plants are compatible with the PLT-1B?**

* The PLT-1B works with all kinds of indoor plants. Look up the light, humidity, and soil moisture your plant likes, then use those values as thresholds in your Homey flows, so you hear about it when a reading drifts out of range.

15\. **Can I monitor multiple plants with one PLT-1B?**

* The PLT-1B is designed to monitor a single plant’s environment. To monitor multiple plants, additional sensors are recommended.

16\. **What makes the PLT-1B better than other plant sensors?**

* The PLT-1B pairs a durable capacitive soil moisture sensor with real-time reporting of several environmental factors, all in one compact, battery-powered device that works with Homey on your local network.

17\. **Is the PLT-1B compatible with other smart home platforms?**

* Yes. Besides Homey (through the Apollo Automation app), the PLT-1B works with Home Assistant, and it may work with other platforms through the <a href="https://esphome.io/components/api.html" target="_blank" rel="noreferrer nofollow noopener">ESPHome API</a> or MQTT. See [Supported platforms](../../general/supported-platforms/).

18\. **Do I need coding knowledge to use the PLT-1B?**

* No. Adding the PLT-1B to Homey and building flows takes no code. YAML knowledge only matters if you want to customize the firmware with ESPHome.

19\. **Can I access data from the PLT-1B remotely?**

* Yes. The PLT-1B reports to your Homey over your local network, and the Homey app shows its latest readings wherever you are, as long as your Homey is reachable remotely.

20\. **What’s the difference between the battery and non-battery versions?**

* The PLT-1B is battery-operated (18650) and slightly larger, while the non-battery (NB) version is compact and requires USB-C power at 5 volts using 1amp or less (5W). They both have all of the same components for measuring soil moisture, air temp/humidity, lux/uv, etc.

21\. **Can I use multiple PLT-1B sensors with one Homey?**

* Yes. Add each PLT-1B with the Apollo Automation app. Each one shows up as its own device in Homey, so you can monitor several plants or spaces.

22\. **Optional Probe Addons:**

* 1\.5m (~5ft) Waterproof Flat Cable (DS18B20) – -55°C to 85°C (-67°F to 185°F), ±0.5°C accuracy. Ideal for fridges, freezers, fish tanks etc.
* 20cm (~8in) Waterproof Flat Cable (DS18B20) – -55°C to 85°C (-67°F to 185°F), ±0.5°C accuracy.
