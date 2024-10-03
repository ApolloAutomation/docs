![](../../../assets/screenshot-2024-09-26-at-10-17-09-am.png)

<a href="https://github.com/Olen/homeassistant-plant" target="_blank" rel="noopener"><strong>Home Assistant Plant Integration</strong></a><br><br>This integration can automatically fetch data from <a href="https://open.plantbook.io/docs.html" rel="nofollow">OpenPlantBook</a> if you are a registered user. Registration is free.<br><br>Plants are set up in the UI and all configuration of your plants can be managed there or by automations and scripts.

<a href="https://github.com/Olen/home-assistant-openplantbook" target="_blank" rel="noopener"><strong>Open Plant Book Integration</strong></a><br><br>This integration allows fetching plants information from and uploading plant sensors' data to OpenPlantBook. It creates a few service calls in Home Assistant to interact with <a href="https://open.plantbook.io/" rel="nofollow">OpenPlantbook API</a> which are:

* Search plant
* Get plant details
* Upload plants sensors data

This is used as a base for the sister-integration [https://github.com/Olen/homeassistant-plant](https://github.com/Olen/homeassistant-plant) which utilizes this API to add threshold values for such as moisture, temperature, conductivity etc. based on the plant species.

<a href="https://github.com/Olen/lovelace-flower-card?tab=readme-ov-file" target="_blank" rel="noopener"><strong>Flower Card GitHub</strong></a>

Flower Card Code

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