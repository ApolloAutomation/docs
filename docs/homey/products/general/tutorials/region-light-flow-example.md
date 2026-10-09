---
title: Turn on a light when someone enters a region
description: Build a Homey flow that turns a light on when someone enters a Radar regions area on your MTR-1 or R PRO-1, and off again when they leave.
---

# Turn on a light when someone enters a region

<span class="difficulty lvl-1">Difficulty: Level 1</span>

Regions turn one radar into several spots you can automate on their own: the desk, the sofa, the workbench. In this guide you build two flows in the Homey mobile app. The first turns a light on the moment someone steps into a region; the second turns it off once the region has been empty for a while. The example uses a region called **Server** on an Apollo R PRO-1, and works the same way on an MTR-1 with any region you have drawn.

<!-- Video walkthrough goes here once recorded:
<video class="phone-media" src="/assets/homey-region-light-flow-walkthrough.mp4" poster="/assets/homey-region-light-flow-walkthrough-poster.jpg" controls muted playsinline preload="metadata"></video>
-->

!!! note "Before you start"

    - Draw at least one region with the Zone Mapper tool, set to **Detect people here**. See the guide for your [R PRO-1](../../../rpro1/setup/r-pro-1-zone-mapper-tool/) or [MTR-1](../../../mtr1/setup/mtr-1-zone-mapper-tool/).
    - Add the light you want to control to Homey.

## Why use the region trigger

Every detect region gives your sensor three flow cards: **A region became occupied**, **A region became empty**, and **A region is occupied**. Start your flow with **A region became occupied** and pick your region. It fires every time someone walks into that spot, even when someone else is already elsewhere in the room.

The sensor's whole-room card, **The occupancy alarm turned on**, only fires when the room goes from empty to occupied. Pairing it with a **Server is occupied** condition misses the moment someone who is already in the room walks over to the server, so the light stays off.

## Flow 1: turn the light on

This flow has one trigger and one action, so it needs no **And** card.

1. In the Homey mobile app, tap **Flow** in the bottom bar, then tap **+** at the top right (or **Create a Flow** if you have none yet).
2. Under **When...**, tap **Add Card**. Open **Apollo Automation** under **Apps**, and choose your sensor.
3. Choose the card **A region became occupied**.
4. Tap **Region** and pick **Server**, then tap the check mark at the top right.
5. Under **Then...**, tap **Add Card**. Find your light under **Zones & Devices**, choose **Turn on**, and tap the check mark.
6. Tap **Next**. Name the flow, for example **Server area light on**, and tap **Save Flow**.

<!-- Clip goes here once recorded:
<video class="phone-media" src="/assets/homey-region-light-flow-on.mp4" autoplay loop muted playsinline></video>
-->

The flow now shows in **My Flows**. Walk into the region and the light turns on.

!!! tip "Only detect regions are listed"

    The region picker lists your **Detect people here** regions. Areas set to **Ignore this area** never report occupied, so they don't appear.

## Flow 2: turn the light off

The second flow mirrors the first. Build it the same way, with two changes:

1. Under **When...**, choose **A region became empty** and pick **Server**.
2. Under **Then...**, choose **Turn off** for the same light.
3. Name it **Server area light off** and tap **Save Flow**.

Now the light follows the region: on when someone arrives, off when they leave.

## Set the hold time

A region stays occupied for its **Hold time** after the last person leaves, 5 seconds by default. That is what stops the light from flickering off when someone leans back or steps away for a moment.

For a desk or a workbench, raise it. Open the dashboard with your **Radar regions** widget, tap the region with **Select** active, and set **Hold time** under **More** to 60 seconds or longer. Press **Save**. Flow 2 now waits that long before it turns the light off.

## Test your flows

Run the flows end to end by walking in and out of the region while you watch the light. To check a single flow without moving, tap the play button next to it in **My Flows**; it runs its **Then** cards once, and a green check mark confirms it ran.

If a flow doesn't fire:

- Open the **Radar regions** widget and watch the dots. If your dot doesn't land inside the region, make the region larger with **Bigger** or the arrows.
- Check that the region is set to **Detect people here** and is **Enabled**.
- Check that both flows are switched on in **My Flows**.

## Take it further

- **One flow for many regions**: pick **Any region** in the trigger instead of a single region. The **Region name** token tells the flow which one fired, for example in a notification.
- **Count people**: **A region became occupied** also passes a **Target count** token, the number of people in the region.
- **Keep other automations in check**: add **A region is occupied** as an **And** condition. For example, add **Sofa** is not occupied (with **Invert** on) to the flow that turns your living room lights off.

See [Use regions in flows](../../../rpro1/setup/r-pro-1-zone-mapper-tool/#use-regions-in-flows) for the full list of region cards.
