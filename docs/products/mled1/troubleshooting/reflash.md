---
title: Update or reflash the MLED-1
description: Update your Apollo MLED-1 to the latest firmware, or reflash it from scratch, with the Apollo installer in your browser.
---
# Update or reflash the MLED-1

The Apollo installer puts the latest MLED-1 firmware on your device over USB. Use it to update to a new release and keep your settings, or to start fresh if your MLED-1 isn't behaving.

!!! note "Before you start"

    You need a computer with Chrome or Edge, and a USB cable that carries data, not only power.

!!! tip "WLED's update button can't fetch MLED-1 builds yet"

    WLED's own update button can't fetch Apollo's MLED-1 builds yet. The Apollo installer always has the latest one.

1\. Plug the MLED-1 into your computer with a USB data cable.

2\. Open the [Apollo installer for the MLED-1](https://install.apolloautomation.com/#/mled-1) and click **Connect & Install**.

3\. Pick the MLED-1's serial port in the browser popup and click **Connect**.

4\. Click **Install Apollo MLED-1**.

5\. When the installer asks whether to erase the device, choose what you want to keep:

- Leave **Erase device** unticked to keep your Wi-Fi, LED settings, and presets.
- Tick **Erase device** to wipe everything and start fresh.

6\. Click **Next**, then **Install**, and keep the page visible until you see **Installation complete!**.

If you kept your settings, the MLED-1 rejoins your Wi-Fi and Home Assistant on its own. If you erased it, set it up again from [getting started](../setup/getting-started.md#connect-to-your-network).

!!! tip "Want the firmware files?"

    Each release on [GitHub](https://github.com/ApolloAutomation/MLED-1/releases) carries `MLED-1_full_install.bin`, a full image you flash at offset 0x0, and an update file for WLED's manual upload.

Still stuck? Reach out on [Discord](https://link.apolloautomation.com/discord) or at support@apolloautomation.com so we can help.
