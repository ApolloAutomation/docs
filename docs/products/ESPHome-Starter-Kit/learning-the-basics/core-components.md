---
title: Core Components
description: A guide to the Web Server and Accessory Power Rail components that ship enabled by default on the Apollo ESPHome Starter Kit.
---
# Core Components

When you create a new Apollo ESPHome Starter Kit project in **ESPHome Device Builder**, two components are included for you by default:

- **Web Server**, which gives your device its own local web page at `esphome-starter-kit.local`.
- **Accessory Power Rail**, which powers the Onboard RGB LED and any modules connected to the accessory header.

You don't have to do anything to turn these on. This page explains what each one does, why Apollo ships them enabled, and the settings most users want to know about.

---

## Web Server

The **Web Server** component runs a small website directly on your ESP32-C6. As soon as your device is on Wi-Fi, you can open <a href="http://esphome-starter-kit.local/" target="_blank" rel="noreferrer nofollow noopener">esphome-starter-kit.local</a> (or its IP address) on any phone or PC on the same network and control the device.

Apollo ships it on by default so the kit works without Home Assistant. If you only want a smart LED on your desk, you never have to touch HA, you just visit the device's page in a browser.

#### Common Settings

- **Version (v2 vs v3).** The Apollo project pins **Version 3**, the newer single-page interface that loads faster, looks cleaner, and shows controls and sensors in a sensible order. v2 is the older multi-page layout. There's almost no reason to switch back.
- **Port.** Defaults to **80** so plain `esphome-starter-kit.local` works. Change it only if something else on your network is already serving on port 80 and you want to avoid a clash.
- **Username and password.** Off by default. Set them under **Show advanced settings → Auth** if you want to gate the page so anyone on your Wi-Fi can't toggle your LED. Pair this with `secrets.yaml` so the credentials don't sit in your shared YAML. See <a href="../what-is-secrets-yaml/">What is secrets.yaml?</a> for the pattern.
- **OTA over the web page.** The v3 web server can accept firmware uploads straight from the browser. Helpful for quick experiments, but turn it off (or behind auth) if your device sits on an untrusted network.
- **Including/excluding entities.** Advanced setting that lets you hide specific entities from the web page without removing them from Home Assistant. Useful if you have internal helpers you don't want users to see.

#### Add Component

If you remove the Web Server component, the device still works, but `esphome-starter-kit.local` will stop responding. To add it back:

1. In **ESPHome Device Builder**, open your device and go to **Core configuration**.
2. Click **Add component**, scroll to **Web Server**, and click **Add**.
3. Click **Add** once more to confirm.
4. Toggle **Show advanced settings**, scroll to **Version**, and select **3**.

<a href="https://esphome.io/components/web_server/" target="_blank" rel="noreferrer nofollow noopener" class="md-button md-button--primary"><img src="/assets/esphome-logo.svg" /> ESPHome Web Server docs</a>

---

## Accessory Power Rail

The **Accessory Power Rail** is a software switch that controls power to the kit's accessory header, the connector where the Onboard RGB LED, button, motion, temperature/humidity, and LED/buzzer modules get their 3.3V.

When the rail is **on**, your modules and the Onboard RGB LED have power and respond. When the rail is **off**, those accessories go dark. The ESP32-C6 itself stays on.

Apollo ships the rail enabled and set to come back on after a reboot, so the kit "just works" out of the box. The reason it exists as a switch (rather than always-on) is that turning the rail off briefly is the cleanest way to reset a misbehaving module without unplugging the kit, and it can be automated from Home Assistant.

#### Common Settings

- **Restore mode.** Controls what happens to the rail when the device powers back on after losing power. The Apollo default is **restore the last state, default to on**, so a power blip won't leave your modules dark. Other options like "always on" or "always off" are available if you want a specific boot behavior.
- **Hide it from Home Assistant.** By default the rail shows up as a controllable switch entity in HA, handy for power-cycling a flaky module from an automation. If you'd rather it not clutter your dashboard, mark it `internal: true` under the advanced settings.
- **Icon and name.** Cosmetic, but you can rename the entity or change its icon if "Accessory Power Rail" isn't how you want it to appear in HA.
- **GPIO pin.** Informational, not something you should change. The pin is fixed in hardware on the ESPHome Starter Kit board, so editing it will just stop the rail from working.

#### How It Works

The Accessory Power Rail is an ESPHome **GPIO switch** under the hood. Apollo gives it a friendly name and pre-fills the pin so you don't have to know that, but if you ever want to see the raw configuration, look at the GPIO switch component in the ESPHome docs.

#### Add Component

If you remove the rail, **the Onboard RGB LED and any plugged-in modules will stop working properly** because they get their power from it. To add it back:

1. In **ESPHome Device Builder**, open your device and go to the **Components** section.
2. Click **Add component**, scroll to **Accessory Power Rail**, and click **Add**.
3. Click **Add** once more to confirm.

<a href="https://esphome.io/components/switch/gpio/" target="_blank" rel="noreferrer nofollow noopener" class="md-button md-button--primary"><img src="/assets/esphome-logo.svg" /> ESPHome GPIO Switch docs</a>
