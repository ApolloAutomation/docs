---
title: TEMP-1B FAQ
description: "Answers to common questions about the TEMP-1B battery temperature sensor with Homey: battery, probes, connecting to Homey, sleep settings, and the out-of-range alarm."
---
# TEMP-1B FAQ

1\. **How is the TEMP-1B powered?**

* The TEMP-1B operates with a **rechargeable** <a href="https://apolloautomation.com/products/16340-rechargeable-battery" target="_blank" rel="noreferrer nofollow noopener">16340 Flat Top battery</a> (not included), giving it portability for temp monitoring without being tied to an outlet.

2\. **How long does the battery last in the TEMP-1B?**

* Battery life depends on sleep/wake intervals. Waking every 12 hours provides around 6+ months of battery life.

3\. **Can you charge the battery by plugging in the device?**

* No, you cannot charge the battery through the USB port. You need a separate 16340 charger such as a <a href="https://imrbatteries.com/products/nitecore-sc2-2-channel-battery-charger" target="_blank" rel="noreferrer nofollow noopener">nitecore 2 or 4 bay</a>.

4\. **What are the Optional Probe Addons?**

* 1\.5m (~5ft) Waterproof Flat Cable (DS18B20) – -55°C to 85°C (-67°F to 185°F), ±0.5°C accuracy. Ideal for fridges, freezers, fish tanks etc.
* 20cm (~8in) Waterproof Flat Cable (DS18B20) – -55°C to 85°C (-67°F to 185°F), ±0.5°C accuracy.
* 1m (~3ft) Stainless Steel Food-Safe Probe (NTC) – Max 350°C (662°F). Perfect for grilling, baking, and food prep (not dishwasher safe).

5\. **Is the TEMP-1B weatherproof? Can I use it outdoors?**

* The TEMP-1B is primarily designed for indoor use, but the waterproof DS18B20 temperature probes are suited for harsh conditions. The main body is not rated for outdoor use without additional protection.

6\. **How does the TEMP-1B connect to Homey?**

* The TEMP-1B joins your Wi-Fi, and the Apollo Automation app for Homey talks to it directly over your local network through the ESPHome native API, with no cloud account. Once you add it, its readings show up on the device in Homey, ready for flows and Insights. The app runs on Homey Pro; Homey Cloud isn't supported.

!!! success "Next step: add your TEMP-1B to Homey"

    Connect the sensor to your Wi-Fi through its hotspot, then add it with the Apollo Automation app. The getting started guide walks you through both.

    [Get started with Homey](../setup/getting-started-temp1/){ .md-button .md-button--primary }

7\. **How often does the TEMP-1B send sensor data?**

* A new TEMP-1B ships with **Prevent sleep** checked, so it stays awake and reports most readings every 60 seconds. That drains the battery fast. Once you uncheck Prevent sleep, the TEMP-1B wakes up, sends its readings to Homey, and goes back to sleep to save battery. How long it sleeps is the **Sleep duration** setting, in hours (12 by default). Both settings are under **Battery settings (if battery is present)** in the device's **Settings** in the Homey app. A shorter sleep gives fresher readings and a shorter battery life. See [Prevent sleep](../setup/prevent-sleep/) for the details.

!!! tip "Change settings while the TEMP-1B is awake"

    Homey can only send a setting while the sensor is awake and connected. If it's asleep, Homey shows **The device is asleep. Settings can be changed when it next wakes up.** [Keep the sensor awake](../setup/prevent-sleep/#keep-your-temp-1b-awake-again) and try again.

8\. **Can I customize the TEMP-1B’s functionality?**

* Absolutely! With ESPHome, users can modify firmware, settings, and even print custom cases for the TEMP-1B. Our <a href="https://github.com/ApolloAutomation/TEMP-1" target="_blank" rel="noreferrer nofollow noopener">YAML is on GitHub</a> and our <a href="https://www.printables.com/@Apollo_1187039" target="_blank" rel="noreferrer nofollow noopener">.STEP and .STL CAD files</a> are available for community use.

9\. **What are the RGB LED and piezo buzzer used for?**

* The RGB LED is the TEMP-1B's light in Homey. Turn it on or off, dim it, or change its color from the device or in a flow. Commands reach the sensor only while it's awake.
* The piezo buzzer sounds an alarm on its own when the probe temperature goes above or below a range you set. In the device's **Settings** in the Homey app, set **Minimum probe temperature** and **Maximum probe temperature** (in °C), then check **Alarm when temperature outside configured range**. The alarm watches the probe chosen in **Select probe**, and it checks each time the sensor is awake and takes a reading. Homey flows can't play the buzzer themselves.

!!! tip "The alarm checkbox is listed under TEMP PRO-1"

    **Alarm when temperature outside configured range** sits in the group **Temperature range and alarm settings for TEMP PRO-1**, but it works on the TEMP-1B too. The minimum and maximum are under **Probes and offsets for TEMP-1 and TEMP-1B**. For a full walkthrough, see [TEMP-1B alert outside a temperature range](../examples/temp1b-alert-example/).

10\. **Is the TEMP-1B compatible with other smart home platforms?**

* Yes. Besides Homey (through the Apollo Automation app), the TEMP-1B works with Home Assistant, and it may work with other platforms through the <a href="https://esphome.io/components/api.html" target="_blank" rel="noreferrer nofollow noopener">ESPHome API</a> or MQTT. See [Supported platforms](../../general/supported-platforms/).

11\. **Do I need coding knowledge to use the TEMP-1B?**

* No. Adding the TEMP-1B to Homey and building flows takes no code. YAML knowledge only matters if you want to customize the firmware with ESPHome.

12\. **Can I access data from the TEMP-1B remotely?**

* Yes. The TEMP-1B reports to your Homey over your local network, and the Homey app shows its latest readings wherever you are, as long as your Homey is reachable remotely.

13\. **What’s the difference between the battery and non-battery versions?**

* The TEMP-1B is battery-operated and slightly larger, while the non-battery (NB) version is compact and requires USB-C power at 5 volts using 1amp or less (5W). They both have the same components: a 3.5mm port for the waterproof temperature probe or the food probe, plus onboard air temperature and humidity.

14\. **Can I use multiple TEMP-1B sensors with one Homey?**

* Yes. Add each TEMP-1B with the Apollo Automation app. Each one shows up as its own device in Homey, so you can monitor several fridges, freezers, rooms, or other spaces.
