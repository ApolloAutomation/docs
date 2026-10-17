---
title: General Tips
description: "Placement and mounting tips for the MSR-1, including keeping the light sensor holes clear and stopping the RGB LED from skewing LUX readings."
---
# General Tips

## **MSR-1**

![MSR-1 circuit board with labeled parts: ESP32-C3 Mini, LD2410B radar, LTR-390UV, BME280, SCD-40, buzzer, and USB-C](/assets/apollo-automation-msr-1-presence-multisensor-pcb-components-layout-1024x768-jpg.webp)

Picture from <a href="https://smarthomescene.com/reviews/apollo-msr-1-review-miniature-multi-sensor-for-presence-and-co2-monitoring/" target="_blank" rel="noreferrer nofollow noopener">Smart Home Scene</a>

## **Light Sensor (LTR-390UV)**

![3D render of the MSR-1 case with the light sensor holes outlined in red](/assets/UWHlight-holes.png)

When mounting the MSR-1 be sure to position the device so that the two large holes are not covered. This allows more light to enter and will ensure better accuracy.

!!! warning "The RGB LED will trigger the Light sensor!"

    Make sure that your automations do not interfere with each other. This includes being aware that your onboard LED can trigger the lux reading but not the uv reading of the LTR390 in your device.

## **Mounting**

The MSR-1 should be mounted 1.5-2 meters off the ground which will then provide a nice even 120-degree FOV of the mmWave radar.

![LD2410 detection arcs for a wall mount at 1.5 to 2 m high and a ceiling mount at 2.6 to 3 m high](/assets/ld2410-gates.png)![Side-view diagram of radar coverage cones from a wall mount and a ceiling mount](/assets/ld2410-zone-map.png)

![HLK-LD2410B manual diagram of wall mounting at 1.5 to 2 m with a polar chart of detection range by angle](/assets/ld2410-mounting-hor-1.jpeg)

The MSR-1 can also be mounted on the ceiling if you can provide power and mount our articulating stand on the ceiling.

## **Gate and FOV Visualization**

**![Table of LD2410 gates 0 to 8 with distance ranges in meters and feet and default move and still thresholds](/assets/ld2410-gate-table.png)![Home Assistant radar settings with 0.75 m distance resolution and Zone 1, 2, and 3 distances in cm](/assets/gate-zones-and-rr.png)**

![Fan diagram of LD2410 gates G1 to G8, each 0.75 m deep, reaching 6 m (19.69 ft) from the sensor](/assets/ld2410-gate-map.png)![Radar gate fan diagram with Zone 1 in red, Zone 2 in blue, and Zone 3 in green](/assets/radar-gates-colored.png)

Each gate is 0.75 m deep, so the eight gates reach 6 m (19.69 ft) from the sensor.

!!! tip "These are some useful hints!"

    * The FOV angle is -60 to 60 degrees - 120 degrees total.
    * Gates are pre-defined by the radar module and are in 0.75 meter increments.
    * Zones are user-configurable and are in cm.