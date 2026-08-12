---
title: ESPHome Device Builder
description: Optional. Use ESPHome Device Builder to rename your CAST-1 or edit its YAML.
---
# ESPHome Device Builder

!!! tip "Most people don't need this"

    Your CAST-1 ships ready to use. You only need the ESPHome Device Builder if you want to rename it or make manual edits to its YAML. To just add your CAST-1 to Home Assistant, follow the [Getting Started guide](https://wiki.apolloautomation.com/products/cast1/setup/getting-started/#add-to-home-assistant).

ESPHome Device Builder is the software that gives you a user interface for editing, compiling, and flashing ESPHome YAML. You'll use it to take control of your CAST-1 and edit its configuration.

### Install ESPHome Device Builder

Pick the platform you'll be running ESPHome Device Builder on:

=== "Windows"

    1. Open <a href="https://esphome.io/install/" target="_blank" rel="noreferrer nofollow noopener">esphome.io/install</a> and click **Download installer (.exe)** on the **Windows** tab.
    2. Open the downloaded `.exe` file. If Windows asks whether to allow the app to make changes, choose **Yes**, then follow the installer prompts.
    3. On the last screen, leave **Run ESPHome Device Builder** checked and click **Finish**.
    4. When **Allow network pairing** appears, click **Allow access**. Windows then asks for administrator approval and shows its own firewall prompt for the Python backend. Allow that one too, or other ESPHome dashboards on your network won't be able to reach this computer.

    !!! warning "If Windows blocks the installer"

        If a blue **Windows protected your PC** warning appears when you open the `.exe`, click **More info → Run anyway** to continue.

    ![](/assets/esphome-builder-install-windows.gif)

    The first launch takes a moment while it sets itself up, then the dashboard opens in your browser at <a href="http://localhost:6052/" target="_blank" rel="noreferrer nofollow noopener">http://localhost:6052/</a>. An ESPHome icon lands in your notification area for getting back to it later.

    A short wizard runs the first time:

    1. Click **Continue** on the welcome screen.
    2. Choose **Installation of the ESPHome Device Builder**, since you're building on this computer.
    3. Choose **New to ESPHome** for the simpler, guided interface.

    Then take **Start guided tour** for a five minute walkthrough, or **Maybe later**.

    ![](/assets/device-builder-first-time-install-pick-your-experience.gif)

=== "Mac"

    1.  Open <a href="https://esphome.io/install/" target="_blank" rel="noreferrer nofollow noopener">esphome.io/install</a>. The page detects your OS and opens the **macOS** tab. Pick the build that matches your chip:

        - **Apple Silicon** (M1, M2, M3, M4, M5)
        - **Intel**

        Not sure which you have? Click the Apple menu → **About This Mac**.

    2.  Open the `.dmg` and drag **ESPHome Device Builder** into your Applications folder.

    3.  Open your Applications folder and double-click **ESPHome Device Builder**. The first time you run it, macOS may ask you to confirm. Click **Open**.

        - If macOS blocks it outright with a Gatekeeper warning instead, right-click the app in Applications and choose **Open**, then click **Open** in the confirmation dialog. After that, double-click works normally.

    The first launch takes a moment while it sets itself up, then the dashboard opens in your browser at <a href="http://localhost:6052/" target="_blank" rel="noreferrer nofollow noopener">http://localhost:6052/</a>. An ESPHome icon lands in your menu bar for getting back to it later.

    A short wizard runs the first time:

    1. Click **Continue** on the welcome screen.
    2. Choose **Installation of the ESPHome Device Builder**, since you're building on this computer.
    3. Choose **New to ESPHome** for the simpler, guided interface.

    Then take **Start guided tour** for a five minute walkthrough, or **Maybe later**.

    ![](/assets/device-builder-first-time-install-pick-your-experience.gif)

=== "Home Assistant App"

    The ESPHome Device Builder runs as a Home Assistant app served right inside your existing HA dashboard. This is the easiest option if you already run Home Assistant OS or a supervised install.

    **<u>Method 1</u>**

    To add the **ESPHome Device Builder** to your Home Assistant instance, use this My button:

    <a href="https://my.home-assistant.io/redirect/supervisor_addon/?addon=5c53de3b_esphome&repository_url=https%3A%2F%2Fgithub.com%2Fesphome%2Fhome-assistant-addon" target="_blank" rel="noreferrer noopener"><img src="https://my.home-assistant.io/badges/supervisor_addon.svg" alt="Open your Home Assistant instance and start setting up a new app."></a>

    **<u>Method 2</u>**

    1. In Home Assistant, open **Settings → Apps → App Store**.
    2. Search for **ESPHome Device Builder** and click **Install**.
    3. Once installed, click **Start**, then **Open Web UI**. The Device Builder will open inside your Home Assistant dashboard.

=== "Linux"

    1.  Open <a href="https://esphome.io/install/" target="_blank" rel="noreferrer nofollow noopener">esphome.io/install</a>. The page opens on the **Linux** tab with **Debian / Ubuntu** selected. Choose the package format your distro uses, then the CPU architecture (**x86_64** for a normal desktop or laptop, **arm64** for a Raspberry Pi or similar board):

        - **Debian / Ubuntu** → downloads a `.deb`
        - **Fedora / openSUSE** → downloads a `.rpm`
        - **Arch (AUR)** → installs the `esphome-desktop-bin` package
        - **AppImage** → a portable build that runs on any distro

    2.  Install it. Double-click the downloaded `.deb` or `.rpm` in your file manager, or run the matching command in a terminal:

        - **Debian / Ubuntu:** `sudo apt install ./ESPHome.Device.Builder_*.deb`
        - **Fedora / openSUSE:** `sudo dnf install ./ESPHome.Device.Builder-*.rpm`
        - **Arch:** `yay -S esphome-desktop-bin`
        - **AppImage:** `chmod +x ESPHome.Device.Builder_*.AppImage` then run `./ESPHome.Device.Builder_*.AppImage`

    3.  Launch **ESPHome Device Builder** from your applications menu.

        If your CAST-1 doesn't appear as a serial port later, add your user to the `dialout` group with `sudo usermod -a -G dialout $USER`, then log out and back in.

    The first launch takes a moment while it sets itself up, then the dashboard opens in your browser at <a href="http://localhost:6052/" target="_blank" rel="noreferrer nofollow noopener">http://localhost:6052/</a>. An ESPHome icon lands in your system tray for getting back to it later. Some Linux desktops, notably GNOME without a tray extension, don't show tray icons at all. The app still runs, so just use the dashboard in your browser.

    A short wizard runs the first time:

    1. Click **Continue** on the welcome screen.
    2. Choose **Installation of the ESPHome Device Builder**, since you're building on this computer.
    3. Choose **New to ESPHome** for the simpler, guided interface.

    Then take **Start guided tour** for a five minute walkthrough, or **Maybe later**.

    ![](/assets/device-builder-first-time-install-pick-your-experience.gif)

### Take Control of Your CAST-1

1\. Open the ESPHome Device Builder.

<a href="https://my.home-assistant.io/redirect/supervisor_addon/?addon=5c53de3b_esphome" target="_blank" rel="noreferrer noopener"><img src="https://my.home-assistant.io/badges/supervisor_addon.svg" alt="Open your Home Assistant instance and show the dashboard of a Supervisor add-on."></a>

2\. Click **Show** next to **Discovered** at the top, then click **Take Control** next to your CAST-1. Change the **Name** and **Friendly Name** if you'd like, or leave them, then click **Take Control** again.

![](/assets/cast-1-esphome-device-builder.gif)

3\. Click **Install** (the up arrow icon), then click **On the network** and watch it finish installing. (1)
{ .annotate }

1.  This takes 5 to 10 minutes depending on how fast your device is.

![](/assets/cast-1-esphome-device-builder-install.gif)

4\. Once it completes, click **Stop**, then press the **Reset** button on your device. Your CAST-1 will reboot and it's now ready to test out!

!!! success "You're all set!"

    Your CAST-1 is now adopted into the ESPHome Device Builder, where you can rename it or edit its YAML.

