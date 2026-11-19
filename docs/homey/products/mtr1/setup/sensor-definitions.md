---
title: Sensor Definitions
description: "These are all of the entities exposed by the MTR-1 to automate on!"
---
--8<-- "products/mtr1/setup/sensor-definitions.md:5:60"
    | **Timeout** | 5 s | How long **LD2450 Presence**, **LD2450 Moving Target**, and **LD2450 Still Target** stay on after the radar stops seeing a target of their kind. **LD2450 Presence** starts counting only once the radar sees nobody anywhere in its view. See the <a href="https://esphome.io/components/sensor/ld2450.html#ld2450-binary-sensors" target="_blank" rel="noopener">ESPHome LD2450 docs</a>. |
--8<-- "products/mtr1/setup/sensor-definitions.md:62:"