# TEMP-1B Sensor Definitions

Once added to Home Assistant you can configure different settings for your sensor. Below is what each setting does.

???+ info "Controls"

    **Alarm Outside Temp Range**

    * Alarm that sounds when the thresholds are met for the sensor.
    * Click on the toggle to turn on or off. Defaults to OFF.

    **RGB Light**

    * <a href="https://esphome.io/components/light/index.html#light-effects" target="_blank" rel="noopener">One RGB Neopixel LED</a>. Click on the light bulb or color wheel to change the color. Click on the toggle to turn on or off.

    **Temp Probe Select**

    * Choose the probe connected to the TEMP-1B. The options are Dallas or Food. The Dallas sensor is a temperature probe (available in long or short versions), while the Food probe is a stainless steel, food-safe option suitable for use with a grill.

???+ info "Sensors"

    **Battery level**

    * Displays the remaining battery percentage. Values range from 0-100%

    **Battery voltage**

    * Represents the current voltage level of the battery for real-time monitoring.

    **Board Humidity**

    * Measures and reports the current humidity level on the board.

    **Board Temperature**

    * Measures and reports the current temperature of the board.

    **Food Probe**

    * The stainless steel food-safe probe is designed for accurate temperature monitoring during grilling, baking, and other food-related activities. Its durable, non-corrosive construction ensures safe and reliable use for cooking, providing real-time temperature readings to help achieve perfect results.

    **Temperature Probe**

    * The temperature sensor probe, offered in both long and short options, is ideal for monitoring fridge/freezer temperatures and aquatic environments like fish tanks, hot tubs, and covered pools. Its flat cable prevents interference with fridge seals, and it includes a customizable temperature threshold with an onboard buzzer to alert when the limit is exceeded.

???+ info "Configuration"

    **Board Humidity Offset**

    * Offset for Board Humidity - values between 0-100%

    **Board Temperature Offset**

    * Offset for Board Temperature - values in Celsius.

    **ESP Reboot**

    * Button to press which reboots your TEMP-1B.

    **Firmware Update**

    * Indicates whether an update is available or if you are Up-to-date.

    **Food Probe Offset**

    * Offset for the Food Probe's temperature readings. Measured in Celsius.

    **Max Probe Temp**

    * Max Temperature threshold used for the *Alarm Outside Temp Range* toggle.

    **Min Probe Temp**

    * Min Temperature threshold used for the *Alarm Outside Temp Range* toggle.

    **Notify Only Outside Temp Difference**

    * Notify on Outside temperature difference ONLY.
    * Click on the toggle to turn on or off. Defaults to OFF.

    **Prevent Sleep**

    * Prevents the TEMP-1B from going to sleep. When sleeping, your TEMP-1B will NOT respond to home assistant it is effectively off until it wakes up again.
    * Click on the toggle to turn on or off. Defaults to ON.

    **Probe Temp Difference Threshold**

    * Max temperature range threshold used for the *Alarm Outside Temp Range* toggle. Measured in Celsius.

    **Sleep Duration**

    * The number of hours the device should remain in sleep mode before waking up. Defaults to 12 hours.

???+ info "Diagnostic"

    **ESP Temperature**

    * Displays the current temperature of the ESP32 chip.

    **Online**

    * Shows the connection status.

    **RSSI**

    * Displays the Wi-Fi signal strength.

    **Uptime**

    * Shows the time since last reboot.

[Join our Discord if you need more help! :simple-discord:](https://dsc.gg/apolloautomation){            .md-button }