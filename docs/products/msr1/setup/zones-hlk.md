---
description: "Tune the MSR-1 mmWave radar over Bluetooth with the HLKRadarTool phone app, covering both auto-calibration and manual gate settings."
---
# How To Tune mmWave Using HLKRadarTool

**Auto-Calibration (Average, Maximum, and Intelligent)**   
1\. Download the HLKRadarTool app for either [Android ](https://play.google.com/store/apps/details?id=com.hlk.hlkradartool&hl=en_US≷=US)or [Apple](https://apps.apple.com/us/app/hlkradartool/id1638651152)  
  
2\. Ensure the mmWave radar you want to tune has Radar Control Bluetooth turned on. Home Assistant > Settings > Devices & services > ESPHome Devices > Select Device > Scroll down and toggle on Radar Control Bluetooth  
  
![Radar Control Bluetooth switch turned on in the MSR-1 Home Assistant device page, outlined in red](/assets/radar-control-bluetooth.png)  
  
3\. Open the app and select your device  
  
![HLKRadarTool Device list showing the HLK-LD2410 radar found over Bluetooth](/assets/find-device.png)  
  
4\. Turn on Engineering Mode  
  
![HLKRadarTool device screen with the Engineering mode toggle turned on and outlined in red](/assets/em.png)  
  
5\. Select More and then select Parameter settings  
  
![HLKRadarTool device screen with More and Parameter settings outlined in red](/assets/more-and-ps.png)  
  
6\. Select Detect background noise  
  
![HLKRadarTool Parameter settings with Detect background noise outlined in red](/assets/dbn.png)  
  
7\. Insert Delay detection and Detection time values. (For iPhone users Delay detection cannot be 0). Then select Start. This will give us our reference values so we can auto-calibrate the mmWave sensor.  
  
![HLKRadarTool Bottom noise statistics with Delay detection, Detection time, and START outlined in red](/assets/dd-dt-and-start.png)  
  
8\. Select Back to navigate to the Parameter settings. Then select one of the auto-calibration buttons.  
  
**Average** - Sets the gate sensitivity to the average move and still energy
![HLKRadarTool Parameter settings with the Average one click setting button outlined in red](/assets/average.png)  
  
**Maximum** - Sets the gate sensitivity to the maximum move and still energy
  
![HLKRadarTool Parameter settings with the Maximum one click setting button outlined in red](/assets/max.png)  
  
**Intelligent** - Sets the gate sensitivity equal to or just above the maximum move and still energ**y** **![HLKRadarTool Parameter settings with the Intelligent one click setting button outlined in red](/assets/intelligent.png)** 9. Now your mmWave should be tuned to your environment! **Manual Calibration** 1. Follow steps 1-5 above  
  
2\. Select Motion or Static sensitivity, change it to your desired value, and select Set  
  
![HLKRadarTool gate sensitivity table with motion and static values and the Set button outlined in red](/assets/manual.png)  
  
3\. Now your mmWave should be tuned to your environment!