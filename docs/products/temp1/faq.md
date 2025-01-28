# **TEMP-1 FAQ**

1\. **How is the TEMP-1 powered?**

* The TEMP-1 operates with USB-C at 5volts using less than 1 amp of power.

2\. **Is the TEMP-1 weatherproof? Can I use it outdoors?**

* The TEMP-1 is primarily designed for indoor use, but components like the waterproof soil probe are suited for harsh conditions. The main body is not rated for outdoor use without additional protection.

3\. **How does the TEMP-1 connect to Home Assistant?**

* The TEMP-1 connects via WiFi to ESPHome on Home Assistant, enabling data monitoring, automations, and alerts directly within Home Assistant.

4\. **How often does the TEMP-1 send sensor data?**

* The TEMP-1’s reporting frequency is adjustable in ESPHome but most things default to 60seconds. You can set it for frequent updates or extend intervals to conserve battery life.

5\. **What is the RGB LED and piezo buzzer used for?**

* The RGB LED provides visual alerts, while the piezo buzzer offers audio notifications for events like low temp levels or high temp levels.

6\. **Is the TEMP-1 compatible with other smart home platforms?**

* While designed for Home Assistant via ESPHome, it may be compatible with other platforms using the <a href="https://esphome.io/components/api.html" target="_blank" rel="noreferrer nofollow noopener">ESPHome API</a> or MQTT.

7\. **Do I need coding knowledge to use the TEMP-1?**

* Basic knowledge of Home Assistant and ESPHome is helpful, but most users can utilize it out of the box. For advanced customization, YAML knowledge is recommended.

8\. **Can I access data from the TEMP-1 remotely?**

* Yes, you can access sensor data remotely via the Home Assistant dashboard if your setup is configured for remote access.

9\. **What’s the difference between the battery and non-battery versions?**

* The TEMP-1B is battery-operated and slightly larger, while the non-battery (NB) version is compact and connects directly to a USB-C power source.

10\. **Can I use multiple TEMP-1 sensors in one Home Assistant setup?**

* Yes, you can add multiple TEMP-1 sensors, each appearing as a separate device, for comprehensive monitoring across multiple plants or spaces.