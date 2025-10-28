---
title: BTN-1 Getting Started Guide
description: Step by step guide to getting started with your BTN-1!
---
# BTN-1 Getting Started

This will guide you through adding on switches and keycaps to your BTN-1 then adding it to your Wi-Fi and Home Assistant!

### Installing Brown Switches

1\. Line up the two gold pins with the holes on your BTN-1, then press down gently. Be careful, as the pins can bend or get damaged if too much force is used.

![](../../../assets/btn-1-install-switches-gif.webp)

### Installing Keycaps

1\. Line up the + on the keycap with the + on the top of the switch you installed. It may require a little pressure, but it should press on smoothly. Once placed, lightly tap to ensure the keycap is fully seated.

![](../../../assets/btn-1-getting-started-installing-keycaps-gif.webp)

### Connecting Through Hotspot

To connect through the sensor's onboard hotspot follow the below:

1\. Plug the BTN-1 in via USB-C. A 5v 1amp power supply will work fine

!!! success "If your sensor is restarting or not broadcasting Wi-Fi try another usb-c cable and power supply!"

    ESP devices are sensitive to power fluctuations and require constant 5v power. Our devices use 1amp or less so most used phone chargers will work - just make sure it's a quality one!

2\. On your phone or PC, open the WiFi settings and connect to "Apollo BTN-1 Hotspot".

![](../../../assets/btn-1-reset-wifi-screenshot.png)

3\. Once connected it should automatically open a dashboard for your sensor. If this does not automatically open the dashboard, please open your web browser and go to [http://192.168.4.1](http://192.168.4.1)

4\. Select the Wi-Fi network that you would like your sensor to connect to or scroll to the bottom and type in your Wi-Fi network then click "**Save**".

![](../../../assets/btn-1-getting-started-enter-wifi-details-hotspot.png)

!!! tip "Tip for Mesh Wi-Fi systems or multiple Access Points"

    If you have multiple access points or a mesh system please manually type in your Wi-Fi network so it will join with the strongest signal!

5\. Once connected, the sensor's dashboard will automatically close. You've successfully connected your sensor to your Wi-Fi.

[Click here for next steps!](https://wiki.apolloautomation.com/products/btn1/setup/getting-started/#connecting-to-home-assistant-via-esphome-integration){                                        .md-button .md-button--primary }

### Connecting with <a href="https://www.home-assistant.io/integrations/improv_ble" target="_blank" rel="noopener">Improv via BLE</a>

!!! note "Pre-requirement: Bluetooth proxy or Bluetooth Home Assistant hardware required"

    Bluetooth built in such as a raspberry pi or at least one <a href="https://wiki.apolloautomation.com/products/general/setup/bluetooth-proxy/" target="_blank" rel="noreferrer nofollow noopener">ESP32 BLE Proxy</a> is required to use this to setup your Apollo device. If you have already followed the "Connecting through Hotspot" please skip this section.

1\. Navigate to settings -&gt; integrations then click the "**ADD**" button below your new Apollo device then click **Submit**.

![](../../../assets/btn-1-improv-ble-add.gif)

2\. Once prompted, type in your Wi-Fi name and password in the two fields then click **Submit**. Click on **Close** once it finishes.

![](../../../assets/btn-1-improv-ble-wifi-setup.gif)

3\. Click on **Add** then click on **Submit**. Choose an area and then click **Finish**.

![](../../../assets/btn-1-improv-ble-esphome-integration.gif)

4\. Your device is now added to your Wi-Fi and added to the ESPHome Integration in Home Assistant. You should now be ready to <a href="https://wiki.apolloautomation.com/products/btn1/examples/btn-1-blueprint" target="_blank" rel="noreferrer nofollow noopener">setup a blueprint</a> and start using your BTN-1!

### Connecting To ESPHome Device Builder

!!! tip "Skip the ESPHome Device Builder unless..."

    Feel free to [skip to the next section by clicking here](https://wiki.apolloautomation.com/products/general/setup/getting-started/#connecting-to-home-assistant-via-esphome-integration "Click to jump to the ESPHome Integration steps!") unless you need to rename your sensor or do manual edits to the yaml

You can add the ESPHome Device Builder addon in Home Assistant to easily update your device or edit the yaml. If you don't have ESPHome Device Builder addon installed you can <a href="http://homeassistant.local:8123/hassio/store" target="_blank" rel="noreferrer nofollow noopener">search esphome device builder on the addon store</a> and install it.

Make sure to fill out your Wi-Fi details in the **secrets** section by clicking on the **secrets** button.

![](../../../assets/esphome-device-builder-secrets.png)

```yaml
# Your Wi-Fi SSID and password - keep the quotes and just replace the name and password between the quotes!
wifi_ssid: "your-wifi-ssid-here"
wifi_password: "your-wifi-pass-here"
```

1\. Open the <a href="http://homeassistant.local:8123/5c53de3b_esphome/ingress" target="_blank" rel="noreferrer nofollow noopener"><strong>ESPHome Device Builder</strong></a> dashboard.

![](assets/esphome-device-builder-show-discovered-device.png)

2\. Click **Show** in the top right to show your discovered devices then click on **Take Control** then click **Install**. This can take multiple minutes or longer on low-end hardware.

![](../../../assets/btn-1-getting-started-take-control-gif.gif)

3\. Once you see "**INFO OTA successful**" you are done. Click "**STOP**" to exit.

![](../../../assets/btn-1-getting-started-ota-successful.png)

4\. Your new device is now adopted into the ESPHome Device Builder and you can move on to Integrating with Home Assistant via the ESPHome Integration below!

### Connecting to Home Assistant via ESPHome Integration:

1\. Head to the <a href="http://homeassistant.local:8123/config/integrations/integration/esphome" target="_blank" rel="noreferrer nofollow noopener">ESPHome Integration</a> then click on **Add** then click **Submit**. When prompted click **Finish** then give it a location and click **Finish** or click **Skip and Finish**.

![](../../../assets/btn-1-getting-started-esphome-integration-gif.gif)

2\. Your device is now added to home assistant via the ESPHome integration, and you can easily navigate to it by going to settings -&gt; <a href="http://homeassistant.local:8123/config/integrations/integration/esphome" target="_blank" rel="noopener">ESPHome integration</a> -&gt; click on the name of your new device!

[Click here to join our Discord for fast support! :simple-discord:](https://dsc.gg/apolloautomation){                                          .md-button .md-button--primary }