# **TEMP-1B FAQ**

1\.**How is the TEMP-1B powered?**

* The TEMP-1B operates with a **rechargeable** 16340 Flat Top battery (not included), giving it portability for temp monitoring without being tied to an outlet.

2\. **How long does the battery last in the TEMP-1B?**

* Battery life depends on sleep/wake intervals. Waking every 12 hours provides around 3 months of battery life.

3\. **Is the TEMP-1B weatherproof? Can I use it outdoors?**

* The TEMP-1B is primarily designed for indoor use, but components like the waterproof soil probe are suited for harsh conditions. The main body is not rated for outdoor use without additional protection.

4\. **How does the TEMP-1B connect to Home Assistant?**

* The TEMP-1B connects via WiFi to ESPHome on Home Assistant, enabling data monitoring, automations, and alerts directly within Home Assistant.

5\. **How often does the TEMP-1B send sensor data?**

* The TEMP-1B’s reporting frequency is adjustable in ESPHome but most things default to 60seconds. You can set it for frequent updates or extend intervals to conserve battery life.

6\. **What is the RGB LED and piezo buzzer used for?**

* The RGB LED provides visual alerts, while the piezo buzzer offers audio notifications for events like low temp levels or high temp levels.

7\. **Is the TEMP-1B compatible with other smart home platforms?**

* While designed for Home Assistant via ESPHome, it may be compatible with other platforms using the <a href="https://esphome.io/components/api.html" target="_blank" rel="noreferrer nofollow noopener">ESPHome API</a> or MQTT.

8\.**Do I need coding knowledge to use the TEMP-1B?**

* Basic knowledge of Home Assistant and ESPHome is helpful, but most users can utilize it out of the box. For advanced customization, YAML knowledge is recommended.

9\. **Can I access data from the TEMP-1B remotely?**

* Yes, you can access sensor data remotely via the Home Assistant dashboard if your setup is configured for remote access.

10\. **What’s the difference between the battery and non-battery versions?**

* The TEMP-1B is battery-operated and slightly larger, while the non-battery (NB) version is compact and connects directly to a power source.

11\. **Can I use multiple TEMP-1B sensors in one Home Assistant setup?**

* Yes, you can add multiple TEMP-1B sensors, each appearing as a separate device, for comprehensive monitoring across multiple plants or spaces.

12\. **Can you charge the battery by plugging in the device?**

* No, you cannot charge the battery through the USB port. You need a separate 16340 charger.