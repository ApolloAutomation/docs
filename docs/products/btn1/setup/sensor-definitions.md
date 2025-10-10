---
title: BTN-1 Sensor Definitions
description: These are all of the entities exposed by the BTN-1 to automate on!
---
# Sensor Definitionsddw

This serves as a list of all sensor definitions to help understand what each entity does for your new BTN-1!

???+ info "Controls"

    **BTN 1 Light**

    * Controls the light in front of the first button. Defaults to off.

    **BTN 2 Light**

    * Controls the light in front of the second button. Defaults to off.

    **BTN 3 Light**

    * Controls the light in front of the third button. Defaults to off.

    **BTN 4 Light**

    * Controls the light in front of the fourth button. Defaults to off.

???+ info "Sensors"

    **Battery level**

    * Displays the remaining battery percentage. Values range from 0-100%

    **Battery voltage**

    * Represents the current voltage level of the battery for real-time monitoring.

    **Wake-up Button Pressed**

    * Counter to let you know when the wake-up button is pressed. Defaults to 0.

???+ info "Events"

    **Button 1**

    * Displays a Single Click, Double Click, Four Clicks and Hold Event for Button 1. Great for automating!

    **Button 2**

    * Displays a Single Click, Double Click, Four Clicks and Hold Event for Button 2. Great for automating!

    **Button 3**

    * Displays a Single Click, Double Click, Four Clicks and Hold Event for Button 3. Great for automating!

    **Button 4**

    * Displays a Single Click, Double Click, Four Clicks and Hold Event for Button 4. Great for automating!

???+ info "Configuration"

    **Prevent Sleep**

    * Prevents the device from going to sleep. When sleeping, your BTN-1 will NOT respond to Home Assistant it is effectively off until it wakes up again. Defaults to ON.

    **Sleep Duration**

    * The number of hours the device should remain in sleep mode before waking up. Defaults to 24 hours.

    **Firmware Update**

    * Indicates whether an update is available or if you are Up-to-date.

??? info "Diagnostic"

    **ESP Temperature**

    * Displays the current temperature of the ESP32 chip. (Disabled by Default)

    **Online**

    * Shows the connection status.

    **RSSI**

    * Displays the Wi-Fi signal strength.

    **Uptime**

    * Shows the time since last reboot.

[Join our Discord if you need more help! :simple-discord:](https://dsc.gg/apolloautomation){                             .md-button }