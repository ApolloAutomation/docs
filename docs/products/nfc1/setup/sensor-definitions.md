---
title: NFC-1 sensor definitions
description: Every entity the Apollo NFC-1 exposes in Home Assistant, from tag sensors and write buttons to card emulation and feedback settings.
---
# NFC-1 sensor definitions

Once your NFC-1 is in Home Assistant, its device page has controls, sensors, and settings for reading, writing, and emulating tags. Use the tabs below to see what each entity does.

=== "Controls"

    | Control | What it does |
    |---------|--------------|
    | **Mode** | What the NFC-1 does with the next tag: **Read**, **Write**, **Clean**, or **Format**. Picking **Write**, **Clean**, or **Format** arms that task, and the NFC-1 goes back to **Read** once the task is done, cancelled, or timed out. **Write** writes the **Write URL**. |
    | **Write URL Tag** | Arms a write of the **Write URL** setting to the next tag you present. |
    | **Write New HA Tag** | Arms a write of a new Home Assistant tag with a random ID to the next tag you present. |
    | **Clean Tag** | Arms a clean of the next tag you present, which removes the data on it so you can reuse it. |
    | **Format Tag** | Arms a format of the next tag you present. On NTAG and MIFARE Ultralight tags, format does the same as clean. |
    | **Cancel Tag Operation** | Cancels an armed write, clean, or format and puts the NFC-1 back in **Read** mode. |
    | **RGB Light** | The NFC-1's RGB LED, with **Slow Pulse**, **Fast Pulse**, and **Armed Pulse** effects. While **LED Feedback** is on, scans and tag tasks take over the LED. Turn **LED Feedback** off to use it as a regular light. |

=== "Sensors"

    | Sensor | What it reports |
    |--------|-----------------|
    | **Tag Present** | On while a tag is on the reader. |
    | **Last Tag** | The Home Assistant tag ID of the last tag scanned, or its UID when the tag doesn't carry a Home Assistant tag. This is the ID the tag shows under **Settings → Tags**. |
    | **Last Tag UID** | The UID of the last tag scanned. |
    | **Last Tag Content** | The content of the first record on the last tag scanned, such as a URL or a line of text. Up to 250 characters. |
    | **Last Operation** | The result of the last write, clean, format, or card emulation change, such as **Waiting for tag**, **Write verified**, **Write mismatch**, **Timed out**, or **Cancelled**. See [Read and write tags](../examples/read-and-write-tags.md#check-the-result). |
    | **NFC Event** | Fires an event for each scan, removal, and step of a tag task. See [NFC Event types](../examples/read-and-write-tags.md#nfc-event-types). |
    | **Online** | Connection status of the device to Home Assistant. |
    | **ESP Temperature** | Internal temperature of the ESP32-C6 chip. Runs warmer than the room because of the processor and Wi-Fi radio. |
    | **Uptime** | How long the device has been running since its last restart. |

=== "Configuration"

    | Setting | Default | What it does |
    |---------|:-------:|--------------|
    | **Write URL** | Empty | The URL that **Write URL Tag** and **Mode: Write** write to a tag. Up to 120 characters. |
    | **Mode Timeout** | 30 s | How long the NFC-1 waits for a tag after you arm a write, clean, or format, from 5 to 300 seconds. |
    | **Card Emulation** | Off | Makes the NFC-1 act as a tag that holds the **Emulation URL**, so a phone tapped on it opens that link. It turns itself off if **Emulation URL** is empty. See [Card emulation](../examples/read-and-write-tags.md#card-emulation). |
    | **Emulation URL** | Empty | The URL the NFC-1 hands to a phone while **Card Emulation** is on. Up to 120 characters. |
    | **HA App Record** | On | Adds an Android app record to Home Assistant tag URLs that the NFC-1 writes or emulates, so Android phones open the Home Assistant app. Other URLs never get it. |
    | **Buzzer** | On | Turns the beeps for scans, tasks, and errors on or off. |
    | **Volume** | 50% | Buzzer volume, from 0 to 100%. |
    | **LED Feedback** | On | Turns the LED flashes for scans, tasks, and errors on or off. While it's off, the NFC-1 leaves the **RGB Light** alone. |
    | **Feedback Brightness** | 80% | How bright the LED feedback flashes are, from 1 to 100%. |
    | **Bluetooth Proxy** | Off | Lets the NFC-1 act as a [Bluetooth proxy](../../general/setup/bluetooth-proxy.md) for Home Assistant, extending Bluetooth range to nearby devices. |
    | **Tag Polling** | On | Turns tag reading on or off. Disabled by default. |
    | **Firmware Channel** | Stable | Which firmware channel the NFC-1 updates from. **Beta** gets new features earlier but is less tested than **Stable**. See [Switch to beta firmware](../../general/setup/switch-to-beta-branch.md). |
    | **Firmware Update** | n/a | Shows whether a newer firmware is available on the selected channel and installs it, straight from Home Assistant. See [Updating firmware](../../general/calibrating-and-updating/updating-firmware.md). |
    | **Reinstall Firmware** | n/a | Installs the firmware from the selected channel, even if it's the version you already have. Press it after you change **Firmware Channel**. |

=== "Diagnostic"

    | Entity | What it shows |
    |--------|---------------|
    | **NFC Reader** | Whether the NFC reader chip is working. It only reads disconnected after the chip fails to start more than 10 times in a row. |
    | **Last Tag Type** | The type of the last tag scanned. Disabled by default. |
    | **RSSI** | Wi-Fi signal strength. |
    | **IP Address**, **Connected SSID**, **Connected BSSID**, **MAC Address** | Wi-Fi connection details. Disabled by default. |
    | **ESPHome Version** | The ESPHome version the firmware was compiled with. |
    | **Apollo Firmware Version** | The Apollo firmware build installed on the device (for example, `26.10.13.2`). |
    | **Restart** | Restarts the device. Helpful for troubleshooting or refreshing the connection. |
    | **Restart (Safe Mode)** | Restarts into safe mode for 5 minutes, which skips the device's normal setup so you can recover it over the network. Disabled by default. |
    | **Factory Reset** | Erases settings and Wi-Fi details and returns the device to its firmware defaults. Disabled by default. |

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
