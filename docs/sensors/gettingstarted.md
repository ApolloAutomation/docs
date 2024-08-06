# Getting Started

This will walk you through the process of connecting your new Apollo Multisensor (MSR-1) to Home Assistant through ESPHome. If at any point you get stuck, join our [Discord](https://discord.gg/mMNgQPyF94) for some help.

### Connecting Through Hotspot

To connect through the sensor's onboard hotspot follow the below:

1. Plug the sensor into a quality power brick. They require 5v and under an amp so most phone chargers will be fine. ESP devices are sensitive to power fluctuations and users have had some issues with really cheap power bricks. If your device is restarting or unavailable please try a different power brick.
2. On your phone or PC, open the wifi settings and connect to "Apollo MSR-1 Hotspot", it might take a minute for the wifi network to show up
3. Once connected it should automatically open a dashboard for your sensor 
    - If this does not automatically open the dashboard, please open your web browser and go to [http://192.168.4.1](http://192.168.4.1)
4. Select the wifi network that you would like your sensor to connect to
5. Input the wifi password. After connecting, the sensor's dashboard will automatically close. You've successfully connected your sensor, please check out the "Connecting Sensor To Home Assistant" section for the next steps.

### Connecting To ESPHome Addon

You can connect to the ESPHome addon in Home Assistant to easily update your device. If you don't have ESPHome addon installed you can follow the steps here: [Installing ESPHome Dashboard](https://esphome.io/guides/getting_started_hassio.html)

1. Once installed you'll have the addon's icon on the left side of your HA instance: 
    1. [![Screenshot 2024-06-06 at 2.57.55 PM.png](https://wiki.apolloautomation.com/uploads/images/gallery/2024-06/scaled-1680-/screenshot-2024-06-06-at-2-57-55-pm.png)](https://wiki.apolloautomation.com/uploads/images/gallery/2024-06/screenshot-2024-06-06-at-2-57-55-pm.png)
    2. Click on adopt for your sensor[![Screenshot 2024-06-06 at 4.06.20 PM.png](https://wiki.apolloautomation.com/uploads/images/gallery/2024-06/scaled-1680-/screenshot-2024-06-06-at-4-06-20-pm.png)](https://wiki.apolloautomation.com/uploads/images/gallery/2024-06/screenshot-2024-06-06-at-4-06-20-pm.png)
    3. Then adopt again

<p class="callout warning">Don't change the name at this step. If you'd like to change the name please refer to [this article](https://wiki.apolloautomation.com/books/general/page/renaming-apollo-devices) after you've completed these steps. </p>

[![image.png](https://wiki.apolloautomation.com/uploads/images/gallery/2024-06/scaled-1680-/image.png)](https://wiki.apolloautomation.com/uploads/images/gallery/2024-06/image.png)

### Connecting Sensor To Home Assistant

1. **Once you connect your sensor to wifi through the above process, open up Home Assistant. Then in the bottom left click on “Settings”**

![homeassistantsettings.png](https://beautiful-cheetah.pikapod.net/uploads/images/gallery/2023-10/homeassistantsettings.png)

2. **From there click on “Devices And Services”**

![homeassistant_deviceandservices.png](https://beautiful-cheetah.pikapod.net/uploads/images/gallery/2023-10/homeassistant-deviceandservices.png)

3. **Look for the discovered sensor. It should be named “apollo-msr-mk1” with some random letters and numbers (Those come from the device's mac address). Click on “Configure” and then “Submit”.**
    
    
    1. <p class="callout info">**If you do not see the device as discovered, make sure you have the ESPHome integration installed to Home Assistant you can find [their instructions here](https://esphome.io/guides/getting_started_hassio.html#connecting-your-device-to-home-assistant)**</p>

![img4_optimized.png](https://beautiful-cheetah.pikapod.net/uploads/images/gallery/2023-10/img4-optimized.png)

4. **Add the sensor to ESPHome. It will now show up in the ESPHome integration**

![img5_optimized.png](https://beautiful-cheetah.pikapod.net/uploads/images/gallery/2023-10/img5-optimized.png)

5. **The sensor has now been added to Home Assistant and you can use it as you please. For ideas please visit our ideas section or join our [Discord](https://discord.gg/mMNgQPyF94)**

![img6_optimized.png](https://beautiful-cheetah.pikapod.net/uploads/images/gallery/2023-10/img6-optimized.png)

### Sensors

You should now have the sensor added! If you have any problems or need help please join our [Discord](https://discord.gg/mMNgQPyF94) and post in the #support channel. Or just join to check out product development and community spotlights. Our team monitors that and can quickly respond there. Or visit our [ideas section](https://wiki.apolloautomation.cloud/Ideas/MultisensorMk1) to find cool ways to display the information

### Looking For Ideas On How To Use Your Sensor?

- Graph Co2 Over Time
- Turn The LED Red When C02 Is Over 1000 ppm
- Send You An Alert When Motion Is Detected After 11pm

Or check out our #show-off channel in the Apollo [Discord](https://discord.gg/mMNgQPyF94) for community submissions