# Calibrating Soil Moisture

This guide will take you through calibrating your PLT-1's moisture sensor. The sensors come with the default calibration so this method is only needed if you want to make your own adjustments.

&nbsp;

1. Take your PLT-1 out of the soil and clean off the probe. It is important to get the dirt off to have the best calibration.
2. Make sure the PLT-1 probe is sitting in the air or on a dry non conductive surface and plugged in.
3. Visit the device's entity drill down page in Home Assistant and scroll down to the diagnostics section. Enable the entity "Soil ADC"
4. Give the sensor a minute for this new entity to populate
5. Once the value is populated take the value and put it into the "Dry Voltage" entity
6. Now place the prob portion of the PLT-1 into a cup of water. Be careful to not dunk the entire sensor, only the exposed PCB below "Apollo" and the horizontal line can be exposed to water
7. Grab the "Soil ADC" value now and put the value into the "100% Water Voltage" entity
8. You can put your PLT-1 back into your plant and you now have a calibrated