---
title: TEMP-1 automation examples
description: Three Home Assistant automations for your TEMP-1, from a freezer temperature alert and a food probe alert to a dashboard button that monitors chicken while it cooks.
---
# Automation examples using a TEMP-1

These three examples show you how to put your Apollo TEMP-1 to work in Home Assistant: get an alert when your freezer warms up, know when your food reaches temperature, and run a whole chicken-cooking routine from one dashboard button.

## Freezer temperature probe example

This example walks you through setting up an automation in Home Assistant with the temperature probe in your freezer. At the end, you'll have an automation that sends your phone a notification when the freezer goes above the temperature you set.

!!! danger "Only the probe goes in the freezer"

    Only the temperature probe and its wire can withstand the temperatures in a fridge, freezer, and similar places. Keep your TEMP-1 itself in a cool, dry place.

1\. Place the temperature probe in your freezer and wait for it to settle around 0°F (-18°C).

2\. Once it has settled, look at the probe's history graph in Home Assistant (shown below) and decide on good values for both the maximum and minimum temperatures. In this example, the mini freezer seems to max out at 30°F, so the maximum goes slightly above that range. However, <a href="https://www.fda.gov/food/buy-store-serve-safe-food/refrigerator-thermometers-cold-facts-about-food-safety" target="_blank" rel="noreferrer nofollow noopener">most freezers should not reach above 0°F</a>, so you'll likely need a lower value than this example. The minimums in this example are around -20°F.

![Home Assistant history graph of the TEMP-1 temperature probe with arrows at freezer highs and lows](/assets/temp-1-temp-probe-ex-automation-pic-1.png)

3\. Convert your values to Celsius, because **Max Probe Temp** and **Min Probe Temp** are set in Celsius, then enter them. This example uses a **Max Probe Temp** of 2°C and a **Min Probe Temp** of -30°C. Yours will likely be different, especially your **Max Probe Temp**. These settings control the TEMP-1's built-in buzzer alarm.

![Home Assistant settings with Max Probe Temp set to 2.0 °C and Min Probe Temp set to -30.0 °C](/assets/temp-1-temp-probe-ex-automation-pic-2.png)

Next, create the automation that sends the notification to your phone.

4\. Go to **Settings → Automations & scenes**, click **+ Create automation** in the bottom right, then **Create new automation**.

[![Open your Home Assistant instance and show your automations.](https://my.home-assistant.io/badges/automations.svg)](https://my.home-assistant.io/redirect/automations/)

5\. Click **Add trigger → Entity → Numeric state** and search for your TEMP-1 temperature probe, such as "temp-1 temperature probe". In the box labeled **Above**, type the maximum temperature you decided on in step 2. Prefer YAML? Skip ahead to the [freezer automation YAML](#freezer-automation-yaml).

![Home Assistant numeric state trigger on the TEMP-1 Temperature Probe, with the entity and the Above field set to 30 highlighted](/assets/temp-1-temp-probe-ex-automation-pic-3.png)

6\. Click **Add action**, type "iPhone", and select your phone. If you don't see your phone, or you have an Android phone, type "notify" instead and scroll down until you find your phone in the list.

![Home Assistant Add action search for iphone with the mobile app notification action highlighted](/assets/temp-1-temp-probe-ex-automation-pic-4.png)

!!! tip "Still don't see your phone?"

    You need the Home Assistant mobile app installed on your phone for this step to work. If you don't have it, try another notification instead of your phone, such as a TTS notification on your speakers. This could be a fun way to announce that dinner is ready!

7\. Type your message. If you want a title too, check the box for the title and type it in. This example's message is "The temperature probe on your TEMP-1 reached its max temperature and your freezer might be having issues." and its title is "Check the freezer!".

![Home Assistant notification action with the message and Check the freezer! title fields highlighted](/assets/temp-1-temp-probe-ex-automation-pic-5.png)

8\. Click **Save** in the bottom right, then give the automation a name and, optionally, a description and a category.

![Home Assistant save dialog for Freezer Over Max Temp Automation with name, description, and category filled in](/assets/temp-1-temp-probe-ex-automation-pic-6.png)

You're done. Your phone now gets a notification whenever the freezer probe goes above your maximum temperature.

### Freezer automation YAML

If you'd rather work in YAML, here's the finished automation. Use your own entity ID and phone in place of the ones shown.

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

This example walks you through setting up an automation in Home Assistant with the food probe while chicken (or anything else) cooks to 165°F (73.9°C). At the end, you'll have an automation that sends your phone a notification when your food reaches that temperature.

!!! danger "Only the probe goes on the grill"

    Only the <a href="https://wiki.apolloautomation.com/products/temp1/addons/food-probe/" title="Click me for more info on installation of food probe and usage." target="_blank" rel="noreferrer nofollow noopener">food probe and the wire can withstand temperatures on a grill, in the oven, and similar places</a>. Keep your TEMP-1 itself in a cool, dry place.

1\. Set your **Max Probe Temp** to 73.9°C. **Max Probe Temp** is always set in Celsius, even if you use °F in the automation below.

![Home Assistant setting with Max Probe Temp set to 73.9 °C highlighted](/assets/temp-1-food-probe-ex-automation-pic-1.png)

2\. Place the food probe inside your food once it's on the grill.

3\. Go to **Settings → Automations & scenes**, click **+ Create automation** in the bottom right, then **Create new automation**.

[![Open your Home Assistant instance and show your automations.](https://my.home-assistant.io/badges/automations.svg)](https://my.home-assistant.io/redirect/automations/)

4\. Click **Add trigger → Entity → Numeric state** and search for your TEMP-1 food probe, such as "temp-1 food probe". In the box labeled **Above**, type the temperature you want for your food. This example uses 165°F (73.9°C), the temperature it's safe to cook chicken to. Prefer YAML? Skip ahead to the [food probe automation YAML](#food-probe-automation-yaml).

![Home Assistant numeric state trigger on the TEMP-1 Food Probe, with the entity and the Above field set to 165 highlighted](/assets/temp-1-food-probe-ex-automation-pic-3.png)

5\. Click **Add action**, type "iPhone", and select your phone. If you don't see your phone, or you have an Android phone, type "notify" instead and scroll down until you find your phone in the list.

![Home Assistant Add action search for iphone with the mobile app notification action highlighted](/assets/temp-1-temp-probe-ex-automation-pic-4.png)

!!! tip "Still don't see your phone?"

    You need the Home Assistant mobile app installed on your phone for this step to work. If you don't have it, try another notification instead of your phone, such as a TTS notification on your speakers. This could be a fun way to announce that dinner is ready!

6\. Type your message. If you want a title too, check the box for the title and type it in. This example's message is "The temperature probe on your TEMP-1 reached its max temperature and your food is ready." and its title is "Check the food!".

![Home Assistant notification action with the message and Check the food! title fields highlighted](/assets/temp-1-food-probe-ex-automation-pic-5.png)

7\. Click **Save** in the bottom right, then give the automation a name and, optionally, a description and a category.

![Home Assistant save dialog for Food over Max Temp Automation with name, description, category, and Save highlighted](/assets/temp-1-food-probe-ex-automation-pic-6.png)

You're done. Your phone now gets a notification when your food reaches the temperature you set.

### Food probe automation YAML

If you'd rather work in YAML, here's the finished automation. Use your own entity ID and phone in place of the ones shown.

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

This example walks you through adding a "Chicken Monitor" button to your dashboard and an automation that runs when you press it. The automation:

- Turns the RGB LED green while it's running.
- Messages your phone when it starts, when the temperature is reached, and when it finishes.
- Turns the RGB LED off at the end.

Thanks to Discord user RalphP for this!

The automation has three triggers, each with its own trigger ID, and one **Choose** action with an option for each trigger ID. You'll build it in that order.

### Create the button

1\. Create a new toggle helper called "Chicken Monitor". For step-by-step directions on creating a toggle helper, <a href="https://wiki.apolloautomation.com/products/general/battery-sensors/awake-ha-helper/" target="_blank" rel="noreferrer nofollow noopener">see this guide</a>.

![Home Assistant Create Toggle dialog for a Chicken Monitor helper with the Create button highlighted](/assets/temp-1-cook-chicken-example-pic-1.png)

2\. Edit your dashboard, add a button card, select Chicken Monitor, and then save.

![Home Assistant Add to dashboard dialog with button typed in the card search](/assets/temp-1-cook-chicken-example-pic-3.png)![Home Assistant Button card configuration with the Chicken Monitor entity and Save button highlighted](/assets/temp-1-cook-chicken-example-pic-2.png)

### Create the automation and its triggers

Next, you'll create the automation and add its three triggers, each with its own trigger ID.

3\. Go to **Settings → Automations & scenes**, click **+ Create automation** in the bottom right, then **Create new automation**.

[![Open your Home Assistant instance and show your automations.](https://my.home-assistant.io/badges/automations.svg)](https://my.home-assistant.io/redirect/automations/)

4\. Click **Add trigger → Entity → State** and search for "Chicken Monitor". In the box labeled **To**, select **On**.

![Home Assistant state trigger for Chicken Monitor with the To field set to On](/assets/temp-1-cook-chicken-example-pic-4.png)

5\. Create a trigger ID for this trigger called "Chicken Monitor On".

![Home Assistant trigger options menu open with Edit ID selected](/assets/temp-1-cook-chicken-example-pic-5.png)![Home Assistant Chicken Monitor trigger with Trigger ID set to Chicken Monitor On](/assets/temp-1-cook-chicken-example-pic-6-1.png)

6\. Click **Add trigger → Entity → State** and search for "Chicken Monitor". In the box labeled **To**, select **Off**. Create a trigger ID for this trigger called "Chicken Monitor Off".

![Home Assistant state trigger for Chicken Monitor set to Off with Trigger ID Chicken Monitor Off highlighted](/assets/temp-1-cook-chicken-example-pic-21.png)

7\. Click **Add trigger → Entity → Numeric state** and search for your TEMP-1 food probe entity, such as "temp-1 food probe". In the box labeled **Above**, type the temperature you want for your food. This example uses 160°F (71.1°C), because the chicken will rest and reach 165°F once it's removed from the oven or grill.

![Home Assistant numeric state trigger on TEMP-1 Food Probe with the Above field set to 160](/assets/temp-1-cook-chicken-example-pic-7.png)

8\. Create a trigger ID for this trigger called "Temp Reached".

![Home Assistant TEMP-1 Food Probe trigger with Trigger ID set to Temp Reached highlighted](/assets/temp-1-cook-chicken-example-pic-8.png)

### Option 1: Monitoring starts

Option 1 runs when you turn Chicken Monitor on. It turns the LED green and tells your phone that monitoring has started.

9\. Click **Add action**, search "choose", and select it.

![Home Assistant Add action dialog with choose searched and the Choose action listed](/assets/temp-1-cook-chicken-example-pic-12.png)

10\. Under Option 1, select **Add condition**, search "trigger id", and select **Triggered by**.

![Home Assistant Add condition dialog with trigger id searched and Triggered by listed](/assets/temp-1-cook-chicken-example-pic-13.png)

11\. Check **State changed to on**, the first trigger in the list. It's the trigger you gave the Chicken Monitor On ID in step 5.

![Home Assistant Triggered by condition with the first trigger, State changed to on, checked and highlighted](/assets/temp-1-cook-chicken-example-pic-14.png)

12\. Still under Option 1 in the Choose action, click **Add action**, search "light", and select **Light: Turn on**.

![Home Assistant Add action dialog with light searched and Light: Turn on highlighted](/assets/temp-1-cook-chicken-example-pic-9.png)

13\. Click **Choose entity** and search for your device, such as "TEMP-1 RGB Light".

![Home Assistant Choose entity search for TEMP-1 with the cursor on the Apollo TEMP-1 RGB Light entity](/assets/temp-1-cook-chicken-example-pic-10.png)

14\. Click **Advanced options**, check the box for **Color name**, then select a color from the drop-down, such as **Green**.

![Home Assistant light action Advanced options with Color name checked and Green picked from the list](/assets/temp-1-cook-chicken-example-pic-11.png)

15\. Still under Option 1 in the Choose action, click **Add action**, search "mobile", and select your phone in the list.

![Home Assistant Add action dialog with mobile searched and the iPhone notification action highlighted](/assets/temp-1-cook-chicken-example-pic-15.png)

16\. Write a custom title and message. The message is required, but the title is not.

![Home Assistant notification action with the title Chicken Monitoring Started and a custom message](/assets/temp-1-cook-chicken-example-pic-16.png)

17\. Check your work. When you're done with this part, Option 1 looks like this:

![Home Assistant Option 1 triggered by Chicken Monitor On with light turn on and notification actions](/assets/temp-1-cook-chicken-example-pic-17-1.png)

### Option 2: Temperature reached

Option 2 runs when the food probe reaches your temperature. It blinks the LED until you turn Chicken Monitor off, and messages your phone.

18\. Click **Add option** at the bottom. Under Option 2, select **Add condition**, search "trigger id", and select **Triggered by**.

![Home Assistant Add condition dialog with trigger id searched and Triggered by listed](/assets/temp-1-cook-chicken-example-pic-13.png)

19\. Check **Temp Reached**, the trigger ID you created in step 8.

![Home Assistant Option 2 Triggered by condition with only Temp Reached checked](/assets/temp-1-cook-chicken-example-pic-18-1.png)

20\. Still under Option 2 in the Choose action, click **Add action**, search "repeat", and select **Until** in the drop-down.

![Home Assistant Add action dialog with repeat searched and the Repeat action listed](/assets/temp-1-cook-chicken-example-pic-22.png)

21\. Under **Until** conditions, select **Add condition** and search "state".

![Home Assistant Add condition dialog with state searched and the State condition listed](/assets/temp-1-cook-chicken-example-pic-25.png)

22\. Type "Chicken Monitor" and select it, then select **Off** in the drop-down for the state of the sensor.

![Home Assistant repeat until condition with Chicken Monitor entity and Off state highlighted](/assets/temp-1-cook-chicken-example-pic-26.png)

23\. Click **Add action** under the **Until** condition you just created. Be very careful to select the correct **Add action** button, as shown below.

![Home Assistant repeat until block with its inner Add Action button highlighted](/assets/temp-1-cook-chicken-example-pic-27.png)

24\. Search "light toggle" in the search bar, then select **Choose entity** and select the RGB LED for your device.

![Home Assistant Add action dialog with light toggle searched and Light: Toggle listed](/assets/temp-1-cook-chicken-example-pic-28.png)

25\. Go down to **Add action** under Option 2, search "mobile", and select your phone, as you did in step 15. Give it a message and a title, as shown below.

![Home Assistant Option 2 notification action titled Time to check the Chicken! with its message](/assets/temp-1-cook-chicken-example-pic-29.png)

26\. (Optional) Add another action here to speak out loud on your smart speakers, such as HomePods. Click **Add action** and search "TTS". This requires you to have Piper and a few other things already set up.

![Home Assistant Add action dialog with tts searched and the TTS Speak action listed](/assets/temp-1-cook-chicken-example-pic-30.png)![Home Assistant TTS Speak action on piper targeting Homepods with The Chicken is almost ready! message](/assets/temp-1-cook-chicken-example-pic-31.png)

### Option 3: Monitoring stops

Option 3 runs when you turn Chicken Monitor off. It turns the LED off and tells your phone that monitoring has stopped.

27\. Click **Add option** (this is now Option 3). Select **Add condition**, search "triggered by", and choose the "Chicken Monitor Off" trigger ID you created in step 6.

28\. Still under Option 3 in the Choose action, click **Add action**, search "light", and select **Light: Turn off**.

![Home Assistant Add action dialog with light.turn searched and Light: Turn off selected](/assets/temp-1-cook-chicken-example-pic-19.png)

29\. Click **Choose entity** and search for your device, such as "TEMP-1 RGB Light".

![Home Assistant Light Turn off action targeting the Apollo TEMP-1 RGB Light](/assets/temp-1-cook-chicken-example-pic-20.png)

30\. Click **Add action**, search "mobile" as you did above, and select your phone. Give it an optional title and message, as shown below.

![Home Assistant notification action titled Chicken Monitoring Stopped! with its message](/assets/temp-1-cook-chicken-example-pic-33.png)

31\. Click **Save** in the bottom right, then give the automation a name and save it.

![Home Assistant save dialog for TEMP-1 Chicken Automation in the Food category with Save clicked](/assets/temp-1-cook-chicken-example-pic-34.png)

You now have one automation that ties together the button you created in the dashboard and alerts you when your chicken is almost done, with a phone notification, a blinking green LED, and an optional TTS notification on your smart speakers. Thanks again to Discord user RalphP for this example!
