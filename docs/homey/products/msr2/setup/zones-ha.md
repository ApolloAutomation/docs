---
title: How To Tune mmWave Using Home Assistant
description: "Tune the MSR-2 mmWave radar using Radar Engineering Mode to find which gates cause false triggers and raise their thresholds."
---
# How To Tune mmWave Using Home Assistant

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

1. Open Home Assistant
2. Navigate to Settings>Devices & services>ESPHome>Select the MSR-2
3. Scroll down to the Configuration section
4. Turn on Radar Engineering Mode (REM)  
    ![Home Assistant MSR-2 Configuration section with the Radar Engineering Mode toggle being switched on](/assets/msr-2-toggle-on-rem-1.png)
5. Scroll down to the Diagnostic section and you will see that REM shows the move and still energy for gates 0-8  
    ![Diagnostic card listing move and still energy percentages for gates 0 to 8](/assets/diagnostic.png)
6. The gates are different distances from the sensor

    | Gate | Distance | Default move threshold | Default still threshold |
    |---|---|---|---|
    | 0 | 0 m / 0 ft | 50 | 0 |
    | 1 | 0-0.75 m / 0-2.46 ft | 50 | 0 |
    | 2 | 0.75-1.5 m / 2.46-4.92 ft | 40 | 40 |
    | 3 | 1.5-2.25 m / 4.92-7.38 ft | 40 | 40 |
    | 4 | 2.25-3 m / 7.38-9.84 ft | 40 | 40 |
    | 5 | 3-3.75 m / 9.84-12.30 ft | 40 | 40 |
    | 6 | 3.75-4.5 m / 12.30-14.76 ft | 30 | 15 |
    | 7 | 4.5-5.25 m / 14.76-17.22 ft | 30 | 15 |
    | 8 | 5.25-6 m / 17.22-19.69 ft | 30 | 15 |

    ![Fan diagram of LD2410 gates G1 to G8, each 0.75 m deep, reaching 6 m (19.69 ft) from the sensor](/assets/ld2410-gate-map.png)

7. Moving the gate still and move threshold slider to the right increases the amount of energy needed to trigger the sensor. Do this if you want the gate to be less sensitive.  
    ![g0 move and still threshold sliders pushed all the way to the right](/assets/high-threshold.png)
8. Moving the gate still and move threshold slider to the left decreases the amount of energy needed to trigger the sensor. Do this if you want the gate to be more sensitive.  
    ![g0 move and still threshold sliders pushed all the way to the left](/assets/low-threshold.png)

**Alternate Method**

Thanks to [MakeItWorkTech](https://www.youtube.com/@makeitworktech) for this method!

"I ended up maxing out the sliders on all gates and then bringing them down just enough to pick up human presence. Definitely easier than using the LD2410B app."

**Example**

\- You may have an open-concept kitchen and living room, and you want the MSR-2 to activate your under-cabinet lights only when you're in the kitchen.

Here's how:

1. Stand in the desired trigger locations.
2. Observe the gate energy.
3. Adjust the gate threshold slider to the right, increasing the energy required to trigger the mmWave sensor. This ensures that your kitchen lights only come on when you're actually in the kitchen, not just walking by in the living room. Also, you can lower the gate threshold in the kitchen by moving the slider to the left. This makes the mmWave sensor more sensitive, even when standing still. This way, you avoid having the lights go off while reading a recipe or doing the dishes.

\- From clarinetJWD, "Engineering mode is what I was missing at first. I did exactly that, and now detection is basically perfect! My under cabinet lights now come on to max brightness whenever someone is in the kitchen, and return to their previous value when they leave. Next up is replacing the really flaky motion switch in my garage so it stops shutting off when I'm doing a project at the workbench! Thanks, these are really good.

**References**

- [https://youtu.be/dAzHXpP3FcI?t=431](https://youtu.be/dAzHXpP3FcI?t=431)
- [https://community.home-assistant.io/t/ld2410-esphome-tips/477058/316](https://community.home-assistant.io/t/ld2410-esphome-tips/477058/316)
- [https://www.youtube.com/watch?v=l212Lvo1R6s](https://www.youtube.com/watch?v=l212Lvo1R6s)