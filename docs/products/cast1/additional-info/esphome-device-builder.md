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

    1. Open <a href="https://desktop.esphome.io/" target="_blank" rel="noreferrer nofollow noopener">desktop.esphome.io</a> and click **Download installer** under the **Windows** tab.
    2. Open the installer and click **Next** then click **Next** again to start the installation process. Once it shows completed, click **Next** again then **Finish** to complete the installation.

    !!! warning "You may see Windows prompts during install"

        - If Windows shows a blue **Windows protected your PC** warning, click **More info → Run anyway** to continue.
        - If **Windows Security** asks whether to allow public and private networks to access Python, click **Allow**.
        - If the installer fails or the Device Builder can't compile firmware, install **Git for Windows** from <a href="https://gitforwindows.org/" target="_blank" rel="noreferrer nofollow noopener">gitforwindows.org</a> and try again. Future installer builds will bundle this for you.

    ![](/assets/esphome-builder-install-windows.gif)

    Once installed, a web browser should launch and navigate to <a href="http://localhost:6052/" target="_blank" rel="noreferrer nofollow noopener">http://localhost:6052/</a>. On first launch, ESPHome Device Builder asks how you will use it. Select **Build and manage devices**, then select **New to ESPHome** and click **Finish**.

    ![](/assets/device-builder-first-time-install-pick-your-experience.gif)

=== "Mac"

    1. Open <a href="https://desktop.esphome.io/" target="_blank" rel="noreferrer nofollow noopener">desktop.esphome.io</a>. The page detects your OS and shows the macOS downloads. Pick the build that matches your chip:

        - **Apple Silicon** (M1, M2, M3, M4, M5)
        - **Intel Mac**

    2. Open the `.dmg` and drag **ESPHome Builder** into your Applications folder. Launch it from Applications or Spotlight.

        - On first launch, macOS may block the app with a Gatekeeper warning. If that happens, right-click the app in Applications and choose **Open**, then click **Open** in the confirmation dialog. After the first launch, double-click will work normally.

    Once installed, a web browser should launch and navigate to <a href="http://localhost:6052/" target="_blank" rel="noreferrer nofollow noopener">http://localhost:6052/</a>. On first launch, ESPHome Device Builder asks how you will use it. Select **Build and manage devices**, then select **New to ESPHome** and click **Finish**.

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

    1.  Open <a href="https://desktop.esphome.io/" target="_blank" rel="noreferrer nofollow noopener">desktop.esphome.io</a>. The page opens on the **Linux** tab and shows **Download .deb** as the default. Click **Download .deb** to grab the Debian / Ubuntu package.

        If your distro fits a different format, switch to the matching tab on the download page first:

        - **Fedora / RHEL** → downloads a `.rpm`
        - **Arch (AUR)** → opens the AUR package page
        - **AppImage** → downloads a portable AppImage that runs on any distro

    2.  Install the package. Pick the workflow you're more comfortable with:

        === "GUI"

            Works for the `.deb` download. Skip to the CLI tab if you grabbed a `.rpm`, AUR package, or AppImage.

            1.  Open your **Downloads** folder in your file manager.
            2.  Right-click the `ESPHome.Builder_*.deb` file and choose **Open with → Archive Manager** (or whichever archive viewer your distro ships).
            3.  In the archive viewer, click **Extract** and pick a folder you can find again, like `~/esphome-desktop`.
            4.  Open the extracted folder, then navigate into **`usr`** → **`bin`**.
            5.  Double-click **`esphome-desktop`** to launch the app.

            ![](/assets/esphome-device-builder-linux-install.gif)

        === "CLI"

            From a terminal, run the installer that matches the file you downloaded:

            - **.deb (Debian / Ubuntu):** `sudo apt install ./ESPHome.Builder_*.deb`
            - **.rpm (Fedora / RHEL):** `sudo dnf install ./ESPHome.Builder*.rpm`
            - **AppImage (any distro):** `chmod +x ESPHome.Builder_*.AppImage` then double-click the file, or run it from a terminal.

    Once installed, a web browser should launch and navigate to <a href="http://localhost:6052/" target="_blank" rel="noreferrer nofollow noopener">http://localhost:6052/</a>. On first launch, ESPHome Device Builder asks how you will use it. Select **Build and manage devices**, then select **New to ESPHome** and click **Finish**.

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

