---
title: Using the MSR-1 buzzer
description: "Play a tune on the MSR-1 buzzer from Home Assistant's action tools, then reuse the same action in an automation."
---
# Using the MSR-1 buzzer

Your Apollo MSR-1 has an onboard piezo buzzer that can play short tunes. In this guide, you play one from Home Assistant to hear it for yourself. Once it works, you can use the same action in your Home Assistant automations.

1\. Open Home Assistant and go to **Developer tools** in the bottom left of the sidebar (**Settings → Tools** in Home Assistant 2026.8 and newer).

[![Open your Home Assistant instance and show your action tools.](https://my.home-assistant.io/badges/tools_actions.svg)](https://my.home-assistant.io/redirect/tools_actions/)

![Home Assistant sidebar with the Developer tools hammer icon highlighted in orange](/assets/screenshot-2023-11-01-at-10-52-38-pm.png)

2\. Click **Actions** at the top of the page. Older Home Assistant versions call this tab **Services**.

3\. Choose your MSR-1's buzzer action. Start typing `buzzer` to find it faster.

4\. Paste an RTTTL tune into the `song_str` field. RTTTL is a plain-text ringtone format. Expand one of the two samples below and copy it:

??? example "Mario"

    ```
    smb:d=4,o=5,b=100:16e6,16e6,32p,8e6,16c6,8e6,8g6,8p,8g,8p,8c6,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e6,16g6,8a6,16f6,8g6,8e6,16c6,16d6,8b,16p,8c6,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e6,16g6,8a6,16f6,8g6,8e6,16c6,16d6,8b,8p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16g#,16a,16c6,16p,16a,16c6,16d6,8p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16c7,16p,16c7,16c7,p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16g#,16a,16c6,16p,16a,16c6,16d6,8p,16d#6,8p,16d6,8p,16c6
    ```

??? example "Cantina"

    ```
    Cantina:d=4,o=5,b=250:8a,8p,8d6,8p,8a,8p,8d6,8p,8a,8d6,8p,8a,8p,8g#,a,8a,8g#,8a,g,8f#,8g,8f#,f.,8d.,16p,p.,8a,8p,8d6,8p,8a,8p,8d6,8p,8a,8d6,8p,8a,8p,8g#,8a,8p,8g,8p,g.,8f#,8g,8p,8c6,a#,a,g
    ```

Find more tunes in <a href="https://picaxe.com/rtttl-ringtones-for-tune-command/">this list of RTTTL ringtones</a>, and test them in <a href="https://adamonsoon.github.io/rtttl-play/">an online RTTTL player</a> before you send them to your MSR-1.

5\. Click the **Perform action** button in the bottom right.

![Home Assistant Actions tab with the MSR-1 play_buzzer action, a Mario RTTTL tune in song_str, and the Perform action button highlighted](/assets/msr-1-play-buzzer-action.png)

Your MSR-1 plays the tune.

!!! tip "Play a tune from an automation"

    The same action works in your Home Assistant automations. When you build an automation, add an action, choose your MSR-1's buzzer action, and paste the tune into the `song_str` field.
