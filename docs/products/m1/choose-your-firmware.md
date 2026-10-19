---
title: Choose your M-1 firmware
description: Find out which firmware your M-1 runs and what each one gives you.
---
# Choose your M-1 firmware

Most M-1 pages on this wiki have a **WLED** and a **WLED-MM** tab. Pick your firmware once and the rest of the wiki follows it, so this page is only here to help you work out which one you have.

## Which one do I have?

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

## Game Day Scoreboard

[Game Day Scoreboard](https://github.com/ApolloAutomation/gameday-scoreboard-main) turns the M-1 into a live sports scoreboard for your team: the next game, the live score and clock, and a splash in your team's color when they score (in basketball, when they win), across the NFL, college football, MLB, the NBA, the WNBA, men's college basketball, the NHL, MLS, and the Premier League. It reads the scores from ESPN by itself, serves its own settings page, and shows up in Home Assistant as an ESPHome device. It needs a **Rev6** controller.

[Set Up Game Day Scoreboard](/products/m1/setup/getting-started-m1-game-day.md){: .md-button }
