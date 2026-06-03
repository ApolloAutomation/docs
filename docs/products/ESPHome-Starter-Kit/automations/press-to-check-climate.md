---
title: Press to Check Climate
description: >-
  ESPHome Device Builder automation: one button click flashes the Onboard RGB
  LED for the current temperature band, then for humidity. Available in a
  hardcoded-thresholds version and an editable / unit-toggle version.
---
# Press to Check Climate

<span class="difficulty lvl-3">Difficulty: Level 3</span>

<p class="automation-steps-heading">🌱 New here? Try these first:</p>
<div class="automation-steps">
  <div class="step">
    <a class="step-title" href="../motion-activated-light/">Turn On a Light with Motion</a>
    <span class="difficulty lvl-1">Difficulty: Level 1</span>
  </div>
  <div class="step">
    <a class="step-title" href="../button-controlled-leds/">Build a Button-Controlled RGB Light</a>
    <span class="difficulty lvl-1">Difficulty: Level 1</span>
  </div>
</div>

Want a quick read on how the room feels without opening Home Assistant? Press the button and the **Onboard RGB LED** gives you one color for the current temperature, then another for the current humidity.

The Onboard RGB LED on the ESP32-C6 is all you need for this tutorial, so the LED & Buzzer module can sit this one out.

!!! note "Before you start"

    Work through these pages first. This tutorial assumes your device is flashed and all three components are connected:

    * [First Steps](../setup/first-steps.md) to create your starter kit device and add the **Onboard RGB LED** component.
    * [Adding the Button Module](../modules/button-module.md) to wire up the input.
    * [Adding the Temperature and Humidity Module](../modules/temperature-humidity-module.md) to wire up the sensor.

## Build the automation

This tutorial has two versions of the same automation. Both end with the same button-press readout. Pick the tab below.

- **Beginner** uses hardcoded thresholds (18 °C and 24 °C for temperature, 30% and 60% for humidity) and Device Builder's `Sensor → In Range` condition. No lambda, no extra components.
- **Advanced** adds four user-editable threshold number entities plus a °C / °F select, with lambda conditions that convert at compare time. Tune from the web server or Home Assistant any time, no re-flash.

#### Color bands

| Temperature band | Color | | Humidity band | Color |
| --- | --- | --- | --- | --- |
| Below 18 °C (64 °F) | Blue | | Below 30% | Orange |
| 18 °C to 24 °C (64 °F to 75 °F) | Green | | 30% to 60% | Green |
| Above 24 °C (75 °F) | Red | | Above 60% | Blue |

=== "Beginner"

    Hardcoded thresholds, no extra components.

    !!! note "The GUI fields take Celsius numbers"

        The AHT20 sensor publishes its readings in Celsius, so the **Above** and **Below** values you enter for the temperature `If` conditions need to be Celsius numbers. The Fahrenheit equivalents in the table above are for reference only.

    A single **Button → On Click** automation whose action body chains nine steps: three `If` conditions for temperature, a delay and clear, another delay, three `If` conditions for humidity, a final delay and clear.

    1.  Open your starter kit device in ESPHome Device Builder and click **Edit**. If you need a refresher on the editor, see the [Device Builder Tour](../learning-the-basics/device-builder-tour.md#editor).
    2.  In the editor's left pane, expand the **Automations** dropdown and click **Add Automation**.
    3.  Set up the trigger:

        <div class="annotate" markdown>

        - **What should this automation react to?** → **A configured component**
        - **Which configured component?** → **Button Module (binary_sensor.gpio)**
        - **Which trigger?** → **Binary Sensor → On Click**

        </div>

    4.  Click **Continue**. You land on the **Binary Sensor → On Click** editor with the **Target** already set to your Button module.

    #### Show the temperature band

    Three `If` actions, one per band. Each `If` checks whether the temperature is inside its band and, if so, turns the LED to that band's color.

    1.  Under **Actions**, click **+ Add action** and choose **Control flow → If**.
    2.  On the new `If` action, set the **Condition**:

        - **Condition type** → **Sensor → In Range**
        - **ID** → **Temperature**
        - **Below** → `18.0` (leave **Above** blank)

    3.  Under the `If`'s **Then** branch, click **+ Add action** and pick **Light → Turn On**:

        <div class="annotate" markdown>

        - **ID** → **Onboard RGB LED**
        - **Brightness** `100%` (1)
        - **Red** `0%`, **Green** `0%`, **Blue** `100%`

        </div>

        1.  Setting **Brightness** explicitly on every `Light → Turn On` keeps the colors at full output. If you leave it off and someone dims the LED from the web server or Home Assistant beforehand, your "red" comes back muted at whatever brightness was last set.

    4.  Add a second `If` for the comfortable band. Condition: **Above** `18.0`, **Below** `24.0`. Color: green (**Red** `0%`, **Green** `100%`, **Blue** `0%`).

        ??? example "Show the click-by-click"

            1.  Under **Actions**, click **+ Add action** and choose **Control flow → If**.
            2.  Set the **Condition**:

                - **Condition type** → **Sensor → In Range**
                - **ID** → **Temperature**
                - **Above** → `18.0`
                - **Below** → `24.0`

            3.  Under the `If`'s **Then** branch, click **+ Add action** and pick **Light → Turn On**:

                - **ID** → **Onboard RGB LED**
                - **Brightness** `100%`
                - **Red** `0%`, **Green** `100%`, **Blue** `0%`

    5.  Add a third `If` for the hot band. Condition: **Above** `24.0` (leave **Below** blank). Color: red (**Red** `100%`, **Green** `0%`, **Blue** `0%`).

        ??? example "Show the click-by-click"

            1.  Under **Actions**, click **+ Add action** and choose **Control flow → If**.
            2.  Set the **Condition**:

                - **Condition type** → **Sensor → In Range**
                - **ID** → **Temperature**
                - **Above** → `24.0` (leave **Below** blank)

            3.  Under the `If`'s **Then** branch, click **+ Add action** and pick **Light → Turn On**:

                - **ID** → **Onboard RGB LED**
                - **Brightness** `100%`
                - **Red** `100%`, **Green** `0%`, **Blue** `0%`

    #### Pause, then clear the LED

    After the three `If` actions, the LED is showing the temperature band's color. Hold it for 3 seconds, then turn it off for 1 second before showing humidity.

    1.  Add a **Control flow → Delay** of `3s`.
    2.  Add **Light → Turn Off** on **Onboard RGB LED**.
    3.  Add a **Control flow → Delay** of `1s`. This gap is what tells the viewer the next color is humidity, not temperature.

    #### Show the humidity band

    Same shape as the temperature section, three `If` actions with `Sensor → In Range` conditions on **Humidity**.

    1.  Add an `If` with condition **Sensor → In Range**, **ID** **Humidity**, **Below** `30.0`. Action: **Light → Turn On** with **Brightness** `100%`, **Red** `100%`, **Green** `50%`, **Blue** `0%` (orange).
    2.  Add a second `If`: **Above** `30.0`, **Below** `60.0`. Action: **Brightness** `100%`, **Red** `0%`, **Green** `100%`, **Blue** `0%` (green).
    3.  Add a third `If`: **Above** `60.0`. Action: **Brightness** `100%`, **Red** `0%`, **Green** `0%`, **Blue** `100%` (blue).

    #### Hold, then clear

    1.  Add a **Control flow → Delay** of `3s`.
    2.  Add a final **Light → Turn Off**, **ID** → **Onboard RGB LED**.

    ??? note "What the GUI built in YAML"

        Your button section now has a single `on_click` trigger that runs the full sequence:

        ```yaml
        binary_sensor:
          - platform: gpio
            name: Button Module
            pin:
              inverted: true
              mode:
                input: true
                pullup: true
              number: 6
            id: button_module
            on_click:
              then:
                - if:
                    condition:
                      sensor.in_range:
                        id: aht_temperature
                        below: 18.0
                    then:
                      - light.turn_on:
                          id: onboard_rgb_led
                          brightness: 100%
                          red: 0%
                          green: 0%
                          blue: 100%
                - if:
                    condition:
                      sensor.in_range:
                        id: aht_temperature
                        above: 18.0
                        below: 24.0
                    then:
                      - light.turn_on:
                          id: onboard_rgb_led
                          brightness: 100%
                          red: 0%
                          green: 100%
                          blue: 0%
                - if:
                    condition:
                      sensor.in_range:
                        id: aht_temperature
                        above: 24.0
                    then:
                      - light.turn_on:
                          id: onboard_rgb_led
                          brightness: 100%
                          red: 100%
                          green: 0%
                          blue: 0%
                - delay: 3s
                - light.turn_off: onboard_rgb_led
                - delay: 1s
                - if:
                    condition:
                      sensor.in_range:
                        id: aht_humidity
                        below: 30.0
                    then:
                      - light.turn_on:
                          id: onboard_rgb_led
                          brightness: 100%
                          red: 100%
                          green: 50%
                          blue: 0%
                - if:
                    condition:
                      sensor.in_range:
                        id: aht_humidity
                        above: 30.0
                        below: 60.0
                    then:
                      - light.turn_on:
                          id: onboard_rgb_led
                          brightness: 100%
                          red: 0%
                          green: 100%
                          blue: 0%
                - if:
                    condition:
                      sensor.in_range:
                        id: aht_humidity
                        above: 60.0
                    then:
                      - light.turn_on:
                          id: onboard_rgb_led
                          brightness: 100%
                          red: 0%
                          green: 0%
                          blue: 100%
                - delay: 3s
                - light.turn_off: onboard_rgb_led
        ```

=== "Advanced"

    Same on-press sequence, but the four band thresholds live in editable `number` components and a `select` lets you switch between °C and °F. Tune from the web server or Home Assistant any time, no re-flash.

    #### Add the tunable components

    Before the automation can compare against editable thresholds, the device needs five new components: two number entities for temperature bounds, two for humidity bounds, and one select to pick the temperature unit.

    **Temperature threshold numbers**

    1.  In Device Builder, click **Edit** on your starter kit device.
    2.  Scroll to **Components** and click **+ Add Component**.
    3.  Search for **Template Number** and click **Add**.
    4.  Fill in the form:

        <div class="annotate" markdown>

        - **Name** → `Cold threshold`
        - **ID** → `temp_min`
        - **Initial value** → `18`
        - **Min value** → `-50`
        - **Max value** → `200`
        - **Step** → `0.5`
        - **Mode** → **Box**
        - **Optimistic** → on
        - **Restore value** → on (1)

        </div>

        1.  **Restore value** persists the user's last value to flash so a reboot doesn't reset the threshold to its `initial_value`.

    5.  Click **Add** again and repeat for the hot threshold: **Name** `Hot threshold`, **ID** `temp_max`, **Initial value** `24`, same min/max/step/mode/optimistic/restore settings.

    **Humidity threshold numbers**

    Add two more template numbers with humidity-appropriate bounds.

    1.  **Name** `Dry threshold`, **ID** `humidity_min`, **Initial value** `30`, **Min value** `0`, **Max value** `100`, **Step** `1`, **Mode** **Box**, **Optimistic** on, **Restore value** on.
    2.  **Name** `Humid threshold`, **ID** `humidity_max`, **Initial value** `60`, same min/max/step/mode/optimistic/restore.

    **Temperature unit select**

    1.  Click **+ Add Component**, search for **Template Select**, and click **Add**.
    2.  Fill in the form:

        - **Name** → `Temperature unit`
        - **ID** → `temp_unit`
        - **Options** → `°C` and `°F` (one per line)
        - **Initial option** → `°C`
        - **Optimistic** → on
        - **Restore value** → on

    3.  Click **Add**.

    ??? note "What the GUI built in YAML (components)"

        ```yaml
        number:
          - platform: template
            name: "Cold threshold"
            id: temp_min
            initial_value: 18
            min_value: -50
            max_value: 200
            step: 0.5
            mode: box
            optimistic: true
            restore_value: true
          - platform: template
            name: "Hot threshold"
            id: temp_max
            initial_value: 24
            min_value: -50
            max_value: 200
            step: 0.5
            mode: box
            optimistic: true
            restore_value: true
          - platform: template
            name: "Dry threshold"
            id: humidity_min
            initial_value: 30
            min_value: 0
            max_value: 100
            step: 1
            mode: box
            optimistic: true
            restore_value: true
          - platform: template
            name: "Humid threshold"
            id: humidity_max
            initial_value: 60
            min_value: 0
            max_value: 100
            step: 1
            mode: box
            optimistic: true
            restore_value: true

        select:
          - platform: template
            name: "Temperature unit"
            id: temp_unit
            options:
              - "°C"
              - "°F"
            initial_option: "°C"
            optimistic: true
            restore_value: true
        ```

    #### Build the action sequence

    Same single **Button → On Click** automation as the Beginner version, but each `If` uses a **Lambda** condition that reads the user's threshold from a number entity, converts to °C if the select says °F, and compares against the raw sensor value.

    !!! tip "ESPHome ships unit-conversion helpers"

        Lambdas can call `fahrenheit_to_celsius(value)` and `celsius_to_fahrenheit(value)` directly (defined in <a href="https://github.com/esphome/esphome/blob/dev/esphome/core/helpers.h" target="_blank" rel="noreferrer nofollow noopener">esphome/core/helpers.h</a>). No `#include`, no math by hand.

    !!! warning "The `°F` in your lambda must match the `°F` in your select"

        The lambda comparisons below check `id(temp_unit).state == "°F"`. That string comparison is byte-exact. If the `°` character in your select options came from a different keyboard layout than the one in the lambda (some layouts produce U+00B0 DEGREE SIGN, others produce U+02DA RING ABOVE, which looks identical), the comparison silently always returns false and °F mode never triggers. Copy-paste the `°` from one place to the other to be safe, or change the select options and the lambda comparisons to plain `"C"` / `"F"`.

    1.  Expand the **Automations** dropdown, click **Add Automation**.
    2.  Set up the trigger:

        - **What should this automation react to?** → **A configured component**
        - **Which configured component?** → **Button Module (binary_sensor.gpio)**
        - **Which trigger?** → **Binary Sensor → On Click**

    3.  Click **Continue**.

    **Show the temperature band**

    Three `If` actions with **Lambda** conditions, one per band.

    1.  Under **Actions**, click **+ Add action** and choose **Control flow → If**.
    2.  Set the **Condition**:

        - **Condition type** → **Lambda**
        - Paste in the body below.

        ```cpp
        float t = id(temp_min).state;
        if (id(temp_unit).state == "°F") t = fahrenheit_to_celsius(t);
        return id(aht_temperature).state < t;
        ```

    3.  Under the `If`'s **Then** branch, click **+ Add action** and pick **Light → Turn On**:

        - **ID** → **Onboard RGB LED**
        - **Brightness** `100%`
        - **Red** `0%`, **Green** `0%`, **Blue** `100%`

    4.  Add a second `If`. Lambda condition body:

        ```cpp
        bool is_f = id(temp_unit).state == "°F";
        float tmin = is_f ? fahrenheit_to_celsius(id(temp_min).state) : id(temp_min).state;
        float tmax = is_f ? fahrenheit_to_celsius(id(temp_max).state) : id(temp_max).state;
        float t = id(aht_temperature).state;
        return t >= tmin && t <= tmax;
        ```

        **Then** → **Light → Turn On** **Onboard RGB LED** with **Brightness** `100%`, **Red** `0%`, **Green** `100%`, **Blue** `0%`.

    5.  Add a third `If`. Lambda condition body:

        ```cpp
        float t = id(temp_max).state;
        if (id(temp_unit).state == "°F") t = fahrenheit_to_celsius(t);
        return id(aht_temperature).state > t;
        ```

        **Then** → **Light → Turn On** **Onboard RGB LED** with **Brightness** `100%`, **Red** `100%`, **Green** `0%`, **Blue** `0%`.

    **Pause, then clear the LED**

    1.  Add a **Control flow → Delay** of `3s`.
    2.  Add **Light → Turn Off** on **Onboard RGB LED**.
    3.  Add a **Control flow → Delay** of `1s`.

    **Show the humidity band**

    Three more `If` actions with lambda conditions. No unit conversion needed (humidity is always a percent).

    1.  Lambda condition:

        ```cpp
        return id(aht_humidity).state < id(humidity_min).state;
        ```

        **Then** → **Light → Turn On** **Onboard RGB LED** with **Brightness** `100%`, **Red** `100%`, **Green** `50%`, **Blue** `0%` (orange).

    2.  Second `If`:

        ```cpp
        float h = id(aht_humidity).state;
        return h >= id(humidity_min).state && h <= id(humidity_max).state;
        ```

        **Then** → **Light → Turn On** with **Brightness** `100%`, **Red** `0%`, **Green** `100%`, **Blue** `0%` (green).

    3.  Third `If`:

        ```cpp
        return id(aht_humidity).state > id(humidity_max).state;
        ```

        **Then** → **Light → Turn On** with **Brightness** `100%`, **Red** `0%`, **Green** `0%`, **Blue** `100%` (blue).

    **Hold, then clear**

    1.  Add a **Control flow → Delay** of `3s`.
    2.  Add a final **Light → Turn Off**, **ID** → **Onboard RGB LED**.

    ??? note "What the GUI built in YAML"

        ```yaml
        binary_sensor:
          - platform: gpio
            name: Button Module
            pin:
              inverted: true
              mode:
                input: true
                pullup: true
              number: 6
            id: button_module
            on_click:
              then:
                - if:
                    condition:
                      lambda: |-
                        float t = id(temp_min).state;
                        if (id(temp_unit).state == "°F") t = fahrenheit_to_celsius(t);
                        return id(aht_temperature).state < t;
                    then:
                      - light.turn_on:
                          id: onboard_rgb_led
                          brightness: 100%
                          red: 0%
                          green: 0%
                          blue: 100%
                - if:
                    condition:
                      lambda: |-
                        bool is_f = id(temp_unit).state == "°F";
                        float tmin = is_f ? fahrenheit_to_celsius(id(temp_min).state) : id(temp_min).state;
                        float tmax = is_f ? fahrenheit_to_celsius(id(temp_max).state) : id(temp_max).state;
                        float t = id(aht_temperature).state;
                        return t >= tmin && t <= tmax;
                    then:
                      - light.turn_on:
                          id: onboard_rgb_led
                          brightness: 100%
                          red: 0%
                          green: 100%
                          blue: 0%
                - if:
                    condition:
                      lambda: |-
                        float t = id(temp_max).state;
                        if (id(temp_unit).state == "°F") t = fahrenheit_to_celsius(t);
                        return id(aht_temperature).state > t;
                    then:
                      - light.turn_on:
                          id: onboard_rgb_led
                          brightness: 100%
                          red: 100%
                          green: 0%
                          blue: 0%
                - delay: 3s
                - light.turn_off: onboard_rgb_led
                - delay: 1s
                - if:
                    condition:
                      lambda: 'return id(aht_humidity).state < id(humidity_min).state;'
                    then:
                      - light.turn_on:
                          id: onboard_rgb_led
                          brightness: 100%
                          red: 100%
                          green: 50%
                          blue: 0%
                - if:
                    condition:
                      lambda: |-
                        float h = id(aht_humidity).state;
                        return h >= id(humidity_min).state && h <= id(humidity_max).state;
                    then:
                      - light.turn_on:
                          id: onboard_rgb_led
                          brightness: 100%
                          red: 0%
                          green: 100%
                          blue: 0%
                - if:
                    condition:
                      lambda: 'return id(aht_humidity).state > id(humidity_max).state;'
                    then:
                      - light.turn_on:
                          id: onboard_rgb_led
                          brightness: 100%
                          red: 0%
                          green: 0%
                          blue: 100%
                - delay: 3s
                - light.turn_off: onboard_rgb_led
        ```

    #### Tune your thresholds without re-flashing

    After Install, the four threshold numbers and the unit select live in the web server and Home Assistant. Change any of them from a browser and the next button press uses the new values immediately. No recompile required.

    !!! warning "Changing the unit doesn't auto-convert your stored values"

        If you switch **Temperature unit** from `°C` to `°F` after entering thresholds, the stored numbers stay the same: `18` was 18 °C, now it's interpreted as 18 °F (which is about −7.8 °C). The simplest fix is to set the unit first, then enter your thresholds in that unit. For an automatic conversion when the select changes, see the optional section below.

    #### Optional: auto-convert thresholds when the unit changes

    Add an `on_value` action to the `Temperature unit` select so that switching `°C` ↔ `°F` rewrites both temperature threshold numbers to the equivalent value in the new unit. This is a YAML-only edit because tracking the previous select value needs a `globals:` block.

    1.  In the YAML pane, add a `globals:` section that records the last unit:

        ```yaml
        globals:
          - id: prev_temp_unit
            type: std::string
            restore_value: true
            initial_value: '"°C"'
        ```

    2.  Under your `Temperature unit` select, add an `on_value` block:

        ```yaml
        select:
          - platform: template
            name: "Temperature unit"
            id: temp_unit
            options:
              - "°C"
              - "°F"
            initial_option: "°C"
            optimistic: true
            restore_value: true
            on_value:
              - then:
                  - if:
                      condition:
                        lambda: 'return id(prev_temp_unit) == "°C" && x == "°F";'
                      then:
                        - number.set:
                            id: temp_min
                            value: !lambda 'return celsius_to_fahrenheit(id(temp_min).state);'
                        - number.set:
                            id: temp_max
                            value: !lambda 'return celsius_to_fahrenheit(id(temp_max).state);'
                  - if:
                      condition:
                        lambda: 'return id(prev_temp_unit) == "°F" && x == "°C";'
                      then:
                        - number.set:
                            id: temp_min
                            value: !lambda 'return fahrenheit_to_celsius(id(temp_min).state);'
                        - number.set:
                            id: temp_max
                            value: !lambda 'return fahrenheit_to_celsius(id(temp_max).state);'
                  - lambda: 'id(prev_temp_unit) = x;'
        ```

    3.  Save and install. Flip the unit select once each direction to verify the numbers convert as you'd expect.

## Install the firmware

Your automation is saved in Device Builder, but the device is still running its old firmware. Compile and install the new code to push the change.

1. Click **Save** in the bottom right of the editor.
2. Click **Install**, then pick **On the Network** to push the new firmware over Wi-Fi.
3. Wait for the compile and flash to finish. The device reboots once the install is done.

## Test the automation

With the device back online, press the button on the Button module. The Onboard RGB LED runs the full sequence in seven seconds: temperature color for 3 s, dark for 1 s, humidity color for 3 s, dark. Press it again any time you want a quick read.

#### Troubleshooting

- **The colors don't reflect what I just did to the sensor.** The temp and humidity sensors publish on a schedule (every 60 seconds by default), so the colors show the most recent reading, not a fresh check at the moment of the press. Lower the sensor's `update_interval` while testing for snappier feedback.
- **First press after boot does nothing.** Right after boot, the sensor hasn't published a reading yet, so the `If` comparisons silently come back false and the LED stays as-is. Wait one publish cycle (60 seconds by default) and try again.

#### Next steps

The same trigger / condition / delay / light pattern works with any sensor and any light on your kit. Swap the temperature sensor for a CO2 reading, the button trigger for a motion event, or the Onboard RGB LED for the LED & Buzzer module's `rgb_leds` strip, and you have a new readout. Then bring it into Home Assistant so you can tune it from anywhere.

<a href="../../tutorials/connect-to-home-assistant/" class="md-button md-button--primary"><img src="/assets/esphome-logo.svg" /> Next - Connect to Home Assistant</a>


--8<-- "_snippets/community-help.md"
