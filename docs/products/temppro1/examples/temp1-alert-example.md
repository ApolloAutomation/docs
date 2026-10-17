---
title: TEMP-1 alert outside temp range example
description: Step-by-step guide to setting up the TEMP-1's built-in alarm so its buzzer sounds when the probe temperature goes outside the range you set.
---
# TEMP-1 alert outside temp range example

<span class="difficulty lvl-1">Difficulty: Level 1</span>

!!! note "Written for the TEMP-1"

    This example was written for the Apollo TEMP-1, and its steps and screenshots show a TEMP-1. The [TEMP Pro-1 sensor definitions](../../setup/temp-pro-1-sensor-definitions/) list the same **Max Probe Temp**, **Min Probe Temp**, and **Alarm Outside Temp Range** settings, so you can follow along with your TEMP Pro-1.

Set up the built-in alarm so your TEMP-1 sounds its buzzer when the temperature probe in your freezer reads outside the range you choose. You'll pick a range from the probe's readings, enter it on the device, and turn the alarm on.

1\. Place the temperature probe into your freezer, then wait for its reading to settle around 0°F (-18°C). Only the probe goes in the freezer, not the entire TEMP-1.

2\. Once the reading settles, look at the graph and pick a good value for both the maximum and the minimum temperature. In this example, the mini freezer seems to max out at 30°F, so the maximum goes slightly above that. However, <a href="https://www.fda.gov/food/buy-store-serve-safe-food/refrigerator-thermometers-cold-facts-about-food-safety" target="_blank" rel="noreferrer nofollow noopener">most freezers should not reach above 0°F</a>, so you'll likely need a lower maximum than this one. The minimums here are around -20°F.

![Home Assistant history graph of the TEMP-1 temperature probe, arrows at freezer highs and lows](/assets/temp-1-temp-probe-ex-automation-pic-1.png)

3\. Convert your maximum and minimum from °F to °C, then enter them in **Max Probe Temp** and **Min Probe Temp**. Both settings are measured in Celsius. This example uses a max probe temp of 2°C and a min probe temp of -30°C. Your values will likely be different, especially your max probe temp.

![TEMP-1 Max Probe Temp set to 2.0 °C and Min Probe Temp set to -30.0 °C](/assets/temp-1-temp-probe-ex-automation-pic-2.png)

4\. Turn on the **Alarm Outside Temp Range** toggle. Your TEMP-1 now plays an audible alert with its buzzer when the temperature thresholds are reached: if the temperature goes under the min or over the max, the alarm goes off.

![Alarm Outside Temp Range toggle switched on in the TEMP-1 Controls card](/assets/temp-1-alarm-outside-range-pic-1.png)

Your freezer alarm is set. The next time the probe reads outside your range, the TEMP-1 lets you know with its buzzer.
