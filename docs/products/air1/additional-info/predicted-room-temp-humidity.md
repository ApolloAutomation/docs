---
title: AIR-1 Predicted Room Temperature & Humidity
description: Get a more accurate room temperature and humidity from the AIR-1 by blending its three sensors and correcting for case self-heating.
---
# AIR-1 Predicted Room Temperature & Humidity

The AIR-1's own electronics warm the air inside the case, so the SEN55 and SCD40 read a little warmer and drier than the room around them. The **Predicted Room Temperature** and **Predicted Room Humidity** sensors correct for that. They blend the SEN55, DPS310, and SCD40 readings and apply a physics model to estimate what the room is actually doing.

Credit to Ellude on our Discord, who worked out the model and fitted the numbers behind these sensors.

!!! note "Requires a recent firmware"

    These sensors ship in a recent AIR-1 firmware update. <!-- Brandon: name the specific version once PR #102 merges --> If you don't see them, [update your firmware](../../general/calibrating-and-updating/updating-firmware.md) first.

## Enable the entities

The predicted sensors and their tuning controls are disabled by default, so they stay out of the way for anyone who doesn't need them. To enable one:

1\. Open **Settings** and then **Devices & Services**.

2\. Select the **ESPHome** integration, then your AIR-1 device.

3\. Scroll down and select **entities not shown**.

4\. Pick **Predicted Room Temperature**, select the gear icon, and choose **Enable**.

5\. Repeat for **Predicted Room Humidity**.

Give the AIR-1 a few minutes after enabling. The sensors hold off for the first three minutes after boot so an early, unsettled reading doesn't skew the estimate.

## Tune it to your room

The defaults work well for a typical AIR-1, but every room and mounting spot is a little different. Enable these controls the same way you enabled the sensors, then adjust them in the device page.

| Control | What it does | Default |
| --- | --- | --- |
| **Physics Multiplier P** | How strongly the case-heat correction is applied. | 0.5357 (provisional) |
| **Baseline Offset** | A flat °C nudge added to the predicted temperature. | 0 |
| **SCD40 Temperature Offset** | Trims the SCD40 temperature before it feeds the model. | 0 |
| **SCD40 Humidity Offset** | Trims the SCD40 humidity before it feeds the model. | 0 |

To dial it in:

1\. Set a trusted thermometer and hygrometer next to the AIR-1 and let everything settle for 15 to 20 minutes.

2\. Compare your reference against **Predicted Room Temperature**.

3\. If the prediction sits a steady amount off, nudge **Baseline Offset** by the difference. Reading 0.4°C high? Set Baseline Offset to -0.4.

4\. Leave **Physics Multiplier P** alone unless you want to experiment. It's still being refined, and a better default is on the way from Ellude.

!!! tip "These sit alongside the stock sensors"

    The standard **SEN55 Temperature** and **SEN55 Humidity** sensors are untouched and keep working as before. The predicted sensors run next to them, so you can compare the two and point your dashboards and automations at whichever you trust.

[Join our Discord if you need more help! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button }
