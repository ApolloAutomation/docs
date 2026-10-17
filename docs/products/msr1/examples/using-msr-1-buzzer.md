---
title: Using MSR-1 Buzzer
description: "Trigger the MSR-1 buzzer from Home Assistant developer tools, then reuse the same call in an automation."
---
# Using MSR-1 Buzzer

This guide will walk you through using the buzzer on your MSR-1. You can also use the action below in Home Assistant automations.

1\. Open Home Assistant and navigate to **Developer tools** in the bottom left (**Settings → Tools** in Home Assistant 2026.8 and newer).

[![Open your Home Assistant instance and show your action tools.](https://my.home-assistant.io/badges/tools_actions.svg)](https://my.home-assistant.io/redirect/tools_actions/)

![Home Assistant sidebar with the Developer tools hammer icon highlighted in orange](/assets/screenshot-2023-11-01-at-10-52-38-pm.png)

2\. Click **Actions** at the top of the page.

3\. Choose your MSR-1's buzzer (You can type in buzzer to find it easier)

4\. Put a rtttl tone into the string box

??? example "Mario"

    ```
    smb:d=4,o=5,b=100:16e6,16e6,32p,8e6,16c6,8e6,8g6,8p,8g,8p,8c6,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e6,16g6,8a6,16f6,8g6,8e6,16c6,16d6,8b,16p,8c6,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e6,16g6,8a6,16f6,8g6,8e6,16c6,16d6,8b,8p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16g#,16a,16c6,16p,16a,16c6,16d6,8p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16c7,16p,16c7,16c7,p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16g#,16a,16c6,16p,16a,16c6,16d6,8p,16d#6,8p,16d6,8p,16c6
    ```

??? example "Cantina"

    ```
    Cantina:d=4,o=5,b=250:8a,8p,8d6,8p,8a,8p,8d6,8p,8a,8d6,8p,8a,8p,8g#,a,8a,8g#,8a,g,8f#,8g,8f#,f.,8d.,16p,p.,8a,8p,8d6,8p,8a,8p,8d6,8p,8a,8d6,8p,8a,8p,8g#,8a,8p,8g,8p,g.,8f#,8g,8p,8c6,a#,a,g
    ```

<a href="https://picaxe.com/rtttl-ringtones-for-tune-command/">Click here</a> to find example RTTTL tones and <a href="https://adamonsoon.github.io/rtttl-play/">click here</a> to test them.

5\. Click the **Perform action** button in the bottom right.

![Developer tools Services tab with the MSR-1 play_buzzer service and an RTTTL song_str highlighted](/assets/screenshot-2023-11-01-at-10-57-33-pm.png)