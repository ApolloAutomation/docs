---
title: MTR-1 Alarmo setup
description: MTR-1 Alarmo setup
---
# MTR-1 + Alarmo Home Security Install

My grandmother wanted a security system that would alert her when there was movement in her home after she had gone to bed. So, I set up three of our Apollo Automation mmWave sensors. These devices, plus the Alarmo integration, quickly allowed me to install a fully local, private, cloud-free, and no monthly subscription security system. She can arm/disarm it with one button on her Home Assistant dashboard, and it makes her feel much safer. This guide assumes you already have a motion/presence sensor installed on HA.

1\. Install [HACS](https://hacs.xyz/docs/use/download/download/)  
2\. Install [Alarmo](https://github.com/nielsfaber/alarmo?tab=readme-ov-file#installation) and the [Alarmo Card](https://github.com/nielsfaber/alarmo-card) (Pretty Arm and Disarm card for your HA dashboard)  

The first button opens Alarmo in HACS and the second opens the Alarmo Card:

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=nielsfaber&repository=alarmo&category=integration)

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=nielsfaber&repository=alarmo-card&category=plugin)

Restart Home Assistant once both are installed, then add the Alarmo integration under **Settings → Devices & services → Add integration**. Alarmo shows up in the sidebar after that.

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=alarmo)
  
![Alarmo Card on a Home Assistant dashboard showing Disarmed with Arm Away and Arm Home buttons](/assets/alarmo-7.png)  
  
![Alarmo panel General tab in Home Assistant with the arm modes list, Armed home enabled](/assets/alarmo-1.png)  
  
3\. Find Alarmo on the left, select the Sensors tab, and toggle on the sensor entities that you would like to use for your alarm system.  
  
![Alarmo Sensors tab with MSR-1 radar target entities toggled on for Home arm mode](/assets/alarmo-2.png)  
  
*Shown with MSR-1 sensors; add your MTR-1 target entities the same way.*
  
4\. Now select the Actions tab and under Condition > Event > Select "Alarm is triggered". You can also select the device you would like to receive a notification on under Task > Target > Select Device (Phone, tablet, etc.)  
  
![Alarmo Configure notification with the Alarm is triggered event and a phone selected as target](/assets/alarmo-3.png)  
  
5\. You can change the Title, Message, and Name of the alarm notification.  
  
![Alarmo notification settings with the Title, Message, and Name fields filled in](/assets/alarmo-4.png)  
  
6\. After saving that action we can add another one that will turn on our sensor lights and/or make the onboard piezo buzzers play an alarm sound. Under Entity select your sensors' RGB light.  
  
![Alarmo Configure action with Alarm is triggered and AIR-1 and MSR-1 RGB light entities selected](/assets/alarmo-5.png)  
  
*Shown with AIR-1 and MSR-1 lights; pick your MTR-1 RGB light the same way.*
  
7\. Under Action select Turn On and now your sensors' RGB lights will turn on when the alarm is triggered.  
  
![Alarmo action Task with Turn On selected for the RGB lights and the action named](/assets/alarmo-6.png)  
  
*Shown with AIR-1 and MSR-1 lights; the MTR-1 steps are the same.*
  
8\. And that's it, seriously... Now you can enjoy a free and local security system.  
  
We hope this was helpful and please let us know if there are any questions!