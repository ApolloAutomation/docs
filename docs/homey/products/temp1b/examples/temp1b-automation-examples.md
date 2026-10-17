---
title: Automation examples using a TEMP-1B
description: "Homey flows for the TEMP-1B: a push notification when your freezer gets too warm, and a green light plus one notification when the food probe reaches its target temperature."
---

# Automation examples using a TEMP-1B

<span class="difficulty lvl-2">Difficulty: Level 2</span>

<p class="automation-steps-heading">🌱 New here? Try these first:</p>
<div class="automation-steps">
  <div class="step">
    <a class="step-title" href="../temp1b-alert-example/">TEMP-1B alert outside a temperature range</a>
    <span class="difficulty lvl-1">Difficulty: Level 1</span>
  </div>
</div>

Your Apollo TEMP-1B sends every probe reading to Homey while it's awake, and each new reading can start a flow. This page has two flows to build in the Homey mobile app: a freezer alert, and a food probe flow that lights the TEMP-1B green and messages you when dinner is almost ready.

!!! note "Before you start"

    - Add your TEMP-1B to Homey with the Apollo Automation app. See [Getting started](../../setup/getting-started-temp1/).
    - Install the Homey mobile app on every phone that should get a notification.
    - For the freezer flow, plug in the [temperature probe](../../addons/temp-probe/). For the food flow, plug in the [food probe](../../addons/food-probe/).

## How probe readings reach Homey

The Apollo Automation app gives each probe its own reading on the TEMP-1B and its own trigger card. Which one reports depends on the **Select probe** setting: open your TEMP-1B's **Settings** and find it under **Probes and offsets for TEMP-1 and TEMP-1B**.

| Probe | Reading in Homey | Trigger card | How often it reports while awake | Set **Select probe** to |
| --- | --- | --- | --- | --- |
| Temperature probe | **Temperature Probe** | **Temperature probe changed** | About once a minute | **Temperature** |
| Food probe | **Food Probe** | **Food probe changed** | Every few seconds | **Food** |

Both cards hand the new reading to the flow as a **Temperature** token, always in °C. The probe that isn't selected sends no readings, so its card never runs.

The cards run each time the reading changes, not only when it crosses your limit. That's why each flow below checks the **Temperature** token in an **And...** condition, and why the food flow adds a second condition so it alerts you once instead of every few seconds.

### Readings and sleep

The TEMP-1B only sends readings while it's awake. With **Prevent sleep** on, it stays connected and reports as shown in the table. With **Prevent sleep** off, it reports once each time it wakes, every 12 hours unless you change **Sleep duration** (in hours). Both settings are under **Battery settings (if battery is present)** in your TEMP-1B's **Settings**, and [Prevent sleep](../../setup/prevent-sleep/) walks you through changing them.

!!! warning "Change settings while the TEMP-1B is awake"

    Homey can only change the TEMP-1B's settings, including **Select probe** and **Prevent sleep**, while it's awake. If Homey shows **The device is asleep. Settings can be changed when it next wakes up.**, wake the sensor and try again. See [How to wake up your sensor](../../battery-sensors/wake-up-battery-sensor/).

## Freezer over its maximum temperature

This flow sends a push notification whenever the freezer probe reads warmer than your maximum. It is Flow 1 from [TEMP-1B alert outside a temperature range](../temp1b-alert-example/#flow-1-too-warm), which walks through every tap and shows you how to pick a limit and a **Sleep duration** that suit your freezer.

| Column | Card | Set it to |
| --- | --- | --- |
| **When...** | **Temperature probe changed**, from **Apollo Automation** for your TEMP-1B | Nothing to set |
| **And...** | Homey's built-in condition for comparing numbers | **Temperature** token greater than **-10** |
| **Then...** | **Send Message to User**, from **Push Notifications** | A message such as **Check the freezer!** with the **Temperature** token, sent to **Everyone** |

Once it's saved, any probe reading above -10 °C sends the alert, with a reminder each time the reading changes until the freezer cools down again.

## Food probe reaches a target temperature

Chicken is safe to eat at 74 °C (165 °F), and it keeps rising a few degrees while it rests. This flow fires at 71 °C (160 °F) so you can take it off the heat in time. When the food probe gets there, the TEMP-1B's light turns green and your phone gets one notification.

The light also stops the alert from repeating. The food probe reports every few seconds, so the flow only runs while the light is off; once the flow has turned it green, later readings leave it alone.

!!! warning "Keep the TEMP-1B away from the heat"

    Only the food probe and its cable can go on the grill or in the oven. Set the TEMP-1B itself somewhere cool and dry, such as a side shelf.

Before you build the flow, wake your TEMP-1B, turn on **Prevent sleep** so it reports for the whole cook, and set **Select probe** to **Food**. Check that the **Food Probe** reading on your TEMP-1B changes when you hold the probe tip in your hand.

1. In the Homey mobile app, tap **Flow** in the bottom bar, then tap **+** at the top right (or **Create a Flow** if you have none yet).
2. Under **When...**, tap **Add Card**. Open **Apollo Automation** under **Apps**, choose your TEMP-1B, and choose **Food probe changed**.
3. Under **And...**, tap **Add Card** and add Homey's built-in condition for comparing numbers. Set it to check that the **Temperature** token is greater than **71**.
4. Under **And...**, tap **Add Card** again. Find your TEMP-1B under **Zones & Devices** and choose its condition for whether it is turned on. Turn on **Invert**, so the card checks that the TEMP-1B is turned off. On a TEMP-1B, turned on and off means its RGB light.
5. Under **Then...**, tap **Add Card**. Find your TEMP-1B under **Zones & Devices** and choose **Turn on**.
6. Under **Then...**, tap **Add Card** again. Choose **Set a color** for your TEMP-1B, pick green, and tap the check mark.
7. Under **Then...**, add **Send Message to User** from **Push Notifications**. Type a message such as **Check the food! The food probe reads**, add the **Temperature** token after it, and pick a **User**.
8. Tap **Next**. Name the flow, for example **Food is ready**, and tap **Save Flow**.

The flow now shows in **My Flows**. When the food probe passes 71 °C, your TEMP-1B glows green and your phone gets one notification.

### Reset it for the next cook

When the food is off the heat, open your TEMP-1B in the Homey app and turn it off, which turns its light off. With the light off, the flow is ready to alert you again. The TEMP-1B also turns its light off whenever it goes to sleep.

Then turn **Prevent sleep** off again if you want to save battery, and switch the flow off in **My Flows** until your next cook.

## Test your flows

To check the alert without cooking anything, wake your TEMP-1B and tap the play button next to the flow in **My Flows**. It runs its **Then** cards once, and a green check mark confirms it ran: the TEMP-1B lights green and the notification arrives. Turn the TEMP-1B's light off afterwards so the flow is ready for the real thing.

If a flow doesn't run:

- Check that **Select probe** matches the probe the flow uses: **Temperature** for the freezer flow, **Food** for the food flow.
- Check that the TEMP-1B is awake, or wait for its next wake-up.
- Check that your limits are in °C.
- For the food flow, check that the TEMP-1B's light is off before the food reaches its target.
- Check that the flow is switched on in **My Flows**.

## Take it further

- **More probes**: with the [Multi-Probe Splitter](../../addons/multiple-probes/), the extra probes each get their own trigger card: **Temperature probe 2 changed**, **Temperature probe 3 changed**, and **Temperature probe 4 changed**. Build the freezer flow once per probe to watch a fridge and a freezer from one TEMP-1B.
- **Other targets**: change the number in the food flow's condition for other dishes, and give each one its own message.

## Coming from the Home Assistant cook chicken example

The [Home Assistant version of the cook chicken example](../../../../../products/temp1b/examples/temp1b-automation-examples/#cook-chicken-example), shared by Discord user RalphP, does a few things the Homey flow above handles differently or leaves out:

- **A dashboard button to start and stop monitoring.** In Homey, switch the flow on in **My Flows** when you start cooking and off when you're done.
- **A blinking light when the food is ready.** The TEMP-1B has pulse effects for its light, but the Apollo Automation app has no card for them, so in Homey the light stays solid green.
- **A spoken announcement on smart speakers.** The Home Assistant version uses text-to-speech. This guide doesn't cover speakers.
