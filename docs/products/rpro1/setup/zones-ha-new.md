---
title: R PRO-1 Home Assistant zone configuration
description: Enter X and Y coordinates for the R PRO-1's LD2450 zones directly in Home Assistant, then tune the optional LD2412.
---
# How to tune the R PRO-1 using Home Assistant

!!! info "Your R PRO-1 has two mmWave sensors that both need to be tuned"

    The Apollo R PRO-1 comes with an LD2450 mmWave sensor and an optional secondary LD2412 mmWave sensor.

    The LD2450 tracks up to three targets in up to three zones, but can have issues with "still detection".

    The optional LD2412 mmWave sensor gives you perfect still detection for one target at up to 9 meters, so it's a great addition to the sensor.

## LD2450 configuration

You can enter the X and Y coordinates for each LD2450 zone manually in Home Assistant, or directly on the device's web page by visiting its IP address or hostname.local. The steps below set up your zones in Home Assistant.

!!! tip "Prefer a phone app?"

    It's much easier to tune using the [HLK Radartool App](zones-hlk.md), and we suggest using that to set up your LD2450 instead.

!!! tip "Drawing zones with the Apollo mmWave dashboard?"

    Skip these steps and leave **LD2450 Zone Type** on **Disabled**. The dashboard's [zone map](apollo-mmwave-dashboard.md#draw-zones-on-the-r-pro-1-and-mtr-1) replaces the radar's built-in zones. On **Detection**, the radar reports only people inside the zones you enter here, and with none set it reports nobody, so the map stays empty.

1\. Go to **Settings → Devices & services**, open the <a href="http://homeassistant.local:8123/config/integrations/integration/esphome" target="_blank" rel="noopener">ESPHome integration</a>, and click the name of your new device.

2\. Scroll down until you see **LD2450 Zone Type** and choose **Detection** from the drop-down menu.

![LD2450 Zone Type dropdown in Home Assistant with Detection selected](/assets/r-pro-1-select-detection.png)

3\. Enter the X and Y coordinates for each zone.

![LD2450 zone coordinate fields in Home Assistant, each entered in millimeters](/assets/r-pro-1-enter-zone-coordinates-manually.png)

!!! tip "Helpful hints for understanding LD2450 zones"

    * X1 must always be less than X2, and Y1 must always be less than Y2.
    * The Y axis is simpler, since it's never negative.
    * The X axis is where you can get tripped up, especially when both values are negative: -3456 is less than -2345.
    * If you use the Plotly chart from the [main R PRO-1 zone page](zones-ha.md), it still draws the rectangles even if the X1/X2 and Y1/Y2 values are reversed, so check the order yourself.
    * Zones can't overlap.

Your LD2450 now detects targets in the zones you entered.

## LD2412 configuration

To tune the optional LD2412, follow the [LD2412 Configuration](zones-ha.md#ld2412-configuration) steps on the main R PRO-1 Home Assistant zone page.
