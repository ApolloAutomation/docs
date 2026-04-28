---
title: Reflash M-1 (ESPHome)
description: Step by step guide for reflashing the M-1 with the hub75-studio ESPHome firmware
---
# Reflash M-1 (ESPHome)

!!! info "Use this article to flash or recover the M-1 with the hub75-studio ESPHome firmware."

    Reflashing must be done in Chrome, Edge, or another Chromium-based browser.

!!! success "Use the Rev6 build"

    All M-1 units currently being sold are Rev6. On the <a href="https://pavlov-net.github.io/hub75-studio/" target="_blank" rel="noreferrer nofollow noopener">hub75-studio installer</a>, select the **Rev6** firmware before clicking **Connect**.

1\. Plug a USB-C cable that supports power and data into your computer.

2\. Push and hold the boot button (the left button) on the M-1 controller. While still holding the button, plug the USB-C cable into the M-1, then release the button.

![](/assets/m-1-hold-boot-webp.webp)

3\. Open <a href="https://pavlov-net.github.io/hub75-studio/" target="_blank" rel="noreferrer nofollow noopener">https://pavlov-net.github.io/hub75-studio/</a> in your Chromium browser.

4\. Pick the **Rev6** firmware, click **Connect**, select the M-1's COM port, and follow the installer prompts.

5\. Once the installer reports completion, close the browser tab.

!!! warning "Power cycle your device before doing anything else!"

    Your device is still in boot mode. Unplug power and plug it back in so it boots normally.

[Head to the ESPHome Getting Started article to set up your M-1!](https://wiki.apolloautomation.com/products/m1/setup/getting-started-m1-esphome/){: .md-button .md-button--primary }
