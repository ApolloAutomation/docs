1\. **What sensors are included in the AIR-1?**

* The AIR-1 uses a SEN55 which includes sensors for PM1, PM2.5, PM4, PM10 (particulate matter), <a href="https://sensirion.com/media/documents/02232963/6294E043/Info_Note_VOC_Index.pdf" target="_blank" rel="noreferrer nofollow noopener">VOC Index</a> (volatile organic compounds), <a href="https://sensirion.com/media/documents/9F289B95/6294DFFC/Info_Note_NOx_Index.pdf" target="_blank" rel="noreferrer nofollow noopener">NOx Index </a>(nitrogen oxides), temperature, and humidity. Addon sensors include the <a href="https://sensirion.com/products/catalog/SCD40" target="_blank" rel="noreferrer nofollow noopener">SCD40 CO2</a> and the <a href="https://wiki.dfrobot.com/_SKU_SEN0377_Gravity__MEMS_Gas_Sensor_CO__Alcohol__NO2___NH3___I2C___MiCS_4514" target="_blank" rel="noreferrer nofollow noopener">MiCS gas sensor</a>.

2\. **What does the AIR-1 measure?**

* The AIR-1 measures a variety of air quality metrics, including particulate matter (dust, pollen, etc.), VOCs, NOx, temperature, and humidity. The optional CO2 sensor can track carbon dioxide levels, and the pressure sensor helps provide more accurate CO2 readings.

3\. **How do I connect the AIR-1 to Home Assistant?**

* The AIR-1 connects via WiFi to ESPHome on Home Assistant, enabling data monitoring, automations, and alerts directly within Home Assistant.

4\. **Does the AIR-1 require cloud connectivity or a subscription?**

* No, the AIR-1 is fully local and does not require any cloud services or subscriptions. All data is processed and stored locally via your Home Assistant setup, ensuring privacy and control over your data.

5\. **What are common use cases for the AIR-1?**

* The AIR-1 is ideal for monitoring indoor air quality, such as tracking dust levels in woodworking shops, ensuring optimal air quality during sleep, or automating air purifiers when certain thresholds are met. The CO2 sensor is particularly useful for identifying high CO2 levels, which can affect sleep and concentration.

6\. **How do I set up automations with the AIR-1?**

* Using Home Assistant, you can set up automations based on the AIR-1’s sensor readings. For example, you can automate an HVAC fan to run when CO2 levels are high, or trigger notifications when particulate matter reaches unhealthy levels.

7\. **How does the optional CO2 sensor work?**

* The optional SCD40 CO2 sensor measures carbon dioxide levels and helps you understand when CO2 concentrations in a room become too high, which can cause fatigue, drowsiness, and worse for humans and pets alike. It’s particularly useful in offices, bedrooms, and other enclosed spaces.

8\. **What is particulate matter (PM) and why is it important?**

* Particulate matter (PM) refers to tiny particles in the air that can be harmful when inhaled. The AIR-1 measures various sizes of particulate matter (PM1, PM2.5, PM4, PM10), helping you track dust, pollen, and other particles that affect air quality. It’s especially useful for people with allergies or respiratory conditions.

9\. **What is VOC and why should I monitor it?**

* VOCs (volatile organic compounds) are chemicals that can be emitted from everyday items like cleaning products, paints, and furniture. Prolonged exposure to high levels of VOCs can affect indoor air quality and health. The AIR-1’s VOC sensor helps you monitor these levels and take action when necessary, such as increasing ventilation.

10\. **What is the NOx Index and why is it measured?**

* NOx (nitrogen oxides) are harmful gases that contribute to air pollution and can affect respiratory health. The AIR-1 gives an <a href="https://sensirion.com/media/documents/9F289B95/6294DFFC/Info_Note_NOx_Index.pdf" target="_blank" rel="noreferrer nofollow noopener">NOx index number</a>, allowing you to keep track of indoor air quality and make adjustments if necessary. "The NO x Index describes the current NO x condition in a room relative to the sensor’s recent history. In this way, the NO x Index behaves like a human nose. "

11\. **How accurate are the air quality readings from the AIR-1?**

* The AIR-1 uses a high-quality SEN55 sensor with a 10-year lifespan, designed for continuous use. Its readings are highly accurate for particulate matter, VOC Index, and NOx Index. However, keep in mind that the ESP32-C3 generates some heat, which may require you to apply a temperature and humidity offset.

12\. **How can I use the RGB LED for notifications?**

* The RGB LED on the AIR-1 can be customized to show different colors for different events. For example, you can set it to flash red when air quality is poor, green on trash night, or blue when CO2 levels are safe. You can configure these notifications through Home Assistant.

13\. **How do I update the firmware on the AIR-1?**

* Firmware updates can be done over-the-air (OTA) using ESPHome. You will receive notifications when new firmware is available, and you can install updates directly through Home Assistant.

14\. **How do I calibrate the CO2 sensor?**

* The CO2 sensor comes pre-calibrated, so you don’t need to perform any manual calibration. However, you can recalibrate the sensor through ESPHome if needed.

15\. **Does the AIR-1 work outdoors?**

* The AIR-1 is primarily designed for indoor use. It could be used outdoors in a sheltered environment, but it is not weatherproof. If you need outdoor air quality monitoring, ensure the device is protected from the elements.

16\. **What is the power source for the AIR-1?**

* The AIR-1 is powered via a USB-C connection. It can be plugged into any standard wall outlet using a 5V adapter.

17\. **How does the pressure sensor help with CO2 readings?**

* The barometric pressure sensor (DPS310) enhances the accuracy of CO2 readings by compensating for changes in altitude and atmospheric pressure, ensuring more reliable measurements of CO2 levels in different environments.

18\. **My AIR-1 CO2 sensors are having a sawtooth pattern, is there any explanation?**

* Some users have noticed the AIR-1 with the "Apollo" side facing up will produce strange behavior with the CO2 sensor readings fluctuating way more than they should. Simply turning the AIR-1 to the other side makes this problem go away!

19\. **Can I integrate multiple AIR-1 sensors in my smart home?**

* Yes, you can have multiple AIR-1 sensors in your Home Assistant setup. Each sensor will be recognized as a separate entity, allowing you to monitor air quality across different rooms or spaces simultaneously.

20\. **How customizable is the AIR-1?**

* The AIR-1 is fully customizable via ESPHome. You can adjust sensor settings, create automations, modify reporting intervals, and even customize the RGB LEDs. Additionally, we provide open-source CAD drawings and code for further customization.

21\. **How frequently does the AIR-1 report data?**

* The reporting frequency for each sensor is adjustable via ESPHome but most default to 60 seconds. You can choose to have data reported as frequently as every second, or adjust intervals to save power and reduce data traffic.

22\. **Does the AIR-1 require specific software?**

* The AIR-1 is designed to work seamlessly with Home Assistant through ESPHome. All configuration, monitoring, and automation setups are done through these platforms.

23\. **Is the AIR-1 compatible with other smart home platforms?**

* While the AIR-1 is optimized for Home Assistant and ESPHome, you may be able to integrate it into other smart home platforms using custom configurations or MQTT, but Home Assistant remains the primary platform.

24\. **What’s the difference between the AIR-1 and other air quality sensors?**

* The AIR-1 is unique because it offers local control with no cloud or subscription required. It also provides a wide range of sensor data (PM, VOC, NOx, CO2, temperature, humidity) in a compact, affordable package. The addition of the RGB LEDs and open-source nature makes it highly customizable.

25\. **What are the optional add-ons for the AIR-1?**

* The AIR-1 offers two optional add-ons: a <a href="https://sensirion.com/products/catalog/SCD40" target="_blank" rel="noreferrer nofollow noopener">SCD40 CO2</a> sensor and the <a href="https://wiki.dfrobot.com/_SKU_SEN0377_Gravity__MEMS_Gas_Sensor_CO__Alcohol__NO2___NH3___I2C___MiCS_4514" target="_blank" rel="noreferrer nofollow noopener">MiCS gas sensor</a>. These can be added to enhance air quality monitoring with very accurate CO2 measurements and the ability to detect multiple gases with the MiCS gas sensor.

26\. **What’s in the box?**

* The AIR-1 comes with the fully assembled board and case, a USB-C power cable, and access to all our documentation, open-source code, and CAD models. You’ll also receive a sticker of Apollo, our mascot.

27\. **How do I install the AIR-1?**

* Installation is easy. Simply plug the AIR-1 into a wall outlet using the USB-C cable, connect it to your Home Assistant through ESPHome, and configure the settings as desired. <a href="https://wiki.apolloautomation.com/products/general/setup/getting-started-air1/" target="_blank" rel="noreferrer nofollow noopener">Detailed setup instructions are available in our documentation</a>.

28\. **What is the warranty on the AIR-1?**

* The AIR-1 comes with a one-year warranty. If you encounter any issues, we provide support via email, Discord, and our community channels to ensure you’re satisfied with the product.

29\. **Can the AIR-1 be used to monitor 3D printer fumes?**

* Yes, the AIR-1 can monitor air quality around 3D printers, especially particulate matter (PM) and VOCs emitted during the printing process. It can trigger alerts or automations when levels become unhealthy.

30\. **How long does it take to set up the AIR-1?**

* Setup typically takes around 5-10 minutes. Once powered and connected to WiFi, it can be configured quickly through ESPHome and Home Assistant.

31\. **How secure is the AIR-1?**

* The AIR-1 operates entirely on your local network and does not send data to the cloud. All information is processed and stored locally, ensuring the security and privacy of your home automation setup.

32\. **Can I use the AIR-1 for safety monitoring (e.g., CO2 or gas leaks)?**

* The AIR-1’s CO2 and gas sensors are intended for air quality monitoring but **DO NOT MEET** the safety standards for CO2 or gas leak detection as defined by the NBIC, NFPA, or IFC. For safety purposes, dedicated gas or CO2 monitors should be used.