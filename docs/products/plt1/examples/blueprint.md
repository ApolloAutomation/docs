---
title: PLT-1 Plant Sensor Alerts Blueprint
description: >-
  Example of how to use the PLT-1 Plant Sensor Alerts Blueprint in
  Home Assistant to receive notifications when your plant needs attention!
---
# Blueprint Setup

### Automatic Import

1\. Click the Import Blueprint button below and then click **Open link**.

<a href="https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FApolloAutomation%2FBlueprints%2Frefs%2Fheads%2Fmain%2FPLT-1%2FPLT-1.yaml" target="_blank" rel="noreferrer noopener">     <img alt="Import Blueprint" src="https://my.home-assistant.io/badges/blueprint_import.svg" />   </a>

2\. Click **Preview** then click **Import blueprint**.

![](/assets/btn-1-blueprint-auto-import.gif)

3\. Click on **Apollo Automation PLT-1 Blueprint** and click on **Select a device** then choose your **Apollo PLT-1** or **PLT-1B** from the dropdown menu.

![](/assets/btn-1-blueprint-select-btn-1.gif)

4\. Enter your **plant's name** (this appears in notification messages), then select your **mobile device** for push notifications.

5\. Enable the sensor groups you want to monitor (e.g. Soil Moisture, Air Temperature, Light Intensity) and adjust the thresholds to suit your plant.

![](/assets/btn-1-blueprint-single-click-example.gif)

!!! success "Each sensor group is disabled by default — enable only what matters!"

    Soil Moisture alerts are enabled out of the box. Expand any sensor group, toggle it on, and set your preferred min/max thresholds. You can also configure an Alert Delay to avoid false alerts from brief fluctuations.

6\. Click **Save**. Your blueprint is now live and will send push notifications whenever your plant needs attention!

### Manual Import

1\. Head to the <a href="http://homeassistant.local:8123/config/automation/dashboard" target="_blank" rel="noreferrer nofollow noopener">automations page</a> and click on **Blueprints** in the top right then select **Import Blueprint**.

![](/assets/btn-1-blueprint-manual-import.gif)

2\. Copy <a href="https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FApolloAutomation%2FBlueprints%2Frefs%2Fheads%2Fmain%2FPLT-1%2FPLT-1.yaml" target="_blank" rel="noreferrer nofollow noopener">this link</a> and paste it into the **Blueprint address** box and click **Preview** then click **Import blueprint**.

![](/assets/btn-1-blueprint-auto-import.gif)

3\. Click on **Apollo Automation PLT-1 Blueprint** and click on **Select a device** then choose your **Apollo PLT-1** or **PLT-1B** from the dropdown menu.

![](/assets/btn-1-blueprint-select-btn-1.gif)

4\. Enter your **plant's name**, select your **mobile device**, enable the sensor groups you want, and set your thresholds.

![](/assets/btn-1-blueprint-single-click-example.gif)

!!! success "Each sensor group is disabled by default — enable only what matters!"

    Soil Moisture alerts are enabled out of the box. Expand any sensor group, toggle it on, and set your preferred min/max thresholds. You can also configure an Alert Delay to avoid false alerts from brief fluctuations.

5\. Click **Save**. Your blueprint is now live and will send push notifications whenever your plant needs attention!
