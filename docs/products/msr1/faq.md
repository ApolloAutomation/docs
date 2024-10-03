1\. What sensors are included in the MSR-1?

•	The MSR-1 includes a mmWave radar sensor (HLK-ld2410b), a LUX and UV sensor (LTR-390UV), and a temperature, humidity, and pressure sensor (BME280). It also has an optional CO2 sensor (SCD40), RGB LED, and piezo buzzer.

2\. What does the mmWave radar sensor do?

•	The mmWave radar sensor detects motion, even subtle movements. It can be used for automation tasks like turning on lights when someone enters a room or keeping them on while someone is sitting still. It’s also effective for detecting presence in spaces like beds or workstations.

3\. How does the MSR-1 connect to Home Assistant?

•	The MSR-1 connects to Home Assistant through ESPHome using WiFi. Once connected, you can configure automations, monitor sensor data, and customize settings from Home Assistant.

4\. Does the MSR-1 require any cloud service or subscription?

•	No, the MSR-1 is fully local and does not rely on cloud services or subscriptions. It operates entirely within your Home Assistant setup, ensuring privacy and data security.

5\. What are the use cases for the MSR-1?

•	The MSR-1 is versatile and can be used for various home automation tasks, such as detecting when someone enters a room to turn on lights, monitoring CO2 levels, measuring sunlight (UV) to optimize plant care, or providing notifications using the RGB LED or piezo buzzer.

6\. What does the optional CO2 sensor measure?

•	The optional CO2 sensor (SCD40) tracks carbon dioxide levels, which can affect air quality and personal comfort. High CO2 levels can cause drowsiness, poor sleep, and brain fog. The sensor can notify you when it’s time to open a window or increase ventilation.

7\. How does the RGB LED work?

•	The RGB LED on the MSR-1 can be used for visual notifications. For example, it can turn red when CO2 levels are high, green for trash night, or blue when the mail arrives. These alerts can be fully customized using Home Assistant.

8\. Can the piezo buzzer be customized?

•	Yes, the piezo buzzer can be programmed to emit different beep patterns based on events. For instance, you can set it to beep when the front door opens, when the CO2 levels rise, or even play a fun tune for a party.

9\. What is the purpose of the LUX and UV sensors?

•	The LUX and UV sensors (LTR-390UV) help monitor light levels and UV exposure. You can use these sensors to control indoor lighting based on natural light conditions or to track the amount of sunlight in a specific area, such as near plants.

10\. How accurate are the temperature and humidity readings?

•	The MSR-1 uses the BME280 sensor for temperature, humidity, and pressure. It provides accurate readings, but keep in mind that the ESP32-C3 processor generates some heat, which may require a temperature offset for the most precise measurements.

11\. What does the pressure sensor do?

•	The pressure sensor enhances the accuracy of CO2 readings by accounting for changes in atmospheric pressure. This helps provide more reliable air quality data.

12\. How do I install the MSR-1?

•	Installation is straightforward. The MSR-1 is powered via a USB-C cable connected to a standard power adapter. Once powered on, it can be configured through Home Assistant using ESPHome.

13\. Can I customize the MSR-1?

•	Yes, the MSR-1 is fully customizable. We provide open-source code and CAD files for you to modify and enhance. You can create automations, adjust sensor settings, and modify reporting intervals based on your needs.

14\. What is the mmWave detection range?

•	The mmWave radar sensor can detect movement up to 5 meters (16.4 feet) with a detection angle of about 60 degrees (though in practice, this can be close to 90 degrees). It’s excellent for detecting both large and small movements, making it suitable for automations like turning on lights or detecting presence in a room.

15\. Can the mmWave sensor detect through walls?

•	Yes, mmWave sensors can detect movement through walls, depending on the material and thickness. This means you may need to fine-tune the sensor’s settings to prevent false positives or adjust its placement to avoid unwanted detections.

16\. How do I set up automations with the MSR-1?

•	Automations can be easily configured in Home Assistant using ESPHome. For example, you can automate lights to turn on when motion is detected or trigger a fan when CO2 levels rise. The sensor data can be used in combination with other Home Assistant devices for more complex automations.

17\. What is the power source for the MSR-1?

•	The MSR-1 is powered via USB-C. Simply plug it into a standard 5V USB power adapter, and you’re good to go.

18\. What is the reporting interval for the MSR-1 sensors?

•	The reporting interval is adjustable via ESPHome. You can configure the sensors to report data as frequently as every second or set longer intervals depending on your specific needs.

19\. Can I use the MSR-1 outdoors?

•	The MSR-1 is designed for indoor use. While it could be used outdoors in a sheltered environment, it is not weatherproof. If you plan to use it outdoors, make sure to protect it from the elements.

20\. What is the maximum number of targets for the mmWave sensor?

•	The mmWave sensor on the MSR-1 is designed to detect a single target at a time. It is excellent for recognizing motion within a specific area, such as a room, and keeping track of when someone is present.

21\. What is the Exposed GPIO feature on the MSR-1?

•	The Exposed GPIO feature provides access to the GPIO pins, 3v, 5v, and I2C on the back of the MSR-1 board. This allows you to expand its capabilities by adding external sensors or other components. For example, you could add an external temperature sensor or other I2C devices.

22\. How do I update the firmware on the MSR-1?

•	Firmware updates are done over-the-air (OTA) using ESPHome. You can update the firmware directly through Home Assistant when new versions are available.

23\. Does the MSR-1 support Bluetooth tracking?

•	Yes, the MSR-1 has Bluetooth tracking capabilities through the ESP32-C3 chip. You can track Bluetooth devices such as phones, tablets, or beacons. This allows for automations based on proximity, such as turning on lights when you walk into a room with your phone.

24\. How do I calibrate the CO2 sensor?

•	The optional CO2 sensor (SCD40) comes pre-calibrated, so no manual calibration is necessary. However, you can perform recalibration via ESPHome if needed.

25\. How can I use the MSR-1 for light control?

•	The MSR-1’s LUX sensor can be used to control indoor lighting. For example, you can set up automations to only turn on lights when motion is detected and the room is dark. The UV sensor can also help you track sunlight exposure, which is useful for managing indoor plant care.

26\. Does the MSR-1 work with other smart home platforms besides Home Assistant?

•	The MSR-1 is designed to work with Home Assistant through ESPHome. While it may be possible to integrate it with other platforms using MQTT or custom configurations, Home Assistant remains the primary platform for full functionality.

27\. What are some creative automation ideas using the MSR-1?

•	The MSR-1 offers endless automation possibilities. You can:

•	Use the mmWave sensor to automate lights based on motion and presence.

•	Use the RGB LED to indicate specific events (e.g., trash night or mail delivery).

•	Trigger the piezo buzzer for notifications, such as when CO2 levels are too high or when a door opens.

•	Use the LUX sensor to control lights based on sunlight levels.

28\. What’s included in the MSR-1 package?

•	The MSR-1 package includes the assembled board, case, and links to our documentation, open-source code, and CAD models. You’ll also get an Apollo Automation sticker as a little bonus.

29\. What’s the difference between the MSR-1 and MSR-2?

•	The MSR-2 is an incremental update based on user feedback. It includes a compact design, improved sensor accuracy (such as a DPS310 pressure sensor), and an additional expansion slot for future accessories. The MSR-1 remains supported, but the MSR-2 is the recommended choice for new users.

30\. How do I get support for the MSR-1?

•	You can get support through our Discord community, where you can ask questions and share your experiences with other users and the Apollo Automation team. We also provide extensive documentation on our GitHub and wiki pages.

&nbsp;