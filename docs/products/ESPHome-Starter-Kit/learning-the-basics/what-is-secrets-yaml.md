---
title: What is secrets.yaml?
description: A short overview of what secrets.yaml is, what it stores, and why ESPHome uses it.
---
# What is secrets.yaml?

secrets.yaml is a single file inside **ESPHome Device Builder** that stores values you don't want pasted into every device config: your Wi-Fi password, your Home Assistant API key, OTA passwords, MQTT credentials, and so on.

You define each value once in secrets.yaml, then reference it from your device YAML using `!secret`:

```yaml
wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
```

When the device compiles, ESPHome substitutes the real value in place of the `!secret` tag.

## Why it exists

There are two reasons to use secrets.yaml:

- **Safety.** You can copy a device YAML to a friend, paste it on a forum, or commit it to a public repo without leaking your Wi-Fi password or API key. The `!secret` references are safe to share. The values they point to never leave your Device Builder.
- **One place to change things.** Rotate a password once in secrets.yaml and every device that references it picks up the new value on the next flash.

## How it fits in

secrets.yaml lives inside **ESPHome Device Builder**, not on the device itself. The same secrets file is available to every device you build there. A device only ever sees the substituted values baked into its firmware, not the secrets.yaml file.

## Good practice

Treat secrets.yaml like a password manager entry:

- Don't share or post the file. Share your device YAMLs instead, since the `!secret` references in them are safe.
- Keep a backup somewhere safe (a password manager works well). If you reinstall ESPHome Device Builder, you will need to recreate it.
- Rotating a credential is a one-line edit here, then re-flash anything that uses it.

Ready to put this into practice? The Using Secrets tutorial walks through opening secrets.yaml in the Device Builder, the `!secret` syntax, and what to store for every common case (Wi-Fi, Home Assistant API, OTA, web server auth, MQTT).

<a href="../../tutorials/using-secrets/" class="md-button md-button--primary"><img src="/assets/esphome-logo.svg" /> Using Secrets tutorial</a>
