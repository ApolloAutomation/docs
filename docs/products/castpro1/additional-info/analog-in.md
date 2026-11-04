---
title: Play a source through CAST PRO-1 Analog In (Line In)
description: Connect a turntable, TV, or other audio source to the CAST PRO-1 Analog In (Line In) jack and play it on any speaker through Music Assistant as a Sendspin Source.
---
# Play a source through Analog In (Line In)

The **Analog In (Line In)** jack on your CAST PRO-1 turns any line-level source into something Music Assistant can play. Plug in a turntable, TV, or CD player, and it shows up in Music Assistant as a **Sendspin Source**. Play it on the speakers connected to your CAST PRO-1, or on any other Music Assistant player in your home.

!!! note "Before you start"

    - Finish the [Getting Started guide](../setup/getting-started.md) first, so your CAST PRO-1 is in Home Assistant and Music Assistant is running.
    - Your CAST PRO-1 needs firmware 26.11.3.2 or newer, and Music Assistant 2.10.7 or newer.

## What you'll need

- **A line-level source.** Most TVs, CD players, and streamers output line level. A turntable needs a phono preamp between it and the CAST PRO-1, unless the turntable has one built in. If the turntable has a **PHONO / LINE** switch on the back, set it to **LINE**.
- **A cable with a 3.5mm plug** for the CAST PRO-1 end. For a source with RCA outputs, use an RCA-to-3.5mm cable.

## Connect your source

1\. Plug the source into the **Analog In** jack, the left of the two 3.5mm jacks. The **Analog/Optical Out** jack is output only, so a source plugged in there won't play.

![Plugging a USB-C power cable into the CAST PRO-1, then a 3.5mm cable into the Analog In jack](/assets/cast-pro-1-plug-in-audio-in.webp)

## Set it up in Music Assistant

Do this once, so Music Assistant can use your CAST PRO-1's Analog In. If you already did it in the [Getting Started guide](../setup/getting-started.md#stream-to-your-cast-pro-1), skip ahead.

1\. Open **Music Assistant**. If your CAST PRO-1 shows **Setup required**, click it. You can also click **Review** on the **A new device was discovered that needs to be set up** banner, then **Start setup**.

2\. Under **How do you want to connect?**, choose **Connect unpaired with audio input**. It's one click with no code.

No **Setup required** on your CAST PRO-1? It's already set up, so go on to the next step.

## Play it in Music Assistant

!!! warning "Your CAST PRO-1 plays through Optical while its Analog In streams"

    While its Analog In streams, your CAST PRO-1 plays through its optical output, even with **Audio Output** set to **Analog**. That's because Analog In and the analog output share one audio connection inside the device. It goes back to Analog when the stream stops, and this applies to anything else it plays in the meantime.

    Speakers on the analog output? Play the source on another player, or connect this CAST PRO-1 to your receiver or soundbar with an optical cable.

1\. Open **Music Assistant** from the Home Assistant sidebar and select the player to hear it on: your CAST PRO-1, or any other player in another room.

2\. Select **Browse**, then **Sendspin Source (Apollo CAST_PRO-1 xxxxxx)**, where `xxxxxx` matches the end of your device's name. If you have more than one CAST PRO-1, open **Sendspin Source** first and pick yours there. (1)
{ .annotate }

1.  Your device's name is at the top of its device page in Home Assistant, for example **Apollo CAST_PRO-1 04c6d0**. If you renamed the player in Music Assistant, the source uses that name instead.

3\. Select **Play**.

<!-- TODO image: /assets/cast-pro-1-sendspin-source.webp | alt: Music Assistant Browse page showing the Sendspin Source for the CAST PRO-1 -->

Your source now plays until you stop it in Music Assistant. It plays on one player at a time, so picking it on another player moves it there. The jack can't tell when your source starts or stops, so start and stop it from Music Assistant each time. On your CAST PRO-1's own player, it's also in the **Select source** menu. No **Sendspin Source** in **Browse**? See [Troubleshooting](#troubleshooting).

!!! tip "See a Line In switch?"

    That's firmware 26.11.3.2. Update from the **Firmware Update** entity, since 26.11.3.3 removes the switch. Until then, leave it off.

## Choose the streaming quality

The **Line In Streaming** setting, under **Configuration** on your CAST PRO-1's device page, sets how it sends your source over the network:

| Option | When to use it |
| --- | --- |
| **Compressed (best for WiFi)** | The default. Uses about 128 kbps, so audio stays smooth on a weaker Wi-Fi connection. |
| **Lossless (Ethernet or strong WiFi)** | Full quality, about 1.5 Mbps. Pick it when your CAST PRO-1 is on Ethernet or a strong Wi-Fi signal. |

Changing it restarts your CAST PRO-1, which stops anything playing on it.

[![Open your Home Assistant instance and show an integration.](https://my.home-assistant.io/badges/integration.svg)](https://my.home-assistant.io/redirect/integration/?domain=esphome)

## Troubleshooting

**The Sendspin Source isn't in Music Assistant**

- Check your CAST PRO-1 is on firmware 26.11.3.2 or newer, and Music Assistant on 2.10.7 or newer.
- Set it up in Music Assistant first. See [Set it up in Music Assistant](#set-it-up-in-music-assistant).
- If you chose **Connect unpaired without audio input** earlier, go to **Settings → Players** in Music Assistant, open your CAST PRO-1's settings, and select **Turn on audio input**.

**No sound from the speakers on your CAST PRO-1**

- While its Analog In streams, the CAST PRO-1 only plays through its optical output. See [Play it in Music Assistant](#play-it-in-music-assistant).

**Choppy audio**

- Set **Line In Streaming** to **Compressed (best for WiFi)**, or connect an Ethernet cable.

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
