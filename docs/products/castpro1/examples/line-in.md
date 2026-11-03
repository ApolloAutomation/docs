---
title: Play Line In with Music Assistant
description: Stream a turntable, TV, or other source from your CAST PRO-1's Line In jack to any speaker or group in Music Assistant.
---
# Play Line In with Music Assistant

Plug a turntable, TV, or other audio source into your Apollo CAST PRO-1, and its Line In becomes a source in Music Assistant. Play it on the CAST PRO-1 itself, on any other speaker, or on a group of rooms in sync.

!!! note "Before you start"

    - **CAST PRO-1 firmware 26.11.3.2 or newer.** Update from the **Firmware Update** entity on the device page. Until this release reaches the Stable channel, [switch to the Beta channel](../../general/setup/switch-to-beta-branch.md) first.
    - **Music Assistant 2.10.7 or newer.** Update it from its app page in Home Assistant.

## Connect your source

Plug your source into the CAST PRO-1's **Line In** jack with a 3.5 mm cable. Line In is input only, and the other jack (analog and optical) is output only. (1)
{ .annotate }

1.  Line In takes line-level audio, like a TV, CD player, or streamer. A turntable needs a phono preamp, built in or separate. If your source has RCA outputs, use a 3.5 mm-to-RCA cable.

## Play it on a speaker

Line In plays on any speaker or group in Music Assistant, Apollo or not.

1\. Open **Music Assistant** from the Home Assistant sidebar.

2\. Select the speaker or group where you want to hear it.

3\. Open **Browse** and select your CAST PRO-1's Line In. It's named **Sendspin Source** with your CAST PRO-1's name, for example **Sendspin Source (Living Room)**. If you have more than one, open **Sendspin Source** first and pick it there.

4\. Select **Play**.

Your Line In now plays on that speaker. It plays in one place at a time, so picking it on another speaker moves it there. Not in the list? See [Troubleshooting](#troubleshooting).

!!! warning "On its own CAST PRO-1, Line In plays through Optical"

    While its Line In streams, the CAST PRO-1 plays through its optical output, even with **Audio Output** set to **Analog**. That's because Line In and the analog output share one audio connection inside the device. It goes back to Analog when the stream stops. This also applies to anything else it plays while its Line In streams to another room.

    Speakers on the analog output? Play Line In on another speaker, or connect this CAST PRO-1 to your receiver or soundbar with an optical cable.

## Start it automatically with the Line In switch

Your CAST PRO-1 can't tell when your source starts playing, so the **Line In** switch on its device page tells Music Assistant instead:

- Turn **Line In** on, and Music Assistant starts playing it after about 2 seconds.
- Turn it off, and Music Assistant stops it about a minute later.

Line In starts on the CAST PRO-1 itself unless you pick somewhere else. To change it, go to **Settings → Players** in Music Assistant, open your CAST PRO-1, and set **Automatically play line-in on** to another speaker or group. Choose **Off** to only start Line In by hand.

!!! tip "Turn on Line In from an automation"

    Turn **Line In** on in an automation, for example when your TV turns on, and the sound starts in the room you picked.

## Line In Streaming

**Line In Streaming**, under **Configuration** on the device page, sets how your CAST PRO-1 sends Line In over your network.

| Option | Pick it when |
| --- | --- |
| **Compressed (best for WiFi)** | Your CAST PRO-1 is on WiFi. This is the default. It uses about 128 kbps, which keeps audio smooth on a weaker signal. |
| **Lossless (Ethernet or strong WiFi)** | Your CAST PRO-1 is on Ethernet or a strong WiFi signal. It sends uncompressed audio at about 1.5 Mbps. |

Changing it restarts your CAST PRO-1, which stops anything playing on it.

## Troubleshooting

**The Line In isn't in Music Assistant**

- Check your CAST PRO-1 is on firmware 26.11.3.2 or newer, and Music Assistant on 2.10.7 or newer.
- If your CAST PRO-1 shows **Setup required** in Music Assistant, finish its setup and choose **Connect unpaired with audio input** or **Pair device**.

**Turning on Line In doesn't start it**

- Check **Automatically play line-in on** isn't set to **Off**.
- If **Line In** was already on when your CAST PRO-1 or Music Assistant restarted, turn it off and back on.

**No sound from the CAST PRO-1's own speakers**

- While its Line In streams, the CAST PRO-1 only plays through its optical output. See [Play it on a speaker](#play-it-on-a-speaker).

**Choppy audio**

- Set **Line In Streaming** to **Compressed (best for WiFi)**, or connect an Ethernet cable.

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
