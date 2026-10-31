---
title: Tune your radar with the Apollo mmWave dashboard
description: Check the radar's settings, calibrate the radar in your Apollo MSR-1 or MSR-2, or the optional LD2412 addon in your R PRO-1, against an empty room, fine-tune each gate, and draw R PRO-1 and MTR-1 zones from the Apollo mmWave dashboard in Home Assistant.
---

# Tune your radar with the Apollo mmWave dashboard

The Apollo mmWave dashboard puts every setting your radar has on one screen, with live charts that show what the radar sees. On an Apollo MSR-1, Apollo MSR-2, or Apollo R PRO-1 with the optional LD2412 radar addon, it can teach the radar what your empty room looks like in about a minute and a half, so it stops reacting to the room itself and starts reacting to people. On an R PRO-1 or an Apollo MTR-1 it is also where you draw occupancy zones on a map of the room.

Every tab starts with a **Start here** card that lists your sensor's first steps in order, and this guide follows the same order: check the **Radar setup** card, calibrate, set how far the radar looks and how long presence stays on, then fine-tune by hand. If you only do one thing today, press **Calibrate with empty room** and leave the room: [Calibrate with an empty room](#calibrate-with-an-empty-room) shows what to expect. On an MTR-1, or an R PRO-1 without the LD2412, go straight to [drawing zones](#draw-zones-on-the-r-pro-1-and-mtr-1).

Here's the **Start here** card on an MSR-1. On an MTR-1, or an R PRO-1 without the LD2412, it lists three zone map steps instead, and on an R PRO-1 with the LD2412 it covers both radars.

![The Start here card for an MSR-1 named MSR-1 Kitchen, with five numbered steps: fix anything the Radar setup card flags, press Calibrate with empty room, set Max Move Gate and Max Still Gate (each gate is about 2.5 ft), set Radar Timeout, and walk the room while you watch the Gate Energy chart, followed by the Full tuning guide and All settings for this device links](/assets/apollo-mmwave-start-here.png)

!!! note "Before you start"

    - The Apollo mmWave integration is installed and its **Apollo mmWave** dashboard is in your Home Assistant sidebar. If it isn't, sign in as an administrator (from Apollo mmWave 2.2.6, the dashboard is for administrators only unless you unticked that box), or follow the [Apollo mmWave dashboard setup guide](apollo-mmwave-dashboard-setup.md) to add it.
    - This guide shows Apollo mmWave 2.3.0. On an older version some cards look different, so [update it](apollo-mmwave-dashboard-setup.md#upgrade-from-an-older-setup) first.
    - Your radar is online in Home Assistant through ESPHome.
    - Your sensor is mounted where it will stay. A calibration, and the zones you draw, describe the room from the sensor's position, so moving the sensor later means calibrating again or redrawing your zones.
    - A calibration needs the room empty for about a minute and a half: people and pets out, robot vacuum docked.

## How radar tuning works

The radar splits the space in front of it into distance bands called *gates*. G0 sits right at the sensor, G1 is the next band out, and so on to the far edge of its range. For every gate the radar measures two kinds of signal on a scale of 0 to 100: *move energy*, which rises when something moves at that distance (someone walking past), and *still energy*, which picks up the much smaller signal of someone who is there but not moving (sitting on the couch, breathing, typing).

Each gate has a *move threshold* and a *still threshold*. When a gate's energy rises above its threshold, that gate detects a target (the radar's word for a person, or anything else it picks up) and the radar reports presence. A lower threshold makes the gate more sensitive (and more likely to trigger on a fan or a curtain); a higher one makes it less sensitive. To see the live energy of every gate, the radar has to be in **Radar Engineering Mode**, a diagnostic setting that streams the per-gate readings to Home Assistant. With it off you still get presence, but the Gate Energy chart has nothing to show. It's safe to turn on and off whenever you like: it changes what the radar reports, not how it detects. The calibration turns it on for you while it listens. Left on, it saves every gate's energy to Home Assistant's database about once a second, so the **Radar setup** card reminds you to turn it off.

![The LD2410 Gate Energy chart with Radar Engineering Mode on: a purple move bar and a green still bar for each gate from G0 to G8, and triangles marking each gate's move and still thresholds](/assets/apollo-mmwave-gate-energy-live.png)

!!! tip "How far away is each gate?"

    Each gate is one step of the radar's gate size. Unless you changed it, that's 0.75 m (about 2.5 ft). You don't need to work the distances out: each row on the **Move Thresholds** and **Still Thresholds** cards is named for how far out its gate reaches, such as **G4 (about 3 m)**, or **G4 (about 10 ft)** when Home Assistant uses US customary units. G4 covers 2.25 m to 3 m (about 7.4 ft to 9.8 ft) from the sensor. The gate size setting is **Gate Size** on an MSR-1 or MSR-2 and **Distance Resolution** on an R PRO-1, and it's hidden on a new sensor: it only shows on the **Detection Range** card after you enable its entity on the sensor's device page. The **Gates** row on the Distances chart draws each gate along the distance axis, so you can read it off the screen. It starts at G1, because G0 is the reading right at the sensor and has no width. On an R PRO-1, a smaller Distance Resolution (0.5 m) gives finer tuning over a shorter range, and a larger one (0.75 m) reaches farther.

## Start with the Radar setup card

The first step on **Start here** points at the **Radar setup** card right under it on an MSR-1, MSR-2, or R PRO-1 tab. It reads the radar's settings and flags anything that gets in the way of a good calibration. Its second line names the chip and the sensor, and when there's nothing to fix it reads **Radar settings look good.**

![The Radar setup card on an MSR-1, with LD2410 · MSR-1 Kitchen under the title and the line Radar settings look good.](/assets/apollo-mmwave-radar-setup-ld2410.png)

The card changes nothing on its own. When it flags something, it says what's wrong and, where it can, offers a button that names the one change it makes:

- **Radar Engineering Mode is on, so every gate's energy is saved to the database about once a second.** Press **Turn off Radar Engineering Mode** once you're done watching the Gate Energy chart. While a calibration runs, the card says nothing about it, because the calibration needs the mode on.
- **The radar has not reported its gate thresholds yet, so those settings are blank.** Press **Read settings from the radar**. It only asks the radar to send them; nothing on the radar changes.
- A zone that can never turn on (MSR-1 and MSR-2), for example **Zone 2 can never turn on. End Zone 2 (150 cm) must be larger than End Zone 1 (200 cm).** The distances on the **LD2410 Zone Config** card are out of order, or a zone starts past how far the radar is set to look. Change the distances on the Zone Config card, or raise the max gates on the **Detection Range** card.
- **Min Gate** at or above **Max Gate** (R PRO-1). The LD2412 only detects people from Min Gate out to Max Gate, so set Min Gate lower than Max Gate on the **LD2412 Detection Range** card.

The last two have no button: the card explains them and leaves the new values to you. On an MTR-1, the **Radar setup** card under **Start here** checks the LD2450 instead, and an R PRO-1 tab has a second **Radar setup** card above the zone map for its LD2450. Both are covered in [Check the LD2450's Radar setup card](#check-the-ld2450s-radar-setup-card).

## Calibrate with an empty room

Calibration is the fastest way to a well-tuned radar. Home Assistant listens to every gate while nobody is in the room, notes the highest energy each gate reaches from the room itself (fans, curtains, plants), and sets each threshold a little above that. Your current thresholds are saved first, so you can always put them back.

Run it when you first set up a radar, when it triggers with nobody there, and after you move the sensor or rearrange the room.

Before you press the button, the card's checklist asks for three things (an R PRO-1 adds a fourth, covered in [R PRO-1 and its LD2412 radar](#r-pro-1-and-its-ld2412-radar)):

- Nobody in the radar's view: people, pets, and robot vacuums all count. Someone sitting still is the hardest case, because their still energy becomes the "background".
- Leave fans, curtains, and plants that normally move as they usually are. They are part of the background you want the radar to ignore.
- Radar Engineering Mode is handled for you. If it is off, Home Assistant turns it on for the listen and back off at the end. If it is already on, the card says **Radar Engineering Mode is already on and will stay on.**

On an MSR-1 or MSR-2 that has never been tuned, the card may also say **These look like factory thresholds. Calibrating sets them for your room.**

A threshold of 100 means that gate never triggers, so some people set a gate to 100 to turn it off. Calibration sets every gate the radar uses, including those, and the card warns you first, for example **The G2 still threshold is off (set to 100). Calibrating will turn it back on.** If you turned that gate off on purpose, calibrate anyway and set it back to 100 afterward on the **Still Thresholds** (or **Move Thresholds**) card.

![The Auto-calibrate card on an MSR-1 before a run, with its checklist, the warning The G2 still threshold is off (set to 100). Calibrating will turn it back on., and the Calibrate with empty room and Preview only buttons](/assets/apollo-mmwave-calibrate-idle.png)

### Run a calibration

You start the calibration from the card, then stay out of the room for about a minute and a half while it listens. On an R PRO-1, first clear the room, press **Start Dynamic Background Correction** on the **LD2412 Controls** card, and wait for **Background Correction Running** to turn off (see [R PRO-1 and its LD2412 radar](#r-pro-1-and-its-ld2412-radar)).

1. Press **Calibrate with empty room** on the **Auto-calibrate** card. Take your phone with you if you'd like to watch the countdown and the listen from outside the room.
2. Leave the room while the countdown runs and close the door behind you. Then move away from the door and the walls: the radar can see through drywall and thin doors, so waiting right outside can count as someone in the room. If the room has no door, go to another room, out of the sensor's view.
3. Come back after about a minute and a half, once the card shows **Thresholds updated**, and read the result.

The job runs inside Home Assistant, so closing the browser or putting your phone away does not stop it. Open the dashboard again and the card picks up wherever the job is. Here is what the card shows along the way:

| Stage | What the card shows | How long |
| --- | --- | --- |
| Starting (only if Radar Engineering Mode was off) | **Turning on Radar Engineering Mode...** | A moment |
| Countdown | **Leave the room now.** and **Listening starts in 15 s.**, counting down | 15 seconds |
| Warm-up | **Waiting for gate energy from the radar...**, only if the radar is slow to start sending energy | A few seconds at most |
| Listening | **Listening to the empty room... 60 s left**, **Keep the room empty. 12 samples so far.**, and two lines starting **Highest so far, move:** and **Highest so far, still:** with the peak of each gate so far | 60 seconds |
| Reading (R PRO-1 only) | **Reading the radar's current thresholds...** | A few seconds |
| Writing | **Writing 16 thresholds to the radar... 7 of 16** and **Values already written stay until you undo.** The count is the number of thresholds that are changing. | A few seconds |
| Checking | **Checking that the radar accepted the new values...** | About 3 seconds |
| Done | **Thresholds updated** | |

Here is a whole run on an MSR-1, sped up: turning on Radar Engineering Mode, the countdown, the listen with the highest energy of each gate so far, the writing and checking stages, and the result.

<video src="/assets/apollo-mmwave-calibrate.mp4" poster="/assets/apollo-mmwave-calibrate-poster.jpg" autoplay loop muted playsinline aria-label="A calibration on the Auto-calibrate card, sped up: Turning on Radar Engineering Mode, Leave the room now with a 15 second countdown, Listening to the empty room with the highest energy of each gate, Writing 18 thresholds to the radar, Checking that the radar accepted the new values, and Thresholds updated with the result table"></video>

From the countdown through the listen, the card also reminds you: **Leave Radar Engineering Mode on until this finishes.** Turning it off during the listen stops the calibration without changing anything.

A **Stop** button sits under the progress bar until the checking stage. Press it and it reads **Stopping...** for a moment. Stopped before the writing stage, the card says **Stopped. Nothing was changed.** Stopped partway through writing, it says how many values were written and that **Undo** restores the saved values.

Not ready to change anything yet? **Preview only** runs the same countdown and listen and shows you the thresholds it would set. The card explains: **Computes new thresholds without changing any of them. Radar Engineering Mode is still turned on for the listen.** The preview ends with **Preview: no threshold was changed.** and **These are the thresholds calibration would set:** above the result table, and two buttons: **Calibrate and apply** starts a full calibration (with a fresh countdown and listen), and **Close** returns the card to its start.

![A preview on the Auto-calibrate card: Preview: no threshold was changed., the line These are the thresholds calibration would set:, a table of nine gates with each peak and the threshold it would set, such as G0 move 36 → 39 and G1 move 35 (unchanged), and the Calibrate and apply and Close buttons](/assets/apollo-mmwave-calibrate-preview.png)

### Read the result

When the run finishes, the card shows **Thresholds updated** and a summary such as **Calibrated at 02:32 PM from 60 samples. 16 of 18 thresholds changed.** Times appear in your browser's format, so you might see 14:32 instead of 02:32 PM. An MSR-1 or MSR-2 has 18 thresholds (9 gates, move and still); an R PRO-1 has 28 (14 gates).

Below the summary is a table with one row per gate and the columns **Gate**, **Move peak**, **Move threshold**, **Still peak**, and **Still threshold**. The peak is the highest energy that gate reached while the room was empty. The new threshold is that peak plus some headroom, capped at 100. From Apollo mmWave 2.2.4, the headroom is 15 points or 35% of the peak, whichever is larger: a move peak of 14 becomes a threshold of 29, and a still peak of 60 becomes 81. Earlier versions used 10 points or a quarter of the peak, so calibrate again after updating to get the extra headroom.

![The result of a calibration on an MSR-1: Thresholds updated, Calibrated at 01:04 PM from 60 samples. 18 of 18 thresholds changed., the result table with each gate's peak and its old and new threshold, such as G2 move peak 6 and 16 → 21, the walk-test line, and the Undo (restore your previous values), Calibrate again, and Close buttons](/assets/apollo-mmwave-calibrate-result.png)

What the threshold cells mean:

- **50 → 24**: the threshold changed from 50 to 24.
- **24 (unchanged)**: the new value matched the old one, so nothing was written.
- **100 → 15 (was off)**: that gate was turned off (set to 100) and calibration turned it back on. A line under the table says so and how to turn it off again.
- **100 (off)** or **40 → 100 (off)**: the background at that gate was so strong the threshold went to the top of the scale, so that gate can no longer trigger. On an MSR-1 or MSR-2, the G0 and G1 still thresholds often end up here, because those gates sit right at the sensor and their still energy idles near the top. That's normal and needs no action, so the card does not warn about them. For any other gate in use, including G0 and G1 move, the card warns you (see [Warnings the card can show](#warnings-the-card-can-show)).
- **no data**: the gate sent too few readings, so it was left as it was.
- **(spike seen)** after a peak: one reading jumped well above the rest, as if something moved. The threshold still comes from that peak, so that gate ends up less sensitive. If nothing should have moved there, run the calibration again with the room empty.
- **not confirmed (radar offline)** or **(not confirmed)**: the radar did not report the new value back. See [Thresholds did not change on the radar](#thresholds-did-not-change-on-the-radar).

Gates outside the range the radar is set to use are dimmed, with a note under the table such as **G7, G8: not used (beyond Max Move Gate 6)**. They are still calibrated, so they are ready if you extend the range later.

### Check the result or undo it

Under the table, the card suggests a walk test:

**Now walk around, then sit still for a minute: the Radar Target row in Target / Occupancy should stay on the whole time you are in the room and turn off a few seconds after you leave (Radar Timeout).**

1. Press **Turn on Radar Engineering Mode** on the Gate Energy chart if you'd like to watch the gates as well.
2. Walk through the room, then sit where you usually sit and stay still for a minute or two. **Radar Target** covers still presence as well as movement, so it should stay on the whole time. With Radar Engineering Mode on, the bars of the gates you're in should be outlined.
3. Leave the room. **Radar Target** should turn off a few seconds later, once **Radar Timeout** runs out, and no gate inside the radar's range should stay outlined.
4. If you turned on Radar Engineering Mode, press **Turn off Radar Engineering Mode** on the **Radar setup** card, or use the switch on the **Controls** card.

Below the walk-test line are three buttons: **Undo (restore your previous values)**, **Calibrate again** (a fresh calibration with a new countdown and listen), and **Close**. If the radar now misses you, or behaves worse than before, press **Undo (restore your previous values)**. The card shows **Restoring saved thresholds... 3 of 16** and then **Restored your previous values.** Undo saves the values it replaces first, so the button then reads **Redo (put the calibrated values back)**, and pressing it puts the calibrated values back. The saved copy survives a Home Assistant restart.

![The Auto-calibrate card after Undo: Restored your previous values., the checklist, and the Redo (put the calibrated values back) and Calibrate with empty room buttons](/assets/apollo-mmwave-calibrate-restored.png)

If someone walked in during the listen, press **Stop**: nothing is written before the writing stage. If you only notice afterward, press **Undo**, clear the room, and press **Calibrate with empty room**.

The next time you open the dashboard, the card starts on its checklist again with a line such as **Last calibrated Oct 11, 02:32 PM, 16 of 18 thresholds changed.** (in your browser's date and time format), the **Undo (restore your previous values)** button with the time those values were saved under it (**Saved Oct 11, 02:31 PM.**), and **Show last result** to open the last result table.

### Warnings the card can show

Warnings appear under the result table. Each one is a sign the result may not match your empty room:

- **The radar reported someone present for 40% of the listen. If someone was in the room, even sitting still, press Undo and run it again.** The radar detected presence for more than a quarter of the listen. That is normal for a radar that was too sensitive (which is what you are fixing), but if a person or pet was in the room, the thresholds are too high. Press **Undo**, clear the room, and run it again. If you're sure the room was empty, keep the result and do the walk test in [Check the result or undo it](#check-the-result-or-undo-it).
- **The G3 move threshold is now off (its background peaked at 92). If a fan or curtain moves there all day this is fine; if not, press Undo and run again with the room really empty.** That gate can no longer detect anything. If something at that distance moves all day, that is the expected result. If not, something moved there during the listen: press **Undo** and run it again with the room empty.
- **The radar was unavailable for part of the listen; gates with too few readings were left as they were.** The radar dropped off the network for a moment. Gates marked **no data** kept their old thresholds. Check the radar's connection and run it again.
- **The G2 still threshold was off (set to 100) and calibration turned it back on (now 15). If you turned it off on purpose, set it back to 100 on the Still Thresholds card, or press Undo to put back all your previous values.** You had that gate turned off, and calibration set it like every other gate. If you want it off, set it back to 100 on the card the line names. A preview words it as what calibration would do.
- **2 values could not be confirmed: G3 move threshold reads back 35 (asked for 27), G5 still threshold could not be read (radar offline). Check the Move / Still Thresholds cards.** The radar did not report some of the new values back. The heading reads **Thresholds updated, 2 could not be confirmed**. Check those gates on the threshold cards, and press **Undo** or run it again once the radar is stable.

## A tour of the radar tab

Open **Apollo mmWave** from your sidebar and, if you have more than one radar, pick your radar's tab. On a wide screen the cards sit in columns; on a phone they stack in the order below. Card titles start with the name of the radar chip: **LD2410** on an MSR-1 or MSR-2, **LD2412** on an R PRO-1. A card only shows rows for entities Home Assistant has, so a setting the firmware hides has no row.

### First column

- **Start here**: your sensor's name and its first steps, pictured at the top of this guide. It ends with two links. **Full tuning guide →** opens this guide on the wiki: on an MSR-1 or MSR-2 the general version, the one that covers every Apollo radar, and on an R PRO-1 [the R PRO-1 version](/products/rpro1/setup/apollo-mmwave-dashboard.md#r-pro-1-and-its-ld2412-radar) at its LD2412 section. **All settings for this device →** opens the sensor's own page in Home Assistant, where every setting the dashboard leaves out lives. On an R PRO-1, the card also says what each radar is for and which presence sensor to use in automations.
- **Radar setup**: checks the radar's settings and offers a fix (see [Start with the Radar setup card](#start-with-the-radar-setup-card)).
- **Auto-calibrate**: the calibration card. It shows the chip and the device name under its title, a short checklist, and the **Calibrate with empty room** button. Everything about it is in [Calibrate with an empty room](#calibrate-with-an-empty-room) above.
- **LD2410 Controls**: the **Radar Engineering Mode** switch, plus **Radar Bluetooth (HLK app)**, **Restart Radar**, and **Factory Reset Radar**. On an R PRO-1 the card also has **Start Dynamic Background Correction** and **Background Correction Running** (see [R PRO-1 and its LD2412 radar](#r-pro-1-and-its-ld2412-radar)). **Radar Bluetooth (HLK app)** is the radar chip's own Bluetooth for the HLK phone app, not your sensor's Bluetooth proxy. **Restart Radar** restarts the radar chip without changing any settings. Leave **Factory Reset Radar** alone unless Apollo support asks you to press it: it puts the radar chip's settings, every threshold included, back to factory values, so run **Calibrate with empty room** again if it happens. Both ask before they act. The restart for the whole sensor is on the **Device** card at the bottom of the tab.

    ![The LD2410 Controls card with the Radar Engineering Mode and Radar Bluetooth (HLK app) switches, a Restart button on the Restart Radar row, and a Reset button on the Factory Reset Radar row](/assets/apollo-mmwave-controls.png)

- **LD2410 Zone Config** (MSR-1 and MSR-2): **Start Zone 1**, **End Zone 1**, **End Zone 2**, and **End Zone 3** split the radar's range into three distance bands, each with its own occupancy sensor (**Radar Zone 1 Occupancy** to **Radar Zone 3 Occupancy**). These are distances from the sensor, not areas you draw like on the R PRO-1 and MTR-1 zone map. The boxes are in cm, even when Home Assistant uses feet, and the zones sit back to back: Zone 1 runs from Start Zone 1 to End Zone 1, Zone 2 from there to End Zone 2, and Zone 3 from there to End Zone 3. They're optional: leave them as they are unless you want separate sensors for, say, the couch and the far end of the room.

### Second column

- **LD2410 Distances**: a chart laid out along the radar's range. From top to bottom it can show a **Zones** row with your three distance bands (**Z1** to **Z3**, with a filled circle when someone is in that band), bars for the current **Detection**, **Moving**, and **Still** distance, the **Gates** row, and bars that mark how far the radar is set to look (**Max Move** and **Max Still**, or **Max Gate** and **Min Gate** on an R PRO-1). On a computer, hover over a row for a short explanation. Distances show in meters, or in inches if Home Assistant uses US units.

    ![The LD2410 Distances chart with nobody in the room: the Zones row with Z1 to Z3, Detection, Moving and Still rows that read no target, the Gates row from G1 to G8, and the Max Move and Max Still bars, on a scale in inches](/assets/apollo-mmwave-distances.png)

- **LD2410 Detection Range**: **Radar Timeout** (how long presence stays on after the last detection), the gate size (hidden until you enable its entity), and the sliders that set how far the radar looks: **Max Move Gate** and **Max Still Gate** on an MSR-1 or MSR-2, **Max Gate** and **Min Gate** on an R PRO-1. The sliders start locked under a **Sliders locked** row (see [Set the range and timeout](#set-the-range-and-timeout)). A note under the card explains each one and gives each gate's depth in your units.

    ![The LD2410 Detection Range card with the Radar Timeout box set to 10s, the row Sliders locked, A scroll cannot move them. with an Unlock button, and the Max Move Gate and Max Still Gate sliders grayed out at 8](/assets/apollo-mmwave-detection-range-locked.png)

- **LD2410 Target / Occupancy**: **Radar Target** (anyone detected), **Radar Moving Target**, **Radar Still Target**, and on an MSR-1 or MSR-2 **Radar Zone 1 Occupancy** to **Radar Zone 3 Occupancy** and **Any zone**, which is on while someone is in any of the three zones. A row lights up while it's on. On an R PRO-1 this card sits in the first column instead.

### Third column

- **LD2410 Gate Energy**: the chart you tune with. Each gate has two bars, a purple one for move energy and a green one for still energy, on a 0 to 100 scale. While Radar Engineering Mode is on, a right-pointing triangle marks each gate's move threshold and a left-pointing triangle its still threshold, and a bar that rises above its threshold gets an outline in the threshold's color: **outlined bar = above threshold (detecting)**. While Radar Engineering Mode is off, the chart is dimmed with **Turn on Radar Engineering Mode to see gate energy values** and a **Turn on Radar Engineering Mode** button you can press right there.
- **LD2410 Move Thresholds**: one slider per gate (**G0** to **G8** on an MSR-1 or MSR-2, **G0** to **G13** on an R PRO-1) to set each gate's move threshold. Each row is named for how far out its gate reaches, from **G0 (at the sensor)** to **G8 (about 6 m)**, in feet when Home Assistant uses US customary units. The sliders start locked, like the Detection Range ones. A note underneath recaps how thresholds work.

### Fourth column

- **LD2410 Occupancy History**: the last 24 hours of **Detected**, **Moving**, and **Still** (and, on an MSR-1 or MSR-2, **Any zone** and **Zone 1** to **Zone 3**), so a false trigger overnight is still there in the morning. On an R PRO-1 it's titled **Occupancy History**, its lines read **LD2412 Presence**, **LD2412 Moving**, and **LD2412 Still**, and it also shows **LD2450 Presence** and each zone you drew.
- **LD2410 Still Thresholds**: one slider per gate for the still thresholds, named and locked the same way.

![The LD2410 Still Thresholds card with the Sliders locked row and an Unlock button above nine grayed-out sliders named G0 (at the sensor), G1 (about 2.5 ft), G2 (about 5 ft), and so on to G8 (about 20 ft), each with its percentage](/assets/apollo-mmwave-still-thresholds-locked.png)

- **Device**: at the bottom of every tab. It shows **Apollo firmware**, the radar chip's firmware (**LD2410 firmware** on an MSR-1 or MSR-2, **LD2450 firmware** on an MTR-1; on an R PRO-1, both chips' versions are hidden until you enable them on the device page), and **Firmware update**, which opens Home Assistant's own update window when you tap it. An MTR-1 has no Firmware update row. **Restart device** restarts the whole sensor after you confirm. On an R PRO-1 with the LD2412 it reads **Restart device (both radars)**, and on an MTR-1 or an R PRO-1 without the LD2412 it reads **Restart device (also restarts the radar)**. Under the rows are the **All settings for this device →** link and how to download a [support file](#send-apollo-a-support-file). While the Wi-Fi signal is below -75 dBm, a **Weak Wi-Fi** note appears too.

![The Device card for an MSR-1: Apollo firmware 26.10.12.1, LD2410 firmware 2.04.23022511, Firmware update Up-to-date, and a Restart button on the Restart device row](/assets/apollo-mmwave-device.png)

On an R PRO-1, the **Zone Map** heading comes right after the first column, with the LD2450's own **Radar setup** card, the zone map, **Zone presence**, **LD2450 Live**, and **LD2450 Controls**, so on a phone you reach them before the LD2412's threshold cards (see [Draw zones on the R PRO-1 and MTR-1](#draw-zones-on-the-r-pro-1-and-mtr-1)). An MTR-1 tab has those cards, its own **Start here**, and the **Device** card, without the tuning cards.

## R PRO-1 and its LD2412 radar

Every R PRO-1 has an LD2450 radar, and the optional LD2412 addon adds a second one. The LD2412 handles presence and gets the tuning cards and the calibration, and the LD2450 tracks positions for the [zone map](#draw-zones-on-the-r-pro-1-and-mtr-1). An R PRO-1 without the LD2412 still shows the LD2412 cards on its tab, but there's no radar behind them, so the calibration and this section don't apply to it; its **Start here** card gives the zone map steps instead, and its zone map works the same. With the LD2412, a few things differ from an MSR-1 or MSR-2:

- The tab has two **Radar setup** cards. The one under **Start here** checks the LD2412, and its second line starts with **LD2412**. The one above the zone map checks the LD2450.
- The LD2412 has 14 gates, **G0** to **G13**, so a calibration sets 28 thresholds.
- **LD2412 Detection Range** has **Distance Resolution** instead of Gate Size, and **Max Gate** and **Min Gate** instead of Max Move Gate and Max Still Gate. Gates below Min Gate or beyond Max Gate are dimmed in the result table, for example **G0: not used (below Min Gate 1)**.
- There is no Zone Config card, and the Distances chart shows the gates and the Max Gate and Min Gate bars without live distance bars.
- Before it writes, the calibration asks the radar for its current thresholds (**Reading the radar's current thresholds...**), so what it saves for Undo matches the radar.

![The Auto-calibrate card on an R PRO-1, titled LD2412 · R PRO-1 Server Rack, with a fourth checklist item asking you to run Start Dynamic Background Correction first](/assets/apollo-mmwave-calibrate-r-pro-1.png)

The LD2412 also has its own background learning, **Start Dynamic Background Correction** on the **LD2412 Controls** card. It runs on the radar chip and stores its result inside the radar. **Background Correction Running** shows whether it is still working. Use both, in this order:

1. Clear the room and press **Start Dynamic Background Correction**.
2. Wait for **Background Correction Running** to turn off. Until it does, the Auto-calibrate card says **Background correction is running on the LD2412. Wait for its status to turn off.** and its button stays disabled.
3. Press **Calibrate with empty room** with the room still empty.

Run the calibration again after any later background correction. During a calibration on an R PRO-1, the card's reminder reads **Leave Radar Engineering Mode on and do not press Start Dynamic Background Correction until this finishes.** Pressing it during the listen stops the calibration without changing anything.

!!! warning "Undo cannot reverse a background correction"

    The Auto-calibrate card's **Undo** restores the thresholds Home Assistant saved. Dynamic Background Correction changes the radar itself, outside those thresholds, so Undo cannot reverse it.

## Set the range and timeout

Steps 3 and 4 on **Start here** point at the **Detection Range** card: how far the radar looks, and how long presence stays on after you stop moving. Its sliders, and the ones on the two threshold cards, start locked, so a finger that lands on one while you scroll a phone can't change a setting.

1. Press **Unlock** on the **Sliders locked** row. That unlocks this sensor's sliders on all three cards, and the row reads **Sliders unlocked**.

    <video src="/assets/apollo-mmwave-slider-lock.mp4" poster="/assets/apollo-mmwave-slider-lock-poster.jpg" autoplay loop muted playsinline aria-label="The LD2410 Detection Range card with its sliders locked: a tap turns the Max Move Gate slider orange, a second tap shows the reminder These sliders are locked. Press Unlock above them to change one. with an Unlock button, then Unlock is pressed and the row reads Sliders unlocked, They lock again after 5 minutes without a change."></video>

2. Lower **Max Move Gate** and **Max Still Gate** (**Max Gate** on an R PRO-1) to stop the radar looking past a certain distance, such as a hallway beyond the doorway. The note under the card gives each gate's depth. On an R PRO-1, raise **Min Gate** to ignore anything right next to the sensor.
3. Raise **Radar Timeout** if lights turn off while you sit still. It's how long **Radar Target** (**LD2412 Presence** on an R PRO-1) stays on after the radar last detects someone. It's a number box, so it's never locked.

The sliders lock again on their own after 5 minutes without a change, when you leave the tab, and each time the page loads, but never while you're dragging one. **Lock** on the same row locks them right away.

!!! tip "Touched a locked slider?"

    A locked slider is gray and still shows its value, and a scroll that starts on it scrolls the page. Touch one and it turns orange for a moment while **Unlock** flashes. Try again within 10 seconds and Home Assistant shows **These sliders are locked. Press Unlock above them to change one.** with an **Unlock** button. The lock lives in the browser page, so another phone or browser tab has its own, and **Calibrate with empty room** works whether the sliders are locked or not.

## Fine-tune gates by hand

Calibration gets most rooms right. If one spot still misbehaves, the Gate Energy chart shows you which gate to change. The outline is the signal to read: an outlined bar is a gate whose energy is above its threshold right now. Inside the range the radar uses, that means the gate is detecting a target.

1. Press **Turn on Radar Engineering Mode** on the Gate Energy chart. The bars and threshold triangles appear.

    <video src="/assets/apollo-mmwave-gate-energy.mp4" autoplay loop muted playsinline aria-label="The LD2410 Gate Energy chart turning on: first dimmed behind Turn on Radar Engineering Mode, then live move and still bars for G0 to G8 with a triangle for each threshold"></video>

2. Leave the room and watch the chart from your phone, somewhere out of the radar's view (it can see through drywall, so step away from the wall too). A bar that is outlined while nobody is there is a gate causing false triggers. Gates outside the range the radar uses can be outlined too, but the radar ignores them: that range runs up to **Max Move Gate** for move bars and **Max Still Gate** for still bars, or from **Min Gate** to **Max Gate** on an R PRO-1.
3. Press **Unlock** above the sliders, then raise the threshold of each gate causing false triggers on **Move Thresholds** (purple bar) or **Still Thresholds** (green bar) until its triangle sits a few points above the highest point the bar reaches.
4. Sit or stand where the radar misses you. Your gate is the one whose bars rise when you shift in place; each threshold row names how far out its gate reaches, and the **Gates** row on the Distances chart shows it too. Lower that gate's threshold a few points at a time until its bar is outlined while you are there, but not after you leave.
5. Turn off **Radar Engineering Mode** when you are done: press **Turn off Radar Engineering Mode** on the **Radar setup** card, or use the switch on the **Controls** card. The chart has no off button.

The **Detection Range** card helps too: [Set the range and timeout](#set-the-range-and-timeout) covers it.

!!! tip "Calibrate first, then fine-tune"

    A new calibration sets every threshold again, including ones you changed by hand. If you calibrate after fine-tuning and prefer your own values, **Undo** brings them back.

## Draw zones on the R PRO-1 and MTR-1

The LD2450 radar in the R PRO-1 and MTR-1 tracks where up to three people are in the room. The zone map lets you draw areas on that map, such as the couch or the desk, and gives each area its own occupancy sensor. On an MTR-1 the tab is built around the zone map: **Start here**, the **Radar setup** card, and the map come first, with the radar's live status and controls beside them. On an R PRO-1, the LD2450's **Radar setup** card, the map, and the radar's live status and controls sit under the **Zone Map** heading, right after the first column of LD2412 cards, and its **Start here** card stays at the top of the tab.

The MTR-1's **Start here** card has three steps, and this section follows them: fix anything the **Radar setup** card flags, set **Cone rotation** to match how the sensor is mounted, then draw a zone and walk into it. An R PRO-1 without the optional LD2412 gets the same steps.

The zone map card shows your radar's name and the area the radar can see: a view cone 120 degrees wide and about 6 m (20 ft) out, with a caption at its edge such as **Radar range 6 m (20 ft), 120°**, and a dot for each person it tracks. The map fits that area, turned the way you set **Cone rotation**, plus any zone you drew outside it. Buttons sit in the bottom corners of the grid, with a row of zone buttons and a **Configure** section underneath.

![The zone map for an R PRO-1 named R PRO-1 Server Rack, in feet: the radar's view cone fills the grid from -16 ft to 16 ft across, with the caption Radar range 20 ft (6 m), 120°, a rectangle named Zone 1 at the sensor, a circle named Zone 2, and a polygon named Zone 3. Along the bottom of the grid are the ✎ button, the m / ft switch with ft selected, the dimmed ↶ undo button, and the Locked button, and under the grid the Zone 1, Zone 2, Zone 3, and Clear All Zones buttons and the collapsed Configure section](/assets/apollo-mmwave-zone-map.png)

The map is in feet when Home Assistant uses US customary units (**Settings → System → General**), and in meters otherwise. The **m / ft** switch in the bottom-right corner of the map changes it. When an administrator presses it, the choice is saved for that radar, so everyone who opens its map sees that unit. Anyone else changes only their own view, until they reload the page. Zones are stored in millimeters either way, so switching units never moves a zone.

### Check the LD2450's Radar setup card

The **Radar setup** card right above the map checks the two LD2450 settings that decide whether the map can show people. The radar chip keeps these itself, and Apollo firmware never sets them:

- **Zone Type** should be **Disabled**, because the zone map replaces the radar's own built-in zones. On **Detection**, the radar reports only people inside those built-in zones, and with none set it reports nobody, so the map stays empty. On **Filter**, it hides people inside them.
- **Multi Target Tracking** should be on. Off, the radar tracks only one person.

![The Radar setup card on an R PRO-1, with LD2450 · R PRO-1 Server Rack under the title, the line Zone Type is Filter. This radar ignores people inside its built-in zones. Disabled is recommended because the zone map replaces them., and a Set Zone Type to Disabled button](/assets/apollo-mmwave-radar-setup-ld2450.png)

Press the button the card shows: **Set Zone Type to Disabled**, **Turn on Multi Target Tracking**, or **Use recommended settings** when both need fixing. The card changes nothing until you press one, and reads **Radar settings look good.** once both are right. On an R PRO-1, Home Assistant hides Multi Target Tracking by default, so the card checks only Zone Type until you enable that setting (see [The zone map shows nobody, or only one person](#the-zone-map-shows-nobody-or-only-one-person)).

### Match the map to how the sensor is mounted

Turn the map so its view cone points the way your sensor faces. The tracked dots turn with it.

1. Open **Configure** under the grid.
2. If the **Cone rotation:** slider is gray, the map is locked: press **Locked** on the map first (see [Lock and unlock](#lock-and-unlock)).
3. Drag **Cone rotation:** (from -180° to 180°) until the view cone points the way your sensor faces. When you let go, the angle is saved for the radar and the map fits the turned cone. Double-click the slider to reset it.

### Lock and unlock

The bottom-right corner has a lock toggle that reads **Unlocked** (🔓) or **Locked** (🔒). The map starts locked once the radar has zones, and your browser remembers your choice for each radar. A radar with no zones yet starts unlocked, so you can set **Cone rotation** and draw right away. While the map is locked:

- Drawing on it shows **Unlock the grid before drawing.**
- The **Cone rotation** slider is gray, and a scroll that starts on it scrolls the page. A tap or drag on it outlines **Locked** and shows **Cone rotation is locked. Press Locked on the map to change it.**
- **Clear All Zones**, double-clicking a zone's button, ↶ (**Undo last zone change**), and **Configure → Zones** still change your zones.

On a phone or tablet, the grid takes every touch, so a swipe on it doesn't scroll the page, even while the map is locked. Scroll with your finger outside the grid, for example on the radar's name above it. Stay off the zone buttons while you scroll: a stray tap on **Clear All Zones** clears every zone's shape. Keep the map on **Locked** when you're not drawing: on an unlocked map, a swipe across the grid can draw a new shape for the selected zone and replace its old one.

From Apollo mmWave 2.2.6, only administrators can save zone changes. Other users still see the zones and their presence sensors, and a change they try to make shows a **Could not save** message.

### Add a zone

Open **Configure → Zones** and press **Add Zone**. The new zone is named **Zone 1** (then Zone 2, and so on), gets its own button under the grid, and is selected and ready to draw.

### Draw a zone

You draw each zone on the grid as a rectangle, ellipse, or polygon.

1. Unlock the map and press the zone's button to select it.
2. Press ✎ (**Drawing modes**) in the bottom-left corner and pick a shape: ▭ (**Rectangle**), ◯ (**Ellipse**), or ⬠ (**Polygon**).
3. For a rectangle or ellipse, drag across the grid and let go to save.
4. For a polygon, click each corner, then double-click or press ✓ (**Finish polygon**) to save. A polygon can have up to 32 points. ↺ (**Undo last point**) or **Backspace** removes the last point, and **Esc** cancels the shape.

Drawing a new shape for a zone replaces its old one. Made a mistake? ↶ (**Undo last zone change**) in the bottom-right corner puts the last change back. Drawing works with touch too, so you can draw zones from a phone or tablet.

### Rename a zone

In **Configure → Zones**, type a new name next to the zone and press **Save**. The name appears on the zone's button.

### Clear or delete a zone

Double-click a zone's button to clear its shape, or press **Clear All Zones** to clear every shape while keeping the zones. To remove a zone completely, along with its sensors, press **Delete** next to it in **Configure → Zones**.

### Use the zone sensors

Each zone gets an occupancy sensor named **Zone 1 presence** (and so on) on the radar's device page in Home Assistant. It turns on when a tracked person is inside the zone, ready to use in your automations. When you rename a zone on the card, its sensors follow, so a zone named Couch gets **Zone 1 presence - Couch**. A name you gave the sensor yourself in Home Assistant is kept.

To try a zone, reload the page after you draw it, then walk into it. The **Zone presence** card next to the map lists each zone's sensor and colors it while someone is in the zone, and **Occupancy History** adds a line for the zone, covering the last 24 hours.

Under it, **LD2450 Live** shows what the radar reports right now. If the map shows no dot with you in the room, look here first: **Presence** off means the radar itself reports nobody.

![The LD2450 Live card on an R PRO-1 with nobody in the room: Presence, Moving Target, and Still Target read Clear, Target Count reads 0.0, and Target 1 to 3 Distance read Unknown with their Direction rows reading NA](/assets/apollo-mmwave-ld2450-live.png)

**LD2450 Controls** holds **Zone Type**, **Multi Target Tracking**, **Radar Timeout**, **Radar Bluetooth (HLK app)**, **Restart Radar**, and **Factory Reset Radar**, whichever your sensor has (the MTR-1 has no Restart Radar). The restart and the reset ask before they act. **Radar Timeout** is how long **LD2450 Presence** stays on after the radar last sees someone. It doesn't hold the zones you draw: a zone turns off as soon as nobody is in it. While Zone Type isn't **Disabled**, a **Radar's built-in zones** card shows the radar chip's own zones, which are not the zones on the map.

While the radar is offline, or still reconnecting after a restart, zone presence reads off, not unavailable. An automation that waits for a zone to be clear for some minutes can't tell that apart from an empty zone, so have it also check that the radar itself is online.

## Calibrate from an automation

The **Calibrate with empty room** button runs the `apollo_mmwave.calibrate_gates` action, and your automations can run it too. When an automation already knows the room is empty, set `settle_s: 0` to skip the countdown, and `wait: true` to get the result back when the run ends. This example recalibrates an office radar at 3:00 AM if nobody has been detected for 30 minutes, and sends a notification when the outcome is anything other than applied:

```yaml
alias: Recalibrate the office radar overnight
triggers:
  - trigger: time
    at: "03:00:00"
conditions:
  - condition: state
    entity_id: binary_sensor.apollo_msr_2_abc123_radar_target
    state: "off"
    for: "00:30:00"
actions:
  - action: apollo_mmwave.calibrate_gates
    data:
      device_id: your_device_id
      settle_s: 0
      wait: true
    response_variable: calibration
  - if:
      - condition: template
        value_template: "{{ calibration.outcome != 'applied' }}"
    then:
      - action: persistent_notification.create
        data:
          title: Radar calibration
          message: >
            Outcome {{ calibration.outcome }}
            {% if calibration.error %}({{ calibration.error.message }}){% endif %},
            {{ calibration.changed }} thresholds changed.
```

To use it, create a new automation under **Settings → Automations & scenes**, open the three-dot menu, choose **Edit in YAML**, and paste it in. Then replace `binary_sensor.apollo_msr_2_abc123_radar_target` with your radar's **Radar Target** sensor, and `your_device_id` with your radar. To fill in the device without looking up its ID, switch the action to the visual editor and pick your radar under **Radar Device**. If the action is refused before it starts (the radar is offline, for example), the automation stops with an error at that step instead of sending the notification.

[![Open your Home Assistant instance and show your automations.](https://my.home-assistant.io/badges/automations.svg)](https://my.home-assistant.io/redirect/automations/)

Each call calibrates one radar. Two related actions round it out: `apollo_mmwave.cancel_calibration` stops a running job, and `apollo_mmwave.restore_gate_thresholds` does what **Undo** does. The card offers only the newest saved thresholds, while the action can restore an older set with its `snapshot_id` field. **Settings → Tools → Actions** lists every field, and the button below opens it with `apollo_mmwave.calibrate_gates` selected.

[![Open your Home Assistant instance and show your action tools with a specific action selected.](https://my.home-assistant.io/badges/tools_perform_action.svg)](https://my.home-assistant.io/redirect/tools_perform_action/?service=apollo_mmwave.calibrate_gates)

!!! warning "Only automate it for a room you know is empty"

    A person sleeping or a pet napping can look like an empty room to an automation. Pick a time and a room where nobody is, and remember each run replaces any thresholds you set by hand.

## Troubleshooting

### The radar still triggers with nobody there

A calibration sets each threshold a margin above the highest energy it heard during a one-minute listen. Something that moves now and then, like a fan that cycles or the heating coming on, may not have moved during that minute.

1. Update Apollo mmWave to 2.2.4 or newer and press **Calibrate with empty room** again. 2.2.4 leaves more headroom above the room's noise (15 points instead of 10).
2. Calibrate while whatever usually runs in the room is running: the fan on, the heating or air conditioning cycling. If it only comes on now and then, listen for longer so a cycle falls inside the listen, for example 5 minutes (`duration_s: 300`, set the same way as `margin` in step 3).
3. Still too sensitive? Raise `margin`, the points added above each gate's peak, for example to 20 or 25, and calibrate again. It sets the headroom on most gates. The percentage (`margin_pct`) only takes over on gates whose peak is 43 or more at the defaults, such as gates right at the sensor, so raising it changes little in most rooms. There are two places to set it:
    - **For one run, on any dashboard:** open **Settings → Tools → Actions**, pick **Calibrate gate thresholds (empty room)**, choose your radar under **Radar Device**, tick **Headroom (points)** and set it to 20 (and **Listen for (seconds)** for a longer listen), then press **Perform action** and leave the room. The Auto-calibrate card shows the run as it goes.

        [![Open your Home Assistant instance and show your action tools with a specific action selected.](https://my.home-assistant.io/badges/tools_perform_action.svg)](https://my.home-assistant.io/redirect/tools_perform_action/?service=apollo_mmwave.calibrate_gates)

    - **For every run, on your own dashboard:** add a `calibration` block to the Auto-calibrate card's YAML. **Calibrate with empty room** then uses it each time:

        ```yaml
        type: custom:apollo-radar-calibrate-card
        device_id: your_device_id
        calibration:
          margin: 20
          duration_s: 300
        ```

        The keys go under `calibration:`. Typed at the card's top level, they are ignored. On the Apollo mmWave dashboard, the same block can go under `strategy:` in its raw configuration; the [Apollo mmWave configuration guide](https://github.com/ApolloAutomation/apollo-mmwave-main/blob/main/docs/configuration.md#auto-calibration) has the details.

4. If only one spot misbehaves, raise only that gate's threshold, as described in [Fine-tune gates by hand](#fine-tune-gates-by-hand).

If the radar now misses you instead, press **Undo (restore your previous values)**, or calibrate again with a smaller `margin`.

### Calibration will not start

The **Calibrate with empty room** button is disabled when the card cannot run a calibration. The card says why:

- **Radar is offline. Calibration needs the radar online and its gate entities enabled.** Check that the radar is powered and shows as online under **Settings → Devices & services → ESPHome**. If it is online, open your sensor's device page from that list and check that the **Radar Engineering Mode** switch and the gate threshold and gate energy entities are enabled. A disabled entity is listed under **+ N entities not shown**: select it, open its settings (the cog), turn on **Enabled**, and click **Update**.

    [![Open your Home Assistant instance and show an integration.](https://my.home-assistant.io/badges/integration.svg)](https://my.home-assistant.io/redirect/integration/?domain=esphome)

- **Background correction is running on the LD2412. Wait for its status to turn off.** (R PRO-1) Wait for **Background Correction Running** to turn off.
- **Apollo mmWave is still loading...** The integration is starting or reloading, and the card keeps trying on its own. If it changes to **Apollo mmWave is not loaded, so calibration is unavailable.**, press **Retry**. If that keeps happening, check **Settings → Devices & services** for an error on the Apollo mmWave integration.

    [![Open your Home Assistant instance and show an integration.](https://my.home-assistant.io/badges/integration.svg)](https://my.home-assistant.io/redirect/integration/?domain=apollo_mmwave)

If the button works but the card answers with a line starting **Calibration failed:**, the rest of the line says what went wrong, and **Try again** runs it again once you have fixed it. The common ones:

- **The radar is unavailable right now. Check that it is online, then try again.** The radar dropped off the network.
- **Home Assistant could not turn Radar Engineering Mode on within 10 s. Is the radar online?** The radar did not respond to the switch.
- **No gate energy readings arrived within 20 s of turning Radar Engineering Mode on.** Check that the radar is online and that **Radar Engineering Mode** on the Controls card brings the Gate Energy chart to life.
- **Radar Engineering Mode turned off during the listen. Nothing was changed.** Someone, or an automation, turned it off during the listen. Leave it on and try again.
- **The radar has not reported 18 of its threshold values yet.** The number is how many are missing: up to 18 on an MSR-1 or MSR-2, and up to 28 on an R PRO-1. The radar has not sent its thresholds to Home Assistant since it started, which can happen after it has been running for a long time. Press **Read settings from the radar** (the **Radar setup** card at the top of the tab offers it too): the card asks the radar for its settings, shows **Reading settings from the radar...**, and tries again a few seconds later. If the card can't find the radar's query params button, it says **Open the radar's device page, press its Query Params button in the Diagnostic section, wait a few seconds, then try again.**
- **Your Home Assistant user is not allowed to control this radar's entities.** Run the calibration from a Home Assistant user that can control the radar.

On an R PRO-1 without the [LD2412 addon](/products/rpro1/addons/add-the-ld2412-mmwave-sensor-to-r-pro-1.md), there's no radar behind the LD2412 cards, so the Auto-calibrate card can't calibrate. Depending on what the sensor reports, the card either reads **Radar is offline. Calibration needs the radar online and its gate entities enabled.** with its buttons disabled, or answers **Calibrate with empty room** with **The radar has not reported 28 of its threshold values yet.** Reading the settings from the radar can't fix either one. Skip the calibration: the [zone map](#draw-zones-on-the-r-pro-1-and-mtr-1) is what that sensor uses.

### Radar Engineering Mode was left on

The calibration only turns Radar Engineering Mode off if it was the one that turned it on. If you turned it on yourself, or with the button on the Gate Energy chart, it stays on until you turn it off. The **Radar setup** card at the top of the tab says so while it's on: press its **Turn off Radar Engineering Mode** button, or use the **Radar Engineering Mode** switch on the **Controls** card.

If Home Assistant restarted during the countdown or the listen, nothing was written: the calibration turns Radar Engineering Mode back off when Home Assistant starts again, and the card says, for example, **Last calibration Oct 12, 12:37 AM was stopped by a Home Assistant restart. Nothing was changed.** Press **Calibrate with empty room** to run it again.

If Home Assistant restarted while thresholds were being written, or the radar went offline before the calibration could turn the mode off, the Auto-calibrate card shows a banner the next time you open it. It starts with **A calibration was interrupted by a restart.** or **The last calibration could not turn Radar Engineering Mode back off (the radar was offline).** Press **Turn it off** next to **Radar Engineering Mode may still be on.** If the banner also says **Some thresholds may have been written.**, press its **Undo** to put the saved thresholds back, then run the calibration again.

!!! tip "Keep Radar Engineering Mode out of your history"

    While Radar Engineering Mode is on, the radar updates its 18 (MSR-1 and MSR-2) or 28 (R PRO-1) gate energy sensors about once a second, and Home Assistant's recorder, the part that saves history, stores every update. Turning the mode off when you're done avoids this. If you like to leave it on to watch the chart, add the block below to your `configuration.yaml` (the **File editor** app is one way to open it), then restart Home Assistant. If the file already has a `recorder:` section, add the `exclude:` lines to it instead of adding a second `recorder:` key.

    [![Open your Home Assistant instance and show the dashboard of an app.](https://my.home-assistant.io/badges/supervisor_app.svg)](https://my.home-assistant.io/redirect/supervisor_app/?app=core_configurator)

    ```yaml title="configuration.yaml"
    recorder:
      exclude:
        entity_globs:
          - sensor.*_g?_move_energy     # LD2410: g0 to g8
          - sensor.*_g?_still_energy
          - sensor.*_g??_move_energy    # LD2412: g00 to g13
          - sensor.*_g??_still_energy
    ```

### Thresholds did not change on the radar

- **You ran a preview.** **Preview only** never writes anything. Press **Calibrate and apply**, or **Calibrate with empty room**.
- **The new value matched the old one.** Cells that read **(unchanged)** were already right, so nothing was written.
- **The gate had no data.** Gates marked **no data** keep their old thresholds. Check the radar's connection and run the calibration again.
- **The radar did not confirm the value.** Cells marked **(not confirmed)** and the warning that values could not be confirmed mean the radar did not report the new value back. Check the gates on the **Move Thresholds** and **Still Thresholds** cards, then run it again once the radar is stable, or set those gates by hand.
- **The run was stopped.** **Stopped. Nothing was changed.** means nothing was written.

### The chart says to turn on Radar Engineering Mode

If the chart instead reads **Radar unavailable** and **Waiting for the device to reconnect**, the radar is offline and the button is hidden until it comes back: check its power and Wi-Fi. Otherwise, the Gate Energy chart only shows bars while Radar Engineering Mode is on. Press **Turn on Radar Engineering Mode** on the chart itself, or turn on **Radar Engineering Mode** on the **Controls** card. The bars appear within a few seconds, once the radar starts sending energy. If the calibration turned the mode on, it turns it back off when it finishes, so the overlay returning after a calibration is expected.

![The Gate Energy chart while Radar Engineering Mode is off: the plot is dimmed behind the message and the Turn on Radar Engineering Mode button](/assets/apollo-mmwave-gate-energy-engineering-off.png)

!!! tip "Prefer the radar maker's app?"

    The HLKRadarTool app connects over the radar's Bluetooth (the **Radar Bluetooth (HLK app)** row on the **Controls** card, or on **LD2450 Controls** for the LD2450) and has its own auto-calibration. Each sensor has its own guide: [MSR-1](/products/msr1/setup/zones-hlk.md), [MSR-2](/products/msr2/setup/zones-hlk.md), [R PRO-1](/products/rpro1/setup/zones-hlk.md), and [MTR-1](/products/mtr1/setup/zones-hlk.md).

### The zone map shows nobody, or only one person

Start with the LD2450's **Radar setup** card, right above the map.

**No dot at all.** The usual cause is **Zone Type** set to **Detection**: the radar then reports only people inside its own built-in zones, and with none set it reports nobody. Press **Set Zone Type to Disabled**, or **Use recommended settings** if the card shows that instead. If Zone Type is already **Disabled** and **Presence** on the **LD2450 Live** card stays off with you in front of the sensor, the radar itself sees nobody: check that it's online and facing the room.

**One dot with several people in the room.** Usually **Multi Target Tracking** is off. Press **Turn on Multi Target Tracking** (or **Use recommended settings** if the card shows that instead) on the Radar setup card. On an R PRO-1, Home Assistant hides that setting by default, so the card can't check it and shows no button. Enable it once:

1. Open the sensor's device page with **All settings for this device →** on the **Start here** card.
2. Under **Configuration**, open the entities that aren't shown and select **LD2450 Multi Target Tracking**.
3. Open its settings (⚙), turn on **Enabled**, and select **Update**.
4. Reload the dashboard after a minute. The Radar setup card then checks the setting and offers its button when it's off.

### The dots sit at the sensor, or a zone misses you

Apollo mmWave 2.2.7 fixed this. Before it, when Home Assistant used US customary units (or you changed a Target X or Target Y sensor's unit), the zone map read the radar's positions in inches as if they were millimeters. The dots sat at or right around the sensor, and zone presence didn't turn on. Update Apollo mmWave (see [Upgrade from an older setup](apollo-mmwave-dashboard-setup.md#upgrade-from-an-older-setup)) and the dots land where people are.

A zone you drew while the dots were in the wrong place may not cover where people show up now. Walk through the room, watch the dots, and redraw any zone that's off.

### A slider won't move

The sliders on **Detection Range**, **Move Thresholds**, and **Still Thresholds** start locked. Press **Unlock** on the **Sliders locked** row above them (see [Set the range and timeout](#set-the-range-and-timeout)). The **Cone rotation** slider on the zone map locks with the map: press **Locked** on the map first.

### Send Apollo a support file

Still stuck? Send Apollo a support file with your question. It holds the Apollo mmWave and Home Assistant versions, the dashboard's state, and each radar's model, firmware, settings, zones, and last calibration. It leaves out MAC and IP addresses, Wi-Fi network names, and tokens, and downloading it changes nothing. Only administrators can download it.

1. Go to **Settings → Devices & services** and open **Apollo mmWave**. The **Device** card at the bottom of each tab links there too.

    [![Open your Home Assistant instance and show an integration.](https://my.home-assistant.io/badges/integration.svg)](https://my.home-assistant.io/redirect/integration/?domain=apollo_mmwave)

2. Open the three-dot menu and choose **Download diagnostics**.
3. Attach the file to your message to [Apollo support](/products/general/contact-us/contact-us-support.md), or to your issue on [GitHub](https://github.com/ApolloAutomation/apollo-mmwave-main/issues).

!!! warning "Check the file before you post it publicly"

    The file includes your zones and their names, which can show the layout of your home. Send it to Apollo support, or look through it before you attach it to a public GitHub issue.
