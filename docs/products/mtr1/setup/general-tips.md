# General Tips

##### **MTR-1 PCB with Sensors**

![20240501_155316.jpg](../assets/20240501-155316.jpg)![20240501_155130.jpg](../assets/20240501-155130.jpg)![20240501_155248.jpg](../assets/20240501-155248.jpg)

&nbsp;

&nbsp;

##### **Light Sensor (LTR-390UV)**

![Screenshot 2024-04-30 at 5.42.54 PM.png](../assets/screenshot-2024-04-30-at-5-42-54-pm.png)

When mounting the MTR-1 be sure to position the device so that the large hole at the top is not covered. This allows more light to enter and will ensure better accuracy

The onboard RGB LED will trigger the light sensor. Be cognizant of this when making automations based on light/LUX.

##### **Mounting**

![Screenshot 2024-04-30 at 5.51.36 PM.png](../assets/screenshot-2024-04-30-at-5-51-36-pm.png)

##### **LD2450 Performance and Electrical Parameters**

##### [**LD2450 Datasheet**](https://www.tinytronics.nl/index.php?route=product/product/get_file&amp;file=6000/HLK-LD2450-Instruction-Manual.pdf)

![Screenshot 2024-04-30 at 5.53.09 PM.png](../assets/screenshot-2024-04-30-at-5-53-09-pm.png)

##### **Expanding Horizontal Distance as Target Moves Further Away**

The detection is 60 degrees from center on each side. So it is a cone when you are close to it but at 4 feet away to the side you might not be visible. If you are further from the wall it can detect further in a horizontal distance.

![image.png](../assets/9jtimage.png)

##### **Increased ESP Temperature**

If you are experiencing higher than normal ESP temperatures ~140+ degrees F then changing the wifi power save mode option might help decrease the temperature. Here is the link to the ESPHome WiFi Component [Power Save Mode](https://esphome.io/components/wifi.html#power-save-mode).

**Power Save Mode** The WiFi interface of all ESPs offer three power save modes to reduce the amount of power spent on WiFi. While some options can reduce the power usage of the ESP, they generally also decrease the reliability of the WiFi connection, with frequent disconnections from the router in the highest power saving mode.

NONE (least power saving, Default for ESP8266)<br> LIGHT (Default for ESP32)<br> HIGH (most power saving)

```
wifi:
  # ...
  power_save_mode: none
```

The code above can be added to the devices .yaml through the ESPHome addon edit button.

(Thank you for the suggestion, Brian!)<br> (Referenced from ESPHome website)