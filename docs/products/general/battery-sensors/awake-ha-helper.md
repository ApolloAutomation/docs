# How to keep your sensor awake using the Home Assistant Helper

1\. Open your Home Assistant dashboard and go to settings then select Devices and services and select helpers in the top right. <a href="http://homeassistant.local:8123/config/helpers" title="Open Helpers Page" target="_blank" rel="noopener">Or click here to go straight there</a>.

![](assets/awake-ha-helper-pic-1.png)

![](assets/awake-ha-helper-pic-2.png)

2\. Select Create Helper in the bottom right.<br>

![](assets/awake-ha-helper-pic-4.png)

<br>3\. Scroll down to the bottom and select Toggle.

![](assets/awake-ha-helper-pic-3-1.png)

<br>4\. For name use "apollo\_ota\_mode" and choose desired icon such as "mdi:sleep-off" then click Create.

![](assets/awake-ha-helper-pic-5.png)

5\. Search "apollo\_ota\_mode" and click on the helper shown.

![](assets/awake-ha-helper-pic-6.png)

<br>6\. Toggle the OTA mode on as shown below.

![](../../../assets/toggle-ota-mode-on.png)

7\. Now when you reboot your device or when it wakes up on its wake timer, it will no longer go back to sleep.

!!! null "Warning: This will keep ALL of your apollo devices from sleeping."

    Please keep reading to create an automation to turn this helper off after one hour of it being on.

8\. Create a new automation and select "add trigger" then select entity then select state.

![](../../../assets/toggle-ota-mode-automation-1.png)

![](../../../assets/toggle-ota-mode-automation-2.png)

9\. Type in "apollo\_ota\_mode" in the box for entity and then select "On" and finally put a 1 in the hours box under "For". This is telling home assistant if the apollo\_ota\_mode is on for one hour then this trigger will fire (trigger).

![](../../../assets/toggle-ota-mode-automation-3.png)

10\. Scroll down to "Then do" and click "Add Action" and type in "input boolean" and choose the option that says "Input Boolean: Turn off".

![](../../../assets/toggle-ota-mode-automation-4.png)

11\. Now select choose entity and select apollo\_ota\_mode as shown below.

![](../../../assets/toggle-ota-mode-automation-5.png)

12\. Now you are done! You can toggle your OTA mode on so that you can update your devices and after one hour it will automatically be turned off for you!

&nbsp;