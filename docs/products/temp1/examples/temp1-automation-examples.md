# Automation Examples using a TEMP-1

###### Freezer Temperature Probe Example

This will guide you through how to setup an automation using the temperature probe in your freezer!

1\. Place the temperature probe into your freezer (not the entire TEMP-1, just the probe!) and then wait for it to normalize around 0 degrees F aka -18C.

2\. Once normalized, look at the graph and determine a good value to set for both the maximum and minimum temperatures. My mini freezer seems to max out at 30F so I would want to go slightly above that range. However, <a href="https://www.energy.gov/energysaver/refrigerator-freezer-use-and-temperature-tips" target="_blank" rel="noreferrer nofollow noopener">in most freezers they should NOT reach above 0F</a> so you will likely need to input a lower value than me. my minimums are around -20F.

![](assets/temp-1-temp-probe-ex-automation-pic-1.png)

3\. We now need to convert F to C since the max and min temps are measured in Celsius. My new values I will input are max probe temp 2C and a min probe temp of -30C. Reminder, yours will likely be different values, especially your max probe temp.

![](assets/temp-1-temp-probe-ex-automation-pic-2.png)

4\. The automation is now ready to be created -

5\. Click Settings -&gt; Automations & scenes -&gt; click Create Automation in the bottom left then "create new automation".

[Click here to go straight there!](http://homeassistant.local:8123/config/automation/edit/new){        .md-button .md-button--primary }

6\. Click Add Trigger then Entity then Numeric state and search for your temp-1 device such as "temp-1 max probe temp" then in the box labeled "Above" type in the max probe temp number you found in step 2 above.

7\.

&nbsp;

&nbsp;

&nbsp;

??? example "This will guide you through setting up the food probe to alert you when your target temperature is met!"

    ###### Food Probe Example

    1\. Head to Settings -&gt; Automations & scenes -&gt;then click Create Automation in the bottom left.[Click here to go straight there!](http://homeassistant.local:8123/config/automation/edit/new){        .md-button .md-button--primary }

    2\. testing

&nbsp;

###### Food Probe Example

This will guide you through setting up the food probe to alert you when your desired food temperature is met.

1\. Click Settings -&gt; Automations & scenes -&gt; click Create Automation in the bottom left.

[Click here to go straight there!](http://homeassistant.local:8123/config/automation/edit/new){        .md-button .md-button--primary }

2\. testing