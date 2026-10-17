---
title: Connection Issues
description: Checks to work through when your Apollo device won't stay connected or Homey can't find it.
---
# Common connection issues

Work through these checks if your Apollo device won't stay connected or Homey can't find it.

1\. Try a couple of different power cord and power brick combinations. This matters a lot more than you'd think!

2\. Check your Wi-Fi list for the device's hotspot. If the hotspot is showing up, the device is not connected to a network. Connect to the hotspot and add your Wi-Fi network, as shown in [Connecting through hotspot](../../setup/getting-started/#connecting-through-hotspot).

3\. Check your router's list of connected devices. Your device shows up with the Apollo name followed by a 6-digit hex value, which is the end of its hardware (MAC) address.

!!! tip "Look at the mDNS wiki articles as well"

    Auto discovery depends on mDNS, which is used to tell which devices are on your network. If a firewall blocks mDNS, or your network doesn't forward mDNS traffic, auto discovery can run into issues. If you use UniFi or OPNsense, see the [UniFi mDNS guide](../ubiquiti-unifi-mdns-auto-discover-issue/) or the [OPNsense mDNS guide](../opnsense-mdns-auto-discover-issue/).
