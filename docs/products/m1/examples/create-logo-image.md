---
title: M-1 LED Matrix Creating Your Own Image
description: Step by step guide to adding your own logo or image to the M-1 LED Matrix!
---
# Create your own image for the M-1

1\. <a href="https://github.com/ApolloAutomation/PixelMagicTool/blob/main/pxmagic.htm" target="_blank" rel="noreferrer nofollow noopener">Click this link</a> and then click "Download raw file" as shown below.

![](../../../assets/m-1-download-raw-file.png)

2\. Double click the pxmagic.htm file you just downloaded and it will launch in a browser such as Firefox.

![](../../../assets/pixelmagictool-point-to-file.png)

3\. Fill in the IP address or the hostname.local such as apollo-led-matrix.local

![](../../../assets/pixelmagictool-hostname.png)

!!! tip "If you need help figuring out your hostname you can edit it from the wled wifi settings"

    You can use an app like "wled-native" on iOS to auto-discover your WLED devices and then go into wifi settings to see your IP and hostname!

4\. Fill in a Preset Name such as "Apollo Logo".

![](../../../assets/pixelmagictool-preset-name.png)

5\. Slide the brightness slider to 255 if you want it to be full brightness!

![](../../../assets/pixelmagictool-full-brightness.png)

6\. Click Select image and navigate to the image or logo you want and select it.

![](../../../assets/pixelmagictool-select-image.png)

7\. Click Generate and you should now see a preview of your image.

![](../../../assets/pixelmagictool-generate-image.png)

8\. Click Save and you should see a notification in the bottom right confirming that your preset was saved successfully!

![](../../../assets/pixelmagictool-save-image-to-m-1.png)

9\. Your preset is now live on your device. You might need to refresh the browser to see it. You also will need to "reload" the WLED integration in Home Assistant for your device for new presets to show up!

![](../../../assets/m-1-apollo-logo-example-preset.jpeg)