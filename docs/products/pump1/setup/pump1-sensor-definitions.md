---
title: PUMP-1 Sensor Definitions
description: These are all of the entities exposed by the PUMP-1 to automate on!
---
# Sensor Definitions

This serves as a list of all sensor definitions to help understand what each entity does for your new PUMP-1!

???+ info "Controls"

    **Pump Run Time**

    * Amount of time in seconds to run the pump. Defaults to 10s

    **RGB Light**

    * One RGB Neopixel LED. Click on the light bulb or color wheel to change the color. Click on the toggle to turn on or off.

    **Run Pump**

    * Press button for running the PUMP-1 Pump. This will run for the amount of seconds set above in "Pump Run Time".

    **Run Pump Until Output Wet**

    * Press button for running the PUMP-1 Pump. This will run the pump until the Fluid Output changes to Wet. (Disabled by default)

???+ info "Sensors"

    **Fluid Input**

    * This ultrasonic sensor is located at the bottom of the PUMP-1 water bottle and monitors the presence of fluid. The state remains **"Wet"** while water is present in the bottle, and changes to **"Dry"** once the bottle is completely empty. It reports a state of either **"Wet"** or **"Dry"**.

    **Fluid Output**

    * This ultrasonic sensor can be mounted on the exterior of any container where you need to detect the presence of water on the other side, such as a Keurig reservoir or fish tank. It can be attached using adhesive tape or other mounting methods. The sensor reports **"Wet"** when the water level is above the sensor and **"Dry"** when the level falls below it. It reports a state of either **"Wet"** or **"Dry"**.

???+ info "Configuration"

    **ESP Reboot**

    * Performs a restart of the sensor.

    **Firmware Update**

    * Shows whether a firmware update is available.

    **Hourly Water Check**

    * Automatic water level monitoring with audible alerts.

    **Max Safe Run Time**

    * Maximum time the pump will run before shutting off. Defaults to 100 seconds.

    **Pump Control**

    * Allows you to toggle the pump on and off via a switch. This will still be stopped by the Max Safe Run Time interval set above. (Disabled by default)

    **Stop Pump When Input Dry**

    * This will turn the pump off when the ultrasonic sensor at the bottom of the water bottle detects no water.

    **Stop Pump When Output Wet**

    * This turns the pump off when the ultrasonic sensor (mounted on a Keurig tank, fish tank, or similar container) detects that the water level has risen above its monitoring point.

    **Factory Reset ESP**

    * Factory resets the device (Disabled by default).

    **Pump Safety Override**

    * Allows you to disable the safety features (Disabled by default).

??? info "Diagnostic"

    **ESP Temperature**

    * Displays the current temperature of the ESP32 chip. (Disabled by Default)

    **Online**

    * Shows the connection status.

    **RSSI**

    * Displays the Wi-Fi signal strength.

    **Uptime**

    * Shows the time since last reboot.

[Join our Discord if you need more help! :simple-discord:](https://dsc.gg/apolloautomation){                         .md-button }