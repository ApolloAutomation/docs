---
title: Turn a light on and off with your BTN-1
description: Build two Homey flows that turn a light on when you click Button 1 on your BTN-1 and off when you hold it, with the button's LED showing which press came last.
---

# Turn a light on and off with your BTN-1

<span class="difficulty lvl-1">Difficulty: Level 1</span>

Every button on your Apollo BTN-1 tells Homey how you pressed it, and each press type can start its own flow. In this guide you build two flows in the Homey mobile app. The first turns a light on when you click Button 1 and lights that button's LED; the second turns both off again when you hold Button 1.

!!! note "Before you start"

    - Add your BTN-1 to Homey with the Apollo Automation app. See [Getting started](../../../general/setup/getting-started/).
    - Add the light you want to control to Homey.
    - Keep **Prevent sleep** on. It is on out of the box; [Keep your BTN-1 awake](#keep-your-btn-1-awake) explains why it matters.

## How button presses reach Homey

All four buttons on your BTN-1 share one trigger card: **Button pressed**. When you add it to a flow, you pick a **Button**, from **Button 1** to **Button 4**, and a **Press type**:

| Press type | How to press the button |
| --- | --- |
| **Click** | Press and release quickly, in under 0.3 seconds. |
| **Double click** | Two quick clicks, less than half a second apart. |
| **Triple click** | Three quick clicks, less than half a second apart. |
| **Hold** | Press and hold for 1 to 5 seconds, then let go. |

The card runs your flow every time the BTN-1 reports that button and press type. A **Click** flow ignores a double click, and two clicks with a pause between them run it twice.

The BTN-1 reports a press up to half a second after you let go, once it knows no further click is coming. **Hold** fires when you release the button, not while you are still holding it.

## Flow 1: turn the light on with a click

This flow has one trigger and two actions: it turns your light on and sets Button 1's LED to a color, so the button itself shows that the light is on.

1. In the Homey mobile app, tap **Flow** in the bottom bar, then tap **+** at the top right (or **Create a Flow** if you have none yet).
2. Under **When...**, tap **Add Card**. Open **Apollo Automation** under **Apps**, and choose your BTN-1.
3. Choose the card **Button pressed**.
4. Tap **Button** and pick **Button 1**. Tap **Press type** and pick **Click**, then tap the check mark at the top right.
5. Under **Then...**, tap **Add Card**. Find your light under **Zones & Devices**, choose **Turn on**, and tap the check mark.
6. Under **Then...**, tap **Add Card** again. Open **Apollo Automation** under **Apps**, choose your BTN-1, and choose **Set button light color**.
7. Tap **Button light** and pick **Button 1**. Tap **Color**, pick a color, and tap the check mark.
8. Tap **Next**. Name the flow, for example **BTN-1 light on**, and tap **Save Flow**.

The flow now shows in **My Flows**. Click Button 1 and your light turns on, with the button lit in the color you picked.

!!! tip "Pick your BTN-1, not another Apollo device"

    The Apollo Automation app offers **Button pressed**, **Set button light color**, and **Turn off button light** on every Apollo device you have added, but only a BTN-1 has the buttons and LEDs they work with. If a flow never runs, check that each of its Apollo cards points at your BTN-1.

## Flow 2: turn the light off with a hold

The second flow mirrors the first. Build it the same way, with these changes:

1. Under **When...**, choose **Button pressed**, then pick **Button 1** and **Hold**.
2. Under **Then...**, choose **Turn off** for the same light.
3. For the second **Then...** card, choose **Turn off button light** from your BTN-1 and pick **Button 1** under **Button light**.
4. Name the flow **BTN-1 light off** and tap **Save Flow**.

Now Button 1 runs your light: a click turns it on, a hold turns it off, and the LED follows along.

## Keep your BTN-1 awake

Your BTN-1 can only report a double click, triple click, or hold while it is awake and connected to Homey.

!!! warning "A sleeping BTN-1 only reports clicks"

    The BTN-1 ships with **Prevent sleep** on, so it stays connected and reports every press. If you turn it off to save battery, the BTN-1 sleeps between presses. Homey receives the press that wakes it as a **Click** of that button, whatever press type you used, and only after the BTN-1 has reconnected, at least 5 seconds later. It then goes back to sleep.

    To use every press type, open the device in Homey, go to its **Settings**, and check **Prevent sleep** under **Battery settings (if battery is present)**. Homey can only change this setting while the BTN-1 is awake, so wake it first with its reset button. [How to wake up your sensor](../../battery-sensors/wake-up-battery-sensor/) shows where the reset button is and how to keep the BTN-1 awake, and [Prevent sleep](../../additional-info/prevent-sleep/) explains what each sleep setting does on the BTN-1.

## Test your flows

Run the flows end to end by clicking and holding Button 1 while you watch the light. To check a single flow without pressing the button, tap the play button next to it in **My Flows**; it runs its **Then** cards once, and a green check mark confirms it ran.

Your BTN-1 also shows you what Homey received. Open it in Homey and look at the **Button 1** reading: it shows the last press type, such as **Click** or **Hold**.

If a flow doesn't run:

- Watch the **Button 1** reading as you press. If it doesn't show the press type you used, check your timing: release within 0.3 seconds for a click, or hold for 1 to 5 seconds.
- Check that both flows are switched on in **My Flows**.
- Check that the BTN-1 is awake, and that every Apollo card in the flow points at your BTN-1.

## Take it further

- **More presses on the same button**: build flows for **Double click** and **Triple click** on Button 1, for example to turn on a second light.
- **A status light for the house**: **Set button light color** works in any flow, not only flows that start with a button press. For example, light Button 4 red when a door opens, and turn it off with **Turn off button light** when the door closes.

!!! success "Next step: put all four buttons to work"

    Button 1 is set up. The next guide shows you how to plan and build flows for all four buttons and all four press types, up to 16 actions from one BTN-1.

    [Use all four buttons and press types](../blueprint/){ .md-button .md-button--primary }
