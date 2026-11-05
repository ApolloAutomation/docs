---
title: CAST PRO-1 FAQ
description: Frequently asked questions about the CAST PRO-1 audio caster.
---
1\. **What does the CAST PRO-1 do?**

* It adds streaming audio to speakers that aren't smart. Connect it to your speakers, receiver, or soundbar, add it to Home Assistant, and it shows up in Music Assistant as a player you can stream to.

2\. **How is it different from the CAST-1?**

* **Built-in Ethernet:** no addon module needed for a wired connection.
* **Optical output:** the output jack takes an optical cable as well as a regular 3.5mm audio cable.
* **Analog In (Line In):** a second jack for audio in, so you can play a turntable or TV through Music Assistant.
* **LED strip terminals:** screw terminals for an addressable LED strip, no soldering.

3\. **Which jack is which?**

* The left jack is **Analog In (Line In)**, audio in only. Whatever you plug in shows up in Music Assistant as a **Sendspin Source**. See [Play a source through Analog In (Line In)](additional-info/analog-in.md).
* The right jack is **Analog/Optical Out**, audio out only. It takes a 3.5mm audio cable for analog or a mini-TOSLINK optical cable for digital.
* The [Getting Started guide](setup/getting-started.md#know-your-ports) has a labeled photo of every port.

4\. **What cable do I need for optical?**

* A mini-TOSLINK to TOSLINK cable, sometimes sold as a "3.5mm optical to TOSLINK" cable. The small end looks like a 3.5mm plug and goes into the CAST PRO-1, the square end goes into your receiver or soundbar. A regular 3.5mm audio cable won't carry optical audio.
* After you plug it in, set **Audio Output** to **Optical** on the device page.

5\. **Do I need powered speakers?**

* Yes. The CAST PRO-1 has no amplifier of its own, so it needs powered speakers, a receiver, or an active soundbar.

6\. **My speakers use RCA or 6.35mm inputs, will it work?**

* Yes, with a 3.5mm-to-RCA or 3.5mm-to-6.35mm adapter cable on the **Analog/Optical Out** jack.

7\. **How do I power it?**

* With **USB-C** from a 5V supply. A 5V 1A supply is plenty. Use a quality supply and cable.
* Running an LED strip from the screw terminals? Use a 5V 3A supply instead, since the strip draws its power through the CAST PRO-1.
* The Ethernet port is for network only. It doesn't take power over Ethernet (PoE), so the CAST PRO-1 needs USB-C power even on a wired connection.

8\. **Can I use Wi-Fi instead of Ethernet?**

* Yes. Set it up through its hotspot or Improv via BLE. See the [Getting Started guide](setup/getting-started.md#connect-to-your-network).
* If it has both, it keeps both up at once, so Home Assistant doesn't lose the device while you plug or unplug the cable. Take the cable out and it goes back to Wi-Fi on its own.
* The **Network Connection** sensor on the device page shows which one is in use. It reads **Ethernet**, **WiFi**, **Ethernet + WiFi**, or **Hotspot**.
* The setup hotspot never broadcasts while an Ethernet cable is connected.

9\. **Do I need Music Assistant?**

* Music Assistant is how you stream to the CAST PRO-1 out of the box, and your CAST PRO-1 shows up there as a player automatically once Music Assistant is running. The [Getting Started guide](setup/getting-started.md#music-assistant) walks through installing it.

10\. **What can I stream to it?**

* Anything Music Assistant can play, including your local library, streaming services, and radio. Music Assistant handles the sources and sends the audio to your CAST PRO-1.
* AirPlay and Spotify Connect aren't built into the CAST PRO-1 firmware. Music Assistant has a plugin for each: <a href="https://www.music-assistant.io/plugins/airplay-receiver/" target="_blank" rel="noreferrer nofollow noopener">AirPlay Receiver</a> and <a href="https://www.music-assistant.io/plugins/spotify-connect/" target="_blank" rel="noreferrer nofollow noopener">Spotify Connect</a>, which make its players show up as AirPlay or Spotify Connect targets. Both are early in development with limited functionality, and Spotify Connect needs a Spotify Premium account.

11\. **Can I play the same music in several rooms?**

* Yes. Group your CAST PRO-1 with other CAST PRO-1s and CAST-1s in Music Assistant and they play in sync. Volume can be set for the whole group or per player.
* One room a little behind the others, for example through a soundbar? Raise that CAST PRO-1's **Static playback delay (ms)** in Music Assistant. See [Play in multiple rooms](setup/getting-started.md#play-in-multiple-rooms).

12\. **Does it need a cloud account or subscription?**

* No. Streaming runs locally through Music Assistant and Sendspin.

13\. **Can I control playback without opening an app?**

* Yes, pair a WizMote. See [WizMote Control](examples/wizmote-blueprint.md).

14\. **What are the RGB LEDs for?**

* The four onboard RGB LEDs are exposed as the **RGB Light** entity. Change the color, use the **Slow Pulse** or **Fast Pulse** effect, or turn them off entirely.
* For more light, connect an addressable LED strip to the screw terminals. See [Add an LED strip](examples/led-strip.md).

15\. **What are the two buttons on the front?**

* Both are recessed, so press them with a pin or a small screwdriver.
* The **left** button is **reset**, which restarts the device.
* The **right** button is **boot**. While the CAST PRO-1 is running, hold it for about 3 seconds for a status check on the onboard LEDs, or for 10 seconds to factory reset it. Hold it while powering up to put the CAST PRO-1 into boot mode for reflashing. See [Boot button status check and factory reset](troubleshooting/castpro1-boot-button.md).
* They're the other way round from the CAST-1, where boot is on the left.

16\. **How do I try beta firmware?**

* Set **Firmware Channel** to **Beta** on your CAST PRO-1's device page, then select **Press** next to **Firmware Update**. See [Switch to Beta Firmware](../general/setup/switch-to-beta-branch.md) for a step-by-step guide.

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
