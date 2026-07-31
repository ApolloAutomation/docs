---
title: CAST-1 TTS and Announcements
description: Send text-to-speech and announcements to your CAST-1, with music ducking automatically.
---
# TTS and Announcements

Your CAST-1 can speak. Send it a text-to-speech message and it plays over whatever is already going, ducking the music down and bringing it back when it's done. Nothing stops or resumes, the two run at once.

You'll need a text-to-speech engine set up in Home Assistant first. The examples below use <a href="https://www.home-assistant.io/voice_control/voice_remote_local_assistant/" target="_blank" rel="noreferrer nofollow noopener">Piper</a>, which runs locally and sounds good, but any engine works since the CAST-1 just plays what Home Assistant sends it.

### Which Player to Use

Your CAST-1 has two media players and only one of them handles announcements.

* **Apollo CAST-1 Player** is the one you want. It has the announcement pipeline.
* **Apollo CAST-1 Sendspin Player** is the Music Assistant streaming target. Send an announcement here and it won't duck your music.

### Send an Announcement

1\. Open **Developer Tools** in Home Assistant and go to the **Actions** tab.

2\. Switch to YAML mode and paste this: (1)
{ .annotate }

1.  The number in the entity ID comes from your CAST-1's MAC address, so yours won't be `722124`. Copy the real one from your device page in Home Assistant.

```yaml
action: tts.speak
target:
  entity_id: tts.piper
data:
  media_player_entity_id: media_player.apollo_cast_1_722124_apollo_cast_1_player
  message: Testing announcements on the CAST dash one
```

3\. Run it with music playing and you'll hear the music drop, the message play, then the music come back.

### What Happens During an Announcement

The CAST-1 ducks the music by 40 dB the instant an announcement starts, so speech stays clear without the music stopping. The onboard LEDs turn cyan while it's talking. When the message finishes, the music fades back over a second and the LEDs go out.

That LED change is a handy way to tell an announcement from a glitch when you're across the room.

### Announce a Sound Instead of Speech

Anything you can play can be an announcement, not just speech. A doorbell chime works the same way, ducking the music and lighting the LEDs:

```yaml
action: media_player.play_media
target:
  entity_id: media_player.apollo_cast_1_722124_apollo_cast_1_player
data:
  media_content_id: media-source://media_source/local/doorbell.mp3
  media_content_type: music
  announce: true
```

The `announce: true` is what routes it to the announcement pipeline. Leave it out and the sound replaces your music instead of playing over it.

### Use It in an Automation

??? example "Announce when the washing machine finishes"

    ```yaml
    alias: Announce laundry done
    triggers:
      - trigger: state
        entity_id: sensor.washing_machine_status
        to: "off"
        for:
          minutes: 2
    actions:
      - action: tts.speak
        target:
          entity_id: tts.piper
        data:
          media_player_entity_id: media_player.apollo_cast_1_722124_apollo_cast_1_player
          message: The washing machine is finished
    mode: single
    ```

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
