---
title: Use all four buttons and press types
description: Homey has no blueprints, so give each BTN-1 press its own flow. Plan and build flows for all four buttons and all four press types (click, double click, triple click, and hold), and use the button LEDs as feedback.
---

# Use all four buttons and press types

<span class="difficulty lvl-2">Difficulty: Level 2</span>

<p class="automation-steps-heading">🌱 New here? Try these first:</p>
<div class="automation-steps">
  <div class="step">
    <a class="step-title" href="../example-automation/">Turn a light on and off with your BTN-1</a>
    <span class="difficulty lvl-1">Difficulty: Level 1</span>
  </div>
</div>

Your Apollo BTN-1 has four buttons, and each one reports four press types: **Click**, **Double click**, **Triple click**, and **Hold**. That is up to 16 actions from one device.

In Home Assistant, a single [BTN-1 blueprint](../../../../../products/btn1/examples/blueprint/) covers every press. Homey has no blueprints, and the BTN-1 doesn't need one there: every press starts its own flow with the **Button pressed** card. This guide shows you how to plan your presses, build the flows, and light up the buttons so you can see what each press did.

!!! note "Before you start"

    - Add your BTN-1 to Homey with the Apollo Automation app. See [Getting started](../../../general/setup/getting-started/).
    - Build your first BTN-1 flow with the [step-by-step guide](../example-automation/). This page builds on it.
    - Keep **Prevent sleep** on. See [Keep the BTN-1 awake](#keep-the-btn-1-awake).

## The Button pressed card

Every flow on this page starts with the same trigger card, **Button pressed**. On it, you pick two things:

- **Button**: **Button 1**, **Button 2**, **Button 3**, or **Button 4**.
- **Press type**: one of the four below.

| Press type | How to press the button |
| --- | --- |
| **Click** | Press and release quickly, in under 0.3 seconds. |
| **Double click** | Two quick clicks, less than half a second apart. |
| **Triple click** | Three quick clicks, less than half a second apart. |
| **Hold** | Press and hold for 1 to 5 seconds, then let go. |

Each card only runs for the button and press type you picked, so a flow for Button 2 never fires when you press Button 3.

Not sure which button is which? Open your BTN-1 in Homey and press a button. The matching reading, **Button 1** to **Button 4**, shows the press type Homey received. Use a different press type each time, so you can see which reading updates.

## Plan your presses

Sixteen presses are a lot to keep in your head, so sketch a plan before you build anything. Here is an example:

| Button | Click | Double click | Triple click | Hold |
| --- | --- | --- | --- | --- |
| **Button 1** | Desk lamp on | Monitor light on | | Desk lamp and monitor light off |
| **Button 2** | Ceiling light on | | | Ceiling light off |
| **Button 3** | Fan on | | | Fan off |
| **Button 4** | Hallway light on | | | Every light in the plan off |

A few rules of thumb:

- Put the actions you use most on **Click**. It is the quickest press, and the only one a sleeping BTN-1 reports.
- Pair opposites on one button, such as **Click** for on and **Hold** for off.
- Leave a cell empty if you don't need it. A press with no flow does nothing.

## Build one flow per press

Each filled cell in your plan becomes one flow. Build them one at a time, starting with the presses you will use most.

1. In the Homey mobile app, tap **Flow** in the bottom bar, then tap **+** at the top right.
2. Under **When...**, tap **Add Card**. Open **Apollo Automation** under **Apps**, choose your BTN-1, and choose **Button pressed**.
3. Tap **Button** and pick the button from your plan. Tap **Press type** and pick the press type, then tap the check mark at the top right.
4. Under **Then...**, tap **Add Card** and add the action from your plan, for example **Turn on** or **Turn off** for a light under **Zones & Devices**. Add more **Then...** cards if the press should do several things.
5. Tap **Next**. Name the flow after the button and press, for example **BTN-1 Button 2 Click**, and tap **Save Flow**.

Repeat these steps for every press in your plan. Each flow shows in **My Flows**, and each press on the BTN-1 runs the flow you built for it.

## Light up the buttons

Each button on the BTN-1 has its own color LED, and the Apollo Automation app gives you two action cards to drive them. Add them under **Then...** from your BTN-1, the same way you add **Button pressed** under **When...**.

| Card | Asks for | What it does |
| --- | --- | --- |
| **Set button light color** | **Button light** (Button 1 to Button 4) and **Color** | Turns that button's LED on in the color you pick, at full brightness. |
| **Turn off button light** | **Button light** | Turns that button's LED off. |

Three ways to use them:

- **Show what's on**: in each **Click** flow, add **Set button light color** for the same button. In the matching **Hold** flow, add **Turn off button light**. Each LED now shows which devices you last turned on from the BTN-1.
- **Confirm the press type**: give each press type its own color, for example green for **Click** and blue for **Double click**, so you can see which press the BTN-1 registered.
- **A status light for the house**: the cards work in any flow, not only flows that start with a button press. Light Button 4 red when a door opens, and turn it off when the door closes.

Each LED also has its own on/off switch on the BTN-1 in Homey, labeled **LED 1** to **LED 4**.

## Put every press on one canvas

Separate flows are quick to build in the mobile app. If you'd rather see your whole BTN-1 in one place, build an Advanced Flow in the Homey web app instead. An Advanced Flow can hold several **When** cards: add one **Button pressed** card for each press in your plan, and draw a line from each one to its own **Then** cards. The [High CO2 notification example](../../../general/tutorials/high-co2-notification-example/) walks you through the Advanced Flow editor.

## Keep the BTN-1 awake

Double clicks, triple clicks, and holds only reach Homey while the BTN-1 is awake and connected.

!!! warning "A sleeping BTN-1 only reports clicks"

    The BTN-1 ships with **Prevent sleep** on, so it stays connected and reports every press. If you turn it off to save battery, the BTN-1 sleeps between presses. Homey receives the press that wakes it as a **Click** of that button, whatever press type you used, and only after the BTN-1 has reconnected, at least 5 seconds later. It then goes back to sleep.

    To use every press type, open the device in Homey, go to its **Settings**, and check **Prevent sleep** under **Battery settings (if battery is present)**. Homey can only change this setting while the BTN-1 is awake, so wake it first with its reset button. [How to wake up your sensor](../../battery-sensors/wake-up-battery-sensor/) shows where the reset button is and how to keep the BTN-1 awake, and [Prevent sleep](../../additional-info/prevent-sleep/) explains what each sleep setting does on the BTN-1.

## Troubleshooting

Most problems come down to press timing, a sleeping BTN-1, or a card pointing at the wrong device.

| Symptom | What to check |
| --- | --- |
| A flow never runs | Check that it is switched on in **My Flows** and that every Apollo card in it points at your BTN-1. The app offers the BTN-1 cards on every Apollo device, but only a BTN-1 has the buttons and LEDs. |
| The wrong flow runs, or none | Press the button and watch its **Button 1** to **Button 4** reading on the BTN-1 in Homey. It shows the last press type Homey received. |
| A double click runs your **Click** flow twice | Click faster. The two clicks must be less than half a second apart. |
| A triple click also runs your **Double click** flow | Click faster. The BTN-1 reports a double click once the button has been released for 0.2 seconds, so the third click has to come sooner than that. |
| A hold does nothing | Hold for 1 to 5 seconds. A press longer than a click but shorter than 1 second isn't reported, and neither is a press longer than 5 seconds. |
| Only clicks work, and they arrive several seconds late | The BTN-1 is sleeping. Turn on **Prevent sleep**, as described in [Keep the BTN-1 awake](#keep-the-btn-1-awake). |
