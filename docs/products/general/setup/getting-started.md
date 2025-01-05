# Getting Started

This will walk you through the process of connecting your new Apollo Automation sensor to Home Assistant through ESPHome. If at any point you get stuck, join our <a href="https://dsc.gg/apolloautomation" target="_blank" rel="noopener">Discord</a> for some help.

### Connecting Through Hotspot

To connect through the sensor's onboard hotspot follow the below:

1. Plug the sensor into a quality power brick. They require 5v and under an amp so most phone chargers will be fine. ESP devices are sensitive to power fluctuations and users have had some issues with really cheap power bricks. If your device is restarting or unavailable please try a different power brick.
2. On your phone or PC, open the WiFi settings and connect to "Apollo MSR-2 Hotspot", it might take a minute for the WiFi network to show up.

   ![](../../../assets/getting-started-connect-to-hotspot-image-1.png)

3. Once connected it should automatically open a dashboard for your sensor

   If this does not automatically open the dashboard, please open your web browser and go to [http://192.168.4.1](http://192.168.4.1)

   ![](../../../assets/getting-started-connect-to-hotspot-image-2.png)

4. Select the WiFi network that you would like your sensor to connect to.
5. Input the WiFi password. After connecting, the sensor's dashboard will automatically close. You've successfully connected your sensor, please check out the "Connecting Sensor To Home Assistant" section for the next steps.

   ![](../../../assets/getting-started-connect-to-hotspot-image-3.png)

### Connecting with <a href="https://www.home-assistant.io/integrations/improv_ble" target="_blank" rel="noopener">Improv via BLE</a>

!!! note "Pre-requirement:"
Bluetooth built in such as a raspberry pi or at least one ESP32 BLE Proxy.

!!! tip "this is a tip"
    this works tho

1\. Navigate to settings -&gt; integrations then click the "ADD" button below your new Apollo device!

![](../../../assets/improv-ble-pic-1.png)

2\. Click submit when it asks if you want to setup your new device and shows you a MAC address.

![](../../../assets/improv-ble-pic-2.png)

3\. Type in your Wi-Fi name and password in the two fields.

![](../../../assets/improv-ble-pic-3.png)

4\. Wait for it to finish, you will see the image below while it connects.

![](../../../assets/improv-ble-pic-4.png)

5\. <a href="https://my.home-assistant.io/redirect/config_flow_start?domain=esphome" target="_blank" rel="noopener">Click the link shown in the image below</a> (do not click close).

![](../../../assets/improv-ble-pic-5-1.png)

6\. When successful, you will see this image appear!

![](../../../assets/improv-ble-pic-6.png)

### Connecting To ESPHome Device Compiler (previously ESPHome Addon)

Note: You can skip the esphome device compiler completely if you do not want to rename your sensor or make edits to the yaml. [Please Skip to the next part by clicking here!](https://wiki.apolloautomation.com/products/general/setup/getting-started/#connecting-to-home-assistant-via-esphome-integration)

You can add the ESPHome Device Compiler addon in Home Assistant to easily update your device or edit the yaml. If you don't have ESPHome Device Compiler addon installed you can follow the steps here: <a href="https://esphome.io/guides/getting_started_hassio.html#installing-esphome-device-compiler" target="_blank" rel="noopener">Installing The ESPHome Device Compiler.</a>

Make sure to fill out your Wi-Fi details in the SECRETS section by clicking on the SECRETS Image below.

![esphome-device-compiler-dashboard-pic-1.png](../../../assets/esphome-device-compiler-dashboard-pic-1.png)

```yaml
# Your Wi-Fi SSID and password - keep the quotes and just replace the name and password between the quotes!
wifi_ssid: "your-wifi-ssid-here"
wifi_password: "your-wifi-pass-here"
```

1\. Click the ESPHome Compiler in your sidebar then click "TAKE CONTROL" for your new Apollo Device!

![](../../../assets/getting-started-esphome-device-compiler-pic-1.png)

2\. Rename your sensor here (this only renames the sensor in the ESPHome Device Compiler's Dashboard) or skip it and continue on by clicking "TAKE CONTROL" again as shown below.

![](../../../assets/getting-started-esphome-device-compiler-pic-2.png)

3\. Click install (DO NOT click skip!) and let your device get adopted into the ESPHome Device Compiler. Please have patience as this takes a few minutes to compile and then install to your new Apollo device!

![](../../../assets/getting-started-esphome-device-compiler-pic-3.png)

4\. When it is finished, it will look like this image below and you can click "Close" in the bottom right to get back to the main screen. As long as it says "INFO OTA successful" then it finished successfully. There is no need to be worried about "ERROR Logger not configured" as that was removed to allow for other components to exist on your new Apollo device!

![](../../../assets/getting-started-esphome-device-compiler-pic-4.png)

5\. Your new device is now adopted into the ESPHome Device Compiler and you can move on to Integrating with Home Assistant via the ESPHome Integration below!

### Connecting to Home Assistant via ESPHome Integration:

1\. Click the "Notification" Icon in the bottom left.

![](../../../assets/connect-to-esphome-integration-1.png "Esphome Notification Icon")

2\. Click "check it out" to go to the integrations page and see the new device that was found.

![](../../../assets/connect-to-esphome-integration-2.png "Esphome New Device Discovered")

3\. Click "ADD" to begin adding the device to home assistant.

![Click add to add device to esphome integration](../../../assets/connect-to-esphome-integration-3.png)

4\. Click "SUBMIT" to confirm you want to add your new Apollo device to home assistant.

![Submit to confirm adding to esphome integration](../../../assets/connect-to-esphome-integration-4.png)

5\. Give it an area and click "FINISH".

![Define what area it is in then click finish](../../../assets/connect-to-esphome-integration-5.png)

6\. Your device is now added to home assistant via the ESPHome integration, and you can easily navigate to it by going to settings -&gt; <a href="http://homeassistant.local:8123/config/integrations/integration/esphome" target="_blank" rel="noopener">esphome integration</a> -&gt; click on the name of your new device!

[Click here to Join our discord for fast support!](https://dsc.gg/apolloautomation)\{ .md-button .md-button--primary \}