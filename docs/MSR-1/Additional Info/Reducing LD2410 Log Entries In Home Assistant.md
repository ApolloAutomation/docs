# Reducing LD2410 Log Entries In Home Assistant

1. Open your Home Assistant config.yaml
2. Add in this code but use your MSR-1's name

```yaml
logbook:
  exclude:
    entities:
      - binary_sensor.hallway_motion_home_security_motion_detection
```