---
title: OPNsense mDNS Auto Discover Issue
description: Tutorial to help fix the OPNsense mDNS Auto Discover Issue
---
# OPNsense mDNS Auto Discover Issue

!!! tip "If mDNS is unchecked then Home Assistant and ESPHome will not auto discover new devices"

    If you have different networks that Home Assistant and ESPHome devices are on, then you will need mDNS working across both networks and firewall rules allowing access between them. Below is a guide for installing the mDNS Repeater plugin on OPNsense to fix this issue.

Install the mDNS Repeater

1\.	Click System -&gt; Click Firmware -&gt; Click Plugins -&gt; Search for "mdns" -&gt; Click the “+” symbol to install os-mdns-repeater.

![OPNsense Firmware Plugins page with numbered steps to search for and install os-mdns-repeater](/assets/opnsense-mdns-guide-pic-1.png)

2\. Confirm that the installation was successful.

![OPNsense Firmware Updates log showing os-mdns-repeater installed successfully](/assets/opnsense-mdns-guide-pic-2.png)

3\. Refresh the page and then go to Services -&gt; mDNS Repeater (if it isn't there after refreshing your screen, verify the plugin install was successful.)-&gt; Check off "enable" -&gt; select your networks containing Home Assistant / ESPHome IoT devices -&gt; click save.

![OPNsense mDNS Repeater page with numbered steps: Enable checked, IOT and LAN interfaces selected, then Save](/assets/opnsense-mdns-guide-pic-3.png)

Now the Home Assistant/ESPHome auto-discover issue should be fixed!