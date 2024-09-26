# Reducing LD2410 Log Entries In Home Assistant

1. Open your Home Assistant configuration.yaml
2. Add this code to the very bottom but use the entity name of your MSR-2  
    ```yaml
    logbook:
      exclude:
        entities:
          - binary_sensor.hallway_motion_home_security_motion_detection
    ```
3. Check Configuration in Home Assistant developer tools tab to confirm your yaml code is correct.
4. Restart Home Assistant