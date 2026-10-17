---
title: Using MSR-2 Buzzer
description: "Trigger the MSR-2 buzzer from developer tools, then reuse the same call in an automation."
---
# Using MSR-2 Buzzer

This guide will walk you through using the buzzer on your MSR-2. You can also use the "action" in an automation in Home Assistant.

1. Open Home Assistant and navigate to developer tools in the bottom left

![Home Assistant sidebar with the Developer tools hammer icon highlighted](/assets/screenshot-2023-11-01-at-10-52-38-pm.png)

2\. Click Actions at the top of the page.

3\. Choose your MSR-2's buzzer (You can type in buzzer to find it easier)

4\. Put an rtttl tone into the string box

??? example "Mario"

    ```
    smb:d=4,o=5,b=100:16e6,16e6,32p,8e6,16c6,8e6,8g6,8p,8g,8p,8c6,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e6,16g6,8a6,16f6,8g6,8e6,16c6,16d6,8b,16p,8c6,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e6,16g6,8a6,16f6,8g6,8e6,16c6,16d6,8b,8p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16g#,16a,16c6,16p,16a,16c6,16d6,8p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16c7,16p,16c7,16c7,p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16g#,16a,16c6,16p,16a,16c6,16d6,8p,16d#6,8p,16d6,8p,16c6
    ```

??? example "Cantina"

    ```
    Cantina:d=4,o=5,b=250:8a,8p,8d6,8p,8a,8p,8d6,8p,8a,8d6,8p,8a,8p,8g#,a,8a,8g#,8a,g,8f#,8g,8f#,f.,8d.,16p,p.,8a,8p,8d6,8p,8a,8p,8d6,8p,8a,8d6,8p,8a,8p,8g#,8a,8p,8g,8p,g.,8f#,8g,8p,8c6,a#,a,g
    ```

??? example "Star Wars Imperial Death March"

    ```
    StarWars/Imp:d=4,o=5,b=112:8d.,16p,8d.,16p,8d.,16p,8a#4,16p,16f,8d.,16p,8a#4,16p,16f,d.,8p,8a.,16p,8a.,16p,8a.,16p,8a#,16p,16f,8c#.,16p,8a#4,16p,16f,d.,8p,8d.6,16p,8d,16p,16d,8d6,8p,8c#6,16p,16c6,16b,16a#,8b,8p,16d#,16p,8g#,8p,8g,16p,16f#,16f,16e,8f,8p,16a#4,16p,2c#
    ```

<a href="https://picaxe.com/rtttl-ringtones-for-tune-command/" title="Example RTTL Tones" target="_blank" rel="noreferrer nofollow noopener">Click here</a> to find example RTTTL Tones and <a href="https://adamonsoon.github.io/rtttl-play/" title="Test RTTTL Tones" target="_blank" rel="noreferrer nofollow noopener">click here</a> to test RTTTL Tones.

5\. Click on the Perform Action button.

![Home Assistant Developer tools Actions tab with the ESPHome MSR-2 play buzzer action and an RTTTL song entered](/assets/HJuimage.png)