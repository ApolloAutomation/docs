# General Tips

##### **Light Sensor (LTR-390UV)**

![20240514_123742.jpg](../../../../assets/homey-products-msr2-setup-20240514-123742.jpg)

When mounting the MSR-2 be sure to position the device so that the two large holes are not covered. This allows more light to enter and will ensure better accuracy.

!!! warning "The RGB LED will trigger the Light sensor!"

    Make sure that your automations do not interfere with each other. This includes being aware that your onboard LED can trigger the lux reading but not the uv reading of the LTR390 in your device.

##### **Mounting**

The MSR-2 should be mounted 1.5-2 meters off the ground which will then provide a nice even 120degree FOV of the mmWave radar.

![ld2410_mounting_hor-1.jpeg](../../../../assets/homey-products-msr2-setup-ld2410-mounting-hor-1.jpeg)

The MSR-2 can also be mounted on the ceiling if you can provide power and mount our articulating stand on the ceiling.

![LD2410 Gates.png](../../../../assets/homey-products-msr2-setup-ld2410-gates.png)

!!! tip "These are some useful hints!"

    * The FOV angle is -60 to 60 degrees - 120 degrees total.
    * Gates are pre-defined by the radar module and are in 0.75 meter increments.
    * Zones are user-configurable and are in cm.

##### **Gate and FOV Visualization**

**![ld2410 table.png](../../../../assets/homey-products-msr2-setup-ld2410-table.png)![Gate, Zones and RR.png](../../../../assets/homey-products-msr2-setup-gate-zones-and-rr.png)**

![MSR-1 radar map.png](../../../../assets/homey-products-msr2-setup-msr-1-radar-map.png)![Radar gates Colored.png](../../../../assets/homey-products-msr2-setup-radar-gates-colored.png)

#####