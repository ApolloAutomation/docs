---
title: AIR-1 FAQ
description: "Answers to common questions about the AIR-1 air quality sensor with Homey: sensors, connecting to Homey, flows, CO2 calibration, firmware, and troubleshooting."
---
# AIR-1 FAQ

1\. **What sensors are included in the AIR-1?**

* The AIR-1 uses a SEN55 which includes sensors for PM1, PM2.5, PM4, PM10 (particulate matter), <a href="https://sensirion.com/media/documents/02232963/6294E043/Info_Note_VOC_Index.pdf" target="_blank" rel="noreferrer nofollow noopener">VOC Index</a> (volatile organic compounds), <a href="https://sensirion.com/media/documents/9F289B95/6294DFFC/Info_Note_NOx_Index.pdf" target="_blank" rel="noreferrer nofollow noopener">NOx Index </a>(nitrogen oxides), temperature, and humidity. Addon sensors include the <a href="https://sensirion.com/products/catalog/SCD40" target="_blank" rel="noreferrer nofollow noopener">SCD40 CO2</a> and the <a href="https://wiki.dfrobot.com/_SKU_SEN0377_Gravity__MEMS_Gas_Sensor_CO__Alcohol__NO2___NH3___I2C___MiCS_4514" target="_blank" rel="noreferrer nofollow noopener">MiCS gas sensor</a>.

2\. **What does the AIR-1 measure?**

* The AIR-1 measures a variety of air quality metrics, including particulate matter (dust, pollen, etc.), VOCs, NOx, temperature, and humidity. The optional CO2 sensor can track carbon dioxide levels.

3\. **How do I connect the AIR-1 to Homey?**

* The AIR-1 joins your Wi-Fi, and the Apollo Automation app for Homey talks to it directly over your local network through the ESPHome native API, with no cloud account. Once you add it, its readings show up on the device in Homey, ready for flows and Insights. The app runs on Homey Pro; Homey Cloud isn't supported.

!!! success "Next step: add your AIR-1 to Homey"

    Connect the sensor to your Wi-Fi through its hotspot, then add it with the Apollo Automation app. The getting started guide walks you through both.

    [Get started with Homey](../../general/setup/getting-started-air1/){ .md-button .md-button--primary }

4\. **Does the AIR-1 require cloud connectivity or a subscription?**

* No, the AIR-1 is fully local and does not require any cloud services or subscriptions. It talks to Homey directly over your local network, so your data stays in your home and under your control.

5\. **What are common use cases for the AIR-1?**

* The AIR-1 is ideal for monitoring indoor air quality, such as tracking dust levels in woodworking shops, ensuring optimal air quality during sleep, or automating air purifiers when certain thresholds are met. The CO2 sensor is particularly useful for identifying high CO2 levels, which can affect sleep and concentration.

6\. **How do I set up flows with the AIR-1?**

* Any AIR-1 reading can start a flow in Homey. For example, run an HVAC fan when CO2 levels are high, or send a notification when particulate matter reaches unhealthy levels. The [high CO2 notification example](../../general/tutorials/high-co2-notification-example/) walks you through one.

7\. **How does the optional CO2 sensor work?**

* The optional SCD40 CO2 sensor measures carbon dioxide levels and helps you understand when CO2 concentrations in a room become too high, which can cause fatigue, drowsiness, and worse for humans and pets alike. It’s particularly useful in offices, bedrooms, and other enclosed spaces.

8\. **What is particulate matter (PM) and why is it important?**

* Particulate matter (PM) refers to tiny particles in the air that can be harmful when inhaled. The AIR-1 measures various sizes of particulate matter (PM1, PM2.5, PM4, PM10), helping you track dust, pollen, and other particles that affect air quality. It’s especially useful for people with allergies or respiratory conditions.

9\. **What is VOC and why should I monitor it?**

* VOCs (volatile organic compounds) are chemicals that can be emitted from everyday items like cleaning products, paints, and furniture. Prolonged exposure to high levels of VOCs can affect indoor air quality and health. The AIR-1’s VOC sensor helps you monitor these levels and take action when necessary, such as increasing ventilation.

10\. **What is the NOx Index and why is it measured?**

* NOx (nitrogen oxides) are harmful gases that contribute to air pollution and can affect respiratory health. The AIR-1 gives an <a href="https://sensirion.com/media/documents/9F289B95/6294DFFC/Info_Note_NOx_Index.pdf" target="_blank" rel="noreferrer nofollow noopener">NOx index number</a>, allowing you to keep track of indoor air quality and make adjustments if necessary. "The NO x Index describes the current NO x condition in a room relative to the sensor’s recent history. In this way, the NO x Index behaves like a human nose. "

11\. **How accurate are the air quality readings from the AIR-1?**

* The AIR-1 uses a high-quality SEN55 sensor with a 10-year lifespan, designed for continuous use. Its readings are highly accurate for particulate matter, VOC Index, and NOx Index. However, keep in mind that the ESP32-C3 generates some heat, which may require you to apply a temperature and humidity offset. Set it with **SEN55 temperature offset** and **SEN55 humidity offset** under **Calibration offsets** in the device's **Settings** in the Homey app.

12\. **My AIR-1 never shows a DPS310 pressure reading in Homey. Is something wrong?**

* No, your device is fine. A small subset of units shipped without the DPS310 sensor because the part was discontinued by the manufacturer. If your AIR-1 never reports a pressure value, your unit is one of these. Every other sensor on the device works normally.

13\. **How can I use the RGB LED for notifications?**

* The RGB LED is the AIR-1's light in Homey. Turn it on or off, dim it, or change its color from the device or in a flow: for example, turn it red when air quality is poor, green on trash night, or blue when CO2 levels are safe.
* On current firmware, the LED can also follow air quality by itself. Choose **NowCast AQI**, **CO2**, or **VOC Index** under **Air Quality LED Source** on the sensor's own web page: in a browser, open `http://apollo-air-1-xxxxxx.local`, where `xxxxxx` is the last 6 characters of the device's name in Homey. This setting isn't in Homey.

14\. **How do I update the firmware on the AIR-1?**

* Homey doesn't install firmware updates: the Apollo Automation app has no update action. On current firmware, the AIR-1's own web page has a **Firmware Update** button that downloads and installs the latest release over Wi-Fi. Open `http://apollo-air-1-xxxxxx.local` in a browser, where `xxxxxx` is the last 6 characters of the device's name in Homey, and press it. The sensor needs internet access to download the update.
* You can also flash the latest firmware over USB with the Apollo installer, as described in [Factory re-flash AIR-1](../troubleshooting/air1-code/).

15\. **How do I calibrate the CO2 sensor?**

* You usually don't need to. The latest AIR-1 firmware enables automatic self-calibration, which keeps the SCD40 accurate as long as the sensor sees fresh air (about 420 ppm) at least once a week.
* If your AIR-1 sits in a space that rarely gets fresh air (a sealed office, a basement, a grow room), turn automatic self-calibration off and calibrate by hand every 1 to 2 years instead. The **CO2 Auto Calibration** switch isn't in Homey: turn it off on the sensor's own web page (see question 13 for the address). Then follow the [manual calibration guide](../../general/calibrating-and-updating/co2-calibration/), which uses the **Calibrate SCD40 to 420 ppm** maintenance action in the device's **Settings** in Homey.

16\. **Does the AIR-1 work outdoors?**

* The AIR-1 is primarily designed for indoor use. It could be used outdoors in a sheltered environment, but it is not weatherproof. If you need outdoor air quality monitoring, ensure the device is protected from the elements.

17\. **What is the power source for the AIR-1?**

* The AIR-1 is powered via a USB-C connection. It can be plugged into any standard wall outlet using a 5V adapter.

18\. **My AIR-1 CO2 sensors are having a sawtooth pattern, is there any explanation?**

* Some users have noticed the AIR-1 with the "Apollo" side facing up will produce strange behavior with the CO2 sensor readings fluctuating way more than they should. Turning the AIR-1 to the other side makes this problem go away!

19\. **Can I integrate multiple AIR-1 sensors in my smart home?**

* Yes. Add each AIR-1 with the Apollo Automation app. Each one shows up as its own device in Homey with its own readings, so you can monitor air quality across different rooms or spaces at the same time.

20\. **How customizable is the AIR-1?**

* The AIR-1 is fully customizable via ESPHome. You can adjust sensor settings, create automations, modify reporting intervals, and even customize the RGB LEDs. Additionally, we provide open-source CAD drawings and code for further customization.

21\. **How frequently does the AIR-1 report data?**

* By default, the SEN55 readings (particulate matter, VOC Index, NOx Index, temperature, and humidity) update every 10 seconds, pressure every 30 seconds, and CO2 and the MiCS gas readings every 60 seconds. These intervals are set in the AIR-1 firmware, and Homey has no setting for them, so changing an interval means editing the firmware with ESPHome.

22\. **Does the AIR-1 require specific software?**

* With Homey, you need the Apollo Automation app, which adds the AIR-1 and its readings to Homey. Monitoring and flows all happen in Homey from there.

23\. **Is the AIR-1 compatible with other smart home platforms?**

* Yes. Besides Homey (through the Apollo Automation app), the AIR-1 works with Home Assistant and with other platforms that support the <a href="https://esphome.io/components/api.html" target="_blank" rel="noreferrer nofollow noopener">ESPHome API</a>. See [Supported platforms](../../general/supported-platforms/).

24\. **What's the difference between the AIR-1 and other air quality sensors?**

* The AIR-1 is unique because it offers local control with no cloud or subscription required. It also provides a wide range of sensor data (PM, VOC, NOx, CO2, temperature, humidity) in a compact, affordable package. The addition of the RGB LEDs and open-source nature makes it highly customizable.

25\. **What are the optional addons for the AIR-1?**

* The AIR-1 offers two optional addons: an <a href="https://sensirion.com/products/catalog/SCD40" target="_blank" rel="noreferrer nofollow noopener">SCD40 CO2</a> sensor and the <a href="https://wiki.dfrobot.com/_SKU_SEN0377_Gravity__MEMS_Gas_Sensor_CO__Alcohol__NO2___NH3___I2C___MiCS_4514" target="_blank" rel="noreferrer nofollow noopener">MiCS gas sensor</a>. These can be added to enhance air quality monitoring with very accurate CO2 measurements and the ability to detect multiple gases with the MiCS gas sensor.

26\. **What's in the box?**

* The AIR-1 comes with the fully assembled board and case, a USB-C power cable, and access to all our documentation, open-source code, and CAD models. You'll also receive a sticker of Apollo, our mascot.

27\. **How do I install the AIR-1?**

* Plug the AIR-1 into a wall outlet using the USB-C cable, connect it to your Wi-Fi through its hotspot, and add it in Homey with the Apollo Automation app. The [getting started guide](../../general/setup/getting-started-air1/) walks you through each step.

28\. **What is the warranty on the AIR-1?**

* The AIR-1 comes with a one-year warranty. If you encounter any issues, we provide support via email, Discord, and our community channels to ensure you're satisfied with the product.

29\. **Can the AIR-1 be used to monitor 3D printer fumes?**

* Yes, the AIR-1 can monitor air quality around 3D printers, especially particulate matter (PM) and VOCs emitted during the printing process. It can trigger alerts or flows when levels become unhealthy.

30\. **How long does it take to set up the AIR-1?**

* Setup typically takes around 5 to 10 minutes: once the AIR-1 is powered and connected to Wi-Fi, you add it in Homey with the Apollo Automation app.

31\. **How secure is the AIR-1?**

* The AIR-1 operates entirely on your local network and does not send data to the cloud. All information is processed and stored locally, ensuring the security and privacy of your home automation setup.

32\. **Can I use the AIR-1 for safety monitoring (e.g., CO2 or gas leaks)?**

* The AIR-1's CO2 and gas sensors are intended for air quality monitoring but **DO NOT MEET** the safety standards for CO2 or gas leak detection as defined by the NBIC, NFPA, or IFC. For safety purposes, dedicated gas or CO2 monitors should be used.

33\. **My NOx Index never shows a value and the logs mention an SEN54. How do I fix it?**

* A small number of AIR-1 units report their sensor as an SEN54, which has no NOx element, on the model register, even though the NOx-capable SEN55 is actually fitted and working. That left the NOx Index without a value. The 26.7.23.1 firmware forces the correct SEN55 model, so updating to the latest firmware (see question 14) brings NOx back. Once it updates, give the reading a little time to appear: like the VOC Index, the NOx Index needs a short conditioning period after boot before it reports a value.

34\. **Is the connection between the AIR-1 and Homey encrypted?**

* When the AIR-1 has an API encryption key, yes. Homey asks for the key when you add the device and only connects with it. If the key changes later, open the device's **Settings** in Homey, choose **Repair**, and enter the new key. A device without a key connects without encryption, on your local network only.

35\. **I build the AIR-1 YAML myself and validation fails on a version error. What do I need?**

* Firmware 26.7.23.1 needs ESPHome 2026.7.2 or newer, and firmware 26.10.8.1 and later need ESPHome 2026.8.0 or newer. Update ESPHome Device Builder and validate again. Firmware installed with the **Firmware Update** button or the Apollo installer isn't affected, since those builds are compiled for you.
