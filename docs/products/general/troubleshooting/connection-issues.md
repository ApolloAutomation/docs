---
title: Connection Issues
description: Suggestions for Connection Issues
---
1\. Try a couple of different power cord and power brick combinations - this matters a lot more than you'd think!

2\. Check to see if the sensor's hotspot is showing up. (this means it is not connected to a network)

3\. Check the router's connected devices - the device will show up with the Apollo name and a 6 digit hex value of the end of the mac address.

4\. Disable [power save mode](https://esphome.io/components/wifi.html#power-save-mode) in ESPHome. (See directions below)

# Wi-Fi Power Save Mode

The Wi-Fi interface of all ESPs offers three power save modes to reduce the amount of power spent on Wi-Fi. While some options *can* reduce the power usage of the ESP, they generally also decrease the reliability of the Wi-Fi connection, with frequent disconnections from the router in the highest power saving mode.

* `NONE` (least power saving, Default for ESP8266)
* `LIGHT` (Default for ESP32)
* `HIGH` (most power saving)

```yaml
wifi:
  # ...
  power_save_mode: none
```

1\. Select the ESPHome app and then select Edit under your desired device. If it isn't in your sidebar, the button below opens the app.

[![Open your Home Assistant instance and show the dashboard of an app.](https://my.home-assistant.io/badges/supervisor_app.svg)](https://my.home-assistant.io/redirect/supervisor_app/?app=5c53de3b_esphome&repository_url=https%3A%2F%2Fgithub.com%2Fesphome%2Fhome-assistant-addon)

![ESPHome in the Home Assistant sidebar and the Edit button on an MSR-2 card circled](/assets/screenshot-2024-10-25-at-5-14-48-pm.png)

2\.  Add the code below to your device's yaml file. Then select Save and press Install.

```yaml
power_save_mode: none
```

![MSR-2 YAML with power_save_mode: none added under wifi and the Save and Install buttons circled](/assets/screenshot-2024-10-25-at-5-25-10-pm.png)

3\. Now your device should have a stronger connection. (This will cause the sensor's internal temperature to increase.)