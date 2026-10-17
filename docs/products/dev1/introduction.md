---
title: Apollo DEV-1 introduction
description: Pinout, power limits, a flashing video, and an example ESPHome YAML for the Apollo DEV-1 dev board.
---
# Apollo DEV-1 introduction

The Apollo DEV-1 is a very small dev board that we use to prototype before creating other new products. It's a great starter device for tinkerers. You can buy it on its own, or with a breadboard and dupont wires (jumper wires) if you need those too.

## Pinout and power

![Apollo DEV-1 pinout showing the GPIO number and functions of every header pin](/assets/apollo-dev-1-pinout.webp)

- **Built-in RGB light:** on GPIO3.
- **3.3V pin:** supplies up to 600mA, but the microcontroller itself uses 100-200mA of that.

!!! warning "Use one power source at a time"

    You can power the DEV-1 through the USB-C port or back-feed power through the 5V and G (ground) pins, but **not** both at the same time.

### GPIO pins

These are the DEV-1's I2C, UART, ADC, and onboard RGB LED pins, written as ESPHome YAML:

```yaml
#These are the i2c pins
i2c:
  sda: GPIO1
  scl: GPIO0

#These are the UART pins
uart:
  tx_pin: GPIO21
  rx_pin: GPIO20
  baud_rate: 115200 #match the device you connect

#ADC pins: GPIO0, GPIO1, GPIO2, GPIO4

#Onboard RGB LED: GPIO3
```

## Flash your DEV-1

The DEV-1 doesn't come pre-flashed with ESPHome or WLED, so you flash it yourself. This getting started video we made walks you through it:

<div class="cms-embed">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/oiKnTH1gg0Q?si=nNFDbHxZBuWIXHyH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen="">
  </iframe>
</div>

## Example ESPHome YAML

Use the example configuration below as a starting point for your DEV-1. Before you use it, give it your own API encryption key:

1\. Open the <a href="https://esphome.io/components/api.html#configuration-variables" target="_blank" rel="noopener">ESPHome API documentation</a> and copy the randomly generated API key from the code block, as shown in the red box below.

![ESPHome API docs with a randomly generated encryption key highlighted in a red box](/assets/apollo-dev-1-image-2.png)

2\. In the YAML below, find the `key:` line under `api:` and replace `use-a-randomly-generated-key-here` with the key you copied.

Your configuration now uses its own encryption key. Here's the full example for the DEV-1:

```yaml
#Define Project
substitutions:
  name: apollo-dev-1
  version:  "1"
  device_description: ${name} made by Apollo Automation - version ${version}.

esphome:
  name: "${name}"
  friendly_name: Apollo DEV-1
  comment: Apollo DEV-1

  project:
    name: "ApolloAutomation.DEV-1"
    version: "${version}"

# Define Board
esp32:
  variant: esp32c3
  framework:
    type: esp-idf

# Enable logging
logger:

# Enable Home Assistant API
api:
  encryption:
    key: "use-a-randomly-generated-key-here"

ota:
  - platform: esphome
    password: !secret ota_password

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password

  # Enable fallback hotspot (captive portal) in case wifi connection fails
  ap:
    ssid: "Apollo-Dev-1 Fallback Hotspot"
    password: !secret wifi_password

captive_portal:

web_server:
  port: 80
  version: 3

#onboard LED using pin GPIO3 as shown below
light:
  - platform: esp32_rmt_led_strip
    id: rgb_onboard_light
    name: "RGB Onboard Light"
    pin: GPIO3
    default_transition_length: 0s
    chipset: WS2812
    num_leds: 1
    channel_colors: GRB
    effects:
      - pulse:
          name: "Slow Pulse"
          transition_length: 1000ms
          update_interval: 1000ms
          min_brightness: 50%
          max_brightness: 100%
      - pulse:
          name: "Fast Pulse"
          transition_length: 100ms
          update_interval: 100ms
          min_brightness: 50%
          max_brightness: 100%

button:
  - platform: restart
    icon: mdi:power-cycle
    name: "ESP Reboot"

sensor:
  - platform: internal_temperature
    name: "ESP Temperature"
    id: sys_esp_temperature

  - platform: uptime
    name: Uptime
    id: sys_uptime
    update_interval: 60s

  - platform: wifi_signal
    name: RSSI
    id: wifi_signal_db
    update_interval: 60s
    entity_category: "diagnostic"

text_sensor:
  - platform: wifi_info
    ip_address:
      name: "${name} IP"
      icon: "mdi:ip-outline"
```
