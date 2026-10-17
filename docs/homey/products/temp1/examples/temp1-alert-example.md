---
title: TEMP-1 alert outside a temperature range
description: "Build two Homey flows that send a push notification when the TEMP-1 temperature probe reads warmer or colder than the range you pick, and optionally sound the TEMP-1's own buzzer."
---

# TEMP-1 alert outside a temperature range

<span class="difficulty lvl-1">Difficulty: Level 1</span>

Your Apollo TEMP-1 sends its temperature probe reading to Homey about once a minute, and every new reading can start a flow. In this guide you build two flows in the Homey mobile app that keep watch on a freezer: the first sends a push notification when the probe gets too warm, the second when it gets too cold.

!!! note "Before you start"

    - Add your TEMP-1 to Homey with the Apollo Automation app. See [Getting started](../../setup/getting-started-temp1/).
    - Plug the [temperature probe](../../addons/temp-probe/) into the TEMP-1. Open your TEMP-1's **Settings** and, under **Probes and offsets for TEMP-1 and TEMP-1B**, set **Select probe** to **Temperature**. With **Food** selected, the temperature probe sends no readings.
    - Install the Homey mobile app on every phone that should get the alert.

## Pick your range

Find out what your freezer normally swings between before you set any limits. That way the alert only fires when something is actually wrong.

1. Place the probe in the freezer and run its flat cable out through the door seal. Keep the TEMP-1 itself outside the freezer, somewhere cool and dry: only the probe and its cable can handle the cold.
2. Leave it for a few hours so the reading settles. [Most freezers should sit at or below -18 °C (0 °F)](https://www.fda.gov/food/buy-store-serve-safe-food/refrigerator-thermometers-cold-facts-about-food-safety).
3. In Homey Insights, look at your TEMP-1's **Temperature Probe** history. Note the highest and lowest readings.
4. Pick a maximum a little above the highest reading and a minimum a little below the lowest. This guide uses -10 °C and -30 °C; yours will likely differ.

You now have a range that covers normal use and flags a real problem.

!!! tip "Enter your limits in degrees Celsius"

    The **Temperature Probe** reading, and the **Temperature** token the flows below compare, are always in °C. If you think in Fahrenheit, convert first: -10 °C is 14 °F, and -30 °C is -22 °F.

## Flow 1: too warm

This flow runs each time the probe reading changes, checks it against your maximum, and sends the alert when the freezer is too warm.

1. In the Homey mobile app, tap **Flow** in the bottom bar, then tap **+** at the top right (or **Create a Flow** if you have none yet).
2. Under **When...**, tap **Add Card**. Open **Apollo Automation** under **Apps**, and choose your TEMP-1.
3. Choose the card **Temperature probe changed**. It hands the new reading to the rest of the flow as the **Temperature** token.
4. Under **And...**, tap **Add Card** and add Homey's built-in condition for comparing numbers. Set it to check that the **Temperature** token is greater than **-10**.
5. Under **Then...**, tap **Add Card** and choose **Send Message to User** from **Push Notifications**.
6. Type a message, for example **Check the freezer! The TEMP-1 probe reads**, and add the **Temperature** token after it.
7. Tap **User** and pick who gets the alert, such as **Everyone**, then tap the check mark at the top right.
8. Tap **Next**. Name the flow, for example **Freezer too warm**, and tap **Save Flow**.

The flow now shows in **My Flows**. Any probe reading above -10 °C sends the alert to your phone.

## Flow 2: too cold

The second flow mirrors the first. Build it the same way, with these changes:

1. In the **And...** condition, check that the **Temperature** token is less than **-30**.
2. Change the message, for example to **The freezer is colder than usual. The TEMP-1 probe reads**, followed by the **Temperature** token.
3. Name the flow **Freezer too cold** and tap **Save Flow**.

Both ends of your range are now covered: you hear about it whether the freezer warms up or runs too cold.

!!! warning "Expect a reminder with each new reading"

    **Temperature probe changed** runs every time the reading changes, not only when it crosses your limit. While the probe stays out of range, every change sends another notification, up to once a minute, until the temperature is back inside your range. To pause the reminders while you deal with the freezer, switch the flow off in **My Flows**, and switch it back on afterwards.

## Test your flows

To check the alert without warming up your freezer, tap the play button next to a flow in **My Flows**. It runs its **Then** cards once, and a green check mark confirms it ran. Your phone gets the notification.

If a flow doesn't run when the freezer is out of range:

- Check that **Select probe** is set to **Temperature** and that the **Temperature Probe** reading keeps updating.
- Check that your limits are in °C.
- Check that both flows are switched on in **My Flows**.

## Optional: sound the TEMP-1's buzzer too

The TEMP-1 can also raise the alarm on its own. When you turn this on, the sensor checks every probe reading against a minimum and maximum you store on the device and sounds a short siren from its buzzer when the reading is outside them. It works alongside your flows, so anyone near the freezer hears it even if their phone is on silent.

1. Open your TEMP-1's **Settings**.
2. Under **Probes and offsets for TEMP-1 and TEMP-1B**, set **Minimum probe temperature** and **Maximum probe temperature** in °C, for example **-30** and **-10**.
3. Under **Temperature range and alarm settings for TEMP PRO-1**, turn on **Alarm when temperature outside configured range**. The group is named for the TEMP PRO-1, but this setting also switches the TEMP-1's alarm on and off.

The TEMP-1 now sounds the siren with each probe reading outside your range, until the reading is back inside it.

!!! tip "Use the probe settings, not the TEMP PRO-1 ones"

    **Minimum temperature** and **Maximum temperature** in the TEMP PRO-1 group belong to the TEMP PRO-1 and don't change anything on a TEMP-1. Set the range with **Minimum probe temperature** and **Maximum probe temperature** instead.

!!! success "Next step: know when dinner is ready"

    Your freezer is covered. The automation examples put the food probe to work: a flow that lights your TEMP-1 green and sends you one notification when your food reaches its target temperature.

    [Build the food probe flow](../temp1-automation-examples/#food-probe-reaches-a-target-temperature){ .md-button .md-button--primary }
