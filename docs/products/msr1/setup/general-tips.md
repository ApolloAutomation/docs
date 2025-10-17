# General Tips

##### **MSR-1**

![apollo-automation-MSR-1-presence-multisensor-PCB-components-layout-1024x768.jpg.webp](../assets/apollo-automation-msr-1-presence-multisensor-pcb-components-layout-1024x768-jpg.webp)

Picture from <a href="https://smarthomescene.com/reviews/apollo-msr-1-review-miniature-multi-sensor-for-presence-and-co2-monitoring/" target="_blank" rel="noreferrer nofollow noopener">Smart Home Scene</a>

##### **Light Sensor (LTR-390UV)**

![Light holes.png](../assets/UWHlight-holes.png)

When mounting the MSR-1 be sure to position the device so that the two large holes are not covered. This allows more light to enter and will ensure better accuracy.

!!! warning "The RGB LED will trigger the Light sensor!"

    Make sure that your automations do not interfere with each other. This includes being aware that your onboard LED can trigger the lux reading but not the uv reading of the LTR390 in your device.

##### **Mounting**

The MSR-1 should be mounted 1.5-2 meters off the ground which will then provide a nice even 120degree FOV of the mmWave radar.

![LD2410 Gates.png](../assets/ld2410-gates.png)![LD2410 Zone map.png](../assets/ld2410-zone-map.png)

![ld2410_mounting_hor-1.jpeg](../assets/ld2410-mounting-hor-1.jpeg)

The MSR-1 can also be mounted on the ceiling if you can provide power and mount our articulating stand on the ceiling.

##### **Gate and FOV Visualization**

**![ld2410 table.png](../assets/ld2410-table_1.png)![Gate, Zones and RR.png](../assets/gate-zones-and-rr.png)**

![MSR-1 radar map.png](../assets/msr-1-radar-map_1.png)![Radar gates Colored.png](../assets/radar-gates-colored.png)

!!! tip "These are some useful hints!"

    * The FOV angle is -60 to 60 degrees - 120 degrees total.
    * Gates are pre-defined by the radar module and are in 0.75 meter increments.
    * Zones are user-configurable and are in cm.