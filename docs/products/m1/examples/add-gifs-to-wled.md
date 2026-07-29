---
title: M-1 LED Matrix Adding GIFs to WLED
description: >-
  Step by step guide to adding an animated GIF to the M-1 LED Matrix.
---
# Add GIFs to Your M-1

Find a GIF you like first. <a href="https://giphy.com/" target="_blank" rel="noreferrer nofollow noopener">Giphy</a> is an easy place to start, and the dancing cat below works as a test.

![](/assets/dancing-cat.gif)

Getting it onto the matrix depends on your firmware. WLED converts and resizes on the device, WLED-MM needs an external tool first.

=== "WLED"

    [Pixel Forge](/products/m1/examples/pixel-forge.md) handles the whole job on the device. Upload your GIF, frame it, set the size, and it lands in the effects list ready to run. No external resizing and no manual file upload.

    [Add a GIF with Pixel Forge](/products/m1/examples/pixel-forge.md){: .md-button .md-button--primary }

=== "WLED-MM"

    !!! null "Make sure you are on version 14.5.1 or newer!"

        WLED-MM (WLED MoonModules) firmware version 14.5.1 or higher is required for this! If you need to re-flash your device follow our<a href="https://wiki.apolloautomation.com/products/m1/troubleshooting/m1-reflash/" target="_blank" rel="noreferrer nofollow noopener"> step by step guide here</a>!

    1\. Download your gif - if it is already using a 64x64 width and height then you can skip to step 5. Click on the gif you want and then click **Download**.

    2\. Head to <a href="https://ezgif.com/" target="_blank" rel="noreferrer nofollow noopener">ezgif.com</a> and click **Resize** then click Browse and choose your gif then click Upload!

    ![](/assets/m-1-create-gifs-resize-gifs.gif)

    3\. Set the **Width** to **64** and the **Height** to **64** then click **Resize image** then scroll down to the **Resized Image:** section and click the **Save** icon.

    ![](/assets/m-1-create-gifs-resize-gifs-save.gif)

    4\. Rename the gif to something simple such as cat-dance. We will need to input the name as-is in a future step so renaming it to a simple name is best!

    ![](/assets/m-1-create-gifs-rename-gif.gif)

    5\. Open a web browser and navigate to `http://<your-m1-ip-address>` or `http://<your-device-name>.local`.

    !!! null "If you need help figuring out your hostname you can edit it from the wled wifi settings"

        You can use an app like "wled-native" on iOS to auto-discover your WLED devices and then go into wifi settings to see your IP and hostname! <a href="https://wiki.apolloautomation.com/products/m1/troubleshooting/m1-find-ip-address-and-hostname/" target="_blank" rel="noreferrer nofollow noopener">Here's a step-by-step guide</a>.

    6\. Click **Config**, then scroll down and click **File System** then click **Browse** and select the resized and renamed gif we just created then click **Save**.

    ![](/assets/m-1-create-gifs-upload-gif-to-wled.gif)

    7\. Click the back button on your browser and navigate back to the main page of the M-1 WLED interface. Click in the search bar and type in **image** and select it.

    ![](/assets/m-1-create-gifs-select-image-effect.gif)

    8\. Click the **arrow** next to Segment 0 and then click the pencil icon to edit the name. Type in the name exactly as you did in step 4 above such as cat-dance.gif

    ![](/assets/m-1-create-gifs-enter-gif-name-as-segment-name.gif)

    9\. Click on **\+ Preset** and write in any name you want such as Cat Dance then click **Save**.

    ![](/assets/m-1-create-gifs-save-gif-as-preset.gif)

    10\. To have the M-1 boot straight into this gif, head to **Config** then **LED Preferences** and scroll down until you see **Apply Preset** and put in your preset number for the effect you just made. If this is your first one then put in 1 and then click **Save**.

    ![](/assets/m-1-create-gifs-set-preset-as-boot.gif)

    !!! warning "Use a browser, not the WLED phone app"

        The app's file picker greys out image files, so uploading a GIF from it does not work. That is a bug in the app rather than anything on the M-1. Open the device in any browser instead.

    GIFs live on the M-1 itself and the space is limited. Delete images you are not using from **Config**, then **File System**.
