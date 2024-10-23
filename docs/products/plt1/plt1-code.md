# Manually Uploading Code Through ESPHome

If your device becomes unresponsive and you've exhausted the other troubleshooting methods you can upload a fresh set of firmware by following the below guide. The utility does need to be run from Chrome or Edge.

If your device has already been connected to Home Assistant previously please refer to Removing Device From Home Assistant first before proceeding

1. Plug your sensor into your computer with a quality USB-C cable that supports data transfer
2. Navigate to our installer page and click connect [\*\* Install Page \*\*](https://apolloautomation.github.io/PLT-1/)
3. Select your Apollo device, it will show with a similar name to the one below, and click connect. If you aren't sure which device it is, you can unplug the sensor and see which disappears.

[![ComSelection.png](https://apolloautomation.github.io/docs/products/mtr1/assets/comselection.png)](https://apolloautomation.github.io/docs/products/mtr1/assets/comselection.png)

If no device shows, click cancel and then install the recommended driver that shows on the popup. If you have installed the driver, tried different cables, and it still won't work refer here for putting the sensor in bootloader mode and then retry step 3. Putting sensor In Boot Mode Document

4\. Choose to install the new firmware

[![](https://apolloautomation.github.io/docs/products/mtr1/assets/image-1698806750134.png)](https://apolloautomation.github.io/docs/products/mtr1/assets/image-1698806750134.png)

5\. Wait for the installer to finish - if you see "ERROR Logger is not configured!" that is totally expected! The logger is disabled to make more room for other components on the microcontroller.

[![](https://apolloautomation.github.io/docs/products/mtr1/assets/image-1698806082666.png)](https://apolloautomation.github.io/docs/products/mtr1/assets/image-1698806082666.png)

6\. VERY IMPORTANT - you need to unplug your device and plug it back in to leave boot mode!

1. After finishing, check for the Apollo hotspot and connect. This might not show if you previously had the MTR-1 connected to your wifi
2. Log into Home Assistant and go to the ESPHome addon check to see if you can adopt the device.

If you encounter the below error, please complete the Putting MTR-1 In Boot Mode Document and go back to step 3.

[![](https://apolloautomation.github.io/docs/products/mtr1/assets/image-1698806793309.png)](https://apolloautomation.github.io/docs/products/mtr1/assets/image-1698806793309.png)