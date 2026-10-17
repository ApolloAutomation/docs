---
title: PRODUCTNAME general tips
description: General tips for using the PRODUCTNAME.
---
# General tips

## Fluid sensor

The fluid level sensor should be securely taped or mounted flat against the surface of your chosen water reservoir. The fluid sensor is rated to go through up to 5mm of plastic but could possibly go further.

## Pump control

There is a disabled entity by default called **Pump Control** which will turn the pump on or off and run it instead of using the **Run Pump** entity. The **Pump Control** entity will ignore the **Pump Run Seconds** however this entity is still affected by the **Max Safe Run Time**. For example, if **Max Safe Run Time** is set to 120 seconds, then when you turn on the **Pump Control** entity, it will run for 120 seconds and then turn off unless you manually turn it off sooner.