---
title: R-PRO-1 General Tips
description: >-
  Multiple helpful images for mounting, lux/rgb, and gate and zone
  visualization.
---
# General Tips

##### **Light Sensor (LTR-390UV)**

![20240514_123742.jpg](../../../assets/rpro-ltr-390.jpg)

The R-PRO-1 doesn't have any slits on the front of the case, so UV rays can't directly reach the sensor for UV detection. However, light can still enter from around the edges or behind the front panel, allowing the lux readings to spike when ambient light is present.

!!! warning "The RGB LED will trigger the Light sensor!"

    Make sure that your automations do not interfere with each other. This includes being aware that your onboard LED can trigger the lux reading but not the uv reading of the LTR390 in your device.

##### **Wall Mounting**

The R-PRO-1 should be mounted 1.5-2 meters off the ground which will then provide a nice even 120degree FOV of the mmWave radar.

![ld2410_mounting_hor-1.jpeg](../../../assets/ld2412-wall-mount-radar-cone.png)

##### **Ceiling Mounting**

The R-PRO-1 should be mounted 2.6-3 meters (8-10 feet) high when mounted on the ceiling using our ceiling mount kit.

![LD2410 Gates.png](../../../assets/ld2412-ceiling-mount-radar-cone.png)

!!! tip "These are some useful hints!"

    * The FOV angle is -60 to 60 degrees - 120 degrees total.
    * Gates are pre-defined by the radar module and are in 0.75 meter increments.
    * Zones are user-configurable and are in cm.

##### **Gate Visualization**

**![ld2410 table.png](../assets/ld2410-table.png)![Gate, Zones and RR.png](../assets/gate-zones-and-rr.png)**

![MSR-1 radar map.png](../assets/msr-1-radar-map.png)![Radar gates Colored.png](../assets/radar-gates-colored.png)

#####