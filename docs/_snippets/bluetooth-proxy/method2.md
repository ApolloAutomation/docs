1\. Open the Esphome Device Builder.

![](/assets/bluetooth-proxy-tutorial-1.png)

2\. If you do not have it installed, [go here](https://esphome.io/guides/getting_started_hassio.html#installing-esphome-device-compiler "Install Esphome Device Builder.") and then move on to step 3.

3\. Click "Edit" as shown below.

![](/assets/bluetooth-proxy-tutorial-2.png)

4\. Copy the code inside the codeblock below.

```yaml
  power_save_mode: LIGHT
```

5\. Paste the code as shown below - make sure the spaces look the same and there are no red lines under any of the code.<br>![](/assets/bluetooth-proxy-tutorial-5.png)

6\. Copy the code inside the codeblock below.

```yaml
bluetooth_proxy:
  active: true
esp32_ble_tracker:
  scan_parameters:
    active: false
```

7\. Paste the code on a new line at the very bottom of the file as shown below.

![](/assets/bluetooth-proxy-tutorial-7-1.png)

8\. Click save then Install in the top right.

![](/assets/bluetooth-proxy-tutorial-8.png)

9\. Click "Wirelessly" and let it finish compiling then installing.

![](/assets/bluetooth-proxy-tutorial-6.png)

10\. When you see this "OTA Successful" it has finished and you can click "Close" in the bottom right.

![](/assets/bluetooth-proxy-tutorial-7.png)

11\. You are finished and your Apollo device is now acting as a Bluetooth Proxy!
