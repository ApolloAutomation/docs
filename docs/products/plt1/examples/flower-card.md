![](../../../assets/screenshot-2024-09-26-at-10-17-09-am.png)

<a href="https://github.com/Olen/homeassistant-plant" target="_blank" rel="noopener">Home Assistant Plant Integration</a>

<a href="https://github.com/Olen/home-assistant-openplantbook" target="_blank" rel="noopener">Open Plant Book Integration</a>

<a href="https://github.com/Olen/lovelace-flower-card?tab=readme-ov-file" target="_blank" rel="noopener">Flower Card GitHub</a>

### **<u>Flower Card Code</u>**

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