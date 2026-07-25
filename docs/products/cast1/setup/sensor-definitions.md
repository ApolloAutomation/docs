---
title: CAST-1 Sensor Definitions
description: These are all of the entities exposed by the CAST-1 to automate on!
---
# Sensor Definitions

Once added to Home Assistant you can configure different settings for your CAST-1. Use the tabs below to see what each entity does, grouped the same way Home Assistant displays them.

=== "Controls"

    | Control | What it does |
    |---------|--------------|
    | **Apollo CAST-1 Player** | The main media player for Home Assistant. Use it to play media, text-to-speech, and announcements to the speakers connected to your CAST-1. Announcements duck the music down, then bring it back when they finish. |
    | **Apollo CAST-1 Sendspin Player** | The Music Assistant streaming player. This is the player your CAST-1 exposes to Music Assistant, and it's the one you group with other CAST-1s for synchronized multi-room audio. |
    | **RGB Light** | The four onboard RGB LEDs. Click the light bulb or color wheel to change the color, pick a **Slow Pulse** or **Fast Pulse** effect, or use the toggle to turn it on or off. |

=== "Sensors"

    | Sensor | What it reports |
    |--------|-----------------|
    | **Track Title** | Title of the track currently playing through the CAST-1. |
    | **Artist** | Artist of the current track. |
    | **Album** | Album of the current track. |

=== "Configuration"

    | Setting | Default | What it does |
    |---------|:-------:|--------------|
    | **Firmware Channel** | Stable | Which firmware channel the CAST-1 updates from. **Beta** gets new features earlier but is less tested than **Stable**. |
    | **Firmware Type** | WiFi | Which firmware variant the CAST-1 updates to, **WiFi** or **Ethernet**. Match this to how your CAST-1 is connected. |
    | **Firmware Update** | — | Checks for and installs a firmware update for the selected Firmware Type and Channel, straight from Home Assistant. |
    | **Bluetooth Proxy** | Off | Lets the CAST-1 act as a Bluetooth proxy for Home Assistant, extending Bluetooth range to nearby devices. |
    | **WizMote Auto-Discovery** | Off | Turn on to pair a WizMote. While it's on, the next WizMote button press links that remote to your CAST-1. |
    | **Clear WizMote Pairing** | — | Unpairs the current WizMote so you can pair a different one. |
    | **WizMote MAC Address** | — | MAC address of the paired WizMote. Set automatically during pairing, or type one in manually. |
    | **WizMote On** | Play | Action the WizMote **On** button runs. Choose from Nothing, Play, Pause, Play / Pause, Next Track, Previous Track, Volume Up, Volume Down, Toggle Light, or Send HA Event. |
    | **WizMote Off** | Pause | Action the WizMote **Off** button runs. |
    | **WizMote Night** | Toggle Light | Action the WizMote **Night** button runs. |
    | **WizMote Brightness Up** | Volume Up | Action the WizMote **Brightness Up** button runs. |
    | **WizMote Brightness Down** | Volume Down | Action the WizMote **Brightness Down** button runs. |
    | **WizMote Button 1** | Previous Track | Action the WizMote **1** button runs. |
    | **WizMote Button 2** | Next Track | Action the WizMote **2** button runs. |
    | **WizMote Button 3** | Send HA Event | Action the WizMote **3** button runs. |
    | **WizMote Button 4** | Send HA Event | Action the WizMote **4** button runs. |
    | **ESP Reboot** | — | Restarts the device. Helpful for troubleshooting or refreshing the connection. |
    | **Factory Reset** | — | Erases settings and returns the device to factory firmware defaults. Disabled by default. |

=== "Diagnostic"

    | Entity | What it shows |
    |--------|---------------|
    | **WizMote Status** | Whether a WizMote is paired. Shows "No WizMote paired", "Discovery mode active", or "Paired:" with the remote's MAC address. |
    | **Link Speed** | Negotiated speed of the wired Ethernet connection. Ethernet firmware only. |
    | **Apollo Firmware Version** | The Apollo firmware build installed on the device (for example, `26.7.12.1`). |
    | **ESPHome Version** | The ESPHome version the firmware was compiled with. |
    | **IP Address** | The device's IP address on your network. |
    | **Online** | Connection status of the device to Home Assistant. |
    | **ESP Temperature** | Internal temperature of the ESP32 chip. Runs warmer than the room because of the processor and Wi-Fi radio. Disabled by default. |
    | **Uptime** | How long the device has been running since its last reboot. |

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
