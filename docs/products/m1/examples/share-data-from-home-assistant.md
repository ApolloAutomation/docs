---
title: M-1 LED Matrix Setting up scrolling text with the states of Home Assistant entities!
description: Step by step guide for custom scrolling text using the states of Home Assistant entities!
---
# Share Data from Home Assistant on your M-1 LED Matrix

!!! tip "This tutorial expects you to already have 4 segments created!"

    Please follow <a href="https://wiki.apolloautomation.com/products/m1/setup/m1-segments/" target="_blank" rel="noreferrer nofollow noopener">this wiki article</a> to setup your M-1 LED Matrix with segments. If you are using multiple panels, <a href="https://wiki.apolloautomation.com/products/m1/setup/m1-multiple-panels/#segment-setup" target="_blank" rel="noreferrer nofollow noopener">follow this article</a> instead then come back!

The <a href="https://www.home-assistant.io/integrations/wled/" target="_blank" rel="noreferrer nofollow noopener">WLED integration for Home Assistant</a> does not support sending data from our devices directly to the M-1 LED Matrix, however, we are still able to do so using the <a href="https://mm.kno.wled.ge/interfaces/json-api/" target="_blank" rel="noreferrer nofollow noopener">WLED JSON API</a>. This is an advanced tutorial but if you follow each step closely you should be able to follow along!

1\. Install "Studio Code Server" <a href="https://github.com/hassio-addons/addon-vscode" target="_blank" rel="noreferrer nofollow noopener">from the addon store</a> in Home Assistant OS. Click Open Webui and navigate to your configuration.yaml file.

![](../../../assets/m1-navigate-to-configuration-yaml.gif)

!!! danger "This file is used by Home Assistant and must be careful edited"

    Home Assistant requires this file to work properly so only make changes exactly as shown below. Do NOT add any extra spaces or change anything other than what is shown in the steps below!

## 🧩 WLED Matrix YAML Generator

<iframe src="/snippets/matrix-yaml-generator.htm" width="100%" height="700" style="border: 1px solid #ccc; border-radius: 6px;"></iframe>


&nbsp;

2\. Copy the code below and paste it at the very bottom of your configuration.yaml file.

```yaml
rest_command:
  matrix_all_segments:
    url: http://10.10.10.176/json/state
    content_type: 'application/json'
    verify_ssl: false
    method: 'post'
    timeout: 20
    payload: >
      {
        "seg":[
          {
            "id":0,
            "fx":122,
            "n": "{{state_attr('weather.nowcast','temperature')}}F {{states('weather.nowcast')|title}} FL: {{ states('sensor.feels_like') | round(0) | int }}F"
          },
          {
            "id":1,
            "fx":122,
            "n": "{{ states('lock.front_door_lock') == 'locked' and 'Front Door Locked' or 'Front Door Unlocked' }}"
          },
          {
            "id":2,
            "fx":122,
            "n": "CO2 {{states('sensor.brandon_air_1_co2') | int}}ppm VOC {{states('sensor.brandon_air_1_sen55_voc') | int}}ppm"
          },
          {
            "id":3,
            "fx":122,
            "n": "Ping {{ states('sensor.1_1_1_1_round_trip_time_average') | float | round(0) | int }}ms {{ states('alarm_control_panel.alarmo') }}"
          }
        ]
      }
```