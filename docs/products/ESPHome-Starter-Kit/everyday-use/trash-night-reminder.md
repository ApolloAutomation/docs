---
title: Trash Night Reminder
description: >-
  Use two Home Assistant Local Calendars and the LED & Buzzer module's RGB
  LEDs to light up your Starter Kit on trash and recycle night.
---
# Trash Night Reminder

<span class="difficulty lvl-2">Difficulty: Level 2</span>

<p class="automation-steps-heading">🌱 New here? Try these first:</p>
<div class="automation-steps">
  <div class="step">
    <a class="step-title" href="../button-toggles-room-light/">Button Toggles a Room Light</a>
    <span class="difficulty lvl-1">Difficulty: Level 1</span>
  </div>
  <div class="step">
    <a class="step-title" href="../motion-activated-room-lights/">Motion-Activated Room Lights</a>
    <span class="difficulty lvl-1">Difficulty: Level 1</span>
  </div>
</div>

Never miss bin night again. Two **Home Assistant Local Calendars** - one for trash, one for recycle - drive a single automation that lights up the Starter Kit's RGB LEDs in a different color for each pickup. When the event starts the LEDs come on; when the event ends they go off.

!!! note "Before you start"

    Work through these pages first. This tutorial assumes your device is flashed, the LED & Buzzer module is wired up, and the kit is connected to Home Assistant:

    * [First Steps](../setup/first-steps.md) to create your starter kit device in ESPHome Device Builder.
    * [Adding the LED & Buzzer Module](../modules/rgb-buzzer-module.md) to wire up the RGB output.
    * [Connect to Home Assistant](../tutorials/connect-to-home-assistant.md) to bring the device's entities into HA.

## Find your RGB LED entity

The LED & Buzzer module's RGB strip shows up in Home Assistant as a light entity.

1. Open [Settings → Devices & services → ESPHome](https://my.home-assistant.io/redirect/integration/?domain=esphome) in Home Assistant.
2. Click your Starter Kit device.
3. Under **Entities**, look for a light entity named **RGB LEDs**. Click it and note the entity ID near the top of the dialog - it will look something like `light.esphome_starter_kit_rgb_leds`. Keep that ID handy.

## Create the calendars

Home Assistant's **Local Calendar** integration stores events entirely inside Home Assistant - no Google account or external service required.

**Add the Trash calendar**

1. Open [Settings → Devices & services](https://my.home-assistant.io/redirect/integrations/) and click **+ Add integration**.
2. Search for **Local Calendar** and select it.
3. Name it `Trash` and click **Submit**. Home Assistant creates a calendar entity called `calendar.trash`.

**Add the Recycle calendar**

4. Click **+ Add integration** again, search for **Local Calendar**, and repeat with the name `Recycle`. This creates `calendar.recycle`.

**Add recurring events**

Add a repeating event to each calendar to match your actual pickup schedule.

5. Open the **Calendar** view in your Home Assistant sidebar. If you do not see it, go to [Settings → Dashboards](https://my.home-assistant.io/redirect/lovelace_dashboards/) and add the **Calendar** panel.
6. Click the first day your trash goes out to open the new-event dialog.

    <div class="annotate" markdown>

    - **Calendar** → **Trash**
    - **Title** → `Trash pickup`
    - Set the **start time** to the evening before your pickup day (for example, 7 PM the night before). (1)
    - Set the **end time** to the morning of pickup day (for example, 9 AM). (2)
    - Enable **Repeat** and set it to **Weekly** on the correct day.

    </div>

    1.  The event start is when the RGB LEDs light up. Setting it to the evening before means the reminder is on while you are home and can act on it.
    2.  The event end is when the LEDs turn back off. Make sure the end time falls after you would normally get the bins back in.

7. Click **Save**.
8. Repeat for the **Recycle** calendar on your recycle pickup day and time.

## Build the automation

One automation handles both calendars. Four triggers - event start and event end for each calendar - feed into a **Choose** action that picks the right color or turns the LEDs off depending on which trigger fired.

**Create the automation**

1. Open [Settings → Automations & scenes](https://my.home-assistant.io/redirect/automations/) and click **+ Create automation** → **Create new automation**.

**Add the triggers**

Add four triggers, one at a time. Each one is a **Calendar** trigger, and each gets a **Trigger ID** so the action block can tell them apart. You set the ID from the trigger's three-dot menu, the same way the [Motion-Activated Room Lights](motion-activated-room-lights.md) automation does.

2. Click **+ Add trigger**, search **Calendar**, and pick the **Calendar** trigger.

    - **Calendar** → `Trash`
    - **Event** → **Start**
    - Open the trigger's three-dot menu, choose **Rename**, and set the **Trigger ID** to `trash_start`.

3. Click **+ Add trigger** and add another **Calendar** trigger.

    - **Calendar** → `Trash`
    - **Event** → **End**
    - Three-dot menu, **Rename**, **Trigger ID** → `trash_end`.

4. Click **+ Add trigger** and add another **Calendar** trigger.

    - **Calendar** → `Recycle`
    - **Event** → **Start**
    - Three-dot menu, **Rename**, **Trigger ID** → `recycle_start`.

5. Click **+ Add trigger** and add another **Calendar** trigger.

    - **Calendar** → `Recycle`
    - **Event** → **End**
    - Three-dot menu, **Rename**, **Trigger ID** → `recycle_end`.

**Add the choose action**

6. Under **Then do**, click **+ Add action** and search for **Choose**.

    The **Choose** block works like a branching decision: it checks each option's condition in order and runs the first one that matches.

7. On the first **Option**, click **+ Add condition** and choose **Triggered by**. Set the **Trigger ID** to `trash_start`. Under the option's **Sequence**, click **+ Add action** → **Perform action** → `light.turn_on`:

    <div class="annotate" markdown>

    - **Target** → your RGB LED entity
    - **RGB color** → Red `255`, Green `140`, Blue `0` (amber) (1)
    - **Brightness** → `100%`

    </div>

    1.  Amber is a warm, high-visibility "take out the trash" color that's easy to tell apart from the blue recycle night across a room. See [Tune the colors](#tune-the-colors) below to match your local bin colors.

8. Click **+ Add option**. Condition: **Triggered by** → `recycle_start`. Sequence: `light.turn_on` targeting the same RGB LED entity:

    - **RGB color** → Red `0`, Green `128`, Blue `255` (blue)
    - **Brightness** → `100%`

9. Click **+ Add option**. Condition: **Triggered by** → set both `trash_end` and `recycle_end`. Sequence: `light.turn_off` targeting the RGB LED entity.

10. Name the automation `Trash night reminder` and click **Save**.

??? note "What the automation looks like in YAML"

    Select **Edit in YAML** from the three-dot menu on the automation to see or paste the raw config. Your entity IDs will differ from the example below.

    ```yaml
    alias: Trash night reminder
    description: Light up the RGB LEDs when a trash or recycle calendar event starts
    triggers:
      - trigger: calendar
        event: start
        entity_id: calendar.trash
        id: trash_start
      - trigger: calendar
        event: end
        entity_id: calendar.trash
        id: trash_end
      - trigger: calendar
        event: start
        entity_id: calendar.recycle
        id: recycle_start
      - trigger: calendar
        event: end
        entity_id: calendar.recycle
        id: recycle_end
    conditions: []
    actions:
      - choose:
          - conditions:
              - condition: trigger
                id: trash_start
            sequence:
              - action: light.turn_on
                target:
                  entity_id: light.esphome_starter_kit_rgb_leds
                data:
                  rgb_color: [255, 140, 0]
                  brightness_pct: 100
          - conditions:
              - condition: trigger
                id: recycle_start
            sequence:
              - action: light.turn_on
                target:
                  entity_id: light.esphome_starter_kit_rgb_leds
                data:
                  rgb_color: [0, 128, 255]
                  brightness_pct: 100
          - conditions:
              - condition: trigger
                id:
                  - trash_end
                  - recycle_end
            sequence:
              - action: light.turn_off
                target:
                  entity_id: light.esphome_starter_kit_rgb_leds
    mode: single
    ```

## Test it

Rather than waiting for your next pickup night, add a short test event to confirm everything fires.

1. Open the **Calendar** view and add a new event on the **Trash** calendar starting one minute from now and ending two minutes from now.
2. Watch the RGB LEDs. They should turn amber at the start time and go off at the end time.
3. Delete the test event once you're done.

!!! success "Your kit is now a physical reminder for Home Assistant events!"

    The same pattern works for any calendar-driven reminder - medication schedules, bin days for a second home, watering days for the garden. Swap the colors, the calendar name, or the action and you have a new reminder with no extra hardware.

## Tune the colors

Change the `rgb_color` values in the automation to match your local bin colors or whatever stands out best in your home.

| Color | RGB values | Suggested use |
| --- | --- | --- |
| Amber | `255, 140, 0` | General trash |
| Blue | `0, 128, 255` | Recycling |
| Green | `0, 200, 0` | Compost or yard waste |
| White | `255, 255, 255` | Bulk pickup or a second reminder |

--8<-- "_snippets/community-help.md"
