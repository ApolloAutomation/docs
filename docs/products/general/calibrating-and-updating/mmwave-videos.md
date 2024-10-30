If you're experiencing false triggers, we recommend using Radar Engineering Mode (REM) to monitor the gate energy and adjust the gate threshold to eliminate them.<br><br>Here is a quick introduction video of the ld2410b gates and zones.

<div class="cms-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/6VrTfaFyMPk?si=KI9gcbJB0EgAT3uW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen=""></iframe></div>

Here is a video of how to tune the mmWave sensor using radar engineering mode,

<div class="cms-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/6VrTfaFyMPk?si=KI9gcbJB0EgAT3uW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen=""></iframe></div>

1. Open Home Assistant
2. Navigate to Settings&gt;Devices & services&gt;ESPHome&gt;Select the MSR-2
3. Scroll down to the Configuration section
4. Turn on Radar Engineering Mode (REM)<br><a href="https://wiki.apolloautomation.cloud/uploads/images/gallery/2023-11/5l4configuration.png" target="_blank" rel="noopener"><img src="https://wiki.apolloautomation.cloud/uploads/images/gallery/2023-11/scaled-1680-/5l4configuration.png" alt="Configuration.png" height="1723" width="300" /></a>
5. Scroll down to the Diagnostic section and you will see that REM shows the move and still energy for gates 0-8<br><a href="https://wiki.apolloautomation.cloud/uploads/images/gallery/2023-11/diagnostic.png" target="_blank" rel="noopener"><img src="https://wiki.apolloautomation.cloud/uploads/images/gallery/2023-11/scaled-1680-/diagnostic.png" alt="Diagnostic.png" height="1205" width="300" /></a>
6. The gates are different distances from the sensor<br><a href="https://wiki.apolloautomation.cloud/uploads/images/gallery/2023-11/ld2410-table.png" target="_blank" rel="noopener"><img src="https://wiki.apolloautomation.cloud/uploads/images/gallery/2023-11/scaled-1680-/ld2410-table.png" alt="ld2410 table.png" height="450" width="600" /></a><a href="https://wiki.apolloautomation.cloud/uploads/images/gallery/2024-01/msr-1-radar-map.png" target="_blank" rel="noopener"><img src="https://wiki.apolloautomation.cloud/uploads/images/gallery/2024-01/scaled-1680-/msr-1-radar-map.png" alt="MSR-1 radar map.png" /></a>
7. Moving the gate still and move threshold slider to the right increases the amount of energy needed to trigger the sensor. Do this if you want the gate to be less sensitive.<br><a href="https://wiki.apolloautomation.cloud/uploads/images/gallery/2023-11/high-threshold.png" target="_blank" rel="noopener"><img src="https://wiki.apolloautomation.cloud/uploads/images/gallery/2023-11/scaled-1680-/high-threshold.png" alt="High Threshold.png" /></a>
8. Moving the gate still and move threshold slider to the left decreases the amount of energy needed to trigger the sensor. Do this if you want the gate to be more sensitive.<br><a href="https://wiki.apolloautomation.cloud/uploads/images/gallery/2023-11/low-threshold.png" target="_blank" rel="noopener"><img src="https://wiki.apolloautomation.cloud/uploads/images/gallery/2023-11/scaled-1680-/low-threshold.png" alt="Low Threshold.png" /></a>

**<u>Alternate Method</u>**

Thanks to [MakeItWorkTech](https://www.youtube.com/@makeitworktech) for this method!

"I ended up maxing out the sliders on all gates and then bringing them down just enough to pick up human presence. Definitely easier than using the LD2410B app."

**<u>Example</u>**

\- You may have an open-concept kitchen and living room, and you want the MSR-1 to activate your under-cabinet lights only when you're in the kitchen.

Here's how:

1. Stand in the desired trigger locations.
2. Observe the gate energy.
3. Adjust the gate threshold slider to the right, increasing the energy required to trigger the mmWave sensor. This ensures that your kitchen lights only come on when you're actually in the kitchen, not just walking by in the living room. Also, you can lower the gate threshold in the kitchen by moving the slider to the left. This makes the mmWave sensor more sensitive, even when standing still. This way, you avoid having the lights go off while reading a recipe or doing the dishes.

\- From clarinetJWD, "Engineering mode is what I was missing at first. I did exactly that, and now detection is basically perfect! My under cabinet lights now come on to max brightness whenever someone is in the kitchen, and return to their previous value when they leave. Next up is replacing the really flaky motion switch in my garage so it stops shutting off when I'm doing a project at the workbench! Thanks, these are really good.

**<u>References</u>**

* [https://youtu.be/dAzHXpP3FcI?t=431](https://youtu.be/dAzHXpP3FcI?t=431)
* [https://community.home-assistant.io/t/ld2410-esphome-tips/477058/316](https://community.home-assistant.io/t/ld2410-esphome-tips/477058/316)
* [https://www.youtube.com/watch?v=l212Lvo1R6s](https://www.youtube.com/watch?v=l212Lvo1R6s)