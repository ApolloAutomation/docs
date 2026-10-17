---
title: Automation examples using a TEMP-1
description: Three Home Assistant automations for the TEMP-1, from a freezer alert to a chicken monitor that blinks the RGB LED and messages your phone when your food is almost done.
---
# Automation examples using a TEMP-1

<span class="difficulty lvl-2">Difficulty: Level 2</span>

<p class="automation-steps-heading">🌱 New here? Try these first:</p>
<div class="automation-steps">
  <div class="step">
    <a class="step-title" href="../temp1-alert-example/">TEMP-1 alert outside temp range example</a>
    <span class="difficulty lvl-1">Difficulty: Level 1</span>
  </div>
</div>

!!! note "Written for the TEMP-1"

    This page was written for the Apollo TEMP-1. Every step, screenshot, and YAML example uses a TEMP-1 and its entity names. Before you follow along with a TEMP Pro-1, check the [TEMP Pro-1 sensor definitions](../../setup/temp-pro-1-sensor-definitions/) to see which of these sensors and settings your TEMP Pro-1 has.

Your TEMP-1's probes can drive Home Assistant automations. This page walks you through three of them: a freezer alert, a food probe alert, and a chicken monitor you start and stop from your dashboard.

## Freezer temperature probe example

Set up a Home Assistant automation that uses the temperature probe in your freezer. At the end, you'll have an automation that sends your phone a notification when the probe goes above your maximum temperature.

1\. Place the temperature probe into your freezer, then wait for its reading to settle around 0°F (-18°C).

!!! danger "Only the probe goes in the freezer"

    Keep your TEMP-1 itself in a cool, dry place. Only the temp probe and its wire can withstand the temperatures in a fridge, freezer, and similar places.

2\. Once the reading settles, look at the graph and pick a good value for both the maximum and the minimum temperature. In this example, the mini freezer seems to max out at 30°F, so the maximum goes slightly above that. However, <a href="https://www.fda.gov/food/buy-store-serve-safe-food/refrigerator-thermometers-cold-facts-about-food-safety" target="_blank" rel="noreferrer nofollow noopener">most freezers should not reach above 0°F</a>, so you'll likely need a lower maximum than this one. The minimums here are around -20°F.

![Home Assistant history graph of the TEMP-1 temperature probe, arrows at freezer highs and lows](/assets/temp-1-temp-probe-ex-automation-pic-1.png)

3\. Convert your maximum and minimum from °F to °C, then enter them in **Max Probe Temp** and **Min Probe Temp**. Both settings are measured in Celsius. This example uses a max probe temp of 2°C and a min probe temp of -30°C. Your values will likely be different, especially your max probe temp.

![TEMP-1 Max Probe Temp set to 2.0 °C and Min Probe Temp set to -30.0 °C](/assets/temp-1-temp-probe-ex-automation-pic-2.png)

With your thresholds set, the automation is now ready to be created.

4\. Go to **Settings → Automations & scenes**, click **+ Create automation** in the bottom right, then **Create new automation**. Shortcut: <a href="http://homeassistant.local:8123/config/automation/edit/new" target="_blank" rel="noreferrer nofollow noopener">go straight to a new automation</a> (works if you reach Home Assistant at homeassistant.local).

5\. Click **Add Trigger**, then **Entity**, then **Numeric state**, and search for your TEMP-1 probe sensor, such as "temp-1 temperature probe". In the box labeled **Above**, type the maximum temperature you picked in step 2. Advanced users can skip to the YAML at the end of this section.

![Home Assistant numeric state trigger on Apollo TEMP-1 Max Probe Temp with Above set to 30](/assets/temp-1-temp-probe-ex-automation-pic-3.png)

6\. Click **Add Action**, type "iPhone", and select your phone. If you don't see your phone, or you have an Android phone, type "notify" instead and scroll down until you find your phone in the list.

![Home Assistant Add action search for iphone with the phone notification action highlighted](/assets/temp-1-temp-probe-ex-automation-pic-4.png)

!!! tip "Still don't see your phone?"

    You need the Home Assistant mobile app installed on your phone for this step to work. If you don't have it, use another kind of notification instead, such as a TTS notification on your speakers. This could be a fun way to announce that dinner is ready!

7\. Type in your message. If you want a title too, check the box for title and type it in. This example uses the message "The temperature probe on your TEMP-1 reached its max temperature and your freezer might be having issues." and the title "Check the freezer!".

![Notification action with the freezer warning message and Check the freezer! title](/assets/temp-1-temp-probe-ex-automation-pic-5.png)

8\. Click **Save** in the bottom right, then give the automation a name and, optionally, a description and a category.

![Save dialog for the Freezer Over Max Temp Automation with name, description, and category](/assets/temp-1-temp-probe-ex-automation-pic-6.png)

You're done! Your phone now gets a notification whenever the freezer probe goes above your maximum.

---

**YAML for advanced users**

```yaml
alias: Freezer Over Max Temp Automation
description: Warning for the freezer when it reaches the max temperature.
triggers:
  - trigger: numeric_state
    entity_id:
      - sensor.apollo_temp_1_temperature_probe
    # in the unit Home Assistant shows for the probe (°F here); use your own entity ID
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

## Food probe example

Set up a Home Assistant automation that uses the food probe while you cook chicken (or anything else) to 165°F (73.9°C). At the end, you'll have an automation that sends your phone a notification when your food reaches that temperature.

1\. Set your **Max Probe Temp** to 73.9°C. Max Probe Temp is always set in Celsius, even if you use °F in the automation below.

![TEMP-1 Max Probe Temp set to 73.9 °C, highlighted in red](/assets/temp-1-food-probe-ex-automation-pic-1.png)

2\. Once your food is on the grill, place the food probe inside it.

!!! danger "Only the food probe goes on the grill"

    Keep your TEMP-1 itself in a cool, dry place. Only the <a href="https://wiki.apolloautomation.com/products/temp1/addons/food-probe/" title="Click me for more info on installation of food probe and usage." target="_blank" rel="noreferrer nofollow noopener">food probe and its wire</a> can withstand temperatures on a grill, in the oven, and similar places.

3\. Go to **Settings → Automations & scenes**, click **+ Create automation** in the bottom right, then **Create new automation**. Shortcut: <a href="http://homeassistant.local:8123/config/automation/edit/new" target="_blank" rel="noreferrer nofollow noopener">go straight to a new automation</a> (works if you reach Home Assistant at homeassistant.local).

4\. Click **Add Trigger**, then **Entity**, then **Numeric state**, and search for your TEMP-1 food probe sensor, such as "temp-1 food probe". In the box labeled **Above**, type the temperature you want for your food. This example uses 165°F (73.9°C), the temperature it's safe to cook chicken to. Advanced users can skip to the YAML at the end of this section.

![Numeric state trigger on Apollo TEMP-1 Max Probe Temp with Above set to 165](/assets/temp-1-food-probe-ex-automation-pic-3.png)

5\. Click **Add Action**, type "iPhone", and select your phone. If you don't see your phone, or you have an Android phone, type "notify" instead and scroll down until you find your phone in the list.

![Home Assistant Add action search for iphone with the phone notification action highlighted](/assets/temp-1-temp-probe-ex-automation-pic-4.png)

!!! tip "Still don't see your phone?"

    You need the Home Assistant mobile app installed on your phone for this step to work. If you don't have it, use another kind of notification instead, such as a TTS notification on your speakers. This could be a fun way to announce that dinner is ready!

6\. Type in your message. If you want a title too, check the box for title and type it in. This example uses the message "The temperature probe on your TEMP-1 reached its max temperature and your food is ready." and the title "Check the food!".

![Notification action with the food ready message and Check the food! title](/assets/temp-1-food-probe-ex-automation-pic-5.png)

7\. Click **Save** in the bottom right, then give the automation a name and, optionally, a description and a category.

![Save dialog for the Food over Max Temp Automation with the cursor on Save](/assets/temp-1-food-probe-ex-automation-pic-6.png)

You're done! Your phone now gets a notification when your food reaches its target temperature.

---

**YAML for advanced users**

```yaml
alias: Food Over Max Temp Automation
description: Warning for the food when it reaches the max temperature.
triggers:
  - trigger: numeric_state
    entity_id:
      - sensor.apollo_temp_1_food_probe
    # in the unit Home Assistant shows for the probe (°F here); use your own entity ID
    above: 165
conditions: []
actions:
  - action: notify.mobile_app_brandons_iphone
    metadata: {}
    data:
      title: Check the food!
      message: >-
        The temperature probe on your TEMP-1 reached its max temperature and your food is ready.
mode: single
```

## Cook chicken example

This example adds a button called "Chicken Monitor" to your dashboard, plus an automation that runs when you press it. While it runs, the RGB LED turns green. Your phone gets a message when monitoring starts, when the temperature is reached, and when monitoring finishes, and then the RGB LED turns off. Thanks to Discord user RalphP for this!

The automation has three triggers, each with its own trigger ID, and one **Choose** action with an option for each trigger ID:

* **Option 1 (Chicken Monitor On):** turns the RGB LED green and messages your phone.
* **Option 2 (Temp Reached):** toggles the RGB LED until Chicken Monitor is turned off, messages your phone, and optionally speaks on your smart speakers.
* **Option 3 (Chicken Monitor Off):** turns the RGB LED off and messages your phone.

First, create the button.

1\. Create a new toggle helper called "Chicken Monitor". For step-by-step directions, see <a href="https://wiki.apolloautomation.com/products/general/battery-sensors/awake-ha-helper/" target="_blank" rel="noreferrer nofollow noopener">creating a toggle helper</a>.

![Home Assistant Create Toggle dialog for a Chicken Monitor helper, Create highlighted](/assets/temp-1-cook-chicken-example-pic-1.png)

2\. Edit your dashboard, add a button card, select Chicken Monitor, and then save.

![Home Assistant Add to dashboard dialog searching for the Button card](/assets/temp-1-cook-chicken-example-pic-3.png)![Button card configuration with Chicken Monitor as the entity, Save highlighted](/assets/temp-1-cook-chicken-example-pic-2.png)

Next, create the automation and its three triggers.

3\. Go to **Settings → Automations & scenes**, click **+ Create automation** in the bottom right, then **Create new automation**. Shortcut: <a href="http://homeassistant.local:8123/config/automation/edit/new" target="_blank" rel="noreferrer nofollow noopener">go straight to a new automation</a> (works if you reach Home Assistant at homeassistant.local).

4\. Click **Add Trigger**, then **Entity**, then **State**, and search for "Chicken Monitor". In the box labeled **To**, select **On**.

![Home Assistant state trigger for Chicken Monitor changing to On](/assets/temp-1-cook-chicken-example-pic-4.png)

5\. Create a Trigger ID for this trigger called "Chicken Monitor On".

![Trigger menu open with Edit ID selected on the Chicken Monitor trigger](/assets/temp-1-cook-chicken-example-pic-5.png)![Chicken Monitor trigger with the Trigger ID set to Chicken Monitor On](/assets/temp-1-cook-chicken-example-pic-6-1.png)

6\. Click **Add Trigger**, then **Entity**, then **State**, and search for "Chicken Monitor". In the box labeled **To**, select **Off**. Create a Trigger ID for this trigger called "Chicken Monitor Off".

![Chicken Monitor state trigger set to Off with Trigger ID Chicken Monitor Off](/assets/temp-1-cook-chicken-example-pic-21.png)

7\. Click **Add Trigger**, then **Entity**, then **Numeric state**, and search for your TEMP-1 food probe entity, such as "temp-1 food probe". In the box labeled **Above**, type the temperature you want for your food. This example uses 160°F (71.1°C), because the chicken will rest and reach 165°F once removed from the oven or grill.

![Numeric state trigger on Apollo TEMP-1 Food Probe with Above set to 160](/assets/temp-1-cook-chicken-example-pic-7.png)

8\. Create a Trigger ID for this trigger called "Temp Reached".

![Apollo TEMP-1 Food Probe trigger with Trigger ID set to Temp Reached](/assets/temp-1-cook-chicken-example-pic-8.png)

Now add the **Choose** action. Option 1 runs when you turn Chicken Monitor on.

9\. Click **Add Action**, search "choose", and select it.

![Home Assistant Add action dialog searching choose, showing the Choose action](/assets/temp-1-cook-chicken-example-pic-12.png)

10\. Under **Option 1**, select **Add Condition**, search "trigger id", and select **Triggered by**.

![Add condition dialog searching trigger id, showing the Triggered by condition](/assets/temp-1-cook-chicken-example-pic-13.png)

11\. Check **Chicken Monitor On**, the trigger ID you created in step 5.

12\. While still under **Option 1** in the Choose action, click **Add Action**, search "light", and select **Light: Turn on**.

![Add action search for light with Light: Turn on highlighted](/assets/temp-1-cook-chicken-example-pic-9.png)

13\. Click **Choose entity** and search for your device, such as "TEMP-1 RGB Light".

![Choose entity search results listing the Apollo TEMP-1 RGB Light](/assets/temp-1-cook-chicken-example-pic-10.png)

14\. Click **Advanced Options**, check the box for **Color name**, and select a color from the dropdown, such as Green.

![Light advanced options with Color name checked and Green selected](/assets/temp-1-cook-chicken-example-pic-11.png)

15\. While still under **Option 1** in the Choose action, click **Add Action**, search "mobile", and select your phone in the list.

![Add action search for mobile with the iPhone notification action highlighted](/assets/temp-1-cook-chicken-example-pic-15.png)

16\. Write a custom title and message. The message is required, but the title is not.

![Notification action titled Chicken Monitoring Started with a TEMP-1 message](/assets/temp-1-cook-chicken-example-pic-16.png)

17\. Check your work. When you're done with this part, Option 1 looks like this:

![Finished Option 1: Chicken Monitor On condition, TEMP-1 RGB Light on, and phone notification](/assets/temp-1-cook-chicken-example-pic-17-1.png)

Option 2 runs when the food probe reaches your target temperature.

18\. Click **Add Option** at the bottom. Under **Option 2**, select **Add Condition**, search "trigger id", and select **Triggered by**.

![Add condition dialog searching trigger id for Option 2, showing Triggered by](/assets/temp-1-cook-chicken-example-pic-13.png)

19\. Check **Temp Reached**, the trigger ID you created in step 8.

![Triggered by condition with only Temp Reached checked](/assets/temp-1-cook-chicken-example-pic-18-1.png)

20\. While still under **Option 2** in the Choose action, click **Add Action**, search "repeat", and select **Until** in the dropdown.

![Add action dialog searching repeat, with the Repeat action selected](/assets/temp-1-cook-chicken-example-pic-22.png)

21\. Under **Until Conditions**, select **Add condition**, then search "state".

![Add condition dialog searching state, with the State condition selected](/assets/temp-1-cook-chicken-example-pic-25.png)

22\. Type in "Chicken Monitor" and select it, then select **Off** in the dropdown for the state of the sensor.

![Repeat until condition with Chicken Monitor entity and Off state highlighted](/assets/temp-1-cook-chicken-example-pic-26.png)

23\. Click the **Add Action** button under the until condition you created. Be very careful to select the correct **Add Action** button, as shown below.

![Repeat until block with its inner Add Action button highlighted](/assets/temp-1-cook-chicken-example-pic-27.png)

24\. Search "light toggle" in the search bar, then select **Choose entity** and select the RGB LED for your device.

![Add action dialog searching light toggle, with Light: Toggle selected](/assets/temp-1-cook-chicken-example-pic-28.png)

25\. Go down to **Add Action** under **Option 2**, search "mobile", and select your phone as you did in step 15. Give it a message and a title, as shown below.

![Option 2 notification titled Time to check the Chicken! with a 160F message](/assets/temp-1-cook-chicken-example-pic-29.png)

26\. Optionally, add another action here that speaks out loud on your smart speakers, such as HomePods. Click **Add Action**, then search "TTS". This requires you to have Piper and a few other things already set up.

![Add action dialog searching tts, with Text-to-speech (TTS): Speak selected](/assets/temp-1-cook-chicken-example-pic-30.png)![TTS Speak action on piper targeting Homepods with The Chicken is almost ready! message](/assets/temp-1-cook-chicken-example-pic-31.png)

Option 3 runs when you turn Chicken Monitor off.

27\. Click **Add Option** (this is now **Option 3**). Select **Add Condition**, search "triggered by", and then choose the "Chicken Monitor Off" trigger ID you created in step 6.

28\. While still under **Option 3** in the Choose action, click **Add Action**, search "light", and select **Light: Turn off**.

![Add action dialog searching light.turn, with Light: Turn off selected](/assets/temp-1-cook-chicken-example-pic-19.png)

29\. Click **Choose entity** and search for your device, such as "TEMP-1 RGB Light".

![Light Turn off action targeting the Apollo TEMP-1 RGB Light](/assets/temp-1-cook-chicken-example-pic-20.png)

30\. Click **Add Action**, search "mobile" as you did above, and select your phone. Give it a message and, optionally, a title, as shown below.

![Notification action titled Chicken Monitoring Stopped! with a no longer monitored message](/assets/temp-1-cook-chicken-example-pic-33.png)

31\. Click **Save** in the bottom right, then give the automation a name and save.

![Save dialog naming the TEMP-1 Chicken Automation in the Food category](/assets/temp-1-cook-chicken-example-pic-34.png)

You now have one automation that ties together the button you created on your dashboard and alerts you when your chicken is almost done, with a phone notification, a blinking green LED, and an optional TTS notification on your smart speakers. Thanks again to Discord user RalphP for this example!
