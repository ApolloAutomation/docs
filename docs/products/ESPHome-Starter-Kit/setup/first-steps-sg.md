---
title: First steps with the ESPHome Starter Kit
description: >-
  Install ESPHome Device Builder, write your first ESPHome config for the
  starter kit, and flash the ESP32-C6 over USB.
---
This guide walks you through installing the ESPHome Device Builder app and making your first ESPHome YAML configuration from scratch. By the end, your ESPHome Starter Kit will be flashed with a working configuration, showing up in Home Assistant, and serving a web UI at its IP address or at `esphome-starter-kit.local` in a browser.

## Install ESPHome Device Builder

ESPHome Device Builder is the software that gives you a user interface for writing, compiling, and flashing ESPHome YAML configurations. You'll use it to build the firmware for your kit. Think of it as how you tell the starter kit what is plugged in and what to do with it.

Pick the platform you'll be running ESPHome Device Builder on.

=== "Windows"

    1. <a href="https://github.com/esphome/esphome-desktop/releases/download/v0.7.0/ESPHome.Builder_0.7.0_x64-setup.exe" title="Download the ESPHome Device Builder for Windows" target="_blank" rel="noreferrer nofollow noopener">Download the ESPHome Device Builder for Windows</a>.
    2. Open the installer and click **Next** then click **Next** again to start the installation process. Once it shows completed, click **Next** again then **Finish** to complete the installation.
        - If Windows shows a blue **Windows protected your PC** warning, click **More info → Run anyway** to continue.

    ![ESPHome Device Builder for Windows installer running through its Next and Finish steps](../../../assets/esphome-builder-install-windows.gif)

    3. Once installed, a web browser should launch and navigate to <a href="http://localhost:6052/" target="_blank" rel="noreferrer nofollow noopener">http://localhost:6052/</a>. When you see this page, your ESPHome Device Builder installation is complete.
        - Use a Chromium-based browser such as Chrome or Edge. Firefox does not yet support WebSerial, which is required for the initial flashing of the device over USB. If Firefox is your default, copy the URL into Chrome or Edge instead.
    4. Navigate to the **system tray** (bottom right of your Windows taskbar). Hover over **Backend** and switch from Classic to the ESPHome Builder Beta with the new layout and features.

    ![Windows system tray showing the ESPHome Builder backend menu switching from Classic to Beta](../../../assets/esphome-builder-backend-switch-to-beta.gif)

    5. Wait at least 30 seconds, then refresh your browser (F5). You should now see the new ESPHome Device Builder Preview.

    ![ESPHome Device Builder Preview UI on first load](../../../assets/esphome-device-builder-preview-image.png)

=== "Mac"

    1. Download the ESPHome Device Builder for Mac. Pick the build that matches your chip.

        - <a href="https://github.com/esphome/esphome-desktop/releases/download/v0.7.0/ESPHome.Builder_0.7.0_aarch64.dmg" target="_blank" rel="noreferrer nofollow noopener">Apple Silicon (M1, M2, M3, M4)</a>
        - <a href="https://github.com/esphome/esphome-desktop/releases/download/v0.7.0/ESPHome.Builder_0.7.0_x64.dmg" target="_blank" rel="noreferrer nofollow noopener">Intel Mac</a>

    2. Open the `.dmg` and drag **ESPHome Builder** into your Applications folder. Launch it from Applications or Spotlight.

        - On first launch, macOS may block the app with a Gatekeeper warning. If that happens, right-click the app in Applications and choose **Open**, then click **Open** in the confirmation dialog. After the first launch, double-click will work normally.

    <!-- TODO: add a Mac installer gif/screenshot if available. -->

    3. Once installed, a web browser should launch and navigate to <a href="http://localhost:6052/" target="_blank" rel="noreferrer nofollow noopener">http://localhost:6052/</a>. When you see this page, your ESPHome Device Builder installation is complete.

        - Use a Chromium-based browser such as Chrome or Edge. Safari and Firefox do not currently support WebSerial, which is required for the initial USB flash.

    4. Find the **ESPHome Builder** icon in the menu bar (top right of your Mac's screen). Click it, hover over **Backend**, and switch from Classic to the ESPHome Builder Beta.

    <!-- TODO: confirm the exact menu bar wording on Mac and add a screenshot. -->

    5. Wait at least 30 seconds, then refresh your browser. You should now see the new ESPHome Device Builder Preview.

=== "Home Assistant App"

    The ESPHome Device Builder runs as a Home Assistant app served right inside your existing HA dashboard. This is the most convenient option if you already run Home Assistant OS or a supervised install.

    **<u>Method 1</u>**

    To add the **ESPHome Device Builder** to your Home Assistant instance, use this My button.

    [![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=esphome)

    **<u>Method 2</u>**

    1. In Home Assistant, open **Settings → Apps → App Store**.
    2. Search for **ESPHome Device Builder** and click **Install**.
    3. Once installed, click **Start**, then **Open Web UI**. The Device Builder will open inside your Home Assistant dashboard.

    !!! info "Already on the new layout"

        The HA app version of Device Builder is already on the new beta backend, so you can skip the backend toggle and browser refresh shown in the desktop tabs.

=== "Linux"

    1. Download the ESPHome Device Builder for Linux. Pick the package that fits your distro.

        - <a href="https://github.com/esphome/esphome-desktop/releases/download/v0.7.0/ESPHome.Builder_0.7.0_amd64.AppImage" target="_blank" rel="noreferrer nofollow noopener">AppImage (works on any distro)</a>
        - <a href="https://github.com/esphome/esphome-desktop/releases/download/v0.7.0/ESPHome.Builder_0.7.0_amd64.deb" target="_blank" rel="noreferrer nofollow noopener">.deb (Debian / Ubuntu)</a>
        - <a href="https://github.com/esphome/esphome-desktop/releases/download/v0.7.0/ESPHome.Builder-0.7.0-1.x86_64.rpm" target="_blank" rel="noreferrer nofollow noopener">.rpm (Fedora / RHEL)</a>

    2. Install or run the file you downloaded.

        - **AppImage:** `chmod +x ESPHome.Builder_0.7.0_amd64.AppImage` then double-click the file, or run it from a terminal.
        - **.deb:** `sudo apt install ./ESPHome.Builder_0.7.0_amd64.deb`
        - **.rpm:** `sudo dnf install ./ESPHome.Builder-0.7.0-1.x86_64.rpm`

    <!-- TODO: add a Linux installer screenshot if available. -->

    3. Once installed, a web browser should launch and navigate to <a href="http://localhost:6052/" target="_blank" rel="noreferrer nofollow noopener">http://localhost:6052/</a>. When you see this page, your ESPHome Device Builder installation is complete.

        - Use a Chromium-based browser such as Chrome or Edge. Firefox does not currently support WebSerial, which is required for the initial USB flash.

    4. Look for the **ESPHome Builder** icon in your system tray or notification area. Its exact location depends on your desktop environment (top bar on GNOME, system tray on KDE, XFCE, or Cinnamon). Click it, hover over **Backend**, and switch from Classic to the ESPHome Builder Beta.

    <!-- TODO: confirm the system tray wording on Linux. -->

    5. Wait at least 30 seconds, then refresh your browser. You should now see the new ESPHome Device Builder Preview.

## Set up your Wi-Fi credentials

ESPHome stores your Wi-Fi name and password centrally so every device you build picks them up automatically. Fill them in once here.

Enter your Wi-Fi network name (SSID) and Wi-Fi password, then click **Save credentials**. The password is case sensitive, so be careful when entering it.

!!! tip "Secrets folder"

    One popular option is to store your encryption keys here. That way, you can share your full YAML with other users without needing to edit and hide your encryption key. See the [using secrets](../tutorials/using-secrets.md) wiki for step by step directions.

![ESPHome Device Builder Secrets editor with wifi_ssid and wifi_password fields filled in](../../../assets/esphome-builder-enter-wifi-credentials.gif)

If you make a mistake or want to change this later, click the 3 dots menu in the top right then select **Secrets**. Click the Eye icon to unhide the Wi-Fi SSID and password, change them, then click **Save** in the bottom right.

!!! success "You're set up"

    You're done with the install guide and ready to build your first device.

## Add a new device

With ESPHome Device Builder installed and your Wi-Fi credentials saved, you can scaffold the starter kit as a new device.

1. Navigate back to the ESPHome Device Builder and click **Add new device** then click **Create new project**.

   ![ESPHome Device Builder Add new device dialog showing Create new project](../../../assets/device-builder-add-new-device.gif)

2. Select the **Apollo ESPHome Starter Kit** and give it a name such as `esphome-starter-kit`, then click **Finish Setup**.

   ![Selecting the Apollo ESPHome Starter Kit and naming the device esphome-starter-kit](../../../assets/device-builder-select-esk-name-it.gif)

Your starter kit now appears as a device card in the Device Builder dashboard, ready for components.

## Configure components

When you create the device, ESPHome Device Builder seeds it with a list of components under **Core configuration**. You'll add three more for this tutorial.

### Accessory power rail

The <a href="https://esphome.io/components/switch/gpio/" target="_blank" rel="noreferrer nofollow noopener">accessory power rail</a> is used behind the scenes to give power to your optional modules including the onboard RGB LED.

1. In the ESPHome Device Builder, navigate to the **Components** section.
2. Click **Add component**.
3. Scroll to **Accessory Power Rail** and click **Add**.
4. Click **Add** once more to confirm.

![Adding the Accessory Power Rail component in ESPHome Device Builder](../../../assets/device-builder-add-accessory-power-rail.gif)

### Web Server component

The <a href="https://esphome.io/components/web_server/" target="_blank" rel="noreferrer nofollow noopener">Web Server</a> broadcasts a local website from your device. That lets you navigate to the device's IP address or hostname (for example <a href="http://esphome-starter-kit.local/" target="_blank" rel="noreferrer nofollow noopener">esphome-starter-kit.local</a>) to control it from any browser on your network.

1. In the ESPHome Device Builder, navigate to the **Core configuration** section.
2. Click **Add component**.
3. Scroll to **Web Server** and click **Add**.
4. Click **Add** once more to confirm.
5. Toggle **Show advanced settings**.
6. Scroll down to **Version** and select **3** from the dropdown.

![Installing the Web Server v3 component in ESPHome Device Builder](../../../assets/device-builder-install-web-server-v3.gif)

### Onboard RGB LED

The onboard RGB LED is a small LED above the Reset button on your ESP32-C6 module. It is great for testing automations and doubles as a status light.

1. In the ESPHome Device Builder, navigate to the **Components** section.
2. Click **Add component**.
3. Scroll to **Onboard RGB LED** and click **Add**.
4. Click **Add** once more to confirm.

![Adding the Onboard RGB LED component in ESPHome Device Builder](../../../assets/device-builder-add-onboard-rgb-led-component.gif)

## Boot mode

The device must be flashed via USB using bootloader mode the very first time it is used. Once you flash it once, you do not have to repeat these steps.

!!! tip "Use a quality USB-C cable and power source"

    ESP32 boards are sensitive to power. If your device keeps restarting, will not be detected, or will not broadcast its hotspot, try a different USB-C cable or a different USB port. A 5V 1A supply is plenty.

1. Hold the sides of the ESP32-C6 and gently push the USB-C cable firmly into the USB-C port. Plug the other end of the USB-C cable into your computer. Be careful not to snap or damage the FPC ribbon cable connectors located on the sides of the device.

   ![Plugging the USB-C cable into the ESP32-C6 main board on the ESPHome Starter Kit](../../../assets/esphome-starter-kit-plug-in-usb-c.webp)

2. Hold down the boot button. While still holding the boot button, press and release the reset button, then release the boot button.

   ![Putting the ESP32-C6 into bootloader mode by holding BOOT and tapping RESET](../../../assets/esphome-starter-kit-boot-mode.webp)

3. Your device is now in boot mode. The board will stay in bootloader mode until you flash it.

## Install firmware

Before you continue, confirm that you have installed ESPHome Device Builder, configured your components, and put your device in boot mode.

1. Click **Save** in the bottom right, which will then show an **Install** button.
2. Click **Install** in the bottom right.
3. Click **Plug into this computer**.
4. Select the COM port, then click **Connect** to connect to the ESP32-C6 module.
5. Wait for the firmware to compile and install. This usually takes two to five minutes.
6. Once it completes, click **Stop**, then press the **Reset** button on your device. Your device will reboot and it is now ready to test.

![ESPHome Device Builder compiling and flashing the initial firmware to the ESP32-C6](../../../assets/device-builder-initial-firmware-install.gif)

!!! tip "Click Show details during the install to watch the compile and flash process"

    It is a great way to see what's happening under the hood.

## Test your LED

Above, you installed the `web_server` component, which lets you navigate to the IP address of your device or to the hostname, for example <a href="http://esphome-starter-kit.local/" target="_blank" rel="noreferrer nofollow noopener">esphome-starter-kit.local</a>.

The page should load and show you the onboard RGB LED. Click the toggle button to make sure the RGB LED turns on and off on your device.

![ESPHome Device Builder Web Server v3 controlling the onboard RGB LED](../../../assets/device-builder-web-server-v3.gif)

Here is the light changing colors.

![Onboard RGB LED on the ESPHome Starter Kit ESP32-C6 cycling through colors](../../../assets/esphome-starter-kit-onboard-rgb-led-light-up.webp)

!!! success "Your starter kit is alive"

    Your ESP32-C6 is on Wi-Fi, in Home Assistant, and serving a web UI you can hit from any browser on your network. From here, every module you add becomes another entity on this same device.

<a href="https://wiki.apolloautomation.com/products/ESPHome-Starter-Kit/start-here/" class="md-button md-button--primary"><img src="/assets/esphome-logo.svg" /> Back - Start Here</a> <a href="../modules/button-module/" class="md-button md-button--primary"><img src="/assets/esphome-logo.svg" /> Next - Add Button Module</a>