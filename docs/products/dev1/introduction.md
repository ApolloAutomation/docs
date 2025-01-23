The Apollo DEV-1 is a very small dev board that we use to prototype before creating other new products. It has a built in RGB light (using GPIO3) and can push up to 600mA out of the 3.3v pin however 100-200mA of that will be used by the microcontroller itself. You are able to back-feed power via the 5v and G (ground) pins or use the USB-C port to power it, but NOT both at the same time.

The DEV-1 is a great starter device for tinkerers and can be purchased on its own or with a breadboard and dupont wires (jumper wires) if you need those too.

The DEV-1 does NOT come pre-flashed with ESPHome or WLED and requires you to flash it yourself, however there is a getting started video we've made here:

<div class="cms-embed">&lt;iframe width="560" height="315" src="https://www.youtube.com/embed/oiKnTH1gg0Q?si=nNFDbHxZBuWIXHyH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen=""&gt;&lt;/iframe&gt;</div>

Please <a href="https://esphome.io/components/api.html#configuration-variables" target="_blank" rel="noopener">go to this website</a> and copy the randomly generated API key inside the code block as shown below then paste it in the code below where you see "use-a-randomly-generated-key-here".

![](assets/apollo-dev-1-image-2.png)

**Example ESPHome yaml**:

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
  platformio_options:
    board_build.flash_mode: dio

  project:
    name: "ApolloAutomation.MSR-2"
    version: "${version}"

# Define Board
esp32:
  board: esp32-c3-devkitm-1
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
    password: "a53d93acd493275512730c776f88722a"

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

light:
  - platform: esp32_rmt_led_strip
    id: rgb_onboard_light
    name: "RGB Onboard Light"
    pin: GPIO3
    rmt_channel: 0
    default_transition_length: 0s
    chipset: WS2812
    num_leds: 1
    rgb_order: grb
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