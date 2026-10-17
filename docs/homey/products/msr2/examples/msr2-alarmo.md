---
title: MSR-2 + Alarmo Home Security Install
description: "Use the Alarmo integration in Home Assistant to turn your MSR-2 into a local alarm that notifies your phone and turns on your sensors' RGB lights."
---
# MSR-2 + Alarmo home security install

My grandmother wanted a security system that would alert her when there was movement in her home after she had gone to bed. So, I set up three of our Apollo Automation mmWave sensors. With the Alarmo integration, they quickly became a fully local, private security system: no cloud and no monthly subscription. She can arm and disarm it with one button on her Home Assistant dashboard, and it makes her feel much safer.

This guide shows you how to build the same system with your Apollo MSR-2. Alarmo watches your sensors and, when the alarm is triggered, sends a notification to your phone and turns on your sensors' RGB lights.

!!! note "Before you start"

    - This guide is for Home Assistant, not Homey. HACS, Alarmo, and the Alarmo Card all run in Home Assistant.
    - You need a motion or presence sensor, such as your MSR-2, already set up in Home Assistant.

1\. Install [HACS](https://hacs.xyz/docs/use/download/download/).

2\. Install [Alarmo](https://github.com/nielsfaber/alarmo?tab=readme-ov-file#installation) and the [Alarmo Card](https://github.com/nielsfaber/alarmo-card). The card puts arm and disarm buttons on your Home Assistant dashboard, as in the first screenshot below. The second shows Alarmo's **General** tab, with its global alarm settings and arm modes.

![Alarmo card on a Home Assistant dashboard showing Disarmed with Arm Away and Arm Home buttons](/assets/alarmo-7.png)

![Alarmo General tab in Home Assistant with global alarm settings and arm modes, Armed home enabled](/assets/alarmo-1.png)

3\. Find **Alarmo** in the sidebar on the left, select the **Sensors** tab, and turn on the sensor entities you want to use for your alarm system.

![Alarmo Sensors tab with MSR-1 radar target entities toggled on for Home arm mode](/assets/alarmo-2.png)

*Shown with MSR-1 sensors; add your MSR-2 radar target entities the same way.*

4\. Select the **Actions** tab. Under **Condition → Event**, select **Alarm is triggered**. Then, under **Task → Target → Select Device**, choose the device you want the notification on, such as your phone or tablet.

![Alarmo notification setup with Event set to Alarm is triggered and Target set to a phone](/assets/alarmo-3.png)

5\. Change the **Title**, **Message**, and **Name** of the alarm notification if you like, then save the action.

![Alarmo notification Title, Message, and Name fields filled in for a movement alert](/assets/alarmo-4.png)

6\. Add a second action that turns on your sensors' RGB lights. Under **Entity**, select your sensor's RGB light. (An action like this can also make the sensors' onboard piezo buzzers play an alarm sound; this guide sets up the lights.)

![Alarmo action setup for Alarm is triggered with AIR-1 and MSR-1 RGB light entities selected](/assets/alarmo-5.png)

*Shown with AIR-1 and MSR-1 lights; pick your MSR-2 RGB light the same way.*

7\. Under **Action**, select **Turn On**.

![Alarmo action with the RGB light entities selected and Turn On chosen as the action](/assets/alarmo-6.png)

*Shown with AIR-1 and MSR-1 lights; the MSR-2 steps are the same.*

And that's it! When the alarm is triggered, your sensors' RGB lights turn on and the notification goes to your phone. Enjoy your free and local security system.

We hope this was helpful. Please let us know if you have any questions!
