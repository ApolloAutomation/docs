---
title: Adding the Battery
description: >-
  Connect the rechargeable LiPo battery to your ESPHome Starter Kit and cut the
  cord on your builds.
---
# Adding the Battery

The battery cuts the cord on your starter kit. It's a rechargeable 3.7V 2800mAh LiPo that plugs into the ESP32-C6 with a 2-pin JST-PH 2.0 connector, so your builds can live anywhere in the home, not just next to a USB port. The ESP32-C6 charges it over the same USB-C cable you've been using all along.

!!! note "Before you start"

    Work through the two prerequisites first:

    * [Start Here](/products/ESPHome-Starter-Kit/start-here.md) to unbox the kit and get familiar with the ESP32-C6.
    * [First Steps](/products/ESPHome-Starter-Kit/setup/first-steps.md) to install ESPHome Device Builder and create your starter kit device.

## Attach the battery

The battery connector only fits one way, but check the wire colors before you push it in. (1)
{ .annotate }

1.  With the connector lined up, the black (ground) wire sits on the side closest to the ESP32-C6 chip and the red wire on the side closest to the USB-C port. If the wires are reversed, stop and don't force it.

Push the connector into the battery port until it seats fully.

![](/assets/esphome-starter-kit-attach-battery.webp)

## Deep Sleep

Wi-Fi is hungry. Left running around the clock, the ESP32-C6 will work through the battery quickly. The fix is the <a href="https://esphome.io/components/deep_sleep/" target="_blank" rel="noreferrer nofollow noopener">Deep Sleep</a> component, which powers the device down between readings so it sips power instead of gulping it.

Add this to your device's YAML in ESPHome Device Builder:

```yaml
deep_sleep:
  id: deep_sleep_1
  run_duration: 30s
  sleep_duration: 10min
```

With this config the device wakes every 10 minutes, stays awake for 30 seconds to connect and report its readings, then goes back to sleep. Tune both numbers to your project: longer sleeps mean longer battery life, shorter sleeps mean fresher data.

A few things to know before you rely on it:

* Deep sleep fits sensor modules best. The [Temp & Humidity module](/products/ESPHome-Starter-Kit/modules/temperature-humidity-module.md) only needs a reading every few minutes, so it can sleep the rest of the time.
* A timer isn't the only way to wake up. A GPIO pin can wake the device too, so a press on the [Button module](/products/ESPHome-Starter-Kit/modules/button-module.md) can pull the ESP32-C6 out of deep sleep. Our <a href="https://github.com/ApolloAutomation/BTN-1" target="_blank" rel="noreferrer nofollow noopener">BTN-1</a> is built around exactly this trick: it sleeps for months on a battery and wakes the instant you press a button.
* While the device sleeps it drops off Wi-Fi, so it shows as unavailable in Home Assistant and the web server between wake-ups. That's normal.
* If an OTA update won't take because the device keeps falling asleep, add the Prevent Sleep switch below, or plug in the USB-C cable and flash it over the wire.

??? example "How the BTN-1 wakes on button press"

    This is the deep sleep block from the <a href="https://github.com/ApolloAutomation/BTN-1/blob/main/Integrations/ESPHome/Core.yaml" target="_blank" rel="noreferrer nofollow noopener">BTN-1 software</a>. The `esp32_ext1_wakeup` section tells the ESP32-C6 to wake when any of the button pins goes high:

    ```yaml
    deep_sleep:
      id: deep_sleep_1
      sleep_duration: 24h
      run_duration: 90s
      esp32_ext1_wakeup:
        mode: ANY_HIGH
        pins:
          - number: GPIO2
            allow_other_uses: true
          - number: GPIO4
            allow_other_uses: true
          - number: GPIO5
            allow_other_uses: true
          - number: GPIO6
            allow_other_uses: true
    ```

    One difference for the starter kit: the Button module's pin reads LOW when pressed (it uses a pull-up), the opposite of the BTN-1's buttons. So on the starter kit you'd wake on `mode: ALL_LOW` with GPIO6 as the only pin.

#### Add a Prevent Sleep switch

A sleeping device is a hard one to update. Every Apollo battery device ships with a **Prevent Sleep** switch for exactly this reason, and you can build the same thing into your starter kit config. It's a template switch that holds the device awake while it's on:

```yaml
switch:
  - platform: template
    name: "Prevent Sleep"
    id: prevent_sleep
    icon: mdi:sleep
    restore_mode: RESTORE_DEFAULT_ON
    optimistic: true
    entity_category: config
    on_turn_on:
      then:
        - lambda: |-
            id(deep_sleep_1).prevent_deep_sleep();
    on_turn_off:
      then:
        - lambda: |-
            id(deep_sleep_1).allow_deep_sleep();
```

The `restore_mode: RESTORE_DEFAULT_ON` line means the device stays awake by default. Get everything working and updated first, then flip the switch off in Home Assistant or the web server when you're ready for the sleep cycle to start. Toggle it while the device is awake, a sleeping device can't hear the command until its next wake-up.

Our battery devices also support a Home Assistant helper that holds every Apollo device awake at once for software updates. (1) The same pattern works here, see the [Awake HA Helper guide](/products/general/battery-sensors/awake-ha-helper.md) for the walkthrough.
{ .annotate }

1.  We say software because it's the friendlier word. The technically correct term is firmware: code that runs directly on the chip instead of on a computer. That's the word ESPHome's own docs use.

## Charging

Plug the USB-C cable into the ESP32-C6 and the battery charges while the device keeps running. There's nothing to configure and no charger to buy, any USB-C power source works.

If you ever need to disconnect the battery, grip the connector body and pull it straight out. Pulling on the wires can rip them out of the connector.

--8<-- "_snippets/community-help.md"
