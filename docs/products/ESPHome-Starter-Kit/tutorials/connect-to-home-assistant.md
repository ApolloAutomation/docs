---
title: Connect to Home Assistant
description: Step by step guide to adding your ESPHome Starter Kit to Home Assistant so its sensors, switches, and LEDs show up as entities.
---
# Connect to Home Assistant

Once your ESPHome Starter Kit is flashed and on Wi-Fi, Home Assistant sees it automatically. This page walks through accepting the device into Home Assistant and confirming your sensors and switches show up as entities you can use in dashboards and automations.

## Before you start

* Home Assistant is running on the same network as your Starter Kit. If you can open the Home Assistant UI from a browser on the same Wi-Fi as the device, you're good.
* Your Starter Kit is flashed and reachable. The fastest check: open `http://esphome-starter-kit.local/` in a browser, you should see the device's built-in web page.

## Add your device

1. Open [Devices & services](https://my.home-assistant.io/redirect/integrations/) in Home Assistant. Look for a card titled **ESPHome** under **Discovered** listing `esphome-starter-kit`.
    * If you do not see the card, [add the ESPHome integration manually](https://my.home-assistant.io/redirect/config_flow_start/?domain=esphome). Enter the device's hostname (`esphome-starter-kit.local`) or its IP address.
2. Click **Configure** on the discovered card.
3. When prompted for the encryption key, paste the value of your `api_encryption_key` from `secrets.yaml` in ESPHome Device Builder. If Home Assistant and Device Builder run on the same machine, the key is often pre-filled.
4. Pick an **Area** for the device (optional), like Living Room or Office.
5. Click **Submit**.

<!-- TODO: screenshot of the ESPHome discovery card in HA with esphome-starter-kit listed. -->

## Confirm it worked

Open the [ESPHome integration](https://my.home-assistant.io/redirect/integration/?domain=esphome) in Home Assistant and pick your device. You should see:

* Every component you added in ESPHome Device Builder as an entity (the **GPIO Switch** for accessory power, the **AHT10** temperature and humidity sensors, the **Onboard RGB LED**).
* A green status indicator showing the device is online.

Toggle the **Onboard RGB LED** light entity and confirm the LED responds on the board. That's the round trip working: Home Assistant talks to your device, your device talks back.

## Troubleshooting

#### The device never appears under Discovered

* Confirm Home Assistant is on the same Wi-Fi network as the device.
* Some routers and VLAN setups block mDNS broadcasts across subnets. If you run UniFi, turning on mDNS in your network settings usually fixes this. See the [UniFi mDNS guide](../../general/troubleshooting/ubiquiti-unifi-mdns-auto-discover-issue.md). Otherwise, add the integration manually using the device's IP address. Look the IP up on your router's client list or in the **Device Information** section of the ESPHome Device Builder info panel.
* The device's web page should still load at the hostname or IP. If it does not, the device is not reachable from your computer yet and Home Assistant will not find it either.

#### The encryption key is rejected

Open `secrets.yaml` in Device Builder, copy the `api_encryption_key` value, and paste it back into the Home Assistant prompt. If the value in Device Builder has changed since you last flashed, install the firmware again so the device knows the new key.

---

Want to understand what just happened under the hood? Read [the Home Assistant integration](../learning-the-basics/how-esphome-talks-to-home-assistant.md).

<a href="../../setup/first-steps/" class="md-button md-button--primary"><img src="/assets/esphome-logo.svg" /> Back - First Steps</a>
