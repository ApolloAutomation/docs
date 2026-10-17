---
title: MSR-1 and Alarmo home security
description: "Build a fully local home security system in Home Assistant from MSR-1 sensors and Alarmo, installed through HACS, with phone alerts and sensor lights that turn on when the alarm is triggered."
---
# MSR-1 and Alarmo home security

This setup started with a grandmother who wanted an alert if anything moved in her home after she had gone to bed. Three Apollo MSR-1 mmWave sensors and the Alarmo integration gave her a fully local, private, cloud-free security system with no monthly subscription, and she arms and disarms it with one button on her Home Assistant dashboard. Follow the steps below to build the same system in your home.

!!! note "Before you start"

    Your MSR-1, or another motion or presence sensor, is already set up in Home Assistant. If it isn't, follow the [MSR-1 getting started guide](../../../general/setup/getting-started-msr1/) first.

## Install Alarmo

Alarmo runs the alarm system itself, and the Alarmo Card puts arm and disarm buttons on your dashboard. Both install through HACS.

1\. Install [HACS](https://hacs.xyz/docs/use/download/download/) if you don't have it yet.

2\. Install [Alarmo](https://github.com/nielsfaber/alarmo?tab=readme-ov-file#installation) and the [Alarmo Card](https://github.com/nielsfaber/alarmo-card). The first button below opens Alarmo in HACS, and the second opens the Alarmo Card:

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=nielsfaber&repository=alarmo&category=integration)

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=nielsfaber&repository=alarmo-card&category=plugin)

3\. Restart Home Assistant once both are installed. The power icon is under **Settings → System**.

[![Open your Home Assistant instance and show the system dashboard.](https://my.home-assistant.io/badges/system_dashboard.svg)](https://my.home-assistant.io/redirect/system_dashboard/)

4\. Add the Alarmo integration under **Settings → Devices & services → Add integration**. Alarmo shows up in the sidebar after that.

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=alarmo)

5\. Add the Alarmo Card to a dashboard: open the dashboard, click **Edit dashboard**, click **Add card**, choose **Custom: Alarmo Card**, and pick your Alarmo entity. The card shows the alarm state and the buttons to arm and disarm it.

![Alarmo card on a Home Assistant dashboard showing Disarmed with Arm Away and Arm Home buttons](/assets/alarmo-7.png)

Alarmo is installed and ready to configure:

![Alarmo alarm panel General tab in Home Assistant, with Alarmo listed in the sidebar](/assets/alarmo-1.png)

## Set up your alarm

Now choose which sensors trigger the alarm and what happens when they do: a notification on your phone, and your sensors' RGB lights turning on.

1\. Open **Alarmo** from the sidebar, select the **Sensors** tab, and toggle on the sensor entities you want your alarm system to use.

![Alarmo Sensors tab with MSR-1 radar target entities enabled for the Home arm mode](/assets/alarmo-2.png)

2\. Select the **Actions** tab to set up a notification. Under **Condition → Event**, select **Alarm is triggered**. Under **Task → Target**, select the device that should get the notification, such as your phone or tablet.

![Alarmo Configure notification screen with the Alarm is triggered event and a phone as the target](/assets/alarmo-3.png)

3\. Change the **Title**, **Message**, and **Name** of the notification if you like, then save it.

![Alarmo notification settings with the Movement Detected title, alarm message, and notification name](/assets/alarmo-4.png)

4\. Add a second action, for the same **Alarm is triggered** event, to turn on your sensor lights. Under **Entity**, select each sensor's RGB light.

![Alarmo Configure action screen with the Alarm is triggered event and AIR-1 and MSR-1 RGB lights selected](/assets/alarmo-5.png)

5\. Under **Action**, select **Turn On**. Your sensors' RGB lights now turn on when the alarm is triggered.

![Alarmo action with Turn On selected for the AIR-1 and MSR-1 RGB light entities](/assets/alarmo-6.png)

That's it. You now have a free, local security system that you arm and disarm from your dashboard.

!!! tip "Add an alarm sound"

    The second action can also make the onboard piezo buzzer on each MSR-1 play an alarm sound. To learn how to play a tune on the buzzer, see [Using the MSR-1 buzzer](../using-msr-1-buzzer/).

We hope this was helpful. If you have any questions, let us know!
