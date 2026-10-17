---
title: Flower Card
description: "Show PLT-1 readings on a Home Assistant dashboard with the Flower Card, the Plant integration, and OpenPlantBook."
---
# Flower Card

The Flower Card shows a plant's moisture, temperature, light, and humidity as bars on a Home Assistant dashboard.

![Flower Card for a ZZ Plant showing moisture, temperature, light, and humidity bars](/assets/screenshot-2024-09-26-at-10-17-09-am.png)

!!! note "Before you start"

    This page is for Home Assistant. The Flower Card is a Home Assistant dashboard card, and it works with the two Home Assistant integrations below: the Plant integration and the Open Plant Book integration.

## Plant integration

<a href="https://github.com/Olen/homeassistant-plant" target="_blank" rel="noopener"><strong>Home Assistant Plant Integration</strong></a>

You set up your plants in the Home Assistant UI, and manage all of their configuration there or with automations and scripts. If you're a registered <a href="https://open.plantbook.io/docs.html" rel="nofollow">OpenPlantBook</a> user, the integration can fetch plant data from it automatically. Registration is free.

## Open Plant Book integration

<a href="https://github.com/Olen/home-assistant-openplantbook" target="_blank" rel="noopener"><strong>Open Plant Book Integration</strong></a>

This integration fetches plant information from OpenPlantBook and uploads your plant sensors' data to it. It adds these service calls to Home Assistant for the <a href="https://open.plantbook.io/" rel="nofollow">OpenPlantbook API</a>:

* Search plant
* Get plant details
* Upload plants sensors data

Its sister integration, the [Plant integration](https://github.com/Olen/homeassistant-plant), is built on it. The Plant integration uses this API to add threshold values, such as moisture, temperature, and conductivity, based on the plant species.

## Add the Flower Card

<a href="https://github.com/Olen/lovelace-flower-card?tab=readme-ov-file" target="_blank" rel="noopener"><strong>Flower Card GitHub</strong></a>

Add the card to your dashboard with this YAML. Replace `plant.my_plant` and `sensor.demo_battery` with your own entity IDs.

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
