---
title: PLT-1 Plant Sensor Alerts Blueprint
description: >-
  Example of how to use the PLT-1 Plant Sensor Alerts Blueprint in
  Home Assistant to receive notifications when your plant needs attention!
---
# Blueprint Setup

## Automatic Import

1\. Click the Import Blueprint button below and then click **Open link**.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FApolloAutomation%2FBlueprints%2Frefs%2Fheads%2Fmain%2FPLT-1%2FPLT-1.yaml)

2\. Click **Preview** then click **Import blueprint**.

![Home Assistant Import a blueprint dialog, clicking Preview then Import blueprint (BTN-1 example shown)](/assets/btn-1-blueprint-auto-import.gif)

3\. Click on **Apollo Automation PLT-1 Blueprint** and click on **Select a device** then choose your **Apollo PLT-1** or **PLT-1B** from the dropdown menu.

![Home Assistant blueprint editor, picking an Apollo device from Select a device (BTN-1 example shown)](/assets/btn-1-blueprint-select-btn-1.gif)

4\. Enter your **plant's name** (this appears in notification messages), then select your **mobile device** for push notifications.

5\. Enable the sensor groups you want to monitor (e.g. Soil Moisture, Air Temperature, Light Intensity) and adjust the thresholds to suit your plant.

![Home Assistant blueprint editor adding a light toggle action and saving (BTN-1 example shown)](/assets/btn-1-blueprint-single-click-example.gif)

!!! success "Each sensor group is disabled by default — enable only what matters!"

    Soil Moisture alerts are enabled out of the box. Expand any sensor group, toggle it on, and set your preferred min/max thresholds. Expand **Repeat Alerts** to control how often you are reminded while a condition lasts.

6\. *(Optional)* Expand **RGB LED Indicator** and set **LED Mode** so the sensor's own LED lights up when the soil gets too dry. (1)
{ .annotate }

1.  Both the PLT-1 and the PLT-1B ship with [Prevent Sleep](/products/plt1/additional-info/prevent-sleep.md) turned on, so **Stay On Until Watered** works out of the box and holds the LED until you water the plant. If you turn Prevent Sleep off to save battery, the LED goes dark every time the sensor sleeps, so choose **Flash On Alert** instead.

7\. Click **Save**. Your blueprint is now live and will send push notifications whenever your plant needs attention!

## Manual Import

1\. Head to the <a href="http://homeassistant.local:8123/config/automation/dashboard" target="_blank" rel="noreferrer nofollow noopener">automations page</a> and click on **Blueprints** in the top right then select **Import Blueprint**.

![Home Assistant Settings, Automations and scenes, Blueprints tab, then the Import blueprint button](/assets/btn-1-blueprint-manual-import.gif)

2\. Copy the address below, paste it into the **Blueprint address** box, and click **Preview** then click **Import blueprint**.

```text
https://raw.githubusercontent.com/ApolloAutomation/Blueprints/refs/heads/main/PLT-1/PLT-1.yaml
```

![Home Assistant Import a blueprint dialog, clicking Preview then Import blueprint (BTN-1 example shown)](/assets/btn-1-blueprint-auto-import.gif)

3\. Click on **Apollo Automation PLT-1 Blueprint** and click on **Select a device** then choose your **Apollo PLT-1** or **PLT-1B** from the dropdown menu.

![Home Assistant blueprint editor, picking an Apollo device from Select a device (BTN-1 example shown)](/assets/btn-1-blueprint-select-btn-1.gif)

4\. Enter your **plant's name**, select your **mobile device**, enable the sensor groups you want, and set your thresholds.

![Home Assistant blueprint editor adding a light toggle action and saving (BTN-1 example shown)](/assets/btn-1-blueprint-single-click-example.gif)

!!! success "Each sensor group is disabled by default — enable only what matters!"

    Soil Moisture alerts are enabled out of the box. Expand any sensor group, toggle it on, and set your preferred min/max thresholds. Expand **Repeat Alerts** to control how often you are reminded while a condition lasts.

5\. *(Optional)* Expand **RGB LED Indicator** and set **LED Mode** so the sensor's own LED lights up when the soil gets too dry. (1)
{ .annotate }

1.  Both the PLT-1 and the PLT-1B ship with [Prevent Sleep](/products/plt1/additional-info/prevent-sleep.md) turned on, so **Stay On Until Watered** works out of the box and holds the LED until you water the plant. If you turn Prevent Sleep off to save battery, the LED goes dark every time the sensor sleeps, so choose **Flash On Alert** instead.

6\. Click **Save**. Your blueprint is now live and will send push notifications whenever your plant needs attention!
