---
title: How to minimize activity spam
description: How to minimize the activity spam on your Apollo mmWave sensors
---
# Minimize Activity Spam

Apollo mmWave sensors report frequently by design, which can cause internal radar entities like target direction, target count, and zone occupancy to flood your Home Assistant Activity log. Adding a `logbook.exclude` block to your `configuration.yaml` tells Home Assistant to stop recording those entities.

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

=== "R-PRO-1"

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

4\. Open **Activity** in Home Assistant to confirm the noisy entities no longer appear.
