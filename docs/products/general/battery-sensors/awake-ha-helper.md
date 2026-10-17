---
title: Apollo Battery Devices - Awake HA Helper
description: Create a Home Assistant toggle that keeps your Apollo battery devices awake for updates, plus an automation that turns it off after one hour.
---
# Keep your sensor awake with a Home Assistant helper

When an `apollo_ota_mode` toggle in Home Assistant is on, your Apollo battery devices stay awake so you can update them. In this guide you create that toggle, then add an automation that turns it off again after one hour.

!!! warning "This keeps every Apollo device awake"

    While `apollo_ota_mode` is on, none of your Apollo devices go back to sleep. Finish the second part of this guide to create an automation that turns the helper off after it has been on for one hour.

## Create the OTA mode toggle

Start by creating the toggle helper and switching it on.

1\. Go to **Settings → Devices & services** and select the **Helpers** tab at the top. Or use the button below to go straight there.

[![Open your Home Assistant instance and show your helper entities.](https://my.home-assistant.io/badges/helpers.svg)](https://my.home-assistant.io/redirect/helpers/)

![Home Assistant Settings with the cursor on Devices and services](/assets/awake-ha-helper-pic-1.png)

![Helpers tab selected at the top of the Devices and services page](/assets/awake-ha-helper-pic-2.png)

2\. Select **Create helper** in the bottom right.

![Create Helper button in the bottom right of the Helpers page](/assets/awake-ha-helper-pic-4.png)

3\. Scroll to the bottom of the list and select **Toggle**.

![Create helper list in Home Assistant with the cursor on Toggle](/assets/awake-ha-helper-pic-3-1.png)

4\. Name the toggle `apollo_ota_mode`, choose an icon such as `mdi:sleep-off`, and click **Create**.

![Create Toggle dialog with name apollo_ota_mode, icon mdi:sleep-off, and the Create button](/assets/awake-ha-helper-pic-5.png)

5\. Search the helpers list for `apollo_ota_mode` and click the helper that appears.

![Helpers list searched for apollo_ota_mode showing the input_boolean helper](/assets/awake-ha-helper-pic-6.png)

6\. Switch the toggle on.

![apollo_ota_mode helper dialog with the toggle switched On](/assets/toggle-ota-mode-on.png)

OTA mode is now on. The next time your Apollo device reboots or wakes up on its wake timer, it stays awake instead of going back to sleep.

## Turn OTA mode off after one hour

Next, create an automation that switches `apollo_ota_mode` off once it has been on for one hour, so you never leave your devices awake by accident.

1\. Go to **Settings → Automations & scenes** and click **Create automation**.

[![Open your Home Assistant instance and show your automations.](https://my.home-assistant.io/badges/automations.svg)](https://my.home-assistant.io/redirect/automations/)

2\. Click **Add trigger**, then select **Entity**.

![New automation with Add trigger and the Entity trigger option circled in red](/assets/toggle-ota-mode-automation-1.png)

3\. Select **State**.

![Entity trigger list with the State option circled in red](/assets/toggle-ota-mode-automation-2.png)

4\. In the **Entity** box, enter `apollo_ota_mode`. Set **To** to **On**, and enter 1 in the hours box under **For**. This trigger fires once `apollo_ota_mode` has been on for one hour.

![State trigger set to apollo_ota_mode, To On, and For 1 hour, circled in red](/assets/toggle-ota-mode-automation-3.png)

5\. Scroll down to **Then do**, click **Add action**, search for `input boolean`, and choose **Input boolean: Turn off**.

![Add action search for input boolean with Input boolean: Turn off circled in red](/assets/toggle-ota-mode-automation-4.png)

6\. Click **Choose entity** and select `apollo_ota_mode`.

![Input boolean Turn off action targeting the apollo_ota_mode entity](/assets/toggle-ota-mode-automation-5.png)

You're done. Turn `apollo_ota_mode` on whenever you want to update your devices, and the automation turns it off for you after one hour.
