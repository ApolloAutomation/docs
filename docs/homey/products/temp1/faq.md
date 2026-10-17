---
title: TEMP-1 FAQ
description: "Answers to common questions about the TEMP-1 temperature sensor with Homey: power, probes, connecting to Homey, the out-of-range alarm, and reporting."
---
# TEMP-1 FAQ

1\. **How is the TEMP-1 powered?**

* The TEMP-1 operates with USB-C at 5volts using less than 1 amp of power.

2\. **What are the Optional Probe Addons?**

* 1\.5m (~5ft) Waterproof Flat Cable (DS18B20) -55°C to 85°C (-67°F to 185°F), ±0.5°C accuracy. Ideal for fridges, freezers, fish tanks etc.
* 20cm (~8in) Waterproof Flat Cable (DS18B20) -55°C to 85°C (-67°F to 185°F), ±0.5°C accuracy.
* 1m (~3ft) Stainless Steel Food-Safe Probe (NTC) – Max 350°C (662°F). Perfect for grilling, baking, and food prep (not dishwasher safe).

Sensor Interface: Equipped with a 3.5mm jack for connecting optional external temperature probes (sold separately). Compatible probe options include:<br>\- 1.5m (~5ft) waterproof flat cable (DS18B20 sensor). Max 85°C 185°F<br>\- 20cm (~8in) waterproof flat cable (DS18B20 sensor). Max 85°C 185°F<br>\- 1m (~3ft) stainless steel food-safe probe (NTC sensor). Max 350°C 662°F **Not dishwasher safe**

3\. **Is the TEMP-1 weatherproof? Can I use it outdoors?**

* The TEMP-1 is primarily designed for indoor use, but the optional waterproof DS18B20 probes are suited for harsh conditions. The main body is not rated for outdoor use without additional protection.

4\. **How does the TEMP-1 connect to Homey?**

* The TEMP-1 joins your Wi-Fi, and the Apollo Automation app for Homey talks to it directly over your local network through the ESPHome native API, with no cloud account. Once you add it, its readings show up on the device in Homey, ready for flows and Insights. The app runs on Homey Pro; Homey Cloud isn't supported.

!!! success "Next step: add your TEMP-1 to Homey"

    Connect the sensor to your Wi-Fi through its hotspot, then add it with the Apollo Automation app. The getting started guide walks you through both.

    [Get started with Homey](../setup/getting-started-temp1/){ .md-button .md-button--primary }

5\. **How often does the TEMP-1 send sensor data?**

* Most TEMP-1 readings, including the temperature probe, update every 60 seconds by default. The interval is set in the sensor's firmware, and Homey has no setting for it, so changing it means editing the firmware with ESPHome.

6\. **Can I customize the TEMP-1 functionality?**

* Absolutely! With ESPHome, users can modify firmware, settings, and even print custom cases for the TEMP-1. Our <a href="https://github.com/ApolloAutomation/TEMP-1" target="_blank" rel="noreferrer nofollow noopener">YAML is on GitHub</a> and our <a href="https://www.printables.com/@Apollo_1187039" target="_blank" rel="noreferrer nofollow noopener">.STEP and .STL CAD files</a> are available for community use.

7\. **What are the RGB LED and piezo buzzer used for?**

* The RGB LED is the TEMP-1's light in Homey. Turn it on or off, dim it, or change its color from the device or in a flow.
* The piezo buzzer sounds an alarm on its own when the probe temperature goes outside a range you set. In the device's **Settings** in the Homey app, set **Minimum probe temperature** and **Maximum probe temperature** (in °C), then check **Alarm when temperature outside configured range**. The alarm watches the probe chosen in **Select probe**. Homey flows can't play the buzzer themselves.

!!! tip "The alarm checkbox is listed under TEMP PRO-1"

    **Alarm when temperature outside configured range** sits in the group **Temperature range and alarm settings for TEMP PRO-1**, but it works on the TEMP-1 too. The minimum and maximum are under **Probes and offsets for TEMP-1 and TEMP-1B**. For a full walkthrough, see [TEMP-1 alert outside a temperature range](../examples/temp1-alert-example/).

8\. **Is the TEMP-1 compatible with other smart home platforms?**

* Yes. Besides Homey (through the Apollo Automation app), the TEMP-1 works with Home Assistant, and it may work with other platforms through the <a href="https://esphome.io/components/api.html" target="_blank" rel="noreferrer nofollow noopener">ESPHome API</a> or MQTT. See [Supported platforms](../../general/supported-platforms/).

9\. **Do I need coding knowledge to use the TEMP-1?**

* No. Adding the TEMP-1 to Homey and building flows takes no code. YAML knowledge only matters if you want to customize the firmware with ESPHome.

10\. **Can I access data from the TEMP-1 remotely?**

* Yes. The TEMP-1 reports to your Homey over your local network, and the Homey app shows its readings wherever you are, as long as your Homey is reachable remotely.

11\. **What’s the difference between the battery and non-battery versions?**

* The TEMP-1B is battery-operated and slightly larger, while the non-battery (NB) version is compact and connects directly to a USB-C power source.

12\. **Can I use multiple TEMP-1 sensors with one Homey?**

* Yes. Add each TEMP-1 with the Apollo Automation app. Each one shows up as its own device in Homey, so you can monitor several rooms or spaces at the same time.
