---
title: Getting Started
description: Getting started with your new M-1 LED Matrix on WLED or WLED-MM.
---
# Getting Started

Congrats on your new M-1! Pick your firmware below and the rest of the M-1 wiki follows your choice.

New units ship with **WLED**. Units shipped earlier came with **WLED-MM**. Open your M-1 in a browser and tap **Info** to see which you have: 16.0.1 or newer is WLED, 14.5.1 is WLED-MM. Running ESPHome instead? Head to [Set Up ESPHome](/products/m1/setup/getting-started-m1-esphome.md).

### Attach M-1 LED Controller

Your M-1 LED Matrix and M-1 controller were shipped separately to minimize damage in shipping. Gently attach the controller to the back of the M-1 LED Matrix panel as shown in the GIF below.

![](/assets/m1-matrix-attach-controller.webp)

### Connect to Wi-Fi

=== "WLED"

    1\. Plug in USB-C power. The M-1 boots within a couple of seconds and displays a setup card on the panel with a QR code.

    ![](/assets/wled-16-boot-image-preset.webp)

    2\. Scan the QR code, or join the open Wi-Fi network named **Apollo M-1** from your phone. There is no password.

    3\. Your phone should pop up "Welcome to WLED!". If it does not, open a browser and go to <a href="http://4.3.2.1/" target="_blank" rel="noopener">http://4.3.2.1/</a>.

    4\. Tap **WIFI SETTINGS**, enter your network name and password, and tap **Save & Connect**.

    !!! tip "Set your mDNS address here too"

        Enter something like **apollo-led-matrix** and you can reach the device at http://apollo-led-matrix.local instead of hunting for its IP.

    The M-1 reboots onto your network and the panel lights up with the default effect. Nothing else to configure, the shipped image already sets up a single 64x64 panel.

=== "WLED-MM"

    Your device is ready to connect to your Wi-Fi and begin controlling via Home Assistant, the WLED app for iPhone and Android, or via a web browser!

    1\. Plug in the USB-C power in and the M-1 device will boot within a couple seconds. Head to the available Wi-Fi networks on your phone and select Apollo M-1. It should pop up saying "Welcome to WLED!". If this popup does not occur, please open a web browser and navigate to <a href="http://4.3.2.1/" target="_blank" rel="noopener">http://4.3.2.1/</a> or <a href="http://wled.me" target="_blank" rel="noreferrer nofollow noopener">http://wled.me</a> and you should be prompted with the same image seen below.

    ![](/assets/m-1-getting-started.png)

    2\. Tap on **WI-FI Settings** then input your Wi-Fi SSID where it shows **Your\_Network** and input your Wi-Fi password directly below it and then click **Save and Connect**.

    !!! tip "You can also set your hostname here such as apollo-led-matrix"

        Later, you can use this to access your device at http://apollo-led-matrix.local in a browser instead of using the IP address!

    #### Post-Connect Setup

    !!! warning "Please complete setup by changing a few settings!"

        The firmware we use currently does not support us pre-configuring a few settings but they are required to be set for you to use the M-1 LED Matrix successfully. Please follow the two steps below to finish setting up your device!

    1\. Click on **Config**, then **LED Preferences**. set **Chain Length** to **1** then uncheck the "enable automatic brightness limiter and click **Save**. Make sure to select **Hub75Matrix** is set to **64x64**.

    ![](/assets/m-1-led-settings.gif)

    2\. Click on **Config**, then **2D Configuration**. Select **2D Matrix**, click the circle next to **Basic**, change the **Panel dimensions (WxH)** to **64 x 64** and click **Save**.

    ![](/assets/m-1-2d-settings.gif)

### Join to Home Assistant

1\. Head to the <a href="http://homeassistant.local:8123/config/integrations" target="_blank" rel="noreferrer nofollow noopener">Integrations page in Home Assistant</a>. The M-1 is discovered automatically by the WLED integration.

![](/assets/m-1-setup-wled-integration-add-device.png)

2\. Click **Add**, then **Submit**.

![](/assets/m-1-setup-wled-integration-click-submit.png)

3\. Give it a name and a location, then click **Skip** and **Finish**.

![](/assets/m-1-setup-wled-integration-name-location-finish.png)

4\. Open the <a href="http://homeassistant.local:8123/config/integrations/integration/wled" target="_blank" rel="noreferrer nofollow noopener">WLED integration page</a> and click your M-1.

![](/assets/m-1-setup-wled-integration-click-device-2.png)

5\. From here you can change the color, pick effects, run presets, and more.

![](/assets/m-1-setup-wled-integration-test-device.png)

#### What Next

=== "WLED"

    Draw your own images and scrolling text right on the device with [Pixel Forge](/products/m1/examples/pixel-forge.md), or wire up more panels with [Multiple Panels](/products/m1/setup/m1-multiple-panels.md).

    [Try Pixel Forge](/products/m1/examples/pixel-forge.md){: .md-button .md-button--primary }

=== "WLED-MM"

    Add a custom GIF to your matrix, or add more panels with [Multiple Panels](/products/m1/setup/m1-multiple-panels.md). On a Rev6 controller you can also [move up to WLED](/products/m1/setup/upgrade-to-wled.md) and keep your settings.

    [Add GIFs to your M-1](/products/m1/examples/add-gifs-to-wled.md){: .md-button .md-button--primary }
