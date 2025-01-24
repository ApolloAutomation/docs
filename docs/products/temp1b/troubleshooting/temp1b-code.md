If your device becomes unresponsive and you've exhausted the other troubleshooting methods you can reflash the factory firmware by following the below guide. This needs to be done in Chrome, Edge, or another Chromium based browser.

If your device has already been connected to Home Assistant please delete it from the ESPHome integration and the ESPHome Device Builder before continuing.

1\. <a href="https://wiki.apolloautomation.com/products/temp1b/troubleshooting/temp1b-boot-mode/" target="_blank" rel="noopener">Put your device in boot mode</a> by holding down the boot button and then plugging in the USB cable.

2\. Navigate to our installer page and click connect under Battery Firmware [Apollo TEMP-1 Installer](https://apolloautomation.github.io/TEMP-1/)

!!! failure "Remove the battery!"

    This will not work properly if the battery is still supplying power to the TEMP-1B. Please remove the battery if you are having issues!

3\. Select the open com port then click Connect.

![](assets/troubleshooting/temp-1b-reflash-pic-2-1.png)

4\. Click "Install ApolloAutomation.TEMP-1B".

![](assets/troubleshooting/temp-1b-reflash-pic-3.png)

5\. Click "INSTALL".

![](assets/troubleshooting/temp-1b-reflash-pic-4.png)

6\. Once you see "Installation complete!" you are finished. Click Next then close out of the browser window.

![](assets/troubleshooting/temp-1b-reflash-pic-7.png)

7\. Please <a href="https://wiki.apolloautomation.com/products/general/setup/getting-started/" target="_blank" rel="noopener">proceed to the getting started guide</a> and setup your sensor as a new device!