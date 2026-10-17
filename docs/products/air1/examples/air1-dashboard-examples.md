---
title: AIR-1 Home Assistant Dashboard Examples
description: AIR-1 Home Assistant Dashboard Examples
---
# AIR-1 Home Assistant Dashboard Examples

Really neat dashboard for your AIR-1 by user "keex"!

![Home Assistant dashboard by keex with AIR-1 particulate matter and air quality charts for two rooms](/assets/air-1-keex-dashboard-image-1-1.png)

[https://community.home-assistant.io/t/apollo-air-1-dashboard/785311](https://community.home-assistant.io/t/apollo-air-1-dashboard/785311)

## **CO2 Charts**

### Home Assistant Sensor

![Home Assistant sensor card showing a 24-hour Bedroom CO2 line graph at 1,000 ppm](/assets/co-2-graph.png)

```yaml
graph: line
type: sensor
entity: sensor.apollo_air_1_a79e38_co2
detail: 2
name: Bedroom CO2
hours_to_show: 24
```

## Custom: Apexcharts Card

This card installs from HACS, so add it there first:

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=RomRider&repository=apexcharts-card&category=plugin)

![ApexCharts card showing 10-minute average CO2 levels for five rooms in Home Assistant](/assets/air-1-suggestions-co2-smarthomesellout.png)

```yaml
type: custom:apexcharts-card
header:
  show: true
  title: CO2 (10m average)
  show_states: true
  colorize_states: true
graph_span: 24h
experimental:
  color_threshold: true
span:
  start: day
now:
  show: true
  label: now
  color: red
series:
  - entity: sensor.apollo_air_1_co2
    name: Brandon Room
    color: Pink
    stroke_width: 3
    fill_raw: last
    extend_to: now
    show:
      in_header: false
      legend_value: false
    group_by:
      func: avg
      duration: 10min
    color_threshold:
      - color: "#DE2349"
        value: 850
      - color: "#FFA500"
        value: 650
      - color: "#008055"
        value: 500
      - color: "#008000"
        value: 0
  - entity: sensor.dining_room_mmwave_sensor_co2
    name: Dining Room
    color: Green
    opacity: 1
    stroke_width: 3
    fill_raw: last
    extend_to: now
    show:
      in_header: false
      legend_value: false
    group_by:
      func: avg
      duration: 10min
    color_threshold:
      - color: "#DE2349"
        value: 850
      - color: "#FFA500"
        value: 650
      - color: "#008055"
        value: 500
      - color: "#008000"
        value: 0
  - entity: sensor.living_room_air_1_co2
    name: Living Room
    color: Orange
    opacity: 1
    stroke_width: 3
    fill_raw: last
    extend_to: now
    show:
      in_header: false
      legend_value: false
    group_by:
      func: avg
      duration: 10min
    color_threshold:
      - color: "#DE2349"
        value: 850
      - color: "#FFA500"
        value: 650
      - color: "#008055"
        value: 500
      - color: "#008000"
        value: 0
  - entity: sensor.kitchen_air_1_co2
    name: Kitchen
    color: Blue
    opacity: 1
    stroke_width: 3
    fill_raw: last
    extend_to: now
    show:
      in_header: false
      legend_value: false
    group_by:
      func: avg
      duration: 10min
    color_threshold:
      - color: "#DE2349"
        value: 850
      - color: "#FFA500"
        value: 650
      - color: "#008055"
        value: 500
      - color: "#008000"
        value: 0
  - entity: sensor.master_bedroom_air_1_co2
    name: Master Bedroom
    color: Purple
    opacity: 1
    stroke_width: 3
    fill_raw: last
    extend_to: now
    show:
      in_header: false
      legend_value: false
    group_by:
      func: avg
      duration: 10min
    color_threshold:
      - color: "#DE2349"
        value: 850
      - color: "#FFA500"
        value: 650
      - color: "#008055"
        value: 500
      - color: "#008000"
        value: 0
```

### Custom: Plotly Graph Card

This card installs from HACS, so add it there first:

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=dbuezas&repository=lovelace-plotly-graph-card&category=plugin)

![Plotly Graph card showing 24 hours of Bedroom CO2 readings in ppm](/assets/plotly-co2-graph.png)

```plaintext
type: custom:plotly-graph
entities:
  - entity: sensor.apollo_air_1_a79e38_co2
hours_to_show: 24
refresh_interval: 10
title: Bedroom CO2
```

### Home Assistant Gauge

![Home Assistant needle gauge card showing MSR-1 CO2 at 1,063 ppm with green, yellow, and red ranges](/assets/co2-guage.png)

```plaintext
type: gauge
entity: sensor.apollo_air_1_a79e38_co2
needle: true
unit: ppm
min: 0
max: 3000
severity:
  green: 0
  yellow: 1000
  red: 2000
```

## **VOC Charts**

### Home Assistant Sensor

![Home Assistant sensor card showing an AIR-1 SEN55 VOC line graph at 446](/assets/air-1-voc-ha-sensor.png)

```
graph: line
type: sensor
detail: 2
entity: sensor.apollo_air_1_6b1a58_sen55_voc
hours_to_show: 24
name: Basement VOC
```

### Custom: Plotly Graph Card

![Plotly Graph card showing 24 hours of Basement VOC readings from the AIR-1](/assets/air-1-voc-plotly.png)

```
type: custom:plotly-graph
entities:
  - entity: sensor.apollo_air_1_6b1a58_sen55_voc
hours_to_show: 24
refresh_interval: 10
title: Basement VOC
```

### Home Assistant Gauge

![Home Assistant needle gauge card showing a Basement VOC reading of 457](/assets/air-1-voc-ha-guage.png)

```
type: gauge
entity: sensor.apollo_air_1_6b1a58_sen55_voc
name: Basement VOC
severity:
  green: 0
  yellow: 150
  red: 350
needle: true
min: 0
max: 500
```