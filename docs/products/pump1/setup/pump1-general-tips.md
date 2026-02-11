---
title: PUMP-1 General Tips
description: >-
  Multiple helpful images for mounting, lux/rgb, and gate and zone
  visualization.
---
# General Tips

###### Fluid Sensor

The fluid level sensor should be securely taped or mounted flat against the surface of your chosen water reservoir. The fluid sensor is rated to go through up to 5mm of plastic but could possibly go further.

###### Pump Control

There is a disabled entity by default called **Pump Control** which will just turn the pump on or off and run it instead of using the **Run Pump** entity. The **Pump Control** entity will ignore the **Pump Run Seconds** however this entity is still effected by the **Max Safe Run Time**. For example, if **Max Safe Run Time** is set to 120 seconds, then when you turn on the **Pump Control** entity, it will run for 120 seconds and then turn off unless you manually turn it off sooner.

###### Siphon Concerns

If you plan to use the PUMP-1 with the output reservoir positioned lower than the input reservoir, please note that a siphon-like effect can occur. In this setup, small amounts of water may continue to drip even when the pump is turned off.

Depending on your application, this may not be a concern. If it is, there are many helpful resources online that explain ways to reduce or prevent this effect.

To clarify, this is not the pump actively siphoning from the source reservoir. It is simply water remaining in the outlet tubing flowing downward due to gravity when the discharge end is lower than the source.