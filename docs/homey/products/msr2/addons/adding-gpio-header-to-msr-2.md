---
title: Adding GPIO Header To MSR-2
description: "Tutorial on adding the GPIO Header to your MSR-2."
---
# Adding GPIO Header To MSR-2

1\. Unplug your MSR-2 from power and remove the back.

![Back of the MSR-2 with the Apollo lettered backplate in place](/assets/msr-2-add-co2-pic-1.jpg)

![Holding the MSR-2 and lifting the backplate off with a thumb](/assets/msr-2-add-co2-pic-2.jpg)

![MSR-2 with the backplate removed and set aside, showing the circuit board](/assets/msr-2-add-co2-pic-3-1.jpg)

2\. Identify the "X" on the PCB on the back of your MSR-2 and the "X" on the top left corner of the GPIO Header addon.

![Tool pointing at the X mark beside the MSR-2 CN2 connector, with the GPIO Header addon beside it](/assets/msr-2-gpio-header-pic-1.jpg)

![MSR-2 CN2 connector next to the GPIO Header addon with its X mark at the top left](/assets/msr-2-gpio-header-pic-2.jpg)

3\. Keep the "X" aligned on both sides and gently push down until it securely seats in the small mezzanine connector.

![GPIO Header addon seated on the MSR-2 board with the X marks aligned](/assets/msr-2-gpio-header-pic-3.jpg)

4\. Align the new back for your MSR-2 that came with the GPIO Header addon. Push down on the corners closest to the GPIO Header addon first, and then push the back on securely on the other two corners.

![Pressing the GPIO Header backplate onto the MSR-2 near the header first](/assets/msr-2-gpio-header-pic-5.jpg)

![MSR-2 with the GPIO Header backplate fully seated and the header exposed](/assets/msr-2-gpio-header-pic-4.jpg)

## GPIO Header pinout

With the header installed, these are the pins you can wire to. IO18 and IO19 can't be used while you flash the MSR-2, and IO0 and IO1 carry the I2C bus (SDA and SCL).

![MSR-2 GPIO Header pinout. Left: GND, IO18, IO19, IO4, IO2, IO6. Right: 5V, IO7, SDA IO1, SCL IO0, GND, 3V](/assets/gpio-header-pinout.webp)

!!! tip "Make sure to check out our MSR-2 GPIO Header LED Strip Tutorial!"

    Brandon AKA SmartHomeSellout made this neat tutorial for how to connect a short LED strip to your MSR-2

    <a href="https://wiki.apolloautomation.com/products/msr2/examples/gpio-header-control-an-led-strip/" target="_blank" rel="noreferrer nofollow noopener">GPIO LED Strip Tutorial</a><br>