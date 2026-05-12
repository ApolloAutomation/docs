---
title: Getting Started with the ESPHome Starter Kit
description: Step by step guide for getting started with the ESPHome Starter Kit
---
# ESPHome Starter Kit - Getting Started

This guide walks you through installing the ESPHome Device Builder app, and writing your first ESPHome YAML configuration from scratch.

By the end you'll have your ESPHome Starter Kit flashed with a working configuration and showing up in Home Assistant and with a working web server accessible at its IP address or hostname.local in a browser.

---

## 1\. Setting up ESPHome Device Builder

ESPHome Device Builder is a standalone program that gives you a user interface for writing, compiling, and flashing ESPHome configurations. You'll use it to build the firmware for your kit.

Think of it like telling the starter kit about what devices it has connected and how to use them!

1\. <a href="https://github.com/esphome/esphome-desktop/releases/download/v0.7.0/ESPHome.Builder_0.7.0_x64-setup.exe" title="Download the ESPHome Device Builder for Windows" target="_blank" rel="noreferrer nofollow noopener">Click here to download</a> the ESPHome Device builder. If you're using MAC, Linux, or Home Assistant OS then select the toggle above for those specific instructions

2\. Open the installer and click **Next** then click **Next** again to start the installation process. Once it shows completed, click **Next** again then **Finish** to complete the installation!

\- If Windows shows a blue **Windows protected your PC** warning, click **More info → Run anyway** to continue.

![](../../../assets/esphome-builder-install-windows.gif)

3\. Once installed, a web browser should launch and navigate to this link: <a href="http://localhost:6052/" target="_blank" rel="noreferrer nofollow noopener">http://localhost:6052/</a> Once you see this in your browser your ESPHome Device Builder installation is completed

!!! ! success "You must use a chromium based browser such as chrome or edge at this time!"

    If you are using Firefox as your default browser, it will default to launching the ESPHome Device Builder in your default browser. Unfortunately, at this time Firefox does not support WebSerial so it cannot be used for the initial flashing of the device via USB. Please copy the URL <a href="http://localhost:6052/" target="_blank" rel="noreferrer nofollow noopener">http://localhost:6052/</a> and paste it in a chromium based browser such as chrome or edge. We have heard Firefox is going to support this soonTM so this problem will eventually go away!

4\. Once installed, navigate to the system tray (bottom right of your windows device). Hover over Backend and switch from Classic to the ESPHome Builder Beta with the new layout and features!

![](../../../assets/esphome-builder-backend-switch-to-beta.gif)

5\. Wait for 30+ seconds then refresh your browser (hit F5) and you should see the new ESPHome Device Builder Preview!

![](../../../assets/esphome-device-builder-preview-image.png)

### Fill in your Wi-Fi secrets

ESPHome keeps your Wi-Fi credentials in a separate `secrets.yaml` file so they aren't pasted into every device config.

1. In the ESPHome Device Builder dashboard, click **Secrets** in the top right.
2. Add your Wi-Fi name and password:

```yaml
# Replace the values inside the quotes with your own Wi-Fi name and password.
wifi_ssid: "your-wifi-ssid-here"
wifi_password: "your-wifi-password-here"
```

1. Click **Save**.

### Add a new device

1\. Click **Add new device** then click Create new project

![](../../../assets/device-builder-add-new-device.gif)

2\. Select the Apollo ESPHome Starter Kit and give it a name such as esphome-starter-kit then click **Finish Setup**.

![](../../../assets/device-builder-select-esk-name-it.gif)

### Connect the C6 to your computer

Plug the ESP32-C6 into your computer using a USB-C cable.

!!! tip "First-time flashing"

    The very first time you flash an ESP32-C6, you need to put it into bootloader mode manually:

    1. Hold down the **BOOT** button on the C6.
    2. While still holding **BOOT**, press and release the **RESET** button.
    3. Release the **BOOT** button.

    The board will now stay in bootloader mode until you flash it. After the first flash you usually won't need to do this again.

!!! info "Use a quality USB-C cable and power source"

    ESP32 boards are sensitive to power. If your device keeps restarting, won't be detected, or won't broadcast its hotspot, try a different USB-C cable or a different USB port. A 5V 1A supply is plenty.

---

## 4\. Flash and add to Home Assistant

1. In ESPHome Device Builder, click **Install** on your device.
2. Choose **Plug into the computer running ESPHome Dashboard** (or **Wirelessly** if you're updating an already-flashed device).
3. Wait for the compile and flash to finish. The first compile can take several minutes.
4. Once it's done, the device will reboot and connect to your Wi-Fi.
5. In Home Assistant, go to **Settings → Devices & Services**. Your new device should appear under **Discovered**. Click **Add**, pick an area, and finish.

!!! success "You did it!"

    Your ESP32-C6 is now running ESPHome and showing up in Home Assistant. You've written your first ESPHome configuration from scratch.

## Next steps

* Add more sensors and modules to your YAML and re-flash to expand the device.
* Browse [Apollo's other product wikis](https://wiki.apolloautomation.com) for more advanced ESPHome examples.
* Join the [Apollo Discord](https://link.apolloautomation.com/discord) to share what you build.