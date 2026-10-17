---
title: Adding Apollo Devices To Hidden Networks
description: Tutorial for how to add Apollo Devices To Hidden Networks.
---
# Adding Apollo Devices To Hidden Networks

1\. Open the ESPHome Device Builder.

![ESPHome Device Builder dashboard listing Apollo devices](/assets/bluetooth-proxy-tutorial-1.png)

2\. If you do not have it installed, [install the standalone ESPHome Device Builder](https://esphome.io/guides/installing_esphome/ "Install ESPHome Device Builder.") and then move on to step 3. It runs on a computer (Windows, macOS, or Linux), so you don't need Home Assistant.

3\. Click "Edit" as shown below. If your Apollo device only appears under **Discovered**, click **Take control** on it first.

![ESPHome Device Builder card for the Apollo MTR-1 with the Edit button circled](/assets/bluetooth-proxy-tutorial-2.png)

4\. Copy the code inside the codeblock below.

```yaml
  fast_connect: True
```

5\. Paste the code as shown below directly below the yaml you just edited above. Make sure the spaces look the same and there are no red lines under any of the code.

![MTR-1 YAML in ESPHome Device Builder with fast_connect: True added under wifi](/assets/hidden-ssid-tutorial-1.png)

6\. Click save then Install in the top right.

![ESPHome Device Builder editor with an arrow pointing to Save and Install in the top right](/assets/hidden-ssid-tutorial-2.png)

!!! warning "Keep Homey connected"

    If ESPHome Device Builder adds an API encryption key to your device, Homey can't connect to the device after the install. Device Builder adds a key when you take control of a device with **Enable encryption** turned on, and that option is on by default in the **Take control** dialog. To reconnect, copy the key with **Show encryption key** in the device's menu in ESPHome Device Builder. Then open the device's settings in Homey, choose **Repair**, and enter the key.

7\. Click "Wirelessly" and let it finish compiling then installing.

![ESPHome Device Builder install options with Wirelessly circled](/assets/hidden-ssid-tutorial-3.png)

8\. When you see this "OTA Successful" it has finished and you can click "Close" in the bottom right.

![ESPHome Device Builder install log showing OTA successful with an arrow to Close](/assets/hidden-ssid-tutorial-4.png)

9\. You are finished and your Apollo device is now able to connect to your Wi-Fi with a hidden SSID! Make sure you understand the downsides as [mentioned here](https://esphome.io/components/wifi.html "downsides of fast_connect: true").<br><br>**fast\_connect** (*Optional*, boolean): If enabled, directly connects to WiFi network without doing a full scan first. This is required for hidden networks and can significantly improve connection times. Defaults to `off`. The downside is that this option connects to the first network the ESP sees, even if that network is very far away and better ones are available.