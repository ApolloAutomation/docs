---
title: Bluetooth Proxy Setup
description: Tutorial for how to turn your Apollo device into a BLE proxy!
---
# Bluetooth Proxy

--8<-- "_snippets/bluetooth-proxy/intro.md"

### Method 1: Switch to \_BLE.yaml firmware

Select your product below to see the full walkthrough.

=== "AIR-1"

    --8<-- "_snippets/bluetooth-proxy/method1-air-1.md"

=== "MSR-1"

    --8<-- "_snippets/bluetooth-proxy/method1-msr-1.md"

=== "MSR-2"

    --8<-- "_snippets/bluetooth-proxy/method1-msr-2.md"

=== "MTR-1"

    --8<-- "_snippets/bluetooth-proxy/method1-mtr-1.md"

=== "R-PRO-1"

    --8<-- "_snippets/bluetooth-proxy/no-ble-fork-tab.md"

=== "PUMP-1"

    --8<-- "_snippets/bluetooth-proxy/no-ble-fork-tab.md"

=== "PLT-1"

    --8<-- "_snippets/bluetooth-proxy/method1-plt-1.md"

=== "PLT-1B"

    --8<-- "_snippets/bluetooth-proxy/method1-plt-1b.md"

=== "TEMP-1"

    --8<-- "_snippets/bluetooth-proxy/method1-temp-1.md"

=== "TEMP-1B"

    --8<-- "_snippets/bluetooth-proxy/method1-temp-1b.md"

=== "BTN-1"

    !!! info "This product needs Method 2"

        This product does not have a prebuilt \_BLE.yaml firmware, so Method 1 does not apply. Scroll down and follow **Method 2** to add the BLE proxy yaml to your existing config by hand.

        Sleep must be disabled for the BTN-1 to work as a Bluetooth Proxy. See the [Prevent Sleep guide](https://wiki.apolloautomation.com/products/btn1/additional-info/prevent-sleep/).

---

### Method 2: Manually enter the BLE proxy yaml

This method works the same on every product.

--8<-- "_snippets/bluetooth-proxy/method2.md"
