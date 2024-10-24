# Manually Uploading Code Through ESPHome

If your device becomes unresponsive and you've exhausted the other troubleshooting methods you can upload a fresh set of firmware by following the below guide. The utility does need to be run from Chrome or Edge.

If your device has already been connected to Home Assistant previously please refer to Removing Device From Home Assistant first before proceeding

1. Plug your MTR-1 into your computer with a quality USB-C cable that supports data transfer
2. Navigate to our installer page and click connect [\*\* Install Page \*\*](https://apolloautomation.github.io/MTR-1/)
3. Select your Apollo device, it will show with a similar name to the one below, and click connect. If you aren't sure which device it is, you can unplug the MTR-1 and see which disappears.

![ComSelection.png](../assets/comselection.png)

If no device shows, click cancel and then install the recommended driver that shows on the popup. If you have installed the driver, tried different cables, and it still won't work refer here for putting the MTR-1 in bootloader mode and then retry step 3. Putting MTR-1 In Boot Mode Document

4. Choose to install the new firmware

![](../assets/image-1698806750134.png)

6. Wait for the installer to finish - if you see "ERROR Logger is not configured!" that is totally expected! The logger is disabled to make more room for other components on the microcontroller.

![](../assets/image-1698806082666.png)

7\.VERY IMPORTANT - you need to unplug your device and plug it back in to leave boot mode!

8. After finishing, check for the Apollo hotspot and connect. This might not show if you previously had the MTR-1 connected to your wifi
9. Log into Home Assistant and go to the ESPHome addon check to see if you can adopt the device.

If you encounter the below error, please complete the Putting MTR-1 In Boot Mode Document and go back to step 3.

![](../assets/image-1698806793309.png)