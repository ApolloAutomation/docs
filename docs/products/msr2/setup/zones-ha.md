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

1\. Head to the **ESPHome** integration page (**Settings → Devices & services → ESPHome**) and select your MSR-2.

[![Open your Home Assistant instance and show an integration.](https://my.home-assistant.io/badges/integration.svg)](https://my.home-assistant.io/redirect/integration/?domain=esphome)

2\. Scroll down to the Configuration section and turn on "Radar Engineering Mode".

![Home Assistant MSR-2 Configuration section with the Radar Engineering Mode toggle being switched on](/assets/msr-2-toggle-on-rem-1.png)

3\. Scroll down to the Diagnostic section and you will see that when REM is enabled, the move and still energy for gates 0-8 are shown.

![Home Assistant MSR-2 Diagnostic section listing move and still energy percentages for gates g0 to g4](/assets/msr-2-gate-energies.png)

The gates are 0.75 meter increments from the sensor - allowing you to "tune" each 0.75 meter section until your sensor works as intended!

| Gate | Distance (m / ft) | Default move threshold | Default still threshold |
|---|---|---|---|
| 0 | 0 m / 0' | 50 | 0 |
| 1 | 0 - 0.75 m / 0' - 2.46' | 50 | 0 |
| 2 | 0.75 - 1.5 m / 2.46' - 4.92' | 40 | 40 |
| 3 | 1.5 - 2.25 m / 4.92' - 7.38' | 40 | 40 |
| 4 | 2.25 - 3 m / 7.38' - 9.84' | 40 | 40 |
| 5 | 3 - 3.75 m / 9.84' - 12.30' | 40 | 40 |
| 6 | 3.75 - 4.5 m / 12.30' - 14.76' | 30 | 15 |
| 7 | 4.5 - 5.25 m / 14.76' - 17.22' | 30 | 15 |
| 8 | 5.25 - 6 m / 17.22' - 19.69' | 30 | 15 |

![Fan diagram of LD2410 gates G1 to G8, each 0.75 m deep, reaching 6 m (19.69 ft) from the sensor](/assets/ld2410-gate-map.png)

Moving the gate still and move threshold slider to the right increases the amount of energy needed to trigger the sensor. Do this if you want the gate to be less sensitive.

![Gate 0 move and still threshold sliders moved all the way right to 100](/assets/msr-2-gate-high-threshold-example.png)

Moving the gate still and move threshold slider to the left decreases the amount of energy needed to trigger the sensor. Do this if you want the gate to be more sensitive.

![Gate 0 move and still threshold sliders moved all the way to the left](/assets/msr-2-gate-low-threshold-example.png)