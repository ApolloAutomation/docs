# General Tips

##### **MSR-1**

![apollo-automation-MSR-1-presence-multisensor-PCB-components-layout-1024x768.jpg.webp](../assets/apollo-automation-msr-1-presence-multisensor-pcb-components-layout-1024x768-jpg.webp)

##### **Light Sensor (LTR-390UV)**

![Light holes.png](../assets/UWHlight-holes.png)

When mounting the MSR-1 be sure to position the device so that the two large holes are not covered. This allows more light to enter and will ensure better accuracy.

!!! warning "The RGB LED will trigger the Light sensor!"

    Make sure that your automations do not interfere with each other. This includes being aware that your onboard LED can trigger the lux reading but not the uv reading of the LTR390 in your device.

##### **Mounting**

![LD2410 Gates.png](../assets/ld2410-gates.png)![LD2410 Zone map.png](../assets/ld2410-zone-map.png)

![ld2410_mounting_hor-1.jpeg](../assets/ld2410-mounting-hor-1.jpeg)

##### **Gate and FOV Visualization**

**![ld2410 table.png](../assets/ld2410-table_1.png)**

![MSR-1 radar map.png](../assets/msr-1-radar-map_1.png)![Radar gates Colored.png](../assets/radar-gates-colored.png)

* FOV angle -60 to 60
* Gate images above are using a Radar Distance Resolution of 0.75m
* ##### **Gates are pre-defined by the radar module and are in meters (m)**
* ##### **Zones are user-configurable and are in centimeters (cm) ![Gate, Zones and RR.png](../assets/gate-zones-and-rr.png)**