# Automation Examples using a TEMP-1

###### Freezer Temperature Probe Example

This will guide you through how to setup an automation in Home Assistant using the temperature probe in your freezer!

1\. Place the temperature probe into your freezer (not the entire TEMP-1, just the probe!) and then wait for it to normalize around 0°F (-18°C).

2\. Once normalized, look at the graph and determine a good value to set for both the maximum and minimum temperatures. My mini freezer seems to max out at 30°F so I would want to go slightly above that range. However, <a href="https://www.energy.gov/energysaver/refrigerator-freezer-use-and-temperature-tips" target="_blank" rel="noreferrer nofollow noopener">in most freezers, they should NOT reach above 0</a>°<a href="https://www.energy.gov/energysaver/refrigerator-freezer-use-and-temperature-tips" target="_blank" rel="noreferrer nofollow noopener">F</a> so you will likely need to input a lower value than me. my minimums are around -20°F.

![](assets/temp-1-temp-probe-ex-automation-pic-1.png)

3\. We now need to convert F to C since the max and min temps are measured in Celsius. My new values I will input are max probe temp 2°C and a min probe temp of -30°C. Reminder, yours will likely be different values, especially your max probe temp.

![](assets/temp-1-temp-probe-ex-automation-pic-2.png)

4\. The automation is now ready to be created -

5\. Click Settings -&gt; Automations & scenes -&gt; click Create Automation in the bottom left then "create new automation". <a href="http://homeassistant.local:8123/config/automation/edit/new" target="_blank" rel="noreferrer nofollow noopener">Click here to go straight there!</a>

[Click here to go straight there!](http://homeassistant.local:8123/config/automation/edit/new){                   .md-button .md-button--primary }

6\. Click Add Trigger then Entity then Numeric state and search for your temp-1 device such as "temp-1 max probe temp" then in the box labeled "Above" type in the max probe temp number you found in step 2 above. Advanced users click here for the YAML.

![](assets/temp-1-temp-probe-ex-automation-pic-3.png)

7\. Click Add Action then type in "iPhone" and select your phone. if you do not see your phone or have an Android, try typing in "notify" instead and scrolling down until you find your phone listed.

![](assets/temp-1-temp-probe-ex-automation-pic-4.png)

!!! tip "If you still do not see your device as shown in step 7 read this!"

    You need the Home Assistant mobile app installed on your phone for this step to work! If you do not have it, try another notification instead of using your phone such as a TTS notification on your speakers. This could be a fun way to announce that dinner is ready!

8\. Type in your preferred message and if you want, check the box for title and type in your title for the message as well. Mine says: "The temperature probe on your TEMP-1 reached its max temperature and your freezer might be having issues." and "Check the freezer!".

![](assets/temp-1-temp-probe-ex-automation-pic-5.png)

9\. Click save in the bottom right and then give it a Name and optionally a Description and a Category as well.

![](assets/temp-1-temp-probe-ex-automation-pic-6.png)

??? tip "Advanced users click here for the YAML"

    ```yaml
    alias: Freezer Over Max Temp Automation
    description: Warning for the freezer when it reaches the max temperature.
    triggers:
      - trigger: numeric_state
        entity_id:
          - number.apollo_temp_1_max_probe_temp
        above: 30
    conditions: []
    actions:
      - action: notify.mobile_app_brandons_iphone
        metadata: {}
        data:
          title: Check the freezer!
          message: >-
            The temperature probe on your TEMP-1 reached its max temperature and
            your freezer might be having issues.
    mode: single
    ```

```yaml
alias: Freezer Over Max Temp Automation
description: Warning for the freezer when it reaches the max temperature.
triggers:
  - trigger: numeric_state
    entity_id:
      - number.apollo_temp_1_max_probe_temp
    above: 30
conditions: []
actions:
  - action: notify.mobile_app_brandons_iphone
    metadata: {}
    data:
      title: Check the freezer!
      message: >-
        The temperature probe on your TEMP-1 reached its max temperature and
        your freezer might be having issues.
mode: single
```

###### Food Probe Example

This will guide you through setting up the food probe to alert you when your desired food temperature is met.

1\. Click Settings -&gt; Automations & scenes -&gt; click Create Automation in the bottom left. <a href="http://homeassistant.local:8123/config/automation/edit/new" target="_blank" rel="noreferrer nofollow noopener">Click here to go straight there!</a>