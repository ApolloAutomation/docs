---
description: "Tutorial on adding the SCD40 CO2 sensor to your MSR-2."
---
# Adding CO<sub>2</sub> To MSR-2

1\. Unplug your MSR-2 from power and remove the back

![Back of the MSR-2 with the Apollo lettered backplate in place](/assets/msr-2-add-co2-pic-1.jpg)![Holding the MSR-2 and lifting the backplate off with a thumb](/assets/msr-2-add-co2-pic-2.jpg)![MSR-2 with the backplate removed and set aside, showing the circuit board](/assets/msr-2-add-co2-pic-3-1.jpg)

2\. Flip the MSR-2 upside down and gently tap the case on the table and your MSR-2 should slide out of the case.

![MSR-2 flipped upside down on the table with the backplate behind it](/assets/msr-2-add-co2-pic-4.jpg)![Lifting the case off the MSR-2 board labeled MSR-2 Rev 9](/assets/msr-2-add-co2-pic-5.jpg)![MSR-2 board out of its case, showing the radar, ESP32-C3 module, and CN1 connector](/assets/msr-2-add-co2-pic-6.jpg)

3\. With the case removed, identify the bottom right corner where the small black mezzanine connector lives. You will see an "X" indicating which corner needs to be lined up with the SCD40 CO<sub>2</sub> sensor. There is an X on the SCD40 sensor's PCB as well, you can see it in the image below but it is slightly cut off on the PCB itself. There is also a "gold dot" in the top left of the SCD40 when oriented properly.

![Close-up of the MSR-2 CN1 mezzanine connector with the X mark at its bottom right](/assets/msr-2-add-co2-pic-7.jpg)![SCD40 CO2 module below the MSR-2 connector with matching X marks and a gold dot](/assets/msr-2-add-co2-pic-8.jpg)

4\. Gently push the SCD40 CO<sub>2</sub> module onto the black mezzanine connector.

![Pressing the SCD40 CO2 module onto the MSR-2 mezzanine connector](/assets/msr-2-add-co2-pic-9.jpg)![SCD40 CO2 module seated on the MSR-2 board next to the ESP32-C3 module](/assets/msr-2-add-co2-pic-10.jpg)

5\. Slide the case back over the MSR-2, making sure that the case has the hole for the USB-C port facing the right direction.

![Sliding the case back over the MSR-2 board with the port hole at the USB-C end](/assets/msr-2-add-co2-pic-11.jpg)![MSR-2 case end with the USB-C port showing through the hole](/assets/msr-2-add-co2-pic-12.jpg)

6\. Gently press the backplate of the MSR-2 case onto the MSR-2 until it lightly snaps into place. Please do not force it, if necessary please repeat steps above until it seats in the case without any force required.

![Pressing the backplate onto the MSR-2 case until it snaps into place](/assets/msr-2-add-co2-pic-15.jpg)

7\. Please refer to our [CO<sub>2</sub> calibration guide](https://wiki.apolloautomation.com/homey/products/general/calibrating-and-updating/co2-calibration/ "CO2 Calibration") to calibrate the CO<sub>2</sub> module after installation. This is required for all CO<sub>2</sub> addons purchased from us separately from a product (such as buying it to addon to an existing Apollo device).