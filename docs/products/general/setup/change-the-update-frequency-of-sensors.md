---
title: How To Change The Update Frequency Of Sensors
description: Tutorial for How To Change The Update Frequency Of Sensors.
---

# How To Change The Update Frequency Of Sensors

You change how often a sensor updates by adding a few lines of YAML to your device in ESPHome Builder, then installing the update.

1\. Select the ESPHome Builder in the sidebar then click "EDIT" on the device you want to change. If it isn't in your sidebar, the button below opens the app.

[![Open your Home Assistant instance and show the dashboard of an app.](https://my.home-assistant.io/badges/supervisor_app.svg)](https://my.home-assistant.io/redirect/supervisor_app/?app=5c53de3b_esphome&repository_url=https%3A%2F%2Fgithub.com%2Fesphome%2Fhome-assistant-addon)

![ESPHome Builder in the Home Assistant sidebar with the Edit button on an AIR-1 card outlined](/assets/update-frequency-pic-1.png)

2\. Insert the YAML for the sensor you want to edit (The example below is for our AIR-1 SEN55 sensor).

```yaml
sensor:
  - platform: sen5x
    id: !extend sen55
    update_interval: 5s
```

!!! tip "You might also want to add force_update: true to make your sensor show the frequent updates in the gui."

    **force\_update** (*Optional*, boolean): If true, this option will force the frontend (usually Home Assistant) to create a state changed event when the sensor updates even if the value stayed the same. Some applications like Grafana require this when working with Home Assistant, but beware it can significantly increase the database size. Defaults to `false`.

3\. In the top right of the same screen click "SAVE" and then "INSTALL".

4\. Once you see "INFO OTA successful" you are done. Click "STOP" to exit.

![ESPHome Device Builder install log with INFO OTA successful and the Stop button circled](/assets/update-frequency-pic-3.png)