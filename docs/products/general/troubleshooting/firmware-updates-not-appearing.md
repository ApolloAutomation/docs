---
title: Firmware Updates Not Appearing
description: What to check when the Firmware Update entity never offers an update.
---
Apollo devices check for new firmware by downloading a small manifest file from `apolloautomation.github.io` over HTTPS. If the **Firmware Update** entity in Home Assistant always shows *up to date* even though a newer release exists, work through the list below.

1\. **Make sure the device can reach the internet.**

* The device needs outbound HTTPS (port 443) to `apolloautomation.github.io`. If your sensors live on an isolated IoT VLAN that blocks traffic leaving the network, the update check fails silently and the entity shows *up to date* forever.
* To confirm, watch the device logs (ESPHome Device Builder → Logs, or the device's web page) — a blocked check logs `Failed to fetch manifest` with `ESP_ERR_HTTP_CONNECT`.
* Allow the device to reach `apolloautomation.github.io` on port 443 in your firewall rules, then reboot the device.

2\. **Give it a moment after a reboot — or update your firmware.**

* On older firmware the very first update check after a boot can be skipped if WiFi isn't connected yet, and the next check only happens about 6 hours later. Newer firmware checks as soon as the network connects.
* If the entity looks stale right after a reboot, either wait, reboot once more while the network is up, or update to the latest firmware release.

3\. **Devices adopted in the ESPHome Device Builder update differently.**

* If you have taken control of the device's configuration in the ESPHome Device Builder, Home Assistant manages updates through the Device Builder instead of the manufacturer Firmware Update entity. That is expected — build and install updates from the Device Builder in that case.

!!! tip "Battery devices"

    Battery powered sensors only check for updates while they are awake and connected. If the update never appears, keep the device awake (see [Prevent Sleep](../battery-sensors/prevent-sleep.md)) and reboot it once.
