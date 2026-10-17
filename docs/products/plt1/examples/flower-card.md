---
title: PLT-1 Flower Card
description: Show your plant sensor's readings as bars on a Flower Card in Home Assistant, using the Plant integration, optional OpenPlantBook data, and the Flower Card from HACS.
---
# Flower Card

A Flower Card shows your plant's readings on your Home Assistant dashboard, with a bar for each one, such as moisture, temperature, light, and humidity.

![Home Assistant Flower Card for a ZZ Plant with moisture, temperature, light, and humidity bars](/assets/screenshot-2024-09-26-at-10-17-09-am.png)

To set one up, you install up to three things through HACS, then add the card to a dashboard. Work through the sections below in order:

1. Install the Plant integration.
2. Install the OpenPlantBook integration (optional).
3. Install the Flower Card.
4. Add the card to your dashboard.

## Install the Plant integration

The <a href="https://github.com/Olen/homeassistant-plant" target="_blank" rel="noopener">Home Assistant Plant integration</a> lets you set up your plants in the Home Assistant UI. You can manage all of their configuration there or with automations and scripts.

If you're a registered <a href="https://open.plantbook.io/docs.html" rel="nofollow">OpenPlantBook</a> user, the Plant integration can automatically fetch data from it. Registration is free.

Install the Plant integration through HACS with the button below.

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=Olen&repository=homeassistant-plant&category=integration)

## Install the OpenPlantBook integration (optional)

The <a href="https://github.com/Olen/home-assistant-openplantbook" target="_blank" rel="noopener">OpenPlantBook integration</a> fetches plant information from OpenPlantBook and uploads your plant sensors' data to it. It creates a few service calls in Home Assistant for working with the <a href="https://open.plantbook.io/" rel="nofollow">OpenPlantBook API</a>:

* Search plant
* Get plant details
* Upload plants sensors data

The [Plant integration](https://github.com/Olen/homeassistant-plant) uses this data to add threshold values, such as moisture, temperature, and conductivity, based on your plant's species.

Install OpenPlantBook through HACS with the button below.

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=Olen&repository=home-assistant-openplantbook&category=integration)

## Install the Flower Card

The Flower Card is the dashboard card that shows your plant. You can read more about it on the <a href="https://github.com/Olen/lovelace-flower-card?tab=readme-ov-file" target="_blank" rel="noopener">Flower Card GitHub</a> page.

Install the card through HACS with the button below.

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=Olen&repository=lovelace-flower-card&category=plugin)

## Add the card to your dashboard

Edit your dashboard, add a **Manual** card, and replace its contents with the Flower Card code below. Then swap in your own entities: replace `plant.my_plant` with the plant you set up in the Plant integration, and `sensor.demo_battery` with your own battery sensor.

```yaml
type: custom:flower-card
entity: plant.my_plant
show_bars:
- illuminance
- humidity
- moisture
- temperature
battery_sensor: sensor.demo_battery
```

Save the card, and your plant's readings appear as bars, like the example at the top of this page.
