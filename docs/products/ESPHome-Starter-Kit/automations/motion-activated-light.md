---
title: Turn On a Light with Motion
description: >-
  Build an ESPHome Device Builder automation: the Motion module turns on the
  LED & Buzzer module's RGB light whenever it detects movement.
---
# Turn On a Light with Motion

This tutorial uses the Motion module and the LED & Buzzer module connected to the ESP32-C6. When the PIR sensor detects movement, the RGB light turns on. It's the same trigger-then-action pattern as the [Button Controlled LEDs](button-controlled-leds.md) automation, swapping the button trigger for a motion trigger.

!!! note "Before you start"

    Work through these pages first. This tutorial assumes your device is flashed and both modules are connected:

    * [First Steps](../setup/first-steps.md) to create your starter kit device in ESPHome Device Builder.
    * [Adding the Motion Module](../modules/motion-module.md) to wire up the PIR sensor.
    * [Adding the LED & Buzzer Module](../modules/rgb-buzzer-module.md) to wire up the RGB light.

## Build the automation

ESPHome Device Builder has a GUI for building <a href="https://esphome.io/automations/" target="_blank" rel="noreferrer nofollow noopener">automations</a>, so you can wire a trigger to an action without hand-writing YAML. The trigger is the *when*, the thing that makes it fire. The action is the *then do*, what happens when it fires.

1.  Open your starter kit device in ESPHome Device Builder and click **Edit**. If you need a refresher on the editor, see the [Device Builder Tour](../learning-the-basics/device-builder-tour.md#editor).
2.  In the editor's left pane, expand the **Automations** dropdown and click **Add Automation**.

    ![](../../../assets/esphome-device-builder-add-automation.gif)

3.  Set up the trigger:

    <div class="annotate" markdown>

    - **What should this automation react to?** → **A configured component**
    - **Which configured component?** → **Motion Module (binary_sensor.gpio)**
    - **Which trigger?** → **Binary Sensor → On Press** (1)

    </div>

    1.  **On Press** fires the moment the sensor detects motion. The dropdown also offers **On Release** (the moment motion stops) and **On State** for other occupancy behaviors. You'll use **On Release** in the optional step below to turn the light back off.

4.  Click **Continue**. You land on the **Binary Sensor → On Press** editor with the **Target** already set to your Motion module.
5.  Set up the action:

    <div class="annotate" markdown>

    - Under **Actions**, click **+ Add action**.
    - In the **Add action** dialog, stay on the **By target** tab and choose **Light → Turn On** under the RGB LED group.
    - On the new action, click the **ID** dropdown and select **RGB LEDs**. (1)

    </div>

    1.  The **ID** dropdown only needs changing if your device also has an **Onboard RGB LED** component configured. If **RGB LEDs** is the only light, it's already selected.

??? note "What the GUI built in YAML"

    The form pane and the YAML editor on the right of the editor stay in sync. Your motion section now grows an `on_press` trigger with a `light.turn_on` action:

    ```yaml
    binary_sensor:
      - platform: gpio
        name: Motion Module
        pin: 3
        device_class: motion
        id: motion_module
        on_press:
          then:
            - light.turn_on: rgb_leds
    ```

    See [Device Builder Tour → YAML editor (right)](../learning-the-basics/device-builder-tour.md#yaml-editor-right) for the full breakdown of the YAML pane.

## Install the firmware

Your automation is saved in Device Builder, but the device is still running its old firmware. Compile and install the new code to push the change.

1. Click **Save** in the bottom right of the editor.
2. Click **Install**, then pick **On the Network** to push the new firmware over Wi-Fi.
3. Wait for the compile and flash to finish. The device reboots once the install is done.

![](../../../assets/esphome-device-builder-install-button-component.gif)

## Test the automation

With the device back online, wave your hand in front of the PIR sensor. The RGB light turns on as soon as motion is detected.

!!! tip "Give the Motion sensor a moment to settle"

    PIR sensors need a brief warm-up after powering on, usually 5 to 10 seconds, before their readings stabilize. If the light triggers right after boot with nothing moving, give the sensor a moment.

## Optional: turn the light off when motion stops

Right now the light turns on with motion but never turns off. Add a second trigger to the same Motion module so the light switches off once motion clears.

1. Add another automation, this time choosing **Binary Sensor → On Release** as the trigger for the Motion module.
2. Give it a **Light → Turn Off** action targeting **RGB LEDs**.
3. **Save** and **Install** again.

??? note "What the GUI built in YAML"

    Your motion section now has both triggers:

    ```yaml
    binary_sensor:
      - platform: gpio
        name: Motion Module
        pin: 3
        device_class: motion
        id: motion_module
        on_press:
          then:
            - light.turn_on: rgb_leds
        on_release:
          then:
            - light.turn_off: rgb_leds
    ```

!!! success "You've built a motion-activated light!"

    Same trigger-then-action pattern, new trigger. Swap the action (play a buzzer tune, dim the light, send a notification) or the trigger (a button, a temperature threshold, a schedule) and you have a new automation.
