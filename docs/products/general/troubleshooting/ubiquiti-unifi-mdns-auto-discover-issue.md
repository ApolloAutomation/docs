# Ubiquiti Unifi mDNS Auto Discover Issue

!!! tip "If mDNS is unchecked then Home Assistant and ESPHome will not auto discover new devices"

    If you have different networks that Homey and ESPHome devices are on, then you will need mDNS working across both networks and firewall rules allowing access between them. Below are guides for using your PC and the Unifi iOS app to fix this issue.

##### **Method 1: Browser**

1\. Log into your Unifi network through your default IP address which is usually <a href="http://192.168.1.1" target="_blank" rel="noreferrer nofollow noopener">http://192.168.1.1</a>

2\. Select Network.

![mdns1.PNG](../assets/mdns1.PNG)

3\. Select Settings.

![mdns2.PNG](../assets/mdns2.PNG)

4\. Select Networks.

![mdns3.PNG](../assets/mdns3.PNG)

5\. Select the Default Network

![mdns4.PNG](../assets/mdns4.PNG)

6\. Check Multicast DNS

![mdns5.PNG](../assets/78Kmdns5.PNG)

7\. Now the Home Assistant/ESPHome auto-discover issue should be fixed!

##### **Method 2: Unifi iOS App.**

1\. Open the UniFi app.

![mmdns1.PNG](../assets/mmdns1.PNG)

2\. Tap Settings/Gear Icon

![mmdns2.PNG](../assets/mmdns2.PNG)

3\. Tap Networks

![mmdns3.PNG](../assets/mmdns3.PNG)

4\. Tap Default Network

![mmdns4.PNG](../assets/mmdns4.PNG)

5\. Tap the Multicast DNS slider

![mmdns5.PNG](../assets/mmdns5.PNG)

6\. Now the Home Assistant/ESPHome auto-discover issue should be fixed!