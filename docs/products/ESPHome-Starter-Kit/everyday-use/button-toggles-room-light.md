---
title: Button Toggles a Room Light
description: >-
  Build a Home Assistant automation that uses your ESPHome Starter Kit's
  button to toggle any light in your home.
---
# Button Toggles a Room Light

<span class="difficulty lvl-1">Difficulty: Level 1</span>

The Starter Kit's button already controls the kit's own RGB LEDs in [Button Controlled LEDs](../automations/button-controlled-leds.md). This tutorial takes it further: pressing the button fires a **Home Assistant automation** that toggles any light in your home. Same physical button, but now it reaches across your whole house.

!!! note "Before you start"

    Work through these pages first. This tutorial assumes your device is flashed, the Button module is wired up, and the kit is connected to Home Assistant:

    * [First Steps](../setup/first-steps.md) to create your starter kit device in ESPHome Device Builder.
    * [Adding the Button Module](../modules/button-module.md) to wire up the input.
    * [Connect to Home Assistant](../tutorials/connect-to-home-assistant.md) to bring the device's entities into HA.

## Find your button entity

The Button module shows up in Home Assistant as a binary sensor. You need its entity ID before building the automation.

1. Open [Settings → Devices & services → ESPHome](https://my.home-assistant.io/redirect/integration/?domain=esphome) in Home Assistant.
2. Click your Starter Kit device.
3. Under **Entities**, look for a binary sensor named **Button Module**. Click it to open the entity detail, then note the entity ID shown near the top of the dialog - it will look something like `binary_sensor.esphome_starter_kit_button_module`. Keep that ID handy.

## Build the automation

1. Open [Settings → Automations & scenes](https://my.home-assistant.io/redirect/automations/) in Home Assistant.
2. Click **+ Create automation** in the bottom right, then choose **Create new automation**.
3. Under **Triggers**, click **+ Add trigger** and choose **Entity → State**.

    <div class="annotate" markdown>

    - **Entity** → select your button entity (the binary sensor you found above)
    - **To** → `On` (1)

    </div>

    1.  The button registers as a binary sensor. `On` maps to a pressed state - the moment you push the button down. Home Assistant fires the automation at that instant.

4. Under **Then do**, click **+ Add action** and choose **Perform action** (labeled **Call service** in older versions of Home Assistant).

    <div class="annotate" markdown>

    - Search for and select **light.toggle** (1)
    - Under **Targets**, click **Choose entity** and pick the light you want to control.

    </div>

    1.  `light.toggle` turns the light on if it is off, and off if it is on - one action handles both directions. If you want to always turn on or always turn off, use `light.turn_on` or `light.turn_off` instead.

5. Give the automation a name like `Button toggles room light`.
6. Click **Save**.

??? note "What the automation looks like in YAML"

    Home Assistant stores automations as YAML. Select **Edit in YAML** from the three-dot menu on the automation to see or paste the raw config. Your entity IDs will differ from the example below.

    ```yaml
    alias: Button toggles room light
    triggers:
      - trigger: state
        entity_id: binary_sensor.esphome_starter_kit_button_module
        to: "on"
    actions:
      - action: light.toggle
        target:
          entity_id: light.your_room_light
    mode: single
    ```

## Test the automation

Press the button on the Button module. The light you targeted toggles. Press again and it toggles back.

!!! success "Your kit is now a physical remote for Home Assistant!"

    Any light in your home - a bedside lamp, a ceiling group, a smart bulb strip - is one button press away. Swap `light.toggle` for `light.turn_on` with a `brightness_pct` to land on a specific brightness, or target a light group to control a whole room at once.

<a href="../trash-night-reminder/" class="md-button md-button--primary"><img src="/assets/esphome-logo.svg" /> Next - Trash Night Reminder</a>

--8<-- "_snippets/community-help.md"
