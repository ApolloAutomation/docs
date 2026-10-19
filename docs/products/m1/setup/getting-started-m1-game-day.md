---
title: Getting started (Game Day Scoreboard)
description: Turn your M-1 into a live sports scoreboard that follows your team from ESPN, with its own settings page and Home Assistant support.
---
# Getting started (Game Day Scoreboard)

!!! tip "Running WLED instead?"

    M-1 units ship with WLED. If you want to keep it, the [Getting Started page](/products/m1/setup/getting-started-m1.md) covers it. You can come back to Game Day Scoreboard any time, and go back to WLED the same way.

Game Day Scoreboard turns your Apollo M-1 LED Matrix into a scoreboard for your team. Before a game it shows the matchup, both records, the start time, the betting line, and the TV network. Once the game starts it switches to the live score and game clock, fills the panel with a splash in your team's color when they score (in basketball, when they win), and stays on the final for a while before it looks up the next game. It covers the NFL, college football, MLB, the NBA, the WNBA, men's college basketball, the NHL, MLS, and the Premier League.

The panel reads the scores from ESPN by itself, so there's no hub, account, or other computer to run. It serves its own settings page, and it shows up in Home Assistant as an ESPHome device if you want it there. Apollo Automation maintains the open-source firmware at [ApolloAutomation/gameday-scoreboard-main](https://github.com/ApolloAutomation/gameday-scoreboard-main).

!!! note "Before you start"

    - An M-1 with a **Rev6** controller. The revision is printed on the back of the board, and every M-1 sold today is Rev6.
    - A desktop or laptop computer with Chrome or Edge, and a USB-C cable that carries data.
    - A 2.4 GHz Wi-Fi network and its password. The panel can't join a 5 GHz network.

!!! warning "Rev6 controllers only"

    Game Day Scoreboard uses the MoonHub75 pin layout, which the Rev6 controller shares. An older Rev4 controller wires the panel to different pins, so the prebuilt firmware won't drive it.

## Attach the M-1 controller

Your M-1 LED Matrix and M-1 controller ship separately to keep them safe in transit. Gently press the controller onto the back of the panel, as shown below. Skip this if your M-1 is already together.

![Hands pressing the M-1 controller onto the back of the M-1 LED Matrix panel](/assets/m1-matrix-attach-controller.webp)

## Flash Game Day Scoreboard

The Game Day Scoreboard installer flashes the firmware from your browser, with nothing to install on your computer. Flashing replaces WLED, along with its presets and settings.

1. Open the [Game Day Scoreboard DIY installer](https://apolloautomation.github.io/gameday-scoreboard-main/install/diy/) in Chrome or Edge.
2. Click the picture that matches your setup:
    - **One 64x64 panel** for a single M-1.
    - **One 128x64 panel** (or two 64x64 side by side) for two M-1 panels in a row. See [Multiple Panels](/products/m1/setup/m1-multiple-panels.md) for chaining them.
3. Plug the M-1 controller into your computer with the USB-C cable.
4. Click **Install for MoonHub75** and pick the M-1's port when the browser asks. This is the right build for the M-1: the two boards share a pin layout.
5. Wait for the install to finish. Leave the cable plugged in until it does.

The panel lights up with **GAME DAY** across the top and **Starting** under it, then shows **SETUP** while it waits for Wi-Fi. You can change the panel layout later on its settings page, so a wrong pick here costs you nothing.

!!! tip "The browser doesn't see your M-1?"

    Put the controller into boot mode and try again: hold the boot button while you plug in the USB-C cable. See [M-1 Boot Mode](/products/m1/troubleshooting/m1-boot-mode.md).

## Connect to Wi-Fi

Your M-1 needs your home Wi-Fi to read the scores. There are two ways to give it your network:

- **Right after the install,** the installer offers to put the panel on your Wi-Fi. Enter your network name and password there, and you're done with this section.
- **From the panel's hotspot.** While it shows **SETUP**, the panel starts its own Wi-Fi network named **Game Day** plus six letters and numbers, like **Game Day 2f6a70**, and shows the name on screen.

To use the hotspot:

1. On your phone or laptop, join the **Game Day** network the panel shows. A setup page opens.
2. Pick your Wi-Fi network and enter the password.
3. Tap **Save**.

The panel joins your Wi-Fi and shows its address, like **gameday-2f6a70.local**. Use your main network, not a guest network: a guest network can let the panel join but keep your phone from reaching it afterward.

!!! tip "About the QR code on the screen"

    The QR code the panel shows during setup is for the separate Game Day phone app, which Apollo Automation doesn't maintain, and which may not find panels running this firmware. You don't need it: the hotspot and the panel's settings page do everything it does.

## Pick your team

The panel serves its own settings page, the device page. This is where you pick your team and set up everything else, from any phone or computer on your Wi-Fi.

1. Open the address the panel shows, like `http://gameday-2f6a70.local`, in a browser.
2. Tap **Change team**.
3. Pick a league tab and tap a logo, or search for any team.

The page says **Now following the** and the team's name, and the panel switches to them. Until you pick a team, the ticker along the bottom asks you to and shows the panel's IP address, for phones that can't open `.local` names. To see the address again any time, hold the boot button on the controller for about 1.5 seconds.

From the same page you can follow up to 16 **Favorite teams** that take turns, or switch to **Live games**, which follows a game in progress in the leagues you pick. The timezone follows the browser you open the page in, so start times read right without setting anything.

## Add it to Home Assistant

Nothing about the scoreboard needs Home Assistant, but it's an ordinary ESPHome device, so it fits right in. Once it's added, you can automate the panel's power and brightness and react to the game itself.

1. With Home Assistant on the same network, go to **Settings → Devices & services**. Home Assistant discovers the panel as a new ESPHome device and lists it under **Discovered**.

    [![Open your Home Assistant instance and show your integrations.](https://my.home-assistant.io/badges/integrations.svg)](https://my.home-assistant.io/redirect/integrations/)

2. Click **Add** (or **Configure**) and confirm. The firmware has no API encryption key, so there's no key to enter.
3. Pick an area for the panel if you like, and finish.

Not discovered? Add it by its address instead:

1. Go to **Settings → Devices & services** and click **Add integration**. The button below covers this step and the next.

    [![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=esphome)

2. Pick **ESPHome**.
3. Enter the panel's `.local` name or IP address.

Your scoreboard now shows up under the ESPHome integration with the entities worth automating: **Team**, **Mode**, **Power**, **Brightness**, **Scroll Speed**, **Game Status**, **Last Play**, **Firmware**, **Install Updates Automatically**, and the WizMote pairing controls. Favorites, the timezone, and the ticker options live on the device page only. The **Microphone Enabled** switch belongs to the [microphone addon](/products/m1/addons/adding-microphone-to-m-1.md); the scoreboard doesn't use the microphone.

**Game Status** changes when a game starts, when someone scores, and when it ends, which makes it a great trigger for your own automations.

!!! success "Next step: celebrate scores with your lights"

    Make your room join in when your team scores: the step-by-step guide sets up an automation that flashes your lights on every score.

    [Flash your lights when your team scores](/products/m1/examples/game-day-score-lights.md){ .md-button .md-button--primary }

### Adopt it in ESPHome Device Builder

Adopting the panel in the **ESPHome Device Builder** app lets you build its firmware yourself and add your own YAML. You don't need this to use the scoreboard in Home Assistant.

1. Go to **Settings → Apps**, click **Install app**, and install the **ESPHome Device Builder** app if you don't have it yet. Click **Start**, then **Open Web UI**.

    [![Open your Home Assistant instance and show the dashboard of an app.](https://my.home-assistant.io/badges/supervisor_app.svg)](https://my.home-assistant.io/redirect/supervisor_app/?app=5c53de3b_esphome&repository_url=https%3A%2F%2Fgithub.com%2Fesphome%2Fhome-assistant-addon)

2. Find your panel under the discovered devices, click **Take Control**, and confirm. Device Builder discovers the panel when it's on the same network.
3. Install the firmware when Device Builder offers to, using the wireless install.

The adopted firmware gets its own API encryption key, which Home Assistant picks up from the app. Leave **Install updates automatically** off on an adopted panel: a release installed from the device page puts the prebuilt firmware back, without your changes.

## Updates

The scoreboard checks for a new release every six hours. When one is out, the **Firmware** box on the device page shows an **Install** button, and the update goes over Wi-Fi with your team and settings kept. Turn on **Install updates automatically** and the panel installs new releases by itself between 3 and 5 AM, never during a game it's following.

## Pair a WizMote remote

Game Day Scoreboard works with a WiZ WizMote, the small battery remote sold for WiZ smart bulbs. Pair it once and you can run the panel from across the room.

1. Open the **Remote** card on the device page.
2. Turn on **Discovery**.
3. Press any button on the remote.

The card says **Paired:** and the remote's address. **ON** and **OFF** turn the panel on and off, the brightness buttons make it brighter or dimmer, **NIGHT** drops it to a night level, and buttons **1** to **4** jump to your first four favorite teams.

## Go back to WLED

You can return your M-1 to WLED at any time with the Apollo M-1 installer. See [Factory re-flash M-1](/products/m1/troubleshooting/m1-reflash.md).

## Learn more

The [Game Day Scoreboard docs](https://github.com/ApolloAutomation/gameday-scoreboard-main/tree/main/docs/wiki/src/content/docs) cover every setting, each sport's board, the boot button's holds and resets, and fixes for the things that go wrong. Found a bug? [Open an issue on GitHub](https://github.com/ApolloAutomation/gameday-scoreboard-main/issues).
