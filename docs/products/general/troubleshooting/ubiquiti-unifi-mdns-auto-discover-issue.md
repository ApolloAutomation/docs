---
title: Ubiquiti UniFi mDNS Auto Discover Issue
description: Tutorial to help fix the Ubiquiti UniFi mDNS Auto Discover Issue.
---
# Ubiquiti UniFi mDNS Auto Discover Issue

!!! tip "If mDNS is unchecked then Home Assistant and ESPHome will not auto discover new devices"

    If you have different networks that Homey and ESPHome devices are on, then you will need mDNS working across both networks and firewall rules allowing access between them. Below are guides for using your PC and the UniFi iOS app to fix this issue.

## **Method 1: Browser**

1\. Log into your UniFi network through your default IP address which is usually <a href="http://192.168.1.1" target="_blank" rel="noreferrer nofollow noopener">http://192.168.1.1</a>

2\. Select Network.

![UniFi OS Applications page with the Network application highlighted](/assets/mdns1.PNG)

3\. Select Settings.

![UniFi Network sidebar with the Settings gear icon highlighted](/assets/mdns2.PNG)

4\. Select Networks.

![UniFi Network settings menu with Networks highlighted](/assets/mdns3.PNG)

5\. Select the Default Network

![UniFi Networks list with the Default network highlighted](/assets/mdns4.PNG)

6\. Check Multicast DNS

![UniFi Default network settings with the Multicast DNS checkbox checked and highlighted](/assets/78Kmdns5.PNG)

7\. Now the Home Assistant/ESPHome auto-discover issue should be fixed!

## **Method 2: UniFi iOS App.**

1\. Open the UniFi app.

![UniFi Network app icon circled in the phone's app search results](/assets/mmdns1.PNG)

2\. Tap Settings/Gear Icon

![UniFi Network app Settings screen with the gear icon circled in the bottom bar](/assets/mmdns2.PNG)

3\. Tap Networks

![UniFi Network app Settings screen with Networks circled](/assets/mmdns3.PNG)

4\. Tap Default Network

![UniFi Network app Networks list with the Default network circled](/assets/mmdns4.PNG)

5\. Tap the Multicast DNS slider

![UniFi Network app Edit Default screen with the Multicast DNS toggle turned on and circled](/assets/mmdns5.PNG)

6\. Now the Home Assistant/ESPHome auto-discover issue should be fixed!