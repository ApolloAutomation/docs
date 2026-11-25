---
title: Mount your radar high or on the ceiling
description: Choose Wall, High, or Ceiling for an LD2450 or LD2460 radar on the Apollo mmWave Dashboard zone map, then set the heights, rotation, coverage zone, Walk, and edge test step by step.
---

# Mount your radar high or on the ceiling

A tracking radar doesn't have to sit at chest height on a wall. From Apollo mmWave Dashboard 2.5.0, the zone map knows how your radar is mounted: on a wall, high up and tilted down, or on the ceiling looking straight down. Tell it once under **Map settings**, and the dots on the map, your zones, their hold times, Walk, and History all use positions measured across the floor, so a zone you draw by the couch stays by the couch wherever the sensor hangs.

This guide covers the LD2450 radar in the Apollo R PRO-1 and Apollo MTR-1, and LD2460 tracking radars (ESPHome devices that use ESPHome's `ld2460` component). Each guide below takes about ten minutes once the sensor is up.

!!! note "Before you start"

    - Apollo mmWave Dashboard **2.5.0 or newer** is installed. Older versions treat every radar as a wall mount. To update, see [Update Apollo mmWave Dashboard](apollo-mmwave-dashboard-setup.md#update-apollo-mmwave).
    - You're signed in to Home Assistant as an administrator. Other users see the mount in use but can't change it.
    - Your sensor's tab has a zone map. If it doesn't, start with the [Apollo mmWave Dashboard setup guide](apollo-mmwave-dashboard-setup.md).
    - You have a tape measure, and a phone or tablet with the dashboard open for the tests.

!!! warning "Check the zones you already have"

    Choosing **High** or **Ceiling** moves the dots to where people are on the floor, closer to the sensor than before. Zones keep the shape you drew, so a zone drawn on **Wall** for a sensor that hangs high no longer covers the same people. After you set the mount, walk through each zone and redraw any that's off (see [A zone drawn before the change is in the wrong place](#a-zone-drawn-before-the-change-is-in-the-wrong-place)).

## Choose a mount

| Mount | Radars | Where the sensor goes | What it covers | Best for |
| --- | --- | --- | --- | --- |
| **Wall** (the default) | LD2450, LD2460 | On a wall at about chest height, looking straight out | A cone about 6 m (20 ft) out and 120 degrees wide | Most rooms, and every setup from before 2.5.0 |
| **High** | LD2450 | High on a wall or in a ceiling corner, about 2 to 2.7 m (6.5 to 9 ft) up, tilted down | From a near edge (about 0.6 m out at 2.2 m up and 30 degrees down) to about 5.9 m out | A whole room, with the sensor out of reach |
| **Ceiling** | LD2450 | On the ceiling near a wall, looking straight down | A strip along that wall, about 5.9 m long and 1.2 m deep under a 2.7 m (9 ft) ceiling | A hallway, a doorway, a bedside, or a desk |
| **Ceiling** | LD2460 | In the middle of the ceiling, looking straight down | A circle up to 4 m (13 ft) out from the spot under it | A whole room from above |

If your sensor sits at about chest height and looks straight out, keep **Wall**: nothing changes from earlier releases. For a whole room with an LD2450 up high, choose **High**. **Ceiling** on an LD2450 sees a narrow strip by the nature of its antennas, so pick it for a strip you want to watch, not a whole room.

![Two diagrams. The first, High mount seen from the side: a radar 2.2 m up a wall, tilted down 30 degrees, with its beam spreading 35 degrees up and down across the room. A dashed line marks a person's chest height of 1 m, a bracket marks the 1.2 m drop from the radar down to it, and a person stands 1 m from the wall. A red line from the radar to the person's chest is labeled The radar reports 1.56 m, and a blue arrow along the floor is labeled High shows 1.0 m out from the wall. Ticks on the chest line mark the near edge, about 0.6 m, and the far edge, about 5.9 m. The second, Ceiling mount seen from above: a radar 2.7 m up on the wall line, a strip under it on the room side about 5.9 m along the wall and about 1.2 m into the room, and an arrow along the wall labeled Walking along the wall moves your dot left and right](/assets/apollo-mmwave-mount-diagram.png)

### Why the heights matter

The LD2450 measures how far away someone is and their angle left or right, but not whether they're above or below it. From up high, the distance it reports includes the drop from the radar down to the person, so someone 1 m from the wall reads about 1.6 m out from a radar 2.2 m up. On **High** and **Ceiling**, the map takes that drop out using the mount height and the height of a person's chest, which is where the radar sees people best. Tilt changes what the radar covers, never where it places someone, so the map only uses tilt to draw the area it covers.

For a radar 2.2 m (7.2 ft) up and a person 1 m (3.3 ft) tall at the chest:

| Out from the wall | The radar reports | High shows |
| --- | --- | --- |
| 0.5 m | 1.30 m | 0.50 m |
| 1 m | 1.56 m | 1.00 m |
| 2 m | 2.33 m | 2.00 m |
| 3 m | 3.23 m | 3.00 m |
| 5 m | 5.14 m | 5.00 m |

An LD2460 corrects its own readings for how it's mounted, so it only needs to know whether it's on a wall or the ceiling, and how high the ceiling is.

<video src="/assets/apollo-mmwave-mount-switch.mp4" poster="/assets/apollo-mmwave-mount-switch-poster.jpg" autoplay loop muted playsinline aria-label="Map settings on an LD2450 zone map in feet, with two people tracked. With Mounted on set to Wall, the map shows the radar's 120 degree view cone and the line In use: Wall, the default. Choose High or Ceiling if the sensor is mounted up high. Pressing High turns the cone into a fan that starts a little out from the wall, adds the Test near and far edge button and Add coverage zone under the map, and the line reads In use: High, as chosen here. Pressing Ceiling turns it into a strip along a dashed wall line, with Test wall line and edge, and the line reads In use: Ceiling, as chosen here. Pressing Wall brings the cone back."></video>

## Mount an LD2450 high on a wall

A high mount keeps the sensor out of reach and lets it look over furniture, so it sees the whole room instead of the back of the couch. Here's how to set it up:

1. Mount the sensor 2 to 2.7 m (6.5 to 9 ft) up, on a wall or in a ceiling corner, facing into the room. Keep it level from side to side, so it isn't rolled, and tilt it down 25 to 35 degrees.
2. On the sensor's tab, open **Map settings** at the bottom of the zone map. **Tilt down:** and **Cone rotation:** lock with the map, so if the map reads **Locked**, press it to unlock (see [Lock and unlock](apollo-mmwave-dashboard.md#lock-and-unlock)).
3. Under **Mounted on**, press **High**. The card shows **Map set to a high mount**, and the line under the buttons reads **In use: High, as chosen here.**
4. Measure from the floor to the sensor and enter it in **Mount height** (1.2 to 4 m, or 3.9 to 13.1 ft). The field uses the map's units.
5. Drag **Tilt down:** to roughly how far the sensor points down from level, from 0 to 60 degrees. A rough guess is fine: the hint under it reads **How far the sensor points down from level. Tilt changes what it covers, not where it places people.**
6. Leave **Person height** at 1 m (3.3 ft), the chest height of most adults standing. If the room is mostly for sitting, such as a home theater, lower it to about 0.7 m (2.3 ft).
7. Read the coverage line under the fields, such as **Covers from about 1.8 ft to 19.3 ft out from the wall.** Closer than the near edge, people are under the radar's view. To see closer, tilt the sensor down more and update **Tilt down:**.
8. Drag **Cone rotation:** until the drawing points the way the sensor faces, as [Match the map to how the sensor is mounted](apollo-mmwave-dashboard.md#match-the-map-to-how-the-sensor-is-mounted) shows.

![Map settings on an LD2450 zone map in feet with High picked under Mounted on: In use: High, as chosen here., Mount height 7.2 ft, the Tilt down: slider at 30 degrees with the hint How far the sensor points down from level. Tilt changes what it covers, not where it places people., Person height 3.3 ft with the hint The height of a person's chest, where the radar sees them best. 1 m (3.3 ft) suits most adults standing., then the lines Covers from about 1.8 ft to 19.3 ft out from the wall., Closer than that, people are under the radar's view. Tilt it down more to see closer., Positions are worked out from the mount height and person height. They are least accurate close under the radar and for people sitting or lying down., and The radar's built-in zones use its own uncorrected coordinates, so on a High or Ceiling mount they do not line up with this map. Draw zones here instead., followed by the Cone rotation: slider at 0 degrees](/assets/apollo-mmwave-mount-high-settings.png)

On a phone, **Map settings** stacks into one column, with the three mount buttons across the full width.

![Map settings on a phone, in feet, with High picked under Mounted on: the Wall, High, and Ceiling buttons across the full width, then Mount height 7.2 ft, the Tilt down: slider at 30 degrees, Person height 3.3 ft, the coverage line Covers from about 1.8 ft to 19.3 ft out from the wall., and the near edge, accuracy, and built-in zones notes, each wrapped to the phone's width](/assets/apollo-mmwave-mount-phone.png){ .phone-media }

The map now draws the area the radar covers in place of the cone, starting at the near edge and fanning out to the far edge. Walk into the room: your dot shows how far you are from the wall across the floor, not the slanted distance the radar measured.

<video src="/assets/apollo-mmwave-mount-high.mp4" poster="/assets/apollo-mmwave-mount-high-poster.jpg" autoplay loop muted playsinline aria-label="An LD2450 zone map on a High mount, locked, in feet, with the radar's coverage drawn as a fan from a near edge a little out from the wall to a far edge, and a zone named Desk in the middle of it. Dot 1 starts at the near edge and walks straight out from the wall, leaving a short trail. While the dot is inside Desk, the zone fills in solid with a solid outline, and once the dot walks past it, Desk goes back to a pale fill with a dashed outline."></video>

Your sensor is now mapped from up high. Next, test the edges and draw your zones (see [Test the edges](#test-the-edges) and [Add a zone that covers everything](#add-a-zone-that-covers-everything)).

## Mount an LD2450 on the ceiling

Looking straight down, an LD2450 sees a strip along one line: about twice as long as the ceiling is high, and less than half as deep. That suits a hallway, a doorway, the side of a bed, or a desk. There's one catch to plan for: from straight above, the radar can't tell which side of it someone is on.

!!! tip "Why mount it near a wall"

    The LD2450 measures angles with two antennas side by side. Looking down, it knows how far along that line you are, and how far from the line, but not which side of the line. The zone map puts everyone on one side, the room side. Mount the sensor close to a wall and turn it so walking along the wall moves your dot left and right on the map. Then the wall is the line, everyone in the room is on the room side, and the map is right.

Here's how to set it up:

1. Pick the strip to watch, and the wall beside it. Mount the sensor on the ceiling close to that wall, looking straight down.
2. Turn the sensor so that its long side runs along the wall. You'll check this in step 7.
3. On the sensor's tab, open **Map settings** at the bottom of the zone map and press **Ceiling** under **Mounted on**. The card shows **Map set to a ceiling mount**.
4. Measure from the floor to the ceiling and enter it in **Ceiling height** (2 to 4 m, or 6.6 to 13.1 ft).
5. Leave **Person height** at 1 m (3.3 ft) unless people there are mostly sitting or lying down.
6. Read the coverage line, such as **Covers a strip about 5.9 m along the wall and 1.2 m into the room.** The box above **Flip room side** explains the one-side rule in the card's own words.
7. Walk along the wall under the sensor. Your dot should move left and right along the dashed wall line. If it moves up and down instead, turn the sensor a quarter turn on the ceiling and try again.
8. Step away from the wall into the room. If your dot shows up past the wall line, on the side where the room isn't, tick **Flip room side**. Zones stay where they are when you flip it, so redraw any zone drawn for the other side.
9. Drag **Map rotation:** until the map's grid lines up with the room's walls. On a ceiling the whole map turns, not a cone. The slider locks with the map, so unlock it first if it's gray.

![Map settings on an LD2450 zone map in feet with Ceiling picked under Mounted on: In use: Ceiling, as chosen here., Ceiling height 8.9 ft, Person height 3.3 ft with its hint, then a box that reads Looking straight down, this radar cannot tell which side of it someone is on, so it shows everyone on one side. Mount it near a wall, turned so walking along the wall moves your dot left and right. Everyone in the room is then on the room side. If people show up past the wall line, turn on Flip room side., an unticked Flip room side box with the line Zones stay where they are, so redraw any zone drawn for the other side., the lines Covers a strip about 19.3 ft along the wall and 3.9 ft into the room., A ceiling sensor of this kind sees a narrow strip. For a whole room, mount it high on a wall and choose High., the accuracy and built-in zones notes, and the Map rotation: slider at 0 degrees](/assets/apollo-mmwave-mount-ceiling-settings.png)

<video src="/assets/apollo-mmwave-mount-ceiling.mp4" poster="/assets/apollo-mmwave-mount-ceiling-poster.jpg" autoplay loop muted playsinline aria-label="An LD2450 zone map on a Ceiling mount in feet, under a caption that reads Map settings: Flip room side is off. The radar is a green dot on a dashed wall line at the top of the map, with its coverage drawn as a strip below the line. Dot 1 walks along the strip from left to right, leaving a trail. The caption changes to Map settings: Flip room side is on, and the strip and the dot move to the other side of the wall line, where the dot walks back from right to left. The caption changes back to off, and the strip returns below the wall line."></video>

The strip is now on the map, on the room side of the wall line. Next, check where it starts and ends (see [Test the edges](#test-the-edges)).

## Set up an LD2460 tracking radar

An LD2460 tracks up to 5 people. Its tab works like an LD2450 tab, and its **Map settings** offer **Wall** and **Ceiling**. The radar corrects its own readings for its height and tilt, so you don't enter a mount height or a person height.

1. On a wall, mount the radar 2.2 to 2.7 m (7 to 9 ft) up, tilted down 25 to 40 degrees. On the ceiling, mount it 2.5 to 3 m (8.2 to 9.8 ft) up, looking straight down, near the middle of the room.
2. Check **Installation Mode** under **LD2460 Live** on the tab: **side** for a wall, **top** for a ceiling. The radar reports it when the device starts, and while it reports one, the zone map follows it: the buttons under **Mounted on** are grayed out, with **In use: Ceiling. The radar reports a ceiling mount.** (or **Wall**). The dashboard can't change the mode. If it doesn't match how the radar now hangs, change the installation setting on the radar itself, where your device's firmware offers one.
3. If **Installation Mode** is missing or unknown, the buttons under **Mounted on** are available: open **Map settings** and press **Wall** or **Ceiling** yourself. An LD2460 has no **High**: on a wall, the radar corrects its own readings for its height and tilt.
4. On a ceiling, enter **Ceiling height**. The line under it says how far the radar sees, such as **The radar covers up to 13.1 ft out from the spot under it, its most.** Above 3 m (9.8 ft), people far from the center may be missed.
5. Drag **Map rotation:** until the grid lines up with the room's walls.

![Map settings on an LD2460 zone map in feet: Mounted on with Wall and Ceiling grayed out and Ceiling picked, the line In use: Ceiling. The radar reports a ceiling mount., Ceiling height 8.9 ft with the line The radar covers up to 13.1 ft out from the spot under it, its most., and the Map rotation: slider at 0 degrees with the hint Turn the map until its grid lines up with the room's walls. Zones match the room only while the sensor stays mounted that way.](/assets/apollo-mmwave-ld2460-mount-settings.png)

On a ceiling, the map puts the radar in the middle and draws a circle around it. With no zones yet, **Add whole-room zone** under the **Zones** heading adds a zone over everything the radar sees in one press, and a zone's editor offers **Whole room** with **Square** and **Circle** under **Draw shape**. Then press **Test center and edge** to check the circle (see [Test the edges](#test-the-edges)).

<video src="/assets/apollo-mmwave-ld2460-ceiling.mp4" poster="/assets/apollo-mmwave-ld2460-ceiling-poster.jpg" autoplay loop muted playsinline aria-label="An LD2460 zone map on a ceiling mount in feet, with the radar as a green dot in the middle of a circle of coverage and two people tracked. Add whole-room zone is pressed, and Zone 1 fills the circle and lights up. Test center and edge is pressed: the checks Right under the radar and At the edge appear with the line More than one person is in view. Only the person testing should be in the room. Once one person is left, they walk to the spot under the radar, Right under the radar gets a check mark, and the line reads You are right under the radar. It sees you here. They walk out toward the edge, with lines such as You are 10.2 ft from the spot under the radar, 2.9 ft from the edge., and at the edge At the edge gets a check mark and the line reads You are at the edge of what the radar sees, about 13.1 ft out. Leaving from here counts as leaving, so held zones turn off without waiting."></video>

## Add a zone that covers everything

On **High** and **Ceiling**, an LD2450 map offers **Add coverage zone** under the **Zones** heading while the radar has no zones. One press adds a zone with the shape of everything the radar covers at this mount, so you get a presence sensor for the whole view right away. On a zone you already have, press **Coverage** under **Draw shape** in its editor, which reads **Gives this zone the shape of everything the radar covers at this mount.** On an LD2460 ceiling, the same buttons are **Add whole-room zone**, and **Square** and **Circle**.

<video src="/assets/apollo-mmwave-coverage-zone.mp4" poster="/assets/apollo-mmwave-coverage-zone-poster.jpg" autoplay loop muted playsinline aria-label="An LD2450 zone map on a High mount in feet, with no zones yet and the radar's coverage drawn as a fan. Add coverage zone is pressed, and Zone 1 appears with the fan's shape, a dot on each corner, and its button under Zones. Dot 1 walks into the room from the far left, and Zone 1 fills in solid while it's inside."></video>

Draw smaller zones over the couch, the desk, or the bed the usual way: [Add a zone](apollo-mmwave-dashboard.md#add-a-zone) and [Draw a zone](apollo-mmwave-dashboard.md#draw-a-zone). [Mark corners by walking](apollo-mmwave-dashboard.md#mark-corners-by-walking) works on every mount, and the corners you mark land where you stood on the floor.

## Test the edges

Each mount has a test that shows where the radar sees you and where its view ends. Leaving the view at its edge counts as leaving, so a zone with a hold time turns off without waiting, while someone who vanishes in the middle of the view keeps a held zone on. The test shows you where those edges are in your room. Be the only person in the room, and take a phone or tablet with the dashboard open.

1. Press the test button under the map: **Test near and far edge** on **High**, **Test wall line and edge** on an LD2450 **Ceiling**, or **Test center and edge** on an LD2460 ceiling.
2. Walk to the first check. On **High**, walk toward the wall until the line reads **You are at the near edge. Any closer and the radar loses you.** On an LD2450 ceiling, stand under the sensor until it reads **You are right under the radar, on the wall line.** On an LD2460 ceiling, stand under it until it reads **You are right under the radar. It sees you here.**
3. Walk slowly out. The line tells you how far you are and how far from the edge, such as **You are 9.2 ft out, 7.3 ft from the edge of what the radar sees.**
4. Keep going until the second check gets its tick, such as **You are at the far edge, about 19.3 ft out.** Step past it, and the line says where the radar lost you.

<video src="/assets/apollo-mmwave-mount-high-test.mp4" poster="/assets/apollo-mmwave-mount-high-test-poster.jpg" autoplay loop muted playsinline aria-label="Test near and far edge on an LD2450 zone map on a High mount in feet. The fan of coverage gets a thick outline, and the checks Near edge and Far edge appear under the map with the line Nobody is in view. Walk into the room to start. Dot 1 appears at the near edge, the near edge glows, Near edge gets a check mark, and the line reads You are at the near edge. Any closer and the radar loses you. The dot walks straight out, with lines such as You are 9.2 ft out, 7.3 ft from the edge of what the radar sees. At the far edge, the far edge glows, Far edge gets a check mark, and the line reads You are at the far edge, about 19.3 ft out. The dot vanishes, and the line reads Lost you at 19.2 ft out, at the edge. That is the end of the radar's view."></video>

<video src="/assets/apollo-mmwave-mount-ceiling-test.mp4" poster="/assets/apollo-mmwave-mount-ceiling-test-poster.jpg" autoplay loop muted playsinline aria-label="Test wall line and edge on an LD2450 zone map on a Ceiling mount in feet. The strip gets a thick outline, and the checks Wall line and At the edge appear under the map. Dot 1 stands under the radar on the dashed wall line, Wall line gets a check mark, and the line reads You are right under the radar, on the wall line. The dot walks out into the room to the strip's far edge, At the edge gets a check mark, and the line reads You are at the far edge, about 3.9 ft out. It then walks along the strip to its side edge, and the line reads You are at the side edge of what the radar sees. Leaving from here counts as leaving."></video>

If the test loses you in the middle of the view, something blocks the radar there, or you stood still too long. A tick on both checks means the mount is set up: the map and hold times now match where the radar's view starts and ends. The tests don't check your zones, so walk through each zone you drew before the change and redraw any that's off.

!!! success "Next step: use your zones in automations"

    Your radar is mapped from where it hangs. Now make a zone do something: each zone has its own presence sensor.

    [Use the zone sensors](apollo-mmwave-dashboard.md#use-the-zone-sensors){ .md-button .md-button--primary }

## What accuracy to expect

The heights turn a slanted distance into a floor distance, and a small error in the reading grows a little on the way. Here's what to expect:

- **Close under the radar** is least accurate. On a ceiling 2.7 m (9 ft) up, a 10 cm error in the reading moves a dot about 28 cm 0.5 m out from the wall line, and about 11 cm 3 m out. Errors shrink with distance.
- **Sitting or lying down** puts the chest lower than **Person height**, so people show a little farther out than they are. Someone seated (chest about 0.7 m) under a radar 2.7 m up, with the default 1 m, shows about 1.2 m out when they're 0.5 m out, and about 2.3 m out when they're 2 m out. Lower **Person height** if the room is mostly seated.
- **The edges are soft.** A radar beam fades out rather than stopping at a line, so the coverage on the map is about right, not exact. **Test the edges** shows where they are in your room.
- **Tilt** never changes where a dot lands, only what's covered.
- **History** is drawn with the mount settings in use now, not the ones in use when it was recorded. The panel reads **History is drawn with the mount settings in use now.**

## Why built-in zones don't line up

The LD2450's own built-in zones (the **Zone Type** setting and the zone coordinates on the R PRO-1 and MTR-1) are worked out by the radar chip itself, using the slanted distances it measures. The integration can't correct them, so on **High** or **Ceiling** they don't line up with the map. Leave **Zone Type** on **Disabled**, as the **Radar setup** card recommends, and draw zones on the zone map instead. The tab's built-in zones card and **Map settings** say the same: **The radar's built-in zones use its own uncorrected coordinates, so on a High or Ceiling mount they do not line up with this map. Draw zones here instead.**

## Troubleshooting

### Dots show past the wall line on a ceiling LD2450

The radar can't tell which side of it someone is on, so the map picks one. Tick **Flip room side** under **Map settings**, then redraw any zone you drew on the wrong side. If dots jump from one side of the wall line to the other, the sensor is turned the wrong way: turn it so walking along the wall moves your dot left and right, as step 7 of [Mount an LD2450 on the ceiling](#mount-an-ld2450-on-the-ceiling) shows.

### People vanish close to a high sensor

They're closer than the near edge, under the radar's view. The coverage line, such as **Covers from about 1.8 ft to 19.3 ft out from the wall.**, says where the view starts. Tilt the sensor down more, then set **Tilt down:** to match. At 45 degrees down, a sensor 2.2 m (7.2 ft) up sees from about 0.2 m (0.7 ft) out.

### Dots sit too far out, or a zone turns on late

Check that **Mounted on** matches how the sensor hangs: on **Wall**, a sensor up high shows people farther out than they are. Then measure **Mount height** or **Ceiling height** again, and lower **Person height** if the room is mostly for sitting. The [support file](apollo-mmwave-dashboard.md#send-apollo-a-support-file) lists each radar's mount and the settings in use.

### The mount buttons are grayed out

On an LD2460 that reports its **Installation Mode**, the radar decides, and the line under the buttons says which mount it reports. The buttons become available only while **Installation Mode** is missing or unknown. If the reported mode doesn't match how the radar hangs, change the installation setting on the radar itself, where your device's firmware offers one; the dashboard can't change it. An LD2460 has no **High** in any case. Only administrators can change the mount, so check that you're signed in as one. If **Tilt down:** is grayed out, the map is locked: press **Locked** on the map to change it.

### A zone drawn before the change is in the wrong place

Zones keep the shape you drew. Positions change when you change the mount or its heights, so a zone drawn on **Wall** for a sensor that's really up high now sits farther from the wall than the people in it. Redraw it, or press **Coverage** in its editor to give it the whole view.
