# Sensor Definitions

Once added to Home Assistant you can configure different settings for your sensor. Below is what each setting does.

### Controls

- **RGB Light**
    - 3 RGB Neopixels. Click on the light bulb to change the color. Click on the toggle to turn on or off
- **Calibrate SCD40**  
    
    - Refer to the [CO2 calibration guide](https://wiki.apolloautomation.cloud/books/general/page/co2-calibration). Place your sensor outside and click this button to calibrate the CO2 levels

### Sensors

- **Ammonia**
    - Measurement from MiCS-4514 gas sensor
- **Carbon Monoxide**
    - Measurement from MiCS-4514 gas sensor
- **CO2**
    - True CO2 reading from the SCD40. This will be Unknown if you do not have the CO2 module. This can be calibrated following this guide but does come precalibrated: [Here](https://wiki.apolloautomation.cloud/books/general/page/co2-calibration)
- **DPS310 Pressure**
    - Atmospheric pressure, used to better calibrate the SCD40 CO2 module
- **DPS310 Temperature**
    - A worse measurement of temperature. This is more susceptible to internal heat buildup. Please use the SEN55 temperature
- **ESP Temperature**
    - This is the temperature of the internal ESP chip. Think of it like your measured CPU temp on your PC
- **Ethanol**
    - Measurement from MiCS-4514 gas sensor
- **Hydrogen**
    - Measurement from MiCS-4514 gas sensor
- **Methane**
    - Measurement from MiCS-4514 gas sensor
- **Nitrogen Dioxide**
    - Measurement from MiCS-4514 gas sensor
- **PM < 10 µM**
    - Measurement of particulates **smaller** than 10 µM
- **PM < 1 µM**
    - Measurement of particulates **smaller** than 1 µM
- **PM < 2.5 µM**
    - Measurement of particulates **smaller** than 2.5 µM
- **PM < 4 µM**
    - Measurement of particulates **smaller** than 4 µM
- **SEN55 Humidity**
    - Humidity measurement from SEN55, will be most accurate
- **SEN55 NOX**
    - Measurement of nitrogen oxides from the SEN55
- **SEN55 Temperature**
    - Measurement of temperature from the SEN55, will be most accurate
- **SEN55 VOC**
    - VOC index from the SEN55
- **VOC Quality**
    - This uses the VOC index and a scale to output an easier to use variable 
        - 0-79: Improved
        - 80-119: Normal
        - 120-199: Abnormal
        - 200-299: Very abnormal
        - 300+: Extremely abnormal
- **PM 0.3 To 1 µm**  
    
    - Disabled by default but can be enabled in HA. Shows particulate count that are from 0.3 to 1.0 µm
- **PM 1 To 2.5 µm**  
    
    - Disabled by default but can be enabled in HA. Shows particulate count that are from 1 to 2.5 µm
- **PM 2.5 To 4 µm**  
    
    - Disabled by default but can be enabled in HA. Shows particulate count that are from 2.5 to 4.0 µm
- **PM 4 To 10 µm**  
    
    - Disabled by default but can be enabled in HA. Shows particulate count that are from 4.0 to 10.0 µm

### Configuration

- **ESP Reboot**
    - Performs a restart of the sensor
- **SEN55 Temperature Offset**
    - Allows you to calibrate the SEN55 temperature. Please refer to our [calibration guide](https://wiki.apolloautomation.cloud/books/msr-1/page/msr-1-temperature-humidity-offsets "MSR-1 Temperature & Humidity Offsets")
- **SEN55 Humidity Offset**
    - Allows you to calibrate the SEN55 humidity. Please refer to our [calibration guide](https://wiki.apolloautomation.cloud/books/msr-1/page/msr-1-temperature-humidity-offsets "MSR-1 Temperature & Humidity Offsets")
- Startup Light Blink

    - Controls if the led blinks after power on when trying to connect to HA

![AIR-1 Sensor Data.jpg](../assets/air-1-sensor-data.jpg)