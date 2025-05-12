---
title: TEMP Pro-1 FAQ
description: Frequently asked questions about the TEMP-1 Pro temperature sensor.
---
# **TEMP Pro-1 FAQ**

1\. **How is the TEMP Pro-1 powered?**

* PoE (IEEE 802.3-compliant) powered or...
* USB-C at 5volts using less than 1 amp of power.

2\. **What are the Optional Probe Addons?**

* 1\.5m (~5ft) Waterproof Flat Cable (DS18B20) -55°C to 85°C (-67°F to 185°F), ±0.5°C accuracy. Ideal for fridges, freezers, fish tanks etc.
* 20cm (~8in) Waterproof Flat Cable (DS18B20) -55°C to 85°C (-67°F to 185°F), ±0.5°C accuracy.
* 12\.7cm (~5 in) dust-proof temperature & humidity sensor with waterproof probe (<a href="https://wiki.dfrobot.com/SHT20_I2C_Temperature_%26_Humidity_Sensor__Waterproof_Probe__SKU__SEN0227" target="_blank" rel="noreferrer nofollow noopener">SHT20</a>)

3\. **What other addons can I use with the TEMP Pro-1?**

* You can add the GPIO header and SCD40 CO2 sensor with the two mezzanine ports. It also includes a Sensirion port for a SEN55 and SEN6x, a QWIIC port and a DfRobot port.

3\. **Is the TEMP Pro-1 weatherproof? Can I use it outdoors?**

* The TEMP Pro-1 is primarily designed for indoor use, but components like the waterproof temp probe are suited for harsh conditions. The main body is not rated for outdoor use without additional protection.

4\. **How does the TEMP Pro-1 connect to Home Assistant?**

* The TEMP Pro-1 connects via WiFi to ESPHome on Home Assistant, enabling data monitoring, automations, and alerts directly within Home Assistant.

5\. **How often does the TEMP Pro-1 send sensor data?**

* The TEMP Pro-1 reporting frequency is adjustable in ESPHome but most things default to 60seconds. You can set it for frequent updates or extend intervals to conserve battery life.

6\. **Can I customize the TEMP Pro-1 functionality?**

* Absolutely! With ESPHome, users can modify firmware, settings, and even print custom cases for the TEMP Pro-1. Our <a href="https://github.com/ApolloAutomation/TEMP-1" target="_blank" rel="noreferrer nofollow noopener">YAML is on Github</a> and our <a href="https://www.printables.com/@Apollo_1187039" target="_blank" rel="noreferrer nofollow noopener">.STEP and .STL CAD files</a> are available for community use.

7\. **What are the RGB LED and piezo buzzer used for?**

* The RGB LED provides visual alerts, while the <a href="https://wiki.apolloautomation.com/products/general/piezo/" title="Click here to go to the piezo buzzer wiki tutorial" target="_blank" rel="noreferrer nofollow noopener">piezo buzzer offers audio notifications</a> for events like low moisture levels or high UV exposure.

8\. **Is the TEMP Pro-1 compatible with other smart home platforms?**

* While designed for Home Assistant via ESPHome, it may be compatible with other platforms using the <a href="https://esphome.io/components/api.html" target="_blank" rel="noreferrer nofollow noopener">ESPHome API</a> or MQTT.

9\. **Do I need coding knowledge to use the TEMP Pro-1?**

* Basic knowledge of Home Assistant and ESPHome is helpful, but most users can utilize it out of the box. For advanced customization, YAML knowledge is recommended.

10\. **Can I access data from the TEMP Pro-1 remotely?**

* Yes, you can access sensor data remotely via the Home Assistant dashboard if your setup is configured for remote access.

11\. **Can I use multiple TEMP Pro-1 sensors in one Home Assistant setup?**

* Yes, you can add multiple TEMP-1 sensors, each appearing as a separate device, for comprehensive monitoring across multiple plants or spaces.