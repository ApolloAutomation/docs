---
title: Add an LED Strip to CAST PRO-1
description: "Connect an addressable LED strip to your CAST PRO-1 and control it from Home Assistant, including a Music Mode that follows playback."
---
# Add an LED Strip

Your CAST PRO-1 has LED strip terminals, **5V**, **GND** and **IO1**, for an addressable LED strip. There's no soldering: the strip's wires go straight into the terminals. Once it's connected, the strip shows up in Home Assistant as a light with effects, and it can switch on by itself whenever music is playing.

!!! note "Coming in a firmware update"

    LED strip support for the CAST PRO-1 is coming in a firmware update. Once it's available, update your CAST PRO-1 from the **Firmware Update** entity on its device page.

## What You'll Need

- **An addressable RGB strip that uses a single data wire.** WS2812B is the most common. WS2812, SK6812 (RGB), WS2811, APA106 and SM16703 also work.
- A strip with bare wire ends (or wires you can connect to its pads) for the terminals.

Strips with separate data and clock wires (APA102, SK9822), RGBW strips, and plain 12V RGB strips with no data wire won't work.

## Power

Every LED draws current. A WS2812B LED pulls up to about 60 mA at full white, so a strip adds up fast: 30 LEDs can draw about 1.8 A, and a 5 m roll of 150 LEDs about 9 A.

- **Short strips** can run from the CAST PRO-1's 5V terminal. Keep **LED Strip Max Brightness** at its default of 50% or lower.
- **Long strips** need their own 5V power supply sized for the strip. Connect the supply to the strip's 5V and GND, connect the CAST PRO-1's **GND** terminal to the strip's GND as well, and run only the data wire from **IO1**. Don't connect the CAST PRO-1's 5V terminal to a strip that has its own supply.

!!! warning "Too much load reboots the CAST PRO-1"

    If the CAST PRO-1 restarts or the audio cuts out when the strip gets bright, the strip is drawing more than the 5V terminal can supply. Lower **LED Strip Max Brightness** or give the strip its own power supply.

## Wiring

You'll connect the strip's power, ground and data wires to the matching terminals on your device.

1\. Unplug your CAST PRO-1 from power.

2\. Find the input end of the strip. Its pads are labelled **DIN** or **DI**, and the arrows printed on the strip point away from it. (1)
{ .annotate }

1.  Data only travels one way along the strip. Wired to the **DOUT** end, the strip stays dark.

3\. Connect the strip's wires to the terminals:

| CAST PRO-1 terminal | LED strip |
| --- | --- |
| 5V | 5V (or +5V) |
| GND | GND |
| IO1 | DIN |

4\. Plug your CAST PRO-1 back into power.

## Turn On the LED Strip Controls

The LED strip controls are hidden until you turn them on, so a CAST PRO-1 without a strip doesn't show extra controls.

1\. In Home Assistant, go to **Settings** > **Devices & services** > **ESPHome** and open your CAST PRO-1.

[![Open your Home Assistant instance and show an integration.](https://my.home-assistant.io/badges/integration.svg)](https://my.home-assistant.io/redirect/integration/?domain=esphome)

2\. Under **Controls**, **Configuration** and **Diagnostic**, select **+N entities not shown** and turn on each entity whose name starts with **LED Strip**. Home Assistant adds them after about 30 seconds.

3\. Set **LED Strip Count** to the number of LEDs on your strip. (1)
{ .annotate }

1.  Multiply the strip's length by its LEDs per meter. A 5 m roll of a 30 LEDs/m strip has 150 LEDs. LEDs past the count stay off.

4\. Press **LED Strip Test**. The strip shows red, green, blue and white, then a rainbow, and turns off.

If the colors come out in the wrong order (for example, green when the test shows red), change **LED Strip Color Order** until they match. GRB is right for most WS2812B strips.

## LED Strip Controls

| Entity | What it does |
| --- | --- |
| **LED Strip** | The strip itself. Turn it on and off, pick a color and brightness, or choose an effect: Rainbow, Color Wipe, Scan, Twinkle, Random Twinkle, Fireworks, Flicker, Pulse or Strobe. |
| **LED Strip Count** | How many LEDs to drive, up to 300. |
| **LED Strip Max Brightness** | Caps the brightness of every LED to keep the current draw down. Defaults to 50%. |
| **LED Strip Color Order** | The order your strip expects its colors in. |
| **LED Strip Chipset** | The type of LED on your strip. Leave it on **WS2812** unless the strip flickers or shows random colors. |
| **LED Strip Music Mode** | Turns the strip on with the **Music Effect** whenever music is playing, and off about 3 seconds after it stops. |
| **LED Strip Music Effect** | The effect Music Mode uses. |
| **LED Strip Test** | Runs the color test from the steps above. |

!!! info "Music Mode follows playback, not the beat"

    Music Mode turns the strip on and off with playback. The effects run at their own pace and don't react to the music itself.

## Troubleshooting

**Nothing lights up**

- Check the data wire goes to the **DIN** end of the strip.
- Make sure the strip's GND is connected to the CAST PRO-1's GND, even when the strip has its own power supply.
- Check the **LED Strip** light is turned on.

**Random colors or flickering**

- Try a different **LED Strip Chipset**.
- Keep the data wire short. The CAST PRO-1 sends a 3.3V data signal, which most strips accept over a short wire.

**Only part of the strip lights up**

- Set **LED Strip Count** to the number of LEDs on your strip.

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
