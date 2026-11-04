---
title: Add an LED strip to CAST PRO-1
description: "Connect an addressable LED strip to your CAST PRO-1 and control it from Home Assistant, including a Music Mode that follows playback."
---
# Add an LED strip

Your CAST PRO-1 has LED strip terminals, **5V**, **GND** and **IO1**, for an addressable LED strip. There's no soldering: the strip's wires go straight into the terminals. Once it's connected, the strip shows up in Home Assistant as a light with effects, and it can switch on by itself whenever music is playing.

!!! note "Update your firmware first"

    If you don't see any **LED Strip** entities on your CAST PRO-1's device page, update it from the **Firmware Update** entity first.

## What you'll need

- **An addressable RGB strip that uses a single data wire.** WS2812B is the most common. WS2812, SK6812 (RGB), WS2811, APA106 and SM16703 also work.
- A strip with bare wire ends (or wires you can connect to its pads) for the terminals.

Strips with separate data and clock wires (APA102, SK9822), RGBW strips, and plain 12V RGB strips with no data wire won't work.

## Power

Every LED draws current. A WS2812B LED pulls up to about 60 mA at full white, so a strip adds up fast: 30 LEDs can draw about 1.8 A, and a 5 m roll of 150 LEDs about 9 A.

- **Short strips** can run from the CAST PRO-1's 5V terminal. Power the CAST PRO-1 from a **5V 3A** USB-C supply instead of the usual 5V 1A, and keep **LED Strip Max Brightness** at its default of 50% or lower.
- **Long strips** need their own 5V power supply sized for the strip. Connect the supply to the strip's 5V and GND, connect the CAST PRO-1's **GND** terminal to the strip's GND as well, and run only the data wire from **IO1**. Don't connect the CAST PRO-1's 5V terminal to a strip that has its own supply.

!!! warning "Too much load reboots the CAST PRO-1"

    If the CAST PRO-1 restarts or the audio cuts out when the strip gets bright, the strip is drawing more than the 5V terminal can supply. Lower **LED Strip Max Brightness** or give the strip its own power supply.

## Wiring

You'll connect the strip's power, ground and data wires to the matching terminals on your device.

1\. Unplug your CAST PRO-1 from power.

2\. Find the input end of the strip. Its pads are labelled **DIN** or **DI**, and the arrows printed on the strip point away from it. (1)
{ .annotate }

1.  Data only travels one way along the strip. Wired to the **DOUT** end, the strip stays dark.

3\. Loosen each screw terminal, slide the strip's wire in, and tighten it down. From left to right, the terminals are **5V**, **GND** and **IO1**:

| CAST PRO-1 terminal | LED strip |
| --- | --- |
| 5V | 5V (or +5V) |
| GND | GND |
| IO1 | DIN |

4\. Plug your CAST PRO-1 back into power.

## Turn on the LED strip controls

The LED strip controls are hidden until you turn them on, so a CAST PRO-1 without a strip doesn't show extra controls.

1\. In Home Assistant, go to **Settings** > **Devices & services** > **ESPHome** and open your CAST PRO-1.

[![Open your Home Assistant instance and show an integration.](https://my.home-assistant.io/badges/integration.svg)](https://my.home-assistant.io/redirect/integration/?domain=esphome)

2\. Under **Controls**, **Configuration** and **Diagnostic**, select **+N entities not shown** and turn on each entity whose name starts with **LED Strip**. Home Assistant adds them after about 30 seconds.

3\. Set **LED Strip Count** to the number of LEDs on your strip. (1)
{ .annotate }

1.  Multiply the strip's length by its LEDs per meter. A 5 m roll of a 30 LEDs/m strip has 150 LEDs. LEDs past the count stay off.

4\. Press **LED Strip Test** under **Diagnostic**. The strip shows red, green, blue and white, then a rainbow, and turns off.

If the colors come out in the wrong order (for example, green when the test shows red), change **LED Strip Color Order** until they match. GRB is right for most WS2812B strips.

## LED strip controls

| Entity | What it does |
| --- | --- |
| **LED Strip** | The strip itself. Turn it on and off, pick a color and brightness, or choose an effect: Rainbow, Color Wipe, Scan, Twinkle, Random Twinkle, Fireworks, Flicker, Pulse, Strobe, **Effect A** or **Effect B**. |
| **LED Strip Count** | How many LEDs to drive, up to 300. Defaults to 30. |
| **LED Strip Max Brightness** | Caps the brightness of every LED to keep the current draw down. Defaults to 50%. |
| **LED Strip Color Order** | The order your strip expects its colors in. |
| **LED Strip Chipset** | The type of LED on your strip. Leave it on **WS2812** unless the strip flickers or shows random colors. |
| **LED Strip Effect A Pattern** and **LED Strip Effect A Speed** | The pattern **Effect A** runs, and how fast. |
| **LED Strip Effect B Pattern** and **LED Strip Effect B Speed** | The pattern **Effect B** runs, and how fast. |
| **LED Strip Music Mode** | Turns the strip on with the **Music Effect** whenever music is playing, and off about 3 seconds after it stops. |
| **LED Strip Music Effect** | The effect Music Mode uses. |
| **LED Strip Test** | Runs the color test from the steps above. Under **Diagnostic**. |

## Effects

**Effect A** and **Effect B** are two effect slots. Give each one a pattern and a speed, then pick it from the **LED Strip** light's effect list. Changes apply live while the effect runs, so you can drag the speed slider and watch the strip react. The other effects in the list run at a fixed speed.

Speed runs from 1 to 100 on a curve: 1 is one step per second, and 100 is one step every 32 ms.

| Pattern | What it does |
| --- | --- |
| **Flicker** | Dips to random levels between full and 30% brightness. |
| **Strobe** | On for one step and off for the next. |
| **Rainbow** | Moves a rainbow along the strip. It ignores the light's color. |
| **Color Wipe** | Fills the strip one LED at a time, then clears it the same way. |
| **Scan** | Moves one lit LED back and forth. |
| **Twinkle** | Fades random LEDs in and out. |
| **Pulse** | Fades the whole strip from off to full and back. |
| **Fireworks** | Lights random sparks that spread and fade. |

!!! danger "Photosensitivity warning"

    **Strobe** flashes faster than 3 times per second from about Speed 50 up, and reaches about 16 flashes per second at Speed 100. **Pulse** passes 3 flashes per second from about Speed 75. Flashing in this range can trigger seizures in people with photosensitive epilepsy.

??? example "Set an effect from an automation"

    Set the pattern and speed first, then turn the strip on with that effect slot:

    ```yaml
    actions:
      - action: select.select_option
        target:
          entity_id: select.apollo_cast_pro_1_04c6d0_led_strip_effect_a_pattern
        data:
          option: Twinkle
      - action: number.set_value
        target:
          entity_id: number.apollo_cast_pro_1_04c6d0_led_strip_effect_a_speed
        data:
          value: 20
      - action: light.turn_on
        target:
          entity_id: light.apollo_cast_pro_1_04c6d0_led_strip
        data:
          effect: Effect A
    ```

    Swap in the entity IDs from your own device page. The end of each ID comes from your device's MAC address, so yours won't be `04c6d0`.

!!! info "Music Mode follows playback, not the beat"

    Music Mode turns the strip on and off with playback. The effects run at their own pace and don't react to the music itself.

## Split the strip into segments

You can split one strip into segments and control each segment as its own light in Home Assistant, for example one color per shelf. Segments are ESPHome partition lights, so you'll add them to your CAST PRO-1's YAML.

!!! note "Before you start"

    Take control of your CAST PRO-1 in the [ESPHome Device Builder](../additional-info/esphome-device-builder.md) first, so you can edit its YAML.

1\. Open your CAST PRO-1's YAML in the ESPHome Device Builder.

2\. Add a `light:` section like the one below. Keep your own name, encryption key and Wi-Fi lines. This example splits a 30 LED strip into two segments of 15. (1)
{ .annotate }

1.  `from` and `to` count from 0, and `to` is included, so `from: 0` and `to: 14` is the first 15 LEDs. Every segment has to fit inside the **LED Strip Count** you set in Home Assistant.

```yaml
light:
  - platform: partition
    name: "LED Segment 1"
    segments:
      - id: led_strip
        from: 0
        to: 14
    default_transition_length: 0s
    # LED Strip Max Brightness doesn't reach segments, so cap each one here
    color_correct: [50%, 50%, 50%]
    # A light restores its effect by position, so add new effects at the end
    effects: &led_segment_effects
      # Effect A and B follow the strip's Pattern and Speed settings
      - addressable_lambda:
          name: "Effect A"
          update_interval: 15ms
          lambda: "id(led_strip_slot_effect)(it, current_color, initial_run, 0);"
      - addressable_lambda:
          name: "Effect B"
          update_interval: 15ms
          lambda: "id(led_strip_slot_effect)(it, current_color, initial_run, 1);"
      # Built-in effects run at a fixed speed
      - addressable_rainbow:
          name: "Rainbow"
      - addressable_twinkle:
          name: "Twinkle"
      - pulse:
          name: "Pulse"
  - platform: partition
    name: "LED Segment 2"
    segments:
      - id: led_strip
        from: 15
        to: 29
    default_transition_length: 0s
    color_correct: [50%, 50%, 50%]
    effects: *led_segment_effects
```

3\. Click **Install** and choose **On the network**. Once it finishes, **LED Segment 1** and **LED Segment 2** show up on your CAST PRO-1's device page.

Both segments share the **Effect A** and **Effect B** pattern and speed settings with the **LED Strip** light.

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
