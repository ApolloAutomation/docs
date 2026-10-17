---
title: General Tips
description: "Multiple helpful images for mounting, lux/rgb, and gate and zone visualization."
---
# General Tips

## **Light Sensor (LTR-390UV)**

![MSR-2 enclosure with the light sensor visible through the vent slots, outlined in red](/assets/20240514-123742.jpg)

When mounting the MSR-2, position it so the center vent slots (outlined in red above) are not covered. This lets more light reach the sensor and keeps the readings accurate.

!!! warning "The RGB LED will trigger the Light sensor!"

    Make sure that your automations do not interfere with each other. This includes being aware that your onboard LED can trigger the lux reading but not the uv reading of the LTR390 in your device.

## **Mounting**

The MSR-2 should be mounted 1.5-2 meters off the ground which will then provide a nice even 120degree FOV of the mmWave radar.

![HLK-LD2410B manual diagram of wall mounting at 1.5 to 2 m with a detection range chart by angle](/assets/ld2410-mounting-hor-1.jpeg)

The MSR-2 can also be mounted on the ceiling if you can provide power and mount our articulating stand on the ceiling.

![LD2410 diagrams for wall mounting at 1.5 to 2 m and ceiling mounting at 2.6 to 3 m](/assets/ld2410-gates.png)

!!! tip "These are some useful hints!"

    * The FOV angle is -60 to 60 degrees - 120 degrees total.
    * Gates are pre-defined by the radar module and are in 0.75 meter increments.
    * Zones are user-configurable and are in cm.

## **Gate and FOV Visualization**

**![Table of LD2410 gates 0 to 8 with distance ranges in meters and feet and default move and still thresholds](/assets/ld2410-gate-table.png)![Radar Distance Resolution set to 0.75m with Radar End Zone 1, 2, and 3 at 50, 100, and 200 cm](/assets/gate-zones-and-rr.png)**

![Fan diagram of LD2410 gates G1 to G8, each 0.75 m deep, reaching 6 m (19.69 ft) from the sensor](/assets/ld2410-gate-map.png)![Radar gate diagram with Zones 1, 2, and 3 shaded red, blue, and green over gates G1 to G7](/assets/radar-gates-colored.png)