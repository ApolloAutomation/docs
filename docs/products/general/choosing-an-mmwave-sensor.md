---
title: Choosing an mmWave Sensor
description: Compare the Apollo MSR-2, MTR-1, and R-PRO-1 mmWave presence sensors and pick the right one for your space.
---
# Choosing an mmWave Sensor

Apollo mmWave sensors detect the **moving** and **still** energy of people and animals, which makes them excellent for presence detection in a room. They are not meant to detect vehicles, so for a car an ultrasonic sensor is a better fit. This guide compares our three current mmWave sensors so you can pick the right one for your space.

<div class="grid cards" markdown>

-   :material-bed:{ .lg .middle } **MSR-2**

    ---

    Best still detection, for one person.

    [:octicons-arrow-right-24: MSR-2 overview](https://wiki.apolloautomation.com/products/msr2/introduction/)

-   :material-account-group:{ .lg .middle } **MTR-1**

    ---

    Tracks multiple people across zones.

    [:octicons-arrow-right-24: MTR-1 overview](https://wiki.apolloautomation.com/products/mtr1/introduction/)

-   :material-ethernet:{ .lg .middle } **R-PRO-1**

    ---

    Best of both worlds, plus PoE.

    [:octicons-arrow-right-24: R-PRO-1 overview](https://wiki.apolloautomation.com/products/rpro1/introduction/)

</div>

## Compare

| | MSR-2 | MTR-1 | R-PRO-1 |
|---|:---:|:---:|:---:|
| **Targets tracked** | 1 | Up to 3 | Up to 3 |
| **Multi-zone tracking** | :material-minus: | :material-check: 3 zones | :material-check: 3 zones |
| **Still detection** | :material-check: Excellent | :material-minus: Limited | :material-check: With LD2412 add-on |
| **PoE / Ethernet** | :material-minus: | :material-minus: | :material-check: |
| **Horizontal FoV** | 120° | 120° | 120°<br>150° with LD2412 |
| **Vertical FoV** | 70° | 70° | 70° |
| **Power** | USB-C | USB-C | PoE, Ethernet, Wi-Fi, USB-C |
| **mmWave module** | LD2410B | LD2450 | LD2450, optional LD2412 |

## Field of view

Each sensor watches a **cone** that fans out in front of it, like the beam of a flashlight. The cone is wider side to side than it is top to bottom.

<div class="grid" markdown>

<figure markdown="span">
<svg role="img" aria-label="Top-down view of the horizontal field of view, 120 degrees" viewBox="0 0 300 230" style="width:100%;max-width:340px;height:auto;">
  <path d="M40,115 L95,18 A112,112 0 0 1 95,212 Z" fill="#4379AA" fill-opacity="0.18" stroke="#4379AA" stroke-width="2"/>
  <line x1="40" y1="115" x2="152" y2="115" stroke="#4379AA" stroke-width="1" stroke-dasharray="4 4"/>
  <circle cx="125" cy="103" r="7" fill="#444"/>
  <rect x="120" y="110" width="10" height="18" rx="4" fill="#444"/>
  <rect x="20" y="101" width="28" height="28" rx="5" fill="#2d5a8a"/>
  <text x="74" y="121" font-size="18" fill="#2d5a8a" font-weight="bold">120°</text>
  <text x="34" y="147" font-size="9" fill="#2d5a8a" text-anchor="middle">sensor</text>
</svg>
<figcaption>Horizontal FoV: 120° side to side (up to 150° on the R-PRO-1 with the LD2412)</figcaption>
</figure>

<figure markdown="span">
<svg role="img" aria-label="Side view of the vertical field of view, 70 degrees" viewBox="0 0 300 230" style="width:100%;max-width:340px;height:auto;">
  <path d="M40,115 L155,34 A140,140 0 0 1 155,196 Z" fill="#4379AA" fill-opacity="0.18" stroke="#4379AA" stroke-width="2"/>
  <line x1="40" y1="115" x2="170" y2="115" stroke="#4379AA" stroke-width="1" stroke-dasharray="4 4"/>
  <circle cx="135" cy="103" r="7" fill="#444"/>
  <rect x="130" y="110" width="10" height="18" rx="4" fill="#444"/>
  <rect x="20" y="101" width="28" height="28" rx="5" fill="#2d5a8a"/>
  <text x="84" y="121" font-size="18" fill="#2d5a8a" font-weight="bold">70°</text>
  <text x="34" y="147" font-size="9" fill="#2d5a8a" text-anchor="middle">sensor</text>
</svg>
<figcaption>Vertical FoV: 70° top to bottom</figcaption>
</figure>

</div>

## Zone tracking (MTR-1 and R-PRO-1)

The LD2450 module tracks up to three moving targets and reports each one's X and Y position. You draw rectangular zones in those coordinates to decide where presence counts.

!!! tip "Setting LD2450 zone coordinates"

    - X1 must always be less than X2, and Y1 must always be less than Y2.
    - The X axis is where you can get tripped up, especially when both values are negative: -3456 is less than -2345.
    - The Y axis is easier since it is never negative.
    - The Plotly chart still draws the rectangles even if the X1/X2 or Y1/Y2 values are reversed, so double-check the order.
    - Zones cannot overlap.

To set up zones, follow the guide for your device: [MTR-1 zones](https://wiki.apolloautomation.com/products/mtr1/setup/zones-ha/) or [R-PRO-1 (LD2450) zones](https://wiki.apolloautomation.com/products/rpro1/setup/zones-ha/).

!!! tip "Beta: try the Zone Mapper"

    We are beta testing **Zone Mapper**, which makes drawing LD2450 zones much easier. It pairs a Home Assistant integration with a Lovelace card, so you can draw rectangular, elliptical, or polygonal zones right on a grid, watch your tracked targets move in real time, and get an occupancy sensor for each zone. Both install through HACS.

    Check it out on GitHub: [Zone Mapper integration](https://github.com/ApolloAutomation/zone-mapper) and [Zone Mapper card](https://github.com/ApolloAutomation/zone-mapper-card).

## Still detection (MSR-2 and R-PRO-1 with the LD2412)

The MSR-2, and the R-PRO-1 once you add the optional LD2412, detect a single target using gates: fixed distance bands rather than X and Y coordinates. This is what makes them so good at catching someone who is barely moving, like sleeping or sitting still. To add the second module to an R-PRO-1, follow [Add the LD2412 to your R-PRO-1](https://wiki.apolloautomation.com/products/rpro1/addons/add-the-ld2412-mmwave-sensor-to-r-pro-1/).

### Reducing false triggers

mmWave detects motion, so things that move or reflect the radar signal can trigger a sensor even when no one is there. Common culprits include:

- Mirrors and other reflective surfaces
- Fans and spinning blades
- Moving air from HVAC vents and registers
- Curtains, blinds, or plants swaying in a draft

The **MSR-2 (LD2410)** and the **R-PRO-1 with the LD2412** let you tune the sensitivity of each gate, so you can dial down the distance bands where a fan or vent sits and tune these false positives out. With the **LD2450 (MTR-1 and R-PRO-1)** you can instead draw your zones to exclude the problem area.

See the [Radar Tuning guide](https://wiki.apolloautomation.com/products/general/calibrating-and-updating/radar-tuning/zones-ha/) to adjust sensitivity.
