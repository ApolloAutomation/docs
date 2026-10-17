---
title: Automation examples using a TEMP-1B
description: Three Home Assistant automations for the TEMP-1B, from a freezer alert to a chicken monitor that blinks the RGB LED and messages your phone when your food is almost done.
---
# Automation examples using a TEMP-1B

<span class="difficulty lvl-2">Difficulty: Level 2</span>

<p class="automation-steps-heading">🌱 New here? Try these first:</p>
<div class="automation-steps">
  <div class="step">
    <a class="step-title" href="../temp1b-alert-example/">TEMP-1B Alert Outside Temp Range Example</a>
    <span class="difficulty lvl-1">Difficulty: Level 1</span>
  </div>
</div>

Your Apollo TEMP-1B's probes can drive Home Assistant automations. This page walks you through three of them: a freezer alert, a food probe alert, and a chicken monitor you start and stop from your dashboard.

## Freezer temperature probe example

Set up a Home Assistant automation that uses the temperature probe in your freezer. At the end, you'll have an automation that sends your phone a notification when the probe goes above your maximum temperature.

1\. Place the temperature probe into your freezer, then wait for its reading to settle around 0°F (-18°C).

!!! danger "Only the probe goes in the freezer"

    Keep your TEMP-1B itself in a cool, dry place. Only the temp probe and its wire can withstand the temperatures in a fridge, freezer, and similar places.

2\. Once the reading settles, look at the graph and pick a good value for both the maximum and the minimum temperature. In this example, the mini freezer seems to max out at 30°F, so the maximum goes slightly above that. However, <a href="https://www.fda.gov/food/buy-store-serve-safe-food/refrigerator-thermometers-cold-facts-about-food-safety" target="_blank" rel="noreferrer nofollow noopener">most freezers should not reach above 0°F</a>, so you'll likely need a lower maximum than this one. The minimums here are around -20°F.

![Home Assistant history graph of the TEMP-1 temperature probe with arrows at freezer highs and lows](/assets/temp-1-temp-probe-ex-automation-pic-1.png)

*Shown on a TEMP-1; the TEMP-1B graph looks the same.*

3\. Convert your maximum and minimum from °F to °C, then enter them in **Max Probe Temp** and **Min Probe Temp**. Both settings are measured in Celsius. This example uses a max probe temp of 2°C and a min probe temp of -30°C. Your values will likely be different, especially your max probe temp.

![Home Assistant settings with Max Probe Temp set to 2.0 °C and Min Probe Temp set to -30.0 °C](/assets/temp-1-temp-probe-ex-automation-pic-2.png)

With your thresholds set, the automation is now ready to be created.

4\. Go to **Settings → Automations & scenes**, click **+ Create automation** in the bottom right, then **Create new automation**.

[![Open your Home Assistant instance and show your automations.](https://my.home-assistant.io/badges/automations.svg)](https://my.home-assistant.io/redirect/automations/)

5\. Click **Add Trigger**, then **Entity**, then **Numeric state**, and search for your TEMP-1B temperature probe, such as "temp-1b temperature probe". In the box labeled **Above**, type the maximum temperature you picked in step 2. Enter the value in the unit your Home Assistant shows (°F in this example). Advanced users can skip to the YAML at the end of this section.

![Home Assistant numeric state trigger on TEMP-1 Max Probe Temp with the Above field set to 30 highlighted](/assets/temp-1-temp-probe-ex-automation-pic-3.png)

*Shown on a TEMP-1; pick your TEMP-1B entity instead.*

6\. Click **Add Action**, type "iPhone", and select your phone. If you don't see your phone, or you have an Android phone, type "notify" instead and scroll down until you find your phone in the list.

![Home Assistant Add action search for iphone with the mobile app notification action highlighted](/assets/temp-1-temp-probe-ex-automation-pic-4.png)

!!! tip "Still don't see your phone?"

    You need the Home Assistant mobile app installed on your phone for this step to work. If you don't have it, use another kind of notification instead, such as a TTS notification on your speakers. This could be a fun way to announce that dinner is ready!

7\. Type in your message. If you want a title too, check the box for title and type it in. This example uses the message "The temperature probe on your TEMP-1B reached its max temperature and your freezer might be having issues." and the title "Check the freezer!".

![Home Assistant notification action with the message and Check the freezer! title fields highlighted](/assets/temp-1-temp-probe-ex-automation-pic-5.png)

*Shown on a TEMP-1; the TEMP-1B steps are the same.*

8\. Click **Save** in the bottom right, then give the automation a name and, optionally, a description and a category.

![Home Assistant save dialog for Freezer Over Max Temp Automation with name, description, and category filled in](/assets/temp-1-temp-probe-ex-automation-pic-6.png)

*Shown on a TEMP-1; the TEMP-1B steps are the same.*

You're done! Your phone now gets a notification whenever the freezer probe goes above your maximum.

---

**YAML for advanced users**

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

## Food probe example

Set up a Home Assistant automation that uses the food probe while you cook chicken (or anything else) to 165°F (73.9°C). At the end, you'll have an automation that sends your phone a notification when your food reaches that temperature.

1\. Set your **Max Probe Temp** to 73.9°C. Max Probe Temp must be entered in Celsius, even if you use °F in the automation below.

![Home Assistant setting with Max Probe Temp set to 73.9 °C highlighted](/assets/temp-1-food-probe-ex-automation-pic-1.png)

2\. Once your food is on the grill, place the food probe inside it.

!!! danger "Only the food probe goes on the grill"

    Keep your TEMP-1B itself in a cool, dry place. Only the [food probe and its wire](../../addons/food-probe/) can withstand temperatures on a grill, in the oven, and similar places.

3\. Go to **Settings → Automations & scenes**, click **+ Create automation** in the bottom right, then **Create new automation**.

[![Open your Home Assistant instance and show your automations.](https://my.home-assistant.io/badges/automations.svg)](https://my.home-assistant.io/redirect/automations/)

4\. Click **Add Trigger**, then **Entity**, then **Numeric state**, and search for your TEMP-1B device, such as "temp-1b food probe". In the box labeled **Above**, type the temperature you want for your food. This example uses 165°F (73.9°C), the temperature it's safe to cook chicken to. Enter the value in the unit your Home Assistant shows (°F in this example). Advanced users can skip to the YAML at the end of this section.

![Home Assistant numeric state trigger with the TEMP-1 Max Probe Temp entity and Above 165 fields highlighted](/assets/temp-1-food-probe-ex-automation-pic-3.png)

*Shown on a TEMP-1; pick your TEMP-1B entity instead.*

5\. Click **Add Action**, type "iPhone", and select your phone. If you don't see your phone, or you have an Android phone, type "notify" instead and scroll down until you find your phone in the list.

![Home Assistant Add action search for iphone with the mobile app notification action highlighted](/assets/temp-1-temp-probe-ex-automation-pic-4.png)

!!! tip "Still don't see your phone?"

    You need the Home Assistant mobile app installed on your phone for this step to work. If you don't have it, use another kind of notification instead, such as a TTS notification on your speakers. This could be a fun way to announce that dinner is ready!

6\. Type in your message. If you want a title too, check the box for title and type it in. This example uses the message "The temperature probe on your TEMP-1B reached its max temperature and your food is ready." and the title "Check the food!".

![Home Assistant notification action with the message and Check the food! title fields highlighted](/assets/temp-1-food-probe-ex-automation-pic-5.png)

*Shown on a TEMP-1; the TEMP-1B steps are the same.*

7\. Click **Save** in the bottom right, then give the automation a name and, optionally, a description and a category.

![Home Assistant save dialog for Food over Max Temp Automation with name, description, category, and Save highlighted](/assets/temp-1-food-probe-ex-automation-pic-6.png)

You're done! Your phone now gets a notification when your food reaches its target temperature.

---

**YAML for advanced users**

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

## Cook chicken example

This example adds a button called "Chicken Monitor" to your dashboard, plus an automation that runs when you press it. While it runs, the RGB LED turns green. Your phone gets a message when monitoring starts, when the temperature is reached, and when monitoring finishes, and then the RGB LED turns off. Thanks to Discord user RalphP for this!

The automation has three triggers, each with its own trigger ID, and one **Choose** action with an option for each trigger ID:

* **Option 1 (Chicken Monitor On):** turns the RGB LED green and messages your phone.
* **Option 2 (Temp Reached):** toggles the RGB LED until Chicken Monitor is turned off, messages your phone, and optionally speaks on your smart speakers.
* **Option 3 (Chicken Monitor Off):** turns the RGB LED off and messages your phone.

First, create the button.

1\. Create a new toggle helper called "Chicken Monitor". For step-by-step directions, see <a href="https://wiki.apolloautomation.com/products/general/battery-sensors/awake-ha-helper/" target="_blank" rel="noreferrer nofollow noopener">creating a toggle helper</a>.

![Home Assistant Create Toggle dialog for a Chicken Monitor helper with the Create button highlighted](/assets/temp-1-cook-chicken-example-pic-1.png)

2\. Edit your dashboard, add a button card, select Chicken Monitor, and then save.

![Home Assistant Add to dashboard dialog with button typed in the card search](/assets/temp-1-cook-chicken-example-pic-3.png)![Home Assistant Button card configuration with the Chicken Monitor entity and Save button highlighted](/assets/temp-1-cook-chicken-example-pic-2.png)

Next, create the automation and its three triggers.

3\. Go to **Settings → Automations & scenes**, click **+ Create automation** in the bottom right, then **Create new automation**.

[![Open your Home Assistant instance and show your automations.](https://my.home-assistant.io/badges/automations.svg)](https://my.home-assistant.io/redirect/automations/)

4\. Click **Add Trigger**, then **Entity**, then **State**, and search for "Chicken Monitor". In the box labeled **To**, select **On**.

![Home Assistant state trigger for Chicken Monitor with the To field set to On](/assets/temp-1-cook-chicken-example-pic-4.png)

5\. Create a Trigger ID for this trigger called "Chicken Monitor On".

![Home Assistant trigger options menu open with Edit ID selected](/assets/temp-1-cook-chicken-example-pic-5.png)![Home Assistant Chicken Monitor trigger with Trigger ID set to Chicken Monitor On](/assets/temp-1-cook-chicken-example-pic-6-1.png)

6\. Click **Add Trigger**, then **Entity**, then **State**, and search for "Chicken Monitor". In the box labeled **To**, select **Off**. Create a Trigger ID for this trigger called "Chicken Monitor Off".

![Home Assistant state trigger for Chicken Monitor set to Off with Trigger ID Chicken Monitor Off highlighted](/assets/temp-1-cook-chicken-example-pic-21.png)

7\. Click **Add Trigger**, then **Entity**, then **Numeric state**, and search for your TEMP-1B food probe entity, such as "temp-1b food probe". In the box labeled **Above**, type the temperature you want for your food. This example uses 160°F (71.1°C), because the chicken will rest and reach 165°F once removed from the oven or grill.

![Home Assistant numeric state trigger on TEMP-1 Food Probe with the Above field set to 160](/assets/temp-1-cook-chicken-example-pic-7.png)

*Shown on a TEMP-1; pick your TEMP-1B food probe instead.*

8\. Create a Trigger ID for this trigger called "Temp Reached".

![Home Assistant TEMP-1 Food Probe trigger with Trigger ID set to Temp Reached highlighted](/assets/temp-1-cook-chicken-example-pic-8.png)

*Shown on a TEMP-1; the TEMP-1B steps are the same.*

Now add the **Choose** action. Option 1 runs when you turn Chicken Monitor on.

9\. Click **Add Action**, search "choose", and select it.

![Home Assistant Add action dialog with choose searched and the Choose action listed](/assets/temp-1-cook-chicken-example-pic-12.png)

10\. Under **Option 1**, select **Add Condition**, search "trigger id", and select **Triggered by**.

![Home Assistant Add condition dialog with trigger id searched and Triggered by listed](/assets/temp-1-cook-chicken-example-pic-13.png)

11\. Check **Chicken Monitor On**, the trigger ID you created in step 5.

![Home Assistant Choose action Option 1 with the Button Pressed trigger checked and highlighted](/assets/temp-1-cook-chicken-example-pic-14.png)

*The screenshot shows a trigger ID called Button Pressed. In your automation, check Chicken Monitor On.*

12\. While still under **Option 1** in the Choose action, click **Add Action**, search "light", and select **Light: Turn on**.

![Home Assistant Add action dialog with light searched and Light: Turn on highlighted](/assets/temp-1-cook-chicken-example-pic-9.png)

13\. Click **Choose entity** and search for your device, such as "TEMP-1B RGB Light".

![Home Assistant Choose entity search for TEMP-1 with the cursor on the Apollo TEMP-1 RGB Light entity](/assets/temp-1-cook-chicken-example-pic-10.png)

*Shown on a TEMP-1; pick your TEMP-1B RGB Light instead.*

14\. Click **Advanced Options**, check the box for **Color name**, and select a color from the dropdown, such as Green.

![Home Assistant light action Advanced options with Color name checked and Green picked from the list](/assets/temp-1-cook-chicken-example-pic-11.png)

15\. While still under **Option 1** in the Choose action, click **Add Action**, search "mobile", and select your phone in the list.

![Home Assistant Add action dialog with mobile searched and the iPhone notification action highlighted](/assets/temp-1-cook-chicken-example-pic-15.png)

16\. Write a custom title and message. The message is required, but the title is not.

![Home Assistant notification action with the title Chicken Monitoring Started and a custom message](/assets/temp-1-cook-chicken-example-pic-16.png)

*Shown on a TEMP-1; the TEMP-1B steps are the same.*

17\. Check your work. When you're done with this part, Option 1 looks like this:

![Home Assistant Option 1 triggered by Chicken Monitor On with light turn on and notification actions](/assets/temp-1-cook-chicken-example-pic-17-1.png)

*Shown on a TEMP-1; the TEMP-1B steps are the same.*

Option 2 runs when the food probe reaches your target temperature.

18\. Click **Add Option** at the bottom. Under **Option 2**, select **Add Condition**, search "trigger id", and select **Triggered by**.

![Home Assistant Add condition dialog with trigger id searched and Triggered by listed](/assets/temp-1-cook-chicken-example-pic-13.png)

19\. Check **Temp Reached**, the trigger ID you created in step 8.

![Home Assistant Option 2 Triggered by condition with only Temp Reached checked](/assets/temp-1-cook-chicken-example-pic-18-1.png)

20\. While still under **Option 2** in the Choose action, click **Add Action**, search "repeat", and select **Until** in the dropdown.

![Home Assistant Add action dialog with repeat searched and the Repeat action listed](/assets/temp-1-cook-chicken-example-pic-22.png)

21\. Under **Until Conditions**, select **Add condition**, then search "state".

![Home Assistant Add condition dialog with state searched and the State condition listed](/assets/temp-1-cook-chicken-example-pic-25.png)

22\. Type in "Chicken Monitor" and select it, then select **Off** in the dropdown for the state of the sensor.

![Home Assistant repeat until condition with Chicken Monitor entity and Off state highlighted](/assets/temp-1-cook-chicken-example-pic-26.png)

23\. Click the **Add Action** button under the until condition you created. Be very careful to select the correct **Add Action** button, as shown below.

![Home Assistant repeat until block with its inner Add Action button highlighted](/assets/temp-1-cook-chicken-example-pic-27.png)

24\. Search "light toggle" in the search bar, then select **Choose entity** and select the RGB LED for your device.

![Home Assistant Add action dialog with light toggle searched and Light: Toggle listed](/assets/temp-1-cook-chicken-example-pic-28.png)

25\. Go down to **Add Action** under **Option 2**, search "mobile", and select your phone as you did in step 15. Give it a message and a title, as shown below.

![Home Assistant Option 2 notification action titled Time to check the Chicken! with its message](/assets/temp-1-cook-chicken-example-pic-29.png)

26\. Optionally, add another action here that speaks out loud on your smart speakers, such as HomePods. Click **Add Action**, then search "TTS". This requires you to have Piper and a few other things already set up.

![Home Assistant Add action dialog with tts searched and the TTS Speak action listed](/assets/temp-1-cook-chicken-example-pic-30.png)![Home Assistant TTS Speak action on piper targeting Homepods with The Chicken is almost ready! message](/assets/temp-1-cook-chicken-example-pic-31.png)

Option 3 runs when you turn Chicken Monitor off.

27\. Click **Add Option** (this is now **Option 3**). Select **Add Condition**, search "triggered by", and then choose the "Chicken Monitor Off" trigger ID you created in step 6.

28\. While still under **Option 3** in the Choose action, click **Add Action**, search "light", and select **Light: Turn off**.

![Home Assistant Add action dialog with light.turn searched and Light: Turn off selected](/assets/temp-1-cook-chicken-example-pic-19.png)

29\. Click **Choose entity** and search for your device, such as "TEMP-1B RGB Light".

![Home Assistant Light Turn off action targeting the Apollo TEMP-1 RGB Light](/assets/temp-1-cook-chicken-example-pic-20.png)

*Shown on a TEMP-1; pick your TEMP-1B RGB Light instead.*

30\. Click **Add Action**, search "mobile" as you did above, and select your phone. Give it a message and, optionally, a title, as shown below.

![Home Assistant notification action titled Chicken Monitoring Stopped! with its message](/assets/temp-1-cook-chicken-example-pic-33.png)

31\. Click **Save** in the bottom right, then give the automation a name and save.

![Home Assistant save dialog for TEMP-1 Chicken Automation in the Food category with Save clicked](/assets/temp-1-cook-chicken-example-pic-34.png)

*Shown on a TEMP-1; the TEMP-1B steps are the same.*

You now have one automation that ties together the button you created on your dashboard and alerts you when your chicken is almost done, with a phone notification, a blinking green LED, and an optional TTS notification on your smart speakers. Thanks again to Discord user RalphP for this example!
