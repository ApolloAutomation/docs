---
title: TEMP-1B Alert Outside Temp Range Example
description: Step by step guide for alerting outside the set range with the TEMP-1B.
---
# TEMP-1B Alert Outside Temp Range Example

######

This will guide you through how to set up the built in alarm using the temperature probe in your freezer!

1\. Place the temperature probe into your freezer (not the entire TEMP-1B, just the probe!) and then wait for it to normalize around 0 degrees F aka -18C.

2\. Once normalized, look at the graph and determine a good value to set for both the maximum and minimum temperatures. My mini freezer seems to max out at 30F so I would want to go slightly above that range. However, <a href="https://www.fda.gov/food/buy-store-serve-safe-food/refrigerator-thermometers-cold-facts-about-food-safety" target="_blank" rel="noreferrer nofollow noopener">in most freezers they should NOT reach above 0F</a> so you will likely need to input a lower value than me. My minimums are around -20F.

![Home Assistant history graph of the TEMP-1 temperature probe with arrows at freezer highs and lows](/assets/temp-1-temp-probe-ex-automation-pic-1.png)

3\. We now need to convert F to C since the max and min temps are measured in Celsius. My new values I will input are max probe temp 2C and a min probe temp of -30C. Reminder, yours will likely be different values, especially your max probe temp.

![Home Assistant settings with Max Probe Temp set to 2.0 °C and Min Probe Temp set to -30.0 °C](/assets/temp-1-temp-probe-ex-automation-pic-2.png)

4\. Enable the "Alarm Outside Temp Range" toggle and now your TEMP-1B will play an audible alert with its buzzer when the temp thresholds are reached. If the temp goes under the min or over the max the alarm will go off

![Home Assistant Controls card with the Alarm Outside Temp Range toggle switched on](/assets/temp-1-alarm-outside-range-pic-1.png)