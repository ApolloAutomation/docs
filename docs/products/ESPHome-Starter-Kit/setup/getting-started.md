---
title: Getting Started with the ESPHome Starter Kit
description: Step by step guide for getting started with the ESPHome Starter Kit
---
# ESPHome Starter Kit - Getting Started

This guide walks you through installing the ESPHome Device Builder app, and writing your first ESPHome YAML configuration from scratch.

By the end you'll have your ESPHome Starter Kit flashed with a working configuration and showing up in Home Assistant and with a working web server accessible at its IP address or esphome-starter-kit.local in a browser.

---

## 1\. Setting up ESPHome Device Builder

ESPHome Device Builder is the software that gives you a user interface for writing, compiling, and flashing ESPHome configurations. You'll use it to build the firmware for your kit.

Think of it like telling the starter kit about what devices it has connected and how to use them!

Pick the platform you'll be running ESPHome Device Builder on:

=== "Windows"

    1. <a href="https://github.com/esphome/esphome-desktop/releases/download/v0.7.0/ESPHome.Builder_0.7.0_x64-setup.exe" title="Download the ESPHome Device Builder for Windows" target="_blank" rel="noreferrer nofollow noopener">Download the ESPHome Device Builder for Windows</a>.
    2. Open the installer and click **Next** then click **Next** again to start the installation process. Once it shows completed, click **Next** again then **Finish** to complete the installation.
       * If Windows shows a blue **Windows protected your PC** warning, click **More info → Run anyway** to continue.

    ![](../../../assets/esphome-builder-install-windows.gif)

    3. Once installed, a web browser should launch and navigate to <a href="http://localhost:6052/" target="_blank" rel="noreferrer nofollow noopener">http://localhost:6052/</a>. Once you see this page, your ESPHome Device Builder installation is complete.
       * Use a Chromium-based browser such as Chrome or Edge. Firefox does not yet support WebSerial, which is required for the initial flashing of the device over USB. If Firefox is your default, copy the URL into Chrome or Edge instead.
    4. Navigate to the **system tray** (bottom right of your Windows taskbar). Hover over **Backend** and switch from Classic to the ESPHome Builder Beta with the new layout and features.

    ![](../../../assets/esphome-builder-backend-switch-to-beta.gif)

    5. Wait 30+ seconds, then refresh your browser (F5). You should now see the new ESPHome Device Builder Preview.

    ![](../../../assets/esphome-device-builder-preview-image.png)

=== "Mac"

    1. Download the ESPHome Device Builder for Mac. Pick the build that matches your chip:

        - <a href="https://github.com/esphome/esphome-desktop/releases/download/v0.7.0/ESPHome.Builder_0.7.0_aarch64.dmg" target="_blank" rel="noreferrer nofollow noopener">Apple Silicon (M1, M2, M3, M4)</a>
        - <a href="https://github.com/esphome/esphome-desktop/releases/download/v0.7.0/ESPHome.Builder_0.7.0_x64.dmg" target="_blank" rel="noreferrer nofollow noopener">Intel Mac</a>

    2. Open the `.dmg` and drag **ESPHome Builder** into your Applications folder. Launch it from Applications or Spotlight.

        - On first launch, macOS may block the app with a Gatekeeper warning. If that happens, right-click the app in Applications and choose **Open**, then click **Open** in the confirmation dialog. After the first launch, double-click will work normally.

    <!-- TODO: add a Mac installer gif/screenshot if available. -->

    3. Once installed, a web browser should launch and navigate to <a href="http://localhost:6052/" target="_blank" rel="noreferrer nofollow noopener">http://localhost:6052/</a>. Once you see this page, your ESPHome Device Builder installation is complete.

        - Use a Chromium-based browser such as Chrome or Edge. Safari and Firefox do not currently support WebSerial, which is required for the initial USB flash.

    4. Find the **ESPHome Builder** icon in the menu bar (top right of your Mac's screen). Click it, hover over **Backend**, and switch from Classic to the ESPHome Builder Beta.

    <!-- TODO: confirm the exact menu bar wording on Mac and add a screenshot. -->

    5. Wait 30+ seconds, then refresh your browser. You should now see the new ESPHome Device Builder Preview.

=== "Home Assistant App"

    The ESPHome Device Builder runs as a Home Assistant app served right inside your existing HA dashboard. This is the easiest option if you already run Home Assistant OS or a supervised install.

    1. In Home Assistant, open **Settings → Apps → App Store**.
    2. Search for **ESPHome Device Builder** and click **Install**.
    3. Once installed, click **Start**, then **Open Web UI**. The Device Builder will open inside your Home Assistant dashboard.

    <!-- TODO: confirm the exact app name shown in the HA App Store (e.g. "ESPHome Device Builder" vs "ESPHome Builder Beta") and add a screenshot of the install flow. -->

    !!! info "Already on the new layout"

        The HA app version of Device Builder is already the new beta backend, so you can skip the backend toggle and browser refresh shown in the desktop tabs.

=== "Linux"

    1. Download the ESPHome Device Builder for Linux. Pick the package that fits your distro:

        - <a href="https://github.com/esphome/esphome-desktop/releases/download/v0.7.0/ESPHome.Builder_0.7.0_amd64.AppImage" target="_blank" rel="noreferrer nofollow noopener">AppImage (works on any distro)</a>
        - <a href="https://github.com/esphome/esphome-desktop/releases/download/v0.7.0/ESPHome.Builder_0.7.0_amd64.deb" target="_blank" rel="noreferrer nofollow noopener">.deb (Debian / Ubuntu)</a>
        - <a href="https://github.com/esphome/esphome-desktop/releases/download/v0.7.0/ESPHome.Builder-0.7.0-1.x86_64.rpm" target="_blank" rel="noreferrer nofollow noopener">.rpm (Fedora / RHEL)</a>

    2. Install or run the file you downloaded:

        - **AppImage:** `chmod +x ESPHome.Builder_0.7.0_amd64.AppImage` then double-click the file, or run it from a terminal.
        - **.deb:** `sudo apt install ./ESPHome.Builder_0.7.0_amd64.deb`
        - **.rpm:** `sudo dnf install ./ESPHome.Builder-0.7.0-1.x86_64.rpm`

    <!-- TODO: add a Linux installer screenshot if available. -->

    3. Once installed, a web browser should launch and navigate to <a href="http://localhost:6052/" target="_blank" rel="noreferrer nofollow noopener">http://localhost:6052/</a>. Once you see this page, your ESPHome Device Builder installation is complete.

        - Use a Chromium-based browser such as Chrome or Edge. Firefox does not currently support WebSerial, which is required for the initial USB flash.

    4. Look for the **ESPHome Builder** icon in your system tray or notification area. Its exact location depends on your desktop environment (top bar on GNOME, system tray on KDE, XFCE, or Cinnamon). Click it, hover over **Backend**, and switch from Classic to the ESPHome Builder Beta.

    <!-- TODO: confirm the system tray wording on Linux. -->

    5. Wait 30+ seconds, then refresh your browser. You should now see the new ESPHome Device Builder Preview.

### Set up Wi-Fi Credentials

1\. Fill in your Wi-Fi network name (SSID) and Wi-Fi password then click Save credentials.

![](../../../assets/esphome-builder-enter-wifi-credentials.gif)

2\. If you make a mistake or want to change this later, click the 3 dots menu in the top right then select Secrets. Click the Eye icon to unhide the Wi-Fi SSID and password and change them then click Save in the bottom right.

!!! tip "Protip: You can put all kinds of credentials here that you want kept secret!"

    One popular option is to store your encryption keys here. That way, you can share your full YAML with other users without needing to edit and hide your encryption key. See our <a href="https://wiki.apolloautomation.com/products/ESPHome-Starter-Kit/tutorials/using-secrets.md" target="_blank" rel="noreferrer nofollow noopener">using secrets wiki for step by step directions</a>!

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