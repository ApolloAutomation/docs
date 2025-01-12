# How To Change The Update Frequency Of Sensors

1\. Select the ESPHome Builder in the sidebar then click "EDIT" on the device you want to change.

![](assets/update-frequency-pic-1.png)

2\. Insert the YAML for the sensor you want to edit(The example below is for our AIR-1 SEN55 sensor).

```yaml
sensor:
  - platform: sen5x
    id: !extend sen55
    update_interval: 5s
```

3\. In the top right of the same screen click "SAVE" and then "INSTALL".

4\. Once you see "INFO OTA successful" you are done. Click "STOP" to exit.

![](assets/update-frequency-pic-3.png)