---
title: MSR-2 general tips
description: Multiple helpful images for mounting, lux/rgb, and gate and zone visualization.
---
# General tips

## **Light sensor (LTR-390UV)**

![MSR-2 case with the light sensor visible through the center vent outlined in red](/assets/20240514-123742.jpg)

When mounting the MSR-2, position it so the center vent slots (outlined in red above) are not covered. This lets more light reach the sensor and keeps the readings accurate.

!!! warning "The RGB LED will trigger the Light sensor!"

    Make sure that your automations do not interfere with each other. This includes being aware that your onboard LED can trigger the lux reading but not the uv reading of the LTR390 in your device.

## **Mounting**

The MSR-2 should be mounted 1.5-2 meters off the ground which will then provide a nice even 120-degree FOV of the mmWave radar.

![HLK-LD2410B manual diagram of wall mounting at 1.5 to 2 m with a polar chart of detection range by angle](/assets/ld2410-mounting-hor-1.jpeg)

The MSR-2 can also be mounted on the ceiling if you can provide power and mount our articulating stand on the ceiling.

![LD2410 detection arcs for a wall mount at 1.5 to 2 m high and a ceiling mount at 2.6 to 3 m high](/assets/ld2410-gates.png)

!!! tip "These are some useful hints!"

    * The FOV angle is -60 to 60 degrees (120 degrees total).
    * Gates are pre-defined by the radar module and are in 0.75 meter increments.
    * Zones are user-configurable and are in cm.

## **Gate and FOV visualization**

**![Table of LD2410 gates 0 to 8 with distance ranges in meters and feet and default move and still thresholds](/assets/ld2410-gate-table.png)![Home Assistant radar settings with 0.75 m distance resolution and Zone 1, 2, and 3 distances in cm](/assets/gate-zones-and-rr.png)**

![Fan diagram of LD2410 gates G1 to G8, each 0.75 m deep, reaching 6 m (19.69 ft) from the sensor](/assets/ld2410-gate-map.png)![Fan diagram of LD2410 gates G1 to G8 grouped into example zones: Zone 1 (G1 to G2) in red, Zone 2 (G3 to G5) in blue, and Zone 3 (G6 to G8) in green, reaching 6 m](/assets/radar-gates-colored.png)

#####