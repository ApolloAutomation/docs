---
title: HA Integration
description: A conceptual overview of how ESPHome devices announce themselves to Home Assistant, what the encryption key is for, and how device components turn into Home Assistant entities.
---
# HA Integration

The **ESPHome integration** is what makes your Starter Kit visible to Home Assistant. Once it's set up, every switch, sensor, and light you defined in ESPHome Device Builder appears in Home Assistant as something you can read, control, or automate against. This page explains how that handoff actually works.

## Auto-discovery

When your Starter Kit boots, it announces itself on your local network. Home Assistant listens for those announcements and shows your device under **Settings → Devices & services** as soon as it sees one.

This is why most users do not have to type anything in to add their device. The device says "I'm here, here are my details" and Home Assistant picks it up.

The protocol that does this is called **mDNS** (multicast DNS). It's the same standard that makes `.local` hostnames work on a Mac or iPhone.

If your router or network setup blocks mDNS across subnets (some VLAN configurations do), auto-discovery does not work. In that case you add the integration manually using the device's IP address.

## Encryption

The link between your Starter Kit and Home Assistant is encrypted. Both ends use the same shared key (the `api_encryption_key` in your `secrets.yaml`) to talk to each other.

When Home Assistant configures the device for the first time, it prompts you for that key. If Home Assistant and ESPHome Device Builder run on the same machine, the key is often pre-filled. Otherwise, copy it from `secrets.yaml` in Device Builder and paste it into the Home Assistant prompt.

If the keys do not match, Home Assistant cannot read from or write to the device. The fix is to copy the current `api_encryption_key` value from Device Builder, install firmware to the device, and re-enter the key in Home Assistant.

For more on `secrets.yaml`, see [What is secrets.yaml?](what-is-secrets-yaml.md).

## Components and entities

Every component you added in ESPHome Device Builder becomes an entity in Home Assistant:

* A **switch** (like the Accessory Power switch) becomes a **switch entity**.
* A **sensor** (temperature, humidity, voltage, and so on) becomes a **sensor entity** with its unit of measurement.
* A **light** (like the Onboard RGB LED) becomes a **light entity** with color and brightness controls.
* A **button** becomes a **button entity** you can trigger from a dashboard.

The entity's name in Home Assistant comes from the **Name** field you set in Device Builder. If you renamed **Accessory Power** to **Bedroom Lamp Power**, that is what it is called in Home Assistant too.

## Controlling your device

You have two ways to control your Starter Kit, and both keep working at the same time:

* Open the **on-device web page** at <a href="http://esphome-starter-kit.local/" target="_blank" rel="noreferrer nofollow noopener">esphome-starter-kit.local</a> to control your device directly from any browser on your network. No Home Assistant required. See the [Web Server in Core Components](core-components.md#web-server) for more.
* Your Starter Kit appears as a new device under the **ESPHome integration** in Home Assistant. Each switch, sensor, and light becomes an entity you can use in dashboards, automations, voice control, history, and alerts.

    [![Open the ESPHome integration in your Home Assistant.](https://my.home-assistant.io/badges/integration.svg)](https://my.home-assistant.io/redirect/integration/?domain=esphome)

For a single device, the on-device web page is often enough. For anything that ties together with other devices or runs on a schedule, Home Assistant is the place.

!!! info "If auto-discovery doesn't work"

    Some router setups (notably VLANs and segmented networks) block mDNS broadcasts. If your device never shows up under **Discovered**, add the integration manually using the device's IP address.

    For UniFi networks specifically, see our [UniFi mDNS troubleshooting guide](../../../general/troubleshooting/ubiquiti-unifi-mdns-auto-discover-issue/).

<a href="../what-is-secrets-yaml/" class="md-button md-button--primary"><img src="/assets/esphome-logo.svg" /> Back - What is secrets.yaml?</a> <a href="../../tutorials/connect-to-home-assistant/" class="md-button md-button--primary"><img src="/assets/esphome-logo.svg" /> Tutorial - Connect to Home Assistant</a>


--8<-- "_snippets/community-help.md"
