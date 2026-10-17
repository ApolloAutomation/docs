---
title: Tim's AIR-1 ERV whole-home solution
description: How AIR-1 owner Tim built a whole-home ventilation system with an AIR-1 inside it and logs its readings in a custom Grafana dashboard.
---
# Tim's AIR-1 ERV whole-home solution

Tim, an Apollo AIR-1 owner, built a whole-home ventilation system (an ERV, or energy recovery ventilator) and put an AIR-1 inside it. Here's what his setup is made of, the data he tracks, and why he built it.

## The setup

Tim's system has three main parts:

- **Controller:** an ESP32-C6 that drives two single-phase inverters through two MCP4725 DACs (digital-to-analog converters) and four relays.
- **Ventilator:** an o3ozon CWP250, which Tim lists as an HRV (heat recovery ventilator).
- **Ducts:** zinc-plated steel at fi160, with the distribution to the vents at 90mm max.

![ERV with AIR-1 inside](/assets/tim-air-1-example-pic-1.jpg)

## The data

Tim logs his AIR-1 readings into a custom Grafana dashboard:

![Grafana showing AIR-1 data](/assets/tim-air-1-example-pic-2.png)

## Why Tim built it

!!! quote "Tim's warning to others"

    My sinuses burned constantly due to lack of ventilation. It was probably CO poisoning in the past, and also temperature inversions in my mountainous valley, which cause massive spikes in smog even though the air is relatively good beyond that. My home was working as a reservoir of smog.
