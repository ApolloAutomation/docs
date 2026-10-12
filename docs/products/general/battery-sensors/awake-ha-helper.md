---
title: Apollo Battery Devices - Awake HA Helper
description: How to keep your sensor awake using the Home Assistant Helper.
---
# How to keep your sensor awake using the Home Assistant Helper

1\. Open your Home Assistant dashboard and go to settings then select Devices and services and select helpers in the top right. <a href="http://homeassistant.local:8123/config/helpers" title="Open Helpers Page" target="_blank" rel="noopener">Or click here to go straight there</a>.

![Home Assistant Settings with the cursor on Devices and services](/assets/awake-ha-helper-pic-1.png)

![Helpers tab selected at the top of the Devices and services page](/assets/awake-ha-helper-pic-2.png)

2\. Select Create Helper in the bottom right.<br>

![Create Helper button in the bottom right of the Helpers page](/assets/awake-ha-helper-pic-4.png)

<br>3\. Scroll down to the bottom and select Toggle.

![Create helper list in Home Assistant with the cursor on Toggle](/assets/awake-ha-helper-pic-3-1.png)

<br>4\. For name use "apollo\_ota\_mode" and choose desired icon such as "mdi:sleep-off" then click Create.

![Create Toggle dialog with name apollo_ota_mode, icon mdi:sleep-off, and the Create button](/assets/awake-ha-helper-pic-5.png)

5\. Search "apollo\_ota\_mode" and click on the helper shown.

![Helpers list searched for apollo_ota_mode showing the input_boolean helper](/assets/awake-ha-helper-pic-6.png)

<br>6\. Toggle the OTA mode on as shown below.

![apollo_ota_mode helper dialog with the toggle switched On](/assets/toggle-ota-mode-on.png)

7\. Now when you reboot your Apollo device or when it wakes up on its wake timer, it will no longer go back to sleep.

!!! null "Warning: This will keep ALL of your Apollo devices from sleeping."

    Please keep reading to create an automation to turn this helper off after one hour of it being on.

8\. Create a new automation and select "add trigger" then select entity then select state.

![New automation with Add trigger and the Entity trigger option circled in red](/assets/toggle-ota-mode-automation-1.png)

![Entity trigger list with the State option circled in red](/assets/toggle-ota-mode-automation-2.png)

9\. Type in "apollo\_ota\_mode" in the box for entity and then select "On" and finally put a 1 in the hours box under "For". This is telling Home Assistant if the apollo\_ota\_mode is on for one hour then this trigger will fire (trigger).

![State trigger set to apollo_ota_mode, To On, and For 1 hour, circled in red](/assets/toggle-ota-mode-automation-3.png)

10\. Scroll down to "Then do" and click "Add Action" and type in "input boolean" and choose the option that says "Input Boolean: Turn off".

![Add action search for input boolean with Input boolean: Turn off circled in red](/assets/toggle-ota-mode-automation-4.png)

11\. Now select choose entity and select apollo\_ota\_mode as shown below.

![Input boolean Turn off action targeting the apollo_ota_mode entity](/assets/toggle-ota-mode-automation-5.png)

12\. Now you are done! You can toggle your OTA mode on so that you can update your devices and after one hour it will automatically be turned off for you!

&nbsp;