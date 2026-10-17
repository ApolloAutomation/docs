---
title: Adding GPIO Header to AIR-1
description: Adding Optional GPIO Header to AIR-1.
---
# Adding GPIO Header to AIR-1

Here you open the case, slide out the PCB, and seat the GPIO Header on its mezzanine connector.

1\. Unplug your AIR-1 from power and lift the top of the case or "lid".

![Closed AIR-1 case seen from the side before the lid is removed](/assets/air-1-add-co2-pic-1.jpg)![Pulling the top edge of the AIR-1 lid away from the case](/assets/air-1-add-co2-pic-2.jpg)![AIR-1 lid partly lifted away from the case, exposing the PCB](/assets/air-1-add-co2-pic-3.jpg)

2\. Remove the lid completely by grabbing the lid from the other side and gently lifting upwards.

![Gripping the AIR-1 lid from the other side and lifting it off the case](/assets/air-1-add-co2-pic-4.jpg)

3\. Hold the PCB and orient it correctly where Apollo (the dog) is facing you in.

![AIR-1 PCB on the removed lid with the Apollo dog artwork facing up, cabled to the SEN55](/assets/air-1-add-co2-pic-5.jpg)

4\. Gently slide the pcb out by sliding it to the left as shown in the images below.

![Starting to slide the AIR-1 PCB to the left out of the lid](/assets/air-1-add-co2-pic-6.jpg)![AIR-1 PCB sliding further out of the lid, still cabled to the SEN55](/assets/air-1-add-co2-pic-7.jpg)

5\. Flip the PCB over and identify the Top Right corner where the small black mezzanine connector lives. You will see an "X" indicating which corner needs to be lined up with the PCB of the GPIO Header. There is an X on the GPIO Header's PCB as well, you can see it in the images below.

![AIR-1 PCB in the case with a probe pointing at the X beside the mezzanine connector](/assets/air-1-gpio-header-wiki-pic-1.webp)![GPIO Header add-on board with a probe pointing at its X marking](/assets/air-1-gpio-header-wiki-pic-2.webp)

6\. Match up the X on the PCB of the GPIO Header and the X on the AIR-1 PCB and then gently push the GPIO Header onto the black mezzanine connector.

![GPIO Header held over the AIR-1 PCB with both X marks lined up](/assets/air-1-gpio-header-wiki-pic-3.webp)![Pressing the GPIO Header onto the AIR-1 mezzanine connector](/assets/air-1-gpio-header-wiki-pic-4.webp)![GPIO Header seated on the AIR-1 PCB inside the case](/assets/air-1-gpio-header-wiki-pic-5.webp)

7\. Flip the AIR-1 PCB over and gently slide it back into the new AIR-1 Lid which came with your GPIO Header addon! Please do not use much force, the PCB should slide in relatively smoothly, with a tiny bit of force needed. There are three channels in the plastic where the PCB slides into!

![Sliding the AIR-1 PCB into the new lid with the Apollo dog artwork facing out](/assets/air-1-gpio-header-wiki-pic-6.webp)![AIR-1 PCB seated in the new lid, still cabled to the SEN55](/assets/air-1-gpio-header-wiki-pic-7.webp)

8\. Gently push the case back together as shown below.

![Lowering the new lid onto the AIR-1 case with the GPIO Header lined up](/assets/air-1-gpio-header-wiki-pic-8.webp)![AIR-1 lid closing with the GPIO Header socket fitting through its opening](/assets/air-1-gpio-header-wiki-pic-9.webp)![Closed AIR-1 case with the GPIO Header socket exposed in the lid](/assets/air-1-gpio-header-wiki-pic-10.webp)

9\. You are now done and your AIR-1 is now able to be used with the GPIO Header addon! Here is the pinout image below and <a href="https://wiki.apolloautomation.com/products/air1/examples/how-to-use-the-apollo-gpio-header-to-control-an-led-strip/" target="_blank" rel="noopener">here's a great wiki article showing you how to add a small led strip!</a>

!!! warning "Warning"

    If you plan to use a lot of leds or your gpio project requires a lot of power then you need to use a dedicated power supply and not try to use too much power (under 350mA) from the GPIO of the device! You can power the AIR-1 via the vcc (5v) and GND pins but please do not power it via the pins AND the USB-C port, it should be one or the other.

![AIR-1 GPIO Header pinout. Left: GND, IO18, IO19, IO4, IO2, IO6. Right: 5V, IO7, SDA IO1, SCL IO0, GND, 3V](/assets/gpio-header-pinout.webp)