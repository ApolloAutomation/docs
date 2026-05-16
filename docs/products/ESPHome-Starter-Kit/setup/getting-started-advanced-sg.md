---
title: Getting started with the ESPHome Starter Kit (advanced)
description: Hand-write your first ESPHome YAML for the starter kit, flash it via Home Assistant, and add it to Home Assistant.
---

This advanced guide walks through every block of the starter kit's YAML by hand instead of using ESPHome Device Builder's component picker. By the end you'll have your ESPHome Starter Kit flashed with a working configuration and showing up in Home Assistant, with a working web server reachable at its IP address or `hostname.local` in a browser.

If you'd rather have ESPHome Device Builder write the YAML for you, see the [First steps](first-steps.md) guide instead.

## Connect the hardware

The ESP32-C6 is the main board in your kit. It is the small module with the USB-C port on one edge and a row of pin headers along the side. Every project you build with the kit starts here.

### Plug a module into the C6

For your first project, attach the LED & Buzzer module (ten RGB LEDs and a piezo buzzer) to the ESP32-C6 module using the FPC connector and ribbon cable. You can connect to the top or bottom FPC connector. This example uses the top.

### Connect the C6 to your computer

Plug the ESP32-C6 into your computer using a USB-C cable.

!!! tip "First-time flashing"

    The very first time you flash an ESP32-C6, you may need to put it into bootloader mode manually.

    1. Hold down the **BOOT** button on the C6.
    2. While still holding **BOOT**, press and release the **RESET** button.
    3. Release the **BOOT** button.

    The board will stay in bootloader mode until you flash it. After the first flash you usually won't need to do this again.

!!! success "Use a quality USB-C cable and power source"

    ESP32 boards are sensitive to power. If your device keeps restarting, will not be detected, or will not broadcast its hotspot, try a different USB-C cable or a different USB port. A 5V 1A supply is plenty.

## Set up ESPHome Device Builder

ESPHome Device Builder is a Home Assistant app that gives you a web UI for writing, compiling, and flashing ESPHome configurations. You'll use it to build the firmware for your kit.

### Install the app

1. In Home Assistant, open **Settings → Apps → App Store**.
2. Search for **ESPHome Device Builder** and install it.
3. Once installed, click **Start**, then **Open Web UI**.

If you don't have Home Assistant set up yet, follow the official Home Assistant installation guide first, then come back here.

### Fill in your Wi-Fi secrets

ESPHome keeps your Wi-Fi credentials in a separate `secrets.yaml` file so they aren't pasted into every device config.

1. In the ESPHome Device Builder dashboard, click **Secrets** in the top right.
2. Add your Wi-Fi name and password.

    ```yaml title="secrets.yaml"
    # Replace the values inside the quotes with your own Wi-Fi name and password.
    wifi_ssid: "your-wifi-ssid-here"
    wifi_password: "your-wifi-password-here"
    ```

3. Click **Save**.

### Add a new device

1. Click **\+ New Device** in the bottom right of the ESPHome Device Builder dashboard.
2. Give your device a name (for example `apollo-esk-1`).
3. When asked for the device type, choose **ESP32-C6**.
4. ESPHome Device Builder will scaffold a starter YAML for you. Don't flash it yet, you're going to replace it in the next section.

## Write your first ESPHome configuration

ESPHome configs are YAML files. Each top-level block configures a different part of the device. Below is a complete starting config for the kit, broken down section by section. Paste each block into your device's YAML in ESPHome Device Builder as you go, or jump to the [complete configuration](#complete-configuration) at the bottom and paste the whole thing at once.

!!! note "YAML basics"

    YAML uses indentation (spaces, not tabs) to define structure. Two spaces per level is the convention used throughout these examples.

### Substitutions

Substitutions are reusable variables. Define them once at the top of the file and reference them anywhere with `${name}`.

```yaml
substitutions:
  name: apollo-esk-1
  version: "25.5.5.1"
  device_description: ${name} made by Apollo Automation - version ${version}.
```

| Variable | Purpose |
| --- | --- |
| `name` | Device identifier used in ESPHome and Home Assistant. |
| `version` | Track your firmware version. The convention used here is Year.Month.Day.Build. |
| `device_description` | Human-readable description. Notice that it references other substitutions with `${}`. |

### Core ESPHome configuration

This block tells ESPHome how the device should appear in the dashboard and in Home Assistant.

```yaml
esphome:
  name: "${name}"
  friendly_name: Apollo ESPHome Starter Kit
  comment: ${device_description}
  name_add_mac_suffix: true
  platformio_options:
    board_build.flash_mode: dio
  project:
    name: "ApolloAutomation.ESK-1"
    version: "${version}"
  min_version: 2024.6.0
```

| Option | Description |
| --- | --- |
| `name` | Internal device name, pulled from substitutions. |
| `friendly_name` | The name shown in Home Assistant's UI. |
| `name_add_mac_suffix` | Appends part of the MAC address to the name, useful when you flash more than one device. |
| `platformio_options` | Low-level build settings. `dio` flash mode is what the ESP32-C6 expects. |
| `project` | Identifies this as an Apollo Automation project. |
| `min_version` | Refuses to compile on ESPHome versions older than this. |

### ESP32 board

Tell ESPHome which chip you're targeting.

```yaml
esp32:
  board: esp32-c6-devkitm-1
  variant: esp32c6
  flash_size: 8MB
  framework:
    type: esp-idf
```

!!! warning "ESP32-C6 needs the ESP-IDF framework"

    The older Arduino framework does not fully support the C6. Stick with `esp-idf` here.

### Home Assistant API

One line enables the native Home Assistant API connection. ESPHome handles the encryption and discovery for you.

```yaml
api:
```

### Wi-Fi

This block uses the secrets you saved earlier and sets up a fallback hotspot in case the device cannot reach your Wi-Fi.

```yaml
wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password

  ap:
    ssid: "Apollo ESK-1 Hotspot"
```

If the device cannot connect to your Wi-Fi at boot, it will broadcast its own network called **Apollo ESK-1 Hotspot**. You can join that network from your phone or laptop to fix the credentials.

### Captive portal

Pairs with the fallback hotspot to give you a web page for entering Wi-Fi details when you connect to the hotspot.

```yaml
captive_portal:
```

### Logger

Enables ESPHome's logging output. You'll see these logs in the ESPHome Device Builder dashboard when viewing the device, and they're invaluable for debugging.

```yaml
logger:
```

### Binary sensors

Binary sensors report on or off state. The first one tracks whether the device is connected to Home Assistant. The second exposes a GPIO pin so you can wire up the button module or any other digital input.

```yaml
binary_sensor:
  - platform: status
    name: Online
    id: ha_connected

  - platform: gpio
    pin:
      number: GPIO9
      inverted: true
      mode:
        input: true
        pullup: true
    id: my_button
    name: "Button"
```

| Option | Description |
| --- | --- |
| `platform: status` | Reports the HA connection state. Useful for automations that check device availability. |
| `platform: gpio` | A simple digital input. |
| `number: GPIO9` | The physical pin you've wired the input to. |
| `inverted: true` | The pin reads LOW when the button is pressed (active-low). |
| `pullup: true` | Enables the C6's internal pull-up resistor so the pin doesn't float. |

### Complete configuration

```yaml title="apollo-esk-1.yaml"
substitutions:
  name: apollo-esk-1
  version: "25.5.5.1"
  device_description: ${name} made by Apollo Automation - version ${version}.

esphome:
  name: "${name}"
  friendly_name: Apollo ESPHome Starter Kit
  comment: ${device_description}
  name_add_mac_suffix: true
  platformio_options:
    board_build.flash_mode: dio
  project:
    name: "ApolloAutomation.ESK-1"
    version: "${version}"
  min_version: 2024.6.0

esp32:
  board: esp32-c6-devkitm-1
  variant: esp32c6
  flash_size: 8MB
  framework:
    type: esp-idf

api:

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  ap:
    ssid: "Apollo ESK-1 Hotspot"

captive_portal:

logger:

binary_sensor:
  - platform: status
    name: Online
    id: ha_connected

  - platform: gpio
    pin:
      number: GPIO9
      inverted: true
      mode:
        input: true
        pullup: true
    id: my_button
    name: "Button"
```

## Flash and add to Home Assistant

With your YAML written, flash the device and finish the handoff to Home Assistant.

1. In ESPHome Device Builder, click **Install** on your device.
2. Choose **Plug into the computer running ESPHome Dashboard** (or **Wirelessly** if you're updating an already-flashed device).
3. Wait for the compile and flash to finish. The first compile can take several minutes.
4. Once it's done, the device will reboot and connect to your Wi-Fi.
5. In Home Assistant, go to **Settings → Devices & Services**. Your new device should appear under **Discovered**. Click **Add**, pick an area, and finish.

!!! success "You did it"

    Your ESP32-C6 is now running ESPHome and showing up in Home Assistant. You've written your first ESPHome configuration from scratch.

## Next steps

- Add more sensors and modules to your YAML and re-flash to expand the device.
- Browse [Apollo's other product wikis](https://wiki.apolloautomation.com) for more advanced ESPHome examples.
- Join the [Apollo Discord](https://link.apolloautomation.com/discord) to share what you build.
