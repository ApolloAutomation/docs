---
title: MSR-2 Home Assistant Zone Configuration
description: Tutorial for R-Pro-1 Home Assistant Zone Configuration.
---
# How To Tune The R-PRO-1 Using Home Assistant

!!! info "Your R-PRO-1 has two unique mmWave sensors that both need to be tuned!"

    The R-PRO-1 comes with an LD2450 mmwave sensor and an optional secondary LD2412 mmWave sensor.

    The LD2450 allows for up to three targets tracked in up to three zones but can have issues with "still detection".

    The optional LD2412 mmWave sensor allows you to have perfect still detection for one target at up to 9 meters so it's a great addition to the sensor.

###### LD2450 Configuration

You can manually enter in the X and Y coordinates for each zone in Home Assistant or directly from the device's webserver by visiting the IP address or hostname.local. We find it much easier to tune using the HLK Radartool App and suggest using that to set up your LD2450!

1\. Navigate to the ESPHome integration by going to settings -&gt; <a href="http://homeassistant.local:8123/config/integrations/integration/esphome" target="_blank" rel="noopener">esphome integration</a> -&gt; click on the name of your new device!

2\. Scroll down until you see "LD2450 Zone Type" and choose "Detection" from the drop-down menu.

![](../../../assets/r-pro-1-select-detection.png)

3\.

###### LD2412 Configuration

&nbsp;