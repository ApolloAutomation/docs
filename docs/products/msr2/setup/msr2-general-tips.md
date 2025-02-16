# General Tips

##### **Light Sensor (LTR-390UV)**

![20240514_123742.jpg](../assets/20240514-123742.jpg)

When mounting the MSR-2 be sure to position the device so that the two large holes are not covered. This allows more light to enter and will ensure better accuracy

!!! warning "The RGB LED will trigger the Light sensor!"

    Make sure that your automations do not interfere with each other. This includes being aware that your onboard LED can trigger the lux reading but not the uv reading of the LTR390 in your device.

##### **Mounting**

The MSR-2 should be mounted 1.5-2 meters off the ground which will then provide a nice even 120degree FOV of the mmWave radar.

![LD2410 Gates.png](../assets/ld2410-gates.png)![ld2410_mounting_hor-1.jpeg](../assets/ld2410-mounting-hor-1.jpeg)

##### **Gate and FOV Visualization**

**![ld2410 table.png](../assets/ld2410-table.png)![Gate, Zones and RR.png](../assets/gate-zones-and-rr.png)**

!!! tip "These are some useful hints!"

    * The FOV angle is -60 to 60 degrees - 120 degrees total.
    * Gates are pre-defined by the radar module and are in 0.75 meter increments.
    * Zones are user-configurable and are in cm.

![MSR-1 radar map.png](../assets/msr-1-radar-map.png)![Radar gates Colored.png](../assets/radar-gates-colored.png)

#####