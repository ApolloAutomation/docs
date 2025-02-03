# **TEMP-1 FAQ**

1\. **How is the TEMP-1 powered?**

* The TEMP-1 operates with USB-C at 5volts using less than 1 amp of power.

2\. **What are the Optional Probe Addons?**

* 1\.5m (~5ft) Waterproof Flat Cable (DS18B20) – -55°C to 85°C (-67°F to 185°F), ±0.5°C accuracy. Ideal for fridges, freezers, fish tanks etc.

* 20cm (~8in) Waterproof Flat Cable (DS18B20) – -55°C to 85°C (-67°F to 185°F), ±0.5°C accuracy.

* 1m (~3ft) Stainless Steel Food-Safe Probe (NTC) – Max 350°C (662°F). Perfect for grilling, baking, and food prep (not dishwasher safe).

3\. **Is the TEMP-1 weatherproof? Can I use it outdoors?**

* The TEMP-1 is primarily designed for indoor use, but components like the waterproof soil probe are suited for harsh conditions. The main body is not rated for outdoor use without additional protection.

4\. **How does the TEMP-1 connect to Home Assistant?**

* The TEMP-1 connects via WiFi to ESPHome on Home Assistant, enabling data monitoring, automations, and alerts directly within Home Assistant.

5\. **How often does the TEMP-1 send sensor data?**

* The TEMP-1’s reporting frequency is adjustable in ESPHome but most things default to 60seconds. You can set it for frequent updates or extend intervals to conserve battery life.

6\. **Can I customize the TEMP-1 functionality?**

* Absolutely! With ESPHome, users can modify firmware, settings, and even print custom cases for the PLT-1B. Our <a href="https://github.com/ApolloAutomation/PLT-1" target="_blank" rel="noreferrer nofollow noopener">YAML is on Github</a> and our <a href="https://www.printables.com/@Apollo_1187039" target="_blank" rel="noreferrer nofollow noopener">.STEP and .STL CAD files</a> are available for community use.

7\. **What are the RGB LED and piezo buzzer used for?**

* The RGB LED provides visual alerts, while the <a href="https://wiki.apolloautomation.com/products/general/piezo/" title="Click here to go to the piezo buzzer wiki tutorial" target="_blank" rel="noreferrer nofollow noopener">piezo buzzer offers audio notifications</a> for events like low moisture levels or high UV exposure.

8\. **Is the TEMP-1 compatible with other smart home platforms?**

* While designed for Home Assistant via ESPHome, it may be compatible with other platforms using the <a href="https://esphome.io/components/api.html" target="_blank" rel="noreferrer nofollow noopener">ESPHome API</a> or MQTT.

9\. **Do I need coding knowledge to use the TEMP-1?**

* Basic knowledge of Home Assistant and ESPHome is helpful, but most users can utilize it out of the box. For advanced customization, YAML knowledge is recommended.

10\. **Can I access data from the TEMP-1 remotely?**

* Yes, you can access sensor data remotely via the Home Assistant dashboard if your setup is configured for remote access.

11\. **What’s the difference between the battery and non-battery versions?**

* The TEMP-1B is battery-operated and slightly larger, while the non-battery (NB) version is compact and connects directly to a USB-C power source.

12\. **Can I use multiple TEMP-1 sensors in one Home Assistant setup?**

* Yes, you can add multiple TEMP-1 sensors, each appearing as a separate device, for comprehensive monitoring across multiple plants or spaces.