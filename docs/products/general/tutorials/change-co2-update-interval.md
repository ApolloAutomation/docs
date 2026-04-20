---
title: How to edit your Sensor's CO2 update interval
description: How to edit your Sensor's CO2 update interval
---
# How to edit your Sensor's CO2 update interval

This guide will show you how to edit the CO<sub>2</sub> updates down to 5 seconds, which is the fastest the SCD40 sensor supports. This is useful for use-cases that benefit from smoother graphs or quicker reaction to CO<sub>2</sub> changes, such as grow rooms, offices, or sleep spaces.

!!! tip "Your sensor is defaulting to 60 seconds for updates to the state of the CO<sub>2</sub> sensor."

    This is the default for all esphome devices using the SCD40 because it uses less Wi-Fi airtime fairness and writes less to your Home Assistant Database. 5 seconds is the minimum. The SCD40 hardware cannot produce a new reading faster than that.

!!! note "Sensor response time"

    Even at a 5 second update interval, the SCD40 itself takes roughly 90 seconds to fully reflect a real change in CO<sub>2</sub> levels in the air. The number on your dashboard will refresh every 5 seconds, but a true spike (for example, someone walking into the room) will ramp in over a couple of minutes. That is normal sensor behavior, not a configuration issue. See the [Sensirion SCD4x datasheet](https://sensirion.com/media/documents/48C4B7FB/67FE0194/CD_DS_SCD4x_Datasheet_D1.pdf) for full specs.

1\. Select the <a href="https://wiki.apolloautomation.com/products/general/setup/getting-started/#connecting-to-esphome-device-builder" target="_blank" rel="noreferrer nofollow noopener">ESPHome Builder</a> in the sidebar then click "EDIT" on the device you want to change.

![image.png](/assets/update-frequency-pic-1.png)

2\. Copy this code and enter it just like shown in the next step. Make sure there are no extra spaces or any other characters. It needs to look just like the example in the next step.

```yaml
#CO2 sensor update interval
sensor:
  - platform: scd4x
    id: !extend scd40
    update_interval: 5s
```

3\. Paste the code you copied in step 2 below your sensor's existing yaml.

4\. In the top right of the same screen click "SAVE" and then "INSTALL".

5\. Once you see "INFO OTA successful" you are done. Click "STOP" to exit.

![](/assets/update-frequency-pic-3.png)

6\. Once that is finished your sensor should now be reporting CO<sub>2</sub> at your new update\_interval such as 5 seconds!
