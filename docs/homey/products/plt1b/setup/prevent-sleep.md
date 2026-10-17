---
title: Prevent sleep
description: "Let the PLT-1B sleep between readings to save battery, or keep it awake, with the Prevent sleep and Sleep duration settings in Homey."
---
# Prevent sleep

Your Apollo PLT-1B can sleep between readings: it wakes up, reports to Homey, and goes back to sleep until the next report. Sleeping is what makes the battery last. It also keeps the board from warming itself up, so the air temperature readings need less offset.

The PLT-1B ships with **Prevent sleep** turned on, so it stays awake and reports all the time. That's handy while you set it up, but it drains the battery far faster. Once the sensor is in its pot, turn Prevent sleep off and let it sleep.

!!! note "Before you start"

    - Add your PLT-1B to Homey. See [Getting started](../getting-started-plt1/).
    - Homey can only change these settings while the sensor is awake and connected. If it's asleep, Homey shows **The device is asleep. Settings can be changed when it next wakes up.** In that case, [keep it awake](#keep-your-plt-1b-awake-again) first.

## The sleep settings in Homey

Both settings sit in your PLT-1B's **Settings** in the Homey app, under **Battery settings (if battery is present)**. They're device settings only, so there's no flow card that turns sleep on or off.

| Setting | What it does |
| --- | --- |
| **Prevent sleep** | Checked, the sensor stays awake. Unchecked, it sleeps between reports. A new PLT-1B has it checked. |
| **Sleep duration** | How many hours the sensor sleeps between reports, from 0 to 800, with up to two decimals: 0.5 is 30 minutes. The default is 12. |

## Let your PLT-1B sleep

Set how long the sensor sleeps first, then let it go to sleep. Make the two changes one at a time: the sensor falls asleep the moment Prevent sleep turns off, so a change sent along with it may never arrive.

!!! warning "Read this before you uncheck Prevent sleep"

    The PLT-1B goes to sleep as soon as Prevent sleep is off, and Homey can't reach it again until it wakes up. Put the sensor where you want it and finish any other settings, such as soil calibration, first.

1. In the Homey app, open your PLT-1B's **Settings**.
2. Under **Battery settings (if battery is present)**, set **Sleep duration** to the hours you want between reports, and save the change. Leave it at 12 unless you need fresher readings.
3. Uncheck **Prevent sleep** and save.

Your PLT-1B is now asleep. It wakes up after each Sleep duration, connects to Homey, sends fresh readings, and goes back to sleep about 20 seconds after it connects.

!!! tip "Device disconnected is normal between reports"

    While the PLT-1B sleeps, Homey shows it as **Device disconnected**. That's expected: Homey reconnects on its own each time the sensor wakes up.

## Keep your PLT-1B awake again

To change a setting, calibrate the soil readings, update the firmware, or troubleshoot, the sensor has to stay awake. Turn Prevent sleep back on from the sensor itself or from the Homey app.

### With the buttons on the sensor

The buttons work even when Homey can't reach the sensor, which makes this the most reliable way. The [sensor connection check](../../battery-sensors/sensor-connection-check/) has photos of the reset and boot buttons.

!!! warning "Watch how long you hold the boot button"

    Hold the boot button for 4 to 5 seconds, no longer. Holding it for 10 seconds or more resets the PLT-1B to factory settings and erases its Wi-Fi, and you'd have to [connect it to Wi-Fi](../getting-started-plt1/) again. A short press of under 3 seconds runs the connection check instead.

1. Press and release the reset button to wake the sensor. You can also take the battery out and put it back in.
2. Wait a few seconds, then press and hold the boot button for 4 to 5 seconds and let go.

The sensor turns Prevent sleep on and stays awake. In Homey, **Prevent sleep** shows as checked again once the sensor is connected. If Homey loses the connection again a few seconds later, the sensor was already on its way back to sleep. It still remembers Prevent sleep, so press the reset button once more and it stays awake this time.

### From the Homey app

The sensor stays awake for only about 20 seconds after Homey connects, so have the Homey app open and ready before you start.

1. Wake the sensor with the reset button, or take the battery out and put it back in.
2. In the Homey app, open your PLT-1B and wait until it no longer shows **Device disconnected**.
3. Right away, open its **Settings**, check **Prevent sleep** under **Battery settings (if battery is present)**, and save.
4. If Homey loses the connection again a few seconds later, press the reset button once more.

Your PLT-1B now stays awake until you uncheck Prevent sleep again. If the sensor was already on its way back to sleep at step 3, it still keeps the change and starts up with Prevent sleep on after the reset in step 4. If Homey shows **The device is asleep. Settings can be changed when it next wakes up.** instead, the change didn't reach the sensor: start again from step 1, or use the buttons.

!!! danger "Keep the main body dry"

    The main body of the PLT-1B isn't rated for outdoor use. Don't leave it outside for long periods or let it get wet. If it will sit in damp air or could see rain, put it inside another, protective case.

!!! success "Next step: check your sensor's connection"

    Not sure whether your PLT-1B woke up and reached Homey? The light on the sensor tells you in a few seconds.

    [Run the sensor connection check](../../battery-sensors/sensor-connection-check/){ .md-button .md-button--primary }
