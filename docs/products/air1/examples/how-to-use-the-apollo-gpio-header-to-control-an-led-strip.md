---
title: How To Use The Apollo GPIO Header To Control An LED Strip
description: A tutorial for how To Use The Apollo GPIO Header To Control An LED Strip.
---
# How To Use The Apollo GPIO Header To Control An LED Strip

This tutorial will guide you through setting up one of our MSR-2 devices (works with any mezzanine port on any Apollo Device) with the optional $4.99 GPIO Header which adds pins for you to easily add functionality to your device! In this tutorial, however, we will be focusing on adding an LED strip to your Apollo device.

**Materials Needed for tutorial:**

* [Apollo MSR-2](https://apolloautomation.com/products/msr-2), [Apollo MTR-1](https://apolloautomation.com/products/mtr-1), and all other future Apollo Automation products with the mezzanine port.
* [Apollo GPIO Header](https://apolloautomation.com/products/msr-2-gpio-header)
* ws2812b aka neopixel RGB led strip or similar. sk6812 RGBW strip will also work. I used BTF Lighting ws2812b 60 leds/meter and white PCB.
* Optional DuPont Cables for GPIO Header but any DuPont cables will do.
* USB-C cable and power brick to power MSR-2

You are limited to 300mA of power output from the 5v port. You can either attach an external power supply and power the MSR-2 via 5v and gnd pins or work with the limited power output of the port

![GPIO Pinout](../assets/cS6XiR5FyO8wvSBi9sW3466gHoUWfT7HhA.png_1719600483)

Above is an image of the GPIO Header and its pinouts. We can use ports 2,4,6,7 for our data channel to an LED strip or multiple LED strips. We will also use the top two ports which are ground and 5v for power.

Did you know you can power the esp32 from the 5v and gnd pin? That means you can connect an external power supply and power it without the side USB port being used! This also allows for more power to be given to your LEDs!

We cannot use the IO ports 0,1,18, or 19 for LEDs but you can use ports 0 and 1 for i2c sensors.

**Connecting the GPIO Header to the MSR-2**

The first thing we will do is remove our MSR-2 back plate and connect our GPIO Header to our MSR-2 and then put the new GPIO back plate on (blue).

Step 1. Remove the backplate of the MSR-2

![](../assets/0Jrm5FqWzsc9G2KmWBJWMLEr2J4aYyj4Bg.jpg_1719609483) ![](../assets/9UJnA9aCGf0TNw1uc3ik2xEFxXlLs95bOw.jpg_1719609472)

Step 2. Line up the Xs shown on the msr-2 and the GPIO Header. They should both be facing in the same direction as shown below.

![](../assets/6uv5liNNA-wHLFfHxiadM56YpIonKQalTg.jpg_1719609565)

Step 3. Gently push down onto the GPIO Header as shown below:

![](../assets/a6nANg-L_gqIkPH6ZKQo6mCSSSbacF7FkQ.jpg_1719609655)

Step 4. Confirm the GPIO Header is seated properly as shown below.

![](../assets/P3TZVCVhVSBYXFOWtPc4fZML_8-LQTEHQw.jpg_1719609689)

Step 5. Slide the GPIO Header back plate for the MSR-2 over your sensor and gently push down until it clicks into place.

![](../assets/hbfGA0fIQlpnykuuZOhiEuHlZDW7r3GfoQ.jpg_1719609715)

If the back plate does not gently go onto the sensor please investigate and confirm it is in the right orientation.

**Connecting DuPont pins to proper GPIO ports** Now we need to reference the GPIO pinout we looked at above and then connect three wires. You will need three male-to-male DuPont wires included in your kit. I suggest using red for power aka 5v, White for ground aka GND, and green for data aka port IO7. Most LED strips will also have this same color scheme and it's easier to match like colors together.

![](../assets/4OHLuxZVKc1TcCGLfvAEf-1UUl-IzmeHzQ.jpg_1719610515)

![](../assets/4Er61OH8tF-IaiVvom0cWPeOyfNkRWtibw.jpg_1719610507)

![](../assets/oBW2IxCJX5zKaZGj_o4JtXuoulEGI8DH5Q.jpg_1719610557)

You can add a bit of hot glue to the Dupont wires to hold them together. DO NOT put hot glue into the GPIO Header's female pins that will ruin the addon. I am only suggesting that you can hot-glue the Dupont pins outer shell themselves together to stiffen them up.

![5QMWMycqBmvOz_mlKdoTbZwkC-4__REi8A.jpg](../assets/5qmwmycqbmvoz-mlkdotbzwkc-4-rei8a.jpg)

**Connecting DuPont pins to LED Strip**

Next, we need to connect the other side of the Dupont pins to the LED strip. Most likely your LED strip will have a JST-SM connector which is a 3amp max connector with three wires connected: red for 5v, green for data, and white for gnd. We will be matching up our red, green, and white wires already attached to the GPIO add-on pins in the MSR-2 (using IO7 as the data pin for this tutorial)

![](../assets/Me6P6lhhZUQMhuY--kIQqoFHV6QgrxpO0g.jpg_1719611251) ![](../assets/LwzqEXM9B89IWUQCIdZtwo_uYIbYVzdT0g.jpg_1719611264)

Make sure to connect to the correct side of the LED strip. The led strip will have an arrow going down the led strip showing one direction for the data line. you want the data channel going FROM the msr-2 TO the led strip going in a "forward" direction as shown below.

![](../assets/n0MT-JcoqRwPKYfZOaYyBD2RU4K3x_gmOA.jpg_1719611527) ![](../assets/BDLaEPEomVhYjATCJMSVMltiTS9aoVY9YQ.jpg_1719611545)

**Edit the YAML of your MSR-2 to let it know about your new LED strip**

Finally, we need to tell the MSR-2 that we connected an LED strip. We need to tell it how many LEDs we have and we need to tell it that it's our second LED since the built-in LED is the first. This tutorial assumes you are comfortable with the ESPHome dashboard.

Step 1. Open ESPhome Dashboard and click edit to bring up the yaml your sensor is currently using.

![](../assets/28MMBJEeIQOmwUGtP9L3cx0PtCaTL0HX_Q.png_1719612259)

You will see some YAML code here and you do NOT want to touch anything above line 20. If you need to, click your cursor at the end of wifi\_password and hit enter to create a new line then make sure you backspace until you are "flush" with the line numbers like how wifi: is.

Step 2. Copy the code below and paste it to line 20 in your ESPHome yaml for this device.

```yaml
light:
  - platform: esp32_rmt_led_strip
    id: bed_led
    name: "Bed LED"
    pin: GPIO7
    rmt_channel: 1
    default_transition_length: 0s
    chipset: WS2812
    num_leds: 60
    rgb_order: grb
    effects:
      - pulse:
          name: "Slow Pulse"
          transition_length: 1000ms
          update_interval: 1000ms
          min_brightness: 50%
          max_brightness: 100%
      - pulse:
          name: "Fast Pulse"
          transition_length: 100ms
          update_interval: 100ms
          min_brightness: 50%
          max_brightness: 100%
      - addressable_rainbow:
```

This is where you can change your number of LEDs as well as the GPIO pin used for the LED data!<br> Make sure to check out [https://esphome.io/components/light/index.html#light-effects](https://esphome.io/components/light/index.html#light-effects) for all the effects supported such as addressable scan effect!

Step 3. Confirm you do not have any red lines showing errors in your code![](../assets/EQdHu-pdF_2D7T6GJkjdqSQYZptmHk-cmw.png_1719612604)You change the rmt\_channel to 1 because 0 is being used by the built-in LED of the MSR-2.

Step 4. Hit save and then install in the top right. It should have a popup where you select "wirelessly" then it will begin compiling the firmware and finally installing the compiled firmware to your MSR-2.

Step 5. Go into home assistant and confirm you now have a new light entity called Bed LED

![](../assets/YfpAVN1FtpsODgbFgZg8qEVBNjl3NgaAvQ.png_1719613175)

Step 6. Click on the name "Bed LED" circled and it will pop up a color picker. You can then choose the color wheel option to pick any color of the rainbow, or select "effect" and choose an effect.

![](../assets/GublKQEhWUdU-OxJiA948P3_HGiwxTpn4w.png_1719613216) ![](../assets/ObY0NPGDBIBaXPuhUVzo80fr1fToBm5ekg.png_1719613432) ![](../assets/1OhdBudlNh2Rk8SoytNKdoUHqknn8KA8sQ.png_1719613457)

![](../assets/JI4fSugUQvhRpK1FauJEEPoj3Vwe-QD02Q.jpg_1719613900)

&nbsp;