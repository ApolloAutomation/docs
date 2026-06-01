---
title: Temp-Reactive LEDs
description: >-
  Build an ESPHome Device Builder automation that drives the LED & Buzzer
  module to a color band based on the current temperature reading.
---
# Temp-Reactive LEDs

This tutorial uses the Temperature and Humidity module and the LED & Buzzer module connected to the ESP32-C6. As the room temperature drifts across set thresholds, the RGB LEDs change color so you can see the comfort band at a glance. It's the same trigger-then-action pattern as [Button Controlled LEDs](button-controlled-leds.md), swapping the button trigger for a sensor-value trigger and adding one trigger per band.

!!! note "Before you start"

    Work through these pages first. This tutorial assumes your device is flashed and both modules are connected:

    * [First Steps](../setup/first-steps.md) to create your starter kit device in ESPHome Device Builder.
    * [Adding the Temperature and Humidity Module](../modules/temperature-humidity-module.md) to wire up the sensor.
    * [Adding the LED & Buzzer Module](../modules/rgb-buzzer-module.md) to wire up the RGB output.

## How the color bands work

The temperature sensor publishes a new reading every minute by default. We wire three triggers to the same sensor, one per band, so whichever band the latest reading falls into sets the LED color.

| Temperature band | Color |
| --- | --- |
| Below 18 °C (64 °F) | Blue |
| 18 °C to 24 °C (64 °F to 75 °F) | Green |
| Above 24 °C (75 °F) | Red |

!!! note "The GUI fields take Celsius numbers"

    The AHT20 sensor publishes its readings in Celsius, so the **Above** and **Below** values you enter in Device Builder need to be Celsius numbers. The Fahrenheit values in the table above are for reference only. Tune the thresholds to whatever fits your space, in Celsius.

## Build the automation

ESPHome Device Builder has a GUI for building <a href="https://esphome.io/automations/" target="_blank" rel="noreferrer nofollow noopener">automations</a>, so you can wire a trigger to an action without hand-writing YAML. We'll add three automations on the same temperature sensor, one for each color band.

1.  Open your starter kit device in ESPHome Device Builder and click **Edit**. If you need a refresher on the editor, see the [Device Builder Tour](../learning-the-basics/device-builder-tour.md#editor).
2.  In the editor's left pane, expand the **Automations** dropdown and click **Add Automation**.

    ![](../../../assets/esphome-device-builder-add-automation.gif)

#### Cold band: below 18 °C → Blue

1.  Set up the trigger:

    <div class="annotate" markdown>

    - **What should this automation react to?** → **A configured component**
    - **Which configured component?** → **Temperature (sensor)**
    - **Which trigger?** → **Sensor → On Value Range** (1)
    - **Below** → `18.0`
    - Leave **Above** blank.

    </div>

    1.  **On Value Range** fires whenever a new sensor reading lands inside the band you describe. The dropdown also offers **On Value**, **On Raw Value**, and **On State** for other sensor behaviors.

2.  Click **Continue**. You land on the **Sensor → On Value Range** editor with the **Target** already set to your temperature sensor.
3.  Set up the action:

    <div class="annotate" markdown>

    - Under **Actions**, click **+ Add action**.
    - In the **Add action** dialog, stay on the **By target** tab and choose **Light → Turn On** under the RGB LED group.
    - On the new action, click the **ID** dropdown and select **RGB LEDs**. (1)
    - Toggle on **Red**, **Green**, and **Blue** controls. Set **Red** `0%`, **Green** `0%`, **Blue** `100%`.

    </div>

    1.  The **ID** dropdown only needs changing if your device also has an **Onboard RGB LED** component configured. If **RGB LEDs** is the only light, it's already selected.

#### Comfortable band: 18 °C to 24 °C → Green

Add another automation, this time picking **Sensor → On Value Range** with **Above** `18.0` and **Below** `24.0`. The action targets **RGB LEDs** with **Red** `0%`, **Green** `100%`, **Blue** `0%`.

#### Hot band: above 24 °C → Red

Add a third automation with **Sensor → On Value Range** and **Above** `24.0` (leave **Below** blank). The action targets **RGB LEDs** with **Red** `100%`, **Green** `0%`, **Blue** `0%`.

??? note "What the GUI built in YAML"

    The form pane and the YAML editor on the right of the editor stay in sync. Your temperature sensor now grows three `on_value_range` triggers, one per band:

    ```yaml
    sensor:
      - platform: aht10
        variant: AHT20
        id: aht_20
        temperature:
          name: "Temperature"
          id: aht_temperature
          on_value_range:
            - below: 18.0
              then:
                - light.turn_on:
                    id: rgb_leds
                    red: 0%
                    green: 0%
                    blue: 100%
            - above: 18.0
              below: 24.0
              then:
                - light.turn_on:
                    id: rgb_leds
                    red: 0%
                    green: 100%
                    blue: 0%
            - above: 24.0
              then:
                - light.turn_on:
                    id: rgb_leds
                    red: 100%
                    green: 0%
                    blue: 0%
        humidity:
          name: "Humidity"
          id: aht_humidity
        update_interval: 60s
    ```

    See [Device Builder Tour → YAML editor (right)](../learning-the-basics/device-builder-tour.md#yaml-editor-right) for the full breakdown of the YAML pane.

## Install the firmware

Your three automations are saved in Device Builder, but the device is still running its old firmware. Compile and install the new code to push the change.

1. Click **Save** in the bottom right of the editor.
2. Click **Install**, then pick **On the Network** to push the new firmware over Wi-Fi.
3. Wait for the compile and flash to finish. The device reboots once the install is done.

![](../../../assets/esphome-device-builder-install-button-component.gif)

## Test the automation

With the device back online, the next sensor reading sets the LED color. With `update_interval: 60s` you may wait up to a minute for the first update. To force a quicker change, cup a warm hand around the sensor for a few cycles and watch the color shift toward red, then let it cool back to green.

!!! tip "Want faster updates?"

    Lower the `update_interval` on the temperature sensor in the YAML pane (for example `update_interval: 10s`) for snappier color changes while you're testing. Raise it back when you're done so the kit isn't broadcasting more often than it needs to.

## Tune the thresholds

Open the Comfortable and Hot triggers in the GUI and edit the **Above** / **Below** numbers to whatever bands fit your space. The three triggers stay independent, so you can move one boundary without touching the others.

!!! success "You've built a sensor-reactive light!"

    Same trigger-then-action pattern, new trigger type. Next, bring it into Home Assistant so the readings show up alongside the rest of your kit.

#### Next Steps

<a href="../../tutorials/connect-to-home-assistant/" class="md-button md-button--primary"><img src="/assets/esphome-logo.svg" /> Next - Connect to Home Assistant</a>
