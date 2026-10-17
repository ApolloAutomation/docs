---
title: Adding Apollo Devices To Hidden Networks
description: Tutorial for how to add Apollo Devices To Hidden Networks.
---

# Adding Apollo Devices To Hidden Networks

1\. Open the ESPHome Device Builder.

[![Open your Home Assistant instance and show the dashboard of an app.](https://my.home-assistant.io/badges/supervisor_app.svg)](https://my.home-assistant.io/redirect/supervisor_app/?app=5c53de3b_esphome&repository_url=https%3A%2F%2Fgithub.com%2Fesphome%2Fhome-assistant-addon)

![ESPHome Device Builder dashboard showing cards for several Apollo devices](/assets/bluetooth-proxy-tutorial-1.png)

2\. If you do not have it installed, [go here](https://esphome.io/guides/getting_started_hassio.html#installing-esphome-device-compiler "Install ESPHome Device Builder.") and then move on to step 3.

3\. Click "Edit" as shown below.

![MTR-1 device card in ESPHome Device Builder with the Edit button circled](/assets/bluetooth-proxy-tutorial-2.png)

4\. Copy the code inside the codeblock below.

```yaml
  fast_connect: True
```

5\. Paste the code as shown below directly below the yaml you just edited above. Make sure the spaces look the same and there are no red lines under any of the code.

![MTR-1 YAML in ESPHome Device Builder with fast_connect: True added under wifi](/assets/hidden-ssid-tutorial-1.png)

6 Click save then Install in the top right.

![ESPHome Device Builder YAML editor with an arrow pointing to the Save and Install buttons](/assets/hidden-ssid-tutorial-2.png)

7\. Click "Wirelessly" and let it finish compiling then installing.

![ESPHome Device Builder install options with Wirelessly circled](/assets/hidden-ssid-tutorial-3.png)

8\. When you see this "OTA Successful" it has finished and you can click "Close" in the bottom right.

![ESPHome Device Builder install log with arrows marking INFO OTA successful and the Close button](/assets/hidden-ssid-tutorial-4.png)

9\. You are finished and your Apollo device is now able to connect to your Wi-Fi with a hidden SSID! Make sure you understand the downsides as [mentioned here](https://esphome.io/components/wifi.html "downsides of fast_connect: true").<br><br>**fast\_connect** (*Optional*, boolean): If enabled, directly connects to WiFi network without doing a full scan first. This is required for hidden networks and can significantly improve connection times. Defaults to `off`. The downside is that this option connects to the first network the ESP sees, even if that network is very far away and better ones are available.