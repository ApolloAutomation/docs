---
title: Getting Started
description: "Generic getting started article."
---
# Getting Started

This will walk you through the process of connecting your new Apollo Automation sensor to Homey. If at any point you get stuck, join our <a href="https://link.apolloautomation.com/discord" target="_blank" rel="noopener">Discord</a> for some help.

## Connecting Through Hotspot:

To get your new Apollo sensor connected to your Wi-Fi, follow the steps below!

1\. Plug the sensor into a quality power brick. They require 5v and under an amp so most phone chargers will be fine. ESP devices are sensitive to power fluctuations and users have had some issues with really cheap power bricks. If your device is restarting or unavailable please try a different power brick.

2\. On your phone or PC, open the Wi-Fi settings and connect to "Apollo MSR-2 Hotspot", it might take a minute for the Wi-Fi network to show up.

![Phone Wi-Fi settings with the Apollo MSR-2 hotspot network highlighted](/assets/getting-started-pic-1-1.png)

3\. Once connected it should automatically open a dashboard for your sensor.

If this does not automatically open the dashboard, please open your web browser and go to [http://192.168.4.1](http://192.168.4.1)

4\. Select the Wi-Fi network that you would like your sensor to connect to or scroll to the bottom and type in your Wi-Fi network then click "**Save**".

![Apollo hotspot page at 192.168.4.1 with the SSID and Password fields and Save button highlighted](/assets/getting-started-pic-2.png)

!!! tip "Tip for Mesh Wi-Fi systems or multiple Access Points"

    If you have multiple access points or a mesh system please manually type in your Wi-Fi network so it will join with the strongest signal!

5\. Once connected, the sensor's dashboard will automatically close. You've successfully connected your sensor to your Wi-Fi.

## Adding Apollo Automation App in Homey:

1\. <a href="https://homey.app/en-us/app/com.apolloautomation/Apollo-Automation/test/" target="_blank" rel="noreferrer nofollow noopener">Navigate to this website</a> and click "Install App". For now this needs to be done from a desktop PC or a browser.

![Homey app store page for Apollo Automation with the Install App button highlighted](/assets/homey-install-app.png)

![Homey install dialog for the Apollo Automation app with Install App highlighted](/assets/homey-install-app-confirm.png)

2\. Select the Homey device you want to install it on and then click "Install App" again!

3\. Your device will install the Apollo Automation Homey App then move to the next section.

## Connecting to Homey:

1\. Open the Homey App on your phone and navigate to the Devices tab at the bottom then select the (+) icon in the top right and choose "**New Device**". Choose "Allow" if it pops up asking to find Bluetooth devices, or you can change this later in settings.

![Homey app Devices tab with the plus menu open and New Device highlighted](/assets/homey-getting-started-pic-2-1.png)

2\. Select Apollo Automation under Brands in the bottom left then choose "Every Apollo Sensor". When prompted, click "Connect".

![Homey Apollo Automation brand page showing the Every Apollo sensor option](/assets/homey-getting-started-pic-3.png)![Homey Every Apollo sensor screen with the Connect button](/assets/homey-getting-started-pic-4.png)

3\. Your Apollo devices will automatically show up and if not, please first <a href="https://wiki.apolloautomation.com/homey/products/general/setup/getting-started/#connecting-through-hotspot" target="_blank" rel="noreferrer nofollow noopener">connect it to your Wi-Fi following the steps outlined here</a>.

4\. Select the device you want to add, in this case an Apollo MTR-1 and click Continue at the bottom.

![Homey New Devices Found screen with an Apollo MTR-1 selected](/assets/homey-getting-started-pic-5.png)

5\. Click Continue Setup and choose a Zone to place your device in. If you are new to Homey you can choose Home and move it to another Zone later after you create more zones!

![Homey Device Connected screen for the Apollo MTR-1 with the Continue Setup button](/assets/homey-getting-started-pic-6.png)

6\. Change any other default settings like the Name, icon, etc or just click Finish in the bottom right.

![Homey Make It Your Own screen for the MTR-1 with name, zone, and Finish button](/assets/homey-getting-started-pic-7.png)

7\. You are done! Your sensor is now ready to create flows and add as a favorite to your dashboard!

[Click here to join our Discord for fast support! :simple-discord:](https://link.apolloautomation.com/discord){                                     .md-button .md-button--primary }