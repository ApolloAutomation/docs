---
title: M-1 LED Matrix - Multiple Panel Setup
description: Tutorial for wiring and configuring multiple panels with your M-1 LED Matrix.
---
# M-1 LED Matrix - Multiple Panels

!!! info "Prerequisites needed for multiple panels"

    To use multiple panels you will need one M-1 LED Matrix Controller, at least two M-1 Matrix panels with a maximum of four, at least one of the data cables with a max of three, and at least one of the Power Modules (with a max of three). You will also need up to four usb-c cables to power each panel including the usb-c of the m-1 led matrix which will power the panel it is connected to.

Choose the number of panels you are using below to get started!

###### Hardware Setup

=== "Two Panels"

    1\. Set both of your M-1 panels face down - the M-1 controller panel should be on the far left. Start by connecting the data cable (ribbon cable) to the "JOUT" port on the far left panel into the "JIN" port on the second panel.

    ![](../../../assets/two-panels-connect-data-cable.webp)

    2\. Gently press the Matrix Power Module over the 4 pin header on the second panel as shown below. Make sure the USB-C port is facing to the right!

    ![](../../../assets/two-panels-connect-power-module.webp)

    3\. Plug in the USB-C cable into the M-1 LED Controller and the second Panel.

    ![](../../../assets/two-panels-connect-usb-c.webp)

=== "Three Panels"

    1\. Set all three of your M-1 panels face down - the M-1 controller panel should be on the far left. Start by connecting the data cable (ribbon cable) to the "JOUT" port on the far left panel into the "JIN" port on the second panel. Repeat for connecting the third panel.

    ![](../../../assets/three-panels-connect-data-cable.webp)

    2\. Gently press the Matrix Power Module over the 4 pin header on the second panel as shown below. Make sure the USB-C port is facing to the right! Repeat for connecting the third panel.

    ![](../../../assets/three-panels-connect-power-module.webp)

    3\. Plug in the USB-C cable into the M-1 LED Controller, the second panel power module, and the third panel power module.

    ![](../../../assets/three-modules-connect-usb-c.webp)

=== "Four Panels"

    1\. Set all four of your M-1 panels face down - the M-1 controller panel should be on the far left. Start by connecting the data cable (ribbon cable) to the "JOUT" port on the far left panel into the "JIN" port on the second panel. Repeat for connecting the third and fourth panel.

    ![](../../../assets/four-panels-connect-data-cable.webp)

    2\. Gently press the Matrix Power Module over the 4 pin header on the second panel as shown below. Make sure the USB-C port is facing to the right! Repeat for connecting the third and fourth panels.

    ![](../../../assets/four-panels-connect-power-module.webp)

    3\. Plug in the USB-C cable into the M-1 LED Controller and all three additional panels via the power module USB-C port.

    ![](../../../assets/four-panels-connect-usb-c.webp)

###### Software Setup

=== "Two Panels"

    1\. Navigate to your WLED instance in a browser or using the WLED-native app on your phone. You can use http://your-hostname-here.local or its IP address. <a href="https://wiki.apolloautomation.com/products/m1/troubleshooting/m1-find-ip-address-and-hostname/" target="_blank" rel="noreferrer nofollow noopener">Click here if you need to find your IP or hostname</a>.

    2\. Click on **Config**, then **LED Preferences**. set **Chain Length** to **2** then **Save**.

    ![](../../../assets/chain-length-2-gif.gif)

    3\. Click on **Config**, then **2D Configuration** and change the **Panel Dimensions** to **128 x 64** and click **Save**.

    ![](../../../assets/2d-config-128-width.gif)

    4\. Reboot WLED before proceeding. Tap **Info** at the top, scroll down, and select **Reboot WLED**. When prompted, tap again to confirm the reboot.

    ![](../../../assets/reboot-wled-gif.gif)

=== "Three Panels"

    1\. Navigate to your WLED instance in a browser or using the WLED-native app on your phone. You can use http://your-hostname-here.local or its IP address. <a href="https://wiki.apolloautomation.com/products/m1/troubleshooting/m1-find-ip-address-and-hostname/" target="_blank" rel="noreferrer nofollow noopener">Click here if you need to find your IP or hostname</a>.

    2\. Click on **Config**, then **LED Preferences**. set **Chain Length** to **3** then **Save**.

    ![](../../../assets/chain-length-3-gif.gif)

    3\. Click on **Config**, then **2D Configuration** and change the **Panel Dimensions** to **192 x 64** and click **Save**.

    ![](../../../assets/2d-config-192-width.gif)

    4\. Reboot WLED before proceeding. Tap **Info** at the top, scroll down, and select **Reboot WLED**. When prompted, tap again to confirm the reboot.

    ![](../../../assets/reboot-wled-gif.gif)

=== "Four Panels"

    1\. Navigate to your WLED instance in a browser or using the WLED-native app on your phone. You can use http://your-hostname-here.local or its IP address. <a href="https://wiki.apolloautomation.com/products/m1/troubleshooting/m1-find-ip-address-and-hostname/" target="_blank" rel="noreferrer nofollow noopener">Click here if you need to find your IP or hostname</a>.

    2\. Click on **Config**, then **LED Preferences**. set **Chain Length** to **4** then **Save**.

    ![](../../../assets/chain-length-4-gif.gif)

    3\. Click on **Config**, then **2D Configuration** and change the **Panel Dimensions** to **256 x 64** and click **Save**.

    ![](../../../assets/2d-config-256-width.gif)

    4\. Reboot WLED before proceeding. Tap **Info** at the top, scroll down, and select **Reboot WLED**. When prompted, tap again to confirm the reboot.

    ![](../../../assets/reboot-wled-gif.gif)