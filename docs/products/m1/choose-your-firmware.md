---
title: Choose Your M-1 Firmware
description: Find out which firmware your M-1 runs and what each one gives you.
---
# Choose Your M-1 Firmware

Most M-1 pages on this wiki have a **WLED** and a **WLED-MM** tab. Pick your firmware once and the rest of the wiki follows it, so this page is only here to help you work out which one you have.

#### Which One Do I Have?

Open your M-1 in a browser and tap **Info**. The version is at the top.

| Version shown | Your firmware |
| --- | --- |
| 16.0.1 or newer | WLED |
| 14.5.1 | WLED-MM |

## WLED

The stock, upstream WLED release, and what new M-1 units ship with. HUB75 matrix support is now built into WLED itself, so the M-1 no longer needs a fork to drive the panel.

It brings [Pixel Forge](/products/m1/examples/pixel-forge.md), an image and scrolling-text tool that runs on the device, and it can arrange panels in a [2x2 grid](/products/m1/setup/m1-multiple-panels.md) instead of only a single row.

WLED requires a **Rev6** M-1 controller. The revision is printed on the back of the board.

## WLED-MM

[WLED MoonModules](https://github.com/MoonModules/WLED-MM), the fork that added HUB75 support before upstream WLED had it. Units shipped before the switch came with this, and every guide on this wiki still covers it under the WLED-MM tab.

On a Rev6 controller you can move to stock WLED over the air and keep your settings. See [Upgrade to WLED](/products/m1/setup/upgrade-to-wled.md).

## ESPHome

[hub75-studio](https://github.com/pavlov-net/hub75-studio) replaces WLED entirely with an ESPHome firmware built for the M-1. You get native Home Assistant entities and YAML you control, at the cost of the WLED effect library and app. Pick this one deliberately.

[Set Up ESPHome](/products/m1/setup/getting-started-m1-esphome.md){: .md-button }
