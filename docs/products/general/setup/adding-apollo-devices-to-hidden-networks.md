---
title: Adding Apollo Devices To Hidden Networks
description: Let your Apollo device join a Wi-Fi network with a hidden SSID by adding fast_connect to its YAML in ESPHome Device Builder and reinstalling the firmware.
---

# Adding Apollo devices to hidden networks

Your Apollo device can only join a Wi-Fi network with a hidden SSID after you turn on `fast_connect` in its ESPHome configuration. You add one line to the device's YAML in ESPHome Device Builder, then install the updated firmware wirelessly.

!!! note "Before you start"

    You need ESPHome Device Builder. If you don't have it installed, [install ESPHome Device Builder](https://esphome.io/guides/getting_started_hassio.html#installing-esphome-device-compiler "Install ESPHome Device Builder.") first, then come back to step 1.

1\. Open ESPHome Device Builder.

[![Open your Home Assistant instance and show the dashboard of an app.](https://my.home-assistant.io/badges/supervisor_app.svg)](https://my.home-assistant.io/redirect/supervisor_app/?app=5c53de3b_esphome&repository_url=https%3A%2F%2Fgithub.com%2Fesphome%2Fhome-assistant-addon)

![ESPHome Device Builder dashboard showing cards for several Apollo devices](/assets/bluetooth-proxy-tutorial-1.png)

2\. Click **Edit** on your Apollo device's card.

![MTR-1 device card in ESPHome Device Builder with the Edit button circled](/assets/bluetooth-proxy-tutorial-2.png)

3\. Copy this line:

```yaml
  fast_connect: True
```

4\. Paste it on a new line at the end of the `wifi:` block, indented two spaces like the other lines in that block, as shown below. If any of the code is underlined in red, check that your spacing matches.

![MTR-1 YAML in ESPHome Device Builder with fast_connect: True added under wifi](/assets/hidden-ssid-tutorial-1.png)

5\. Click **Save**, then **Install** in the top right.

![ESPHome Device Builder YAML editor with an arrow pointing to the Save and Install buttons](/assets/hidden-ssid-tutorial-2.png)

6\. Click **Wirelessly** and wait while the firmware compiles and installs.

![ESPHome Device Builder install options with Wirelessly circled](/assets/hidden-ssid-tutorial-3.png)

7\. When the log shows **OTA Successful**, the install is finished. Click **Close** in the bottom right.

![ESPHome Device Builder install log with arrows marking INFO OTA successful and the Close button](/assets/hidden-ssid-tutorial-4.png)

Your Apollo device can now connect to your Wi-Fi network with a hidden SSID.

!!! warning "Know the tradeoff before you rely on it"

    With `fast_connect` on, your device connects to Wi-Fi directly without doing a full scan first. That's what makes hidden networks work, and it can significantly improve connection times. The downside is that it connects to the first network the ESP sees, even if that network is very far away and better ones are available. The option defaults to `off`. Read more about the [downsides of fast_connect](https://esphome.io/components/wifi.html "downsides of fast_connect: true") in the ESPHome docs.
