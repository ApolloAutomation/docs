---
title: mmWave tuning videos
description: Two short videos and a quick summary on how to best tune the LD2410B in the MSR-2!
---
!!! tip "Radar Engineering Mode (REM)"

    If you're experiencing false triggers, we recommend using Radar Engineering Mode (REM) to monitor the gate energy and adjust the gate threshold to eliminate them.
    
Quick introduction video of the LD2410B gates and zones.

<div class="cms-embed">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/6VrTfaFyMPk?si=KI9gcbJB0EgAT3uW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen="">
  </iframe>
</div>

How to tune the mmWave sensor using radar engineering mode.

<div class="cms-embed">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/w_Gq62Edsnc?si=IxNE-pt-3u2FHMzT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen="">
  </iframe>
</div>

To tune your sensor, you'll turn on Radar Engineering Mode and adjust the gate thresholds.

1\. Go to **Settings → Devices & services → ESPHome** and click the name of your device.

[![Open your Home Assistant instance and show an integration.](https://my.home-assistant.io/badges/integration.svg)](https://my.home-assistant.io/redirect/integration/?domain=esphome)

2\. Scroll down to the Configuration section.

3\. Turn on Radar Engineering Mode (REM).

![MSR-2 Configuration card in Home Assistant with the Radar Engineering Mode toggle turned on and circled](/assets/mmwave-tuning-pic-1.png)

4\. Scroll down to the Diagnostic section and you will see that REM shows the move and still energy for gates 0-8.

![Diagnostic entities in Home Assistant showing gate move and still energy percentages](/assets/mmwave-tuning-pic-2-1.png)

5\. The gates are different distances from the sensor.

![Radar Gates Colored](/assets/radar-gates-colored.png "Radar Gates Colored")

6\. Moving the gate still and move threshold slider to the right increases the amount of energy needed to trigger the sensor. Do this if you want the gate to be less sensitive.

![MSR-2 gate threshold sliders in Home Assistant with the g6 still threshold slider moved fully right and circled](/assets/mmwave-tuning-pic-3.png)

7\. Moving the gate still and move threshold slider to the left decreases the amount of energy needed to trigger the sensor. Do this if you want the gate to be more sensitive.

![MSR-2 gate threshold sliders in Home Assistant with the g4 move threshold slider moved left and circled](/assets/mmwave-tuning-pic-4.png)

!!! quote "Quote from popular YouTuber Make It Work Tech"

    I ended up maxing out the sliders on all gates and then bringing them down just enough to pick up human presence. Definitely easier than using the LD2410B app. - <a href="https://www.youtube.com/@makeitworktech" title="Make it Work" target="_blank" rel="noreferrer nofollow noopener">MakeItWorkTech</a>

!!! example "Open-Concept kitchen and living room with MSR-2 to activate the under-cabinet lights only when person in the kitchen"

    Here's how you tune the gates so the kitchen lights only come on when you're in the kitchen.

    1. Stand in the desired trigger locations.
    2. Observe the gate energy.
    3. Adjust the gate threshold slider to the right, increasing the energy required to trigger the mmWave sensor. This ensures that your kitchen lights only come on when you're actually in the kitchen, not just walking by in the living room. Also, you can lower the gate threshold in the kitchen by moving the slider to the left. This makes the mmWave sensor more sensitive, even when standing still. This way, you avoid having the lights go off while reading a recipe or doing the dishes.

**<u>References</u>**

* [https://youtu.be/dAzHXpP3FcI?t=431](https://youtu.be/dAzHXpP3FcI?t=431)
* [https://community.home-assistant.io/t/ld2410-esphome-tips/477058/316](https://community.home-assistant.io/t/ld2410-esphome-tips/477058/316)
* [https://www.youtube.com/watch?v=l212Lvo1R6s](https://www.youtube.com/watch?v=l212Lvo1R6s)