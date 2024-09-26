# How To Add Temp And Humidity From SCD40

1\. Navigate to the ESPHome addon  
  
 2. Select the Edit button under the desired device

![ESPHome Edit Button.png](../assets/esphome-edit-button_1.png)

 3. Insert your code (The example below is for our AIR-1 SEN55 sensor but this applies to MSR-1/2, MTR or any sensor with the CO2 module)

```
sensor:
  - platform: scd4x
    id: !extend scd40 
    temperature:
      name: "SCD40 Temperature"
    humidity:
      name: "SCD40 Humidity"
```

![Screenshot 2024-05-20 at 8.49.17â€¯PM.png](../assets/screenshot-2024-05-20-at-8-49-17-pm.png)   
 4. In the top right of the same screen Select Save and then Install   
  
 5. If it compiles correctly then you should see a green Success

![Install Success.png](../assets/install-success_1.png)

 6. When you see the sensor logs, you are finished and can select Stop

![Sensor Log Stop.png](../assets/sensor-log-stop_1.png)

 7. Now your sensor value should update!