---
title: Read and write tags with the NFC-1
description: Run Home Assistant automations from NFC tag scans, write URLs, text, and Home Assistant tags, clean and format tags, and use card emulation on the Apollo NFC-1.
---
# Read and write tags with the NFC-1

Your NFC-1 does more than read tags. This guide covers running automations from a scan, writing your own tags from Home Assistant, reusing old tags, and letting phones tap the NFC-1 itself.

!!! note "Before you start"

    Add your NFC-1 to Home Assistant first. The [getting started guide](../setup/getting-started.md) walks you through it.

## Run an automation from a tag

Every tag you scan is reported to Home Assistant and listed under **Settings → Tags**. A tag that holds a Home Assistant tag is listed by that tag's ID, and any other tag by its UID.

[![Open your Home Assistant instance and show your tags.](https://my.home-assistant.io/badges/tags.svg)](https://my.home-assistant.io/redirect/tags/)

1\. Scan the tag on your NFC-1.

2\. Go to **Settings → Tags** in Home Assistant and click the tag at the top of the list. Give it a name you'll recognize, such as **Front door**.

3\. Click **Create automation** in the tag's dialog. Home Assistant starts a new automation with a **Tag** trigger for that tag.

4\. Add the actions you want, such as arming the alarm or starting a scene, then click **Save**.

The automation now runs every time that tag is scanned. In YAML, the trigger looks like this:

```yaml
triggers:
  - trigger: tag
    tag_id: your-tag-id
```

!!! tip "Phones show up as a different tag each time"

    A phone held to the NFC-1 can show up as a tag with a random UID that starts with `08-`. Because that UID changes every time, the NFC-1 doesn't report it to **Settings → Tags**. Use a real tag or card for automations.

You can also trigger on the **NFC Event** entity, for example on `tag_scanned` or `tag_removed`, and read **Last Tag**, **Last Tag UID**, or **Last Tag Content** in your automation.

## Write a tag

The NFC-1 writes a tag in three steps: you arm the write, hold a tag on the reader, and the NFC-1 reads the tag back to check it. While a write is armed, the LED pulses blue. You have 30 seconds to present a tag, which you can change with **Mode Timeout**.

!!! warning "Keep the tag on the reader until it's checked"

    After writing, the NFC-1 reads the tag again to make sure the data matches. If you lift the tag too soon, **Last Operation** reads **Write unverified (tag removed)**. Hold the tag in place until you hear the three-note chime and **Last Operation** reads **Write verified**.

### Write a Home Assistant tag

A Home Assistant tag holds a URL with a random tag ID. Phones with the Home Assistant app report it to Home Assistant when you tap them on the tag, and the NFC-1 reports it too.

1\. On the NFC-1's device page, press **Write New HA Tag**.

2\. Hold a tag flat against the NFC-1.

3\. Wait for two green flashes and the three-note chime, then check that **Last Operation** reads **Write verified**.

The new tag shows up under **Settings → Tags** right away, ready for an automation.

With **HA App Record** on (the default), the tag also tells Android phones to open the Home Assistant app when tapped.

### Write a URL

1\. Under **Configuration**, type the URL into **Write URL**. It can be up to 120 characters, which fits on an NTAG213 tag.

2\. Press **Write URL Tag**, or set **Mode** to **Write**.

3\. Hold a tag flat against the NFC-1 until **Last Operation** reads **Write verified**.

### Write text

Text tags are written with the `write_text` action. See [Use actions in automations](#use-actions-in-automations).

## Clean or format a tag

Clean a tag to remove its data so you can write it again. Press **Clean Tag**, or set **Mode** to **Clean**, then hold the tag on the reader. The LED pulses orange while a clean is armed.

**Format Tag** works the same way, and the LED pulses magenta while it's armed. On NTAG and MIFARE Ultralight tags, format does the same as clean.

Like a write, the NFC-1 reads the tag back afterward. **Last Operation** reads **Clean done (no readable data)** or **Format done (no readable data)** once it's checked.

To stop an armed write, clean, or format, press **Cancel Tag Operation** or set **Mode** back to **Read**.

## Check the result

**Last Operation** on the device page tells you how the last task went:

| Last Operation | What it means |
| --- | --- |
| **Waiting for tag** | A write, clean, or format is armed. Hold a tag on the reader. |
| **Write done, verifying** | The tag was written. Keep it on the reader while the NFC-1 checks it. |
| **Write verified** | The NFC-1 read the tag back and the data matches. |
| **Write mismatch** | The tag was read back, but the data doesn't match. Try writing it again. |
| **Write failed (tag not formatted or unsupported)** | The write didn't go through. Clean or format the tag, or try another tag. |
| **Write refused: nothing to write** | **Write URL** is empty. Fill it in and try again. |
| **Clean done (no readable data)**, **Format done (no readable data)** | The tag is empty and ready to reuse. |
| **Clean failed (data remains)**, **Format failed (data remains)** | Data is still on the tag. Try again. |
| **Write unverified (tag removed)** | The tag was lifted before the NFC-1 could check it. Scan it to see what's on it. |
| **Timed out** | No tag was presented before **Mode Timeout** ran out. |
| **Cancelled** | The task was cancelled. |
| **Emulation off: Emulation URL is empty** | **Card Emulation** was turned on without an **Emulation URL**. |

## Card emulation

With card emulation on, the NFC-1 acts as a tag. A phone tapped on it opens the link you set, with no app needed, which makes it handy for a guest page or a menu.

1\. Under **Configuration**, type the link into **Emulation URL**. It can be up to 120 characters.

2\. Turn on **Card Emulation**.

3\. Tap a phone on the NFC-1. The LED flashes cyan, the buzzer beeps twice, and **NFC Event** fires `emulated_tag_scanned`.

If the **Emulation URL** is a Home Assistant tag URL and **HA App Record** is on, Android phones open the Home Assistant app when they tap. To change the link later, edit **Emulation URL**. The NFC-1 picks it up while emulation stays on.

## Use actions in automations

The NFC-1 adds these actions to Home Assistant, so automations and scripts can write tags and set the emulated link. Each one is named after your device, for example `esphome.apollo_nfc_1_xxxxxx_write_url`, where `xxxxxx` is the end of your NFC-1's MAC address. Find yours under **Settings → Tools → Actions** by typing `nfc`.

[![Open your Home Assistant instance and show your action tools.](https://my.home-assistant.io/badges/tools_actions.svg)](https://my.home-assistant.io/redirect/tools_actions/)

| Action | Field | What it does |
| --- | --- | --- |
| `write_url` | `url` | Arms a write of a URL to the next tag. |
| `write_text` | `text_str` | Arms a write of a line of text to the next tag. |
| `write_ha_tag` | `tag_id` | Arms a write of a Home Assistant tag. Leave `tag_id` empty for a new random ID, or give an existing tag ID to make a second tag that runs the same automations. |
| `clean_tag` | none | Arms a clean of the next tag. |
| `format_tag` | none | Arms a format of the next tag. |
| `cancel_tag_operation` | none | Cancels an armed task. |
| `set_emulation_url` | `url` | Sets the **Emulation URL**. |
| `play_buzzer` | `song_str` | Plays an RTTTL tune on the buzzer. See [Piezo buzzer](../../general/piezo.md) for tunes to try. |

For example, this action arms a write of a URL to the next tag:

```yaml
action: esphome.apollo_nfc_1_xxxxxx_write_url
data:
  url: "https://wiki.apolloautomation.com"
```

## What the LED and buzzer mean

| LED | Buzzer | What happened |
| --- | --- | --- |
| One green flash | One beep | A tag was scanned. |
| One cyan flash | Two beeps | A phone read the emulated tag. |
| Pulsing blue | Two rising notes | A write is armed and waiting for a tag. |
| Pulsing orange | Two rising notes | A clean is armed and waiting for a tag. |
| Pulsing magenta | Two rising notes | A format is armed and waiting for a tag. |
| Two green flashes | Three rising notes | The write, clean, or format went through. |
| Three red flashes | Two falling notes | The task failed or the check didn't match. |
| Two orange flashes | Two beeps | The armed task timed out. |
| No change | Two falling notes | The armed task was cancelled. |

Turn the sounds off with **Buzzer** or lower them with **Volume**. Turn the flashes off with **LED Feedback** or dim them with **Feedback Brightness**.

## NFC Event types

The **NFC Event** entity fires one of these event types. Use them as triggers in automations.

| Event type | When it fires |
| --- | --- |
| `tag_scanned` | A tag was scanned in **Read** mode. |
| `tag_removed` | The scanned tag was taken off the reader. |
| `emulated_tag_scanned` | A phone read the emulated tag. |
| `armed` | A write, clean, or format was armed. |
| `written`, `cleaned`, `formatted` | The task ran, and the NFC-1 is about to check the tag. |
| `write_verified`, `clean_verified`, `format_verified` | The check passed. |
| `write_mismatch`, `clean_failed`, `format_failed` | The check found the wrong data on the tag. |
| `write_failed` | The write didn't go through, or there was nothing to write. |
| `unverified` | The tag was removed, or the task cancelled, before the check. |
| `timed_out` | No tag was presented before **Mode Timeout** ran out. |
| `cancelled` | The armed task was cancelled. |

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
