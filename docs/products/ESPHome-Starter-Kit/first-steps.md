---
title: ESPHome Starter Kit - First Steps
description: Landing page of the ESPHome Starter Kit QR Code.
---

# Welcome to the ESPHome Starter Kit

Welcome to the start of your ESPHome journey with the all-new **ESPHome Starter Kit**!

By the end of this wiki you'll know how to:

- Identify each part of your kit
- Snap the modules off the panel safely
- Get your ESP32-C6 board on Wi-Fi and talking to Home Assistant
- Write your very first ESPHome YAML config from scratch

## What's in the kit

Your kit arrives as a single snap-apart panel that contains the ESP32-C6 main board and a set of modules you can mix and match.

<!-- TODO: replace this with a labeled photo of the panel that calls out each module. Suggested filename: docs/assets/esk-1-panel-callouts.png -->

![](/assets/esk-1-panel-callouts.png)

## Snapping the panel apart

Each module is connected to the panel by small breakaway tabs. To separate them:

1. Hold the panel flat on a table with one hand on the module you want to remove.
2. Gently flex the panel along the tab line until the tab snaps cleanly.
3. If a tab leaves a small nub on the module, you can file or sand it smooth. It will not affect how the module works.

!!! warning "Take it slow"

    Bend the panel a little at a time rather than forcing it. The PCB is rigid but the components on the modules can be damaged by sharp impacts or twisting.

## Meet the modules

The kit includes:

- **ESP32-C6 main board.** The brain of every project you'll build with the kit. It handles Wi-Fi, runs your ESPHome config, and exposes the GPIO pins the modules plug into.
- **PIR motion sensor module.** Detects movement in a room.

<!-- TODO: confirm the full module list with Trevor and add the rest here (button module, etc.) -->

Each module connects to the ESP32-C6 board through the kit's pin headers. You don't need to solder anything to get started.

## Next: bring it online

Once you've identified your modules and snapped them off the panel, the next step is to connect the ESP32-C6 to your computer and walk through your first ESPHome configuration.

<a href="../setup/getting-started/" class="md-button md-button--primary">
  <img src="/assets/esphome-logo.svg" alt="" style="height:1.2em;vertical-align:-0.2em;margin-right:0.4em;">
  Open ESPHome Getting Started
</a>
