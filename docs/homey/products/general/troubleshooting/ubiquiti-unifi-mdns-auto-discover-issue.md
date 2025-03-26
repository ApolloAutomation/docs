# Ubiquiti Unifi mDNS Auto Discover Issue

**If mDNS is unchecked then Home Assistant and ESPHome will not auto discover new devices. Also, if you have different networks that Home Assistant and ESPHome devices are on, then you will need mDNS on both networks and firewall rules between them. (Thank you to the Ubiquiti Discord member Blue!) Below are guides for using your PC and the Unifi Network mobile app to fix this issue.  
  
Quick Guide**

1. Settings > Network > Multicast Settings > Select the networks you want mDNS/IGMP Snooping on

![mDNS Settings.jpeg](../assets/mdns-settings.jpeg)

(Thank you to the Ubiquiti Discord member MK!)  
  
**Steps for PC**

1\. Log into your Unifi network through your default IP address which is usually 192.168.1.1  
2\. Select Network

![mdns1.PNG](../assets/mdns1.PNG)

3\. Select Settings

![mdns2.PNG](../assets/mdns2.PNG)  
  
4\. Select Networks

![mdns3.PNG](../assets/mdns3.PNG)

5\. Select the Default Network

![mdns4.PNG](../assets/mdns4.PNG)

6\. Check Multicast DNS

![mdns5.PNG](../assets/78Kmdns5.PNG)

7\. Now the Home Assistant/ESPHome auto-discover issue should be fixed!  
8\. If this does not work then you can also try checking IGMP Snooping (checkbox above Multicast DNS) on your IoT networks.

  
**Steps for the Unifi Network Mobile App**

1\. Open the Unifi Network app

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