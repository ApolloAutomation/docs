---
title: M-1 LED Matrix Creating Your Own GIF
description: Step by step guide to adding a GIF to the M-1 LED Matrix!
---
1. Make sure you know your Apollo M-1 board revision (look on the back of the controller), Rev 4 or Rev 6, and are on firmware version 14.5.1. You can flash your device [here](https://wiki.apolloautomation.com/products/m1/troubleshooting/m1-reflash/). Also, make sure you have the correct LED matrix settings [here](https://wiki.apolloautomation.com/products/m1/setup/m1-matrix-settings/).
2. Connect to the Apollo M-1 Wi-Fi hot spot and it should take you directly to the main dashboard. Then select Config.
3. ![](../../../assets/products-m1-examples-config.png)
4. Select Wi-Fi Setup.

   ![](../../../assets/products-m1-examples-wifi.png)

5. Add your M-1 to your Wi-Fi network by selecting Scan and adding your Wi-Fi credentials.

   ![](../../../assets/products-m1-examples-ssid.png)

6. Now you can grab the IP address of the M-1 from your router which should be labeled esp32s3 or you can use the WLED Native app to automatically find the device. (Download here: [Android](https://play.google.com/store/apps/details?id=ca.cgagnier.wlednativeandroid&amp;hl=en_US) / [Apple](https://apps.apple.com/us/app/wled-native/id6446207239))

   ![](../../../assets/products-m1-examples-esp.png)

7. Copy the IP address and paste it into the URL bar of your browser. This will take you to the Apollo M-1 dashboard.

   ![](../../../assets/products-m1-examples-ip.png)

8. Now find your GIF of choice and save it to your computer.

   ![](../../../assets/products-m1-examples-gsd.gif)

9. Now we need to go to [https://ezgif.com/](https://ezgif.com/) and select Resize.

   ![](../../../assets/products-m1-examples-resize.png)

10. Select Browse and Upload your GIF.

    ![](../../../assets/products-m1-examples-upload-gif.png)

11. Change the Width and Height to 64x64, select resize and save the GIF (use an easy name since we will be using it later).

    ![](../../../assets/products-m1-examples-64x64-1.png)

12. Now go back to the Apollo M-1 IP address and select config.

    ![](../../../assets/products-m1-examples-config-1.png)

13. Select File System.

    ![](../../../assets/products-m1-examples-file-system.png)

14. Select Browse, choose your GIF and then select Upload.

    ![](../../../assets/products-m1-examples-upload.png)

15. Now go back to your Apollo M-1 IP address, select the Image effect, use the pencil to rename the effect EXACTLY the same as your GIF file (example: gsd.gif) and select the check mark to save it.

    ![](../../../assets/products-m1-examples-image-8.png)

16. Now you should see your GIF playing on the Apollo M-1!

    ![](../../../assets/products-m1-examples-panel.png)

17. Not finished yet though! Select Preset, type in a name and save it to the device.

    ![](../../../assets/products-m1-examples-save.png)

18. Now you can play it whenever you would like and you can even set it as the boot effect (Config &gt; LED Preferences &gt; Change Apply Preset to the preset number you just made).

    ![](../../../assets/products-m1-examples-boot.png)

    &nbsp;

    &nbsp;