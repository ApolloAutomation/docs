---
title: Adding Apollo Devices To Hidden Networks
description: Turn on fast_connect in ESPHome Device Builder so your Apollo device can connect to a Wi-Fi network with a hidden SSID.
---
# Adding Apollo devices to hidden networks

A Wi-Fi network with a hidden SSID needs the ESPHome `fast_connect` option, which connects your Apollo device to the network directly instead of scanning for it first. In this guide you add that option to your device's YAML in ESPHome Device Builder and install the update over Wi-Fi.

!!! note "Before you start"

    You need ESPHome Device Builder. If you do not have it installed, [install the standalone ESPHome Device Builder](https://esphome.io/guides/installing_esphome/ "Install ESPHome Device Builder.") first. It runs on a computer (Windows, macOS, or Linux), so you don't need Home Assistant.

1\. Open ESPHome Device Builder.

![ESPHome Device Builder dashboard listing Apollo devices](/assets/bluetooth-proxy-tutorial-1.png)

2\. Click **Edit** on your Apollo device, as shown below. If your Apollo device only appears under **Discovered**, click **Take control** on it first.

![ESPHome Device Builder card for the Apollo MTR-1 with the Edit button circled](/assets/bluetooth-proxy-tutorial-2.png)

!!! warning "Keep Homey connected"

    If ESPHome Device Builder adds an API encryption key to your device, Homey can't connect to the device after the install. Device Builder adds a key when you take control of a device with **Enable encryption** turned on, and that option is on by default in the **Take control** dialog. To reconnect, copy the key with **Show encryption key** in the device's menu in ESPHome Device Builder. Then open the device's settings in Homey, choose **Repair**, and enter the key.

3\. Copy the code inside the code block below.

```yaml
  fast_connect: True
```

4\. Paste it on a new line inside the `wifi:` section of your device's YAML, as shown in the screenshot below. Make sure the spaces at the start of the line match the lines around it, and that there are no red lines under any of the code.

![MTR-1 YAML in ESPHome Device Builder with fast_connect: True added under wifi](/assets/hidden-ssid-tutorial-1.png)

5\. Click **Save**, then **Install** in the top right.

![ESPHome Device Builder editor with an arrow pointing to Save and Install in the top right](/assets/hidden-ssid-tutorial-2.png)

6\. Click **Wirelessly** and let it finish compiling, then installing.

![ESPHome Device Builder install options with Wirelessly circled](/assets/hidden-ssid-tutorial-3.png)

7\. When you see **OTA Successful**, the install has finished. Click **Close** in the bottom right.

![ESPHome Device Builder install log showing OTA successful with an arrow to Close](/assets/hidden-ssid-tutorial-4.png)

You're finished! Your Apollo device can now connect to your Wi-Fi with a hidden SSID.

!!! warning "Understand the downside of fast_connect"

    `fast_connect` (optional, true or false): when enabled, your device connects directly to your Wi-Fi network without doing a full scan first. This is required for hidden networks and can significantly improve connection times. It defaults to `off`. The downside is that your device connects to the first network it sees, even if that network is very far away and better ones are available. Read more about the downsides [in the ESPHome Wi-Fi documentation](https://esphome.io/components/wifi.html "downsides of fast_connect: true").
