---
title: What is YAML?
description: A short primer on YAML, the configuration format ESPHome uses, with examples drawn from the ESPHome Starter Kit.
---
# What is YAML?

YAML is a plain-text format used to describe configuration in a way that is readable for both people and computers. ESPHome uses YAML to describe what your device is and what it should do.

You do not have to write YAML yourself when using the **ESPHome Device Builder**. The Builder generates it for you as you click around. Recognising what you are looking at when you peek at the YAML view helps you understand what your device is doing, and a little YAML opens up advanced settings the GUI does not expose.

## The basics

YAML is built from three ideas: key-value pairs, indentation, and lists.

#### Key and value

Most lines are a name, a colon, then a value:

```yaml
name: esphome-starter-kit
platform: ESP32
```

#### Indentation groups things together

Indentation shows which settings belong to which item:

```yaml
wifi:
  ssid: my-wifi-network
  password: my-wifi-password
```

Here, `ssid` and `password` belong to `wifi`. The two spaces in front are what links them.

#### Lists use dashes

A dash at the start of a line means "this is one item in a list":

```yaml
sensor:
  - platform: dht
    pin: GPIO4
  - platform: dht
    pin: GPIO5
```

That is two sensors, each with its own settings.

#### Comments

A `#` starts a comment. Anything after it on that line is ignored, which makes it useful for leaving yourself notes:

```yaml
# Built-in LED on the ESP32-C6
light:
  - platform: esp32_rmt_led_strip
    pin: GPIO8
```

#### Quoting strings

Most text values do not need quotes. You only need quotes if your value contains special characters, starts with a number, or could be confused for something else (like the word `yes` or `no`). When in doubt, quotes are always safe:

```yaml
wifi_password: "my-password-with-spaces and symbols!"
```

## Spacing matters

YAML uses indentation to figure out which settings belong to which item. Get the spacing wrong and the Device Builder will refuse to save or compile. Three rules cover almost every mistake.

**Use spaces, never tabs.** Tabs and spaces look the same on screen, but a YAML parser treats them differently. Most editors handle this for you, but if you paste YAML from somewhere else and get errors, tabs are the first thing to check for.

**Two spaces per level, consistently.** Every level of nesting is two more spaces than the parent. The number doesn't strictly have to be two, but it has to stay the same across the whole file. Mixing two-space and four-space indents in one file will fail.

**A space after every colon.** `name: esphome-starter-kit` works. `name:esphome-starter-kit` does not. The parser uses the colon-plus-space to separate keys from values.

A correct example, with the indent levels visible:

```yaml
wifi:                    # top level
  ssid: my-network       # two spaces in, belongs to wifi
  password: my-pass      # two spaces in, belongs to wifi
  ap:                    # two spaces in, belongs to wifi
    ssid: Fallback       # four spaces in, belongs to ap
```

And the same content with broken indentation, which will fail to compile:

```yaml
wifi:
ssid: my-network         # no indent, no longer part of wifi
  password: my-pass
   ap:                   # three spaces, doesn't match siblings
    ssid: Fallback
```

!!! tip "Back up before you edit"

    Before hand-editing YAML in the Device Builder, copy the current contents into a notepad or text file as a safety net. If a misplaced indent breaks the build, you can paste the original back and start over.

## ESPHome example

When you add the Onboard RGB LED component in the Device Builder, the YAML view shows something like this:

```yaml
light:
  - platform: esp32_rmt_led_strip
    name: Onboard RGB LED
    pin: GPIO8
    num_leds: 1
    chipset: WS2812
```

You did not type any of that. The Builder wrote it when you clicked **Add**. Once you can read it, you know exactly what your device is doing.

The official YAML site has the full specification, and the ESPHome docs walk through YAML in the context of ESPHome specifically.

<a href="https://yaml.org/" target="_blank" rel="noreferrer nofollow noopener" class="md-button md-button--primary">YAML official site</a> <a href="https://esphome.io/guides/configuration-types.html" target="_blank" rel="noreferrer nofollow noopener" class="md-button md-button--primary"><img src="/assets/esphome-logo.svg" /> ESPHome YAML guide</a>


--8<-- "_snippets/community-help.md"
