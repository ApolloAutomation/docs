---
title: Automation Examples using a TEMP-1B
description: "Multiple automation examples with the TEMP-1B."
---
# Automation Examples using a TEMP-1B

## Freezer Temperature Probe Example

This will guide you through how to set up an automation in Home Assistant using the temperature probe in your freezer! At the end, you will have an automation that sends your phone a notification when your temp is exceeded.

1\. Place the temperature probe into your freezer and then wait for it to normalize around 0°F (-18°C). Make sure your TEMP-1B is in a cool dry place - only the temp probe and wire can withstand the temperatures in the fridge, freezer, etc.

2\. Once normalized, look at the graph and determine a good value to set for both the maximum and minimum temperatures. My mini freezer seems to max out at 30°F so I would want to go slightly above that range. However, <a href="https://www.fda.gov/food/buy-store-serve-safe-food/refrigerator-thermometers-cold-facts-about-food-safety" target="_blank" rel="noreferrer nofollow noopener">in most freezers, they should NOT reach above 0</a>°<a href="https://www.fda.gov/food/buy-store-serve-safe-food/refrigerator-thermometers-cold-facts-about-food-safety" target="_blank" rel="noreferrer nofollow noopener">F</a> so you will likely need to input a lower value than me. My minimums are around -20°F.

![Home Assistant history graph of the temperature probe in a freezer, with arrows at a high and a low point](/assets/temp-1-temp-probe-ex-automation-pic-1.png)

*Shown on a TEMP-1; the TEMP-1B graph looks the same.*

3\. We now need to convert F to C since the max and min temps are measured in Celsius. My new values I will input are max probe temp 2°C and a min probe temp of -30°C. Reminder, yours will likely be different values, especially your max probe temp.

![Max Probe Temp set to 2.0 and Min Probe Temp set to -30.0 degrees Celsius in Home Assistant](/assets/temp-1-temp-probe-ex-automation-pic-2.png)

4\. The automation is now ready to be created -

5\. Click Settings -&gt; Automations & scenes -&gt; click Create Automation in the bottom left then "create new automation". <a href="http://homeassistant.local:8123/config/automation/edit/new" target="_blank" rel="noreferrer nofollow noopener">Click here to go straight there!</a>

6\. Click Add Trigger then Entity then Numeric state and search for your TEMP-1B device such as "temp-1b temperature probe" then in the box labeled "Above" type in the maximum temperature you picked in step 2 above. Enter the value in the unit your Home Assistant shows (°F in this example). Advanced users skip to step 10.

![Home Assistant numeric state trigger for Apollo TEMP-1 Max Probe Temp with the Above field set to 30 highlighted](/assets/temp-1-temp-probe-ex-automation-pic-3.png)

*Shown on a TEMP-1; pick your TEMP-1B entity instead.*

7\. Click Add Action then type in "iPhone" and select your phone. If you do not see your phone or have an Android, try typing in "notify" instead and scrolling down until you find your phone listed.

![Home Assistant Add action dialog searching iphone, with the mobile app notification action highlighted](/assets/temp-1-temp-probe-ex-automation-pic-4.png)

!!! tip "If you still do not see your device as shown in step 7 read this!"

    You need the Home Assistant mobile app installed on your phone for this step to work! If you do not have it, try another notification instead of using your phone such as a TTS notification on your speakers. This could be a fun way to announce that dinner is ready!

8\. Type in your preferred message and if you want, check the box for title and type in your title for the message as well. Mine says: "The temperature probe on your TEMP-1B reached its max temperature and your freezer might be having issues." and "Check the freezer!".

![Home Assistant notification action with the message and the Check the freezer title fields highlighted](/assets/temp-1-temp-probe-ex-automation-pic-5.png)

*Shown on a TEMP-1; the TEMP-1B steps are the same.*

9\. Click save in the bottom right and then give it a Name and optionally a Description and a Category as well. You are done!

![Home Assistant Save dialog with name, description, and category filled in and the Save button highlighted](/assets/temp-1-temp-probe-ex-automation-pic-6.png)

*Shown on a TEMP-1; the TEMP-1B steps are the same.*

---

10\. YAML for Advanced Users

```yaml
alias: Freezer Over Max Temp Automation
description: Warning for the freezer when it reaches the max temperature.
triggers:
  - trigger: numeric_state
    entity_id:
      - sensor.apollo_temp_1b_temperature_probe
    above: 30
conditions: []
actions:
  - action: notify.mobile_app_brandons_iphone
    metadata: {}
    data:
      title: Check the freezer!
      message: >-
        The temperature probe on your TEMP-1B reached its max temperature and
        your freezer might be having issues.
mode: single
```

## Food Probe Example

This will guide you through how to set up an automation in Home Assistant using the food probe with Chicken(or anything) cooking to 165°F(73.9C). At the end, you will have an automation that sends your phone a notification when your temp is exceeded.

1\. Set your Max Probe Temp to 73.9°C. Max Probe Temp must be entered in Celsius, even if you use °F in the automation below.

![Home Assistant Max Probe Temp field set to 73.9 degrees Celsius, highlighted](/assets/temp-1-food-probe-ex-automation-pic-1.png)

2\. Place the food probe inside your food once it's on the grill. Make sure your TEMP-1B is in a cool dry place. Only the [food probe and its wire can withstand the heat of a grill, oven, and so on](../addons/food-probe.md).

3\. Click Settings -&gt; Automations & scenes -&gt; click Create Automation in the bottom left. <a href="http://homeassistant.local:8123/config/automation/edit/new" target="_blank" rel="noreferrer nofollow noopener">Click here to go straight there!</a>

4\. Click Add Trigger then Entity then Numeric state and search for your TEMP-1B device such as "temp-1b food probe" then in the box labeled "Above" type in the temperature you want for your food - In this example we will use 165°F(73.9C) such as the temperature it's safe to cook Chicken to. Enter the value in the unit your Home Assistant shows (°F in this example). Advanced users skip to step 8.

![Home Assistant numeric state trigger for Apollo TEMP-1 Max Probe Temp with Above set to 165](/assets/temp-1-food-probe-ex-automation-pic-3.png)

*Shown on a TEMP-1; pick your TEMP-1B entity instead.*

5\. Click Add Action then type in "iPhone" and select your phone. If you do not see your phone or have an Android, try typing in "notify" instead and scrolling down until you find your phone listed.

![Home Assistant Add action dialog searching iphone, with the mobile app notification action highlighted](/assets/temp-1-temp-probe-ex-automation-pic-4.png)

!!! tip "If you still do not see your device as shown in step 5, read this!"

    You need the Home Assistant mobile app installed on your phone for this step to work! If you do not have it, try another notification instead of using your phone such as a TTS notification on your speakers. This could be a fun way to announce that dinner is ready!

6\. Type in your preferred message and if you want, check the box for title and type in your title for the message as well. Mine says: "The temperature probe on your TEMP-1B reached its max temperature and your food is ready." and "Check the food!".

![Home Assistant notification action with the message and the Check the food title fields highlighted](/assets/temp-1-food-probe-ex-automation-pic-5.png)

*Shown on a TEMP-1; the TEMP-1B steps are the same.*

7\. Click save in the bottom right and then give it a Name and optionally a Description and a Category as well. You are done!

![Home Assistant Save dialog for the Food over Max Temp Automation with the Save button highlighted](/assets/temp-1-food-probe-ex-automation-pic-6.png)

---

8\. YAML for Advanced Users

```yaml
alias: Food Over Max Temp Automation
description: Warning for the food when it reaches the max temperature.
triggers:
  - trigger: numeric_state
    entity_id:
      - sensor.apollo_temp_1b_food_probe
    above: 165
conditions: []
actions:
  - action: notify.mobile_app_brandons_iphone
    metadata: {}
    data:
      title: Check the food!
      message: >-
        The temperature probe on your TEMP-1B reached its max temperature and your food is ready.
mode: single
```

## Cook Chicken Example

This will guide you through adding a button to your dashboard called "Chicken Monitor" and an automation that runs when the button is pressed! This will turn the RGB LED Green when running, message your phone when it starts and when it finishes, plus when the temperature is reached, then turn the RGB LED off. Thanks to Discord user RalphP for this!

1\. Create a new toggle helper called "Chicken Monitor". Please <a href="https://wiki.apolloautomation.com/products/general/battery-sensors/awake-ha-helper/" target="_blank" rel="noreferrer nofollow noopener">click here</a> for step by step directions on creating a toggle helper.

![Home Assistant Create Toggle dialog named Chicken Monitor with a drumstick icon and the Create button highlighted](/assets/temp-1-cook-chicken-example-pic-1.png)

2\. Edit your dashboard, add a button card, select Chicken Monitor, and then save.

![Home Assistant Add to dashboard dialog searching button, showing the Button card](/assets/temp-1-cook-chicken-example-pic-3.png)![Home Assistant Button card configuration with the Chicken Monitor entity and the Save button highlighted](/assets/temp-1-cook-chicken-example-pic-2.png)

3\. Click Settings -&gt; Automations & scenes -&gt; click Create Automation in the bottom left then "create new automation". <a href="http://homeassistant.local:8123/config/automation/edit/new" target="_blank" rel="noreferrer nofollow noopener">Click here to go straight there!</a>

4\. Click Add Trigger then Entity then State and search for "Chicken Monitor" then in the box labeled "To" select "On".

![Home Assistant state trigger that fires when Chicken Monitor changes to On](/assets/temp-1-cook-chicken-example-pic-4.png)

5\. Create a Trigger ID for this called "Chicken Monitor On".

![Trigger options menu in the Home Assistant automation editor with Edit ID selected](/assets/temp-1-cook-chicken-example-pic-5.png)![Home Assistant state trigger with the Trigger ID set to Chicken Monitor On](/assets/temp-1-cook-chicken-example-pic-6-1.png)

6\. Click Add Trigger then Entity then State and search for "Chicken Monitor" then in the box labeled "To" select "Off". Create a Trigger ID for this called "Chicken Monitor Off".

![Home Assistant state trigger for Chicken Monitor changing to Off with the Trigger ID Chicken Monitor Off](/assets/temp-1-cook-chicken-example-pic-21.png)

7\. Click Add Trigger then Entity then Numeric state and search for your TEMP-1B food probe entity such as "temp-1b food probe" then in the box labeled "Above" type in the temperature you want for your food - In this example we will use 160°F(71.1C) because the Chicken will rest and reach 165°F once removed from the oven/grill.

![Home Assistant numeric state trigger for Apollo TEMP-1 Food Probe with Above set to 160](/assets/temp-1-cook-chicken-example-pic-7.png)

*Shown on a TEMP-1; pick your TEMP-1B food probe instead.*

8\. Create a Trigger ID for this called "Temp Reached".

![Home Assistant food probe trigger with the Trigger ID set to Temp Reached highlighted](/assets/temp-1-cook-chicken-example-pic-8.png)

*Shown on a TEMP-1; the TEMP-1B steps are the same.*

9\. Click Add Action and search "choose" then select it.

![Home Assistant Add action dialog searching choose, with the Choose action shown](/assets/temp-1-cook-chicken-example-pic-12.png)

10\. Under option 1 select "Add Condition" then search "trigger id" and select Triggered by.

![Home Assistant Add condition dialog searching trigger id, with Triggered by shown](/assets/temp-1-cook-chicken-example-pic-13.png)

11\. Check off the option "Chicken Monitor On" that we created in step 5 above.

![Option 1 condition in the Home Assistant choose action with the Button Pressed trigger checked](/assets/temp-1-cook-chicken-example-pic-14.png)

12\. While still under Option 1 in the choose action: Click Add Action and search "light" then select Light: Turn on.

![Home Assistant Add action dialog searching light, with Light: Turn on highlighted](/assets/temp-1-cook-chicken-example-pic-9.png)

13\. Click choose entity then search for your device such as "TEMP-1B RGB Light".

![Home Assistant entity picker listing Apollo TEMP-1 and TEMP-1B RGB Light entities](/assets/temp-1-cook-chicken-example-pic-10.png)

*Shown on a TEMP-1; pick your TEMP-1B RGB Light instead.*

14\. Click "Advanced Options" and then click the check box for Color name then select a color from the dropdown such as Green.

![Home Assistant Advanced options with Color name checked and Green chosen in the color dropdown](/assets/temp-1-cook-chicken-example-pic-11.png)

15\. While still under Option 1 in the choose action: Click Add Action and search "mobile" and then select your phone in the list.

![Home Assistant Add action dialog searching mobile, with the iPhone notification action highlighted](/assets/temp-1-cook-chicken-example-pic-15.png)

16\. Write in a custom title and or message- the message is required but the title is not.

![Home Assistant notification action with the Chicken Monitoring Started title and message filled in](/assets/temp-1-cook-chicken-example-pic-16.png)

*Shown on a TEMP-1; the TEMP-1B steps are the same.*

17\. This is how option 1 will look when you are done with this part:

![Finished Option 1 in the Home Assistant choose action with the RGB light turn on and notification actions](/assets/temp-1-cook-chicken-example-pic-17-1.png)

*Shown on a TEMP-1; the TEMP-1B steps are the same.*

18\. Click "Add Option" at the bottom then under option 2 select "Add Condition" then search "trigger id" and select Triggered by.

![Home Assistant Add condition dialog searching trigger id, with Triggered by shown](/assets/temp-1-cook-chicken-example-pic-13.png)

19\. Check off the option "Temp Reached" that we created in step 8 above.

![Option 2 condition in Home Assistant with the Temp Reached trigger checked](/assets/temp-1-cook-chicken-example-pic-18-1.png)

20\. While still under Option 2 in the choose action: Click Add Action and search "repeat" then select "Until" in the dropdown.

![Home Assistant Add action dialog searching repeat, with the Repeat action shown](/assets/temp-1-cook-chicken-example-pic-22.png)

21\. Under Until Conditions, select "Add condition" then search "state".

![Home Assistant Add condition dialog searching state, with the State condition shown](/assets/temp-1-cook-chicken-example-pic-25.png)

22\. Type in Chicken Monitor and select it, then click "Off" in the dropdown for the state of the sensor.

![Home Assistant repeat until condition with the Chicken Monitor entity and Off state highlighted](/assets/temp-1-cook-chicken-example-pic-26.png)

23\. Click "Add Action" under the "until" condition we created above. Be very careful to select the correct "Add Action" button as shown below.

![Add Action button inside the repeat until block in Home Assistant, highlighted](/assets/temp-1-cook-chicken-example-pic-27.png)

24\. Search "light toggle" in the search bar shown then select "Choose entity" and select the rgb led for your device

![Home Assistant Add action dialog searching light toggle, with Light: Toggle shown](/assets/temp-1-cook-chicken-example-pic-28.png)

25\. Head down to Add Action under Option 2 and search "mobile" then select your phone as you did above in step 15. Give it a message and a title as shown below.

![Home Assistant notification action titled Time to check the Chicken, below the repeat action](/assets/temp-1-cook-chicken-example-pic-29.png)

26\. Optionally add another action here for speaking out loud on your smart speakers such as Homepods. Click add Action then search "TTS". This requires you to have piper and a few other things already set up.

![Home Assistant Add action dialog searching tts, with the Text-to-speech (TTS): Speak action selected](/assets/temp-1-cook-chicken-example-pic-30.png)![Home Assistant TTS Speak action on piper targeting Homepods with the message The Chicken is almost ready](/assets/temp-1-cook-chicken-example-pic-31.png)

27\. Click "Add Option" (this is now Option 3). We will choose add condition then search "triggered by" and then choose the "Chicken Monitor Off" Trigger ID that we created in step 6.

28\. While still under Option 3 in the choose action: Click Add Action and search "light" then select Light: Turn off.

![Home Assistant Add action dialog searching light.turn, with Light: Turn off selected](/assets/temp-1-cook-chicken-example-pic-19.png)

29\. Click choose entity then search for your device such as "TEMP-1B RGB Light".

![Home Assistant Light Turn off action targeting the Apollo TEMP-1 RGB Light](/assets/temp-1-cook-chicken-example-pic-20.png)

*Shown on a TEMP-1; pick your TEMP-1B RGB Light instead.*

30\. Choose "Add Action" and search mobile like we did above and select your mobile phone. Give it an optional title and message as shown below.

![Home Assistant notification action titled Chicken Monitoring Stopped with its message filled in](/assets/temp-1-cook-chicken-example-pic-33.png)

31\. Click save in the bottom right then give it a name and save

![Home Assistant Save dialog for the TEMP-1 Chicken Automation with the Save button](/assets/temp-1-cook-chicken-example-pic-34.png)

*Shown on a TEMP-1; the TEMP-1B steps are the same.*

32\. You now have one automation which unifies the button you created in the dashboard and alerts you when your chicken is almost done via a phone notification, a blinking green led, and an optional TTS notification to your smart speakers! Thanks again to Discord user RalphP for this example!