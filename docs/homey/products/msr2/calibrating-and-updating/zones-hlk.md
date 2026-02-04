# How To Tune mmWave Using HLKRadarTool

**Auto-Calibration (Average, Maximum, and Intelligent)**   
1\. Download the HLKRadarTool app for either [Android ](https://play.google.com/store/apps/details?id=com.hlk.hlkradartool&hl=en_US≷=US)or [Apple](https://apps.apple.com/us/app/hlkradartool/id1638651152)

- The default password to connect to the HLKRadarTool is HiLink

2\. Ensure the mmWave radar you want to tune has Radar Control Bluetooth turned on. Home Assistant > Settings > Devices & services > ESPHome Devices > Select Device > Scroll down and toggle on Radar Control Bluetooth  
  
![Radar Control Bluetooth.png](../../../../assets/homey-products-msr2-calibrating-and-updating-radar-control-bluetooth.png)  
  
3\. Open the app and select your device  
  
![Find Device.png](../../../../assets/homey-products-msr2-calibrating-and-updating-find-device.png)  
  
4\. Turn on Engineering Mode  
  
![EM.png](../../../../assets/homey-products-msr2-calibrating-and-updating-em.png)  
  
5\. Select More and then select Parameter settings  
  
![More and PS.png](../../../../assets/homey-products-msr2-calibrating-and-updating-more-and-ps.png)  
  
6\. Select Detect background noise  
  
![DBN.png](../../../../assets/homey-products-msr2-calibrating-and-updating-dbn.png)  
  
7\. Insert Delay detection and Detection time values. (For iPhone users Delay detection cannot be 0). Then select Start. This will give us our reference values so we can auto-calibrate the mmWave sensor.  
  
![DD, DT and Start.png](../../../../assets/homey-products-msr2-calibrating-and-updating-dd-dt-and-start.png)  
  
8\. Select Back to navigate to the Parameter settings. Then select one of the auto-calibration buttons.  
  
**Average** - Sets the gate sensitivity to the average move and still energy
![Average.png](../../../../assets/homey-products-msr2-calibrating-and-updating-average.png)  
  
**Maximum** - Sets the gate sensitivity to the maximum move and still energy
  
![Max.png](../../../../assets/homey-products-msr2-calibrating-and-updating-max.png)  
  
**Intelligent** - Sets the gate sensitivity equal to or just above the maximum move and still energ**y** **![Intelligent.png](../../../../assets/homey-products-msr2-calibrating-and-updating-intelligent.png)** 9. Now your mmWave should be tuned to your environment! **Manual Calibration** 1. Follow steps 1-5 above  
  
2\. Select Motion or Static sensitivity, change it to your desired value, and select Set  
  
![Manual.png](../../../../assets/homey-products-msr2-calibrating-and-updating-manual.png)  
  
3\. Now your mmWave should be tuned to your environment!