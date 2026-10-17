---
title: Removing Device From Home Assistant
description: Tutorial for Removing Device From Home Assistant.
---
# Removing Device From Home Assistant

## ESPHome app

This will cover how to remove an Apollo device from Home Assistant

!!! tip "Skip this step unless you took control of your device with the ESPHome Device Builder app!"

    This step is only necessary for advanced users who added the device to the ESPHome device builder to edit the yaml and customize the device. Please skip to the next step if you are only using the ESPHome or Apollo Automation integration!

1\. Navigate to Home Assistant and open your **ESPHome Device Builder** app.

[![Open your Home Assistant instance and show the dashboard of an app.](https://my.home-assistant.io/badges/supervisor_app.svg)](https://my.home-assistant.io/redirect/supervisor_app/?app=5c53de3b_esphome&repository_url=https%3A%2F%2Fgithub.com%2Fesphome%2Fhome-assistant-addon)

![ESPHome Builder selected in the Home Assistant sidebar, showing the ESPHome Device Builder dashboard](/assets/esphome-device-builder-addon-image.png)

2\. On the device you would like to remove, click the three dots and select "Delete" then click Delete to confirm.

![Deleting an H-1 in ESPHome Device Builder from the three-dot menu and confirming Delete](/assets/delete-device-from-esphome-device-builder-gif.gif)

## ESPHome Integration

1\. Head to the **ESPHome** integration page (**Settings → Devices & services → ESPHome**). Next to the device you would like to remove, click the three dots and then "Delete".

[![Open your Home Assistant instance and show an integration.](https://my.home-assistant.io/badges/integration.svg)](https://my.home-assistant.io/redirect/integration/?domain=esphome)

![Deleting an H-1 from the ESPHome integration page in Home Assistant and confirming Delete](/assets/delete-device-from-esphome-integration-gif.gif)