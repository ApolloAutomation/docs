---
title: CAST-1 FAQ
description: Frequently asked questions about the CAST-1 audio caster.
---
1\. **What does the CAST-1 do?**

* It adds streaming audio to speakers that aren't smart. Plug it into a 3.5mm line-in, add it to Home Assistant, and it shows up in Music Assistant as a player you can stream to.

2\. **Do I need powered speakers?**

* Yes. The CAST-1 outputs line level and has no amplifier of its own, so it needs powered speakers, a receiver, or an active soundbar.

3\. **My speakers use RCA or 6.35mm inputs, will it work?**

* Yes, with a 3.5mm-to-RCA or 3.5mm-to-6.35mm adapter cable.

4\. **What power supply does it need?**

* A 5V 1A USB-C supply is plenty. The CAST-1 is sensitive to power fluctuations and needs constant 5V, so use a quality supply and cable.

5\. **Do I need Music Assistant?**

* Music Assistant is how you stream to the CAST-1 out of the box, and your CAST-1 shows up there as a player automatically once Music Assistant is running. The [Getting Started guide](https://wiki.apolloautomation.com/products/cast1/setup/getting-started/) walks through installing it.
* A Squeezelite firmware is also on the way if you'd rather run your CAST-1 as a Squeezelite player instead.

6\. **Do I need Home Assistant?**

* Not strictly. The CAST-1 works with Music Assistant on its own, though most people run both. Home Assistant adds the device entities, text-to-speech, and announcements, and our [Getting Started guide](https://wiki.apolloautomation.com/products/cast1/setup/getting-started/) sets the CAST-1 up through it.

7\. **What can I stream to it?**

* Anything Music Assistant can play, including your local library, streaming services, and radio. Music Assistant handles the sources and sends the audio to your CAST-1.
* AirPlay and Spotify Connect aren't built into the CAST-1 firmware. Music Assistant has a plugin for each: <a href="https://www.music-assistant.io/plugins/airplay-receiver/" target="_blank" rel="noreferrer nofollow noopener">AirPlay Receiver</a> and <a href="https://www.music-assistant.io/plugins/spotify-connect/" target="_blank" rel="noreferrer nofollow noopener">Spotify Connect</a>, which make its players show up as AirPlay or Spotify Connect targets. Both are early in development with limited functionality, and Spotify Connect needs a Spotify Premium account.

8\. **Why are there two media players on my device?**

* **Apollo CAST-1 Sendspin Player** is the player Music Assistant streams to, and the one you group with other CAST-1s for multi-room audio.
* **Apollo CAST-1 Player** is the Home Assistant media player. Use it for text-to-speech and announcements, which duck the music down and bring it back when they finish. See [TTS and Announcements](https://wiki.apolloautomation.com/products/cast1/examples/tts-announcements/).

9\. **Can I play the same music in several rooms?**

* Yes. Group multiple CAST-1s in Music Assistant and they play in sync. Volume can be set for the whole group or per player.

10\. **Does it need a cloud account or subscription?**

* No. Streaming runs locally through Music Assistant and Sendspin.

11\. **Can I control playback without opening an app?**

* Yes, pair a WizMote. Each of the nine buttons is configurable in Home Assistant using the CAST-1 WizMote blueprint. See [WizMote Control](https://wiki.apolloautomation.com/products/cast1/examples/wizmote-blueprint/).

12\. **Can I connect it with an Ethernet cable instead of Wi-Fi?**

* Yes, with the [Ethernet add-on module](https://wiki.apolloautomation.com/products/cast1/addons/ethernet-module/). It's a header board that presses onto the top of the case. There's nothing to flash, one firmware covers both connections.
* Plug a cable in and your CAST-1 switches over to the wired connection. If it's also joined to your Wi-Fi it keeps both up at once, so Home Assistant doesn't lose the device while you plug or unplug the cable. Take the cable out and it goes back to Wi-Fi on its own.
* The **Network Connection** sensor on the device page shows which one is in use. It reads **Ethernet**, **WiFi**, **Ethernet + WiFi**, or **Hotspot**.
* The setup hotspot never broadcasts while an Ethernet cable is connected. Unplug the cable if you need it back.

13\. **Can I pair my phone to the CAST-1 over Bluetooth?**

* Not with the firmware it ships with today. Music reaches your CAST-1 over your network through Music Assistant instead.
* The Squeezelite firmware that's on the way adds Bluetooth support, so this will change.

14\. **What does the Bluetooth Proxy switch do then?**

* It lets the CAST-1 relay nearby Bluetooth devices back to Home Assistant, extending your Bluetooth coverage. That's for sensors and trackers, not for audio.

15\. **What are the RGB LEDs for?**

* The four onboard RGB LEDs are exposed as the **RGB Light** entity. Change the color, use the **Slow Pulse** or **Fast Pulse** effect, or turn them off entirely.

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
