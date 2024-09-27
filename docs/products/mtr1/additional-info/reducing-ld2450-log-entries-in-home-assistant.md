# Reducing LD2450 Log Entries In Home Assistant

1. Open your Home Assistant config.yaml
2. Add in this code but use your MTR-1's name

```yaml
logbook:
  exclude:
    entities:
      - binary_sensor.hallway_motion_home_security_motion_detection
```