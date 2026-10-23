---
title: Putting the PLT-1B in boot mode
description: Step by step guide for putting The PLT-1B In Boot Mode.
---
# Putting the PLT-1B in boot mode

!!! info "This will cover how to put the PLT-1B into boot mode."

    This is needed to force the device into boot mode to reflash the firmware.

![PLT-1B diagram labeling the reset button on the left and the USB-C port and boot button on the right](/assets/plt-1b-buttons-2.png)

## Method 1: Boot button only

You can put your device into boot mode with only the boot button and a pin.

1\. Position the PLT-1B as shown in the image below and locate the small opening to press the boot button.

![Open PLT-1B case with tweezers pointing at the boot button (SW1) next to the USB-C port](/assets/plt-boot-mode-pic-2.jpg)

![Closed PLT-1B case with tweezers inserted into the boot button opening on the side](/assets/plt-boot-mode-pic-4.jpg)

2\. Use a pin to press and hold the boot button, while holding the boot button plug the PLT-1B back into your computer/power and then release the boot button

3\. Continue with [uploading the firmware](https://wiki.apolloautomation.com/products/plt1b/troubleshooting/plt1b-code/)

## Method 2: Boot and reset buttons

You can also put your device into boot mode by holding the boot button down while you press and release the reset button.

1\. Plug in the device

2\. Put your PLT-1B in boot mode. Use both buttons, in this order:

- Press and hold the **boot** button (next to the USB-C port, shown in the images above). Keep holding it.
- While you're still holding **boot**, press and release the **reset** button (labeled RST, shown in the images below).
- Let go of **boot**.

!!! warning "Keep holding boot the whole time"

    Pressing **reset** by itself only restarts the PLT-1B. It goes into boot mode only when **boot** is held down while you press and release **reset**.

![Open PLT-1B case with tweezers pointing near the reset button labeled SW2 RST](/assets/plt-boot-mode-pic-6.jpg)

![Closed PLT-1B case with tweezers pointing at the reset button opening on the side](/assets/plt-boot-mode-pic-7.jpg)

3\. Continue with [uploading the firmware](https://wiki.apolloautomation.com/products/plt1b/troubleshooting/plt1b-code/)