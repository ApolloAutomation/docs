---
title: Explaining ESPHome
description: A short overview of what ESPHome is, how the Device Builder app fits in, and why the ESPHome Starter Kit is built on it.
---
# Explaining ESPHome

ESPHome is the open-source firmware project that powers your Apollo ESPHome Starter Kit. You describe what is connected to your board (a button, a sensor, an LED) and ESPHome runs on the device, exposes those parts to Home Assistant, and accepts updates over the network.

You do not need to write any code to use it. For the Starter Kit, the **ESPHome Device Builder** app handles it.

## ESPHome vs Device Builder

These two names get used interchangeably, but they are different pieces:

- **ESPHome** is the software that runs on your device after it has been flashed. It is what makes your board talk to Home Assistant, expose its sensors and controls, and accept wireless updates.
- **ESPHome Device Builder** is the app where you set everything up. Pick the components you want (button, LED, sensor, etc.), click **Install**, and the Builder compiles the firmware and flashes it to your device. Run it as a desktop app on Windows, Mac, or Linux, or install it as a Home Assistant app.

For the Starter Kit, you will spend almost all your time in the Device Builder.

## Controlling your device

Once your device is flashed, you can control it two ways:

#### From any web browser

ESPHome's built-in **Web Server** component makes your device serve its own local web page. Open <a href="http://esphome-starter-kit.local/" target="_blank" rel="noreferrer nofollow noopener">esphome-starter-kit.local</a> (or the device's IP address) in any browser on your network, on a phone or PC, and you can toggle the LED, view sensor readings, and control the device directly. No Home Assistant required. See the [Web Server in Core Components](core-components.md#web-server) for more.

#### From Home Assistant

Home Assistant discovers your device automatically through the **ESPHome integration**. Each of your device's sensors, switches, and lights then appears in Home Assistant as an entity you can use in dashboards and automations.

For more on how this works under the hood, see [the Home Assistant integration](how-esphome-talks-to-home-assistant.md).

A typical flow looks like this:

1. Click **Add component** in **ESPHome Device Builder** and pick what is connected to your device. No code or YAML required.
2. Click **Install** to flash the firmware to the device.
3. Home Assistant picks up the device through the **ESPHome integration** and shows its sensors, buttons, and lights as entities you can control or automate.

If you ever want to fine-tune something the GUI does not expose, the YAML view is always available. Most users never need it.

## Why ESPHome

ESPHome is part of the **ESPHome ecosystem**, an open-source project with a large community of contributors and direct first-class support in Home Assistant. Apollo builds on **open standards**: public protocols like ESPHome and OpenThread, so your kit is never locked to one vendor. Everything you set up runs under **local control**: your home runs on your own network, and your devices keep working even if your internet goes down or Apollo goes away.

You get wireless updates, a built-in web page for controlling your device, and direct Home Assistant integration without writing any code. The skills you build on the Starter Kit carry over to any ESPHome project you take on later.

The official ESPHome documentation covers every component, configuration option, and advanced topic in detail.

<a href="../device-builder-tour/" class="md-button md-button--primary"><img src="/assets/esphome-logo.svg" /> Next - Device Builder Tour</a> <a href="https://esphome.io/" target="_blank" rel="noreferrer nofollow noopener" class="md-button md-button--primary"><img src="/assets/esphome-logo.svg" /> Visit esphome.io</a>


--8<-- "_snippets/community-help.md"
