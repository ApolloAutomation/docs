# Getting Started

This will walk you through the process of connecting your new Apollo Automation sensor to Home Assistant through ESPHome. If at any point you get stuck, join our [Discord](https://dsc.gg/apolloautomation) for some help.

### Connecting Through Hotspot

To connect through the sensor's onboard hotspot follow the below:

1. Plug the sensor into a quality power brick. They require 5v and under an amp so most phone chargers will be fine. ESP devices are sensitive to power fluctuations and users have had some issues with really cheap power bricks. If your device is restarting or unavailable please try a different power brick.
2. On your phone or PC, open the wifi settings and connect to "Apollo MSR-1 Hotspot", it might take a minute for the wifi network to show up
3. Once connected it should automatically open a dashboard for your sensor
   * If this does not automatically open the dashboard, please open your web browser and go to [http://192.168.4.1](http://192.168.4.1)
4. Select the wifi network that you would like your sensor to connect to
5. Input the wifi password. After connecting, the sensor's dashboard will automatically close. You've successfully connected your sensor, please check out the "Connecting Sensor To Home Assistant" section for the next steps.

### Connecting To ESPHome Addon

You can connect to the ESPHome addon in Home Assistant to easily update your device. If you don't have ESPHome addon installed you can follow the steps here: [Installing ESPHome Dashboard](https://esphome.io/guides/getting_started_hassio.html)

Make sure to fill out your Wi-Fi details in the SECRETS section by clicking on the SECRETS Image below.

![image.png](../assets/9P0image.png)

```yaml
# Your Wi-Fi SSID and password - keep the quotes and just replace the name and password between the quotes!
wifi_ssid: "your-wifi-ssid-here"
wifi_password: "your-wifi-pass-here"
```

1. 1. Once installed you'll have the addon's icon on the left side of your HA instance:
      1. ![Screenshot 2024-06-06 at 2.57.55 PM.png](../assets/screenshot-2024-06-06-at-2-57-55-pm.png)
      2. Click on adopt for your sensor![Screenshot 2024-06-06 at 4.06.20 PM.png](../assets/screenshot-2024-06-06-at-4-06-20-pm.png)
      3. Then adopt again

   ![image.png](../assets/image.png)

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