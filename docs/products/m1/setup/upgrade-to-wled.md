---
title: Migrate to WLED
description: Move an M-1 from WLED-MM 14.5.1 to WLED 16.0.1 over the air, keeping your settings.
---
# Migrate to WLED

M-1 units shipped before the firmware switch run WLED-MM 14.5.1. You can move to WLED 16.0.1 over the air without a USB cable, and because the partition layout is unchanged, your Wi-Fi credentials, presets, and uploaded files survive the update.

Take a backup anyway. It takes a minute, and it is the difference between a five minute recovery and rebuilding every preset by hand if the update goes sideways.

!!! warning "Rev6 controllers only"

    WLED 16.0.1 is built for the Rev6 M-1 controller. The revision is printed on the back of the board. On a Rev4, stay on [WLED-MM 14.5.1](/products/m1/setup/getting-started-m1.md).

1\. Back up first. Open your M-1 in a browser, click **Config**, then **Security & Updates**, and under **Backup & Restore** download both your presets and your configuration. Keep the two files somewhere safe.

2\. Download **M-1_ota.bin** from the latest release on <a href="https://github.com/ApolloAutomation/WLED-M1/releases" target="_blank" rel="noreferrer nofollow noopener">ApolloAutomation/WLED-M1</a>. Take the OTA image, not the full install image.

3\. Back on the **Security & Updates** page, find **Manual OTA Update**, click **Browse**, pick `M-1_ota.bin`, and click **Update!**.

4\. Wait for the device to finish and reboot on its own. Do not pull power partway through.

5\. Tap **Info** and confirm the version now reads 16.0.1.

###### After the Upgrade

Check **Config** then **LED Preferences**. The HUB75 section in WLED 16 describes panels as a grid rather than a chain length, so an existing multi-panel setup may need its **No. of Panels** and grid values set. [Matrix Settings](/products/m1/setup/m1-matrix-settings.md) covers a single panel and [Multiple Panels](/products/m1/setup/m1-multiple-panels.md) covers the rest.

The display stays black after a HUB75 change until you reboot.

Your old presets still exist, but presets that referenced MoonModules-only effects will fall back to something else, since those effects do not exist in stock WLED.

If the upgrade leaves the device unresponsive, a [factory re-flash](/products/m1/troubleshooting/m1-reflash.md) over USB puts it back to a known state. That wipes everything, which is where your backup earns its keep: restore the presets file from **Config**, then **Security & Updates**, under **Backup & Restore**.

Restore the presets file rather than the configuration file. The config backup describes WLED-MM's settings, and it is worth keeping in case you ever go back to 14.5.1, but pushing it onto WLED can leave you with panel settings that do not match this firmware.
