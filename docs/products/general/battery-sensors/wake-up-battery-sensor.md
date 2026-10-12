---
title: Apollo Battery Devices - wake up battery device.
description: How to wake up your Apollo device which is currently sleeping.
---
There are two ways to wake a sleeping Apollo battery sensor: press the reset button, or hold the boot button. Select your device below for the button locations.

=== "TEMP-1B"

    **Method 1: Reset button.** Press and release the reset button to restart the device.

    ![TEMP-1B with lid off, tweezers pointing at the RST reset button](/assets/temp-1-reset-button-lid-off.jpg)

    **Method 2: Boot button.** Quickly press and hold the boot button for 4-5 seconds.

    ![TEMP-1B with lid off, tweezers pointing at the BOOT button](/assets/temp-1b-boot-button-lid-off.jpg)

    Button locations: [TEMP-1B boot mode](https://wiki.apolloautomation.com/products/temp1b/troubleshooting/temp1b-boot-mode/).

=== "PLT-1B"

    **Method 1: Reset button.** Press and release the reset button to restart the device.

    ![PLT-1B circuit board with tweezers pointing at the reset button](/assets/plt-boot-mode-pic-6-1.jpg)

    **Method 2: Boot button.** Quickly press and hold the boot button for 4-5 seconds.

    ![PLT-1B circuit board with tweezers pointing at the BOOT button next to the USB-C port](/assets/plt-boot-mode-pic-2.jpg)

    Button locations: [PLT-1B boot mode](https://wiki.apolloautomation.com/products/plt1b/troubleshooting/plt1b-boot-mode/).

=== "BTN-1"

    **Method 1: Reset button.** Press and release the reset (left) button to restart the device.

    **Method 2: Boot button.** Quickly press and hold the boot (right) button for 4-5 seconds.

    ![Side of the BTN-1 with arrows marking the Reset button on the left and Boot button on the right](/assets/btn-1-reset-boot-buttons.png)

    Button locations: [BTN-1 boot mode](https://wiki.apolloautomation.com/products/btn1/troubleshooting/btn1-boot-mode/).

=== "H-1"

    !!! note "Smart firmware only"

        The H-1 only sleeps when running the [smart firmware](https://wiki.apolloautomation.com/products/h1/reflash/). These steps apply when it is running that firmware.

    **Method 1: Reset button.** Press and release the reset button to restart the device.

    **Method 2: Boot button.** Quickly press and hold the boot button for 4-5 seconds.

    ![H-1 tree-shaped circuit board with the Boot and Reset buttons circled in red](/assets/screenshot-2024-11-01-015948.png)

    Button locations: [H-1 boot mode](https://wiki.apolloautomation.com/products/h1/boot-mode/).

=== "H-2"

    !!! note "Smart firmware only"

        The H-2 only sleeps when running the [smart firmware](https://wiki.apolloautomation.com/products/h2/troubleshooting/reflash/). These steps apply when it is running that firmware.

    **Method 1: Reset button.** Press and release the reset (left) button to restart the device.

    **Method 2: Boot button.** Quickly press and hold the boot (right) button for 4-5 seconds.

    ![H-2 snowflake-shaped circuit board with arrows marking the Reset and Boot buttons](/assets/h-2-reset-and-boot-buttons-labeled.png)

    Button locations: [H-2 boot mode](https://wiki.apolloautomation.com/products/h2/troubleshooting/boot-mode/).

Your device is now awake, but it will not stay awake on its own yet. Click the **Prevent Sleep** button on your device page in Home Assistant, or directly on the device web server such as plt-1.local or its IP address.

!!! success "Head to the awake helper wiki article"

    If you need to keep your sensor awake for extended periods of time we suggest using our [OTA awake helper](https://wiki.apolloautomation.com/products/general/battery-sensors/awake-ha-helper/).
