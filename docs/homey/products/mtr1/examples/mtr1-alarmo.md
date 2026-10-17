---
title: MTR-1 + Alarmo home security install
description: "Build a fully local home security system with no monthly subscription, using the Apollo MTR-1 and the Alarmo integration for Home Assistant."
---
# MTR-1 + Alarmo home security install

My grandmother wanted a security system that would alert her when there was movement in her home after she had gone to bed. So I set up three of our Apollo Automation mmWave sensors with the Alarmo integration. Together, they quickly gave her a fully local, private, cloud-free security system with no monthly subscription. She can arm and disarm it with one button on her Home Assistant dashboard, and it makes her feel much safer.

This guide shows you how to build the same system with your Apollo MTR-1.

!!! note "Before you start"

    This guide is for Home Assistant. Alarmo is a Home Assistant integration, so these steps don't apply to Homey. You need a motion or presence sensor, such as your MTR-1, already set up in Home Assistant.

Follow these steps to install Alarmo, choose the sensors that trigger your alarm, and decide what happens when it goes off.

1\. Install [HACS](https://hacs.xyz/docs/use/download/download/).

2\. Install [Alarmo](https://github.com/nielsfaber/alarmo?tab=readme-ov-file#installation) and the [Alarmo Card](https://github.com/nielsfaber/alarmo-card). The Alarmo Card adds a good-looking arm and disarm card to your Home Assistant dashboard.

![Alarmo Card on a dashboard showing Disarmed with Arm Away and Arm Home buttons](/assets/alarmo-7.png)

![Alarmo alarm panel General tab in Home Assistant listing the arm modes](/assets/alarmo-1.png)

3\. Open **Alarmo** from the sidebar on the left, select the **Sensors** tab, and turn on the sensor entities you want your alarm system to use.

![Alarmo Sensors tab with MSR-1 radar target entities enabled for Home mode](/assets/alarmo-2.png)

*Shown with MSR-1 sensors; add your MTR-1 target entities the same way.*

4\. Select the **Actions** tab. Under **Condition → Event**, select **Alarm is triggered**. To choose which device gets the notification, such as your phone or tablet, select it under **Task → Target**.

![Alarmo notification action with the Alarm is triggered event and a phone as the target](/assets/alarmo-3.png)

5\. Optionally, change the **Title**, **Message**, and **Name** of the alarm notification.

![Alarmo notification Title, Message, and Name fields filled in for the alarm alert](/assets/alarmo-4.png)

6\. Save that action, then add another one. A second action can turn on your sensors' lights, make their onboard piezo buzzers play an alarm sound, or both. This guide sets up the lights: under **Entity**, select your sensors' RGB light.

![Alarmo action for Alarm is triggered with Apollo sensor RGB light entities selected](/assets/alarmo-5.png)

*Shown with AIR-1 and MSR-1 lights; pick your MTR-1 RGB light the same way.*

7\. Under **Action**, select **Turn On**. Your sensors' RGB lights now turn on whenever the alarm is triggered.

![Alarmo action with Turn On selected for the Apollo sensor RGB light entities](/assets/alarmo-6.png)

*Shown with AIR-1 and MSR-1 lights; the MTR-1 steps are the same.*

That's it, seriously. You now have a free, local security system that sends you an alert and lights up your sensors when the alarm is triggered.

We hope this was helpful. If you have any questions, please let us know!
