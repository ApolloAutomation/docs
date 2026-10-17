---
title: Prevent sleep
description: "Why the USB-powered PLT-1 stays awake in Homey, what its Prevent sleep and Sleep duration settings do, and how to correct the air temperature instead."
---
# Prevent sleep

Your Apollo PLT-1 runs on USB power, but its firmware can still sleep between readings: it wakes up, reports, and goes back to sleep. Sleeping keeps the board from warming itself up, so the air temperature reads closer to the room. The PLT-1 ships with **Prevent sleep** on, so it stays awake and reports all the time.

## Sleep isn't available for the PLT-1 in Homey

In Homey, your PLT-1 stays awake. You'll see **Prevent sleep** and **Sleep duration** in your PLT-1's **Settings** in the Homey app, under **Battery settings (if battery is present)**, but the Apollo Automation app only lets you change **Prevent sleep** on a sensor with a battery. If you uncheck it on the PLT-1, Homey refuses the change and shows **Battery settings are not supported on this device.**

Staying awake is how Homey expects a USB-powered sensor to work, so there's nothing you need to change here.

!!! tip "Leave Sleep duration as it is"

    Homey shows **Sleep duration** in hours, but the PLT-1 reads the number as minutes: the default of 5 means 5 minutes. It only applies while Prevent sleep is off, so you don't need to change it in Homey.

!!! tip "Using Home Assistant too?"

    Home Assistant can turn sleep on for the PLT-1. See the [Home Assistant Prevent Sleep guide](../../../../../products/plt1/additional-info/prevent-sleep/). While the PLT-1 sleeps, Homey loses its connection between reports.

## Correct the air temperature instead

If you wanted sleep to stop the board's own warmth from nudging the air temperature up, an offset fixes the reading without it. You need a reference thermometer you trust.

1. Put the reference thermometer next to your PLT-1 and give both time to settle.
2. Compare the PLT-1's air temperature reading in Homey with the reference.
3. In your PLT-1's **Settings**, under **Calibration offsets**, set **Air temperature offset** to how many degrees Celsius the PLT-1 reads too high, and save. For example, if the PLT-1 shows 23.5 °C and the reference shows 22 °C, enter 1.5.

The PLT-1's air temperature in Homey now matches your reference thermometer. The offset only changes the air reading, not the soil temperature probe.

!!! tip "Homey set to Fahrenheit?"

    The offset is always in degrees Celsius. Divide the difference you see in °F by 1.8: a reading 2.7 °F too high is an offset of 1.5.

## If your PLT-1 was set to sleep before

If Prevent sleep was turned off earlier, for example in Home Assistant, the PLT-1 remembers it and keeps sleeping after you add it to Homey, so Homey keeps losing the connection. Homey can't change Prevent sleep on the PLT-1, so turn it back on with the boot button. [Putting the PLT-1 in boot mode](../../troubleshooting/plt1-boot-mode/) shows where the button is.

!!! warning "Don't hold the boot button while you plug in"

    Plugging in with the boot button held puts the PLT-1 in boot mode for flashing firmware instead. Also let go before 10 seconds: holding the boot button that long resets the PLT-1 to factory settings and erases its Wi-Fi.

1. Unplug the PLT-1 and plug it back in to wake it.
2. Wait a few seconds, then press and hold the boot button for 4 to 5 seconds and let go.

The PLT-1 turns Prevent sleep back on and stays connected to Homey, and **Prevent sleep** shows as checked in its settings. If Homey loses the connection again a few seconds later, the PLT-1 was already on its way back to sleep. It still remembers Prevent sleep, so unplug it and plug it back in once more, and it stays awake this time.

!!! danger "Keep the main body dry"

    The main body of the PLT-1 isn't rated for outdoor use. Don't leave it outside for long periods or let it get wet. If it will sit in damp air or could see rain, put it inside another, protective case.
