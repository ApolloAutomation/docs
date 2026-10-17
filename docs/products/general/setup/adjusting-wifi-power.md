---
title: Adjusting Wi-Fi power save
description: Tutorial for how to adjust Wi-Fi Power Save.
---
# Adjusting Wi-Fi power save

The ESP chips produce a significant amount of energy (heat) constantly using Wi-Fi. This guide explains how to <a href="https://esphome.io/components/wifi.html#power-save-mode" target="_blank" rel="noreferrer nofollow noopener">adjust the Wi-Fi power save mode to high</a> to combat this.

!!! warning "This will negatively affect your Wi-Fi performance!"

    While some options *can* reduce the power usage of the ESP, they generally also decrease the reliability of the Wi-Fi connection, with frequent disconnections from the router in the highest power saving mode.

1\. Open the ESPHome Device Builder.

[![Open your Home Assistant instance and show the dashboard of an app.](https://my.home-assistant.io/badges/supervisor_app.svg)](https://my.home-assistant.io/redirect/supervisor_app/?app=5c53de3b_esphome&repository_url=https%3A%2F%2Fgithub.com%2Fesphome%2Fhome-assistant-addon)

![ESPHome Device Builder dashboard showing cards for several Apollo devices](/assets/power-save-tutorial-1.png)

2\. If you do not have it installed, [go here](https://esphome.io/guides/getting_started_hassio.html#installing-esphome-device-compiler "Install ESPHome Device Builder.") and then move on to step 3.

3\. Click "Edit" as shown below.

![MTR-1 device card in ESPHome Device Builder with the Edit button circled](/assets/power-save-tutorial-2.png)

4\. Copy the code inside the codeblock below.

```yaml
  power_save_mode: HIGH
```

5\. Paste the code as shown below. Make sure the spaces look the same and there are no red lines under any of the code.

![MTR-1 YAML in ESPHome Device Builder with power_save_mode: HIGH added under wifi](/assets/power-save-tutorial-3-1.png)

6\. In the top right of the same screen click "SAVE" and then "INSTALL".

![Save and Install buttons outlined in red at the top right of the ESPHome Device Builder editor](/assets/renaming-devices-pic-7-1.png)

7\. Once you see "INFO OTA successful" you are done. Click "STOP" to exit.

![ESPHome Device Builder install log with INFO OTA successful and the Stop button circled](/assets/update-frequency-pic-3.png)

8\. You are finished and your Apollo device now has power\_save\_mode set to high!