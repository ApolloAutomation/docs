---
title: ESPHome Starter Kit - Start Here
description: Landing page of the ESPHome Starter Kit QR Code.
---
# Welcome to the ESPHome Starter Kit!

Welcome to the start of your ESPHome journey with the all-new **ESPHome Starter Kit**!

![](../../assets/esphome-starter-kit-exploded-with-box-1.png)

By the end of this wiki you'll know how to:

* Remove the modules off the panel safely
* Identify each part of your kit

## What's in the kit

Your kit arrives as a single snap-apart panel that includes the ESP32-C6 main board along with a selection of interchangeable modules. The kit also includes three ribbon cables for connecting modules to the main board, one more than any project uses at once so you always have a spare, plus a stand for the LED & Buzzer module.

![](../../assets/esphome-starter-kit-whats-in-the-box.png)

## Snapping the panel apart

Each module is connected to the panel by small breakaway tabs. Follow the steps below to separate them.

!!! success "Take it slow"

    Bend the panel gradually, not all at once. The PCB is sturdy, but the components on the modules prefer a gentle snap.

1. Hold the panel flat on a table with one hand on the module you want to remove.
2. Gently flex the panel along the tab line until the tab snaps cleanly.

![](../../assets/esphome-starter-kit-disassembly-final.gif)

## Meet the modules

**ESP32-C6 main board**

* The brain of every project you'll build with the kit. It handles Wi-Fi and Bluetooth, runs your ESPHome config, and exposes the GPIO pins the modules plug into.

![](../../assets/esphome-starter-kit-main-board-only.jpg)

---

**LED & Buzzer module**

* The starter kit's notification module, a strip of ten addressable RGB LEDs and a small piezo buzzer behind the ESPHome logo silkscreen. *Use the included stand to show it off!*

![](../../assets/esphome-starter-kit-rgb-buzzer-module-only.jpg)

---

**Motion module**

* Detects movement in a room and a great way to get started automating your home. It comes in two parts, and the PIR sensor easily plugs into the PIR module board.

![](../../assets/esphome-starter-kit-pir-module-only.jpg)

---

**Button module**

* Premium feel button perfect to trigger automations for lights and more.

![](../../assets/esphome-starter-kit-button-module-only.jpg)

---

**Temperature and Humidity module**

* Extremely accurate temp and humidity sensor trustworthy enough to track a room comfort level with ease!

![](../../assets/esphome-starter-kit-temp-hum-module-only-1.jpg)

---

**FPC cables**

* Each module connects to the main board through the FPC connector using one of the three provided cables. *Tear the brown paper bag open from one of the ends. Please DO NOT use scissors as you could accidentally cut the cables!*

![](../../assets/esphome-starter-kit-fpc-cables-only.jpg)

## Next: bring it online

Once you've identified your modules and snapped them off the panel, the next step is to connect the main board to your computer and walk through your first ESPHome configuration.

<a href="../setup/first-steps/" class="md-button md-button--primary">   <img src="/assets/esphome-logo.svg" />   Next - First Steps </a>