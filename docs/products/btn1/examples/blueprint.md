---
title: BTN-1 4 Event Blueprint
description: >-
  Example of how to use the BTN-1 Events with the BTN-1 4 Event Blueprint in
  Home Assistant!
---
# Blueprint Setup

## Automatic Import

1\. Click the Import Blueprint button below and then click **Open link**.

<a href="https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FApolloAutomation%2FBlueprints%2Frefs%2Fheads%2Fmain%2FBTN-1%2FBTN-1.yaml" target="_blank" rel="noreferrer noopener">     <img alt="Import Blueprint" src="https://my.home-assistant.io/badges/blueprint_import.svg" />   </a>

2\. Click **Preview** then click **Import blueprint**.

![Home Assistant Import a blueprint dialog for the BTN-1 blueprint, clicking Preview then Import blueprint](/assets/btn-1-blueprint-auto-import.gif)

3\. Click on **Apollo Automation BTN-1 Blueprint** and click on **Select a device** then choose your **Apollo BTN-1** from the dropdown menu.

![Choosing an Apollo BTN-1 from the Select a device dropdown in the BTN-1 blueprint](/assets/btn-1-blueprint-select-btn-1.gif)

4\. For the **Single Click** event, click **Add Action**, then search for **Light: Toggle** and select it. Next, choose the entity you want to control, such as **BTN-1 Light**, and click **Save**. Name your automation something like **Apollo BTN-1 Blueprint**. You can repeat this process for **Double Click**, **Triple Click**, and **Hold** events.

![Adding a Light Toggle action to Button 1 Single Click in the BTN-1 blueprint, then saving it](/assets/btn-1-blueprint-single-click-example.gif)

!!! success "You can do this for all four buttons all in one blueprint!"

    This blueprint is packed with features - you can do a Single Click, a Double Click, Three Clicks, or a Hold on each of the four buttons. Just click Add action and set them all up!

5\. Your blueprint is now live. Click the button 1 button and it should toggle whatever light you selected in the blueprint. This can be anything in Home Assistant such as your light, fan, scene, etc!

## Manual Import

1\. Go to **Settings → Automations & scenes**, click **Blueprints** at the top, then click **Import blueprint**.

![Opening the Home Assistant Blueprints tab under Automations and scenes and clicking Import blueprint](/assets/btn-1-blueprint-manual-import.gif)

2\. Copy the address below, paste it into the **Blueprint address** box, and click **Preview** then click **Import blueprint**.

```text
https://raw.githubusercontent.com/ApolloAutomation/Blueprints/refs/heads/main/BTN-1/BTN-1.yaml
```

![Home Assistant Import a blueprint dialog for the BTN-1 blueprint, clicking Preview then Import blueprint](/assets/btn-1-blueprint-auto-import.gif)

3\. Click on **Apollo Automation BTN-1 Blueprint** and click on **Select a device** then choose your **Apollo BTN-1** from the dropdown menu.

![Choosing an Apollo BTN-1 from the Select a device dropdown in the BTN-1 blueprint](/assets/btn-1-blueprint-select-btn-1.gif)

3\. For the **Single Click** event, click **Add Action**, then search for **Light: Toggle** and select it. Next, choose the entity you want to control, such as **BTN-1 Light**, and click **Save**. Name your automation something like **Apollo BTN-1 Blueprint**. You can repeat this process for **Double Click**, **Triple Click**, and **Hold** events.

![Adding a Light Toggle action to Button 1 Single Click in the BTN-1 blueprint, then saving it](/assets/btn-1-blueprint-single-click-example.gif)

!!! success "You can do this for all four buttons all in one blueprint!"

    This blueprint is packed with features - you can do a Single Click, a Double Click, Three Clicks, or a Hold on each of the four buttons. Just click Add action and set them all up!

4\. Your blueprint is now live. Click the button 1 button and it should toggle whatever light you selected in the blueprint. This can be anything in Home Assistant such as your light, fan, scene, etc.