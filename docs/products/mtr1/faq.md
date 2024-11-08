1\. What sensors are included in the MTR-1?

•	The MTR-1 includes a multi-target mmWave radar sensor for detecting motion and positioning, as well as LUX, UV, temperature, and pressure sensors. There’s also an optional CO2 sensor available.

2\. How does the mmWave radar sensor work?

•	The MTR-1’s mmWave radar sensor tracks movement by emitting radar waves and detecting changes in reflected signals. This sensor can detect multiple targets and their locations within a room, offering more precise tracking than traditional motion sensors. It can even detect through light walls.

3\. How many targets can the MTR-1 track?

•	The MTR-1 can track up to three targets simultaneously, allowing it to monitor multiple people in a room and provide their positions within defined zones.

4\. What is the maximum detection range of the mmWave radar?

•	The mmWave radar sensor in the MTR-1 has a maximum detection range of 6 meters (about 19.6 feet), making it ideal for monitoring large rooms or spaces.

5\. Can the MTR-1 be used to track the exact location of people in a room?

•	Yes, the MTR-1 can detect people’s positions within zones, such as distinguishing if someone is near a door, on the couch, or standing by the kitchen counter. This enables precise automation based on a person’s location within the room.

6\. What is the benefit of the LUX and UV sensor?

•	The LUX sensor measures the ambient light in the room, while the UV sensor tracks ultraviolet light exposure. This data can be used for automations like adjusting lighting levels, or providing alerts when sunlight is strong.

7\. How does the optional CO2 sensor work?

•	The optional CO2 sensor measures the concentration of carbon dioxide in the air, which is important for monitoring air quality in enclosed spaces. High CO2 levels can lead to poor sleep, drowsiness, and other health issues, and the sensor can trigger automations to turn on fans or open windows.

8\. What are some common use cases for the MTR-1?

•	The MTR-1 can be used to automate lights based on people’s presence in a room, trigger alarms or notifications when someone enters a space, and adjust HVAC settings based on CO2 levels. Its precise tracking capabilities also make it great for monitoring multiple zones within a room, such as distinguishing when someone is at the stove versus the sink.

9\. How do I connect the MTR-1 to Home Assistant?

•	The MTR-1 connects to Home Assistant through ESPHome using WiFi. Once connected, you can access data from all the sensors and create automations based on the sensor readings.

10\. What kind of automations can I set up with the MTR-1?

•	You can create automations for turning lights on/off based on motion, adjusting air filtration when CO2 levels rise, and sending notifications when specific zones (like doorways) detect movement. The multi-target tracking allows for even more advanced automations, such as adjusting lights depending on where people are in the room.

11\. How do I adjust the sensitivity of the motion detection?

•	Sensitivity can NOT be adjusted via the ESPHome configuration. The MTR-1 LD2450 mmWave sensor cannot be tuned like the MSR-2 can. The MTR-1 can set zones and track multiple users instead.

12\. Can the MTR-1 detect motion through walls?

•	Yes, the mmWave radar in the MTR-1 can detect movement through certain materials, such as light walls or thin furniture, though you may need to adjust the sensitivity to prevent false positives from nearby rooms.

13\. Can the MTR-1 be used outdoors?

•	While the MTR-1 is primarily designed for indoor use, with proper weatherproofing and environmental protection, it could be used in sheltered outdoor environments. Be cautious of exposure to moisture or extreme weather.

14\. Does the MTR-1 work with other smart home platforms?

•	The MTR-1 is designed to work seamlessly with Home Assistant via ESPHome. While it could potentially be integrated into other smart home platforms through custom configurations, its primary use case is for Home Assistant.

15\. How does the temperature and pressure sensor work?

•	The temperature and pressure sensor provides accurate measurements for air temperature and barometric pressure. This data can be used in automations, such as controlling heating/cooling systems or monitoring environmental conditions.

16\. How is the MTR-1 powered?

•	The MTR-1 is powered through a USB-C connection and can be plugged into a standard wall outlet using a 5V adapter.

17\. What is the purpose of the RGB LED and piezo buzzer?

•	The RGB LED can display different colors for various events or alerts, such as turning red when air quality is poor or green for general notifications. The piezo buzzer can be used for sound alerts, such as a beep when motion is detected or a CO2 level warning.

18\. Can I customize the MTR-1’s features?

•	Yes, the MTR-1 is fully customizable through ESPHome. You can modify sensor settings, change reporting intervals, adjust sensitivity, and create custom automations based on the sensor readings.

19\. What is the reporting frequency of the MTR-1’s sensors?

•	The reporting frequency for each sensor can be adjusted through the ESPHome YAML configuration. You can choose to report data as frequently as every second or extend the intervals to reduce power consumption.

20\. Can I use multiple MTR-1 sensors in my smart home setup?

•	Yes, you can integrate multiple MTR-1 sensors into your Home Assistant system. Each will show up as a separate entity, allowing you to monitor multiple rooms or areas in your home simultaneously.

21\. What’s the difference between the MTR-1 and MSR-2?

•	The MTR-1 features multi-target radar tracking, allowing it to detect multiple people in a room and track their positions. The MSR-2, on the other hand, is designed more for single-target detection and has a slightly different sensor set, though both sensors offer robust environmental monitoring capabilities.

22\. What accessories are available for the MTR-1?

•	Accessories for the MTR-1 include mounting brackets, stands, and a variety of expansion options, like additional sensor modules. These allow for greater flexibility in where and how you use the sensor.

23\. What are the primary advantages of the MTR-1 over other motion sensors?

•	The MTR-1’s mmWave radar is significantly more advanced than traditional PIR (Passive Infrared) motion sensors. It can detect subtle movements, track multiple targets, and monitor precise locations within a room, making it ideal for sophisticated home automations. Its additional sensors (LUX, UV, temperature, pressure, optional CO2) also provide greater environmental awareness.

24\. How do I install the MTR-1?

•	Installation is simple. The MTR-1 is powered via USB-C and connects to your WiFi. From there, you configure it through ESPHome and integrate it into your Home Assistant setup. Detailed instructions are available on our documentation wiki, and we offer support via our Discord community.

25\. How secure is the MTR-1?

•	The MTR-1 operates entirely on your local network, using ESPHome, which means no data is sent to external servers. This ensures that your home automation data remains private and secure.

26\. Does the MTR-1 require cloud connectivity?

•	No, the MTR-1 works entirely within your local network through Home Assistant and ESPHome. You don’t need cloud access or a subscription to use the sensor.

27\. How do I update the firmware on the MTR-1?

•	Firmware updates for the MTR-1 can be done directly through ESPHome. When updates are available, you can install them wirelessly over-the-air (OTA), making it simple to keep the sensor up to date.

28\. What is the warranty on the MTR-1?

•	The MTR-1 comes with a one-year warranty. If you encounter any issues, we provide comprehensive support via email, Discord, or our website to ensure you’re fully satisfied with the product.

29\. How long does it take to set up the MTR-1?

•	Setup is quick and easy. Most users report being able to configure and integrate the MTR-1 into their Home Assistant setup within 10-15 minutes.

30\. What’s in the box?

•	Each MTR-1 package includes the assembled board, case, support stand, and a link to documentation, open-source code, and CAD models. Additionally, you’ll receive an Apollo Automation sticker.