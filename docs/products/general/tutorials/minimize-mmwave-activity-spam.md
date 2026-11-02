---
title: How to minimize activity spam
description: How to keep Apollo mmWave sensors from flooding the Activity log and the Home Assistant database
---
# Minimize activity spam

Apollo mmWave sensors report frequently by design, which can cause internal radar entities like target direction, target count, and zone occupancy to flood your Home Assistant Activity log. Adding a `logbook.exclude` block to your `configuration.yaml` hides those entities from **Activity**. It does not stop Home Assistant from saving their history. On an MTR-1 or R PRO-1, also [stop recording the LD2450 target positions](#stop-recording-ld2450-target-positions).

!!! info "Home Assistant Activity Documentation"

    For more details on activity filtering, see the [Home Assistant Logbook integration docs](https://www.home-assistant.io/integrations/logbook/).

1\. Open your Home Assistant `configuration.yaml` file.

2\. Select your sensor below and copy the snippet, then paste it into `configuration.yaml`.

=== "MSR-1 / MSR-2"

    ```yaml
    logbook:
      exclude:
        entity_globs:
          # LD2410
          - binary_sensor.*radar_moving_target
          - binary_sensor.*radar_still_target
          - binary_sensor.*radar_zone*occupancy
    ```

=== "MTR-1"

    ```yaml
    logbook:
      exclude:
        entity_globs:
          # LD2450
          - binary_sensor.*ld2450_*
          - sensor.*target_*_direction*
          - sensor.*target_count*
    ```

=== "R PRO-1"

    ```yaml
    logbook:
      exclude:
        entity_globs:
          # LD2450
          - binary_sensor.*ld2450_*
          - sensor.*target_*_direction*
          - sensor.*target_count*
          # LD2412
          - binary_sensor.*ld2412_*
    ```

!!! warning "If you already have a `logbook:` section"

    Do not add a second `logbook:` key. Merge the `exclude.entity_globs` list into your existing section.

3\. Save `configuration.yaml` and restart Home Assistant (**Settings → System → Restart**).

[![Open your Home Assistant instance and show the system dashboard.](https://my.home-assistant.io/badges/system_dashboard.svg)](https://my.home-assistant.io/redirect/system_dashboard/)

4\. Open **Activity** in Home Assistant to confirm the noisy entities no longer appear.

## Stop recording LD2450 target positions

The MTR-1 and the R PRO-1 have an LD2450 radar that tracks up to three people. For each one it reports X, Y, angle, distance, speed and direction several times a second, and the Home Assistant recorder saves every change to its database. In our testing, one R PRO-1 saved about 460,000 changes in a single day from Target 1 alone, while it tracked an object that never moved.

The `logbook.exclude` block above only hides entities from Activity. A `recorder.exclude` block stops the saving. The Apollo mmWave zone map, the drawn zone presence sensors and the Apollo mmWave dashboard read the live values, so they keep working. From then on, the history graphs of these sensors get no new readings. Readings saved before stay until you delete them in step 5 or Home Assistant's regular cleanup removes them.

!!! info "Home Assistant Recorder Documentation"

    For more details on excluding entities, see the [Home Assistant Recorder integration docs](https://www.home-assistant.io/integrations/recorder/).

1\. Open your Home Assistant `configuration.yaml` file.

2\. Copy this snippet and paste it into `configuration.yaml`. The same snippet works for the MTR-1 and the R PRO-1.

```yaml
recorder:
  exclude:
    entity_globs:
      # LD2450 Target 1 to 3: X, Y, angle, distance, speed, direction
      - sensor.*_target_?_*
```

!!! warning "If you already have a `recorder:` section"

    Do not add a second `recorder:` key. Merge the `exclude.entity_globs` entry into your existing section.

3\. Check what the pattern matches before you restart. Go to **Developer tools → States** (**Settings → Tools → States** in Home Assistant 2026.8 and newer) and filter for `_target_`. The pattern matches sensors whose ID has `_target_`, then one character, then `_`, such as `sensor.office_r_pro_1_ld2450_target_1_x`. It skips target counts, presence and the LD2410 sensors of the MSR-1 and MSR-2. If it also matches a sensor from another device that you want to keep, list the Apollo sensors by name under `entities:` instead of `entity_globs:`.

[![Open your Home Assistant instance and show your state tools.](https://my.home-assistant.io/badges/tools_states.svg)](https://my.home-assistant.io/redirect/tools_states/)

4\. Save `configuration.yaml` and restart Home Assistant (**Settings → System → Restart**).

[![Open your Home Assistant instance and show the system dashboard.](https://my.home-assistant.io/badges/system_dashboard.svg)](https://my.home-assistant.io/redirect/system_dashboard/)

5\. Optional: Home Assistant keeps the history it already saved until its regular cleanup, after 10 days by default. To delete it now, go to **Developer tools → Actions** (**Settings → Tools → Actions** in Home Assistant 2026.8 and newer), switch to YAML mode and perform this action:

```yaml
action: recorder.purge_entities
data:
  entity_globs:
    - sensor.*_target_?_*
  keep_days: 0
```

!!! warning "If you listed the sensors by name in step 3"

    The action above deletes the saved history of every sensor the pattern matches, including sensors you chose to keep. Purge the same list you put under `entities:` instead:

    ```yaml
    action: recorder.purge_entities
    target:
      entity_id:
        - sensor.office_r_pro_1_ld2450_target_1_x
        - sensor.office_r_pro_1_ld2450_target_1_y
    data:
      keep_days: 0
    ```

[![Open your Home Assistant instance and show your action tools.](https://my.home-assistant.io/badges/tools_actions.svg)](https://my.home-assistant.io/redirect/tools_actions/)
