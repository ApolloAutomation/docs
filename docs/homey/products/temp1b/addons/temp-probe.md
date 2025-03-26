# TEMP-1B Temp Probe

The TEMP-1B comes with an optional temp probe which can be used to monitor a fridge, freezer, fish tank, pool, hot tub, etc. It includes a protected cable but the TEMP-1 itself needs to stay in a cool environment.

1\. To use your temp probe simply take it out of the package and insert it into the 3.5mm port on your TEMP-1B.

![](assets/temp-probe-insert-1.jpg)

![](assets/temp-probe-fully-inserted.jpg)

2\. Once inserted, proceed to step 3 unless you have a battery in it

!!! tip "If you are using it with a battery you need to push the reset button."

    The TEMP-1B looks for the temp probe when it boots and if it is not there then the sensor is marked as failed and will not work properly in Home Assistant. You need to click the reset button if you have a battery in it or power cycle your TEMP-1B to make it reliably use the new food temperature probe.

&nbsp;

![](assets/temp1b-temp-probe-pic-1.jpg)

3\. Go to the device page of your TEMP-1B in Home Assistant and choose probe "Dallas" aka Temperature.

![](assets/temp1b-temp-probe-pic-1-1.png)

!!! danger "Do not leave your sensor outside or let it get wet!"

    The TEMP-1B should not be left outside for long periods of time or allowed to get wet. You will need to use another case around your TEMP-1B if there will be high moisture content in the air or if it is expected to rain.

**Example images of the long temperature probe in a mini freezer:**

![](assets/temp1b-temp-probe-freezer-pic-1.jpg)

![](assets/temp1b-temp-probe-freezer-pic-2.jpg)