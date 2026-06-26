---
title: Adding the RGB & Buzzer Module
description: >-
  Wire up the ESPHome Starter Kit RGB & Buzzer module, add it through ESPHome
  Device Builder, then turn the lights and off and change colors.
---
# Adding the LED & Buzzer Module

The LED & Buzzer is the starter kit's notification module, a strip of ten addressable RGB LEDs and a small piezo buzzer behind the ESPHome logo silkscreen. By the end of this tutorial you'll have the lights and buzzer wired to your ESP32-C6, surfaced in your YAML, and ready to flash, animate, or sing in response to anything else you build.

!!! note "Before you start"

    Work through the two prerequisites first:

    * [Start Here](/products/ESPHome-Starter-Kit/start-here.md) to snap the RGB & Buzzer module off the panel.
    * [First Steps](/products/ESPHome-Starter-Kit/setup/first-steps.md) to install ESPHome Device Builder and create your starter kit device.

#### Prerequisite

The <a href="https://esphome.io/components/web_server/" target="_blank" rel="noreferrer nofollow noopener">Web Server</a> is used to broadcast a local website using your device. This allows you to navigate to the IP address of your device or hostname such as <a href="http://esphome-starter-kit.local/" target="_blank" rel="noreferrer nofollow noopener">esphome-starter-kit.local</a> to easily control your new device!

1. In the ESPHome Device Builder, navigate to the **Core configuration** section.
2. Click **Add component**.
3. Scroll to **Web Server** and click **Add**.
4. Click **Add** once more to confirm.
5. Toggle **Show advanced settings**.
6. Scroll down to **Version** and select **3** from the dropdown.

![](../../../assets/device-builder-install-web-server-v3.gif)

## Attach LED & Buzzer module

Connect the LED & Buzzer module to the ESP32-C6 using one of the FPC ribbon cables that came with the kit. Either FPC connector on the ESP32-C6 works, top or bottom.

1\. Unplug the USB-C cable from the ESP32-C6 so it is powered off.

![](../../../assets/esphome-starter-kit-remove-usb.webp)

!!! warning "Handle the FPC connectors gently"

    The latches are small and the ribbon cable is fragile. Lift the latch with a fingernail, slide the cable in, and press the latch down. Never pull on the cable itself.

2\. Flip up the latch on the FPC connector then gently slide the ribbon cable in to the connector. Gently press the latch down to lock it in place

![](../../../assets/esphome-starter-kit-attach-top-fpc-ribbon.webp)

3\. Slide the ribbon cable into the button module with the blue side facing upwards then press the latch down to lock it in place.

![](../../../assets/esphome-starter-kit-attach-fpc-to-rgb-buzzer-module.webp)

4\. Plug the ESP32-C6 back into your computer.

## Add to ESPHome Device Builder

ESPHome Device Builder ships an **Add Component** flow that knows the pin layout for every Apollo Starter Kit module. Use it instead of writing the LED strip and buzzer config by hand, and you'll get the right GPIOs, chipset, and PWM setup on the first try.

1. Open your starter kit device in Device Builder and click **Edit**.
2. In the ESPHome Device Builder, navigate to the **Components** section.
3. Click **Add Component** in the editor toolbar.
4. Select the **RGB LED + Buzzer Module Bundle** at the top.
5. Click **Add** -&gt; Click **Add** -&gt; Click **Add** -&gt; Click **Add**. Each section lets you make changes but we will leave them at defaults for now. Device Builder inserts the light, output, and rtttl blocks into your YAML.

![](../../../assets/esphome-device-builder-add-rgb-buzzer-bundle-module.gif)

??? note "What the LED & Buzzer Module YAML does"

    The blocks Add Component drops into your config look like this:

    ```yaml
    light:
      - platform: esp32_rmt_led_strip
        id: rgb_leds
        name: "RGB LEDs"
        pin: GPIO14
        chipset: WS2812
        num_leds: 10
        rmt_symbols: 48
        rgb_order: grb
        default_transition_length: 0s
        effects:
          - addressable_rainbow:
              name: "Rainbow"
          - addressable_twinkle:
              name: "Twinkle"

    output:
      - platform: ledc
        pin: GPIO18
        id: buzzer

    rtttl:
      id: rtttl_buzzer
      output: buzzer
    ```

    Each option does something specific:

    \| Option \| What it does \| \| --- \| --- \| \| **LED strip** \| \| \| `light.platform: esp32_rmt_led_strip` \| Uses the ESP32's RMT peripheral to drive addressable LEDs with precise timing. \| \| `light.pin: GPIO14` \| The data line going to the first LED on the PCB. \| \| `light.chipset: WS2812` \| Which addressable LED protocol to use. WS2812 is the most common, sometimes also called NeoPixel. \| \| `light.num_leds: 10` \| The number of LEDs on the RGB & Buzzer module. \| \| `light.rgb_order: grb` \| Color channel order. WS2812 LEDs receive color data in green-red-blue order, so this makes sure red looks red and not green. \| \| `light.rmt_symbols: 48` \| Low-level RMT setting needed on the ESP32-C6. Leave it at 48. \| \| `light.effects` \| Pre-loaded animations you can select from the web server or trigger from Home Assistant. \| \| **Piezo buzzer** \| \| \| `output.platform: ledc` \| PWM output for driving the buzzer. PWM is how digital pins create audio tones on a piezo. \| \| `output.pin: GPIO18` \| The pin the buzzer is wired to. \| \| `output.id: buzzer` \| Internal handle the rtttl component uses to send tones to this output. \| \| `rtttl.id: rtttl_buzzer` \| Internal handle for triggering tunes from automations and lambdas. \| \| `rtttl.output: buzzer` \| Tells rtttl to use the buzzer output for playback. \|

## Install the firmware

Flash the device so the new web server and the RGB & Buzzer entities go live.

1. Click **Install** on your device card in ESPHome Device Builder.
2. Choose **Plug into the computer running ESPHome Device Builder** for the first flash, or **On The Network** if the device is already on your Wi-Fi.
3. Wait for the compile and flash to finish. First builds can take a few minutes.
4. The device reboots and reconnects to your Wi-Fi on its own.

![](../../../assets/esphome-device-builder-install-rgb-buzzer-component.gif)

## Test the LEDs

With the device back online, the RGB LED light entity is live on the web server. <a href="http://esphome-starter-kit.local/" target="_blank" rel="noreferrer nofollow noopener">Open it in a browser</a> on the same network and play with it.

1. In a browser, open `http://<your-device-name>.local/`. If you used `esphome-starter-kit` as the device name in Getting Started, that's `http://esphome-starter-kit.local/`.
2. Toggle the **RGB LEDs** entity and play around with the colors and brightness.

![](../../../assets/esphome-device-builder-test-rgb-leds.gif)

!!! tip "For more effects check out this wiki on how to do advanced configurations with your RGB & Buzzer module!"

    There are a lot of advanced things you can do with a light entity. Click here (NEED-TO-LINK-TO-NEW-LIGHT-COMPONENT-WIKI) to learn more about that!

The buzzer doesn't have its own web server control, since it's an output rather than a switch. Once you've added the device to Home Assistant, you can trigger tunes with the `rtttl.play` action or by exposing your own service.

> Web server page showing the RGB Light controls on the LED & Buzzer Module.

!!! success "Your LED & Buzzer notification module is wired up!"

    Your LED & Buzzer Module is now ready for some fun tasks.. like toggling lights on and off, playing with the colors, or using the buzzer to play fun tunes!

## Try it in an automation

Your notification module is ready. Drive it from any of these automations:

<a href="/products/ESPHome-Starter-Kit/automations/button-controlled-leds/" class="md-button md-button--primary"> <img src="/assets/esphome-logo.svg" /> Button Controlled LEDs </a>
<a href="/products/ESPHome-Starter-Kit/automations/play-a-tune/" class="md-button md-button--primary"> <img src="/assets/esphome-logo.svg" /> Play a Tune </a>
<a href="/products/ESPHome-Starter-Kit/automations/temp-reactive-leds/" class="md-button md-button--primary"> <img src="/assets/esphome-logo.svg" /> Temp-Reactive LEDs </a>
<a href="/products/ESPHome-Starter-Kit/automations/motion-activated-light/" class="md-button md-button--primary"> <img src="/assets/esphome-logo.svg" /> Motion-Activated Light </a>

--8<-- "_snippets/community-help.md"