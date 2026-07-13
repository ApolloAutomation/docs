---
title: Air Quality on Your Dashboard
description: >-
  Put your SEN65's air quality readings on a Home Assistant dashboard and get a
  push notification when the air goes bad, all with built-in cards and a native
  automation.
---
# Air Quality on Your Dashboard

The [SEN65](../modules/breakout-addons/sen65-air-quality-sensor.md) reads particulate matter, VOC, and NOx, and the AQI component turns your PM readings into a single NowCast AQI number. Putting those on a Home Assistant dashboard gives you a live air quality monitor, and one small automation can nudge you when it's time to open a window. Everything here uses cards and triggers that ship with Home Assistant, so there's nothing to install.

!!! note "Before you start"

    * Your SEN65 is wired to the Breakout Module and added to Home Assistant. If not, start with the [SEN65 Air Quality Sensor](../modules/breakout-addons/sen65-air-quality-sensor.md) page, then [Connect to Home Assistant](../tutorials/connect-to-home-assistant.md).
    * For the gauge and the alert, add the **NowCast AQI** sensor from the [SEN65 YAML](../modules/breakout-addons/sen65-air-quality-sensor.md#add-to-esphome-device-builder). The particulate, VOC, and NOx tiles work without it.

Level 1 is the everyday display. Level 2 adds a gauge and an alert on top. Open your dashboard, click the pencil in the top right to start editing, then follow whichever level you like.

## Level 1: Tile cards

<span class="difficulty lvl-1">Difficulty: Level 1</span>

A Tile card is the small, modern card with an icon, a name, and the current reading. You'll add one each for the readings you check most.

<div class="annotate" markdown>

1. With the dashboard in edit mode, click **Add Card** and open the **By entity** tab.
2. Search `starter kit` and check the readings you want: **PM &lt;2.5µm**, **VOC Index**, **NOx Index**, and **NowCast AQI** are a good starting set. (1)
3. Click **Tile** to lay them out, then click **Save**.

</div>

1.  The preview fills in with the live reading as soon as you pick an entity, so you can confirm you grabbed the right ones.

??? note "Tile cards in YAML"

    Edit any card and choose **Show code editor** to paste one in. Swap in your own entity names; yours usually follow `sensor.<device-name>_nowcast_aqi`.

    ```yaml
    type: tile
    entity: sensor.esphome_starter_kit_pm_2_5um
    ---
    type: tile
    entity: sensor.esphome_starter_kit_nowcast_aqi
    ```

## Level 2: A NowCast AQI gauge

<span class="difficulty lvl-2">Difficulty: Level 2</span>

A Gauge card shines when a higher reading really does mean worse, and NowCast AQI is exactly that: one 0-500 number where bigger is worse. The dial runs green to red as the air degrades.

<div class="annotate" markdown>

1. Click **Add Card** and search for **Gauge**.
2. Set **Entity** to your **NowCast AQI** sensor and give it a **Name** like `Living Room AQI`.
3. Set **Minimum** to `0` and **Maximum** to `500`, the full AQI range.
4. Toggle on **Display as needle gauge**, then turn on **Severity** and set green at `0`, yellow at `51`, and red at `101`. (1)

</div>

1.  Those cutoffs follow the EPA AQI categories: 0 to 50 is Good, 51 to 100 is Moderate, and 101 and up is Unhealthy for Sensitive Groups or worse. Red is your cue to act.

??? note "Gauge card in YAML"

    ```yaml
    type: gauge
    entity: sensor.esphome_starter_kit_nowcast_aqi
    min: 0
    max: 500
    needle: true
    severity:
      green: 0
      yellow: 51
      red: 101
    name: Living Room AQI
    ```

## Level 2: A bad-air alert

<span class="difficulty lvl-2">Difficulty: Level 2</span>

<div class="annotate" markdown>

A dashboard only helps when you're looking at it. This one automation watches the NowCast AQI and pushes a notification to your phone when it crosses into unhealthy air, so you find out from another room. (1)

</div>

1.  Want it to act, not just alert? Add a second action, `switch.turn_on` on a smart-plug purifier or fan, plus a matching automation that turns the plug off when the AQI drops back under 100. The same one-trigger pattern also covers the readings the AQI leaves out: point a **Numeric state** trigger at the **VOC Index** above 100 or the **NOx Index** above 1 to catch cooking and cleaning as they happen.

1. Click the button below to open **Settings → Automations & scenes**, then click **+ Create automation** → **Create new automation**:

    [![Open your Home Assistant instance and show your automations.](https://my.home-assistant.io/badges/automations.svg)](https://my.home-assistant.io/redirect/automations/)

2. Click **+ Add trigger**, search **Numeric state**, and pick the **Numeric state** trigger.

    <div class="annotate" markdown>

    - **Entity** → your **NowCast AQI** sensor
    - **Above** → `100`
    - **For** → 5 minutes (1)

    </div>

    1.  The **For** duration means the AQI has to stay above 100 for five straight minutes before the automation fires, so a quick spike from searing a steak rides out and only air that's actually staying bad reaches your phone.

3. Under **Then do**, click **+ Add action**, search **Notifications**, and pick **Send a notification via device** for your phone.

    - **Message** → `Air quality is unhealthy (NowCast AQI {{ states('sensor.esphome_starter_kit_nowcast_aqi') }}). Time to ventilate.`
    - **Title** → `Air Quality Alert`

4. Name the automation `Air quality alert` and click **Save**.

??? note "Automation in YAML"

    Select **Edit in YAML** from the automation's three-dot menu to see or paste the raw config. Your entity IDs will differ.

    ```yaml
    alias: Air quality alert
    triggers:
      - trigger: numeric_state
        entity_id: sensor.esphome_starter_kit_nowcast_aqi
        above: 100
        for:
          minutes: 5
    actions:
      - action: notify.mobile_app_your_phone
        data:
          title: Air Quality Alert
          message: >-
            Air quality is unhealthy (NowCast AQI
            {{ states('sensor.esphome_starter_kit_nowcast_aqi') }}). Time to
            ventilate.
    mode: single
    ```

--8<-- "_snippets/community-help.md"
