---
title: Apollo Automation FAQ
description: "Answers to common questions about Apollo Automation sensors with Homey: power, radar, Wi-Fi resets, light readings, and adding devices to Homey."
---
# Apollo Automation FAQ

## 1\. How much power do your sensors use?

* All Apollo sensors use 1amp or less, some of them 350-500mA.

---

## 2\. What all can the MSR-2 LD2410B mmWave sensor go through?

* It can reliably go through drywall and some other materials such as thin wood and some couches.

---

## 3\. My MSR-2 is triggering and no one is there.

* We have seen this happen before. First, restart the radar with **Restart radar** under **Maintenance** in the device's **Settings** in the Homey app. If that doesn't help, factory reset the radar with **Factory Reset Radar** on the sensor's own web page: in a browser, open `http://apollo-msr-2-xxxxxx.local`, where `xxxxxx` is the last 6 characters of the device's name in Homey. If it still triggers, try a [factory re-flash](../../msr2/troubleshooting/msr2-code/). We also see success with users re-seating their LD2410B mmWave sensor.

---

## 4\. How do I reset my Wi-Fi?

* Plug in your device then hold down the boot button for 10 seconds. The Wi-Fi credentials should be reset and it will broadcast its hotspot again.

---

## 5\. My lux sensor doesn't seem to be working, how do I fix it?

* The light reading updates every 60 seconds by default, which isn't great for flows that react to lux values. On the MSR-2, MTR-1, and PLT-1, shorten it to a more responsive 3 to 5 seconds with **LTR390 Update Interval** on the sensor's own web page. In a browser, open the sensor's address, such as `http://apollo-mtr-1-xxxxxx.local` for an MTR-1, where `xxxxxx` is the last 6 characters of the device's name in Homey. On the MSR-2, the page hides this setting at first, so click **Show All** to list it. Homey has no setting for it.
* On other sensors, the interval is fixed in the firmware, and changing it means editing the firmware with ESPHome. If you also run Home Assistant, [this short guide](../../../../products/general/tutorials/how-to-edit-your-sensor's-lux-update-interval/) shows how.

---

## 6\. Do I need to press Clean SEN55 for my AIR-1 or set up a flow for it?

* No, your AIR-1 will self-clean once a week per this [recommended documentation from the manufacturer.](https://sensirion.com/media/documents/6791EFA0/62A1F68F/Sensirion_Datasheet_Environmental_Node_SEN5x.pdf)

---

## 7\. Can your sensors be used with OpenHAB?

* Yes, please install [this binding](https://github.com/seime/openhab-esphome "OpenHAB-ESPHome") and then restart OpenHAB and our devices will show up to configure!

---

## 8\. My Apollo device doesn't show up when I add it in Homey.

* Make sure the device is powered on and connected to the same network as your Homey. If it still isn't listed, choose **Enter an address instead** on the first page of the pairing wizard and enter the device's IP address or hostname, plus its encryption key if it has one.
* Homey finds devices with mDNS, which doesn't cross every VLAN, so a device on a separate network may only show up by address. To make discovery work across networks, see [Connection issues](../troubleshooting/connection-issues/) and the mDNS guides for [UniFi](../troubleshooting/ubiquiti-unifi-mdns-auto-discover-issue/) and [OPNsense](../troubleshooting/opnsense-mdns-auto-discover-issue/).

---

## 9\. My CO2 values are way off from my other Apollo devices.

* If your sensor is exposed to high levels of vibrations or too much airflow, the <a href="https://sensirion.com/products/catalog/SCD40" target="_blank" rel="noreferrer nofollow noopener">SCD40 CO2 sensor</a> will have issues working properly.
