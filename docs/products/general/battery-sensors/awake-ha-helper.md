# How to keep your sensor awake using the Home Assistant Helper

1\. Select HA Settings<br><br>2\. Select Devices and Services<br>![](../../../assets/screenshot-2024-10-22-at-2-00-40-pm.png)<br><br>3\. Select Helpers<br><br>4\. Select Create Helper<br>![](../../../assets/screenshot-2024-10-22-at-2-02-07-pm.png)<br><br>5\. Select Toggle<br>![](../../../assets/screenshot-2024-10-22-at-2-07-53-pm.png)<br><br>6\. Under Name input: apollo\_ota\_mode<br>![](../../../assets/screenshot-2024-10-22-at-2-08-41-pm.png)<br><br>7\. Select desired icon such as "mdi:sleep-off"<br><br>8\. Select Create<br><br>9\. Toggle the OTA mode on as shown below.

![](../../../assets/toggle-ota-mode-on.png)

10\. Now when you reboot your device or when it wakes up on its wake timer, it will no longer go back to sleep. Warning: this will keep ALL of your apollo devices from sleeping. You might want to keep reading to create an automation to turn this helper off after one hour of it being on.

11\. Create a new automation and select "add trigger" then select entity then select state.

![](../../../assets/toggle-ota-mode-automation-1.png)

![](../../../assets/toggle-ota-mode-automation-2.png)

12\. Type in "apollo\_ota\_mode" in the box for entity and then select "On" and finally put a 1 in the hours box under "For". This is telling home assistant if the apollo\_ota\_mode is on for one hour then this trigger will fire (trigger).

![](../../../assets/toggle-ota-mode-automation-3.png)

13\. Scroll down to "Then do" and click "Add Action" and type in "input boolean" and choose the option that says "Input Boolean: Turn off".

![](../../../assets/toggle-ota-mode-automation-4.png)

14\. Now select choose entity and select apollo\_ota\_mode as shown below.

![](../../../assets/toggle-ota-mode-automation-5.png)

15\. Now you are done! You can toggle your OTA mode on and after one hour it will automatically be turned off for you!

&nbsp;