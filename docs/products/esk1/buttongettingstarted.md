# Writing Your First ESPHome Configuration

This guide walks you through building an ESPHome YAML configuration from scratch. By the end, you'll understand each section and have your Apollo Button Dev Kit connected to Home Assistant.

---

## Understanding ESPHome YAML Structure

ESPHome configurations are written in YAML, a human-readable format that uses indentation to define structure. Each section controls a different aspect of your device's behavior.

!!! tip "YAML Basics"
    - Indentation matters—use **2 spaces** (not tabs)
    - Colons separate keys from values
    - Lists use dashes (`-`)

---

## 1. Substitutions

Substitutions are variables you define once and reuse throughout your configuration. This keeps your code clean and makes updates simple.

```yaml
substitutions:
  name: apollo-button-1
  version: "24.7.15.1"
  device_description: ${name} made by Apollo Automation - version ${version}.
```

| Variable | Purpose |
|----------|---------|
| `name` | Device identifier used in ESPHome and Home Assistant |
| `version` | Track your firmware version |
| `device_description` | Human-readable description (note how it references other variables with `${}`) |

!!! note "Using Substitutions"
    Reference any substitution elsewhere in your config using `${variable_name}` syntax.

---

## 2. ESPHome Core Configuration

This section defines how your device appears in ESPHome and Home Assistant.

```yaml
esphome:
  name: "${name}"
  friendly_name: Apollo Button Dev Kit
  comment: Apollo Button Dev Kit
  name_add_mac_suffix: true
  platformio_options:
    board_build.flash_mode: dio

  project:
    name: "ApolloAutomation.ButtonDev-1"
    version: "${version}"
  min_version: 2024.6.0
```

**Key options explained:**

| Option | Description |
|--------|-------------|
| `name` | Internal device name (pulled from substitutions) |
| `friendly_name` | The name displayed in Home Assistant's UI |
| `comment` | Optional description shown in ESPHome dashboard |
| `name_add_mac_suffix` | Adds unique MAC address suffix—useful when flashing multiple identical devices |
| `platformio_options` | Low-level build settings (DIO flash mode for ESP32-C6) |
| `project` | Identifies this as an Apollo Automation device for updates |
| `min_version` | Ensures compatibility with ESPHome features used |

---

## 3. ESP32 Board Definition

Tell ESPHome which microcontroller you're using.

```yaml
esp32:
  board: esp32-c6-devkitm-1
  variant: esp32c6
  flash_size: 8MB
  framework:
    type: esp-idf
```

| Option | Description |
|--------|-------------|
| `board` | The specific development board type |
| `variant` | ESP32 chip variant (C6 in this case) |
| `flash_size` | Available flash memory |
| `framework` | Build framework—ESP-IDF is recommended for ESP32-C6 |

!!! warning "Framework Note"
    The ESP32-C6 requires `esp-idf` framework. The older `arduino` framework is not fully supported on this chip.

---

## 4. Home Assistant API

This single line enables the native Home Assistant API connection.

```yaml
api:
```

That's it! ESPHome handles the encryption and connection automatically. Once your device is online, Home Assistant will discover it.

!!! info "Encryption"
    By default, ESPHome generates an encryption key on first install. You'll see this key in the ESPHome dashboard logs during initial setup.

---

## 5. WiFi Configuration

Configure how your device connects to your network.

```yaml
wifi:
  # Enable fallback hotspot (captive portal) in case wifi connection fails
  ap:
    ssid: "Apollo Button Hotspot"
```

This minimal configuration creates a **fallback hotspot**. If the device can't connect to WiFi, it broadcasts its own network you can join to configure it.

### Optional: Hardcode Your WiFi Credentials

```yaml
wifi:
  ssid: "Your_WiFi_Name"
  password: "Your_WiFi_Password"
  
  # Fallback hotspot
  ap:
    ssid: "Apollo Button Hotspot"
```

!!! tip "Secrets File"
    For better security, store credentials in a separate `secrets.yaml` file:
    ```yaml
    wifi:
      ssid: !secret wifi_ssid
      password: !secret wifi_password
    ```

---

## 6. Captive Portal

Works with the fallback hotspot to provide a web-based configuration interface.

```yaml
captive_portal:
```

When connected to the fallback hotspot, your phone or computer will automatically open a configuration page where you can enter your WiFi credentials.

---

## 7. Logger

Enables logging output for debugging.

```yaml
logger:
```

Logs appear in the ESPHome dashboard when viewing device logs. Useful for troubleshooting connection issues or sensor problems.

---

## 8. Binary Sensors

Now let's add some actual functionality—sensors that report on/off states.

```yaml
binary_sensor:
  - platform: status
    name: Online
    id: ink_ha_connected
    
  - platform: gpio
    pin: 
      number: GPIO9
      inverted: true
      mode:
        input: true
        pullup: true
    id: reset_button
    name: "Button"
```

### Status Sensor

```yaml
- platform: status
  name: Online
  id: ink_ha_connected
```

Reports whether the device is connected to Home Assistant. Useful for automations that check device availability.

### Physical Button

```yaml
- platform: gpio
  pin: 
    number: GPIO9
    inverted: true
    mode:
      input: true
      pullup: true
  id: reset_button
  name: "Button"
```

| Option | Description |
|--------|-------------|
| `platform: gpio` | A simple digital input |
| `number: GPIO9` | The physical pin the button is connected to |
| `inverted: true` | Button reads LOW when pressed (active-low) |
| `pullup: true` | Enables internal pull-up resistor |
| `id` | Internal reference for use in automations |
| `name` | How it appears in Home Assistant |

---

## Complete Configuration

Here's everything together:

```yaml
substitutions:
  name: apollo-button-1
  version: "24.7.15.1"
  device_description: ${name} made by Apollo Automation - version ${version}.

esphome:
  name: "${name}"
  friendly_name: Apollo Button Dev Kit
  comment: Apollo Button Dev Kit
  name_add_mac_suffix: true
  platformio_options:
    board_build.flash_mode: dio

  project:
    name: "ApolloAutomation.ButtonDev-1"
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
  ap:
    ssid: "Apollo Button Hotspot"

captive_portal:

logger:

binary_sensor:
  - platform: status
    name: Online
    id: ink_ha_connected
    
  - platform: gpio
    pin: 
      number: GPIO9
      inverted: true
      mode:
        input: true
        pullup: true
    id: reset_button
    name: "Button"
```

---

## Next Steps

- **Flash your device** using the ESPHome dashboard
- **Add it to Home Assistant** when prompted
- **Create automations** using your new button entity

!!! success "You Did It!"
    You've written your first ESPHome configuration from scratch. The button will now appear in Home Assistant as a binary sensor you can use in automations.