---
title: MSR-2 Home Assistant Zone Configuration
description: Tutorial for MSR-2 Home Assistant Zone Configuration.
---
# How To Tune the MSR-2 Using Home Assistant

!!! tip "Prefer a guided dashboard?"

    The Apollo mmWave integration gives your Apollo MSR-2 a tuning dashboard with a Gate Energy chart and a **Calibrate with empty room** button that sets the gate thresholds for you. The [Apollo mmWave dashboard guide](/products/msr2/setup/apollo-mmwave-dashboard.md) walks you through it as a guided alternative to the manual steps below.

If you're experiencing false triggers, Radar Engineering Mode (REM) lets you monitor the gate energy and adjust the gate thresholds to eliminate them.

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

1\. Head to the <a href="http://homeassistant.local:8123/config/integrations/integration/esphome" title="Click me to go to the ESPHome integrations page" target="_blank" rel="noreferrer nofollow noopener">ESPHome Integrations page</a> and select your MSR-2.

2\. Scroll down to the Configuration section and turn on "Radar Engineering Mode".

![Home Assistant MSR-2 Configuration section with the Radar Engineering Mode toggle being switched on](/assets/msr-2-toggle-on-rem-1.png)

3\. Scroll down to the Diagnostic section and you will see that when REM is enabled, the move and still energy for gates 0-8 are shown.

![Home Assistant MSR-2 Diagnostic section listing move and still energy percentages for gates g0 to g4](/assets/msr-2-gate-energies.png)

The gates are 0.75meter increments from the sensor - allowing you to "tune" each 0.75 meter section until your sensor works as intended!

![Table of LD2410 gates 0 to 8 with distance ranges and default move and still thresholds](/assets/msr-2-ld2410-gate-table.png)

![Diagram of the LD2410 detection area split into gates at 0.75 m steps](/assets/msr-2-ld2410-gates-visualized.png)

Moving the gate still and move threshold slider to the right increases the amount of energy needed to trigger the sensor. Do this if you want the gate to be less sensitive.

![Gate 0 move and still threshold sliders moved all the way right to 100](/assets/msr-2-gate-high-threshold-example.png)

Moving the gate still and move threshold slider to the left decreases the amount of energy needed to trigger the sensor. Do this if you want the gate to be more sensitive.

![Gate 0 move and still threshold sliders moved all the way to the left](/assets/msr-2-gate-low-threshold-example.png)