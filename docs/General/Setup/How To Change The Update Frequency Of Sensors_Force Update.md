# How To Change The Update Frequency Of Sensors/Force Update

 1. Navigate to the ESPHome addon  
  
 2. Select the Edit button under the desired device

![ESPHome Edit Button.png](../assets/esphome-edit-button.png)

 3. Insert your code (The example below is for our AIR-1 SEN55 sensor)

```
sensor:
  - platform: sen5x
    id: !extend sen55
    update_interval: 5s
```

![SEN55 update interval.png](../assets/sen55-update-interval.png)   
 4. In the top right of the same screen Select Save and then Install   
  
 5. If it compiles correctly then you should see a green Success

![Install Success.png](../assets/install-success.png)

 6. When you see the sensor logs, you are finished and can select Stop

![Sensor Log Stop.png](../assets/sensor-log-stop.png)

 7. Now your sensor value should update!  
  
**Force Update**

Follow the same steps above but use this code to force the sensor to update.

```
sensor:
- platform: sen5x
  id: !extend sen55
  nox:
    name: "SEN55 NOX"
    force_update: True
```