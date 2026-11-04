---
title: CAST PRO-1 sensor definitions
description: These are all of the entities exposed by the CAST PRO-1 to automate on!
---
# Sensor definitions

Once added to Home Assistant you can configure different settings for your CAST PRO-1. Use the tabs below to see what each entity does, grouped the same way Home Assistant displays them.

=== "Controls"

    | Control | What it does |
    |---------|--------------|
    | **Player** | The main media player for Home Assistant. Use it to play media, text-to-speech, and announcements to the speakers connected to your CAST PRO-1. Announcements duck the music down, then bring it back when they finish. See [TTS and Announcements](../examples/tts-announcements.md). |
    | **Sendspin Player** | The Music Assistant streaming player. This is the player your CAST PRO-1 exposes to Music Assistant, and it's the one you group with other CAST players for synchronized multi-room audio. Announcements sent to it forward to the ESPHome player and duck the music the same way. |
    | **RGB Light** | The four onboard RGB LEDs. Click the light bulb or color wheel to change the color, pick a **Slow Pulse** or **Fast Pulse** effect, or use the toggle to turn it on or off. |
    | **LED Strip** | An addressable LED strip on the screw terminals. Disabled by default. See [Add an LED strip](../examples/led-strip.md). |
    | **LED Strip Music Mode** | Turns the LED strip on whenever music is playing. Disabled by default. |

=== "Sensors"

    | Sensor | What it reports |
    |--------|-----------------|
    | **Track Title** | Title of the track currently playing through the CAST PRO-1. |
    | **Artist** | Artist of the current track. |
    | **Album** | Album of the current track. |

=== "Configuration"

    | Setting | Default | What it does |
    |---------|:-------:|--------------|
    | **Firmware Channel** | Stable | Which firmware channel the CAST PRO-1 updates from. **Beta** gets new features earlier but is less tested than **Stable**. See [Switch to Beta Firmware](../../general/setup/switch-to-beta-branch.md). |
    | **Firmware Update** | n/a | Checks for and installs a firmware update from the selected channel, straight from Home Assistant. See [Updating Firmware](https://wiki.apolloautomation.com/products/general/calibrating-and-updating/updating-firmware/) for the full walkthrough. |
    | **Audio Output** | Analog | Which output the **Analog/Optical Out** jack uses: **Analog** for a 3.5mm audio cable, or **Optical** for a mini-TOSLINK optical cable. |
    | **Line In Streaming** | Compressed (best for WiFi) | How the CAST PRO-1 sends the **Analog In (Line In)** source over your network. **Compressed (best for WiFi)** suits a weaker Wi-Fi connection, **Lossless (Ethernet or strong WiFi)** suits Ethernet or a strong Wi-Fi signal. Changing it restarts the device. See [Play a source through Analog In (Line In)](../additional-info/analog-in.md#choose-the-streaming-quality). |
    | **Announcement Ducking** | -40 dB | How far music drops while an announcement plays, from -80 to 0 dB. 0 turns ducking off. Firmware 26.11.3.3 or newer. See [TTS and Announcements](../examples/tts-announcements.md#what-happens-during-an-announcement). |
    | **Announcement LED Brightness** | 100% | How bright the onboard LEDs glow during an announcement. 0% keeps them off. Firmware 26.11.3.3 or newer. |
    | **Bluetooth Proxy** | Off | Lets the CAST PRO-1 act as a Bluetooth proxy for Home Assistant, extending Bluetooth range to nearby devices. |
    | **WizMote Auto-Discovery** | Off | Turn on to pair a WizMote. While it's on, the next WizMote button press links that remote to your CAST PRO-1. |
    | **Clear WizMote Pairing** | n/a | Unpairs the current WizMote so you can pair a different one. |
    | **WizMote MAC Address** | n/a | MAC address of the paired WizMote. Set automatically during pairing, or type one in manually. |
    | **WizMote On** | Play | Action the WizMote **On** button runs. Choose from Nothing, Play, Pause, Play / Pause, Next Track, Previous Track, Volume Up, Volume Down, Toggle Light, or Send HA Event. |
    | **WizMote Off** | Pause | Action the WizMote **Off** button runs. |
    | **WizMote Night** | Toggle Light | Action the WizMote **Night** button runs. |
    | **WizMote Brightness Up** | Volume Up | Action the WizMote **Brightness Up** button runs. |
    | **WizMote Brightness Down** | Volume Down | Action the WizMote **Brightness Down** button runs. |
    | **WizMote Button 1** | Previous Track | Action the WizMote **1** button runs. |
    | **WizMote Button 2** | Next Track | Action the WizMote **2** button runs. |
    | **WizMote Button 3** | Send HA Event | Action the WizMote **3** button runs. |
    | **WizMote Button 4** | Send HA Event | Action the WizMote **4** button runs. |
    | **ESP Reboot** | n/a | Restarts the device. Helpful for troubleshooting or refreshing the connection. |
    | **Factory Reset ESP** | n/a | Erases settings and returns the device to factory firmware defaults. Disabled by default. Holding the **boot** button for 10 seconds does the same thing, see [Factory reset](../troubleshooting/castpro1-boot-button.md#factory-reset). |
    | **LED Strip** settings | n/a | **Chipset**, **Color Order**, **Count**, **Effect A Pattern**, **Effect A Speed**, **Effect B Pattern**, **Effect B Speed**, **Max Brightness** and **Music Effect**. Disabled by default. See [Add an LED strip](../examples/led-strip.md). |

=== "Diagnostic"


    | Entity | What it shows |
    |--------|---------------|
    | **LED Strip Test** | Runs a color test on an [LED strip](../examples/led-strip.md): red, green, blue and white, then a rainbow. Disabled by default. |
    | **WizMote Status** | Whether a WizMote is paired. Shows "No WizMote paired", "Discovery mode active", or "Paired:" with the remote's MAC address. |
    | **Apollo Firmware Version** | The Apollo firmware build installed on the device (for example, `26.7.12.1`). |
    | **ESPHome Version** | The ESPHome version the firmware was compiled with, and its config hash. |
    | **Network Connection** | Which connection the CAST PRO-1 is using: **Ethernet**, **WiFi**, **Ethernet + WiFi** when it's on both at once, **Hotspot** while it's waiting for Wi-Fi details, or **Connecting**. |
    | **Ethernet IP Address** | The device's IP address on the wired connection. Reads **Unknown** when no Ethernet cable is connected. |
    | **WiFi IP Address** | The device's IP address on your Wi-Fi network. |
    | **Online** | Connection status of the device to Home Assistant. |
    | **ESP Temperature** | Internal temperature of the ESP32 chip. Runs warmer than the room because of the processor and Wi-Fi radio. Disabled by default. |
    | **Uptime** | How long the device has been running since its last reboot. |

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
