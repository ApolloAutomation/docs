---
title: M-1 LED Matrix Creating Your Own GIF
description: Step by step guide to adding a GIF to the M-1 LED Matrix!
---
1. Make sure you know your Apollo M-1 board revision (look on the back of the controller), Rev 4 or Rev 6, and are on firmware version 14.5.1. You can flash your device [here](https://wiki.apolloautomation.com/products/m1/troubleshooting/m1-reflash/).
2. Select Config
3. ![](../../../assets/config.png)
4. Select Wi-Fi Setup

   ![](../../../assets/wifi.png)

5. Add your M-1 to your Wi-Fi network by selecting Scan and adding your Wi-Fi credentials

   ![](../../../assets/ssid.png)

6. Now you can grab the IP address of the M-1 from your router which should be labeled esp32s3

   ![](../../../assets/esp.png)

7. Copy the IP address and paste it into the URL bar of your browser

   ![](../../../assets/ip.png)

8. Now find your GIFof choice

   ![](../../../assets/gsd.gif)

9. Now we need to go to [https://ezgif.com/](https://ezgif.com/) and select Resize

   ![](../../../assets/resize.png)

10. Select Browse and Upload your GIF

    ![](../../../assets/upload-gif.png)

11. Change the Width and Height to 64x64, select resize and save the GIF (use an easy name since we will be using it later)

    ![](../../../assets/64x64-1.png)

12. Now go back to the Apollo M-1 IP address and select config

    ![](../../../assets/config-1.png)

13. Select File System

    ![](../../../assets/file-system.png)

14. Select Browse, choose your GIF and then select Upload

    ![](../../../assets/upload.png)

15. Now go back to your Apollo M-1 IP address, select the Image effect, use the pencil to rename the effect EXACTLY the same as your GIF (example: gsd.gif) and select the check mark to save it

    ![](../../../assets/image-8.png)

16. Now you should see your GIF playing on the Apollo M-1!

    ![](../../../assets/panel.png)

17. Not finished yet though! Select Preset, type in a name and save it to the device

    ![](../../../assets/save.png)

18. Now you can play it whenever you would like and you can even set it as the boot effect (Config &gt; LED Preferences &gt; Change Apply Preset to the preset number you just made)

    ![](../../../assets/boot.png)

    &nbsp;

    &nbsp;